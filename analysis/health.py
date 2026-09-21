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
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Iterable, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

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
#: ``error`` is a position the manager could not read or could not protect.
NAKED_ACTIONS = frozenset({"unmanaged", "error"})

#: Share of the day's tickers that may fail before a warning becomes
#: critical. One ticker failing is a bad afternoon; a tenth of the watchlist
#: is a dead source.
FAILED_SHARE_CRITICAL = 0.10


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
        text = path.read_text(encoding="utf-8")
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


def no_cycle(today: list[dict]) -> Optional[Alarm]:
    """16 Sep 2026: the schedule never fired and nothing noticed."""
    if today:
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


def check(journal: Path, audit: Path, day: date) -> list[Alarm]:
    """Every alarm the day's record raises, critical first."""
    today = journal_lines_on(_read_lines(journal), day)
    actions = audit_actions_on(_read_lines(audit), day)
    found = [
        no_cycle(today),
        naked_positions(actions),
        failed_tickers(today),
        screen_errors(today),
        cftc_gaps(today),
        news_gaps(today),
        duplicate_cycle(today),
    ]
    alarms = [a for a in found if a is not None]
    return sorted(alarms, key=lambda a: 0 if a.is_critical else 1)


def render(alarms: list[Alarm], day: date) -> str:
    """The alarms as Markdown for a job summary or an issue. Plain words."""
    out = [f"## Health of the record for {day.isoformat()}", ""]
    if not alarms:
        out += ["Clean. Every position has a stop, every ticker was judged once, every mapped source answered.", ""]
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
    args = parser.parse_args(argv)
    day = date.fromisoformat(args.day) if args.day else datetime.now(timezone.utc).date()
    alarms = check(args.journal, args.audit, day)
    print(render(alarms, day), end="")
    return exit_code(alarms)


if __name__ == "__main__":
    raise SystemExit(main())
