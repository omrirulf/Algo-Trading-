"""Exploratory tests A, B and C (pre-registration section 13), for the shadow funds.

* **A** (``veto_signal``): the momentum rule's signal, kept only when the
  line's live price is on its side of the 200-day simple moving average of
  final closes up to the session before the signal's day (13.2).
* **B** (``TimingFund``): VT when VT's month-end close is above the average
  of its last 10 month-end closes, else BIL; switched at the next open,
  0.10% per side, from the 2026-09-30 month-end (13.3).
* **C** (``PullbackFund``): the momentum fund's signals entered by limit
  order at the signal price minus (a short: plus) half the line's ATR14,
  valid 3 sessions (13.4).

And their counters, the only thing shown between checkpoints (13.1): the
share of momentum signals A's veto removes, B's switches and state, and C's
fill rate. Each is counted from the journal and the prices alone, without
running a fund, so no fund result is made to count them.

Nothing here trades: the funds are the same simulated books as every other
shadow fund (``shadow.fund``), and CI keeps ``shadow/`` from a broker.
"""

from __future__ import annotations

import math
from collections import Counter
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Final, Mapping, Optional, Sequence

from app.schemas import Bias, ExecutionStatus, LLMSignal
from config import settings as cfg
from config.market_calendar import is_trading_day
from shadow.broker import DEFAULT_COST_PER_SIDE
from shadow.fund import (
    PULLBACK, STARTING_CASH, Day, Fund, Line, SignalFor, Tally, refused_by, rule_signal,
)
from shadow.market import Bars

#: The funds' names, as the output and the graveyard use them.
VETO: Final[str] = "momentum_200"
TIMING: Final[str] = "vt_timing"
LIMIT: Final[str] = "momentum_pullback"
NEW_FUNDS: Final[tuple[str, ...]] = (VETO, TIMING, LIMIT)
#: What each is compared with (13.2-13.4).
COMPARED_WITH: Final[dict[str, str]] = {VETO: "momentum", TIMING: "vt", LIMIT: "momentum"}

#: A: the veto's average, in final closes (Brock, Lakonishok and LeBaron 1992).
VETO_SMA: Final[int] = 200
#: B: the month-end closes averaged (Faber 2007), the two funds, and the first decision.
TIMING_MONTHS: Final[int] = 10
TIMING_IN: Final[str] = "VT"
TIMING_OUT: Final[str] = "BIL"
TIMING_FIRST_MONTH_END: Final[date] = date(2026, 9, 30)
#: C: the limit's distance in ATR14, and how many sessions it stands.
PULLBACK_ATRS: Final[float] = 0.5
PULLBACK_SESSIONS: Final[int] = 3
#: Calendar days of closes fetched before the first cycle: 200 sessions
#: for A, and 10 month-ends before 2026-09-30 for B, with room to spare.
LONG_LEAD_DAYS: Final[int] = 330


def pullback_acted(fund: "PullbackFund", momentum) -> int:
    """C acting differently from the momentum fund (13.7): each momentum signal on which the two
    funds did differently. One bought it and the other did not, or both bought it at different
    prices. A signal both funds skipped (held in both, no room in either) is no difference.

    The momentum fund bought a signal when it has an entry in that name at the first session
    after the signal's day; C bought it when one of its limit orders for it filled.
    """
    from shadow.broker import ENTRY

    paid = {(f.ticker, f.day): f.price for f in momentum.broker.fills if f.kind == ENTRY}
    mine = {(ticker, signal_day): price for ticker, signal_day, _, price in fund.pullback.filled}
    differs = 0
    for ticker, signal_day in fund.pullback.considered:
        ours = mine.get((ticker, signal_day))
        theirs = paid.get((ticker, sessions_after(signal_day, 1)[0]))
        if ours is None and theirs is None:
            continue
        if ours is None or theirs is None or not math.isclose(ours, theirs, rel_tol=1e-9, abs_tol=1e-9):
            differs += 1
    return differs


def _positive(value: object) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value) if math.isfinite(value) and value > 0 else None


# --------------------------------------------------------------------------- #
# A: the 200-day veto
# --------------------------------------------------------------------------- #


def sma_before(bars: Bars, ticker: str, day: date, length: int = VETO_SMA) -> Optional[float]:
    """The mean of ``ticker``'s last ``length`` final closes dated before ``day``; None with fewer."""
    closes = bars.history(ticker, day - timedelta(days=1))["Close"]
    if len(closes) < length:
        return None
    return float(closes.iloc[-length:].mean())


def live_price(line: Line) -> Optional[float]:
    """The line's recorded last trade (``live.price``), or None."""
    live = line.entry.live
    if live is None or live.get("error") is not None:
        return None
    return _positive(live.get("price"))


def veto(signal: Optional[LLMSignal], price: Optional[float], sma: Optional[float]) -> Optional[LLMSignal]:
    """A's rule on one momentum signal: kept on its side of the average, else NEUTRAL (13.2).

    No price or no average: the signal is kept as it is (counted by ``veto_counters``).
    Strict: a price equal to the average is NEUTRAL.
    """
    if signal is None or signal.bias is Bias.NEUTRAL or price is None or sma is None:
        return signal
    kept = price > sma if signal.bias is Bias.BULLISH else price < sma
    if kept:
        return signal
    return LLMSignal(ticker=signal.ticker, bias=Bias.NEUTRAL, conviction=0.0,
                     rationale=f"{VETO}: live {price:.4g} on the wrong side of the {VETO_SMA}-day average {sma:.4g}")


def veto_signal(long_bars: Bars) -> SignalFor:
    """A's signal maker, for a fund: the momentum rule, then the veto."""
    momentum = rule_signal("momentum")

    def signal(line: Line) -> Optional[LLMSignal]:
        return veto(momentum(line), live_price(line), sma_before(long_bars, line.ticker, line.day))

    return signal


def _counted(signal: Optional[LLMSignal]) -> bool:
    """A signal the funds would dispatch: a side, at or above the conviction floor."""
    return signal is not None and signal.bias is not Bias.NEUTRAL and signal.conviction >= cfg.MIN_CONVICTION


def veto_counters(cycles: Mapping[date, Sequence[Line]], long_bars: Bars, first: date) -> dict:
    """A's counter: momentum's signals from ``first``, and how many the veto turns NEUTRAL."""
    momentum = rule_signal("momentum")
    tally: Counter = Counter()
    for day, lines in cycles.items():
        if day < first:
            continue
        for line in lines:
            signal = momentum(line)
            if not _counted(signal):
                continue
            tally["signals"] += 1
            price, sma = live_price(line), sma_before(long_bars, line.ticker, line.day)
            if price is None:
                tally["no_live_price"] += 1
            if sma is None:
                tally["no_average"] += 1
            if veto(signal, price, sma).bias is Bias.NEUTRAL:
                tally["vetoed"] += 1
    n = tally["signals"]
    return {"from": first.isoformat(), "signals": n, "vetoed": tally["vetoed"],
            "vetoed_share": tally["vetoed"] / n if n else None,
            "under_ten_percent": (tally["vetoed"] / n < 0.10) if n else None,
            "no_live_price": tally["no_live_price"], "no_average": tally["no_average"]}


# --------------------------------------------------------------------------- #
# B: 10-month timing on VT
# --------------------------------------------------------------------------- #


def last_trading_day(year: int, month: int) -> date:
    day = date(year + (month == 12), month % 12 + 1, 1) - timedelta(days=1)
    while not is_trading_day(day):
        day -= timedelta(days=1)
    return day


def month_end_close(bars: Bars, ticker: str, year: int, month: int) -> tuple[Optional[float], bool]:
    """The close on the month's last trading day, or the last close before it in the month (True: fallen back)."""
    end = last_trading_day(year, month)
    frame = bars.history(ticker, end)
    if frame.empty:
        return None, True
    frame = frame[frame.index >= f"{year:04d}-{month:02d}-01"]
    if frame.empty:
        return None, True
    return float(frame["Close"].iloc[-1]), frame.index[-1].date() != end


def _months_back(year: int, month: int, n: int) -> list[tuple[int, int]]:
    out = []
    for k in range(n):
        m = month - k
        y = year + (m - 1) // 12
        out.append((y, (m - 1) % 12 + 1))
    return out


def timing_signals(bars: Bars, through: date, first: date = TIMING_FIRST_MONTH_END) -> list[dict]:
    """Every month-end decision from ``first`` to ``through``: the day, VT's close, its average, and the fund to hold."""
    out = []
    year, month = first.year, first.month
    while True:
        end = last_trading_day(year, month)
        if end > through:
            break
        close, fell_back = month_end_close(bars, TIMING_IN, year, month)
        closes = [month_end_close(bars, TIMING_IN, y, m)[0] for y, m in _months_back(year, month, TIMING_MONTHS)]
        average = (sum(closes) / TIMING_MONTHS) if close is not None and all(c is not None for c in closes) else None
        hold = None if average is None else (TIMING_IN if close > average else TIMING_OUT)
        out.append({"day": end.isoformat(), "close": close, "average": average, "hold": hold,
                    "fell_back": fell_back})
        year, month = (year + 1, 1) if month == 12 else (year, month + 1)
    return out


def timing_counters(bars: Bars, through: date) -> dict:
    """B's counter: switches so far, the current state, and the last month-end signal."""
    signals = [s for s in timing_signals(bars, through) if s["hold"] is not None]
    held = [s["hold"] for s in signals]
    switches = sum(1 for a, b in zip(held, held[1:]) if a != b)
    # What counts as B acting differently from the VT fund (13.7): trading
    # days, from its first session through ``through``, meant to be out of VT.
    decided = [(date.fromisoformat(s["day"]), s["hold"]) for s in signals]
    out_days, d = 0, (decided[0][0] + timedelta(days=1)) if decided else through
    while decided and d <= through:
        if is_trading_day(d) and [h for day, h in decided if day < d][-1] == TIMING_OUT:
            out_days += 1
        d += timedelta(days=1)
    return {"signals": len(signals), "switches": switches, "state": held[-1] if held else None,
            "days_out_of_vt": out_days,
            "last_signal": signals[-1]["day"] if signals else None,
            "month_ends_fallen_back": sum(1 for s in timing_signals(bars, through) if s["fell_back"])}


class TimingFund:
    """B: all of the fund in VT or in BIL, switched at the open after a month-end decision.

    Outside the engine, like the VT fund: no stop and no position manager.
    Each leg trades at the first open where its fund has a bar, 0.10% of
    notional per side; in between, the money is cash at 0%. Dividends are
    credited on the ex-date for the shares held at the previous close. The
    fund's days start at the first session after its first decision.
    """

    def __init__(self, name: str, bars: Bars, through: date, *, cash: float = STARTING_CASH,
                 cost_per_side: float = DEFAULT_COST_PER_SIDE) -> None:
        self.name = name
        self.bars = bars
        self.cash = cash
        self.cost = cost_per_side
        self.holding: Optional[str] = None
        self.qty = 0
        self.decisions = [(date.fromisoformat(s["day"]), s["hold"]) for s in timing_signals(bars, through)
                          if s["hold"] is not None]
        self.days: list[Day] = []
        self.tally = Tally()
        self.switches = 0
        self.waited = 0
        self._last_close: dict[str, float] = {}
        #: Every leg, for the after-tax view (``shadow.after_tax``): (day,
        #: ticker, "buy"/"sell", shares, the open, the fee). And every
        #: dividend credited: (day, ticker, shares, per share).
        self.trades: list[tuple[date, str, str, int, float, float]] = []
        self.dividends: list[tuple[date, str, int, float]] = []

    def target(self, day: date) -> Optional[str]:
        """The fund to hold at ``day``'s open: the latest decision made on a day before it."""
        chosen = None
        for decided, hold in self.decisions:
            if decided < day:
                chosen = hold
        return chosen

    def session(self, day: date, cycle: Optional[Sequence[Line]] = None) -> Optional[Day]:
        target = self.target(day)
        if target is None:
            return None                          # before the first decision: not started
        held_at_open = (self.holding, self.qty)
        bars = {t: self.bars.bar(t, day) for t in (TIMING_IN, TIMING_OUT)}
        if self.holding is not None and self.holding != target:
            bar = bars[self.holding]
            if bar is None:
                self.waited += 1
            else:
                self.cash += self.qty * bar[0] * (1 - self.cost)
                self.trades.append((day, self.holding, "sell", self.qty, bar[0], self.qty * bar[0] * self.cost))
                self.holding, self.qty = None, 0
                self.switches += 1
        if self.holding is None:
            bar = bars[target]
            if bar is None:
                self.waited += 1
            else:
                self.qty = math.floor(self.cash / (bar[0] * (1 + self.cost)))
                self.cash -= self.qty * bar[0] * (1 + self.cost)
                self.holding = target
                self.tally.accepted += 1
                if self.qty:
                    self.trades.append((day, target, "buy", self.qty, bar[0], self.qty * bar[0] * self.cost))
        before, before_qty = held_at_open
        if before is not None and bars[before] is not None and bars[before][4]:
            self.cash += before_qty * bars[before][4]
            if before_qty:
                self.dividends.append((day, before, before_qty, bars[before][4]))
        for ticker, bar in bars.items():
            if bar is not None:
                self._last_close[ticker] = bar[3]
        mark = self._last_close.get(self.holding, 0.0) if self.holding else 0.0
        record = Day(day, self.cash + self.qty * mark, self.cash, self.qty * mark, 1 if self.qty else 0)
        self.days.append(record)
        return record


# --------------------------------------------------------------------------- #
# C: pullback limit entry
# --------------------------------------------------------------------------- #


def limit_price(line: Line, side: Bias) -> tuple[Optional[float], Optional[str]]:
    """C's limit for one line, or why there is none: signal price -/+ 0.5 x the line's ATR14 (13.4)."""
    technicals = line.entry.technicals or {}
    price = live_price(line)
    fallback = price is None
    if price is None:
        price = _positive(technicals.get("last_close"))
    atr = _positive(technicals.get("atr14"))
    if price is None or atr is None:
        return None, "no price or ATR"
    limit = price - PULLBACK_ATRS * atr if side is Bias.BULLISH else price + PULLBACK_ATRS * atr
    if limit <= 0:
        return None, "no price or ATR"
    return limit, ("technicals price" if fallback else None)


def touches(side: Bias, limit: float, bar: tuple) -> Optional[tuple[float, str]]:
    """The fill a bar gives a limit: at the open if it opens at or past it, else at the limit if the range reaches it."""
    opened, high, low = bar[0], bar[1], bar[2]
    if side is Bias.BULLISH:
        if opened <= limit:
            return opened, "open"
        return (limit, "range") if low <= limit else None
    if opened >= limit:
        return opened, "open"
    return (limit, "range") if high >= limit else None


def sessions_after(day: date, n: int) -> list[date]:
    """The first ``n`` trading days after ``day`` (a day with no bar for a name is still one of them)."""
    out, d = [], day
    while len(out) < n:
        d += timedelta(days=1)
        if is_trading_day(d):
            out.append(d)
    return out


def pullback_counters(cycles: Mapping[date, Sequence[Line]], bars: Bars, first: date, through: date) -> dict:
    """C's counters: for every momentum signal from ``first``, would its limit fill within 3 sessions?"""
    momentum = rule_signal("momentum")
    tally: Counter = Counter()
    for day, lines in cycles.items():
        if day < first:
            continue
        for line in lines:
            signal = momentum(line)
            if not _counted(signal):
                continue
            limit, why = limit_price(line, signal.bias)
            if limit is None:
                tally["no_limit"] += 1
                continue
            tally["technicals_price"] += why == "technicals price"
            window = sessions_after(day, PULLBACK_SESSIONS)
            filled = None
            for session in window:
                if session > through:
                    break
                bar = bars.bar(line.ticker, session)
                if bar is not None:
                    filled = touches(signal.bias, limit, bar)
                    if filled:
                        break
            if filled:
                tally["filled"] += 1
            elif window[-1] <= through:
                tally["missed"] += 1
            else:
                tally["open"] += 1
    done = tally["filled"] + tally["missed"]
    return {"from": first.isoformat(), "filled": tally["filled"], "missed": tally["missed"],
            "still_open": tally["open"], "fill_rate": tally["filled"] / done if done else None,
            "no_limit": tally["no_limit"], "technicals_price": tally["technicals_price"]}


@dataclass
class _Order:
    line: Line
    signal: LLMSignal
    limit: float
    sessions: list[date]


@dataclass
class PullbackStats:
    placed: int = 0
    filled_open: int = 0
    filled_range: int = 0
    missed: int = 0
    no_room: int = 0
    ignored_pending: int = 0
    no_limit: int = 0
    technicals_price: int = 0
    #: Signals C considered but could not order because its own book held the name.
    skipped_held: int = 0
    #: Every momentum signal C considered: (ticker, the signal's day).
    considered: list = field(default_factory=list)
    #: Every fill: (ticker, the signal's day, the fill's day, the fill price).
    filled: list = field(default_factory=list)


class PullbackFund(Fund):
    """C: the momentum fund's machinery, entering by limit order instead of at the open (13.4).

    A session: stops gapped through fill at the open; the position manager
    runs; the cycle's new orders are placed (a held name, or one with an
    order standing, gets none); orders the open fills are executed, in the
    order they were placed; stops touched during the session; then orders
    the day's range fills, whose new positions' stops are first checked at
    the next open. The engine sizes and checks each entry at its fill price
    (``RecordedQuote``); a refusal drops the order. An order not filled in
    its 3 sessions is cancelled.
    """

    def __init__(self, name: str, feed, bars: Bars, **kwargs) -> None:
        super().__init__(name, rule_signal("momentum"), feed, bars, entry=PULLBACK, **kwargs)
        self.orders: list[_Order] = []
        self.pullback = PullbackStats()

    def session(self, day: date, cycle: Optional[Sequence[Line]], manage: bool = True,
                today: Optional[Sequence[Line]] = None) -> Day:
        broker = self.broker
        broker.day = day
        held_at_open = broker.held_quantities()
        opens, lows, highs, closes, dividends = {}, {}, {}, {}, {}

        def read(tickers) -> None:
            for ticker in sorted(tickers):
                if ticker in closes:
                    continue
                bar = self.bars.bar(ticker, day)
                if bar is not None:
                    opens[ticker], highs[ticker], lows[ticker], closes[ticker], dividends[ticker] = bar

        read(set(held_at_open) | {o.line.ticker for o in self.orders} | {line.ticker for line in cycle or ()})
        broker.fill_gapped_stops(opens)
        if cycle is not None:
            if manage:
                self._manage()
            self._place(cycle, day)
        read({o.line.ticker for o in self.orders})
        self._fill(day, at_open=True)
        read(broker.positions)
        broker.fill_touched_stops(lows, highs)
        self._fill(day, at_open=False)
        read(broker.positions)
        self._expire(day)
        broker.pay_dividends({t: d for t, d in dividends.items() if d}, held_at_open)
        broker.remember_marks(closes)
        record = Day(day, broker.equity(closes), broker.cash, broker.gross(closes), len(broker.positions))
        self.days.append(record)
        return record

    def _place(self, cycle: Sequence[Line], day: date) -> None:
        standing = {o.line.ticker for o in self.orders}
        for line in cycle:
            signal = self.signal_for(line)
            if not _counted(signal):
                continue
            self.pullback.considered.append((line.ticker, line.day))
            if line.ticker in self.broker.positions:
                self.pullback.skipped_held += 1
                continue
            if line.ticker in standing:
                self.pullback.ignored_pending += 1
                continue
            limit, why = limit_price(line, signal.bias)
            if limit is None:
                self.pullback.no_limit += 1
                continue
            self.pullback.technicals_price += why == "technicals price"
            self.orders.append(_Order(line, signal, limit, sessions_after(line.day, PULLBACK_SESSIONS)))
            standing.add(line.ticker)
            self.pullback.placed += 1

    def _fill(self, day: date, at_open: bool) -> None:
        left = []
        for order in self.orders:
            bar = self.bars.bar(order.line.ticker, day) if day in order.sessions else None
            fill = touches(order.signal.bias, order.limit, bar) if bar is not None else None
            if fill is None or (fill[1] == "open") != at_open:
                left.append(order)
                continue
            if order.line.ticker in self.broker.positions:
                self.pullback.no_room += 1
                continue
            self.broker.not_shortable = refused_by(self.refused_on, order.line.day)
            self.quotes.price[order.line.ticker] = fill[0]
            try:
                result, _ = self._execute(order.signal)
            finally:
                self.quotes.price.clear()
            if result.status is ExecutionStatus.ACCEPTED:
                self.tally.accepted += 1
                if at_open:
                    self.pullback.filled_open += 1
                else:
                    self.pullback.filled_range += 1
                self.pullback.filled.append((order.line.ticker, order.line.day, day, fill[0]))
            else:
                self.tally.rejected += 1
                self.pullback.no_room += 1
                if result.status is ExecutionStatus.ERROR and result.reason.startswith("unexpected"):
                    self.tally.errors += 1
                    self.tally.unexpected.append(f"{order.line.ticker}: {result.reason}")
        self.orders = left

    def _expire(self, day: date) -> None:
        left = []
        for order in self.orders:
            if order.sessions[-1] <= day:
                self.pullback.missed += 1
            else:
                left.append(order)
        self.orders = left


# --------------------------------------------------------------------------- #
# The race side, read at a checkpoint only (13.2, 13.4, 13.5)
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class RaceSettings:
    """The race's own arithmetic (``analysis/horse_race.py``'s defaults)."""

    floor: float
    horizon: int
    entry_rule: str
    today: date
    source: object
    fetcher: object
    equity: float
    stop_multiplier: float
    max_position_pct: float
    cost_per_side: float


def race_settings(today: date, final_through: date, lines) -> RaceSettings:
    """Fresh price sources, warmed over the lines as the race warms its own."""
    from analysis import horse_race as hr
    from analysis.baseline_compare import OhlcFetcher
    from analysis.returns import YFinancePriceSource

    source, fetcher = YFinancePriceSource(final_through=final_through), OhlcFetcher(final_through=final_through)
    hr.prewarm(lines, source, fetcher, hr.DEFAULT_HORIZON, today)
    return RaceSettings(cfg.MIN_CONVICTION, hr.DEFAULT_HORIZON, hr.ENTRY_AUTO, today, source, fetcher,
                        100_000.0, cfg.ATR_STOP_MULTIPLIER, cfg.MAX_POSITION_PCT, hr.DEFAULT_COST_PER_SIDE)


def arm_trades(name: str, entries, how: RaceSettings) -> list:
    """An arm's scored trades on its entries, exactly as ``horse_race.race_arm`` scores them."""
    from analysis.baseline_compare import simulate_model_trades
    from analysis.horse_race import scored_trades
    from analysis.scoring import score_entries

    above = [e for e in entries if e.is_directional and (e.conviction or 0.0) >= how.floor]
    scored, _ = score_entries(above, how.source, how.horizon, how.entry_rule, how.today)
    trades, matched, _ = simulate_model_trades(
        scored, equity=how.equity, horizon_days=how.horizon, stop_multiplier=how.stop_multiplier,
        max_position_pct=how.max_position_pct, fetcher=how.fetcher)
    return scored_trades(name, matched, trades, how.cost_per_side)


def veto_entries(momentum_entries, long_bars: Bars) -> list:
    """Momentum's entries with A's veto applied: a vetoed line becomes NEUTRAL."""
    from dataclasses import replace

    out = []
    for e in momentum_entries:
        if e.is_directional:
            live = e.live or {}
            price = None if live.get("error") is not None else _positive(live.get("price"))
            day = e.timestamp.date()
            kept = veto(LLMSignal(ticker=e.ticker, bias=Bias(e.bias), conviction=float(e.conviction),
                                  rationale="momentum"), price, sma_before(long_bars, e.ticker, day))
            if kept.bias is Bias.NEUTRAL:
                e = replace(e, bias="NEUTRAL", conviction=0.0)
        out.append(e)
    return out


def _test(diffs: Sequence[float], lag: int) -> dict:
    from analysis.horse_race import newey_west_t
    from analysis.multiple_tests import p_two_sided, series_stats

    t = newey_west_t(list(diffs), lag)
    return {"days": len(diffs), "mean_daily_diff": (sum(diffs) / len(diffs)) if diffs else None,
            "t": t, "p": p_two_sided(t), "stats": series_stats(diffs)}


def race_tests(lines, long_bars: Bars, how: RaceSettings, first: date, window_start: date) -> dict:
    """A's race arm against momentum (13.2), the insider arm's test (13.5), and C's filled against missed (13.4)."""
    import statistics

    from analysis.horse_race import daily_net, entries_for_arm, on_grid

    utc = lambda e: e.timestamp.date()  # noqa: E731 - lines carry UTC timestamps
    from_first = [e for e in lines if utc(e) >= first]
    momentum_entries = entries_for_arm("momentum", from_first)
    momentum = arm_trades("momentum", momentum_entries, how)
    vetoed = arm_trades(VETO, veto_entries(momentum_entries, long_bars), how)
    grid = sorted(set(daily_net(momentum)) | set(daily_net(vetoed)))
    a = [x - y for x, y in zip(on_grid(daily_net(vetoed), grid), on_grid(daily_net(momentum), grid))]
    out = {VETO: _test(a, how.horizon) | {"trades": len(vetoed), "momentum_trades": len(momentum)}}

    window = [e for e in lines if utc(e) >= window_start]
    insider = arm_trades("insiders", entries_for_arm("insiders", window), how)
    rule = {(t.ticker, t.signal_at): t.net for t in arm_trades("momentum", entries_for_arm("momentum", window), how)}
    per_day: dict[date, list[float]] = {}
    for trade in insider:
        per_day.setdefault(trade.entry_day, []).append(trade.net - rule.get((trade.ticker, trade.signal_at), 0.0))
    out["insiders"] = _test([statistics.fmean(v) for _, v in sorted(per_day.items())], how.horizon) | {
        "trades": len(insider)}

    net = {(t.ticker, t.signal_at): t.net for t in momentum}
    groups: dict[str, list[float]] = {"filled": [], "missed": []}
    for e in momentum_entries:
        if not (e.is_directional and (e.conviction or 0.0) >= how.floor) or e.held:
            continue
        key = (e.ticker, e.timestamp)
        limit, _ = limit_price(Line(e.ticker, utc(e), 1, e), Bias(e.bias))
        if limit is None or key not in net:
            continue
        window_days = sessions_after(utc(e), PULLBACK_SESSIONS)
        if window_days[-1] > how.today:
            continue
        hit = any(touches(Bias(e.bias), limit, bar) for bar in
                  (long_bars.bar(e.ticker, d) for d in window_days) if bar is not None)
        groups["filled" if hit else "missed"].append(net[key])
    out["pullback_filled_vs_missed"] = _filled_vs_missed(groups)
    return out


def _filled_vs_missed(groups: dict[str, list[float]]) -> dict:
    """Number, mean net return and hit rate of each group, and missed minus filled with a Welch t (for reading)."""
    import statistics

    out = {}
    for name, values in groups.items():
        out[name] = {"n": len(values), "mean_net": statistics.fmean(values) if values else None,
                     "hit_rate": (sum(1 for v in values if v > 0) / len(values)) if values else None}
    f, m = groups["filled"], groups["missed"]
    welch = None
    if len(f) >= 2 and len(m) >= 2:
        se = math.sqrt(statistics.variance(f) / len(f) + statistics.variance(m) / len(m))
        welch = (statistics.fmean(m) - statistics.fmean(f)) / se if se > 0 else None
    out["missed_minus_filled"] = (statistics.fmean(m) - statistics.fmean(f)) if f and m else None
    out["welch_t"] = welch
    return out


__all__ = [
    "COMPARED_WITH", "LIMIT", "NEW_FUNDS", "PullbackFund", "RaceSettings", "TIMING", "TimingFund", "VETO",
    "arm_trades", "limit_price", "race_settings", "race_tests",
    "pullback_counters", "sma_before", "timing_counters", "timing_signals", "touches", "veto", "veto_counters",
    "veto_signal",
]
