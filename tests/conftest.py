"""Shared fakes. No test in this suite touches the network, Alpaca or yfinance."""

from __future__ import annotations

from dataclasses import dataclass, field

import pytest

from app.broker_client import OpenPosition, SubmittedOrder
from app.execution_engine import ExecutionEngine


@dataclass
class FakeBroker:
    equity: float = 100_000.0
    positions: list[OpenPosition] = field(default_factory=list)
    submitted: list[dict] = field(default_factory=list)

    def get_equity(self) -> float:
        return self.equity

    def get_open_positions(self) -> list[OpenPosition]:
        return list(self.positions)

    def submit_bracket_order(self, ticker: str, qty: int, side: str, stop_price: float) -> SubmittedOrder:
        self.submitted.append({"ticker": ticker, "qty": qty, "side": side, "stop_price": stop_price})
        return SubmittedOrder(order_id=f"fake-{len(self.submitted)}", ticker=ticker, qty=qty, side=side, stop_price=stop_price)


@dataclass
class FakeMarketData:
    price: float = 100.0
    atr: float = 2.0

    def get_latest_price(self, ticker: str) -> float:
        return self.price

    def get_atr(self, ticker: str) -> float:
        return self.atr


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


def _fresh_logger(path):
    import logging

    from pythonjsonlogger import jsonlogger

    lg = logging.getLogger("execution_audit")
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
