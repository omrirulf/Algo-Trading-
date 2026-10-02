"""The regime split (pre-registration section 13.10): the state of a session from the closes before it only.

Offline, on made-up closes: the trend and the volatility tercile of a
session must read VT's final closes up to the previous session's close and
nothing on or after its own day; the cut-offs must be numpy's 'linear' 1/3
and 2/3 quantiles of each session's volatility dated by its own close, up to
the window's end; the split must give each state's days, mean and the
race's own Newey-West t; and while the cut-offs are not fixed, the
volatility part must say so everywhere.
"""

from __future__ import annotations

import math
import statistics
from datetime import date, timedelta

import numpy as np
import pytest

from analysis import regimes
from analysis.horse_race import newey_west_t


def _closes(n: int, start: date = date(2024, 1, 1), seed: int = 7, vol: float = 0.01) -> list[tuple[date, float]]:
    rng = np.random.default_rng(seed)
    days = [start + timedelta(days=i) for i in range(n)]
    values = 50.0 * np.exp(np.cumsum(rng.normal(0.0002, vol, n)))
    return [(d, float(v)) for d, v in zip(days, values)]


def _manual_vol(values) -> float:
    returns = [math.log(b / a) for a, b in zip(values, values[1:])]
    return statistics.stdev(returns) * math.sqrt(252)


# --------------------------------------------------------------------------- #
# The constants
# --------------------------------------------------------------------------- #


def test_the_registered_settings():
    assert regimes.VT_CUTOFF_WINDOW_END == date(2026, 9, 30)
    assert (regimes.TREND_CLOSES, regimes.VOL_RETURNS, regimes.SESSIONS_PER_YEAR) == (200, 21, 252)
    assert (regimes.RACE_LAG, regimes.FUND_LAG) == (3, 5)
    assert regimes.TERCILES == (1 / 3, 2 / 3)
    # None until the integrator writes the registered numbers in; then two finite numbers, low below high.
    cutoffs = regimes.VOL_CUTOFFS
    assert cutoffs is None or (len(cutoffs) == 2 and math.isfinite(cutoffs[0]) and cutoffs[0] < cutoffs[1])


# --------------------------------------------------------------------------- #
# Volatility and the cut-offs
# --------------------------------------------------------------------------- #


def test_volatility_is_the_annualised_sample_deviation_of_21_log_returns():
    closes = _closes(30)
    values = [v for _, v in closes]
    assert regimes.realized_vol(values[:22]) == pytest.approx(_manual_vol(values[:22]), rel=1e-12)
    series = regimes.vol_series(closes)
    assert len(series) == len(closes) - 21
    # Dated by its own close: the first value is at the 22nd close, from the 21 returns ending there.
    assert series[0][0] == closes[21][0]
    assert series[0][1] == regimes.realized_vol(values[0:22])
    assert series[-1] == (closes[-1][0], regimes.realized_vol(values[-22:]))
    with pytest.raises(ValueError):
        regimes.realized_vol(values[:2])


def test_the_cut_offs_are_numpys_linear_terciles_up_to_the_window_end_and_nothing_after():
    closes = _closes(400)
    last = closes[300][0]
    vols = [v for d, v in regimes.vol_series(closes) if d <= last]
    expected = np.quantile(vols, [1 / 3, 2 / 3])                     # numpy's default method: 'linear'
    c1, c2 = regimes.tercile_cutoffs(closes, last)
    assert (c1, c2) == (float(expected[0]), float(expected[1]))
    assert (c1, c2) == tuple(float(x) for x in np.quantile(vols, [1 / 3, 2 / 3], method="linear"))
    assert c1 < c2
    # A wild move after the window's end changes nothing.
    later = [(d, v * (3.0 if d > last and i % 2 else 1.0)) for i, (d, v) in enumerate(closes)]
    assert regimes.tercile_cutoffs(later, last) == (c1, c2)
    # About a third of the window's sessions in each tercile.
    counts = {s: sum(1 for v in vols if regimes.tercile(v, (c1, c2)) == s) for s in regimes.VOL_STATES}
    assert all(abs(n - len(vols) / 3) <= 1 for n in counts.values()), counts
    # The default window is the registered one.
    assert regimes.tercile_cutoffs(closes) == regimes.tercile_cutoffs(closes, date(2026, 9, 30))


def test_too_few_closes_or_flat_volatility_cannot_make_cut_offs():
    with pytest.raises(ValueError, match="fewer than 22"):
        regimes.tercile_cutoffs(_closes(21))
    # Up, down, up, down by the same step: every 21-day window has exactly the same volatility.
    flat = [(date(2024, 1, 1) + timedelta(days=i), 200.0 if i % 2 else 100.0) for i in range(40)]
    assert len({vol for _, vol in regimes.vol_series(flat)}) == 1
    with pytest.raises(ValueError, match="c1 < c2"):
        regimes.tercile_cutoffs(flat)


def test_a_tercile_is_low_up_to_c1_mid_up_to_c2_and_high_above():
    cutoffs = (0.10, 0.20)
    assert regimes.tercile(0.05, cutoffs) == regimes.LOW
    assert regimes.tercile(0.10, cutoffs) == regimes.LOW               # equal to c1: low
    assert regimes.tercile(0.15, cutoffs) == regimes.MID
    assert regimes.tercile(0.20, cutoffs) == regimes.MID               # equal to c2: mid
    assert regimes.tercile(0.2000001, cutoffs) == regimes.HIGH
    for bad in ((0.2, 0.1), (0.1, 0.1), (0.1,), (float("nan"), 0.2)):
        with pytest.raises(ValueError):
            regimes.tercile(0.15, bad)


# --------------------------------------------------------------------------- #
# A session's state
# --------------------------------------------------------------------------- #


def test_a_sessions_state_reads_the_closes_before_it_and_nothing_on_or_after_its_day():
    closes = _closes(260)
    values = [v for _, v in closes]
    day = closes[230][0]
    cutoffs = (0.12, 0.18)
    label = regimes.labels(closes, [day], cutoffs)[day]
    previous = values[229]
    mean = math.fsum(values[30:230]) / 200
    assert label["trend"] == (regimes.ABOVE if previous > mean else regimes.BELOW)
    assert label["vol"] == regimes.tercile(regimes.realized_vol(values[208:230]), cutoffs)
    # The vol a state uses is the cut-off series' value of the session before (dated by its own close).
    by_day = dict(regimes.vol_series(closes))
    assert regimes.realized_vol(values[208:230]) == by_day[closes[229][0]]
    # Rewrite the session's own close and everything after it: the label must not move.
    changed = [(d, v * (5.0 if d >= day else 1.0)) for d, v in closes]
    assert regimes.labels(changed, [day], cutoffs)[day] == label
    # A session between two closes (a day with no close) reads the last close before it.
    gap = [c for c in closes if c[0] != closes[229][0]]
    between = regimes.labels(gap, [closes[229][0]], cutoffs)[closes[229][0]]
    assert between == regimes.labels(closes, [closes[229][0]], cutoffs)[closes[229][0]]


def test_the_trend_is_above_only_when_strictly_above_and_unknown_under_200_closes():
    start = date(2024, 1, 1)
    flat = [(start + timedelta(days=i), 100.0) for i in range(210)]
    after = start + timedelta(days=210)
    # The previous close equals its 200-close mean: not above, so "below".
    assert regimes.labels(flat, [after], None)[after]["trend"] == regimes.BELOW
    rising = [(d, 100.0 + i) for i, (d, _) in enumerate(flat)]
    assert regimes.labels(rising, [after], None)[after]["trend"] == regimes.ABOVE
    falling = [(d, 400.0 - i) for i, (d, _) in enumerate(flat)]
    assert regimes.labels(falling, [after], None)[after]["trend"] == regimes.BELOW
    # Exactly 200 closes before the session is enough; 199 is not.
    assert regimes.labels(rising, [flat[200][0]], None)[flat[200][0]]["trend"] == regimes.ABOVE
    assert regimes.labels(rising, [flat[199][0]], None)[flat[199][0]]["trend"] is None


def test_volatility_needs_22_closes_and_says_not_fixed_while_the_cut_offs_are_none():
    closes = _closes(40)
    early, ready = closes[21][0], closes[22][0]       # 21 and 22 closes before the session
    got = regimes.labels(closes, [early, ready], (0.1, 0.2))
    assert got[early]["vol"] is None and got[ready]["vol"] in regimes.VOL_STATES
    unfixed = regimes.labels(closes, [early, ready], None)
    assert {label["vol"] for label in unfixed.values()} == {regimes.NOT_FIXED}


def test_closes_are_sorted_and_a_repeated_day_or_a_bad_close_is_refused():
    closes = _closes(230)
    day = closes[-1][0] + timedelta(days=1)
    assert regimes.labels(list(reversed(closes)), [day], (0.1, 0.2)) == regimes.labels(closes, [day], (0.1, 0.2))
    with pytest.raises(ValueError, match="two closes"):
        regimes.labels(closes + [closes[5]], [day], None)
    for bad in (0.0, -1.0, float("nan")):
        with pytest.raises(ValueError, match="positive"):
            regimes.labels(closes[:-1] + [(closes[-1][0], bad)], [day], None)


# --------------------------------------------------------------------------- #
# Counters, split and record
# --------------------------------------------------------------------------- #

D = [date(2026, 10, 1) + timedelta(days=i) for i in range(8)]
LABELS = {
    D[0]: {"trend": "above", "vol": "low"},
    D[1]: {"trend": "above", "vol": "mid"},
    D[2]: {"trend": "below", "vol": "high"},
    D[3]: {"trend": "above", "vol": "low"},
    D[4]: {"trend": "below", "vol": "low"},
    D[5]: {"trend": None, "vol": None},
    D[6]: {"trend": "above", "vol": "high"},
}


def test_counters_count_sessions_per_state_and_nothing_else():
    count = regimes.counters(LABELS)
    assert count == {"sessions": 7, "first": D[0].isoformat(), "last": D[6].isoformat(),
                     "trend": {"above": 4, "below": 2, "unknown": 1},
                     "vol": {"low": 3, "mid": 1, "high": 2, "unknown": 1}}
    unfixed = {d: {"trend": l["trend"], "vol": regimes.NOT_FIXED} for d, l in LABELS.items()}
    assert regimes.counters(unfixed)["vol"] == regimes.NOT_FIXED
    assert regimes.counters({})["sessions"] == 0


def test_the_split_gives_each_states_days_mean_and_the_races_newey_west_t():
    series = {"model - vt": {D[i]: 0.001 * (i + 1) for i in range(8)},
              "momentum - vt": {D[0]: -0.002, D[3]: 0.004}}
    out = regimes.split(series, LABELS, 3)
    above = [0.001, 0.002, 0.004, 0.007]                   # D0, D1, D3, D6 in date order
    got = out["trend"]["above"]["model - vt"]
    assert got["days"] == 4 and got["mean"] == pytest.approx(statistics.fmean(above), rel=1e-15)
    assert got["t"] == newey_west_t(above, 3)
    assert out["trend"]["below"]["model - vt"]["days"] == 2
    low = out["vol"]["low"]["model - vt"]
    assert low["days"] == 3 and low["t"] == newey_west_t([0.001, 0.004, 0.005], 3)
    # D5 has no state and D7 no label: neither is in any split.
    total = sum(out["trend"][s]["model - vt"]["days"] for s in regimes.TREND_STATES)
    assert total == 6
    # A series with too few days in a state still has its row.
    assert out["vol"]["mid"]["momentum - vt"] == {"days": 0, "mean": None, "t": None}
    assert out["vol"]["low"]["momentum - vt"] == {"days": 2, "mean": pytest.approx(0.001), "t": newey_west_t(
        [-0.002, 0.004], 3)}
    assert set(out["vol"]) == set(regimes.VOL_STATES) and set(out["trend"]) == set(regimes.TREND_STATES)


def test_the_record_uses_lag_3_for_the_race_and_lag_5_for_the_funds():
    race = {"model - vt": {d: 0.001 * ((i * 7) % 5 - 2) for i, d in enumerate(D)}}
    funds = {"momentum - vt": {d: 0.0005 * ((i * 3) % 4 - 1.5) for i, d in enumerate(D)}}
    got = regimes.record(race, funds, LABELS, (0.1, 0.2))
    assert set(got) == {"race", "funds", "counters", "cutoffs"}
    assert got["race"] == regimes.split(race, LABELS, 3)
    assert got["funds"] == regimes.split(funds, LABELS, 5)
    assert got["counters"] == regimes.counters(LABELS)
    assert got["cutoffs"] == [0.1, 0.2]


def test_while_the_cut_offs_are_not_fixed_every_volatility_part_says_so():
    closes = _closes(260)
    sessions = [d for d, _ in closes[200:]]
    labels = regimes.labels(closes, sessions, None)
    series = {"model - vt": {d: 0.001 for d in sessions}}
    got = regimes.record(series, series, labels, None)
    assert got["cutoffs"] == regimes.NOT_FIXED == "cut-offs not fixed yet"
    assert got["race"]["vol"] == got["funds"]["vol"] == got["counters"]["vol"] == regimes.NOT_FIXED
    assert got["race"]["trend"]["above"]["model - vt"]["days"] + got["race"]["trend"]["below"]["model - vt"]["days"] \
        == len(sessions)
    assert regimes.split(series, labels, 3)["vol"] == regimes.NOT_FIXED
    # Labels made with cut-offs, recorded as unfixed: the record still says not fixed.
    fixed = regimes.labels(closes, sessions, (0.1, 0.2))
    assert regimes.record(series, series, fixed, None)["race"]["vol"] == regimes.NOT_FIXED


def test_the_module_is_pure_arithmetic():
    import inspect

    text = inspect.getsource(regimes)
    for word in ("open(", "write_text", "requests", "yfinance", "os.environ", "getenv", "datetime.now"):
        assert word not in text, word
