"""The model's answers, week by week, against its own previous four weeks.

    python -m analysis.drift                  # the record, as JSON (logs/drift.json)
    python -m analysis.drift --text           # the latest weeks, for a person

The owner's weekly drift report (27 Sep 2026). A model can change without a
diff: a provider swaps what serves a name, a prompt edit shifts the answers,
a data source goes quiet and the model stops taking sides. None of that is a
change of rule, and the race would show it only months later, as a result.
This watches the answers themselves, every week:

* the share of answers that are NEUTRAL;
* the conviction of the answers that take a side: the mean, the share at or
  above the floor (``MIN_CONVICTION``), and the count in each conviction
  group the race uses;
* how often the model's side agrees with the momentum rule's, on the lines
  where both take one (the rule recomputed from the line's own technicals,
  as the race does);
* the long/short mix of the answers that take a side;
* failed calls, by type: setup errors and model errors, as
  ``analysis/call_errors.py`` splits them, each as a share of the calls
  that reached the model;
* when each day's run started, and which starter started it;
* the model, the host that served it, its settings (reasoning level,
  screening) and the prompt fingerprint (``model_setup`` on each line).

The normal band (the owner's fixed rule). A number leaves its normal band
when it is outside the mean plus or minus 2 standard deviations of the same
number over the 4 weeks before it. The standard deviation is the sample one
(divided by n - 1), and all 4 weeks must have the number, or there is no
band that week. A name -- the model, the host, a setting, the prompt
fingerprint -- leaves its band when it was not seen in any of the 4 weeks
before. No band, and so no alert, until 4 weeks of data exist.

Weeks run Monday to Sunday by the UTC date of each line, from 28 Sep 2026:
the first week in which every cycle line carries its run block, its live
price and its model setup. Only a complete week is judged; the current week
is shown "so far". The alert reaches the owner's phone once: the record
names the day to say it (``alert_on``, the first cycle day of the next
week), and the daily health check raises a warning on that day only.

Held lines (no model was asked) and lines that failed before the model was
asked (``stage == "context"``) are left out of every number: the question
is what the model did with the calls it got.

Read-only, like everything in ``analysis``: no broker, no model, no network,
no file written. The workflow redirects the output.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis.reader import JournalEntry, read_journal  # noqa: E402
from analysis.run_timing import day_timings  # noqa: E402
from config import settings as cfg  # noqa: E402
from orchestrator.technicals import TechnicalSnapshot  # noqa: E402
from rules import momentum  # noqa: E402

#: The first week judged: the Monday of the first cycle whose every line
#: carries its run block, live price and model setup.
START = date(2026, 9, 28)

#: The owner's rule: the band is the mean plus or minus this many standard
#: deviations of the same number over this many weeks before.
BAND_WEEKS = 4
BAND_SDS = 2.0

#: The day's main starter (``analysis/cycle_day.py:PRIMARY_SOURCE``).
PRIMARY_SOURCE = "supabase-cron"

#: The race's conviction groups (``analysis/horse_race.py:CONVICTION_GROUPS``),
#: with the answers under the floor counted apart.
GROUPS: tuple[tuple[str, float, float], ...] = (
    ("0.30-0.40", 0.30, 0.40),
    ("0.40-0.50", 0.40, 0.50),
    ("0.50-0.60", 0.50, 0.60),
    ("0.60+", 0.60, math.inf),
)

#: Every number judged against its band, in report order, with the words a
#: person reads it by.
NUMBERS: tuple[tuple[str, str], ...] = (
    ("neutral_pct", "NEUTRAL share (%)"),
    ("conviction_mean", "mean conviction (side-taking answers)"),
    ("at_floor_pct", "side-taking answers at or above the floor (%)"),
    ("agreement_pct", "agreement with momentum (%)"),
    ("long_pct", "longs among side-taking answers (%)"),
    ("setup_error_pct", "setup errors (% of calls)"),
    ("model_error_pct", "model errors (% of calls)"),
    ("minutes_late_mean", "run start, mean minutes after schedule"),
    ("primary_start_pct", "days started by the Supabase starter (%)"),
)

#: Every name judged against the names seen before it.
NAMES: tuple[tuple[str, str], ...] = (
    ("model", "model"),
    ("provider", "host"),
    ("reasoning_effort", "reasoning level"),
    ("screening", "screening"),
    ("prompt", "prompt fingerprint"),
)


def monday_of(day: date) -> date:
    return day - timedelta(days=day.weekday())


def week_label(monday: date) -> str:
    year, week, _ = monday.isocalendar()
    return f"{year}-W{week:02d}"


def _utc_day(entry: JournalEntry) -> Optional[date]:
    stamp = entry.timestamp
    if stamp is None:
        return None
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=timezone.utc)
    return stamp.astimezone(timezone.utc).date()


def _pct(part: int, whole: int) -> Optional[float]:
    return round(100.0 * part / whole, 2) if whole else None


def momentum_side(entry: JournalEntry) -> int:
    """+1, -1 or 0: the momentum rule's side on the line's own technicals, as the race computes it."""
    if not entry.technicals:
        return 0
    try:
        snapshot = TechnicalSnapshot.from_dict(entry.technicals)
    except Exception:  # noqa: BLE001 - a line the rule cannot read is a line with no side
        return 0
    bias = momentum.signal_for(entry.ticker, snapshot).bias.value
    return {"BULLISH": 1, "BEARISH": -1}.get(bias, 0)


def _names(entries: Sequence[JournalEntry]) -> dict[str, list[str]]:
    """Each name seen on the week's asked lines, sorted; a line without the field adds nothing."""
    seen: dict[str, set[str]] = {key: set() for key, _ in NAMES}
    for e in entries:
        setup = e.model_setup or {}
        for key in ("model", "provider", "prompt"):
            value = setup.get(key)
            if isinstance(value, str) and value:
                seen[key].add(value)
        if e.model_answered and e.model:
            seen["model"].add(e.model)
        if e.reasoning_effort:
            seen["reasoning_effort"].add(e.reasoning_effort)
        if e.screening is not None:
            seen["screening"].add("on" if e.screening else "off")
    return {key: sorted(values) for key, values in seen.items()}


def week_numbers(entries: Sequence[JournalEntry]) -> dict[str, Any]:
    """Every number of one week, from its lines. Pure: the same lines always give the same record."""
    asked = [e for e in entries if not e.held and e.stage != "context"]
    answered = [e for e in asked if e.model_answered]
    sides = [e for e in answered if e.is_directional]
    convictions = [float(e.conviction) for e in sides if e.conviction is not None]
    failed = Counter(e.failure_kind for e in asked if e.model_failed)
    both = [(e.direction, momentum_side(e)) for e in sides]
    both = [(mine, rule) for mine, rule in both if rule != 0]

    groups: dict[str, int] = {"below the floor": sum(1 for c in convictions if c < cfg.MIN_CONVICTION)}
    for label, low, high in GROUPS:
        groups[label] = sum(1 for c in convictions if low <= c < high)

    timings = day_timings(entries)
    starts = [
        {
            "day": t.day.isoformat(),
            "started_at": t.started_at.astimezone(timezone.utc).isoformat(timespec="minutes"),
            "minutes_late": t.minutes_late,
            "source": t.run_source,
            "runs": t.runs,
        }
        for t in timings
    ]
    late = [t.minutes_late for t in timings if t.minutes_late is not None]
    known = [t for t in timings if t.run_source != "unknown"]

    values = {
        "neutral_pct": _pct(sum(1 for e in answered if e.bias == "NEUTRAL"), len(answered)),
        "conviction_mean": round(statistics.fmean(convictions), 4) if convictions else None,
        "at_floor_pct": _pct(sum(1 for c in convictions if c >= cfg.MIN_CONVICTION), len(convictions)),
        "agreement_pct": _pct(sum(1 for mine, rule in both if mine == rule), len(both)),
        "long_pct": _pct(sum(1 for e in sides if e.bias == "BULLISH"), len(sides)),
        "setup_error_pct": _pct(failed.get("setup", 0), len(asked)),
        "model_error_pct": _pct(failed.get("model", 0), len(asked)),
        "minutes_late_mean": round(statistics.fmean(late), 1) if late else None,
        "primary_start_pct": _pct(sum(1 for t in known if t.run_source == PRIMARY_SOURCE), len(known)),
    }
    return {
        "days": [t.day.isoformat() for t in timings],
        "counts": {
            "lines": len(entries),
            "asked": len(asked),
            "answered": len(answered),
            "side_taking": len(sides),
            "both_take_a_side": len(both),
            "setup_errors": failed.get("setup", 0),
            "model_errors": failed.get("model", 0),
        },
        "values": values,
        "conviction_groups": groups,
        "starts": starts,
        "names": _names(asked),
    }


def band(previous: Sequence[Optional[float]]) -> Optional[dict[str, float]]:
    """The owner's band from the weeks before, or None unless all ``BAND_WEEKS`` have the number."""
    if len(previous) < BAND_WEEKS or any(v is None for v in previous[-BAND_WEEKS:]):
        return None
    last = [float(v) for v in previous[-BAND_WEEKS:]]  # type: ignore[arg-type]
    mean = statistics.fmean(last)
    sd = statistics.stdev(last)
    return {
        "mean": round(mean, 4),
        "sd": round(sd, 4),
        "low": round(mean - BAND_SDS * sd, 4),
        "high": round(mean + BAND_SDS * sd, 4),
    }


def _outside(value: Optional[float], limits: Optional[dict[str, float]]) -> bool:
    if value is None or limits is None:
        return False
    mean, sd = limits["mean"], limits["sd"]
    # Judged on the unrounded limits, so a value exactly on a limit is inside.
    return value < mean - BAND_SDS * sd or value > mean + BAND_SDS * sd


def judge(weeks: list[dict[str, Any]]) -> None:
    """Add each complete week's bands and alerts, in place, from the weeks before it."""
    for i, week in enumerate(weeks):
        previous = weeks[max(0, i - BAND_WEEKS):i]
        week["bands"], week["alerts"] = {}, []
        if not week["complete"]:
            continue
        for key, words in NUMBERS:
            limits = band([w["values"].get(key) for w in previous])
            value = week["values"].get(key)
            week["bands"][key] = limits
            if _outside(value, limits):
                week["alerts"].append(
                    f"{words}: {value:g} is outside its band {limits['low']:g} to {limits['high']:g}"
                )
        if len(previous) < BAND_WEEKS or not all(w["counts"]["asked"] for w in previous):
            continue
        for key, words in NAMES:
            before = {name for w in previous for name in w["names"].get(key, [])}
            new = [name for name in week["names"].get(key, []) if name not in before]
            if before and new:
                week["alerts"].append(f"{words}: {', '.join(new)} was not seen in the 4 weeks before")


def build(entries: Iterable[JournalEntry], today: date) -> dict[str, Any]:
    """The whole record: every week from ``START`` to today's, judged, and the day to say it."""
    by_week: dict[date, list[JournalEntry]] = {}
    first_day_this_week: Optional[date] = None
    this_monday = monday_of(today)
    for entry in entries:
        day = _utc_day(entry)
        if day is None or day < START or day > today:
            continue
        by_week.setdefault(monday_of(day), []).append(entry)
        if monday_of(day) == this_monday:
            first_day_this_week = day if first_day_this_week is None else min(first_day_this_week, day)

    weeks: list[dict[str, Any]] = []
    monday = monday_of(START)
    while monday <= this_monday:
        record = {"week": week_label(monday), "monday": monday.isoformat(),
                  "complete": monday < this_monday}
        record.update(week_numbers(by_week.get(monday, [])))
        weeks.append(record)
        monday += timedelta(days=7)
    judge(weeks)

    last_complete = next((w for w in reversed(weeks) if w["complete"]), None)
    alerts = list(last_complete["alerts"]) if last_complete else []
    # Said once: on the first cycle day of the week after the judged one.
    alert_on = first_day_this_week.isoformat() if alerts and first_day_this_week else None
    return {
        "kind": "drift",
        "made_on": today.isoformat(),
        "start": START.isoformat(),
        "rule": (f"a number leaves its band outside the mean +/- {BAND_SDS:g} sample standard "
                 f"deviations of the {BAND_WEEKS} weeks before; a name, when it was not seen in "
                 f"them; no band until {BAND_WEEKS} weeks of data exist"),
        "judged_week": last_complete["week"] if last_complete else None,
        "alerts": alerts,
        "alert_on": alert_on,
        "weeks": weeks,
    }


def render_week(week: dict[str, Any]) -> list[str]:
    """One week as plain lines: every number with its band, then the names."""
    counts = week["counts"]
    status = "" if week["complete"] else " (so far)"
    out = [f"Week of {week['monday']}{status}: {len(week['days'])} cycle day(s), "
           f"{counts['answered']} answers of {counts['asked']} calls"]
    for key, words in NUMBERS:
        value = week["values"].get(key)
        limits = (week.get("bands") or {}).get(key)
        shown = "n/a" if value is None else f"{value:g}"
        where = (f" (band {limits['low']:g} to {limits['high']:g})" if limits
                 else " (no band yet)" if week["complete"] else "")
        out.append(f"- {words}: {shown}{where}")
    groups = ", ".join(f"{label} {n}" for label, n in week["conviction_groups"].items())
    out.append(f"- conviction groups: {groups}")
    starters = Counter(s["source"] for s in week["starts"])
    if starters:
        out.append("- started by: " + ", ".join(f"{s} {n}" for s, n in sorted(starters.items())))
    for key, words in NAMES:
        names = week["names"].get(key) or ["none recorded"]
        out.append(f"- {words}: {', '.join(names)}")
    for alert in week.get("alerts") or []:
        out.append(f"- OUTSIDE ITS BAND: {alert}")
    return out


def render(record: dict[str, Any], weeks: int = 2) -> str:
    """The latest ``weeks`` weeks as text, newest first."""
    out = [f"Drift report, made {record['made_on']}. Rule: {record['rule']}.", ""]
    for week in list(reversed(record["weeks"]))[:weeks]:
        out += render_week(week) + [""]
    return "\n".join(out).rstrip() + "\n"


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="The model's answers, week by week, against its last 4 weeks.")
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH)
    parser.add_argument("--day", default=None, help="ISO date, default today in UTC")
    parser.add_argument("--text", action="store_true", help="plain text instead of JSON")
    args = parser.parse_args(argv)
    today = date.fromisoformat(args.day) if args.day else datetime.now(timezone.utc).date()
    record = build(read_journal(args.journal).entries, today)
    print(render(record) if args.text else json.dumps(record, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
