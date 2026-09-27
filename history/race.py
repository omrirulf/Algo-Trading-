"""The race on history: the locked momentum rule and A, scored exactly as the live race scores them.

Each arm's call on each history line goes through the race's own steps
(``analysis.horse_race``): the conviction floor (0.30), ``score_entries``,
``simulate_model_trades`` -- the next session's open, 3 sessions, the ATR
stop (2 x ATR14), the 5% cap -- and 0.10% a side. A's calls are momentum's
with A's own veto (``shadow.exploratory.veto_entries``), on the stand-in
live price. Nothing is re-implemented but the one step that would take days
as written: the coin flip's band (below).

**Year by year.** The race fetches each ticker's bars once, from 40 days
before its first line (``hr.prewarm``), and finds each signal's bar by
walking the frame from its start, so 26 years in one piece would walk
thousands of bars for every one of half a million signals. So each calendar
year of lines is raced on its own, with fresh price sources fed from the
price table -- exactly what the live race does, as if its journal had
started that January -- and the trades are pooled. A trade belongs to the
year of its line, and nothing crosses: the live race's own ATR warm-up (from
40 days before the first line) is what each year starts from.

**Compared with the coin flip and with "always long".** Two controls the
race registers, on the same lines, through the same trade:

* the coin flip on the arm's own lines (``rules/control.py``, seeds 0 to
  999; the race's condition 3 reads the same band for the model): where the
  arm's mean net return per trade, hit rate and mean per day fall in it. Its
  1,000 draws on half a million trades take hours one trade at a time
  (``hr.bands_for`` asks ``control.signal_for`` for every trade of every
  seed), so each flip is still drawn by ``control.signal_for``, spread over
  the processors, and only the averaging is done on arrays
  (``coin_band``); ``tests/test_history_screen.py`` checks it gives
  ``bands_for``'s numbers exactly. Beside it, a paired test: the arm minus
  what a coin flip earns on the same line on average (half the long trade
  plus half the short one), day by day, Newey-West t at lag 3;
* always long: the long side of the same trade (``hr.both_sides``) on the
  arm's own lines, and on every line -- owning every name, three sessions
  at a time -- each paired day by day with the arm, Newey-West t at lag 3.

Longs and shorts are read separately, and every number is split at 2010.
C's pullback is read here too: whether each momentum signal's limit would
have filled in its 3 sessions, and the race trade of the signals that
filled against those that did not (``shadow.exploratory.race_tests``'s
grouping, section 13.4). A fill means the price went against the signal
first, inside the very sessions that race trade is scored on, so that
comparison is built partly into the grouping: it says what C avoids, not
what C earns. C's own result is its fund (``history.funds``).
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Final, Mapping, Optional, Sequence

import numpy as np
import pandas as pd

from analysis import horse_race as hr
from analysis.baseline_compare import LEAD_DAYS as OHLC_LEAD_DAYS, OhlcFetcher
from analysis.returns import HISTORY_LEAD_DAYS, YFinancePriceSource
from analysis.scoring import score_entries
from analysis.baseline_compare import simulate_model_trades
from app.schemas import Bias
from config import settings as cfg
from history import journal
from history.periods import Period, periods_for, test_of, welch
from history.sessions import historical_calendar
from rules import control, momentum
from shadow import exploratory as xp
from shadow.fund import Line
from shadow.market import Bars

#: The race's registered arithmetic (``shadow.exploratory.race_settings``, section 2).
EQUITY: Final[float] = 100_000.0
ARMS: Final[tuple[str, ...]] = (momentum.NAME, xp.VETO)
Key = tuple[str, datetime]


# --------------------------------------------------------------------------- #
# The race's price sources, fed from the table
# --------------------------------------------------------------------------- #


class FrameCloses(YFinancePriceSource):
    """``YFinancePriceSource`` answering from the price table instead of yfinance, same window."""

    def __init__(self, frames: Mapping[str, pd.DataFrame], final_through: date) -> None:
        super().__init__(final_through=final_through)
        self._frames = frames

    def _fetch(self, ticker: str, start: date, end: date) -> list[tuple[date, float]]:
        frame = self._frames.get(ticker)
        if frame is None or frame.empty:
            return []
        part = frame.loc[pd.Timestamp(start - timedelta(days=HISTORY_LEAD_DAYS)): pd.Timestamp(end), "Close"]
        return [(stamp.date(), float(value)) for stamp, value in part.dropna().items()]


class FrameOhlc(OhlcFetcher):
    """``OhlcFetcher`` answering from the price table instead of yfinance, same window."""

    def __init__(self, frames: Mapping[str, pd.DataFrame], final_through: date) -> None:
        super().__init__(final_through=final_through)
        self._frames = frames

    def _fetch(self, ticker: str, start: date, end: date) -> pd.DataFrame:
        frame = self._frames.get(ticker)
        if frame is None or frame.empty:
            return pd.DataFrame()
        part = frame.loc[pd.Timestamp(start - timedelta(days=OHLC_LEAD_DAYS)): pd.Timestamp(end)]
        return part.dropna(subset=["Open", "High", "Low", "Close"])


def settings(frames: Mapping[str, pd.DataFrame], final_through: date, lines) -> xp.RaceSettings:
    """``shadow.exploratory.race_settings`` with the table's sources: fresh, warmed over ``lines``."""
    source, fetcher = FrameCloses(frames, final_through), FrameOhlc(frames, final_through)
    hr.prewarm(lines, source, fetcher, hr.DEFAULT_HORIZON, final_through)
    return xp.RaceSettings(cfg.MIN_CONVICTION, hr.DEFAULT_HORIZON, hr.ENTRY_AUTO, final_through, source, fetcher,
                           EQUITY, cfg.ATR_STOP_MULTIPLIER, cfg.MAX_POSITION_PCT, hr.DEFAULT_COST_PER_SIDE)


def arm_result(name: str, arm_entries, how: xp.RaceSettings) -> hr.ArmResult:
    """``hr.race_arm`` from the arm's entries on: the same steps, for an arm ``rules.ARMS`` does not carry (A)."""
    directional = [e for e in arm_entries if e.is_directional]
    above = [e for e in directional if (e.conviction or 0.0) >= how.floor]
    scored, _ = score_entries(above, how.source, how.horizon, how.entry_rule, how.today)
    trades, matched, dropped = simulate_model_trades(
        scored, equity=how.equity, horizon_days=how.horizon, stop_multiplier=how.stop_multiplier,
        max_position_pct=how.max_position_pct, fetcher=how.fetcher,
    )
    return hr.ArmResult(
        name=name, offered=len(arm_entries), directional=len(directional), below_floor=len(directional) - len(above),
        pending=len(above) - len(scored), acted_on=len(scored), could_not_simulate=dropped,
        trades=tuple(hr.scored_trades(name, matched, trades, how.cost_per_side)),
    )


# --------------------------------------------------------------------------- #
# One year
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Side:
    """One line's trade both ways (``hr.BothSides``), as the controls read it."""

    entry_day: date
    buy_net: float
    sell_net: float


@dataclass(frozen=True)
class Pullback:
    """One momentum signal C would have ordered: did its limit fill, and how did momentum's race trade do."""

    key: Key
    entry_day: date
    side: str
    net: float
    filled: bool


@dataclass
class YearResult:
    year: int
    lines: int = 0
    arms: dict[str, hr.ArmResult] = field(default_factory=dict)
    sides: dict[Key, Side] = field(default_factory=dict)
    pullback: list[Pullback] = field(default_factory=list)


def filled_or_missed(momentum_entries, momentum_trades, bars: Bars, how: xp.RaceSettings) -> list[Pullback]:
    """``shadow.exploratory.race_tests``'s grouping of momentum's signals into filled and missed (13.4)."""
    trade = {(t.ticker, t.signal_at): t for t in momentum_trades}
    out = []
    for e in momentum_entries:
        if not (e.is_directional and (e.conviction or 0.0) >= how.floor) or e.held:
            continue
        key = (e.ticker, e.timestamp)
        day = e.timestamp.date()                 # lines carry UTC timestamps
        limit, _ = xp.limit_price(Line(e.ticker, day, 1, e), Bias(e.bias))
        if limit is None or key not in trade:
            continue
        window = xp.sessions_after(day, xp.PULLBACK_SESSIONS)
        if window[-1] > how.today:
            continue
        hit = any(xp.touches(Bias(e.bias), limit, bar) for bar in
                  (bars.bar(e.ticker, d) for d in window) if bar is not None)
        scored = trade[key]
        out.append(Pullback(key, scored.entry_day, scored.trade.side, scored.net, hit))
    return out


def race_year(year: int, journal_dir: Path, frames: Mapping[str, pd.DataFrame], bars: Bars,
              sessions: Sequence[date], final_through: date) -> YearResult:
    """Every arm's trades on one calendar year of history lines, and both sides of every line."""
    with historical_calendar(sessions):
        lines = hr.offered(journal.read(journal_dir, [year]))
        if not lines:
            return YearResult(year)
        how = settings(frames, final_through, lines)
        momentum_entries = hr.entries_for_arm(momentum.NAME, lines)
        arms = {
            momentum.NAME: arm_result(momentum.NAME, momentum_entries, how),
            xp.VETO: arm_result(xp.VETO, xp.veto_entries(momentum_entries, bars), how),
        }
        both = hr.both_sides(
            lines, horizon=how.horizon, entry_rule=how.entry_rule, today=how.today, source=how.source,
            fetcher=how.fetcher, equity=how.equity, stop_multiplier=how.stop_multiplier,
            max_position_pct=how.max_position_pct, cost_per_side=how.cost_per_side,
        )
        sides = {key: Side(pair.buy.entry_day, pair.buy.net, pair.sell.net) for key, pair in both.items()}
        pullback = filled_or_missed(momentum_entries, arms[momentum.NAME].trades, bars, how)
    return YearResult(year, len(lines), arms, sides, pullback)


#: What the year workers read, set before the pool forks (so nothing is copied per task).
_SHARED: dict = {}


def _year_job(year: int) -> YearResult:
    s = _SHARED
    return race_year(year, s["journal"], s["frames"], s["bars"], s["sessions"], s["final_through"])


def race_years(years: Sequence[int], journal_dir: Path, frames, bars: Bars, sessions,
               final_through: date) -> list[YearResult]:
    """Every year raced, one after another (``history.screen`` runs ``_year_job`` in a pool instead)."""
    _SHARED.update(journal=journal_dir, frames=frames, bars=bars, sessions=list(sessions),
                   final_through=final_through)
    return [_year_job(y) for y in years]


# --------------------------------------------------------------------------- #
# The coin flip's band, drawn by rules/control.py
# --------------------------------------------------------------------------- #


def _flip_job(job: tuple[int, int]) -> tuple[int, np.ndarray]:
    lo, hi = job
    keys = _SHARED["flip_keys"]
    out = np.empty((len(keys), hi - lo), dtype=bool)
    for j, seed in enumerate(range(lo, hi)):
        for i, (ticker, day) in enumerate(keys):
            out[i, j] = control.signal_for(ticker, day, seed=seed).bias is Bias.BULLISH
    return lo, out


def coin_flips(keys: Sequence[Key], seeds: int, processes: int = 1, chunk: int = 25) -> np.ndarray:
    """``flips[i, s]``: seed ``s``'s coin flip on line ``keys[i]`` goes long (``hr.flip_trades``'s draw)."""
    _SHARED["flip_keys"] = [(ticker, stamp.astimezone(timezone.utc).date()) for ticker, stamp in keys]
    jobs = [(lo, min(seeds, lo + chunk)) for lo in range(0, seeds, chunk)]
    if processes > 1:
        from multiprocessing import get_context

        # Forked after the keys are set, so no worker is sent them.
        with get_context("fork").Pool(processes) as pool:
            parts = pool.map(_flip_job, jobs, chunksize=1)
    else:
        parts = [_flip_job(j) for j in jobs]
    flips = np.empty((len(keys), seeds), dtype=bool)
    for lo, block in parts:
        flips[:, lo:lo + block.shape[1]] = block
    return flips


def coin_band(trades: Sequence[hr.ScoredTrade], sides: Mapping[Key, Side], flips: np.ndarray,
              row_of: Mapping[Key, int], grid: Sequence[date]) -> dict[str, dict]:
    """``hr.bands_for``'s three bands, from flips drawn once: the coin flip on the arm's own lines.

    For each seed, the draw is the flip's side of every one of the arm's lines
    that has both sides (``hr.flip_trades``); its mean net return, hit rate
    and mean per day over ``grid`` go into the sample, and the arm's own
    value is placed in it with the race's ``percentile`` and ``percentile_of``.
    """
    seeds = flips.shape[1]
    usable = [t.key for t in trades if t.key in sides]
    values = {
        "mean net": hr.mean_net(trades),
        "hit rate": hr.hit_rate(trades),
        "mean/day": statistics.fmean(hr.on_grid(hr.daily_net(trades), grid)) if grid and trades else None,
    }
    samples: dict[str, list[float]] = {name: [] for name in values}
    if usable:
        by_day = sorted(range(len(usable)), key=lambda i: sides[usable[i]].entry_day)
        keys = [usable[i] for i in by_day]
        rows = np.array([row_of[k] for k in keys])
        buy = np.array([sides[k].buy_net for k in keys])[:, None]
        sell = np.array([sides[k].sell_net for k in keys])[:, None]
        days = [sides[k].entry_day for k in keys]
        starts = np.array([0] + [i for i in range(1, len(days)) if days[i] != days[i - 1]])
        counts = np.diff(np.append(starts, len(days)))[:, None]
        for lo in range(0, seeds, 50):
            chosen = np.where(flips[rows, lo:lo + 50], buy, sell)
            samples["mean net"] += list(chosen.sum(axis=0) / len(keys))
            samples["hit rate"] += list((chosen > 0.0).sum(axis=0) / len(keys))
            if grid:
                daily = np.add.reduceat(chosen, starts, axis=0) / counts
                samples["mean/day"] += list(daily.sum(axis=0) / len(grid))
    out = {}
    for name, value in values.items():
        sample = [float(v) for v in samples[name]]
        out[name] = {"low": hr.percentile(sample, hr.BAND[0]), "high": hr.percentile(sample, hr.BAND[1]),
                     "median": hr.percentile(sample, 50.0), "value": value,
                     "percentile": hr.percentile_of(value, sample), "seeds": len(sample)}
    return out


# --------------------------------------------------------------------------- #
# Pooled, and read over each period
# --------------------------------------------------------------------------- #


@dataclass
class Pooled:
    """Every year's results together."""

    lines: int
    arms: dict[str, list[hr.ScoredTrade]]
    counts: dict[str, dict[str, int]]
    sides: dict[Key, Side]
    pullback: list[Pullback]
    lines_by_year: dict[int, int]


def pool_years(results: Sequence[YearResult]) -> Pooled:
    arms: dict[str, list[hr.ScoredTrade]] = {name: [] for name in ARMS}
    counts = {name: {"offered": 0, "directional": 0, "below_floor": 0, "pending": 0, "acted_on": 0,
                     "could_not_simulate": 0, "trades": 0} for name in ARMS}
    sides: dict[Key, Side] = {}
    pullback: list[Pullback] = []
    for result in sorted(results, key=lambda r: r.year):
        for name, arm in result.arms.items():
            arms[name].extend(arm.trades)
            for field_name in ("offered", "directional", "below_floor", "pending", "acted_on", "could_not_simulate"):
                counts[name][field_name] += getattr(arm, field_name)
            counts[name]["trades"] += arm.n
        sides.update(result.sides)
        pullback.extend(result.pullback)
    return Pooled(sum(r.lines for r in results), arms, counts, sides, pullback,
                  {r.year: r.lines for r in results})


def _daily(values: Sequence[tuple[date, float]]) -> dict[date, float]:
    """Equal-weighted mean per entry day (``hr.daily_net``'s rule, on any per-trade number)."""
    by_day: dict[date, list[float]] = {}
    for day, value in values:
        by_day.setdefault(day, []).append(value)
    return {day: statistics.fmean(v) for day, v in sorted(by_day.items())}


def _paired(mine: dict[date, float], theirs: dict[date, float], grid: Sequence[date]) -> dict:
    """``mine - theirs`` over ``grid`` (0 on a day either has no trade), Newey-West t at the race's lag."""
    return test_of([mine.get(d, 0.0) - theirs.get(d, 0.0) for d in grid], hr.DEFAULT_HORIZON)


def _side_stats(trades: Sequence[hr.ScoredTrade], sides: Mapping[Key, Side],
                every_long: Optional[dict[date, float]] = None) -> dict:
    """One side's trades: the race's own split (number, mean net, hit rate), and its paired reads.

    Both sides against what a coin flip earns on the same lines; the longs
    also against owning every name on the same entry days (``every_long``),
    the owner's "its buys trailed holding all the ETFs".
    """
    stats = hr.split_stats("", trades).as_json()
    stats.pop("too_few", None)
    edge = _daily([(t.entry_day, t.net - (sides[t.key].buy_net + sides[t.key].sell_net) / 2.0)
                   for t in trades if t.key in sides])
    stats["vs_coin_flip_expected"] = test_of([edge[d] for d in sorted(edge)], hr.DEFAULT_HORIZON)
    if every_long is not None:
        days = sorted({t.entry_day for t in trades})
        stats["vs_always_long_every_line_same_days"] = _paired(hr.daily_net(trades), every_long, days)
    return stats


def arm_period(trades_all: Sequence[hr.ScoredTrade], pooled: Pooled, period: Period, flips: Optional[np.ndarray],
               row_of: Mapping[Key, int]) -> dict:
    """One arm over one period: the race's numbers, the coin flip, always long, longs and shorts."""
    sides = pooled.sides
    trades = [t for t in trades_all if period.contains(t.entry_day)]
    every = [(key, s) for key, s in sides.items() if period.contains(s.entry_day)]
    grid = sorted({s.entry_day for _, s in every})
    every_long = _daily([(s.entry_day, s.buy_net) for _, s in every])
    mine = hr.daily_net(trades)
    own_days = sorted(mine)
    out = {
        "trades": len(trades),
        "days_traded": len(own_days),
        "grid_days": len(grid),
        "mean_net": hr.mean_net(trades),
        "median_net": hr.median_net(trades),
        "hit_rate": hr.hit_rate(trades),
        "stop_rate": hr.stop_rate(trades),
        "mean_per_day": statistics.fmean(hr.on_grid(mine, grid)) if grid else None,
        "longs": _side_stats([t for t in trades if t.trade.side == "buy"], sides, every_long),
        "shorts": _side_stats([t for t in trades if t.trade.side == "sell"], sides),
    }
    edge = _daily([(t.entry_day, t.net - (sides[t.key].buy_net + sides[t.key].sell_net) / 2.0)
                   for t in trades if t.key in sides])
    out["vs_coin_flip_expected"] = test_of([edge[d] for d in own_days if d in edge], hr.DEFAULT_HORIZON)
    if flips is not None:
        out["coin_flip_band"] = coin_band(trades, sides, flips, row_of, grid)
    same_long = _daily([(t.entry_day, sides[t.key].buy_net) for t in trades if t.key in sides])
    out["always_long_same_lines"] = {
        "mean_net": statistics.fmean([sides[t.key].buy_net for t in trades if t.key in sides]) if trades else None,
        "paired": _paired(mine, same_long, own_days),
    }
    out["always_long_every_line"] = {
        "trades": len(every),
        "mean_net": statistics.fmean([s.buy_net for _, s in every]) if every else None,
        "hit_rate": (sum(1 for _, s in every if s.buy_net > 0) / len(every)) if every else None,
        "mean_per_day": statistics.fmean(hr.on_grid(every_long, grid)) if grid else None,
        "paired": _paired(mine, every_long, grid),
    }
    return out


def veto_vs_momentum(pooled: Pooled, period: Period) -> dict:
    """A's race arm against momentum (section 13.2's main metric): the grid is either arm's entry days."""
    mine = hr.daily_net([t for t in pooled.arms[xp.VETO] if period.contains(t.entry_day)])
    theirs = hr.daily_net([t for t in pooled.arms[momentum.NAME] if period.contains(t.entry_day)])
    grid = sorted(set(mine) | set(theirs))
    return _paired(mine, theirs, grid)


def pullback_period(pooled: Pooled, period: Period) -> dict:
    """C's filled against missed signals (13.4's checkpoint table), all and by side, for reading only."""
    out = {}
    for label, side in (("all", None), ("longs", "buy"), ("shorts", "sell")):
        rows = [p for p in pooled.pullback if period.contains(p.entry_day) and (side is None or p.side == side)]
        groups = {"filled": [p.net for p in rows if p.filled], "missed": [p.net for p in rows if not p.filled]}
        block = {name: {"n": len(v), "mean_net": statistics.fmean(v) if v else None,
                        "hit_rate": (sum(1 for x in v if x > 0) / len(v)) if v else None}
                 for name, v in groups.items()}
        f, m = groups["filled"], groups["missed"]
        block["fill_rate"] = len(f) / len(rows) if rows else None
        block["missed_minus_filled"] = (statistics.fmean(m) - statistics.fmean(f)) if f and m else None
        block["welch_t"] = welch(m, f)
        out[label] = block
    return out


def summarise(pooled: Pooled, flips: Optional[np.ndarray], row_of: Mapping[Key, int]) -> dict:
    """Every number the report reads from the race side, arm by arm and period by period."""
    first = min((s.entry_day for s in pooled.sides.values()), default=None)
    out: dict = {"lines": pooled.lines, "lines_by_year": {str(k): v for k, v in pooled.lines_by_year.items()},
                 "lines_both_sides": len(pooled.sides), "arms": {}}
    for name in ARMS:
        out["arms"][name] = {"counts": pooled.counts[name], "periods": {
            p.name: arm_period(pooled.arms[name], pooled, p, flips, row_of) for p in periods_for(name, first)}}
    out["veto_vs_momentum"] = {p.name: veto_vs_momentum(pooled, p) for p in periods_for(xp.VETO, first)}
    out["pullback_filled_vs_missed"] = {p.name: pullback_period(pooled, p) for p in periods_for(xp.LIMIT, first)}
    return out


__all__ = ["ARMS", "FrameCloses", "FrameOhlc", "Pooled", "Pullback", "Side", "YearResult", "arm_period",
           "arm_result", "coin_band", "coin_flips", "filled_or_missed", "pool_years", "race_year", "race_years",
           "settings", "summarise", "veto_vs_momentum"]
