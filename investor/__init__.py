"""The investor simulator: the owner's lots, Israeli tax, rebalancing and harvest suggestions, in a private place.

The plan the owner approved on 16 Oct 2026 (``docs/research/investor-simulator-plan.md``,
every decision D1 to D20 as recommended). A tool, not a test: it uses no
experiment slot, never trades, holds no key and sends nothing anywhere. It
reads one folder the owner points it at (``--data``), prices the lots at the
last close and the Bank of Israel's rate, and writes one Markdown report into
another folder (``--out``). Both folders must be outside this repository.

What is where:

* ``funds`` -- the public fund table, the similar-but-not-identical pairs of
  section 6.5, and the trading-cost parameters of section 6.4;
* ``files`` -- the owner's five CSV files (section 3): read, checked, refused
  when a header line is missing;
* ``ledger`` -- the person: FIFO lots per account on ``analysis.israel_tax``,
  one year netted across accounts (section 4.2), half-years, the tax cost of
  a possible sale, and "value if sold today";
* ``rebalance`` -- section 5; ``harvest`` -- section 6; ``benchmark`` -- the
  same shekels in VT and in VWRA (section 7.4); ``forms`` -- the annual
  report pack (sections 7.2 and 7.3);
* ``market`` -- prices and rates, fetched for the whole fund table from one
  fixed day so the requests show nothing of what is held; ``report`` -- the
  report and the command line.

Nothing here prints an amount, a share count, a ticker or an account name:
the report file is the only place they go (section 2.6, test T41).
"""

from __future__ import annotations

from pathlib import Path
from typing import Final

#: The repository this package lives in: no data folder and no report folder
#: may be inside it (section 2.6).
REPOSITORY: Final[Path] = Path(__file__).resolve().parents[1]

#: The first line of every data file. A private file says the one, a sample
#: file (made-up numbers, in this repository) the other; a file with neither
#: is refused before anything is read. (The private marker is written here as
#: a value, never as a line of its own: a line that is exactly the marker is
#: what the CI detector looks for.)
PRIVATE_MARKER: Final[str] = "# " + "PRIVATE"
SAMPLE_MARKER: Final[str] = "# SAMPLE"

__all__ = ["PRIVATE_MARKER", "REPOSITORY", "SAMPLE_MARKER"]
