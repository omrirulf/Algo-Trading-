"""The race and the funds cannot see ``live`` or ``management``.

The owner's rule of 25 Sep 2026: record the price at signal time on every
line, and do not change the race or the funds. Both still enter at the next
session's open. So the same journal, once as it was written before these
fields existed and once with them on every line -- prices read, prices
failed, the market found shut -- must give byte-identical race output and
identical fund books.
"""

from __future__ import annotations

import json
from datetime import date, datetime, timedelta, timezone

import numpy as np
import pandas as pd
import pytest

from analysis import decision_gate, horse_race
from analysis.reader import read_lines
from analysis.returns import PriceSeries, final_bars
from backtest.simulate import MIN_WARMUP_BARS
from shadow.fund import Fund, IndexFund, coin_signal, cycle_days, lines_by_day, model_signal, rule_signal, run
from shadow.market import Bars, SimFeed

TICKERS = ("NVDA", "XOM", "TLT", "GLD", "XLK")
WARM = MIN_WARMUP_BARS + 30
DAYS = pd.bdate_range("2026-01-05", periods=WARM + 45)
SIGNAL_DAYS = [d.date() for d in DAYS[WARM: WARM + 30]]
TREND = {
    "up": {"return_63d": 0.10, "distance_sma50": 0.03, "annualised_volatility": 0.20},
    "down": {"return_63d": -0.12, "distance_sma50": -0.04, "annualised_volatility": 0.25},
}


def _walk(seed: int, start: float) -> pd.DataFrame:
    rng = np.random.RandomState(seed)
    n = len(DAYS)
    close = start * np.exp(np.cumsum(rng.normal(0.0005, 0.015, n)))
    open_ = np.concatenate([[start], close[:-1]]) * np.exp(rng.normal(0, 0.004, n))
    spread = np.abs(rng.normal(0, 0.01, n)) + 0.004
    return pd.DataFrame({
        "Open": open_, "High": np.maximum(open_, close) * (1 + spread),
        "Low": np.minimum(open_, close) * (1 - spread), "Close": close,
        "Volume": 1_000_000.0, "Dividends": 0.0,
    }, index=DAYS)


FRAMES = {t: _walk(i, 40.0 + 25 * i) for i, t in enumerate(TICKERS)}
FRAMES["VT"] = _walk(99, 110.0)
FRAMES["SPY"] = _walk(98, 500.0)


def _journal(with_new_fields: bool) -> list[dict]:
    """A month of cycles: answers both ways, NEUTRALs, held and failed lines."""
    rng = np.random.RandomState(7)
    lines = []
    for k, day in enumerate(SIGNAL_DAYS):
        stamp = datetime(day.year, day.month, day.day, 14, 45, tzinfo=timezone.utc)
        closed = k % 9 == 4  # now and then a cycle that straddled the close
        for i, ticker in enumerate(TICKERS):
            u = rng.rand()
            line = {"ts_utc": (stamp + timedelta(seconds=i)).isoformat(), "ticker": ticker,
                    "context": {"technicals": TREND["up" if rng.rand() < 0.6 else "down"], "gaps": []},
                    "signal": None, "outcome": None, "error": None, "held": False, "stage": None,
                    "screening": False, "reasoning_effort": "high"}
            if u < 0.08:
                line["held"] = True
            elif u < 0.14:
                line["error"] = "timed out"
            else:
                bias = ("BULLISH", "BEARISH", "NEUTRAL")[int(rng.rand() * 3)]
                line["signal"] = {"ticker": ticker, "bias": bias, "conviction": float(rng.choice([0.3, 0.55, 0.8])),
                                  "rationale": "r", "news_score": float(rng.uniform(-1, 1))}
                reason = "market is closed" if closed else (
                    "bias is NEUTRAL; no trade" if bias == "NEUTRAL" else "accepted")
                line["outcome"] = {"mode": "direct", "status": "REJECTED" if closed or bias == "NEUTRAL"
                                   else "ACCEPTED", "reason": reason}
            if with_new_fields:
                asked = (stamp + timedelta(seconds=i, milliseconds=300)).isoformat()
                if u < 0.9:
                    line["live"] = {"price": round(float(FRAMES[ticker]["Close"].iloc[WARM + k]) * 1.013, 2),
                                    "bid": None if u > 0.7 else 1.0, "ask": None if u > 0.7 else 1.1,
                                    "quote_at": stamp.isoformat(), "asked_at": asked,
                                    "source": "alpaca-iex" if u < 0.7 else "yfinance"}
                else:
                    line["live"] = {"price": None, "bid": None, "ask": None, "quote_at": None,
                                    "asked_at": asked, "source": "yfinance",
                                    "error": "alpaca-iex: no answer within 5.0s; yfinance: no bars"}
                line["management"] = {"market_closed": closed}
            lines.append(line)
    return lines


def test_the_two_journals_differ_only_in_the_new_fields():
    plain, rich = _journal(False), _journal(True)
    assert len(plain) == len(rich) > 100
    for a, b in zip(plain, rich):
        assert {k: v for k, v in b.items() if k not in ("live", "management")} == a
    entries = read_lines(json.dumps(line) for line in rich).entries
    assert any(e.live and e.live.get("error") for e in entries)
    assert any(e.management_market_closed for e in entries)
    assert any(e.outcome_reason == "market is closed" for e in entries)


# --------------------------------------------------------------------------- #
# The race
# --------------------------------------------------------------------------- #


class _Closes:
    def __init__(self, final_through=None):
        self.final_through = final_through

    def closes(self, ticker, start, end):
        df = FRAMES.get(ticker)
        if df is None:
            return PriceSeries(ticker, [])
        return PriceSeries(ticker, final_bars([(ts.date(), float(c)) for ts, c in df["Close"].items()],
                                              self.final_through))


class _Ohlc:
    def __init__(self, final_through=None):
        self.final_through = final_through

    def ohlc(self, ticker, start, end):
        df = FRAMES.get(ticker, pd.DataFrame())
        if self.final_through is None or df.empty:
            return df
        return df[[ts.date() <= self.final_through for ts in df.index]]


def _race(tmp_path, monkeypatch, capsys, lines, *extra) -> str:
    journal = tmp_path / "journal.log"
    journal.write_text("\n".join(json.dumps(line) for line in lines) + "\n", encoding="utf-8")
    cutoff = date(2000, 1, 1)
    monkeypatch.setattr(decision_gate, "DECISION_CUTOFF", cutoff)
    monkeypatch.setattr(decision_gate, "FAILURE_WATCH_START", cutoff)
    now = datetime.combine(DAYS[-1].date(), datetime.min.time(), tzinfo=timezone.utc) + timedelta(days=1)
    monkeypatch.setattr(horse_race, "_now", lambda: now)
    monkeypatch.setattr(horse_race, "YFinancePriceSource", _Closes)
    monkeypatch.setattr(horse_race, "OhlcFetcher", _Ohlc)
    horse_race.main(["--journal", str(journal), "--seeds", "20", *extra])
    return capsys.readouterr().out


@pytest.mark.parametrize("extra", [("--per-trade",), ("--gate-json",), ("--horizon", "1", "--per-trade")])
def test_the_race_prints_the_same_bytes_with_or_without_them(tmp_path, monkeypatch, capsys, extra):
    plain = _race(tmp_path, monkeypatch, capsys, _journal(False), *extra)
    rich = _race(tmp_path, monkeypatch, capsys, _journal(True), *extra)
    assert plain == rich
    assert len(plain) > 500, "the race had something to say"
    if "--per-trade" in extra:
        assert "model" in plain and "momentum" in plain


# --------------------------------------------------------------------------- #
# The funds
# --------------------------------------------------------------------------- #


def _funds(lines: list[dict]):
    entries = read_lines(json.dumps(line) for line in lines).entries
    bars = Bars(FRAMES)
    feed = SimFeed(bars)
    funds = [
        Fund("model", model_signal, feed, bars, keep_actions=True),
        Fund("momentum", rule_signal("momentum"), feed, bars, keep_actions=True),
        Fund("coin-3", coin_signal(3), feed, bars, keep_actions=True),
        IndexFund("vt", "VT", bars),
    ]
    sessions = [d.date() for d in DAYS[WARM:]]
    run(funds, sessions, lines_by_day(entries), cycle_days(entries), feed)
    index = funds.pop()
    return [index.days] + [(f.days, f.broker.fills, f.broker.closed, f.decisions, f.audit.actions,
                            f.tally.accepted, f.tally.unexpected) for f in funds]


def test_the_funds_keep_the_same_books_with_or_without_them():
    plain, rich = _funds(_journal(False)), _funds(_journal(True))
    assert plain == rich
    model_fills = plain[1][1]
    assert model_fills, "the model fund traded, so there was something to compare"
    assert any(fills for (_, fills, *_) in plain[1:])
