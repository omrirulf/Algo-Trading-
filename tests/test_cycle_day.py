"""The catch-up guard: did a cycle run today?

The guard's whole job is to be wrong in only one direction. Saying "no cycle
today" when one ran costs a wasted run the broker's idempotency key makes
harmless. Saying "a cycle ran" when none did loses the trading day silently,
which is the failure the catch-up exists to prevent.
"""

from __future__ import annotations

import json
from datetime import date, datetime, timedelta, timezone

import yaml
from pathlib import Path

from analysis.cycle_day import cycle_ran_on, main
from analysis.reader import read_lines


def _line(ticker: str, when: datetime | None) -> str:
    payload = {"ticker": ticker, "signal": {"bias": "NEUTRAL", "conviction": 0.1}}
    if when is not None:
        payload["ts_utc"] = when.isoformat()
    return json.dumps(payload)


def _entries(*lines: str):
    return read_lines(list(lines)).entries


def test_an_entry_from_today_counts_as_a_cycle():
    today = datetime(2026, 9, 16, 15, 54, tzinfo=timezone.utc)
    assert cycle_ran_on(_entries(_line("MSFT", today)), date(2026, 9, 16))


def test_yesterdays_entries_do_not_count():
    """The bug this guards: a journal full of history is not today's proof."""
    yesterday = datetime(2026, 9, 15, 19, 10, tzinfo=timezone.utc)
    assert not cycle_ran_on(_entries(_line("MSFT", yesterday)), date(2026, 9, 16))


def test_a_late_entry_still_counts_for_the_day_it_was_written():
    """23:59 UTC is still today; the comparison is on the date, not the hour."""
    late = datetime(2026, 9, 16, 23, 59, 59, tzinfo=timezone.utc)
    assert cycle_ran_on(_entries(_line("MSFT", late)), date(2026, 9, 16))


def test_an_entry_in_another_zone_is_compared_in_utc():
    """A cycle at 01:30 in UTC+3 is still 22:30 the previous day in UTC."""
    stamped = datetime(2026, 9, 17, 1, 30, tzinfo=timezone(timedelta(hours=3)))
    assert cycle_ran_on(_entries(_line("MSFT", stamped)), date(2026, 9, 16))
    assert not cycle_ran_on(_entries(_line("MSFT", stamped)), date(2026, 9, 17))


def test_an_entry_with_no_timestamp_proves_nothing():
    """It cannot say when it happened, so it cannot say today is covered.

    Counting it would skip the catch-up on exactly the days the journal is
    damaged -- the days the catch-up matters most.
    """
    assert not cycle_ran_on(_entries(_line("MSFT", None)), date(2026, 9, 16))


def test_one_today_among_many_older_lines_is_enough():
    old = datetime(2026, 9, 10, 15, 0, tzinfo=timezone.utc)
    today = datetime(2026, 9, 16, 15, 0, tzinfo=timezone.utc)
    lines = [_line(f"T{i}", old) for i in range(50)] + [_line("LLY", today)]
    assert cycle_ran_on(_entries(*lines), date(2026, 9, 16))


def test_an_empty_journal_is_no():
    assert not cycle_ran_on([], date(2026, 9, 16))


# --------------------------------------------------------------------------- #
# the CLI the workflow calls
# --------------------------------------------------------------------------- #

def test_cli_prints_yes_and_exits_zero(tmp_path, capsys):
    path = tmp_path / "journal.log"
    path.write_text(_line("MSFT", datetime(2026, 9, 16, 15, 0, tzinfo=timezone.utc)) + "\n")
    assert main(["--journal", str(path), "--day", "2026-09-16"]) == 0
    assert capsys.readouterr().out.strip() == "yes"


def test_cli_prints_no_and_still_exits_zero(tmp_path, capsys):
    """Zero either way: the caller must tell 'no cycle' from 'check broke'."""
    path = tmp_path / "journal.log"
    path.write_text(_line("MSFT", datetime(2026, 9, 15, 15, 0, tzinfo=timezone.utc)) + "\n")
    assert main(["--journal", str(path), "--day", "2026-09-16"]) == 0
    assert capsys.readouterr().out.strip() == "no"


def test_a_missing_journal_is_no_not_a_crash(tmp_path, capsys):
    """No journal at all is the strongest possible 'no cycle today'."""
    assert main(["--journal", str(tmp_path / "absent.log"), "--day", "2026-09-16"]) == 0
    assert capsys.readouterr().out.strip() == "no"


# --------------------------------------------------------------------------- #
# the wiring, which is where this can silently stop working
# --------------------------------------------------------------------------- #

def _heartbeat() -> dict:
    path = Path(__file__).resolve().parents[1] / ".github/workflows/heartbeat.yml"
    # PyYAML reads a bare `on:` key as the boolean True.
    return yaml.safe_load(path.read_text())


def test_the_catch_up_cron_exists_and_the_guard_matches_it():
    """The guard keys off the exact cron string, so the two must not drift.

    Rename the cron without renaming it here and the guard stops firing: the
    catch-up would then run a second full cycle every day, quietly, at cost.
    """
    workflow = _heartbeat()
    crons = [entry["cron"] for entry in workflow[True]["schedule"]]
    assert len(crons) == 2, "the catch-up cron is what makes a lost day recoverable"
    catch_up = crons[1]
    steps = workflow["jobs"]["cycle"]["steps"]
    guard = next(s for s in steps if s.get("id") == "guard")
    assert catch_up in guard["if"], f"guard does not name the catch-up cron {catch_up}"


def test_the_first_cron_and_a_manual_run_are_never_guarded():
    """Neither should ever be talked out of running."""
    guard = next(s for s in _heartbeat()["jobs"]["cycle"]["steps"] if s.get("id") == "guard")
    assert "github.event.schedule ==" in guard["if"]


def test_every_step_after_the_guard_respects_it():
    """A skipped catch-up must not still commit, refit or publish.

    Those steps run on `always()` so a failed cycle still records itself. That
    same `always()` would run them for a catch-up that correctly did nothing,
    re-rendering and re-committing a cycle that already happened.
    """
    steps = _heartbeat()["jobs"]["cycle"]["steps"]
    after = steps[[s.get("id") for s in steps].index("guard") + 1:]
    assert after, "the guard is the last step, which cannot be right"
    for step in after:
        condition = step.get("if", "")
        assert "steps.guard.outputs.ran != 'yes'" in condition, (
            f"step {step.get('name')!r} ignores the guard: {condition!r}"
        )


def test_the_guard_test_is_on_yes_rather_than_not_no():
    """A skipped guard leaves the output unset, and unset must mean run.

    `!= 'no'` would read an unset output as "a cycle already ran" and skip the
    15:05 cycle every single day.
    """
    steps = _heartbeat()["jobs"]["cycle"]["steps"]
    cycle = next(s for s in steps if s.get("name") == "Run one cycle")
    assert cycle["if"] == "steps.guard.outputs.ran != 'yes'"
