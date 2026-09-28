#!/usr/bin/env python3
"""Run a history screen of the rules running live, and write its report.

    python -m history.screen fetch --out OUT          # the price table (needs Yahoo: run it on GitHub)
    python -m history.screen run --out OUT            # the journal, the race, the funds, the report
    python -m history.screen run --out OUT --processes 4 --seeds 1000

``fetch`` writes ``OUT/prices.csv.gz`` (and its SHA-256 beside it). ``run``
reads it and writes, all under ``OUT``:

* ``journal/YYYY-MM.log``: the history journal (``history.journal``);
* ``results.json``: every number, for checking and for the next screen;
* ``report.md``: the report (``history.report``).

The workflow ``.github/workflows/history-screen.yml`` runs both, by hand only,
and commits ``results.json`` and ``report.md`` to ``docs/research/history/``.
Nothing else is written, anywhere.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis import horse_race as hr  # noqa: E402
from config import journal_files  # noqa: E402
from config.watchlist import DEFAULT_WATCHLIST  # noqa: E402
from history import journal, prices, race, report  # noqa: E402
from history import funds as fund_screen  # noqa: E402
from history.sessions import production_differences  # noqa: E402
from shadow.market import Bars  # noqa: E402

log = logging.getLogger("history.screen")

#: What the forked fund worker reads (set before the pool forks).
_FUNDS: dict = {}


def _funds_job() -> dict:
    s = _FUNDS
    return fund_screen.run_funds(s["journal"], s["frames"], s["sessions"], s["final_through"])


def sessions_of(table: prices.PriceTable) -> list[date]:
    """The sessions: every day SPY has a final bar for (``history.sessions``)."""
    frame = table.frames[prices.CALENDAR_TICKER]
    return [stamp.date() for stamp in frame.index]


def price_gaps(table: prices.PriceTable, sessions: list[date], first: date) -> dict:
    """Ticker-days a name was trading but the price source has no bar for (section 11.2's count)."""
    known = set(sessions)
    out = {}
    total = missing = 0
    for ticker in DEFAULT_WATCHLIST:
        frame = table.frames.get(ticker)
        if frame is None or frame.empty:
            continue
        have = {stamp.date() for stamp in frame.index}
        lo, hi = max(first, min(have)), max(have)
        expected = [d for d in sessions if lo <= d <= hi]
        gaps = [d for d in expected if d not in have]
        total += len(expected)
        missing += len(gaps)
        if gaps:
            out[ticker] = {"missing": len(gaps), "examples": [d.isoformat() for d in gaps[:5]]}
    extra = {t: len({s.date() for s in f.index} - known) for t, f in table.frames.items()
             if len({s.date() for s in f.index} - known)}
    return {"ticker_days": total, "missing": missing, "share": missing / total if total else None,
            "by_ticker": out, "bars_on_days_spy_did_not_trade": extra}


def run(args: argparse.Namespace) -> int:
    from multiprocessing import get_context

    out: Path = args.out
    started = time.monotonic()
    table, prices_sha = prices.load(args.prices or out / "prices.csv.gz")
    # The calendar, the VT fund and B cannot be done without these; say so now, not after an hour.
    absent = [t for t in (prices.CALENDAR_TICKER, prices.INDEX_TICKER, prices.BILLS_TICKER)
              if t not in table.frames or table.frames[t].empty]
    if absent:
        raise SystemExit(f"history screen: no prices for {', '.join(absent)}; nothing was run")
    sessions = sessions_of(table)
    final_through = table.final_through
    log.info("prices through %s, %d sessions, sha256 %s", final_through, len(sessions), prices_sha)

    journal_dir = out / "journal"
    if args.reuse_journal and journal_files.exists(journal_dir):
        lines = sum(1 for _ in journal_files.iter_lines(journal_dir))
    else:
        months = journal.build(table.frames, sessions, first=args.first, processes=args.processes)
        lines = journal.write(months, journal_dir)
        del months
    journal_sha = hashlib.sha256(journal_files.read_bytes(journal_dir)).hexdigest()
    log.info("journal: %d lines, sha256 %s (%.0fs)", lines, journal_sha, time.monotonic() - started)

    bars = Bars(dict(table.frames))
    years = sorted({int(p.name[:4]) for p in journal.months_of(journal_dir)})
    race._SHARED.update(journal=journal_dir, frames=table.frames, bars=bars, sessions=sessions,
                        final_through=final_through)
    _FUNDS.update(journal=journal_dir, frames=table.frames, sessions=sessions, final_through=final_through)
    with get_context("fork").Pool(max(2, args.processes)) as pool:
        pending_funds = pool.apply_async(_funds_job)
        years_done = pool.map(race._year_job, years, chunksize=1)
        log.info("race: %d years (%.0fs)", len(years_done), time.monotonic() - started)
        fund_results = pending_funds.get()
    log.info("funds done (%.0fs)", time.monotonic() - started)

    pooled = race.pool_years(years_done)
    del years_done
    keys = sorted({t.key for name in race.ARMS for t in pooled.arms[name]})
    flips = race.coin_flips(keys, args.seeds, processes=args.processes)
    row_of = {key: i for i, key in enumerate(keys)}
    log.info("coin flips: %d lines x %d seeds (%.0fs)", len(keys), args.seeds, time.monotonic() - started)
    race_results = race.summarise(pooled, flips, row_of)

    first = args.first
    results = {
        "meta": {
            "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "final_through": final_through.isoformat(),
            "first_line_day": first.isoformat(),
            "last_session": sessions[-1].isoformat(),
            "watchlist_names": len(DEFAULT_WATCHLIST),
            "prices_sha256": prices_sha,
            "prices_fetched_at": table.fetched_at,
            "journal_sha256": journal_sha,
            "journal_lines": lines,
            "seeds": args.seeds,
            "horizon": hr.DEFAULT_HORIZON,
            "cost_per_side": hr.DEFAULT_COST_PER_SIDE,
            "missing_tickers": list(table.missing),
            "run": {"run_id": args.run_id, "commit": args.commit},
            "seconds": round(time.monotonic() - started),
        },
        "data": {
            "coverage": prices.coverage(table, (*DEFAULT_WATCHLIST, prices.CALENDAR_TICKER, prices.INDEX_TICKER,
                                                prices.BILLS_TICKER)),
            "price_gaps": price_gaps(table, sessions, first),
            "calendar_vs_production": production_differences(sessions, date(2025, 1, 1), final_through),
        },
        "race": race_results,
        "funds": fund_results,
    }
    out.mkdir(parents=True, exist_ok=True)
    text = json.dumps(results, indent=1, default=str) + "\n"
    (out / "results.json").write_text(text, encoding="utf-8")
    # From the file's own text, so the report can always be written again from results.json alone.
    (out / "report.md").write_text(report.render(json.loads(text)), encoding="utf-8")
    log.info("wrote %s (%.0fs)", out, time.monotonic() - started)
    return 0


def fetch(args: argparse.Namespace) -> int:
    table = prices.fetch()
    digest = prices.save(table, args.out / "prices.csv.gz")
    print(f"prices through {table.final_through}: {len(table.frames)} tickers, sha256 {digest}")
    if table.missing:
        print(f"missing: {', '.join(table.missing)}")
    return 0


def _positive(text: str) -> int:
    value = int(text)
    if value < 1:
        raise argparse.ArgumentTypeError("at least 1: a screen always draws the coin flip's band")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="history.screen", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    f = sub.add_parser("fetch", help="fetch the price table (needs Yahoo)")
    f.add_argument("--out", type=Path, required=True)
    r = sub.add_parser("run", help="build the journal, race and run the funds, write the report")
    r.add_argument("--out", type=Path, required=True)
    r.add_argument("--prices", type=Path, default=None, help="the table (default: OUT/prices.csv.gz)")
    r.add_argument("--processes", type=int, default=os.cpu_count() or 2)
    r.add_argument("--seeds", type=_positive, default=hr.DEFAULT_SEEDS,
                   help="coin flips per line for the band (default: the race's %(default)s)")
    r.add_argument("--first", type=date.fromisoformat, default=journal.FIRST_LINE_DAY)
    r.add_argument("--reuse-journal", action="store_true", help="read OUT/journal instead of building it")
    r.add_argument("--run-id", default=None, help="the workflow run, for the report's header")
    r.add_argument("--commit", default=None, help="the commit the code was run at, for the report's header")
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(message)s")
    args = build_parser().parse_args(argv)
    return fetch(args) if args.command == "fetch" else run(args)


if __name__ == "__main__":
    raise SystemExit(main())
