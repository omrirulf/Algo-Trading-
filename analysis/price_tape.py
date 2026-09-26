"""The daily prices a night's scoring used, as one table and one hash.

The race and the funds score every trade against prices fetched from
yfinance that night. Those prices are not the record's to keep: a vendor
revises a bar, drops a row, or answers differently next month, and a result
that cannot be re-scored on the prices it was scored on cannot be checked.
So each nightly run can hand over exactly what it read (``--with-prices``):

* the table, every bar each price source handed out, in a fixed order;
* ``prices_sha256``, the SHA-256 of that table's rows as canonical JSON,
  which goes into the run's committed output as one new field.

The table travels as a workflow artifact and is copied into the archive by a
workflow that holds the key (``.github/workflows/scoring-prices.yml``); the
hash is in git, so a later check needs neither the archive nor the vendor
to prove it has the same prices -- only the table and this module.

Read-only and pure: it reads what the sources already cached and builds a
dict. Nothing that scores reads it, so no number a run prints can move.
"""

from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime
from typing import Any, Iterable, Optional

#: Bumped if a row's shape changes; the hash is only comparable within one.
TAPE_VERSION = 1

#: Every row has every key, in this order, so a row rebuilt from the archive
#: hashes exactly as the one written here. A close-only source leaves the
#: others null.
ROW_KEYS = ("instance", "kind", "ticker", "date", "open", "high", "low", "close", "dividends")

#: Where the prices came from. yfinance, unadjusted (``auto_adjust=False``).
SOURCE = "yfinance"


def _number(value: Any) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if math.isfinite(number) else None


def rows_and_coverage(instances: Iterable[tuple[str, Any]]) -> tuple[list[dict], dict[str, dict]]:
    """Every bar the named sources handed out, and which tickers each covered.

    ``instances`` are ``(name, source)`` pairs -- ``("closes", source)``,
    ``("ohlc", fetcher)`` -- in any order; the rows come back sorted by
    instance, ticker and date. A source with no ``recorded`` method (a
    test's stand-in) contributes nothing rather than failing the run.
    """
    rows: list[dict] = []
    coverage: dict[str, dict] = {}
    for name, source in instances:
        recorded = getattr(source, "recorded", None)
        if not callable(recorded):
            continue
        kind, bars, fetched_at = recorded()
        tickers: dict[str, dict] = {}
        for ticker in sorted(bars):
            dated = sorted(bars[ticker], key=lambda bar: bar["date"])
            for bar in dated:
                rows.append({
                    "instance": name, "kind": kind, "ticker": ticker, "date": bar["date"],
                    "open": _number(bar.get("open")), "high": _number(bar.get("high")),
                    "low": _number(bar.get("low")), "close": _number(bar.get("close")),
                    "dividends": _number(bar.get("dividends")),
                })
            tickers[ticker] = {
                "first": dated[0]["date"] if dated else None,
                "last": dated[-1]["date"] if dated else None,
                "bars": len(dated),
                "fetched_at": fetched_at.get(ticker),
            }
        coverage[name] = {"kind": kind, "tickers": tickers}
    rows.sort(key=lambda row: (row["instance"], row["ticker"], row["date"]))
    return rows, coverage


def canonical_rows(rows: list[dict]) -> str:
    """The one JSON text the hash is taken over: rows in order, keys in ``ROW_KEYS`` order."""
    ordered = [{key: row.get(key) for key in ROW_KEYS} for row in rows]
    return json.dumps(ordered, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def digest(rows: list[dict]) -> str:
    """``prices_sha256``: the SHA-256 of ``canonical_rows(rows)``."""
    return hashlib.sha256(canonical_rows(rows).encode("ascii")).hexdigest()


def tape(instances: Iterable[tuple[str, Any]], *, consumer: str, final_through: Any,
         generated_at: datetime) -> dict[str, Any]:
    """The whole hand-over: who scored, through which close, the hash, and the rows."""
    rows, coverage = rows_and_coverage(instances)
    return {
        "kind": "scoring-prices",
        "v": TAPE_VERSION,
        "consumer": consumer,
        "source": SOURCE,
        "generated_at": generated_at.isoformat(),
        "final_through": final_through.isoformat() if hasattr(final_through, "isoformat") else final_through,
        "prices_sha256": digest(rows),
        "coverage": coverage,
        "rows": rows,
    }


def dumps(value: dict[str, Any]) -> str:
    """The tape as one line of JSON: what ``--with-prices`` prints last."""
    return json.dumps(value, separators=(",", ":"), allow_nan=False)


__all__ = ["ROW_KEYS", "SOURCE", "TAPE_VERSION", "canonical_rows", "digest", "dumps",
           "rows_and_coverage", "tape"]
