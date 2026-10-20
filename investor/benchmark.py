"""The same shekels, on the same days, in VT and in VWRA, held (section 7.4).

Every deposit into a taxable account (a dollar deposit at its day's rate; a
shekel one after the conversion cost) buys VT, and separately VWRA, at that
day's close in whole shares after the trading cost; money left over waits
for the next deposit. A withdrawal sells the same amount, FIFO. A lot held
before the records start, or transferred in, counts as a deposit of its
cost on its own purchase day. A transfer between the owner's own accounts
is neither (T40).

VT pays out: each dividend, less the US tax withheld, buys whole shares on
its day (a new lot, rule c); Israel's extra tax is usually 0 (T10). VWRA
accumulates: no dividend rows, and no Israeli tax until it is sold
(accountant question 5). Money that went in before VWRA's first price is
shown as "n/a" for VWRA.

Each book is its own person-year: its own netting, loss carried forward and
tax. It is shown after tax "if sold today" (this year's tax if everything
were sold; a finished year's tax counts as paid from outside, as it does for
the owner's own accounts), with a money-weighted return a year -- a yearly
return that counts when each shekel went in and out. The experiment's
daily-return code is not used: it reads a deposit as a gain.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from datetime import date
from typing import Callable, Iterable, Optional, Protocol, Sequence

from analysis.israel_tax import DEFAULT_RULES, TaxBook, TaxRules, year_tax
from investor.funds import CostTable, DEFAULT_COSTS, fund
from investor.ledger import Flow

VT = "VT"
VWRA = "VWRA"
BOOKS: tuple[str, ...] = (VT, VWRA)


class PriceHistory(Protocol):
    """Daily closes and per-share dividends of one fund, from the fetch."""

    def first_day(self, ticker: str) -> Optional[date]: ...

    def close_on_or_after(self, ticker: str, day: date) -> Optional[tuple[date, float]]: ...

    def dividends(self, ticker: str, start: date, end: date) -> list[tuple[date, float]]: ...


@dataclass
class _Held:
    ticker: str
    book: TaxBook
    cash_usd: float = 0.0
    shares: float = 0.0
    first_bought: Optional[date] = None
    #: (day, shekels in or out) for the money-weighted return.
    cash_flows: list[tuple[date, float]] = field(default_factory=list)


@dataclass(frozen=True)
class BenchmarkBook:
    ticker: str
    available: bool
    market_ils: float = 0.0
    tax_if_sold_ils: float = 0.0
    after_tax_ils: float = 0.0
    shares: float = 0.0
    cash_usd: float = 0.0
    #: A yearly rate, or None when it cannot be reckoned.
    money_weighted: Optional[float] = None
    reason: str = ""


def _buy_whole(held: _Held, day: date, price: float, fx: float, costs: CostTable) -> None:
    known = fund(held.ticker)
    k = math.floor(held.cash_usd / price + 1e-9)
    while k > 0 and k * price + costs.side_usd(known, k, price) > held.cash_usd + 1e-9:
        k -= 1
    if k < 1:
        return
    fee = costs.side_usd(known, k, price)
    held.book.buy(day, held.ticker, k, price, fx, fee)
    held.cash_usd -= k * price + fee
    held.shares += k
    if held.first_bought is None:
        held.first_bought = day


def _sell_for(held: _Held, day: date, dollars: float, price: float, fx: float, costs: CostTable) -> None:
    k = min(held.shares, math.ceil(dollars / price - 1e-9))
    if k >= 1:
        fee = costs.side_usd(fund(held.ticker), k, price)
        held.book.sell(day, held.ticker, k, price, fx, fee)
        held.cash_usd += k * price - fee
        held.shares -= k
    held.cash_usd -= dollars


def _pay_dividends(held: _Held, since: date, until: date, prices: PriceHistory, rate: Callable[[date], float],
                   costs: CostTable, rules: TaxRules) -> date:
    """VT's dividends on the shares held, between ``since`` (exclusive) and ``until`` (inclusive), reinvested."""
    if held.shares <= 0 or held.first_bought is None:
        return until
    for day, per_share in prices.dividends(held.ticker, since, until):
        if day <= since or day <= held.first_bought:
            continue
        gross = held.shares * per_share
        if gross <= 0:
            continue
        fx = rate(day)
        held.book.dividend(day, held.ticker, gross, fx)
        held.cash_usd += gross * (1.0 - rules.us_withholding)
        bar = prices.close_on_or_after(held.ticker, day)
        if bar is not None:
            _buy_whole(held, bar[0], bar[1], rate(bar[0]), costs)
    return until


def money_weighted_return(flows: Sequence[tuple[date, float]], end: date, final_value: float) -> Optional[float]:
    """The yearly rate at which the shekels in and out, and the value at the end, net to zero (XIRR)."""
    points = [(d, v) for d, v in flows if v] + [(end, final_value)]
    if len(points) < 2 or not any(v < 0 for _, v in points) or not any(v > 0 for _, v in points):
        return None
    start = min(d for d, _ in points)
    years = [((d - start).days / 365.25, v) for d, v in points]
    if max(t for t, _ in years) <= 0:
        return None

    def npv(rate: float) -> float:
        return math.fsum(v / (1.0 + rate) ** t for t, v in years)

    low, high = -0.99, 10.0
    f_low, f_high = npv(low), npv(high)
    if f_low * f_high > 0:
        return None
    for _ in range(200):
        middle = (low + high) / 2.0
        f_middle = npv(middle)
        if abs(f_middle) < 1e-9:
            return middle
        if f_low * f_middle < 0:
            high, f_high = middle, f_middle
        else:
            low, f_low = middle, f_middle
    return (low + high) / 2.0


def benchmark(flows: Iterable[Flow], prices: PriceHistory, rate: Callable[[date], float], day: date,
              closes_today: dict[str, float], fx_today: float, costs: CostTable = DEFAULT_COSTS,
              rules: TaxRules = DEFAULT_RULES, tickers: Sequence[str] = BOOKS) -> list[BenchmarkBook]:
    """Each buy-and-hold book from the owner's own flows, valued after tax on ``day``."""
    ordered = sorted(flows, key=lambda f: (f.day, f.kind))
    out: list[BenchmarkBook] = []
    for ticker in tickers:
        first = prices.first_day(ticker)
        if first is None:
            out.append(BenchmarkBook(ticker, False, reason="no price history"))
            continue
        if any(f.day < first for f in ordered):
            out.append(BenchmarkBook(ticker, False, reason=f"money went in before {first.isoformat()}, its first price"))
            continue
        held = _Held(ticker, TaxBook(rules))
        last = first
        for flow in ordered:
            if flow.day > day:
                break
            if ticker == VT:
                last = _pay_dividends(held, last, flow.day, prices, rate, costs, rules)
            bar = prices.close_on_or_after(ticker, flow.day)
            if bar is None:
                continue
            trade_day, price = bar
            fx = rate(trade_day)
            if flow.kind in ("deposit", "lot"):
                dollars = flow.amount_usd
                if not flow.in_usd:
                    dollars -= costs.conversion_usd(dollars)
                held.cash_usd += dollars
                held.cash_flows.append((flow.day, -flow.amount_ils))
                _buy_whole(held, trade_day, price, fx, costs)
            else:
                _sell_for(held, trade_day, flow.amount_usd, price, fx, costs)
                held.cash_flows.append((flow.day, flow.amount_ils))
        if ticker == VT:
            _pay_dividends(held, last, day, prices, rate, costs, rules)
        close = closes_today.get(ticker)
        if close is None or not close > 0:
            out.append(BenchmarkBook(ticker, False, reason="no close today"))
            continue
        market = (held.shares * close + held.cash_usd) * fx_today
        book = held.book
        finished = book.finished_years(day.year)
        carry = finished[-1].carry_out if finished else 0.0
        amounts = [r.amount for r in book.realised if r.day.year == day.year]
        divs = [(d.gross_ils, d.us_withheld_ils) for d in book.received if d.day.year == day.year]
        sold, _ = book.liquidation(day, {ticker: close}, fx_today)
        amounts += [g.amount for g in sold]
        this_year = year_tax(day.year, [a for a in amounts if a > 0], [a for a in amounts if a < 0], divs, carry, rules)
        after_tax = market - this_year.israeli_tax
        out.append(BenchmarkBook(ticker, True, market, this_year.israeli_tax, after_tax, held.shares, held.cash_usd,
                                 money_weighted_return(held.cash_flows, day, after_tax)))
    return out


__all__ = ["BOOKS", "BenchmarkBook", "PriceHistory", "VT", "VWRA", "benchmark", "money_weighted_return"]
