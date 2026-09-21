"""A race is only a race if every arm ran the same course.

The properties that decide that: held lines are offered to nobody; the
rule arms are recomputed from the technicals on the line, not read from
anywhere else; every arm is scored against prices fetched once, over the
widest window any of them needs, so the order they run in cannot change
what any of them sees.
"""

from __future__ import annotations

import json
from dataclasses import replace
from datetime import date, datetime, timedelta, timezone

import pytest

from analysis import horse_race
from analysis.horse_race import (
    MODEL_ARM,
    ArmResult,
    direction_agreement,
    entries_for_arm,
    offered,
    prewarm,
    render,
)
from analysis.reader import JournalEntry
from analysis.returns import PriceSeries
from backtest.simulate import MIN_WARMUP_BARS
from backtest.sweep import Outcome
from rules import control, momentum
from tests.test_baseline_compare import FakeFetcher, FakePriceSource, _at, _trade, _warm_frame

UPTREND = {"return_63d": 0.10, "distance_sma50": 0.03, "annualised_volatility": 0.20}
STAMP = datetime(2026, 3, 2, 14, tzinfo=timezone.utc)


def line(ticker="NVDA", bias="BULLISH", conviction=0.72, technicals=UPTREND,
         held=False, stamp=STAMP, signal=True) -> JournalEntry:
    return JournalEntry(
        ticker=ticker, timestamp=stamp, timestamp_is_exact=True,
        bias=bias if signal else None, conviction=conviction if signal else None,
        technicals=dict(technicals) if technicals else {}, held=held,
    )


# --- who gets asked -------------------------------------------------------------


def test_a_held_line_is_offered_to_no_arm():
    lines = offered([line(), line(held=True), line(stamp=None)])
    assert len(lines) == 1
    assert not lines[0].held


def test_the_model_arm_is_the_journal_as_written():
    lines = offered([line(bias="BEARISH"), line(signal=False)])
    model = entries_for_arm(MODEL_ARM, lines)
    assert [e.bias for e in model] == ["BEARISH"]
    assert model[0] is lines[0]


def test_the_momentum_arm_is_recomputed_from_the_lines_own_technicals():
    lines = offered([line(bias="BEARISH"), line(technicals=None, signal=False)])
    arm = entries_for_arm(momentum.NAME, lines)
    assert len(arm) == 2, "the rule answers every offered line, signal or not"
    assert arm[0].bias == "BULLISH" and arm[0].conviction == pytest.approx(0.5)
    assert arm[1].bias == "NEUTRAL" and arm[1].conviction == 0.0
    # Ticker and timestamp untouched, so the scorer joins the same return.
    assert arm[0].ticker == lines[0].ticker and arm[0].timestamp == lines[0].timestamp


def test_the_control_arm_takes_a_side_on_every_offered_line():
    lines = offered([line(signal=False, technicals=None) for _ in range(5)])
    arm = entries_for_arm(control.NAME, lines)
    assert len(arm) == 5
    assert all(e.is_directional for e in arm)
    assert all(e.conviction == control.CONVICTION for e in arm)


# --- agreement --------------------------------------------------------------------


def test_direction_agreement_counts_only_lines_where_both_took_a_side():
    a = [line(ticker="A", bias="BULLISH"), line(ticker="B", bias="BEARISH"), line(ticker="C", bias="NEUTRAL")]
    b = [line(ticker="A", bias="BULLISH"), line(ticker="B", bias="BULLISH"), line(ticker="C", bias="BULLISH")]
    rate, n = direction_agreement(a, b)
    assert n == 2 and rate == pytest.approx(0.5)


def test_direction_agreement_with_no_overlap_is_not_zero():
    assert direction_agreement([line(bias="NEUTRAL")], [line(bias="BULLISH")]) == (None, 0)


# --- one fetch per ticker, widest window ----------------------------------------


class RecordingSource:
    def __init__(self):
        self.asked: list[tuple] = []

    def closes(self, ticker, start, end):
        self.asked.append((ticker, start, end))
        return PriceSeries(ticker, [])


def test_prewarm_asks_each_source_once_per_ticker_over_the_widest_window():
    early, late = date(2026, 3, 2), date(2026, 3, 9)
    lines = offered([
        line(stamp=_at(late)), line(stamp=_at(early)),          # NVDA, out of order
        line(ticker="XLE", stamp=_at(late)),
    ])
    source, fetcher = RecordingSource(), FakeFetcher({})
    prewarm(lines, source, fetcher, horizon=3, today=date(2026, 3, 20))

    assert [a[0] for a in source.asked] == ["NVDA", "XLE"]
    nvda_close, nvda_ohlc = source.asked[0], fetcher.asked[0]
    assert nvda_close[1] == early and nvda_close[2] == date(2026, 3, 20)
    assert nvda_ohlc[1] == early and nvda_ohlc[2] == late + timedelta(days=3 * 2 + 10)


# --- render -----------------------------------------------------------------------


def test_render_names_every_arm_and_marks_thin_rows():
    results = [
        ArmResult("model", 10, 4, 3, Outcome("model", [_trade(0.02), _trade(-0.01)]), 1),
        ArmResult("momentum", 10, 10, 8, Outcome("momentum", [_trade(0.01)] * 25), 0),
        ArmResult("random", 10, 10, 10, Outcome("random", []), 0),
    ]
    text = render(
        results, floor=0.3, horizon=3, window_start=date(2026, 3, 2), window_end=date(2026, 3, 9),
        agreement=0.5, agreed_on=4, watchlist_return=0.01, watchlist_n=80, watchlist_total=80,
        watchlist_missing=0, spy_return=None,
    )
    assert "THREE ARMS" in text
    for name in ("model", "momentum", "random"):
        assert name in text
    assert "<- too few" in text          # the 2-trade model row
    assert text.count("<- too few") == 1  # the 25-trade momentum row is not marked
    assert "n/a" in text                  # SPY had no data


# --- end to end, no network ---------------------------------------------------------


def test_main_races_all_three_arms_on_a_tiny_journal(tmp_path, monkeypatch, capsys):
    warm = _warm_frame()
    signal_day = warm.index[MIN_WARMUP_BARS].date()
    stamp = _at(signal_day)

    journal = tmp_path / "signal_journal.log"
    journal.write_text("\n".join([
        json.dumps({"ts_utc": stamp.isoformat(), "ticker": "NVDA",
                    "context": {"technicals": UPTREND},
                    "signal": {"bias": "BULLISH", "conviction": 0.72}}),
        json.dumps({"ts_utc": stamp.isoformat(), "ticker": "NVDA",
                    "context": {"technicals": UPTREND}, "held": True}),
    ]) + "\n", encoding="utf-8")

    closes = PriceSeries("NVDA", [(signal_day + timedelta(days=i), 100.0 * 1.01 ** i) for i in range(10)])
    monkeypatch.setattr(horse_race, "YFinancePriceSource", lambda: FakePriceSource({"NVDA": closes}))
    monkeypatch.setattr(horse_race, "OhlcFetcher", lambda: FakeFetcher({"NVDA": warm}))

    assert horse_race.main(["--journal", str(journal)]) == 0
    out = capsys.readouterr().out
    assert "THREE ARMS" in out
    for name in ("model", momentum.NAME, control.NAME):
        assert name in out
