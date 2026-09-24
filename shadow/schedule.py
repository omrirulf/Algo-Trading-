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
"""

from __future__ import annotations

from datetime import date
from typing import Final, Optional

CALIBRATION_START: Optional[date] = None
CALIBRATION_DAYS: Final[int] = 15

FUND_START: Optional[date] = None

#: The fund test's three looks are read on the race's look days, with bars
#: from the fund test's OWN share of its data at each (the owner's decision
#: of 24 Sep 2026), not the race's. Planned: calibration seeded from the
#: 2026-09-25 close, 15 sessions to 2026-10-16, the funds starting on the
#: next session, 2026-10-19; the race's looks estimated at 2026-12-22,
#: 2027-03-22 and 2027-06-16. That is 46, 106 and 166 fund sessions.
FUND_TEST_PLANNED_START: Final[date] = date(2026, 10, 19)
FUND_TEST_PLANNED_SESSIONS: Final[tuple[int, int, int]] = (46, 106, 166)
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

__all__ = ["CALIBRATION_DAYS", "CALIBRATION_START", "FUNDS", "FUND_START", "FUND_TEST_BARS",
           "FUND_TEST_PLANNED_SESSIONS", "FUND_TEST_PLANNED_START", "RANDOM_FUNDS"]
