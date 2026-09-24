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

import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from pythonjsonlogger import jsonlogger

from app.schemas import LLMSignal
from orchestrator.fx import FxRate
from orchestrator.pricing import Usage
from config import settings as cfg
from orchestrator import arms, llm
from orchestrator.context import TickerContext

log = logging.getLogger(__name__)

_JOURNAL_LOGGER_NAME = "signal_journal"


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
) -> None:
    """Write one journal line. Swallows its own failures by design."""
    try:
        now = datetime.now(timezone.utc)
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
            },
        )
    except Exception:  # noqa: BLE001 - journalling must not break the cycle
        log.exception("failed to journal %s", context.ticker)
