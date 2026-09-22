"""What the rule arms would have said, written beside the model's answer.

``rules/`` holds the coded thesis and its control. This is the live side:
for every journal line, each arm is asked the question the model was asked,
from the same ``TechnicalSnapshot`` the model saw, and its answer is
recorded under ``arms`` so ``analysis/horse_race.py`` can score all three
against the same realised returns.

It is called from ``journal.record`` itself rather than from the cycle.
That is deliberate: the arms must be on every line -- the ones the screen
dropped, the ones the book already held, the ones the model failed on --
because a rule-based system would still have had an opinion on those
tickers that day, and a race that only ran on the lines the model chose
to answer would be handing the model the choice of battlefield. Computing
it where the line is written is the one place no call site can forget.

Nothing here reaches the engine. The signal handed to ``post_signal`` is
the model's, untouched; the only consumer of what this produces is the
journal line, and CI pins both, exactly as it does for the learned blend.

Failure is a labelled fallback, never an exception, and never the loss of
the line: an arm that raises is recorded as its error, the other arms are
still recorded, and the cycle runs exactly as it did before this existed.
"""

from __future__ import annotations

import logging
from datetime import date
from typing import Any, Optional

from app.schemas import LLMSignal
from orchestrator.context import TickerContext
from rules import ARMS, Seen

log = logging.getLogger("arms")


def arms_record(
    context: TickerContext, day: Optional[date], signal: Optional[LLMSignal] = None,
) -> dict[str, Any]:
    """Every arm's call for one line. Never raises.

    ``day`` is the calendar day the line is written on, which is what seeds
    the control arm -- so the harness, reading the day back off the line's
    own timestamp, recomputes the identical coin flip. ``signal`` is the
    model's answer on the line, if there was one: the hybrid arm reads its
    news score, and nothing else of it.
    """
    seen = Seen(
        ticker=context.ticker, day=day, technicals=context.technicals,
        insiders=context.insiders,
        news_score=signal.news_score if signal is not None else None,
    )
    record: dict[str, Any] = {}
    for name, arm in ARMS.items():
        try:
            call = arm(seen)
            record[name] = {
                "bias": call.bias.value,
                "conviction": call.conviction,
                "rationale": call.rationale,
            }
        except Exception as exc:  # noqa: BLE001 - one arm's failure is one arm's line
            log.exception("%s: %s arm failed", context.ticker, name)
            record[name] = {"error": f"{type(exc).__name__}: {exc}"[:200]}
    return record


__all__ = ["arms_record"]
