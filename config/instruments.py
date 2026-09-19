"""What we trade, what kind of thing each ticker is, and what it correlates with.

Four kinds, because they carry four different risks and so deserve four
different position caps:

``EQUITY``
    One company. Idiosyncratic: it can gap on a fraud, a failed trial or a
    guidance cut. It is also the only kind with analyst coverage and insider
    filings, so it is the only kind where all five prompt dimensions have
    content.

``BROAD_FUND``
    A basket of hundreds of positions spanning sectors, countries or issuers.
    Internally diversified, so a larger share of equity is appropriate -- the
    diversification argument for index funds and a single-name cap cancel each
    other out.

``FOCUSED_FUND``
    A fund holding many companies, all of them in **one sector or one
    country**. Diversified against a single company failing and not against
    anything else: an energy fund is twenty-three ways of making the same bet
    on the oil price, and a Brazil fund is one currency, one central bank and
    one election. It sits between the two caps above because that is where its
    risk sits -- above a single name, below a fund that spans the world.

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
    FOCUSED_FUND = "focused fund"
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
# What belongs here is a fund whose holdings span sectors, countries or
# issuers. One that holds a hundred companies in a single sector, or a single
# country, is not this -- it is a FOCUSED_FUND below, and it gets a smaller
# cap for it.
#
# RSP rather than SPY: a cap-weighted US index is a concentrated technology
# bet wearing a diversified label, and equal weight is the diversified version
# of the same market.

US_BROAD: Final[tuple[str, ...]] = ("RSP", "IWM")
#: Multi-country by construction. The single-country funds that used to sit
#: here (Japan, Israel) moved to the focused sleeve: one country is one
#: currency, one central bank and one election, which is a narrower bet than
#: this row is sized for.
INTERNATIONAL_BROAD: Final[tuple[str, ...]] = ("VGK", "VWO")
#: Government paper across the curve. Not equity risk, and historically the
#: most reliable diversifier against it -- but only at the long end: SHY is a
#: cash proxy and TIP prices inflation rather than growth, so the curve is
#: carried in pieces rather than as one duration bet.
DURATION: Final[tuple[str, ...]] = ("SHY", "IEF", "TLT", "TIP")
#: Corporate and sovereign credit. Each fund holds hundreds of issuers, so
#: default risk is diversified -- but spread risk is not, and it correlates
#: with equities exactly when that hurts. Hence its own exposure group.
CREDIT: Final[tuple[str, ...]] = ("LQD", "HYG", "EMB")
#: Broad commodity baskets. These *are* diversified across commodities, so
#: they are broad funds rather than commodity funds.
#:
#: That is a statement about *sizing* only. For exposure, DBA is grouped with
#: the grains rather than with DBC -- it holds the same futures they do. See
#: EXPOSURE_GROUPS below.
BROAD_COMMODITY: Final[tuple[str, ...]] = ("DBC", "DBA")
#: The dollar, as a basket against six developed currencies. Here because
#: almost every other row on this list is priced in dollars, so the dollar is
#: a factor in all of them and is otherwise unobservable.
CURRENCY: Final[tuple[str, ...]] = ("UUP",)

BROAD_FUND_ROLES: Final[dict[str, tuple[str, ...]]] = {
    "US broad equity": US_BROAD,
    "International equity": INTERNATIONAL_BROAD,
    "Duration": DURATION,
    "Credit": CREDIT,
    "Broad commodities": BROAD_COMMODITY,
    "Currency": CURRENCY,
}

BROAD_FUNDS: Final[tuple[str, ...]] = tuple(
    t for bucket in BROAD_FUND_ROLES.values() for t in bucket
)


# --------------------------------------------------------------------------- #
# Sleeve 2b: focused funds -- one sector, or one country
# --------------------------------------------------------------------------- #
# The sleeve that makes the watchlist wide enough to be worth reading. A model
# handed only RSP and IWM can say "US equities up" and nothing more useful; a
# story about a rate cut, an oil shock, a drug approval or an election is
# about a *sector* or a *country*, and until this sleeve existed there was
# nowhere for such a story to land.
#
# Why they are not broad funds
# ----------------------------
# A sector fund is diversified against one company failing and against nothing
# else. XLE is twenty-three different ways of being long the oil price. A
# country fund is one currency, one central bank, one government. Sizing
# either like a fund that spans the world would repeat, one level up, the
# error the commodity sleeve exists to avoid: picking a cap from the word
# "fund" rather than from the risk.
#
# Why they are not single names either
# ------------------------------------
# One company can go to zero on a fraud or a failed trial. A sector cannot. So
# the cap sits between the two, at MAX_FOCUSED_FUND_PCT.
#
# Overlap with the broad sleeve is deliberate and is not double-counting: RSP
# already contains every US sector, so a sector position is a *tilt* on top of
# the market, and EXPOSURE_GROUPS is what stops the tilt and the single names
# beneath it adding up to one undiversified bet.

SECTOR_ENERGY: Final[tuple[str, ...]] = ("XLE",)
SECTOR_FINANCIALS: Final[tuple[str, ...]] = ("XLF", "KRE")
SECTOR_HEALTH_CARE: Final[tuple[str, ...]] = ("XLV", "XBI")
#: XLC is here rather than in a communication row of its own for the same
#: reason GOOGL is: in a drawdown it trades like technology.
SECTOR_TECHNOLOGY: Final[tuple[str, ...]] = ("XLK", "XLC", "SMH", "IGV")
SECTOR_INDUSTRIALS: Final[tuple[str, ...]] = ("XLI", "ITA", "IYT")
SECTOR_CONSUMER: Final[tuple[str, ...]] = ("XLY", "XLP")
SECTOR_UTILITIES: Final[tuple[str, ...]] = ("XLU",)
SECTOR_MATERIALS: Final[tuple[str, ...]] = ("XLB",)
#: House builders sit with property rather than with retail. GICS calls them
#: consumer discretionary; rates and housing starts call them real estate, and
#: the point of a grouping here is what a thing trades like.
SECTOR_REAL_ESTATE: Final[tuple[str, ...]] = ("VNQ", "XHB")
#: Miners are equities, not metal -- but they are a levered bet on the metal,
#: so they are grouped with it rather than with materials.
SECTOR_MINERS: Final[tuple[str, ...]] = ("GDX",)

#: Single developed markets. Israel is here on MSCI's classification, and
#: Japan moved down from the broad sleeve with the rest of them.
COUNTRY_DEVELOPED: Final[tuple[str, ...]] = (
    "EWJ", "EIS", "EWU", "EWG", "EWL", "EWN", "EWI", "EWP", "EWD", "EWC", "EWA",
)
#: Single emerging markets. Thinner, more volatile and more prone to a single
#: political event than the developed row, and sized the same -- which is an
#: argument for watching what verify_tickers.py measures on this row in
#: particular.
COUNTRY_EMERGING: Final[tuple[str, ...]] = (
    "MCHI", "INDA", "EWY", "EWT", "EWZ", "EWW", "KSA", "TUR", "EZA", "EPOL", "ARGT",
)

FOCUSED_FUND_ROLES: Final[dict[str, tuple[str, ...]]] = {
    "Sector: energy": SECTOR_ENERGY,
    "Sector: financials": SECTOR_FINANCIALS,
    "Sector: health care": SECTOR_HEALTH_CARE,
    "Sector: technology": SECTOR_TECHNOLOGY,
    "Sector: industrials": SECTOR_INDUSTRIALS,
    "Sector: consumer": SECTOR_CONSUMER,
    "Sector: utilities": SECTOR_UTILITIES,
    "Sector: materials": SECTOR_MATERIALS,
    "Sector: real estate": SECTOR_REAL_ESTATE,
    "Sector: miners": SECTOR_MINERS,
    "Country: developed": COUNTRY_DEVELOPED,
    "Country: emerging": COUNTRY_EMERGING,
}

FOCUSED_FUNDS: Final[tuple[str, ...]] = tuple(
    t for bucket in FOCUSED_FUND_ROLES.values() for t in bucket
)


# --------------------------------------------------------------------------- #
# Sleeve 2c: single-commodity funds
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
FUNDS: Final[tuple[str, ...]] = BROAD_FUNDS + FOCUSED_FUNDS + COMMODITY_FUNDS

FUND_ROLES: Final[dict[str, tuple[str, ...]]] = {
    **BROAD_FUND_ROLES, **FOCUSED_FUND_ROLES, **COMMODITY_ROLES,
}


# --------------------------------------------------------------------------- #
# Classification
# --------------------------------------------------------------------------- #

_BROAD_SET: Final[frozenset[str]] = frozenset(BROAD_FUNDS)
_FOCUSED_SET: Final[frozenset[str]] = frozenset(FOCUSED_FUNDS)
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
    if symbol in _FOCUSED_SET:
        return InstrumentKind.FOCUSED_FUND
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
# Human labels
# --------------------------------------------------------------------------- #
# A ticker is an identifier, not a name. A report that says only "NVO" asks
# the reader to hold 35 symbols in their head; one that says "Novo Nordisk"
# does not. Kept as a static map rather than read from yfinance: the
# watchlist is fixed and curated, so a name is a fact about the list itself,
# and looking one up would mean a network call in a report that is meant to
# work offline from a journal.

DISPLAY_NAMES: Final[dict[str, str]] = {
    # Single names
    "MSFT": "Microsoft",
    "NVDA": "Nvidia",
    "ASML": "ASML",
    "GOOGL": "Alphabet (Google)",
    "JPM": "JPMorgan Chase",
    "RY": "Royal Bank of Canada",
    "HDB": "HDFC Bank",
    "LLY": "Eli Lilly",
    "NVO": "Novo Nordisk",
    "TEVA": "Teva Pharmaceutical",
    "CAT": "Caterpillar",
    "ESLT": "Elbit Systems",
    "TM": "Toyota",
    "MELI": "MercadoLibre",
    "PG": "Procter & Gamble",
    "XOM": "Exxon Mobil",
    # Broad funds
    "RSP": "S&P 500, equal weight",
    "IWM": "US small companies",
    "VGK": "Europe",
    "EWJ": "Japan",
    "VWO": "Emerging markets",
    "EIS": "Israel",
    "VNQ": "US real estate",
    "TLT": "US government bonds, 20+ years",
    "DBC": "Commodities basket",
    "DBA": "Farm goods basket",
    # Sectors -- what an American would call the industry, not the GICS label
    "XLE": "US energy companies",
    "XLF": "US banks and finance",
    "XLV": "US health care",
    "XLK": "US technology",
    "XLI": "US industry",
    "XLY": "US shopping and leisure",
    "XLP": "US everyday goods",
    "XLU": "US electricity and water",
    "XLB": "US materials and chemicals",
    "XLC": "US media and communication",
    # Narrower themes inside those sectors
    "SMH": "Chip makers",
    "IGV": "Software",
    "XBI": "Biotech",
    "KRE": "US regional banks",
    "ITA": "Defence and aerospace",
    "IYT": "Transport and delivery",
    "XHB": "US house builders",
    "GDX": "Gold mining companies",
    # Single countries
    "EWU": "United Kingdom",
    "EWG": "Germany",
    "EWL": "Switzerland",
    "EWN": "Netherlands",
    "EWI": "Italy",
    "EWP": "Spain",
    "EWD": "Sweden",
    "EWC": "Canada",
    "EWA": "Australia",
    "MCHI": "China",
    "INDA": "India",
    "EWY": "South Korea",
    "EWT": "Taiwan",
    "EWZ": "Brazil",
    "EWW": "Mexico",
    "KSA": "Saudi Arabia",
    "TUR": "Turkey",
    "EZA": "South Africa",
    "EPOL": "Poland",
    "ARGT": "Argentina",
    # Bonds and credit
    "SHY": "US government bonds, 1-3 years",
    "IEF": "US government bonds, 7-10 years",
    "TIP": "US inflation-linked bonds",
    "LQD": "US company bonds, safer",
    "HYG": "US company bonds, riskier",
    "EMB": "Developing country bonds",
    # Currency
    "UUP": "US dollar",
    # Single commodities
    "GLD": "Gold",
    "SLV": "Silver",
    "CPER": "Copper",
    "USO": "Oil",
    "UNG": "Natural gas",
    "CORN": "Corn",
    "WEAT": "Wheat",
    "SOYB": "Soybeans",
    "CANE": "Sugar",
}

#: What each kind is called in a report. The enum names are for code; these
#: are for a person, and they say what the thing *is* rather than how the
#: sizing code groups it.
SLEEVE_LABELS: Final[dict[InstrumentKind, str]] = {
    InstrumentKind.EQUITY: "Company",
    InstrumentKind.BROAD_FUND: "Index fund",
    InstrumentKind.FOCUSED_FUND: "Sector or country",
    InstrumentKind.COMMODITY_FUND: "Commodity",
}


def name_for(ticker: str) -> str:
    """The readable name, or the ticker itself when there is no entry.

    Falling back to the symbol keeps this safe for a ticker added to the
    watchlist before anyone writes its name down.
    """
    symbol = ticker.strip().upper()
    return DISPLAY_NAMES.get(symbol, symbol)


def sleeve_label(ticker: str) -> str:
    """What this ticker is, in one phrase a non-specialist can read."""
    return SLEEVE_LABELS[kind_for(ticker)]


# --------------------------------------------------------------------------- #
# Exposure groups
# --------------------------------------------------------------------------- #
# Deliberately coarse, and deliberately spanning both sleeves. GOOGL sits with
# technology rather than in a communication group of its own because in a
# drawdown that is what it trades like, and the point of a group is to bound
# correlated risk rather than to reproduce a classification standard.

EXPOSURE_GROUPS: Final[dict[str, tuple[str, ...]]] = {
    # Each sector fund sits with the single names it is a diversified version
    # of. This is the check that makes the focused sleeve safe to widen: NVDA
    # plus MSFT plus XLK plus SMH is one technology bet made four times, and
    # without this row every per-ticker cap would be satisfied while it
    # happened.
    "Technology": TECHNOLOGY + COMMUNICATION + SECTOR_TECHNOLOGY,
    "Financials": FINANCIALS + SECTOR_FINANCIALS,
    "Health care": HEALTH_CARE + SECTOR_HEALTH_CARE,
    "Industrials": INDUSTRIALS + SECTOR_INDUSTRIALS,
    "Consumer": CONSUMER_DISCRETIONARY + CONSUMER_STAPLES + SECTOR_CONSUMER,
    # One energy bet, whether taken through a driller, a sector fund or the
    # barrel.
    "Energy": ENERGY_EQUITY + ENERGY_COMMODITY + SECTOR_ENERGY,
    "Utilities": SECTOR_UTILITIES,
    "Materials": SECTOR_MATERIALS,
    "Real estate": SECTOR_REAL_ESTATE,
    "US broad equity": US_BROAD,
    # Split in two, because they are not one bet. A European fund and a Japan
    # fund move together far more than either moves with Brazil, and holding
    # them under one 25% ceiling would have made "the rest of the world" a
    # single position.
    "Developed international": ("VGK",) + COUNTRY_DEVELOPED,
    "Emerging markets": ("VWO",) + COUNTRY_EMERGING,
    "Duration": DURATION,
    # Its own group rather than part of duration: credit sells off with
    # equities, while government paper rallies. Putting them together would
    # net two opposite risks into one number.
    "Credit": CREDIT,
    "US dollar": CURRENCY,
    # DBC only. DBA is a broad fund for sizing -- it spans about ten crops --
    # but it is not a *separate bet* from the grain funds below, because it
    # holds the same futures: corn, wheat, soybeans and sugar are four of its
    # largest positions, and the note on AGRICULTURE above already relies on
    # that ("coffee exposure now comes through DBA"). Holding DBA alongside
    # CORN, WEAT, SOYB and CANE was one agricultural bet spread across two
    # groups, each with its own ceiling.
    #
    # Measured rather than assumed: of the 171 pairs of exposure groups,
    # this was the only one to clear |excess r| >= 0.6 over 2007-present --
    # 0.66 over the last year and 0.67 in the tail, after removing the
    # factor every holding shares (analysis/correlations.py).
    "Broad commodities": ("DBC",),
    # Miners with the metal: a gold miner is a levered bet on gold, not a
    # diversifier from it.
    "Precious metals": PRECIOUS_METALS + SECTOR_MINERS,
    "Industrial metals": INDUSTRIAL_METALS,
    "Agriculture": AGRICULTURE + ("DBA",),
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
    "FOCUSED_FUND_ROLES",
    "FOCUSED_FUNDS",
    "COMMODITY_ROLES",
    "COMMODITY_FUNDS",
    "FUNDS",
    "FUND_ROLES",
    "EXPOSURE_GROUPS",
    "UNGROUPED",
    "kind_for",
    "is_fund",
    "group_for",
    "DISPLAY_NAMES",
    "SLEEVE_LABELS",
    "name_for",
    "sleeve_label",
]
