"""The run block: what started a cycle run, riding on every journal line.

Three places touch it and each has one job. The journal writes it only when
the workflow described the run, and a line without it must be exactly the
line written before it existed. The reader hands it back and never fails over
it. The report says it in one sentence and never fails over it either.
"""

from __future__ import annotations

import json
import re

import pytest

from analysis import cycle_report as cr
from analysis.reader import entry_from, read_lines
from orchestrator import context, journal
from tests.test_context import HEADLINES, full_provider

BLOCK = {
    "trigger": "backup",
    "scheduled_for": "2026-09-28T14:40:00+00:00",
    "started_at": "2026-09-28T15:12:00+00:00",
    "minutes_late": 32,
    "late": True,
    "run_id": "17234567890",
}

#: Every key record() wrote before the run block existed, in order.
KEYS_BEFORE_THE_BLOCK = [
    "ts_utc", "ticker", "context", "signal", "outcome", "error", "usage", "fx",
    "screen", "blend", "arms", "held", "screening", "reasoning_effort", "stage",
]

#: The formatter's own keys. Where it puts them, and whether it adds
#: ``taskName`` (Python 3.12 does, 3.11 does not), is the logging library's
#: business and the same with or without the block.
FORMATTER_KEYS = {"ts", "level", "event", "taskName"}


def _own_keys(payload: dict) -> list[str]:
    assert {"ts", "level", "event"} <= set(payload)
    return [key for key in payload if key not in FORMATTER_KEYS]


#: The production logger factory, captured at import -- before the autouse
#: fixture in conftest swaps in a test logger whose formatter keeps the
#: stdlib's own key names. The key order under test is production's.
_PRODUCTION_LOGGER = journal.get_journal_logger


@pytest.fixture
def ctx():
    return context.gather("NVDA", HEADLINES, provider=full_provider())


@pytest.fixture
def journal_path(tmp_path, monkeypatch):
    """The real journal formatter, writing to a temporary file."""
    import logging

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


def _written(path) -> list[str]:
    return [line for line in path.read_text().splitlines() if line.strip()]


# --------------------------------------------------------------------------- #
# the journal writes it
# --------------------------------------------------------------------------- #

def test_a_described_run_puts_the_block_on_the_line(journal_path, ctx, monkeypatch):
    monkeypatch.setenv("HEARTBEAT_RUN", json.dumps(BLOCK))
    journal.record(ctx, error="timed out")
    (line,) = _written(journal_path)
    payload = json.loads(line)
    assert payload["run"] == BLOCK
    assert _own_keys(payload) == KEYS_BEFORE_THE_BLOCK + ["run"], "the block goes last"


def test_without_the_variable_a_line_has_exactly_the_keys_it_always_had(journal_path, ctx, monkeypatch):
    monkeypatch.delenv("HEARTBEAT_RUN", raising=False)
    journal.record(ctx, error="timed out")
    (line,) = _written(journal_path)
    assert _own_keys(json.loads(line)) == KEYS_BEFORE_THE_BLOCK
    assert '"run"' not in line


@pytest.mark.parametrize("junk", ["", "   ", "not json", "{broken", "[1, 2]", "42", '"text"', "null",
                                  pytest.param("[" * 100_000, id="nested-past-the-recursion-limit")])
def test_junk_in_the_variable_is_no_block_and_no_error(journal_path, ctx, monkeypatch, junk):
    """Byte for byte the line an unset variable writes, timestamps aside."""
    monkeypatch.delenv("HEARTBEAT_RUN", raising=False)
    journal.record(ctx, error="timed out")
    monkeypatch.setenv("HEARTBEAT_RUN", junk)
    journal.record(ctx, error="timed out")
    clean, junked = _written(journal_path)

    def without_time(line: str) -> str:
        return re.sub(r'"(ts|ts_utc)": "[^"]*"', r'"\1": "-"', line)

    assert without_time(junked) == without_time(clean)


def test_the_block_is_read_when_the_line_is_written(monkeypatch):
    """Not cached at import: one process, two runs, two blocks."""
    monkeypatch.setenv("HEARTBEAT_RUN", json.dumps({"trigger": "schedule"}))
    assert journal.run_block() == {"trigger": "schedule"}
    monkeypatch.setenv("HEARTBEAT_RUN", json.dumps({"trigger": "manual"}))
    assert journal.run_block() == {"trigger": "manual"}
    monkeypatch.delenv("HEARTBEAT_RUN")
    assert journal.run_block() is None


# --------------------------------------------------------------------------- #
# the reader hands it back
# --------------------------------------------------------------------------- #

def _payload(**extra) -> dict:
    return {"ticker": "NVDA", "ts_utc": "2026-09-28T15:20:00+00:00",
            "signal": {"bias": "NEUTRAL", "conviction": 0.1}, **extra}


def test_the_reader_returns_the_block():
    entry = entry_from(_payload(run=BLOCK))
    assert entry.run == BLOCK


def test_a_line_from_before_the_block_has_none():
    assert entry_from(_payload()).run is None


@pytest.mark.parametrize("junk", [None, "backup", 32, 1.5, True, ["schedule"], []])
def test_anything_that_is_not_an_object_is_none_and_never_an_error(junk):
    entry = entry_from(_payload(run=junk))
    assert entry is not None, "the line itself is still read"
    assert entry.run is None
    assert entry.ticker == "NVDA" and entry.bias == "NEUTRAL"


def test_a_block_with_odd_values_inside_is_returned_as_written():
    """The reader does not judge the keys; a caller checks what it uses."""
    odd = {"trigger": 7, "minutes_late": "lots", "late": None}
    assert entry_from(_payload(run=odd)).run == odd


def test_read_lines_carries_the_block_through():
    lines = [json.dumps(_payload(run=BLOCK)), json.dumps(_payload(run="junk"))]
    first, second = read_lines(lines).entries
    assert first.run == BLOCK and second.run is None


# --------------------------------------------------------------------------- #
# the report says it
# --------------------------------------------------------------------------- #

def _report_line(**extra) -> cr.Line:
    return cr.Line(_payload(**extra))


def test_the_report_says_who_started_the_run_and_how_late():
    text = cr.render([_report_line(run=BLOCK)])
    assert ("**Run:** started by the backup, because GitHub's schedule had not started it, "
            "32 minutes after the planned 14:40 UTC — late.") in text


def test_an_on_time_run_says_so():
    block = dict(BLOCK, trigger="schedule", minutes_late=-2, late=False)
    assert cr.run_line([_report_line(run=block)]) == (
        "**Run:** started by GitHub's schedule, on time (planned for 14:40 UTC).")


def test_a_manual_run_a_few_minutes_late_is_not_called_late():
    """``manual`` is any dispatch that did not say it was the backup. Every
    cycle since 21 Sep was dispatched by a Claude Routine, so the words must
    not claim a person started it."""
    block = dict(BLOCK, trigger="manual", minutes_late=12, late=False)
    line = cr.run_line([_report_line(run=block)])
    assert line == ("**Run:** started by a manual dispatch (a person or a Claude Routine), "
                    "12 minutes after the planned 14:40 UTC.")
    assert "by hand" not in line


def test_a_report_of_old_lines_has_no_run_sentence():
    text = cr.render([_report_line()])
    assert "**Run:**" not in text
    assert cr.run_line([_report_line()]) is None


@pytest.mark.parametrize("junk", [
    "backup", 5, [], {}, {"trigger": "backup"}, {"minutes_late": "x", "scheduled_for": 3},
    {"trigger": None, "minutes_late": True, "scheduled_for": "not a time"},
])
def test_junk_in_the_block_never_breaks_the_report(junk):
    text = cr.render([_report_line(run=junk)])
    assert text.startswith("# Daily report")
