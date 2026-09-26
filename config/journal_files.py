"""Where the signal journal lives, and how to read it as one stream.

Until 26 Sep 2026 the journal was one file, ``logs/signal_journal.log``.
It grows by about 0.64 MB a trading day, and GitHub refuses to take a push
that carries a file over 100 MB -- which one file would have reached in the
spring of 2027, before the experiment ends, and from that day no cycle's
journal could have been committed. So it is now a directory,
``logs/journal/``, holding one file per UTC month: ``2026-09.log``,
``2026-10.log``, ...

A storage change, not a change to the record. A line is written exactly as
before, only into the month's file; and every reader goes through
``iter_lines`` or ``read_text`` below, which join the months in order, so
what a reader sees is byte for byte the single file it used to open. The
split of the file that existed on 26 Sep was a move of that file, whole, to
``2026-09.log`` (every line in it was from September), and
``tests/test_journal_files.py`` pins that the joined months hash to the old
file.

Anything that is not a directory is read as one plain file, exactly as
before: the tests, the replay tools pointed at a copy, and the execution
audit, which goes through the same readers and was not split.

Pure paths and reading only, standard library only, so every package may
import it -- including those that may not write a file.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, Optional

#: The only files in the directory that are part of the journal. Anything
#: else there -- an editor's backup, a stray copy -- is not read.
MONTH_FILE = re.compile(r"^\d{4}-\d{2}\.log$")


def is_split(path: Path | str) -> bool:
    """True for the monthly directory, False for a plain file.

    A path that does not exist yet counts as the directory when it has no
    suffix (a fresh ``logs/journal``), so the writer can create it.
    """
    path = Path(path)
    return path.is_dir() or (not path.exists() and path.suffix == "")


def month_file(directory: Path | str, when: Optional[datetime] = None) -> Path:
    """The month's file in ``directory``, by the UTC month of ``when`` (now)."""
    when = when or datetime.now(timezone.utc)
    if when.tzinfo is not None:
        when = when.astimezone(timezone.utc)
    return Path(directory) / f"{when:%Y-%m}.log"


def parts(path: Path | str) -> list[Path]:
    """The files that make up the journal at ``path``, oldest month first.

    The names sort in time order (``YYYY-MM``), so a plain sort is the order
    the lines were written in.
    """
    path = Path(path)
    if path.is_dir():
        return sorted(p for p in path.iterdir() if p.is_file() and MONTH_FILE.match(p.name))
    return [path]


def exists(path: Path | str) -> bool:
    """Whether there is a journal to read: the file, or at least one month."""
    found = parts(path)
    return bool(found) and all(part.exists() for part in found)


def iter_lines(path: Path | str) -> Iterator[str]:
    """Every line of the journal, as iterating the old single file gave them.

    Lines keep their newline, as a file object's do. A month whose last line
    has no newline (a process killed mid-write) is joined to the next
    month's first line, which is exactly what appending to one file would
    have produced -- so the stream is the same in that case too.
    """
    carry = ""
    for part in parts(path):
        with part.open(encoding="utf-8") as handle:
            for line in handle:
                if carry:
                    line, carry = carry + line, ""
                if line.endswith("\n"):
                    yield line
                else:
                    carry = line
    if carry:
        yield carry


def read_text(path: Path | str) -> str:
    """The whole journal as one string, the months joined in order."""
    return "".join(part.read_text(encoding="utf-8") for part in parts(path))


def read_bytes(path: Path | str) -> bytes:
    """The whole journal as bytes, the months joined in order."""
    return b"".join(part.read_bytes() for part in parts(path))
