"""The momentum arm is a fixed function of the snapshot the model saw.

Two properties carry the whole comparison. It must be deterministic, so the
harness can recompute it over every line ever journalled and get the same
answer the cycle would have. And it must read nothing the model did not
also see, so any gap between the two is about judgement, not information.
"""

from __future__ import annotations

import pytest

from app.schemas import Bias
from orchestrator.technicals import TechnicalSnapshot
from rules import momentum


def snapshot(**fields) -> TechnicalSnapshot:
    """A snapshot with only the fields the rule reads; everything else None."""
    return TechnicalSnapshot.from_dict(fields)


# --- the rule ---------------------------------------------------------------


def test_a_confirmed_uptrend_is_bullish():
    sig = momentum.signal_for("NVDA", snapshot(return_63d=0.10, distance_sma50=0.03, annualised_volatility=0.20))
    assert sig.bias is Bias.BULLISH
    assert sig.ticker == "NVDA"


def test_a_confirmed_downtrend_is_bearish():
    sig = momentum.signal_for("XLE", snapshot(return_63d=-0.10, distance_sma50=-0.03, annualised_volatility=0.20))
    assert sig.bias is Bias.BEARISH


def test_a_quarter_and_its_average_that_disagree_is_neutral():
    """A positive quarter with price already back under its average is a
    trend that may be over. The rule declines rather than guessing."""
    sig = momentum.signal_for("NVDA", snapshot(return_63d=0.10, distance_sma50=-0.01, annualised_volatility=0.20))
    assert sig.bias is Bias.NEUTRAL
    assert sig.conviction == 0.0
    assert "disagree" in sig.rationale


# --- conviction scaling -----------------------------------------------------


def test_conviction_is_the_quarter_in_units_of_annual_vol():
    """Two quarterly sigmas is one annual sigma, so the divisor is just vol."""
    sig = momentum.signal_for("NVDA", snapshot(return_63d=0.10, distance_sma50=0.01, annualised_volatility=0.20))
    assert sig.conviction == pytest.approx(0.5)


def test_a_one_annual_sigma_move_is_full_conviction():
    sig = momentum.signal_for("NVDA", snapshot(return_63d=0.20, distance_sma50=0.01, annualised_volatility=0.20))
    assert sig.conviction == pytest.approx(1.0)


def test_conviction_is_clamped_at_one():
    sig = momentum.signal_for("NVDA", snapshot(return_63d=0.90, distance_sma50=0.01, annualised_volatility=0.20))
    assert sig.conviction == 1.0


def test_the_same_move_counts_for_more_in_a_calmer_name():
    """A 10% quarter in a 15%-vol fund is a bigger deal than in a 60%-vol name."""
    calm = momentum.signal_for("TLT", snapshot(return_63d=0.10, distance_sma50=0.01, annualised_volatility=0.15))
    wild = momentum.signal_for("NVDA", snapshot(return_63d=0.10, distance_sma50=0.01, annualised_volatility=0.60))
    assert calm.conviction > wild.conviction


def test_the_scale_constant_is_derived_not_tuned():
    """The docstring's claim: 2 * sqrt(63/252) == 1, so nothing is left over."""
    assert momentum.FULL_CONVICTION_SIGMAS * momentum.QUARTER_OF_A_YEAR == pytest.approx(1.0)


# --- thin history is an outcome, not an error --------------------------------


@pytest.mark.parametrize(
    "fields, reason",
    [
        ({"distance_sma50": 0.01, "annualised_volatility": 0.2}, "bars of history"),
        ({"return_63d": 0.1, "annualised_volatility": 0.2}, "50-day average"),
        ({"return_63d": 0.1, "distance_sma50": 0.01}, "volatility"),
        ({"return_63d": 0.1, "distance_sma50": 0.01, "annualised_volatility": 0.0}, "volatility"),
    ],
)
def test_missing_inputs_are_neutral_with_the_reason(fields, reason):
    sig = momentum.signal_for("NEW", snapshot(**fields))
    assert sig.bias is Bias.NEUTRAL
    assert sig.conviction == 0.0
    assert reason in sig.rationale


def test_no_snapshot_at_all_is_neutral():
    sig = momentum.signal_for("NEW", None)
    assert sig.bias is Bias.NEUTRAL
    assert "no technicals" in sig.rationale


# --- determinism ------------------------------------------------------------


def test_the_same_snapshot_always_gives_the_same_signal():
    snap = snapshot(return_63d=0.07, distance_sma50=0.02, annualised_volatility=0.25)
    a, b = momentum.signal_for("NVDA", snap), momentum.signal_for("NVDA", snap)
    assert a == b


def test_it_round_trips_through_the_journal_dict():
    """What the harness does: rebuild the snapshot from the journalled dict."""
    live = snapshot(return_63d=0.07, distance_sma50=0.02, annualised_volatility=0.25)
    rebuilt = TechnicalSnapshot.from_dict(live.as_dict())
    assert momentum.signal_for("NVDA", live) == momentum.signal_for("NVDA", rebuilt)


def test_from_dict_ignores_fields_a_future_line_might_carry():
    snap = TechnicalSnapshot.from_dict({"return_63d": 0.1, "some_new_field": 42})
    assert snap.return_63d == 0.1
    assert snap.sma50 is None
