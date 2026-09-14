"""What the orchestrator evaluates each cycle, and why it is this list.

Version-controlled rather than an environment variable so a change to what
gets traded shows up in a diff and in review -- the same reasoning that keeps
the guardrail thresholds in code.

Why individual equities rather than ETFs
----------------------------------------
The obvious way to diversify is VGK for Europe, EIS for Israel, GLD for gold.
It does not work here, and the reason is structural rather than a preference.

This pipeline builds a five-dimension prompt: news, technicals, fundamentals,
the analyst view, and insider filings. An ETF has no earnings, no margins, no
price targets and no Form 4 filings, and a Google News query for its ticker
returns almost nothing. Four of the five dimensions come back empty, the
prompt names them as gaps, and the model is told to score them 0.0. What runs
is a technicals-only strategy that nothing here has tested -- exactly the
failure mode the news-skip rule exists to prevent.

So geography and commodity exposure are taken through *companies* that happen
to be listed in the US: ADRs for Europe and Asia, US-listed Israeli issuers,
and producers rather than the commodity itself. Those have news, earnings,
analysts, and mostly insiders -- the strategy stays the one that was built.

What this cannot reach
----------------------
Alpaca trades ``us_equity``, ``us_option`` and ``crypto`` only. There is no
path to the Frankfurt, Paris, London or Tel Aviv order books, and none to
futures, so physical oil and gold are out of reach whatever the watchlist
says. Everything below is US-listed.

Cost
----
One Bright Data request and one Claude call per ticker per cycle. At the
default hourly cadence inside market hours that is roughly seven cycles a day,
about 1,400 input tokens and a short answer each. Per ticker that lands near
$6-7 a month on Claude Opus 5 at $5/$25 per million tokens, so this list is on
the order of $150-200 a month, plus Bright Data. Shortening the list is the
lever; ``HEARTBEAT_INTERVAL_MINUTES`` is the other.

A longer list does not mean more positions. ``MAX_OPEN_POSITIONS`` still caps
holdings at 10 and ``MAX_POSITION_PCT`` at 5% each -- breadth buys the model
more to choose between, not more exposure.
"""

from __future__ import annotations

from typing import Final

from orchestrator import pricing

# --- United States, spread across sectors --------------------------------
# The starting default was AAPL, MSFT, NVDA. Three US mega-cap technology
# names move together closely enough that they are nearer one position than
# three, which is the opposite of what a watchlist is for.
US_SECTORS: Final[tuple[str, ...]] = (
    "MSFT",   # software
    "NVDA",   # semiconductors
    "GOOGL",  # communication services
    "JPM",    # financials
    "UNH",    # healthcare
    "LLY",    # pharmaceuticals
    "PG",     # consumer staples
    "COST",   # consumer discretionary / retail
    "CAT",    # industrials
    "NEE",    # utilities
)

# --- Europe, through US-listed ADRs ---------------------------------------
EUROPE_ADRS: Final[tuple[str, ...]] = (
    "ASML",   # Netherlands - semiconductor equipment
    "SAP",    # Germany - enterprise software
    "NVO",    # Denmark - pharmaceuticals
    "SHEL",   # UK/Netherlands - energy
    "AZN",    # UK - pharmaceuticals
    "UL",     # UK - consumer goods
)

# --- Israel, through US-listed issuers -------------------------------------
ISRAEL: Final[tuple[str, ...]] = (
    "TEVA",   # pharmaceuticals
    "CHKP",   # cybersecurity
    "NICE",   # enterprise software
    "CYBR",   # cybersecurity
    "MNDY",   # work software
    "ESLT",   # defence
)

# --- Asia and Latin America, through ADRs ---------------------------------
EMERGING_ADRS: Final[tuple[str, ...]] = (
    "TSM",    # Taiwan - semiconductor foundry
    "INFY",   # India - IT services
    "HDB",    # India - banking
    "VALE",   # Brazil - iron ore
)

# --- Commodities, through producers ---------------------------------------
# A gold miner has earnings, analysts and insiders; GLD has none of them.
# The exposure is less pure -- a miner carries company risk the metal does
# not -- and that is the price of keeping all five dimensions alive.
COMMODITY_PRODUCERS: Final[tuple[str, ...]] = (
    "XOM",    # oil and gas
    "NEM",    # gold
    "FCX",    # copper
    "NTR",    # agriculture / fertiliser
)

DEFAULT_WATCHLIST: Final[tuple[str, ...]] = (
    US_SECTORS + EUROPE_ADRS + ISRAEL + EMERGING_ADRS + COMMODITY_PRODUCERS
)

#: Buckets, for reporting and for anyone trimming the list by theme.
BUCKETS: Final[dict[str, tuple[str, ...]]] = {
    "US sectors": US_SECTORS,
    "Europe (ADR)": EUROPE_ADRS,
    "Israel": ISRAEL,
    "Emerging (ADR)": EMERGING_ADRS,
    "Commodity producers": COMMODITY_PRODUCERS,
}

#: Input tokens in one ticker's prompt, counted from the rendered system and
#: user blocks. This one is measured.
ESTIMATED_INPUT_TOKENS: Final[int] = 1_400

#: Output tokens in one answer. This one is **assumed** -- a signal plus its
#: five rationales, before any thinking. It is the whole uncertainty in the
#: figures below, and it is named here rather than folded into a single magic
#: constant so that it can be argued with.
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
    tickers: int, cycles_per_day: int = 7, trading_days: int = 21
) -> float:
    """Rough Claude spend for a watchlist of this size.

    Superseded the moment real cycles exist: once the journal carries measured
    ``usage`` blocks, feed an observed per-call cost to
    ``pricing.monthly_usd`` instead of trusting this. Sizing a list before the
    first cycle is the only job this function has.
    """
    return pricing.monthly_usd(
        COST_PER_TICKER_PER_CYCLE_USD, tickers, cycles_per_day, trading_days
    )


__all__ = [
    "US_SECTORS",
    "EUROPE_ADRS",
    "ISRAEL",
    "EMERGING_ADRS",
    "COMMODITY_PRODUCERS",
    "DEFAULT_WATCHLIST",
    "BUCKETS",
    "ESTIMATED_INPUT_TOKENS",
    "ASSUMED_OUTPUT_TOKENS",
    "COST_PER_TICKER_PER_CYCLE_USD",
    "default_watchlist_csv",
    "estimated_monthly_cost_usd",
]
