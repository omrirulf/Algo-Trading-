#!/usr/bin/env python3
"""How much more an actively traded fund must earn, before tax, to tie with VT held for 20 years.

    python -m analysis.tax_breakeven                          # growth 6%, dividend yield 2%, 20 years
    python -m analysis.tax_breakeven --growth 0.05 --dividend-yield 0.02
    python -m analysis.tax_breakeven --table                  # a small grid of both

For information only (the owner's instruction of 2 Oct 2026): it is not a
gate, and nothing that decides reads it. The owner's own rough estimate was
about 0.8 points a year with a 2% yield.

Both books start with one dollar and pay Israeli tax by ``analysis.israel_tax``
(``config.israel_tax``'s rules), the exchange rate held still:

* **VT, held.** Its price grows by ``growth`` a year. Each year end it pays
  ``dividend_yield`` times the year's opening price; the US withholds its
  25% (W-8BEN) and the rest is reinvested as a new lot (rule c). Israel
  adds nothing on the dividend (the credit covers it). After ``years`` every
  lot is sold and the capital gain is taxed once.
* **The active fund.** The same yield, and ``growth + extra`` of price
  growth. It turns its whole book over every year: each year end it sells
  everything, pays the year's tax, and buys again with what is left -- so
  its gains are taxed every year instead of once at the end.

``extra`` is found by bisection: the smallest extra pre-tax return a year at
which the active fund's after-tax wealth after ``years`` equals VT's. It
leaves out what else an active fund pays (trading costs, the spread), so it
is the tax drag alone. The search looks only inside ``SEARCH_RANGE``; when
the answer is outside it (a very large ``growth``, say), it says so and
stops instead of giving the edge of the range as the answer.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path
from typing import Final, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis.israel_tax import DEFAULT_RULES, TaxBook, TaxRules, year_tax  # noqa: E402

#: The defaults: 20 years, the owner's 2% yield, and 6% of price growth.
YEARS = 20
GROWTH = 0.06
DIVIDEND_YIELD = 0.02
#: The exchange rate is held still, so shekel and dollar gains are the same.
_FX = 1.0
_TICKER = "VT"
#: Where the bisection looks for ``extra``, a fraction a year (-5 to +20
#: points). An answer outside it raises ``ValueError``; it is never clipped.
SEARCH_RANGE: Final[tuple[float, float]] = (-0.05, 0.20)


def _day(year: int) -> date:
    return date(2000 + year, 12, 31)


def held(years: int = YEARS, growth: float = GROWTH, dividend_yield: float = DIVIDEND_YIELD,
         rules: TaxRules = DEFAULT_RULES) -> float:
    """VT bought with $1, dividends reinvested net of the US tax, sold after ``years``: the after-tax wealth."""
    book = TaxBook(rules)
    price = 1.0
    book.buy(date(2000, 1, 1), _TICKER, 1.0, price, _FX)
    for year in range(1, years + 1):
        units = book.open_quantity(_TICKER)
        paid = units * dividend_yield * price
        price *= 1.0 + growth
        net = paid * (1.0 - rules.us_withholding)
        book.dividend(_day(year), _TICKER, paid, _FX, reinvest=(net / price, price))
    units = book.open_quantity(_TICKER)
    final = _day(years)
    book.sell(final, _TICKER, units, price, _FX)
    # The capital gain and the year's dividend are taxed in the last year; the
    # US tax on every dividend was already withheld from what was reinvested.
    carry = book.finished_years(final.year)
    carry_in = carry[-1].carry_out if carry else 0.0
    gains = [r.amount for r in book.realised if r.day.year == final.year]
    divs = [(d.gross_ils, d.us_withheld_ils) for d in book.received if d.day.year == final.year]
    last = year_tax(final.year, [a for a in gains if a > 0], [a for a in gains if a < 0], divs, carry_in, rules)
    israeli = sum(y.israeli_tax for y in carry) + last.israeli_tax
    return units * price - israeli


def active(extra: float, years: int = YEARS, growth: float = GROWTH, dividend_yield: float = DIVIDEND_YIELD,
           rules: TaxRules = DEFAULT_RULES) -> float:
    """$1 turned over every year at ``growth + extra``, taxed every year: the after-tax wealth."""
    cash, carry = 1.0, 0.0
    for year in range(1, years + 1):
        book = TaxBook(rules)
        start = date(2000 + year, 1, 1)
        book.buy(start, _TICKER, cash, 1.0, _FX)               # cash dollars of units at $1 each
        paid = cash * dividend_yield
        book.dividend(_day(year), _TICKER, paid, _FX)
        price = 1.0 + growth + extra
        book.sell(_day(year), _TICKER, cash, price, _FX)
        amounts = [r.amount for r in book.realised]
        divs = [(d.gross_ils, d.us_withheld_ils) for d in book.received]
        result = year_tax(2000 + year, [a for a in amounts if a > 0], [a for a in amounts if a < 0],
                          divs, carry, rules)
        carry = result.carry_out
        cash = cash * price + paid * (1.0 - rules.us_withholding) - result.israeli_tax
    return cash


def breakeven(years: int = YEARS, growth: float = GROWTH, dividend_yield: float = DIVIDEND_YIELD,
              rules: TaxRules = DEFAULT_RULES, tolerance: float = 1e-9) -> dict:
    """The extra pre-tax return a year (a fraction: 0.008 is 0.8 points) at which the two tie.

    Raises ``ValueError`` when the tie is not inside ``SEARCH_RANGE``.
    """
    target = held(years, growth, dividend_yield, rules)
    low, high = SEARCH_RANGE
    at_low = active(low, years, growth, dividend_yield, rules)
    at_high = active(high, years, growth, dividend_yield, rules)
    if not at_low <= target <= at_high:
        side = f"more than {high * 100:+.0f}" if target > at_high else f"less than {low * 100:+.0f}"
        raise ValueError(
            f"no break-even inside the search range ({low * 100:+.0f} to {high * 100:+.0f} points a year): "
            f"the answer is {side} points a year (growth {growth:.1%}, dividend yield {dividend_yield:.1%}, "
            f"{years} years; VT after tax {target:.3f}, the active fund {at_low:.3f} to {at_high:.3f})")
    while high - low > tolerance:
        middle = (low + high) / 2.0
        if active(middle, years, growth, dividend_yield, rules) < target:
            low = middle
        else:
            high = middle
    extra = (low + high) / 2.0
    return {
        "years": years, "growth": growth, "dividend_yield": dividend_yield,
        "offset_losses_vs_dividends": rules.offset_losses_vs_dividends, "w8ben": rules.w8ben,
        "vt_after_tax": target, "active_after_tax_at_zero": active(0.0, years, growth, dividend_yield, rules),
        "extra_per_year": extra,
    }


def table(growths: Sequence[float] = (0.04, 0.05, 0.06, 0.07, 0.08),
          yields: Sequence[float] = (0.015, 0.02, 0.025), years: int = YEARS,
          rules: TaxRules = DEFAULT_RULES) -> list[dict]:
    """``breakeven`` over a grid, growth fastest within each yield."""
    return [breakeven(years, g, y, rules) for y in yields for g in growths]


def render(rows: Sequence[dict]) -> str:
    lines = ["Extra pre-tax return a year an actively traded fund needs to tie with VT held "
             f"for {rows[0]['years']} years, after Israeli tax (for information only; not a gate)", "",
             "| VT price growth | Dividend yield | VT after tax ($1 in) | Extra needed (points a year) |",
             "| --- | --- | --- | --- |"]
    for row in rows:
        lines.append(f"| {row['growth']:.1%} | {row['dividend_yield']:.1%} | {row['vt_after_tax']:.3f} "
                     f"| {row['extra_per_year'] * 100:.2f} |")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="analysis.tax_breakeven", description=__doc__.split("\n\n")[0])
    parser.add_argument("--years", type=int, default=YEARS)
    parser.add_argument("--growth", type=float, default=GROWTH, help="VT's price growth a year (0.06 is 6%%)")
    parser.add_argument("--dividend-yield", type=float, default=DIVIDEND_YIELD)
    parser.add_argument("--table", action="store_true", help="a grid of growth and yield instead of one row")
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.years < 1:
        print("--years must be at least 1", file=sys.stderr)
        return 2
    try:
        rows = table(years=args.years) if args.table else [breakeven(args.years, args.growth, args.dividend_yield)]
    except ValueError as error:
        print(error, file=sys.stderr)
        return 2
    print(render(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["DIVIDEND_YIELD", "GROWTH", "SEARCH_RANGE", "YEARS", "active", "breakeven", "held", "render", "table"]
