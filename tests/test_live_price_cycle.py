"""A cycle that reads prices trades exactly as a cycle that does not.

The owner's rule for the ``live`` price (25 Sep 2026): record it on every
journal line, and change nothing about what is traded. So, driven through
``run_cycle`` with a real engine over a fake broker, both ways the cycle can
ask the model:

* every line of the cycle -- judged, NEUTRAL, failed, held, context failure --
  carries ``live`` and ``management``;
* a signal's price is read before the engine is asked about it, once;
* a cycle whose every price read fails or hangs journals every line and
  sends the engine exactly the signals, and the broker exactly the orders,
  of a cycle that reads no price at all;
* only ``main`` turns the reading on.
"""

from __future__ import annotations

import json
import time

import pytest

from app.broker_client import OpenPosition, StopOrder
from app.execution_engine import ExecutionEngine
from config.settings import Settings
from orchestrator import heartbeat as hb
from orchestrator import live_price as lp
from orchestrator.dispatch import DirectDispatcher
from orchestrator.llm import Completion, LLMError
from orchestrator.pricing import Usage
from tests.conftest import FakeBroker, FakeMarketData

WATCHLIST = ("NVDA", "XOM", "TLT", "EIS", "GLD")
ANSWERS = {"NVDA": "BULLISH", "XOM": "NEUTRAL"}      # TLT's call fails; EIS never gets a prompt; GLD is held


class Broker(FakeBroker):
    """The conftest broker, also writing each order into a shared event log."""

    events: list

    def submit_bracket_order(self, ticker, qty, side, stop_price):
        self.events.append(("order", ticker))
        return super().submit_bracket_order(ticker, qty, side, stop_price)


def _dispatcher(events: list) -> DirectDispatcher:
    broker = Broker(positions=[OpenPosition("GLD", 10, 2000.0, 190.0)],
                    stop_orders={"GLD": StopOrder("stop-gld", "GLD", 10, 180.0, "sell")})
    broker.events = events
    return DirectDispatcher(engine=ExecutionEngine(broker=broker, market_data=FakeMarketData()))


@pytest.fixture(params=[True, False], ids=["batched", "live"])
def cycle(request, monkeypatch):
    """The production cycle with the model, the news and one context faked."""
    monkeypatch.setattr(hb.cfg, "USE_BATCH_API", request.param)
    monkeypatch.setattr(hb.cfg, "SKIP_HELD_TICKERS", True)
    monkeypatch.setattr(hb, "get_settings", lambda: Settings(_env_file=None, watchlist=",".join(WATCHLIST)))
    monkeypatch.setattr(hb, "fetch_news", lambda t: ["news"])
    # No batch mode, as production's own full model has none: asked live.
    monkeypatch.setattr(hb, "full_model_provider", lambda: object())
    real_build_context = hb.build_context

    def build_context(ticker):
        if ticker == "EIS":
            raise RuntimeError("the context could not be gathered")
        return real_build_context(ticker)

    monkeypatch.setattr(hb, "build_context", build_context)

    def full(system_prompt, user_prompt, schema):
        ticker = user_prompt.split("\n", 1)[0].removeprefix("TICKER:").strip()
        if ticker not in ANSWERS:
            raise LLMError("timed out")
        text = json.dumps({"ticker": ticker, "bias": ANSWERS[ticker], "conviction": 0.8, "rationale": "r"})
        return Completion(text=text, usage=Usage(model=hb.MODEL, input_tokens=4000, output_tokens=500))

    monkeypatch.setattr(hb, "call_llm", full)
    return request.param


def _run(journal_path, prices):
    events: list = []
    dispatcher = _dispatcher(events)
    started = time.monotonic()
    report = hb.run_cycle(dispatcher, prices=prices)
    took = time.monotonic() - started
    lines = [json.loads(line) for line in journal_path.read_text().splitlines() if line.strip()]
    journal_path.write_text("")
    return report, lines, dispatcher._get_engine().broker, events, took


class Recording:
    """A reader that always answers, and writes each read into the event log."""

    def __init__(self, events):
        self.events, self.asked = events, []

    def read(self, ticker):
        self.asked.append(ticker)
        self.events.append(("price", ticker))
        return lp.answered(lp.Quote(price=101.0, bid=100.9, ask=101.1, quote_at="2026-09-16T14:50:00+00:00"),
                           "2026-09-16T14:50:01+00:00", "alpaca-iex")

    def close(self):
        pass


def _comparable(line: dict) -> dict:
    """A line with the parts that are allowed to differ between two runs taken out."""
    return {k: v for k, v in line.items() if k not in ("ts", "ts_utc", "live", "asctime", "created",
                                                         "msecs", "relativeCreated", "thread", "process")}


# --------------------------------------------------------------------------- #
# Every line, and the signal's price before the signal
# --------------------------------------------------------------------------- #


def test_every_line_of_the_cycle_carries_a_price_and_the_management_result(cycle, _journal_to_tmp):
    readers = []

    def prices(dispatcher):
        readers.append(Recording(dispatcher._get_engine().broker.events))
        return readers[-1]

    report, lines, broker, events, _ = _run(_journal_to_tmp, prices)

    assert sorted(line["ticker"] for line in lines) == sorted(WATCHLIST)
    by_ticker = {line["ticker"]: line for line in lines}
    assert by_ticker["GLD"]["held"] is True
    assert by_ticker["EIS"]["stage"] == hb.CONTEXT_FAILED
    assert by_ticker["TLT"]["error"] == "timed out"
    assert by_ticker["XOM"]["outcome"]["reason"] == "bias is NEUTRAL; no trade"
    assert by_ticker["NVDA"]["outcome"]["status"] == "ACCEPTED"
    for line in lines:
        assert line["live"]["price"] == 101.0 and line["live"]["source"] == "alpaca-iex", line["ticker"]
        assert line["management"] == {"market_closed": False}, line["ticker"]
    (reader,) = readers
    assert sorted(reader.asked) == sorted(WATCHLIST), "one read per line, no more"
    assert events.index(("price", "NVDA")) < events.index(("order", "NVDA")), \
        "the signal's price is read before the engine is asked, not after our own order"


def test_a_market_the_ladder_found_shut_is_on_every_line(cycle, _journal_to_tmp, monkeypatch):
    """The cheap gate said open, the ladder then found it shut: a cycle that
    straddled the close. Every line says so."""
    from app.position_manager import ManagementReport

    monkeypatch.setattr(DirectDispatcher, "manage_positions",
                        lambda self, protect_only=False: ManagementReport(market_closed=True).as_dict())
    _, lines, *_ = _run(_journal_to_tmp, None)
    assert lines and all(line["management"] == {"market_closed": True} for line in lines)
    assert all("live" not in line for line in lines), "no reader was asked for"


# --------------------------------------------------------------------------- #
# Failing or hanging reads change nothing
# --------------------------------------------------------------------------- #


class Hangs:
    def __init__(self, name):
        self.name = name

    def quote(self, ticker, timeout):
        time.sleep(0.5)
        return lp.Quote(price=1.0)


class Fails:
    def __init__(self, name):
        self.name = name

    def quote(self, ticker, timeout):
        raise RuntimeError(f"{self.name} is down")


@pytest.mark.parametrize("sources", [
    pytest.param(lambda: [Hangs("alpaca-iex"), Hangs("yfinance")], id="every-read-hangs"),
    pytest.param(lambda: [Fails("alpaca-iex"), Fails("yfinance")], id="every-read-fails"),
])
def test_a_cycle_whose_price_reads_all_fail_trades_exactly_as_one_that_reads_none(
        cycle, _journal_to_tmp, sources):
    budget = 0.15
    plain_report, plain, plain_broker, _, plain_took = _run(_journal_to_tmp, None)
    readers = []

    def prices(dispatcher):
        readers.append(lp.LivePrices(sources(), read_timeout=0.02, budget=budget))
        return readers[-1]

    report, priced, broker, _, took = _run(_journal_to_tmp, prices)

    # The same signals, the same orders, the same verdicts.
    assert broker.submitted == plain_broker.submitted and broker.submitted
    assert broker.protected == plain_broker.protected and broker.replaced == plain_broker.replaced
    assert report.results == plain_report.results
    # Every line still written, and identical but for the time and the price.
    assert [_comparable(line) for line in priced] == [_comparable(line) for line in plain]
    for line in priced:
        live = line["live"]
        assert live["price"] is None and live["error"], line["ticker"]
        assert set(live) == {"price", "bid", "ask", "quote_at", "asked_at", "source", "error"}
    assert all("live" not in line for line in plain)
    # And the waiting was bounded by the budget, not by the number of names.
    (reader,) = readers
    assert reader.spent <= budget + 0.05
    assert took - plain_took < 1.5


def test_a_reader_that_cannot_be_built_costs_the_prices_and_nothing_else(cycle, _journal_to_tmp):
    plain_report, plain, plain_broker, *_ = _run(_journal_to_tmp, None)

    def broken(dispatcher):
        raise RuntimeError("no reader today")

    report, lines, broker, *_ = _run(_journal_to_tmp, broken)
    assert broker.submitted == plain_broker.submitted
    assert report.results == plain_report.results
    assert [_comparable(line) for line in lines] == [_comparable(line) for line in plain]


def test_a_cycle_that_raises_leaves_nothing_on_the_next_lines(cycle, _journal_to_tmp, monkeypatch):
    closed = []

    class Closing(Recording):
        def close(self):
            closed.append(1)

    def dies(*a, **k):
        raise RuntimeError("the cycle died")

    # After the reader is built, in both paths: the first ticker's context.
    monkeypatch.setattr(hb, "prepare_ticker", dies)
    with pytest.raises(RuntimeError):
        hb.run_cycle(_dispatcher([]), prices=lambda d: Closing([]))
    assert closed == [1]
    from orchestrator import journal
    from orchestrator.context import TickerContext

    journal.record(TickerContext(ticker="NVDA"), error="after")
    (line,) = [json.loads(l) for l in _journal_to_tmp.read_text().splitlines() if l.strip()]
    assert "live" not in line and "management" not in line


# --------------------------------------------------------------------------- #
# Who turns it on
# --------------------------------------------------------------------------- #


def test_once_mode_reads_prices_for_the_dispatcher_it_trades_through(monkeypatch):
    seen = {}

    def fake_cycle(*args, **kwargs):
        seen.update(kwargs)
        return hb.CycleReport(tickers=("AAPL",), results=(hb.TickerResult("AAPL", hb.COMPLETED, "REJECTED"),))

    monkeypatch.setattr(hb, "run_cycle", fake_cycle)
    hb.main(["--once"])
    assert seen["prices"] is lp.for_dispatcher


def test_scheduler_mode_reads_prices_on_every_cycle(monkeypatch):
    calls, jobs = [], []

    class Scheduler:
        def add_job(self, func, *args, **kwargs):
            jobs.append(kwargs)

        def start(self):
            raise KeyboardInterrupt

    monkeypatch.setattr(hb, "BlockingScheduler", Scheduler)
    monkeypatch.setattr(hb, "run_cycle", lambda *a, **k: calls.append(k))
    hb.main([])
    # Every cycle also records its model calls (orchestrator/model_io.py).
    expected = {"prices": lp.for_dispatcher, "model_io_dir": hb.cfg.MODEL_IO_DIR}
    assert calls == [expected]
    assert jobs[0]["kwargs"] == expected


def test_a_cycle_started_anywhere_else_asks_nobody_for_a_price(cycle, _journal_to_tmp):
    _, lines, *_ = _run(_journal_to_tmp, None)
    assert lines and all("live" not in line for line in lines)
