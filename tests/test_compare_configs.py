"""Comparing configurations must not overstate what it knows.

The tool's whole risk is that "95% agreement" reads as "95% as good". These
tests pin the guardrails against that: agreement is measured against the
incumbent rather than against truth, an unjudgeable cell reports unknown
rather than passing, and the report says so in words.
"""

from __future__ import annotations

import pytest

from app.schemas import Bias, LLMSignal
from config import settings as cfg
from orchestrator.pricing import Usage
from replay.compare import SignalDiff
from replay.compare_configs import (
    EFFORT_NOTCHES,
    MODEL_TIERS,
    Cell,
    clears_floor,
    staircase_order,
)
from replay.compare_models import render


def sig(bias=Bias.BULLISH, conviction=0.72):
    return LLMSignal(ticker="AAPL", bias=bias, conviction=conviction, rationale="r")


def cell(model="claude-opus-5", effort="low", out_tokens=800, agree=20, n=20, errors=0):
    diffs = []
    for i in range(n):
        before = sig()
        after = before if i < agree else sig(bias=Bias.BEARISH)
        diffs.append(SignalDiff("AAPL", before, after))
    usages = [Usage(model=model, input_tokens=1420, output_tokens=out_tokens)] * n
    return Cell(model=model, effort=effort, usages=usages, diffs=diffs,
                errors=["boom"] * errors)


# --- agreement ------------------------------------------------------------


def test_full_agreement_is_one():
    assert cell(agree=20).bias_agreement == 1.0


def test_disagreement_lowers_it():
    assert cell(agree=10).bias_agreement == pytest.approx(0.5)


def test_trade_agreement_is_stricter_than_bias_agreement():
    """Matching direction but crossing the floor is a different portfolio."""
    below, above = cfg.MIN_CONVICTION - 0.1, cfg.MIN_CONVICTION + 0.1
    diffs = [SignalDiff("AAPL", sig(conviction=above), sig(conviction=below))]
    c = Cell(model="claude-opus-5", effort="low", diffs=diffs,
             usages=[Usage(model="claude-opus-5", input_tokens=1, output_tokens=1)])
    assert c.bias_agreement == 1.0          # same direction
    assert c.tradeable_agreement == 0.0     # but one would trade and one would not


def test_a_cell_with_nothing_comparable_reports_unknown():
    """None rather than a pass: a false pass prunes the walk irreversibly."""
    empty = Cell(model="claude-opus-5", effort="low")
    assert empty.bias_agreement is None
    assert clears_floor(empty, 0.9) is None


def test_an_unknown_cell_is_not_treated_as_passing():
    assert clears_floor(Cell(model="claude-opus-5", effort="low"), 0.9) is not True


def test_the_floor_is_a_threshold_not_a_ranking():
    assert clears_floor(cell(agree=19), 0.90) is True     # 95%
    assert clears_floor(cell(agree=17), 0.90) is False    # 85%


# --- cost -----------------------------------------------------------------


def test_cost_comes_from_measured_tokens():
    c = cell(out_tokens=1000)
    assert c.cost_per_call > 0
    assert c.mean_output_tokens == 1000


def test_more_output_costs_more():
    assert cell(out_tokens=2000).cost_per_call > cell(out_tokens=500).cost_per_call


def test_monthly_scales_with_the_watchlist():
    c = cell()
    assert c.monthly_usd(30) == pytest.approx(c.monthly_usd(10) * 3)


def test_a_cell_with_no_usage_has_no_cost():
    assert Cell(model="claude-opus-5", effort="low").cost_per_call is None


def test_failures_are_counted_against_the_cell():
    assert cell(n=18, agree=18, errors=2).failure_rate == pytest.approx(0.1)


# --- the walk -------------------------------------------------------------


def test_the_walk_enters_at_the_strongest_tier_and_cheapest_effort():
    """Entry is budget-bounded and unambiguous to step away from."""
    assert staircase_order()[0] == (MODEL_TIERS[0], EFFORT_NOTCHES[0])


def test_effort_notches_run_cheapest_first():
    assert EFFORT_NOTCHES[0] == "low"


def test_model_tiers_run_strongest_first():
    assert MODEL_TIERS[0] == "claude-opus-5"


def test_every_cell_is_reachable():
    assert len(staircase_order()) == len(MODEL_TIERS) * len(EFFORT_NOTCHES)


# --- the report says what it cannot tell you ------------------------------


def test_the_report_says_agreement_is_not_correctness():
    """The trap: reading 95% agreement as 95% as good."""
    text = render([cell()], 0.9, 30, None)
    assert "Agreement is not correctness" in text
    assert "score_journal" in text


def test_the_report_names_the_cold_cache_caveat():
    text = render([cell()], 0.9, 30, None)
    assert "cold cache" in text


def test_the_report_marks_a_cell_below_the_floor():
    text = render([cell(agree=10)], 0.9, 30, None)
    assert "below floor" in text


def test_the_report_marks_the_cheapest_acceptable_cell():
    cheap = cell(model="claude-sonnet-5", out_tokens=500)
    text = render([cell(), cheap], 0.9, 30, cheap)
    assert "cheapest acceptable" in text


def test_the_report_renders_with_an_unpriceable_cell():
    unknown = Cell(model="mystery-model", effort="low",
                   usages=[Usage(model="mystery-model", input_tokens=10)],
                   diffs=[SignalDiff("AAPL", sig(), sig())])
    assert "n/a" in render([unknown], 0.9, 30, None)
