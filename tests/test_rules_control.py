"""The control arm is a coin flip that is the same coin flip every time."""

from __future__ import annotations

from datetime import date

from app.schemas import Bias
from config import settings as cfg
from rules import control


def test_it_always_takes_a_side():
    """A random NEUTRAL is a missing observation, not a control."""
    for i in range(50):
        sig = control.signal_for("NVDA", date(2026, 9, 1 + i % 28))
        assert sig.bias in (Bias.BULLISH, Bias.BEARISH)


def test_its_conviction_always_clears_the_floor():
    assert control.CONVICTION >= cfg.MIN_CONVICTION
    assert control.signal_for("NVDA", date(2026, 9, 21)).conviction == control.CONVICTION


def test_the_same_ticker_and_day_is_the_same_flip():
    """Seeded from the journal, not from a clock, so two runs of the race
    disagree only when the journal or the prices did."""
    a = control.signal_for("NVDA", date(2026, 9, 21))
    b = control.signal_for("NVDA", date(2026, 9, 21))
    assert a == b


def test_different_tickers_or_days_are_independent_flips():
    """Not a proof of independence -- a check that the seed actually varies."""
    flips = {
        (t, d): control.signal_for(t, date(2026, 9, d)).bias
        for t in ("NVDA", "XLE", "TLT", "GLD", "SPY")
        for d in range(1, 29)
    }
    assert len(set(flips.values())) == 2, "a seed that never varies is not a coin"


def test_a_missing_day_still_seeds_deterministically():
    assert control.signal_for("NVDA", None) == control.signal_for("NVDA", None)
