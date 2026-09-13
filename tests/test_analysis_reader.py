"""Reading the journal, including the malformed lines a long-lived log collects."""

from __future__ import annotations

import json
from datetime import datetime, timezone

from analysis.reader import read_journal, read_lines

FULL = {
    "ts": "2026-03-02 14:00:02,331",
    "ts_utc": "2026-03-02T14:00:02.331000+00:00",
    "event": "signal_generated",
    "ticker": "nvda",
    "context": {"headlines": ["x"], "gaps": ["fundamentals unavailable: HTTP 429"]},
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
