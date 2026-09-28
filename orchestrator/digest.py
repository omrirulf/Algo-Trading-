"""The weekly risk digest for the names the paper account holds: flags, each with a link.

The owner's request (27 Sep 2026), made smaller by the owner on 28 Sep
2026: once a week, with the weekly report, two things only, both found by
code, with no model call and so no cost:

* **Earnings dates.** Each held company's next earnings date, the one the
  cycle already read (yfinance's calendar, on the name's latest journal
  line), listed when it falls in the next ``EARNINGS_DAYS`` days.
* **Operational events.** A headline the cycle already fetched for a held
  name this week (``context.sources`` in the journal; no new search) whose
  title or snippet names a fund closing or liquidating, a delisting, a
  ticker or name change, a share split, or a merger or buy-out. These can
  break an order or a stop-loss, so they are worth a look. The match is a
  fixed list of words (``EVENTS``): a flag says which words it found and
  links the headline; a headline that says the same thing in other words
  is missed, and one that uses the words in passing is flagged anyway.

Flags only: nothing here trades, changes a rule or calculates a number, and
nothing that trades reads it (CI: only the heartbeat's ``--weekly-digest``
mode imports it, and that mode builds no dispatcher). Headlines are
untrusted text: only their title, source and link are copied, cleaned of
control characters, and never followed.
"""

from __future__ import annotations

import json
import re
from datetime import date, timedelta
from typing import Any, Iterable, Optional

from config.instruments import is_fund

#: How far ahead an earnings date is listed: this week and the next.
EARNINGS_DAYS = 14
#: The week of headlines read: the seven days up to and including today.
NEWS_DAYS = 7
#: At most this many headlines per held name (the newest), and in all.
PER_NAME = 15
MAX_ITEMS = 300
#: At most this many flags are kept.
MAX_FLAGS = 25

#: The operational events, in the order they are tried: a headline gets the
#: first that matches. Words, not judgement: see the module's docstring.
EVENTS: tuple[tuple[str, "re.Pattern[str]"], ...] = (
    ("closure", re.compile(
        r"\b(liquidat(?:e|es|ed|ing|ion)|delist(?:s|ed|ing)?|wind(?:s|ing)? down|"
        r"(?:fund|etf|etn)s? (?:to|will) (?:close|shut)|"
        r"(?:clos(?:e|es|ing|ure)|shut(?:s|ting)? down) (?:of )?(?:the |its |this )?(?:fund|etf|etn)s?)\b",
        re.IGNORECASE)),
    ("ticker_or_name_change", re.compile(
        r"\b(ticker (?:symbol )?change|new ticker|renam(?:e|es|ed|ing)|"
        r"chang(?:e|es|ed|ing) (?:its |the )?(?:ticker|name))\b", re.IGNORECASE)),
    ("split", re.compile(r"\b(reverse split|stock split|share split|\d+-for-\d+ (?:reverse )?split)\b",
                         re.IGNORECASE)),
    ("merger", re.compile(
        r"\b(merg(?:e|es|ed|ing|er) (?:into|with)|(?:to be|being|agrees to be) (?:acquired|bought)|"
        r"take-?private|taken private)\b", re.IGNORECASE)),
)
KINDS = tuple(kind for kind, _ in EVENTS)

_TICKER = re.compile(r"[A-Z][A-Z0-9.\-]{0,9}")
_URL = re.compile(r"https://[^\s\"'<>]{1,490}")
_CONTROL = re.compile(r"[\x00-\x1f\x7f]")


def week_of(day: date) -> str:
    year, week, _ = day.isocalendar()
    return f"{year}-W{week:02d}"


def _clean(value: Any, limit: int) -> str:
    text = _CONTROL.sub(" ", value if isinstance(value, str) else "")
    text = " ".join(text.split())
    return text[:limit]


def held_names(account_lines: Iterable[str]) -> dict[str, str]:
    """``{ticker: "long" | "short"}`` from the account's last snapshot; empty without one."""
    last: Optional[dict[str, Any]] = None
    for raw in account_lines:
        try:
            snapshot = json.loads(raw)
        except ValueError:
            continue
        if isinstance(snapshot, dict) and isinstance(snapshot.get("positions"), list):
            if last is None or str(snapshot.get("at") or "") >= str(last.get("at") or ""):
                last = snapshot
    names: dict[str, str] = {}
    for p in (last or {}).get("positions") or []:
        ticker, qty = p.get("ticker"), p.get("qty")
        if isinstance(ticker, str) and _TICKER.fullmatch(ticker) and isinstance(qty, (int, float)) and qty:
            names[ticker] = "short" if qty < 0 else "long"
    return dict(sorted(names.items()))


def _yahoo(ticker: str) -> str:
    return ticker.replace(".", "-")


def gather(journal_lines: Iterable[str], held: dict[str, str], today: date) -> dict[str, Any]:
    """The week's facts for the held names, from the journal: earnings dates and headlines.

    Pure: no network, no clock but ``today``.
    """
    since = (today - timedelta(days=NEWS_DAYS - 1)).isoformat()
    until = today.isoformat()
    earnings: dict[str, tuple[str, str]] = {}      # ticker -> (line time, date)
    items: dict[str, dict[str, Any]] = {}          # url -> item
    for raw in journal_lines:
        start = raw.find("{")
        if start < 0:
            continue
        try:
            line = json.loads(raw[start:])
        except ValueError:
            continue
        ticker = line.get("ticker") if isinstance(line, dict) else None
        stamp = str(line.get("ts_utc") or "") if isinstance(line, dict) else ""
        if ticker not in held or not (since <= stamp[:10] <= until):
            continue
        context = line.get("context") if isinstance(line.get("context"), dict) else {}
        fundamentals = context.get("fundamentals") if isinstance(context.get("fundamentals"), dict) else {}
        when = fundamentals.get("next_earnings_date")
        if isinstance(when, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", when):
            if ticker not in earnings or stamp >= earnings[ticker][0]:
                earnings[ticker] = (stamp, when)
        for source in context.get("sources") or []:
            if not isinstance(source, dict):
                continue
            url = source.get("url")
            if not isinstance(url, str) or not _URL.fullmatch(url.strip()):
                continue
            url = url.strip()
            title = _clean(source.get("title"), 200)
            if not title:
                continue
            seen = items.get(url)
            if seen is None or stamp < seen["seen"]:
                items[url] = {"ticker": ticker, "seen": stamp, "title": title,
                              "snippet": _clean(source.get("snippet"), 300),
                              "source": _clean(source.get("source"), 60), "link": url}

    upcoming = []
    for ticker, (_, when) in sorted(earnings.items()):
        if is_fund(ticker):
            continue
        day = date.fromisoformat(when)
        if today <= day <= today + timedelta(days=EARNINGS_DAYS):
            upcoming.append({"ticker": ticker, "date": when, "days_away": (day - today).days,
                             "link": f"https://finance.yahoo.com/calendar/earnings?symbol={_yahoo(ticker)}"})
    upcoming.sort(key=lambda e: (e["date"], e["ticker"]))

    chosen: list[dict[str, Any]] = []
    for ticker in held:
        mine = sorted((i for i in items.values() if i["ticker"] == ticker), key=lambda i: i["seen"], reverse=True)
        chosen += mine[:PER_NAME]
    chosen = sorted(chosen, key=lambda i: (i["ticker"], i["seen"], i["link"]))[:MAX_ITEMS]
    for number, item in enumerate(chosen, start=1):
        item["id"] = f"H{number}"
    return {"earnings": upcoming, "items": chosen}


def flag(items: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """The headlines that name an operational event, one flag each, with the words found."""
    flags: list[dict[str, Any]] = []
    for item in items:
        text = f"{item['title']} {item['snippet']}"
        for kind, pattern in EVENTS:
            found = pattern.search(text)
            if found:
                flags.append({"ticker": item["ticker"], "kind": kind,
                              "note": f"headline mentions \"{found.group(0).lower()}\"",
                              "title": item["title"], "source": item["source"],
                              "seen": item["seen"][:10], "link": item["link"]})
                break
    return flags[:MAX_FLAGS]


def run(*, today: date, account_lines: Iterable[str], journal_lines: Iterable[str]) -> dict[str, Any]:
    """One week's digest, as a record. Code only: no model call, no cost."""
    held = held_names(account_lines)
    facts = gather(journal_lines, held, today)
    record: dict[str, Any] = {
        "kind": "risk-digest", "week": week_of(today), "made_on": today.isoformat(),
        "held": held, "earnings": facts["earnings"], "headlines_read": len(facts["items"]),
        "flags": flag(facts["items"]), "cost_usd": 0.0,
    }
    record["status"] = "no held names" if not held else "ok"
    return record
