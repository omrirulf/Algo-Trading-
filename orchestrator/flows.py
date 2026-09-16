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

Two honest limits, both stated in the prompt rather than hidden:

* **It is not sentiment about price.** Creations follow demand for exposure,
  and a fund can bleed shares through a rally. Read it as conviction of
  flow, not as a forecast.
* **Yahoo's series is irregular.** Points arrive when they arrive, sometimes
  weekly and sometimes not for a fortnight, so every window reports the
  actual span it measured instead of pretending to the span it wanted.

Pure parsing, like its sibling modules: ``orchestrator.context`` does the
fetching and hands the series in.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Optional, Sequence

from orchestrator import formatting as fmt

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
    "MIN_POINTS",
]
