"""The sleeve comparison, including the bug that CSV loading shipped with once.

``load_bars`` originally read CSVs without parsing the index, which produced an
integer index that only failed deep inside ``simulate_trade`` with an opaque
``'int' object has no attribute 'date'``. The date-index tests below are the
regression for that.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from backtest import compare_sleeves as cs
from config import settings as cfg


def _bars(path, rows: int = 260, vol: float = 0.02, seed: int = 3, index: bool = True):
    rng = np.random.default_rng(seed)
    close = 100.0 * np.exp(np.cumsum(rng.normal(0.0003, vol, rows)))
    intra = np.abs(rng.normal(0, vol * 0.6, rows))
    op = np.concatenate([[100.0], close[:-1]])
    frame = pd.DataFrame(
        {
            "Open": op,
            "High": np.maximum.reduce([close * (1 + intra), op, close]),
            "Low": np.minimum.reduce([close * (1 - intra), op, close]),
            "Close": close,
        },
        index=pd.bdate_range("2024-01-01", periods=rows) if index else range(rows),
    )
    frame.to_csv(path, index=index)
    return frame


def test_bars_load_with_a_real_date_index(tmp_path):
    """The original bug: a bare read_csv gives integers the simulator cannot use."""
    _bars(tmp_path / "MSFT.csv")
    loaded = cs.load_bars("MSFT", tmp_path, period="2y")
    assert loaded is not None
    assert isinstance(loaded.index, pd.DatetimeIndex)


@pytest.mark.filterwarnings("ignore:Could not infer format:UserWarning")
def test_a_csv_without_dates_is_rejected_rather_than_crashing_later(tmp_path):
    """Better a named 'no bars' than an AttributeError forty frames down."""
    _bars(tmp_path / "MSFT.csv", index=False)
    assert cs.load_bars("MSFT", tmp_path, period="2y") is None


def test_a_missing_ticker_is_reported_not_raised(tmp_path):
    """One delisted symbol must not void the whole comparison."""
    _bars(tmp_path / "MSFT.csv")
    result = cs.run_sleeve("t", ["MSFT", "NOPE"], cfg.MAX_POSITION_PCT, csv_dir=tmp_path)
    assert result.tickers == ["MSFT"]
    assert result.missing == ["NOPE"]
    assert result.trades


def test_each_sleeve_is_replayed_under_its_own_cap(tmp_path):
    """Comparing both at the same cap would answer a question nobody asked."""
    _bars(tmp_path / "MSFT.csv")
    _bars(tmp_path / "IWM.csv")
    single = cs.run_sleeve("single name", ["MSFT"], cfg.MAX_POSITION_PCT, csv_dir=tmp_path)
    index = cs.run_sleeve("index", ["IWM"], cfg.MAX_ETF_POSITION_PCT, csv_dir=tmp_path)
    assert single.max_position_pct == cfg.MAX_POSITION_PCT
    assert index.max_position_pct == cfg.MAX_ETF_POSITION_PCT


def test_a_larger_cap_on_the_same_bars_risks_more_per_trade(tmp_path):
    """The relationship the ETF cap is tuned against: risk scales with the cap.

    Identical price history, two caps. If this ever stopped holding, the
    'risk/trade' column in the report would be meaningless and the cap could
    be raised without apparent cost.
    """
    _bars(tmp_path / "X.csv")
    small = cs.run_sleeve("small", ["X"], 0.05, csv_dir=tmp_path)
    large = cs.run_sleeve("large", ["X"], 0.20, csv_dir=tmp_path)
    assert large.mean_risk_pct > small.mean_risk_pct


def test_a_thin_sleeve_is_flagged_rather_than_quietly_reported(tmp_path):
    """A precise-looking number from four trades is worse than no number."""
    _bars(tmp_path / "MSFT.csv", rows=40)
    result = cs.run_sleeve("t", ["MSFT"], cfg.MAX_POSITION_PCT, csv_dir=tmp_path, every=20)
    assert not result.enough
    assert "NOT ENOUGH DATA" in cs.render([result])


def test_an_empty_sleeve_reports_dashes_not_zeros(tmp_path):
    """A zero would read as 'measured nothing bad', which is not what happened."""
    result = cs.run_sleeve("t", ["NOPE"], cfg.MAX_POSITION_PCT, csv_dir=tmp_path)
    assert result.n == 0
    assert result.stop_hit_rate is None
    assert result.mean_risk_pct is None
    assert "--" in cs.render([result])


def test_the_report_says_it_is_not_evidence_of_edge(tmp_path):
    """Metronome entries measure the risk engine, never the model."""
    _bars(tmp_path / "MSFT.csv")
    text = cs.render([cs.run_sleeve("t", ["MSFT"], cfg.MAX_POSITION_PCT, csv_dir=tmp_path)])
    assert "not the model" in text
    assert "no LLM was asked anything" in text


def test_json_output_is_serialisable(tmp_path):
    import json

    _bars(tmp_path / "MSFT.csv")
    result = cs.run_sleeve("t", ["MSFT"], cfg.MAX_POSITION_PCT, csv_dir=tmp_path)
    assert json.loads(json.dumps(result.as_dict()))["trades"] == result.n


def test_the_cli_runs_offline_and_exits_zero(tmp_path, capsys):
    for ticker in cs.SINGLE_NAMES[:2] + cs.INDEX_SLEEVE[:2]:
        _bars(tmp_path / f"{ticker}.csv")
    assert cs.main(["--csv-dir", str(tmp_path)]) == 0
    assert "SLEEVE COMPARISON" in capsys.readouterr().out


def test_the_cli_fails_when_no_bars_exist_anywhere(tmp_path):
    """Exit 1 so a scheduled run cannot report success on zero data."""
    assert cs.main(["--csv-dir", str(tmp_path)]) == 1
