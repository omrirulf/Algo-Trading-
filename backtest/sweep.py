"""Vary one guardrail at a time and see what it costs.

The point is not to find the multiplier with the best return -- with synthetic
signals there is no edge to optimise, and a number picked that way would be
curve-fitting to two years of one ticker. The point is to see the *mechanical*
consequences, which do not depend on signal quality:

    how often a stop is hit, how often price gaps through it, and how much of
    the account a single trade actually puts at risk.
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass
from typing import Optional, Sequence

import pandas as pd

from backtest.simulate import DEFAULT_HORIZON_DAYS, Trade, simulate_series
from config import settings as cfg

DEFAULT_MULTIPLIERS: tuple[float, ...] = (1.0, 1.5, 2.0, 2.5, 3.0, 4.0)
DEFAULT_CAPS: tuple[float, ...] = (0.02, 0.05, 0.10)

#: Below this, a percentage is a description of these particular bars rather
#: than an estimate of anything. Mirrors the scorer's MIN_SAMPLE.
MIN_TRADES = 20


@dataclass(frozen=True)
class Outcome:
    """Aggregates for one parameter setting."""

    label: str
    trades: list[Trade]

    @property
    def n(self) -> int:
        return len(self.trades)

    @property
    def enough(self) -> bool:
        return self.n >= MIN_TRADES

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
        if not self.trades:
            return None
        return statistics.fmean(t.risk_pct_of_equity for t in self.trades)

    @property
    def median_return(self) -> Optional[float]:
        if not self.trades:
            return None
        return statistics.median(t.return_pct for t in self.trades)

    @property
    def mean_realised_pct(self) -> Optional[float]:
        if not self.trades:
            return None
        return statistics.fmean(t.realised_pct_of_equity for t in self.trades)

    @property
    def worst_realised_pct(self) -> Optional[float]:
        if not self.trades:
            return None
        return min(t.realised_pct_of_equity for t in self.trades)


def sweep_multipliers(
    ohlc: pd.DataFrame,
    multipliers: Sequence[float] = DEFAULT_MULTIPLIERS,
    side: str = "buy",
    every: int = 5,
    equity: float = 100_000.0,
    horizon_days: int = DEFAULT_HORIZON_DAYS,
    max_position_pct: float = cfg.MAX_POSITION_PCT,
) -> list[Outcome]:
    return [
        Outcome(
            label=f"{m:g}x ATR",
            trades=simulate_series(
                ohlc, side=side, every=every, equity=equity, horizon_days=horizon_days,
                stop_multiplier=m, max_position_pct=max_position_pct,
            ),
        )
        for m in multipliers
    ]


def sweep_caps(
    ohlc: pd.DataFrame,
    caps: Sequence[float] = DEFAULT_CAPS,
    side: str = "buy",
    every: int = 5,
    equity: float = 100_000.0,
    horizon_days: int = DEFAULT_HORIZON_DAYS,
    stop_multiplier: float = cfg.ATR_STOP_MULTIPLIER,
) -> list[Outcome]:
    return [
        Outcome(
            label=f"{c:.0%} cap",
            trades=simulate_series(
                ohlc, side=side, every=every, equity=equity, horizon_days=horizon_days,
                stop_multiplier=stop_multiplier, max_position_pct=c,
            ),
        )
        for c in caps
    ]


__all__ = [
    "DEFAULT_MULTIPLIERS",
    "DEFAULT_CAPS",
    "MIN_TRADES",
    "Outcome",
    "sweep_multipliers",
    "sweep_caps",
]
