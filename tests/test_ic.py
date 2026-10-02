"""The daily IC report (``analysis/ic.py``), on hand-built lines and bars. No network, no journal of record.

Every case builds its own journal lines and its own bars, so nothing here
reads a real IC: no IC value of the real journal may be computed before the
22 Dec 2026 checkpoint (the owner's instruction of 2 Oct 2026).
"""

from __future__ import annotations

import inspect
import json
import math
import random
import statistics
from datetime import date, datetime, time, timedelta, timezone

import pytest

from analysis import ic
from analysis.metrics import spearman
from config.market_calendar import is_trading_day

UTC = timezone.utc

#: NYSE sessions from 28 Sep 2026 to the end of 2026, by the repo's own calendar (26 Nov is not one).
SESSIONS = [d for d in (date(2026, 9, 28) + timedelta(days=i) for i in range(95)) if is_trading_day(d)]


def at(day: date, hour: int = 15, minute: int = 0) -> datetime:
    return datetime.combine(day, time(hour, minute), UTC)


def make_line(ticker: str, day: date, hour: int = 15, minute: int = 0, **scores) -> ic.IcLine:
    """An answered line written straight as an ``IcLine``; every score not given is None."""
    return ic.IcLine(ticker=ticker, day=day, timestamp=at(day, hour, minute),
                     scores={name: scores.get(name) for name in ic.ALL_SCORES})


def payload(ticker: str = "AAA", when: str = "2026-10-01T15:00:00+00:00", *, signal: bool = True,
            blend=0.1, news=0.0, technical=0.2, fundamental=-0.1, analyst=0.3, insider=0.0,
            momentum=("BULLISH", 0.5), held=None, error=None, **extra) -> dict:
    """A production journal line with the fields the IC report reads."""
    out = {
        "ts_utc": when,
        "ticker": ticker,
        "context": {"technicals": {"return_63d": 0.05}},
        "signal": ({"ticker": ticker, "bias": "NEUTRAL", "conviction": 0.0, "rationale": "r",
                    "news_score": news, "technical_score": technical, "fundamental_score": fundamental,
                    "analyst_score": analyst, "insider_score": insider, "key_factors": []}
                   if signal else None),
        "error": error,
        "blend": {"mode": "shadow", "composite": blend} if signal else None,
        "arms": ({"momentum": {"bias": momentum[0], "conviction": momentum[1], "rationale": "m"}}
                 if momentum is not None else {}),
        "held": held,
    }
    out.update(extra)
    return out


def priced(days=SESSIONS) -> list[tuple[date, float, float]]:
    """Bars whose Opens are all different, so a price names the bar it came from."""
    return [(d, 100.0 + i, 100.5 + i) for i, d in enumerate(days)]


def bars_from_returns(returns: dict[str, dict[date, float]], days=SESSIONS) -> dict:
    """Each bar opens at 100 and closes at 100 x (1 + that name's return that day; 0 if none given)."""
    return {name: [(d, 100.0, 100.0 * (1.0 + by_day.get(d, 0.0))) for d in days]
            for name, by_day in returns.items()}


# --------------------------------------------------------------------------- #
# The registered settings
# --------------------------------------------------------------------------- #


def test_the_registered_settings():
    assert ic.IC_START == date(2026, 9, 28)
    assert ic.IC_REGISTRATION == date(2026, 12, 22)
    assert ic.SHADOW_START == date(2027, 1, 1)
    assert ic.HORIZONS == (1, 3)
    assert ic.SCORES == ("blend", "news", "technical", "fundamental", "analyst", "insider")
    assert ic.COMPARATOR == "momentum"
    assert ic.MIN_NAMES == 10
    assert ic.MDE_T == 2.4
    assert ic.NW_LAG == {h: h for h in ic.HORIZONS}, "the Newey-West lag is the horizon (the race's convention)"
    assert ic.UNIVERSES == ("production", "shadow")
    assert ic.UNIVERSE_START == {"production": ic.IC_START, "shadow": ic.SHADOW_START}
    assert (ic.MAIN_SCORE, ic.MAIN_HORIZON) == ("blend", 3)
    assert ic.MAIN_SCORE in ic.SCORES and ic.MAIN_HORIZON in ic.HORIZONS
    assert ic.PAIRED == ("blend", "momentum")
    assert ic.COUNTER_KEYS == ("answered_lines", "lines_with_score", "line_days")
    assert (ic.N_EFF_MIN_RETURNS, ic.N_EFF_MIN_DATES, ic.N_EFF_MIN_COVERAGE) == (20, 20, 0.9)


def test_the_record_carries_every_n_eff_setting():
    found = ic.settings()
    assert found["n_eff_min_coverage"] == ic.N_EFF_MIN_COVERAGE == 0.9
    assert (found["n_eff_min_returns"], found["n_eff_min_dates"]) == (20, 20)
    for phrase in ("90%", "mean return across the names taken out", "N^2 / max(sum(C^2) - N(N - 1) / (T - 1), N)",
                   "n_eff_raw = N^2 / sum(C^2)"):
        assert phrase in found["n_eff"], phrase


def test_the_shadow_start_is_the_universes_own():
    universe = pytest.importorskip("config.shadow_universe")
    assert ic.SHADOW_START == universe.START


def test_the_card_carries_the_registered_settings():
    text = ic.card()
    for phrase in ("2026-09-28", "2027-01-01", "22 Dec 2026", "**t = 2.4**", "**10 names**", "h = 1 and 3",
                   "lag = horizon", "Price only", "proposed; the owner confirms at registration",
                   "blended score's IC at 3 sessions", "Benjamini-Hochberg", "Deflated Sharpe Ratio",
                   "No IC value is written to any file, page or log", "Shadow only",
                   "(a signal about this ticker, not held)", "webhook unreachable", "**90%**",
                   "The common move is taken out", "N^2 / max(sum of C^2 - N(N - 1) / (T - 1), N)", "n_eff_raw"):
        assert phrase in text, phrase
    assert "no error" not in text, "an error written after the answer does not take a line out (the race's rule)"


# --------------------------------------------------------------------------- #
# Reading lines
# --------------------------------------------------------------------------- #


def test_an_answered_line_carries_every_score():
    line = ic.line_from(payload(blend=0.12, news=0.0, technical=0.4, fundamental=-0.2, analyst=None,
                                insider=0.1, momentum=("BEARISH", 0.35)))
    assert line is not None
    assert (line.ticker, line.day) == ("AAA", date(2026, 10, 1))
    assert line.scores == {"blend": 0.12, "news": 0.0, "technical": 0.4, "fundamental": -0.2, "analyst": None,
                           "insider": 0.1, "momentum": -0.35}


@pytest.mark.parametrize("arms, expected", [
    ({"momentum": {"bias": "BULLISH", "conviction": 0.4}}, 0.4),
    ({"momentum": {"bias": "BEARISH", "conviction": 0.4}}, -0.4),
    ({"momentum": {"bias": "BEARISH", "conviction": 1.0}}, -1.0),
    ({"momentum": {"bias": "NEUTRAL", "conviction": 0.0}}, 0.0),
    ({"momentum": {"bias": "NEUTRAL"}}, 0.0),
    ({"momentum": {"bias": "BULLISH"}}, None),
    ({"momentum": {"bias": "BULLISH", "conviction": True}}, None),
    ({"momentum": {"bias": "SIDEWAYS", "conviction": 0.3}}, None),
    ({"momentum": {"error": "ValueError: boom"}}, None),
    ({}, None),
    (None, None),
])
def test_the_momentum_sign(arms, expected):
    assert ic.momentum_score(arms) == expected


@pytest.mark.parametrize("line", [
    payload(held=True, signal=False),
    payload(held=True),
    payload(signal=False, error="invalid LLM output: conviction"),
    payload(error="answered for MSFT"),
    payload(when="not a time"),
    {"ticker": "", "signal": None},
    ["not", "a", "line"],
])
def test_held_failed_and_unreadable_lines_are_left_out(line):
    assert ic.line_from(line) is None


@pytest.mark.parametrize("error", [
    "webhook unreachable: x",
    "engine unavailable: paper engine down",
    "something went wrong after the answer",
])
def test_an_error_written_after_the_answer_keeps_the_line_as_in_the_race(error):
    """The race counts a line with a signal about its own ticker, whatever went wrong after (``model_answered``)."""
    reader = pytest.importorskip("analysis.reader")
    line = ic.line_from(payload(error=error, blend=0.2))
    assert line is not None and line.scores["blend"] == 0.2
    entry = reader.entry_from(payload(error=error))
    assert entry.model_answered and not entry.held


def test_a_null_score_leaves_the_line_out_of_that_score_only():
    line = ic.line_from(payload(blend=None, analyst=None, momentum=None))
    assert line is not None
    assert line.scores["blend"] is None and line.scores["analyst"] is None and line.scores["momentum"] is None
    assert line.scores["technical"] == 0.2


def test_read_lines_skips_what_it_cannot_read():
    raw = [json.dumps(payload("AAA")) + "\n", "{not json\n", "\n", json.dumps(payload("BBB", held=True)) + "\n",
           json.dumps([1, 2]) + "\n", json.dumps(payload("CCC"))]
    assert [line.ticker for line in ic.read_lines(raw)] == ["AAA", "CCC"]


def test_shadow_universe_lines_are_read_from_their_directory(tmp_path):
    def shadow_line(ticker, when, signal=True, error=None):
        line = payload(ticker, when, signal=signal, error=error, momentum=("BULLISH", 0.25))
        del line["held"]   # the shadow line format has no held field
        line.update({"universe": "shadow", "usage": {"cost_usd": 0.002} if signal else None,
                     "model_setup": {"model": "m", "provider": "p", "prompt": "abc"},
                     "reasoning_effort": "high", "event": "shadow_universe_scored"})
        return json.dumps(line) + "\n"

    directory = tmp_path / "shadow_universe"
    directory.mkdir()
    (directory / "2026-12.log").write_text(shadow_line("EARLY", "2026-12-30T18:40:00+00:00"))
    (directory / "2027-01.log").write_text(
        shadow_line("KO", "2027-01-04T18:40:00+00:00")
        + shadow_line("PEP", "2027-01-04T18:41:00+00:00")
        + shadow_line("FAIL", "2027-01-04T18:42:00+00:00", signal=False, error="timed out")
        + shadow_line("KO", "2027-01-05T18:40:00+00:00"))
    (directory / "notes.txt").write_text(shadow_line("STRAY", "2027-01-04T18:40:00+00:00"))

    lines = ic.read_universe(directory)
    assert [line.ticker for line in lines] == ["EARLY", "KO", "PEP", "KO"]
    assert lines[1].scores["momentum"] == 0.25 and lines[1].scores["blend"] == 0.1
    shown = ic.counters({"production": [], "shadow": lines})["shadow"]
    assert shown["answered_lines"] == 3, "a line before the shadow universe's first day is not counted"
    assert shown["line_days"] == 2
    assert shown["lines_with_score"]["analyst"] == 3
    assert ic.read_universe(tmp_path / "missing") == []


# --------------------------------------------------------------------------- #
# Forward returns: entry at the next open, as the race enters
# --------------------------------------------------------------------------- #


def test_a_friday_line_enters_on_monday():
    bars = priced()
    one = ic.forward_return(bars, date(2026, 10, 2), 1)
    assert (one.status, one.entry_day, one.exit_day) == (ic.OK, date(2026, 10, 5), date(2026, 10, 5))
    i = SESSIONS.index(date(2026, 10, 5))
    assert one.pct == pytest.approx((100.5 + i) / (100.0 + i) - 1.0)
    three = ic.forward_return(bars, date(2026, 10, 2), 3)
    assert (three.entry_day, three.exit_day) == (date(2026, 10, 5), date(2026, 10, 7))
    assert three.pct == pytest.approx((100.5 + i + 2) / (100.0 + i) - 1.0), "the 3rd bar, the entry bar the 1st"


def test_a_line_after_midnight_utc_enters_the_session_after_that_day():
    late = ic.line_from(payload(when="2026-10-06T01:30:00+00:00"))   # Monday 21:30 in New York
    assert late.day == date(2026, 10, 6)
    assert ic.forward_return(priced(), late.day, 1).entry_day == date(2026, 10, 7)
    friday_night = ic.line_from(payload(when="2026-10-03T01:00:00+00:00"))   # Friday 21:00 in New York
    assert ic.forward_return(priced(), friday_night.day, 1).entry_day == date(2026, 10, 5)


def test_the_signal_days_own_bar_is_never_the_entry():
    assert ic.forward_return(priced(), date(2026, 10, 5), 1).entry_day == date(2026, 10, 6)


def test_a_holiday_is_not_a_session():
    found = ic.forward_return(priced(), date(2026, 11, 25), 3)
    assert (found.entry_day, found.exit_day) == (date(2026, 11, 27), date(2026, 12, 1))


def test_returns_not_there_yet_are_pending_and_a_name_without_prices_is_counted():
    bars = priced()
    last = SESSIONS[-1]
    assert ic.forward_return(bars, last, 1) == ic.Forward(ic.PENDING)
    assert ic.forward_return(bars, SESSIONS[-2], 3) == ic.Forward(ic.PENDING, entry_day=last)
    assert ic.forward_return(bars, SESSIONS[-2], 1).status == ic.OK
    assert ic.forward_return([], SESSIONS[0], 1).status == ic.NO_PRICE
    assert ic.forward_return(None, SESSIONS[0], 1).status == ic.NO_PRICE
    broken = [(d, 0.0 if d == SESSIONS[1] else 100.0, 101.0) for d in SESSIONS]
    assert ic.forward_return(broken, SESSIONS[0], 1).status == ic.NO_PRICE
    with pytest.raises(ValueError):
        ic.forward_return(bars, SESSIONS[0], 0)


def test_bars_come_from_a_fetcher_by_their_session_day():
    pd = pytest.importorskip("pandas")

    class Fetcher:
        def ohlc(self, ticker, start, end):
            if ticker == "DOWN":
                raise RuntimeError("no data")
            if ticker == "EMPTY":
                return pd.DataFrame()
            stamps = pd.DatetimeIndex([pd.Timestamp(d) for d in SESSIONS[:4]]).tz_localize("America/New_York")
            return pd.DataFrame({"Open": [10.0, 11.0, float("nan"), 13.0], "High": 20.0, "Low": 5.0,
                                 "Close": [10.5, 11.5, 12.5, 13.5]}, index=stamps)

    got = ic.bars_from_fetcher(Fetcher(), ["UP", "DOWN", "EMPTY"], SESSIONS[0], SESSIONS[3])
    assert got["UP"] == [(SESSIONS[0], 10.0, 10.5), (SESSIONS[1], 11.0, 11.5), (SESSIONS[3], 13.0, 13.5)]
    assert got["DOWN"] == [] and got["EMPTY"] == []


# --------------------------------------------------------------------------- #
# Daily ICs
# --------------------------------------------------------------------------- #


def _one_day(n: int, day: date = date(2026, 10, 2), **score_for):
    """``n`` names on one Friday, each with return i/100 on Monday; scores given as functions of i."""
    names = [f"N{i:02d}" for i in range(n)]
    monday = date(2026, 10, 5)
    bars = bars_from_returns({name: {monday: i / 100.0} for i, name in enumerate(names)})
    lines = [make_line(name, day, **{score: f(i) for score, f in score_for.items()}) for i, name in enumerate(names)]
    return lines, bars, monday


def test_ties_take_average_ranks():
    lines, bars, monday = _one_day(10, technical=lambda i: 0.0 if i < 5 else 1.0)
    found = ic.daily_ics(lines, bars, 1)
    # Ranks of the score: 3 for the five zeros and 8 for the five ones; of the return 1..10.
    assert found.ics["technical"][monday] == pytest.approx(math.sqrt(62.5 / 82.5))


def test_a_day_needs_min_names_and_a_spread():
    lines, bars, monday = _one_day(9, blend=lambda i: i)
    found = ic.daily_ics(lines, bars, 1)
    assert found.ics["blend"] == {} and found.skipped["blend"] == {ic.FEW_NAMES: 1, ic.NO_SPREAD: 0}

    lines, bars, monday = _one_day(
        11, blend=lambda i: i, analyst=lambda i: None if i < 2 else i, news=lambda i: 0.0)
    found = ic.daily_ics(lines, bars, 1)
    assert found.ics["blend"] == {monday: pytest.approx(1.0)} and found.pairs["blend"] == 11
    assert found.ics["analyst"] == {} and found.skipped["analyst"][ic.FEW_NAMES] == 1, "9 names with the score"
    assert found.ics["news"] == {} and found.skipped["news"] == {ic.FEW_NAMES: 0, ic.NO_SPREAD: 1}
    summary = ic.summarise(found.ics["news"], 1, skipped=found.skipped["news"])
    assert (summary["days"], summary["skipped_days"], summary["mean_ic"], summary["t"]) == (0, 1, None, None)


def test_a_name_twice_on_one_entry_day_counts_once_with_its_last_line():
    lines, bars, monday = _one_day(11, blend=lambda i: i)
    top = lines[-1].ticker   # the name with the highest return
    # The same name again after midnight UTC on Friday night: it also enters on Monday.
    later = ic.IcLine(top, date(2026, 10, 3), at(date(2026, 10, 3), 1),
                      {name: (-5.0 if name == "blend" else None) for name in ic.ALL_SCORES})
    found = ic.daily_ics(lines + [later], bars, 1)
    assert found.pairs["blend"] == 11
    expected = spearman([float(i) for i in range(10)] + [-5.0], [i / 100.0 for i in range(11)]).rho
    assert found.ics["blend"][monday] == pytest.approx(expected) and expected < 1.0


def test_a_perfect_score_has_an_ic_of_1_and_a_shuffled_one_about_0():
    rng = random.Random(20261002)
    names = [f"N{i:02d}" for i in range(30)]
    days = SESSIONS[:61]
    returns = {name: {d: rng.gauss(0.0, 0.02) for d in days} for name in names}
    bars = bars_from_returns(returns, days)
    lines = [make_line(name, d, blend=3.0 * returns[name][nxt] + 0.1, news=rng.random(),
                       momentum=-returns[name][nxt])
             for d, nxt in zip(days, days[1:]) for name in names]
    lines += [make_line(name, days[-1], blend=0.0) for name in names]
    found = ic.daily_ics(lines, bars, 1)
    assert len(found.ics["blend"]) == 60
    assert all(v == pytest.approx(1.0) for v in found.ics["blend"].values())
    assert all(v == pytest.approx(-1.0) for v in found.ics["momentum"].values())
    blend = ic.summarise(found.ics["blend"], 1)
    news = ic.summarise(found.ics["news"], 1)
    assert blend["mean_ic"] == pytest.approx(1.0)
    assert news["days"] == 60 and abs(news["mean_ic"]) < 0.1 and abs(news["t"]) < 3.0
    assert found.pending == len(names), "the last day's lines have no bar after them"


def test_the_three_session_return_is_grouped_by_its_entry_day():
    names = [f"N{i:02d}" for i in range(10)]
    # Only the third bar after entry moves, so a 1-session score sees nothing and a 3-session one sees it all.
    entry, third = SESSIONS[1], SESSIONS[3]
    bars = bars_from_returns({name: {third: i / 100.0} for i, name in enumerate(names)})
    lines = [make_line(name, SESSIONS[0], blend=float(i)) for i, name in enumerate(names)]
    assert ic.daily_ics(lines, bars, 3).ics["blend"] == {entry: pytest.approx(1.0)}
    one = ic.daily_ics(lines, bars, 1)
    assert one.ics["blend"] == {} and one.skipped["blend"][ic.NO_SPREAD] == 1


# --------------------------------------------------------------------------- #
# Newey-West, the smallest detectable IC, n_eff
# --------------------------------------------------------------------------- #


def test_the_newey_west_t_is_the_races():
    hr = pytest.importorskip("analysis.horse_race")
    rng = random.Random(5)
    for n in (2, 3, 7, 40):
        xs = [rng.gauss(0.03, 0.1) for _ in range(n)]
        for lag in (0, 1, 3, 5, 60):
            se = ic.newey_west_se(xs, lag)
            expected = hr.newey_west_t(xs, lag)
            assert (se is None) == (expected is None)
            if se is not None:
                assert sum(xs) / n / se == pytest.approx(expected, rel=1e-12)
    for xs in ([], [0.1], [0.5, 0.5, 0.5]):
        assert ic.newey_west_se(xs, 3) is None and hr.newey_west_t(xs, 3) is None
    daily = {d: rng.gauss(0.02, 0.1) for d in SESSIONS[:30]}
    for h in ic.HORIZONS:
        summary = ic.summarise(daily, h)
        series = [daily[d] for d in sorted(daily)]
        assert summary["t"] == pytest.approx(hr.newey_west_t(series, h))
        assert summary["t"] == pytest.approx(summary["mean_ic"] / summary["nw_se"])
        assert summary["nw_lag"] == h


def test_the_smallest_detectable_ic():
    assert ic.mde_theory(21.0, 60, 3) == pytest.approx(2.4 / math.sqrt(20 * 20))
    assert ic.mde_theory(21.0, 60, 1) == pytest.approx(2.4 / math.sqrt(20 * 60))
    assert ic.mde_theory(None, 60, 3) is None and ic.mde_theory(1.0, 60, 3) is None
    assert ic.mde_theory(21.0, 0, 3) is None
    rng = random.Random(9)
    daily = {d: rng.gauss(0.0, 0.1) for d in SESSIONS[:40]}
    summary = ic.summarise(daily, 3, n_eff=11.0)
    assert summary["mde_measured"] == pytest.approx(2.4 * summary["nw_se"])
    assert summary["mde_theory"] == pytest.approx(2.4 / math.sqrt(10 * 40 / 3))
    assert summary["p"] == pytest.approx(2 * (1 - 0.5 * (1 + math.erf(abs(summary["t"]) / math.sqrt(2)))))
    assert summary["stats"]["t_days"] == 40


def _walks(n_names: int, n_days: int, seed: int, shared: float = 0.0) -> dict:
    """Closes of ``n_names`` random walks over consecutive days; ``shared`` mixes in one common move."""
    rng = random.Random(seed)
    days = [date(2020, 1, 1) + timedelta(days=i) for i in range(n_days + 1)]
    closes = {f"W{i:02d}": [100.0] for i in range(n_names)}
    for _ in range(n_days):
        common = rng.gauss(0.0, 0.01)
        for name in closes:
            move = shared * common + (1.0 - shared) * rng.gauss(0.0, 0.01)
            closes[name].append(closes[name][-1] * (1.0 + move))
    return {name: [(d, c, c) for d, c in zip(days, cs)] for name, cs in closes.items()}, days


def _by_hand(bars: dict, names: list, dates: list) -> tuple[float, float]:
    """(n_eff, n_eff_raw) recomputed here from the closes: the common move out, then the two formulas."""
    np = pytest.importorskip("numpy")
    rows = []
    for name in names:
        close = {d: c for d, _, c in bars[name]}
        days = sorted(close)
        previous = {d: close[p] for p, d in zip(days, days[1:])}
        rows.append([close[d] / previous[d] - 1.0 for d in dates])
    matrix = np.array(rows)
    matrix = matrix - matrix.mean(axis=0, keepdims=True)
    squares = float((np.corrcoef(matrix) ** 2).sum())
    n, t = len(names), len(dates)
    return n * n / max(squares - n * (n - 1) / (t - 1), n), n * n / squares


def test_n_eff_of_independent_names_is_about_their_number():
    bars, days = _walks(10, 1000, seed=1)
    found = ic.effective_names(bars, bars, days[1], days[-1])
    assert found["reason"] is None and found["dates"] == found["window_dates"] == 1000
    assert len(found["names"]) == 10
    # Taking out each day's mean move uses up one name: 10 independent names give about 9.
    assert 8.5 < found["n_eff"] <= 10.0
    assert found["n_eff_raw"] < found["n_eff"], "the uncorrected ratio reads low (sampling noise)"
    assert abs(found["mean_corr"]) < 0.05
    assert (found["n_eff"], found["n_eff_raw"]) == pytest.approx(_by_hand(bars, found["names"], days[1:]),
                                                                  rel=1e-9)


def _one_factor(n_names: int, n_days: int, seed: int, market: float = 0.012, own: float = 0.008):
    """Every name = one market move + its own noise; each bar opens at the last close, so a bar's
    open-to-close return is its close-to-close return. Each name has one fixed blended score."""
    rng = random.Random(seed)
    days = [date(2027, 1, 1) + timedelta(days=i) for i in range(n_days + 1)]
    names = [f"F{i:02d}" for i in range(n_names)]
    close = {name: 100.0 for name in names}
    bars = {name: [(days[0], 100.0, 100.0)] for name in names}
    for d in days[1:]:
        common = rng.gauss(0.0, market)
        for name in names:
            move = common + rng.gauss(0.0, own)
            bars[name].append((d, close[name], close[name] * (1.0 + move)))
            close[name] *= 1.0 + move
    fixed = {name: rng.uniform(-1.0, 1.0) for name in names}
    lines = [make_line(name, d, blend=fixed[name]) for d in days[:-1] for name in names]
    return bars, lines, days


def test_the_common_move_is_taken_out_so_a_one_factor_universe_gives_about_n():
    """A move shared by every name does not change a day's ranks, so it must not shrink n_eff (review 1, item 2)."""
    np = pytest.importorskip("numpy")
    n = 40
    bars, lines, days = _one_factor(n, 120, seed=1)
    found = ic.universe_record(lines, bars, days[-1])
    assert found["mean_corr"] > 0.5, "the names move together strongly"
    assert 0.9 * n < found["n_eff"] <= n and found["n_eff_dates"] == 120
    assert found["n_eff_raw"] < found["n_eff"]
    assert (found["n_eff"], found["n_eff_raw"]) == pytest.approx(_by_hand(bars, found["names"], days[1:]), rel=1e-9)

    # The spread of the daily IC is what n_eff says it is: about 1 / sqrt(n_eff - 1).
    daily = ic.daily_ics(lines, bars, 1, days[-1]).ics["blend"]
    assert len(daily) == 120
    spread = statistics.stdev(daily.values())
    assert 0.8 < spread * math.sqrt(found["n_eff"] - 1.0) < 1.25

    # Left in, the common move would make 40 names look like fewer than 3: what the review found.
    raw = np.array([[c / p - 1.0 for (_, _, p), (_, _, c) in zip(bars[name], bars[name][1:])]
                    for name in found["names"]])
    assert n * n / float((np.corrcoef(raw) ** 2).sum()) < 3.0
    one = found["horizons"]["1"]["blend"]
    assert one["mde_theory"] == pytest.approx(ic.mde_theory(found["n_eff"], 120, 1))
    assert 0.5 < one["mde_theory"] / one["mde_measured"] < 2.0, "the theory now agrees with the measured spread"


def test_names_that_move_as_one_leave_nothing_to_rank():
    bars, days = _walks(10, 200, seed=2, shared=1.0)
    found = ic.effective_names(bars, bars, days[1], days[-1])
    assert found["n_eff"] is None and found["n_eff_raw"] is None and "move as one" in found["reason"]
    assert found["mean_corr"] == pytest.approx(1.0)
    one, _ = _walks(5, 400, seed=3, shared=1.0)
    other, _ = _walks(5, 400, seed=4, shared=1.0)
    two = {**{f"A{k}": v for k, v in one.items()}, **{f"B{k}": v for k, v in other.items()}}
    # Two blocks that each move as one: once the common move is out, one contrast is left (A against B).
    found = ic.effective_names(two, two, days[1], days[-1])
    assert found["n_eff"] == pytest.approx(1.0, abs=0.01) and found["n_eff_raw"] == pytest.approx(1.0)
    assert ic.mde_theory(found["n_eff"], 60, 3) > 1.0, "no IC could be detected"


def test_a_short_history_is_dropped_by_coverage_and_does_not_cut_the_window(monkeypatch):
    bars, days = _walks(30, 120, seed=7)
    bars["NEW"] = _walks(1, 120, seed=8)[0]["W00"][-26:]   # 25 returns of the window's 120: a new listing
    found = ic.effective_names(bars, bars, days[1], days[-1])
    assert found["reason"] is None and "NEW" not in found["names"] and len(found["names"]) == 30
    assert found["dates"] == found["window_dates"] == 120
    assert 0.85 * 30 < found["n_eff"] <= 30
    # Without the coverage rule the new name has enough returns (25 >= 20) and cuts every name to 25 dates.
    monkeypatch.setattr(ic, "N_EFF_MIN_COVERAGE", 0.0)
    cut = ic.effective_names(bars, bars, days[1], days[-1])
    assert "NEW" in cut["names"] and cut["dates"] == 25 and cut["window_dates"] == 120


def test_coverage_is_counted_on_the_windows_dates_and_the_boundary_is_kept():
    bars, days = _walks(3, 30, seed=12)
    # Three bars missing: 27 returns of the 30 dates is exactly 90%, kept; four missing is 26 of 30, dropped.
    bars["EDGE"] = [b for i, b in enumerate(_walks(1, 30, seed=13)[0]["W00"]) if i not in (5, 10, 15)]
    bars["SHORT"] = [b for i, b in enumerate(_walks(1, 30, seed=14)[0]["W00"]) if i not in (5, 10, 15, 20)]
    found = ic.effective_names(bars, bars, days[1], days[-1])
    assert found["window_dates"] == 30
    assert "EDGE" in found["names"] and "SHORT" not in found["names"] and found["dates"] == 27


def test_n_eff_drops_thin_names_and_says_why_it_cannot_be_measured():
    bars, days = _walks(4, 60, seed=6)
    bars["THIN"] = bars["W00"][:15]
    found = ic.effective_names(bars, bars, days[1], days[-1])
    assert "THIN" not in found["names"] and len(found["names"]) == 4

    halves = {"EARLY": bars["W00"][:31], "LATE": [bars["W01"][0]] + bars["W01"][31:]}
    found = ic.effective_names(halves, halves, days[1], days[-1])
    assert found["n_eff"] is None and "90% of the 60 dates" in found["reason"] and "needs 2" in found["reason"]

    # Each name covers 21 of the 23 dates (91%, kept), but each misses different ones: 17 shared dates.
    short, short_days = _walks(3, 23, seed=10)
    gaps = {"W00": (3, 4), "W01": (8, 9), "W02": (13, 14)}
    holes = {name: [b for i, b in enumerate(rows) if i not in gaps[name]] for name, rows in short.items()}
    found = ic.effective_names(holes, holes, short_days[1], short_days[-1])
    assert found["n_eff"] is None and found["dates"] == 17 and found["window_dates"] == 23
    assert "only 17 date(s)" in found["reason"] and "needs 20" in found["reason"]

    found = ic.effective_names(bars, bars, None, None)
    assert found["n_eff"] is None and found["reason"] == "no resolved return yet"
    found = ic.effective_names(bars, ["W00"], days[1], days[-1])
    assert found["n_eff"] is None and "needs 2" in found["reason"]
    found = ic.effective_names({}, ["W00", "W01"], days[1], days[-1])
    assert found["n_eff"] is None and found["window_dates"] == 0 and "needs 2" in found["reason"]


def test_names_whose_price_never_moves_are_left_out():
    bars, days = _walks(3, 60, seed=15)
    for name in ("FLAT1", "FLAT2"):
        bars[name] = [(d, 50.0, 50.0) for d in days]
    found = ic.effective_names(bars, bars, days[1], days[-1])
    assert found["reason"] is None and found["names"] == ["W00", "W01", "W02"]
    assert (found["n_eff"], found["n_eff_raw"]) == pytest.approx(_by_hand(bars, found["names"], days[1:]), rel=1e-9)

    lonely = {"W00": bars["W00"], "FLAT1": bars["FLAT1"], "FLAT2": bars["FLAT2"]}
    found = ic.effective_names(lonely, lonely, days[1], days[-1])
    assert found["n_eff"] is None and found["reason"] == "fewer than 2 names whose price moves in the window"
    assert found["dates"] == 60 and found["names"] == []


def test_paired_is_the_daily_difference_on_shared_days_by_hand():
    d1, d2, d3, d4, d5 = SESSIONS[:5]
    first = {d1: 0.5, d2: 0.3, d3: 0.4, d4: 0.9}
    second = {d1: 0.2, d2: 0.2, d3: 0.2, d5: -0.3}
    # Shared days d1..d3; differences 0.3, 0.1, 0.2: mean 0.2, deviations 0.1, -0.1, 0.
    # Variance 0.02/3; autocovariance at lag 1 -0.01/3, at lag 2 0.
    # Lag 1 (weight 1/2): variance 0.01/3, se = sqrt(0.01/9) = 0.1/3, t = 6.
    # Lag 3 cut to 2 (weights 3/4, 1/2): variance 0.005/3, se = 0.1/(3 sqrt 2), t = 6 sqrt 2.
    one = ic.paired(first, second, 1)
    assert one["days"] == 3 and one["mean"] == pytest.approx(0.2) and one["t"] == pytest.approx(6.0)
    three = ic.paired(first, second, 3)
    assert three["days"] == 3 and three["t"] == pytest.approx(6.0 * math.sqrt(2.0))
    assert ic.paired(first, {d4: 0.1}, 1) == {"days": 1, "mean": pytest.approx(0.8), "t": None}
    assert ic.paired(first, {d5: 0.1}, 1) == {"days": 0, "mean": None, "t": None}


# --------------------------------------------------------------------------- #
# Hidden until the checkpoint
# --------------------------------------------------------------------------- #


def test_counters_carry_no_statistic():
    assert list(inspect.signature(ic.counters).parameters) == ["lines_by_universe", "through"], \
        "counters is given no prices, so it cannot compute a return"
    lines = [make_line(f"N{i}", d, blend=0.1 * i, news=0.0, momentum=-0.2) for i, d in enumerate(SESSIONS[:5])]
    lines.append(make_line("OLD", date(2026, 9, 25), blend=0.5))
    shown = ic.counters({"production": lines})
    assert set(shown) == set(ic.UNIVERSES)
    for block in shown.values():
        assert set(block) == set(ic.COUNTER_KEYS)
        assert set(block["lines_with_score"]) == set(ic.ALL_SCORES)
        leaves = [block["answered_lines"], block["line_days"], *block["lines_with_score"].values()]
        assert all(type(v) is int for v in leaves)
    assert shown["production"] == {
        "answered_lines": 5, "line_days": 5,
        "lines_with_score": {"blend": 5, "news": 5, "technical": 0, "fundamental": 0, "analyst": 0,
                             "insider": 0, "momentum": 5}}
    assert ic.counters({"production": lines}, through=SESSIONS[1])["production"]["answered_lines"] == 2
    with pytest.raises(ValueError):
        ic._counts_only({"production": {**shown["production"], "mean_ic": 0.1}})
    with pytest.raises(ValueError):
        ic._counts_only({"production": {**shown["production"], "answered_lines": 0.5}})


def test_the_record_is_due_only_at_a_new_look_from_registration():
    assert ic.due(True, date(2026, 12, 22)) is True
    assert ic.due(True, date(2027, 3, 22)) is True
    assert ic.due(True, date(2026, 12, 21)) is False
    assert ic.due(False, date(2026, 12, 22)) is False
    assert ic.due(False, date(2027, 6, 16)) is False


# --------------------------------------------------------------------------- #
# The checkpoint record
# --------------------------------------------------------------------------- #


def _universe(n_names: int = 12, n_days: int = 31, seed: int = 11):
    rng = random.Random(seed)
    names = [f"N{i:02d}" for i in range(n_names)]
    days = SESSIONS[:n_days + 5]   # bars and lines go past ``through`` on purpose
    returns = {name: {d: rng.gauss(0.0, 0.02) for d in days} for name in names}
    lines = [make_line(name, d, blend=rng.uniform(-0.3, 0.3), news=rng.choice([0.0, 0.0, 0.5]),
                       technical=rng.uniform(-1, 1), fundamental=rng.uniform(-1, 1),
                       analyst=None if name == "N00" else rng.uniform(-1, 1), insider=rng.uniform(-1, 1),
                       momentum=rng.choice([0.0, 0.4, -0.7]))
             for d in days for name in names]
    return lines, bars_from_returns(returns, days), days[n_days - 1]


def test_the_record_has_the_registered_shape():
    lines, bars, through = _universe()
    found = ic.record({"production": lines}, {"production": bars}, through)
    assert json.loads(json.dumps(found)) == found, "the record is plain JSON"
    assert (found["through"], found["registered"], found["start"]) == (through.isoformat(), "2026-12-22",
                                                                       "2026-09-28")
    assert found["settings"]["main"] == {"score": "blend", "horizon": 3}
    assert found["universes"]["shadow"] == {"no_data": True}
    production = found["universes"]["production"]
    assert production["lines"] == 31 * 12, "lines after ``through`` are not read"
    assert set(production["horizons"]) == {"1", "3"}
    for horizon in production["horizons"].values():
        assert set(horizon) == set(ic.ALL_SCORES) | {"blend_minus_momentum"}
        for name in ic.ALL_SCORES:
            assert {"days", "skipped_days", "mean_ic", "nw_se", "t", "p", "stats", "mde_measured",
                    "mde_theory"} <= set(horizon[name])
        assert set(horizon["blend_minus_momentum"]) == {"days", "mean", "t"}
    # The last session's lines have no entry bar by ``through``; at 3 sessions the last three days are pending.
    assert production["pending_by_horizon"] == {"1": 12, "3": 36} and production["pending"] == 36
    assert production["no_price"] == 0
    three = production["horizons"]["3"]
    assert three["blend"]["days"] == 31 - 3 and production["horizons"]["1"]["blend"]["days"] == 31 - 1
    assert three["analyst"]["days"] == 28, "11 names carry the analyst score: still enough"
    assert production["n_eff"] is not None and production["n_eff_reason"] is None
    assert production["names"] == ic.tickers_of(lines) and production["n_eff_dates"] == 30
    assert production["n_eff_window_dates"] == 30 and 0 < production["n_eff_raw"] <= production["n_eff"] <= 12
    assert found["settings"]["n_eff_min_coverage"] == ic.N_EFF_MIN_COVERAGE
    assert three["blend"]["mde_theory"] == pytest.approx(ic.mde_theory(production["n_eff"], 28, 3))
    main = production["main"]
    assert {"t", "stats", "mean_daily_diff", "days"} <= set(main)
    assert main["t"] == three["blend"]["t"] and main["days"] == three["blend"]["days"]
    assert main["mean_daily_diff"] == three["blend"]["mean_ic"] and main["stats"] == three["blend"]["stats"]
    assert main["name"] == "ic_production_blend_3"


def test_a_record_does_not_move_with_later_lines_or_bars():
    lines, bars, through = _universe()
    found = ic.record({"production": lines}, {"production": bars}, through)
    early = [line for line in lines if line.day <= through]
    clipped = {name: [b for b in rows if b[0] <= through] for name, rows in bars.items()}
    assert ic.record({"production": early}, {"production": clipped}, through) == found


def test_a_universe_without_prices_is_all_no_price_and_without_lines_no_data():
    lines, _, through = _universe(n_days=5)
    found = ic.record({"production": lines, "shadow": []}, {}, through)
    production = found["universes"]["production"]
    assert production["no_price"] == 5 * 12 and production["main"]["days"] == 0 and production["main"]["t"] is None
    assert production["n_eff"] is None and production["n_eff_reason"] == "no resolved return yet"
    assert found["universes"]["shadow"] == {"no_data": True}
    old = [make_line("N00", date(2026, 9, 25), blend=0.1)]
    assert ic.record({"production": old}, {}, through)["universes"]["production"] == {"no_data": True}
