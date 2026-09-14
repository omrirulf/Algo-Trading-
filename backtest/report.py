"""Render a sweep, with its limits attached to it.

Every figure carries its sample size, and anything thin is marked rather than
printed as though it meant something -- the same rule the signal scorer
follows, for the same reason.
"""

from __future__ import annotations

from typing import Optional, Sequence

from backtest.sweep import MIN_TRADES, Outcome
from config import settings as cfg


def _pct(value: Optional[float], places: int = 1) -> str:
    return "n/a" if value is None else f"{value:.{places}%}"


def _table(title: str, outcomes: Sequence[Outcome], current: str) -> list[str]:
    lines = [
        title,
        "-" * 78,
        f"{'setting':<12} {'n':>5} {'stopped':>9} {'gapped':>8} "
        f"{'risk/trade':>11} {'median ret':>11} {'worst':>8}",
    ]
    for outcome in outcomes:
        marker = "  <- current" if outcome.label == current else ""
        thin = "" if outcome.enough else "  (thin)"
        lines.append(
            f"{outcome.label:<12} {outcome.n:>5} "
            f"{_pct(outcome.stop_hit_rate):>9} "
            f"{_pct(outcome.gap_rate):>8} "
            f"{_pct(outcome.mean_risk_pct, 2):>11} "
            f"{_pct(outcome.median_return, 2):>11} "
            f"{_pct(outcome.worst_realised_pct, 2):>8}"
            f"{marker}{thin}"
        )
    lines.append("")
    return lines


def render(
    ticker: str,
    bars: int,
    multipliers: Sequence[Outcome],
    caps: Sequence[Outcome],
    side: str,
    horizon_days: int,
) -> str:
    out = [
        "RISK-ENGINE BACKTEST",
        "=" * 78,
        f"Ticker   : {ticker}   ({bars} daily bars)",
        f"Trades   : synthetic {side} every few bars, held {horizon_days} days or until stopped",
        "",
    ]

    out += _table(
        "STOP MULTIPLIER  (currently ATR_STOP_MULTIPLIER = "
        f"{cfg.ATR_STOP_MULTIPLIER:g})",
        multipliers,
        f"{cfg.ATR_STOP_MULTIPLIER:g}x ATR",
    )
    out += _table(
        f"POSITION CAP  (currently MAX_POSITION_PCT = {cfg.MAX_POSITION_PCT:.0%})",
        caps,
        f"{cfg.MAX_POSITION_PCT:.0%} cap",
    )

    out += [
        "HOW TO READ THIS",
        "-" * 78,
        "risk/trade is the number the two settings jointly decide: quantity times",
        "stop distance, as a fraction of equity. A 5% position cap does not put 5%",
        "at risk -- the stop distance does, and it is usually far smaller.",
        "",
        "gapped is the share of stopped-out trades that opened through the stop and",
        "filled worse than it. That is the part a stop cannot protect you from, and",
        "it rises as the stop gets tighter.",
        "",
        "LIMITS",
        "-" * 78,
        "These trades carry no signal. Entries are spaced through the history with",
        "no view attached, so returns here measure the price series, not a strategy:",
        "a multiplier that looks best by median return is telling you about these",
        "particular bars, not about an edge. Read the stop rate, the gap rate and",
        "the risk per trade -- those are mechanical and do not depend on the signal.",
        "",
        "Nothing here models slippage, commission, or the interaction between",
        f"positions that MAX_OPEN_POSITIONS ({cfg.MAX_OPEN_POSITIONS}) governs.",
        f"Anything marked (thin) has fewer than {MIN_TRADES} trades.",
    ]
    return "\n".join(out)


__all__ = ["render"]
