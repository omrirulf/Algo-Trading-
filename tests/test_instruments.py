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
from config.instruments import (  # noqa: F401
    COMMUNICATION,
    TECHNOLOGY,
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

    Sugar is one thing. A fund holding sugar futures is a concentrated,
    volatile, single-factor bet carrying roll decay a basket never does.
    Sizing it like RSP because both are technically ETFs would be picking a
    cap by label rather than by risk.

    Measured 2026-09-14: USO 3.29% and SLV 2.62% daily volatility, both above
    the median single name at 2.26%. "Fund" is not a synonym for "calmer".
    """
    assert kind_for("CANE") is InstrumentKind.COMMODITY_FUND
    assert kind_for("RSP") is InstrumentKind.BROAD_FUND
    assert risk_engine.max_position_pct_for("CANE") < risk_engine.max_position_pct_for("MSFT")
    assert risk_engine.max_position_pct_for("CANE") < risk_engine.max_position_pct_for("RSP")


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

    Before it, MSFT + NVDA + TSM + ASML + GOOGL were five accepted positions
    and one bet, with every per-ticker cap satisfied. A diversified watchlist
    does not produce a diversified portfolio on its own.

    The technology sleeve can no longer reach the cap at all: four names at the
    single-name cap is 20%, under the 25% group limit. Bounded is the property
    that matters -- ``test_the_group_cap_binds_where_it_can_be_reached`` is
    where the rejection itself is pinned.
    """
    engine = ExecutionEngine(broker, market)
    accepted = []
    for ticker in TECHNOLOGY + COMMUNICATION:
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


def test_duration_has_its_own_ceiling_set_by_what_it_can_lose():
    """The one group whose number is not the general 25%.

    It is *higher*, which is the point: a cap is a loss budget, and the
    general number was set for equity groups. Duration's worst fall as a
    basket was 18.9% (2022), so 30% of the account risks about 5.7% of it --
    still less than an equity group at 25% risked in 2008.
    """
    assert cfg.EXPOSURE_GROUP_CAP_OVERRIDES["Duration"] == pytest.approx(0.30)
    assert risk_engine.group_cap_pct("Duration") == pytest.approx(0.30)


def test_every_other_group_keeps_the_general_cap():
    from config.instruments import EXPOSURE_GROUPS

    for group in EXPOSURE_GROUPS:
        if group != "Duration":
            assert risk_engine.group_cap_pct(group) == cfg.MAX_EXPOSURE_GROUP_PCT


def test_the_whole_curve_plus_credit_shares_one_ceiling(broker, market):
    """Four maturities and LQD are one rate view, bounded once.

    Each leg passes its own fund cap; only the shared Duration group stops
    them summing past 30% of the account. Before this group existed, the
    same five tickets could reach 50% -- 25% of Treasuries plus 25% of LQD
    through Credit.
    """
    rejected = []
    for ticker in ("TLT", "IEF", "TIP", "SHY", "LQD"):
        result = ExecutionEngine(broker, market).execute(
            LLMSignal(ticker=ticker, bias=Bias.BEARISH, conviction=0.9, rationale="x")
        )
        if result.status is ExecutionStatus.ACCEPTED:
            broker.positions.append(
                OpenPosition(ticker=ticker, qty=-result.quantity,
                             market_value=result.quantity * market.price)
            )
        else:
            rejected.append(result.reason)

    held = sum(p.market_value for p in broker.positions) / broker.equity
    assert held <= cfg.EXPOSURE_GROUP_CAP_OVERRIDES["Duration"] + 1e-9
    assert rejected, "five legs of one rate bet should not all fit"
    assert any("Duration" in r for r in rejected)


def test_the_rate_bet_is_not_bounded_by_the_stock_limit(broker, market):
    """Pure-rate Treasuries are outside the stock bucket and never consume its room.

    LQD is the deliberate exception: it is a rate instrument on a quiet day
    and an equity instrument in a credit crisis (NBER WP 27168), so it counts
    at a small beta against the stock limit *in addition to* being a full
    Duration member -- both caps see it, at the size each actually risks.
    """
    from config.instruments import equity_risk_beta

    for ticker in ("SHY", "IEF", "TLT", "TIP"):
        assert equity_risk_beta(ticker) is None
    assert equity_risk_beta("LQD") == pytest.approx(0.36)


def test_groups_over_cap_is_empty_for_a_compliant_book():
    """The read-only half of a group-cap trim: nothing to report when nothing is over."""
    positions = [OpenPosition(ticker="TLT", qty=-50, market_value=5_000.0)]
    assert risk_engine.groups_over_cap(100_000.0, positions) == {}


def test_groups_over_cap_measures_duration_against_its_own_ceiling():
    """Not the general 25%: $32,000 of Duration is over its 30%, not its 25%."""
    positions = [
        OpenPosition(ticker="TLT", qty=-160, market_value=16_000.0),
        OpenPosition(ticker="IEF", qty=-110, market_value=11_000.0),
        OpenPosition(ticker="LQD", qty=-50, market_value=5_000.0),
    ]
    excess = risk_engine.groups_over_cap(100_000.0, positions)
    assert excess == {"Duration": pytest.approx(2_000.0)}


def test_lqd_counts_against_duration_not_credit_when_over_cap():
    """The group move has to reach the trim pass, not just the entry check."""
    positions = [
        OpenPosition(ticker="LQD", qty=-320, market_value=32_000.0),
    ]
    assert risk_engine.groups_over_cap(100_000.0, positions) == {
        "Duration": pytest.approx(2_000.0)
    }


def test_groups_over_cap_rejects_non_positive_equity():
    with pytest.raises(risk_engine.RiskViolation):
        risk_engine.groups_over_cap(0.0, [])


def test_the_farm_basket_is_grouped_with_the_crops_it_holds():
    """DBA holds corn, wheat, soybeans and sugar -- the four funds beside it.

    Grouped with DBC it was one agricultural bet spread across two ceilings.
    This was the only one of 171 group pairs to clear |excess r| >= 0.6 over
    2007-present, which is what sent someone looking.
    """
    assert group_for("DBA") == group_for("CORN") == "Agriculture"
    assert group_for("DBA") != group_for("DBC")


def test_the_commodity_basket_is_grouped_with_the_oil_that_dominates_it():
    """DBC is 55-60% energy futures and measures 0.82 excess against Energy.

    Its metals and grain weight counts against the energy ceiling as a
    result, which overstates that part -- the accepted cost of grouping by
    what a thing trades like rather than by what its prospectus spans.
    """
    assert group_for("DBC") == group_for("USO") == group_for("XOM") == "Energy"


def test_broad_commodities_is_a_sizing_roster_and_not_an_exposure_group():
    """Both members are broad funds; neither is a broad bet.

    DBA belongs with the crops it holds, DBC with the oil it mostly holds,
    so there is nothing left for a group of that name to bound.
    """
    from config.instruments import BROAD_FUND_ROLES, EXPOSURE_GROUPS

    assert BROAD_FUND_ROLES["Broad commodities"] == ("DBC", "DBA")
    assert "Broad commodities" not in EXPOSURE_GROUPS


def test_the_farm_basket_is_still_sized_as_a_broad_fund():
    """Grouping is about correlated risk; the cap is about what it holds.

    Ten crops is genuinely more diversified than one, so the sizing is
    unchanged -- only the ceiling it counts against moved.
    """
    assert kind_for("DBA") is InstrumentKind.BROAD_FUND
    assert risk_engine.max_position_pct_for("DBA") == cfg.MAX_BROAD_FUND_PCT


def test_every_watchlist_ticker_lands_in_exactly_one_group():
    """A ticker in two groups would be counted against two ceilings."""
    from config.instruments import EXPOSURE_GROUPS

    seen: dict[str, str] = {}
    for group, tickers in EXPOSURE_GROUPS.items():
        for ticker in tickers:
            assert ticker not in seen, f"{ticker} in {seen.get(ticker)} and {group}"
            seen[ticker] = group
    assert [t for t in SINGLE_NAMES + FUNDS if t not in seen] == []


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
    full = broker.equity * cfg.MAX_SINGLE_NAME_SLEEVE_PCT
    broker.positions = [OpenPosition(ticker="JPM", qty=1, market_value=full)]
    engine = ExecutionEngine(broker, market)
    result = engine.execute(
        LLMSignal(ticker="LLY", bias=Bias.BULLISH, conviction=0.9, rationale="x")
    )
    assert result.status is ExecutionStatus.REJECTED
    assert "sleeve" in result.reason


def test_a_fund_still_fits_when_the_name_sleeve_is_full(broker, market):
    """The budgets are separate, so a full equity sleeve must not block funds."""
    full = broker.equity * cfg.MAX_SINGLE_NAME_SLEEVE_PCT
    broker.positions = [OpenPosition(ticker="JPM", qty=1, market_value=full)]
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
    # Equality rather than identity: asked without a context the fund prompt is
    # assembled from its paragraphs rather than handed out as one constant.
    assert system_prompt_for("IWM") == ETF_SYSTEM_PROMPT
    assert system_prompt_for("GLD") == ETF_SYSTEM_PROMPT
    assert system_prompt_for("MSFT") is SYSTEM_PROMPT
    assert system_prompt_for("ZZZZ") is SYSTEM_PROMPT


def test_the_fund_prompt_sets_a_higher_bar_than_the_company_prompt():
    assert "NEUTRAL" in ETF_SYSTEM_PROMPT
    assert "macro timing" in ETF_SYSTEM_PROMPT
    assert "NO ANALYST PUBLISHES A PRICE TARGET ON AN INDEX" in ETF_SYSTEM_PROMPT


def test_the_account_is_not_left_sitting_in_cash():
    """A standing cash allocation is a drag nobody chose.

    The gross cap sat at 60% for one revision, which meant a permanent 40%
    cash floor. Cash yields close to nothing while equities are the reason the
    account exists, and the risk work that floor looked like it was doing is
    already done by the group cap, the per-kind caps and a stop on every
    position.
    """
    assert cfg.MAX_GROSS_EXPOSURE_PCT >= 0.90


def test_the_position_limit_cannot_re_impose_a_cash_floor():
    """The interaction that is invisible until two constants are read together.

    Per-position caps are small by design, so a fully invested book needs many
    positions. If MAX_OPEN_POSITIONS were low it would cap the account well
    below the gross limit through the back door.
    """
    funds_needed = cfg.MAX_FUND_SLEEVE_PCT / cfg.MAX_BROAD_FUND_PCT
    names_needed = cfg.MAX_SINGLE_NAME_SLEEVE_PCT / cfg.MAX_POSITION_PCT
    assert cfg.MAX_OPEN_POSITIONS >= funds_needed + names_needed


def test_a_full_book_must_span_several_exposure_groups():
    """Being fully invested and being concentrated are now incompatible."""
    groups_needed = cfg.MAX_GROSS_EXPOSURE_PCT / cfg.MAX_EXPOSURE_GROUP_PCT
    assert groups_needed >= 3


def test_the_group_cap_binds_where_it_can_be_reached(broker, market):
    """Eleven developed-country funds at 8% would be 88% of the book in one bet.

    This is where the group cap does visible work, and the reason the focused
    sleeve is safe to widen: every per-ticker cap is satisfied the whole way
    up, so something else has to stop it.
    """
    from config.instruments import COUNTRY_DEVELOPED as INTERNATIONAL

    engine = ExecutionEngine(broker, market)
    rejected = []
    for ticker in INTERNATIONAL:
        result = engine.execute(
            LLMSignal(ticker=ticker, bias=Bias.BULLISH, conviction=0.9, rationale="x")
        )
        if result.status is ExecutionStatus.ACCEPTED:
            broker.positions.append(
                OpenPosition(ticker=ticker, qty=result.quantity,
                             market_value=result.quantity * market.price)
            )
        else:
            rejected.append(result.reason)

    held = sum(p.market_value for p in broker.positions) / broker.equity
    assert held <= cfg.MAX_EXPOSURE_GROUP_PCT + 1e-9
    assert rejected, "eleven country funds should not all fit in one group"
    assert any("Developed international" in r for r in rejected)


# --------------------------------------------------------------------------- #
# Human labels
# --------------------------------------------------------------------------- #


def test_every_watchlist_ticker_has_a_name():
    """A report that says "NVO" makes the reader look it up. That is the bug."""
    from config.instruments import DISPLAY_NAMES, SINGLE_NAMES, FUNDS

    missing = [t for t in SINGLE_NAMES + FUNDS if t not in DISPLAY_NAMES]
    assert missing == []


def test_a_name_is_not_just_the_ticker_again():
    from config.instruments import DISPLAY_NAMES

    # Two exceptions, both honest: ASML is the company's actual name, and
    # CORN is corn.
    same = [t for t, name in DISPLAY_NAMES.items() if t == name.upper()]
    assert same == ["ASML", "CORN"]


@pytest.mark.parametrize(
    "ticker,name",
    [("NVO", "Novo Nordisk"), ("GOOGL", "Alphabet (Google)"), ("TLT", "US government bonds, 20+ years")],
)
def test_name_for_returns_the_readable_name(ticker, name):
    from config.instruments import name_for

    assert name_for(ticker) == name
    assert name_for(ticker.lower()) == name
    assert name_for(f"  {ticker} ") == name


def test_an_unnamed_ticker_falls_back_to_its_symbol():
    """A ticker added to the watchlist before its name was written down."""
    from config.instruments import name_for

    assert name_for("zzzz") == "ZZZZ"


@pytest.mark.parametrize(
    "ticker,label",
    [
        ("MSFT", "Company"), ("RSP", "Index fund"), ("DBC", "Index fund"),
        ("XLE", "Sector or country"), ("EWZ", "Sector or country"),
        ("GLD", "Commodity"),
    ],
)
def test_the_sleeve_label_says_what_the_thing_is(ticker, label):
    """DBC is a basket across commodities; XLE is one sector; GLD is one metal."""
    from config.instruments import sleeve_label

    assert sleeve_label(ticker) == label


def test_every_kind_has_a_label():
    """A new kind must not render as a KeyError in the report."""
    from config.instruments import SLEEVE_LABELS, InstrumentKind

    assert set(SLEEVE_LABELS) == set(InstrumentKind)


def test_an_unknown_ticker_labels_as_a_company():
    """The same fail-closed default the position cap uses: never the widest one."""
    from config.instruments import sleeve_label

    assert sleeve_label("ZZZZ") == "Company"


# --------------------------------------------------------------------------- #
# The focused sleeve: one sector, or one country
# --------------------------------------------------------------------------- #


def test_the_focused_cap_sits_between_the_other_two():
    """Not a broad fund and not a single name, and priced as neither."""
    assert cfg.MAX_POSITION_PCT < cfg.MAX_FOCUSED_FUND_PCT < cfg.MAX_BROAD_FUND_PCT


@pytest.mark.parametrize("ticker", ["XLE", "XLK", "SMH", "VNQ", "EWJ", "EWZ", "KSA", "GDX"])
def test_a_sector_or_country_fund_gets_the_focused_cap(ticker):
    from config.instruments import InstrumentKind, kind_for

    assert kind_for(ticker) is InstrumentKind.FOCUSED_FUND
    assert risk_engine.max_position_pct_for(ticker) == cfg.MAX_FOCUSED_FUND_PCT


def test_a_single_country_is_no_longer_sized_as_a_whole_market():
    """Japan and Israel moved down a tier: one country is one bet."""
    from config.instruments import InstrumentKind, kind_for

    for ticker in ("EWJ", "EIS", "VNQ"):
        assert kind_for(ticker) is not InstrumentKind.BROAD_FUND
        assert risk_engine.max_position_pct_for(ticker) < cfg.MAX_BROAD_FUND_PCT


def test_a_multi_country_fund_is_still_broad():
    from config.instruments import InstrumentKind, kind_for

    for ticker in ("VGK", "VWO", "RSP", "IWM"):
        assert kind_for(ticker) is InstrumentKind.BROAD_FUND


def test_an_unknown_ticker_never_gets_the_focused_cap():
    """The fail-closed default has to stay the smallest of the equity tiers."""
    assert risk_engine.max_position_pct_for("ZZZZ") == cfg.MAX_POSITION_PCT


def test_the_model_still_cannot_assert_a_focused_kind():
    """A fourth kind is a fourth cap, so it is a fourth thing worth claiming."""
    from app.schemas import LLMSignal

    assert "kind" not in LLMSignal.model_fields
    assert "instrument" not in LLMSignal.model_fields
    with pytest.raises(Exception):
        LLMSignal(ticker="MSFT", bias=Bias.BULLISH, conviction=0.9, rationale="x",
                  kind="focused fund")


# --------------------------------------------------------------------------- #
# Exposure groups: what makes a wide watchlist safe
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize(
    "fund,single_name",
    [("XLE", "XOM"), ("XLK", "MSFT"), ("XLF", "JPM"), ("XLV", "LLY"), ("XLI", "CAT")],
)
def test_a_sector_fund_shares_a_group_with_the_names_it_contains(fund, single_name):
    """Otherwise the sector fund is a second helping of the same bet, uncounted."""
    from config.instruments import group_for

    assert group_for(fund) == group_for(single_name)


def test_a_gold_miner_groups_with_gold_not_with_materials():
    """A miner is a levered bet on the metal, not a diversifier from it."""
    from config.instruments import group_for

    assert group_for("GDX") == group_for("GLD")
    assert group_for("GDX") != group_for("XLB")


def test_credit_is_not_filed_with_government_duration():
    """High yield and emerging debt sell off with stocks while Treasuries rally.

    LQD is the exception the data found: it moves with Treasuries (IEF 0.67
    with the market taken out, 0.86 in 2022), so it counts against Duration.
    """
    from config.instruments import group_for

    assert group_for("HYG") == group_for("EMB")
    assert group_for("HYG") != group_for("TLT")
    assert group_for("LQD") == group_for("TLT")


def test_developed_and_emerging_are_not_one_bet():
    from config.instruments import group_for

    assert group_for("EWG") == group_for("EWJ")
    assert group_for("EWZ") == group_for("TUR")
    assert group_for("EWG") != group_for("EWZ")


def test_every_watchlist_ticker_belongs_to_exactly_one_group():
    """An ungrouped ticker is one the group cap cannot see."""
    from config.instruments import EXPOSURE_GROUPS, UNGROUPED, group_for
    from config.watchlist import DEFAULT_WATCHLIST

    assert [t for t in DEFAULT_WATCHLIST if group_for(t) == UNGROUPED] == []
    listed = [t for tickers in EXPOSURE_GROUPS.values() for t in tickers]
    assert sorted(listed) == sorted(DEFAULT_WATCHLIST)


def test_one_technology_bet_cannot_be_taken_four_ways(broker, market):
    """NVDA + MSFT + XLK + SMH is one bet, and every per-ticker cap allows it.

    The reason the focused sleeve could be widened at all: this is the check
    that stops a sector fund stacking on top of the names inside it.
    """
    engine = ExecutionEngine(broker, market)
    rejected = []
    for ticker in ("NVDA", "MSFT", "ASML", "GOOGL", "XLK", "XLC", "SMH", "IGV"):
        result = engine.execute(
            LLMSignal(ticker=ticker, bias=Bias.BULLISH, conviction=0.9, rationale="x")
        )
        if result.status is ExecutionStatus.ACCEPTED:
            broker.positions.append(
                OpenPosition(ticker=ticker, qty=result.quantity,
                             market_value=result.quantity * market.price)
            )
        else:
            rejected.append(result.reason)

    held = sum(p.market_value for p in broker.positions) / broker.equity
    assert held <= cfg.MAX_EXPOSURE_GROUP_PCT + 1e-9
    assert rejected, "four tech names plus four tech funds should not all fit"
    assert any("Technology" in r for r in rejected)


def test_a_ladder_trimmed_book_still_has_room_to_redeploy():
    """The slot count must not block the cash the ladder frees.

    After both rungs a position holds a third of its size but a whole slot.
    A book of full-size positions fills the gross ceiling at N; the same
    book trimmed to thirds uses a third of the account and needs room for
    roughly 2N more entries to redeploy the rest. At 20 that room was zero.
    """
    from app.risk_engine import max_position_pct_for
    from config.watchlist import DEFAULT_WATCHLIST

    average_cap = sum(max_position_pct_for(t) for t in DEFAULT_WATCHLIST) / len(DEFAULT_WATCHLIST)
    full_size_fill = cfg.MAX_GROSS_EXPOSURE_PCT / average_cap
    assert cfg.MAX_OPEN_POSITIONS >= 2 * full_size_fill


def test_the_slot_limit_is_not_what_keeps_the_book_diverse():
    """Diversity is the group cap's job: at any slot count, no group can pass 25%."""
    from config.instruments import EXPOSURE_GROUPS

    widest_group = max(len(t) for t in EXPOSURE_GROUPS.values())
    # Even the widest group, fully populated, is bounded by the group cap --
    # a bound that does not mention the slot count at all.
    assert widest_group <= cfg.MAX_OPEN_POSITIONS
    assert cfg.MAX_EXPOSURE_GROUP_PCT < cfg.MAX_GROSS_EXPOSURE_PCT / 3
