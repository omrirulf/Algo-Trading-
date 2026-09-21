"""A context that flips its own answer under repetition is not comparable to
a different model that "disagreed" with it -- some of that disagreement is
this. The grouping logic (a flat list of repeated calls sliced back into
per-context chunks) is exactly the kind of off-by-one-prone code that needs
a real end-to-end test, not just a unit test of the pure aggregation.
"""

from __future__ import annotations

import json

import pytest

from app.schemas import Bias
from replay import determinism_check as dc
from replay import runner
from replay.runner import ReplayEntry, ReplayResult


def journal_line(ticker="AAPL", bias="BULLISH", conviction=0.72):
    from orchestrator.context import TickerContext

    context = TickerContext(ticker=ticker, headlines=["h"])
    record = {
        "ts_utc": "2026-09-12T14:00:00+00:00", "ticker": ticker,
        "context": context.as_dict(),
        "signal": {"ticker": ticker, "bias": bias, "conviction": conviction, "rationale": "r"},
        "outcome": None, "error": None,
    }
    return json.dumps(record)


def answer(bias=Bias.BULLISH, conviction=0.7):
    from app.schemas import LLMSignal
    return LLMSignal(ticker="AAPL", bias=bias, conviction=conviction, rationale="r")


def result(bias=None, conviction=None, error=None) -> ReplayResult:
    entry = ReplayEntry(ticker="AAPL", ts_utc=None, prompt="p", original=None)
    replayed = None if error else answer(bias or Bias.BULLISH, conviction if conviction is not None else 0.7)
    return ReplayResult(entry=entry, replayed=replayed, error=error)


# --------------------------------------------------------------------------- #
# context_stability
# --------------------------------------------------------------------------- #


def test_identical_repeats_are_fully_unanimous():
    group = [result(Bias.BULLISH, 0.7) for _ in range(3)]
    stability = dc.context_stability("AAPL", group, floor=0.30)
    assert stability.assessable
    assert stability.direction_unanimous
    assert stability.trade_decision_unanimous
    assert stability.conviction_spread == pytest.approx(0.0)


def test_a_direction_flip_is_caught():
    group = [result(Bias.BULLISH, 0.7), result(Bias.NEUTRAL, 0.1), result(Bias.BULLISH, 0.7)]
    stability = dc.context_stability("AAPL", group, floor=0.30)
    assert not stability.direction_unanimous
    assert not stability.trade_decision_unanimous  # a direction flip is also a trade flip


def test_a_trade_decision_flip_without_a_direction_flip():
    """Same bias every time, but conviction lands on both sides of the floor."""
    group = [result(Bias.BULLISH, 0.20), result(Bias.BULLISH, 0.60)]
    stability = dc.context_stability("AAPL", group, floor=0.30)
    assert stability.direction_unanimous
    assert not stability.trade_decision_unanimous


def test_errors_are_excluded_not_counted_as_a_third_answer():
    group = [result(Bias.BULLISH, 0.7), result(error="boom"), result(Bias.BULLISH, 0.7)]
    stability = dc.context_stability("AAPL", group, floor=0.30)
    assert stability.n_answered == 2
    assert stability.direction_unanimous


def test_fewer_than_two_answers_is_not_assessable():
    group = [result(Bias.BULLISH, 0.7), result(error="boom"), result(error="boom")]
    stability = dc.context_stability("AAPL", group, floor=0.30)
    assert stability.n_answered == 1
    assert not stability.assessable
    assert stability.conviction_spread is None


# --------------------------------------------------------------------------- #
# render
# --------------------------------------------------------------------------- #


def test_render_reports_both_unanimity_rates():
    stabilities = [
        dc.context_stability("AAPL", [result(Bias.BULLISH, 0.7)] * 3, floor=0.30),
        dc.context_stability("MSFT", [result(Bias.BULLISH, 0.7), result(Bias.NEUTRAL, 0.1),
                                       result(Bias.BULLISH, 0.7)], floor=0.30),
    ]
    text = dc.render(stabilities, floor=0.30, repeats=3, label="test-model / high")
    assert "Direction unanimous across every repeat      : 1/2 (50%)" in text
    assert "Trade decision unanimous across every repeat : 1/2 (50%)" in text


def test_render_with_nothing_assessable_says_so_rather_than_dividing_by_zero():
    stabilities = [dc.context_stability("AAPL", [result(error="boom"), result(error="boom")], floor=0.30)]
    text = dc.render(stabilities, floor=0.30, repeats=2, label="m")
    assert "nothing here can be judged" in text


# --------------------------------------------------------------------------- #
# main() end to end: the flat-list-sliced-back-into-groups logic
# --------------------------------------------------------------------------- #


def test_main_groups_the_flat_call_list_back_by_context(tmp_path, monkeypatch, capsys):
    journal = tmp_path / "journal.log"
    journal.write_text(
        journal_line("AAPL") + "\n" + journal_line("MSFT") + "\n", encoding="utf-8",
    )

    # Flat call order for limit=2, repeats=3: AAPL x3, then MSFT x3.
    script = [
        ("AAPL", "BULLISH", 0.5), ("AAPL", "BULLISH", 0.5), ("AAPL", "BULLISH", 0.5),
        ("MSFT", "BULLISH", 0.6), ("MSFT", "NEUTRAL", 0.1), ("MSFT", "BULLISH", 0.6),
    ]
    state = {"n": 0}

    def complete(system, user, schema):
        ticker, bias, conviction = script[state["n"]]
        state["n"] += 1
        return json.dumps({"ticker": ticker, "bias": bias, "conviction": conviction, "rationale": "r"})

    monkeypatch.setattr(runner, "measured_completer", lambda **kwargs: (complete, []))

    exit_code = dc.main([
        "--journal", str(journal), "--limit", "2", "--repeats", "3",
        "--model", "test-model",
    ])
    assert exit_code == 0
    out = capsys.readouterr().out
    # AAPL was stable across all 3 repeats, MSFT flipped once -- exactly one
    # of the two contexts is unanimous, and it must be the right one.
    assert "1/2 (50%)" in out


def test_main_rejects_a_single_repeat():
    assert dc.main(["--model", "m", "--repeats", "1"]) == 2


def test_a_blank_effort_input_means_no_effort_asked(tmp_path, monkeypatch):
    """A workflow_dispatch text input left blank arrives as the string '',
    not as absent. Passed straight through, that would ask the provider for
    reasoning at effort '' instead of leaving reasoning off entirely."""
    journal = tmp_path / "journal.log"
    journal.write_text(journal_line("AAPL") + "\n", encoding="utf-8")

    seen_effort = {}

    def fake_measured_completer(**kwargs):
        seen_effort["effort"] = kwargs["effort"]

        def complete(system, user, schema):
            return json.dumps({"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.5,
                               "rationale": "r"})
        return complete, []

    monkeypatch.setattr(runner, "measured_completer", fake_measured_completer)
    dc.main(["--journal", str(journal), "--limit", "1", "--repeats", "2",
             "--model", "m", "--effort", ""])
    assert seen_effort["effort"] is None
