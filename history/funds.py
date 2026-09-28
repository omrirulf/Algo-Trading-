"""The funds on history: momentum, A and C through the production engine; B, VT and SPY beside them.

The funds of pre-registration sections 11 and 13, run on the history
journal the way ``shadow.run.run_funds`` runs them on the live one: one
``shadow.fund.run`` over every session, one feed clock, $100,000 each, 0.10%
a side on every fill, dividends on the ex-date, watchlist order.

* ``momentum``, ``momentum_200`` (A) and ``momentum_pullback`` (C): the
  production ``ExecutionEngine`` and ``PositionManager`` on a ``SimBroker``,
  signals from each line's technicals (``shadow.fund.rule_signal``,
  ``shadow.exploratory.veto_signal``, ``shadow.exploratory.PullbackFund``);
* ``vt``: VT bought at its first open and held (``shadow.fund.IndexFund``).
  VT's history starts in June 2008, so every comparison with it starts
  there; before that it holds its cash;
* ``spy``: SPY bought and held the same way, from the first session -- not a
  registered fund, a longer yardstick for the years before VT;
* ``vt_timing`` (B): ``shadow.exploratory.TimingFund``, unchanged, from the
  first month-end VT has ten month-end closes for (March 2009) instead of
  the registered 2026-09-30 -- the only setting moved, since the rule cannot
  start before VT existed;
* ``vt_timing_on_spy``: B's code with SPY in place of VT, from the first
  month-end BIL (its T-bills) existed (May 2007). Not the registered rule:
  the owner's own quick test ran the 10-month average on SPY, and this is
  the same test through the real code, for comparing the two.

What history changes, and the report says: no name is held by a real
account, so no line is skipped for it (live, the names the paper account
holds are out of every fund's reach); the paper account's short refusals are
dated 2026, after every history session, so none applies; the lines' "model
answer" is the stand-in of ``history.journal.as_answered``, which no rule
reads.
"""

from __future__ import annotations

import statistics
from contextlib import contextmanager
from datetime import date
from pathlib import Path
from typing import Iterator, Mapping, Optional, Sequence

import numpy as np
import pandas as pd

from history import journal
from history.periods import (
    ALL, BEFORE_2010, FROM_2010, Period, annualised, max_drawdown, periods_for, test_of,
)
from history.prices import BILLS_TICKER, CALENDAR_TICKER, INDEX_TICKER
from history.sessions import historical_calendar
from shadow import exploratory as xp
from shadow import fund as sim
from shadow.broker import ENTRY
from shadow.fund import STARTING_CASH, Fund, IndexFund, cycle_days, lines_by_day, rule_signal
from shadow.market import Bars, SimFeed, calendar
from shadow.order_matters import fund_summary
from shadow.run import VS_MODEL_LAG, integrity, sides

B_ON_SPY = "vt_timing_on_spy"
SPY_FUND = "spy"


@contextmanager
def timing(first_month_end: date, ticker_in: str = xp.TIMING_IN) -> Iterator[None]:
    """B's code with its first month-end (and, for the SPY check, its "in" fund) moved; restored after.

    ``TimingFund`` and ``timing_counters`` read ``timing_signals`` and
    ``TIMING_IN`` from their module when they run, so both are replaced in
    ``shadow.exploratory`` for the block and put back after it.
    """
    signals, held_in = xp.timing_signals, xp.TIMING_IN

    def from_first(bars, through, first=first_month_end):
        return signals(bars, through, first)

    xp.timing_signals, xp.TIMING_IN = from_first, ticker_in
    try:
        yield
    finally:
        xp.timing_signals, xp.TIMING_IN = signals, held_in


def month_end_of(day: date) -> date:
    """The last session of ``day``'s month (``shadow.exploratory.last_trading_day``, on the history calendar)."""
    return xp.last_trading_day(day.year, day.month)


# --------------------------------------------------------------------------- #
# Reading a fund over a period
# --------------------------------------------------------------------------- #


def returns_by_day(fund) -> dict[date, float]:
    """Close-to-close returns on the equity to the cent (``shadow.run.paired``'s own rule)."""
    equity = [STARTING_CASH] + [round(d.equity, 2) for d in fund.days]
    return {d.day: today / before - 1.0 for d, before, today in zip(fund.days, equity, equity[1:])}


def slice_of(fund, period: Period, since: Optional[date] = None) -> dict:
    """Total return, yearly rate and maximum drawdown of ``fund`` over the sessions of ``period`` (from ``since``)."""
    days = [d for d in fund.days if period.contains(d.day) and (since is None or d.day >= since)]
    if not days:
        return {"sessions": 0}
    first = fund.days.index(days[0])
    base = fund.days[first - 1].equity if first > 0 else STARTING_CASH
    total = days[-1].equity / base - 1.0
    invested = [d.gross / d.equity for d in days if d.equity > 0]
    return {"from": days[0].day.isoformat(), "to": days[-1].day.isoformat(), "sessions": len(days),
            "total_return": total, "annualised": annualised(total, len(days)),
            "max_drawdown": max_drawdown([base] + [d.equity for d in days]),
            "mean_invested": statistics.fmean(invested) if invested else None,
            "mean_positions": statistics.fmean(d.positions for d in days)}


def paired(fund, other, period: Period, since: Optional[date] = None) -> dict:
    """``fund`` against ``other`` day by day (section 13's fund test): mean difference, Newey-West t at lag 5."""
    mine, theirs = returns_by_day(fund), returns_by_day(other)
    days = sorted(d for d in set(mine) & set(theirs) if period.contains(d) and (since is None or d >= since))
    out = test_of([mine[d] - theirs[d] for d in days], VS_MODEL_LAG)
    if not days:
        return out
    out["from"], out["to"] = days[0].isoformat(), days[-1].isoformat()
    out["fund"] = slice_of(fund, period, days[0])
    out["compared"] = slice_of(other, period, days[0])
    return out


def trades_of(fund, period: Period) -> dict:
    """Entries made, and the closed trades opened in ``period``: longs and shorts (``shadow.run.sides``).

    Also, for reading the fund's result: how long a position was held (weekdays from its entry to its
    last share), what the 0.10%-a-side cost took from the book per year (each fill's cost over that
    day's equity, summed, per 252 sessions), and how many entries were under $1 (split-adjusted prices,
    where the engine's cent-rounded stops are coarse).
    """
    closed = [c for c in fund.broker.closed if period.contains(c.opened)]
    equity = {d.day: d.equity for d in fund.days}
    fills = [f for f in fund.broker.fills if period.contains(f.day)]
    sessions = sum(1 for d in fund.days if period.contains(d.day))
    held = [int(np.busday_count(c.opened, c.closed)) for c in closed]
    cost_share = sum(f.cost / equity[f.day] for f in fills if equity.get(f.day))
    return {
        "entries": sum(1 for f in fills if f.kind == ENTRY),
        "closed": len(closed),
        "win_rate": (sum(1 for c in closed if c.pnl > 0) / len(closed)) if closed else None,
        "sides": sides(closed),
        "mean_days_held": statistics.fmean(held) if held else None,
        "median_days_held": statistics.median(held) if held else None,
        "costs_per_year": cost_share * 252.0 / sessions if sessions else None,
        "entries_under_1_dollar": sum(1 for f in fills if f.kind == ENTRY and f.price < 1.0),
    }


def _cycles_in(cycles: Mapping[date, list], period: Period) -> dict[date, list]:
    return {day: lines for day, lines in cycles.items() if period.contains(day)}


# --------------------------------------------------------------------------- #
# The run
# --------------------------------------------------------------------------- #


def run_funds(journal_dir: Path, frames: Mapping[str, pd.DataFrame], sessions: Sequence[date],
              final_through: date) -> dict:
    """Every fund over every session of the history journal, and every number the report reads of them."""
    bars = Bars(dict(frames))
    with historical_calendar(sessions):
        entries = journal.as_answered(journal.read(journal_dir))
        cycles = lines_by_day(entries)
        ran = cycle_days(entries)
        del entries
        tickers = {line.ticker for lines in cycles.values() for line in lines} | {INDEX_TICKER}
        first_cycle = min(cycles)
        start = next(d for d in sorted(sessions) if d > first_cycle)
        days = calendar(bars, (INDEX_TICKER, CALENDAR_TICKER, *sorted(tickers)), start, final_through)
        feed = SimFeed(bars)
        vt_first = month_end_of(frames[INDEX_TICKER].index[0].date())
        with timing(vt_first):
            funds = [
                Fund("momentum", rule_signal("momentum"), feed, bars),
                Fund(xp.VETO, xp.veto_signal(bars), feed, bars),
                xp.PullbackFund(xp.LIMIT, feed, bars),
                IndexFund("vt", INDEX_TICKER, bars),
                IndexFund(SPY_FUND, CALENDAR_TICKER, bars),
                xp.TimingFund(xp.TIMING, bars, final_through),
            ]
            sim.run(funds, days, cycles, ran, feed, first_cycle)
            b_counters = xp.timing_counters(bars, final_through)
        bil_first = month_end_of(frames[BILLS_TICKER].index[0].date())
        with timing(bil_first, CALENDAR_TICKER):
            b_spy = xp.TimingFund(B_ON_SPY, bars, final_through)
            sim.run([b_spy], days, {}, set(), feed, None)
            b_spy_counters = xp.timing_counters(bars, final_through)
        by_name = {f.name: f for f in funds}
        counters = {
            xp.VETO: {p.name: xp.veto_counters(_cycles_in(cycles, p), bars, first_cycle)
                      for p in periods_for(xp.VETO, first_cycle)},
            xp.LIMIT: {p.name: xp.pullback_counters(_cycles_in(cycles, p), bars, first_cycle, final_through)
                       for p in periods_for(xp.LIMIT, first_cycle)},
            xp.TIMING: b_counters | {"first_month_end": vt_first.isoformat()},
            B_ON_SPY: b_spy_counters | {"first_month_end": bil_first.isoformat()},
        }
        results = summarise(by_name, b_spy, counters, first_cycle)
    results["sessions"] = {"first": days[0].isoformat(), "last": days[-1].isoformat(), "count": len(days),
                           "first_cycle": first_cycle.isoformat()}
    results["integrity"] = integrity([*funds, b_spy])
    return results


def summarise(by_name: Mapping[str, object], b_spy, counters: dict, first_cycle: date) -> dict:
    vt, spy = by_name["vt"], by_name[SPY_FUND]
    vt_from = vt.bought
    out: dict = {"funds": {}, "counters": counters,
                 "vt_first_session": vt_from.isoformat() if vt_from else None}
    for name in ("momentum", xp.VETO, xp.LIMIT):
        fund = by_name[name]
        rows = {}
        for period in periods_for(name, first_cycle):
            row = {"fund": slice_of(fund, period), "trades": trades_of(fund, period),
                   "vs_vt": paired(fund, vt, period, vt_from), "vs_spy": paired(fund, spy, period)}
            if name != "momentum":
                row["vs_momentum"] = paired(fund, by_name["momentum"], period)
            rows[period.name] = row
        # C enters by limit order outside the fund's own dispatch, so the order report has nothing of it.
        out["funds"][name] = {"periods": rows, "order_matters": _order_counts(fund) if name != xp.LIMIT else None}
    b = by_name[xp.TIMING]
    b_first = b.days[0].day if b.days else None
    out["funds"][xp.TIMING] = {"periods": {
        p.name: {"fund": slice_of(b, p), "vs_vt": paired(b, vt, p, b_first)}
        for p in (ALL, BEFORE_2010, FROM_2010)}, "switches": b.switches, "waited": b.waited}
    spy_first = b_spy.days[0].day if b_spy.days else None
    out["funds"][B_ON_SPY] = {"periods": {
        p.name: {"fund": slice_of(b_spy, p), "vs_spy": paired(b_spy, spy, p, spy_first)}
        for p in (ALL, BEFORE_2010, FROM_2010)}, "switches": b_spy.switches, "waited": b_spy.waited}
    out["funds"]["vt"] = {"periods": {p.name: {"fund": slice_of(vt, p, vt_from)} for p in (ALL, BEFORE_2010, FROM_2010)}}
    out["funds"][SPY_FUND] = {"periods": {p.name: {"fund": slice_of(spy, p)} for p in (ALL, BEFORE_2010, FROM_2010)}}
    c = by_name[xp.LIMIT]
    stats = {k: v for k, v in vars(c.pullback).items() if k not in ("filled", "considered")}
    placed = stats.get("placed") or 0
    stats["fill_rate_of_orders"] = ((stats["filled_open"] + stats["filled_range"]) / placed) if placed else None
    stats["acted_differently"] = xp.pullback_acted(c, by_name["momentum"])
    out["funds"][xp.LIMIT]["orders"] = stats
    return out


def _order_counts(fund) -> dict:
    """How often the book ran out of room (``shadow.order_matters``): the counts, not the day list."""
    summary = fund_summary(fund)
    return {k: summary.get(k) for k in ("cycle_days", "days", "skipped", "outranked_days", "by_kind")}


__all__ = ["B_ON_SPY", "SPY_FUND", "month_end_of", "paired", "returns_by_day", "run_funds", "slice_of", "timing",
           "trades_of"]
