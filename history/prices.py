"""The daily prices a history screen reads: fetched once, kept as one table, hashed.

Every price in a screen comes from one table, fetched once through the same
yfinance call the race and the funds make (``analysis.baseline_compare.
OhlcFetcher``: daily bars, ``auto_adjust=False``), and cut to final closes
(``analysis.returns.last_final_session``). The table is written as one
gzipped CSV and its SHA-256 goes into the report, so any number in it can be
checked again on the prices it was computed from -- the same arrangement as
the funds' ``prices_sha256``.

``auto_adjust=False`` is what production reads: Yahoo's close adjusted for
splits and not for dividends, with the dividends in their own column. The
funds credit those dividends on the ex-date; the race, like the live race,
scores price moves only.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import io
import logging
import time
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Callable, Final, Iterable, Optional, Sequence

import pandas as pd

from analysis.returns import last_final_session
from config.watchlist import DEFAULT_WATCHLIST

log = logging.getLogger(__name__)

#: The calendar: the days SPY traded are the sessions (``history.sessions``).
CALENDAR_TICKER: Final[str] = "SPY"
#: The world index fund (the VT fund, and B's "in"), and B's "out": T-bills.
INDEX_TICKER: Final[str] = "VT"
BILLS_TICKER: Final[str] = "BIL"
#: Everything a screen of the rules running live reads: the watchlist as it is
#: today (so a fund or company that closed is missing: survivorship), plus the
#: calendar, the index and T-bills.
TICKERS: Final[tuple[str, ...]] = tuple(DEFAULT_WATCHLIST) + (CALENDAR_TICKER, INDEX_TICKER, BILLS_TICKER)
#: The first day fetched. The first journal line is in January 2000, and its
#: technicals read the two years before it (``history.journal``).
FIRST_FETCH: Final[date] = date(1997, 1, 1)

COLUMNS: Final[tuple[str, ...]] = ("Open", "High", "Low", "Close", "Volume", "Dividends")
_CSV_HEADER: Final[tuple[str, ...]] = ("ticker", "date", "open", "high", "low", "close", "volume", "dividends")

#: A fetch that fails is retried after these many seconds, then given up and
#: reported: a missing ticker is a line in the report, never a silent gap.
RETRY_WAITS: Final[tuple[float, ...]] = (2.0, 4.0, 8.0, 16.0)


@dataclass(frozen=True)
class PriceTable:
    """One frame per ticker (``COLUMNS``, a date index), and where they came from."""

    frames: dict[str, pd.DataFrame]
    #: The last session whose bar is a final close when the table was fetched.
    final_through: date
    fetched_at: str
    #: Tickers asked for that came back empty, after every retry.
    missing: tuple[str, ...] = ()

    def first_bar(self, ticker: str) -> Optional[date]:
        frame = self.frames.get(ticker)
        return None if frame is None or frame.empty else frame.index[0].date()


def _as_day(value: object) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    return pd.Timestamp(value).date()


def normalise(frame: Optional[pd.DataFrame], final_through: date) -> pd.DataFrame:
    """A vendor frame as the table keeps it: the six columns, one row per exchange date, final bars only.

    Rows with a missing open, high, low or close are dropped, as
    ``OhlcFetcher`` drops them; a missing volume or dividend reads as 0.
    """
    if frame is None or frame.empty or any(c not in frame.columns for c in ("Open", "High", "Low", "Close")):
        return pd.DataFrame(columns=list(COLUMNS), index=pd.DatetimeIndex([]))
    frame = frame.dropna(subset=["Open", "High", "Low", "Close"])
    out = pd.DataFrame(
        {c: (frame[c].astype("float64").to_numpy() if c in frame.columns else 0.0) for c in COLUMNS},
        index=pd.DatetimeIndex([pd.Timestamp(_as_day(ts)) for ts in frame.index]),
    )
    out[["Volume", "Dividends"]] = out[["Volume", "Dividends"]].fillna(0.0)
    out = out[~out.index.duplicated(keep="last")].sort_index()
    return out[out.index <= pd.Timestamp(final_through)]


def _yahoo(ticker: str, start: date, end: date) -> Optional[pd.DataFrame]:
    """The race's own call (``OhlcFetcher._fetch``), over the whole window at once."""
    import yfinance as yf

    return yf.Ticker(ticker).history(
        start=start.isoformat(),
        # yfinance treats ``end`` as exclusive.
        end=(end + timedelta(days=1)).isoformat(),
        interval="1d",
        auto_adjust=False,
    )


def fetch(
    tickers: Sequence[str] = TICKERS, *, start: date = FIRST_FETCH, now: Optional[datetime] = None,
    source: Callable[[str, date, date], Optional[pd.DataFrame]] = _yahoo,
    sleep: Callable[[float], None] = time.sleep,
) -> PriceTable:
    """Every ticker from ``start`` to the last final close, retried, and the ones that never came."""
    now = now or datetime.now(timezone.utc)
    final_through = last_final_session(now)
    frames: dict[str, pd.DataFrame] = {}
    missing: list[str] = []
    for ticker in dict.fromkeys(t.strip().upper() for t in tickers):
        frame = None
        for attempt, wait in enumerate((0.0, *RETRY_WAITS)):
            if wait:
                sleep(wait)
            try:
                frame = normalise(source(ticker, start, final_through), final_through)
            except Exception as exc:  # noqa: BLE001 - one ticker's failure is one ticker's line
                log.warning("%s: fetch %d failed: %s", ticker, attempt + 1, exc)
                frame = None
            if frame is not None and not frame.empty:
                break
        if frame is None or frame.empty:
            missing.append(ticker)
            continue
        frames[ticker] = frame
        log.info("%s: %d bars from %s", ticker, len(frame), frame.index[0].date())
    return PriceTable(frames, final_through, now.isoformat(timespec="seconds"), tuple(missing))


# --------------------------------------------------------------------------- #
# The table on disk
# --------------------------------------------------------------------------- #


def to_csv(table: PriceTable) -> str:
    """The table as CSV text, tickers in order, every float at full precision (``repr``)."""
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(_CSV_HEADER)
    for ticker in sorted(table.frames):
        frame = table.frames[ticker]
        for stamp, row in zip(frame.index, frame.itertuples(index=False)):
            writer.writerow((ticker, stamp.date().isoformat(), *(repr(float(v)) for v in row)))
    return buffer.getvalue()


def sha256_of(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def save(table: PriceTable, path: Path) -> str:
    """Write the table as gzipped CSV (the same bytes every time) and return the CSV's SHA-256."""
    text = to_csv(table)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", mtime=0) as handle:
        handle.write(text.encode("utf-8"))
    meta = {"final_through": table.final_through.isoformat(), "fetched_at": table.fetched_at,
            "missing": list(table.missing), "sha256": sha256_of(text)}
    path.with_suffix("").with_suffix(".meta.json").write_text(_json(meta), encoding="utf-8")
    return meta["sha256"]


def load(path: Path) -> tuple[PriceTable, str]:
    """The table written by ``save``, and its SHA-256 (checked against the one saved beside it)."""
    import json

    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        text = handle.read()
    meta = json.loads(path.with_suffix("").with_suffix(".meta.json").read_text(encoding="utf-8"))
    digest = sha256_of(text)
    if digest != meta["sha256"]:
        raise ValueError(f"{path}: SHA-256 {digest} is not the {meta['sha256']} saved with it")
    rows: dict[str, list[list]] = {}
    for record in csv.DictReader(io.StringIO(text)):
        rows.setdefault(record["ticker"], []).append(
            [record["date"], *(float(record[c]) for c in _CSV_HEADER[2:])])
    frames = {}
    for ticker, values in rows.items():
        index = pd.DatetimeIndex([pd.Timestamp(v[0]) for v in values])
        frames[ticker] = pd.DataFrame([v[1:] for v in values], index=index, columns=list(COLUMNS))
    table = PriceTable(frames, date.fromisoformat(meta["final_through"]), meta["fetched_at"],
                       tuple(meta.get("missing", ())))
    return table, digest


def _json(value: object) -> str:
    import json

    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def coverage(table: PriceTable, tickers: Iterable[str] = DEFAULT_WATCHLIST) -> list[dict]:
    """Each ticker's first and last bar and its number of bars: what the screen could see of it."""
    out = []
    for ticker in tickers:
        frame = table.frames.get(ticker)
        if frame is None or frame.empty:
            out.append({"ticker": ticker, "first": None, "last": None, "bars": 0})
            continue
        out.append({"ticker": ticker, "first": frame.index[0].date().isoformat(),
                    "last": frame.index[-1].date().isoformat(), "bars": int(len(frame))})
    return out


__all__ = ["BILLS_TICKER", "CALENDAR_TICKER", "COLUMNS", "FIRST_FETCH", "INDEX_TICKER", "PriceTable", "TICKERS",
           "coverage", "fetch", "load", "normalise", "save", "sha256_of", "to_csv"]
