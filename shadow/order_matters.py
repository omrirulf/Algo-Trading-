"""How often the buying order mattered: a report, nothing more.

Each cycle the engine works through the day's signals one at a time, in
watchlist order, each seeing the orders before it. When the book runs out of
room part-way -- cash, the gross cap, the sleeve budget, an exposure-group
cap, the stock-market limit, the position count -- the signals left are
refused, and which ones got in was decided by their place in the list, not
by their conviction. The owner asked (24 Sep 2026) how often that happens,
in the real paper account and in every simulated fund, and for each such
day: the date, which signals were skipped, their conviction, and whether a
skipped signal had a higher conviction than one that was bought.

Report only. Nothing here changes the order or anything else.

A refusal counts as "ran out of room" only when a portfolio limit bound it:
the engine's "no room under the X limit", its "no room for T under its N%
cap or the X limit" when the headroom left was smaller than the ticker's own
cap would have allowed (otherwise the ticker's own cap bound it, which no
order would change), the position count, and the broker's buying power.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from typing import Iterable, Optional, Sequence

from config import settings as cfg

#: The kinds of room a book can run out of, as the report names them.
GROUP, SLEEVE, GROSS, STOCK_MARKET, POSITIONS, CASH = (
    "exposure group", "sleeve budget", "gross exposure", "stock-market", "position count", "cash")

_NO_ROOM = re.compile(r"^no room under the (?P<limit>.+) limit$")
_NO_SHARE = re.compile(
    r"^no room for .+? under its (?P<cap>[\d.]+)% cap or the (?P<limit>.+?) limit: "
    r"equity (?P<equity>[\d.]+), price (?P<price>[\d.]+), existing exposure (?P<existing>[\d.]+), "
    r"headroom (?P<headroom>[\d.]+)")
_POSITIONS = re.compile(r"^already holding \d+ positions")
_CASH = re.compile(r"insufficient buying power|buying power", re.IGNORECASE)


def _limit_kind(limit: str) -> str:
    limit = limit.strip()
    if limit.endswith("group"):
        return GROUP
    if limit.startswith("sleeve"):
        return SLEEVE
    if limit.startswith("gross"):
        return GROSS
    if limit.startswith("stock-market"):
        return STOCK_MARKET
    return limit


def capacity_kind(reason: Optional[str]) -> Optional[str]:
    """The room the book ran out of, if a portfolio limit refused the signal; else None."""
    text = (reason or "").strip()
    match = _NO_ROOM.match(text)
    if match:
        return _limit_kind(match.group("limit"))
    match = _NO_SHARE.match(text)
    if match:
        own_room = float(match.group("equity")) * float(match.group("cap")) / 100.0 - float(match.group("existing"))
        # The portfolio limit bound it only if the ticker's own cap, alone,
        # would have bought at least one order's worth: otherwise its own cap
        # refused it and no order of the list would have changed that.
        if own_room >= float(match.group("price")) * cfg.MIN_ORDER_QTY and float(match.group("headroom")) < own_room:
            return _limit_kind(match.group("limit"))
        return None
    if _POSITIONS.match(text):
        return POSITIONS
    if _CASH.search(text):
        return CASH
    return None


@dataclass(frozen=True, slots=True)
class Event:
    """One dispatched signal and what became of it."""

    day: date
    ticker: str
    conviction: Optional[float]
    status: str                # ACCEPTED, REJECTED or ERROR
    reason: str
    #: The limit, when it is already known (a fund records it, not the reason).
    kind: Optional[str] = None


@dataclass(frozen=True)
class Skipped:
    ticker: str
    conviction: Optional[float]
    kind: str
    #: Tickers bought that day with a lower conviction than this one.
    outranks: tuple[str, ...]


@dataclass(frozen=True)
class OrderDay:
    day: date
    bought: tuple[tuple[str, Optional[float]], ...]
    skipped: tuple[Skipped, ...]


def order_days(events: Iterable[Event]) -> tuple[list[OrderDay], int]:
    """The days the book ran out of room before the end of the list, and how many cycle days there were."""
    by_day: dict[date, list[Event]] = defaultdict(list)
    for event in events:
        by_day[event.day].append(event)
    out = []
    for day, rows in sorted(by_day.items()):
        bought = tuple((e.ticker, e.conviction) for e in rows if e.status == "ACCEPTED")
        bought_names = {t for t, _ in bought}
        skipped = []
        for e in rows:
            # A ticker bought that day was not left out, whatever a second
            # dispatch of it the same day was told (a day with two cycles).
            if e.status == "ACCEPTED" or e.ticker in bought_names:
                continue
            kind = e.kind or capacity_kind(e.reason)
            if kind is None:
                continue
            lower = tuple(t for t, c in bought
                          if t != e.ticker and e.conviction is not None and c is not None and c < e.conviction)
            skipped.append(Skipped(e.ticker, e.conviction, kind, lower))
        if skipped:
            out.append(OrderDay(day, bought, tuple(skipped)))
    return out, len(by_day)


def summary(days: Sequence[OrderDay], cycle_days: int) -> dict:
    """The JSON the fund output and the dashboard read: a running count, and every day."""
    kinds = Counter(s.kind for d in days for s in d.skipped)
    return {
        "cycle_days": cycle_days,
        "days": len(days),
        "skipped": sum(len(d.skipped) for d in days),
        "outranked_days": sum(1 for d in days if any(s.outranks for s in d.skipped)),
        "by_kind": dict(sorted(kinds.items())),
        "list": [
            {
                "day": d.day.isoformat(),
                "bought": [{"ticker": t, "conviction": c} for t, c in d.bought],
                "skipped": [{"ticker": s.ticker, "conviction": s.conviction, "kind": s.kind,
                             "outranks": list(s.outranks)} for s in d.skipped],
            }
            for d in days
        ],
    }


def real_events(audit_lines: Iterable[str]) -> list[Event]:
    """The real paper account's dispatched signals, from its own audit log (read as text)."""
    from shadow.calibration import _audit_instant, ny_day

    out = []
    for raw in audit_lines:
        try:
            record = json.loads(raw)
        except (json.JSONDecodeError, TypeError):
            continue
        if not isinstance(record, dict) or (record.get("event") or record.get("message")) != "signal_processed":
            continue
        result = record.get("result") if isinstance(record.get("result"), dict) else {}
        signal = record.get("signal") if isinstance(record.get("signal"), dict) else {}
        at = _audit_instant(record.get("ts"))
        ticker = str(result.get("ticker") or signal.get("ticker") or "").strip().upper()
        if at is None or not ticker:
            continue
        conviction = signal.get("conviction")
        out.append(Event(ny_day(at), ticker, float(conviction) if isinstance(conviction, (int, float)) else None,
                         str(result.get("status") or ""), str(result.get("reason") or "")))
    return out


def real_summary(audit_lines: Iterable[str]) -> dict:
    days, cycles = order_days(real_events(audit_lines))
    return summary(days, cycles)


def fund_summary(fund) -> dict:
    """A simulated fund's own record of the same (``Fund.order_events``).

    A fund that keeps no detail (the thousand coin-flip funds) kept only the
    days it ran out of room: its summary is the count, with no list.
    """
    if fund.order_events is None:
        return {"cycle_days": fund.cycles_dispatched, "days": len(fund.order_days_seen), "skipped": None,
                "outranked_days": None, "by_kind": {}, "list": []}
    days, _ = order_days(fund.order_events)
    return summary(days, fund.cycles_dispatched)


__all__ = ["CASH", "Event", "GROSS", "GROUP", "OrderDay", "POSITIONS", "SLEEVE", "STOCK_MARKET", "Skipped",
           "capacity_kind", "fund_summary", "order_days", "real_events", "real_summary", "summary"]
