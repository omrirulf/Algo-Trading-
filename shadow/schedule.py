"""When calibration and the fund test start. Set by the owner's decision, never by the code.

* ``CALIBRATION_START`` -- the trading day whose close seeds the calibration
  fund from the real paper account. ``None`` until the owner sets it, in a
  reviewed change to this file, and only after the owner has approved the
  pass rule in ``shadow.calibration.PASS_RULE``; until then calibration has
  not started, whatever the code could compute.
* ``FUND_START`` -- the first fund session: the day the four funds (the
  exploratory funds and the thousand coin-flip funds too) start with
  $100,000 each. Fixed by the owner's decision of 26 Sep 2026: the funds act
  on the cycle journalled on ``FUND_FIRST_CYCLE`` (Monday 28 Sep 2026) at the
  next open, so the first fund session is 29 Sep 2026, and the fund test's
  sample runs from it. It does not move when calibration is delayed.
* The fund test still **counts only after calibration passes**. Until the
  calibration verdict is a pass, no fund is run and no fund result is
  calculated or shown (``shadow.run.build``): during calibration only the
  calibration match is reported. When it passes, every fund is run from
  ``FUND_FIRST_CYCLE`` with the code as merged -- after a calibration fix,
  with the fixed code only -- so a delayed calibration delays the reading,
  never the start.

``CALIBRATION_FIXES`` is the third thing only a reviewed change sets: the
record of every fix made after a calibration fail (the owner's fail rule of
25 Sep 2026, which replaced "restart the 15 days from zero").
"""

from __future__ import annotations

from datetime import date
from typing import Final, Optional

CALIBRATION_START: Optional[date] = None
CALIBRATION_DAYS: Final[int] = 15

#: Every fix made after a calibration fail, oldest first: (the day the fix
#: was merged, one line saying what it fixed). A fail is fixed, logged in the
#: pre-registration's Amendments table, and added here in the same reviewed
#: change -- never by the code, and never without its Amendments row. The
#: nightly job re-runs calibration from the same seed snapshot with the code
#: as merged, so adding a fix here is all a re-run needs; what it changes is
#: how long calibration lasts (``AFTER_FIX_DAYS``).
CALIBRATION_FIXES: Final[tuple[tuple[date, str], ...]] = ()
#: Calibration days that must come after the last fix. A day counts as after
#: a fix only if its date is later than the fix's: a fix merged on a day may
#: have been written with that day's close in view. So calibration ends at
#: day ``CALIBRATION_DAYS`` or at the last fix + 5 days, whichever is later.
AFTER_FIX_DAYS: Final[int] = 5

#: The cycle day whose lines the funds act on first, at the next open (the
#: owner's decision of 26 Sep 2026).
FUND_FIRST_CYCLE: Final[date] = date(2026, 9, 28)
#: The first fund session: the trading day after ``FUND_FIRST_CYCLE``. The
#: fund test's sample runs from it.
FUND_START: Final[date] = date(2026, 9, 29)

#: The fund test's three looks are read on the race's look days, with bars
#: from the fund test's OWN share of its data at each (the owner's decision
#: of 24 Sep 2026), not the race's. The start is fixed (above), so the plan
#: does not depend on when calibration ends: from the 2026-09-29 session to
#: the race's looks, estimated at 2026-12-22, 2027-03-22 and 2027-06-16, that
#: is 60, 120 and 180 fund sessions.
FUND_TEST_PLANNED_START: Final[date] = FUND_START
FUND_TEST_PLANNED_SESSIONS: Final[tuple[int, int, int]] = (60, 120, 180)
#: The race's estimated look days, as above: the registered sessions and
#: bars were computed from these. ``shadow.fund_test.fund_test_plan``
#: counts from them again, and skips a look that comes before calibration
#: has passed.
FUND_TEST_LOOK_ESTIMATES: Final[tuple[date, date, date]] = (
    date(2026, 12, 22), date(2027, 3, 22), date(2027, 6, 16))
#: The O'Brien-Fleming-type alpha-spending rule (Lan-DeMets, the owner's
#: decision of 26 Sep 2026; ``analysis.decision_gate.spending_bars``), two-
#: sided 5% overall, at shares 60/180, 120/180 and 1 of the planned final
#: sessions: exactly 3.395, 2.407 and 2.015, printed as the pre-registration
#: prints them (``analysis.decision_gate.rounded_bar``). If a look moves, or
#: is skipped because calibration has not passed, the bar is computed at the
#: look by the same rule from the fund sessions actually there, with the
#: bars already used kept, and logged in the Amendments table the day it is
#: used. The race's bars are not these (``analysis.decision_gate.CHECKPOINTS``).
FUND_TEST_BARS: Final[tuple[float, float, float]] = (3.40, 2.41, 2.02)

#: The four funds, in the order they are reported.
FUNDS: Final[tuple[str, ...]] = ("model", "momentum", "hybrid", "vt")
#: Coin-flip funds drawn for the band of what luck alone does.
RANDOM_FUNDS: Final[int] = 1000

__all__ = ["AFTER_FIX_DAYS", "CALIBRATION_DAYS", "CALIBRATION_FIXES", "CALIBRATION_START", "FUNDS",
           "FUND_FIRST_CYCLE", "FUND_START", "FUND_TEST_BARS", "FUND_TEST_LOOK_ESTIMATES",
           "FUND_TEST_PLANNED_SESSIONS", "FUND_TEST_PLANNED_START", "RANDOM_FUNDS"]
