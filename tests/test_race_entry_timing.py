"""A late run changes when a signal is made, never the price it is entered at.

The race scores every arm's trade from ``backtest.simulate.simulate_trade``,
which enters at the Open of the bar AFTER the signal bar, and the signal bar
is chosen by ``analysis.baseline_compare._signal_index``: the last bar dated
on or before the line's UTC calendar day. So the entry is the first session
that opens after the signal's UTC day has ended.

That rule was checked here, by reading the code and then by running it,
for every time of day a journal line can be written -- the question being
whether any of them can enter at a price that was already printed when the
model was asked. None can: a bar is dated by its New York session day, and a
New York day never starts after the UTC day of the same instant, so the
entry bar is always dated after the signal's New York day too. Two paths
are conservative -- they can wait up to one session longer than they
strictly need to -- and are pinned as such, so a later change to them is a
decision someone makes, not a drift:

* a line written before the open (the 12:35 UTC pre-market run that never
  once arrived on time) enters at the NEXT day's open, not the same day's;
* a line written after midnight UTC but before midnight New York -- from
  20:00 New York in summer, from 19:00 in winter -- carries the next UTC
  date, so it enters one session after the first open that followed it
  (unless no session comes between, as on a Friday evening).

Every case below uses hand-built bars whose Opens are all different, so the
entry price names the bar it came from. No network.
"""

from __future__ import annotations

from datetime import date, datetime, time, timedelta, timezone

import pandas as pd
import pytest

from analysis import decision_gate, horse_race
from analysis.baseline_compare import simulate_model_trades
from analysis.metrics import ScoredSignal
from analysis.reader import JournalEntry, entry_from
from analysis.returns import MARKET_TZ, ForwardReturn, PriceSeries, final_bars
from config.market_calendar import is_trading_day
from rules import EXPLORATORY, control, hybrid, momentum

UTC = timezone.utc
HORIZON = 3
UPTREND = {"return_63d": 0.10, "distance_sma50": 0.03, "annualised_volatility": 0.20}

#: Every NYSE session from June to the end of 2026, by the repo's own calendar:
#: 3 Jul, 7 Sep (Labor Day) and 26 Nov (Thanksgiving) are not in it.
SESSIONS = [d for d in (date(2026, 6, 1) + timedelta(days=i) for i in range(214)) if is_trading_day(d)]


def bars(days=SESSIONS, index: str = "new_york") -> pd.DataFrame:
    """OHLC on ``days``, every Open different, so a price names its bar.

    ``index`` is how the source dates its bars: yfinance hands back midnight
    in the exchange's own zone (``new_york``); ``utc`` and ``naive`` are the
    two other shapes a source could plausibly use. All three must agree.
    """
    stamps = pd.DatetimeIndex([pd.Timestamp(d) for d in days])
    if index == "new_york":
        stamps = stamps.tz_localize("America/New_York")
    elif index == "utc":
        stamps = stamps.tz_localize("UTC")
    opens = [100.0 + 0.25 * i for i in range(len(days))]
    return pd.DataFrame({
        "Open": opens,
        "High": [o + 1.5 for o in opens],
        "Low": [o - 1.5 for o in opens],
        "Close": [o + 0.2 for o in opens],
    }, index=stamps)


def open_on(frame: pd.DataFrame, day: date) -> float:
    rows = [i for i, ts in enumerate(frame.index) if ts.date() == day]
    assert len(rows) == 1, f"the frame has no single bar for {day}"
    return float(frame.iloc[rows[0]]["Open"])


class Fetcher:
    """Hands back pre-built frames, cut to final bars like the real fetcher."""

    def __init__(self, frames: dict[str, pd.DataFrame], final_through: date | None = None):
        self.frames, self.final_through = frames, final_through

    def ohlc(self, ticker, start, end):
        frame = self.frames.get(ticker, pd.DataFrame())
        if self.final_through is None or frame.empty:
            return frame
        return frame[[ts.date() <= self.final_through for ts in frame.index]]


class Closes:
    """Daily closes from the same frames, for the scorer's resolved-or-pending check."""

    def __init__(self, frames: dict[str, pd.DataFrame], final_through: date | None = None):
        self.frames, self.final_through = frames, final_through

    def closes(self, ticker, start, end):
        frame = self.frames.get(ticker)
        if frame is None:
            return PriceSeries(ticker, [])
        series = [(ts.date(), float(c)) for ts, c in frame["Close"].items()]
        return PriceSeries(ticker, final_bars(series, self.final_through))


def acted_on(stamp: datetime, ticker: str = "NVDA", exact: bool = True, bias: str = "BULLISH") -> ScoredSignal:
    """One signal as the race hands it to the simulator; ``forward`` is never read there."""
    entry = JournalEntry(ticker=ticker, timestamp=stamp, timestamp_is_exact=exact, bias=bias, conviction=0.72)
    placeholder = ForwardReturn(entry_date=date(2026, 1, 1), exit_date=date(2026, 1, 2),
                                entry_price=1.0, exit_price=1.0, pct=0.0)
    return ScoredSignal(entry=entry, forward=placeholder)


def entered(stamp: datetime, frame: pd.DataFrame, exact: bool = True):
    trades, matched, dropped = simulate_model_trades(
        [acted_on(stamp, exact=exact)], equity=100_000.0, horizon_days=HORIZON,
        stop_multiplier=2.0, max_position_pct=0.05, fetcher=Fetcher({"NVDA": frame}),
    )
    assert dropped == 0 and len(trades) == 1, "the case must produce exactly one trade"
    return trades[0]


def assert_entered_after(stamp: datetime, trade, frame: pd.DataFrame, expected: date) -> None:
    """The four things every case must show."""
    entry_day = date.fromisoformat(trade.entry_date)
    assert entry_day == expected
    assert trade.entry_price == open_on(frame, expected), "entry is the entry bar's Open"
    assert entry_day > stamp.astimezone(UTC).date(), "entry bar dated after the signal's UTC day"
    # The one that matters: the open the trade was filled at printed after
    # the signal was made. 09:30 New York on the entry day, in either season.
    opened = datetime.combine(entry_day, time(9, 30), tzinfo=MARKET_TZ)
    assert opened > stamp, "entered at a price printed before the signal existed"


# --------------------------------------------------------------------------- #
# Every time of day a line can be written
# --------------------------------------------------------------------------- #

CASES = [
    # (what, the line's UTC timestamp, the entry session the race uses)
    ("session, 15:06 UTC = 11:06 New York (every cycle since 21 Sep)",
     datetime(2026, 9, 22, 15, 6, tzinfo=UTC), date(2026, 9, 23)),
    ("session, 17:35 UTC = 13:35 New York (the second cron slot)",
     datetime(2026, 9, 22, 17, 35, tzinfo=UTC), date(2026, 9, 23)),
    ("after the close, 20:30 UTC = 16:30 New York",
     datetime(2026, 9, 22, 20, 30, tzinfo=UTC), date(2026, 9, 23)),
    # Conservative: 20:30 New York on the 22nd is the 23rd in UTC, so the
    # 23rd's open -- the first after the signal -- is skipped for the 24th's.
    ("after the close, 00:30 UTC the next UTC day = 20:30 New York",
     datetime(2026, 9, 23, 0, 30, tzinfo=UTC), date(2026, 9, 24)),
    # Conservative: the 22nd's open printed after an 08:35 signal, but the
    # signal bar is the 22nd's own, so the race waits for the 23rd.
    ("before the open, 12:35 UTC = 08:35 New York (the --premarket slot)",
     datetime(2026, 9, 22, 12, 35, tzinfo=UTC), date(2026, 9, 23)),
    ("Friday in the session: entry Monday",
     datetime(2026, 9, 18, 15, 6, tzinfo=UTC), date(2026, 9, 21)),
    ("Friday after the close, already Saturday in UTC: entry Monday",
     datetime(2026, 9, 19, 0, 30, tzinfo=UTC), date(2026, 9, 21)),
    ("the Friday before Labor Day: entry Tuesday",
     datetime(2026, 9, 4, 15, 6, tzinfo=UTC), date(2026, 9, 8)),
    ("the day before Thanksgiving: entry the half day after it",
     datetime(2026, 11, 25, 15, 6, tzinfo=UTC), date(2026, 11, 27)),
    # Winter: 20:30 UTC is 15:30 EST, still in the session.
    ("winter session, 20:30 UTC = 15:30 New York",
     datetime(2026, 12, 1, 20, 30, tzinfo=UTC), date(2026, 12, 2)),
    ("winter, 14:40 UTC = 09:40 New York (the 14:40 UTC schedule)",
     datetime(2026, 12, 1, 14, 40, tzinfo=UTC), date(2026, 12, 2)),
    # Conservative, and earlier in the evening than in summer: EST is UTC-5,
    # so 00:30 UTC is 19:30 New York on the 1st, already the 2nd in UTC.
    ("winter after the close, 00:30 UTC the next UTC day = 19:30 New York",
     datetime(2026, 12, 2, 0, 30, tzinfo=UTC), date(2026, 12, 3)),
]


@pytest.mark.parametrize("index", ["new_york", "utc", "naive"])
@pytest.mark.parametrize("what, stamp, expected", CASES, ids=[c[0] for c in CASES])
def test_entry_is_the_next_sessions_open_after_the_signals_day(what, stamp, expected, index):
    frame = bars(index=index)
    trade = entered(stamp, frame)
    assert_entered_after(stamp, trade, frame, expected)


# --------------------------------------------------------------------------- #
# A day the price source never printed (the 22 Sep Yahoo hole)
# --------------------------------------------------------------------------- #

HOLE = date(2026, 9, 22)


@pytest.mark.parametrize("stamp, expected", [
    # The signal's own day is missing: the signal bar falls back to the 21st,
    # and the next bar the source HAS is the 23rd. Never the 21st's.
    (datetime(2026, 9, 22, 15, 6, tzinfo=UTC), date(2026, 9, 23)),
    (datetime(2026, 9, 22, 12, 35, tzinfo=UTC), date(2026, 9, 23)),
    # The day after the signal is missing: the race enters at the next open
    # it has, a session later than the market offered, never earlier.
    (datetime(2026, 9, 21, 15, 6, tzinfo=UTC), date(2026, 9, 23)),
])
def test_a_missing_bar_moves_the_entry_later_never_earlier(stamp, expected):
    frame = bars([d for d in SESSIONS if d != HOLE])
    trade = entered(stamp, frame)
    assert_entered_after(stamp, trade, frame, expected)


# --------------------------------------------------------------------------- #
# What the reader hands the simulator: always an aware UTC timestamp
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("fields, utc_day, exact, expected", [
    ({"ts_utc": "2026-09-22T15:06:50.177746+00:00"}, date(2026, 9, 22), True, date(2026, 9, 23)),
    # An offset other than UTC is converted, not read as a wall clock.
    ({"ts_utc": "2026-09-22T20:30:00-04:00"}, date(2026, 9, 23), True, date(2026, 9, 24)),
    # A ts_utc with no offset is read as UTC.
    ({"ts_utc": "2026-09-22T15:06:00"}, date(2026, 9, 22), True, date(2026, 9, 23)),
    # The old tz-naive logging field: read as UTC and flagged inexact.
    ({"ts": "2026-09-22 15:06:50,177"}, date(2026, 9, 22), False, date(2026, 9, 23)),
])
def test_every_timestamp_the_reader_accepts_is_aware_utc(fields, utc_day, exact, expected):
    """``simulate_model_trades`` calls ``timestamp.date()`` directly, which on
    an aware datetime is the date in its own zone. The reader always hands it
    UTC -- converted from any offset, or assumed for the naive old field -- so
    ``.date()`` is the UTC date in every case and the race's own ``_line_day``
    (``astimezone(UTC).date()``) can never disagree with it."""
    entry = entry_from({"ticker": "NVDA", "signal": {"bias": "BULLISH", "conviction": 0.72}, **fields})
    assert entry.timestamp.tzinfo is not None
    assert entry.timestamp.utcoffset() == timedelta(0)
    assert entry.timestamp.date() == utc_day == horse_race._line_day(entry)
    assert entry.timestamp_is_exact is exact

    frame = bars()
    trade = entered(entry.timestamp, frame, exact=exact)
    assert_entered_after(entry.timestamp, trade, frame, expected)


# --------------------------------------------------------------------------- #
# Every arm, the coin flip's both sides, and the index: the same open
# --------------------------------------------------------------------------- #

ARM_CASES = [
    (datetime(2026, 9, 22, 15, 6, tzinfo=UTC), date(2026, 9, 23)),
    (datetime(2026, 9, 22, 12, 35, tzinfo=UTC), date(2026, 9, 23)),
    (datetime(2026, 9, 23, 0, 30, tzinfo=UTC), date(2026, 9, 24)),
    (datetime(2026, 9, 18, 17, 35, tzinfo=UTC), date(2026, 9, 21)),
]


def _line(ticker: str, stamp: datetime) -> JournalEntry:
    # Two distinct insiders buying ten days before the line, so the
    # exploratory insider arm takes a side on every line too.
    bought = (stamp - timedelta(days=10)).date().isoformat()
    insiders = {"buys": [{"when": bought, "who": who, "role": "Director", "shares": 100.0, "value": None}
                         for who in ("Ann", "Bob")], "sells": []}
    return JournalEntry(ticker=ticker, timestamp=stamp, timestamp_is_exact=True, bias="BULLISH",
                        conviction=0.72, scores={"news_score": 0.4}, technicals=dict(UPTREND),
                        insiders=insiders)


def _race_setup():
    frame = bars()
    tickers = [f"T{i}" for i in range(len(ARM_CASES))]
    frames = {t: frame for t in tickers}
    lines = [_line(t, stamp) for t, (stamp, _) in zip(tickers, ARM_CASES)]
    expected = {t: day for t, (_, day) in zip(tickers, ARM_CASES)}
    final = date(2026, 10, 30)
    common = dict(horizon=HORIZON, entry_rule="auto", today=final, source=Closes(frames, final),
                  fetcher=Fetcher(frames, final), equity=100_000.0, stop_multiplier=2.0,
                  max_position_pct=0.05, cost_per_side=0.001)
    return frame, lines, expected, common


@pytest.mark.parametrize("arm", [*horse_race.ARM_ORDER, *sorted(EXPLORATORY)])
def test_every_arm_enters_at_the_same_next_session_open(arm):
    """The rule arms are the model's lines with the call replaced; ticker and
    timestamp are untouched, so they reach the same bar through the same code.
    The exploratory arm too: it is raced through the same ``race_arm``."""
    frame, lines, expected, common = _race_setup()
    result = horse_race.race_arm(arm, lines, floor=0.30, **common)
    assert result.n == len(lines), f"{arm} traded every line"
    for trade in result.trades:
        assert trade.entry_day == expected[trade.ticker]
        assert trade.trade.entry_price == open_on(frame, trade.entry_day)
        assert trade.entry_day > trade.signal_day == trade.signal_at.astimezone(UTC).date()
        assert datetime.combine(trade.entry_day, time(9, 30), tzinfo=MARKET_TZ) > trade.signal_at


def test_the_coin_flip_enters_both_sides_at_the_same_open():
    frame, lines, expected, common = _race_setup()
    sides = horse_race.both_sides(lines, **common)
    assert len(sides) == len(lines)
    for (ticker, stamp), pair in sides.items():
        for trade in (pair.buy, pair.sell):
            assert trade.entry_day == expected[ticker] > stamp.date()
            assert trade.trade.entry_price == open_on(frame, trade.entry_day)


def test_the_index_is_bought_at_the_same_open_the_arms_entered_at():
    """VT is bought at the entry day's open and held to the close of the
    horizon bar: the same window as every trade opened that day, so it too
    starts after the signal.

    Through the race's own path, not a helper called by hand: the grid is
    built the way ``run_race`` builds it (every entry day any arm traded),
    and each day's index return is ``horse_race.index_daily``'s. A version
    that bought VT one session early -- at a price printed before the signal
    -- fails here."""
    frame, lines, expected, common = _race_setup()
    vt = bars()
    index = horse_race.index_bars(Fetcher({decision_gate.INDEX_TICKER: vt}), SESSIONS[0], date(2026, 10, 30))
    results = [horse_race.race_arm(name, lines, floor=0.30, **common) for name in horse_race.ARM_ORDER]
    grid = sorted({t.entry_day for r in results for t in r.trades})
    assert grid == sorted(set(expected.values()))
    daily = horse_race.index_daily(index, grid, HORIZON)
    assert sorted(daily) == grid, "every entry day's window is priced"
    trades = next(r for r in results if r.name == horse_race.MODEL_ARM).trades
    for trade in trades:
        position = next(i for i, bar in enumerate(index) if bar[0] == trade.entry_day)
        assert index[position][1] == open_on(vt, trade.entry_day)
        bought_at, sold_at = open_on(vt, trade.entry_day), index[position + HORIZON - 1][2]
        assert daily[trade.entry_day] == pytest.approx(sold_at / bought_at - 1.0)
        # Not the previous session's open, which was printed before the signal.
        before = open_on(vt, index[position - 1][0])
        assert daily[trade.entry_day] != pytest.approx(sold_at / before - 1.0)
        # The arm's trade and the index's window are the same sessions.
        assert trade.exit_day == index[position + HORIZON - 1][0]
        assert trade.entry_day > trade.signal_day


# --------------------------------------------------------------------------- #
# End to end: the journal file, the race's own main, the per-trade table
# --------------------------------------------------------------------------- #


def test_the_race_itself_prints_every_entry_on_the_next_sessions_open(tmp_path, monkeypatch, capsys):
    from tests.test_horse_race import _race

    cases = {
        "AAA": (datetime(2026, 9, 22, 15, 6, 50, tzinfo=UTC), date(2026, 9, 23)),
        "BBB": (datetime(2026, 9, 22, 20, 30, tzinfo=UTC), date(2026, 9, 23)),
        "CCC": (datetime(2026, 9, 23, 0, 30, tzinfo=UTC), date(2026, 9, 24)),
        "DDD": (datetime(2026, 9, 22, 12, 35, tzinfo=UTC), date(2026, 9, 23)),
        "EEE": (datetime(2026, 9, 18, 17, 35, tzinfo=UTC), date(2026, 9, 21)),
    }
    frame = bars()
    lines = [{"ts_utc": stamp.isoformat(), "ticker": ticker, "context": {"technicals": UPTREND},
              "signal": {"bias": "BULLISH", "conviction": 0.72, "news_score": 0.4}}
             for ticker, (stamp, _) in cases.items()]
    now = datetime(2026, 10, 20, 22, 0, tzinfo=UTC)
    code, out = _race(tmp_path, monkeypatch, capsys, {t: frame for t in cases}, lines, now)
    assert code == 0

    seen = {}
    for row in out.splitlines():
        parts = row.split()
        if (len(parts) == 10 and parts[0] in ("model", momentum.NAME, hybrid.NAME, control.NAME)
                and parts[1] in cases and parts[2].count("-") == 2):
            seen[(parts[0], parts[1])] = (date.fromisoformat(parts[2]), date.fromisoformat(parts[3]))
    assert len(seen) == 4 * len(cases), "every arm traded every line"
    for (arm, ticker), (signal_day, entry_day) in seen.items():
        stamp, expected = cases[ticker]
        assert signal_day == stamp.date()
        assert entry_day == expected, (arm, ticker)
        assert entry_day > signal_day
