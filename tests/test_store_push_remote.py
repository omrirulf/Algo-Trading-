"""The push CLI: what it sends, what it skips, and what it refuses to fail on."""

from __future__ import annotations

import json

import httpx
import pytest

from store import push_remote
from store.remote import RemoteArchive
from tests.test_store_loader import AUDIT_LINE, JOURNAL_LINE, line

URL = "https://proj.supabase.co"
#: The shape of the key the heartbeat really uses: a new-style secret key
#: ("github-archive"), sent on the apikey header only. Not a real key.
#: Assembled at runtime so no secret scanner mistakes this file for a leak.
KEY = "sb_" + "secret_" + "TESTONLY" + "0" * 24


@pytest.fixture
def configured(monkeypatch):
    from config.settings import get_settings

    settings = get_settings()
    monkeypatch.setattr(settings, "supabase_url", URL, raising=False)
    monkeypatch.setattr(settings, "supabase_service_key", KEY, raising=False)
    return settings


@pytest.fixture
def unconfigured(monkeypatch):
    from config.settings import get_settings

    settings = get_settings()
    monkeypatch.setattr(settings, "supabase_url", "", raising=False)
    monkeypatch.setattr(settings, "supabase_service_key", "", raising=False)
    return settings


def wire(monkeypatch, handler) -> list[httpx.Request]:
    """Point RemoteArchive.from_settings at a mock transport."""
    seen: list[httpx.Request] = []

    def recording(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return handler(request)

    real = RemoteArchive.from_settings

    def patched(cls=None, client=None):
        return real(client=httpx.Client(transport=httpx.MockTransport(recording)))

    monkeypatch.setattr(RemoteArchive, "from_settings", staticmethod(patched))
    return seen


def logs(tmp_path, journal_lines=2):
    journal = tmp_path / "signal_journal.log"
    audit = tmp_path / "execution_audit.log"
    journal.write_text(
        "".join(
            line({**JOURNAL_LINE, "ts_utc": f"2026-09-{15 + n:02d}T14:05:02+00:00"})
            for n in range(journal_lines)
        ),
        encoding="utf-8",
    )
    audit.write_text(line(AUDIT_LINE), encoding="utf-8")
    return journal, audit


def args(journal, audit, *extra):
    return ["--journal", str(journal), "--audit", str(audit), *extra]


# --------------------------------------------------------------------------- #
# Not configured is a state, not a failure
# --------------------------------------------------------------------------- #


def test_without_a_credential_it_does_nothing_and_succeeds(tmp_path, capsys, unconfigured):
    """A repo with no Supabase set up must not have a permanently red heartbeat."""
    journal, audit = logs(tmp_path)
    assert push_remote.main(args(journal, audit)) == 0

    out = capsys.readouterr().out
    assert "No remote archive configured" in out
    assert "local logs are unaffected" in out


def test_print_schema_needs_no_credential(capsys, unconfigured):
    assert push_remote.main(["--print-schema"]) == 0
    sql = capsys.readouterr().out
    assert "create table if not exists public.signals" in sql
    assert "enable row level security" in sql


# --------------------------------------------------------------------------- #
# Sending
# --------------------------------------------------------------------------- #


def test_it_sends_both_logs(tmp_path, capsys, configured, monkeypatch):
    def handler(request: httpx.Request) -> httpx.Response:
        if request.method == "GET":
            return httpx.Response(200, json=[])
        return httpx.Response(200, json=[{"line_hash": "x"} for _ in json.loads(request.content)])

    seen = wire(monkeypatch, handler)
    journal, audit = logs(tmp_path, journal_lines=3)

    assert push_remote.main(args(journal, audit)) == 0
    posts = [r for r in seen if r.method == "POST"]
    assert {str(r.url).split("/rest/v1/")[1].split("?")[0] for r in posts} == {
        "signals", "executions"
    }
    out = capsys.readouterr().out
    assert "signals: 3 pushed" in out
    assert "executions: 1 pushed" in out


def test_only_rows_at_or_after_the_watermark_are_sent(tmp_path, capsys, configured, monkeypatch):
    def handler(request: httpx.Request) -> httpx.Response:
        if request.method == "GET":
            return httpx.Response(200, json=[{"ts_utc": "2026-09-17T14:05:02+00:00"}])
        return httpx.Response(200, json=[{"line_hash": "x"} for _ in json.loads(request.content)])

    seen = wire(monkeypatch, handler)
    journal, audit = logs(tmp_path, journal_lines=4)  # 15th..18th

    assert push_remote.main(args(journal, audit)) == 0
    signal_post = next(r for r in seen if r.method == "POST" and "signals" in str(r.url))
    sent = json.loads(signal_post.content)
    assert [row["ts_utc"] for row in sent] == [
        "2026-09-17T14:05:02+00:00",
        "2026-09-18T14:05:02+00:00",
    ]


def test_all_ignores_the_watermark(tmp_path, capsys, configured, monkeypatch):
    def handler(request: httpx.Request) -> httpx.Response:
        if request.method == "GET":
            return httpx.Response(200, json=[{"ts_utc": "2026-09-18T14:05:02+00:00"}])
        return httpx.Response(200, json=[{"line_hash": "x"} for _ in json.loads(request.content)])

    seen = wire(monkeypatch, handler)
    journal, audit = logs(tmp_path, journal_lines=4)

    assert push_remote.main(args(journal, audit, "--all")) == 0
    assert not [r for r in seen if r.method == "GET"]  # no watermark asked for
    signal_post = next(r for r in seen if r.method == "POST" and "signals" in str(r.url))
    assert len(json.loads(signal_post.content)) == 4


def test_dry_run_sends_nothing(tmp_path, capsys, configured, monkeypatch):
    seen = wire(monkeypatch, lambda request: httpx.Response(200, json=[]))
    journal, audit = logs(tmp_path, journal_lines=3)

    assert push_remote.main(args(journal, audit, "--dry-run")) == 0
    assert not [r for r in seen if r.method == "POST"]
    assert "would send 3 of 3 rows" in capsys.readouterr().out


def test_a_missing_log_is_reported_not_fatal(tmp_path, capsys, configured, monkeypatch):
    wire(monkeypatch, lambda request: httpx.Response(200, json=[]))
    journal, audit = logs(tmp_path)
    audit.unlink()

    assert push_remote.main(args(journal, audit)) == 0
    assert "executions: nothing at" in capsys.readouterr().out


def test_a_duplicate_line_in_the_file_is_sent_once(tmp_path, configured, monkeypatch):
    def handler(request: httpx.Request) -> httpx.Response:
        if request.method == "GET":
            return httpx.Response(200, json=[])
        return httpx.Response(200, json=[{"line_hash": "x"} for _ in json.loads(request.content)])

    seen = wire(monkeypatch, handler)
    journal = tmp_path / "signal_journal.log"
    journal.write_text(line(JOURNAL_LINE) * 3, encoding="utf-8")
    audit = tmp_path / "execution_audit.log"
    audit.write_text("", encoding="utf-8")

    assert push_remote.main(args(journal, audit)) == 0
    signal_post = next(r for r in seen if r.method == "POST" and "signals" in str(r.url))
    assert len(json.loads(signal_post.content)) == 1


def test_a_truncated_line_is_skipped_rather_than_sent(tmp_path, configured, monkeypatch):
    def handler(request: httpx.Request) -> httpx.Response:
        if request.method == "GET":
            return httpx.Response(200, json=[])
        return httpx.Response(200, json=[{"line_hash": "x"} for _ in json.loads(request.content)])

    seen = wire(monkeypatch, handler)
    journal = tmp_path / "signal_journal.log"
    journal.write_text(line(JOURNAL_LINE) + '{"ts": "2026-09-15 14:0', encoding="utf-8")
    audit = tmp_path / "execution_audit.log"
    audit.write_text("", encoding="utf-8")

    assert push_remote.main(args(journal, audit)) == 0
    signal_post = next(r for r in seen if r.method == "POST" and "signals" in str(r.url))
    assert len(json.loads(signal_post.content)) == 1


# --------------------------------------------------------------------------- #
# Failure
# --------------------------------------------------------------------------- #


def test_a_refused_push_exits_non_zero_with_the_reason(tmp_path, capsys, configured, monkeypatch):
    """Loudly. The journal is already safe in git, so this can afford to fail."""
    wire(monkeypatch, lambda request: httpx.Response(404, text='{"message":"no such table"}'))
    journal, audit = logs(tmp_path)

    assert push_remote.main(args(journal, audit)) == 1
    err = capsys.readouterr().err
    assert "Remote archive push failed" in err
    assert "no such table" in err


# --------------------------------------------------------------------------- #
# --status: the push writes down how it went (26 Sep 2026)
# --------------------------------------------------------------------------- #


def _status(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_a_push_that_worked_is_recorded_as_the_last_success(tmp_path, configured, monkeypatch):
    wire(monkeypatch, lambda r: httpx.Response(200, json=[] if r.method == "GET" else [{"line_hash": "x"}]))
    journal, audit = logs(tmp_path)
    record = tmp_path / "archive_status.json"
    assert push_remote.main(args(journal, audit, "--status", str(record))) == 0
    status = _status(record)
    assert status["ok"] is True and status["error"] is None
    assert status["last_success"] == status["last_attempt"] and status["last_attempt"].endswith("+00:00")


def test_not_configured_is_recorded_and_keeps_the_last_success(tmp_path, unconfigured):
    """Not a failure of the run -- it still exits 0 -- but written down, so the
    brief can warn every day that the Supabase project will pause."""
    journal, audit = logs(tmp_path)
    record = tmp_path / "archive_status.json"
    record.write_text(json.dumps({"last_success": "2026-09-20T15:00:00+00:00", "ok": True}))
    assert push_remote.main(args(journal, audit, "--status", str(record))) == 0
    status = _status(record)
    assert (status["ok"], status["error"], status["last_success"]) == (False, "not configured",
                                                                      "2026-09-20T15:00:00+00:00")


@pytest.mark.parametrize("answer, said", [
    (httpx.ConnectError("name or service not known"), "project paused or unreachable"),
    (httpx.ReadTimeout("timed out"), "project paused or unreachable"),
    (httpx.Response(540, text="project paused"), "project paused or unreachable"),
    (httpx.Response(503, text="unavailable"), "project paused or unreachable"),
    (httpx.Response(401, text='{"message":"Invalid API key"}'), "HTTP 401"),
    (httpx.Response(404, text="no table"), "HTTP 404"),
])
def test_a_failed_push_is_classified_in_a_few_words_and_the_last_success_is_kept(
        tmp_path, configured, monkeypatch, answer, said):
    def handler(request):
        if isinstance(answer, Exception):
            raise answer
        return answer

    wire(monkeypatch, handler)
    journal, audit = logs(tmp_path)
    record = tmp_path / "archive_status.json"
    record.write_text(json.dumps({"last_success": "2026-09-20T15:00:00+00:00"}))
    assert push_remote.main(args(journal, audit, "--status", str(record))) == 1, "still fails loudly"
    status = _status(record)
    assert (status["ok"], status["error"], status["last_success"]) == (False, said, "2026-09-20T15:00:00+00:00")
    text = record.read_text()
    assert KEY not in text and URL not in text and "Invalid API key" not in text


def test_a_record_that_is_not_ours_is_not_copied_forward(tmp_path, unconfigured):
    journal, audit = logs(tmp_path)
    record = tmp_path / "archive_status.json"
    for junk in ("{broken", "[1, 2]", json.dumps({"last_success": {"nested": KEY}})):
        record.write_text(junk)
        assert push_remote.main(args(journal, audit, "--status", str(record))) == 0
        assert _status(record)["last_success"] is None


def test_a_crashed_push_still_says_so_and_still_crashes(tmp_path, configured, monkeypatch):
    journal, audit = logs(tmp_path)
    record = tmp_path / "archive_status.json"

    def boom(*a, **k):
        raise RuntimeError("the loader broke")

    monkeypatch.setattr(push_remote, "rows_from", boom)
    wire(monkeypatch, lambda r: httpx.Response(200, json=[]))
    with pytest.raises(RuntimeError):
        push_remote.main(args(journal, audit, "--status", str(record)))
    assert _status(record)["error"] == "push crashed (RuntimeError)"


def test_a_dry_run_or_no_status_flag_writes_no_record(tmp_path, configured, monkeypatch):
    wire(monkeypatch, lambda r: httpx.Response(200, json=[]))
    journal, audit = logs(tmp_path)
    record = tmp_path / "archive_status.json"
    assert push_remote.main(args(journal, audit, "--status", str(record), "--dry-run")) == 0
    assert push_remote.main(args(journal, audit)) == 0
    assert not record.exists()


def test_an_unwritable_record_never_fails_the_push(tmp_path, unconfigured, capsys):
    journal, audit = logs(tmp_path)
    assert push_remote.main(args(journal, audit, "--status", str(tmp_path / "missing" / "status.json"))) == 0
    assert "could not write the push record" in capsys.readouterr().err
