"""The thesis-check logger: once a week, does the reason a held name was bought still hold? Log only.

Why it exists (the owner's instruction of 4 Oct 2026, item 2). Once a week,
for each name the paper account holds, the same model is asked: given the
entry reasoning archived with the entry and today's headlines for the name,
is the thesis VALID, WEAKENED or BROKEN? With one sentence of reason.

Log only. It never trades, never changes a stop, never feeds any arm or fund,
and nothing in the cycle reads it. At the checkpoints after it is registered,
the forward returns of the names it called BROKEN are compared with those it
called VALID, as a description only: it is not a test, it is not in the
Benjamini-Hochberg family and has no Deflated Sharpe Ratio
(pre-registration section 13.12).

When. Registered at the race's second planned look (``REGISTRATION``,
2027-03-22), as an idea of the second quarter of 2027 -- the same pattern as
the IC test, registered at the 2026-12-22 checkpoint and counted in the
first quarter of 2027 -- and switched on from the first day of that quarter
(``START``, 2027-04-01). ``THESIS_CHECK_ENABLED`` keeps it off until then; a
test fails if it is on before ``START``.

Standard library only and no side effects, so any package may import it.
"""

from __future__ import annotations

from datetime import date, time as clock_time
from pathlib import Path
from typing import Final

#: The logger's on/off switch. False until the pre-registration says it is
#: on; ``tests/test_thesis_check_runner.py`` fails if this is True before ``START``.
THESIS_CHECK_ENABLED: Final[bool] = False

#: The checkpoint at which it is registered: the race's second planned look
#: (estimated), the checkpoint before the second quarter of 2027.
REGISTRATION: Final[date] = date(2027, 3, 22)

#: The first UTC day a name may be checked, and the first day any of its
#: results may be computed: the first day of the second quarter of 2027.
#: Must equal the date the pre-registration names.
START: Final[date] = date(2027, 4, 1)

#: The day this was prepared.
PREPARED_ON: Final[date] = date(2026, 10, 4)

#: The quarter whose limit of two new ideas it counts against (section 13.8).
QUARTER: Final[str] = "2027-Q2"

#: Its row in ``docs/research/graveyard.md`` (one trial in N).
TRIAL: Final[int] = 43

#: The three answers, in order from "still holds" to "no longer holds".
VERDICTS: Final[tuple[str, ...]] = ("VALID", "WEAKENED", "BROKEN")

#: The longest reason kept, in characters ("one sentence").
REASON_MAX_CHARS: Final[int] = 300

#: Hard cap on the logger's model cost in one ISO week, in dollars (the
#: owner's instruction of 4 Oct 2026). Every HTTP ask counts.
WEEKLY_COST_CAP_USD: Final[float] = 0.10

#: What one check is expected to cost: held in reserve for each call in
#: flight, and charged for an ask whose price is unknown. Production's
#: measured mean is $0.0025 an answered call; the prompt here is shorter.
ESTIMATED_COST_PER_CALL_USD: Final[float] = 0.003

#: What a week is expected to cost: about 20 held names at the estimate. The
#: headlines are the ones production already gathered, so no news search is paid.
ESTIMATED_WEEKLY_COST_USD: Final[float] = 0.06

#: The forward return the checkpoint description reads: from the open of the
#: first session after the check's day to the close of the 5th session
#: (one week, the time to the next check), price only, signed by the side the
#: position was opened on (+1 bought, -1 sold short).
FORWARD_SESSIONS: Final[int] = 5

#: Fewer BROKEN checks than this by the final checkpoint: the comparison is
#: "not tested" (as section 13.7's minimum).
MIN_BROKEN: Final[int] = 20

#: No new name is started at or after this UTC time, as the vote and the
#: shadow universe: a line is dated by the UTC time it is written, and a check
#: asked after midnight would read the next day's held lines.
NO_NEW_NAME_AFTER_UTC: Final[clock_time] = clock_time(23, 15)

#: The ``event`` field on every line the logger writes.
EVENT: Final[str] = "thesis_check"

#: The repository root, worked out the same way ``config/settings.py`` does it.
_PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent.parent

#: Where the logger's lines go: one file per UTC month, like the journal.
JOURNAL_DIR: Final[Path] = _PROJECT_ROOT / "logs" / "thesis_check"


__all__ = [
    "ESTIMATED_COST_PER_CALL_USD",
    "ESTIMATED_WEEKLY_COST_USD",
    "EVENT",
    "FORWARD_SESSIONS",
    "JOURNAL_DIR",
    "MIN_BROKEN",
    "NO_NEW_NAME_AFTER_UTC",
    "PREPARED_ON",
    "QUARTER",
    "REASON_MAX_CHARS",
    "REGISTRATION",
    "START",
    "THESIS_CHECK_ENABLED",
    "TRIAL",
    "VERDICTS",
    "WEEKLY_COST_CAP_USD",
]
