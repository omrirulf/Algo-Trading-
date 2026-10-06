"""The owner's weekly report: drift, the risk digest and, when new, the concentration report.

    python -m analysis.weekly --week 2026-W40 --markdown     # the full report
    python -m analysis.weekly --week 2026-W40 --phone --url URL

Made on the first cycle day of each week, after the daily brief, and sent to
the phone as its own notification (27 Sep 2026). It only joins what three
other programs wrote, all committed beside the journal:

* ``logs/drift.json`` (``analysis/drift.py``): the model's answers last week
  against their normal bands. An alert from it also heads that day's brief,
  through the health check; here it is shown in full.
* ``logs/digest/<week>.json`` (``orchestrator/digest.py``): the risk digest
  for the held names, the one model call of the week.
* ``logs/concentration.json`` (``analysis/concentration.py``): the monthly
  concentration report, shown in the first weekly report after it is made.

The phone text is cut to fit one notification (``PHONE_BYTES``); the full
report is the Markdown file the notification links to. Read-only: it reads
three files and prints.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis import concentration, drift  # noqa: E402

LOGS = Path(__file__).resolve().parent.parent / "logs"

#: ntfy takes 4,096 bytes of message; the rest goes in the linked report.
PHONE_BYTES = 3800


def _read(path: Path) -> Optional[dict[str, Any]]:
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return record if isinstance(record, dict) else None


def monday_of_week(week: str) -> date:
    year, number = week.split("-W")
    return date.fromisocalendar(int(year), int(number), 1)


def judged(drift_record: Optional[dict[str, Any]], week: str) -> Optional[dict[str, Any]]:
    """The last complete week before ``week`` in the drift record, or None."""
    if not drift_record:
        return None
    monday = monday_of_week(week).isoformat()
    weeks = [w for w in drift_record.get("weeks") or [] if w.get("complete") and w.get("monday") < monday]
    return weeks[-1] if weeks else None


def new_concentration(record: Optional[dict[str, Any]], week: str) -> Optional[dict[str, Any]]:
    """The latest monthly report, if it was made in the 7 days before this week's Monday or since."""
    if not record or not isinstance(record.get("months"), dict) or not record.get("latest"):
        return None
    month = record["months"].get(record["latest"])
    made = month.get("made_on") if isinstance(month, dict) else None
    if not isinstance(made, str):
        return None
    return month if made >= (monday_of_week(week) - timedelta(days=7)).isoformat() else None


def drift_lines(week: Optional[dict[str, Any]]) -> list[str]:
    """Last week's numbers in three lines: the verdict, the numbers, the names."""
    if week is None:
        return ["Drift: no complete week recorded yet."]
    alerts = week.get("alerts") or []
    bands = [b for b in (week.get("bands") or {}).values() if b]
    if alerts:
        head = f"Drift, week of {week['monday']}: {len(alerts)} outside the normal band:"
    elif bands:
        head = f"Drift, week of {week['monday']}: every number inside its band."
    else:
        head = f"Drift, week of {week['monday']}: no bands yet (4 weeks of data needed)."
    v = week.get("values") or {}

    def show(key: str, unit: str = "") -> str:
        value = v.get(key)
        return "n/a" if value is None else f"{value:g}{unit}"

    numbers = (f"NEUTRAL {show('neutral_pct', '%')} · conviction {show('conviction_mean')} "
               f"({show('at_floor_pct', '%')} at floor) · agrees with momentum {show('agreement_pct', '%')} · "
               f"long {show('long_pct', '%')} · errors setup {show('setup_error_pct', '%')}, "
               f"model {show('model_error_pct', '%')} · start {show('minutes_late_mean')} min late · "
               f"Supabase start {show('primary_start_pct', '%')}")
    names = week.get("names") or {}
    who = (f"{'/'.join(names.get('model') or ['?'])} @ {'/'.join(names.get('provider') or ['?'])}, "
           f"{'/'.join(names.get('reasoning_effort') or ['?'])}, screening "
           f"{'/'.join(names.get('screening') or ['?'])}, prompt {'/'.join(names.get('prompt') or ['?'])}")
    quiet = drift.no_headlines_line(week.get("news"), limit=drift.PHONE_NAMES)
    fetches = drift.news_fetches_line(week.get("news_fetches"))
    return ([head] + [f"- {a}" for a in alerts] + [numbers, who]
            + [line[0].upper() + line[1:] for line in (quiet, fetches) if line])


def digest_lines(record: Optional[dict[str, Any]], limit: int = 25) -> list[str]:
    """The digest as plain lines, links in full (a phone makes them clickable)."""
    if record is None:
        return ["Risk digest: not made this week."]
    out = [f"Risk digest for {len(record.get('held') or {})} held names ({record.get('status')}):"]
    for e in record.get("earnings") or []:
        out.append(f"- {e['ticker']} earnings {e['date']} (in {e['days_away']} days) {e['link']}")
    for f in (record.get("flags") or [])[:limit]:
        out.append(f"- {f['ticker']} [{f['kind'].replace('_', ' ')}] {f['note']} {f['link']}")
    if not record.get("earnings") and not record.get("flags"):
        out.append("- nothing flagged")
    return out


def phone(week: str, url: str, logs: Path = LOGS) -> str:
    """The notification: title line, then the body, cut to fit, ending with the link."""
    d = judged(_read(logs / "drift.json"), week)
    dig = _read(logs / "digest" / f"{week}.json")
    conc = new_concentration(_read(logs / "concentration.json"), week)
    title = f"Weekly report {week}"
    if d and d.get("alerts"):
        title += f": {len(d['alerts'])} drift alert(s)"
    body = drift_lines(d) + [""] + digest_lines(dig)
    if conc:
        body += [""] + concentration.render(conc).rstrip("\n").split("\n")
    tail = f"Full report: {url}"
    text = "\n".join(body)
    budget = PHONE_BYTES - len(title.encode()) - len(tail.encode()) - 4
    if len(text.encode()) > budget:
        text = text.encode()[: budget - 4].decode("utf-8", "ignore").rsplit("\n", 1)[0] + "\n…"
    return f"{title}\n{text}\n{tail}"


def markdown(week: str, logs: Path = LOGS) -> str:
    """The whole report, for the file the notification links to."""
    drift_record = _read(logs / "drift.json")
    dig = _read(logs / "digest" / f"{week}.json")
    conc = new_concentration(_read(logs / "concentration.json"), week)
    out = [f"# Weekly report {week}", "",
           "Made on the week's first cycle day, after the daily brief. Nothing here trades "
           "or changes a rule: it is for reading.", "", "## Drift", ""]
    d = judged(drift_record, week)
    if d is None:
        out.append("No complete week recorded yet.")
    else:
        out.append(f"Rule: {drift_record.get('rule')}.")
        out.append("")
        out += drift.render_week(d)
    out += ["", "## Risk digest for the held names", ""]
    if dig is None:
        out.append("Not made this week.")
    else:
        out.append(f"Status: {dig.get('status')}. Headlines read: {dig.get('headlines_read', 0)}. "
                   f"Cost: ${dig.get('cost_usd') or 0:.4f} (cap ${dig.get('cap_usd', 1):.2f} a week). "
                   f"Flags dropped for naming no headline given: {dig.get('dropped', 0)}.")
        out.append("")
        for e in dig.get("earnings") or []:
            out.append(f"- **{e['ticker']}** earnings on {e['date']} (in {e['days_away']} days): {e['link']}")
        for f in dig.get("flags") or []:
            out.append(f"- **{f['ticker']}** ({f['kind'].replace('_', ' ')}): {f['note']} "
                       f"Source: {f['source'] or 'unknown'}, seen {f['seen']}: [{f['title']}]({f['link']})")
        if not dig.get("earnings") and not dig.get("flags"):
            out.append("Nothing flagged.")
    if conc:
        # The month in the heading: the section is last month's, which the
        # render's own first line says and the lines below it do not.
        out += ["", f"## Concentration for {conc.get('month')} (as of {conc.get('as_of')}; "
                    "monthly, descriptive only)", ""]
        out += concentration.render(conc).rstrip("\n").split("\n")[1:]
        rows = ((conc.get("book") or {}).get("beta_to_vt") or {}).get("by_position") or []
        if rows:
            out += ["", "| Position | Side | Weight | Beta to VT |", "| --- | --- | --- | --- |"]
            out += [f"| {r['ticker']} | {r['side']} | {r['weight_pct']}% | "
                    f"{'n/a' if r['beta'] is None else r['beta']} |" for r in rows]
    return "\n".join(out) + "\n"


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="The owner's weekly report.")
    parser.add_argument("--week", default=None, help="ISO week, e.g. 2026-W40; default this week (UTC)")
    parser.add_argument("--logs", type=Path, default=LOGS)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--markdown", action="store_true")
    mode.add_argument("--phone", action="store_true")
    parser.add_argument("--url", default="", help="the full report's address, for the phone text")
    args = parser.parse_args(argv)
    week = args.week or drift.week_label(drift.monday_of(datetime.now(timezone.utc).date()))
    print(markdown(week, args.logs) if args.markdown else phone(week, args.url, args.logs), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
