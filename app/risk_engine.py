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
    of the four.
    """
    kind = kind_for(ticker)
    if kind is InstrumentKind.BROAD_FUND:
        return cfg.MAX_BROAD_FUND_PCT
    if kind is InstrumentKind.FOCUSED_FUND:
        return cfg.MAX_FOCUSED_FUND_PCT
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
    max_group_pct: float | None = None,
) -> float:
    """Dollars still deployable into this ticker's exposure group.

    The check that makes a diversified watchlist produce a diversified book.
    Per-ticker caps never noticed five technology names opened on one morning;
    this does, and it spans both sleeves, so an oil driller and two energy
    funds count against the same group.

    A group in ``cfg.EXPOSURE_GROUP_CAP_OVERRIDES`` -- currently just
    Duration -- binds tighter than the general cap, because its members move
    on one number rather than merely sharing a theme. ``max_group_pct``
    overrides both when a caller passes one explicitly.

    ``positions`` is anything with ``.ticker`` and ``.market_value``.
    """
    group = group_for(ticker)
    cap_pct = (
        max_group_pct
        if max_group_pct is not None
        else cfg.EXPOSURE_GROUP_CAP_OVERRIDES.get(group, cfg.MAX_EXPOSURE_GROUP_PCT)
    )
    used = sum(
        p.market_value for p in positions if group_for(p.ticker) == group
    )
    return _headroom(equity, used, cap_pct, f"group {group!r}")


def groups_over_cap(equity: float, positions: Sequence[Any]) -> dict[str, float]:
    """Dollars each exposure group is over its own cap, for groups that are.

    ``exposure_group_headroom`` is an entry-time check: it stops a *new*
    order from pushing a group over its cap, and has nothing to say about a
    position already open. That is sufficient for a cap that has always
    applied, since nothing legitimately opened could have crossed it. It is
    not sufficient the day a cap tightens -- Duration's did, from 25% to
    10% -- because a position sized lawfully under yesterday's number does
    not shrink on its own just because today's is smaller. This is the
    read-only half of that check: what the position manager's group-cap
    trim acts on, and what a test can assert against without touching a
    broker.

    A group absent from the result is at or under its cap. Nothing here says
    whether it got there by never being tested against a cap this tight or
    by an entry-time rejection -- only that it is fine now.
    """
    if equity <= 0:
        raise RiskViolation(f"equity must be positive, got {equity}")
    used_by_group: dict[str, float] = {}
    for p in positions:
        group = group_for(p.ticker)
        used_by_group[group] = used_by_group.get(group, 0.0) + p.market_value
    excess_by_group: dict[str, float] = {}
    for group, used in used_by_group.items():
        cap_pct = cfg.EXPOSURE_GROUP_CAP_OVERRIDES.get(group, cfg.MAX_EXPOSURE_GROUP_PCT)
        excess = used - equity * cap_pct
        if excess > 0:
            excess_by_group[group] = excess
    return excess_by_group


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


# --------------------------------------------------------------------------- #
# Profit ladder -- pure arithmetic in units of R
# --------------------------------------------------------------------------- #
# R is the entry-to-initial-stop distance. Everything below is expressed in
# it so that one ladder fits every instrument kind, and none of it touches a
# broker: the position manager decides *what* from these, then acts.


def initial_r(entry_price: float, stop_price: float) -> float:
    """The distance the initial stop sat from the entry -- one R."""
    r = abs(entry_price - stop_price)
    if r <= 0:
        raise RiskViolation(f"R must be positive; entry {entry_price} stop {stop_price}")
    return r


def r_multiple(entry_price: float, current_price: float, r: float, side: str) -> float:
    """Unrealised gain in units of R, signed so that a winning trade is positive."""
    if r <= 0:
        raise RiskViolation(f"R must be positive, got {r}")
    move = current_price - entry_price
    return (move if side == "buy" else -move) / r


def tranche_size(base_qty: int, fraction: float) -> int:
    """Whole shares to close at a rung: ``floor(base * fraction)``.

    Floored rather than rounded so that the fractions in the ladder can never
    add up to the whole position through rounding -- the runner is
    guaranteed by arithmetic, not by hoping.
    """
    if base_qty < 0 or not 0 < fraction < 1:
        raise RiskViolation(f"bad tranche inputs: base {base_qty}, fraction {fraction}")
    return int(math.floor(base_qty * fraction))


def stop_for_rung(entry_price: float, r: float, side: str, stop_to_r: float) -> float:
    """Where a rung moves the stop: ``entry +/- stop_to_r * R``, in the money's favour."""
    if side not in ("buy", "sell"):
        raise RiskViolation(f"side must be 'buy' or 'sell', got {side!r}")
    offset = stop_to_r * r
    price = entry_price + offset if side == "buy" else entry_price - offset
    if price <= 0:
        raise RiskViolation(f"ratcheted stop would be non-positive: {price}")
    return round(price, 2)


def tighter_stop(current: float, proposed: float, side: str) -> float:
    """Whichever of two stops protects more. A ratchet never loosens.

    For a long that is the higher price; for a short, the lower. Calling this
    on every proposed move is what makes the ladder monotone regardless of
    the order rungs are evaluated in.
    """
    if side == "buy":
        return max(current, proposed)
    if side == "sell":
        return min(current, proposed)
    raise RiskViolation(f"side must be 'buy' or 'sell', got {side!r}")


def rungs_due(gain_r: float, rungs_taken: int, ladder=cfg.PROFIT_LADDER) -> list[int]:
    """Indices of the rungs a position has reached but not yet taken, in order.

    Contiguous from ``rungs_taken``: a gap that clears two rungs at once
    returns both, and a rung is never returned out of order.
    """
    due: list[int] = []
    for index in range(rungs_taken, len(ladder)):
        if gain_r >= ladder[index].take_at_r:
            due.append(index)
        else:
            break
    return due
