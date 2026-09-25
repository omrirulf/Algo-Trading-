"""When calibration and the fund test start. Set by the owner's decision, never by the code.

Both are ``None`` until the owner says otherwise, in a reviewed change to
this file:

* ``CALIBRATION_START`` -- the trading day whose close seeds the calibration
  fund from the real paper account. It is set only after the owner has
  approved the pass rule in ``shadow.calibration.PASS_RULE``; until
  then calibration has not started, whatever the code could compute.
* ``FUND_START`` -- the first trading day after calibration passes, and the
  day the four funds (and the thousand coin-flip funds) start with $100,000
  each. Until it is set, no fund is run and nothing about how the funds
  compare is printed: during calibration, only the calibration match is
  reported.

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

FUND_START: Optional[date] = None

#: The fund test's three looks are read on the race's look days, with bars
#: from the fund test's OWN share of its data at each (the owner's decision
#: of 24 Sep 2026), not the race's. Planned: calibration seeded from the
#: 2026-09-25 close, 15 sessions to 2026-10-16, the funds starting on the
#: next session, 2026-10-19; the race's looks estimated at 2026-12-22,
#: 2027-03-22 and 2027-06-16. That is 46, 106 and 166 fund sessions.
FUND_TEST_PLANNED_START: Final[date] = date(2026, 10, 19)
FUND_TEST_PLANNED_SESSIONS: Final[tuple[int, int, int]] = (46, 106, 166)
#: The race's estimated look days, as above: the registered sessions and
#: bars were computed from these. ``shadow.fund_test.fund_test_plan``
#: counts from them again when calibration's end moves.
FUND_TEST_LOOK_ESTIMATES: Final[tuple[date, date, date]] = (
    date(2026, 12, 22), date(2027, 3, 22), date(2027, 6, 16))
#: O'Brien-Fleming for those shares, two-sided 5% overall
#: (``analysis.decision_gate.obrien_fleming_bars``): exactly 3.797, 2.501
#: and 1.999, rounded as the race's are. If the start or the look days move,
#: these are recomputed by the same function and the change is logged in the
#: pre-registration's Amendments table before the fund test starts.
FUND_TEST_BARS: Final[tuple[float, float, float]] = (3.80, 2.50, 2.00)

#: The four funds, in the order they are reported.
FUNDS: Final[tuple[str, ...]] = ("model", "momentum", "hybrid", "vt")
#: Coin-flip funds drawn for the band of what luck alone does.
RANDOM_FUNDS: Final[int] = 1000

__all__ = ["AFTER_FIX_DAYS", "CALIBRATION_DAYS", "CALIBRATION_FIXES", "CALIBRATION_START", "FUNDS", "FUND_START",
           "FUND_TEST_BARS", "FUND_TEST_LOOK_ESTIMATES", "FUND_TEST_PLANNED_SESSIONS", "FUND_TEST_PLANNED_START",
           "RANDOM_FUNDS"]
