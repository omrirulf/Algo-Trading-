"""Who is positioned how, from the CFTC's weekly Commitments of Traders.

A fund has no insiders. Nobody files a Form 4 on gold, and no director of
the Treasury sells bonds and discloses it. So the insider slot for a
commodity or a bond fund was empty by necessity -- until you remember that
the futures market publishes something better every Friday.

The CFTC requires every large trader to report their position, and publishes
the aggregate: how many contracts the professional speculators ("managed
money" in commodities, "leveraged funds" in financials) hold long and short
in gold, oil, wheat, Treasuries and the dollar. It is the closest thing an
index has to insider activity -- not what one informed person did, but what
every large speculator is *currently betting*, official and free.

Three numbers go into the prompt, because the level alone is not a signal:

* **Net as a share of open interest.** Direction and size in one number,
  comparable across contracts of wildly different sizes.
* **The week-over-week change.** Positioning that is building means
  conviction arriving; positioning that is unwinding means it leaving.
* **Its percentile over the past year.** A crowded extreme is where
  positioning stops being confirmation and starts being a contrarian risk,
  and the model cannot know that from the level alone.

Two honest limits, stated in the prompt itself:

* A contract that stopped reporting is worse than one that never reported.
  The live audit found TLT matching a market whose most recent row is dated
  **February 2022** -- four and a half years old, printed as "positions as of"
  with no hint that it was not this week's. A series whose *newest* row is
  older than ``MAX_REPORT_AGE_DAYS`` is therefore treated as dead and the
  section omitted, which is the only honest reading of a contract that has
  been renamed or delisted. Judged on the newest row rather than row by row:
  dropping every old row would leave a month of history and destroy the
  52-week percentile, which is most of what this block is for.

* The data is **as of Tuesday, published Friday**, so it is three to six days
  stale by the time a cycle reads it. That is the dataset, not a bug.
* Positioning is a **crowding measure, not a forecast**. The prompt says so,
  because "managed money is very long" is as easily the top of a move as the
  middle of one.

Fetching is separated from parsing, as everywhere else here: the parser takes
a list of weekly rows and never touches the network.
"""

from __future__ import annotations

import logging
from dataclasses import asdict, dataclass
from datetime import date
from typing import Any, Iterable, Optional, Sequence

from orchestrator import formatting as fmt

log = logging.getLogger(__name__)

#: CFTC's public Socrata endpoints. No key is needed at this volume.
BASE_URL = "https://publicreporting.cftc.gov/resource"
#: Disaggregated report: physical commodities, with a "managed money" category.
DISAGGREGATED = "72hh-3qpy"
#: Traders in Financial Futures: rates, equity indices and currencies, with a
#: "leveraged funds" category that plays the same role.
FINANCIAL = "gpe5-46if"

#: Weeks of history pulled, for the percentile. A year plus a margin, so a
#: missing week or two still leaves a full 52 to rank against.
HISTORY_WEEKS = 60

#: How old the newest report may be before the series is treated as dead.
#: The CFTC publishes weekly, so a month covers a holiday and a late release;
#: past that the contract has been renamed or delisted and its last reading is
#: history rather than positioning.
MAX_REPORT_AGE_DAYS = 31

#: Below this many weeks the percentile is not reported rather than computed
#: from a handful of points and quietly believed.
MIN_WEEKS_FOR_PERCENTILE = 26

#: Candidate field spellings. Socrata column names have changed across CFTC
#: report revisions and differ between the two datasets, so every plausible
#: spelling is probed and the first present wins. A source that renames a
#: column should cost a gap, never a wrong number.
_FIELDS = {
    "date": ("report_date_as_yyyy_mm_dd", "report_date_as_yyyy_mm_dd_2", "report_date"),
    "open_interest": ("open_interest_all", "open_interest"),
    "managed_long": (
        "m_money_positions_long_all", "m_money_positions_long",
        "lev_money_positions_long", "lev_money_positions_long_all",
    ),
    "managed_short": (
        "m_money_positions_short_all", "m_money_positions_short",
        "lev_money_positions_short", "lev_money_positions_short_all",
    ),
}

#: Ticker -> (dataset, the contract's name in the report).
#:
#: Matched as a case-insensitive substring of ``market_and_exchange_names``,
#: which carries the exchange too ("GOLD - COMMODITY EXCHANGE INC."). Only
#: tickers with one dominant futures contract appear: DBC and DBA are baskets
#: spanning a dozen contracts with no single position to report, and a single
#: country fund has no future at all, so both are absent by design rather
#: than by oversight.
CONTRACTS: dict[str, tuple[str, str]] = {
    # Physical commodities -- managed money
    "GLD": (DISAGGREGATED, "GOLD"),
    "SLV": (DISAGGREGATED, "SILVER"),
    "CPER": (DISAGGREGATED, "COPPER"),
    "USO": (DISAGGREGATED, "CRUDE OIL, LIGHT SWEET"),
    "UNG": (DISAGGREGATED, "NATURAL GAS"),
    "CORN": (DISAGGREGATED, "CORN"),
    "WEAT": (DISAGGREGATED, "WHEAT-SRW"),
    "SOYB": (DISAGGREGATED, "SOYBEANS"),
    "CANE": (DISAGGREGATED, "SUGAR NO. 11"),
    # Rates, currencies and equity indices -- leveraged funds
    "TLT": (FINANCIAL, "ULTRA U.S. TREASURY BONDS"),
    "IEF": (FINANCIAL, "10-YEAR U.S. TREASURY NOTES"),
    "SHY": (FINANCIAL, "2-YEAR U.S. TREASURY NOTES"),
    "TIP": (FINANCIAL, "10-YEAR U.S. TREASURY NOTES"),
    "UUP": (FINANCIAL, "U.S. DOLLAR INDEX"),
    "RSP": (FINANCIAL, "E-MINI S&P 500"),
    "IWM": (FINANCIAL, "RUSSELL E-MINI"),
    "VWO": (FINANCIAL, "MSCI EM INDEX"),
    "VGK": (FINANCIAL, "MSCI EAFE"),
    "EWJ": (FINANCIAL, "NIKKEI STOCK AVERAGE"),
}


def contract_for(ticker: str) -> Optional[tuple[str, str]]:
    """The dataset and contract name for a ticker, or ``None`` if it has none."""
    return CONTRACTS.get(ticker.strip().upper())


def _field(row: dict, key: str) -> Any:
    for name in _FIELDS[key]:
        if name in row and not fmt.is_missing(row[name]):
            return row[name]
    return None


def _number(value: Any) -> Optional[float]:
    if fmt.is_missing(value):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def net_share(row: dict) -> Optional[float]:
    """Managed-money net position as a share of open interest, for one week."""
    long_, short = _number(_field(row, "managed_long")), _number(_field(row, "managed_short"))
    interest = _number(_field(row, "open_interest"))
    if long_ is None or short is None or not interest:
        return None
    return (long_ - short) / interest


def percentile(value: float, history: Sequence[float]) -> Optional[float]:
    """Where ``value`` ranks in ``history``, 0.0 to 1.0.

    The share of past weeks at or below it -- so 0.95 means "more bullish
    than 95% of the past year", which is the sentence the prompt wants.
    """
    points = [p for p in history if p is not None]
    if len(points) < MIN_WEEKS_FOR_PERCENTILE:
        return None
    return sum(1 for p in points if p <= value) / len(points)


@dataclass(frozen=True)
class PositioningSnapshot:
    """What the large speculators are holding, and how unusual that is."""

    ticker: str = ""
    contract: str = ""
    as_of: str = ""
    net_share: Optional[float] = None
    week_change: Optional[float] = None
    year_percentile: Optional[float] = None
    weeks_of_history: int = 0
    open_interest: Optional[float] = None

    def as_dict(self) -> dict:
        return asdict(self)

    def _crowding(self) -> str:
        if self.year_percentile is None:
            return f"not enough history to rank ({self.weeks_of_history} weeks)"
        rank = self.year_percentile
        if rank >= 0.9:
            note = "a crowded long by the standards of the past year"
        elif rank <= 0.1:
            note = "a crowded short by the standards of the past year"
        else:
            note = "within its normal range"
        return f"{rank:.0%} percentile over 52 weeks -- {note}"

    def as_lines(self) -> list[str]:
        direction = "net long" if (self.net_share or 0) >= 0 else "net short"
        return [
            f"Contract: {self.contract} (positions as of {self.as_of or fmt.NA}, "
            "published the following Friday)",
            f"Large speculators: {direction} "
            f"{fmt.pct(abs(self.net_share) if self.net_share is not None else None, signed=False)} "
            f"of open interest ({fmt.num(self.open_interest, 0)} contracts)",
            f"Change on the week: {fmt.pct(self.week_change)} of open interest",
            f"Crowding: {self._crowding()}",
            "Read this as crowding, not as a forecast: an extreme is as often "
            "the end of a move as the middle of one.",
        ]


def report_date(row: dict) -> Optional[date]:
    """The date a row was reported for, or ``None`` if it has none."""
    raw = _field(row, "date")
    if raw is None:
        return None
    text = str(raw).strip()[:10]
    try:
        return date.fromisoformat(text)
    except ValueError:
        return None


def _series_is_live(rows: Sequence[dict], today: Optional[date] = None) -> bool:
    """Whether this contract is still reporting, judged on its newest row.

    A series with no readable date anywhere is treated as live: the CFTC's two
    datasets spell their date column differently, and refusing every series
    over a spelling would silently empty sections that are working. Only a
    newest date that is *readable and old* disqualifies.
    """
    stamps = [stamp for stamp in (report_date(row) for row in rows) if stamp]
    if not stamps:
        return True
    return ((today or date.today()) - max(stamps)).days <= MAX_REPORT_AGE_DAYS


def build_snapshot(ticker: str, rows: Sequence[dict]) -> Optional[PositioningSnapshot]:
    """Parse weekly CFTC rows, newest first, into one snapshot.

    ``None`` when the rows carry no usable position, so the caller omits the
    section rather than printing a form of blanks.
    """
    contract = contract_for(ticker)
    if contract is None or not rows:
        return None

    # Judged on the newest row, not row by row. Filtering every old row would
    # leave five weeks of history and destroy the 52-week percentile, which is
    # most of what this block is for: the question is whether the *series* is
    # still reporting, and its newest row is the only thing that answers it.
    if not _series_is_live(rows):
        return None

    shares = [net_share(row) for row in rows]
    if not shares or shares[0] is None:
        return None

    latest = shares[0]
    previous = shares[1] if len(shares) > 1 else None
    history = [s for s in shares if s is not None]

    return PositioningSnapshot(
        ticker=ticker.strip().upper(),
        contract=contract[1],
        as_of=str(_field(rows[0], "date") or "")[:10],
        net_share=latest,
        week_change=(latest - previous) if previous is not None else None,
        year_percentile=percentile(latest, history),
        weeks_of_history=len(history),
        open_interest=_number(_field(rows[0], "open_interest")),
    )


def fetch_rows(ticker: str, client: Any = None, weeks: int = HISTORY_WEEKS) -> list[dict]:
    """Weekly rows for a ticker's contract, newest first. Raises on failure.

    The caller wraps this in the same ``_attempt`` that every other source
    goes through, so a CFTC outage costs a named gap and nothing else.
    """
    contract = contract_for(ticker)
    if contract is None:
        return []
    dataset, name = contract

    import httpx

    params = {
        "$where": f"upper(market_and_exchange_names) like '%{name.upper()}%'",
        "$order": "report_date_as_yyyy_mm_dd DESC",
        "$limit": str(weeks),
    }
    url = f"{BASE_URL}/{dataset}.json"
    if client is None:
        with httpx.Client(timeout=30.0) as fresh:
            response = fresh.get(url, params=params)
    else:
        response = client.get(url, params=params)
    response.raise_for_status()
    payload = response.json()
    return [row for row in payload if isinstance(row, dict)]


__all__ = [
    "PositioningSnapshot",
    "CONTRACTS",
    "contract_for",
    "build_snapshot",
    "fetch_rows",
    "report_date",
    "MAX_REPORT_AGE_DAYS",
    "net_share",
    "percentile",
    "BASE_URL",
    "DISAGGREGATED",
    "FINANCIAL",
]
