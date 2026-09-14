#!/usr/bin/env python3
"""Ask the archive questions, from the shell.

    python store/query.py summary          # what is in there
    python store/query.py daily            # signals, conviction and cost per day
    python store/query.py tickers          # per-ticker behaviour
    python store/query.py rejections       # which guardrail bites, and how often
    python store/query.py costs            # tokens and dollars by day and model
    python store/query.py health           # missing-data and error rates
    python store/query.py trades           # signals that became real orders
    python store/query.py --sql "SELECT ..."

The connection is opened read-only, so nothing reachable from here can modify
the archive -- an ``UPDATE`` typed into ``--sql`` fails with "attempt to write
a readonly database" rather than editing the record of what was decided.

Every canned query below is ordinary SQL, printed with ``--explain``. They are
starting points to copy and change, not an API.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import settings as cfg  # noqa: E402
from store import database  # noqa: E402

#: Canned queries. Name -> (one-line purpose, SQL).
QUERIES: dict[str, tuple[str, str]] = {
    "summary": (
        "Row counts, date span and the spread of engine verdicts",
        """
        SELECT 'signals'                       AS what,
               COUNT(*)                        AS n,
               MIN(trade_date)                 AS first_day,
               MAX(trade_date)                 AS last_day,
               ROUND(AVG(conviction), 3)       AS mean_conviction
        FROM signals
        UNION ALL
        SELECT 'executions', COUNT(*), MIN(trade_date), MAX(trade_date), NULL
        FROM executions
        UNION ALL
        SELECT 'verdict: ' || COALESCE(outcome_status, 'none'),
               COUNT(*), MIN(trade_date), MAX(trade_date),
               ROUND(AVG(conviction), 3)
        FROM signals
        GROUP BY outcome_status
        """,
    ),
    "daily": (
        "Per-day volume, conviction and cost -- the drift check, as a table",
        """
        SELECT trade_date,
               COUNT(*)                                          AS signals,
               SUM(bias = 'BULLISH')                             AS bullish,
               SUM(bias = 'BEARISH')                             AS bearish,
               SUM(bias = 'NEUTRAL')                             AS neutral,
               ROUND(AVG(conviction), 3)                         AS mean_conviction,
               SUM(outcome_status = 'ACCEPTED')                  AS accepted,
               ROUND(SUM(COALESCE(cost_usd, 0)), 4)              AS cost_usd
        FROM signals
        WHERE trade_date IS NOT NULL
        GROUP BY trade_date
        ORDER BY trade_date
        """,
    ),
    "tickers": (
        "Per-ticker behaviour: how often it is called, how confidently, how often it trades",
        """
        SELECT ticker,
               COUNT(*)                                  AS cycles,
               ROUND(AVG(conviction), 3)                 AS mean_conviction,
               ROUND(MAX(conviction), 3)                 AS max_conviction,
               SUM(bias IN ('BULLISH', 'BEARISH'))       AS directional,
               SUM(outcome_status = 'ACCEPTED')          AS accepted,
               SUM(error IS NOT NULL)                    AS errors,
               ROUND(AVG(gap_count), 2)                  AS mean_gaps
        FROM signals
        GROUP BY ticker
        ORDER BY accepted DESC, mean_conviction DESC
        """,
    ),
    "rejections": (
        "Which reason stopped a signal becoming a trade, most common first",
        """
        SELECT COALESCE(outcome_reason, '(none recorded)')  AS reason,
               COUNT(*)                                     AS n,
               ROUND(AVG(conviction), 3)                    AS mean_conviction,
               COUNT(DISTINCT ticker)                       AS tickers
        FROM signals
        WHERE outcome_status = 'REJECTED'
        GROUP BY reason
        ORDER BY n DESC
        """,
    ),
    "costs": (
        "What the archive cost to produce, by day and model",
        """
        SELECT trade_date,
               COALESCE(model, '(unrecorded)')          AS model,
               COUNT(*)                                 AS calls,
               SUM(COALESCE(input_tokens, 0))           AS input_tokens,
               SUM(COALESCE(output_tokens, 0))          AS output_tokens,
               ROUND(SUM(COALESCE(cost_usd, 0)), 4)     AS cost_usd
        FROM signals
        WHERE trade_date IS NOT NULL
        GROUP BY trade_date, model
        ORDER BY trade_date, model
        """,
    ),
    "health": (
        "Data gaps and errors per day -- a degraded cycle still writes a signal",
        """
        SELECT trade_date,
               COUNT(*)                                 AS cycles,
               SUM(gap_count > 0)                       AS cycles_with_gaps,
               SUM(error IS NOT NULL)                   AS cycles_with_errors,
               SUM(ts_exact = 0)                        AS inexact_timestamps,
               SUM(conviction IS NULL)                  AS no_signal
        FROM signals
        WHERE trade_date IS NOT NULL
        GROUP BY trade_date
        ORDER BY trade_date
        """,
    ),
    "trades": (
        "Signals that became real orders, with the size and stop the engine chose",
        """
        SELECT ts_utc, ticker, bias,
               ROUND(conviction, 2)   AS conviction,
               quantity, side,
               ROUND(entry_price, 2)  AS entry,
               ROUND(stop_price, 2)   AS stop,
               ROUND(atr, 3)          AS atr,
               ROUND(100.0 * (entry_price - stop_price) / entry_price, 2) AS stop_pct,
               order_id
        FROM decisions
        WHERE order_id IS NOT NULL
        ORDER BY ts_utc DESC
        """,
    ),
    "errors": (
        "Cycles that failed, newest first -- the ones worth reading by hand",
        """
        SELECT ts_utc, ticker, error, outcome_status, outcome_reason
        FROM signals
        WHERE error IS NOT NULL
        ORDER BY ts_utc DESC
        LIMIT 100
        """,
    ),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="query",
        description="Read-only queries over the log index.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="queries: " + ", ".join(QUERIES),
    )
    parser.add_argument(
        "query", nargs="?", choices=sorted(QUERIES), help="a canned query to run"
    )
    parser.add_argument("--sql", help="run this SQL instead of a canned query")
    parser.add_argument(
        "--db", type=Path, default=cfg.DATABASE_PATH,
        help="database to read (default: %(default)s)",
    )
    parser.add_argument("--limit", type=int, default=0, help="show at most N rows")
    parser.add_argument("--json", action="store_true", help="emit JSON rather than a table")
    parser.add_argument(
        "--explain", action="store_true",
        help="print the SQL a canned query runs, and stop",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.sql and args.query:
        print("Pass a canned query or --sql, not both.", file=sys.stderr)
        return 2
    if not args.sql and not args.query:
        build_parser().print_help()
        return 2

    sql = args.sql or QUERIES[args.query][1]
    if args.explain:
        print(sql.strip())
        return 0

    try:
        connection = database.connect_ro(args.db)
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        return 1

    try:
        rows = connection.execute(sql).fetchall()
    except sqlite3.Error as exc:
        print(f"SQL error: {exc}", file=sys.stderr)
        return 1
    finally:
        connection.close()

    if args.limit > 0:
        rows = rows[: args.limit]

    if args.json:
        print(json.dumps([dict(row) for row in rows], indent=2, default=str))
    else:
        if args.query:
            print(QUERIES[args.query][0])
            print()
        print(render_table(rows))
    return 0


def render_table(rows: list[sqlite3.Row]) -> str:
    """Aligned columns. Deliberately plain: no dependency, pipes into grep."""
    if not rows:
        return "(no rows)"
    headers = list(rows[0].keys())
    cells = [[_cell(row[name]) for name in headers] for row in rows]
    widths = [
        max(len(headers[i]), *(len(row[i]) for row in cells)) for i in range(len(headers))
    ]
    lines = [
        "  ".join(header.ljust(widths[i]) for i, header in enumerate(headers)),
        "  ".join("-" * widths[i] for i in range(len(headers))),
    ]
    lines.extend("  ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)) for row in cells)
    lines.append(f"\n{len(rows)} row{'s' if len(rows) != 1 else ''}")
    return "\n".join(lines)


def _cell(value) -> str:
    if value is None:
        return "-"
    if isinstance(value, float):
        return f"{value:g}"
    text = str(value)
    # A rationale is 2000 characters; a terminal is not.
    return text if len(text) <= 60 else text[:57] + "..."


if __name__ == "__main__":
    raise SystemExit(main())
