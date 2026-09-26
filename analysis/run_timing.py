"""When each cycle actually ran, against when it was scheduled to.

    python analysis/run_timing.py
    python analysis/run_timing.py --journal logs/journal

The race scores a signal from the moment the journal says it was made, so
the one thing a late run could corrupt is the entry: a signal made at 15:00
New York and "entered" at that morning's open would be scored on a price
that was already history when the model was asked. The race does not do
that -- entry is always the open of the next session after the signal's
day, pinned by ``tests/test_race_entry_timing.py`` -- so a late run changes
WHEN a signal is made, never the price it is entered at. What a late run
does change is what the model saw (a morning's prices, or an afternoon's),
and that is worth being able to see day by day. This module is how.

GitHub's scheduler delivered the heartbeat's cron runs hours late on every
day the 12:35 UTC slot existed (21-24 Sep 2026: 4.5 to 5.7 hours; on 25 Sep
it had not arrived by 15:00 UTC), and every cycle since 21 Sep was in fact
started by a backup dispatch at about 15:05 UTC. Nothing in the journal said
so. Two sources, in order of trust:

* **the journal run block** -- from the first heartbeat cycle after the
  change that added it (28 Sep 2026 at the earliest; 25 Sep's cycle ran the
  code before it), every line the heartbeat's cycle step writes carries
  ``run``: what started it (``schedule``, ``scheduler``, ``backup`` or
  ``manual``), the day's scheduled start, when the cycle step started, how
  many minutes late that was, and the GitHub run id; from 26 Sep 2026 also
  ``source``, which starter asked for the run (``supabase-cron``, the main
  one; ``claude-bridge``, ``claude-routine``, ``watchdog``, ``manual`` or
  ``github-schedule``). When a day has one, it wins.
* **inferred from the first line** -- every earlier day has no run block,
  so its start is taken to be its first journal line and its scheduled
  start comes from ``SCHEDULE_HISTORY`` below, which is the heartbeat's own
  cron history written down. What started it is ``unknown``.

Pure functions over journal entries, and a ``main`` that prints. Read-only
in every direction, like everything in ``analysis``: it reads the journal
and writes nothing. It decides nothing either -- the race prints it beside
the gate, and no look, bar or verdict reads it.
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime, time, timezone
from pathlib import Path
from typing import Any, Iterable, Optional, Sequence

# Allow ``python analysis/run_timing.py`` from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis.returns import MARKET_TZ, SESSION_CLOSE_LOCAL  # noqa: E402
from config.market_calendar import is_trading_day  # noqa: E402

#: The regular session opens at 09:30 New York; it closes at
#: ``SESSION_CLOSE_LOCAL`` (16:00), the same close the scorer's finality
#: rule reads, so the two can never disagree about when a day ended.
SESSION_OPEN_LOCAL = time(9, 30)

#: Where a journal line was written, relative to the New York session on
#: its own New York calendar day. ``no_session`` is a weekend or a full-day
#: holiday: there was no open to be before, and no close to be after.
#:
#: Half days are not known: ``config.market_calendar`` deliberately treats
#: an early close (13:00 New York, the day after Thanksgiving and some
#: Christmas Eves) as a trading day and says nothing about its hours. A line
#: written between 13:00 and 16:00 on such a day therefore reads ``session``
#: although the market had shut. (``analysis.cycle_day.EARLY_CLOSES`` knows
#: them, for the one question that needs them: whether a run may start.) The
#: heartbeat starts at 14:40 UTC (09:40 or 10:40 New York) once the change
#: that moved it is live, well before any early close, so this costs nothing
#: today; it is written down so nobody has to rediscover it.
PRE_OPEN = "pre_open"
SESSION = "session"
AFTER_CLOSE = "after_close"
NO_SESSION = "no_session"
PHASES = (PRE_OPEN, SESSION, AFTER_CLOSE, NO_SESSION)

#: A day whose run started more than this many minutes after its scheduled
#: start is a late-run day. The same threshold the journal run block's own
#: ``late`` flag uses, so a day reads the same whichever source it came from.
LATE_AFTER_MINUTES = 30

#: What may have started a run, as the journal run block records it.
#: ``scheduler`` is an outside scheduler that is the day's main start (the
#: Supabase starter, from 26 Sep 2026), not a rescue.
TRIGGERS = ("schedule", "scheduler", "backup", "manual")
UNKNOWN = "unknown"

#: A run block's ``source``: which starter asked for the run. The same short
#: safe token ``analysis/cycle_day.py:SOURCE_PATTERN`` writes; read again
#: here because a line is read months after another process wrote it.
SOURCE_PATTERN = re.compile(r"[a-z0-9-]{1,40}")

#: Where a day's timing came from. Printed in full in the JSON, shortened
#: in the text table.
FROM_RUN_BLOCK = "journal run block"
INFERRED = "inferred from the first line"

#: The one sentence the race prints under the table. Pinned by
#: ``tests/test_race_entry_timing.py``, which checks the code does what it
#: says for every time of day a line can be written.
ENTRY_SENTENCE = (
    "Entry is always the open of the next session after the signal's day, so a late run "
    "changes when a signal is made, never the price it is entered at."
)

#: The heartbeat's scheduled start, UTC, as ``(first day it applied, time)``.
#: Each entry applies from its day until the next one's. This is the cron
#: history of ``.github/workflows/heartbeat.yml`` on ``main``, read from git
#: and the GitHub API on 25 Sep 2026, written down because a day with no
#: journal run block has nothing else to be measured against. A day before
#: the first entry has no known schedule and is never called late. The cron
#: runs Monday to Friday only, so a weekend day has no scheduled start.
#:
#: * 14 Sep: ``5 13-21 * * 1-5``, hourly; the first slot, 13:05, is the
#:   day's scheduled start. (Replaced at 21:26 UTC that day.)
#: * 15-18 Sep: ``5 15 * * 1-5``, 15:05. From 16 Sep a second slot at 17:35
#:   was added as a catch-up; the day's start is still the first slot.
#: * from 21 Sep: ``35 12 * * 1-5`` with ``--premarket``, 12:35, meant to
#:   run before the open. GitHub delivered it between 17:11 and 18:17 UTC on
#:   21-24 Sep and had not delivered it by 15:00 UTC on 25 Sep; a backup
#:   dispatch at about 15:05 started every cycle first, and no cycle ever
#:   ran before the open.
#:
#: There is no row for the 14:40 UTC start that replaced 12:35, on purpose.
#: The same change that moved the cron made every cycle line carry a run
#: block, and a day with one is measured against the block's own
#: ``scheduled_for``, never this table. So the table only ever measures days
#: from before that change -- whose cron was the last row here, for however
#: many days the change took to merge. A row dated by a guess at the merge
#: day would have measured every weekday between the guess and the real
#: merge against the wrong time, and an old row may not be edited. (A day
#: after the change with no block at all -- a local run, or a block that
#: could not be built -- is measured against the last row too, and reads
#: ``inferred``, so it can be seen for what it is.)
#:
#: When the schedule changes again, and a day could be journalled without a
#: run block under it, add a row; never edit an old one. The rows are the
#: record of what each past day was measured against.
SCHEDULE_HISTORY: tuple[tuple[date, time], ...] = (
    (date(2026, 9, 14), time(13, 5)),
    (date(2026, 9, 15), time(15, 5)),
    (date(2026, 9, 21), time(12, 35)),
)


# --------------------------------------------------------------------------- #
# Small, total parsers: junk in, None out, never an exception
# --------------------------------------------------------------------------- #


def to_utc(value: Any) -> Optional[datetime]:
    """``value`` as a timezone-aware UTC datetime, or None if it is not one.

    A naive datetime is read as UTC, the same rule ``analysis.reader`` applies
    to the old tz-naive ``ts`` field. A string is read as ISO-8601, with a
    trailing ``Z`` accepted. Anything else -- a number, a dict, a malformed
    string -- is None. The run block is written by another process and read
    months later; this is the one place its dates are trusted.
    """
    if isinstance(value, str):
        text = value.strip()
        if text.endswith(("Z", "z")):
            text = text[:-1] + "+00:00"
        try:
            value = datetime.fromisoformat(text)
        except ValueError:
            return None
    if not isinstance(value, datetime):
        return None
    try:
        if value.tzinfo is None or value.tzinfo.utcoffset(value) is None:
            return value.replace(tzinfo=timezone.utc)
        return value.astimezone(timezone.utc)
    except (OverflowError, ValueError):
        return None


def _integer(value: Any) -> Optional[int]:
    """An int that is not a bool; a float only if it is whole and finite."""
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and math.isfinite(value) and value == int(value):
        return int(value)
    return None


# --------------------------------------------------------------------------- #
# The journal run block
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class RunBlock:
    """The usable parts of one line's ``run`` block. Any field may be None."""

    trigger: Optional[str]
    scheduled_for: Optional[datetime]
    started_at: Optional[datetime]
    minutes_late: Optional[int]
    late: Optional[bool]
    run_id: Optional[str]
    #: Which starter asked for the run; None on a block from before the
    #: field existed, ``unknown`` when it is not a short safe token.
    source: Optional[str] = None

    @property
    def has_timing(self) -> bool:
        """The block says something about when, not only who."""
        return any(v is not None for v in (self.scheduled_for, self.started_at, self.minutes_late, self.late))


def parse_run_block(value: Any) -> Optional[RunBlock]:
    """A ``run`` block as journalled, or None when there is nothing usable in it.

    Each field is taken only if it has the type the agreed format gives it;
    a field of the wrong type is dropped, not coerced, and the rest of the
    block still counts. A trigger outside the known ones is ``unknown``
    rather than printed, and so is a ``source`` that is not a short safe
    token: the text is a report, and a report should not echo whatever a
    line happened to carry.
    """
    if not isinstance(value, dict):
        return None
    trigger = value.get("trigger")
    run_id = value.get("run_id")
    late = value.get("late")
    source = value.get("source")
    if source is not None:
        source = source if isinstance(source, str) and SOURCE_PATTERN.fullmatch(source) else UNKNOWN
    block = RunBlock(
        trigger=trigger if isinstance(trigger, str) and trigger in TRIGGERS else None,
        scheduled_for=to_utc(value.get("scheduled_for")),
        started_at=to_utc(value.get("started_at")),
        minutes_late=_integer(value.get("minutes_late")),
        late=late if isinstance(late, bool) else None,
        run_id=(str(run_id) if isinstance(run_id, (str, int)) and not isinstance(run_id, bool)
                and str(run_id).strip() else None),
        source=source,
    )
    if block.trigger is None and block.run_id is None and not block.has_timing:
        return None
    return block


def run_block_of(entry: Any) -> Optional[RunBlock]:
    """The run block of one journal entry, whatever the entry is.

    ``getattr`` rather than ``entry.run`` so this reads entries from before
    ``JournalEntry`` had the field as well as after, and the ``try`` because
    a property that raises must cost this report one line, not the race.
    """
    try:
        raw = getattr(entry, "run", None)
    except Exception:  # noqa: BLE001 - a broken field is an absent one here
        return None
    return parse_run_block(raw)


# --------------------------------------------------------------------------- #
# The schedule, and where in the day a line fell
# --------------------------------------------------------------------------- #


def scheduled_start(day: date) -> Optional[datetime]:
    """The heartbeat's scheduled start on ``day`` (UTC), from ``SCHEDULE_HISTORY``.

    None before the history starts, and on a Saturday or Sunday, when the
    cron does not fire. A weekday holiday keeps its time: the cron fires on
    it (the cycle itself then stands down), so a line written on one is
    still measured against it.
    """
    if day.weekday() >= 5:
        return None
    applies: Optional[time] = None
    for first_day, at in SCHEDULE_HISTORY:
        if day >= first_day:
            applies = at
    if applies is None:
        return None
    return datetime.combine(day, applies, tzinfo=timezone.utc)


def session_phase(moment: datetime) -> str:
    """``pre_open``, ``session``, ``after_close`` or ``no_session`` for one instant.

    Judged on the New York calendar day the instant falls in, so a line at
    00:30 UTC is the previous New York evening's ``after_close``, not the
    next morning's ``pre_open``.
    """
    local = to_utc(moment).astimezone(MARKET_TZ)
    if not is_trading_day(local.date()):
        return NO_SESSION
    clock = local.time().replace(tzinfo=None)
    if clock < SESSION_OPEN_LOCAL:
        return PRE_OPEN
    if clock < SESSION_CLOSE_LOCAL:
        return SESSION
    return AFTER_CLOSE


# --------------------------------------------------------------------------- #
# One cycle day
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class DayTiming:
    """One cycle day (the UTC date of its journal lines), and when it ran."""

    day: date
    lines: int
    first_utc: datetime
    last_utc: datetime
    #: Lines per phase, every phase in ``PHASES`` order.
    phases: tuple[tuple[str, int], ...]
    #: The day's scheduled start: the run block's if it gave one, else
    #: ``SCHEDULE_HISTORY``'s; None when neither knows.
    scheduled_for: Optional[datetime]
    #: When the run started: the run block's if it gave one, else the first line.
    started_at: datetime
    #: ``started_at - scheduled_for`` in whole minutes, floored (the run
    #: block's own number when it gave one). Negative is early.
    minutes_late: Optional[int]
    #: More than ``LATE_AFTER_MINUTES`` late (the run block's own flag when it
    #: gave one). None when there is no schedule to be late against.
    late: Optional[bool]
    started_by: str
    source: str
    #: Which starter asked for the day's first run (the run block's
    #: ``source``: ``supabase-cron``, ``claude-bridge``, ``watchdog``...);
    #: ``unknown`` on a day with no block, or a block from before the field.
    #: Not to be confused with ``source`` above, which says where this
    #: row's timing came from.
    run_source: str
    #: Distinct GitHub run ids the day's run blocks name. 0 on a day with
    #: none; more than 1 means more than one cycle wrote lines that day.
    runs: int

    @property
    def first_new_york(self) -> datetime:
        return self.first_utc.astimezone(MARKET_TZ)

    @property
    def last_new_york(self) -> datetime:
        return self.last_utc.astimezone(MARKET_TZ)

    def count(self, phase: str) -> int:
        return dict(self.phases).get(phase, 0)

    @property
    def phase(self) -> str:
        """The day's one phase, or ``mixed`` when its lines fell in more than one."""
        present = [name for name, n in self.phases if n]
        return present[0] if len(present) == 1 else "mixed"


def day_timings(entries: Iterable[Any]) -> list[DayTiming]:
    """Every cycle day in ``entries``, oldest first.

    Every line with a timestamp counts -- held, failed and answered alike --
    because the question is when the cycle ran, not what it said. A line
    with no timestamp cannot be placed and is left out.
    """
    by_day: dict[date, list[tuple[datetime, Any]]] = {}
    for entry in entries:
        stamp = to_utc(getattr(entry, "timestamp", None))
        if stamp is None:
            continue
        by_day.setdefault(stamp.date(), []).append((stamp, entry))
    return [_one_day(day, sorted(rows, key=lambda row: row[0])) for day, rows in sorted(by_day.items())]


def _one_day(day: date, rows: list[tuple[datetime, Any]]) -> DayTiming:
    first, last = rows[0][0], rows[-1][0]
    tally = {name: 0 for name in PHASES}
    for stamp, _ in rows:
        tally[session_phase(stamp)] += 1

    # The day's first usable run block, in line order: when two runs wrote
    # lines on one day, the first run is the one that was (or was not) late.
    blocks = [block for block in (run_block_of(entry) for _, entry in rows) if block is not None]
    block = blocks[0] if blocks else None
    timed = next((b for b in blocks if b.has_timing), None)

    scheduled = (timed.scheduled_for if timed and timed.scheduled_for else None) or scheduled_start(day)
    started = (timed.started_at if timed and timed.started_at else None) or first
    if timed is not None and timed.minutes_late is not None:
        minutes: Optional[int] = timed.minutes_late
    elif scheduled is not None:
        minutes = math.floor((started - scheduled).total_seconds() / 60.0)
    else:
        minutes = None
    if timed is not None and timed.late is not None:
        late: Optional[bool] = timed.late
    else:
        late = None if minutes is None else minutes > LATE_AFTER_MINUTES

    return DayTiming(
        day=day, lines=len(rows), first_utc=first, last_utc=last,
        phases=tuple((name, tally[name]) for name in PHASES),
        scheduled_for=scheduled, started_at=started, minutes_late=minutes, late=late,
        started_by=(block.trigger if block and block.trigger else UNKNOWN),
        source=FROM_RUN_BLOCK if timed is not None else INFERRED,
        run_source=(block.source if block and block.source else UNKNOWN),
        runs=len({b.run_id for b in blocks if b.run_id}),
    )


# --------------------------------------------------------------------------- #
# Totals, JSON and text
# --------------------------------------------------------------------------- #


def part_of(day: date, cutoff: Optional[date]) -> Optional[str]:
    """``window`` or ``before`` against the race's decision cutoff; None without one."""
    if cutoff is None:
        return None
    return "window" if day >= cutoff else "before"


def totals(timings: Sequence[DayTiming]) -> dict[str, int]:
    """The count line's numbers: late days, days, and lines outside the session."""
    return {
        "late_days": sum(1 for t in timings if t.late),
        "cycle_days": len(timings),
        "unscheduled_days": sum(1 for t in timings if t.late is None),
        "lines_before_open": sum(t.count(PRE_OPEN) for t in timings),
        "lines_after_close": sum(t.count(AFTER_CLOSE) for t in timings),
        "lines_no_session": sum(t.count(NO_SESSION) for t in timings),
    }


def timing_json(timings: Sequence[DayTiming], cutoff: Optional[date] = None) -> dict:
    """The table as data: strings, ints, bools and nulls only, so it serialises strictly."""
    def stamp(value: Optional[datetime]) -> Optional[str]:
        return None if value is None else value.isoformat()

    window = [t for t in timings if part_of(t.day, cutoff) == "window"]
    return {
        "entry_rule": ENTRY_SENTENCE,
        "late_after_minutes": LATE_AFTER_MINUTES,
        "cutoff": None if cutoff is None else cutoff.isoformat(),
        **totals(timings),
        "window_late_days": sum(1 for t in window if t.late),
        "window_cycle_days": len(window),
        "days": [
            {
                "day": t.day.isoformat(),
                "part": part_of(t.day, cutoff),
                "lines": t.lines,
                "first_utc": stamp(t.first_utc),
                "last_utc": stamp(t.last_utc),
                "first_new_york": t.first_new_york.strftime("%H:%M"),
                "last_new_york": t.last_new_york.strftime("%H:%M"),
                "phase": t.phase,
                "phases": dict(t.phases),
                "scheduled_for": stamp(t.scheduled_for),
                "started_at": stamp(t.started_at),
                "minutes_late": t.minutes_late,
                "late": t.late,
                "started_by": t.started_by,
                "source": t.source,
                "run_source": t.run_source,
                "runs": t.runs,
            }
            for t in timings
        ],
    }


def _short_source(source: str) -> str:
    return "run block" if source == FROM_RUN_BLOCK else "inferred"


def render(timings: Sequence[DayTiming], cutoff: Optional[date] = None) -> list[str]:
    """The section as printed lines, one per cycle day, then the counts and the entry sentence."""
    out = [
        "",
        "RUN TIMING (when each cycle ran; report only, decides nothing)",
        "-" * 78,
        "One line per cycle day (the UTC date of its lines): first-last line in New York",
        "time, where in the session they fell, minutes after the scheduled start, what",
        f"started it, and LATE when that was more than {LATE_AFTER_MINUTES} minutes. 'run block' is the",
        "journal's own record of the run; 'inferred' is the first line against the",
        "heartbeat's cron history. 'via' is the starter that asked for the run, when",
        "the run block names it: supabase-cron is the main one, anything else a backup.",
    ]
    if not timings:
        return out + ["no cycle day with a timestamp in the journal", "", ENTRY_SENTENCE]
    labelled = cutoff is not None
    out.append((
        f"{'day':<12}" + (f"{'part':<8}" if labelled else "")
        + f"{'New York':<13}{'phase':<12}{'vs sched':>9}  {'by':<10}{'source':<10}"
    ).rstrip())
    for t in timings:
        vs = "n/a" if t.minutes_late is None else f"{t.minutes_late:+d} min"
        marks = " ".join(mark for mark in (
            "LATE" if t.late else "",
            f"({t.runs} runs)" if t.runs > 1 else "",
            f"via {t.run_source}" if t.run_source != UNKNOWN else "",
        ) if mark)
        out.append((
            f"{t.day.isoformat():<12}" + (f"{part_of(t.day, cutoff):<8}" if labelled else "")
            + f"{t.first_new_york:%H:%M}-{t.last_new_york:%H:%M}  {t.phase:<12}{vs:>9}  "
            f"{t.started_by:<10}{_short_source(t.source):<10}{marks}"
        ).rstrip())
    counts = totals(timings)
    line = (f"late-run days: {counts['late_days']} of {counts['cycle_days']}; "
            f"lines before the open: {counts['lines_before_open']}; "
            f"after the close: {counts['lines_after_close']}")
    if counts["lines_no_session"]:
        line += f"; on a day with no session: {counts['lines_no_session']}"
    out.append(line)
    if counts["unscheduled_days"]:
        out.append(f"note: {counts['unscheduled_days']} day(s) have no known schedule (a weekend, or "
                   f"before {SCHEDULE_HISTORY[0][0].isoformat()}), so none of them is called late")
    if labelled:
        window = [t for t in timings if part_of(t.day, cutoff) == "window"]
        out.append(f"in the decision window (from {cutoff.isoformat()}): late-run days "
                   f"{sum(1 for t in window if t.late)} of {len(window)}")
    out += ["", ENTRY_SENTENCE]
    return out


def main(argv: Optional[list[str]] = None) -> int:
    from analysis import decision_gate
    from analysis.reader import read_journal
    from config import settings as cfg

    parser = argparse.ArgumentParser(
        prog="run_timing", description="When each cycle ran, against when it was scheduled to.",
    )
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH,
                        help="path to the signal journal (default: %(default)s)")
    args = parser.parse_args(argv)
    try:
        read = read_journal(args.journal)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print("\n".join(render(day_timings(read.entries), cutoff=decision_gate.DECISION_CUTOFF)).lstrip("\n"))
    return 0


__all__ = [
    "AFTER_CLOSE",
    "DayTiming",
    "ENTRY_SENTENCE",
    "FROM_RUN_BLOCK",
    "INFERRED",
    "LATE_AFTER_MINUTES",
    "NO_SESSION",
    "PHASES",
    "PRE_OPEN",
    "RunBlock",
    "SCHEDULE_HISTORY",
    "SESSION",
    "SESSION_OPEN_LOCAL",
    "TRIGGERS",
    "UNKNOWN",
    "day_timings",
    "parse_run_block",
    "part_of",
    "render",
    "run_block_of",
    "scheduled_start",
    "session_phase",
    "timing_json",
    "to_utc",
    "totals",
]


if __name__ == "__main__":
    raise SystemExit(main())
