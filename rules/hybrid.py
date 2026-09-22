"""Second main arm: the momentum rule, with the news score allowed one veto.

The momentum arm reads strictly less than the model. This arm reads one
thing more: the news score the model call on that line already produced --
a number in [-1, 1] for how the headlines read. No new model call is made;
in the live loop it would be the screening model's score, which is the
cheap first stage of the funnel, so this arm costs the screen and not the
full model. That is the question it exists to ask: is the full model's
judgement worth more than a trend rule that merely listens to the news?

The rule
--------
Momentum decides the direction, exactly as ``rules/momentum.py`` does. The
news score decides whether to act: the hybrid takes momentum's side when
the score does not point the other way, and stands aside (NEUTRAL) when it
does. Conviction is the equal-weight mean of momentum's conviction and the
score's magnitude. When the line carries no score the arm is momentum,
unchanged.

Why every number here is fixed
------------------------------
Equal weights is the only weighting that involves no fitting. The veto is
a sign test, which has no parameter. A score of exactly zero is "no view"
and does not veto. Nothing was chosen by looking at this journal, and
nothing will be moved by it: the harness judges this rule, it does not
tune it.
"""

from __future__ import annotations

from typing import Optional

from app.schemas import Bias, LLMSignal
from orchestrator.technicals import TechnicalSnapshot
from rules import momentum

NAME = "hybrid"


def signal_for(
    ticker: str, snapshot: Optional[TechnicalSnapshot], news_score: Optional[float],
) -> LLMSignal:
    """Momentum's call, vetoed by a news score that points the other way."""
    trend = momentum.signal_for(ticker, snapshot)
    if trend.bias is Bias.NEUTRAL:
        return LLMSignal(ticker=ticker, bias=Bias.NEUTRAL, conviction=0.0,
                         rationale=f"{NAME}: {trend.rationale}")
    if news_score is None:
        return LLMSignal(ticker=ticker, bias=trend.bias, conviction=trend.conviction,
                         rationale=f"{NAME}: no news score; {trend.rationale}")

    direction = 1 if trend.bias is Bias.BULLISH else -1
    if news_score * direction < 0:
        return LLMSignal(
            ticker=ticker, bias=Bias.NEUTRAL, conviction=0.0,
            rationale=f"{NAME}: news score {news_score:+.2f} vetoes the {trend.bias.value} trend",
        )
    conviction = round((trend.conviction + abs(news_score)) / 2.0, 4)
    return LLMSignal(
        ticker=ticker, bias=trend.bias, conviction=conviction,
        rationale=f"{NAME}: news score {news_score:+.2f} agrees; {trend.rationale}",
    )


__all__ = ["NAME", "signal_for"]
