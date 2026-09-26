"""The catch-up guard: did a cycle run today?

The guard's whole job is to be wrong in only one direction. Saying "no cycle
today" when one ran costs a wasted run the broker's idempotency key makes
harmless. Saying "a cycle ran" when none did loses the trading day silently,
which is the failure the catch-up exists to prevent.
"""

from __future__ import annotations

import json
from datetime import date, datetime, timedelta, timezone

import pytest
import yaml
from pathlib import Path

from analysis.cycle_day import (
    EARLY_CLOSES,
    LATEST_START_NY,
    SCHEDULED_START_UTC,
    check_start,
    closes_at,
    cycle_ran_on,
    latest_start,
    main,
    other_runs_from,
    run_block,
    start_decision,
    start_summary,
    trigger_for,
)
from config.market_calendar import NYSE_HOLIDAYS, is_trading_day
from analysis.reader import read_lines

UTC = timezone.utc


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


def test_the_catch_up_cron_exists_and_the_guard_no_longer_names_a_cron():
    """Two crons: the cycle and a catch-up. The guard used to key off the
    catch-up's exact string, which is how a late-delivered 15:05 run slipped
    past it and ran the day twice. Now no cron string appears in the guard at
    all, so neither can drift away from it."""
    workflow = _heartbeat()
    crons = [entry["cron"] for entry in workflow[True]["schedule"]]
    assert len(crons) == 2, "the catch-up cron is what makes a lost day recoverable"
    steps = workflow["jobs"]["cycle"]["steps"]
    guard = next(s for s in steps if s.get("id") == "guard")
    for cron in crons:
        assert cron not in guard["if"]
    assert "github.event.schedule" not in guard["if"]


def test_every_cycle_run_is_guarded_and_only_a_rerun_gets_past():
    """On 16 Sep the 15:05 cron was delivered after the 17:35 catch-up had
    already run the cycle, and because only the catch-up asked, the day ran
    twice. So every scheduled run came to ask the journal, whichever cron
    delivered it. Since 25 Sep a dispatch asks too: the watchdog's backup,
    the Routines and a late cron can all land on one day. A protection pass
    is not a cycle, and a person's `rerun` is the one deliberate way past --
    on its first attempt only: "Re-run" replays the dispatch, `rerun`
    included, and must not trade the day a second time."""
    guard = next(s for s in _heartbeat()["jobs"]["cycle"]["steps"] if s.get("id") == "guard")
    assert guard["if"] == ("inputs.mode != 'protect' && "
                           "(inputs.rerun != true || github.run_attempt != '1')")
    assert "github.event_name" not in guard["if"], "a dispatch must be guarded too"


def test_every_step_after_the_guard_respects_it():
    """A skipped run must not still commit, refit or publish.

    Those steps run on `always()` so a failed cycle still records itself. That
    same `always()` would run them for a run the guard correctly stopped,
    re-rendering and re-committing a cycle that already happened. The one
    exception is the protection pass, which is never scheduled: it runs only
    when a dispatch asks for it, and the guard does not run on one.
    """
    steps = _heartbeat()["jobs"]["cycle"]["steps"]
    after = steps[[s.get("id") for s in steps].index("guard") + 1:]
    assert after, "the guard is the last step, which cannot be right"
    for step in after:
        condition = step.get("if", "")
        if step.get("name") == "Protect every open position":
            assert condition == "inputs.mode == 'protect'"
            continue
        if step.get("name") == "Tell the owner's phone the backup started too late":
            # The one step that exists BECAUSE the guard said stop: it only
            # tells the phone, and only when it was the watchdog's backup.
            assert condition == "steps.guard.outputs.why == 'too_late' && inputs.started_by == 'backup'"
            assert set(step["env"]) == {"NTFY_TOPIC", "RUN_URL"}
            continue
        assert "steps.guard.outputs.skip != 'yes'" in condition, (
            f"step {step.get('name')!r} ignores the guard: {condition!r}"
        )


def test_the_guard_test_is_on_yes_rather_than_not_no():
    """A skipped guard leaves the output unset, and unset must mean run.

    `!= 'no'` would read an unset output as "stop here" and skip every
    rerun -- and, before dispatches were guarded, every manual cycle.
    """
    steps = _heartbeat()["jobs"]["cycle"]["steps"]
    cycle = next(s for s in steps if s.get("name") == "Run one cycle")
    assert cycle["if"] == "steps.guard.outputs.skip != 'yes' && inputs.mode != 'protect'"


def test_the_guard_asks_the_three_way_question_and_names_each_answer():
    guard = next(s for s in _heartbeat()["jobs"]["cycle"]["steps"] if s.get("id") == "guard")
    run = guard["run"]
    assert "python analysis/cycle_day.py --journal logs/signal_journal.log --decide" in run
    for answer in ("run)", "already)", "too_late)"):
        assert answer in run, answer
    assert 'echo "skip=no"' in run
    assert 'echo "skip=yes"; echo "why=already"' in run
    assert 'echo "skip=yes"; echo "why=too_late"' in run
    # Anything else is the script misbehaving, and must be loud, not a run.
    assert "exit 1" in run


def test_a_protect_only_dispatch_places_stops_and_runs_no_cycle():
    """The protection pass is its own door: no model, no signals, no report,
    no refit -- and the audit log it writes is still committed."""
    wf = _heartbeat()
    mode = wf[True]["workflow_dispatch"]["inputs"]["mode"]  # `on` parses as True
    assert mode["options"] == ["cycle", "protect"] and mode["default"] == "cycle"
    steps = wf["jobs"]["cycle"]["steps"]
    by_name = {s.get("name"): s for s in steps}
    protect = by_name["Protect every open position"]
    assert protect["run"].strip() == "python -m orchestrator.heartbeat --protect-only"
    assert set(protect["env"]) == {"EXECUTION_MODE", "ALPACA_API_KEY", "ALPACA_SECRET_KEY"}
    assert "ANTHROPIC_API_KEY" not in protect["env"]  # no model is consulted
    for name in ("Run one cycle", "Render the cycle for a human", "Refit the blend weights",
                 "Score the journal", "Push the archive to Supabase"):
        assert "inputs.mode != 'protect'" in by_name[name]["if"], name
    assert "inputs.mode" not in by_name["Commit the journal"]["if"]
    assert "logs/execution_audit.log" in by_name["Commit the journal"]["run"]


# --------------------------------------------------------------------------- #
# may a cycle still start? (the guard's --decide)
# --------------------------------------------------------------------------- #



def test_no_cycle_yet_in_the_morning_is_run():
    now = datetime(2026, 9, 25, 14, 45, tzinfo=UTC)          # 10:45 New York
    assert start_decision([], now) == "run"


def test_a_cycle_already_journalled_is_already():
    now = datetime(2026, 9, 25, 17, 40, tzinfo=UTC)
    earlier = _entries(_line("MSFT", datetime(2026, 9, 25, 15, 8, tzinfo=UTC)))
    assert start_decision(earlier, now) == "already"


def test_yesterdays_cycle_does_not_make_today_already():
    now = datetime(2026, 9, 25, 15, 0, tzinfo=UTC)
    yesterday = _entries(_line("MSFT", datetime(2026, 9, 24, 15, 36, tzinfo=UTC)))
    assert start_decision(yesterday, now) == "run"


def test_the_latest_safe_start_is_14_30_new_york_in_summer():
    """EDT is UTC-4: 14:30 New York is 18:30 UTC."""
    assert LATEST_START_NY.strftime("%H:%M") == "14:30"
    assert start_decision([], datetime(2026, 9, 25, 18, 29, 59, tzinfo=UTC)) == "run"
    assert start_decision([], datetime(2026, 9, 25, 18, 30, tzinfo=UTC)) == "too_late"


def test_the_latest_safe_start_moves_with_new_york_in_winter():
    """EST is UTC-5: the same 18:30 UTC is only 13:30 New York in December,
    still safe; the cut-off is 19:30 UTC. A fixed UTC hour would be wrong
    in one season or the other."""
    assert start_decision([], datetime(2026, 12, 2, 18, 30, tzinfo=UTC)) == "run"
    assert start_decision([], datetime(2026, 12, 2, 19, 29, tzinfo=UTC)) == "run"
    assert start_decision([], datetime(2026, 12, 2, 19, 30, tzinfo=UTC)) == "too_late"


def test_a_half_day_closes_at_13_00_and_the_latest_start_is_11_30():
    """27 Nov 2026 (the day after Thanksgiving) is EST, UTC-5: 11:30 New York
    is 16:30 UTC. A run started at 12:40 New York would send its orders into
    the 13:00 close, which a 16:00 cut-off would have let through."""
    assert date(2026, 11, 27) in EARLY_CLOSES
    assert closes_at(date(2026, 11, 27)).strftime("%H:%M") == "13:00"
    assert latest_start(date(2026, 11, 27)).strftime("%H:%M") == "11:30"
    assert start_decision([], datetime(2026, 11, 27, 16, 29, 59, tzinfo=UTC)) == "run"
    assert start_decision([], datetime(2026, 11, 27, 16, 30, tzinfo=UTC)) == "too_late"
    assert start_decision([], datetime(2026, 11, 27, 17, 40, tzinfo=UTC)) == "too_late"
    # An ordinary day keeps 16:00 and 14:30.
    assert closes_at(date(2026, 11, 30)).strftime("%H:%M") == "16:00"
    assert latest_start(date(2026, 11, 30)) == LATEST_START_NY
    assert start_decision([], datetime(2026, 11, 30, 17, 40, tzinfo=UTC)) == "run"


def test_every_half_day_is_a_weekday_the_market_trades():
    """A half day is a real session: never a weekend, never a full holiday,
    and within the years the holiday list covers."""
    years = {d.year for d in NYSE_HOLIDAYS}
    for day in EARLY_CLOSES:
        assert day.weekday() < 5 and is_trading_day(day) and day not in NYSE_HOLIDAYS, day
        assert day.year in years, day
    # The two known ones this year and next.
    assert {date(2026, 11, 27), date(2026, 12, 24), date(2027, 11, 26)} <= EARLY_CLOSES


def test_already_wins_over_too_late():
    """Both are true late in a day that ran; 'the day is covered' is the one to say."""
    now = datetime(2026, 9, 25, 20, 36, tzinfo=UTC)
    ran = _entries(_line("MSFT", datetime(2026, 9, 25, 15, 8, tzinfo=UTC)))
    assert start_decision(ran, now) == "already"


def test_the_late_github_crons_of_21_to_24_sep_are_now_stopped():
    """The deliveries the orchestrator measured. The 12:35 ones (17:11-18:17
    UTC) came after the Routine's cycle and are 'already'; the 17:35 ones
    (20:23-21:11 UTC) are past 14:30 New York even on a day with no cycle."""
    cycle = {21: (15, 8), 22: (15, 7), 23: (15, 6), 24: (15, 8)}
    late = {21: [(18, 17), (21, 11)], 22: [(17, 11), (20, 23)],
            23: [(17, 23), (20, 36)], 24: [(17, 27), (20, 39)]}
    for day, deliveries in late.items():
        ran = _entries(_line("MSFT", datetime(2026, 9, day, *cycle[day], tzinfo=UTC)))
        for hour, minute in deliveries:
            assert start_decision(ran, datetime(2026, 9, day, hour, minute, tzinfo=UTC)) == "already"
        assert start_decision([], datetime(2026, 9, day, *deliveries[1], tzinfo=UTC)) == "too_late"


def test_a_naive_now_is_read_as_utc():
    assert start_decision([], datetime(2026, 9, 25, 18, 30)) == "too_late"


def test_cli_decide_prints_one_word_and_exits_zero(tmp_path, capsys):
    path = tmp_path / "journal.log"
    path.write_text(_line("MSFT", datetime(2026, 9, 25, 15, 8, tzinfo=UTC)) + "\n")
    assert main(["--journal", str(path), "--decide", "--now", "2026-09-25T17:40:00+00:00"]) == 0
    assert capsys.readouterr().out.strip() == "already"
    assert main(["--journal", str(tmp_path / "absent.log"), "--decide",
                 "--now", "2026-09-25T15:00:00+00:00"]) == 0
    assert capsys.readouterr().out.strip() == "run"
    assert main(["--journal", str(tmp_path / "absent.log"), "--decide",
                 "--now", "2026-09-25T19:00:00Z"]) == 0
    assert capsys.readouterr().out.strip() == "too_late"


def test_the_old_yes_no_question_still_answers_the_old_way(tmp_path, capsys):
    """Anything that still asks without --decide gets yes or no, as before."""
    path = tmp_path / "journal.log"
    path.write_text(_line("MSFT", datetime(2026, 9, 25, 15, 8, tzinfo=UTC)) + "\n")
    assert main(["--journal", str(path), "--day", "2026-09-25"]) == 0
    assert capsys.readouterr().out.strip() == "yes"


# --------------------------------------------------------------------------- #
# ...and has another run today already reached its trading step?
# --------------------------------------------------------------------------- #

#: When GitHub delivered the 14:40 cron on 21-24 Sep: about 13:30 New York,
#: well before the latest safe start, with the day's Routine run long done.
LATE_CRON = datetime(2026, 9, 25, 17, 30, tzinfo=UTC)


def _run(id: int = 41, status: str = "completed", conclusion: str | None = "failure",
         title: str = "heartbeat cycle (manual)",
         created: datetime = datetime(2026, 9, 25, 15, 5, tzinfo=UTC)) -> dict:
    """One run as GitHub lists it."""
    return {"id": id, "display_title": title, "status": status,
            "conclusion": conclusion if status == "completed" else None,
            "created_at": created.strftime("%Y-%m-%dT%H:%M:%SZ")}


def _jobs(*steps: tuple[str, str | None], attempt: int | None = None, status: str = "completed",
          ran: tuple[datetime, datetime] | None = None) -> dict:
    """GitHub's jobs answer for one run: ``(step name, conclusion)`` pairs.

    ``ran`` is when every step started and completed, as GitHub stamps them;
    without it the steps carry no times, which counts as "may have traded"."""
    job = {"name": "cycle", "steps": [{"name": name, "status": status, "conclusion": conclusion}
                                      for name, conclusion in steps]}
    if ran is not None:
        for step in job["steps"]:
            step["started_at"], step["completed_at"] = (t.strftime("%Y-%m-%dT%H:%M:%SZ") for t in ran)
    if attempt is not None:
        job["run_attempt"] = attempt
    return {"total_count": 1, "jobs": [job]}


#: The owner's case: the run traded, then its journal push was refused.
TRADED = _jobs(("May this run start a cycle?", "success"), ("Run one cycle", "success"),
               ("Commit the journal", "failure"))
#: A run its guard stopped: the trading step skipped.
STOPPED = _jobs(("May this run start a cycle?", "success"), ("Run one cycle", "skipped"),
                ("Commit the journal", "skipped"))


def test_a_late_cron_after_a_run_that_traded_and_lost_its_record_stops():
    """The gap the journal alone left open. The Routine's run traded at 15:05
    and its commit never reached the branch, so the journal says "no cycle";
    the 14:40 cron, delivered at 17:30, used to pass the guard and sell the
    same profit-ladder rungs a second time."""
    assert start_decision([], LATE_CRON) == "run"            # the journal alone
    check = check_start([], LATE_CRON, other_runs=[(_run(), TRADED)])
    assert check.decision == "already" and check.reached["id"] == 41
    assert check.journalled is False


@pytest.mark.parametrize("conclusion", ["success", "failure", "cancelled"])
def test_a_trading_step_that_started_stops_the_day_whatever_it_ended_as(conclusion):
    """Green included: a run that started before the open stopped at the
    market-closed gate and a run on another branch look the same from here as
    one that traded, and only a person can tell them apart."""
    answer = _jobs(("Run one cycle", conclusion))
    for run_conclusion in ("success", "failure", "cancelled", "timed_out"):
        other = [(_run(conclusion=run_conclusion), answer)]
        assert start_decision([], LATE_CRON, other_runs=other) == "already", run_conclusion


def test_a_run_whose_trading_step_is_running_now_stops_the_day():
    """The concurrency group should make this impossible; if it ever is not,
    two cycles side by side is the worse way to be wrong."""
    running = _run(status="in_progress")
    answer = _jobs(("May this run start a cycle?", "success"), ("Run one cycle", None), status="in_progress")
    assert start_decision([], LATE_CRON, other_runs=[(running, answer)]) == "already"


@pytest.mark.parametrize("answer", [
    STOPPED,                                              # its guard said stop
    _jobs(("Set up job", "success"), ("Run pip install -r requirements.txt", "failure"),
          ("Run one cycle", "skipped")),                  # failed before it
    _jobs(("Set up job", "failure")),                     # never listed: never reached
    {"total_count": 0, "jobs": []},                       # never got a machine
])
def test_a_run_that_never_reached_its_trading_step_leaves_the_day_open(answer):
    for conclusion in ("success", "failure", "cancelled"):
        assert start_decision([], LATE_CRON, other_runs=[(_run(conclusion=conclusion), answer)]) == "run"


@pytest.mark.parametrize("status", ["queued", "pending", "waiting", "requested"])
def test_a_run_still_waiting_for_a_machine_has_reached_nothing(status):
    """It is queued behind this one and lists no jobs yet; its own guard will
    see this run."""
    for answer in ({"total_count": 0, "jobs": []},
                   {"jobs": [{"name": "cycle", "status": "queued", "steps": []}]}):
        assert start_decision([], LATE_CRON, other_runs=[(_run(status=status), answer)]) == "run"


@pytest.mark.parametrize("status", ["queued", "pending", "waiting", "requested", "in_progress"])
def test_a_run_that_traded_and_was_re_run_from_its_page_counts_while_it_waits(status):
    """Run 41 traded and lost its record; this run took the concurrency group;
    then someone pressed "Re-run" on 41, which now waits as "pending". Its
    jobs answer (every attempt) still holds the attempt that traded. Reading
    the status instead of the steps let this run trade the day again."""
    waiting = {"total_count": 2, "jobs": [
        {"name": "cycle", "run_attempt": 2, "status": "queued", "steps": []},
        {**TRADED["jobs"][0], "run_attempt": 1},
    ]}
    check = check_start([], LATE_CRON, other_runs=[(_run(status=status), waiting)])
    assert check.decision == "already" and check.reached["id"] == 41


# --------------------------------------------------------------------------- #
# ...but not by a trading step that was over before the open
# --------------------------------------------------------------------------- #

#: 08:00-08:01 New York on 25 Sep (EDT): the owner dispatching at 15:00 in
#: Israel. The cycle asks the broker's clock, finds the market shut, and
#: stops with nothing journalled and a green run.
PRE_MARKET = (datetime(2026, 9, 25, 12, 0, 20, tzinfo=UTC), datetime(2026, 9, 25, 12, 1, 5, tzinfo=UTC))


def _early(*times: datetime) -> dict:
    return _jobs(("May this run start a cycle?", "success"), ("Run one cycle", "success"),
                 ("Commit the journal", "success"), ran=times or PRE_MARKET)


def test_a_run_started_before_the_open_does_not_use_up_the_day():
    """The reviewer's case: an 08:00 New York dispatch, then the 14:40 cron.
    The engine and the profit ladder both refuse to act while the market is
    shut, so a trading step over before 09:30 New York placed nothing, and
    the cron is the day's cycle."""
    early = _run(id=7, conclusion="success", created=datetime(2026, 9, 25, 12, 0, tzinfo=UTC))
    cron = datetime(2026, 9, 25, 14, 40, tzinfo=UTC)
    assert start_decision([], cron, other_runs=[(early, _early())]) == "run"
    # Without the step's times it cannot be shown to have been early: it counts.
    assert start_decision([], cron, other_runs=[(early, TRADED)]) == "already"


def test_yesterdays_cron_delivered_after_midnight_new_york_does_not_use_up_the_day():
    """00:30 New York on the 25th is today's date there, before the open."""
    late = _run(id=8, title="heartbeat cycle (schedule)", conclusion="success",
                created=datetime(2026, 9, 25, 4, 30, tzinfo=UTC))
    ran = (datetime(2026, 9, 25, 4, 31, tzinfo=UTC), datetime(2026, 9, 25, 4, 32, tzinfo=UTC))
    assert start_decision([], LATE_CRON, other_runs=[(late, _early(*ran))]) == "run"


@pytest.mark.parametrize("started, ended, counts", [
    ((13, 29), (13, 29, 59), False),     # over at 09:29:59 EDT
    ((13, 29), (13, 30), True),          # still running at the open
    ((13, 35), (14, 20), True),          # after the open
    ((14, 20), (14, 25), True),          # 10:20 EDT: well after the open
])
def test_the_open_is_09_30_new_york_in_summer(started, ended, counts):
    ran = tuple(datetime(2026, 9, 25, *hm, tzinfo=UTC) for hm in (started, ended))
    other = [(_run(conclusion="success"), _early(*ran))]
    assert (start_decision([], LATE_CRON, other_runs=other) == "already") is counts


def test_the_open_is_14_30_utc_in_winter():
    """EST: 09:30 New York is 14:30 UTC, an hour later against UTC."""
    december = datetime(2026, 12, 2, 17, 30, tzinfo=UTC)
    created = datetime(2026, 12, 2, 14, 0, tzinfo=UTC)
    before = (datetime(2026, 12, 2, 14, 20, tzinfo=UTC), datetime(2026, 12, 2, 14, 21, tzinfo=UTC))
    after = (datetime(2026, 12, 2, 14, 31, tzinfo=UTC), datetime(2026, 12, 2, 14, 32, tzinfo=UTC))
    early = _run(conclusion="success", created=created)
    assert start_decision([], december, other_runs=[(early, _early(*before))]) == "run"
    assert start_decision([], december, other_runs=[(early, _early(*after))]) == "already"


def test_a_protection_pass_never_stops_a_cycle():
    """It never runs "Run one cycle"; its title says what it is."""
    protect = _run(title="heartbeat protect", conclusion="success")
    assert start_decision([], LATE_CRON, other_runs=[(protect, TRADED)]) == "run"


def test_only_todays_new_york_runs_count():
    yesterday = _run(created=datetime(2026, 9, 24, 15, 5, tzinfo=UTC))
    # 00:10 UTC on the 25th is 20:10 on the 24th in New York: yesterday's.
    last_night = _run(created=datetime(2026, 9, 25, 0, 10, tzinfo=UTC))
    other = [(yesterday, TRADED), (last_night, TRADED)]
    assert start_decision([], LATE_CRON, other_runs=other) == "run"


def test_steps_that_cannot_be_read_leave_that_run_to_the_journal():
    """A GitHub hiccup must not cost the day; it is reported, not hidden."""
    for answer in (None, "junk", {}, {"jobs": "nope"}, {"jobs": [5]}):
        check = check_start([], LATE_CRON, other_runs=[(_run(id=7), answer)])
        assert check.decision == "run" and check.unread == ("7",), answer
    # And the journal still decides on its own.
    ran = _entries(_line("MSFT", datetime(2026, 9, 25, 15, 8, tzinfo=UTC)))
    assert start_decision(ran, LATE_CRON, other_runs=[(_run(id=7), None)]) == "already"


def test_another_run_that_traded_wins_over_too_late():
    """Past 14:30 New York either stops the run; "the day already had its
    cycle" is the true reason, as with a journalled one."""
    late = datetime(2026, 9, 25, 19, 0, tzinfo=UTC)
    assert start_decision([], late) == "too_late"
    assert start_decision([], late, other_runs=[(_run(), TRADED)]) == "already"


def test_the_journal_is_asked_first():
    ran = _entries(_line("MSFT", datetime(2026, 9, 25, 15, 8, tzinfo=UTC)))
    check = check_start(ran, LATE_CRON, other_runs=[(_run(), TRADED)])
    assert check.decision == "already" and check.journalled and check.reached is None


# --------------------------------------------------------------------------- #
# which runs are "other": never this one, except its earlier attempts
# --------------------------------------------------------------------------- #

def test_the_asking_run_is_left_out():
    """This run's own trading step is listed and not yet skipped while its
    guard runs; counting it would stop every run."""
    me = _run(id=99, status="in_progress")
    mine = _jobs(("May this run start a cycle?", None), ("Run one cycle", None),
                 attempt=1, status="in_progress")
    pairs = other_runs_from([me, _run(id=41)], {"99": mine, "41": STOPPED}, this_run="99", this_attempt="1")
    assert [run["id"] for run, _ in pairs] == [41]
    assert start_decision([], LATE_CRON, other_runs=pairs) == "run"


def test_a_re_run_from_githubs_page_checks_its_own_earlier_attempts():
    """Pressing "Re-run" on a red run keeps its id. If attempt 1 traded and
    lost its record, attempt 2 is a second cycle like any other."""
    me = _run(id=99, status="in_progress")
    both = {"total_count": 2, "jobs": [
        {"name": "cycle", "run_attempt": 2, "status": "in_progress",
         "steps": [{"name": "Run one cycle", "status": "queued", "conclusion": None}]},
        {**TRADED["jobs"][0], "run_attempt": 1},
    ]}
    pairs = other_runs_from([me], {"99": both}, this_run=99, this_attempt="2")
    check = check_start([], LATE_CRON, other_runs=pairs)
    assert check.decision == "already"
    assert "an earlier attempt of this run" in start_summary(check, runs_read=True)[0]
    # Attempt 1 stopped at its guard: attempt 2 may run.
    stopped = {"jobs": [both["jobs"][0], {**STOPPED["jobs"][0], "run_attempt": 1}]}
    assert start_decision([], LATE_CRON, other_runs_from([me], {"99": stopped}, this_run=99,
                                                         this_attempt="2")) == "run"
    # A job that cannot say which attempt it was is not counted against itself.
    anonymous = {"jobs": [{**TRADED["jobs"][0]}]}
    assert start_decision([], LATE_CRON, other_runs_from([me], {"99": anonymous}, this_run=99,
                                                         this_attempt="2")) == "run"


# --------------------------------------------------------------------------- #
# "Re-run" on a run that was dispatched with `rerun`
# --------------------------------------------------------------------------- #

#: A rescue dispatched with `rerun` at 15:05 on the 25th, re-run from its page.
RESCUE = _run(id=99, status="in_progress", created=datetime(2026, 9, 25, 15, 5, tzinfo=UTC))


def _rerun_pairs(attempt_one: dict | None, run: dict = RESCUE, others: tuple = ()) -> list:
    """What the guard of attempt 2 reads: attempt 1's jobs (None: unreadable)."""
    jobs = {str(run["id"]): None if attempt_one is None else {"jobs": [
        {"name": "cycle", "run_attempt": 2, "status": "in_progress",
         "steps": [{"name": "Run one cycle", "status": "queued", "conclusion": None}]},
        {**attempt_one["jobs"][0], "run_attempt": 1},
    ]}}
    jobs.update({str(other["id"]): answer for other, answer in others})
    return other_runs_from([run, *(other for other, _ in others)], jobs, this_run=run["id"],
                           this_attempt="2")


def test_re_running_a_rerun_that_traded_stops():
    """The rescue traded, its push was refused three times, the run went red,
    and the owner pressed "Re-run failed jobs". The re-run replays `rerun`;
    without the guard attempt 2 would sell the same profit-ladder rungs."""
    check = check_start([], LATE_CRON, _rerun_pairs(TRADED), rerun=True)
    assert check.decision == "already" and check.rerun is True
    [line] = start_summary(check, runs_read=True)
    assert line.startswith("An earlier attempt of this run already reached its trading step.")
    assert "start heartbeat by hand (Run workflow) with rerun ticked" in line


def test_re_running_a_rerun_that_never_traded_still_runs_as_rerun_asked():
    """Attempt 1 failed before its trading step (pip install, say). `rerun`
    still gets past the journal, the other runs and the clock, as it did."""
    journalled = _entries(_line("MSFT", datetime(2026, 9, 25, 15, 8, tzinfo=UTC)))
    other = (_run(id=41), TRADED)
    too_late = datetime(2026, 9, 25, 19, 0, tzinfo=UTC)
    for entries, now, others in (([], LATE_CRON, ()), (journalled, LATE_CRON, (other,)),
                                 ([], too_late, (other,))):
        pairs = _rerun_pairs(_jobs(("Run one cycle", "skipped")), others=others)
        check = check_start(entries, now, pairs, rerun=True)
        assert check.decision == "run" and check.rerun is True, (now, others)
    assert start_summary(check)[0].endswith("so it runs, as rerun asked.")


def test_re_running_a_rerun_whose_attempts_cannot_be_read_stops():
    """A person is at the page and can dispatch afresh; the unattended
    fallback (the journal alone) is not for this."""
    for pairs in (_rerun_pairs(None), None):
        check = check_start([], LATE_CRON, pairs, rerun=True)
        assert check.decision == "already" and check.rerun is True
        assert start_summary(check)[0].startswith(
            "The steps of this run's earlier attempts could not be read.")


def test_a_rerun_from_an_earlier_day_re_run_today_is_guarded_like_any_other_run():
    """Its `rerun` was given for the 24th. Re-run on the 25th, it must not get
    past today's journal -- nor today's run that traded."""
    yesterday = _run(id=99, status="in_progress", created=datetime(2026, 9, 24, 15, 5, tzinfo=UTC))
    journalled = _entries(_line("MSFT", datetime(2026, 9, 25, 15, 8, tzinfo=UTC)))
    pairs = _rerun_pairs(STOPPED, run=yesterday)
    check = check_start(journalled, LATE_CRON, pairs, rerun=True)
    assert check.decision == "already" and check.journalled and check.rerun is False
    assert "on an earlier New York day" in start_summary(check, runs_read=True)[0]
    # Not listed at all (the list only reaches back to today): the same.
    assert check_start([], LATE_CRON, other_runs_from([], {}, this_run=99, this_attempt="2"),
                       rerun=True).rerun is False
    traded_today = _rerun_pairs(STOPPED, run=yesterday, others=((_run(id=41), TRADED),))
    assert start_decision([], LATE_CRON, traded_today, rerun=True) == "already"
    assert start_decision([], LATE_CRON, _rerun_pairs(STOPPED, run=yesterday), rerun=True) == "run"


def test_cli_re_run_of_a_rerun(tmp_path, capsys):
    journal = ["--journal", str(tmp_path / "absent.log"), "--decide", "--now", LATE_CRON.isoformat()]
    both = {"jobs": [{"name": "cycle", "run_attempt": 2, "status": "in_progress", "steps": []},
                     {**TRADED["jobs"][0], "run_attempt": 1}]}
    record = _save(tmp_path, {"workflow_runs": [RESCUE]}, {"99": both})
    assert main(journal + record + ["--this-run", "99", "--this-attempt", "2", "--rerun", "true"]) == 0
    out, err = capsys.readouterr()
    assert out == "already\n" and "An earlier attempt of this run" in err
    # The first attempt of a rerun never reaches the guard; asked anyway, the
    # flag is ignored rather than read as "this attempt traded".
    assert main(journal + record + ["--this-run", "99", "--this-attempt", "1", "--rerun", "true"]) == 0
    assert capsys.readouterr().out == "run\n"
    # A scheduled run's empty input, and a dispatch's false, are not rerun.
    for value in ("", "false"):
        assert main(journal + record + ["--this-run", "99", "--this-attempt", "2", "--rerun", value]) == 0
        out, err = capsys.readouterr()
        assert out == "already\n" and "Another run today already reached" in err


def test_no_run_list_means_the_journal_alone():
    assert other_runs_from(None, {"41": TRADED}, this_run="99", this_attempt="1") is None
    assert check_start([], LATE_CRON, None).decision == "run"
    pairs = other_runs_from(["junk", 5, _run()], {"41": TRADED}, this_run="", this_attempt="")
    assert start_decision([], LATE_CRON, other_runs=pairs) == "already"


# --------------------------------------------------------------------------- #
# what the job summary says
# --------------------------------------------------------------------------- #

def test_the_summary_names_the_run_and_the_way_past():
    check = check_start([], LATE_CRON, other_runs=[(_run(id=41), TRADED)])
    [line] = start_summary(check, runs_read=True)
    assert line == ("Another run today already reached its trading step (run 41, failure); a second "
                    "cycle could repeat profit-ladder sales. This run stops here. Re-run by hand "
                    "with rerun only after checking the account.")


def test_the_summary_says_when_github_could_not_be_read():
    lines = start_summary(check_start([], LATE_CRON, None), runs_read=False)
    assert lines[0].endswith("Running one now.")
    assert "decided from the journal alone" in lines[1]
    unread = check_start([], LATE_CRON, other_runs=[(_run(id=7), None), (_run(id=8), None)])
    assert "The steps of runs 7, 8 could not be read" in start_summary(unread, runs_read=True)[1]
    # Asked for nothing, it claims nothing.
    assert start_summary(check_start([], LATE_CRON), runs_read=None) == [
        "No cycle journalled for today. Running one now."]


def _save(tmp_path: Path, runs, jobs: dict) -> list[str]:
    (tmp_path / "runs.json").write_text(runs if isinstance(runs, str) else json.dumps(runs))
    (tmp_path / "jobs").mkdir(exist_ok=True)
    for run_id, answer in jobs.items():
        (tmp_path / "jobs" / f"{run_id}.json").write_text(json.dumps(answer))
    return ["--runs", str(tmp_path / "runs.json"), "--jobs", str(tmp_path / "jobs")]


def test_cli_reads_githubs_record_and_still_prints_one_word(tmp_path, capsys):
    journal = ["--journal", str(tmp_path / "absent.log"), "--decide", "--now", LATE_CRON.isoformat()]
    record = _save(tmp_path, {"total_count": 2, "workflow_runs": [_run(id=99, status="in_progress"), _run()]},
                   {"41": TRADED})
    assert main(journal + record + ["--this-run", "99", "--this-attempt", "1"]) == 0
    out, err = capsys.readouterr()
    assert out == "already\n"
    assert "another run today already reached its trading step (run 41, failure)" in err.lower()
    # Without the record, the same journal says run: the record is what stopped it.
    assert main(journal) == 0
    assert capsys.readouterr().out == "run\n"


def test_cli_with_an_unreadable_record_decides_from_the_journal_and_says_so(tmp_path, capsys):
    journal = ["--journal", str(tmp_path / "absent.log"), "--decide", "--now", LATE_CRON.isoformat()]
    for runs in ("<html>rate limited</html>", "{}"):
        assert main(journal + _save(tmp_path, runs, {}) + ["--this-run", "99"]) == 0
        out, err = capsys.readouterr()
        assert out == "run\n", runs
        assert "decided from the journal alone" in err
    missing = ["--runs", str(tmp_path / "gone.json"), "--jobs", str(tmp_path / "nowhere")]
    assert main(journal + missing) == 0
    assert capsys.readouterr().out == "run\n"


# --------------------------------------------------------------------------- #
# the run block every journal line of a cycle carries
# --------------------------------------------------------------------------- #

def test_a_scheduled_run_on_time():
    block = run_block(event="schedule", started_by="", run_id=17234567890,
                      started_at=datetime(2026, 9, 28, 14, 41, 12, 345678, tzinfo=UTC))
    assert block == {
        "trigger": "schedule",
        "source": "github-schedule",
        "scheduled_for": "2026-09-28T14:40:00+00:00",
        "started_at": "2026-09-28T14:41:12+00:00",
        "minutes_late": 1,
        "late": False,
        "run_id": "17234567890",
    }


def test_the_scheduled_time_is_the_days_start_whatever_started_the_run():
    """A backup at 15:12 is 32 minutes late against the same 14:40."""
    block = run_block(event="workflow_dispatch", started_by="backup", run_id="1",
                      started_at=datetime(2026, 9, 28, 15, 12, tzinfo=UTC))
    assert block["trigger"] == "backup"
    assert block["scheduled_for"] == "2026-09-28T14:40:00+00:00"
    assert block["minutes_late"] == 32 and block["late"] is True


def test_what_started_the_run():
    assert trigger_for("schedule", "") == "schedule"
    assert trigger_for("schedule", "backup") == "schedule"     # a cron has no inputs anyway
    assert trigger_for("workflow_dispatch", "backup") == "backup"
    assert trigger_for("workflow_dispatch", " Backup ") == "backup"
    assert trigger_for("workflow_dispatch", "manual") == "manual"
    # The Routines of 25 Sep dispatch {"mode": "cycle"} only: the default.
    assert trigger_for("workflow_dispatch", "") == "manual"
    assert trigger_for("", None) == "manual"


def test_late_means_more_than_thirty_minutes():
    def late(minute: int, second: int = 0) -> dict:
        return run_block(event="schedule", started_by="", run_id="1",
                         started_at=datetime(2026, 9, 28, 15, minute, second, tzinfo=UTC))

    assert (late(10)["minutes_late"], late(10)["late"]) == (30, False)
    assert (late(10, 59)["minutes_late"], late(10, 59)["late"]) == (30, False)   # floored
    assert (late(11)["minutes_late"], late(11)["late"]) == (31, True)


def test_a_run_before_its_time_is_negative_minutes_late():
    block = run_block(event="workflow_dispatch", started_by="manual", run_id="9",
                      started_at=datetime(2026, 9, 28, 14, 20, 30, tzinfo=UTC))
    assert block["minutes_late"] == -20      # floor(-19.5)
    assert block["late"] is False


def test_the_scheduled_start_is_the_first_heartbeat_cron():
    """One number in two places: pinned so they cannot drift apart."""
    first = _heartbeat()[True]["schedule"][0]["cron"]
    minute, hour = first.split()[:2]
    assert (int(hour), int(minute)) == (SCHEDULED_START_UTC.hour, SCHEDULED_START_UTC.minute)


def test_cli_run_block_is_one_line_of_json(capsys):
    assert main(["--run-block", "--event", "workflow_dispatch", "--started-by", "backup",
                 "--run-id", "42", "--now", "2026-09-28T15:12:00Z"]) == 0
    out = capsys.readouterr().out
    assert out.count("\n") == 1
    block = json.loads(out)
    assert block["trigger"] == "backup" and block["run_id"] == "42" and block["minutes_late"] == 32


def test_the_run_block_is_what_the_journal_reads_back(monkeypatch):
    """The CLI's output, set as HEARTBEAT_RUN, is what journal.run_block returns."""
    from orchestrator import journal

    block = run_block(event="schedule", started_by="", run_id="5",
                      started_at=datetime(2026, 9, 28, 14, 55, tzinfo=UTC))
    monkeypatch.setenv("HEARTBEAT_RUN", json.dumps(block))
    assert journal.run_block() == block
