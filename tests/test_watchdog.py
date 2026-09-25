"""The watchdog: has today's trading run started, and if not, what now?

Every rule in ``analysis.watchdog.decide`` is pinned here, in the order the
function applies them, with the two things that make timing code wrong in
practice: a New York holiday that is an ordinary day in UTC, and a winter
date on which New York is an hour further from UTC than in summer.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from analysis import watchdog
from analysis.reader import read_lines
from analysis.watchdog import Decision, decide, main

UTC = timezone.utc
ROOT = Path(__file__).resolve().parents[1]

#: A Friday in summer time (EDT, UTC-4).
FRIDAY = datetime(2026, 9, 25, tzinfo=UTC)


def at(hour: int, minute: int = 0, day: datetime = FRIDAY) -> datetime:
    return day.replace(hour=hour, minute=minute)


def run(title: str = "heartbeat cycle (schedule)", status: str = "completed", *,
        created: datetime | None = None, started: datetime | None = None,
        conclusion: str | None = "success", updated: datetime | None = None, id: int = 1) -> dict:
    created = created or at(14, 41)
    stamp = lambda d: d.strftime("%Y-%m-%dT%H:%M:%SZ")  # noqa: E731 - GitHub's own format
    return {
        "id": id,
        "display_title": title,
        "status": status,
        "conclusion": conclusion if status == "completed" else None,
        "created_at": stamp(created),
        "run_started_at": stamp(started or created),
        "updated_at": stamp(updated or created + timedelta(minutes=40)),
    }


def steps(*reached: tuple[str, str]) -> dict:
    """GitHub's jobs answer for one run: ``(step name, conclusion)`` pairs."""
    return {"total_count": 1, "jobs": [{"name": "cycle", "steps": [
        {"name": name, "status": "completed", "conclusion": conclusion} for name, conclusion in reached]}]}


#: A run that stopped before it traded: set-up failed, the trading step skipped.
NEVER_TRADED = steps(("Set up job", "success"), ("Run pip install -r requirements.txt", "failure"),
                     ("Run one cycle", "skipped"), ("Commit the journal", "skipped"))
#: A run that reached the trading step and then went red.
TRADED = steps(("May this run start a cycle?", "success"), ("Run one cycle", "success"),
               ("Commit the journal", "failure"))
#: A run that reached the trading step and went green, and yet wrote nothing
#: to this branch's journal: most likely on another branch.
TRADED_GREEN = steps(("May this run start a cycle?", "success"), ("Run one cycle", "success"),
                     ("Commit the journal", "success"))


def timed(answer: dict, started: datetime, ended: datetime) -> dict:
    """``answer`` with every step stamped as GitHub stamps them."""
    stamp = lambda d: d.strftime("%Y-%m-%dT%H:%M:%SZ")  # noqa: E731
    return {**answer, "jobs": [{**job, "steps": [{**step, "started_at": stamp(started),
                                                   "completed_at": stamp(ended)}
                                                  for step in job["steps"]]}
                               for job in answer["jobs"]]}


#: A green run started at 08:00 New York (12:00 UTC in summer): its trading
#: step asked the broker's clock, found the market shut, and stopped.
BEFORE_THE_OPEN = timed(TRADED_GREEN, at(12, 0), at(12, 1))
#: A run its guard stopped: green, with every step after the guard skipped.
STOPPED_AT_GUARD = steps(("May this run start a cycle?", "success"), ("Run one cycle", "skipped"),
                         ("Commit the journal", "skipped"))


def journal_today(when: datetime = at(15, 8)):
    line = {"ticker": "MSFT", "ts_utc": when.isoformat(), "signal": {"bias": "NEUTRAL", "conviction": 0.1}}
    return read_lines([json.dumps(line)]).entries


# --------------------------------------------------------------------------- #
# 1. not a trading day
# --------------------------------------------------------------------------- #

def test_a_weekend_is_nothing_to_do():
    saturday = datetime(2026, 9, 26, 16, 0, tzinfo=UTC)
    d = decide(saturday, [], [])
    assert (d.action, d.ping) == ("none", False)
    assert "not a trading day" in d.reason


def test_a_new_york_holiday_is_nothing_to_do():
    """Thanksgiving: an ordinary Thursday in UTC, a closed market in New York."""
    thanksgiving = datetime(2026, 11, 26, 16, 0, tzinfo=UTC)
    d = decide(thanksgiving, [], [])
    assert (d.action, d.ping) == ("none", False)
    assert "2026-11-26" in d.reason


# --------------------------------------------------------------------------- #
# 2. too early to judge
# --------------------------------------------------------------------------- #

def test_before_the_start_plus_thirty_minutes_is_too_early():
    d = decide(at(15, 9), [], [])
    assert (d.action, d.ping) == ("none", False)
    assert "too early" in d.reason


def test_thirty_minutes_after_the_start_it_judges():
    """15:10 UTC is the first watchdog cron, and exactly 14:40 + 30."""
    assert decide(at(15, 10), [], []).action == "dispatch"


def test_the_grace_and_the_start_are_parameters():
    assert decide(at(15, 0), [], [], grace=timedelta(minutes=10)).action == "dispatch"
    assert decide(at(15, 0), [], [], scheduled=at(14, 50).time()).action == "none"


# --------------------------------------------------------------------------- #
# 3. the journal already has today
# --------------------------------------------------------------------------- #

def test_a_cycle_in_the_journal_is_nothing_to_do():
    d = decide(at(15, 40), [run()], journal_today())
    assert (d.action, d.ping) == ("none", False)
    assert "journal" in d.reason


def test_the_journal_wins_even_late_in_the_day():
    """A day that ran is never 'too late'."""
    assert decide(at(20, 40), [], journal_today()).action == "none"


def test_yesterdays_journal_does_not_count():
    yesterday = journal_today(at(15, 8) - timedelta(days=1))
    assert decide(at(15, 40), [], yesterday).action == "dispatch"


# --------------------------------------------------------------------------- #
# 4. a run on its way
# --------------------------------------------------------------------------- #

def test_a_running_cycle_is_nothing_to_do():
    d = decide(at(15, 40), [run(status="in_progress", id=77)], [])
    assert (d.action, d.ping) == ("none", False)
    assert "77" in d.reason


@pytest.mark.parametrize("status", ["queued", "waiting", "requested", "pending"])
def test_a_cycle_waiting_less_than_thirty_minutes_is_nothing_to_do(status):
    d = decide(at(15, 40), [run(status=status, created=at(15, 15))], [])
    assert (d.action, d.ping) == ("none", False)


@pytest.mark.parametrize("status", ["queued", "waiting", "requested", "pending"])
def test_a_cycle_waiting_more_than_thirty_minutes_is_stuck(status):
    """Told, not doubled: a second run would only wait behind the first."""
    d = decide(at(15, 40), [run(status=status, created=at(15, 5))], [])
    assert d.action == "stuck"
    assert d.ping is True and d.priority == 4
    assert "waiting for a GitHub machine" in d.title
    assert "35 minutes" in d.message and "15:05 UTC (18:05 Israel time)" in d.message


def test_a_running_cycle_beside_a_long_queued_one_is_not_stuck():
    """Something is running; the queued one is waiting for it, as designed."""
    runs = [run(status="in_progress", created=at(14, 41)), run(status="pending", created=at(15, 0), id=2)]
    assert decide(at(15, 40), runs, []).action == "none"


def test_a_rerun_attempt_counts_from_when_it_was_asked_for():
    """A run re-run from GitHub's page keeps its morning created_at."""
    queued = run(status="queued", created=at(14, 41), started=at(15, 30))
    assert decide(at(15, 40), [queued], []).action == "none"


def test_runs_from_before_the_new_titles_count_as_cycles():
    """Every run before 25 Sep is titled plain 'heartbeat' and cannot say
    which kind it was; waiting on it is the safe way to be wrong."""
    d = decide(at(15, 40), [run(title="heartbeat", status="in_progress")], [])
    assert d.action == "none"


def test_a_protection_pass_is_not_a_cycle():
    """A running protect pass does not mean the day's cycle is on its way."""
    for title in ("heartbeat protect", "Heartbeat Protect"):
        d = decide(at(15, 40), [run(title=title, status="in_progress")], [])
        assert d.action == "dispatch", title


def test_yesterdays_runs_are_ignored():
    yesterday = run(status="in_progress", created=at(15, 5) - timedelta(days=1))
    assert decide(at(15, 40), [yesterday], []).action == "dispatch"


# --------------------------------------------------------------------------- #
# 5. the backup cap
# --------------------------------------------------------------------------- #

def test_the_backup_stops_after_two_tries():
    runs = [run("heartbeat cycle (backup)", conclusion="failure", created=at(15, 11), id=1),
            run("heartbeat cycle (backup)", conclusion="failure", created=at(15, 41), id=2)]
    d = decide(at(16, 40), runs, [])
    assert d.action == "none"
    assert d.ping is True and d.priority == 5
    assert "2 times" in d.message and "will not try again" in d.message


def test_one_backup_so_far_may_be_followed_by_another():
    runs = [run("heartbeat cycle (backup)", conclusion="failure", created=at(15, 11))]
    d = decide(at(15, 40), runs, [], jobs={"1": NEVER_TRADED})
    assert d.action == "dispatch"
    assert "result 'failure'" in d.message


def test_only_the_watchdogs_own_runs_count_toward_the_cap():
    runs = [run("heartbeat cycle (manual)", conclusion="failure", id=1),
            run("heartbeat cycle (schedule)", conclusion="failure", id=2),
            run("heartbeat cycle (backup)", conclusion="failure", id=3)]
    jobs = {str(i): NEVER_TRADED for i in (1, 2, 3)}
    assert decide(at(16, 40), runs, [], jobs=jobs).action == "dispatch"
    assert decide(at(16, 40), runs, [], jobs=jobs, max_backups=1).action == "none"


# --------------------------------------------------------------------------- #
# 6. a run that may have traded and lost its record
# --------------------------------------------------------------------------- #

@pytest.mark.parametrize("conclusion", ["failure", "cancelled", "timed_out"])
def test_a_run_that_reached_its_trading_step_and_failed_is_never_run_again(conclusion):
    """Its push was refused, or GitHub lost the machine: orders may have gone
    out, and the audit log that counts the profit-ladder rungs went with the
    journal. A second cycle would sell those rungs again, so: tell the owner,
    start nothing."""
    failed = run(conclusion=conclusion, updated=at(15, 20), id=41)
    d = decide(at(15, 40), [failed], [], jobs={"41": TRADED})
    assert d.action == "none"
    assert d.ping is True and d.priority == 5
    assert d.title == "Daily run failed and may have traded: check before starting it again"
    assert "after its trading step had started" in d.message
    assert "profit-ladder" in d.message and "start heartbeat by hand" in d.message
    # A plain dispatch would stop at the guard now; the message names the way past.
    assert "with rerun ticked" in d.message and "any other start stops at its guard" in d.message
    assert f"result '{conclusion}'" in d.message and "15:20 UTC (18:20 Israel time)" in d.message
    assert "41" in d.reason


def test_a_run_re_run_from_githubs_page_still_shows_the_attempt_that_traded():
    """Attempt 1 traded and lost its record; someone pressed "Re-run", and
    attempt 2 stopped at its guard, green. The latest attempt alone would read
    as "never traded" and start a backup; every attempt's jobs do not."""
    rerun_twice = {"total_count": 2, "jobs": [
        {**STOPPED_AT_GUARD["jobs"][0], "run_attempt": 2},
        {**TRADED["jobs"][0], "run_attempt": 1},
    ]}
    d = decide(at(15, 40), [run(conclusion="success", id=41)], [], jobs={"41": rerun_twice})
    assert d.action == "none" and d.priority == 5
    assert "after its trading step had started" in d.message


def test_a_failed_run_whose_steps_cannot_be_read_counts_as_one_that_traded():
    """No jobs answer, or a junk one: the safe way to be wrong is to ask."""
    failed = run(conclusion="failure", id=41)
    for jobs in (None, {}, {"41": "junk"}, {"41": {"jobs": "nope"}}, {"41": {"jobs": [5]}}):
        d = decide(at(15, 40), [failed], [], jobs=jobs)
        assert d.action == "none" and d.priority == 5, jobs
        assert "could not tell whether it had reached its trading step" in d.message


def test_a_failed_run_that_never_reached_the_trading_step_is_started_again():
    failed = run(conclusion="failure", id=41)
    for jobs in (NEVER_TRADED, {"total_count": 0, "jobs": []}, steps(("Set up job", "failure"))):
        assert decide(at(15, 40), [failed], [], jobs={"41": jobs}).action == "dispatch", jobs


def test_a_successful_run_that_reached_its_trading_step_and_wrote_nothing_is_not_run_again():
    """Green means its commit reached the repository -- most likely another
    branch's, and its audit log is not on this one. heartbeat.yml's guard
    stops every later cycle today after a run that reached its trading step,
    whatever its result, so a backup would only stop there -- after the phone
    had said "the backup has started it". The phone hears the truth instead,
    and the one way past: rerun."""
    other = run(conclusion="success", created=at(14, 41), updated=at(15, 2), id=7)
    d = decide(at(15, 40), [other], [], jobs={"7": timed(TRADED_GREEN, at(14, 42), at(15, 1))})
    assert d.action == "none"
    assert d.ping is True and d.priority == 5
    assert d.title == "Daily run succeeded but wrote nothing: check before starting it again"
    assert "result 'success' after its trading step had started" in d.message
    assert "another branch" in d.message and "market-closed gate" not in d.message
    assert "with rerun ticked" in d.message and "any other start stops at its guard" in d.message
    assert "7" in d.reason


def test_a_run_whose_trading_step_was_over_before_the_open_is_started_again():
    """An 08:00 New York dispatch stopped at the market-closed gate: nothing
    was placed and nothing sold, so it must not use up the day. Before this,
    the guard stopped every later cycle after it, and the owner had to start
    the day by hand with rerun."""
    from analysis.cycle_day import start_decision

    early = run(conclusion="success", created=at(12, 0), updated=at(12, 2), id=7)
    d = decide(at(15, 10), [early], [], jobs={"7": BEFORE_THE_OPEN})
    assert d.action == "dispatch" and d.priority == 4
    assert "result 'success' and wrote nothing" in d.message
    # And the backup's guard, a few minutes later, lets it trade.
    assert start_decision([], at(15, 13), other_runs=[(early, BEFORE_THE_OPEN)]) == "run"


def test_a_successful_run_whose_steps_cannot_be_read_is_not_run_again():
    """The safe way to be wrong, as for a failed one -- without claiming the
    guard would stop a backup, which it would not if it could read them."""
    early = run(conclusion="success", id=7)
    d = decide(at(15, 40), [early], [], jobs={})
    assert d.action == "none" and d.priority == 5
    assert "could not tell whether it had reached its trading step" in d.message
    assert "with rerun ticked" in d.message and "stops at its guard" not in d.message


def test_a_successful_run_the_guard_stopped_is_started_again():
    """Green with the trading step skipped: a late cron that reached its guard
    after the latest safe start, say. It placed nothing."""
    stopped = run(conclusion="success", created=at(13, 0), updated=at(13, 2), id=7)
    d = decide(at(15, 40), [stopped], [], jobs={"7": STOPPED_AT_GUARD})
    assert d.action == "dispatch"
    assert "result 'success'" in d.message


def test_a_run_that_may_have_traded_outranks_too_late():
    """After the cut-off, "nothing is traded today" would be false."""
    failed = run(conclusion="failure", id=41)
    assert decide(at(19, 0), [failed], [], jobs={"41": TRADED}).title.startswith("Daily run failed")


@pytest.mark.parametrize("answer, expected", [
    (TRADED, True),
    (steps(("Run one cycle", "failure")), True),
    (steps(("Run one cycle", "cancelled")), True),
    (steps(("Run one cycle", None)), True),          # the machine was lost mid-step
    (NEVER_TRADED, False),
    (steps(("Set up job", "failure")), False),       # never listed: never reached
    ({"total_count": 0, "jobs": []}, False),         # never got a machine
    ({"jobs": [{"name": "cycle", "steps": []}]}, False),
    (None, None), ("junk", None), ({}, None), ({"jobs": None}, None), ({"jobs": ["x"]}, None),
    ({"jobs": [{"steps": "x"}]}, None),
    # Over before the 09:30 open (13:30 UTC in summer): the market was shut.
    (BEFORE_THE_OPEN, False),
    (timed(TRADED, at(13, 20), at(13, 29)), False),
    (timed(TRADED, at(13, 29), at(13, 30)), True),               # still running at the open
    (timed(TRADED, at(3, 50), at(4, 10)), True),                 # across midnight in New York
    (timed(TRADED, at(12, 5), at(12, 0)), True),                 # times out of order: junk
    ({"jobs": [{"steps": [{"name": "Run one cycle", "conclusion": "success",
                           "completed_at": "2026-09-25T12:01:00Z"}]}]}, True),  # no start time
])
def test_trading_step_ran_reads_githubs_jobs_answer(answer, expected):
    assert watchdog.trading_step_ran(answer) is expected


def test_the_open_is_an_hour_later_against_utc_in_winter():
    """EST: 09:30 New York is 14:30 UTC."""
    december = datetime(2026, 12, 2, tzinfo=UTC)
    assert watchdog.trading_step_ran(timed(TRADED, at(14, 20, december), at(14, 29, december))) is False
    assert watchdog.trading_step_ran(timed(TRADED, at(14, 25, december), at(14, 31, december))) is True


# --------------------------------------------------------------------------- #
# 6b. the watchdog and heartbeat.yml's guard give the same answer
# --------------------------------------------------------------------------- #

@pytest.mark.parametrize("conclusion, answer", [
    ("failure", TRADED),                              # traded, record lost
    ("cancelled", steps(("Run one cycle", "cancelled"))),
    ("timed_out", steps(("Run one cycle", None))),    # the machine was lost mid-step
    ("success", TRADED_GREEN),                        # another branch
    ("success", STOPPED_AT_GUARD),                    # its guard said stop
    ("failure", NEVER_TRADED),                        # set-up failed
    ("cancelled", {"total_count": 0, "jobs": []}),    # never got a machine
])
def test_the_backup_starts_exactly_when_its_guard_would_let_it_trade(conclusion, answer):
    """The owner's phone is told "the backup has started it" only on a day the
    backup's own guard will not stop. Both read the same record through the
    same two helpers; this pins that they reach the same verdict on it."""
    from analysis.cycle_day import start_decision

    earlier = run(conclusion=conclusion, created=at(15, 5), updated=at(15, 20), id=41)
    backup = decide(at(15, 40), [earlier], [], jobs={"41": answer})
    # The backup reaches its guard a few minutes later, and sees the same run.
    guard = start_decision([], at(15, 43), other_runs=[(earlier, answer)])
    assert (backup.action == "dispatch") == (guard == "run"), (backup.reason, guard)
    assert backup.action in ("dispatch", "none")
    if guard == "already":
        assert backup.ping and backup.priority == 5


# --------------------------------------------------------------------------- #
# 7. too late
# --------------------------------------------------------------------------- #

def test_past_14_30_new_york_is_too_late_in_summer():
    """EDT: 14:30 New York is 18:30 UTC."""
    d = decide(at(18, 30), [], [])
    assert d.action == "too_late"
    assert d.ping is True and d.priority == 5
    assert d.title == "No trading run today: too late to start safely"
    assert "18:30 UTC (21:30 Israel time), 14:30 in New York" in d.message
    assert "start by 14:30 New York time" in d.message and "closes at 16:00" in d.message


def test_the_backup_stops_a_quarter_of_an_hour_before_the_latest_start():
    """The guard asks "too late?" when the dispatched run reaches it, one to
    three minutes (or more) after the watchdog decided. A backup started at
    14:29 New York would be refused there after the phone had been told "you
    do not need to do anything"."""
    assert watchdog.DISPATCH_LEAD == timedelta(minutes=15)
    assert decide(at(18, 14), [], []).action == "dispatch"
    for minute in (15, 20, 29):
        d = decide(at(18, minute), [], [])
        assert d.action == "too_late", minute
        assert "GitHub takes several minutes to start one" in d.message
        assert "You do not need to do anything" not in d.message


def test_the_same_utc_hour_is_not_too_late_in_winter():
    """EST: New York is UTC-5, so 18:45 UTC is 13:45 there -- still safe --
    and the cut-off is 19:30 UTC, the last backup 19:14. Israel is UTC+2 by then."""
    wednesday = datetime(2026, 12, 2, tzinfo=UTC)
    d = decide(at(18, 45, wednesday), [], [])
    assert d.action == "dispatch"
    assert "18:45 UTC (20:45 Israel time)" in d.message
    assert decide(at(19, 14, wednesday), [], []).action == "dispatch"
    assert decide(at(19, 15, wednesday), [], []).action == "too_late"
    assert decide(at(19, 30, wednesday), [], []).action == "too_late"
    assert decide(at(18, 45), [], []).action == "too_late"   # the same hour in September


def test_a_half_day_closes_at_13_00_and_the_latest_start_is_11_30():
    """27 Nov 2026, the day after Thanksgiving: EST, so 11:30 New York is
    16:30 UTC and the last backup 16:15. After the 13:00 close a backup would
    only stop at the market-closed gate, write nothing, and after two tries
    report "the backup did not work" about a day that was simply over."""
    half = datetime(2026, 11, 27, tzinfo=UTC)
    assert decide(at(15, 10, half), [], []).action == "dispatch"
    assert decide(at(16, 14, half), [], []).action == "dispatch"
    d = decide(at(16, 15, half), [], [])
    assert d.action == "too_late"
    assert "start by 11:30 New York time" in d.message and "closes at 13:00" in d.message
    for hour, minute in ((16, 40), (17, 40), (18, 30), (19, 0)):
        assert decide(at(hour, minute, half), [], []).action == "too_late", (hour, minute)


def test_the_17_40_cron_three_hours_late_is_too_late():
    """What GitHub actually did to the 17:35 cron on 21-24 Sep."""
    assert decide(at(20, 40), [], []).action == "too_late"


def test_a_run_still_waiting_after_the_latest_start_is_a_lost_day_not_quiet():
    """It will stop at its guard when it gets a machine. Staying quiet about it
    would leave "the backup has started it" as the last word."""
    queued = run("heartbeat cycle (backup)", status="queued", created=at(18, 10))
    assert decide(at(18, 25), [queued], []).action == "none"       # before 14:30: it may still make it
    d = decide(at(18, 45), [queued], [])
    assert d.action == "too_late" and d.priority == 5
    # A cycle already running is past its guard: still nothing to say.
    running = run(status="in_progress", created=at(18, 10))
    assert decide(at(18, 45), [running], []).action == "none"


# --------------------------------------------------------------------------- #
# 8. dispatch
# --------------------------------------------------------------------------- #

def test_no_cycle_and_nothing_on_its_way_starts_the_backup():
    d = decide(at(15, 10), [], [])
    assert d.action == "dispatch"
    assert d.ping is True and d.priority == 4
    assert d.title == "Daily run was late: the backup started it"
    assert "had not started by 15:10 UTC (18:10 Israel time)" in d.message
    assert "planned for 14:40 UTC (17:40 Israel time)" in d.message


def test_a_run_that_ended_without_a_journal_line_is_started_again():
    """Cancelled while it waited for a machine: GitHub lists no job for it."""
    ended = run(conclusion="cancelled", updated=at(15, 2))
    d = decide(at(15, 40), [ended], [], jobs={"1": {"total_count": 0, "jobs": []}})
    assert d.action == "dispatch"
    assert "ended at 15:02 UTC (18:02 Israel time) with result 'cancelled'" in d.message


def test_yesterdays_catch_up_delivered_after_midnight_utc_is_not_todays_run():
    """The 17:35 cron, delivered at 00:10 UTC, is 20:10 the evening before in
    New York: yesterday's run, stopped by its guard. It must not be reported
    as "a run today ended and wrote nothing"."""
    late_cron = run(created=at(0, 10), updated=at(0, 12), conclusion="success")
    d = decide(at(15, 10), [late_cron], [])
    assert d.action == "dispatch"
    assert "had not started by 15:10 UTC" in d.message
    assert "00:12" not in d.message and "ended at" not in d.message
    assert watchdog.todays_cycle_runs([late_cron], at(15, 10)) == []
    # Created at 04:10 UTC it is 00:10 in New York: today's.
    assert len(watchdog.todays_cycle_runs([run(created=at(4, 10))], at(15, 10))) == 1


def test_an_unreadable_run_list_still_starts_the_backup_and_says_why():
    """The guard in heartbeat.yml makes an unneeded backup harmless; a lost
    day is not."""
    d = decide(at(15, 40), None, [])
    assert d.action == "dispatch"
    assert "could not read GitHub's list of runs" in d.message
    assert "unreadable" in d.reason


def test_an_unreadable_run_list_is_still_too_late_when_it_is():
    assert decide(at(19, 0), None, []).action == "too_late"


def test_junk_in_the_run_list_is_ignored():
    junk = ["not a run", 5, None, {"status": "in_progress"}, {"created_at": "yesterday"}]
    assert decide(at(15, 40), junk, []).action == "dispatch"


def test_every_message_is_one_line():
    for decision in (decide(at(15, 10), [], []), decide(at(18, 30), [], []),
                     decide(at(15, 40), [run(status="queued", created=at(15, 0))], [])):
        for text in (decision.title, decision.message):
            assert "\n" not in text


# --------------------------------------------------------------------------- #
# the command line the workflow calls
# --------------------------------------------------------------------------- #

def _outputs(text: str) -> dict:
    return dict(line.split("=", 1) for line in text.strip().splitlines())


def test_cli_prints_github_output_lines_and_exits_zero(tmp_path, capsys):
    runs = tmp_path / "runs.json"
    runs.write_text(json.dumps({"total_count": 0, "workflow_runs": []}))
    code = main(["--runs", str(runs), "--journal", str(tmp_path / "absent.log"),
                 "--now", "2026-09-25T15:10:00Z"])
    assert code == 0
    captured = capsys.readouterr()
    out = _outputs(captured.out)
    assert list(out) == ["action", "ping", "priority", "title", "message", "reason"]
    assert out["action"] == "dispatch" and out["ping"] == "yes" and out["priority"] == "4"
    assert "## Watchdog" in captured.err and "dispatch" in captured.err


def test_cli_reads_the_journal_and_stays_quiet_on_a_covered_day(tmp_path, capsys):
    runs = tmp_path / "runs.json"
    runs.write_text(json.dumps({"workflow_runs": [run(status="completed")]}))
    journal = tmp_path / "journal.log"
    journal.write_text(json.dumps({"ticker": "MSFT", "ts_utc": "2026-09-25T15:08:00+00:00"}) + "\n")
    assert main(["--runs", str(runs), "--journal", str(journal), "--now", "2026-09-25T15:40:00Z"]) == 0
    out = _outputs(capsys.readouterr().out)
    assert out["action"] == "none" and out["ping"] == "no" and out["priority"] == "0"


def test_cli_with_no_run_list_file_decides_without_one(tmp_path, capsys):
    assert main(["--runs", str(tmp_path / "missing.json"), "--journal", str(tmp_path / "j.log"),
                 "--now", "2026-09-25T15:40:00Z"]) == 0
    out = _outputs(capsys.readouterr().out)
    assert out["action"] == "dispatch" and "unreadable" in out["reason"]


def test_cli_that_breaks_still_reaches_the_phone(tmp_path, capsys, monkeypatch):
    def broken(*_args, **_kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr(watchdog, "decide", broken)
    runs = tmp_path / "runs.json"
    runs.write_text("{}")
    assert main(["--runs", str(runs), "--journal", str(tmp_path / "j.log"),
                 "--now", "2026-09-25T15:40:00Z"]) == 0
    out = _outputs(capsys.readouterr().out)
    assert out["action"] == "none" and out["ping"] == "yes"
    assert out["title"] == "The watchdog could not check today's run"


def test_cli_reads_each_failed_runs_steps_from_the_jobs_directory(tmp_path, capsys):
    runs = tmp_path / "runs.json"
    runs.write_text(json.dumps({"workflow_runs": [run(conclusion="failure", id=41)]}))
    jobs = tmp_path / "jobs"
    jobs.mkdir()
    (jobs / "41.json").write_text(json.dumps(TRADED))
    args = ["--runs", str(runs), "--journal", str(tmp_path / "j.log"), "--now", "2026-09-25T15:40:00Z"]
    assert main(args + ["--jobs", str(jobs)]) == 0
    out = _outputs(capsys.readouterr().out)
    assert out["action"] == "none" and out["priority"] == "5"
    (jobs / "41.json").write_text(json.dumps(NEVER_TRADED))
    assert main(args + ["--jobs", str(jobs)]) == 0
    assert _outputs(capsys.readouterr().out)["action"] == "dispatch"
    # No directory, or an unreadable file: cannot tell, so nothing is started.
    (jobs / "41.json").write_text("not json")
    for extra in (["--jobs", str(jobs)], ["--jobs", str(tmp_path / "absent")], []):
        assert main(args + extra) == 0
        assert _outputs(capsys.readouterr().out)["action"] == "none", extra


def test_the_runs_file_may_be_the_api_answer_or_a_bare_list(tmp_path):
    answer = tmp_path / "answer.json"
    answer.write_text(json.dumps({"total_count": 1, "workflow_runs": [run()]}))
    bare = tmp_path / "bare.json"
    bare.write_text(json.dumps([run()]))
    junk = tmp_path / "junk.json"
    junk.write_text("not json")
    assert len(watchdog.read_runs(answer)) == 1
    assert len(watchdog.read_runs(bare)) == 1
    assert watchdog.read_runs(junk) is None
    assert watchdog.read_runs(tmp_path / "absent.json") is None


def test_outputs_flatten_any_newline():
    d = Decision("dispatch", True, 4, "a\nb", "c\r\nd", "e\nf")
    lines = watchdog.as_outputs(d)
    assert len(lines) == 6
    assert "title=a b" in lines and "message=c d" in lines


# --------------------------------------------------------------------------- #
# it only prints
# --------------------------------------------------------------------------- #

def test_the_watchdog_cannot_start_a_run_trade_or_write():
    """The CI guardrail's grep over analysis/, run on this file from the
    inside, plus the things that would let it act on its own: an HTTP
    client, a subprocess, the gh CLI, or the phone topic."""
    source = Path(watchdog.__file__).read_text()
    assert not re.search(r"(submit_order|submit_bracket_order|ExecutionEngine|post_signal"
                         r"|\.write_text\(|open\([^)]*[\"'][wa])", source)
    for banned in ("subprocess", "requests", "httpx", "urllib", "os.system", "NTFY",
                   "broker_client", "alpaca"):
        assert banned not in source, banned
