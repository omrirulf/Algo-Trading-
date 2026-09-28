"""The history screen: prices only, the registered code, no look-ahead, and nothing left patched.

Offline, on made-up prices: the screen's journal must be production's
technicals on bars before the line's day and nothing later; its race must be
the race's own code (``race_arm``, ``arm_trades``, ``bands_for``,
``race_tests``' grouping) with the year-by-year feeding and the vectorised
coin-flip averaging giving the same numbers; its funds must run clean through
the production engine; and every module it patches for a run must be put
back after it.
"""

from __future__ import annotations

import json
import re
from dataclasses import replace
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import yaml

from analysis import horse_race as hr
from analysis.reader import read_journal
from config import market_calendar
from history import funds as fund_screen
from history import journal, prices, race, report, screen
from history.sessions import PATCHED, historical_calendar
from orchestrator.technicals import build_snapshot
from rules import momentum
from shadow import exploratory as xp
from shadow import market as sim_market
from shadow.market import Bars

ROOT = Path(__file__).resolve().parents[1]
#: Days the made-up exchange is shut: a holiday mid-week and a month's last weekday.
CLOSED = (date(2001, 7, 4), date(2001, 8, 31), date(2000, 12, 25), date(2001, 1, 1))
END = date(2001, 12, 31)


def _frame(seed: int, start: str, drift: float = 0.0, vol: float = 0.015, price: float = 40.0,
           dividend: float = 0.0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    index = pd.bdate_range(start, END)
    index = index[~index.isin([pd.Timestamp(d) for d in CLOSED])]
    # Trending stretches, so the momentum rule takes both sides and the veto has something to veto.
    regime = np.repeat(rng.choice([-1.0, 1.0], size=len(index) // 60 + 1), 60)[:len(index)]
    close = price * np.exp(np.cumsum(rng.normal(drift + 0.0012 * regime, vol, len(index))))
    opened = close * np.exp(rng.normal(0, vol / 3, len(index)))
    high = np.maximum(opened, close) * np.exp(np.abs(rng.normal(0, vol / 2, len(index))))
    low = np.minimum(opened, close) * np.exp(-np.abs(rng.normal(0, vol / 2, len(index))))
    dividends = np.zeros(len(index))
    if dividend:
        dividends[::63] = dividend
    return pd.DataFrame({"Open": opened, "High": high, "Low": low, "Close": close,
                         "Volume": rng.integers(100_000, 1_000_000, len(index)).astype(float),
                         "Dividends": dividends}, index=index)


def _table() -> prices.PriceTable:
    frames = {
        "MSFT": _frame(1, "1998-01-01"), "XLE": _frame(2, "1998-06-01", drift=0.0003),
        "TLT": _frame(3, "2000-03-01", drift=-0.0002, vol=0.008),
        "SPY": _frame(4, "1997-01-01", dividend=0.3), "VT": _frame(5, "2000-05-15", dividend=0.2),
        "BIL": _frame(6, "2000-04-20", vol=0.0004),
    }
    return prices.PriceTable(frames, END, "test", ())


@pytest.fixture(scope="module")
def table() -> prices.PriceTable:
    return _table()


@pytest.fixture(scope="module")
def sessions(table) -> list[date]:
    return screen.sessions_of(table)


@pytest.fixture(scope="module")
def journal_dir(tmp_path_factory, table, sessions) -> Path:
    directory = tmp_path_factory.mktemp("history") / "journal"
    journal.write(journal.build(table.frames, sessions), directory)
    return directory


@pytest.fixture(scope="module")
def year_2001(table, sessions, journal_dir):
    """The race's inputs for one year of lines, as ``race.race_year`` builds them."""
    with historical_calendar(sessions):
        lines = hr.offered(journal.read(journal_dir, [2001]))
        how = race.settings(table.frames, table.final_through, lines)
        entries = hr.entries_for_arm(momentum.NAME, lines)
        mine = race.arm_result(momentum.NAME, entries, how)
    return lines, how, entries, mine


# --------------------------------------------------------------------------- #
# Prices
# --------------------------------------------------------------------------- #


def test_the_price_table_is_saved_and_read_back_to_the_bit_and_a_changed_file_is_refused(tmp_path, table):
    path = tmp_path / "prices.csv.gz"
    digest = prices.save(table, path)
    again, read_digest = prices.load(path)
    assert read_digest == digest and again.final_through == table.final_through
    for ticker, frame in table.frames.items():
        pd.testing.assert_frame_equal(again.frames[ticker], frame[list(prices.COLUMNS)], check_freq=False)
    meta = json.loads(path.with_suffix("").with_suffix(".meta.json").read_text())
    meta["sha256"] = "0" * 64
    path.with_suffix("").with_suffix(".meta.json").write_text(json.dumps(meta))
    with pytest.raises(ValueError, match="SHA-256"):
        prices.load(path)


def test_a_vendor_frame_is_cut_to_final_bars_and_dated_by_exchange_day():
    index = pd.DatetimeIndex(["2001-03-01 00:00", "2001-03-02 00:00", "2001-03-05 00:00"], tz="America/New_York")
    raw = pd.DataFrame({"Open": [1.0, np.nan, 3.0], "High": [1.0, 2.0, 3.0], "Low": [1.0, 2.0, 3.0],
                        "Close": [1.0, 2.0, 3.0], "Volume": [10.0, 20.0, 30.0]}, index=index)
    frame = prices.normalise(raw, date(2001, 3, 2))
    assert [d.date() for d in frame.index] == [date(2001, 3, 1)]
    assert list(frame.columns) == list(prices.COLUMNS) and frame["Dividends"].iloc[0] == 0.0


def test_a_ticker_that_never_comes_back_is_reported_missing_after_every_retry():
    waits = []

    def source(ticker, start, end):
        if ticker == "GONE":
            raise RuntimeError("no data")
        return _frame(9, "2000-01-03")

    table = prices.fetch(("SPY", "GONE"), source=source, sleep=waits.append,
                         now=pd.Timestamp("2002-01-02 23:00", tz="UTC").to_pydatetime())
    assert table.missing == ("GONE",) and "SPY" in table.frames
    assert tuple(waits) == prices.RETRY_WAITS


# --------------------------------------------------------------------------- #
# The journal
# --------------------------------------------------------------------------- #


def test_a_line_is_productions_technicals_on_bars_before_its_day_and_nothing_after(table):
    frame = table.frames["MSFT"]
    day = date(2001, 3, 15)
    bars = journal.window(frame, day)
    assert bars.index.max() < pd.Timestamp(day)
    assert bars.index.min() > pd.Timestamp(journal.two_years_before(day))
    production = frame[(frame.index > pd.Timestamp(journal.two_years_before(day))) & (frame.index < pd.Timestamp(day))]
    line = journal.line("MSFT", day, bars)
    assert line["context"]["technicals"] == build_snapshot(production).as_dict()
    assert line["context"]["technicals"]["as_of"] == "2001-03-14"
    assert line["live"]["price"] == frame["Close"].loc["2001-03-14"]
    assert line["live"]["source"] == journal.STAND_IN and line["signal"] is None
    # Rewrite everything from the line's day on: the line must not move.
    later = frame.copy()
    later.loc[later.index >= pd.Timestamp(day), ["Open", "High", "Low", "Close"]] *= 10.0
    assert journal.line("MSFT", day, journal.window(later, day)) == line


def test_the_journal_is_one_file_a_month_read_by_productions_reader(journal_dir, sessions):
    names = sorted(p.name for p in journal_dir.iterdir())
    assert names[0] == "2000-01.log" and names[-1] == "2001-12.log"
    entries = read_journal(journal_dir).entries
    assert entries and all(re.fullmatch(r"\d{4}-\d{2}\.log", n) for n in names)
    assert {e.ticker for e in entries} == {"MSFT", "XLE", "TLT"}          # the watchlist names priced
    assert all(not e.has_signal and not e.held for e in entries)          # no model, on disk
    assert all(e.live["source"] == journal.STAND_IN for e in entries)
    assert all(date.fromisoformat(e.technicals["as_of"]) < e.timestamp.date() for e in entries)
    assert all(e.timestamp.date() in set(sessions) for e in entries)       # no line on a closed day
    first_tlt = min(e.timestamp.date() for e in entries if e.ticker == "TLT")
    assert first_tlt > date(2000, 3, 1)                                    # a line needs a bar before it
    answered = journal.as_answered(entries)
    assert all(e.model_answered and e.bias == "NEUTRAL" and e.conviction == 0.0 for e in answered)
    assert '"signal": null' in (journal_dir / "2001-06.log").read_text().splitlines()[0]


# --------------------------------------------------------------------------- #
# The calendar
# --------------------------------------------------------------------------- #


def test_the_past_is_counted_in_the_days_spy_traded_and_the_production_calendar_comes_back(sessions):
    assert xp.sessions_after(date(2001, 7, 3), 1) == [date(2001, 7, 4)]   # production: 2001 has no holidays
    with historical_calendar(sessions):
        assert xp.sessions_after(date(2001, 7, 3), 1) == [date(2001, 7, 5)]
        assert xp.last_trading_day(2001, 8) == date(2001, 8, 30)
    import importlib

    for name in PATCHED:
        assert importlib.import_module(name).is_trading_day is market_calendar.is_trading_day
    assert xp.last_trading_day(2001, 8) == date(2001, 8, 31)


# --------------------------------------------------------------------------- #
# The race
# --------------------------------------------------------------------------- #


def test_an_arm_is_raced_by_the_races_own_steps(year_2001):
    lines, how, _, mine = year_2001
    theirs = hr.race_arm(momentum.NAME, lines, floor=how.floor, horizon=how.horizon, entry_rule=how.entry_rule,
                         today=how.today, source=how.source, fetcher=how.fetcher, equity=how.equity,
                         stop_multiplier=how.stop_multiplier, max_position_pct=how.max_position_pct,
                         cost_per_side=how.cost_per_side)
    assert mine == theirs and mine.n > 50
    assert {t.trade.side for t in mine.trades} == {"buy", "sell"}
    assert all(t.entry_day > t.signal_day for t in mine.trades)            # next open, never the signal's day


def test_a_is_the_checkpoints_own_veto_on_the_stand_in_price(table, sessions, year_2001):
    _, how, entries, mine = year_2001
    bars = Bars(dict(table.frames))
    with historical_calendar(sessions):
        vetoed = xp.veto_entries(entries, bars)
        a = race.arm_result(xp.VETO, vetoed, how)
        assert a.trades == tuple(xp.arm_trades(xp.VETO, vetoed, how))
    removed = sum(1 for before, after in zip(entries, vetoed) if before.is_directional and not after.is_directional)
    assert removed > 0
    assert {t.key for t in a.trades} <= {t.key for t in mine.trades}


def test_the_coin_flip_band_is_bands_for_to_the_last_digit(year_2001):
    lines, how, _, mine = year_2001
    both = hr.both_sides(lines, horizon=how.horizon, entry_rule=how.entry_rule, today=how.today, source=how.source,
                         fetcher=how.fetcher, equity=how.equity, stop_multiplier=how.stop_multiplier,
                         max_position_pct=how.max_position_pct, cost_per_side=how.cost_per_side)
    grid = sorted({pair.buy.entry_day for pair in both.values()})
    seeds = 12
    expected = hr.bands_for(mine.trades, both, grid, seeds)
    sides = {key: race.Side(p.buy.entry_day, p.buy.net, p.sell.net) for key, p in both.items()}
    keys = sorted({t.key for t in mine.trades})
    flips = race.coin_flips(keys, seeds, chunk=5)
    got = race.coin_band(mine.trades, sides, flips, {k: i for i, k in enumerate(keys)}, grid)
    for band in expected:
        mine_band = got[band.metric]
        assert mine_band["seeds"] == band.seeds == seeds
        for field in ("low", "high", "value", "percentile"):
            assert mine_band[field] == pytest.approx(getattr(band, field), rel=1e-12, abs=1e-15), (band.metric, field)


def test_cs_filled_and_missed_signals_are_race_tests_grouping(table, sessions, year_2001):
    lines, how, entries, mine = year_2001
    bars = Bars(dict(table.frames))
    with historical_calendar(sessions):
        ours = race.filled_or_missed(entries, mine.trades, bars, how)
        theirs = xp.race_tests(lines, bars, how, date(2001, 1, 1), date(2001, 1, 1))["pullback_filled_vs_missed"]
    filled = [p.net for p in ours if p.filled]
    missed = [p.net for p in ours if not p.filled]
    assert theirs["filled"]["n"] == len(filled) > 0 and theirs["missed"]["n"] == len(missed) > 0
    assert theirs["filled"]["mean_net"] == pytest.approx(sum(filled) / len(filled), rel=1e-12)
    assert theirs["missed"]["mean_net"] == pytest.approx(sum(missed) / len(missed), rel=1e-12)


def test_raced_year_by_year_the_trades_are_the_ones_raced_in_one_piece(table, sessions, journal_dir):
    """Only the ATR's first bars differ (each year warms up as the live race does); entries never do."""
    bars = Bars(dict(table.frames))
    years = race.race_years([2000, 2001], journal_dir, table.frames, bars, sessions, table.final_through)
    split = {t.key: t for y in years for t in y.arms[momentum.NAME].trades}
    with historical_calendar(sessions):
        lines = hr.offered(journal.read(journal_dir))
        how = race.settings(table.frames, table.final_through, lines)
        whole = {t.key: t for t in race.arm_result(momentum.NAME, hr.entries_for_arm(momentum.NAME, lines), how).trades}
    assert set(split) == set(whole)
    assert all(split[k].entry_day == whole[k].entry_day and split[k].trade.entry_price == whole[k].trade.entry_price
               and split[k].trade.side == whole[k].trade.side for k in split)
    same_exit = sum(1 for k in split if split[k].trade.exit_price == whole[k].trade.exit_price)
    assert same_exit / len(split) > 0.97


# --------------------------------------------------------------------------- #
# The funds
# --------------------------------------------------------------------------- #


def test_the_funds_run_clean_through_the_production_engine_and_nothing_stays_patched(table, sessions, journal_dir):
    before = (xp.timing_signals, xp.TIMING_IN, sim_market.is_trading_day, xp.is_trading_day)
    results = fund_screen.run_funds(journal_dir, table.frames, sessions, table.final_through)
    assert (xp.timing_signals, xp.TIMING_IN, sim_market.is_trading_day, xp.is_trading_day) == before
    assert results["integrity"]["ok"], results["integrity"]
    funds = results["funds"]
    assert funds["momentum"]["periods"]["all years"]["trades"]["entries"] > 0
    assert funds["momentum_pullback"]["orders"]["placed"] > 0
    # B starts at VT's first month-end with ten month-end closes: VT from 2000-05-15.
    assert results["counters"]["vt_timing"]["first_month_end"] == "2000-05-31"
    b = funds["vt_timing"]["periods"]["all years"]["vs_vt"]
    assert b["from"] == "2001-03-01" and b["days"] > 100
    assert results["counters"]["vt_timing_on_spy"]["first_month_end"] == "2000-04-28"
    assert funds["vt_timing_on_spy"]["periods"]["all years"]["vs_spy"]["days"] > 100
    assert results["vt_first_session"] == "2000-05-15"
    vt_row = funds["momentum"]["periods"]["all years"]["vs_vt"]
    assert vt_row["from"] == "2000-05-15"


# --------------------------------------------------------------------------- #
# End to end, and the report
# --------------------------------------------------------------------------- #


def test_a_screen_writes_its_results_and_a_report_with_the_network_cut(tmp_path, table, monkeypatch):
    """The whole screen, forked workers too, with every outbound connection refused: no model, no broker, no feed."""
    import socket

    def refuse(*args, **kwargs):
        raise AssertionError("the history screen tried to reach the network")

    monkeypatch.setattr(socket.socket, "connect", refuse)
    monkeypatch.setattr(socket.socket, "connect_ex", refuse)
    prices.save(table, tmp_path / "prices.csv.gz")
    assert screen.main(["run", "--out", str(tmp_path), "--processes", "2", "--seeds", "8",
                        "--first", "2001-01-02"]) == 0
    results = json.loads((tmp_path / "results.json").read_text())
    assert results["meta"]["seeds"] == 8 and results["meta"]["journal_lines"] > 0
    arm = results["race"]["arms"]["momentum"]["periods"]["all years"]
    assert arm["trades"] > 0 and arm["coin_flip_band"]["mean/day"]["seeds"] == 8
    assert "always long, same lines" in arm["coin_flip_band"]["mean/day"]["others"]
    assert arm["longs"]["vs_same_side_every_line_same_days"]["days"] > 0
    fund = results["funds"]["funds"]["momentum"]["periods"]["all years"]["trades"]
    assert fund["mean_days_held"] > 0 and fund["costs_per_year"] > 0
    assert results["funds"]["funds"]["momentum_pullback"]["order_matters"] is None
    text = (tmp_path / "report.md").read_text()
    assert text == report.render(results)
    for words in ("previous session's final close stands in", "Survivorship", "Nothing here changes the locked test",
                  "anything that uses the AI", "may mean little more than", "Read with care",
                  "How to read the coin-flip band", "adjusted for splits", "one calendar year at a time",
                  "keep them as cash", "A is then almost the momentum rule"):
        assert words in text, words


def test_a_screen_without_vt_bil_or_spy_stops_before_it_runs_anything(tmp_path, table):
    frames = {t: f for t, f in table.frames.items() if t != "BIL"}
    prices.save(prices.PriceTable(frames, table.final_through, "test", ("BIL",)), tmp_path / "prices.csv.gz")
    with pytest.raises(SystemExit, match="no prices for BIL"):
        screen.main(["run", "--out", str(tmp_path), "--processes", "1"])
    assert not (tmp_path / "journal").exists()
    with pytest.raises(SystemExit):
        screen.main(["run", "--out", str(tmp_path), "--seeds", "0"])


def test_the_verdict_is_read_from_the_paired_t_and_says_which_way():
    assert report.verdict({"mean": -0.00002, "t": -0.07}) == "no clear difference from a coin flip"
    assert report.verdict({"mean": 0.001, "t": 2.5}) == "better than a coin flip"
    assert report.verdict({"mean": -0.001, "t": -2.5}) == "worse than a coin flip"
    assert report.verdict({"mean": None, "t": None}).startswith("not known")
    period = {"coin_flip_band": {"mean/day": {"low": -0.00224, "high": -0.00201}},
              "vs_coin_flip_expected": {"mean": -0.00002, "t": -0.07}}
    assert report.band_ratio(period) == pytest.approx(abs(-0.00002 / -0.07) / ((0.00023) / 3.29))


# --------------------------------------------------------------------------- #
# The workflow and the fence
# --------------------------------------------------------------------------- #

GUARD = "The history screen cannot trade and asks no model"


def _guard_python() -> str:
    steps = yaml.safe_load((ROOT / ".github/workflows/ci.yml").read_text())["jobs"]["guardrails"]["steps"]
    run = next(step["run"] for step in steps if step.get("name") == GUARD)
    import textwrap

    return textwrap.dedent(run.split("python3 - <<'PY'\n", 1)[1].split("\nPY", 1)[0])


def _guard(tree: Path):
    import subprocess
    import sys

    return subprocess.run([sys.executable, "-c", _guard_python()], cwd=tree, capture_output=True, text=True,
                          timeout=120)


def test_the_workflow_runs_by_hand_only_holds_no_secret_and_needs_its_graveyard_row():
    path = ROOT / ".github" / "workflows" / "history-screen.yml"
    text = path.read_text()
    wf = yaml.safe_load(text)
    assert set(wf[True]) == {"workflow_dispatch"}            # "on:" reads as True in YAML
    inputs = wf[True]["workflow_dispatch"]["inputs"]
    assert inputs["name"].get("required") is True and "default" not in inputs["name"]
    assert inputs["replace"]["default"] is False
    assert "secrets." not in text
    assert wf["permissions"] == {"contents": "write"}
    assert "git add docs/research/history/" in text and "git add -A" not in text
    assert 'grep -q "history/$SCREEN_NAME/" docs/research/graveyard.md' in text
    assert "^[1-9][0-9]*$" in text


def test_the_guard_passes_the_repository_and_fails_every_way_out(tmp_path):
    import shutil

    assert _guard(ROOT).returncode == 0, _guard(ROOT).stdout
    breaches = {
        "multi-line model import": "from orchestrator import (\n    llm,\n)\n",
        "the replay harness": "from replay.runner import main\n",
        "a key from the environment": "import os\nKEY = os.environ.get('K')\n",
        "the live audit log": "from config import settings as cfg\nPATH = cfg.AUDIT_LOG_PATH\n",
        "a live log path": "PATH = 'logs/journal'\n",
        "an engine of its own": "engine = ExecutionEngine(broker, feed)\n",
        "the model's answers": "from shadow.fund import model_signal\n",
        "the hybrid arm": "signal = rule_signal('hybrid')\n",
    }
    for label, code in breaches.items():
        tree = tmp_path / label.replace(" ", "_")
        shutil.copytree(ROOT / "history", tree / "history")
        shutil.copytree(ROOT / ".github", tree / ".github")
        (tree / "history" / "breach.py").write_text(code)
        assert _guard(tree).returncode != 0, label
    tree = tmp_path / "secret"
    shutil.copytree(ROOT / "history", tree / "history")
    shutil.copytree(ROOT / ".github", tree / ".github")
    wf = tree / ".github" / "workflows" / "history-screen.yml"
    wf.write_text(wf.read_text().replace("SCREEN_SEEDS: ${{ inputs.seeds }}", "KEY: ${{ secrets.X }}"))
    assert _guard(tree).returncode != 0
