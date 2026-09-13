"""Parsing the sell-side and ownership frames yfinance returns."""

from __future__ import annotations

import pandas as pd
import pytest

from orchestrator import analysts

INFO = {
    "recommendationKey": "buy",
    "recommendationMean": 2.05,
    "numberOfAnalystOpinions": 41,
    "targetMeanPrice": 265.0,
    "targetHighPrice": 320.0,
    "targetLowPrice": 200.0,
    "heldPercentInstitutions": 0.621,
}

RECOMMENDATIONS = pd.DataFrame(
    {
        "period": ["0m", "-1m"],
        "strongBuy": [22, 20],
        "buy": [12, 13],
        "hold": [6, 7],
        "sell": [1, 1],
        "strongSell": [0, 0],
    }
)

UPGRADES = pd.DataFrame(
    {
        "Firm": ["Morgan Stanley", "Goldman Sachs"],
        "ToGrade": ["Overweight", "Neutral"],
        "FromGrade": ["Equal-Weight", "Buy"],
        "Action": ["up", "down"],
    },
    index=pd.to_datetime(["2026-09-05", "2026-09-09"]),
)

HOLDERS = pd.DataFrame(
    {
        "Holder": ["Vanguard Group Inc", "Blackrock Inc."],
        "pctHeld": [0.0889, 0.0662],
        "Shares": [1_300_000_000, 1_000_000_000],
    }
)


def test_full_inputs_produce_a_complete_snapshot():
    snapshot = analysts.build_snapshot(
        info=INFO,
        recommendations=RECOMMENDATIONS,
        upgrades_downgrades=UPGRADES,
        institutional_holders=HOLDERS,
        last_close=234.5,
    )

    assert snapshot.recommendation == "buy"
    assert snapshot.analyst_count == 41
    assert snapshot.target_upside == pytest.approx(265.0 / 234.5 - 1)
    assert snapshot.rating_counts == {
        "strongBuy": 22, "buy": 12, "hold": 6, "sell": 1, "strongSell": 0
    }
    assert snapshot.institutional_ownership == pytest.approx(0.621)


def test_rating_counts_use_the_most_recent_period_only():
    assert analysts.parse_rating_counts(RECOMMENDATIONS)["strongBuy"] == 22


def test_rating_actions_are_newest_first_and_name_the_move():
    actions = analysts.parse_rating_actions(UPGRADES)
    assert actions[0] == "2026-09-09 Goldman Sachs: down, Buy -> Neutral"
    assert actions[1] == "2026-09-05 Morgan Stanley: up, Equal-Weight -> Overweight"


def test_rating_actions_are_capped():
    many = pd.concat([UPGRADES] * 10, ignore_index=False)
    assert len(analysts.parse_rating_actions(many, limit=3)) == 3


def test_top_holders_render_with_their_stake():
    assert analysts.parse_top_holders(HOLDERS) == [
        "Vanguard Group Inc (8.9%)",
        "Blackrock Inc. (6.6%)",
    ]


def test_holders_accept_the_older_percent_out_column():
    frame = pd.DataFrame({"Holder": ["State Street"], "% Out": [0.04]})
    assert analysts.parse_top_holders(frame) == ["State Street (4.0%)"]


def test_upside_needs_a_price_to_compare_against():
    snapshot = analysts.build_snapshot(info=INFO, last_close=None)
    assert snapshot.target_mean == 265.0
    assert snapshot.target_upside is None


@pytest.mark.parametrize("frame", [None, pd.DataFrame()])
def test_missing_frames_degrade_to_empty_rather_than_raising(frame):
    snapshot = analysts.build_snapshot(
        info={}, recommendations=frame, upgrades_downgrades=frame, institutional_holders=frame
    )
    assert snapshot.rating_counts == {}
    assert snapshot.recent_actions == []
    assert snapshot.top_holders == []
    assert "none reported" in "\n".join(snapshot.as_lines())


def test_rendered_lines_explain_the_consensus_scale():
    lines = "\n".join(
        analysts.build_snapshot(
            info=INFO, recommendations=RECOMMENDATIONS, last_close=234.5
        ).as_lines()
    )
    # A bare "2.05" is meaningless without saying which end is bullish.
    assert "1=strong buy" in lines
    assert "22 strong buy, 12 buy, 6 hold, 1 sell, 0 strong sell" in lines
    assert "+13.0%" in lines
