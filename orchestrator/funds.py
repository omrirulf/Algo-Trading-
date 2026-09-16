"""What a fund actually is, in the terms that apply to a fund.

A fund was being described to the model with the company form: sector,
market cap, profit margin, revenue growth, next earnings date. An index has
none of those, so the block rendered as seven lines of ``n/a`` -- and worse,
yfinance occasionally fills one in with nonsense. The first 80-ticker cycle
showed the model a *forward P/E of -4,036* for a Treasury bond fund, and the
model scored that fund's fundamentals -0.1.

This is the honest replacement. Three shapes, because three kinds of fund
answer three different questions:

``equity``
    A basket of shares. What it holds is what matters: the weighted P/E and
    P/B of the holdings, their earnings growth, the yield, the cost of
    owning it, and the top names.
``bond``
    A basket of debt. Price is a function of yield and duration -- a 20-year
    Treasury fund and a high-yield credit fund are both "bonds" and behave
    nothing alike, and the numbers that separate them are here, including the
    ratings mix, which is the difference stated plainly.
``none``
    A single commodity. Gold has no P/E, no yield and no balance sheet, and
    inventing a form for it would be the original mistake in a new costume.
    ``build_snapshot`` returns ``None`` and the section is omitted outright.

Pure parsing, like its sibling modules: ``orchestrator.context`` does the
fetching and hands the payloads in.

A note on trusting Yahoo, learned the hard way. The first live run of this
module returned a P/E of 0.06 for an energy fund -- an earnings yield wearing
a P/E's name, because Yahoo stores several holdings ratios inverted and lets
its own formatter flip them back, while the ``raw`` field yfinance reads keeps
them inverted. The suppression band was written to catch *absurd* numbers and
0.06 is not absurd, it is merely wrong, which is worse. So the parsing here
does not only reject: where the unit is knowable it converts, and where it is
not it says nothing.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Optional

from config.instruments import CREDIT, DURATION, InstrumentKind, kind_for
from orchestrator import formatting as fmt

#: Holdings named in the prompt. Enough to recognise what the fund is, few
#: enough that forty funds do not bury the rest of the context.
MAX_TOP_HOLDINGS = 5
MAX_SECTORS = 4

#: A P/E outside this range is not a valuation, it is a data error. yfinance
#: reports a *negative* forward P/E for bond funds (there are no earnings to
#: divide by) and occasionally four-digit values where a fund holds one
#: loss-making name. Both are suppressed rather than shown: a number the
#: model cannot use is worse than a stated blank, because it looks usable.
#:
#: The floor used to be zero, which let through the inverted ratios described
#: at the top of this file: 0.06 is a perfectly ordinary-looking number and
#: passed straight to the model as XLE's P/E. A basket of shares cannot cost
#: less than one year of its own earnings, so the floor is now one.
MIN_SANE_PE = 1.0
MAX_SANE_PE = 1000.0

#: How the inversion is detected. It is decided once for the whole block
#: rather than per field, because the ratios in a payload are consistent with
#: each other: if the P/E is inverted, so are the P/B and P/S beside it. Per
#: field would mean guessing at a P/B of 0.8, which a deep-value or emerging
#: market basket genuinely can have, and guessing is what produced the bug.
RECIPROCAL_PE_CEILING = 1.0

#: Duration outside this band is not a duration. The longest Treasury fund on
#: the watchlist sits near seventeen years; anything past forty is a parsing
#: error, and zero or negative is a missing field dressed as a number.
MAX_SANE_DURATION = 40.0

#: Yahoo spells a fund's yield two ways and does not agree with itself about
#: the units -- ``yield`` arrives as a fraction (0.0295) while
#: ``dividendYield`` has been a percentage (2.95) in recent versions, and the
#: convention has flipped before. Rather than trust either spelling, anything
#: above this is read as a percentage and scaled down. The rule is wrong for a
#: fund yielding under 1% *reported in percent*, which it would read as a
#: fraction; that error is bounded and small, while the one it prevents tells
#: the model a bond fund pays 295%.
MAX_PLAUSIBLE_YIELD = 1.0

#: Rating buckets named in the prompt. Yahoo returns the full ladder down to
#: "below B" and most of it is noise for a fund that is 95% one rating.
MAX_RATING_BUCKETS = 4

#: Yahoo's sector and rating keys are machine spellings. These are the ones
#: that do not survive a naive de-underscoring.
_LABELS = {
    "realestate": "Real estate",
    "aaa": "AAA", "aa": "AA", "a": "A", "bbb": "BBB",
    "bb": "BB", "b": "B", "below_b": "Below B", "us_government": "US government",
    "other": "Other", "bondPosition": "Bonds", "stockPosition": "Stocks",
    "cashPosition": "Cash", "otherPosition": "Other", "preferredPosition": "Preferred",
    "convertiblePosition": "Convertible",
}

#: Funds whose prompt should read as debt rather than equity.
_BOND_TICKERS = frozenset(DURATION + CREDIT)

EQUITY_FUND = "equity"
BOND_FUND = "bond"
NO_FUND_SECTION = "none"


def fund_shape(ticker: str) -> str:
    """Which of the three forms this ticker's fund block takes."""
    kind = kind_for(ticker)
    if kind is InstrumentKind.EQUITY:
        return NO_FUND_SECTION
    if kind is InstrumentKind.COMMODITY_FUND:
        return NO_FUND_SECTION
    if ticker.strip().upper() in _BOND_TICKERS:
        return BOND_FUND
    return EQUITY_FUND


def _value(payload: Any, *names: str) -> Optional[float]:
    """One number out of a yfinance payload, whatever container it arrived in.

    ``funds_data`` returns a Series here, a one-row DataFrame there and a
    plain dict elsewhere depending on the property and the version. Rather
    than branch on type at every call site, every shape is probed for every
    spelling of the key and the first usable number wins.
    """
    if payload is None:
        return None
    for name in names:
        value = None
        try:
            if isinstance(payload, dict):
                value = payload.get(name)
            elif hasattr(payload, "columns") and name in getattr(payload, "columns", []):
                column = payload[name]
                value = column.iloc[0] if len(column) else None
            elif hasattr(payload, "index") and name in list(getattr(payload, "index", [])):
                value = payload.loc[name]
                # A one-column frame indexed by field name yields a Series.
                value = value.iloc[0] if hasattr(value, "iloc") and len(value) else value
            elif hasattr(payload, name):
                value = getattr(payload, name)
        except Exception:  # noqa: BLE001 - an odd shape is a missing value
            value = None
        if fmt.is_missing(value):
            continue
        try:
            return float(value)
        except (TypeError, ValueError):
            continue
    return None


def _sane_pe(value: Optional[float]) -> Optional[float]:
    """A P/E, or ``None`` when the number cannot be a valuation."""
    if value is None:
        return None
    return value if MIN_SANE_PE < value < MAX_SANE_PE else None


def _sane_duration(value: Optional[float]) -> Optional[float]:
    """Years, or ``None`` when the number cannot be a span of years."""
    if value is None:
        return None
    return value if 0.0 < value < MAX_SANE_DURATION else None


def _invert(value: Optional[float]) -> Optional[float]:
    """The other side of a ratio, when there is one to take."""
    if value is None or value <= 0:
        return None
    return 1.0 / value


def _price_ratios(payload: Any) -> tuple[Optional[float], Optional[float], Optional[float]]:
    """``(P/E, P/B, P/S)`` for a basket, the right way up.

    See the module docstring: Yahoo hands these over inverted often enough
    that reading them at face value is how a fund got a P/E of 0.06. The P/E
    decides for the block, since a share basket costing less than one year of
    its earnings does not exist and the three ratios travel together.
    """
    pe = _value(payload, "priceToEarnings", "Price/Earnings")
    pb = _value(payload, "priceToBook", "Price/Book")
    ps = _value(payload, "priceToSales", "Price/Sales")
    if pe is not None and 0.0 < pe < RECIPROCAL_PE_CEILING:
        pe, pb, ps = _invert(pe), _invert(pb), _invert(ps)
    return _sane_pe(pe), pb, ps


def _fund_yield(info: Optional[dict]) -> Optional[float]:
    """A fund's yield as a fraction, whichever way Yahoo spelled it.

    ``funds_data`` has no yield at all -- its ``fund_overview`` carries only
    the category, family and legal type -- so this is the only place it can
    come from, and the first version of this module looked for it in the one
    payload that could never hold it.
    """
    info = info or {}
    for key in ("yield", "dividendYield"):
        value = _as_float(info.get(key))
        if value is None or value <= 0:
            continue
        return value / 100.0 if value > MAX_PLAUSIBLE_YIELD else value
    return None


def _label(key: str) -> str:
    """A sector or rating key as a person would write it."""
    text = str(key).strip()
    if text in _LABELS:
        return _LABELS[text]
    return text.replace("_", " ").capitalize()


def _mix(payload: Any, limit: int) -> list[str]:
    """``Name 42%`` strings for the largest slices of a weighting dict."""
    rows = [(name, weight) for name, weight in _rows(payload, limit=None) if weight]
    rows.sort(key=lambda row: row[1], reverse=True)
    return [f"{_label(name)} {fmt.pct(weight, signed=False)}" for name, weight in rows[:limit]]


def _rows(frame: Any, limit: Optional[int]) -> list[tuple[str, Optional[float]]]:
    """``(name, weight)`` pairs out of a holdings or weighting payload.

    A ``limit`` of ``None`` takes everything, for callers that need to sort
    before they truncate.
    """
    out: list[tuple[str, Optional[float]]] = []
    if frame is None:
        return out
    try:
        if isinstance(frame, dict):
            items = list(frame.items())[:limit]
            return [(str(k), _as_float(v)) for k, v in items]
        if hasattr(frame, "iterrows"):
            columns = [str(c) for c in getattr(frame, "columns", [])]
            name_col = next((c for c in columns if "name" in c.lower()), None)
            weight_col = next(
                (c for c in columns if "percent" in c.lower() or "weight" in c.lower()), None
            )
            for index, row in list(frame.iterrows())[:limit]:
                label = str(row[name_col]) if name_col else str(index)
                out.append((label, _as_float(row[weight_col]) if weight_col else None))
            return out
        if hasattr(frame, "items"):  # a Series of weights keyed by name
            for key, value in list(frame.items())[:limit]:
                out.append((str(key), _as_float(value)))
    except Exception:  # noqa: BLE001
        return out
    return out


def _as_float(value: Any) -> Optional[float]:
    if fmt.is_missing(value):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


@dataclass(frozen=True)
class FundSnapshot:
    """What this fund holds, what it costs, and what it yields."""

    ticker: str = ""
    shape: str = EQUITY_FUND
    category: Optional[str] = None
    #: Equity funds
    holdings_pe: Optional[float] = None
    holdings_pb: Optional[float] = None
    holdings_ps: Optional[float] = None
    holdings_earnings_growth: Optional[float] = None
    #: Bond funds
    duration: Optional[float] = None
    maturity: Optional[float] = None
    credit_quality: Optional[float] = None
    credit_mix: list[str] = field(default_factory=list)
    #: Both
    dividend_yield: Optional[float] = None
    expense_ratio: Optional[float] = None
    total_assets: Optional[float] = None
    top_holdings: list[str] = field(default_factory=list)
    sector_mix: list[str] = field(default_factory=list)
    asset_mix: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)

    def as_lines(self) -> list[str]:
        lines = [f"Fund type: {self.category or fmt.NA}"]
        if self.shape == BOND_FUND:
            lines.append(
                f"Yield and rate risk: yield {fmt.pct(self.dividend_yield, signed=False)} | "
                f"duration {fmt.num(self.duration)} years | "
                f"average maturity {fmt.num(self.maturity)} years"
            )
            credit = ", ".join(self.credit_mix) if self.credit_mix else fmt.NA
            lines.append(f"Credit quality: {credit}")
        else:
            lines.append(
                f"What it holds: P/E {fmt.num(self.holdings_pe)} | "
                f"P/B {fmt.num(self.holdings_pb)} | "
                f"P/S {fmt.num(self.holdings_ps)} | "
                f"3y earnings growth {fmt.pct(self.holdings_earnings_growth)}"
            )
            lines.append(f"Yield: {fmt.pct(self.dividend_yield, signed=False)}")
        lines.append(
            f"Cost and size: expense ratio {fmt.pct(self.expense_ratio, signed=False)} | "
            f"net assets {fmt.money(self.total_assets)}"
        )
        if self.asset_mix:
            lines.append(f"What it is made of: {', '.join(self.asset_mix)}")
        if self.top_holdings:
            lines.append(f"Largest holdings: {', '.join(self.top_holdings)}")
        if self.sector_mix:
            lines.append(f"Sector mix: {', '.join(self.sector_mix)}")
        return lines


def build_snapshot(
    ticker: str,
    equity_holdings: Any = None,
    bond_holdings: Any = None,
    bond_ratings: Any = None,
    fund_operations: Any = None,
    fund_overview: Any = None,
    top_holdings: Any = None,
    sector_weightings: Any = None,
    asset_classes: Any = None,
    info: Optional[dict] = None,
) -> Optional[FundSnapshot]:
    """A fund's own numbers, or ``None`` when the fund has none to give.

    ``None`` for a single-commodity fund is the point, not an omission: gold
    has no valuation, no yield and no holdings, and the caller omits the
    section entirely rather than printing a form full of blanks.
    """
    shape = fund_shape(ticker)
    if shape == NO_FUND_SECTION:
        return None

    info = info or {}
    category = None
    if isinstance(fund_overview, dict):
        category = fund_overview.get("categoryName") or fund_overview.get("category")
    category = category or info.get("category") or info.get("longName")

    holdings = _rows(top_holdings, MAX_TOP_HOLDINGS)
    pe, pb, ps = _price_ratios(equity_holdings)

    return FundSnapshot(
        ticker=ticker.strip().upper(),
        shape=shape,
        category=str(category) if category else None,
        holdings_pe=pe,
        holdings_pb=pb,
        holdings_ps=ps,
        holdings_earnings_growth=_value(
            equity_holdings, "threeYearEarningsGrowth", "3 Year Earnings Growth"
        ),
        duration=_sane_duration(_value(bond_holdings, "duration", "Duration")),
        maturity=_sane_duration(_value(bond_holdings, "maturity", "Maturity")),
        credit_quality=_value(bond_holdings, "creditQuality", "Credit Quality"),
        credit_mix=_mix(bond_ratings, MAX_RATING_BUCKETS),
        dividend_yield=_fund_yield(info),
        expense_ratio=_value(fund_operations, "annualReportExpenseRatio",
                             "Annual Report Expense Ratio")
        or _as_float(info.get("annualReportExpenseRatio")),
        total_assets=_value(fund_operations, "totalNetAssets", "Total Net Assets")
        or _as_float(info.get("totalAssets")),
        top_holdings=[
            f"{name} {fmt.pct(weight, signed=False)}" if weight is not None else name
            for name, weight in holdings
        ],
        sector_mix=_mix(sector_weightings, MAX_SECTORS),
        asset_mix=_mix(asset_classes, MAX_SECTORS),
    )


__all__ = [
    "FundSnapshot",
    "build_snapshot",
    "fund_shape",
    "EQUITY_FUND",
    "BOND_FUND",
    "NO_FUND_SECTION",
    "MAX_SANE_PE",
    "MIN_SANE_PE",
    "MAX_SANE_DURATION",
]
