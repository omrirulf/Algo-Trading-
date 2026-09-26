#!/usr/bin/env python3
"""Run calibration and the four funds, and print what the dashboard reads.

    python -m shadow.run                      # the nightly job: JSON to stdout
    python -m shadow.run --processes 4        # the coin-flip funds on 4 cores
    python -m shadow.run --with-prices        # + prices_sha256, and the price table as a last line

Prints one JSON document (the "funds" contract in ``dashboard/funds.html``).
What it contains depends on ``shadow/schedule.py`` and nothing else:

* no calibration start set: calibration "not_started", the pass
  rule, the real account's holding times. No fund is run.
* calibration started: the calibration fund against the real account,
  day by day, with the trades that differ. Still no fund is run -- during
  calibration only the match is reported.
* fund start set: the four funds and the 1,000 coin-flip funds, from that
  day, through the last final close -- and, listed after the four, the two
  exploratory funds (``EXPLORATORY_FUNDS``), each compared with the model
  fund. Every fund but VT also says how its longs and its shorts did.

Reads the journal, the live audit log (read only), the account snapshots
and yfinance. Writes nothing: the workflow redirects stdout.
"""

from __future__ import annotations

import argparse
import json
import logging
import math
import re
import statistics
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Final, Iterable, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis import price_tape  # noqa: E402
from analysis.baseline_compare import OhlcFetcher  # noqa: E402
from analysis.reader import JournalEntry, read_journal  # noqa: E402
from analysis.returns import last_final_session  # noqa: E402
from config import settings as cfg  # noqa: E402
from shadow import schedule  # noqa: E402
from shadow.broker import ENTRY  # noqa: E402
from shadow.fund import (  # noqa: E402
    CONVICTION_FIRST,
    STARTING_CASH,
    Fund,
    IndexFund,
    coin_signal,
    cycle_days,
    lines_by_day,
    model_signal,
    rule_signal,
    run,
)
from shadow.market import Bars, SimFeed, calendar  # noqa: E402
from shadow.order_matters import fund_summary, real_summary  # noqa: E402

log = logging.getLogger("shadow.run")

INDEX_TICKER = "VT"
LABELS = {"model": "Model", "momentum": "Momentum", "hybrid": "Hybrid", "vt": "VT (world index, held)",
          "model_by_conviction": "Model, highest conviction first", "model_sized": "Model, sized by conviction"}

#: The owner's two exploratory funds (decisions 3 and 4 of 25 Sep 2026), in
#: the order they are listed, after the four. The model's own signals, each
#: with one thing changed: the buying order, then the size. Each is compared
#: with the model fund, never ranked with the four: it cannot change the
#: decision.
EXPLORATORY_FUNDS: Final[tuple[str, ...]] = ("model_by_conviction", "model_sized")
#: The fund an exploratory fund is compared with: same signals, one change.
COMPARE_TO: Final[str] = "model"
#: The lag of the Newey-West t on the daily difference from the model fund:
#: a week of sessions, as positions held for days make consecutive days'
#: differences correlated.
VS_MODEL_LAG: Final[int] = 5
#: Longs vs shorts (the owner's decision 6 of 25 Sep 2026): a side's mean
#: return and hit rate read "too few" until it has this many closed trades.
MIN_SIDE_TRADES: Final[int] = 20

#: The real broker's own refusals, as the live audit log records them. A
#: shadow fund is refused the same shorts; nothing else is inferred.
#: The broker quotes the ticker: 'asset "LQD" cannot be sold short'. The
#: quotes are optional here so a reworded message still reads.
_NOT_SHORTABLE = (
    re.compile(r"asset \\?\"?(\w[\w.\-]*)\\?\"? cannot be sold short", re.IGNORECASE),
    re.compile(r"hard-to-borrow asset \\?\"?(\w[\w.\-]*)", re.IGNORECASE),
)


def _now() -> datetime:
    return datetime.now(timezone.utc)


def not_shortable(audit_lines: Iterable[str]) -> frozenset[str]:
    """Tickers the paper account has refused to short, from its own audit log."""
    found: set[str] = set()
    for raw in audit_lines:
        if "short" not in raw and "borrow" not in raw:
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError:
            continue
        reason = str(((record.get("result") or {}).get("reason")) or "")
        for pattern in _NOT_SHORTABLE:
            match = pattern.search(reason)
            if match:
                found.add(match.group(1).upper())
    return frozenset(found)


# --------------------------------------------------------------------------- #
# Summaries
# --------------------------------------------------------------------------- #


def max_drawdown(equity: Sequence[float]) -> float:
    peak, worst = -math.inf, 0.0
    for value in equity:
        peak = max(peak, value)
        if peak > 0:
            worst = max(worst, 1.0 - value / peak)
    return worst


def total_return(fund) -> float:
    return fund.days[-1].equity / STARTING_CASH - 1.0 if fund.days else 0.0


def daily_returns(fund) -> list[float]:
    """Close to close, the first session from the starting cash.

    On the equity as printed, to the cent: two books that agree to the cent
    every day -- as the model fund and the "highest conviction first" fund
    do until the first cycle watchlist order runs out of room in -- then
    differ by exactly nothing, not by float noise a t statistic would divide
    by itself.
    """
    equity = [STARTING_CASH] + [round(d.equity, 2) for d in fund.days]
    return [today / before - 1.0 for before, today in zip(equity, equity[1:])]


def sides(closed: Sequence) -> dict:
    """Longs vs shorts over a fund's closed trades: a report, nothing more.

    A trade's net return is its pnl -- costs and dividends in -- over the
    notional it was opened at; a hit is a return above zero. Open positions
    are not counted: their return is not known yet. ``too_few`` until a side
    has ``MIN_SIDE_TRADES`` trades, and the page says so instead of a number.
    """
    out = {}
    for side, name in (("buy", "long"), ("sell", "short")):
        returns = [t.pnl / t.notional for t in closed if t.side == side and t.notional > 0]
        n = len(returns)
        out[name] = {
            "n": n,
            "mean_return": statistics.fmean(returns) if returns else None,
            "hit_rate": sum(1 for r in returns if r > 0) / n if n else None,
            "too_few": n < MIN_SIDE_TRADES,
        }
    return out


def vs_model(fund, model) -> dict:
    """An exploratory fund against the model fund: same signals, same days, one change.

    The difference is taken day by day, so a market that lifts both funds
    alike cancels, and its mean is judged by a Newey-West t (the race's own,
    ``analysis.horse_race.newey_west_t``), since the two books hold the same
    names for days at a time and consecutive differences are not independent.
    """
    from analysis.horse_race import newey_west_t

    diffs = [a - b for a, b in zip(daily_returns(fund), daily_returns(model))]
    equity, model_equity = [d.equity for d in fund.days], [d.equity for d in model.days]
    return {
        "total_return_diff": total_return(fund) - total_return(model),
        "max_drawdown": max_drawdown(equity),
        "model_max_drawdown": max_drawdown(model_equity),
        "mean_daily_diff": statistics.fmean(diffs) if diffs else None,
        "t": newey_west_t(diffs, VS_MODEL_LAG),
        "days": len(diffs),
    }


def summarise(fund, vt_return: Optional[float]) -> dict:
    equity = [d.equity for d in fund.days]
    total = total_return(fund)
    if isinstance(fund, IndexFund):
        trades, win_rate, open_positions, cash = 1 if fund.qty else 0, None, 1 if fund.qty else 0, fund.cash
    else:
        broker = fund.broker
        trades = sum(1 for f in broker.fills if f.kind == ENTRY)
        closed = broker.closed
        win_rate = (sum(1 for c in closed if c.pnl > 0) / len(closed)) if closed else None
        open_positions, cash = len(broker.positions), broker.cash
    return {
        "name": fund.name,
        "label": LABELS.get(fund.name, fund.name),
        "equity": [round(v, 2) for v in equity],
        "total_return": total,
        "vs_vt": None if vt_return is None or fund.name == "vt" else total - vt_return,
        "max_drawdown": max_drawdown(equity),
        "trades": trades,
        "win_rate": win_rate,
        "open_positions": open_positions,
        "cash": round(cash, 2),
        # How often the buying order mattered (the owner's report, 24 Sep
        # 2026): VT buys once and never meets a limit.
        "order_matters": None if isinstance(fund, IndexFund) else fund_summary(fund),
        # Longs vs shorts: VT holds one long and is not a signal's trade.
        "sides": None if isinstance(fund, IndexFund) else sides(fund.broker.closed),
        "exploratory": fund.name in EXPLORATORY_FUNDS,
    }


def summarise_exploratory(fund, model, vt_return: Optional[float]) -> dict:
    """An exploratory fund's row: every field a fund has, and how it compares with the model fund."""
    return summarise(fund, vt_return) | {"compare_to": COMPARE_TO, "vs_model": vs_model(fund, model)}


def exploratory_funds(feed: SimFeed, bars: Bars, shortable_no: frozenset[str]) -> list[Fund]:
    """The two exploratory funds: the model fund with one thing changed each.

    Same signals, feed, bars, costs, starting cash and short refusals as the
    model fund; everything else is the ``Fund`` defaults, which are
    production's. Simulation only.
    """
    return [
        Fund("model_by_conviction", model_signal, feed, bars, not_shortable=shortable_no,
             priority=CONVICTION_FIRST),
        Fund("model_sized", model_signal, feed, bars, not_shortable=shortable_no, sized_by_conviction=True),
    ]


def percentile(values: Sequence[float], p: float) -> Optional[float]:
    if not values:
        return None
    ordered = sorted(values)
    rank = (len(ordered) - 1) * p / 100.0
    lo, hi = math.floor(rank), math.ceil(rank)
    return ordered[lo] + (ordered[hi] - ordered[lo]) * (rank - lo)


def band(curves: Sequence[Sequence[float]]) -> dict:
    """5th and 95th percentile of the coin-flip funds' equity, session by session."""
    if not curves:
        return {"p5": [], "p95": [], "funds": 0}
    length = min(len(c) for c in curves)
    return {
        "p5": [round(percentile([c[i] for c in curves], 5.0), 2) for i in range(length)],
        "p95": [round(percentile([c[i] for c in curves], 95.0), 2) for i in range(length)],
        "funds": len(curves),
    }


def integrity(funds: Sequence) -> dict:
    """What would say the simulation itself went wrong, fund by fund.

    Apart from the problems: ``data_holes``, the ticker-days the price
    source had no bar for (see ``Tally.data_holes``). A gap in the data is
    reported, not counted against the machinery.
    """
    problems: list[str] = []
    for fund in funds:
        if isinstance(fund, IndexFund):
            continue
        problems += [f"{fund.name}: {u}" for u in fund.tally.unexpected]
        problems += [f"{fund.name}: manager: {e}" for e in fund.tally.manager_errors]
        if fund.tally.estimated_r:
            problems.append(f"{fund.name}: {fund.tally.estimated_r} action(s) with an estimated R")
        covered = {}
        for stop in fund.broker.live_stops():
            covered[stop.ticker] = covered.get(stop.ticker, 0) + stop.qty
        for ticker, pos in fund.broker.positions.items():
            if covered.get(ticker, 0) != abs(pos.qty):
                problems.append(f"{fund.name}: {ticker} stops cover {covered.get(ticker, 0)} of {abs(pos.qty)}")
    holes = [f"{fund.name}: {h}" for fund in funds if not isinstance(fund, IndexFund) for h in fund.tally.data_holes]
    return {"ok": not problems, "problems": problems[:50], "data_holes": len(holes), "data_hole_examples": holes[:10]}


# --------------------------------------------------------------------------- #
# The coin-flip funds, on several cores
# --------------------------------------------------------------------------- #

#: Set before the pool forks, so every worker reads the same bars without a copy.
_SHARED: dict = {}


def _coin_chunk(seeds: Sequence[int]) -> list[tuple[int, list[float], dict]]:
    shared = _SHARED
    feed = SimFeed(shared["bars"])
    funds = [Fund(f"coin-{seed}", coin_signal(seed), feed, shared["bars"],
                  not_shortable=shared["not_shortable"], order_detail=False) for seed in seeds]
    run(funds, shared["sessions"], shared["cycles"], shared["ran"], feed)
    return [(seed, [d.equity for d in fund.days], integrity([fund]) | {"order_days": fund_summary(fund)["days"]})
            for seed, fund in zip(seeds, funds)]


def coin_funds(count: int, processes: int, bars: Bars, sessions, cycles, ran, shortable_no) -> tuple[list[list[float]], dict]:
    _SHARED.update(bars=bars, sessions=sessions, cycles=cycles, ran=ran, not_shortable=shortable_no)
    seeds = list(range(count))
    chunks = [seeds[i::max(1, processes)] for i in range(max(1, processes))]
    if processes > 1:
        import multiprocessing

        with multiprocessing.get_context("fork").Pool(processes) as pool:
            results = [r for part in pool.map(_coin_chunk, chunks) for r in part]
    else:
        results = _coin_chunk(seeds)
    results.sort(key=lambda r: r[0])
    problems = [p for _, _, check in results for p in check["problems"]]
    holes = sum(check["data_holes"] for _, _, check in results)
    examples = [e for _, _, check in results for e in check["data_hole_examples"]][:10]
    order = sorted(check["order_days"] for _, _, check in results)
    return [curve for _, curve, _ in results], {"ok": not problems, "problems": problems[:50],
                                                "data_holes": holes, "data_hole_examples": examples,
                                                "order_days": {"median": percentile(order, 50.0),
                                                               "p5": percentile(order, 5.0),
                                                               "p95": percentile(order, 95.0)}}


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def _read_lines(path: Path) -> list[str]:
    try:
        return path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return []


def run_funds(
    entries: Sequence[JournalEntry], start: date, final_through: date, fetcher, *,
    random_funds: int, processes: int, shortable_no: frozenset[str],
) -> tuple[dict, dict]:
    cycles = lines_by_day(entries)
    ran = cycle_days(entries)
    tickers = {line.ticker for lines in cycles.values() for line in lines} | {INDEX_TICKER}
    bars = Bars.fetch(tickers, start, final_through, fetcher)
    sessions = calendar(bars, (INDEX_TICKER, "SPY", *sorted(tickers)), start, final_through)
    feed = SimFeed(bars)
    four = [
        Fund("model", model_signal, feed, bars, not_shortable=shortable_no),
        Fund("momentum", rule_signal("momentum"), feed, bars, not_shortable=shortable_no),
        Fund("hybrid", rule_signal("hybrid"), feed, bars, not_shortable=shortable_no),
        IndexFund("vt", INDEX_TICKER, bars),
    ]
    explore = exploratory_funds(feed, bars, shortable_no)
    # One run for all six: the same sessions, cycles and feed clock.
    run([*four, *explore], sessions, cycles, ran, feed)
    vt = four[-1].days[-1].equity / STARTING_CASH - 1.0 if four[-1].days else None
    curves, coin_check = coin_funds(random_funds, processes, bars, sessions, cycles, ran, shortable_no)
    # The key keeps its name; the check covers the exploratory funds too.
    check = integrity([*four, *explore])
    model = next(f for f in four if f.name == COMPARE_TO)
    return {
        "start": start.isoformat(),
        "days": [d.isoformat() for d in sessions],
        "list": [summarise(f, vt) for f in four] + [summarise_exploratory(f, model, vt) for f in explore],
        "band": band(curves),
    }, {"four": check, "coin": coin_check}


def build(args: argparse.Namespace, now: datetime, fetchers: Optional[list] = None) -> dict:
    """The funds document. ``fetchers``, when given, receives the price fetcher the run used,
    so ``main`` can hand over its prices without a second fetch (``--with-prices``)."""
    from shadow import calibration as calib

    final_through = last_final_session(now)
    read = read_journal(args.journal)
    audit_lines = _read_lines(args.audit)
    snapshots = calib.load_snapshots(_read_lines(args.account))
    shortable_no = not_shortable(audit_lines)
    fetcher = OhlcFetcher(final_through=final_through)
    if fetchers is not None:
        fetchers.append(fetcher)
    holding = calib.holding_days(audit_lines, read.entries, snapshots)

    calibration_start = schedule.CALIBRATION_START
    if calibration_start is None:
        calibration = calib.calibration_json(None, "not_started", None, None, holding)
    else:
        calibration = calib.calibration_report(
            snapshots=snapshots, entries=read.entries, audit_lines=audit_lines, start=calibration_start,
            final_through=final_through, fetcher=fetcher, not_shortable=shortable_no,
            days_needed=schedule.CALIBRATION_DAYS, holding=holding,
        )

    funds, checks = None, None
    fund_start = schedule.FUND_START
    passed = calibration.get("status") == "passed"
    if fund_start is not None and passed and fund_start <= final_through:
        funds, checks = run_funds(read.entries, fund_start, final_through, fetcher,
                                  random_funds=args.random, processes=args.processes,
                                  shortable_no=shortable_no)
    return {
        "generated_at": now.isoformat(),
        "final_through": final_through.isoformat(),
        "simulated": True,
        "calibration": calibration,
        "funds": funds,
        "fund_test": {
            "status": "running" if funds else "not_started",
            "start": fund_start.isoformat() if fund_start else None,
            "sessions": len(funds["days"]) if funds else 0,
            "independent": (len(funds["days"]) // 3) if funds else None,
            "next_checkpoint": None,
        },
        "integrity": checks,
        "not_shortable": sorted(shortable_no),
        # The real paper account's own record, always: it is the account,
        # not a fund result. The calibration fund's is in "calibration" and
        # each fund's in its own row, shown when those are.
        "order_matters": {"real": real_summary(audit_lines)},
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="shadow.run", description=__doc__.split("\n\n")[0])
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH)
    parser.add_argument("--audit", type=Path, default=cfg.AUDIT_LOG_PATH)
    parser.add_argument("--account", type=Path, default=Path(cfg.AUDIT_LOG_PATH).parent / "account.jsonl")
    parser.add_argument("--random", type=int, default=schedule.RANDOM_FUNDS,
                        help="coin-flip funds for the band (default: %(default)s)")
    parser.add_argument("--processes", type=int, default=1,
                        help="cores for the coin-flip funds (default: %(default)s)")
    parser.add_argument("--with-prices", action="store_true",
                        help="also hand over the daily prices this run used: their SHA-256 as "
                             "prices_sha256, and the table itself as one JSON line printed last")
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.ERROR,
                        format="%(levelname)s %(name)s: %(message)s")
    now = _now()
    used: list = []
    out = build(args, now, used)
    tape = None
    if args.with_prices:
        # What the fetcher cached once everything above had run: the bars the
        # funds were priced with. A new last key; every other key is as it was.
        tape = price_tape.tape([("ohlc", fetcher) for fetcher in used], consumer="funds",
                               final_through=out.get("final_through"), generated_at=now)
        out["prices_sha256"] = tape["prices_sha256"]
    # allow_nan=False: NaN is not JSON, and a browser that cannot parse the
    # file would show nothing at all. A NaN here is a bug to fail on.
    print(json.dumps(out, separators=(",", ":"), allow_nan=False))
    if tape is not None:
        print(price_tape.dumps(tape))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
