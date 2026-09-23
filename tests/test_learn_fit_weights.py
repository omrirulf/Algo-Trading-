"""The trainer: journal lines in, one weights file out, nothing else touched."""

from __future__ import annotations

import json
from datetime import date, datetime, timedelta, timezone

import pytest

from analysis import reader
from analysis.blend import EQUAL_WEIGHTS, WeightsArtifact
from analysis.returns import PriceSeries
from learn import fit_weights as fw
from orchestrator import blend as applier

# The journal lines these fixtures write must claim whatever model
# production actually runs: the trainer fits per model and discards
# every line another one wrote, so a pinned name here would test the
# discard path by accident the next time the model changes.
from orchestrator.llm import MODEL  # noqa: E402
START = date(2026, 6, 1)


class RisingSource:
    """Closes that rise 1% a session from START, for as many sessions as asked."""

    def __init__(self, sessions: int = 60, step: float = 0.01):
        self.bars = [(START + timedelta(days=i), 100.0 * (1 + step) ** i) for i in range(sessions)]
        self.calls: list[str] = []

    def closes(self, ticker, start, end):
        self.calls.append(ticker)
        return PriceSeries(ticker, self.bars)


def payload(ticker="NVDA", day=0, hour=14, *, model=MODEL, atr=0.02, gaps=(), bias="BULLISH", **scores):
    ts = datetime(START.year, START.month, START.day, hour, tzinfo=timezone.utc) + timedelta(days=day)
    signal = {"ticker": ticker, "bias": bias, "conviction": 0.5, "rationale": "r"}
    signal.update({name: scores.get(name.replace("_score", "")) for name in reader.SCORE_FIELDS})
    return {
        "ts_utc": ts.isoformat(),
        "ticker": ticker,
        "context": {"gaps": list(gaps), "technicals": {"atr_pct_of_price": atr}},
        "signal": signal,
        "usage": {"model": model, "input_tokens": 1, "output_tokens": 1},
    }


def entries(*payloads):
    return [reader.entry_from(p) for p in payloads]


def test_screened_error_and_scoreless_lines_are_left_out_and_counted():
    source = RisingSource()
    prepared = fw.prepare(entries(
        payload(day=0, news=0.5),
        payload(day=1, news=0.5, model="claude-haiku-4-5-20251001"),   # screened: the cheap model answered
        payload(day=2),                                                  # no dimension scored
        {**payload(day=3, news=0.5), "signal": None, "error": "declined"},
        payload(day=4, news=0.5, atr=None),                              # nothing to scale by
    ), source, horizon=3, today=START + timedelta(days=59))
    assert prepared.statuses["used"] == 1
    assert prepared.statuses[fw.SKIP_OTHER_MODEL] == 1
    assert prepared.statuses[fw.SKIP_NO_SCORES] == 1
    assert prepared.statuses[fw.SKIP_NO_SIGNAL] == 1
    assert prepared.statuses[fw.SKIP_NO_ATR] == 1


def test_a_dated_model_id_still_counts_as_the_full_model():
    entry = reader.entry_from(payload(model="claude-opus-5-20260901", news=0.1))
    assert fw.is_full_model(entry, "claude-opus-5")
    assert not fw.is_full_model(reader.entry_from(payload(model=None, news=0.1)), "claude-opus-5")


def test_a_signal_whose_horizon_has_not_elapsed_is_pending_and_left_out():
    source = RisingSource(sessions=5)
    prepared = fw.prepare(entries(payload(day=0, news=0.5), payload(day=3, news=0.5)),
                          source, horizon=3, today=START + timedelta(days=4))
    assert prepared.statuses["used"] == 1
    assert prepared.statuses["pending"] == 1


def test_the_target_is_the_return_in_atrs_and_is_winsorised():
    source = RisingSource(step=0.01)
    prepared = fw.prepare(entries(payload(day=0, news=0.5, atr=0.02)), source, horizon=3,
                          today=START + timedelta(days=59))
    (obs,) = prepared.observations
    # Signal at 14:00 UTC, before the close: entry is that day's close, exit three sessions on.
    assert obs.target == pytest.approx((1.01 ** 3 - 1) / 0.02)
    assert obs.when == START
    prepared = fw.prepare(entries(payload(day=0, news=0.5, atr=0.001)), source, horizon=3,
                          today=START + timedelta(days=59))
    assert prepared.observations[0].target == fw.WINSOR


def test_a_legacy_zero_beside_a_named_gap_is_read_as_null():
    scores = {"news_score": 0.0, "fundamental_score": 0.0, "analyst_score": 0.0, "insider_score": -0.2, "technical_score": None}
    out = fw.nulled_by_gaps(scores, ["fundamentals unavailable: HTTP 429", "insider transactions unavailable: x"])
    assert out["fundamental_score"] is None       # named, and 0.0
    assert out["news_score"] == 0.0               # not named: an honest neutral
    assert out["analyst_score"] == 0.0            # not named
    assert out["insider_score"] == -0.2           # named, but a real read
    out = fw.nulled_by_gaps({name: 0.0 for name in reader.SCORE_FIELDS}, ["yfinance unavailable: timeout"])
    assert out["news_score"] == 0.0 and all(out[n] is None for n in reader.SCORE_FIELDS if n != "news_score")


def test_one_observation_per_ticker_per_day_and_one_fetch_per_ticker():
    source = RisingSource()
    prepared = fw.prepare(entries(
        payload(day=0, hour=13, news=0.1), payload(day=0, hour=15, news=0.9),
        payload(ticker="MSFT", day=0, news=0.3),
    ), source, horizon=3, today=START + timedelta(days=59))
    assert prepared.statuses["used"] == 2
    assert prepared.statuses[fw.SKIP_DUPLICATE] == 1
    assert [o.scores["news_score"] for o in prepared.observations if o.ticker == "NVDA"] == [0.9]
    assert sorted(source.calls) == ["MSFT", "NVDA"]


def test_main_writes_an_artifact_the_cycle_can_load(tmp_path, monkeypatch, capsys):
    journal = tmp_path / "signal_journal.log"
    journal.write_text("".join(json.dumps(payload(day=d, news=0.5, technical=-0.2)) + "\n" for d in range(30)))
    out = tmp_path / "blend_weights.json"
    monkeypatch.setattr(fw, "YFinancePriceSource", lambda: RisingSource(sessions=400))

    assert fw.main(["--journal", str(journal), "--out", str(out), "--horizon", "3"]) == 0

    artifact = WeightsArtifact.from_dict(json.loads(out.read_text()))
    assert artifact.model == MODEL and artifact.horizon == 3
    assert set(artifact.levels) == {"global", "kind:equity", "ticker:NVDA"}
    assert artifact.levels["ticker:NVDA"].n_raw == 30
    loaded = applier.load_weights(out, model=MODEL)
    assert loaded.source == applier.SOURCE_FILE
    text = capsys.readouterr().out
    assert "observations used: 30" in text and "ticker:NVDA" in text and f"wrote {out}" in text
    assert not out.with_name(out.name + ".tmp").exists()


def test_dry_run_reports_but_writes_nothing(tmp_path, monkeypatch, capsys):
    journal = tmp_path / "signal_journal.log"
    journal.write_text(json.dumps(payload(news=0.5)) + "\n")
    out = tmp_path / "blend_weights.json"
    monkeypatch.setattr(fw, "YFinancePriceSource", lambda: RisingSource())
    assert fw.main(["--journal", str(journal), "--out", str(out), "--dry-run"]) == 0
    assert not out.exists()
    assert "blend weights" in capsys.readouterr().out


def test_a_journal_with_nothing_usable_still_writes_an_honest_empty_file(tmp_path, monkeypatch, capsys):
    journal = tmp_path / "signal_journal.log"
    journal.write_text(json.dumps(payload(news=0.5, model="claude-haiku-4-5-20251001")) + "\n")
    out = tmp_path / "blend_weights.json"
    monkeypatch.setattr(fw, "YFinancePriceSource", lambda: RisingSource())
    assert fw.main(["--journal", str(journal), "--out", str(out)]) == 0
    artifact = WeightsArtifact.from_dict(json.loads(out.read_text()))
    assert artifact.levels == {}
    assert artifact.weights_for("NVDA") == (EQUAL_WEIGHTS, "equal")
    assert "no level fitted" in capsys.readouterr().out


def test_a_missing_journal_is_exit_1_and_bad_arguments_exit_2(tmp_path, capsys):
    assert fw.main(["--journal", str(tmp_path / "none.log"), "--out", str(tmp_path / "w.json")]) == 1
    assert fw.main(["--horizon", "0"]) == 2
    assert fw.main(["--since", "2026-01-01"]) == 2



def test_the_calibration_is_fitted_from_journalled_composites_once_there_are_enough(tmp_path, monkeypatch):
    journal = tmp_path / "signal_journal.log"
    lines = []
    for d in range(30):
        line = payload(day=d, news=0.5)
        line["blend"] = {"mode": "shadow", "composite": 0.4, "level": "equal"}   # prices rise: right every time
        lines.append(json.dumps(line) + "\n")
    journal.write_text("".join(lines))
    out = tmp_path / "blend_weights.json"
    monkeypatch.setattr(fw, "YFinancePriceSource", lambda: RisingSource(sessions=400))
    assert fw.main(["--journal", str(journal), "--out", str(out)]) == 0
    artifact = WeightsArtifact.from_dict(json.loads(out.read_text()))
    assert artifact.calibration is not None
    assert artifact.calibration.n == 30
    assert artifact.calibration.probability(0.4) == pytest.approx(1.0)


def test_no_calibration_below_the_minimum_and_a_zero_composite_is_not_a_call(tmp_path, monkeypatch, capsys):
    journal = tmp_path / "signal_journal.log"
    lines = []
    for d in range(10):
        line = payload(day=d, news=0.5)
        line["blend"] = {"mode": "shadow", "composite": 0.4 if d else 0.0, "level": "equal"}
        lines.append(json.dumps(line) + "\n")
    journal.write_text("".join(lines))
    out = tmp_path / "blend_weights.json"
    monkeypatch.setattr(fw, "YFinancePriceSource", lambda: RisingSource(sessions=400))
    assert fw.main(["--journal", str(journal), "--out", str(out)]) == 0
    assert WeightsArtifact.from_dict(json.loads(out.read_text())).calibration is None
    assert "calibration: none stored (9 journalled composites" in capsys.readouterr().out
