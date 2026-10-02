"""Israeli tax on a USD book: FIFO lots in shekels, a year's netting, and "if sold today".

The owner's rules of 2 Oct 2026, every number from ``config.israel_tax``
(read that file's docstring for the rules in words). What this module does
with them:

* ``lot_gain`` -- rule a, one lot (or part of one) closed: the shekel cost
  and proceeds, the nominal gain, the inflationary amount from the exchange
  rate, and what is taxable (a gain, never below 0) or allowable (a loss,
  never above 0). A loss made only by the exchange rate is not deductible.
* ``dividend_tax`` -- rule d: 25% of the gross shekel amount, a credit for
  the US tax withheld, the extra Israeli tax (usually 0), and any US tax the
  credit could not use (lost).
* ``year_tax`` -- rule e: a calendar year's gains against its losses, the
  carry-forward from earlier years against a net gain only, the switch
  ``offset_losses_vs_dividends`` setting a net loss against the year's
  dividends, and what carries forward. Never below 0.
* ``surtax`` -- rule b's surtax, off by default.
* ``TaxBook`` -- one account's lots, FIFO per ticker (rule c): buys, sales,
  dividends (a reinvested one is a new lot), and a short's dividend charge.
  ``TaxBook.state`` is the book's tax on a day: what is due on everything
  realised so far, and what would be due if every open lot were closed at
  that day's close ("if sold today").
* ``after_tax_series`` -- the walk the after-tax gate reads (pre-registration
  section 5c): for each day, the equity minus the tax due if everything were
  sold at that day's close, in dollars and in shekels.

Two conventions this module adds, both written into the pre-registration's
section 5c and put to the accountant (``docs/research/cpa-questions.md``):

* **A short** is a lot opened by a sale and closed by a purchase. Rule a is
  applied with the purchase as the cost (at the purchase day's rate) and the
  sale as the proceeds (at the sale day's rate). A dividend a short pays is
  an allowable loss on the day it is charged.
* **Tax for a finished year** is converted to dollars at that year's last
  rate in the walk; the current year's at the day's own rate.

Pure arithmetic: no prices, no files, no clock, no network.
"""

from __future__ import annotations

import math
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import date
from typing import Callable, Iterable, Mapping, Optional, Sequence

from config import israel_tax as cfg

#: What a book's event is, in ``TaxBook.apply`` and ``after_tax_series``.
BUY = "buy"
SELL = "sell"
DIVIDEND = "dividend"
#: A dividend a short position pays (the lender's): an allowable loss.
CHARGE = "charge"
EVENT_KINDS = (BUY, SELL, DIVIDEND, CHARGE)

#: Quantities this close to zero are zero (float shares from a broker).
_EPS = 1e-9


@dataclass(frozen=True)
class TaxRules:
    """The parameters of the rules; the defaults are ``config.israel_tax``'s."""

    capital_rate: float = cfg.CAPITAL_GAINS_RATE
    dividend_rate: float = cfg.DIVIDEND_RATE
    w8ben: bool = cfg.W8BEN_FILED
    offset_losses_vs_dividends: bool = cfg.OFFSET_LOSSES_VS_DIVIDENDS
    surtax_enabled: bool = cfg.SURTAX_ENABLED
    surtax_threshold: float = cfg.SURTAX_THRESHOLD_ILS
    surtax_rate: float = cfg.SURTAX_RATE
    surtax_capital_rate: float = cfg.SURTAX_CAPITAL_RATE
    #: An input, never a stored figure (``config.israel_tax.SALARY_ILS``).
    salary_ils: float = cfg.SALARY_ILS

    @property
    def us_withholding(self) -> float:
        """The share of a dividend the US withholds: the treaty rate with a W-8BEN on file."""
        return cfg.US_WITHHOLDING_W8BEN if self.w8ben else cfg.US_WITHHOLDING_NO_W8BEN


DEFAULT_RULES = TaxRules()


# --------------------------------------------------------------------------- #
# Rule a: one lot
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class LotGain:
    """One lot, or part of one, closed: rule a in shekels."""

    cost_ils: float
    proceeds_ils: float
    nominal: float
    inflation: float
    #: A taxable gain (>= 0) when the nominal result is a gain, an allowable
    #: loss (<= 0) when it is a loss.
    amount: float

    @property
    def taxable_gain(self) -> float:
        return max(self.amount, 0.0)

    @property
    def allowable_loss(self) -> float:
        return min(self.amount, 0.0)


def lot_gain(cost_usd: float, fx_buy: float, proceeds_usd: float, fx_sell: float) -> LotGain:
    """Rule a. ``fx_buy`` is the rate on the purchase's day, ``fx_sell`` on the sale's.

    nominal >= 0: taxable gain = max(0, nominal - max(inflation, 0)).
    nominal < 0: allowable loss = min(0, nominal - min(inflation, 0)).
    """
    if fx_buy <= 0 or fx_sell <= 0:
        raise ValueError("an exchange rate must be positive")
    cost_ils = cost_usd * fx_buy
    proceeds_ils = proceeds_usd * fx_sell
    nominal = proceeds_ils - cost_ils
    inflation = cost_ils * (fx_sell / fx_buy - 1.0)
    if nominal >= 0:
        amount = max(0.0, nominal - max(inflation, 0.0))
    else:
        amount = min(0.0, nominal - min(inflation, 0.0))
    return LotGain(cost_ils, proceeds_ils, nominal, inflation, amount)


# --------------------------------------------------------------------------- #
# Rule d: a dividend
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class DividendTax:
    gross_ils: float
    us_withheld_ils: float
    israeli_tax_ils: float
    credit_ils: float
    #: Israeli tax beyond the US credit: usually 0 with a W-8BEN.
    extra_ils: float
    #: US tax the Israeli credit could not use.
    lost_ils: float


def dividend_tax(gross_ils: float, rules: TaxRules = DEFAULT_RULES, offset_ils: float = 0.0,
                 us_withheld_ils: Optional[float] = None) -> DividendTax:
    """Rule d for a gross shekel amount. ``offset_ils`` is a capital loss set against it (rule e)."""
    us = gross_ils * rules.us_withholding if us_withheld_ils is None else us_withheld_ils
    israeli = rules.dividend_rate * max(0.0, gross_ils - offset_ils)
    credit = min(us, israeli)
    return DividendTax(gross_ils, us, israeli, credit, israeli - credit, us - credit)


# --------------------------------------------------------------------------- #
# Rule b's surtax, and rule e: a year
# --------------------------------------------------------------------------- #


def surtax(salary_ils: float, capital_income_ils: float, rules: TaxRules = DEFAULT_RULES) -> float:
    """3% of taxable income above the line, plus 2% of capital income above the same line.

    Computed whether or not ``rules.surtax_enabled``; ``year_tax`` asks for it
    only when it is.
    """
    line = rules.surtax_threshold
    return (rules.surtax_rate * max(0.0, salary_ils + capital_income_ils - line)
            + rules.surtax_capital_rate * max(0.0, capital_income_ils - line))


@dataclass(frozen=True)
class YearTax:
    """One calendar year's tax, in shekels."""

    year: int
    gains: float
    losses: float
    net_capital: float
    carry_in: float
    carry_used: float
    dividend_offset: float
    taxable_capital: float
    capital_tax: float
    dividends: float
    us_withheld: float
    israeli_dividend_tax: float
    credit: float
    extra_dividend_tax: float
    lost_credit: float
    surtax: float
    carry_out: float

    @property
    def israeli_tax(self) -> float:
        """What Israel collects for the year: capital gains, extra dividend tax, surtax."""
        return self.capital_tax + self.extra_dividend_tax + self.surtax

    @property
    def total_tax(self) -> float:
        """Every tax on the year's income, both countries: Israel's plus the US tax withheld."""
        return self.israeli_tax + self.us_withheld


def year_tax(year: int, gains: Iterable[float], losses: Iterable[float],
             dividends: Iterable[tuple[float, float]] = (), carry_in: float = 0.0,
             rules: TaxRules = DEFAULT_RULES) -> YearTax:
    """Rule e for one year.

    ``gains`` are taxable gains (each >= 0), ``losses`` allowable losses (each
    <= 0), ``dividends`` ``(gross_ils, us_withheld_ils)`` pairs, ``carry_in``
    the loss carried in from earlier years (<= 0). The year's losses go first
    against its gains. A net gain then uses the carry-forward. A net loss is
    set against the year's dividends when ``rules.offset_losses_vs_dividends``,
    and the rest is added to the carry-forward, which is used against future
    capital gains only, nominal, never expiring.
    """
    gains = [float(g) for g in gains]
    losses = [float(x) for x in losses]
    if any(g < 0 for g in gains) or any(x > 0 for x in losses) or carry_in > 0:
        raise ValueError("gains are >= 0, losses and the carry-forward are <= 0")
    pairs = [(float(g), float(w)) for g, w in dividends]
    total_gains, total_losses = math.fsum(gains), math.fsum(losses)
    net = total_gains + total_losses
    divs = math.fsum(g for g, _ in pairs)
    withheld = math.fsum(w for _, w in pairs)
    if net >= 0:
        carry_used = min(net, -carry_in)
        taxable = net - carry_used
        offset = 0.0
        carry_out = carry_in + carry_used
    else:
        carry_used, taxable = 0.0, 0.0
        left = -net
        offset = min(left, divs) if rules.offset_losses_vs_dividends else 0.0
        carry_out = carry_in - (left - offset)
    div = dividend_tax(divs, rules, offset_ils=offset, us_withheld_ils=withheld)
    extra = surtax(rules.salary_ils, taxable + max(0.0, divs - offset), rules) if rules.surtax_enabled else 0.0
    return YearTax(
        year=year, gains=total_gains, losses=total_losses, net_capital=net, carry_in=carry_in,
        carry_used=carry_used, dividend_offset=offset, taxable_capital=taxable,
        capital_tax=rules.capital_rate * taxable, dividends=divs, us_withheld=withheld,
        israeli_dividend_tax=div.israeli_tax_ils, credit=div.credit_ils, extra_dividend_tax=div.extra_ils,
        lost_credit=div.lost_ils, surtax=extra, carry_out=carry_out,
    )


# --------------------------------------------------------------------------- #
# Rule c: one account's lots
# --------------------------------------------------------------------------- #


@dataclass
class Lot:
    """Shares bought (or sold short) together, as many as are left."""

    ticker: str
    #: > 0 long, < 0 short.
    qty: float
    day: date
    #: A long: what the shares left cost, fees in. A short: what they were
    #: sold for, fees out. Always >= 0, in dollars.
    usd: float
    #: The rate on the day the lot was opened.
    fx: float


@dataclass(frozen=True)
class Realised:
    """A lot (or part of one) closed, or a short's dividend charge: one line of the year's capital account."""

    day: date
    ticker: str
    qty: float
    kind: str
    gain: Optional[LotGain]
    amount: float


@dataclass(frozen=True)
class Received:
    """A dividend credited: rule d's inputs."""

    day: date
    ticker: str
    gross_usd: float
    fx: float
    gross_ils: float
    us_withheld_ils: float


@dataclass(frozen=True)
class TaxState:
    """The book's tax on one day, in shekels unless named.

    ``realised`` is "tax paid so far": every finished year, plus this year's
    realised gains, losses and dividends as if the year ended today with
    nothing sold. ``if_sold`` adds every open lot closed at the day's close
    (``closes``) at the day's rate. Both include the US tax withheld on
    dividends (``YearTax.total_tax``).
    """

    day: date
    fx: float
    realised_ils: float
    if_sold_ils: float
    #: The same two in dollars: finished years at their own last rate, this year at ``fx``.
    realised_usd: float
    if_sold_usd: float
    #: The loss carried forward after the realised-only reckoning (<= 0).
    carry_forward_ils: float
    #: The year as reckoned "if sold today" (this year only).
    year: Optional[YearTax] = None
    #: Open lots no close was given for: valued at what they cost, so they add no gain.
    unpriced: tuple[str, ...] = ()


class TaxBook:
    """One account's lots, FIFO per ticker, and what it has realised and received."""

    def __init__(self, rules: TaxRules = DEFAULT_RULES) -> None:
        self.rules = rules
        self.lots: dict[str, deque[Lot]] = defaultdict(deque)
        self.realised: list[Realised] = []
        self.received: list[Received] = []
        #: The last rate seen in each calendar year: a finished year's tax is
        #: converted to dollars at it.
        self.year_end_fx: dict[int, float] = {}

    # -- events ------------------------------------------------------------ #

    def _seen(self, day: date, fx: float) -> None:
        if fx <= 0 or not math.isfinite(fx):
            raise ValueError(f"no usable exchange rate for {day}")
        self.year_end_fx[day.year] = fx

    def buy(self, day: date, ticker: str, qty: float, price_usd: float, fx: float, fee_usd: float = 0.0) -> None:
        """Bought ``qty`` shares: covers shorts first (FIFO), then opens a long lot."""
        self._seen(day, fx)
        self._trade(day, ticker, qty, price_usd, fx, fee_usd, buying=True)

    def sell(self, day: date, ticker: str, qty: float, price_usd: float, fx: float, fee_usd: float = 0.0) -> None:
        """Sold ``qty`` shares: closes longs first (FIFO), then opens a short lot."""
        self._seen(day, fx)
        self._trade(day, ticker, qty, price_usd, fx, fee_usd, buying=False)

    def _trade(self, day: date, ticker: str, qty: float, price: float, fx: float, fee: float,
               buying: bool) -> None:
        if qty <= 0 or price <= 0 or fee < 0:
            raise ValueError("a trade has a positive quantity and price and a fee >= 0")
        left = float(qty)
        lots = self.lots[ticker]
        while left > _EPS and lots and ((lots[0].qty < 0) if buying else (lots[0].qty > 0)):
            lot = lots[0]
            take = min(left, abs(lot.qty))
            share = take / abs(lot.qty)
            basis = lot.usd * share
            fee_part = fee * take / qty
            if buying:     # a short covered: the purchase is the cost, the short sale the proceeds
                gain = lot_gain(take * price + fee_part, fx, basis, lot.fx)
                kind = "cover"
            else:          # a long sold
                gain = lot_gain(basis, lot.fx, take * price - fee_part, fx)
                kind = "sale"
            self.realised.append(Realised(day, ticker, take, kind, gain, gain.amount))
            lot.usd -= basis
            lot.qty = lot.qty - take if lot.qty > 0 else lot.qty + take
            left -= take
            if abs(lot.qty) <= _EPS:
                lots.popleft()
        if left > _EPS:
            fee_part = fee * left / qty
            usd = left * price + fee_part if buying else left * price - fee_part
            lots.append(Lot(ticker, left if buying else -left, day, max(usd, 0.0), fx))

    def dividend(self, day: date, ticker: str, gross_usd: float, fx: float,
                 reinvest: Optional[tuple[float, float]] = None) -> None:
        """A dividend credited, gross. ``reinvest=(qty, price_usd)`` buys a new lot with it (rule c)."""
        self._seen(day, fx)
        if gross_usd < 0:
            raise ValueError("a dividend received is >= 0; a short's charge is ``charge``")
        gross_ils = gross_usd * fx
        self.received.append(Received(day, ticker, gross_usd, fx, gross_ils,
                                      gross_ils * self.rules.us_withholding))
        if reinvest is not None:
            qty, price = reinvest
            self.buy(day, ticker, qty, price, fx)

    def charge(self, day: date, ticker: str, amount_usd: float, fx: float) -> None:
        """A dividend a short position paid: an allowable loss on the day (the module's convention)."""
        self._seen(day, fx)
        if amount_usd < 0:
            raise ValueError("a charge is a positive amount paid")
        loss = -amount_usd * fx
        self.realised.append(Realised(day, ticker, 0.0, CHARGE, None, loss))

    def apply(self, day: date, kind: str, ticker: str, qty: float, price_usd: float, fx: float,
              fee_usd: float = 0.0) -> None:
        """One event by kind; for ``DIVIDEND`` and ``CHARGE`` the amount is ``qty * price_usd``."""
        if kind == BUY:
            self.buy(day, ticker, qty, price_usd, fx, fee_usd)
        elif kind == SELL:
            self.sell(day, ticker, qty, price_usd, fx, fee_usd)
        elif kind == DIVIDEND:
            self.dividend(day, ticker, qty * price_usd, fx)
        elif kind == CHARGE:
            self.charge(day, ticker, qty * price_usd, fx)
        else:
            raise ValueError(f"unknown event kind {kind!r}")

    # -- reading ----------------------------------------------------------- #

    def open_lots(self) -> list[Lot]:
        return [lot for lots in self.lots.values() for lot in lots]

    def open_quantity(self, ticker: str) -> float:
        return math.fsum(lot.qty for lot in self.lots.get(ticker, ()))

    def _year_parts(self, year: int) -> tuple[list[float], list[float], list[tuple[float, float]]]:
        amounts = [r.amount for r in self.realised if r.day.year == year]
        divs = [(d.gross_ils, d.us_withheld_ils) for d in self.received if d.day.year == year]
        return [a for a in amounts if a > 0], [a for a in amounts if a < 0], divs

    def _years(self, before: int) -> list[int]:
        seen = {r.day.year for r in self.realised} | {d.day.year for d in self.received}
        return sorted(y for y in seen if y < before)

    def finished_years(self, before: int) -> list[YearTax]:
        """Every year before ``before`` that has an event, netted in order, the carry-forward chained."""
        out: list[YearTax] = []
        carry = 0.0
        for year in self._years(before):
            gains, losses, divs = self._year_parts(year)
            result = year_tax(year, gains, losses, divs, carry, self.rules)
            out.append(result)
            carry = result.carry_out
        return out

    def liquidation(self, day: date, closes: Mapping[str, float], fx: float) -> tuple[list[LotGain], list[str]]:
        """Every open lot closed at ``closes`` at rate ``fx``: the gains, and the tickers with no close."""
        gains: list[LotGain] = []
        unpriced: list[str] = []
        for lot in self.open_lots():
            price = closes.get(lot.ticker)
            if price is None or not price > 0:
                unpriced.append(lot.ticker)
                continue
            if lot.qty > 0:
                gains.append(lot_gain(lot.usd, lot.fx, lot.qty * price, fx))
            else:
                gains.append(lot_gain(-lot.qty * price, fx, lot.usd, lot.fx))
        return gains, sorted(set(unpriced))

    def state(self, day: date, closes: Mapping[str, float], fx: float) -> TaxState:
        """The tax on ``day``: everything realised so far, and "if sold today" at ``closes``."""
        self._seen(day, fx)
        finished = self.finished_years(day.year)
        carry = finished[-1].carry_out if finished else 0.0
        done_ils = math.fsum(y.total_tax for y in finished)
        done_usd = math.fsum(y.total_tax / self.year_end_fx[y.year] for y in finished)
        gains, losses, divs = self._year_parts(day.year)
        now = year_tax(day.year, gains, losses, divs, carry, self.rules)
        sold, unpriced = self.liquidation(day, closes, fx)
        extra = [g.amount for g in sold]
        if_sold = year_tax(day.year, gains + [a for a in extra if a > 0], losses + [a for a in extra if a < 0],
                           divs, carry, self.rules)
        return TaxState(
            day=day, fx=fx,
            realised_ils=done_ils + now.total_tax, if_sold_ils=done_ils + if_sold.total_tax,
            realised_usd=done_usd + now.total_tax / fx, if_sold_usd=done_usd + if_sold.total_tax / fx,
            carry_forward_ils=now.carry_out, year=if_sold, unpriced=tuple(unpriced),
        )


# --------------------------------------------------------------------------- #
# The walk the gate reads
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Event:
    """One thing a book did on a day, in the order it happened."""

    kind: str
    ticker: str
    qty: float
    price_usd: float
    fee_usd: float = 0.0


@dataclass(frozen=True)
class AfterTaxDay:
    day: date
    fx: float
    equity_usd: float
    equity_ils: float
    #: Equity minus the tax due if every position were sold at the day's close.
    after_tax_usd: float
    after_tax_ils: float
    #: "Tax paid so far" and "if sold today", in shekels.
    realised_tax_ils: float
    if_sold_tax_ils: float
    unpriced: tuple[str, ...] = ()


@dataclass
class AfterTaxSeries:
    days: list[AfterTaxDay] = field(default_factory=list)
    start_equity_usd: float = 0.0
    start_fx: Optional[float] = None

    def returns(self, after_tax: bool = True, ils: bool = False) -> dict[date, float]:
        """Daily returns by day: today over yesterday, minus one; the first day from the start.

        On the values rounded to the cent (agorot), as ``shadow.run.daily_returns``
        does, so two books that agree to the cent differ by exactly nothing.
        """
        key = ("after_tax_" if after_tax else "equity_") + ("ils" if ils else "usd")
        first = self.start_equity_usd * (self.start_fx if ils and self.start_fx else 1.0)
        values = [round(first, 2)] + [round(getattr(d, key), 2) for d in self.days]
        return {d.day: (today / before - 1.0) if before else 0.0
                for d, before, today in zip(self.days, values, values[1:])}


def after_tax_series(
    days: Sequence[date], equity_usd: Sequence[float], events: Mapping[date, Sequence[Event]],
    closes: Callable[[date], Mapping[str, float]], fx: Mapping[date, float], *,
    start_equity_usd: float, start_fx: Optional[float] = None, rules: TaxRules = DEFAULT_RULES,
) -> AfterTaxSeries:
    """For each day: the book's events, then its tax "if sold today" at that day's closes.

    ``equity_usd`` is the book's own equity at each day's close, pre-tax --
    as the funds and the paper account report it, dividends credited gross.
    After-tax equity = equity - the tax due if every position were sold at
    the day's close (floored at 0: a year never has negative tax).
    """
    if len(days) != len(equity_usd):
        raise ValueError("one equity per day")
    book = TaxBook(rules)
    out = AfterTaxSeries(start_equity_usd=start_equity_usd,
                         start_fx=start_fx if start_fx is not None else (fx.get(days[0]) if days else None))
    for day, equity in zip(days, equity_usd):
        rate = fx.get(day)
        if rate is None:
            raise ValueError(f"no exchange rate for {day}")
        for event in events.get(day, ()):
            book.apply(day, event.kind, event.ticker, event.qty, event.price_usd, rate, event.fee_usd)
        state = book.state(day, closes(day), rate)
        out.days.append(AfterTaxDay(
            day=day, fx=rate, equity_usd=equity, equity_ils=equity * rate,
            after_tax_usd=equity - state.if_sold_usd, after_tax_ils=equity * rate - state.if_sold_ils,
            realised_tax_ils=state.realised_ils, if_sold_tax_ils=state.if_sold_ils, unpriced=state.unpriced,
        ))
    return out


__all__ = [
    "AfterTaxDay", "AfterTaxSeries", "BUY", "CHARGE", "DEFAULT_RULES", "DIVIDEND", "DividendTax", "EVENT_KINDS",
    "Event", "Lot", "LotGain", "Realised", "Received", "SELL", "TaxBook", "TaxRules", "TaxState", "YearTax",
    "after_tax_series", "dividend_tax", "lot_gain", "surtax", "year_tax",
]
