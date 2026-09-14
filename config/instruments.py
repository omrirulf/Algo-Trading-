"""What we trade, what kind of thing each ticker is, and what it correlates with.

Three kinds, because they carry three different risks and so deserve three
different position caps:

``EQUITY``
    One company. Idiosyncratic: it can gap on a fraud, a failed trial or a
    guidance cut. It is also the only kind with analyst coverage and insider
    filings, so it is the only kind where all five prompt dimensions have
    content.

``BROAD_FUND``
    A basket of hundreds of positions. Internally diversified, so a larger
    share of equity is appropriate -- the diversification argument for index
    funds and a single-name cap cancel each other out.

``COMMODITY_FUND``
    A fund tracking **one** commodity. The word "fund" is doing no
    diversification work here: coffee is one thing, and a fund holding coffee
    futures is a concentrated, volatile, single-factor bet -- often more
    volatile than a large-cap equity, not less. Giving these the broad-fund
    cap because they are technically funds would repeat, in a subtler place,
    the error of sizing a cap by roundness rather than by risk. They get the
    tightest cap here.

Why the kind lives in this file and not in the signal
------------------------------------------------------
The kind decides the position cap. If a model could assert its own kind it
could enlarge its own position by claiming one, so it cannot: the kind is a
property of this file, resolved from the ticker, and ``LLMSignal`` has no
field that could carry one. An unrecognised ticker resolves to ``EQUITY`` --
never the largest cap -- so a mistake fails closed.

Exposure groups
---------------
Sector diversity in the *watchlist* does not produce sector diversity in the
*portfolio*. Nothing stopped the engine opening MSFT, NVDA, TSM, ASML and
GOOGL on the same morning -- five positions, one bet. ``EXPOSURE_GROUPS``
exists so a cap can be put on that, and it spans both sleeves on purpose:
holding XOM *and* an oil fund *and* a natural-gas fund is one energy bet made
three times, and a cap that only looked at equities would miss it.
"""

from __future__ import annotations

from enum import Enum
from typing import Final


class InstrumentKind(str, Enum):
    EQUITY = "equity"
    BROAD_FUND = "broad fund"
    COMMODITY_FUND = "commodity fund"


# --------------------------------------------------------------------------- #
# Sleeve 1: single names -- the alpha sleeve
# --------------------------------------------------------------------------- #
# Deliberately smaller than the fund sleeve. These are the only holdings where
# analyst coverage and insider filings exist, so this is where a stock-picking
# edge could show up if there is one -- but that edge is unproven, and the
# sleeve budget reflects that rather than assuming it.
#
# No materials sector any more: NEM and BHP were standing in for gold and
# copper, and a miner is a company bet with a commodity attached. The metals
# are now held directly.

TECHNOLOGY: Final[tuple[str, ...]] = ("MSFT", "NVDA", "ASML")
COMMUNICATION: Final[tuple[str, ...]] = ("GOOGL",)
FINANCIALS: Final[tuple[str, ...]] = ("JPM", "RY", "HDB")
HEALTH_CARE: Final[tuple[str, ...]] = ("LLY", "NVO", "TEVA")
INDUSTRIALS: Final[tuple[str, ...]] = ("CAT", "ESLT")
CONSUMER_DISCRETIONARY: Final[tuple[str, ...]] = ("TM", "MELI")
CONSUMER_STAPLES: Final[tuple[str, ...]] = ("PG",)
ENERGY_EQUITY: Final[tuple[str, ...]] = ("XOM",)

SINGLE_NAME_SECTORS: Final[dict[str, tuple[str, ...]]] = {
    "Technology": TECHNOLOGY,
    "Communication": COMMUNICATION,
    "Financials": FINANCIALS,
    "Health care": HEALTH_CARE,
    "Industrials": INDUSTRIALS,
    "Consumer discretionary": CONSUMER_DISCRETIONARY,
    "Consumer staples": CONSUMER_STAPLES,
    "Energy": ENERGY_EQUITY,
}

SINGLE_NAMES: Final[tuple[str, ...]] = tuple(
    t for bucket in SINGLE_NAME_SECTORS.values() for t in bucket
)


# --------------------------------------------------------------------------- #
# Sleeve 2a: broad funds -- the core
# --------------------------------------------------------------------------- #
# RSP rather than SPY: a cap-weighted US index is a concentrated technology
# bet wearing a diversified label, and equal weight is the diversified version
# of the same market.

US_BROAD: Final[tuple[str, ...]] = ("RSP", "IWM")
INTERNATIONAL: Final[tuple[str, ...]] = ("VGK", "EWJ", "VWO", "EIS")
REAL_ESTATE: Final[tuple[str, ...]] = ("VNQ",)
#: The only holding here that is not equity risk, and historically the most
#: reliable diversifier against it.
DURATION: Final[tuple[str, ...]] = ("TLT",)
#: Broad commodity baskets. These *are* diversified across commodities, so
#: they are broad funds rather than commodity funds.
BROAD_COMMODITY: Final[tuple[str, ...]] = ("DBC", "DBA")

BROAD_FUND_ROLES: Final[dict[str, tuple[str, ...]]] = {
    "US broad equity": US_BROAD,
    "International equity": INTERNATIONAL,
    "Real estate": REAL_ESTATE,
    "Duration": DURATION,
    "Broad commodities": BROAD_COMMODITY,
}

BROAD_FUNDS: Final[tuple[str, ...]] = tuple(
    t for bucket in BROAD_FUND_ROLES.values() for t in bucket
)


# --------------------------------------------------------------------------- #
# Sleeve 2b: single-commodity funds
# --------------------------------------------------------------------------- #
# Alpaca trades us_equity, us_option and crypto only, so futures are out of
# reach and physical metal is not a thing one can hold in a brokerage account.
# These US-listed funds are the only route to the commodities themselves --
# as opposed to the companies that mine and drill them.
#
# Three structural risks that do not apply to the equity sleeve, documented
# here because they are easy to forget once a ticker is just a ticker:
#
# 1. ROLL DECAY. A futures-backed fund rolls contracts forward. In contango it
#    sells cheap and buys dear every month, so it can lose value while the spot
#    price is flat. USO is the notorious example. These are not buy-and-hold
#    instruments.
# 2. ETN CREDIT RISK. JO is an exchange-traded *note* -- unsecured debt of its
#    issuer, not a fund holding anything. If the issuer fails the note can go
#    to zero with coffee trading normally. ETNs also get called by the issuer.
# 3. THINNESS. Several of these trade a small fraction of the volume of a
#    broad fund, so the spread is a real cost and a stop can fill badly.
#
# The tighter COMMODITY cap is the response to all three.

PRECIOUS_METALS: Final[tuple[str, ...]] = ("GLD", "SLV")
INDUSTRIAL_METALS: Final[tuple[str, ...]] = ("CPER",)
ENERGY_COMMODITY: Final[tuple[str, ...]] = ("USO", "UNG")
#: CANE is sugar. Coffee and rice have no single-commodity fund here:
#:
#: - JO, the iPath coffee ETN, was on this list until the first verification
#:   run returned no bars for it. That is the ETN failure mode described above
#:   happening in practice -- an issuer can call a note, and then the ticker
#:   simply stops existing. Coffee exposure now comes through DBA, whose
#:   basket includes it.
#: - Rice has never had a US-listed fund. Rough-rice futures exist; nothing
#:   wraps them.
AGRICULTURE: Final[tuple[str, ...]] = ("CORN", "WEAT", "SOYB", "CANE")

COMMODITY_ROLES: Final[dict[str, tuple[str, ...]]] = {
    "Precious metals": PRECIOUS_METALS,
    "Industrial metals": INDUSTRIAL_METALS,
    "Energy commodities": ENERGY_COMMODITY,
    "Agriculture": AGRICULTURE,
}

COMMODITY_FUNDS: Final[tuple[str, ...]] = tuple(
    t for bucket in COMMODITY_ROLES.values() for t in bucket
)

#: Everything that is not a single name.
FUNDS: Final[tuple[str, ...]] = BROAD_FUNDS + COMMODITY_FUNDS

FUND_ROLES: Final[dict[str, tuple[str, ...]]] = {**BROAD_FUND_ROLES, **COMMODITY_ROLES}


# --------------------------------------------------------------------------- #
# Classification
# --------------------------------------------------------------------------- #

_BROAD_SET: Final[frozenset[str]] = frozenset(BROAD_FUNDS)
_COMMODITY_SET: Final[frozenset[str]] = frozenset(COMMODITY_FUNDS)


def kind_for(ticker: str) -> InstrumentKind:
    """Classify a ticker for sizing and prompting.

    Total by design: any ticker gets an answer, and anything unrecognised is
    an ``EQUITY``. That default is never the largest cap, so an unknown or
    misspelled ticker can only be sized down.
    """
    symbol = ticker.strip().upper()
    if symbol in _BROAD_SET:
        return InstrumentKind.BROAD_FUND
    if symbol in _COMMODITY_SET:
        return InstrumentKind.COMMODITY_FUND
    return InstrumentKind.EQUITY


def is_fund(ticker: str) -> bool:
    """True for anything holding a basket or a commodity rather than a company.

    What the prompt path branches on: a fund of either sort has no analysts
    publishing targets on it and no insiders filing Form 4.
    """
    return kind_for(ticker) is not InstrumentKind.EQUITY


# --------------------------------------------------------------------------- #
# Exposure groups
# --------------------------------------------------------------------------- #
# Deliberately coarse, and deliberately spanning both sleeves. GOOGL sits with
# technology rather than in a communication group of its own because in a
# drawdown that is what it trades like, and the point of a group is to bound
# correlated risk rather than to reproduce a classification standard.

EXPOSURE_GROUPS: Final[dict[str, tuple[str, ...]]] = {
    "Technology": TECHNOLOGY + COMMUNICATION,
    "Financials": FINANCIALS,
    "Health care": HEALTH_CARE,
    "Industrials": INDUSTRIALS,
    "Consumer": CONSUMER_DISCRETIONARY + CONSUMER_STAPLES,
    # One energy bet, whether taken through a driller or the barrel.
    "Energy": ENERGY_EQUITY + ENERGY_COMMODITY,
    "US broad equity": US_BROAD,
    "International equity": INTERNATIONAL,
    "Real estate": REAL_ESTATE,
    "Duration": DURATION,
    "Broad commodities": BROAD_COMMODITY,
    "Precious metals": PRECIOUS_METALS,
    "Industrial metals": INDUSTRIAL_METALS,
    "Agriculture": AGRICULTURE,
}

_GROUP_OF: Final[dict[str, str]] = {
    ticker: group for group, tickers in EXPOSURE_GROUPS.items() for ticker in tickers
}

#: What an unrecognised ticker belongs to. Its own group, so it is bounded by
#: the group cap like everything else but cannot consume another group's room.
UNGROUPED: Final[str] = "ungrouped"


def group_for(ticker: str) -> str:
    return _GROUP_OF.get(ticker.strip().upper(), UNGROUPED)


__all__ = [
    "InstrumentKind",
    "SINGLE_NAME_SECTORS",
    "SINGLE_NAMES",
    "BROAD_FUND_ROLES",
    "BROAD_FUNDS",
    "COMMODITY_ROLES",
    "COMMODITY_FUNDS",
    "FUNDS",
    "FUND_ROLES",
    "EXPOSURE_GROUPS",
    "UNGROUPED",
    "kind_for",
    "is_fund",
    "group_for",
]
