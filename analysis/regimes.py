"""The regime split: the race's and the funds' results by market state (VT's trend and VT's volatility).

The owner's instruction of 2 Oct 2026 (item 7): "Split the race and fund
results by market state: VT above or below its 200-day average, and VT
21-day realized volatility terciles (fix the cut-offs at registration).
Hidden until the checkpoints." Pre-registration section 13.10 holds the
rule; this module is its arithmetic.

Why: a result over the whole window mixes calm, rising markets with
falling, nervous ones. A rule can earn its whole result in one kind of
market and lose in the other, and the mean alone does not show it. The
split shows in which market state each result was made. It is a reading
aid: **descriptive only**. It decides nothing, it is not a test in the
Benjamini-Hochberg family (section 13.5), and it changes no rule.

The state of a session uses only what was known before it opened: VT's
final closes up to the **previous** session's close (the last VT close
dated before the session). The closes are VT's final daily closes as the
race and the funds read them (``analysis.baseline_compare.OhlcFetcher``'s
``Close``: Yahoo with ``auto_adjust=False``, adjusted for splits and not for
dividends); the cut-offs and the labels must be read from the same kind of
close.

* **trend** (``labels``): ``"above"`` if that previous close is above the
  mean of VT's last 200 final closes up to and including it, else
  ``"below"``. A close exactly equal to the mean is not above it, so it is
  ``"below"``: "below" means "not above". None with fewer than 200 closes.
* **volatility** (``labels``): the annualised sample standard deviation
  (x sqrt(252)) of VT's last 21 daily log returns up to that previous close
  (``realized_vol``), put in a tercile by two fixed cut-offs c1 < c2:
  ``"low"`` if vol <= c1, ``"mid"`` if c1 < vol <= c2, ``"high"`` if vol > c2
  (``tercile``). None with fewer than 22 closes.

**The cut-offs** (``VOL_CUTOFFS``) are fixed once, at registration, by a
rule over a window that ends before it: ``tercile_cutoffs``, the 1/3 and
2/3 quantiles of VT's daily 21-day volatility from its first 21 returns to
2026-09-30. The sandbox this was written in cannot reach a price source, so
the history screen's stress kind computes them from the prices it fetches
(``history.stress``, ``results.json`` key ``regime_cutoffs``) and the numbers
are then written into ``VOL_CUTOFFS`` and pre-registration section 13.10.
Until then, the volatility split says "cut-offs not fixed yet".

One difference to keep in mind. For the cut-offs, each session's volatility
is dated by its **own** close (the 21 returns ending at that close): they
describe the whole window, so each number is filed under the day it was
measured. A session's **state** uses the volatility up to the **previous**
close, because the state must be known before the session opens. Both use
the same function on the same 21 returns; only the session a number is
filed under differs, by one.

**Hidden until the checkpoints** (section 13.1's pattern): between
checkpoints only ``counters`` -- sessions per state, the market's state
only, no result -- may be written; ``record`` is computed once at each
checkpoint and kept unchanged after it.

Pure arithmetic: no prices are fetched, no files, no clock, no network.
"""

from __future__ import annotations

import math
from bisect import bisect_left
from dataclasses import dataclass
from datetime import date, datetime
from typing import Final, Iterable, Mapping, Optional, Sequence

import numpy as np

#: The market whose state is read: the world index fund the race and the funds are measured against.
INDEX_TICKER: Final[str] = "VT"
#: Trend: the previous final close against the mean of the last 200 final closes up to and including it.
TREND_CLOSES: Final[int] = 200
#: Volatility: the last 21 daily log returns (22 final closes) up to the previous close.
VOL_RETURNS: Final[int] = 21
#: Volatility is annualised with the square root of this many sessions a year.
SESSIONS_PER_YEAR: Final[int] = 252
#: The quantiles that cut the volatility series into terciles (numpy's default method, 'linear').
TERCILES: Final[tuple[float, float]] = (1.0 / 3.0, 2.0 / 3.0)
#: The last day of the cut-off window: VT's daily 21-day volatility from its first 21 returns to this day,
#: inclusive. It ends before the registration (2 Oct 2026), so nothing can be fitted to the cut-offs.
VT_CUTOFF_WINDOW_END: Final[date] = date(2026, 9, 30)
#: The two volatility cut-offs (low/mid, mid/high), annualised. Fixed at registration from
#: ``tercile_cutoffs`` over VT's final closes from its first 21 returns (2008-07-28) to
#: ``VT_CUTOFF_WINDOW_END`` inclusive, 4,573 sessions, computed once by the history screen's stress kind
#: (workflow run 37013435615, ``docs/research/history/2026-10-stress-periods/results.json``, key
#: ``regime_cutoffs``) and written into pre-registration section 13.10 with its own Amendments row
#: (2026-10-02). Nothing can move them. Were it None, the volatility split would report ``NOT_FIXED``.
VOL_CUTOFFS: Final[Optional[tuple[float, float]]] = (0.11302353418809083, 0.16965241927688823)

#: The trend states.
ABOVE: Final[str] = "above"
BELOW: Final[str] = "below"
TREND_STATES: Final[tuple[str, ...]] = (ABOVE, BELOW)
#: The volatility terciles.
LOW: Final[str] = "low"
MID: Final[str] = "mid"
HIGH: Final[str] = "high"
VOL_STATES: Final[tuple[str, ...]] = (LOW, MID, HIGH)
#: What the volatility split says, in a label and in a record, while ``VOL_CUTOFFS`` is None.
NOT_FIXED: Final[str] = "cut-offs not fixed yet"
#: Sessions with no state (too few closes) are counted under this key in ``counters``.
UNKNOWN: Final[str] = "unknown"
#: Newey-West lags, as registered: race trades overlap for 3 sessions; the funds' daily returns use lag 5.
RACE_LAG: Final[int] = 3
FUND_LAG: Final[int] = 5

Closes = Sequence[tuple[date, float]]
Label = dict[str, Optional[str]]


@dataclass(frozen=True)
class _Series:
    """Final closes in date order, one per day."""

    days: tuple[date, ...]
    closes: tuple[float, ...]


def _day(value: date) -> date:
    return value.date() if isinstance(value, datetime) else value


def _series(closes: Closes) -> _Series:
    """``closes`` in date order; a repeated day or a close that is not a positive number is refused."""
    rows = sorted(((_day(d), float(c)) for d, c in closes), key=lambda row: row[0])
    for (before, _), (day, _) in zip(rows, rows[1:]):
        if day == before:
            raise ValueError(f"two closes for {day}")
    for day, close in rows:
        if not math.isfinite(close) or close <= 0:
            raise ValueError(f"close {close!r} on {day} is not a positive number")
    return _Series(tuple(d for d, _ in rows), tuple(c for _, c in rows))


def _checked(cutoffs: Sequence[float]) -> tuple[float, float]:
    """Two finite cut-offs, the first below the second."""
    if len(cutoffs) != 2:
        raise ValueError(f"two cut-offs are needed, got {len(cutoffs)}")
    c1, c2 = float(cutoffs[0]), float(cutoffs[1])
    if not (math.isfinite(c1) and math.isfinite(c2) and c1 < c2):
        raise ValueError(f"the cut-offs must be finite with c1 < c2, got {c1!r} and {c2!r}")
    return c1, c2


def realized_vol(closes: Sequence[float]) -> float:
    """The annualised (x sqrt(252)) sample standard deviation of the daily log returns of ``closes``.

    The state and the cut-offs both call this on 22 consecutive final closes
    (21 returns); the sample standard deviation divides by n - 1.
    """
    values = np.asarray(closes, dtype="float64")
    if len(values) < 3:
        raise ValueError("at least 3 closes (2 returns) are needed for a sample standard deviation")
    returns = np.diff(np.log(values))
    return float(np.std(returns, ddof=1) * math.sqrt(SESSIONS_PER_YEAR))


def vol_series(closes: Closes) -> list[tuple[date, float]]:
    """Each session's 21-day volatility, **dated by its own close**: the 21 returns ending at that close.

    This is the series the cut-offs are read from (``tercile_cutoffs``). A
    session's state uses the value of the session before it (``labels``).
    The first value is at the 22nd close.
    """
    series = _series(closes)
    window = VOL_RETURNS + 1
    return [(series.days[j], realized_vol(series.closes[j + 1 - window: j + 1]))
            for j in range(window - 1, len(series.closes))]


def tercile_cutoffs(closes: Closes, last: date = VT_CUTOFF_WINDOW_END) -> tuple[float, float]:
    """The registration's two cut-offs: the 1/3 and 2/3 quantiles of the daily 21-day volatility to ``last``.

    The volatility series is ``vol_series`` (each session's value from the
    21 returns ending at its own close), from VT's first 21 returns to
    ``last`` inclusive. The quantiles are numpy's default method, 'linear'
    (``numpy.quantile``). Refused when there is no value up to ``last`` or
    when the two quantiles are equal (no terciles can be cut).
    """
    vols = [vol for day, vol in vol_series(closes) if day <= last]
    if not vols:
        raise ValueError(f"no 21-day volatility up to {last}: fewer than {VOL_RETURNS + 1} closes")
    low, high = np.quantile(np.asarray(vols, dtype="float64"), TERCILES)
    return _checked((float(low), float(high)))


def tercile(vol: float, cutoffs: Sequence[float]) -> str:
    """``"low"`` if vol <= c1, ``"mid"`` if c1 < vol <= c2, ``"high"`` if vol > c2."""
    c1, c2 = _checked(cutoffs)
    if vol <= c1:
        return LOW
    if vol <= c2:
        return MID
    return HIGH


def labels(closes: Closes, sessions: Iterable[date], cutoffs: Optional[Sequence[float]]) -> dict[date, Label]:
    """Each session's market state, from VT's final closes up to the previous session's close only.

    ``{day: {"trend": "above" | "below" | None, "vol": "low" | "mid" | "high" | None | NOT_FIXED}}``,
    in date order. The previous close is the last close in ``closes`` dated
    before the session, so a close on or after the session is never read.
    ``trend`` is None with fewer than 200 closes before the session; ``vol``
    is None with fewer than 22, and ``NOT_FIXED`` for every session while
    ``cutoffs`` is None.
    """
    series = _series(closes)
    fixed = None if cutoffs is None else _checked(cutoffs)
    window = VOL_RETURNS + 1
    out: dict[date, Label] = {}
    for day in sorted({_day(d) for d in sessions}):
        known = bisect_left(series.days, day)          # closes dated before ``day``
        trend: Optional[str] = None
        if known >= TREND_CLOSES:
            mean = math.fsum(series.closes[known - TREND_CLOSES: known]) / TREND_CLOSES
            trend = ABOVE if series.closes[known - 1] > mean else BELOW
        vol: Optional[str] = NOT_FIXED if fixed is None else None
        if fixed is not None and known >= window:
            vol = tercile(realized_vol(series.closes[known - window: known]), fixed)
        out[day] = {"trend": trend, "vol": vol}
    return out


def _not_fixed(labels: Mapping[date, Mapping[str, Optional[str]]]) -> bool:
    return any(label.get("vol") == NOT_FIXED for label in labels.values())


def counters(labels: Mapping[date, Mapping[str, Optional[str]]]) -> dict:
    """Sessions per trend state and per volatility tercile: the market's state only, no result.

    This is all that may be written between checkpoints. Sessions with no
    state (too few closes) are counted as ``"unknown"``; while the cut-offs
    are not fixed, the volatility part is ``NOT_FIXED``.
    """
    trend = {state: 0 for state in (*TREND_STATES, UNKNOWN)}
    vol = {state: 0 for state in (*VOL_STATES, UNKNOWN)}
    for label in labels.values():
        state = label.get("trend")
        trend[state if state in TREND_STATES else UNKNOWN] += 1
        state = label.get("vol")
        vol[state if state in VOL_STATES else UNKNOWN] += 1
    days = sorted(labels)
    return {"sessions": len(days), "first": days[0].isoformat() if days else None,
            "last": days[-1].isoformat() if days else None, "trend": trend,
            "vol": NOT_FIXED if _not_fixed(labels) else vol}


def _summary(values: Sequence[float], lag: int) -> dict:
    """Days, mean and Newey-West t (``analysis.horse_race.newey_west_t``) of one state's values in date order."""
    # Imported here: the race may import this module for its checkpoint record, and a module-level
    # import of the race from here would then be circular.
    from analysis.horse_race import newey_west_t

    n = len(values)
    return {"days": n, "mean": math.fsum(values) / n if n else None,
            "t": newey_west_t(list(values), lag) if n >= 2 else None}


def split(series: Mapping[str, Mapping[date, float]], labels: Mapping[date, Mapping[str, Optional[str]]],
          lag: int) -> dict:
    """Each series' days, mean and Newey-West t at ``lag``, per trend state and per volatility tercile.

    ``series`` maps a name to a daily series the caller has already
    differenced, named for what it is (``"model - vt"``: the model arm's
    daily result minus VT's on the same days). A day goes to the state of
    its label; a day with no label, or no state in it, is left out of that
    split. Each state's values are taken in date order, and the t treats
    them as one series.

    ``{"trend": {"above": {name: {"days", "mean", "t"}}, "below": {...}},
    "vol": {"low": {...}, "mid": {...}, "high": {...}} or NOT_FIXED}``.

    Descriptive only: it decides nothing and is not a test in the
    Benjamini-Hochberg family (pre-registration sections 13.5 and 13.10).
    """
    groups: dict[tuple[str, str], dict[str, list[float]]] = {
        **{("trend", s): {} for s in TREND_STATES}, **{("vol", s): {} for s in VOL_STATES}}
    for name, by_day in series.items():
        for key in groups:
            groups[key][name] = []
        for day in sorted(by_day):
            label = labels.get(day)
            if label is None:
                continue
            value = float(by_day[day])
            if label.get("trend") in TREND_STATES:
                groups[("trend", label["trend"])][name].append(value)
            if label.get("vol") in VOL_STATES:
                groups[("vol", label["vol"])][name].append(value)
    out: dict = {"trend": {}, "vol": {}}
    for (kind, state), by_name in groups.items():
        out[kind][state] = {name: _summary(values, lag) for name, values in by_name.items()}
    if _not_fixed(labels):
        out["vol"] = NOT_FIXED
    return out


def record(race_series: Mapping[str, Mapping[date, float]], fund_series: Mapping[str, Mapping[date, float]],
           labels: Mapping[date, Mapping[str, Optional[str]]], cutoffs: Optional[Sequence[float]]) -> dict:
    """A checkpoint's regime split: the race's series at lag 3, the funds' at lag 5, the counters, the cut-offs.

    ``{"race": split(..., lag=3), "funds": split(..., lag=5), "counters": counters(labels),
    "cutoffs": [c1, c2] or NOT_FIXED}``. Computed once at each checkpoint
    and kept unchanged; while ``cutoffs`` is None every volatility part is
    ``NOT_FIXED``. Descriptive only, as ``split``.
    """
    race = split(race_series, labels, RACE_LAG)
    funds = split(fund_series, labels, FUND_LAG)
    count = counters(labels)
    if cutoffs is None:
        race["vol"] = funds["vol"] = count["vol"] = NOT_FIXED
    return {"race": race, "funds": funds, "counters": count,
            "cutoffs": NOT_FIXED if cutoffs is None else list(_checked(cutoffs))}


__all__ = [
    "ABOVE", "BELOW", "FUND_LAG", "HIGH", "INDEX_TICKER", "LOW", "MID", "NOT_FIXED", "RACE_LAG", "SESSIONS_PER_YEAR",
    "TERCILES", "TREND_CLOSES", "TREND_STATES", "UNKNOWN", "VOL_CUTOFFS", "VOL_RETURNS", "VOL_STATES",
    "VT_CUTOFF_WINDOW_END", "counters", "labels", "realized_vol", "record", "split", "tercile", "tercile_cutoffs",
    "vol_series",
]
