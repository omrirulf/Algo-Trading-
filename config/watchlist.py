"""What the orchestrator evaluates each cycle, and what that costs.

The list itself lives in :mod:`config.instruments`, split into a single-name
sleeve and an index sleeve. This module assembles them and prices the result,
so that "what do we watch" and "what does watching it cost" are one diff.

Version-controlled rather than an environment variable so a change to what
gets traded shows up in review -- the same reasoning that keeps the guardrail
thresholds in code.

Why two sleeves instead of picking one
---------------------------------------
Diversification and edge pull in opposite directions here. Breadth argues for
index funds: one call on a broad fund prices hundreds of underlying names, and
whole asset classes -- small caps, REITs, duration, real commodities -- have
no affordable single-name route at all. Edge argues for single names: only a
specific company has the analyst coverage and insider filings that three of
the five prompt dimensions are built on, and a sentiment read on a broad index
is macro timing, which is a much harder call.

Neither argument settles it, which is why both sleeves ship and
``backtest/run_backtest.py`` decides between them from real bars rather than
from the paragraph above.
"""

from __future__ import annotations

from typing import Final

from config.instruments import (
    FUND_ROLES,
    FUNDS,
    SINGLE_NAME_SECTORS,
    SINGLE_NAMES,
    InstrumentKind,
    kind_for,
)
from orchestrator import pricing
from config import settings as cfg

DEFAULT_WATCHLIST: Final[tuple[str, ...]] = SINGLE_NAMES + FUNDS

#: Buckets for reporting, and for anyone trimming the list by theme.
BUCKETS: Final[dict[str, tuple[str, ...]]] = {
    **SINGLE_NAME_SECTORS,
    **{f"Fund: {role}": tickers for role, tickers in FUND_ROLES.items()},
}

#: Input tokens in one ticker's prompt, counted from the rendered system and
#: user blocks. This one is measured.
ESTIMATED_INPUT_TOKENS: Final[int] = 1_400

#: Output tokens in one answer. This one is **assumed** -- a signal plus its
#: rationales, before any thinking. It is the whole uncertainty in the figures
#: below, and it is named here rather than folded into a single magic constant
#: so that it can be argued with.
ASSUMED_OUTPUT_TOKENS: Final[int] = 1_600


def _cost_per_call_usd(model: str = "claude-opus-5") -> float:
    """Estimated dollars for one ticker's call, from the published prices.

    Derived from ``pricing.PRICES`` rather than hard-coded so a price change
    is a one-line diff in one place. Still an estimate: it rests on
    ``ASSUMED_OUTPUT_TOKENS``, and it assumes no cache hit and no thinking.
    """
    price = pricing.PRICES[model]
    return (
        ESTIMATED_INPUT_TOKENS * price.input_per_mtok
        + ASSUMED_OUTPUT_TOKENS * price.output_per_mtok
    ) / 1e6


#: Rough Claude cost per ticker per cycle, in dollars.
COST_PER_TICKER_PER_CYCLE_USD: Final[float] = _cost_per_call_usd()


def default_watchlist_csv() -> str:
    return ",".join(DEFAULT_WATCHLIST)


def estimated_monthly_cost_usd(
    tickers: int, cycles_per_day: int = cfg.CYCLES_PER_TRADING_DAY, trading_days: int = 21
) -> float:
    """Rough Claude spend for a watchlist of this size.

    Superseded the moment real cycles exist: once the journal carries measured
    ``usage`` blocks, feed an observed per-call cost to ``pricing.monthly_usd``
    instead of trusting this. Sizing a list before the first cycle is the only
    job this function has.
    """
    return pricing.monthly_usd(
        COST_PER_TICKER_PER_CYCLE_USD, tickers, cycles_per_day, trading_days
    )


def sleeve_of(ticker: str) -> str:
    """``"fund"`` or ``"single name"``, for reports that group by sleeve.

    Coarser than ``kind_for``: the two fund kinds are sized differently but
    share one sleeve budget, because they are both "not a company".
    """
    return "single name" if kind_for(ticker) is InstrumentKind.EQUITY else "fund"


__all__ = [
    "DEFAULT_WATCHLIST",
    "BUCKETS",
    "SINGLE_NAMES",
    "FUNDS",
    "ESTIMATED_INPUT_TOKENS",
    "ASSUMED_OUTPUT_TOKENS",
    "COST_PER_TICKER_PER_CYCLE_USD",
    "default_watchlist_csv",
    "estimated_monthly_cost_usd",
    "sleeve_of",
]
