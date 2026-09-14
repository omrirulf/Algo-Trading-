"""Deterministic, pure-Python risk math. No I/O, no SDKs, no secrets.

Every function here is a plain function of its arguments so the guardrails
can be proven with unit tests (see ``tests/test_risk_engine.py``).
"""

from __future__ import annotations

import math
from typing import Any, Sequence

from config import settings as cfg
from config.instruments import InstrumentKind, group_for, kind_for


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


def max_position_pct_for(ticker: str) -> float:
    """The equity cap that applies to this ticker, from its instrument kind.

    Resolved from ``config.instruments`` and nothing else. The signal has no
    say: ``LLMSignal`` carries no instrument field, and if it did, a model
    could enlarge its own position cap by claiming a name was a fund. An
    unrecognised ticker gets the single-name cap, which is never the largest
    of the three.
    """
    kind = kind_for(ticker)
    if kind is InstrumentKind.BROAD_FUND:
        return cfg.MAX_BROAD_FUND_PCT
    if kind is InstrumentKind.COMMODITY_FUND:
        return cfg.MAX_COMMODITY_FUND_PCT
    return cfg.MAX_POSITION_PCT


def _headroom(equity: float, used: float, cap_pct: float, label: str) -> float:
    if equity <= 0:
        raise RiskViolation(f"equity must be positive, got {equity}")
    if used < 0:
        raise RiskViolation(f"{label} exposure cannot be negative, got {used}")
    if not 0 < cap_pct <= 1:
        raise RiskViolation(f"{label} cap must be in (0, 1], got {cap_pct}")
    return max(0.0, equity * cap_pct - used)


def exposure_group_headroom(
    equity: float,
    ticker: str,
    positions: Sequence[Any],
    max_group_pct: float = cfg.MAX_EXPOSURE_GROUP_PCT,
) -> float:
    """Dollars still deployable into this ticker's exposure group.

    The check that makes a diversified watchlist produce a diversified book.
    Per-ticker caps never noticed five technology names opened on one morning;
    this does, and it spans both sleeves, so an oil driller and two energy
    funds count against the same group.

    ``positions`` is anything with ``.ticker`` and ``.market_value``.
    """
    group = group_for(ticker)
    used = sum(
        p.market_value for p in positions if group_for(p.ticker) == group
    )
    return _headroom(equity, used, max_group_pct, f"group {group!r}")


def sleeve_headroom(
    equity: float,
    ticker: str,
    positions: Sequence[Any],
    single_name_pct: float = cfg.MAX_SINGLE_NAME_SLEEVE_PCT,
    fund_pct: float = cfg.MAX_FUND_SLEEVE_PCT,
) -> float:
    """Dollars still deployable into this ticker's sleeve.

    Funds are the core and single names the satellite. That ordering is the
    point of these budgets rather than a side effect: a broad fund is
    diversified by construction, and a stock-picking edge is unproven here.
    """
    wants_equity = kind_for(ticker) is InstrumentKind.EQUITY
    used = sum(
        p.market_value
        for p in positions
        if (kind_for(p.ticker) is InstrumentKind.EQUITY) == wants_equity
    )
    cap = single_name_pct if wants_equity else fund_pct
    return _headroom(equity, used, cap, "single name" if wants_equity else "fund")


def budget_ceiling_for(
    equity: float, ticker: str, positions: Sequence[Any]
) -> tuple[float, str]:
    """The tightest of the three portfolio limits, and which one it was.

    Returned together so a rejection can name the limit that actually bound,
    rather than reporting the gross cap when it was really the energy group.
    """
    candidates = (
        ("gross exposure", gross_exposure_headroom(
            equity, sum(p.market_value for p in positions))),
        (f"{group_for(ticker)!r} group", exposure_group_headroom(
            equity, ticker, positions)),
        ("sleeve budget", sleeve_headroom(equity, ticker, positions)),
    )
    label, room = min(candidates, key=lambda pair: pair[1])
    return room, label


def check_gross_exposure_limit(
    equity: float,
    open_position_value: float,
    incoming_notional: float,
    max_gross_pct: float = cfg.MAX_GROSS_EXPOSURE_PCT,
) -> bool:
    """True if adding ``incoming_notional`` keeps total exposure under the cap.

    The per-ticker caps alone do not bound the portfolio: ten positions at the
    ETF cap would be twice the account. This is the only check that looks at
    every holding at once, so it is what actually guarantees the cash floor.
    """
    if equity <= 0:
        raise RiskViolation(f"equity must be positive, got {equity}")
    if open_position_value < 0 or incoming_notional < 0:
        raise RiskViolation("exposure values cannot be negative")
    if not 0 < max_gross_pct <= 1:
        raise RiskViolation(f"max_gross_pct must be in (0, 1], got {max_gross_pct}")
    return open_position_value + incoming_notional <= equity * max_gross_pct + 1e-9


def gross_exposure_headroom(
    equity: float,
    open_position_value: float,
    max_gross_pct: float = cfg.MAX_GROSS_EXPOSURE_PCT,
) -> float:
    """Dollars still deployable under the gross cap; never negative.

    Returned rather than inferred by the caller so that sizing can be capped
    by the portfolio limit *before* rounding to whole shares, instead of
    placing an order and rejecting it afterwards.
    """
    if equity <= 0:
        raise RiskViolation(f"equity must be positive, got {equity}")
    return max(0.0, equity * max_gross_pct - open_position_value)


def calculate_position_size(
    equity: float,
    price: float,
    max_position_pct: float = cfg.MAX_POSITION_PCT,
    existing_position_value: float = 0.0,
    budget_ceiling: float | None = None,
) -> int:
    """Whole-share quantity such that new + existing exposure <= cap.

    The cap is enforced twice:

    1. On the dollar budget before rounding (``budget = cap - existing``).
    2. On the actual notional after rounding down to whole shares, as a belt-
       and-braces assertion that no arithmetic path can exceed the cap.

    ``budget_ceiling`` is a second, lower ceiling applied to the same budget --
    the portfolio's remaining gross-exposure headroom. It is applied *before*
    rounding so the whole-share result already respects the portfolio limit,
    rather than being sized first and rejected afterwards.

    Returns 0 when even a single share would breach either cap.
    """
    if equity <= 0:
        raise RiskViolation(f"equity must be positive, got {equity}")
    if price <= 0:
        raise RiskViolation(f"price must be positive, got {price}")
    if not 0 < max_position_pct <= 1:
        raise RiskViolation(f"max_position_pct must be in (0, 1], got {max_position_pct}")
    if existing_position_value < 0:
        raise RiskViolation("existing_position_value cannot be negative")

    if budget_ceiling is not None and budget_ceiling < 0:
        raise RiskViolation(f"budget_ceiling cannot be negative, got {budget_ceiling}")

    cap_dollars = equity * max_position_pct
    budget = cap_dollars - existing_position_value  # check 1: pre-rounding
    if budget_ceiling is not None:
        budget = min(budget, budget_ceiling)  # check 1b: portfolio-level
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
