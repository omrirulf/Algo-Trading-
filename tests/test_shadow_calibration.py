"""Calibration: the model fund's machinery started from the real book, held against it.

Every test builds its own bars, snapshots, audit lines and journal: nothing
here reads logs/, and nothing reaches the network or the live audit log.
The dates are a real run of sessions: C0 is Thursday 1 Oct 2026, C1 Friday,
C2 Monday 5 Oct, C3 Tuesday, C4 Wednesday. New York is on EDT, so the close
is 20:00 UTC.
"""

from __future__ import annotations

import dataclasses
import json
import logging
from datetime import date, datetime, timedelta, timezone

import pandas as pd
import pytest

from analysis.reader import JournalEntry
from shadow import calibration as calib
from shadow.audit import live_audit_guarded
from shadow.calibration import (
    OPEN,
    PASS_RULE,
    CalibrationResult,
    Difference,
    Integrity,
    Match,
    SeriesPoint,
    Trade,
)
from shadow.fund import Fund
from shadow.market import Bars, SimFeed

C0, C1, C2, C3, C4 = date(2026, 10, 1), date(2026, 10, 2), date(2026, 10, 5), date(2026, 10, 6), date(2026, 10, 7)


def utc(text: str) -> datetime:
    return datetime.fromisoformat(text).replace(tzinfo=timezone.utc)


# --------------------------------------------------------------------------- #
# Builders
# --------------------------------------------------------------------------- #


def flat_frame(first: str = "2026-05-01", last: str = "2026-10-09", price: float = 100.0) -> pd.DataFrame:
    """A quiet tape: opens and closes at ``price``, one point either side, so no stop is ever reached."""
    days = pd.bdate_range(first, last)
    return pd.DataFrame({"Open": price, "High": price + 1, "Low": price - 1, "Close": price, "Dividends": 0.0},
                        index=days)


def bars_for(*tickers: str) -> Bars:
    return Bars({t: flat_frame() for t in tickers})


def snapshot_line(at: str, cash: float, positions=(), stops=(), fills=(), history=None, **extra) -> str:
    record = {
        "at": at, "sha": None, "mode": "cycle",
        "account": {"equity": None, "cash": cash, "long_market_value": None, "short_market_value": None,
                    "last_equity": None},
        # None: that read failed, and the recorder wrote null for it.
        "positions": None if positions is None else [
            {"ticker": t, "qty": q, "avg_entry_price": p, "market_value": abs(q) * p, "current_price": p}
            for t, q, p in positions
        ],
        "stops": None if stops is None else [
            {"order_id": oid, "ticker": t, "qty": q, "stop_price": sp, "side": side}
            for oid, t, q, sp, side in stops
        ],
        "fills": [
            {"id": fid, "order_id": oid, "ticker": t, "side": side, "qty": q, "price": p, "at": when}
            for fid, oid, t, side, q, p, when in fills
        ],
        "history": history or {"days": [], "equity": []},
    }
    record.update(extra)
    return json.dumps(record)


def history(pairs: dict[date, float]) -> dict:
    return {"days": [d.isoformat() for d in pairs], "equity": list(pairs.values())}


def ts(moment: str) -> str:
    """The live audit log's ``ts``: ``YYYY-MM-DD HH:MM:SS,mmm`` in UTC."""
    return moment.replace("T", " ") + ",000"


def accepted(moment: str, ticker: str, side: str, qty: int, entry: float, stop: float) -> str:
    return json.dumps({
        "signal": {"ticker": ticker, "bias": "BULLISH" if side == "buy" else "BEARISH", "conviction": 0.8},
        "result": {"status": "ACCEPTED", "ticker": ticker, "side": side, "quantity": qty, "entry_price": entry,
                   "stop_price": stop, "reason": f"submitted {side} {qty} {ticker}", "timestamp": None},
        "ts": ts(moment), "level": "INFO", "event": "signal_processed",
    })


def refused(moment: str, ticker: str, status: str, reason: str) -> str:
    return json.dumps({
        "signal": {"ticker": ticker, "bias": "BEARISH", "conviction": 0.8},
        "result": {"status": status, "ticker": ticker, "reason": reason, "quantity": None, "side": None,
                   "entry_price": None, "stop_price": None, "timestamp": None},
        "ts": ts(moment), "level": "ERROR" if status == "ERROR" else "INFO", "event": "signal_processed",
    })


def managed(moment: str, ticker: str, action: str, **fields) -> str:
    return json.dumps({"action": {"ticker": ticker, "action": action, **fields}, "ts": ts(moment),
                       "level": "INFO", "event": "position_managed"})


def line(moment: str, ticker: str, bias: str = "BULLISH", conviction: float = 0.8, held: bool = False):
    stamp = utc(moment)
    if held:
        return JournalEntry(ticker=ticker, timestamp=stamp, timestamp_is_exact=True, held=True)
    return JournalEntry(ticker=ticker, timestamp=stamp, timestamp_is_exact=True, bias=bias, conviction=conviction)


# --------------------------------------------------------------------------- #
# a) Snapshots
# --------------------------------------------------------------------------- #


def test_load_snapshots_keeps_what_it_can_and_counts_the_rest():
    good_late = snapshot_line(
        "2026-10-02T15:40:00Z", 90_000.0,
        positions=[("NVDA", 50, 100.0), ("ZERO", 0, 10.0)],
        stops=[("s1", "NVDA", 50, 96.0, "sell")],
        history=history({C0: 95_000.0}),
        a_field_nobody_knows={"x": 1},
    )
    record = json.loads(snapshot_line("2026-10-01T15:40:00Z", 91_000.0))
    record["positions"] = [{"ticker": "AAPL"}, "junk", {"ticker": "msft", "qty": 3, "avg_entry_price": None,
                                                           "market_value": None, "current_price": None}]
    record["stops"] = [{"ticker": "MSFT", "qty": 3, "stop_price": None, "side": "sell"}]
    record["fills"] = [{"ticker": "MSFT", "side": "buy", "qty": 3, "price": 10.0, "at": "not a time"},
                       {"id": "f1", "order_id": "o1", "ticker": "MSFT", "side": "sell_short", "qty": 3,
                        "price": 10.0, "at": "2026-10-01T14:00:00Z"}]
    record["history"] = {"days": ["2026-09-30", "bad"], "equity": [None, 5.0]}
    good_early = json.dumps(record)
    lines = [
        "", "not json", "[1, 2]",
        json.dumps({"at": "2026-10-01T15:40:00Z", "error": "account unreachable"}),
        snapshot_line("no time at all", 1.0),
        good_late, good_early,
    ]

    snaps = calib.load_snapshots(lines)

    assert [s.at for s in snaps] == [utc("2026-10-01T15:40:00"), utc("2026-10-02T15:40:00")]
    assert snaps.errors == 1
    assert snaps.skipped == 3
    early, late = snaps
    assert [(p.ticker, p.qty) for p in early.positions] == [("MSFT", 3)]
    assert early.stops == ()
    assert [(f.id, f.side, f.signed) for f in early.fills] == [("f1", "sell_short", -3)]
    assert early.history == ()
    assert [p.ticker for p in late.positions] == ["NVDA"]          # a zero position is not a position
    assert late.stops[0].order_id == "s1" and late.day == C1


def test_a_line_with_a_failed_read_keeps_the_parts_that_were_read():
    """The recorder writes null for a part it could not read and keeps the
    rest. The fills and closes such a line carries are still true; its
    cash, positions or stops are unknown -- never zero, never a flat book."""
    lines = [
        snapshot_line("2026-10-01T15:40:00Z", 90_000.0, positions=[("NVDA", 50, 100.0)],
                      stops=[("stop-nvda", "NVDA", 50, 96.0, "sell")]),
        snapshot_line("2026-10-01T21:00:00Z", 0.0, account=None, positions=None,
                      fills=[("f1", "o1", "MSFT", "buy", 40, 100.0, "2026-10-01T16:20:00Z")],
                      history=history({C0: 91_000.0}),
                      errors=[{"part": "account", "error": "x"}, {"part": "positions", "error": "x"}]),
        # The whole recorder failed: nothing was read at all.
        json.dumps({"at": "2026-10-02T15:40:00Z", "mode": "cycle", "error": "BrokerError: down"}),
    ]
    snaps = calib.load_snapshots(lines)

    assert len(snaps) == 2 and snaps.errors == 1 and snaps.skipped == 0
    partial = snaps[1]
    assert partial.cash is None and partial.equity is None and partial.positions is None
    assert partial.stops == () and [f.id for f in partial.fills] == ["f1"]
    assert not partial.can_seed and snaps[0].can_seed
    assert calib.real_closes(snaps) == {C0: 91_000.0}
    with pytest.raises(ValueError, match="no cash, positions"):
        calib.book_at_close(partial, [])

    # The seed is the earlier, complete line, rolled forward through the fill.
    seed, chosen, _ = calib._choose_seed(snaps, C0)
    assert chosen is snaps[0]
    assert {(p.ticker, p.qty) for p in seed.positions} == {("NVDA", 50), ("MSFT", 40)}
    assert seed.cash == pytest.approx(86_000.0)


def test_a_snapshot_whose_positions_read_failed_says_nothing_about_what_is_held():
    """Read as an empty book, the C1 line would close NVDA on C1."""
    audit = [accepted("2026-10-01T14:00:00", "NVDA", "buy", 50, 100.0, 96.0)]
    snaps = calib.load_snapshots([
        snapshot_line("2026-10-01T21:00:00Z", 90_000.0, positions=[("NVDA", 50, 100.0)]),
        snapshot_line("2026-10-02T21:00:00Z", 90_000.0, positions=None),
    ])
    (period,) = calib.holding_periods(audit, [], snaps)
    assert (period.ticker, period.entered, period.closed) == ("NVDA", C0, None)


def test_load_snapshots_of_a_missing_file_is_empty():
    snaps = calib.load_snapshots([])
    assert list(snaps) == [] and snaps.errors == 0 and snaps.skipped == 0
    assert calib.real_closes(snaps) == {}


# --------------------------------------------------------------------------- #
# b) Real closes
# --------------------------------------------------------------------------- #


def test_real_closes_take_the_newest_snapshot_and_skip_an_open_session():
    older = snapshot_line("2026-10-02T21:00:00Z", 1.0, history=history({C0: 100.0, C1: 101.0}))
    newer = snapshot_line("2026-10-05T15:40:00Z", 1.0,
                          history=history({C0: 100.5, C1: 101.5, C2: 999.0}))   # C2 is still trading

    closes = calib.real_closes(calib.load_snapshots([newer, older]))

    assert closes == {C0: 100.5, C1: 101.5}


# --------------------------------------------------------------------------- #
# c) The book at the close
# --------------------------------------------------------------------------- #


def test_book_at_close_applies_only_that_days_fills_up_to_four_pm_new_york():
    seed_snapshot = calib.load_snapshots([snapshot_line(
        "2026-10-01T15:40:00Z", 90_000.0,
        positions=[("NVDA", 50, 100.0), ("TLT", -20, 80.0)],
        stops=[("stop-nvda", "NVDA", 50, 96.0, "sell"), ("stop-tlt", "TLT", 20, 84.0, "buy")],
    )])[0]
    later = calib.load_snapshots([snapshot_line("2026-10-02T15:40:00Z", 0.0, fills=[
        ("f0", "o0", "NVDA", "buy", 10, 99.0, "2026-10-01T15:00:00Z"),      # before the snapshot: in it
        ("f1", "o1", "MSFT", "buy", 40, 100.0, "2026-10-01T16:20:00Z"),     # a new position
        ("f2", "o2", "NVDA", "buy", 10, 106.0, "2026-10-01T17:00:00Z"),     # an add: the average moves
        ("f3", "stop-tlt", "TLT", "buy", 20, 81.0, "2026-10-01T18:00:00Z"), # the short's stop fills
        ("f4", "o4", "NVDA", "sell", 5, 102.0, "2026-10-01T20:00:00Z"),     # 16:00 New York exactly
        ("f5", "o5", "NVDA", "sell", 30, 102.0, "2026-10-01T20:30:00Z"),    # after the close
        ("f6", "o6", "NVDA", "sell", 30, 102.0, "2026-10-02T14:00:00Z"),    # the next day
    ])])[0]

    seed = calib.book_at_close(seed_snapshot, later.fills, C0,
                               later_stops=[calib.RestingStop("stop-msft", "MSFT", 40, 96.0, "sell")])

    assert seed.day == C0 and seed.fills_applied == 4
    assert seed.cash == pytest.approx(90_000 - 4_000 - 1_060 - 1_620 + 510)
    assert {(p.ticker, p.qty) for p in seed.positions} == {("MSFT", 40), ("NVDA", 55)}
    nvda = next(p for p in seed.positions if p.ticker == "NVDA")
    assert nvda.avg_entry_price == pytest.approx((50 * 100 + 10 * 106) / 60)
    # The closed short took its stop with it; MSFT's came from the next snapshot.
    assert {(s.ticker, s.qty, s.stop_price) for s in seed.stops} == {("NVDA", 50, 96.0), ("MSFT", 40, 96.0)}
    assert any("MSFT" in note and "next snapshot" in note for note in seed.notes)


def test_a_fill_between_two_reads_is_applied_only_to_the_parts_read_before_it():
    """The recorder reads cash, then positions, then stops. A fill between
    the cash read and the positions read is in the positions already and
    not yet in the cash; applying it to both would count it twice."""
    reads = {"account": {"from": "2026-10-01T15:40:00.100Z", "to": "2026-10-01T15:40:00.200Z"},
             "positions": {"from": "2026-10-01T15:40:00.400Z", "to": "2026-10-01T15:40:00.500Z"},
             "stops": {"from": "2026-10-01T15:40:00.700Z", "to": "2026-10-01T15:40:00.800Z"},
             "fills": {"from": "2026-10-01T15:40:00.900Z", "to": "2026-10-01T15:40:01.000Z"}}
    snaps = calib.load_snapshots([snapshot_line(
        "2026-10-01T15:40:00Z", 90_000.0,
        # Read after the MSFT buy and before the NVDA stop filled.
        positions=[("NVDA", 50, 100.0), ("MSFT", 40, 100.0)],
        # Read after the NVDA stop filled: it is no longer resting.
        stops=[("stop-msft", "MSFT", 40, 96.0, "sell")],
        # The snapshot's own fills: its window reaches past the snapshot's start.
        fills=[("f1", "o-msft", "MSFT", "buy", 40, 100.0, "2026-10-01T15:40:00.300Z"),
               ("f2", "stop-nvda", "NVDA", "sell", 50, 95.0, "2026-10-01T15:40:00.600Z")],
        reads=reads,
    )])

    seed, chosen, _ = calib._choose_seed(snaps, C0)

    assert chosen.read_window("positions") == (utc("2026-10-01T15:40:00.400"), utc("2026-10-01T15:40:00.500"))
    assert seed.cash == pytest.approx(90_000.0 - 4_000.0 + 50 * 95.0)      # both fills came after the cash
    assert [(p.ticker, p.qty) for p in seed.positions] == [("MSFT", 40)]    # MSFT once, NVDA gone
    assert [(s.order_id, s.qty) for s in seed.stops] == [("stop-msft", 40)]
    assert seed.fills_applied == 2 and not any("read; applied" in n for n in seed.notes)


def test_a_fill_during_a_read_is_applied_as_though_after_and_noted():
    reads = {"account": {"from": "2026-10-01T15:40:00.100Z", "to": "2026-10-01T15:40:00.200Z"},
             "positions": {"from": "2026-10-01T15:40:00.400Z", "to": "2026-10-01T15:40:00.500Z"},
             "stops": {"from": "2026-10-01T15:40:00.700Z", "to": "2026-10-01T15:40:00.800Z"}}
    snap = calib.load_snapshots([snapshot_line("2026-10-01T15:40:00Z", 90_000.0, reads=reads)])[0]
    fill = calib.AccountFill("f1", "o1", "XOM", "buy", 5, 50.0, utc("2026-10-01T15:40:00.450"))

    seed = calib.book_at_close(snap, [fill])

    assert [(p.ticker, p.qty) for p in seed.positions] == [("XOM", 5)]
    assert seed.cash == pytest.approx(90_000.0 - 250.0)
    assert any("XOM" in n and "during the positions read" in n for n in seed.notes)


def test_book_at_close_without_the_next_snapshot_says_the_stop_is_unknown():
    snap = calib.load_snapshots([snapshot_line("2026-10-01T15:40:00Z", 90_000.0)])[0]
    fill = calib.AccountFill("f1", "o1", "MSFT", "buy", 40, 100.0, utc("2026-10-01T16:20:00"))

    seed = calib.book_at_close(snap, [fill])

    assert seed.stops == ()
    assert any("MSFT" in note and "no known stop" in note for note in seed.notes)


# --------------------------------------------------------------------------- #
# d) The seeded fund
# --------------------------------------------------------------------------- #


SEED_AUDIT = [
    accepted("2026-09-25T15:30:00", "NVDA", "buy", 50, 100.0, 96.0),
    managed("2026-09-28T15:07:00", "NVDA", "held", remaining_qty=50, new_stop=96.0),
    accepted("2026-10-01T16:20:00", "MSFT", "buy", 40, 100.0, 96.0),
    accepted("2026-09-29T15:30:00", "XOM", "buy", 10, 100.0, 96.0),         # closed since: not held
]


def a_seed() -> calib.Seed:
    return calib.Seed(
        day=C0, taken_at=utc("2026-10-01T15:40:00"), cash=86_000.0,
        positions=(calib.SeedPosition("MSFT", 40, 100.0), calib.SeedPosition("NVDA", 50, 100.0)),
        stops=(calib.RestingStop("s-msft", "MSFT", 40, 96.0, "sell"),
               calib.RestingStop("s-nvda", "NVDA", 50, 96.0, "sell")),
    )


def test_seed_fund_holds_the_seeded_book_and_only_its_record():
    bars = bars_for("NVDA", "MSFT", "XOM", "VT")
    fund = calib.seed_fund(a_seed(), SimFeed(bars), bars, SEED_AUDIT)

    assert fund.name == "calibration" and fund.decisions == [] and fund.audit.keep_actions
    assert fund.broker.cash == 86_000.0
    assert fund.broker.held_quantities() == {"MSFT": 40, "NVDA": 50}
    assert fund.broker.positions["NVDA"].avg_entry_price == 100.0
    assert fund.broker.positions["NVDA"].opened == C0
    assert sorted((s.ticker, s.qty, s.stop_price) for s in fund.broker.live_stops()) == [
        ("MSFT", 40, 96.0), ("NVDA", 50, 96.0)]
    assert fund.broker.fills == []                      # seeding is not a trade
    assert len(fund.audit.lines_for("NVDA")) == 2
    assert fund.audit.lines_for("XOM") == []            # forgotten: the fund does not hold it


def test_the_manager_measures_a_seeded_position_from_its_real_entry():
    bars = bars_for("NVDA", "MSFT", "VT")
    feed = SimFeed(bars)
    fund = calib.seed_fund(a_seed(), feed, bars, SEED_AUDIT)

    with live_audit_guarded():
        feed.at_open(C2)
        fund.session(C2, [])                            # a cycle ran: the manager passes over the book

    actions = [a for a in fund.audit.actions if a["ticker"] in ("NVDA", "MSFT")]
    assert {a["ticker"] for a in actions} == {"NVDA", "MSFT"}
    assert not any(a["r_estimated"] for a in actions)
    assert fund.tally.estimated_r == 0 and fund.tally.manager_errors == []
    assert {a["r"] for a in actions} == {4.0}           # entry 100, stop 96


def test_without_the_seeded_record_the_manager_would_have_guessed_r():
    """The control for the test above: the seeding is what makes R real."""
    bars = bars_for("NVDA", "MSFT", "VT")
    feed = SimFeed(bars)
    fund = calib.seed_fund(a_seed(), feed, bars, [])

    with live_audit_guarded():
        feed.at_open(C2)
        fund.session(C2, [])

    assert fund.tally.estimated_r > 0


def test_audit_lines_through_drops_what_the_live_manager_did_later():
    lines = SEED_AUDIT + [managed("2026-10-05T15:07:00", "NVDA", "tranche_taken", rung=0, qty_closed=16),
                          "garbage"]
    kept = calib.audit_lines_through(lines, calib.close_of(C0))
    assert kept == SEED_AUDIT


# --------------------------------------------------------------------------- #
# e, f) The run and its trades
# --------------------------------------------------------------------------- #


def scenario() -> dict:
    """The real account, and what it journalled, around C0..C4.

    Seeded from the C0 snapshot: NVDA held, MSFT bought after the snapshot
    (its fill and its stop come from the C1 snapshot). On C0 the model also
    liked GOOGL -- the real account's business, already in the seed. On C1
    the real account bought JPM (the sim should buy it at C2's open), bought
    XOM on a line whose conviction the engine refuses, and tried to short LQD,
    which the real broker refused. On C3 it bought GLD, which the sim can only
    answer at C4's open, after the run.
    """
    snaps = [
        snapshot_line("2026-10-01T15:40:00Z", 90_000.0, positions=[("NVDA", 50, 100.0)],
                      stops=[("stop-nvda", "NVDA", 50, 96.0, "sell")],
                      history=history({date(2026, 9, 30): 95_000.0})),
        snapshot_line("2026-10-02T15:40:00Z", 86_000.0, positions=[("NVDA", 50, 100.0), ("MSFT", 40, 100.0)],
                      stops=[("stop-nvda", "NVDA", 50, 96.0, "sell"), ("stop-msft", "MSFT", 40, 96.0, "sell")],
                      fills=[("f1", "o-msft", "MSFT", "buy", 40, 100.0, "2026-10-01T16:20:00Z")],
                      history=history({date(2026, 9, 30): 95_000.0, C0: 95_000.0})),
        snapshot_line("2026-10-05T15:40:00Z", 80_300.0,
                      positions=[("NVDA", 50, 100.0), ("MSFT", 40, 100.0), ("JPM", 47, 100.0), ("XOM", 10, 100.0)],
                      fills=[("f2", "o-jpm", "JPM", "buy", 47, 100.0, "2026-10-02T16:20:00Z"),
                             ("f3", "o-xom", "XOM", "buy", 10, 100.0, "2026-10-02T16:21:00Z")],
                      history=history({C0: 95_000.0, C1: 95_000.0})),
        snapshot_line("2026-10-07T15:40:00Z", 79_800.0,
                      fills=[("f4", "o-gld", "GLD", "buy", 5, 100.0, "2026-10-06T16:20:00Z")],
                      history=history({C0: 95_000.0, C1: 95_000.0, C2: 95_000.0, C3: 95_000.0, C4: 95_100.0})),
    ]
    audit = SEED_AUDIT + [
        refused("2026-10-01T16:21:00", "GOOGL", "REJECTED", "no room under the sleeve budget limit"),
        accepted("2026-10-02T16:20:00", "JPM", "buy", 47, 100.0, 96.3),
        accepted("2026-10-02T16:21:00", "XOM", "buy", 10, 100.0, 96.3),
        refused("2026-10-02T16:22:00", "LQD", "ERROR",
                'BrokerError: submit_order failed for LQD: {"code":42210000,'
                '"message":"asset \\"LQD\\" cannot be sold short"}'),
        # What the live manager did after the seed: never the sim's business.
        managed("2026-10-05T15:07:00", "NVDA", "tranche_taken", rung=0, qty_closed=16, remaining_qty=34),
    ]
    entries = [
        line("2026-10-01T16:10:00", "MSFT"),
        line("2026-10-01T16:11:00", "GOOGL"),
        line("2026-10-02T16:10:00", "JPM"),
        line("2026-10-02T16:11:00", "XOM", conviction=0.10),
        line("2026-10-02T16:12:00", "LQD", bias="BEARISH"),
        line("2026-10-06T16:10:00", "GLD"),
    ]
    bars = bars_for("NVDA", "MSFT", "GOOGL", "JPM", "XOM", "LQD", "GLD", "VT")
    return {"snapshots": calib.load_snapshots(snaps), "entries": entries, "bars": bars, "audit": audit}


def run(s: dict, **kw) -> CalibrationResult:
    return calib.run_calibration(s["snapshots"], s["entries"], s["bars"], SimFeed(s["bars"]), C0, 15, s["audit"],
                                 frozenset(), **kw)


def test_the_run_leaves_c0s_cycle_to_the_seed_and_acts_on_c1s_at_c2():
    result = run(scenario())

    assert [p.day for p in result.series] == [C1, C2, C3]  # through the last real close
    assert result.days_done == 3
    assert not [d for d in result.decisions if d.cycle_day == C0]
    assert not [f for f in result.fund.broker.fills if f.ticker == "GOOGL"]
    jpm = [d for d in result.decisions if d.ticker == "JPM"]
    assert [(d.session, d.cycle_day, d.status) for d in jpm] == [(C2, C1, "ACCEPTED")]
    assert [(f.day, f.kind, f.qty) for f in result.fund.broker.fills if f.ticker == "JPM"] == [(C2, "entry", 47)]
    # The seed itself was right: marked at C0's close it is the real close.
    assert result.day0.sim == pytest.approx(95_000.0) and result.day0.real == 95_000.0
    assert [p.diff_pct for p in result.series] == [pytest.approx(0.0)] * 3


def test_a_real_trade_the_sim_makes_a_session_later_is_timing_not_a_difference():
    result = run(scenario())

    jpm = [m for m in result.matches if m.real.ticker == "JPM"]
    assert len(jpm) == 1 and jpm[0].timing and (jpm[0].real.day, jpm[0].sim.day) == (C1, C2)
    assert "JPM" not in {d.ticker for d in result.differences}
    assert result.metrics.timing == 1


def test_a_trade_the_sim_refused_says_why():
    result = run(scenario())

    xom = [d for d in result.differences if d.ticker == "XOM"]
    assert len(xom) == 1
    assert xom[0].reason.startswith("sim rejected: conviction 0.10 below minimum")
    assert xom[0].real == "bought 10 @ 100.00" and xom[0].sim == "none"


def test_a_trade_only_the_sim_made_names_the_real_brokers_refusal():
    result = run(scenario())

    lqd = [d for d in result.differences if d.ticker == "LQD"]
    assert len(lqd) == 1
    assert lqd[0].reason == 'real broker refused: asset "LQD" cannot be sold short'
    assert lqd[0].real == "none" and lqd[0].sim.startswith("sold short")


def test_the_final_sessions_real_trades_wait_for_the_next_open():
    result = run(scenario())

    assert [(t.ticker, t.day) for t in result.pending] == [("GLD", C3)]
    assert "GLD" not in {d.ticker for d in result.differences}
    metrics = result.metrics
    assert (metrics.real_trades, metrics.matched, metrics.matched_share) == (2, 1, 0.5)
    assert metrics.unexplained == 0
    assert all(d.reason.startswith(calib.REASONS) for d in result.differences)


def test_the_run_writes_nothing_to_the_live_audit_log(_audit_log_to_tmp, monkeypatch):
    live = logging.getLogger("execution_audit")
    seen: list[str] = []
    # Watched at the logger itself, not with a handler: the guard swaps the
    # live logger's handlers out for its tripwire, so a handler added here
    # would be detached for the whole run and could never see a line. The
    # guard opens the level to DEBUG, so every line that reaches the logger
    # passes through ``handle``.
    handle = live.handle
    monkeypatch.setattr(live, "handle", lambda record: (seen.append(record.getMessage()), handle(record))[1])

    result = run(scenario())

    assert seen == []
    assert result.integrity.leak is None and result.integrity.ok
    assert not _audit_log_to_tmp.exists() or _audit_log_to_tmp.read_text() == ""
    # The manager's later work was not seeded: the sim took no NVDA tranche.
    assert not [f for f in result.fund.broker.fills if f.ticker == "NVDA"]


def test_a_line_that_reaches_the_live_audit_log_fails_integrity(monkeypatch):
    original = Fund._manage
    live = logging.getLogger("execution_audit")

    def leaky(self):
        live.info("position_managed")       # a manager that forgot its fund's own logger
        original(self)

    monkeypatch.setattr(Fund, "_manage", leaky)
    level = live.level
    live.setLevel(logging.INFO)             # as app.logger.get_audit_logger configures it
    try:
        result = run(scenario())
    finally:
        live.setLevel(level)

    assert result.integrity.leak and "live audit logger" in result.integrity.leak
    passed, lines = calib.evaluate_pass_rule(result)
    assert not passed
    assert any(line.startswith("5. integrity: FAIL") for line in lines)


def test_no_snapshot_before_the_start_is_a_problem_not_a_crash():
    s = scenario()
    result = calib.run_calibration(s["snapshots"], s["entries"], s["bars"], SimFeed(s["bars"]), date(2026, 9, 1))
    assert result.series == [] and result.problems
    assert calib.calibration_status(result, calib.evaluate_pass_rule(result)) == "running"


def test_calibration_report_fetches_what_it_needs_and_returns_the_json_part():
    s = scenario()
    asked: list[str] = []

    class Fetcher:
        def ohlc(self, ticker, start, end):
            asked.append(ticker)
            return flat_frame()

    out = calib.calibration_report(snapshots=s["snapshots"], entries=s["entries"], audit_lines=s["audit"],
                                   start=C0, final_through=C3, fetcher=Fetcher(), holding=None)

    assert {"NVDA", "MSFT", "JPM", "XOM", "LQD", "VT"} <= set(asked)
    assert out["status"] == "running" and out["start"] == "2026-10-01"
    assert out["days_done"] == 3 and out["days_needed"] == 15
    assert [p["day"] for p in out["series"]] == ["2026-10-02", "2026-10-05", "2026-10-06"]
    assert {d["ticker"] for d in out["differences"]} == {"XOM", "LQD"}
    assert out["metrics"]["matched_share"] == 0.5 and out["metrics"]["unexplained"] == 0
    assert out["pass_rule"]["approved"] is False and out["pass_rule"]["verdicts"]
    json.dumps(out)                                     # plain JSON, nothing else


def test_a_real_reduction_is_a_ladder_close_only_when_the_manager_recorded_it():
    seed = calib.Seed(C0, utc("2026-10-01T15:40:00"), 0.0,
                      (calib.SeedPosition("AAA", 10, 100.0), calib.SeedPosition("BBB", 10, 100.0),
                       calib.SeedPosition("SSS", -10, 100.0)), ())
    fills = [
        calib.AccountFill("f1", "tranche-1", "AAA", "sell", 4, 104.0, utc("2026-10-02T15:07:00")),
        calib.AccountFill("f2", "stop-new-id", "BBB", "sell", 10, 95.0, utc("2026-10-02T18:00:00")),
        calib.AccountFill("f3", "entry-1", "CCC", "sell_short", 5, 50.0, utc("2026-10-02T16:00:00")),
        calib.AccountFill("f4", "stop-listed", "SSS", "buy", 10, 104.0, utc("2026-10-05T14:00:00")),
    ]
    trades = calib.real_trades(seed, fills, calib.close_of(C0), C1, C2,
                               stop_order_ids=frozenset({"stop-listed"}), ladder_order_ids=frozenset({"tranche-1"}))

    got = {(t.ticker, t.direction, t.side, t.is_stop) for t in trades}
    assert got == {("AAA", "reduce", "sell", False), ("BBB", "reduce", "sell", True),
                   ("CCC", "open", "sell", False), ("SSS", "reduce", "buy", True)}
    reasons = {t.ticker: calib._why_real_only(t, []) for t in trades}
    assert reasons == {"AAA": calib.LADDER, "BBB": calib.STOP_DAY, "CCC": calib.UNEXPLAINED,
                       "SSS": calib.STOP_DAY}


def test_a_stop_is_never_the_one_session_lag():
    """Stops rest at the broker and fill the same day in both books. A stop
    a session apart, or a stop in one book against a ladder close in the
    other, is a difference; a ladder close a session apart is the lag."""
    from types import SimpleNamespace

    from shadow.broker import STOP, TRANCHE

    seed = calib.Seed(C0, utc("2026-10-01T21:00:00"), 0.0,
                      tuple(calib.SeedPosition(t, 10, 100.0) for t in ("AAA", "BBB", "CCC")), ())
    snaps = calib.load_snapshots([snapshot_line(
        "2026-10-06T21:00:00Z", 0.0, stops=[("stop-aaa", "AAA", 10, 95.0, "sell")],
        fills=[("f1", "stop-aaa", "AAA", "sell", 10, 95.0, "2026-10-02T15:00:00Z"),
               ("f2", "rung-bbb", "BBB", "sell", 4, 104.0, "2026-10-02T15:07:00Z"),
               ("f3", "rung-ccc", "CCC", "sell", 4, 104.0, "2026-10-02T15:07:00Z")])])
    audit = [managed("2026-10-02T15:07:00", t, "tranche_taken", order_id=f"rung-{t.lower()}", qty_closed=4)
             for t in ("BBB", "CCC")]

    def sim(day, ticker, kind, qty, price):
        return SimpleNamespace(day=day, ticker=ticker, kind=kind, side="sell", qty=qty, price=price)

    fund = SimpleNamespace(broker=SimpleNamespace(fills=[
        sim(C2, "AAA", STOP, 10, 95.0),        # the same stop, a session later
        sim(C1, "BBB", STOP, 10, 95.0),        # a stop where the account took a rung
        sim(C2, "CCC", TRANCHE, 4, 104.0),     # the rung, a session later: the lag
    ]))
    result = CalibrationResult(start=C0, seed=seed)

    calib.compare_trades(result, snaps, audit, fund, calib.close_of(C0), [C1, C2, C3])

    assert len(result.matches) == 3
    assert {(d.ticker, d.reason) for d in result.differences} == {("AAA", calib.STOP_DAY),
                                                                  ("BBB", calib.STOP_DAY)}
    assert result.metrics.timing == 1


def test_a_sim_entry_a_session_before_the_real_one_is_a_different_decision():
    """The sim answers a cycle the session after the real account does, so a
    sim entry a session EARLIER answered an earlier cycle. Only a stop, which
    rests at the broker in both books, may pair a session earlier."""
    order = [C0, C1, C2, C3]
    real_buy = Trade(C2, "JPM", OPEN, "buy", 10, 100.0)
    assert calib.match_trades([real_buy], [Trade(C1, "JPM", OPEN, "buy", 10, 100.0)], order) == []
    real_rung = Trade(C2, "JPM", "reduce", "sell", 4, 104.0, frozenset({"market"}))
    assert calib.match_trades([real_rung], [Trade(C1, "JPM", "reduce", "sell", 4, 104.0,
                                                  frozenset({"close"}))], order) == []

    real_stop = Trade(C2, "JPM", "reduce", "sell", 10, 95.0, frozenset({"stop"}))
    [m] = calib.match_trades([real_stop], [Trade(C1, "JPM", "reduce", "sell", 10, 95.0, frozenset({"stop"}))], order)
    assert m.stop_differs and not m.lag
    # A later sim entry is the lag; the same one earlier never is.
    later = Match(real_buy, Trade(C3, "JPM", OPEN, "buy", 10, 100.0))
    earlier = Match(real_buy, Trade(C1, "JPM", OPEN, "buy", 10, 100.0))
    assert later.lag and not earlier.lag


def test_a_real_stop_on_the_final_session_is_compared_not_left_pending():
    """Stops fill the same day in both books; the sim has run the final
    session, so a real stop there with no sim stop is already a difference."""
    from types import SimpleNamespace

    seed = calib.Seed(C0, utc("2026-10-01T21:00:00"), 0.0, (calib.SeedPosition("AAA", 10, 100.0),), ())
    snaps = calib.load_snapshots([snapshot_line(
        "2026-10-06T21:00:00Z", 0.0, stops=[("stop-aaa", "AAA", 10, 95.0, "sell")],
        fills=[("f1", "stop-aaa", "AAA", "sell", 10, 95.0, "2026-10-06T15:00:00Z")])])
    result = CalibrationResult(start=C0, seed=seed)

    calib.compare_trades(result, snaps, [], SimpleNamespace(broker=SimpleNamespace(fills=[])),
                         calib.close_of(C0), [C1, C2, C3])

    assert result.pending == []
    assert [(d.ticker, d.reason) for d in result.differences] == [("AAA", calib.STOP_DAY)]


def test_seeded_stops_never_protect_more_than_is_held():
    """The recorder lists a stop at its order quantity; a partial fill does
    not reduce it. Six held under a stop for ten is seeded as a stop for six."""
    snap = calib.load_snapshots([snapshot_line(
        "2026-10-01T15:40:00Z", 90_000.0, positions=[("XOM", 6, 100.0), ("NVDA", 6, 100.0)],
        stops=[("sx", "XOM", 10, 95.0, "sell"), ("n1", "NVDA", 4, 95.0, "sell"), ("n2", "NVDA", 4, 94.0, "sell")],
    )])[0]

    seed = calib.book_at_close(snap, [])

    assert sorted((s.order_id, s.qty) for s in seed.stops) == [("n1", 4), ("n2", 2), ("sx", 6)]
    assert any("XOM" in n and "seeded at 6" in n for n in seed.notes)


def test_matching_prefers_the_same_session_then_the_next():
    order = [C0, C1, C2, C3]
    real = [Trade(C1, "AAA", OPEN, "buy", 10, 100.0)]
    same, later, earlier, far = (Trade(d, "AAA", OPEN, "buy", 10, 100.0) for d in (C1, C2, C0, C3))
    assert calib.match_trades(real, [later, same, earlier], order)[0].sim == same
    assert calib.match_trades(real, [earlier, later], order)[0].sim == later
    assert calib.match_trades(real, [far], order) == []
    assert calib.match_trades(real, [Trade(C1, "AAA", "reduce", "sell", 10, 100.0)], order) == []


# --------------------------------------------------------------------------- #
# h) The pass rule
# --------------------------------------------------------------------------- #


def crafted(closes: int = 15, worst: float = 0.004, real_trades: int = 10, matched: int = 10,
            differences=(), integrity: Integrity | None = None, sim_only: int = 0, fixes=()) -> CalibrationResult:
    # The gap drifts steadily out to ``worst`` on the last close: a drift the
    # gap condition sees and the tracking error, a spread, barely does.
    days = calibration_days(closes)
    series = [SeriesPoint(day, 100_000.0 * (1 + worst * (i + 1) / closes), 100_000.0)
              for i, day in enumerate(days)]
    trades = [Trade(days[0], f"T{i}", OPEN, "buy", 10, 100.0) for i in range(real_trades)]
    # The sim made the matched trades, and ``sim_only`` the account never made.
    extra = [Trade(days[0], f"S{i}", OPEN, "buy", 10, 100.0) for i in range(sim_only)]
    return CalibrationResult(
        start=date(2026, 10, 1), series=series, day0=SeriesPoint(date(2026, 10, 1), 100_000.0, 100_000.0),
        real_trades=trades, sim_trades=trades[:matched] + extra, matches=[Match(t, t) for t in trades[:matched]],
        differences=list(differences), integrity=integrity or Integrity(), fixes=tuple(fixes),
    )


def calibration_days(count: int) -> list[date]:
    """Calibration day 1 is Friday 2 Oct 2026, day 12 Monday 19 Oct, day 15 Thursday 22 Oct."""
    return [d.date() for d in pd.bdate_range("2026-10-02", periods=count)]


def day(n: int) -> date:
    """Calibration day ``n``, counted from 1 as the owner counts them."""
    return calibration_days(n)[-1]


#: The rule as it reads once in force: what the verdicts are tested
#: against. The flag flips with the start date (see the pinning tests).
APPROVED = dataclasses.replace(PASS_RULE, approved=True)


def test_a_clean_complete_calibration_passes_every_condition():
    passed, lines = calib.evaluate_pass_rule(crafted(), APPROVED)
    assert passed
    assert lines[0].startswith("Approved rule")
    assert [line.split(":")[1].split()[0] for line in lines[1:]] == ["PASS"] * 6


def test_an_unapproved_rule_cannot_pass_however_good_the_numbers():
    """The owner approves the rule before calibration starts; until then no
    result, however clean, may read "passed" -- and "passed" is what shows
    the funds."""
    result = crafted()
    passed, lines = calib.evaluate_pass_rule(result)
    assert not passed
    assert "not in force" in lines[0] and "cannot pass" in lines[1]
    assert [line.split(":")[1].split()[0] for line in lines[2:]] == ["PASS"] * 6
    assert calib.calibration_status(result, (True, lines)) == "failed", "even a forged verdict"
    assert calib.calibration_status(result, (True, lines), APPROVED) == "passed"


@pytest.mark.parametrize("result,failing", [
    (crafted(worst=0.015), "1."),
    (crafted(worst=0.009, closes=15), None),            # inside 1%, and the spread stays under 0.20%
    (crafted(matched=8), "3."),
    (crafted(differences=[Difference(date(2026, 10, 2), "X", "none", "bought 1 @ 1.00", "unexplained")]), "4."),
    (crafted(integrity=Integrity(manager_errors=["NVDA: BrokerError"])), "5."),
    (crafted(integrity=Integrity(uncovered=["2026-10-05 NVDA: 50 held, stops cover 40"])), "5."),
    # Every real trade matched, but the sim made two more the account never
    # made: 10 of 12 is 83%, under 90% the other way round.
    (crafted(sim_only=2), "6."),
    (crafted(sim_only=1), None),                         # 10 of 11 is 91%
])
def test_each_condition_fails_on_its_own(result, failing):
    passed, lines = calib.evaluate_pass_rule(result, APPROVED)
    verdicts = {line[:2]: line for line in lines[1:]}
    if failing is None:
        assert passed
    else:
        assert not passed
        assert "FAIL" in verdicts[failing]
        assert all("PASS" in v for k, v in verdicts.items() if k != failing)


def test_a_large_tracking_error_fails_even_inside_the_gap():
    result = crafted(worst=0.001)
    result.series = [SeriesPoint(p.day, 100_000.0 * (1 + (0.008 if i % 2 else -0.008)), 100_000.0)
                     for i, p in enumerate(result.series)]
    passed, lines = calib.evaluate_pass_rule(result, APPROVED)
    assert not passed
    assert "2. tracking error" in lines[2] and "FAIL" in lines[2]
    assert "PASS" in lines[1]


def test_an_incomplete_calibration_is_pending_not_passed():
    result = crafted(closes=5)
    passed, lines = calib.evaluate_pass_rule(result, APPROVED)
    assert not passed
    assert "5 of 15 closes" in lines[0]
    assert "PENDING" in lines[1]
    assert calib.calibration_status(result, (passed, lines), APPROVED) == "running"
    broken = crafted(closes=5, worst=0.02)
    assert "FAIL" in calib.evaluate_pass_rule(broken, APPROVED)[1][1]   # a broken close cannot heal


def test_status_follows_the_verdict_once_complete():
    good, bad = crafted(), crafted(worst=0.02)
    assert calib.calibration_status(good, calib.evaluate_pass_rule(good, APPROVED), APPROVED) == "passed"
    assert calib.calibration_status(bad, calib.evaluate_pass_rule(bad, APPROVED), APPROVED) == "failed"
    assert calib.calibration_status(None, None) == "not_started"


def test_the_pass_rule_is_the_owners():
    """Approved on 2026-09-24 with a sixth condition; the flag takes effect
    with the start date (test_shadow_run). The line after the conditions is
    the owner's fail rule of 25 Sep 2026, which replaced "restart the 15 days
    from zero"; the last is the owner's late-run decision of the same day."""
    rule = PASS_RULE
    assert "all six hold over 15 trading days" in rule.text[0] and len(rule.text) == 9
    assert rule.text[6].startswith("6. The other way round: at least 90% of the sim's trades")
    assert rule.text[8] == (
        "Late runs: on a day the real account's run fell outside market hours, the sim does not make the "
        "entries the real broker refused as 'market is closed', nor a profit-ladder pass that could not run; "
        "each is counted and shown. If more than 2 calibration days need this, calibration stops and the "
        "owner is told.")
    assert rule.mirror_limit == calib.MIRROR_LIMIT == 2
    last = rule.text[7]
    assert last.startswith("If calibration fails: the cause is fixed and logged in the Amendments table.")
    assert "re-run on every calibration day recorded so far, from the same starting snapshot" in last
    assert "every day must pass all the conditions again" in last
    assert "At least 5 calibration days must come after the last fix" in last
    assert "ends at day 15 or at the last fix + 5 days, whichever is later" in last
    assert "If a re-run fails on an earlier day, that is a new fail: fix, log and re-run again." in last
    assert "turns out to be a bug still counts as a fail" in last
    assert "restart" not in last
    assert (rule.closes, rule.max_gap_pct, rule.tracking_error_pct, rule.matched_share, rule.unexplained,
            rule.sim_matched_share) == (15, 0.01, 0.002, 0.90, 0, 0.90)


# --------------------------------------------------------------------------- #
# The owner's fail rule of 25 Sep 2026: fix, log, re-run; five days after the last fix
# --------------------------------------------------------------------------- #


def fix_on(n: int, what: str = "a fix") -> tuple[tuple[date, str], ...]:
    """A fix merged on calibration day ``n``: it may have seen that day's close."""
    return ((day(n), what),)


def test_the_end_rule_is_day_15_or_the_last_fix_plus_5_whichever_is_later():
    twenty = calibration_days(20)
    assert calib.closes_needed(twenty) == 15                                # no fix
    assert calib.closes_needed(twenty, fix_on(12)) == 17                    # after day 12: 12 + 5
    assert calib.closes_needed(twenty, fix_on(3)) == 15                     # after day 3: 3 + 5 is before 15
    assert calib.closes_needed(twenty, fix_on(10)) == 15                    # 10 + 5 is exactly 15
    assert calib.closes_needed(twenty, fix_on(11)) == 16
    # The last fix is what counts, in whatever order they were listed.
    assert calib.closes_needed(twenty, fix_on(12) + fix_on(3)) == 17
    assert calib.closes_needed(twenty, fix_on(3) + fix_on(12)) == 17
    # A fix merged over a weekend: the Friday is before it, the Monday after.
    assert calib.closes_needed(twenty, ((day(11) + timedelta(days=1), "Saturday"),)) == 16
    # Merged on day 12 before its close was compared: five more than so far,
    # until day 12 is compared and lands on the fix's side.
    assert calib.closes_needed(twenty[:11], fix_on(12)) == 16
    assert calib.closes_needed(twenty[:12], fix_on(12)) == 17


def test_a_day_on_the_fix_day_is_not_after_it():
    """A fix merged on day F may have been written with F's close in view."""
    fixed_on_12 = crafted(closes=16, fixes=fix_on(12))
    assert fixed_on_12.last_fix == day(12)
    assert fixed_on_12.days_since_fix == 4                                   # 13, 14, 15, 16: not 12
    assert calib.needed_for(fixed_on_12) == 17 and not calib.is_complete(fixed_on_12)
    assert crafted(closes=17, fixes=fix_on(12)).days_since_fix == 5
    assert crafted(closes=15).days_since_fix is None and crafted(closes=15).last_fix is None


def quiet_account(last: date) -> dict:
    """A book of cash only and a real close every session from C0 to ``last``: nothing trades, nothing differs."""
    closes = {d.date(): 100_000.0 for d in pd.bdate_range(C0, last)}
    snaps = calib.load_snapshots([
        snapshot_line("2026-10-01T15:40:00Z", 100_000.0, history=history({date(2026, 9, 30): 100_000.0})),
        snapshot_line(f"{last.isoformat()}T21:00:00Z", 100_000.0, history=history(closes)),
    ])
    frame = flat_frame(last=last.isoformat())
    return {"snapshots": snaps, "bars": Bars({"VT": frame, "SPY": frame.copy()})}


def run_quiet(account: dict, **kw) -> CalibrationResult:
    return calib.run_calibration(account["snapshots"], [], account["bars"], SimFeed(account["bars"]), C0, 15, [],
                                 frozenset(), **kw)


def test_the_run_goes_on_until_five_days_after_the_last_fix():
    """The nightly run is the re-run: same seed, the code as merged, every
    day so far. A fix after day 12 makes it run to day 17, not stop at 15."""
    account = quiet_account(date(2026, 10, 30))                              # 21 sessions after C0

    assert run_quiet(account).days_done == 15
    assert run_quiet(account).series[-1].day == day(15)
    assert run_quiet(account, fixes=fix_on(3)).days_done == 15
    fixed = run_quiet(account, fixes=fix_on(12, "the seed's cash sign"))
    assert fixed.days_done == 17 and fixed.series[-1].day == day(17)
    assert fixed.fixes == ((day(12), "the seed's cash sign"),) and fixed.days_since_fix == 5
    assert calib.is_complete(fixed)

    # Until day 17's close exists the run is still going, whatever it passed.
    short = run_quiet(quiet_account(day(16)), fixes=fix_on(12))
    assert short.days_done == 16 and short.days_since_fix == 4
    assert not calib.is_complete(short)


def test_a_fail_reads_failed_at_once_and_a_merged_fix_runs_on_five_days_after_it():
    # Day 9: a close outside 1%. Failed at once, not at day 15.
    broken = crafted(closes=9, worst=0.03)
    assert calib.calibration_status(broken, calib.evaluate_pass_rule(broken, APPROVED), APPROVED) == "failed"
    assert calib.calibration_status(broken, calib.evaluate_pass_rule(broken)) == "failed"

    # The cause is fixed and merged on day 9; the nightly re-run of the same
    # days from the same seed passes them. Running: five days after the fix.
    for closes, status in ((9, "running"), (13, "running"), (14, "running"), (15, "passed")):
        rerun = crafted(closes=closes, fixes=fix_on(9, "the gap on day 9"))
        evaluation = calib.evaluate_pass_rule(rerun, APPROVED)
        assert calib.calibration_status(rerun, evaluation, APPROVED) == status, closes
    # 9 + 5 is 14, so day 15 is the end; passed only under the rule in force.
    done = crafted(closes=15, fixes=fix_on(9))
    assert calib.calibration_status(done, calib.evaluate_pass_rule(done)) == "failed"

    # A fix after day 12 moves the end to day 17.
    late = crafted(closes=15, fixes=fix_on(12))
    passed, lines = calib.evaluate_pass_rule(late, APPROVED)
    assert not passed and calib.calibration_status(late, (passed, lines), APPROVED) == "running"
    assert lines[0] == ("Approved rule: 15 of 17 closes compared (day 15 or the last fix + 5 days, whichever is "
                        "later; last fix 2026-10-19, 3 of 5 days since).")
    assert all("FAIL" not in line for line in lines)
    end = crafted(closes=17, fixes=fix_on(12))
    passed, lines = calib.evaluate_pass_rule(end, APPROVED)
    assert passed and calib.calibration_status(end, (passed, lines), APPROVED) == "passed"
    assert calib.calibration_status(end, calib.evaluate_pass_rule(end)) == "failed"   # the unapproved rule

    # A re-run that fails on an earlier day is a new fail, fix or no fix.
    again = crafted(closes=15, worst=0.03, fixes=fix_on(12))
    assert calib.calibration_status(again, calib.evaluate_pass_rule(again, APPROVED), APPROVED) == "failed"


def test_the_header_says_how_many_closes_are_needed_and_why():
    _, lines = calib.evaluate_pass_rule(crafted(closes=8), APPROVED)
    assert lines[0] == ("Approved rule: 8 of 15 closes compared (day 15 or the last fix + 5 days, whichever is "
                        "later; no fix so far).")


def gapless(closes: int) -> CalibrationResult:
    """Every close exactly on the real one."""
    return crafted(closes=closes, worst=0.0)


def test_days_passed_counts_from_the_first_day_until_a_day_by_day_check_breaks():
    assert calib.days_passed(None) == 0
    assert calib.days_passed(gapless(8)) == 8

    # Condition 1: a close outside 1% on day 4 ends the count at 3, even
    # though days 5 to 8 were back inside it.
    outside = gapless(8)
    outside.series[3] = SeriesPoint(day(4), 101_500.0, 100_000.0)
    assert calib.days_passed(outside) == 3

    # Condition 4: an unexplained difference dated day 6. An explained one does not count.
    explained = Difference(day(2), "X", "bought 1 @ 1.00", "none", "sim held it already")
    unexplained = Difference(day(6), "Y", "none", "bought 1 @ 1.00", calib.UNEXPLAINED)
    assert calib.days_passed(gapless(8)) == calib.days_passed(crafted(closes=8, worst=0.0,
                                                                      differences=[explained])) == 8
    assert calib.days_passed(crafted(closes=8, worst=0.0, differences=[explained, unexplained])) == 5

    # Condition 5: the uncovered list is dated. The undated breaches are in the verdicts, not here.
    uncovered = Integrity(uncovered=[f"{day(2).isoformat()} NVDA: 50 held, stops cover 40"])
    assert calib.days_passed(crafted(closes=8, worst=0.0, integrity=uncovered)) == 1
    undated = Integrity(manager_errors=["NVDA: BrokerError"], unexpected=["boom"])
    assert calib.days_passed(crafted(closes=8, worst=0.0, integrity=undated)) == 8

    # Judged only over the whole period (2, 3, 6): not in this count.
    assert calib.days_passed(crafted(closes=8, worst=0.0, matched=5, sim_only=5)) == 8

    # A session with no real close is not a calibration day and breaks nothing.
    holed = gapless(8)
    holed.series[3] = SeriesPoint(day(4), 100_000.0, None)
    assert holed.days_done == 7 and calib.days_passed(holed) == 7


def test_the_json_carries_the_fail_rule():
    fixes = fix_on(12, "the seed applied a fill during the positions read twice")
    result = crafted(closes=13, fixes=fixes)
    evaluation = calib.evaluate_pass_rule(result, APPROVED)
    out = calib.calibration_json(result, calib.calibration_status(result, evaluation, APPROVED),
                                 date(2026, 10, 1), evaluation, None, APPROVED)

    assert out["status"] == "running"
    assert (out["days_done"], out["days_needed"], out["days_passed"]) == (13, 17, 13)
    assert out["fixes"] == [{"day": "2026-10-19", "what": "the seed applied a fill during the positions read twice"}]
    assert out["last_fix"] == "2026-10-19"
    assert out["days_since_fix"] == 1 and out["days_after_fix_needed"] == 5
    # Days 1-13 are known; days 14-17 are counted forward in trading days.
    assert out["end_estimate"] == day(17).isoformat() == "2026-10-26"
    # The fund test's start is fixed (the owner's decision of 26 Sep 2026):
    # a later end moves nothing but which looks come before it.
    plan = out["fund_test_plan"]
    assert plan["start"] == "2026-09-29" and plan["matches_registered"] is True
    assert plan["registered"] == [3.40, 2.41, 2.02] and plan["registered_start"] == "2026-09-29"
    json.dumps(out, allow_nan=False)


def test_the_json_without_a_fix():
    result = crafted(closes=15)
    evaluation = calib.evaluate_pass_rule(result, APPROVED)
    out = calib.calibration_json(result, "passed", date(2026, 10, 1), evaluation, None, APPROVED)

    assert (out["days_needed"], out["days_passed"]) == (15, 15)
    assert out["fixes"] == [] and out["last_fix"] is None and out["days_since_fix"] is None
    assert out["days_after_fix_needed"] == 5
    assert out["end_estimate"] == "2026-10-22"
    assert out["fund_test_plan"]["start"] == "2026-09-29"


def test_the_end_estimate_counts_trading_days_from_the_start():
    """Seeded from the 2026-09-25 close, day 15 is 2026-10-16. A fix moves
    the end; the fund test's start (2026-09-29) and its planned bars do not
    move with it (the owner's decision of 26 Sep 2026)."""
    from shadow.fund_test import fund_test_plan

    start = date(2026, 9, 25)
    planned = calib.end_estimate(start, [])
    assert planned == date(2026, 10, 16)
    assert fund_test_plan(planned)["matches_registered"] is True

    # Twelve days compared (to 13 Oct), a fix merged on 14 Oct before its
    # close: day 15 is 16 Oct, the fifth session after the fix 21 Oct.
    known = [date(2026, 9, 28), date(2026, 9, 29), date(2026, 9, 30), date(2026, 10, 1), date(2026, 10, 2),
             date(2026, 10, 5), date(2026, 10, 6), date(2026, 10, 7), date(2026, 10, 8), date(2026, 10, 9),
             date(2026, 10, 12), date(2026, 10, 13)]
    assert calib.end_estimate(start, known, ((date(2026, 10, 14), "x"),)) == date(2026, 10, 21)
    # A fix after day 3 leaves day 15 as the end.
    assert calib.end_estimate(start, known, ((date(2026, 9, 30), "x"),)) == planned
    moved = fund_test_plan(date(2026, 10, 21))
    assert moved["start"] == "2026-09-29" and moved["matches_registered"] is True


#: The registered plan's seed: calibration seeded from the 2026-09-25 close.
REGISTERED_SEED = date(2026, 9, 25)


def plan_day(n: int) -> date:
    """Calibration day ``n`` on the registered plan: day 12 is 13 Oct 2026, day 15 is 16 Oct."""
    from shadow.fund_test import next_trading_day

    day_n = REGISTERED_SEED
    for _ in range(n):
        day_n = next_trading_day(day_n)
    return day_n


def on_the_registered_plan(closes: int, off_on: int | None = None, fixes=(), **kw) -> CalibrationResult:
    """``crafted`` moved onto the registered plan's calendar, every close on
    the real one except day ``off_on``, which is 3% off."""
    series = [SeriesPoint(plan_day(n), 103_000.0 if n == off_on else 100_000.0, 100_000.0)
              for n in range(1, closes + 1)]
    return dataclasses.replace(crafted(closes=closes, worst=0.0, fixes=fixes, **kw), start=REGISTERED_SEED,
                               series=series, day0=SeriesPoint(REGISTERED_SEED, 100_000.0, 100_000.0))


def json_of(result: CalibrationResult, rule=APPROVED) -> dict:
    """The JSON the nightly job would print for ``result``, under ``rule``."""
    evaluation = calib.evaluate_pass_rule(result, rule)
    return calib.calibration_json(result, calib.calibration_status(result, evaluation, rule), result.start,
                                  evaluation, None, rule)


def test_an_open_fail_moves_the_end_before_its_fix_is_merged():
    """A fail needs a fix, the fix cannot be dated before the day the fail
    was seen, and five days must follow it. So the night a fail on day 15
    is seen, the page already says the end is a week later -- not after the
    fix. The fund test's start and planned bars hold all the same: its start
    is fixed, and no look comes before the new end."""
    assert (plan_day(12), plan_day(15)) == (date(2026, 10, 13), date(2026, 10, 16))
    clean = json_of(on_the_registered_plan(15))
    assert clean["status"] == "passed" and clean["end_estimate"] == "2026-10-16"
    assert clean["fund_test_plan"]["matches_registered"] is True

    failed = json_of(on_the_registered_plan(15, off_on=15))
    assert failed["status"] == "failed"
    assert failed["end_estimate"] == "2026-10-23"                             # day 20
    assert failed["fund_test_plan"]["start"] == "2026-09-29"
    assert failed["fund_test_plan"]["matches_registered"] is True
    # The fix it assumes is not a fix: nothing about fixes says one was made.
    assert (failed["fixes"], failed["last_fix"], failed["days_since_fix"], failed["days_needed"]) == (
        [], None, None, 15)

    # Once the fix is merged that day and the re-run passes, the same end, now from the record.
    fixed = json_of(on_the_registered_plan(15, fixes=((plan_day(15), "the close on 16 Oct"),)))
    assert fixed["status"] == "running" and fixed["end_estimate"] == "2026-10-23"

    # A fail first seen on day 11 or later moves the end; on day 10 or before it cannot.
    assert json_of(on_the_registered_plan(11, off_on=11))["end_estimate"] == plan_day(16).isoformat()
    for seen in (3, 10):
        early = json_of(on_the_registered_plan(seen, off_on=seen))
        assert early["status"] == "failed" and early["end_estimate"] == "2026-10-16", seen
        assert early["fund_test_plan"]["matches_registered"] is True, seen

    # A condition only a complete calibration can judge (3, the matched share) counts the same.
    unmatched = json_of(on_the_registered_plan(15, matched=5))
    assert unmatched["status"] == "failed" and unmatched["end_estimate"] == "2026-10-23"

    # A fail seen before a fix already dated later: the end stays that fix's.
    behind = on_the_registered_plan(9, off_on=9, fixes=((plan_day(12), "x"),))
    assert calib.estimated_end(behind) == plan_day(17)


def test_days_needed_counts_the_days_still_to_come_up_to_a_later_fix():
    """The account's record lags: nine closes compared, and a fix merged on
    day 12 (13 Oct). Days 10 to 12 will be on the fix's side once they are
    compared, so 17 are needed now, and the end estimate is day 17 too."""
    lagging = on_the_registered_plan(9, fixes=((plan_day(12), "x"),))
    out = json_of(lagging)
    assert (out["status"], out["days_done"], out["days_needed"], out["days_since_fix"]) == ("running", 9, 17, 0)
    assert out["end_estimate"] == plan_day(17).isoformat() == "2026-10-20"
    assert out["pass_rule"]["verdicts"][0] == (
        "Approved rule: 9 of 17 closes compared (day 15 or the last fix + 5 days, whichever is later; "
        "last fix 2026-10-13, 0 of 5 days since).")
    # The run counts on what it has compared, and runs on until five days after the fix either way.
    assert calib.closes_needed(lagging.compared_days, lagging.fixes) == 15 and not calib.is_complete(lagging)

    # A fix merged on a Saturday after Friday's close (day 10): Monday is the first day after it.
    assert calib.needed_for(on_the_registered_plan(10, fixes=((date(2026, 10, 10), "Saturday"),))) == 15

    # However far the record lags, the number needed and the end estimate agree.
    for fixed_on in range(1, 21):
        fixes = ((plan_day(fixed_on), "x"),)
        results = [CalibrationResult(start=REGISTERED_SEED, fixes=fixes)]
        results += [on_the_registered_plan(closes, fixes=fixes) for closes in range(1, 16)]
        for result in results:
            needed = calib.needed_for(result)
            assert needed == max(15, fixed_on + 5), (fixed_on, result.days_done)
            assert calib.estimated_end(result) == plan_day(needed), (fixed_on, result.days_done)


def test_calibration_report_reads_the_fixes_from_the_schedule(monkeypatch):
    """shadow.run does not pass the fixes: the report reads them itself."""
    from shadow import schedule

    account = quiet_account(date(2026, 10, 30))

    class Fetcher:
        def ohlc(self, ticker, start, end):
            return flat_frame(last="2026-10-30")

    def report():
        return calib.calibration_report(snapshots=account["snapshots"], entries=[], audit_lines=[], start=C0,
                                        final_through=date(2026, 10, 30), fetcher=Fetcher())

    plain = report()
    assert (plain["days_done"], plain["days_needed"], plain["last_fix"]) == (15, 15, None)
    monkeypatch.setattr(schedule, "CALIBRATION_FIXES", fix_on(12, "logged in the Amendments table"))
    fixed = report()
    assert (fixed["days_done"], fixed["days_needed"], fixed["last_fix"], fixed["days_since_fix"]) == (
        17, 17, "2026-10-19", 5)
    # Complete, and a book that never traded has no trade to match: 3 and 6 fail.
    assert fixed["status"] == "failed" and fixed["days_passed"] == 17
    # That fail needs a fix of its own, not merged yet, so dated no earlier
    # than the latest real close (day 21, 30 Oct) and followed by five more
    # days: the end estimate is day 26, not day 17 or 22.
    assert fixed["end_estimate"] == day(26).isoformat() == "2026-11-06"


def test_an_open_fail_keeps_moving_the_end_while_it_waits_for_its_fix():
    """The run stops comparing at the days it needs; a fail left open must
    not keep an end date that is already past (the integration review)."""
    ends = []
    for last in (date(2026, 10, 30), date(2026, 11, 13), date(2026, 12, 18)):
        account = quiet_account(last)

        class Fetcher:
            def ohlc(self, ticker, start, end, _last=last):
                return flat_frame(last=_last.isoformat())

        out = calib.calibration_report(snapshots=account["snapshots"], entries=[], audit_lines=[], start=C0,
                                       final_through=last, fetcher=Fetcher())
        assert out["status"] == "failed" and out["days_done"] == 15
        ends.append(date.fromisoformat(out["end_estimate"]))
        assert ends[-1] > last
    assert ends == sorted(ends) and len(set(ends)) == 3


# --------------------------------------------------------------------------- #
# i) Holding time
# --------------------------------------------------------------------------- #


def test_holding_days_infers_a_close_as_the_first_day_it_was_missing():
    audit = [
        accepted("2026-09-16T16:00:00", "AAA", "buy", 10, 100.0, 96.0),
        accepted("2026-09-18T16:00:00", "CCC", "buy", 10, 100.0, 96.0),      # never seen held: left out
        managed("2026-09-17T15:07:00", "AAA", "held"),
        managed("2026-09-18T15:07:00", "AAA", "stop_raised"),
        accepted("2026-09-21T16:00:00", "BBB", "buy", 10, 100.0, 96.0),
        managed("2026-09-22T15:07:00", "BBB", "held"),                        # a full pass without AAA
        managed("2026-09-23T19:15:00", "BBB", "stop_resized"),                # protect-only: proves nothing
    ]
    journal = [line("2026-09-21T15:08:00", "AAA", held=True)]

    periods = {h.ticker: h for h in calib.holding_periods(audit, journal, [])}
    assert set(periods) == {"AAA", "BBB"}
    assert (periods["AAA"].entered, periods["AAA"].closed, periods["AAA"].days) == (
        date(2026, 9, 16), date(2026, 9, 22), 4)
    assert periods["BBB"].closed is None and periods["BBB"].days == 2       # 22nd and 23rd

    assert calib.holding_days(audit, journal, []) == {
        "median": 4.0, "min": 4, "max": 4, "closed": 1, "open_median": 2.0}


def test_holding_days_takes_the_close_from_a_snapshot_and_its_fill():
    audit = [accepted("2026-09-29T16:00:00", "XXX", "buy", 10, 100.0, 96.0)]
    snaps = calib.load_snapshots([
        snapshot_line("2026-10-01T15:40:00Z", 1.0, positions=[("XXX", 10, 100.0)]),
        snapshot_line("2026-10-05T15:40:00Z", 1.0,
                      fills=[("f1", "o1", "XXX", "sell", 10, 99.0, "2026-10-02T17:00:00Z")]),
    ])

    (period,) = calib.holding_periods(audit, [], snaps)
    assert (period.closed, period.days) == (C1, 3)                          # 30 Sep, 1 and 2 Oct


def test_holding_days_with_nothing_to_read():
    assert calib.holding_days([], [], []) == calib.EMPTY_HOLDING


# --------------------------------------------------------------------------- #
# j) The JSON
# --------------------------------------------------------------------------- #


def test_calibration_json_before_the_start_is_not_started():
    holding = {"median": 4.0, "min": 4, "max": 4, "closed": 2, "open_median": 3.5}
    out = calib.calibration_json(crafted(), "running", None, (True, ["x"]), holding)

    assert out["status"] == "not_started" and out["start"] is None
    assert out["days_done"] == 0 and out["days_needed"] == 15
    assert out["series"] == [] and out["differences"] == []
    assert all(v is None for v in out["metrics"].values())
    assert out["holding_days"] == holding
    assert out["pass_rule"] == {"text": list(PASS_RULE.text), "approved": False, "verdicts": []}
    # The fail rule's keys say nothing before the start, whatever result is passed.
    assert (out["days_passed"], out["fixes"], out["last_fix"], out["days_since_fix"], out["days_after_fix_needed"],
            out["end_estimate"], out["fund_test_plan"]) == (0, [], None, None, 5, None, None)
    fixed = calib.calibration_json(crafted(fixes=fix_on(12)), "running", None, (True, ["x"]), holding)
    assert (fixed["fixes"], fixed["last_fix"], fixed["days_since_fix"], fixed["end_estimate"]) == ([], None, None,
                                                                                                    None)


def test_calibration_json_of_a_run_matches_the_contract():
    result = crafted(differences=[Difference(date(2026, 10, 2), "X", "bought 1 @ 1.00", "none",
                                             "sim held it already")])
    evaluation = calib.evaluate_pass_rule(result, APPROVED)
    out = calib.calibration_json(result, calib.calibration_status(result, evaluation, APPROVED),
                                 date(2026, 10, 1), evaluation, None, APPROVED)

    assert out["status"] == "passed" and out["start"] == "2026-10-01" and out["days_done"] == 15
    assert out["pass_rule"]["approved"] is True
    assert set(out["series"][0]) == {"day", "sim", "real", "diff_pct"}
    assert out["differences"] == [{"day": "2026-10-02", "ticker": "X", "real": "bought 1 @ 1.00", "sim": "none",
                                   "reason": "sim held it already"}]
    assert set(out["metrics"]) >= {"max_abs_gap_pct", "tracking_error_pct", "matched_share", "unexplained"}
    assert out["metrics"]["max_abs_gap_pct"] == pytest.approx(0.004)
    assert out["series"][-1] == {"day": "2026-10-22", "sim": 100_400.0, "real": 100_000.0, "diff_pct": 0.004}
    assert out["holding_days"] == calib.EMPTY_HOLDING
