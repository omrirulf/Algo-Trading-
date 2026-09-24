"""Calibration: a copy of the model fund, started from the real paper book and held against it.

Before the shadow funds are believed, one of them has to be shown to behave
like the account it imitates. Calibration runs the model fund's machinery --
the production engine and position manager on a ``SimBroker`` over daily
bars, exactly as ``shadow.fund`` runs every fund -- from the real paper
account's own positions, cash and stops, on the model's own journalled
calls, and compares it with the real account every day for 15 trading days:
the equity at each close, and every trade that differs, with the reason.

Nothing here trades or writes. The real account is read from what the
heartbeat recorded (``logs/account.jsonl``, see ``load_snapshots``) and from
the live audit log, read as text; the only book that changes is the sim's.
It does not start until the owner has approved ``PASS_RULE`` and set
``shadow.schedule.CALIBRATION_START``.

Timing, which everything below depends on
-----------------------------------------
The real account acts on cycle day D *during* D: its management pass and
its entries fill at that day's prices. A fund acts on D's cycle at the *open
of the next session* (``shadow.fund``). So:

* The seed is the real book at the close of the start day C0, which already
  includes everything C0's cycle did.
* The fund's sessions are the ones AFTER C0: C1, C2, ... At C1's open the
  fund would act on C0's cycle -- already in the seed -- so C1 gets no cycle
  at all: no management pass, no entries; only the stops resting at the
  broker, the dividends and the close. At C2's open it acts on C1's cycle,
  at C3's on C2's, and so on.
* Stops are the exception to the one-session lag: they rest at the broker
  and fill the same day in both books.

So a real entry on C1 and the sim's entry at C2's open are the same trade a
session apart. Such a pair is counted as timing, not as a difference.
"""

from __future__ import annotations

import json
import re
import statistics
from bisect import bisect_left
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Iterable, Mapping, Optional, Sequence
from zoneinfo import ZoneInfo

from analysis.reader import JournalEntry
from config.market_calendar import is_trading_day
from shadow.audit import ENTRY_EVENT, MANAGED_EVENT, LiveAuditLeak, live_audit_guarded
from shadow.broker import ENTRY, STOP, TRANCHE
from shadow.fund import Decision, Fund, cycle_days, lines_by_day, model_signal
from shadow.market import Bars, SimFeed, calendar

#: The exchange's clock. Account times are UTC; a trading day is a New York day.
NY = ZoneInfo("America/New_York")
CLOSE = time(16, 0)

DAYS_NEEDED = 15
NAME = "calibration"

#: The paper account charges no commission, so the copy that is compared
#: with it pays none either. The funds' 0.10% a side is the race's
#: registered cost for comparing arms with one another, not a property of
#: this account; charging it here would open a gap of its own of roughly
#: the day's turnover x 0.1%, every day, that is no fault of the machinery.
CALIBRATION_COST_PER_SIDE = 0.0

#: Which bars say what a session is: the index the funds are measured
#: against, then the broad US market, then whatever else was fetched.
CALENDAR_TICKERS = ("VT", "SPY")

#: A matched trade whose quantity differs by more than this is a difference.
#: An entry sized off an equity 1-2% apart differs by 1-2%; ten percent is a
#: different decision, not rounding.
QTY_TOLERANCE = 0.10

# --------------------------------------------------------------------------- #
# The fixed list of reasons a trade may differ. Nothing else is ever written.
# --------------------------------------------------------------------------- #

TIMING = "sim acts at the next open"
SIZE = "size differs: equity differed"
SIM_REJECTED = "sim rejected: "
SIM_HELD = "sim held it already"
REAL_REFUSED = "real broker refused: "
REAL_REJECTED = "real rejected: "
STOP_DAY = "stop: filled on a different day or not at all on daily bars"
LADDER = "ladder/trim differs"
UNEXPLAINED = "unexplained"

#: Every reason, the three with a detail by their prefix.
REASONS = (TIMING, SIZE, SIM_REJECTED, SIM_HELD, REAL_REFUSED, REAL_REJECTED, STOP_DAY, LADDER,
           UNEXPLAINED)

OPEN = "open"          # opens a position or adds to it
REDUCE = "reduce"      # reduces or closes one


# --------------------------------------------------------------------------- #
# Small parsers. The account file is written by a long-running job and read
# by this one; a bad field costs that field, never the run.
# --------------------------------------------------------------------------- #


def _num(value: Any) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if number == number and abs(number) != float("inf") else None


def _text(value: Any) -> Optional[str]:
    return value.strip() if isinstance(value, str) and value.strip() else None


def _instant(value: Any) -> Optional[datetime]:
    """An ISO time (``Z`` or an offset) as an aware UTC datetime; naive is read as UTC."""
    text = _text(value)
    if text is None:
        return None
    try:
        parsed = datetime.fromisoformat(text[:-1] + "+00:00" if text.endswith("Z") else text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _audit_instant(value: Any) -> Optional[datetime]:
    """The audit log's ``ts`` (``YYYY-MM-DD HH:MM:SS,mmm``, UTC), or an ISO time."""
    text = _text(value)
    if text is None:
        return None
    try:
        return datetime.strptime(text, "%Y-%m-%d %H:%M:%S,%f").replace(tzinfo=timezone.utc)
    except ValueError:
        return _instant(text)


def ny_day(moment: datetime) -> date:
    """The New York trading day a UTC moment falls on."""
    return moment.astimezone(NY).date()


def close_of(day: date) -> datetime:
    """16:00 New York on ``day``, as UTC."""
    return datetime.combine(day, CLOSE, tzinfo=NY).astimezone(timezone.utc)


# --------------------------------------------------------------------------- #
# a) The account snapshots
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class HeldPosition:
    ticker: str
    #: Signed: a short is negative.
    qty: float
    avg_entry_price: Optional[float]
    market_value: Optional[float]
    current_price: Optional[float]


@dataclass(frozen=True)
class RestingStop:
    order_id: str
    ticker: str
    qty: int
    stop_price: float
    #: The stop's own side: "sell" protects a long.
    side: str


@dataclass(frozen=True)
class AccountFill:
    id: str
    order_id: str
    ticker: str
    side: str               # buy, sell or sell_short
    qty: float
    price: float
    at: datetime

    @property
    def signed(self) -> float:
        return self.qty if self.side == "buy" else -self.qty

    @property
    def day(self) -> date:
        return ny_day(self.at)


@dataclass(frozen=True)
class Snapshot:
    """One line of logs/account.jsonl: the account as the heartbeat saw it."""

    at: datetime
    sha: Optional[str]
    mode: Optional[str]
    equity: Optional[float]
    cash: Optional[float]
    long_market_value: Optional[float]
    short_market_value: Optional[float]
    last_equity: Optional[float]
    #: None when the positions read failed: unknown, not a flat book.
    positions: Optional[tuple[HeldPosition, ...]] = ()
    #: None when the stops read failed: unknown, not "no stops".
    stops: Optional[tuple[RestingStop, ...]] = ()
    #: A failed fills read is ``()``: the recorder reads that window again
    #: next time, so the fills are not lost, only later.
    fills: tuple[AccountFill, ...] = ()
    #: The account's equity at each day's close (portfolio history, 1D).
    history: tuple[tuple[date, float], ...] = ()
    #: When each part was read, ``part -> (from, to)``; see ``read_from``.
    reads: tuple[tuple[str, datetime, datetime], ...] = ()

    @property
    def day(self) -> date:
        return ny_day(self.at)

    @property
    def can_seed(self) -> bool:
        """Cash, positions and stops all read: the three things a seed is made of."""
        return self.cash is not None and self.positions is not None and self.stops is not None

    def read_window(self, part: str) -> tuple[datetime, datetime]:
        """When ``part`` was read: a fill before the start is in it, one after the end is not.

        A line from before the recorder timed its reads says only when the
        snapshot started; every part was read after that.
        """
        for name, start, end in self.reads:
            if name == part:
                return start, end
        return self.at, self.at


class Snapshots(list):
    """The snapshots, oldest first, and what was left out on the way."""

    def __init__(self, items: Iterable[Snapshot] = (), errors: int = 0, skipped: int = 0) -> None:
        super().__init__(items)
        #: Lines the heartbeat wrote when the recorder failed as a whole (an
        #: "error" and no fills read): a missing reading, not a bad file.
        self.errors = errors
        #: Lines that were not JSON, or not a snapshot at all.
        self.skipped = skipped


def _position(raw: Any) -> Optional[HeldPosition]:
    if not isinstance(raw, dict):
        return None
    ticker, qty = _text(raw.get("ticker")), _num(raw.get("qty"))
    if ticker is None or qty is None:
        return None
    return HeldPosition(ticker.upper(), qty, _num(raw.get("avg_entry_price")), _num(raw.get("market_value")),
                        _num(raw.get("current_price")))


def _stop(raw: Any) -> Optional[RestingStop]:
    if not isinstance(raw, dict):
        return None
    ticker, qty, price = _text(raw.get("ticker")), _num(raw.get("qty")), _num(raw.get("stop_price"))
    side = _text(raw.get("side"))
    if ticker is None or qty is None or qty < 1 or price is None or price <= 0 or side not in ("buy", "sell"):
        return None
    return RestingStop(_text(raw.get("order_id")) or "", ticker.upper(), int(qty), price, side)


def _fill(raw: Any) -> Optional[AccountFill]:
    if not isinstance(raw, dict):
        return None
    ticker, side = _text(raw.get("ticker")), _text(raw.get("side"))
    qty, price, at = _num(raw.get("qty")), _num(raw.get("price")), _instant(raw.get("at"))
    if (ticker is None or side not in ("buy", "sell", "sell_short") or qty is None or qty <= 0
            or price is None or price <= 0 or at is None):
        return None
    return AccountFill(_text(raw.get("id")) or "", _text(raw.get("order_id")) or "", ticker.upper(), side,
                       qty, price, at)


def _history(raw: Any) -> tuple[tuple[date, float], ...]:
    if not isinstance(raw, dict):
        return ()
    days, equity = raw.get("days"), raw.get("equity")
    if not isinstance(days, list) or not isinstance(equity, list):
        return ()
    out = []
    for day, value in zip(days, equity):
        number = _num(value)
        try:
            parsed = date.fromisoformat(day) if isinstance(day, str) else None
        except ValueError:
            parsed = None
        if parsed is not None and number is not None and number > 0:
            out.append((parsed, number))
    return tuple(out)


def _reads(raw: Any) -> tuple[tuple[str, datetime, datetime], ...]:
    if not isinstance(raw, dict):
        return ()
    out = []
    for part, window in raw.items():
        if isinstance(part, str) and isinstance(window, dict):
            start, end = _instant(window.get("from")), _instant(window.get("to"))
            if start is not None and end is not None and start <= end:
                out.append((part, start, end))
    return tuple(out)


def _snapshot(record: dict) -> Optional[Snapshot]:
    """A line as a snapshot, or None when its time does not parse.

    A part whose read failed is kept as unknown -- ``None`` cash, ``None``
    positions or stops -- and the rest of the line still counts: a failed
    account read does not unsay the fills and closes the same line carries.
    """
    at = _instant(record.get("at"))
    if at is None:
        return None
    account = record.get("account") if isinstance(record.get("account"), dict) else {}

    def items(key, parse):
        raw = record.get(key)
        return tuple(x for x in (parse(r) for r in raw) if x is not None) if isinstance(raw, list) else None

    positions = items("positions", _position)
    return Snapshot(
        at=at, sha=_text(record.get("sha")), mode=_text(record.get("mode")),
        equity=_num(account.get("equity")), cash=_num(account.get("cash")),
        long_market_value=_num(account.get("long_market_value")),
        short_market_value=_num(account.get("short_market_value")),
        last_equity=_num(account.get("last_equity")),
        positions=None if positions is None else tuple(p for p in positions if p.qty != 0),
        stops=items("stops", _stop), fills=items("fills", _fill) or (), history=_history(record.get("history")),
        reads=_reads(record.get("reads")),
    )


def load_snapshots(lines: Iterable[str]) -> Snapshots:
    """Every usable snapshot, oldest first. Junk and error lines are counted, not fatal."""
    found: list[Snapshot] = []
    errors = skipped = 0
    for line in lines:
        if not line or not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            skipped += 1
            continue
        if not isinstance(record, dict):
            skipped += 1
            continue
        if "error" in record and not isinstance(record.get("fills"), list):
            errors += 1
            continue
        snapshot = _snapshot(record)
        if snapshot is None:
            skipped += 1
            continue
        found.append(snapshot)
    return Snapshots(sorted(found, key=lambda s: s.at), errors=errors, skipped=skipped)


def _all_fills(snapshots: Iterable[Snapshot]) -> list[AccountFill]:
    """Every fill any snapshot carried, once, oldest first.

    A snapshot carries the fills since the one before it (or the last ten
    days when there is none), so windows can overlap; the account's own
    activity id is what makes a fill the same fill.
    """
    seen: dict[tuple, AccountFill] = {}
    for snapshot in snapshots:
        for fill in snapshot.fills:
            seen.setdefault(_fill_key(fill), fill)
    return sorted(seen.values(), key=lambda f: f.at)


def _fill_key(fill: AccountFill) -> tuple:
    """The same fill in two snapshots: the account's activity id, or everything it says."""
    return (fill.id,) if fill.id else (fill.order_id, fill.at, fill.ticker, fill.side, fill.qty, fill.price)


# --------------------------------------------------------------------------- #
# b) The real account's equity at each close
# --------------------------------------------------------------------------- #


def real_closes(snapshots: Iterable[Snapshot]) -> dict[date, float]:
    """The account's equity at each close; a later snapshot's history wins a day.

    A snapshot taken during a session carries that session's equity so far
    as its last history value -- not a close. So a day is taken from a
    snapshot only if the snapshot was taken after that day's 16:00 in New
    York; a later snapshot supplies it once it is final.
    """
    closes: dict[date, float] = {}
    for snapshot in sorted(snapshots, key=lambda s: s.at):
        for day, equity in snapshot.history:
            if snapshot.at >= close_of(day):
                closes[day] = equity
    return dict(sorted(closes.items()))


# --------------------------------------------------------------------------- #
# c) The real book at a close: the seed
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class SeedPosition:
    ticker: str
    qty: int                # signed
    avg_entry_price: float


@dataclass(frozen=True)
class Seed:
    """The real book at the close of ``day``, as the calibration fund starts it."""

    day: date
    #: When the snapshot it was built from was taken.
    taken_at: datetime
    cash: float
    positions: tuple[SeedPosition, ...]
    stops: tuple[RestingStop, ...]
    #: Fills after the snapshot and up to the close that were applied to it.
    fills_applied: int = 0
    notes: tuple[str, ...] = ()

    def tickers(self) -> set[str]:
        return {p.ticker for p in self.positions}


def book_at_close(
    snapshot: Snapshot, later_fills: Iterable[AccountFill], close_day: Optional[date] = None,
    later_stops: Optional[Iterable[RestingStop]] = None,
) -> Seed:
    """The real book at the close of ``close_day`` (default: the snapshot's own New York day).

    Starts from the snapshot's positions, cash and stops and applies every
    fill taken after the snapshot and at or before 16:00 New York on that
    day: a buy adds, a sell or short sale subtracts, cash moves by the
    signed quantity times the price (no fees: the paper account charges
    none), a fill of a stop order spends that stop, and a fill that closes a
    position (or turns it over) removes its stops.

    "After the snapshot" is part by part. The recorder reads cash, then
    positions, then stops, one after another, and a fill can land between
    two reads: then the positions already show it and the cash does not.
    Each part takes only the fills after its own read (``Snapshot.reads``).
    A fill during a read itself -- the few hundred milliseconds between
    asking and the answer -- cannot be placed: it is applied as though it
    came after, and a note says so.

    What this cannot know: a stop *placed* after the snapshot -- the bracket
    stop of an entry made later that day, a trail the manager moved. The
    snapshot's stops are as of when it was taken. The next snapshot's stops
    list is the correction: passed as ``later_stops``, it supplies the stop
    of any position the seed would otherwise hold without one. When the
    seeding snapshot was taken after the close (a "protect" run), there is
    nothing to correct.
    """
    close_day = close_day or snapshot.day
    if not snapshot.can_seed:
        missing = [name for name, part in (("cash", snapshot.cash), ("positions", snapshot.positions),
                                           ("stops", snapshot.stops)) if part is None]
        raise ValueError(f"the snapshot taken at {snapshot.at.isoformat()} has no {', '.join(missing)} "
                         f"to seed from")
    assert snapshot.cash is not None and snapshot.positions is not None and snapshot.stops is not None
    cutoff = close_of(close_day)
    book: dict[str, list[float]] = {}                      # ticker -> [signed qty, avg entry]
    for p in snapshot.positions:
        avg = p.avg_entry_price if p.avg_entry_price and p.avg_entry_price > 0 else (p.current_price or 0.0)
        book[p.ticker] = [p.qty, avg]
    stops = [[s, s.qty] for s in snapshot.stops]           # [stop, qty still resting]
    cash = snapshot.cash
    notes: list[str] = []
    applied = 0
    windows = {part: snapshot.read_window(part) for part in ("account", "positions", "stops")}

    def drop_stops(ticker: str) -> None:
        stops[:] = [pair for pair in stops if pair[0].ticker != ticker]

    for fill in sorted({_fill_key(f): f for f in later_fills}.values(), key=lambda f: f.at):
        if not (snapshot.at < fill.at <= cutoff):
            continue
        after = {part: fill.at > start for part, (start, _) in windows.items()}
        during = [part for part, (start, end) in windows.items() if start < fill.at <= end]
        if during:
            notes.append(f"{fill.ticker}: a fill at {fill.at.isoformat()} landed during the "
                         f"{' and '.join(during)} read; applied as though after it")
        if not any(after.values()):
            continue
        applied += 1
        signed = fill.signed
        if after["account"]:
            cash -= signed * fill.price
        if after["stops"]:
            for pair in stops:
                if fill.order_id and pair[0].order_id == fill.order_id:
                    pair[1] -= int(round(abs(signed)))
            stops[:] = [pair for pair in stops if pair[1] >= 1]
        if not after["positions"]:
            continue
        held, avg = book.get(fill.ticker, [0.0, 0.0])
        after = held + signed
        if abs(after) < 1e-9:
            book.pop(fill.ticker, None)
            drop_stops(fill.ticker)
        elif held == 0 or (held > 0) == (signed > 0):
            book[fill.ticker] = [after, (avg * abs(held) + fill.price * abs(signed)) / abs(after)]
        elif (after > 0) != (held > 0):
            # Turned over: what is left was opened at this fill, and the old
            # stops protected the other side.
            book[fill.ticker] = [after, fill.price]
            drop_stops(fill.ticker)
        else:
            book[fill.ticker][0] = after

    positions: list[SeedPosition] = []
    for ticker, (qty, avg) in sorted(book.items()):
        whole = int(round(qty))
        if whole == 0:
            continue
        if abs(whole - qty) > 1e-6:
            notes.append(f"{ticker}: {qty:g} shares held; seeded as {whole}")
        positions.append(SeedPosition(ticker, whole, float(avg)))

    held_sides = {p.ticker: ("sell" if p.qty > 0 else "buy") for p in positions}
    # What is held and not yet protected. The recorder lists a stop at its
    # order quantity, which a partial fill does not reduce, so stops can add
    # up to more than is held; none may protect more than that.
    room = {p.ticker: abs(p.qty) for p in positions}
    resting: list[RestingStop] = []

    def rest(stop: RestingStop, qty: int) -> None:
        take = min(int(qty), room[stop.ticker])
        if take < qty:
            notes.append(f"{stop.ticker}: a stop for {int(qty)} with {room[stop.ticker]} held and unprotected; "
                         f"seeded at {take}" if take else
                         f"{stop.ticker}: a stop for {int(qty)} with every held share already protected; left out")
        if take:
            room[stop.ticker] -= take
            resting.append(RestingStop(stop.order_id, stop.ticker, take, stop.stop_price, stop.side))

    for stop, qty in stops:
        if held_sides.get(stop.ticker) != stop.side:
            notes.append(f"{stop.ticker}: a {stop.side} stop with no position it protects was left out")
            continue
        rest(stop, qty)

    if later_stops is not None:
        protected = {s.ticker for s in resting}
        for stop in later_stops:
            if stop.ticker not in protected and held_sides.get(stop.ticker) == stop.side:
                notes.append(f"{stop.ticker}: no stop in the seeding snapshot; took the next snapshot's "
                             f"{stop.qty} @ {stop.stop_price:.2f}")
                rest(stop, stop.qty)
    for ticker in sorted(set(held_sides) - {s.ticker for s in resting}):
        notes.append(f"{ticker}: seeded with no known stop; the first management pass protects it")

    return Seed(close_day, snapshot.at, float(cash), tuple(positions), tuple(resting), applied, tuple(notes))


# --------------------------------------------------------------------------- #
# The live audit log, read as text
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class AuditRecord:
    at: Optional[datetime]
    level: str
    event: str
    result: dict
    action: dict
    raw: str

    @property
    def ticker(self) -> str:
        source = self.result if self.event == ENTRY_EVENT else self.action
        return str(source.get("ticker") or "").strip().upper()


def audit_records(lines: Iterable[str]) -> list[AuditRecord]:
    """The live audit log's lines, parsed; anything unreadable is left out."""
    out = []
    for raw in lines:
        raw = raw.strip() if isinstance(raw, str) else ""
        if not raw:
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if not isinstance(record, dict):
            continue
        result = record.get("result") if isinstance(record.get("result"), dict) else {}
        action = record.get("action") if isinstance(record.get("action"), dict) else {}
        at = _audit_instant(record.get("ts")) or _instant(result.get("timestamp"))
        out.append(AuditRecord(at, str(record.get("level") or ""), str(record.get("event") or record.get("message")
                                                                         or ""), result, action, raw))
    return out


def audit_lines_through(lines: Iterable[str], moment: datetime) -> list[str]:
    """The lines written at or before ``moment``.

    The seeded fund must know what the live manager knew at the seed, and
    nothing after it: a rung the live account took on C3 read back at C2
    would stop the sim taking it.
    """
    return [r.raw for r in audit_records(lines) if r.at is not None and r.at <= moment]


def _tickers_in(records: Iterable[AuditRecord]) -> set[str]:
    return {r.ticker for r in records if r.ticker and r.ticker != "*"}


def _short(reason: str, limit: int = 160) -> str:
    """A broker refusal's own message when it carries one; the reason, trimmed, otherwise."""
    match = re.search(r"\{.*\}", reason)
    if match:
        try:
            body = json.loads(match.group(0))
        except json.JSONDecodeError:
            body = None
        if isinstance(body, dict) and _text(body.get("message")):
            return body["message"].strip()[:limit]
    return " ".join(reason.split())[:limit]


# --------------------------------------------------------------------------- #
# d) The calibration fund
# --------------------------------------------------------------------------- #


def _no_quote(ticker: str) -> float:
    return 0.0


def seed_fund(
    seed: Seed, feed: SimFeed, bars: Bars, audit_lines: Iterable[str],
    not_shortable: frozenset[str] = frozenset(), *, cost_per_side: float = CALIBRATION_COST_PER_SIDE,
) -> Fund:
    """The model fund, holding the seeded book, with the live record of those positions.

    Positions are seeded at the account's own average entry, opened on the
    seed day, with their resting stops. No quote is taken while seeding: a
    stop placed against a live quote fills at once if the price is through
    it, and the seed is the book as it stood, not a trade.

    The fund's audit record gets the live log's lines (``audit_lines``: the
    caller cuts them at the seed), and then forgets every ticker the seed
    does not hold, so the position manager sees exactly the held positions'
    entries, rungs taken and last stops -- R from the real entry, not an
    estimate -- and nothing about a name it may buy later.
    """
    fund = Fund(NAME, model_signal, feed, bars, cash=seed.cash, cost_per_side=cost_per_side,
                not_shortable=frozenset(not_shortable), keep_actions=True)
    broker = fund.broker
    quote, broker.quote = broker.quote, _no_quote
    try:
        for p in seed.positions:
            stops = [(s.qty, s.stop_price) for s in seed.stops if s.ticker == p.ticker]
            broker.seed_position(p.ticker, p.qty, p.avg_entry_price, seed.day, stops)
    finally:
        broker.quote = quote
    marks = {}
    for p in seed.positions:
        bar = bars.bar(p.ticker, seed.day)
        if bar is not None:
            marks[p.ticker] = bar[3]
    broker.remember_marks(marks)

    lines = [line for line in audit_lines if isinstance(line, str)]
    fund.audit.seed(lines)
    fund.audit.forget(_tickers_in(audit_records(lines)) - seed.tickers())
    return fund


# --------------------------------------------------------------------------- #
# e) The run, and what it produced
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class SeriesPoint:
    day: date
    sim: float
    real: Optional[float]

    @property
    def diff(self) -> Optional[float]:
        return None if self.real is None else self.sim - self.real

    @property
    def diff_pct(self) -> Optional[float]:
        return None if not self.real else self.sim / self.real - 1.0


@dataclass(frozen=True)
class Trade:
    """One day's trading in one ticker, one way: total quantity at its average price."""

    day: date
    ticker: str
    direction: str          # OPEN or REDUCE
    side: str               # buy or sell
    qty: float
    price: float
    #: For the sim, the fill kinds (entry, close, stop); for the real account,
    #: "stop" or "market", as ``real_trades`` classes each fill.
    kinds: frozenset[str] = frozenset()

    @property
    def is_stop(self) -> bool:
        return STOP in self.kinds

    def describe(self, with_day: bool = False) -> str:
        verb = {(OPEN, "buy"): "bought", (OPEN, "sell"): "sold short", (REDUCE, "sell"): "sold",
                (REDUCE, "buy"): "bought to cover"}[(self.direction, self.side)]
        text = f"{verb} {self.qty:g} @ {self.price:.2f}"
        if self.is_stop:
            text += " (stop)"
        return f"{text} on {self.day.isoformat()}" if with_day else text


@dataclass(frozen=True)
class Match:
    real: Trade
    sim: Trade

    @property
    def timing(self) -> bool:
        return self.real.day != self.sim.day

    @property
    def stop_differs(self) -> bool:
        """A stop exit that the other book did not make the same way on the same day.

        Stops rest at the broker and fill the same day in both books, so a
        stop a session apart is not the one-session lag, and a stop in one
        book against a ladder close in the other is a different exit.
        """
        return self.real.direction == REDUCE and (self.real.is_stop or self.sim.is_stop) and (
            self.timing or self.real.is_stop != self.sim.is_stop)

    @property
    def lag(self) -> bool:
        """The same trade a session later in the sim, because it acts at the next open: not a difference.

        Only later. The sim acts on a cycle the session after the real
        account does, so a sim entry or ladder close a session *earlier*
        than the real one answered an earlier cycle: a different decision.
        """
        return self.sim.day > self.real.day and not self.stop_differs


@dataclass(frozen=True)
class Difference:
    day: date
    ticker: str
    real: str
    sim: str
    reason: str


@dataclass
class Integrity:
    unexpected: list[str] = field(default_factory=list)
    manager_errors: list[str] = field(default_factory=list)
    #: Sim positions whose live stops covered fewer shares than were held.
    uncovered: list[str] = field(default_factory=list)
    leak: Optional[str] = None
    #: Management actions that had to estimate R: the seeded record missed an entry.
    estimated_r: int = 0

    @property
    def ok(self) -> bool:
        return not (self.unexpected or self.manager_errors or self.uncovered or self.leak)


@dataclass(frozen=True)
class Metrics:
    max_abs_gap_pct: Optional[float]
    tracking_error_pct: Optional[float]
    matched_share: Optional[float]
    unexplained: Optional[int]
    #: Matched trades a session apart for the one-session lag: not differences.
    timing: int = 0
    real_trades: int = 0
    matched: int = 0
    #: The other way round (the owner's condition 6): the sim's trades that
    #: the real account also made within one session.
    sim_matched_share: Optional[float] = None
    sim_trades: int = 0
    sim_matched: int = 0


@dataclass
class CalibrationResult:
    start: date
    days_needed: int = DAYS_NEEDED
    #: One point per session run; ``real`` is None on a session with no real close.
    series: list[SeriesPoint] = field(default_factory=list)
    #: The seed marked at the start day's closes against the real close that day:
    #: the seed's own accounting, before the sim has done anything.
    day0: Optional[SeriesPoint] = None
    #: The real trades compared (the ones still pending are not among them).
    real_trades: list[Trade] = field(default_factory=list)
    sim_trades: list[Trade] = field(default_factory=list)
    matches: list[Match] = field(default_factory=list)
    differences: list[Difference] = field(default_factory=list)
    #: Real trades on the final session with no sim trade yet: the sim acts on
    #: them at the next open, which the run has not reached. Compared next run.
    pending: list[Trade] = field(default_factory=list)
    integrity: Integrity = field(default_factory=Integrity)
    seed: Optional[Seed] = None
    decisions: list[Decision] = field(default_factory=list)
    problems: list[str] = field(default_factory=list)
    fund: Optional[Fund] = field(default=None, repr=False, compare=False)

    @property
    def days_done(self) -> int:
        """Closes compared: sessions that have a real close."""
        return sum(1 for p in self.series if p.real is not None)

    @property
    def metrics(self) -> Metrics:
        gaps = [abs(p.diff_pct) for p in self.series if p.diff_pct is not None]
        spreads: list[float] = []
        previous = self.day0
        for point in self.series:
            if previous is not None and previous.real and point.real and previous.sim:
                spreads.append((point.sim / previous.sim - 1.0) - (point.real / previous.real - 1.0))
            previous = point
        matched_real = {m.real for m in self.matches}
        matched = sum(1 for t in self.real_trades if t in matched_real)
        matched_sim = {m.sim for m in self.matches}
        sim_matched = sum(1 for t in self.sim_trades if t in matched_sim)
        return Metrics(
            max_abs_gap_pct=max(gaps) if gaps else None,
            tracking_error_pct=statistics.pstdev(spreads) if len(spreads) >= 2 else None,
            matched_share=matched / len(self.real_trades) if self.real_trades else None,
            unexplained=sum(1 for d in self.differences if d.reason == UNEXPLAINED) if self.series else None,
            timing=sum(1 for m in self.matches if m.lag),
            real_trades=len(self.real_trades),
            matched=matched,
            sim_matched_share=sim_matched / len(self.sim_trades) if self.sim_trades else None,
            sim_trades=len(self.sim_trades),
            sim_matched=sim_matched,
        )


def _choose_seed(snapshots: Sequence[Snapshot], start: date) -> tuple[Optional[Seed], Optional[Snapshot], list[str]]:
    """The seed at the close of ``start``: the latest snapshot on or before it, rolled forward."""
    ordered = sorted(snapshots, key=lambda s: s.at)
    candidates = [s for s in ordered if s.day <= start and s.can_seed]
    if not candidates:
        return None, None, [f"no account snapshot on or before {start.isoformat()} read cash, positions "
                            f"and stops: nothing to seed from"]
    chosen = candidates[-1]
    later = [s for s in ordered if s.at > chosen.at]
    next_stops = next((s.stops for s in later if s.stops is not None), None)
    # The chosen snapshot's own fills too: a fill made while it was being
    # read is in its own list, and the next window may not reach back to it.
    seed = book_at_close(chosen, _all_fills([chosen, *later]), start, later_stops=next_stops)
    problems = []
    if chosen.day < start:
        problems.append(f"the seed is the {chosen.day.isoformat()} snapshot rolled forward to "
                        f"{start.isoformat()}'s close through later fills")
    return seed, chosen, problems


def _seed_cut(start: date, snapshot: Snapshot) -> datetime:
    """The moment the seed stands for: the start's close, or a later snapshot taken after it."""
    return max(close_of(start), snapshot.at)


def _marked(seed: Seed, bars: Bars, day: date) -> float:
    total = seed.cash
    for p in seed.positions:
        bar = bars.bar(p.ticker, day)
        total += p.qty * (bar[3] if bar is not None else p.avg_entry_price)
    return total


def _uncovered(fund: Fund, day: date) -> list[str]:
    covered: dict[str, int] = defaultdict(int)
    for stop in fund.broker.live_stops():
        covered[stop.ticker] += stop.qty
    return [f"{day.isoformat()} {ticker}: {abs(pos.qty)} held, stops cover {covered[ticker]}"
            for ticker, pos in sorted(fund.broker.positions.items()) if covered[ticker] < abs(pos.qty)]


def run_calibration(
    snapshots: Sequence[Snapshot], entries: Sequence[JournalEntry], bars: Bars, feed: SimFeed, start: date,
    days_needed: int = DAYS_NEEDED, audit_lines: Iterable[str] = (), not_shortable: frozenset[str] = frozenset(),
    *, calendar_tickers: Sequence[str] = CALENDAR_TICKERS, cost_per_side: float = CALIBRATION_COST_PER_SIDE,
) -> CalibrationResult:
    """The calibration fund from the real book at ``start``'s close, session by session.

    Sessions are the bar sessions after ``start``, through the last day the
    real account has a close for, until ``days_needed`` of them have a real
    close to compare with. C1 gets no cycle (C0's is in the seed); every
    later session acts on the session before it, when a cycle ran that day.
    ``feed`` must be a ``SimFeed`` over ``bars``.
    """
    result = CalibrationResult(start=start, days_needed=days_needed)
    audit_lines = list(audit_lines)
    seed, chosen, problems = _choose_seed(snapshots, start)
    result.problems += problems
    if seed is None or chosen is None:
        return result
    result.seed = seed
    real = real_closes(snapshots)
    fund = seed_fund(seed, feed, bars, audit_lines_through(audit_lines, _seed_cut(start, chosen)), not_shortable,
                     cost_per_side=cost_per_side)
    result.fund = fund
    result.day0 = SeriesPoint(start, _marked(seed, bars, start), real.get(start))

    last_real = max((d for d in real if d > start), default=None)
    sessions: list[date] = []
    if last_real is None:
        result.problems.append(f"no real close after {start.isoformat()} yet")
    else:
        sessions = calendar(bars, (*calendar_tickers, *sorted(seed.tickers()), *bars.tickers()),
                            start + timedelta(days=1), last_real)
    cycles = lines_by_day(entries)
    ran = cycle_days(entries)

    run: list[date] = []
    managed = False
    try:
        with live_audit_guarded():
            previous = start
            compared = 0
            for session in sessions:
                if compared >= days_needed:
                    break
                feed.at_open(session)
                cycle = None
                if previous != start and previous in ran:
                    cycle = cycles.get(previous, [])
                fund.session(session, cycle)
                run.append(session)
                # The seeded book is the real account's, faults and all; from
                # the first management pass on, its stops are the sim's own.
                managed = managed or cycle is not None
                if managed:
                    result.integrity.uncovered += _uncovered(fund, session)
                if session in real:
                    compared += 1
                previous = session
    except LiveAuditLeak as exc:
        result.integrity.leak = str(exc)

    result.series = [SeriesPoint(d.day, d.equity, real.get(d.day)) for d in fund.days]
    result.decisions = list(fund.decisions or ())
    result.integrity.unexpected = list(fund.tally.unexpected)
    result.integrity.manager_errors = list(fund.tally.manager_errors)
    result.integrity.estimated_r = fund.tally.estimated_r
    if fund.tally.data_holes:
        holes = fund.tally.data_holes
        result.problems.append(f"{len(holes)} ticker-day(s) had no price bar, so the sim left those positions "
                               f"as they were and made no entry in them that day (first: {holes[0]})")
    if run:
        compare_trades(result, snapshots, audit_lines, fund, _seed_cut(start, chosen), run)
    return result


# --------------------------------------------------------------------------- #
# f) The trades that differ
# --------------------------------------------------------------------------- #


def _group(rows: Iterable[tuple[date, str, str, str, float, float, str]]) -> list[Trade]:
    """(day, ticker, direction, side, qty, price, kind) rows into one Trade per day, ticker and direction."""
    totals: dict[tuple[date, str, str], list] = {}
    for day, ticker, direction, side, qty, price, kind in rows:
        entry = totals.setdefault((day, ticker, direction), [side, 0.0, 0.0, set()])
        entry[1] += qty
        entry[2] += qty * price
        entry[3].add(kind)
    return [Trade(day, ticker, direction, side, qty, notional / qty if qty else 0.0, frozenset(kinds))
            for (day, ticker, direction), (side, qty, notional, kinds) in sorted(totals.items())]


def real_trades(seed: Seed, fills: Iterable[AccountFill], after: datetime, first: date, last: date,
                stop_order_ids: frozenset[str] = frozenset(),
                ladder_order_ids: frozenset[str] = frozenset()) -> list[Trade]:
    """The real account's trades from ``first`` to ``last``, each classed against the book it met.

    Fills at or before ``after`` are already in the seed. Every later fill
    moves the book forward from the seed, so a sell is known to be a close
    of a long, not a short sale, whatever day it falls on.

    A reduction is a stop's when its order is one a snapshot listed as a
    stop, a ladder or trim close when the live manager recorded its order,
    and otherwise a stop still: the stop is the only other exit this system
    has, and a stop replaced and filled between two snapshots is never
    listed under the id that filled.
    """
    book = {p.ticker: float(p.qty) for p in seed.positions}
    rows = []
    for fill in sorted(fills, key=lambda f: f.at):
        if fill.at <= after:
            continue
        held = book.get(fill.ticker, 0.0)
        signed = fill.signed
        direction = OPEN if abs(held) < 1e-9 or (held > 0) == (signed > 0) else REDUCE
        book[fill.ticker] = held + signed
        if first <= fill.day <= last:
            if fill.order_id and fill.order_id in stop_order_ids:
                kind = STOP
            elif direction == OPEN or (fill.order_id and fill.order_id in ladder_order_ids):
                kind = "market"
            else:
                kind = STOP
            rows.append((fill.day, fill.ticker, direction, "buy" if signed > 0 else "sell", fill.qty, fill.price,
                         kind))
    return _group(rows)


def sim_trades(fund: Fund) -> list[Trade]:
    """The fund's fills (entries, ladder/trim closes, stops) grouped the same way."""
    direction = {ENTRY: OPEN, TRANCHE: REDUCE, STOP: REDUCE}
    return _group((f.day, f.ticker, direction[f.kind], f.side, float(f.qty), f.price, f.kind)
                  for f in fund.broker.fills if f.kind in direction)


def match_trades(real: Sequence[Trade], sim: Sequence[Trade], order: Sequence[date]) -> list[Match]:
    """Each real trade to the sim's same ticker and direction within one session.

    Preference, for the same pair: the same session, then the sim a session
    later (what the one-session lag produces), then -- for a stop only -- a
    session earlier. An entry or a ladder close the sim made a session
    before the real account answered an earlier cycle than the real one
    did, so it is not the same trade; a stop rests at the broker in both
    books and can fill a day apart on daily bars. Greedy in date order, so
    the result does not depend on dict order.
    """
    def index(day: date) -> int:
        return bisect_left(order, day)

    used: set[int] = set()
    matches = []
    for r in sorted(real, key=lambda t: (t.day, t.ticker, t.direction)):
        best, rank = None, None
        for i, s in enumerate(sim):
            if i in used or s.ticker != r.ticker or s.direction != r.direction:
                continue
            gap = index(s.day) - index(r.day)
            if abs(gap) > 1 or (gap == -1 and not (r.is_stop or s.is_stop)):
                continue
            candidate_rank = {0: 0, 1: 1, -1: 2}[gap]
            if rank is None or candidate_rank < rank:
                best, rank = i, candidate_rank
        if best is not None:
            used.add(best)
            matches.append(Match(r, sim[best]))
    return matches


def _real_refusals(records: Iterable[AuditRecord]) -> dict[tuple[str, date], list[AuditRecord]]:
    out: dict[tuple[str, date], list[AuditRecord]] = defaultdict(list)
    for record in records:
        if record.event == ENTRY_EVENT and record.at is not None and record.ticker:
            out[(record.ticker, ny_day(record.at))].append(record)
    return out


def _why_real_only(trade: Trade, decisions: Sequence[Decision]) -> str:
    """A real trade the sim did not make."""
    if trade.direction == REDUCE:
        return STOP_DAY if trade.is_stop else LADDER
    # The sim acts on the real account's cycle day at the next open: its
    # answer to the same line is the decision journalled for that cycle day.
    said = [d for d in decisions if d.cycle_day == trade.day and d.ticker == trade.ticker]
    for decision in reversed(said):
        if not decision.dispatched:
            return SIM_HELD
        if decision.status in ("REJECTED", "ERROR"):
            return SIM_REJECTED + _short(decision.reason)
    return UNEXPLAINED


def _why_sim_only(trade: Trade, order: Sequence[date],
                  refusals: Mapping[tuple[str, date], list[AuditRecord]]) -> str:
    """A sim trade the real account did not make."""
    if trade.direction == REDUCE:
        return STOP_DAY if trade.is_stop else LADDER
    position = bisect_left(order, trade.day)
    if position < 1:
        return UNEXPLAINED
    cycle_day = order[position - 1]
    said = refusals.get((trade.ticker, cycle_day), [])
    if any(r.result.get("status") == "ACCEPTED" for r in said):
        return UNEXPLAINED          # accepted live, yet no fill recorded
    for status, prefix in (("ERROR", REAL_REFUSED), ("REJECTED", REAL_REJECTED)):
        hits = [r for r in said if r.result.get("status") == status]
        if hits:
            return prefix + _short(str(hits[-1].result.get("reason") or ""))
    return UNEXPLAINED


def compare_trades(result: CalibrationResult, snapshots: Sequence[Snapshot], audit_lines: Sequence[str],
                   fund: Fund, after: datetime, sessions: Sequence[date]) -> None:
    """Fill in the result's trades, matches, pending trades and differences."""
    assert result.seed is not None
    order = [result.start, *sessions]
    records = audit_records(audit_lines)
    stop_ids = frozenset(s.order_id for snap in snapshots for s in (snap.stops or ()) if s.order_id)
    ladder_ids = frozenset(str(r.action.get("order_id")) for r in records if r.event == MANAGED_EVENT
                           and r.action.get("action") in ("tranche_taken", "group_cap_trimmed")
                           and r.action.get("order_id"))
    real = real_trades(result.seed, _all_fills(snapshots), after, sessions[0], sessions[-1], stop_ids, ladder_ids)
    sim = sim_trades(fund)
    matches = match_trades(real, sim, order)
    # A trade is one (day, ticker, direction): its value is its identity.
    matched_real = {m.real for m in matches}
    matched_sim = {m.sim for m in matches}

    final = sessions[-1]
    # A real entry or ladder close on the final session is answered at the
    # next open, which the run has not reached. A stop is not: it fills the
    # same day in both books, so an unmatched one is already a difference.
    result.pending = [t for t in real if t.day == final and t not in matched_real and not t.is_stop]
    result.real_trades = [t for t in real if t not in result.pending]
    result.sim_trades = sim
    result.matches = matches

    refusals = _real_refusals(records)
    differences = []
    for m in matches:
        reason = None
        if m.stop_differs:
            reason = STOP_DAY
        elif abs(m.sim.qty - m.real.qty) > QTY_TOLERANCE * m.real.qty:
            reason = SIZE if m.real.direction == OPEN or (m.real.is_stop and m.sim.is_stop) else LADDER
        if reason is not None:
            differences.append(Difference(m.real.day, m.real.ticker, m.real.describe(m.timing),
                                          m.sim.describe(m.timing), reason))
    for t in result.real_trades:
        if t not in matched_real:
            differences.append(Difference(t.day, t.ticker, t.describe(), "none", _why_real_only(t, result.decisions)))
    for t in sim:
        if t not in matched_sim:
            differences.append(Difference(t.day, t.ticker, "none", t.describe(), _why_sim_only(t, order, refusals)))
    result.differences = sorted(differences, key=lambda d: (d.day, d.ticker, d.real, d.sim))


# --------------------------------------------------------------------------- #
# h) The pass rule -- approved by the owner on 2026-09-24; in force with the start date
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class PassRule:
    text: tuple[str, ...]
    #: The owner approved the rule on 2026-09-24 and asked for it to take
    #: effect together with the start date, once the first account snapshot
    #: exists: this flag and ``shadow.schedule.CALIBRATION_START`` change
    #: together, in one reviewed change (a test enforces it).
    approved: bool
    closes: int
    max_gap_pct: float
    tracking_error_pct: float
    matched_share: float
    unexplained: int
    #: Condition 6: the share of the sim's trades the real account also made.
    sim_matched_share: float = 0.90


PASS_RULE = PassRule(
    text=(
        "Calibration passes only if all six hold over 15 trading days:",
        "1. On every one of the 15 closes, the simulated equity is within 1.0% of the real account's equity.",
        "2. The tracking error of daily returns (the spread of sim minus real, day by day) is at most "
        "0.20% a day.",
        "3. At least 90% of the real account's trades (entries, ladder/trim closes, stop exits) are "
        "matched by the same trade in the sim within one session.",
        "4. No 'unexplained' difference: every trade that differs names a reason from the fixed list.",
        "5. Integrity: no unexpected engine error, no position-manager error, every sim position's stops "
        "cover it, and no line reached the live audit log.",
        "6. The other way round: at least 90% of the sim's trades are also made by the real account "
        "within one session.",
        "If calibration fails: the cause is fixed and logged in the Amendments table, and the 15 trading "
        "days restart from zero. A difference whose stated reason turns out to be a bug counts as a fail.",
    ),
    approved=False,
    closes=DAYS_NEEDED,
    # (1) The sim enters a session late: the account buys during the day it
    # decides, the sim at the next open. On one day's entries -- a few
    # positions of 3-5% of equity each, each moving about 1% between the two
    # fills, in both directions -- that nets to about 0.03-0.05% of equity per
    # trade day. As a random walk over 15 days it is 0.1-0.2%; even if every
    # day's error pointed the same way it is 0.45-0.75%. So 1% is loose
    # enough for timing noise and still catches what calibration exists for:
    # a missed fill or a cash sign error is a step of a whole position (3-12%
    # of equity) at once, a position held in one book and not the other
    # carries its full move, and a sizing error on every entry compounds
    # past 1% within days.
    max_gap_pct=0.01,
    # (2) The book itself moves 0.5-1% a day. Timing noise on the day's
    # entries is 0.03-0.05% of equity, and stops filled at their price on
    # daily bars rather than on the tape add a few basis points, so an honest
    # copy tracks well under 0.1% a day. 0.20% is twice that, and a sim
    # holding a fifth of the book differently (gross ~95%, names moving ~1% a
    # day) already shows about 0.2%.
    tracking_error_pct=0.002,
    # (3) Fifteen sessions are some 50-100 real trades. A few may differ for
    # real reasons -- a stop the tape reaches on a different day than the
    # daily bar, a refusal only the real broker makes (a hard-to-borrow short
    # it takes as a day order only), a tranche whose shares were still held
    # for a stop. One in ten leaves room for those, each still needing a
    # reason (4); more means the sim is not the same system.
    matched_share=0.90,
    # (4) Calibration is for understanding every difference. An unexplained
    # one is exactly the sim bug, or real-account fault, it exists to find.
    unexplained=0,
    # (5) is not statistics: any one of those is a bug, and a sim with a bug
    # proves nothing however close its equity line runs.
    # (6) The owner's addition of 24 Sep 2026: (3) alone lets a sim that
    # trades far more than the account pass, as long as it also makes the
    # account's trades. Asking the same of the sim's trades closes that.
    sim_matched_share=0.90,
)


def _pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def evaluate_pass_rule(result: Optional[CalibrationResult],
                       rule: PassRule = PASS_RULE) -> tuple[bool, list[str]]:
    """Each condition's verdict (PASS, FAIL or PENDING), and whether the whole rule passed.

    The rule passes only on a complete calibration -- ``rule.closes`` closes
    compared -- with all five conditions met. Before that a condition already
    broken reads FAIL, and one that could still go either way reads PENDING.
    """
    if result is None:
        return False, ["Calibration has not started."]
    m = result.metrics
    done = result.days_done
    complete = done >= rule.closes
    header = [f"{'Rule not in force yet' if not rule.approved else 'Approved rule'}: "
              f"{done} of {rule.closes} closes compared."]
    if not rule.approved:
        header.append("A rule not yet in force cannot pass, whatever the numbers say.")
    header += [f"Note: {p}" for p in result.problems]
    verdicts: list[bool] = []
    lines: list[str] = []

    def verdict(ok: Optional[bool], number: int, what: str, detail: str) -> None:
        state = "PENDING" if ok is None else ("PASS" if ok else "FAIL")
        verdicts.append(bool(ok))
        lines.append(f"{number}. {what}: {state} ({detail})")

    # 1. Every close within the gap: broken by one close, confirmed only at the end.
    worst = max((p for p in result.series if p.diff_pct is not None), key=lambda p: abs(p.diff_pct),
                default=None)
    if worst is None:
        verdict(None, 1, f"every close within {_pct(rule.max_gap_pct)}", "no close compared yet")
    else:
        over = abs(worst.diff_pct) > rule.max_gap_pct
        verdict(False if over else (True if complete else None), 1,
                f"every close within {_pct(rule.max_gap_pct)}",
                f"worst {_pct(abs(worst.diff_pct))} on {worst.day.isoformat()}")

    # 2. Tracking error: a spread, so only a complete run can be judged.
    te = m.tracking_error_pct
    if te is None:
        verdict(None, 2, f"tracking error at most {_pct(rule.tracking_error_pct)} a day", "too few days")
    else:
        ok = te <= rule.tracking_error_pct
        verdict(ok if complete else None, 2, f"tracking error at most {_pct(rule.tracking_error_pct)} a day",
                f"{_pct(te)} a day so far" if not complete else f"{_pct(te)} a day")

    # 3. Matched share.
    if m.matched_share is None:
        verdict(False if complete else None, 3, f"at least {rule.matched_share:.0%} of real trades matched",
                "no real trade to match")
    else:
        ok = m.matched_share >= rule.matched_share
        verdict(ok if complete else None, 3, f"at least {rule.matched_share:.0%} of real trades matched",
                f"{m.matched} of {m.real_trades}, {m.matched_share:.1%}; {m.timing} a session apart")

    # 4. Unexplained differences: one is enough to fail.
    unexplained = m.unexplained or 0
    ok4 = unexplained <= rule.unexplained
    verdict(False if not ok4 else (True if complete else None), 4, "no unexplained difference",
            f"{unexplained} of {len(result.differences)} difference(s) unexplained")

    # 5. Integrity: one breach is enough to fail.
    i = result.integrity
    problems = []
    if i.unexpected:
        problems.append(f"{len(i.unexpected)} unexpected engine error(s)")
    if i.manager_errors:
        problems.append(f"{len(i.manager_errors)} position-manager error(s)")
    if i.uncovered:
        problems.append(f"{len(i.uncovered)} uncovered position-day(s)")
    if i.leak:
        problems.append("a line reached the live audit log")
    verdict(False if problems else (True if complete else None), 5, "integrity",
            "; ".join(problems) if problems else "clean so far" if not complete else "clean")

    # 6. The two-way match: the sim's trades found in the real account.
    what6 = f"at least {rule.sim_matched_share:.0%} of the sim's trades matched in the real account"
    if m.sim_matched_share is None:
        verdict(False if complete else None, 6, what6, "no sim trade to match")
    else:
        verdict((m.sim_matched_share >= rule.sim_matched_share) if complete else None, 6, what6,
                f"{m.sim_matched} of {m.sim_trades}, {m.sim_matched_share:.1%}")

    passed = rule.approved and complete and all(verdicts)
    return passed, header + lines


def calibration_status(result: Optional[CalibrationResult], evaluation: Optional[tuple[bool, list[str]]],
                       rule: PassRule = PASS_RULE) -> str:
    """not_started, running (fewer closes than the rule needs), passed or failed.

    Passed needs an approved rule as well as the numbers: the funds are
    shown only after calibration passes, and an unapproved rule is not the
    owner's rule. A complete run under an unapproved rule reads "failed" --
    the one reading that shows nothing more -- and the rule's own lines say
    why. (It cannot happen in a real run: ``shadow.schedule`` keeps
    calibration from starting until the rule is approved.)
    """
    if result is None:
        return "not_started"
    if result.days_done < min(result.days_needed, rule.closes):
        return "running"
    return "passed" if rule.approved and evaluation is not None and evaluation[0] else "failed"


# --------------------------------------------------------------------------- #
# i) How long the real account holds a position
# --------------------------------------------------------------------------- #

#: Actions only a full management pass writes, one per position held. A
#: protect-only pass writes a line only for a position it had to fix, so
#: its silence about a ticker says nothing about whether it is held.
_FULL_PASS = frozenset({"held", "stop_raised", "tranche_taken", "unmanaged", "group_cap_trimmed"})


@dataclass(frozen=True)
class Holding:
    ticker: str
    entered: date
    #: None while it is still held.
    closed: Optional[date]
    #: Trading days from entry to close (or to the last observation, if open).
    days: int
    #: False when no entry line was found and the first sighting stands in.
    entry_known: bool = True


def trading_days_between(first: date, last: date) -> int:
    """Trading days after ``first``, up to and including ``last``."""
    count, day = 0, first
    while day < last:
        day += timedelta(days=1)
        if is_trading_day(day):
            count += 1
    return count


def holding_periods(audit_lines: Iterable[str], journal_entries: Iterable[JournalEntry],
                    snapshots: Iterable[Snapshot]) -> list[Holding]:
    """Every real position from entry to close, from what the logs saw.

    Entry: the New York day of the ``ACCEPTED`` line that opened it (an add
    to a held position does not restart it). Held on a day: a
    ``position_managed`` line for it, a journal line marking it held, or a
    snapshot listing it. Closed: once snapshots exist, the first snapshot
    day it is gone, moved back to the day of the last fill in that ticker if
    one is on record. Before snapshots, the close is inferred: the first day
    after it was last seen on which a full management pass ran or a cycle
    journalled held lines, and it was in neither. That is an upper bound --
    the position closed some time between the last sighting and that day --
    so an inferred holding time is at most a day or two long, never short.

    An entry never seen held afterwards, with no fill to confirm it, is left
    out: the order may never have filled.
    """
    records = audit_records(audit_lines)
    snapshots = list(snapshots)
    entries: dict[str, set[date]] = defaultdict(set)
    seen: dict[str, set[date]] = defaultdict(set)
    observed: set[date] = set()
    for r in records:
        if r.at is None or not r.ticker or r.ticker == "*":
            continue
        day = ny_day(r.at)
        if r.event == ENTRY_EVENT and r.result.get("status") == "ACCEPTED":
            entries[r.ticker].add(day)
        elif r.event == MANAGED_EVENT:
            seen[r.ticker].add(day)
            if r.action.get("action") in _FULL_PASS:
                observed.add(day)
    for e in journal_entries:
        if e.held and e.timestamp is not None:
            day = ny_day(e.timestamp if e.timestamp.tzinfo else e.timestamp.replace(tzinfo=timezone.utc))
            seen[e.ticker].add(day)
            observed.add(day)
    fills: dict[str, list[date]] = defaultdict(list)
    for s in snapshots:
        if s.positions is None:
            continue            # the positions read failed: this line saw nothing held
        observed.add(s.day)
        for p in s.positions:
            seen[p.ticker].add(s.day)
    for f in _all_fills(snapshots):
        fills[f.ticker].append(f.day)

    everything = observed | {d for days in seen.values() for d in days} | {d for days in entries.values() for d in days}
    if not everything:
        return []
    as_of = max(everything)

    out: list[Holding] = []
    for ticker in sorted(set(entries) | set(seen)):
        entry_days, seen_days = entries[ticker], seen[ticker]
        start: Optional[date] = None
        known = True
        last_seen: Optional[date] = None
        sighted = False
        absent_on: Optional[date] = None

        def finish(close: date) -> None:
            confirming = [d for d in fills[ticker] if (last_seen or start) <= d <= close]
            if not sighted and not confirming:
                return
            closed = max(confirming) if confirming else close
            out.append(Holding(ticker, start, closed, trading_days_between(start, closed), known))

        for day in sorted(entry_days | seen_days | observed):
            is_entry, is_seen = day in entry_days, day in seen_days
            if start is not None:
                if is_seen:
                    last_seen, sighted, absent_on = day, True, None
                elif day in observed and day > start and absent_on is None:
                    absent_on = day
                if is_entry and absent_on is not None:
                    finish(absent_on)
                    start = None
            if start is None and (is_entry or is_seen):
                start, known = day, is_entry
                last_seen, sighted, absent_on = (day, True, None) if is_seen else (None, False, None)
        if start is not None:
            if absent_on is not None:
                finish(absent_on)
            else:
                out.append(Holding(ticker, start, None, trading_days_between(start, as_of), known))
    return out


def holding_days(audit_lines: Iterable[str], journal_entries: Iterable[JournalEntry],
                 snapshots: Iterable[Snapshot]) -> dict:
    """The real account's typical holding time: closed positions, and the age of open ones.

    The shape of the funds JSON's ``calibration.holding_days``. Holding times
    are in trading days; see ``holding_periods`` for how a close is found and
    why an inferred one is an upper bound.
    """
    periods = holding_periods(audit_lines, journal_entries, snapshots)
    closed = [h.days for h in periods if h.closed is not None]
    still_open = [h.days for h in periods if h.closed is None]
    return {
        "median": float(statistics.median(closed)) if closed else None,
        "min": min(closed) if closed else None,
        "max": max(closed) if closed else None,
        "closed": len(closed),
        "open_median": float(statistics.median(still_open)) if still_open else None,
    }


EMPTY_HOLDING = {"median": None, "min": None, "max": None, "closed": 0, "open_median": None}


# --------------------------------------------------------------------------- #
# j) What the dashboard reads
# --------------------------------------------------------------------------- #


def _round(value: Optional[float], places: int) -> Optional[float]:
    return None if value is None else round(float(value), places)


def calibration_json(
    result: Optional[CalibrationResult], status: str, start: Optional[date],
    pass_rule_eval: Optional[tuple[bool, list[str]]], holding: Optional[dict],
    rule: PassRule = PASS_RULE,
) -> dict:
    """The ``calibration`` part of the funds JSON.

    With no ``start`` it is "not_started" whatever else is passed: no series,
    no differences, null metrics -- only the pass rule and the real
    account's holding times. Two keys beyond the contract: the rule's
    per-condition ``verdicts``, and ``timing`` (trades matched a session
    apart) in the metrics; a reader that does not know them ignores them.
    """
    started = start is not None and result is not None
    metrics = result.metrics if started else None
    out = {
        "status": status if start is not None else "not_started",
        "start": start.isoformat() if start is not None else None,
        "days_done": result.days_done if started else 0,
        "days_needed": result.days_needed if started else rule.closes,
        "pass_rule": {
            "text": list(rule.text),
            "approved": rule.approved,
            "verdicts": list(pass_rule_eval[1]) if (started and pass_rule_eval) else [],
        },
        "series": [
            {"day": p.day.isoformat(), "sim": round(p.sim, 2), "real": _round(p.real, 2),
             "diff_pct": _round(p.diff_pct, 6)}
            for p in (result.series if started else ())
        ],
        "differences": [
            {"day": d.day.isoformat(), "ticker": d.ticker, "real": d.real, "sim": d.sim, "reason": d.reason}
            for d in (result.differences if started else ())
        ],
        "metrics": {
            "max_abs_gap_pct": _round(metrics.max_abs_gap_pct, 6) if metrics else None,
            "tracking_error_pct": _round(metrics.tracking_error_pct, 6) if metrics else None,
            "matched_share": _round(metrics.matched_share, 6) if metrics else None,
            "sim_matched_share": _round(metrics.sim_matched_share, 6) if metrics else None,
            "unexplained": metrics.unexplained if metrics else None,
            "timing": metrics.timing if metrics else None,
        },
        "holding_days": dict(holding) if holding else dict(EMPTY_HOLDING),
    }
    if started and result.problems:
        out["problems"] = list(result.problems)
    return out


def calibration_report(
    *, snapshots: Sequence[Snapshot], entries: Sequence[JournalEntry], audit_lines: Sequence[str], start: date,
    final_through: date, fetcher, not_shortable: frozenset[str] = frozenset(), days_needed: int = DAYS_NEEDED,
    holding: Optional[dict] = None,
) -> dict:
    """Fetch the bars, run the calibration and return its JSON part: what ``shadow.run`` prints.

    Bars are fetched for the seeded positions, every line journalled from
    the start on, and the calendar tickers, through ``fetcher`` (the race's
    ``OhlcFetcher``, cut to final closes at ``final_through``).
    """
    seed, _, problems = _choose_seed(snapshots, start)
    if seed is None:
        result = CalibrationResult(start=start, days_needed=days_needed, problems=problems)
        evaluation = evaluate_pass_rule(result)
        return calibration_json(result, calibration_status(result, evaluation), start, evaluation, holding)
    tickers = set(CALENDAR_TICKERS) | seed.tickers() | {
        line.ticker for day, lines in lines_by_day(entries).items() if day >= start for line in lines
    }
    bars = Bars.fetch(tickers, start, final_through, fetcher)
    feed = SimFeed(bars)
    result = run_calibration(snapshots, entries, bars, feed, start, days_needed, audit_lines, not_shortable)
    evaluation = evaluate_pass_rule(result)
    out = calibration_json(result, calibration_status(result, evaluation), start, evaluation, holding)
    if result.fund is not None:
        from shadow.order_matters import fund_summary

        out["order_matters"] = fund_summary(result.fund)
    return out


__all__ = [
    "AccountFill", "AuditRecord", "CALIBRATION_COST_PER_SIDE", "CalibrationResult", "DAYS_NEEDED", "Difference",
    "Holding", "HeldPosition", "Integrity", "Match", "Metrics", "PASS_RULE", "PassRule", "REASONS",
    "RestingStop", "Seed", "SeedPosition", "SeriesPoint", "Snapshot", "Snapshots", "Trade", "audit_lines_through",
    "audit_records", "book_at_close", "calibration_json", "calibration_report", "calibration_status",
    "compare_trades", "evaluate_pass_rule", "holding_days", "holding_periods", "load_snapshots", "match_trades",
    "real_closes", "real_trades", "run_calibration", "seed_fund", "sim_trades", "trading_days_between",
]
