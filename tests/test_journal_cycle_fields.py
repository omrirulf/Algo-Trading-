"""``live`` and ``management``: what a cycle adds to each of its journal lines.

The journal writes them only inside a cycle, and a line written without them
must be exactly the line written before they existed -- same keys, same order,
the run block still last. The reader hands them back and never fails over
them, and it hands back the engine's own reason for what it did.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime

import pytest

from analysis.reader import entry_from, read_lines
from app.position_manager import ManagementReport
from orchestrator import context, journal
from tests.test_context import HEADLINES, full_provider

#: Every key record() wrote before either field existed, in order.
KEYS_BEFORE = [
    "ts_utc", "ticker", "context", "signal", "outcome", "error", "usage", "fx",
    "screen", "blend", "arms", "held", "screening", "reasoning_effort", "stage",
]
FORMATTER_KEYS = {"ts", "level", "event", "taskName"}
RUN = {"trigger": "schedule", "minutes_late": 3, "late": False}
PRICE = {"price": 187.42, "bid": 187.4, "ask": 187.45, "quote_at": "2026-09-28T14:52:07+00:00",
         "asked_at": "2026-09-28T14:52:08+00:00", "source": "alpaca-iex"}

#: Captured before conftest swaps in a test logger: the key order under test
#: is the production formatter's.
_PRODUCTION_LOGGER = journal.get_journal_logger


@pytest.fixture
def ctx():
    return context.gather("NVDA", HEADLINES, provider=full_provider())


@pytest.fixture
def journal_path(tmp_path, monkeypatch):
    path = tmp_path / "production_journal.log"
    logger = logging.getLogger("signal_journal")
    saved = list(logger.handlers)
    for handler in saved:
        logger.removeHandler(handler)
    monkeypatch.setattr(journal, "get_journal_logger", lambda: _PRODUCTION_LOGGER(path))
    yield path
    for handler in list(logger.handlers):
        handler.close()
        logger.removeHandler(handler)
    for handler in saved:
        logger.addHandler(handler)


def _lines(path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _own_keys(payload: dict) -> list[str]:
    return [key for key in payload if key not in FORMATTER_KEYS]


class Reader:
    """A price reader that answers from a table and remembers who it was asked about."""

    def __init__(self, answer=None, exc=None):
        self.answer, self.exc = answer or PRICE, exc
        self.asked: list[str] = []
        self.closed = 0

    def read(self, ticker):
        self.asked.append(ticker)
        if self.exc:
            raise self.exc
        return dict(self.answer, asked_at=datetime.now().astimezone().isoformat())

    def close(self):
        self.closed += 1


# --------------------------------------------------------------------------- #
# Outside a cycle, nothing changes
# --------------------------------------------------------------------------- #


def test_outside_a_cycle_a_line_has_exactly_the_keys_it_always_had(journal_path, ctx, monkeypatch):
    monkeypatch.delenv("HEARTBEAT_RUN", raising=False)
    journal.note_cycle({"market_closed": True}, object())  # ignored: no cycle is open
    journal.record(ctx, error="timed out")
    monkeypatch.setenv("HEARTBEAT_RUN", json.dumps(RUN))
    journal.record(ctx, error="timed out")
    plain, with_run = _lines(journal_path)
    assert _own_keys(plain) == KEYS_BEFORE
    assert _own_keys(with_run) == KEYS_BEFORE + ["run"]
    assert journal.read_live("NVDA") is None


def test_a_cycle_that_learned_nothing_writes_the_old_line(journal_path, ctx, monkeypatch):
    """A dispatcher with no manager and no reader: nothing to add, so nothing added."""
    monkeypatch.delenv("HEARTBEAT_RUN", raising=False)
    with journal.cycle(lambda d: None):
        journal.note_cycle(None, object())
        journal.record(ctx, error="timed out")
    (line,) = _lines(journal_path)
    assert _own_keys(line) == KEYS_BEFORE


# --------------------------------------------------------------------------- #
# Inside a cycle
# --------------------------------------------------------------------------- #


def test_inside_a_cycle_both_ride_on_the_line_before_the_run_block(journal_path, ctx, monkeypatch):
    monkeypatch.setenv("HEARTBEAT_RUN", json.dumps(RUN))
    reader = Reader()
    with journal.cycle(lambda dispatcher: reader):
        journal.note_cycle({"positions_seen": 3, "market_closed": False}, "the dispatcher")
        journal.record(ctx, held=True)
    (line,) = _lines(journal_path)
    assert _own_keys(line) == KEYS_BEFORE + ["live", "management", "run"]
    assert line["live"]["price"] == 187.42 and line["live"]["source"] == "alpaca-iex"
    assert line["management"] == {"market_closed": False}
    assert line["run"] == RUN
    assert reader.asked == ["NVDA"]


def test_the_reader_is_built_for_the_dispatcher_the_cycle_trades_through():
    seen = []
    with journal.cycle(lambda dispatcher: seen.append(dispatcher) or Reader()):
        journal.note_cycle({}, "the dispatcher")
        journal.note_cycle({}, "a second note builds nothing new")
    assert seen == ["the dispatcher"]


def test_the_line_time_is_taken_before_the_price_is_read(journal_path, ctx):
    """The line's own time decides which day it belongs to in the race and the
    funds; a slow price read must not be able to move it."""
    with journal.cycle(lambda d: Reader()):
        journal.note_cycle({"market_closed": False})
        journal.record(ctx, error="x")
    (line,) = _lines(journal_path)
    assert datetime.fromisoformat(line["ts_utc"]) <= datetime.fromisoformat(line["live"]["asked_at"])


def test_a_price_read_at_the_moment_of_the_signal_is_used_as_given(journal_path, ctx):
    reader = Reader()
    earlier = dict(PRICE, asked_at="2026-09-28T14:00:00+00:00")
    with journal.cycle(lambda d: reader):
        journal.note_cycle({"market_closed": False})
        journal.record(ctx, outcome={"status": "ACCEPTED"}, live=earlier)
    (line,) = _lines(journal_path)
    assert line["live"] == earlier
    assert reader.asked == [], "not read a second time at write time"


@pytest.mark.parametrize("positions, expected", [
    ({"market_closed": True}, {"market_closed": True}),
    ({"positions_seen": 4, "market_closed": False, "errors": 1}, {"market_closed": False}),
    (ManagementReport(market_closed=True).as_dict(), {"market_closed": True}),
    (ManagementReport().as_dict(), {"market_closed": False}),
    ({"error": "RuntimeError: broker down"}, None),
    ({"error": "HTTP 500", "body": "..."}, None),
    ({"positions_seen": 2}, None),
    ({"market_closed": "yes"}, None),
    ({"market_closed": 1}, None),
    (None, None),
    ("closed", None),
])
def test_management_is_what_the_pass_reported_and_absent_when_it_reported_nothing(
        journal_path, ctx, positions, expected):
    with journal.cycle():
        journal.note_cycle(positions)
        journal.record(ctx, held=True)
    (line,) = _lines(journal_path)
    assert line.get("management") == expected
    assert ("management" in line) == (expected is not None)
    assert "live" not in line, "no reader, no price"


# --------------------------------------------------------------------------- #
# A failure here is never a lost line
# --------------------------------------------------------------------------- #


def test_a_reader_that_raises_costs_the_price_not_the_line(journal_path, ctx):
    with journal.cycle(lambda d: Reader(exc=RuntimeError("boom"))):
        journal.note_cycle({"market_closed": False})
        journal.record(ctx, error="x")
        assert journal.read_live("NVDA") is None
    (line,) = _lines(journal_path)
    assert "live" not in line and line["management"] == {"market_closed": False}


def test_a_reader_that_cannot_be_built_costs_the_prices_not_the_lines(journal_path, ctx):
    def broken(dispatcher):
        raise RuntimeError("no reader today")

    with journal.cycle(broken):
        journal.note_cycle({"market_closed": True})
        journal.record(ctx, error="x")
    (line,) = _lines(journal_path)
    assert "live" not in line and line["management"] == {"market_closed": True}


@pytest.mark.parametrize("junk", ["text", 3, None, ["a"]])
def test_a_reader_that_returns_junk_is_no_price(junk):
    class Junk:
        def read(self, ticker):
            return junk

    with journal.cycle(lambda d: Junk()):
        journal.note_cycle({})
        assert journal.read_live("NVDA") is None


def test_the_cycle_is_closed_and_the_reader_let_go_even_when_the_cycle_raises(journal_path, ctx):
    reader = Reader()
    with pytest.raises(RuntimeError):
        with journal.cycle(lambda d: reader):
            journal.note_cycle({"market_closed": True})
            raise RuntimeError("the cycle died")
    assert reader.closed == 1
    journal.record(ctx, error="written after the cycle died")
    (line,) = _lines(journal_path)
    assert _own_keys(line)[: len(KEYS_BEFORE)] == KEYS_BEFORE
    assert "live" not in line and "management" not in line, "one cycle's facts on another's line"


def test_a_reader_that_will_not_close_does_not_raise():
    class Stubborn(Reader):
        def close(self):
            raise OSError("socket")

    with journal.cycle(lambda d: Stubborn()):
        journal.note_cycle({})


# --------------------------------------------------------------------------- #
# The reader hands them back
# --------------------------------------------------------------------------- #


def _payload(**extra) -> dict:
    return {"ticker": "NVDA", "ts_utc": "2026-09-28T15:20:00+00:00",
            "signal": {"bias": "BULLISH", "conviction": 0.7}, **extra}


def test_the_reader_returns_all_three():
    entry = entry_from(_payload(
        live=PRICE, management={"market_closed": True},
        outcome={"status": "REJECTED", "reason": "  market is closed "},
    ))
    assert entry.live == PRICE
    assert entry.management_market_closed is True
    assert entry.outcome_reason == "market is closed"


def test_a_line_from_before_them_has_none_of_them():
    entry = entry_from(_payload())
    assert entry.live is None
    assert entry.management_market_closed is None
    assert entry.outcome_reason is None


def test_a_failed_price_read_is_returned_as_written():
    failed = {"price": None, "bid": None, "ask": None, "quote_at": None,
              "asked_at": "2026-09-28T14:52:08+00:00", "source": "yfinance", "error": "timed out"}
    assert entry_from(_payload(live=failed)).live == failed


@pytest.mark.parametrize("junk", [None, "187.42", 187.42, True, [], ["price"]])
def test_a_live_record_that_is_not_an_object_is_none_and_never_an_error(junk):
    entry = entry_from(_payload(live=junk))
    assert entry is not None and entry.live is None
    assert entry.ticker == "NVDA" and entry.bias == "BULLISH"


@pytest.mark.parametrize("junk", [None, True, "closed", [], {}, {"market_closed": "true"},
                                  {"market_closed": 1}, {"market_closed": None}])
def test_management_that_is_not_a_true_false_value_is_none(junk):
    assert entry_from(_payload(management=junk)).management_market_closed is None


@pytest.mark.parametrize("outcome", [None, "market is closed", [], {}, {"reason": None},
                                     {"reason": ""}, {"reason": "   "}, {"reason": 7},
                                     {"reason": ["market is closed"]}])
def test_an_outcome_with_no_reason_text_is_none(outcome):
    entry = entry_from(_payload(outcome=outcome))
    assert entry is not None and entry.outcome_reason is None


def test_read_lines_carries_them_through():
    lines = [json.dumps(_payload(live=PRICE, management={"market_closed": False},
                                 outcome={"status": "REJECTED", "reason": "bias is NEUTRAL; no trade"})),
             json.dumps(_payload(live="junk", management="junk", outcome="junk"))]
    first, second = read_lines(lines).entries
    assert (first.live, first.management_market_closed, first.outcome_reason) == (
        PRICE, False, "bias is NEUTRAL; no trade")
    assert (second.live, second.management_market_closed, second.outcome_reason) == (None, None, None)


def test_the_properties_are_safe_to_read_through_getattr_on_any_entry():
    """How the calibration reads them, so it works on either side of this change."""
    entry = entry_from(_payload())
    for name in ("live", "management_market_closed", "outcome_reason"):
        assert getattr(entry, name, None) is None
