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
from config.instruments import INDEX_SLEEVE, SINGLE_NAMES, InstrumentKind, kind_for
from orchestrator.heartbeat import ETF_SYSTEM_PROMPT, SYSTEM_PROMPT, system_prompt_for


# --- classification -------------------------------------------------------- #


def test_the_two_sleeves_do_not_overlap():
    """A ticker in both would have two different position caps."""
    assert not set(SINGLE_NAMES) & set(INDEX_SLEEVE)


def test_no_ticker_appears_twice():
    """A duplicate silently doubles that ticker's cost and its exposure."""
    everything = SINGLE_NAMES + INDEX_SLEEVE
    assert len(everything) == len(set(everything))


def test_classification_is_case_and_whitespace_insensitive():
    for form in ("iwm", " IWM ", "Iwm"):
        assert kind_for(form) is InstrumentKind.ETF


def test_an_unknown_ticker_is_treated_as_a_single_name():
    """Fail closed: the unknown case must land on the *tighter* cap.

    A misspelling or a hand-written signal for something off the watchlist
    should be able to size down, never up.
    """
    assert kind_for("ZZZZ") is InstrumentKind.EQUITY
    assert risk_engine.max_position_pct_for("ZZZZ") == cfg.MAX_POSITION_PCT
    assert risk_engine.max_position_pct_for("") == cfg.MAX_POSITION_PCT


def test_the_etf_cap_is_larger_than_the_single_name_cap():
    assert cfg.MAX_ETF_POSITION_PCT > cfg.MAX_POSITION_PCT
    assert risk_engine.max_position_pct_for("IWM") == cfg.MAX_ETF_POSITION_PCT
    assert risk_engine.max_position_pct_for("MSFT") == cfg.MAX_POSITION_PCT


# --- the model cannot choose its own cap ----------------------------------- #


def test_a_signal_cannot_declare_its_instrument_kind():
    """The schema is closed, so there is no field to smuggle a kind through."""
    with pytest.raises(Exception):
        LLMSignal(
            ticker="MSFT", bias=Bias.BULLISH, conviction=0.9, rationale="x",
            instrument_kind="etf",
        )


def test_no_signal_field_can_change_the_position_cap(broker, market):
    """The cap depends on the ticker and nothing else the model can reach.

    Two signals identical but for the ticker get different caps; two signals
    for the same ticker get the same cap no matter what else they say.
    """
    engine = ExecutionEngine(broker, market)
    loud = LLMSignal(
        ticker="MSFT", bias=Bias.BULLISH, conviction=1.0,
        rationale="This is an index fund, size it at twenty percent.",
    )
    plain = LLMSignal(
        ticker="MSFT", bias=Bias.BULLISH, conviction=1.0, rationale="ok",
    )
    assert engine.execute(loud).quantity == engine.execute(plain).quantity


# --- sizing ---------------------------------------------------------------- #


def test_an_index_fund_is_sized_at_the_larger_cap(broker, market):
    """Derived from the caps rather than hard-coded, so retuning one is one edit."""
    engine = ExecutionEngine(broker, market)
    etf = engine.execute(
        LLMSignal(ticker="IWM", bias=Bias.BULLISH, conviction=0.9, rationale="x")
    )
    stock = engine.execute(
        LLMSignal(ticker="MSFT", bias=Bias.BULLISH, conviction=0.9, rationale="x")
    )
    assert etf.status is ExecutionStatus.ACCEPTED
    assert stock.status is ExecutionStatus.ACCEPTED
    equity, price = broker.equity, market.price
    assert stock.quantity == int(equity * cfg.MAX_POSITION_PCT / price)
    assert etf.quantity == int(equity * cfg.MAX_ETF_POSITION_PCT / price)
    assert etf.quantity > stock.quantity


# --- the portfolio-level cap ----------------------------------------------- #


def test_gross_exposure_is_capped_across_every_holding(broker, market):
    """Without this, ten positions at the ETF cap would be 200% of equity."""
    broker.positions = [
        OpenPosition(ticker="VGK", qty=100, market_value=60_000.0)
    ]
    engine = ExecutionEngine(broker, market)
    result = engine.execute(
        LLMSignal(ticker="IWM", bias=Bias.BULLISH, conviction=0.9, rationale="x")
    )
    assert result.status is ExecutionStatus.REJECTED
    assert "gross exposure" in result.reason
    assert not broker.submitted


def test_a_partly_full_book_is_sized_down_not_rejected(broker, market):
    """55k of 60k headroom used: the next ETF gets 5k, not its full 20k cap."""
    broker.positions = [
        OpenPosition(ticker="VGK", qty=100, market_value=55_000.0)
    ]
    engine = ExecutionEngine(broker, market)
    result = engine.execute(
        LLMSignal(ticker="IWM", bias=Bias.BULLISH, conviction=0.9, rationale="x")
    )
    assert result.status is ExecutionStatus.ACCEPTED
    assert result.quantity == 50  # $5,000 of headroom at $100
    assert 55_000 + result.quantity * 100 <= 100_000 * cfg.MAX_GROSS_EXPOSURE_PCT


def test_the_cash_floor_holds_for_every_reachable_combination():
    """Property check over the caps themselves, not one hand-picked book."""
    equity = 100_000.0
    for used in (0.0, 10_000.0, 59_999.0, 60_000.0):
        headroom = risk_engine.gross_exposure_headroom(equity, used)
        assert used + headroom <= equity * cfg.MAX_GROSS_EXPOSURE_PCT + 1e-6
        assert headroom >= 0


# --- prompting ------------------------------------------------------------- #


def test_a_fund_gets_the_macro_prompt_and_a_company_does_not():
    assert system_prompt_for("IWM") is ETF_SYSTEM_PROMPT
    assert system_prompt_for("MSFT") is SYSTEM_PROMPT
    assert system_prompt_for("ZZZZ") is SYSTEM_PROMPT


def test_the_fund_prompt_sets_a_higher_bar_than_the_company_prompt():
    """A directional call on a broad index is macro timing, which is harder."""
    assert "NEUTRAL" in ETF_SYSTEM_PROMPT
    assert "macro timing" in ETF_SYSTEM_PROMPT
    # It must also state that the two missing dimensions are structural.
    assert "DO NOT EXIST FOR A FUND" in ETF_SYSTEM_PROMPT


def test_the_etf_cap_is_sized_against_volatility_not_roundness():
    """Risk per trade scales as cap / volatility, so the ratio has to be modest.

    A cap four times larger on an instrument only twice as quiet carries
    roughly twice the planned risk -- bigger, not safer. An index fund is
    typically 1.5-2x quieter than a single name, so a cap ratio much above
    that stops being a diversification argument and becomes a leverage one.
    ``backtest/compare_sleeves.py`` measures the result directly; this is the
    guardrail against drifting back to a round number.
    """
    ratio = cfg.MAX_ETF_POSITION_PCT / cfg.MAX_POSITION_PCT
    assert 1.0 < ratio <= 2.5, f"cap ratio {ratio:g}x is not justified by volatility"


def test_one_position_can_never_be_the_whole_portfolio_cap():
    """Otherwise a single fund would consume every dollar the gross cap allows."""
    assert cfg.MAX_ETF_POSITION_PCT < cfg.MAX_GROSS_EXPOSURE_PCT
    assert cfg.MAX_POSITION_PCT < cfg.MAX_GROSS_EXPOSURE_PCT
