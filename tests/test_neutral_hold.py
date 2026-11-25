"""NEUTRAL on a broad fund means "hold the normal weight", not "no trade".

What has to stay true around that:

* it is an ordinary entry -- a bracket with a stop, every portfolio limit --
  only smaller, and the size comes from the ticker's kind, never the signal;
* it is the lowest-priority entry: it cannot fill the fund sleeve past its
  own share, it counts the orders the pass has already sent, and the cycle
  delivers it after every directional signal;
* nothing else changes: NEUTRAL on any other kind of ticker is still no
  trade, and an engine built without the switch behaves as it always did.
"""

from __future__ import annotations

import pytest

from app import risk_engine
from app.broker_client import OpenPosition
from app.execution_engine import ExecutionEngine
from app.schemas import ExecutionStatus, LLMSignal
from config import settings as cfg
from config.instruments import BROAD_FUNDS, COMMODITY_FUNDS, FOCUSED_FUNDS, SINGLE_NAMES
from config.settings import Settings
from orchestrator import heartbeat as hb
from orchestrator.llm import Completion, Usage
from tests.conftest import FakeBroker, FakeMarketData

EQUITY = 100_000.0


@pytest.fixture(autouse=True)
def _holds_switched_on(monkeypatch):
    """The feature under test, switched on, whatever production's switch says.

    ``NEUTRAL_HOLD_ENABLED`` is off in production until the core has run on
    its own; the engine tests below pass ``neutral_holds=True`` themselves,
    and the cycle tests read the constant.
    """
    monkeypatch.setattr(cfg, "NEUTRAL_HOLD_ENABLED", True)


HOLD_PCT = cfg.MAX_BROAD_FUND_PCT * cfg.NEUTRAL_HOLD_FRACTION


def sig(**over) -> LLMSignal:
    base = {"ticker": "RSP", "bias": "NEUTRAL", "conviction": 0.1, "rationale": "no view"}
    return LLMSignal.model_validate({**base, **over})


def pos(ticker: str, value: float, price: float = 100.0) -> OpenPosition:
    return OpenPosition(ticker, value / price, value, price)


def holding_engine(broker, market=None) -> ExecutionEngine:
    return ExecutionEngine(broker, market or FakeMarketData(), neutral_holds=True)


# --- the size ---------------------------------------------------------------


def test_the_normal_weight_is_a_fraction_of_the_broad_fund_cap():
    assert 0 < cfg.NEUTRAL_HOLD_FRACTION < 1
    for ticker in BROAD_FUNDS:
        assert risk_engine.neutral_hold_pct_for(ticker) == pytest.approx(HOLD_PCT)


@pytest.mark.parametrize("ticker", [SINGLE_NAMES[0], FOCUSED_FUNDS[0], COMMODITY_FUNDS[0], "ZZZZ"])
def test_only_a_broad_fund_has_a_normal_weight(ticker):
    """A sector, a country, one commodity, one company -- or a typo -- is a bet."""
    assert risk_engine.neutral_hold_pct_for(ticker) is None


def test_neutral_on_a_broad_fund_buys_its_normal_weight():
    broker, market = FakeBroker(equity=EQUITY), FakeMarketData(price=100.0, atr=2.0)
    result = holding_engine(broker, market).execute(sig())

    assert result.status is ExecutionStatus.ACCEPTED
    assert result.side == "buy"
    assert result.quantity == int(EQUITY * HOLD_PCT / 100.0)
    assert "neutral hold" in result.reason


def test_a_neutral_hold_is_half_a_bullish_position():
    neutral = holding_engine(FakeBroker(equity=EQUITY)).execute(sig())
    bullish = holding_engine(FakeBroker(equity=EQUITY)).execute(sig(bias="BULLISH", conviction=0.8))
    assert neutral.quantity == pytest.approx(bullish.quantity * cfg.NEUTRAL_HOLD_FRACTION)


def test_a_neutral_hold_carries_a_stop_like_every_other_entry():
    broker, market = FakeBroker(equity=EQUITY), FakeMarketData(price=100.0, atr=2.0)
    result = holding_engine(broker, market).execute(sig())
    assert result.stop_price == 100.0 - cfg.ATR_STOP_MULTIPLIER * 2.0
    assert broker.submitted == [
        {"ticker": "RSP", "qty": result.quantity, "side": "buy", "stop_price": result.stop_price}
    ]
    assert broker.core_bought == [], "a neutral hold is a bracket, never a stopless buy"


def test_the_conviction_floor_does_not_apply_to_a_neutral_hold():
    """The floor asks how sure the model is of a direction; NEUTRAL names none."""
    result = holding_engine(FakeBroker(equity=EQUITY)).execute(sig(conviction=0.0))
    assert result.status is ExecutionStatus.ACCEPTED


def test_the_conviction_floor_still_applies_to_a_directional_signal():
    result = holding_engine(FakeBroker(equity=EQUITY)).execute(
        sig(bias="BULLISH", conviction=cfg.MIN_CONVICTION - 0.01))
    assert result.status is ExecutionStatus.REJECTED and "conviction" in result.reason


# --- what does not change ---------------------------------------------------


@pytest.mark.parametrize("ticker", [SINGLE_NAMES[0], FOCUSED_FUNDS[0], COMMODITY_FUNDS[0]])
def test_neutral_on_anything_else_is_still_no_trade(ticker):
    broker = FakeBroker(equity=EQUITY)
    broker.get_equity = lambda: (_ for _ in ()).throw(AssertionError("should not be called"))
    result = holding_engine(broker).execute(sig(ticker=ticker))
    assert result.status is ExecutionStatus.REJECTED
    assert result.reason == "bias is NEUTRAL; no trade"
    assert broker.submitted == []


def test_an_engine_built_without_the_switch_never_holds():
    """Every simulated book builds the engine this way."""
    broker = FakeBroker(equity=EQUITY)
    result = ExecutionEngine(broker, FakeMarketData()).execute(sig())
    assert result.status is ExecutionStatus.REJECTED
    assert result.reason == "bias is NEUTRAL; no trade"
    assert broker.submitted == []


def test_a_closed_market_refuses_a_neutral_hold():
    result = holding_engine(FakeBroker(equity=EQUITY, market_open=False)).execute(sig())
    assert result.status is ExecutionStatus.REJECTED and "closed" in result.reason


# --- it opens, and nothing else ---------------------------------------------


@pytest.mark.parametrize("held", [2_000.0, 6_000.0, 12_000.0])
def test_a_neutral_hold_never_adds_to_a_position(held):
    broker = FakeBroker(equity=EQUITY, positions=[pos("RSP", held)])
    result = holding_engine(broker).execute(sig())
    assert result.status is ExecutionStatus.REJECTED and "already held" in result.reason
    assert broker.submitted == [] and broker.closed == []


def test_a_neutral_hold_does_not_touch_a_short():
    short = OpenPosition("RSP", -50.0, 5_000.0, 100.0)
    broker = FakeBroker(equity=EQUITY, positions=[short])
    result = holding_engine(broker).execute(sig())
    assert result.status is ExecutionStatus.REJECTED
    assert broker.submitted == [] and broker.closed == []


# --- it is the lowest priority ----------------------------------------------


def test_neutral_holds_stop_at_their_share_of_the_fund_sleeve():
    """The last of the fund budget is kept for funds the model has a view on."""
    funds = [pos("XLE", 7_000), pos("XLF", 7_000), pos("XLV", 7_000), pos("XLK", 7_000),
             pos("XLI", 7_000), pos("XLU", 7_000), pos("XLB", 7_000)]   # 49% in focused funds
    broker = FakeBroker(equity=EQUITY, positions=funds)
    result = holding_engine(broker).execute(sig(ticker="TLT"))

    room = EQUITY * cfg.NEUTRAL_HOLD_SLEEVE_PCT - 49_000
    assert result.status is ExecutionStatus.ACCEPTED
    assert result.quantity == int(room / 100.0) < int(EQUITY * HOLD_PCT / 100.0)

    full = FakeBroker(equity=EQUITY, positions=funds + [pos("XLP", 7_000)])    # 56%
    refused = holding_engine(full).execute(sig(ticker="TLT"))
    assert refused.status is ExecutionStatus.REJECTED
    assert "neutral-hold share of the sleeve budget" in refused.reason


def test_a_directional_fund_still_has_the_whole_sleeve():
    funds = [pos(t, 7_000) for t in ("XLE", "XLF", "XLV", "XLK", "XLI", "XLU", "XLB", "XLP")]  # 56%
    broker = FakeBroker(equity=EQUITY, positions=funds)
    result = holding_engine(broker).execute(sig(ticker="TLT", bias="BULLISH", conviction=0.8))
    assert result.status is ExecutionStatus.ACCEPTED
    assert result.quantity == int(EQUITY * cfg.MAX_BROAD_FUND_PCT / 100.0)


def test_the_sleeve_share_leaves_room_below_the_fund_sleeve():
    assert 0 < cfg.NEUTRAL_HOLD_SLEEVE_PCT < cfg.MAX_FUND_SLEEVE_PCT


def test_a_neutral_hold_obeys_the_duration_ceiling():
    book = [pos("TLT", 12_000), pos("IEF", 12_000), pos("LQD", 6_000)]   # Duration at its 30%
    result = holding_engine(FakeBroker(equity=EQUITY, positions=book)).execute(sig(ticker="SHY"))
    assert result.status is ExecutionStatus.REJECTED and "'Duration' group" in result.reason


def test_holds_in_one_pass_see_each_other_though_the_broker_shows_none():
    """The broker's list lags its fills; a pass of holds must not all fit 'the same' room.

    Every broad fund is NEUTRAL on the first day this runs. Sized against a
    list that shows none of the orders sent a moment earlier, all fourteen
    would be accepted -- 84% of the account against a 50% share.
    """
    broker = FakeBroker(equity=EQUITY)          # never shows a fill
    engine = holding_engine(broker)
    results = [engine.execute(sig(ticker=t)) for t in BROAD_FUNDS]

    accepted = [r for r in results if r.status is ExecutionStatus.ACCEPTED]
    assert 0 < len(accepted) < len(BROAD_FUNDS)
    total = sum(r.quantity * 100.0 for r in accepted)
    assert total <= EQUITY * cfg.NEUTRAL_HOLD_SLEEVE_PCT + 1e-6


def test_a_hold_sees_the_directional_orders_sent_before_it():
    broker = FakeBroker(equity=EQUITY)
    engine = holding_engine(broker)
    for ticker in ("XLE", "XLF", "XLV", "XLK", "XLI", "XLU", "XLB", "XLP"):   # 56% once filled
        assert engine.execute(sig(ticker=ticker, bias="BULLISH", conviction=0.8)).status \
            is ExecutionStatus.ACCEPTED
    assert engine.execute(sig(ticker="TLT")).status is ExecutionStatus.REJECTED


def test_a_second_hold_in_the_same_ticker_is_refused_before_the_fill_shows():
    engine = holding_engine(FakeBroker(equity=EQUITY))
    assert engine.execute(sig()).status is ExecutionStatus.ACCEPTED
    again = engine.execute(sig())
    assert again.status is ExecutionStatus.REJECTED and "already held" in again.reason


# --- the cycle delivers holds last -------------------------------------------


def _completion(ticker: str, bias: str) -> Completion:
    import json

    text = json.dumps({"ticker": ticker, "bias": bias, "conviction": 0.6, "rationale": "r"})
    return Completion(text=text, usage=Usage(model="m", input_tokens=1, output_tokens=1))


class _Recorder:
    def __init__(self):
        self.calls: list[str] = []

    def is_market_open(self):
        return True

    def manage_positions(self, protect_only: bool = False):
        self.calls.append("manage")
        return {"positions_seen": 0}

    def dispatch(self, signal):
        self.calls.append(f"{signal.bias.value}:{signal.ticker}")
        return {"mode": "direct", "status": "ACCEPTED", "reason": "ok", "quantity": 1, "order_id": "x"}

    def rebalance_core(self):
        self.calls.append("core")
        return {"invested_pct": 0.94, "bought": 1, "sold": 0, "errors": 0, "actions": [
            {"ticker": "VT", "action": "bought", "qty": 3, "price": 100.0, "held_qty": 3}]}


def _run(monkeypatch, biases: dict[str, str], dispatcher, batch: bool = False):
    monkeypatch.setattr(hb.cfg, "USE_BATCH_API", batch)
    monkeypatch.setattr(hb, "get_settings", lambda: Settings(watchlist=",".join(biases), _env_file=None))
    monkeypatch.setattr(hb, "fetch_news", lambda t: ["news"])

    def answer(system_prompt, user_prompt, schema):
        ticker = user_prompt.split("\n", 1)[0].removeprefix("TICKER:").strip()
        return _completion(ticker, biases[ticker])

    monkeypatch.setattr(hb, "call_llm", answer)
    monkeypatch.setattr(hb, "screen_signal", answer)
    return hb.run_cycle(dispatcher)


BIASES = {"RSP": "NEUTRAL", "XLE": "BULLISH", "TLT": "NEUTRAL", "NVDA": "BEARISH", "XLF": "NEUTRAL"}


def test_holds_are_delivered_after_every_directional_signal(monkeypatch):
    dispatcher = _Recorder()
    report = _run(monkeypatch, BIASES, dispatcher)

    assert dispatcher.calls == [
        "manage",
        "BULLISH:XLE", "BEARISH:NVDA", "NEUTRAL:XLF",   # a focused fund's NEUTRAL is not a hold
        "NEUTRAL:RSP", "NEUTRAL:TLT",                   # the holds, in watchlist order
        "core",
    ]
    assert len(report.completed) == len(BIASES)


def test_the_screen_hands_a_broad_fund_neutral_to_the_engine(monkeypatch):
    """With the funnel on, a screened NEUTRAL used to end the ticker unseen by the engine."""
    monkeypatch.setattr(hb, "SCREENING_ENABLED", True)
    dispatcher = _Recorder()
    report = _run(monkeypatch, BIASES, dispatcher)

    assert dispatcher.calls == ["manage", "BULLISH:XLE", "BEARISH:NVDA", "NEUTRAL:RSP", "NEUTRAL:TLT", "core"]
    assert [r.ticker for r in report.screened] == ["XLF"]
    assert sorted(r.ticker for r in report.completed) == ["NVDA", "RSP", "TLT", "XLE"]


def test_a_ticker_run_on_its_own_is_never_set_aside(monkeypatch):
    monkeypatch.setattr(hb, "fetch_news", lambda t: ["news"])
    monkeypatch.setattr(hb, "call_llm", lambda s, u, j: _completion("RSP", "NEUTRAL"))
    dispatcher = _Recorder()
    result = hb.process_ticker("RSP", dispatcher)
    assert isinstance(result, hb.TickerResult) and result.stage == hb.COMPLETED
    assert dispatcher.calls == ["NEUTRAL:RSP"]


def test_holds_are_not_set_aside_when_the_feature_is_off(monkeypatch):
    monkeypatch.setattr(hb.cfg, "NEUTRAL_HOLD_ENABLED", False)
    dispatcher = _Recorder()
    _run(monkeypatch, BIASES, dispatcher)
    assert dispatcher.calls == ["manage"] + [f"{b}:{t}" for t, b in BIASES.items()] + ["core"]


def test_a_held_hold_is_journalled_with_the_engines_verdict(monkeypatch, _journal_to_tmp):
    import json

    _run(monkeypatch, {"RSP": "NEUTRAL"}, _Recorder())
    lines = [json.loads(line) for line in _journal_to_tmp.read_text().splitlines()]
    rsp = [line for line in lines if line.get("ticker") == "RSP"]
    assert len(rsp) == 1
    assert rsp[0]["outcome"]["status"] == "ACCEPTED"


# --- the core pass closes the cycle ------------------------------------------


def test_the_core_pass_runs_after_the_last_signal_and_reaches_the_summary(monkeypatch):
    dispatcher = _Recorder()
    report = _run(monkeypatch, {"XLE": "BULLISH"}, dispatcher)
    assert dispatcher.calls[-1] == "core"
    assert report.core["bought"] == 1
    summary = hb.render_summary(report)
    assert "**Core:** 94.0% of the account invested" in summary
    assert "| VT | bought 3 at ~100.00, 3 held |" in summary


def test_a_dispatcher_with_no_core_is_not_an_error(monkeypatch):
    class Plain:
        def is_market_open(self):
            return True

        def dispatch(self, signal):
            return {"status": "ACCEPTED", "reason": "ok"}

    report = _run(monkeypatch, {"XLE": "BULLISH"}, Plain())
    assert report.core is None
    assert "Core" not in hb.render_summary(report)


def test_a_core_pass_that_raises_does_not_take_the_cycle_down(monkeypatch):
    class Broken(_Recorder):
        def rebalance_core(self):
            raise RuntimeError("boom")

    report = _run(monkeypatch, {"XLE": "BULLISH"}, Broken())
    assert len(report.completed) == 1
    assert "boom" in report.core["error"]
    assert "not rebalanced this cycle" in hb.render_summary(report)


# --- the rollout: the core first, holds later ---------------------------------


def test_with_the_switch_off_the_live_engine_is_built_without_holds(monkeypatch):
    """What production runs today: NEUTRAL is no trade everywhere, the core still on."""
    from orchestrator import dispatch

    monkeypatch.setattr(cfg, "NEUTRAL_HOLD_ENABLED", False)
    built = {}

    class Engine:
        def __init__(self, broker, market_data, neutral_holds, core):
            built.update(neutral_holds=neutral_holds, core=core)

    import app.broker_client, app.execution_engine, app.market_data
    monkeypatch.setattr(app.execution_engine, "ExecutionEngine", Engine)
    monkeypatch.setattr(app.broker_client, "AlpacaPaperBroker", lambda: None)
    monkeypatch.setattr(app.market_data, "YFinanceMarketData", lambda: None)
    dispatch.DirectDispatcher()._get_engine()
    assert built == {"neutral_holds": False, "core": cfg.CORE_ENABLED}
