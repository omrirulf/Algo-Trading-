#!/usr/bin/env python3
"""Does the fund machinery hold on the real journal and real prices? Prints no result.

    python -m shadow.smoke                    # the last 15 final sessions, 20 coin-flip funds
    python -m shadow.smoke --sessions 30 --random 50

The tests run the funds on made-up bars and made-up lines. This runs them
the way the nightly job will: the journal as the heartbeat wrote it, the
paper account's own short refusals, and yfinance's final closes, through
the production engine and position manager on simulated books. It exists to
catch what made-up data cannot -- a field the real journal spells
differently, a ticker with a missing bar, a rejection the tests never
thought of.

It prints only whether the machinery held, fund by fund: sessions run,
cycles acted on, orders the engine accepted and refused, fills by kind,
positions left open, and every integrity problem -- an unexpected engine
error, a position-manager error, a position its stops do not cover, a line
that reached the live audit log. Never an equity, a return, a win rate or a
comparison between funds: those belong to the fund test, from its start
date, and are not computed for display before it.

Exit status 1 when any fund has an integrity problem, so the workflow that
runs this goes red. Reads the journal, the live audit log (read only) and
yfinance. Writes nothing.
"""

from __future__ import annotations

import argparse
import logging
import sys
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis.baseline_compare import OhlcFetcher  # noqa: E402
from analysis.reader import read_journal  # noqa: E402
from analysis.returns import last_final_session  # noqa: E402
from config import settings as cfg  # noqa: E402
from shadow.fund import (  # noqa: E402
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
from shadow.run import INDEX_TICKER, _read_lines, integrity, not_shortable  # noqa: E402

#: Calendar days fetched per session wanted: weekends and holidays, with room.
_DAYS_PER_SESSION = 1.6
#: More of the (ticker, session) pairs missing than this is a fetch that
#: broke, not a vendor's odd day, and fails the run. A vendor's odd day is
#: reported and does not.
MAX_MISSING_SHARE = 0.10


def health(fund) -> dict:
    """What the fund did, as counts; nothing about how well it did."""
    if isinstance(fund, IndexFund):
        return {"name": fund.name, "sessions": len(fund.days), "held": bool(fund.qty)}
    kinds = Counter(f.kind for f in fund.broker.fills)
    return {
        "name": fund.name,
        "sessions": len(fund.days),
        "accepted": fund.tally.accepted,
        "refused": fund.tally.rejected + fund.tally.errors,
        "fills": dict(sorted(kinds.items())),
        "open": len(fund.broker.positions),
        "data_holes": len(fund.tally.data_holes),
        "problems": integrity([fund])["problems"],
    }


def missing_bars(bars: Bars, tickers, sessions) -> list[tuple[str, date]]:
    """(ticker, session) pairs with no bar, inside each ticker's own span of bars."""
    out = []
    for ticker in sorted(tickers):
        have = bars.sessions(ticker, sessions[0], sessions[-1])
        if not have:
            out += [(ticker, day) for day in sessions]
            continue
        out += [(ticker, day) for day in sessions if have[0] <= day <= have[-1] and day not in set(have)]
    return out


def smoke(entries, sessions_wanted: int, coin_funds: int, fetcher, final_through, shortable_no) -> list[dict]:
    cycles = lines_by_day(entries)
    ran = cycle_days(entries)
    first = final_through - timedelta(days=int(sessions_wanted * _DAYS_PER_SESSION) + 7)
    tickers = {line.ticker for day, lines in cycles.items() if day >= first for line in lines} | {INDEX_TICKER}
    bars = Bars.fetch(tickers, first, final_through, fetcher)
    sessions = calendar(bars, (INDEX_TICKER, "SPY", *sorted(tickers)), first, final_through)[-sessions_wanted:]
    if not sessions:
        raise SystemExit("no session with prices in the window: nothing was run")
    feed = SimFeed(bars)
    funds = [
        Fund("model", model_signal, feed, bars, not_shortable=shortable_no),
        Fund("momentum", rule_signal("momentum"), feed, bars, not_shortable=shortable_no),
        Fund("hybrid", rule_signal("hybrid"), feed, bars, not_shortable=shortable_no),
        IndexFund("vt", INDEX_TICKER, bars),
        *(Fund(f"coin-{seed}", coin_signal(seed), feed, bars, not_shortable=shortable_no)
          for seed in range(coin_funds)),
    ]
    run(funds, sessions, cycles, ran, feed)
    acted = sum(1 for previous in sessions[:-1] if previous in ran)
    print(f"sessions {sessions[0].isoformat()} to {sessions[-1].isoformat()} ({len(sessions)}); "
          f"cycles acted on: {acted}; tickers fetched: {len(tickers)}; "
          f"refused shorts read from the paper account: {', '.join(sorted(shortable_no)) or 'none'}")
    gaps = missing_bars(bars, tickers, sessions)
    share = len(gaps) / (len(tickers) * len(sessions))
    by_day = Counter(day for _, day in gaps)
    print(f"missing bars: {len(gaps)} of {len(tickers) * len(sessions)} ticker-sessions ({share:.1%}); "
          + ("; ".join(f"{day.isoformat()}: {n}" for day, n in sorted(by_day.items())) or "none"))
    rows = [health(f) for f in funds]
    if share > MAX_MISSING_SHARE:
        rows.append({"name": "prices", "problems": [f"{share:.1%} of ticker-sessions have no bar: the fetch broke"]})
    return rows


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="shadow.smoke", description=__doc__.split("\n\n")[0])
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH)
    parser.add_argument("--audit", type=Path, default=cfg.AUDIT_LOG_PATH)
    parser.add_argument("--sessions", type=int, default=15)
    parser.add_argument("--random", type=int, default=20, help="coin-flip funds (default: %(default)s)")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.ERROR, format="%(levelname)s %(name)s: %(message)s")

    final_through = last_final_session(datetime.now(timezone.utc))
    report = smoke(read_journal(args.journal).entries, args.sessions, args.random,
                   OhlcFetcher(final_through=final_through), final_through,
                   not_shortable(_read_lines(args.audit)))
    failed = 0
    for row in report:
        problems = row.pop("problems", [])
        print(row)
        for problem in problems:
            print(f"  PROBLEM {problem}")
        failed += bool(problems)
    coins = [r for r in report if r["name"].startswith("coin-")]
    if coins and not any(r["accepted"] for r in coins):
        print("PROBLEM no coin-flip fund had a single order accepted")
        failed += 1
    print("OK: the machinery held" if not failed else f"FAILED: {failed} fund(s) with a problem")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
