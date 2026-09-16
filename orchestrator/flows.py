"""Who is actually buying a fund, measured in money rather than opinion.

A single name has insiders: the people who run the company, filing when they
buy their own shares. It is the one signal in the block that is nobody's
forecast -- it is somebody spending money and having to say so. A fund has no
insiders, and the slot stood empty.

It has something better suited to it. An ETF does not have a fixed share
count: when demand exceeds supply an authorised participant creates new
shares against a basket of the underlying, and when it falls away shares are
redeemed and destroyed. So the share count *is* the flow. A fund whose shares
outstanding grew 8% in a month had real money pushed into it by people who
had to deliver the underlying to get in, and unlike a rating or a target, it
has already happened.

Three windows, because they answer different questions: a week is
positioning, a month is a trend, a quarter is a regime. And the change is
quoted in dollars as well as percent, since 3% of a $70bn fund and 3% of a
$400m fund are not the same event.

Where the history comes from, and why it starts empty
----------------------------------------------------

Nowhere free publishes a share-count *series* for an ETF. Yahoo's
fundamentals-timeseries carries ``shares_out`` for companies and, the live
probe says flatly, for no fund on this watchlist: every one came back with an
empty series. What Yahoo does give is today's count -- sometimes as
``sharesOutstanding``, and otherwise derivable as net assets over NAV.

So this keeps its own. One reading per fund per cycle is appended to
``logs/fund_size.log``, which the heartbeat commits back to the repository
along with the journal, exactly as it already does for every signal. The
series is the project's own memory, and it has two consequences worth being
plain about:

* **It is empty on the first day and thin for a fortnight.** ``build_snapshot``
  returns ``None`` below three readings, so the section is simply absent until
  it can say something -- rather than present and saying nothing, which is the
  failure every module here was written to avoid.
* **A reading is only comparable to one measured the same way.** The two
  sources disagree: GLD reports ``sharesOutstanding`` of 260.3M while its net
  assets over NAV give 390.7M. Both are plausibly stale in different places,
  and it does not matter, because what is read here is the *change*. Mixing
  them would invent a 50% flow on the day the source changed, so each reading
  carries its source and only like is compared with like.

Two honest limits, both stated in the prompt rather than hidden:

* **It is not sentiment about price.** Creations follow demand for exposure,
  and a fund can bleed shares through a rally. Read it as conviction of
  flow, not as a forecast.
* **The series is irregular.** A cycle that failed, a market holiday or a
  changed source leaves a hole, so every window reports the actual span it
  measured instead of pretending to the span it wanted.

Pure parsing, like its sibling modules, plus the small append-only log that
makes the parsing possible: ``orchestrator.context`` does the fetching and
hands the series in.
"""

from __future__ import annotations

import json
import logging
from dataclasses import asdict, dataclass, field
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Optional, Sequence

from orchestrator import formatting as fmt

log = logging.getLogger(__name__)

#: The three windows, in days. Named in the prompt exactly as written here.
WINDOWS = (("1 week", 7), ("1 month", 30), ("3 months", 90))

#: How far a window may overshoot the span it names. Yahoo's series is
#: irregular, so a window takes the nearest point *at least* its own span
#: back -- which, for a fund that reports twice a year, would otherwise let
#: "1 week" be measured over two hundred days. Past this multiple the window
#: is dropped instead of relabelled, and the measured span is printed beside
#: every window that survives.
MAX_WINDOW_STRETCH = 2.5

#: Below this the change is noise -- share counts are rounded to blocks and a
#: fund can wobble a fraction of a percent on nothing at all.
FLAT_THRESHOLD = 0.005

#: Two points is a line, not a series. Below this the fund is reported as
#: having no usable flow history rather than as flat.
MIN_POINTS = 3

#: Where the accumulated readings live. JSON lines, one per fund per cycle,
#: committed back by the heartbeat alongside the signal journal.
LOG_NAME = "fund_size.log"

#: How a reading was measured. Never compared across sources -- see the
#: module docstring.
REPORTED = "reported"
DERIVED = "derived"

#: Readings older than this are dropped on read. The longest window is three
#: months; a year of history is generous and keeps the file small.
MAX_HISTORY_DAYS = 400


def _direction(change: Optional[float]) -> str:
    if change is None:
        return "unknown"
    if change > FLAT_THRESHOLD:
        return "money coming in"
    if change < -FLAT_THRESHOLD:
        return "money going out"
    return "flat"


@dataclass(frozen=True)
class FlowWindow:
    """One window's change, and the span actually measured."""

    label: str = ""
    change: Optional[float] = None
    dollars: Optional[float] = None
    days: Optional[int] = None

    def as_text(self) -> str:
        span = f" over {self.days}d" if self.days else ""
        money = f" ({fmt.money(self.dollars)})" if self.dollars is not None else ""
        return f"{self.label}: {fmt.pct(self.change)}{money}{span}"


@dataclass(frozen=True)
class FlowSnapshot:
    """Creations and redemptions, which is to say money in and money out."""

    ticker: str = ""
    shares: Optional[float] = None
    net_assets: Optional[float] = None
    points: int = 0
    windows: list[FlowWindow] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)

    @property
    def headline(self) -> Optional[FlowWindow]:
        """The month, or the longest window there is if the month is missing."""
        for label, _ in WINDOWS[1:]:
            for window in self.windows:
                if window.label == label:
                    return window
        return self.windows[0] if self.windows else None

    def as_lines(self) -> list[str]:
        headline = self.headline
        lines = [
            f"Direction: {_direction(headline.change if headline else None)}"
            + (f" ({headline.label})" if headline else "")
        ]
        if self.windows:
            lines.append("Share count change: " + " | ".join(w.as_text() for w in self.windows))
        else:
            lines.append(f"Share count change: {fmt.NA} (too few readings)")
        lines.append(
            f"Shares outstanding: {fmt.money(self.shares)} | "
            f"fund size: {fmt.money(self.net_assets)}"
        )
        lines.append(
            "Creations and redemptions are settled money, not an opinion -- but they "
            "follow demand for the exposure, so read them as conviction rather than "
            "as a forecast of price."
        )
        return lines


def _pairs(series: Any) -> list[tuple[Any, float]]:
    """``(timestamp, shares)`` pairs out of whatever Yahoo returned, sorted."""
    if series is None:
        return []
    items: Sequence = ()
    try:
        if isinstance(series, dict):
            items = list(series.items())
        elif hasattr(series, "items"):
            items = list(series.items())
        else:
            items = list(series)
    except Exception:  # noqa: BLE001 - an odd shape is no series
        return []
    out: list[tuple[Any, float]] = []
    for item in items:
        # A plain list of numbers unpacks to nothing usable, and a hostile
        # payload should cost a section rather than a cycle.
        try:
            stamp, value = item
        except (TypeError, ValueError):
            continue
        if fmt.is_missing(value):
            continue
        try:
            count = float(value)
        except (TypeError, ValueError):
            continue
        if count > 0:
            out.append((stamp, count))
    try:
        out.sort(key=lambda row: row[0])
    except TypeError:  # timestamps that will not compare to each other
        return []
    return out


def _days_between(earlier: Any, later: Any) -> Optional[int]:
    try:
        delta = later - earlier
    except Exception:  # noqa: BLE001
        return None
    days = getattr(delta, "days", None)
    if days is None:
        try:
            days = int(float(delta) / 86_400.0)
        except (TypeError, ValueError):
            return None
    return int(days)


def build_snapshot(
    ticker: str,
    shares_series: Any = None,
    price: Optional[float] = None,
) -> Optional[FlowSnapshot]:
    """Share-count flow for one fund, or ``None`` when there is none to read.

    ``None`` rather than a block of blanks: plenty of funds report their share
    count rarely or not at all, and a section saying nothing four different
    ways is worse than no section.
    """
    pairs = _pairs(shares_series)
    if len(pairs) < MIN_POINTS:
        return None

    latest_stamp, latest = pairs[-1]
    windows: list[FlowWindow] = []
    for label, span in WINDOWS:
        # The last point at least ``span`` days back, so a window is measured
        # over the period it names or longer -- never over less.
        candidates = [
            (stamp, count)
            for stamp, count in pairs[:-1]
            if (_days_between(stamp, latest_stamp) or 0) >= span
        ]
        if not candidates:
            continue
        then_stamp, then = candidates[-1]
        days = _days_between(then_stamp, latest_stamp)
        if not then or days is None or days > span * MAX_WINDOW_STRETCH:
            continue
        if any(window.days == days for window in windows):
            # Two labels that landed on the same reading are one fact printed
            # twice; the shorter label already said it.
            continue
        change = (latest - then) / then
        windows.append(FlowWindow(
            label=label,
            change=change,
            dollars=(latest - then) * price if price else None,
            days=days,
        ))

    return FlowSnapshot(
        ticker=ticker.strip().upper(),
        shares=latest,
        net_assets=latest * price if price else None,
        points=len(pairs),
        windows=windows,
    )


__all__ = [
    "FlowSnapshot",
    "FlowWindow",
    "build_snapshot",
    "WINDOWS",
    "FLAT_THRESHOLD",
    "MAX_WINDOW_STRETCH",
    "reading_from_info",
    "record",
    "series_from_log",
    "LOG_NAME",
    "REPORTED",
    "DERIVED",
    "MIN_POINTS",
]


# --------------------------------------------------------------------------- #
# The accumulated series
# --------------------------------------------------------------------------- #


def reading_from_info(info: Optional[dict]) -> tuple[Optional[float], str]:
    """Today's share count, and how it was arrived at.

    ``sharesOutstanding`` is preferred where a fund reports one. Where it does
    not -- TLT does not -- net assets over NAV gives the same quantity by
    definition. The source travels with the number because the two disagree
    and are never compared with each other.
    """
    info = info or {}
    reported = _positive(info.get("sharesOutstanding"))
    if reported is not None:
        return reported, REPORTED

    assets = _positive(info.get("totalAssets"))
    nav = _positive(info.get("navPrice"))
    if assets is not None and nav is not None:
        return assets / nav, DERIVED
    return None, DERIVED


def _positive(value: Any) -> Optional[float]:
    if fmt.is_missing(value):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if number > 0 else None


def record(ticker: str, shares: Optional[float], source: str, path: Any) -> bool:
    """Append one reading. Returns whether anything was written.

    Append-only and one line at a time, like every other log here: a cycle
    that dies halfway leaves a shorter file, never a corrupt one.
    """
    if shares is None or not ticker:
        return False
    line = json.dumps({
        "date": date.today().isoformat(),
        "ticker": ticker.strip().upper(),
        "shares": float(shares),
        "source": source,
    }, sort_keys=True)
    try:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(line + "\n")
    except OSError as exc:  # noqa: BLE001 - a lost reading is not a lost cycle
        log.warning("could not record fund size for %s: %s", ticker, exc)
        return False
    return True


def series_from_log(ticker: str, path: Any, source: Optional[str] = None) -> dict:
    """``{date: shares}`` for one fund, all measured the same way.

    ``source`` defaults to whichever the most recent reading used, so a fund
    that changed source mid-history reports the run since the change rather
    than a 50% flow on the day it switched.
    """
    wanted = ticker.strip().upper()
    rows: list[dict] = []
    try:
        with Path(path).open(encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except ValueError:
                    continue
                if isinstance(row, dict) and row.get("ticker") == wanted:
                    rows.append(row)
    except OSError:
        return {}
    if not rows:
        return {}

    if source is None:
        source = rows[-1].get("source", DERIVED)
    cutoff = date.today() - timedelta(days=MAX_HISTORY_DAYS)

    out: dict = {}
    for row in rows:
        if row.get("source") != source:
            continue
        shares = _positive(row.get("shares"))
        if shares is None:
            continue
        try:
            stamp = date.fromisoformat(str(row.get("date")))
        except (TypeError, ValueError):
            continue
        if stamp < cutoff:
            continue
        # A later line for the same day wins: a re-run corrects, it does not
        # add a second reading.
        out[stamp] = shares
    return dict(sorted(out.items()))
