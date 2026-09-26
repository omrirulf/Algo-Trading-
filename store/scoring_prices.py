"""A night's scoring prices, as the archive keeps them.

``analysis/price_tape.py`` hands over the prices a race or funds run scored
with -- every bar every price source handed out, and their SHA-256, which
the run's committed output carries as ``prices_sha256``. The workflows that
make those runs hold no credential, so they pass the table on as an
artifact, and ``.github/workflows/scoring-prices.yml`` (which holds the
Supabase key) brings it here.

Two tables, so a year of nights does not store a year of copies:

* ``scoring_prices``: each distinct bar once -- keyed on the SHA-256 of what
  it says (kind, ticker, date, open, high, low, close, dividends). A bar that
  reads the same tonight as last night is not stored again; a bar the vendor
  revised is a new row beside the old one. Each row says which run first
  saw it and when that ticker was fetched.
* ``scoring_runs``: one row per run -- who scored (``race-gate``, ``funds``,
  ``race-report``), the GitHub run id, the last final close, the hash, the
  number of rows and, per source and ticker, the first and last date and
  the bar count (``coverage``).

A night is rebuilt from those two by taking, for each source and ticker in
``coverage``, the bars of that kind between its first and last date as they
stood when the run first saw them; the result must hash to the run's
``prices_sha256`` (the committed one), or it is not that night's table. The
one case that rebuild cannot tell apart -- a bar revised and then revised
back -- the hash catches, and the artifact (90 days) holds the exact table.

Pure: validates and builds rows. Nothing here touches the network.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from typing import Any, Optional

from analysis.price_tape import ROW_KEYS, SOURCE, TAPE_VERSION, digest
from config.redaction import credential_shape

#: The consumers a tape may name. Anything else is not one of ours.
CONSUMERS = ("race-gate", "race-report", "funds")

_TICKER = re.compile(r"[A-Z0-9.^=-]{1,15}")
_DAY = re.compile(r"\d{4}-\d{2}-\d{2}")
_KINDS = ("close", "ohlc")


class TapeError(ValueError):
    """The hand-over is not a tape this archive will store."""


def load(text: str) -> dict[str, Any]:
    """Parse and check one tape. Raises ``TapeError`` with the reason.

    Checked hard because it arrives as an artifact: it is handed from one
    workflow to another, and only a table that hashes to its own
    ``prices_sha256`` and is shaped like prices is let into the archive.
    """
    try:
        tape = json.loads(text)
    except (json.JSONDecodeError, TypeError) as exc:
        raise TapeError(f"not JSON: {exc}") from exc
    if not isinstance(tape, dict) or tape.get("kind") != "scoring-prices" or tape.get("v") != TAPE_VERSION:
        raise TapeError("not a scoring-prices tape of this version")
    if tape.get("consumer") not in CONSUMERS:
        raise TapeError("unknown consumer")
    rows = tape.get("rows")
    if not isinstance(rows, list):
        raise TapeError("no rows")
    for row in rows:
        if not isinstance(row, dict) or set(row) != set(ROW_KEYS):
            raise TapeError("a row is not shaped like a price")
        if row["kind"] not in _KINDS or not _TICKER.fullmatch(str(row["ticker"])) \
                or not _DAY.fullmatch(str(row["date"])):
            raise TapeError("a row names no valid kind, ticker or date")
        for key in ("open", "high", "low", "close", "dividends"):
            value = row[key]
            if value is not None and (isinstance(value, bool) or not isinstance(value, (int, float))):
                raise TapeError(f"a row's {key} is not a number")
    if digest(rows) != tape.get("prices_sha256"):
        raise TapeError("the rows do not hash to prices_sha256")
    if credential_shape(json.dumps({k: v for k, v in tape.items() if k != "rows"})) is not None:
        raise TapeError("the tape looks like it holds a credential")
    return tape


def price_key(row: dict[str, Any]) -> str:
    """The content key of one bar: what it says, not which source said it."""
    content = {k: row.get(k) for k in ("kind", "ticker", "date", "open", "high", "low", "close", "dividends")}
    return hashlib.sha256(json.dumps(content, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def price_rows(tape: dict[str, Any], run_id: Optional[str]) -> list[dict[str, Any]]:
    """Each distinct bar in the tape once, as ``scoring_prices`` rows."""
    fetched = {
        (name, ticker): info.get("fetched_at")
        for name, part in (tape.get("coverage") or {}).items() if isinstance(part, dict)
        for ticker, info in (part.get("tickers") or {}).items() if isinstance(info, dict)
    }
    out: dict[str, dict[str, Any]] = {}
    for row in tape["rows"]:
        key = price_key(row)
        if key in out:
            continue
        out[key] = {
            "price_key": key,
            "ingested_at": _now(),
            "kind": row["kind"],
            "ticker": row["ticker"],
            "bar_date": row["date"],
            "open": row["open"],
            "high": row["high"],
            "low": row["low"],
            "close": row["close"],
            # Not read by any scorer (every fetch is auto_adjust=False), so
            # never recorded; the column is there so the table says so.
            "adj_close": None,
            "dividends": row["dividends"],
            "source": tape.get("source") or SOURCE,
            "first_consumer": tape["consumer"],
            "first_run_id": run_id,
            "first_fetched_at": fetched.get((row["instance"], row["ticker"])),
        }
    return list(out.values())


def run_row(tape: dict[str, Any], run_id: Optional[str]) -> dict[str, Any]:
    """The tape's one ``scoring_runs`` row: the run, its hash, and what it covered."""
    run = run_id or "local"
    return {
        "run_key": f"{tape['consumer']}:{run}:{tape['prices_sha256'][:16]}",
        "ingested_at": _now(),
        "consumer": tape["consumer"],
        "run_id": run_id,
        "generated_at": tape.get("generated_at"),
        "final_through": tape.get("final_through"),
        "prices_sha256": tape["prices_sha256"],
        "rows": len(tape["rows"]),
        "coverage": tape.get("coverage") or {},
    }


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


__all__ = ["CONSUMERS", "TapeError", "load", "price_key", "price_rows", "run_row"]
