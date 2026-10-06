"""The model's answers, week by week, against their own history; its settings, day by day.

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
  screening) and the prompt fingerprint (``model_setup`` on each line);
* the names whose news search found no headline on any of their lines that
  week, with their list (the owner's request of 3 Oct 2026; a report only,
  with no band and no alert), and which of them had a failed search.
* how many of production's own news fetches failed that week, of how many
  lines, and on which day (the owner's request of 6 Oct 2026; a report only,
  with no band and no alert).

The owner's rule, as changed on 27 Sep 2026 before any data existed:

* **Settings** -- the model, the host, the reasoning level, screening and
  the prompt fingerprint -- alert on any change, the same day: a value on
  today's lines that the last cycle day before it did not have, or two
  values on today's lines. Nothing is waited for.
* **Numbers** -- the NEUTRAL share, the mean conviction, agreement with
  momentum, the long share, setup and model errors, and lateness (``BANDED``)
  -- have a band: the mean plus or minus 2 standard deviations (the sample
  one, divided by n - 1) of the same number over **every** complete week
  before, from the first. No band until 4 weeks have the number. An alert
  fires only when a number is outside its band **2 weeks in a row** (each
  week against its own band). The share at or above the floor and the share
  of days the Supabase starter started are shown, with no band (``SHOWN``).

Weeks run Monday to Sunday by the UTC date of each line, from 28 Sep 2026:
the first week in which every cycle line carries its run block, its live
price and its model setup. Only a complete week is judged; the current week
is shown "so far". A number's alert reaches the owner's phone once: the
record names the day to say it (``alert_on``, the first cycle day of the
next week), and the daily health check raises a warning on that day only. A
setting's alert is said on the day it is seen (``setting_alert_on``).

Held lines (no model was asked) and lines that failed before the model was
asked (``stage == "context"``) are left out of the answer numbers (the
NEUTRAL share, conviction, agreement, the long share, the error shares and
the names): the question is what the model did with the calls it got. Two
things read more lines. The run start, its lateness and the starter share
read every line, because the question there is when the cycle ran
(``analysis/run_timing.day_timings``). The count of names with no headlines
reads held lines too -- a held name's news is still searched and journalled,
and leaving those lines out would miss a name held all week or count a name
as silent when its held line had news -- and a line that failed before the
model was asked counts only when it carried headlines: a failed gather
journals an empty context, which is not a search that found nothing, while a
prompt that failed to render journals the context it gathered.

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

from analysis.health import NEWS_GAP_PREFIX  # noqa: E402
from analysis.reader import JournalEntry, read_journal  # noqa: E402
from analysis.run_timing import day_timings  # noqa: E402
from config import settings as cfg  # noqa: E402
from orchestrator.technicals import TechnicalSnapshot  # noqa: E402
from rules import momentum  # noqa: E402

#: The first week judged: the Monday of the first cycle whose every line
#: carries its run block, live price and model setup.
START = date(2026, 9, 28)

#: The owner's rule: the band is the mean plus or minus this many standard
#: deviations of every complete week before; none until this many weeks have
#: the number; an alert after this many weeks outside it in a row.
MIN_WEEKS = 4
BAND_SDS = 2.0
IN_A_ROW = 2

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
BANDED: tuple[tuple[str, str], ...] = (
    ("neutral_pct", "NEUTRAL share (%)"),
    ("conviction_mean", "mean conviction (side-taking answers)"),
    ("agreement_pct", "agreement with momentum (%)"),
    ("long_pct", "longs among side-taking answers (%)"),
    ("setup_error_pct", "setup errors (% of calls)"),
    ("model_error_pct", "model errors (% of calls)"),
    ("minutes_late_mean", "run start, mean minutes after schedule"),
)

#: Numbers shown every week with no band.
SHOWN: tuple[tuple[str, str], ...] = (
    ("at_floor_pct", "side-taking answers at or above the floor (%)"),
    ("primary_start_pct", "days started by the Supabase starter (%)"),
)

NUMBERS: tuple[tuple[str, str], ...] = BANDED + SHOWN

#: Every setting, judged day by day against the last cycle day before.
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


#: The most names the phone line lists; the report and the record list them all.
PHONE_NAMES = 12


def no_headlines(entries: Sequence[JournalEntry]) -> dict[str, Any]:
    """The names whose news was empty on every line of the week, and which of them had a failed search.

    Every line that says how many headlines it carried counts, held lines
    included. A line without the field does not, and neither does a line
    that failed before the model was asked (``stage == "context"``) with no
    headline: a failed gather journals an empty context, which is not a
    search that found nothing. A prompt that failed to render journals the
    context it gathered, so its headlines count. A name is listed when all
    its counted lines that week had zero headlines.
    ``search_failed`` names those of them with at least one failed news
    search that week (a gap starting ``NEWS_GAP_PREFIX``): for them "no
    headlines" may be the vendor's fault, not an empty search.
    """
    lines: dict[str, list[JournalEntry]] = {}
    for e in entries:
        if e.headline_count is None or (e.stage == "context" and not e.headline_count):
            continue
        lines.setdefault(e.ticker, []).append(e)
    silent = sorted(t for t, own in lines.items() if not any(e.headline_count for e in own))
    failed = [t for t in silent if any(g.startswith(NEWS_GAP_PREFIX) for e in lines[t] for g in e.gaps)]
    return {"names": len(lines), "no_headlines": silent, "search_failed": failed}


def no_headlines_line(news: Optional[dict[str, Any]], limit: Optional[int] = None) -> Optional[str]:
    """The count and the list in one line; ``limit`` caps the names shown. None when nothing could be counted."""
    if not isinstance(news, dict) or not news.get("names"):
        return None
    silent = list(news.get("no_headlines") or [])
    shown = silent if limit is None or len(silent) <= limit else silent[:limit] + ["…"]
    line = f"names with no headlines all week: {len(silent)} of {news['names']}"
    line += f" ({', '.join(shown)})" if silent else ""
    failed = list(news.get("search_failed") or [])
    if failed:
        listed = failed if limit is None or len(failed) <= limit else failed[:limit] + ["…"]
        line += f"; the news search failed at least once for {len(failed)} of them ({', '.join(listed)})"
    return line


def news_fetches(entries: Sequence[JournalEntry]) -> dict[str, Any]:
    """How many of production's news fetches failed: lines with a failed search, of the lines that searched.

    A line searched when it says how many headlines it carried, by the same
    rule as ``no_headlines`` (held lines included; not a line that failed
    before the model was asked with no headline). A fetch failed when the
    line's gaps start with ``NEWS_GAP_PREFIX``: the search failed after
    production's own retry and the name was judged without news. Per line,
    so a name searched twice in a day counts twice; and per day.
    """
    searched = [e for e in entries
                if e.headline_count is not None and not (e.stage == "context" and not e.headline_count)]
    by_day: dict[str, list[int]] = {}
    failed_names: set[str] = set()
    for e in searched:
        day = e.timestamp.date().isoformat() if e.timestamp is not None else "unknown"
        counts = by_day.setdefault(day, [0, 0])
        counts[1] += 1
        if any(g.startswith(NEWS_GAP_PREFIX) for g in e.gaps):
            counts[0] += 1
            failed_names.add(e.ticker)
    return {"lines": len(searched), "failed": sum(c[0] for c in by_day.values()),
            "names": sorted(failed_names), "by_day": dict(sorted(by_day.items()))}


def news_fetches_line(fetches: Optional[dict[str, Any]]) -> Optional[str]:
    """The week's failed news fetches in one line, with each day's count. None when nothing searched."""
    if not isinstance(fetches, dict) or not fetches.get("lines"):
        return None
    days = fetches.get("by_day") or {}
    each = ", ".join(f"{failed}" for failed, _ in days.values())
    return (f"production news fetches that failed: {fetches['failed']} of {fetches['lines']} lines"
            + (f" (by day: {each})" if days else ""))


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
        "news": no_headlines(entries),
        "news_fetches": news_fetches(entries),
    }


def band(previous: Sequence[Optional[float]]) -> Optional[dict[str, float]]:
    """The owner's band from every week before that has the number; None with fewer than ``MIN_WEEKS``."""
    known = [float(v) for v in previous if v is not None]
    if len(known) < MIN_WEEKS:
        return None
    mean = statistics.fmean(known)
    sd = statistics.stdev(known)
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
    """Add each complete week's bands, outside marks and alerts, in place, from the weeks before it."""
    for i, week in enumerate(weeks):
        previous = weeks[:i]
        week["bands"], week["outside"], week["alerts"] = {}, {}, []
        if not week["complete"]:
            continue
        for key, words in BANDED:
            limits = band([w["values"].get(key) for w in previous])
            value = week["values"].get(key)
            week["bands"][key] = limits
            week["outside"][key] = _outside(value, limits)
            run = [week] + list(reversed(previous))[:IN_A_ROW - 1]
            if len(run) == IN_A_ROW and all(w.get("outside", {}).get(key) for w in run):
                week["alerts"].append(
                    f"{words}: {value:g} is outside its band {limits['low']:g} to {limits['high']:g}, "
                    f"{IN_A_ROW} weeks in a row"
                )


def setting_changes(entries: Sequence[JournalEntry], today: date) -> list[str]:
    """Today's settings against the last cycle day before today (from ``START``); empty if none changed."""
    by_day: dict[date, list[JournalEntry]] = {}
    for entry in entries:
        day = _utc_day(entry)
        if day is not None and START <= day <= today:
            by_day.setdefault(day, []).append(entry)
    if today not in by_day:
        return []
    now = _names(by_day[today])
    earlier = [day for day in by_day if day < today]
    before = _names(by_day[max(earlier)]) if earlier else {}
    out = []
    for key, words in NAMES:
        values, old = now.get(key) or [], before.get(key) or []
        if len(values) > 1:
            out.append(f"{words}: {', '.join(values)} on the same day")
        elif values and old and values != old:
            out.append(f"{words} changed: {', '.join(old)} -> {', '.join(values)}")
    return out


def build(entries: Iterable[JournalEntry], today: date) -> dict[str, Any]:
    """The whole record: every week from ``START`` to today's, judged, and the day to say it."""
    entries = list(entries)
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
    changes = setting_changes(entries, today)
    return {
        "kind": "drift",
        "made_on": today.isoformat(),
        "start": START.isoformat(),
        "rule": (f"a number alerts when it is outside the mean +/- {BAND_SDS:g} sample standard "
                 f"deviations of every week before, {IN_A_ROW} weeks in a row (no band until "
                 f"{MIN_WEEKS} weeks have it); a setting alerts on any change, the same day"),
        "judged_week": last_complete["week"] if last_complete else None,
        "alerts": alerts,
        "alert_on": alert_on,
        "setting_alerts": changes,
        "setting_alert_on": today.isoformat() if changes else None,
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
        banded = key in dict(BANDED)
        where = (f" (band {limits['low']:g} to {limits['high']:g})" if limits
                 else " (no band yet)" if week["complete"] and banded else "")
        out.append(f"- {words}: {shown}{where}")
    groups = ", ".join(f"{label} {n}" for label, n in week["conviction_groups"].items())
    out.append(f"- conviction groups: {groups}")
    starters = Counter(s["source"] for s in week["starts"])
    if starters:
        out.append("- started by: " + ", ".join(f"{s} {n}" for s, n in sorted(starters.items())))
    for key, words in NAMES:
        names = week["names"].get(key) or ["none recorded"]
        out.append(f"- {words}: {', '.join(names)}")
    quiet = no_headlines_line(week.get("news"))
    if quiet:
        out.append(f"- {quiet}")
    fetches = news_fetches_line(week.get("news_fetches"))
    if fetches:
        out.append(f"- {fetches}")
    for alert in week.get("alerts") or []:
        out.append(f"- ALERT: {alert}")
    return out


def render(record: dict[str, Any], weeks: int = 2) -> str:
    """The latest ``weeks`` weeks as text, newest first."""
    out = [f"Drift report, made {record['made_on']}. Rule: {record['rule']}.", ""]
    for week in list(reversed(record["weeks"]))[:weeks]:
        out += render_week(week) + [""]
    return "\n".join(out).rstrip() + "\n"


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="The model's answers, week by week, against their history.")
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
