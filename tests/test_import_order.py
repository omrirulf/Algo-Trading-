"""Every module must import cleanly when it is the first thing imported.

A circular import that only fails for one import order is invisible to a
test suite whose conftest happens to import the right module first -- which
is exactly how one shipped: orchestrator.pricing and config.watchlist gained
module-level imports of config.settings, which itself imports watchlist, and
``import orchestrator.llm`` in a fresh interpreter blew up on a partially
initialised pricing module. Each module below is imported alone, in its own
process, so order cannot mask it.
"""

from __future__ import annotations

import subprocess
import sys

import pytest

MODULES = [
    "app.main",
    "app.execution_engine",
    "app.risk_engine",
    "config.settings",
    "config.watchlist",
    "config.instruments",
    "orchestrator.pricing",
    "orchestrator.llm",
    "orchestrator.heartbeat",
    "orchestrator.context",
    "orchestrator.news",
    "orchestrator.fx",
    "orchestrator.journal",
    "replay.compare_configs",
    "replay.compare_models",
    "replay.signal_sanity",
    "replay.historical",
    "replay.runner",
    "backtest.compare_sleeves",
    "backtest.verify_tickers",
    "analysis.score_journal",
    "analysis.blend",
    "learn.fit_weights",
]


@pytest.mark.parametrize("module", MODULES)
def test_module_imports_first_in_a_fresh_interpreter(module):
    proc = subprocess.run(
        [sys.executable, "-c", f"import {module}"],
        capture_output=True, text=True, timeout=60,
        env={"PATH": "", "PYTHONPATH": "."},
    )
    assert proc.returncode == 0, f"{module}:\n{proc.stderr[-800:]}"
