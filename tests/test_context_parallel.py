"""Fetching a ticker's sections at the same time, without changing the prompt.

A ticker cost about 32 seconds, almost all of it waiting in turn on six
different companies' servers. Overlapping that is the fix. The risk it
introduces is subtler than a crash: gaps are printed into the prompt, so a
list that reorders itself between runs changes the bytes the model reads
while every number stays the same -- and silently invalidates every replay
and sanity baseline measured against the old ordering.

These tests are almost all about that ordering, and about proving the overlap
is real rather than a pool that runs one job at a time.
"""

from __future__ import annotations

import sys
import time
import types

import pytest

from orchestrator import context, macro


# --------------------------------------------------------------------------- #
# the runner itself
# --------------------------------------------------------------------------- #

def test_gaps_come_back_in_declared_order_not_completion_order():
    """The job that finishes last still reports first if it was declared first."""
    def slow(gaps, label, delay):
        time.sleep(delay)
        gaps.append(label)
        return label

    jobs = [
        ("first", lambda g: slow(g, "first", 0.06)),
        ("second", lambda g: slow(g, "second", 0.0)),
        ("third", lambda g: slow(g, "third", 0.03)),
    ]
    results, buckets = context._in_parallel(jobs)
    assert results == {"first": "first", "second": "second", "third": "third"}
    assert [g for name, _ in jobs for g in buckets[name]] == ["first", "second", "third"]


def test_the_jobs_really_do_overlap():
    """Four 80ms waits finish in well under the 320ms they would take in turn."""
    jobs = [(str(i), lambda g, _i=i: time.sleep(0.08)) for i in range(4)]
    started = time.monotonic()
    context._in_parallel(jobs, workers=4)
    elapsed = time.monotonic() - started
    assert elapsed < 0.2, f"ran in {elapsed:.3f}s, which is not concurrent"


def test_one_job_cannot_see_another_job_s_gaps():
    """Separate lists are what makes the ordering possible at all."""
    def note(gaps, label):
        gaps.append(label)
        return len(gaps)

    _, buckets = context._in_parallel([
        ("a", lambda g: note(g, "a")),
        ("b", lambda g: note(g, "b")),
    ])
    assert buckets["a"] == ["a"] and buckets["b"] == ["b"]


def test_the_first_declared_failure_is_the_one_that_surfaces():
    """Not whichever failed soonest, which would depend on the weather."""
    def boom(_gaps, label, delay):
        time.sleep(delay)
        raise RuntimeError(label)

    with pytest.raises(RuntimeError, match="declared-first"):
        context._in_parallel([
            ("first", lambda g: boom(g, "declared-first", 0.05)),
            ("second", lambda g: boom(g, "failed-sooner", 0.0)),
        ])


# --------------------------------------------------------------------------- #
# a whole ticker, with every section failing on a different schedule
# --------------------------------------------------------------------------- #

class _ScrambledTicker:
    """Every payload raises, each after a different wait.

    The waits are deliberately in the opposite order to the order the gaps
    must be reported in, so a run that merged them as they arrived would come
    out backwards and the test would catch it.
    """

    DELAYS = {
        "info": 0.05, "calendar": 0.04, "recommendations": 0.035,
        "upgrades_downgrades": 0.03, "institutional_holders": 0.02,
        "insider_purchases": 0.01, "insider_transactions": 0.0,
    }

    def __init__(self, symbol):
        self.symbol = symbol

    def history(self, **_kwargs):
        return None

    def __getattr__(self, name):
        if name not in self.DELAYS:
            raise AttributeError(name)
        time.sleep(self.DELAYS[name])
        raise RuntimeError(f"{name} is down")


def _provider(monkeypatch, tmp_path, ticker_cls=_ScrambledTicker):
    monkeypatch.setitem(sys.modules, "yfinance", types.SimpleNamespace(Ticker=ticker_cls))
    return context.YFinanceContextProvider(fund_size_path=tmp_path / "fund_size.log")


def test_a_ticker_whose_every_section_fails_reports_them_in_the_stated_order(
    monkeypatch, tmp_path
):
    provider = _provider(monkeypatch, tmp_path)
    gaps = provider.fetch("MSFT").gaps

    labels = [
        "company fundamentals", "earnings calendar", "analyst recommendations",
        "upgrade/downgrade history", "institutional holders",
        "insider buy/sell summary", "insider transactions",
    ]
    seen = [next(i for i, g in enumerate(gaps) if g.startswith(label)) for label in labels]
    assert seen == sorted(seen), f"gaps arrived out of order: {gaps}"


def test_a_whole_ticker_waits_once_rather_than_section_by_section(monkeypatch, tmp_path):
    """The point of the change, measured on the real path.

    An earlier version of this file only timed the runner with an explicit
    worker count, so setting FETCH_WORKERS to 1 broke the entire optimisation
    and every test still passed. This times `fetch` itself, which is what the
    cycle actually calls.
    """
    total = sum(_ScrambledTicker.DELAYS.values())
    started = time.monotonic()
    _provider(monkeypatch, tmp_path).fetch("MSFT")
    elapsed = time.monotonic() - started
    assert elapsed < total * 0.75, (
        f"one ticker took {elapsed:.3f}s of a possible {total:.3f}s: the "
        "sections are still waiting in turn"
    )


def test_the_pool_is_actually_wide_enough_to_overlap():
    """A width of one is a sequential fetch wearing a thread pool."""
    assert context.FETCH_WORKERS > 1
    assert context.NESTED_FETCH_WORKERS > 1


def test_the_same_ticker_twice_produces_the_identical_gap_list(monkeypatch, tmp_path):
    """The property that matters: the prompt does not move between runs."""
    first = _provider(monkeypatch, tmp_path).fetch("MSFT").gaps
    for _ in range(5):
        assert _provider(monkeypatch, tmp_path).fetch("MSFT").gaps == first


def test_the_declared_gap_order_covers_every_section_that_can_record_one():
    """A section missing from GAP_ORDER would have its gaps silently dropped.

    The assembly reads `buckets.get(name)`, so a name that is fetched but not
    listed contributes nothing: the model would be told a section is present
    when the fetch for it failed, which is the one thing this project never
    does.
    """
    order = context.YFinanceContextProvider.GAP_ORDER
    assert len(set(order)) == len(order), "a name appears twice"
    for name in ("info", "fund_payloads", "positioning", "holding_analysts",
                 "macro", "commodity", "calendar", "recommendations", "upgrades",
                 "institutional", "insider_purchases", "insider_transactions"):
        assert name in order, f"{name} can record a gap but is not in GAP_ORDER"


# --------------------------------------------------------------------------- #
# the fan-outs inside a section
# --------------------------------------------------------------------------- #

class _MacroTicker:
    """The macro symbols answer in reverse, and two of them never answer."""

    DEAD = set(macro.SYMBOLS[1:3])

    def __init__(self, symbol):
        self.symbol = symbol
        self.info = {}

    def history(self, **_kwargs):
        time.sleep(0.04 * (len(macro.SYMBOLS) - macro.SYMBOLS.index(self.symbol))
                   if self.symbol in macro.SYMBOLS else 0.0)
        if self.symbol in self.DEAD:
            return None
        return types.SimpleNamespace(empty=False)

    def __getattr__(self, name):
        raise AttributeError(name)


def test_the_missing_macro_symbols_are_named_in_symbol_order(monkeypatch, tmp_path):
    """One line names them, so the order inside that line is prompt bytes."""
    provider = _provider(monkeypatch, tmp_path, _MacroTicker)
    gaps: list[str] = []
    provider._macro_histories("TLT", gaps)

    line = next(g for g in gaps if g.startswith("macro series for"))
    named = line.removeprefix("macro series for ").split(", ")
    assert named == [s for s in macro.SYMBOLS if s in _MacroTicker.DEAD]


def test_macro_histories_keep_the_symbols_that_answered(monkeypatch, tmp_path):
    provider = _provider(monkeypatch, tmp_path, _MacroTicker)
    histories = provider._macro_histories("TLT", [])
    assert list(histories) == [s for s in macro.SYMBOLS if s not in _MacroTicker.DEAD]


def test_holdings_stay_in_the_fund_s_own_weight_order(monkeypatch, tmp_path):
    """The heaviest holding is rendered first however slowly it answered."""
    provider = _provider(monkeypatch, tmp_path)
    pairs = [("AAA", 0.09), ("BBB", 0.07), ("CCC", 0.05), ("DDD", 0.02)]
    delays = {"AAA": 0.05, "BBB": 0.0, "CCC": 0.03, "DDD": 0.01}

    monkeypatch.setattr(context, "holdings",
                        types.SimpleNamespace(holdings_from_payload=lambda _p: pairs))
    monkeypatch.setattr(context.funds, "fund_shape", lambda _t: context.funds.EQUITY_FUND)

    def one(symbol):
        time.sleep(delays[symbol])
        return None if symbol in ("BBB", "DDD") else f"snap-{symbol}"

    monkeypatch.setattr(provider, "_analyst_for", one)
    gaps: list[str] = []
    out = provider._holding_analysts("XLE", {"top_holdings": object()}, gaps)

    assert [symbol for symbol, _w, _s in out] == ["AAA", "BBB", "CCC", "DDD"]
    assert [weight for _s, weight, _x in out] == [0.09, 0.07, 0.05, 0.02]
    assert "BBB, DDD" in gaps[0], gaps
