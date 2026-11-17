"""The fallback check (replay/model_fallback_check.py, the owner's fallback of 17 Nov 2026).

One ask of the second host in production's request shape, before the cycle
relies on it. These pin which archived asks it takes, what it sends, how it
judges an answer, what it prints, and that the workflow asks with the
second host's key and nothing more.
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from orchestrator import heartbeat, llm
from orchestrator.context import TickerContext
from orchestrator.pricing import Usage
from replay import model_fallback_check as check

ROOT = Path(__file__).resolve().parent.parent
SIGNAL = {"ticker": "NVDA", "bias": "BULLISH", "conviction": 0.6, "rationale": "Trend up; news supportive.",
          "news_score": 0.5, "technical_score": 0.4, "fundamental_score": None, "analyst_score": None,
          "insider_score": None, "key_factors": ["Price above the 200-day average"]}


def _record(ticker: str, ts: str, kind: str = "first", provider: str = "openai-compatible", request=None) -> dict:
    body = request if request is not None else {
        "model": "openai/gpt-oss-120b",
        "messages": [{"role": "system", "content": f"system for {ticker}"}, {"role": "user", "content": f"user for {ticker}"}],
    }
    return {"provider": provider, "ticker": ticker, "kind": kind, "ts": ts, "request": json.dumps(body)}


def _archive(tmp_path: Path, *records: dict) -> Path:
    directory = tmp_path / "model_io"
    directory.mkdir()
    (directory / "run.jsonl").write_text("".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")
    return directory


class FakeProvider:
    """Answers a signal for the name asked (or a scripted text), recording how it was asked."""

    def __init__(self, text=None, error: str | None = None, model: str = "openai/gpt-oss-120b"):
        self.text = text
        self.error = error
        self.model = model
        self.asked: list[dict] = []

    def complete_detailed(self, system_prompt, user_prompt, json_schema, model=None, effort=None,
                          reasoning=True, check=None):
        self.asked.append({"system": system_prompt, "user": user_prompt, "schema": json_schema,
                           "model": model, "effort": effort, "check": check})
        if self.error:
            raise llm.LLMError(self.error)
        if self.text is None:
            ticker = user_prompt.rsplit("for ", 1)[-1].rstrip(".") if "for " in user_prompt else "NVDA"
            text = json.dumps({**SIGNAL, "ticker": ticker})
        else:
            text = json.dumps(self.text)
        return llm.Completion(text, Usage(model=self.model, input_tokens=4000, output_tokens=900), host="api.groq.com")

    def request_body(self, system_prompt, user_prompt, json_schema, *, model=None, effort=None, reasoning=True):
        return llm.OpenAICompatibleProvider("http://x/v1", self.model, api_key="k2").request_body(
            system_prompt, user_prompt, json_schema, model=model, effort=effort, reasoning=reasoning)


# --------------------------------------------------------------------------- #
# The questions
# --------------------------------------------------------------------------- #


def test_archived_first_asks_one_per_name_newest_first_and_the_count_is_a_cap(tmp_path):
    archive = _archive(
        tmp_path,
        _record("AAPL", "2026-11-16T15:00:00+00:00"),
        _record("NVDA", "2026-11-17T15:05:00+00:00"),
        _record("NVDA", "2026-11-16T15:05:00+00:00"),
        _record("MSFT", "2026-11-17T15:01:00+00:00", kind="retry after HTTP 503"),
        _record("XOM", "2026-11-17T15:02:00+00:00", provider="anthropic"),
        _record("SPY", "2026-11-17T15:03:00+00:00", request={"messages": "not a list"}),
    )
    chosen = check.archived_questions(archive, 5)
    assert [q.ticker for q in chosen] == ["NVDA", "AAPL"]
    assert chosen[0].system == "system for NVDA" and chosen[0].user == "user for NVDA"
    assert chosen[0].source == "archived ask of 2026-11-17T15:05"
    assert [q.ticker for q in check.archived_questions(archive, 1)] == ["NVDA"]


def test_without_an_archive_the_built_in_question_is_production_s_prompt_for_spy(tmp_path):
    (only,) = check.questions(None, 3)
    assert only.ticker == check.BUILTIN_TICKER == "SPY"
    assert only.system == heartbeat.system_prompt_for("SPY", TickerContext("SPY"))
    assert only.user == heartbeat.build_user_prompt(TickerContext("SPY"))
    assert only.user.endswith("Respond with the JSON signal for SPY.")
    assert check.questions(tmp_path / "missing", 3)[0].ticker == "SPY"
    empty = tmp_path / "empty"
    empty.mkdir()
    assert check.questions(empty, 3)[0].source.startswith("built-in")


# --------------------------------------------------------------------------- #
# The ask and its judgement
# --------------------------------------------------------------------------- #


def test_the_ask_is_production_s_call_path_with_its_schema_effort_and_check():
    provider = FakeProvider()
    result = check.ask(provider, check.Question("NVDA", "s", "u for NVDA", "test"))
    (asked,) = provider.asked
    assert asked["schema"] is heartbeat.SIGNAL_JSON_SCHEMA
    assert asked["effort"] == heartbeat.full_model_effort() == "high"
    assert asked["check"] is heartbeat.parse_signal
    assert asked["model"] is None                         # the second host's own name for the model
    assert result.ok and result.verdict == "a signal" and result.usage_reported
    assert result.input_tokens == 4000 and result.output_tokens == 900


def test_an_answer_for_another_name_or_no_signal_or_an_error_is_not_ok():
    other = check.ask(FakeProvider(text={**SIGNAL, "ticker": "AAPL"}), check.Question("NVDA", "s", "u", "t"))
    assert not other.ok and other.verdict == "a signal for AAPL, not NVDA"
    prose = check.ask(FakeProvider(text="hello"), check.Question("NVDA", "s", "u", "t"))
    assert not prose.ok and prose.verdict == "answered, not a signal"
    failed = check.ask(FakeProvider(error="http://x returned HTTP 429: busy (gave up after 4 attempt(s))"),
                       check.Question("NVDA", "s", "u", "t"))
    assert not failed.ok and failed.verdict == "error" and "HTTP 429" in failed.error


def test_the_request_shape_shows_the_parameters_and_never_the_messages():
    shape = check.request_shape(FakeProvider(), check.Question("NVDA", "secret system", "secret user", "t"))
    assert shape["model"] == "openai/gpt-oss-120b" and shape["reasoning_effort"] == "high"
    assert shape["stream"] is True and shape["stream_options"] == {"include_usage": True}
    assert shape["max_tokens"] == llm.MAX_TOKENS
    assert shape["response_format"]["type"] == "json_schema" and shape["response_format"]["strict"] is True
    assert "secret" not in json.dumps(shape)


# --------------------------------------------------------------------------- #
# The report and the exit code
# --------------------------------------------------------------------------- #


def test_the_report_counts_what_matters_and_names_no_key():
    good = check.ask(FakeProvider(), check.Question("NVDA", "s", "u for NVDA", "archived ask of 2026-11-17T15:05"))
    bad = check.ask(FakeProvider(error="http://x returned HTTP 401: bad key (gave up after 1 attempt(s))"),
                    check.Question("AAPL", "s", "u", "archived ask of 2026-11-17T15:00"))
    text = check.report("api.groq.com", {"model": "m"}, [good, bad])
    assert "fallback host: api.groq.com" in text
    assert "fallback check: 1 of 2 answered with a signal for the name asked" in text
    assert "usage reported on 1 of 1 answer(s)" in text
    assert "verdict: NOT OK" in text
    assert "verdict: OK" in check.report("api.groq.com", {}, [good])
    assert "in 4000 out 900" in text and "HTTP 401" in text
    assert "k2" not in text


def test_main_asks_the_second_host_and_exits_by_the_answers(monkeypatch, capsys):
    provider = FakeProvider()
    monkeypatch.setattr(heartbeat, "fallback_model_provider", lambda: provider)
    assert check.main([]) == check.EXIT_OK
    out = capsys.readouterr().out
    assert "asking api.groq.com 1 question(s), 1 at a time, as openai/gpt-oss-120b at high effort" in out
    assert "verdict: OK" in out and "built-in question" in out
    assert "k2" not in out

    monkeypatch.setattr(heartbeat, "fallback_model_provider", lambda: FakeProvider(text="prose"))
    assert check.main(["--count", "2"]) == check.EXIT_FAILED


def test_main_without_a_key_checks_nothing_and_says_which_secret(monkeypatch, capsys):
    monkeypatch.setattr(heartbeat, "fallback_model_provider", lambda: None)
    assert check.main([]) == check.EXIT_NO_KEY
    assert "FULL_MODEL_FALLBACK_API_KEY is empty" in capsys.readouterr().out


def test_the_real_factory_builds_nothing_in_the_suite(monkeypatch):
    """conftest keeps the second host's key out of the suite, so the check has nothing to ask."""
    assert heartbeat.fallback_model_provider() is None


# --------------------------------------------------------------------------- #
# The workflow
# --------------------------------------------------------------------------- #


def test_the_workflow_asks_with_the_second_host_s_key_only_and_runs_by_hand_only():
    text = (ROOT / ".github/workflows/model-fallback-check.yml").read_text(encoding="utf-8")
    wf = yaml.safe_load(text)
    assert wf["permissions"] == {"contents": "read", "actions": "read"}
    triggers = wf.get("on") or wf.get(True)
    assert set(triggers) == {"workflow_dispatch"}
    job = wf["jobs"]["check"]
    step = next(s for s in job["steps"] if s.get("name", "").startswith("Ask the fallback host"))
    env = step["env"]
    assert env["FULL_MODEL_FALLBACK_API_KEY"] == "${{ secrets.FULL_MODEL_FALLBACK_API_KEY }}"
    assert [k for k, v in env.items() if "secrets." in str(v)] == ["FULL_MODEL_FALLBACK_API_KEY"]
    assert "python replay/model_fallback_check.py" in step["run"]
    for banned in ("ALPACA", "ANTHROPIC", "BRIGHTDATA", "NTFY", "FULL_MODEL_API_KEY", "DEEPINFRA"):
        assert banned not in text, banned
    download = next(s for s in job["steps"] if s.get("name", "").startswith("Download"))
    assert download["continue-on-error"] is True                    # no archive: the built-in question
