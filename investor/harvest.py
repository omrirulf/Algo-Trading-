"""Harvest suggestions (section 6): taxable lots whose loss is worth taking, each with a similar but not identical fund.

The owner's rule (6.1), read as A and B and C:

* **A**, the loss test: the FIFO group's allowable shekel loss (rule a, at
  the last close and that day's rate) is at least the larger of 2,000 ILS
  and 5% of the value of everything sold. A later lot cannot be sold before
  the earlier lots of the same fund in the same account (D10), so every
  prefix of the lots is a group, and the one with the largest net loss that
  passes is shown.
* **B**, the cost test: 25% of the loss is at least 5 times the trading
  cost of both sides (6.4): selling the group, and buying the candidate in
  whole shares with the dollars left after the selling cost.
* **C**: a net gain this year (D11: this year's taxable gain after the loss
  carried in, before this harvest, above 0), or the owner expects gains
  within 3 years (a dated answer in ``plan.csv``), or the swap is a domicile
  switch (D12: a US-listed fund sold for an Irish one).

Several harvests (D14) are taken one after another, the largest first, and
C is checked again after each. Every suggestion starts with its tax cost
this year (usually a saving) and shows what the loss is really worth (D13):
this year, against dividends (worth 0 when the US credit already covers
Israel's 25%, and that credit is then lost), and carried forward. Nothing
is sold: every line says "Suggestion only".

A loss made only by the exchange rate gives 0 (T5): while the accountant has
not confirmed T5 (question 1), such a group's line says what would happen if
T5 is rejected (T26).
"""

from __future__ import annotations

import copy
import math
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Iterable, Mapping, Optional

from analysis.israel_tax import LotGain, lot_gain
from config.israel_tax import CAPITAL_GAINS_RATE
from investor.files import Dated, Transaction
from investor.funds import CostTable, DEFAULT_COSTS, SUBSTITUTES, Fund, domicile_switch, fund, identical
from investor.ledger import Person

#: 6.1: at least 2,000 ILS and 5% of the lot value...
LOSS_FLOOR_ILS = 2_000.0
LOSS_SHARE = 0.05
#: ...and a tax value of at least 5 times the trading cost.
COST_MULTIPLE = 5.0
#: Israel has no 30-day rule like the US; the purchase check is a reminder only.
PURCHASE_WINDOW_DAYS = 30


@dataclass
class Candidate:
    ticker: str
    shares: int
    trading_cost_ils: float
    passes_b: bool
    passes_c: bool
    switch: bool
    why_c: str = ""

    @property
    def passes(self) -> bool:
        return self.passes_b and self.passes_c

    @property
    def failed(self) -> str:
        if not self.passes_b and not self.passes_c:
            return "B and C"
        return "B" if not self.passes_b else "C" if not self.passes_c else ""


@dataclass
class Group:
    """One FIFO group of a fund in an account, tested."""

    account: str
    ticker: str
    lots: int
    shares: float
    value_ils: float
    #: The group's net allowable amount (< 0 is a loss) and its nominal shekel result.
    net_ils: float
    nominal_ils: float
    passes_a: bool
    candidates: list[Candidate] = field(default_factory=list)
    #: The T5 reading: what the tests say with the whole shekel loss allowed.
    if_t5_rejected: Optional[str] = None

    @property
    def loss_ils(self) -> float:
        return max(0.0, -self.net_ils)

    @property
    def tax_value_ils(self) -> float:
        return CAPITAL_GAINS_RATE * self.loss_ils

    @property
    def flagged(self) -> bool:
        return self.passes_a and any(c.passes for c in self.candidates)

    @property
    def suggested(self) -> Optional[Candidate]:
        return next((c for c in self.candidates if c.passes), None) if self.passes_a else None

    @property
    def floor_ils(self) -> float:
        return max(LOSS_FLOOR_ILS, LOSS_SHARE * self.value_ils)


@dataclass
class Harvest:
    """One suggestion, with what the loss is worth (D13) and its warnings."""

    group: Group
    fund: str
    tax_delta_ils: float
    worth_now_ils: float
    against_gains_ils: float
    against_dividends_ils: float
    credit_lost_ils: float
    carried_forward_ils: float
    net_gain_this_year_ils: float
    gains_less_losses_ils: float
    warnings: list[str] = field(default_factory=list)


@dataclass
class HarvestResult:
    suggestions: list[Harvest]
    #: Groups looked at and not flagged (the largest loss per account and fund), with why.
    not_flagged: list[Group]
    unpriced: list[str]
    #: Funds sold in the suggestions (never bought this run) and the funds suggested for each class.
    sold: frozenset[str]
    bought: dict[str, str]


def _trading_cost_ils(sold: Optional[Fund], shares: float, price: float, candidate: Fund, candidate_price: float,
                      fx: float, costs: CostTable) -> tuple[float, int]:
    sell_side = costs.side_usd(sold, shares, price)
    dollars = shares * price - sell_side
    bought = max(0, math.floor(dollars / candidate_price + 1e-9))
    buy_side = costs.side_usd(candidate, bought, candidate_price)
    return (sell_side + buy_side) * fx, bought


def _test_group(person: Person, account: str, ticker: str, lots, closes: Mapping[str, float], fx: float,
                day: date, costs: CostTable, cost_override: Optional[float], expects: bool,
                net_gain: float, classes: Mapping[str, str]) -> Optional[Group]:
    price = closes.get(ticker)
    if price is None or not price > 0:
        return None
    gains: list[LotGain] = [lot_gain(lot.usd, lot.fx, lot.qty * price, fx) for lot in lots]
    shares = math.fsum(lot.qty for lot in lots)
    value = shares * price * fx
    net = math.fsum(g.amount for g in gains)
    nominal = math.fsum(g.nominal for g in gains)
    group = Group(account, ticker, len(lots), shares, value, net, nominal, False)
    sold = fund(ticker)

    def candidates(loss: float) -> list[Candidate]:
        out: list[Candidate] = []
        for other in SUBSTITUTES.get(ticker, ()):
            candidate = fund(other)
            if candidate is None or (sold is not None and identical(sold, candidate)):
                continue
            other_price = closes.get(other)
            if other_price is None or not other_price > 0:
                continue
            cost, bought = _trading_cost_ils(sold, shares, price, candidate, float(other_price), fx, costs)
            if cost_override is not None:
                cost = cost_override
            switch = sold is not None and domicile_switch(sold, candidate)
            passes_c = net_gain > 0 or expects or switch
            why = ("a net gain this year" if net_gain > 0 else "gains expected within 3 years" if expects
                   else "a domicile switch" if switch else "no gain this year, none expected, not a domicile switch")
            out.append(Candidate(other, bought, cost, CAPITAL_GAINS_RATE * loss >= COST_MULTIPLE * cost - 1e-9,
                                 passes_c, switch, why))
        return out

    if net < 0:
        group.passes_a = -net >= group.floor_ils - 1e-9
        group.candidates = candidates(-net)
    elif nominal < 0:
        # T5: a loss made only by the exchange rate. What the tests would say with the whole shekel loss.
        loss = -nominal
        trial = Group(account, ticker, len(lots), shares, value, -loss, nominal, loss >= group.floor_ils - 1e-9,
                      candidates(loss))
        if trial.flagged:
            best = trial.suggested
            group.if_t5_rejected = (f"it would be flagged (tax value {trial.tax_value_ils:,.2f} against "
                                    f"{COST_MULTIPLE:.0f} x {best.trading_cost_ils:,.2f}) if the accountant rejects T5")
        else:
            group.if_t5_rejected = "it would still not be flagged if the accountant rejects T5"
    return group


def _best_groups(person: Person, closes: Mapping[str, float], fx: float, day: date, costs: CostTable,
                 cost_override: Optional[float], expects: bool, classes: Mapping[str, str]) -> tuple[list[Group], list[str]]:
    """Per account and fund: the flagged group with the largest loss, else the group with the largest loss."""
    net_gain = person.year_tax(day.year).taxable_capital
    out: list[Group] = []
    unpriced: list[str] = []
    for position in person.positions():
        if closes.get(position.ticker) in (None, 0):
            unpriced.append(position.ticker)
            continue
        groups = [g for g in (_test_group(person, position.account, position.ticker, position.lots[:k], closes, fx,
                                           day, costs, cost_override, expects, net_gain, classes)
                              for k in range(1, len(position.lots) + 1)) if g is not None]
        flagged = [g for g in groups if g.flagged]
        chosen = max(flagged, key=lambda g: g.loss_ils) if flagged else max(groups, key=lambda g: g.loss_ils)
        out.append(chosen)
    return out, sorted(set(unpriced))


def _worth(person: Person, group: Group, price: float, fx: float, day: date) -> tuple[float, ...]:
    """D13: the loss's worth this year, against dividends (and the credit lost), and carried forward."""
    before = person.year_tax(day.year)
    cost = person.sale_cost(group.account, group.ticker, group.shares, price, fx, day)
    books = copy.deepcopy(person.books)
    books[group.account].sell(day, group.ticker, group.shares, price, fx)
    after = person._year_with(books, day.year)
    against_dividends = after.dividend_offset - before.dividend_offset
    credit_lost = after.lost_credit - before.lost_credit
    carried = -(after.carry_out - before.carry_out)
    against_gains = max(0.0, group.loss_ils - against_dividends - carried)
    worth_now = before.israeli_tax - after.israeli_tax
    return cost.tax_delta, worth_now, against_gains, against_dividends, credit_lost, carried, before.taxable_capital, before.net_capital


def harvest(person: Person, closes: Mapping[str, float], fx: float, day: date, classes: Mapping[str, str],
            expects: Dated = Dated(False, None), costs: CostTable = DEFAULT_COSTS,
            cost_override: Optional[float] = None, transactions: Iterable[Transaction] = (),
            question_6_open: bool = True) -> HarvestResult:
    """Section 6.3, one run: the suggestions one after another (D14), and the groups not flagged."""
    working = copy.deepcopy(person)
    suggestions: list[Harvest] = []
    taken: set[tuple[str, str]] = set()
    recent = [t for t in transactions if t.kind in ("buy", "transfer_in") and
              day - timedelta(days=PURCHASE_WINDOW_DAYS) <= t.day <= day]
    unpriced: list[str] = []
    for _ in range(100):
        groups, unpriced = _best_groups(working, closes, fx, day, costs, cost_override, expects.value, classes)
        flagged = [g for g in groups if g.flagged and (g.account, g.ticker) not in taken]
        if not flagged:
            break
        group = max(flagged, key=lambda g: g.loss_ils)
        price = float(closes[group.ticker])
        tax_delta, worth_now, against_gains, against_dividends, credit_lost, carried, net_gain, net = \
            _worth(working, group, price, fx, day)
        candidate = group.suggested
        assert candidate is not None
        line = Harvest(group, candidate.ticker, tax_delta, worth_now, against_gains, against_dividends, credit_lost,
                       carried, net_gain, net)
        if question_6_open:
            line.warnings.append("do not act before accountant question 6 (section 86) is answered")
        if against_dividends > 0:
            line.warnings.append(f"{against_dividends:,.0f} ILS of the loss goes against this year's dividends "
                                 "(accountant question 2: the dividend switch); the US credit lost is "
                                 f"{credit_lost:,.0f} ILS")
        if any(t.ticker == group.ticker for t in recent):
            line.warnings.append(f"{group.ticker} was bought in the last {PURCHASE_WINDOW_DAYS} days (a dividend "
                                 "reinvestment counts); Israel has no 30-day rule like the US, so this is only a reminder")
        else:
            line.warnings.append(f"buy no {group.ticker} in any account for {PURCHASE_WINDOW_DAYS} days after the sale "
                                 "(a reminder: Israel has no 30-day rule like the US)")
        suggested = fund(candidate.ticker)
        if suggested is not None and suggested.distributing:
            line.warnings.append(f"{candidate.ticker} pays out dividends: check that its next ex-dividend day is not "
                                 "within 5 trading days")
        line.warnings.append("check again on the day you trade")
        suggestions.append(line)
        taken.add((group.account, group.ticker))
        working.books[group.account].sell(day, group.ticker, group.shares, price, fx)
    groups, unpriced = _best_groups(working, closes, fx, day, costs, cost_override, expects.value, classes)
    not_flagged = [g for g in groups if (g.account, g.ticker) not in taken]
    sold = frozenset(s.group.ticker for s in suggestions)
    bought: dict[str, str] = {}
    for s in suggestions:
        klass = classes.get(s.group.ticker)
        if klass is not None and klass not in bought:
            bought[klass] = s.fund
    return HarvestResult(suggestions, not_flagged, unpriced, sold, bought)


__all__ = ["COST_MULTIPLE", "Candidate", "Group", "Harvest", "HarvestResult", "LOSS_FLOOR_ILS", "LOSS_SHARE",
           "PURCHASE_WINDOW_DAYS", "harvest"]
