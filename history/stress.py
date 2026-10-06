"""The stress screen: the rules that need no model, through four bad stretches of the market.

The owner's instruction of 2 Oct 2026 (item 6): "Run the history screen for
momentum, A, B, C, VT and SPY over 2000-2002, 2008, 2020 and 2022. Report
maximum drawdown and return against VT for each period. Descriptive only.
No AI arms (the model remembers history). Log it in docs/research/history/
and in the graveyard." (graveyard rows 37 to 40, report folder
``docs/research/history/2026-10-stress-periods/``.)

Why: the full screen (``history.screen run``) reads every number over 26
years, where a crash is a few bad months among many good ones. Here each bad
stretch is read on its own: how deep each fund fell, and how it did against
simply holding VT, exactly when holding hurt most.

How, with the full screen's own pieces, unchanged:

* **the periods** are fixed here (``PERIODS``), each end checked to be a
  trading day by ``config.market_calendar`` (the first or last trading day
  of the span if it is not);
* **a fresh start** in each period: every fund starts with $100,000 on the
  period's first session. The indicators warm up on the prices before it:
  each journal line's technicals read the two years of final closes before
  its day (momentum's 63-day return and 50-day average), A's 200-day average
  reads the 200 closes before it, and B decides at the last month-end
  before the period from VT's 10 month-end closes up to it. The first
  trades are at the first session's open, on the lines of the session
  before it, as the live funds act on the previous session's cycle;
* **the funds** are the full screen's classes (``history.funds``):
  momentum, A (``shadow.exploratory.veto_signal``) and C
  (``shadow.exploratory.PullbackFund``) through the production engine on a
  ``SimBroker``; B (``shadow.exploratory.TimingFund``, VT or BIL); VT and
  SPY bought and held (``shadow.fund.IndexFund``). No model and no hybrid:
  the model has read about these years, so they cannot test it;
* **the journal** is ``history.journal``'s (production's technicals on
  final closes up to the previous session; the previous close stands in for
  the live price), made only for each period's sessions and the session
  before it;
* **the calendar** is the days SPY traded (``history.sessions``).

Where a fund cannot run because its prices do not exist, the screen says
"not possible" and why -- never a proxy: VT's prices start in June 2008, so
there is no VT fund and no B in 2000-2002 and VT only from its first price
in 2008; B needs 10 VT month-ends, so it cannot run in 2008; BIL (B's
T-bills) starts in May 2007. When VT does not exist in a period, each fund's
return against SPY is shown, labelled ``VT_MISSING``.

**Descriptive only**: total return, maximum drawdown (from the running high
within the period), the return minus VT's and minus SPY's over the same
sessions. No t, no verdict: four periods, each chosen because it was bad,
cannot say whether a rule is good.

Also here, because the screen is where prices are fetched (the development
sandbox has none): VT's 21-day realized volatility terciles from its first
21 returns to 2026-09-30, the regime split's cut-offs (pre-registration
section 13.10, ``analysis.regimes.tercile_cutoffs``), on the same table's
final closes.
"""

from __future__ import annotations

from collections import Counter
from datetime import date, timedelta
from pathlib import Path
from typing import Callable, Final, Mapping, Optional, Sequence

import pandas as pd

from analysis import regimes
from config import market_calendar
from config.watchlist import DEFAULT_WATCHLIST
from history import journal
from history.funds import SPY_FUND, slice_of, timing
from history.periods import Period
from history.prices import BILLS_TICKER, CALENDAR_TICKER, FIRST_FETCH, INDEX_TICKER
from history.sessions import historical_calendar
from shadow import exploratory as xp
from shadow import fund as sim
from shadow.broker import ENTRY
from shadow.fund import Fund, IndexFund, cycle_days, lines_by_day, rule_signal
from shadow.market import Bars, SimFeed, calendar
from shadow.run import integrity

#: The kind of screen this module runs (``history.screen run --kind stress``).
KIND: Final[str] = "stress"
#: The owner's four periods, as given: name, first day, last day.
PERIOD_SPANS: Final[tuple[tuple[str, date, date], ...]] = (
    ("2000-2002", date(2000, 1, 3), date(2002, 12, 31)),
    ("2008", date(2008, 1, 2), date(2008, 12, 31)),
    ("2020", date(2020, 1, 2), date(2020, 12, 31)),
    ("2022", date(2022, 1, 3), date(2022, 12, 30)),
)
#: The VT fund's name (``history.funds``, ``shadow.run``).
VT_FUND: Final[str] = "vt"
#: The funds, in the report's order: momentum, A, B, C, VT, SPY.
FUNDS: Final[tuple[str, ...]] = ("momentum", xp.VETO, xp.TIMING, xp.LIMIT, VT_FUND, SPY_FUND)
#: The funds run by the production engine.
ENGINE_FUNDS: Final[tuple[str, ...]] = ("momentum", xp.VETO, xp.LIMIT)
#: The label of a period VT did not exist in.
VT_MISSING: Final[str] = "VT did not exist; against SPY instead"


def trading_span(name: str, first: date, last: date,
                 is_trading_day: Callable[[date], bool] = market_calendar.is_trading_day) -> Period:
    """A period whose ends are trading days: the first and last trading day of ``first`` to ``last``."""
    while not is_trading_day(first):
        first += timedelta(days=1)
    while not is_trading_day(last):
        last -= timedelta(days=1)
    if first > last:
        raise ValueError(f"{name}: no trading day from {first} to {last}")
    return Period(name, first, last)


#: The periods, each end a trading day by ``config.market_calendar``.
PERIODS: Final[tuple[Period, ...]] = tuple(trading_span(*span) for span in PERIOD_SPANS)
#: The earliest price the warm-up needs: the first period's first cycle is the session before it (a few
#: days earlier), and its technicals read the two calendar years before that (``history.journal``). A's
#: 200 closes and B's 10 month-ends need less.
WARM_UP_FROM: Final[date] = journal.two_years_before(PERIODS[0].first) - timedelta(days=10)
#: Where the stress kind's fetch starts: the full kind's start already reaches far enough back, so the two
#: kinds fetch the same table (the stress kind also needs VT through 2026-09-30, for the cut-offs).
FETCH_FROM: Final[date] = min(FIRST_FETCH, WARM_UP_FROM)


# --------------------------------------------------------------------------- #
# What a period has
# --------------------------------------------------------------------------- #


def first_bar(frames: Mapping[str, pd.DataFrame], ticker: str) -> Optional[date]:
    frame = frames.get(ticker)
    return None if frame is None or frame.empty else frame.index[0].date()


def sessions_in(sessions: Sequence[date], period: Period) -> list[date]:
    return [d for d in sessions if period.contains(d)]


def first_cycle_of(sessions: Sequence[date], period: Period) -> Optional[date]:
    """The session before the period: its lines are the ones the funds act on at the first open."""
    before = [d for d in sessions if period.first is not None and d < period.first]
    return before[-1] if before else None


def journal_sessions(sessions: Sequence[date], periods: Sequence[Period] = PERIODS) -> list[date]:
    """The sessions a stress journal needs lines for: each period's, and the session before each."""
    needed: set[date] = set()
    for period in periods:
        span = sessions_in(sessions, period)
        cycle = first_cycle_of(sessions, period)
        if span and cycle is not None:
            needed.update(span)
            needed.add(cycle)
    return sorted(needed)


def build_journal(frames: dict[str, pd.DataFrame], sessions: Sequence[date], periods: Sequence[Period] = PERIODS,
                  processes: int = 1) -> dict[str, list[str]]:
    """The history journal (``history.journal.build``) for the periods' sessions only, grouped by month."""
    needed = journal_sessions(sessions, periods)
    if not needed:
        return {}
    return journal.build(frames, needed, first=needed[0], processes=processes)


def names_with_prices(frames: Mapping[str, pd.DataFrame], period: Period) -> dict:
    """How many of today's watchlist names had a price in the period, and how many from its first session."""
    lo, hi = pd.Timestamp(period.first), pd.Timestamp(period.last)
    within = started = 0
    for ticker in DEFAULT_WATCHLIST:
        frame = frames.get(ticker)
        if frame is None or frame.empty or not ((frame.index >= lo) & (frame.index <= hi)).any():
            continue
        within += 1
        if frame.index[0] <= lo:
            started += 1
    return {"watchlist": len(DEFAULT_WATCHLIST), "with_prices": within, "from_the_first_session": started}


def month_end_before(day: date) -> date:
    """The last month-end session before ``day``: B's first decision for a fresh start on ``day``.

    On the calendar in force (``shadow.exploratory.last_trading_day``): call it inside ``historical_calendar``.
    """
    previous = day.replace(day=1) - timedelta(days=1)
    return xp.last_trading_day(previous.year, previous.month)


def vt_state(frames: Mapping[str, pd.DataFrame], period: Period) -> dict:
    """Whether VT existed in the period: ``"whole"``, ``"part"`` (from its first price) or ``"none"``."""
    first = first_bar(frames, INDEX_TICKER)
    if first is None or first > period.last:
        state, note = "none", VT_MISSING
    elif first > period.first:
        state, note = "part", f"VT only from {first.isoformat()} (its first price): against VT over its sessions only"
    else:
        state, note = "whole", None
    return {"first_price": first.isoformat() if first else None, "in_period": state, "note": note}


def vt_not_possible(frames: Mapping[str, pd.DataFrame], period: Period) -> Optional[str]:
    """Why the VT fund cannot run in the period, or None."""
    first = first_bar(frames, INDEX_TICKER)
    if first is None:
        return "no VT prices in the table"
    if first > period.last:
        return f"VT did not exist (its first price is {first.isoformat()})"
    return None


def b_not_possible(bars: Bars, frames: Mapping[str, pd.DataFrame], period: Period,
                   first_decision: date) -> Optional[str]:
    """Why B cannot start fresh on the period's first session, or None when it can.

    B needs a decision on the last month-end before the period -- VT's close
    against the mean of its 10 month-end closes up to it -- and both its
    funds, VT and BIL, priced from the first session. Call it inside
    ``historical_calendar``.
    """
    reasons = []
    vt_first, bil_first = first_bar(frames, INDEX_TICKER), first_bar(frames, BILLS_TICKER)
    with timing(first_decision):
        decided = xp.timing_signals(bars, first_decision)
    if not decided or decided[0]["hold"] is None:
        if vt_first is None:
            reasons.append("no VT prices in the table")
        elif vt_first > period.last:
            reasons.append(f"VT did not exist (its first price is {vt_first.isoformat()})")
        else:
            reasons.append(f"B needs VT's month-end closes for the 10 months up to {first_decision.isoformat()}, "
                           f"its first decision; VT's first price is {vt_first.isoformat()}")
    if bil_first is None:
        reasons.append("no BIL prices in the table")
    elif bil_first > period.first:
        reasons.append(f"BIL (B's T-bills) did not exist yet (its first price is {bil_first.isoformat()})")
    return "; ".join(reasons) or None


# --------------------------------------------------------------------------- #
# Reading a fund over a period
# --------------------------------------------------------------------------- #


def own_days(fund, period: Period) -> list[date]:
    """The sessions of the period the fund was running: a held fund from its purchase, the others all."""
    days = [d.day for d in fund.days if period.contains(d.day)]
    if isinstance(fund, IndexFund):
        return [d for d in days if fund.bought is not None and d >= fund.bought]
    return days


def _window(period: Period, days: Sequence[date]) -> Period:
    return Period(period.name, days[0], days[-1])


def fund_row(fund, period: Period) -> dict:
    """Total return and maximum drawdown (from the running high, from $100,000) over the fund's sessions."""
    days = own_days(fund, period)
    if not days:
        return {"possible": False, "why": "the fund held nothing in the period"}
    s = slice_of(fund, _window(period, days))
    return {"possible": True, "first": s["from"], "last": s["to"], "sessions": s["sessions"],
            "total_return": s["total_return"], "max_drawdown": s["max_drawdown"],
            "mean_invested": s["mean_invested"]}


def against(fund, other, period: Period) -> dict:
    """The fund's total return minus ``other``'s, over the sessions both were running (the same sessions)."""
    common = sorted(set(own_days(fund, period)) & set(own_days(other, period)))
    if not common:
        return {"possible": False, "why": f"no session in common with {other.name}"}
    window = _window(period, common)
    mine, theirs = slice_of(fund, window), slice_of(other, window)
    return {"possible": True, "from": common[0].isoformat(), "to": common[-1].isoformat(), "sessions": len(common),
            "fund_return": mine["total_return"], "compared_return": theirs["total_return"],
            "difference": mine["total_return"] - theirs["total_return"]}


def _entries(fund, period: Period) -> int:
    return sum(1 for f in fund.broker.fills if f.kind == ENTRY and period.contains(f.day))


# --------------------------------------------------------------------------- #
# One period
# --------------------------------------------------------------------------- #


def new_fund(name: str, feed: SimFeed, bars: Bars, through: date):
    """A fresh fund with $100,000, of the class the full screen runs for ``name`` (``history.funds.run_funds``).

    B's first decision is the one ``timing`` sets: build it inside that block.
    """
    if name == "momentum":
        return Fund("momentum", rule_signal("momentum"), feed, bars)
    if name == xp.VETO:
        return Fund(xp.VETO, xp.veto_signal(bars), feed, bars)
    if name == xp.TIMING:
        return xp.TimingFund(xp.TIMING, bars, through)
    if name == xp.LIMIT:
        return xp.PullbackFund(xp.LIMIT, feed, bars)
    if name == VT_FUND:
        return IndexFund(VT_FUND, INDEX_TICKER, bars)
    if name == SPY_FUND:
        return IndexFund(SPY_FUND, CALENDAR_TICKER, bars)
    raise ValueError(f"not a stress fund: {name!r}")


def run_period(journal_dir: Path, frames: Mapping[str, pd.DataFrame], sessions: Sequence[date],
               period: Period) -> dict:
    """Every fund, from a fresh $100,000, over the period's sessions; or "not possible" and why for each."""
    span = sessions_in(sessions, period)
    first_cycle = first_cycle_of(sessions, period)
    out: dict = {"first": period.first.isoformat(), "last": period.last.isoformat(),
                 "names": names_with_prices(frames, period), "vt": vt_state(frames, period)}
    if not span or first_cycle is None:
        why = "no session in the price table" if not span else "no session before it to start from"
        out["funds"] = {name: {"possible": False, "why": why} for name in FUNDS}
        out["sessions"] = len(span)
        return out
    bars = Bars(dict(frames))
    why_not: dict[str, Optional[str]] = {}
    with historical_calendar(sessions):
        years = range(first_cycle.year, span[-1].year + 1)
        entries = [e for e in journal.as_answered(journal.read(journal_dir, years))
                   if e.timestamp is not None and first_cycle <= e.timestamp.date() <= span[-1]]
        cycles = lines_by_day(entries)
        ran = cycle_days(entries)
        del entries
        tickers = {line.ticker for lines in cycles.values() for line in lines}
        days = calendar(bars, (INDEX_TICKER, CALENDAR_TICKER, *sorted(tickers)), span[0], span[-1])
        feed = SimFeed(bars)
        first_decision = month_end_before(period.first)
        if not tickers:
            for name in ENGINE_FUNDS:
                why_not[name] = "no watchlist name has a journal line in the period"
        why_not[VT_FUND] = vt_not_possible(frames, period)
        why_not[xp.TIMING] = b_not_possible(bars, frames, period, first_decision)
        with timing(first_decision):
            funds = {name: new_fund(name, feed, bars, span[-1]) for name in FUNDS if why_not.get(name) is None}
            sim.run(list(funds.values()), days, cycles, ran, feed, first_cycle)
    vt, spy = funds.get(VT_FUND), funds[SPY_FUND]
    rows: dict = {}
    for name in FUNDS:
        if name not in funds:
            rows[name] = {"possible": False, "why": why_not[name]}
            continue
        fund = funds[name]
        row = fund_row(fund, period)
        if row["possible"]:
            if name != VT_FUND:
                row["vs_vt"] = (against(fund, vt, period) if vt is not None
                                else {"possible": False, "why": why_not[VT_FUND]})
            if name != SPY_FUND:
                row["vs_spy"] = against(fund, spy, period)
            if name in ENGINE_FUNDS:
                row["entries"] = _entries(fund, period)
            elif name == xp.TIMING:
                row["switches"], row["first_decision"] = fund.switches, first_decision.isoformat()
        rows[name] = row
    out.update(sessions=len(days), first_session=days[0].isoformat(), last_session=days[-1].isoformat(),
               first_cycle=first_cycle.isoformat(), funds=rows, integrity=integrity(list(funds.values())))
    return out


#: What the forked period workers read (set before the pool forks).
_SHARED: dict = {}


def _period_job(index: int) -> tuple[str, dict]:
    s = _SHARED
    period = s["periods"][index]
    return period.name, run_period(s["journal"], s["frames"], s["sessions"], period)


def run_periods(journal_dir: Path, frames: Mapping[str, pd.DataFrame], sessions: Sequence[date],
                periods: Sequence[Period] = PERIODS, processes: int = 1) -> dict[str, dict]:
    """``run_period`` for every period, in order; the periods side by side when ``processes`` > 1."""
    if processes > 1 and len(periods) > 1:
        from multiprocessing import get_context

        _SHARED.update(journal=journal_dir, frames=frames, sessions=list(sessions), periods=tuple(periods))
        try:
            with get_context("fork").Pool(min(processes, len(periods))) as pool:
                done = pool.map(_period_job, range(len(periods)), chunksize=1)
        finally:
            _SHARED.clear()
    else:
        done = [(p.name, run_period(journal_dir, frames, sessions, p)) for p in periods]
    return dict(done)


# --------------------------------------------------------------------------- #
# The regime split's cut-offs
# --------------------------------------------------------------------------- #


def regime_cutoffs(frames: Mapping[str, pd.DataFrame], final_through: date,
                   last: date = regimes.VT_CUTOFF_WINDOW_END) -> dict:
    """VT's 21-day volatility terciles to ``last`` (``analysis.regimes.tercile_cutoffs``), and the sessions in each.

    ``complete`` is False when the table's prices end before ``last``: the
    numbers are then not the registration's.
    """
    frame = frames.get(INDEX_TICKER)
    if frame is None or frame.empty:
        return {"possible": False, "why": "no VT prices in the table"}
    closes = [(stamp.date(), float(close)) for stamp, close in frame["Close"].items()]
    vols = [(day, vol) for day, vol in regimes.vol_series(closes) if day <= last]
    if not vols:
        return {"possible": False, "why": f"fewer than {regimes.VOL_RETURNS + 1} VT closes up to {last.isoformat()}"}
    cutoffs = regimes.tercile_cutoffs(closes, last)
    counts = Counter(regimes.tercile(vol, cutoffs) for _, vol in vols)
    return {"possible": True, "cutoffs": list(cutoffs), "window_end": last.isoformat(),
            "first_session": vols[0][0].isoformat(), "last_session": vols[-1][0].isoformat(), "sessions": len(vols),
            "by_tercile": {state: counts.get(state, 0) for state in regimes.VOL_STATES},
            "complete": final_through >= last,
            "method": "numpy.quantile (default method 'linear') at 1/3 and 2/3 of the daily 21-day volatility, "
                      "each session's from the 21 log returns ending at its own close, x sqrt(252)"}


__all__ = ["ENGINE_FUNDS", "FETCH_FROM", "FUNDS", "KIND", "PERIODS", "PERIOD_SPANS", "VT_FUND", "VT_MISSING",
           "WARM_UP_FROM", "against", "b_not_possible", "build_journal", "first_bar", "first_cycle_of", "fund_row",
           "journal_sessions", "month_end_before", "names_with_prices", "new_fund", "own_days", "regime_cutoffs",
           "run_period", "run_periods", "sessions_in", "trading_span", "vt_not_possible", "vt_state"]
