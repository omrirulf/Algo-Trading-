"""The CFTC weekly report, the fund world's answer to insider filings.

Nobody files a Form 4 on gold. But every large trader must report their
futures position, and the CFTC publishes the aggregate every Friday -- so
"what is informed money doing" *is* answerable for a commodity or a bond
fund, from a free official source.

These tests pin the three numbers the prompt carries (net share, the week's
change, the 52-week percentile), the mapping, and the two ways the module is
allowed to say nothing: an unmapped ticker and an empty response.
"""

from __future__ import annotations

import httpx
import pytest

from orchestrator import positioning as pos


def rows(nets, open_interest=500_000, start_day=15):
    """Weekly rows, newest first, with a given sequence of net shares."""
    out = []
    for i, net in enumerate(nets):
        long_ = (open_interest * net + open_interest) / 2
        out.append({
            "report_date_as_yyyy_mm_dd": f"2026-09-{start_day - i:02d}T00:00:00.000",
            "open_interest_all": str(open_interest),
            "m_money_positions_long_all": str(long_),
            "m_money_positions_short_all": str(open_interest - long_),
        })
    return out


# --- the mapping --------------------------------------------------------------


def test_every_commodity_on_the_watchlist_has_a_contract():
    from config.instruments import COMMODITY_FUNDS

    for ticker in COMMODITY_FUNDS:
        assert pos.contract_for(ticker) is not None, ticker


def test_every_bond_fund_and_the_dollar_have_one():
    for ticker in ("TLT", "IEF", "SHY", "TIP", "UUP"):
        assert pos.contract_for(ticker) is not None, ticker


def test_the_broad_equity_funds_have_index_futures():
    for ticker in ("RSP", "IWM", "VWO", "VGK", "EWJ"):
        assert pos.contract_for(ticker) is not None, ticker


def test_a_basket_without_one_dominant_contract_is_absent_by_design():
    """DBC and DBA span a dozen contracts; there is no single position to report."""
    for ticker in ("DBC", "DBA"):
        assert pos.contract_for(ticker) is None


def test_a_single_name_and_a_single_country_have_none():
    for ticker in ("MSFT", "LLY", "EWZ", "INDA", "KSA", "XLE"):
        assert pos.contract_for(ticker) is None


def test_commodities_read_managed_money_and_financials_read_leveraged_funds():
    assert pos.contract_for("GLD")[0] == pos.DISAGGREGATED
    assert pos.contract_for("TLT")[0] == pos.FINANCIAL


# --- the numbers --------------------------------------------------------------


def test_net_share_is_signed_and_scaled_by_open_interest():
    assert pos.net_share(rows([0.4])[0]) == pytest.approx(0.4)
    assert pos.net_share(rows([-0.25])[0]) == pytest.approx(-0.25)


def test_a_row_without_open_interest_yields_nothing_rather_than_dividing_by_zero():
    row = rows([0.4])[0]
    row["open_interest_all"] = "0"
    assert pos.net_share(row) is None


def test_the_week_change_is_the_difference_from_last_week():
    snapshot = pos.build_snapshot("GLD", rows([0.40, 0.33] + [0.2] * 30))
    assert snapshot.week_change == pytest.approx(0.07)


def test_the_percentile_ranks_against_the_year():
    """0.95 has to mean "more bullish than 95% of the past year"."""
    history = [i / 100 for i in range(40)]      # 0.00 .. 0.39
    assert pos.percentile(0.39, history) == pytest.approx(1.0)
    assert pos.percentile(0.00, history) == pytest.approx(0.025)
    assert pos.percentile(0.20, history) == pytest.approx(0.525)


def test_too_little_history_reports_no_percentile_rather_than_a_confident_one():
    assert pos.percentile(0.4, [0.1, 0.2, 0.3]) is None
    snapshot = pos.build_snapshot("GLD", rows([0.4, 0.3]))
    assert snapshot.year_percentile is None
    assert "not enough history to rank" in "\n".join(snapshot.as_lines())


# --- what the prompt says -----------------------------------------------------


def test_a_crowded_long_is_named_as_crowding_not_as_a_signal():
    # Newest is the highest of 40 weeks.
    snapshot = pos.build_snapshot("GLD", rows([0.50] + [i / 200 for i in range(39)]))
    text = "\n".join(snapshot.as_lines())
    assert "net long 50.0% of open interest" in text
    assert "100% percentile" in text and "crowded long" in text
    assert "crowding, not as a forecast" in text


def test_a_crowded_short_reads_the_other_way():
    snapshot = pos.build_snapshot("GLD", rows([-0.30] + [i / 200 for i in range(39)]))
    text = "\n".join(snapshot.as_lines())
    assert "net short 30.0%" in text and "crowded short" in text


def test_an_ordinary_reading_says_so():
    snapshot = pos.build_snapshot("GLD", rows([0.10] + [i / 200 for i in range(39)]))
    assert "within its normal range" in "\n".join(snapshot.as_lines())


def test_the_prompt_states_the_staleness_the_dataset_has():
    """Tuesday's positions, published Friday. The model must not read it as live."""
    text = "\n".join(pos.build_snapshot("GLD", rows([0.2] * 30)).as_lines())
    assert "published the following Friday" in text
    assert "2026-09-15" in text


def test_the_contract_is_named_so_a_person_can_check_it():
    assert "GOLD" in "\n".join(pos.build_snapshot("GLD", rows([0.2] * 30)).as_lines())


# --- saying nothing, correctly -------------------------------------------------


def test_an_unmapped_ticker_produces_no_snapshot():
    assert pos.build_snapshot("MSFT", rows([0.3] * 30)) is None
    assert pos.build_snapshot("DBA", rows([0.3] * 30)) is None


def test_no_rows_produce_no_snapshot():
    assert pos.build_snapshot("GLD", []) is None


def test_rows_with_no_usable_position_produce_no_snapshot():
    assert pos.build_snapshot("GLD", [{"report_date_as_yyyy_mm_dd": "2026-09-15"}]) is None


def test_an_alternative_field_spelling_is_still_read():
    """The financial dataset names the same idea "leveraged funds"."""
    row = {
        "report_date": "2026-09-15",
        "open_interest": "1000",
        "lev_money_positions_long": "600",
        "lev_money_positions_short": "100",
    }
    assert pos.net_share(row) == pytest.approx(0.5)
    assert pos.build_snapshot("TLT", [row] * 30) is not None


# --- fetching -----------------------------------------------------------------


def test_fetch_asks_the_right_dataset_for_the_right_contract():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        return httpx.Response(200, json=rows([0.2] * 5))

    client = httpx.Client(transport=httpx.MockTransport(handler))
    out = pos.fetch_rows("USO", client=client)
    assert pos.DISAGGREGATED in seen["url"]
    assert "CRUDE+OIL" in seen["url"] or "CRUDE%20OIL" in seen["url"]
    assert len(out) == 5


def test_fetch_of_an_unmapped_ticker_asks_nothing():
    def explode(request):  # pragma: no cover - must never run
        raise AssertionError("no request should be made")

    assert pos.fetch_rows("MSFT", client=httpx.Client(transport=httpx.MockTransport(explode))) == []


def test_a_refusal_raises_so_the_caller_records_a_gap():
    client = httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(503, text="down")))
    with pytest.raises(httpx.HTTPStatusError):
        pos.fetch_rows("GLD", client=client)
