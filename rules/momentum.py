"""Arm B: time-series momentum, with nothing fitted to this journal.

The thesis is the oldest documented one there is. Moskowitz, Ooi and
Pedersen ("Time Series Momentum", *Journal of Financial Economics* 2012)
showed that the sign of an asset's own trailing return predicts its next
return, across every asset class they looked at -- equities, bonds,
currencies, commodities -- which matters here because half this watchlist
is funds tracking exactly those things. Medhat and Schmeling ("Short-Term
Momentum", *Review of Financial Studies* 2022) showed the shorter-horizon
version survives trading costs in large, liquid names, which is what this
watchlist is made of.

The rule
--------
Go with the trailing quarter, when the 50-day average agrees:

* BULLISH when the 63-bar return is positive AND price is above its 50-day
  SMA; BEARISH when both are negative; NEUTRAL when they disagree. Requiring
  both is the standard trend-confirmation filter -- a positive quarter with
  price already back under its average is a trend that may be over.
* Conviction is the quarter's return measured in volatility, so a 10% move
  in a 15%-vol fund counts for more than the same move in a 60%-vol single
  name. Full conviction is set at a two-quarterly-sigma move. Since a
  quarter is 63/252 of a year, and sqrt(63/252) = 0.5, two quarterly sigmas
  is exactly one annual sigma -- so the number that comes out is simply
  ``|return_63d| / annualised_volatility``, clamped to [0, 1].

Why every number here is fixed
------------------------------
63 bars is a quarter. 50 is the confirmation average the literature uses.
Two sigmas for full conviction is the choice that makes the scale fall out
as one annual sigma with no leftover constant. None of them was chosen by
looking at what this journal would then say, and none of them will be moved
by it: the harness judges this rule, it does not tune it. A rule that is
re-fitted on the returns it is then scored against is the overfitting
machine the second opinion warned about, and this is the one place in the
project where "leave it alone" is the whole method.

What it reads
-------------
Only ``TechnicalSnapshot``: the fields the cycle computed from price history
up to the signal bar and showed the model in its prompt. No news, no
fundamentals, no analysts, no insiders. That is the point, not a limit --
the model sees all of those too, and the question is whether reading them
buys anything over reading the price alone.

Thin history is an outcome, not an error: a name without 64 bars, or without
a 50-day average, is NEUTRAL with the reason in the rationale.
"""

from __future__ import annotations

from typing import Optional

from app.schemas import Bias, LLMSignal
from orchestrator.technicals import TechnicalSnapshot

NAME = "momentum"

#: The trailing window, in bars. One quarter. Read from ``return_63d``.
LOOKBACK_BARS = 63
#: The confirmation average. Read from ``distance_sma50``.
CONFIRMATION_SMA = 50
#: Full conviction at a move of this many quarterly standard deviations.
FULL_CONVICTION_SIGMAS = 2.0
#: A quarter's share of a year's volatility: sqrt(63 / 252).
QUARTER_OF_A_YEAR = (LOOKBACK_BARS / 252) ** 0.5


def signal_for(ticker: str, snapshot: Optional[TechnicalSnapshot]) -> LLMSignal:
    """The momentum arm's call for one ticker, from the snapshot the model saw.

    Deterministic: the same snapshot always yields the same signal, which is
    what lets the harness recompute this arm over the whole journal from the
    technicals each line already carries.
    """
    if snapshot is None:
        return _neutral(ticker, "no technicals in the context")

    quarter = snapshot.return_63d
    above_average = snapshot.distance_sma50
    vol = snapshot.annualised_volatility

    if quarter is None:
        return _neutral(ticker, f"fewer than {LOOKBACK_BARS + 1} bars of history")
    if above_average is None:
        return _neutral(ticker, f"no {CONFIRMATION_SMA}-day average yet")
    if vol is None or vol <= 0:
        return _neutral(ticker, "no usable volatility to scale conviction by")

    trend_up = quarter > 0 and above_average > 0
    trend_down = quarter < 0 and above_average < 0
    if not (trend_up or trend_down):
        return _neutral(
            ticker,
            f"{LOOKBACK_BARS}d return {quarter:+.1%} and distance to {CONFIRMATION_SMA}d SMA "
            f"{above_average:+.1%} disagree",
        )

    # Two quarterly sigmas == one annual sigma, so the divisor is just vol.
    full = FULL_CONVICTION_SIGMAS * QUARTER_OF_A_YEAR * vol
    conviction = min(1.0, abs(quarter) / full)

    return LLMSignal(
        ticker=ticker,
        bias=Bias.BULLISH if trend_up else Bias.BEARISH,
        conviction=round(conviction, 4),
        rationale=(
            f"{LOOKBACK_BARS}d return {quarter:+.1%} is {abs(quarter) / vol:.2f}x annual vol "
            f"{vol:.1%}; price {above_average:+.1%} vs {CONFIRMATION_SMA}d SMA"
        ),
    )


def _neutral(ticker: str, reason: str) -> LLMSignal:
    return LLMSignal(ticker=ticker, bias=Bias.NEUTRAL, conviction=0.0, rationale=f"{NAME}: {reason}")


__all__ = [
    "NAME",
    "LOOKBACK_BARS",
    "CONFIRMATION_SMA",
    "FULL_CONVICTION_SIGMAS",
    "QUARTER_OF_A_YEAR",
    "signal_for",
]
