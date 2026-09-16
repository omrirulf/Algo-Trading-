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
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx  # noqa: E402

from orchestrator import positioning  # noqa: E402

TIMEOUT = 45.0
NAME_FIELD = "market_and_exchange_names"
DATE_FIELD = "report_date_as_yyyy_mm_dd"


def _rows(dataset: str, where: str, limit: int = 2000) -> list[dict]:
    url = f"{positioning.BASE_URL}/{dataset}.json"
    params = {
        "$select": f"{NAME_FIELD},{DATE_FIELD}",
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


def newest_by_name(rows: list[dict]) -> dict[str, str]:
    """``{market name: newest report date}``."""
    newest: dict[str, str] = defaultdict(str)
    for row in rows:
        name = str(row.get(NAME_FIELD) or "")
        stamp = str(row.get(DATE_FIELD) or "")[:10]
        if name and stamp > newest[name]:
            newest[name] = stamp
    return dict(newest)


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


def audit() -> int:
    """Every mapped ticker, with the newest date its contract reports."""
    print("=== every mapping in CONTRACTS ===")
    dead = []
    for ticker in sorted(positioning.CONTRACTS):
        dataset, name = positioning.CONTRACTS[ticker]
        rows = _rows(dataset, f"upper({NAME_FIELD}) like '%{name.upper()}%'", limit=400)
        found = newest_by_name(rows)
        if not found:
            print(f"  {ticker:<6} NOTHING MATCHES {name!r}")
            dead.append(ticker)
            continue
        # A substring can match more than one market; show every one, because
        # two contracts interleaved is the failure this exists to expose.
        for market, stamp in sorted(found.items(), key=lambda kv: kv[1], reverse=True):
            print(f"  {ticker:<6} {stamp}  {market}")
        if len(found) > 1:
            print(f"  {'':<6} ^^ {len(found)} markets match {name!r} -- they interleave")
        newest = max(found.values())
        if newest < "2026-08-01":
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
    args = parser.parse_args(argv)
    if args.like:
        search(args.like)
        return 0
    return audit()


if __name__ == "__main__":
    raise SystemExit(main())
