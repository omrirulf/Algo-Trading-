"""The shadow stock universe: built now, off until 2027-01-01, never traded.

The owner's instruction of 2 Oct 2026, item 5: a fixed list of about 250 US
stocks and ADRs, scored daily by the production model with the production
prompt, one call per name, with a $1 daily cost cap, kept off by a flag that
must not be on before the date the pre-registration names. This file pins
the flag to the pre-registration, the list to its selection rule, the scorer
to the production path (and away from the engine), the line format the IC
report reads, the cost cap, and the workflow's keys.

Offline throughout: the context and the model are stand-ins.
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

import pytest
import yaml

from analysis.reader import entry_from
from config import settings as cfg
from config import shadow_universe as su
from config.instruments import FUNDS, is_fund
from config.journal_files import month_file
from config.market_calendar import is_trading_day
from config.watchlist import DEFAULT_WATCHLIST
from orchestrator import context, heartbeat, journal, llm, sources, universe
from orchestrator.llm import Completion, LLMError
from orchestrator.pricing import Usage
from rules import ARMS
from tests.test_context import HEADLINES, full_provider

ROOT = Path(__file__).resolve().parents[1]
PREREG = ROOT / "docs/horse-race-preregistration.md"
WORKFLOW = ROOT / ".github/workflows/shadow-universe.yml"
SOURCE = ROOT / "orchestrator/universe.py"

#: A Tuesday in the universe's first week: on or after START, and a trading day.
A_DAY_ON = datetime(2027, 1, 5, 18, 30, tzinfo=timezone.utc)

#: The keys of the shared line format (scratchpad/tasks/universe_line.md).
LINE_KEYS = {
    "ts_utc", "ticker", "universe", "signal", "blend", "arms", "context", "usage",
    "error", "model_setup", "reasoning_effort", "event",
}


# --------------------------------------------------------------------------- #
# The flag and the pre-registration
# --------------------------------------------------------------------------- #

FLAG_PHRASE = "Shadow stock universe (`SHADOW_UNIVERSE_ENABLED`): **{state}** until **"


def test_the_flag_is_the_one_the_pre_registration_registers():
    """The screening-flag pattern (tests/test_horse_race.py): the file says
    off or on and until when; the code's start date is that date; and the
    flag cannot be on before it. Fails until the pre-registration carries
    the phrase -- the file is amended first, the code follows."""
    text = " ".join(PREREG.read_text(encoding="utf-8").split())
    off, on = FLAG_PHRASE.format(state="off"), FLAG_PHRASE.format(state="on")
    assert off in text or on in text, (
        "the pre-registration does not register the shadow universe; it must say "
        f"{off}{su.START.isoformat()}**"
    )
    registered_off = off in text
    tail = text.split(off if registered_off else on, 1)[1]
    found = re.match(r"(\d{4}-\d{2}-\d{2})\*\*", tail)
    assert found, "the registered date must follow `until **` as YYYY-MM-DD"
    registered = date.fromisoformat(found.group(1))
    assert su.START == registered, f"START is {su.START}; the pre-registration registers {registered}"
    if registered_off:
        assert su.SHADOW_UNIVERSE_ENABLED is False, (
            "SHADOW_UNIVERSE_ENABLED is on but the pre-registration says off; amend the file first"
        )
    if date.today() < registered:
        assert su.SHADOW_UNIVERSE_ENABLED is False, (
            f"SHADOW_UNIVERSE_ENABLED is on before {registered}, the date the pre-registration names"
        )


def test_the_registered_settings():
    # The flag itself is pinned against the pre-registration's date above, so
    # switching it on as registered does not fail here.
    assert su.START == date(2027, 1, 1)
    assert su.REGISTRATION == date(2026, 12, 22)
    assert su.REGISTRATION < su.START
    assert su.DAILY_COST_CAP_USD == 1.00
    assert su.ESTIMATED_DAILY_COST_USD == 0.65
    assert su.ESTIMATED_DAILY_COST_USD < su.DAILY_COST_CAP_USD


def test_the_journal_has_its_own_directory_beside_the_production_one():
    # Compared with the literal: the suite points SIGNAL_JOURNAL_PATH at a
    # temporary file (tests/conftest.py), LOG_DIR it leaves alone.
    assert su.JOURNAL_DIR == cfg.LOG_DIR / "shadow_universe"
    assert su.JOURNAL_DIR != cfg.LOG_DIR / "journal"


# --------------------------------------------------------------------------- #
# The list
# --------------------------------------------------------------------------- #


def test_about_250_unique_names_that_look_like_us_tickers():
    assert 240 <= len(su.TICKERS) <= 260
    assert len(set(su.TICKERS)) == len(su.TICKERS)
    for ticker in su.TICKERS:
        assert re.fullmatch(r"[A-Z][A-Z0-9.-]{0,9}", ticker), ticker


def test_no_production_name_and_no_other_share_class_of_one():
    """The two universes are kept apart, so no name is counted twice."""
    assert not set(su.TICKERS) & set(DEFAULT_WATCHLIST)
    assert "GOOG" not in su.TICKERS  # Alphabet's other class; GOOGL is production's
    # One share class per company: no dotted or dashed class tickers at all.
    assert not [t for t in su.TICKERS if "." in t or "-" in t]


def test_companies_only_so_every_name_gets_the_company_prompt():
    """``is_fund`` is total (an unknown ticker is a company), so a name off the
    watchlist gets the company prompt and the analyst and insider sections."""
    assert not set(su.TICKERS) & set(FUNDS)
    for ticker in su.TICKERS:
        assert is_fund(ticker) is False, ticker
        assert heartbeat.system_prompt_for(ticker) == heartbeat.SYSTEM_PROMPT


def test_every_name_has_a_sector_and_every_sector_is_there():
    assert set(su.SECTORS) == set(su.TICKERS)
    labels = set(su.SECTORS.values())
    assert len(su.GICS_SECTORS) == 11
    assert set(su.GICS_SECTORS) <= labels
    for sector in su.GICS_SECTORS:
        assert len(su.BLOCKS[sector]) >= 10, sector


def test_there_is_an_adr_block_across_regions():
    adr = {label for label in su.BLOCKS if label.startswith(su.ADR_PREFIX)}
    regions = {label[len(su.ADR_PREFIX):] for label in adr}
    assert {"Europe", "Japan", "China and Hong Kong", "India", "Latin America", "Israel"} <= regions
    assert sum(len(su.BLOCKS[label]) for label in adr) >= 40
    # Every label is either a GICS sector or an ADR region.
    assert set(su.BLOCKS) == set(su.GICS_SECTORS) | adr


def test_ordered_by_sector_then_alphabetically():
    labels = list(su.BLOCKS)
    assert labels[:11] == list(su.GICS_SECTORS)
    assert all(label.startswith(su.ADR_PREFIX) for label in labels[11:])
    for label, names in su.BLOCKS.items():
        assert list(names) == sorted(names), label
    assert su.TICKERS == tuple(t for names in su.BLOCKS.values() for t in names)


def test_the_card_table_lists_every_name_by_sector():
    table = su.markdown_table()
    for label, names in su.BLOCKS.items():
        assert f"| {label} | {len(names)} | {', '.join(names)} |" in table
    assert f"**{len(su.TICKERS)}**" in table
    assert su.REGISTRATION.isoformat() in table and su.SELECTED_ON.isoformat() in table


# --------------------------------------------------------------------------- #
# The scorer stays off when it should
# --------------------------------------------------------------------------- #


@pytest.fixture
def nothing_may_happen(monkeypatch, tmp_path):
    """Any context, model call or file would be a failure."""
    def refuse(*_args, **_kwargs):
        raise AssertionError("the scorer did something on a day it must not run")

    for name in ("build_context", "call_llm", "full_model_provider", "model_setup"):
        monkeypatch.setattr(heartbeat, name, refuse)
    return tmp_path / "shadow_universe"


@pytest.mark.parametrize("enabled, now, reason", [
    (False, A_DAY_ON, "the flag SHADOW_UNIVERSE_ENABLED is off"),
    (True, datetime(2026, 12, 31, 18, 30, tzinfo=timezone.utc), "before the start date 2027-01-01"),
    (True, datetime(2027, 1, 18, 18, 30, tzinfo=timezone.utc), "not a trading day"),   # Martin Luther King Day
    (True, datetime(2027, 1, 9, 18, 30, tzinfo=timezone.utc), "not a trading day"),    # a Saturday
])
def test_the_scorer_does_nothing_when_off_early_or_closed(monkeypatch, nothing_may_happen, enabled, now, reason):
    monkeypatch.setattr(su, "SHADOW_UNIVERSE_ENABLED", enabled)
    monkeypatch.setattr(universe, "utc_now", lambda: now)
    run = universe.score_universe(journal_dir=nothing_may_happen)
    assert run.ran is False and reason in run.reason
    assert (run.asked, run.answered, run.failed, run.cost_usd) == (0, 0, 0, 0.0)
    assert run.exit_code == universe.EXIT_OK
    assert not nothing_may_happen.exists()
    assert universe.check(now) == {"date": now.date().isoformat(), "run": False, "reason": run.reason}


def _production_journal(monkeypatch, tmp_path, *stamps: datetime) -> Path:
    """A production journal holding one line at each of ``stamps``."""
    directory = tmp_path / "journal"
    for stamp in stamps:
        path = month_file(directory, stamp)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"ts_utc": stamp.isoformat(), "ticker": "XLE", "signal": None,
                                     "error": "x"}) + "\n")
    monkeypatch.setattr(cfg, "SIGNAL_JOURNAL_PATH", directory)
    return directory


def test_the_check_says_yes_on_a_trading_day_after_the_start_once_production_ran(monkeypatch, tmp_path):
    monkeypatch.setattr(su, "SHADOW_UNIVERSE_ENABLED", True)
    assert is_trading_day(A_DAY_ON.date())
    _production_journal(monkeypatch, tmp_path, A_DAY_ON.replace(hour=15, minute=2))
    assert universe.check(A_DAY_ON) == {"date": "2027-01-05", "run": True, "reason": None}


def test_the_universe_waits_for_the_days_production_cycle(monkeypatch, tmp_path, nothing_may_happen):
    """So the two never ask the model provider at the same time, and no
    catch-up cycle starts once the universe runs (heartbeat.yml's guard)."""
    monkeypatch.setattr(su, "SHADOW_UNIVERSE_ENABLED", True)
    monkeypatch.setattr(universe, "utc_now", lambda: A_DAY_ON)
    yesterday = A_DAY_ON - timedelta(days=1)
    _production_journal(monkeypatch, tmp_path, yesterday)   # yesterday's cycle is not today's
    answer = universe.check(A_DAY_ON)
    assert answer["run"] is False and "no production cycle is journalled for 2027-01-05" in answer["reason"]
    run = universe.score_universe(("AAPL",), journal_dir=nothing_may_happen)
    assert run.ran is False and run.reason == answer["reason"] and run.exit_code == universe.EXIT_OK
    assert not nothing_may_happen.exists()
    monkeypatch.setattr(cfg, "SIGNAL_JOURNAL_PATH", tmp_path / "no-journal-at-all")
    assert universe.production_ran(A_DAY_ON.date()) is False


def test_the_cli_check_and_an_off_run_ask_nothing_and_exit_0(monkeypatch, capsys, nothing_may_happen):
    monkeypatch.setattr(su, "SHADOW_UNIVERSE_ENABLED", False)
    monkeypatch.setattr(universe, "utc_now", lambda: A_DAY_ON)
    assert universe.main(["--check"]) == 0
    answer = json.loads(capsys.readouterr().out)
    assert answer == {"date": "2027-01-05", "run": False, "reason": "the flag SHADOW_UNIVERSE_ENABLED is off"}
    monkeypatch.setattr(su, "JOURNAL_DIR", nothing_may_happen)
    assert universe.main([]) == 0
    summary = json.loads(capsys.readouterr().out)
    assert summary["ran"] is False and summary["asked"] == 0
    assert not nothing_may_happen.exists()


# --------------------------------------------------------------------------- #
# The scorer reuses production and cannot reach the engine
# --------------------------------------------------------------------------- #

#: Names that would mean the module can trade, writes the production journal
#: or reads the live price: none may appear in it, as a name or an attribute.
FORBIDDEN_NAMES = {
    "post_signal", "build_dispatcher", "Dispatcher", "DirectDispatcher", "dispatch",
    "dispatcher", "judge_answer", "process_ticker", "prepare_ticker", "apply_screen",
    "screen_signal", "run_cycle", "run_batched_cycle", "manage_positions",
    "protect_positions", "open_tickers", "is_market_open", "ExecutionEngine",
    "PositionManager", "AlpacaPaperBroker", "TradingClient", "submit_order",
    "submit_bracket_order", "record", "read_live", "note_cycle", "live_price",
    "flows",
}

FORBIDDEN_MODULES = (
    "orchestrator.live_price", "orchestrator.dispatch",
    "orchestrator.digest", "orchestrator.flows", "app.broker_client", "app.execution_engine",
    "app.position_manager", "app.main", "alpaca", "store", "anthropic", "openai",
)


def _tree() -> ast.Module:
    return ast.parse(SOURCE.read_text(encoding="utf-8"))


def _imported(tree: ast.Module) -> set[str]:
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names |= {alias.name for alias in node.names}
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module)
            names |= {f"{node.module}.{alias.name}" for alias in node.names}
    return names


def test_the_scorer_never_names_the_engine_the_broker_or_the_production_journal():
    tree = _tree()
    used = ({n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}
            | {n.attr for n in ast.walk(tree) if isinstance(n, ast.Attribute)}
            | {alias.asname or alias.name for n in ast.walk(tree)
               if isinstance(n, (ast.Import, ast.ImportFrom)) for alias in n.names})
    assert not used & FORBIDDEN_NAMES, sorted(used & FORBIDDEN_NAMES)
    imported = _imported(tree)
    bad = sorted(name for name in imported
                 for module in FORBIDDEN_MODULES if name == module or name.startswith(module + "."))
    assert not bad, bad


def test_the_only_journal_function_the_scorer_uses_makes_the_blend_and_arms_records():
    """The journal computes the blend's and the arms' records (the CI guardrails allow only it, besides their own
    modules); ``journal.record``, which writes the production journal, is never named."""
    tree = _tree()
    used = {n.attr for n in ast.walk(tree)
            if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name) and n.value.id == "journal"}
    assert used == {"universe_records"}


def test_the_scorer_calls_the_production_functions():
    """Same model, settings and prompt: the steps are heartbeat's own, not copies."""
    tree = _tree()
    attributes = {(n.value.id, n.attr) for n in ast.walk(tree)
                  if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name)}
    for name in ("build_context", "system_prompt_for", "build_user_prompt", "call_llm", "_ask",
                 "parse_signal", "scores_without_a_source", "PreparedTicker", "model_setup",
                 "full_model_provider"):
        assert ("heartbeat", name) in attributes, name
    assert ("blend", "load_weights") in attributes
    # The blend's and the arms' records are made by the journal, the one module besides theirs the CI
    # guardrails let compute and write them down.
    assert ("journal", "universe_records") in attributes
    assert ("journal_files", "month_file") in attributes


def test_the_scorer_reads_no_credential_and_does_not_import_the_price_reader():
    """The two CI greps that cover every orchestrator module, run here too."""
    text = SOURCE.read_text(encoding="utf-8")
    credential = re.compile(r"(get_settings|os\.environ|getenv|\bsettings\.|\.[A-Za-z_]*(secret|api_key|_token|password)\b)")
    assert not [line for line in text.splitlines() if credential.search(line)]
    assert not re.search(r"(from orchestrator import [^#\n]*\blive_price\b|orchestrator\.live_price|import live_price)", text)


def test_the_workers_and_the_budget_are_production_s_and_fit_the_list():
    assert universe.WORKERS == cfg.FULL_MODEL_MAX_CONCURRENCY
    # About two and a half minutes a name (context, then one call at high
    # effort): the whole list fits the budget with room to spare.
    expected_minutes = math.ceil(len(su.TICKERS) / universe.WORKERS) * 150 / 60
    assert expected_minutes <= universe.RUN_BUDGET_SECONDS / 60
    assert universe.ESTIMATED_COST_PER_NAME_USD * len(su.TICKERS) == pytest.approx(su.ESTIMATED_DAILY_COST_USD)


# --------------------------------------------------------------------------- #
# Scoring, with stand-ins for the context and the model
# --------------------------------------------------------------------------- #

#: gpt-oss-120b's price row is $0.05 in and $0.45 out per million tokens.
CHEAP = Usage(model="openai/gpt-oss-120b", input_tokens=1_000, output_tokens=2_000)
THIRTY_CENTS = Usage(model="openai/gpt-oss-120b", input_tokens=0, output_tokens=666_667)


def _ticker_of(user_prompt: str) -> str:
    return re.search(r"Respond with the JSON signal for (\S+)\.$", user_prompt).group(1)


def _signal(ticker: str) -> dict:
    return {
        "ticker": ticker, "bias": "BULLISH", "conviction": 0.6,
        "rationale": f"{ticker}: steady climb and an analyst upgrade",
        "news_score": 0.2, "technical_score": 0.5, "fundamental_score": 0.1,
        "analyst_score": 0.3, "insider_score": -0.1, "key_factors": ["trend", "upgrade"],
    }


class FakeModel:
    """Stands in for ``heartbeat.call_llm``: one answer per call, counted."""

    def __init__(self, usage: Usage = CHEAP, behaviour: dict | None = None) -> None:
        self.usage = usage
        self.behaviour = behaviour or {}
        self.calls: list[tuple[str, str, str]] = []
        self._lock = threading.Lock()

    def __call__(self, system_prompt: str, user_prompt: str, json_schema: dict) -> Completion:
        ticker = _ticker_of(user_prompt)
        with self._lock:
            self.calls.append((ticker, system_prompt, user_prompt))
        assert json_schema is heartbeat.SIGNAL_JSON_SCHEMA
        act = self.behaviour.get(ticker)
        if isinstance(act, BaseException):
            raise act
        if act == "not json":
            return Completion(text="this is not JSON", usage=self.usage)
        if isinstance(act, str):  # answer for another ticker
            return Completion(text=json.dumps(_signal(act)), usage=self.usage)
        return Completion(text=json.dumps(_signal(ticker)), usage=self.usage)

    def asked(self) -> list[str]:
        return [ticker for ticker, _, _ in self.calls]


@pytest.fixture
def wired(monkeypatch, tmp_path):
    """The flag on, a trading day in January 2027, stand-ins for the context
    and the model, and production's order path and journal booby-trapped."""
    monkeypatch.setattr(su, "SHADOW_UNIVERSE_ENABLED", True)
    monkeypatch.setattr(universe, "utc_now", lambda: A_DAY_ON)
    monkeypatch.setattr(universe, "production_ran", lambda day: True)
    monkeypatch.setattr(cfg, "BLEND_WEIGHTS_PATH", tmp_path / "no-weights.json")
    gathered: list[str] = []
    failing_context: set[str] = set()

    def build_context(ticker: str):
        gathered.append(ticker)
        if ticker in failing_context:
            raise RuntimeError(f"yfinance fell over for {ticker}")
        return context.gather(ticker, HEADLINES, provider=full_provider())

    monkeypatch.setattr(heartbeat, "build_context", build_context)

    def never(*_args, **_kwargs):
        raise AssertionError("the shadow universe reached the engine or the production journal")

    for name in ("post_signal", "build_dispatcher", "judge_answer", "process_ticker",
                 "prepare_ticker", "apply_screen", "journal_context_failure"):
        monkeypatch.setattr(heartbeat, name, never)
    monkeypatch.setattr(journal, "record", never)

    model = FakeModel()
    monkeypatch.setattr(heartbeat, "call_llm", model)
    directory = tmp_path / "shadow_universe"
    return SimpleNamespace(dir=directory, model=model, gathered=gathered,
                           failing_context=failing_context,
                           month=month_file(directory, A_DAY_ON))


def _lines(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def test_writes_the_documented_line_for_every_name(wired):
    names = ("AAPL", "KO", "SAP")
    run = universe.score_universe(names, journal_dir=wired.dir)
    assert (run.ran, run.names, run.asked, run.answered, run.failed, run.not_asked) == (True, 3, 3, 3, 0, 0)
    assert run.exit_code == universe.EXIT_OK and run.cap_reached is False
    assert run.cost_usd == pytest.approx(3 * CHEAP.cost_usd)

    # One call per name, with exactly the production prompts.
    assert sorted(wired.model.asked()) == sorted(names)
    for ticker, system_prompt, user_prompt in wired.model.calls:
        ctx = context.gather(ticker, HEADLINES, provider=full_provider())
        assert system_prompt == heartbeat.system_prompt_for(ticker, ctx) == heartbeat.SYSTEM_PROMPT
        assert user_prompt == heartbeat.build_user_prompt(ctx)

    assert wired.month.name == "2027-01.log"
    lines = _lines(wired.month)
    assert sorted(line["ticker"] for line in lines) == sorted(names)
    for line in lines:
        assert LINE_KEYS <= set(line)
        assert line["universe"] == "shadow" and line["event"] == "shadow_universe_scored"
        assert datetime.fromisoformat(line["ts_utc"]) == A_DAY_ON
        assert line["error"] is None and line["stage"] is None and line["held"] is False
        assert line["signal"] == _signal(line["ticker"])
        assert "composite" in line["blend"] and line["blend"]["mode"] == "shadow"
        assert line["blend"]["composite"] is not None
        assert set(line["arms"]) == set(ARMS)
        assert set(line["arms"]["momentum"]) == {"bias", "conviction", "rationale"}
        assert isinstance(line["context"]["technicals"], dict)
        assert line["context"]["headline_count"] == len(HEADLINES)
        assert "headlines" not in line["context"] and "sources" not in line["context"]
        assert line["usage"]["cost_usd"] == pytest.approx(CHEAP.cost_usd)
        assert line["model_setup"] == heartbeat.model_setup()
        assert line["reasoning_effort"] == llm.configured_effort()
        # The project's own reader takes it as an answered line, its scores intact.
        entry = entry_from(line)
        assert entry.model_answered and not entry.model_failed
        assert entry.sections == {"analysts", "insiders"}


def test_the_ic_report_reads_the_line_with_every_score(wired):
    """The reader the line is written for, when it is there (analysis/ic.py)."""
    ic = pytest.importorskip("analysis.ic")
    if not hasattr(ic, "line_from"):
        pytest.skip("analysis.ic has no line_from")
    universe.score_universe(("AAPL",), journal_dir=wired.dir)
    (line,) = _lines(wired.month)
    read = ic.line_from(line)
    assert read is not None and read.ticker == "AAPL" and read.day == A_DAY_ON.date()
    assert read.scores["blend"] == line["blend"]["composite"]
    for name in ("news", "technical", "fundamental", "analyst", "insider"):
        assert read.scores[name] == line["signal"][f"{name}_score"], name
    assert read.scores["momentum"] is not None


def test_the_arms_are_the_ones_the_production_journal_would_write(wired):
    universe.score_universe(("AAPL",), journal_dir=wired.dir)
    (line,) = _lines(wired.month)
    ctx = context.gather("AAPL", HEADLINES, provider=full_provider())
    from app.schemas import LLMSignal
    from orchestrator import arms

    expected = arms.arms_record(ctx, A_DAY_ON.date(), LLMSignal.model_validate(_signal("AAPL")))
    assert line["arms"] == json.loads(json.dumps(expected))


def test_one_call_per_name_a_day_so_a_second_run_asks_nobody_again(wired):
    names = ("AAPL", "KO", "SAP")
    universe.score_universe(names, journal_dir=wired.dir)
    again = universe.score_universe(names, journal_dir=wired.dir)
    assert (again.asked, again.answered, again.already_answered) == (0, 0, 3)
    assert len(wired.model.calls) == 3
    assert again.cost_usd == pytest.approx(3 * CHEAP.cost_usd)  # the day's total, read back
    assert len(_lines(wired.month)) == 3


def test_failures_are_counted_and_written(wired):
    wired.failing_context.add("KO")
    wired.model.behaviour.update({
        "SAP": LLMError("https://api.deepinfra.com returned HTTP 500 (gave up after 4 attempt(s))"),
        "NKE": "not json",
        "TSM": "AAPL",  # answered for another name
    })
    run = universe.score_universe(("AAPL", "KO", "SAP", "NKE", "TSM"), journal_dir=wired.dir)
    assert (run.asked, run.answered, run.failed) == (4, 1, 4)  # KO never reached the model
    assert run.exit_code == universe.EXIT_OK
    by_name = {line["ticker"]: line for line in _lines(wired.month)}
    assert by_name["AAPL"]["error"] is None
    assert by_name["KO"]["stage"] == "context" and "yfinance fell over" in by_name["KO"]["error"]
    assert by_name["KO"]["signal"] is None and by_name["KO"]["usage"] is None
    assert "momentum" in by_name["KO"]["arms"]  # the arms are on a failed line too
    assert by_name["SAP"]["error"].startswith("https://api.deepinfra.com returned HTTP 500")
    assert by_name["SAP"]["stage"] is None and by_name["SAP"]["signal"] is None
    assert by_name["NKE"]["error"].startswith("invalid LLM output")
    assert by_name["NKE"]["usage"]["cost_usd"] == pytest.approx(CHEAP.cost_usd)  # paid for all the same
    assert by_name["TSM"]["error"] == "answered for AAPL" and by_name["TSM"]["signal"]["ticker"] == "AAPL"
    for line in by_name.values():
        entry = entry_from(line)
        assert entry.model_answered is (line["ticker"] == "AAPL")


def test_a_run_where_every_name_failed_exits_1(wired):
    wired.model.behaviour.update({t: LLMError("down") for t in ("AAPL", "KO")})
    run = universe.score_universe(("AAPL", "KO"), journal_dir=wired.dir)
    assert (run.answered, run.failed) == (0, 2)
    assert run.exit_code == universe.EXIT_FAILED


def test_no_model_key_stops_before_any_context_is_gathered(wired, monkeypatch):
    def no_key():
        raise LLMError("FULL_MODEL_API_KEY is empty")

    monkeypatch.setattr(heartbeat, "full_model_provider", no_key)
    run = universe.score_universe(("AAPL", "KO"), journal_dir=wired.dir)
    assert run.error and "FULL_MODEL_API_KEY is empty" in run.error
    assert run.exit_code == universe.EXIT_FAILED
    assert wired.gathered == [] and wired.model.calls == []
    assert not wired.month.exists()


def test_the_time_budget_stops_new_names(wired):
    run = universe.score_universe(("AAPL", "KO"), journal_dir=wired.dir, budget_seconds=0)
    assert (run.asked, run.not_asked) == (0, 2)
    assert wired.gathered == []


class TickingClock:
    """``utc_now`` that moves one minute on at every reading."""

    def __init__(self, start: datetime, then: datetime | None = None) -> None:
        self.now = start
        self.then = then

    def __call__(self) -> datetime:
        current = self.now
        self.now = self.then if self.then is not None else self.now + timedelta(minutes=1)
        return current


#: A Monday in the universe's first week, so the next UTC day is a trading day too.
A_MONDAY = date(2027, 1, 4)


def test_no_name_is_started_after_the_cut_off_so_no_line_is_dated_the_next_day(wired, monkeypatch):
    assert universe.NO_NEW_NAME_AFTER_UTC.isoformat() == "23:15:00"
    # The run starts at 23:12; each name reads the clock to start and to write.
    clock = TickingClock(datetime(2027, 1, 4, 23, 12, tzinfo=timezone.utc))
    monkeypatch.setattr(universe, "utc_now", clock)
    run = universe.score_universe(("AAPL", "KO", "SAP", "NKE"), journal_dir=wired.dir, workers=1)
    assert run.day == A_MONDAY and run.ran is True
    assert (run.asked, run.answered, run.not_asked) == (1, 1, 3)
    assert wired.gathered == ["AAPL"]
    lines = _lines(month_file(wired.dir, datetime(2027, 1, 4, tzinfo=timezone.utc)))
    assert [line["ticker"] for line in lines] == ["AAPL"]
    assert all(datetime.fromisoformat(line["ts_utc"]).date() == A_MONDAY for line in lines)


def test_a_run_that_reaches_the_next_utc_day_starts_no_new_name(wired, monkeypatch):
    # Started at 22:00 on Monday; by the time the first name is due it is Tuesday.
    clock = TickingClock(datetime(2027, 1, 4, 22, 0, tzinfo=timezone.utc),
                         then=datetime(2027, 1, 5, 0, 1, tzinfo=timezone.utc))
    monkeypatch.setattr(universe, "utc_now", clock)
    run = universe.score_universe(("AAPL", "KO"), journal_dir=wired.dir, workers=1)
    assert run.day == A_MONDAY
    assert (run.asked, run.not_asked) == (0, 2)
    assert wired.gathered == [] and not wired.dir.exists()


def test_a_run_started_after_the_cut_off_does_nothing_and_says_why(wired, monkeypatch, nothing_may_happen):
    late = datetime(2027, 1, 5, 23, 20, tzinfo=timezone.utc)
    monkeypatch.setattr(universe, "utc_now", lambda: late)
    run = universe.score_universe(("AAPL",), journal_dir=nothing_may_happen)
    assert run.ran is False and "too late in the UTC day" in run.reason
    assert run.exit_code == universe.EXIT_OK and not nothing_may_happen.exists()
    assert universe.check(late) == {"date": "2027-01-05", "run": False, "reason": run.reason}
    assert universe.check(late.replace(hour=23, minute=14))["run"] is True


# --------------------------------------------------------------------------- #
# The cost cap
# --------------------------------------------------------------------------- #


def test_the_cap_stops_asking_and_the_cli_exits_3(wired, monkeypatch, capsys):
    wired.model.usage = THIRTY_CENTS
    names = ("AAPL", "ABBV", "ABT", "ADBE", "AMD", "AMZN", "KO", "SAP")
    monkeypatch.setattr(su, "TICKERS", names)
    monkeypatch.setattr(su, "JOURNAL_DIR", wired.dir)
    monkeypatch.setattr(universe, "WORKERS", 1)  # one at a time, so the count is exact
    assert universe.main([]) == universe.EXIT_CAP_REACHED
    summary = json.loads(capsys.readouterr().out)
    # 0.30, 0.60, 0.90: still under $1, so a fourth call starts; then no more.
    assert (summary["asked"], summary["answered"], summary["not_asked"]) == (4, 4, 4)
    assert summary["cap_reached"] is True and summary["cap_usd"] == 1.0
    assert summary["cost_usd"] == pytest.approx(4 * THIRTY_CENTS.cost_usd)
    assert summary["estimated_usd"] == pytest.approx(8 * universe.ESTIMATED_COST_PER_NAME_USD, abs=1e-4)
    assert len(_lines(wired.month)) == 4
    assert wired.gathered == list(names[:4])  # nothing is even gathered past the cap


def test_the_cap_counts_what_was_already_spent_today(wired):
    yesterday = A_DAY_ON - timedelta(days=1)
    wired.dir.mkdir(parents=True)
    with wired.month.open("w", encoding="utf-8") as handle:
        for when, cost in ((yesterday, 5.0), (A_DAY_ON - timedelta(hours=2), 0.6),
                           (A_DAY_ON - timedelta(hours=1), 0.45)):
            handle.write(json.dumps({"ts_utc": when.isoformat(), "ticker": "OLD", "signal": None,
                                     "error": "x", "usage": {"cost_usd": cost}}) + "\n")
        handle.write("not json\n")
    run = universe.score_universe(("AAPL", "KO"), journal_dir=wired.dir)
    assert run.cap_reached is True and run.exit_code == universe.EXIT_CAP_REACHED
    assert (run.asked, run.not_asked) == (0, 2)
    assert run.cost_usd == pytest.approx(1.05)  # yesterday's $5 is not today's
    assert wired.model.calls == []


def test_with_four_workers_the_cap_holds_up_to_the_calls_in_flight(wired):
    wired.model.usage = THIRTY_CENTS
    names = su.TICKERS[:20]
    run = universe.score_universe(names, journal_dir=wired.dir, workers=4)
    assert run.cap_reached is True and run.exit_code == universe.EXIT_CAP_REACHED
    # A call starts only while spent + in flight is under $1, so at most three
    # finished calls ($0.90) plus four in flight: never more than seven.
    assert 4 <= run.asked <= 7
    assert run.cost_usd == pytest.approx(run.asked * THIRTY_CENTS.cost_usd)
    assert run.asked + run.not_asked == len(names)
    assert len(_lines(wired.month)) == run.asked


def test_the_guard_reserves_under_a_lock_and_settles_the_real_cost():
    guard = universe.CostGuard(1.0, spent_usd=0.5, per_name_usd=0.2)
    assert guard.reserve() and guard.reserve()           # 0.5, then 0.7 held: both under $1
    assert guard.reserve()                               # 0.9 is still under $1
    assert not guard.reserve() and guard.cap_reached     # 1.1 is not
    assert guard.asked == 3
    for _ in range(3):
        guard.settle(0.05)                               # cheaper than the estimate
    assert guard.spent_usd == pytest.approx(0.65)
    assert guard.has_room()                              # the estimates are released
    fresh = universe.CostGuard(1.0, spent_usd=0.6, per_name_usd=0.2)
    assert fresh.has_room() and not fresh.cap_reached


def test_an_unpriced_answer_is_charged_at_the_estimate():
    assert universe.charged_usd({"cost_usd": 0.004}) == 0.004
    assert universe.charged_usd({"cost_usd": None}) == universe.ESTIMATED_COST_PER_NAME_USD
    assert universe.charged_usd({"model": "unknown"}) == universe.ESTIMATED_COST_PER_NAME_USD
    assert universe.charged_usd({"cost_usd": True}) == universe.ESTIMATED_COST_PER_NAME_USD
    assert universe.charged_usd(None) == 0.0
    # A call that failed with no usage is still billed for what it generated.
    assert universe.charged_usd(None, asked=True) == universe.ESTIMATED_COST_PER_NAME_USD


def test_a_call_that_failed_counts_against_the_cap_today_and_on_a_re_run(wired):
    wired.failing_context.add("KO")
    wired.model.behaviour["SAP"] = LLMError("the request timed out after 480 seconds")
    run = universe.score_universe(("AAPL", "KO", "SAP"), journal_dir=wired.dir)
    # AAPL is priced; SAP failed with no usage, so it is charged the estimate;
    # KO never reached the model, so it costs nothing.
    expected = CHEAP.cost_usd + universe.ESTIMATED_COST_PER_NAME_USD
    assert run.cost_usd == pytest.approx(expected)
    assert universe.day_lines(wired.dir, A_DAY_ON.date()).spent_usd == pytest.approx(expected)


def test_the_days_lines_read_only_today(tmp_path):
    directory = tmp_path / "u"
    directory.mkdir()
    day = date(2027, 2, 1)
    path = month_file(directory, datetime(2027, 2, 1, tzinfo=timezone.utc))
    rows = [
        {"ts_utc": "2027-02-01T18:31:00+00:00", "ticker": "AAPL", "signal": {"bias": "BULLISH"}, "error": None,
         "usage": {"cost_usd": 0.01}},
        {"ts_utc": "2027-02-01T18:32:00+00:00", "ticker": "KO", "signal": None, "error": "down", "usage": None},
        {"ts_utc": "2027-02-02T18:31:00+00:00", "ticker": "SAP", "signal": {"bias": "BEARISH"}, "error": None,
         "usage": {"cost_usd": 0.02}},
    ]
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\n[1, 2]\n", encoding="utf-8")
    seen = universe.day_lines(directory, day)
    # KO's failed call carries no usage: it is charged the estimate.
    assert seen.spent_usd == pytest.approx(0.01 + universe.ESTIMATED_COST_PER_NAME_USD)
    assert seen.answered == frozenset({"AAPL"})
    assert universe.day_lines(tmp_path / "missing", day) == universe.DayLines()


# --------------------------------------------------------------------------- #
# The workflow
# --------------------------------------------------------------------------- #


def _workflow() -> dict:
    return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))


def _steps(job: str = "score") -> list[dict]:
    return _workflow()["jobs"][job]["steps"]


def _step(name: str, job: str = "score") -> dict:
    return next(s for s in _steps(job) if s.get("name") == name)


#: What the scoring step may hold: the model's key (every spelling the
#: production chain tries), the news, the keyed sources, the phone topic.
ALLOWED_SECRETS = {
    "ANTHROPIC_API_KEY", "BRIGHTDATA_API_TOKEN", "EIA_API_KEY", "USDA_NASS_KEY", "FRED_API_KEY",
    "FINNHUB_API_KEY", "FULL_MODEL_API_KEY", "DEEPINFRA_API_KEY", "SCREENING_API_KEY",
    "GEMINI_API_KEY", "GOOGLE_API_KEY", "GROQ_API_KEY", "NTFY_TOPIC",
}

#: The production cycle step's entries the scoring step copies, unchanged.
COPIED_FROM_THE_CYCLE = {
    "ANTHROPIC_API_KEY", "BRIGHTDATA_API_TOKEN", "BRIGHTDATA_SERP_ZONE", "EIA_API_KEY",
    "USDA_NASS_KEY", "FRED_API_KEY", "FINNHUB_API_KEY", "FULL_MODEL_API_KEY",
}


def test_the_workflow_holds_no_broker_key_and_no_webhook_secret():
    text = WORKFLOW.read_text(encoding="utf-8")
    named = set(re.findall(r"secrets\.([A-Z0-9_]+)", text))
    assert named <= ALLOWED_SECRETS, sorted(named - ALLOWED_SECRETS)
    code = json.dumps(_workflow()).upper()  # everything but the comments
    for word in ("ALPACA", "APCA", "WEBHOOK", "SUPABASE", "EXECUTION_MODE"):
        assert word not in code, word
    for job in _workflow()["jobs"].values():
        for step in job["steps"]:
            for key in step.get("env") or {}:
                assert "ALPACA" not in key and "WEBHOOK" not in key, key
    # The verify job holds no secret at all.
    assert "secrets." not in json.dumps(_workflow()["jobs"]["verify"])


def test_the_scoring_step_gets_exactly_the_cycle_s_model_news_and_source_keys():
    cycle = next(s for s in yaml.safe_load((ROOT / ".github/workflows/heartbeat.yml").read_text())
                 ["jobs"]["cycle"]["steps"] if s.get("name") == "Run one cycle")["env"]
    score = _step("Score the universe")["env"]
    assert set(score) - {"LIMIT"} == COPIED_FROM_THE_CYCLE
    for key in COPIED_FROM_THE_CYCLE:
        assert score[key] == cycle[key], key
    for spellings in sources.KEY_ENV_VARS.values():
        assert spellings[0] in score


def test_the_workflow_runs_after_each_production_run_on_weekdays_and_by_hand():
    wf = _workflow()
    triggers = wf.get("on") or wf[True]
    assert set(triggers) == {"workflow_run", "schedule", "workflow_dispatch"}
    heartbeat_wf = yaml.safe_load((ROOT / ".github/workflows/heartbeat.yml").read_text(encoding="utf-8"))
    assert triggers["workflow_run"] == {"workflows": [heartbeat_wf["name"]], "types": ["completed"]}
    (cron,) = [entry["cron"] for entry in triggers["schedule"]]
    assert cron.split()[-1] == "1-5"
    assert wf["permissions"] == {"contents": "write"}
    assert wf["concurrency"]["group"] == "shadow-universe"


def test_the_workflow_checks_before_it_scores_and_skips_everything_after():
    steps = _steps()
    names = [s.get("name") for s in steps]
    check_at = names.index("Would it run today?")
    assert "python -m orchestrator.universe --check" in steps[check_at]["run"]
    assert "GITHUB_OUTPUT" in steps[check_at]["run"]
    assert not steps[check_at].get("env")  # the check needs no key
    for step in steps[check_at + 1:]:
        assert "steps.check.outputs.run == 'yes'" in step["if"] or "steps.score.outputs" in step["if"], step["name"]
    score = _step("Score the universe")
    assert score["if"] == "steps.check.outputs.run == 'yes'"
    assert "python -m orchestrator.universe" in score["run"] and '"$status" = "3"' in score["run"]
    commit = _step("Commit the lines")
    assert "git add -f logs/shadow_universe/" in commit["run"]
    assert "git pull --rebase" in commit["run"] and "for attempt in" in commit["run"]


def test_the_cap_alert_is_fixed_words_through_the_topic_secret():
    alert = _step("Tell the owner's phone the cost cap stopped the run")
    assert alert["if"] == "always() && steps.score.outputs.cap == 'yes'"
    assert alert["env"]["NTFY_TOPIC"] == "${{ secrets.NTFY_TOPIC }}"
    run = alert["run"]
    assert '"topic": os.environ["NTFY_TOPIC"]' in run
    assert "https://ntfy.sh/ " in run and "ntfy.sh/$" not in run
    words = " ".join(re.findall(r'"([^"]*)"', re.search(r'"message": \((.*?)\),', run, re.S).group(1)))
    cap = f"${su.DAILY_COST_CAP_USD:g}"
    assert cap in words
    assert re.findall(r"\d", words.replace(cap, "")) == []  # no number but the cap


def test_every_tee_step_sets_pipefail():
    """The CI rule ("A piped script cannot report a false green"), for this file."""
    text = WORKFLOW.read_text(encoding="utf-8")
    for block in re.split(r"\n\s*- name:", text):
        lines = [line.strip() for line in block.splitlines()]
        pipes = [i for i, line in enumerate(lines)
                 if not line.startswith("#") and re.search(r"\|\s*tee\b", re.sub(r"""(['"]).*?\1""", "", line))]
        if pipes:
            assert any(re.match(r"set\s+-[a-z]*o\s+pipefail\b", line) for line in lines[:max(pipes)])


def test_the_job_clock_outlasts_the_budget_and_one_slow_name():
    """Derived from the constants, so a longer budget or timeout fails here
    instead of killing a run before its lines are committed."""
    clock = _workflow()["jobs"]["score"]["timeout-minutes"]
    worst_call = llm.FULL_MODEL_TIMEOUT_SECONDS + llm.TRANSPORT_RETRY_TIMEOUT_SECONDS
    slowest_name = llm.SCHEMA_ATTEMPTS * worst_call / 60 + 5   # plus its context
    setup_and_commit = 10
    assert clock >= universe.RUN_BUDGET_SECONDS / 60 + slowest_name + setup_and_commit
    assert clock <= 360  # GitHub's own ceiling for a job


def test_the_verify_run_checks_every_name_without_a_model():
    wf = _workflow()
    assert wf["jobs"]["verify"]["if"] == "${{ inputs.verify }}"
    assert wf["jobs"]["score"]["if"] == "${{ !inputs.verify }}"
    assert wf["jobs"]["verify"]["permissions"] == {"contents": "read"}
    run = _step("Does every name resolve?", "verify")["run"]
    assert "from backtest.verify_tickers import check" in run and "TICKERS" in run
    assert "orchestrator" not in run
