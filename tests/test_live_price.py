"""The price reader: one price per journal line, read at the moment, never in the way.

What has to hold, whatever the sources do: a read returns the line's ``live``
record and never raises; a source that hangs is cut off at its deadline; a
source that keeps failing is not asked again this cycle; the cycle's reading
has a ceiling; the key goes into two request headers and nowhere else; and
the only thing the reader ever does is GET a price from the data host.

No network here: Alpaca is an ``httpx.MockTransport`` and yfinance a function.
"""

from __future__ import annotations

import json
import logging
import re
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import httpx
import pandas as pd
import pytest

from app.broker_client import AlpacaCredentials, BrokerError
from orchestrator import live_price as lp
from orchestrator.dispatch import DirectDispatcher, WebhookDispatcher

ROOT = Path(__file__).resolve().parents[1]
KEY, SECRET = "PKTESTKEY0123456789", "sEcReT-value-that-must-never-leak"
ASKED = datetime(2026, 9, 28, 14, 52, 7, 902214, tzinfo=timezone.utc)

SNAPSHOT = {
    "NVDA": {
        "latestTrade": {"t": "2026-09-28T14:52:07.311123456Z", "p": 187.42, "s": 100, "x": "V"},
        "latestQuote": {"t": "2026-09-28T14:52:07.5Z", "bp": 187.40, "ap": 187.45, "bs": 1, "as": 2},
        "minuteBar": {"o": 187.0, "c": 187.4},
    }
}


def keys() -> AlpacaCredentials:
    return AlpacaCredentials(api_key=KEY, secret_key=SECRET, source="settings")


class Alpaca:
    """Alpaca's data host, as a transport: records every request it is sent."""

    def __init__(self, respond=None):
        self.requests: list[httpx.Request] = []
        self._respond = respond or (lambda request: httpx.Response(200, json=SNAPSHOT))

    def handler(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        return self._respond(request)

    def source(self, credentials=keys) -> lp.AlpacaIex:
        transport = httpx.MockTransport(self.handler)
        return lp.AlpacaIex(credentials, lambda **kw: httpx.Client(transport=transport, **kw))


def minutes(*bars, tz="America/New_York"):
    """A yfinance-shaped frame of one-minute closes: (time, close) pairs."""
    index = pd.DatetimeIndex([pd.Timestamp(t, tz=tz) for t, _ in bars])
    return pd.DataFrame({"Close": [c for _, c in bars]}, index=index)


class Yahoo:
    def __init__(self, frame=None, error=None):
        self.frame, self.error, self.asked = frame, error, []

    def __call__(self, ticker, timeout):
        self.asked.append(ticker)
        if self.error:
            raise self.error
        return self.frame if self.frame is not None else minutes(("2026-09-28 10:51", 99.5))

    def source(self) -> lp.YFinanceLast:
        return lp.YFinanceLast(self)


def reader(*sources, **kw) -> lp.LivePrices:
    kw.setdefault("now", lambda: ASKED)
    return lp.LivePrices(sources, **kw)


class Hangs:
    """A source that does not answer for ``seconds``."""

    def __init__(self, name="alpaca-iex", seconds=0.5):
        self.name, self.seconds, self.asked = name, seconds, 0

    def quote(self, ticker, timeout):
        self.asked += 1
        time.sleep(self.seconds)
        return lp.Quote(price=1.0)


class Raises:
    def __init__(self, exc, name="alpaca-iex"):
        self.name, self.exc, self.asked = name, exc, 0

    def quote(self, ticker, timeout):
        self.asked += 1
        raise self.exc


# --------------------------------------------------------------------------- #
# A good read
# --------------------------------------------------------------------------- #


def test_an_alpaca_read_is_one_get_to_the_data_host_with_the_engines_key():
    alpaca = Alpaca()
    live = reader(alpaca.source()).read("nvda")

    assert live == {
        "price": 187.42, "bid": 187.40, "ask": 187.45,
        "quote_at": "2026-09-28T14:52:07.311123+00:00",
        "asked_at": ASKED.isoformat(), "source": "alpaca-iex",
    }
    assert list(live) == ["price", "bid", "ask", "quote_at", "asked_at", "source"]
    assert "error" not in live, "a line that has its price carries no error key"
    (request,) = alpaca.requests
    assert request.method == "GET"
    assert request.url.host == "data.alpaca.markets"
    assert request.url.path == "/v2/stocks/snapshots"
    assert dict(request.url.params) == {"symbols": "NVDA", "feed": "iex"}
    assert request.headers["APCA-API-KEY-ID"] == KEY
    assert request.headers["APCA-API-SECRET-KEY"] == SECRET
    assert KEY not in str(request.url) and SECRET not in str(request.url)


def test_an_oauth_login_is_sent_as_a_bearer_token():
    alpaca = Alpaca()
    token = lambda: AlpacaCredentials(access_token="oauth-token-xyz", source="cli-oauth:paper")
    reader(alpaca.source(token)).read("NVDA")
    (request,) = alpaca.requests
    assert request.headers["Authorization"] == "Bearer oauth-token-xyz"
    assert "APCA-API-KEY-ID" not in request.headers


def test_an_empty_side_of_the_book_is_null_not_zero():
    thin = {"NVDA": {"latestTrade": {"t": "2026-09-28T14:00:00Z", "p": 10.0},
                     "latestQuote": {"bp": 0, "ap": 10.2}}}
    live = reader(Alpaca(lambda r: httpx.Response(200, json=thin)).source()).read("NVDA")
    assert (live["price"], live["bid"], live["ask"]) == (10.0, None, 10.2)
    assert live["quote_at"] == "2026-09-28T14:00:00+00:00"


def test_the_connection_is_made_once_and_the_key_resolved_once_per_cycle():
    asked = []

    def counted():
        asked.append(1)
        return keys()

    alpaca = Alpaca()
    prices = reader(alpaca.source(counted))
    for _ in range(3):
        prices.read("NVDA")
    assert asked == [1]
    assert len(alpaca.requests) == 3


# --------------------------------------------------------------------------- #
# Falling back, and saying so
# --------------------------------------------------------------------------- #


def test_a_name_alpaca_has_no_trade_for_is_read_from_yfinance_and_says_so():
    alpaca, yahoo = Alpaca(lambda r: httpx.Response(200, json={})), Yahoo()
    prices = reader(alpaca.source(), yahoo.source())

    live = prices.read("EIS")
    assert live["source"] == "yfinance"
    assert live["price"] == 99.5 and live["bid"] is None and live["ask"] is None
    assert live["quote_at"] == "2026-09-28T14:51:00+00:00", "the bar's own time, in UTC"
    assert "error" not in live

    # A name Alpaca lacks says nothing about Alpaca: it is still asked.
    for _ in range(5):
        prices.read("EIS")
    assert len(alpaca.requests) == 6


def test_the_latest_usable_one_minute_close_is_the_price():
    frame = minutes(("2026-09-28 10:50", 99.0), ("2026-09-28 10:51", 99.5), ("2026-09-28 10:52", float("nan")))
    live = reader(Yahoo(frame).source()).read("EIS")
    assert live["price"] == 99.5 and live["quote_at"] == "2026-09-28T14:51:00+00:00"


def test_a_refused_key_is_not_asked_again_this_cycle():
    alpaca = Alpaca(lambda r: httpx.Response(403, json={"message": "forbidden."}))
    yahoo = Yahoo()
    prices = reader(alpaca.source(), yahoo.source())
    for _ in range(4):
        assert prices.read("NVDA")["source"] == "yfinance"
    assert len(alpaca.requests) == 1
    assert len(yahoo.asked) == 4


def test_no_key_at_all_means_yfinance_and_the_line_still_has_its_price():
    def none():
        raise BrokerError("No Alpaca credentials found")

    alpaca, yahoo = Alpaca(), Yahoo()
    live = reader(alpaca.source(none), yahoo.source()).read("NVDA")
    assert live["source"] == "yfinance" and live["price"] == 99.5
    assert alpaca.requests == []


def test_when_every_source_fails_the_line_says_why_and_has_every_key():
    alpaca = Alpaca(lambda r: httpx.Response(500, json={"message": "internal"}))
    yahoo = Yahoo(error=RuntimeError("Yahoo said no"))
    live = reader(alpaca.source(), yahoo.source()).read("NVDA")
    assert list(live) == ["price", "bid", "ask", "quote_at", "asked_at", "source", "error"]
    assert live["price"] is None and live["quote_at"] is None
    assert live["source"] == "yfinance", "the last source asked"
    assert live["asked_at"] == ASKED.isoformat()
    assert "alpaca-iex: HTTP 500 (internal)" in live["error"]
    assert "yfinance: RuntimeError: Yahoo said no" in live["error"]


@pytest.mark.parametrize("junk", [
    {"NVDA": {"latestTrade": {"p": 0}}},
    {"NVDA": {"latestTrade": {"p": float("nan")}}},
    {"NVDA": {"latestTrade": {"p": "187.42"}}},
    {"NVDA": {"latestTrade": None}},
    {"NVDA": "nope"},
    ["NVDA"],
])
def test_a_junk_answer_is_no_price_never_an_exception(junk):
    body = json.dumps(junk, allow_nan=True)
    alpaca = Alpaca(lambda r: httpx.Response(200, content=body, headers={"content-type": "application/json"}))
    live = reader(alpaca.source()).read("NVDA")
    assert live["price"] is None and "alpaca-iex" in live["error"]


def test_a_source_that_answers_nonsense_is_a_failure_not_a_crash():
    class Odd:
        name = "alpaca-iex"

        def quote(self, ticker, timeout):
            return {"price": 3}

    live = reader(Odd()).read("NVDA")
    assert live["price"] is None and "not a positive price" in live["error"]


# --------------------------------------------------------------------------- #
# Never in the way
# --------------------------------------------------------------------------- #


def test_a_hanging_source_is_cut_off_at_the_deadline():
    hangs = Hangs(seconds=1.0)
    started = time.monotonic()
    live = reader(hangs, read_timeout=0.05).read("NVDA")
    assert time.monotonic() - started < 0.5
    assert live["price"] is None and "no answer within 0.1s" in live["error"]


def test_three_failures_in_a_row_and_a_source_is_not_asked_again_this_cycle():
    hangs, yahoo = Hangs(seconds=0.3), Yahoo()
    prices = reader(hangs, yahoo.source(), read_timeout=0.02)
    for _ in range(6):
        assert prices.read("NVDA")["source"] == "yfinance"
    assert hangs.asked == 3
    assert len(yahoo.asked) == 6


def test_a_success_resets_the_count():
    flaky = [RuntimeError("1"), RuntimeError("2"), None, RuntimeError("3"), RuntimeError("4"), None]

    class Flaky:
        name = "alpaca-iex"

        def __init__(self):
            self.asked = 0

        def quote(self, ticker, timeout):
            self.asked += 1
            exc = flaky.pop(0)
            if exc:
                raise exc
            return lp.Quote(price=5.0)

    source = Flaky()
    prices = reader(source)
    for _ in range(6):
        prices.read("NVDA")
    assert source.asked == 6, "never three failures in a row, so never given up"


def test_the_cycle_budget_caps_all_the_waiting_and_then_costs_nothing():
    hangs = [Hangs("a", 0.5), Hangs("b", 0.5)]
    prices = reader(*hangs, read_timeout=0.05, budget=0.12, give_up_after=100)
    started = time.monotonic()
    lines = [prices.read(f"T{i}") for i in range(20)]
    took = time.monotonic() - started
    assert took < 0.6, f"twenty reads waited {took:.2f}s against a 0.12s budget"
    assert prices.spent <= 0.12 + 0.1
    assert "for reading prices is used up" in lines[-1]["error"]
    assert sum(h.asked for h in hangs) <= 4


def test_a_read_never_raises_whatever_the_source_throws():
    for exc in (RuntimeError("x"), KeyError("y"), ValueError("z"), lp.PriceUnavailable("w")):
        live = reader(Raises(exc)).read("NVDA")
        assert live["price"] is None and live["error"]


def test_with_no_sources_a_line_still_gets_a_record():
    live = reader().read("NVDA")
    assert live == {"price": None, "bid": None, "ask": None, "quote_at": None,
                    "asked_at": ASKED.isoformat(), "source": "none", "error": "no price source"}


def test_close_lets_go_of_the_connection():
    closed = []

    class Client(httpx.Client):
        def close(self):
            closed.append(1)
            super().close()

    transport = httpx.MockTransport(lambda r: httpx.Response(200, json=SNAPSHOT))
    prices = reader(lp.AlpacaIex(keys, lambda **kw: Client(transport=transport, **kw)))
    prices.read("NVDA")
    prices.close()
    assert closed == [1]
    lp.LivePrices([Raises(RuntimeError("x"))]).close()  # nothing to close: no error


# --------------------------------------------------------------------------- #
# The key goes into two headers and nowhere else
# --------------------------------------------------------------------------- #


def test_a_key_echoed_back_by_the_host_never_reaches_the_line_or_the_log(caplog):
    caplog.set_level(logging.DEBUG)
    echo = Alpaca(lambda r: httpx.Response(429, json={"message": f"slow down {KEY} / {SECRET}"}))
    live = reader(echo.source()).read("NVDA")
    assert "[redacted]" in live["error"]
    assert KEY not in json.dumps(live) and SECRET not in json.dumps(live)
    assert KEY not in caplog.text and SECRET not in caplog.text


def test_a_transport_error_naming_the_key_is_scrubbed_too(caplog):
    caplog.set_level(logging.DEBUG)

    def refuse(request):
        raise httpx.ConnectError(f"refused while sending {request.headers['APCA-API-SECRET-KEY']}")

    prices = reader(Alpaca(refuse).source())
    for _ in range(4):
        live = prices.read("NVDA")
        assert SECRET not in json.dumps(live)
    assert SECRET not in caplog.text


# --------------------------------------------------------------------------- #
# Which reader a cycle gets
# --------------------------------------------------------------------------- #


def test_direct_mode_asks_alpaca_then_yfinance_and_building_it_reads_no_key(monkeypatch):
    from app import broker_client

    monkeypatch.setattr(broker_client, "resolve_credentials",
                        lambda: (_ for _ in ()).throw(AssertionError("a key was read to build a reader")))
    prices = lp.for_dispatcher(DirectDispatcher(engine=object()))
    assert [s.name for s in prices.sources] == ["alpaca-iex", "yfinance"]


def test_webhook_mode_holds_no_broker_key_so_it_never_asks_alpaca():
    prices = lp.for_dispatcher(WebhookDispatcher())
    assert [s.name for s in prices.sources] == ["yfinance"]


@pytest.mark.parametrize("dispatcher", [None, object(), "direct"])
def test_any_other_dispatcher_gets_no_reader_and_so_no_network_call(dispatcher):
    assert lp.for_dispatcher(dispatcher) is None


def test_in_direct_mode_the_key_comes_from_the_brokers_own_resolver(monkeypatch):
    from app import broker_client

    monkeypatch.setattr(broker_client, "resolve_credentials", keys)
    alpaca = Alpaca()
    transport = httpx.MockTransport(alpaca.handler)
    source = lp.AlpacaIex(client_factory=lambda **kw: httpx.Client(transport=transport, **kw))
    reader(source).read("NVDA")
    assert alpaca.requests[0].headers["APCA-API-KEY-ID"] == KEY


# --------------------------------------------------------------------------- #
# Timestamps
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("raw, expected", [
    ("2026-09-28T14:52:07.311123456Z", "2026-09-28T14:52:07.311123+00:00"),
    ("2026-09-28T14:52:07Z", "2026-09-28T14:52:07+00:00"),
    ("2026-09-28T10:52:07-04:00", "2026-09-28T14:52:07+00:00"),
    (pd.Timestamp("2026-09-28 10:52", tz="America/New_York"), "2026-09-28T14:52:00+00:00"),
    (datetime(2026, 9, 28, 14, 52), "2026-09-28T14:52:00+00:00"),
    ("not a time", None), ("", None), (None, None), (1727535127, None),
])
def test_every_time_is_written_in_utc_like_the_journals_own(raw, expected):
    assert lp.iso_utc(raw) == expected


# --------------------------------------------------------------------------- #
# The suite-side mirror of the CI guardrail
# --------------------------------------------------------------------------- #


SOURCE = (ROOT / "orchestrator/live_price.py").read_text(encoding="utf-8")


def test_the_module_can_only_get_a_price():
    forbidden = re.compile(
        r"(\.(post|put|patch|delete|request|stream|submit_[a-z_]*|cancel[a-z_]*|replace_order[a-z_]*"
        r"|close_position[a-z_]*)\(|as_prompt|as_lines|\.write_text\(|\.write_bytes\(|open\([^)]*[\"'][wax])"
    )
    assert not forbidden.search(SOURCE)
    assert re.findall(r"https?://[^\"' ]+", SOURCE) == ["https://data.alpaca.markets/v2/stocks/snapshots"]


def test_the_key_is_touched_on_exactly_the_two_lines_ci_allows():
    credential = re.compile(r"(get_settings|os\.environ|getenv|\bsettings\.|\.[A-Za-z_]*(secret|api_key|_token|password)\b)")
    hits = [line for line in SOURCE.splitlines() if credential.search(line)]
    assert hits == [
        '        return {"Authorization": "Bearer " + credentials.access_token}',
        '    return {"APCA-API-KEY-ID": credentials.api_key, "APCA-API-SECRET-KEY": credentials.secret_key}',
    ]
    assert "alpaca_api_key" not in SOURCE and "alpaca_secret_key" not in SOURCE
    assert not re.search(r"^\s*(import|from)\s+alpaca", SOURCE, re.M), "the SDK stays in broker_client.py"


def test_only_the_heartbeat_imports_the_reader_and_no_price_reaches_post_signal():
    importer = re.compile(r"(from orchestrator import [^#\n]*\blive_price\b|orchestrator\.live_price|import live_price)")
    users = sorted(
        p.relative_to(ROOT).as_posix()
        for top in ("app", "orchestrator", "config", "analysis", "store", "backtest", "replay", "learn", "rules", "shadow")
        for p in (ROOT / top).rglob("*.py")
        if importer.search(p.read_text(encoding="utf-8"))
    )
    assert users == ["orchestrator/heartbeat.py"]
    heartbeat = (ROOT / "orchestrator/heartbeat.py").read_text(encoding="utf-8")
    assert not re.search(r"post_signal\([^)]*live", heartbeat)


def test_the_deadline_thread_cannot_keep_the_process_alive():
    before = {t.ident for t in threading.enumerate()}
    reader(Hangs(seconds=0.3), read_timeout=0.01).read("NVDA")
    new = [t for t in threading.enumerate() if t.ident not in before and t.name == "live-price"]
    assert new and all(t.daemon for t in new)
