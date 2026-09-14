"""The two-stage funnel: a cheap model screens, the full model decides.

The property under test is that the screen can only ever *save* a call. It
never places the trade itself, it never changes what the full model is asked,
and when it breaks the system behaves exactly as it did before it existed.
"""

from __future__ import annotations

import json

import pytest

from orchestrator import heartbeat as hb
from orchestrator import llm
from orchestrator.llm import Completion, LLMError
from orchestrator.pricing import PRICES, Usage


def _completion(payload: dict, model: str) -> Completion:
    return Completion(
        text=json.dumps(payload),
        usage=Usage(model=model, input_tokens=1400, output_tokens=120),
    )


def _signal(bias: str, conviction: float = 0.8) -> dict:
    return {"ticker": "AAPL", "bias": bias, "conviction": conviction, "rationale": "r"}


@pytest.fixture
def funnel(monkeypatch):
    """Screening on, both stages faked, every call recorded."""
    calls: dict[str, list] = {"screen": [], "full": [], "posted": []}
    monkeypatch.setattr(hb, "SCREENING_ENABLED", True)
    monkeypatch.setattr(hb, "fetch_news", lambda t: ["news"])
    monkeypatch.setattr(
        hb, "post_signal",
        lambda s, dispatcher=None: (calls["posted"].append(s), {"status": "ACCEPTED", "reason": "ok"})[1],
    )

    def wire(screen_answer, full_answer=None):
        def screen(system_prompt, user_prompt, schema):
            calls["screen"].append((system_prompt, user_prompt, schema))
            if isinstance(screen_answer, Exception):
                raise screen_answer
            return _completion(screen_answer, hb.SCREENING_MODEL)

        def full(system_prompt, user_prompt, schema):
            calls["full"].append((system_prompt, user_prompt, schema))
            return _completion(full_answer or _signal("BULLISH"), llm.MODEL)

        monkeypatch.setattr(hb, "screen_signal", screen)
        monkeypatch.setattr(hb, "call_llm", full)
        return calls

    return wire


def _journal_entry(path) -> dict:
    lines = path.read_text().splitlines()
    assert len(lines) == 1, lines
    return json.loads(lines[0])


# --- the saving ------------------------------------------------------------


def test_a_neutral_screen_never_asks_the_full_model(funnel):
    calls = funnel(_signal("NEUTRAL", 0.2))
    result = hb.process_ticker("AAPL")
    assert result.stage == hb.SCREENED
    assert len(calls["screen"]) == 1
    assert calls["full"] == []
    assert calls["posted"] == []


def test_a_screened_ticker_is_journalled_with_the_screen_answer(funnel, _journal_to_tmp):
    funnel(_signal("NEUTRAL", 0.2))
    hb.process_ticker("AAPL")
    entry = _journal_entry(_journal_to_tmp)
    assert entry["screen"]["model"] == hb.SCREENING_MODEL
    assert entry["screen"]["bias"] == "NEUTRAL"
    assert entry["screen"]["usage"]["model"] == hb.SCREENING_MODEL
    # The screen's answer *is* the recorded signal on a screened ticker,
    # so a later scorer can price what the funnel chose not to look at.
    assert entry["signal"]["bias"] == "NEUTRAL"
    assert entry["outcome"] is None
    assert entry["usage"]["model"] == hb.SCREENING_MODEL


# --- the escalation --------------------------------------------------------


@pytest.mark.parametrize("bias", ["BULLISH", "BEARISH"])
def test_a_directional_screen_escalates_to_the_full_model(funnel, bias):
    calls = funnel(_signal(bias, 0.7), full_answer=_signal("BULLISH", 0.9))
    result = hb.process_ticker("AAPL")
    assert result.stage == hb.COMPLETED
    assert len(calls["screen"]) == 1
    assert len(calls["full"]) == 1
    # The full model, not the screen, is what reached the engine.
    assert calls["posted"][0].conviction == 0.9


def test_both_stages_see_the_identical_prompt(funnel):
    calls = funnel(_signal("BULLISH"))
    hb.process_ticker("AAPL")
    assert calls["screen"][0] == calls["full"][0]


def test_an_escalated_ticker_records_both_answers(funnel, _journal_to_tmp):
    funnel(_signal("BEARISH", 0.6), full_answer=_signal("BULLISH", 0.9))
    hb.process_ticker("AAPL")
    entry = _journal_entry(_journal_to_tmp)
    # The disagreement is the number that decides whether the screen is
    # trustworthy, and it is only measurable if both answers are kept.
    assert entry["screen"]["bias"] == "BEARISH"
    assert entry["signal"]["bias"] == "BULLISH"
    assert entry["usage"]["model"] == llm.MODEL


# --- the failure mode that must not silence the system ---------------------


@pytest.mark.parametrize(
    "failure",
    [LLMError("screen down"), json.JSONDecodeError("bad", "{", 0)],
    ids=["api-error", "non-json"],
)
def test_a_broken_screen_falls_through_to_the_full_model(funnel, failure, _journal_to_tmp):
    calls = funnel(failure, full_answer=_signal("BULLISH", 0.9))
    result = hb.process_ticker("AAPL")
    assert result.stage == hb.COMPLETED
    assert len(calls["full"]) == 1
    entry = _journal_entry(_journal_to_tmp)
    assert entry["screen"]["model"] == hb.SCREENING_MODEL
    assert "error" in entry["screen"]
    assert entry["signal"]["bias"] == "BULLISH"


def test_a_screen_answering_outside_the_schema_falls_through(funnel):
    calls = funnel({"ticker": "AAPL", "bias": "NEUTRAL", "conviction": 0.2, "rationale": "r", "qty": 100})
    result = hb.process_ticker("AAPL")
    # extra="forbid" rejects the smuggled field; that is a screen failure,
    # not a NEUTRAL, so the full model is asked.
    assert result.stage == hb.COMPLETED
    assert len(calls["full"]) == 1


def test_screening_off_means_one_call_and_no_screen_block(funnel, monkeypatch, _journal_to_tmp):
    calls = funnel(_signal("NEUTRAL"))
    monkeypatch.setattr(hb, "SCREENING_ENABLED", False)
    hb.process_ticker("AAPL")
    assert calls["screen"] == []
    assert len(calls["full"]) == 1
    assert _journal_entry(_journal_to_tmp)["screen"] is None


# --- the cycle-level view --------------------------------------------------


def _result(ticker: str, stage: str, status: str | None = None):
    return hb.TickerResult(ticker, stage, status=status)


def test_a_fully_screened_cycle_is_not_an_outage():
    """Every ticker screened NEUTRAL is a judgement, not 'nothing was judged'."""
    report = hb.CycleReport(
        tickers=("AAPL", "MSFT"),
        results=(_result("AAPL", hb.SCREENED), _result("MSFT", hb.SCREENED)),
    )
    assert report.produced_nothing is False
    assert len(report.screened) == 2


def test_screened_is_not_a_failure_stage():
    assert hb.SCREENED not in hb.FAILURE_STAGES
    assert hb.SCREENED in hb.STAGE_LABELS


def test_summary_reports_screened_apart_from_failures():
    report = hb.CycleReport(
        tickers=("AAPL", "MSFT", "NVDA"),
        results=(
            _result("AAPL", hb.SCREENED),
            _result("MSFT", hb.COMPLETED, "ACCEPTED"),
            _result("NVDA", hb.CONTEXT_FAILED),
        ),
    )
    text = hb.render_summary(report)
    assert "1 of 3** screened NEUTRAL" in text
    assert hb.SCREENING_MODEL in text
    assert "| " + hb.STAGE_LABELS[hb.CONTEXT_FAILED] + " | 1 |" in text
    assert "| " + hb.STAGE_LABELS[hb.SCREENED] not in text
    assert "Nothing reached the engine" not in text


def test_summary_of_a_fully_screened_cycle_is_calm():
    report = hb.CycleReport(
        tickers=("AAPL",), results=(_result("AAPL", hb.SCREENED),)
    )
    text = hb.render_summary(report)
    assert "Nothing reached the engine" not in text
    assert "What to check" not in text
    assert "1 of 1** screened NEUTRAL" in text


# --- the request shape the cheap model accepts -----------------------------


def _capture_create(monkeypatch):
    seen: dict = {}

    class _Block:
        type = "text"
        text = json.dumps(_signal("NEUTRAL"))

    class _Response:
        content = [_Block()]
        usage = None

    def fake_create(**kwargs):
        seen.update(kwargs)
        return _Response()

    monkeypatch.setattr(llm, "usage_from_response", lambda r, m: Usage(model=m, input_tokens=1, output_tokens=1))
    provider = llm.AnthropicSignalProvider("test-key")
    monkeypatch.setattr(provider, "_create", fake_create)
    return provider, seen


def test_reasoning_off_omits_thinking_and_effort(monkeypatch):
    provider, seen = _capture_create(monkeypatch)
    out = provider.complete_detailed("s", "u", {"type": "object"}, model=llm.SCREENING_MODEL, reasoning=False)
    assert seen["model"] == llm.SCREENING_MODEL
    assert "thinking" not in seen
    assert "effort" not in seen["output_config"]
    # Structured output is not a reasoning feature; the screen keeps it.
    assert seen["output_config"]["format"]["type"] == "json_schema"
    assert out.usage.model == llm.SCREENING_MODEL


def test_the_production_path_still_reasons(monkeypatch):
    provider, seen = _capture_create(monkeypatch)
    provider.complete_detailed("s", "u", {"type": "object"})
    assert seen["model"] == llm.MODEL
    assert seen["thinking"] == {"type": "adaptive"}
    assert seen["output_config"]["effort"] == llm.EFFORT


def test_screen_signal_asks_the_cheap_model_without_reasoning(monkeypatch):
    seen: dict = {}

    class _Provider:
        def __init__(self, key):
            pass

        def complete_detailed(self, s, u, j, **kw):
            seen.update(kw)
            return _completion(_signal("NEUTRAL"), hb.SCREENING_MODEL)

    monkeypatch.setattr(hb, "AnthropicSignalProvider", _Provider)
    hb.screen_signal("s", "u", {})
    assert seen == {"model": hb.SCREENING_MODEL, "reasoning": False}


def test_the_screening_model_is_priced():
    """A journal line the cost scorer cannot price is a silent hole in the bill."""
    assert hb.SCREENING_MODEL in PRICES
    assert PRICES[hb.SCREENING_MODEL].input_per_mtok < PRICES[llm.MODEL].input_per_mtok
    assert PRICES[hb.SCREENING_MODEL].output_per_mtok < PRICES[llm.MODEL].output_per_mtok
