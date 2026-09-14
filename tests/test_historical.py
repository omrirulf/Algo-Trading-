"""The historical replay: two honest dimensions, no look-ahead, scored by the engine.

No network. Frames are synthetic, news is stubbed, and the batch never leaves
the process.
"""

from __future__ import annotations

import json
import random
from datetime import date

import numpy as np
import pandas as pd
import pytest

from app.schemas import Bias, LLMSignal
from config import settings as cfg
from orchestrator import llm, news
from replay import historical as h


def _frame(rows=600, seed=1, price=100.0, vol=0.01):
    rng = np.random.default_rng(seed)
    close = price * np.exp(np.cumsum(rng.normal(0.0003, vol, rows)))
    intra = np.abs(rng.normal(0, vol * 0.6, rows))
    op = np.concatenate([[price], close[:-1]]) * (1 + rng.normal(0, vol * 0.3, rows))
    return pd.DataFrame({
        "Open": op,
        "High": np.maximum.reduce([close * (1 + intra), op, close]),
        "Low": np.minimum.reduce([close * (1 - intra), op, close]),
        "Close": close,
        "Volume": np.full(rows, 1_000_000),
    }, index=pd.bdate_range("2023-01-02", periods=rows))


# --- news date window ------------------------------------------------------ #

def test_the_dated_query_uses_a_custom_range_ending_on_the_day():
    url = news.build_news_search_url("MSFT", on=date(2025, 3, 3))
    assert "cdr%3A1" in url and "cd_min%3A3%2F2%2F2025" in url and "cd_max%3A3%2F3%2F2025" in url
    assert "qdr" not in url


def test_the_live_query_is_unchanged_without_a_date():
    assert "qdr%3Ad" in news.build_news_search_url("MSFT")


def test_fetch_on_sends_the_dated_url_through_the_same_parser():
    seen = {}

    class _Resp:
        status_code = 200
        text = json.dumps({"news": [{"title": "old story", "source": "x", "link": "l"}]})

    class _Client:
        def post(self, url, json=None, headers=None):
            seen["url"] = json["url"]
            return _Resp()

    provider = news.BrightDataNewsProvider("tok", "zone", client=_Client())
    out = provider.fetch_on("MSFT", date(2025, 3, 3))
    assert "cd_max%3A3%2F3%2F2025" in seen["url"]
    assert out and "old story" in out[0]


# --- look-ahead safety ------------------------------------------------------ #

def test_technicals_use_only_bars_up_to_the_signal_bar():
    """Mutating every later bar must not move the snapshot by a cent."""
    f = _frame()
    i = 400
    before = h.technicals_as_of(f, i)
    g = f.copy()
    g.iloc[i + 1:, g.columns.get_loc("Close")] *= 3.0
    g.iloc[i + 1:, g.columns.get_loc("High")] *= 3.0
    after = h.technicals_as_of(g, i)
    assert before is not None and after is not None
    assert before.as_dict() == after.as_dict()


def test_technicals_change_when_an_earlier_bar_changes():
    """The complement: the snapshot really is a function of the past."""
    f = _frame()
    i = 400
    before = h.technicals_as_of(f, i)
    g = f.copy()
    g.iloc[i, g.columns.get_loc("Close")] *= 1.5
    after = h.technicals_as_of(g, i)
    assert before.as_dict() != after.as_dict()


def test_raw_forward_return_spans_next_open_to_horizon_close():
    f = _frame()
    i, hzn = 100, 10
    r = h.raw_forward_return(f, i, hzn)
    expected = float(f["Close"].iloc[i + hzn]) / float(f["Open"].iloc[i + 1]) - 1
    assert r == pytest.approx(expected)
    assert h.raw_forward_return(f, len(f) - 3, hzn) is None   # not enough bars ahead


# --- sampling -------------------------------------------------------------- #

def test_samples_have_a_year_behind_and_the_horizon_ahead():
    frames = {"A": _frame(600), "B": _frame(400, seed=2)}
    drawn = h.draw_samples(frames, 50, 10, random.Random(3))
    assert drawn and len(drawn) == len(set(drawn))
    for t, i in drawn:
        assert i >= h.MIN_HISTORY_BARS
        assert i + 10 + 2 <= len(frames[t])


def test_sampling_is_reproducible_by_seed():
    frames = {"A": _frame(600), "B": _frame(600, seed=2)}
    a = h.draw_samples(frames, 30, 10, random.Random(9))
    b = h.draw_samples(frames, 30, 10, random.Random(9))
    assert a == b


def test_a_ticker_with_too_little_history_is_never_sampled():
    frames = {"A": _frame(600), "SHORT": _frame(200, seed=5)}
    drawn = h.draw_samples(frames, 40, 10, random.Random(1))
    assert all(t == "A" for t, _ in drawn)


# --- context --------------------------------------------------------------- #

def test_withheld_dimensions_are_named_gaps_not_silent_absences():
    ctx = h.build_sample_context("MSFT", ["h1"], None)
    joined = " ".join(ctx.gaps)
    assert "fundamentals withheld" in joined
    assert "analyst view withheld" in joined
    assert "insider activity withheld" in joined
    assert ctx.fundamentals is None and ctx.analysts is None and ctx.insiders is None


def test_a_fund_is_not_told_about_analysts_or_insiders():
    """Those sections never existed for a fund, so they are not 'withheld'."""
    ctx = h.build_sample_context("IWM", [], None)
    joined = " ".join(ctx.gaps)
    assert "fundamentals withheld" in joined
    assert "analyst" not in joined and "insider" not in joined


# --- scoring --------------------------------------------------------------- #

def _sig(t, bias, conv=0.8):
    return LLMSignal(ticker=t, bias=bias, conviction=conv, rationale="x")


def _sample(t, i, sig=None):
    return h.Sample(ticker=t, day="2024-01-01", index=i, system_prompt="S",
                    user_prompt="U", headlines=1, signal=sig)


def test_only_sided_signals_over_the_floor_are_traded():
    f = _frame()
    samples = [
        _sample("A", 300, _sig("A", Bias.BULLISH)),
        _sample("A", 310, _sig("A", Bias.BEARISH)),
        _sample("A", 320, _sig("A", Bias.NEUTRAL)),
        _sample("A", 330, _sig("A", Bias.BULLISH, conv=cfg.MIN_CONVICTION - 0.05)),
        _sample("A", 340, None),
    ]
    h.score(samples, {"A": f}, 10)
    assert samples[0].trade is not None and samples[0].trade.side == "buy"
    assert samples[1].trade is not None and samples[1].trade.side == "sell"
    assert samples[2].trade is None and samples[3].trade is None and samples[4].trade is None
    assert all(s.raw_forward is not None for s in samples)   # base rate uses every sample


def test_hit_means_the_direction_was_right():
    r = h.Report(samples=[], horizon=10)
    up = _sample("A", 1, _sig("A", Bias.BULLISH)); up.raw_forward = 0.02
    down = _sample("A", 2, _sig("A", Bias.BULLISH)); down.raw_forward = -0.02
    bear_ok = _sample("A", 3, _sig("A", Bias.BEARISH)); bear_ok.raw_forward = -0.01
    r.samples = [up, down, bear_ok]
    assert r.hit_rate(Bias.BULLISH) == (0.5, 2)
    assert r.hit_rate(Bias.BEARISH) == (1.0, 1)
    assert r.base_rate_up == pytest.approx(1 / 3)


def test_the_report_renders_the_base_rate_beside_the_hit_rate():
    r = h.Report(samples=[], horizon=10)
    s = _sample("A", 1, _sig("A", Bias.BULLISH)); s.raw_forward = 0.01
    r.samples = [s]
    text = h.render(r)
    assert "BASE RATE" in text and "must beat the base rate" in text
    assert "Two of five dimensions" in text
    d = json.loads(json.dumps(r.as_dict()))
    assert d["bullish"]["n"] == 1


def test_apply_results_returns_the_failures():
    s_ok, s_bad = _sample("A", 1), _sample("B", 2)
    good = llm.Completion(text=_sig("A", Bias.BULLISH).model_dump_json(), usage=None)
    failed = h.apply_results([s_ok, s_bad], {"A:2024-01-01": good, "B:2024-01-01": llm.LLMError("x")},
                             LLMSignal.model_validate_json)
    assert s_ok.signal is not None and s_bad.signal is None
    assert failed == [s_bad]


def test_samples_round_trip_through_json():
    s = _sample("A", 5)
    text = h._samples_to_json([s], 10, 7)
    back, horizon = h._samples_from_json(text)
    assert horizon == 10 and back[0].custom_id == s.custom_id
