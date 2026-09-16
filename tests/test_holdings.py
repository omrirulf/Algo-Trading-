"""The analyst view of a fund, assembled from the analyst view of its holdings.

Nobody publishes a price target on XLE. But XLE *is* twenty-three companies,
every one of them covered, and this project already knows how to fetch that
coverage -- so the fund's empty analyst slot can be filled from data it
already has. The number that keeps it honest is coverage: five names at 62%
of the fund says something about the fund; five names at 4% of a broad index
says something about four percent, and the prompt has to say which.
"""

from __future__ import annotations

import pytest

from orchestrator import holdings
from orchestrator.analysts import AnalystSnapshot


def snap(mean=None, upside=None, actions=()):
    return AnalystSnapshot(
        recommendation_mean=mean, target_upside=upside, recent_actions=list(actions)
    )


XLE = [
    ("XOM", 0.229, snap(2.1, 0.14, ["Goldman: Hold -> Buy"])),
    ("CVX", 0.171, snap(2.3, 0.11)),
    ("COP", 0.043, snap(1.9, 0.19)),
    ("EOG", 0.041, snap(3.8, -0.02, ["Citi: Buy -> Sell"])),
]


# --- the roll-up ---------------------------------------------------------------


def test_the_weighted_target_is_weighted_by_the_funds_own_weights():
    """XOM at 22.9% must move the number more than EOG at 4.1%."""
    rolled = holdings.build_snapshot("XLE", XLE)
    weights = sum(w for _, w, _ in XLE)
    expected = sum(s.target_upside * w for _, w, s in XLE) / weights
    assert rolled.target_upside == pytest.approx(expected)


def test_ratings_are_bucketed_by_weight_not_by_headcount():
    rolled = holdings.build_snapshot("XLE", XLE)
    # Three buys carrying 44.3% of weight, one sell carrying 4.1%.
    assert rolled.buy_weight == pytest.approx(0.443 / 0.484, rel=1e-3)
    assert rolled.sell_weight == pytest.approx(0.041 / 0.484, rel=1e-3)
    assert rolled.hold_weight == pytest.approx(0.0)


def test_the_bucket_boundaries_follow_the_1_to_5_scale():
    rolled = holdings.build_snapshot("F", [
        ("A", 0.25, snap(1.0)), ("B", 0.25, snap(2.5)),
        ("C", 0.25, snap(3.0)), ("D", 0.25, snap(4.0)),
    ])
    assert rolled.buy_weight == pytest.approx(0.5)   # 1.0 and 2.5
    assert rolled.hold_weight == pytest.approx(0.25)  # 3.0
    assert rolled.sell_weight == pytest.approx(0.25)  # 4.0


def test_coverage_is_reported_so_a_thin_roll_up_can_be_discounted():
    text = "\n".join(holdings.build_snapshot("XLE", XLE).as_lines())
    assert "4 largest holdings, 48.4% of the fund by weight" in text
    assert "thin" not in text


def test_a_thin_roll_up_says_so_in_the_prompt():
    """Five names at 4% of a 500-stock index is a fact about four percent."""
    thin = [("AAPL", 0.02, snap(2.0, 0.1)), ("MSFT", 0.02, snap(2.0, 0.1))]
    text = "\n".join(holdings.build_snapshot("RSP", thin).as_lines())
    assert "4.0% of the fund by weight" in text
    assert "thin, so read this as a fact about that slice" in text


def test_rating_changes_among_the_holdings_are_carried_with_their_ticker():
    text = "\n".join(holdings.build_snapshot("XLE", XLE).as_lines())
    assert "XOM: Goldman: Hold -> Buy" in text
    assert "EOG: Citi: Buy -> Sell" in text


def test_no_rating_changes_is_stated_rather_than_omitted():
    quiet = [("XOM", 0.2, snap(2.0, 0.1))]
    assert "none reported" in "\n".join(holdings.build_snapshot("XLE", quiet).as_lines())


# --- degrading ------------------------------------------------------------------


def test_a_holding_with_no_coverage_is_skipped_not_counted():
    with_gap = XLE + [("PRIVATE", 0.05, None)]
    rolled = holdings.build_snapshot("XLE", with_gap)
    assert rolled.covered == 4
    assert "PRIVATE" not in rolled.names


def test_nothing_analysable_produces_no_section():
    assert holdings.build_snapshot("XLE", []) is None
    assert holdings.build_snapshot("XLE", [("A", 0.1, None)]) is None


def test_a_holding_with_no_rating_still_counts_toward_coverage():
    """It is in the fund whether or not an analyst has an opinion on it."""
    rolled = holdings.build_snapshot("XLE", [("XOM", 0.2, snap(None, 0.1))])
    assert rolled.covered == 1
    assert rolled.buy_weight is None and rolled.target_upside == pytest.approx(0.1)


def test_zero_weights_do_not_divide_by_zero():
    rolled = holdings.build_snapshot("XLE", [("XOM", 0.0, snap(2.0, 0.1))])
    assert rolled is not None and rolled.mean_rating is None


# --- reading yfinance's holdings payload -----------------------------------------


def test_symbols_come_out_of_a_dict_payload():
    assert holdings.holdings_from_payload({"XOM": 0.229, "CVX": 0.171}) == [
        ("XOM", 0.229), ("CVX", 0.171)
    ]


def test_symbols_come_out_of_a_dataframe_payload():
    pd = pytest.importorskip("pandas")
    frame = pd.DataFrame({"Name": ["Exxon", "Chevron"], "Holding Percent": [0.229, 0.171]},
                         index=["XOM", "CVX"])
    assert holdings.holdings_from_payload(frame) == [("XOM", 0.229), ("CVX", 0.171)]


def test_only_the_top_holdings_are_taken():
    payload = {f"T{i}": 0.01 for i in range(50)}
    assert len(holdings.holdings_from_payload(payload)) == holdings.MAX_HOLDINGS


def test_a_row_that_is_not_a_ticker_is_skipped_rather_than_looked_up():
    assert holdings.holdings_from_payload({"Cash & Other": 0.02, "XOM": 0.2}) == [("XOM", 0.2)]


def test_a_broken_payload_yields_no_holdings_rather_than_raising():
    class Hostile:
        def iterrows(self):
            raise RuntimeError("boom")
        columns = ["Holding Percent"]

    assert holdings.holdings_from_payload(Hostile()) == []


def test_the_snapshot_round_trips_through_the_journal():
    rolled = holdings.build_snapshot("XLE", XLE)
    assert holdings.HoldingsSnapshot(**rolled.as_dict()).as_lines() == rolled.as_lines()
