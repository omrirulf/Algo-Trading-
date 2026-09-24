"""A fund's day: which lines, in what order, through the production engine and manager.

``shadow.fund`` drives the real ``ExecutionEngine`` and ``PositionManager``
over a ``SimBroker`` and a ``SimFeed``. These tests check the driving: the
lines every fund may act on, the one priority rule production has (cycle,
then watchlist order), the held-name skip, a session with no cycle, the
engine's sizing against the book as it stood at each dispatch, the index
fund, and -- over long random runs with coin-flip funds -- the invariants
that say the simulation itself has not gone wrong: every position's stops
cover it exactly, cash is the sum of the fills, no line reaches the live
audit log, and two runs are identical.
"""

from __future__ import annotations

import logging
import math
from datetime import date, datetime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import pytest

from analysis.reader import JournalEntry
from app import position_manager as pm
from app import risk_engine
from app.broker_client import OpenPosition
from app.market_data import MarketDataError
from app.schemas import Bias, LLMSignal
from config import settings as cfg
from shadow.broker import DEFAULT_COST_PER_SIDE, DIVIDEND, ENTRY, STOP, TRANCHE
from shadow.fund import (
    STARTING_CASH,
    Fund,
    IndexFund,
    Line,
    coin_signal,
    cycle_days,
    dispatch_order,
    lines_by_day,
    model_signal,
    run,
)
from shadow.market import Bars, SimFeed

COST = DEFAULT_COST_PER_SIDE
WARM = 70                                               # business days before the first session: a 90-day ATR
DAYS = pd.bdate_range("2026-01-05", periods=WARM + 90)
S = [d.date() for d in DAYS[WARM:]]                     # the sessions


def stamp(day: date, hour: int = 15, minute: int = 0) -> datetime:
    return datetime(day.year, day.month, day.day, hour, minute, tzinfo=timezone.utc)


def said(ticker: str, day: date, bias: str = "BULLISH", conviction: float = 0.6, hour: int = 15,
         **fields) -> JournalEntry:
    """One journal line the model answered."""
    return JournalEntry(ticker=ticker, timestamp=stamp(day, hour), timestamp_is_exact=True, bias=bias,
                        conviction=conviction, **fields)


def flat(price: float = 100.0, changes: dict[int, dict[str, float]] | None = None) -> pd.DataFrame:
    """A quiet tape: open and close at ``price``, a point either side, so no
    stop is reached unless ``changes`` (session index -> column values) says so."""
    frame = pd.DataFrame({"Open": price, "High": price + 1, "Low": price - 1, "Close": price, "Dividends": 0.0},
                         index=DAYS)
    for k, values in (changes or {}).items():
        for column, value in values.items():
            frame.iloc[WARM + k, frame.columns.get_loc(column)] = value
    return frame


def walk(seed: int, start: float, vol: float, drift: float = 0.0, dividend_every: int = 0) -> pd.DataFrame:
    rng = np.random.RandomState(seed)
    n = len(DAYS)
    close = start * np.exp(np.cumsum(rng.normal(drift, vol, n)))
    prev = np.concatenate([[start], close[:-1]])
    open_ = prev * np.exp(rng.normal(0.0, vol / 2, n))
    spread = np.abs(rng.normal(0.0, vol, n)) * 0.8 + vol / 3
    dividends = np.zeros(n)
    if dividend_every:
        dividends[WARM + 3::dividend_every] = start * 0.004
    return pd.DataFrame({"Open": open_, "High": np.maximum(open_, close) * (1 + spread),
                         "Low": np.minimum(open_, close) * (1 - spread), "Close": close,
                         "Dividends": dividends}, index=DAYS)


def fund(name: str, bars: Bars, feed: SimFeed, signal=model_signal, **kw) -> Fund:
    return Fund(name, signal, feed, bars, keep_actions=True, **kw)


def line(entry: JournalEntry, cycle: int = 1) -> Line:
    return Line(entry.ticker, entry.timestamp.date(), cycle, entry)


# --------------------------------------------------------------------------- #
# Which lines, in what order
# --------------------------------------------------------------------------- #


def test_lines_by_day_keeps_only_what_the_model_answered_about_that_ticker():
    d = S[0]
    entries = [
        said("MSFT", d),
        said("XOM", d, bias="NEUTRAL"),                                           # an answer: kept
        JournalEntry(ticker="NVDA", timestamp=stamp(d), held=True),               # held live: nobody gets it
        JournalEntry(ticker="JPM", timestamp=stamp(d), error="timeout"),          # a failed call
        JournalEntry(ticker="LLY", timestamp=stamp(d), error="context: fetch failed", stage="context"),
        said("TM", d, error="answered for TSLA"),                                 # an answer about another name
        said("PG", d, held=True),
        JournalEntry(ticker="CAT", timestamp=None, bias="BULLISH", conviction=0.6),
    ]
    cycles = lines_by_day(entries)
    assert [(ln.ticker, ln.cycle) for ln in cycles[d]] == [("MSFT", 1), ("XOM", 1)]
    # Every cycle that ran counts as having run, whatever its lines were.
    assert cycle_days(entries) == {d}
    assert cycle_days([JournalEntry(ticker="NVDA", timestamp=stamp(S[1]), held=True)]) == {S[1]}


def test_lines_are_grouped_by_their_utc_day():
    """A New York evening is already the next day in UTC; a naive stamp (the
    old ``ts`` fallback) is read as UTC."""
    new_york_evening = JournalEntry(ticker="MSFT", timestamp=datetime(2026, 4, 1, 21, 30,
                                                                      tzinfo=ZoneInfo("America/New_York")),
                                    timestamp_is_exact=True, bias="BULLISH", conviction=0.6)
    naive = JournalEntry(ticker="XOM", timestamp=datetime(2026, 4, 1, 23, 30), bias="BULLISH", conviction=0.6)
    just_after_midnight = JournalEntry(ticker="NVDA", timestamp=datetime(2026, 4, 2, 0, 30, tzinfo=timezone.utc),
                                       timestamp_is_exact=True, bias="BULLISH", conviction=0.6)
    cycles = lines_by_day([new_york_evening, naive, just_after_midnight])
    assert [ln.ticker for ln in cycles[date(2026, 4, 1)]] == ["XOM"]
    assert [ln.ticker for ln in cycles[date(2026, 4, 2)]] == ["MSFT", "NVDA"]


def test_dispatch_is_cycle_then_watchlist_order_with_unknown_tickers_last_by_name():
    d = S[0]
    entries = [said(t, d, hour=14) for t in ("ZZZ", "GLD", "AAPL", "XOM", "MSFT", "RSP")]
    entries += [said(t, d, hour=18) for t in ("GLD", "MSFT")]
    order = [(ln.ticker, ln.cycle) for ln in lines_by_day(entries)[d]]
    assert order == [("MSFT", 1), ("XOM", 1), ("RSP", 1), ("GLD", 1), ("AAPL", 1), ("ZZZ", 1),
                     ("MSFT", 2), ("GLD", 2)]
    assert dispatch_order(line(said("MSFT", d), cycle=2)) > dispatch_order(line(said("ZZZ", d)))


def test_a_second_cycles_line_is_not_promoted_when_its_first_cycle_line_was_dropped():
    d = S[0]
    entries = [
        JournalEntry(ticker="MSFT", timestamp=stamp(d, 14), held=True),     # cycle 1: MSFT held live
        said("XOM", d, hour=14),                                            # cycle 1
        said("MSFT", d, hour=18),                                           # cycle 2
        said("XOM", d, hour=18),                                            # cycle 2
    ]
    order = [(ln.ticker, ln.entry.timestamp.hour) for ln in lines_by_day(entries)[d]]
    assert order == [("XOM", 14), ("MSFT", 18), ("XOM", 18)]


# --------------------------------------------------------------------------- #
# One session, by hand
# --------------------------------------------------------------------------- #


def book_before(fills, opens: dict[str, float], cash: float) -> tuple[float, list[OpenPosition], float]:
    """Equity, positions and cash after ``fills``, marked at today's opens."""
    held: dict[str, int] = {}
    for f in fills:
        signed = f.qty if f.side == "buy" else -f.qty
        if f.kind == DIVIDEND:
            cash += signed * f.price
            continue
        cash -= signed * f.price + f.cost
        held[f.ticker] = held.get(f.ticker, 0) + signed
    positions = [OpenPosition(t, float(q), abs(q) * opens[t], opens[t]) for t, q in held.items() if q]
    return cash + sum(p.qty * opens[p.ticker] for p in positions), positions, cash


def expected_qty(fills_before, ticker: str, side: str, opens: dict[str, float], cash: float) -> int:
    """What the engine must size, from the book as it stood just before this entry:
    floor(min(equity x the ticker's cap, the tightest portfolio headroom) / price)."""
    equity, positions, _ = book_before(fills_before, opens, cash)
    headroom, _ = risk_engine.budget_ceiling_for(equity, ticker, positions, side)
    cap = equity * risk_engine.max_position_pct_for(ticker)
    return max(0, math.floor(min(cap, headroom) / opens[ticker]))


def test_priority_is_watchlist_order_and_every_entry_is_sized_on_the_book_before_it():
    """Six Technology names, more than the group's 25% can hold. In watchlist
    order the two single names and the first funds take the room, and IGV,
    last of them, is refused. Each accepted size is floor(min(equity x cap,
    headroom) / open) on the book as it stood after every fill before it --
    costs included -- and each stop is the open less two ATRs."""
    tech = ("IGV", "SMH", "XLC", "XLK", "NVDA", "MSFT")                      # journalled backwards on purpose
    bars = Bars({t: flat() for t in tech})
    feed = SimFeed(bars)
    f = fund("model", bars, feed)
    d = S[0]
    cycle = lines_by_day([said(t, S[0]) for t in tech])[d]
    assert [ln.ticker for ln in cycle] == ["MSFT", "NVDA", "XLK", "XLC", "SMH", "IGV"]
    feed.at_open(S[1])
    f.session(S[1], cycle)

    entries = [x for x in f.broker.fills if x.kind == ENTRY]
    assert [x.ticker for x in entries] == ["MSFT", "NVDA", "XLK", "XLC", "SMH"]
    opens = {t: 100.0 for t in tech}
    for i, fill in enumerate(entries):
        assert fill.qty == expected_qty(entries[:i], fill.ticker, "buy", opens, STARTING_CASH), fill.ticker
        assert fill.price == 100.0 and fill.cost == pytest.approx(fill.qty * 100.0 * COST)
    assert [x.qty for x in entries] == [50, 49, 69, 69, 12]                   # the arithmetic, spelled out
    [igv] = [x for x in f.decisions if x.ticker == "IGV"]
    assert igv.status == "REJECTED" and "'Technology' group" in igv.reason
    for stop in f.broker.live_stops():
        assert stop.stop_price == risk_engine.calculate_stop_price(100.0, feed.get_atr(stop.ticker), "buy")
        assert stop.qty == f.broker.positions[stop.ticker].qty


def test_a_second_cycle_the_same_day_is_dispatched_after_the_first():
    bars = Bars({t: flat() for t in ("MSFT", "XOM")})
    feed = SimFeed(bars)
    f = fund("model", bars, feed)
    d = S[0]
    cycle = lines_by_day([
        said("MSFT", d, bias="NEUTRAL", hour=14), said("XOM", d, hour=14),
        said("MSFT", d, hour=18), said("XOM", d, hour=18),
    ])[d]
    feed.at_open(S[1])
    f.session(S[1], cycle)
    assert [(x.ticker, x.status, x.dispatched) for x in f.decisions] == [
        ("MSFT", "REJECTED", True), ("XOM", "ACCEPTED", True),
        ("MSFT", "ACCEPTED", True), ("XOM", "SKIPPED", False)]
    assert [x.ticker for x in f.broker.fills if x.kind == ENTRY] == ["XOM", "MSFT"]


def test_a_held_ticker_is_skipped_not_added_to():
    """Production asks nothing about a held name (``SKIP_HELD_TICKERS``), so
    no fund may add to one -- nor be refused a flip it was never offered."""
    assert cfg.SKIP_HELD_TICKERS
    bars = Bars({"MSFT": flat()})
    feed = SimFeed(bars)
    f = fund("model", bars, feed)
    feed.at_open(S[1])
    f.session(S[1], [line(said("MSFT", S[0]))])
    signal_lines = len(f.audit.lines_for("MSFT"))
    feed.at_open(S[2])
    f.session(S[2], [line(said("MSFT", S[1], conviction=0.9)), line(said("MSFT", S[1], bias="BEARISH"), cycle=2)])
    assert [x.kind for x in f.broker.fills] == [ENTRY]
    assert f.broker.positions["MSFT"].qty == 50
    assert [(x.status, x.dispatched, x.reason) for x in f.decisions[1:]] == [
        ("SKIPPED", False, "already held"), ("SKIPPED", False, "already held")]
    # The engine was never asked: the only new record is the manager's pass.
    new = f.audit.lines_for("MSFT")[signal_lines:]
    assert all('"position_managed"' in raw for raw in new) and len(new) == 1


def test_a_session_with_no_cycle_before_it_still_fills_stops_and_marks_but_does_not_manage():
    bars = Bars({"MSFT": flat(changes={2: {"Low": 90.0}}), "XOM": flat(50.0, {3: {"Close": 55.0}})})
    feed = SimFeed(bars)
    f = fund("model", bars, feed)
    feed.at_open(S[1])
    f.session(S[1], [line(said("MSFT", S[0])), line(said("XOM", S[0]))])
    stop = f.broker.get_open_stop_order("MSFT").stop_price
    actions = len(f.audit.actions)

    feed.at_open(S[2])
    day = f.session(S[2], None)                                            # no cycle ran on S[1]
    assert len(f.audit.actions) == actions                                 # the manager did not run
    [hit] = [x for x in f.broker.fills if x.kind == STOP]
    assert (hit.ticker, hit.day, hit.price, hit.gapped) == ("MSFT", S[2], stop, False)
    assert "MSFT" not in f.broker.positions
    xom = f.broker.positions["XOM"].qty
    assert day.equity == pytest.approx(f.broker.cash + xom * 50.0)

    feed.at_open(S[3])
    day = f.session(S[3], None)
    assert day.equity == pytest.approx(f.broker.cash + xom * 55.0)         # marked at this close
    assert day.gross == pytest.approx(xom * 55.0) and day.positions == 1

    feed.at_open(S[4])
    f.session(S[4], [])                                                    # a cycle ran, nothing to act on
    assert len(f.audit.actions) == actions + 1                             # the manager did


def test_run_hands_each_session_the_cycle_of_the_session_before_it():
    """The first session has no cycle before it; a session after a day no
    cycle ran gets None (stops and marks only); after a cycle that had
    nothing actionable it gets [] (the manager still runs, as live); and the
    feed's clock is at that session's open whenever a fund acts."""
    seen: list[tuple[date, object]] = []

    class Spy:
        def session(self, day, cycle):
            assert feed.session == day
            seen.append((day, cycle))

    feed = SimFeed(Bars({"MSFT": flat()}))
    a, b = line(said("MSFT", S[0])), line(said("MSFT", S[3]))
    run([Spy(), Spy()], S[:5], {S[0]: [a], S[3]: [b]}, {S[0], S[2], S[3]}, feed)
    assert seen[::2] == seen[1::2]                                          # every fund, the same cycle
    assert seen[::2] == [(S[0], None), (S[1], [a]), (S[2], None), (S[3], []), (S[4], [b])]


def test_the_index_fund_buys_once_at_the_first_open_with_cost_and_is_paid_its_dividends():
    vt = flat(110.0, {1: {"Open": 111.0, "Dividends": 0.9}, 3: {"Dividends": 0.5, "Close": 112.0}})
    vt = vt.drop(index=DAYS[WARM + 5])                                     # one session with no bar
    bars = Bars({"VT": vt})
    index = IndexFund("vt", "VT", bars)
    days = [index.session(d) for d in S[1:7]]
    qty = math.floor(STARTING_CASH / (111.0 * (1 + COST)))
    cash = STARTING_CASH - qty * 111.0 * (1 + COST)
    assert index.qty == qty and index.bought == S[1] and index.tally.accepted == 1
    assert days[0].cash == pytest.approx(cash)                             # bought ON the ex-date: not paid
    assert days[0].equity == pytest.approx(cash + qty * 110.0)
    assert days[1].cash == pytest.approx(cash)
    assert days[2].cash == pytest.approx(cash + qty * 0.5)                 # held at the previous close: paid
    assert days[2].equity == pytest.approx(cash + qty * 0.5 + qty * 112.0)
    assert days[4].day == S[5] and days[4].equity == days[3].equity        # no bar: carried
    assert days[5].equity == pytest.approx(cash + qty * 0.5 + qty * 110.0)
    assert index.qty == qty                                                # never bought again


def test_an_index_fund_whose_first_session_has_no_bar_buys_at_the_first_that_does():
    bars = Bars({"VT": flat(110.0).drop(index=DAYS[WARM + 1])})
    index = IndexFund("vt", "VT", bars)
    first = index.session(S[1])
    assert index.qty == 0 and first.equity == STARTING_CASH
    index.session(S[2])
    assert index.bought == S[2] and index.qty == math.floor(STARTING_CASH / (110.0 * (1 + COST)))


# --------------------------------------------------------------------------- #
# Long runs: the invariants
# --------------------------------------------------------------------------- #

UNIVERSE = ("MSFT", "NVDA", "JPM", "XOM", "RSP", "IWM", "TLT", "IEF", "HYG", "XLE", "XLK", "GLD")


#: Overnight gaps: from that session on, the tape opens at a new level -- the
#: move a resting stop is gapped through, long side and short side alike.
GAPS = {"XOM": (12, 0.86), "NVDA": (20, 1.14), "JPM": (27, 0.88), "XLK": (35, 1.12), "GLD": (44, 0.9)}


def universe(missing: dict[str, list[int]] | None = None) -> Bars:
    frames = {t: walk(i, 30 + 13 * i, 0.012 + 0.004 * (i % 4), 0.0015 * ((i % 3) - 1),
                      dividend_every=17 if i % 3 == 0 else 0)
              for i, t in enumerate(UNIVERSE)}
    for ticker, (k, factor) in GAPS.items():
        frames[ticker].iloc[WARM + k:, :4] *= factor
    for ticker, sessions in (missing or {}).items():
        frames[ticker] = frames[ticker].drop(index=[DAYS[WARM + k] for k in sessions])
    frames["VT"] = walk(99, 110.0, 0.008)
    return Bars(frames)


def journal(sessions, seed: int = 11) -> list[JournalEntry]:
    """A cycle every session for every name: mostly answers, some held or failed."""
    rng = np.random.RandomState(seed)
    out = []
    for day in sessions:
        for ticker in UNIVERSE:
            u = rng.rand()
            if u < 0.05:
                out.append(JournalEntry(ticker=ticker, timestamp=stamp(day), held=True))
            elif u < 0.08:
                out.append(JournalEntry(ticker=ticker, timestamp=stamp(day), error="timeout"))
            else:
                out.append(said(ticker, day, bias=("BULLISH", "BEARISH", "NEUTRAL")[int(rng.rand() * 3)],
                                conviction=float(rng.choice([0.2, 0.5, 0.8]))))
    return out


class CheckedFund(Fund):
    """A fund that checks, after every session, what must always hold."""

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.violations: list[str] = []

    def session(self, day, cycle):
        record = super().session(day, cycle)
        broker, bars = self.broker, self.bars
        covered: dict[str, int] = {}
        for stop in broker.live_stops():
            covered[stop.ticker] = covered.get(stop.ticker, 0) + stop.qty
        for ticker, pos in broker.positions.items():
            if covered.pop(ticker, 0) != abs(pos.qty):
                self.violations.append(f"{day} {ticker}: stops do not cover {pos.qty}")
        if covered:
            self.violations.append(f"{day}: stops with no position {covered}")
        # Cash is exactly the sum of what the fills say moved it.
        ledger = STARTING_CASH
        for f in broker.fills:
            signed = f.qty if f.side == "buy" else -f.qty
            ledger += signed * f.price if f.kind == DIVIDEND else -(signed * f.price + f.cost)
        if not math.isclose(ledger, broker.cash, rel_tol=0, abs_tol=1e-6):
            self.violations.append(f"{day}: cash {broker.cash} but the fills say {ledger}")
        # Every trade's money is somewhere: closed trades plus open positions.
        booked = sum(c.pnl for c in broker.closed) + sum(p.realised for p in broker.positions.values())
        if not math.isclose(booked, broker.cash - STARTING_CASH, rel_tol=0, abs_tol=1e-6):
            self.violations.append(f"{day}: trades book {booked}, cash moved {broker.cash - STARTING_CASH}")
        # Marked at today's close, or the last close before it when there is no bar.
        mark = 0.0
        for ticker, pos in broker.positions.items():
            bar = bars.bar(ticker, day)
            mark += pos.qty * (bar[3] if bar else bars.last_close_before(ticker, day))
        if not math.isclose(record.equity, broker.cash + mark, rel_tol=1e-12):
            self.violations.append(f"{day}: equity {record.equity} != {broker.cash + mark}")
        return record


def sizing_mismatches(f: Fund) -> list[str]:
    """Every entry the fund made, re-sized from its own fills: the book just
    before it (earlier days, then today's gap stops, rungs and earlier
    entries), marked at today's open -- or the last close, with no bar."""
    out = []
    fills = f.broker.fills
    for i, x in enumerate(fills):
        if x.kind != ENTRY:
            continue
        held = _held_on_fills(fills[:i])
        opens = {}
        for ticker in held | {x.ticker}:
            bar = f.bars.bar(ticker, x.day)
            opens[ticker] = bar[0] if bar else f.bars.last_close_before(ticker, x.day)
        want = expected_qty(fills[:i], x.ticker, x.side, opens, STARTING_CASH)
        if x.qty != want or x.price != opens[x.ticker]:
            out.append(f"{f.name} {x.day} {x.ticker}: {x.qty} @ {x.price}, expected {want} @ {opens[x.ticker]}")
    return out


def _held_on_fills(fills) -> set[str]:
    held: dict[str, int] = {}
    for x in fills:
        if x.kind != DIVIDEND:
            held[x.ticker] = held.get(x.ticker, 0) + (x.qty if x.side == "buy" else -x.qty)
    return {t for t, q in held.items() if q}


def build(bars: Bars, seeds=(1, 2, 3), with_model: bool = False, sessions=None):
    sessions = sessions or S[:60]
    entries = journal(sessions)
    feed = SimFeed(bars)
    funds = [CheckedFund(f"coin-{s}", coin_signal(s), feed, bars, keep_actions=True) for s in seeds]
    if with_model:
        funds.append(CheckedFund("model", model_signal, feed, bars, keep_actions=True))
    funds.append(IndexFund("vt", "VT", bars))
    return funds, sessions, lines_by_day(entries), cycle_days(entries), feed


def test_a_long_random_run_keeps_every_invariant_and_nothing_reaches_the_live_log(
        monkeypatch, _audit_log_to_tmp):
    """Three coin-flip funds and the model fund, sixty sessions, twelve names:
    after every session each position's stops cover it exactly, cash is the
    sum of the fills, the trades account for all of it, and the book is
    marked at the close. No engine error is "unexpected", the manager never
    errs, R is never estimated -- and no line reaches the live audit log."""
    from app import logger as app_logger

    asked: list[object] = []
    monkeypatch.setattr(app_logger, "get_audit_logger",
                        lambda *a, **k: asked.append(a) or logging.Logger("would-have-been-the-live-log"))
    live = logging.getLogger("execution_audit")
    before = (list(live.handlers), live.level, live.propagate)
    funds, sessions, cycles, ran, feed = build(universe(), with_model=True)
    run(funds, sessions, cycles, ran, feed)                                 # raises LiveAuditLeak on a leak

    assert asked == []
    assert not _audit_log_to_tmp.exists()
    assert (list(live.handlers), live.level, live.propagate) == before
    checked = [f for f in funds if isinstance(f, CheckedFund)]
    for f in checked:
        assert f.violations == [], f.name
        assert f.tally.unexpected == [] and f.tally.manager_errors == [] and f.tally.estimated_r == 0, f.name
        assert len(f.days) == len(sessions)
        assert sizing_mismatches(f) == [], f.name
    # And the run did something worth checking.
    fills = [x for f in checked for x in f.broker.fills]
    kinds = {x.kind for x in fills}
    assert {ENTRY, STOP, TRANCHE, DIVIDEND} <= kinds
    assert {x.side for x in fills if x.kind == ENTRY} == {"buy", "sell"}
    assert any(x.gapped for x in fills if x.kind == STOP) and any(not x.gapped for x in fills if x.kind == STOP)
    assert sum(len(f.broker.closed) for f in checked) > 20
    actions = {a["action"] for f in checked for a in f.audit.actions}
    assert {pm.TRANCHE_TAKEN, pm.STOP_RAISED, pm.HELD} <= actions
    assert not actions & {pm.ERROR, pm.NO_STOP, pm.PROTECTED, pm.STOP_RESIZED}
    assert sum(f.tally.accepted for f in checked) > 50
    assert sum(1 for f in checked for x in f.decisions if x.status == "SKIPPED") > 0


def test_two_runs_are_identical():
    def once():
        funds, sessions, cycles, ran, feed = build(universe(), seeds=(4, 5), with_model=True,
                                                   sessions=S[:40])
        run(funds, sessions, cycles, ran, feed)
        index = funds.pop()
        return [index.days] + [(f.days, f.broker.fills, f.broker.closed, f.decisions, f.audit.actions)
                               for f in funds]

    first, second = once(), once()
    assert first == second
    assert first[1][1] != first[2][1]                                       # and the seeds really differ


def test_the_run_is_stable_when_a_held_ticker_has_no_bar_on_some_sessions():
    """GLD is missing four sessions while the model fund holds it. Nothing
    raises; its stops still cover it; it is marked at its last close; the
    only manager errors are the feed's "no bar" for GLD on exactly those
    days; and it is managed again once its bars return."""
    missing = [10, 11, 12, 30]
    bars = universe(missing={"GLD": missing})
    sessions = S[:45]
    entries = journal(sessions)
    entries += [said("GLD", day, hour=16) for day in sessions]               # the model wants it every day
    feed = SimFeed(bars)
    model = CheckedFund("model", model_signal, feed, bars, keep_actions=True)
    coin = CheckedFund("coin-7", coin_signal(7), feed, bars, keep_actions=True)
    run([model, coin], sessions, lines_by_day(entries), cycle_days(entries), feed)

    gaps = {S[k] for k in missing}
    for f in (model, coin):
        assert f.violations == [] and f.tally.unexpected == [], f.name
        assert sizing_mismatches(f) == [], f.name
        for error in f.tally.manager_errors:
            ticker, reason = error.split(": ", 1)
            assert ticker == "GLD" and reason.startswith("MarketDataError: no bar for GLD on "), error
            assert date.fromisoformat(reason.rsplit(" ", 1)[1]) in gaps
    held_through = [k for k in missing if model.days[k].positions and "GLD" in _held_on(model, S[k])]
    assert held_through, "the scenario must have GLD held across a gap"
    assert len(model.tally.manager_errors) >= len(held_through)
    assert [x for x in model.broker.fills if x.ticker == "GLD" and x.day in gaps] == []
    gld = [a["action"] for a in model.audit.actions if a["ticker"] == "GLD"]
    last_error = max(i for i, action in enumerate(gld) if action == pm.ERROR)
    assert any(action != pm.ERROR for action in gld[last_error + 1:])     # managed again after the gap


def _held_on(f: Fund, day: date) -> set[str]:
    """Tickers the fund held at the close of ``day``, rebuilt from its fills."""
    return _held_on_fills([x for x in f.broker.fills if x.day <= day])


def test_a_missing_bar_on_a_line_the_fund_does_not_hold_is_an_engine_error_not_an_unexpected_one():
    bars = Bars({"MSFT": flat().drop(index=DAYS[WARM + 1])})
    feed = SimFeed(bars)
    f = fund("model", bars, feed)
    feed.at_open(S[1])
    f.session(S[1], [line(said("MSFT", S[0]))])
    assert f.tally.errors == 1 and f.tally.unexpected == []
    assert f.decisions[0].reason.startswith("MarketDataError")
    with pytest.raises(MarketDataError):
        feed.get_latest_price("MSFT")


def test_the_model_signal_is_the_journals_own_bias_and_conviction():
    entry = said("MSFT", S[0], bias="BEARISH", conviction=0.73)
    signal = model_signal(line(entry))
    assert (signal.ticker, signal.bias, signal.conviction) == ("MSFT", Bias.BEARISH, 0.73)
    assert model_signal(line(said("MSFT", S[0], bias="SIDEWAYS"))) is None
    assert isinstance(coin_signal(3)(line(entry)), LLMSignal)
    assert coin_signal(3)(line(entry)) == coin_signal(3)(line(entry))


# The order of a day: gapped stops at the open, the manager, the entries, the
# session's stops, then dividends on the shares held at the previous close.
# Found by review: every other test passed with the order shuffled.
def test_the_day_is_gap_manage_enter_touch_then_dividends_on_the_previous_close():
    bars = Bars({"MSFT": flat(100.0, {2: {"Open": 90.0, "Low": 89.0, "High": 91.0, "Close": 90.0,
                                         "Dividends": 0.5}}),
                 "XOM": flat(50.0, {2: {"Dividends": 0.2}})})
    feed = SimFeed(bars)
    f = fund("model", bars, feed)
    feed.at_open(S[1])
    f.session(S[1], [line(said("MSFT", S[0]))])
    held = f.broker.positions["MSFT"].qty

    calls = []
    for obj, name in ((f.broker, "fill_gapped_stops"), (f.manager, "manage"), (f.engine, "execute"),
                      (f.broker, "fill_touched_stops"), (f.broker, "pay_dividends")):
        real = getattr(obj, name)
        setattr(obj, name, lambda *a, _r=real, _n=name, **k: calls.append(_n) or _r(*a, **k))
    feed.at_open(S[2])
    f.session(S[2], [line(said("MSFT", S[1])), line(said("XOM", S[1]))])
    assert calls == ["fill_gapped_stops", "manage", "execute", "execute", "fill_touched_stops", "pay_dividends"]

    [paid] = [x for x in f.broker.fills if x.kind == DIVIDEND]
    assert (paid.ticker, paid.qty) == ("MSFT", held)              # XOM bought today: not entitled
    [trade] = f.broker.closed
    assert trade.opened == S[1] and trade.closed == S[2]
    assert trade.pnl == pytest.approx(sum(
        (-1 if x.side == "buy" else 1) * x.qty * x.price - x.cost for x in f.broker.fills
        if x.ticker == "MSFT" and x.day <= S[2] and x.kind != DIVIDEND and x.kind != ENTRY or
        (x.ticker == "MSFT" and x.kind == ENTRY and x.day == S[1])) + held * 0.5)
