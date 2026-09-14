"""A replayed prompt must be the prompt the model actually saw.

This is the load-bearing property of the whole harness. If reconstruction is
lossy, every comparison downstream is measuring a prompt nobody was ever
shown, and the result looks like evidence while being noise.
"""

from __future__ import annotations

import pytest

from orchestrator import analysts, fundamentals, insiders, technicals
from orchestrator.context import TickerContext
from replay.rebuild import RebuildError, context_from_dict, prompt_from_dict


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
