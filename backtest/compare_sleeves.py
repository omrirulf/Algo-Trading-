#!/usr/bin/env python3
"""Do index funds and single names behave differently under the risk engine?

    python backtest/compare_sleeves.py                  # fetch 2y from yfinance
    python backtest/compare_sleeves.py --csv-dir bars/  # offline, reproducible
    python backtest/compare_sleeves.py --json

Each sleeve is replayed under **its own** position cap -- single names at
``MAX_POSITION_PCT``, funds at ``MAX_BROAD_FUND_PCT`` -- because that is the
configuration that will actually run. Comparing both at the same cap would
answer a question nobody asked.

What this can and cannot tell you
----------------------------------
It replays *mechanical* entries every N bars through the real stop and sizing
arithmetic. So it answers questions about the risk engine: how often a 2x ATR
stop is hit, how often price gaps straight through it, how much of the account
one trade puts at risk, and how that differs between a volatile single name
and a diversified fund.

It says **nothing** about whether the LLM's signal is any good, because it
never asks the LLM anything. Entries here are a metronome, not a view. The
question "does the model add edge" needs live journal entries and
``analysis/score_journal.py``; no amount of OHLC replay substitutes for it.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Sequence

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backtest.simulate import DEFAULT_HORIZON_DAYS, Trade, simulate_series  # noqa: E402
from config import settings as cfg  # noqa: E402
from config.instruments import (  # noqa: E402
    BROAD_FUNDS,
    COMMODITY_FUNDS,
    FOCUSED_FUNDS,
    SINGLE_NAMES,
)

REQUIRED_COLUMNS = ("Open", "High", "Low", "Close")

#: Below this many trades a sleeve's aggregates are noise, and the report says
#: so rather than printing a precise-looking number.
MIN_TRADES_PER_SLEEVE = 30


@dataclass(frozen=True)
class SleeveResult:
    """Every trade from one sleeve, pooled across its tickers."""

    name: str
    max_position_pct: float
    trades: list[Trade]
    tickers: list[str]
    missing: list[str]

    @property
    def n(self) -> int:
        return len(self.trades)

    @property
    def enough(self) -> bool:
        return self.n >= MIN_TRADES_PER_SLEEVE

    def _mean(self, attr: str) -> Optional[float]:
        if not self.trades:
            return None
        return statistics.fmean(getattr(t, attr) for t in self.trades)

    @property
    def stop_hit_rate(self) -> Optional[float]:
        if not self.trades:
            return None
        return sum(1 for t in self.trades if t.stopped_out) / self.n

    @property
    def gap_rate(self) -> Optional[float]:
        """Of the stopped-out trades, how many filled worse than the stop."""
        stopped = [t for t in self.trades if t.stopped_out]
        if not stopped:
            return None
        return sum(1 for t in stopped if t.gapped_through) / len(stopped)

    @property
    def mean_risk_pct(self) -> Optional[float]:
        """Planned risk: what the stop says one trade can lose."""
        return self._mean("risk_pct_of_equity")

    @property
    def mean_realised_pct(self) -> Optional[float]:
        return self._mean("realised_pct_of_equity")

    @property
    def worst_realised_pct(self) -> Optional[float]:
        if not self.trades:
            return None
        return min(t.realised_pct_of_equity for t in self.trades)

    def as_dict(self) -> dict:
        return {
            "sleeve": self.name,
            "max_position_pct": self.max_position_pct,
            "tickers": list(self.tickers),
            "missing": list(self.missing),
            "trades": self.n,
            "enough_trades": self.enough,
            "stop_hit_rate": self.stop_hit_rate,
            "gap_rate": self.gap_rate,
            "mean_risk_pct_of_equity": self.mean_risk_pct,
            "mean_realised_pct_of_equity": self.mean_realised_pct,
            "worst_realised_pct_of_equity": self.worst_realised_pct,
        }


def load_bars(ticker: str, csv_dir: Optional[Path], period: str) -> Optional[pd.DataFrame]:
    """Bars for one ticker, or ``None`` when they cannot be had.

    A ticker that fails is reported as missing rather than raising: one
    delisted symbol or one rate-limited fetch must not void the whole
    comparison.
    """
    if csv_dir is not None:
        path = csv_dir / f"{ticker}.csv"
        if not path.exists():
            return None
        # index_col/parse_dates matter: simulate_trade reads dates off the
        # index, and a bare read_csv gives it integers that only fail much
        # deeper in. Same contract as run_backtest.py.
        frame = pd.read_csv(path, index_col=0, parse_dates=True)
    else:
        import yfinance as yf  # imported here so --csv-dir needs no network

        frame = yf.Ticker(ticker).history(
            period=period, interval="1d", auto_adjust=False
        )

    if frame is None or frame.empty:
        return None
    if any(column not in frame.columns for column in REQUIRED_COLUMNS):
        return None
    if not isinstance(frame.index, pd.DatetimeIndex):
        return None
    return frame.dropna(subset=list(REQUIRED_COLUMNS))


def run_sleeve(
    name: str,
    tickers: Sequence[str],
    max_position_pct: float,
    csv_dir: Optional[Path] = None,
    period: str = "2y",
    side: str = "buy",
    every: int = 5,
    equity: float = 100_000.0,
    horizon_days: int = DEFAULT_HORIZON_DAYS,
) -> SleeveResult:
    trades: list[Trade] = []
    used: list[str] = []
    missing: list[str] = []

    for ticker in tickers:
        bars = load_bars(ticker, csv_dir, period)
        if bars is None:
            missing.append(ticker)
            continue
        used.append(ticker)
        trades.extend(
            simulate_series(
                bars,
                side=side,
                every=every,
                equity=equity,
                horizon_days=horizon_days,
                stop_multiplier=cfg.ATR_STOP_MULTIPLIER,
                max_position_pct=max_position_pct,
            )
        )

    return SleeveResult(
        name=name,
        max_position_pct=max_position_pct,
        trades=trades,
        tickers=used,
        missing=missing,
    )


def _pct(value: Optional[float], places: int = 2) -> str:
    return "--" if value is None else f"{value * 100:.{places}f}%"


def render(results: Sequence[SleeveResult]) -> str:
    lines = [
        "SLEEVE COMPARISON",
        "",
        "Mechanical entries every N bars through the real stop and sizing math.",
        "This measures the risk engine, not the model: no LLM was asked anything.",
        "",
        f"{'sleeve':<14}{'cap':>6}{'trades':>8}{'stop hit':>10}"
        f"{'gapped':>9}{'risk/trade':>12}{'mean P&L':>11}{'worst':>9}",
    ]
    for r in results:
        lines.append(
            f"{r.name:<14}{r.max_position_pct:>5.0%}{r.n:>8}"
            f"{_pct(r.stop_hit_rate, 1):>10}{_pct(r.gap_rate, 1):>9}"
            f"{_pct(r.mean_risk_pct):>12}{_pct(r.mean_realised_pct):>11}"
            f"{_pct(r.worst_realised_pct):>9}"
        )

    thin = [r.name for r in results if not r.enough]
    if thin:
        lines += [
            "",
            f"NOT ENOUGH DATA: {', '.join(thin)} has fewer than "
            f"{MIN_TRADES_PER_SLEEVE} trades. Treat those rows as noise.",
        ]

    missing = {r.name: r.missing for r in results if r.missing}
    if missing:
        lines.append("")
        for name, tickers in missing.items():
            lines.append(f"NO BARS ({name}): {', '.join(tickers)}")

    lines += [
        "",
        "Reading it:",
        "- 'risk/trade' is what the stop says one position can lose, as a share",
        "  of the account. It is the number the two caps are trading off: a 20%",
        "  position in a quiet fund can risk less than a 5% one in a volatile",
        "  single name, which is the whole argument for the larger ETF cap.",
        "- 'gapped' is the share of stopped-out trades that opened through the",
        "  stop and filled worse than it. A stop is a request, not a guarantee.",
        "- 'mean P&L' comes from metronome entries, so it is a property of the",
        "  instruments and the holding period -- not evidence that anything here",
        "  has edge.",
    ]
    return "\n".join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare the single-name and index sleeves under their own caps."
    )
    parser.add_argument("--csv-dir", type=Path,
                        help="directory of <TICKER>.csv bars (offline, reproducible)")
    parser.add_argument("--period", default="2y", help="yfinance period (default: 2y)")
    parser.add_argument("--side", choices=("buy", "sell"), default="buy")
    parser.add_argument("--every", type=int, default=5,
                        help="open a trade every N bars (default: 5)")
    parser.add_argument("--horizon", type=int, default=DEFAULT_HORIZON_DAYS)
    parser.add_argument("--equity", type=float, default=100_000.0)
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    common = dict(
        csv_dir=args.csv_dir, period=args.period, side=args.side,
        every=args.every, equity=args.equity, horizon_days=args.horizon,
    )
    results = [
        run_sleeve("single name", SINGLE_NAMES, cfg.MAX_POSITION_PCT, **common),
        run_sleeve("broad fund", BROAD_FUNDS, cfg.MAX_BROAD_FUND_PCT, **common),
        run_sleeve("focused fund", FOCUSED_FUNDS, cfg.MAX_FOCUSED_FUND_PCT, **common),
        run_sleeve("commodity", COMMODITY_FUNDS, cfg.MAX_COMMODITY_FUND_PCT, **common),
    ]

    if args.as_json:
        print(json.dumps([r.as_dict() for r in results], indent=2))
    else:
        print(render(results))

    return 0 if any(r.trades for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
