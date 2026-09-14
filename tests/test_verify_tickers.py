"""The ticker check, which exists because the watchlist was written blind.

No test here touches the network: ``check`` imports yfinance lazily inside a
try block, so monkeypatching the module is enough to drive every path.
"""

from __future__ import annotations

import sys
import types

import pandas as pd
import pytest

from backtest import verify_tickers as vt


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


def _bars(rows=60, price=100.0, vol=0.01, volume=1_000_000):
    closes = [price * (1 + vol) ** i for i in range(rows)]
    return pd.DataFrame(
        {"Close": closes, "Volume": [volume] * rows},
        index=pd.bdate_range("2025-01-01", periods=rows),
    )


@pytest.fixture
def install(monkeypatch):
    def _install(module):
        monkeypatch.setitem(sys.modules, "yfinance", module)
    return _install


def test_a_resolving_ticker_reports_its_numbers(install):
    install(_fake_yfinance(_bars()))
    result = vt.check("MSFT")
    assert result.resolved
    assert result.bars == 60
    assert result.daily_vol_pct is not None
    assert result.median_dollar_volume is not None


def test_an_empty_frame_means_delisted_not_crashed(install):
    """The failure mode this tool exists to catch: a silent per-ticker outage."""
    install(_fake_yfinance(pd.DataFrame()))
    result = vt.check("JO")
    assert not result.resolved
    assert "delisted" in result.note


def test_a_fetch_failure_is_reported_not_raised(install):
    """One bad symbol must not void the whole report."""
    install(_fake_yfinance(None, raises=RuntimeError("boom")))
    result = vt.check("NOPE")
    assert not result.resolved
    assert "RuntimeError" in result.note


def test_the_kind_comes_from_configuration(install):
    install(_fake_yfinance(_bars()))
    assert vt.check("MSFT").kind == "equity"
    assert vt.check("RSP").kind == "broad fund"
    assert vt.check("GLD").kind == "commodity fund"


def test_the_position_size_comes_from_the_instrument_cap(install):
    """Each kind is checked against the size it would actually be traded at."""
    install(_fake_yfinance(_bars()))
    assert vt.check("GLD").position_usd < vt.check("MSFT").position_usd
    assert vt.check("MSFT").position_usd < vt.check("RSP").position_usd


def test_a_position_too_large_for_the_volume_is_flagged(install):
    """What matters is the position relative to the day, not the day alone."""
    install(_fake_yfinance(_bars(volume=100)))
    result = vt.check("EIS")
    assert result.thin
    assert "TOO BIG FOR THE BOOK" in vt.render([result])


def test_a_thin_fund_is_fine_when_the_position_is_small(install):
    """The check this replaced cried wolf.

    An absolute dollar-volume floor flagged SOYB at $1.6M/day. But a full
    position there is $4,000 -- a quarter of one percent of the day. Thinness
    is only thin relative to what you are trying to put in it.
    """
    install(_fake_yfinance(_bars(price=27.5, volume=60_000)))  # ~$1.6M/day
    result = vt.check("SOYB")
    assert result.participation < 0.01
    assert not result.thin
    assert "under 1% of a day's volume" in vt.render([result])


def test_participation_scales_with_the_account(install):
    """A size that is harmless at 100k is not harmless at 10m."""
    install(_fake_yfinance(_bars(price=27.5, volume=60_000)))
    small = vt.check("SOYB", equity=100_000)
    large = vt.check("SOYB", equity=10_000_000)
    assert not small.thin
    assert large.thin
    assert large.participation == pytest.approx(small.participation * 100)


def test_liquid_volume_is_not_flagged(install):
    install(_fake_yfinance(_bars(volume=10_000_000)))
    assert not vt.check("RSP").thin


def test_a_broken_ticker_is_called_out_in_the_report(install):
    install(_fake_yfinance(pd.DataFrame()))
    text = vt.render([vt.check("JO")])
    assert "DOES NOT RESOLVE" in text
    assert "silently" in text


def test_the_cli_exits_non_zero_when_a_ticker_is_broken(install, capsys):
    """A scheduled run must not report success while a holding is broken."""
    install(_fake_yfinance(pd.DataFrame()))
    assert vt.main([]) == 1


def test_the_cli_exits_zero_when_everything_resolves(install, capsys):
    install(_fake_yfinance(_bars()))
    assert vt.main([]) == 0
    assert "TICKER VERIFICATION" in capsys.readouterr().out


def test_json_output_is_serialisable(install):
    import json

    install(_fake_yfinance(_bars()))
    assert json.loads(json.dumps(vt.check("MSFT").as_dict()))["resolved"] is True
