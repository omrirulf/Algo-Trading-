"""Stage zero of the funnel: a name already in the book is asked nothing.

The property under test is the mirror of the screen's. The screen may only
ever *save* a call; this stage may only ever save a call **on a ticker the
book already holds**. Everything else about the cycle -- what the other
tickers are asked, what the ladder does to the open book, what the journal
records -- has to be indistinguishable from a cycle without it.

The one direction that must never invert: when the book cannot be read, the
whole watchlist is reviewed. Skipping a ticker nobody holds is a missed trade,
and a missed trade is worth more than the call it saved.
"""

from __future__ import annotations

import json

import pytest

from orchestrator import heartbeat as hb
from orchestrator.llm import Completion, LLMError
from orchestrator.pricing import Usage


def _signal(ticker: str = "AAPL", bias: str = "BULLISH") -> dict:
    return {"ticker": ticker, "bias": bias, "conviction": 0.8, "rationale": "r"}


@pytest.fixture
def cycle(monkeypatch):
    """Both model stages faked and counted, so a skipped call is visible."""
    calls: dict[str, list] = {"screen": [], "full": [], "posted": []}
    monkeypatch.setattr(hb.cfg, "SKIP_HELD_TICKERS", True)
    monkeypatch.setattr(hb, "SCREENING_ENABLED", True)
    monkeypatch.setattr(hb, "fetch_news", lambda t: ["news"])

    # Which ticker is in flight, so a faked answer is for the ticker that was
    # asked: an answer for another one is dropped, which would read as a skip.
    asked = {"ticker": ""}
    build_context = hb.build_context

    def tracked(ticker: str):
        asked["ticker"] = ticker
        return build_context(ticker)

    monkeypatch.setattr(hb, "build_context", tracked)

    def screen(system_prompt, user_prompt, schema):
        calls["screen"].append(asked["ticker"])
        return Completion(
            text=json.dumps(_signal(asked["ticker"])),
            usage=Usage(model=hb.SCREENING_MODEL, input_tokens=4000, output_tokens=500),
        )

    def full(system_prompt, user_prompt, schema):
        calls["full"].append(asked["ticker"])
        return Completion(
            text=json.dumps(_signal(asked["ticker"])),
            usage=Usage(model=hb.MODEL, input_tokens=4000, output_tokens=500),
        )

    monkeypatch.setattr(hb, "screen_signal", screen)
    monkeypatch.setattr(hb, "call_llm", full)
    monkeypatch.setattr(
        hb, "post_signal",
        lambda s, dispatcher=None: (calls["posted"].append(s), {"status": "ACCEPTED", "reason": "ok"})[1],
    )
    return calls


def _journal_entry(path) -> dict:
    lines = path.read_text().splitlines()
    assert len(lines) == 1, lines
    return json.loads(lines[0])


# --- the saving ------------------------------------------------------------


def test_a_held_ticker_asks_neither_model(cycle):
    result = hb.process_ticker("AAPL", held=frozenset({"AAPL"}))
    assert result.stage == hb.HELD
    assert cycle["screen"] == []
    assert cycle["full"] == []
    assert cycle["posted"] == []


def test_an_unheld_ticker_is_reviewed_exactly_as_before(cycle):
    result = hb.process_ticker("AAPL", held=frozenset({"MSFT"}))
    assert result.stage == hb.COMPLETED
    assert len(cycle["screen"]) == 1
    assert len(cycle["full"]) == 1
    assert len(cycle["posted"]) == 1


def test_a_ticker_run_on_its_own_is_reviewed_whether_or_not_it_is_held(cycle):
    """The default is empty, so a single-ticker run never silently skips."""
    assert hb.process_ticker("AAPL").stage == hb.COMPLETED
    assert len(cycle["full"]) == 1


def test_the_skip_can_be_turned_off(cycle, monkeypatch):
    monkeypatch.setattr(hb.cfg, "SKIP_HELD_TICKERS", False)
    result = hb.process_ticker("AAPL", held=frozenset({"AAPL"}))
    assert result.stage == hb.COMPLETED
    assert len(cycle["full"]) == 1


# --- what the record keeps -------------------------------------------------


def test_a_held_ticker_is_journalled_with_its_context_and_no_signal(cycle, _journal_to_tmp):
    hb.process_ticker("AAPL", held=frozenset({"AAPL"}))
    entry = _journal_entry(_journal_to_tmp)
    assert entry["held"] is True
    assert entry["signal"] is None
    assert entry["usage"] is None
    assert entry["error"] is None
    # The day is not a hole in the record: what was in front of the model that
    # was never asked is still what a replay would need to price the skip.
    assert entry["context"]["ticker"] == "AAPL"


def test_a_reviewed_ticker_is_journalled_as_not_held(cycle, _journal_to_tmp):
    hb.process_ticker("AAPL", held=frozenset())
    assert _journal_entry(_journal_to_tmp)["held"] is False


# --- reading the book ------------------------------------------------------


class _Book:
    """A dispatcher that knows what it holds."""

    def __init__(self, tickers=(), error: Exception | None = None):
        self._tickers, self._error = tickers, error

    def open_tickers(self):
        if self._error:
            raise self._error
        return frozenset(self._tickers)

    def is_market_open(self):
        return True

    def manage_positions(self, protect_only: bool = False):
        return {"positions_seen": len(self._tickers)}

    def dispatch(self, signal):
        return {"status": "ACCEPTED", "reason": "ok"}


def test_the_book_is_read_once_and_its_names_are_skipped(cycle, monkeypatch):
    monkeypatch.setattr(hb, "get_settings", lambda: type("S", (), {"watchlist_tickers": ("AAPL", "MSFT", "NVDA")})())
    report = hb.run_cycle(_Book(("AAPL", "NVDA")))
    assert {r.ticker for r in report.held} == {"AAPL", "NVDA"}
    assert [r.ticker for r in report.completed] == ["MSFT"]
    assert len(cycle["full"]) == 1


def test_an_unreadable_book_reviews_everything(cycle, monkeypatch):
    """The safe direction: pay for the cycle rather than skip a candidate."""
    monkeypatch.setattr(hb, "get_settings", lambda: type("S", (), {"watchlist_tickers": ("AAPL", "MSFT")})())
    report = hb.run_cycle(_Book(("AAPL",), error=RuntimeError("broker down")))
    assert report.held == ()
    assert len(report.completed) == 2


def test_a_dispatcher_that_cannot_read_a_book_reviews_everything(cycle, monkeypatch):
    """Webhook mode holds no broker credentials, so it has no book to read."""

    class _NoBook(_Book):
        open_tickers = None

    monkeypatch.setattr(hb, "get_settings", lambda: type("S", (), {"watchlist_tickers": ("AAPL",)})())
    report = hb.run_cycle(_NoBook())
    assert report.held == ()
    assert len(report.completed) == 1


def test_the_book_is_read_after_the_ladder_has_run(monkeypatch):
    """A position the ladder just closed is a candidate again today."""
    order: list[str] = []

    class _Ordered(_Book):
        def manage_positions(self, protect_only: bool = False):
            order.append("ladder")
            return {}

        def open_tickers(self):
            order.append("book")
            return frozenset()

    monkeypatch.setattr(hb, "get_settings", lambda: type("S", (), {"watchlist_tickers": ()})())
    hb.run_cycle(_Ordered())
    assert order == ["ladder", "book"]


# --- the report ------------------------------------------------------------


def test_held_is_not_a_failure_stage():
    assert hb.HELD not in hb.FAILURE_STAGES
    assert hb.HELD in hb.STAGE_LABELS


def test_a_cycle_that_held_everything_is_not_a_cycle_that_produced_nothing():
    """A full book is a state, not an outage -- and the ladder still ran."""
    report = hb.CycleReport(
        tickers=("AAPL", "MSFT"),
        results=(
            hb.TickerResult("AAPL", hb.HELD),
            hb.TickerResult("MSFT", hb.HELD),
        ),
    )
    assert not report.produced_nothing
    assert len(report.held) == 2


def test_the_summary_says_how_many_were_held():
    report = hb.CycleReport(
        tickers=("AAPL", "MSFT"),
        results=(
            hb.TickerResult("AAPL", hb.HELD),
            hb.TickerResult("MSFT", hb.COMPLETED, status="ACCEPTED"),
        ),
    )
    text = hb.render_summary(report)
    assert "**1 of 2** already held" in text
    # Not counted among the things that went wrong.
    assert "Stopped at" not in text
    assert "Nothing reached the engine" not in text


# --- the stage below it ----------------------------------------------------


def test_a_screen_failure_still_escalates_for_an_unheld_ticker(cycle, monkeypatch):
    """Stage zero must not change how the stage below it fails."""

    def broken(system_prompt, user_prompt, schema):
        raise LLMError("screen down")

    monkeypatch.setattr(hb, "screen_signal", broken)
    result = hb.process_ticker("AAPL", held=frozenset({"MSFT"}))
    assert result.stage == hb.COMPLETED
    assert len(cycle["full"]) == 1
