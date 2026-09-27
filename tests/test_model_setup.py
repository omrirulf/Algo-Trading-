"""``model_setup``: who answered each cycle line, and with which prompt.

Added for the owner's weekly drift report (27 Sep 2026): the model's name
alone does not say who serves it, and a prompt edit leaves no trace in the
journal. Inside a cycle every line carries the model, the host and a
fingerprint of the prompt's fixed texts; outside one, a line is exactly the
line it always was.
"""

from __future__ import annotations

import json
import re

import pytest

from analysis.reader import entry_from
from orchestrator import heartbeat, journal, llm
from tests.test_journal_cycle_fields import (  # noqa: F401  (fixtures)
    KEYS_BEFORE, RUN, Reader, _lines, _own_keys, ctx, journal_path,
)

SETUP = {"model": "openai/gpt-oss-120b", "provider": "api.deepinfra.com", "prompt": "0123456789ab"}


def test_inside_a_cycle_the_setup_rides_after_the_price_and_before_the_run_block(journal_path, ctx, monkeypatch):
    monkeypatch.setenv("HEARTBEAT_RUN", json.dumps(RUN))
    with journal.cycle(lambda dispatcher: Reader(), setup=SETUP):
        journal.note_cycle({"market_closed": False}, "the dispatcher")
        journal.record(ctx, held=True)
    (line,) = _lines(journal_path)
    assert _own_keys(line) == KEYS_BEFORE + ["live", "management", "model_setup", "run"]
    assert line["model_setup"] == SETUP


def test_without_a_setup_or_outside_a_cycle_the_line_is_unchanged(journal_path, ctx, monkeypatch):
    monkeypatch.delenv("HEARTBEAT_RUN", raising=False)
    with journal.cycle(lambda d: None):
        journal.record(ctx, error="timed out")
    journal.record(ctx, error="timed out")
    for line in _lines(journal_path):
        assert _own_keys(line) == KEYS_BEFORE


def test_a_cycle_that_raised_leaves_no_setup_on_the_next_line(journal_path, ctx, monkeypatch):
    monkeypatch.delenv("HEARTBEAT_RUN", raising=False)
    with pytest.raises(RuntimeError):
        with journal.cycle(lambda d: None, setup=SETUP):
            raise RuntimeError("the cycle broke")
    journal.record(ctx, error="timed out")
    (line,) = _lines(journal_path)
    assert "model_setup" not in line


def test_the_setup_names_the_configured_model_and_host_and_never_a_key():
    setup = heartbeat.model_setup()
    assert setup["model"] == llm.MODEL
    assert setup["provider"] == "api.deepinfra.com"
    assert re.fullmatch(r"[0-9a-f]{12}", setup["prompt"])
    assert llm._hostname("https://user:secret@example.com/v1") == "example.com"


def test_with_no_base_url_the_setup_is_anthropic_s(monkeypatch):
    monkeypatch.setattr(llm, "MODEL_BASE_URL", "")
    assert llm.configured_model() == llm.ANTHROPIC_MODEL
    assert llm.configured_provider() == "api.anthropic.com"


def test_the_fingerprint_is_stable_and_moves_with_any_fixed_text(monkeypatch):
    first = heartbeat.prompt_fingerprint()
    assert heartbeat.prompt_fingerprint() == first
    monkeypatch.setattr(heartbeat, "SYSTEM_PROMPT", heartbeat.SYSTEM_PROMPT + " ")
    assert heartbeat.prompt_fingerprint() != first
    monkeypatch.undo()
    attr, text = heartbeat.ETF_SECTION_GUIDANCE[0]
    monkeypatch.setattr(heartbeat, "ETF_SECTION_GUIDANCE",
                        ((attr, text + "!"),) + heartbeat.ETF_SECTION_GUIDANCE[1:])
    assert heartbeat.prompt_fingerprint() != first
    monkeypatch.undo()
    monkeypatch.setattr(llm, "OFF_SCHEMA_INSTRUCTION", llm.OFF_SCHEMA_INSTRUCTION + ".")
    assert heartbeat.prompt_fingerprint() != first


def test_the_user_prompt_still_ends_as_it_always_did(ctx):
    assert heartbeat.build_user_prompt(ctx).endswith("\n\nRespond with the JSON signal for NVDA.")


def test_a_setup_that_cannot_be_described_costs_the_label_not_the_cycle(monkeypatch):
    def broken():
        raise ValueError("boom")

    monkeypatch.setattr(heartbeat, "prompt_fingerprint", broken)
    assert heartbeat.model_setup() is None


def test_the_cycle_is_opened_with_the_setup():
    source = (heartbeat.__file__ and open(heartbeat.__file__, encoding="utf-8").read())
    assert "with journal.cycle(prices, setup=model_setup()), model_io.capture(" in source


def test_the_reader_hands_the_setup_back_and_never_fails_over_it():
    entry = entry_from({"ticker": "NVDA", "ts_utc": "2026-09-28T15:00:00+00:00", "model_setup": SETUP})
    assert entry.model_setup == SETUP
    for junk in ("text", 3, None, ["a"]):
        entry = entry_from({"ticker": "NVDA", "ts_utc": "2026-09-28T15:00:00+00:00", "model_setup": junk})
        assert entry.model_setup is None
