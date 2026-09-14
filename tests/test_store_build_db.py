"""The build CLI: what it writes, what it refuses, and what it leaves alone."""

from __future__ import annotations

from store import build_db, database
from tests.test_store_loader import AUDIT_LINE, JOURNAL_LINE, line


def write_logs(tmp_path, journal_lines=1):
    journal = tmp_path / "signal_journal.log"
    audit = tmp_path / "execution_audit.log"
    journal.write_text(
        "".join(
            line({**JOURNAL_LINE, "ts_utc": f"2026-09-{15 + i:02d}T14:05:02+00:00"})
            for i in range(journal_lines)
        ),
        encoding="utf-8",
    )
    audit.write_text(line(AUDIT_LINE), encoding="utf-8")
    return journal, audit


def args(tmp_path, journal, audit, *extra):
    return [
        "--db", str(tmp_path / "trading.db"),
        "--journal", str(journal),
        "--audit", str(audit),
        *extra,
    ]


def test_a_build_loads_both_logs_and_reports_what_it_did(tmp_path, capsys):
    journal, audit = write_logs(tmp_path, journal_lines=3)
    assert build_db.main(args(tmp_path, journal, audit)) == 0

    out = capsys.readouterr().out
    assert "signals: 3 new" in out
    assert "executions: 1 new" in out
    assert "3 signals, 1 executions" in out


def test_running_it_again_adds_nothing(tmp_path, capsys):
    journal, audit = write_logs(tmp_path, journal_lines=3)
    build_db.main(args(tmp_path, journal, audit))
    capsys.readouterr()

    assert build_db.main(args(tmp_path, journal, audit)) == 0
    assert "signals: 0 new, 3 already loaded" in capsys.readouterr().out


def test_rebuild_starts_from_empty(tmp_path, capsys):
    """Cheap, because the logs are the record and this file is only an index."""
    journal, audit = write_logs(tmp_path, journal_lines=3)
    build_db.main(args(tmp_path, journal, audit))
    capsys.readouterr()

    assert build_db.main(args(tmp_path, journal, audit, "--rebuild")) == 0
    assert "signals: 3 new" in capsys.readouterr().out


def test_a_missing_audit_log_is_not_a_failure(tmp_path, capsys):
    """Nothing reached the engine yet. That is a state, not an error."""
    journal, audit = write_logs(tmp_path)
    audit.unlink()

    assert build_db.main(args(tmp_path, journal, audit)) == 0
    out = capsys.readouterr().out
    assert "signals: 1 new" in out
    assert "nothing to load from it" in out


def test_no_logs_at_all_says_what_to_run(tmp_path, capsys):
    journal, audit = write_logs(tmp_path)
    journal.unlink()
    audit.unlink()

    assert build_db.main(args(tmp_path, journal, audit)) == 1
    assert "run a cycle first" in capsys.readouterr().err


def test_quiet_prints_nothing(tmp_path, capsys):
    journal, audit = write_logs(tmp_path)
    assert build_db.main(args(tmp_path, journal, audit, "--quiet")) == 0
    assert capsys.readouterr().out == ""


def test_the_database_is_readable_afterwards(tmp_path):
    journal, audit = write_logs(tmp_path, journal_lines=2)
    build_db.main(args(tmp_path, journal, audit, "--quiet"))

    connection = database.connect_ro(tmp_path / "trading.db")
    try:
        assert connection.execute("SELECT COUNT(*) FROM signals").fetchone()[0] == 2
    finally:
        connection.close()
