#!/usr/bin/env python3
"""Which CFTC contracts are still reporting, and under what name?

    python backtest/probe_cftc_contracts.py                 # every mapped ticker
    python backtest/probe_cftc_contracts.py --like TREASURY # search for a name

The live audit found TLT mapped to ULTRA U.S. TREASURY BONDS, whose most
recent row is dated February 2022. The mapping was not wrong when it was
written; the contract was renamed or delisted, and a substring query returns
the last rows it ever produced without complaint.

Two questions, then:

``--like``
    What is the exchange actually calling this thing now? Distinct market
    names matching a keyword, each with the date of its newest row, so a
    replacement is chosen from what reports today rather than from memory.

``--live``
    What does this dataset actually contain *this week*? ``--like`` can only
    find a contract whose new name still carries the old keyword, and the
    audit found a batch of unrelated majors -- every Treasury, the dollar
    index, NYMEX natural gas and NYMEX crude -- all stopping on the same
    date, 2022-02-01. Contracts are not delisted in batches on one day, and
    ``COPPER-GRADE #1`` becoming ``COPPER- #1`` on that date says what
    happened: the names were rewritten. So this lists every market still
    reporting, which is the only way to find a contract whose new name
    shares no keyword with its old one.

default
    Is every mapping still alive? The newest report date for each ticker
    already in ``CONTRACTS``, which is the check that would have caught TLT
    the day it went quiet.

A substring is deliberately *not* widened to fix a dead mapping: "U.S.
TREASURY BONDS" also matches "ULTRA U.S. TREASURY BONDS", and a query that
returns both interleaves two contracts into one series, which is a subtler
wrong answer than no answer.

Needs the open internet, so it runs on a runner. Read-only, no key, no LLM.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx  # noqa: E402

from orchestrator import positioning  # noqa: E402

TIMEOUT = 45.0
NAME_FIELD = "market_and_exchange_names"
DATE_FIELD = "report_date_as_yyyy_mm_dd"


def _rows(dataset: str, where: str, limit: int = 2000,
          select: tuple[str, ...] = (NAME_FIELD, DATE_FIELD)) -> list[dict]:
    url = f"{positioning.BASE_URL}/{dataset}.json"
    params = {
        "$select": ",".join(select),
        "$where": where,
        "$order": f"{DATE_FIELD} DESC",
        "$limit": str(limit),
    }
    try:
        response = httpx.get(url, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        payload = response.json()
    except Exception as exc:  # noqa: BLE001 - a probe reports, it does not raise
        print(f"    request failed: {type(exc).__name__}: {exc}")
        return []
    return [row for row in payload if isinstance(row, dict)]


OI_FIELD = "open_interest_all"


def newest_by_name(rows: list[dict]) -> dict[str, str]:
    """``{market name: newest report date}``."""
    newest: dict[str, str] = defaultdict(str)
    for row in rows:
        name = str(row.get(NAME_FIELD) or "")
        stamp = str(row.get(DATE_FIELD) or "")[:10]
        if name and stamp > newest[name]:
            newest[name] = stamp
    return dict(newest)


def newest_row_by_name(rows: list[dict]) -> dict[str, tuple[str, Optional[float]]]:
    """``{market name: (newest date, open interest on that date)}``.

    Open interest is how a benchmark is told from a look-alike: several
    exchanges list a contract on the same underlying, and the one the fund
    actually tracks is the one with the size.
    """
    best: dict[str, tuple[str, Optional[float]]] = {}
    for row in rows:
        name = str(row.get(NAME_FIELD) or "")
        stamp = str(row.get(DATE_FIELD) or "")[:10]
        if not name or stamp <= best.get(name, ("", None))[0]:
            continue
        try:
            interest = float(row.get(OI_FIELD))  # type: ignore[arg-type]
        except (TypeError, ValueError):
            interest = None
        best[name] = (stamp, interest)
    return best


def search(keyword: str) -> None:
    """Every market name containing ``keyword``, newest first."""
    keyword = keyword.upper()
    for dataset, label in ((positioning.FINANCIAL, "financial"),
                           (positioning.DISAGGREGATED, "commodity")):
        print(f"=== {label} dataset, names containing {keyword!r} ===")
        rows = _rows(dataset, f"upper({NAME_FIELD}) like '%{keyword}%'")
        found = newest_by_name(rows)
        if not found:
            print("    nothing matched")
            continue
        for name, stamp in sorted(found.items(), key=lambda kv: kv[1], reverse=True):
            print(f"    {stamp}  {name}")
        print()


#: Rows asked for when listing a dataset's live markets. Comfortably above
#: the few hundred markets either dataset reports in a week; if it is ever
#: reached the listing is truncated, and a truncated list of "everything
#: still reporting" is a wrong answer that reads like a right one, so it is
#: said out loud rather than trusted.
LIVE_LIMIT = 20000


def live(keyword: Optional[str] = None, today: Optional[date] = None) -> None:
    """Every market still reporting, by dataset, newest date first."""
    cutoff = (today or date.today()) - timedelta(days=positioning.MAX_REPORT_AGE_DAYS)
    where = f"{DATE_FIELD} >= '{cutoff.isoformat()}'"
    if keyword:
        where += f" AND upper({NAME_FIELD}) like '%{keyword.upper()}%'"
    for dataset, label in ((positioning.FINANCIAL, "financial"),
                           (positioning.DISAGGREGATED, "commodity")):
        title = f"=== {label} dataset, reporting since {cutoff.isoformat()}"
        print(f"{title}, names containing {keyword.upper()!r} ===" if keyword else f"{title} ===")
        rows = _rows(dataset, where, limit=LIVE_LIMIT, select=(NAME_FIELD, DATE_FIELD, OI_FIELD))
        if len(rows) >= LIVE_LIMIT:
            print(f"    !! {LIVE_LIMIT} rows returned -- the list below is TRUNCATED "
                  "and must not be read as complete")
        found = newest_row_by_name(rows)
        if not found:
            print("    nothing reporting")
            print()
            continue
        for name, (stamp, interest) in sorted(found.items()):
            size = f"{interest:>12,.0f}" if interest is not None else f"{'n/a':>12}"
            print(f"    {stamp}  {size}  {name}")
        print(f"    ({len(found)} markets, open interest on the newest row)")
        print()


def audit() -> int:
    """Every mapped ticker, with the newest date its contract reports."""
    cutoff = (date.today() - timedelta(days=positioning.MAX_REPORT_AGE_DAYS)).isoformat()
    print(f"=== every mapping in CONTRACTS (stale before {cutoff}) ===")
    dead = []
    for ticker in sorted(positioning.CONTRACTS):
        dataset, name = positioning.CONTRACTS[ticker]
        # Asked exactly as the cycle asks it. An audit that queries differently
        # from the code it audits is testing something nothing runs.
        rows = _rows(dataset, f"upper({NAME_FIELD}) = '{name.upper()}'", limit=400)
        found = newest_by_name(rows)
        if not found:
            print(f"  {ticker:<6} NOTHING REPORTS UNDER {name!r}")
            dead.append(ticker)
            continue
        # Exactly one market by construction; more would mean the query grew a
        # wildcard back, so it is still worth saying out loud.
        for market, stamp in sorted(found.items(), key=lambda kv: kv[1], reverse=True):
            print(f"  {ticker:<6} {stamp}  {market}  [{len(rows)} rows]")
        if len(found) > 1:
            print(f"  {'':<6} ^^ {len(found)} markets matched an EXACT name -- the query is not exact")
        if max(found.values()) < cutoff:
            dead.append(ticker)
    print()
    if dead:
        print(f"Stale or missing: {', '.join(dead)}")
    else:
        print("Every mapping is reporting.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--like", help="search for market names containing this")
    parser.add_argument("--live", nargs="?", const="", metavar="KEYWORD",
                        help="every market still reporting, optionally filtered by keyword")
    args = parser.parse_args(argv)
    if args.live is not None:
        live(args.live or None)
        return 0
    if args.like:
        search(args.like)
        return 0
    return audit()


if __name__ == "__main__":
    raise SystemExit(main())
