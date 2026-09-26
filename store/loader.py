"""Turn log lines into database rows, without ever losing one.

The loader is deliberately dull. It reads a JSON-lines file, extracts the
columns worth indexing, keeps the original line verbatim alongside them, and
inserts. Everything interesting about it is a consequence of one decision:
**the log file is the record, this is an index over it.**

That decision buys three properties:

* *Idempotence.* Rows are keyed on a content hash of the source line, so
  loading a journal that has grown by one line inserts one row. The natural
  way to run this is "after every cycle", over a file that is append-only and
  almost entirely unchanged, and that has to be cheap and safe.
* *Tolerance.* A truncated final line from a killed process, or a line written
  by an older schema, is counted and skipped -- exactly as the file-based
  reader treats it. A bad line must never abort a load over months of good
  data.
* *Agreement.* Journal rows are built from ``analysis.reader.entry_from``,
  the same parser the file-based scorer uses. Two parsers over one format
  drift, and the drift surfaces as a report that disagrees with the file it
  came from. There is one parser.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Optional

from analysis.reader import SCORE_FIELDS, entry_from, parse_timestamp
from config import journal_files


@dataclass
class LoadResult:
    """What one load did. Every line is accounted for in exactly one bucket."""

    #: Rows newly written.
    inserted: int = 0
    #: Lines already present, identified by content hash. The normal case when
    #: re-loading an append-only file.
    duplicates: int = 0
    #: Lines that were not valid JSON, or not shaped like a record.
    skipped: int = 0

    @property
    def total(self) -> int:
        return self.inserted + self.duplicates + self.skipped

    def __add__(self, other: "LoadResult") -> "LoadResult":
        return LoadResult(
            inserted=self.inserted + other.inserted,
            duplicates=self.duplicates + other.duplicates,
            skipped=self.skipped + other.skipped,
        )

    def describe(self, what: str) -> str:
        return (
            f"{what}: {self.inserted} new, {self.duplicates} already loaded, "
            f"{self.skipped} unreadable ({self.total} lines)"
        )


def line_hash(raw: str) -> str:
    """Content key for a source line.

    A hash rather than a natural key because there is no natural key: a journal
    line is identified by everything in it. Two byte-identical lines are the
    same event -- ``ts_utc`` carries microseconds, so a genuine repeat of a
    ticker in a cycle cannot collide with itself.
    """
    return hashlib.sha256(raw.strip().encode("utf-8")).hexdigest()


# --------------------------------------------------------------------------- #
# Row construction
# --------------------------------------------------------------------------- #


def signal_row(raw: str) -> Optional[dict[str, Any]]:
    """One journal line as a row, or None if unreadable."""
    payload = _load_json(raw)
    if payload is None:
        return None
    entry = entry_from(payload)
    if entry is None:
        return None

    signal = _dict(payload.get("signal"))
    outcome = _dict(payload.get("outcome"))
    usage = _dict(payload.get("usage"))
    fx = _dict(payload.get("fx"))

    row: dict[str, Any] = {
        "line_hash": line_hash(raw),
        "ingested_at": _now(),
        "ts_utc": entry.timestamp.isoformat() if entry.timestamp else None,
        "ts_exact": int(entry.timestamp_is_exact),
        "trade_date": entry.timestamp.date().isoformat() if entry.timestamp else None,
        "ticker": entry.ticker,
        "bias": entry.bias,
        "conviction": entry.conviction,
        "rationale": _text(signal.get("rationale")),
        "outcome_status": entry.outcome_status,
        "outcome_reason": _text(outcome.get("reason")),
        "outcome_quantity": _integer(outcome.get("quantity")),
        "order_id": _text(outcome.get("order_id")),
        "error": entry.error,
        "gap_count": len(entry.gaps),
        "model": _text(usage.get("model")),
        "input_tokens": _integer(usage.get("input_tokens")),
        "output_tokens": _integer(usage.get("output_tokens")),
        "cost_usd": _number(usage.get("cost_usd")),
        "fx_rate": _number(fx.get("rate")),
        "raw": raw.strip(),
    }
    row.update({name: entry.scores.get(name) for name in SCORE_FIELDS})
    return row


def execution_row(raw: str) -> Optional[dict[str, Any]]:
    """One ``execution_audit.log`` line as a row, or None if unreadable.

    Two kinds of line share the file. A ``signal_processed`` line carries
    the engine's verdict under ``result``. A ``position_managed`` line --
    the profit ladder and the stops (``app/position_manager.py``) -- carries
    its ticker under ``action`` and has no ``result`` at all, and until 26
    Sep 2026 this function dropped every one of them as unreadable: the
    remote archive held no record of a stop raised or a tranche sold. Such a
    line is now a row too, with ``status`` the action (``stop_raised``,
    ``tranche_taken``, ``held`` ...), ``quantity`` what it closed and
    ``stop_price`` the stop it left, and the whole line in ``raw``.

    Its order id is the ladder's own order (a partial close, a stop), never
    the entry order a journal line records, so the ``decisions`` join on
    order id does not pick these rows up.
    """
    payload = _load_json(raw)
    if payload is None:
        return None

    result = _dict(payload.get("result"))
    signal = _dict(payload.get("signal"))
    action = _dict(payload.get("action"))
    ticker = _text(result.get("ticker")) or _text(signal.get("ticker"))
    if not ticker and not result:
        ticker = _text(action.get("ticker"))
        if ticker:
            return _action_row(raw, payload, action, ticker)
    if not ticker:
        return None

    timestamp, exact = _execution_timestamp(payload, result)
    return {
        "line_hash": line_hash(raw),
        "ingested_at": _now(),
        "ts_utc": timestamp.isoformat() if timestamp else None,
        "ts_exact": int(exact),
        "trade_date": timestamp.date().isoformat() if timestamp else None,
        "ticker": ticker.upper(),
        "status": _text(result.get("status")),
        "reason": _text(result.get("reason")),
        "bias": _text(result.get("bias")) or _text(signal.get("bias")),
        "conviction": _number(result.get("conviction")),
        "quantity": _integer(result.get("quantity")),
        "side": _text(result.get("side")),
        "entry_price": _number(result.get("entry_price")),
        "stop_price": _number(result.get("stop_price")),
        "atr": _number(result.get("atr")),
        "order_id": _text(result.get("order_id")),
        "level": _text(payload.get("level")),
        "raw": raw.strip(),
    }


def _action_row(raw: str, payload: dict, action: dict, ticker: str) -> dict[str, Any]:
    """A ``position_managed`` line as an ``executions`` row. See ``execution_row``."""
    timestamp, exact = parse_timestamp(payload)
    return {
        "line_hash": line_hash(raw),
        "ingested_at": _now(),
        "ts_utc": timestamp.isoformat() if timestamp else None,
        "ts_exact": int(exact),
        "trade_date": timestamp.date().isoformat() if timestamp else None,
        "ticker": ticker.upper(),
        "status": _text(action.get("action")),
        "reason": _text(action.get("reason")),
        "bias": None,
        "conviction": None,
        "quantity": _integer(action.get("qty_closed")),
        "side": _text(action.get("side")),
        "entry_price": None,
        "stop_price": _number(action.get("new_stop")),
        "atr": None,
        "order_id": _text(action.get("order_id")),
        "level": _text(payload.get("level")),
        "raw": raw.strip(),
    }


def account_row(raw: str) -> Optional[dict[str, Any]]:
    """One ``logs/account.jsonl`` snapshot as an ``account_snapshots`` row, or None.

    The paper account as the heartbeat read it after a run
    (``app/account_snapshot.py``): cash, equity, the book, the resting
    stops and what filled since the last snapshot. The columns are the few
    numbers worth filtering on; the snapshot itself is ``raw``, verbatim.
    Remote only: the local index has no table for it.
    """
    payload = _load_json(raw)
    if payload is None:
        return None
    at = _text(payload.get("at"))
    moment = _instant(at)
    if moment is None:
        return None
    account = _dict(payload.get("account"))
    return {
        "line_hash": line_hash(raw),
        "ingested_at": _now(),
        "ts_utc": moment.isoformat(),
        "trade_date": moment.date().isoformat(),
        "mode": _text(payload.get("mode")),
        "sha": _text(payload.get("sha")),
        "equity": _number(account.get("equity")),
        "cash": _number(account.get("cash")),
        "long_market_value": _number(account.get("long_market_value")),
        "short_market_value": _number(account.get("short_market_value")),
        "last_equity": _number(account.get("last_equity")),
        "positions": _count(payload.get("positions")),
        "stops": _count(payload.get("stops")),
        "fills": _count(payload.get("fills")),
        "errors": _count(payload.get("errors")),
        "raw": raw.strip(),
    }


def fill_rows(raw: str) -> list[dict[str, Any]]:
    """Every fill in one account snapshot, as ``account_fills`` rows keyed on the broker's fill id.

    A fill is read by two snapshots when their windows overlap (on purpose,
    ``FILLS_OVERLAP``), with the same id both times, so the id is the key and
    the second copy is ignored on arrival. A fill with no id is left out: it
    cannot be told apart from its own repeat. Remote only, like the snapshot.
    """
    payload = _load_json(raw)
    fills = payload.get("fills") if payload is not None else None
    if not isinstance(fills, list):
        return []
    source = line_hash(raw)
    rows = []
    for fill in fills:
        if not isinstance(fill, dict):
            continue
        fill_id = _text(fill.get("id"))
        if not fill_id:
            continue
        moment = _instant(_text(fill.get("at")))
        rows.append({
            "fill_id": fill_id,
            "ingested_at": _now(),
            "ts_utc": moment.isoformat() if moment else None,
            "order_id": _text(fill.get("order_id")),
            "ticker": (_text(fill.get("ticker")) or "").upper() or None,
            "side": _text(fill.get("side")),
            "qty": _number(fill.get("qty")),
            "price": _number(fill.get("price")),
            "snapshot_hash": source,
        })
    return rows


def _execution_timestamp(payload: dict, result: dict) -> tuple[Optional[datetime], bool]:
    """Prefer the result's own UTC stamp over the formatter's local one.

    ``ExecutionResult.timestamp`` defaults to ``datetime.now(timezone.utc)``
    and is serialised with its offset. The formatter's ``ts`` is local time
    with no offset, which cannot say which side of a session close a decision
    fell on -- so it is a fallback, and one that is flagged as inexact.
    """
    raw_ts = result.get("timestamp")
    if isinstance(raw_ts, str):
        try:
            parsed = datetime.fromisoformat(raw_ts)
        except ValueError:
            parsed = None
        if parsed is not None:
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed.astimezone(timezone.utc), True
    # Same tz-naive fallback the journal reader applies, for the same reason.
    return parse_timestamp(payload)


# --------------------------------------------------------------------------- #
# Insertion
# --------------------------------------------------------------------------- #

_SIGNAL_COLUMNS = (
    "line_hash", "ingested_at", "ts_utc", "ts_exact", "trade_date", "ticker",
    "bias", "conviction", "rationale", "news_score", "technical_score",
    "fundamental_score", "analyst_score", "insider_score", "outcome_status",
    "outcome_reason", "outcome_quantity", "order_id", "error", "gap_count",
    "model", "input_tokens", "output_tokens", "cost_usd", "fx_rate", "raw",
)

_EXECUTION_COLUMNS = (
    "line_hash", "ingested_at", "ts_utc", "ts_exact", "trade_date", "ticker",
    "status", "reason", "bias", "conviction", "quantity", "side",
    "entry_price", "stop_price", "atr", "order_id", "level", "raw",
)


def load_signals(connection: sqlite3.Connection, lines: Iterable[str]) -> LoadResult:
    """Load journal lines into ``signals``."""
    return _load(connection, "signals", _SIGNAL_COLUMNS, lines, signal_row)


def load_executions(connection: sqlite3.Connection, lines: Iterable[str]) -> LoadResult:
    """Load audit lines into ``executions``."""
    return _load(connection, "executions", _EXECUTION_COLUMNS, lines, execution_row)


def load_file(connection: sqlite3.Connection, path: Path | str, kind: str) -> LoadResult:
    """Load one log file. A missing file is an empty load, not an error.

    The orchestrator writes the audit log only once a signal reaches the
    engine, so a journal can legitimately exist with no audit beside it.
    """
    path = Path(path)
    if not journal_files.exists(path):
        return LoadResult()
    loader = load_signals if kind == "signals" else load_executions
    # The journal's monthly files joined in order, or one plain file.
    return loader(connection, journal_files.iter_lines(path))


def _load(
    connection: sqlite3.Connection,
    table: str,
    columns: tuple[str, ...],
    lines: Iterable[str],
    build_row,
) -> LoadResult:
    rows: list[tuple] = []
    seen: set[str] = set()
    skipped = 0
    repeated = 0

    for line in lines:
        if not line.strip():
            continue
        row = build_row(line)
        if row is None:
            skipped += 1
            continue
        # A file can repeat a line within itself. ``executemany`` would count
        # the second one as inserted before the UNIQUE constraint absorbed it,
        # so it is held out here -- and counted, or ``total`` would silently
        # stop matching the number of lines read.
        if row["line_hash"] in seen:
            repeated += 1
            continue
        seen.add(row["line_hash"])
        rows.append(tuple(row[name] for name in columns))

    if not rows:
        return LoadResult(duplicates=repeated, skipped=skipped)

    placeholders = ", ".join("?" for _ in columns)
    statement = (
        f"INSERT OR IGNORE INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"
    )
    with connection:
        cursor = connection.executemany(statement, rows)
        inserted = cursor.rowcount if cursor.rowcount and cursor.rowcount > 0 else 0

    return LoadResult(
        inserted=inserted,
        duplicates=(len(rows) - inserted) + repeated,
        skipped=skipped,
    )


# --------------------------------------------------------------------------- #
# Coercion. Mirrors analysis.reader: return None rather than a wrong value.
# --------------------------------------------------------------------------- #


def _load_json(raw: str) -> Optional[dict]:
    try:
        payload = json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return None
    return payload if isinstance(payload, dict) else None


def _dict(value: Any) -> dict:
    return value if isinstance(value, dict) else {}


def _number(value: Any) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if number == number and abs(number) != float("inf") else None


def _integer(value: Any) -> Optional[int]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    if number != number or abs(number) == float("inf"):
        return None
    return int(number)


def _text(value: Any) -> Optional[str]:
    return value.strip() if isinstance(value, str) and value.strip() else None


def _count(value: Any) -> Optional[int]:
    return len(value) if isinstance(value, list) else None


def _instant(value: Optional[str]) -> Optional[datetime]:
    """An ISO-8601 instant in UTC; a value with no offset is taken as UTC. None if unreadable."""
    if not value:
        return None
    try:
        moment = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=timezone.utc)
    return moment.astimezone(timezone.utc)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()
