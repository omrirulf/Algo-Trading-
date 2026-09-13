"""The signal journal: what the model saw, what it said, what the engine did."""

from __future__ import annotations

import json

import pytest

from app.schemas import Bias, LLMSignal
from orchestrator import context, journal
from tests.test_context import HEADLINES, full_provider

SIGNAL = LLMSignal(
    ticker="NVDA",
    bias=Bias.BULLISH,
    conviction=0.72,
    rationale="Guidance raise corroborated by an uptrend and a fresh upgrade.",
    news_score=0.8,
    technical_score=0.5,
    fundamental_score=0.1,
    analyst_score=0.6,
    key_factors=["Guidance raised 20%", "Price above the 200-day average"],
)


def read_lines(path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


@pytest.fixture
def ctx():
    return context.gather("NVDA", HEADLINES, provider=full_provider())


def test_a_full_cycle_is_recorded(_journal_to_tmp, ctx):
    journal.record(ctx, SIGNAL, outcome={"http_status": 200, "status": "ACCEPTED"})
    (entry,) = read_lines(_journal_to_tmp)

    assert entry["ticker"] == "NVDA"
    assert entry["signal"]["conviction"] == 0.72
    assert entry["signal"]["key_factors"][0] == "Guidance raised 20%"
    assert entry["outcome"]["status"] == "ACCEPTED"
    assert entry["error"] is None


def test_the_context_behind_the_call_is_recorded_in_full(_journal_to_tmp, ctx):
    """Without the inputs, the scores cannot be second-guessed later."""
    journal.record(ctx, SIGNAL)
    (entry,) = read_lines(_journal_to_tmp)

    assert entry["context"]["headlines"] == HEADLINES
    assert entry["context"]["technicals"]["rsi14"] is not None
    assert entry["context"]["fundamentals"]["trailing_pe"] is not None
    assert entry["context"]["analysts"]["recommendation"] == "buy"


def test_failures_are_journalled_too(_journal_to_tmp, ctx):
    # A cycle that produced no signal is exactly the case worth reviewing.
    journal.record(ctx, error="model declined to answer")
    (entry,) = read_lines(_journal_to_tmp)

    assert entry["signal"] is None
    assert entry["error"] == "model declined to answer"


def test_journalling_never_breaks_the_cycle(monkeypatch, ctx, caplog):
    monkeypatch.setattr(
        journal, "get_journal_logger", lambda: (_ for _ in ()).throw(OSError("disk full"))
    )
    journal.record(ctx, SIGNAL)  # must not raise
    assert "failed to journal NVDA" in caplog.text


def test_one_line_per_ticker_per_cycle(_journal_to_tmp, ctx):
    for _ in range(3):
        journal.record(ctx, SIGNAL)
    assert len(read_lines(_journal_to_tmp)) == 3
