"""Replaying must be cheap to trust: never trade, never write, never crash.

The harness is meant to be run repeatedly while iterating on a prompt, so its
failure modes matter more than its happy path. A bad prompt edit should show
up as a reported error on one entry, not as an exception that loses the run.
"""

from __future__ import annotations

import json

import pytest

from app.schemas import Bias, LLMSignal
from config import settings as cfg
from orchestrator.context import TickerContext
from orchestrator.llm import LLMError
from replay import runner
from replay.compare import ReplaySummary, SignalDiff
from replay.replay_journal import render


def journal_line(ticker="AAPL", bias="BULLISH", conviction=0.72, ts="2026-09-12T14:00:00+00:00",
                 signal=True, headlines=("something happened",)):
    context = TickerContext(ticker=ticker, headlines=list(headlines))
    record = {
        "ts_utc": ts, "ticker": ticker, "context": context.as_dict(),
        "signal": ({"ticker": ticker, "bias": bias, "conviction": conviction,
                    "rationale": "because"} if signal else None),
        "outcome": None, "error": None,
    }
    return json.dumps(record)


def sig(ticker="AAPL", bias=Bias.BULLISH, conviction=0.72):
    return LLMSignal(ticker=ticker, bias=bias, conviction=conviction, rationale="because")


def answering(bias="BULLISH", conviction=0.8):
    def complete(system, user, schema):
        ticker = user.split("TICKER: ")[1].split("\n")[0]
        return json.dumps({"ticker": ticker, "bias": bias, "conviction": conviction,
                           "rationale": "replayed"})
    return complete


# --- loading --------------------------------------------------------------


def test_entries_are_loaded_with_their_original_answer():
    [entry] = runner.load_entries([journal_line()])
    assert entry.ticker == "AAPL"
    assert entry.original.conviction == 0.72
    assert "TICKER: AAPL" in entry.prompt


def test_a_truncated_final_line_is_skipped_not_fatal():
    """The journal is append-only and may be read mid-write."""
    entries = list(runner.load_entries([journal_line(), '{"context": ']))
    assert len(entries) == 1


def test_a_cycle_that_produced_no_signal_is_still_replayable():
    """Asking whether a new prompt rescues a failed cycle is the point."""
    [entry] = runner.load_entries([journal_line(signal=False)])
    assert entry.original is None
    assert entry.prompt


def test_the_ticker_filter_selects():
    lines = [journal_line("AAPL"), journal_line("MSFT"), journal_line("AAPL")]
    assert len(list(runner.load_entries(lines, ticker="aapl"))) == 2


def test_a_line_that_cannot_be_rebuilt_is_skipped_with_a_warning(caplog):
    bad = json.dumps({"ts_utc": "t", "context": {"headlines": []}, "signal": None})
    entries = list(runner.load_entries([bad, journal_line()]))
    assert len(entries) == 1


# --- replaying ------------------------------------------------------------


def test_a_replay_produces_a_comparable_signal():
    [entry] = runner.load_entries([journal_line(conviction=0.72)])
    result = runner.replay_one(entry, "sys", answering("BULLISH", 0.9))
    assert result.error is None
    assert result.replayed.conviction == 0.9
    assert result.diff.conviction_delta == pytest.approx(0.18)


def test_the_replay_sends_the_reconstructed_prompt():
    seen = {}

    def capture(system, user, schema):
        seen["system"], seen["user"] = system, user
        return json.dumps({"ticker": "AAPL", "bias": "NEUTRAL", "conviction": 0.1,
                           "rationale": "r"})

    [entry] = runner.load_entries([journal_line(headlines=("a very specific headline",))])
    runner.replay_one(entry, "MY SYSTEM PROMPT", capture)
    assert seen["system"] == "MY SYSTEM PROMPT"
    assert "a very specific headline" in seen["user"]
    assert "Respond with the JSON signal for AAPL" in seen["user"]


@pytest.mark.parametrize(
    "boom, expected",
    [
        (LLMError("declined"), "declined"),
        (ValueError("nope"), "invalid output"),
        (RuntimeError("kaboom"), "unexpected RuntimeError"),
    ],
)
def test_a_failing_model_call_is_reported_not_raised(boom, expected):
    """One bad entry must not lose the whole run."""
    [entry] = runner.load_entries([journal_line()])

    def failing(system, user, schema):
        raise boom

    result = runner.replay_one(entry, "sys", failing)
    assert result.replayed is None
    assert expected in result.error


def test_off_schema_output_is_a_finding_not_a_crash():
    """A prompt edit that breaks the shape is information about the prompt."""
    [entry] = runner.load_entries([journal_line()])
    result = runner.replay_one(entry, "sys", lambda s, u, j: "not json at all")
    assert result.replayed is None
    assert "invalid output" in result.error


def test_an_answer_for_the_wrong_ticker_is_rejected():
    [entry] = runner.load_entries([journal_line("AAPL")])
    result = runner.replay_one(
        entry, "sys",
        lambda s, u, j: json.dumps({"ticker": "MSFT", "bias": "BULLISH",
                                    "conviction": 0.9, "rationale": "r"}),
    )
    assert result.replayed is None
    assert "MSFT" in result.error


def test_errored_entries_are_excluded_from_the_summary():
    entries = list(runner.load_entries([journal_line("AAPL"), journal_line("MSFT")]))
    results = [
        runner.replay_one(entries[0], "sys", answering()),
        runner.replay_one(entries[1], "sys", lambda s, u, j: "garbage"),
    ]
    assert runner.summarise(results).n == 1


# --- what counts as a change ---------------------------------------------


def test_a_small_conviction_move_is_not_consequential():
    diff = SignalDiff("AAPL", sig(conviction=0.90), sig(conviction=0.85))
    assert not diff.consequential


def test_crossing_the_floor_is_consequential():
    below, above = cfg.MIN_CONVICTION - 0.05, cfg.MIN_CONVICTION + 0.05
    assert SignalDiff("AAPL", sig(conviction=below), sig(conviction=above)).crossed_floor


def test_a_bias_flip_is_consequential():
    diff = SignalDiff("AAPL", sig(bias=Bias.BULLISH), sig(bias=Bias.BEARISH))
    assert diff.bias_flipped and diff.consequential


def test_neutral_to_bullish_below_the_floor_does_not_cross_it():
    """A flip that still cannot trade has not changed what the engine does."""
    low = cfg.MIN_CONVICTION - 0.1
    diff = SignalDiff("AAPL", sig(bias=Bias.NEUTRAL, conviction=low),
                      sig(bias=Bias.BULLISH, conviction=low))
    assert not diff.crossed_floor


def test_a_rescued_cycle_is_consequential():
    diff = SignalDiff("AAPL", None, sig())
    assert diff.appeared and diff.consequential


def test_a_lost_signal_is_consequential():
    diff = SignalDiff("AAPL", sig(), None)
    assert diff.vanished and diff.consequential


def test_uniform_boldness_is_named():
    diffs = [SignalDiff("AAPL", sig(conviction=0.5), sig(conviction=0.7)) for _ in range(5)]
    summary = ReplaySummary(diffs)
    assert summary.conviction_drift_direction == "bolder"
    assert summary.mean_conviction_delta == pytest.approx(0.2)


def test_no_drift_is_not_reported_as_drift():
    diffs = [SignalDiff("AAPL", sig(conviction=0.70), sig(conviction=0.705))]
    assert ReplaySummary(diffs).conviction_drift_direction is None


# --- the report ----------------------------------------------------------


def test_the_report_renders_with_no_changes():
    entries = list(runner.load_entries([journal_line(conviction=0.72)]))
    results = [runner.replay_one(entries[0], "sys", answering("BULLISH", 0.72))]
    text = render(runner.summarise(results), results, "the live prompt", verbose=False)
    assert "No change that would alter what the engine does" in text


def test_the_report_renders_when_everything_errored():
    entries = list(runner.load_entries([journal_line()]))
    results = [runner.replay_one(entries[0], "sys", lambda s, u, j: "garbage")]
    text = render(runner.summarise(results), results, "src", verbose=False)
    assert "Nothing to compare" in text
    assert "ERRORS" in text


def test_the_report_warns_against_reading_change_as_improvement():
    """The trap this tool sets: more changes looking like a better prompt."""
    entries = list(runner.load_entries([journal_line()]))
    results = [runner.replay_one(entries[0], "sys", answering())]
    text = render(runner.summarise(results), results, "src", verbose=False)
    assert "not thereby a better prompt" in text
    assert "score_journal" in text
