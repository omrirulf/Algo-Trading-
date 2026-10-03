"""The paper account and the funds after Israeli tax, and in shekels.

Two things the owner asked for on 2 Oct 2026, read from books this package
already has, with the rules of ``config.israel_tax`` (never a flat 25%):

* **The after-tax gate's test** (pre-registration section 5c): each main
  fund minus the VT fund on daily after-tax returns, "if sold today", with
  the fund test's own Newey-West t (lag 5). Made once, on the first night
  from the night the race reaches a look on which the look is readable, the
  rate table is there and the funds' prices reach the look's last close,
  over the fund sessions up to that close, and kept unchanged (made again
  only if a bug fix moves the look's window); the race reads it back
  (``analysis.horse_race.after_tax_records``).
* **The after-tax and shekel views** (section 11.9): for the real paper
  account, the four funds and, at checkpoints only, the exploratory funds --
  before and after tax side by side, "tax paid so far" and "if sold today",
  the same results in shekels at the Bank of Israel's rate, and how much of
  the shekel result came from the dollar's move against the shekel.

How each book becomes a list of taxable events (``analysis.israel_tax.Event``):

* a fund run by the engine: its ``SimBroker`` fills, in order -- an entry,
  a ladder rung, a trim or a stop is a purchase or a sale at the fill price,
  its cost the fee; a dividend credited to a long is a dividend, one charged
  to a short is a charge;
* the VT fund: one purchase at its first open (the fee in), then each
  dividend on the ex-date for the shares held (``IndexFund``);
* B (VT or T-bills): the legs it recorded (``TimingFund.trades``), and the
  dividends of whatever it held at the open;
* the paper account: its own fills from ``logs/account.jsonl``, once each
  (``shadow.calibration``), at the price Alpaca filled them; no fee, as the
  paper account charges none. Alpaca's record has no dividends, so none are
  taxed here; the account's own equity is what it reports.

Read-only, like everything in shadow/: books and tables in, numbers out.
"""

from __future__ import annotations

import statistics
from collections import defaultdict
from datetime import date
from typing import Callable, Iterable, Mapping, Optional, Sequence

from analysis import decision_gate as gate
from analysis.israel_tax import (
    BUY,
    CHARGE,
    DEFAULT_RULES,
    DIVIDEND,
    SELL,
    AfterTaxSeries,
    Event,
    TaxBook,
    TaxRules,
    after_tax_series,
)
from shadow.broker import DIVIDEND as FILL_DIVIDEND
from shadow.fund import STARTING_CASH, IndexFund
from shadow.market import Bars

#: The rate table starts on the paper account's first funded day (its equity
#: history reads $100,000 from 2026-09-10), so every book here can be priced.
FX_TABLE_START = date(2026, 9, 10)

#: The main funds the after-tax gate pairs with the VT fund (section 5c).
GATE_FUNDS = ("model", "momentum", "hybrid")
VT_FUND = "vt"


# --------------------------------------------------------------------------- #
# Books as taxable events
# --------------------------------------------------------------------------- #


def fund_events(fund) -> dict[date, list[Event]]:
    """Every taxable event of one simulated fund, by day, in the order it happened."""
    out: dict[date, list[Event]] = defaultdict(list)
    if isinstance(fund, IndexFund):
        if fund.bought is None or not fund.qty:
            return {}
        opened = fund.bars.bar(fund.ticker, fund.bought)[0]
        out[fund.bought].append(Event(BUY, fund.ticker, fund.qty, opened, fund.qty * opened * fund.cost_per_side))
        for record in fund.days:
            bar = fund.bars.bar(fund.ticker, record.day)
            if record.day > fund.bought and bar is not None and bar[4]:
                out[record.day].append(Event(DIVIDEND, fund.ticker, fund.qty, bar[4]))
        return dict(out)
    trades = getattr(fund, "trades", None)
    if trades is not None and not hasattr(fund, "broker"):     # B: its own legs and its holdings' dividends
        for day, ticker, side, qty, price, cost in trades:
            out[day].append(Event(BUY if side == "buy" else SELL, ticker, qty, price, cost))
        for day, ticker, qty, per_share in getattr(fund, "dividends", ()):
            out[day].append(Event(DIVIDEND, ticker, qty, per_share))
        return {day: _ordered(events) for day, events in out.items()}
    for fill in fund.broker.fills:
        if fill.kind == FILL_DIVIDEND:
            out[fill.day].append(Event(DIVIDEND if fill.side == "buy" else CHARGE, fill.ticker, fill.qty, fill.price))
        else:
            out[fill.day].append(Event(BUY if fill.side == "buy" else SELL, fill.ticker, fill.qty, fill.price,
                                       fill.cost))
    return dict(out)


def _ordered(events: list[Event]) -> list[Event]:
    """B's day: a dividend on what was held at the open comes before that open's sale and purchase."""
    return [e for e in events if e.kind == DIVIDEND] + [e for e in events if e.kind != DIVIDEND]


def account_events(fills: Iterable) -> dict[date, list[Event]]:
    """The paper account's fills (``shadow.calibration.AccountFill``), by New York day, oldest first."""
    out: dict[date, list[Event]] = defaultdict(list)
    for fill in sorted(fills, key=lambda f: f.at):
        kind = BUY if fill.side == "buy" else SELL           # "sell" closes a long, "sell_short" opens a short
        out[fill.day].append(Event(kind, fill.ticker, float(fill.qty), float(fill.price)))
    return dict(out)


class _DayCloses(Mapping):
    """One day's closes, looked up only for the tickers a book asks about."""

    def __init__(self, bars: Bars, day: date) -> None:
        self._bars, self._day, self._seen = bars, day, {}

    def __getitem__(self, ticker: str) -> float:
        if ticker not in self._seen:
            bar = self._bars.bar(ticker, self._day)
            self._seen[ticker] = bar[3] if bar is not None else self._bars.last_close_before(ticker, self._day)
        price = self._seen[ticker]
        if price is None:
            raise KeyError(ticker)
        return price

    def __iter__(self):
        return iter(self._bars.tickers())

    def __len__(self) -> int:
        return len(self._bars.tickers())


def closes_from(bars: Bars) -> Callable[[date], Mapping[str, float]]:
    """Each day's close per ticker, or the last close before it (a day with no bar): what a book is marked at."""
    return lambda day: _DayCloses(bars, day)


# --------------------------------------------------------------------------- #
# Series
# --------------------------------------------------------------------------- #


def fund_series(fund, bars: Bars, rate: Callable[[date], float],
                rules: TaxRules = DEFAULT_RULES) -> Optional[AfterTaxSeries]:
    """One fund after tax, day by day, from its own start; None before its first session."""
    if not fund.days:
        return None
    days = [d.day for d in fund.days]
    return after_tax_series(days, [d.equity for d in fund.days], fund_events(fund), closes_from(bars),
                            {d: rate(d) for d in days}, start_equity_usd=STARTING_CASH, start_fx=rate(days[0]),
                            rules=rules)


def account_series(snapshots, bars: Bars, rate: Callable[[date], float], through: date,
                   rules: TaxRules = DEFAULT_RULES) -> Optional[AfterTaxSeries]:
    """The paper account after tax, from its first funded close to ``through``."""
    from shadow.calibration import _all_fills, real_closes

    equity = {d: e for d, e in real_closes(snapshots).items() if e and e > 0 and FX_TABLE_START <= d <= through}
    if not equity:
        return None
    days = sorted(equity)
    first = days[0]
    return after_tax_series(days, [equity[d] for d in days], account_events(_all_fills(snapshots)),
                            closes_from(bars), {d: rate(d) for d in days}, start_equity_usd=equity[first],
                            start_fx=rate(first), rules=rules)


def account_lot_check(snapshots, rules: TaxRules = DEFAULT_RULES) -> dict:
    """Whether the lots rebuilt from the fills hold what the latest snapshot says the account holds."""
    from shadow.calibration import _all_fills

    book = TaxBook(rules)
    for day, events in sorted(account_events(_all_fills(snapshots)).items()):
        for e in events:
            book.apply(day, e.kind, e.ticker, e.qty, e.price_usd, 1.0, e.fee_usd)
    latest = next((s for s in reversed(snapshots) if s.positions is not None), None)
    if latest is None:
        return {"checked": False, "mismatches": []}
    held = {p.ticker: p.qty for p in latest.positions}
    tickers = set(held) | {lot.ticker for lot in book.open_lots()}
    mismatches = sorted(t for t in tickers if abs(book.open_quantity(t) - held.get(t, 0.0)) > 1e-6)
    return {"checked": True, "at": latest.at.isoformat(), "mismatches": mismatches}


# --------------------------------------------------------------------------- #
# What is shown
# --------------------------------------------------------------------------- #


def view(series: Optional[AfterTaxSeries]) -> Optional[dict]:
    """Before and after tax side by side, in dollars and in shekels, and the dollar's part of the shekel result.

    Returns since the series' start. "after_tax" is "if sold today" (equity
    minus the tax due if every position were sold at the close); "paid_so_far"
    is equity minus the tax due on what was sold or received so far.
    "from_usd_ils" is the shekel return minus the dollar return: what the
    dollar's move against the shekel added (or took away) for someone counting
    in shekels; "after_tax_from_usd_ils" is the same on the "if sold today"
    returns.
    """
    if series is None or not series.days:
        return None
    last = series.days[-1]
    start_usd = series.start_equity_usd
    start_ils = start_usd * (series.start_fx or last.fx)

    def change(now: float, then: float) -> Optional[float]:
        return now / then - 1.0 if then else None

    usd, usd_after = change(last.equity_usd, start_usd), change(last.after_tax_usd, start_usd)
    ils, ils_after = change(last.equity_ils, start_ils), change(last.after_tax_ils, start_ils)
    paid_usd = last.realised_tax_usd if last.realised_tax_usd is not None else last.realised_tax_ils / last.fx
    usd_paid, ils_paid = last.equity_usd - paid_usd, last.equity_ils - last.realised_tax_ils
    return {
        "from": series.days[0].day.isoformat(),
        "through": last.day.isoformat(),
        "days": len(series.days),
        "usd": {"start": round(start_usd, 2), "equity": round(last.equity_usd, 2),
                "after_tax": round(last.after_tax_usd, 2), "return": usd, "after_tax_return": usd_after,
                "paid_so_far": round(usd_paid, 2), "paid_so_far_return": change(usd_paid, start_usd)},
        "ils": {"start": round(start_ils, 2), "equity": round(last.equity_ils, 2),
                "after_tax": round(last.after_tax_ils, 2), "return": ils, "after_tax_return": ils_after,
                "paid_so_far": round(ils_paid, 2), "paid_so_far_return": change(ils_paid, start_ils),
                "from_usd_ils": None if ils is None or usd is None else ils - usd,
                "after_tax_from_usd_ils": None if ils_after is None or usd_after is None else ils_after - usd_after},
        "tax_ils": {"paid_so_far": round(last.realised_tax_ils, 2), "if_sold_today": round(last.if_sold_tax_ils, 2)},
        "usd_ils": {"start": series.start_fx, "end": last.fx,
                    "change": change(last.fx, series.start_fx) if series.start_fx else None},
        "unpriced": list(last.unpriced),
    }


def paired(fund: AfterTaxSeries, other: AfterTaxSeries, through: Optional[date] = None,
           lag: int = gate.AFTER_TAX_LAG) -> dict:
    """Section 5c's test: daily after-tax returns, fund minus ``other``, Newey-West t, paired by date."""
    from analysis.horse_race import newey_west_t
    from analysis.multiple_tests import p_two_sided, series_stats

    mine, theirs = fund.returns(), other.returns()
    days = sorted(d for d in set(mine) & set(theirs) if through is None or d <= through)
    diffs = [mine[d] - theirs[d] for d in days]
    t = newey_west_t(diffs, lag)
    return {"days": len(diffs), "from": days[0].isoformat() if days else None,
            "through": days[-1].isoformat() if days else None,
            "mean_daily_diff": statistics.fmean(diffs) if diffs else None, "t": t, "p": p_two_sided(t),
            "stats": series_stats(diffs), "lag": lag}


def rules_json(rules: TaxRules = DEFAULT_RULES) -> dict:
    """The parameters a record was made with, so a record says what it assumed."""
    return {"capital_rate": rules.capital_rate, "dividend_rate": rules.dividend_rate, "w8ben": rules.w8ben,
            "us_withholding": rules.us_withholding, "offset_losses_vs_dividends": rules.offset_losses_vs_dividends,
            "surtax_enabled": rules.surtax_enabled}


def gate_record(look: int, made_on: date, window_end: Optional[date],
                series: Optional[Mapping[str, Optional[AfterTaxSeries]]], reason: str = "",
                rules: TaxRules = DEFAULT_RULES) -> dict:
    """One look's after-tax test (section 5c): each main fund against the VT fund, up to ``window_end``.

    ``series`` None means no fund could be run that night (``reason`` says
    why): the record says so, and no arm can pass the test at that look.
    """
    base = {"look": look, "made_on": made_on.isoformat(),
            "window_end": window_end.isoformat() if window_end else None, "lag": gate.AFTER_TAX_LAG,
            "rules": rules_json(rules)}
    vt = (series or {}).get(VT_FUND)
    if series is None or vt is None:
        return base | {"status": gate.AFTER_TAX_UNAVAILABLE, "reason": reason or "no fund was run", "tests": {}}
    tests = {name: paired(series[name], vt, window_end) for name in GATE_FUNDS if series.get(name) is not None}
    return base | {"status": gate.AFTER_TAX_READY, "reason": "", "tests": tests}


# --------------------------------------------------------------------------- #
# logs/after_tax.md
# --------------------------------------------------------------------------- #


def _money(value, sign: str) -> str:
    if not isinstance(value, (int, float)):
        return "n/a"
    return ("−" if value < 0 else "") + sign + f"{abs(value):,.0f}"


def _pct(value) -> str:
    if not isinstance(value, (int, float)):
        return "n/a"
    return ("+" if value > 0 else "−" if value < 0 else "") + f"{abs(value) * 100:.2f}%"


def _points(value) -> str:
    if not isinstance(value, (int, float)):
        return "n/a"
    return ("+" if value > 0 else "−" if value < 0 else "") + f"{abs(value) * 100:.2f} points"


def _view_rows(label: str, v: Optional[dict]) -> list[str]:
    if not isinstance(v, dict):
        return []
    usd, ils, tax = v.get("usd") or {}, v.get("ils") or {}, v.get("tax_ils") or {}
    return [f"| {label} | {_money(usd.get('equity'), '$')} ({_pct(usd.get('return'))}) "
            f"| {_money(usd.get('after_tax'), '$')} ({_pct(usd.get('after_tax_return'))}) "
            f"| {_money(usd.get('paid_so_far'), '$')} ({_pct(usd.get('paid_so_far_return'))}) "
            f"| {_money(ils.get('equity'), '₪')} ({_pct(ils.get('return'))}) "
            f"| {_money(ils.get('after_tax'), '₪')} ({_pct(ils.get('after_tax_return'))}) "
            f"| {_money(ils.get('paid_so_far'), '₪')} ({_pct(ils.get('paid_so_far_return'))}) "
            f"| {_points(ils.get('from_usd_ils'))} | {_points(ils.get('after_tax_from_usd_ils'))} "
            f"| {_money(tax.get('paid_so_far'), '₪')} | {_money(tax.get('if_sold_today'), '₪')} |"]


def render(document: dict) -> str:
    """The after-tax part of a funds document as a short report, in plain words."""
    part = document.get("after_tax") if isinstance(document, dict) else None
    lines = ["# After Israeli tax and in shekels", ""]
    if not isinstance(part, dict):
        return "\n".join(lines + ["No after-tax part in this record.", ""])
    rules, fx = part.get("rules") or {}, part.get("fx") or {}
    lines += [f"Record through {document.get('final_through', 'n/a')}, written {document.get('generated_at', 'n/a')}. "
              "Rules: pre-registration section 5c, every number in `config/israel_tax.py` "
              f"(tax {rules.get('capital_rate', 0.25):.0%}; losses also against dividends: "
              f"{'on' if rules.get('offset_losses_vs_dividends') else 'off'}; "
              f"W-8BEN: {'yes' if rules.get('w8ben') else 'no'}; surtax: {'on' if rules.get('surtax_enabled') else 'off'}).", ""]
    if fx.get("available"):
        counts = fx.get("counts") or {}
        other = (counts.get("ecb") or 0) + (counts.get("carried") or 0)
        days = ", ".join(f"{d} ({src})" for d, src in fx.get("fallback_days") or []) or "none"
        lines += [f"Rates: the Bank of Israel's representative rate, {fx.get('first')} to {fx.get('last')}; "
                  f"{counts.get('boi') or 0} day(s) from the Bank of Israel, "
                  f"{other} day(s) from another source: {days}. Table SHA-256 `{fx.get('rates_sha256')}`.", ""]
    else:
        lines += [f"No rate table tonight ({fx.get('reason', 'unknown')}): nothing is shown rather than a guessed rate.", ""]
    head = ["| | Before tax ($) | After tax, if sold today ($) | After tax, tax paid so far ($) | Before tax (₪) "
            "| After tax, if sold today (₪) | After tax, tax paid so far (₪) | From the $/₪ move, before tax "
            "| From the $/₪ move, after tax | Tax paid so far (₪) | Tax if sold today (₪) |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    paper = _view_rows("Paper account (real)", part.get("paper"))
    funds = part.get("funds")
    fund_rows = [r for name, label in (("model", "Model fund"), ("momentum", "Momentum fund"),
                                        ("hybrid", "Hybrid fund"), ("vt", "VT fund"))
                 for r in _view_rows(label, (funds or {}).get(name))]
    if paper or fund_rows:
        lines += ["Returns since each book's start. \"Tax paid so far\" is the tax due on everything sold or "
                  "received so far; \"if sold today\" adds every open position sold at the close. \"From the $/₪ "
                  "move\" is the shekel return minus the dollar return, before tax and after tax (if sold today).",
                  ""] + head + paper + fund_rows + [""]
    if part.get("paper_problem"):
        lines += [f"The paper account: {part['paper_problem']}.", ""]
    lots = part.get("paper_lots") or {}
    if lots.get("mismatches"):
        lines += [f"Check: the lots rebuilt from the paper account's fills differ from its positions for "
                  f"{', '.join(lots['mismatches'])}.", ""]
    if not funds and (document.get("calibration") or {}).get("status") != "passed":
        lines += ["The funds are shown after tax once calibration has passed, like every fund result.", ""]
    looks = [r for r in part.get("looks") or [] if isinstance(r, dict)]
    lines += ["## The after-tax gate (section 5c)", ""]
    if not looks:
        lines += ["No look reached yet. Each look's test is made once, on the first night from the night the race reaches "
                  "it on which the look is readable, the rate table is there and the funds' prices reach the look's "
                  "last close.", ""]
    for r in looks:
        if r.get("status") == gate.AFTER_TAX_READY:
            tests = r.get("tests") or {}
            shown = "; ".join(f"{name} t = {tests[name]['t']:.2f}" if isinstance(tests.get(name, {}).get("t"), (int, float))
                              else f"{name} t = n/a" for name in GATE_FUNDS if name in tests)
            lines.append(f"- Look {r.get('look')} (made {r.get('made_on')}, through {r.get('window_end')}): {shown}.")
        else:
            lines.append(f"- Look {r.get('look')} (made {r.get('made_on')}): not available: {r.get('reason')}.")
    be = part.get("breakeven") or {}
    if isinstance(be.get("extra_per_year"), (int, float)):
        lines += ["", "## For information only (not a gate)", "",
                  f"An actively traded fund needs about {be['extra_per_year'] * 100:.2f} points a year more before tax "
                  f"to tie with VT held {be.get('years')} years ({be.get('growth', 0):.0%} growth, "
                  f"{be.get('dividend_yield', 0):.0%} dividend yield). `python -m analysis.tax_breakeven --table`."]
    return "\n".join(lines) + "\n"


def main(argv: Optional[Sequence[str]] = None) -> int:
    """``python -m shadow.after_tax FUNDS_JSON``: print the report; the workflow redirects it."""
    import json
    import sys
    from pathlib import Path

    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print("usage: python -m shadow.after_tax FUNDS_JSON", file=sys.stderr)
        return 2
    try:
        document = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"cannot read {args[0]}: {exc}", file=sys.stderr)
        return 1
    print(render(document), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["FX_TABLE_START", "GATE_FUNDS", "VT_FUND", "account_events", "account_lot_check", "account_series",
           "closes_from", "fund_events", "fund_series", "gate_record", "main", "paired", "render", "rules_json",
           "view"]
