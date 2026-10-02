"""The history screen's stress kind: four fixed periods, a fresh start in each, and "not possible" said out loud.

Offline, on made-up prices, with every outbound connection refused: the
stress kind (``history.stress``, the owner's instruction of 2 Oct 2026) must
run momentum, A, B, C, VT and SPY from a fresh $100,000 on each period's
first session, say "not possible" and why where VT, B or BIL had no prices
(never a proxy), show the return against SPY with its label where VT did
not exist, compute the total return and the drawdown from the running high
exactly, and carry the regime split's volatility cut-offs at full
precision. The full kind must not change.
"""

from __future__ import annotations

import json
import math
import socket
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import yaml

from analysis import regimes
from config import market_calendar
from history import journal, prices, report, screen, stress
from history.periods import Period, max_drawdown
from shadow.fund import STARTING_CASH, Day, IndexFund
from shadow.market import Bars

ROOT = Path(__file__).resolve().parents[1]
END = date(2026, 10, 1)
#: Days the made-up exchange is shut, besides every 1 January and 25 December.
CLOSED = (date(2001, 9, 11), date(2001, 9, 12), date(2001, 9, 13), date(2001, 9, 14), date(2008, 7, 4))
#: VT's and BIL's real first prices.
VT_FIRST, BIL_FIRST = date(2008, 6, 26), date(2007, 5, 30)


def _frame(seed: int, start: str, drift: float = 0.0, vol: float = 0.015, price: float = 40.0,
           dividend: float = 0.0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    index = pd.bdate_range(start, END)
    holiday = ((index.month == 1) & (index.day == 1)) | ((index.month == 12) & (index.day == 25))
    index = index[~holiday & ~index.isin([pd.Timestamp(d) for d in CLOSED])]
    # Trending stretches, so the momentum rule takes both sides and the veto has something to veto.
    regime = np.repeat(rng.choice([-1.0, 1.0], size=len(index) // 60 + 1), 60)[:len(index)]
    close = price * np.exp(np.cumsum(rng.normal(drift + 0.0012 * regime, vol, len(index))))
    opened = close * np.exp(rng.normal(0, vol / 3, len(index)))
    high = np.maximum(opened, close) * np.exp(np.abs(rng.normal(0, vol / 2, len(index))))
    low = np.minimum(opened, close) * np.exp(-np.abs(rng.normal(0, vol / 2, len(index))))
    dividends = np.zeros(len(index))
    if dividend:
        dividends[5::63] = dividend
    return pd.DataFrame({"Open": opened, "High": high, "Low": low, "Close": close,
                         "Volume": rng.integers(100_000, 1_000_000, len(index)).astype(float),
                         "Dividends": dividends}, index=index)


def _table() -> prices.PriceTable:
    frames = {
        "MSFT": _frame(1, "1998-01-01"), "XLE": _frame(2, "1999-01-04", drift=0.0003),
        # Starts in the middle of the first period: one name fewer from its first session.
        "TLT": _frame(3, "2002-07-30", drift=-0.0002, vol=0.008),
        "SPY": _frame(4, "1997-01-02", dividend=0.3),
        "VT": _frame(5, VT_FIRST.isoformat(), dividend=0.2), "BIL": _frame(6, BIL_FIRST.isoformat(), vol=0.0004),
    }
    return prices.PriceTable(frames, END, "test", ())


@pytest.fixture(scope="module")
def table() -> prices.PriceTable:
    return _table()


@pytest.fixture(scope="module")
def sessions(table) -> list[date]:
    return screen.sessions_of(table)


@pytest.fixture(scope="module")
def ran(tmp_path_factory, table) -> tuple[Path, dict]:
    """One stress screen, forked workers too, with every outbound connection refused."""
    out = tmp_path_factory.mktemp("stress")
    prices.save(table, out / "prices.csv.gz")

    def refuse(*args, **kwargs):
        raise AssertionError("the stress screen tried to reach the network")

    with pytest.MonkeyPatch.context() as patch:
        patch.setattr(socket.socket, "connect", refuse)
        patch.setattr(socket.socket, "connect_ex", refuse)
        assert screen.main(["run", "--out", str(out), "--kind", "stress", "--processes", "2"]) == 0
    return out, json.loads((out / "results.json").read_text())


@pytest.fixture(scope="module")
def results(ran) -> dict:
    return ran[1]


def _period_sessions(sessions, name):
    period = next(p for p in stress.PERIODS if p.name == name)
    return [d for d in sessions if period.contains(d)]


# --------------------------------------------------------------------------- #
# The periods and the fetch
# --------------------------------------------------------------------------- #


def test_the_periods_are_the_owners_four_with_each_end_a_trading_day():
    assert [(p.name, p.first, p.last) for p in stress.PERIODS] == [
        ("2000-2002", date(2000, 1, 3), date(2002, 12, 31)), ("2008", date(2008, 1, 2), date(2008, 12, 31)),
        ("2020", date(2020, 1, 2), date(2020, 12, 31)), ("2022", date(2022, 1, 3), date(2022, 12, 30))]
    for period in stress.PERIODS:
        assert market_calendar.is_trading_day(period.first) and market_calendar.is_trading_day(period.last)
    # An end that is not a trading day moves inward to the span's first or last trading day.
    shut = {date(2022, 1, 3), date(2022, 12, 30)}
    span = stress.trading_span("x", date(2022, 1, 1), date(2022, 12, 31),
                               lambda d: d.weekday() < 5 and d not in shut)
    assert (span.first, span.last) == (date(2022, 1, 4), date(2022, 12, 29))
    with pytest.raises(ValueError):
        stress.trading_span("x", date(2022, 1, 1), date(2022, 1, 2))
    assert stress.FUNDS == ("momentum", "momentum_200", "vt_timing", "momentum_pullback", "vt", "spy")
    # The report reads results.json alone, so it keeps its own copies of these; they must stay the same.
    assert report.STRESS_FUNDS == stress.FUNDS and report.VT_MISSING == stress.VT_MISSING
    assert report.STRESS_KIND == stress.KIND and screen.KINDS == ("full", "stress")
    with pytest.raises(ValueError):
        stress.new_fund("hybrid", None, Bars({}), END)


def test_the_fetch_reaches_back_far_enough_and_the_full_kinds_fetch_is_unchanged(tmp_path, monkeypatch):
    # The first period's first cycle is the session before 2000-01-03; its technicals read two years before it.
    assert stress.WARM_UP_FROM <= journal.two_years_before(date(1999, 12, 24))
    assert stress.FETCH_FROM <= stress.WARM_UP_FROM and stress.FETCH_FROM == prices.FIRST_FETCH
    calls = []

    def fake_fetch(*args, **kwargs):
        calls.append((args, kwargs))
        return prices.PriceTable({}, END, "test", ())

    monkeypatch.setattr(prices, "fetch", fake_fetch)
    monkeypatch.setattr(prices, "save", lambda table, path: "0" * 64)
    assert screen.main(["fetch", "--out", str(tmp_path)]) == 0
    assert screen.main(["fetch", "--out", str(tmp_path), "--kind", "stress"]) == 0
    assert calls == [((), {}), ((), {"start": stress.FETCH_FROM})]
    assert screen.build_parser().parse_args(["run", "--out", "x"]).kind == "full"
    with pytest.raises(SystemExit):
        screen.build_parser().parse_args(["run", "--out", "x", "--kind", "crash"])


# --------------------------------------------------------------------------- #
# The run
# --------------------------------------------------------------------------- #


def test_each_period_is_a_fresh_start_on_its_first_session_acting_on_the_session_before(results, sessions):
    assert list(results["periods"]) == ["2000-2002", "2008", "2020", "2022"]
    assert results["meta"]["kind"] == "stress" and results["meta"]["starting_cash"] == STARTING_CASH
    for name, period in results["periods"].items():
        span = _period_sessions(sessions, name)
        before = [d for d in sessions if d < span[0]][-1]
        assert period["first_session"] == span[0].isoformat() and period["last_session"] == span[-1].isoformat()
        assert period["sessions"] == len(span) and period["first_cycle"] == before.isoformat()
        assert period["integrity"]["ok"], (name, period["integrity"])
        for fund, row in period["funds"].items():
            if not row["possible"] or (fund == "vt" and name == "2008"):
                continue
            assert (row["first"], row["last"], row["sessions"]) == (span[0].isoformat(), span[-1].isoformat(),
                                                                     len(span)), (name, fund)
        for fund in stress.ENGINE_FUNDS:
            assert period["funds"][fund]["entries"] > 0, (name, fund)
    assert results["periods"]["2020"]["first_cycle"] == "2019-12-31"
    assert results["periods"]["2020"]["funds"]["vt_timing"]["first_decision"] == "2019-12-31"


def test_the_journal_holds_only_the_periods_sessions_and_the_session_before_each(ran, sessions):
    out, results = ran
    needed = set(stress.journal_sessions(sessions))
    entries = journal.read(out / "journal")
    assert entries and {e.timestamp.date() for e in entries} <= needed
    assert {e.timestamp.date() for e in entries} >= {date(1999, 12, 31), date(2007, 12, 31), date(2022, 12, 30)}
    assert results["meta"]["journal_lines"] == len(entries)


def test_the_held_spy_fund_is_100000_bought_at_the_first_open_and_its_numbers_are_exact(results, table, sessions):
    """The fresh start and the arithmetic, rebuilt from the bars: buy at the first open, dividends after."""
    frame = table.frames["SPY"]
    for name in ("2008", "2020"):
        span = _period_sessions(sessions, name)
        opened = float(frame.loc[pd.Timestamp(span[0]), "Open"])
        qty = math.floor(STARTING_CASH / (opened * 1.001))
        cash = STARTING_CASH - qty * opened * 1.001
        equity = []
        for i, day in enumerate(span):
            bar = frame.loc[pd.Timestamp(day)]
            if i and bar["Dividends"]:
                cash += qty * float(bar["Dividends"])
            equity.append(cash + qty * float(bar["Close"]))
        row = results["periods"][name]["funds"]["spy"]
        assert row["total_return"] == pytest.approx(equity[-1] / STARTING_CASH - 1.0, rel=1e-12)
        assert row["max_drawdown"] == pytest.approx(max_drawdown([STARTING_CASH] + equity), rel=1e-12)
        # Against SPY, every fund over the whole period: its return minus SPY's, on the same sessions.
        for fund in ("momentum", "momentum_200", "momentum_pullback"):
            vs = results["periods"][name]["funds"][fund]["vs_spy"]
            assert vs["from"] == span[0].isoformat() and vs["sessions"] == len(span)
            assert vs["compared_return"] == pytest.approx(row["total_return"], rel=1e-12)
            assert vs["fund_return"] == results["periods"][name]["funds"][fund]["total_return"]
            assert vs["difference"] == pytest.approx(vs["fund_return"] - vs["compared_return"], abs=1e-15)


def test_where_vt_b_or_bil_had_no_prices_the_screen_says_not_possible_and_why(results, sessions):
    early = results["periods"]["2000-2002"]["funds"]
    assert early["vt"] == {"possible": False, "why": "VT did not exist (its first price is 2008-06-26)"}
    assert not early["vt_timing"]["possible"]
    assert "VT did not exist" in early["vt_timing"]["why"] and "BIL" in early["vt_timing"]["why"]
    assert "2007-05-30" in early["vt_timing"]["why"]
    for fund in ("momentum", "momentum_200", "momentum_pullback", "spy"):
        assert early[fund]["possible"] and early[fund]["vs_vt"] == {
            "possible": False, "why": "VT did not exist (its first price is 2008-06-26)"}
    crash = results["periods"]["2008"]["funds"]
    assert not crash["vt_timing"]["possible"] and "10 months up to 2007-12-31" in crash["vt_timing"]["why"]
    # VT only from its first price in 2008: its own row, and every comparison with it, start there.
    vt_days = [d for d in _period_sessions(sessions, "2008") if d >= VT_FIRST]
    assert crash["vt"]["possible"] and crash["vt"]["first"] == "2008-06-26"
    assert crash["vt"]["sessions"] == len(vt_days)
    assert results["periods"]["2008"]["vt"]["in_period"] == "part"
    for fund in ("momentum", "momentum_200", "momentum_pullback", "spy"):
        vs = crash[fund]["vs_vt"]
        assert vs["from"] == "2008-06-26" and vs["sessions"] == len(vt_days)
        assert vs["compared_return"] == pytest.approx(crash["vt"]["total_return"], rel=1e-12)
    for name in ("2020", "2022"):
        assert all(row["possible"] for row in results["periods"][name]["funds"].values()), name
        assert results["periods"][name]["vt"]["in_period"] == "whole"


def test_where_vt_did_not_exist_the_return_against_spy_is_labelled(ran, results):
    out, _ = ran
    assert results["periods"]["2000-2002"]["vt"] == {"first_price": "2008-06-26", "in_period": "none",
                                                     "note": "VT did not exist; against SPY instead"}
    text = (out / "report.md").read_text()
    early = text.split("## 2000-2002", 1)[1].split("\n## ", 1)[0]
    assert "**VT did not exist; against SPY instead.**" in early
    assert "Minus SPY (same sessions): VT did not exist; against SPY instead |" in early
    later = text.split("## 2020", 1)[1].split("\n## ", 1)[0]
    assert "against SPY instead" not in later


def test_the_names_with_prices_are_counted_per_period(results):
    assert results["periods"]["2000-2002"]["names"] == {"watchlist": 80, "with_prices": 3,
                                                        "from_the_first_session": 2}
    assert results["periods"]["2008"]["names"] == {"watchlist": 80, "with_prices": 3, "from_the_first_session": 3}


def test_the_volatility_terciles_are_the_regime_splits_cut_offs_at_full_precision(ran, results, table):
    out, _ = ran
    closes = [(stamp.date(), float(c)) for stamp, c in table.frames["VT"]["Close"].items()]
    block = results["regime_cutoffs"]
    assert block["cutoffs"] == list(regimes.tercile_cutoffs(closes, date(2026, 9, 30)))     # to the last bit
    assert block["complete"] and block["window_end"] == "2026-09-30" and block["last_session"] == "2026-09-30"
    vols = [v for d, v in regimes.vol_series(closes) if d <= date(2026, 9, 30)]
    assert block["sessions"] == len(vols) == sum(block["by_tercile"].values())
    assert block["first_session"] == closes[21][0].isoformat()
    text = (out / "report.md").read_text()
    assert ("## VT 21-day realized volatility terciles, from its first 21 returns to 2026-09-30 (the regime "
            "split's cut-offs, pre-registration section 13.10)") in text
    c1, c2 = block["cutoffs"]
    assert f"c1 = {c1!r}, c2 = {c2!r}" in text
    # Prices that end before the window's end are said not to be the registration's numbers.
    short = stress.regime_cutoffs(table.frames, date(2020, 1, 31), date(2020, 1, 31))
    assert short["possible"] and short["last_session"] <= "2020-01-31"
    assert not stress.regime_cutoffs(table.frames, date(2026, 9, 1))["complete"]
    assert stress.regime_cutoffs({}, END) == {"possible": False, "why": "no VT prices in the table"}


def test_the_report_is_descriptive_and_written_from_results_alone(ran, results):
    out, _ = ran
    text = (out / "report.md").read_text()
    assert text == report.render(results) == report.render_stress(results)
    for words in ("Descriptive only", "no t and no verdict", "today's watchlist", "No AI arms",
                  "not possible: VT did not exist", "fresh start", "running high",
                  "Nothing here changes the locked test", "previous session's final close stands in"):
        assert words in text, words

    def keys(value):
        if isinstance(value, dict):
            for k, v in value.items():
                yield k
                yield from keys(v)
        elif isinstance(value, list):
            for v in value:
                yield from keys(v)

    found = set(keys(results["periods"]))
    assert not found & {"t", "p", "verdict"}                 # no test, no verdict


def test_the_stress_kind_builds_its_own_journal_and_refuses_an_old_one(tmp_path, table):
    prices.save(table, tmp_path / "prices.csv.gz")
    with pytest.raises(SystemExit, match="reuse-journal"):
        screen.main(["run", "--out", str(tmp_path), "--kind", "stress", "--reuse-journal"])
    (tmp_path / "journal").mkdir()
    (tmp_path / "journal" / "2001-01.log").write_text("{}\n")
    with pytest.raises(SystemExit, match="fresh --out"):
        screen.main(["run", "--out", str(tmp_path), "--kind", "stress"])
    assert not (tmp_path / "results.json").exists()
    frames = {t: f for t, f in table.frames.items() if t != "VT"}
    prices.save(prices.PriceTable(frames, END, "test", ("VT",)), tmp_path / "prices.csv.gz")
    with pytest.raises(SystemExit, match="no prices for VT"):
        screen.main(["run", "--out", str(tmp_path), "--kind", "stress"])


# --------------------------------------------------------------------------- #
# The arithmetic, on funds made by hand
# --------------------------------------------------------------------------- #

DAYS = [date(2020, 3, 2) + timedelta(days=i) for i in range(5)]
PERIOD = Period("test", DAYS[0], DAYS[-1])


class _Book:
    """A fund's record and nothing else: what ``fund_row`` and ``against`` read."""

    def __init__(self, name: str, equity: list[float]) -> None:
        self.name = name
        self.days = [Day(d, e, e, 0.0, 0) for d, e in zip(DAYS, equity)]


def _held(name: str, equity: list[float], bought: date) -> IndexFund:
    fund = IndexFund(name, "VT", Bars({}))
    fund.days = [Day(d, e, e, e if d >= bought else 0.0, 1 if d >= bought else 0) for d, e in zip(DAYS, equity)]
    fund.bought = bought
    return fund


def test_the_drawdown_is_from_the_running_high_and_the_start_counts_as_a_high():
    row = stress.fund_row(_Book("a", [110_000.0, 99_000.0, 120_000.0, 102_000.0, 102_000.0]), PERIOD)
    assert row["total_return"] == pytest.approx(0.02, abs=1e-15)
    assert row["max_drawdown"] == pytest.approx(1 - 102 / 120, abs=1e-15)     # deeper than 1 - 99/110
    assert (row["first"], row["last"], row["sessions"]) == (DAYS[0].isoformat(), DAYS[-1].isoformat(), 5)
    down = stress.fund_row(_Book("b", [95_000.0, 90_000.0, 92_000.0, 93_000.0, 94_000.0]), PERIOD)
    assert down["max_drawdown"] == pytest.approx(0.10, abs=1e-15)               # from the $100,000 start
    assert down["total_return"] == pytest.approx(-0.06, abs=1e-15)


def test_against_is_over_the_sessions_both_were_running():
    a = _Book("a", [101_000.0, 102_000.0, 104_000.0, 103_000.0, 106_000.0])
    vt = _held("vt", [100_000.0, 100_000.0, 99_000.0, 101_000.0, 103_000.0], DAYS[2])
    assert stress.own_days(vt, PERIOD) == DAYS[2:]
    row = stress.fund_row(vt, PERIOD)
    assert row["first"] == DAYS[2].isoformat() and row["total_return"] == pytest.approx(0.03, abs=1e-15)
    assert row["max_drawdown"] == pytest.approx(0.01, abs=1e-15)                # from the cash it held before
    vs = stress.against(a, vt, PERIOD)
    assert (vs["from"], vs["to"], vs["sessions"]) == (DAYS[2].isoformat(), DAYS[-1].isoformat(), 3)
    assert vs["fund_return"] == pytest.approx(106 / 102 - 1, abs=1e-15)
    assert vs["compared_return"] == pytest.approx(0.03, abs=1e-15)
    assert vs["difference"] == pytest.approx(106 / 102 - 1 - 0.03, abs=1e-15)
    never = _held("vt", [100_000.0] * 5, DAYS[0])
    never.bought = None
    assert stress.against(a, never, PERIOD)["possible"] is False
    assert stress.fund_row(never, PERIOD)["possible"] is False


def test_b_and_vt_say_why_they_cannot_start(table, sessions):
    from history.sessions import historical_calendar

    bars = Bars(dict(table.frames))
    early, crash, covid = stress.PERIODS[0], stress.PERIODS[1], stress.PERIODS[2]
    with historical_calendar(sessions):
        assert stress.month_end_before(date(2020, 1, 2)) == date(2019, 12, 31)
        assert stress.month_end_before(date(2001, 9, 17)) == date(2001, 8, 31)
        assert stress.b_not_possible(bars, table.frames, covid, date(2019, 12, 31)) is None
        assert "10 months up to 2007-12-31" in stress.b_not_possible(bars, table.frames, crash, date(2007, 12, 31))
        no_bil = {t: f for t, f in table.frames.items() if t != "BIL"}
        assert stress.b_not_possible(bars, no_bil, covid, date(2019, 12, 31)) == "no BIL prices in the table"
    assert stress.vt_not_possible(table.frames, early) == "VT did not exist (its first price is 2008-06-26)"
    assert stress.vt_not_possible(table.frames, crash) is None
    assert stress.vt_not_possible({}, crash) == "no VT prices in the table"


# --------------------------------------------------------------------------- #
# The full kind, and the workflow
# --------------------------------------------------------------------------- #


def test_the_full_kind_keeps_its_report_and_its_results_shape():
    """The full kind's results carry no kind and are rendered by the full report, as before."""
    full = {"meta": {"generated_at": "x"}, "race": {}, "funds": {}, "data": {}}
    text = report.render(full)
    assert text.startswith("# History screen: the rules that run live, on past prices\n")
    assert "stress" not in text
    source = (ROOT / "history" / "screen.py").read_text()
    full_meta = source.split("def run(", 1)[1].split("def run_stress(", 1)[0]
    assert '"kind"' not in full_meta


def test_the_workflow_takes_a_kind_and_passes_it_to_fetch_and_run():
    path = ROOT / ".github" / "workflows" / "history-screen.yml"
    text = path.read_text()
    wf = yaml.safe_load(text)
    assert set(wf[True]) == {"workflow_dispatch"} and "secrets." not in text
    kind = wf[True]["workflow_dispatch"]["inputs"]["kind"]
    assert kind["type"] == "choice" and kind["options"] == ["full", "stress"] and kind["default"] == "full"
    job = wf["jobs"]["screen"]
    assert job["env"]["SCREEN_KIND"] == "${{ inputs.kind }}"
    steps = {s.get("name"): s for s in job["steps"]}
    assert '--kind "$SCREEN_KIND"' in steps["Fetch the prices"]["run"]
    assert '--kind "$SCREEN_KIND"' in steps["Run the screen"]["run"]
