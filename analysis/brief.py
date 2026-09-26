"""The day in one phone notification.

    python -m analysis.brief                      # from logs/book.json
    python -m analysis.brief --book /tmp/b.json

Reads the book snapshot ``analysis/book.py`` writes after each cycle and
prints a message short enough for a phone's notification tray: the status in
the first line, then only what changed or what is wrong. A Routine in the
owner's Claude account runs this after the cycle and pushes the text.

Three rules keep it honest. The first line is the worst thing in the record:
a critical alarm beats a warning beats a clean day, and a day with no
snapshot for today is itself the headline. Nothing is invented: a missing
equity is "equity not recorded", not a number. And the last line ends with
the snapshot's day, so whoever reads the text later can tell whether it is
today's or yesterday's without opening the snapshot.

Since 26 Sep 2026 it also says how the day was started and kept: which
starter started today's run and how long after 14:40 UTC, a warning when
that was not the Supabase starter (the main one; anything else is a backup
that had to step in), what the Supabase starter's own request to GitHub got
back (the HTTP status code and nothing else: 204 is a request GitHub
accepted), and when the archive last took a push -- with a warning every
day it is not configured, because a free Supabase project nothing writes to
is paused, and the starter lives in it. All of it comes from the snapshot,
which read the journal's run block and the two records beside it.

Read-only. Two files at most, no broker, no model, no network.
"""

from __future__ import annotations

import argparse
import json
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Optional

# Deliberately no project import: this runs in a bare clone with nothing
# installed, so the only dependency is the standard library.
DEFAULT_BOOK = Path(__file__).resolve().parent.parent / "logs" / "book.json"

#: Notification trays cut long text; the first line must carry the verdict.
#: 420 until 26 Sep 2026, when the brief gained two or three short lines
#: about who started the day and the Supabase side of it; the tray still
#: shows the first line, and the expanded notification shows the rest.
MAX_CHARS = 600

#: The day's main starter, as the run block names it. Anything else that
#: started the run is a backup (``analysis/cycle_day.py:PRIMARY_SOURCE``).
PRIMARY_SOURCE = "supabase-cron"

#: The brief's two warnings about the machinery, word for word the titles
#: ``analysis/health.py`` gives the same alarms, so neither is said twice.
NOT_STARTED_BY_SUPABASE = "The Supabase starter did not start today's run; {source} did"
ARCHIVE_NOT_CONFIGURED = "Archive not configured: the Supabase project will pause"


def _money(value: Optional[float]) -> str:
    if value is None:
        return "n/a"
    sign = "-" if value < 0 else ""
    return f"{sign}${abs(value):,.0f}"


def _signed(value: Optional[float]) -> str:
    if value is None:
        return "n/a"
    return f"{'+' if value >= 0 else '-'}${abs(value):,.0f}"


def headline(book: dict, today: date) -> str:
    """The first line: the worst thing the record says, in a few words."""
    if str(book.get("day")) != today.isoformat():
        return f"⚠️ No snapshot for today yet (last: {book.get('day') or 'none'})"
    alarms = book.get("alarms") or []
    critical = [a for a in alarms if a.get("severity") == "critical"]
    warnings = [a for a in alarms if a.get("severity") == "warning"]
    if critical:
        return f"🔴 {critical[0].get('title')}"
    if warnings:
        return f"🟡 {len(warnings)} warning{'s' if len(warnings) != 1 else ''}: {warnings[0].get('title')}"
    return "🟢 Clean day"


def _clock(stamp: object) -> Optional[str]:
    """``HH:MM`` in UTC from an ISO timestamp, or None."""
    if not isinstance(stamp, str):
        return None
    try:
        moment = datetime.fromisoformat(stamp.strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=timezone.utc)
    return moment.astimezone(timezone.utc).strftime("%H:%M")


def started_line(run: object) -> Optional[str]:
    """``Started by supabase-cron at 14:41 UTC (1 min after 14:40)``, or None with no run block today."""
    if not isinstance(run, dict):
        return None
    source = run.get("source") if isinstance(run.get("source"), str) else "an unknown starter"
    at, planned = _clock(run.get("started_at")), _clock(run.get("scheduled_for"))
    late = run.get("minutes_late")
    text = f"Started by {source}"
    if at:
        text += f" at {at} UTC"
    if isinstance(late, int) and not isinstance(late, bool) and planned:
        text += (f" ({late} min after {planned})" if late >= 0 else f" ({-late} min before {planned})")
    return text


def supabase_line(book: dict, today: date) -> Optional[str]:
    """The Supabase starter's own request today, and the archive's last push, in one line.

    Only the starter's HTTP status code is shown (204 is a request GitHub
    accepted), never anything it sent or got back. None when the snapshot
    has neither record.
    """
    starter, archive = book.get("starter"), book.get("archive")
    if not isinstance(starter, dict) and not isinstance(archive, dict):
        return None
    if not isinstance(starter, dict):
        first = "starter: no record"
    elif str(starter.get("day")) != today.isoformat():
        first = "starter: no record for today"
    elif starter.get("status") == "unknown":
        why = str(starter.get("why") or "no reason given").split(":")[0][:40]
        first = f"starter: unknown ({why})"
    elif isinstance(starter.get("status_code"), int) and not isinstance(starter.get("status_code"), bool):
        at = _clock(starter.get("requested_at"))
        first = f"starter HTTP {starter['status_code']}" + (f" at {at} UTC" if at else "")
    else:
        first = "starter: no answer from GitHub" + (" yet" if not starter.get("error") else "")
    if not isinstance(archive, dict):
        second = "archive: no push recorded"
    else:
        last = archive.get("last_success")
        last = last[:10] if isinstance(last, str) and last else None
        if archive.get("ok") is True:
            second = f"archive pushed {last}" if last else "archive pushed"
        elif archive.get("error") == "not configured":
            second = "archive not configured"
        else:
            second = f"archive push failed ({archive.get('error') or 'no reason'}), last worked {last or 'never'}"
    return f"Supabase: {first} · {second}"


def compose(book: dict, today: Optional[date] = None) -> str:
    today = today or datetime.now(timezone.utc).date()
    lines = [headline(book, today)]
    e = book.get("exposure") or {}
    c = book.get("cycle") or {}
    equity = book.get("equity")
    lines.append(
        f"Equity {_money(equity) if equity else 'not recorded'} · "
        f"{e.get('positions', 0)} positions · {_money(e.get('gross'))} gross · "
        f"{_money(e.get('at_risk'))} at risk · unrealised {_signed(e.get('unrealised'))}"
    )
    traded = c.get("accepted") or []
    directional = c.get("directional") or []
    if traded:
        lines.append("Traded: " + ", ".join(traded))
    elif directional:
        lines.append(f"{len(directional)} directional call{'s' if len(directional) != 1 else ''}, none traded")
    else:
        lines.append("No directional call today")
    # How the day was started and kept (26 Sep 2026). The two warnings are
    # the health check's own alarm titles: each is said once, here, and left
    # out of "Also" below -- unless it is already the headline.
    said: set[str] = set()
    run = book.get("run")
    started = started_line(run)
    if started:
        lines.append(started)
        source = run.get("source")
        if source is not None and source != PRIMARY_SOURCE:
            said.add(NOT_STARTED_BY_SUPABASE.format(source=source))
    supabase = supabase_line(book, today)
    if supabase:
        lines.append(supabase)
    if isinstance(book.get("archive"), dict) and book["archive"].get("error") == "not configured":
        said.add(ARCHIVE_NOT_CONFIGURED)
    for title in sorted(said):
        if title not in lines[0]:
            lines.append(f"⚠️ {title}")
    closed = book.get("closed") or []
    recent = [p for p in closed if str(p.get("last_seen")) >= (today.isoformat()[:8] + "01")]
    if recent:
        lines.append("Closed: " + ", ".join(str(p.get("ticker")) for p in recent[:6]))
    naked = [p["ticker"] for p in (book.get("positions") or []) if not p.get("has_stop", True)]
    if naked:
        lines.append(f"No stop on record: {', '.join(naked[:8])}{' …' if len(naked) > 8 else ''}")
    alarms = book.get("alarms") or []
    extra = [a.get("title") for a in alarms[1:] if a.get("title") not in said][:3]
    if extra:
        lines.append("Also: " + "; ".join(str(t) for t in extra))
    cost = c.get("cost_usd")
    stamp = str(book.get("day") or "undated")
    if isinstance(cost, (int, float)):
        tail = f"Cycle {c.get('tickers', 0)} tickers, ${cost:.2f} · {stamp}"
    else:
        tail = f"Snapshot {stamp}"
    # The last line always ends with the snapshot's day, and survives the
    # cut: a reader that only has this text can tell today's from stale.
    body = "\n".join(lines)
    budget = MAX_CHARS - len(tail) - 1
    if len(body) > budget:
        body = body[: budget - 1].rstrip() + "…"
    return body + "\n" + tail


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="The day in one notification.")
    parser.add_argument("--book", type=Path, default=DEFAULT_BOOK)
    parser.add_argument("--day", default=None, help="ISO date, default today in UTC")
    args = parser.parse_args(argv)
    try:
        book = json.loads(args.book.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"⚠️ No readable snapshot at {args.book} ({type(exc).__name__})")
        return 1
    today = date.fromisoformat(args.day) if args.day else None
    print(compose(book, today))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
