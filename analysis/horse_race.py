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

Every arm is offered every line, except the ones no arm was offered: a
ticker already in the book, where the model was never asked and a rule
holding the same book would not have been either. The model then answers
on fewer lines than the rules, because the screen drops some and the model
fails on some, and both of those are the model's to own -- the funnel is
part of the design being raced, not an excuse for it.

Nothing here is fitted. The momentum arm's parameters are the textbook
values and this file never touches them; it judges the rule, it does not
tune it. Read-only in every direction -- it reads the journal, fetches
prices, and prints.
"""

from __future__ import annotations

import argparse
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
from orchestrator.technicals import TechnicalSnapshot  # noqa: E402
from rules import ARMS, control, momentum  # noqa: E402

DEFAULT_HORIZON = 3

#: Per side, as a fraction of notional: 0.10% each way, 0.20% a round trip.
#: Applied identically to every trade of every arm. The number is a
#: pre-registered assumption, not a measurement of this broker.
DEFAULT_COST_PER_SIDE = 0.001

#: Coin flips drawn per line to put a band around "no information".
DEFAULT_SEEDS = 1000
BAND = (5.0, 95.0)

#: Arm A's name in the report. The rule arms report under their own.
MODEL_ARM = "model"

#: Report order. The model first because it is the incumbent; the coin flip
#: last because it is the floor everything above it has to clear.
ARM_ORDER = (MODEL_ARM, momentum.NAME, control.NAME)

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
        technicals = TechnicalSnapshot.from_dict(entry.technicals) if entry.technicals else None
        signal = arm(entry.ticker, technicals, _line_day(entry))
        out.append(replace(entry, bias=signal.bias.value, conviction=signal.conviction, scores={}, blend={}))
    return out


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
    lines = offered(read.entries)
    if not lines:
        print(f"{args.journal} has no lines any arm could be asked on.", file=sys.stderr)
        return 1

    now = _now()
    today = now.date()
    final_through = last_final_session(now)
    source = YFinancePriceSource(final_through=final_through)
    fetcher = OhlcFetcher(final_through=final_through)
    prewarm(lines, source, fetcher, args.horizon, today)

    common = dict(
        horizon=args.horizon, entry_rule=args.entry, today=today, source=source, fetcher=fetcher,
        equity=args.equity, stop_multiplier=args.stop_multiplier,
        max_position_pct=args.max_position_pct, cost_per_side=args.cost_per_side,
    )
    results = [race_arm(name, lines, floor=args.floor, **common) for name in ARM_ORDER]
    if not any(r.n for r in results):
        print("No arm has a resolved, above-floor trade yet -- nothing to race.", file=sys.stderr)
        return 1
    sides = both_sides(lines, **common)

    # Buy-and-hold over the union of every arm's trades, on final closes too.
    everything = [t for r in results for t in r.trades]
    window_start = min(t.entry_day for t in everything)
    window_end = max(t.exit_day for t in everything)
    basket = YFinancePriceSource(final_through=final_through)

    reports: list[GroupReport] = []
    for group in GROUPS:
        members = {"all": DEFAULT_WATCHLIST, "funds": FUNDS, "companies": SINGLE_NAMES}[group]
        grid = sorted({t.entry_day for r in results for t in r.in_group(group)})
        bands = {
            r.name: bands_for(r.in_group(group), sides, grid, args.seeds) for r in results
        }
        wl, wl_n, _ = watchlist_buy_and_hold(members, window_start, window_end, basket)
        spy, spy_n, _ = watchlist_buy_and_hold(("SPY",), window_start, window_end, basket)
        reports.append(GroupReport(
            group=group, tickers=len(members), results=results, grid=grid, bands=bands,
            watchlist_return=wl, watchlist_n=wl_n, watchlist_total=len(members),
            spy_return=spy if spy_n else None,
        ))

    model_lines = entries_for_arm(MODEL_ARM, lines)
    momentum_lines = entries_for_arm(momentum.NAME, lines)
    agreement, agreed_on = direction_agreement(model_lines, momentum_lines)
    breakdown = agreement_breakdown(model_lines, momentum_lines)

    print(render(
        read=read, lines=lines, results=results, reports=reports,
        floor=args.floor, horizon=args.horizon, cost_per_side=args.cost_per_side,
        seeds=args.seeds, final_through=final_through, now=now,
        window_start=window_start, window_end=window_end,
        agreement=agreement, agreed_on=agreed_on, breakdown=breakdown,
        per_trade=args.per_trade,
    ))
    return 0


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #


def render(
    *, read: JournalRead, lines: Sequence[JournalEntry], results: Sequence[ArmResult],
    reports: Sequence[GroupReport], floor: float, horizon: int, cost_per_side: float,
    seeds: int, final_through: date, now: datetime, window_start: date, window_end: date,
    agreement: Optional[float], agreed_on: int, breakdown: Sequence[AgreementDay],
    per_trade: bool = False,
) -> str:
    days = sorted({_line_day(e) for e in lines})
    held = sum(1 for e in read.entries if e.held)
    no_stamp = sum(1 for e in read.entries if not e.held and e.timestamp is None)
    out = [
        "THREE ARMS, THE SAME LINES, THE SAME REALISED RETURNS, AFTER COSTS",
        "=" * 78,
        f"journal {days[0]} to {days[-1]} ({len(days)} cycle days) | trades enter {window_start}, "
        f"last exit {window_end}",
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
        "primary test paired daily difference, model minus momentum, Newey-West",
        f"             standard error at lag {horizon}; checked on every {_ordinal(horizon)} day alone",
        "",
        "COVERAGE AND RECONCILIATION",
        "-" * 78,
        f"journal lines {read.total_lines} | unparseable {read.skipped} | held, offered to no arm {held} | "
        f"no timestamp {no_stamp} | offered to every arm {len(lines)}",
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
        "  'offered' differs between the model and the rules by design: the",
        "  screen drops lines and the model fails on lines, and both are the",
        "  model's to own.",
    ]

    for report in reports:
        out += _render_group(report, horizon, seeds)

    out += [
        "",
        f"AGREEMENT, model vs {momentum.NAME}, where both took a side: {_pct(agreement)} (n={agreed_on})",
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
        out += ["", "EVERY SCORED TRADE", "-" * 78,
                f"{'arm':<10}{'ticker':<7}{'signal':<11}{'entry':<11}{'exit':<11}{'side':<5}"
                f"{'gross':>8}{'net':>8}{'hit':>4}{'stop':>5}"]
        for r in results:
            for t in sorted(r.trades, key=lambda t: (t.signal_day, t.ticker)):
                out.append(
                    f"{t.arm:<10}{t.ticker:<7}{t.signal_day.isoformat():<11}{t.entry_day.isoformat():<11}"
                    f"{t.exit_day.isoformat():<11}{t.trade.side:<5}{t.gross:>+8.2%}{t.net:>+8.2%}"
                    f"{'y' if t.hit else 'n':>4}{'y' if t.stopped else 'n':>5}"
                )

    out += [
        "",
        "HOW TO READ THIS",
        "-" * 78,
        "Read the daily table first and the per-trade table second: trades",
        "opened on the same day share the same sessions of market and are one",
        "observation, not several, which is what the n of the per-trade table",
        "hides. The coin-flip bands say what an arm's own selection of lines",
        "would have scored with the direction replaced by chance; an arm inside",
        "its band is not reading anything its choice of lines did not already",
        "give it. Buy-and-hold rows are what the direction of the market alone",
        "was worth over the same days.",
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


def _render_group(report: GroupReport, horizon: int, seeds: int) -> list[str]:
    title = {"all": "ALL NAMES", "funds": "FUNDS", "companies": "COMPANIES"}[report.group]
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

    model_series = series.get(MODEL_ARM, [])
    rule_series = series.get(momentum.NAME, [])
    out += ["", f"Paired difference, {MODEL_ARM} minus {momentum.NAME}, day by day",
            f"{'entry day':<12}{MODEL_ARM:>9}{momentum.NAME:>10}{'diff':>9}"]
    diffs = [m - r for m, r in zip(model_series, rule_series)]
    for day, m, r, d in zip(grid, model_series, rule_series, diffs):
        out.append(f"{day.isoformat():<12}{_pct(m, 2):>9}{_pct(r, 2):>10}{_pct(d, 2):>9}")
    sparse = every_nth(grid, horizon)
    sparse_diffs = [d for day, d in zip(grid, diffs) if day in set(sparse)]
    out += [
        f"mean diff {_pct(statistics.fmean(diffs) if diffs else None, 2)} | "
        f"t (Newey-West, lag {horizon}) {_num(newey_west_t(diffs, horizon))} | n={len(diffs)} days",
        f"non-overlapping, every {_ordinal(horizon)} entry day: mean diff "
        f"{_pct(statistics.fmean(sparse_diffs) if sparse_diffs else None, 2)} | "
        f"t {_num(newey_west_t(sparse_diffs, 0))} | n={len(sparse_diffs)} days",
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
