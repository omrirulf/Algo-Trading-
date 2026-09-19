"""The macro layer added on top of the exposure groups (study of 2007-2026 prices).

Three things, each tested at the level it lives at:

- five tickers count against a different group, and "Broad commodities" is gone;
- Duration has its own 30% ceiling, now that it holds LQD;
- one new limit, on net stock-market risk counted by beta, where longs add and
  shorts subtract inside the stock bucket and nowhere else.
"""

from __future__ import annotations

import pytest

from app import risk_engine
from app.broker_client import OpenPosition
from app.execution_engine import ExecutionEngine
from app.schemas import Bias, ExecutionStatus, LLMSignal
from config import settings as cfg
from config.instruments import (
    EQUITY_RISK_BETAS,
    EXPOSURE_GROUPS,
    InstrumentKind,
    equity_risk_beta,
    group_for,
    kind_for,
)

EQUITY = 100_000.0


def long(ticker: str, value: float) -> OpenPosition:
    return OpenPosition(ticker=ticker, qty=1, market_value=value)


def short(ticker: str, value: float) -> OpenPosition:
    return OpenPosition(ticker=ticker, qty=-1, market_value=value)


# --------------------------------------------------------------------------- #
# Group moves
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize(
    "moved,now_with",
    [("DBC", "USO"), ("DBA", "CORN"), ("LQD", "TLT"), ("HDB", "INDA"), ("MELI", "ARGT")],
)
def test_each_moved_ticker_counts_with_what_it_trades_like(moved, now_with):
    assert group_for(moved) == group_for(now_with)


def test_the_moves_leave_the_old_groups_and_the_broad_commodity_group_is_gone():
    assert "Broad commodities" not in EXPOSURE_GROUPS
    assert group_for("HDB") != group_for("JPM")
    assert group_for("MELI") != group_for("XLY")
    assert group_for("LQD") != group_for("HYG")


def test_a_group_move_does_not_change_a_ticker_s_position_cap():
    """Kind decides the per-position cap; the group only decides what it counts against."""
    assert kind_for("DBC") is InstrumentKind.BROAD_FUND
    assert kind_for("LQD") is InstrumentKind.BROAD_FUND
    assert kind_for("HDB") is InstrumentKind.EQUITY
    assert kind_for("MELI") is InstrumentKind.EQUITY


# --------------------------------------------------------------------------- #
# Duration's own ceiling
# --------------------------------------------------------------------------- #


def test_duration_has_its_own_ceiling_and_every_other_group_the_default():
    assert risk_engine.group_cap_pct("Duration") == pytest.approx(0.30)
    for group in EXPOSURE_GROUPS:
        if group != "Duration":
            assert risk_engine.group_cap_pct(group) == cfg.MAX_EXPOSURE_GROUP_PCT


def test_treasuries_and_lqd_share_the_30_percent():
    room = risk_engine.exposure_group_headroom(
        EQUITY, "TLT", [long("IEF", 20_000.0), long("LQD", 5_000.0)]
    )
    assert room == pytest.approx(5_000.0)


# --------------------------------------------------------------------------- #
# The stock bucket
# --------------------------------------------------------------------------- #


def test_the_stock_bucket_is_the_equity_groups_plus_four():
    equity_groups = (
        "Technology", "Financials", "Health care", "Industrials", "Consumer",
        "Utilities", "Materials", "Real estate", "US broad equity",
        "Developed international", "Emerging markets",
    )
    expected = {t for g in equity_groups for t in EXPOSURE_GROUPS[g]}
    expected |= {"XLE", "XOM", "HYG", "EMB"}
    assert set(EQUITY_RISK_BETAS) == expected
    assert all(0 < beta < 3 for beta in EQUITY_RISK_BETAS.values())


@pytest.mark.parametrize("outside", ["TLT", "LQD", "GLD", "USO", "DBC", "UNG", "CORN", "UUP", "CPER"])
def test_bonds_commodities_gold_and_the_dollar_are_outside_it(outside):
    assert equity_risk_beta(outside) is None
    assert risk_engine.equity_risk_headroom(EQUITY, outside, "buy", []) is None


def test_an_unknown_ticker_counts_as_a_full_unit_of_market():
    assert equity_risk_beta("ZZZZ") == 1.0


def test_the_limit_counts_beta_weighted_dollars():
    """$20k of XLP (beta 0.54) uses about half the room of $20k of NVDA (1.57)."""
    book = [long("XLP", 20_000.0)]
    used = risk_engine.net_equity_risk(book)
    assert used == pytest.approx(20_000.0 * 0.54)
    room = risk_engine.equity_risk_headroom(EQUITY, "RSP", "buy", book)
    assert room == pytest.approx((60_000.0 - 10_800.0) / 1.04)


def test_the_limit_binds_across_groups_the_group_caps_cannot_see():
    """Three groups, each well under 25%, add up to the whole stock limit."""
    book = [long("RSP", 20_000.0), long("VGK", 20_000.0), long("XLK", 20_000.0)]
    assert risk_engine.net_equity_risk(book) > EQUITY * cfg.MAX_EQUITY_RISK_PCT
    room, label = risk_engine.budget_ceiling_for(EQUITY, "XLV", book, "buy")
    assert room == 0.0
    assert label.startswith("stock-market")


def test_a_short_inside_the_bucket_frees_room():
    book = [long("RSP", 50_000.0), short("XLK", 20_000.0)]
    net = 50_000.0 * 1.04 - 20_000.0 * 1.03
    assert risk_engine.net_equity_risk(book) == pytest.approx(net)
    buy_room = risk_engine.equity_risk_headroom(EQUITY, "VGK", "buy", book)
    sell_room = risk_engine.equity_risk_headroom(EQUITY, "VGK", "sell", book)
    assert buy_room == pytest.approx((60_000.0 - net) / 1.00)
    assert sell_room == pytest.approx((60_000.0 + net) / 1.00)


def test_a_short_outside_the_bucket_does_not_offset_stocks():
    """Bonds moved with stocks in 2022; nothing outside the bucket nets against it."""
    with_gold_short = [long("RSP", 50_000.0), short("GLD", 20_000.0)]
    without = [long("RSP", 50_000.0)]
    assert risk_engine.net_equity_risk(with_gold_short) == risk_engine.net_equity_risk(without)


def test_a_net_short_book_is_bounded_the_same_way():
    book = [short("RSP", 57_000.0)]
    room = risk_engine.equity_risk_headroom(EQUITY, "IWM", "sell", book)
    assert room == pytest.approx(max(0.0, 60_000.0 - 57_000.0 * 1.04) / 1.16)


def test_the_group_caps_stay_sign_blind():
    """A long and a short in one group still both count toward its 25%."""
    room = risk_engine.exposure_group_headroom(
        EQUITY, "XLK", [long("MSFT", 10_000.0), short("SMH", 10_000.0)]
    )
    assert room == pytest.approx(5_000.0)


# --------------------------------------------------------------------------- #
# End to end through the execution engine
# --------------------------------------------------------------------------- #


def _full_of_stocks(broker) -> None:
    broker.positions = [
        long("RSP", 20_000.0), long("VGK", 20_000.0), long("XLK", 20_000.0),
    ]


def test_the_engine_refuses_a_stock_buy_once_the_limit_is_full(broker, market):
    _full_of_stocks(broker)
    result = ExecutionEngine(broker, market).execute(
        LLMSignal(ticker="XLP", bias=Bias.BULLISH, conviction=0.9, rationale="x")
    )
    assert result.status is ExecutionStatus.REJECTED
    assert "stock-market" in result.reason


def test_the_engine_still_allows_a_stock_short_that_reduces_the_net(broker, market):
    _full_of_stocks(broker)
    result = ExecutionEngine(broker, market).execute(
        LLMSignal(ticker="XLP", bias=Bias.BEARISH, conviction=0.9, rationale="x")
    )
    assert result.status is ExecutionStatus.ACCEPTED
    assert broker.submitted[-1]["side"] == "sell"


def test_the_engine_still_allows_a_bond_buy_when_stocks_are_full(broker, market):
    _full_of_stocks(broker)
    result = ExecutionEngine(broker, market).execute(
        LLMSignal(ticker="IEF", bias=Bias.BULLISH, conviction=0.9, rationale="x")
    )
    assert result.status is ExecutionStatus.ACCEPTED
