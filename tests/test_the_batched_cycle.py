"""Both model stages asked offline, at half price, without losing a session.

The saving is easy; the safety is the part worth testing. Three properties:

* a batched answer and a live one are the same thing to everything downstream
  -- same journal line, same engine call, same stage in the report;
* anything the batch does not answer, for any reason, is asked live, so the
  worst case is the bill the cycle already pays today;
* the market-open gate is given up only by the run that is *meant* to start
  early, and never by accident.
"""

from __future__ import annotations

import json

import pytest

from config.settings import Settings
from orchestrator import heartbeat as hb
from orchestrator.llm import BatchTimeout, Completion, LLMError
from orchestrator.pricing import Usage


def _signal(ticker: str, bias: str = "BULLISH") -> str:
    return json.dumps(
        {"ticker": ticker, "bias": bias, "conviction": 0.8, "rationale": "r"}
    )


def _answer(ticker: str, bias: str = "BULLISH", model: str | None = None) -> Completion:
    return Completion(
        text=_signal(ticker, bias),
        usage=Usage(model=model or hb.MODEL, input_tokens=4000, output_tokens=500),
    )


def _ticker_of(user_prompt: str) -> str:
    return user_prompt.split("\n", 1)[0].removeprefix("TICKER:").strip()


class _Engine:
    """A dispatcher with an open book and no batch mode of its own."""

    def __init__(self, held=()):
        self._held = held
        self.dispatched: list[str] = []

    def is_market_open(self):
        return True

    def open_tickers(self):
        return frozenset(self._held)

    def manage_positions(self, protect_only: bool = False):
        return {"positions_seen": len(self._held)}

    def dispatch(self, signal):
        self.dispatched.append(signal.ticker)
        return {"status": "ACCEPTED", "reason": "ok"}


class _Batches:
    """An Anthropic provider whose batch behaviour each test chooses."""

    def __init__(self, answer=None, submit_error=None, timeout=False, drop=()):
        self.answer, self.submit_error = answer, submit_error
        self.timeout, self.drop = timeout, tuple(drop)
        self.submitted: list[list] = []

    def submit_batch(self, requests):
        if self.submit_error:
            raise self.submit_error
        self.submitted.append(list(requests))
        return "batch_test"

    def collect_batch(self, batch_id, model=None, timeout_seconds=None, **kw):
        if self.timeout:
            raise BatchTimeout(batch_id, "still in_progress")
        out = {}
        for request in self.submitted[-1]:
            ticker = _ticker_of(request.user_prompt)
            if ticker in self.drop:
                continue
            out[request.custom_id] = (
                self.answer(ticker, model) if self.answer else _answer(ticker, model=model)
            )
        return out

    def complete_detailed(self, *a, **kw):  # pragma: no cover - live path unused here
        raise AssertionError("the batch answered; no live call should happen")


@pytest.fixture
def batched(monkeypatch):
    """The batched cycle, with news faked and live calls counted."""
    live: dict[str, list[str]] = {"screen": [], "full": []}
    monkeypatch.setattr(hb.cfg, "USE_BATCH_API", True)
    # conftest turns the funnel off for every test by default; this file is
    # about both stages, so it opts back in.
    monkeypatch.setattr(hb, "SCREENING_ENABLED", True)
    monkeypatch.setattr(hb, "fetch_news", lambda t: ["news"])

    def screen(system_prompt, user_prompt, schema):
        ticker = _ticker_of(user_prompt)
        live["screen"].append(ticker)
        return _answer(ticker, model=hb.SCREENING_MODEL)

    def full(system_prompt, user_prompt, schema):
        ticker = _ticker_of(user_prompt)
        live["full"].append(ticker)
        return _answer(ticker)

    monkeypatch.setattr(hb, "screen_signal", screen)
    monkeypatch.setattr(hb, "call_llm", full)

    def use(*tickers, **settings):
        monkeypatch.setattr(
            hb, "get_settings",
            lambda: Settings(_env_file=None, watchlist=",".join(tickers), **settings),
        )

    return use, live


def _provider(monkeypatch, provider):
    monkeypatch.setattr(hb, "AnthropicSignalProvider", lambda *a, **kw: provider)
    monkeypatch.setattr(hb, "screening_provider", lambda: (provider, hb.SCREENING_MODEL))


# --- the saving ------------------------------------------------------------


def test_both_stages_are_asked_offline(batched, monkeypatch):
    use, live = batched
    use("AAPL", "MSFT")
    batches = _Batches()
    _provider(monkeypatch, batches)

    engine = _Engine()
    report = hb.run_cycle(engine)

    assert report.batched is True
    assert len(report.completed) == 2
    assert sorted(engine.dispatched) == ["AAPL", "MSFT"]
    # Two batches -- the screen, then what it escalated -- and no live call.
    assert len(batches.submitted) == 2
    assert live == {"screen": [], "full": []}


def test_the_screen_batch_asks_for_no_reasoning(batched, monkeypatch):
    """Haiku takes neither adaptive thinking nor effort; a batch built the
    other way is rejected whole."""
    use, _ = batched
    use("AAPL")
    batches = _Batches()
    _provider(monkeypatch, batches)
    hb.run_cycle(_Engine())

    screen_batch, full_batch = batches.submitted
    assert all(r.reasoning is False for r in screen_batch)
    assert all(r.reasoning is True for r in full_batch)


def test_a_neutral_screen_never_reaches_the_expensive_batch(batched, monkeypatch):
    use, _ = batched
    use("AAPL", "MSFT")
    batches = _Batches(answer=lambda t, m: _answer(t, "NEUTRAL", model=m))
    _provider(monkeypatch, batches)

    report = hb.run_cycle(_Engine())
    assert len(report.screened) == 2
    # Only the screen batch was ever submitted.
    assert len(batches.submitted) == 1


def test_a_held_ticker_is_in_neither_batch(batched, monkeypatch):
    use, _ = batched
    use("AAPL", "MSFT")
    batches = _Batches()
    _provider(monkeypatch, batches)

    report = hb.run_cycle(_Engine(held=("AAPL",)))
    assert [r.ticker for r in report.held] == ["AAPL"]
    assert [_ticker_of(r.user_prompt) for r in batches.submitted[0]] == ["MSFT"]


# --- the fallback ----------------------------------------------------------


def test_a_batch_that_times_out_is_paid_for_live(batched, monkeypatch):
    """The deadline is the safety property: a slow batch costs money, never a
    session."""
    use, live = batched
    use("AAPL", "MSFT")
    _provider(monkeypatch, _Batches(timeout=True))

    report = hb.run_cycle(_Engine())
    assert len(report.completed) == 2
    assert sorted(live["screen"]) == ["AAPL", "MSFT"]
    assert sorted(live["full"]) == ["AAPL", "MSFT"]


def test_a_batch_that_cannot_be_submitted_is_paid_for_live(batched, monkeypatch):
    use, live = batched
    use("AAPL")
    _provider(monkeypatch, _Batches(submit_error=LLMError("no credentials")))

    report = hb.run_cycle(_Engine())
    assert len(report.completed) == 1
    assert live["screen"] == ["AAPL"] and live["full"] == ["AAPL"]


def test_only_the_tickers_the_batch_missed_fall_back(batched, monkeypatch):
    """The saving is kept for everything the batch did answer."""
    use, live = batched
    use("AAPL", "MSFT", "NVDA")
    _provider(monkeypatch, _Batches(drop=("MSFT",)))

    report = hb.run_cycle(_Engine())
    assert len(report.completed) == 3
    assert live["screen"] == ["MSFT"]


def test_a_provider_with_no_batch_mode_is_simply_called(batched, monkeypatch):
    """The OpenAI-compatible provider has no offline mode, and needs none --
    its tokens are not billed in the first place."""
    use, live = batched
    use("AAPL")

    class _NoBatch:
        def complete_detailed(self, *a, **kw):  # pragma: no cover
            raise AssertionError("heartbeat should call screen_signal, not this")

    monkeypatch.setattr(hb, "screening_provider", lambda: (_NoBatch(), "local-model"))
    monkeypatch.setattr(hb, "AnthropicSignalProvider", lambda *a, **kw: _Batches())

    report = hb.run_cycle(_Engine())
    assert live["screen"] == ["AAPL"]
    assert len(report.completed) == 1


# --- the gate --------------------------------------------------------------


def test_a_closed_market_still_stops_an_ordinary_run(batched, monkeypatch):
    use, live = batched
    use("AAPL")

    class _Shut(_Engine):
        def is_market_open(self):
            return False

    report = hb.run_cycle(_Shut())
    assert report.market_closed is True
    assert report.results == ()
    assert live == {"screen": [], "full": []}


def test_premarket_is_what_gives_the_gate_up(batched, monkeypatch):
    """And it has to: the waiting happens before the session or during it."""
    use, _ = batched
    use("AAPL")
    batches = _Batches()
    _provider(monkeypatch, batches)

    class _Shut(_Engine):
        def is_market_open(self):
            return False

    report = hb.run_cycle(_Shut(), premarket=True)
    assert report.market_closed is False
    assert len(report.completed) == 1


def test_an_unreadable_clock_does_not_stop_the_batch(batched, monkeypatch):
    """Same as the live cycle: the engine fails closed on its own."""
    use, _ = batched
    use("AAPL")
    _provider(monkeypatch, _Batches())

    class _Broken(_Engine):
        def is_market_open(self):
            from app.broker_client import BrokerError

            raise BrokerError("clock unreachable")

    assert len(hb.run_cycle(_Broken()).completed) == 1
