"""The voting arm ``model_vote``: five calls of the same model on the same input, one vote. Shadow only.

Why it exists (the owner's instruction of 4 Oct 2026, item 1). The model's
answer to one call is one draw: the same model, asked the same question
again, can answer differently. A vote of five draws reduces that sampling
noise. Whether that makes better trades is the question this idea asks,
against the model's single call on the same lines. Nothing here is ever
traded: the vote is a race arm and a fund in the shadow funds, like every
exploratory idea, and it can change no decision (pre-registration section 6).

What it does not do. Repeating the same model reduces sampling noise, not
the bias every call of that model shares: five calls see the same prompt
with the same training, and are wrong together where the model is wrong.
The wisdom-of-the-crowd study (Schoenegger et al., Science Advances, 2024)
used 12 different models on forecasting questions, not stock returns; a
vote across different models would be a separate, later idea. The card says
so (``docs/research/cards/model_vote.md``).

The rule, fixed here before any vote exists (pre-registration section 13.11):

* **Votes.** Vote 1 is the production answer, as journalled. Votes 2 to 5
  are four more calls to the same model with the same settings, each
  re-sending the archived request body of the production line's first ask
  (the heartbeat's capture, ``orchestrator/model_io.py``), through
  production's own call path, so its retries and re-asks are production's.
* **Sides.** BULLISH is LONG, BEARISH is SHORT, NEUTRAL is NEUTRAL: each
  vote's own bias, as answered, before any floor.
* **Answer.** At least ``MIN_VOTES`` (3) of the ``VOTES`` (5) must succeed,
  or the line has no answer and is dropped for the vote and its comparator
  alike. The signal is the side with the most votes if it has at least 3 of
  the 5, else NEUTRAL; a tie for the most is NEUTRAL. Conviction is the
  share of the 5 votes that agree times the mean conviction of the agreeing
  votes. A failed vote is a vote that does not agree (the share is always
  out of 5). The conviction floor is production's (0.30).
* **Vote score** (the IC comparison only): the mean of the blended scores of
  the successful votes, each blended with the weights the production line
  itself applied.

Off until ``START``. ``MODEL_VOTE_ENABLED`` keeps the runner off; a test
fails if it is on before the date the pre-registration names. Registered at
the first checkpoint (2026-12-22), as the second new idea of the first
quarter of 2027 (the IC test is the first). Its results are computed only at
the checkpoints from that date, never before.

Standard library only and no side effects, so any package may import it --
the race and the funds included.
"""

from __future__ import annotations

from datetime import date, time as clock_time
from pathlib import Path
from typing import Final

#: The runner's on/off switch. False until the pre-registration says the vote
#: is on; ``tests/test_model_vote_runner.py`` fails if this is True before ``START``.
MODEL_VOTE_ENABLED: Final[bool] = False

#: The checkpoint at which the vote is registered: the race's first planned
#: look, where the IC test is registered too (the owner's instruction of
#: 4 Oct 2026: "register it at the 22 Dec 2026 checkpoint window").
REGISTRATION: Final[date] = date(2026, 12, 22)

#: The first UTC day a line may be voted on, and the first day any result of
#: the vote may be computed. Must equal the date the pre-registration names.
START: Final[date] = date(2026, 12, 22)

#: The day this was prepared.
PREPARED_ON: Final[date] = date(2026, 10, 4)

#: The quarter it counts in (section 13.8): the quarter it starts producing
#: data, ``START`` (the owner's rule of 6 Oct 2026). First written as the
#: second idea of the first quarter of 2027; by that rule it is an idea of the
#: fourth quarter of 2026.
QUARTER: Final[str] = "2026-Q4"

#: Its row in ``docs/research/graveyard.md`` (one trial in N).
TRIAL: Final[int] = 42

#: Votes per line: the production answer and four more calls.
VOTES: Final[int] = 5
EXTRA_CALLS: Final[int] = VOTES - 1

#: The fewest successful votes (the production answer counted) that give a
#: line an answer, and the fewest votes the winning side needs.
MIN_VOTES: Final[int] = 3

#: Each vote's bias as a side of the vote.
SIDES: Final[dict[str, str]] = {"BULLISH": "LONG", "BEARISH": "SHORT", "NEUTRAL": "NEUTRAL"}

#: A side back as the bias the race and the funds read.
BIASES: Final[dict[str, str]] = {side: bias for bias, side in SIDES.items()}

#: Hard cap on the vote's model cost in one UTC day, in dollars, and the day's
#: cost at which the owner's phone is told (the owner's instruction of
#: 4 Oct 2026: "Cap $1.00 a day with a phone alert at $0.80, like the universe
#: cap"). Every HTTP ask counts, retries and re-asks included.
DAILY_COST_CAP_USD: Final[float] = 1.00
DAILY_COST_WARN_USD: Final[float] = 0.80

#: What a full day is expected to cost (the owner's figure of 4 Oct 2026):
#: about 58 answered lines a day, four calls each.
ESTIMATED_DAILY_COST_USD: Final[float] = 0.70

#: What one call is expected to cost: held in reserve for each call in flight,
#: and charged for an ask whose price is unknown (a timeout, a failure).
#: About the day's estimate over 232 calls; the measured mean of an answered
#: production call in October 2026 is $0.0025, before retries and re-asks.
ESTIMATED_COST_PER_CALL_USD: Final[float] = 0.003

#: No new line is started at or after this UTC time (the owner's instruction:
#: "Start no new name after 23:15 UTC"), as the shadow universe.
NO_NEW_NAME_AFTER_UTC: Final[clock_time] = clock_time(23, 15)

#: The ``event`` field on every line the runner writes.
EVENT: Final[str] = "model_vote"

#: The repository root, worked out the same way ``config/settings.py`` does it.
_PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent.parent

#: Where the vote's lines go: one file per UTC month (``2026-12.log``, ...),
#: like the production journal, and never mixed into it.
JOURNAL_DIR: Final[Path] = _PROJECT_ROOT / "logs" / "model_vote"

#: The names the race arm, the fund and its comparator go by.
ARM: Final[str] = "model_vote"
COMPARATOR_FUND: Final[str] = "model_vote_comparator"


__all__ = [
    "ARM",
    "BIASES",
    "COMPARATOR_FUND",
    "DAILY_COST_CAP_USD",
    "DAILY_COST_WARN_USD",
    "ESTIMATED_COST_PER_CALL_USD",
    "ESTIMATED_DAILY_COST_USD",
    "EVENT",
    "EXTRA_CALLS",
    "JOURNAL_DIR",
    "MIN_VOTES",
    "MODEL_VOTE_ENABLED",
    "NO_NEW_NAME_AFTER_UTC",
    "PREPARED_ON",
    "QUARTER",
    "REGISTRATION",
    "SIDES",
    "START",
    "TRIAL",
    "VOTES",
]
