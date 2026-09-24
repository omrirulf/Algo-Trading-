"""When calibration and the fund test start. Set by the owner's decision, never by the code.

Both are ``None`` until the owner says otherwise, in a reviewed change to
this file:

* ``CALIBRATION_START`` -- the trading day whose close seeds the calibration
  fund from the real paper account. It is set only after the owner has
  approved the pass rule in ``shadow.calibration.PROPOSED_PASS_RULE``; until
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

#: The four funds, in the order they are reported.
FUNDS: Final[tuple[str, ...]] = ("model", "momentum", "hybrid", "vt")
#: Coin-flip funds drawn for the band of what luck alone does.
RANDOM_FUNDS: Final[int] = 1000

__all__ = ["CALIBRATION_DAYS", "CALIBRATION_START", "FUNDS", "FUND_START", "RANDOM_FUNDS"]
