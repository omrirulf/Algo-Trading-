"""What we trade, and what kind of thing each ticker is.

Two sleeves, because they are different bets that need different handling:

**Single names** carry idiosyncratic information. A specific company has
earnings, analyst targets and insider filings, and the five-dimension prompt
has something to chew on. This is where an LLM signal could plausibly have an
edge: "these insiders bought, analysts upgraded, and the news is a real
catalyst" is a coherent thesis about one business.

**Index funds** carry none of that, and reaching for them is a different
claim entirely -- a macro or flow read, which is the hardest call in finance
and the one where a language model's edge is least obvious. They are here
anyway for a reason single names cannot serve: they are the only affordable
way to reach whole asset classes. One call on ``IWM`` prices two thousand
small caps; reaching the same breadth through single names would cost a
hundred times as much and drown in thin news coverage.

Which sleeve actually earns its place is an open question, and deliberately
so. ``backtest/`` can now answer it from two years of real bars, which is a
better arbiter than the argument above.

Why the kind lives here and not in the signal
----------------------------------------------
``InstrumentKind`` decides the position-size cap, and an ETF's cap is several
times an equity's. If the model could assert its own instrument kind, it
could unlock a larger position by claiming one -- so it cannot. The kind is a
property of *this file*, resolved from the ticker by the execution engine,
and ``LLMSignal`` has no field that could carry it. An unrecognised ticker
resolves to ``EQUITY``, the tighter cap, so a mistake fails closed.
"""

from __future__ import annotations

from enum import Enum
from typing import Final


class InstrumentKind(str, Enum):
    """What a ticker is, for sizing and prompting purposes."""

    EQUITY = "equity"
    #: An exchange-traded fund holding many underlying positions. Internally
    #: diversified, so a larger share of equity is appropriate -- and it has
    #: no analysts covering it and no insiders filing Form 4.
    ETF = "etf"


# --------------------------------------------------------------------------- #
# Sleeve 1: single names
# --------------------------------------------------------------------------- #
# Grouped by sector rather than by country, because sector is what actually
# drives correlation. The previous list was 37% technology and called its
# ADRs "geographic diversification" -- but ASML, TSM, SAP and INFY are global
# technology cyclicals that fall together with US technology in a drawdown.
# A mega-cap multinational's listing venue tells you almost nothing about
# what it is correlated with.

TECHNOLOGY: Final[tuple[str, ...]] = ("MSFT", "NVDA", "TSM", "ASML")
COMMUNICATION: Final[tuple[str, ...]] = ("GOOGL",)
FINANCIALS: Final[tuple[str, ...]] = ("JPM", "HDB", "RY")
HEALTH_CARE: Final[tuple[str, ...]] = ("LLY", "NVO", "TEVA")
INDUSTRIALS: Final[tuple[str, ...]] = ("CAT", "CNI", "ESLT")
CONSUMER_DISCRETIONARY: Final[tuple[str, ...]] = ("TM", "MELI")
CONSUMER_STAPLES: Final[tuple[str, ...]] = ("PG", "UL")
ENERGY: Final[tuple[str, ...]] = ("XOM", "SHEL")
MATERIALS: Final[tuple[str, ...]] = ("BHP", "NEM")

SINGLE_NAME_SECTORS: Final[dict[str, tuple[str, ...]]] = {
    "Technology": TECHNOLOGY,
    "Communication": COMMUNICATION,
    "Financials": FINANCIALS,
    "Health care": HEALTH_CARE,
    "Industrials": INDUSTRIALS,
    "Consumer discretionary": CONSUMER_DISCRETIONARY,
    "Consumer staples": CONSUMER_STAPLES,
    "Energy": ENERGY,
    "Materials": MATERIALS,
}

SINGLE_NAMES: Final[tuple[str, ...]] = tuple(
    ticker for bucket in SINGLE_NAME_SECTORS.values() for ticker in bucket
)


# --------------------------------------------------------------------------- #
# Sleeve 2: index funds
# --------------------------------------------------------------------------- #
# Chosen for what single names cannot reach: whole cap tiers, whole regions,
# and asset classes that are not equities at all. Every one is US-listed, so
# Alpaca can trade it -- its AssetClass enum is us_equity / us_option /
# crypto, and there is no route to a foreign order book or to futures.

#: Equal-weighted S&P 500 rather than SPY. Cap-weighted US indices are a
#: concentrated technology bet in disguise; equal weight is the diversified
#: version of the same market.
BROAD_EQUITY: Final[tuple[str, ...]] = ("RSP", "IWM")

#: Regions as whole markets, which is the exposure ADRs only pretend to give.
REGIONS: Final[tuple[str, ...]] = ("VGK", "EWJ", "VWO", "EIS")

#: Sectors and asset classes with no single-name representation at all.
REAL_ASSETS: Final[tuple[str, ...]] = ("VNQ", "GLD", "DBC")

#: Duration. The one holding here that is not equity risk, and historically
#: the most reliable diversifier against it.
DURATION: Final[tuple[str, ...]] = ("TLT",)

INDEX_ROLES: Final[dict[str, tuple[str, ...]]] = {
    "Broad equity": BROAD_EQUITY,
    "Regions": REGIONS,
    "Real assets": REAL_ASSETS,
    "Duration": DURATION,
}

INDEX_SLEEVE: Final[tuple[str, ...]] = tuple(
    ticker for bucket in INDEX_ROLES.values() for ticker in bucket
)

#: Set form, for the O(1) lookup ``kind_for`` does on every execution.
_INDEX_SET: Final[frozenset[str]] = frozenset(INDEX_SLEEVE)


def kind_for(ticker: str) -> InstrumentKind:
    """Classify a ticker for sizing and prompting.

    Deliberately total: any ticker at all gets an answer, and anything this
    file does not recognise is an ``EQUITY``. That default is the tighter
    position cap, so an unknown or misspelled ticker can only ever be sized
    down, never up.
    """
    return InstrumentKind.ETF if ticker.strip().upper() in _INDEX_SET else InstrumentKind.EQUITY


def is_index_fund(ticker: str) -> bool:
    return kind_for(ticker) is InstrumentKind.ETF


__all__ = [
    "InstrumentKind",
    "SINGLE_NAME_SECTORS",
    "SINGLE_NAMES",
    "INDEX_ROLES",
    "INDEX_SLEEVE",
    "kind_for",
    "is_index_fund",
]
