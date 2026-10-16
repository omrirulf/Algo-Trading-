"""The person: FIFO lots per account, one year netted across accounts, and what the money is worth after tax.

Section 4 of the plan. ``analysis.israel_tax`` does the arithmetic of one
account (``TaxBook``) and of one year (``year_tax``); this module puts the
owner's accounts together into one person, as Israel taxes them:

* every taxable account's gains, losses and dividends of a year go into one
  ``year_tax``, the loss carried forward chained year to year from the
  owner's last assessment (``plan.csv``'s ``carry_in``); FIFO stays per
  account (rule c, accountant question 3);
* a transfer between two of the owner's accounts moves the oldest lots
  first, each keeping its day, price and rate: no sale, no deposit;
* a dividend arrives net of the US tax actually withheld (``withheld_usd``),
  so "value if sold today" takes off Israel's tax only (T36);
* the tax cost of a possible sale (D6) is reckoned on copies of the books,
  for the whole person: this year's extra Israeli tax, plus 25% of the loss
  the sale uses up (a loss carried forward is worth 25% of itself later);
* "value if sold today" and "tax paid so far" (section 7.1), and the
  half-year figures (7.2).

Dates with no Bank of Israel rate: a weekday follows ``analysis.boi_rates``
(the ECB's rate, then the last earlier rate, each counted); a weekend day,
on which only a deposit or a withdrawal can fall, takes the last weekday's
rate -- a new rule, counted and listed, for accountant question 4.

Pure arithmetic over the owner's rows: no prices fetched, no file written.
"""

from __future__ import annotations

import copy
import math
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Callable, Iterable, Mapping, Optional

from analysis.israel_tax import DEFAULT_RULES, Lot, Realised, TaxBook, TaxRules, YearTax, lot_gain, year_tax
from investor.files import Account, DataError, Payment, Plan, TrackValue, Transaction
from investor.funds import CostTable, DEFAULT_COSTS, fund

_EPS = 1e-9

WEEKEND = "weekend"
OVERRIDE = "override"


@dataclass
class Cash:
    usd: float = 0.0
    ils: float = 0.0

    def ils_value(self, fx: float) -> float:
        return self.usd * fx + self.ils


@dataclass(frozen=True)
class Flow:
    """Money that went into or out of the owner's taxable accounts, for the benchmark (section 7.4)."""

    day: date
    account: str
    #: ``deposit``, ``withdrawal`` or ``lot`` (a lot held before the records, or transferred in: its cost).
    kind: str
    amount_ils: float
    amount_usd: float
    fx: float
    #: A deposit made in dollars needs no conversion; one made in shekels does.
    in_usd: bool


@dataclass(frozen=True)
class DividendRecord:
    day: date
    account: str
    ticker: str
    gross_usd: float
    withheld_usd: float
    fx: float

    @property
    def gross_ils(self) -> float:
        return self.gross_usd * self.fx

    @property
    def withheld_ils(self) -> float:
        return self.withheld_usd * self.fx

    @property
    def net_usd(self) -> float:
        return self.gross_usd - self.withheld_usd


@dataclass(frozen=True)
class Position:
    account: str
    ticker: str
    qty: float
    lots: tuple[Lot, ...]


@dataclass(frozen=True)
class SaleCost:
    """What selling ``qty`` of a fund, FIFO, would cost the person this year (D6)."""

    proceeds_ils: float
    #: This year's extra Israeli tax because of the sale.
    tax_delta: float
    #: The loss the sale uses up: what would have carried forward without it, less what carries with it.
    loss_used: float
    #: The taxable amount of the sale itself (a gain > 0, a loss < 0), FIFO.
    amount: float
    #: The lots the sale closes, FIFO: (the lot's day, the shares taken, the amount).
    lots: tuple[tuple[date, float, float], ...]
    #: With specific lots: (the lot's number by purchase order, its amount), when lower than FIFO's.
    best_specific: Optional[tuple[int, float]] = None

    @property
    def cost(self) -> float:
        """D6: this year's extra tax plus 25% of the loss used up. Negative is a saving."""
        from config.israel_tax import CAPITAL_GAINS_RATE

        return self.tax_delta + CAPITAL_GAINS_RATE * self.loss_used

    @property
    def share(self) -> Optional[float]:
        """The cost against the gross proceeds (the 0.5% test), or None with no proceeds."""
        return self.cost / self.proceeds_ils if self.proceeds_ils else None


@dataclass(frozen=True)
class IfSold:
    """Section 7.1 on one day, in shekels unless named."""

    day: date
    fx: float
    market_ils: float
    #: This year's Israeli tax if every taxable lot were sold today, for the whole person.
    tax_if_sold_ils: float
    advances_paid_ils: float
    unpaid_finished_ils: float
    value_ils: float
    tax_paid_so_far_ils: float
    #: Israel's tax for the finished years, and this year's on what was sold and received so far.
    finished_tax_ils: float
    this_year_tax_ils: float
    us_withheld_ils: float
    selling_cost_ils: float
    #: The tax-free accounts' tracks, at their value (no withdrawal tax taken off, D9).
    tax_free_ils: float = 0.0
    unpriced: tuple[str, ...] = ()
    #: The year as reckoned "if sold today".
    year: Optional[YearTax] = None

    @property
    def value_usd(self) -> float:
        return self.value_ils / self.fx

    @property
    def market_usd(self) -> float:
        return self.market_ils / self.fx

    @property
    def taxable_value_ils(self) -> float:
        """The taxable accounts alone, after tax if sold today: what the benchmark books are compared with."""
        return self.value_ils - self.tax_free_ils


@dataclass(frozen=True)
class HalfYear:
    year: int
    half: int
    proceeds_ils: float
    gains_ils: float
    losses_ils: float
    #: Three readings of the advance (section 7.2; accountant questions 7 and 15).
    on_gains: float
    on_net: float
    on_year: float
    #: What the owner recorded as paid for this half, if anything.
    paid_ils: Optional[float]

    @property
    def net_ils(self) -> float:
        return self.gains_ils + self.losses_ils


def _weekday_before(day: date) -> date:
    while day.weekday() >= 5:
        day -= timedelta(days=1)
    return day


class Person:
    """The owner's accounts as one taxpayer."""

    def __init__(self, accounts: Mapping[str, Account], plan: Plan, rate: Callable[[date], float],
                 rules: Optional[TaxRules] = None) -> None:
        self.accounts = dict(accounts)
        self.plan = plan
        self._rate = rate
        base = rules or DEFAULT_RULES
        self.rules = TaxRules(
            capital_rate=base.capital_rate, dividend_rate=base.dividend_rate, w8ben=plan.w8ben.value,
            offset_losses_vs_dividends=base.offset_losses_vs_dividends, surtax_enabled=plan.surtax,
            surtax_threshold=base.surtax_threshold, surtax_rate=base.surtax_rate,
            surtax_capital_rate=base.surtax_capital_rate, salary_ils=plan.other_income_ils if plan.surtax else 0.0,
        )
        self.books: dict[str, TaxBook] = {name: TaxBook(self.rules) for name, a in self.accounts.items() if a.taxable}
        self.cash: dict[str, Cash] = {name: Cash() for name in self.accounts}
        self.tracks: dict[str, dict[str, float]] = {name: {} for name, a in self.accounts.items() if not a.taxable}
        self.flows: list[Flow] = []
        self.dividends: list[DividendRecord] = []
        #: (day, kind): a weekend day priced at the last weekday's rate, or a row's own rate used instead.
        self.rate_notes: list[tuple[date, str]] = []
        self._fees_usd: dict[str, float] = defaultdict(float)

    # -- rates --------------------------------------------------------------- #

    def fx(self, day: date, override: Optional[float] = None) -> float:
        if override is not None:
            self.rate_notes.append((day, OVERRIDE))
            return float(override)
        weekday = _weekday_before(day)
        if weekday != day:
            self.rate_notes.append((day, WEEKEND))
        try:
            return float(self._rate(weekday))
        except (KeyError, ValueError):
            raise DataError("rates", None, "no exchange rate for a day the records need") from None

    # -- the rows ----------------------------------------------------------- #

    def apply(self, transactions: Iterable[Transaction]) -> None:
        for row in transactions:
            self._apply(row)

    def _book(self, row: Transaction, account: Optional[str] = None) -> TaxBook:
        name = account or row.account
        if name not in self.books:
            raise DataError("transactions.csv", row.row, "a trade or a dividend belongs to a taxable account")
        return self.books[name]

    def _apply(self, row: Transaction) -> None:
        fx = self.fx(row.day, row.fx)
        kind = row.kind
        if kind == "buy":
            self._check_usd_fund(row)
            book = self._book(row)
            book.buy(row.day, row.ticker, row.quantity, row.price_usd, fx, row.fee_usd)
            self.cash[row.account].usd -= row.quantity * row.price_usd + row.fee_usd
        elif kind == "sell":
            self._check_usd_fund(row)
            book = self._book(row)
            if book.open_quantity(row.ticker) + _EPS < row.quantity:
                raise DataError("transactions.csv", row.row, "a sale larger than the account holds")
            book.sell(row.day, row.ticker, row.quantity, row.price_usd, fx, row.fee_usd)
            self.cash[row.account].usd += row.quantity * row.price_usd - row.fee_usd
        elif kind == "dividend":
            self._check_usd_fund(row)
            book = self._book(row)
            withheld = row.withheld_usd
            if withheld is None:
                known = fund(row.ticker)
                if known is None or known.domicile != "US":
                    raise DataError("transactions.csv", row.row,
                                    "the US tax withheld must be filled in for a fund that is not US-listed")
                withheld = row.amount * self.rules.us_withholding
            book.dividend(row.day, row.ticker, row.amount, fx, withheld_usd=withheld)
            self.cash[row.account].usd += row.amount - withheld
            self.dividends.append(DividendRecord(row.day, row.account, row.ticker, row.amount, withheld, fx))
        elif kind == "deposit":
            self._cash_in(row, fx, +1)
        elif kind == "withdrawal":
            self._cash_in(row, fx, -1)
        elif kind == "fee":
            if row.currency == "USD":
                self.cash[row.account].usd -= row.amount
            else:
                self.cash[row.account].ils -= row.amount
            self._fees_usd[row.account] += row.amount if row.currency == "USD" else row.amount / fx
        elif kind == "transfer":
            if row.ticker:
                self._move_lots(row)
            elif row.currency == "USD":
                self.cash[row.account].usd -= row.amount
                self.cash[row.to_account].usd += row.amount
            else:
                self.cash[row.account].ils -= row.amount
                self.cash[row.to_account].ils += row.amount
        elif kind == "transfer_in":
            self._check_usd_fund(row)
            book = self._book(row)
            bought = row.bought_on or row.day
            fx_then = self.fx(bought)
            book.buy(bought, row.ticker, row.quantity, row.price_usd, fx_then, row.fee_usd)
            self._sort_lots(book, row.ticker)
            cost = row.quantity * row.price_usd + row.fee_usd
            self.flows.append(Flow(bought, row.account, "lot", cost * fx_then, cost, fx_then, True))
        else:  # pragma: no cover - read_transactions refuses anything else
            raise DataError("transactions.csv", row.row, "an unknown kind of event")

    def _check_usd_fund(self, row: Transaction) -> None:
        known = fund(row.ticker)
        if known is not None and known.currency != "USD":
            raise DataError("transactions.csv", row.row, "a fund not quoted in dollars is refused")

    def _cash_in(self, row: Transaction, fx: float, sign: int) -> None:
        cash = self.cash[row.account]
        in_usd = row.currency == "USD"
        if in_usd:
            cash.usd += sign * row.amount
            ils, usd = row.amount * fx, row.amount
        else:
            cash.ils += sign * row.amount
            ils, usd = row.amount, row.amount / fx
        if self.accounts[row.account].taxable:
            self.flows.append(Flow(row.day, row.account, "deposit" if sign > 0 else "withdrawal", ils, usd, fx, in_usd))

    def _move_lots(self, row: Transaction) -> None:
        src, dst = self._book(row), self._book(row, row.to_account)
        left = float(row.quantity)
        lots = src.lots[row.ticker]
        while left > _EPS and lots and lots[0].qty > 0:
            lot = lots[0]
            take = min(left, lot.qty)
            share = take / lot.qty
            dst.lots[row.ticker].append(Lot(row.ticker, take, lot.day, lot.usd * share, lot.fx))
            lot.usd -= lot.usd * share
            lot.qty -= take
            left -= take
            if lot.qty <= _EPS:
                lots.popleft()
        if left > _EPS:
            raise DataError("transactions.csv", row.row, "a transfer larger than the account holds")
        self._sort_lots(dst, row.ticker)

    @staticmethod
    def _sort_lots(book: TaxBook, ticker: str) -> None:
        """FIFO is by purchase day: a lot brought in from outside takes its own place in the queue."""
        book.lots[ticker] = deque(sorted(book.lots[ticker], key=lambda lot: lot.day))

    def set_tracks(self, values: Iterable[TrackValue], as_of: date) -> None:
        """The latest value of each tax-free track on or before ``as_of``."""
        latest: dict[tuple[str, str], TrackValue] = {}
        for value in values:
            if value.day <= as_of:
                key = (value.account, value.track)
                if key not in latest or value.day >= latest[key].day:
                    latest[key] = value
        for (account, track), value in latest.items():
            self.tracks.setdefault(account, {})[track] = value.value_ils

    # -- reading ------------------------------------------------------------ #

    def positions(self) -> list[Position]:
        out: list[Position] = []
        for account in sorted(self.books):
            book = self.books[account]
            for ticker in sorted(book.lots):
                lots = tuple(lot for lot in book.lots[ticker] if lot.qty > _EPS)
                if lots:
                    out.append(Position(account, ticker, math.fsum(l.qty for l in lots), lots))
        return out

    def years(self) -> list[int]:
        seen = {r.day.year for b in self.books.values() for r in b.realised}
        seen |= {d.day.year for b in self.books.values() for d in b.received}
        return sorted(seen)

    @staticmethod
    def _parts(books: Mapping[str, TaxBook], year: int) -> tuple[list[float], list[float], list[tuple[float, float]]]:
        amounts = [r.amount for b in books.values() for r in b.realised if r.day.year == year]
        divs = [(d.gross_ils, d.us_withheld_ils) for b in books.values() for d in b.received if d.day.year == year]
        return [a for a in amounts if a > 0], [a for a in amounts if a < 0], divs

    def _rules_for(self, year: int) -> TaxRules:
        if self.rules.surtax_enabled and self.plan.other_income_year not in (None, year):
            return TaxRules(**{**self.rules.__dict__, "surtax_enabled": False, "salary_ils": 0.0})
        return self.rules

    def _chain(self, books: Mapping[str, TaxBook], up_to: int) -> tuple[list[YearTax], float]:
        """The finished years before ``up_to``, from the assessment the carry-in came from; and the carry into it."""
        carry = self.plan.carry_in
        years = [y for y in self.years() if y < up_to]
        if self.plan.carry_in_year is not None:
            first = self.plan.carry_in_year + 1
            years = [y for y in years if y >= first]
            if years or first < up_to:
                years = list(range(first, up_to))
        out: list[YearTax] = []
        for year in years:
            gains, losses, divs = self._parts(books, year)
            result = year_tax(year, gains, losses, divs, carry, self._rules_for(year))
            out.append(result)
            carry = result.carry_out
        return out, carry

    def finished_years(self, before: int) -> list[YearTax]:
        return self._chain(self.books, before)[0]

    def _year_with(self, books: Mapping[str, TaxBook], year: int, extra: Iterable[float] = ()) -> YearTax:
        _, carry = self._chain(books, year)
        gains, losses, divs = self._parts(books, year)
        extra = [float(a) for a in extra]
        return year_tax(year, gains + [a for a in extra if a > 0], losses + [a for a in extra if a < 0], divs, carry,
                        self._rules_for(year))

    def year_tax(self, year: int, extra: Iterable[float] = ()) -> YearTax:
        """The person's year, chained from the carry-in; ``extra`` are amounts of sales not yet made."""
        return self._year_with(self.books, year, extra)

    # -- a possible sale ---------------------------------------------------- #

    def sale_cost(self, account: str, ticker: str, qty: float, price_usd: float, fx: float, day: date,
                  fee_usd: float = 0.0) -> SaleCost:
        """D6, on copies: the person's year with and without selling ``qty`` FIFO at ``price_usd``."""
        year = day.year
        before = self.year_tax(year)
        books = copy.deepcopy(self.books)
        book = books[account]
        if book.open_quantity(ticker) + _EPS < qty:
            raise ValueError("a sale larger than the account holds")
        start = len(book.realised)
        book.sell(day, ticker, qty, price_usd, fx, fee_usd)
        closed = book.realised[start:]
        after = self._year_with(books, year)
        proceeds = math.fsum(r.gain.proceeds_ils for r in closed if r.gain is not None)
        amount = math.fsum(r.amount for r in closed)
        lots = tuple((r.opened or r.day, r.qty, r.amount) for r in closed)
        best = self._best_specific(account, ticker, qty, price_usd, fx, fee_usd, amount)
        return SaleCost(proceeds, after.israeli_tax - before.israeli_tax, after.carry_out - before.carry_out, amount,
                        lots, best)

    def _best_specific(self, account: str, ticker: str, qty: float, price_usd: float, fx: float, fee_usd: float,
                       fifo_amount: float) -> Optional[tuple[int, float]]:
        """The single open lot whose sale of ``qty`` would be taxed least, when that is less than FIFO's."""
        best: Optional[tuple[int, float]] = None
        for number, lot in enumerate(self.books[account].lots.get(ticker, ()), start=1):
            if lot.qty + _EPS < qty or lot.qty <= 0:
                continue
            share = qty / lot.qty
            amount = lot_gain(lot.usd * share, lot.fx, qty * price_usd - fee_usd, fx).amount
            if best is None or amount < best[1]:
                best = (number, amount)
        if best is not None and best[1] < fifo_amount - 1e-6:
            return best
        return None

    # -- what the money is worth (7.1) -------------------------------------- #

    def market_value(self, closes: Mapping[str, float], fx: float) -> tuple[float, list[str]]:
        """Every account in shekels: positions at the close, cash, and the tax-free tracks; and the unpriced funds."""
        total = 0.0
        unpriced: list[str] = []
        for position in self.positions():
            price = closes.get(position.ticker)
            if price is None or not price > 0:
                unpriced.append(position.ticker)
                total += math.fsum(l.usd for l in position.lots) * fx
            else:
                total += position.qty * price * fx
        for cash in self.cash.values():
            total += cash.ils_value(fx)
        for tracks in self.tracks.values():
            total += math.fsum(tracks.values())
        return total, sorted(set(unpriced))

    def if_sold(self, day: date, closes: Mapping[str, float], fx: float, payments: Iterable[Payment] = (),
                costs: CostTable = DEFAULT_COSTS) -> IfSold:
        year = day.year
        payments = list(payments)
        market, unpriced = self.market_value(closes, fx)
        extra: list[float] = []
        for book in self.books.values():
            gains, _ = book.liquidation(day, closes, fx)
            extra += [g.amount for g in gains]
        sold = self._year_with(self.books, year, extra)
        finished, _ = self._chain(self.books, year)
        finished_tax = math.fsum(y.israeli_tax for y in finished)
        this_year = self.year_tax(year)
        advances = math.fsum(p.amount_ils for p in payments if p.year == year and p.half in ("1", "2"))
        unpaid_finished = 0.0
        if payments:
            paid_finished = math.fsum(p.amount_ils for p in payments if p.year < year)
            unpaid_finished = max(0.0, finished_tax - paid_finished)
        withheld = math.fsum(d.withheld_ils for d in self.dividends)
        selling = 0.0
        for position in self.positions():
            price = closes.get(position.ticker)
            if price and price > 0:
                selling += costs.side_usd(fund(position.ticker), position.qty, price) * fx
        value = market - (sold.israeli_tax - advances) - unpaid_finished
        tax_free = math.fsum(math.fsum(tracks.values()) for tracks in self.tracks.values())
        tax_free += math.fsum(c.ils_value(fx) for name, c in self.cash.items() if not self.accounts[name].taxable)
        return IfSold(day, fx, market, sold.israeli_tax, advances, unpaid_finished, value,
                      finished_tax + this_year.israeli_tax + withheld, finished_tax, this_year.israeli_tax, withheld,
                      selling, tax_free, tuple(unpriced), sold)

    # -- half-years (7.2) ----------------------------------------------------- #

    def half_years(self, year: int, payments: Iterable[Payment] = ()) -> list[HalfYear]:
        from config.israel_tax import CAPITAL_GAINS_RATE as rate

        payments = list(payments)
        realised = [r for b in self.books.values() for r in b.realised if r.day.year == year]
        halves: list[HalfYear] = []
        year_net = 0.0
        paid_first: Optional[float] = None
        for half in (1, 2):
            rows = [r for r in realised if (r.day.month <= 6) == (half == 1)]
            proceeds = math.fsum(r.gain.proceeds_ils for r in rows if r.gain is not None and r.kind == "sale")
            gains = math.fsum(r.amount for r in rows if r.amount > 0)
            losses = math.fsum(r.amount for r in rows if r.amount < 0)
            year_net += gains + losses
            recorded = [p.amount_ils for p in payments if p.year == year and p.half == str(half)]
            paid = math.fsum(recorded) if recorded else None
            on_gains = rate * gains
            on_net = rate * max(0.0, gains + losses)
            if half == 1:
                on_year = on_net
                paid_first = paid if paid is not None else on_net
            else:
                on_year = rate * max(0.0, year_net) - (paid_first or 0.0)
            halves.append(HalfYear(year, half, proceeds, gains, losses, on_gains, on_net, on_year, paid))
        return halves

    def realised_rows(self, year: int) -> list[tuple[str, Realised]]:
        """Every closed lot of the year, with its account, in date order (section 7.3)."""
        rows = [(name, r) for name, b in self.books.items() for r in b.realised if r.day.year == year]
        return sorted(rows, key=lambda pair: (pair[1].day, pair[0]))


__all__ = ["Cash", "DividendRecord", "Flow", "HalfYear", "IfSold", "OVERRIDE", "Person", "Position", "SaleCost",
           "WEEKEND"]
