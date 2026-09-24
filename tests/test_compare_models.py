"""Which recorded lines a model comparison grades, and the call mix it prints."""

from __future__ import annotations

from datetime import date

import pytest
import yaml

from app.schemas import Bias, LLMSignal
from replay import compare_models as cm
from replay.compare import SignalDiff
from replay.compare_configs import Cell
from replay.runner import ReplayEntry


def entry(ticker, stamp, model):
    return ReplayEntry(ticker=ticker, ts_utc=stamp, prompt="p", original=None, model=model)


def signal(ticker, bias):
    return LLMSignal(ticker=ticker, bias=Bias(bias), conviction=0.6, rationale="r")


def diff(ticker, before, after):
    return SignalDiff(ticker=ticker, before=signal(ticker, before), after=signal(ticker, after))


ENTRIES = [
    entry("AAA", "2026-09-14T15:00:00+00:00", "claude-opus-5"),
    entry("BBB", "2026-09-15T15:00:00+00:00", "claude-opus-5"),
    entry("CCC", "2026-09-15T15:00:01+00:00", "claude-haiku-4-5-20251001"),
    entry("DDD", "2026-09-22T15:00:00+00:00", "claude-opus-5"),
    entry("EEE", "2026-09-23T15:00:00+00:00", "openai/gpt-oss-120b"),
    entry("FFF", None, "claude-opus-5"),
]


def test_the_window_and_the_answering_model_select_exactly_those_lines():
    first, last = cm.parse_days("2026-09-15..2026-09-22")
    kept = cm.select_entries(ENTRIES, answered_by="claude-opus-5", first=first, last=last, limit=500)
    assert [e.ticker for e in kept] == ["BBB", "DDD"]


def test_the_limit_keeps_the_most_recent_of_what_the_filters_left():
    kept = cm.select_entries(ENTRIES, answered_by="claude-opus-5", limit=2)
    assert [e.ticker for e in kept] == ["DDD", "FFF"]


def test_no_filter_is_the_old_behaviour():
    assert cm.select_entries(ENTRIES, limit=3) == ENTRIES[-3:]
    assert cm.select_entries(ENTRIES) == ENTRIES


def test_a_line_without_a_timestamp_is_outside_every_window():
    first, last = cm.parse_days("..2026-09-30")
    assert "FFF" not in [e.ticker for e in cm.select_entries(ENTRIES, first=first, last=last)]


@pytest.mark.parametrize("spec", ["2026-09-15", "2026-09-22..2026-09-15", "x..y"])
def test_a_malformed_window_is_refused(spec):
    with pytest.raises(SystemExit):
        cm.parse_days(spec)


def test_the_mix_counts_both_sides_on_the_same_lines_only():
    cell = Cell(model="openai/gpt-oss-120b", effort="high", diffs=[
        diff("A", "BEARISH", "BEARISH"),
        diff("B", "BEARISH", "NEUTRAL"),
        diff("C", "BEARISH", "NEUTRAL"),
        diff("D", "BEARISH", "BULLISH"),
        diff("E", "BULLISH", "BULLISH"),
        diff("F", "NEUTRAL", "NEUTRAL"),
        SignalDiff(ticker="G", before=signal("G", "BEARISH"), after=None),
    ])
    mix = cm.bias_mix(cell)
    assert mix["lines"] == 6
    assert mix["incumbent"] == {"LONG": 1, "SHORT": 4, "NEUTRAL": 1}
    assert mix["candidate"] == {"LONG": 2, "SHORT": 1, "NEUTRAL": 3}
    assert mix["agreement"] == pytest.approx(3 / 6)
    assert (mix["incumbent_shorts"], mix["candidate_also_short"]) == (4, 1)
    assert mix["short_retention"] == pytest.approx(0.25)
    text = "\n".join(cm.render_mix(cell, "claude-opus-5"))
    assert "1 of 4 also SHORT" in text
    assert "trigger (a) not met" in text  # exactly a quarter is not below it


def test_below_a_quarter_says_so():
    cell = Cell(model="m", effort="high", diffs=[
        diff(t, "BEARISH", "NEUTRAL") for t in "ABCDE"
    ])
    assert "trigger (a) -- report it and stop" in "\n".join(cm.render_mix(cell, "inc"))


def test_the_workflow_passes_the_filters_through_the_environment():
    wf = yaml.safe_load(open(".github/workflows/model-compare.yml"))
    triggers = wf.get("on") or wf.get(True)
    inputs = triggers["workflow_dispatch"]["inputs"]
    assert {"answered_by", "days"} <= set(inputs)
    assert len(inputs) <= 10  # GitHub's limit for a dispatch form
    step = next(s for s in wf["jobs"]["compare"]["steps"] if "compare_models.py" in s.get("run", ""))
    assert step["env"]["ANSWERED_BY"] == "${{ inputs.answered_by }}"
    assert '--answered-by "$ANSWERED_BY"' in step["run"]
    assert "${{ inputs.answered_by }}" not in step["run"]
    assert "${{ inputs.days }}" not in step["run"]
