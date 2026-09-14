"""Loading the logs into the index, including the lines a long-lived log collects.

The index is derived data, and the one property that makes that safe is that
it agrees with the file it came from. Most of what is pinned here is that
agreement, in its several forms: same entries, byte-exact originals, and a
re-load that adds nothing.
"""

from __future__ import annotations

import json

from analysis.reader import read_database, read_journal
from store import database, loader

JOURNAL_LINE = {
    "ts": "2026-09-15 14:05:02,331",
    "ts_utc": "2026-09-15T14:05:02.331000+00:00",
    "level": "INFO",
    "event": "signal_generated",
    "ticker": "nvda",
    "context": {
        "headlines": ["Chipmaker raises guidance"],
        "technicals": {"rsi14": 61.2, "last_close": 180.5},
        "gaps": ["insider filings unavailable: HTTP 429"],
    },
    "signal": {
        "ticker": "NVDA", "bias": "BULLISH", "conviction": 0.72,
        "rationale": "Guidance raise corroborated by an uptrend.",
        "news_score": 0.8, "technical_score": 0.5, "fundamental_score": None,
        "analyst_score": 0.6, "insider_score": 0.1,
        "key_factors": ["Guidance raised 20%"],
    },
    "outcome": {
        "mode": "direct", "status": "ACCEPTED", "reason": "sized and submitted",
        "quantity": 50, "order_id": "ord-1",
    },
    "error": None,
    "usage": {
        "model": "claude-opus-5", "input_tokens": 4100, "output_tokens": 260,
        "cost_usd": 0.0812,
    },
    "fx": {"symbol": "USDILS=X", "rate": 3.71, "change_3mo_pct": -0.02, "gap": None},
}

AUDIT_LINE = {
    "ts": "2026-09-15 17:05:02,400",
    "level": "INFO",
    "event": "signal_processed",
    "signal": {"ticker": "NVDA", "bias": "BULLISH", "conviction": 0.72},
    "result": {
        "status": "ACCEPTED", "ticker": "NVDA", "bias": "BULLISH", "conviction": 0.72,
        "reason": "sized and submitted", "quantity": 50, "side": "buy",
        "entry_price": 180.5, "stop_price": 171.2, "atr": 4.65, "order_id": "ord-1",
        "timestamp": "2026-09-15T14:05:02.400000+00:00",
    },
}


def line(payload: dict) -> str:
    return json.dumps(payload) + "\n"


def db(tmp_path):
    return database.connect_rw(tmp_path / "trading.db")


# --------------------------------------------------------------------------- #
# Row construction
# --------------------------------------------------------------------------- #


def test_a_full_journal_line_becomes_a_row_field_by_field(tmp_path):
    connection = db(tmp_path)
    result = loader.load_signals(connection, [line(JOURNAL_LINE)])

    assert (result.inserted, result.duplicates, result.skipped) == (1, 0, 0)
    row = connection.execute("SELECT * FROM signals").fetchone()

    assert row["ticker"] == "NVDA"  # normalised, as the file reader normalises it
    assert row["ts_utc"] == "2026-09-15T14:05:02.331000+00:00"
    assert row["ts_exact"] == 1
    assert row["trade_date"] == "2026-09-15"
    assert row["bias"] == "BULLISH" and row["conviction"] == 0.72
    assert row["news_score"] == 0.8
    assert row["fundamental_score"] is None  # a missing score is not a zero
    assert row["outcome_status"] == "ACCEPTED"
    assert row["outcome_quantity"] == 50
    assert row["order_id"] == "ord-1"
    assert row["gap_count"] == 1
    assert row["model"] == "claude-opus-5"
    assert row["input_tokens"] == 4100 and row["cost_usd"] == 0.0812
    assert row["fx_rate"] == 3.71


def test_the_naive_timestamp_is_a_fallback_and_is_flagged(tmp_path):
    """Same rule as the file reader: a tz-naive stamp never earns a same-day entry."""
    payload = {k: v for k, v in JOURNAL_LINE.items() if k != "ts_utc"}
    connection = db(tmp_path)
    loader.load_signals(connection, [line(payload)])

    row = connection.execute("SELECT ts_utc, ts_exact FROM signals").fetchone()
    assert row["ts_utc"] == "2026-09-15T14:05:02.331000+00:00"
    assert row["ts_exact"] == 0


def test_an_execution_prefers_its_own_utc_stamp_over_the_formatters(tmp_path):
    """``ts`` is local time with no offset; ``result.timestamp`` is real UTC."""
    connection = db(tmp_path)
    loader.load_executions(connection, [line(AUDIT_LINE)])

    row = connection.execute("SELECT * FROM executions").fetchone()
    assert row["ts_utc"] == "2026-09-15T14:05:02.400000+00:00"  # not the 17:05 ``ts``
    assert row["ts_exact"] == 1
    assert row["entry_price"] == 180.5 and row["stop_price"] == 171.2
    assert row["side"] == "buy" and row["order_id"] == "ord-1"


def test_an_execution_without_its_own_stamp_falls_back_and_is_flagged(tmp_path):
    payload = {**AUDIT_LINE, "result": {k: v for k, v in AUDIT_LINE["result"].items()}}
    del payload["result"]["timestamp"]
    connection = db(tmp_path)
    loader.load_executions(connection, [line(payload)])

    row = connection.execute("SELECT ts_utc, ts_exact FROM executions").fetchone()
    assert row["ts_utc"] == "2026-09-15T17:05:02.400000+00:00"
    assert row["ts_exact"] == 0


def test_a_cycle_that_produced_no_signal_is_still_a_row(tmp_path):
    """The failures are the rows worth reading, so they must survive the load."""
    payload = {**JOURNAL_LINE, "signal": None, "outcome": None,
               "error": "model returned a signal for the wrong ticker"}
    connection = db(tmp_path)
    assert loader.load_signals(connection, [line(payload)]).inserted == 1

    row = connection.execute("SELECT * FROM signals").fetchone()
    assert row["bias"] is None and row["conviction"] is None
    assert row["error"] == "model returned a signal for the wrong ticker"


# --------------------------------------------------------------------------- #
# Tolerance
# --------------------------------------------------------------------------- #


def test_a_truncated_final_line_is_counted_not_fatal(tmp_path):
    """What a killed process leaves behind must not cost the rest of the file."""
    connection = db(tmp_path)
    result = loader.load_signals(
        connection, [line(JOURNAL_LINE), '{"ts": "2026-09-15 14:0', line(JOURNAL_LINE)]
    )

    # The repeated line is the same event, so one row -- but it is still
    # counted, because every line read has to land in exactly one bucket.
    assert (result.inserted, result.duplicates, result.skipped) == (1, 1, 1)
    assert result.total == 3


def test_a_line_that_is_not_a_record_is_skipped(tmp_path):
    connection = db(tmp_path)
    result = loader.load_signals(
        connection, ['{"ts": "x", "event": "startup"}', "[1, 2, 3]", "null"]
    )
    assert (result.inserted, result.skipped) == (0, 3)


def test_blank_lines_are_not_counted_at_all(tmp_path):
    connection = db(tmp_path)
    result = loader.load_signals(connection, ["\n", "   \n", line(JOURNAL_LINE)])
    assert (result.inserted, result.skipped, result.total) == (1, 0, 1)


def test_a_missing_file_is_an_empty_load_not_an_error(tmp_path):
    """A journal can exist with no audit beside it: nothing reached the engine."""
    connection = db(tmp_path)
    result = loader.load_file(connection, tmp_path / "absent.log", "executions")
    assert result.total == 0


# --------------------------------------------------------------------------- #
# Idempotence
# --------------------------------------------------------------------------- #


def test_reloading_an_unchanged_file_inserts_nothing(tmp_path):
    connection = db(tmp_path)
    lines = [line(JOURNAL_LINE)]

    assert loader.load_signals(connection, lines).inserted == 1
    again = loader.load_signals(connection, lines)

    assert (again.inserted, again.duplicates) == (0, 1)
    assert connection.execute("SELECT COUNT(*) FROM signals").fetchone()[0] == 1


def test_a_journal_that_grew_by_one_line_costs_one_insert(tmp_path):
    """The natural way to run this is after every cycle, over an append-only file."""
    connection = db(tmp_path)
    second = {**JOURNAL_LINE, "ts_utc": "2026-09-15T15:05:02.331000+00:00"}

    loader.load_signals(connection, [line(JOURNAL_LINE)])
    grown = loader.load_signals(connection, [line(JOURNAL_LINE), line(second)])

    assert (grown.inserted, grown.duplicates) == (1, 1)
    assert connection.execute("SELECT COUNT(*) FROM signals").fetchone()[0] == 2


def test_two_tickers_in_one_cycle_are_two_rows(tmp_path):
    """Idempotence keys on content, so it must not collapse distinct events."""
    connection = db(tmp_path)
    other = {**JOURNAL_LINE, "ticker": "MSFT"}
    result = loader.load_signals(connection, [line(JOURNAL_LINE), line(other)])

    assert result.inserted == 2


# --------------------------------------------------------------------------- #
# Agreement with the file it was built from
# --------------------------------------------------------------------------- #


def test_the_original_line_is_kept_byte_exact(tmp_path):
    """So a field nobody thought to columnise is a query away, not a migration."""
    connection = db(tmp_path)
    loader.load_signals(connection, [line(JOURNAL_LINE)])

    raw = connection.execute("SELECT raw FROM signals").fetchone()[0]
    assert json.loads(raw) == JOURNAL_LINE

    rsi = connection.execute(
        "SELECT json_extract(raw, '$.context.technicals.rsi14') FROM signals"
    ).fetchone()[0]
    assert rsi == 61.2


def test_the_database_and_the_file_give_the_scorer_the_same_entries(tmp_path):
    """Two sources, one parser. A report must not depend on which was read."""
    path = tmp_path / "signal_journal.log"
    payloads = [
        JOURNAL_LINE,
        {**JOURNAL_LINE, "ticker": "MSFT", "ts_utc": "2026-09-16T14:05:02+00:00"},
        {**JOURNAL_LINE, "ticker": "GLD", "ts_utc": "2026-09-17T14:05:02+00:00"},
    ]
    path.write_text("".join(line(p) for p in payloads), encoding="utf-8")

    db_path = tmp_path / "trading.db"
    connection = database.connect_rw(db_path)
    loader.load_file(connection, path, "signals")
    connection.close()

    from_file = read_journal(path)
    from_db = read_database(db_path)

    assert [e.ticker for e in from_db.entries] == [e.ticker for e in from_file.entries]
    assert [e.conviction for e in from_db.entries] == [e.conviction for e in from_file.entries]
    assert [e.timestamp for e in from_db.entries] == [e.timestamp for e in from_file.entries]


def test_since_narrows_the_window_the_scorer_sees(tmp_path):
    path = tmp_path / "signal_journal.log"
    payloads = [
        {**JOURNAL_LINE, "ts_utc": "2026-09-15T14:05:02+00:00"},
        {**JOURNAL_LINE, "ts_utc": "2026-09-16T14:05:02+00:00"},
        {**JOURNAL_LINE, "ts_utc": "2026-09-17T14:05:02+00:00"},
    ]
    path.write_text("".join(line(p) for p in payloads), encoding="utf-8")

    db_path = tmp_path / "trading.db"
    connection = database.connect_rw(db_path)
    loader.load_file(connection, path, "signals")
    connection.close()

    assert len(read_database(db_path).entries) == 3
    assert len(read_database(db_path, since="2026-09-16").entries) == 2
    assert len(read_database(db_path, since="2026-09-18").entries) == 0


# --------------------------------------------------------------------------- #
# The join the scorer could not previously make
# --------------------------------------------------------------------------- #


def test_the_decisions_view_joins_a_signal_to_the_order_it_became(tmp_path):
    """Close-to-close returns ignore the stop. This is what makes the stop visible."""
    connection = db(tmp_path)
    loader.load_signals(connection, [line(JOURNAL_LINE)])
    loader.load_executions(connection, [line(AUDIT_LINE)])

    row = connection.execute("SELECT * FROM decisions").fetchone()
    assert row["ticker"] == "NVDA"
    assert row["conviction"] == 0.72          # from the signal
    assert row["quantity"] == 50              # from the execution
    assert row["entry_price"] == 180.5 and row["stop_price"] == 171.2


def test_a_rejected_signal_still_appears_in_decisions(tmp_path):
    """A rejection is data. A LEFT JOIN is what keeps it from disappearing."""
    payload = {**JOURNAL_LINE,
               "outcome": {"mode": "direct", "status": "REJECTED",
                           "reason": "conviction 0.41 below floor 0.60",
                           "quantity": None, "order_id": None}}
    connection = db(tmp_path)
    loader.load_signals(connection, [line(payload)])

    row = connection.execute("SELECT * FROM decisions").fetchone()
    assert row["outcome_status"] == "REJECTED"
    assert row["order_id"] is None and row["quantity"] is None


def test_load_result_adds_up(tmp_path):
    total = loader.LoadResult(inserted=2, duplicates=1) + loader.LoadResult(skipped=3)
    assert (total.inserted, total.duplicates, total.skipped, total.total) == (2, 1, 3, 6)
