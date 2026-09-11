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
