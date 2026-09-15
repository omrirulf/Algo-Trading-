"""Every formatter renders a missing value as n/a -- including pandas' own."""

from __future__ import annotations

import math

import pandas as pd
import pytest

from orchestrator import formatting as fmt


@pytest.mark.parametrize("value", [None, float("nan"), float("inf"), pd.NA, pd.NaT])
def test_every_missing_shape_is_missing(value):
    assert fmt.is_missing(value)


@pytest.mark.parametrize("value", [0, 0.0, -0.021, True, False, "text"])
def test_present_values_are_not_missing(value):
    assert not fmt.is_missing(value)


def test_pandas_na_renders_as_na_rather_than_raising():
    """The first live-data run died here: float(pd.NA) raises TypeError."""
    assert fmt.pct(pd.NA) == fmt.NA
    assert fmt.num(pd.NA) == fmt.NA
    assert fmt.points(pd.NA) == fmt.NA
    assert fmt.money(pd.NA) == fmt.NA


def test_clean_turns_pandas_na_into_none():
    assert fmt.clean(pd.NA) is None
    assert fmt.clean(pd.NaT) is None
    assert fmt.clean(float("nan")) is None
    assert fmt.clean(-0.021) == pytest.approx(-0.021)
    assert math.isfinite(fmt.clean(3))
