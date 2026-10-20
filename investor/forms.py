"""The annual report pack (sections 7.2 and 7.3): form rows, the year's summary, the dividend rows.

* **Form 1325** (appendix C1 of the annual return 1301) lists every sale of
  traded securities with no tax withheld at source: one row per closed lot
  or part of one, in FIFO order, with the fund and its ID, the quantity, the
  purchase day, the cost in shekels at the purchase day's rate, the rate
  ratio (the index for a dollar security), the adjusted cost, the sale day,
  the proceeds in shekels and the real gain or loss. The dollar amounts, the
  nominal gain and the inflationary amount are kept beside them.
* **Form 1322** (appendix C) is the year's summary, from ``year_tax``.
* **Dividends**: one row each, gross in shekels, the US tax at its own day's
  rate, Israel's tax, the credit, the extra and any credit lost -- what the
  foreign-income appendix (form 1324, question 9) asks for.

The exact fields of each form are to be copied from the Tax Authority's
current forms, and the mapping goes to the accountant (question 13) before
anything is filed from it. How a fall of the dollar shows in the 1325
columns (the adjusted cost is never below the cost for a gain, T1) is part
of that question.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Optional

from analysis.israel_tax import YearTax, dividend_tax
from investor.funds import fund
from investor.ledger import Person


@dataclass(frozen=True)
class Row1325:
    account: str
    ticker: str
    isin: str
    kind: str
    qty: float
    bought_on: Optional[date]
    sold_on: date
    fx_open: Optional[float]
    fx_close: float
    usd_cost: Optional[float]
    usd_proceeds: Optional[float]
    cost_ils: float
    proceeds_ils: float
    nominal_ils: float
    inflation_ils: float
    #: The index: the sale day's rate over the purchase day's.
    ratio: Optional[float]
    adjusted_cost_ils: float
    #: The real gain (> 0) or allowable loss (< 0).
    real_ils: float


@dataclass(frozen=True)
class DividendRow:
    day: date
    account: str
    ticker: str
    gross_usd: float
    fx: float
    gross_ils: float
    us_withheld_ils: float
    israeli_tax_ils: float
    credit_ils: float
    extra_ils: float
    lost_ils: float


def rows_1325(person: Person, year: int) -> list[Row1325]:
    out: list[Row1325] = []
    for account, r in person.realised_rows(year):
        if r.gain is None:
            continue
        g = r.gain
        if g.nominal >= 0:
            adjusted = g.cost_ils + max(g.inflation, 0.0)
        else:
            adjusted = g.cost_ils + min(g.inflation, 0.0)
        known = fund(r.ticker)
        ratio = (r.fx_close / r.fx_open) if r.fx_open and r.fx_close else None
        out.append(Row1325(account, r.ticker, known.isin if known else "", r.kind, r.qty, r.opened, r.day, r.fx_open,
                           r.fx_close or 0.0, r.usd_open, r.usd_close, g.cost_ils, g.proceeds_ils, g.nominal, g.inflation,
                           ratio, adjusted, r.amount))
    return out


def form_1322(person: Person, year: int) -> YearTax:
    """The year's summary: gains, losses, the loss against dividends, the carry in and out, the tax."""
    return person.year_tax(year)


def dividend_rows(person: Person, year: int) -> list[DividendRow]:
    out: list[DividendRow] = []
    for d in person.dividends:
        if d.day.year != year:
            continue
        tax = dividend_tax(d.gross_ils, person.rules, us_withheld_ils=d.withheld_ils)
        out.append(DividendRow(d.day, d.account, d.ticker, d.gross_usd, d.fx, d.gross_ils, d.withheld_ils,
                               tax.israeli_tax_ils, tax.credit_ils, tax.extra_ils, tax.lost_ils))
    return out


__all__ = ["DividendRow", "Row1325", "dividend_rows", "form_1322", "rows_1325"]
