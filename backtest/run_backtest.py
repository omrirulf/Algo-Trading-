#!/usr/bin/env python3
"""Replay price history through the risk engine's stop and sizing arithmetic.

    python backtest/run_backtest.py AAPL
    python backtest/run_backtest.py AAPL --side sell --horizon 20
    python backtest/run_backtest.py AAPL --csv bars.csv     # offline, reproducible

Answers what a 2x ATR stop and a 5% cap actually do -- how often the stop is
hit, how often price gaps through it, and how much of the account one trade
puts at risk -- without waiting for live trades.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backtest import report, sweep  # noqa: E402
from backtest.simulate import DEFAULT_HORIZON_DAYS  # noqa: E402

REQUIRED_COLUMNS = ("Open", "High", "Low", "Close")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backtest the risk engine's arithmetic.")
    parser.add_argument("ticker", help="ticker to fetch, or a label when --csv is given")
    parser.add_argument("--csv", type=Path,
                        help="read bars from a CSV instead of yfinance (reproducible, offline)")
    parser.add_argument("--period", default="2y", help="yfinance period (default: 2y)")
    parser.add_argument("--side", choices=("buy", "sell"), default="buy")
    parser.add_argument("--horizon", type=int, default=DEFAULT_HORIZON_DAYS,
                        help=f"days held if never stopped (default: {DEFAULT_HORIZON_DAYS})")
    parser.add_argument("--every", type=int, default=5,
                        help="open a trade every N bars (default: 5)")
    parser.add_argument("--equity", type=float, default=100_000.0)
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args(argv)


def load_bars(args: argparse.Namespace) -> pd.DataFrame:
    if args.csv:
        frame = pd.read_csv(args.csv, index_col=0, parse_dates=True)
    else:
        import yfinance as yf  # imported here so --csv needs no network

        frame = yf.Ticker(args.ticker).history(
            period=args.period, interval="1d", auto_adjust=False
        )
    missing = [c for c in REQUIRED_COLUMNS if c not in frame.columns]
    if missing:
        raise SystemExit(f"bars are missing columns: {', '.join(missing)}")
    return frame.dropna(subset=list(REQUIRED_COLUMNS))


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    bars = load_bars(args)
    if len(bars) < 60:
        print(f"Only {len(bars)} usable bars; need a longer history.", file=sys.stderr)
        return 1

    shared = dict(side=args.side, every=args.every, equity=args.equity,
                  horizon_days=args.horizon)
    multipliers = sweep.sweep_multipliers(bars, **shared)
    caps = sweep.sweep_caps(bars, **shared)

    if args.as_json:
        print(json.dumps({
            "ticker": args.ticker,
            "bars": len(bars),
            "side": args.side,
            "horizon_days": args.horizon,
            "min_trades_for_confidence": sweep.MIN_TRADES,
            "multipliers": [_row(o) for o in multipliers],
            "caps": [_row(o) for o in caps],
        }, indent=2))
    else:
        print(report.render(args.ticker, len(bars), multipliers, caps,
                            args.side, args.horizon))
    return 0


def _row(outcome: sweep.Outcome) -> dict:
    return {
        "setting": outcome.label,
        "trades": outcome.n,
        "enough_trades": outcome.enough,
        "stop_hit_rate": outcome.stop_hit_rate,
        "gap_rate": outcome.gap_rate,
        "mean_risk_pct_of_equity": outcome.mean_risk_pct,
        "median_return": outcome.median_return,
        "worst_realised_pct_of_equity": outcome.worst_realised_pct,
    }


if __name__ == "__main__":
    raise SystemExit(main())
