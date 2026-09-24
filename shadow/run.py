#!/usr/bin/env python3
"""Run calibration and the four funds, and print what the dashboard reads.

    python -m shadow.run                      # the nightly job: JSON to stdout
    python -m shadow.run --processes 4        # the coin-flip funds on 4 cores

Prints one JSON document (the "funds" contract in ``dashboard/funds.html``).
What it contains depends on ``shadow/schedule.py`` and nothing else:

* no calibration start set: calibration "not_started", the proposed pass
  rule, the real account's holding times. No fund is run.
* calibration started: the calibration fund against the real account,
  day by day, with the trades that differ. Still no fund is run -- during
  calibration only the match is reported.
* fund start set: the four funds and the 1,000 coin-flip funds, from that
  day, through the last final close.

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
from typing import Iterable, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis.baseline_compare import OhlcFetcher  # noqa: E402
from analysis.reader import JournalEntry, read_journal  # noqa: E402
from analysis.returns import last_final_session  # noqa: E402
from config import settings as cfg  # noqa: E402
from shadow import schedule  # noqa: E402
from shadow.broker import ENTRY  # noqa: E402
from shadow.fund import (  # noqa: E402
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

log = logging.getLogger("shadow.run")

INDEX_TICKER = "VT"
LABELS = {"model": "Model", "momentum": "Momentum", "hybrid": "Hybrid", "vt": "VT (world index, held)"}

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


def summarise(fund, vt_return: Optional[float]) -> dict:
    equity = [d.equity for d in fund.days]
    total = equity[-1] / STARTING_CASH - 1.0 if equity else 0.0
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
    }


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
    """What would say the simulation itself went wrong, fund by fund."""
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
    return {"ok": not problems, "problems": problems[:50]}


# --------------------------------------------------------------------------- #
# The coin-flip funds, on several cores
# --------------------------------------------------------------------------- #

#: Set before the pool forks, so every worker reads the same bars without a copy.
_SHARED: dict = {}


def _coin_chunk(seeds: Sequence[int]) -> list[tuple[int, list[float], dict]]:
    shared = _SHARED
    feed = SimFeed(shared["bars"])
    funds = [Fund(f"coin-{seed}", coin_signal(seed), feed, shared["bars"],
                  not_shortable=shared["not_shortable"]) for seed in seeds]
    run(funds, shared["sessions"], shared["cycles"], shared["ran"], feed)
    return [(seed, [d.equity for d in fund.days], integrity([fund])) for seed, fund in zip(seeds, funds)]


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
    return [curve for _, curve, _ in results], {"ok": not problems, "problems": problems[:50]}


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
    run(four, sessions, cycles, ran, feed)
    vt = four[-1].days[-1].equity / STARTING_CASH - 1.0 if four[-1].days else None
    curves, coin_check = coin_funds(random_funds, processes, bars, sessions, cycles, ran, shortable_no)
    check = integrity(four)
    return {
        "start": start.isoformat(),
        "days": [d.isoformat() for d in sessions],
        "list": [summarise(f, vt) for f in four],
        "band": band(curves),
    }, {"four": check, "coin": coin_check}


def build(args: argparse.Namespace, now: datetime) -> dict:
    from shadow import calibration as calib

    final_through = last_final_session(now)
    read = read_journal(args.journal)
    audit_lines = _read_lines(args.audit)
    snapshots = calib.load_snapshots(_read_lines(args.account))
    shortable_no = not_shortable(audit_lines)
    fetcher = OhlcFetcher(final_through=final_through)
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
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.ERROR,
                        format="%(levelname)s %(name)s: %(message)s")
    # allow_nan=False: NaN is not JSON, and a browser that cannot parse the
    # file would show nothing at all. A NaN here is a bug to fail on.
    print(json.dumps(build(args, _now()), separators=(",", ":"), allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
