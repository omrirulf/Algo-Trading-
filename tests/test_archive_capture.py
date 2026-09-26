"""What the archive keeps of each model call, and the rules it keeps it by.

The owner's rule of 26 Sep 2026: store what cannot be got back later, and
what a result would need to be checked again -- never a secret. So, driven
through the production cycle with the real OpenAI-compatible provider over a
mock transport:

* every ask -- retries, refusals and off-schema answers included -- is
  captured with its exact request body and the response body as received,
  reasoning text and all, and the journal line carries each call's id and
  the SHA-256 of both bodies, which match the stored bodies;
* capture never fails a cycle: a capture that cannot write, or breaks, costs
  the record of a call and nothing else;
* no header and no key ever reaches a record, and a record that looks like
  it holds a credential is withheld whole (hashes kept), at capture and
  again on the way to the archive, and counted in the push status;
* the push is idempotent: the same object and the same rows a second time
  change nothing and fail nothing;
* the audit log's ``position_managed`` lines and the account snapshots reach
  the archive, and what that does to the local index is exactly one thing.
"""

from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path

import httpx
import pytest

from app.broker_client import OpenPosition
from app.execution_engine import ExecutionEngine
from config.redaction import credential_shape
from config.settings import Settings
from orchestrator import heartbeat as hb
from orchestrator import llm, model_io
from orchestrator.dispatch import DirectDispatcher
from store import database, loader, model_calls, push_remote
from store.remote import RemoteArchive
from tests.conftest import FakeBroker, FakeMarketData

ROOT = Path(__file__).resolve().parent.parent
WATCHLIST = ("NVDA", "XOM", "TLT")
#: Not a real key, and not shaped like one: only the exact-value check can
#: catch it, which is the point of the test that uses it.
KEY = "plain-provider-key-0000000000"
#: Credential shapes, assembled at runtime so no scanner reads this file as a leak.
SUPABASE_SHAPED = "sb_" + "secret_" + "TESTONLY" + "7" * 20
GITHUB_SHAPED = "gh" + "p_" + "TESTONLY" + "4" * 28
REASONING = "Momentum is positive but the news is thin; conviction stays moderate."


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def answer(ticker: str, *, reasoning: str = REASONING, content: str | None = None) -> httpx.Response:
    body = content if content is not None else json.dumps(
        {"ticker": ticker, "bias": "NEUTRAL", "conviction": 0.3, "rationale": "r"})
    return httpx.Response(200, json={
        "id": f"chatcmpl-{ticker}",
        "choices": [{"message": {"role": "assistant", "content": body, "reasoning_content": reasoning}}],
        "usage": {"prompt_tokens": 3100, "completion_tokens": 420,
                  "completion_tokens_details": {"reasoning_tokens": 300}},
    })


class Provider:
    """A scripted OpenAI-compatible endpoint: per ticker, a list of answers in order."""

    def __init__(self, script: dict[str, list]) -> None:
        self.script = {t: list(r) for t, r in script.items()}
        self.sent: list[dict] = []
        self.headers: list[dict] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content)
        self.sent.append(body)
        self.headers.append(dict(request.headers))
        ticker = body["messages"][1]["content"].split("\n", 1)[0].removeprefix("TICKER:").strip()
        step = self.script[ticker].pop(0)
        if isinstance(step, Exception):
            raise step
        return step


@pytest.fixture
def cycle(monkeypatch):
    """The production cycle, live, with the real provider over a mock endpoint."""
    monkeypatch.setattr(hb.cfg, "USE_BATCH_API", False)
    monkeypatch.setattr(hb, "get_settings", lambda: Settings(_env_file=None, watchlist=",".join(WATCHLIST)))
    monkeypatch.setattr(hb, "fetch_news", lambda t: ["news"])
    server = Provider({
        "NVDA": [answer("NVDA")],
        # Off-schema first: prose, then the re-ask with the complaint stated.
        "XOM": [answer("XOM", content="I think XOM is fine."), answer("XOM")],
        # A 503, then the retry.
        "TLT": [httpx.Response(503, text="upstream busy"), answer("TLT")],
    })
    client = httpx.Client(transport=httpx.MockTransport(server))
    monkeypatch.setattr(hb, "full_model_provider", lambda: llm.OpenAICompatibleProvider(
        "https://api.example.test/v1/openai", hb.MODEL, api_key=KEY, client=client, sleep=lambda _: None))
    return server


def run(journal_path, model_io_dir):
    broker = FakeBroker(positions=[OpenPosition("GLD", 10, 2000.0, 190.0)])
    dispatcher = DirectDispatcher(engine=ExecutionEngine(broker=broker, market_data=FakeMarketData()))
    report = hb.run_cycle(dispatcher, model_io_dir=model_io_dir)
    lines = [json.loads(line) for line in journal_path.read_text().splitlines() if line.strip()]
    return report, lines


def records(directory) -> list[dict]:
    files = model_calls.capture_files(directory)
    return [json.loads(line) for path in files for line in path.read_text().splitlines() if line.strip()]


# --------------------------------------------------------------------------- #
# The capture, and the journal's hashes of it
# --------------------------------------------------------------------------- #


def test_every_ask_is_captured_and_the_journal_hashes_match_the_bodies(cycle, _journal_to_tmp, tmp_path):
    report, lines = run(_journal_to_tmp, tmp_path / "io")
    captured = {r["call_id"]: r for r in records(tmp_path / "io")}

    # One record per HTTP ask: NVDA 1, XOM 2 (off-schema, re-ask), TLT 2 (503, retry).
    assert len(captured) == len(cycle.sent) == 5
    by_ticker = {line["ticker"]: line for line in lines}
    assert [len(by_ticker[t]["model_calls"]) for t in WATCHLIST] == [1, 2, 2]
    outcomes = {t: [captured[c["call_id"]]["outcome"] for c in by_ticker[t]["model_calls"]] for t in WATCHLIST}
    assert outcomes == {"NVDA": ["answer"], "XOM": ["off_schema", "answer"], "TLT": ["http_error", "answer"]}
    assert captured[by_ticker["TLT"]["model_calls"][0]["call_id"]]["status"] == 503
    assert captured[by_ticker["XOM"]["model_calls"][1]["call_id"]]["kind"] == "re-ask after an off-schema answer"

    for line in lines:
        for ref in line["model_calls"]:
            record = captured[ref["call_id"]]
            # The journal's hashes are the hashes of what is stored...
            assert ref["prompt_sha256"] == record["prompt_sha256"] == sha(record["request"])
            assert ref["answer_sha256"] == record["answer_sha256"] == sha(record["response"])
            assert model_calls.verify(record) == []
    # ... and what is stored is exactly what was sent, and what came back.
    sent = sorted(json.dumps(b, sort_keys=True) for b in cycle.sent)
    assert sorted(json.dumps(json.loads(r["request"]), sort_keys=True) for r in captured.values()) == sent
    answered = [r for r in captured.values() if r["outcome"] == "answer"]
    assert all(REASONING in r["response"] for r in answered)             # reasoning text kept
    assert all(r["params"]["model"] == hb.MODEL and "messages" not in r["params"] for r in captured.values())
    assert all(r["params"].get("reasoning_effort") == hb.full_model_effort() for r in captured.values())


def test_the_capture_is_one_file_per_run_named_after_the_run(cycle, _journal_to_tmp, tmp_path, monkeypatch):
    monkeypatch.setenv("HEARTBEAT_RUN", json.dumps({"run_id": "18123456789", "source": "supabase-cron"}))
    run(_journal_to_tmp, tmp_path / "io")
    (path,) = model_calls.capture_files(tmp_path / "io")
    relative = path.relative_to(tmp_path / "io").as_posix()
    year, month, day, name = relative.split("/")
    assert day.startswith(f"{year}-{month}-") and name.startswith("18123456789-") and name.endswith(".jsonl")
    assert {r["run_id"] for r in records(tmp_path / "io")} == {"18123456789"}


def test_nothing_is_captured_unless_a_cycle_opens_it(cycle, _journal_to_tmp, tmp_path):
    report, lines = run(_journal_to_tmp, None)
    assert lines and all("model_calls" not in line for line in lines)
    assert not model_io.active()


# --------------------------------------------------------------------------- #
# Capture never fails a cycle
# --------------------------------------------------------------------------- #


def _signals(lines):
    return sorted((line["ticker"], json.dumps(line.get("signal"), sort_keys=True), line.get("error")) for line in lines)


def test_a_capture_that_cannot_write_costs_the_record_not_the_cycle(cycle, _journal_to_tmp, tmp_path):
    blocked = tmp_path / "not-a-directory"
    blocked.write_text("a file where the capture directory should be")
    report, lines = run(_journal_to_tmp, blocked)
    assert len(report.completed) == len(WATCHLIST)
    assert len(lines) == len(WATCHLIST) and all("model_calls" not in line for line in lines)


def test_a_capture_that_breaks_changes_no_signal(cycle, _journal_to_tmp, tmp_path, monkeypatch):
    _, clean = run(_journal_to_tmp, None)
    _journal_to_tmp.write_text("")
    cycle.script = {"NVDA": [answer("NVDA")], "XOM": [answer("XOM", content="prose"), answer("XOM")],
                    "TLT": [httpx.Response(503), answer("TLT")]}

    def explode(*args, **kwargs):
        raise RuntimeError("the capture is broken")

    monkeypatch.setattr(model_io, "_write", explode)
    monkeypatch.setattr(model_io, "take", explode)
    report, broken = run(_journal_to_tmp, tmp_path / "io")
    assert len(report.completed) == len(WATCHLIST)
    assert _signals(broken) == _signals(clean)


def test_begin_and_finish_never_raise():
    with model_io.capture(None):
        assert model_io.begin("p", "m", {"messages": []}) is None      # nothing open: nothing recorded
    model_io.finish_attempt(None, outcome="answer")                     # and nothing to finish


# --------------------------------------------------------------------------- #
# Never a header, never a key; withheld when it looks like one
# --------------------------------------------------------------------------- #


def test_no_header_and_no_key_is_ever_captured(cycle, _journal_to_tmp, tmp_path):
    run(_journal_to_tmp, tmp_path / "io")
    assert all(h.get("authorization") == f"Bearer {KEY}" for h in cycle.headers)   # it WAS sent...
    for path in model_calls.capture_files(tmp_path / "io"):
        text = path.read_text()
        assert KEY not in text                                                     # ...and never kept
        assert "authorization" not in text.lower() and "bearer" not in text.lower()
    assert {r.get("host") for r in records(tmp_path / "io")} == {"api.example.test"}


def test_a_response_echoing_the_key_is_withheld_whole(tmp_path):
    server = Provider({"AAPL": [httpx.Response(401, text=f"invalid key {KEY}")]})
    provider = llm.OpenAICompatibleProvider("http://local/v1", "m", api_key=KEY,
                                            client=httpx.Client(transport=httpx.MockTransport(server)))
    with model_io.capture(tmp_path / "io", "1"), llm.call_label("AAPL"):
        with pytest.raises(llm.LLMError):
            provider.complete_detailed("s", "TICKER: AAPL\nu", {"type": "object"})
        refs = model_io.take("AAPL")
    (record,) = records(tmp_path / "io")
    assert KEY not in json.dumps(record)
    assert record["withheld"] == "looked like it held a credential (known credential)"
    assert record["request"] is None and record["response"] is None and "error" not in record
    # The hashes survive, so the journal's copy still names what was sent.
    assert refs == [{"call_id": record["call_id"], "prompt_sha256": record["prompt_sha256"],
                     "answer_sha256": record["answer_sha256"]}]
    assert record["prompt_sha256"] and record["answer_sha256"] == sha(f"invalid key {KEY}")


@pytest.mark.parametrize("token", [SUPABASE_SHAPED, GITHUB_SHAPED, "Bearer " + "x" * 30])
def test_a_credential_shaped_answer_is_withheld_at_capture(tmp_path, token):
    server = Provider({"AAPL": [answer("AAPL", reasoning=f"the header was {token}")]})
    provider = llm.OpenAICompatibleProvider("http://local/v1", "m", api_key="",
                                            client=httpx.Client(transport=httpx.MockTransport(server)))
    with model_io.capture(tmp_path / "io", "1"), llm.call_label("AAPL"):
        provider.complete_detailed("s", "TICKER: AAPL\nu", {"type": "object"})
    (record,) = records(tmp_path / "io")
    assert token not in json.dumps(record) and record["withheld"].startswith("looked like it held a credential")
    assert record["outcome"] == "answer" and record["answer_sha256"]


def test_news_about_an_authorization_is_not_a_credential():
    """A prompt carries headlines: the word alone must not withhold a day of prompts."""
    assert credential_shape("FDA grants Emergency Use Authorization; api key rates rise") is None
    assert credential_shape("Authorization: " + "Bearer " + "abcdefghijklmnop1234") is not None
    assert credential_shape('{"apikey": "' + "q" * 24 + '"}') is not None


def test_the_journal_s_own_context_trips_no_credential_shape():
    """The real record: every context the model was shown passes the check."""
    from config import journal_files

    hits = [json.loads(line)["ticker"] for line in journal_files.iter_lines(ROOT / "logs" / "journal")
            if credential_shape(line)]
    assert hits == []
    # Nor the fixed half of every request: the system prompts and the schema.
    assert credential_shape(hb.SYSTEM_PROMPT + hb.etf_system_prompt() + json.dumps(hb.SIGNAL_JSON_SCHEMA)) is None


def test_the_archive_side_withholds_what_the_capture_let_through(tmp_path):
    """A record written before a shape was known is caught again on the way out."""
    day = tmp_path / "io" / "2026" / "09" / "2026-09-26"
    day.mkdir(parents=True)
    leaked = {"call_id": "c1", "ts": "2026-09-26T15:00:00+00:00", "ticker": "AAPL", "provider": "p",
              "request": "{}", "response": f"here: {GITHUB_SHAPED}", "prompt_sha256": sha("{}"),
              "answer_sha256": sha(f"here: {GITHUB_SHAPED}"), "status": 200, "outcome": "answer"}
    fine = dict(leaked, call_id="c2", response="{}", answer_sha256=sha("{}"))
    (day / "1-150000.jsonl").write_text(json.dumps(leaked) + "\n" + json.dumps(fine) + "\n{cut sh")
    package = model_calls.package(day / "1-150000.jsonl", tmp_path / "io")
    assert (package.withheld, package.unreadable, len(package.rows)) == (1, 1, 2)
    stored = gzip.decompress(package.data).decode()
    assert GITHUB_SHAPED not in stored and sha(f"here: {GITHUB_SHAPED}") in stored
    assert package.object_path == "2026/09/2026-09-26/1-150000.jsonl.gz"
    assert [r["withheld"] is not None for r in package.rows] == [True, False]


# --------------------------------------------------------------------------- #
# The Anthropic path: the same rules
# --------------------------------------------------------------------------- #


def test_the_anthropic_path_keeps_the_thinking_and_never_the_key(tmp_path):
    from tests.test_llm import Block, FakeClient, Response

    signal = json.dumps({"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.7, "rationale": "r"})
    client = FakeClient(Response(content=[Block("thinking", "weighing the gap"), Block("text", signal)]))
    client.api_key = KEY
    provider = llm.AnthropicSignalProvider(api_key="", client=client)
    with model_io.capture(tmp_path / "io", "1"), llm.call_label("AAPL"):
        provider.complete_detailed("system text", "TICKER: AAPL\nu", {"type": "object"})
    (record,) = records(tmp_path / "io")
    assert record["provider"] == "anthropic" and record["outcome"] == "answer"
    assert "weighing the gap" in record["response"] and KEY not in json.dumps(record)
    sent = json.loads(record["request"])
    assert sent["messages"] == [{"role": "user", "content": "TICKER: AAPL\nu"}]
    assert sent["system"][0]["text"] == "system text" and sent["fallbacks"] == llm.FALLBACK_MODE
    assert "betas" not in sent                                  # a header, and never recorded


# --------------------------------------------------------------------------- #
# The push: idempotent, apikey only, withheld counted
# --------------------------------------------------------------------------- #

URL = "https://proj.supabase.co"
SECRET_KEY = "sb_" + "secret_" + "TESTONLY" + "0" * 24


class Supabase:
    """Enough of PostgREST and Storage to see what a push sends and what it stores."""

    def __init__(self) -> None:
        self.rows: dict[str, dict[str, dict]] = {}
        self.objects: dict[str, bytes] = {}
        self.requests: list[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        path = request.url.path
        if path.startswith("/storage/v1/object/"):
            key = path.removeprefix("/storage/v1/object/")
            if key in self.objects:
                return httpx.Response(400, json={"statusCode": "409", "error": "Duplicate",
                                                 "message": "The resource already exists"})
            self.objects[key] = request.content
            return httpx.Response(200, json={"Key": key})
        table = path.removeprefix("/rest/v1/")
        if request.method == "GET":
            return httpx.Response(200, json=[])
        key = request.url.params["on_conflict"]
        stored = self.rows.setdefault(table, {})
        fresh = [row for row in json.loads(request.content) if row[key] not in stored]
        for row in fresh:
            stored[row[key]] = row
        return httpx.Response(201, json=[{key: row[key]} for row in fresh])


@pytest.fixture
def supabase(monkeypatch):
    from config.settings import get_settings

    settings = get_settings()
    monkeypatch.setattr(settings, "supabase_url", URL, raising=False)
    monkeypatch.setattr(settings, "supabase_service_key", SECRET_KEY, raising=False)
    fake = Supabase()
    real = RemoteArchive.from_settings
    monkeypatch.setattr(RemoteArchive, "from_settings", staticmethod(
        lambda cls=None, client=None: real(client=httpx.Client(transport=httpx.MockTransport(fake)))))
    return fake


def _push(tmp_path, *extra):
    nowhere = tmp_path / "nothing"
    return push_remote.main(["--journal", str(nowhere / "j.log"), "--audit", str(nowhere / "a.log"),
                             "--account", str(nowhere / "account.jsonl"), *extra])


def test_the_model_io_push_is_idempotent_and_sends_the_key_on_apikey_only(
        cycle, _journal_to_tmp, tmp_path, supabase, capsys):
    run(_journal_to_tmp, tmp_path / "io")
    status = tmp_path / "status.json"
    args = ("--model-io", str(tmp_path / "io"), "--status", str(status))

    assert _push(tmp_path, *args) == 0
    first_objects = dict(supabase.objects)
    assert len(supabase.rows["model_calls"]) == 5 and len(supabase.rows["model_io_files"]) == 1
    (key,) = first_objects
    assert key.startswith("model-io/") and key.endswith(".jsonl.gz")

    assert _push(tmp_path, *args) == 0                       # the same push again
    out = capsys.readouterr().out
    assert "model_calls: 0 pushed, 5 already there" in out and "already there (" in out
    assert supabase.objects == first_objects                 # never overwritten
    assert json.loads(status.read_text())["ok"] is True

    uploads = [r for r in supabase.requests if r.url.path.startswith("/storage/")]
    assert len(uploads) == 2 and uploads[0].content == uploads[1].content   # same bytes both times
    for request in supabase.requests:
        assert request.headers["apikey"] == SECRET_KEY
        assert "authorization" not in request.headers        # the new key: apikey only
    assert all(r.headers["x-upsert"] == "false" and r.headers["content-type"] == "application/gzip"
               for r in uploads)

    # What Storage holds checks out against the journal, with nothing else.
    lines = [json.loads(l) for l in _journal_to_tmp.read_text().splitlines() if l.strip()]
    stored = {json.loads(l)["call_id"]: json.loads(l)
              for l in gzip.decompress(first_objects[key]).decode().splitlines()}
    for line in lines:
        for ref in line["model_calls"]:
            assert sha(stored[ref["call_id"]]["request"]) == ref["prompt_sha256"]
            assert sha(stored[ref["call_id"]]["response"]) == ref["answer_sha256"]
    # And the table holds no body at all.
    assert all("request" not in row and "response" not in row for row in supabase.rows["model_calls"].values())


def test_withheld_records_are_counted_in_the_push_status(tmp_path, supabase):
    day = tmp_path / "io" / "2026" / "09" / "2026-09-26"
    day.mkdir(parents=True)
    record = {"call_id": "c1", "ts": "2026-09-26T15:00:00+00:00", "request": "{}",
              "response": SUPABASE_SHAPED, "prompt_sha256": sha("{}"), "answer_sha256": sha(SUPABASE_SHAPED)}
    (day / "1-150000.jsonl").write_text(json.dumps(record) + "\n")
    status = tmp_path / "status.json"
    assert _push(tmp_path, "--model-io", str(tmp_path / "io"), "--status", str(status)) == 0
    assert json.loads(status.read_text())["withheld"] == 1
    assert all(SUPABASE_SHAPED.encode() not in gzip.decompress(b) for b in supabase.objects.values())


def test_a_failed_upload_fails_the_push_with_its_few_words(tmp_path, supabase, monkeypatch):
    day = tmp_path / "io" / "2026" / "09" / "2026-09-26"
    day.mkdir(parents=True)
    (day / "1-150000.jsonl").write_text(json.dumps({"call_id": "c1", "ts": "2026-09-26T15:00:00+00:00"}) + "\n")
    real = supabase.__call__

    def storage_down(request):
        if request.url.path.startswith("/storage/"):
            return httpx.Response(403, json={"message": "new keys not accepted"})
        return real(request)

    monkeypatch.setattr(Supabase, "__call__", lambda self, request: storage_down(request))
    status = tmp_path / "status.json"
    assert _push(tmp_path, "--model-io", str(tmp_path / "io"), "--status", str(status)) == 1
    written = json.loads(status.read_text())
    assert written["ok"] is False and written["error"] == "HTTP 403"
    assert "c1" in supabase.rows["model_calls"]                # the rows still went


def test_an_unsafe_object_path_is_refused():
    archive = RemoteArchive(URL, SECRET_KEY, client=httpx.Client(transport=httpx.MockTransport(
        lambda r: httpx.Response(200))))
    with pytest.raises(Exception, match="unsafe"):
        archive.upload_object("model-io", "../other-bucket/x.gz", b"", "application/gzip")


# --------------------------------------------------------------------------- #
# The account, and the ladder's lines
# --------------------------------------------------------------------------- #

ACTION_LINE = {"taskName": None, "action": {"ticker": "EMB", "action": "stop_raised", "side": "sell",
                                            "price": 93.26, "qty_closed": 0, "remaining_qty": 128,
                                            "old_stop": 94.18, "new_stop": 94.05, "order_id": "",
                                            "reason": "trailing stop"},
               "ts": "2026-09-16 18:47:56,174", "level": "INFO", "event": "position_managed"}


def test_a_position_managed_line_is_a_row_now():
    row = loader.execution_row(json.dumps(ACTION_LINE))
    assert row is not None
    assert (row["ticker"], row["status"], row["reason"], row["stop_price"], row["quantity"]) == (
        "EMB", "stop_raised", "trailing stop", 94.05, 0)
    assert row["order_id"] is None and row["ts_exact"] == 0 and row["trade_date"] == "2026-09-16"


def test_the_local_index_gains_the_ladder_lines_and_nothing_else_moves(tmp_path):
    """The one change to the local index: ``executions`` holds the ladder's
    lines too. The ``decisions`` view -- the one join on it -- is unchanged,
    because a ladder order is never an entry order a journal line records."""
    connection = database.connect_rw(tmp_path / "t.db")
    loader.load_file(connection, ROOT / "logs" / "journal", "signals")
    audit_lines = (ROOT / "logs" / "execution_audit.log").read_text().splitlines()
    kept = [l for l in audit_lines if '"position_managed"' not in l]
    before = loader.load_executions(connection, kept)
    decisions_before = connection.execute("SELECT * FROM decisions ORDER BY ts_utc, ticker").fetchall()
    after = loader.load_executions(connection, audit_lines)
    managed = len(audit_lines) - len(kept)
    assert managed > 0 and after.inserted == managed and before.skipped == after.skipped == 0
    decisions_after = connection.execute("SELECT * FROM decisions ORDER BY ts_utc, ticker").fetchall()
    assert [tuple(r) for r in decisions_after] == [tuple(r) for r in decisions_before]
    connection.close()


def test_the_account_snapshots_and_their_fills_reach_the_archive(tmp_path, supabase):
    snapshot = {"at": "2026-09-25T16:21:20Z", "sha": "abc", "mode": "cycle",
                "account": {"equity": 100873.22, "cash": 103893.04},
                "positions": [{"ticker": "ASML"}], "stops": [], "errors": [],
                "fills": [{"id": "f1", "order_id": "o1", "ticker": "lly", "side": "buy", "qty": 2.0,
                           "price": 1147.72, "at": "2026-09-16T15:57:33.647151Z"}]}
    again = dict(snapshot, at="2026-09-25T19:15:32Z", mode="protect")   # the same fill, read twice
    account = tmp_path / "account.jsonl"
    account.write_text(json.dumps(snapshot) + "\n" + json.dumps(again) + "\n")
    nowhere = tmp_path / "nothing"
    assert push_remote.main(["--journal", str(nowhere / "j"), "--audit", str(nowhere / "a"),
                             "--account", str(account), "--model-io", str(nowhere)]) == 0
    assert len(supabase.rows["account_snapshots"]) == 2
    (fill,) = supabase.rows["account_fills"].values()
    assert (fill["fill_id"], fill["ticker"], fill["price"]) == ("f1", "LLY", 1147.72)
    row = next(iter(supabase.rows["account_snapshots"].values()))
    assert row["equity"] == 100873.22 and row["positions"] == 1 and json.loads(row["raw"])["sha"] == "abc"
