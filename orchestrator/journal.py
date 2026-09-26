"""Per-cycle record of what the analyst saw and what it concluded.

The execution audit log (``app/logger.py``) answers "what did the engine do
with this signal". This answers the question you actually need in order to
tell whether the signals are any good: *what was in front of the model when it
said that*, and did the confident calls turn out better than the timid ones.

One JSON object per ticker per cycle, written from the orchestrator side.
Journalling is best-effort -- a failure to write a line must never take down
the cycle that produced it.
"""

from __future__ import annotations

import json
import logging
import os
import re
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterator, Optional

from pythonjsonlogger import jsonlogger

from app.schemas import LLMSignal
from orchestrator.fx import FxRate
from orchestrator.pricing import Usage
from config import settings as cfg
from orchestrator import arms, llm
from orchestrator.context import TickerContext

log = logging.getLogger(__name__)

_JOURNAL_LOGGER_NAME = "signal_journal"


def run_block() -> Optional[dict[str, Any]]:
    """What started this cycle run, as the workflow described it; else None.

    The heartbeat workflow sets HEARTBEAT_RUN on the cycle step to a small
    JSON object -- the trigger (schedule, scheduler, backup or manual), the
    source (which starter asked for the run: supabase-cron, claude-bridge,
    watchdog, github-schedule...), when the day's run was scheduled and when
    this one started, how late that was, and the GitHub run id (built by
    ``analysis/cycle_day.py``). It rides on every line
    so the journal alone can answer "which runs were late, and who started
    them", which GitHub's own run list forgets after a few months.

    Read at write time, not import time, and never trusted: unset, empty, not
    JSON, or JSON that is not an object all mean "no block", silently. A
    journal line must never be lost over a label about it.

    The one environment read in this module. The CI guardrail that keeps
    orchestrator modules away from credentials allows exactly this line: the
    value describes the run and is not a secret.
    """
    raw = os.environ.get("HEARTBEAT_RUN")
    if not raw:
        return None
    try:
        parsed = json.loads(raw)
    except Exception:  # noqa: BLE001 - not JSON (or absurdly nested): no block
        return None
    if not isinstance(parsed, dict):
        return None
    # ``source`` is which starter asked for the run (the Supabase starter, a
    # Claude Routine, the watchdog...), typed by whatever dispatched it. The
    # workflow already validates it (analysis/cycle_day.py:source_for); this
    # is the same rule again at the last door before a public, committed
    # file, so a block built some other way cannot put free text on every
    # line. Only this key is judged: the rest is the workflow's own numbers.
    if "source" in parsed and not (isinstance(parsed["source"], str)
                                   and _SAFE_SOURCE.fullmatch(parsed["source"])):
        parsed["source"] = "unknown"
    return parsed


#: A run block's ``source``: a short safe token, as
#: ``analysis/cycle_day.py:SOURCE_PATTERN`` defines it. Repeated rather than
#: imported: the journal must not depend on the analysis package.
_SAFE_SOURCE = re.compile(r"[a-z0-9-]{1,40}")


def _run_field() -> dict[str, Any]:
    """``{"run": block}`` when the workflow described the run, else nothing at all."""
    block = run_block()
    return {} if block is None else {"run": block}


# --------------------------------------------------------------------------- #
# What a cycle knows about itself, on every line it writes
# --------------------------------------------------------------------------- #


@dataclass
class _Cycle:
    """The facts one open cycle adds to each of its lines.

    Held here rather than passed down, because lines are written from a dozen
    places deep inside the cycle -- held, screened, failed, judged -- and a
    fact that every call site had to remember is a fact one of them would
    forget. Nothing that decides a trade reads any of it.
    """

    #: Builds the price reader, given the dispatcher the cycle trades through.
    prices_for: Optional[Callable[[Any], Any]] = None
    #: Has ``read(ticker) -> dict`` and ``close()``; see orchestrator/live_price.py.
    reader: Any = None
    #: ``{"market_closed": bool}`` once the position-management pass returned.
    management: Optional[dict[str, bool]] = None


#: The open cycle, or None. Only ``cycle()`` opens one, so a line written by
#: a test, a replay or a notebook is exactly the line it was before.
_open: Optional[_Cycle] = None


@contextmanager
def cycle(prices_for: Optional[Callable[[Any], Any]] = None) -> Iterator[None]:
    """Mark the lines written inside as one cycle's.

    ``prices_for`` builds the reader that prices each line (``None`` reads no
    price, and the lines carry none). Closed in ``finally`` so a cycle that
    raised cannot leave its facts on the next cycle's lines -- in scheduler
    mode one process runs many.
    """
    global _open
    _open = _Cycle(prices_for=prices_for)
    try:
        yield
    finally:
        closing, _open = _open, None
        close = getattr(closing.reader, "close", None) if closing else None
        if close is not None:
            try:
                close()
            except Exception:  # noqa: BLE001 - a connection left open is not worth a crash
                log.exception("could not close the live price reader")


def note_cycle(positions: Any, dispatcher: Any = None) -> None:
    """Record what the cycle learned before its first line. Never raises.

    Called by the heartbeat once the position-management pass has returned,
    which in both cycles is before any line is written. Two things come of it:

    * ``management`` -- whether that pass found the market closed, exactly as
      the pass reported it. It is left off when the pass reported nothing
      (no manager behind this dispatcher, or it failed outright): unknown is
      not the same as open.
    * the price reader, built for the dispatcher this cycle trades through.

    Outside ``cycle()`` it does nothing.
    """
    facts = _open
    if facts is None:
        return
    closed = positions.get("market_closed") if isinstance(positions, dict) else None
    facts.management = {"market_closed": closed} if isinstance(closed, bool) else None
    if facts.prices_for is not None and facts.reader is None:
        try:
            facts.reader = facts.prices_for(dispatcher)
        except Exception:  # noqa: BLE001 - lines without a price, never a cycle without lines
            log.exception("could not build the live price reader; lines will carry no price")


def read_live(ticker: str) -> Optional[dict[str, Any]]:
    """``ticker``'s price now, as a line's ``live`` record; None with no reader.

    The heartbeat calls this at the moment a signal is made, just before it is
    dispatched; ``record`` calls it for every other line when it is written.
    Never raises: a reader that breaks its own promise costs the line its
    price, not the line.
    """
    reader = _open.reader if _open is not None else None
    if reader is None:
        return None
    try:
        live = reader.read(ticker)
    except Exception:  # noqa: BLE001 - see the docstring
        log.exception("the live price reader failed for %s", ticker)
        return None
    return live if isinstance(live, dict) else None


def _cycle_fields(live: Optional[dict[str, Any]]) -> dict[str, Any]:
    """``live`` and ``management``, each only when there is one to write."""
    fields: dict[str, Any] = {}
    if live is not None:
        fields["live"] = live
    facts = _open
    if facts is not None and facts.management is not None:
        fields["management"] = dict(facts.management)
    return fields


def get_journal_logger(path: Path = cfg.SIGNAL_JOURNAL_PATH) -> logging.Logger:
    """Return the journal logger, creating the file handler on first use."""
    logger = logging.getLogger(_JOURNAL_LOGGER_NAME)
    if logger.handlers:
        return logger

    path.parent.mkdir(parents=True, exist_ok=True)
    handler = logging.FileHandler(path, encoding="utf-8")
    handler.setFormatter(
        jsonlogger.JsonFormatter(
            "%(asctime)s %(levelname)s %(message)s",
            rename_fields={"asctime": "ts", "levelname": "level", "message": "event"},
        )
    )
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    return logger


def record(
    context: TickerContext,
    signal: Optional[LLMSignal] = None,
    outcome: Optional[dict[str, Any]] = None,
    error: Optional[str] = None,
    usage: Optional[Usage] = None,
    fx: Optional[FxRate] = None,
    screen: Optional[dict[str, Any]] = None,
    blend: Optional[dict[str, Any]] = None,
    held: bool = False,
    stage: Optional[str] = None,
    live: Optional[dict[str, Any]] = None,
) -> None:
    """Write one journal line. Swallows its own failures by design.

    ``stage`` names where a failed line failed, when that was before the
    model was asked (``"context"``): a news-vendor outage is not a failed
    model call, and the owner's model-watch trigger counts only those.

    ``live`` is the price read when the line's signal was made, for the one
    caller that reads it before dispatching (``heartbeat.judge_answer``).
    Every other line inside a cycle is priced here, as it is written.
    """
    try:
        now = datetime.now(timezone.utc)
        # After ``now``, so the line's own time -- which decides the day it
        # belongs to in the race and the funds -- is what it always was.
        if live is None:
            live = read_live(context.ticker)
        get_journal_logger().info(
            "signal_generated",
            extra={
                # The formatter's own ``ts`` is local time with no offset, which
                # is not enough to tell whether a signal fired before or after
                # the session close -- and that decides which bar a scorer may
                # honestly use as the entry price.
                "ts_utc": now.isoformat(),
                "ticker": context.ticker,
                "context": context.as_dict(),
                "signal": signal.model_dump(mode="json") if signal else None,
                "outcome": outcome,
                "error": error,
                # Measured token counts, so "what does a cycle cost" is
                # answerable from the archive rather than re-estimated.
                "usage": usage.as_dict() if usage else None,
                # USD/ILS at the time of the signal. Recorded because an FX
                # move does not reduce a dollar return, it redenominates it --
                # so without the rate as of the entry, no later analysis can
                # say what a trade was worth in the currency that matters.
                "fx": fx.as_dict() if fx else None,
                # The cheap first-stage answer, when the funnel ran. Kept
                # beside the final signal so what the screen filtered, and
                # how often the full model disagreed with it on the tickers
                # it escalated, are numbers the journal answers rather than
                # assumptions the funnel rests on.
                "screen": screen,
                # The learned blend of the five scores, computed in shadow
                # beside the model's answer. Recorded so the composite can be
                # scored against realised returns exactly as conviction is;
                # nothing in the cycle reads it back.
                "blend": blend,
                # What the rule arms in rules/ would have said, from the same
                # technicals the model saw. Computed here rather than passed
                # in, so it is on every line -- screened, held, failed -- and
                # no call site can leave it off. The race in
                # analysis/horse_race.py is only fair if the rule got to
                # answer on every ticker the model did, not just the ones the
                # model chose to. Nothing in the cycle reads it back.
                "arms": arms.arms_record(context, now.date(), signal),
                # True when the ticker was already in the book and no model
                # was asked. The context above was still gathered, so these
                # lines are what a later replay would need to price what
                # skipping held names cost -- and they are the reason a line
                # with no signal is not automatically a failure.
                "held": held,
                # How the line was made, as configured when it was written:
                # whether the cheap screen stood in front of the full model,
                # and the reasoning level the full model was asked at. On
                # every line -- held and failed ones included -- because the
                # race has to be able to say, from the journal alone, that
                # no line in its window was made under a different setting
                # from the one the pre-registration names.
                "screening": bool(llm.SCREENING_ENABLED),
                "reasoning_effort": llm.configured_effort(),
                "stage": stage,
                # The price of the name when this line's signal was made, and
                # whether the cycle's position-management pass found the
                # market shut (the owner's request of 25 Sep 2026). For later
                # study only: the race and the funds still enter at the next
                # open, and nothing in the cycle reads either back. Absent
                # rather than null outside a cycle, so a line written without
                # them keeps exactly the keys, in exactly the order, it had.
                **_cycle_fields(live),
                # What started this run and how late it was (see run_block).
                # Last, and absent rather than null when unset, so a line
                # written without it keeps exactly the keys, in exactly the
                # order, it had before the block existed.
                **_run_field(),
            },
        )
    except Exception:  # noqa: BLE001 - journalling must not break the cycle
        log.exception("failed to journal %s", context.ticker)
