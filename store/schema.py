"""The SQLite schema, in one place, as plain DDL.

Two tables, mirroring the two log files, plus a ``meta`` table carrying the
schema version so a future migration can tell what it is looking at.

**The database is derived, not authoritative.** The JSON-lines files under
``logs/`` remain the system of record: they are what the orchestrator writes,
what git carries between runs, and what can still be read with ``grep`` in ten
years. Everything here can be deleted and rebuilt from them in seconds. That
single property is what makes this safe to add to a system that trades -- a
corrupt index costs a rebuild, never a cycle and never a record.

Two consequences follow from it, and both are deliberate:

* Every row keeps the byte-exact ``raw`` line it came from. The extracted
  columns are a convenience for the queries worth indexing; anything else is
  reachable through SQLite's built-in JSON1 functions, e.g.::

      SELECT json_extract(raw, '$.context.technicals.rsi14') FROM signals;

  So a column that was never anticipated is a query away rather than a
  migration away, and the archive cannot become less readable than the file.

* Loading is idempotent, keyed on a hash of that raw line. Re-running the
  loader over a journal that has grown by one line inserts one row. This
  matters because the natural way to run it is "after every cycle", over a
  file that is append-only and mostly unchanged.
"""

from __future__ import annotations

from typing import Final

#: Bumped when the DDL below changes in a way a rebuild would not fix.
#: Because the database is derived, a mismatch is not an error to migrate
#: around -- it is a prompt to rebuild from the logs, which is cheap.
SCHEMA_VERSION: Final[int] = 1

#: One row per journalled cycle: what the model saw, said, and what came back.
#: Source: ``logs/signal_journal.log`` (``orchestrator/journal.py``).
SIGNALS_DDL: Final[str] = """
CREATE TABLE IF NOT EXISTS signals (
    id                 INTEGER PRIMARY KEY,
    -- Content hash of the source line. UNIQUE is what makes the loader
    -- idempotent; see the module docstring.
    line_hash          TEXT    NOT NULL UNIQUE,
    ingested_at        TEXT    NOT NULL,

    -- ISO-8601 UTC. NULL when the line carried no parseable timestamp at all.
    ts_utc             TEXT,
    -- 0 when the timestamp came from the formatter's tz-naive ``ts`` fallback
    -- rather than the explicit ``ts_utc`` field. The scorer refuses a same-day
    -- entry price on those, so the distinction has to survive into the index.
    ts_exact           INTEGER NOT NULL DEFAULT 0,
    -- UTC date, denormalised because "group by day" is the single most common
    -- question asked of this table.
    trade_date         TEXT,

    ticker             TEXT    NOT NULL,
    bias               TEXT,
    conviction         REAL,
    rationale          TEXT,

    news_score         REAL,
    technical_score    REAL,
    fundamental_score  REAL,
    analyst_score      REAL,
    insider_score      REAL,

    -- The engine's verdict, as the journal recorded it.
    outcome_status     TEXT,
    outcome_reason     TEXT,
    outcome_quantity   INTEGER,
    -- The join key to ``executions``. Exact, not fuzzy time-matching.
    order_id           TEXT,
    error              TEXT,

    -- Context health. The prompt asks for a null score when a dimension's
    -- data was missing, so null and 0.0 are different events. Lines journalled
    -- before it did carry a 0.0 for a missing dimension, and there only the
    -- gap count can tell that from a 0.0 scored on the merits.
    gap_count          INTEGER NOT NULL DEFAULT 0,

    -- Measured, not estimated: taken from the API's own usage report.
    model              TEXT,
    input_tokens       INTEGER,
    output_tokens      INTEGER,
    cost_usd           REAL,

    -- USD/ILS as of the signal. An FX move does not reduce a dollar return,
    -- it redenominates it, so the rate has to be pinned at entry.
    fx_rate            REAL,

    raw                TEXT    NOT NULL
);
"""

#: One row per execution decision. Source: ``logs/execution_audit.log``
#: (``app/logger.py``). This is the compliance record: what the engine *did*.
EXECUTIONS_DDL: Final[str] = """
CREATE TABLE IF NOT EXISTS executions (
    id            INTEGER PRIMARY KEY,
    line_hash     TEXT    NOT NULL UNIQUE,
    ingested_at   TEXT    NOT NULL,

    -- Preferred from ``result.timestamp``, which ExecutionResult stamps in UTC.
    -- The formatter's own ``ts`` is local time with no offset and is only a
    -- fallback; ``ts_exact`` records which one was used.
    ts_utc        TEXT,
    ts_exact      INTEGER NOT NULL DEFAULT 0,
    trade_date    TEXT,

    ticker        TEXT    NOT NULL,
    status        TEXT,
    reason        TEXT,
    bias          TEXT,
    conviction    REAL,

    quantity      INTEGER,
    side          TEXT,
    entry_price   REAL,
    stop_price    REAL,
    atr           REAL,
    order_id      TEXT,

    level         TEXT,
    raw           TEXT    NOT NULL
);
"""

META_DDL: Final[str] = """
CREATE TABLE IF NOT EXISTS meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
"""

#: Indexes chosen for the questions the scorer actually asks: slice by ticker,
#: walk forward in time, and filter to the directional calls.
INDEX_DDL: Final[tuple[str, ...]] = (
    "CREATE INDEX IF NOT EXISTS signals_ticker_ts ON signals (ticker, ts_utc);",
    "CREATE INDEX IF NOT EXISTS signals_ts ON signals (ts_utc);",
    "CREATE INDEX IF NOT EXISTS signals_date ON signals (trade_date);",
    "CREATE INDEX IF NOT EXISTS signals_bias ON signals (bias);",
    "CREATE INDEX IF NOT EXISTS signals_order ON signals (order_id);",
    "CREATE INDEX IF NOT EXISTS executions_ticker_ts ON executions (ticker, ts_utc);",
    "CREATE INDEX IF NOT EXISTS executions_status ON executions (status);",
    "CREATE INDEX IF NOT EXISTS executions_order ON executions (order_id);",
)

#: The signal and what the engine did with it, joined on the order id the
#: journal already records. This is the join the docs listed as missing: it is
#: what lets a question be asked about *filled* trades -- their size, entry and
#: stop -- rather than about close-to-close moves that ignore the stop-loss.
#:
#: A LEFT JOIN because most signals never become orders. A rejection is data.
DECISIONS_VIEW_DDL: Final[str] = """
CREATE VIEW IF NOT EXISTS decisions AS
SELECT
    s.ts_utc              AS ts_utc,
    s.trade_date          AS trade_date,
    s.ticker              AS ticker,
    s.bias                AS bias,
    s.conviction          AS conviction,
    s.news_score          AS news_score,
    s.technical_score     AS technical_score,
    s.fundamental_score   AS fundamental_score,
    s.analyst_score       AS analyst_score,
    s.insider_score       AS insider_score,
    s.outcome_status      AS outcome_status,
    s.outcome_reason      AS outcome_reason,
    s.gap_count           AS gap_count,
    s.cost_usd            AS cost_usd,
    s.fx_rate             AS fx_rate,
    e.quantity            AS quantity,
    e.side                AS side,
    e.entry_price         AS entry_price,
    e.stop_price          AS stop_price,
    e.atr                 AS atr,
    e.order_id            AS order_id
FROM signals s
LEFT JOIN executions e ON e.order_id = s.order_id AND s.order_id IS NOT NULL;
"""

#: Everything needed to bring an empty file up to the current schema.
ALL_DDL: Final[tuple[str, ...]] = (
    (META_DDL, SIGNALS_DDL, EXECUTIONS_DDL) + INDEX_DDL + (DECISIONS_VIEW_DDL,)
)
