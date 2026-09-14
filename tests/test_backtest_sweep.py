"""The sweep must report its own limits, not just its numbers.

A parameter table is the easiest place in this project to produce something
that looks like evidence and isn't: signal-free trades have no edge to find,
so the returns column describes the price series. The report has to say so,
and thin samples have to be marked rather than printed bare.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from backtest import report
from backtest.simulate import MIN_WARMUP_BARS
from backtest.sweep import MIN_TRADES, Outcome, sweep_caps, sweep_multipliers
from config import settings as cfg
from tests.test_backtest_simulate import flat, frame


def wiggly(n: int = 400, seed: int = 3) -> pd.DataFrame:
    """A price series with enough movement to hit stops sometimes."""
    rng = np.random.default_rng(seed)
    close = 100 * np.exp(np.cumsum(rng.normal(0.0003, 0.02, n)))
    open_ = np.concatenate([[100.0], close[:-1]])
    high = np.maximum(open_, close) * 1.01
    low = np.minimum(open_, close) * 0.99
    return pd.DataFrame(
        {"Open": open_, "High": high, "Low": low, "Close": close},
        index=pd.bdate_range("2024-01-01", periods=n),
    )


# --- the mechanical findings ---------------------------------------------


def test_a_tighter_stop_is_hit_more_often():
    """The core finding the tool exists to produce."""
    outcomes = {o.label: o for o in sweep_multipliers(wiggly(), multipliers=(1.0, 3.0))}
    assert outcomes["1x ATR"].stop_hit_rate > outcomes["3x ATR"].stop_hit_rate


def test_a_wider_stop_risks_more_per_trade():
    """Wider stop, same cap: the quantity is unchanged, the distance is not."""
    outcomes = {o.label: o for o in sweep_multipliers(wiggly(), multipliers=(1.0, 3.0))}
    assert outcomes["3x ATR"].mean_risk_pct > outcomes["1x ATR"].mean_risk_pct


def test_a_bigger_cap_risks_more_per_trade():
    outcomes = {o.label: o for o in sweep_caps(wiggly(), caps=(0.02, 0.10))}
    assert outcomes["10% cap"].mean_risk_pct > outcomes["2% cap"].mean_risk_pct


def test_the_cap_does_not_change_whether_a_stop_is_hit():
    """Sizing and stop distance are independent; conflating them would mislead."""
    outcomes = {o.label: o for o in sweep_caps(wiggly(), caps=(0.02, 0.10))}
    assert outcomes["2% cap"].stop_hit_rate == outcomes["10% cap"].stop_hit_rate


def test_risk_per_trade_is_well_below_the_cap():
    """The headline correction: a 5% cap is not 5% at risk."""
    [outcome] = sweep_caps(wiggly(), caps=(0.05,))
    assert 0 < outcome.mean_risk_pct < 0.05


# --- honest reporting of thin data ---------------------------------------


def test_a_thin_sample_is_flagged():
    tiny = Outcome(label="2x ATR", trades=[])
    assert not tiny.enough
    assert tiny.n < MIN_TRADES


def test_rates_are_none_rather_than_zero_when_undefined():
    """Zero would read as 'never happened' rather than 'nothing to measure'."""
    empty = Outcome(label="2x ATR", trades=[])
    assert empty.stop_hit_rate is None
    assert empty.gap_rate is None
    assert empty.mean_risk_pct is None
    assert empty.median_return is None


def test_gap_rate_is_none_when_nothing_stopped_out():
    calm = frame(flat(MIN_WARMUP_BARS + 60, price=100.0, spread=0.5))
    [outcome] = sweep_multipliers(calm, multipliers=(4.0,))
    assert outcome.gap_rate is None


# --- the report ----------------------------------------------------------


def test_the_report_marks_the_current_setting():
    df = wiggly()
    text = report.render("T", len(df), sweep_multipliers(df), sweep_caps(df), "buy", 10)
    assert f"{cfg.ATR_STOP_MULTIPLIER:g}x ATR" in text
    assert "<- current" in text


def test_the_report_states_that_returns_are_not_an_edge():
    """The trap: reading the best median return as the best multiplier."""
    df = wiggly()
    text = report.render("T", len(df), sweep_multipliers(df), sweep_caps(df), "buy", 10)
    assert "no signal" in text
    assert "not about an edge" in text


def test_the_report_names_what_it_does_not_model():
    df = wiggly()
    text = report.render("T", len(df), sweep_multipliers(df), sweep_caps(df), "buy", 10)
    for omission in ("slippage", "commission", "MAX_OPEN_POSITIONS"):
        assert omission in text


def test_the_report_flags_thin_rows():
    thin = [Outcome(label="2x ATR", trades=[])]
    text = report.render("T", 10, thin, thin, "buy", 10)
    assert "(thin)" in text
    assert str(MIN_TRADES) in text


def test_the_report_renders_with_no_trades_at_all():
    empty = [Outcome(label="2x ATR", trades=[])]
    text = report.render("T", 0, empty, empty, "buy", 10)
    assert "n/a" in text


def test_the_report_explains_risk_per_trade():
    df = wiggly()
    text = report.render("T", len(df), sweep_multipliers(df), sweep_caps(df), "buy", 10)
    assert "does not put 5%" in text or "does not put" in text
