"""Batch custom_ids are checked before the API sees them.

The first historical replay built 200 prompts, pulled three years of OHLC for
35 tickers, and then had the whole batch refused with
``requests.0.custom_id: String should match pattern '^[a-zA-Z0-9_-]{1,64}$'``
because the ids carried a colon. That is the expensive end of a run to find
out at, so the pattern is enforced at construction, and both replay harnesses
build their ids through the one helper that knows it.
"""

from __future__ import annotations

from datetime import date

import pytest

from orchestrator.llm import CUSTOM_ID_PATTERN, BatchRequest, batch_custom_id
from replay import historical, signal_sanity


def _req(cid: str) -> BatchRequest:
    return BatchRequest(cid, "SYS", "USER", {"type": "object"})


def test_the_pattern_is_the_apis():
    assert CUSTOM_ID_PATTERN.pattern == r"^[a-zA-Z0-9_-]{1,64}$"


@pytest.mark.parametrize("bad", ["AAPL:real", "AAPL 2025-03-14", "", "x" * 65, "BRK.B"])
def test_an_id_the_api_would_refuse_is_refused_at_construction(bad):
    with pytest.raises(ValueError, match="batch_custom_id"):
        _req(bad)


@pytest.mark.parametrize("good", ["AAPL_real", "AAPL_2025-03-14", "a", "x" * 64])
def test_an_id_the_api_accepts_is_accepted(good):
    assert _req(good).custom_id == good


def test_the_helper_joins_and_sanitises():
    assert batch_custom_id("AAPL", "real") == "AAPL_real"
    assert batch_custom_id("AAPL", date(2025, 3, 14)) == "AAPL_2025-03-14"
    # A dotted share class survives as something the API takes, and the
    # date is still legible.
    assert batch_custom_id("BRK.B", date(2025, 3, 14)) == "BRK-B_2025-03-14"
    assert batch_custom_id("A", "B", "C") == "A_B_C"


def test_the_helper_caps_the_length():
    assert len(batch_custom_id("t" * 100)) == 64


def test_the_helper_refuses_an_empty_id():
    with pytest.raises(ValueError):
        batch_custom_id("")


def test_every_helper_output_is_constructible():
    for parts in (("AAPL", "real"), ("BRK.B", date(2025, 3, 14)), ("a b:c/d", 1)):
        _req(batch_custom_id(*parts))


def test_sanity_trial_ids_pass_the_pattern():
    t = signal_sanity.Trial("MSFT", signal_sanity.SCRAMBLED, "S", "U")
    assert CUSTOM_ID_PATTERN.match(t.custom_id)
    assert t.custom_id == "MSFT_scrambled"


def test_historical_sample_ids_pass_the_pattern():
    s = historical.Sample(ticker="GLD", day="2025-12-15", index=300, system_prompt="S", user_prompt="U", headlines=0)
    assert CUSTOM_ID_PATTERN.match(s.custom_id)
    assert s.custom_id == "GLD_2025-12-15"
