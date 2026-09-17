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
MAX_CHARS = 420


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
    closed = book.get("closed") or []
    recent = [p for p in closed if str(p.get("last_seen")) >= (today.isoformat()[:8] + "01")]
    if recent:
        lines.append("Closed: " + ", ".join(str(p.get("ticker")) for p in recent[:6]))
    naked = [p["ticker"] for p in (book.get("positions") or []) if not p.get("has_stop", True)]
    if naked:
        lines.append(f"No stop on record: {', '.join(naked[:8])}{' …' if len(naked) > 8 else ''}")
    alarms = book.get("alarms") or []
    extra = [a.get("title") for a in alarms[1:4]]
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
