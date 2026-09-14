"""Cost has to be measured, and an unknown price has to say so.

Until now cost was an estimate: an assumed output length times a list price,
which then drove a real decision about how many tickers to watch. These tests
pin the two properties that make the measured version trustworthy -- it reads
the API's own counts, and it refuses to invent a number it does not have.
"""

from __future__ import annotations

import pytest

from orchestrator.pricing import (
    CACHE_READ_MULTIPLIER,
    PRICES,
    Usage,
    cost_usd,
    monthly_usd,
    usage_from_response,
)


class FakeUsage:
    def __init__(self, **fields):
        for key, value in fields.items():
            setattr(self, key, value)


class FakeResponse:
    def __init__(self, usage=None, model="claude-opus-5"):
        if usage is not None:
            self.usage = usage
        self.model = model


# --- an unknown price is not free ----------------------------------------


def test_an_unknown_model_costs_none_not_zero():
    """Zero would sum into a total that understates the bill."""
    assert cost_usd(Usage(model="something-new", input_tokens=10_000)) is None


def test_every_known_model_prices():
    for model in PRICES:
        assert cost_usd(Usage(model=model, input_tokens=1000, output_tokens=1000)) > 0


# --- the arithmetic -------------------------------------------------------


def test_cost_is_input_plus_output_at_list_price():
    usage = Usage(model="claude-opus-5", input_tokens=1_000_000, output_tokens=1_000_000)
    assert cost_usd(usage) == pytest.approx(5.00 + 25.00)


def test_output_dominates_at_this_prompt_shape():
    """~1,400 input against a thinking response: the bill is mostly output.

    This is why effort is a bigger lever than model tier here.
    """
    usage = Usage(model="claude-opus-5", input_tokens=1420, output_tokens=1500)
    assert usage.output_share > 0.8


def test_a_cache_read_is_much_cheaper_than_a_fresh_read():
    fresh = cost_usd(Usage(model="claude-opus-5", input_tokens=10_000))
    cached = cost_usd(Usage(model="claude-opus-5", cache_read_input_tokens=10_000))
    assert cached == pytest.approx(fresh * CACHE_READ_MULTIPLIER)


def test_cheaper_tiers_are_actually_cheaper():
    same = dict(input_tokens=1420, output_tokens=1500)
    opus = cost_usd(Usage(model="claude-opus-5", **same))
    sonnet = cost_usd(Usage(model="claude-sonnet-5", **same))
    haiku = cost_usd(Usage(model="claude-haiku-4-5", **same))
    assert opus > sonnet > haiku


def test_a_stronger_model_thinking_less_can_beat_a_weaker_one_thinking_more():
    """The cost guide's central point, as arithmetic.

    Fixing the model and tuning effort never finds this cell.
    """
    opus_low = cost_usd(Usage(model="claude-opus-5", input_tokens=1420, output_tokens=600))
    sonnet_medium = cost_usd(Usage(model="claude-sonnet-5", input_tokens=1420, output_tokens=2000))
    assert opus_low < sonnet_medium


def test_monthly_scales_linearly():
    assert monthly_usd(0.05, 30) == pytest.approx(monthly_usd(0.05, 10) * 3)


# --- reading usage off a response ----------------------------------------


def test_usage_is_read_from_the_response():
    response = FakeResponse(FakeUsage(input_tokens=100, output_tokens=200,
                                      cache_read_input_tokens=50))
    usage = usage_from_response(response)
    assert (usage.input_tokens, usage.output_tokens) == (100, 200)
    assert usage.cache_read_input_tokens == 50


def test_a_response_with_no_usage_block_does_not_raise():
    """A moved field must not take down a cycle that produced a good signal."""
    usage = usage_from_response(FakeResponse(), model="claude-opus-5")
    assert usage.input_tokens == 0
    assert usage.model == "claude-opus-5"


def test_a_missing_field_counts_as_zero():
    usage = usage_from_response(FakeResponse(FakeUsage(input_tokens=100)))
    assert usage.input_tokens == 100
    assert usage.output_tokens == 0


def test_a_non_numeric_field_counts_as_zero():
    usage = usage_from_response(FakeResponse(FakeUsage(input_tokens="lots")))
    assert usage.input_tokens == 0


def test_the_response_model_wins_over_the_requested_one():
    """A server-side fallback can answer on a different model than was asked."""
    response = FakeResponse(FakeUsage(input_tokens=10), model="claude-opus-4-8")
    assert usage_from_response(response, model="claude-opus-5").model == "claude-opus-4-8"


def test_usage_serialises_with_its_cost():
    payload = Usage(model="claude-opus-5", input_tokens=1420, output_tokens=1500).as_dict()
    assert payload["cost_usd"] > 0
    assert payload["input_tokens"] == 1420
