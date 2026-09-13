"""Insider activity parsing — especially the distinctions that decide its value.

Two mistakes would make this dimension worse than useless: counting a stock
grant as insider buying, and reading a routine sale as a bearish view. Most of
what is asserted here is that neither happens.
"""

from __future__ import annotations

from datetime import date

import pandas as pd
import pytest

from orchestrator import insiders

TODAY = date(2026, 9, 13)

PURCHASES = pd.DataFrame(
    {
        "Insider Purchases Last 6m": [
            "Purchases",
            "Sales",
            "Net Shares Purchased (Sold)",
            "Total Insider Shares Held",
            "% Net Shares Purchased (Sold)",
        ],
        "Shares": [120_000, 900_000, -780_000, 37_000_000, -0.021],
        "Trans": [4, 12, None, None, None],
    }
)

TRANSACTIONS = pd.DataFrame(
    {
        "Start Date": pd.to_datetime(
            ["2026-08-14", "2026-09-01", "2026-07-02", "2026-08-20", "2025-01-05"]
        ),
        "Insider": ["Jane Roe", "John Doe", "Jane Roe", "Ann Lee", "Old Timer"],
        "Position": ["CFO", "Director", "CFO", "CEO", "Director"],
        "Transaction": ["Purchase", "Sale", "Purchase", "Stock Award(Grant)", "Purchase"],
        "Text": ["Purchase at price 122.00", "Sale at price 130.00", "Purchase", "Grant", "Purchase"],
        "Shares": [50_000, 400_000, 20_000, 10_000, 999],
        "Value": [6_100_000, 52_000_000, 2_400_000, None, 100],
    }
)


def snapshot(**kw) -> insiders.InsiderSnapshot:
    kw.setdefault("purchases", PURCHASES)
    kw.setdefault("transactions", TRANSACTIONS)
    kw.setdefault("as_of", TODAY)
    return insiders.build_snapshot(**kw)


# --------------------------------------------------------------------------- #
# A grant is not a purchase
# --------------------------------------------------------------------------- #


def test_stock_grants_are_excluded_from_buying():
    """Counting compensation as insider buying would make the dimension noise."""
    snap = snapshot()
    buyers = {t.who for t in snap.buys}
    assert "Ann Lee" not in buyers  # received a grant, did not buy
    assert snap.non_market_count == 1


@pytest.mark.parametrize(
    "transaction",
    ["Stock Award(Grant)", "Exercise of derivative security", "Stock Gift",
     "Payment of exercise price or tax liability"],
)
def test_compensation_and_paperwork_are_never_trades(transaction):
    frame = pd.DataFrame({
        "Start Date": pd.to_datetime(["2026-09-01"]),
        "Insider": ["X"], "Position": ["CEO"],
        "Transaction": [transaction], "Text": [transaction],
        "Shares": [1_000], "Value": [100_000],
    })
    buys, sells, non_market = insiders.parse_transactions(frame, as_of=TODAY)
    assert buys == [] and sells == [] and non_market == 1


def test_purchases_and_sales_are_classified():
    snap = snapshot()
    assert {t.who for t in snap.buys} == {"Jane Roe"}
    assert {t.who for t in snap.sells} == {"John Doe"}


# --------------------------------------------------------------------------- #
# The buy/sell asymmetry must survive into the prompt
# --------------------------------------------------------------------------- #


def test_rendering_marks_sales_as_weak_evidence():
    lines = "\n".join(snapshot().as_lines())
    assert "own money" in lines                      # buys framed as signal
    assert "10b5-1" in lines and "weak evidence" in lines  # sales framed as noise


def test_rendering_says_grants_were_excluded():
    assert "compensation, not a view on the price" in "\n".join(snapshot().as_lines())


def test_distinct_insiders_are_counted_not_transactions():
    # Jane Roe bought twice; that is one insider with a view, not two.
    snap = snapshot()
    assert len(snap.buys) == 2
    assert snap.distinct_buyers == 1
    assert snap.distinct_sellers == 1


# --------------------------------------------------------------------------- #
# Windowing and ordering
# --------------------------------------------------------------------------- #


def test_transactions_outside_the_window_are_dropped():
    snap = snapshot()
    assert all(t.when >= "2026-03-17" for t in snap.buys)
    assert "Old Timer" not in {t.who for t in snap.buys}  # from 2025


def test_window_is_configurable():
    # 20 days back from 2026-09-13 is 2026-08-24: the Aug 14 and Jul 2 buys
    # fall outside, the Sep 1 sale stays.
    snap = snapshot(window_days=20)
    assert snap.buys == []
    assert {t.who for t in snap.sells} == {"John Doe"}
    assert snap.window_days == 20


def test_a_trade_exactly_on_the_window_edge_is_kept():
    # 2026-08-14 is exactly 30 days before 2026-09-13.
    snap = snapshot(window_days=30)
    assert "Jane Roe" in {t.who for t in snap.buys}


def test_trades_are_newest_first():
    whens = [t.when for t in snapshot().buys]
    assert whens == sorted(whens, reverse=True)


# --------------------------------------------------------------------------- #
# The six-month rollup
# --------------------------------------------------------------------------- #


def test_rollup_is_read_row_by_row():
    snap = snapshot()
    assert snap.shares_purchased == pytest.approx(120_000)
    assert snap.purchase_count == 4
    assert snap.shares_sold == pytest.approx(900_000)
    assert snap.sale_count == 12
    assert snap.net_shares == pytest.approx(-780_000)
    assert snap.total_shares_held == pytest.approx(37_000_000)
    assert snap.net_pct_of_held == pytest.approx(-0.021)


def test_rollup_label_column_is_found_by_position_not_name():
    """yfinance has renamed that column between releases."""
    renamed = PURCHASES.rename(columns={"Insider Purchases Last 6m": "Insider Purchases Last 12m"})
    assert insiders.parse_rollup(renamed)["shares_purchased"] == pytest.approx(120_000)


@pytest.mark.parametrize("frame", [None, pd.DataFrame()])
def test_a_missing_rollup_yields_nones_not_zeroes(frame):
    # Zero purchases and unknown purchases are different facts.
    values = insiders.parse_rollup(frame)
    assert all(v is None for v in values.values())


# --------------------------------------------------------------------------- #
# Nothing happening vs nothing available
# --------------------------------------------------------------------------- #


def test_no_transactions_is_stated_explicitly():
    snap = insiders.build_snapshot(purchases=pd.DataFrame(), transactions=pd.DataFrame())
    assert not snap.has_activity
    assert "No insider transactions reported" in "\n".join(snap.as_lines())


def test_activity_is_detected_from_the_rollup_alone():
    snap = insiders.build_snapshot(purchases=PURCHASES, transactions=pd.DataFrame())
    assert snap.has_activity
    assert "bought 120,000 shares" in "\n".join(snap.as_lines())


def test_snapshot_is_json_serialisable_for_the_journal():
    import json

    assert json.loads(json.dumps(snapshot().as_dict()))["distinct_buyers"] == 1


def test_missing_values_render_as_na_not_zero():
    frame = pd.DataFrame({
        "Start Date": pd.to_datetime(["2026-09-01"]),
        "Insider": [None], "Position": [None],
        "Transaction": ["Purchase"], "Text": ["Purchase"],
        "Shares": [None], "Value": [None],
    })
    snap = insiders.build_snapshot(purchases=None, transactions=frame, as_of=TODAY)
    lines = "\n".join(snap.as_lines())
    assert "unnamed insider" in lines
    assert "n/a" in lines
