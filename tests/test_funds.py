"""A fund is described in the terms that apply to a fund.

The block this replaced handed an index the company form -- sector, market
cap, profit margin, next earnings -- which rendered as seven blanks and,
worse, occasionally as nonsense: the first 80-ticker cycle showed the model a
*forward P/E of -4,036.25* for a Treasury bond fund, and the model scored
that fund's fundamentals -0.1. These tests pin the three shapes and the
suppression that stops a number like that reaching a prompt again.
"""

from __future__ import annotations

import pytest

from orchestrator import funds

EQUITY_PAYLOAD = {
    "equity_holdings": {"priceToEarnings": 18.27, "priceToBook": 1.26, "threeYearEarningsGrowth": 0.121},
    "fund_operations": {"annualReportExpenseRatio": 0.0008, "totalNetAssets": 3.1e10},
    "fund_overview": {"categoryName": "Equity Energy", "yield": 0.031},
    "top_holdings": {"XOM": 0.229, "CVX": 0.171, "COP": 0.043},
    "sector_weightings": {"energy": 0.99, "utilities": 0.01},
}
BOND_PAYLOAD = {
    "bond_holdings": {"duration": 16.8, "maturity": 25.7, "creditQuality": 1.2},
    "fund_operations": {"annualReportExpenseRatio": 0.0015, "totalNetAssets": 4.8e10},
    "fund_overview": {"categoryName": "Long Government", "yield": 0.045},
}


# --- which shape each kind gets ----------------------------------------------


@pytest.mark.parametrize(
    "ticker,shape",
    [
        ("XLE", funds.EQUITY_FUND), ("RSP", funds.EQUITY_FUND), ("EWZ", funds.EQUITY_FUND),
        ("VNQ", funds.EQUITY_FUND),
        ("TLT", funds.BOND_FUND), ("SHY", funds.BOND_FUND), ("IEF", funds.BOND_FUND),
        ("TIP", funds.BOND_FUND), ("LQD", funds.BOND_FUND), ("HYG", funds.BOND_FUND),
        ("EMB", funds.BOND_FUND),
        ("GLD", funds.NO_FUND_SECTION), ("USO", funds.NO_FUND_SECTION),
        ("CORN", funds.NO_FUND_SECTION),
        ("MSFT", funds.NO_FUND_SECTION), ("LLY", funds.NO_FUND_SECTION),
    ],
)
def test_each_kind_gets_the_form_that_fits_it(ticker, shape):
    assert funds.fund_shape(ticker) == shape


def test_every_bond_fund_in_the_config_is_treated_as_one():
    from config.instruments import CREDIT, DURATION

    for ticker in DURATION + CREDIT:
        assert funds.fund_shape(ticker) == funds.BOND_FUND


def test_a_commodity_has_no_block_at_all():
    """Gold has no P/E, no yield and no holdings. A form of blanks was the bug."""
    for ticker in ("GLD", "SLV", "USO", "UNG", "CORN", "WEAT", "SOYB", "CANE", "CPER"):
        assert funds.build_snapshot(ticker, **EQUITY_PAYLOAD) is None


def test_a_single_name_has_no_block_either():
    assert funds.build_snapshot("MSFT", **EQUITY_PAYLOAD) is None


# --- what each block says -----------------------------------------------------


def test_an_equity_fund_is_described_by_what_it_holds():
    text = "\n".join(funds.build_snapshot("XLE", **EQUITY_PAYLOAD).as_lines())
    assert "Fund type: Equity Energy" in text
    assert "P/E 18.27" in text and "P/B 1.26" in text
    assert "3y earnings growth +12.1%" in text
    assert "Yield: 3.1%" in text
    assert "expense ratio 0.1%" in text and "31.00B" in text
    assert "XOM 22.9%" in text and "CVX 17.1%" in text
    assert "energy 99.0%" in text
    # The bond lines belong to the other shape.
    assert "duration" not in text.lower()


def test_a_bond_fund_is_described_by_yield_and_duration():
    text = "\n".join(funds.build_snapshot("TLT", **BOND_PAYLOAD).as_lines())
    assert "yield 4.5%" in text
    assert "duration 16.80 years" in text
    assert "average maturity 25.70 years" in text
    assert "Credit quality (1=highest): 1.20" in text
    # A bond fund has no price/earnings to speak of, so the line is not there.
    assert "P/E" not in text


def test_a_missing_number_reads_as_blank_not_as_zero():
    snapshot = funds.build_snapshot("XLE", fund_overview={"categoryName": "Equity Energy"})
    text = "\n".join(snapshot.as_lines())
    assert "P/E n/a" in text and "P/B n/a" in text
    assert "0.00" not in text


# --- the regression that started this ----------------------------------------


@pytest.mark.parametrize("nonsense", [-4036.25, -1.0, 0.0, 5000.0, 1e9])
def test_an_impossible_pe_is_suppressed_rather_than_shown(nonsense):
    """TLT was shown "forward P/E -4,036.25". A number the model cannot use is
    worse than a stated blank, because it looks usable."""
    snapshot = funds.build_snapshot("XLE", equity_holdings={"priceToEarnings": nonsense})
    assert snapshot.holdings_pe is None
    assert "P/E n/a" in "\n".join(snapshot.as_lines())


@pytest.mark.parametrize("sane", [0.5, 18.27, 120.0, 999.0])
def test_a_plausible_pe_survives(sane):
    assert funds.build_snapshot("XLE", equity_holdings={"priceToEarnings": sane}).holdings_pe == sane


# --- yfinance returns three different containers for the same thing -----------


def test_a_pandas_series_payload_is_read_the_same_as_a_dict():
    pd = pytest.importorskip("pandas")
    series = pd.Series({"priceToEarnings": 18.27, "priceToBook": 1.26})
    assert funds.build_snapshot("XLE", equity_holdings=series).holdings_pe == 18.27


def test_a_one_row_dataframe_payload_is_read_too():
    pd = pytest.importorskip("pandas")
    frame = pd.DataFrame([{"annualReportExpenseRatio": 0.0008, "totalNetAssets": 3.1e10}])
    assert funds.build_snapshot("XLE", fund_operations=frame).expense_ratio == 0.0008


def test_a_holdings_dataframe_with_names_and_weights_renders():
    pd = pytest.importorskip("pandas")
    frame = pd.DataFrame(
        {"Name": ["Exxon Mobil", "Chevron"], "Holding Percent": [0.229, 0.171]},
        index=["XOM", "CVX"],
    )
    text = "\n".join(funds.build_snapshot("XLE", top_holdings=frame).as_lines())
    assert "Exxon Mobil 22.9%" in text


def test_a_broken_payload_degrades_to_blanks_rather_than_raising():
    class Hostile:
        def __getattr__(self, name):
            raise RuntimeError("boom")

    snapshot = funds.build_snapshot("XLE", equity_holdings=Hostile(), top_holdings=Hostile())
    assert snapshot is not None and snapshot.holdings_pe is None
    assert snapshot.top_holdings == []


def test_info_fills_in_what_the_fund_payload_omits():
    snapshot = funds.build_snapshot("EWZ", info={"yield": 0.052, "category": "Latin America Equity"})
    assert snapshot.dividend_yield == 0.052
    assert snapshot.category == "Latin America Equity"


def test_the_snapshot_round_trips_through_the_journal():
    snapshot = funds.build_snapshot("XLE", **EQUITY_PAYLOAD)
    stored = snapshot.as_dict()
    assert stored["holdings_pe"] == 18.27 and stored["shape"] == funds.EQUITY_FUND
    assert funds.FundSnapshot(**stored).as_lines() == snapshot.as_lines()
