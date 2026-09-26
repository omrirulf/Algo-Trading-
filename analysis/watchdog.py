"""Has today's trading run started? If not, say so -- and say what to do.

    python -m analysis.watchdog --runs runs.json --journal logs/journal
    python -m analysis.watchdog --runs runs.json --journal logs/journal --now 2026-09-25T15:10:00Z
    python -m analysis.watchdog --runs runs.json --jobs jobs/ --journal logs/journal

GitHub's cron is not a clock. In the week of 21 Sep the heartbeat's 12:35 UTC
cron was delivered 4.5 to 5.7 hours late every single day, and the 17:35 one
about 3 hours late; on 16 Sep a cron was never delivered at all. Every cycle
that week was started by a Claude Routine, not by the schedule. A daily
experiment cannot rest on that, so the owner asked for three things: a
notification when the run has not started within 30 minutes of its time, a
backup that starts it, and a guarantee that a day never runs twice.

This module is the judgement in the middle of that. It reads three things
-- GitHub's list of today's heartbeat runs and, for every run that has
finished, the steps it reached (both fetched by the workflow, saved as
JSON), and the journal -- and prints a decision:

* ``none``      nothing to do: not a trading day, too early to judge, a cycle
                is already in the journal, or a run is on its way. Also, with
                an urgent notification, when a run today reached its trading
                step and left nothing in the journal (see below), or when the
                backup has already tried twice.
* ``dispatch``  no cycle today and nothing on its way: the workflow starts
                heartbeat.yml as the backup, and the owner is told.
* ``stuck``     a run exists but GitHub has not given it a machine for more
                than 30 minutes. Starting another would only queue behind it,
                so the owner is told and nothing is started.
* ``too_late``  no cycle today and too near or past the latest safe start:
                nothing is started, and the owner is told the day is lost.

It is print-only, like everything in ``analysis/``: it never starts a run,
places an order or writes a file. The workflow reads the printed lines and
does the dispatching and the notifying, so the decision is pure, tested
Python and the side effects are a few visible lines of YAML.

A backup dispatched on a day that did not need one is stopped by
heartbeat.yml's own guard (``analysis/cycle_day.py``), which reads the
journal on the branch's latest commit before any cycle starts. The journal
alone cannot show a run that traded and whose journal never reached the
branch (its push was refused, or GitHub lost the machine mid-run): it says
"no cycle", yet orders went out. The broker refuses a second entry for the
same ticker, side and UTC day, but the profit ladder counts the rungs
already sold from the audit log, which was lost with the journal, so a
second run would sell them again. So the guard also reads GitHub's record
and stops every cycle after another run today reached its trading step,
whatever that run's result -- and this module, reading the same record with
the same two helpers (``todays_cycle_runs``, ``trading_step_ran``), starts no
backup on such a day. After any run today has finished, it starts the backup
only when GitHub's record shows that run never reached its trading step;
otherwise, or when it cannot tell, it tells the owner and starts nothing. A
backup started anyway would only stop at the guard, after the phone had been
told "the backup has started it".
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable, Optional
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis.cycle_day import (  # noqa: E402
    MARKET_OPEN_NY, NEW_YORK, SCHEDULED_START_UTC, closes_at, cycle_ran_on, latest_start,
    too_late_to_start,
)
from analysis.reader import JournalEntry, read_journal  # noqa: E402
from config.market_calendar import is_trading_day  # noqa: E402

#: The owner reads the phone in Israel. Every time in a message is given in
#: UTC, which is what GitHub and the journal use, with Israel time beside it
#: -- the same pairing the daily report uses (``analysis/cycle_report.py``).
ISRAEL = ZoneInfo("Asia/Jerusalem")

#: Run statuses that mean "on its way". Everything else (completed) is done.
ACTIVE_STATUSES = frozenset({"queued", "in_progress", "waiting", "requested", "pending"})

#: The subset of those that mean the run has not started on a machine yet.
NOT_STARTED_STATUSES = ACTIVE_STATUSES - {"in_progress"}

#: How long a run may wait for a machine before the owner is told. The same
#: 30 minutes the schedule itself is given.
QUEUE_PATIENCE = timedelta(minutes=30)

#: How long a dispatched run takes to reach heartbeat.yml's guard: GitHub
#: creates it, finds it a machine, checks out, installs Python and the
#: requirements -- one to three minutes on a normal day. The guard asks
#: "too late?" at THAT moment, not at this one. A backup started at 14:29
#: New York would reach it after 14:30 and stop, while the phone had
#: already said "the backup has started it, you do not need to do
#: anything". So the watchdog stops starting backups this long before the
#: latest safe start, and says the day is lost instead. heartbeat.yml also
#: tells the phone if a backup reaches its guard too late anyway.
DISPATCH_LEAD = timedelta(minutes=15)

#: The heartbeat step that trades. A run that never reached this step placed
#: nothing, and the backup may start the day again; one that reached it may
#: have traded, whatever its result. heartbeat.yml's guard reads the same
#: name, through ``analysis/cycle_day.py``. tests/test_heartbeat_workflow.py
#: pins it to heartbeat.yml, so a rename there cannot quietly make every run
#: look as if it never traded -- to the watchdog and the guard both.
TRADING_STEP = "Run one cycle"

#: ntfy priorities, as the heartbeat's own phone step uses them.
URGENT, HIGH = 5, 4


@dataclass(frozen=True)
class Decision:
    """What the workflow should do, and what the phone should say."""

    #: ``none``, ``dispatch``, ``too_late`` or ``stuck``.
    action: str
    #: Whether the owner's phone should hear about it.
    ping: bool
    #: ntfy priority for the notification: 5 urgent, 4 high; 0 when no ping.
    priority: int
    #: One-line notification title, empty when no ping.
    title: str
    #: One-line notification body, empty when no ping.
    message: str
    #: Why, in a few words, for the job summary. Always set.
    reason: str


def _quiet(reason: str) -> Decision:
    return Decision("none", False, 0, "", "", reason)


def _utc(moment: datetime) -> datetime:
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=timezone.utc)
    return moment.astimezone(timezone.utc)


def _parse(text: Any) -> Optional[datetime]:
    """A GitHub timestamp (``2026-09-25T15:04:05Z``), or None."""
    if not isinstance(text, str) or not text.strip():
        return None
    try:
        return _utc(datetime.fromisoformat(text.strip().replace("Z", "+00:00")))
    except ValueError:
        return None


def _clock(moment: datetime) -> str:
    """``15:10 UTC (18:10 Israel time)``."""
    utc = _utc(moment)
    return f"{utc.strftime('%H:%M')} UTC ({utc.astimezone(ISRAEL).strftime('%H:%M')} Israel time)"


def _title(run: dict) -> str:
    return str(run.get("display_title") or run.get("name") or "")


#: How heartbeat.yml's ``run-name`` begins, for a protection pass and for
#: the watchdog's own backup. Matched at the start of the title only.
#:
#: Since 26 Sep 2026 a cycle's title also names the starter that asked for
#: it ("heartbeat cycle (scheduler) via supabase-cron"), and that part is
#: free text from the dispatch's ``source`` input -- GitHub builds the title
#: before any step can validate it. Matching anywhere in the title would let
#: a source such as "protect-test" make a real cycle read as a protection
#: pass, which the guard does not count, so a second cycle could trade the
#: same day; or let "(backup)" in a source eat into the watchdog's cap. The
#: prefixes are written by heartbeat.yml itself, before the source.
PROTECT_TITLE = "heartbeat protect"
BACKUP_TITLE = "heartbeat cycle (backup)"


def is_cycle_run(run: dict) -> bool:
    """A heartbeat run that is (or may be) a trading cycle.

    Every run created after heartbeat.yml gained its ``run-name`` names
    itself ("heartbeat cycle (backup) via watchdog", "heartbeat protect").
    Runs from before that (25 Sep 2026 and earlier) are all titled plain
    "heartbeat", and cannot say which they were; they count as cycles, which
    is the direction that errs towards waiting rather than dispatching.
    """
    return not _title(run).strip().lower().startswith(PROTECT_TITLE)


def is_backup_run(run: dict) -> bool:
    """A run the watchdog started -- its title says so, at its start.

    Only ``started_by: backup`` makes that title. The Supabase starter
    dispatches with ``started_by: scheduler`` ("heartbeat cycle
    (scheduler)"), and a Routine or a person with ``manual``: neither is the
    watchdog's rescue, so neither counts toward ``max_backups``.
    """
    return _title(run).strip().lower().startswith(BACKUP_TITLE)


def _status(run: dict) -> str:
    return str(run.get("status") or "").strip().lower()


def _queued_since(run: dict) -> Optional[datetime]:
    """When the run's latest attempt was asked for.

    The later of ``created_at`` and ``run_started_at``: a run re-run from
    GitHub's page keeps its first ``created_at``, and would otherwise look as
    if it had been waiting since the morning.
    """
    stamps = [s for s in (_parse(run.get("created_at")), _parse(run.get("run_started_at"))) if s]
    return max(stamps) if stamps else None


def todays_cycle_runs(runs: Iterable[Any], now: datetime) -> list[dict]:
    """The heartbeat cycle runs created on today's New York date, whatever started them.

    New York, not UTC: a catch-up cron GitHub delivers at 00:10 UTC is
    yesterday's run (20:10 the evening before in New York), and must not be
    reported as "a run today ended and wrote nothing".
    """
    today = _utc(now).astimezone(NEW_YORK).date()
    out = []
    for run in runs:
        if not isinstance(run, dict) or not is_cycle_run(run):
            continue
        created = _parse(run.get("created_at"))
        if created is not None and created.astimezone(NEW_YORK).date() == today:
            out.append(run)
    return out


def ran_before_the_open(step: dict) -> bool:
    """Whether a step began and ended before the open, on one New York day.

    Such a step could not trade. heartbeat.yml runs the cycle with plain
    ``--once``, which asks the broker's clock first and stops while the
    market is shut; and behind that gate the engine refuses every order
    into a closed market and the position manager skips the profit ladder,
    each asking the same clock (``app/execution_engine.py``,
    ``app/position_manager.py``). Counting such a step as "may have traded"
    would let one run started before the open -- a dispatch at 15:00 in
    Israel, a pre-market test, yesterday's cron delivered after midnight --
    stop every cycle for the rest of the day.

    Both times must be readable, in order and on the same New York date;
    anything less is a step that may have traded.
    """
    started, ended = _parse(step.get("started_at")), _parse(step.get("completed_at"))
    if started is None or ended is None or ended < started:
        return False
    started, ended = started.astimezone(NEW_YORK), ended.astimezone(NEW_YORK)
    return started.date() == ended.date() and ended.time() < MARKET_OPEN_NY


def trading_step_ran(jobs: Any) -> Optional[bool]:
    """Whether a run reached its trading step, from GitHub's jobs answer for it.

    ``jobs`` is what ``gh api repos/OWNER/REPO/actions/runs/ID/jobs?filter=all``
    returned: the jobs of every attempt, so a run re-run from GitHub's page
    still shows the attempt that traded, not only the latest one, which its
    guard may have stopped. True when the step is listed and was not skipped
    in any of them, whatever its result, unless it began and ended before
    the open (``ran_before_the_open``).
    False when the answer lists the run's jobs and none of them reached it:
    the step skipped (the guard said stop, or an earlier step failed), run
    wholly before the open, or not listed at all (the job never got a
    machine, or failed while setting up).
    None when there is no answer, or not one this can read -- which the
    caller must treat as "may have traded".
    """
    if not isinstance(jobs, dict) or not isinstance(jobs.get("jobs"), list):
        return None
    for job in jobs["jobs"]:
        if not isinstance(job, dict):
            return None
        steps = job.get("steps") or []
        if not isinstance(steps, list):
            return None
        for step in steps:
            if isinstance(step, dict) and step.get("name") == TRADING_STEP:
                if str(step.get("conclusion") or "").strip().lower() == "skipped":
                    continue
                if not ran_before_the_open(step):
                    return True
    return False


def _ended(run: dict, fallback: datetime) -> datetime:
    return _parse(run.get("updated_at")) or _parse(run.get("created_at")) or fallback


def decide(
    now_utc: datetime,
    runs: Optional[Iterable[Any]],
    entries: Iterable[JournalEntry],
    *,
    jobs: Optional[dict] = None,
    scheduled: time = SCHEDULED_START_UTC,
    grace: timedelta = timedelta(minutes=30),
    max_backups: int = 2,
) -> Decision:
    """What to do about today's run, at ``now_utc``.

    ``runs`` is GitHub's list of heartbeat runs (today's, though anything
    older is ignored here too), or None when the list could not be read.
    ``jobs`` maps a run id (as a string) to GitHub's jobs answer for that
    run; the workflow fetches it for every run that has finished.
    ``entries`` is the journal.

    The rules, in order -- the first that applies decides:

    1. Not a trading day in New York: nothing to do.
    2. Before the scheduled start plus ``grace``: too early to judge.
    3. The journal already has a cycle today: nothing to do.
    4. A cycle run is running: nothing to do. One waiting for a machine is
       nothing to do either, until it has waited 30 minutes (``stuck`` --
       tell the owner, start nothing) -- but only before the latest safe
       start: after it, the waiting run will stop at its guard, and the day
       falls through to the rules below.
    5. The backup has already been started ``max_backups`` times today and
       the journal still has nothing: stop trying, tell the owner.
    6. A run today finished after reaching its trading step, whatever its
       result (or the watchdog cannot tell whether it did), and the journal
       has nothing for today. A failed one may have traded and lost its
       record; a green one most likely ran on another branch, but nothing
       here can tell those apart, and heartbeat.yml's guard stops every
       later cycle today on the same evidence (``analysis/cycle_day.py``).
       Start nothing, tell the owner urgently, and say that only a re-run
       with ``rerun`` gets past. A trading step that began and ended before
       the open is not "reached" (``ran_before_the_open``): it found the
       market shut and could not trade, so such a run falls through to the
       rules below like one its guard stopped.
    7. Within ``DISPATCH_LEAD`` of the latest safe start in New York, or past
       it: ``too_late`` -- tell the owner.
    8. Otherwise: ``dispatch`` the backup, and tell the owner.
    """
    now = _utc(now_utc)
    ny_day = now.astimezone(NEW_YORK).date()
    if not is_trading_day(ny_day):
        return _quiet(f"{ny_day.isoformat()} is not a trading day in New York")

    due = datetime.combine(now.date(), scheduled, tzinfo=timezone.utc)
    if now < due + grace:
        return _quiet(f"too early to judge: the run is due at {due.strftime('%H:%M')} UTC "
                      f"and has until {(due + grace).strftime('%H:%M')} UTC to start")

    if cycle_ran_on(entries, now.date()):
        return _quiet("a cycle is already in the journal for today")

    planned = f"It was planned for {_clock(due)}."
    unread = runs is None
    cycles = [] if unread else todays_cycle_runs(runs, now)
    jobs = jobs if isinstance(jobs, dict) else {}

    running = [r for r in cycles if _status(r) == "in_progress"]
    if running:
        return _quiet(f"run {running[0].get('id')} is running now")
    waiting = [r for r in cycles if _status(r) in NOT_STARTED_STATUSES]
    if waiting and not too_late_to_start(now):
        since = [s for s in (_queued_since(r) for r in waiting) if s]
        oldest = min(since) if since else None
        if oldest is None or now - oldest <= QUEUE_PATIENCE:
            return _quiet(f"run {waiting[0].get('id')} is waiting to start")
        minutes = int((now - oldest).total_seconds() // 60)
        return Decision(
            "stuck", True, HIGH,
            "Daily run is waiting for a GitHub machine",
            f"The daily trading run was created at {_clock(oldest)} and has waited "
            f"{minutes} minutes without starting. GitHub has not given it a machine "
            f"yet. The backup did not start a second run: the waiting one starts "
            f"as soon as GitHub is ready. {planned}",
            f"run queued for {minutes} minutes without starting",
        )

    backups = [r for r in cycles if is_backup_run(r)]
    if len(backups) >= max_backups:
        return Decision(
            "none", True, URGENT,
            "No trading run today: the backup did not work",
            f"The backup has started the daily run {len(backups)} times today, and "
            f"the journal still has nothing for today. It will not try again. "
            f"Open the Actions page on GitHub to see what went wrong.",
            f"{len(backups)} backups already started today; not starting another",
        )

    # Every finished run, green ones included: heartbeat.yml's guard stops a
    # cycle after ANY other run today reached its trading step, so a backup
    # started after a green one would only stop there, after the phone had
    # been told "the backup has started it".
    finished = [r for r in cycles if _status(r) == "completed"]
    reached = [(r, trading_step_ran(jobs.get(str(r.get("id"))))) for r in finished]
    risky = [(r, ran) for r, ran in reached if ran is not False]
    if risky:
        run, ran = max(risky, key=lambda pair: _ended(pair[0], now))
        result = str(run.get("conclusion") or "unknown")
        how = ("after its trading step had started" if ran else
               "and the watchdog could not tell whether it had reached its trading step")
        by_hand = "start heartbeat by hand with rerun ticked (Actions, heartbeat, Run workflow)" + (
            ": any other start stops at its guard today." if ran else ".")
        green = result.strip().lower() == "success"
        if green and ran:
            title = "Daily run succeeded but wrote nothing: check before starting it again"
            why = ("Its record reached the repository, so it most likely ran on another "
                   "branch, but nothing here can tell that from a run that traded, so the "
                   "backup did not start another. Open the run on GitHub and check the "
                   f"account: to trade today anyway, {by_hand}")
        elif green:
            title = "Daily run succeeded but wrote nothing: check before starting it again"
            why = ("Its steps could not be read, so nothing here can tell whether it stopped "
                   "before trading or traded where this branch's record cannot show it, and "
                   "the backup did not start another. Open the run on GitHub: if it placed "
                   f"no order, {by_hand}")
        else:
            title = "Daily run failed and may have traded: check before starting it again"
            why = ("It may have placed orders whose record never reached the repository, "
                   "and a second run could sell the same profit-ladder rungs again, so the "
                   "backup did not start one. Open the run on GitHub: if it placed no "
                   f"order, {by_hand}")
        return Decision(
            "none", True, URGENT, title,
            f"A run today ended at {_clock(_ended(run, now))} with result '{result}' {how}, "
            f"and the journal has nothing for today. {why} {planned}",
            f"run {run.get('id')} ended ({result}) "
            + ("after its trading step started" if ran else "and its steps could not be read")
            + " with no journal line; not starting another",
        )

    latest = latest_start(ny_day).strftime("%H:%M")
    if too_late_to_start(now + DISPATCH_LEAD):
        ny = now.astimezone(NEW_YORK).strftime("%H:%M")
        return Decision(
            "too_late", True, URGENT,
            "No trading run today: too late to start safely",
            f"It is {_clock(now)}, {ny} in New York, and no trading run has "
            f"started today. A run must start by {latest} New York time to be done "
            f"sending orders before the market closes at "
            f"{closes_at(ny_day).strftime('%H:%M')}, and GitHub takes several "
            f"minutes to start one, so the backup did not start one. Nothing is "
            f"traded today. {planned}",
            f"too near or past the latest safe start ({latest} New York)",
        )

    if finished:
        last = max(finished, key=lambda r: _ended(r, datetime.min.replace(tzinfo=timezone.utc)))
        ended = _ended(last, now)
        result = str(last.get("conclusion") or "unknown")
        return Decision(
            "dispatch", True, HIGH,
            "Daily run wrote nothing: the backup started it again",
            f"A run today ended at {_clock(ended)} with result '{result}' and wrote "
            f"nothing to the journal. The backup has started the daily run again. "
            f"{planned}",
            f"run {last.get('id')} ended ({result}) with no journal line; starting the backup",
        )

    note = (" The watchdog could not read GitHub's list of runs, so it started "
            "the backup anyway; the backup checks the journal and GitHub's record "
            "again before it trades, and stops if a run was already on its way or "
            "has already traded.") if unread else " You do not need to do anything."
    return Decision(
        "dispatch", True, HIGH,
        "Daily run was late: the backup started it",
        f"The daily trading run had not started by {_clock(now)}. {planned} "
        f"The backup has started it now.{note}",
        "no cycle today and no run on its way; starting the backup"
        + (" (run list unreadable)" if unread else ""),
    )


def read_runs(path: Path) -> Optional[list]:
    """The runs in a saved ``gh api .../runs`` answer, or None if unreadable.

    None -- not an empty list -- because "GitHub has no run today" and "we
    could not ask GitHub" call for different messages.
    """
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    if isinstance(payload, dict) and isinstance(payload.get("workflow_runs"), list):
        return payload["workflow_runs"]
    if isinstance(payload, list):
        return payload
    return None


def read_jobs(directory: Optional[Path]) -> dict:
    """``{run id: GitHub's jobs answer}`` from ``<directory>/<run id>.json``.

    A file that cannot be read is left out, which ``decide`` reads as "could
    not tell whether that run traded" -- the safe way to be wrong.
    """
    out: dict = {}
    if directory is None or not directory.is_dir():
        return out
    for path in sorted(directory.glob("*.json")):
        try:
            out[path.stem] = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
    return out


def _one_line(text: str) -> str:
    """GITHUB_OUTPUT takes one line per key."""
    return " ".join(str(text).split())


def as_outputs(decision: Decision) -> list[str]:
    """``key=value`` lines for ``$GITHUB_OUTPUT``."""
    return [
        f"action={decision.action}",
        f"ping={'yes' if decision.ping else 'no'}",
        f"priority={decision.priority}",
        f"title={_one_line(decision.title)}",
        f"message={_one_line(decision.message)}",
        f"reason={_one_line(decision.reason)}",
    ]


def summary(decision: Decision, now: datetime) -> str:
    """A few lines of Markdown for the job summary."""
    lines = [
        "## Watchdog",
        "",
        f"Checked at {_clock(now)}. **Action:** `{decision.action}` · "
        f"**Phone:** {'yes, priority ' + str(decision.priority) if decision.ping else 'no'}",
        "",
        f"Why: {decision.reason}.",
    ]
    if decision.ping:
        lines += ["", f"> **{decision.title}**", f"> {decision.message}"]
    return "\n".join(lines) + "\n"


def main(argv: Optional[list[str]] = None) -> int:
    """Print the decision as ``key=value`` lines; a summary goes to stderr.

    Exits 0 whatever it decides, and even when it breaks: a watchdog that
    crashes must still say so on the owner's phone, not only as a red mark
    on a page nobody is looking at.
    """
    parser = argparse.ArgumentParser(description="Has today's trading run started?")
    parser.add_argument("--runs", type=Path, required=True,
                        help="GitHub's list of today's heartbeat runs, as JSON")
    parser.add_argument("--jobs", type=Path, default=None,
                        help="a directory of GitHub's jobs answers, one <run id>.json per run")
    parser.add_argument("--journal", type=Path, required=True)
    parser.add_argument("--now", default=None, help="ISO datetime, default now (UTC if naive)")
    args = parser.parse_args(argv)

    now = _parse(args.now) if args.now else datetime.now(timezone.utc)
    if now is None:
        parser.error(f"--now is not an ISO datetime: {args.now!r}")
    try:
        runs = read_runs(args.runs)
        try:
            entries = read_journal(args.journal).entries
        except FileNotFoundError:
            entries = []
        decision = decide(now, runs, entries, jobs=read_jobs(args.jobs))
    except Exception as exc:  # noqa: BLE001 - the phone must hear about a broken watchdog
        decision = Decision(
            "none", True, HIGH,
            "The watchdog could not check today's run",
            f"The watchdog stopped with an error ({type(exc).__name__}) and could "
            f"not tell whether today's trading run has started. Open the Actions "
            f"page on GitHub to check.",
            f"the watchdog failed: {type(exc).__name__}: {exc}",
        )
    print("\n".join(as_outputs(decision)))
    print(summary(decision, now), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
