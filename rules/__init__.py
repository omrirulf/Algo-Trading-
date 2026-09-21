"""Signal arms that involve no model: the coded thesis, and a control.

The question this package exists to answer is whether the model's daily
judgement beats a fixed rule reading only the price. So every arm here is
deterministic, holds no key, calls nothing over the network, and reads
exactly one thing: the ``TechnicalSnapshot`` the cycle already built and
already showed the model. Same inputs, same instant, nothing the model did
not also see -- which is what makes the comparison a comparison.

Nothing here can trade. An arm's answer goes to the journal beside the
model's and is read back by ``analysis/horse_race.py`` against realised
returns; the signal handed to the engine is the model's, untouched. CI
pins that the same way it pins the learned blend.

Nothing here is fitted to this journal either. Every parameter is the
textbook value from the paper the rule comes from, chosen before a single
line of this journal was scored, and stays there. A rule tuned to the data
it is then judged on is not a rule, it is a story about the past.
"""

from __future__ import annotations

from datetime import date
from typing import Callable, Optional

from app.schemas import LLMSignal
from orchestrator.technicals import TechnicalSnapshot
from rules import control, momentum

#: What every arm is called with: the ticker, the technicals the model saw,
#: and the calendar day. Each module's own ``signal_for`` takes only what it
#: actually reads -- that signature is the statement of what the arm knows --
#: and this is the one place that adapts them to a common shape.
Arm = Callable[[str, Optional[TechnicalSnapshot], Optional[date]], LLMSignal]

#: Every arm, by the name it is journalled and reported under. The journal
#: and the harness both iterate this, so neither can drift from the other.
ARMS: dict[str, Arm] = {
    momentum.NAME: lambda ticker, technicals, day: momentum.signal_for(ticker, technicals),
    control.NAME: lambda ticker, technicals, day: control.signal_for(ticker, day),
}

__all__ = ["ARMS", "Arm", "control", "momentum"]
