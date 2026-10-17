"""The report (section 7), and the command line: ``python -m investor.report --data DIR --out DIR``.

One Markdown file, text and tables only, written as ``latest.md`` and as
``YYYY-MM-DD.md`` in the folder ``--out`` names:

1. **Summary**: the total value; the value if sold today; the tax paid so
   far; the close and the rate used, with their dates, and every day whose
   rate did not come from the Bank of Israel.
2. **Allocation and rebalancing** (section 5), the tax cost first on every
   line.
3. **Harvest** (section 6), or "nothing to flag".
4. **Against VT and VWRA** (section 7.4).
5. **The annual report pack** (sections 7.2 and 7.3), this year so far and
   each finished year.
6. **What is assumed**: the open accountant questions, the dated answers,
   the surtax.

The command line prints one line, "report written", with the line count,
and an error prints only its kind: no amount, share, ticker or account name
ever reaches the screen, a log or an exception (section 2.6, test T41).
``--data`` has no default, there is no environment variable or ``.env``
lookup, and both folders are refused inside this repository.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Optional, Sequence

from investor import REPOSITORY
from investor.benchmark import BenchmarkBook, benchmark
from investor.files import DataError, Inputs, inside_repository, read_folder
from investor.forms import DividendRow, Row1325, dividend_rows, form_1322, rows_1325
from investor.funds import BY_TICKER, CostTable, DEFAULT_COSTS, US, US_ESTATE_TAX_LINE_USD, fund
from investor.harvest import HarvestResult, harvest
from investor.ledger import HalfYear, IfSold, Person, WEEKEND
from investor.market import Market, MarketError
from investor.rebalance import BUY, CONTRIBUTION, SALE, TAX_FREE_MOVE, Line, PlanError, Rebalance, rebalance

SUGGESTION_ONLY = "Suggestion only: you decide and trade yourself."
#: A dated yes/no older than this is pointed out.
ANSWER_AGE_DAYS = 365


def _ils(value: float) -> str:
    sign = "−" if value < 0 else ""
    return f"{sign}{abs(value):,.2f} ILS"


def _usd(value: float) -> str:
    sign = "−" if value < 0 else ""
    return f"{sign}${abs(value):,.2f}"


def _pct(value: Optional[float]) -> str:
    return "n/a" if value is None else f"{value * 100:.2f}%"


def _tax_cost(value: float) -> str:
    if abs(value) < 0.005:
        return "Tax cost: 0.00 ILS."
    if value < 0:
        return f"Tax cost: {_ils(value)} (a saving)."
    return f"Tax cost: {_ils(value)}."


def _shares(value: float) -> str:
    return f"{value:,.0f}" if abs(value - round(value)) < 1e-9 else f"{value:,.4f}"


# --------------------------------------------------------------------------- #
# Sections
# --------------------------------------------------------------------------- #


def _summary(day: date, fx: float, state: IfSold, person: Person, market: Market) -> list[str]:
    lines = ["## 1. Summary", "",
             f"| | Shekels | Dollars |", "| --- | ---: | ---: |",
             f"| Market value | {_ils(state.market_ils)} | {_usd(state.market_usd)} |",
             f"| Value if sold today | **{_ils(state.value_ils)}** | {_usd(state.value_usd)} |",
             f"| This year's tax if every taxable lot were sold today | {_ils(state.tax_if_sold_ils)} | "
             f"{_usd(state.tax_if_sold_ils / fx)} |",
             f"| Advances recorded as paid this year | {_ils(state.advances_paid_ils)} | |",
             f"| Tax of finished years still unpaid (from payments.csv) | {_ils(state.unpaid_finished_ils)} | |",
             f"| Tax paid so far (computed: finished years {_ils(state.finished_tax_ils)}, this year "
             f"{_ils(state.this_year_tax_ils)}, US tax withheld {_ils(state.us_withheld_ils)}) | "
             f"{_ils(state.tax_paid_so_far_ils)} | |",
             f"| The cost of selling everything (not taken off) | {_ils(state.selling_cost_ils)} | |", ""]
    lines.append(f"Priced at the close of {day.isoformat()} and the Bank of Israel's rate of {fx:.4f} ILS per dollar "
                 f"on that day. \"Value if sold today\" takes no selling cost off, as the after-tax gate assumes; "
                 f"dividends arrived net, so the US tax is not taken off again. The tax-free accounts are shown at "
                 f"their value, with no withdrawal tax taken off (D9).")
    if state.unpriced:
        lines.append(f"\nFunds with no price today, valued at what they cost: {', '.join(state.unpriced)}.")
    fallback = market.fallback_days()
    weekend = sorted({d for d, kind in person.rate_notes if kind == WEEKEND})
    overrides = sorted({d for d, kind in person.rate_notes if kind != WEEKEND})
    if fallback or weekend or overrides:
        lines.append("")
        if fallback:
            shown = ", ".join(f"{d.isoformat()} ({src})" for d, src in fallback[:20])
            lines.append(f"Days whose rate did not come from the Bank of Israel: {len(fallback)} ({shown}"
                         f"{', …' if len(fallback) > 20 else ''}).")
        if weekend:
            lines.append(f"Weekend days priced at the last weekday's rate (a rule for accountant question 4): "
                         f"{len(weekend)} ({', '.join(d.isoformat() for d in weekend[:20])}).")
        if overrides:
            lines.append(f"Rows whose own rate was used instead of the Bank's: {len(overrides)} "
                         f"({', '.join(d.isoformat() for d in overrides[:20])}).")
    return lines + [""]


def _line_words(line: Line) -> str:
    if line.step == CONTRIBUTION:
        what = (f"put {_ils(line.amount_ils)} of new money into the {line.ticker} track" if not line.shares
                else f"buy {_shares(line.shares)} {line.ticker} for {_ils(line.amount_ils)}")
        return f"{_tax_cost(line.tax_cost_ils)} In {line.account}, {what} ({line.klass}: {line.reason}). {SUGGESTION_ONLY}"
    if line.step == TAX_FREE_MOVE:
        return (f"{_tax_cost(0.0)} In {line.account}, move {_ils(line.amount_ils)} from the {line.ticker} track to the "
                f"{line.to} track ({line.reason}). {SUGGESTION_ONLY}")
    if line.step == SALE:
        verb = "Sell" if line.suggested else "Not suggested: selling"
        text = (f"{_tax_cost(line.tax_cost_ils)} {verb} {_shares(line.shares)} {line.ticker} in {line.account} for "
                f"{_ils(line.amount_ils)} ({line.klass}; tax cost {_pct(line.cost_share)} of the sale; "
                f"commission and spread about {_ils(line.trading_cost_ils)}, not in the tax cost): {line.reason}.")
        for buy in line.buys:
            text += f" The money buys {_shares(buy.shares)} {buy.ticker} ({buy.klass}) for {_ils(buy.amount_ils)}."
        if line.suggested and line.cash_left_ils > 0.005:
            text += f" {_ils(line.cash_left_ils)} stays as cash and counts as next month's contribution."
        for note in line.notes:
            text += f" Beside it: {note}."
        return text + f" {SUGGESTION_ONLY}"
    return f"{_tax_cost(line.tax_cost_ils)} {line.reason}. {SUGGESTION_ONLY}"


def _allocation(plan_result: Rebalance) -> list[str]:
    lines = ["## 2. Allocation and rebalancing", "",
             "| Class | Target | Band | Weight today | Drift (points) | Out of band | Weight after the plan |",
             "| --- | ---: | ---: | ---: | ---: | --- | ---: |"]
    after = {row.name: row for row in plan_result.after}
    for row in plan_result.classes:
        lines.append(f"| {row.name} | {row.target:.2f}% | ±{row.band:.2f} | {row.weight:.2f}% | {row.drift:.2f} | "
                     f"{'yes' if row.out_of_band else 'no'} | {after[row.name].weight:.2f}% |")
    lines.append("")
    lines.append(f"Total {_ils(plan_result.total_ils)}, every account at market value before tax; cash counts in the "
                 "total and in no class. Bands: ±5 points, or 25% of the target under 20%; on the edge is inside. "
                 "Order: new money first, moves inside the tax-free accounts second, taxable sales last; a taxable "
                 "sale is suggested when its tax cost is under 0.5% of the sale, or the drift is above 10 points (D7).")
    lines.append("")
    if not plan_result.lines:
        lines.append("Nothing to do: every class is inside its band, and there is no new money to place.")
    for line in plan_result.lines:
        lines.append(f"- {_line_words(line)}")
    for note in plan_result.notes:
        lines.append(f"- Note: {note}.")
    return lines + [""]


def _harvest(result: HarvestResult) -> list[str]:
    lines = ["## 3. Harvest suggestions", "",
             "The rule is read as A (the loss is at least the larger of 2,000 ILS and 5% of what is sold) and B "
             "(25% of the loss is at least 5 times the trading cost) and C (a net gain this year, or gains expected "
             "within 3 years, or a domicile switch). FIFO: a later lot cannot be sold before the earlier lots of the "
             "same fund in the same account, so every test is on a group of lots (D10).", ""]
    if not result.suggestions:
        lines.append("Nothing to flag.")
    for s in result.suggestions:
        g = s.group
        c = next(c for c in g.candidates if c.ticker == s.fund)
        text = (f"{_tax_cost(s.tax_delta_ils)} Sell {_shares(g.shares)} {g.ticker} in {g.account} "
                f"({g.lots} lot(s) FIFO, {_ils(g.value_ils)}): an allowable loss of {_ils(g.loss_ils)} "
                f"(A: at least {_ils(g.floor_ils)}), tax value {_ils(g.tax_value_ils)} against "
                f"{c.trading_cost_ils * 5:,.2f} ILS, five times the trading cost (B), and C: {c.why_c}. "
                f"Buy {c.shares} {s.fund} with the money"
                f"{' (a domicile switch)' if c.switch else ''}. "
                f"What the loss is worth: {_ils(s.worth_now_ils)} this year ({_ils(s.against_gains_ils)} against this "
                f"year's gain); {_ils(s.against_dividends_ils)} against dividends, worth 0 when the US credit already "
                f"covers Israel's 25% ({_ils(s.credit_lost_ils)} of US credit lost); {_ils(s.carried_forward_ils)} "
                f"carried forward, worth up to 25% of itself against later gains. Net gain this year (D11): "
                f"{_ils(s.net_gain_this_year_ils)} after the loss carried in; gains less losses, the literal reading: "
                f"{_ils(s.gains_less_losses_ils)}.")
        others = [o for o in g.candidates if o.ticker != s.fund]
        if others:
            text += " Other funds: " + "; ".join(
                f"{o.ticker} ({o.shares} shares, cost {_ils(o.trading_cost_ils)}, "
                f"{'passes' if o.passes else 'fails test ' + o.failed})" for o in others) + "."
        for warning in s.warnings:
            text += f" Warning: {warning}."
        lines.append(f"- {text} {SUGGESTION_ONLY}")
    if result.not_flagged:
        lines += ["", "Looked at and not flagged:", ""]
        for g in result.not_flagged:
            if g.if_t5_rejected is not None:
                why = (f"a shekel loss of {_ils(-g.nominal_ils)} made only by the exchange rate: not allowable under "
                       f"T5 (accountant question 1 open); {g.if_t5_rejected}")
            elif g.net_ils >= 0:
                why = "no loss"
            elif not g.passes_a:
                why = f"A fails: a loss of {_ils(g.loss_ils)} is under {_ils(g.floor_ils)}"
            else:
                failed = "; ".join(f"{c.ticker} fails test {c.failed}" for c in g.candidates) or "no fund to suggest"
                why = f"A passes (a loss of {_ils(g.loss_ils)}) but {failed}"
            lines.append(f"- {g.ticker} in {g.account} ({g.lots} lot(s), {_ils(g.value_ils)}): {why}.")
    if result.unpriced:
        lines.append(f"\nNot tested, no price today: {', '.join(result.unpriced)}.")
    return lines + [""]


def _benchmark(books: list[BenchmarkBook], own: IfSold) -> list[str]:
    own_taxable = _ils(own.taxable_value_ils)
    lines = ["## 4. Against buy-and-hold VT and VWRA", "",
             "The same shekels on the same days, in whole shares after the same trading cost, after tax \"if sold "
             "today\". The tax-free accounts are the same in all three, so they are left out; the figures below are "
             f"the taxable accounts only (after tax if sold today: {own_taxable}).", "",
             "| Book | Market value | Tax if sold today | After tax | Money-weighted return a year | Difference from "
             "the owner's taxable accounts |", "| --- | ---: | ---: | ---: | ---: | ---: |"]
    for b in books:
        if not b.available:
            lines.append(f"| {b.ticker} | n/a | n/a | n/a | n/a | {b.reason} |")
            continue
        lines.append(f"| {b.ticker} | {_ils(b.market_ils)} | {_ils(b.tax_if_sold_ils)} | **{_ils(b.after_tax_ils)}** | "
                     f"{_pct(b.money_weighted)} | {_ils(b.after_tax_ils - own.taxable_value_ils)} |")
    lines.append("")
    lines.append("VT pays out: each dividend, less the US tax withheld, buys whole shares on its day. VWRA accumulates: "
                 "no Israeli tax until it is sold (accountant question 5).")
    return lines + [""]


def _pack(person: Person, years: list[int], payments) -> list[str]:
    lines = ["## 5. The annual report pack", ""]
    for year in years:
        summary = form_1322(person, year)
        lines += [f"### {year}", "", "Half-years (section 91: the first half's advance by 31 July, the second's by "
                  "31 January). Three readings of each advance until accountant questions 7 and 15 are answered: on "
                  "the gains alone, on the half's own net, and on the year's net so far less what the first half paid.",
                  "", "| Half | Proceeds | Gains | Losses | Net | Advance on the gains | On the half's net | "
                  "On the year's net | Recorded as paid |", "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
        for h in person.half_years(year, payments):
            paid = "" if h.paid_ils is None else _ils(h.paid_ils)
            lines.append(f"| {h.half} | {_ils(h.proceeds_ils)} | {_ils(h.gains_ils)} | {_ils(h.losses_ils)} | "
                         f"{_ils(h.net_ils)} | {_ils(h.on_gains)} | {_ils(h.on_net)} | {_ils(h.on_year)} | {paid} |")
        lines += ["", f"Form 1322, the year's summary: proceeds and gains {_ils(summary.gains)}, losses "
                  f"{_ils(summary.losses)}, net {_ils(summary.net_capital)}; loss carried in {_ils(summary.carry_in)}, "
                  f"of which {_ils(summary.carry_used)} used; loss set against dividends {_ils(summary.dividend_offset)} "
                  f"(the other way, for question 2: {_ils(0.0) if summary.dividend_offset == 0 else 'carried forward instead'}); "
                  f"taxable gain {_ils(summary.taxable_capital)}; capital gains tax {_ils(summary.capital_tax)}; "
                  f"extra dividend tax {_ils(summary.extra_dividend_tax)}; surtax {_ils(summary.surtax)}; "
                  f"loss carried out {_ils(summary.carry_out)}.", ""]
        rows = rows_1325(person, year)
        if rows:
            lines += ["Form 1325 rows, one per closed lot or part of one, FIFO:", "",
                      "| Account | Fund | ID | Quantity | Bought | Cost (ILS, at the purchase day's rate) | Rate ratio | "
                      "Adjusted cost | Sold | Proceeds (ILS) | Real gain or loss | Nominal | Inflationary amount | "
                      "Cost ($) | Proceeds ($) |",
                      "| --- | --- | --- | ---: | --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |"]
            for r in rows:
                lines.append(f"| {r.account} | {r.ticker} | {r.isin or 'n/a'} | {_shares(r.qty)} | "
                             f"{r.bought_on.isoformat() if r.bought_on else 'n/a'} | {_ils(r.cost_ils)} | "
                             f"{r.ratio:.6f} | {_ils(r.adjusted_cost_ils)} | {r.sold_on.isoformat()} | "
                             f"{_ils(r.proceeds_ils)} | {_ils(r.real_ils)} | {_ils(r.nominal_ils)} | "
                             f"{_ils(r.inflation_ils)} | {_usd(r.usd_cost or 0.0)} | {_usd(r.usd_proceeds or 0.0)} |")
            lines.append("")
        divs = dividend_rows(person, year)
        if divs:
            lines += ["Dividends (the foreign-income appendix, form 1324, question 9):", "",
                      "| Day | Account | Fund | Gross ($) | Rate | Gross (ILS) | US tax withheld (ILS, at its day's rate) | "
                      "Israel's 25% | Credit | Extra | Credit lost |",
                      "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
            for d in divs:
                lines.append(f"| {d.day.isoformat()} | {d.account} | {d.ticker} | {_usd(d.gross_usd)} | {d.fx:.4f} | "
                             f"{_ils(d.gross_ils)} | {_ils(d.us_withheld_ils)} | {_ils(d.israeli_tax_ils)} | "
                             f"{_ils(d.credit_ils)} | {_ils(d.extra_ils)} | {_ils(d.lost_ils)} |")
            lines.append("")
    lines.append("The exact fields of forms 1322 and 1325 are to be checked against the Tax Authority's current forms, "
                 "and the mapping goes to the accountant (question 13) before anything is filed from this pack.")
    return lines + [""]


def _assumed(inputs: Inputs, person: Person, day: date) -> list[str]:
    plan = inputs.plan
    offset_words = ("also set against that year's dividends" if person.rules.offset_losses_vs_dividends
                    else "carried forward, not set against dividends")
    if plan.surtax:
        surtax_words = "on, with the other taxable income entered" + (
            f" for {plan.other_income_year}" if plan.other_income_year else "")
    else:
        surtax_words = ("off (D20); turn it on in plan.csv with the year's other taxable income when that income "
                        "is near the 721,560 ILS line")
    lines = ["## 6. What is assumed", "",
             "- T5: a loss made only by the exchange rate is not allowable (accountant question 1, open); every line "
             "it touches says so.",
             f"- A year's net capital loss is {offset_words} (question 2).",
             "- FIFO lots, per account (question 3); a cheaper specific-lot sale is shown beside a line, not used.",
             "- The Bank of Israel's rate on the trade date; a weekend day takes the last weekday's rate (question 4).",
             "- An accumulating Irish fund (VWRA) is taxed only when sold (question 5).",
             "- Section 86: every harvest says \"do not act before question 6 is answered\" (D15).",
             "- Half-year advances: three readings until questions 7 and 15 are answered.",
             f"- The surtax: {surtax_words}.",
             f"- A W-8BEN is {'on file' if plan.w8ben.value else 'not on file'}"
             + (f" (answered {plan.w8ben.as_of.isoformat()})" if plan.w8ben.as_of else "") + ".",
             f"- Gains expected within 3 years: {'yes' if plan.expect_gains.value else 'no'}"
             + (f" (answered {plan.expect_gains.as_of.isoformat()})" if plan.expect_gains.as_of else "") + "."]
    for label, dated in (("the W-8BEN answer", plan.w8ben), ("the gains-within-3-years answer", plan.expect_gains)):
        if dated.as_of is not None and (day - dated.as_of).days > ANSWER_AGE_DAYS:
            lines.append(f"- Reminder: {label} is more than 12 months old ({dated.as_of.isoformat()}).")
    if plan.carry_in_year is not None:
        lines.append(f"- The loss carried in from the {plan.carry_in_year} assessment: {_ils(plan.carry_in)}.")
    lines.append("- The ISINs of the US-listed funds in the fund table are to be checked on the provider's page "
                 "before a filing; the three Irish funds' are the plan's.")
    return lines + [""]


def _estate_note(person: Person, closes, fx: float) -> list[str]:
    total = 0.0
    for position in person.positions():
        known = fund(position.ticker)
        price = closes.get(position.ticker)
        if known is not None and known.domicile == US and price:
            total += position.qty * price
    if total <= 0:
        return []
    return [f"Note, not a rule: US-listed holdings of {_usd(total)} against the ${US_ESTATE_TAX_LINE_USD:,.0f} line "
            "above which the US estate tax applies to a non-US person (Israel has no estate-tax treaty with the US); "
            "a domicile switch lowers that amount.", ""]


# --------------------------------------------------------------------------- #
# The run
# --------------------------------------------------------------------------- #


def build(inputs: Inputs, market: Market, day: Optional[date] = None, costs: CostTable = DEFAULT_COSTS) -> str:
    """The report's text for one run."""
    day = day or market.as_of
    person = Person(inputs.accounts, inputs.plan, market.rate)
    person.apply(inputs.transactions)
    person.set_tracks(inputs.tracks, day)
    fx = person.fx(day)
    wanted = {p.ticker for p in person.positions()} | set(BY_TICKER) | set(inputs.plan.classes) | set(inputs.plan.buy_first.values())
    closes = {ticker: price for ticker in wanted if (price := market.close(ticker)) is not None and price > 0}
    state = person.if_sold(day, closes, fx, inputs.payments, costs)
    harvested = harvest(person, closes, fx, day, inputs.plan.classes, inputs.plan.expect_gains, costs,
                        transactions=inputs.transactions)
    plan_result = rebalance(person, inputs.plan, closes, fx, day, costs, avoid=harvested.sold, prefer=harvested.bought)
    books = benchmark(person.flows, market, person.fx, day, closes, fx, costs, person.rules)
    years = sorted(set(person.years()) | {day.year})
    text = [f"# The investor simulator: {day.isoformat()}", "",
            "Written by `python -m investor.report`, sample data" if inputs.marker == "SAMPLE" else
            "Written by `python -m investor.report`", "",
            "Every line that proposes a trade starts with its tax cost and ends with "
            f"\"{SUGGESTION_ONLY}\" Nothing here trades.", ""]
    text += _summary(day, fx, state, person, market)
    text += _allocation(plan_result)
    text += _harvest(harvested)
    text += _benchmark(books, state)
    text += _pack(person, years, inputs.payments)
    text += _assumed(inputs, person, day)
    text += _estate_note(person, closes, fx)
    return "\n".join(text).rstrip() + "\n"


def run(data: Path, out: Path, market: Market, day: Optional[date] = None, costs: CostTable = DEFAULT_COSTS) -> Path:
    """Read the folder, write the report; returns the dated file's path."""
    data, out = Path(data), Path(out)
    if inside_repository(out):
        raise DataError(out.name, None, "the report folder is inside the repository; real numbers never live here")
    inputs = read_folder(data)
    text = build(inputs, market, day, costs)
    out.mkdir(parents=True, exist_ok=True)
    stamp = (day or market.as_of).isoformat()
    (out / "latest.md").write_text(text, encoding="utf-8")
    dated = out / f"{stamp}.md"
    dated.write_text(text, encoding="utf-8")
    return dated


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="investor.report", description="Write the investor report from a private folder.")
    parser.add_argument("--data", type=Path, required=True, help="the folder with the owner's CSV files")
    parser.add_argument("--out", type=Path, required=True, help="the folder the report is written to")
    parser.add_argument("--as-of", type=date.fromisoformat, default=None, help="price as of this day (default: the last close)")
    parser.add_argument("--start", type=date.fromisoformat, default=None, help="fetch prices from this day (default: the fixed start)")
    return parser


def main(argv: Optional[Sequence[str]] = None, market_factory=None) -> int:
    """The command line. ``market_factory(extra_tickers, start, as_of)`` is the fetch; the tests pass a fake."""
    from investor.market import FIXED_START, fetch_market, quiet

    quiet()
    args = build_parser().parse_args(argv)
    try:
        if inside_repository(args.data) or inside_repository(args.out):
            raise DataError("a folder", None, "the data and report folders must be outside the repository")
        inputs = read_folder(args.data)
        extra = tuple(sorted(set(inputs.plan.classes) | set(inputs.plan.buy_first.values())
                             | {t.ticker for t in inputs.transactions if t.ticker}))
        factory = market_factory or (lambda tickers, start, as_of: fetch_market(tickers, start=start, as_of=as_of))
        market = factory(extra, args.start or FIXED_START, args.as_of)
        written = run(args.data, args.out, market, args.as_of)
    except DataError as exc:
        print(f"refused: {exc}", file=sys.stderr)
        return 2
    except (MarketError, PlanError) as exc:
        print(f"failed: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # noqa: BLE001 - its text could carry a value; its kind cannot
        print(f"failed: {type(exc).__name__}", file=sys.stderr)
        return 1
    print(f"report written: {len(written.read_text(encoding='utf-8').splitlines())} lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["ANSWER_AGE_DAYS", "SUGGESTION_ONLY", "build", "build_parser", "main", "run"]
