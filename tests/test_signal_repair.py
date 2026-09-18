"""A bad read of a transparency field never costs the ticker its day; a bad
decision field still does."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest
from pydantic import ValidationError

from orchestrator import heartbeat as hb

GOOD = {"ticker": "CANE", "bias": "BULLISH", "conviction": 0.6, "rationale": "sugar is tight"}


def parse(**over):
    return hb.parse_signal(json.dumps({**GOOD, **over}))


@pytest.mark.parametrize("value", [10.0, -999, 1.0001, -1.5, "0.5", True])
def test_a_score_outside_the_scale_is_recorded_as_unknown_not_clamped(value, caplog):
    signal = parse(analyst_score=value, news_score=0.4)
    assert signal.analyst_score is None          # unknown, not "maximally bullish"
    assert signal.news_score == 0.4              # the good one is untouched
    assert "analyst_score" in caplog.text and "unknown" in caplog.text


def test_scores_inside_the_scale_pass_through_exactly():
    signal = parse(analyst_score=-1.0, insider_score=1.0, technical_score=0.0, fundamental_score=None)
    assert (signal.analyst_score, signal.insider_score, signal.technical_score, signal.fundamental_score) == (-1.0, 1.0, 0.0, None)


def test_too_many_key_factors_are_cut_to_the_limit_in_order():
    signal = parse(key_factors=[f"factor {i}" for i in range(9)])
    assert signal.key_factors == [f"factor {i}" for i in range(hb.MAX_KEY_FACTORS)]


def test_a_key_factor_that_is_not_text_is_dropped_and_a_long_one_cut():
    signal = parse(key_factors=["ok", 42, "", "x" * 500, None])
    assert signal.key_factors == ["ok", "x" * 200]


def test_an_over_long_rationale_is_cut_not_refused():
    signal = parse(rationale="r" * 2500)
    assert len(signal.rationale) == 2000


@pytest.mark.parametrize("bad", [{"conviction": 1.5}, {"conviction": -0.1}, {"bias": "LONG"}, {"ticker": ""},
                                 {"quantity": 9999}, {"rationale": ""}])
def test_the_decision_fields_and_the_closed_shape_are_still_strict(bad):
    with pytest.raises(ValidationError):
        parse(**bad)


def test_repair_never_adds_or_renames_a_field():
    payload = {**GOOD, "analyst_score": 10.0, "key_factors": ["a"] * 7, "extra": 1}
    fixed = hb.repair_transparency(payload)
    assert set(fixed) == set(payload)            # a smuggled field is left for extra="forbid" to refuse
    assert fixed is not payload and payload["analyst_score"] == 10.0   # the input is not mutated


def test_something_that_is_not_an_object_is_left_to_the_validator():
    assert hb.repair_transparency([1, 2]) == [1, 2]
    with pytest.raises(ValidationError):
        hb.parse_signal("[1, 2]")


def test_every_signal_is_validated_through_parse_signal():
    """Both the screen and the decide call parse through one function, so the
    repair reaches both; a validate call anywhere else would bypass it."""
    source = Path(hb.__file__).read_text()
    calls = [m.start() for m in re.finditer(r"LLMSignal\.model_validate\(", source)]
    assert len(calls) == 1
    body = source[source.index("def parse_signal("):]
    assert "LLMSignal.model_validate(repair_transparency(" in body.split("\ndef ", 1)[0]
