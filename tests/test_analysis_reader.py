"""Reading the journal, including the malformed lines a long-lived log collects."""

from __future__ import annotations

import json
from datetime import datetime, timezone

import pytest

from analysis import reader
from analysis.reader import read_journal, read_lines

FULL = {
    "ts": "2026-03-02 14:00:02,331",
    "ts_utc": "2026-03-02T14:00:02.331000+00:00",
    "event": "signal_generated",
    "ticker": "nvda",
    "context": {
        "headlines": ["x"],
        # A scored dimension needs its source section in the context, or the
        # reader treats the score as having nothing behind it.
        "analysts": "Mean target 180.00 (n=42), consensus BUY",
        "gaps": ["fundamentals unavailable: HTTP 429"],
    },
    "signal": {
        "ticker": "NVDA", "bias": "BULLISH", "conviction": 0.72, "rationale": "r",
        "news_score": 0.8, "technical_score": 0.5,
        "fundamental_score": None, "analyst_score": 0.6,
        "key_factors": ["Guidance raised 20%"],
    },
    "outcome": {"http_status": 200, "status": "ACCEPTED"},
    "error": None,
}


def line(payload: dict) -> str:
    return json.dumps(payload) + "\n"


def test_a_full_entry_is_parsed_field_by_field():
    (entry,) = read_lines([line(FULL)]).entries

    assert entry.ticker == "NVDA"  # normalised
    assert entry.timestamp == datetime(2026, 3, 2, 14, 0, 2, 331000, tzinfo=timezone.utc)
    assert entry.timestamp_is_exact
    assert entry.bias == "BULLISH" and entry.conviction == 0.72
    assert entry.scores["news_score"] == 0.8
    assert entry.scores["fundamental_score"] is None
    assert entry.available_scores() == {
        "news_score": 0.8, "technical_score": 0.5, "analyst_score": 0.6
    }
    assert entry.gaps == ["fundamentals unavailable: HTTP 429"]
    assert entry.outcome_status == "ACCEPTED"
    assert entry.has_signal and entry.is_directional and entry.direction == 1


def test_the_naive_timestamp_is_a_fallback_and_is_flagged():
    payload = {k: v for k, v in FULL.items() if k != "ts_utc"}
    (entry,) = read_lines([line(payload)]).entries

    assert entry.timestamp == datetime(2026, 3, 2, 14, 0, 2, 331000, tzinfo=timezone.utc)
    assert not entry.timestamp_is_exact  # so it never earns a same-day entry


def test_a_journal_line_written_before_insider_score_existed_still_parses():
    """Adding a dimension must not orphan the history the scorer needs."""
    payload = {**FULL, "signal": {k: v for k, v in FULL["signal"].items()}}
    assert "insider_score" not in payload["signal"]

    (entry,) = read_lines([line(payload)]).entries
    assert entry.scores["insider_score"] is None
    assert entry.scores["news_score"] == 0.8
    assert "insider_score" not in entry.available_scores()


def test_neutral_has_a_signal_but_no_direction():
    payload = {**FULL, "signal": {**FULL["signal"], "bias": "NEUTRAL"}}
    (entry,) = read_lines([line(payload)]).entries
    assert entry.has_signal and not entry.is_directional and entry.direction == 0


def test_a_cycle_that_produced_no_signal_is_still_an_entry():
    payload = {"ts_utc": FULL["ts_utc"], "ticker": "AAPL", "signal": None,
               "context": {"gaps": []}, "error": "model declined to answer"}
    (entry,) = read_lines([line(payload)]).entries
    assert not entry.has_signal
    assert entry.error == "model declined to answer"


def test_a_truncated_final_line_is_skipped_not_fatal():
    """A killed process leaves half a line; months of good data must survive it."""
    read = read_lines([line(FULL), '{"ticker": "AAPL", "sig'])
    assert len(read.entries) == 1
    assert read.skipped == 1
    assert read.total_lines == 2


def test_lines_without_a_ticker_are_not_journal_records():
    read = read_lines([line({"event": "something_else"}), "[]", "null"])
    assert read.entries == [] and read.skipped == 3


def test_blank_lines_are_not_counted_as_anything():
    read = read_lines(["\n", "  \n", line(FULL)])
    assert read.total_lines == 1 and read.skipped == 0


def test_non_numeric_and_infinite_values_become_none():
    payload = {**FULL, "signal": {**FULL["signal"], "conviction": "high", "news_score": 1e999}}
    (entry,) = read_lines([line(payload)]).entries
    assert entry.conviction is None
    assert entry.scores["news_score"] is None


def test_an_unparseable_timestamp_leaves_the_entry_usable():
    payload = {**FULL, "ts_utc": "not a date", "ts": "also not a date"}
    (entry,) = read_lines([line(payload)]).entries
    assert entry.timestamp is None
    assert entry.bias == "BULLISH"


def test_read_journal_round_trips_a_real_file(tmp_path):
    path = tmp_path / "signal_journal.log"
    path.write_text(line(FULL) + line({**FULL, "ticker": "AAPL"}), encoding="utf-8")
    read = read_journal(path)
    assert [e.ticker for e in read.entries] == ["NVDA", "AAPL"]


def test_the_blend_record_comes_through_and_composite_reads_it():
    payload = {**FULL, "blend": {"mode": "shadow", "composite": 0.31, "coverage": 0.8, "level": "equal"}}
    entry = reader.entry_from(payload)
    assert entry.blend["level"] == "equal"
    assert entry.composite == pytest.approx(0.31)


def test_a_line_without_a_blend_has_no_composite():
    entry = reader.entry_from(FULL)
    assert entry.blend == {} and entry.composite is None
    entry = reader.entry_from({**FULL, "blend": None})
    assert entry.blend == {} and entry.composite is None
    entry = reader.entry_from({**FULL, "blend": {"composite": None}})
    assert entry.composite is None


def test_the_model_and_the_atr_come_through_for_the_trainer():
    entry = reader.entry_from({
        **FULL,
        "usage": {"model": "claude-opus-5", "input_tokens": 1},
        "context": {**FULL["context"], "technicals": {"atr_pct_of_price": 0.031}},
    })
    assert entry.model == "claude-opus-5"
    assert entry.atr_pct == pytest.approx(0.031)
    bare = reader.entry_from(FULL)
    assert bare.model is None and bare.atr_pct is None


def test_the_whole_technicals_section_rides_on_the_entry():
    """The rule arms are functions of this, so the harness needs all of it,
    not the one ATR field the trainer happened to want."""
    from analysis.reader import entry_from

    payload = {
        "ticker": "NVDA",
        "ts_utc": "2026-09-21T14:00:00+00:00",
        "context": {"technicals": {"return_63d": 0.07, "distance_sma50": 0.02,
                                   "annualised_volatility": 0.25, "atr_pct_of_price": 0.02}},
        "signal": {"bias": "BULLISH", "conviction": 0.5},
    }
    entry = entry_from(payload)
    assert entry.technicals["return_63d"] == 0.07
    assert entry.atr_pct == 0.02


def test_a_line_with_no_technicals_has_an_empty_dict_not_none():
    from analysis.reader import entry_from

    entry = entry_from({"ticker": "NVDA", "ts_utc": "2026-09-21T14:00:00+00:00", "context": {}})
    assert entry.technicals == {}


def test_a_held_line_is_flagged_so_a_race_can_leave_it_out_of_every_arm():
    from analysis.reader import entry_from

    held = entry_from({"ticker": "NVDA", "ts_utc": "2026-09-21T14:00:00+00:00",
                       "context": {}, "held": True})
    asked = entry_from({"ticker": "NVDA", "ts_utc": "2026-09-21T14:00:00+00:00",
                        "context": {}, "signal": {"bias": "NEUTRAL", "conviction": 0.1}})
    assert held.held is True
    assert asked.held is False
