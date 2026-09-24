"""Structured JSON audit log. Every accept / reject / error is one JSON line."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

from pythonjsonlogger import jsonlogger

from app.schemas import ExecutionResult, LLMSignal
from config import settings as cfg

_AUDIT_LOGGER_NAME = "execution_audit"


def get_audit_logger(path: Path = cfg.AUDIT_LOG_PATH) -> logging.Logger:
    """Return the audit logger, creating the file handler on first use."""
    logger = logging.getLogger(_AUDIT_LOGGER_NAME)
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


def log_execution(
    signal: LLMSignal, result: ExecutionResult, logger: Optional[logging.Logger] = None,
) -> None:
    """Write one audit line containing the incoming signal and the decision.

    ``logger`` is for a caller that keeps its own record -- the shadow funds
    in ``shadow/``, each of which must have a book of its own and must never
    write into the live account's log. Left out, it is the live audit log.
    """
    logger = logger or get_audit_logger()
    level = logging.ERROR if result.status.value == "ERROR" else logging.INFO
    logger.log(
        level,
        "signal_processed",
        extra={
            "signal": signal.model_dump(mode="json"),
            "result": result.model_dump(mode="json"),
        },
    )
