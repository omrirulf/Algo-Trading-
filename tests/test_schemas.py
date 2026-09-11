"""Proves the LLM cannot smuggle quantity / price / order fields past the schema."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from app.schemas import Bias, LLMSignal

VALID = {"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.75, "rationale": "Strong earnings beat"}


def test_valid_signal_parses():
    s = LLMSignal.model_validate(VALID)
    assert s.ticker == "AAPL"
    assert s.bias is Bias.BULLISH
    assert s.conviction == 0.75


@pytest.mark.parametrize(
    "extra",
    [
        {"quantity": 500},
        {"qty": 500},
        {"notional": 1_000_000},
        {"price": 1.0},
        {"limit_price": 1.0},
        {"stop_price": 0.01},
        {"stop_loss": {"stop_price": 0.01}},
        {"take_profit": {"limit_price": 999}},
        {"order_type": "market"},
        {"type": "market"},
        {"side": "buy"},
        {"time_in_force": "gtc"},
        {"leverage": 10},
        {"max_position_pct": 0.99},
        {"api_key": "abc"},
        {"extended_hours": True},
        {"__proto__": {}},
        {"": 1},
    ],
)
def test_extra_fields_are_rejected(extra):
    with pytest.raises(ValidationError) as exc_info:
        LLMSignal.model_validate({**VALID, **extra})
    assert any(e["type"] == "extra_forbidden" for e in exc_info.value.errors())


def test_all_extra_fields_reported_at_once():
    with pytest.raises(ValidationError) as exc_info:
        LLMSignal.model_validate({**VALID, "quantity": 1, "price": 2, "side": "buy"})
    forbidden = {e["loc"][0] for e in exc_info.value.errors() if e["type"] == "extra_forbidden"}
    assert forbidden == {"quantity", "price", "side"}


@pytest.mark.parametrize("missing", ["ticker", "bias", "conviction", "rationale"])
def test_required_fields(missing):
    payload = {k: v for k, v in VALID.items() if k != missing}
    with pytest.raises(ValidationError):
        LLMSignal.model_validate(payload)


@pytest.mark.parametrize("conviction", [-0.01, 1.01, 5, "high", None])
def test_conviction_bounds(conviction):
    with pytest.raises(ValidationError):
        LLMSignal.model_validate({**VALID, "conviction": conviction})


@pytest.mark.parametrize("conviction", [0.0, 1.0, 0.5])
def test_conviction_edges_allowed(conviction):
    assert LLMSignal.model_validate({**VALID, "conviction": conviction}).conviction == conviction


@pytest.mark.parametrize("bias", ["LONG", "buy", "bullish ", "", None, 1])
def test_bias_must_be_enum(bias):
    with pytest.raises(ValidationError):
        LLMSignal.model_validate({**VALID, "bias": bias})


@pytest.mark.parametrize("bias", ["BULLISH", "BEARISH", "NEUTRAL"])
def test_bias_values(bias):
    assert LLMSignal.model_validate({**VALID, "bias": bias}).bias.value == bias


@pytest.mark.parametrize(
    "ticker",
    ["", "TOOLONGTICKER", "AA PL", "AAPL;DROP", "$AAPL", "1AAPL", "../etc", "AA\nPL"],
)
def test_ticker_format_enforced(ticker):
    with pytest.raises(ValidationError):
        LLMSignal.model_validate({**VALID, "ticker": ticker})


@pytest.mark.parametrize("ticker,expected", [("aapl", "AAPL"), (" msft ", "MSFT"), ("BRK.B", "BRK.B"), ("BF-B", "BF-B")])
def test_ticker_normalised(ticker, expected):
    assert LLMSignal.model_validate({**VALID, "ticker": ticker}).ticker == expected


def test_rationale_required_and_bounded():
    with pytest.raises(ValidationError):
        LLMSignal.model_validate({**VALID, "rationale": ""})
    with pytest.raises(ValidationError):
        LLMSignal.model_validate({**VALID, "rationale": "x" * 2001})


def test_json_schema_forbids_additional_properties():
    """The schema handed to the LLM's structured-output mode says the same thing."""
    schema = LLMSignal.model_json_schema()
    assert schema.get("additionalProperties") is False
    assert set(schema["properties"]) == {"ticker", "bias", "conviction", "rationale"}
    assert set(schema["required"]) == {"ticker", "bias", "conviction", "rationale"}
