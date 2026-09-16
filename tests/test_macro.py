"""The weather every fund trades in.

The fund prompt tells the model to answer NEUTRAL unless "a policy or rate
surprise" has happened -- and then hands it a day of headlines and no rates
at all. These pin the block that fixes that, and in particular the curve,
which is the one number a level cannot give you.
"""

from __future__ import annotations

import pytest

from orchestrator import macro

pd = pytest.importorskip("pandas")


def frame(values):
    return pd.DataFrame({"Close": values})


def histories(irx=4.31, fvx=3.72, tnx=4.02, tyx=4.65, dollar=98.4, vix=14.2, prior=None):
    """Six symbols, five sessions of history plus today."""
    prior = prior or {}
    out = {}
    for symbol, latest in (
        ("^IRX", irx), ("^FVX", fvx), ("^TNX", tnx), ("^TYX", tyx),
        ("DX-Y.NYB", dollar), ("^VIX", vix),
    ):
        base = prior.get(symbol, latest)
        out[symbol] = frame([base] * (macro.WEEK + 1) + [latest])
    return out


# --- what it says -------------------------------------------------------------


def test_the_whole_curve_is_read_out_with_the_week_beside_it():
    text = "\n".join(macro.build_snapshot(histories()).as_lines())
    assert "3-month 4.31%" in text
    assert "10-year 4.02%" in text
    assert "30-year 4.65%" in text


def test_a_move_is_quoted_in_points_not_as_a_percentage_of_the_yield():
    """A two-basis-point shift is `+0.02`. Rendered as a percentage change it
    would read as `+0.5%`, which is a different and wrong statement."""
    text = "\n".join(macro.build_snapshot(
        histories(tnx=4.02, prior={"^TNX": 4.10})).as_lines())
    assert "10-year 4.02% (-0.08 on the week)" in text
    assert "-0.1%" not in text


def test_the_dollar_and_volatility_are_both_there():
    text = "\n".join(macro.build_snapshot(histories()).as_lines())
    assert "US dollar index: 98.40" in text
    assert "Volatility (VIX): 14.20" in text


# --- the curve, which is the point --------------------------------------------


def test_an_upward_sloping_curve_is_called_normal():
    snapshot = macro.build_snapshot(histories(irx=3.10, tnx=4.02))
    assert snapshot.slope == pytest.approx(0.92)
    assert "upward sloping (normal)" in "\n".join(snapshot.as_lines())


def test_an_inverted_curve_is_named_and_explained():
    """An inversion is a regime, not a reading, and the model should not have
    to know that a negative slope is the thing everyone watches."""
    snapshot = macro.build_snapshot(histories(irx=5.42, tnx=4.02))
    assert snapshot.slope == pytest.approx(-1.40)
    text = "\n".join(snapshot.as_lines())
    assert "inverted" in text
    assert "short rates above long" in text and "slowdown ahead" in text


def test_a_flat_curve_is_neither():
    snapshot = macro.build_snapshot(histories(irx=4.00, tnx=4.10))
    text = "\n".join(snapshot.as_lines())
    assert "flat" in text
    assert "inverted" not in text and "normal" not in text


def test_the_slope_needs_both_ends_and_says_nothing_without_them():
    partial = histories()
    partial.pop("^IRX")
    assert macro.build_snapshot(partial).slope is None


# --- volatility bands ---------------------------------------------------------


@pytest.mark.parametrize("level,band", [(11.5, "calm"), (18.0, "elevated"), (34.0, "stressed")])
def test_volatility_is_banded_because_the_same_signal_means_different_things(level, band):
    """A bullish read at a VIX of 12 and at 34 are not the same trade."""
    assert band in "\n".join(macro.build_snapshot(histories(vix=level)).as_lines())


# --- degrading rather than raising --------------------------------------------


def test_nothing_at_all_is_no_section_rather_than_four_lines_of_blanks():
    assert macro.build_snapshot({}) is None
    assert macro.build_snapshot(None) is None


def test_one_missing_symbol_does_not_cost_the_others():
    partial = histories()
    partial.pop("DX-Y.NYB")
    snapshot = macro.build_snapshot(partial)
    assert snapshot is not None
    assert snapshot.dollar is None
    assert snapshot.yields["10-year"] == 4.02
    assert "US dollar index: n/a" in "\n".join(snapshot.as_lines())


def test_a_history_too_short_for_a_week_keeps_the_level_and_drops_the_change():
    snapshot = macro.build_snapshot({"^TNX": frame([4.02, 4.03])})
    assert snapshot.yields["10-year"] == 4.03
    assert "10-year" not in snapshot.yield_changes
    assert "on the week" not in snapshot.as_lines()[0]


@pytest.mark.parametrize("hostile", [{"^TNX": 17}, {"^TNX": object()},
                                     {"^TNX": pd.DataFrame({"Open": [1.0]})},
                                     {"^TNX": frame([float("nan")] * 8)}])
def test_a_payload_of_the_wrong_shape_degrades_rather_than_raising(hostile):
    assert macro.build_snapshot(hostile) is None


def test_the_block_reaches_the_journal():
    record = macro.build_snapshot(histories()).as_dict()
    assert record["yields"]["10-year"] == 4.02
    assert record["volatility"] == 14.2
