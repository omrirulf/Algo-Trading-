"""How much of the book is one bet: the monthly concentration report.

    python -m analysis.concentration --month 2026-09          # one month, JSON
    python -m analysis.concentration --month 2026-09 --text   # the same, for a person
    python -m analysis.concentration --previous --history logs/concentration.json

The owner's monthly report (27 Sep 2026). **Descriptive only**: it changes no
cap, moves no position and raises no alarm. For a month's last trading day:

* **the book's beta to VT** (world stocks). Each position's beta is the
  ordinary least-squares slope of its daily returns on VT's, over the 252
  sessions (one year) up to that day, from final closes. The book's beta is
  the sum over positions of side x market value x beta, divided by equity:
  1.0 means the book moves like all of its equity held in VT, 0 like cash.
  The long and short sides are shown apart as well. A position with fewer
  than ``MIN_RETURNS`` daily returns in the year has no beta and is listed.
* **each exposure group against its cap** (25%; Duration 30%), counted
  exactly as the risk engine counts them (``analysis.book.exposure_from``).
* **breadth**: the share of the watchlist whose final close that day is
  above the average of its last 50 final closes (that day included).
* **VT's realized volatility**: the standard deviation of VT's daily
  returns in the month, times the square root of 252.

The book is the paper account as its last snapshot of the month recorded it
(``logs/account.jsonl``, written after every heartbeat run): its positions,
their market values and the equity, in the session of that snapshot. Prices
are the raw daily closes (``auto_adjust=False``, the race's own basis), so a
dividend shows as a small drop on its ex-day; for a one-year beta that is
noise, not a bias.

``--previous`` makes the month before today's, once: when ``--history``
already holds it, the history is printed back unchanged and nothing is
fetched. The funds workflow runs it every night and commits the file, so
the report is made on the first night after a month ends.

Read-only: it reads the account record and daily closes (yfinance, no key),
and prints. The workflow redirects the output.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Iterable, Optional, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis.book import exposure_from  # noqa: E402
from analysis.returns import YFinancePriceSource, last_final_session  # noqa: E402
from config.instruments import group_for, kind_for  # noqa: E402
from config.market_calendar import is_trading_day  # noqa: E402
from config.watchlist import DEFAULT_WATCHLIST  # noqa: E402

#: World stocks: the index the race and the fund test compare against.
INDEX = "VT"
#: One year of daily returns for each beta.
BETA_SESSIONS = 252
#: Fewer daily returns than this in the year, and a position has no beta.
MIN_RETURNS = 60
#: The breadth average.
BREADTH_SMA = 50
#: Trading sessions in a year, to annualise a daily standard deviation.
YEAR = 252
#: Calendar days of closes fetched before the month's end: a year of
#: sessions, and room for holidays and a missing bar or two.
LOOKBACK_DAYS = 400

ACCOUNT_FILE = Path(__file__).resolve().parent.parent / "logs" / "account.jsonl"

Closes = Callable[[str, date, date], Sequence[tuple[date, float]]]


def last_trading_day(month: str) -> date:
    """The month's last NYSE session."""
    year, number = (int(part) for part in month.split("-"))
    day = (date(year + (number == 12), number % 12 + 1, 1)) - timedelta(days=1)
    while not is_trading_day(day):
        day -= timedelta(days=1)
    return day


def previous_month(today: date) -> str:
    first = today.replace(day=1) - timedelta(days=1)
    return f"{first.year:04d}-{first.month:02d}"


def book_at(lines: Iterable[str], through: date) -> Optional[dict[str, Any]]:
    """The last account snapshot recorded on or before ``through`` (UTC day), or None."""
    best: Optional[dict[str, Any]] = None
    for raw in lines:
        try:
            snapshot = json.loads(raw)
        except ValueError:
            continue
        if not isinstance(snapshot, dict) or not isinstance(snapshot.get("at"), str):
            continue
        if snapshot["at"][:10] > through.isoformat():
            continue
        if not isinstance(snapshot.get("positions"), list):
            continue
        if best is None or snapshot["at"] >= best["at"]:
            best = snapshot
    return best


def no_book_reason(lines: Iterable[str], through: date) -> str:
    """Why ``book_at`` found no snapshot on or before ``through``, in plain words.

    The account has been recorded only since 25 Sep 2026 (``logs/account.jsonl``,
    written after every heartbeat run from then on), so every month before
    September 2026 has no book to measure: an expected gap, not a recorder
    that failed. Saying when the record starts tells the two apart.
    """
    first: Optional[str] = None
    for raw in lines:
        try:
            snapshot = json.loads(raw)
        except ValueError:
            continue
        if isinstance(snapshot, dict) and isinstance(snapshot.get("at"), str) \
                and isinstance(snapshot.get("positions"), list):
            first = snapshot["at"] if first is None else min(first, snapshot["at"])
    if first is None:
        return "no account snapshot has been recorded yet (logs/account.jsonl)"
    return (f"the paper account has been recorded only since {first[:10]} (logs/account.jsonl), "
            f"after this month's last trading day, {through.isoformat()}")


def daily_returns(bars: Sequence[tuple[date, float]]) -> dict[date, float]:
    """Each session's close over the previous close in ``bars``, minus one, by the later date."""
    out: dict[date, float] = {}
    for (_, before), (day, after) in zip(bars, bars[1:]):
        if before > 0:
            out[day] = after / before - 1.0
    return out


def beta(asset: Sequence[tuple[date, float]], index: Sequence[tuple[date, float]],
         through: date) -> tuple[Optional[float], int]:
    """OLS slope of ``asset``'s daily returns on ``index``'s, over the year to ``through``.

    Only sessions on which both had a close and a close the session before
    count, so a missing bar costs a return, never shifts one. Returns the
    slope (None with fewer than ``MIN_RETURNS`` returns) and the count.
    """
    window = [bar for bar in index if bar[0] <= through][-(BETA_SESSIONS + 1):]
    days = [day for day, _ in window]
    mine, ix = dict(asset), dict(window)
    pairs = []
    for before, day in zip(days, days[1:]):
        if before in mine and day in mine and mine[before] > 0 and ix[before] > 0:
            pairs.append((mine[day] / mine[before] - 1.0, ix[day] / ix[before] - 1.0))
    if len(pairs) < MIN_RETURNS:
        return None, len(pairs)
    xs = [x for _, x in pairs]
    ys = [y for y, _ in pairs]
    var = statistics.pvariance(xs)
    if var <= 0:
        return None, len(pairs)
    mx, my = statistics.fmean(xs), statistics.fmean(ys)
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / len(pairs)
    return cov / var, len(pairs)


def above_average(bars: Sequence[tuple[date, float]], through: date) -> Optional[bool]:
    """Whether the close on ``through`` is above the mean of the last 50 closes to it; None without both."""
    upto = [close for day, close in bars if day <= through]
    if len(upto) < BREADTH_SMA or not bars or max(day for day, _ in bars if day <= through) != through:
        return None
    return upto[-1] > statistics.fmean(upto[-BREADTH_SMA:])


def month_volatility(bars: Sequence[tuple[date, float]], month: str) -> tuple[Optional[float], int]:
    """VT's daily returns in the month: sample standard deviation x sqrt(252), and how many."""
    returns = [r for day, r in daily_returns(bars).items() if day.isoformat()[:7] == month]
    if len(returns) < 2:
        return None, len(returns)
    return statistics.stdev(returns) * math.sqrt(YEAR), len(returns)


def report(month: str, account_lines: Iterable[str], closes: Closes,
           watchlist: Sequence[str] = DEFAULT_WATCHLIST) -> dict[str, Any]:
    """The month's concentration record. ``closes(ticker, start, end)`` gives final daily closes."""
    as_of = last_trading_day(month)
    start = as_of - timedelta(days=LOOKBACK_DAYS)
    account_lines = list(account_lines)
    snapshot = book_at(account_lines, as_of)
    index = list(closes(INDEX, start, as_of))
    record: dict[str, Any] = {"month": month, "as_of": as_of.isoformat(), "index": INDEX}

    vol, sessions = month_volatility(index, month)
    record["vt_volatility"] = {
        "annualised_pct": None if vol is None else round(vol * 100, 2),
        "sessions": sessions,
    }

    marks = {t: above_average(list(closes(t, start, as_of)), as_of) for t in watchlist}
    known = [t for t, v in marks.items() if v is not None]
    above = sum(1 for t in known if marks[t])
    record["breadth"] = {
        "above": above, "of": len(known),
        "pct": round(100.0 * above / len(known), 1) if known else None,
        "no_data": sorted(t for t, v in marks.items() if v is None),
    }

    if snapshot is None:
        record["book"] = None
        record["book_missing"] = no_book_reason(account_lines, as_of)
        return record
    account = snapshot.get("account") if isinstance(snapshot.get("account"), dict) else {}
    equity = account.get("equity") if isinstance(account.get("equity"), (int, float)) else None
    positions = []
    for p in snapshot.get("positions") or []:
        ticker, qty, value = p.get("ticker"), p.get("qty"), p.get("market_value")
        if not isinstance(ticker, str) or not isinstance(qty, (int, float)) or not isinstance(value, (int, float)):
            continue
        positions.append({
            "ticker": ticker, "side": "sell" if qty < 0 else "buy", "market_value": abs(float(value)),
            "group": group_for(ticker), "kind": kind_for(ticker).value,
            "risk_to_stop": 0.0, "unrealised": 0.0,
        })

    rows, missing = [], []
    beta_long = beta_short = 0.0
    for p in sorted(positions, key=lambda p: -p["market_value"]):
        b, n = beta(list(closes(p["ticker"], start, as_of)), index, as_of)
        sign = -1.0 if p["side"] == "sell" else 1.0
        weight = sign * p["market_value"] / equity if equity else None
        rows.append({"ticker": p["ticker"], "side": "short" if sign < 0 else "long",
                     "weight_pct": None if weight is None else round(weight * 100, 2),
                     "beta": None if b is None else round(b, 3), "returns": n})
        if b is None or weight is None:
            missing.append(p["ticker"])
        elif sign > 0:
            beta_long += weight * b
        else:
            beta_short += weight * b

    exposure = exposure_from(positions, equity)
    record["book"] = {
        "snapshot_at": snapshot["at"],
        "equity": equity,
        "positions": len(positions),
        "beta_to_vt": {
            "net": round(beta_long + beta_short, 3) if equity else None,
            "long_side": round(beta_long, 3) if equity else None,
            "short_side": round(beta_short, 3) if equity else None,
            "without_beta": missing,
            "by_position": rows,
        },
        "groups": [
            {"group": g["label"], "used_pct": round(g["used"] / equity * 100, 1) if equity else None,
             "cap_pct": round(g["cap_pct"] * 100, 1), "share_of_cap_pct": g["share"]}
            for g in exposure["groups"]
        ],
    }
    return record


def render(record: dict[str, Any]) -> str:
    """One month as a few plain lines."""
    out = [f"Concentration, {record['month']} (as of {record['as_of']}), descriptive only:"]
    book = record.get("book")
    if book is None:
        # A record made before ``book_missing`` existed (2026-08's) says only the date.
        why = record.get("book_missing") or f"no account snapshot was recorded on or before {record['as_of']}"
        out.append(f"- book: not measured: {why}")
    else:
        b = book["beta_to_vt"]
        out.append(f"- beta to VT: {b['net']} net (longs {b['long_side']}, shorts {b['short_side']}), "
                   f"{book['positions']} positions"
                   + (f"; no beta for {', '.join(b['without_beta'])}" if b["without_beta"] else ""))
        groups = [g for g in book["groups"] if g["used_pct"] is not None]
        if groups:
            out.append("- groups vs cap: " + ", ".join(
                f"{g['group']} {g['used_pct']:g}% of {g['cap_pct']:g}%" for g in groups[:8]))
    br = record["breadth"]
    out.append(f"- breadth: {br['above']} of {br['of']} names above their 50-day average"
               + (f" ({br['pct']:g}%)" if br["pct"] is not None else ""))
    v = record["vt_volatility"]
    out.append(f"- VT volatility: {v['annualised_pct']}% a year over {v['sessions']} sessions"
               if v["annualised_pct"] is not None else "- VT volatility: not enough sessions")
    return "\n".join(out) + "\n"


def _read_history(path: Optional[Path]) -> dict[str, Any]:
    try:
        history = json.loads(Path(path).read_text(encoding="utf-8")) if path else {}
    except (OSError, ValueError):
        history = {}
    if not isinstance(history, dict) or not isinstance(history.get("months"), dict):
        history = {"kind": "concentration", "months": {}}
    return history


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="The monthly concentration report (descriptive).")
    which = parser.add_mutually_exclusive_group(required=True)
    which.add_argument("--month", help="YYYY-MM")
    which.add_argument("--previous", action="store_true", help="the month before today's (UTC)")
    parser.add_argument("--history", type=Path, default=None,
                        help="the committed record; with it, the output is the record with the month added")
    parser.add_argument("--account", type=Path, default=ACCOUNT_FILE)
    parser.add_argument("--text", action="store_true")
    args = parser.parse_args(argv)

    now = datetime.now(timezone.utc)
    month = args.month or previous_month(now.date())
    history = _read_history(args.history)
    if args.history is not None and month in history["months"] and not args.text:
        print(json.dumps(history, sort_keys=True))
        return 0

    source = YFinancePriceSource(final_through=last_final_session(now))
    try:
        lines = args.account.read_text(encoding="utf-8").splitlines()
    except OSError:
        lines = []
    record = report(month, lines, lambda t, a, b: source.closes(t, a, b).bars)
    record["made_on"] = now.date().isoformat()
    if args.text:
        print(render(record), end="")
        return 0
    if args.history is None:
        print(json.dumps(record, sort_keys=True))
        return 0
    history["months"][month] = record
    history["latest"] = max(history["months"])
    print(json.dumps(history, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
