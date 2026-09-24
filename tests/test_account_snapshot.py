"""The paper account, recorded read-only for the shadow funds' calibration.

A simulated fund is only worth reading once it has been shown to track the
account it imitates, and until app/account_snapshot.py the record had none of
the account's own numbers: no cash, no closing equity, no fill prices, no
stop exits. These tests hold the recorder to three things -- it reports what
the broker said in the shape the calibration reads, a failed read is recorded
as a failure rather than as an empty book, and it cannot move a share.
"""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

from app import account_snapshot as cli
from app import broker_client as bc

ROOT = Path(__file__).resolve().parents[1]


# --------------------------------------------------------------------------- #
# A fake SDK client that can read and can do nothing else
# --------------------------------------------------------------------------- #


def _position(symbol, qty, side, *, avg="100.0", value="1000.0", price="101.5"):
    return SimpleNamespace(symbol=symbol, qty=qty, side=side, avg_entry_price=avg,
                           market_value=value, current_price=price)


def _order(oid, symbol, *, kind="stop", status="new", side="sell", qty="10",
           stop_price="95.0", legs=None):
    return SimpleNamespace(id=oid, symbol=symbol, order_type=kind, type=kind, status=status,
                           side=side, qty=qty, stop_price=stop_price, legs=legs)


def _fill(n, at, *, symbol="xom", side="sell", qty="5", price="101.25"):
    return {"id": f"act-{n}", "order_id": f"ord-{n}", "symbol": symbol, "side": side,
            "qty": qty, "price": price, "transaction_time": at, "activity_type": "FILL"}


class _Sdk:
    """The five reads the snapshot makes, and a tripwire on everything else.

    Any attribute that is not one of the reads raises, so a snapshot that
    reached for submit_order, replace_order_by_id, cancel_order_by_id,
    close_position -- or anything else that is not a read -- fails the test
    loudly instead of quietly calling a fake.
    """

    _READS = {"get_account", "get_all_positions", "get_orders", "get"}

    def __init__(self, *, account=None, positions=(), orders=(), fill_pages=((),),
                 history=None, fail=()):
        self._account = account or SimpleNamespace(
            equity="100250.5", cash="40000", long_market_value="70250.5",
            short_market_value="-10000", last_equity="99800",
        )
        self._positions = list(positions)
        self._orders = list(orders)
        self._fill_pages = [list(p) for p in fill_pages]
        self._history = history if history is not None else {"timestamp": [], "equity": []}
        self._fail = set(fail)
        self.gets: list[tuple[str, dict]] = []
        self.order_requests: list = []
        self.touched: list[str] = []

    def _check(self, name):
        if name in self._fail:
            raise RuntimeError(f"{name} is down (HTTP 503)")

    def get_account(self):
        self._check("get_account")
        return self._account

    def get_all_positions(self):
        self._check("get_all_positions")
        return list(self._positions)

    def get_orders(self, request):
        self._check("get_orders")
        self.order_requests.append(request)
        return list(self._orders)

    def get(self, path, data=None):
        self.gets.append((path, dict(data or {})))
        if path == "/account/activities/FILL":
            self._check("fills")
            index = sum(1 for p, _ in self.gets if p == path) - 1
            return self._fill_pages[index] if index < len(self._fill_pages) else []
        if path == "/account/portfolio/history":
            self._check("history")
            return self._history
        raise AssertionError(f"unexpected GET {path}")

    # The four calls that change the book, named so the intent is explicit.
    def submit_order(self, *args, **kwargs):
        raise AssertionError("the snapshot submitted an order")

    def replace_order_by_id(self, *args, **kwargs):
        raise AssertionError("the snapshot replaced an order")

    def cancel_order_by_id(self, *args, **kwargs):
        raise AssertionError("the snapshot cancelled an order")

    def close_position(self, *args, **kwargs):
        raise AssertionError("the snapshot closed a position")

    def __getattr__(self, name):
        # Only reached for attributes not defined above.
        raise AssertionError(f"the snapshot reached for {name!r}, which is not a read")


def _broker(sdk) -> bc.AlpacaPaperBroker:
    broker = bc.AlpacaPaperBroker.__new__(bc.AlpacaPaperBroker)
    broker._client = sdk
    return broker


SINCE = datetime(2026, 9, 24, 15, 40, 12, tzinfo=timezone.utc)


# --------------------------------------------------------------------------- #
# What the snapshot says
# --------------------------------------------------------------------------- #


def test_the_account_numbers_are_plain_floats():
    snap = _broker(_Sdk()).account_snapshot(SINCE)
    assert snap["account"] == {
        "equity": 100250.5, "cash": 40000.0, "long_market_value": 70250.5,
        "short_market_value": -10000.0, "last_equity": 99800.0,
    }
    assert snap["errors"] == []


def test_a_missing_account_field_is_null_not_zero():
    """0.0 cash and "cash not reported" are different accounts."""
    account = SimpleNamespace(equity="100000", cash=None, long_market_value="0",
                              short_market_value="0", last_equity="")
    snap = _broker(_Sdk(account=account)).account_snapshot(SINCE)
    assert snap["account"]["cash"] is None
    assert snap["account"]["last_equity"] is None
    assert snap["account"]["long_market_value"] == 0.0


def test_a_short_is_signed_negative_and_its_value_is_absolute():
    from alpaca.trading.enums import PositionSide

    sdk = _Sdk(positions=[
        _position("xom", "7", PositionSide.LONG, value="700.0"),
        # Positive quantity with side short, as the SDK model can carry it...
        _position("USO", "4", PositionSide.SHORT, value="-416.0", price="104.0"),
        # ...and a negative one, which must not be flipped back to positive.
        _position("TLT", "-3", "short", value="-270.0"),
    ])
    rows = {r["ticker"]: r for r in _broker(sdk).account_snapshot(SINCE)["positions"]}
    assert rows["XOM"]["qty"] == 7.0 and rows["XOM"]["market_value"] == 700.0
    assert rows["USO"]["qty"] == -4.0 and rows["USO"]["market_value"] == 416.0
    assert rows["USO"]["current_price"] == 104.0 and rows["USO"]["avg_entry_price"] == 100.0
    assert rows["TLT"]["qty"] == -3.0 and rows["TLT"]["market_value"] == 270.0


def test_only_live_stop_orders_are_recorded_legs_included():
    from alpaca.trading.enums import OrderSide, OrderStatus, OrderType, QueryOrderStatus

    leg = _order("leg-1", "LLY", kind=OrderType.STOP, status=OrderStatus.HELD,
                 side=OrderSide.SELL, qty="9", stop_price="880.5")
    sdk = _Sdk(orders=[
        _order("stop-1", "xom", kind=OrderType.STOP, side=OrderSide.SELL, qty="7", stop_price="96"),
        _order("stop-2", "USO", side="buy", qty="4", stop_price="108.25"),
        _order("lim-1", "XOM", kind=OrderType.LIMIT),
        _order("trail-1", "XOM", kind=OrderType.TRAILING_STOP),
        _order("dead-1", "XOM", status="canceled"),
        _order("no-price", "XOM", stop_price=None),
        # A parent market order still open, carrying its stop as a leg.
        _order("parent-1", "LLY", kind=OrderType.MARKET, side="buy", legs=[leg]),
        # The same stop surfacing twice is recorded once.
        _order("stop-1", "XOM", kind=OrderType.STOP, side=OrderSide.SELL, qty="7", stop_price="96"),
    ])
    stops = _broker(sdk).account_snapshot(SINCE)["stops"]
    assert stops == [
        {"order_id": "stop-1", "ticker": "XOM", "qty": 7, "stop_price": 96.0, "side": "sell"},
        {"order_id": "stop-2", "ticker": "USO", "qty": 4, "stop_price": 108.25, "side": "buy"},
        {"order_id": "leg-1", "ticker": "LLY", "qty": 9, "stop_price": 880.5, "side": "sell"},
    ]
    [request] = sdk.order_requests
    assert request.status == QueryOrderStatus.OPEN and request.nested is True
    assert request.symbols is None, "every symbol, not one"
    assert request.limit == bc.SNAPSHOT_OPEN_ORDER_LIMIT, "Alpaca's default of 50 could drop stops"


def test_the_position_manager_lookup_still_finds_its_stop():
    """The stop rule was lifted into a shared helper; the lookup the ladder
    depends on must answer exactly as it did."""
    from alpaca.trading.enums import OrderSide, OrderType

    sdk = _Sdk(orders=[
        _order("stop-xom", "XOM", kind=OrderType.STOP, side=OrderSide.SELL, qty="7", stop_price="96"),
    ])
    found = _broker(sdk).get_open_stop_order("xom")
    assert found == bc.StopOrder("stop-xom", "XOM", 7, 96.0, "sell")
    assert _broker(_Sdk(orders=[_order("lim", "XOM", kind="limit")])).get_open_stop_order("XOM") is None


def test_fills_are_paged_by_the_last_id_and_come_back_oldest_first(monkeypatch):
    monkeypatch.setattr(bc, "SNAPSHOT_FILL_PAGE_SIZE", 2)
    pages = [
        [_fill(1, "2026-09-24T13:30:01.547389331Z", side="buy"),
         _fill(2, "2026-09-24T13:30:01Z", symbol="uso", side="sell_short")],
        [_fill(3, "2026-09-24T19:59:59.5Z"), _fill(4, "2026-09-25T13:31:00Z", price="99")],
        [_fill(5, "2026-09-25T14:00:00Z")],
    ]
    sdk = _Sdk(fill_pages=pages)
    snap = _broker(sdk).account_snapshot(SINCE)

    calls = [params for path, params in sdk.gets if path == "/account/activities/FILL"]
    assert len(calls) == 3, "a short third page ends the paging"
    assert calls[0] == {"after": "2026-09-24T15:40:12Z", "direction": "asc", "page_size": 2}
    assert "page_token" not in calls[0]
    assert calls[1]["page_token"] == "act-2" and calls[2]["page_token"] == "act-4"
    assert all(c["after"] == "2026-09-24T15:40:12Z" for c in calls)

    fills = snap["fills"]
    # act-2 came second from the server but is the older of the two (13:30:01
    # against 13:30:01.547...): oldest first means by time, not by page.
    assert [f["id"] for f in fills] == ["act-2", "act-1", "act-3", "act-4", "act-5"]
    assert fills[0] == {"id": "act-2", "order_id": "ord-2", "ticker": "USO", "side": "sell_short",
                        "qty": 5.0, "price": 101.25, "at": "2026-09-24T13:30:01Z"}
    assert fills[1]["at"] == "2026-09-24T13:30:01.547389Z"
    assert fills[3]["price"] == 99.0
    assert snap["fills_after"] == "2026-09-24T15:40:12Z"
    assert snap["errors"] == []


def test_with_no_earlier_snapshot_fills_go_back_ten_days():
    sdk = _Sdk()
    before = datetime.now(timezone.utc)
    snap = _broker(sdk).account_snapshot(None)
    [(_, params)] = [g for g in sdk.gets if g[0] == "/account/activities/FILL"]
    after = datetime.fromisoformat(params["after"].replace("Z", "+00:00"))
    expected = before - timedelta(days=bc.SNAPSHOT_FILL_LOOKBACK_DAYS)
    assert abs((after - expected).total_seconds()) < 60
    assert bc.SNAPSHOT_FILL_LOOKBACK_DAYS == 10
    assert snap["fills"] == []


def test_the_page_cap_keeps_what_was_read_and_says_it_stopped(monkeypatch):
    """The next window starts after this snapshot, so fills beyond the cap
    would vanish without a word unless the record says so."""
    monkeypatch.setattr(bc, "SNAPSHOT_FILL_PAGE_SIZE", 1)
    monkeypatch.setattr(bc, "SNAPSHOT_FILL_MAX_PAGES", 3)
    sdk = _Sdk(fill_pages=[[_fill(n, f"2026-09-24T14:0{n}:00Z")] for n in range(1, 10)])
    snap = _broker(sdk).account_snapshot(SINCE)
    assert [f["id"] for f in snap["fills"]] == ["act-1", "act-2", "act-3"]
    assert len([g for g in sdk.gets if g[0] == "/account/activities/FILL"]) == 3
    [error] = snap["errors"]
    assert error["part"] == "fills" and "not read" in error["error"]


def test_history_is_dated_in_new_york():
    """02:00 UTC on the 22nd is 22:00 on the 21st in New York -- read in UTC,
    that close would be filed under the wrong session."""
    ny_midnight_21 = int(datetime(2026, 9, 21, 4, 0, tzinfo=timezone.utc).timestamp())
    late_21 = int(datetime(2026, 9, 22, 2, 0, tzinfo=timezone.utc).timestamp())
    ny_midnight_22 = int(datetime(2026, 9, 22, 4, 0, tzinfo=timezone.utc).timestamp())
    sdk = _Sdk(history={"timestamp": [ny_midnight_21, late_21, ny_midnight_22],
                        "equity": [100000.0, 100125.5, None], "profit_loss": [0, 0, 0]})
    snap = _broker(sdk).account_snapshot(SINCE)
    assert snap["history"] == {"days": ["2026-09-21", "2026-09-21", "2026-09-22"],
                               "equity": [100000.0, 100125.5, None]}
    [(_, params)] = [g for g in sdk.gets if g[0] == "/account/portfolio/history"]
    assert params == {"period": "1M", "timeframe": "1D"}


@pytest.mark.parametrize("broken, part", [
    ("get_account", "account"),
    ("get_all_positions", "positions"),
    ("get_orders", "stops"),
    ("fills", "fills"),
    ("history", "history"),
])
def test_one_failed_read_is_null_with_a_reason_and_the_rest_still_recorded(broken, part):
    """Null, not []: an empty list says "no open positions", and a
    calibration that read a failed read as a flat book would be comparing
    the simulation with an account that never existed."""
    snap = _broker(_Sdk(positions=[_position("XOM", "7", "long")], fail={broken})).account_snapshot(SINCE)
    assert snap[part] is None
    [error] = snap["errors"]
    assert error == {"part": part, "error": f"RuntimeError: {broken} is down (HTTP 503)"}
    for other in {"account", "positions", "stops", "fills", "history"} - {part}:
        assert snap[other] is not None, other


def test_the_snapshot_never_touches_the_book():
    """Every call a snapshot makes is one of the five reads.

    The fake raises on submit_order, replace_order_by_id, cancel_order_by_id
    and close_position, and on any other attribute that is not a read. Were
    the snapshot to reach one, the error would land in "errors" (each part is
    caught so one failure cannot cost the record), so the proof is that the
    record is clean.
    """
    from alpaca.trading.enums import OrderType

    sdk = _Sdk(
        positions=[_position("XOM", "7", "long"), _position("USO", "4", "short")],
        orders=[_order("stop-1", "XOM", kind=OrderType.STOP)],
        fill_pages=[[_fill(1, "2026-09-24T16:00:00Z")]],
        history={"timestamp": [1790049600], "equity": [100000.0]},
    )
    snap = _broker(sdk).account_snapshot(SINCE)
    assert snap["errors"] == []
    assert all(snap[p] is not None for p in ("account", "positions", "stops", "fills", "history"))
    with pytest.raises(AssertionError):
        sdk.close_all_positions()  # the tripwire itself works


# --------------------------------------------------------------------------- #
# The command line
# --------------------------------------------------------------------------- #


class _FakeBroker:
    """Stands in for AlpacaPaperBroker in the CLI: no credentials, no SDK."""

    seen_since: list = []
    raise_on_init: Exception | None = None
    chatter = False

    def __init__(self):
        if _FakeBroker.raise_on_init is not None:
            raise _FakeBroker.raise_on_init

    def account_snapshot(self, since):
        _FakeBroker.seen_since.append(since)
        if _FakeBroker.chatter:
            print("a library that prints to stdout")
        return {"account": {"equity": 100000.0, "cash": 5000.0, "long_market_value": 95000.0,
                            "short_market_value": 0.0, "last_equity": 99000.0},
                "positions": [], "stops": [], "fills": [],
                "history": {"days": [], "equity": []},
                "fills_after": "2026-09-24T15:40:12Z", "errors": []}


@pytest.fixture
def fake_broker(monkeypatch):
    _FakeBroker.seen_since = []
    _FakeBroker.raise_on_init = None
    _FakeBroker.chatter = False
    monkeypatch.setattr(cli, "AlpacaPaperBroker", _FakeBroker)
    return _FakeBroker


def _lines(capsys) -> list[str]:
    return capsys.readouterr().out.splitlines()


def test_the_cli_prints_one_line_with_when_which_commit_and_which_run(tmp_path, capsys,
                                                                     monkeypatch, fake_broker):
    monkeypatch.setenv("GITHUB_SHA", "abc123")
    log = tmp_path / "account.jsonl"
    assert cli.main(["--log", str(log), "--mode", "protect"]) == 0

    [line] = _lines(capsys)
    record = json.loads(line)
    assert record["sha"] == "abc123" and record["mode"] == "protect"
    at = datetime.strptime(record["at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    assert abs((datetime.now(timezone.utc) - at).total_seconds()) < 60
    assert record["account"]["cash"] == 5000.0 and record["fills"] == []
    assert list(record)[:3] == ["at", "sha", "mode"]
    assert " " not in line, "compact: one line, no padding"
    assert not log.exists(), "the recorder prints; the workflow appends"
    assert fake_broker.seen_since == [None]


def test_without_a_commit_sha_the_field_is_null(tmp_path, capsys, monkeypatch, fake_broker):
    monkeypatch.delenv("GITHUB_SHA", raising=False)
    cli.main(["--log", str(tmp_path / "account.jsonl"), "--mode", "cycle"])
    assert json.loads(_lines(capsys)[0])["sha"] is None


def test_the_cli_exits_zero_with_an_error_line_when_the_broker_raises(tmp_path, capsys, fake_broker):
    """A recorder that could turn a trading run red is one somebody turns off."""
    fake_broker.raise_on_init = bc.BrokerError("No Alpaca credentials found")
    assert cli.main(["--log", str(tmp_path / "account.jsonl"), "--mode", "cycle"]) == 0
    [line] = _lines(capsys)
    record = json.loads(line)
    assert record["error"] == "BrokerError: No Alpaca credentials found"
    assert record["mode"] == "cycle" and record["at"].endswith("Z")
    assert "fills" not in record


def test_stray_prints_do_not_reach_the_log(tmp_path, capsys, fake_broker):
    """The workflow appends stdout to the log, so stdout is exactly one line."""
    fake_broker.chatter = True
    cli.main(["--log", str(tmp_path / "account.jsonl"), "--mode", "cycle"])
    captured = capsys.readouterr()
    assert len(captured.out.splitlines()) == 1
    assert "a library that prints" in captured.err


def test_the_cli_starts_the_fills_window_where_the_last_snapshot_ended(tmp_path, capsys, fake_broker):
    log = tmp_path / "account.jsonl"
    before = log.write_text(
        '{"at":"2026-09-22T15:00:00Z","mode":"cycle","fills":[]}\n'
        '{"at":"2026-09-23T15:05:09Z","mode":"cycle","fills":[],"new_field":1}\n',
        encoding="utf-8",
    )
    cli.main(["--log", str(log), "--mode", "cycle"])
    assert fake_broker.seen_since == [datetime(2026, 9, 23, 15, 5, 9, tzinfo=timezone.utc)]
    assert log.stat().st_size == before, "the log is read, never written"


def test_a_snapshot_that_read_no_fills_does_not_move_the_window(tmp_path, capsys, fake_broker):
    """An error line, or a snapshot whose fills read failed, read nothing for
    its window. Starting after it would drop those fills for good."""
    log = tmp_path / "account.jsonl"
    log.write_text(
        '{"at":"2026-09-22T15:00:00Z","mode":"cycle","fills":[]}\n'
        '{"at":"2026-09-23T15:00:00Z","mode":"cycle","fills":null}\n'
        '{"at":"2026-09-24T15:00:00Z","mode":"cycle","error":"BrokerError: x"}\n'
        'not json at all\n\n',
        encoding="utf-8",
    )
    cli.main(["--log", str(log), "--mode", "cycle"])
    assert fake_broker.seen_since == [datetime(2026, 9, 22, 15, 0, tzinfo=timezone.utc)]


def test_the_latest_at_wins_over_the_last_line(tmp_path, capsys, fake_broker):
    """The log merges as a union, so two runs' lines can land in either order."""
    log = tmp_path / "account.jsonl"
    log.write_text(
        '{"at":"2026-09-24T21:00:00Z","mode":"protect","fills":[]}\n'
        '{"at":"2026-09-24T15:00:00Z","mode":"cycle","fills":[]}\n',
        encoding="utf-8",
    )
    cli.main(["--log", str(log), "--mode", "cycle"])
    assert fake_broker.seen_since == [datetime(2026, 9, 24, 21, 0, tzinfo=timezone.utc)]


def test_an_empty_log_has_no_window(tmp_path, capsys, fake_broker):
    """`>>` creates the file before the script runs, so the first run sees it empty."""
    log = tmp_path / "account.jsonl"
    log.write_text("", encoding="utf-8")
    cli.main(["--log", str(log), "--mode", "cycle"])
    assert fake_broker.seen_since == [None]


def test_the_recorder_holds_no_key_and_imports_no_sdk():
    """broker_client.py is the one module that reads the keys and imports the
    SDK (CI enforces both); the recorder only asks it."""
    source = (ROOT / "app/account_snapshot.py").read_text(encoding="utf-8")
    for banned in ("ALPACA_API_KEY", "ALPACA_SECRET_KEY", "alpaca_api_key", "alpaca_secret_key",
                   "get_settings", "import alpaca", "from alpaca", ".write_text(", "open("):
        assert banned not in source, banned


# --------------------------------------------------------------------------- #
# The heartbeat runs it, and commits what it wrote
# --------------------------------------------------------------------------- #


def _heartbeat_steps() -> list[dict]:
    wf = yaml.safe_load((ROOT / ".github/workflows/heartbeat.yml").read_text())
    return wf["jobs"]["cycle"]["steps"]


def test_the_heartbeat_records_the_account_after_trading_and_before_the_commit():
    steps = _heartbeat_steps()
    names = [s.get("name") for s in steps]
    here = names.index("Record the paper account")
    assert here > names.index("Protect every open position")
    assert here > names.index("Run one cycle")
    assert here < names.index("Commit the journal")

    step = steps[here]
    assert step["continue-on-error"] is True, "a recorder must never fail a trading run"
    assert step["timeout-minutes"] <= 3
    # Both modes, never a skipped day, and on a red cycle too.
    assert step["if"] == "always() && steps.guard.outputs.ran != 'yes'"
    assert "inputs.mode" not in step["if"]
    run = " ".join(step["run"].split())
    assert run.startswith("python -m app.account_snapshot --log logs/account.jsonl --mode ")
    assert run.endswith(">> logs/account.jsonl")
    assert step["env"]["MODE"] == "${{ inputs.mode || 'cycle' }}"


def test_the_recorder_step_gets_the_two_alpaca_secrets_and_nothing_else():
    steps = {s.get("name"): s for s in _heartbeat_steps()}
    env = steps["Record the paper account"]["env"]
    secrets = {k: v for k, v in env.items() if "secrets." in str(v)}
    assert secrets == {
        "ALPACA_API_KEY": "${{ secrets.ALPACA_API_KEY }}",
        "ALPACA_SECRET_KEY": "${{ secrets.ALPACA_SECRET_KEY }}",
    }
    # Passed exactly as the steps that trade pass them.
    for trader in ("Protect every open position", "Run one cycle"):
        for name, value in secrets.items():
            assert steps[trader]["env"][name] == value, (trader, name)


def test_the_account_log_is_committed_and_merges_as_a_union():
    steps = {s.get("name"): s for s in _heartbeat_steps()}
    add = next(line for line in steps["Commit the journal"]["run"].splitlines()
               if line.strip().startswith("git add -f"))
    assert "logs/account.jsonl" in add.split()
    attributes = (ROOT / ".gitattributes").read_text().splitlines()
    assert "logs/account.jsonl merge=union" in attributes
