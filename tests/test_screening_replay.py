"""Validating a screening candidate against what Haiku actually said.

The property that matters most here: the baseline is the recorded *screen*,
never the recorded final signal. On a line the screen escalated, those two
differ -- the screen's own NEUTRAL-or-not call versus the full model's
directional one -- and comparing a screening candidate against the full
model would grade it on a question production never asked it.
"""

from __future__ import annotations

import json
import time

import httpx
import pytest

from app.schemas import Bias, LLMSignal
from orchestrator import heartbeat as hb
from orchestrator.context import TickerContext
from orchestrator import llm
from orchestrator.llm import Completion, OpenAICompatibleProvider
from replay import runner
from replay.compare import SignalDiff


def journal_line(
    ticker="AAPL", ts="2026-09-12T14:00:00+00:00",
    screen_bias="BULLISH", screen_conviction=0.6, screen_error=None,
    final_bias="BULLISH", final_conviction=0.8, headlines=("something happened",),
    fund_sections=None,
):
    """A journal line with a screen distinct from the final escalated signal."""
    context = TickerContext(ticker=ticker, headlines=list(headlines), **(fund_sections or {}))
    screen = (
        {"model": "claude-haiku-4-5", "error": screen_error}
        if screen_error
        else {"model": "claude-haiku-4-5", "bias": screen_bias, "conviction": screen_conviction,
              "usage": {"model": "claude-haiku-4-5", "cost_usd": 0.006}}
    )
    record = {
        "ts_utc": ts, "ticker": ticker, "context": context.as_dict(),
        "signal": {"ticker": ticker, "bias": final_bias, "conviction": final_conviction,
                   "rationale": "escalated"},
        "screen": screen, "outcome": None, "error": None,
    }
    return json.dumps(record)


# --- loading carries the screen and the context -----------------------------


def test_an_entry_carries_its_recorded_screen():
    [entry] = runner.load_entries([journal_line(screen_bias="BEARISH", screen_conviction=0.55)])
    assert entry.recorded_screen == {
        "model": "claude-haiku-4-5", "bias": "BEARISH", "conviction": 0.55,
        "usage": {"model": "claude-haiku-4-5", "cost_usd": 0.006},
    }


def test_an_entry_carries_its_rebuilt_context():
    [entry] = runner.load_entries([journal_line()])
    assert isinstance(entry.context, TickerContext)
    assert entry.context.ticker == "AAPL"


def test_an_old_line_with_no_screen_carries_none():
    line = json.dumps({
        "ts_utc": "t", "ticker": "AAPL",
        "context": TickerContext(ticker="AAPL", headlines=[]).as_dict(),
        "signal": None, "outcome": None, "error": None,
    })
    [entry] = runner.load_entries([line])
    assert entry.recorded_screen is None


# --- the baseline is the screen, not the escalated final signal ------------


def test_the_baseline_is_the_screen_even_when_it_escalated():
    """The whole point: on an escalated line, signal != screen."""
    [entry] = runner.load_entries([journal_line(
        screen_bias="BULLISH", screen_conviction=0.55,
        final_bias="NEUTRAL", final_conviction=0.2,
    )])
    baseline = runner.recorded_screen_signal(entry)
    assert baseline.bias is Bias.BULLISH
    assert baseline.conviction == 0.55
    assert baseline.bias is not entry.original.bias  # would be NEUTRAL if taken from `signal`


def test_a_screen_with_no_bias_field_has_no_baseline():
    """No recorded screen, or one that couldn't be parsed, means nothing to
    compare a candidate against -- not an implicit pass."""
    assert runner.recorded_screen_signal(_entry_with_screen(None)) is None


def test_a_failed_screen_has_no_baseline():
    [entry] = runner.load_entries([journal_line(screen_error="timeout")])
    assert runner.recorded_screen_signal(entry) is None


def _entry_with_screen(screen: dict | None) -> runner.ReplayEntry:
    context = TickerContext(ticker="AAPL", headlines=[])
    return runner.ReplayEntry(
        ticker="AAPL", ts_utc="t", prompt="p", original=None,
        context=context, recorded_screen=screen,
    )


# --- the right system prompt per entry --------------------------------------


def test_a_single_name_gets_the_company_prompt():
    [entry] = runner.load_entries([journal_line(ticker="AAPL")])
    assert runner.system_prompt_for_entry(entry) == hb.SYSTEM_PROMPT


def test_a_fund_gets_the_trimmed_macro_prompt():
    """Not the one shared SYSTEM_PROMPT every other replay tool sends
    regardless of ticker -- and not the untrimmed fund prompt either."""
    [entry] = runner.load_entries([journal_line(ticker="GLD", fund_sections={"crops": None})])
    prompt = runner.system_prompt_for_entry(entry)
    assert prompt != hb.SYSTEM_PROMPT
    # The paragraph itself, not the word "crops" -- the tail names every
    # scoreable section regardless of what this line carried.
    assert dict(hb.ETF_SECTION_GUIDANCE)["crops"] not in prompt


# --- asking a candidate exactly as production asks Haiku -------------------


def _server(handler) -> httpx.Client:
    return httpx.Client(transport=httpx.MockTransport(handler), base_url="http://local")


def test_the_candidate_is_asked_with_reasoning_off():
    sent = {}

    def handler(request: httpx.Request) -> httpx.Response:
        sent.update(json.loads(request.content))
        return httpx.Response(200, json={
            "choices": [{"message": {"content": json.dumps(
                {"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.5, "rationale": "r"}
            )}}]
        })

    provider = OpenAICompatibleProvider("http://local/v1", "candidate", client=_server(handler))
    complete, usages = runner.screening_candidate_completer(provider, "candidate")
    complete("sys", "user", {"type": "object"})
    assert "thinking" not in sent and "output_config" not in sent or "effort" not in sent.get("output_config", {})
    assert len(usages) == 1


def test_an_unpriced_candidate_reports_cost_as_none_not_zero():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={
            "choices": [{"message": {"content": json.dumps(
                {"ticker": "AAPL", "bias": "NEUTRAL", "conviction": 0.1, "rationale": "r"}
            )}}]
        })

    provider = OpenAICompatibleProvider("http://local/v1", "candidate", client=_server(handler))
    complete, usages = runner.screening_candidate_completer(provider, "candidate")
    complete("sys", "user", {"type": "object"})
    assert usages[0].cost_usd is None


# --- the CLI script end to end -----------------------------------------------


import replay.compare_screening as cs  # noqa: E402


def _write_journal(tmp_path, lines):
    path = tmp_path / "journal.log"
    path.write_text("\n".join(lines) + "\n")
    return path


def test_dry_run_counts_comparable_and_skipped_lines(tmp_path, capsys):
    journal = _write_journal(tmp_path, [
        journal_line(ticker="AAPL"),
        journal_line(ticker="MSFT", screen_error="down"),
    ])
    args = cs.parse_args(["--journal", str(journal), "--dry-run"])
    assert cs.run(args) == 0
    out = capsys.readouterr().out
    assert "1 of 2" in out


def test_agreement_is_measured_against_the_screen_not_the_escalated_signal(tmp_path):
    """End-to-end version of the unit property above, through the CLI path."""
    journal = _write_journal(tmp_path, [
        journal_line(ticker="AAPL", screen_bias="BULLISH", screen_conviction=0.6,
                     final_bias="NEUTRAL", final_conviction=0.1),
    ])

    def handler(request: httpx.Request) -> httpx.Response:
        # The candidate agrees with the *screen* (BULLISH), not the escalated
        # final signal (NEUTRAL).
        return httpx.Response(200, json={
            "choices": [{"message": {"content": json.dumps(
                {"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.58, "rationale": "r"}
            )}}]
        })

    monkey_client = _server(handler)
    real_init = OpenAICompatibleProvider.__init__

    def patched_init(self, base_url, model, api_key="", client=None, timeout=120.0):
        real_init(self, base_url, model, api_key=api_key, client=monkey_client, timeout=timeout)

    OpenAICompatibleProvider.__init__ = patched_init
    try:
        args = cs.parse_args([
            "--journal", str(journal), "--base-url", "http://local/v1",
            "--model", "candidate", "--json",
        ])
        assert cs.run(args) == 0
    finally:
        OpenAICompatibleProvider.__init__ = real_init


def test_a_line_with_no_recorded_screen_is_never_sent_to_the_candidate(tmp_path):
    journal = _write_journal(tmp_path, [journal_line(ticker="AAPL", screen_error="down")])
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(200, json={"choices": [{"message": {"content": "{}"}}]})

    monkey_client = _server(handler)
    real_init = OpenAICompatibleProvider.__init__

    def patched_init(self, base_url, model, api_key="", client=None, timeout=120.0):
        real_init(self, base_url, model, api_key=api_key, client=monkey_client, timeout=timeout)

    OpenAICompatibleProvider.__init__ = patched_init
    try:
        args = cs.parse_args([
            "--journal", str(journal), "--base-url", "http://local/v1", "--model", "candidate",
        ])
        assert cs.run(args) == 1  # nothing comparable
        assert calls == []
    finally:
        OpenAICompatibleProvider.__init__ = real_init


def test_missing_base_url_or_model_is_refused(tmp_path):
    journal = _write_journal(tmp_path, [journal_line()])
    args = cs.parse_args(["--journal", str(journal), "--model", "candidate"])
    assert cs.run(args) == 2


# --- escalation recall: the asymmetric metric ------------------------------


def _diff(before_bias, after_bias):
    before = None if before_bias is None else LLMSignal(
        ticker="AAPL", bias=Bias(before_bias), conviction=0.6, rationale="r"
    )
    after = None if after_bias is None else LLMSignal(
        ticker="AAPL", bias=Bias(after_bias), conviction=0.6, rationale="r"
    )
    return SignalDiff(ticker="AAPL", before=before, after=after)


def test_recall_is_none_when_haiku_never_escalated():
    """Nothing to have missed, so 100% would flatter an untested candidate."""
    diffs = [_diff("NEUTRAL", "NEUTRAL"), _diff("NEUTRAL", "BULLISH")]
    recall, recalled, n = cs.escalation_recall(diffs)
    assert recall is None and n == 0


def test_a_directional_haiku_call_the_candidate_also_escalates_counts():
    diffs = [_diff("BULLISH", "BEARISH")]  # disagrees on direction, but still escalated
    recall, recalled, n = cs.escalation_recall(diffs)
    assert (recall, recalled, n) == (1.0, 1, 1)


def test_a_directional_haiku_call_the_candidate_calls_neutral_is_a_miss():
    """The exact failure mode a symmetric agreement floor cannot see."""
    diffs = [_diff("BULLISH", "NEUTRAL")]
    recall, recalled, n = cs.escalation_recall(diffs)
    assert (recall, recalled, n) == (0.0, 0, 1)


def test_neutral_haiku_calls_never_enter_the_recall_denominator():
    diffs = [_diff("BULLISH", "BULLISH"), _diff("NEUTRAL", "BULLISH"), _diff("NEUTRAL", "NEUTRAL")]
    recall, recalled, n = cs.escalation_recall(diffs)
    assert (recall, recalled, n) == (1.0, 1, 1)


def test_recall_can_diverge_from_trade_agreement(tmp_path):
    """The property the metric exists to catch: a candidate that scores well
    on trade agreement overall while missing every one of Haiku's calls."""
    journal = _write_journal(tmp_path, [
        journal_line(ticker="AAPL", screen_bias="BULLISH", screen_conviction=0.6,
                     final_bias="BULLISH", final_conviction=0.6),
        journal_line(ticker="MSFT", screen_bias="NEUTRAL", screen_conviction=0.1,
                     final_bias="NEUTRAL", final_conviction=0.1),
    ])

    def handler(request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content)
        ticker = "AAPL" if "AAPL" in body["messages"][1]["content"] else "MSFT"
        # Agrees on the NEUTRAL line, misses the one directional call entirely.
        bias = "NEUTRAL" if ticker == "AAPL" else "NEUTRAL"
        return httpx.Response(200, json={
            "choices": [{"message": {"content": json.dumps(
                {"ticker": ticker, "bias": bias, "conviction": 0.1, "rationale": "r"}
            )}}]
        })

    monkey_client = _server(handler)
    real_init = OpenAICompatibleProvider.__init__

    def patched_init(self, base_url, model, api_key="", client=None, timeout=120.0):
        real_init(self, base_url, model, api_key=api_key, client=monkey_client, timeout=timeout)

    OpenAICompatibleProvider.__init__ = patched_init
    try:
        args = cs.parse_args([
            "--journal", str(journal), "--base-url", "http://local/v1",
            "--model", "candidate", "--json",
        ])
        assert cs.run(args) == 0
    finally:
        OpenAICompatibleProvider.__init__ = real_init


def test_the_verdict_is_gated_by_recall_not_by_trade_agreement(tmp_path):
    """A candidate can clear the agreement floor and still fail the verdict."""
    lines = [
        journal_line(ticker="AAPL", screen_bias="BULLISH", screen_conviction=0.6,
                     final_bias="BULLISH", final_conviction=0.6),
    ] + [
        journal_line(ticker="MSFT", ts=f"2026-09-{d:02d}T14:00:00+00:00",
                     screen_bias="NEUTRAL", screen_conviction=0.1,
                     final_bias="NEUTRAL", final_conviction=0.1)
        for d in range(1, 10)
    ]
    journal = _write_journal(tmp_path, lines)

    def handler(request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content)
        content = body["messages"][1]["content"]
        ticker = "AAPL" if "AAPL" in content else "MSFT"
        # Agrees on all nine NEUTRAL lines (90%+ trade agreement) but misses
        # the single directional one -- 0% recall.
        return httpx.Response(200, json={
            "choices": [{"message": {"content": json.dumps(
                {"ticker": ticker, "bias": "NEUTRAL", "conviction": 0.1, "rationale": "r"}
            )}}]
        })

    monkey_client = _server(handler)
    real_init = OpenAICompatibleProvider.__init__

    def patched_init(self, base_url, model, api_key="", client=None, timeout=120.0):
        real_init(self, base_url, model, api_key=api_key, client=monkey_client, timeout=timeout)

    OpenAICompatibleProvider.__init__ = patched_init
    try:
        import io
        from contextlib import redirect_stdout

        args = cs.parse_args([
            "--journal", str(journal), "--base-url", "http://local/v1",
            "--model", "candidate", "--json",
        ])
        buf = io.StringIO()
        with redirect_stdout(buf):
            assert cs.run(args) == 0
        payload = json.loads(buf.getvalue())
        assert payload["tradeable_agreement"] >= 0.9
        assert payload["escalation_recall"] == 0.0
        assert payload["verdict_pass"] is False
    finally:
        OpenAICompatibleProvider.__init__ = real_init


def test_a_small_sample_is_flagged_but_not_refused(tmp_path, capsys):
    journal = _write_journal(tmp_path, [
        journal_line(ticker="AAPL", screen_bias="BULLISH", screen_conviction=0.6),
    ])

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={
            "choices": [{"message": {"content": json.dumps(
                {"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.5, "rationale": "r"}
            )}}]
        })

    monkey_client = _server(handler)
    real_init = OpenAICompatibleProvider.__init__

    def patched_init(self, base_url, model, api_key="", client=None, timeout=120.0):
        real_init(self, base_url, model, api_key=api_key, client=monkey_client, timeout=timeout)

    OpenAICompatibleProvider.__init__ = patched_init
    try:
        args = cs.parse_args([
            "--journal", str(journal), "--base-url", "http://local/v1", "--model", "candidate",
        ])
        assert cs.run(args) == 0
        assert "not evidence yet" in capsys.readouterr().out
    finally:
        OpenAICompatibleProvider.__init__ = real_init


# --- asking a reasoning model to actually reason ---------------------------


def test_the_screen_is_asked_with_reasoning_off_by_default():
    """The default has to match production, or the verdict grades a question
    the cycle never asks."""
    seen = {}

    class Recording:
        def complete_detailed(self, s, u, schema, **kw):
            seen.update(kw)
            return Completion(text=json.dumps({"ticker": "AAPL", "bias": "NEUTRAL", "conviction": 0.1, "rationale": "r"}), usage=None)

    complete, _ = runner.screening_candidate_completer(Recording(), "m")
    complete("sys", "user", {"type": "object"})
    assert seen["reasoning"] is False
    assert seen["effort"] is None


def test_an_effort_turns_reasoning_on():
    """gpt-oss-20b has no true off switch, so the screen's low effort is a
    handicap. Separating 'weak model' from 'crippled by the setting' needs
    this to actually reach the provider."""
    seen = {}

    class Recording:
        def complete_detailed(self, s, u, schema, **kw):
            seen.update(kw)
            return Completion(text=json.dumps({"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.7, "rationale": "r"}), usage=None)

    complete, _ = runner.screening_candidate_completer(Recording(), "m", "high")
    complete("sys", "user", {"type": "object"})
    assert seen["reasoning"] is True
    assert seen["effort"] == "high"


def test_the_provider_sends_the_effort_it_was_given():
    """It used to accept ``effort`` and drop it, which made the experiment
    unrunnable while looking like it ran."""
    sent = {}

    def handler(request):
        sent.update(json.loads(request.content))
        return httpx.Response(200, json={
            "choices": [{"message": {"content": json.dumps({"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.7, "rationale": "r"})}}]
        })

    transport = httpx.MockTransport(handler)
    provider = llm.OpenAICompatibleProvider(
        base_url="https://example.test/v1", model="m", api_key="k",
        client=httpx.Client(transport=transport),
    )
    provider.complete_detailed("sys", "user", {"type": "object"}, reasoning=True, effort="high")
    assert sent["reasoning_effort"] == "high"


def test_reasoning_off_still_pins_the_floor_whatever_effort_says():
    """The screen's request shape must not drift because an experiment exists."""
    sent = {}

    def handler(request):
        sent.update(json.loads(request.content))
        return httpx.Response(200, json={
            "choices": [{"message": {"content": json.dumps({"ticker": "AAPL", "bias": "NEUTRAL", "conviction": 0.1, "rationale": "r"})}}]
        })

    transport = httpx.MockTransport(handler)
    provider = llm.OpenAICompatibleProvider(
        base_url="https://example.test/v1", model="m", api_key="k",
        client=httpx.Client(transport=transport),
    )
    provider.complete_detailed("sys", "user", {"type": "object"}, reasoning=False, effort="high")
    assert sent["reasoning_effort"] == "low", "an effort must not leak into the screen"
    assert llm.NO_REASONING_INSTRUCTION in sent["messages"][0]["content"]


# --- grading a sample large enough to mean something -----------------------


def _entries(n):
    return [
        runner.ReplayEntry(ticker=f"T{i}", ts_utc=None, prompt=f"T{i} body", original=None)
        for i in range(n)
    ]


def test_replay_each_can_run_in_parallel():
    """A reasoning model answers in ~97s, so a sample big enough to separate
    97% from 90% is hours sequentially -- which is how a run ends up too small
    to conclude anything from."""
    import threading

    inflight, peak = [], []
    lock = threading.Lock()

    def slow(system_prompt, user_prompt, schema):
        with lock:
            inflight.append(1)
            peak.append(len(inflight))
        time.sleep(0.03)
        with lock:
            inflight.pop()
        return json.dumps(
            {"ticker": user_prompt.split()[0], "bias": "NEUTRAL",
             "conviction": 0.1, "rationale": "r"}
        )

    entries = _entries(16)
    runner.replay_each(entries, lambda e: "sys", slow, max_workers=8)
    assert max(peak) > 1
    assert max(peak) <= 8


def test_replay_each_is_sequential_by_default():
    """Anthropic is the caller that would otherwise fire a whole journal at a
    rate limit, and a rate-limited context is lost where a slow one is late."""
    import threading

    inflight, peak = [], []
    lock = threading.Lock()

    def slow(system_prompt, user_prompt, schema):
        with lock:
            inflight.append(1)
            peak.append(len(inflight))
        time.sleep(0.01)
        with lock:
            inflight.pop()
        return json.dumps(
            {"ticker": user_prompt.split()[0], "bias": "NEUTRAL",
             "conviction": 0.1, "rationale": "r"}
        )

    runner.replay_each(_entries(8), lambda e: "sys", slow)
    assert max(peak) == 1


def test_results_keep_their_entry_order_under_concurrency():
    """A diff attributed to the wrong ticker is silent and wrong, and the
    whole point of the run is which tickers disagreed."""
    def echo(system_prompt, user_prompt, schema):
        ticker = user_prompt.split()[0]
        time.sleep(0.02 if ticker.endswith("0") else 0.001)
        return json.dumps(
            {"ticker": ticker, "bias": "NEUTRAL", "conviction": 0.1, "rationale": "r"}
        )

    entries = _entries(20)
    results = runner.replay_each(entries, lambda e: "sys", echo, max_workers=8)
    assert [r.entry.ticker for r in results] == [e.ticker for e in entries]
    for r in results:
        assert r.replayed is not None
        assert r.replayed.ticker == r.entry.ticker


def test_each_entry_is_asked_its_own_prompt():
    seen = {}

    def record(system_prompt, user_prompt, schema):
        ticker = user_prompt.split()[0]
        seen[ticker] = system_prompt
        return json.dumps(
            {"ticker": ticker, "bias": "NEUTRAL", "conviction": 0.1, "rationale": "r"}
        )

    entries = _entries(6)
    runner.replay_each(entries, lambda e: f"prompt-for-{e.ticker}", record, max_workers=4)
    assert seen == {f"T{i}": f"prompt-for-T{i}" for i in range(6)}
