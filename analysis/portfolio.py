#!/usr/bin/env python3
"""The book as it stands, reconstructed from the execution audit log.

    python -m analysis.portfolio            # the book, as a table
    python -m analysis.portfolio --json     # the same, machine-readable

The daily report answers "what did the model think about 78 names". It does
not answer "what do I hold", and those are different questions: the first is
about signals, the second about state. ``analysis/cycle_report.py`` renders an
*event* view -- the ladder actions a cycle took -- which is empty on any day
nothing happened to a position. This is the *state* view, and it is never
empty while the book is not.

Reconstructed rather than fetched
---------------------------------
The broker knows the book authoritatively, and asking it would need a
credential. The audit log already records every ACCEPTED entry, and
``app.position_manager`` already records every rung taken against it, so the
book is derivable from the record this system keeps of its own decisions --
offline, with no key, and identically in a test.

That has one consequence worth stating plainly rather than hiding: this is the
book *as recorded*, not as the broker holds it. A stop filled overnight closes
a position at the broker and leaves no line here until the next cycle notices.
So a position is reported with the age of the record behind it, and the
dashboard says when it was last confirmed.

What is deliberately absent
---------------------------
**No current price, so no unrealised P&L.** The record carries the entry, the
stop and the ATR the decision was made against; it carries no mark. Inventing
one from a stale entry would make a number that reads like P&L and is not, so
the mark is an *input*: pass ``prices`` and every position gains its current
standing, omit it and the book still reports everything that does not need a
quote.

**No account equity, so no cap percentages by default.** The risk engine sizes
against equity and the audit record does not keep it, so "was this inside the
5% cap" cannot be answered from the record alone. ``equity`` is an input for
the same reason ``prices`` is, and where it is absent the exposure section
reports dollars and says the denominator is missing rather than guessing one.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import settings as cfg  # noqa: E402
from config.instruments import (  # noqa: E402
    InstrumentKind,
    group_for,
    kind_for,
    name_for,
    sleeve_label,
)

#: The audit events this reads. ``signal_processed`` opens a position;
#: ``position_managed`` is how ``app.position_manager`` records a rung.
ENTRY_EVENT = "signal_processed"
MANAGED_EVENT = "position_managed"

#: Actions that close part of a position or move its stop. Kept in step with
#: ``app.position_manager._RUNG_COMPLETING`` by a test rather than by memory.
TRANCHE = "tranche_taken"
STOP_RAISED = "stop_raised"
HELD = "held"
UNMANAGED = "unmanaged"

#: Actions taken after the manager actually looked up a price. The ones left
#: out matter more than the ones in: an ``unmanaged`` pass gives up before
#: fetching a quote and records ``price: 0.0`` as a placeholder, and a zero
#: read as a mark values a short at its full entry -- an invented gain the
#: size of the position. A mark is taken only from a pass that made one.
MARKING_ACTIONS = frozenset({TRANCHE, STOP_RAISED, HELD})

#: Rungs on the ladder, in order, as ``app.position_manager`` applies them.
LADDER_RUNGS = (1.0, 3.0)

#: Where a mark's price came from. The distinction is the whole point: a
#: live quote is now, a recorded one is as of the last management pass, and
#: presenting the second as the first is the lie this module exists to avoid.
LIVE = "live"
RECORDED = "recorded"


def _num(value: Any) -> Optional[float]:
    """A float, or None for anything that is not a real number.

    ``bool`` is excluded deliberately: it is an ``int`` in Python, and a
    ``True`` quantity silently becoming ``1`` share is the kind of quiet
    nonsense this whole module exists to avoid.
    """
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


@dataclass(frozen=True)
class Position:
    """One open position, as the record describes it."""

    ticker: str
    side: str
    quantity: int
    entry_price: float
    stop_price: float
    atr: Optional[float] = None
    opened: Optional[str] = None
    order_id: Optional[str] = None
    #: Rungs of the profit ladder already taken, from the audit record.
    rungs_taken: int = 0
    #: The stop as last moved, when a rung or a trail has moved it.
    current_stop: Optional[float] = None
    #: When the manager last looked at this position, whatever it decided.
    last_managed: Optional[str] = None
    #: What it decided on that pass.
    last_action: Optional[str] = None
    #: The price the manager saw, from the last pass that actually looked one
    #: up. Not a live quote -- a mark the record kept, which is the only kind
    #: this module will report.
    last_price: Optional[float] = None
    #: When that price was observed. Distinct from ``last_managed``, because
    #: the manager can look at a position without marking it.
    last_marked: Optional[str] = None
    #: The gain in R the manager computed on that pass, kept as a cross-check
    #: on this module's own arithmetic rather than as the number displayed.
    last_gain_r: Optional[float] = None

    # -- identity ---------------------------------------------------------

    @property
    def name(self) -> str:
        return name_for(self.ticker)

    @property
    def sleeve(self) -> str:
        return sleeve_label(self.ticker)

    @property
    def group(self) -> str:
        return group_for(self.ticker)

    @property
    def kind(self) -> InstrumentKind:
        return kind_for(self.ticker)

    @property
    def is_long(self) -> bool:
        return self.side.lower() == "buy"

    @property
    def direction(self) -> str:
        return "Long" if self.is_long else "Short"

    # -- what it is worth and what it risks -------------------------------

    @property
    def stop(self) -> float:
        """The stop in force: the ladder's if it moved one, else the entry's."""
        return self.current_stop if self.current_stop is not None else self.stop_price

    @property
    def notional(self) -> float:
        """Exposure at entry. Absolute, so a short counts as exposure taken."""
        return abs(self.quantity * self.entry_price)

    @property
    def risk_dollars(self) -> float:
        """What is lost if the stop fills, from the stop in force.

        Negative when the stop has been walked past the entry -- a locked-in
        gain rather than a risk -- and reported as such rather than clamped to
        zero, because "this position can no longer lose" is the thing the
        ladder exists to produce and the number worth seeing.
        """
        per_share = (
            self.entry_price - self.stop if self.is_long else self.stop - self.entry_price
        )
        return per_share * self.quantity

    @property
    def initial_risk_dollars(self) -> float:
        """One R: what the position risked at entry, before any rung."""
        per_share = (
            self.entry_price - self.stop_price
            if self.is_long
            else self.stop_price - self.entry_price
        )
        return per_share * self.quantity

    @property
    def stop_distance_pct(self) -> Optional[float]:
        """How far the stop sits from entry, as a percent of entry."""
        if not self.entry_price:
            return None
        return abs(self.entry_price - self.stop) / self.entry_price * 100.0

    @property
    def protected(self) -> bool:
        """True once the stop can no longer give back the entry price."""
        return self.risk_dollars <= 0

    # -- what needs a quote -----------------------------------------------

    def mark(
        self, price: Optional[float], source: str = LIVE, as_of: Optional[str] = None
    ) -> "Mark":
        """This position's standing at ``price``, or an empty standing."""
        if price is None or not self.entry_price:
            return Mark()
        move = (price - self.entry_price) if self.is_long else (self.entry_price - price)
        one_r = self.initial_risk_dollars / self.quantity if self.quantity else 0.0
        return Mark(
            price=price,
            unrealised=move * self.quantity,
            pct=move / self.entry_price * 100.0,
            r_multiple=(move / one_r) if one_r else None,
            source=source,
            as_of=as_of,
        )

    def recorded_mark(self) -> "Mark":
        """The standing at the last price the manager wrote down, if any."""
        return self.mark(self.last_price, RECORDED, self.last_marked)

    @property
    def unmanaged(self) -> bool:
        """The manager last found no live stop order to work with.

        Worth surfacing rather than burying: the stop is this system's only
        exit, so a position the manager cannot reach is one nothing is
        protecting.
        """
        return self.last_action == UNMANAGED

    def as_dict(self) -> dict[str, Any]:
        return {
            "ticker": self.ticker,
            "name": self.name,
            "sleeve": self.sleeve,
            "group": self.group,
            "direction": self.direction,
            "quantity": self.quantity,
            "entry_price": self.entry_price,
            "initial_stop": self.stop_price,
            "stop": self.stop,
            "atr": self.atr,
            "opened": self.opened,
            "rungs_taken": self.rungs_taken,
            "rungs_total": len(LADDER_RUNGS),
            "notional": self.notional,
            "risk_dollars": self.risk_dollars,
            "initial_risk_dollars": self.initial_risk_dollars,
            "stop_distance_pct": self.stop_distance_pct,
            "protected": self.protected,
            "last_managed": self.last_managed,
            "last_action": self.last_action,
            "last_price": self.last_price,
            "last_gain_r": self.last_gain_r,
            "last_marked": self.last_marked,
            "unmanaged": self.unmanaged,
        }


@dataclass(frozen=True)
class Mark:
    """A position's standing against a price, and where that price came from."""

    price: Optional[float] = None
    unrealised: Optional[float] = None
    pct: Optional[float] = None
    r_multiple: Optional[float] = None
    source: str = ""
    #: When the price was observed. ``None`` for a supplied live quote.
    as_of: Optional[str] = None

    @property
    def known(self) -> bool:
        return self.price is not None

    @property
    def is_live(self) -> bool:
        return self.source == LIVE


@dataclass(frozen=True)
class Exposure:
    """One bucket of exposure, and the cap it is measured against.

    Two different percentages live here, and conflating them would be the
    easiest way to make this page lie. ``share_of_book`` is exact and always
    available -- it needs only the positions. ``used_pct`` is the one the caps
    are written in, and it needs equity, which the record does not keep. Where
    equity is absent the first is still reported and the second is ``None``.
    """

    label: str
    notional: float
    cap_pct: Optional[float] = None
    equity: Optional[float] = None
    #: Total book notional, so this bucket can report its share of it.
    book_notional: float = 0.0

    @property
    def share_of_book(self) -> Optional[float]:
        if not self.book_notional:
            return None
        return self.notional / self.book_notional * 100.0

    @property
    def used_pct(self) -> Optional[float]:
        if not self.equity:
            return None
        return self.notional / self.equity * 100.0

    @property
    def headroom_pct(self) -> Optional[float]:
        if self.cap_pct is None or self.used_pct is None:
            return None
        return self.cap_pct * 100.0 - self.used_pct

    @property
    def over_cap(self) -> bool:
        head = self.headroom_pct
        return head is not None and head < 0

    def as_dict(self) -> dict[str, Any]:
        return {
            "label": self.label,
            "notional": self.notional,
            "share_of_book": self.share_of_book,
            "cap_pct": None if self.cap_pct is None else self.cap_pct * 100.0,
            "used_pct": self.used_pct,
            "headroom_pct": self.headroom_pct,
            "over_cap": self.over_cap,
        }


@dataclass(frozen=True)
class Book:
    """Every open position, and what they add up to."""

    positions: tuple[Position, ...] = ()
    equity: Optional[float] = None
    prices: dict[str, float] = field(default_factory=dict)
    #: The newest audit timestamp seen, so the page can say how fresh this is.
    as_of: Optional[str] = None

    # -- totals -----------------------------------------------------------

    @property
    def notional(self) -> float:
        return sum(p.notional for p in self.positions)

    @property
    def risk_dollars(self) -> float:
        """What the whole book loses if every stop fills at once.

        Positions whose stop is already past entry contribute their locked-in
        gain, which is why this can be negative and is not a sum of absolutes.
        """
        return sum(p.risk_dollars for p in self.positions)

    @property
    def longs(self) -> tuple[Position, ...]:
        return tuple(p for p in self.positions if p.is_long)

    @property
    def shorts(self) -> tuple[Position, ...]:
        return tuple(p for p in self.positions if not p.is_long)

    @property
    def protected_count(self) -> int:
        return sum(1 for p in self.positions if p.protected)

    @property
    def unmanaged(self) -> tuple[Position, ...]:
        """Positions the manager last found no live stop order for."""
        return tuple(p for p in self.positions if p.unmanaged)

    @property
    def marks_known(self) -> bool:
        """True when any position can be marked at all, live or recorded."""
        return any(self.mark_for(p).known for p in self.positions)

    @property
    def marks_are_live(self) -> bool:
        """True only when a price was supplied for at least one position."""
        return any(p.ticker in self.prices for p in self.positions)

    @property
    def unrealised(self) -> Optional[float]:
        """Book P&L, or None when no quote was supplied for any position."""
        if not self.marks_known:
            return None
        return sum((self.mark_for(p).unrealised or 0.0) for p in self.positions)

    def mark_for(self, position: Position) -> Mark:
        """A supplied price if there is one, else the last one recorded.

        Preferring the supplied price matters: a caller who went and fetched a
        quote wants that quote, not a mark from the last management pass. The
        fallback is what makes the page useful without one -- the manager
        writes down the price it saw, so the record does hold a mark, just not
        a current one. Which it is travels with the number.
        """
        live = self.prices.get(position.ticker)
        if live is not None:
            return position.mark(live)
        return position.recorded_mark()

    # -- exposure ---------------------------------------------------------

    def by_group(self) -> tuple[Exposure, ...]:
        """Exposure per group, against the group cap that spans both sleeves."""
        totals: dict[str, float] = {}
        for p in self.positions:
            totals[p.group] = totals.get(p.group, 0.0) + p.notional
        return tuple(
            Exposure(
                label, notional, cfg.MAX_EXPOSURE_GROUP_PCT, self.equity, self.notional
            )
            for label, notional in sorted(
                totals.items(), key=lambda kv: (-kv[1], kv[0])
            )
        )

    def by_sleeve(self) -> tuple[Exposure, ...]:
        """Exposure per sleeve, against each sleeve's own budget.

        The split is binary and deliberately mirrors
        ``app.risk_engine.sleeve_headroom``: single names on one side, every
        kind of fund on the other. It is *not* the four-way ``sleeve_label``
        used on a position row -- that is a readable description of one
        instrument, and using it here would invent four budgets where the
        engine enforces two, so this page would disagree with the code that
        actually stops a trade. A test pins the two together.
        """
        single, funds = 0.0, 0.0
        for p in self.positions:
            if p.kind is InstrumentKind.EQUITY:
                single += p.notional
            else:
                funds += p.notional
        buckets = (
            ("Single names", single, cfg.MAX_SINGLE_NAME_SLEEVE_PCT),
            ("Funds", funds, cfg.MAX_FUND_SLEEVE_PCT),
        )
        return tuple(
            Exposure(label, notional, cap, self.equity, self.notional)
            for label, notional, cap in buckets
            if notional
        )

    def gross(self) -> Exposure:
        return Exposure(
            "Gross exposure",
            self.notional,
            cfg.MAX_GROSS_EXPOSURE_PCT,
            self.equity,
            self.notional,
        )

    def as_dict(self) -> dict[str, Any]:
        return {
            "as_of": self.as_of,
            "equity": self.equity,
            "positions": [p.as_dict() for p in self.positions],
            "totals": {
                "count": len(self.positions),
                "long": len(self.longs),
                "short": len(self.shorts),
                "notional": self.notional,
                "risk_dollars": self.risk_dollars,
                "protected": self.protected_count,
                "unrealised": self.unrealised,
            },
            "exposure": {
                "gross": self.gross().as_dict(),
                "groups": [e.as_dict() for e in self.by_group()],
                "sleeves": [e.as_dict() for e in self.by_sleeve()],
            },
        }


# --------------------------------------------------------------------------- #
# Reading the record
# --------------------------------------------------------------------------- #


def _records(audit_path: Path) -> Iterable[tuple[dict, str]]:
    """Every parseable audit line, with its timestamp, in file order.

    File order is time order. A malformed line is skipped rather than raised
    on: the book must still be readable when one line was truncated by a
    runner dying mid-write.
    """
    try:
        text = audit_path.read_text(encoding="utf-8")
    except OSError:
        return
    for raw in text.splitlines():
        raw = raw.strip()
        if not raw:
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(record, dict):
            # Production renames message->event and asctime->ts; a plain
            # JsonFormatter does not. Read either, so a log written under any
            # handler configuration still yields a book.
            yield record, str(record.get("ts") or record.get("asctime") or "")


def read_book(
    audit_path: Path = cfg.AUDIT_LOG_PATH,
    *,
    equity: Optional[float] = None,
    prices: Optional[dict[str, float]] = None,
) -> Book:
    """The open book, from the audit log.

    A later ACCEPTED entry for a ticker replaces the earlier one and resets its
    ladder, matching ``app.position_manager.ladder_history``: an add-on
    restarts the ladder on the enlarged position. A position whose last rung
    closed the whole quantity is dropped, because it is no longer held.
    """
    open_positions: dict[str, dict[str, Any]] = {}
    newest = ""

    for record, stamp in _records(audit_path):
        event = record.get("event") or record.get("message")
        if stamp > newest:
            newest = stamp

        if event == ENTRY_EVENT:
            result = record.get("result") or {}
            if result.get("status") != "ACCEPTED":
                continue
            ticker = str(result.get("ticker") or "").upper()
            qty, entry, stop = (
                _num(result.get("quantity")),
                _num(result.get("entry_price")),
                _num(result.get("stop_price")),
            )
            if not ticker or not qty or entry is None or stop is None:
                continue
            open_positions[ticker] = {
                "ticker": ticker,
                "side": str(result.get("side") or "buy"),
                "quantity": int(qty),
                "entry_price": entry,
                "stop_price": stop,
                "atr": _num(result.get("atr")),
                "opened": stamp or None,
                "order_id": result.get("order_id"),
                "rungs_taken": 0,
                "current_stop": None,
                "last_managed": None,
                "last_action": None,
                "last_price": None,
                "last_gain_r": None,
                "last_marked": None,
            }

        elif event == MANAGED_EVENT:
            action = record.get("action") or {}
            ticker = str(action.get("ticker") or "").upper()
            held = open_positions.get(ticker)
            if not held:
                continue
            kind = action.get("action")
            new_stop = _num(action.get("new_stop"))
            if new_stop is not None:
                held["current_stop"] = new_stop
            if kind == TRANCHE:
                remaining = _num(action.get("remaining_qty"))
                if remaining is not None:
                    held["quantity"] = int(remaining)
                if isinstance(action.get("rung"), int):
                    held["rungs_taken"] = max(held["rungs_taken"], int(action["rung"]))
            # Every pass stamps the position, including a "held": the
            # manager did look, and "when was this last checked" is the
            # question the stamp answers. Price and gain come from any pass,
            # because the manager records them whatever it decides.
            held["last_managed"] = stamp or None
            held["last_action"] = kind
            # Only from a pass that actually fetched a quote, and only a
            # positive one. ``unmanaged`` writes price 0.0 as a placeholder;
            # taking it would value a short at its whole entry.
            price, gain = _num(action.get("price")), _num(action.get("gain_r"))
            if kind in MARKING_ACTIONS and price is not None and price > 0:
                held["last_price"] = price
                held["last_gain_r"] = gain
                held["last_marked"] = stamp or None

    positions = tuple(
        Position(**data)
        for _, data in sorted(open_positions.items())
        if data["quantity"] > 0
    )
    return Book(
        positions=positions,
        equity=equity,
        prices=dict(prices or {}),
        as_of=newest or None,
    )


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def _money(value: float) -> str:
    return f"{value:,.2f}"


def render(book: Book) -> str:
    """The book as a plain-text table, for the shell."""
    if not book.positions:
        return "No open positions in the record."

    out = [
        f"{len(book.positions)} open ({len(book.longs)} long, {len(book.shorts)} short)"
        f"  ·  notional {_money(book.notional)}"
        f"  ·  at risk {_money(book.risk_dollars)}",
        "",
        f"{'Ticker':<7}{'Side':<7}{'Qty':>7}{'Entry':>12}{'Stop':>12}"
        f"{'Notional':>14}{'Risk':>12}  Ladder",
        "-" * 84,
    ]
    for p in sorted(book.positions, key=lambda x: -x.notional):
        out.append(
            f"{p.ticker:<7}{p.direction:<7}{p.quantity:>7}"
            f"{p.entry_price:>12,.2f}{p.stop:>12,.2f}"
            f"{p.notional:>14,.2f}{p.risk_dollars:>12,.2f}"
            f"  {p.rungs_taken}/{len(LADDER_RUNGS)}"
            + ("  protected" if p.protected else "")
        )
    if book.equity:
        out += ["", f"Gross {book.gross().used_pct:.1f}% of equity "
                    f"(cap {cfg.MAX_GROSS_EXPOSURE_PCT * 100:.0f}%)"]
    else:
        out += ["", "Account equity is not in the record, so cap use is not shown."]
    return "\n".join(out)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="portfolio", description="The open book, from the execution audit log."
    )
    parser.add_argument("--audit", type=Path, default=cfg.AUDIT_LOG_PATH)
    parser.add_argument(
        "--equity", type=float, default=None,
        help="account equity, to report exposure against the caps",
    )
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args(argv)

    book = read_book(args.audit, equity=args.equity)
    if args.json:
        print(json.dumps(book.as_dict(), indent=2))
    else:
        print(render(book))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
