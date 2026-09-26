"""When each cycle ran, and the race's report of it.

GitHub delivered the heartbeat's scheduled runs hours late on every day so
far, and every cycle since 21 Sep 2026 was really started by a backup
dispatch at about 15:05 UTC. The journal said none of it. These tests pin
how ``analysis/run_timing.py`` reads a day -- from the journal's own run
block when a line carries one, from the first line against the cron history
when it does not -- that no junk in a run block can break the race, and that
the race's report of it moves no look, bar or verdict.

The journals here are synthetic. The times in ``OBSERVED`` are the first and
last journal lines of 15-24 Sep 2026 as the real log has them, so the test
also says what the owner was told: every one of those days was late (44 to
153 minutes after its schedule) and every line was written during the
session, none before the open.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from typing import Any

import pytest

from analysis import decision_gate, horse_race, run_timing
from analysis.reader import entry_from, read_lines
from analysis.run_timing import (
    AFTER_CLOSE,
    ENTRY_SENTENCE,
    FROM_RUN_BLOCK,
    INFERRED,
    NO_SESSION,
    PRE_OPEN,
    SESSION,
    day_timings,
    parse_run_block,
    scheduled_start,
    session_phase,
    timing_json,
    totals,
)

UTC = timezone.utc


@dataclass
class Line:
    """The two things run timing reads off a journal entry, and nothing else."""

    timestamp: Any
    run: Any = None


def at(text: str) -> datetime:
    return datetime.fromisoformat(text).replace(tzinfo=UTC)


#: First and last journal line of every cycle day so far, UTC, and the minutes
#: after that day's scheduled start the first one was written.
OBSERVED = [
    ("2026-09-15T16:54:47", "2026-09-15T19:10:21", 109),
    ("2026-09-16T15:54:01", "2026-09-16T19:31:46", 49),
    ("2026-09-17T15:49:15", "2026-09-17T19:23:57", 44),
    ("2026-09-18T16:18:07", "2026-09-18T17:02:56", 73),
    ("2026-09-21T15:08:08", "2026-09-21T15:34:05", 153),
    ("2026-09-22T15:07:29", "2026-09-22T15:45:13", 152),
    ("2026-09-23T15:06:50", "2026-09-23T16:20:36", 151),
    ("2026-09-24T15:08:10", "2026-09-24T15:36:19", 153),
]


def observed_journal() -> list[str]:
    """Three lines a day: the first, one in the middle, the last."""
    lines = []
    for first, last, _ in OBSERVED:
        a, b = at(first), at(last)
        for stamp in (a, a + (b - a) / 2, b):
            lines.append(json.dumps({"ts_utc": stamp.isoformat(), "ticker": "NVDA",
                                     "signal": {"bias": "BULLISH", "conviction": 0.5}}))
    return lines


# --------------------------------------------------------------------------- #
# The schedule, and the session
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("day, expected", [
    (date(2026, 9, 11), None),                 # before the history: no known schedule
    (date(2026, 9, 14), time(13, 5)),          # hourly cron, its first slot
    (date(2026, 9, 15), time(15, 5)),
    (date(2026, 9, 18), time(15, 5)),
    (date(2026, 9, 19), None),                 # Saturday: the cron does not fire
    (date(2026, 9, 20), None),
    (date(2026, 9, 21), time(12, 35)),         # the --premarket slot
    (date(2026, 9, 25), time(12, 35)),
    # No row for 14:40: a day from the change on carries its schedule in its
    # run block. A block-less day after it (a local run) falls back to the
    # last row, and reads "inferred".
    (date(2026, 9, 28), time(12, 35)),
    (date(2026, 12, 1), time(12, 35)),
    (date(2026, 11, 26), time(12, 35)),        # Thanksgiving: the cron still fires
])
def test_the_scheduled_start_is_the_heartbeats_cron_history(day, expected):
    got = scheduled_start(day)
    if expected is None:
        assert got is None
    else:
        assert got == datetime.combine(day, expected, tzinfo=UTC)


def test_the_schedule_history_only_ever_grows():
    days = [first for first, _ in run_timing.SCHEDULE_HISTORY]
    assert days == sorted(days) and len(set(days)) == len(days)
    # The last row is the last schedule a day could be journalled under
    # without a run block. 14:40 has no row: the change that set it is the
    # one that made every cycle line carry its own ``scheduled_for``, and its
    # merge day was not known when this was written. A guessed date would
    # have measured every weekday between the guess and the real merge
    # against the wrong time, in a table whose rows may never be edited.
    assert run_timing.SCHEDULE_HISTORY[-1] == (date(2026, 9, 21), time(12, 35))


def test_the_current_schedule_and_the_late_rule_are_the_run_blocks_own():
    """Days from the run block on are measured against the block the cycle
    step writes, which carries the cycle guard's scheduled start and late
    threshold; the history measures only days from before it, the same way."""
    from analysis import cycle_day

    if not hasattr(cycle_day, "SCHEDULED_START_UTC"):  # pragma: no cover - before the run block existed
        pytest.skip("the cycle guard does not write a run block yet")
    block = cycle_day.run_block(event="workflow_dispatch", started_by="backup", run_id=7,
                                started_at=at("2026-10-05T15:12:00"))
    (t,) = day_timings([Line(at("2026-10-05T15:20:00"), block)])
    assert t.scheduled_for == datetime.combine(date(2026, 10, 5), cycle_day.SCHEDULED_START_UTC, tzinfo=UTC)
    assert (t.minutes_late, t.late, t.source) == (32, True, FROM_RUN_BLOCK)
    assert cycle_day.SCHEDULED_START_UTC not in {when for _, when in run_timing.SCHEDULE_HISTORY}
    assert run_timing.LATE_AFTER_MINUTES == cycle_day.LATE_AFTER_MINUTES


def test_the_pre_registration_logs_the_run_timing_and_keeps_the_entry_rule():
    from pathlib import Path

    raw = (Path(__file__).resolve().parents[1] / "docs/horse-race-preregistration.md").read_text()
    rows = [r for r in raw.partition("## Amendments")[2].splitlines()
            if r.startswith("| 2026-09-25 | **Run timing and late runs**")]
    assert len(rows) == 1
    row = rows[0]
    assert "operational, not a decision rule" in row and "**The entry rule is unchanged**" in row
    assert "tests/test_race_entry_timing.py" in row and "**none ran before the open.**" in row
    assert "No decision rule changes." in row
    # The entry rule the row says is unchanged is the one section 2 registered.
    assert "the session after the signal, at the open" in " ".join(raw.split())


@pytest.mark.parametrize("stamp, phase", [
    # Summer (EDT, UTC-4): the session is 13:30-20:00 UTC.
    ("2026-09-22T12:35:00", PRE_OPEN),         # the --premarket slot: 08:35 New York
    ("2026-09-22T13:29:59", PRE_OPEN),
    ("2026-09-22T13:30:00", SESSION),          # the bell
    ("2026-09-22T15:06:50", SESSION),
    ("2026-09-22T19:59:59", SESSION),
    ("2026-09-22T20:00:00", AFTER_CLOSE),
    ("2026-09-23T00:30:00", AFTER_CLOSE),      # the 22nd's evening in New York, not the 23rd's morning
    ("2026-09-19T15:00:00", NO_SESSION),       # Saturday
    ("2026-09-07T15:00:00", NO_SESSION),       # Labor Day
    # Winter (EST, UTC-5): the session is 14:30-21:00 UTC.
    ("2026-12-01T14:29:00", PRE_OPEN),
    ("2026-12-01T14:40:00", SESSION),          # the 14:40 UTC schedule: 09:40 New York
    ("2026-12-01T20:30:00", SESSION),          # 15:30 New York
    ("2026-12-01T21:00:00", AFTER_CLOSE),
])
def test_the_phase_is_read_on_new_york_time(stamp, phase):
    assert session_phase(at(stamp)) == phase


# --------------------------------------------------------------------------- #
# Days with no run block: inferred from the first line
# --------------------------------------------------------------------------- #


def test_every_cycle_day_so_far_was_late_and_every_line_was_in_the_session():
    timings = day_timings(read_lines(observed_journal()).entries)
    assert [t.day for t in timings] == [at(first).date() for first, _, _ in OBSERVED]
    for t, (first, last, minutes) in zip(timings, OBSERVED):
        assert (t.first_utc, t.last_utc) == (at(first), at(last))
        assert t.started_at == t.first_utc
        assert t.minutes_late == minutes
        assert t.late is True
        assert t.phase == SESSION and t.count(SESSION) == 3
        assert t.started_by == "unknown" and t.source == INFERRED and t.runs == 0
    assert min(t.minutes_late for t in timings) == 44 and max(t.minutes_late for t in timings) == 153
    assert totals(timings) == {"late_days": 8, "cycle_days": 8, "unscheduled_days": 0,
                               "lines_before_open": 0, "lines_after_close": 0, "lines_no_session": 0}

    text = run_timing.render(timings, cutoff=date(2026, 9, 23))
    assert "late-run days: 8 of 8; lines before the open: 0; after the close: 0" in text
    assert "in the decision window (from 2026-09-23): late-run days 2 of 2" in text
    assert "2026-09-15  before  12:54-15:10  session      +109 min  unknown   inferred  LATE" in text
    assert "2026-09-23  window  11:06-12:20  session      +151 min  unknown   inferred  LATE" in text
    assert text[-1] == ENTRY_SENTENCE


def test_minutes_late_are_floored_and_thirty_is_not_late():
    """The run block's own rule, applied to an inferred day the same way."""
    on_time = day_timings([Line(at("2026-09-22T13:05:59"))])[0]
    assert on_time.minutes_late == 30 and on_time.late is False
    late = day_timings([Line(at("2026-09-22T13:06:00"))])[0]
    assert late.minutes_late == 31 and late.late is True
    early = day_timings([Line(at("2026-09-22T12:34:30"))])[0]
    assert early.minutes_late == -1 and early.late is False


def test_a_day_with_no_known_schedule_is_never_called_late():
    weekend = day_timings([Line(at("2026-09-19T15:00:00"))])
    before = day_timings([Line(at("2026-09-11T15:00:00"))])
    for (t,) in (weekend, before):
        assert t.scheduled_for is None and t.minutes_late is None and t.late is None
    assert weekend[0].phase == NO_SESSION
    text = run_timing.render(weekend + before)
    assert "late-run days: 0 of 2; lines before the open: 0; after the close: 0; on a day with no session: 1" in text
    assert ("note: 2 day(s) have no known schedule (a weekend, or before 2026-09-14), so none of them "
            "is called late") in text
    assert any(row.startswith("2026-09-19") and " n/a " in row and "LATE" not in row for row in text)


def test_a_day_split_across_phases_reads_mixed_and_counts_every_line():
    (t,) = day_timings([Line(at("2026-09-22T12:00:00")), Line(at("2026-09-22T14:45:00")),
                        Line(at("2026-09-22T20:05:00"))])
    assert t.phase == "mixed"
    assert (t.count(PRE_OPEN), t.count(SESSION), t.count(AFTER_CLOSE)) == (1, 1, 1)
    # The first line, not the earliest in the session, is when the run started.
    assert t.minutes_late == -35 and t.late is False
    assert totals([t])["lines_before_open"] == 1 and totals([t])["lines_after_close"] == 1


def test_lines_are_grouped_by_their_utc_day_and_ordered_within_it():
    """Journal order is not trusted: two runs can interleave their lines."""
    (t,) = day_timings([Line(at("2026-09-28T15:30:00")), Line(at("2026-09-28T14:50:00")),
                        Line(None), Line("not a time")])
    assert t.lines == 2 and t.first_utc == at("2026-09-28T14:50:00")
    naive = day_timings([Line(datetime(2026, 9, 28, 14, 50))])[0]
    assert naive.first_utc == at("2026-09-28T14:50:00"), "a naive time is read as UTC, like the reader's"


# --------------------------------------------------------------------------- #
# Days with a run block: the block wins
# --------------------------------------------------------------------------- #

BLOCK = {"trigger": "backup", "scheduled_for": "2026-09-28T14:40:00+00:00",
         "started_at": "2026-09-28T15:12:00+00:00", "minutes_late": 32, "late": True, "run_id": "9001"}


def test_the_run_block_wins_over_the_first_line_and_the_history():
    (t,) = day_timings([Line(at("2026-09-28T15:20:00"), BLOCK), Line(at("2026-09-28T15:40:00"), BLOCK)])
    assert t.scheduled_for == at("2026-09-28T14:40:00")
    assert t.started_at == at("2026-09-28T15:12:00"), "the cycle step's start, not its first line"
    assert (t.minutes_late, t.late) == (32, True)
    assert (t.started_by, t.source, t.runs) == ("backup", FROM_RUN_BLOCK, 1)
    row = next(r for r in run_timing.render([t]) if r.startswith("2026-09-28"))
    assert row == "2026-09-28  11:20-11:40  session       +32 min  backup    run block LATE"

    # A block that disagrees with the history is still the record of the day.
    moved = dict(BLOCK, scheduled_for="2026-09-28T15:00:00+00:00", minutes_late=12, late=False,
                 trigger="schedule")
    (m,) = day_timings([Line(at("2026-09-28T15:20:00"), moved)])
    assert (m.scheduled_for, m.minutes_late, m.late, m.started_by) == (at("2026-09-28T15:00:00"), 12, False,
                                                                       "schedule")


def test_a_block_without_its_own_numbers_is_measured_from_its_own_times():
    block = {"trigger": "manual", "scheduled_for": "2026-09-28T14:40:00Z", "started_at": "2026-09-28T14:10:30Z"}
    (t,) = day_timings([Line(at("2026-09-28T14:30:00"), block)])
    assert t.minutes_late == -30 and t.late is False and t.source == FROM_RUN_BLOCK
    only_start = {"started_at": "2026-09-22T13:25:00+00:00"}
    (s,) = day_timings([Line(at("2026-09-22T13:26:00"), only_start)])
    assert s.scheduled_for == at("2026-09-22T12:35:00"), "the history fills what the block left out"
    assert s.minutes_late == 50 and s.late is True and s.started_by == "unknown"


def test_a_block_with_only_a_trigger_says_who_but_not_when():
    (t,) = day_timings([Line(at("2026-09-22T13:26:00"), {"trigger": "backup"})])
    assert t.started_by == "backup" and t.source == INFERRED and t.minutes_late == 51


def test_two_runs_on_one_day_are_counted_and_the_first_is_measured():
    """The guard race of 25 Sep: a queued run read an old journal and ran a
    second cycle. The day's lateness is the first run's; the second shows as
    a second run id, so the day cannot quietly hide it."""
    second = dict(BLOCK, trigger="schedule", started_at="2026-09-28T17:40:00+00:00", minutes_late=180,
                  run_id="9002")
    (t,) = day_timings([Line(at("2026-09-28T17:45:00"), second), Line(at("2026-09-28T15:20:00"), BLOCK)])
    assert t.runs == 2 and t.started_by == "backup" and t.minutes_late == 32
    row = next(r for r in run_timing.render([t]) if r.startswith("2026-09-28"))
    assert row.endswith("LATE (2 runs)")


JUNK = [
    None, "backup", 42, 3.5, True, [BLOCK], {}, {"trigger": 5},
    {"trigger": "somebody", "scheduled_for": "yesterday", "started_at": 1727000000,
     "minutes_late": "12", "late": "yes", "run_id": None},
    {"minutes_late": True, "late": 1},
    {"minutes_late": float("nan"), "scheduled_for": "2026-13-45T99:00:00", "run_id": ""},
    {"started_at": {"nested": "dict"}, "run_id": ["x"], "trigger": ["backup"]},
]


@pytest.mark.parametrize("junk", JUNK, ids=[repr(j)[:40] for j in JUNK])
def test_junk_in_a_run_block_is_read_as_no_block_and_never_raises(junk):
    (t,) = day_timings([Line(at("2026-09-22T13:26:00"), junk)])
    assert t.source == INFERRED and t.started_by == "unknown" and t.runs == 0
    assert t.minutes_late == 51 and t.late is True
    json.dumps(timing_json([t]), allow_nan=False)


def test_a_minutes_late_given_as_a_whole_float_is_taken_and_a_bool_never_is():
    assert parse_run_block({"minutes_late": 45.0}).minutes_late == 45
    assert parse_run_block({"minutes_late": 45.5}) is None
    assert parse_run_block({"minutes_late": False}) is None


def test_an_entry_whose_run_field_raises_costs_one_block_not_the_report():
    class Broken:
        timestamp = at("2026-09-22T13:26:00")

        @property
        def run(self):
            raise RuntimeError("a property that should never raise, raising")

    (t,) = day_timings([Broken()])
    assert t.source == INFERRED and t.minutes_late == 51


def test_the_reader_carries_the_journals_run_block_through():
    """Through the real reader: the block when ``JournalEntry`` has ``run``, and
    no error either way -- this module reads it with ``getattr``."""
    good = json.dumps({"ts_utc": "2026-09-28T15:20:00+00:00", "ticker": "NVDA", "run": BLOCK})
    junk = json.dumps({"ts_utc": "2026-09-29T13:15:00+00:00", "ticker": "NVDA", "run": "not an object"})
    entries = read_lines([good, junk]).entries
    first, second = day_timings(entries)
    if getattr(entry_from(json.loads(good)), "run", None) is not None:
        assert first.source == FROM_RUN_BLOCK and first.started_by == "backup" and first.minutes_late == 32
    else:  # pragma: no cover - only before the reader had the field
        assert first.source == INFERRED
    assert second.source == INFERRED and second.minutes_late == 40


# --------------------------------------------------------------------------- #
# JSON, text and the command line
# --------------------------------------------------------------------------- #


def test_the_json_is_strict_json_and_labels_each_day_against_the_cutoff():
    timings = day_timings(read_lines(observed_journal()).entries)
    data = json.loads(json.dumps(timing_json(timings, cutoff=date(2026, 9, 23)), allow_nan=False))
    assert data["entry_rule"] == ENTRY_SENTENCE
    assert (data["late_days"], data["cycle_days"], data["window_late_days"], data["window_cycle_days"]) == (8, 8, 2, 2)
    assert (data["lines_before_open"], data["lines_after_close"]) == (0, 0)
    assert [d["part"] for d in data["days"]] == ["before"] * 6 + ["window"] * 2
    first = data["days"][0]
    assert first == {
        "day": "2026-09-15", "part": "before", "lines": 3,
        "first_utc": "2026-09-15T16:54:47+00:00", "last_utc": "2026-09-15T19:10:21+00:00",
        "first_new_york": "12:54", "last_new_york": "15:10", "phase": "session",
        "phases": {"pre_open": 0, "session": 3, "after_close": 0, "no_session": 0},
        "scheduled_for": "2026-09-15T15:05:00+00:00", "started_at": "2026-09-15T16:54:47+00:00",
        "minutes_late": 109, "late": True, "started_by": "unknown", "source": INFERRED,
        "run_source": "unknown", "runs": 0,
    }
    assert timing_json(timings)["days"][0]["part"] is None, "no cutoff, no label"


def test_the_command_line_prints_the_table_and_writes_nothing(tmp_path, capsys):
    journal = tmp_path / "signal_journal.log"
    journal.write_text("\n".join(observed_journal()) + "\n", encoding="utf-8")
    before = sorted(p.name for p in tmp_path.iterdir())
    assert run_timing.main(["--journal", str(journal)]) == 0
    out = capsys.readouterr().out
    assert out.startswith("RUN TIMING")
    assert "late-run days: 8 of 8; lines before the open: 0; after the close: 0" in out
    assert sorted(p.name for p in tmp_path.iterdir()) == before
    assert run_timing.main(["--journal", str(tmp_path / "missing.log")]) == 1


# --------------------------------------------------------------------------- #
# The race: printed after the checks, carried in the gate JSON, deciding nothing
# --------------------------------------------------------------------------- #


def _journal(with_runs: bool) -> list[dict]:
    """Four cycle days, four names each, some long, some short."""
    out = []
    for n, day in enumerate((date(2026, 9, 15), date(2026, 9, 16), date(2026, 9, 17), date(2026, 9, 18))):
        start = datetime.combine(day, time(15, 50), tzinfo=UTC)
        for i in range(4):
            stamp = start + timedelta(minutes=3 * i)
            row = {"ts_utc": stamp.isoformat(), "ticker": f"T{i}",
                   "context": {"technicals": {"return_63d": 0.10, "distance_sma50": 0.03,
                                              "annualised_volatility": 0.20}},
                   "signal": {"bias": "BULLISH" if (i + n) % 3 else "BEARISH",
                              "conviction": 0.45 + 0.1 * i, "news_score": 0.3}}
            if with_runs:
                row["run"] = {"trigger": "backup", "scheduled_for": f"{day}T15:05:00+00:00",
                              "started_at": f"{day}T15:49:00+00:00", "minutes_late": 44, "late": True,
                              "run_id": str(1000 + n)}
            out.append(row)
    return out


def _frames():
    from tests.test_race_entry_timing import bars

    frame = bars()
    return {**{f"T{i}": frame for i in range(4)}, decision_gate.INDEX_TICKER: frame, "SPY": frame}


NOW = datetime(2026, 10, 20, 22, 0, tzinfo=UTC)


def _without_run_timing(text: str) -> str:
    start = text.index("\nRUN TIMING")
    end = text.index(ENTRY_SENTENCE, start) + len(ENTRY_SENTENCE)
    return text[:start] + text[end:]


def test_the_race_prints_run_timing_after_the_checks_and_before_the_tables(tmp_path, monkeypatch, capsys):
    from tests.test_horse_race import _race

    code, out = _race(tmp_path, monkeypatch, capsys, _frames(), _journal(False), NOW,
                      cutoff=date(2026, 9, 17))
    assert code == 0
    assert (out.index("DECISION GATE") < out.index("MODEL WATCH") < out.index("LLM SPEND")
            < out.index("RUN TIMING") < out.index("DEFINITIONS") < out.index("COVERAGE AND RECONCILIATION"))
    section = out[out.index("RUN TIMING"):out.index("DEFINITIONS")].splitlines()
    rows = [r for r in section if r[:4] == "2026"]
    assert [r.split()[:2] for r in rows] == [["2026-09-15", "before"], ["2026-09-16", "before"],
                                             ["2026-09-17", "window"], ["2026-09-18", "window"]]
    assert rows[0] == "2026-09-15  before  11:50-11:59  session       +45 min  unknown   inferred  LATE"
    assert "late-run days: 4 of 4; lines before the open: 0; after the close: 0" in section
    assert "in the decision window (from 2026-09-17): late-run days 2 of 2" in section
    assert ENTRY_SENTENCE in section


def test_the_gate_json_carries_run_timing_as_strict_json():
    timings = day_timings(read_lines(observed_journal()).entries)
    view = horse_race.GateView(registered=True, mismatches=(), window_lines=6, window_cycle_days=2,
                               unanswered_in_window=0, entry_days=1, independent=0,
                               looks=tuple(decision_gate.evaluate({})), next_estimate=None)
    plain = horse_race.gate_json(view, 3, NOW)
    assert plain["run_timing"] is None
    data = horse_race.gate_json(view, 3, NOW, splits=horse_race.trade_splits([]), timings=timings)
    json.loads(json.dumps(data, allow_nan=False))
    assert data["run_timing"] == timing_json(timings, cutoff=decision_gate.DECISION_CUTOFF)
    assert data["run_timing"]["window_cycle_days"] == 2
    assert {k: v for k, v in data.items() if k not in ("run_timing", "conviction_groups", "sides")} == \
           {k: v for k, v in plain.items() if k not in ("run_timing", "conviction_groups", "sides")}


def test_run_blocks_move_no_look_no_bar_and_no_verdict(tmp_path, monkeypatch, capsys):
    """The same journal with and without run blocks: every decision number the
    gate read, the gate JSON field for field, and the whole printed race
    outside the run timing section are identical. Only the run timing moves.

    The looks are shrunk to 1, 2 and 3 independent days so that a real look
    is reached and evaluated on this small journal -- a comparison of two
    runs that decide nothing would prove nothing."""
    monkeypatch.setattr(decision_gate, "CHECKPOINTS", ((1, 3.47), (2, 2.45), (3, 2.00)))
    seen: list[dict] = []
    original = decision_gate.evaluate

    def recording(inputs):
        seen.append(dict(inputs))
        return original(inputs)

    monkeypatch.setattr(decision_gate, "evaluate", recording)
    from tests.test_horse_race import _race

    results = {}
    for with_runs in (False, True):
        # The registered 1000 seeds: any other setting is a sensitivity run,
        # which evaluates no look at all.
        _, gate_out = _race(tmp_path, monkeypatch, capsys, _frames(), _journal(with_runs), NOW,
                            extra=("--seeds", "1000", "--gate-json"))
        _, text = _race(tmp_path, monkeypatch, capsys, _frames(), _journal(with_runs), NOW,
                        extra=("--seeds", "1000"))
        results[with_runs] = (json.loads(gate_out), text)

    (plain, plain_text), (runs, runs_text) = results[False], results[True]
    assert plain["looks"][0]["reached"] is True, "a look was evaluated, so there is something to compare"
    assert len(seen) == 4 and seen[0] and seen[0] == seen[1] == seen[2] == seen[3]
    assert {k: v for k, v in plain.items() if k != "run_timing"} == \
           {k: v for k, v in runs.items() if k != "run_timing"}
    assert _without_run_timing(plain_text) == _without_run_timing(runs_text)

    assert plain["run_timing"]["days"][0]["source"] == INFERRED
    if getattr(entry_from(_journal(True)[0]), "run", None) is not None:
        assert runs["run_timing"]["days"][0]["source"] == FROM_RUN_BLOCK
        assert runs["run_timing"]["days"][0]["started_by"] == "backup"
        assert "backup    run block LATE" in runs_text
