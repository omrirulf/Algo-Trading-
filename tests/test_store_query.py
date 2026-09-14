"""The canned queries, checked against a real database rather than by eye.

Each one is a starting point somebody will copy and change, so the property
worth pinning is narrow: it is valid SQL against the current schema, and it
runs. A query that silently stopped parsing after a column was renamed would
otherwise only be found by the person who needed the answer.
"""

from __future__ import annotations

import json

from store import database, loader, query
from tests.test_store_loader import AUDIT_LINE, JOURNAL_LINE, line


def loaded(tmp_path):
    path = tmp_path / "trading.db"
    connection = database.connect_rw(path)
    loader.load_signals(connection, [
        line(JOURNAL_LINE),
        line({**JOURNAL_LINE, "ticker": "MSFT", "ts_utc": "2026-09-16T14:05:02+00:00"}),
    ])
    loader.load_executions(connection, [line(AUDIT_LINE)])
    connection.close()
    return path


def test_every_canned_query_runs_against_the_schema(tmp_path):
    path = loaded(tmp_path)
    connection = database.connect_ro(path)
    try:
        for name, (purpose, sql) in query.QUERIES.items():
            rows = connection.execute(sql).fetchall()  # must not raise
            assert purpose, f"{name} has no stated purpose"
            assert isinstance(rows, list)
    finally:
        connection.close()


def test_summary_counts_what_was_loaded(tmp_path, capsys):
    assert query.main(["summary", "--db", str(loaded(tmp_path))]) == 0
    out = capsys.readouterr().out
    assert "signals" in out and "executions" in out


def test_json_output_is_parseable(tmp_path, capsys):
    assert query.main(["tickers", "--db", str(loaded(tmp_path)), "--json"]) == 0
    rows = json.loads(capsys.readouterr().out)
    assert {row["ticker"] for row in rows} == {"NVDA", "MSFT"}


def test_limit_trims_the_output(tmp_path, capsys):
    assert query.main(["tickers", "--db", str(loaded(tmp_path)), "--json", "--limit", "1"]) == 0
    assert len(json.loads(capsys.readouterr().out)) == 1


def test_explain_prints_the_sql_without_needing_a_database(tmp_path, capsys):
    """So a canned query can be copied and changed before there is any data."""
    assert query.main(["daily", "--db", str(tmp_path / "absent.db"), "--explain"]) == 0
    assert "FROM signals" in capsys.readouterr().out


def test_a_write_through_sql_is_refused(tmp_path, capsys):
    """The archive is the record of what was decided. Nothing here may edit it."""
    code = query.main(["--sql", "DELETE FROM signals", "--db", str(loaded(tmp_path))])
    assert code == 1
    assert "readonly" in capsys.readouterr().err


def test_a_missing_database_names_itself(tmp_path, capsys):
    code = query.main(["summary", "--db", str(tmp_path / "absent.db")])
    assert code == 1
    assert "absent.db" in capsys.readouterr().err


def test_a_broken_query_reports_the_error_rather_than_raising(tmp_path, capsys):
    code = query.main(["--sql", "SELECT nope FROM signals", "--db", str(loaded(tmp_path))])
    assert code == 1
    assert "SQL error" in capsys.readouterr().err


def test_a_canned_query_and_sql_together_is_a_usage_error(tmp_path, capsys):
    code = query.main(["summary", "--sql", "SELECT 1", "--db", str(loaded(tmp_path))])
    assert code == 2


def test_an_empty_result_says_so_rather_than_printing_nothing(tmp_path, capsys):
    path = tmp_path / "trading.db"
    database.connect_rw(path).close()
    assert query.main(["errors", "--db", str(path)]) == 0
    assert "(no rows)" in capsys.readouterr().out


def test_a_long_value_is_truncated_for_the_terminal(tmp_path, capsys):
    """A rationale is 2000 characters; a terminal is not."""
    path = tmp_path / "trading.db"
    connection = database.connect_rw(path)
    loader.load_signals(connection, [
        line({**JOURNAL_LINE, "error": "x" * 500, "signal": None})
    ])
    connection.close()

    assert query.main(["errors", "--db", str(path)]) == 0
    assert "..." in capsys.readouterr().out
