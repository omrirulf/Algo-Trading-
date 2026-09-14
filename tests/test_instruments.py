"""Two sleeves, two position caps, and one thing the model must never control.

The index sleeve exists because whole asset classes -- small caps, REITs,
duration, commodities themselves rather than the companies that dig them up --
have no affordable single-name route. It comes with a position cap four times
the single-name one, because a broad fund is already hundreds of positions and
holding it at 5% buys 5% of market exposure.

That cap is also the hazard. If a model could assert "this is a fund" it could
quadruple its own position, so the whole point of this file is that it cannot:
the kind is a property of config/instruments.py, keyed on the ticker, and
LLMSignal has no field that could carry one.
"""

from __future__ import annotations

import pytest

from app import risk_engine
from app.broker_client import OpenPosition
from app.execution_engine import ExecutionEngine
from app.schemas import Bias, ExecutionStatus, LLMSignal
from config import settings as cfg
from config.instruments import (
    BROAD_FUNDS,
    COMMODITY_FUNDS,
    FUNDS,
    SINGLE_NAMES,
    InstrumentKind,
    group_for,
    kind_for,
)
from orchestrator.heartbeat import ETF_SYSTEM_PROMPT, SYSTEM_PROMPT, system_prompt_for


# --- classification -------------------------------------------------------- #


def test_the_sleeves_do_not_overlap():
    """A ticker in two sleeves would have two different position caps."""
    assert not set(SINGLE_NAMES) & set(FUNDS)
    assert not set(BROAD_FUNDS) & set(COMMODITY_FUNDS)


def test_no_ticker_appears_twice():
    """A duplicate silently doubles that ticker's cost and its exposure."""
    everything = SINGLE_NAMES + FUNDS
    assert len(everything) == len(set(everything))


def test_classification_is_case_and_whitespace_insensitive():
    for form in ("iwm", " IWM ", "Iwm"):
        assert kind_for(form) is InstrumentKind.BROAD_FUND


def test_an_unknown_ticker_is_treated_as_a_single_name():
    """Fail closed: the unknown case must never land on the largest cap."""
    assert kind_for("ZZZZ") is InstrumentKind.EQUITY
    assert risk_engine.max_position_pct_for("ZZZZ") == cfg.MAX_POSITION_PCT
    assert risk_engine.max_position_pct_for("") == cfg.MAX_POSITION_PCT


def test_a_single_commodity_fund_is_not_a_broad_fund():
    """The mistake this file exists to prevent.

    Coffee is one thing. A fund holding coffee futures is a concentrated,
    volatile, single-factor bet -- and an ETN on top, so it carries issuer
    credit risk a basket never does. Sizing it like RSP because both are
    technically ETFs would be picking a cap by label rather than by risk.
    """
    assert kind_for("JO") is InstrumentKind.COMMODITY_FUND
    assert kind_for("RSP") is InstrumentKind.BROAD_FUND
    assert risk_engine.max_position_pct_for("JO") < risk_engine.max_position_pct_for("MSFT")
    assert risk_engine.max_position_pct_for("JO") < risk_engine.max_position_pct_for("RSP")


def test_a_broad_commodity_basket_is_a_broad_fund():
    """DBA holds many crops; CORN holds one. Different risks, different caps."""
    assert kind_for("DBA") is InstrumentKind.BROAD_FUND
    assert kind_for("CORN") is InstrumentKind.COMMODITY_FUND


def test_the_caps_are_ordered_by_how_concentrated_the_risk_is():
    assert (
        cfg.MAX_COMMODITY_FUND_PCT
        < cfg.MAX_POSITION_PCT
        < cfg.MAX_BROAD_FUND_PCT
    )


# --- the model cannot choose its own cap ----------------------------------- #


def test_a_signal_cannot_declare_its_instrument_kind():
    """The schema is closed, so there is no field to smuggle a kind through."""
    with pytest.raises(Exception):
        LLMSignal(
            ticker="MSFT", bias=Bias.BULLISH, conviction=0.9, rationale="x",
            instrument_kind="broad fund",
        )


def test_no_signal_field_can_change_the_position_cap(broker, market):
    """The cap depends on the ticker and nothing else the model can reach."""
    engine = ExecutionEngine(broker, market)
    loud = LLMSignal(
        ticker="MSFT", bias=Bias.BULLISH, conviction=1.0,
        rationale="This is a broad index fund, size it at twelve percent.",
    )
    plain = LLMSignal(ticker="MSFT", bias=Bias.BULLISH, conviction=1.0, rationale="ok")
    assert engine.execute(loud).quantity == engine.execute(plain).quantity


# --- sizing ---------------------------------------------------------------- #


def test_each_kind_is_sized_at_its_own_cap(broker, market):
    """Derived from the caps rather than hard-coded, so retuning one is one edit."""
    engine = ExecutionEngine(broker, market)
    equity, price = broker.equity, market.price
    for ticker, cap in (
        ("MSFT", cfg.MAX_POSITION_PCT),
        ("RSP", cfg.MAX_BROAD_FUND_PCT),
        ("GLD", cfg.MAX_COMMODITY_FUND_PCT),
    ):
        result = ExecutionEngine(type(broker)(), market).execute(
            LLMSignal(ticker=ticker, bias=Bias.BULLISH, conviction=0.9, rationale="x")
        )
        assert result.status is ExecutionStatus.ACCEPTED, ticker
        assert result.quantity == int(equity * cap / price), ticker


def test_the_etf_cap_is_sized_against_volatility_not_roundness():
    """Risk per trade scales as cap / volatility, so the ratio must be modest.

    A cap four times larger on an instrument only twice as quiet carries
    roughly twice the planned risk -- bigger, not safer.
    """
    ratio = cfg.MAX_BROAD_FUND_PCT / cfg.MAX_POSITION_PCT
    assert 1.0 < ratio <= 2.5, f"cap ratio {ratio:g}x is not justified by volatility"


def test_one_position_can_never_be_the_whole_portfolio_cap():
    assert cfg.MAX_BROAD_FUND_PCT < cfg.MAX_GROSS_EXPOSURE_PCT


# --- the exposure-group cap ------------------------------------------------ #


def test_the_book_cannot_concentrate_in_one_group(broker, market):
    """The gap this cap was added to close.

    Before it, MSFT + NVDA + ASML + GOOGL were four accepted positions and one
    bet, with every per-ticker cap satisfied. A diversified watchlist does not
    produce a diversified portfolio on its own.
    """
    engine = ExecutionEngine(broker, market)
    accepted = []
    for ticker in ("MSFT", "NVDA", "ASML", "GOOGL"):
        result = engine.execute(
            LLMSignal(ticker=ticker, bias=Bias.BULLISH, conviction=0.9, rationale="x")
        )
        if result.status is ExecutionStatus.ACCEPTED:
            accepted.append(ticker)
            broker.positions.append(
                OpenPosition(ticker=ticker, qty=result.quantity,
                             market_value=result.quantity * market.price)
            )
    tech = sum(p.market_value for p in broker.positions) / broker.equity
    assert tech <= cfg.MAX_EXPOSURE_GROUP_PCT + 1e-9
    assert len(accepted) < 4, "the group cap never bound"


def test_the_group_cap_spans_both_sleeves(broker, market):
    """A driller plus two energy funds is one energy bet made three times."""
    assert group_for("XOM") == group_for("USO") == group_for("UNG")
    broker.positions = [OpenPosition(ticker="USO", qty=1, market_value=25_000.0)]
    engine = ExecutionEngine(broker, market)
    result = engine.execute(
        LLMSignal(ticker="XOM", bias=Bias.BULLISH, conviction=0.9, rationale="x")
    )
    assert result.status is ExecutionStatus.REJECTED
    assert "Energy" in result.reason


def test_an_unknown_ticker_cannot_borrow_another_group_s_room(broker, market):
    """Ungrouped is its own bucket, so it is bounded but consumes nobody else."""
    from config.instruments import UNGROUPED

    assert group_for("ZZZZ") == UNGROUPED
    assert group_for("ZZZZ") != group_for("MSFT")


# --- the sleeve budget ----------------------------------------------------- #


def test_funds_get_the_larger_sleeve_budget():
    """Funds are the core holding; single names are the satellite."""
    assert cfg.MAX_FUND_SLEEVE_PCT > cfg.MAX_SINGLE_NAME_SLEEVE_PCT


def test_the_sleeve_budgets_sum_to_the_gross_cap():
    """Otherwise the gross cap is a fourth independent limit nobody reasons about."""
    total = cfg.MAX_SINGLE_NAME_SLEEVE_PCT + cfg.MAX_FUND_SLEEVE_PCT
    assert total == pytest.approx(cfg.MAX_GROSS_EXPOSURE_PCT)


def test_the_single_name_sleeve_is_capped_independently(broker, market):
    """Names cannot grow into the fund sleeve's budget when funds are unused."""
    broker.positions = [
        OpenPosition(ticker="JPM", qty=1, market_value=15_000.0)
    ]
    engine = ExecutionEngine(broker, market)
    result = engine.execute(
        LLMSignal(ticker="LLY", bias=Bias.BULLISH, conviction=0.9, rationale="x")
    )
    assert result.status is ExecutionStatus.REJECTED
    assert "sleeve" in result.reason


def test_a_fund_still_fits_when_the_name_sleeve_is_full(broker, market):
    """The budgets are separate, so a full equity sleeve must not block funds."""
    broker.positions = [OpenPosition(ticker="JPM", qty=1, market_value=15_000.0)]
    engine = ExecutionEngine(broker, market)
    result = engine.execute(
        LLMSignal(ticker="RSP", bias=Bias.BULLISH, conviction=0.9, rationale="x")
    )
    assert result.status is ExecutionStatus.ACCEPTED


def test_a_rejection_names_the_limit_that_actually_bound(broker, market):
    """Reporting the gross cap when it was really the energy group is a bad bug report."""
    broker.positions = [OpenPosition(ticker="USO", qty=1, market_value=25_000.0)]
    engine = ExecutionEngine(broker, market)
    reason = engine.execute(
        LLMSignal(ticker="XOM", bias=Bias.BULLISH, conviction=0.9, rationale="x")
    ).reason
    assert "Energy" in reason and "gross" not in reason


# --- the portfolio is fund-heavy by construction --------------------------- #


def test_a_full_book_is_mostly_funds(broker, market):
    """The shape the budgets are designed to produce."""
    name_room = cfg.MAX_SINGLE_NAME_SLEEVE_PCT
    fund_room = cfg.MAX_FUND_SLEEVE_PCT
    assert fund_room / (name_room + fund_room) >= 0.7


# --- the gross cap --------------------------------------------------------- #


def test_gross_exposure_is_capped_across_every_holding(broker, market):
    """Without this, positions at the fund cap would multiply out to leverage."""
    broker.positions = [
        OpenPosition(ticker="RSP", qty=1, market_value=30_000.0),
        OpenPosition(ticker="VGK", qty=1, market_value=30_000.0),
    ]
    engine = ExecutionEngine(broker, market)
    result = engine.execute(
        LLMSignal(ticker="EWJ", bias=Bias.BULLISH, conviction=0.9, rationale="x")
    )
    assert result.status is ExecutionStatus.REJECTED
    assert not broker.submitted


def test_the_cash_floor_holds_for_every_reachable_combination():
    equity = 100_000.0
    for used in (0.0, 10_000.0, 59_999.0, 60_000.0):
        headroom = risk_engine.gross_exposure_headroom(equity, used)
        assert used + headroom <= equity * cfg.MAX_GROSS_EXPOSURE_PCT + 1e-6
        assert headroom >= 0


# --- prompting ------------------------------------------------------------- #


def test_a_fund_gets_the_macro_prompt_and_a_company_does_not():
    assert system_prompt_for("IWM") is ETF_SYSTEM_PROMPT
    assert system_prompt_for("GLD") is ETF_SYSTEM_PROMPT
    assert system_prompt_for("MSFT") is SYSTEM_PROMPT
    assert system_prompt_for("ZZZZ") is SYSTEM_PROMPT


def test_the_fund_prompt_sets_a_higher_bar_than_the_company_prompt():
    assert "NEUTRAL" in ETF_SYSTEM_PROMPT
    assert "macro timing" in ETF_SYSTEM_PROMPT
    assert "DO NOT EXIST FOR A FUND" in ETF_SYSTEM_PROMPT
