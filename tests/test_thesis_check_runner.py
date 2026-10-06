"""The thesis-check logger: built now, off until 2027-04-01, log only.

The owner's instruction of 4 Oct 2026, item 2: once a week, for each held
name, ask the same model whether the reasoning archived with the entry still
holds, given today's headlines -- VALID, WEAKENED or BROKEN, with one sentence
of reason. It never trades, never changes a stop, never feeds an arm. This
file pins the flag to the pre-registration, the week's rule (the check day,
the retries), where the reasoning and the headlines come from, the answer's
checks, the weekly cost cap, the logger away from the engine and from every
file but its own, and the workflow's job.

Offline throughout: the model is a scripted OpenAI-compatible endpoint behind
the real provider.
"""

from __future__ import annotations

import ast
import json
import math
import re
import threading
import typing
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace

import httpx
import pytest
import yaml

from analysis import thesis as checks
from config import settings as cfg
from config import thesis_check as tc
from config.journal_files import month_file
from orchestrator import heartbeat, journal, llm, thesis
from orchestrator.llm import OpenAICompatibleProvider
from orchestrator.pricing import Usage
from tests.test_model_vote_runner import assert_cannot_trade, assert_reads_no_credential_and_no_blend
from tests.test_phone import _is_a_safe_push

ROOT = Path(__file__).resolve().parents[1]
PREREG = ROOT / "docs/horse-race-preregistration.md"
WORKFLOW = ROOT / ".github/workflows/shadow-universe.yml"
SOURCE = ROOT / "orchestrator/thesis.py"

#: A Monday in the logger's first full week (2027-W14), at the universe's backup hour.
MONDAY = datetime(2027, 4, 5, 18, 30, tzinfo=timezone.utc)

LINE_KEYS = {
    "ts_utc", "event", "week", "ticker", "side", "entry", "headline_count", "verdict", "reason", "asks",
    "cost_usd", "model_setup", "reasoning_effort", "error",
}


# --------------------------------------------------------------------------- #
# The flag and the pre-registration
# --------------------------------------------------------------------------- #

FLAG_PHRASE = "Thesis-check logger (`THESIS_CHECK_ENABLED`): **{state}** until **"


def test_the_flag_is_the_one_the_pre_registration_registers():
    """The file says off or on and until when; the code's start date is that
    date; and the flag cannot be on before it. Fails until the
    pre-registration carries the phrase -- the file is amended first."""
    text = " ".join(PREREG.read_text(encoding="utf-8").split())
    off, on = FLAG_PHRASE.format(state="off"), FLAG_PHRASE.format(state="on")
    assert off in text or on in text, (
        f"the pre-registration does not register the thesis check; it must say {off}{tc.START.isoformat()}**"
    )
    registered_off = off in text
    tail = text.split(off if registered_off else on, 1)[1]
    found = re.match(r"(\d{4}-\d{2}-\d{2})\*\*", tail)
    assert found, "the registered date must follow `until **` as YYYY-MM-DD"
    registered = date.fromisoformat(found.group(1))
    assert tc.START == registered, f"START is {tc.START}; the pre-registration registers {registered}"
    if registered_off:
        assert tc.THESIS_CHECK_ENABLED is False, (
            "THESIS_CHECK_ENABLED is on but the pre-registration says off; amend the file first"
        )
    if date.today() < registered:
        assert tc.THESIS_CHECK_ENABLED is False, (
            f"THESIS_CHECK_ENABLED is on before {registered}, the date the pre-registration names"
        )


def test_the_registered_settings():
    assert tc.START == date(2027, 4, 1) and tc.REGISTRATION == date(2027, 3, 22)
    assert tc.REGISTRATION < tc.START
    assert tc.WEEKLY_COST_CAP_USD == 0.10 and tc.ESTIMATED_WEEKLY_COST_USD < tc.WEEKLY_COST_CAP_USD
    assert tc.REASON_MAX_CHARS == 300
    # The answer's three verdicts are the config's, in its order, and the schema holds the model to them.
    assert typing.get_args(thesis.ThesisCheck.model_fields["verdict"].annotation) == tc.VERDICTS
    assert thesis.SCHEMA["properties"]["verdict"]["enum"] == list(tc.VERDICTS)
    assert tc.JOURNAL_DIR == cfg.LOG_DIR / "thesis_check"
    assert thesis.NO_NEW_NAME_AFTER_UTC.isoformat() == "23:15:00"


# --------------------------------------------------------------------------- #
# A scripted endpoint, the production journal and the audit log
# --------------------------------------------------------------------------- #

CHEAP = {"prompt_tokens": 1500, "completion_tokens": 800}
CHEAP_USD = Usage(model=llm.MODEL, input_tokens=1500, output_tokens=800).cost_usd
DIME = {"prompt_tokens": 0, "completion_tokens": 222_223}


def _ticker_of(body: dict) -> str:
    return re.search(r"Respond with the JSON thesis check for (\S+)\.$", body["messages"][1]["content"]).group(1)


def _answer(ticker: str, verdict: str = "VALID", reason: str = "The trend and the upgrade still stand.") -> dict:
    return {"ticker": ticker, "verdict": verdict, "reason": reason}


class Endpoint:
    """Per ticker, a script of steps (a response, an exception, an answer dict), then a VALID answer."""

    def __init__(self) -> None:
        self.script: dict[str, list] = {}
        self.usage = dict(CHEAP)
        self.sent: list[dict] = []
        self._lock = threading.Lock()

    def __call__(self, request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content)
        ticker = _ticker_of(body)
        with self._lock:
            self.sent.append(body)
            steps = self.script.get(ticker)
            step = steps.pop(0) if steps else None
        if isinstance(step, BaseException):
            raise step
        if isinstance(step, httpx.Response):
            return step
        content = json.dumps(step if isinstance(step, dict) else _answer(ticker))
        return httpx.Response(200, json={"choices": [{"message": {"content": content}}], "usage": self.usage})

    def asked(self) -> list[str]:
        return [_ticker_of(body) for body in self.sent]

    def user_prompt(self, ticker: str) -> str:
        return next(b["messages"][1]["content"] for b in self.sent if _ticker_of(b) == ticker)


@pytest.fixture
def wired(monkeypatch, tmp_path):
    """The flag on, a Monday in April 2027, the real provider over the scripted
    endpoint, and production's order path, journal and context booby-trapped."""
    monkeypatch.setattr(tc, "THESIS_CHECK_ENABLED", True)
    monkeypatch.setattr(thesis, "utc_now", lambda: MONDAY)
    endpoint = Endpoint()
    provider = OpenAICompatibleProvider(
        "https://api.example.test/v1/openai", heartbeat.MODEL, api_key="plain-test-key",
        client=httpx.Client(transport=httpx.MockTransport(endpoint)), sleep=lambda _: None,
        timeout=llm.FULL_MODEL_TIMEOUT_SECONDS,
    )
    monkeypatch.setattr(heartbeat, "full_model_provider", lambda: provider)

    def never(*_args, **_kwargs):
        raise AssertionError("the thesis check reached the engine, the production journal or the context gather")

    for name in ("post_signal", "build_dispatcher", "judge_answer", "process_ticker", "prepare_ticker",
                 "apply_screen", "journal_context_failure", "build_context", "fetch_news", "call_llm",
                 "manage_positions", "protect_positions"):
        monkeypatch.setattr(heartbeat, name, never)
    monkeypatch.setattr(journal, "record", never)
    from orchestrator import context
    monkeypatch.setattr(context, "gather", never)

    journal_dir = tmp_path / "journal"
    monkeypatch.setattr(cfg, "SIGNAL_JOURNAL_PATH", journal_dir)
    lines = tmp_path / "thesis_check"
    return SimpleNamespace(endpoint=endpoint, journal=journal_dir, lines=lines, capture=tmp_path / "model_io",
                           audit=Path(cfg.AUDIT_LOG_PATH), month=month_file(lines, MONDAY))


def _cycle(wired, day: date, held: dict[str, list[str]], answered: tuple[str, ...] = ("XLE",),
           hour: int = 15) -> None:
    """One production cycle on ``day``: a held line for each name in ``held`` (with its headlines)."""
    when = datetime(day.year, day.month, day.day, hour, 0, tzinfo=timezone.utc)
    path = month_file(wired.journal, when)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for i, (ticker, headlines) in enumerate(held.items()):
            handle.write(json.dumps({
                "ts_utc": (when + timedelta(seconds=i)).isoformat(), "ticker": ticker,
                "context": {"ticker": ticker, "headlines": headlines}, "signal": None, "error": None,
                "held": True, "event": "signal_generated"}) + "\n")
        for ticker in answered:
            handle.write(json.dumps({
                "ts_utc": (when + timedelta(minutes=5)).isoformat(), "ticker": ticker,
                "context": {"ticker": ticker, "headlines": ["x"]}, "held": False, "error": None,
                "signal": {"ticker": ticker, "bias": "BULLISH", "conviction": 0.6, "rationale": "r"},
                "event": "signal_generated"}) + "\n")


def _entry(wired, ticker: str, when: datetime, *, side: str = "buy", status: str = "ACCEPTED",
           rationale: str | None = None, key_factors: list[str] | None = None, entry_price: float | None = 100.0,
           bias: str | None = None) -> None:
    """One ``signal_processed`` audit record, as the engine's audit logger writes it."""
    bias = bias or ("BULLISH" if side == "buy" else "BEARISH")
    record = {
        "signal": {"ticker": ticker, "bias": bias, "conviction": 0.62,
                   "rationale": rationale if rationale is not None else f"{ticker}: breakout on rising volume",
                   "key_factors": key_factors if key_factors is not None else ["breakout", "volume"]},
        "result": {"status": status, "ticker": ticker, "bias": bias, "conviction": 0.62, "reason": "ok",
                   "quantity": 10, "side": side, "entry_price": entry_price, "stop_price": 95.0,
                   "timestamp": when.isoformat().replace("+00:00", "Z")},
        "ts": when.strftime("%Y-%m-%d %H:%M:%S,000"), "level": "INFO", "event": "signal_processed",
    }
    with wired.audit.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record) + "\n")


def _lines(wired) -> list[dict]:
    if not wired.lines.exists():
        return []
    return [json.loads(line) for path in sorted(wired.lines.glob("*.log"))
            for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _run(wired, **kwargs) -> thesis.ThesisRun:
    kwargs.setdefault("journal_dir", wired.lines)
    kwargs.setdefault("capture_dir", wired.capture)
    return thesis.check_theses(**kwargs)


def _at(monkeypatch, moment: datetime) -> None:
    monkeypatch.setattr(thesis, "utc_now", lambda: moment)


# --------------------------------------------------------------------------- #
# The logger stays off when it should
# --------------------------------------------------------------------------- #


@pytest.fixture
def nothing_may_happen(monkeypatch, tmp_path):
    """Any model call, any read of the week, or any file would be a failure."""
    def refuse(*_args, **_kwargs):
        raise AssertionError("the thesis check did something on a day it must not run")

    for name in ("call_llm", "full_model_provider", "model_setup", "full_model_effort"):
        monkeypatch.setattr(heartbeat, name, refuse)
    for name in ("due_names", "week_lines", "latest_entries"):
        monkeypatch.setattr(thesis, name, refuse)
    return SimpleNamespace(lines=tmp_path / "thesis_check", capture=tmp_path / "capture")


@pytest.mark.parametrize("enabled, now, reason", [
    (False, MONDAY, "the flag THESIS_CHECK_ENABLED is off"),
    (True, datetime(2027, 3, 31, 18, 30, tzinfo=timezone.utc), "before the start date 2027-04-01"),
    (True, datetime(2027, 5, 31, 18, 30, tzinfo=timezone.utc), "not a trading day"),   # Memorial Day
    (True, datetime(2027, 4, 10, 18, 30, tzinfo=timezone.utc), "not a trading day"),   # a Saturday
])
def test_the_logger_does_nothing_when_off_early_or_closed(monkeypatch, nothing_may_happen, enabled, now, reason):
    monkeypatch.setattr(tc, "THESIS_CHECK_ENABLED", enabled)
    _at(monkeypatch, now)
    run = thesis.check_theses(journal_dir=nothing_may_happen.lines, capture_dir=nothing_may_happen.capture)
    assert run.ran is False and reason in run.reason
    assert (run.names, run.checked, run.asks, run.cost_usd) == (0, 0, 0, 0.0)
    assert run.exit_code == thesis.EXIT_OK
    assert not nothing_may_happen.lines.exists() and not nothing_may_happen.capture.exists()
    assert thesis.check(now) == {"date": now.date().isoformat(), "run": False, "reason": run.reason}


def test_today_the_flag_is_off_and_nothing_can_run(nothing_may_happen):
    if date.today() < tc.START:
        assert thesis.check()["run"] is False
        assert thesis.check_theses(journal_dir=nothing_may_happen.lines,
                                   capture_dir=nothing_may_happen.capture).ran is False
        assert not nothing_may_happen.lines.exists()


def test_the_logger_waits_for_the_days_production_cycle(monkeypatch, wired):
    _cycle(wired, MONDAY.date() - timedelta(days=3), {"AAA": ["h"]})      # last Friday's cycle is not today's
    answer = thesis.check(MONDAY)
    assert answer["run"] is False and "no production cycle is journalled for 2027-04-05" in answer["reason"]
    run = _run(wired)
    assert run.ran is False and run.reason == answer["reason"]
    assert wired.endpoint.sent == [] and not wired.lines.exists()


def test_the_cli_check_and_an_off_run_ask_nothing_and_exit_0(monkeypatch, capsys, nothing_may_happen):
    monkeypatch.setattr(tc, "THESIS_CHECK_ENABLED", False)
    _at(monkeypatch, MONDAY)
    assert thesis.main(["--check"]) == 0
    assert json.loads(capsys.readouterr().out) == {
        "date": "2027-04-05", "run": False, "reason": "the flag THESIS_CHECK_ENABLED is off"}
    monkeypatch.setattr(tc, "JOURNAL_DIR", nothing_may_happen.lines)
    assert thesis.main(["--capture", str(nothing_may_happen.capture)]) == 0
    assert json.loads(capsys.readouterr().out)["ran"] is False
    assert not nothing_may_happen.lines.exists()


def test_a_run_started_after_the_cut_off_does_nothing(monkeypatch, wired):
    _cycle(wired, MONDAY.date(), {"AAA": ["h"]})
    _entry(wired, "AAA", MONDAY - timedelta(days=3))
    _at(monkeypatch, MONDAY.replace(hour=23, minute=20))
    run = _run(wired)
    assert run.ran is False and "too late in the UTC day" in run.reason
    assert wired.endpoint.sent == []


# --------------------------------------------------------------------------- #
# The logger reads and writes nothing it should not
# --------------------------------------------------------------------------- #


def test_the_logger_never_names_the_engine_the_broker_the_journal_or_the_context():
    assert_cannot_trade(SOURCE)


def test_the_logger_reads_no_credential_and_never_names_the_blend():
    assert_reads_no_credential_and_no_blend(SOURCE)


def test_the_logger_writes_no_file_itself_and_asks_the_production_model():
    """Its one writer is the vote's ``LineWriter`` on its own directory; every
    other file it opens, it opens to read. The model and its settings are production's."""
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    attributes = {n.attr for n in ast.walk(tree) if isinstance(n, ast.Attribute)}
    assert not attributes & {"write_text", "write_bytes", "unlink", "rmtree", "touch", "mkdir"}
    assert not [n for n in ast.walk(tree) if isinstance(n, ast.Name) and n.id == "open"]
    for call in ast.walk(tree):
        if isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute) and call.func.attr == "open":
            assert not call.args and {k.arg for k in call.keywords} == {"encoding"}
    pairs = {(n.value.id, n.attr) for n in ast.walk(tree)
             if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name)}
    for name in ("full_model_provider", "full_model_effort", "model_setup"):
        assert ("heartbeat", name) in pairs, name
    assert ("llm", "MODEL") in pairs and ("llm", "call_label") in pairs and ("model_io", "capture") in pairs


def test_a_run_writes_only_its_own_lines_and_its_model_calls(wired, tmp_path):
    _cycle(wired, MONDAY.date(), {"AAA": ["h"], "BBB": []})
    _entry(wired, "AAA", MONDAY - timedelta(days=3))
    before = {p for p in tmp_path.rglob("*") if p.is_file()}
    audit = wired.audit.read_bytes()
    _run(wired)
    after = {p for p in tmp_path.rglob("*") if p.is_file()}
    new = after - before
    assert new and all(p.is_relative_to(wired.lines) or p.is_relative_to(wired.capture) for p in new)
    assert wired.audit.read_bytes() == audit


def test_the_workers_and_the_budget_fit_a_week_of_held_names():
    assert thesis.WORKERS == cfg.FULL_MODEL_MAX_CONCURRENCY
    names = round(tc.ESTIMATED_WEEKLY_COST_USD / tc.ESTIMATED_COST_PER_CALL_USD)     # about 20
    assert names == 20
    assert math.ceil(names / thesis.WORKERS) * 212 <= thesis.RUN_BUDGET_SECONDS


# --------------------------------------------------------------------------- #
# The week's names
# --------------------------------------------------------------------------- #


def test_the_held_names_of_the_week_s_check_day_are_checked(wired):
    _cycle(wired, MONDAY.date(), {"AAA": ["Supplier raises guidance", "Upgrade at a big bank"], "BBB": []})
    _entry(wired, "AAA", datetime(2027, 4, 1, 15, 2, tzinfo=timezone.utc), rationale="Breakout above the 50-day.",
           key_factors=["50-day breakout", "analyst upgrade"])
    _entry(wired, "BBB", datetime(2027, 4, 2, 15, 3, tzinfo=timezone.utc), side="sell",
           rationale="Earnings miss and a guidance cut.")
    run = _run(wired)
    assert (run.ran, run.week, run.check_day, run.names, run.checked, run.failed) == (
        True, "2027-W14", MONDAY.date(), 2, 2, 0)
    assert run.exit_code == thesis.EXIT_OK and run.asks == 2
    assert run.cost_usd == pytest.approx(2 * CHEAP_USD)
    assert sorted(wired.endpoint.asked()) == ["AAA", "BBB"]     # XLE was answered, not held

    # One call each, production's model, effort and the fixed system prompt.
    for body in wired.endpoint.sent:
        assert body["model"] == heartbeat.MODEL and body["reasoning_effort"] == heartbeat.full_model_effort()
        assert body["messages"][0] == {"role": "system", "content": thesis.SYSTEM_PROMPT}
    aaa = wired.endpoint.user_prompt("AAA")
    for words in ("TICKER: AAA", "POSITION: long (bought)", "OPENED: 2027-04-01", "Breakout above the 50-day.",
                  "- 50-day breakout", "- analyst upgrade", "- Supplier raises guidance", "- Upgrade at a big bank"):
        assert words in aaa, words
    assert aaa.endswith("Respond with the JSON thesis check for AAA.")
    bbb = wired.endpoint.user_prompt("BBB")
    assert "POSITION: short (sold short)" in bbb and "TODAY'S HEADLINES:\nno headlines today" in bbb

    assert wired.month.name == "2027-04.log"
    lines = {line["ticker"]: line for line in _lines(wired)}
    for ticker, line in lines.items():
        assert set(line) == LINE_KEYS
        assert line["event"] == "thesis_check" and line["week"] == "2027-W14" and line["error"] is None
        assert line["verdict"] == "VALID" and line["reason"] == "The trend and the upgrade still stand."
        assert datetime.fromisoformat(line["ts_utc"]) == MONDAY
        assert line["asks"] == 1 and line["cost_usd"] == pytest.approx(CHEAP_USD, abs=1e-6)
        assert line["model_setup"] == heartbeat.model_setup()
        assert line["reasoning_effort"] == llm.configured_effort()
    assert lines["AAA"]["side"] == "long" and lines["BBB"]["side"] == "short"
    assert lines["AAA"]["entry"] == {"ts": "2027-04-01T15:02:00+00:00", "rationale": "Breakout above the 50-day.",
                                     "key_factors": ["50-day breakout", "analyst upgrade"], "bias": "BULLISH"}
    assert (lines["AAA"]["headline_count"], lines["BBB"]["headline_count"]) == (2, 0)


def test_failed_names_are_asked_again_later_in_the_week_while_still_held(monkeypatch, wired):
    monday = MONDAY.date()
    _cycle(wired, monday, {"AAA": ["h"], "BBB": ["h"], "EEE": ["h"]})
    for ticker in ("AAA", "BBB", "EEE"):
        _entry(wired, ticker, MONDAY - timedelta(days=4))
    wired.endpoint.script["BBB"] = [httpx.Response(400, text="no")]
    wired.endpoint.script["EEE"] = [httpx.Response(400, text="no")]
    first = _run(wired)
    assert (first.checked, first.failed) == (1, 2) and first.exit_code == thesis.EXIT_OK

    # The same day: nobody again.
    again = _run(wired)
    assert (again.names, again.asks) == (0, 0) and len(wired.endpoint.sent) == 3

    # Tuesday: EEE was sold, DDD was bought; only BBB is asked again.
    tuesday = MONDAY + timedelta(days=1)
    _cycle(wired, tuesday.date(), {"AAA": ["h"], "BBB": ["h2"], "DDD": ["h"]})
    _entry(wired, "DDD", MONDAY + timedelta(hours=1))
    _at(monkeypatch, tuesday)
    second = _run(wired)
    assert (second.check_day, second.names, second.checked) == (monday, 1, 1)
    assert wired.endpoint.asked()[3:] == ["BBB"]

    # Wednesday: everything held on Monday is done or gone.
    _cycle(wired, (tuesday + timedelta(days=1)).date(), {"AAA": ["h"], "BBB": ["h"], "DDD": ["h"]})
    _at(monkeypatch, tuesday + timedelta(days=1))
    third = _run(wired)
    assert third.ran is True and third.names == 0 and len(wired.endpoint.sent) == 4

    # Next Monday is a new week: its own check day, its own names.
    _cycle(wired, monday + timedelta(days=7), {"AAA": ["h"], "DDD": ["h"]})
    _at(monkeypatch, MONDAY + timedelta(days=7))
    fourth = _run(wired)
    assert (fourth.week, fourth.check_day, fourth.checked) == ("2027-W15", monday + timedelta(days=7), 2)
    # Names are checked four at a time, so lines of one run are written in the order the calls end: compare sorted.
    weeks = sorted((line["week"], line["ticker"], line["error"] is None) for line in _lines(wired))
    assert weeks == [("2027-W14", "AAA", True), ("2027-W14", "BBB", False), ("2027-W14", "BBB", True),
                     ("2027-W14", "EEE", False), ("2027-W15", "AAA", True), ("2027-W15", "DDD", True)]


def test_the_first_week_s_check_day_is_not_before_the_start(monkeypatch, wired):
    """2027-W13 runs from Monday 29 March; the logger starts on Thursday 1 April."""
    _cycle(wired, date(2027, 3, 29), {"OLD": ["h"]})
    _cycle(wired, date(2027, 4, 1), {"AAA": ["h"], "BBB": ["h"]})
    for ticker in ("OLD", "AAA", "BBB"):
        _entry(wired, ticker, datetime(2027, 3, 25, 15, tzinfo=timezone.utc))
    _at(monkeypatch, datetime(2027, 4, 1, 18, 30, tzinfo=timezone.utc))
    run = _run(wired)
    assert (run.week, run.check_day, run.checked) == ("2027-W13", date(2027, 4, 1), 2)
    assert sorted(wired.endpoint.asked()) == ["AAA", "BBB"]


# --------------------------------------------------------------------------- #
# The entry reasoning and the headlines
# --------------------------------------------------------------------------- #


def test_the_reasoning_is_the_latest_accepted_entry_on_record(wired):
    _cycle(wired, MONDAY.date(), {"AAA": ["h"], "BBB": ["h"], "CCC": ["h"]})
    _entry(wired, "AAA", datetime(2027, 3, 1, 15, tzinfo=timezone.utc), rationale="The first time it was bought.")
    _entry(wired, "AAA", datetime(2027, 4, 1, 15, tzinfo=timezone.utc), rationale="Bought again: a new breakout.")
    _entry(wired, "AAA", datetime(2027, 4, 2, 15, tzinfo=timezone.utc), status="REJECTED", rationale="Refused.")
    _entry(wired, "AAA", MONDAY + timedelta(hours=1), rationale="A record from after now.")
    _entry(wired, "BBB", datetime(2027, 4, 1, 15, tzinfo=timezone.utc), side="sell", rationale="Sold short.")
    _entry(wired, "CCC", datetime(2027, 4, 1, 15, tzinfo=timezone.utc), entry_price=None, rationale="No price.")
    with wired.audit.open("a", encoding="utf-8") as handle:
        handle.write("not json, but signal_processed\n")
        handle.write(json.dumps({"event": "position_managed", "action": {"ticker": "AAA"}}) + "\n")
    run = _run(wired)
    assert (run.checked, run.no_entry) == (2, 1)
    assert "Bought again: a new breakout." in wired.endpoint.user_prompt("AAA")
    assert "Sold short." in wired.endpoint.user_prompt("BBB")
    lines = {line["ticker"]: line for line in _lines(wired)}
    assert lines["AAA"]["entry"]["ts"] == "2027-04-01T15:00:00+00:00"
    assert lines["BBB"]["side"] == "short" and lines["BBB"]["entry"]["bias"] == "BEARISH"
    # No accepted entry with a price: the line says so, and nothing is asked.
    assert lines["CCC"]["error"] == thesis.NO_ENTRY and lines["CCC"]["verdict"] is None
    assert (lines["CCC"]["entry"], lines["CCC"]["side"], lines["CCC"]["asks"]) == (None, None, 0)
    assert "CCC" not in wired.endpoint.asked()


def test_the_audit_time_falls_back_to_the_log_clock(tmp_path):
    item = {"event": "signal_processed", "ts": "2027-04-01 15:02:03,456",
            "signal": {"bias": "BULLISH", "rationale": " r ", "key_factors": ["a", "", 3]},
            "result": {"status": "ACCEPTED", "ticker": "aaa", "side": "buy", "entry_price": 1.0, "stop_price": 0.9}}
    entry = thesis.entry_from_audit(item)
    assert entry.ticker == "AAA" and entry.at == datetime(2027, 4, 1, 15, 2, 3, 456000, tzinfo=timezone.utc)
    assert (entry.rationale, entry.key_factors, entry.side) == ("r", ("a",), "long")
    assert thesis.latest_entries(MONDAY, tmp_path / "no-audit-log") == {}


def test_the_headlines_are_today_s_latest_held_line_s(wired):
    _cycle(wired, MONDAY.date() - timedelta(days=0), {"AAA": ["an old headline"]}, hour=14)
    _cycle(wired, MONDAY.date(), {"AAA": ["a new headline", "another"]}, answered=(), hour=16)
    _entry(wired, "AAA", MONDAY - timedelta(days=3))
    _run(wired)
    prompt = wired.endpoint.user_prompt("AAA")
    assert "- a new headline\n- another" in prompt and "an old headline" not in prompt
    assert _lines(wired)[0]["headline_count"] == 2


# --------------------------------------------------------------------------- #
# The answer
# --------------------------------------------------------------------------- #


def test_a_verdict_outside_the_three_is_asked_once_more_then_a_failed_check(wired):
    _cycle(wired, MONDAY.date(), {"AAA": ["h"], "BBB": ["h"], "CCC": ["h"]})
    for ticker in ("AAA", "BBB", "CCC"):
        _entry(wired, ticker, MONDAY - timedelta(days=3))
    wired.endpoint.script["AAA"] = [_answer("AAA", "MAYBE"), _answer("AAA", "MAYBE")]
    wired.endpoint.script["BBB"] = [_answer("BBB", "UNSURE"), _answer("BBB", "BROKEN", "The guidance cut undid it.")]
    wired.endpoint.script["CCC"] = [_answer("XLE", "VALID")]
    run = _run(wired)
    assert (run.checked, run.failed, run.asks) == (1, 2, 5)
    lines = {line["ticker"]: line for line in _lines(wired)}
    assert lines["AAA"]["verdict"] is None and lines["AAA"]["error"].startswith("invalid model output")
    assert lines["AAA"]["asks"] == 2 and lines["AAA"]["cost_usd"] == pytest.approx(2 * CHEAP_USD, abs=1e-6)
    assert (lines["BBB"]["verdict"], lines["BBB"]["reason"], lines["BBB"]["asks"]) == (
        "BROKEN", "The guidance cut undid it.", 2)
    assert lines["CCC"]["error"] == "answered for XLE" and lines["CCC"]["verdict"] is None
    # The re-ask states the problem, as production's does.
    reask = [b for b in wired.endpoint.sent if _ticker_of(b) == "AAA"][1]
    assert llm.INVALID_VALUES_INSTRUCTION in reask["messages"][0]["content"]


def test_the_reason_is_kept_to_one_short_sentence(wired):
    _cycle(wired, MONDAY.date(), {"AAA": ["h"]})
    _entry(wired, "AAA", MONDAY - timedelta(days=3))
    wired.endpoint.script["AAA"] = [_answer("AAA", "WEAKENED", "x" * 1000)]
    _run(wired)
    (line,) = _lines(wired)
    assert line["verdict"] == "WEAKENED" and line["reason"] == "x" * tc.REASON_MAX_CHARS


def test_a_failed_call_is_a_failed_check_and_every_name_failing_exits_1(wired):
    _cycle(wired, MONDAY.date(), {"AAA": ["h"]})
    _entry(wired, "AAA", MONDAY - timedelta(days=3))
    wired.endpoint.script["AAA"] = [httpx.ReadTimeout("timed out"), httpx.ReadTimeout("timed out")]
    run = _run(wired)
    assert (run.checked, run.failed, run.asks) == (0, 1, 2) and run.exit_code == thesis.EXIT_FAILED
    (line,) = _lines(wired)
    assert "unreachable" in line["error"]
    # Two asks with no usage: each is charged the estimate.
    assert line["cost_usd"] == pytest.approx(2 * tc.ESTIMATED_COST_PER_CALL_USD)


def test_no_model_key_stops_before_anything_is_written(wired, monkeypatch):
    _cycle(wired, MONDAY.date(), {"AAA": ["h"]})

    def no_key():
        raise llm.LLMError("FULL_MODEL_API_KEY is empty")

    monkeypatch.setattr(heartbeat, "full_model_provider", no_key)
    run = _run(wired)
    assert run.error and run.exit_code == thesis.EXIT_FAILED and not wired.lines.exists()


# --------------------------------------------------------------------------- #
# The weekly cost cap
# --------------------------------------------------------------------------- #


def test_the_weekly_cap_stops_new_names_and_the_cli_exits_3(monkeypatch, capsys, wired):
    wired.endpoint.usage = DIME                                     # ten cents a check
    _cycle(wired, MONDAY.date(), {"AAA": ["h"], "BBB": ["h"], "CCC": ["h"]})
    for ticker in ("AAA", "BBB", "CCC"):
        _entry(wired, ticker, MONDAY - timedelta(days=3))
    monkeypatch.setattr(tc, "JOURNAL_DIR", wired.lines)
    monkeypatch.setattr(cfg, "MODEL_IO_DIR", wired.capture)
    monkeypatch.setattr(thesis, "WORKERS", 1)
    assert thesis.main(["--run-id", "555"]) == thesis.EXIT_CAP_REACHED
    summary = json.loads(capsys.readouterr().out)
    assert (summary["checked"], summary["not_asked"], summary["cap_reached"]) == (1, 2, True)
    assert summary["cap_stopped"] is True
    assert summary["cap_usd"] == tc.WEEKLY_COST_CAP_USD and summary["cost_usd"] == pytest.approx(0.10, abs=1e-4)
    assert sorted(wired.capture.rglob("*.jsonl"))[0].name.startswith("thesis-555-")
    # The names the cap stopped get one line each, saying so, with no call.
    lines = [json.loads(raw) for raw in month_file(wired.lines, MONDAY).read_text().splitlines()]
    stopped = [line for line in lines if line["error"] == thesis.NOT_ASKED_CAP]
    assert sorted(line["ticker"] for line in stopped) == ["BBB", "CCC"]
    assert all(line["asks"] == 0 and line["verdict"] is None for line in stopped)
    # Tuesday, the same week: those names wait for next week, nobody is asked, and the phone is not told again.
    _cycle(wired, (MONDAY + timedelta(days=1)).date(), {"AAA": ["h"], "BBB": ["h"], "CCC": ["h"]})
    _at(monkeypatch, MONDAY + timedelta(days=1))
    tuesday = _run(wired)
    assert tuesday.names == 0 and tuesday.asks == 0 and len(wired.endpoint.sent) == 1
    assert tuesday.cap_stopped is False and tuesday.exit_code == thesis.EXIT_OK
    assert len(month_file(wired.lines, MONDAY).read_text().splitlines()) == len(lines)   # no line repeated


def test_a_name_with_no_entry_record_gets_one_line_a_week(monkeypatch, wired):
    _cycle(wired, MONDAY.date(), {"AAA": ["h"]})
    run = _run(wired)
    assert (run.no_entry, run.asks) == (1, 0) and wired.endpoint.sent == []
    _cycle(wired, (MONDAY + timedelta(days=1)).date(), {"AAA": ["h"]})
    _at(monkeypatch, MONDAY + timedelta(days=1))
    tuesday = _run(wired)
    assert tuesday.names == 0 and tuesday.no_entry == 0
    lines = [json.loads(raw) for raw in month_file(wired.lines, MONDAY).read_text().splitlines()]
    assert [(line["ticker"], line["error"]) for line in lines] == [("AAA", thesis.NO_ENTRY)]
    assert thesis.NO_ENTRY == checks.NO_ENTRY and thesis.NOT_ASKED_CAP == checks.NOT_ASKED_CAP   # one spelling


def test_the_cap_counts_this_week_s_lines_only(wired):
    _cycle(wired, MONDAY.date(), {"AAA": ["h"]})
    _entry(wired, "AAA", MONDAY - timedelta(days=3))
    wired.lines.mkdir(parents=True)
    with month_file(wired.lines, MONDAY).open("w", encoding="utf-8") as handle:
        handle.write(json.dumps({"ts_utc": "2027-04-02T18:00:00+00:00", "event": "thesis_check", "week": "2027-W13",
                                 "ticker": "OLD", "cost_usd": 5.0, "error": None, "verdict": "VALID"}) + "\n")
    run = _run(wired)
    assert run.checked == 1 and run.cost_usd == pytest.approx(CHEAP_USD)
    seen = thesis.week_lines(wired.lines, "2027-W14", MONDAY.date())
    assert seen.spent_usd == pytest.approx(CHEAP_USD, abs=1e-6) and seen.done == frozenset({"AAA"})


# --------------------------------------------------------------------------- #
# The workflow's job
# --------------------------------------------------------------------------- #


def _workflow() -> dict:
    return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))


def _step(name: str) -> dict:
    return next(s for s in _workflow()["jobs"]["thesis"]["steps"] if s.get("name") == name)


THESIS_STEPS = [
    "Is a thesis check due?", "Check the theses", "Keep the thesis check's model calls as an artifact",
    "Commit the thesis check lines", "Tell the owner's phone the cost cap stopped the thesis check",
]


def test_the_thesis_job_runs_last_after_the_universe():
    jobs = _workflow()["jobs"]
    job = jobs["thesis"]
    assert job["needs"] == "score"
    # After the universe's job whether it passed or failed, never after a cancel: a cancel stops the spending.
    assert job["if"] == "${{ !cancelled() && github.event_name != 'pull_request' && !inputs.verify }}"
    assert job["permissions"] == {"contents": "write"}
    assert [s.get("name") for s in job["steps"] if s.get("name")] == ["Install dependencies", *THESIS_STEPS]
    assert [s.get("uses") for s in job["steps"][:2]] == [s.get("uses") for s in jobs["score"]["steps"][:2]]
    check = _step("Is a thesis check due?")
    assert "python -m orchestrator.thesis --check" in check["run"] and not check.get("env")
    names = [s.get("name") for s in job["steps"]]
    for step in job["steps"][names.index("Is a thesis check due?") + 1:]:
        assert "steps.check.outputs.run == 'yes'" in step["if"] or "steps.thesis.outputs" in step["if"], step["name"]


def test_the_thesis_step_gets_exactly_the_model_key():
    step = _step("Check the theses")
    score = next(s for s in _workflow()["jobs"]["score"]["steps"] if s.get("name") == "Score the universe")
    assert step["if"] == "steps.check.outputs.run == 'yes'"
    assert set(step["env"]) == {"FULL_MODEL_API_KEY"}         # it asks the full model by name: no other key
    for key in step["env"]:
        assert step["env"][key] == score["env"][key], key
    assert 'python -m orchestrator.thesis --run-id "$GITHUB_RUN_ID"' in step["run"]
    assert '"$status" = "3"' in step["run"] and 'echo "cap=yes" >> "$GITHUB_OUTPUT"' in step["run"]


def test_the_thesis_job_commits_its_lines_and_tells_the_phone_at_the_cap():
    commit = _step("Commit the thesis check lines")
    assert commit["if"] == "always() && steps.check.outputs.run == 'yes'"
    assert "git add -f logs/thesis_check/" in commit["run"] and "git pull --rebase" in commit["run"]
    artifact = _step("Keep the thesis check's model calls as an artifact")
    assert artifact["with"]["name"] == "model-io-thesis-${{ github.run_id }}-${{ github.run_attempt }}"
    assert artifact["continue-on-error"] is True
    alert = _step("Tell the owner's phone the cost cap stopped the thesis check")
    _is_a_safe_push(alert)
    assert alert["if"] == "always() && steps.thesis.outputs.cap == 'yes'"
    words = " ".join(re.findall(r'"([^"]*)"', re.search(r'"message": \((.*?)\),', alert["run"], re.S).group(1)))
    cap = f"${tc.WEEKLY_COST_CAP_USD:.2f}"
    assert cap == "$0.10" and cap in words and "weekly" in words
    assert re.findall(r"\d", words.replace(cap, "")) == []


def test_the_thesis_job_s_clock_outlasts_the_budget_and_the_last_calls():
    clock = _workflow()["jobs"]["thesis"]["timeout-minutes"]
    worst_call = llm.SCHEMA_ATTEMPTS * (llm.FULL_MODEL_TIMEOUT_SECONDS + llm.TRANSPORT_RETRY_TIMEOUT_SECONDS) / 60
    assert clock >= thesis.RUN_BUDGET_SECONDS / 60 + worst_call + 10
    assert clock <= 360
