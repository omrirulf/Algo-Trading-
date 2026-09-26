"""The journal as one file per month: the same record, byte for byte.

The owner's conditions for the split of 26 Sep 2026: joining the monthly
files must give exactly the old file (same hash); the race and the funds
must read exactly what they read before; calibration must not move. The
first is pinned here against the file as it was on main at 0768262; the
race and fund outputs are compared on real prices by
``.github/workflows/journal-split-check.yml``; the rest of this file pins
that every reader, handed the monthly directory, reads the same thing it
reads from one plain file holding the same bytes.
"""

from __future__ import annotations

import hashlib
import json
import logging
from datetime import date, datetime, timezone
from pathlib import Path

import pytest

from analysis import book, cycle_report, health
from analysis.reader import read_journal
from config import journal_files
from config import settings as cfg
from orchestrator.journal import MonthlyFileHandler
from orchestrator.journal import get_journal_logger as real_get_journal_logger
from store import database, loader, push_remote

ROOT = Path(__file__).resolve().parents[1]

#: logs/signal_journal.log on main at 0768262, the last commit before the
#: split: its size and its sha256. Every line in it was from September
#: 2026, so the split moved it whole to logs/journal/2026-09.log.
OLD_SIZE = 6_972_754
OLD_SHA256 = "26b6e7a2fd1d0a5dce350a556294d424e6c0049b91b8da698b04b7a6673a483d"


def line(ts: str, ticker: str, **extra) -> str:
    record = {"ts_utc": ts, "ticker": ticker, "event": "signal_generated",
              "signal": {"ticker": ticker, "bias": "BULLISH", "conviction": 0.6}, **extra}
    return json.dumps(record) + "\n"


def two_months(tmp_path: Path) -> tuple[Path, Path]:
    """The same lines as one file and as a monthly directory."""
    september = line("2026-09-29T14:41:00+00:00", "NVDA") + line("2026-09-30T14:41:00+00:00", "XOM")
    october = line("2026-10-01T14:41:00+00:00", "NVDA") + line("2026-10-02T14:41:00+00:00", "SPY")
    single = tmp_path / "signal_journal.log"
    single.write_text(september + october, encoding="utf-8")
    directory = tmp_path / "journal"
    directory.mkdir()
    (directory / "2026-09.log").write_text(september, encoding="utf-8")
    (directory / "2026-10.log").write_text(october, encoding="utf-8")
    return single, directory


# --------------------------------------------------------------------------- #
# The move of 26 Sep: the same bytes


def test_joining_the_months_gives_exactly_the_old_file():
    """The joined months begin with the old file, byte for byte.

    Only a prefix, because the journal only ever grows: every cycle after
    the split appends to the month's file, and what was there stays.
    """
    directory = ROOT / "logs" / "journal"
    if not journal_files.exists(directory):
        pytest.skip("no journal in this checkout")
    joined = journal_files.read_bytes(directory)
    assert len(joined) >= OLD_SIZE
    assert hashlib.sha256(joined[:OLD_SIZE]).hexdigest() == OLD_SHA256
    first = journal_files.parts(directory)[0]
    assert first.name == "2026-09.log"
    assert hashlib.sha256(first.read_bytes()[:OLD_SIZE]).hexdigest() == OLD_SHA256


def test_the_old_file_is_gone_and_nothing_else_is_in_the_directory():
    assert not (ROOT / "logs" / "signal_journal.log").exists()
    directory = ROOT / "logs" / "journal"
    if directory.exists():
        stray = [p.name for p in directory.iterdir() if not journal_files.MONTH_FILE.match(p.name)]
        assert stray == []


def test_the_settings_point_at_the_directory():
    # Read from the source: the suite's autouse fixture moves the live
    # setting to a temporary path so no test writes into logs/.
    source = (ROOT / "config" / "settings.py").read_text()
    assert 'SIGNAL_JOURNAL_PATH: Final[Path] = LOG_DIR / "journal"\n' in source
    assert cfg.LEGACY_SIGNAL_JOURNAL_PATH == cfg.LOG_DIR / "signal_journal.log"
    assert health.LEGACY_JOURNAL_FILE == cfg.LEGACY_SIGNAL_JOURNAL_PATH.name


def test_the_append_only_months_merge_as_a_union():
    attributes = (ROOT / ".gitattributes").read_text()
    assert "logs/journal/*.log merge=union" in attributes


# --------------------------------------------------------------------------- #
# Reading: the months joined are the single file


def test_the_months_are_read_in_order_and_nothing_else_is_read(tmp_path):
    single, directory = two_months(tmp_path)
    (directory / "notes.txt").write_text("not the journal\n")
    (directory / "2026-10.log.bak").write_text("an editor's copy\n")
    (directory / "2026-9.log").write_text("a wrong name\n")
    assert [p.name for p in journal_files.parts(directory)] == ["2026-09.log", "2026-10.log"]
    assert journal_files.read_text(directory) == single.read_text(encoding="utf-8")
    assert journal_files.read_bytes(directory) == single.read_bytes()
    assert list(journal_files.iter_lines(directory)) == list(single.open(encoding="utf-8"))


def test_a_plain_file_is_read_as_before(tmp_path):
    single, _ = two_months(tmp_path)
    assert journal_files.parts(single) == [single]
    assert journal_files.read_text(single) == single.read_text(encoding="utf-8")
    assert list(journal_files.iter_lines(single)) == list(single.open(encoding="utf-8"))


def test_a_month_cut_mid_line_joins_like_one_file_would(tmp_path):
    """A killed process leaves a line with no newline; the next write
    continues right after it. One file and the joined months agree."""
    directory = tmp_path / "journal"
    directory.mkdir()
    (directory / "2026-09.log").write_text('{"a": 1}\n{"trunc', encoding="utf-8")
    (directory / "2026-10.log").write_text('ated": 2}\n{"b": 3}', encoding="utf-8")
    single = tmp_path / "one.log"
    single.write_text('{"a": 1}\n{"truncated": 2}\n{"b": 3}', encoding="utf-8")
    assert list(journal_files.iter_lines(directory)) == list(single.open(encoding="utf-8"))
    assert journal_files.read_text(directory) == single.read_text(encoding="utf-8")


def test_what_counts_as_there(tmp_path):
    assert not journal_files.exists(tmp_path / "missing.log")
    assert not journal_files.exists(tmp_path / "missing")
    empty = tmp_path / "empty"
    empty.mkdir()
    assert not journal_files.exists(empty)
    assert journal_files.read_text(empty) == ""
    single, directory = two_months(tmp_path)
    assert journal_files.exists(single) and journal_files.exists(directory)
    assert journal_files.is_split(directory) and not journal_files.is_split(single)
    assert journal_files.is_split(tmp_path / "not_yet_made")


def test_the_month_is_the_utc_month():
    # 20:30 New York on 30 Sep is already 1 Oct in UTC.
    from zoneinfo import ZoneInfo

    evening = datetime(2026, 9, 30, 20, 30, tzinfo=ZoneInfo("America/New_York"))
    assert journal_files.month_file("logs/journal", evening) == Path("logs/journal/2026-10.log")
    assert journal_files.month_file("j", datetime(2027, 1, 4, 14, 40, tzinfo=timezone.utc)).name == "2027-01.log"


# --------------------------------------------------------------------------- #
# Every reader: the directory reads as the single file


def test_the_scorers_reader_reads_the_same_entries(tmp_path):
    single, directory = two_months(tmp_path)
    from_file, from_dir = read_journal(single), read_journal(directory)
    assert from_dir.entries == from_file.entries
    assert (from_dir.total_lines, from_dir.skipped) == (from_file.total_lines, from_file.skipped)
    with pytest.raises(FileNotFoundError):
        read_journal(tmp_path / "nowhere")


def test_the_book_the_health_check_and_the_cycle_report_read_the_same_lines(tmp_path):
    single, directory = two_months(tmp_path)
    assert book._lines(directory) == book._lines(single)
    assert health._read_lines(directory) == health._read_lines(single)
    assert [l.raw for l in cycle_report.read_lines(directory)] == [l.raw for l in cycle_report.read_lines(single)]


def test_the_index_and_the_archive_push_read_the_same_rows(tmp_path):
    single, directory = two_months(tmp_path)
    def rows(source):  # ``ingested_at`` is the clock at load time, not the line
        return [{k: v for k, v in row.items() if k != "ingested_at"}
                for row in push_remote.rows_from(source, loader.signal_row)]

    assert rows(directory) == rows(single) and len(rows(single)) == 4
    counts = []
    for source in (single, directory):
        db = tmp_path / f"{source.name}.db"
        connection = database.connect_rw(db)
        try:
            loader.load_file(connection, source, "signals")
            connection.commit()
            counts.append(connection.execute("SELECT raw FROM signals ORDER BY id").fetchall())
        finally:
            connection.close()
    assert counts[0] == counts[1] and len(counts[0]) == 4


def test_the_replay_tools_read_the_same_text(tmp_path):
    """They take ``exists`` and ``read_text`` from the one module."""
    for name in ("compare_screening", "compare_models", "determinism_check", "replay_journal", "news_ablation"):
        source = (ROOT / "replay" / f"{name}.py").read_text()
        assert "journal_files.exists(" in source and "journal_files.read_text(" in source, name
        assert ".read_text(encoding=\"utf-8\").splitlines()" not in source.replace(
            "journal_files.read_text(", ""), name


def test_nothing_opens_the_journal_path_but_the_one_module():
    """No reader may open ``SIGNAL_JOURNAL_PATH`` itself: a plain open of a
    directory fails, and a reader that found a way round it would read one
    month. The name of the old file appears only where it is meant to."""
    allowed = {"config/settings.py", "analysis/health.py", "config/journal_files.py"}
    hits = []
    for path in ROOT.rglob("*.py"):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(("tests/", ".claude/", ".venv/", "venv/")) or rel in allowed:
            continue
        text = path.read_text(encoding="utf-8")
        if "signal_journal.log" in text and "journal_files" not in text:
            hits.append(rel)
        if "SIGNAL_JOURNAL_PATH.open(" in text or "SIGNAL_JOURNAL_PATH.read_text(" in text:
            hits.append(rel)
    assert hits == []
    for workflow in (ROOT / ".github" / "workflows").glob("*.yml"):
        if workflow.name == "journal-split-check.yml":
            continue
        assert "logs/signal_journal.log" not in workflow.read_text(), workflow.name


# --------------------------------------------------------------------------- #
# Writing: each line into its month's file, and nothing else changes


def _record(message: str, when: datetime) -> logging.LogRecord:
    record = logging.LogRecord("signal_journal", logging.INFO, __file__, 1, message, None, None)
    record.created = when.timestamp()
    return record


def test_each_line_goes_to_its_months_file_and_the_months_join_to_one_file(tmp_path):
    directory = tmp_path / "journal"
    single = tmp_path / "single.log"
    monthly, plain = MonthlyFileHandler(directory), logging.FileHandler(single, encoding="utf-8")
    try:
        for when, text in [(datetime(2026, 9, 30, 14, 41, tzinfo=timezone.utc), "a"),
                           (datetime(2026, 9, 30, 23, 59, 59, tzinfo=timezone.utc), "b"),
                           (datetime(2026, 10, 1, 0, 0, 1, tzinfo=timezone.utc), "c"),
                           (datetime(2026, 11, 2, 14, 41, tzinfo=timezone.utc), "d")]:
            monthly.emit(_record(text, when))
            plain.emit(_record(text, when))
    finally:
        monthly.close()
        plain.close()
    assert [p.name for p in journal_files.parts(directory)] == ["2026-09.log", "2026-10.log", "2026-11.log"]
    assert (directory / "2026-09.log").read_text() == "a\nb\n"
    assert journal_files.read_bytes(directory) == single.read_bytes()


def test_a_new_line_is_appended_after_what_the_month_already_holds(tmp_path):
    directory = tmp_path / "journal"
    directory.mkdir()
    (directory / "2026-09.log").write_text("yesterday\n")
    handler = MonthlyFileHandler(directory)
    try:
        handler.emit(_record("today", datetime(2026, 9, 28, 14, 41, tzinfo=timezone.utc)))
    finally:
        handler.close()
    assert (directory / "2026-09.log").read_text() == "yesterday\ntoday\n"


@pytest.fixture
def clean_journal_logger():
    logger = logging.getLogger("signal_journal")
    saved = list(logger.handlers)
    for handler in saved:
        logger.removeHandler(handler)
    yield logger
    for handler in list(logger.handlers):
        handler.close()
        logger.removeHandler(handler)
    for handler in saved:
        logger.addHandler(handler)


def test_the_journal_logger_writes_the_directory_or_a_plain_file(tmp_path, clean_journal_logger):
    logger = real_get_journal_logger(tmp_path / "journal")
    (handler,) = logger.handlers
    assert isinstance(handler, MonthlyFileHandler)
    logger.info("signal_generated", extra={"ticker": "NVDA"})
    (part,) = journal_files.parts(tmp_path / "journal")
    assert part.name == journal_files.month_file(tmp_path / "journal").name
    written = json.loads(part.read_text())
    assert written["ticker"] == "NVDA" and written["event"] == "signal_generated"
    assert set(written) >= {"ts", "level", "event"}

    for h in list(logger.handlers):
        h.close()
        logger.removeHandler(h)
    logger = real_get_journal_logger(tmp_path / "plain.log")
    (handler,) = logger.handlers
    assert type(handler) is logging.FileHandler


# --------------------------------------------------------------------------- #
# The old file coming back is caught


def test_the_old_file_coming_back_is_a_critical_alarm(tmp_path):
    single, directory = two_months(tmp_path)
    alarm = health.legacy_journal(directory)
    assert alarm is not None and alarm.is_critical and "signal_journal.log" in alarm.detail
    single.unlink()
    assert health.legacy_journal(directory) is None
    assert health.legacy_journal(tmp_path / "a_plain_file.log") is None


def test_the_health_check_raises_it(tmp_path):
    single, directory = two_months(tmp_path)
    alarms = health.check(directory, tmp_path / "audit.log", date(2026, 10, 2), token_expires=None)
    assert any(a.title == "The old journal file is back" for a in alarms)
    single.unlink()
    alarms = health.check(directory, tmp_path / "audit.log", date(2026, 10, 2), token_expires=None)
    assert not any(a.title == "The old journal file is back" for a in alarms)
