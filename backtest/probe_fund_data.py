#!/usr/bin/env python3
"""What does Yahoo actually put in a fund's payload?

    python backtest/probe_fund_data.py              # parsed, as the model sees it
    python backtest/probe_fund_data.py --raw        # the untouched JSON behind it
    python backtest/probe_fund_data.py --raw SPY TLT

The fund block was written against yfinance's *source*, which was enough to
learn the key names and nothing at all about the values behind them. The first
live run showed why that is not enough: XLE came back with a "P/E" of 0.06.
Yahoo stores several of those ratios inverted and lets its own formatter flip
them back, so reading ``raw`` gives an earnings yield wearing a P/E's name --
the exact failure mode ``orchestrator.funds`` exists to prevent, since a
number the model cannot use is worse than a stated blank.

This is the instrument for settling such questions with data instead of
guesses. It needs the open internet, so it runs on a runner, not locally.

Read-only. No orders, no LLM, no credentials.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import yfinance as yf  # noqa: E402

from orchestrator import analysts, flows, funds, holdings  # noqa: E402

#: One of each shape: two sector funds, a broad fund, a long-duration
#: Treasury fund, a credit fund, a non-US fund, and a commodity fund that
#: should have no block at all.
DEFAULT_TICKERS = ("XLE", "SMH", "SPY", "TLT", "HYG", "EWZ", "GLD")

#: Keys in ``info`` worth seeing next to the fund block. Yahoo spells yield
#: two ways and has changed which one is a fraction and which a percentage,
#: so both are printed rather than one being trusted.
INFO_KEYS = (
    "quoteType", "category", "longName", "yield", "dividendYield",
    "trailingPE", "annualReportExpenseRatio", "totalAssets", "navPrice",
    "threeYearAverageReturn", "beta3Year",
)


def dump_raw(ticker: str) -> None:
    """The quoteSummary modules yfinance parses, exactly as they arrive."""
    handle = yf.Ticker(ticker)
    data = handle.funds_data
    print(f"===== {ticker}: raw quoteSummary =====")
    try:
        payload = data._fetch()["quoteSummary"]["result"][0]
    except Exception as exc:  # noqa: BLE001 - a probe reports, it does not raise
        print(f"  fetch failed: {type(exc).__name__}: {exc}")
        return
    for module in ("topHoldings", "fundProfile"):
        section = payload.get(module)
        if section is None:
            print(f"  {module}: absent")
            continue
        print(f"  --- {module} ---")
        print(json.dumps(section, indent=2, default=str)[:6000])

    print("  --- info (selected) ---")
    try:
        info = handle.info or {}
    except Exception as exc:  # noqa: BLE001
        print(f"  info failed: {type(exc).__name__}: {exc}")
        return
    for key in INFO_KEYS:
        if key in info:
            print(f"    {key} = {info[key]!r}")


def dump_flows(handle: Any, ticker: str) -> None:
    """Today's share count, and which of the two ways it was arrived at.

    There is no series to check: Yahoo's fundamentals-timeseries carries
    `shares_out` for companies and, this probe established, for no fund on the
    watchlist. The series is the project's own, accumulated one reading per
    cycle, so what matters here is that the *reading* is available for every
    fund -- a fund it cannot measure contributes nothing, forever.
    """
    try:
        info = handle.info or {}
    except Exception as exc:  # noqa: BLE001
        print(f"  flow reading: FAILED {type(exc).__name__}: {exc}")
        return
    shares, source = flows.reading_from_info(info)
    if shares is None:
        print("  flow reading: NONE -- this fund can never build a flow series")
        return
    print(f"  flow reading: {shares:,.0f} shares ({source})")


def dump_holdings(handle: Any, ticker: str) -> None:
    """The analyst roll-up, and the thing that decides whether it is worth it.

    ``coverage`` is the number to watch: a roll-up over 11% of a broad index
    costs five lookups to say something about eleven percent.
    """
    if funds.fund_shape(ticker) != funds.EQUITY_FUND:
        return
    try:
        payload = handle.funds_data.top_holdings
    except Exception as exc:  # noqa: BLE001
        print(f"  holdings: FAILED {type(exc).__name__}: {exc}")
        return
    rows = []
    for symbol, weight in holdings.holdings_from_payload(payload):
        try:
            info = yf.Ticker(symbol).info or {}
            price = info.get("currentPrice") or info.get("regularMarketPrice")
            rows.append((symbol, weight, analysts.build_snapshot(info=info, last_close=price)))
        except Exception:  # noqa: BLE001 - a missed holding is the finding
            rows.append((symbol, weight, None))
    snapshot = holdings.build_snapshot(ticker, rows)
    if snapshot is None:
        print(f"  holdings: {len(rows)} read, none covered")
        return
    for line in snapshot.as_lines()[:2]:
        print(f"  {line}")


def dump_parsed(ticker: str) -> None:
    """The block as the prompt would carry it."""
    handle = yf.Ticker(ticker)
    print(f"===== {ticker}: parsed block ({funds.fund_shape(ticker)}) =====")
    try:
        data = handle.funds_data
        info = handle.info or {}
        snapshot = funds.build_snapshot(
            ticker,
            equity_holdings=getattr(data, "equity_holdings", None),
            bond_holdings=getattr(data, "bond_holdings", None),
            bond_ratings=getattr(data, "bond_ratings", None),
            fund_operations=getattr(data, "fund_operations", None),
            fund_overview=getattr(data, "fund_overview", None),
            top_holdings=getattr(data, "top_holdings", None),
            sector_weightings=getattr(data, "sector_weightings", None),
            asset_classes=getattr(data, "asset_classes", None),
            info=info,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"  failed: {type(exc).__name__}: {exc}")
        return
    if snapshot is None:
        print("  (no fund section -- by design)")
    else:
        for line in snapshot.as_lines():
            print(f"  {line}")
    dump_holdings(handle, ticker)
    dump_flows(handle, ticker)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tickers", nargs="*", default=list(DEFAULT_TICKERS))
    parser.add_argument("--raw", action="store_true", help="dump the untouched JSON")
    args = parser.parse_args(argv)

    for ticker in args.tickers or list(DEFAULT_TICKERS):
        if args.raw:
            dump_raw(ticker)
        else:
            dump_parsed(ticker)
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
