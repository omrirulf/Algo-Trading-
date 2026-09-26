"""What the Supabase starter did today: read from its log, only the status code kept.

The heartbeat reads ``public.starter_log`` read-only before the book snapshot
(``store/starter_status.py``) and commits the answer as
``logs/starter_status.json``. It must never fail the run, never print the
key, and never pass on more than a status code and a short, checked error.
"""

from __future__ import annotations

import json
from datetime import date

import httpx
import pytest

from store import starter_status
from store.remote import RemoteArchive
from tests.test_store_push_remote import KEY, URL, configured, unconfigured, wire  # noqa: F401

DAY = date(2026, 9, 28)


def row(**over):
    base = {"requested_at": "2026-09-28T14:40:00.123+00:00", "source": "supabase-cron",
            "request_id": 17, "status_code": 204, "error": None}
    base.update(over)
    return base


def test_todays_request_is_the_status_code_and_nothing_else():
    status = starter_status.status_from_rows([row()], DAY)
    assert status == {"day": "2026-09-28", "requested_at": "2026-09-28T14:40:00+00:00",
                      "status_code": 204, "error": None}


def test_the_newest_request_today_wins_and_other_days_are_ignored():
    rows = [row(requested_at="2026-09-27T14:40:00+00:00", status_code=401),
            row(requested_at="2026-09-28T14:40:00+00:00", status_code=401),
            row(requested_at="2026-09-28T15:10:00Z", status_code=204),
            row(requested_at="not a time", status_code=500),
            row(source="someone-else", requested_at="2026-09-28T16:00:00Z", status_code=500),
            "junk", None]
    status = starter_status.status_from_rows(rows, DAY)
    assert (status["requested_at"], status["status_code"]) == ("2026-09-28T15:10:00+00:00", 204)


def test_no_request_today_is_unknown_with_a_reason():
    assert starter_status.status_from_rows([], DAY) == {
        "day": "2026-09-28", "status": "unknown", "why": "the starter recorded no request today"}
    assert starter_status.status_from_rows("not a list", DAY)["status"] == "unknown"


def test_an_unanswered_request_says_so_and_a_timeout_keeps_its_short_text():
    assert starter_status.status_from_rows([row(status_code=None)], DAY)["status_code"] is None
    timed_out = starter_status.status_from_rows([row(status_code=None, error="Timeout of 10000 ms reached")], DAY)
    assert timed_out["error"] == "Timeout of 10000 ms reached"
    assert starter_status.status_from_rows([row(status_code=True)], DAY)["status_code"] is None


@pytest.mark.parametrize("text", [
    # Credential-shaped strings assembled at runtime, so no secret scanner
    # mistakes this file for a leak.
    "Authorization: Bearer abc", "failed with " + "gh" + "p_abcdefghijklmnop", "github" + "_pat_11AAAA",
    "apikey=" + "eyJ" + "hbGciOiJIUzI1",
])
def test_an_error_that_looks_like_it_holds_a_credential_is_withheld_whole(text):
    cleaned = starter_status.clean_error(text)
    assert cleaned == "error text withheld: it looked like it held a credential"


def test_a_long_or_multi_line_error_is_one_short_line():
    cleaned = starter_status.clean_error("line one\nline two " + "x" * 400)
    assert "\n" not in cleaned and len(cleaned) == starter_status.MAX_ERROR_CHARS


def test_it_asks_for_todays_rows_with_the_one_reader_of_the_key(configured, monkeypatch, capsys):
    seen = wire(monkeypatch, lambda request: httpx.Response(200, json=[row()]))
    assert starter_status.main(["--day", "2026-09-28"]) == 0
    printed = capsys.readouterr()
    assert json.loads(printed.out) == {"day": "2026-09-28", "requested_at": "2026-09-28T14:40:00+00:00",
                                       "status_code": 204, "error": None}
    (request,) = seen
    assert request.method == "GET" and request.url.path == "/rest/v1/starter_log"
    params = dict(request.url.params)
    assert params == {"select": "requested_at,source,request_id,status_code,error",
                      "requested_at": "gte.2026-09-28T00:00:00Z", "order": "requested_at.desc", "limit": "5"}
    # The new secret key goes on apikey only (store.remote.auth_headers).
    assert request.headers["apikey"] == KEY and "authorization" not in request.headers
    assert KEY not in printed.out + printed.err


def test_missing_secrets_are_unknown_and_exit_zero(unconfigured, capsys):
    assert starter_status.main(["--day", "2026-09-28"]) == 0
    status = json.loads(capsys.readouterr().out)
    assert status["status"] == "unknown" and status["why"].startswith("not configured")


@pytest.mark.parametrize("answer, why", [
    (httpx.ConnectError("unreachable"), "project paused or unreachable"),
    (httpx.Response(540, text="paused"), "project paused or unreachable"),
    (httpx.Response(401, text="Invalid API key"), "HTTP 401"),
    (httpx.Response(404, text="relation does not exist"),
     "HTTP 404: no starter_log table (supabase/heartbeat_starter.sql not applied?)"),
])
def test_any_failure_is_unknown_with_a_few_words_never_the_servers_text(configured, monkeypatch, capsys, answer, why):
    def handler(request):
        if isinstance(answer, Exception):
            raise answer
        return answer

    wire(monkeypatch, handler)
    assert starter_status.main(["--day", "2026-09-28"]) == 0
    out = capsys.readouterr().out
    assert json.loads(out) == {"day": "2026-09-28", "status": "unknown", "why": why}
    assert KEY not in out and URL not in out


def test_even_an_unexpected_error_is_unknown(configured, monkeypatch):
    class Broken:
        def rows(self, *a, **k):
            raise ValueError("surprise")

    assert starter_status.read(DAY, archive=Broken()) == {
        "day": "2026-09-28", "status": "unknown", "why": "could not read the starter's log (ValueError)"}


def test_the_module_reads_the_key_only_through_the_one_reader():
    from pathlib import Path

    source = Path(starter_status.__file__).read_text()
    assert "supabase_service_key" not in source and "supabase_url" not in source
    assert "os.environ" not in source and "getenv" not in source
    assert "RemoteArchive.from_settings()" in source
    assert hasattr(RemoteArchive, "rows")
