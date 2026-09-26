"""Read the day's record and say, loudly, what went quietly wrong.

On 17 Sep 2026 eleven of twelve positions spent the session with no stop, a
mapped CFTC contract had been silent for four years, and a delayed cron ran
the cycle twice. Every one of those facts was already in the record -- the
journal and the audit log -- and nothing read them. A green tick sat on top.

This reads them. It is read-only, like everything in ``analysis``: it never
reaches a broker, a model, or the network. It turns the day's lines into a
short list of alarms, each **critical** (something is exposed or missing
right now) or a **warning** (something is degraded and will get worse if
nobody looks), renders them as Markdown, and exits with a code the workflow
can act on:

* ``0`` -- the record is clean;
* ``1`` -- warnings only;
* ``2`` -- at least one critical alarm.

The rules are deliberately few and each names the day it was learned. A
check nobody can explain is a check that gets switched off.

Two rules read a nightly record committed beside the journal: the shadow
funds' (``logs/funds.json``), for a calibration the owner's late-run limit
has stopped, and the race's gate (``logs/race_gate.json``), for the owner's
trigger (d) on the paper account. They are read like the others -- a
missing or broken file says nothing -- and never written. Trigger (d) is
judged on closing equity only: a mid-day reading below its line is in the
race's record as a separate "mid-day" warning, and raises no alarm here.

Three rules, from 26 Sep 2026, watch the machinery that starts the day and
keeps its record, now that the main starter is a job in the Supabase
project rather than GitHub's cron: which starter actually started today's
run (the journal's run block), whether the archive push to Supabase is set
up and working (``logs/archive_status.json``, written by
``store/push_remote.py``), and how long the GitHub token the starter uses
has left (``config.settings.GITHUB_DISPATCH_TOKEN_EXPIRES``). The first two
are read like the nightly records; the starter's own request result
(``logs/starter_status.json``) only adds detail to the first.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Iterable, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import journal_files  # noqa: E402  (standard library only)

CRITICAL = "critical"
WARNING = "warning"

#: A gap the context writer records for a mapped CFTC contract that returned
#: nothing. The prefix is the contract between ``orchestrator.context`` and
#: this reader; the test suite pins it from both sides.
CFTC_GAP_PREFIX = "CFTC positioning"

#: The gap ``orchestrator.context`` leaves when the news lookup failed. Since
#: 21 Sep 2026 that no longer costs the ticker its day -- it keeps its other
#: four dimensions -- so nothing would otherwise report a news outage at all.
#: This prefix is what makes it visible; ``orchestrator.context`` owns the
#: other side of the contract and the test suite pins both.
NEWS_GAP_PREFIX = "news unavailable"

#: Position-management actions that leave a position without a working stop.
#: ``unmanaged`` is history (the manager stopped writing it on 17 Sep 2026);
#: ``error`` is a position the manager could not read or could not protect;
#: ``no_stop`` is the one failure that is worse than an error -- the old stop
#: was cancelled to resize it and the replacement was refused (22 Sep 2026).
NAKED_ACTIONS = frozenset({"unmanaged", "error", "no_stop"})

#: Share of the day's tickers that may fail before a warning becomes
#: critical. One ticker failing is a bad afternoon; a tenth of the watchlist
#: is a dead source.
FAILED_SHARE_CRITICAL = 0.10

#: The shadow funds' nightly record, by its name beside the journal: the
#: funds workflow commits ``logs/funds.json`` next to the journal directory
#: ``logs/journal/``, so every caller that already passes the journal
#: reaches it with no new argument (``analysis/book.py`` included).
FUNDS_FILE = "funds.json"

#: The race's nightly gate record, committed beside the journal by the same
#: workflow (``analysis/horse_race.py --gate-json``). Read for trigger (d).
RACE_GATE_FILE = "race_gate.json"

#: What the Supabase starter's own request did today, as the heartbeat read
#: it from the starter's log just before the snapshot (``store/starter_status.py``).
STARTER_FILE = "starter_status.json"

#: How the last archive push to Supabase went (``store/push_remote.py
#: --status``). Written after the push, which is the heartbeat's last step,
#: so what this run reads is the previous run's push.
ARCHIVE_FILE = "archive_status.json"

#: The one file the journal was before 26 Sep 2026, beside the monthly
#: directory (``config.settings.LEGACY_SIGNAL_JOURNAL_PATH``; a test pins
#: the two together). Written here as a name so this module keeps to the
#: standard library.
LEGACY_JOURNAL_FILE = "signal_journal.log"

#: The day's main starter, as the run block names it
#: (``analysis/cycle_day.py:PRIMARY_SOURCE``). Any other source that started
#: a run is a backup that had to step in.
PRIMARY_SOURCE = "supabase-cron"

#: A run block's ``source`` as this module may print it; anything else is
#: "an unknown source" (the same token rule as ``analysis/cycle_day.py``).
_SAFE_SOURCE = re.compile(r"[a-z0-9-]{1,40}")

#: The few shapes ``store/push_remote.py`` writes as a push's error. Only
#: these are repeated in an alarm; anything else is "an unrecognised error".
_ARCHIVE_ERRORS = re.compile(r"not configured|project paused or unreachable|HTTP [0-9]{3}|push crashed \([A-Za-z]+\)")


@dataclass(frozen=True)
class Alarm:
    severity: str
    title: str
    detail: str

    @property
    def is_critical(self) -> bool:
        return self.severity == CRITICAL


def _read_lines(path: Path) -> list[dict]:
    """Every JSON object in a log, skipping what cannot be read.

    A missing file is an empty record, not an exception: the caller decides
    what an empty record means (for the journal, "no cycle today").
    """
    try:
        # The journal's monthly files joined, or one plain file (the audit).
        text = journal_files.read_text(path)
    except OSError:
        return []
    out: list[dict] = []
    for raw in text.splitlines():
        raw = raw.strip()
        if not raw:
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(record, dict):
            out.append(record)
    return out


def journal_lines_on(lines: Iterable[dict], day: date) -> list[dict]:
    """The journal lines written on ``day``, by their UTC timestamp."""
    prefix = day.isoformat()
    return [line for line in lines if str(line.get("ts_utc") or "").startswith(prefix)]


def audit_actions_on(lines: Iterable[dict], day: date) -> list[dict]:
    """The ``position_managed`` actions the audit log recorded on ``day``.

    The audit log's ``ts`` is the runner's local clock with no offset, and
    the runner is UTC; the same calendar-day match ``analysis.cycle_report``
    uses.
    """
    prefix = day.isoformat()
    out: list[dict] = []
    for record in lines:
        if (record.get("event") or record.get("message")) != "position_managed":
            continue
        if not str(record.get("ts") or record.get("asctime") or "").startswith(prefix):
            continue
        action = record.get("action")
        if isinstance(action, dict) and action.get("ticker"):
            out.append(action)
    return out


# --------------------------------------------------------------------------- #
# The rules
# --------------------------------------------------------------------------- #


def no_cycle(today: list[dict], day: Optional[date] = None) -> Optional[Alarm]:
    """16 Sep 2026: the schedule never fired and nothing noticed.

    Not on a weekend or a market holiday (``day`` given): the cycle stands
    down by design there (``orchestrator/heartbeat.py``,
    ``skip_for_non_trading_day``) and writes nothing, and every weekday
    starter -- GitHub's cron, the Supabase starter, the Routines -- still
    fires on a holiday. Without this, each holiday would turn the run red
    and page the owner urgently about a day the market was shut.
    """
    if today:
        return None
    if day is not None:
        from config.market_calendar import is_trading_day

        if not is_trading_day(day):
            return None
    return Alarm(CRITICAL, "No cycle ran today",
                 "The journal has no line dated today. No ticker was judged and the open book was not managed.")


def naked_positions(actions: list[dict]) -> Optional[Alarm]:
    """17 Sep 2026: eleven of twelve positions had no stop for a whole session.

    Judged on the *last* thing the manager said about each position today,
    so a position protected later in the day is not still an alarm.
    """
    last: dict[str, dict] = {}
    for action in actions:
        last[str(action["ticker"]).upper()] = action
    if "*" in last and last["*"].get("action") == "error":
        return Alarm(CRITICAL, "The open book could not be read",
                     f"The position manager failed before it saw any position: {last['*'].get('reason', '')}")
    naked = sorted(t for t, a in last.items() if t != "*" and a.get("action") in NAKED_ACTIONS)
    if not naked:
        return None
    reasons = "; ".join(f"{t}: {last[t].get('reason', '')}" for t in naked[:6])
    return Alarm(CRITICAL, f"{len(naked)} position(s) without a working stop",
                 f"{', '.join(naked)}. Last word from the manager -- {reasons}")


def missized_stops(actions: list[dict]) -> Optional[Alarm]:
    """22 Sep 2026: TEVA held 1 share behind a stop for 127, for six days.

    A stop is protection because it can execute, not because it exists. The
    stop leg of TEVA's original bracket was never resized when the position
    shrank to a single share, so every check that asked "is there a stop?"
    said yes while a 127-share sell order sat against 1 share held -- an
    order that could never fill. Nothing compared the two numbers.

    This does. The manager records ``stop_qty`` -- what the live stop covers
    once it is finished with a position -- alongside ``remaining_qty``, what
    is actually held. They must be equal. Judged on the last thing said about
    each position today, so one corrected later in the day is not an alarm.
    """
    last: dict[str, dict] = {}
    for action in actions:
        if action.get("stop_qty") is None:
            continue
        last[str(action["ticker"]).upper()] = action
    wrong = sorted(t for t, a in last.items()
                   if int(a["stop_qty"]) != int(a.get("remaining_qty") or 0))
    if not wrong:
        return None
    detail = "; ".join(
        f"{t}: stop covers {int(last[t]['stop_qty'])} against "
        f"{int(last[t].get('remaining_qty') or 0)} held"
        for t in wrong[:6]
    )
    return Alarm(CRITICAL, f"{len(wrong)} stop(s) sized for shares that are not held",
                 f"A stop for the wrong number of shares cannot execute, so the "
                 f"position is unprotected however live the order looks. {detail}")


def failed_calls(today: list[dict]) -> Optional[Alarm]:
    """More than 20% of the run's model calls failed, setup and model errors together.

    The owner's rule of 24 Sep 2026: such a run pings the phone the same day,
    whichever kind of failure it was. A critical alarm is what the brief's
    push sends as an urgent notification. The split into setup errors (our
    key or configuration) and model errors (timeouts, bad or empty answers)
    is ``analysis.call_errors``; only model errors count toward trigger (c).
    """
    from analysis.call_errors import SETUP
    from analysis.decision_gate import RUN_ALERT_FAILED_SHARE
    from analysis.reader import entry_from

    asked = [e for e in (entry_from(line) for line in today)
             if e is not None and not e.held and e.stage != "context"]
    failed = [e for e in asked if e.model_failed]
    if not asked or len(failed) / len(asked) <= RUN_ALERT_FAILED_SHARE:
        return None
    setup = sum(1 for e in failed if e.failure_kind == SETUP)
    sample = next((e.error for e in failed if e.error), "no error text")
    return Alarm(CRITICAL,
                 f"{len(failed)} of {len(asked)} model calls failed today "
                 f"({setup} setup, {len(failed) - setup} model)",
                 f"Above the {RUN_ALERT_FAILED_SHARE:.0%} alert line. Setup errors are our key or "
                 f"configuration and do not count toward trigger (c); model errors do. "
                 f"First error: {sample[:200]}")


def failed_tickers(today: list[dict]) -> Optional[Alarm]:
    """A ticker that produced no signal is journalled with its error (PR #56).

    One is a warning. A tenth of the watchlist is a dead source and critical.
    """
    tickers = {str(line.get("ticker")) for line in today}
    failed = sorted({str(line.get("ticker")) for line in today if line.get("error")})
    if not failed:
        return None
    share = len(failed) / max(len(tickers), 1)
    severity = CRITICAL if share >= FAILED_SHARE_CRITICAL else WARNING
    sample = next(str(line.get("error")) for line in today if line.get("error"))
    return Alarm(severity, f"{len(failed)} of {len(tickers)} ticker(s) produced no signal",
                 f"{', '.join(failed[:12])}{' …' if len(failed) > 12 else ''}. First error: {sample[:200]}")


def screen_errors(today: list[dict]) -> Optional[Alarm]:
    """The screen that failed on a ticker let it through unscreened, at full cost."""
    broken = sorted({str(line.get("ticker")) for line in today
                     if isinstance(line.get("screen"), dict) and line["screen"].get("error")})
    if not broken:
        return None
    sample = next(str(line["screen"]["error"]) for line in today
                  if isinstance(line.get("screen"), dict) and line["screen"].get("error"))
    return Alarm(WARNING, f"The screen failed on {len(broken)} ticker(s)",
                 f"{', '.join(broken[:12])}. First error: {sample.splitlines()[0][:160]}")


def cftc_gaps(today: list[dict]) -> Optional[Alarm]:
    """A mapped contract that said nothing (PR #54 made it a stated gap; this makes it heard)."""
    quiet: dict[str, str] = {}
    for line in today:
        context = line.get("context") or {}
        for gap in context.get("gaps") or []:
            if str(gap).startswith(CFTC_GAP_PREFIX):
                quiet[str(line.get("ticker"))] = str(gap)
    if not quiet:
        return None
    tickers = sorted(quiet)
    return Alarm(WARNING, f"CFTC positioning is silent for {len(tickers)} mapped contract(s)",
                 f"{', '.join(tickers)}. {quiet[tickers[0]][:200]}")


def news_gaps(today: list[dict]) -> Optional[Alarm]:
    """News that could not be fetched, now that it no longer stops the ticker.

    Before 21 Sep 2026 a failed news lookup raised and the name produced no
    signal, so ``failed_tickers`` caught it. Letting the ticker continue on
    its other four dimensions (issue #69) removed that alarm's grip on the
    case, and a silent degradation is worse than a loud failure: eighty names
    judged on four fifths of their context, with nobody told.

    Same shape as ``failed_tickers`` on purpose. One name is a flake and a
    warning; a tenth of the watchlist is the vendor being down, and that is
    critical whether or not the signals still came out.
    """
    quiet: dict[str, str] = {}
    for line in today:
        context = line.get("context") or {}
        for gap in context.get("gaps") or []:
            if str(gap).startswith(NEWS_GAP_PREFIX):
                quiet[str(line.get("ticker"))] = str(gap)
    if not quiet:
        return None
    tickers = sorted(quiet)
    seen = {str(line.get("ticker")) for line in today}
    share = len(tickers) / max(len(seen), 1)
    severity = CRITICAL if share >= FAILED_SHARE_CRITICAL else WARNING
    return Alarm(
        severity,
        f"{len(tickers)} of {len(seen)} ticker(s) were judged without news",
        f"{', '.join(tickers[:12])}{' …' if len(tickers) > 12 else ''}. "
        f"They still produced signals, on their other sections. "
        f"First gap: {quiet[tickers[0]][:200]}",
    )


def _read_record(path: Path) -> Optional[dict]:
    """One JSON object from a file, or None when it is missing or not one."""
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return record if isinstance(record, dict) else None


def calibration_stopped(funds: Optional[dict]) -> Optional[Alarm]:
    """25 Sep 2026: calibration stopped, because too many days needed late-run mirroring.

    The owner's rule: when more calibration days than the limit (2) need the
    sim to mirror a late run of the real account, that is a schedule problem
    to fix, not something to copy around, so calibration stops and the owner
    is told. The nightly funds record says "stopped" and why
    (``shadow.calibration``); this says it to the owner, every day until they
    decide. A warning, not critical: nothing in the real book is exposed, and
    a critical alarm would turn the trading run red over a simulation.
    """
    calibration = funds.get("calibration") if isinstance(funds, dict) else None
    if not isinstance(calibration, dict) or calibration.get("status") != "stopped":
        return None
    days, limit = calibration.get("mirrored_day_count"), calibration.get("mirror_limit")
    reason = str(calibration.get("stop_reason") or "the record gives no reason")
    count = f"{days} days" if isinstance(days, int) and not isinstance(days, bool) else "too many days"
    cap = f" (limit {limit})" if isinstance(limit, int) and not isinstance(limit, bool) else ""
    return Alarm(WARNING, f"Calibration stopped: late runs on {count}{cap}",
                 f"{reason[:300]}. Calibration gives neither a pass nor a fail, and the fund test "
                 f"cannot start, until the owner decides. From the funds record through "
                 f"{funds.get('final_through') or 'an unknown date'}.")


def _fraction(value: object) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value) if math.isfinite(value) else None


def drawdown_tripped(race: Optional[dict]) -> Optional[Alarm]:
    """26 Sep 2026: the owner's trigger (d) on the real paper account tripped.

    The owner's rule, replacing trigger (b): stop and tell the owner if the
    account's equity falls more than 8% below its highest close since
    2026-09-23, or its return since the 2026-09-23 close falls more than 5
    percentage points behind VT's. The race computes it every night
    (``analysis.decision_gate.drawdown_watch``) and records it in its gate
    record under ``watch.d``; this says it to the owner, every day the record
    says it tripped, until they decide. A warning, not critical, as for a
    stopped calibration: it is a question for the owner, not an exposed
    position, and nothing reverts or trades because of it.
    """
    from analysis.decision_gate import DRAWDOWN_START, INDEX_TICKER, MAX_BEHIND_VT, MAX_DRAWDOWN

    watch = race.get("watch") if isinstance(race, dict) else None
    d = watch.get("d") if isinstance(watch, dict) else None
    if not isinstance(d, dict) or d.get("tripped") is not True:
        return None
    listed = d.get("trips")
    trips = [t for t in listed if isinstance(t, dict)] if isinstance(listed, list) else []
    last = trips[-1] if trips else {}
    drawdown, gap = _fraction(last.get("drawdown")), _fraction(last.get("gap"))
    parts = []
    if last.get("below_peak") is True and drawdown is not None:
        parts.append(f"{abs(drawdown):.1%} below its peak")
    if last.get("behind_vt") is True and gap is not None:
        parts.append(f"{abs(gap) * 100:.1f} points behind {INDEX_TICKER}")
    what = " and ".join(parts) or "past the owner's limit"
    when = f" on {last['day']}" if isinstance(last.get("day"), str) else ""
    detail = str(last.get("detail") or "the record gives no detail")
    return Alarm(WARNING, f"Trigger (d) tripped: the paper account is {what}{when}",
                 f"{detail[:300]}. The owner's trigger (d): more than {MAX_DRAWDOWN:.0%} below the "
                 f"peak since {DRAWDOWN_START.isoformat()}, or more than {MAX_BEHIND_VT * 100:.0f} points "
                 f"behind {INDEX_TICKER}. Stop and tell the owner; nothing reverts or trades. Tripped on "
                 f"{len(trips) or 'at least one'} day(s); from the race gate record of "
                 f"{race.get('generated_at') or 'an unknown time'}.")


def _first_run_block(today: list[dict]) -> Optional[dict]:
    """The run block of the day's first run: the first line today that has one."""
    for line in today:
        block = line.get("run")
        if isinstance(block, dict):
            return block
    return None


#: What the starter's request result means, in words, for the codes that
#: have happened or will: GitHub answers a dispatch it accepted with 204.
_STARTER_CODES = {
    204: "GitHub accepted it",
    401: "GitHub refused the token: it has expired or was revoked",
    403: "GitHub refused the token: it may not start workflows on this repository",
    404: "GitHub could not find the workflow with that token: check its repository access",
    422: "GitHub refused the dispatch: the workflow's inputs or branch do not match",
}


def starter_result(starter: Optional[dict]) -> Optional[str]:
    """The Supabase starter's own request today, in one sentence; None with no record.

    Only the status code and a short, already-checked error text
    (``store/starter_status.py``) are used -- never anything else from the file.
    """
    if not isinstance(starter, dict):
        return None
    if starter.get("status") == "unknown":
        why = starter.get("why")
        return f"The starter's own request today could not be read ({why if isinstance(why, str) else 'no reason given'})."
    code = starter.get("status_code")
    if isinstance(code, int) and not isinstance(code, bool):
        meaning = _STARTER_CODES.get(code, "an answer the starter does not expect")
        return f"The starter's own request today: HTTP {code} ({meaning})."
    error = starter.get("error")
    if isinstance(error, str) and error:
        return f"The starter's own request today got no answer from GitHub: {error[:160]}."
    return "The starter's own request today has no answer recorded."


def started_elsewhere(today: list[dict], starter: Optional[dict] = None) -> Optional[Alarm]:
    """26 Sep 2026: the day's run should be started by the Supabase starter.

    The owner moved the day's start off GitHub's cron, which was hours late
    on every day it was measured, to a pg_cron job in the Supabase project
    that dispatches heartbeat.yml at 14:40 UTC. GitHub's cron, the Claude
    Routines, a temporary Claude bridge at 14:42 and the watchdog stay as
    backups, and the guard lets only one of them run the day. So a day
    started by any of those still ran once -- but the main starter failed,
    and the owner wants to hear it the same day. A warning, not critical:
    the day traded.

    Judged on the run block of today's first run (the one that traded).
    Says nothing when there is no block, or a block from before its
    ``source`` existed: an unknown starter is not evidence of a failed one.
    """
    block = _first_run_block(today)
    if block is None or "source" not in block:
        return None
    source = block.get("source")
    if source == PRIMARY_SOURCE:
        return None
    shown = source if isinstance(source, str) and _SAFE_SOURCE.fullmatch(source) else "an unknown source"
    detail = [f"Today's run was started by {shown}, a backup, not by the Supabase starter "
              f"(the pg_cron job that dispatches the run at 14:40 UTC). The day still ran once: "
              f"every starter goes through the same guard."]
    said = starter_result(starter)
    if said:
        detail.append(said)
    detail.append("Its log is the table public.starter_log in the Supabase project.")
    return Alarm(WARNING, f"The Supabase starter did not start today's run; {shown} did", " ".join(detail))


def legacy_journal(journal: Path) -> Optional[Alarm]:
    """The old single journal file is back, beside the monthly directory.

    Since 26 Sep 2026 the journal is one file per month in ``logs/journal/``
    and every reader joins those. Nothing reads ``logs/signal_journal.log``
    any more, so a line written there -- by an old checkout, or a workflow
    step the split missed -- is a line the race, the funds and this check
    never see. Critical, because it needs a person: move its lines into the
    right month's file, in order, and find what wrote it.
    """
    journal = Path(journal)
    stray = journal.parent / LEGACY_JOURNAL_FILE
    if not journal.is_dir() or not stray.is_file():
        return None
    return Alarm(CRITICAL, "The old journal file is back",
                 f"{stray} exists beside the monthly journal directory {journal}. Nothing reads it, "
                 "so its lines are missing from the race, the funds and this check. Move them into "
                 "the month's file in logs/journal/ (in order) and find what wrote the old file.")


def archive_problem(archive: Optional[dict]) -> Optional[Alarm]:
    """26 Sep 2026: the Supabase project was paused because nothing wrote to it.

    The heartbeat's archive push printed "No remote archive configured" on
    every run -- the two secrets were never set -- so nothing touched the
    free project and Supabase paused it. The Supabase starter lives in that
    project, so a paused project is also a day with no main starter. The
    owner wants the project kept awake, so "not configured" is a warning
    every day, and so is a push that failed (it was already sent to the
    phone the same day, by the heartbeat's own step after the push).

    Read from the push's own record, which the heartbeat writes after this
    check runs: what it says is the previous run's push. A missing or
    unreadable record says nothing.
    """
    if not isinstance(archive, dict) or archive.get("ok") is not False:
        return None
    error = archive.get("error")
    error = error if isinstance(error, str) and _ARCHIVE_ERRORS.fullmatch(error) else "an unrecognised error"
    last = archive.get("last_success")
    since = (f"The last push that worked was on {last[:10]}." if isinstance(last, str) and last
             else "No push has worked yet.")
    if error == "not configured":
        return Alarm(WARNING, "Archive not configured: the Supabase project will pause",
                     "The heartbeat's push to Supabase found no SUPABASE_URL / SUPABASE_SERVICE_KEY "
                     "secret, so nothing reaches the archive and nothing keeps the free project "
                     "awake. Supabase pauses a free project after about a week without activity, "
                     "and the Supabase starter stops with it. Add the two secrets in GitHub "
                     f"(Settings, Secrets and variables, Actions). {since}")
    advice = (" The Supabase project may be paused; restore it from the Supabase dashboard."
              if error == "project paused or unreachable" else "")
    return Alarm(WARNING, f"The archive push to Supabase failed: {error}",
                 f"The heartbeat's last push to the Supabase archive failed ({error}).{advice} "
                 f"No line is lost: the journal is in git, and the next push that works sends "
                 f"everything the archive is missing. {since}")


def dispatch_token_expiry(expires: Optional[date], day: date) -> Optional[Alarm]:
    """26 Sep 2026: the Supabase starter's GitHub token has an end date.

    ``expires`` is ``config.settings.GITHUB_DISPATCH_TOKEN_EXPIRES``, the
    one fact about the token this repository keeps (the token itself is only
    in Supabase Vault, as ``github_heartbeat_dispatch``). A warning from
    ``GITHUB_DISPATCH_TOKEN_WARN_DAYS`` days before, and critical from the
    day itself: GitHub refuses an expired token with HTTP 401, and the day's
    run then waits for a backup. The day itself counts as expired, the safe
    reading of "expires on".
    """
    from config.settings import GITHUB_DISPATCH_TOKEN_WARN_DAYS

    if not isinstance(expires, date):
        return None
    left = (expires - day).days
    how = ("Make a new fine-grained token (this repository only, Actions: read and write), put it in "
           "Supabase Vault under the same name, github_heartbeat_dispatch, and write its expiry date "
           "in config/settings.py (GITHUB_DISPATCH_TOKEN_EXPIRES).")
    if left <= 0:
        return Alarm(CRITICAL,
                     f"The GitHub token the Supabase starter uses expired on {expires.isoformat()}: make a new one",
                     f"GitHub refuses the Supabase starter's dispatch with an expired token (HTTP 401), so "
                     f"every day's run now waits for a backup. {how}")
    if left > GITHUB_DISPATCH_TOKEN_WARN_DAYS:
        return None
    return Alarm(WARNING,
                 f"The GitHub token the Supabase starter uses expires on {expires.isoformat()}: make a new one",
                 f"{left} day{'s' if left != 1 else ''} left. After that GitHub refuses the starter's "
                 f"dispatch (HTTP 401) and every day's run waits for a backup. {how}")


def duplicate_cycle(today: list[dict]) -> Optional[Alarm]:
    """16 and 17 Sep 2026: a cron delivered hours late ran the day twice."""
    counts = Counter(str(line.get("ticker")) for line in today)
    twice = sorted(t for t, n in counts.items() if n > 1)
    if not twice:
        return None
    return Alarm(WARNING, f"{len(twice)} ticker(s) were judged more than once today",
                 "A second cycle ran. It cannot double a position (the broker refuses a repeat order "
                 "inside the day), but it paid for the model twice and the journal now carries two "
                 f"opinions per name. First few: {', '.join(twice[:8])}")


#: ``check``'s default for the token's expiry: read from config.settings.
_FROM_SETTINGS = object()


def check(journal: Path, audit: Path, day: date, funds: Optional[Path] = None,
          race: Optional[Path] = None, *, starter: Optional[Path] = None,
          archive: Optional[Path] = None, token_expires: object = _FROM_SETTINGS) -> list[Alarm]:
    """Every alarm the day's record raises, critical first.

    ``funds`` is the shadow funds' record; by default the ``funds.json``
    beside the journal (``FUNDS_FILE``). ``race`` is the race's gate record;
    by default the ``race_gate.json`` beside it (``RACE_GATE_FILE``).
    ``starter`` and ``archive`` are the Supabase starter's and the archive
    push's records, by default beside the journal too (``STARTER_FILE``,
    ``ARCHIVE_FILE``). ``token_expires`` is the starter's token's expiry,
    by default ``config.settings.GITHUB_DISPATCH_TOKEN_EXPIRES``.
    """
    today = journal_lines_on(_read_lines(journal), day)
    actions = audit_actions_on(_read_lines(audit), day)
    funds_path = Path(funds) if funds is not None else Path(journal).parent / FUNDS_FILE
    race_path = Path(race) if race is not None else Path(journal).parent / RACE_GATE_FILE
    starter_path = Path(starter) if starter is not None else Path(journal).parent / STARTER_FILE
    archive_path = Path(archive) if archive is not None else Path(journal).parent / ARCHIVE_FILE
    if token_expires is _FROM_SETTINGS:
        from config.settings import GITHUB_DISPATCH_TOKEN_EXPIRES as token_expires
    found = [
        legacy_journal(journal),
        no_cycle(today, day),
        naked_positions(actions),
        missized_stops(actions),
        failed_calls(today),
        # First of the warnings: they wait on the owner, and the brief's
        # headline names the first warning. The real account before the
        # simulation.
        drawdown_tripped(_read_record(race_path)),
        calibration_stopped(_read_record(funds_path)),
        failed_tickers(today),
        screen_errors(today),
        cftc_gaps(today),
        news_gaps(today),
        duplicate_cycle(today),
        # The machinery that starts the day and keeps its record, after
        # everything about the day's trading: the brief names the first
        # warning, and a day that traded badly is the bigger news. The
        # brief has its own lines for the starter and the archive anyway.
        dispatch_token_expiry(token_expires if isinstance(token_expires, date) else None, day),
        started_elsewhere(today, _read_record(starter_path)),
        archive_problem(_read_record(archive_path)),
    ]
    alarms = [a for a in found if a is not None]
    return sorted(alarms, key=lambda a: 0 if a.is_critical else 1)


def render(alarms: list[Alarm], day: date) -> str:
    """The alarms as Markdown for a job summary or an issue. Plain words."""
    out = [f"## Health of the record for {day.isoformat()}", ""]
    if not alarms:
        out += ["Clean. Every position has a stop for the shares it holds, every ticker "
                "was judged once, every mapped source answered.", ""]
        return "\n".join(out)
    critical = [a for a in alarms if a.is_critical]
    out.append(f"**{len(critical)} critical, {len(alarms) - len(critical)} warning(s).**")
    out.append("")
    for alarm in alarms:
        mark = "🔴" if alarm.is_critical else "🟡"
        out.append(f"- {mark} **{alarm.title}.** {alarm.detail}")
    out.append("")
    return "\n".join(out)


def exit_code(alarms: list[Alarm]) -> int:
    if any(a.is_critical for a in alarms):
        return 2
    return 1 if alarms else 0


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Read the day's record and raise its alarms.")
    parser.add_argument("--journal", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--day", default=None, help="ISO date, default today in UTC")
    parser.add_argument("--funds", type=Path, default=None,
                        help="the shadow funds' record, default funds.json beside the journal")
    parser.add_argument("--race", type=Path, default=None,
                        help="the race's gate record, default race_gate.json beside the journal")
    args = parser.parse_args(argv)
    day = date.fromisoformat(args.day) if args.day else datetime.now(timezone.utc).date()
    alarms = check(args.journal, args.audit, day, args.funds, args.race)
    print(render(alarms, day), end="")
    return exit_code(alarms)


if __name__ == "__main__":
    raise SystemExit(main())
