"""A journal made from prices only: one line per watchlist name per session, as production writes it.

Every line is what the cycle would have journalled for that name that day,
as far as prices alone can say it:

* **technicals**: ``orchestrator.technicals.build_snapshot`` -- the function
  production calls -- on the two calendar years of daily bars before the
  line's day (production fetches ``period="2y"``, ``orchestrator.context``),
  final closes only, **up to and including the previous session**;
* **live price**: there is none in the past, so the previous session's final
  close stands in for it (``live.price``), marked as a stand-in on every line
  (``live.source``). It is the price A's veto compares with its 200-day
  average and C's limit is set from;
* **no model**: ``signal`` is null. Nothing a model said, and nothing only a
  model reads (news, fundamentals, analysts, insiders), exists for the past.

One thing production has that history cannot give: the cycle runs during
the session, and yfinance's last daily row is then that session's partial
bar, so a live line's technicals run to the moment the cycle read them
(every line journalled so far has ``technicals.as_of`` equal to its own
day). Here they stop at the previous close, so a history line knows about
one session less than a live one; the report says so.

The line is stamped 15:00 UTC on its day, when the live cycles are
journalled (about 10:00-11:00 in New York), so every reader dates it, and
enters it, as it would a live line: the race and the funds enter at the open
of the next session. It is written one file per UTC month, the layout of
``logs/journal/`` (``config.journal_files``), and read back with
production's parser (``analysis.reader``), so the rules read exactly what
they would read from a live journal.

The journal is written only under the output directory a screen is given,
never under ``logs/``: it is not the record of anything that happened.
"""

from __future__ import annotations

import json
from dataclasses import replace
from datetime import date, datetime, time, timezone
from pathlib import Path
from typing import Final, Iterable, Optional, Sequence

import numpy as np
import pandas as pd

from analysis.reader import JournalEntry, read_lines
from config import journal_files
from config.watchlist import DEFAULT_WATCHLIST
from orchestrator.technicals import build_snapshot

#: Production's ``HISTORY_PERIOD = "2y"``: the technicals read two years of bars.
HISTORY_YEARS: Final[int] = 2
#: When a history line is stamped on its day: when the live cycles run.
LINE_TIME_UTC: Final[time] = time(15, 0)
#: The first day a line is made. Its technicals read the two years before it.
FIRST_LINE_DAY: Final[date] = date(2000, 1, 3)
#: What every line says in place of a live price.
STAND_IN: Final[str] = "history: the previous session's final close stands in for the live price"
GAP: Final[str] = ("history: technicals only; news, fundamentals, analysts, insiders and a model's answer "
                   "do not exist for the past")

_ORDER = {ticker: i for i, ticker in enumerate(DEFAULT_WATCHLIST)}


def two_years_before(day: date) -> date:
    """The same calendar day two years earlier (29 February becomes the 28th)."""
    try:
        return day.replace(year=day.year - HISTORY_YEARS)
    except ValueError:
        return day.replace(year=day.year - HISTORY_YEARS, day=28)


def stamp(day: date) -> datetime:
    return datetime.combine(day, LINE_TIME_UTC, tzinfo=timezone.utc)


def window(frame: pd.DataFrame, day: date, dates: Optional[np.ndarray] = None) -> pd.DataFrame:
    """The bars production's technicals would read on ``day``, less the partial one: (day - 2y, day)."""
    dates = frame.index.values if dates is None else dates
    lo = int(np.searchsorted(dates, np.datetime64(two_years_before(day)), side="right"))
    hi = int(np.searchsorted(dates, np.datetime64(day), side="left"))
    return frame.iloc[lo:hi]


def line(ticker: str, day: date, bars: pd.DataFrame) -> dict:
    """One journal line for ``ticker`` on ``day``, from ``bars`` (the window: final bars before ``day``)."""
    when = stamp(day)
    gaps = [GAP]
    technicals = None
    try:
        technicals = build_snapshot(bars).as_dict()
    except (ValueError, KeyError) as exc:
        # The cycle's own handling (orchestrator.context._build_technicals).
        gaps.append(f"technicals could not be computed: {exc}")
    previous = bars.index[-1].date()
    return {
        "ts_utc": when.isoformat(),
        "ticker": ticker,
        "context": {"ticker": ticker, "technicals": technicals, "gaps": gaps},
        "signal": None,
        "outcome": None,
        "error": None,
        "held": False,
        "live": {
            "price": float(bars["Close"].iloc[-1]),
            "bid": None,
            "ask": None,
            "quote_at": previous.isoformat(),
            "asked_at": when.isoformat(),
            "source": STAND_IN,
        },
        "history": {"technicals_through": previous.isoformat(), "live_price": "previous final close"},
    }


def lines_for_ticker(ticker: str, frame: pd.DataFrame, sessions: Sequence[date],
                     first: date = FIRST_LINE_DAY) -> list[tuple[date, str]]:
    """Every line for one ticker: each session from ``first`` on that has at least one bar before it."""
    if frame is None or frame.empty:
        return []
    dates = frame.index.values
    first_bar = frame.index[0].date()
    out = []
    for day in sessions:
        if day < first or day <= first_bar:
            continue
        bars = window(frame, day, dates)
        if bars.empty:
            continue
        out.append((day, json.dumps(line(ticker, day, bars))))
    return out


def _ticker_job(job: tuple) -> tuple[str, list[tuple[date, str]]]:
    ticker, frame, sessions, first = job
    return ticker, lines_for_ticker(ticker, frame, sessions, first)


def build(frames: dict[str, pd.DataFrame], sessions: Sequence[date], tickers: Sequence[str] = DEFAULT_WATCHLIST,
          first: date = FIRST_LINE_DAY, processes: int = 1) -> dict[str, list[str]]:
    """Every line, grouped by UTC month (``YYYY-MM``), in day then watchlist order."""
    jobs = [(t, frames.get(t), list(sessions), first) for t in tickers]
    if processes > 1:
        from multiprocessing import get_context

        with get_context("fork").Pool(processes) as pool:
            results = pool.map(_ticker_job, jobs, chunksize=1)
    else:
        results = [_ticker_job(job) for job in jobs]
    rows = [(day, _ORDER.get(ticker, len(_ORDER)), ticker, text)
            for ticker, lines in results for day, text in lines]
    rows.sort(key=lambda row: row[:3])
    months: dict[str, list[str]] = {}
    for day, _, _, text in rows:
        months.setdefault(f"{day:%Y-%m}", []).append(text)
    return months


def write(months: dict[str, list[str]], directory: Path) -> int:
    """One ``YYYY-MM.log`` per month, as ``logs/journal/``; returns the number of lines."""
    directory.mkdir(parents=True, exist_ok=True)
    count = 0
    for month, lines in sorted(months.items()):
        with (directory / f"{month}.log").open("w", encoding="utf-8") as handle:
            for text in lines:
                handle.write(text + "\n")
        count += len(lines)
    return count


def months_of(directory: Path, years: Optional[Iterable[int]] = None) -> list[Path]:
    """The journal's month files, oldest first; only those of ``years`` when given."""
    wanted = None if years is None else {f"{y:04d}-" for y in years}
    return [p for p in journal_files.parts(directory) if wanted is None or p.name[:5] in wanted]


def read(directory: Path, years: Optional[Iterable[int]] = None) -> list[JournalEntry]:
    """The journal's lines through production's parser; every one of them, or only ``years``'."""
    def lines() -> Iterable[str]:
        for part in months_of(directory, years):
            with part.open(encoding="utf-8") as handle:
                yield from handle

    parsed = read_lines(lines())
    if parsed.skipped:
        raise ValueError(f"{parsed.skipped} journal line(s) in {directory} could not be parsed")
    return parsed.entries


def as_answered(entries: Iterable[JournalEntry]) -> list[JournalEntry]:
    """The lines as the funds take them: every line counts as answered, NEUTRAL, at conviction 0.

    The funds act only on lines the model answered (``shadow.fund.lines_by_day``,
    the race's rule for a failed call). History has no model, so no line
    failed: each is marked answered with the only answer that says nothing.
    No rule fund reads it -- they recompute their own signal from the line's
    technicals -- and the file on disk keeps ``signal`` null.
    """
    return [replace(e, bias="NEUTRAL", conviction=0.0) for e in entries]


__all__ = ["FIRST_LINE_DAY", "GAP", "HISTORY_YEARS", "LINE_TIME_UTC", "STAND_IN", "as_answered", "build", "line",
           "lines_for_ticker", "months_of", "read", "stamp", "two_years_before", "window", "write"]
