"""A ticker that never got a prompt is still part of the cycle's record.

The cycle knows every ticker's outcome -- it holds a ``TickerResult`` for all
eighty -- but only the journal survives the run, and `analysis/cycle_report.py`
is rebuilt from that. So a ticker whose context could not be gathered left no
trace: on 17 Sep four names (MSFT, XLK, XLI, VNQ) died on the news fetch, each
logged as an ERROR by the run, and the report's header still read
"76 names checked · 1 traded · 0 with a problem". VNQ did not appear in the
file at all.

The renderer was never wrong. It counts a problem as a line carrying an
``error``, and there were none to count. The record was incomplete, so
everything built on it was too -- the same shape as the CFTC mappings and the
sourceless scores.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from analysis import cycle_report
from orchestrator import heartbeat
from orchestrator.news import NewsFetchError


class Recorder:
    """Captures what would have been journalled."""

    def __init__(self):
        self.calls = []

    def record(self, context, **kwargs):
        self.calls.append((context, kwargs))


def test_a_context_failure_is_journalled_with_its_error(monkeypatch):
    spy = Recorder()
    monkeypatch.setattr(heartbeat.journal, "record", spy.record)

    heartbeat.journal_context_failure("VNQ", RuntimeError("Bright Data unreachable"))

    (context, kwargs) = spy.calls[0]
    assert context.ticker == "VNQ"
    assert "Bright Data unreachable" in kwargs["error"]
    assert "signal" not in kwargs, "a failed ticker has no signal to record"


def test_the_gathered_context_is_kept_when_only_rendering_failed(monkeypatch):
    """Two different failures. One has a context worth keeping; one does not."""
    from orchestrator.context import TickerContext

    spy = Recorder()
    monkeypatch.setattr(heartbeat.journal, "record", spy.record)
    gathered = TickerContext(ticker="XLI", headlines=["something happened"])

    heartbeat.journal_context_failure("XLI", ValueError("bad float"), gathered)

    context, _ = spy.calls[0]
    assert context is gathered
    assert context.headlines == ["something happened"]


def test_an_exception_with_no_message_still_produces_a_readable_error(monkeypatch):
    spy = Recorder()
    monkeypatch.setattr(heartbeat.journal, "record", spy.record)

    heartbeat.journal_context_failure("MSFT", KeyError())

    assert spy.calls[0][1]["error"], "an empty message must not journal an empty error"


def test_a_journal_that_cannot_be_written_does_not_take_the_cycle_down(monkeypatch):
    def explode(*args, **kwargs):
        raise OSError("disk full")

    monkeypatch.setattr(heartbeat.journal, "record", explode)
    heartbeat.journal_context_failure("XLK", RuntimeError("boom"))  # must not raise


# --- and what the report then says ------------------------------------------

def _line(ticker: str, *, error: str | None = None, bias: str | None = None) -> dict:
    """One journal line as `cycle_report` reads them: the raw dict."""
    return {
        "ts_utc": "2026-09-17T15:50:00+00:00",
        "ticker": ticker,
        "context": {"gaps": [], "technicals": {"atr_pct_of_price": 0.02}},
        "signal": (
            {"ticker": ticker, "bias": bias, "conviction": 0.5, "rationale": "r"}
            if bias else None
        ),
        "error": error,
        "usage": {"model": "claude-opus-5", "input_tokens": 1, "output_tokens": 1},
    }


def test_the_report_header_counts_a_failure_as_a_problem():
    text = cycle_report.render([
        cycle_report.Line(_line("GOOGL", bias="BULLISH")),
        cycle_report.Line(_line("NVDA", bias="NEUTRAL")),
        cycle_report.Line(_line("VNQ", error="Bright Data unreachable: timed out")),
    ])

    assert "3 names checked" in text
    assert "1 with a problem" in text


def test_the_failed_ticker_is_named_in_the_report():
    text = cycle_report.render([
        cycle_report.Line(_line("GOOGL", bias="BULLISH")),
        cycle_report.Line(_line("VNQ", error="Bright Data unreachable: timed out")),
    ])

    assert "VNQ" in text, "a ticker the cycle attempted must appear in its report"


def test_the_group_table_puts_the_failure_in_its_own_sleeve():
    """VNQ is a fund. A problem must be counted where the reader looks for it."""
    text = cycle_report.render([
        cycle_report.Line(_line("GOOGL", bias="BULLISH")),
        cycle_report.Line(_line("VNQ", error="Bright Data unreachable: timed out")),
    ])
    lines = text.splitlines()
    start = next(i for i, r in enumerate(lines) if r.startswith("| Group |"))
    body = []
    for row in lines[start + 2:]:
        if not row.startswith("| "):
            break
        body.append(row)
    assert body, "the group table has no rows"
    problems = sum(int(row.rsplit("|", 2)[1].strip()) for row in body)
    assert problems == 1, f"expected one problem across the table, got {body}"


# --- the wiring, which is the part that was actually missing ---------------

@pytest.mark.parametrize("boom", [
    pytest.param(lambda t: (_ for _ in ()).throw(NewsFetchError("Bright Data unreachable")),
                 id="news-fetch-failed"),
    pytest.param(lambda t: (_ for _ in ()).throw(RuntimeError("yfinance exploded")),
                 id="context-gather-failed"),
])
def test_process_ticker_journals_the_failure_it_returns(monkeypatch, boom):
    """The helper existing is not the fix; being called is.

    The first version of these tests exercised ``journal_context_failure``
    directly and passed with every call site deleted -- the same hole that
    let the screen path miss the source rule, and that let four names vanish
    from the 17 Sep report. So this drives ``process_ticker`` itself.
    """
    spy = Recorder()
    monkeypatch.setattr(heartbeat.journal, "record", spy.record)
    monkeypatch.setattr(heartbeat, "build_context", boom)

    result = heartbeat.process_ticker("VNQ")

    assert result.stage == heartbeat.CONTEXT_FAILED
    assert spy.calls, "a ticker that failed at the context stage left no record"
    context, kwargs = spy.calls[0]
    assert context.ticker == "VNQ"
    assert kwargs["error"]


def test_every_context_failure_return_journals_first():
    """Structural, so the call site added next year fails here.

    Each ``return TickerResult(ticker, CONTEXT_FAILED...)`` must be preceded
    by a ``journal_context_failure`` call in the same branch.
    """
    import ast

    # Scanned over the whole module rather than one named function: these
    # returns moved from process_ticker to prepare_ticker when the cycle
    # learned to batch, and a test that follows the invariant instead of the
    # function name does not have to move with them again.
    tree = ast.parse(Path(heartbeat.__file__).read_text())
    func = tree

    def is_context_failed_return(node: ast.AST) -> bool:
        return (
            isinstance(node, ast.Return)
            and isinstance(node.value, ast.Call)
            and any(
                isinstance(a, ast.Name) and a.id == "CONTEXT_FAILED"
                for a in node.value.args
            )
        )

    def journals(stmts: list[ast.stmt]) -> bool:
        return any(
            isinstance(s, ast.Expr) and isinstance(s.value, ast.Call)
            and isinstance(s.value.func, ast.Name)
            and s.value.func.id == "journal_context_failure"
            for s in stmts
        )

    blocks = [
        node for node in ast.walk(func)
        if isinstance(node, (ast.ExceptHandler, ast.If))
        and any(is_context_failed_return(s) for s in getattr(node, "body", []))
    ]
    assert len(blocks) >= 3, f"expected the three known failure branches, found {len(blocks)}"
    unrecorded = [
        b.body[-1].lineno for b in blocks if not journals(b.body)
    ]
    assert not unrecorded, (
        "a CONTEXT_FAILED return with no journal line at heartbeat.py:"
        + ", ".join(str(n) for n in unrecorded)
    )
