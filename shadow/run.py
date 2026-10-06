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
* calibration passed: the four funds and the 1,000 coin-flip funds, from
  the fixed fund start (``schedule.FUND_START``, acting first on the cycle
  of ``schedule.FUND_FIRST_CYCLE``), through the last final close -- and,
  listed after the four, the three exploratory funds
  (``EXPLORATORY_FUNDS``), each compared with the model fund. Every fund but
  VT also says how its longs and its shorts did.

**The hard gate** (the owner's decision of 26 Sep 2026): the fund start is
fixed, but the fund test counts only after calibration passes. Until the
calibration verdict is "passed", no fund is run: nothing about a fund's
book, equity or trades is calculated, and ``funds`` and ``integrity`` are
null (``build``). A delayed calibration delays the reading, never the start.

**Exploratory results only at checkpoints** (pre-registration section 13.1,
2026-09-28): the three exploratory funds and tests A, B and C (``shadow.
exploratory``) are run only on the night the race first reaches a planned
look (``--race-gate``), and only once calibration has passed. Their results
go into a record for that look, carried unchanged from the previous
document (``--previous``) every night after; between looks the document
carries only their counters, which are counted from the journal and the
prices without running a fund.

**The voting arm and the thesis check: nothing before their dates**
(pre-registration sections 13.11 and 13.12, the owner's instruction of
4 Oct 2026). From 2026-12-22 (``config.model_vote.START``) the document
carries the vote's counters, and a look's record carries its race arm, its
fund against the model fund on the same lines (``shadow.vote``) and the
descriptive IC comparison. From 2027-04-01 (``config.thesis_check.START``)
it carries the thesis check's counters, and a look's record its
BROKEN-against-VALID description, which is in no test's family. Before
those dates neither key exists anywhere in the document, and the vote's and
the checks' lines are not even read (``--votes``, ``--thesis``).

**The fund test's verdict** (sections 11.5-11.8; the layout the owner
approved on 2026-10-06, ``docs/research/checkpoint-verdict-plan.md``): on the
night the race's look is readable, each look gets one record under
``fund_test.looks`` -- skipped if calibration has not passed that night, else
read at the fund test's own bar by the spending rule of 11.7 and decided by
``decision_gate.decide`` -- and keeps it unchanged every night after
(``fund_test_part``). ``fund_test.verdict`` is the first deciding look's
verdict, and the document's last key, ``verdict``, combines it with the
race's (section 11.8).

Two reports that are not fund results are in every document from the fund
start on, whatever calibration says: ``price_gaps`` (the price source's
missing ticker-days per calendar month over the watchlist) and
``held_names`` (the names the paper account held, so no fund could trade
them, per cycle day).

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
from typing import Final, Iterable, Mapping, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis import price_tape  # noqa: E402
from analysis.baseline_compare import OhlcFetcher  # noqa: E402
from analysis.reader import JournalEntry, read_journal  # noqa: E402
from analysis.returns import last_final_session  # noqa: E402
from config import model_vote as mv  # noqa: E402
from config import settings as cfg  # noqa: E402
from config import thesis_check as tc  # noqa: E402
from config.market_calendar import is_trading_day  # noqa: E402
from config.watchlist import DEFAULT_WATCHLIST  # noqa: E402
from shadow import schedule  # noqa: E402
from shadow.broker import ENTRY  # noqa: E402
from shadow.fund import (  # noqa: E402
    CONVICTION_FIRST,
    NO_PRICE,
    OTHER_DAY,
    OUTSIDE_HOURS,
    SAME_DAY,
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
from shadow import exploratory as xp  # noqa: E402

log = logging.getLogger("shadow.run")

INDEX_TICKER = "VT"
LABELS = {"model": "Model", "momentum": "Momentum", "hybrid": "Hybrid", "vt": "VT (world index, held)",
          "model_by_conviction": "Model, highest conviction first", "model_sized": "Model, sized by conviction",
          "model_same_day": "Model, entered the same day", xp.VETO: "Momentum, 200-day average veto (A)",
          xp.TIMING: "VT or T-bills by the 10-month average (B)", xp.LIMIT: "Momentum, pullback limit entry (C)"}

#: The owner's exploratory funds (decisions 3 and 4 of 25 Sep 2026, and
#: ``model_same_day`` of 26 Sep 2026), in the order they are listed, after
#: the four. The model's own signals, each with one thing changed: the
#: buying order, the size, then the day and price of entry. Each is compared
#: with the model fund, never ranked with the four: it cannot change the
#: decision.
EXPLORATORY_FUNDS: Final[tuple[str, ...]] = ("model_by_conviction", "model_sized", "model_same_day")
#: The same-day fund's lines not entered, by reason, as the JSON names them.
NOT_ENTERED_KEYS: Final[dict[str, str]] = {NO_PRICE: "no_price", OUTSIDE_HOURS: "outside_hours",
                                           OTHER_DAY: "other_day"}
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


def _refused_on(record: dict) -> date:
    """The UTC day an audit line was written: its ``ts`` (UTC), else its result's timestamp.

    UTC because the funds date a cycle by its UTC day (``shadow.fund.lines_by_day``),
    and a refusal happens during the cycle that asked for the short. A line
    that carries neither is dated ``date.min``: refused from the start, as
    every refusal was before refusals were dated.
    """
    from shadow.calibration import _audit_instant, _instant

    result = record.get("result") if isinstance(record.get("result"), dict) else {}
    moment = _audit_instant(record.get("ts")) or _instant(result.get("timestamp"))
    return moment.astimezone(timezone.utc).date() if moment is not None else date.min


def not_shortable(audit_lines: Iterable[str]) -> dict[str, date]:
    """Tickers the paper account has refused to short, from its own audit log: name -> first refusal day.

    The day is the audit line's UTC day, the calendar the funds date cycles
    on. A fund acting on a cycle journalled on day D is refused only the
    names refused on D or earlier (``shadow.fund.refused_by``): a refusal
    counts from the day it happened, never backwards (the owner's decision
    of 26 Sep 2026).
    """
    found: dict[str, date] = {}
    for raw in audit_lines:
        if "short" not in raw and "borrow" not in raw:
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if not isinstance(record, dict):
            continue
        reason = str(((record.get("result") or {}).get("reason")) or "")
        for pattern in _NOT_SHORTABLE:
            match = pattern.search(reason)
            if match:
                ticker, day = match.group(1).upper(), _refused_on(record)
                found[ticker] = min(day, found.get(ticker, day))
    return dict(sorted(found.items()))


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
    """An exploratory fund's row: every field a fund has, and how it compares with the model fund.

    The same-day fund's row also counts the directional lines it did not
    enter, by reason (``not_entered``): no usable recorded price, recorded
    outside regular New York hours, recorded on another day.
    """
    row = summarise(fund, vt_return) | {"compare_to": COMPARE_TO, "vs_model": vs_model(fund, model)}
    if getattr(fund, "entry", None) == SAME_DAY:
        counts = {key: fund.not_entered.get(reason, 0) for reason, key in NOT_ENTERED_KEYS.items()}
        row["not_entered"] = counts | {"total": sum(counts.values())}
    return row


def exploratory_funds(feed: SimFeed, bars: Bars, shortable_no) -> list[Fund]:
    """The three exploratory funds: the model fund with one thing changed each.

    Same signals, feed, bars, costs, starting cash and short refusals as the
    model fund; everything else is the ``Fund`` defaults, which are
    production's. Simulation only.
    """
    return [
        Fund("model_by_conviction", model_signal, feed, bars, not_shortable=shortable_no,
             priority=CONVICTION_FIRST),
        Fund("model_sized", model_signal, feed, bars, not_shortable=shortable_no, sized_by_conviction=True),
        Fund("model_same_day", model_signal, feed, bars, not_shortable=shortable_no, entry=SAME_DAY),
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
        if not hasattr(fund, "broker"):
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
    holes = [f"{fund.name}: {h}" for fund in funds if hasattr(fund, "broker") for h in fund.tally.data_holes]
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
    run(funds, shared["sessions"], shared["cycles"], shared["ran"], feed, shared.get("first_cycle"))
    return [(seed, [d.equity for d in fund.days], integrity([fund]) | {"order_days": fund_summary(fund)["days"]})
            for seed, fund in zip(seeds, funds)]


def coin_funds(count: int, processes: int, bars: Bars, sessions, cycles, ran, shortable_no,
               first_cycle: Optional[date] = None) -> tuple[list[list[float]], dict]:
    _SHARED.update(bars=bars, sessions=sessions, cycles=cycles, ran=ran, not_shortable=shortable_no,
                   first_cycle=first_cycle)
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
# Two reports that are not fund results: price gaps, held names
# --------------------------------------------------------------------------- #


def price_gaps(fetcher, first: date, last: date, tickers: Sequence[str] = tuple(DEFAULT_WATCHLIST)) -> dict:
    """The price source's missing ticker-days, per calendar month (the owner's decision of 26 Sep 2026).

    A ticker-day is missing when a watchlist ticker has no final bar on a
    trading day (the exchange calendar: every watchlist name trades every
    session). The share for a month is missing ticker-days / (watchlist
    tickers x that month's sessions), over the sessions from ``first`` to
    ``last``. Every fund leaves such a ticker's position as it was that day
    (``shadow.fund``); this says how often it happened, not what it cost.
    Bars come through the run's own fetcher (the race's ``OhlcFetcher``),
    so a ticker the run already fetched is not fetched again. ``over`` is
    the month's share above the owner's 2%
    (``config.settings.MAX_PRICE_GAP_SHARE``), the line the daily health
    check warns at.
    """
    MAX_PRICE_GAP_SHARE = cfg.MAX_PRICE_GAP_SHARE

    sessions = [first + timedelta(days=i) for i in range((last - first).days + 1)]
    sessions = [d for d in sessions if is_trading_day(d)]
    out = {"from": first.isoformat(), "through": last.isoformat(), "tickers": len(tickers),
           "limit": MAX_PRICE_GAP_SHARE, "months": []}
    if not sessions:
        return out
    bars = Bars.fetch(tickers, first, last, fetcher)
    months: dict[str, dict] = {}
    for day in sessions:
        month = months.setdefault(day.strftime("%Y-%m"), {"sessions": 0, "missing": 0, "days": {}})
        month["sessions"] += 1
        missing = [t for t in sorted(tickers) if bars.bar(t, day) is None]
        month["missing"] += len(missing)
        if missing:
            month["days"][day.isoformat()] = len(missing)
    for name, month in months.items():
        share = month["missing"] / (len(tickers) * month["sessions"])
        out["months"].append({"month": name, "sessions": month["sessions"], "missing": month["missing"],
                              "share": share, "over": share > MAX_PRICE_GAP_SHARE, "by_day": month["days"]})
    return out


def held_names(entries: Iterable[JournalEntry], first: date) -> dict:
    """Per cycle day from ``first``: the names the paper account held, so no fund could trade them.

    The model is not asked about a name the paper account holds, so the
    line is ``held`` and every fund skips it that day (the race's rule,
    ``shadow.fund.lines_by_day``). A report, nothing more: the known
    limitation of section 11.1, counted every day. ``names`` is the distinct
    tickers, ``lines`` the held lines (a second cycle can repeat a name).
    Days are the funds' own: UTC cycle days.
    """
    days: dict[date, dict] = {}
    for entry in entries:
        if entry.timestamp is None:
            continue
        stamp = entry.timestamp
        day = (stamp.astimezone(timezone.utc) if stamp.tzinfo else stamp).date()
        if day < first:
            continue
        row = days.setdefault(day, {"names": set(), "lines": 0, "asked": set()})
        row["asked"].add(entry.ticker)
        if entry.held:
            row["names"].add(entry.ticker)
            row["lines"] += 1
    return {"from": first.isoformat(),
            "days": [{"day": day.isoformat(), "names": len(row["names"]), "lines": row["lines"],
                      "of": len(row["asked"])} for day, row in sorted(days.items())]}


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def _read_lines(path: Path) -> list[str]:
    try:
        return path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return []


def paired(fund, other, after: Optional[date] = None, through: Optional[date] = None) -> dict:
    """``fund`` against ``other`` day by day, on the sessions both have: the test of section 13.

    The daily net returns are paired by date (a fund that starts later, like
    B, is paired from its own first session), then judged as the fund test's
    are: mean difference, Newey-West t (lag 5), two-sided p, and the stats
    the Deflated Sharpe Ratio reads (``analysis.multiple_tests``). With
    ``after``, only the sessions strictly after that day are paired: the
    vote's lines begin on the 2026-12-22 cycle, acted on at the next open
    (section 13.11), so the days before are two books of cash, not a test.

    ``through`` cuts the paired days at that session (the fund test's look,
    section 11.6: "read on the same days as the race's looks"), and adds
    ``through``, the last paired day; the totals and drawdowns stay the
    whole run's. Without it (the exploratory tests and the vote) nothing changes.
    """
    from analysis.horse_race import newey_west_t
    from analysis.multiple_tests import p_two_sided, series_stats

    def by_day(f) -> dict:
        equity = [STARTING_CASH] + [round(d.equity, 2) for d in f.days]
        return {d.day: today / before - 1.0 for d, before, today in zip(f.days, equity, equity[1:])}

    mine, theirs = by_day(fund), by_day(other)
    days = sorted(d for d in set(mine) & set(theirs) if after is None or d > after)
    if through is not None:
        days = [d for d in days if d <= through]
    diffs = [mine[d] - theirs[d] for d in days]
    t = newey_west_t(diffs, VS_MODEL_LAG)
    out = {"compare_to": other.name, "days": len(diffs), "from": days[0].isoformat() if days else None,
           "mean_daily_diff": statistics.fmean(diffs) if diffs else None, "t": t, "p": p_two_sided(t),
           "stats": series_stats(diffs),
           "total_return": total_return(fund), "compare_total_return": total_return(other),
           "max_drawdown": max_drawdown([d.equity for d in fund.days]),
           "compare_max_drawdown": max_drawdown([d.equity for d in other.days])}
    if through is not None:
        out["through"] = days[-1].isoformat() if days else None
    return out


def order_changed_days(fund, model) -> int:
    """Sessions on which ``fund`` bought something other than the model fund did (section 13.7)."""
    def bought(f) -> dict:
        out: dict = {}
        for fill in f.broker.fills:
            if fill.kind == ENTRY:
                out.setdefault(fill.day, set()).add((fill.ticker, fill.side))
        return out

    mine, theirs = bought(fund), bought(model)
    return sum(1 for day in set(mine) | set(theirs) if mine.get(day, set()) != theirs.get(day, set()))


def sized_trades_scaled(fund) -> int:
    """``model_sized`` acting differently (section 13.7): its accepted entries whose size factor is not 1.0.

    Conviction 0.50-0.60 has factor 1.0 -- the model fund's own size -- so those trades do not differ.
    """
    from shadow.fund import conviction_factor

    return sum(1 for e in fund.order_events or [] if e.status == "ACCEPTED" and e.conviction is not None
               and conviction_factor(e.conviction) not in (None, 1.0))


def new_funds(feed: SimFeed, bars: Bars, long_bars: Bars, final_through: date, shortable_no) -> list:
    """Tests A, B and C as funds (section 13): the veto and pullback funds on the funds' own bars and feed."""
    return [
        Fund(xp.VETO, xp.veto_signal(long_bars), feed, bars, not_shortable=shortable_no),
        xp.TimingFund(xp.TIMING, long_bars, final_through),
        xp.PullbackFund(xp.LIMIT, feed, bars, not_shortable=shortable_no),
    ]


def vote_funds(feed: SimFeed, bars: Bars, shortable_no, votes: Mapping) -> list[Fund]:
    """The voting arm as a fund, and its comparator (section 13.11): the model fund with one thing changed.

    ``model_vote`` trades the vote's answer on each line that has one;
    ``model_vote_comparator`` trades the model's single call on exactly
    those lines. Same feed, bars, costs, starting cash, refusals and
    production engine as the model fund. Simulation only, and never in the
    funds' list: they are compared with each other, never ranked.
    """
    from shadow import vote as sv

    return [
        Fund(mv.ARM, sv.vote_signal(votes), feed, bars, not_shortable=shortable_no),
        Fund(mv.COMPARATOR_FUND, sv.comparator_signal(votes), feed, bars, not_shortable=shortable_no),
    ]


def price_coverage(cycles: dict, bars: Bars, start: date, final_through: date) -> dict:
    """Each ticker the funds could trade, as ``(first cycle day, last final bar)``, from the funds' own fetch.

    What section 5c's "the funds' prices reach the close of the look's last
    trades" is checked against (``after_tax_part``): a name with a cycle on
    or before a look's last close must have a bar on that close. VT counts
    from the fund start. A name with no bar at all has None for its last bar.
    """
    first: dict[str, date] = {}
    for day in sorted(cycles):
        for line in cycles[day]:
            first.setdefault(line.ticker, day)
    first.setdefault(INDEX_TICKER, start)
    out = {}
    for ticker, day in sorted(first.items()):
        sessions = bars.sessions(ticker, start, final_through)
        out[ticker] = (day, sessions[-1] if sessions else None)
    return out


def missing_prices(coverage: Optional[dict], end: date) -> Optional[list[str]]:
    """The names whose prices do not reach ``end`` though a cycle named them by then; None without coverage."""
    if coverage is None:
        return None
    return [t for t, (first, last) in sorted(coverage.items()) if first <= end and (last is None or last < end)]


def run_funds(
    entries: Sequence[JournalEntry], start: date, final_through: date, fetcher, *,
    random_funds: int, processes: int, shortable_no, first_cycle: Optional[date] = None,
    exploratory: bool = True, long_bars: Optional[Bars] = None, rates=None,
    votes: Optional[Mapping] = None, fund_test: bool = False,
) -> tuple[dict, dict]:
    """Every fund from ``start`` through ``final_through``. Called only once calibration has passed (``build``).

    ``first_cycle`` is the cycle day the first session acts on at its open
    (the fund test's 2026-09-28); without one, the first session acts on no
    cycle. ``shortable_no`` is the paper account's refusals, name -> first
    refusal day (``not_shortable``), or a plain set of names refused from
    the start. ``rates`` is the night's shekel rate table (``analysis.boi_rates``):
    with it, every fund is also reckoned after Israeli tax (``shadow.after_tax``),
    the four funds' views go under ``after_tax`` and every fund's series under
    ``_after_tax_series``, which ``build`` takes out before anything is printed.
    ``votes`` is the voting arm's answers by line (``analysis.vote.answers``),
    given only on a checkpoint night from 2026-12-22 (section 13.11): with
    it, and with the exploratory funds, the vote's fund and its comparator
    run too, and their test goes under ``tests``.
    With ``fund_test``, the output also carries ``_fund_test``: the four funds and the
    coin-flip funds' raw equity, which the fund test reads at a look
    (``fund_test_part``). Neither changes anything else in the output.
    """
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
    explore = exploratory_funds(feed, bars, shortable_no) if exploratory else []
    tests = new_funds(feed, bars, long_bars, final_through, shortable_no) if exploratory and long_bars else []
    # Section 13.11: after the others, so the positions of ``tests`` do not move.
    voting = vote_funds(feed, bars, shortable_no, votes) if exploratory and votes is not None else []
    # One run for all of them: the same sessions, cycles and feed clock.
    run([*four, *explore, *tests, *voting], sessions, cycles, ran, feed, first_cycle)
    vt = four[-1].days[-1].equity / STARTING_CASH - 1.0 if four[-1].days else None
    curves, coin_check = coin_funds(random_funds, processes, bars, sessions, cycles, ran, shortable_no,
                                    first_cycle)
    # The key keeps its name; the check covers the exploratory funds too.
    check = integrity([*four, *explore, *tests, *voting])
    model = next(f for f in four if f.name == COMPARE_TO)  # the three exploratory funds' comparator
    out = {
        "start": start.isoformat(),
        "days": [d.isoformat() for d in sessions],
        "list": [summarise(f, vt) for f in four] + [summarise_exploratory(f, model, vt) for f in explore],
        "band": band(curves),
    }
    if explore:
        out["tests"] = {f.name: paired(f, model) for f in explore}
        by_conviction = next((f for f in explore if f.name == "model_by_conviction"), None)
        if by_conviction is not None:
            out["tests"]["model_by_conviction"]["acted"] = order_changed_days(by_conviction, model)
        sized = next((f for f in explore if f.name == "model_sized"), None)
        if sized is not None:
            out["tests"]["model_sized"]["acted"] = sized_trades_scaled(sized)
    if rates is not None:
        from shadow import after_tax as tax

        series = {f.name: tax.fund_series(f, f.bars, rates.rate) for f in [*four, *explore, *tests, *voting]}
        out["after_tax"] = {f.name: tax.view(series[f.name]) for f in four}
        out["_after_tax_series"] = series
        out["_after_tax_coverage"] = price_coverage(cycles, bars, start, final_through)
    if tests:
        by_name = {f.name: f for f in four}
        out["tests"] |= {f.name: paired(f, by_name[xp.COMPARED_WITH[f.name]]) for f in tests}
        out["tests"][xp.TIMING]["switches"] = tests[1].switches
        out["tests"][xp.LIMIT]["orders"] = {k: v for k, v in vars(tests[2].pullback).items()
                                            if k not in ("filled", "considered")}
        out["tests"][xp.LIMIT]["acted"] = xp.pullback_acted(tests[2], by_name["momentum"])
    if voting:
        from shadow import vote as sv

        # The vote against the single call on the same lines, from the sessions after its first cycle;
        # "acting differently" is counted on the lines, exactly as the race arm counts it.
        vote_fund, comparator = voting
        out.setdefault("tests", {})[mv.ARM] = paired(vote_fund, comparator, after=mv.START) | {
            "acted": sv.acted(sv.lines_with_an_answer(entries, votes), votes)}
    # The fund test's own numbers at a look (section 11.6, ``fund_test_part``):
    # the four funds, to pair cut at the look's close, and the coin-flip funds'
    # raw equity, session by session, for the 95th percentile of their total
    # returns (not the band, which is rounded to cents). ``build`` takes this
    # out before anything is printed.
    if fund_test:
        out["_fund_test"] = {"funds": {f.name: f for f in four}, "coin": curves}
    return out, {"four": check, "coin": coin_check}


def exploratory_counters(entries: Sequence[JournalEntry], long_bars: Bars, final_through: date) -> dict:
    """Everything shown about the exploratory tests between checkpoints (section 13.1): counters, no result.

    Counted from the journal and the prices alone; no fund is built. For
    ``model_same_day``, the directional lines from the first cycle it could
    not have entered, by reason (the check ``shadow.fund.recorded_fill``
    makes); nothing else of the three exploratory funds is shown between
    checkpoints.
    """
    from shadow.fund import recorded_fill

    first = schedule.FUND_FIRST_CYCLE
    cycles = lines_by_day(entries)
    unusable: dict[str, int] = {key: 0 for key in NOT_ENTERED_KEYS.values()}
    for day, lines in cycles.items():
        if day < first:
            continue
        for line in lines:
            signal = model_signal(line)
            if signal is None or signal.bias.value == "NEUTRAL":
                continue
            _, why = recorded_fill(line.entry, "buy" if signal.bias.value == "BULLISH" else "sell", day)
            if why is not None:
                unusable[NOT_ENTERED_KEYS[why]] += 1
    return {
        xp.VETO: xp.veto_counters(cycles, long_bars, first),
        xp.TIMING: xp.timing_counters(long_bars, final_through),
        xp.LIMIT: xp.pullback_counters(cycles, long_bars, first, final_through),
        "model_same_day": {"lines_without_usable_price": unusable},
    }


def long_history(entries: Sequence[JournalEntry], final_through: date, fetcher) -> Bars:
    """Closes far enough back for A's 200-day average and B's 10 month-ends, from their own fetcher."""
    first = schedule.FUND_FIRST_CYCLE
    tickers = {e.ticker for e in entries if e.timestamp is not None and e.timestamp.date() >= first}
    return Bars.fetch(tickers | {xp.TIMING_IN, xp.TIMING_OUT}, first - timedelta(days=xp.LONG_LEAD_DAYS),
                      final_through, fetcher)


def checkpoint_race(entries: Sequence[JournalEntry], long_bars: Bars, today: date, final_through: date,
                    fetchers: Optional[list] = None, votes: Optional[Mapping] = None) -> dict:
    """A's race arm, the insider arm's test and C's filled against missed, at a checkpoint (section 13).

    With ``votes`` (the voting arm's answers, given only on a checkpoint
    night from 2026-12-22), also the vote's race arm against the model's
    single call on the same lines (section 13.11, ``shadow.vote.race``),
    with the same price sources.
    """
    from analysis import decision_gate as gate

    lines = [e for e in entries if e.timestamp is not None and e.model_answered]
    how = xp.race_settings(today, final_through, lines)
    if fetchers is not None:
        fetchers += [("race_closes", how.source), ("race_ohlc", how.fetcher)]
    out = xp.race_tests(lines, long_bars, how, schedule.FUND_FIRST_CYCLE, gate.DECISION_CUTOFF)
    if votes is not None:
        from shadow import vote as sv

        out[mv.ARM] = sv.race(lines, votes, how)
    return out


#: Every test of the family (section 13.5), by where its numbers are in a
#: look's record, and where its count of "acting differently" is (13.7):
#: None for the ideas that differ on every trade and so always act.
FAMILY: Final[tuple[tuple[str, str, str, Optional[tuple[str, ...]]], ...]] = (
    ("insider arm", "race", "insiders", ("race", "insiders", "trades")),
    ("A, race arm", "race", xp.VETO, ("counters", xp.VETO, "vetoed")),
    ("A, fund", "tests", xp.VETO, ("counters", xp.VETO, "vetoed")),
    ("B, fund", "tests", xp.TIMING, ("counters", xp.TIMING, "days_out_of_vt")),
    ("C, fund", "tests", xp.LIMIT, ("tests", xp.LIMIT, "acted")),
    ("model_by_conviction", "tests", "model_by_conviction", ("tests", "model_by_conviction", "acted")),
    ("model_sized", "tests", "model_sized", ("tests", "model_sized", "acted")),
    ("model_same_day", "tests", "model_same_day", None),
    # Section 13.9 (prepared 2026-10-02, registered at the 2026-12-22
    # checkpoint): the IC report's primary test, one per universe (the
    # blended score's IC at 1 session, the owner's decision of 3 Oct 2026),
    # from the checkpoint record it is first made in. These two are the only
    # IC members of the family; the other IC numbers are descriptive. A
    # universe with no data yet is left out of the family, as 13.5 says;
    # "acting" is a day with an IC.
    ("IC, production names", "ic_main", "production", ("ic_main", "production", "days")),
    ("IC, shadow stock universe", "ic_main", "shadow", ("ic_main", "shadow", "days")),
    # Section 13.11 (prepared 2026-10-04, registered at the 2026-12-22
    # checkpoint, one trial in N): the voting arm, as a race arm (lag 3) and
    # as a fund (lag 5), each against the model's single call on the same
    # lines. "Acting" is a line where the two signals differ. Its look
    # records carry it only from 2026-12-22; a record without it is left out
    # of the family, as 13.5 says.
    ("model_vote, race arm", "race", mv.ARM, ("race", mv.ARM, "acted")),
    ("model_vote, fund", "tests", mv.ARM, ("tests", mv.ARM, "acted")),
)
#: The last planned look, the minimum of "acting differently", and B, whose
#: purpose (crash protection) the final "zero or below" rule does not judge.
FINAL_LOOK: Final[int] = 3
MIN_ACTED: Final[int] = 20
NO_ZERO_RULE: Final[frozenset[str]] = frozenset({"B, fund"})
#: Family members that exist only from a date: a look's table made before it
#: does not list them at all, not even as "no data" (the owner's rule of
#: 4 Oct 2026: nothing of a new idea is shown before its registration date).
FAMILY_FROM: Final[dict[str, date]] = {"model_vote, race arm": mv.START, "model_vote, fund": mv.START}


def outcome(row: dict, mean: Optional[float], acted: Optional[int], final: bool, zero_rule: bool) -> str:
    """Section 13.7: promising, dead, not tested or not proven -- read by code, never by a person."""
    if final and acted is not None and acted < MIN_ACTED:
        return "not tested"
    if row.get("passes_bh") and row.get("t") is not None:
        return "promising" if row["t"] > 0 else "dead"
    if final and zero_rule and mean is not None and mean <= 0:
        return "dead"
    return "no data" if row.get("no_data") else "not proven"


def checkpoint_table_for(record: dict) -> dict:
    """Benjamini-Hochberg across the family, the Deflated Sharpe Ratio with N from the graveyard, and each outcome."""
    from analysis.multiple_tests import checkpoint_table, graveyard_n

    n = graveyard_n()
    final = record.get("look") == FINAL_LOOK
    try:
        made = date.fromisoformat(record["made_on"]) if isinstance(record.get("made_on"), str) else None
    except ValueError:
        made = None
    tests, extra = [], []
    for label, part, key, where in FAMILY:
        if made is not None and label in FAMILY_FROM and made < FAMILY_FROM[label]:
            continue
        found = (record.get(part) or {}).get(key) or {}
        tests.append({"name": label, "t": found.get("t"), "stats": found.get("stats")})
        acted = None
        if where is not None:
            value = (((record.get(where[0]) or {}).get(where[1])) or {}).get(where[2])
            acted = value if isinstance(value, int) and not isinstance(value, bool) else 0
        extra.append((found.get("mean_daily_diff"), acted, label not in NO_ZERO_RULE))
    rows = checkpoint_table(tests, n)
    for row, (mean, acted, zero_rule) in zip(rows, extra):
        row["acted_differently"] = acted
        row["outcome"] = outcome(row, mean, acted, final, zero_rule)
    return {"n_trials": n, "final": final, "rows": rows}


def load_rates(path: Optional[Path]) -> tuple[Optional[object], dict]:
    """The night's shekel rate table (``analysis.boi_rates``'s tape), and what the document says about it.

    Read from the file the workflow's rate step wrote; nothing is fetched
    here. No file, or one that does not check out, means no after-tax or
    shekel view tonight, said in so many words -- never a guessed rate.
    """
    from analysis import boi_rates

    if path is None:
        return None, {"available": False, "reason": "no rate table was given"}
    if not Path(path).is_file():
        return None, {"available": False, "reason": "tonight's rate step wrote no table; the run's log says why"}
    try:
        text = Path(path).read_text(encoding="utf-8")
        table = boi_rates.load_tape(text)
        tape = json.loads(text)
    except (OSError, ValueError, KeyError) as exc:
        return None, {"available": False, "reason": f"the rate table could not be read: {exc}"}
    counts = table.counts()
    return table, {
        "available": True, "source": tape.get("source"), "first": table.first.isoformat(),
        "last": table.last.isoformat(), "counts": counts,
        "fallback_days": [[d.isoformat(), src] for d, src in table.fallback_days()],
        "rates_sha256": tape.get("prices_sha256"),
    }


def after_tax_part(now: datetime, final_through: date, snapshots, funds: Optional[dict], passed: bool,
                   race_gate: Optional[dict], records: list, fetchers: Optional[list],
                   rates, fx: dict) -> tuple[dict, Optional[dict]]:
    """Everything after Israeli tax and in shekels (pre-registration sections 5c and 11.9).

    * the paper account's view, every night (it is the account, not a fund result);
    * the four funds' views, once calibration has passed (``funds["after_tax"]``);
    * each planned look's after-tax test against the VT fund, made once, on
      the first night from the night the race reaches the look on which the
      look is readable, and carried unchanged after: with funds when
      calibration has passed, the rate table is there and the funds' own
      prices reach the look's last close (every name a cycle named by then,
      ``missing_prices``); "unavailable" when calibration has not passed; no
      record (the look waits) otherwise. A ready record cut at another close
      (a bug fix re-ran the race and moved the look's window) is made again
      at the new close on the first night the same conditions hold, and the
      old one is kept inside it under ``superseded``;
    * the break-even of an actively traded fund against VT held 20 years,
      for information only.
    """
    from analysis import decision_gate as gate
    from analysis import tax_breakeven
    from shadow import after_tax as tax
    from shadow import calibration as calib

    paper, problem = None, None
    if rates is not None:
        fetcher = OhlcFetcher(final_through=final_through)
        if fetchers is not None:
            fetchers.append(("ohlc_tax", fetcher))
        tickers = {f.ticker for f in calib._all_fills(snapshots)}
        try:
            bars = Bars.fetch(tickers, tax.FX_TABLE_START, final_through, fetcher)
            paper = tax.view(tax.account_series(snapshots, bars, rates.rate, final_through))
        except (KeyError, ValueError) as exc:
            problem = f"the paper account could not be reckoned: {exc}"
    series = (funds or {}).pop("_after_tax_series", None)
    coverage = (funds or {}).pop("_after_tax_coverage", None)
    for look in looks_reached(race_gate):
        entry = (race_gate.get("looks") or [])[look - 1]
        if entry.get("readable") is not True:
            continue                        # the race could not read the look tonight: it waits, and so does this
        old = next((r for r in records if r.get("look") == look), None)
        if old is not None and (old.get("status") != gate.AFTER_TAX_READY
                                or old.get("window_end") in (None, entry.get("window_end"))):
            continue                        # made once, carried unchanged
        end = date.fromisoformat(entry["window_end"]) if entry.get("window_end") else None
        if old is None and not passed:
            records.append(tax.gate_record(look, now.date(), end, None, reason=(
                "calibration had not passed when the race reached this look: no fund was run")))
        elif passed and series is not None and end is not None and all(
                series.get(name) is not None and series[name].days and series[name].days[-1].day >= end
                for name in (*tax.GATE_FUNDS, tax.VT_FUND)) and missing_prices(coverage, end) == []:
            record = tax.gate_record(look, now.date(), end, series)
            if old is not None:
                records.remove(old)
                record["superseded"] = old
            records.append(record)
        # Otherwise no record tonight (no rate table, or the funds' prices do
        # not reach the look's last close yet): the look waits for the first
        # night that has both, and the test is cut at the same close then.
    return {
        "rules": tax.rules_json(),
        "fx": fx,
        "paper": paper,
        "paper_problem": problem,
        "paper_lots": tax.account_lot_check(snapshots),
        "funds": (funds or {}).pop("after_tax", None),
        "looks": records,
        "breakeven": tax_breakeven.breakeven() | {"note": "for information only; not a gate"},
    }, series


# --------------------------------------------------------------------------- #
# The fund test's verdict at each look (sections 11.5-11.8; the owner's
# approval of the checkpoint verdict, 6 Oct 2026)
# --------------------------------------------------------------------------- #


def _after_tax_for(look: int, end: str, tax_records: Sequence[dict]) -> Optional[dict]:
    """Look ``look``'s after-tax record tonight, as the fund test reads it; None while there is none.

    A ready record counts only if it was cut at the look's own close (the
    race's rule, section 5c); an unavailable one counts as it is (it is
    never made again).
    """
    from analysis import decision_gate as gate

    record = next((r for r in tax_records if r.get("look") == look), None)
    if record is None:
        return None
    if record.get("status") == gate.AFTER_TAX_READY:
        if record.get("window_end") != end:
            return None
        tests = record.get("tests") or {}
        return {"status": gate.AFTER_TAX_READY,
                "t": {arm: (tests.get(arm) or {}).get("t") for arm in ("model", "momentum", "hybrid")}}
    return {"status": gate.AFTER_TAX_UNAVAILABLE, "t": {}, "reason": record.get("reason") or "no fund was run"}


def _read_looks(records: Sequence[dict], before: int) -> list[tuple[float, float]]:
    """``(share, bar used)`` of every look read before checkpoint ``before``, in order: the spending rule's past."""
    return [(r["share"], r["bar"]) for r in sorted(records, key=lambda r: r["look"])
            if r.get("status") == "read" and r["look"] < before]


def _first_decision(records: Sequence[dict], before: int = 4) -> Optional[int]:
    """The first checkpoint before ``before`` whose fund-test record decided; None if none did."""
    for record in sorted(records, key=lambda r: r["look"]):
        if record["look"] >= before:
            break
        if record.get("status") == "read" and (record.get("decision") or {}).get("outcome") is not None:
            return record["look"]
    return None


def _planned_next(look: int, read: Sequence[tuple[float, float]]) -> Optional[tuple[int, date, float]]:
    """``(checkpoint, planned day, planned bar)`` of the fund test's look after ``look``, by the spending rule."""
    from analysis import verdict

    later = verdict.planned_fund_bars(read, after_look=look)
    if not later or later[0][0] != look + 1:
        return None
    return look + 1, schedule.FUND_TEST_LOOK_ESTIMATES[look], later[0][1]


def fund_test_record(look: int, made_on: date, end: date, days: Sequence[str], raw: dict, after_tax: dict,
                     downturn: Optional[float], records: Sequence[dict],
                     calibration_passed_on: Optional[str]) -> dict:
    """One look of the fund test, read (section 11.6), as the record ``fund_test.looks`` keeps.

    Everything through the race look's last close ``end`` only (5c, 11.7):
    the funds' own sessions from the fixed start (``schedule.FUND_START``)
    through ``end``; the bar by the spending rule of 11.7 from the looks
    actually read (``spending_bars`` with the bars already used kept as
    they were, ``used=``; a skipped look spends nothing), rounded up; the
    six paired before-tax tests of the four funds, Newey-West lag 5, cut at
    ``end`` (``paired(..., through=end)``); the coin flip (11.5): the model
    fund's total return since the start against the 95th percentile of the
    coin-flip funds' total returns, both from the raw equity; the race's
    after-tax record for the look (5c), at the fund test's own bar; the
    race's downturn number (5d, owner reading 4). The decision is
    ``decision_gate.decide`` at that bar ("exactly as section 5a").

    A look before the final one with 180 or more fund sessions is not
    decided: its share would reach 1 before the final look, and the
    spending rule has no bar for it; the record says the owner decides.
    Raises ``ValueError`` for a date outside the experiment (owner
    Addition 2: the 2099 examples can never become a real record).
    """
    from analysis import decision_gate as gate
    from analysis import verdict
    from shadow.fund_test import sessions_through

    verdict.check_dates(made_on, end, calibration_passed_on, schedule.FUND_START)
    sessions = sum(1 for d in days if date.fromisoformat(d) <= end)
    final = look == verdict.LOOKS
    base = {"look": look, "made_on": made_on.isoformat(), "window_end": end.isoformat(),
            "start": schedule.FUND_START.isoformat()}
    read = _read_looks(records, look)
    share = 1.0 if final else min(1.0, sessions / verdict.FUND_PLANNED_SESSIONS)
    owner = None
    if not final and sessions >= verdict.FUND_PLANNED_SESSIONS:
        owner = verdict.FUND_OWNER_REASON
    else:
        try:
            exact = gate.spending_bars([s for s, _ in read] + [share], used=[b for _, b in read])[-1]
        except ValueError as error:
            owner = f"the spending rule of 11.7 gives no bar here ({error}): the owner decides"
    if owner is not None:
        record = base | {"status": verdict.FUND_OWNER, "reason": owner, "sessions": sessions,
                         "sessions_calendar": sessions_through(schedule.FUND_START, end)}
        record["table"] = verdict.table_json(verdict.fund_test_table(record))
        return record
    bar = gate.rounded_bar(exact)
    planned_bar = schedule.FUND_TEST_BARS[look - 1]
    funds = raw["funds"]
    tests = {}
    for first, second in verdict.FUND_TEST_PAIRS:
        test = paired(funds[first], funds[second], through=end)
        tests[verdict.fund_pair(first, second)] = {
            "days": test["days"], "from": test["from"], "through": test["through"], "t": test["t"],
            "mean_daily_diff": test["mean_daily_diff"], "lag": VS_MODEL_LAG}
    at = days.index(end.isoformat())
    model_equity = {d.day: d.equity for d in funds["model"].days}[end]
    coin = [curve[at] / STARTING_CASH - 1.0 for curve in raw["coin"] if len(curve) > at]
    coin_flip = {"model_total": model_equity / STARTING_CASH - 1.0, "p95_total": percentile(coin, 95.0),
                 "funds": len(raw["coin"])}
    t = {arm: tests[verdict.fund_pair(arm, "vt")]["t"] for arm in ("model", "momentum", "hybrid")}
    tax = after_tax.get("t") or {}
    inputs = gate.LookInputs(
        entry_days=sessions,
        t_model_momentum=tests["model-momentum"]["t"], t_model_hybrid=tests["model-hybrid"]["t"],
        t_hybrid_momentum=tests["hybrid-momentum"]["t"],
        model_mean=coin_flip["model_total"], model_band_high=coin_flip["p95_total"], t_vs_index=t,
        after_tax=gate.AfterTax(after_tax["status"], dict(tax), after_tax.get("reason") or ""),
        vt_max_drawdown=downturn, window_end=end,
    )
    candidate, outcome, reason = gate.decide(inputs, bar, final)
    record = base | {
        "status": verdict.FUND_READ, "sessions": sessions,
        "sessions_calendar": sessions_through(schedule.FUND_START, end), "share": share, "bar": bar,
        "bar_exact": round(exact, 4), "planned_bar": planned_bar, "bar_differs": bar != planned_bar,
        "calibration_passed_on": calibration_passed_on, "tests": tests, "coin_flip": coin_flip,
        "after_tax": after_tax, "downturn": downturn,
        "decision": {"candidate": candidate, "outcome": outcome, "reason": reason},
    }
    record["table"] = verdict.table_json(verdict.fund_test_table(
        record, planned_next=None if final else _planned_next(look, [*read, (share, bar)]),
        decided_at=_first_decision(records, look)))
    return record


def fund_test_part(now: datetime, race_gate: Optional[dict], records: list, passed: bool,
                   funds: Optional[dict], raw: Optional[dict], tax_records: Sequence[dict],
                   calibration: dict) -> Optional[str]:
    """Each planned look's fund-test record, made once and frozen (sections 11.6-11.7; owner readings 2 and 3).

    ``records`` is last night's ``fund_test.looks``, carried unchanged; this
    adds tonight's. A look's record is made on a night the race's look is
    reached and readable and no record for it exists (or the one there was
    cut at another close: a bug fix moved the window; it is made again and
    the old one kept inside it under ``superseded``):

    * **skipped** when calibration has not passed that night (owner reading
      3: judged on the first night the look is readable, as the race's
      "unavailable" after-tax record is): not read, nothing spent, no bar.
      Never made again;
    * **read** (``fund_test_record``) when calibration has passed, the funds
      reach the look's last close, and the race's after-tax record for the
      look exists tonight (ready, cut at that close, or unavailable);
    * otherwise no record tonight: the look waits, and is cut at the same
      close on the first night all that holds. A later look waits for an
      earlier one (the spending rule reads the looks in order).

    A run with fewer coin-flip funds than the registered 1,000 (a run by
    hand; 11.1, 11.5) makes no read record and returns why, for
    ``fund_test.note``; otherwise returns None.
    """
    from analysis import verdict

    looks = race_gate.get("looks") if isinstance(race_gate, dict) else None
    days = (funds or {}).get("days") or []
    note = None
    for look in looks_reached(race_gate):
        entry = looks[look - 1]
        end_text = entry.get("window_end")
        old = next((r for r in records if r.get("look") == look), None)
        if old is not None and (old.get("status") == verdict.FUND_SKIPPED
                                or old.get("window_end") in (None, end_text)):
            continue                        # made once, carried unchanged
        if entry.get("readable") is not True or not end_text:
            break                           # the race cannot read the look tonight: it waits, and so does this
        end = date.fromisoformat(end_text)
        if not passed:
            if old is not None:
                break
            verdict.check_dates(now.date(), end)
            record = {"look": look, "made_on": now.date().isoformat(), "window_end": end_text,
                      "status": verdict.FUND_SKIPPED, "reason": verdict.FUND_SKIP_REASON}
            record["table"] = verdict.table_json(verdict.fund_test_table(record, read_before=_read_looks(records,
                                                                                                    look)))
            records.append(record)
            continue
        after_tax = _after_tax_for(look, end_text, tax_records)
        if (raw is None or end_text not in days or after_tax is None
                or not all(any(d.day == end for d in fund.days) for fund in raw["funds"].values())):
            break                           # the funds do not reach the close yet, or the after-tax record waits
        if len(raw["coin"]) < schedule.RANDOM_FUNDS:
            note = (f"checkpoint {look}: this run had {len(raw['coin']):,} coin-flip funds, not the registered "
                    f"{schedule.RANDOM_FUNDS:,} (sections 11.1 and 11.5), so no fund-test record was made")
            break
        passed_on = calibration.get("end_estimate") if isinstance(calibration.get("end_estimate"), str) else None
        record = fund_test_record(look, now.date(), end, days, raw, after_tax, entry.get("vt_max_drawdown"),
                                  [r for r in records if r is not old], passed_on)
        if old is not None:
            records.remove(old)
            record["superseded"] = old
        records.append(record)
    records.sort(key=lambda r: r["look"])
    return note


def carried_fund_looks(previous: Optional[dict]) -> list[dict]:
    """Last night's ``fund_test.looks``, carried unchanged (owner reading 2); a damaged record is left out.

    A record is kept only if it is a dict with a checkpoint number 1 to 3, a
    known status, and -- for a read look -- the share and bar the spending
    rule reads back. A record left out is made again, as if it never was.
    """
    from analysis import verdict

    part = (previous or {}).get("fund_test")
    looks = part.get("looks") if isinstance(part, dict) else None
    out, seen = [], set()
    for record in looks if isinstance(looks, list) else []:
        if not isinstance(record, dict):
            continue
        look = record.get("look")
        if not isinstance(look, int) or isinstance(look, bool) or not 1 <= look <= verdict.LOOKS or look in seen:
            continue
        status = record.get("status")
        if status not in (verdict.FUND_READ, verdict.FUND_SKIPPED, verdict.FUND_OWNER):
            continue
        if status == verdict.FUND_READ and not all(
                isinstance(record.get(k), (int, float)) and not isinstance(record.get(k), bool)
                for k in ("share", "bar")):
            continue
        seen.add(look)
        out.append(record)
    return sorted(out, key=lambda r: r["look"])


def fund_test_verdict(records: Sequence[dict]) -> dict:
    """``fund_test.verdict``: the first deciding look's verdict, frozen with it; else "no decision yet"."""
    from analysis import verdict

    for record in sorted(records, key=lambda r: r["look"]):
        table = record.get("table") or {}
        if table.get("status") == verdict.DECIDED:
            return {"text": table["verdict"], "decided_at": record["look"], "outcome": table.get("outcome")}
    return {"text": verdict.NO_DECISION_YET, "decided_at": None, "outcome": None}


def fund_test_next(records: Sequence[dict]) -> Optional[dict]:
    """``fund_test.next_checkpoint``: the next look with no record, its planned day and its bar.

    The bar by the spending rule of 11.7 from the looks read so far and the
    planned sessions (60, 120, 180); ``planned_bar`` is the registered one
    (``schedule.FUND_TEST_BARS``). None once every look has a record.
    """
    from analysis import verdict

    done = {r["look"] for r in records}
    upcoming = next((k for k in range(1, verdict.LOOKS + 1) if k not in done), None)
    if upcoming is None:
        return None
    later = verdict.planned_fund_bars(_read_looks(records, upcoming), after_look=upcoming - 1)
    bar = later[0][1] if later and later[0][0] == upcoming else None
    return {"look": upcoming, "estimated": schedule.FUND_TEST_LOOK_ESTIMATES[upcoming - 1].isoformat(),
            "bar": bar, "planned_bar": schedule.FUND_TEST_BARS[upcoming - 1]}


def combined_verdict(race_gate: Optional[dict], records: Sequence[dict], fund_verdict: dict,
                     next_checkpoint: Optional[dict]) -> dict:
    """The document's top-level ``verdict``: the race's and the fund test's verdicts combined (section 11.8).

    Owner reading 1: each test is frozen at its own first deciding look, an
    early answer is final, and section 9 only delays the money. The race's
    side is tonight's race gate (its ``verdict``); the fund test's is its
    records. Before any look of either: ``{"text": "no decision yet"}``.
    """
    from analysis import decision_gate as gate
    from analysis import verdict

    def inside(day) -> Optional[str]:
        try:
            value = verdict.as_date(day)
        except ValueError:
            return None
        return day if verdict.inside_experiment(value) else None

    looks = race_gate.get("looks") if isinstance(race_gate, dict) else None
    reached = looks_reached(race_gate)
    race_part = race_gate.get("verdict") if isinstance(race_gate, dict) else None
    race_part = race_part if isinstance(race_part, dict) else {}
    decided_at = race_part.get("decided_at")
    decided_at = decided_at if isinstance(decided_at, int) and not isinstance(decided_at, bool) else None
    outcome, final_read = None, False
    for entry in race_part.get("looks") or []:
        table = entry.get("table") if isinstance(entry, dict) else None
        if not isinstance(table, dict):
            continue
        if entry.get("look") == decided_at:
            outcome = table.get("outcome")
        if entry.get("look") == verdict.LOOKS and table.get("complete") is True:
            final_read = True
    upcoming = race_gate.get("next") if isinstance(race_gate, dict) else None
    race_next = None
    if isinstance(upcoming, dict) and upcoming.get("independent") in [d for d, _ in gate.CHECKPOINTS]:
        race_next = {"look": [d for d, _ in gate.CHECKPOINTS].index(upcoming["independent"]) + 1,
                     "estimated": inside(upcoming.get("estimated"))}
    race_look = max(reached) if reached else None
    race = {"decided_at": decided_at if outcome is not None else None, "outcome": outcome,
            "final_read": final_read, "skipped_all": False, "look": race_look,
            "window_end": inside((looks[race_look - 1] or {}).get("window_end")) if race_look else None,
            "next": race_next}
    latest = max(records, key=lambda r: r["look"]) if records else None
    fund = {"decided_at": fund_verdict.get("decided_at"), "outcome": fund_verdict.get("outcome"),
            "final_read": any(r["look"] == verdict.LOOKS for r in records),
            "skipped_all": bool(records) and all(r.get("status") == verdict.FUND_SKIPPED for r in records),
            "look": latest["look"] if latest else None,
            "window_end": inside(latest.get("window_end")) if latest else None,
            "next": ({"look": next_checkpoint["look"], "estimated": next_checkpoint["estimated"]}
                     if next_checkpoint else None)}
    return verdict.combined(race, fund)


def ic_lines(journal: Path, universe_dir: Optional[Path]) -> dict:
    """The IC report's answered lines, per universe (section 13.9): the production journal and the shadow universe's."""
    from analysis import ic

    return {"production": ic.read_universe(journal),
            "shadow": ic.read_universe(universe_dir) if universe_dir is not None else []}


def ic_record(lines: dict, final_through: date, fetchers: Optional[list]) -> dict:
    """The IC report's checkpoint record, once (``analysis.ic.record``), and the main tests the family reads."""
    from analysis import ic

    bars = {}
    for universe, found in lines.items():
        window = ic.in_window(found, universe, final_through)
        if not window:
            continue
        fetcher = OhlcFetcher(final_through=final_through)
        if fetchers is not None:
            fetchers.append((f"ohlc_ic_{universe}", fetcher))
        first = min(line.day for line in window)
        bars[universe] = ic.bars_from_fetcher(fetcher, ic.tickers_of(window), first - timedelta(days=45),
                                              final_through)
    made = ic.record(lines, bars, final_through)
    return made


def vote_lines_in(path: Optional[Path]) -> dict:
    """The voting arm's lines (``logs/model_vote``), by production line; none without a path.

    Read only from 2026-12-22 (``build``): before it, nothing of the vote is
    read, let alone computed. No path means no lines, as with ``--universe``.
    """
    from analysis import vote as model_vote

    return model_vote.read_votes(path) if path is not None else {}


def thesis_lines_in(path: Optional[Path]) -> list:
    """The thesis check's lines (``logs/thesis_check``); none without a path. Read only from 2027-04-01."""
    from analysis import thesis as thesis_check

    return thesis_check.read_checks(path) if path is not None else []


def vote_ic_record(entries: Sequence[JournalEntry], lines: Mapping, final_through: date,
                   fetchers: Optional[list]) -> dict:
    """Section 13.11's secondary number, once at a look: the vote score's daily IC minus the single call's.

    Descriptive only (``analysis.vote.ic_comparison``): no ``main``, not in
    the family. The bars are fetched for the names with a vote answer, from
    45 days before the first one, with a fetcher of its own, as the IC
    report fetches its own (``ic_record``).
    """
    from analysis import ic
    from analysis import vote as model_vote

    found = model_vote.answers(lines, start=mv.START, through=final_through)
    bars: dict = {}
    if found:
        fetcher = OhlcFetcher(final_through=final_through)
        if fetchers is not None:
            fetchers.append(("ohlc_vote_ic", fetcher))
        first = min(key[1].date() for key in found)
        bars = ic.bars_from_fetcher(fetcher, sorted({key[0] for key in found}), first - timedelta(days=45),
                                    final_through)
    return model_vote.ic_comparison(entries, lines, bars, final_through)


def thesis_record(lines: Sequence, final_through: date, fetchers: Optional[list], final: bool) -> dict:
    """Section 13.12 at a look, once: what came after the thesis check's BROKEN and VALID verdicts.

    A description only (``analysis.thesis.checkpoint``), never in the
    family. The bars come through a fetcher of its own, from the first check
    with a verdict. ``final``: the last planned look, where too few BROKEN
    checks read "not tested".
    """
    from analysis import ic
    from analysis import thesis as thesis_check

    names = thesis_check.tickers_of(lines, final_through)
    bars: dict = {}
    if names:
        fetcher = OhlcFetcher(final_through=final_through)
        if fetchers is not None:
            fetchers.append(("ohlc_thesis", fetcher))
        first = min(c.day for c in thesis_check.one_per_name_and_week(thesis_check.in_window(lines, final_through)))
        bars = ic.bars_from_fetcher(fetcher, names, first, final_through)
    return thesis_check.checkpoint(lines, bars, final_through, final=final)


def vt_bars(long_bars: Bars, final_through: date) -> list[tuple[date, float, float, float]]:
    """VT's ``(day, open, close, dividend)`` from the long history: the regime split's market and the race's index."""
    frame = long_bars.history(xp.TIMING_IN, final_through)
    out = []
    for day in (ts.date() for ts in frame.index):
        bar = long_bars.bar(xp.TIMING_IN, day)
        if bar is not None:
            out.append((day, bar[0], bar[3], bar[4]))
    return out


def regime_counters(long_bars: Bars, final_through: date) -> dict:
    """Pre-registration section 13.10, between checkpoints: sessions per market state since the fund start, nothing else."""
    from analysis import regimes

    bars = vt_bars(long_bars, final_through)
    sessions = [d for d, *_ in bars if schedule.FUND_START <= d <= final_through]
    return regimes.counters(regimes.labels([(d, c) for d, _, c, _ in bars], sessions, regimes.VOL_CUTOFFS))


def checkpoint_regimes(entries: Sequence[JournalEntry], long_bars: Bars, today: date, final_through: date,
                       funds: Optional[dict], fetchers: Optional[list] = None) -> dict:
    """Section 13.10 at a checkpoint: the race's and the funds' results split by VT's market state, once.

    The race side: each main arm's mean daily net return per entry day over
    the decision window (``horse_race``'s own scoring), each against VT's own
    3-session window and against each other. The fund side, once the funds
    run: each main fund's daily return and each against the VT fund.
    Descriptive only (``analysis.regimes``).
    """
    from analysis import decision_gate as gate
    from analysis import regimes
    from analysis.horse_race import daily_net, entries_for_arm, on_grid

    lines = [e for e in entries if e.timestamp is not None and e.model_answered
             and gate.in_window(e.timestamp.date())]
    how = xp.race_settings(today, final_through, lines)
    if fetchers is not None:
        fetchers += [("race_closes_regimes", how.source), ("race_ohlc_regimes", how.fetcher)]
    daily = {name: daily_net(xp.arm_trades(name, entries_for_arm(name, lines), how))
             for name in ("model", "momentum", "hybrid")}
    grid = sorted(set().union(*(set(d) for d in daily.values())))
    race = {name: dict(zip(grid, on_grid(values, grid))) for name, values in daily.items()}
    bars = vt_bars(long_bars, final_through)
    vt = {day: r for day in grid if (r := gate.index_window_return(bars, day, gate.REGISTERED_HORIZON)) is not None}
    for name in ("model", "momentum", "hybrid"):
        race[f"{name} - vt"] = {d: race[name][d] - vt[d] for d in grid if d in vt}
    race["model - momentum"] = {d: race["model"][d] - race["momentum"][d] for d in grid}
    race["model - hybrid"] = {d: race["model"][d] - race["hybrid"][d] for d in grid}
    fund_series: dict = {}
    sessions: list[date] = []
    if funds:
        sessions = [date.fromisoformat(d) for d in funds.get("days") or []]
        for row in funds.get("list") or []:
            equity = [STARTING_CASH] + list(row.get("equity") or [])
            if len(equity) == len(sessions) + 1:
                fund_series[row["name"]] = {d: (a / b - 1.0 if b else 0.0)
                                            for d, b, a in zip(sessions, equity, equity[1:])}
        for name in ("model", "momentum", "hybrid"):
            if name in fund_series and "vt" in fund_series:
                fund_series[f"{name} - vt"] = {d: fund_series[name][d] - fund_series["vt"][d] for d in sessions}
    labels = regimes.labels([(d, c) for d, _, c, _ in bars], sorted(set(grid) | set(sessions)), regimes.VOL_CUTOFFS)
    return regimes.record(race, fund_series, labels, regimes.VOL_CUTOFFS)


def looks_reached(race_gate: Optional[dict]) -> list[int]:
    """The race's planned looks reached so far, numbered from 1 (``logs/race_gate.json``)."""
    looks = race_gate.get("looks") if isinstance(race_gate, dict) else None
    return [i + 1 for i, look in enumerate(looks or []) if isinstance(look, dict) and look.get("reached") is True]


def _read_json(path: Optional[Path]) -> Optional[dict]:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8")) if path else None
    except (OSError, ValueError):
        return None
    return value if isinstance(value, dict) else None


def build(args: argparse.Namespace, now: datetime, fetchers: Optional[list] = None) -> dict:
    """The funds document. ``fetchers``, when given, receives the price fetchers the run used, as
    ``(name, fetcher)``, so ``main`` can hand over its prices without a second fetch (``--with-prices``):
    the funds' own (``ohlc``) and the longer history tests A and B read (``ohlc_long``)."""
    from shadow import calibration as calib

    final_through = last_final_session(now)
    read = read_journal(args.journal)
    audit_lines = _read_lines(args.audit)
    snapshots = calib.load_snapshots(_read_lines(args.account))
    shortable_no = not_shortable(audit_lines)
    fetcher = OhlcFetcher(final_through=final_through)
    if fetchers is not None:
        fetchers.append(("ohlc", fetcher))
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

    # The hard gate (the owner's decision of 26 Sep 2026): the fund start is
    # fixed, but nothing about a fund is computed until calibration's
    # verdict is a pass. Then every fund runs from the fixed start, with the
    # code as merged.
    funds, checks, fund_test_raw = None, None, None
    fund_start = schedule.FUND_START
    passed = calibration.get("status") == "passed"
    # Section 13.1: the exploratory funds and tests A, B and C only on the
    # night the race first reaches a look, and only after calibration passed;
    # a look's record is kept as it was made, night after night.
    previous = (_read_json(getattr(args, "previous", None)) or {}).get("exploratory") or {}
    records = [r for r in previous.get("checkpoints") or [] if isinstance(r, dict)]
    recorded = {r.get("look") for r in records}
    new_looks = [k for k in looks_reached(_read_json(getattr(args, "race_gate", None))) if k not in recorded]
    long_fetcher = OhlcFetcher(final_through=final_through)
    if fetchers is not None:
        fetchers.append(("ohlc_long", long_fetcher))
    long_bars = long_history(read.entries, final_through, long_fetcher)
    counters = exploratory_counters(read.entries, long_bars, final_through)
    # Section 13.9: the IC report shows counters only until the checkpoint at
    # which it is registered (2026-12-22); never an IC value before it.
    from analysis import ic

    universe_dir = getattr(args, "universe", None)
    lines_for_ic = ic_lines(args.journal, universe_dir)
    counters["ic"] = ic.counters(lines_for_ic, final_through)
    # Section 13.10: the regime split shows sessions per market state only, until the checkpoints.
    counters["regimes"] = regime_counters(long_bars, final_through)
    # Sections 13.11 and 13.12: the vote's counters from 2026-12-22, the thesis
    # check's from 2027-04-01. Before its date, an idea's lines are not read
    # and its key is not in the document at all.
    from analysis import thesis as thesis_check
    from analysis import vote as model_vote

    today = now.date()
    vote_lines = vote_lines_in(getattr(args, "votes", None)) if model_vote.active(today) else {}
    if model_vote.active(today):
        # The journal too, so an answered line with no vote record is counted ("missing").
        counters[mv.ARM] = model_vote.counters(vote_lines, final_through, read.entries)
    thesis_lines = thesis_lines_in(getattr(args, "thesis", None)) if thesis_check.active(today) else []
    if thesis_check.active(today):
        counters[tc.EVENT] = thesis_check.counters(thesis_lines, final_through)
    # The vote's answers, on a checkpoint night from 2026-12-22 only: the race
    # arm, the fund and its comparator are made from them, once, at the look.
    votes = (model_vote.answers(vote_lines, start=mv.START, through=final_through)
             if model_vote.due(bool(new_looks), today) else None)
    rates, fx = load_rates(getattr(args, "fx_table", None))
    if rates is not None and rates.last < final_through:
        # A table one session short would fail every fund's reckoning; no
        # shekel view tonight instead, said in so many words.
        rates, fx = None, {"available": False,
                           "reason": f"the rate table ends {rates.last.isoformat()}, "
                                     f"before the last final session {final_through.isoformat()}"}
    if fund_start is not None and passed and fund_start <= final_through:
        funds, checks = run_funds(read.entries, fund_start, final_through, fetcher,
                                  random_funds=args.random, processes=args.processes,
                                  shortable_no=shortable_no, first_cycle=schedule.FUND_FIRST_CYCLE,
                                  exploratory=bool(new_looks), long_bars=long_bars, rates=rates, votes=votes,
                                  fund_test=True)
        fund_test_raw = funds.pop("_fund_test", None)
        if new_looks:
            rows = [r for r in funds["list"] if r.get("exploratory")]
            records.append({"look": max(new_looks), "made_on": now.date().isoformat(),
                            "through": final_through.isoformat(), "counters": counters,
                            "funds": {r["name"]: r for r in rows}, "tests": funds.pop("tests", {})})
            funds["list"] = [r for r in funds["list"] if not r.get("exploratory")]
    elif new_looks:
        records.append({"look": max(new_looks), "made_on": now.date().isoformat(),
                        "through": final_through.isoformat(), "counters": counters,
                        "status": "calibration has not passed: counters only", "tests": {}})
    race_gate = _read_json(getattr(args, "race_gate", None))
    previous_tax = (_read_json(getattr(args, "previous", None)) or {}).get("after_tax") or {}
    tax_records = [r for r in previous_tax.get("looks") or [] if isinstance(r, dict)]
    after_tax, tax_series = after_tax_part(now, final_through, snapshots, funds, passed, race_gate,
                                           tax_records, fetchers, rates, fx)
    # The fund test's verdict (sections 11.6-11.8; the owner's approval of
    # 6 Oct 2026): each look's record made once, on the night the race's look
    # is readable, after the same night's after-tax record, and carried
    # unchanged after. Read from the funds and records above; nothing above
    # reads it.
    fund_looks = carried_fund_looks(_read_json(getattr(args, "previous", None)))
    fund_note = fund_test_part(now, race_gate, fund_looks, passed, funds, fund_test_raw, tax_records,
                               calibration)
    fund_verdict = fund_test_verdict(fund_looks)
    fund_next = fund_test_next(fund_looks)
    if new_looks:
        # The race side, and the table of section 13.5-13.6 over every test with data.
        records[-1]["race"] = checkpoint_race(read.entries, long_bars, now.date(), final_through, fetchers,
                                              votes=votes)
        # Section 13.9: the IC report, made once at the first checkpoint on or
        # after its registration (2026-12-22), and at every one after.
        if ic.due(True, now.date()):
            records[-1]["ic"] = ic_record(lines_for_ic, final_through, fetchers)
            records[-1]["ic_main"] = {u: block.get("main") or {}
                                      for u, block in records[-1]["ic"]["universes"].items()}
        # Section 13.11: the vote score's IC against the single call's, descriptive only, from 2026-12-22.
        if votes is not None:
            records[-1]["vote_ic"] = vote_ic_record(read.entries, vote_lines, final_through, fetchers)
        # Section 13.12: the thesis check's BROKEN against VALID, a description only, from 2027-04-01.
        if thesis_check.due(True, today):
            records[-1][tc.EVENT] = thesis_record(thesis_lines, final_through, fetchers,
                                                  final=max(new_looks) == FINAL_LOOK)
        records[-1]["table"] = checkpoint_table_for(records[-1])
        # Section 13.10: the regime split, once, kept with the look's record.
        records[-1]["regimes"] = checkpoint_regimes(read.entries, long_bars, now.date(), final_through, funds,
                                                    fetchers)
        # Section 11.9: the exploratory funds after tax, at checkpoints only.
        if tax_series is not None:
            from shadow import after_tax as tax

            # The vote's fund and its comparator only on a night they ran (section 13.11).
            shown = (*EXPLORATORY_FUNDS, *xp.NEW_FUNDS,
                     *(name for name in (mv.ARM, mv.COMPARATOR_FUND) if name in tax_series))
            records[-1]["after_tax"] = {name: tax.view(tax_series.get(name)) for name in shown}
        elif funds is not None:
            records[-1]["after_tax"] = {"status": f"not available: {fx.get('reason', 'no rate table')}"}
    # Not fund results: the price source's gaps and the names no fund could
    # trade, from the fund start on, whatever calibration says. After the
    # funds and calibration, so their bars are fetched as they always were.
    gaps = price_gaps(fetcher, fund_start, final_through) if fund_start is not None else None
    held = held_names(read.entries, schedule.FUND_FIRST_CYCLE)
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
            # The fund test's own next look and bar (owner reading 5), not the race's.
            "next_checkpoint": fund_next,
            "first_cycle": schedule.FUND_FIRST_CYCLE.isoformat(),
            # Why nothing is shown yet, when nothing is: the gate, not the date.
            "waiting_for": None if funds else ("calibration" if not passed else "the first session"),
            # The checkpoint verdict (owner readings 2, 3 and 5): the planned
            # final sample, each look's frozen record and table, and the
            # verdict of the first look that decided.
            "planned_sessions": schedule.FUND_TEST_PLANNED_SESSIONS[-1],
            "looks": fund_looks,
            "verdict": fund_verdict,
            "note": fund_note,
        },
        "integrity": checks,
        "not_shortable": sorted(shortable_no),
        # The day of each name's first refusal: a fund acting on a cycle of
        # day D is refused only the names refused on D or earlier.
        "not_shortable_since": ({t: (d.isoformat() if d != date.min else None) for t, d in shortable_no.items()}
                                if isinstance(shortable_no, dict) else None),
        "price_gaps": gaps,
        "held_names": held,
        # Section 13: counters between checkpoints, results only in a look's record.
        "exploratory": {"counters": counters, "checkpoints": records},
        # The real paper account's own record, always: it is the account,
        # not a fund result. The calibration fund's is in "calibration" and
        # each fund's in its own row, shown when those are.
        "order_matters": {"real": real_summary(audit_lines)},
        # Sections 5c and 11.9 (Amendment 2026-10-02): after Israeli tax and
        # in shekels; each look's after-tax test against the VT fund.
        "after_tax": after_tax,
        # Section 11.8 (owner reading 1): the race's verdict and the fund
        # test's, combined; "no decision yet" before any look. The last key,
        # so it lands just before prices_sha256.
        "verdict": combined_verdict(race_gate, fund_looks, fund_verdict, fund_next),
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
    parser.add_argument("--race-gate", type=Path, default=Path(cfg.AUDIT_LOG_PATH).parent / "race_gate.json",
                        help="the race's gate record, for the looks reached (section 13.1)")
    parser.add_argument("--previous", type=Path, default=Path(cfg.AUDIT_LOG_PATH).parent / "funds.json",
                        help="the last funds document, whose checkpoint records are carried unchanged")
    parser.add_argument("--universe", type=Path, default=None,
                        help="the shadow stock universe's journal (logs/shadow_universe), for the IC report's "
                             "second universe (pre-registration section 13.9)")
    parser.add_argument("--fx-table", type=Path, default=None,
                        help="the night's shekel rate table, as analysis.boi_rates --with-table printed it "
                             "(pre-registration sections 5c and 11.9); without it, no after-tax view")
    parser.add_argument("--votes", type=Path, default=None,
                        help="the voting arm's lines (logs/model_vote), read from 2026-12-22 only "
                             "(pre-registration section 13.11); without it, no vote lines")
    parser.add_argument("--thesis", type=Path, default=None,
                        help="the thesis check's lines (logs/thesis_check), read from 2027-04-01 only "
                             "(pre-registration section 13.12); without it, no checks")
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
        tape = price_tape.tape(used, consumer="funds",
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
