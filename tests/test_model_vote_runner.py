"""The voting arm's runner: built now, off until 2026-12-22, never traded.

The owner's instruction of 4 Oct 2026, item 1: each answered production line
gets four more calls of the same model, with the same settings, re-sending
the archived input of that same call, and the five answers vote. This file
pins the flag to the pre-registration, the input to the archive (by its
SHA-256), the calls to production's call path, the line format to what
``analysis.vote`` reads, the timing (after production, before 23:15 UTC),
the cost cap and its alerts, the runner away from the engine, and the
workflow's job.

Offline throughout: the model is a scripted OpenAI-compatible endpoint
behind the real provider, so every ask goes through production's own
retries, re-asks and capture.
"""

from __future__ import annotations

import ast
import json
import math
import re
import threading
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace

import httpx
import pytest
import yaml

from analysis import vote as rule
from config import model_vote as mv
from config import settings as cfg
from config.journal_files import month_file
from config.market_calendar import is_trading_day
from orchestrator import heartbeat, journal, llm, model_io, vote
from orchestrator.llm import Completion, OpenAICompatibleProvider
from orchestrator.pricing import Usage
from tests.test_phone import _is_a_safe_push

ROOT = Path(__file__).resolve().parents[1]
PREREG = ROOT / "docs/horse-race-preregistration.md"
WORKFLOW = ROOT / ".github/workflows/shadow-universe.yml"
SOURCE = ROOT / "orchestrator/vote.py"

#: The vote's first day: a Tuesday, a trading day, at the universe's backup hour.
A_DAY_ON = datetime(2026, 12, 22, 18, 30, tzinfo=timezone.utc)

#: A production run's GitHub id, as the journal's ``run`` block carries it.
RUN = "37021453868"

#: The keys of the vote line (the build spec's format, read by ``analysis.vote.line_from``).
LINE_KEYS = {
    "ts_utc", "event", "ticker", "line_ts_utc", "run_id", "prompt_sha256", "model_setup",
    "reasoning_effort", "votes", "answer", "asks", "cost_usd", "error",
}


# --------------------------------------------------------------------------- #
# The flag and the pre-registration
# --------------------------------------------------------------------------- #

FLAG_PHRASE = "Voting arm `model_vote` (`MODEL_VOTE_ENABLED`): **{state}** until **"


def test_the_flag_is_the_one_the_pre_registration_registers():
    """The pattern of the screening flag and the shadow universe: the file
    says off or on and until when; the code's start date is that date; and
    the flag cannot be on before it. Fails until the pre-registration carries
    the phrase -- the file is amended first, the code follows."""
    text = " ".join(PREREG.read_text(encoding="utf-8").split())
    off, on = FLAG_PHRASE.format(state="off"), FLAG_PHRASE.format(state="on")
    assert off in text or on in text, (
        f"the pre-registration does not register the voting arm; it must say {off}{mv.START.isoformat()}**"
    )
    registered_off = off in text
    tail = text.split(off if registered_off else on, 1)[1]
    found = re.match(r"(\d{4}-\d{2}-\d{2})\*\*", tail)
    assert found, "the registered date must follow `until **` as YYYY-MM-DD"
    registered = date.fromisoformat(found.group(1))
    assert mv.START == registered, f"START is {mv.START}; the pre-registration registers {registered}"
    if registered_off:
        assert mv.MODEL_VOTE_ENABLED is False, (
            "MODEL_VOTE_ENABLED is on but the pre-registration says off; amend the file first"
        )
    if date.today() < registered:
        assert mv.MODEL_VOTE_ENABLED is False, (
            f"MODEL_VOTE_ENABLED is on before {registered}, the date the pre-registration names"
        )


def test_the_registered_settings():
    # The flag itself is pinned against the pre-registration's date above.
    assert mv.START == mv.REGISTRATION == date(2026, 12, 22)
    assert (mv.VOTES, mv.EXTRA_CALLS, mv.MIN_VOTES) == (5, 4, 3)
    assert (mv.DAILY_COST_CAP_USD, mv.DAILY_COST_WARN_USD, mv.ESTIMATED_DAILY_COST_USD) == (1.00, 0.80, 0.70)
    assert mv.ESTIMATED_DAILY_COST_USD < mv.DAILY_COST_WARN_USD < mv.DAILY_COST_CAP_USD
    assert mv.NO_NEW_NAME_AFTER_UTC.isoformat() == "23:15:00"
    assert is_trading_day(A_DAY_ON.date())                    # the first day is a day it runs
    # About 58 answered lines a day, four calls each, at the estimate: the owner's $0.70.
    assert vote.EXPECTED_LINES == 58
    assert vote.EXPECTED_LINES * mv.EXTRA_CALLS * mv.ESTIMATED_COST_PER_CALL_USD == pytest.approx(
        mv.ESTIMATED_DAILY_COST_USD, abs=0.01)


def test_the_lines_have_their_own_directory():
    # Compared with the literal: the suite points SIGNAL_JOURNAL_PATH at a temporary file.
    assert mv.JOURNAL_DIR == cfg.LOG_DIR / "model_vote"
    assert mv.JOURNAL_DIR not in (cfg.LOG_DIR / "journal", cfg.LOG_DIR / "shadow_universe", cfg.MODEL_IO_DIR)


# --------------------------------------------------------------------------- #
# A scripted endpoint behind the real provider, and production lines made by it
# --------------------------------------------------------------------------- #

#: Measured tokens of one answer: $0.00105 at gpt-oss-120b's $0.05 / $0.45 per million.
CHEAP = {"prompt_tokens": 3000, "completion_tokens": 2000}
CHEAP_USD = Usage(model=llm.MODEL, input_tokens=3000, output_tokens=2000).cost_usd
#: Ten cents an ask, and thirty.
DIME = {"prompt_tokens": 0, "completion_tokens": 222_223}
THIRTY_CENTS = {"prompt_tokens": 0, "completion_tokens": 666_667}


def _ticker_of(body: dict) -> str:
    return re.search(r"Respond with the JSON signal for (\S+)\.$", body["messages"][1]["content"]).group(1)


def _signal(ticker: str, bias: str = "BULLISH", conviction: float = 0.6) -> dict:
    return {
        "ticker": ticker, "bias": bias, "conviction": conviction,
        "rationale": f"{ticker}: steady climb and an analyst upgrade",
        "news_score": 0.2, "technical_score": 0.5, "fundamental_score": 0.1,
        "analyst_score": 0.3, "insider_score": -0.1, "key_factors": ["trend", "upgrade"],
    }


class Endpoint:
    """An OpenAI-compatible endpoint: per ticker, a script of steps, then a default answer.

    A step is an exception to raise (a timeout), an ``httpx.Response``, a
    signal dict, or a text to answer with. Records every body it was sent.
    """

    def __init__(self) -> None:
        self.script: dict[str, list] = {}
        self.answers: dict[str, dict] = {}
        self.usage = dict(CHEAP)
        self.sent: list[dict] = []
        self._lock = threading.Lock()

    def reply(self, content: str) -> httpx.Response:
        return httpx.Response(200, json={"choices": [{"message": {"content": content}}], "usage": self.usage})

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
        if isinstance(step, dict):
            return self.reply(json.dumps(step))
        if isinstance(step, str):
            return self.reply(step)
        return self.reply(json.dumps(_signal(ticker, **self.answers.get(ticker, {}))))

    def asked(self) -> list[str]:
        return [_ticker_of(body) for body in self.sent]


def _user_prompt(ticker: str) -> str:
    return f"TICKER: {ticker}\nTECHNICALS: up\n" + heartbeat.USER_PROMPT_TAIL.format(ticker=ticker)


def _context(ticker: str, *, insiders: bool = True) -> dict:
    return {"ticker": ticker, "headlines": ["a headline"], "technicals": {"rsi": 55.0},
            "analysts": {"rating": "buy"}, "insiders": {"net": 1} if insiders else None}


@pytest.fixture
def wired(monkeypatch, tmp_path):
    """The flag on, the vote's first day, the real provider over the scripted
    endpoint, production's order path, journal and context booby-trapped."""
    monkeypatch.setattr(mv, "MODEL_VOTE_ENABLED", True)
    monkeypatch.setattr(vote, "utc_now", lambda: A_DAY_ON)
    endpoint = Endpoint()
    provider = OpenAICompatibleProvider(
        "https://api.example.test/v1/openai", heartbeat.MODEL, api_key="plain-test-key",
        client=httpx.Client(transport=httpx.MockTransport(endpoint)), sleep=lambda _: None,
        timeout=llm.FULL_MODEL_TIMEOUT_SECONDS,
    )
    monkeypatch.setattr(heartbeat, "full_model_provider", lambda: provider)

    def never(*_args, **_kwargs):
        raise AssertionError("the vote reached the engine, the production journal or the context gather")

    for name in ("post_signal", "build_dispatcher", "judge_answer", "process_ticker", "prepare_ticker",
                 "apply_screen", "journal_context_failure", "build_context", "fetch_news"):
        monkeypatch.setattr(heartbeat, name, never)
    monkeypatch.setattr(journal, "record", never)
    from orchestrator import context
    monkeypatch.setattr(context, "gather", never)

    journal_dir = tmp_path / "journal"
    monkeypatch.setattr(cfg, "SIGNAL_JOURNAL_PATH", journal_dir)
    votes = tmp_path / "model_vote"
    return SimpleNamespace(endpoint=endpoint, provider=provider, journal=journal_dir, votes=votes,
                           archive=tmp_path / "downloaded", capture=tmp_path / "model_io",
                           month=month_file(votes, A_DAY_ON), stamps=iter(range(10_000)))


def _production_call(wired, ticker: str, run_id: str) -> list[dict]:
    """Ask the endpoint the way the cycle does, under a capture like the heartbeat's.

    The capture goes where the workflow downloads the production artifact
    (``model-io-<run>-<attempt>/...``); returns the refs the line carries.
    """
    with model_io.capture(wired.archive / f"model-io-{run_id}-1", run_id=run_id):
        with llm.call_label(ticker):
            heartbeat.call_llm(heartbeat.system_prompt_for(ticker), _user_prompt(ticker), heartbeat.SIGNAL_JSON_SCHEMA)
        refs = model_io.take(ticker)
    wired.endpoint.sent.clear()
    return refs


def _add_line(wired, ticker: str, *, when: datetime | None = None, run_id: str | None = RUN,
              bias: str = "BULLISH", conviction: float = 0.6, held: bool = False, answered: bool = True,
              error: str | None = None, insiders: bool = True, calls: list[dict] | None = None) -> dict:
    """A production journal line for ``ticker``, its first ask archived under ``run_id``."""
    when = when or A_DAY_ON.replace(hour=15, minute=0) + timedelta(seconds=next(wired.stamps))
    if calls is None:
        calls = [] if held or not answered else _production_call(wired, ticker, run_id or "local")
    signal = None if held or not answered else {**_signal(ticker, bias, conviction)}
    if signal is not None and not insiders:
        signal["insider_score"] = None
    payload = {
        "ts_utc": when.isoformat(), "ticker": ticker, "context": _context(ticker, insiders=insiders),
        "signal": signal, "error": error, "blend": {"composite": 0.25, "applied": {"technical_score": 1.0}},
        "held": held, "event": "signal_generated",
    }
    if run_id is not None:
        payload["run"] = {"run_id": run_id}
    if calls:
        payload["model_calls"] = calls
    path = month_file(wired.journal, when)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload) + "\n")
    return payload


def _lines(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _run(wired, **kwargs) -> vote.VoteRun:
    kwargs.setdefault("model_io_dir", wired.archive)
    kwargs.setdefault("journal_dir", wired.votes)
    kwargs.setdefault("capture_dir", wired.capture)
    return vote.vote_today(**kwargs)


def _archived(wired) -> dict[str, dict]:
    return vote.archived_calls(wired.archive)


# --------------------------------------------------------------------------- #
# The read-only body builder (orchestrator/llm.py)
# --------------------------------------------------------------------------- #


class _Server:
    def __init__(self, *contents: str) -> None:
        self.contents = list(contents)
        self.sent: list[dict] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.sent.append(json.loads(request.content))
        return httpx.Response(200, json={"choices": [{"message": {"content": self.contents.pop(0)}}],
                                         "usage": CHEAP})


@pytest.mark.parametrize("kwargs", [
    {"model": "openai/gpt-oss-120b", "effort": "high"},
    {"effort": "medium"},
    {},
    {"reasoning": False},
])
def test_request_body_is_the_first_ask_and_sends_nothing(kwargs):
    server = _Server(json.dumps(_signal("XLE")))
    provider = OpenAICompatibleProvider("http://local/v1", "openai/gpt-oss-120b", api_key="k",
                                        client=httpx.Client(transport=httpx.MockTransport(server)),
                                        sleep=lambda _: None)
    args = ("the system prompt", "the user prompt", heartbeat.SIGNAL_JSON_SCHEMA)
    built = provider.request_body(*args, **kwargs)
    assert server.sent == []                                  # read-only: nothing was asked
    provider.complete_detailed(*args, **kwargs)
    assert server.sent == [built]


def test_call_llm_s_arguments_rebuild_the_hash_the_capture_records(tmp_path, monkeypatch):
    server = _Server(json.dumps(_signal("XLE")))
    provider = OpenAICompatibleProvider("http://local/v1", heartbeat.MODEL, api_key="k",
                                        client=httpx.Client(transport=httpx.MockTransport(server)),
                                        sleep=lambda _: None)
    monkeypatch.setattr(heartbeat, "full_model_provider", lambda: provider)
    with model_io.capture(tmp_path / "io", run_id="1"):
        with llm.call_label("XLE"):
            heartbeat.call_llm("a system prompt", _user_prompt("XLE"), heartbeat.SIGNAL_JSON_SCHEMA)
        (ref,) = model_io.take("XLE")
        captured = json.loads(model_io.current_path().read_text(encoding="utf-8"))
    rebuilt = provider.request_body("a system prompt", _user_prompt("XLE"), heartbeat.SIGNAL_JSON_SCHEMA,
                                    model=llm.MODEL, effort=heartbeat.full_model_effort())
    digest = model_io.sha256_text(model_io.canonical(rebuilt))
    assert digest == captured["prompt_sha256"] == ref["prompt_sha256"]
    assert json.loads(captured["request"]) == rebuilt == server.sent[0]


# --------------------------------------------------------------------------- #
# The runner stays off when it should
# --------------------------------------------------------------------------- #


@pytest.fixture
def nothing_may_happen(monkeypatch, tmp_path):
    """Any model call, any context, or any file would be a failure."""
    def refuse(*_args, **_kwargs):
        raise AssertionError("the vote did something on a day it must not run")

    for name in ("build_context", "call_llm", "full_model_provider", "model_setup", "full_model_effort"):
        monkeypatch.setattr(heartbeat, name, refuse)
    monkeypatch.setattr(vote, "production_lines", refuse)
    monkeypatch.setattr(vote, "archived_calls", refuse)
    return SimpleNamespace(votes=tmp_path / "model_vote", capture=tmp_path / "capture",
                           archive=tmp_path / "downloaded")


def _nothing_written(paths) -> None:
    assert not paths.votes.exists() and not paths.capture.exists()


@pytest.mark.parametrize("enabled, now, reason", [
    (False, A_DAY_ON, "the flag MODEL_VOTE_ENABLED is off"),
    (True, datetime(2026, 12, 21, 18, 30, tzinfo=timezone.utc), "before the start date 2026-12-22"),
    (True, datetime(2026, 12, 25, 18, 30, tzinfo=timezone.utc), "not a trading day"),   # Christmas
    (True, datetime(2026, 12, 26, 18, 30, tzinfo=timezone.utc), "not a trading day"),   # a Saturday
])
def test_the_vote_does_nothing_when_off_early_or_closed(monkeypatch, nothing_may_happen, enabled, now, reason):
    monkeypatch.setattr(mv, "MODEL_VOTE_ENABLED", enabled)
    monkeypatch.setattr(vote, "utc_now", lambda: now)
    run = vote.vote_today(model_io_dir=nothing_may_happen.archive, journal_dir=nothing_may_happen.votes,
                          capture_dir=nothing_may_happen.capture)
    assert run.ran is False and reason in run.reason
    assert (run.calls, run.asks, run.voted, run.cost_usd) == (0, 0, 0, 0.0)
    assert run.exit_code == vote.EXIT_OK
    _nothing_written(nothing_may_happen)
    assert vote.check(now) == {"date": now.date().isoformat(), "run": False, "reason": run.reason, "runs": []}


def test_today_the_flag_is_off_and_nothing_can_run(nothing_may_happen):
    """The real clock and the real flag: before 2026-12-22 the check says no, whatever else is true."""
    if date.today() < mv.START:
        assert vote.check()["run"] is False
        assert vote.vote_today(journal_dir=nothing_may_happen.votes,
                               capture_dir=nothing_may_happen.capture).ran is False
        _nothing_written(nothing_may_happen)


def test_the_vote_waits_for_the_days_production_cycle(monkeypatch, tmp_path, nothing_may_happen):
    """So the vote never asks the model provider beside production, and no catch-up cycle starts once it runs."""
    monkeypatch.setattr(mv, "MODEL_VOTE_ENABLED", True)
    monkeypatch.setattr(vote, "utc_now", lambda: A_DAY_ON)
    yesterday = A_DAY_ON - timedelta(days=1)
    directory = tmp_path / "journal"
    path = month_file(directory, yesterday)
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps({"ts_utc": yesterday.isoformat(), "ticker": "XLE", "signal": None, "error": "x"})
                    + "\n", encoding="utf-8")
    monkeypatch.setattr(cfg, "SIGNAL_JOURNAL_PATH", directory)
    answer = vote.check(A_DAY_ON)
    assert answer["run"] is False and "no production cycle is journalled for 2026-12-22" in answer["reason"]
    run = vote.vote_today(model_io_dir=nothing_may_happen.archive, journal_dir=nothing_may_happen.votes,
                          capture_dir=nothing_may_happen.capture)
    assert run.ran is False and run.reason == answer["reason"] and run.exit_code == vote.EXIT_OK
    _nothing_written(nothing_may_happen)
    monkeypatch.setattr(cfg, "SIGNAL_JOURNAL_PATH", tmp_path / "no-journal-at-all")
    assert vote.production_ran(A_DAY_ON.date()) is False


def test_the_cli_check_and_an_off_run_ask_nothing_and_exit_0(monkeypatch, capsys, nothing_may_happen):
    monkeypatch.setattr(mv, "MODEL_VOTE_ENABLED", False)
    monkeypatch.setattr(vote, "utc_now", lambda: A_DAY_ON)
    assert vote.main(["--check"]) == 0
    assert json.loads(capsys.readouterr().out) == {
        "date": "2026-12-22", "run": False, "reason": "the flag MODEL_VOTE_ENABLED is off", "runs": []}
    monkeypatch.setattr(mv, "JOURNAL_DIR", nothing_may_happen.votes)
    assert vote.main(["--model-io", str(nothing_may_happen.archive), "--capture",
                      str(nothing_may_happen.capture)]) == 0
    summary = json.loads(capsys.readouterr().out)
    assert summary["ran"] is False and summary["calls"] == 0
    _nothing_written(nothing_may_happen)


def test_a_run_started_after_the_cut_off_does_nothing_and_says_why(monkeypatch, wired):
    _add_line(wired, "XLE")
    late = A_DAY_ON.replace(hour=23, minute=20)
    monkeypatch.setattr(vote, "utc_now", lambda: late)
    run = _run(wired)
    assert run.ran is False and "too late in the UTC day" in run.reason
    assert wired.endpoint.sent == [] and not wired.votes.exists()
    assert vote.check(late)["run"] is False
    assert vote.check(late.replace(minute=14))["run"] is True


# --------------------------------------------------------------------------- #
# The runner reuses production's call path and cannot reach the engine
# --------------------------------------------------------------------------- #

#: Names that would mean the module can trade, writes the production journal,
#: reads the live price or gathers context: none may appear in it.
FORBIDDEN_NAMES = {
    "post_signal", "build_dispatcher", "Dispatcher", "DirectDispatcher", "dispatch",
    "dispatcher", "judge_answer", "process_ticker", "prepare_ticker", "apply_screen",
    "screen_signal", "run_cycle", "run_batched_cycle", "manage_positions",
    "protect_positions", "open_tickers", "is_market_open", "ExecutionEngine",
    "PositionManager", "AlpacaPaperBroker", "TradingClient", "submit_order",
    "submit_bracket_order", "record", "read_live", "note_cycle", "live_price",
    "flows", "build_context", "fetch_news", "gather", "universe_records", "TickerContext",
}

FORBIDDEN_MODULES = (
    "orchestrator.live_price", "orchestrator.dispatch", "orchestrator.digest", "orchestrator.flows",
    "orchestrator.news", "orchestrator.universe_news", "orchestrator.context", "orchestrator.sources",
    "orchestrator.journal", "orchestrator.universe", "app", "alpaca", "store", "anthropic", "openai",
)


def _tree(source: Path = SOURCE) -> ast.Module:
    return ast.parse(source.read_text(encoding="utf-8"))


def _imported(tree: ast.Module) -> set[str]:
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names |= {alias.name for alias in node.names}
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module)
            names |= {f"{node.module}.{alias.name}" for alias in node.names}
    return names


def _used(tree: ast.Module) -> set[str]:
    return ({n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}
            | {n.attr for n in ast.walk(tree) if isinstance(n, ast.Attribute)}
            | {alias.asname or alias.name for n in ast.walk(tree)
               if isinstance(n, (ast.Import, ast.ImportFrom)) for alias in n.names})


def assert_cannot_trade(source: Path) -> None:
    tree = _tree(source)
    used = _used(tree)
    assert not used & FORBIDDEN_NAMES, sorted(used & FORBIDDEN_NAMES)
    bad = sorted(name for name in _imported(tree)
                 for module in FORBIDDEN_MODULES if name == module or name.startswith(module + "."))
    assert not bad, bad


def assert_reads_no_credential_and_no_blend(source: Path) -> None:
    """The CI greps that cover every orchestrator module ("Market context carries no credentials",
    "The learned blend runs in shadow"), run here on every line, comments and docstrings included."""
    text = source.read_text(encoding="utf-8")
    credential = re.compile(r"(get_settings|os\.environ|getenv|\bsettings\.|\.[A-Za-z_]*(secret|api_key|_token|password)\b)")
    assert not [line for line in text.splitlines() if credential.search(line)]
    assert not re.search(r"(from orchestrator import [^#\n]*\blive_price\b|orchestrator\.live_price|import live_price)", text)
    assert "composite" not in text and "blend_signal" not in text and "blend_record" not in text


def test_the_voter_never_names_the_engine_the_broker_the_journal_or_the_context():
    assert_cannot_trade(SOURCE)


def test_the_voter_reads_no_credential_and_never_names_the_blend():
    assert_reads_no_credential_and_no_blend(SOURCE)


def test_the_voter_calls_the_production_functions():
    """Same model, settings and call path: the steps are heartbeat's own, not copies."""
    tree = _tree()
    attributes = {(n.value.id, n.attr) for n in ast.walk(tree)
                  if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name)}
    for name in ("call_llm", "parse_signal", "scores_without_a_source", "full_model_provider",
                 "full_model_effort", "model_setup", "SIGNAL_JSON_SCHEMA"):
        assert ("heartbeat", name) in attributes, name
    assert ("llm", "call_label") in attributes and ("model_io", "capture") in attributes
    assert ("rule", "aggregate") in attributes and ("rule", "line_from") in attributes


def test_the_workers_and_the_budget_are_production_s_and_fit_a_day():
    assert vote.WORKERS == cfg.FULL_MODEL_MAX_CONCURRENCY
    # 146 seconds: production's median answered call at high effort (llm.py,
    # 23 and 25 Sep 2026); 212: the universe's slowest measured pace a name.
    for seconds in (146, 212):
        assert math.ceil(vote.EXPECTED_LINES * mv.EXTRA_CALLS / vote.WORKERS) * seconds <= vote.RUN_BUDGET_SECONDS


# --------------------------------------------------------------------------- #
# Voting
# --------------------------------------------------------------------------- #


def test_writes_the_documented_line_for_every_answered_line(wired):
    first = _add_line(wired, "XLE")
    second = _add_line(wired, "GLD", bias="BEARISH", conviction=0.5)
    wired.endpoint.answers["GLD"] = {"bias": "BEARISH", "conviction": 0.4}
    run = _run(wired)
    assert (run.ran, run.lines, run.voted, run.answered, run.dropped, run.not_voted) == (True, 2, 2, 2, 0, 0)
    assert (run.calls, run.asks, run.failed_calls) == (8, 8, 0)
    assert run.exit_code == vote.EXIT_OK and run.cap_reached is False
    assert run.cost_usd == pytest.approx(8 * CHEAP_USD)

    # Four calls a line, each re-sending exactly the archived first ask.
    archived = _archived(wired)
    for payload in (first, second):
        body = json.loads(archived[payload["model_calls"][0]["call_id"]]["request"])
        sent = [b for b in wired.endpoint.sent if _ticker_of(b) == payload["ticker"]]
        assert len(sent) == mv.EXTRA_CALLS and all(b == body for b in sent)
    # Under their own labels, captured beside production's calls, never with them.
    (capture,) = sorted(wired.capture.rglob("*.jsonl"))
    assert capture.name.startswith("vote-local-")
    labels = sorted(json.loads(line)["ticker"] for line in capture.read_text().splitlines())
    assert labels == sorted(f"{t} vote {n}" for t in ("XLE", "GLD") for n in range(2, 6))

    assert wired.month.name == "2026-12.log"
    lines = {line["ticker"]: line for line in _lines(wired.month)}
    for payload in (first, second):
        line = lines[payload["ticker"]]
        assert set(line) == LINE_KEYS
        assert line["event"] == "model_vote" and line["error"] is None
        assert line["line_ts_utc"] == payload["ts_utc"] and line["run_id"] == RUN
        assert line["prompt_sha256"] == payload["model_calls"][0]["prompt_sha256"]
        assert datetime.fromisoformat(line["ts_utc"]) == A_DAY_ON
        assert line["model_setup"] == heartbeat.model_setup()
        assert line["reasoning_effort"] == llm.configured_effort()
        assert [v["vote"] for v in line["votes"]] == [1, 2, 3, 4, 5]
        assert line["votes"][0] == {"vote": 1, "source": "production", "bias": payload["signal"]["bias"],
                                    "conviction": payload["signal"]["conviction"],
                                    "scores": {k: payload["signal"][k] for k in rule.SCORE_FIELDS}, "error": None}
        for extra in line["votes"][1:]:
            assert extra["error"] is None and extra["asks"] == 1
            assert extra["cost_usd"] == pytest.approx(CHEAP_USD, abs=1e-6)
            assert set(extra["scores"]) == set(rule.SCORE_FIELDS)
        assert (line["asks"], line["cost_usd"]) == (4, pytest.approx(4 * CHEAP_USD, abs=1e-6))
    assert lines["XLE"]["answer"] == {"side": "LONG", "bias": "BULLISH", "conviction": pytest.approx(0.6),
                                      "agree": 5, "successful": 5}
    # GLD: five BEARISH votes, 0.5 and four of 0.4: conviction = 5/5 x 0.42.
    assert lines["GLD"]["answer"]["side"] == "SHORT"
    assert lines["GLD"]["answer"]["conviction"] == pytest.approx(0.42)


def test_the_line_is_what_analysis_vote_reads_and_its_answer_is_the_rule_s(wired):
    payload = _add_line(wired, "XLE")
    # Two of the four calls say NEUTRAL: production and two BULLISH are 3 of 5.
    wired.endpoint.script["XLE"] = [_signal("XLE", "NEUTRAL", 0.2), _signal("XLE", "NEUTRAL", 0.1),
                                    _signal("XLE", "BULLISH", 0.5), _signal("XLE", "BULLISH", 0.7)]
    _run(wired, workers=1)
    (written,) = _lines(wired.month)
    read = rule.read_lines(wired.month.read_text(encoding="utf-8").splitlines())
    key = ("XLE", datetime.fromisoformat(payload["ts_utc"]))
    assert list(read) == [key] and rule.read_votes(wired.votes) == read
    line = read[key]
    assert line.day == A_DAY_ON.date() and line.error is None and len(line.votes) == 5
    assert (line.asks, line.cost_usd) == (4, pytest.approx(4 * CHEAP_USD, abs=1e-6))
    answer = rule.aggregate(line.votes)
    assert line.answer == answer
    assert written["answer"] == answer.as_dict()
    assert (answer.side, answer.agree, answer.successful) == ("LONG", 3, 5)
    assert answer.conviction == pytest.approx(3 / 5 * (0.6 + 0.5 + 0.7) / 3)
    assert rule.counters(read, A_DAY_ON.date()) == {"lines": 1, "answered": 1, "dropped": 0, "not_voted": 0,
                                                     "not_asked": 0, "missing": 0, "extra_calls": 4,
                                                     "failed_calls": 0}


def test_fewer_than_three_successful_votes_is_no_answer(wired):
    _add_line(wired, "XLE")
    _add_line(wired, "GLD")
    def refused():                                          # not asked again: one ask, one failed vote
        return httpx.Response(400, text="bad request")

    wired.endpoint.script["XLE"] = [refused(), refused(), refused()]      # 2 of 5 succeed
    wired.endpoint.script["GLD"] = [refused(), refused()]                 # 3 of 5 succeed
    run = _run(wired)
    assert (run.voted, run.answered, run.dropped, run.failed_calls, run.calls) == (2, 1, 1, 5, 8)
    assert run.exit_code == vote.EXIT_OK
    lines = {line["ticker"]: line for line in _lines(wired.month)}
    assert lines["XLE"]["answer"] is None and lines["XLE"]["error"] is None
    failed = [v for v in lines["XLE"]["votes"] if v["error"]]
    assert len(failed) == 3 and all("HTTP 400" in v["error"] for v in failed)
    assert all(v["bias"] is None and v["conviction"] is None for v in failed)
    assert lines["GLD"]["answer"]["successful"] == 3 and lines["GLD"]["answer"]["side"] == "LONG"
    assert lines["GLD"]["answer"]["conviction"] == pytest.approx(3 / 5 * 0.6)
    read = rule.read_votes(wired.votes)
    assert rule.counters(read, A_DAY_ON.date())["dropped"] == 1
    assert len(rule.answers(read)) == 1


def test_a_vote_for_another_ticker_or_out_of_bounds_fails(wired):
    _add_line(wired, "XLE")
    wired.endpoint.script["XLE"] = [_signal("GLD"), "this is not JSON", "still not JSON",
                                    {**_signal("XLE"), "conviction": 1.5}, {**_signal("XLE"), "conviction": 2.0}]
    run = _run(wired, workers=1)
    (line,) = _lines(wired.month)
    errors = [v["error"] for v in line["votes"][1:]]
    assert errors[0] == "answered for GLD"
    assert errors[1].startswith("model returned non-JSON output")     # asked twice, prose both times
    assert errors[2].startswith("invalid LLM output")                 # asked twice, out of bounds both times
    assert errors[3] is None
    assert run.failed_calls == 3 and line["answer"] is None           # 2 of 5 succeeded
    assert line["asks"] == 6


def test_every_ask_is_charged_a_re_ask_and_a_timeout_included(wired):
    _add_line(wired, "XLE")
    wired.endpoint.script["XLE"] = [
        "I think XLE is fine.", _signal("XLE"),                    # off-schema, then the re-ask
        httpx.ReadTimeout("timed out"), _signal("XLE"),            # a timeout, then the retry
    ]
    run = _run(wired, workers=1)
    (line,) = _lines(wired.month)
    # Six asks: five answered with usage, one timed out with none (charged the estimate).
    expected = 5 * CHEAP_USD + mv.ESTIMATED_COST_PER_CALL_USD
    assert (run.calls, run.asks, line["asks"]) == (4, 6, 6)
    assert [v["asks"] for v in line["votes"][1:]] == [2, 2, 1, 1]
    assert line["cost_usd"] == pytest.approx(expected, abs=1e-6)
    assert run.cost_usd == pytest.approx(expected)
    assert line["answer"]["successful"] == 5
    # A re-run the same day reads the cost back from the line.
    assert vote.day_votes(wired.votes, A_DAY_ON.date()).spent_usd == pytest.approx(expected, abs=1e-5)


def test_two_lines_of_one_ticker_today_are_each_voted_and_charged_their_own_asks(wired):
    """A second cycle by hand: two answered XLE lines on one day. Each call has a label of its own."""
    _add_line(wired, "XLE")
    _add_line(wired, "XLE", conviction=0.4)
    run = _run(wired, workers=4)
    assert (run.voted, run.calls, run.asks) == (2, 8, 8)
    lines = _lines(wired.month)
    assert [line["asks"] for line in lines] == [4, 4]
    assert run.cost_usd == pytest.approx(8 * CHEAP_USD)
    labels = sorted(json.loads(line)["ticker"] for path in wired.capture.rglob("*.jsonl")
                    for line in path.read_text().splitlines())
    assert labels == sorted([f"XLE vote {n}" for n in range(2, 6)] + [f"XLE (2) vote {n}" for n in range(2, 6)])
    assert len(rule.read_votes(wired.votes)) == 2


def test_scores_with_no_source_on_the_production_line_are_nulled_in_the_votes(wired):
    _add_line(wired, "XLE", insiders=False)
    _run(wired)
    (line,) = _lines(wired.month)
    for extra in line["votes"][1:]:
        assert extra["scores"]["insider_score"] is None
        assert extra["scores"]["analyst_score"] == 0.3


def test_held_unanswered_old_and_already_voted_lines_are_not_voted(wired):
    _add_line(wired, "GLD", held=True)
    _add_line(wired, "TLT", answered=False, error="https://api.deepinfra.com returned HTTP 500")
    _add_line(wired, "SLV", error="answered for GLD")
    _add_line(wired, "USO", when=A_DAY_ON - timedelta(days=1))
    _add_line(wired, "XLE")
    run = _run(wired)
    assert (run.lines, run.voted) == (1, 1)
    assert set(wired.endpoint.asked()) == {"XLE"}
    assert [line["ticker"] for line in _lines(wired.month)] == ["XLE"]
    again = _run(wired)
    assert (again.lines, again.already_voted, again.calls) == (0, 1, 0)
    assert again.exit_code == vote.EXIT_OK
    assert len(wired.endpoint.sent) == mv.EXTRA_CALLS and len(_lines(wired.month)) == 1
    assert again.cost_usd == pytest.approx(4 * CHEAP_USD, abs=1e-5)   # the day's total, read back


def test_the_check_names_the_production_runs_still_to_vote(wired):
    _add_line(wired, "XLE", run_id="222")
    _add_line(wired, "GLD", run_id="111")
    _add_line(wired, "TLT", run_id="111")
    _add_line(wired, "SLV", run_id="not-a-number")
    _add_line(wired, "USO", run_id=None)
    assert vote.check(A_DAY_ON, journal_dir=wired.votes) == {"date": "2026-12-22", "run": True, "reason": None,
                                                            "runs": ["111", "222"]}
    _run(wired)
    assert vote.check(A_DAY_ON, journal_dir=wired.votes)["runs"] == []


# --------------------------------------------------------------------------- #
# The archived input: missing, or not what production sends today
# --------------------------------------------------------------------------- #


def test_a_missing_archive_writes_the_reason_and_asks_nothing(wired):
    _add_line(wired, "XLE")                                        # archived
    _add_line(wired, "GLD", calls=[{"call_id": "f" * 32, "prompt_sha256": "0" * 64, "answer_sha256": None}])
    _add_line(wired, "TLT", calls=[])                              # no call ids on the line
    run = _run(wired)
    assert (run.voted, run.not_voted) == (1, 2)
    assert set(wired.endpoint.asked()) == {"XLE"}
    lines = {line["ticker"]: line for line in _lines(wired.month)}
    for ticker in ("GLD", "TLT"):
        line = lines[ticker]
        assert line["error"] == vote.NO_ARCHIVE
        assert [v["vote"] for v in line["votes"]] == [1] and line["answer"] is None
        assert (line["asks"], line["cost_usd"]) == (0, 0.0)
    read = rule.read_votes(wired.votes)
    assert rule.counters(read, A_DAY_ON.date())["not_voted"] == 2
    # Final: a second run votes neither again.
    assert _run(wired).lines == 0


def test_an_archive_that_does_not_match_its_hash_or_was_withheld_is_no_archive(wired):
    payload = _add_line(wired, "XLE")
    _add_line(wired, "GLD")
    _add_line(wired, "TLT")
    for path in sorted(wired.archive.rglob("*.jsonl")):
        items = _lines(path)
        for item in items:
            if item["ticker"] == "XLE":      # a copy whose body is not the one the journal hashed
                item["request"] = item["request"].replace("TECHNICALS: up", "TECHNICALS: down")
            elif item["ticker"] == "GLD":    # withheld at capture: hashes kept, bodies dropped
                item.update(model_io.withhold(item, "a test"))
            else:                            # the right body, but not the line's first ask
                item["kind"] = "re-ask after an off-schema answer"
        path.write_text("\n".join(json.dumps(item) for item in items) + "\nnot json\n", encoding="utf-8")
    run = _run(wired)
    assert run.not_voted == 3 and wired.endpoint.sent == []
    lines = {line["ticker"]: line for line in _lines(wired.month)}
    assert {line["error"] for line in lines.values()} == {vote.NO_ARCHIVE}
    assert lines["XLE"]["prompt_sha256"] == payload["model_calls"][0]["prompt_sha256"]


def test_an_input_that_production_would_not_send_today_is_not_voted(wired, monkeypatch):
    """Archived at effort "medium", while production asks at "high": not the same settings."""
    monkeypatch.setattr(heartbeat, "MODEL_EFFORT", "medium")
    _add_line(wired, "XLE")
    monkeypatch.setattr(heartbeat, "MODEL_EFFORT", llm.MODEL_EFFORT)
    run = _run(wired)
    assert (run.voted, run.not_voted, run.calls) == (0, 1, 0)
    assert wired.endpoint.sent == []
    (line,) = _lines(wired.month)
    assert line["error"] == vote.ARCHIVE_DIFFERS


def test_a_provider_that_cannot_rebuild_the_body_is_not_the_same_input(wired, monkeypatch):
    _add_line(wired, "XLE")
    monkeypatch.setattr(heartbeat, "full_model_provider", lambda: SimpleNamespace())
    run = _run(wired)
    assert run.not_voted == 1 and wired.endpoint.sent == []
    assert _lines(wired.month)[0]["error"] == vote.ARCHIVE_DIFFERS


@pytest.mark.parametrize("where", ["none", "missing", "empty"])
def test_no_download_writes_nothing_and_exits_1(wired, where):
    _add_line(wired, "XLE")
    directory = {"none": None, "missing": wired.archive.parent / "nowhere",
                 "empty": wired.archive.parent / "empty"}[where]
    if where == "empty":
        directory.mkdir()
        (directory / "notes.txt").write_text("no capture here")
    run = _run(wired, model_io_dir=directory)
    assert run.error == vote.NO_DOWNLOAD and run.exit_code == vote.EXIT_FAILED
    assert (run.calls, run.not_asked) == (0, 1)
    assert not wired.votes.exists() and wired.endpoint.sent == []


def test_no_model_key_stops_before_any_line_is_judged(wired, monkeypatch):
    _add_line(wired, "XLE")

    def no_key():
        raise llm.LLMError("FULL_MODEL_API_KEY is empty")

    monkeypatch.setattr(heartbeat, "full_model_provider", no_key)
    run = _run(wired)
    assert run.error and "FULL_MODEL_API_KEY is empty" in run.error and run.exit_code == vote.EXIT_FAILED
    assert not wired.votes.exists()


def test_a_run_where_every_call_failed_exits_1(wired):
    _add_line(wired, "XLE")
    wired.endpoint.script["XLE"] = [httpx.Response(400, text="no") for _ in range(4)]
    run = _run(wired)
    assert (run.calls, run.failed_calls) == (4, 4) and run.exit_code == vote.EXIT_FAILED


# --------------------------------------------------------------------------- #
# Timing: the budget, the cut-off and the day
# --------------------------------------------------------------------------- #


class TickingClock:
    """``utc_now`` that moves one minute on at every reading."""

    def __init__(self, start: datetime, then: datetime | None = None) -> None:
        self.now = start
        self.then = then

    def __call__(self) -> datetime:
        current = self.now
        self.now = self.then if self.then is not None else self.now + timedelta(minutes=1)
        return current


def test_the_time_budget_stops_new_names(wired):
    _add_line(wired, "XLE")
    _add_line(wired, "GLD")
    run = _run(wired, budget_seconds=0)
    assert (run.calls, run.not_asked, run.voted) == (0, 2, 0)
    assert wired.endpoint.sent == [] and not wired.votes.exists()


def test_no_name_is_started_after_the_cut_off_so_no_line_is_dated_the_next_day(wired, monkeypatch):
    for ticker in ("XLE", "GLD", "TLT"):
        _add_line(wired, ticker)
    # The run starts at 23:12; a name reads the clock to start and to write its line.
    monkeypatch.setattr(vote, "utc_now", TickingClock(A_DAY_ON.replace(hour=23, minute=12)))
    run = _run(wired, workers=1)
    assert run.ran is True and (run.voted, run.not_asked, run.calls) == (1, 2, 4)
    assert set(wired.endpoint.asked()) == {"XLE"}
    lines = _lines(wired.month)
    # The names the cut-off stopped are recorded, with no call, and are final (section 13.11: "and is counted").
    assert [line["ticker"] for line in lines] == ["XLE", "GLD", "TLT"]
    assert [line["error"] for line in lines] == [None, rule.NOT_ASKED_LATE, rule.NOT_ASKED_LATE]
    assert [len(line["votes"]) for line in lines] == [5, 1, 1] and [line["asks"] for line in lines] == [4, 0, 0]
    assert all(datetime.fromisoformat(line["ts_utc"]).date() == A_DAY_ON.date() for line in lines)
    assert run.exit_code == vote.EXIT_OK                    # the cut-off is not the cap: no phone
    assert rule.counters(rule.read_votes(wired.votes), A_DAY_ON.date())["not_asked"] == 2


def test_a_run_that_reaches_the_next_utc_day_starts_no_new_name(wired, monkeypatch):
    _add_line(wired, "XLE")
    monkeypatch.setattr(vote, "utc_now", TickingClock(A_DAY_ON.replace(hour=22),
                                                      then=A_DAY_ON.replace(hour=0, minute=1) + timedelta(days=1)))
    run = _run(wired, workers=1)
    assert run.day == A_DAY_ON.date() and (run.calls, run.not_asked) == (0, 1)
    assert wired.endpoint.sent == []


# --------------------------------------------------------------------------- #
# The cost cap
# --------------------------------------------------------------------------- #


def test_the_cap_stops_new_names_and_the_cli_exits_3(wired, monkeypatch, capsys):
    wired.endpoint.usage = DIME                               # $0.40 a name
    names = ("XLE", "GLD", "TLT", "SLV", "USO")
    for ticker in names:
        _add_line(wired, ticker)
    monkeypatch.setattr(mv, "JOURNAL_DIR", wired.votes)
    monkeypatch.setattr(cfg, "MODEL_IO_DIR", wired.capture)
    monkeypatch.setattr(vote, "WORKERS", 1)                   # one at a time, so the count is exact
    assert vote.main(["--model-io", str(wired.archive), "--run-id", "987"]) == vote.EXIT_CAP_REACHED
    summary = json.loads(capsys.readouterr().out)
    # A name starts while the day's total is under the cap: at $0, $0.40, $0.80; not at $1.20.
    assert (summary["voted"], summary["not_asked"], summary["calls"]) == (3, 2, 12)
    assert summary["cap_reached"] is True and summary["cap_usd"] == mv.DAILY_COST_CAP_USD
    assert summary["cost_usd"] == pytest.approx(1.20, abs=1e-4)
    assert summary["warn_crossed"] is True and summary["warn_usd"] == mv.DAILY_COST_WARN_USD
    assert summary["estimated_usd"] == pytest.approx(len(names) * 4 * mv.ESTIMATED_COST_PER_CALL_USD)
    assert summary["cap_stopped"] is True
    assert set(summary) == {"date", "ran", "reason", "lines", "already_voted", "voted", "answered", "dropped",
                            "not_voted", "not_asked", "unrecorded", "calls", "asks", "failed_calls", "cost_usd",
                            "cap_usd", "cap_reached", "cap_stopped", "warn_usd", "warn_crossed", "estimated_usd",
                            "error"}
    lines = _lines(wired.month)
    assert [line["ticker"] for line in lines] == list(names)
    assert [line["error"] for line in lines] == [None, None, None, rule.NOT_ASKED_CAP, rule.NOT_ASKED_CAP]
    assert sorted(wired.capture.rglob("*.jsonl"))[0].name.startswith("vote-987-")
    # The next run today has nothing left to vote, and does not tell the phone again.
    again = _run(wired)
    assert again.cap_reached is True and again.calls == 0 and again.warn_crossed is False
    assert again.cap_stopped is False and again.exit_code == vote.EXIT_OK
    # Nor does a run that the cap stops again on a later line of the same day: the cap line is already written.
    _add_line(wired, "DBA", when=A_DAY_ON.replace(hour=16, minute=0))
    later = _run(wired)
    assert later.cap_refused == 1 and later.cap_noted_before is True
    assert later.cap_stopped is False and later.exit_code == vote.EXIT_OK
    assert _lines(wired.month)[-1]["ticker"] == "DBA" and _lines(wired.month)[-1]["error"] == rule.NOT_ASKED_CAP


def test_a_run_that_reaches_the_cap_but_stops_no_name_does_not_tell_the_phone(wired):
    wired.endpoint.usage = THIRTY_CENTS                       # $1.20 a name: the only name passes the cap
    _add_line(wired, "XLE")
    run = _run(wired, workers=1)
    assert run.voted == 1 and run.cap_reached is True and run.cap_refused == 0
    assert run.cap_stopped is False and run.exit_code == vote.EXIT_OK


def test_the_cap_counts_what_was_already_spent_today(wired):
    _add_line(wired, "XLE")
    wired.votes.mkdir(parents=True)
    yesterday = A_DAY_ON - timedelta(days=1)
    with wired.month.open("w", encoding="utf-8") as handle:
        for when, cost in ((yesterday, 5.0), (A_DAY_ON - timedelta(hours=2), 0.6), (A_DAY_ON - timedelta(hours=1), 0.45)):
            handle.write(json.dumps({"ts_utc": when.isoformat(), "event": "model_vote", "ticker": "OLD",
                                     "line_ts_utc": when.isoformat(), "votes": [], "cost_usd": cost}) + "\n")
        handle.write("not json\n")
    run = _run(wired)
    assert run.cap_reached is True and run.exit_code == vote.EXIT_CAP_REACHED
    assert (run.calls, run.not_asked) == (0, 1)
    assert run.cost_usd == pytest.approx(1.05)                # yesterday's $5 is not today's
    assert wired.endpoint.sent == []


def test_with_four_workers_the_cap_holds_up_to_the_calls_in_flight(wired):
    wired.endpoint.usage = THIRTY_CENTS                       # $1.20 a name
    names = ("XLE", "GLD", "TLT", "SLV", "USO", "DBA")
    for ticker in names:
        _add_line(wired, ticker)
    run = _run(wired, workers=4)
    assert run.cap_reached is True and run.exit_code == vote.EXIT_CAP_REACHED
    assert run.voted + run.not_asked == len(names) and run.not_asked >= 1
    # A started name always gets its four calls, and is written; a name the cap stopped gets its final line.
    assert run.calls == 4 * run.voted
    lines = _lines(wired.month)
    assert all(len(line["votes"]) == 5 for line in lines if line["error"] is None)
    assert sum(1 for line in lines if line["error"] == rule.NOT_ASKED_CAP) == run.not_asked
    assert all(len(line["votes"]) == 1 and line["asks"] == 0 for line in lines if line["error"] is not None)
    # Names start only while spent + held is under the cap; at most three calls of
    # other names are unsettled then, so the overshoot is bounded.
    assert run.cost_usd <= mv.DAILY_COST_CAP_USD + 3 * 0.30 + 4 * 0.30 + 1e-6


def test_the_guard_holds_a_name_s_four_calls_refuses_at_the_cap_and_settles_each_call():
    guard = vote.CostGuard(1.0, spent_usd=0.5, per_call_usd=0.05)
    assert not guard.cap_reached
    assert guard.reserve(4)                                   # 0.5 is under $1: 0.2 held
    assert guard.reserve(4)                                   # 0.7 is under $1: 0.4 held
    assert guard.reserve(4)                                   # 0.9 is under $1: 0.6 held
    assert not guard.reserve(1) and guard.cap_reached         # 1.1 is not
    assert guard.calls == 12
    for _ in range(12):
        guard.settle(0.01)                                    # each call cheaper than the estimate
    assert guard.spent_usd == pytest.approx(0.62)
    assert guard.has_room()                                   # the estimates are released
    assert vote.CostGuard(1.0, spent_usd=1.0).cap_reached


@pytest.mark.parametrize("before, after, crossed", [
    (0.0, 0.70, False), (0.0, 0.80, True), (0.75, 0.85, True), (0.81, 0.95, False), (0.5, 1.05, True),
])
def test_warn_crossed_fires_only_in_the_run_that_passes_the_line(before, after, crossed):
    run = vote.VoteRun(day=A_DAY_ON.date(), ran=True, spent_before_usd=before, cost_usd=after)
    assert run.warn_crossed is crossed
    assert run.summary()["warn_crossed"] is crossed and run.summary()["warn_usd"] == mv.DAILY_COST_WARN_USD


def test_an_ask_is_charged_its_tokens_else_the_estimate():
    est = mv.ESTIMATED_COST_PER_CALL_USD
    priced = {"model": llm.MODEL, "usage": CHEAP}
    assert vote.ask_cost_usd(priced, est) == pytest.approx(CHEAP_USD)
    assert vote.ask_cost_usd({"model": llm.MODEL, "usage": None}, est) == est            # a timeout
    assert vote.ask_cost_usd({"model": "a-model-with-no-price", "usage": CHEAP}, est) == est
    assert vote.ask_cost_usd({"model": llm.MODEL, "usage": {"prompt_tokens": True, "completion_tokens": 1}}, est) == est
    assert vote.ask_cost_usd({"model": llm.MODEL, "usage": {"prompt_tokens": 10}}, est) == est


def test_with_no_capture_a_call_is_one_ask_at_the_estimate_or_its_measured_cost(tmp_path):
    ledger = vote.CaptureLedger(0.003)
    assert ledger.asks("XLE vote 2") is None                 # no capture open
    assert ledger.charge("XLE vote 2", llm.LLMError("down")) == (1, 0.003)
    dear = Completion(text="{}", usage=Usage(model=llm.MODEL, input_tokens=0, output_tokens=666_667))
    assert ledger.charge("XLE vote 3", dear) == (1, pytest.approx(0.30, abs=1e-4))
    with model_io.capture(tmp_path / "io", run_id="x"):
        assert ledger.asks("XLE vote 2") is None             # open, nothing written yet
        attempt = model_io.begin("openai-compatible", llm.MODEL, {"a": 1}, label="XLE vote 2")
        model_io.finish_attempt(attempt, outcome="answer", usage=CHEAP)
        assert ledger.asks("XLE vote 2") == [pytest.approx(CHEAP_USD)]
        assert ledger.asks("XLE vote 3") == []
        assert ledger.charge("XLE vote 3", llm.LLMError("down")) == (1, 0.003)
        # Charging takes the label's asks: a later call under the same label pays only its own.
        assert ledger.charge("XLE vote 2", llm.LLMError("down")) == (1, pytest.approx(CHEAP_USD))
        assert ledger.asks("XLE vote 2") == []
        again = model_io.begin("openai-compatible", llm.MODEL, {"a": 2}, label="XLE vote 2")
        model_io.finish_attempt(again, outcome="timeout")
        assert ledger.charge("XLE vote 2", llm.LLMError("down")) == (1, 0.003)


def test_the_days_vote_lines_read_only_today(tmp_path):
    directory = tmp_path / "v"
    directory.mkdir()
    day = date(2027, 2, 1)
    path = month_file(directory, datetime(2027, 2, 1, tzinfo=timezone.utc))
    rows = [
        {"ts_utc": "2027-02-01T18:31:00+00:00", "event": "model_vote", "ticker": "XLE",
         "line_ts_utc": "2027-02-01T15:00:00+00:00", "votes": [], "cost_usd": 0.01},
        {"ts_utc": "2027-02-02T18:31:00+00:00", "event": "model_vote", "ticker": "GLD",
         "line_ts_utc": "2027-02-02T15:00:00+00:00", "votes": [], "cost_usd": 0.02},
        {"ts_utc": "2027-02-01T18:32:00+00:00", "event": "something_else", "ticker": "TLT", "cost_usd": 9.0},
    ]
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\n[1, 2]\n", encoding="utf-8")
    seen = vote.day_votes(directory, day)
    assert seen.spent_usd == pytest.approx(0.01)
    assert seen.voted == frozenset({("XLE", datetime(2027, 2, 1, 15, tzinfo=timezone.utc))})
    assert vote.day_votes(tmp_path / "missing", day) == vote.DayVotes()


# --------------------------------------------------------------------------- #
# The workflow's job
# --------------------------------------------------------------------------- #


def _workflow() -> dict:
    return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))


def _steps(job: str) -> list[dict]:
    return _workflow()["jobs"][job]["steps"]


def _step(name: str, job: str = "vote") -> dict:
    return next(s for s in _steps(job) if s.get("name") == name)


#: The model's key under every spelling the production chain tries; the vote needs nothing else.
#: The vote can only re-send an OpenAI-compatible body, so the full model's key is all it may hold.
MODEL_KEYS = {"FULL_MODEL_API_KEY"}

VOTE_STEPS = [
    "Would it vote today?", "Has the production run finished, and its model calls?", "Vote",
    "Keep the vote's model calls as an artifact", "Commit the vote lines",
    "Tell the owner's phone the vote passed $0.80 today", "Tell the owner's phone the cost cap stopped the vote",
]


def test_the_vote_job_runs_after_the_universe_and_only_where_the_universe_may():
    jobs = _workflow()["jobs"]
    job = jobs["vote"]
    assert job["needs"] == "score"
    # After the universe's job whether it passed or failed, never after a cancel: a cancel stops the spending.
    assert job["if"] == "${{ !cancelled() && github.event_name != 'pull_request' && !inputs.verify }}"
    assert jobs["score"]["if"] == "${{ github.event_name != 'pull_request' && !inputs.verify }}"
    assert job["permissions"] == {"contents": "write", "actions": "read"}
    assert job["runs-on"] == "ubuntu-latest"
    names = [s.get("name") for s in job["steps"] if s.get("name")]
    assert names == ["Install dependencies", *VOTE_STEPS]
    # The same pinned actions as the universe's job.
    assert [s.get("uses") for s in job["steps"][:2]] == [s.get("uses") for s in jobs["score"]["steps"][:2]]
    assert job["steps"][0]["with"] == {"ref": "${{ github.ref }}"}


def test_the_vote_job_checks_first_and_skips_everything_after():
    steps = _steps("vote")
    names = [s.get("name") for s in steps]
    check_at = names.index("Would it vote today?")
    check = steps[check_at]
    assert "python -m orchestrator.vote --check" in check["run"]
    assert 'echo "run=$run" >> "$GITHUB_OUTPUT"' in check["run"] and 'echo "runs=$runs" >> "$GITHUB_OUTPUT"' in check["run"]
    assert "r.isdigit()" in check["run"]
    assert not check.get("env")                               # the check needs no key
    for step in steps[check_at + 1:]:
        assert ("steps.check.outputs.run == 'yes'" in step["if"] or "steps.ready.outputs.ready == 'yes'" in step["if"]
                or "steps.vote.outputs" in step["if"]), step["name"]


def test_the_vote_waits_for_the_production_run_and_downloads_its_model_calls():
    ready = _step("Has the production run finished, and its model calls?")
    assert ready["id"] == "ready" and ready["if"] == "steps.check.outputs.run == 'yes'"
    assert ready["env"] == {"GH_TOKEN": "${{ github.token }}", "RUNS": "${{ steps.check.outputs.runs }}"}
    run = ready["run"]
    assert 'gh run view "$id" --repo "$GITHUB_REPOSITORY" --json status --jq .status' in run
    assert '!= "completed"' in run
    assert ('gh run download "$id" --repo "$GITHUB_REPOSITORY" --pattern "model-io-$id-*" '
            '--dir "$RUNNER_TEMP/model_io"') in run
    assert "(*[!0-9]*)" in run                                # a run id is digits only
    assert 'echo "ready=$ready" >> "$GITHUB_OUTPUT"' in run
    assert "exit 1" not in run                                # never fails the job
    # The production artifact's name, as heartbeat.yml uploads it.
    heartbeat_wf = (ROOT / ".github/workflows/heartbeat.yml").read_text(encoding="utf-8")
    assert "name: model-io-${{ github.run_id }}-${{ github.run_attempt }}" in heartbeat_wf


def test_the_vote_step_gets_exactly_the_model_key_and_nothing_else():
    voting = _step("Vote")
    score = _step("Score the universe", "score")
    assert voting["if"] == "steps.ready.outputs.ready == 'yes'"
    assert set(voting["env"]) == MODEL_KEYS
    for key in MODEL_KEYS:
        assert voting["env"][key] == score["env"][key], key
    run = voting["run"]
    assert 'python -m orchestrator.vote --model-io "$RUNNER_TEMP/model_io" --run-id "$GITHUB_RUN_ID"' in run
    assert '"$status" = "3"' in run and 'echo "cap=yes" >> "$GITHUB_OUTPUT"' in run
    assert '"warn_crossed"' in run and 'echo "warn=$warn" >> "$GITHUB_OUTPUT"' in run
    assert run.index("warn=$warn") < run.index('exit "$status"')


def test_the_vote_keeps_its_model_calls_and_commits_its_lines():
    artifact = _step("Keep the vote's model calls as an artifact")
    heartbeat_steps = yaml.safe_load((ROOT / ".github/workflows/heartbeat.yml").read_text())["jobs"]["cycle"]["steps"]
    upload = next(s for s in heartbeat_steps if s.get("name") == "Keep the day's model calls as an artifact")
    assert artifact["uses"] == upload["uses"]
    assert artifact["with"] == {"name": "model-io-vote-${{ github.run_id }}-${{ github.run_attempt }}",
                                "path": "logs/model_io/", "retention-days": 90, "if-no-files-found": "ignore"}
    assert artifact["continue-on-error"] is True
    commit = _step("Commit the vote lines")
    assert commit["if"] == "always() && steps.check.outputs.run == 'yes'"
    assert "git add -f logs/model_vote/" in commit["run"]
    assert "git pull --rebase" in commit["run"] and "for attempt in" in commit["run"]


def _words(run: str) -> str:
    return " ".join(re.findall(r'"([^"]*)"', re.search(r'"message": \((.*?)\),', run, re.S).group(1)))


def test_the_vote_s_phone_alerts_are_fixed_words_through_the_topic_secret():
    warn, cap = f"${mv.DAILY_COST_WARN_USD:.2f}", f"${mv.DAILY_COST_CAP_USD:.2f}"
    assert (warn, cap) == ("$0.80", "$1.00")
    passed = _step("Tell the owner's phone the vote passed $0.80 today")
    _is_a_safe_push(passed)
    assert passed["if"] == "always() && steps.vote.outputs.warn == 'yes' && steps.vote.outputs.cap != 'yes'"
    words = _words(passed["run"])
    assert warn in words and cap in words
    assert re.findall(r"\d", words.replace(warn, "").replace(cap, "")) == []
    stopped = _step("Tell the owner's phone the cost cap stopped the vote")
    _is_a_safe_push(stopped)
    assert stopped["if"] == "always() && steps.vote.outputs.cap == 'yes'"
    words = _words(stopped["run"])
    assert cap in words and "stopped" in words
    assert re.findall(r"\d", words.replace(cap, "")) == []


def test_the_vote_job_s_clock_outlasts_the_budget_and_the_last_calls():
    """Derived from the constants, so a longer budget or a shorter timeout fails here
    instead of killing a run before its lines are committed."""
    clock = _workflow()["jobs"]["vote"]["timeout-minutes"]
    worst_call = llm.SCHEMA_ATTEMPTS * (llm.FULL_MODEL_TIMEOUT_SECONDS + llm.TRANSPORT_RETRY_TIMEOUT_SECONDS) / 60
    # After the budget: the calls in flight, then the rest of the last name started.
    setup_and_commit = 10
    assert clock >= vote.RUN_BUDGET_SECONDS / 60 + 2 * worst_call + setup_and_commit
    assert clock <= 360  # GitHub's own ceiling for a job
