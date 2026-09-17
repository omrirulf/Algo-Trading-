"""The cheap model's scores obey the source rule too, not just the expensive one.

``scores_without_a_source`` was wired into the decide call site and not the
screen one. The first live cycle after it shipped proved the cost exactly:
every sourceless score on an Opus line was null, and every one of the
thirty-eight on a Haiku line was still a number.

It was survivable rather than harmless. The trainer reads full-model lines
only, so no weight was fitted on them, and the readers added alongside the
rule (``JournalEntry.scores_with_a_source``) correct the view at read time
whichever stage wrote the line. What was not survivable is the journal: it is
committed to a public repository every cycle, and a screened NEUTRAL line is
the *only* record of that ticker for that day.

Two tests, because one of them is the one that would have caught it. The
behavioural test pins the screen path. The structural test pins every path,
including the one somebody adds next year.
"""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

from app.schemas import Bias, LLMSignal
from orchestrator import heartbeat


class Ctx:
    """A fund context with a real analyst source and no insider source."""

    ticker = "XLE"
    analysts = None
    holdings = "Rolled up from the 5 largest holdings, 51.7% of the fund"
    insiders = None
    positioning = None
    flows = None


def signal(**scores) -> LLMSignal:
    return LLMSignal(
        ticker="XLE", bias=Bias.BULLISH, conviction=0.5, rationale="r",
        news_score=0.2, technical_score=0.1, fundamental_score=0.0, **scores,
    )


def test_the_rule_nulls_the_sourceless_score_and_keeps_the_sourced_one():
    out = heartbeat.scores_without_a_source(
        signal(analyst_score=0.4, insider_score=-0.3), Ctx()
    )
    assert out.analyst_score == 0.4      # holdings is a real source
    assert out.insider_score is None     # no insiders, positioning or flows
    assert out.news_score == 0.2 and out.bias is Bias.BULLISH


def test_the_screen_path_applies_it_before_journalling():
    """A screened NEUTRAL ticker is journalled from the screen's own answer.

    That line is the only record of the ticker for the day, so a number the
    prompt could not support must not survive into it. This is the call site
    that was missed, so it is named specifically rather than left to the
    structural test below to catch in aggregate.
    """
    tree = ast.parse(Path(heartbeat.__file__).read_text())

    def reads_the_screen(node: ast.AST) -> bool:
        return (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name) and node.func.id == "parse_signal"
            and bool(node.args)
            and isinstance(node.args[0], ast.Attribute) and node.args[0].attr == "text"
            and isinstance(node.args[0].value, ast.Name) and node.args[0].value.id == "first"
        )

    screen_calls = [node for node in ast.walk(tree) if reads_the_screen(node)]
    assert len(screen_calls) == 1, "expected exactly one parse of the screen's answer"

    wrapping_the_screen = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "scores_without_a_source"
        and node.args and reads_the_screen(node.args[0])
    ]
    assert wrapping_the_screen, (
        f"heartbeat.py:{screen_calls[0].lineno}: the screen's signal is journalled "
        "without scores_without_a_source"
    )


def _parse_signal_calls(tree: ast.AST) -> list[ast.Call]:
    return [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "parse_signal"
    ]


def test_no_parsed_signal_reaches_the_journal_unwrapped():
    """Every ``parse_signal`` result is wrapped in ``scores_without_a_source``.

    The structural version of the behaviour above, so that a third call site
    added later fails here rather than in a prompt. The rule cannot be
    enforced by the parser itself: it needs the context, which ``parse_signal``
    is deliberately not given.
    """
    tree = ast.parse(Path(heartbeat.__file__).read_text())

    wrapped = {
        (node.args[0].lineno, node.args[0].col_offset)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "scores_without_a_source"
        and node.args
        and isinstance(node.args[0], ast.Call)
        and isinstance(node.args[0].func, ast.Name)
        and node.args[0].func.id == "parse_signal"
    }
    every = {(node.lineno, node.col_offset) for node in _parse_signal_calls(tree)}

    naked = sorted(every - wrapped)
    assert not naked, (
        "parse_signal used without scores_without_a_source at "
        + ", ".join(f"heartbeat.py:{line}" for line, _ in naked)
    )
    assert len(every) >= 2, "expected both the screen and the decide call sites"


@pytest.mark.parametrize("field,sources", sorted(heartbeat.SCORE_SOURCES.items()))
def test_every_mapped_score_is_nulled_when_all_its_sources_are_absent(field, sources):
    class Empty:
        ticker = "TLT"

    out = heartbeat.scores_without_a_source(
        signal(analyst_score=0.6, insider_score=0.6), Empty()
    )
    assert getattr(out, field) is None, f"{field} survived with none of {sources}"
