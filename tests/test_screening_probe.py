"""The probe that says whether the screening endpoint is really wired.

Its whole reason to exist is that every misconfiguration here is silent, so
the thing worth testing is that it is *loud* -- a non-zero status and a named
cause -- and that it never prints the key, since its output is meant to be
pasted into a run summary.
"""

from __future__ import annotations

import pytest

from backtest import probe_screening as probe
from orchestrator.llm import SCREENING_KEY_ENV_VARS, Completion, LLMError, Usage

SECRET = "AIzaTOTALLYSECRETVALUE"


@pytest.fixture(autouse=True)
def _no_screening_env(monkeypatch):
    for name in (*SCREENING_KEY_ENV_VARS, "SCREENING_BASE_URL", "SCREENING_MODEL"):
        monkeypatch.delenv(name, raising=False)


def test_the_canonical_spelling_wins_over_the_alternatives(monkeypatch):
    monkeypatch.setenv("SCREENING_API_KEY", "canonical")
    monkeypatch.setenv("GEMINI_API_KEY", "alternative")
    assert probe.key_for() == ("SCREENING_API_KEY", "canonical")


def test_an_alternative_spelling_is_still_found(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", SECRET)
    assert probe.key_for() == ("GEMINI_API_KEY", SECRET)


def test_whitespace_only_is_not_a_key(monkeypatch):
    monkeypatch.setenv("SCREENING_API_KEY", "   ")
    assert probe.key_for() == (None, None)


def test_nothing_configured_is_not_a_fault(monkeypatch, capsys):
    assert probe.main() == 0
    out = capsys.readouterr().out
    assert "Screening is off" in out
    assert "not a fault" in out


def test_a_key_with_no_endpoint_is_a_failure(monkeypatch, capsys):
    monkeypatch.setenv("GEMINI_API_KEY", SECRET)
    assert probe.main() == 1
    out = capsys.readouterr().out
    assert "MISCONFIGURED" in out
    assert "paid for nothing" in out
    # It has to say which name carried it, or the report cannot be acted on.
    assert "GEMINI_API_KEY" in out
    assert SECRET not in out


def test_a_base_url_with_no_model_is_a_failure(monkeypatch, capsys):
    monkeypatch.setenv("SCREENING_BASE_URL", "https://example.test/v1")
    assert probe.main() == 1
    assert "SCREENING_MODEL is empty" in capsys.readouterr().out


def test_a_refused_call_reports_rather_than_raises(monkeypatch, capsys):
    class Refusing:
        def __init__(self, **kwargs):
            pass

        def complete_detailed(self, *a, **k):
            raise LLMError(f"400 bad key: {SECRET}")

    monkeypatch.setattr(probe, "OpenAICompatibleProvider", Refusing)
    monkeypatch.setenv("SCREENING_API_KEY", SECRET)
    monkeypatch.setenv("SCREENING_BASE_URL", "https://example.test/v1")
    monkeypatch.setenv("SCREENING_MODEL", "some-model")
    assert probe.main() == 1
    out = capsys.readouterr().out
    assert "REFUSED" in out
    # The endpoint echoed the key back in its error body. It must not survive.
    assert SECRET not in out
    assert "<redacted>" in out


def test_an_answer_outside_the_schema_is_a_failure(monkeypatch, capsys):
    class Chatty:
        def __init__(self, **kwargs):
            pass

        def complete_detailed(self, *a, **k):
            return Completion(text="Sure! Here is your signal.", usage=None)

    monkeypatch.setattr(probe, "OpenAICompatibleProvider", Chatty)
    monkeypatch.setenv("SCREENING_BASE_URL", "https://example.test/v1")
    monkeypatch.setenv("SCREENING_MODEL", "some-model")
    assert probe.main() == 1
    assert "not in the schema" in capsys.readouterr().out


def test_a_good_answer_still_sends_you_to_the_recall_check(monkeypatch, capsys):
    class Good:
        def __init__(self, **kwargs):
            pass

        def complete_detailed(self, *a, **k):
            return Completion(
                text='{"ticker": "PROBE", "bias": "NEUTRAL", "conviction": 0.1, "rationale": "probe"}',
                usage=Usage(model="some-model", input_tokens=500, output_tokens=40),
            )

    monkeypatch.setattr(probe, "OpenAICompatibleProvider", Good)
    monkeypatch.setenv("SCREENING_BASE_URL", "https://example.test/v1")
    monkeypatch.setenv("SCREENING_MODEL", "some-model")
    assert probe.main() == 0
    out = capsys.readouterr().out
    assert "answers in the schema" in out
    # Answering is not agreeing. The probe must not be mistaken for a verdict.
    assert "not the same as agreeing" in out
    assert "compare_screening.py" in out
    assert "escalation-recall" in out


def test_a_reasoning_model_is_called_out_by_its_output_tokens(monkeypatch, capsys):
    class Verbose:
        def __init__(self, **kwargs):
            pass

        def complete_detailed(self, *a, **k):
            return Completion(
                text='{"ticker": "PROBE", "bias": "NEUTRAL", "conviction": 0.1, "rationale": "probe"}',
                usage=Usage(model="m", input_tokens=500, output_tokens=9000),
            )

    monkeypatch.setattr(probe, "OpenAICompatibleProvider", Verbose)
    monkeypatch.setenv("SCREENING_BASE_URL", "https://example.test/v1")
    monkeypatch.setenv("SCREENING_MODEL", "m")
    assert probe.main() == 0
    assert "reasoned anyway" in capsys.readouterr().out


def test_the_probe_never_asks_for_reasoning(monkeypatch):
    """The screen is always asked with reasoning off; a probe that asked
    differently would be measuring a call production never makes."""
    seen = {}

    class Recording:
        def __init__(self, **kwargs):
            seen.update(kwargs)

        def complete_detailed(self, *a, **k):
            seen.update(k)
            return Completion(
                text='{"ticker": "PROBE", "bias": "NEUTRAL", "conviction": 0.1, "rationale": "p"}',
                usage=None,
            )

    monkeypatch.setattr(probe, "OpenAICompatibleProvider", Recording)
    monkeypatch.setenv("SCREENING_BASE_URL", "https://example.test/v1")
    monkeypatch.setenv("SCREENING_MODEL", "m")
    monkeypatch.setenv("GROQ_API_KEY", SECRET)
    assert probe.main() == 0
    assert seen["reasoning"] is False
    assert seen["model"] == "m"
    assert seen["base_url"] == "https://example.test/v1"
    assert seen["api_key"] == SECRET
