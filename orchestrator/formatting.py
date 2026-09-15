"""Number formatting for the context block handed to the LLM.

Every helper renders a missing value as ``n/a`` rather than raising or dropping
the line. Telling the model explicitly what it does *not* have is the point: an
omitted line is indistinguishable from a neutral reading, and a model that
cannot tell the difference will happily invent the missing half of a thesis.
"""

from __future__ import annotations

import math
import numbers
from typing import Any

NA = "n/a"

_MAGNITUDES = ((1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K"))


def is_missing(value: Any) -> bool:
    """True for None and for the NaN/inf that yfinance sprinkles through its data.

    ``numbers.Real`` rather than ``(int, float)`` so numpy scalars, which
    pandas hands back from every ``.iloc``, are covered too.
    """
    if value is None:
        return True
    if isinstance(value, bool):
        return False
    if isinstance(value, numbers.Real):
        return not math.isfinite(float(value))
    # pandas' own missing scalars (``pd.NA``, ``pd.NaT``) are neither None nor
    # a Real, and ``float(pd.NA)`` raises rather than returning NaN. Matched
    # by type name so this module stays free of a pandas import. The first
    # live-data run with news died on exactly this: yfinance's insider rollup
    # carried ``<NA>`` for "% net shares purchased", it passed through here as
    # present, and ``pct()`` crashed on it inside the prompt builder.
    return type(value).__name__ in ("NAType", "NaTType")


def num(value: Any, digits: int = 2) -> str:
    """Plain number, e.g. ``234.50``."""
    if is_missing(value):
        return NA
    return f"{float(value):,.{digits}f}"


def pct(value: Any, digits: int = 1, signed: bool = True) -> str:
    """A fraction rendered as a percentage: ``0.061`` -> ``+6.1%``."""
    if is_missing(value):
        return NA
    sign = "+" if signed else ""
    return f"{float(value) * 100:{sign}.{digits}f}%"


def points(value: Any, digits: int = 1, signed: bool = False) -> str:
    """A value already expressed in percentage points: ``145.0`` -> ``145.0%``."""
    if is_missing(value):
        return NA
    sign = "+" if signed else ""
    return f"{float(value):{sign}.{digits}f}%"


def money(value: Any) -> str:
    """Abbreviated currency magnitude: ``3.52e12`` -> ``3.52T``."""
    if is_missing(value):
        return NA
    amount = float(value)
    sign = "-" if amount < 0 else ""
    amount = abs(amount)
    for threshold, suffix in _MAGNITUDES:
        if amount >= threshold:
            return f"{sign}{amount / threshold:,.2f}{suffix}"
    return f"{sign}{amount:,.2f}"


def ratio(value: Any, digits: int = 2) -> str:
    """Multiple of something, e.g. ``1.32x``."""
    if is_missing(value):
        return NA
    return f"{float(value):.{digits}f}x"


def clean(value: Any) -> Any:
    """Return ``value`` unless it is missing, in which case ``None``.

    Numbers are narrowed to plain ``float`` on the way through: snapshots get
    written to the JSON journal, and numpy scalars are not JSON-serialisable.
    Used at parse time so a NaN from yfinance never reaches a snapshot field
    and has to be re-checked at every use site.
    """
    if is_missing(value):
        return None
    if isinstance(value, numbers.Real) and not isinstance(value, bool):
        return float(value)
    return value
