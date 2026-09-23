"""Shared fakes. No test in this suite touches the network, Alpaca or yfinance."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date

import pytest

from app.broker_client import BrokerError, OpenPosition, StopOrder, SubmittedOrder
from app.execution_engine import ExecutionEngine


#: An ordinary Wednesday, chosen only for being a weekday that is not in
#: config.market_calendar.NYSE_HOLIDAYS. Frozen below so the calendar gate in
#: orchestrator.heartbeat cannot make a test's outcome depend on which real
#: calendar day happens to run it.
_A_TRADING_DAY = date(2026, 9, 16)


@pytest.fixture(autouse=True)
def _a_real_trading_day(monkeypatch):
    """Freeze "today" for the weekend/holiday gate.

    Without this, a test suite that runs on an actual weekend or listed
    holiday would have every cycle-running test skip before doing anything --
    the gate working exactly as designed, and exactly wrong for a test that
    wants to exercise the cycle it guards. A test for the gate itself
    overrides this with its own date.
    """
    from orchestrator import heartbeat as hb

    monkeypatch.setattr(hb, "today_et", lambda: _A_TRADING_DAY)


@pytest.fixture(autouse=True)
def _a_configured_deployment(monkeypatch):
    """Give the suite the bearer token a real deployment has.

    ``orchestrator.llm.MODEL_BASE_URL`` names an OpenAI-compatible endpoint,
    and ``heartbeat.full_model_provider`` refuses to ask it anonymously --
    deliberately, because an endpoint answering 401 once per ticker loses a
    session quietly now that no screen stands behind the full model. Every
    test that runs a cycle would otherwise fail on the missing key rather than
    on what it is testing. Nothing here reaches the network: the providers are
    faked in the tests themselves.
    """
    monkeypatch.setenv("FULL_MODEL_API_KEY", "test-full-model-key")


@pytest.fixture(autouse=True)
def _no_real_http(monkeypatch):
    """Make the file's first line true rather than merely intended.

    It stopped being true the moment the full model moved to an
    OpenAI-compatible endpoint: a test that faked ``AnthropicSignalProvider``
    was faking nothing, and ``OpenAICompatibleProvider`` built its own
    ``httpx.Client`` and went to api.deepinfra.com for real. It was the proxy
    that caught it, which is luck, not a test suite.

    A test that means to exercise the transport passes its own client, and
    that still works -- only the un-injected path is closed.
    """
    from orchestrator import llm as _llm

    def _refuse(timeout):
        raise AssertionError(
            "a test let orchestrator.llm open a real connection; "
            "pass a fake client to the provider instead"
        )

    monkeypatch.setattr(_llm, "new_http_client", _refuse)


@dataclass
class FakeBroker:
    equity: float = 100_000.0
    positions: list[OpenPosition] = field(default_factory=list)
    submitted: list[dict] = field(default_factory=list)
    # Open by default so existing tests exercise the trading path; set False
    # to test the closed-market gate.
    market_open: bool = True
    # Position management. ``stop_orders`` is what the ladder reads; the two
    # lists are what it did, in order, so a test can assert the sequence
    # (stop replaced *before* the tranche sold) and not only the totals.
    stop_orders: dict[str, StopOrder] = field(default_factory=dict)
    replaced: list[dict] = field(default_factory=list)
    closed: list[dict] = field(default_factory=list)
    protected: list[dict] = field(default_factory=list)

    def is_market_open(self) -> bool:
        return self.market_open

    def get_equity(self) -> float:
        return self.equity

    def get_open_positions(self) -> list[OpenPosition]:
        return list(self.positions)

    def submit_bracket_order(self, ticker: str, qty: int, side: str, stop_price: float) -> SubmittedOrder:
        self.submitted.append({"ticker": ticker, "qty": qty, "side": side, "stop_price": stop_price})
        order_id = f"fake-{len(self.submitted)}"
        # The OTO child, as the real broker would create it once the entry fills.
        self.stop_orders[ticker] = StopOrder(
            order_id=f"stop-{order_id}", ticker=ticker, qty=qty, stop_price=stop_price,
            side="sell" if side == "buy" else "buy",
        )
        return SubmittedOrder(order_id=order_id, ticker=ticker, qty=qty, side=side, stop_price=stop_price)

    # --- position management ---

    def get_open_stop_order(self, ticker: str):
        return self.stop_orders.get(ticker)

    def submit_stop_order(self, ticker: str, qty: int, side: str, stop_price: float) -> StopOrder:
        """Mirrors the real primitive's refusals, so a test cannot protect a phantom."""
        from app.broker_client import BrokerError

        held = next((p for p in self.positions if p.ticker == ticker), None)
        if held is None:
            raise BrokerError(f"refusing a stop for {ticker}: there is no open position to protect")
        closing = "sell" if held.qty > 0 else "buy"
        if side != closing or qty > abs(held.qty):
            raise BrokerError(f"refusing a stop for {ticker}: not a reduction")
        self.protected.append({"ticker": ticker, "qty": qty, "side": side, "stop_price": stop_price})
        placed = StopOrder(order_id=f"protect-{len(self.protected)}", ticker=ticker, qty=qty,
                           stop_price=stop_price, side=side)
        self.stop_orders[ticker] = placed
        return placed

    def replace_stop_order(self, order_id: str, qty: int, stop_price: float,
                           current_qty: int | None = None) -> StopOrder:
        for ticker, current in self.stop_orders.items():
            if current.order_id == order_id:
                updated = StopOrder(order_id, ticker, qty, stop_price, current.side)
                self.stop_orders[ticker] = updated
                self.replaced.append({"order_id": order_id, "ticker": ticker, "qty": qty,
                                      "stop_price": stop_price, "was": current.stop_price,
                                      # What the caller said the stop covers now. The
                                      # real client uses this to decide whether to send
                                      # a qty at all, so a test can assert on it.
                                      "current_qty": current_qty})
                return updated
        raise BrokerError(f"no open stop order {order_id}")

    def close_position_partially(self, ticker: str, qty: int) -> str:
        for index, position in enumerate(self.positions):
            if position.ticker != ticker:
                continue
            sign = 1 if position.qty > 0 else -1
            remaining = position.qty - sign * qty
            if abs(remaining) < 1e-9:
                self.positions.pop(index)
            else:
                scale = abs(remaining) / abs(position.qty)
                self.positions[index] = OpenPosition(
                    ticker, remaining, position.market_value * scale, position.avg_entry_price
                )
            self.closed.append({"ticker": ticker, "qty": qty})
            return f"close-{len(self.closed)}"
        raise BrokerError(f"no open position in {ticker}")


@dataclass
class FakeMarketData:
    price: float = 100.0
    atr: float = 2.0

    def get_latest_price(self, ticker: str) -> float:
        return self.price

    def get_atr(self, ticker: str) -> float:
        return self.atr


@pytest.fixture(autouse=True)
def _offline_market_context(monkeypatch):
    """No test may reach yfinance.

    Enrichment returns an empty context with a stated gap, which is also the
    shape a real outage produces -- so the default in every test is the
    degraded path, and a test that wants real snapshots injects its own
    provider.
    """
    from orchestrator import context as ctx

    class OfflineProvider:
        def fetch(self, ticker: str) -> ctx.RawMarketData:
            return ctx.RawMarketData(gaps=["market context disabled in tests"])

    # Replace the cached singleton rather than get_provider itself, so the
    # lookup path stays the real one.
    monkeypatch.setattr(ctx, "_provider", OfflineProvider())

    # The FX rate is a second yfinance caller, reached from run_cycle rather
    # than from the context provider, so patching the provider alone left it
    # hitting the network. It degrades to a gap rather than raising, which is
    # exactly why it could slip through green.
    from orchestrator import fx as fx_module
    from orchestrator import heartbeat as hb

    offline_rate = fx_module.FxRate(gap="FX disabled in tests")
    monkeypatch.setattr(fx_module, "fetch_rate", lambda *a, **k: offline_rate)
    monkeypatch.setattr(hb, "fetch_fx_rate", lambda *a, **k: offline_rate)

    # The screening stage is a third network caller, reached before call_llm.
    # Off by default so every existing test still exercises the one model
    # call it was written against; tests/test_funnel.py turns it on and
    # fakes the screen explicitly.
    monkeypatch.setattr(hb, "SCREENING_ENABLED", False)


@pytest.fixture(autouse=True)
def _no_ambient_credentials(monkeypatch):
    """No test may pick up a real credential from the machine it runs on.

    A developer who has run `brightdata login` or `alpaca profile login` would
    otherwise have a credential on disk that the "missing credentials" tests
    would silently find, passing locally and failing in CI -- or worse,
    reaching the network. The Alpaca case is the one that matters most: a real
    profile could carry a live-trading bundle.
    """
    from app import broker_client
    from orchestrator import news

    monkeypatch.delenv(news.CLI_ENV_VAR, raising=False)
    monkeypatch.delenv("BRIGHTDATA_API_TOKEN", raising=False)
    monkeypatch.delenv(news.CLI_UNLOCKER_ENV_VAR, raising=False)
    monkeypatch.setattr(news, "cli_credential_paths", list)

    # Point the Alpaca CLI lookup at a directory that cannot exist, so the
    # real ~/.config/alpaca is never consulted. Tests that exercise the
    # lookup set ALPACA_CONFIG_DIR to their own tmp_path.
    monkeypatch.delenv("ALPACA_API_KEY", raising=False)
    monkeypatch.delenv("ALPACA_SECRET_KEY", raising=False)
    monkeypatch.delenv(broker_client.CLI_PROFILE_ENV, raising=False)
    monkeypatch.setenv(broker_client.CLI_CONFIG_DIR_ENV, "/nonexistent/alpaca-config")


@pytest.fixture(autouse=True)
def _journal_to_tmp(tmp_path, monkeypatch):
    """Redirect the signal journal so tests never write into the repo's logs/ dir."""
    import logging

    from orchestrator import journal

    path = tmp_path / "signal_journal.log"
    monkeypatch.setattr(journal.cfg, "SIGNAL_JOURNAL_PATH", path, raising=True)
    monkeypatch.setattr(journal, "get_journal_logger", lambda p=path: _fresh_logger(p, "signal_journal"))
    yield path
    lg = logging.getLogger("signal_journal")
    for h in list(lg.handlers):
        h.close()
        lg.removeHandler(h)


@pytest.fixture(autouse=True)
def _audit_log_to_tmp(tmp_path, monkeypatch):
    """Redirect the audit log so tests never write into the repo's logs/ dir."""
    import logging

    from app import logger as audit

    log_path = tmp_path / "execution_audit.log"
    monkeypatch.setattr(audit.cfg, "AUDIT_LOG_PATH", log_path, raising=True)
    monkeypatch.setattr(audit, "get_audit_logger", lambda path=log_path: _fresh_logger(path))
    yield log_path
    lg = logging.getLogger("execution_audit")
    for h in list(lg.handlers):
        h.close()
        lg.removeHandler(h)


def _fresh_logger(path, name: str = "execution_audit"):
    import logging

    from pythonjsonlogger import jsonlogger

    lg = logging.getLogger(name)
    if not any(getattr(h, "baseFilename", None) == str(path) for h in lg.handlers):
        for h in list(lg.handlers):
            h.close()
            lg.removeHandler(h)
        h = logging.FileHandler(path, encoding="utf-8")
        h.setFormatter(jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(message)s"))
        lg.addHandler(h)
        lg.setLevel(logging.INFO)
        lg.propagate = False
    return lg


@pytest.fixture
def broker() -> FakeBroker:
    return FakeBroker()


@pytest.fixture
def market() -> FakeMarketData:
    return FakeMarketData()


@pytest.fixture
def engine(broker, market) -> ExecutionEngine:
    return ExecutionEngine(broker=broker, market_data=market)


@pytest.fixture(autouse=True)
def _blend_weights_to_tmp(tmp_path, monkeypatch):
    """Point the blend at a weights file that does not exist.

    The heartbeat reads ``BLEND_WEIGHTS_PATH`` on every cycle. A test must see
    the same thing whether or not a trainer has written the real file.
    """
    from orchestrator import blend

    monkeypatch.setattr(blend.cfg, "BLEND_WEIGHTS_PATH", tmp_path / "blend_weights.json", raising=True)
