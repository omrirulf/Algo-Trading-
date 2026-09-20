"""A replayed prompt must be the prompt the model actually saw.

This is the load-bearing property of the whole harness. If reconstruction is
lossy, every comparison downstream is measuring a prompt nobody was ever
shown, and the result looks like evidence while being noise.

It is held for a company and for a fund, separately, because the two render
different sections and for four months only the company half was checked.
"""

from __future__ import annotations

import dataclasses
import json
from dataclasses import is_dataclass
from pathlib import Path
from typing import get_args, get_type_hints

import pytest

from config.instruments import is_fund
from orchestrator import (
    analysts, carry, crops, earnings, energy, flows, fundamentals, funds,
    holdings, insiders, macro, outlook, positioning, technicals,
)
from orchestrator.context import ENRICHMENT_SECTIONS, TickerContext
from replay.rebuild import (
    PASSTHROUGH_KEYS, SNAPSHOT_TYPES, RebuildError, context_from_dict,
    prompt_from_dict,
)


def full_context() -> TickerContext:
    """A context with every dimension populated, including nested trades."""
    return TickerContext(
        ticker="AAPL",
        headlines=["Apple beats on earnings — revenue up 8% (Reuters, 2h ago)"],
        technicals=technicals.TechnicalSnapshot(
            bars=500, as_of="2026-09-12", last_close=225.5,
            sma20=220.0, sma50=215.0, sma200=200.0,
            distance_sma20=0.025, distance_sma50=0.049, distance_sma200=0.128,
            rsi14=61.2, macd=1.4, macd_signal=1.1, macd_histogram=0.3,
            atr14=3.2, atr_pct_of_price=0.014,
            return_1d=0.004, return_5d=0.021, return_21d=0.055, return_63d=0.11,
            high_52w=240.0, low_52w=164.0, position_in_52w_range=0.81,
            relative_volume=1.3, annualised_volatility=0.28,
        ),
        fundamentals=fundamentals.FundamentalSnapshot(
            sector="Technology", industry="Consumer Electronics", market_cap=3.4e12,
            trailing_pe=34.2, forward_pe=29.9, next_earnings_date="2026-10-30",
        ),
        analysts=analysts.AnalystSnapshot(
            recommendation="buy", recommendation_mean=1.9, analyst_count=42,
            target_mean=250.0, target_upside=0.11,
            rating_counts={"strongBuy": 20, "buy": 12, "hold": 8},
            recent_actions=["Morgan Stanley: Overweight (maintained)"],
            institutional_ownership=0.61, top_holders=["Vanguard 8.2%"],
        ),
        insiders=insiders.InsiderSnapshot(
            shares_purchased=50_000, purchase_count=1, shares_sold=400_000, sale_count=2,
            net_shares=-350_000, net_pct_of_held=-0.021, total_shares_held=16_700_000,
            buys=[insiders.InsiderTrade("2026-08-14", "Jane Roe", "CFO", 50_000, 6.1e6)],
            sells=[
                insiders.InsiderTrade("2026-09-01", "John Doe", "Director", 400_000, 5.2e7),
                insiders.InsiderTrade("2026-08-20", "A Third", "SVP", 12_000, 2.7e6),
            ],
            distinct_buyers=1, distinct_sellers=2, non_market_count=3,
        ),
        gaps=[],
    )


# --- the guarantee --------------------------------------------------------


def test_a_rebuilt_context_renders_an_identical_prompt():
    original = full_context()
    assert prompt_from_dict(original.as_dict()) == original.as_prompt()


def test_the_prompt_is_not_trivially_short():
    """Guards the test above from passing on an empty render."""
    prompt = full_context().as_prompt()
    assert len(prompt) > 400
    for heading in ("TICKER:", "NEWS", "INSIDER"):
        assert heading in prompt


def test_nested_insider_trades_survive_the_round_trip():
    """asdict() flattens these to plain dicts; as_lines() raises on those."""
    rebuilt = context_from_dict(full_context().as_dict())
    assert isinstance(rebuilt.insiders.buys[0], insiders.InsiderTrade)
    assert isinstance(rebuilt.insiders.sells[1], insiders.InsiderTrade)
    assert rebuilt.insiders.buys[0].who == "Jane Roe"
    assert len(rebuilt.insiders.sells) == 2


def test_every_dimension_comes_back_as_its_own_type():
    rebuilt = context_from_dict(full_context().as_dict())
    assert isinstance(rebuilt.technicals, technicals.TechnicalSnapshot)
    assert isinstance(rebuilt.fundamentals, fundamentals.FundamentalSnapshot)
    assert isinstance(rebuilt.analysts, analysts.AnalystSnapshot)
    assert isinstance(rebuilt.insiders, insiders.InsiderSnapshot)


# --- degraded cycles are the common case ---------------------------------


def test_a_missing_dimension_stays_missing():
    """A source that was down must render as unavailable, not as defaults."""
    payload = full_context().as_dict()
    payload["insiders"] = None
    rebuilt = context_from_dict(payload)
    assert rebuilt.insiders is None
    assert "unavailable this cycle" in rebuilt.as_prompt()


def test_gaps_are_preserved_verbatim():
    original = full_context()
    object.__setattr__(original, "gaps", ["insider data: HTTP 502"])
    rebuilt = context_from_dict(original.as_dict())
    assert rebuilt.gaps == ["insider data: HTTP 502"]
    assert "DATA GAPS" in rebuilt.as_prompt()


def test_a_news_only_cycle_round_trips():
    bare = TickerContext(ticker="MSFT", headlines=["something happened"],
                         gaps=["technicals: no data"])
    assert prompt_from_dict(bare.as_dict()) == bare.as_prompt()


def test_a_cycle_with_no_headlines_round_trips():
    bare = TickerContext(ticker="NVDA")
    assert prompt_from_dict(bare.as_dict()) == bare.as_prompt()
    assert "none found" in bare.as_prompt()


# --- schema drift: old lines must stay readable --------------------------


def test_a_line_written_before_insiders_existed_still_rebuilds():
    payload = full_context().as_dict()
    del payload["insiders"]
    rebuilt = context_from_dict(payload)
    assert rebuilt.insiders is None


def test_an_unknown_field_is_ignored_rather_than_fatal():
    """A line from a newer schema must not break an older reader."""
    payload = full_context().as_dict()
    payload["technicals"]["sma400"] = 123.0
    payload["sentiment"] = {"score": 1.0}
    rebuilt = context_from_dict(payload)
    assert rebuilt.technicals.sma20 == 220.0


# --- refuse rather than invent -------------------------------------------


def test_a_context_without_a_ticker_is_refused():
    with pytest.raises(RebuildError) as excinfo:
        context_from_dict({"headlines": []})
    assert "ticker" in str(excinfo.value)


@pytest.mark.parametrize("bad", [None, [], "AAPL", 42])
def test_a_non_object_context_is_refused(bad):
    with pytest.raises(RebuildError):
        context_from_dict(bad)


def test_a_non_object_dimension_is_refused():
    payload = full_context().as_dict()
    payload["technicals"] = "not a snapshot"
    with pytest.raises(RebuildError) as excinfo:
        context_from_dict(payload)
    assert "technicals" in str(excinfo.value)


def test_the_ticker_is_normalised():
    rebuilt = context_from_dict({"ticker": "  aapl  "})
    assert rebuilt.ticker == "AAPL"


# --- funds are the majority of the watchlist -----------------------------
#
# Everything above builds a company, and for four months that was the whole
# test: the company sections were the only ones ``rebuild`` restored, so the
# guarantee held for the 20% of the watchlist these tests covered and failed
# silently for the other 80%. A fund exercises the sections a company does not
# have, and exercises them through ``json`` -- the journal is a JSON file, and
# JSON is where a tuple field stops being a tuple.


def full_fund_context() -> TickerContext:
    """A fund carrying every section any fund can have, all at once.

    Deliberately not realistic: no single ticker has both a crop and a sector
    mix. Realism would cost coverage, and coverage is the whole point --
    nine sections that a company context never exercises, four of them
    (``Window``, ``Stock``, ``Point``, ``FlowWindow``) lists of dataclasses
    that ``asdict`` flattens on the way out, and one of those nested two deep.
    """
    return TickerContext(
        ticker="XLE",
        headlines=["Energy names rally as crude firms (Reuters, 1h ago)"],
        sources=[{"title": "Energy names rally", "url": "https://example.test/e"}],
        technicals=technicals.TechnicalSnapshot(
            bars=500, as_of="2026-09-12", last_close=312.4,
            sma20=305.0, sma50=298.0, sma200=270.0,
            distance_sma20=0.024, distance_sma50=0.048, distance_sma200=0.157,
            rsi14=64.0, macd=2.1, macd_signal=1.7, macd_histogram=0.4,
            atr14=4.0, atr_pct_of_price=0.013,
            return_1d=0.003, return_5d=0.018, return_21d=0.041, return_63d=0.092,
            high_52w=315.0, low_52w=228.0, position_in_52w_range=0.97,
            relative_volume=1.4, annualised_volatility=0.16,
        ),
        macro=macro.MacroSnapshot(
            yields={"2-year": 3.42, "10-year": 4.08},
            yield_changes={"2-year": -0.06, "10-year": -0.03},
            slope=0.66, dollar=97.4, dollar_change=-0.008,
            volatility=15.2, volatility_change=0.9,
            release_lines=["CPI 2.9% y/y (Aug, released 11 Sep)"],
        ),
        funds=funds.FundSnapshot(
            ticker="XLE", shape=funds.EQUITY_FUND, category="Equity Energy",
            holdings_pe=14.2, holdings_pb=2.1, holdings_ps=1.4,
            holdings_earnings_growth=0.08, three_year_return=0.21, beta=0.94,
            dividend_yield=0.031, expense_ratio=0.0009, total_assets=3.4e10,
            top_holdings=["XOM 22.1%", "CVX 17.4%"],
            sector_mix=["Energy 99.8%"], asset_mix=["Stocks 99.9%"],
        ),
        holdings=holdings.HoldingsSnapshot(
            ticker="XLE", covered=3, coverage_weight=0.62, buy_weight=0.4,
            hold_weight=0.18, sell_weight=0.04, mean_rating=2.1, target_upside=0.07,
            recent_actions=["UBS: Buy (maintained)"], names=["XOM 22.1%", "CVX 17.4%"],
        ),
        positioning=positioning.PositioningSnapshot(
            ticker="XLE", contract="CRUDE OIL, LIGHT SWEET - NYMEX",
            as_of="2026-09-09", net_share=0.31, week_change=0.02,
            year_percentile=0.88, weeks_of_history=52, open_interest=452_000.0,
        ),
        carry=carry.CarrySnapshot(
            ticker="XLE", commodity="crude oil",
            windows=[
                carry.Window(label="3 months", days=63, fund=0.041,
                             commodity=0.045, gap=-0.004),
                carry.Window(label="1 year", days=252, fund=0.238,
                             commodity=0.251, gap=-0.013),
            ],
        ),
        energy=energy.EnergySnapshot(
            ticker="XLE", period="2026-09-11",
            stocks=[
                energy.Stock(label="crude", name="Crude oil", unit="mb", level=421.3,
                             change=-2.1, percentile=0.34, period="2026-09-11", weeks=260),
            ],
        ),
        outlook=outlook.OutlookSnapshot(
            ticker="XLE",
            forecasts=[
                outlook.Forecast(
                    label="wti", name="WTI crude", unit="$/b",
                    now=outlook.Point(0, "Sep 2026", 64.5),
                    ahead=[outlook.Point(3, "Dec 2026", 62.0),
                           outlook.Point(6, "Mar 2027", 61.0)],
                    # A tuple, which JSON has no way to store: it comes back a
                    # list, and only the annotation says to make it one again.
                    next_year=(2027, 61.4),
                ),
            ],
        ),
        crops=crops.CropSnapshot(
            ticker="XLE", crop="CORN", year=2026, week=37, condition=0.64,
            change=-0.01, weeks=22, last_year=0.58,
            history=[0.61, 0.63, 0.65, 0.64],
        ),
        flows=flows.FlowSnapshot(
            ticker="XLE", shares=3.4e8, net_assets=3.4e10, points=44,
            windows=[
                flows.FlowWindow(label="1 week", change=0.004, dollars=4.4e8, days=5),
                flows.FlowWindow(label="1 month", change=0.021, dollars=2.3e9, days=21),
            ],
        ),
        gaps=["analyst coverage of 2 holdings (BRK-B, JPM)"],
    )


def journalled(context: TickerContext) -> dict:
    """The context as the journal actually stores it -- through JSON.

    ``as_dict()`` alone is not the archive. The archive is a line of JSON, and
    the trip through it is what turns tuples into lists.
    """
    return json.loads(json.dumps(context.as_dict()))


def test_a_rebuilt_fund_renders_an_identical_prompt():
    original = full_fund_context()
    assert prompt_from_dict(journalled(original)) == original.as_prompt()


def test_the_fund_prompt_carries_the_sections_a_company_has_not():
    """Guards the test above from passing on a prompt that lost them all.

    The truncated rebuild rendered TICKER / NEWS / TECHNICALS and nothing
    else, which still compared equal to itself.
    """
    prompt = prompt_from_dict(journalled(full_fund_context()))
    for heading in ("MACRO", "FUND BASICS", "ANALYST VIEW OF THE HOLDINGS",
                    "POSITIONING", "COST OF HOLDING", "ENERGY INVENTORIES",
                    "PRICE OUTLOOK", "CROP CONDITION", "FUND FLOWS"):
        assert heading in prompt, heading
    assert len(prompt) > 2000


def test_every_fund_dimension_comes_back_as_its_own_type():
    rebuilt = context_from_dict(journalled(full_fund_context()))
    for attribute, expected in (
        ("macro", macro.MacroSnapshot),
        ("funds", funds.FundSnapshot),
        ("holdings", holdings.HoldingsSnapshot),
        ("positioning", positioning.PositioningSnapshot),
        ("carry", carry.CarrySnapshot),
        ("energy", energy.EnergySnapshot),
        ("outlook", outlook.OutlookSnapshot),
        ("crops", crops.CropSnapshot),
        ("flows", flows.FlowSnapshot),
    ):
        assert isinstance(getattr(rebuilt, attribute), expected), attribute


def test_nested_records_inside_the_fund_sections_survive():
    """Each of these is a list of dataclasses that ``asdict`` flattened."""
    rebuilt = context_from_dict(journalled(full_fund_context()))
    assert isinstance(rebuilt.carry.windows[0], carry.Window)
    assert isinstance(rebuilt.flows.windows[1], flows.FlowWindow)
    assert isinstance(rebuilt.energy.stocks[0], energy.Stock)
    assert isinstance(rebuilt.outlook.forecasts[0], outlook.Forecast)
    # Two levels down, and one of them is not in a list.
    assert isinstance(rebuilt.outlook.forecasts[0].now, outlook.Point)
    assert isinstance(rebuilt.outlook.forecasts[0].ahead[1], outlook.Point)
    assert rebuilt.carry.windows[1].annualised_pct == pytest.approx(-1.3)


def test_a_tuple_field_comes_back_a_tuple_not_a_list():
    """JSON stores it as a list; the annotation is the only record it was not."""
    rebuilt = context_from_dict(journalled(full_fund_context()))
    assert rebuilt.outlook.forecasts[0].next_year == (2027, 61.4)
    assert isinstance(rebuilt.outlook.forecasts[0].next_year, tuple)


def test_an_earnings_record_round_trips_for_a_company():
    """The last journalled section a company can have, and it nests too."""
    original = full_context()
    object.__setattr__(original, "earnings", earnings.EarningsSnapshot(
        ticker="AAPL", beats=3, misses=1, in_line=0,
        quarters=[earnings.Quarter(period="2026-06-30", actual=1.42,
                                   estimate=1.35, surprise_pct=5.2)],
    ))
    rebuilt = context_from_dict(journalled(original))
    assert isinstance(rebuilt.earnings.quarters[0], earnings.Quarter)
    assert prompt_from_dict(journalled(original)) == original.as_prompt()


def test_news_sources_are_carried_back():
    """Not in the prompt, but it is how a reviewer reaches the article."""
    rebuilt = context_from_dict(journalled(full_fund_context()))
    assert rebuilt.sources[0]["url"] == "https://example.test/e"


# --- the list of sections must not be able to rot ------------------------


def test_every_journalled_section_is_rebuilt():
    """The regression that started this: a section in the journal, not here.

    ``SNAPSHOT_TYPES`` is derived from ``TickerContext``'s annotations, so
    this should hold by construction -- which is the point. It fails the day
    somebody goes back to writing the list out by hand and forgets one.
    """
    journalled_keys = set(full_fund_context().as_dict())
    handled = set(SNAPSHOT_TYPES) | PASSTHROUGH_KEYS
    assert journalled_keys - handled == set()


def test_the_derived_section_list_matches_the_dataclass():
    """Every ``Optional[Snapshot]`` field on the context, and only those."""
    hints = get_type_hints(TickerContext)
    expected = {
        spec.name
        for spec in dataclasses.fields(TickerContext)
        if any(is_dataclass(arg) for arg in get_args(hints[spec.name]))
    }
    assert set(SNAPSHOT_TYPES) == expected
    for name, cls in SNAPSHOT_TYPES.items():
        assert is_dataclass(cls), name


def test_every_prompt_section_can_be_rebuilt():
    """``as_prompt`` reads these attributes; all of them must be restorable."""
    for _, attribute in ENRICHMENT_SECTIONS:
        assert attribute in SNAPSHOT_TYPES, attribute


# --- a partial or damaged line must not take the harness down ------------


def test_a_fund_line_missing_every_optional_section_rebuilds():
    """The common shape in the archive: a fund on a cycle with no EIA key."""
    payload = journalled(full_fund_context())
    for key in ("energy", "outlook", "crops", "flows", "positioning", "carry"):
        payload[key] = None
    rebuilt = context_from_dict(payload)
    assert rebuilt.energy is None
    # Omitted outright rather than rendered as a form of blanks.
    assert "ENERGY INVENTORIES" not in rebuilt.as_prompt()
    assert "MACRO" in rebuilt.as_prompt()


def test_a_fund_line_written_before_a_section_existed_rebuilds():
    payload = journalled(full_fund_context())
    for key in ("carry", "crops", "outlook"):
        del payload[key]
    rebuilt = context_from_dict(payload)
    assert rebuilt.carry is None
    assert rebuilt.crops is None


def test_a_malformed_nested_record_degrades_rather_than_raising():
    """One damaged corner of an old line must not cost the whole line."""
    payload = journalled(full_fund_context())
    payload["carry"]["windows"] = "not a list of windows"
    payload["energy"]["stocks"] = [None, 7]
    rebuilt = context_from_dict(payload)
    assert rebuilt.carry.windows == "not a list of windows"
    assert rebuilt.energy.stocks == [None, 7]


def test_an_unknown_nested_field_is_ignored():
    payload = journalled(full_fund_context())
    payload["carry"]["windows"][0]["basis"] = 1.0
    rebuilt = context_from_dict(payload)
    assert rebuilt.carry.windows[0].gap == -0.004


def test_a_nested_record_missing_a_required_field_is_refused():
    """``outlook.Point`` has no defaults, so there is nothing honest to use."""
    payload = journalled(full_fund_context())
    del payload["outlook"]["forecasts"][0]["now"]["value"]
    with pytest.raises(RebuildError) as excinfo:
        context_from_dict(payload)
    assert "Point" in str(excinfo.value)


def test_every_recorded_fund_line_in_the_archive_rebuilds():
    """The real journal, not a fixture -- the lines the harness will meet.

    ``logs/signal_journal.log`` is committed, so this is a real archive with
    the schema drift four months of live cycles actually produced, which no
    hand-written payload would think to reproduce. Read through the repo root
    rather than ``cfg``: the autouse fixture in ``conftest`` redirects
    ``SIGNAL_JOURNAL_PATH`` to a tmp dir so no test can write into ``logs/``,
    and that redirect is worth keeping even though this test only reads.
    """
    path = Path(__file__).resolve().parents[1] / "logs" / "signal_journal.log"
    if not path.exists():
        pytest.skip("no signal journal in this checkout")

    seen = 0
    enriched = 0
    for number, line in enumerate(path.read_text().splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        context = json.loads(line).get("context")
        if not isinstance(context, dict) or not is_fund(context.get("ticker", "")):
            continue
        seen += 1
        rebuilt = context_from_dict(context)
        # A second trip through the journal must change nothing: the prompt a
        # replay renders has to be a fixed point, or replaying a replay drifts.
        assert prompt_from_dict(journalled(rebuilt)) == rebuilt.as_prompt(), number
        for key, cls in SNAPSHOT_TYPES.items():
            if context.get(key) is not None:
                assert isinstance(getattr(rebuilt, key), cls), f"{number}: {key}"
        if "MACRO" in rebuilt.as_prompt():
            enriched += 1

    # Not a smoke test: the truncated rebuild passed the loop above on every
    # one of these lines by rendering three sections and comparing them to
    # themselves. These two numbers are what it could not have produced.
    assert seen > 300, seen
    assert enriched > seen // 2, (enriched, seen)
