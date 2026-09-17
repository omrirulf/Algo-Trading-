"""A ticker that has a contract and no positioning has failed, not abstained.

Absent is not failed, and ``CONTRACTS`` is what decides which one this is. A
fund with no futures contract was never going to have this section, so
nothing is said. A fund *with* one is a promise that the block exists, so
silence there has to read as a failure.

It did not. Both ways a mapping dies -- an exact name that matches no market,
and a series whose newest row is too old -- end with no snapshot and no
exception, and so produced an omission indistinguishable from a fund that
never had a contract. Five mappings sat on names the CFTC retired in
February 2022 and nothing in a single cycle said a word about it.
"""

from __future__ import annotations

from datetime import date, timedelta

import pandas as pd
import pytest

from orchestrator import context, positioning

HEADLINES = ["Something happened — (Reuters, 1 hour ago)"]


def make_frame(closes):
    index = pd.date_range("2024-01-01", periods=len(closes), freq="B")
    return pd.DataFrame(
        {"Open": closes, "High": [c * 1.01 for c in closes],
         "Low": [c * 0.99 for c in closes], "Close": closes,
         "Volume": [1_000_000] * len(closes)},
        index=index,
    )


def cot_rows(*, weeks: int = 30, age_days: int = 3):
    """Weekly rows ending ``age_days`` ago, newest first."""
    newest = date.today() - timedelta(days=age_days)
    return [
        {
            "market_and_exchange_names": "GOLD - COMMODITY EXCHANGE INC.",
            "report_date_as_yyyy_mm_dd": (newest - timedelta(weeks=w)).isoformat(),
            "open_interest_all": "400000",
            "m_money_positions_long_all": "240000",
            "m_money_positions_short_all": "160000",
        }
        for w in range(weeks)
    ]


class Provider:
    """Returns a canned payload, as the real provider's `fetch` would."""

    def __init__(self, rows):
        self.payload = context.RawMarketData(
            history=make_frame([100.0 + i * 0.1 for i in range(300)]),
            positioning_rows=list(rows),
        )

    def fetch(self, ticker: str) -> context.RawMarketData:
        return self.payload


def gather(ticker, rows):
    return context.gather(ticker, HEADLINES, provider=Provider(rows))


def positioning_gaps(ctx):
    return [gap for gap in ctx.gaps if gap.startswith("CFTC positioning")]


# --- the hole this closes ---------------------------------------------------

def test_a_mapping_that_matches_no_market_says_so():
    """The rename case: the query is valid, the answer is empty."""
    ctx = gather("GLD", [])
    assert ctx.positioning is None
    (gap,) = positioning_gaps(ctx)
    assert "GOLD - COMMODITY EXCHANGE INC." in gap
    assert "not reporting" in gap


def test_a_series_whose_newest_row_is_too_old_says_so():
    """The staleness case: rows come back, and every one of them is history."""
    stale = cot_rows(age_days=positioning.MAX_REPORT_AGE_DAYS + 60)
    ctx = gather("GLD", stale)
    assert ctx.positioning is None
    assert len(positioning_gaps(ctx)) == 1


def test_the_gap_reaches_the_prompt_the_model_reads():
    prompt = gather("GLD", []).as_prompt()
    assert "GOLD - COMMODITY EXCHANGE INC. is not reporting" in prompt
    assert "POSITIONING (CFTC, weekly)" not in prompt


# --- and what it must not do ------------------------------------------------

def test_a_ticker_with_no_contract_stays_silent():
    """MSFT has no futures contract. That is an absence, not a failure."""
    assert positioning.contract_for("MSFT") is None
    assert positioning_gaps(gather("MSFT", [])) == []


def test_a_healthy_contract_records_no_gap():
    ctx = gather("GLD", cot_rows())
    assert ctx.positioning is not None
    assert positioning_gaps(ctx) == []


def test_a_parse_that_failed_loudly_is_not_reported_twice(monkeypatch):
    """One gap for one thing, and the failure's own message is the better one.

    Forced rather than provoked with malformed rows: the parser is built to
    survive those without raising, so a test that fed it nonsense and saw one
    gap would be watching this path never run and calling it covered.
    """
    def explode(*args, **kwargs):
        raise RuntimeError("HTTP 503")

    monkeypatch.setattr(context.positioning, "build_snapshot", explode)
    ctx = gather("GLD", cot_rows())
    assert ctx.positioning is None
    (gap,) = positioning_gaps(ctx)
    assert "RuntimeError" in gap or "503" in gap
    assert "not reporting" not in gap


@pytest.mark.parametrize("ticker", sorted(positioning.CONTRACTS))
def test_every_mapped_ticker_is_covered_by_this(ticker):
    """Whatever the watchlist becomes, a mapping cannot go quiet."""
    assert positioning_gaps(gather(ticker, [])), f"{ticker} went silent"
