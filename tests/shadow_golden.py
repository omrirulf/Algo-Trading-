"""A fixed journal and price table for proving that the funds did not move.

Not a test module (no ``test_`` prefix): ``tests/test_shadow_same_day.py``
builds the funds document from these inputs and compares every existing
fund's part of it with hashes recorded from the code BEFORE the dated short
refusals, the price-gap and held-name reports and the ``model_same_day``
fund were added (commit dc9fe11). The journal carries ``live`` records of
every kind -- in hours, after the close, failed, missing, quote-less -- and
held lines, so the new fund has everything to act on and the old code
simply ignored it.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timedelta, timezone

import numpy as np

from analysis.reader import JournalEntry
from shadow.market import Bars
from tests.test_shadow_fund import S, stamp
from tests.test_shadow_variants import NAMES, Walks, said, wider

#: The sessions the funds run over, and the refusals every fund reads.
SESSIONS = S[:40]
REFUSED = frozenset({"HYG", "XLE"})


def live_record(rng, bars, ticker, day) -> dict | None:
    """A ``live`` record as ``orchestrator/live_price.py`` writes one, of a drawn kind."""
    u = rng.rand()
    asked = datetime(day.year, day.month, day.day, 15, 0, 5, tzinfo=timezone.utc)
    if u < 0.05:
        return None                                               # a line written before the record existed
    if u < 0.12:
        return {"price": None, "bid": None, "ask": None, "quote_at": None, "asked_at": asked.isoformat(),
                "source": "alpaca-iex", "error": "timed out"}
    bar = bars.bar(ticker, day)
    base = bar[0] if bar is not None else 50.0
    price = round(base * (1 + rng.normal(0.0, 0.004)), 2)
    if u < 0.20:
        asked = asked + timedelta(hours=6, minutes=30)            # 21:30 UTC: after the New York close
    quoted = u >= 0.28
    return {"price": price, "bid": round(price * 0.9995, 2) if quoted else None,
            "ask": round(price * 1.0005, 2) if quoted else None, "quote_at": asked.isoformat(),
            "asked_at": asked.isoformat(), "source": "alpaca-iex"}


def golden_inputs():
    """(entries, bars) for the golden run.

    The made-up prices are rounded to 4 decimals, as real prices are. They
    are drawn with ``np.exp``, whose last bit depends on the CPU numpy runs
    on (it picks a vectorised version by the instructions the chip has), so
    unrounded they differ by a hair between two CI runners, and every hash
    with them. The funds themselves use no such function.
    """
    raw = wider()
    bars = Bars({t: raw._frames[t].round(4) for t in raw.tickers()})
    rng = np.random.RandomState(11)
    out = []
    for day in SESSIONS:
        for ticker in NAMES:
            u = rng.rand()
            if u < 0.08:
                out.append(JournalEntry(ticker=ticker, timestamp=stamp(day), held=True))
                continue
            out.append(said(ticker, day, bias=("BULLISH", "BEARISH", "NEUTRAL")[int(rng.rand() * 3)],
                            conviction=float(rng.choice([0.2, 0.35, 0.45, 0.55, 0.65, 0.85])),
                            live_record=live_record(rng, bars, ticker, day)))
    return out, bars


def canonical(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     allow_nan=False).encode()).hexdigest()


def golden_parts(refused=REFUSED, *, without_same_day: bool = False) -> dict[str, str]:
    """The hash of every part of the funds document, by name.

    ``without_same_day`` runs the same inputs with ``model_same_day`` left
    out of the exploratory funds, so a test can show, on whatever Python it
    runs on, that adding it changes no other part.
    """
    from shadow import run as shadow_run

    entries, bars = golden_inputs()
    build = shadow_run.exploratory_funds
    if without_same_day:
        shadow_run.exploratory_funds = lambda *a, **k: [f for f in build(*a, **k) if f.name != "model_same_day"]
    try:
        funds, checks = shadow_run.run_funds(entries, SESSIONS[0], SESSIONS[-1], Walks(bars), random_funds=2,
                                             processes=1, shortable_no=refused)
    finally:
        shadow_run.exploratory_funds = build
    parts = {f"row:{row['name']}": canonical(row) for row in funds["list"]}
    parts["days"] = canonical(funds["days"])
    parts["start"] = canonical(funds["start"])
    parts["band"] = canonical(funds["band"])
    parts["checks:coin"] = canonical(checks["coin"])
    return parts


__all__ = ["REFUSED", "SESSIONS", "canonical", "golden_inputs", "golden_parts", "live_record"]
