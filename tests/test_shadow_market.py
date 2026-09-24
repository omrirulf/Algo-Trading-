"""The feed shows the engine the open of session T and nothing after it.

``SimFeed`` is the production ``YFinanceMarketData`` with only ``_history``
replaced, so the engine's price and ATR come from the production methods.
What has to be proved is the slice those methods are handed: the 90
calendar days of final bars before T, then a partial bar for T made of the
only thing known at the open (O = H = L = C = Open[T]) -- never T's own
high, low or close, and never a later bar. ``Bars`` is checked for the
index shapes yfinance really returns: tz-aware, duplicated, unsorted.
"""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from app.execution_engine import ExecutionEngine
from app.market_data import MarketDataError, YFinanceMarketData, calculate_atr
from app.schemas import Bias, ExecutionStatus, LLMSignal
from config import settings as cfg
from shadow.audit import FundAudit
from shadow.broker import SimBroker
from shadow.market import Bars, SimFeed, calendar

DAYS = pd.bdate_range("2026-01-02", "2026-07-31")


def tape(seed: int = 0, start: float = 100.0, vol: float = 0.02, days=DAYS) -> pd.DataFrame:
    rng = np.random.RandomState(seed)
    close = start * np.exp(np.cumsum(rng.normal(0.0, vol, len(days))))
    prev = np.concatenate([[start], close[:-1]])
    open_ = prev * np.exp(rng.normal(0.0, vol / 3, len(days)))
    spread = np.abs(rng.normal(0.0, vol, len(days))) + vol / 2
    return pd.DataFrame({
        "Open": open_,
        "High": np.maximum(open_, close) * (1 + spread),
        "Low": np.minimum(open_, close) * (1 - spread),
        "Close": close,
        "Volume": 1_000_000,
        "Dividends": 0.0,
    }, index=days)


def expected_atr(frame: pd.DataFrame, session: date) -> float:
    """``calculate_atr`` on what yfinance's "90d" shows at the open of ``session``:
    the final bars of the 90 calendar days ending on it, then the partial bar."""
    first = pd.Timestamp(session - timedelta(days=cfg.OHLC_LOOKBACK_DAYS))
    past = frame[(frame.index > first) & (frame.index < pd.Timestamp(session))][["Open", "High", "Low", "Close"]]
    opened = float(frame.loc[pd.Timestamp(session), "Open"])
    partial = pd.DataFrame({"Open": [opened], "High": [opened], "Low": [opened], "Close": [opened]},
                           index=pd.DatetimeIndex([pd.Timestamp(session)]))
    return calculate_atr(pd.concat([past, partial]), cfg.ATR_PERIOD)


SESSION = DAYS[120].date()


# --------------------------------------------------------------------------- #
# What the feed shows
# --------------------------------------------------------------------------- #


def test_the_answers_come_from_the_production_methods_once_per_ticker_and_session(monkeypatch):
    """The feed's own code is the slice and a memo; the price and the ATR are
    computed by ``YFinanceMarketData``'s methods, once for every fund that asks."""
    assert issubclass(SimFeed, YFinanceMarketData)
    calls: list[tuple[str, str]] = []
    for name in ("get_latest_price", "get_atr"):
        production = getattr(YFinanceMarketData, name)

        def spy(self, ticker, _production=production, _name=name):
            calls.append((_name, ticker))
            return _production(self, ticker)

        monkeypatch.setattr(YFinanceMarketData, name, spy)
    feed = SimFeed(Bars({"AAA": tape()}))
    assert feed._lookback_days == cfg.OHLC_LOOKBACK_DAYS and feed._atr_period == cfg.ATR_PERIOD
    feed.at_open(SESSION)
    for _ in range(3):
        feed.get_latest_price("AAA")
        feed.get_atr("aaa")
    assert calls == [("get_latest_price", "AAA"), ("get_atr", "AAA")]


def test_the_latest_price_at_session_t_is_the_open_of_t():
    frame = tape()
    feed = SimFeed(Bars({"AAA": frame}))
    for i in (60, 90, 120, len(DAYS) - 1):
        feed.at_open(DAYS[i].date())
        assert feed.get_latest_price("AAA") == float(frame["Open"].iloc[i])
        assert feed.get_latest_price("aaa") == float(frame["Open"].iloc[i])


def test_the_atr_is_the_production_atr_of_the_ninety_days_before_t_and_a_partial_bar():
    frame = tape()
    feed = SimFeed(Bars({"AAA": frame}))
    for i in (40, 64, 120, 150):
        day = DAYS[i].date()
        feed.at_open(day)
        assert feed.get_atr("AAA") == expected_atr(frame, day)
    feed.at_open(SESSION)
    history = feed._history("AAA")
    assert list(history.columns) == ["Open", "High", "Low", "Close"]
    assert history.index[-1] == pd.Timestamp(SESSION)
    last = history.iloc[-1]
    assert last["Open"] == last["High"] == last["Low"] == last["Close"] == frame.loc[pd.Timestamp(SESSION), "Open"]
    assert history.index[0] > pd.Timestamp(SESSION - timedelta(days=90))
    assert (history.index[1:] > history.index[:-1]).all()


def test_the_window_is_ninety_calendar_days_ending_at_t():
    """A bar dated exactly 90 days before T is outside; one day later is inside.

    The close is what is moved: the first bar of an ATR window contributes
    only its close (as the previous close of the second), so a close is the
    one field that proves a bar is in the window at all."""
    frame = tape()
    session = date(2026, 6, 1)                               # a Monday; T-90 is Wed 4 Mar, T-89 Thu 5 Mar
    edge, inside = pd.Timestamp(session - timedelta(days=90)), pd.Timestamp(session - timedelta(days=89))
    assert edge in frame.index and inside in frame.index
    base = SimFeed(Bars({"AAA": frame}))
    base.at_open(session)
    wild_edge = frame.copy()
    wild_edge.loc[edge, ["High", "Close"]] = [1_000.0, 1_000.0]
    moved_edge = SimFeed(Bars({"AAA": wild_edge}))
    moved_edge.at_open(session)
    wild_inside = frame.copy()
    wild_inside.loc[inside, ["High", "Close"]] = [1_000.0, 1_000.0]
    moved_inside = SimFeed(Bars({"AAA": wild_inside}))
    moved_inside.at_open(session)
    assert moved_edge.get_atr("AAA") == base.get_atr("AAA")
    assert moved_inside.get_atr("AAA") != base.get_atr("AAA")


def test_nothing_after_the_open_of_t_can_move_the_price_or_the_atr():
    """Build a second tape identical up to the open of T, then wild: T's own
    high, low and close, and every later bar. At T and every session before
    it, the feed must answer exactly as it did on the tame tape."""
    frame = tape()
    k = 120
    spiked = frame.copy()
    spiked.iloc[k, spiked.columns.get_loc("High")] *= 10
    spiked.iloc[k, spiked.columns.get_loc("Low")] *= 0.1
    spiked.iloc[k, spiked.columns.get_loc("Close")] *= 5
    spiked.iloc[k + 1:, [spiked.columns.get_loc(c) for c in ("Open", "High", "Low", "Close")]] *= 50
    spiked.iloc[k + 1:, spiked.columns.get_loc("Dividends")] = 3.0
    tame, wild = SimFeed(Bars({"AAA": frame})), SimFeed(Bars({"AAA": spiked}))
    for i in (k - 30, k - 5, k - 1, k):
        day = DAYS[i].date()
        tame.at_open(day)
        wild.at_open(day)
        assert wild.get_latest_price("AAA") == tame.get_latest_price("AAA")
        assert wild.get_atr("AAA") == tame.get_atr("AAA")
        assert wild._history("AAA").equals(tame._history("AAA"))
    wild.at_open(DAYS[k + 1].date())
    assert wild.get_latest_price("AAA") == pytest.approx(50 * frame["Open"].iloc[k + 1])   # and then it does


def test_an_unknown_ticker_or_one_with_no_bar_that_session_is_a_market_data_error():
    frame = tape()
    gappy = frame.drop(index=DAYS[120])
    feed = SimFeed(Bars({"AAA": frame, "GAP": gappy}))
    feed.at_open(SESSION)
    for ticker in ("ZZZZ", "GAP"):
        for ask in (feed.get_latest_price, feed.get_atr):
            with pytest.raises(MarketDataError) as err:
                ask(ticker)
            assert not isinstance(err.value, KeyError)
    feed.at_open(DAYS[121].date())
    assert feed.get_latest_price("GAP") == float(frame["Open"].iloc[121])
    # A ticker too new for a 14-bar ATR is a MarketDataError too.
    young = SimFeed(Bars({"NEW": frame.iloc[110:]}))
    young.at_open(DAYS[115].date())
    assert young.get_latest_price("NEW") == float(frame["Open"].iloc[115])
    with pytest.raises(MarketDataError):
        young.get_atr("NEW")


def test_a_feed_whose_clock_is_not_set_refuses():
    feed = SimFeed(Bars({"AAA": tape()}))
    with pytest.raises(MarketDataError, match="clock"):
        feed.get_latest_price("AAA")


def test_a_missing_bar_reaches_the_engine_as_a_market_data_error_not_an_unexpected_one():
    frame = tape()
    feed = SimFeed(Bars({"GAP": frame.drop(index=DAYS[120])}))
    feed.at_open(SESSION)
    broker = SimBroker("t", 100_000.0, quote=feed.get_latest_price, day=SESSION)
    result = ExecutionEngine(broker, feed, audit_logger=FundAudit("t").logger).execute(
        LLMSignal(ticker="GAP", bias=Bias.BULLISH, conviction=0.6, rationale="r"))
    assert result.status is ExecutionStatus.ERROR
    assert result.reason.startswith("MarketDataError: no bar for GAP")


def test_answers_are_cached_per_session_and_never_leak_into_another():
    frame = tape()
    feed = SimFeed(Bars({"AAA": frame}))
    first, second = DAYS[120].date(), DAYS[121].date()
    feed.at_open(first)
    price, atr = feed.get_latest_price("AAA"), feed.get_atr("AAA")
    feed.at_open(first)                                        # same session: still cached, same answers
    assert (feed.get_latest_price("AAA"), feed.get_atr("AAA")) == (price, atr)
    feed.at_open(second)
    assert feed.session == second
    assert feed.get_latest_price("AAA") == float(frame["Open"].iloc[121]) != price
    assert feed.get_atr("AAA") == expected_atr(frame, second) != atr
    feed.at_open(first)                                        # back again: recomputed, not remembered wrong
    assert (feed.get_latest_price("AAA"), feed.get_atr("AAA")) == (price, atr)


# --------------------------------------------------------------------------- #
# Bars
# --------------------------------------------------------------------------- #


def test_bars_sessions_bar_and_history():
    frame = tape()
    frame.loc[DAYS[10], "Dividends"] = 0.42
    bars = Bars({"aaa": frame, "BBB": frame.iloc[5:20]})
    assert bars.tickers() == ["AAA", "BBB"]
    first, last = DAYS[3].date(), DAYS[8].date()
    assert bars.sessions("AAA", first, last) == [d.date() for d in DAYS[3:9]]   # inclusive both ends
    assert bars.sessions("BBB", DAYS[0].date(), DAYS[6].date()) == [d.date() for d in DAYS[5:7]]
    assert bars.sessions("NOPE", first, last) == []
    row = frame.iloc[10]
    assert bars.bar("AAA", DAYS[10].date()) == (row.Open, row.High, row.Low, row.Close, 0.42)
    assert bars.bar("aaa", DAYS[11].date())[4] == 0.0
    assert bars.bar("AAA", date(2026, 1, 3)) is None                              # a Saturday
    assert bars.bar("NOPE", DAYS[10].date()) is None
    history = bars.history("AAA", DAYS[10].date())
    assert history.index[-1] == DAYS[10] and len(history) == 11                   # inclusive of ``through``
    assert bars.history("AAA", date(2026, 1, 4)).index[-1] == DAYS[0]             # a Sunday: Friday's
    assert bars.history("NOPE", DAYS[10].date()).empty
    assert bars.last_close_before("AAA", DAYS[10].date()) == float(frame["Close"].iloc[9])
    assert bars.last_close_before("AAA", DAYS[0].date()) is None
    from config.market_calendar import is_trading_day

    # The union of every ticker's sessions, trading days only.
    assert calendar(bars, ("NOPE", "BBB", "AAA"), DAYS[0].date(), DAYS[30].date()) == \
        [d.date() for d in DAYS[0:31] if is_trading_day(d.date())]
    assert calendar(bars, ("NOPE", "BBB"), DAYS[0].date(), DAYS[30].date()) == \
        [d.date() for d in DAYS[5:20] if is_trading_day(d.date())]
    assert calendar(bars, ("NOPE",), DAYS[0].date(), DAYS[30].date()) == []


def test_one_missing_index_bar_does_not_drop_the_session():
    """yfinance leaving one VT row out must not take that session away from
    every fund: its stops would never be checked and its cycle never sent."""
    from config.market_calendar import is_trading_day

    frame = tape()
    gap = next(d for d in DAYS[5:] if is_trading_day(d.date()))
    bars = Bars({"VT": frame.drop(index=gap), "MSFT": frame})
    days = calendar(bars, ("VT", "MSFT"), DAYS[0].date(), DAYS[30].date())
    assert gap.date() in days


@pytest.mark.parametrize("tz, hour", [("America/New_York", 0), ("UTC", 4), ("UTC", 20)])
def test_bars_file_a_tz_aware_index_under_its_exchange_date(tz, hour):
    frame = tape().iloc[:30]
    aware = frame.copy()
    aware.index = pd.DatetimeIndex([pd.Timestamp(d.date()).replace(hour=hour) for d in frame.index]).tz_localize(tz)
    bars = Bars({"AAA": aware})
    assert bars.sessions("AAA", DAYS[0].date(), DAYS[29].date()) == [d.date() for d in DAYS[:30]]
    assert bars.bar("AAA", DAYS[7].date())[0] == float(frame["Open"].iloc[7])
    assert bars.history("AAA", DAYS[7].date()).index.tz is None
    feed = SimFeed(bars)
    feed.at_open(DAYS[29].date())
    assert feed.get_atr("AAA") == expected_atr(frame, DAYS[29].date())


def test_bars_keep_the_last_of_a_duplicated_day_sort_the_rest_and_drop_incomplete_rows():
    frame = tape().iloc[:30]
    repeat = frame.iloc[[12]].copy()
    repeat["Open"] = 777.0
    messy = pd.concat([frame.iloc[15:], frame.iloc[:15], repeat])               # out of order; day 12 re-sent last
    messy.loc[DAYS[20], "Close"] = np.nan                                       # an unfinished bar
    messy = messy.drop(columns=["Dividends"])
    bars = Bars({"AAA": messy})
    days = bars.sessions("AAA", DAYS[0].date(), DAYS[29].date())
    assert days == sorted(days) and len(days) == 29 and DAYS[20].date() not in days
    assert bars.bar("AAA", DAYS[12].date())[0] == 777.0
    assert bars.bar("AAA", DAYS[13].date())[4] == 0.0                           # no Dividends column: none
    history = bars.history("AAA", DAYS[29].date())
    assert history.index.is_monotonic_increasing and not history.index.has_duplicates


def test_bars_of_an_empty_frame_have_nothing_and_the_feed_says_so():
    bars = Bars({"AAA": pd.DataFrame(columns=["Open", "High", "Low", "Close"]), "BBB": None})
    assert bars.sessions("AAA", DAYS[0].date(), DAYS[-1].date()) == []
    assert bars.history("BBB", DAYS[-1].date()).empty
    feed = SimFeed(bars)
    feed.at_open(DAYS[5].date())
    with pytest.raises(MarketDataError):
        feed.get_latest_price("AAA")
