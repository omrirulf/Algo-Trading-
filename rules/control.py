"""Arm C: a coin flip, so the other two arms have a floor to clear.

A hit rate means nothing on its own. In a week the index rose 2%, "always
long" hit 78% of the time without knowing a single thing about a single
name -- so a model that hits 60% in that week is not beating the market, it
is losing to the direction of it. This arm is what "knowing nothing" scores
on the same tickers over the same windows, and it is the number every other
arm is really being compared against.

It always takes a side, and its conviction always clears the floor, so every
one of its lines is a scoreable trade: a random NEUTRAL would just be a
missing observation, and the point of a control is to have as many
observations as the arms it controls for.

It is seeded from the ticker and the calendar day, not from a clock. That
makes it a fixed function of the journal rather than a fresh draw per run:
the harness recomputes the identical coin flip for NVDA on 21 Sep every time
it is asked, the same way it recomputes the momentum arm, so two runs of the
race disagree only when the journal or the prices did.
"""

from __future__ import annotations

import hashlib
import random
from datetime import date
from typing import Optional

from app.schemas import Bias, LLMSignal

NAME = "random"

#: Fixed, and above MIN_CONVICTION, so every draw is a trade the scorer sees.
CONVICTION = 0.50


def signal_for(ticker: str, day: Optional[date]) -> LLMSignal:
    """A seeded coin flip for one ticker on one day. Never NEUTRAL."""
    seed = int.from_bytes(
        hashlib.sha256(f"{ticker}|{day.isoformat() if day else ''}".encode()).digest()[:8],
        "big",
    )
    bias = random.Random(seed).choice((Bias.BULLISH, Bias.BEARISH))
    return LLMSignal(
        ticker=ticker,
        bias=bias,
        conviction=CONVICTION,
        rationale=f"{NAME}: coin flip seeded from ticker and day",
    )


__all__ = ["NAME", "CONVICTION", "signal_for"]
