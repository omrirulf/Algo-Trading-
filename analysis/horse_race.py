"""Three arms, the same lines, the same realised returns, after costs.

    python analysis/horse_race.py
    python analysis/horse_race.py --horizon 5 --floor 0.5 --cost-per-side 0.0015
    python analysis/horse_race.py --per-trade

Arm A is the model: whatever the journal says it said. Arm B is the coded
thesis in ``rules/momentum.py``, recomputed here from the technicals every
line already carries. Arm C is the coin flip in ``rules/control.py``,
recomputed the same way. Each is put through the identical floor, the
identical stop and sizing arithmetic, the identical round-trip cost, and
scored against the identical price history -- so the only thing that
differs between the rows is the judgement, and the coin flip is what "no
judgement" scores.

What a number here means
------------------------
* **net return** is a trade's return through the real stop and sizing
  (``backtest.simulate.simulate_trade``), minus a fixed round-trip cost
  applied to every trade of every arm alike.
* **hit** is a trade whose net return is strictly greater than zero.
* **daily return** is the equal-weighted mean net return of the trades an
  arm opened on one entry day; a day it opened none is 0. This is the
  primary series, because trades opened on the same day share the same
  three sessions of market and are one observation, not several.
* **final closes only**: every price source is truncated to the last
  session whose bar is final at the moment the race runs, so a trade whose
  exit bar is still being traded is pending, never scored on an intraday
  print. Two runs on the same journal agree on every resolved trade.

The primary test is the paired difference, model minus momentum, day by
day, with a Newey-West standard error at lag = horizon (the overlap the
horizon creates) and, as a check, the plain t on every h-th day only.

Every arm is offered exactly the same lines. Two kinds are offered to no
arm: a ticker already in the book, where the model was never asked and a
rule holding the same book would not have been either; and a line where
the model gave no answer at all -- a timeout or a failed call -- which is
dropped for every arm alike (Amendment 2026-09-24, a bug fix: counting it
as a day the rules traded and the model sat out compared the arms on
different lines). Before 2026-09-23 a cheap screen answered NEUTRAL on the
names it did not escalate; those lines are the model's NEUTRAL, because the
funnel was the design then. Since 2026-09-23 the screen is off.

The decision is taken on the decision window only -- lines journalled on
or after ``decision_gate.DECISION_CUTOFF`` -- at the planned looks, with
the bars and the index-first rule in ``analysis/decision_gate.py``. The
whole journal is printed after it, for reading.

Nothing here is fitted. The momentum arm's parameters are the textbook
values and this file never touches them; it judges the rule, it does not
tune it. Read-only in every direction -- it reads the journal, fetches
prices, and prints.
"""

from __future__ import annotations

import argparse
import json
import logging
import math
import statistics
import sys
from collections import Counter
from dataclasses import dataclass, replace
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Optional, Sequence

# Allow ``python analysis/horse_race.py`` from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis import decision_gate as gate  # noqa: E402
from analysis.baseline_compare import (  # noqa: E402
    OhlcFetcher,
    simulate_model_trades,
    watchlist_buy_and_hold,
)
from analysis.metrics import ScoredSignal  # noqa: E402
from analysis.reader import JournalEntry, JournalRead, read_journal  # noqa: E402
from analysis.returns import (  # noqa: E402
    ENTRY_AUTO,
    ENTRY_RULES,
    PriceSource,
    YFinancePriceSource,
    last_final_session,
)
from analysis.scoring import score_entries  # noqa: E402
from backtest.simulate import Trade  # noqa: E402
from backtest.sweep import MIN_TRADES  # noqa: E402
from config import settings as cfg  # noqa: E402
from config.instruments import FUNDS, SINGLE_NAMES, is_fund  # noqa: E402
from config.watchlist import DEFAULT_WATCHLIST  # noqa: E402
from orchestrator.insiders import InsiderSnapshot  # noqa: E402
from orchestrator.technicals import TechnicalSnapshot  # noqa: E402
from rules import ARMS, EXPLORATORY, MAIN_ARMS, Seen, control, hybrid, insider_buying, momentum  # noqa: E402

DEFAULT_HORIZON = 3

#: Per side, as a fraction of notional: 0.10% each way, 0.20% a round trip.
#: Applied identically to every trade of every arm. The number is a
#: pre-registered assumption, not a measurement of this broker.
DEFAULT_COST_PER_SIDE = 0.001

#: Coin flips drawn per line to put a band around "no information".
DEFAULT_SEEDS = 1000
#: The coin-flip band. Its top is keep-rule condition 3, so it is the
#: registered percentile and nothing else.
BAND = (100.0 - gate.COIN_FLIP_PERCENTILE, gate.COIN_FLIP_PERCENTILE)

#: Arm A's name in the report. The rule arms report under their own.
MODEL_ARM = "model"

#: Report order of the main tables. The model first because it is the
#: incumbent; the coin flip last because it is the floor everything above it
#: has to clear. Exploratory arms are not in here: they are raced apart,
#: on their own lines only.
ARM_ORDER = (MODEL_ARM, *MAIN_ARMS)

#: The two comparisons the pre-registration decides on, model first.
PAIRED = ((MODEL_ARM, momentum.NAME), (MODEL_ARM, hybrid.NAME))

#: The second horizon an exploratory arm is scored at: the insider effect is
#: measured in months in the literature, and a three-session test alone
#: would test the wrong thing.
EXPLORATORY_HORIZON = 20

#: An exploratory arm reports "too few" below this many scored trades on
#: this many distinct entry days. Pre-registered; not a decision threshold.
EXPLORATORY_MIN_TRADES = 20
EXPLORATORY_MIN_DAYS = 20

#: The two halves of the watchlist, raced separately as well as together:
#: a fund has no analysts, insiders or earnings, so a model reading all of
#: those may behave differently on the two.
GROUPS = ("all", "funds", "companies")

log = logging.getLogger("horse_race")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="horse_race",
        description="Race the model against the coded rule and a coin flip on realised returns.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH,
                        help="path to the signal journal (default: %(default)s)")
    parser.add_argument("--horizon", type=int, default=DEFAULT_HORIZON,
                        help="trading sessions held after entry (default: %(default)s)")
    parser.add_argument("--entry", choices=ENTRY_RULES, default=ENTRY_AUTO,
                        help="which close resolves a signal (default: %(default)s)")
    parser.add_argument("--floor", type=float, default=cfg.MIN_CONVICTION,
                        help="conviction floor applied to EVERY arm alike (default: %(default)s)")
    parser.add_argument("--cost-per-side", type=float, default=DEFAULT_COST_PER_SIDE,
                        help="cost per side as a fraction of notional, charged to every trade of "
                             "every arm (default: %(default)s, i.e. 0.10%% each way)")
    parser.add_argument("--seeds", type=int, default=DEFAULT_SEEDS,
                        help="coin flips drawn per line for the random band (default: %(default)s)")
    parser.add_argument("--equity", type=float, default=100_000.0)
    parser.add_argument("--stop-multiplier", type=float, default=cfg.ATR_STOP_MULTIPLIER)
    parser.add_argument("--max-position-pct", type=float, default=cfg.MAX_POSITION_PCT)
    parser.add_argument("--per-trade", action="store_true",
                        help="also list every scored trade of every arm")
    parser.add_argument("--gate-json", action="store_true",
                        help="print only the decision gate, as JSON (for the dashboard), and stop")
    parser.add_argument("-v", "--verbose", action="store_true", help="log fetch failures")
    return parser


def _now() -> datetime:
    """The clock, in one place, so a test can move it."""
    return datetime.now(timezone.utc)


# --------------------------------------------------------------------------- #
# Which lines, and what each arm said on them
# --------------------------------------------------------------------------- #


def offered(entries: Sequence[JournalEntry]) -> list[JournalEntry]:
    """The lines every arm is asked on: not held, and placeable in time."""
    return [e for e in entries if not e.held and e.timestamp is not None]


def split_answered(lines: Sequence[JournalEntry]) -> tuple[list[JournalEntry], list[JournalEntry]]:
    """The lines the model answered, and the ones it gave no answer on.

    A line with no answer -- the call timed out or failed -- is removed for
    every arm, not only the model (Amendment 2026-09-24, a bug fix). Left in,
    the rules traded it and the model sat it out, so the paired difference
    compared the arms on different lines and charged the model a day in
    cash for an outage. A screened line before 2026-09-23 carries the
    screen's NEUTRAL, which was the funnel's answer, and stays.
    """
    answered = [e for e in lines if e.model_answered]
    return answered, [e for e in lines if not e.model_answered]


def decision_window(lines: Sequence[JournalEntry]) -> list[JournalEntry]:
    """The lines the decision is taken on: journalled on or after the cutoff."""
    return [e for e in lines if gate.in_window(_line_day(e))]


def in_group(entry: JournalEntry, group: str) -> bool:
    if group == "all":
        return True
    return is_fund(entry.ticker) == (group == "funds")


def _line_day(entry: JournalEntry) -> date:
    return entry.timestamp.astimezone(timezone.utc).date()


def entries_for_arm(name: str, lines: Sequence[JournalEntry]) -> list[JournalEntry]:
    """One entry per offered line, carrying this arm's call instead of the model's.

    The model's entries are the lines as journalled, where it produced a
    signal at all. A rule's entries are the same lines with the bias and
    conviction replaced by what the rule says of the technicals on that
    line -- ticker, timestamp and technicals untouched, so the scorer joins
    them to exactly the same forward return.
    """
    if name == MODEL_ARM:
        return [e for e in lines if e.has_signal]
    arm = ARMS[name]
    out: list[JournalEntry] = []
    for entry in lines:
        signal = arm(seen_on(entry))
        out.append(replace(entry, bias=signal.bias.value, conviction=signal.conviction, scores={}, blend={}))
    return out


def seen_on(entry: JournalEntry) -> Seen:
    """What the arms are shown for one journalled line: what the model was."""
    return Seen(
        ticker=entry.ticker,
        day=_line_day(entry),
        technicals=TechnicalSnapshot.from_dict(entry.technicals) if entry.technicals else None,
        insiders=InsiderSnapshot.from_dict(entry.insiders) if entry.insiders else None,
        news_score=entry.scores.get("news_score"),
    )


def direction_agreement(
    a: Sequence[JournalEntry], b: Sequence[JournalEntry]
) -> tuple[Optional[float], int]:
    """Of the lines where both took a side, the share on which they took the same one."""
    calls_a = {(e.ticker, e.timestamp): e.bias for e in a if e.is_directional}
    calls_b = {(e.ticker, e.timestamp): e.bias for e in b if e.is_directional}
    both = [key for key in calls_a if key in calls_b]
    if not both:
        return None, 0
    return sum(1 for key in both if calls_a[key] == calls_b[key]) / len(both), len(both)


@dataclass(frozen=True)
class AgreementDay:
    day: date
    both: int
    agreed_long: int
    agreed_short: int
    disagreed: int


def agreement_breakdown(
    a: Sequence[JournalEntry], b: Sequence[JournalEntry]
) -> list[AgreementDay]:
    """The agreeing lines split into longs and shorts, day by day.

    An agreement rate is only interesting once you know what was agreed
    on: two arms that both say "long" on every name in a rising week agree
    automatically, and the number says nothing about either of them.
    """
    calls_a = {(e.ticker, e.timestamp): e.bias for e in a if e.is_directional}
    calls_b = {(e.ticker, e.timestamp): e.bias for e in b if e.is_directional}
    by_day: dict[date, Counter] = {}
    for key, bias in calls_a.items():
        other = calls_b.get(key)
        if other is None:
            continue
        tally = by_day.setdefault(key[1].astimezone(timezone.utc).date(), Counter())
        tally["both"] += 1
        if bias != other:
            tally["disagreed"] += 1
        elif bias == "BULLISH":
            tally["agreed_long"] += 1
        else:
            tally["agreed_short"] += 1
    return [
        AgreementDay(day, t["both"], t["agreed_long"], t["agreed_short"], t["disagreed"])
        for day, t in sorted(by_day.items())
    ]


# --------------------------------------------------------------------------- #
# Fetching once, for every arm
# --------------------------------------------------------------------------- #


def prewarm(
    lines: Sequence[JournalEntry], source: PriceSource, fetcher: OhlcFetcher,
    horizon: int, today: date,
) -> None:
    """Fetch each ticker once, over the widest window any arm will ask for.

    Both price sources cache by ticker and answer a later, narrower request
    from the first fetch -- so whichever arm ran first would decide how much
    history the others got. Asking for the union up front, before any arm
    runs, is what makes the order of the arms not matter. The windows here
    are exactly the ones score_entries and simulate_model_trades would ask
    for themselves, computed over every offered line rather than one arm's.
    """
    span: dict[str, tuple[date, date]] = {}
    for entry in lines:
        day = _line_day(entry)
        lo, hi = span.get(entry.ticker, (day, day))
        span[entry.ticker] = (min(lo, day), max(hi, day))
    for ticker, (lo, hi) in sorted(span.items()):
        source.closes(ticker, lo, today)
        fetcher.ohlc(ticker, lo, hi + timedelta(days=horizon * 2 + 10))


# --------------------------------------------------------------------------- #
# One scored trade, and the arithmetic over many
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class ScoredTrade:
    """One arm's trade on one line, through the stop, after costs."""

    arm: str
    ticker: str
    #: The journal line's own timestamp, which with the ticker names the line.
    signal_at: datetime
    #: The journal line's own calendar day (UTC).
    signal_day: date
    #: The bar the trade was opened on: the session after the signal bar.
    entry_day: date
    exit_day: date
    fund: bool
    trade: Trade
    cost_per_side: float

    @property
    def key(self) -> tuple[str, datetime]:
        return self.ticker, self.signal_at

    @property
    def gross(self) -> float:
        return self.trade.return_pct

    @property
    def net(self) -> float:
        """Signed return minus the round trip. The number every table uses."""
        return self.gross - 2.0 * self.cost_per_side

    @property
    def hit(self) -> bool:
        """The one definition of a hit: net return strictly above zero."""
        return self.net > 0.0

    @property
    def stopped(self) -> bool:
        return self.trade.stopped_out


def scored_trades(
    arm: str, matched: Sequence[ScoredSignal], trades: Sequence[Trade], cost_per_side: float,
) -> list[ScoredTrade]:
    return [
        ScoredTrade(
            arm=arm, ticker=signal.entry.ticker, signal_at=signal.entry.timestamp,
            signal_day=_line_day(signal.entry),
            entry_day=date.fromisoformat(trade.entry_date), exit_day=date.fromisoformat(trade.exit_date),
            fund=is_fund(signal.entry.ticker), trade=trade, cost_per_side=cost_per_side,
        )
        for signal, trade in zip(matched, trades)
    ]


def hit_rate(trades: Sequence[ScoredTrade]) -> Optional[float]:
    return sum(1 for t in trades if t.hit) / len(trades) if trades else None


def mean_net(trades: Sequence[ScoredTrade]) -> Optional[float]:
    return statistics.fmean(t.net for t in trades) if trades else None


def median_net(trades: Sequence[ScoredTrade]) -> Optional[float]:
    return statistics.median(t.net for t in trades) if trades else None


def stop_rate(trades: Sequence[ScoredTrade]) -> Optional[float]:
    return sum(1 for t in trades if t.stopped) / len(trades) if trades else None


def daily_net(trades: Sequence[ScoredTrade]) -> dict[date, float]:
    """Equal-weighted mean net return of the trades opened on each entry day."""
    by_day: dict[date, list[float]] = {}
    for trade in trades:
        by_day.setdefault(trade.entry_day, []).append(trade.net)
    return {day: statistics.fmean(values) for day, values in sorted(by_day.items())}


def on_grid(daily: dict[date, float], grid: Sequence[date]) -> list[float]:
    """The daily series over a fixed calendar of entry days; no trade is 0."""
    return [daily.get(day, 0.0) for day in grid]


def cumulative(series: Sequence[float]) -> Optional[float]:
    if not series:
        return None
    total = 1.0
    for value in series:
        total *= 1.0 + value
    return total - 1.0


def newey_west_t(xs: Sequence[float], lag: int) -> Optional[float]:
    """t-statistic of the mean with a Newey-West (Bartlett) variance.

    Consecutive daily returns of an arm holding for ``horizon`` sessions
    overlap, so their errors are correlated out to ``lag = horizon`` and a
    plain standard error is too small. ``lag = 0`` is the plain t.
    """
    n = len(xs)
    if n < 2:
        return None
    mean = statistics.fmean(xs)
    e = [x - mean for x in xs]
    var = sum(v * v for v in e) / n
    for k in range(1, min(lag, n - 1) + 1):
        gamma = sum(e[i] * e[i - k] for i in range(k, n)) / n
        var += 2.0 * (1.0 - k / (lag + 1.0)) * gamma
    if var <= 0:
        return None
    return mean / math.sqrt(var / n)


def every_nth(grid: Sequence[date], n: int) -> list[date]:
    """Every ``n``-th entry day from the first: trades that cannot overlap."""
    return list(grid[:: max(1, n)])


def percentile(values: Sequence[float], p: float) -> Optional[float]:
    """Linear-interpolated percentile of a sample, ``p`` in [0, 100]."""
    if not values:
        return None
    ordered = sorted(values)
    rank = (len(ordered) - 1) * p / 100.0
    lo, hi = math.floor(rank), math.ceil(rank)
    if lo == hi:
        return ordered[lo]
    return ordered[lo] + (ordered[hi] - ordered[lo]) * (rank - lo)


def percentile_of(value: Optional[float], values: Sequence[float]) -> Optional[float]:
    """Where ``value`` sits inside ``values``: the share below it, ties split."""
    if value is None or not values:
        return None
    below = sum(1 for v in values if v < value)
    ties = sum(1 for v in values if v == value)
    return 100.0 * (below + 0.5 * ties) / len(values)


# --------------------------------------------------------------------------- #
# Racing one arm
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class ArmResult:
    name: str
    #: Lines the arm was asked on.
    offered: int
    #: Of those, lines where it took a side.
    directional: int
    #: Of the directional lines, below the floor (never a trade).
    below_floor: int
    #: At or above the floor, but the horizon has not elapsed yet.
    pending: int
    #: At or above the floor with a realised close-to-close outcome.
    acted_on: int
    #: Of those, warm-up, cap, missing bars or incomplete horizon in the simulation.
    could_not_simulate: int
    #: The trades that made it through, after costs.
    trades: tuple[ScoredTrade, ...]

    @property
    def n(self) -> int:
        return len(self.trades)

    @property
    def enough(self) -> bool:
        return self.n >= MIN_TRADES

    def in_group(self, group: str) -> list[ScoredTrade]:
        if group == "all":
            return list(self.trades)
        return [t for t in self.trades if t.fund == (group == "funds")]

    @property
    def accounted_for(self) -> bool:
        """offered == neutral + below floor + pending + unresolved + acted_on, by construction."""
        return self.acted_on == self.could_not_simulate + self.n


def race_arm(
    name: str, lines: Sequence[JournalEntry], *, floor: float, horizon: int,
    entry_rule: str, today: date, source: PriceSource, fetcher: OhlcFetcher,
    equity: float, stop_multiplier: float, max_position_pct: float,
    cost_per_side: float = DEFAULT_COST_PER_SIDE,
) -> ArmResult:
    arm_lines = entries_for_arm(name, lines)
    directional = [e for e in arm_lines if e.is_directional]
    above = [e for e in directional if (e.conviction or 0.0) >= floor]
    scored, _ = score_entries(above, source, horizon, entry_rule, today)
    trades, matched, dropped = simulate_model_trades(
        scored, equity=equity, horizon_days=horizon, stop_multiplier=stop_multiplier,
        max_position_pct=max_position_pct, fetcher=fetcher,
    )
    return ArmResult(
        name=name,
        offered=len(arm_lines),
        directional=len(directional),
        below_floor=len(directional) - len(above),
        pending=len(above) - len(scored),
        acted_on=len(scored),
        could_not_simulate=dropped,
        trades=tuple(scored_trades(name, matched, trades, cost_per_side)),
    )


# --------------------------------------------------------------------------- #
# The coin flip, many times over
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class BothSides:
    """One line simulated long and short, so any coin flip on it is a lookup."""

    buy: ScoredTrade
    sell: ScoredTrade


def both_sides(
    lines: Sequence[JournalEntry], *, horizon: int, entry_rule: str, today: date,
    source: PriceSource, fetcher: OhlcFetcher, equity: float, stop_multiplier: float,
    max_position_pct: float, cost_per_side: float,
) -> dict[tuple[str, datetime], BothSides]:
    """Every offered line, traded both ways through the same arithmetic.

    Whether a line can be simulated at all does not depend on the side --
    warm-up, cap and ATR sanity are side-blind -- so a line has both trades
    or neither, and the thousand seeds below never touch the simulator.
    """
    sides: dict[str, dict[tuple[str, datetime], ScoredTrade]] = {}
    for bias in ("BULLISH", "BEARISH"):
        entries = [replace(e, bias=bias, conviction=control.CONVICTION, scores={}, blend={}) for e in lines]
        scored, _ = score_entries(entries, source, horizon, entry_rule, today)
        trades, matched, _ = simulate_model_trades(
            scored, equity=equity, horizon_days=horizon, stop_multiplier=stop_multiplier,
            max_position_pct=max_position_pct, fetcher=fetcher,
        )
        sides[bias] = {t.key: t for t in scored_trades(control.NAME, matched, trades, cost_per_side)}
    return {
        key: BothSides(buy=trade, sell=sides["BEARISH"][key])
        for key, trade in sides["BULLISH"].items()
        if key in sides["BEARISH"]
    }


def flip_trades(
    keys: Sequence[tuple[str, datetime]], sides: dict[tuple[str, datetime], BothSides], seed: int,
) -> list[ScoredTrade]:
    """The coin flip's trades on exactly ``keys``, under one seed."""
    out: list[ScoredTrade] = []
    for ticker, stamp in keys:
        pair = sides.get((ticker, stamp))
        if pair is None:
            continue
        bias = control.signal_for(ticker, stamp.astimezone(timezone.utc).date(), seed=seed).bias.value
        out.append(pair.buy if bias == "BULLISH" else pair.sell)
    return out


@dataclass(frozen=True)
class Band:
    """One metric over many seeds, and where an arm's own value sits in it."""

    metric: str
    low: Optional[float]
    high: Optional[float]
    value: Optional[float]
    percentile: Optional[float]
    seeds: int


def bands_for(
    trades: Sequence[ScoredTrade], sides: dict[tuple[str, datetime], BothSides],
    grid: Sequence[date], seeds: int,
) -> list[Band]:
    """The coin flip on this arm's own lines, ``seeds`` times.

    The null for "did this arm read anything" is not the coin flip on every
    line -- it is the coin flip on the lines this arm chose. Selection is
    the arm's; only the direction is replaced.
    """
    keys = [t.key for t in trades]
    draws = [flip_trades(keys, sides, seed) for seed in range(seeds)]
    metrics = (
        ("mean net", mean_net, mean_net(trades)),
        ("hit rate", hit_rate, hit_rate(trades)),
        ("mean/day", lambda ts: statistics.fmean(on_grid(daily_net(ts), grid)) if grid and ts else None,
         statistics.fmean(on_grid(daily_net(trades), grid)) if grid and trades else None),
    )
    out: list[Band] = []
    for label, fn, value in metrics:
        sample = [v for v in (fn(d) for d in draws) if v is not None]
        out.append(Band(
            metric=label, low=percentile(sample, BAND[0]), high=percentile(sample, BAND[1]),
            value=value, percentile=percentile_of(value, sample), seeds=len(sample),
        ))
    return out


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class GroupReport:
    group: str
    tickers: int
    results: list[ArmResult]
    grid: list[date]
    bands: dict[str, list[Band]]
    watchlist_return: Optional[float]
    watchlist_n: int
    watchlist_total: int
    spy_return: Optional[float]
    #: The world index fund, bought and held over the same window.
    index_return: Optional[float] = None


# --------------------------------------------------------------------------- #
# The decision gate: the index's windows, and one look's inputs
# --------------------------------------------------------------------------- #


def _day(value: object) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    import pandas as pd

    return pd.Timestamp(value).date()


def index_bars(fetcher: OhlcFetcher, start: date, end: date) -> list[tuple[date, float, float, float]]:
    """``(day, open, close, dividend)`` for the index, final bars only."""
    frame = fetcher.ohlc(gate.INDEX_TICKER, start, end)
    if frame is None or getattr(frame, "empty", True):
        return []
    has_dividends = "Dividends" in frame.columns
    out: list[tuple[date, float, float, float]] = []
    for stamp, row in frame.iterrows():
        paid = float(row["Dividends"]) if has_dividends else 0.0
        out.append((_day(stamp), float(row["Open"]), float(row["Close"]),
                    paid if paid == paid else 0.0))
    out.sort(key=lambda bar: bar[0])
    return out


def index_daily(
    bars: Sequence[tuple[date, float, float, float]], grid: Sequence[date], horizon: int,
) -> dict[date, float]:
    """The index's return over each entry day's own window, where it can be priced."""
    out: dict[date, float] = {}
    for day in grid:
        value = gate.index_window_return(bars, day, horizon)
        if value is not None:
            out[day] = value
    return out


def look_inputs(
    results: Sequence[ArmResult], sides: dict[tuple[str, datetime], BothSides],
    grid: Sequence[date], index: dict[date, float], entry_days: int, horizon: int, seeds: int,
) -> gate.LookInputs:
    """Everything one look reads, on its own first ``entry_days`` entry days only.

    A look is re-computed from the journal every night, and must say the
    same thing every night: so it reads the trades opened on its own entry
    days and nothing opened after them, whatever the race has since seen.
    """
    days = list(grid[:entry_days])
    cut = days[-1]
    trades = {r.name: [t for t in r.trades if t.entry_day <= cut] for r in results}
    series = {name: on_grid(daily_net(ts), days) for name, ts in trades.items()}

    def paired(first: str, second: str) -> Optional[float]:
        return newey_west_t([a - b for a, b in zip(series[first], series[second])], horizon)

    band = next(b for b in bands_for(trades[MODEL_ARM], sides, days, seeds) if b.metric == "mean/day")
    priced = [i for i, day in enumerate(days) if day in index]
    versus = {
        name: newey_west_t([series[name][i] - index[days[i]] for i in priced], horizon)
        for name in (MODEL_ARM, momentum.NAME, hybrid.NAME)
    }
    return gate.LookInputs(
        entry_days=entry_days,
        t_model_momentum=paired(MODEL_ARM, momentum.NAME),
        t_model_hybrid=paired(MODEL_ARM, hybrid.NAME),
        t_hybrid_momentum=paired(hybrid.NAME, momentum.NAME),
        model_mean=band.value,
        model_band_high=band.high,
        t_vs_index=versus,
        index_days=len(priced),
        index_missing=len(days) - len(priced),
    )


def look_data_problem(
    window: Sequence[JournalEntry], fetcher: OhlcFetcher, grid: Sequence[date],
    entry_days: int, horizon: int, today: date,
    source: Optional[PriceSource] = None, entry_rule: str = ENTRY_AUTO,
) -> Optional[str]:
    """Why a look's own days cannot be read tonight, or None if they can.

    A look reads every trade opened on its first ``entry_days`` entry days.
    If the price history of any ticker with a line in those days did not
    arrive -- a yfinance outage for one name -- that name's trades silently
    leave every arm and the look would read a different sample than it will
    tomorrow. So the look waits: every such ticker must have final bars
    through the close of the look's last trades.
    """
    cut = grid[entry_days - 1]
    needed = gate.trading_days_after(cut, max(0, horizon - 1))
    missing: list[str] = []
    for ticker in sorted({e.ticker for e in window if _line_day(e) < cut}):
        frame = fetcher.ohlc(ticker, cut, today)
        if frame is None or getattr(frame, "empty", True):
            missing.append(ticker)
            continue
        if _day(frame.index[-1]) < needed:
            missing.append(ticker)
    if missing:
        return (f"no final prices through {needed} for {len(missing)} ticker(s): "
                f"{', '.join(missing[:8])}{'...' if len(missing) > 8 else ''}")
    # Every line the look's days are made of must also be resolved by the
    # scorer. A line written after the close resolves one night later than
    # its simulated trade is dated (the scorer's entry rule moves it to the
    # next close), so a look read the night before would be missing part of
    # its own last day. The coin flip takes a side on every line, so its
    # entries are exactly the look's lines.
    if source is not None:
        early = [e for e in window if _line_day(e) < cut]
        _, statuses = score_entries(entries_for_arm(control.NAME, early), source, horizon,
                                    entry_rule, today)
        waiting = statuses.get("pending", 0)
        if waiting:
            return f"{waiting} line(s) in the look's days have not resolved yet"
    return None


def registered_mismatches(args: argparse.Namespace) -> list[str]:
    """Every setting of this run that differs from the registered one."""
    registered = (
        ("horizon", args.horizon, gate.REGISTERED_HORIZON),
        ("cost per side", args.cost_per_side, DEFAULT_COST_PER_SIDE),
        ("conviction floor", args.floor, cfg.MIN_CONVICTION),
        ("seeds", args.seeds, DEFAULT_SEEDS),
        ("entry rule", args.entry, ENTRY_AUTO),
        ("equity", args.equity, 100_000.0),
        ("stop multiplier", args.stop_multiplier, cfg.ATR_STOP_MULTIPLIER),
        ("max position", args.max_position_pct, cfg.MAX_POSITION_PCT),
    )
    return [f"{name} {value} (registered {want})" for name, value, want in registered if value != want]


@dataclass(frozen=True)
class GateView:
    """What the decision gate saw and said, for the header."""

    registered: bool
    mismatches: tuple[str, ...]
    window_lines: int
    window_cycle_days: int
    unanswered_in_window: int
    entry_days: int
    independent: int
    looks: tuple[gate.Look, ...]
    next_estimate: Optional[date]


def gate_json(view: GateView, horizon: int, now: datetime) -> dict:
    """The gate as data, for the dashboard's banner: the same numbers the header prints."""
    decided = gate.first_decision(view.looks)
    upcoming = None if decided else gate.next_look(view.looks)
    return {
        "generated_at": now.isoformat(),
        "status_line": gate.status_line(view.independent, view.looks),
        "registered": view.registered,
        "independent": min(view.independent, gate.MIN_INDEPENDENT_DAYS),
        "of": gate.MIN_INDEPENDENT_DAYS,
        "trading_days": gate.entry_days_needed(gate.MIN_INDEPENDENT_DAYS, horizon),
        "decided": decided is not None,
        "outcome": decided.outcome if decided else None,
        "outcome_text": gate.OUTCOME_TEXT[decided.outcome] if decided else None,
        "next": None if upcoming is None else {
            "independent": upcoming.independent,
            "entry_days": gate.entry_days_needed(upcoming.independent, horizon),
            "estimated": view.next_estimate.isoformat() if view.next_estimate else None,
            "bar": upcoming.bar,
        },
        "looks": [
            {"independent": look.independent, "bar": look.bar, "reached": look.reached,
             "outcome": look.outcome, "reason": look.reason}
            for look in view.looks
        ],
    }


def watch_days(entries: Sequence[JournalEntry]) -> list[gate.WatchDay]:
    """The model arm's cycle days in the window, for the owner's triggers."""
    by_day: dict[date, list[JournalEntry]] = {}
    for entry in entries:
        if entry.timestamp is None or entry.held or not gate.in_window(_line_day(entry)):
            continue
        # A name whose context never arrived was never put to the model:
        # a news-vendor outage is not a failed model call.
        if entry.stage == "context":
            continue
        by_day.setdefault(_line_day(entry), []).append(entry)
    return [
        gate.WatchDay(
            day=day, asked=len(rows),
            failed=sum(1 for e in rows if e.model_failed),
            shorts=sum(1 for e in rows if e.model_answered and e.bias == "BEARISH"),
        )
        for day, rows in sorted(by_day.items())
    ]


@dataclass(frozen=True)
class Spend:
    """What the model calls cost, from the journal's own measured usage."""

    lines: int
    priced: int
    model_usd: float
    screen_usd: float

    @property
    def total(self) -> float:
        return self.model_usd + self.screen_usd


def llm_spend(entries: Sequence[JournalEntry]) -> Spend:
    """Every call counted once: on a line the screen ended, the usage IS the screen's."""
    return Spend(
        lines=len(entries),
        priced=sum(1 for e in entries if e.cost_usd is not None or e.screen_cost_usd is not None),
        model_usd=sum(e.cost_usd or 0.0 for e in entries if not e.cost_is_screen),
        screen_usd=sum((e.screen_cost_usd or 0.0) + ((e.cost_usd or 0.0) if e.cost_is_screen else 0.0)
                       for e in entries),
    )


def window_warnings(entries: Sequence[JournalEntry]) -> list[str]:
    """Lines in the window made under settings other than the registered ones."""
    from orchestrator import llm

    window = [e for e in entries if e.timestamp is not None and gate.in_window(_line_day(e))]
    out: list[str] = []
    screened = [e for e in window if e.screening]
    if screened:
        days = sorted({_line_day(e).isoformat() for e in screened})
        out.append(
            f"WARNING: {len(screened)} line(s) in the decision window were made with the screen ON "
            f"({', '.join(days)}); the pre-registration says the screen is off, so those lines are "
            "not the model arm it registered"
        )
    unrecorded = [e for e in window if e.model_answered and e.reasoning_effort is None]
    if unrecorded:
        days = sorted({_line_day(e).isoformat() for e in unrecorded})
        out.append(f"note: {len(unrecorded)} answered line(s) in the decision window predate the "
                   f"journalled reasoning level ({', '.join(days)}); their settings are the code's on those days")
    efforts = [e for e in window if e.reasoning_effort and e.reasoning_effort != llm.MODEL_EFFORT]
    if efforts:
        seen = sorted({e.reasoning_effort for e in efforts})
        out.append(f"WARNING: {len(efforts)} line(s) in the decision window were made at reasoning "
                   f"{', '.join(seen)}, not the registered {llm.MODEL_EFFORT}")
    others = [e for e in window if e.has_signal and e.model and e.model != llm.MODEL]
    if others:
        seen = sorted({e.model for e in others})
        out.append(f"WARNING: {len(others)} answered line(s) in the decision window came from "
                   f"{', '.join(seen)}, not the registered {llm.MODEL}")
    return out


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Race:
    """One set of lines, raced: the arms, and the three group reports."""

    lines: list[JournalEntry]
    results: list[ArmResult]
    reports: list[GroupReport]
    window_start: Optional[date]
    window_end: Optional[date]

    @property
    def scored(self) -> bool:
        return any(r.n for r in self.results)


def run_race(
    lines: Sequence[JournalEntry], *, groups: Sequence[str], floor: float, seeds: int,
    sides: dict[tuple[str, datetime], BothSides], basket: PriceSource, **common,
) -> Race:
    results = [race_arm(name, lines, floor=floor, **common) for name in ARM_ORDER]
    everything = [t for r in results for t in r.trades]
    if not everything:
        return Race(list(lines), results, [], None, None)
    window_start = min(t.entry_day for t in everything)
    window_end = max(t.exit_day for t in everything)
    reports: list[GroupReport] = []
    for group in groups:
        members = {"all": DEFAULT_WATCHLIST, "funds": FUNDS, "companies": SINGLE_NAMES}[group]
        grid = sorted({t.entry_day for r in results for t in r.in_group(group)})
        bands = {r.name: bands_for(r.in_group(group), sides, grid, seeds) for r in results}
        wl, wl_n, _ = watchlist_buy_and_hold(members, window_start, window_end, basket)
        spy, spy_n, _ = watchlist_buy_and_hold(("SPY",), window_start, window_end, basket)
        vt, vt_n, _ = watchlist_buy_and_hold((gate.INDEX_TICKER,), window_start, window_end, basket)
        reports.append(GroupReport(
            group=group, tickers=len(members), results=results, grid=grid, bands=bands,
            watchlist_return=wl, watchlist_n=wl_n, watchlist_total=len(members),
            spy_return=spy if spy_n else None, index_return=vt if vt_n else None,
        ))
    return Race(list(lines), results, reports, window_start, window_end)


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.ERROR,
        format="%(levelname)s %(name)s: %(message)s",
    )
    if args.horizon < 1:
        print("--horizon must be at least 1 session", file=sys.stderr)
        return 2
    if args.cost_per_side < 0:
        print("--cost-per-side cannot be negative", file=sys.stderr)
        return 2

    try:
        read = read_journal(args.journal)
    except FileNotFoundError as exc:
        print(f"{exc}\nThe orchestrator writes one entry per ticker per cycle; run it first.", file=sys.stderr)
        return 1
    lines, unanswered = split_answered(offered(read.entries))
    if not lines:
        print(f"{args.journal} has no lines any arm could be asked on.", file=sys.stderr)
        return 1
    window = decision_window(lines)

    now = _now()
    today = now.date()
    final_through = last_final_session(now)
    source = YFinancePriceSource(final_through=final_through)
    fetcher = OhlcFetcher(final_through=final_through)
    prewarm(lines, source, fetcher, args.horizon, today)
    earliest = min(_line_day(e) for e in lines)
    basket = YFinancePriceSource(final_through=final_through)
    # Widest first: both sources cache the first window they are asked for.
    for ticker in ("SPY", gate.INDEX_TICKER):
        basket.closes(ticker, min(earliest, gate.DECISION_CUTOFF) - timedelta(days=14), today)
    bars = index_bars(fetcher, earliest, today)

    common = dict(
        horizon=args.horizon, entry_rule=args.entry, today=today, source=source, fetcher=fetcher,
        equity=args.equity, stop_multiplier=args.stop_multiplier,
        max_position_pct=args.max_position_pct, cost_per_side=args.cost_per_side,
    )
    sides = both_sides(lines, **common)
    whole = run_race(lines, groups=("all",), floor=args.floor, seeds=args.seeds, sides=sides,
                     basket=basket, **common)
    if not whole.scored:
        print("No arm has a resolved, above-floor trade yet -- nothing to race.", file=sys.stderr)
        return 1
    decision = run_race(window, groups=GROUPS, floor=args.floor, seeds=args.seeds, sides=sides,
                        basket=basket, **common)

    # The gate: the looks reached so far, each on its own entry days.
    mismatches = registered_mismatches(args)
    grid = decision.reports[0].grid if decision.reports else []
    entry_days = len(grid)
    independent = gate.independent_days(entry_days, args.horizon)
    inputs: dict[int, Optional[gate.LookInputs]] = {}
    if not mismatches:
        index = index_daily(bars, grid, args.horizon)
        for look_days, _ in gate.CHECKPOINTS:
            needed = gate.entry_days_needed(look_days, args.horizon)
            if entry_days >= needed:
                computed = look_inputs(decision.results, sides, grid, index, needed,
                                       args.horizon, args.seeds)
                problem = look_data_problem(window, fetcher, grid, needed, args.horizon, today,
                                            source=source, entry_rule=args.entry)
                inputs[look_days] = replace(computed, unreadable=problem) if problem else computed
    looks = tuple(gate.evaluate(inputs))
    upcoming = gate.next_look(looks)
    cycle_days = sorted({_line_day(e) for e in window})
    any_cycle = [_line_day(e) for e in read.entries
                 if e.timestamp is not None and gate.in_window(_line_day(e))]
    estimate = (
        gate.estimated_readable(gate.entry_days_needed(upcoming.independent, args.horizon),
                                gate.known_entry_days(cycle_days), args.horizon,
                                last_cycle_day=max(any_cycle) if any_cycle else None)
        if upcoming is not None else None
    )
    view = GateView(
        registered=not mismatches, mismatches=tuple(mismatches),
        window_lines=len(window), window_cycle_days=len(cycle_days),
        unanswered_in_window=len(decision_window(unanswered)),
        entry_days=entry_days, independent=independent, looks=looks, next_estimate=estimate,
    )

    if args.gate_json:
        print(json.dumps(gate_json(view, args.horizon, now)))
        return 0

    # The owner's model-watch triggers, and what the calls cost.
    days = watch_days(read.entries)
    spy = {day: price for day, price in basket.closes("SPY", earliest, today).bars}
    trips = {"b": gate.no_short_trips(days, spy),
             "c": gate.failure_trips(days, max_names_per_day=len(DEFAULT_WATCHLIST))}
    watch_counts = {"b": sum(1 for d in days if d.answered), "c": len(days)}
    in_window = [e for e in read.entries if e.timestamp is not None and gate.in_window(_line_day(e))]

    # The exploratory arms, on their own lines only, at both horizons, over
    # the whole journal: they cannot change the decision, and they need the
    # days. The longer horizon needs more history than prewarm fetched for
    # the main race, so its sources are fresh ones, cut to the same closes.
    long_source = YFinancePriceSource(final_through=final_through)
    long_fetcher = OhlcFetcher(final_through=final_through)
    prewarm(lines, long_source, long_fetcher, EXPLORATORY_HORIZON, today)
    exploratory = [
        race_exploratory(name, lines, floor=args.floor, horizons=(
            (args.horizon, source, fetcher), (EXPLORATORY_HORIZON, long_source, long_fetcher),
        ), entry_rule=args.entry, today=today, equity=args.equity,
           stop_multiplier=args.stop_multiplier, max_position_pct=args.max_position_pct,
           cost_per_side=args.cost_per_side)
        for name in sorted(EXPLORATORY)
    ]

    model_lines = entries_for_arm(MODEL_ARM, window)
    momentum_lines = entries_for_arm(momentum.NAME, window)
    agreement, agreed_on = direction_agreement(model_lines, momentum_lines)
    breakdown = agreement_breakdown(model_lines, momentum_lines)

    print(render(
        read=read, lines=window, results=decision.results, reports=decision.reports,
        exploratory=exploratory, floor=args.floor, horizon=args.horizon,
        cost_per_side=args.cost_per_side, seeds=args.seeds, final_through=final_through, now=now,
        window_start=decision.window_start, window_end=decision.window_end,
        agreement=agreement, agreed_on=agreed_on, breakdown=breakdown, per_trade=args.per_trade,
        gate_view=view, whole=whole, unanswered=unanswered, trips=trips, watch_counts=watch_counts,
        spend=llm_spend(in_window), spend_whole=llm_spend(read.entries),
        warnings=window_warnings(read.entries),
    ))
    return 0


# --------------------------------------------------------------------------- #
# Exploratory arms: on their own lines, paired, at two horizons
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class PairedRow:
    """One arm's trades on exactly the lines another arm took a side on."""

    name: str
    trades: tuple[ScoredTrade, ...]


@dataclass(frozen=True)
class ExploratoryResult:
    name: str
    horizon: int
    offered: int
    directional: int
    #: The arm itself, then the model and the momentum rule on the arm's lines.
    rows: tuple[PairedRow, ...]

    @property
    def own(self) -> PairedRow:
        return self.rows[0]

    @property
    def entry_days(self) -> int:
        return len({t.entry_day for t in self.own.trades})

    @property
    def enough(self) -> bool:
        return len(self.own.trades) >= EXPLORATORY_MIN_TRADES and self.entry_days >= EXPLORATORY_MIN_DAYS


def race_exploratory(
    name: str, lines: Sequence[JournalEntry], *, floor: float,
    horizons: Sequence[tuple[int, PriceSource, OhlcFetcher]], entry_rule: str, today: date,
    equity: float, stop_multiplier: float, max_position_pct: float, cost_per_side: float,
) -> list[ExploratoryResult]:
    """An exploratory arm on the lines it took a side on, paired, per horizon.

    The comparison is on the arm's own lines only: the model's and the
    momentum rule's trades on exactly those tickers on exactly those days,
    through the same arithmetic. Where the model or the rule was NEUTRAL or
    below the floor on such a line, it has no trade there and the pairing
    says so in its n.
    """
    arm_lines = entries_for_arm(name, lines)
    took_a_side = [e for e in arm_lines if e.is_directional]
    keys = {(e.ticker, e.timestamp) for e in took_a_side}
    same_lines = [e for e in lines if (e.ticker, e.timestamp) in keys]
    out: list[ExploratoryResult] = []
    for horizon, source, fetcher in horizons:
        common = dict(
            floor=floor, horizon=horizon, entry_rule=entry_rule, today=today, source=source,
            fetcher=fetcher, equity=equity, stop_multiplier=stop_multiplier,
            max_position_pct=max_position_pct, cost_per_side=cost_per_side,
        )
        rows = [PairedRow(name, race_arm(name, same_lines, **common).trades)]
        for other in (MODEL_ARM, momentum.NAME):
            rows.append(PairedRow(other, race_arm(other, same_lines, **common).trades))
        out.append(ExploratoryResult(
            name=name, horizon=horizon, offered=len(arm_lines), directional=len(took_a_side),
            rows=tuple(rows),
        ))
    return out


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #


def render(
    *, read: JournalRead, lines: Sequence[JournalEntry], results: Sequence[ArmResult],
    reports: Sequence[GroupReport], floor: float, horizon: int, cost_per_side: float,
    exploratory: Sequence[Sequence[ExploratoryResult]] = (),
    seeds: int, final_through: date, now: datetime, window_start: Optional[date],
    window_end: Optional[date], agreement: Optional[float], agreed_on: int,
    breakdown: Sequence[AgreementDay], per_trade: bool = False,
    gate_view: Optional[GateView] = None, whole: Optional[Race] = None,
    unanswered: Sequence[JournalEntry] = (), trips: Optional[dict[str, list[gate.Trip]]] = None,
    watch_counts: Optional[dict[str, int]] = None,
    spend: Optional[Spend] = None, spend_whole: Optional[Spend] = None,
    warnings: Sequence[str] = (),
) -> str:
    held = sum(1 for e in read.entries if e.held)
    no_stamp = sum(1 for e in read.entries if not e.held and e.timestamp is None)
    out = [
        "THREE ARMS, THE SAME LINES, THE SAME REALISED RETURNS, AFTER COSTS",
        "=" * 78,
    ]
    if gate_view is not None:
        out += _render_gate(gate_view, horizon)
    out += _render_watch(trips or {}, watch_counts)
    if spend is not None:
        out += _render_spend(spend, spend_whole)
    if warnings:
        out += ["", *warnings]

    days = sorted({_line_day(e) for e in lines})
    out += [
        "",
        f"decision window: {len(lines)} answered line(s) on {len(days)} cycle day(s)"
        + (f", {days[0]} to {days[-1]}" if days else "")
        + (f" | trades enter {window_start}, last exit {window_end}" if window_start else
           " | no trade resolved yet"),
        f"prices: final closes through {final_through} only (run at {now:%Y-%m-%d %H:%M} UTC); "
        f"a bar still trading is pending, never scored",
        f"horizon {horizon} session(s) | conviction floor {floor} on every arm | "
        f"cost {cost_per_side:.2%} per side ({2 * cost_per_side:.2%} round trip) on every trade of every arm",
        "",
        "DEFINITIONS",
        "-" * 78,
        f"net return   the trade's signed return through the real ATR stop and sizing,",
        f"             gap fills included, minus the {2 * cost_per_side:.2%} round trip",
        "hit          a trade whose net return is strictly greater than zero",
        "daily return the equal-weighted mean net return of the trades an arm opened",
        "             on one entry day; a day it opened none is 0 (it sat in cash)",
        "primary test paired daily difference, model minus momentum and model minus",
        f"             hybrid, Newey-West standard error at lag {horizon}; checked on every",
        f"             {_ordinal(horizon)} day alone",
        f"index test   the winner's daily return minus {gate.INDEX_TICKER} bought at the same",
        "             open and held over the same sessions (no stop, no cost,",
        "             dividends included), Newey-West at the same lag",
        f"independent  complete blocks of {horizon} scored entry days in the decision window",
        "",
        "COVERAGE AND RECONCILIATION",
        "-" * 78,
        f"journal lines {read.total_lines} | unparseable {read.skipped} | held, offered to no arm {held} | "
        f"no timestamp {no_stamp} | no model answer, offered to no arm {len(unanswered)} "
        f"({sum(1 for e in unanswered if gate.in_window(_line_day(e)))} in the window)",
        f"decision window: offered to every arm {len(lines)}",
        f"{'arm':<10}{'offered':>8}{'neutral':>8}{'a side':>7}{'< floor':>8}{'pending':>8}"
        f"{'resolved':>9}{'dropped':>8}{'scored':>7}",
    ]
    for r in results:
        out.append(
            f"{r.name:<10}{r.offered:>8}{r.offered - r.directional:>8}{r.directional:>7}"
            f"{r.below_floor:>8}{r.pending:>8}{r.acted_on:>9}{r.could_not_simulate:>8}{r.n:>7}"
        )
    tallies = all(r.accounted_for for r in results)
    out += [
        "",
        "  offered = neutral + a side; a side = < floor + pending + resolved;",
        "  resolved = dropped + scored. Every resolved line is scored or named as",
        f"  dropped (warm-up, cap, missing bars, incomplete horizon): "
        f"{'yes' if tallies else 'NO -- a line went missing'}",
        "  'offered' is the same number for every arm: held lines and lines the",
        "  model gave no answer on (a timeout or a failed call) are offered to",
        "  no arm at all, so every arm is judged on exactly the same lines.",
    ]

    if not reports:
        out += ["", "No trade in the decision window has resolved yet: nothing to decide on."]
    for report in reports:
        out += _render_group(report, horizon, seeds)

    for per_horizon in exploratory:
        out += _render_exploratory(per_horizon)

    out += [
        "",
        f"AGREEMENT, model vs {momentum.NAME}, where both took a side (decision window): "
        f"{_pct(agreement)} (n={agreed_on})",
        "-" * 78,
    ]
    longs = sum(d.agreed_long for d in breakdown)
    shorts = sum(d.agreed_short for d in breakdown)
    disagreed = sum(d.disagreed for d in breakdown)
    out.append(f"agreed long {longs} | agreed short {shorts} | disagreed {disagreed}")
    out.append(f"{'day':<12}{'both':>6}{'long':>6}{'short':>7}{'differ':>8}")
    for d in breakdown:
        out.append(f"{d.day.isoformat():<12}{d.both:>6}{d.agreed_long:>6}{d.agreed_short:>7}{d.disagreed:>8}")
    out.append(_agreement_verdict(longs, shorts, disagreed))

    if per_trade:
        out += ["", "EVERY SCORED TRADE (decision window)", "-" * 78,
                f"{'arm':<10}{'ticker':<7}{'signal':<11}{'entry':<11}{'exit':<11}{'side':<5}"
                f"{'gross':>8}{'net':>8}{'hit':>4}{'stop':>5}"]
        for r in results:
            for t in sorted(r.trades, key=lambda t: (t.signal_day, t.ticker)):
                out.append(
                    f"{t.arm:<10}{t.ticker:<7}{t.signal_day.isoformat():<11}{t.entry_day.isoformat():<11}"
                    f"{t.exit_day.isoformat():<11}{t.trade.side:<5}{t.gross:>+8.2%}{t.net:>+8.2%}"
                    f"{'y' if t.hit else 'n':>4}{'y' if t.stopped else 'n':>5}"
                )

    if whole is not None and whole.reports:
        whole_days = sorted({_line_day(e) for e in whole.lines})
        out += [
            "",
            "=" * 78,
            f"WHOLE JOURNAL, FOR READING ONLY: {whole_days[0]} to {whole_days[-1]}. It includes lines",
            f"before {gate.DECISION_CUTOFF}, answered by other models, which cannot count toward",
            "the decision and cannot be added to the decision window's days.",
            "=" * 78,
        ]
        for report in whole.reports:
            out += _render_group(report, horizon, seeds, title="WHOLE JOURNAL, ALL NAMES")

    out += [
        "",
        "HOW TO READ THIS",
        "-" * 78,
        "Read the decision gate first: it is the only part that decides anything,",
        "and it decides only at a planned look. Then the daily table, then the",
        "per-trade table: trades opened on the same day share the same sessions",
        "of market and are one observation, not several, which is what the n of",
        "the per-trade table hides. The coin-flip bands say what an arm's own",
        "selection of lines would have scored with the direction replaced by",
        "chance; an arm inside its band is not reading anything its choice of",
        "lines did not already give it. Buy-and-hold rows are what the direction",
        "of the market alone was worth over the same days.",
        "",
        f"The {momentum.NAME} arm's parameters are the textbook ones and were not",
        "chosen by looking at this journal. This report judges the rule; it",
        "does not tune it, and a good number here is not a reason to start.",
        "",
        "LIMITS",
        "-" * 78,
        "Per-trade rows are not a portfolio: no overlapping positions, no cash",
        "constraint, no compounding. The daily rows equal-weight each day's",
        "trades and compound days, which is a portfolio only if it rebalances",
        "to equal weight every morning. Anything marked 'too few' is",
        "arithmetic, not evidence, and a few weeks inside one market regime",
        "are fewer independent observations than any n here suggests.",
    ]
    return "\n".join(out)


def _render_gate(view: GateView, horizon: int) -> list[str]:
    out = [
        "",
        "DECISION GATE (pre-registered; applied by this code, not by a reader)",
        "-" * 78,
        gate.status_line(view.independent, view.looks),
    ]
    if not view.registered:
        out += [
            "SENSITIVITY RUN: these settings differ from the registered ones, so no look",
            "is evaluated and nothing below can decide anything:",
            *[f"  {m}" for m in view.mismatches],
        ]
    upcoming = None if gate.first_decision(view.looks) else gate.next_look(view.looks)
    if gate.first_decision(view.looks) is not None:
        out.append("The race has decided; no later look can change it.")
    elif upcoming is not None:
        needed = gate.entry_days_needed(upcoming.independent, horizon)
        when = view.next_estimate.isoformat() if view.next_estimate else "n/a"
        out.append(
            f"Next checkpoint: {upcoming.independent} independent days (= {needed} trading days), "
            f"estimated {when}, bar t > {upcoming.bar:.2f}"
        )
    else:
        out.append("Every planned look has been reached.")
    out.append(
        f"decision window: lines journalled on or after {gate.DECISION_CUTOFF} | "
        f"{view.window_lines} answered on {view.window_cycle_days} cycle day(s) | "
        f"{view.unanswered_in_window} with no model answer, dropped for every arm | "
        f"{view.entry_days} entry day(s) scored"
    )
    out.append(
        "looks: " + " | ".join(
            f"{look.independent} days, t > {look.bar:.2f}" for look in view.looks
        ) + f" | index {gate.INDEX_TICKER} at every look"
    )
    for look in view.looks:
        if not look.reached:
            continue
        i = look.inputs
        out += [
            "",
            f"look at {look.independent} independent days ({i.entry_days} entry days), bar {look.bar:.2f}"
            + (" -- FINAL" if look.final else ""),
            f"  t model-momentum {_num(i.t_model_momentum)} | t model-hybrid {_num(i.t_model_hybrid)} | "
            f"t hybrid-momentum {_num(i.t_hybrid_momentum)}",
            f"  model mean/day {_pct(i.model_mean, 3)} vs its coin flip's "
            f"{gate.COIN_FLIP_PERCENTILE:.0f}th percentile {_pct(i.model_band_high, 3)}",
            "  t vs " + gate.INDEX_TICKER + ": " + " | ".join(
                f"{name} {_num(t)}" for name, t in i.t_vs_index.items()
            ) + f" ({i.index_days} days priced, {i.index_missing} not)",
            f"  -> {gate.OUTCOME_TEXT[look.outcome] if look.decided else 'no decision at this look'}: "
            f"{look.reason}",
        ]
    return out


def _render_watch(trips: dict[str, list[gate.Trip]], counts: Optional[dict[str, int]] = None) -> list[str]:
    """The owner's model-watch triggers. A trip means: stop and tell the owner."""
    out = [
        "",
        "MODEL WATCH (the owner's triggers; a trip means stop and tell the owner, never revert)",
        "-" * 78,
    ]
    labels = {
        "b": f"(b) {gate.WATCH_DAYS} answered days in a row with no SHORT while SPY fell",
        "c": f"(c) failed or timed-out calls above {gate.WATCH_MAX_FAILED_SHARE:.0%} of names "
             f"over {gate.WATCH_DAYS} cycle days",
    }
    for key, label in labels.items():
        hits = trips.get(key, [])
        have = (counts or {}).get(key)
        if not hits and have is not None and have < gate.WATCH_DAYS:
            unit = "answered cycle day(s)" if key == "b" else "cycle day(s)"
            out.append(f"{label}: not yet judged ({have} of {gate.WATCH_DAYS} {unit} so far)")
            continue
        if not hits:
            out.append(f"{label}: not tripped")
            continue
        latest = hits[-1]
        out.append(f"{label}: TRIPPED {len(hits)} time(s); latest {latest.first} to {latest.last}: "
                   f"{latest.detail}")
    out.append("(a) is read from the zero-shorts replay (model-compare), not from the journal.")
    return out


def _render_spend(spend: Spend, whole: Optional[Spend]) -> list[str]:
    out = [
        "",
        f"LLM SPEND over the decision window: ${spend.total:.2f} "
        f"(model ${spend.model_usd:.2f}, screen ${spend.screen_usd:.2f}) "
        f"on {spend.priced} priced line(s) of {spend.lines}",
    ]
    if whole is not None:
        out.append(f"LLM spend over the whole journal: ${whole.total:.2f} "
                   f"(model ${whole.model_usd:.2f}, screen ${whole.screen_usd:.2f})")
    return out


def _render_group(report: GroupReport, horizon: int, seeds: int, title: Optional[str] = None) -> list[str]:
    title = title or {"all": "ALL NAMES", "funds": "FUNDS", "companies": "COMPANIES"}[report.group]
    grid = report.grid
    rows = sorted(
        ((r, r.in_group(report.group)) for r in report.results),
        key=lambda pair: (mean_net(pair[1]) is None, -(mean_net(pair[1]) or 0.0)),
    )
    out = [
        "",
        f"== {title} ({report.tickers} tickers) ==",
        "",
        f"PRIMARY: daily equal-weighted net return, sorted by mean per day ({len(grid)} entry days)",
        "-" * 78,
        f"{'arm':<10}{'days':>6}{'traded':>7}{'mean/day':>10}{'t (NW)':>8}{'cumulative':>12}",
    ]
    series: dict[str, list[float]] = {}
    for r, trades in rows:
        daily = daily_net(trades)
        series[r.name] = on_grid(daily, grid)
        mean = statistics.fmean(series[r.name]) if grid else None
        out.append(
            f"{r.name:<10}{len(grid):>6}{len(daily):>7}{_pct(mean, 2):>10}"
            f"{_num(newey_west_t(series[r.name], horizon)):>8}{_pct(cumulative(series[r.name])):>12}"
        )
    out.append(
        f"{'buy & hold':<10}{'':>6}{'':>7}{'':>10}{'':>8}"
        f"{_pct(report.watchlist_return):>12}  watchlist ({report.watchlist_n}/{report.watchlist_total} priced)"
    )
    out.append(f"{'SPY':<10}{'':>6}{'':>7}{'':>10}{'':>8}{_pct(report.spy_return):>12}")
    out.append(f"{gate.INDEX_TICKER:<10}{'':>6}{'':>7}{'':>10}{'':>8}{_pct(report.index_return):>12}"
               "  world index fund, bought and held")

    sparse = set(every_nth(grid, horizon))
    for first, second in PAIRED:
        a_series, b_series = series.get(first, []), series.get(second, [])
        out += ["", f"Paired difference, {first} minus {second}, day by day",
                f"{'entry day':<12}{first:>9}{second:>10}{'diff':>9}"]
        diffs = [a - b for a, b in zip(a_series, b_series)]
        for day, a, b, d in zip(grid, a_series, b_series, diffs):
            out.append(f"{day.isoformat():<12}{_pct(a, 2):>9}{_pct(b, 2):>10}{_pct(d, 2):>9}")
        sparse_diffs = [d for day, d in zip(grid, diffs) if day in sparse]
        out += [
            f"mean diff {_pct(statistics.fmean(diffs) if diffs else None, 2)} | "
            f"t (Newey-West, lag {horizon}) {_num(newey_west_t(diffs, horizon))} | n={len(diffs)} days",
            f"non-overlapping, every {_ordinal(horizon)} entry day: mean diff "
            f"{_pct(statistics.fmean(sparse_diffs) if sparse_diffs else None, 2)} | "
            f"t {_num(newey_west_t(sparse_diffs, 0))} | n={len(sparse_diffs)} days",
        ]
    out += [
        "",
        "SECONDARY: per-trade, through the real stop and sizing, sorted by mean net",
        "-" * 78,
        f"{'arm':<10}{'n':>5}{'mean net':>10}{'median':>9}{'hit rate':>10}{'stopped':>9}",
    ]
    for r, trades in rows:
        flag = "" if not trades or len(trades) >= MIN_TRADES else "  <- too few"
        out.append(
            f"{r.name:<10}{len(trades):>5}{_pct(mean_net(trades), 2):>10}{_pct(median_net(trades), 2):>9}"
            f"{_pct(hit_rate(trades)):>10}{_pct(stop_rate(trades)):>9}{flag}"
        )
    out += [
        "",
        f"COIN FLIP ON EACH ARM'S OWN LINES, {seeds} seeds (the journalled flip is seed 0)",
        f"{'arm':<10}{'metric':<10}{'value':>9}{'5th':>9}{'95th':>9}{'pctile':>8}",
    ]
    for r, _ in rows:
        for band in report.bands.get(r.name, []):
            digits = 2 if band.metric != "hit rate" else 1
            out.append(
                f"{r.name:<10}{band.metric:<10}{_pct(band.value, digits):>9}{_pct(band.low, digits):>9}"
                f"{_pct(band.high, digits):>9}{_num(band.percentile, 0):>8}"
            )
    return out


def _render_exploratory(per_horizon: Sequence[ExploratoryResult]) -> list[str]:
    if not per_horizon:
        return []
    first = per_horizon[0]
    out = [
        "",
        f"== EXPLORATORY: {first.name} (secondary; cannot change the main decision) ==",
        f"offered {first.offered} lines, took a side on {first.directional}. Scored on those lines",
        "only, paired against the model and the momentum rule on the same lines.",
        f"'too few' until {EXPLORATORY_MIN_TRADES} trades on {EXPLORATORY_MIN_DAYS} distinct entry days.",
    ]
    for result in per_horizon:
        flag = "" if result.enough else f"  <- too few ({len(result.own.trades)} trades, {result.entry_days} days)"
        out += [
            "",
            f"horizon {result.horizon} session(s){flag}",
            f"{'arm':<10}{'n':>5}{'mean net':>10}{'median':>9}{'hit rate':>10}{'stopped':>9}",
        ]
        for row in result.rows:
            out.append(
                f"{row.name:<10}{len(row.trades):>5}{_pct(mean_net(row.trades), 2):>10}"
                f"{_pct(median_net(row.trades), 2):>9}{_pct(hit_rate(row.trades)):>10}"
                f"{_pct(stop_rate(row.trades)):>9}"
            )
    return out


def _agreement_verdict(longs: int, shorts: int, disagreed: int) -> str:
    agreed = longs + shorts
    if agreed == 0:
        return "verdict: no line where both took a side."
    share = max(longs, shorts) / agreed
    side = "long" if longs >= shorts else "short"
    if disagreed == 0 and share >= 0.8:
        return (f"verdict: agreement is mostly automatic -- {share:.0%} of the agreeing lines are "
                f"{side}, so both arms were largely saying the same thing about the market, "
                "not about the names.")
    if disagreed == 0:
        return (f"verdict: agreement spans both directions ({longs} long, {shorts} short) with no "
                "disagreement at all; the model has not yet once called against the trend.")
    return f"verdict: {disagreed} disagreement(s); {longs} long and {shorts} short agreements."


def _ordinal(n: int) -> str:
    suffix = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


def _pct(value: Optional[float], digits: int = 1) -> str:
    return "n/a" if value is None else f"{value * 100:+.{digits}f}%"


def _num(value: Optional[float], digits: int = 2) -> str:
    return "n/a" if value is None else f"{value:.{digits}f}"


if __name__ == "__main__":
    raise SystemExit(main())
