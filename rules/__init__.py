"""Signal arms that involve no model call of their own: the coded theses, and a control.

The question this package exists to answer is whether the model's daily
judgement beats a fixed rule. So every arm here is deterministic, holds no
key, calls nothing over the network, and reads only what the cycle already
built and already showed the model -- the same inputs at the same instant,
nothing the model did not also see -- which is what makes the comparison a
comparison.

Nothing here can trade. An arm's answer goes to the journal beside the
model's and is read back by ``analysis/horse_race.py`` against realised
returns; the signal handed to the engine is the model's, untouched. CI
pins that the same way it pins the learned blend.

Nothing here is fitted to this journal either. Every parameter is the
textbook value from the paper the rule comes from, chosen before a single
line of this journal was scored, and stays there. A rule tuned to the data
it is then judged on is not a rule, it is a story about the past.

Main arms and exploratory arms
------------------------------
``momentum`` and ``hybrid`` are main arms: the race's pre-registered
decision compares the model against each of them. ``random`` is the floor.
``insiders`` is exploratory: it takes a side on a small share of lines and
is reported only on those, paired against the model and the momentum rule
on the same lines, and it can never change the main decision. The
distinction is written down here, once, so the harness and the
pre-registration cannot drift apart.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Callable, Optional

from app.schemas import LLMSignal
from orchestrator.insiders import InsiderSnapshot
from orchestrator.technicals import TechnicalSnapshot
from rules import control, hybrid, insider_buying, momentum


@dataclass(frozen=True)
class Seen:
    """What an arm is shown: exactly what the model was, no more.

    The calendar day seeds the control. The technicals are the snapshot the
    prompt carried. The insider snapshot is the prompt's INSIDER ACTIVITY
    section, ``None`` for a fund or a line without one. The news score is
    the model's own reading of the headlines on that line -- it is an
    *output* of the model call, which is why only the hybrid reads it and
    why the hybrid is a separate, second main comparison rather than a rule
    that "sees strictly less".
    """

    ticker: str
    day: Optional[date] = None
    technicals: Optional[TechnicalSnapshot] = None
    insiders: Optional[InsiderSnapshot] = None
    news_score: Optional[float] = None


#: What every arm is called with. Each module's own ``signal_for`` takes only
#: what it actually reads -- that signature is the statement of what the arm
#: knows -- and this is the one place that adapts them to a common shape.
Arm = Callable[[Seen], LLMSignal]

#: Every arm, by the name it is journalled and reported under. The journal
#: and the harness both iterate this, so neither can drift from the other.
ARMS: dict[str, Arm] = {
    momentum.NAME: lambda seen: momentum.signal_for(seen.ticker, seen.technicals),
    hybrid.NAME: lambda seen: hybrid.signal_for(seen.ticker, seen.technicals, seen.news_score),
    control.NAME: lambda seen: control.signal_for(seen.ticker, seen.day),
    insider_buying.NAME: lambda seen: insider_buying.signal_for(seen.ticker, seen.insiders, seen.day),
}

#: Arms that take a side on a small share of lines and are reported only on
#: those. Never part of the main decision.
EXPLORATORY: frozenset[str] = frozenset({insider_buying.NAME})

#: The arms the model is raced against in the main tables, in report order.
MAIN_ARMS: tuple[str, ...] = (momentum.NAME, hybrid.NAME, control.NAME)

__all__ = ["ARMS", "Arm", "EXPLORATORY", "MAIN_ARMS", "Seen", "control", "hybrid",
           "insider_buying", "momentum"]
