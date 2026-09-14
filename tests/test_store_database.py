"""Opening the database, and the read-only boundary that keeps the scorer honest.

``analysis/`` grades past decisions and a CI invariant holds it to reading
only. A plain ``sqlite3.connect`` creates the file it is pointed at, so the
distinction between the two connect helpers is a privilege boundary rather
than a convenience, and it is pinned here.
"""

from __future__ import annotations

import sqlite3

import pytest

from store import database, schema


def test_connect_rw_creates_the_schema_and_stamps_a_version(tmp_path):
    path = tmp_path / "trading.db"
    connection = database.connect_rw(path)

    assert path.exists()
    assert database.schema_version(connection) == schema.SCHEMA_VERSION
    tables = {
        row[0]
        for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type IN ('table', 'view')"
        )
    }
    assert {"signals", "executions", "meta", "decisions"} <= tables


def test_opening_an_existing_database_again_is_safe(tmp_path):
    """The DDL runs on every open, so it has to be idempotent."""
    path = tmp_path / "trading.db"
    first = database.connect_rw(path)
    first.execute(
        "INSERT INTO signals (line_hash, ingested_at, ticker, raw) VALUES (?, ?, ?, ?)",
        ("h", "now", "NVDA", "{}"),
    )
    first.commit()
    first.close()

    second = database.connect_rw(path)
    assert second.execute("SELECT COUNT(*) FROM signals").fetchone()[0] == 1


def test_connect_ro_refuses_to_create_a_missing_database(tmp_path):
    """A wrong path must be a loud error, not an empty file and a zero-row report."""
    path = tmp_path / "absent.db"
    with pytest.raises(FileNotFoundError) as excinfo:
        database.connect_ro(path)

    assert str(path) in str(excinfo.value)
    assert not path.exists()


def test_a_read_only_connection_cannot_write(tmp_path):
    path = tmp_path / "trading.db"
    database.connect_rw(path).close()

    connection = database.connect_ro(path)
    with pytest.raises(sqlite3.OperationalError):
        connection.execute("DELETE FROM signals")


def test_rows_come_back_addressable_by_column_name(tmp_path):
    """Queries here are read by hand; positional tuples would not survive an edit."""
    connection = database.connect_rw(tmp_path / "trading.db")
    connection.execute(
        "INSERT INTO signals (line_hash, ingested_at, ticker, raw) VALUES (?, ?, ?, ?)",
        ("h", "now", "NVDA", "{}"),
    )
    row = connection.execute("SELECT ticker FROM signals").fetchone()
    assert row["ticker"] == "NVDA"
