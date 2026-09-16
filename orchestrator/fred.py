"""What the economy actually did, from the people who measure it.

``orchestrator.macro`` gives the market's own prices -- yields, the dollar,
volatility -- which are free and need no key. They say what traders think.
They do not say what happened: an inflation print, a jobs number, a claims
figure. Those are published by the Bureau of Labor Statistics and the
Department of Labor, and the Federal Reserve Bank of St. Louis puts them all
behind one free API.

Five numbers, chosen because each answers a question the price series cannot:

``inflation``
    CPI year on year. Asked for as ``pc1`` so the percentage arrives already
    computed rather than being derived here from index levels, where an
    off-by-one month would be invisible and wrong.
``unemployment``
    The rate. Monthly, and the single most watched release there is.
``jobless_claims``
    Weekly first-time claims. The only one of these that is *fresh* -- the
    others describe last month, this describes last week.
``policy_rate``
    The upper limit of the Fed's target range. What the Fed has actually set,
    against which the three-month yield in ``MACRO`` is the market's opinion.
``breakeven``
    The ten-year breakeven rate: what the market expects inflation to average
    over ten years, read off the gap between nominal and inflation-linked
    Treasuries. Backward-looking CPI says what happened; this says what is
    priced, which is the thing a bond fund actually trades.

Absent is not failed. With no key nothing is fetched, this module is handed
nothing, and the line is omitted -- the same rule as every other optional
source here. A key is a way to see more, never a thing the system depends on.

Pure parsing, like its siblings. ``orchestrator.sources`` does the fetching,
because it is the one module on this side permitted to read a credential: a
key that reached a snapshot would reach a prompt, and the journal those
prompts feed is committed to the repository every cycle.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from orchestrator import formatting as fmt

#: ``(series id, label, FRED units, how to render)``. ``pc1`` is FRED's
#: "percent change from a year ago" -- computing it here from index levels
#: would put an off-by-one month somewhere nobody would ever look.
SERIES = (
    ("CPIAUCSL", "inflation", "pc1", "percent"),
    ("UNRATE", "unemployment", "lin", "percent"),
    ("ICSA", "jobless_claims", "lin", "thousands"),
    ("DFEDTARU", "policy_rate", "lin", "percent"),
    ("T10YIE", "breakeven", "lin", "percent"),
)

#: A release this old is not news, it is history: the series was discontinued
#: or the fetch fell back to a stale cache. Monthly data can legitimately be
#: six weeks old, so the bar is generous.
MAX_RELEASE_AGE_DAYS = 120


@dataclass(frozen=True)
class Release:
    """One official number, and when it was for."""

    label: str = ""
    value: Optional[float] = None
    date: str = ""
    render: str = "percent"

    def as_text(self) -> str:
        if self.value is None:
            return f"{self.label} {fmt.NA}"
        if self.render == "thousands":
            shown = f"{self.value / 1000:,.0f}k"
        else:
            shown = f"{self.value:.1f}%"
        when = f" ({self.date})" if self.date else ""
        return f"{self.label.replace('_', ' ')} {shown}{when}"


def _observations(payload: Any) -> list[dict]:
    if not isinstance(payload, dict):
        return []
    rows = payload.get("observations")
    return [row for row in rows if isinstance(row, dict)] if isinstance(rows, list) else []


def parse_release(label: str, render: str, payload: Any) -> Optional[Release]:
    """The most recent *real* observation, or ``None``.

    FRED writes a missing value as the string ``"."`` rather than omitting the
    row, which floats to zero if read carelessly -- and an unemployment rate of
    0.0% is exactly the kind of usable-looking wrong number this project keeps
    finding. Rows are walked newest first until one parses.
    """
    for row in _observations(payload):
        raw = str(row.get("value", "")).strip()
        if not raw or raw == ".":
            continue
        try:
            value = float(raw)
        except ValueError:
            continue
        return Release(label=label, value=value, date=str(row.get("date") or ""),
                       render=render)
    return None


def build_releases(payloads: Optional[dict] = None) -> dict:
    """``{label: Release}`` from the raw observations, keyed by label.

    Pure, like its siblings: ``orchestrator.sources`` does the fetching,
    because it is the only module on this side allowed to hold a key.
    """
    out: dict = {}
    for _, label, _, render in SERIES:
        release = parse_release(label, render, (payloads or {}).get(label))
        if release is not None:
            out[label] = release
    return out


def as_lines(releases: Optional[dict]) -> list[str]:
    """The prompt lines for a set of releases, or none at all.

    Two lines rather than five: what was measured, and what is expected. A
    fifth blank line for a series that did not arrive would say less than
    leaving it out.
    """
    releases = releases or {}
    measured = [releases.get(k) for k in ("inflation", "unemployment", "jobless_claims")]
    priced = [releases.get(k) for k in ("policy_rate", "breakeven")]

    lines = []
    if any(measured):
        lines.append("Latest US data: " + " | ".join(r.as_text() for r in measured if r))
    if any(priced):
        parts = []
        if releases.get("policy_rate"):
            parts.append(f"Fed target {releases['policy_rate'].value:.2f}%")
        if releases.get("breakeven"):
            parts.append(
                f"market expects {releases['breakeven'].value:.1f}% inflation over 10 years"
            )
        lines.append("Policy and expectations: " + " | ".join(parts))
    return lines


__all__ = [
    "Release",
    "as_lines",
    "build_releases",
    "parse_release",
    "SERIES",
]
