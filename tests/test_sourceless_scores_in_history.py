"""A score with no source section behind it is null, in history as in the cycle.

The cycle nulls these before they are journalled (``heartbeat``), but every
line written before it did carries the model's own number for a dimension the
prompt never showed it: usually 0.0, sometimes a confident direction. Those
lines are what the trainer fits weights against and what the report measures,
so the same rule has to be readable backwards, off the context each line
recorded -- the evidence, not the date it was written.
"""

from __future__ import annotations

import json
from datetime import date, datetime, timedelta, timezone

import pytest

from analysis import metrics, reader
from analysis.returns import ForwardReturn, PriceSeries
from learn import fit_weights as fw
from orchestrator import heartbeat

# The journal lines these fixtures write must claim whatever model
# production actually runs: the trainer fits per model and discards
# every line another one wrote, so a pinned name here would test the
# discard path by accident the next time the model changes.
from orchestrator.llm import MODEL  # noqa: E402
START = date(2026, 6, 1)


def payload(*, sections=(), day=0, model=MODEL, atr=0.02, gaps=(), **scores):
    """One journal line whose context carries exactly ``sections``."""
    ts = datetime(START.year, START.month, START.day, 14, tzinfo=timezone.utc) + timedelta(days=day)
    signal = {"ticker": "NVDA", "bias": "BULLISH", "conviction": 0.5, "rationale": "r"}
    signal.update({name: scores.get(name.replace("_score", "")) for name in reader.SCORE_FIELDS})
    context = {"gaps": list(gaps), "technicals": {"atr_pct_of_price": atr}}
    context.update({name: f"{name} block" for name in sections})
    return {
        "ts_utc": ts.isoformat(),
        "ticker": "NVDA",
        "context": context,
        "signal": signal,
        "usage": {"model": model, "input_tokens": 1, "output_tokens": 1},
    }


def entry(**kwargs):
    return reader.entry_from(payload(**kwargs))


# --- the rule itself -------------------------------------------------------

def test_the_cycle_and_the_trainer_read_one_definition():
    """Two copies of this map would drift, and the drift would be silent."""
    assert heartbeat.SCORE_SOURCES is reader.SCORE_SOURCES


def test_a_score_with_no_source_section_is_read_as_null():
    line = entry(sections=(), analyst=0.6, insider=-0.4)
    assert line.scores["analyst_score"] == 0.6      # the raw line is kept as written
    assert line.scores_with_a_source()["analyst_score"] is None
    assert line.scores_with_a_source()["insider_score"] is None


def test_a_score_with_its_source_present_is_left_alone():
    line = entry(sections=("analysts", "insiders"), analyst=0.6, insider=-0.4)
    assert line.scores_with_a_source()["analyst_score"] == 0.6
    assert line.scores_with_a_source()["insider_score"] == -0.4


def test_a_genuine_zero_with_a_source_behind_it_survives():
    """The whole point: 0.0 is a real read when something was there to read."""
    line = entry(sections=("analysts", "insiders"), analyst=0.0, insider=0.0)
    assert line.scores_with_a_source()["analyst_score"] == 0.0
    assert line.scores_with_a_source()["insider_score"] == 0.0


@pytest.mark.parametrize("section", ["analysts", "holdings"])
def test_either_analyst_source_is_enough(section):
    line = entry(sections=(section,), analyst=0.3)
    assert line.scores_with_a_source()["analyst_score"] == 0.3


@pytest.mark.parametrize("section", ["insiders", "positioning", "flows"])
def test_any_insider_source_is_enough(section):
    line = entry(sections=(section,), insider=0.3)
    assert line.scores_with_a_source()["insider_score"] == 0.3


def test_a_fabricated_direction_is_nulled_too_not_only_a_zero():
    """What separates this from the gap rule, which only rescues exact 0.0."""
    line = entry(sections=(), insider=-0.5)
    assert line.scores_with_a_source()["insider_score"] is None


def test_the_three_dimensions_with_no_source_map_are_never_touched():
    line = entry(sections=(), news=0.4, technical=-0.2, fundamental=0.0)
    kept = line.scores_with_a_source()
    assert kept["news_score"] == 0.4
    assert kept["technical_score"] == -0.2
    assert kept["fundamental_score"] == 0.0


def test_one_missing_source_does_not_take_the_other_dimension_with_it():
    line = entry(sections=("analysts",), analyst=0.6, insider=-0.4, news=0.5)
    kept = line.scores_with_a_source()
    assert kept["analyst_score"] == 0.6
    assert kept["insider_score"] is None
    assert kept["news_score"] == 0.5


def test_an_empty_section_counts_as_absent():
    """A section rendered empty offered the model nothing, same as no section."""
    raw = payload(analyst=0.6)
    raw["context"]["analysts"] = ""
    assert reader.entry_from(raw).scores_with_a_source()["analyst_score"] is None


# --- the line that cannot tell us ------------------------------------------

def test_a_line_that_journalled_no_context_is_left_exactly_as_written():
    """Absent is not failed, and unknown is not absent.

    An old line with no context recorded does not prove the model had no
    source -- it proves the line does not say. Nulling on that would throw
    away real history to punish a missing field.
    """
    raw = payload(analyst=0.6, insider=-0.4)
    del raw["context"]
    line = reader.entry_from(raw)
    assert line.sections is None
    assert line.scores_with_a_source()["analyst_score"] == 0.6
    assert line.scores_with_a_source()["insider_score"] == -0.4


def test_a_context_that_was_recorded_and_offered_nothing_does_null():
    raw = payload(analyst=0.6)
    raw["context"] = {}
    line = reader.entry_from(raw)
    assert line.sections == frozenset()
    assert line.scores_with_a_source()["analyst_score"] is None


# --- what reads it ---------------------------------------------------------

def test_available_scores_excludes_a_sourceless_score():
    line = entry(sections=("analysts",), news=0.5, analyst=0.6, insider=-0.4)
    assert line.available_scores() == {"news_score": 0.5, "analyst_score": 0.6}


class RisingSource:
    def __init__(self, sessions: int = 60, step: float = 0.01):
        self.bars = [(START + timedelta(days=i), 100.0 * (1 + step) ** i) for i in range(sessions)]

    def closes(self, ticker, start, end):
        return PriceSeries(ticker, self.bars)


def test_the_trainer_fits_on_the_sourced_dimensions_only():
    prepared = fw.prepare(
        [reader.entry_from(payload(sections=("analysts",), news=0.5, analyst=0.6, insider=-0.4))],
        RisingSource(), horizon=3, today=START + timedelta(days=59),
    )
    (observation,) = prepared.observations
    assert observation.scores["news_score"] == 0.5
    assert observation.scores["analyst_score"] == 0.6
    assert observation.scores["insider_score"] is None


def test_a_line_whose_every_score_was_invented_is_left_out_and_counted():
    prepared = fw.prepare(
        [reader.entry_from(payload(sections=(), analyst=0.6, insider=-0.4))],
        RisingSource(), horizon=3, today=START + timedelta(days=59),
    )
    assert prepared.observations == []
    assert prepared.statuses[fw.SKIP_NO_SCORES] == 1


def test_the_gap_rule_still_applies_on_top_of_it():
    """Source present, fetch failed, legacy 0.0: the older rule still catches it."""
    line = reader.entry_from(payload(
        sections=("analysts",), analyst=0.0, gaps=("analyst recommendations unavailable: HTTP 429",),
    ))
    assert fw.nulled_by_gaps(line.scores_with_a_source(), line.gaps)["analyst_score"] is None


def test_the_report_correlates_a_dimension_only_where_it_had_a_source():
    scored = [
        metrics.ScoredSignal(
            entry=reader.entry_from(payload(sections=sections, day=i, analyst=0.5, news=0.5)),
            forward=ForwardReturn(
                entry_date=START + timedelta(days=i), exit_date=START + timedelta(days=i + 3),
                entry_price=100.0, exit_price=100.0 * (1 + 0.01 * (i + 1)), pct=0.01 * (i + 1),
            ),
        )
        for i, sections in enumerate([("analysts",), (), (), ()])
    ]
    correlations = metrics.dimension_correlations(scored)
    assert correlations["analyst_score"].n == 1
    assert correlations["news_score"].n == 4
