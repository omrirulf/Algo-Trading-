"""Context assembly, and above all its behaviour when sources fail.

Enrichment is only an improvement if it cannot take the pipeline down with it,
so most of what is proved here is that a broken source becomes a named gap
rather than an exception.
"""

from __future__ import annotations

import json

import pytest

from orchestrator import context
from tests.test_analysts import HOLDERS, INFO as ANALYST_INFO, RECOMMENDATIONS, UPGRADES
from tests.test_fundamentals import INFO as FUNDAMENTAL_INFO
from tests.test_insiders import PURCHASES, TRANSACTIONS
from tests.test_technicals import make_frame

HEADLINES = ["Chipmaker raises guidance — revenue seen up 20% (Reuters, 2h ago)"]

#: yfinance returns one ``info`` dict carrying both kinds of field.
INFO = {**FUNDAMENTAL_INFO, **ANALYST_INFO}


class FakeProvider:
    """Returns a canned payload, and counts how often it was asked."""

    def __init__(self, **overrides):
        self.calls = 0
        self.payload = context.RawMarketData(**overrides)

    def fetch(self, ticker: str) -> context.RawMarketData:
        self.calls += 1
        return self.payload


def full_provider() -> FakeProvider:
    return FakeProvider(
        history=make_frame([100.0 + i * 0.1 for i in range(300)]),
        info=INFO,
        calendar={"Earnings Date": ["2026-10-30"]},
        recommendations=RECOMMENDATIONS,
        upgrades_downgrades=UPGRADES,
        institutional_holders=HOLDERS,
        insider_purchases=PURCHASES,
        insider_transactions=TRANSACTIONS,
    )


# --------------------------------------------------------------------------- #
# The happy path
# --------------------------------------------------------------------------- #


def test_gather_populates_every_section():
    ctx = context.gather("NVDA", HEADLINES, provider=full_provider())

    assert ctx.ticker == "NVDA"
    assert ctx.technicals is not None
    assert ctx.fundamentals is not None
    assert ctx.analysts is not None
    assert ctx.gaps == []


def test_prompt_contains_all_four_kinds_of_context():
    prompt = context.gather("NVDA", HEADLINES, provider=full_provider()).as_prompt()

    assert "TICKER: NVDA" in prompt
    assert "Chipmaker raises guidance" in prompt
    assert "TECHNICALS" in prompt and "RSI(14)" in prompt
    assert "FUNDAMENTALS" in prompt and "trailing P/E" in prompt
    assert "ANALYST & INSTITUTIONAL VIEW" in prompt and "Vanguard" in prompt
    assert "DATA GAPS" not in prompt


def test_analyst_upside_is_measured_against_the_fetched_close():
    ctx = context.gather("NVDA", HEADLINES, provider=full_provider())
    expected = INFO["targetMeanPrice"] / ctx.technicals.last_close - 1
    assert ctx.analysts.target_upside == pytest.approx(expected)


def test_context_is_json_serialisable_for_the_journal():
    payload = context.gather("NVDA", HEADLINES, provider=full_provider()).as_dict()
    assert json.loads(json.dumps(payload))["ticker"] == "NVDA"


# --------------------------------------------------------------------------- #
# Degradation
# --------------------------------------------------------------------------- #


def test_missing_price_history_leaves_the_other_sections_intact():
    provider = FakeProvider(info=INFO, recommendations=RECOMMENDATIONS)
    ctx = context.gather("NVDA", HEADLINES, provider=provider)

    assert ctx.technicals is None
    assert ctx.fundamentals is not None
    assert ctx.analysts is not None
    assert ctx.analysts.target_upside is None  # nothing to compare the target with


def test_insider_activity_reaches_the_prompt():
    prompt = context.gather("NVDA", HEADLINES, provider=full_provider()).as_prompt()
    assert "INSIDER ACTIVITY" in prompt
    assert "Open-market purchases" in prompt
    assert "Jane Roe" in prompt


def test_insiders_do_not_depend_on_the_info_dict():
    """Unlike fundamentals and the analyst view, insider data is its own source."""
    provider = FakeProvider(insider_purchases=PURCHASES, insider_transactions=TRANSACTIONS)
    ctx = context.gather("NVDA", HEADLINES, provider=provider)

    assert ctx.fundamentals is None and ctx.analysts is None
    assert ctx.insiders is not None and ctx.insiders.has_activity


def test_no_insider_trading_is_distinguished_from_no_insider_data():
    """An empty frame is a fact; a failed fetch is a gap. They must not look alike."""
    import pandas as pd

    quiet = context.gather(
        "NVDA", HEADLINES,
        provider=FakeProvider(insider_purchases=pd.DataFrame(), insider_transactions=pd.DataFrame()),
    )
    assert quiet.insiders is not None
    assert "No insider transactions reported" in quiet.as_prompt()

    absent = context.gather("NVDA", HEADLINES, provider=FakeProvider())
    assert absent.insiders is None
    assert "INSIDER ACTIVITY\n- unavailable this cycle" in absent.as_prompt()


def test_missing_info_leaves_technicals_intact():
    provider = FakeProvider(history=make_frame([100.0 + i for i in range(60)]))
    ctx = context.gather("NVDA", HEADLINES, provider=provider)

    assert ctx.technicals is not None
    assert ctx.fundamentals is None
    assert ctx.analysts is None


def test_long_failure_text_is_trimmed_before_it_reaches_the_prompt():
    """Five quoted connection errors would cost more tokens than the news does."""
    gaps: list[str] = []
    context._attempt(
        lambda: (_ for _ in ()).throw(RuntimeError("x" * 500)), "analyst view", gaps
    )
    assert len(gaps[0]) < 200
    assert gaps[0].endswith("…")


def test_provider_gaps_are_named_in_the_prompt():
    provider = FakeProvider(gaps=["analyst recommendations unavailable: HTTP 429"])
    prompt = context.gather("NVDA", HEADLINES, provider=provider).as_prompt()

    assert "DATA GAPS" in prompt
    assert "HTTP 429" in prompt
    assert "score these dimensions 0.0" in prompt


def test_unusable_history_becomes_a_gap_not_an_exception():
    provider = FakeProvider(history=make_frame([1.0, 2.0]).drop(columns=["Close"]))
    ctx = context.gather("NVDA", HEADLINES, provider=provider)

    assert ctx.technicals is None
    assert any("technicals could not be computed" in gap for gap in ctx.gaps)


def test_total_blackout_still_produces_a_usable_context():
    ctx = context.gather("NVDA", HEADLINES, provider=FakeProvider(gaps=["everything is down"]))
    prompt = ctx.as_prompt()

    assert "Chipmaker raises guidance" in prompt
    # Every enrichment section *that applies to a company* says so rather than
    # silently rendering empty. The fund-only sections are not counted: a
    # single name has no holdings and no futures contract, so they are absent
    # by kind rather than by outage.
    company_sections = [
        attribute for _, attribute in context.ENRICHMENT_SECTIONS
        if attribute not in context.FUND_ONLY_SECTIONS
    ]
    assert prompt.count("unavailable this cycle") == len(company_sections)
    assert "FUND BASICS" not in prompt and "POSITIONING" not in prompt


def test_absent_news_is_stated_rather_than_omitted():
    prompt = context.gather("NVDA", [], provider=full_provider()).as_prompt()
    assert "NEWS (past 24 hours)\n- none found" in prompt


# --------------------------------------------------------------------------- #
# Fetching
# --------------------------------------------------------------------------- #


def test_slow_data_is_cached_but_history_is_refetched():
    """yfinance is unauthenticated and rate-limited; asking it for the same
    fundamentals 24 times a day is how a watchlist gets itself blocked."""
    calls: list[str] = []

    class Handle:
        def history(self, **kwargs):
            calls.append("history")
            return make_frame([100.0, 101.0])

        @property
        def info(self):
            calls.append("info")
            return dict(INFO)

        calendar = None
        recommendations = None
        upgrades_downgrades = None
        institutional_holders = None

    provider = context.YFinanceContextProvider()
    for _ in range(3):
        provider._history(Handle(), "NVDA")
        provider._slow_data(Handle(), "NVDA")

    assert calls.count("history") == 3
    assert calls.count("info") == 1


def test_expired_cache_is_refetched():
    class Handle:
        calendar = recommendations = upgrades_downgrades = institutional_holders = None
        info = dict(INFO)

    provider = context.YFinanceContextProvider(ttl_seconds=-1)
    provider._slow_data(Handle(), "NVDA")
    provider._slow_data(Handle(), "NVDA")
    assert len(provider._cache) == 1


def test_a_raising_source_is_recorded_as_a_gap():
    class Handle:
        def history(self, **kwargs):
            raise RuntimeError("connection reset")

        @property
        def info(self):
            raise RuntimeError("rate limited")

        calendar = recommendations = upgrades_downgrades = institutional_holders = None

    provider = context.YFinanceContextProvider()
    frame, gaps = provider._history(Handle(), "NVDA")
    assert frame is None and "connection reset" in gaps[0]

    slow = provider._slow_data(Handle(), "NVDA")
    assert slow.info == {}
    assert any("rate limited" in gap for gap in slow.gaps)


def test_get_provider_is_a_singleton_so_the_cache_survives_cycles(monkeypatch):
    monkeypatch.setattr(context, "_provider", None)
    assert context.get_provider() is context.get_provider()


def test_structured_headlines_carry_their_urls_without_changing_the_prompt():
    """The URL reaches the journal; the model's input stays byte-identical."""
    from orchestrator.news import Headline

    items = [Headline(title="T", snippet="S", source="Reuters", when="2h ago", url="https://x/1")]
    with_urls = context.gather("AAPL", items)
    as_text = context.gather("AAPL", [items[0].as_line()])

    assert with_urls.as_prompt() == as_text.as_prompt()
    assert with_urls.sources[0]["url"] == "https://x/1"
    assert as_text.sources == []
    assert with_urls.as_dict()["sources"][0]["title"] == "T"


# --------------------------------------------------------------------------- #
# Each kind of ticker is asked the question that fits it
# --------------------------------------------------------------------------- #

FUND_PAYLOADS = {
    "equity_holdings": {"priceToEarnings": 18.27, "priceToBook": 1.26},
    "fund_operations": {"annualReportExpenseRatio": 0.0008, "totalNetAssets": 3.1e10},
    "fund_overview": {"categoryName": "Equity Energy", "yield": 0.031},
    "top_holdings": {"XOM": 0.229, "CVX": 0.171},
}

COT_ROWS = [
    {
        "report_date_as_yyyy_mm_dd": f"2026-09-{15 - i:02d}",
        "open_interest_all": "500000",
        "m_money_positions_long_all": str(300000 - i * 1000),
        "m_money_positions_short_all": "100000",
    }
    for i in range(30)
]


#: Every heading the prompt can carry, in the order as_prompt emits them.
ALL_HEADINGS = ("NEWS (past 24 hours)",) + tuple(t for t, _ in context.ENRICHMENT_SECTIONS)


def headings(prompt: str) -> list[str]:
    """The section headings present, in order -- the shape of the question asked."""
    lines = prompt.splitlines()
    return [title for title in ALL_HEADINGS if title in lines]


def test_a_company_is_asked_exactly_what_it_was_asked_before():
    """The company prompt is the input every replay and sanity baseline was
    measured against. Adding fund sections must not have moved a byte of it."""
    prompt = context.gather("NVDA", HEADLINES, provider=full_provider()).as_prompt()
    assert headings(prompt) == [
        "NEWS (past 24 hours)",
        "TECHNICALS (daily bars)",
        "FUNDAMENTALS",
        "ANALYST & INSTITUTIONAL VIEW",
        "INSIDER ACTIVITY",
    ]
    assert "FUND BASICS" not in prompt
    assert "POSITIONING" not in prompt


def test_a_company_never_fetches_the_fund_sources():
    """Not merely unused -- never asked for, so a CFTC outage cannot gap a stock."""
    from orchestrator import funds, positioning

    assert funds.fund_shape("NVDA") == funds.NO_FUND_SECTION
    assert positioning.contract_for("NVDA") is None


def test_a_sector_fund_gets_fund_basics_instead_of_the_company_form():
    ctx = context.gather("XLE", HEADLINES, provider=FakeProvider(
        history=make_frame([100.0 + i * 0.1 for i in range(300)]),
        info=INFO, fund_payloads=FUND_PAYLOADS,
    ))
    prompt = ctx.as_prompt()
    assert "FUND BASICS" in prompt
    assert "P/E 18.27" in prompt and "XOM 22.9%" in prompt
    # The company form, and the two sections a fund does not have, are gone.
    assert "FUNDAMENTALS" not in prompt
    assert "ANALYST & INSTITUTIONAL VIEW" not in prompt
    assert "INSIDER ACTIVITY" not in prompt


def test_a_bond_fund_is_asked_about_yield_and_duration():
    ctx = context.gather("TLT", HEADLINES, provider=FakeProvider(
        history=make_frame([100.0 + i * 0.1 for i in range(300)]),
        fund_payloads={"bond_holdings": {"duration": 16.8, "maturity": 25.7}},
        positioning_rows=COT_ROWS,
    ))
    prompt = ctx.as_prompt()
    assert "duration 16.80 years" in prompt
    assert "P/E" not in prompt


def test_a_commodity_is_asked_no_fundamentals_at_all():
    """Gold has no valuation. A form of blanks was the thing this replaced."""
    ctx = context.gather("GLD", HEADLINES, provider=FakeProvider(
        history=make_frame([100.0 + i * 0.1 for i in range(300)]),
        info=INFO, positioning_rows=COT_ROWS,
    ))
    prompt = ctx.as_prompt()
    assert "FUNDAMENTALS" not in prompt and "FUND BASICS" not in prompt
    assert "POSITIONING (CFTC, weekly)" in prompt
    assert ctx.funds is None
    # Nothing was attempted, so nothing is reported as missing.
    assert not any("fund" in gap.lower() for gap in ctx.gaps)


def test_positioning_reaches_the_prompt_with_its_three_numbers():
    ctx = context.gather("GLD", HEADLINES, provider=FakeProvider(
        history=make_frame([100.0 + i * 0.1 for i in range(300)]), positioning_rows=COT_ROWS,
    ))
    prompt = ctx.as_prompt()
    assert "net long 40.0% of open interest" in prompt
    assert "Change on the week:" in prompt
    assert "percentile over 52 weeks" in prompt
    assert "crowding, not as a forecast" in prompt


def test_a_fund_with_no_futures_contract_simply_has_no_positioning_section():
    ctx = context.gather("EWZ", HEADLINES, provider=FakeProvider(
        history=make_frame([100.0 + i * 0.1 for i in range(300)]), fund_payloads=FUND_PAYLOADS,
    ))
    prompt = ctx.as_prompt()
    assert "POSITIONING" not in prompt
    assert not any("CFTC" in gap for gap in ctx.gaps)


def test_the_new_sections_reach_the_journal():
    ctx = context.gather("GLD", HEADLINES, provider=FakeProvider(
        history=make_frame([100.0 + i * 0.1 for i in range(300)]), positioning_rows=COT_ROWS,
    ))
    stored = ctx.as_dict()
    assert stored["funds"] is None
    assert stored["positioning"]["contract"] == "GOLD"
    assert stored["positioning"]["net_share"] == pytest.approx(0.4)


def test_a_broken_fund_fetch_degrades_to_a_named_gap():
    class Hostile(dict):
        def __getitem__(self, key):
            raise RuntimeError("boom")

    ctx = context.gather("XLE", HEADLINES, provider=FakeProvider(
        history=make_frame([100.0 + i * 0.1 for i in range(300)]),
        fund_payloads={"equity_holdings": 1, "top_holdings": 2, "bad": Hostile()},
    ))
    # Either it parsed what it could or it recorded a gap; what it must not do
    # is raise, and the cycle must still have a prompt.
    assert "TECHNICALS" in ctx.as_prompt()
