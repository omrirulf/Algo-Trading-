"""Did a cycle actually run today -- and may one still start?

The 16 Sep schedule never fired. Not late, not failed -- GitHub simply never
created the run, and nothing noticed. A trading day would have been lost in
silence if an unrelated reminder had not happened to look.

A second scheduled run later in the day fixes that, but only if it can tell
whether the first one happened. This answers that question from the one
artifact that proves it: the journal, which the cycle commits to the
repository at the end of every run. One entry dated today means a cycle ran
today.

Two things make this the right evidence rather than merely the easiest:

* It is committed, so a fresh checkout can read it. A workflow run's status
  would need an API call, a token and a permission; the journal needs none.
* It is what the rest of the system is scored from. A cycle whose journal
  never landed is, to every later measurement, a cycle that did not happen --
  so re-running is the repair, not a duplicate.

That last point is only safe because the broker refuses a second order for
the same ticker and side inside the same UTC day (see
``broker_client.build_client_order_id``). A catch-up run therefore cannot
double a position the lost run already opened; at worst it pays for one more
cycle's model calls and writes the record that went missing.

The broker covers entries, not the profit ladder. The position manager
counts the rungs a position has already sold from the audit log, which is
committed with the journal, so a run whose trading step ran and whose commit
never reached the branch leaves no record of the rungs it sold, and a second
run would sell them again.

Since 25 Sep the same question is asked by every cycle run, not only the
scheduled ones: a late GitHub cron, the watchdog's backup
(``analysis/watchdog.py``) and the Claude Routines can all start a run on the
same day, and exactly one of them may trade. So the guard now also says when
it is too late in the day to start at all (``LATEST_START_NY``), and this
module builds the small "run block" every journal line of the cycle carries:
what started the run, which starter asked for it (the Supabase starter, a
backup, a person), when it was meant to start, and how late it was.

The journal cannot show the one run that matters most: the one that traded
and lost its record. So the guard also reads GitHub's own record of today's
heartbeat runs, fetched by the workflow, and stops when another run today
reached its trading step, whatever its result (``run_that_reached_trading``),
unless that step began and ended before the open, when the market was shut
and nothing could trade.
That is the only question here that needs an API call, a token and a
permission, and it is asked in addition to the journal, never instead of it:
when GitHub cannot be read, the guard decides from the journal alone and says
so. The watchdog reads the same record with the same helpers and refuses a
backup on the same days, so the two never disagree about whether a day has
had its cycle.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass, replace
from datetime import date, datetime, time, timezone
from pathlib import Path
from typing import Any, Iterable, Optional
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis.reader import JournalEntry, read_journal  # noqa: E402

#: US market hours are set in New York and move against UTC twice a year, on a
#: DST calendar that is not Europe's or Israel's. Every "is it too late" check
#: is therefore asked in New York time, never as a fixed UTC hour.
NEW_YORK = ZoneInfo("America/New_York")

#: The day's scheduled start, in UTC: the first cron in heartbeat.yml
#: ("40 14 * * 1-5"). 10:40 New York in summer and 09:40 in winter, so after
#: the 09:30 open in both seasons. Fixed in UTC because a GitHub cron is. The
#: workflow test pins this constant to the cron, so the two cannot drift.
SCHEDULED_START_UTC = time(14, 40)

#: The latest a cycle may start, in New York time.
#:
#: The runs of 21-24 Sep took 26-74 minutes from their first journal line to
#: their last, and the orders go out along the way. A start after 14:30 New
#: York risks orders reaching the broker after the 16:00 close, where the
#: engine refuses them ("market is closed"), the position manager skips the
#: profit ladder, and the shadow funds' calibration would see simulated trades
#: the real account never made. 90 minutes before the close covers the
#: slowest run measured with a quarter of an hour to spare; a day that cannot
#: start by then is better lost loudly than traded half-way.
#:
#: Not a trading rule: it only decides whether a run starts, never what it
#: trades.
LATEST_START_NY = time(14, 30)

#: The same 90 minutes before the bell on a half day, when the market closes
#: at 13:00 New York.
EARLY_CLOSE_LATEST_START_NY = time(11, 30)

#: Days the NYSE closes early, at 13:00 New York: the day after Thanksgiving,
#: and Christmas Eve when it is a weekday and not itself the observed holiday.
#: ``config/market_calendar.py`` deliberately lists only full closures (a
#: half day is a real session and must not be skipped), so the hours live
#: here, beside the one question that needs them: may a run still start?
#:
#: Without this, a backup at 12:40 New York on 27 Nov would pass the guard
#: and send its orders into the 13:00 close, and every backup after 13:00
#: would stop at the broker's market-closed gate, write nothing, and after
#: two of them tell the owner "the backup did not work" -- about a day that
#: was simply over. Same span as the holiday list; extend both together.
EARLY_CLOSES: frozenset[date] = frozenset({
    date(2025, 7, 3), date(2025, 11, 28), date(2025, 12, 24),
    date(2026, 11, 27), date(2026, 12, 24),
    date(2027, 11, 26),
})

#: A run that starts more than this many minutes after its scheduled time is
#: marked late in the run block -- the same 30 minutes after which the
#: watchdog stops waiting for GitHub and starts the run itself.
LATE_AFTER_MINUTES = 30

#: The New York open, the same on a half day as on any other. Before it the
#: broker's clock says the market is shut, and both the engine and the
#: position manager's profit ladder ask that clock before they act, so a
#: trading step that began and ended before 09:30 New York placed nothing and
#: sold nothing (``analysis/watchdog.py``: ``trading_step_ran``).
MARKET_OPEN_NY = time(9, 30)

#: What ``start_decision`` can answer.
RUN, ALREADY, TOO_LATE = "run", "already", "too_late"

#: Which starter asked for the run, as the run block records it under
#: ``source``. Since 26 Sep 2026 the owner's main starter is a pg_cron job in
#: the Supabase project that dispatches heartbeat.yml at 14:40 UTC
#: (``supabase/heartbeat_starter.sql``); GitHub's own cron, the Claude
#: Routines, a temporary Claude "bridge" Routine at 14:42 and the watchdog
#: stay as backups. Every one of them is only a request to run -- the guard
#: above decides, the same way for all of them -- so the source is a label,
#: never an input to any decision. It is recorded because "did the main
#: starter start today's run, or did a backup have to?" is the question the
#: daily brief now answers, and GitHub's run list forgets it after a few
#: months.
PRIMARY_SOURCE = "supabase-cron"
#: A scheduled run has no inputs at all, so its source is named here.
SCHEDULE_SOURCE = "github-schedule"
#: The ``source`` input's own default, for a dispatch that does not name one.
DEFAULT_SOURCE = "manual"
#: What a source that is not a short safe token becomes.
UNKNOWN_SOURCE = "unknown"
#: The sources the owner's starters send. Documentation for a reader: any
#: short safe token is accepted (``source_for``), so adding a starter never
#: needs a change here first.
KNOWN_SOURCES = (PRIMARY_SOURCE, "claude-bridge", "claude-routine", "watchdog",
                 DEFAULT_SOURCE, SCHEDULE_SOURCE)
#: A short safe token: lower-case letters, digits and hyphens, at most 40.
#: The input is free text typed by whatever dispatched the run -- a person,
#: a Routine, a database job -- and it rides on every journal line, which is
#: committed to a public repository and read back by the brief and the race.
#: Anything else (spaces, markup, a pasted secret, a 2 000-character string)
#: is replaced, never echoed.
SOURCE_PATTERN = re.compile(r"[a-z0-9-]{1,40}")


def cycle_ran_on(entries: Iterable[JournalEntry], day: date) -> bool:
    """Whether any journal entry was written on ``day``, in UTC.

    Entries with no readable timestamp do not count. A line that cannot say
    when it happened cannot prove that today is covered, and treating it as
    proof would skip the catch-up on exactly the days the journal is damaged.
    """
    for entry in entries:
        stamp = entry.timestamp
        if stamp is None:
            continue
        if stamp.astimezone(timezone.utc).date() == day:
            return True
    return False


def _utc(moment: datetime) -> datetime:
    """``moment`` in UTC. A naive datetime is read as UTC, like the journal's."""
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=timezone.utc)
    return moment.astimezone(timezone.utc)


def closes_at(day: date) -> time:
    """The New York close on ``day``: 13:00 on a half day, 16:00 otherwise."""
    return time(13, 0) if day in EARLY_CLOSES else time(16, 0)


def latest_start(day: date) -> time:
    """The latest safe start on ``day``, New York time: 90 minutes before the close."""
    return EARLY_CLOSE_LATEST_START_NY if day in EARLY_CLOSES else LATEST_START_NY


def too_late_to_start(now: datetime) -> bool:
    """Whether ``now`` is at or after that day's latest safe start, in New York."""
    local = _utc(now).astimezone(NEW_YORK)
    return local.time() >= latest_start(local.date())


def run_that_reached_trading(
    other_runs: Optional[Iterable[tuple[Any, Any]]], now: datetime,
) -> tuple[Optional[dict], tuple[str, ...]]:
    """Another heartbeat run today whose trading step started, if there is one.

    ``other_runs`` is ``(run, jobs)`` pairs: a run from GitHub's list of
    heartbeat runs, and GitHub's jobs answer for it (None when it could not
    be read). It never holds the run that is asking (``other_runs_from``
    builds it).

    A run counts when it was created on today's New York date, is a cycle
    run (a protection pass never runs "Run one cycle"), and its jobs show
    the trading step listed and not skipped, whatever its result, unless
    that step began and ended before the open. That is the watchdog's own
    reading (``analysis/watchdog.py``: ``todays_cycle_runs`` and
    ``trading_step_ran``), imported rather than copied so the two cannot
    come to disagree about what "reached its trading step" means.

    Whatever the run's status. A run waiting for a machine usually lists
    no jobs yet, which reads as "reached nothing". But a run that traded
    and was then re-run from GitHub's page is "pending" or "queued" again
    while its new attempt waits, and its jobs answer (``filter=all``)
    still holds the attempt that traded; skipping it by its status would
    let this run trade the day a second time.

    Returns that run, or None; and the ids of today's runs whose steps
    could not be read, which the guard reports and otherwise leaves to the
    journal.
    """
    # Imported here, not at the top: analysis.watchdog imports this module.
    from analysis.watchdog import todays_cycle_runs, trading_step_ran

    unread: list[str] = []
    for run, jobs in other_runs or ():
        if not isinstance(run, dict) or not todays_cycle_runs([run], now):
            continue
        ran = trading_step_ran(jobs)
        if ran:
            return run, tuple(unread)
        if ran is None:
            unread.append(str(run.get("id")))
    return None, tuple(unread)


def _earlier_attempts(jobs: Any, attempt: Optional[int]) -> Any:
    """This run's own jobs from attempts before ``attempt``, as a jobs answer.

    A run re-run from GitHub's page keeps its id and gets a new attempt, and
    the jobs answer the workflow fetches (``filter=all``) holds every
    attempt's jobs, this one's included. Only the earlier ones can have
    traded before this one; this attempt's own trading step is listed and
    not yet skipped, and counting it would stop every run. So a job whose
    attempt cannot be read is left out. None when the answer itself cannot
    be read.
    """
    if not isinstance(jobs, dict) or not isinstance(jobs.get("jobs"), list):
        return None
    earlier = [job for job in jobs["jobs"] if isinstance(job, dict)
               and type(job.get("run_attempt")) is int and job["run_attempt"] < (attempt or 0)]
    return {"jobs": earlier}


def _attempt(value: Any) -> Optional[int]:
    """``github.run_attempt`` as a number, or None."""
    text = str(value if value is not None else "").strip()
    return int(text) if text.isdigit() else None


#: Marks the pair ``other_runs_from`` builds for this run's own earlier
#: attempts, so ``check_start`` can tell it from every other run.
_EARLIER_ATTEMPTS = "_earlier_attempts_of_this_run"


def other_runs_from(
    runs: Optional[Iterable[Any]], jobs: Optional[dict], *,
    this_run: Any = None, this_attempt: Any = None,
) -> Optional[list[tuple[dict, Any]]]:
    """The ``(run, jobs)`` pairs the guard checks, from what the workflow saved.

    ``runs`` is GitHub's list of heartbeat runs (``watchdog.read_runs``), or
    None when it could not be read -- and then so is this, which the guard
    reads as "decide from the journal alone". ``jobs`` maps a run id to
    GitHub's jobs answer for it (``watchdog.read_jobs``).

    The asking run itself is left out, except on a re-run from GitHub's
    page (``this_attempt`` above 1): its earlier attempts are checked like
    any other run, so pressing "Re-run" on a run that traded and lost its
    record is not a way past the guard. They are named as such in the step
    summary.
    """
    if runs is None:
        return None
    answers = jobs if isinstance(jobs, dict) else {}
    me = str(this_run if this_run is not None else "").strip()
    attempt = _attempt(this_attempt)
    pairs: list[tuple[dict, Any]] = []
    for run in runs:
        if not isinstance(run, dict):
            continue
        run_id = str(run.get("id"))
        if run_id != me:
            pairs.append((run, answers.get(run_id)))
        elif attempt is not None and attempt > 1:
            earlier = {**run, "conclusion": "an earlier attempt of this run", _EARLIER_ATTEMPTS: True}
            pairs.append((earlier, _earlier_attempts(answers.get(run_id), attempt)))
    return pairs


@dataclass(frozen=True)
class Start:
    """The guard's answer, and what it rests on."""

    #: ``run``, ``already`` or ``too_late``.
    decision: str
    #: A cycle is in the journal for today.
    journalled: bool = False
    #: Another run today that reached its trading step, if that is why.
    reached: Optional[dict] = None
    #: Today's runs whose steps could not be read.
    unread: tuple[str, ...] = ()
    #: For a re-run from GitHub's page of a run dispatched with ``rerun``:
    #: True when that ``rerun`` covered today and only this run's earlier
    #: attempts were asked; False when the run was dispatched on an earlier
    #: day and was guarded like any other. None for every other run.
    rerun: Optional[bool] = None


def check_start(
    entries: Iterable[JournalEntry], now: datetime,
    other_runs: Optional[Iterable[tuple[Any, Any]]] = None, *, rerun: bool = False,
) -> Start:
    """May a cycle start at ``now``? The answer and its reason.

    In order, the first that holds decides:

    1. A cycle is journalled for today: ``already``.
    2. Another heartbeat run today reached its trading step, whatever its
       result (``run_that_reached_trading``): ``already``. The one case the
       journal cannot show is a run that traded and whose commit never
       reached the branch (a refused push, a lost machine); a second cycle
       would then sell the profit-ladder rungs that run already sold. A run
       that ran on another branch looks the same from here, and counts the
       same: only a person can tell them apart, and ``rerun`` is how a
       person says "run anyway".
    3. It is at or past the day's latest safe start: ``too_late``.
    4. Otherwise ``run``.

    ``already`` wins over ``too_late`` when both hold, because it is the more
    useful thing to tell a person reading the run: the day is covered.

    ``other_runs`` None means GitHub's record was not read, and the answer
    rests on the journal alone.

    ``rerun`` is for a run dispatched with ``rerun`` and then re-run from
    GitHub's page. A re-run replays the dispatch, inputs included, so the
    person's "run anyway" still holds against the journal, the other runs
    and the clock -- but it was given before this run's first attempt
    traded, and says nothing about trading the day again. So only this
    run's own earlier attempts are asked (the pair ``other_runs_from``
    builds for them): if one reached its trading step, or they cannot be
    read, ``already``; otherwise ``run``. Stopping when GitHub cannot be
    read is the opposite of rule 2's fallback, and deliberately so: a
    re-run is always a person at the page, who can start a fresh run with
    ``rerun``, while the fallback exists for the unattended starts. A run
    dispatched with ``rerun`` on an earlier New York day and re-run today
    was never given "run anyway" for today, so it is guarded like any other
    run, by the rules above.

    Weekends and holidays are not this function's business. The cycle itself
    skips them before it fetches anything (``orchestrator/heartbeat.py``), and
    a guard that also knew the calendar would be a second list to keep in
    step with the first.

    Nor is a start that is too *early*. Without ``--premarket`` the cycle asks
    the broker's clock before anything else and stops when the market is
    shut, so an early run costs one API call and writes nothing. Nor does it
    use up the day: a trading step that began and ended before the open is
    not counted by rule 2 (``MARKET_OPEN_NY``), so the day's cycle still
    runs after the open.
    """
    now_utc = _utc(now)
    if rerun:
        if other_runs is None:
            return Start(ALREADY, rerun=True)
        # Imported here, not at the top: analysis.watchdog imports this module.
        from analysis.watchdog import todays_cycle_runs

        mine = [(run, jobs) for run, jobs in other_runs
                if isinstance(run, dict) and run.get(_EARLIER_ATTEMPTS)]
        if todays_cycle_runs([run for run, _ in mine], now_utc):
            reached, unread = run_that_reached_trading(mine, now_utc)
            if reached is None and not unread:
                return Start(RUN, rerun=True)
            return Start(ALREADY, reached=reached, unread=unread, rerun=True)
    return replace(_guarded(entries, now_utc, other_runs), rerun=False if rerun else None)


def _guarded(
    entries: Iterable[JournalEntry], now_utc: datetime,
    other_runs: Optional[Iterable[tuple[Any, Any]]],
) -> Start:
    """Rules 1 to 4 of ``check_start``: every run but a ``rerun`` re-run of today's."""
    if cycle_ran_on(entries, now_utc.date()):
        return Start(ALREADY, journalled=True)
    reached, unread = run_that_reached_trading(other_runs, now_utc) if other_runs else (None, ())
    if reached is not None:
        return Start(ALREADY, reached=reached)
    if too_late_to_start(now_utc):
        return Start(TOO_LATE, unread=unread)
    return Start(RUN, unread=unread)


def start_decision(
    entries: Iterable[JournalEntry], now: datetime,
    other_runs: Optional[Iterable[tuple[Any, Any]]] = None, *, rerun: bool = False,
) -> str:
    """``run``, ``already`` or ``too_late``: ``check_start`` without the reason."""
    return check_start(entries, now, other_runs, rerun=rerun).decision


def _describe(run: dict) -> str:
    """``run 123, failure``: which run, and how it ended (or that it is running)."""
    how = run.get("conclusion") or run.get("status") or "unknown"
    return f"run {run.get('id')}, {str(how).replace('_', ' ')}"


def start_summary(start: Start, *, runs_read: Optional[bool] = None) -> list[str]:
    """The guard's paragraphs for the job summary, one per line.

    ``runs_read`` is None when GitHub's record was not asked for at all, and
    False when it was asked for and could not be read: then the answer rests
    on the journal alone, and the summary says so rather than let a quiet
    fallback read as a full check.
    """
    if start.rerun:
        if start.decision == RUN:
            return ["This run was dispatched with rerun and is a re-run from GitHub's page. No "
                    "earlier attempt of it reached its trading step, so it runs, as rerun asked."]
        why = ("An earlier attempt of this run already reached its trading step." if start.reached
               else "The steps of this run's earlier attempts could not be read.")
        return [f"{why} It was dispatched with rerun, but pressing Re-run on it does not run the "
                f"day's cycle a second time: this run stops here. To run another cycle today, start "
                f"heartbeat by hand (Run workflow) with rerun ticked, after checking the account."]
    lines: list[str] = []
    if start.rerun is False:
        lines.append("This run was dispatched with rerun on an earlier New York day and re-run from "
                     "GitHub's page today. That rerun does not carry over to today, so it was checked "
                     "like any other run.")
    lines += _guard_summary(start, runs_read)
    return lines


def _guard_summary(start: Start, runs_read: Optional[bool]) -> list[str]:
    """``start_summary`` for every run but a ``rerun`` re-run of today's."""
    if start.decision == ALREADY and start.reached is not None:
        lines = [f"Another run today already reached its trading step ({_describe(start.reached)}); "
                 f"a second cycle could repeat profit-ladder sales. This run stops here. Re-run by "
                 f"hand with rerun only after checking the account."]
    elif start.decision == ALREADY:
        lines = ["A cycle is already journalled for today; this run stops here."]
    elif start.decision == TOO_LATE:
        lines = ["No cycle is journalled for today, but it is past the latest safe start (14:30 New "
                 "York, 11:30 on a half day): a cycle started now could still be sending orders at "
                 "the close. This run stops here."]
    elif runs_read:
        lines = ["No cycle is journalled for today, and no other run today reached its trading step. "
                 "Running one now."]
    else:
        lines = ["No cycle journalled for today. Running one now."]
    if runs_read is False:
        lines.append("GitHub's list of today's heartbeat runs could not be read, so this was decided "
                     "from the journal alone: a run today that traded and lost its record would not "
                     "have been seen.")
    elif start.unread and start.reached is None:
        one = len(start.unread) == 1
        lines.append(f"The steps of {'run' if one else 'runs'} {', '.join(start.unread)} could not "
                     f"be read, so for {'that run' if one else 'those runs'} this was decided from "
                     f"the journal alone.")
    return lines


def trigger_for(event: Optional[str], started_by: Optional[str]) -> str:
    """``schedule``, ``scheduler``, ``backup`` or ``manual``, from what GitHub says started the run.

    A scheduled run has no inputs at all, so the event name is the only thing
    that can say it was the cron. Anything dispatched is manual unless it
    says otherwise: the watchdog always says ``backup``, and the Supabase
    starter says ``scheduler`` (an outside scheduler that is the day's main
    start, not a rescue -- so it must never be counted against the
    watchdog's cap on its own backups, which counts "(backup)" titles). A
    person clicking "Run workflow" and a Claude Routine dispatching with only
    ``mode`` both get the default. So ``manual`` means "dispatched", not "by
    a person"; ``source`` in the run block says which dispatcher it was.
    """
    if (event or "").strip() == "schedule":
        return "schedule"
    said = (started_by or "").strip().lower()
    if said == "backup":
        return "backup"
    if said == "scheduler":
        return "scheduler"
    return "manual"


def source_for(event: Optional[str], source: Optional[str]) -> str:
    """The run block's ``source``: which starter asked for this run.

    ``github-schedule`` for a scheduled run, whatever else is said: a cron
    has no inputs. For a dispatch, the ``source`` input when it is a short
    safe token (``SOURCE_PATTERN``); ``manual`` when it is empty, which is
    the input's own default and what GitHub fills in for any dispatch that
    leaves it out; ``unknown`` for anything else, so no arbitrary text a
    dispatcher sent reaches the journal. Surrounding blanks are ignored;
    nothing else is repaired -- ``Supabase-Cron`` is not a token and reads
    ``unknown``, which is the honest answer to a starter that spells its own
    name wrong.
    """
    if (event or "").strip() == "schedule":
        return SCHEDULE_SOURCE
    text = (source or "").strip()
    if not text:
        return DEFAULT_SOURCE
    return text if SOURCE_PATTERN.fullmatch(text) else UNKNOWN_SOURCE


def run_block(
    *,
    event: Optional[str],
    started_by: Optional[str],
    run_id: object,
    started_at: datetime,
    scheduled: time = SCHEDULED_START_UTC,
    source: Optional[str] = None,
) -> dict:
    """The block every journal line of this run carries under ``"run"``.

    ``scheduled_for`` is the day's scheduled start whatever started this run:
    the question the block answers is "how late was today's cycle", and a
    backup or a person starting it at 16:10 is 90 minutes late against the
    same 14:40 the cron was meant to keep. ``minutes_late`` is floored, so a
    run 30 minutes and 59 seconds after its time is 30 minutes late and not
    yet ``late``; it is negative for a run started early.

    ``source`` is which starter asked for the run (``source_for``): the
    Supabase starter, the Claude bridge, a Routine, the watchdog, a person,
    or GitHub's schedule. Validated here, where the block is built, so the
    journal only ever carries a short safe token.
    """
    started = _utc(started_at).replace(microsecond=0)
    scheduled_for = datetime.combine(started.date(), scheduled, tzinfo=timezone.utc)
    minutes_late = math.floor((started - scheduled_for).total_seconds() / 60)
    return {
        "trigger": trigger_for(event, started_by),
        "source": source_for(event, source),
        "scheduled_for": scheduled_for.isoformat(),
        "started_at": started.isoformat(),
        "minutes_late": minutes_late,
        "late": minutes_late > LATE_AFTER_MINUTES,
        "run_id": str(run_id or ""),
    }


def _today(value: Optional[str]) -> date:
    return date.fromisoformat(value) if value else datetime.now(timezone.utc).date()


def _now(value: Optional[str]) -> datetime:
    return _utc(datetime.fromisoformat(value)) if value else datetime.now(timezone.utc)


def main(argv: Optional[list[str]] = None) -> int:
    """Print the answer and exit 0 whatever it is.

    Three questions, one script:

    * default: ``yes`` or ``no`` -- has a cycle run today? (kept for anything
      that still asks the old way)
    * ``--decide``: ``run``, ``already`` or ``too_late`` -- the guard's
      question in heartbeat.yml. With ``--runs`` (and ``--jobs``,
      ``--this-run``, ``--this-attempt``, ``--rerun``) it also reads
      GitHub's record of today's other heartbeat runs, as the workflow saved
      it; the one word is still all that goes to stdout, and the reason,
      written for the job summary, goes to stderr.
    * ``--run-block``: the JSON the cycle step hands the journal (with
      ``--event``, ``--started-by``, ``--source`` and ``--run-id``)

    A non-zero exit would be indistinguishable from the script itself
    breaking, and the caller must be able to tell "no cycle today" from "the
    check failed" -- those call for opposite actions. So every answer exits
    0, and only a real crash does not: the workflow step then goes red and
    the owner's phone hears about it, rather than a broken check being read
    as either answer. A run list or a jobs answer that cannot be read is not
    a crash: the answer then rests on the journal alone, and says so.
    """
    parser = argparse.ArgumentParser(description="Has a cycle run today, and may one start?")
    parser.add_argument("--journal", type=Path, default=None)
    parser.add_argument("--day", default=None, help="ISO date, default today in UTC")
    parser.add_argument("--decide", action="store_true",
                        help="print run, already or too_late instead of yes or no")
    parser.add_argument("--run-block", action="store_true",
                        help="print this run's journal run block as one line of JSON")
    parser.add_argument("--now", default=None, help="ISO datetime, default now (UTC if naive)")
    parser.add_argument("--event", default="", help="github.event_name")
    parser.add_argument("--started-by", default="", help="the started_by input, if any")
    parser.add_argument("--source", default="", help="the source input, if any")
    parser.add_argument("--run-id", default="", help="github.run_id")
    parser.add_argument("--runs", type=Path, default=None,
                        help="with --decide: GitHub's list of today's heartbeat runs, as JSON")
    parser.add_argument("--jobs", type=Path, default=None,
                        help="with --runs: a directory of GitHub's jobs answers, one <run id>.json per run")
    parser.add_argument("--this-run", default="", help="with --runs: github.run_id, left out of the check")
    parser.add_argument("--this-attempt", default="",
                        help="with --runs: github.run_attempt; a re-run checks its own earlier attempts")
    parser.add_argument("--rerun", default="",
                        help="with --runs: the rerun input; 'true' on a re-run (--this-attempt above 1) "
                             "asks only this run's earlier attempts")
    args = parser.parse_args(argv)

    if args.run_block:
        block = run_block(event=args.event, started_by=args.started_by,
                          run_id=args.run_id, started_at=_now(args.now), source=args.source)
        print(json.dumps(block, separators=(",", ":")))
        print(f"{block['trigger']} run from {block['source']}, {block['minutes_late']} min after "
              f"{block['scheduled_for']}", file=sys.stderr)
        return 0

    if args.journal is None:
        parser.error("--journal is required unless --run-block is given")

    try:
        entries = read_journal(args.journal).entries
    except FileNotFoundError:
        # No journal at all is the strongest possible "no cycle today".
        entries = []
        print(f"no journal at {args.journal}\n", file=sys.stderr)

    if args.decide:
        now = _now(args.now)
        other_runs, runs_read, rerun = None, None, False
        if args.runs is not None:
            # Imported here, not at the top: analysis.watchdog imports this module.
            from analysis.watchdog import read_jobs, read_runs

            other_runs = other_runs_from(read_runs(args.runs), read_jobs(args.jobs),
                                         this_run=args.this_run, this_attempt=args.this_attempt)
            runs_read = other_runs is not None
            # A first attempt with rerun never reaches the guard (heartbeat.yml
            # skips it), so only a re-run from GitHub's page is asked this way.
            rerun = (args.rerun.strip().lower() == "true"
                     and (_attempt(args.this_attempt) or 0) > 1)
        start = check_start(entries, now, other_runs, rerun=rerun)
        print(start.decision)
        clock = f"{now.strftime('%H:%M')} UTC ({now.astimezone(NEW_YORK).strftime('%H:%M')} New York)"
        print(f"The guard answered `{start.decision}` at {clock}.\n", file=sys.stderr)
        for line in start_summary(start, runs_read=runs_read):
            print(f"{line}\n", file=sys.stderr)
        return 0

    day = _today(args.day)
    ran = cycle_ran_on(entries, day)
    print("yes" if ran else "no")
    print(f"{'found' if ran else 'no'} journal entries for {day.isoformat()}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
