"""Parsing yfinance's ``info`` dict, including the shapes it gets wrong."""

from __future__ import annotations

from datetime import date, datetime

import pandas as pd
import pytest

from orchestrator import fundamentals

INFO = {
    "sector": "Technology",
    "industry": "Consumer Electronics",
    "marketCap": 3_520_000_000_000,
    "trailingPE": 34.2,
    "forwardPE": 29.1,
    "priceToBook": 51.2,
    "trailingPegRatio": 2.4,
    "profitMargins": 0.243,
    "operatingMargins": 0.31,
    "revenueGrowth": 0.061,
    "earningsGrowth": -0.094,
    "returnOnEquity": 1.472,
    "debtToEquity": 145.0,
    "freeCashflow": 98_500_000_000,
    "shortPercentOfFloat": 0.008,
    "beta": 1.12,
}


def test_full_info_maps_onto_the_snapshot():
    snapshot = fundamentals.build_snapshot(INFO, {"Earnings Date": [date(2026, 10, 30)]})

    assert snapshot.sector == "Technology"
    assert snapshot.market_cap == 3_520_000_000_000
    assert snapshot.trailing_pe == pytest.approx(34.2)
    assert snapshot.profit_margin == pytest.approx(0.243)
    assert snapshot.earnings_growth == pytest.approx(-0.094)
    assert snapshot.debt_to_equity == pytest.approx(145.0)
    assert snapshot.next_earnings_date == "2026-10-30"


def test_empty_info_yields_an_all_none_snapshot_rather_than_an_error():
    snapshot = fundamentals.build_snapshot({})
    assert all(value is None for value in snapshot.as_dict().values())
    assert "n/a" in "\n".join(snapshot.as_lines())


def test_nan_values_are_treated_as_missing():
    snapshot = fundamentals.build_snapshot({"trailingPE": float("nan"), "beta": float("inf")})
    assert snapshot.trailing_pe is None
    assert snapshot.beta is None


def test_snapshot_is_json_serialisable():
    """Numpy scalars from yfinance must not reach the journal."""
    import json

    import numpy as np

    snapshot = fundamentals.build_snapshot({"marketCap": np.int64(5), "beta": np.float64(1.1)})
    assert json.loads(json.dumps(snapshot.as_dict()))["market_cap"] == 5


def test_rendered_lines_label_units_correctly():
    lines = "\n".join(fundamentals.build_snapshot(INFO).as_lines())
    assert "profit margin 24.3%" in lines
    assert "revenue +6.1%" in lines
    assert "earnings -9.4%" in lines
    assert "debt/equity 145.0%" in lines
    assert "market cap 3.52T" in lines
    assert "short interest 0.8% of float" in lines


# --------------------------------------------------------------------------- #
# Earnings date, which yfinance has shipped in several different shapes
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize(
    "calendar",
    [
        {"Earnings Date": [date(2026, 10, 30), date(2026, 11, 3)]},
        {"Earnings Date": date(2026, 10, 30)},
        {"Earnings Date": datetime(2026, 10, 30, 16, 30)},
        {"Earnings Date": "2026-10-30 16:30:00"},
        pd.DataFrame({"Value": [date(2026, 10, 30)]}, index=["Earnings Date"]),
    ],
)
def test_earnings_date_survives_every_known_shape(calendar):
    assert fundamentals.parse_earnings_date(calendar) == "2026-10-30"


@pytest.mark.parametrize("calendar", [None, {}, {"Earnings Date": []}, {"Earnings Date": None}])
def test_missing_earnings_date_is_none(calendar):
    assert fundamentals.parse_earnings_date(calendar) is None
