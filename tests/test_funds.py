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
    "equity_holdings": {
        "priceToEarnings": 18.27, "priceToBook": 1.26, "priceToSales": 1.55,
        "threeYearEarningsGrowth": 0.121,
    },
    "fund_operations": {"annualReportExpenseRatio": 0.0008, "totalNetAssets": 3.1e10},
    "fund_overview": {"categoryName": "Equity Energy"},
    "top_holdings": {"XOM": 0.229, "CVX": 0.171, "COP": 0.043},
    "sector_weightings": {"energy": 0.99, "utilities": 0.01},
    "asset_classes": {"stockPosition": 0.985, "cashPosition": 0.015, "bondPosition": 0.0},
    "info": {"yield": 0.031, "totalAssets": 3.1e10, "threeYearAverageReturn": 0.094,
             "beta3Year": 0.71},
}
BOND_PAYLOAD = {
    "bond_holdings": {"duration": 16.8, "maturity": 25.7, "creditQuality": 1.2},
    "bond_ratings": {"aa": 0.96, "aaa": 0.03, "other": 0.01, "us_government": 0.95},
    "fund_operations": {"annualReportExpenseRatio": 0.0015, "totalNetAssets": 0.0},
    "fund_overview": {"categoryName": "Long Government"},
    "info": {"yield": 0.045, "totalAssets": 4.8e10, "threeYearAverageReturn": -0.006,
             "beta3Year": 2.39},
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
    assert "P/E 18.27" in text and "P/B 1.26" in text and "P/S 1.55" in text
    assert "3y earnings growth +12.1%" in text
    assert "Yield: 3.1%" in text
    assert "Three-year record: +9.4% a year" in text and "beta to the market 0.71" in text
    assert "expense ratio 0.08%" in text and "31.00B" in text
    assert "XOM 22.9%" in text and "CVX 17.1%" in text
    assert "Energy 99.0%" in text
    assert "Stocks 98.5%" in text
    # The bond lines belong to the other shape.
    assert "duration" not in text.lower()


def test_a_bond_fund_is_described_by_yield_and_credit():
    text = "\n".join(funds.build_snapshot("TLT", **BOND_PAYLOAD).as_lines())
    assert "Yield: 4.5%" in text
    assert "Credit quality: AA 96.0%, AAA 3.0%" in text
    assert "US government debt 95.0%" in text
    assert "Three-year record: -0.6% a year" in text
    assert "48.00B" in text
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


@pytest.mark.parametrize("sane", [1.5, 18.27, 120.0, 999.0])
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


# --- the four defects the first live run exposed ------------------------------
#
# The block connected to Yahoo on the first try and returned wrong numbers,
# which is the more expensive half of "it works". Each of these pins one of
# them against the shape yfinance actually hands over in production: a frame
# indexed by the printed field name, with the fund's own column first and the
# category average second.


def _equity_frame(**values):
    """``equity_holdings`` exactly as yfinance builds it."""
    pd = pytest.importorskip("pandas")
    order = [
        ("Price/Earnings", "priceToEarnings"), ("Price/Book", "priceToBook"),
        ("Price/Sales", "priceToSales"), ("Price/Cashflow", "priceToCashflow"),
        ("Median Market Cap", "medianMarketCap"),
        ("3 Year Earnings Growth", "threeYearEarningsGrowth"),
    ]
    return pd.DataFrame({
        "Average": [label for label, _ in order],
        "XLE": [values.get(key, pd.NA) for _, key in order],
        "Category Average": [pd.NA] * len(order),
    }).set_index("Average")


def _bond_frame(**values):
    """``bond_holdings`` exactly as yfinance builds it."""
    pd = pytest.importorskip("pandas")
    order = [("Duration", "duration"), ("Maturity", "maturity"),
             ("Credit Quality", "creditQuality")]
    return pd.DataFrame({
        "Average": [label for label, _ in order],
        "TLT": [values.get(key, pd.NA) for _, key in order],
        "Category Average": [pd.NA] * len(order),
    }).set_index("Average")


def test_the_real_yfinance_frame_is_read_from_the_funds_own_column():
    """Not the category average sitting next to it."""
    snapshot = funds.build_snapshot("XLE", equity_holdings=_equity_frame(
        priceToEarnings=18.27, priceToBook=1.26, threeYearEarningsGrowth=0.121))
    assert snapshot.holdings_pe == 18.27
    assert snapshot.holdings_pb == 1.26
    assert snapshot.holdings_earnings_growth == pytest.approx(0.121)


def test_an_inverted_ratio_block_is_turned_the_right_way_up():
    """XLE came back with a "P/E" of 0.0597. That is 1/16.75 -- an earnings
    yield wearing a P/E's name, because Yahoo's raw field is stored inverted
    and only its own formatter flips it back."""
    snapshot = funds.build_snapshot("XLE", equity_holdings=_equity_frame(
        priceToEarnings=0.0597, priceToBook=0.4, priceToSales=0.8))
    assert snapshot.holdings_pe == pytest.approx(16.75, abs=0.01)
    assert snapshot.holdings_pb == pytest.approx(2.5)
    assert snapshot.holdings_ps == pytest.approx(1.25)


@pytest.mark.parametrize("inverted,upright", [(0.06, 16.67), (0.03, 33.33), (0.10, 10.0)])
def test_the_three_funds_that_were_wrong_live_come_back_right(inverted, upright):
    """XLE 0.06, SMH 0.03 and EWZ 0.10 in the first live run."""
    snapshot = funds.build_snapshot("XLE", equity_holdings={"priceToEarnings": inverted})
    assert snapshot.holdings_pe == pytest.approx(upright, abs=0.01)


def test_a_ratio_block_that_is_already_upright_is_left_alone():
    snapshot = funds.build_snapshot("XLE", equity_holdings=_equity_frame(
        priceToEarnings=18.27, priceToBook=0.84))
    assert snapshot.holdings_pe == 18.27
    # A P/B under 1 is real for a value basket, and is only inverted when the
    # P/E beside it says the whole block is upside down.
    assert snapshot.holdings_pb == 0.84


def test_the_yield_comes_from_info_because_the_fund_payload_has_none():
    """``fund_overview`` carries the category, the family and the legal type,
    and was asked for a yield it could never hold. Every fund read "n/a"."""
    assert funds.build_snapshot("XLE", fund_overview={"yield": 0.031}).dividend_yield is None
    assert funds.build_snapshot("XLE", info={"yield": 0.031}).dividend_yield == 0.031


@pytest.mark.parametrize("info,expected", [
    ({"yield": 0.0295}, 0.0295),
    ({"dividendYield": 2.95}, 0.0295),
    ({"yield": 4.2}, 0.042),
    ({"yield": 0.0, "dividendYield": 3.1}, 0.031),
    ({"dividendYield": None}, None),
])
def test_a_yield_is_read_as_a_fraction_whichever_way_yahoo_spelled_it(info, expected):
    value = funds.build_snapshot("XLE", info=info).dividend_yield
    if expected is None:
        assert value is None
    else:
        assert value == pytest.approx(expected)


def test_credit_quality_reads_as_a_ratings_mix_not_a_bare_number():
    """A "1.20" told the model nothing. "US government 96%" tells it what the
    fund is, and it is the field Yahoo actually populates."""
    snapshot = funds.build_snapshot(
        "HYG", bond_ratings={"bb": 0.52, "b": 0.33, "ccc": 0.09, "aaa": 0.01, "other": 0.05})
    assert snapshot.credit_mix[:2] == ["BB 52.0%", "B 33.0%"]
    assert len(snapshot.credit_mix) == funds.MAX_RATING_BUCKETS
    assert "Credit quality: BB 52.0%" in "\n".join(snapshot.as_lines())


def test_a_bond_fund_with_no_ratings_says_so_rather_than_inventing_one():
    snapshot = funds.build_snapshot("TLT", bond_holdings=_bond_frame(duration=16.8))
    assert snapshot.credit_mix == []
    assert "Credit quality: n/a" in "\n".join(snapshot.as_lines())


@pytest.mark.parametrize("impossible", [0.0, -1.0, 40.0, 4000.0])
def test_a_duration_that_cannot_be_a_span_of_years_is_suppressed(impossible):
    assert funds.build_snapshot(
        "TLT", bond_holdings=_bond_frame(duration=impossible)).duration is None


def test_a_real_duration_survives_the_band_but_is_still_not_shown():
    """Parsed and journalled, so the decision is reversible from data. Not put
    in front of the model, because the data is wrong -- see the next test."""
    snapshot = funds.build_snapshot("TLT", bond_holdings=_bond_frame(duration=16.8))
    assert snapshot.duration == 16.8
    assert funds.SHOW_BOND_DURATION is False
    assert "duration" not in "\n".join(snapshot.as_lines()).lower()


def test_yahoos_own_bond_durations_are_why_the_line_is_gone():
    """The live probe returned `duration 3.6` for TLT, a 20+ year Treasury
    fund whose real duration is about sixteen and a half, and `6.65` for HYG,
    whose real duration is about three and a half. Wrong in both directions,
    with nothing in the payload to say which funds are right."""
    tlt = funds.build_snapshot("TLT", bond_holdings=_bond_frame(duration=3.6, maturity=7.693))
    hyg = funds.build_snapshot("HYG", bond_holdings=_bond_frame(duration=6.65, maturity=9.846))
    for text in ("\n".join(tlt.as_lines()), "\n".join(hyg.as_lines())):
        assert "3.60" not in text and "6.65" not in text
        assert "7.69" not in text and "9.85" not in text


def test_a_weighting_mix_is_sorted_largest_first_and_named_readably():
    snapshot = funds.build_snapshot("RSP", sector_weightings={
        "realestate": 0.03, "technology": 0.31, "financial_services": 0.13,
        "energy": 0.04, "utilities": 0.02, "healthcare": 0.11})
    assert snapshot.sector_mix == [
        "Technology 31.0%", "Financial services 13.0%", "Healthcare 11.0%", "Energy 4.0%"]


def test_what_a_fund_is_made_of_is_stated():
    """A "bond fund" that is a third cash is a different instrument."""
    snapshot = funds.build_snapshot("RSP", asset_classes={
        "stockPosition": 0.97, "cashPosition": 0.03, "bondPosition": 0.0,
        "preferredPosition": None})
    assert snapshot.asset_mix == ["Stocks 97.0%", "Cash 3.0%"]
    assert "What it is made of: Stocks 97.0%" in "\n".join(snapshot.as_lines())


def test_the_operations_frame_is_read_by_its_printed_row_names():
    """yfinance indexes it "Annual Report Expense Ratio", not the camelCase
    key the API uses. Only the camelCase spelling was being asked for."""
    pd = pytest.importorskip("pandas")
    frame = pd.DataFrame({
        "Attributes": ["Annual Report Expense Ratio", "Annual Holdings Turnover",
                       "Total Net Assets"],
        "XLE": [0.0008, 0.05, 3.1e10],
        "Category Average": [0.01, 0.6, 1e9],
    }).set_index("Attributes")
    snapshot = funds.build_snapshot("XLE", fund_operations=frame)
    assert snapshot.expense_ratio == 0.0008


def test_the_real_top_holdings_frame_is_read():
    pd = pytest.importorskip("pandas")
    frame = pd.DataFrame({
        "Symbol": ["XOM", "CVX", "COP"],
        "Name": ["Exxon Mobil Corp", "Chevron Corp", "ConocoPhillips"],
        "Holding Percent": [0.229, 0.171, 0.043],
    }).set_index("Symbol")
    snapshot = funds.build_snapshot("XLE", top_holdings=frame)
    assert snapshot.top_holdings[0] == "Exxon Mobil Corp 22.9%"


# --- the five more the raw payloads exposed -----------------------------------
#
# The first round of fixes was reasoned from yfinance's source, which gives
# the key names and says nothing about the values. Dumping the untouched
# Yahoo JSON for five real funds settled four questions and opened five more.
# These use the exact payloads the runner returned, quoted verbatim.

EWZ_LIVE = {
    "equity_holdings": {
        "priceToEarnings": 0.09543, "priceToBook": 0.55817,
        "priceToSales": 0.78365, "priceToCashflow": 0.18804,
    },
    "fund_operations": {
        "annualReportExpenseRatio": 0.0058999998, "annualHoldingsTurnover": 0.19,
        "totalNetAssets": 32828.75,
    },
    "fund_overview": {"categoryName": "Focused Region", "family": "iShares"},
    "asset_classes": {"cashPosition": 0.0269, "stockPosition": 0.9654,
                      "preferredPosition": 0.0077, "bondPosition": 0.0},
    "info": {"yield": 0.040700004, "dividendYield": 4.07, "trailingPE": 10.98785,
             "totalAssets": 8173754368, "threeYearAverageReturn": 0.1152231,
             "beta3Year": 0.84},
}
TLT_LIVE = {
    "bond_holdings": {"maturity": 7.693, "duration": 3.6},
    "bond_ratings": {"bb": 0.0, "aa": 1.0, "aaa": 0.0, "a": 0.0, "other": 0.0,
                     "b": 0.0, "bbb": 0.0, "below_b": 0.0, "us_government": 0.996},
    "fund_operations": {"annualReportExpenseRatio": 0.0015, "totalNetAssets": 0.0},
    "fund_overview": {"categoryName": "Long Government"},
    "asset_classes": {"cashPosition": 0.004, "stockPosition": 0.0,
                      "bondPosition": 0.996, "otherPosition": 0.0},
    "info": {"yield": 0.0473, "dividendYield": 4.73, "totalAssets": 47046328320,
             "threeYearAverageReturn": -0.0059244, "beta3Year": 2.39},
}
HYG_LIVE = {
    "bond_ratings": {"bb": 0.5788, "aa": 0.0, "aaa": 0.0, "a": 0.0, "other": 0.0055,
                     "b": 0.32209998, "bbb": 0.011, "below_b": 0.082600005,
                     "us_government": 0.0},
    "sector_weightings": {"utilities": 0.9959, "realestate": 0.0041, "energy": 0.0,
                          "financial_services": 0.0, "technology": 0.0},
    "fund_operations": {"annualReportExpenseRatio": 0.0049, "totalNetAssets": 0.0},
    "fund_overview": {"categoryName": "High Yield Bond"},
    "asset_classes": {"cashPosition": 0.0119, "bondPosition": 0.9863,
                      "preferredPosition": 0.0018000001},
    "info": {"yield": 0.0588, "totalAssets": 16186192896,
             "threeYearAverageReturn": 0.0779121, "beta3Year": 0.67},
}


def test_the_inversion_is_confirmed_by_yahoos_own_other_field():
    """EWZ's holdings `priceToEarnings` is 0.09543 and its `info.trailingPE` is
    10.99. 1/0.09543 = 10.48. Two independent fields agreeing is what turns
    the inversion from a reading of the data into a fact about it."""
    snapshot = funds.build_snapshot("EWZ", **EWZ_LIVE)
    assert snapshot.holdings_pe == pytest.approx(10.48, abs=0.05)
    assert abs(snapshot.holdings_pe - EWZ_LIVE["info"]["trailingPE"]) < 1.0
    assert snapshot.holdings_pb == pytest.approx(1.79, abs=0.01)
    assert snapshot.holdings_ps == pytest.approx(1.28, abs=0.01)


def test_net_assets_come_from_info_not_from_the_category_total():
    """`fund_operations.totalNetAssets` is the *category's* total in millions --
    SPY and its category average both report 513975.7, which rendered as a
    $514K fund. EWZ reports 32828.75 against real assets of $8.17bn."""
    snapshot = funds.build_snapshot("EWZ", **EWZ_LIVE)
    assert snapshot.total_assets == 8173754368
    assert "8.17B" in "\n".join(snapshot.as_lines())
    assert "32.83K" not in "\n".join(snapshot.as_lines())


def test_a_fund_that_reports_no_net_assets_anywhere_says_so():
    assert funds.build_snapshot(
        "XLE", fund_operations={"totalNetAssets": 4.2e10}).total_assets is None


def test_government_debt_is_pulled_out_of_the_ratings_ladder():
    """TLT returns `{"aa": 1.0, "us_government": 0.996}` -- the same bonds
    counted twice, which as a ladder sums to 199.6%."""
    snapshot = funds.build_snapshot("TLT", **TLT_LIVE)
    assert snapshot.credit_mix == ["AA 100.0%"]
    assert snapshot.government_share == pytest.approx(0.996)
    line = next(l for l in snapshot.as_lines() if l.startswith("Credit quality"))
    assert line == "Credit quality: AA 100.0% | US government debt 99.6%"


def test_a_credit_fund_keeps_its_whole_ladder_and_says_nothing_about_government():
    snapshot = funds.build_snapshot("HYG", **HYG_LIVE)
    assert snapshot.credit_mix == ["BB 57.9%", "B 32.2%", "Below B 8.3%", "BBB 1.1%"]
    assert not snapshot.government_share
    assert "US government" not in "\n".join(snapshot.as_lines())


def test_a_bond_fund_is_given_no_sector_mix_because_yahoos_is_nonsense():
    """HYG came back "utilities 99.6%", which is not what a high-yield
    corporate bond fund holds."""
    snapshot = funds.build_snapshot("HYG", **HYG_LIVE)
    assert snapshot.sector_mix == []
    assert "Utilities" not in "\n".join(snapshot.as_lines())


def test_an_equity_funds_sector_mix_is_kept_because_that_one_is_right():
    snapshot = funds.build_snapshot("EWZ", **dict(
        EWZ_LIVE, sector_weightings={"financial_services": 0.3405, "energy": 0.1743,
                                     "basic_materials": 0.1446, "utilities": 0.1244}))
    assert snapshot.sector_mix[0] == "Financial services 34.1%"


def test_the_three_year_record_and_beta_are_carried():
    """What a fund did and how hard it swung. Both verified against five live
    funds, and they carry the rate risk the dropped duration line was for:
    TLT's beta of 2.39 against HYG's 0.67 is the same story, measured."""
    tlt = funds.build_snapshot("TLT", **TLT_LIVE)
    hyg = funds.build_snapshot("HYG", **HYG_LIVE)
    assert "Three-year record: -0.6% a year | beta to the market 2.39" in "\n".join(tlt.as_lines())
    assert "Three-year record: +7.8% a year | beta to the market 0.67" in "\n".join(hyg.as_lines())


def test_an_expense_ratio_keeps_two_digits():
    """0.09% and 0.59% are different funds; one digit rounds both to 0.1%."""
    cheap = funds.build_snapshot("XLE", fund_operations={"annualReportExpenseRatio": 0.000945})
    dear = funds.build_snapshot("XLE", fund_operations={"annualReportExpenseRatio": 0.0059})
    assert "expense ratio 0.09%" in "\n".join(cheap.as_lines())
    assert "expense ratio 0.59%" in "\n".join(dear.as_lines())


def test_the_two_bond_funds_are_told_apart_by_what_survived():
    """The whole purpose of the block. Dropping duration cost nothing: a long
    Treasury fund and a high-yield credit fund are still unmistakable."""
    tlt = "\n".join(funds.build_snapshot("TLT", **TLT_LIVE).as_lines())
    hyg = "\n".join(funds.build_snapshot("HYG", **HYG_LIVE).as_lines())
    assert "Long Government" in tlt and "High Yield Bond" in hyg
    assert "US government debt 99.6%" in tlt and "BB 57.9%" in hyg
    assert "beta to the market 2.39" in tlt and "beta to the market 0.67" in hyg
    assert "Yield: 4.7%" in tlt and "Yield: 5.9%" in hyg


def test_every_line_of_the_three_live_funds_renders_without_a_stray_blank():
    """A block that is mostly `n/a` is the failure this module replaced."""
    for ticker, payload in (("EWZ", EWZ_LIVE), ("TLT", TLT_LIVE), ("HYG", HYG_LIVE)):
        lines = funds.build_snapshot(ticker, **payload).as_lines()
        assert sum("n/a" in line for line in lines) <= 1, (ticker, lines)
