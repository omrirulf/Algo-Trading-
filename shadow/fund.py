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
lines dispatched take the room. Every fund uses the one rule production
uses: **watchlist order** (``config.watchlist.DEFAULT_WATCHLIST``), one
signal at a time, each seeing the fills before it. Production has no other
rule -- there is no sort by conviction anywhere on the dispatch path -- and
a calibration fund dispatching in any other order would differ from the
real account for that reason alone. A day with two cycles is dispatched
cycle by cycle, each in watchlist order; a second same-side entry in a
ticker on one day is refused by the broker, as live.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from datetime import date, timezone
from typing import Callable, Iterable, Optional, Sequence

from analysis.reader import JournalEntry
from app.execution_engine import ExecutionEngine
from app.position_manager import PositionManager
from app.schemas import Bias, ExecutionStatus, LLMSignal
from config.watchlist import DEFAULT_WATCHLIST
from shadow.audit import FundAudit
from shadow.broker import DEFAULT_COST_PER_SIDE, SimBroker
from shadow.market import Bars, SimFeed

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


class Fund:
    """A book run by the production engine and manager. See the module docstring."""

    def __init__(
        self, name: str, signal_for: SignalFor, feed: SimFeed, bars: Bars, *,
        cash: float = STARTING_CASH, cost_per_side: float = DEFAULT_COST_PER_SIDE,
        not_shortable: frozenset[str] = frozenset(), keep_actions: bool = False,
    ) -> None:
        self.name = name
        self.signal_for = signal_for
        self.bars = bars
        self.broker = SimBroker(name=name, cash=cash, quote=feed.get_latest_price,
                                cost_per_side=cost_per_side, not_shortable=not_shortable)
        self.audit = FundAudit(name, keep_actions=keep_actions)
        self.engine = ExecutionEngine(self.broker, feed, audit_logger=self.audit.logger)
        self.manager = PositionManager(self.broker, feed, audit_path=self.audit,
                                       audit_logger=self.audit.logger)
        self.days: list[Day] = []
        self.tally = Tally()
        #: Every line's outcome, kept only when asked for (``keep_actions``):
        #: calibration explains a differing trade with it.
        self.decisions: Optional[list[Decision]] = [] if keep_actions else None

    def session(self, day: date, cycle: Optional[Sequence[Line]]) -> Day:
        """One session. ``cycle`` is the previous day's lines, or None if none ran."""
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
            self._manage()
            self._enter(cycle)
        # New positions' bars, for their stops and marks.
        for ticker in sorted(broker.positions):
            if ticker not in closes:
                bar = self.bars.bar(ticker, day)
                if bar is not None:
                    opens[ticker], highs[ticker], lows[ticker], closes[ticker], dividends[ticker] = bar
        broker.fill_touched_stops(lows, highs)
        broker.pay_dividends({t: d for t, d in dividends.items() if d}, held_at_open)
        broker.remember_marks(closes)
        record = Day(day, broker.equity(closes), broker.cash, broker.gross(closes), len(broker.positions))
        self.days.append(record)
        return record

    def _manage(self) -> None:
        report = self.manager.manage()
        for action in report.actions:
            if action.action == "error":
                self.tally.manager_errors.append(f"{action.ticker}: {action.reason}")
            if action.r_estimated:
                self.tally.estimated_r += 1

    def _enter(self, cycle: Sequence[Line]) -> None:
        for line in cycle:
            signal = self.signal_for(line)
            if line.ticker in self.broker.positions:        # SKIP_HELD_TICKERS
                if self.decisions is not None and signal is not None:
                    self.decisions.append(Decision(self.broker.day, line.day, line.ticker, signal.bias.value,
                                                   signal.conviction, "SKIPPED", "already held", False))
                continue
            if signal is None:
                continue
            result = self.engine.execute(signal)
            if self.decisions is not None:
                self.decisions.append(Decision(self.broker.day, line.day, line.ticker, signal.bias.value,
                                               signal.conviction, result.status.value, result.reason))
            if result.status is ExecutionStatus.ACCEPTED:
                self.tally.accepted += 1
            elif result.status is ExecutionStatus.ERROR:
                self.tally.errors += 1
                if result.reason.startswith("unexpected"):
                    self.tally.unexpected.append(f"{line.ticker}: {result.reason}")
            else:
                self.tally.rejected += 1


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
    ran: set[date], feed: SimFeed,
) -> None:
    """Every fund through every session, the feed's clock moved once per session.

    ``cycles`` maps a cycle day to its actionable lines; ``ran`` is every
    cycle day at all. A session acts on the cycle of the session before it.
    """
    from shadow.audit import live_audit_guarded

    previous: Optional[date] = None
    with live_audit_guarded():
        for session in sessions:
            feed.at_open(session)
            cycle: Optional[list[Line]] = None
            if previous is not None and previous in ran:
                cycle = cycles.get(previous, [])
            for fund in funds:
                fund.session(session, cycle)
            previous = session


__all__ = [
    "Day", "Decision", "Fund", "IndexFund", "Line", "STARTING_CASH", "Tally", "coin_signal", "cycle_days",
    "dispatch_order", "lines_by_day", "model_signal", "rule_signal", "run",
]
