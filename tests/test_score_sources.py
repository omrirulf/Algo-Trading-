"""A score whose section was never rendered is null, not 0.0.

The 16 Sep cycle shipped six bond funds whose prompts carried no analyst
roll-up, no CFTC positioning and no fund flows. The prompt tells the model
four separate times to leave those scores null. It returned 0.0 for all six,
and for TLT it returned -0.20 -- a bearish read on an instrument the system
was short, invented from a section that was not in front of it.

0.0 is not a harmless default. It reads as "I looked and it was balanced"
when the truth is "there was nothing to look at", and nothing downstream can
tell the two apart: the learned blend counted five dimensions of coverage for
every fund and fitted weights against numbers nobody measured.

So the orchestrator decides it instead of asking. These tests are about that
decision being made from what was actually rendered.
"""

from __future__ import annotations

import types

from app.schemas import Bias, LLMSignal
from orchestrator.heartbeat import SCORE_SOURCES, scores_without_a_source


def _signal(**scores) -> LLMSignal:
    return LLMSignal(ticker="TLT", bias=Bias.BEARISH, conviction=0.35,
                     rationale="rates", **scores)


def _context(**sections):
    base = dict(ticker="TLT", analysts=None, holdings=None, insiders=None,
                positioning=None, flows=None)
    base.update(sections)
    return types.SimpleNamespace(**base)


def test_a_bond_fund_with_no_roll_up_and_no_positioning_records_null():
    """The exact shape of the six funds that shipped wrong on 16 Sep."""
    fixed = scores_without_a_source(
        _signal(analyst_score=0.0, insider_score=0.0), _context()
    )
    assert fixed.analyst_score is None
    assert fixed.insider_score is None


def test_an_invented_directional_score_is_nulled_too():
    """TLT's -0.20 came from a section that was not there.

    A fabricated number is worse than a fabricated zero, not better: it is a
    view with a direction, on an instrument the system holds.
    """
    fixed = scores_without_a_source(_signal(insider_score=-0.20), _context())
    assert fixed.insider_score is None


def test_a_fund_with_a_holdings_roll_up_keeps_its_analyst_score():
    fixed = scores_without_a_source(
        _signal(analyst_score=0.30), _context(holdings=object())
    )
    assert fixed.analyst_score == 0.30


def test_positioning_alone_is_enough_to_keep_the_insider_score():
    fixed = scores_without_a_source(
        _signal(insider_score=-0.20), _context(positioning=object())
    )
    assert fixed.insider_score == -0.20


def test_flows_alone_is_enough_when_there_is_no_positioning():
    """A country fund has no futures contract but does have a share count."""
    fixed = scores_without_a_source(
        _signal(insider_score=0.15), _context(flows=object())
    )
    assert fixed.insider_score == 0.15


def test_a_company_keeps_both_from_its_own_sections():
    fixed = scores_without_a_source(
        _signal(analyst_score=0.5, insider_score=-0.15),
        _context(analysts=object(), insiders=object()),
    )
    assert fixed.analyst_score == 0.5 and fixed.insider_score == -0.15


def test_a_score_the_model_already_left_null_stays_null():
    fixed = scores_without_a_source(_signal(), _context())
    assert fixed.analyst_score is None and fixed.insider_score is None


def test_a_zero_with_a_real_source_behind_it_is_left_alone():
    """0.0 is a legitimate reading when there was something to read.

    This is the line the whole change turns on: the rule is about whether a
    source existed, never about whether the number happens to be zero.
    """
    fixed = scores_without_a_source(
        _signal(analyst_score=0.0, insider_score=0.0),
        _context(holdings=object(), positioning=object()),
    )
    assert fixed.analyst_score == 0.0
    assert fixed.insider_score == 0.0


def test_the_other_three_dimensions_are_never_touched():
    """Only the two that swap source by instrument kind are governed here."""
    signal = _signal(news_score=0.0, technical_score=-0.55, fundamental_score=-0.1)
    fixed = scores_without_a_source(signal, _context())
    assert fixed.news_score == 0.0
    assert fixed.technical_score == -0.55
    assert fixed.fundamental_score == -0.1


def test_an_untouched_signal_is_returned_as_is():
    signal = _signal(analyst_score=0.3)
    assert scores_without_a_source(signal, _context(holdings=object())) is signal


def test_every_governed_score_names_both_kinds_of_source():
    """A fund and a company read the same slot from different places.

    Listing only one kind would null the other kind's real score on every
    ticker -- silently, because a null looks exactly like an honest absence.
    """
    assert SCORE_SOURCES["analyst_score"] == ("analysts", "holdings")
    assert SCORE_SOURCES["insider_score"] == ("insiders", "positioning", "flows")
