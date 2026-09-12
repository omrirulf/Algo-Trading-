"""Deterministic, pure-Python risk math. No I/O, no SDKs, no secrets.

Every function here is a plain function of its arguments so the guardrails
can be proven with unit tests (see ``tests/test_risk_engine.py``).
"""

from __future__ import annotations

import math

from config import settings as cfg


class RiskViolation(ValueError):
    """Raised when a signal cannot be turned into a compliant order."""


def check_conviction_threshold(
    conviction: float, min_conviction: float = cfg.MIN_CONVICTION
) -> bool:
    """True if the signal is confident enough to act on."""
    return conviction >= min_conviction


def check_position_count_limit(
    open_position_count: int, max_positions: int = cfg.MAX_OPEN_POSITIONS
) -> bool:
    """True if opening one more ticker would stay within the limit."""
    return open_position_count < max_positions


def calculate_position_size(
    equity: float,
    price: float,
    max_position_pct: float = cfg.MAX_POSITION_PCT,
    existing_position_value: float = 0.0,
) -> int:
    """Whole-share quantity such that new + existing exposure <= cap.

    The cap is enforced twice:

    1. On the dollar budget before rounding (``budget = cap - existing``).
    2. On the actual notional after rounding down to whole shares, as a belt-
       and-braces assertion that no arithmetic path can exceed the cap.

    Returns 0 when even a single share would breach the cap.
    """
    if equity <= 0:
        raise RiskViolation(f"equity must be positive, got {equity}")
    if price <= 0:
        raise RiskViolation(f"price must be positive, got {price}")
    if not 0 < max_position_pct <= 1:
        raise RiskViolation(f"max_position_pct must be in (0, 1], got {max_position_pct}")
    if existing_position_value < 0:
        raise RiskViolation("existing_position_value cannot be negative")

    cap_dollars = equity * max_position_pct
    budget = cap_dollars - existing_position_value  # check 1: pre-rounding
    if budget <= 0:
        return 0

    qty = math.floor(budget / price)
    if qty < cfg.MIN_ORDER_QTY:
        return 0

    # check 2: post-rounding. floor() can only reduce notional, but assert
    # anyway so a future edit can't silently break the invariant.
    notional = qty * price
    if notional + existing_position_value > cap_dollars + 1e-9:
        raise RiskViolation(
            f"post-rounding notional {notional:.2f} + existing "
            f"{existing_position_value:.2f} exceeds cap {cap_dollars:.2f}"
        )
    return qty


def calculate_stop_price(
    entry_price: float,
    atr: float,
    side: str,
    multiplier: float = cfg.ATR_STOP_MULTIPLIER,
) -> float:
    """ATR-based stop: ``entry -/+ multiplier * ATR`` for long/short.

    Rounded to cents. Raises if the result would be non-positive (which can
    only happen with an absurd ATR relative to price) so a nonsensical stop
    can never reach the broker.
    """
    if entry_price <= 0:
        raise RiskViolation(f"entry_price must be positive, got {entry_price}")
    if atr <= 0:
        raise RiskViolation(f"atr must be positive, got {atr}")
    if multiplier <= 0:
        raise RiskViolation(f"multiplier must be positive, got {multiplier}")

    distance = multiplier * atr
    if side == "buy":
        stop = entry_price - distance
    elif side == "sell":
        stop = entry_price + distance
    else:
        raise RiskViolation(f"side must be 'buy' or 'sell', got {side!r}")

    stop = round(stop, 2)
    if stop <= 0:
        raise RiskViolation(
            f"stop {stop} is non-positive (entry={entry_price}, atr={atr}, mult={multiplier})"
        )
    return stop


def check_atr_sanity(
    atr: float, price: float, min_pct: float = cfg.MIN_ATR_PCT_OF_PRICE
) -> bool:
    """False if ATR is so small relative to price that the stop is meaningless."""
    if price <= 0 or atr <= 0 or math.isnan(atr):
        return False
    return atr / price >= min_pct
