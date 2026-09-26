"""One simulated fund, day by day, through the production engine and manager.

The day, for every fund alike
-----------------------------
A cycle journalled on day D is acted on at the open of the next session T,
the race's own entry rule (a line on D enters at the D+1 open). At T:

1. **The open.** Every resting stop the price gapped through fills at the
   open (the broker does this, not the manager, as live).
2. **The manager** -- ``app.position_manager.PositionManager``, unchanged --
   runs its pass: profit-ladder rungs, the trailing stop, the exposure-group
   trims. It sees the open as the latest price, and an ATR computed by the
   production method from the 90 days before it (``shadow.market``). Live,
   management runs before any entry; so here.
3. **The entries.** D's answered lines, one at a time, through the
   production ``ExecutionEngine``: conviction floor, position count, the
   gross, sleeve, group and stock-market limits, ATR stop, sizing. Market
   orders fill at the open. A ticker the fund already holds is skipped, as
   live (``SKIP_HELD_TICKERS``). Order: see "Priority", below.
4. **The session.** Every live stop the bar's low (high, for a short)
   reaches fills at its price.
5. **The close.** Dividends going ex that day are credited or charged on
   the shares held at the previous close, and the book is marked at the
   close. That mark is the fund's equity for the day.

A session with no cycle the day before still does 1, 4 and 5: stops rest
at the broker whether or not the heartbeat ran.

Which lines, and in what order
------------------------------
Only lines every fund can act on: not held by the live account (the model
was not asked, so no fund gets that name that day), and answered by the
model -- a timeout or a failed call removes the name for EVERY fund that
day, the same rule as the race (Amendment 2026-09-24).

**Priority.** When there is more to buy than the caps allow, the first
lines dispatched take the room. Every fund -- all but the exploratory
"highest conviction first" one, below -- uses the one rule production
uses: **watchlist order** (``config.watchlist.DEFAULT_WATCHLIST``), one
signal at a time, each seeing the fills before it. Production has no other
rule -- there is no sort by conviction anywhere on the dispatch path -- and
a calibration fund dispatching in any other order would differ from the
real account for that reason alone. A day with two cycles is dispatched
cycle by cycle, each in watchlist order; a second same-side entry in a
ticker on one day is refused by the broker, as live.

Two exploratory funds
---------------------
The owner's decisions of 25 Sep 2026 add two funds that trade the model's
own signals with the same machinery, start, costs and rules, each changing
one thing, so that a comparison with the model fund isolates it. Both are
simulation only and exploratory: they answer a question, they cannot change
the decision. Production and the calibration copy keep watchlist order and
the normal size; nothing here is reachable from either.

* **Highest conviction first** (``priority=CONVICTION_FIRST``). The owner's
  rule: when there is not enough room, it buys in highest-conviction-first
  order instead of watchlist order. So each cycle is first tried in
  watchlist order on a copy of the book (``Fund._short_of_room``). If that
  runs out of room -- a signal a portfolio limit refuses or cuts short --
  the cycle is dispatched by conviction, highest first, ties in watchlist
  order; if not, in watchlist order, exactly as the model fund. Its one
  question: does the buying order matter?
* **Sized by conviction** (``sized_by_conviction=True``). Each new position's
  size is the normal size times a factor set by its conviction
  (``CONVICTION_SIZES``). Watchlist order, as production. See
  ``Fund._execute`` for how that is done inside the unchanged engine.

A third, the owner's decision of 26 Sep 2026:

* **Same day** (``entry=SAME_DAY``). Each line is entered on its own
  session, at the price recorded on the journal line when its signal was
  made (its ``live`` record, ``orchestrator/live_price.py``), instead of at
  the next open: a buy at the recorded ask, a short at the recorded bid, or
  at the recorded last trade when that side is missing, plus the same cost.
  The day is the one above with the entries moved: at the open, stops the
  price gapped through and the manager (on the previous cycle, as every
  fund); during the session, the stops of the positions already held;
  THEN the day's own lines, through the same production engine, which sizes
  and stops them on the recorded price (``RecordedQuote``); at the close,
  the marks. So a new position's stop is first checked at the next
  session's open. Its ATR is the production method on the bars known at the
  session's open, as for every fund: daily bars say nothing about the range
  between the open and the moment the signal was made. The rest of the book
  is valued at the session's open when the engine sizes, as at every
  fund's entries. A directional line with no usable recorded price (no
  ``live`` record, one with an ``error``, no positive price for its side,
  or no readable ``asked_at``), recorded outside regular New York hours
  (09:30 to 16:00, 13:00 on a half day; ``shadow.market.in_regular_hours``),
  or recorded on another New York day than its session, is not entered, and
  each is counted by reason (``Fund.not_entered``). Its first cycle is the
  one journalled on its first session: the cycle of the day before, which
  the others enter at that first open, it would have entered the day
  before, outside the sample.

Short refusals are dated
------------------------
A fund is refused a short in a name the paper account was refused one in
(``shadow.run.not_shortable``: name -> the UTC day of its first refusal,
the calendar the cycles are dated on). A refusal counts only from the day it
happened, never backwards: a cycle journalled on day D is blocked only by
refusals recorded on day D or earlier (the owner's decision of 26 Sep 2026),
so a new refusal can never change a past result. A plain set of names, with
no day, is refused from the start.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from collections import Counter
from datetime import date, datetime, timezone
from itertools import groupby
from typing import Callable, Final, Iterable, Mapping, Optional, Sequence, Union
from zoneinfo import ZoneInfo

from analysis.reader import JournalEntry
from app import risk_engine
from app.execution_engine import ExecutionEngine
from app.position_manager import PositionManager
from app.schemas import Bias, ExecutionResult, ExecutionStatus, LLMSignal
from config.watchlist import DEFAULT_WATCHLIST
from shadow.audit import FundAudit
from shadow.broker import DEFAULT_COST_PER_SIDE, SimBroker
from shadow.market import Bars, SimFeed, in_regular_hours

STARTING_CASH = 100_000.0

#: A signal maker: one journal line in, the fund's call on it out (or None).
SignalFor = Callable[["Line"], Optional[LLMSignal]]


@dataclass(frozen=True)
class Line:
    """One journal line every fund may act on."""

    ticker: str
    #: The cycle day (UTC) the line was journalled on.
    day: date
    #: 1 for the day's first cycle, 2 for a second one, ...
    cycle: int
    entry: JournalEntry


_ORDER = {ticker: i for i, ticker in enumerate(DEFAULT_WATCHLIST)}


def dispatch_order(line: Line) -> tuple:
    """Cycle, then watchlist position (unknown tickers last, by name)."""
    return (line.cycle, _ORDER.get(line.ticker, len(_ORDER)), line.ticker)


#: The two buying orders a fund can use. Production's is the watchlist's.
WATCHLIST_FIRST: Final[str] = "watchlist"
CONVICTION_FIRST: Final[str] = "conviction"

#: When a fund enters a cycle's lines: at the next session's open, as the
#: race and every fund but one; or on the line's own session, at the price
#: recorded when its signal was made (the exploratory ``model_same_day``).
NEXT_OPEN: Final[str] = "next_open"
SAME_DAY: Final[str] = "same_day"

#: Why the same-day fund did not enter a directional line.
NO_PRICE: Final[str] = "no recorded price"
OUTSIDE_HOURS: Final[str] = "recorded outside regular hours"
OTHER_DAY: Final[str] = "recorded on another day"
NOT_ENTERED_REASONS: Final[tuple[str, ...]] = (NO_PRICE, OUTSIDE_HOURS, OTHER_DAY)

_NY = ZoneInfo("America/New_York")

#: Refusals as a fund takes them: name -> the day of the first refusal, or
#: a plain set of names refused from the start.
Refusals = Union[Mapping[str, date], Iterable[str]]


def refusal_days(refusals: Refusals) -> dict[str, date]:
    """Name -> the first day a short in it was refused; ``date.min`` for an undated name."""
    if isinstance(refusals, Mapping):
        return {str(t).strip().upper(): d for t, d in refusals.items()}
    return {str(t).strip().upper(): date.min for t in refusals}


def refused_by(refusals: Mapping[str, date], cycle_day: date) -> frozenset[str]:
    """The names a fund acting on ``cycle_day``'s cycle may not short: refused on that day or earlier."""
    return frozenset(t for t, d in refusals.items() if d <= cycle_day)


def _positive(value: object) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if math.isfinite(number) and number > 0 else None


def _moment(value: object) -> Optional[datetime]:
    if not isinstance(value, str) or not value.strip():
        return None
    text = value.strip()
    try:
        moment = datetime.fromisoformat(text[:-1] + "+00:00" if text.endswith(("Z", "z")) else text)
    except ValueError:
        return None
    return moment if moment.tzinfo else moment.replace(tzinfo=timezone.utc)


def recorded_fill(entry: JournalEntry, side: str, session: date) -> tuple[Optional[float], Optional[str]]:
    """The price a same-day entry fills at, from the line's ``live`` record, or why there is none.

    ``side`` is the entry's: "buy" fills at the recorded ask, "sell" (a
    short) at the recorded bid, either at the recorded last trade when that
    side is missing. Returns ``(price, None)``, or ``(None, reason)`` with a
    reason from ``NOT_ENTERED_REASONS``.
    """
    live = entry.live
    if live is None or live.get("error") is not None:
        return None, NO_PRICE
    price = _positive(live.get("ask" if side == "buy" else "bid")) or _positive(live.get("price"))
    asked = _moment(live.get("asked_at"))
    if price is None or asked is None:
        return None, NO_PRICE
    if not in_regular_hours(asked):
        return None, OUTSIDE_HOURS
    if asked.astimezone(_NY).date() != session:
        return None, OTHER_DAY
    return price, None


class RecordedQuote:
    """The shared feed, except for the one line being entered at the price recorded for it.

    The same-day fund's engine, broker and manager read prices through
    this. ``price`` holds at most one ticker, and only while that line is
    dispatched (``Fund._enter``); otherwise every answer is the feed's own.
    """

    def __init__(self, feed: SimFeed) -> None:
        self._feed = feed
        self.price: dict[str, float] = {}

    def get_latest_price(self, ticker: str) -> float:
        recorded = self.price.get(ticker.strip().upper())
        return recorded if recorded is not None else self._feed.get_latest_price(ticker)

    def get_atr(self, ticker: str) -> float:
        return self._feed.get_atr(ticker)

    def __getattr__(self, name: str):
        return getattr(self._feed, name)


def by_conviction(signals: Sequence[tuple[Line, Optional[LLMSignal]]]) -> list[tuple[Line, Optional[LLMSignal]]]:
    """Lines, cycle by cycle, highest conviction first within each cycle.

    ``sorted`` is stable, so lines of equal conviction keep the order they
    came in -- watchlist order. A line with no signal is dispatched to
    nothing, so where it goes does not matter; it goes last.

    The fund uses this only on a cycle that watchlist order would run out of
    room in (``Fund._short_of_room``), which is the owner's rule. Sorting
    every cycle would not be the same thing, though it looks it. The
    stock-market limit is on the net, longs less shorts, so a short
    dispatched first makes room for a long after it. By conviction that long
    can come first and be cut short, on a day watchlist order had room for
    every line.
    """
    def key(pair: tuple[Line, Optional[LLMSignal]]) -> tuple:
        line, signal = pair
        return (line.cycle, -signal.conviction if signal is not None else math.inf)

    return sorted(signals, key=key)


#: Fund 6's sizes (the owner's decision of 25 Sep 2026): from each
#: conviction up to the next, the normal size times this factor. Below the
#: first nothing reaches sizing -- the engine's conviction floor refuses it.
CONVICTION_SIZES: Final[tuple[tuple[float, float], ...]] = ((0.30, 0.25), (0.40, 0.5), (0.50, 1.0), (0.60, 1.5))


def conviction_factor(conviction: float) -> Optional[float]:
    """The size factor for a conviction, or None below the table.

    Compared at six decimals, so a conviction of 0.4 that arrives as
    0.39999999 is read as the 0.4 the model said, not the band below it.
    """
    value = round(float(conviction), 6)
    for floor, factor in reversed(CONVICTION_SIZES):
        if value >= floor:
            return factor
    return None


def lines_by_day(entries: Iterable[JournalEntry]) -> dict[date, list[Line]]:
    """Every actionable line, grouped by cycle day, in dispatch order."""
    by_day: dict[date, list[Line]] = {}
    seen: dict[tuple[date, str], int] = {}
    for entry in entries:
        if entry.timestamp is None:
            continue
        day = _utc_day(entry)
        key = (day, entry.ticker)
        # A ticker's n-th line of the day is from the day's n-th cycle,
        # whether or not that line is kept -- a held or failed first-cycle
        # line still means the next one is the second cycle's, and must not
        # be dispatched ahead of the other tickers' first-cycle lines.
        seen[key] = seen.get(key, 0) + 1
        # The race's own rule: held names and names the model gave no answer
        # on -- a failed call, or an answer about another ticker -- leave
        # every fund that day.
        if entry.held or not entry.model_answered:
            continue
        by_day.setdefault(day, []).append(Line(entry.ticker, day, seen[key], entry))
    return {day: sorted(lines, key=dispatch_order) for day, lines in sorted(by_day.items())}


def cycle_days(entries: Iterable[JournalEntry]) -> set[date]:
    """Every day a cycle ran at all -- answered, failed or held lines alike."""
    return {_utc_day(e) for e in entries if e.timestamp is not None}


def _utc_day(entry: JournalEntry) -> date:
    stamp = entry.timestamp
    return stamp.astimezone(timezone.utc).date() if stamp.tzinfo else stamp.date()


# --------------------------------------------------------------------------- #
# What each fund says on a line
# --------------------------------------------------------------------------- #


def model_signal(line: Line) -> Optional[LLMSignal]:
    """The model fund: the journal's own answer, bias and conviction only."""
    entry = line.entry
    try:
        return LLMSignal(ticker=entry.ticker, bias=Bias(entry.bias), conviction=float(entry.conviction),
                         rationale="journal")
    except (ValueError, TypeError):
        return None


def rule_signal(name: str) -> SignalFor:
    """A rule fund: the arm recomputed from the line's own technicals, as the race does."""
    from analysis.horse_race import seen_on
    from rules import ARMS

    arm = ARMS[name]

    def signal(line: Line) -> Optional[LLMSignal]:
        return arm(seen_on(line.entry))

    return signal


def coin_signal(seed: int) -> SignalFor:
    """A coin-flip fund: ``rules.control`` with one seed, on every line."""
    from rules import control

    def signal(line: Line) -> Optional[LLMSignal]:
        return control.signal_for(line.ticker, line.day, seed=seed)

    return signal


# --------------------------------------------------------------------------- #
# The fund
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Day:
    """One session's close."""

    day: date
    equity: float
    cash: float
    gross: float
    positions: int


@dataclass(frozen=True)
class Decision:
    """The engine's answer to one line, as the fund dispatched it."""

    session: date
    cycle_day: date
    ticker: str
    bias: str
    conviction: float
    status: str             # ACCEPTED, REJECTED or ERROR
    reason: str
    #: False when the fund already held the ticker and never dispatched it.
    dispatched: bool = True


@dataclass
class Tally:
    """What the engine and the manager did, for integrity checks and the report."""

    accepted: int = 0
    rejected: int = 0
    errors: int = 0
    unexpected: list[str] = field(default_factory=list)
    manager_errors: list[str] = field(default_factory=list)
    estimated_r: int = 0
    #: A ticker the price source has no bar for on a session every other
    #: ticker trades: the manager left that position as it was and no entry
    #: was made in it that day. A gap in the data, not a fault of the
    #: machinery -- and counted only when the bars really lack that day, so
    #: a fault that says "no bar" is never excused by the word.
    data_holes: list[str] = field(default_factory=list)


class Fund:
    """A book run by the production engine and manager. See the module docstring."""

    def __init__(
        self, name: str, signal_for: SignalFor, feed: SimFeed, bars: Bars, *,
        cash: float = STARTING_CASH, cost_per_side: float = DEFAULT_COST_PER_SIDE,
        not_shortable: Refusals = frozenset(), keep_actions: bool = False, order_detail: bool = True,
        priority: str = WATCHLIST_FIRST, sized_by_conviction: bool = False, entry: str = NEXT_OPEN,
    ) -> None:
        if priority not in (WATCHLIST_FIRST, CONVICTION_FIRST):
            raise ValueError(f"priority must be {WATCHLIST_FIRST!r} or {CONVICTION_FIRST!r}, got {priority!r}")
        if entry not in (NEXT_OPEN, SAME_DAY):
            raise ValueError(f"entry must be {NEXT_OPEN!r} or {SAME_DAY!r}, got {entry!r}")
        if entry == SAME_DAY and priority != WATCHLIST_FIRST:
            raise ValueError("a same-day fund dispatches in watchlist order")
        self.name = name
        self.signal_for = signal_for
        self.bars = bars
        #: The buying order within a cycle. Every fund but the exploratory
        #: "highest conviction first" one uses production's: watchlist order;
        #: that one too, on a cycle watchlist order has room for.
        self.priority = priority
        #: The exploratory "sized by conviction" fund only: see ``_execute``.
        self.sized_by_conviction = sized_by_conviction
        #: When this fund enters a cycle's lines (``NEXT_OPEN`` or ``SAME_DAY``).
        self.entry = entry
        #: Name -> the day of the paper account's first refusal to short it.
        #: The broker is refused the names refused by the day of the cycle
        #: being dispatched, set in ``_enter``; until then, every name.
        self.refused_on = refusal_days(not_shortable)
        #: The same-day fund's prices: the feed's, but the recorded price for
        #: the line being entered. Every other fund reads the feed itself.
        self.quotes: Optional[RecordedQuote] = RecordedQuote(feed) if entry == SAME_DAY else None
        feed = self.quotes if self.quotes is not None else feed
        self.broker = SimBroker(name=name, cash=cash, quote=feed.get_latest_price,
                                cost_per_side=cost_per_side, not_shortable=frozenset(self.refused_on))
        self.audit = FundAudit(name, keep_actions=keep_actions)
        self.engine = ExecutionEngine(self.broker, feed, audit_logger=self.audit.logger)
        self.manager = PositionManager(self.broker, feed, audit_path=self.audit,
                                       audit_logger=self.audit.logger)
        self.days: list[Day] = []
        self.tally = Tally()
        #: Every line's outcome, kept only when asked for (``keep_actions``):
        #: calibration explains a differing trade with it.
        self.decisions: Optional[list[Decision]] = [] if keep_actions else None
        #: For the owner's order report (``shadow.order_matters``): every
        #: order the engine accepted and every signal a portfolio limit
        #: refused, dated by the cycle day whose list it was. Other refusals
        #: are not kept -- a thousand funds would carry every NEUTRAL. A fund
        #: with ``order_detail`` off (the coin-flip funds, which are never
        #: NEUTRAL and so meet a limit nearly every day) keeps only the days.
        self.order_events: Optional[list] = [] if order_detail else None
        self.order_days_seen: set = set()
        #: Cycles in which at least one signal was dispatched.
        self.cycles_dispatched = 0
        #: The same-day fund only: directional lines it did not enter, by
        #: reason (``NOT_ENTERED_REASONS``).
        self.not_entered: Counter = Counter()

    def session(self, day: date, cycle: Optional[Sequence[Line]], manage: bool = True,
                today: Optional[Sequence[Line]] = None) -> Day:
        """One session. ``cycle`` is the previous day's lines, or None if none ran.

        ``manage`` is for the calibration copy alone: False when the real
        account's own management pass for that cycle was skipped because
        the market was closed, so the copy skips it too
        (``shadow.calibration``, "Late runs"). Every fund leaves it at True,
        and then a session is exactly what it always was.

        ``today`` is this session's own lines, or None if no cycle ran
        today: read by the same-day fund alone, which enters them after the
        session's stops (see the module docstring). Every other fund enters
        ``cycle`` at the open and ignores it.
        """
        broker = self.broker
        broker.day = day
        held_at_open = broker.held_quantities()
        opens, lows, highs, closes, dividends = {}, {}, {}, {}, {}
        for ticker in sorted(set(held_at_open) | {line.ticker for line in cycle or ()}):
            bar = self.bars.bar(ticker, day)
            if bar is None:
                continue
            opens[ticker], highs[ticker], lows[ticker], closes[ticker], dividends[ticker] = bar

        broker.fill_gapped_stops(opens)
        if cycle is not None:
            if manage:
                self._manage()
            if self.entry == NEXT_OPEN:
                self._enter(cycle)
        # New positions' bars, for their stops and marks.
        for ticker in sorted(broker.positions):
            if ticker not in closes:
                bar = self.bars.bar(ticker, day)
                if bar is not None:
                    opens[ticker], highs[ticker], lows[ticker], closes[ticker], dividends[ticker] = bar
        broker.fill_touched_stops(lows, highs)
        if self.entry == SAME_DAY and today is not None:
            # After the session's stops: a new position's stop is first
            # checked at the next open. Its bar is read for the close's mark.
            self._enter(today, recorded=True)
            for ticker in sorted(broker.positions):
                if ticker not in closes:
                    bar = self.bars.bar(ticker, day)
                    if bar is not None:
                        opens[ticker], highs[ticker], lows[ticker], closes[ticker], dividends[ticker] = bar
        broker.pay_dividends({t: d for t, d in dividends.items() if d}, held_at_open)
        broker.remember_marks(closes)
        record = Day(day, broker.equity(closes), broker.cash, broker.gross(closes), len(broker.positions))
        self.days.append(record)
        return record

    def _hole(self, ticker: str, reason: str) -> bool:
        """The error is the feed's "no bar", and the bars do lack that ticker today."""
        return "no bar for" in reason and self.bars.bar(ticker, self.broker.day) is None

    def _manage(self) -> None:
        report = self.manager.manage()
        for action in report.actions:
            if action.action == "error":
                if self._hole(action.ticker, action.reason):
                    self.tally.data_holes.append(f"{self.broker.day.isoformat()} {action.ticker}: no bar; "
                                                 f"the manager left the position as it was")
                else:
                    self.tally.manager_errors.append(f"{action.ticker}: {action.reason}")
            if action.r_estimated:
                self.tally.estimated_r += 1

    def _enter(self, cycle: Sequence[Line], recorded: bool = False) -> None:
        """Dispatch a cycle's lines; ``recorded``: the same-day fund, each at its recorded price."""
        from shadow.order_matters import Event, capacity_kind

        dispatched = False
        signals = [(line, self.signal_for(line)) for line in cycle]
        refused_for: Optional[date] = None
        # One journal cycle at a time (``lines_by_day`` hands them over cycle
        # by cycle), so that the "highest conviction first" fund chooses each
        # cycle's order on the book the cycles before it left. For every
        # other fund this is the list as it came, in the order it came.
        for _, batch in groupby(signals, key=lambda pair: pair[0].cycle):
            batch = list(batch)
            if batch[0][0].day != refused_for:
                # Dated refusals: only those recorded on the cycle's day or before.
                refused_for = batch[0][0].day
                self.broker.not_shortable = refused_by(self.refused_on, refused_for)
            if self.priority == CONVICTION_FIRST and self._short_of_room(batch):
                batch = by_conviction(batch)
            for line, signal in batch:
                # Held is read at dispatch, whatever the order: a name bought
                # earlier in this list is held by the time a later line reaches it.
                if line.ticker in self.broker.positions:        # SKIP_HELD_TICKERS
                    if self.decisions is not None and signal is not None:
                        self.decisions.append(Decision(self.broker.day, line.day, line.ticker,
                                                       signal.bias.value, signal.conviction, "SKIPPED",
                                                       "already held", False))
                    continue
                if signal is None:
                    continue
                if recorded and signal.bias is not Bias.NEUTRAL:
                    price, why = recorded_fill(line.entry, "buy" if signal.bias is Bias.BULLISH else "sell",
                                               self.broker.day)
                    if why is not None:
                        self.not_entered[why] += 1
                        if self.decisions is not None:
                            self.decisions.append(Decision(self.broker.day, line.day, line.ticker,
                                                           signal.bias.value, signal.conviction, "SKIPPED",
                                                           why, False))
                        continue
                    self.quotes.price[line.ticker] = price
                    try:
                        result, cap = self._execute(signal)
                    finally:
                        self.quotes.price.clear()
                else:
                    result, cap = self._execute(signal)
                dispatched = True
                accepted = result.status is ExecutionStatus.ACCEPTED
                kind = None if accepted else capacity_kind(result.reason, cap)
                if kind is not None:
                    self.order_days_seen.add(line.day)
                if self.order_events is not None and (accepted or kind is not None):
                    self.order_events.append(Event(line.day, line.ticker, signal.conviction,
                                                   result.status.value, "", kind))
                if self.decisions is not None:
                    self.decisions.append(Decision(self.broker.day, line.day, line.ticker, signal.bias.value,
                                                   signal.conviction, result.status.value, result.reason))
                if result.status is ExecutionStatus.ACCEPTED:
                    self.tally.accepted += 1
                elif result.status is ExecutionStatus.ERROR:
                    self.tally.errors += 1
                    if result.reason.startswith("unexpected"):
                        self.tally.unexpected.append(f"{line.ticker}: {result.reason}")
                    elif self._hole(line.ticker, result.reason):
                        self.tally.data_holes.append(f"{self.broker.day.isoformat()} {line.ticker}: no bar; "
                                                     f"no entry that day")
                else:
                    self.tally.rejected += 1
        self.cycles_dispatched += dispatched

    def _short_of_room(self, batch: Sequence[tuple[Line, Optional[LLMSignal]]]) -> bool:
        """Would this cycle, dispatched in watchlist order, run out of room?

        Asked of a copy of the book (``SimBroker.scratch``) and an engine
        built on it, whose audit record is thrown away, so the fund itself is
        exactly as it was. The feed is only read. The copy is dispatched just
        as ``_enter`` would: held names skipped, each signal seeing the
        fills before it.

        "Out of room" is a signal a portfolio limit refused (the order
        report's own test, ``capacity_kind``: a group, the sleeve, the
        gross, the stock-market limit, the position count or cash), or one
        a limit cut short of what its own cap alone would have bought.
        Either way the list held more than the book could take, and its
        order decided who got what. A signal refused for any other reason,
        or bought at its own cap's full size, is not a lack of room.
        """
        from shadow.order_matters import capacity_kind

        book = self.broker.scratch()
        engine = ExecutionEngine(book, self.engine.market_data,
                                 audit_logger=FundAudit(f"{self.name}.trial").logger)
        for line, signal in batch:
            if signal is None or line.ticker in book.positions:
                continue
            result, cap = self._execute(signal, engine)
            if result.status is ExecutionStatus.ACCEPTED:
                own_cap = cap if cap is not None else risk_engine.max_position_pct_for(signal.ticker)
                alone = risk_engine.calculate_position_size(equity=result.equity, price=result.entry_price,
                                                            max_position_pct=own_cap)
                if result.quantity < alone:
                    return True
            elif capacity_kind(result.reason, cap) is not None:
                return True
        return False

    def _execute(self, signal: LLMSignal,
                 engine: Optional[ExecutionEngine] = None) -> tuple[ExecutionResult, Optional[float]]:
        """The production engine's answer to one signal, and the cap it was sized under if this fund scaled it.

        Every fund but one calls the engine as it is. The "sized by
        conviction" fund changes the one number that sets a position's normal
        size: the per-ticker cap. There is no other size budget in this
        system -- the ATR sets only the stop -- and the engine reads the cap
        in one place, ``risk_engine.max_position_pct_for(signal.ticker)``,
        once per new entry, just before ``calculate_position_size``. So for
        the length of this one call, and only this fund's, that function
        returns the ticker's own cap times the signal's conviction factor,
        and the original is put back in ``finally``, whatever happens.
        Everything the engine checks before sizing -- the conviction floor,
        the position count, the gross, sleeve, exposure-group and
        stock-market limits -- is computed as for any fund and still bounds
        the size; the position manager is untouched, and its ladder tranches
        are fractions of the position, so they scale with it. The engine
        never learns it was run differently, and nothing in ``app/`` changes.

        The run is one process working through its funds one at a time, so
        no other fund's engine can run while the cap is scaled.

        ``engine`` is the fund's own unless ``_short_of_room`` is trying the
        cycle on a copy of the book.
        """
        engine = engine if engine is not None else self.engine
        factor = conviction_factor(signal.conviction) if self.sized_by_conviction else None
        if factor is None:
            return engine.execute(signal), None
        normal = risk_engine.max_position_pct_for
        applied: list[float] = []

        def scaled(ticker: str) -> float:
            cap = normal(ticker) * factor
            # calculate_position_size refuses a cap outside (0, 1] as a risk
            # violation, which the tally would read as an ordinary refusal.
            # Raised here it is an "unexpected" error: an integrity problem.
            if not 0.0 < cap <= 1.0:
                raise ValueError(f"{ticker}: cap {normal(ticker)} x {factor} is {cap}, outside (0, 1]")
            applied.append(cap)
            return cap

        risk_engine.max_position_pct_for = scaled
        try:
            result = engine.execute(signal)
        finally:
            risk_engine.max_position_pct_for = normal
        return result, (applied[-1] if applied else None)


class IndexFund:
    """VT, bought once at the first open with all the cash, and held.

    Not through the engine: the engine would size VT as one equity at 5% of
    the book and put a stop under it, which is not "hold the index". Same
    cost per side on the one purchase, same bars, dividends credited on the
    ex-date -- the treatment the race's index test registers.
    """

    def __init__(self, name: str, ticker: str, bars: Bars, *, cash: float = STARTING_CASH,
                 cost_per_side: float = DEFAULT_COST_PER_SIDE) -> None:
        self.name = name
        self.ticker = ticker
        self.bars = bars
        self.cash = cash
        self.cost_per_side = cost_per_side
        self.qty = 0
        self.bought: Optional[date] = None
        self.days: list[Day] = []
        self.tally = Tally()

    def session(self, day: date, cycle: Optional[Sequence[Line]] = None) -> Day:
        bar = self.bars.bar(self.ticker, day)
        if bar is None:
            last = self.days[-1] if self.days else Day(day, self.cash, self.cash, 0.0, 0)
            record = Day(day, last.equity, self.cash, last.gross, 1 if self.qty else 0)
            self.days.append(record)
            return record
        opened, _, _, close, dividend = bar
        held = self.qty
        if self.bought is None:
            self.qty = math.floor(self.cash / (opened * (1 + self.cost_per_side)))
            self.cash -= self.qty * opened * (1 + self.cost_per_side)
            self.bought = day
            self.tally.accepted = 1
        if dividend and held:
            self.cash += held * dividend
        record = Day(day, self.cash + self.qty * close, self.cash, self.qty * close, 1 if self.qty else 0)
        self.days.append(record)
        return record


def run(
    funds: Sequence, sessions: Sequence[date], cycles: dict[date, list[Line]],
    ran: set[date], feed: SimFeed, previous: Optional[date] = None,
) -> None:
    """Every fund through every session, the feed's clock moved once per session.

    ``cycles`` maps a cycle day to its actionable lines; ``ran`` is every
    cycle day at all. A session acts on the cycle of the session before it;
    the first session on the cycle of ``previous``, when one is given (the
    fund test's first cycle, 2026-09-28, acted on at the 2026-09-29 open).
    A same-day fund (``SAME_DAY``) is also handed the session's own cycle.
    """
    from shadow.audit import live_audit_guarded

    with live_audit_guarded():
        for session in sessions:
            feed.at_open(session)
            cycle: Optional[list[Line]] = None
            if previous is not None and previous in ran:
                cycle = cycles.get(previous, [])
            today = cycles.get(session, []) if session in ran else None
            for fund in funds:
                if getattr(fund, "entry", NEXT_OPEN) == SAME_DAY:
                    fund.session(session, cycle, today=today)
                else:
                    fund.session(session, cycle)
            previous = session


__all__ = [
    "CONVICTION_FIRST", "CONVICTION_SIZES", "Day", "Decision", "Fund", "IndexFund", "Line", "NEXT_OPEN",
    "NOT_ENTERED_REASONS", "NO_PRICE", "OTHER_DAY", "OUTSIDE_HOURS", "RecordedQuote", "Refusals", "SAME_DAY",
    "STARTING_CASH", "Tally", "WATCHLIST_FIRST", "by_conviction", "coin_signal", "conviction_factor",
    "cycle_days", "dispatch_order", "lines_by_day", "model_signal", "recorded_fill", "refusal_days",
    "refused_by", "rule_signal", "run",
]
