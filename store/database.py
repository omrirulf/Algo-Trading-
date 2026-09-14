"""Opening the database, in the two modes that exist here.

The split is a privilege boundary, not a convenience. ``analysis/`` grades past
decisions and a CI invariant holds it to being read-only -- it may not place an
order and it may not write a file. A plain ``sqlite3.connect(path)`` *creates*
the file when it is missing, which would quietly make the scorer a writer and
leave an empty database behind as the evidence.

So a reader opens ``file:...?mode=ro``, which cannot create and cannot write.
A caller that has nothing to load gets an error naming the missing database
instead of an empty one it will go on to report zero rows from.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Final

from store import schema

#: Default location comes from config.settings, which is the single source of
#: truth for every path in this project.
from config.settings import DATABASE_PATH

_SCHEMA_VERSION_KEY: Final[str] = "schema_version"


def connect_rw(path: Path | str = DATABASE_PATH) -> sqlite3.Connection:
    """Open for writing, creating and migrating the file if needed."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    # Appending from a scheduled job while a report reads the same file is the
    # normal case here, and the default rollback journal makes those two block
    # each other. WAL lets the reader carry on against the last committed state.
    connection.execute("PRAGMA journal_mode=WAL;")
    connection.execute("PRAGMA foreign_keys=ON;")
    _ensure_schema(connection)
    return connection


def connect_ro(path: Path | str = DATABASE_PATH) -> sqlite3.Connection:
    """Open read-only. Raises if the database does not exist.

    Used by every consumer that only asks questions. It physically cannot
    create the file, so a typo in a path is a loud error rather than a silent
    empty result.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"no database at {path}. Build one with: python store/build_db.py"
        )
    connection = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    return connection


def _ensure_schema(connection: sqlite3.Connection) -> None:
    """Apply the DDL and stamp the version. Safe to run on every open."""
    with connection:
        for statement in schema.ALL_DDL:
            connection.execute(statement)
        connection.execute(
            "INSERT INTO meta (key, value) VALUES (?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
            (_SCHEMA_VERSION_KEY, str(schema.SCHEMA_VERSION)),
        )


def schema_version(connection: sqlite3.Connection) -> int | None:
    """The version stamped in the file, or None for a pre-``meta`` database."""
    try:
        row = connection.execute(
            "SELECT value FROM meta WHERE key = ?", (_SCHEMA_VERSION_KEY,)
        ).fetchone()
    except sqlite3.DatabaseError:
        return None
    if row is None:
        return None
    try:
        return int(row[0])
    except (TypeError, ValueError):
        return None


__all__ = [
    "DATABASE_PATH",
    "connect_ro",
    "connect_rw",
    "schema_version",
]
