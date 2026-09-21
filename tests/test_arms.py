"""The rule arms are on every journal line, in shadow, and cannot trade.

Three things have to hold for the race in analysis/horse_race.py to mean
anything. The arms must be on every line -- screened, held, failed -- or
the model gets to choose the battlefield. An arm that fails must cost its
own field and nothing else, or a bug in a control could lose the line the
model's real answer is on. And nothing an arm says may reach the engine,
which CI pins and this suite mirrors so the property is stated where the
code is, not only where it is enforced.
"""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

import pytest

from app.schemas import Bias, LLMSignal
from orchestrator import arms, context, journal
from rules import control, momentum
from tests.test_context import HEADLINES, full_provider

ROOT = Path(__file__).resolve().parents[1]

SIGNAL = LLMSignal(ticker="NVDA", bias=Bias.BEARISH, conviction=0.4, rationale="the model's view")


def read_lines(path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


@pytest.fixture
def ctx():
    # 300 bars of a steady climb: a quarter up, price above its 50-day.
    return context.gather("NVDA", HEADLINES, provider=full_provider())


# --- on every line ------------------------------------------------------------


def test_a_full_model_line_carries_both_arms(_journal_to_tmp, ctx):
    journal.record(ctx, SIGNAL, outcome={"status": "ACCEPTED"})
    (line,) = read_lines(_journal_to_tmp)
    assert set(line["arms"]) == {momentum.NAME, control.NAME}
    # The model said BEARISH; the momentum arm, reading the same climb, did
    # not. That disagreement is the whole point of recording both.
    assert line["signal"]["bias"] == "BEARISH"
    assert line["arms"][momentum.NAME]["bias"] == "BULLISH"
    assert line["arms"][momentum.NAME]["conviction"] == 1.0
    assert line["arms"][control.NAME]["bias"] in ("BULLISH", "BEARISH")


def test_a_held_line_carries_the_arms_too(_journal_to_tmp, ctx):
    """No model was asked. The rule still had an opinion, and it is written
    down so the race can decide -- separately -- whether to count it."""
    journal.record(ctx, held=True)
    (line,) = read_lines(_journal_to_tmp)
    assert line["signal"] is None and line["held"] is True
    assert line["arms"][momentum.NAME]["bias"] == "BULLISH"


def test_a_failed_line_carries_the_arms_too(_journal_to_tmp, ctx):
    journal.record(ctx, error="model timed out")
    (line,) = read_lines(_journal_to_tmp)
    assert line["error"] == "model timed out"
    assert momentum.NAME in line["arms"]


def test_a_line_with_no_technicals_says_so_rather_than_guessing(_journal_to_tmp):
    bare = context.TickerContext(ticker="NEW")
    journal.record(bare, error="no history")
    (line,) = read_lines(_journal_to_tmp)
    assert line["arms"][momentum.NAME]["bias"] == "NEUTRAL"
    assert "no technicals" in line["arms"][momentum.NAME]["rationale"]
    # The control needs no technicals and still takes a side.
    assert line["arms"][control.NAME]["bias"] in ("BULLISH", "BEARISH")


# --- the control is recomputable from the line itself --------------------------


def test_the_journalled_coin_flip_is_the_one_the_line_seeds(_journal_to_tmp, ctx):
    """The harness must land on the identical flip from the line's own
    timestamp, or the control is a fresh draw every run."""
    journal.record(ctx, SIGNAL)
    (line,) = read_lines(_journal_to_tmp)
    day = datetime.fromisoformat(line["ts_utc"]).date()
    assert line["arms"][control.NAME]["bias"] == control.signal_for("NVDA", day).bias.value


# --- failure is a labelled field, never a lost line ---------------------------


def test_an_arm_that_raises_costs_only_its_own_field(_journal_to_tmp, ctx, monkeypatch, caplog):
    def kaboom(ticker, technicals, day):
        raise RuntimeError("kaboom")

    monkeypatch.setitem(arms.ARMS, "broken", kaboom)
    journal.record(ctx, SIGNAL, outcome={"status": "ACCEPTED"})
    (line,) = read_lines(_journal_to_tmp)
    assert line["arms"]["broken"] == {"error": "RuntimeError: kaboom"}
    assert line["arms"][momentum.NAME]["bias"] == "BULLISH"  # the others survived
    assert line["signal"]["bias"] == "BEARISH"                # and so did the line
    assert "broken arm failed" in caplog.text


# --- shadow only: the suite-side mirror of the CI guardrail --------------------


def test_rules_cannot_trade_write_or_read_a_credential():
    forbidden = re.compile(
        r"(submit_order|submit_bracket_order|ExecutionEngine|post_signal|AlpacaPaperBroker"
        r"|\.write_text\(|open\([^)]*[\"'][wa]|get_settings|os\.environ|getenv|api_key|secret)"
    )
    offenders = [
        p.name for p in (ROOT / "rules").rglob("*.py")
        if forbidden.search(p.read_text(encoding="utf-8"))
    ]
    assert not offenders, f"rules/ must stay inert: {offenders}"


def test_the_arms_output_is_read_only_where_it_is_computed_and_journalled():
    readers = [
        p.name for p in (ROOT / "orchestrator").rglob("*.py")
        if "arms_record" in p.read_text(encoding="utf-8") and p.name not in ("arms.py", "journal.py")
    ]
    assert not readers, f"arms_record is read outside arms.py/journal.py: {readers}"


def test_no_arm_is_ever_handed_to_post_signal():
    text = (ROOT / "orchestrator/heartbeat.py").read_text(encoding="utf-8")
    assert not re.search(r"post_signal\([^)]*arms", text)
