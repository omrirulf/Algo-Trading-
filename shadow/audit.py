"""One fund's audit record: written by the real engine and manager, read back by the manager.

The position manager keeps no state of its own. Everything it knows about a
position -- the entry and initial stop that define R, which profit rungs are
already taken, the last stop it recorded -- it reads back from the audit
record the engine and it wrote. So a simulated fund needs a record of its
own, and it must be the SAME record for writing and reading, or the ladder
would take rung 1 every day.

A ``FundAudit`` is both ends of that: a ``logging.Logger`` the engine and the
manager write to (``audit_logger=``), formatting every line exactly as the
live log does, and an ``audit_path=`` object the manager reads back through
``lines_for(ticker)``. Nothing is written to disk.

What it keeps is exactly what ``app.position_manager._history`` can use, and
nothing it could not: a qualifying ``ACCEPTED`` entry line restarts that
ticker's list (``_history`` discards everything before one anyway), every
``position_managed`` line for the ticker is appended, and every other line is
dropped (a rejected or errored ``signal_processed`` line can never match, and
neither can a ``"*"`` line). The parser that reads it back is the production
one, unchanged; ``tests/test_shadow_audit.py`` checks the two readings agree
line for line against a whole-file record.
"""

from __future__ import annotations

import json
import logging
from contextlib import contextmanager
from typing import Iterable, Iterator, Optional

from pythonjsonlogger import jsonlogger

#: The event names the live log uses (app/logger.py, app/position_manager.py).
ENTRY_EVENT = "signal_processed"
MANAGED_EVENT = "position_managed"
LIVE_AUDIT_LOGGER = "execution_audit"


def _formatter() -> logging.Formatter:
    """The live audit log's own formatter (app/logger.py), field for field."""
    return jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(message)s",
        rename_fields={"asctime": "ts", "levelname": "level", "message": "event"},
    )


def _qualifying_entry(result: object) -> Optional[str]:
    """The ticker an ``ACCEPTED`` entry line restarts, as ``_history`` tests it."""
    if not isinstance(result, dict):
        return None
    if result.get("status") != "ACCEPTED":
        return None
    if not isinstance(result.get("entry_price"), (int, float)):
        return None
    if not isinstance(result.get("stop_price"), (int, float)):
        return None
    ticker = str(result.get("ticker") or "").strip().upper()
    return ticker or None


class _Router(logging.Handler):
    """Formats a line the way the live log would, and files it under its ticker."""

    def __init__(self, audit: "FundAudit") -> None:
        super().__init__(level=logging.INFO)
        self._audit = audit
        self.setFormatter(_formatter())

    def emit(self, record: logging.LogRecord) -> None:
        event = record.getMessage()
        if event == ENTRY_EVENT:
            ticker = _qualifying_entry(getattr(record, "result", None))
            if ticker is None:
                self._audit.dropped += 1
                return
            self._audit._restart(ticker, self.format(record))
        elif event == MANAGED_EVENT:
            action = getattr(record, "action", None) or {}
            ticker = str(action.get("ticker") or "").strip().upper()
            if not ticker or ticker == "*":
                self._audit.dropped += 1
                return
            self._audit._append(ticker, self.format(record))
            if self._audit.keep_actions:
                self._audit.actions.append(dict(action))
        else:
            self._audit.dropped += 1


class FundAudit:
    """The audit record of one simulated fund. See the module docstring."""

    def __init__(self, name: str, keep_actions: bool = False) -> None:
        self.name = name
        #: Every management action, in order, when asked for: the model and
        #: calibration funds keep them for their trade lists; a thousand
        #: coin-flip funds do not need to.
        self.keep_actions = keep_actions
        self.actions: list[dict] = []
        self.dropped = 0
        self._lines: dict[str, list[str]] = {}
        # A logger of its own that is not in logging's registry, so a
        # thousand funds leave nothing behind, and no handler of any other
        # logger -- the live one least of all -- ever sees a line.
        self.logger = logging.Logger(f"shadow.audit.{name}", level=logging.INFO)
        self.logger.propagate = False
        self.logger.addHandler(_Router(self))

    # -- what the manager reads -------------------------------------------

    def lines_for(self, symbol: str) -> list[str]:
        return list(self._lines.get(symbol.strip().upper(), ()))

    def read_text(self, encoding: Optional[str] = None) -> str:
        """The whole record, for a reader that does not ask by ticker."""
        return "\n".join(line for lines in self._lines.values() for line in lines)

    # -- seeding a fund that starts from a real book ------------------------

    def seed(self, raw_lines: Iterable[str]) -> int:
        """File lines from another record (the live log) as if written here.

        Used by calibration, whose fund starts holding the real account's
        positions: their entries, rungs and last stops are in the live log,
        and the manager must see them to manage those positions the way the
        live one does. Returns how many lines were kept.
        """
        kept = 0
        for raw in raw_lines:
            raw = raw.strip()
            if not raw:
                continue
            try:
                record = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if not isinstance(record, dict):
                continue
            event = record.get("event") or record.get("message")
            if event == ENTRY_EVENT:
                ticker = _qualifying_entry(record.get("result"))
                if ticker is not None:
                    self._restart(ticker, raw)
                    kept += 1
            elif event == MANAGED_EVENT:
                action = record.get("action") or {}
                ticker = str(action.get("ticker") or "").strip().upper()
                if ticker and ticker != "*":
                    self._append(ticker, raw)
                    kept += 1
        return kept

    def forget(self, tickers: Iterable[str]) -> None:
        """Drop the record of tickers the fund does not hold (seeding only)."""
        for ticker in tickers:
            self._lines.pop(ticker.strip().upper(), None)

    def _restart(self, ticker: str, line: str) -> None:
        self._lines[ticker] = [line]

    def _append(self, ticker: str, line: str) -> None:
        self._lines.setdefault(ticker, []).append(line)


class LiveAuditLeak(RuntimeError):
    """A simulated fund wrote to the live audit logger. Never acceptable."""


class _Tripwire(logging.Handler):
    def __init__(self) -> None:
        super().__init__(level=logging.DEBUG)
        self.hits: list[str] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.hits.append(record.getMessage())


@contextmanager
def live_audit_guarded() -> Iterator[None]:
    """Make the live audit log unreachable for the duration, and prove it.

    ``app.logger.get_audit_logger`` opens logs/execution_audit.log only when
    the ``execution_audit`` logger has no handler yet. A tripwire handler is
    attached first, so any code path that forgot its fund's logger lands in
    the tripwire instead of the live file -- and the run fails afterwards
    rather than having quietly reset a live position's ladder.

    The logger's own level is opened to DEBUG for the duration as well. A
    logger drops a record below its effective level before any handler sees
    it, and in ``python -m shadow.run`` the live logger is never configured
    (it inherits the root's ERROR): without this, a forgotten INFO line --
    every accepted entry and every rung -- would vanish silently instead of
    tripping the wire.
    """
    live = logging.getLogger(LIVE_AUDIT_LOGGER)
    saved_handlers, saved_propagate, saved_level = list(live.handlers), live.propagate, live.level
    tripwire = _Tripwire()
    for handler in saved_handlers:
        live.removeHandler(handler)
    live.addHandler(tripwire)
    live.propagate = False
    live.setLevel(logging.DEBUG)
    try:
        yield
    finally:
        live.removeHandler(tripwire)
        for handler in saved_handlers:
            live.addHandler(handler)
        live.propagate = saved_propagate
        live.setLevel(saved_level)
    if tripwire.hits:
        raise LiveAuditLeak(
            f"{len(tripwire.hits)} line(s) reached the live audit logger during a shadow run: "
            f"{sorted(set(tripwire.hits))}"
        )


__all__ = ["FundAudit", "LiveAuditLeak", "live_audit_guarded"]
