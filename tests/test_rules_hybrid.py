"""The hybrid arm is momentum with the news score allowed one veto.

Momentum decides the direction; the score can only stand the arm aside,
never flip it. Conviction is the equal-weight mean, which is the only
weighting that involves no fitting.
"""

from __future__ import annotations

import pytest

from app.schemas import Bias
from orchestrator.technicals import TechnicalSnapshot
from rules import hybrid, momentum

UP = TechnicalSnapshot.from_dict({"return_63d": 0.10, "distance_sma50": 0.03, "annualised_volatility": 0.20})
DOWN = TechnicalSnapshot.from_dict({"return_63d": -0.10, "distance_sma50": -0.03, "annualised_volatility": 0.20})
FLAT = TechnicalSnapshot.from_dict({"return_63d": 0.10, "distance_sma50": -0.01, "annualised_volatility": 0.20})


def test_agreeing_news_keeps_the_trend_and_averages_conviction():
    sig = hybrid.signal_for("NVDA", UP, news_score=0.8)
    assert sig.bias is Bias.BULLISH
    assert sig.conviction == pytest.approx((0.5 + 0.8) / 2)


def test_opposing_news_vetoes_the_trend_rather_than_flipping_it():
    sig = hybrid.signal_for("NVDA", UP, news_score=-0.3)
    assert sig.bias is Bias.NEUTRAL
    assert "vetoes" in sig.rationale
    sig = hybrid.signal_for("XLE", DOWN, news_score=0.3)
    assert sig.bias is Bias.NEUTRAL


def test_a_zero_score_is_no_view_and_does_not_veto():
    sig = hybrid.signal_for("NVDA", UP, news_score=0.0)
    assert sig.bias is Bias.BULLISH
    assert sig.conviction == pytest.approx(0.25)


def test_no_score_is_plain_momentum():
    sig = hybrid.signal_for("NVDA", UP, news_score=None)
    trend = momentum.signal_for("NVDA", UP)
    assert (sig.bias, sig.conviction) == (trend.bias, trend.conviction)


def test_no_trend_is_neutral_whatever_the_news_says():
    """The news cannot start a trade on its own; that would be a news arm."""
    assert hybrid.signal_for("NVDA", FLAT, news_score=0.9).bias is Bias.NEUTRAL
    assert hybrid.signal_for("NVDA", None, news_score=0.9).bias is Bias.NEUTRAL


def test_it_is_deterministic():
    assert hybrid.signal_for("NVDA", UP, 0.4) == hybrid.signal_for("NVDA", UP, 0.4)
