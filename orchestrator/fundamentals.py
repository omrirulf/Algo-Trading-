"""Company fundamentals parsed out of yfinance's ``Ticker.info`` dictionary.

Pure parsing: ``build_snapshot`` takes the dict and the earnings calendar that
``orchestrator.context`` fetched and returns plain data, so every field and
every gap is testable without touching the network.

Only fields with an unambiguous unit are carried. ``dividendYield``, for one,
has been a fraction in some yfinance releases and a percentage in others, and a
number the prompt cannot label correctly is worse than no number at all.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date, datetime
from typing import Any, Optional

from orchestrator import formatting as fmt

#: yfinance key -> snapshot field, for the values that are plain fractions
#: (0.243 meaning 24.3%) or plain multiples.
_FRACTIONS = {
    "profitMargins": "profit_margin",
    "operatingMargins": "operating_margin",
    "revenueGrowth": "revenue_growth",
    "earningsGrowth": "earnings_growth",
    "returnOnEquity": "return_on_equity",
    "shortPercentOfFloat": "short_percent_of_float",
}

_MULTIPLES = {
    "trailingPE": "trailing_pe",
    "forwardPE": "forward_pe",
    "priceToBook": "price_to_book",
    "trailingPegRatio": "peg_ratio",
    "beta": "beta",
}


@dataclass(frozen=True)
class FundamentalSnapshot:
    sector: Optional[str] = None
    industry: Optional[str] = None
    market_cap: Optional[float] = None
    trailing_pe: Optional[float] = None
    forward_pe: Optional[float] = None
    price_to_book: Optional[float] = None
    peg_ratio: Optional[float] = None
    profit_margin: Optional[float] = None
    operating_margin: Optional[float] = None
    revenue_growth: Optional[float] = None
    earnings_growth: Optional[float] = None
    return_on_equity: Optional[float] = None
    #: yfinance reports this already multiplied by 100, i.e. 145.0 means 145%.
    debt_to_equity: Optional[float] = None
    free_cash_flow: Optional[float] = None
    short_percent_of_float: Optional[float] = None
    beta: Optional[float] = None
    next_earnings_date: Optional[str] = None

    def as_dict(self) -> dict:
        return asdict(self)

    def as_lines(self) -> list[str]:
        return [
            f"Sector: {self.sector or fmt.NA} / {self.industry or fmt.NA} | "
            f"market cap {fmt.money(self.market_cap)}",
            f"Valuation: trailing P/E {fmt.num(self.trailing_pe)} | "
            f"forward P/E {fmt.num(self.forward_pe)} | "
            f"P/B {fmt.num(self.price_to_book)} | PEG {fmt.num(self.peg_ratio)}",
            f"Profitability: profit margin {fmt.pct(self.profit_margin, signed=False)} | "
            f"operating margin {fmt.pct(self.operating_margin, signed=False)} | "
            f"ROE {fmt.pct(self.return_on_equity, signed=False)}",
            f"Growth (YoY): revenue {fmt.pct(self.revenue_growth)} | "
            f"earnings {fmt.pct(self.earnings_growth)}",
            f"Balance sheet: debt/equity {fmt.points(self.debt_to_equity)} | "
            f"free cash flow {fmt.money(self.free_cash_flow)}",
            f"Risk: beta {fmt.num(self.beta)} | "
            f"short interest {fmt.pct(self.short_percent_of_float, signed=False)} of float",
            f"Next earnings: {self.next_earnings_date or fmt.NA}",
        ]


def build_snapshot(info: dict[str, Any], calendar: Any = None) -> FundamentalSnapshot:
    """Turn a yfinance ``info`` dict (and optional calendar) into a snapshot."""
    info = info or {}
    values: dict[str, Any] = {
        "sector": _text(info.get("sector")),
        "industry": _text(info.get("industry")),
        "market_cap": fmt.clean(info.get("marketCap")),
        "debt_to_equity": fmt.clean(info.get("debtToEquity")),
        "free_cash_flow": fmt.clean(info.get("freeCashflow")),
        "next_earnings_date": parse_earnings_date(calendar),
    }
    for source, field in {**_FRACTIONS, **_MULTIPLES}.items():
        values[field] = fmt.clean(info.get(source))
    return FundamentalSnapshot(**values)


def parse_earnings_date(calendar: Any) -> Optional[str]:
    """Pull the next earnings date out of whatever shape yfinance returned.

    ``Ticker.calendar`` has been a DataFrame in some versions and a dict in
    others, and the value may be a single date or a confirmed/estimated pair.
    """
    if calendar is None:
        return None

    raw: Any = None
    if isinstance(calendar, dict):
        raw = calendar.get("Earnings Date")
    else:
        try:
            raw = calendar.loc["Earnings Date"]
        except (AttributeError, KeyError, TypeError):
            return None

    if isinstance(raw, (list, tuple)):
        candidates = list(raw)
    elif hasattr(raw, "tolist") and not isinstance(raw, (str, bytes)):
        candidates = list(raw.tolist())
    else:
        candidates = [raw]

    for candidate in candidates:
        rendered = _as_date(candidate)
        if rendered:
            return rendered
    return None


def _as_date(value: Any) -> Optional[str]:
    if value is None or fmt.is_missing(value):
        return None
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str) and value.strip():
        return value.strip()[:10]
    return None


def _text(value: Any) -> Optional[str]:
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None
