"""The book as the record describes it, in one machine-readable snapshot.

    python -m analysis.book                 # a short table, for a person
    python -m analysis.book --json          # the snapshot, for the dashboard

The daily report says what the model thought about eighty names. It does not
say what is held, what each position is worth against its stop, how much of
the account the risk caps still allow, or how today's cycle went in numbers
-- and those are the questions a person opens a dashboard to answer. This
writes them once per cycle to ``logs/book.json``, committed beside the
journal, so a page can read them without a key and without a broker.

Reconstructed, not fetched. The audit log records every ACCEPTED entry and
every management pass against it -- the rung taken, the stop moved, the price
the manager saw -- so the book is derivable from the record this system keeps
of its own decisions, offline and identically in a test. Two honest limits:

* **The mark is the manager's, not the market's.** The last price here is
  the one the position manager saw on its last pass, about 18:50 Israel
  time. It is stamped with that time, and the page says so.
* **A position the manager stopped seeing is reported as closed.** The
  manager walks the broker's open positions every cycle. A ticker with an
  entry on record but no management record on the latest pass is no longer
  held -- a stop filled, or a tranche finished the position -- and the record
  cannot say which. It is listed under ``closed`` with the last day it was
  seen, never silently dropped.

Read-only, like everything in ``analysis``: no broker, no model, no network.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis import health  # noqa: E402
from config import settings as cfg  # noqa: E402
from config.instruments import (  # noqa: E402
    InstrumentKind, duration_rate_weight, equity_risk_beta, group_for, kind_for,
    name_for, sleeve_label,
)

ENTRY_EVENT = "signal_processed"
MANAGED_EVENT = "position_managed"

#: Management actions on which the manager actually looked up a price. An
#: ``unmanaged`` or ``error`` pass records ``price: 0.0`` as a placeholder,
#: and a zero read as a mark is an invented gain.
MARKING_ACTIONS = frozenset({"held", "tranche_taken", "stop_raised"})

#: The per-ticker cap for each instrument kind, as the risk engine applies it.
KIND_CAPS = {
    InstrumentKind.EQUITY: cfg.MAX_POSITION_PCT,
    InstrumentKind.BROAD_FUND: cfg.MAX_BROAD_FUND_PCT,
    InstrumentKind.FOCUSED_FUND: cfg.MAX_FOCUSED_FUND_PCT,
    InstrumentKind.COMMODITY_FUND: cfg.MAX_COMMODITY_FUND_PCT,
}


def _num(value: Any) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def _lines(path: Path) -> list[dict]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return []
    out = []
    for raw in text.splitlines():
        raw = raw.strip()
        if not raw:
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(record, dict):
            out.append(record)
    return out


def _stamp(record: dict) -> str:
    """The audit log's local-clock stamp, ``2026-09-17 15:47:41,444`` -> ISO-ish."""
    raw = str(record.get("ts") or record.get("asctime") or "")
    return raw.replace(",", ".").replace(" ", "T")[:19]


# --------------------------------------------------------------------------- #
# Positions
# --------------------------------------------------------------------------- #


def positions_from(audit: list[dict]) -> tuple[list[dict], list[dict]]:
    """``(open, closed)`` positions from the audit record, oldest entry first."""
    entries: dict[str, dict] = {}
    passes: dict[str, list[dict]] = defaultdict(list)
    for record in audit:
        event = record.get("event") or record.get("message")
        if event == ENTRY_EVENT:
            result = record.get("result") or {}
            ticker = str(result.get("ticker") or "").upper()
            if (result.get("status") == "ACCEPTED" and ticker
                    and _num(result.get("entry_price")) and _num(result.get("stop_price"))):
                entries[ticker] = {**result, "_stamp": _stamp(record)}
                passes[ticker] = []
        elif event == MANAGED_EVENT:
            action = record.get("action") or {}
            ticker = str(action.get("ticker") or "").upper()
            if ticker in entries:
                passes[ticker].append({**action, "_stamp": _stamp(record)})

    latest_pass_day = max((p["_stamp"][:10] for ps in passes.values() for p in ps), default="")

    open_positions, closed = [], []
    for ticker, entry in entries.items():
        side = str(entry.get("side") or "buy")
        sign = 1.0 if side == "buy" else -1.0
        entry_price = float(entry["entry_price"])
        entry_stop = float(entry["stop_price"])
        qty = int(entry.get("quantity") or 0)
        stop = entry_stop
        mark = None
        marked_at = None
        gain_r = None
        rungs = 0
        last_action = None
        last_seen = entry["_stamp"][:10]
        for p in passes[ticker]:
            last_seen = p["_stamp"][:10]
            last_action = p.get("action")
            remaining = p.get("remaining_qty")
            if isinstance(remaining, int) and not isinstance(remaining, bool) and remaining > 0:
                qty = remaining
            new_stop = _num(p.get("new_stop"))
            if new_stop and new_stop > 0:
                stop = new_stop
            if p.get("action") in MARKING_ACTIONS:
                price = _num(p.get("price"))
                if price and price > 0:
                    mark, marked_at = price, p["_stamp"]
                    gain_r = _num(p.get("gain_r"))
            if p.get("action") == "tranche_taken":
                rungs += 1

        r = abs(entry_price - entry_stop)
        reference = mark if mark else entry_price
        position = {
            "ticker": ticker,
            "name": name_for(ticker),
            "sleeve": sleeve_label(ticker),
            "kind": kind_for(ticker).value,
            "group": group_for(ticker),
            "side": side,
            "quantity": qty,
            "opened": entry["_stamp"],
            "entry_price": entry_price,
            "entry_stop": entry_stop,
            "stop": stop,
            "r": r,
            "rungs_taken": rungs,
            "mark": mark,
            "marked_at": marked_at,
            "gain_r": gain_r,
            "unrealised": round((mark - entry_price) * sign * qty, 2) if mark else None,
            "market_value": round(reference * qty, 2),
            "risk_to_stop": round(abs(reference - stop) * qty, 2),
            "stop_distance_pct": round(abs(reference - stop) / reference * 100, 2) if reference else None,
            "last_seen": last_seen,
            "last_action": last_action,
            "has_stop": last_action not in ("unmanaged", "error"),
        }
        if latest_pass_day and last_seen < latest_pass_day:
            closed.append({**position, "closed_reason": "not seen by the manager since " + last_seen})
        else:
            open_positions.append(position)
    return open_positions, closed


# --------------------------------------------------------------------------- #
# Equity, exposure and the caps
# --------------------------------------------------------------------------- #


def latest_equity(journal: list[dict]) -> tuple[Optional[float], Optional[str]]:
    """The newest account equity any decision recorded, and when."""
    best: tuple[str, float] | None = None
    for line in journal:
        outcome = line.get("outcome") or {}
        equity = _num(outcome.get("equity"))
        stamp = str(line.get("ts_utc") or "")
        if equity and equity > 0 and stamp and (best is None or stamp > best[0]):
            best = (stamp, equity)
    return (best[1], best[0]) if best else (None, None)


def exposure_from(open_positions: list[dict], equity: Optional[float]) -> dict:
    """Dollars used against each cap the risk engine applies, and the room left."""
    gross = sum(p["market_value"] for p in open_positions)
    by_group: Counter = Counter()
    by_sleeve = Counter()
    for p in open_positions:
        by_group[p["group"]] += p["market_value"]
        by_sleeve["single names" if p["kind"] == InstrumentKind.EQUITY.value else "funds"] += p["market_value"]
    # HYG and EMB carry real interest-rate duration that neither their own
    # group (Credit) nor the stock-market limit measures. That charge lands
    # on Duration too, on top of its five members, at each ticker's
    # duration-equivalent weight -- see risk_engine._group_market_value,
    # which this mirrors so the dashboard shows the number the engine
    # actually enforces.
    for p in open_positions:
        if p["group"] != "Duration":
            weight = duration_rate_weight(p["ticker"])
            if weight is not None:
                by_group["Duration"] += p["market_value"] * weight

    def cap(label: str, used: float, pct: float) -> dict:
        limit = equity * pct if equity else None
        return {
            "label": label, "used": round(used, 2), "cap_pct": pct,
            "cap": round(limit, 2) if limit else None,
            "headroom": round(max(0.0, limit - used), 2) if limit else None,
            "share": round(used / limit * 100, 1) if limit else None,
        }

    # Net, beta-weighted: longs add and shorts subtract, stocks only
    # (settings.MAX_EQUITY_RISK_PCT). The cap is on the *size* of the net
    # either way, since a big net short is as much a bet as a big net long --
    # but the label carries the side, because this is the one row where the
    # same number means opposite things and the bar cannot show it.
    stock_net = 0.0
    for p in open_positions:
        beta = equity_risk_beta(p["ticker"])
        if beta is not None:
            stock_net += (-1.0 if p["side"] == "sell" else 1.0) * p["market_value"] * beta
    side = "flat" if round(stock_net, 2) == 0 else "net short" if stock_net < 0 else "net long"

    caps = [cap("Whole account", gross, cfg.MAX_GROSS_EXPOSURE_PCT),
            cap("Funds", by_sleeve["funds"], cfg.MAX_FUND_SLEEVE_PCT),
            cap("Single names", by_sleeve["single names"], cfg.MAX_SINGLE_NAME_SLEEVE_PCT),
            cap(f"Stock market ({side}, by beta)", abs(stock_net), cfg.MAX_EQUITY_RISK_PCT)]
    groups = sorted(
        (cap(group, used, cfg.EXPOSURE_GROUP_CAP_OVERRIDES.get(group, cfg.MAX_EXPOSURE_GROUP_PCT))
         for group, used in by_group.items()),
        key=lambda c: -c["used"],
    )
    return {
        "gross": round(gross, 2),
        "at_risk": round(sum(p["risk_to_stop"] for p in open_positions), 2),
        "unrealised": round(sum(p["unrealised"] or 0.0 for p in open_positions), 2),
        "positions": len(open_positions),
        "max_positions": cfg.MAX_OPEN_POSITIONS,
        "caps": caps,
        "groups": groups,
    }


# --------------------------------------------------------------------------- #
# Today's cycle, in numbers
# --------------------------------------------------------------------------- #


def cycle_from(journal: list[dict], day: date) -> dict:
    """The funnel, the cost and the directional calls of ``day``'s cycle.

    One line per ticker: a ticker judged twice (a duplicate cycle) counts
    its first line, so the funnel is over the watchlist and not over lines.

    A held position and a screened-out one look identical on the two fields
    that used to tell them apart -- neither has an ``outcome`` (nothing was
    dispatched) or an ``error`` (nothing failed) -- because both are lines the
    model was never asked to judge. They used to be rare enough next to each
    other's numbers that conflating them went unnoticed: a held position is
    always a small slice of the watchlist, and the screen used to filter most
    of it. With the screen off since 23 September 2026, every line in that
    bucket is a held position, and a dashboard that still called the whole
    bucket "screened out" was reporting a stage that no longer runs. ``held``
    is on every line regardless of whether the screen is on, so it is what
    actually tells the two apart.
    """
    prefix = day.isoformat()
    today = [l for l in journal if str(l.get("ts_utc") or "").startswith(prefix)]
    first: dict[str, dict] = {}
    for line in sorted(today, key=lambda l: str(l.get("ts_utc"))):
        first.setdefault(str(line.get("ticker")), line)
    lines = list(first.values())
    failed = [t for t, l in first.items() if l.get("error")]
    judged = [l for l in lines if l.get("outcome")]
    held = [l for l in lines if l.get("held") and not l.get("error")]
    screened_out = [
        l for l in lines
        if not l.get("outcome") and not l.get("error") and not l.get("held")
    ]
    directional = []
    for l in judged:
        signal = l.get("signal") or {}
        if signal.get("bias") in ("BULLISH", "BEARISH"):
            outcome = l.get("outcome") or {}
            directional.append({
                "ticker": l.get("ticker"), "name": name_for(str(l.get("ticker"))),
                "bias": signal.get("bias"), "conviction": signal.get("conviction"),
                "status": outcome.get("status"), "reason": outcome.get("reason"),
            })
    cost = sum(
        (_num((l.get("usage") or {}).get("cost_usd")) or 0.0)
        + (_num(((l.get("screen") or {}).get("usage") or {}).get("cost_usd")) or 0.0)
        for l in today
    )
    stamps = sorted(str(l.get("ts_utc")) for l in today)
    return {
        "day": prefix,
        "tickers": len(lines),
        "lines": len(today),
        "failed": sorted(failed),
        "held": len(held),
        "screened_out": len(screened_out),
        "judged": len(judged),
        "directional": sorted(directional, key=lambda d: -(d["conviction"] or 0)),
        "accepted": [d["ticker"] for d in directional if d["status"] == "ACCEPTED"],
        "cost_usd": round(cost, 2),
        "started": stamps[0] if stamps else None,
        "finished": stamps[-1] if stamps else None,
    }


# --------------------------------------------------------------------------- #
# The snapshot
# --------------------------------------------------------------------------- #


def build(audit_path: Path, journal_path: Path, day: Optional[date] = None) -> dict:
    audit = _lines(audit_path)
    journal = _lines(journal_path)
    day = day or datetime.now(timezone.utc).date()
    open_positions, closed = positions_from(audit)
    equity, equity_at = latest_equity(journal)
    alarms = health.check(journal_path, audit_path, day)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "day": day.isoformat(),
        "equity": equity,
        "equity_at": equity_at,
        "positions": sorted(open_positions, key=lambda p: -p["market_value"]),
        "closed": sorted(closed, key=lambda p: p["last_seen"], reverse=True)[:20],
        "exposure": exposure_from(open_positions, equity),
        "cycle": cycle_from(journal, day),
        "alarms": [{"severity": a.severity, "title": a.title, "detail": a.detail} for a in alarms],
        "ladder": [{"take_at_r": r.take_at_r, "take_fraction": r.take_fraction, "stop_to_r": r.stop_to_r}
                   for r in cfg.PROFIT_LADDER],
    }


def render(book: dict) -> str:
    out = [f"Book as recorded, {book['day']}"]
    equity = book["equity"]
    out.append(f"Equity {equity:,.0f} (as of {book['equity_at']})" if equity else "Equity not yet recorded")
    e = book["exposure"]
    out.append(f"{e['positions']} positions, {e['gross']:,.0f} gross, {e['at_risk']:,.0f} at risk to the stops")
    out.append("")
    out.append(f"{'Ticker':<6} {'Side':<4} {'Qty':>5} {'Entry':>9} {'Stop':>9} {'Mark':>9} {'Unreal.':>9} {'Risk':>8}  Last")
    for p in book["positions"]:
        mark = f"{p['mark']:.2f}" if p["mark"] else "n/a"
        unreal = f"{p['unrealised']:+.2f}" if p["unrealised"] is not None else "n/a"
        out.append(f"{p['ticker']:<6} {p['side']:<4} {p['quantity']:>5} {p['entry_price']:>9.2f} "
                   f"{p['stop']:>9.2f} {mark:>9} {unreal:>9} {p['risk_to_stop']:>8.0f}  {p['last_action'] or ''}")
    if book["closed"]:
        out.append("")
        out.append("Closed: " + ", ".join(f"{p['ticker']} ({p['last_seen']})" for p in book["closed"]))
    c = book["cycle"]
    out.append("")
    out.append(f"Cycle {c['day']}: {c['tickers']} tickers, {c['held']} already held, "
               f"{c['screened_out']} screened out, {c['judged']} judged, "
               f"{len(c['directional'])} directional, {len(c['accepted'])} traded, ${c['cost_usd']:.2f}")
    for a in book["alarms"]:
        out.append(f"  [{a['severity']}] {a['title']}")
    return "\n".join(out)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="The book as the record describes it.")
    parser.add_argument("--audit", type=Path, default=cfg.AUDIT_LOG_PATH)
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH)
    parser.add_argument("--day", default=None, help="ISO date, default today in UTC")
    parser.add_argument("--json", action="store_true", help="the snapshot as JSON")
    args = parser.parse_args(argv)
    day = date.fromisoformat(args.day) if args.day else None
    book = build(args.audit, args.journal, day)
    print(json.dumps(book, indent=2) if args.json else render(book))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
