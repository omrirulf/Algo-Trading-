"""Prices and rates for the report: fetched for the whole fund table from one fixed day, so the requests show nothing.

The engine's only use of the network (section 2.6). Every fund in the public
table is fetched from ``FIXED_START`` whatever the owner holds; a fund the
owner holds that is not in the table (listed in the private ``plan.csv``)
is fetched on its own. The quote lines are the dollar ones (``Fund.yahoo``),
and a line whose quote currency is not dollars is refused, named by its
place in the table, never by the owner's rows.

The rate table is ``analysis.boi_rates.build``: the Bank of Israel's
representative rate for every weekday, the European Central Bank's crossed
through the euro for a weekday the Bank did not publish, and the last
earlier rate after that, each counted. A weekend day is the ledger's rule
(``investor.ledger``).

Nothing here logs a ticker: the price library's own loggers are silenced
before any request, and a failed fetch is one line saying that a fetch
failed, without the name.
"""

from __future__ import annotations

import logging
from bisect import bisect_left
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from typing import Callable, Mapping, Optional, Protocol

from investor.funds import FUNDS, Fund, fund

#: Every fund in the table is fetched from here (a public date, nothing of the owner's).
FIXED_START = date(2015, 1, 1)

#: Loggers that would name a ticker on a failed request.
_NOISY = ("yfinance", "peewee", "httpx", "httpcore", "urllib3", "requests")

log = logging.getLogger(__name__)


class MarketError(RuntimeError):
    """The prices or the rates could not be fetched. Its text names no fund of the owner's."""


class Market(Protocol):
    as_of: date

    def close(self, ticker: str) -> Optional[float]: ...

    def rate(self, day: date) -> float: ...

    def first_day(self, ticker: str) -> Optional[date]: ...

    def close_on_or_after(self, ticker: str, day: date) -> Optional[tuple[date, float]]: ...

    def dividends(self, ticker: str, start: date, end: date) -> list[tuple[date, float]]: ...

    def fallback_days(self) -> list[tuple[date, str]]: ...


@dataclass
class Series:
    """One fund's daily closes and per-share dividends, in date order."""

    days: list[date]
    closes: list[float]
    dividends: dict[date, float] = field(default_factory=dict)


@dataclass
class TableMarket:
    """A market from tables already in memory: the tests' market, and the fetched one."""

    as_of: date
    series: dict[str, Series]
    rates: Mapping[date, float]
    sources: Mapping[date, str] = field(default_factory=dict)

    def close(self, ticker: str) -> Optional[float]:
        bar = self.close_on_or_before(ticker, self.as_of)
        return bar[1] if bar else None

    def rate(self, day: date) -> float:
        try:
            return float(self.rates[day])
        except KeyError:
            raise KeyError(f"no rate for {day.isoformat()}") from None

    def first_day(self, ticker: str) -> Optional[date]:
        s = self.series.get(ticker)
        return s.days[0] if s and s.days else None

    def close_on_or_after(self, ticker: str, day: date) -> Optional[tuple[date, float]]:
        s = self.series.get(ticker)
        if not s or not s.days:
            return None
        i = bisect_left(s.days, day)
        return (s.days[i], s.closes[i]) if i < len(s.days) else None

    def close_on_or_before(self, ticker: str, day: date) -> Optional[tuple[date, float]]:
        s = self.series.get(ticker)
        if not s or not s.days:
            return None
        i = bisect_left(s.days, day + timedelta(days=1)) - 1
        return (s.days[i], s.closes[i]) if i >= 0 else None

    def dividends(self, ticker: str, start: date, end: date) -> list[tuple[date, float]]:
        s = self.series.get(ticker)
        if not s:
            return []
        return sorted((d, v) for d, v in s.dividends.items() if start < d <= end and v > 0)

    def fallback_days(self) -> list[tuple[date, str]]:
        return sorted((d, src) for d, src in self.sources.items() if src != "boi")


def quiet() -> None:
    """Silence every logger that could print a ticker on a failed request."""
    for name in _NOISY:
        logger = logging.getLogger(name)
        logger.setLevel(logging.CRITICAL + 1)
        logger.propagate = False
        logger.disabled = True


def _yahoo_series(symbol: str, start: date, end: date) -> Optional[Series]:
    import yfinance as yf

    frame = yf.Ticker(symbol).history(start=start.isoformat(), end=(end + timedelta(days=1)).isoformat(),
                                      interval="1d", auto_adjust=False)
    if frame is None or frame.empty or "Close" not in frame.columns:
        return None
    frame = frame.dropna(subset=["Close"])
    days = [ts.date() if hasattr(ts, "date") else ts for ts in frame.index]
    closes = [float(v) for v in frame["Close"].tolist()]
    dividends: dict[date, float] = {}
    if "Dividends" in frame.columns:
        for day, value in zip(days, frame["Dividends"].tolist()):
            if value and value > 0:
                dividends[day] = float(value)
    return Series(days, closes, dividends)


def _quote_currency(symbol: str) -> Optional[str]:
    import yfinance as yf

    try:
        info = yf.Ticker(symbol).fast_info
        currency = info["currency"] if "currency" in info else None
    except Exception:  # noqa: BLE001 - the check is advisory; the fetch itself decides
        return None
    return str(currency).upper() if currency else None


def fetch_market(extra_tickers: tuple[str, ...] = (), *, start: date = FIXED_START, as_of: Optional[date] = None,
                 fetch: Callable[[str, date, date], Optional[Series]] = _yahoo_series,
                 currency_of: Callable[[str], Optional[str]] = _quote_currency,
                 rates: Optional[Callable[[date, date], object]] = None) -> TableMarket:
    """Every table fund from ``start``, plus ``extra_tickers`` by name; the rates from the earliest day needed."""
    quiet()
    today = as_of or (datetime.now(timezone.utc) - timedelta(days=1)).date()
    series: dict[str, Series] = {}
    for number, known in enumerate(FUNDS, start=1):
        currency = currency_of(known.yahoo)
        if currency is not None and currency != known.currency:
            raise MarketError(f"fund table line {number}: its quote line is not in {known.currency}")
        try:
            got = fetch(known.yahoo, start, today)
        except Exception as exc:  # noqa: BLE001 - one fund's failure is one line, without its name
            log.warning("fund table line %d: fetch failed (%s)", number, type(exc).__name__)
            got = None
        if got is not None:
            series[known.ticker] = got
    for ticker in extra_tickers:
        if ticker in series or fund(ticker) is not None:
            continue
        try:
            got = fetch(ticker, start, today)
        except Exception as exc:  # noqa: BLE001
            log.warning("a fund outside the table: fetch failed (%s)", type(exc).__name__)
            got = None
        if got is not None:
            series[ticker] = got
    if not series:
        raise MarketError("no prices could be fetched")
    last = max(s.days[-1] for s in series.values() if s.days)
    table = (rates or _boi_table)(start, last)
    return TableMarket(last, series, table.as_dict(), {entry.day: entry.source for entry in table.entries})


def _boi_table(start: date, end: date):
    from analysis.boi_rates import RateError, build

    try:
        return build(start, end)
    except RateError as exc:
        raise MarketError(f"the rate table could not be built ({type(exc).__name__})") from None


__all__ = ["FIXED_START", "Market", "MarketError", "Series", "TableMarket", "fetch_market", "quiet"]
