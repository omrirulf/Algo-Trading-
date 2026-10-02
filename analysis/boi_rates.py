"""The shekel rate for every weekday: the Bank of Israel's, and every day that is not.

The owner's instruction of 2 Oct 2026: the shekel view uses "the Bank of
Israel representative rate (daily, from the Bank of Israel's public data;
use another source only for a missing day and count those days)", and the
tax rule says the same (``config.israel_tax``, rule f): the Bank of Israel's
representative rate on the trade date. So, for every weekday from the start
to the end, both included, the rate (shekels per dollar) comes from:

1. the Bank of Israel's representative rate (series RER_USD_ILS), from its
   public SDMX service (``BOI_URL``), when the Bank published one that day;
2. else, only for a day the Bank did not publish, the European Central
   Bank's reference rates for that same day, crossed through the euro:
   USD/ILS = (shekels per euro) / (dollars per euro) (``ECB_URL``);
3. else the Bank of Israel's latest earlier rate, "carried".

Every day from 2 or 3 is counted and listed (``RateTable.counts``,
``RateTable.fallback_days``) and printed with the table. A day that must be
carried with no Bank of Israel rate before it stops the run: a rate is
never made up.

Both services answer in CSV, and the date and value columns are found by
their names. An answer that is not CSV, that has lost one of those columns,
or that holds a value which cannot be a USD/ILS rate stops the run with a
clear error. So a change in either service fails the nightly step loudly
(and the funds then say there is no shekel view tonight) instead of giving
wrong numbers. The rates themselves are kept exactly as the services gave
them.

The table travels like the price table (``analysis/price_tape.py``):
``tape`` builds it in exactly that shape, consumer ``fx-rates``. Its SHA-256
(``rates_sha256`` in the line the CLI prints first) goes into git through
the caller's committed JSON; the table itself (``--with-table``, the last
line) goes into the scoring-prices artifact, which
``.github/workflows/scoring-prices.yml`` copies into the archive
(``store/scoring_prices.py``). ``load_tape`` rebuilds the table from a tape
and refuses one that does not hash to its own SHA-256.

The fetches are passed in (``build(boi=..., ecb=...)``,
``fetch_boi(start, end, get=...)``), so the tests run with no network.
Writes no file and holds no key: both services are public.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import math
import re
import sys
import time
from bisect import bisect_left
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from typing import Any, Callable, Final, Iterator, Optional

import httpx

from analysis import price_tape
from config import israel_tax

#: The Bank of Israel's public SDMX service: the representative USD/ILS rate,
#: one row per day the Bank published, as CSV.
BOI_URL: Final[str] = (
    "https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2/data/dataflow/BOI.STATISTICS/EXR/1.0/"
    "RER_USD_ILS?startperiod={start}&endperiod={end}&format=csv"
)
#: The European Central Bank's reference rates, shekels and dollars per euro,
#: as CSV. Read only for days the Bank of Israel did not publish.
ECB_URL: Final[str] = (
    "https://data-api.ecb.europa.eu/service/data/EXR/D.ILS+USD.EUR.SP00.A"
    "?startPeriod={start}&endPeriod={end}&format=csvdata"
)

#: Seconds one request may take, how many tries a fetch gets, and the pause
#: before a retry (times the try's number).
TIMEOUT_SECONDS: Final[float] = 30.0
ATTEMPTS: Final[int] = 3
PAUSE_SECONDS: Final[float] = 5.0
#: Calendar days of Bank of Israel rates read before the start, so a first
#: day that must be carried still has a Bank of Israel rate before it.
LOOKBACK_DAYS: Final[int] = 14
#: Shekels per dollar. The rate has stayed far inside this range for
#: decades, so a value outside it is a changed format (a rate per 100
#: dollars, or dollars per shekel), and the run stops.
PLAUSIBLE_RANGE: Final[tuple[float, float]] = (1.0, 10.0)

#: Where a day's rate came from, as ``RateTable.source`` and the tape's
#: ``instance`` name it.
BOI: Final[str] = "boi"
ECB: Final[str] = "ecb"
CARRIED: Final[str] = "carried"
SOURCES: Final[tuple[str, ...]] = (BOI, ECB, CARRIED)
#: The tape's ticker for each source, so the archive never mixes a fallback
#: day with a Bank of Israel day.
TICKERS: Final[dict[str, str]] = {BOI: "USDILS", ECB: "USDILS.ECB", CARRIED: "USDILS.CARRIED"}

#: The tape's consumer and the CLI line's kind.
CONSUMER: Final[str] = "fx-rates"
#: The tape's source: the primary one. A fallback day says so in its row.
SOURCE: Final[str] = "bank-of-israel"
#: A rate is one number a day: a close-only row.
KIND: Final[str] = "close"

#: The column names looked for, in order of preference (upper case).
DATE_COLUMNS: Final[tuple[str, ...]] = ("TIME_PERIOD", "DATE")
VALUE_COLUMNS: Final[tuple[str, ...]] = ("OBS_VALUE", "VALUE")
#: Value cells that mean "no rate that day" rather than a changed format.
_NO_VALUE: Final[frozenset[str]] = frozenset({"", "nan", "na"})
_DAY_TEXT = re.compile(r"(\d{4}-\d{2}-\d{2})(?:[T ].*)?")
_HEADERS: Final[dict[str, str]] = {"User-Agent": "Algo-Trading research (public rate table)",
                                   "Accept": "text/csv, */*"}

#: A fetch: ``url -> body``, or None when the service says it holds no data (HTTP 404).
Getter = Callable[[str], Optional[str]]
#: A source of rates: ``(start, end) -> {day: shekels per dollar}``.
Fetcher = Callable[[date, date], dict[date, float]]


class RateError(ValueError):
    """The rates could not be fetched, or did not read as rates. Never answered with a guessed number."""


@dataclass(frozen=True)
class DayRate:
    """One weekday's rate and where it came from (``BOI``, ``ECB`` or ``CARRIED``)."""

    day: date
    rate: float
    source: str


@dataclass(frozen=True)
class RateTable:
    """Every weekday from ``first`` to ``last``, each once, in order, with its rate and source."""

    entries: tuple[DayRate, ...]
    _index: dict = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        entries = tuple(self.entries)
        if not entries:
            raise RateError("a rate table needs at least one day")
        index: dict[date, DayRate] = {}
        previous: Optional[date] = None
        for entry in entries:
            day = entry.day
            if not isinstance(day, date) or isinstance(day, datetime) or day.weekday() >= 5:
                raise RateError(f"{day!r} is not a weekday")
            if previous is not None and day != _next_weekday(previous):
                raise RateError(f"the table is not every weekday in order: {previous} is followed by {day}")
            if entry.source not in SOURCES:
                raise RateError(f"{day}: unknown source {entry.source!r}")
            _check_rate(entry.rate, day, "the table")
            index[day] = entry
            previous = day
        object.__setattr__(self, "entries", entries)
        object.__setattr__(self, "_index", index)

    def _entry(self, day: date) -> DayRate:
        key = day.date() if isinstance(day, datetime) else day
        found = self._index.get(key)
        if found is None:
            raise KeyError(f"no rate for {day}: the table holds the weekdays from {self.first} to {self.last}")
        return found

    def rate(self, day: date) -> float:
        """The day's USD/ILS rate. KeyError for a day outside the table (or a weekend)."""
        return self._entry(day).rate

    def source(self, day: date) -> str:
        """Where the day's rate came from: ``"boi"``, ``"ecb"`` or ``"carried"``. KeyError as ``rate``."""
        return self._entry(day).source

    def counts(self) -> dict[str, int]:
        """How many days came from each source, every source named."""
        counted = {name: 0 for name in SOURCES}
        for entry in self.entries:
            counted[entry.source] += 1
        return counted

    def fallback_days(self) -> list[tuple[date, str]]:
        """Every day not from the Bank of Israel, and its source, in date order."""
        return [(entry.day, entry.source) for entry in self.entries if entry.source != BOI]

    @property
    def first(self) -> date:
        return self.entries[0].day

    @property
    def last(self) -> date:
        return self.entries[-1].day

    @property
    def days(self) -> tuple[date, ...]:
        return tuple(entry.day for entry in self.entries)

    def as_dict(self) -> dict[date, float]:
        """Day -> rate, in date order."""
        return {entry.day: entry.rate for entry in self.entries}

    def __len__(self) -> int:
        return len(self.entries)


# --------------------------------------------------------------------------- #
# Days and checks
# --------------------------------------------------------------------------- #


def weekdays(start: date, end: date) -> list[date]:
    """Every Monday to Friday from ``start`` to ``end``, both included."""
    days, day = [], start
    while day <= end:
        if day.weekday() < 5:
            days.append(day)
        day += timedelta(days=1)
    return days


def _next_weekday(day: date) -> date:
    day += timedelta(days=1)
    while day.weekday() >= 5:
        day += timedelta(days=1)
    return day


def _check_rate(value: Any, day: date, who: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise RateError(f"{who}: {day}'s rate {value!r} is not a number")
    low, high = PLAUSIBLE_RANGE
    if not low <= value <= high:
        raise RateError(f"{who}: {day}'s rate {value!r} cannot be shekels per dollar "
                        f"(outside {low} to {high}); has the format changed?")
    return value


def _day(text: Any, who: str, *, strict: bool = False) -> date:
    """An ISO date. ``strict``: exactly YYYY-MM-DD; otherwise a time after it is allowed."""
    match = _DAY_TEXT.fullmatch(text.strip()) if isinstance(text, str) else None
    if match is None or (strict and match.group(0) != match.group(1)):
        raise RateError(f"{who}: {text!r} is not an ISO date (YYYY-MM-DD)")
    try:
        return date.fromisoformat(match.group(1))
    except ValueError as exc:
        raise RateError(f"{who}: {text!r} is not a date ({exc})") from exc


def _put(out: dict[date, float], day: date, value: float, who: str) -> None:
    if day in out and out[day] != value:
        raise RateError(f"{who}: two different values for {day} ({out[day]!r} and {value!r})")
    out[day] = value


# --------------------------------------------------------------------------- #
# Parsing: tolerant of column order, loud about anything else
# --------------------------------------------------------------------------- #


def _csv(text: Any, who: str) -> tuple[list[str], list[list[str]]]:
    """The header (upper case) and the data rows of a CSV answer. Raises if it is not CSV."""
    if not isinstance(text, str) or not text.strip():
        raise RateError(f"{who}: the answer is empty, not CSV")
    body = text.lstrip("﻿").strip()
    first = body.splitlines()[0]
    if first.lstrip().startswith(("<", "{", "[")):
        raise RateError(f"{who}: the answer is not CSV (it begins {first[:60]!r})")
    delimiter = max(",;\t", key=first.count)
    if first.count(delimiter) == 0:
        raise RateError(f"{who}: the answer is not CSV (one column: {first[:60]!r})")
    try:
        rows = list(csv.reader(io.StringIO(body), delimiter=delimiter, strict=True))
    except csv.Error as exc:
        raise RateError(f"{who}: the answer is not CSV ({exc})") from exc
    header = [cell.strip().upper() for cell in rows[0]]
    return header, [row for row in rows[1:] if any(cell.strip() for cell in row)]


def _column(header: list[str], names: tuple[str, ...], who: str) -> int:
    for name in names:
        if name in header:
            return header.index(name)
    raise RateError(f"{who}: the answer has no {' or '.join(names)} column "
                    f"(its columns: {', '.join(header)[:300]}); has the format changed?")


def _observations(header: list[str], rows: list[list[str]], who: str,
                  extra: tuple[int, ...] = ()) -> Iterator[tuple[list[str], date, Optional[float]]]:
    """Each row with its date and its value (None: no rate that day).

    A row with more filled cells than the header has columns raises: its
    cells may have moved (a decimal comma, say), and a moved cell would
    give a wrong number, not an error.
    """
    when = _column(header, DATE_COLUMNS, who)
    value = _column(header, VALUE_COLUMNS, who)
    needed = max((when, value, *extra))
    for row in rows:
        if len(row) <= needed:
            raise RateError(f"{who}: a row has fewer cells than the header ({','.join(row)[:120]!r})")
        if any(cell.strip() for cell in row[len(header):]):
            raise RateError(f"{who}: a row has more cells than the header ({','.join(row)[:120]!r})")
        day = _day(row[when], who)
        text = row[value].strip()
        if text.lower() in _NO_VALUE:
            yield row, day, None
            continue
        try:
            number = float(text)
        except ValueError:
            raise RateError(f"{who}: {day}'s value {text!r} is not a number") from None
        if not math.isfinite(number) or number <= 0:
            raise RateError(f"{who}: {day}'s value {text!r} is not a positive number")
        yield row, day, number


def parse_boi(text: str) -> dict[date, float]:
    """The Bank of Israel's CSV answer as {day: shekels per dollar}. Raises ``RateError`` on a changed format."""
    who = "the Bank of Israel"
    header, rows = _csv(text, who)
    out: dict[date, float] = {}
    for _, day, number in _observations(header, rows, who):
        if number is not None:
            _put(out, day, _check_rate(number, day, who), who)
    return out


def parse_ecb(text: str) -> dict[date, float]:
    """The European Central Bank's CSV answer, crossed: {day: (ILS per EUR) / (USD per EUR)}.

    Only days with both rates; other currencies are skipped. Raises
    ``RateError`` on a changed format, or a rate that is not per euro.
    """
    who = "the European Central Bank"
    header, rows = _csv(text, who)
    currency = _column(header, ("CURRENCY",), who)
    denominator = header.index("CURRENCY_DENOM") if "CURRENCY_DENOM" in header else None
    extra = (currency,) if denominator is None else (currency, denominator)
    legs: dict[str, dict[date, float]] = {"ILS": {}, "USD": {}}
    for row, day, number in _observations(header, rows, who, extra):
        if denominator is not None and row[denominator].strip().upper() != "EUR":
            raise RateError(f"{who}: {day}'s rate is per {row[denominator]!r}, not per euro")
        code = row[currency].strip().upper()
        if code in legs and number is not None:
            _put(legs[code], day, number, who)
    return {day: _check_rate(legs["ILS"][day] / legs["USD"][day], day, who)
            for day in sorted(set(legs["ILS"]) & set(legs["USD"]))}


# --------------------------------------------------------------------------- #
# Fetching
# --------------------------------------------------------------------------- #


def http_get(url: str, *, client: Optional[httpx.Client] = None, attempts: int = ATTEMPTS,
             pause: Callable[[float], None] = time.sleep) -> Optional[str]:
    """The body of ``url``; None for HTTP 404 (the service holds no data for the query).

    Up to ``attempts`` tries for a network error, HTTP 429 or a 5xx answer;
    any other answer is final. Raises ``RateError`` when no try succeeds.
    """
    own = client is None
    if own:
        client = httpx.Client(timeout=TIMEOUT_SECONDS, follow_redirects=True, headers=_HEADERS)
    problem = "no try was made"
    try:
        for attempt in range(1, attempts + 1):
            try:
                response = client.get(url)
            except httpx.HTTPError as exc:
                problem = f"{type(exc).__name__}: {exc}"
            else:
                if response.status_code == 200:
                    return response.text
                if response.status_code == 404:
                    return None
                problem = f"HTTP {response.status_code}"
                if response.status_code != 429 and response.status_code < 500:
                    break
            if attempt < attempts:
                pause(PAUSE_SECONDS * attempt)
    finally:
        if own:
            client.close()
    raise RateError(f"could not fetch {url} ({problem})")


def fetch_boi(start: date, end: date, get: Optional[Getter] = None) -> dict[date, float]:
    """The Bank of Israel's published rates from ``start`` to ``end``. Raises ``RateError``."""
    body = (get or http_get)(BOI_URL.format(start=start.isoformat(), end=end.isoformat()))
    if body is None:
        raise RateError(f"the Bank of Israel holds no rates from {start} to {end} (HTTP 404); "
                        "has its address or series changed?")
    return parse_boi(body)


def fetch_ecb(start: date, end: date, get: Optional[Getter] = None) -> dict[date, float]:
    """The European Central Bank's crossed USD/ILS rates from ``start`` to ``end``; {} when it has none."""
    body = (get or http_get)(ECB_URL.format(start=start.isoformat(), end=end.isoformat()))
    return {} if body is None else parse_ecb(body)


def build(start: date, end: date, *, boi: Optional[Fetcher] = None,
          ecb: Optional[Fetcher] = None) -> RateTable:
    """Every weekday from ``start`` to ``end``: the Bank of Israel's rate, else the ECB's, else carried.

    ``boi`` and ``ecb`` default to ``fetch_boi`` and ``fetch_ecb``. The ECB
    is asked only when the Bank of Israel is missing a day, and only for the
    span of the missing days. Raises ``RateError`` when a fetch fails, an
    answer does not read as rates, or a day must be carried with no Bank of
    Israel rate before it.
    """
    if end < start:
        raise RateError(f"the end ({end}) is before the start ({start})")
    days = weekdays(start, end)
    if not days:
        raise RateError(f"there is no weekday from {start} to {end}")
    published = (boi or fetch_boi)(start - timedelta(days=LOOKBACK_DAYS), end)
    missing = [day for day in days if day not in published]
    crossed = (ecb or fetch_ecb)(missing[0], missing[-1]) if missing else {}
    earlier = sorted(published)
    entries = []
    for day in days:
        if day in published:
            entries.append(DayRate(day, float(published[day]), BOI))
        elif day in crossed:
            entries.append(DayRate(day, float(crossed[day]), ECB))
        else:
            before = bisect_left(earlier, day)
            if before == 0:
                raise RateError(f"{day}: neither the Bank of Israel nor the European Central Bank has a rate, "
                                f"and there is no earlier Bank of Israel rate to carry (looked back to "
                                f"{start - timedelta(days=LOOKBACK_DAYS)})")
            entries.append(DayRate(day, float(published[earlier[before - 1]]), CARRIED))
    return RateTable(tuple(entries))


# --------------------------------------------------------------------------- #
# The hand-over: the price table's shape
# --------------------------------------------------------------------------- #


def tape(table: RateTable, generated_at: datetime, final_through: Any) -> dict[str, Any]:
    """The table in ``analysis.price_tape``'s tape shape, so the archive's copy takes it unchanged.

    One close-only row a day: instance and ticker say the source
    (``TICKERS``), close is the rate, every other price is null. Rows are
    sorted by instance, ticker and date, and ``prices_sha256`` is
    ``price_tape.digest(rows)``.
    """
    stamp = generated_at.isoformat()
    rows = sorted(({"instance": entry.source, "kind": KIND, "ticker": TICKERS[entry.source],
                    "date": entry.day.isoformat(), "open": None, "high": None, "low": None,
                    "close": entry.rate, "dividends": None} for entry in table.entries),
                  key=lambda row: (row["instance"], row["ticker"], row["date"]))
    coverage: dict[str, dict] = {}
    for source in sorted({entry.source for entry in table.entries}):
        dated = [row for row in rows if row["instance"] == source]
        coverage[source] = {"kind": KIND, "tickers": {TICKERS[source]: {
            "first": dated[0]["date"], "last": dated[-1]["date"], "bars": len(dated), "fetched_at": stamp}}}
    return {
        "kind": "scoring-prices",
        "v": price_tape.TAPE_VERSION,
        "consumer": CONSUMER,
        "source": SOURCE,
        "generated_at": stamp,
        "final_through": final_through.isoformat() if hasattr(final_through, "isoformat") else final_through,
        "prices_sha256": price_tape.digest(rows),
        "coverage": coverage,
        "rows": rows,
    }


def load_tape(text: str) -> RateTable:
    """The table a tape holds. Raises ``RateError`` unless it is a rate tape that hashes to its ``prices_sha256``."""
    try:
        hand_over = json.loads(text)
    except (json.JSONDecodeError, TypeError) as exc:
        raise RateError(f"the rate table is not JSON: {exc}") from exc
    if not isinstance(hand_over, dict) or hand_over.get("kind") != "scoring-prices" \
            or hand_over.get("v") != price_tape.TAPE_VERSION:
        raise RateError("not a scoring-prices tape of this version")
    if hand_over.get("consumer") != CONSUMER:
        raise RateError(f"not a rate table (consumer {hand_over.get('consumer')!r})")
    rows = hand_over.get("rows")
    if not isinstance(rows, list) or not rows:
        raise RateError("the rate table has no rows")
    entries = []
    for row in rows:
        if not isinstance(row, dict) or set(row) != set(price_tape.ROW_KEYS):
            raise RateError("a row is not shaped like a price row")
        source = row["instance"]
        if source not in SOURCES or row["ticker"] != TICKERS[source] or row["kind"] != KIND:
            raise RateError(f"a row names no rate source ({source!r}, {row['ticker']!r}, {row['kind']!r})")
        if any(row[key] is not None for key in ("open", "high", "low", "dividends")):
            raise RateError(f"the row for {row['date']!r} holds more than a rate")
        rate = row["close"]
        if isinstance(rate, bool) or not isinstance(rate, (int, float)):
            raise RateError(f"the rate for {row['date']!r} is not a number")
        entries.append(DayRate(_day(row["date"], "the rate table", strict=True), float(rate), source))
    if price_tape.digest(rows) != hand_over.get("prices_sha256"):
        raise RateError("the rate table's rows do not hash to its prices_sha256")
    return RateTable(tuple(sorted(entries, key=lambda entry: entry.day)))


def summary(table: RateTable, hand_over: dict[str, Any]) -> dict[str, Any]:
    """The line the CLI prints first, which the caller commits: counts, fallback days and the hash."""
    return {
        "kind": CONSUMER,
        "source": israel_tax.FX_SOURCE,
        "fallback_source": israel_tax.FX_FALLBACK_SOURCE,
        "first": table.first.isoformat(),
        "last": table.last.isoformat(),
        "days": len(table),
        "counts": table.counts(),
        "fallback_days": [[day.isoformat(), source] for day, source in table.fallback_days()],
        "rates_sha256": hand_over["prices_sha256"],
        "generated_at": hand_over["generated_at"],
    }


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def _now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def _arg_day(text: str) -> date:
    try:
        return _day(text, "the argument", strict=True)
    except RateError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="analysis.boi_rates", description=__doc__.split("\n\n")[0])
    parser.add_argument("--start", type=_arg_day, required=True, help="the first day, YYYY-MM-DD")
    parser.add_argument("--end", type=_arg_day, required=True, help="the last day, YYYY-MM-DD (included)")
    parser.add_argument("--with-table", action="store_true",
                        help="also print the table itself, in the price table's shape, as one JSON line printed last")
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        table = build(args.start, args.end)
    except (ValueError, httpx.HTTPError, OSError) as exc:
        print(f"analysis.boi_rates: no rate table: {exc}", file=sys.stderr)
        return 1
    hand_over = tape(table, _now(), table.last)
    print(price_tape.dumps(summary(table, hand_over)))
    if args.with_table:
        print(price_tape.dumps(hand_over))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "ATTEMPTS", "BOI", "BOI_URL", "CARRIED", "CONSUMER", "DATE_COLUMNS", "DayRate", "ECB", "ECB_URL", "KIND",
    "LOOKBACK_DAYS", "PAUSE_SECONDS", "PLAUSIBLE_RANGE", "RateError", "RateTable", "SOURCE", "SOURCES", "TICKERS",
    "TIMEOUT_SECONDS", "VALUE_COLUMNS", "build", "fetch_boi", "fetch_ecb", "http_get", "load_tape", "main",
    "parse_boi", "parse_ecb", "summary", "tape", "weekdays",
]
