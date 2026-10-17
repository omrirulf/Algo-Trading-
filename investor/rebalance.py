"""Rebalancing (section 5): new money first, tax-free moves second, taxable sales last, the tax cost before every line.

The owner's rule (5.1), as the code reads it (5.2):

* **Weights** are of every account at market value before tax, in shekels.
  Cash counts in the total and in no class; a mixed tax-free track counts in
  each class by its mix.
* **Band** = the smaller of 5 points and 25% of the target. On the edge is
  inside. **Trade to** = 1 point inside the band towards the target; with a
  band of 1 point or less (a target of 4% or less), the target itself (D5).
* **Order** (5.3): new contributions (D4), then moves between the tracks of
  a tax-free account, then taxable sales -- each class above target drawn on
  in order of the lowest tax per shekel, never below its target (D8).
* **A taxable sale is suggested** when its tax cost (D6: this year's extra
  tax plus 25% of the loss it uses up) is under 0.5% of its gross proceeds,
  or the drift (D7: measured once at the start of the taxable step, the
  largest among the classes the sale moves towards target) is above 10
  points. Otherwise the line says "not suggested", with the same cost.
* **The money stays in its account**: a sale buys, in the same account, the
  classes below target, the largest gap first; what is left stays as cash.
  A fund being harvested or sold in the same run is never bought.
* **Whole shares** at a broker; a tax-free account takes exact shekels. If
  no whole count can put a class inside its band, nothing is suggested and
  the line says from what total it will fit (T23).

Every line carries its tax cost, 0 included; the report prints it first and
ends each line with "Suggestion only: you decide and trade yourself."
"""

from __future__ import annotations

import copy
import math
from dataclasses import dataclass, field
from datetime import date
from typing import Mapping, Optional

from investor.files import Plan
from investor.funds import CostTable, DEFAULT_COSTS, fund
from investor.ledger import Person, SaleCost

#: 5.1: bands of +-5 points, 25% relative under a target of 20%.
BAND_POINTS = 5.0
BAND_RELATIVE = 0.25
#: Trade back to the band edge minus 1 point.
INSIDE_POINTS = 1.0
#: A taxable sale needs a tax cost under 0.5% of what it sells...
COST_SHARE_LIMIT = 0.005
#: ...unless the drift is above 10 points.
DRIFT_OVERRIDE_POINTS = 10.0
#: Weights are compared on unrounded numbers with a tiny tolerance (5.2).
_TOL = 1e-9

CONTRIBUTION = "contribution"
TAX_FREE_MOVE = "tax_free_move"
SALE = "sale"
BUY = "buy"


class PlanError(ValueError):
    """The plan cannot be read as a portfolio: targets that do not add up, a fund with no class."""


@dataclass
class ClassRow:
    name: str
    target: float
    band: float
    value: float
    weight: float

    @property
    def drift(self) -> float:
        """Points from the target, absolute."""
        return abs(self.weight - self.target)

    @property
    def above_band(self) -> bool:
        return self.weight > self.target + self.band + _TOL

    @property
    def below_band(self) -> bool:
        return self.weight < self.target - self.band - _TOL

    @property
    def out_of_band(self) -> bool:
        return self.above_band or self.below_band

    @property
    def trade_to_above(self) -> float:
        return self.target if self.band <= INSIDE_POINTS + _TOL else self.target + self.band - INSIDE_POINTS

    @property
    def trade_to_below(self) -> float:
        return self.target if self.band <= INSIDE_POINTS + _TOL else self.target - self.band + INSIDE_POINTS


def band_for(target: float) -> float:
    return min(BAND_POINTS, BAND_RELATIVE * target)


@dataclass
class Holding:
    account: str
    ticker: str
    qty: float
    price_usd: float
    klass: str

    def value(self, fx: float) -> float:
        return self.qty * self.price_usd * fx


@dataclass
class Line:
    """One suggestion (or one "not suggested"), structured; the report words it."""

    step: str
    account: str
    klass: str
    #: The fund (or the track) the line is about, and the one it moves money to.
    ticker: str = ""
    to: str = ""
    shares: float = 0.0
    amount_ils: float = 0.0
    tax_cost_ils: float = 0.0
    #: The cost against the proceeds, for a sale.
    cost_share: Optional[float] = None
    suggested: bool = True
    reason: str = ""
    #: Things shown beside the line: other funds' costs, the specific-lot note, warnings.
    notes: list[str] = field(default_factory=list)
    #: The buys a sale's money makes, in the same account.
    buys: list["Line"] = field(default_factory=list)
    #: What is left as cash after the buys.
    cash_left_ils: float = 0.0
    #: The trading cost beside the tax cost (commission and half the spread), in shekels.
    trading_cost_ils: float = 0.0


@dataclass
class Rebalance:
    day: date
    fx: float
    total_ils: float
    classes: list[ClassRow]
    #: The table after the contribution step, and after the whole plan.
    after: list[ClassRow]
    contributions: list[Line]
    moves: list[Line]
    sales: list[Line]
    notes: list[str]
    cash_ils: dict[str, float]

    @property
    def lines(self) -> list[Line]:
        return self.contributions + self.moves + self.sales


# --------------------------------------------------------------------------- #
# The working portfolio
# --------------------------------------------------------------------------- #


class _Portfolio:
    def __init__(self, person: Person, plan: Plan, closes: Mapping[str, float], fx: float, day: date,
                 costs: CostTable, avoid: frozenset[str], prefer: Mapping[str, str]) -> None:
        self.person, self.plan, self.closes, self.fx, self.day = person, plan, closes, fx, day
        self.costs, self.avoid, self.prefer = costs, avoid, dict(prefer)
        self.notes: list[str] = []
        if abs(sum(plan.targets.values()) - 100.0) > 1e-6:
            raise PlanError("the targets do not add up to 100")
        self.holdings: list[Holding] = []
        for position in person.positions():
            klass = plan.class_of(position.ticker)
            if klass is None or klass not in plan.targets:
                raise PlanError("a fund held has no class in plan.csv, or its class has no target")
            price = closes.get(position.ticker)
            if price is None or not price > 0:
                self.notes.append(f"{position.ticker} in {position.account} has no price today: valued at cost, "
                                  "and left out of every suggestion")
                price = math.fsum(l.usd for l in position.lots) / position.qty
                self.holdings.append(Holding(position.account, position.ticker, position.qty, price, klass))
                continue
            self.holdings.append(Holding(position.account, position.ticker, position.qty, float(price), klass))
        self.unpriced = {h.ticker for h in self.holdings if closes.get(h.ticker) in (None, 0)}
        self.tracks: dict[str, dict[str, float]] = {a: dict(t) for a, t in person.tracks.items()}
        for account, from_track, to_track, amount, _ in plan.pending:
            tracks = self.tracks.setdefault(account, {})
            tracks[from_track] = tracks.get(from_track, 0.0) - amount
            tracks[to_track] = tracks.get(to_track, 0.0) + amount
        for account, tracks in self.tracks.items():
            for track in tracks:
                if (account, track) not in plan.track_mix:
                    raise PlanError("a tax-free track has no mix in plan.csv")
        self.cash: dict[str, float] = {a: c.ils_value(fx) for a, c in person.cash.items()}
        for account, cash in self.cash.items():
            if cash < -0.005:
                self.notes.append(f"{account}: its cash is negative in the records (a deposit may be missing); "
                                  "counted as 0 for new purchases")
        self.working = copy.deepcopy(person)

    # -- weights ----------------------------------------------------------- #

    def mix(self, account: str, track: str) -> dict[str, float]:
        return self.plan.track_mix[(account, track)]

    def values(self) -> dict[str, float]:
        out = {name: 0.0 for name in self.plan.targets}
        for h in self.holdings:
            out[h.klass] += h.value(self.fx)
        for account, tracks in self.tracks.items():
            for track, value in tracks.items():
                for klass, pct in self.mix(account, track).items():
                    out[klass] += value * pct / 100.0
        return out

    def total(self) -> float:
        return math.fsum(self.values().values()) + math.fsum(self.cash.values())

    def table(self) -> list[ClassRow]:
        total = self.total()
        values = self.values()
        return [ClassRow(name, target, band_for(target), values[name], 100.0 * values[name] / total if total else 0.0)
                for name, target in self.plan.targets.items()]

    def row(self, name: str) -> ClassRow:
        return next(r for r in self.table() if r.name == name)

    def target_value(self, name: str) -> float:
        return self.total() * self.plan.targets[name] / 100.0

    # -- funds to buy ------------------------------------------------------ #

    def fund_to_buy(self, account: str, klass: str) -> Optional[Holding]:
        """The fund of ``klass`` to buy in ``account``: the one preferred, else the largest held, else plan.csv's."""
        preferred = self.prefer.get(klass)
        held = sorted((h for h in self.holdings if h.account == account and h.klass == klass
                       and h.ticker not in self.avoid and h.ticker not in self.unpriced),
                      key=lambda h: -h.value(self.fx))
        ticker = preferred if preferred and preferred not in self.avoid else (held[0].ticker if held else None)
        if ticker is None:
            ticker = self.plan.buy_first.get(klass)
        if ticker is None or ticker in self.avoid:
            return None
        price = self.closes.get(ticker)
        if price is None or not price > 0:
            return None
        existing = next((h for h in self.holdings if h.account == account and h.ticker == ticker), None)
        if existing is None:
            existing = Holding(account, ticker, 0.0, float(price), klass)
            self.holdings.append(existing)
        return existing

    def buy_shares(self, holding: Holding, shares: float) -> float:
        """Buy whole shares with the account's cash; returns what it cost in shekels."""
        cost = shares * holding.price_usd * self.fx
        holding.qty += shares
        self.cash[holding.account] -= cost
        return cost

    def fits_note(self, row: ClassRow, holding: Holding) -> Optional[str]:
        """T23: no whole count puts the class inside its band -- from what total would one share more fit."""
        total = self.total()
        price = holding.price_usd * self.fx
        lower = (row.target - row.band) / 100.0
        upper = (row.target + row.band) / 100.0
        k = max(1, math.ceil((lower * total - row.value) / price - _TOL))
        if (row.value + k * price) / total <= upper + _TOL:
            return None
        needed = (row.value + k * price) / upper
        return (f"{row.name}: no whole number of shares of {holding.ticker} puts it inside its band today; "
                f"it fits once the total is {needed:,.0f} ILS")


# --------------------------------------------------------------------------- #
# The steps
# --------------------------------------------------------------------------- #


def _contributions(p: _Portfolio) -> list[Line]:
    lines: list[Line] = []
    for account, (amount, currency) in p.plan.contributions.items():
        p.cash[account] = p.cash.get(account, 0.0) + (amount * p.fx if currency == "USD" else amount)
    money = {a: max(0.0, c) for a, c in p.cash.items()}
    if not any(m > 0.005 for m in money.values()):
        return lines
    # Pass 1: classes below their band, the largest shekel gap first; pass 2: the other classes below target.
    for below_band_only in (True, False):
        while True:
            rows = [r for r in p.table() if (r.below_band if below_band_only else not r.below_band)
                    and p.target_value(r.name) - r.value > 0.005]
            if not rows:
                break
            rows.sort(key=lambda r: -(p.target_value(r.name) - r.value))
            bought = False
            for row in rows:
                for account in sorted(money, key=lambda a: -money[a]):
                    if money[account] <= 0.005:
                        continue
                    line = _contribute(p, account, row, money, below_band_only)
                    if line is not None:
                        lines.append(line)
                        bought = True
                        break
                if bought:
                    break
            if not bought:
                break
    return lines


def _contribute(p: _Portfolio, account: str, row: ClassRow, money: dict[str, float],
                below_band: bool) -> Optional[Line]:
    gap = p.target_value(row.name) - row.value
    taxable = p.person.accounts[account].taxable
    if not taxable:
        track = next((t for t in p.tracks.get(account, {}) if p.mix(account, t).get(row.name) == 100.0), None)
        if track is None:
            track = next((t for (a, t), mix in p.plan.track_mix.items() if a == account and mix.get(row.name) == 100.0),
                         None)
        if track is None:
            return None
        amount = min(gap, money[account])
        p.tracks.setdefault(account, {})[track] = p.tracks[account].get(track, 0.0) + amount
        p.cash[account] -= amount
        money[account] -= amount
        return Line(CONTRIBUTION, account, row.name, ticker=track, amount_ils=amount, tax_cost_ils=0.0,
                    reason="new money, to a class below its band" if below_band else "new money, to a class below target")
    holding = p.fund_to_buy(account, row.name)
    if holding is None:
        return None
    price = holding.price_usd * p.fx
    if below_band:
        k = math.ceil(gap / price - _TOL)
        upper = (row.target + row.band) / 100.0
        if (row.value + k * price) / p.total() > upper + _TOL:
            k = math.floor(gap / price + _TOL)
        if k < 1:
            note = p.fits_note(row, holding)
            if note and note not in p.notes:
                p.notes.append(note)
            return None
    else:
        k = math.floor(gap / price + _TOL)
    k = min(k, math.floor(money[account] / price + _TOL))
    if k < 1:
        return None
    cost = p.buy_shares(holding, k)
    money[account] -= cost
    return Line(CONTRIBUTION, account, row.name, ticker=holding.ticker, shares=k, amount_ils=cost, tax_cost_ils=0.0,
                reason="new money, to a class below its band" if below_band else "new money, to a class below target",
                trading_cost_ils=p.costs.side_usd(fund(holding.ticker), k, holding.price_usd) * p.fx)


def _needs(p: _Portfolio) -> tuple[dict[str, float], dict[str, float]]:
    """Money each class above its band must shed to its trade-to point, and each class below must take."""
    sell: dict[str, float] = {}
    buy: dict[str, float] = {}
    total = p.total()
    for row in p.table():
        if row.above_band:
            sell[row.name] = row.value - total * row.trade_to_above / 100.0
        elif row.below_band:
            buy[row.name] = total * row.trade_to_below / 100.0 - row.value
    return sell, buy


def _tax_free_moves(p: _Portfolio) -> list[Line]:
    lines: list[Line] = []
    for _ in range(50):
        sell, buy = _needs(p)
        if not sell or not buy:
            break
        moved = False
        for a_name in sorted(sell, key=lambda c: -sell[c]):
            for b_name in sorted(buy, key=lambda c: -buy[c]):
                best = None
                for account, tracks in p.tracks.items():
                    for from_track, value in tracks.items():
                        if value <= 0.005:
                            continue
                        for (acc, to_track), to_mix in p.plan.track_mix.items():
                            if acc != account or to_track == from_track:
                                continue
                            from_mix = p.mix(account, from_track)
                            d_a = from_mix.get(a_name, 0.0) / 100.0 - to_mix.get(a_name, 0.0) / 100.0
                            d_b = to_mix.get(b_name, 0.0) / 100.0 - from_mix.get(b_name, 0.0) / 100.0
                            if d_a <= _TOL or d_b <= _TOL:
                                continue
                            if best is None or d_a > best[0]:
                                best = (d_a, d_b, account, from_track, to_track, value)
                if best is None:
                    continue
                d_a, d_b, account, from_track, to_track, value = best
                amount = min(sell[a_name] / d_a, buy[b_name] / d_b, value)
                if amount <= 0.005:
                    continue
                p.tracks[account][from_track] = value - amount
                p.tracks[account][to_track] = p.tracks[account].get(to_track, 0.0) + amount
                lines.append(Line(TAX_FREE_MOVE, account, a_name, ticker=from_track, to=to_track, amount_ils=amount,
                                  tax_cost_ils=0.0, reason=f"{a_name} down, {b_name} up, inside the tax-free account"))
                moved = True
                break
            if moved:
                break
        if not moved:
            break
    return lines


def _sources(p: _Portfolio) -> list[tuple[float, Holding, int]]:
    """Every taxable holding of a class above target: its tax per shekel for one share, and how many it can give."""
    out: list[tuple[float, Holding, int]] = []
    for h in p.holdings:
        if h.qty < 1 or h.ticker in p.avoid or h.ticker in p.unpriced:
            continue
        room = p.row(h.klass).value - p.target_value(h.klass)
        capacity = min(math.floor(room / (h.price_usd * p.fx) + _TOL), math.floor(h.qty + _TOL))
        if capacity < 1:
            continue
        cost = p.working.sale_cost(h.account, h.ticker, 1, h.price_usd, p.fx, p.day)
        out.append((cost.share if cost.share is not None else 0.0, h, capacity))
    return sorted(out, key=lambda item: (item[0], item[1].account, item[1].ticker))


def _nearest(amount: float, price: float) -> int:
    """The share count nearest ``amount``; fewer on a tie."""
    low = math.floor(amount / price + _TOL)
    high = low + 1
    return low if abs(low * price - amount) <= abs(high * price - amount) + _TOL else high


def _months_to_close(p: _Portfolio, gap: float) -> Optional[int]:
    monthly = math.fsum(amount * (p.fx if currency == "USD" else 1.0)
                        for amount, currency in p.plan.contributions.values())
    return math.ceil(gap / monthly) if monthly > 0 else None


def _taxable_sales(p: _Portfolio) -> list[Line]:
    lines: list[Line] = []
    drift = {r.name: r.drift for r in p.table()}          # D7: measured once, now
    for _ in range(50):
        sell, buy = _needs(p)
        if not sell and not buy:
            break
        sources = _sources(p)
        if not sources:
            break
        share, holding, capacity = sources[0]
        own = sell.get(holding.klass, 0.0)
        need = math.fsum(buy.values())
        want = max(own, need)
        if want <= 0.005:
            break
        price = holding.price_usd * p.fx
        shares = min(_nearest(want, price), capacity)
        if shares < 1:
            p.avoid = p.avoid | {holding.ticker}
            continue
        cost = p.working.sale_cost(holding.account, holding.ticker, shares, holding.price_usd, p.fx, p.day)
        buyers = [name for name in sorted(buy, key=lambda c: -buy[c])]
        moved = [holding.klass] + buyers
        worst = max(drift.get(name, 0.0) for name in moved)
        suggested = (cost.share is not None and cost.share < COST_SHARE_LIMIT) or worst > DRIFT_OVERRIDE_POINTS + _TOL
        if cost.share is not None and cost.share < COST_SHARE_LIMIT:
            reason = f"tax cost under {COST_SHARE_LIMIT:.1%} of the sale"
        elif worst > DRIFT_OVERRIDE_POINTS + _TOL:
            reason = f"tax cost over {COST_SHARE_LIMIT:.1%}, suggested because the drift is {worst:.2f} points, above 10"
        else:
            months = _months_to_close(p, want)
            reason = (f"tax cost over {COST_SHARE_LIMIT:.1%} and the drift is {worst:.2f} points, not above 10"
                      + (f"; about {months} month(s) of contributions would close the gap" if months else ""))
        line = Line(SALE, holding.account, holding.klass, ticker=holding.ticker, shares=shares,
                    amount_ils=cost.proceeds_ils, tax_cost_ils=cost.cost, cost_share=cost.share, suggested=suggested,
                    reason=reason, trading_cost_ils=p.costs.side_usd(fund(holding.ticker), shares, holding.price_usd) * p.fx)
        for other_share, other, other_capacity in sources[1:]:
            if other.klass != holding.klass:
                continue
            k = min(_nearest(want, other.price_usd * p.fx), other_capacity)
            if k >= 1:
                alt = p.working.sale_cost(other.account, other.ticker, k, other.price_usd, p.fx, p.day)
                line.notes.append(f"{k} {other.ticker} in {other.account} would cost {alt.cost:,.2f} ILS "
                                  f"({(alt.share or 0.0):.2%})")
        if cost.best_specific is not None:
            number, amount = cost.best_specific
            what = f"a loss of {-amount:,.0f}" if amount < 0 else f"a gain of {amount:,.0f}"
            line.notes.append(f"with specific lots (lot {number}) it would be {what}; not allowed while FIFO "
                              "applies (accountant question 3)")
        p.avoid = p.avoid | {holding.ticker}
        if not suggested:
            lines.append(line)
            continue
        p.working.books[holding.account].sell(p.day, holding.ticker, shares, holding.price_usd, p.fx)
        holding.qty -= shares
        p.cash[holding.account] += cost.proceeds_ils
        money = {holding.account: cost.proceeds_ils}
        for below_band_only in (True, False):
            while money[holding.account] > 0.005:
                rows = [r for r in p.table() if r.name != holding.klass
                        and (r.below_band if below_band_only else not r.below_band)
                        and p.target_value(r.name) - r.value > 0.005]
                if not rows:
                    break
                rows.sort(key=lambda r: -(p.target_value(r.name) - r.value))
                bought = None
                for row in rows:
                    bought = _contribute(p, holding.account, row, money, below_band_only)
                    if bought is not None:
                        bought.step = BUY
                        bought.reason = "bought with the sale's money, in the same account"
                        line.buys.append(bought)
                        break
                if bought is None:
                    break
        line.cash_left_ils = money[holding.account]
        lines.append(line)
    sell, buy = _needs(p)
    for name in buy:
        row = p.row(name)
        for account in p.person.accounts:
            if not p.person.accounts[account].taxable:
                continue
            holding = p.fund_to_buy(account, name)
            if holding is not None:
                note = p.fits_note(row, holding)
                if note and note not in p.notes:
                    p.notes.append(note)
                break
    return lines


def rebalance(person: Person, plan: Plan, closes: Mapping[str, float], fx: float, day: date,
              costs: CostTable = DEFAULT_COSTS, avoid: frozenset[str] = frozenset(),
              prefer: Optional[Mapping[str, str]] = None) -> Rebalance:
    """The whole plan for one run (5.3). ``avoid`` are funds never to buy (sold or harvested this run)."""
    p = _Portfolio(person, plan, closes, fx, day, costs, frozenset(avoid), prefer or {})
    before = p.table()
    contributions = _contributions(p)
    moves = _tax_free_moves(p)
    sales = _taxable_sales(p)
    return Rebalance(day, fx, p.total(), before, p.table(), contributions, moves, sales, p.notes, dict(p.cash))


__all__ = ["BAND_POINTS", "BAND_RELATIVE", "BUY", "CONTRIBUTION", "COST_SHARE_LIMIT", "DRIFT_OVERRIDE_POINTS",
           "INSIDE_POINTS", "SALE", "TAX_FREE_MOVE", "ClassRow", "Holding", "Line", "PlanError", "Rebalance",
           "band_for", "rebalance"]
