"""The currency gap between where the money is and where the life is.

None of the rest of this system measures it. The journal, the scorer and the
backtest all count dollars, so an FX move does not reduce a return -- it
silently redenominates one. These tests pin the arithmetic and the failure
behaviour.
"""

from __future__ import annotations

import sys
import types

import pandas as pd
import pytest

from orchestrator import fx

#: The autouse offline fixture replaces fx.fetch_rate for every test, which is
#: right for the rest of the suite and wrong here. Captured at import time,
#: before that fixture runs, so these tests exercise the real implementation
#: against a fake yfinance.
REAL_FETCH = fx.fetch_rate


def _fake_yfinance(frame, raises=None):
    module = types.ModuleType("yfinance")

    class _Ticker:
        def __init__(self, symbol):
            self.symbol = symbol

        def history(self, **kwargs):
            if raises is not None:
                raise raises
            return frame

    module.Ticker = _Ticker
    return module


def _series(values):
    return pd.DataFrame(
        {"Close": values}, index=pd.bdate_range("2026-06-01", periods=len(values))
    )


@pytest.fixture
def install(monkeypatch):
    def _install(module):
        monkeypatch.setitem(sys.modules, "yfinance", module)
    return _install


# --- the arithmetic that makes the risk real ------------------------------- #


def test_a_dollar_gain_can_be_a_shekel_loss():
    """The whole reason this module exists.

    Ten percent in dollars, with the dollar down ten percent, is not break
    even -- it is slightly negative, because the two compound.
    """
    assert fx.shekel_return_pct(10, -10) == pytest.approx(-1.0)


def test_returns_compound_rather_than_add():
    """Adding them would say 15%; compounding says 15.5%."""
    assert fx.shekel_return_pct(10, 5) == pytest.approx(15.5)
    assert fx.shekel_return_pct(10, 5) != pytest.approx(15.0)


def test_a_flat_currency_leaves_the_return_alone():
    assert fx.shekel_return_pct(7.3, 0) == pytest.approx(7.3)


def test_a_flat_portfolio_still_moves_in_shekels():
    """Holding dollars is a position, even when nothing is traded."""
    assert fx.shekel_return_pct(0, -8) == pytest.approx(-8.0)


def test_conversion_is_shekels_per_dollar():
    """ILS=X quotes USD/ILS, so the rate multiplies rather than divides."""
    assert fx.in_shekels(1_000, 3.7) == pytest.approx(3_700)


# --- fetching -------------------------------------------------------------- #


def test_a_good_fetch_reports_level_and_change(install):
    install(_fake_yfinance(_series([3.60, 3.65, 3.78])))
    rate = REAL_FETCH()
    assert rate.ok
    assert rate.rate == pytest.approx(3.78)
    assert rate.change_3mo_pct == pytest.approx(5.0)


def test_a_falling_dollar_reports_a_negative_change(install):
    install(_fake_yfinance(_series([4.00, 3.90, 3.60])))
    assert REAL_FETCH().change_3mo_pct == pytest.approx(-10.0)


def test_a_failed_fetch_is_a_gap_not_an_exception(install):
    """A missing rate must never take down a cycle that produced good signals."""
    install(_fake_yfinance(None, raises=RuntimeError("boom")))
    rate = REAL_FETCH()
    assert not rate.ok
    assert "RuntimeError" in rate.gap
    assert rate.rate is None


def test_an_empty_frame_is_a_gap(install):
    install(_fake_yfinance(pd.DataFrame()))
    rate = REAL_FETCH()
    assert not rate.ok
    assert "no bars" in rate.gap


def test_a_gap_renders_as_a_named_absence(install):
    install(_fake_yfinance(pd.DataFrame()))
    assert "unavailable" in REAL_FETCH().as_lines()[0]


def test_a_single_bar_reports_a_level_with_no_change(install):
    """Enough to convert with, not enough to say anything about risk."""
    install(_fake_yfinance(_series([3.7])))
    rate = REAL_FETCH()
    assert rate.ok
    assert rate.change_3mo_pct is None


# --- the journal carries it ------------------------------------------------ #


def _last_entry(path):
    import json

    return json.loads(path.read_text().strip().splitlines()[-1])


def test_the_rate_is_journalled_with_every_signal(_journal_to_tmp):
    """Without the rate as of the entry, no later analysis can redenominate."""
    from orchestrator import journal
    from orchestrator.context import TickerContext

    journal.record(
        TickerContext(ticker="MSFT"),
        fx=fx.FxRate(rate=3.7412, change_3mo_pct=-2.3),
    )
    entry = _last_entry(_journal_to_tmp)
    assert entry["fx"]["rate"] == pytest.approx(3.7412)
    assert entry["fx"]["change_3mo_pct"] == pytest.approx(-2.3)


def test_a_missing_rate_journals_as_null_not_zero(_journal_to_tmp):
    """A zero rate would read as 'the shekel is worthless', not 'unknown'."""
    from orchestrator import journal
    from orchestrator.context import TickerContext

    journal.record(TickerContext(ticker="MSFT"), fx=fx.FxRate(gap="fetch failed"))
    entry = _last_entry(_journal_to_tmp)
    assert entry["fx"]["rate"] is None
    assert entry["fx"]["gap"] == "fetch failed"


def test_a_cycle_with_no_fx_at_all_still_journals(_journal_to_tmp):
    """FX is an addition, not a new requirement: omitting it must not break."""
    from orchestrator import journal
    from orchestrator.context import TickerContext

    journal.record(TickerContext(ticker="MSFT"))
    assert _last_entry(_journal_to_tmp)["fx"] is None
