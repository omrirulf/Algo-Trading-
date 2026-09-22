"""Re-simulate the trades the model actually took through the real risk
engine, and set the result beside two baselines that involve no model call
at all.

    python analysis/baseline_compare.py
    python analysis/baseline_compare.py --horizon 5 --equity 50000

score_journal.py's hit rate is close-to-close and blind to the stop: a
"hit" there is "the market moved the right way at all over the window", not
"the trade made money" -- no stop-loss, no gap risk, no position sizing.
This asks the harder question with the code that actually trades,
``backtest.simulate.simulate_trade``, applied at each signal's own
timestamp so nothing here can see a move the live system could not have.

Two baselines sit beside it, both requiring no model and no stop, so any gap
between them and the model's own trades is something the model's direction
call and risk management would have to explain:

* **same tickers, same windows, always long, no stop** -- score_journal.py
  already computed this for every signal (``ScoredSignal.raw_return``), so
  it costs no extra fetch. It isolates whether the SHORT calls and the stop
  exits add anything over just holding the names the model looked at.
* **buy-and-hold of the whole watchlist, and of SPY**, over the calendar
  span the acted-on signals cover -- the "did nothing clever" comparison,
  a single static return rather than a per-trade one.

This is not a portfolio equity curve. It does not model overlapping
positions, cash constraints, or compounding -- see LIMITS in the report for
why that is a bigger, more assumption-laden build than this one, and why a
per-trade comparison is the honest scope for what a still-small sample can
support.

Read-only, like score_journal.py: it reads the journal, fetches price
history, and prints.
"""

from __future__ import annotations

import argparse
import logging
import statistics
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Optional, Sequence

# Allow ``python analysis/baseline_compare.py`` from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd  # noqa: E402

from analysis.metrics import ScoredSignal  # noqa: E402
from analysis.reader import read_journal  # noqa: E402
from analysis.returns import (  # noqa: E402
    ENTRY_AUTO,
    ENTRY_RULES,
    YFinancePriceSource,
    last_final_session,
)
from analysis.scoring import build_run  # noqa: E402
from backtest.simulate import Trade, simulate_trade  # noqa: E402
from backtest.sweep import MIN_TRADES, Outcome  # noqa: E402
from config import settings as cfg  # noqa: E402
from config.watchlist import DEFAULT_WATCHLIST  # noqa: E402

DEFAULT_HORIZON = 3

#: Calendar days of history fetched before the earliest signal for a ticker,
#: so ATR has MIN_WARMUP_BARS of daily bars to smooth over even across a
#: long weekend or a run of holidays.
LEAD_DAYS = 40

log = logging.getLogger("baseline_compare")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="baseline_compare",
        description="Re-simulate acted-on signals through the risk engine and compare to two baselines.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH,
        help="path to the signal journal (default: %(default)s)",
    )
    parser.add_argument(
        "--horizon", type=int, default=DEFAULT_HORIZON,
        help="trading sessions held after entry (default: %(default)s)",
    )
    parser.add_argument(
        "--entry", choices=ENTRY_RULES, default=ENTRY_AUTO,
        help="which close resolves the underlying signal as scored (default: %(default)s)",
    )
    parser.add_argument(
        "--floor", type=float, default=cfg.MIN_CONVICTION,
        help="conviction floor: only signals at or above this were acted on (default: %(default)s)",
    )
    parser.add_argument("--equity", type=float, default=100_000.0)
    parser.add_argument("--stop-multiplier", type=float, default=cfg.ATR_STOP_MULTIPLIER)
    parser.add_argument("--max-position-pct", type=float, default=cfg.MAX_POSITION_PCT)
    parser.add_argument("-v", "--verbose", action="store_true", help="log fetch failures")
    return parser


class OhlcFetcher:
    """Daily OHLC bars per ticker, fetched once and cached.

    ``simulate_trade`` needs High/Low to catch an intraday stop and Open to
    price a gap -- the daily closes ``YFinancePriceSource`` keeps are not
    enough for that, which is why this exists alongside it rather than
    reusing it.

    ``final_through`` is the last date whose bar is a final close (see
    ``analysis.returns.last_final_session``). Later bars are dropped before
    caching, for the same reason the closes source drops them: a stop
    checked against today's High/Low at 14:30 is checked against half a day.
    """

    def __init__(self, final_through: Optional[date] = None) -> None:
        self._cache: dict[str, pd.DataFrame] = {}
        self.final_through = final_through

    def ohlc(self, ticker: str, start: date, end: date) -> pd.DataFrame:
        cached = self._cache.get(ticker)
        if cached is not None:
            return cached
        frame = self.final_only(self._fetch(ticker, start, end))
        self._cache[ticker] = frame
        return frame

    def final_only(self, frame: pd.DataFrame) -> pd.DataFrame:
        """``frame`` without any bar dated after ``final_through``."""
        if self.final_through is None or frame.empty:
            return frame
        return frame[[_as_date(ts) <= self.final_through for ts in frame.index]]

    def _fetch(self, ticker: str, start: date, end: date) -> pd.DataFrame:
        try:
            import yfinance as yf
        except ImportError as exc:  # pragma: no cover - dependency is pinned
            log.error("yfinance unavailable: %s", exc)
            return pd.DataFrame()
        try:
            frame = yf.Ticker(ticker).history(
                start=(start - timedelta(days=LEAD_DAYS)).isoformat(),
                # yfinance treats ``end`` as exclusive.
                end=(end + timedelta(days=1)).isoformat(),
                interval="1d",
                auto_adjust=False,
            )
        except Exception as exc:  # noqa: BLE001 - a missing series is a status, not a crash
            log.warning("OHLC unavailable for %s: %s", ticker, exc)
            return pd.DataFrame()
        required = ("Open", "High", "Low", "Close")
        if frame is None or frame.empty or any(c not in frame.columns for c in required):
            log.warning("no OHLC history returned for %s", ticker)
            return pd.DataFrame()
        return frame.dropna(subset=list(required))


def _as_date(value: object) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    return pd.Timestamp(value).date()


def _signal_index(ohlc: pd.DataFrame, signal_date: date) -> Optional[int]:
    """Index of the last bar at or before ``signal_date``.

    ``simulate_trade`` enters on the *next* bar's open after this index --
    always, regardless of whether the signal fired before or after that
    day's close. That is a simplification against score_journal.py's
    'auto'/'same'/'next' entry rules (see returns.py), taken deliberately
    rather than accidentally: it is the same next-open convention
    run_backtest.py already uses, it needs no look-ahead reasoning about
    when in the day the model ran, and where it differs from 'auto' it is
    the conservative direction -- a signal timestamped before the close is
    compared with one session less of edge than score_journal.py would
    give it, never one more.
    """
    at_or_before = [i for i, ts in enumerate(ohlc.index) if _as_date(ts) <= signal_date]
    return at_or_before[-1] if at_or_before else None


def _horizon_complete(ohlc: pd.DataFrame, signal_index: int, horizon_days: int) -> bool:
    """True when every bar of the holding period is in the frame.

    ``simulate_trade`` exits on the last bar it has when the horizon runs
    past the end of the frame, which is right for a backtest over a fixed
    history and wrong here: a trade opened two sessions ago is not a
    resolved three-session trade, and scoring it as one lets the answer
    change with the clock. The closes side already calls such a signal
    pending; this keeps the OHLC side from disagreeing with it.
    """
    return signal_index + horizon_days <= len(ohlc) - 1


def simulate_model_trades(
    signals: Sequence[ScoredSignal],
    equity: float,
    horizon_days: int,
    stop_multiplier: float,
    max_position_pct: float,
    fetcher: OhlcFetcher,
) -> tuple[list[Trade], list[ScoredSignal], int]:
    """Re-simulate each acted-on signal through the real stop/gap arithmetic.

    Returns ``(trades, matched, could_not_simulate)``. ``matched`` is the
    subset of ``signals`` each trade in ``trades`` came from, same order --
    the caller needs it to compare the model's trades against a baseline
    over the *same* population, not the fuller one that includes signals a
    warm-up, cap, or gap reason dropped from this side only (see
    ``simulate_trade``'s own docstring for why that return is ``None`` and
    not an error). Comparing against the fuller population would make any
    gap partly a sampling artifact rather than a real one.
    """
    trades: list[Trade] = []
    matched: list[ScoredSignal] = []
    dropped = 0

    by_ticker: dict[str, list[ScoredSignal]] = {}
    for signal in signals:
        by_ticker.setdefault(signal.entry.ticker, []).append(signal)

    for ticker, group in sorted(by_ticker.items()):
        dates = [s.entry.timestamp.date() for s in group]
        window_end = max(dates) + timedelta(days=horizon_days * 2 + 10)
        ohlc = fetcher.ohlc(ticker, min(dates), window_end)
        if ohlc.empty:
            dropped += len(group)
            continue
        for signal in group:
            index = _signal_index(ohlc, signal.entry.timestamp.date())
            if index is None or not _horizon_complete(ohlc, index, horizon_days):
                dropped += 1
                continue
            side = "buy" if signal.entry.direction > 0 else "sell"
            trade = simulate_trade(
                ohlc, index, side=side, equity=equity, horizon_days=horizon_days,
                stop_multiplier=stop_multiplier, max_position_pct=max_position_pct,
            )
            if trade is None:
                dropped += 1
                continue
            trades.append(trade)
            matched.append(signal)

    return trades, matched, dropped


def watchlist_buy_and_hold(
    tickers: Sequence[str], start: date, end: date, source: YFinancePriceSource,
) -> tuple[Optional[float], int, int]:
    """Equal-weight buy-and-hold return of ``tickers`` from ``start`` to ``end``.

    Returns ``(mean_return, priced, missing)``. A ticker with no bar at or
    before ``start`` or at or after ``end`` is left out and counted, rather
    than treated as a 0% return it never had.
    """
    per_ticker: list[float] = []
    missing = 0
    for ticker in tickers:
        series = source.closes(ticker, start, end)
        entry = next((price for bar_date, price in series.bars if bar_date >= start), None)
        exit_ = next((price for bar_date, price in reversed(series.bars) if bar_date <= end), None)
        if entry is None or exit_ is None or entry <= 0:
            missing += 1
            continue
        per_ticker.append(exit_ / entry - 1.0)
    mean = statistics.fmean(per_ticker) if per_ticker else None
    return mean, len(per_ticker), missing


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.ERROR,
        format="%(levelname)s %(name)s: %(message)s",
    )

    if args.horizon < 1:
        print("--horizon must be at least 1 session", file=sys.stderr)
        return 2

    try:
        read = read_journal(args.journal)
    except FileNotFoundError as exc:
        print(
            f"{exc}\nThe orchestrator writes one entry per ticker per cycle; run it first.",
            file=sys.stderr,
        )
        return 1
    if not read.entries:
        print(f"{args.journal} has no usable entries.", file=sys.stderr)
        return 1

    final_through = last_final_session(datetime.now(timezone.utc))
    price_source = YFinancePriceSource(final_through=final_through)
    run = build_run(read=read, source=price_source, horizon=args.horizon,
                     floor=args.floor, entry_rule=args.entry)

    acted_on = [s for s in run.signals if s.conviction >= args.floor]
    if not acted_on:
        print(
            f"No signals have both a resolved outcome and conviction >= {args.floor} yet -- "
            "nothing to compare.",
            file=sys.stderr,
        )
        return 1

    trades, matched, could_not_simulate = simulate_model_trades(
        acted_on, equity=args.equity, horizon_days=args.horizon,
        stop_multiplier=args.stop_multiplier, max_position_pct=args.max_position_pct,
        fetcher=OhlcFetcher(),
    )
    model = Outcome(label="model signals, stop-aware", trades=trades)
    # Same population the model side actually produced a trade for -- not
    # the fuller ``acted_on``, which would make any gap partly about which
    # signals a warm-up/cap/gap check happened to drop.
    naive_returns = [s.raw_return for s in matched]

    window_start = min(s.forward.entry_date for s in acted_on)
    window_end = max(s.forward.exit_date for s in acted_on)
    # A fresh source: YFinancePriceSource caches by ticker only, ignoring the
    # window on a cache hit, and price_source above may already hold a
    # narrower per-ticker range from build_run. Reusing it here would risk
    # silently answering from a shorter window than the one asked for.
    basket_source = YFinancePriceSource(final_through=final_through)
    watchlist_return, watchlist_n, watchlist_missing = watchlist_buy_and_hold(
        DEFAULT_WATCHLIST, window_start, window_end, basket_source,
    )
    spy_return, spy_n, _ = watchlist_buy_and_hold(("SPY",), window_start, window_end, basket_source)

    print(render(
        run_horizon=args.horizon, floor=args.floor, model=model,
        could_not_simulate=could_not_simulate, naive_returns=naive_returns,
        window_start=window_start, window_end=window_end,
        watchlist_return=watchlist_return, watchlist_n=watchlist_n,
        watchlist_total=len(DEFAULT_WATCHLIST), watchlist_missing=watchlist_missing,
        spy_return=spy_return if spy_n else None,
    ))
    return 0


def render(
    *, run_horizon: int, floor: float, model: Outcome, could_not_simulate: int,
    naive_returns: list[float], window_start: date, window_end: date,
    watchlist_return: Optional[float], watchlist_n: int, watchlist_total: int,
    watchlist_missing: int, spy_return: Optional[float],
) -> str:
    total_signals = model.n + could_not_simulate
    naive_hit = (sum(1 for r in naive_returns if r > 0) / len(naive_returns)
                 if naive_returns else None)
    naive_median = statistics.median(naive_returns) if naive_returns else None
    naive_mean = statistics.fmean(naive_returns) if naive_returns else None

    lines = [
        "MODEL TRADES vs. TWO BASELINES THAT INVOLVE NO MODEL CALL",
        "=" * 78,
        f"horizon {run_horizon} session(s) | conviction floor {floor} | "
        f"window {window_start} to {window_end}",
        "",
        "Coverage",
        "--------",
        f"signals at or above the floor with a resolved outcome  {total_signals}",
        f"  re-simulated through the real stop/gap arithmetic    {model.n}",
        f"  could not be simulated (warm-up, cap, missing bars)  {could_not_simulate}"
        + ("" if could_not_simulate == 0 else "  <- excluded below, not counted as a hit or a miss"),
        "",
        "Per-trade return: the model's own trades vs. the same tickers and",
        "windows held long with no stop at all.",
        "",
        f"{'':<32}{'n':>5}{'hit rate':>11}{'median':>11}{'mean':>11}",
        _row("model signals, stop-aware", model.n, _rate(model.trades), model.median_return,
             _mean(model.trades)),
        "same tickers/windows, long,",
        _row("  no stop (naive)", len(naive_returns), naive_hit, naive_median, naive_mean),
    ]
    if model.n and model.n < MIN_TRADES:
        lines.append(f"  fewer than {MIN_TRADES} model trades -- arithmetic, not evidence")

    lines += [
        "",
        f"Of the model's stop-aware trades: stopped out "
        f"{_pct(model.stop_hit_rate)}, of those filled through a gap "
        f"{_pct(model.gap_rate)}.",
        "",
        f"Buy-and-hold, same window, no model and no stop:",
        f"  watchlist ({watchlist_n}/{watchlist_total} tickers priced"
        + (f", {watchlist_missing} missing" if watchlist_missing else "")
        + f")  {_pct(watchlist_return)}",
        f"  SPY                                             {_pct(spy_return)}",
        "",
        "LIMITS",
        "-" * 78,
        "This is per-trade, not a portfolio equity curve: it does not model",
        "overlapping positions, cash constraints, or compounding, so it cannot",
        "say what an account following every signal would actually be worth",
        "today. Building that means choosing a position-sizing and overlap",
        "policy, which would shape the answer as much as measure it -- this",
        "stays at the level score_journal.py already reports at.",
        "",
        "The watchlist and SPY rows are a single static return over the whole",
        "window, not a per-trade average, and are not risk-adjusted or",
        "cost-adjusted -- read them as 'did nothing clever', not as a fair",
        "trading strategy in their own right.",
        "",
        "Same small-sample caveat as everywhere else in this package: a",
        "handful of resolved trades is arithmetic, not evidence.",
    ]
    return "\n".join(lines)


def _row(label: str, n: Optional[int], hit: Optional[float], median: Optional[float],
         mean: Optional[float]) -> str:
    return f"{label:<32}{n:>5}{_pct(hit):>11}{_pct(median):>11}{_pct(mean):>11}"


def _rate(trades: list[Trade]) -> Optional[float]:
    if not trades:
        return None
    return sum(1 for t in trades if t.return_pct > 0) / len(trades)


def _mean(trades: list[Trade]) -> Optional[float]:
    if not trades:
        return None
    return statistics.fmean(t.return_pct for t in trades)


def _pct(value: Optional[float]) -> str:
    return "n/a" if value is None else f"{value * 100:+.1f}%"


if __name__ == "__main__":
    raise SystemExit(main())
