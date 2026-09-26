"""Late runs in calibration: the owner's decision of 25 Sep 2026.

When the real account's run falls outside market hours its broker refuses
the entries ("market is closed") and its profit-ladder pass cannot run. The
calibration copy mirrors that -- it does not make those entries, and skips
that pass -- counts every item, shows it, and stops calibration when more
than 2 calibration days need it. The race and the funds do not change.

Every test builds its own bars, snapshots, audit lines and journal. The
dates are the ones ``test_shadow_calibration`` uses: C0 is Thursday 1 Oct
2026, C1 Friday, C2 Monday 5 Oct, C3 Tuesday, C4 Wednesday. New York is on
EDT, so the session is 13:30 to 20:00 UTC.
"""

from __future__ import annotations

import dataclasses
import inspect
import json
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

import pandas as pd
import pytest

from analysis.reader import JournalEntry
from shadow import calibration as calib
from shadow.fund import Decision, Fund, IndexFund
from shadow.market import Bars, SimFeed
from tests.test_dashboard_build import (  # the node harness the 4 Funds page's own tests use
    FUNDS_SAMPLE,
    RACE_SAMPLE,
    _build_module,
    _page_functions,
    _run_js,
    _text,
    needs_node,
)
from tests.test_shadow_calibration import (
    C0,
    C1,
    C2,
    C3,
    C4,
    accepted,
    flat_frame,
    history,
    refused,
    snapshot_line,
    utc,
)

ROOT = Path(__file__).resolve().parents[1]
APPROVED = dataclasses.replace(calib.PASS_RULE, approved=True)
CLOSED = calib.MARKET_CLOSED


# --------------------------------------------------------------------------- #
# Builders
# --------------------------------------------------------------------------- #


class NewLine:
    """A journal line as the reader gives it once it exposes the new fields.

    Wraps a ``JournalEntry`` and adds ``outcome_reason`` and
    ``management_market_closed``, so these tests hold before and after the
    reader change whatever form it takes: calibration reads both through
    ``getattr``.
    """

    def __init__(self, entry: JournalEntry, outcome_reason: Optional[str] = None,
                 management_market_closed: Optional[bool] = None) -> None:
        self._entry = entry
        self.outcome_reason = outcome_reason
        self.management_market_closed = management_market_closed

    def __getattr__(self, name):
        return getattr(self._entry, name)


def jline(moment: str, ticker: str, bias: str = "BULLISH", conviction: float = 0.8, *, status: Optional[str] = None,
          held: bool = False, started: Optional[str] = None, reason: Optional[str] = None,
          management: Optional[bool] = None):
    """One journal line at ``moment`` (UTC). ``reason``/``management`` give it the reader's new fields."""
    run = {"trigger": "backup", "started_at": started + "+00:00"} if started else None
    if held:
        entry = JournalEntry(ticker=ticker, timestamp=utc(moment), timestamp_is_exact=True, held=True,
                             run_record=run)
    else:
        entry = JournalEntry(ticker=ticker, timestamp=utc(moment), timestamp_is_exact=True, bias=bias,
                             conviction=conviction, outcome_status=status, run_record=run)
    if reason is None and management is None:
        return entry
    return NewLine(entry, reason, management)


def closed_at(moment: str, ticker: str) -> str:
    """The live engine's refusal of ``ticker`` for a closed market, a moment before its journal line."""
    return refused(moment, ticker, "REJECTED", CLOSED)


def snaps_for(last: date, fills=(), positions=(), stops=(), seed_at: str = "2026-10-01T21:00:00Z",
              first: date = C0):
    """A seed after C0's close, and a later snapshot with the fills and a flat real close every session."""
    closes = {d.date(): 100_000.0 for d in pd.bdate_range(first, last)}
    return calib.load_snapshots([
        snapshot_line(seed_at, 100_000.0, positions=positions, stops=stops,
                      history=history({first: 100_000.0})),
        snapshot_line(f"{last.isoformat()}T23:00:00Z", 100_000.0, positions=positions, stops=stops,
                      fills=fills, history=history(closes)),
    ])


def flat_bars(*tickers: str, last: str = "2026-10-09") -> Bars:
    return Bars({t: flat_frame(last=last) for t in (*tickers, "VT")})


def run(snaps, entries, bars, audit=(), start: date = C0) -> calib.CalibrationResult:
    return calib.run_calibration(snaps, entries, bars, SimFeed(bars), start, 15, list(audit), frozenset())


def sim_fills(result, ticker: str):
    return [(f.day, f.kind, f.qty) for f in result.fund.broker.fills if f.ticker == ticker]


def json_of(result: calib.CalibrationResult, rule=calib.PASS_RULE) -> dict:
    evaluation = calib.evaluate_pass_rule(result, rule)
    return calib.calibration_json(result, calib.calibration_status(result, evaluation, rule), result.start,
                                  evaluation, None, rule)


# --------------------------------------------------------------------------- #
# Regular hours, on New York's clock
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("moment, inside", [
    ("2026-10-02T13:29:59", False),        # 09:29:59 New York: before the bell
    ("2026-10-02T13:30:00", True),         # the bell
    ("2026-10-02T19:59:59", True),
    ("2026-10-02T20:00:00", False),        # the close itself: the broker's clock already says shut
    ("2026-10-03T15:00:00", False),        # Saturday
    ("2026-11-26T15:00:00", False),        # Thanksgiving
    ("2026-11-27T17:59:00", True),         # the half day after it: 12:59 New York (EST)
    ("2026-11-27T18:30:00", False),        # 13:30 New York: past the 13:00 half-day close
    ("2026-11-25T18:30:00", True),         # the same hour on a full day
    ("2026-12-01T20:30:00", True),         # winter: 15:30 New York
    ("2026-12-01T21:00:00", False),        # winter: the 16:00 close
])
def test_regular_hours_are_new_yorks_with_its_half_days(moment, inside):
    assert calib.in_regular_hours(utc(moment)) is inside


# --------------------------------------------------------------------------- #
# Entries
# --------------------------------------------------------------------------- #


def test_a_pre_open_cycle_day_is_mirrored_not_traded():
    """C1's run went out at 08:35 New York. The real broker refused both
    entries; without the mirror the sim would buy both at C2's open."""
    entries = [jline("2026-10-02T12:35:00", "JPM", status="REJECTED"),
               jline("2026-10-02T12:35:01", "XOM", conviction=0.7, status="REJECTED")]
    audit = [closed_at("2026-10-02T12:35:00", "JPM"), closed_at("2026-10-02T12:35:01", "XOM")]

    result = run(snaps_for(C3), entries, flat_bars("JPM", "XOM"), audit)

    assert [(m.day, m.ticker, m.what) for m in result.mirrored] == [(C1, "JPM", "entry"), (C1, "XOM", "entry")]
    assert sim_fills(result, "JPM") == [] and sim_fills(result, "XOM") == []
    assert result.differences == []                     # neither book traded: not a difference
    mirrored = [d for d in result.decisions if d.status == calib.MIRRORED]
    assert [(d.session, d.cycle_day, d.ticker, d.dispatched, d.reason) for d in mirrored] == [
        (C2, C1, "JPM", True, calib.MIRROR_REASON), (C2, C1, "XOM", True, calib.MIRROR_REASON)]
    assert result.problems == []                        # 08:35 is not inside the schedule
    _, lines = calib.evaluate_pass_rule(result)
    assert "Note: 2 entries and 0 ladder passes mirrored on 1 day (limit 2)" in lines
    assert calib.calibration_status(result, (False, lines)) == "running"


def test_a_closed_market_refusal_during_the_session_is_never_mirrored():
    """12:00 New York and the broker said closed: the real account's clock at
    fault. The sim trades it, and the difference shows with its reason."""
    entries = [jline("2026-10-02T16:00:00", "JPM", status="REJECTED")]
    audit = [closed_at("2026-10-02T16:00:00", "JPM")]

    result = run(snaps_for(C3), entries, flat_bars("JPM"), audit)

    assert result.mirrored == []
    assert [(day, kind) for day, kind, _ in sim_fills(result, "JPM")] == [(C2, "entry")]
    [diff] = result.differences
    assert (diff.ticker, diff.real, diff.reason) == ("JPM", "none", "real rejected: market is closed")


def test_an_after_close_second_cycle_is_mirrored_and_the_first_is_traded():
    """Cycle 1 at 11:10 New York bought JPM; a second run at 16:30 was refused
    XOM. The sim buys JPM at C2 (a session later: timing) and not XOM."""
    entries = [
        jline("2026-10-02T15:10:00", "JPM", status="ACCEPTED", management=False),
        jline("2026-10-02T15:10:01", "XOM", bias="NEUTRAL", conviction=0.0, status="REJECTED", management=False),
        jline("2026-10-02T20:30:00", "JPM", held=True, management=True),
        jline("2026-10-02T20:30:01", "XOM", status="REJECTED", reason=CLOSED, management=True),
    ]
    audit = [accepted("2026-10-02T15:10:00", "JPM", "buy", 49, 100.0, 96.0),
             refused("2026-10-02T15:10:01", "XOM", "REJECTED", "bias is NEUTRAL; no trade")]
    fills = [("f1", "o-jpm", "JPM", "buy", 49, 100.0, "2026-10-02T15:10:30Z")]

    result = run(snaps_for(C3, fills=fills), entries, flat_bars("JPM", "XOM"), audit)

    assert [(m.day, m.ticker, m.what) for m in result.mirrored] == [(C1, "XOM", "entry")]
    # One cycle of the day managed, so the copy manages: no ladder pass is mirrored.
    assert not [m for m in result.mirrored if m.what == calib.MIRROR_LADDER]
    assert [(day, kind) for day, kind, _ in sim_fills(result, "JPM")] == [(C2, "entry")]
    assert sim_fills(result, "XOM") == []
    jpm = [m for m in result.matches if m.real.ticker == "JPM"]
    assert len(jpm) == 1 and jpm[0].lag
    assert "XOM" not in {d.ticker for d in result.differences}
    # No run block says when the second run started; the day's first line
    # (11:10, inside the schedule) is another run's, and blames no guard.
    assert not [p for p in result.problems if calib.SCHEDULE_GUARD in p]


@pytest.mark.parametrize("started, flagged", [
    ("2026-10-02T19:30:00", False),        # 15:30 New York: past the latest safe start, the guard's to refuse
    ("2026-10-02T18:00:00", True),         # 14:00 New York: inside the schedule, and it still ran past the close
])
def test_a_run_straddling_the_close_mirrors_only_what_came_after_it(started, flagged):
    entries = [
        jline("2026-10-02T19:50:00", "JPM", status="ACCEPTED", started=started),
        jline("2026-10-02T20:05:00", "XOM", status="REJECTED", started=started),
    ]
    audit = [accepted("2026-10-02T19:50:00", "JPM", "buy", 49, 100.0, 96.0),
             closed_at("2026-10-02T20:05:00", "XOM")]
    fills = [("f1", "o-jpm", "JPM", "buy", 49, 100.0, "2026-10-02T19:50:30Z")]

    result = run(snaps_for(C3, fills=fills), entries, flat_bars("JPM", "XOM"), audit)

    assert [(m.ticker, m.what) for m in result.mirrored] == [("XOM", "entry")]
    assert [(day, kind) for day, kind, _ in sim_fills(result, "JPM")] == [(C2, "entry")]
    notes = [p for p in result.problems if calib.SCHEDULE_GUARD in p]
    if flagged:
        assert notes == ["2026-10-02: late-run mirroring was needed for a cycle that started at 14:00 New York, "
                         "inside the schedule: the schedule guard should have prevented this"]
        _, lines = calib.evaluate_pass_rule(result)
        assert f"Note: {notes[0]}" in lines
    else:
        assert notes == []


@pytest.mark.parametrize("early_bias", ["BULLISH", "BEARISH"])
def test_a_refused_line_is_mirrored_and_the_days_accepted_line_trades(early_bias):
    """Refused before the open (the clock read failed and the run went out at
    08:35), then bought by the day's own run at 11:00. The mirror goes line by
    line: the refused line is not traded, the accepted one is. Were the
    refused line traded instead, the sim would make the stale call first --
    a short, when it said BEARISH -- and skip the line that really traded as
    "already held"."""
    entries = [jline("2026-10-02T12:35:00", "XOM", bias=early_bias, status="REJECTED"),
               jline("2026-10-02T15:00:00", "XOM", status="ACCEPTED")]
    audit = [closed_at("2026-10-02T12:35:00", "XOM"), accepted("2026-10-02T15:00:00", "XOM", "buy", 49, 100.0, 96.0)]
    fills = [("f1", "o-xom", "XOM", "buy", 49, 100.0, "2026-10-02T15:00:30Z")]

    result = run(snaps_for(C3, fills=fills), entries, flat_bars("XOM"), audit)

    # The early run met a closed market: that day counts against the limit.
    assert [(m.day, m.ticker, m.what) for m in result.mirrored] == [(C1, "XOM", "entry")]
    assert [(f.day, f.kind, f.side) for f in result.fund.broker.fills if f.ticker == "XOM"] == [(C2, "entry", "buy")]
    assert [(d.bias, d.status) for d in result.decisions if d.ticker == "XOM"] == [
        (early_bias, calib.MIRRORED), ("BULLISH", "ACCEPTED")]
    assert [m.lag for m in result.matches if m.real.ticker == "XOM"] == [True]
    assert result.differences == []


def test_a_real_fill_no_line_explains_is_shown_not_matched_away():
    """Refused before the open, and then XOM was bought with no journal line
    behind it (a trade by hand). The refused line is still mirrored, so the
    real buy is a difference that reads "unexplained", never a match with a
    stale refused line."""
    entries = [jline("2026-10-02T12:35:00", "XOM", status="REJECTED")]
    audit = [closed_at("2026-10-02T12:35:00", "XOM")]
    fills = [("f1", "o-hand", "XOM", "buy", 49, 100.0, "2026-10-02T15:00:30Z")]

    result = run(snaps_for(C3, fills=fills), entries, flat_bars("XOM"), audit)

    assert [(m.day, m.ticker) for m in result.mirrored] == [(C1, "XOM")]
    assert sim_fills(result, "XOM") == []
    [diff] = result.differences
    assert (diff.day, diff.ticker, diff.sim, diff.reason) == (C1, "XOM", "none", calib.UNEXPLAINED)


def test_a_sim_trade_the_other_way_is_never_a_match():
    """A real buy and a sim short sale both open a position, but they are
    opposite bets: never "the same trade a session apart"."""
    real = [calib.Trade(C1, "XOM", calib.OPEN, "buy", 49, 100.0, frozenset({"market"}))]
    short = calib.Trade(C2, "XOM", calib.OPEN, "sell", 50, 100.0, frozenset({calib.ENTRY}))
    long_ = dataclasses.replace(short, side="buy")
    order = [C0, C1, C2, C3]
    assert calib.match_trades(real, [short], order) == []
    assert calib.match_trades(real, [short, long_], order) == [calib.Match(real[0], long_)]
    # Closing a long (a sell) is not covering a short (a buy) either.
    sold = calib.Trade(C1, "XOM", calib.REDUCE, "sell", 49, 104.0, frozenset({"market"}))
    covered = calib.Trade(C1, "XOM", calib.REDUCE, "buy", 49, 104.0, frozenset({calib.TRANCHE}))
    assert calib.match_trades([sold], [covered], order) == []


def test_a_long_and_a_short_opened_the_same_day_are_two_trades():
    """Bought, stopped out, then sold short, all on C1: two openings, one
    each way, not one "buy of 15" lumped under the side that came first."""
    seed = calib.Seed(C0, utc("2026-10-01T21:00:00"), 100_000.0, (), ())
    fills = [calib.AccountFill("f1", "o1", "XOM", "buy", 10, 100.0, utc("2026-10-02T14:00:00")),
             calib.AccountFill("f2", "o2", "XOM", "sell", 10, 95.0, utc("2026-10-02T16:00:00")),
             calib.AccountFill("f3", "o3", "XOM", "sell_short", 5, 94.0, utc("2026-10-02T18:00:00"))]
    trades = calib.real_trades(seed, fills, utc("2026-10-01T21:00:00"), C1, C1)
    assert [(t.direction, t.side, t.qty) for t in trades] == [
        (calib.OPEN, "buy", 10), (calib.OPEN, "sell", 5), (calib.REDUCE, "sell", 10)]


def test_a_sim_that_flips_a_calls_direction_fails_the_trade_match():
    """End to end, with the mirror out of the way: the real account bought
    XOM on C1 and the sim, on a line that said BEARISH, sold it short at C2's
    open. Both trades are differences, and the real one reads "unexplained"."""
    entries = [jline("2026-10-02T15:00:00", "XOM", bias="BEARISH", status="ACCEPTED")]
    audit = [accepted("2026-10-02T15:00:00", "XOM", "buy", 49, 100.0, 96.0)]
    fills = [("f1", "o-xom", "XOM", "buy", 49, 100.0, "2026-10-02T15:00:30Z")]

    result = run(snaps_for(C3, fills=fills), entries, flat_bars("XOM"), audit)

    assert [(f.day, f.side) for f in result.fund.broker.fills if f.ticker == "XOM"] == [(C2, "sell")]
    assert result.matches == []
    assert sorted((d.real != "none", d.reason) for d in result.differences) == [
        (False, calib.UNEXPLAINED), (True, calib.UNEXPLAINED)]
    _, lines = calib.evaluate_pass_rule(result, APPROVED)
    assert any(line.startswith("4. no unexplained difference: FAIL") for line in lines)


def test_a_mirrored_line_the_real_account_then_fills_is_unexplained():
    """Mirrored after C1's close; then the real account bought XOM on C2 with
    no line to say why. That must fail condition 4 loudly."""
    entries = [jline("2026-10-02T20:30:00", "XOM", status="REJECTED")]
    audit = [closed_at("2026-10-02T20:30:00", "XOM")]
    fills = [("f1", "o-xom", "XOM", "buy", 49, 100.0, "2026-10-05T14:00:00Z")]    # after the copy's C2 open

    result = run(snaps_for(C3, fills=fills), entries, flat_bars("XOM"), audit)

    assert [(m.ticker, m.what) for m in result.mirrored] == [("XOM", "entry")]
    [diff] = [d for d in result.differences if d.ticker == "XOM"]
    assert (diff.day, diff.sim, diff.reason) == (C2, "none", calib.UNEXPLAINED)
    passed, lines = calib.evaluate_pass_rule(result, APPROVED)
    assert not passed and any(line.startswith("4. no unexplained difference: FAIL") for line in lines)
    assert calib.calibration_status(result, (passed, lines), APPROVED) == "failed"


def test_a_mirrored_decision_counts_as_dispatched_so_a_real_fill_is_never_held_away():
    """A MIRRORED line is recorded as dispatched: a real fill answered by it
    reads "unexplained". Recorded as a skip it would read "sim held it
    already" and pass condition 4 quietly."""
    trade = calib.Trade(C1, "XOM", calib.OPEN, "buy", 49, 100.0, frozenset({"market"}))
    mirrored = Decision(C2, C1, "XOM", "BULLISH", 0.8, calib.MIRRORED, calib.MIRROR_REASON)
    skipped = dataclasses.replace(mirrored, status="SKIPPED", reason="already held", dispatched=False)
    assert mirrored.dispatched is True
    assert calib._why_real_only(trade, [mirrored]) == calib.UNEXPLAINED
    assert calib._why_real_only(trade, [skipped]) == calib.SIM_HELD


def test_a_half_day_line_at_13_30_new_york_is_mirrored():
    """27 Nov 2026 closes at 13:00. C0 is 25 Nov, Thanksgiving is shut, the
    half day is C1 and Monday 30 Nov is C2."""
    c0, c1, c2 = date(2026, 11, 25), date(2026, 11, 27), date(2026, 11, 30)
    entries = [jline("2026-11-27T18:30:00", "JPM", status="REJECTED")]          # 13:30 EST
    audit = [closed_at("2026-11-27T18:30:00", "JPM")]
    snaps = snaps_for(date(2026, 12, 1), seed_at="2026-11-25T22:00:00Z", first=c0)
    bars = flat_bars("JPM", last="2026-12-04")

    result = run(snaps, entries, bars, audit, start=c0)

    assert c1 in [p.day for p in result.series] and date(2026, 11, 26) not in [p.day for p in result.series]
    assert [(m.day, m.ticker) for m in result.mirrored] == [(c1, "JPM")]
    assert sim_fills(result, "JPM") == []
    assert [d.session for d in result.decisions if d.status == calib.MIRRORED] == [c2]


def test_journal_lines_as_the_cycle_writes_them_are_mirrored_on_their_own_word():
    """The journal's own ``outcome.reason`` and ``management`` record, read
    by the reader, with no audit log at all: the late run is mirrored, entry
    and ladder pass. Skipped until the reader exposes those fields."""
    from analysis.reader import read_lines

    if not hasattr(JournalEntry, "outcome_reason") or not hasattr(JournalEntry, "management_market_closed"):
        pytest.skip("the reader does not expose outcome_reason and management_market_closed yet")

    def written(moment, ticker, reason, bias="BULLISH"):
        return json.dumps({"ts_utc": moment + "+00:00", "ticker": ticker,
                           "signal": {"ticker": ticker, "bias": bias, "conviction": 0.8},
                           "outcome": {"mode": "direct", "status": "REJECTED", "reason": reason},
                           "management": {"market_closed": True}, "held": False, "error": None})

    entries = read_lines([written("2026-10-02T20:30:00", "JPM", CLOSED),
                          written("2026-10-02T20:30:01", "XOM", "bias is NEUTRAL; no trade", bias="NEUTRAL")]).entries

    result = run(snaps_for(C3), entries, flat_bars("JPM", "XOM"))

    assert [(m.day, m.ticker, m.what) for m in result.mirrored] == [(C1, "JPM", "entry"), (C1, None, "ladder pass")]
    assert sim_fills(result, "JPM") == [] and result.differences == []


def test_the_audit_join_takes_the_latest_record_at_or_before_the_line_within_five_minutes():
    late = calib.LateRuns([], [
        refused("2026-10-02T20:20:00", "XOM", "REJECTED", CLOSED),               # 10 minutes before: too early
        refused("2026-10-02T20:28:00", "JPM", "REJECTED", CLOSED),
        refused("2026-10-02T20:31:00", "LQD", "REJECTED", CLOSED),               # after the line: not its answer
        refused("2026-10-02T20:29:00", "JPM", "REJECTED", "bias is NEUTRAL; no trade"),
    ])
    assert late.engine_answer(jline("2026-10-02T20:30:00", "XOM")) == (None, None, None)
    assert late.engine_answer(jline("2026-10-02T20:30:00", "LQD")) == (None, None, None)
    status, reason, when = late.engine_answer(jline("2026-10-02T20:30:00", "JPM"))
    assert (status, reason, when) == ("REJECTED", "bias is NEUTRAL; no trade", utc("2026-10-02T20:29:00"))
    # The reader's own reason, when a line carries it, wins over the log.
    new = jline("2026-10-02T20:30:00", "JPM", status="REJECTED", reason=CLOSED)
    assert late.engine_answer(new) == ("REJECTED", CLOSED, utc("2026-10-02T20:30:00"))


def test_a_reworded_refusal_or_an_accepted_line_is_not_mirrored():
    entries = [jline("2026-10-02T20:30:00", "JPM", status="REJECTED", reason="market is closed today"),
               jline("2026-10-02T20:30:01", "XOM", status="ACCEPTED", reason=CLOSED)]

    result = run(snaps_for(C3), entries, flat_bars("JPM", "XOM"))

    assert result.mirrored == []


# --------------------------------------------------------------------------- #
# The ladder pass
# --------------------------------------------------------------------------- #


def ladder_case(management: Optional[bool]) -> calib.CalibrationResult:
    """NVDA held from 100 with a stop at 96 (R = 4); from C2 it opens at 105,
    past the first rung. C1's run went out at 17:00 New York, after the close,
    and its management pass was skipped: the real account took no rung."""
    frame = flat_frame()
    later = frame.index >= pd.Timestamp(C2)
    frame.loc[later, ["Open", "Close"]] = 105.0
    frame.loc[later, "High"], frame.loc[later, "Low"] = 106.0, 104.0
    bars = Bars({"NVDA": frame, "JPM": flat_frame(), "VT": flat_frame()})
    position = [("NVDA", 50, 100.0)]
    stops = [("s-nvda", "NVDA", 50, 96.0, "sell")]
    entries = [jline("2026-10-02T21:00:00", "JPM", bias="NEUTRAL", conviction=0.0, status="REJECTED",
                     management=management),
               jline("2026-10-02T21:00:01", "NVDA", held=True, management=management)]
    audit = [accepted("2026-09-25T15:30:00", "NVDA", "buy", 50, 100.0, 96.0),
             refused("2026-10-02T21:00:00", "JPM", "REJECTED", "bias is NEUTRAL; no trade")]
    return run(snaps_for(C3, positions=position, stops=stops), entries, bars, audit)


def test_a_ladder_pass_the_real_account_could_not_run_is_skipped_on_the_journals_word():
    result = ladder_case(True)

    assert [(m.day, m.ticker, m.what) for m in result.mirrored] == [(C1, None, "ladder pass")]
    assert result.mirrored[0].at == utc("2026-10-02T21:00:00")
    assert sim_fills(result, "NVDA") == []
    assert result.differences == []
    out = json_of(result)
    assert out["mirrored"] == [{"day": "2026-10-02", "ticker": None, "at": "2026-10-02T21:00:00+00:00",
                                "what": "ladder pass", "reason": "late run: real market closed, mirrored"}]
    assert "Note: 0 entries and 1 ladder pass mirrored on 1 day (limit 2)" in out["pass_rule"]["verdicts"]


@pytest.mark.parametrize("management", [None, False])
def test_without_the_journals_word_the_ladder_pass_runs(management):
    """A line with no field (an older line) is never read as a skip: the
    copy manages, takes the rung, and the difference shows with its reason."""
    result = ladder_case(management)

    assert result.mirrored == []
    assert [(day, kind) for day, kind, _ in sim_fills(result, "NVDA")] == [(C2, "close")]      # a ladder rung
    assert [(d.ticker, d.reason) for d in result.differences] == [("NVDA", calib.LADDER)]


def test_a_day_is_skipped_only_when_every_line_of_it_says_so():
    lines = [jline("2026-10-02T21:00:00", "JPM", management=True),
             jline("2026-10-02T21:00:01", "XOM", management=True)]
    assert calib.LateRuns(lines, []).management_skipped(C1)
    assert not calib.LateRuns(lines + [jline("2026-10-02T21:00:02", "LQD")], []).management_skipped(C1)
    assert not calib.LateRuns(lines + [jline("2026-10-02T15:00:00", "LQD", management=False)], []) \
        .management_skipped(C1)
    assert not calib.LateRuns([], []).management_skipped(C1)


# --------------------------------------------------------------------------- #
# The owner's limit: more than 2 days stops calibration
# --------------------------------------------------------------------------- #


def late_days(*days: date) -> tuple[list, list]:
    """A run after the close (16:30 New York) on each day, its one entry refused for a closed market."""
    entries, audit = [], []
    for day in days:
        moment = f"{day.isoformat()}T20:30:00"
        entries.append(jline(moment, "JPM", status="REJECTED"))
        audit.append(closed_at(moment, "JPM"))
    return entries, audit


class Fetcher:
    def ohlc(self, ticker, start, end):
        return flat_frame()


def report(days: tuple[date, ...], last_close: date = C4) -> dict:
    entries, audit = late_days(*days)
    return calib.calibration_report(snapshots=snaps_for(last_close), entries=entries, audit_lines=audit, start=C0,
                                    final_through=last_close, fetcher=Fetcher(), holding=None)


def test_a_third_late_day_stops_calibration_the_night_it_is_journalled():
    """Late runs on C1, C2 and C3, and the real closes only through C3: the
    sim has not reached C3's cycle (it acts on it at C4's open, once C4's
    close is in). The day is counted from the record anyway, so the nightly
    record says "stopped" now, not two or three sessions later."""
    out = report((C1, C2, C3), last_close=C3)

    assert out["status"] == "stopped"
    assert out["mirrored_days"] == ["2026-10-02", "2026-10-05", "2026-10-06"]
    assert out["end_estimate"] is None and out["fund_test_plan"] is None


def test_a_day_counted_ahead_is_the_same_day_once_the_sim_reaches_it():
    entries, audit = late_days(C1, C2, C3)
    bars = flat_bars("JPM")
    ahead = run(snaps_for(C3), entries, bars, audit)
    reached = run(snaps_for(C4), entries, bars, audit)

    assert ahead.mirrored == reached.mirrored                           # counted once, the same way
    # Only a day the sim has reached leaves a decision behind: C3's line is
    # decided at C4's open, which the first run has not got to.
    assert [(d.session, d.cycle_day) for d in ahead.decisions if d.status == calib.MIRRORED] == [(C2, C1), (C3, C2)]
    assert [(d.session, d.cycle_day) for d in reached.decisions if d.status == calib.MIRRORED] == [
        (C2, C1), (C3, C2), (C4, C3)]
    assert sim_fills(ahead, "JPM") == [] and sim_fills(reached, "JPM") == []


@pytest.mark.parametrize("days_needed, counted", [(3, [C1, C2]), (4, [C1, C2, C3])])
def test_only_days_the_copy_acts_on_within_calibration_are_counted(days_needed, counted):
    """C0's cycle is in the seed, and a cycle on the last calibration day is
    acted on only after calibration ends: neither is copied, so neither
    counts. With three closes needed and three compared, C3 is the last day;
    with four needed, the sim will act on C3's cycle at C4's open."""
    entries, audit = late_days(C0, C1, C2, C3)
    bars = flat_bars("JPM")
    result = calib.run_calibration(snaps_for(C3), entries, bars, SimFeed(bars), C0, days_needed, audit, frozenset())
    assert result.mirrored_days == counted


def test_a_late_day_journalled_before_any_real_close_is_counted():
    """The first night: no real close after C0 yet, so the sim runs no
    session at all. C1's late run is counted all the same."""
    entries, audit = late_days(C1)
    bars = flat_bars("JPM")
    snaps = calib.load_snapshots([snapshot_line("2026-10-01T21:00:00Z", 100_000.0,
                                                history=history({C0: 100_000.0}))])
    result = run(snaps, entries, bars, audit)
    assert result.series == [] and [(m.day, m.ticker) for m in result.mirrored] == [(C1, "JPM")]


def test_two_late_days_are_mirrored_and_calibration_runs_on():
    out = report((C1, C2))

    assert out["status"] == "running"
    assert (out["mirrored_days"], out["mirrored_day_count"], out["mirror_limit"]) == (["2026-10-02", "2026-10-05"],
                                                                                    2, 2)
    assert out["stop_reason"] is None
    assert out["end_estimate"] is not None and out["fund_test_plan"] is not None
    assert out["differences"] == []
    assert "Note: 2 entries and 0 ladder passes mirrored on 2 days (limit 2)" in out["pass_rule"]["verdicts"]
    json.dumps(out, allow_nan=False)


def test_a_third_late_day_stops_calibration():
    out = report((C1, C2, C3))

    assert out["status"] == "stopped"
    assert out["mirrored_day_count"] == 3 and len(out["mirrored"]) == 3
    assert out["stop_reason"] == (
        "late-run copying was needed on 3 calibration days (limit 2): this is a schedule problem to fix, not "
        "something to copy around; calibration is stopped until the owner decides")
    # Neither a pass nor a fail, no end date, no fund test start from it.
    assert out["end_estimate"] is None and out["fund_test_plan"] is None
    verdicts = out["pass_rule"]["verdicts"]
    assert f"Stopped: {out['stop_reason']}. A stopped calibration neither passes nor fails." in verdicts
    assert "Note: 3 entries and 0 ladder passes mirrored on 3 days (limit 2)" in verdicts
    assert out["differences"] == []                     # shown, but never a difference
    json.dumps(out, allow_nan=False)


def test_stopped_wins_over_passed_and_failed():
    """A stopped calibration gives neither, whatever its conditions read."""
    def mirrored(n):
        return [calib.Mirrored(day, "JPM", calib.close_of(day), calib.MIRROR_ENTRY)
                for day in (C1, C2, C3, C4)[:n]]

    from tests.test_shadow_calibration import crafted

    clean, broken = crafted(), crafted(worst=0.03)
    assert calib.calibration_status(clean, calib.evaluate_pass_rule(clean, APPROVED), APPROVED) == "passed"
    for result in (clean, broken):
        result.mirrored = mirrored(3)
        passed, lines = calib.evaluate_pass_rule(result, APPROVED)
        assert not passed and calib.is_stopped(result, APPROVED)
        assert calib.calibration_status(result, (passed, lines), APPROVED) == "stopped"
    clean.mirrored = mirrored(2)
    assert calib.calibration_status(clean, calib.evaluate_pass_rule(clean, APPROVED), APPROVED) == "passed"
    assert calib.stop_reason(clean) is None and calib.stop_reason(None) is None


def test_the_shadow_run_does_not_run_the_funds_on_a_stopped_calibration(monkeypatch, tmp_path):
    """Only "passed" starts the funds (``shadow.run.build``)."""
    from types import SimpleNamespace

    from shadow import run as shadow_run
    from shadow import schedule

    stopped = {"status": "stopped"}
    monkeypatch.setattr(schedule, "CALIBRATION_START", C0)
    monkeypatch.setattr(schedule, "FUND_START", C1)
    monkeypatch.setattr(calib, "calibration_report", lambda **kw: stopped)
    called = []
    monkeypatch.setattr(shadow_run, "run_funds", lambda *a, **kw: called.append(1))

    class NoPrices:                                     # the price-gap report fetches; no network here
        def __init__(self, **kw):
            pass

        def ohlc(self, ticker, start, end):
            return pd.DataFrame()

    monkeypatch.setattr(shadow_run, "OhlcFetcher", NoPrices)
    journal = tmp_path / "journal.log"
    journal.write_text("")
    args = SimpleNamespace(journal=journal, audit=tmp_path / "audit.log", account=tmp_path / "account.jsonl",
                           random=1, processes=1)
    out = shadow_run.build(args, datetime(2026, 10, 9, 23, 0, tzinfo=timezone.utc))
    assert out["calibration"] is stopped and out["funds"] is None and called == []
    assert out["fund_test"]["status"] == "not_started"


# --------------------------------------------------------------------------- #
# Nothing else changes: the funds, the race, and a calibration with no late run
# --------------------------------------------------------------------------- #


def test_the_manage_switch_defaults_to_the_old_session():
    params = inspect.signature(Fund.session).parameters
    assert params["manage"].default is True
    assert "manage" not in inspect.signature(IndexFund.session).parameters


def synthetic_funds() -> dict:
    """The six funds and two coin-flip funds through ``shadow.run`` on made-up bars and lines."""
    import random

    import numpy as np

    from config.watchlist import DEFAULT_WATCHLIST
    from shadow import run as shadow_run

    rng = np.random.default_rng(7)
    tickers = list(DEFAULT_WATCHLIST)[:8]
    days = pd.bdate_range("2026-03-02", "2026-09-18")
    frames = {}
    for t in sorted(set(tickers) | {"VT", "SPY"}):
        close = 100 * np.exp(np.cumsum(rng.normal(0.0008, 0.02, len(days))))
        opened = close * np.exp(rng.normal(0, 0.006, len(days)))
        high = np.maximum(opened, close) * (1 + np.abs(rng.normal(0, 0.01, len(days))))
        low = np.minimum(opened, close) * (1 - np.abs(rng.normal(0, 0.01, len(days))))
        frames[t] = pd.DataFrame({"Open": opened, "High": high, "Low": low, "Close": close, "Dividends": 0.0},
                                 index=days)

    class Frames:
        def ohlc(self, ticker, start, end):
            return frames.get(ticker, pd.DataFrame())

    pick = random.Random(3)
    entries = []
    for day in pd.bdate_range("2026-08-17", "2026-09-17"):
        for i, t in enumerate(tickers):
            stamp = datetime(day.year, day.month, day.day, 15, 10, tzinfo=timezone.utc) + timedelta(seconds=i)
            q = pick.uniform(-0.3, 0.3)
            tech = {"last_close": 100.0, "return_63d": q, "distance_sma50": q / 3 + pick.uniform(-0.03, 0.03),
                    "annualised_volatility": 0.3, "atr_pct_of_price": 0.02}
            entries.append(JournalEntry(ticker=t, timestamp=stamp, timestamp_is_exact=True,
                                        bias=pick.choice(["BULLISH", "BULLISH", "BEARISH", "NEUTRAL"]),
                                        conviction=round(pick.uniform(0.2, 0.8), 2), technicals=tech,
                                        scores={"news_score": pick.uniform(-1, 1)}))
    funds, checks = shadow_run.run_funds(entries, date(2026, 8, 24), date(2026, 9, 18), Frames(), random_funds=2,
                                         processes=1, shortable_no=frozenset())
    return {"funds": funds, "checks": checks}


def test_every_fund_is_the_same_with_the_manage_switch_left_alone(monkeypatch):
    """The funds call ``session(day, cycle)``; the old session is
    ``session(day, cycle, manage=True)``. Run both ways, the record is the
    same to the byte, and every fund still manages on every cycle."""
    plain = json.dumps(synthetic_funds(), sort_keys=True, allow_nan=False)

    session, calls = Fund.session, []

    def explicit(self, day, cycle, manage=True, today=None):
        calls.append(manage)
        return session(self, day, cycle, manage=True, today=today)

    monkeypatch.setattr(Fund, "session", explicit)
    forced = json.dumps(synthetic_funds(), sort_keys=True, allow_nan=False)

    assert forced == plain
    assert calls and all(calls)                         # no fund ever asked to skip its pass
    record = json.loads(plain)["funds"]
    assert {f["name"] for f in record["list"]} == {"model", "momentum", "hybrid", "vt", "model_by_conviction",
                                                   "model_sized", "model_same_day"}
    assert sum(f["trades"] for f in record["list"]) > 20            # the funds did trade


def test_the_race_cannot_see_calibration():
    """The race and the rule arms import nothing from shadow/: the mirror
    cannot reach them."""
    for path in [ROOT / "analysis" / "horse_race.py", ROOT / "analysis" / "decision_gate.py",
                 *sorted((ROOT / "rules").glob("*.py"))]:
        text = path.read_text()
        assert "from shadow" not in text and "import shadow" not in text, path


def test_a_calibration_with_no_late_run_is_the_same_with_and_without_the_mirror(monkeypatch):
    """``test_shadow_calibration``'s scenario, every run inside the session:
    the mirror finds nothing, and the record is what it was without it."""
    from tests.test_shadow_calibration import run as run_scenario
    from tests.test_shadow_calibration import scenario

    def record(result):
        out = json_of(result)
        return json.dumps({k: v for k, v in out.items()
                           if k not in ("mirrored", "mirrored_days", "mirrored_day_count", "mirror_limit",
                                        "stop_reason")}, sort_keys=True, allow_nan=False)

    with_mirror = run_scenario(scenario())
    assert with_mirror.mirrored == []

    monkeypatch.setattr(calib.LateRuns, "cycle", lambda self, day, session, lines, fund=None: (list(lines), True))
    without = run_scenario(scenario())

    assert record(with_mirror) == record(without)
    assert [(f.day, f.ticker, f.kind, f.qty, f.price) for f in with_mirror.fund.broker.fills] == \
        [(f.day, f.ticker, f.kind, f.qty, f.price) for f in without.fund.broker.fills]


def test_calibration_before_the_start_says_nothing_was_mirrored():
    out = calib.calibration_json(None, "not_started", None, None, None)
    assert (out["mirrored"], out["mirrored_days"], out["mirrored_day_count"], out["mirror_limit"],
            out["stop_reason"]) == ([], [], 0, 2, None)


# --------------------------------------------------------------------------- #
# It reaches the owner: the health check, the brief, the 4 Funds page
# --------------------------------------------------------------------------- #


def health_logs(tmp_path, funds: Optional[object]) -> tuple[Path, Path]:
    journal, audit = tmp_path / "signal_journal.log", tmp_path / "execution_audit.log"
    journal.write_text(json.dumps({"ticker": "JPM", "ts_utc": "2026-10-09T15:48:00+00:00",
                                   "signal": {"ticker": "JPM", "bias": "NEUTRAL", "conviction": 0.2},
                                   "outcome": {"status": "REJECTED", "reason": "bias is NEUTRAL; no trade"},
                                   "context": {"ticker": "JPM", "gaps": []}}) + "\n")
    audit.write_text("")
    if funds is not None:
        (tmp_path / "funds.json").write_text(funds if isinstance(funds, str) else json.dumps(funds))
    return journal, audit


STOPPED = {"final_through": "2026-10-08", "simulated": True,
           "calibration": {"status": "stopped", "mirrored_day_count": 3, "mirror_limit": 2,
                           "stop_reason": "late-run copying was needed on 3 calibration days (limit 2): this is a "
                                          "schedule problem to fix, not something to copy around; calibration is "
                                          "stopped until the owner decides"}}


def test_a_stopped_calibration_is_a_warning_in_the_daily_health_check(tmp_path):
    from analysis import health

    journal, audit = health_logs(tmp_path, STOPPED)
    alarms = health.check(journal, audit, date(2026, 10, 9))

    [alarm] = alarms
    assert alarm.severity == health.WARNING and not alarm.is_critical         # never turns the trading run red
    assert alarm.title == "Calibration stopped: late runs on 3 days (limit 2)"
    assert "schedule problem to fix" in alarm.detail and "until the owner decides" in alarm.detail
    assert health.exit_code(alarms) == 1
    assert "Calibration stopped" in health.render(alarms, date(2026, 10, 9))
    # The CLI reads the same file, or the one it is pointed at.
    other = tmp_path / "elsewhere.json"
    other.write_text(json.dumps({"calibration": {"status": "running"}}))
    assert health.main(["--journal", str(journal), "--audit", str(audit), "--day", "2026-10-09"]) == 1
    assert health.main(["--journal", str(journal), "--audit", str(audit), "--day", "2026-10-09",
                        "--funds", str(other)]) == 0


@pytest.mark.parametrize("funds", [
    None, "not json", "[1, 2]", {"calibration": {"status": "running"}}, {"calibration": "stopped"},
    {"calibration": {"status": "failed"}},
])
def test_no_stop_no_alarm(tmp_path, funds):
    from analysis import health

    journal, audit = health_logs(tmp_path, funds)
    assert health.check(journal, audit, date(2026, 10, 9)) == []


def test_the_stop_heads_the_brief_that_goes_to_the_phone(tmp_path):
    """The heartbeat writes the book, the brief reads its alarms, and the
    phone step sends the brief: the first warning is the headline."""
    from analysis import book, brief

    journal, audit = health_logs(tmp_path, STOPPED)
    snapshot = book.build(audit, journal, date(2026, 10, 9))
    text = brief.compose(snapshot, date(2026, 10, 9))
    assert text.splitlines()[0] == "🟡 1 warning: Calibration stopped: late runs on 3 days (limit 2)"




@pytest.fixture(scope="module")
def funds_page(tmp_path_factory):
    """The 4 Funds page as the site build writes it, with the dashboard tests' own samples."""
    folder = tmp_path_factory.mktemp("funds-page")
    funds, race = folder / "funds.json", folder / "race_gate.json"
    funds.write_text(json.dumps(FUNDS_SAMPLE))
    race.write_text(json.dumps(RACE_SAMPLE))
    return _build_module().build_funds(ROOT / "dashboard" / "funds.html", funds, race)

MIRRORED_ITEMS = [
    {"day": "2026-10-02", "ticker": "XOM", "at": "2026-10-02T20:30:00+00:00", "what": "entry",
     "reason": "late run: real market closed, mirrored"},
    {"day": "2026-10-05", "ticker": None, "at": "2026-10-05T21:00:00+00:00", "what": "ladder pass",
     "reason": "late run: real market closed, mirrored"},
    {"day": "2026-10-06", "ticker": "<b>JPM</b>", "at": "2026-10-06T20:30:00+00:00", "what": "entry",
     "reason": "late run: real market closed, mirrored"},
]


def calibration_record(status: str, items, **extra) -> dict:
    days = sorted({m["day"] for m in items})
    return {"calibration": {
        "status": status, "start": "2026-10-01", "days_done": 4, "days_needed": 15, "days_passed": 4,
        "fixes": [], "last_fix": None, "days_since_fix": None, "days_after_fix_needed": 5,
        "end_estimate": "2026-10-22" if status != "stopped" else None,
        "fund_test_plan": {"start": "2026-10-23", "bars": [3.8, 2.5, 2.0], "registered": [3.8, 2.5, 2.0],
                           "registered_start": "2026-10-19", "matches_registered": False},
        "pass_rule": {"text": list(calib.PASS_RULE.text), "approved": True,
                      "verdicts": ["Approved rule: 4 of 15 closes compared.",
                                   "1. every close within 1.00%: FAIL (worst 1.42% on 2026-10-03)"]},
        "series": [], "differences": [], "metrics": {}, "holding_days": {},
        "mirrored": items, "mirrored_days": days, "mirrored_day_count": len(days), "mirror_limit": 2,
        "stop_reason": STOPPED["calibration"]["stop_reason"] if status == "stopped" else None,
        **extra}}


@needs_node
def test_the_calibration_card_shows_a_stop_and_every_mirrored_item(tmp_path, funds_page):
    stopped = calibration_record("stopped", MIRRORED_ITEMS)
    running = calibration_record("running", MIRRORED_ITEMS[:1])
    older = calibration_record("running", [])
    for key in ("mirrored", "mirrored_days", "mirrored_day_count", "mirror_limit", "stop_reason"):
        del older["calibration"][key]
    source = _page_functions(funds_page, "verdictRow", "ruleHtml", "verdictsHtml", "calibrationFixHtml",
                             "renderCalibration")
    pages = _run_js(tmp_path, source, "CASES.map(c=>{ renderCalibration(c); return $(\"calibration\").innerHTML; })",
                    [stopped, running, older])

    page, text = pages[0], _text(pages[0])
    assert '<span class="chip bad">stopped</span>' in page
    assert "Why: late-run copying was needed on 3 calibration days (limit 2)" in text
    assert "Late runs: 2 entries and 1 ladder pass mirrored on 3 days (limit 2)." in text
    assert 'class="alert bad"' in page                  # over the limit: in the alarm colours
    assert "ladder pass (the whole book)" in text and "entry XOM" in text
    assert "&lt;b&gt;JPM&lt;/b&gt;" in page and "<b>JPM</b>" not in page      # escaped
    # No end date and no fund test start from a stopped calibration, whatever the record holds.
    assert "Calibration is stopped, so it has no end date" in text
    assert "If nothing more fails" not in text and "Fund test would start" not in text
    assert "Where each condition stands" in text        # the conditions are still shown

    running_text = _text(pages[1])
    assert "Late runs: 1 entry and 0 ladder passes mirrored on 1 day (limit 2)." in running_text
    assert 'class="amber"' in pages[1] and "alert bad" not in pages[1]
    assert "If nothing more fails, it ends 22 Oct 2026." in running_text
    assert "mirrored on" not in _text(pages[2])         # an older record says nothing about late runs


@needs_node
def test_a_stop_heads_the_problems_card(tmp_path, funds_page):
    source = _page_functions(funds_page, "verdictRow", "problemList", "problemsHtml")
    stopped = calibration_record("stopped", MIRRORED_ITEMS, problems=["2026-10-05: " + calib.SCHEDULE_GUARD])
    out = _run_js(tmp_path, source, "CASES.map(problemsHtml)", [stopped, calibration_record("running", [])])

    text = _text(out[0])
    assert 'class="alert bad"' in out[0]
    assert text.index("Calibration stopped: late-run copying was needed on 3 calibration days") < \
        text.index("the schedule guard should have prevented this")
    assert "Pass rule: 1. every close within 1.00%: FAIL" in text
    assert "Calibration stopped" not in _text(out[1])


def test_the_page_states_the_late_run_fields():
    text = (ROOT / "dashboard" / "funds.html").read_text()
    comment = text[text.index("<!--") + 4:text.index("-->")]
    assert "<!--" not in comment and "--!>" not in comment
    for field in ("stopped", "calibration.mirrored[]", "calibration.mirrored_days[]",
                  "calibration.mirrored_day_count", "calibration.mirror_limit", "calibration.stop_reason",
                  '"ladder pass"'):
        assert field in comment, field


def test_the_docs_and_the_pre_registration_carry_the_owners_decision():
    shadow_doc = " ".join((ROOT / "docs" / "shadow-funds.mdx").read_text().split())
    assert "### Late runs" in (ROOT / "docs" / "shadow-funds.mdx").read_text()
    assert "If more than 2 calibration days need this, calibration stops" in shadow_doc
    raw = (ROOT / "docs" / "horse-race-preregistration.md").read_text()
    rows = [r for r in raw.partition("## Amendments")[2].splitlines()
            if r.startswith("| 2026-09-25 | **Calibration: late-run mirroring**")]
    assert len(rows) == 1
    row = rows[0]
    assert "Changes calibration only: not the race, not the funds." in row
    assert "**If more than 2 calibration days need this, calibration stops**" in row
    # The code mirrors line by line and counts a day when it is journalled;
    # both texts say so, and neither keeps a name-level exception.
    for text in (shadow_doc, row):
        assert "The mirror goes line by line" in text
        assert "counted the evening its cycle is journalled" in text
        assert "before the copy would have entered" not in text
    # In date order: no row after it is dated earlier.
    dated = [r[2:12] for r in raw.partition("## Amendments")[2].splitlines() if r.startswith("| 20")]
    assert dated == sorted(dated)
