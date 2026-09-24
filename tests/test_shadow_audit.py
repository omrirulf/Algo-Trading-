"""A fund's audit record reads back exactly as the live log file would.

The position manager keeps no state of its own: R, the rungs already taken
and the last stop all come back out of the record the engine and it wrote.
``shadow.audit.FundAudit`` keeps that record in memory and hands the manager
one ticker's lines at a time, dropping everything the manager could never
match. These tests hold it to the one thing that matters: for every ticker,
the manager's own readers (``ladder_history``, ``last_recorded_stop`` and the
``_history`` under them) give the same answer reading the FundAudit as they
give reading a whole-file record written by the production handler.

The live-log guard is here too: a shadow run that forgot its fund's logger
must fail loudly, whatever level the live logger happens to be at, and must
never open logs/execution_audit.log.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from app import position_manager as pm
from app.execution_engine import ExecutionEngine
from app.logger import log_execution
# Captured at import, before the suite's autouse fixture swaps the module
# attribute for a tmp-path stand-in: the guard test needs the real function,
# the one that would open the live file.
from app.logger import get_audit_logger as _real_get_audit_logger
from app.schemas import Bias, ExecutionResult, ExecutionStatus, LLMSignal
from shadow.audit import FundAudit, LiveAuditLeak, live_audit_guarded
from shadow.broker import SimBroker
from shadow.market import Bars, SimFeed

REPO_AUDIT_LOG = Path(__file__).resolve().parent.parent / "logs" / "execution_audit.log"


# --------------------------------------------------------------------------- #
# Builders
# --------------------------------------------------------------------------- #


def _production_handler(path: Path) -> logging.FileHandler:
    """The live log's own FileHandler and formatter, pointed at ``path``.

    Built by the real ``app.logger.get_audit_logger`` rather than copied, so a
    change to the production formatter shows up here as a difference instead
    of being reproduced by hand. The live logger is left as it was found.
    """
    assert _real_get_audit_logger.__module__ == "app.logger", "captured the test stand-in, not the real one"
    live = logging.getLogger("execution_audit")
    saved, level, propagate = list(live.handlers), live.level, live.propagate
    for handler in saved:
        live.removeHandler(handler)
    try:
        _real_get_audit_logger(path)
        [handler] = live.handlers
        live.removeHandler(handler)
    finally:
        for h in saved:
            live.addHandler(h)
        live.setLevel(level)
        live.propagate = propagate
    return handler


DAYS = pd.bdate_range("2026-01-02", "2026-06-30")
START = 100  # sessions of warm-up before the fund starts: enough for a 90-day ATR


def _walk(start: float, vol: float, seed: int, drift: float = 0.0, shock: tuple[int, float] | None = None
          ) -> pd.DataFrame:
    """A daily random walk: flat through the warm-up, then ``drift`` a day, with one optional gap."""
    rng = np.random.RandomState(seed)
    n = len(DAYS)
    ret = rng.normal(0.0, vol, n)
    ret[START:] += drift
    opens_gap = rng.normal(0.0, vol / 3, n)
    if shock is not None:
        ret[shock[0]] += shock[1]
        opens_gap[shock[0]] = shock[1]
    close = start * np.exp(np.cumsum(ret))
    prev = np.concatenate([[start], close[:-1]])
    open_ = prev * np.exp(opens_gap)
    spread = np.abs(rng.normal(0.0, vol, n)) + vol / 2
    return pd.DataFrame({
        "Open": open_,
        "High": np.maximum(open_, close) * (1 + spread / 2),
        "Low": np.minimum(open_, close) * (1 - spread / 2),
        "Close": close,
        "Dividends": 0.0,
    }, index=DAYS)


def _universe() -> Bars:
    """Three Duration funds that rally (rungs, trails, and a group over its cap),
    a choppy name traded both ways (stop-outs and re-entries), a falling fund
    held short, and a commodity fund that gaps down through its stop."""
    return Bars({
        "TLT": _walk(90, 0.004, 1, drift=0.006),
        "IEF": _walk(95, 0.003, 2, drift=0.005),
        "SHY": _walk(82, 0.002, 3, drift=0.004),
        "MSFT": _walk(400, 0.025, 4),
        "XLE": _walk(90, 0.010, 5, drift=-0.006),
        "GLD": _walk(180, 0.008, 6, drift=0.003, shock=(START + 20, -0.08)),
    })


LEANING = {"TLT": "BULLISH", "IEF": "BULLISH", "SHY": "BULLISH", "XLE": "BEARISH", "GLD": "BULLISH"}


def _signal(ticker: str, bias: str, conviction: float = 0.6) -> LLMSignal:
    return LLMSignal(ticker=ticker, bias=Bias(bias), conviction=conviction, rationale="test")


def _classify(raw: str) -> str:
    """What ``_history`` can use a line for, decided independently of shadow.audit."""
    record = json.loads(raw)
    event = record.get("event") or record.get("message")
    if event == "signal_processed":
        result = record.get("result") or {}
        ok = (result.get("status") == "ACCEPTED"
              and isinstance(result.get("entry_price"), (int, float))
              and isinstance(result.get("stop_price"), (int, float)))
        return "entry" if ok else "useless"
    if event == "position_managed":
        return "useless" if (record.get("action") or {}).get("ticker") in (None, "", "*") else "managed"
    return "useless"


def _assert_same_reading(tickers, audit: FundAudit, path: Path) -> None:
    for ticker in tickers:
        assert pm._history(ticker, audit) == pm._history(ticker, path), ticker
        assert pm.ladder_history(ticker, audit) == pm.ladder_history(ticker, path), ticker
        assert pm.last_recorded_stop(ticker, audit) == pm.last_recorded_stop(ticker, path), ticker


# --------------------------------------------------------------------------- #
# 1. The FundAudit and a whole-file record read back identically
# --------------------------------------------------------------------------- #


@pytest.fixture
def whole_file(tmp_path):
    """A plain whole-file record written by the production handler, closed afterwards."""
    path = tmp_path / "whole_file.log"
    handler = _production_handler(path)
    yield path, handler
    handler.close()


def test_the_manager_reads_the_same_state_from_a_fund_audit_as_from_the_whole_file(whole_file):
    """Forty-five sessions of the real engine and manager on a simulated book,
    every line written both to a FundAudit and, through the production
    handler, to a plain file. After every session and for every ticker, the
    manager's readers must agree -- and the FundAudit's lines must be the
    file's own lines, byte for byte, from the latest entry on."""
    bars = _universe()
    feed = SimFeed(bars)
    audit = FundAudit("equivalence", keep_actions=True)
    record, handler = whole_file
    audit.logger.addHandler(handler)
    broker = SimBroker("equivalence", 100_000.0, quote=feed.get_latest_price)
    engine = ExecutionEngine(broker, feed, audit_logger=audit.logger)
    manager = pm.PositionManager(broker, feed, audit_path=audit, audit_logger=audit.logger)
    tickers = bars.tickers()
    statuses: list[tuple[str, str]] = []
    add_ons: list[str] = []

    for i, day in enumerate(d.date() for d in DAYS[START:START + 45]):
        feed.at_open(day)
        broker.day = day
        broker.fill_gapped_stops({t: bars.bar(t, day)[0] for t in tickers})
        manager.manage()
        for ticker in tickers:
            # Mostly one signal per name not held; now and then an add-on to a
            # held one (sized as an addition, restarting its ladder, or refused
            # for want of room) and a same-day repeat.
            if ticker in broker.positions and not (i % 9 == 4 and ticker in ("TLT", "XLE")):
                continue
            bias = LEANING.get(ticker) or ("BULLISH" if i % 2 else "BEARISH")
            held = ticker in broker.positions
            statuses.append((ticker, engine.execute(_signal(ticker, bias)).status.value))
            if held:
                add_ons.append(statuses[-1][1])
            if i % 11 == 3:
                engine.execute(_signal(ticker, bias))
        if i == 20:
            # Lines the manager can never use, written through the same logger:
            # a "*" failure, an ERROR and a REJECTED that carry prices, an
            # ACCEPTED without them, a NEUTRAL, and another event altogether.
            pm._record(pm.ManagementAction(ticker="*", action=pm.ERROR, reason="BrokerError: down"), audit.logger)
            for status, prices in ((ExecutionStatus.ERROR, (1.0, 0.5)), (ExecutionStatus.REJECTED, (2.0, 1.5)),
                                   (ExecutionStatus.ACCEPTED, (None, None))):
                log_execution(_signal("TLT", "BULLISH"), ExecutionResult(
                    status=status, ticker="TLT", bias=Bias.BULLISH, conviction=0.6, reason="injected",
                    entry_price=prices[0], stop_price=prices[1]), logger=audit.logger)
            engine.execute(_signal("TLT", "NEUTRAL"))
            audit.logger.info("heartbeat", extra={"action": {"ticker": "TLT", "new_stop": 1.0}})
        broker.fill_touched_stops({t: bars.bar(t, day)[2] for t in tickers},
                                  {t: bars.bar(t, day)[1] for t in tickers})
        broker.remember_marks({t: bars.bar(t, day)[3] for t in tickers})
        # "*" is not asked for: no position is ever called that, so the
        # manager never reads it, and the FundAudit does not keep it.
        _assert_same_reading([*tickers, "NOPE"], audit, record)

    # Line for line: what the FundAudit keeps is the file's latest qualifying
    # entry for the ticker and every management line after it, verbatim.
    raw = [line for line in record.read_text(encoding="utf-8").splitlines() if line.strip()]
    for ticker in tickers:
        mine = [line for line in raw if _mentions(line, ticker)]
        starts = [i for i, line in enumerate(mine) if _classify(line) == "entry"]
        expected = [line for line in mine[starts[-1] if starts else 0:] if _classify(line) != "useless"]
        assert audit.lines_for(ticker) == expected, ticker
        assert audit.lines_for(ticker.lower()) == expected
    assert audit.dropped == sum(1 for line in raw if _classify(line) == "useless")

    # The scenario did what it claims to exercise; otherwise agreement proves little.
    actions = audit.actions
    kinds = {a["action"] for a in actions}
    assert {pm.TRANCHE_TAKEN, pm.GROUP_CAP_TRIMMED, pm.STOP_RAISED, pm.HELD} <= kinds
    assert any(a["action"] == pm.STOP_RAISED and a["rung"] is None for a in actions)       # a trail
    assert any(a["action"] == pm.TRANCHE_TAKEN and a["rung"] == 1 for a in actions)        # the second rung
    assert any(a["action"] == pm.TRANCHE_TAKEN and a["side"] == "sell" for a in actions)   # a short's rung
    entries = [json.loads(line) for line in raw if _classify(line) == "entry"]
    per_ticker = {t: sum(1 for e in entries if e["result"]["ticker"] == t) for t in tickers}
    assert max(per_ticker.values()) >= 3                                                   # re-entries
    assert any(f.kind == "stop" and f.gapped for f in broker.fills)                        # a gap-through
    assert ("TLT", "ACCEPTED") in statuses and any(s == "REJECTED" for _, s in statuses)
    assert any("no room for" in line for line in raw)                                     # a refused add-on
    assert {"ACCEPTED", "REJECTED"} <= set(add_ons)                                     # an add-on restarts a ladder
    assert any(json.loads(line).get("result", {}).get("status") == "REJECTED"
               and json.loads(line)["result"].get("entry_price") for line in raw
               if json.loads(line).get("event") == "signal_processed")


def _mentions(raw: str, ticker: str) -> bool:
    record = json.loads(raw)
    owner = (record.get("result") or record.get("action") or {}).get("ticker")
    return str(owner or "").upper() == ticker


# --------------------------------------------------------------------------- #
# 2. What is kept, what is dropped, what restarts
# --------------------------------------------------------------------------- #


def _result(status: ExecutionStatus, ticker: str = "LLY", entry=None, stop=None) -> ExecutionResult:
    return ExecutionResult(status=status, ticker=ticker, bias=Bias.BULLISH, conviction=0.6,
                           reason=status.value.lower(), entry_price=entry, stop_price=stop)


def test_rejected_errored_and_star_lines_are_dropped_and_an_accepted_entry_restarts_the_ticker():
    audit = FundAudit("keep")
    signal = _signal("LLY", "BULLISH")

    log_execution(signal, _result(ExecutionStatus.ACCEPTED, entry=100.0, stop=96.0), logger=audit.logger)
    pm._record(pm.ManagementAction(ticker="LLY", action=pm.TRANCHE_TAKEN, rung=0, qty_closed=3,
                                   new_stop=100.0), audit.logger)
    assert len(audit.lines_for("LLY")) == 2

    # None of these may touch LLY's record: a REJECTED and an ERROR that carry
    # prices, an ACCEPTED that does not, a "*" failure, a line without a
    # ticker, and an event that is not the manager's.
    log_execution(signal, _result(ExecutionStatus.REJECTED, entry=150.0, stop=140.0), logger=audit.logger)
    log_execution(signal, _result(ExecutionStatus.ERROR, entry=150.0, stop=140.0), logger=audit.logger)
    log_execution(signal, _result(ExecutionStatus.ACCEPTED), logger=audit.logger)
    pm._record(pm.ManagementAction(ticker="*", action=pm.ERROR, reason="BrokerError: down"), audit.logger)
    pm._record(pm.ManagementAction(ticker="", action=pm.ERROR), audit.logger)
    audit.logger.info("something_else", extra={"action": {"ticker": "LLY"}})
    assert audit.dropped == 6
    assert len(audit.lines_for("LLY")) == 2
    assert audit.lines_for("*") == []
    entry, rungs = pm.ladder_history("LLY", audit)
    assert entry["entry_price"] == 100.0 and [r["rung"] for r in rungs] == [0]
    assert pm.last_recorded_stop("LLY", audit) == 100.0

    # A qualifying ACCEPTED -- an add-on, or a re-entry -- restarts the ladder:
    # the rung taken on the old position is no longer counted.
    log_execution(signal, _result(ExecutionStatus.ACCEPTED, entry=110.0, stop=104.0), logger=audit.logger)
    assert len(audit.lines_for("LLY")) == 1
    entry, rungs = pm.ladder_history("LLY", audit)
    assert entry["entry_price"] == 110.0 and rungs == []
    assert pm.last_recorded_stop("LLY", audit) == 104.0

    # Other tickers are untouched by LLY's restart, and lookups ignore case and space.
    pm._record(pm.ManagementAction(ticker="NVDA", action=pm.HELD, new_stop=90.0), audit.logger)
    log_execution(signal, _result(ExecutionStatus.ACCEPTED, entry=111.0, stop=105.0), logger=audit.logger)
    assert len(audit.lines_for(" nvda ")) == 1
    assert pm.last_recorded_stop("NVDA", audit) == 90.0


def test_a_fund_audit_line_is_formatted_exactly_as_the_live_handler_formats_it(whole_file):
    audit = FundAudit("format")
    path, handler = whole_file
    audit.logger.addHandler(handler)
    log_execution(_signal("LLY", "BULLISH"), _result(ExecutionStatus.ACCEPTED, entry=100.0, stop=96.0),
                  logger=audit.logger)
    pm._record(pm.ManagementAction(ticker="LLY", action=pm.ERROR, reason="MarketDataError: x"), audit.logger)
    written = path.read_text(encoding="utf-8").splitlines()
    assert audit.lines_for("LLY") == written
    first = json.loads(written[0])
    assert first["event"] == "signal_processed" and first["level"] == "INFO" and "ts" in first
    assert json.loads(written[1])["level"] == "ERROR"


def test_a_fund_audit_is_invisible_to_every_other_logger(caplog):
    audit = FundAudit("isolated-fund")
    with caplog.at_level(logging.DEBUG):
        pm._record(pm.ManagementAction(ticker="LLY", action=pm.HELD), audit.logger)
        log_execution(_signal("LLY", "BULLISH"), _result(ExecutionStatus.ACCEPTED, entry=1.0, stop=0.5),
                      logger=audit.logger)
    assert caplog.records == []
    assert not audit.logger.propagate
    # Not in logging's registry, so a thousand funds leave nothing behind.
    assert "shadow.audit.isolated-fund" not in logging.Logger.manager.loggerDict
    assert audit.logger is not logging.getLogger("shadow.audit.isolated-fund")


def test_read_text_is_every_kept_line():
    audit = FundAudit("text")
    pm._record(pm.ManagementAction(ticker="LLY", action=pm.HELD), audit.logger)
    pm._record(pm.ManagementAction(ticker="NVDA", action=pm.HELD), audit.logger)
    pm._record(pm.ManagementAction(ticker="*", action=pm.ERROR), audit.logger)
    lines = audit.read_text().splitlines()
    assert sorted(lines) == sorted(audit.lines_for("LLY") + audit.lines_for("NVDA"))


# --------------------------------------------------------------------------- #
# 3. Seeding from the live log, and forgetting
# --------------------------------------------------------------------------- #


def _live(extra: dict, ts: str, level: str, event: str) -> str:
    """A line in the live log's own shape: extra fields first, then ts, level, event."""
    return json.dumps({"taskName": None, **extra, "ts": ts, "level": level, "event": event})


def _live_signal(ticker, status, bias, reason, ts, **result) -> str:
    fields = {"quantity": None, "side": None, "entry_price": None, "stop_price": None, "atr": None,
              "order_id": None, "timestamp": "2026-09-15T16:54:47.800832Z"}
    fields.update(result)
    return _live({"signal": {"ticker": ticker, "bias": bias, "conviction": 0.55, "rationale": "r",
                             "news_score": 0.1, "key_factors": ["k"]},
                  "result": {"status": status, "ticker": ticker, "bias": bias, "conviction": 0.55,
                             "reason": reason, **fields}},
                 ts, "ERROR" if status == "ERROR" else "INFO", "signal_processed")


def _live_action(ticker, action, ts, level="INFO", **fields) -> str:
    base = {"ticker": ticker, "action": action, "side": "buy", "gain_r": 0.0, "price": 0.0, "qty_closed": 0,
            "remaining_qty": 0, "rung": None, "old_stop": None, "new_stop": None, "order_id": "", "r": 0.0,
            "r_estimated": False, "reason": ""}
    base.update(fields)
    return _live({"action": base}, ts, level, "position_managed")


def _real_shaped_log() -> list[str]:
    return [
        _live_signal("NVDA", "REJECTED", "NEUTRAL", "bias is NEUTRAL; no trade", "2026-09-15 16:54:47,801"),
        _live_signal("LLY", "ACCEPTED", "BULLISH", "submitted buy 4 LLY @ ~1147.19, stop 1085.29",
                     "2026-09-15 18:45:10,457", quantity=4, side="buy", entry_price=1147.18994140625,
                     stop_price=1085.29, atr=30.95, order_id="0f3c"),
        _live_action("LLY", "held", "2026-09-16 18:47:57,207", gain_r=-0.12, price=1140.06005859375,
                     remaining_qty=4, old_stop=1085.29, new_stop=1085.29, r=61.8999),
        _live_signal("LQD", "ERROR", "BEARISH", "BrokerError: asset LQD cannot be sold short",
                     "2026-09-16 18:48:01,002"),
        _live_signal("NVDA", "ACCEPTED", "BULLISH", "submitted buy 23 NVDA @ ~215.00, stop 212.84",
                     "2026-09-17 15:47:40,100", quantity=23, side="buy", entry_price=215.0, stop_price=212.84),
        _live_action("NVDA", "tranche_taken", "2026-09-22 15:07:07,666", gain_r=1.04, price=228.6699981689453,
                     qty_closed=7, remaining_qty=16, rung=0, old_stop=212.84, new_stop=216.23, r=13.2),
        _live_action("NVDA", "error", "2026-09-21 15:07:40,654", level="ERROR", side="buy",
                     reason="BrokerError: close_position failed for NVDA"),
        _live_action("*", "error", "2026-09-21 15:07:41,000", level="ERROR", reason="BrokerError: down"),
        _live_action("IEF", "group_cap_trimmed", "2026-09-24 15:06:57,086", side="sell", price=89.985,
                     qty_closed=11, remaining_qty=120, old_stop=91.28, new_stop=91.28, stop_qty=120),
        _live_action("LLY", "stop_raised", "2026-09-24 15:07:00,000", gain_r=0.5, price=1170.0,
                     remaining_qty=4, old_stop=1085.29, new_stop=1100.5, r=61.8999, reason="trailing stop"),
        # What any long-running file collects: a truncated tail, a blank, a
        # non-object, and a line from a plain formatter (``message``, not ``event``).
        '{"taskName": null, "action": {"ticker": "LLY", "act',
        "",
        "[1, 2, 3]",
        json.dumps({"message": "position_managed", "action": {"ticker": "lly", "action": "held",
                                                               "new_stop": 1101.0}}),
    ]


def test_seed_files_real_shaped_lines_exactly_as_the_whole_file_reads_them(tmp_path):
    lines = _real_shaped_log()
    path = tmp_path / "seeded.log"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    audit = FundAudit("seeded")
    kept = audit.seed(lines)
    # LLY: entry, held, stop_raised, plain-formatter held; NVDA: entry, tranche,
    # error; IEF: trim. The NEUTRAL, the ERROR, the "*" and the junk are not kept.
    assert kept == 8
    for ticker in ("LLY", "NVDA", "IEF", "LQD"):
        assert pm._history(ticker, audit) == pm._history(ticker, path)
        assert pm.ladder_history(ticker, audit) == pm.ladder_history(ticker, path)
        assert pm.last_recorded_stop(ticker, audit) == pm.last_recorded_stop(ticker, path)
    assert pm.last_recorded_stop("LLY", audit) == 1101.0
    assert pm.last_recorded_stop("NVDA", audit) == 216.23
    entry, rungs = pm.ladder_history("NVDA", audit)
    assert entry["entry_price"] == 215.0 and [r["rung"] for r in rungs] == [0]
    # Seeded lines are kept verbatim, so they are the live file's own bytes.
    assert audit.lines_for("LLY")[0] == lines[1]


def test_a_seeded_record_continues_with_what_the_fund_writes_itself():
    audit = FundAudit("continued")
    audit.seed(_real_shaped_log())
    pm._record(pm.ManagementAction(ticker="NVDA", action=pm.TRANCHE_TAKEN, rung=1, qty_closed=5,
                                   new_stop=228.0), audit.logger)
    entry, rungs = pm.ladder_history("NVDA", audit)
    assert entry["entry_price"] == 215.0 and [r["rung"] for r in rungs] == [0, 1]
    assert pm.last_recorded_stop("NVDA", audit) == 228.0


def test_a_seeded_re_entry_restarts_that_ticker():
    audit = FundAudit("reentry")
    audit.seed(_real_shaped_log() + [
        _live_signal("NVDA", "ACCEPTED", "BULLISH", "submitted buy 10 NVDA", "2026-09-25 15:00:00,000",
                     quantity=10, side="buy", entry_price=230.0, stop_price=220.0),
    ])
    entry, rungs = pm.ladder_history("NVDA", audit)
    assert entry["entry_price"] == 230.0 and rungs == []
    assert pm.last_recorded_stop("NVDA", audit) == 220.0


def test_forget_drops_only_the_named_tickers_whatever_their_case():
    audit = FundAudit("forget")
    audit.seed(_real_shaped_log())
    audit.forget([" lly ", "nvda", "NOT-HELD"])
    assert audit.lines_for("LLY") == [] and audit.lines_for("NVDA") == []
    assert pm.ladder_history("LLY", audit) == (None, [])
    assert pm.last_recorded_stop("NVDA", audit) is None
    assert len(audit.lines_for("IEF")) == 1


# --------------------------------------------------------------------------- #
# 4. The live audit log is unreachable during a shadow run
# --------------------------------------------------------------------------- #


class _Sentinel(logging.Handler):
    """Stands in for the live FileHandler: it must see nothing a shadow run writes."""

    def __init__(self) -> None:
        super().__init__(level=logging.DEBUG)
        self.seen: list[str] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.seen.append(record.getMessage())


@pytest.fixture
def live_logger():
    """The live audit logger, restored exactly afterwards, whatever a test does to it."""
    live = logging.getLogger("execution_audit")
    root = logging.getLogger()
    saved = (list(live.handlers), live.level, live.propagate, root.level)
    try:
        yield live
    finally:
        for handler in list(live.handlers):
            live.removeHandler(handler)
        for handler in saved[0]:
            live.addHandler(handler)
        live.setLevel(saved[1])
        live.propagate = saved[2]
        root.setLevel(saved[3])


def _stat(path: Path):
    return (path.stat().st_size, path.stat().st_mtime_ns) if path.exists() else None


@pytest.mark.parametrize("configured", [logging.NOTSET, logging.INFO, logging.WARNING],
                         ids=["never-configured", "as-get_audit_logger-sets-it", "quieter"])
def test_a_write_to_the_live_logger_inside_the_guard_raises_after_the_block(live_logger, configured):
    """``python -m shadow.run`` never configures the live logger, and sets the
    root to ERROR: an INFO line from a code path that forgot its fund's
    logger must still land in the tripwire, not vanish below a level."""
    live_logger.setLevel(configured)
    logging.getLogger().setLevel(logging.ERROR)
    sentinel = _Sentinel()
    live_logger.addHandler(sentinel)
    finished = False
    with pytest.raises(LiveAuditLeak) as leak:
        with live_audit_guarded():
            logging.getLogger("execution_audit").info("signal_processed")
            finished = True
    assert finished, "the leak must be reported after the block, not stop it mid-run"
    assert "signal_processed" in str(leak.value)
    assert sentinel.seen == []
    assert live_logger.handlers == [sentinel] and live_logger.level == configured


def test_the_guard_restores_the_live_handlers_and_is_silent_when_nothing_leaks(live_logger):
    sentinel = _Sentinel()
    live_logger.addHandler(sentinel)
    live_logger.setLevel(logging.INFO)
    live_logger.propagate = True
    with live_audit_guarded():
        assert sentinel not in live_logger.handlers and not live_logger.propagate
        FundAudit("quiet").logger.info("position_managed", extra={"action": {"ticker": "LLY"}})
    assert live_logger.handlers == [sentinel] and live_logger.propagate
    logging.getLogger("execution_audit").info("after the block")
    assert sentinel.seen == ["after the block"]


def test_the_guard_restores_the_live_handlers_when_the_body_raises(live_logger):
    sentinel = _Sentinel()
    live_logger.addHandler(sentinel)
    with pytest.raises(ZeroDivisionError):
        with live_audit_guarded():
            1 / 0
    assert live_logger.handlers == [sentinel]


def test_get_audit_logger_never_opens_the_live_file_inside_the_guard(live_logger, tmp_path):
    """The real ``app.logger.get_audit_logger`` opens its file only when the
    live logger has no handler. Inside the guard it has one -- the tripwire --
    so a forgotten ``logger=None`` can reach neither a new file nor the repo's."""
    for handler in list(live_logger.handlers):
        live_logger.removeHandler(handler)
    before = _stat(REPO_AUDIT_LOG)
    sentinel_path = tmp_path / "would_have_been_opened.log"
    with pytest.raises(LiveAuditLeak):
        with live_audit_guarded():
            assert live_logger.handlers, "the tripwire must be attached before anything can ask"
            got = _real_get_audit_logger(sentinel_path)
            assert got is live_logger
            assert _real_get_audit_logger() is live_logger          # the default: the repo's own file
            assert not any(isinstance(h, logging.FileHandler) for h in live_logger.handlers)
            got.info("signal_processed")
    assert not sentinel_path.exists()
    assert _stat(REPO_AUDIT_LOG) == before
    assert not any(isinstance(h, logging.FileHandler) for h in live_logger.handlers)
