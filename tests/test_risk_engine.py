"""Proves the 5% cap and ATR stop math hold, independent of any I/O."""

from __future__ import annotations

import math

import pytest

from app import risk_engine as re_
from config import settings as cfg


# --------------------------------------------------------------------------- #
# Position sizing: the 5% cap
# --------------------------------------------------------------------------- #


def test_cap_is_five_percent_in_config():
    assert cfg.MAX_POSITION_PCT == 0.05


def test_basic_size_is_floor_of_cap_over_price():
    # 5% of 100k = 5000; 5000 / 123.45 = 40.5 -> 40 shares
    assert re_.calculate_position_size(100_000, 123.45) == 40


@pytest.mark.parametrize(
    "equity,price",
    [
        (100_000, 1.0),
        (100_000, 3.33),
        (250_000, 999.99),
        (12_345.67, 0.07),
        (1_000_000, 4_999.0),
        (50_000, 2_500.0),  # exactly one share fits
        (50_000, 2_500.01),  # one share would breach by a cent
    ],
)
def test_notional_never_exceeds_cap(equity, price):
    qty = re_.calculate_position_size(equity, price)
    assert qty * price <= equity * cfg.MAX_POSITION_PCT + 1e-9
    # and it's the *largest* whole-share qty that fits
    assert (qty + 1) * price > equity * cfg.MAX_POSITION_PCT


def test_existing_position_counts_toward_cap():
    # cap = 5000, already holding 4000 -> budget 1000 -> 10 shares at 100
    assert re_.calculate_position_size(100_000, 100.0, existing_position_value=4_000) == 10


def test_existing_position_at_cap_yields_zero():
    assert re_.calculate_position_size(100_000, 100.0, existing_position_value=5_000) == 0


def test_existing_position_over_cap_yields_zero_not_negative():
    assert re_.calculate_position_size(100_000, 100.0, existing_position_value=9_000) == 0


def test_price_above_cap_yields_zero():
    assert re_.calculate_position_size(100_000, 5_000.01) == 0


def test_fractional_shares_never_returned():
    qty = re_.calculate_position_size(100_000, 333.33)
    assert isinstance(qty, int)


@pytest.mark.parametrize("equity", [0, -1])
def test_non_positive_equity_rejected(equity):
    with pytest.raises(re_.RiskViolation):
        re_.calculate_position_size(equity, 100.0)


@pytest.mark.parametrize("price", [0, -10.0])
def test_non_positive_price_rejected(price):
    with pytest.raises(re_.RiskViolation):
        re_.calculate_position_size(100_000, price)


@pytest.mark.parametrize("pct", [0, -0.05, 1.5])
def test_bad_cap_rejected(pct):
    with pytest.raises(re_.RiskViolation):
        re_.calculate_position_size(100_000, 100.0, max_position_pct=pct)


def test_negative_existing_rejected():
    with pytest.raises(re_.RiskViolation):
        re_.calculate_position_size(100_000, 100.0, existing_position_value=-1)


# --------------------------------------------------------------------------- #
# Stop-loss math
# --------------------------------------------------------------------------- #


def test_long_stop_is_entry_minus_multiplier_atr():
    assert re_.calculate_stop_price(100.0, 2.0, "buy", multiplier=2.0) == 96.0


def test_short_stop_is_entry_plus_multiplier_atr():
    assert re_.calculate_stop_price(100.0, 2.0, "sell", multiplier=2.0) == 104.0


def test_default_multiplier_comes_from_config():
    expected = round(150.0 - cfg.ATR_STOP_MULTIPLIER * 3.0, 2)
    assert re_.calculate_stop_price(150.0, 3.0, "buy") == expected


def test_stop_is_rounded_to_cents():
    stop = re_.calculate_stop_price(100.123456, 1.987654, "buy", multiplier=1.5)
    assert stop == round(stop, 2)


def test_long_stop_always_below_entry_and_short_always_above():
    for entry, atr in [(10, 0.1), (250.5, 4.2), (3.21, 0.05)]:
        assert re_.calculate_stop_price(entry, atr, "buy") < entry
        assert re_.calculate_stop_price(entry, atr, "sell") > entry


def test_stop_that_would_go_non_positive_is_rejected():
    with pytest.raises(re_.RiskViolation):
        re_.calculate_stop_price(1.0, 5.0, "buy", multiplier=2.0)


@pytest.mark.parametrize("atr", [0, -1.0])
def test_non_positive_atr_rejected(atr):
    with pytest.raises(re_.RiskViolation):
        re_.calculate_stop_price(100.0, atr, "buy")


def test_unknown_side_rejected():
    with pytest.raises(re_.RiskViolation):
        re_.calculate_stop_price(100.0, 1.0, "long")


# --------------------------------------------------------------------------- #
# Other gates
# --------------------------------------------------------------------------- #


def test_conviction_threshold_inclusive():
    assert re_.check_conviction_threshold(cfg.MIN_CONVICTION)
    assert re_.check_conviction_threshold(cfg.MIN_CONVICTION + 0.01)
    assert not re_.check_conviction_threshold(cfg.MIN_CONVICTION - 0.01)
    assert not re_.check_conviction_threshold(0.0)


def test_position_count_limit():
    assert re_.check_position_count_limit(0)
    assert re_.check_position_count_limit(cfg.MAX_OPEN_POSITIONS - 1)
    assert not re_.check_position_count_limit(cfg.MAX_OPEN_POSITIONS)
    assert not re_.check_position_count_limit(cfg.MAX_OPEN_POSITIONS + 5)


def test_atr_sanity():
    assert re_.check_atr_sanity(atr=1.0, price=100.0)
    assert not re_.check_atr_sanity(atr=0.01, price=100.0)
    assert not re_.check_atr_sanity(atr=0.0, price=100.0)
    assert not re_.check_atr_sanity(atr=math.nan, price=100.0)
    assert not re_.check_atr_sanity(atr=1.0, price=0.0)


# --------------------------------------------------------------------------- #
# Profit ladder arithmetic
# --------------------------------------------------------------------------- #


def test_r_is_the_entry_to_stop_distance():
    assert re_.initial_r(100.0, 96.0) == 4.0
    assert re_.initial_r(96.0, 100.0) == 4.0  # a short's stop is above


def test_r_must_be_positive():
    with pytest.raises(re_.RiskViolation):
        re_.initial_r(100.0, 100.0)


def test_r_multiple_is_signed_by_side():
    assert re_.r_multiple(100.0, 104.0, 4.0, "buy") == pytest.approx(1.0)
    assert re_.r_multiple(100.0, 96.0, 4.0, "buy") == pytest.approx(-1.0)
    assert re_.r_multiple(100.0, 96.0, 4.0, "sell") == pytest.approx(1.0)
    assert re_.r_multiple(100.0, 104.0, 4.0, "sell") == pytest.approx(-1.0)


@pytest.mark.parametrize("base,expected", [(1, 0), (2, 0), (3, 1), (4, 1), (5, 1), (9, 3), (10, 3), (100, 33)])
def test_tranche_size_floors(base, expected):
    assert re_.tranche_size(base, 1 / 3) == expected


def test_two_ladder_tranches_always_leave_a_runner():
    """The property the whole ladder rests on, checked across every plausible size."""
    for base in range(1, 500):
        taken = sum(re_.tranche_size(base, rung.take_fraction) for rung in cfg.PROFIT_LADDER)
        assert taken < base or base == 0, base


def test_the_ladder_fractions_sum_to_less_than_one():
    assert sum(r.take_fraction for r in cfg.PROFIT_LADDER) < 1.0


def test_the_ladder_rungs_are_ascending_and_the_stop_only_climbs():
    takes = [r.take_at_r for r in cfg.PROFIT_LADDER]
    stops = [r.stop_to_r for r in cfg.PROFIT_LADDER]
    assert takes == sorted(takes) and len(set(takes)) == len(takes)
    assert stops == sorted(stops)
    assert all(s < t for s, t in zip(stops, takes)), "a stop must sit below the rung that set it"


def test_stop_for_rung_moves_in_the_moneys_favour():
    assert re_.stop_for_rung(100.0, 4.0, "buy", 0.0) == 100.0
    assert re_.stop_for_rung(100.0, 4.0, "buy", 1.0) == 104.0
    assert re_.stop_for_rung(100.0, 4.0, "sell", 0.0) == 100.0
    assert re_.stop_for_rung(100.0, 4.0, "sell", 1.0) == 96.0


def test_tighter_stop_never_loosens():
    assert re_.tighter_stop(98.0, 100.0, "buy") == 100.0
    assert re_.tighter_stop(101.0, 100.0, "buy") == 101.0
    assert re_.tighter_stop(102.0, 100.0, "sell") == 100.0
    assert re_.tighter_stop(99.0, 100.0, "sell") == 99.0


def test_rungs_due_is_contiguous_and_ordered():
    assert re_.rungs_due(0.5, 0) == []
    assert re_.rungs_due(1.0, 0) == [0]
    assert re_.rungs_due(2.9, 0) == [0]
    assert re_.rungs_due(3.5, 0) == [0, 1]
    assert re_.rungs_due(3.5, 1) == [1]
    assert re_.rungs_due(3.5, 2) == []
    assert re_.rungs_due(10.0, 0) == [0, 1]


def test_the_floor_now_admits_what_the_model_actually_produces():
    """The three live cycles' directional calls sat between 0.30 and 0.58."""
    assert cfg.MIN_CONVICTION == pytest.approx(0.30)
    assert re_.check_conviction_threshold(0.30)
    assert not re_.check_conviction_threshold(0.29)
