"""The remote archive: request shape, idempotence, and the watermark.

No test here reaches the network. Every one drives ``httpx.MockTransport``,
the same way the Bright Data tests do, so the request this would really send
is asserted rather than hoped for.
"""

from __future__ import annotations

import json

import httpx
import pytest

from store import loader, remote
from store.remote import EXECUTIONS, SIGNALS, RemoteArchive, RemoteArchiveError
from tests.test_store_loader import AUDIT_LINE, JOURNAL_LINE, line

URL = "https://proj.supabase.co"
KEY = "service-role-key"


def archive(handler) -> tuple[RemoteArchive, list[httpx.Request]]:
    seen: list[httpx.Request] = []

    def recording(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return handler(request)

    client = httpx.Client(transport=httpx.MockTransport(recording))
    return RemoteArchive(URL, KEY, client=client), seen


def ok(payload) -> httpx.Response:
    return httpx.Response(200, json=payload)


# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize(
    "url, key", [("", KEY), (URL, ""), ("", ""), ("   ", "   ")]
)
def test_a_half_configured_remote_is_refused_with_a_useful_message(url, key):
    with pytest.raises(RemoteArchiveError) as excinfo:
        RemoteArchive(url, key)
    assert "SUPABASE_URL" in str(excinfo.value)


def test_a_trailing_slash_in_the_url_does_not_double_up():
    """Supabase's dashboard shows the URL with a trailing slash; people paste it."""
    seen: list[httpx.Request] = []

    def recording(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return ok([])

    client = httpx.Client(transport=httpx.MockTransport(recording))
    RemoteArchive(f"{URL}/", KEY, client=client).latest_timestamp(SIGNALS)

    assert str(seen[0].url).startswith(f"{URL}/rest/v1/signals")


def test_is_configured_reads_the_settings(monkeypatch):
    from config.settings import get_settings

    settings = get_settings()
    monkeypatch.setattr(settings, "supabase_url", "", raising=False)
    monkeypatch.setattr(settings, "supabase_service_key", "", raising=False)
    assert RemoteArchive.is_configured() is False

    monkeypatch.setattr(settings, "supabase_url", URL, raising=False)
    monkeypatch.setattr(settings, "supabase_service_key", KEY, raising=False)
    assert RemoteArchive.is_configured() is True


# --------------------------------------------------------------------------- #
# Request shape
# --------------------------------------------------------------------------- #


def test_the_insert_is_idempotent_by_line_hash():
    """The whole design rests on a re-send being free. Pin the headers that do it."""
    remote_archive, seen = archive(lambda request: ok([{"line_hash": "a"}]))
    row = loader.signal_row(line(JOURNAL_LINE))

    remote_archive.push(SIGNALS, [row])

    (request,) = seen
    assert request.method == "POST"
    assert str(request.url).startswith(f"{URL}/rest/v1/signals")
    assert "on_conflict=line_hash" in str(request.url)
    prefer = request.headers["Prefer"]
    assert "resolution=ignore-duplicates" in prefer
    assert "return=representation" in prefer


def test_the_service_key_is_sent_both_ways_supabase_expects():
    remote_archive, seen = archive(lambda request: ok([]))
    remote_archive.latest_timestamp(SIGNALS)

    (request,) = seen
    assert request.headers["apikey"] == KEY
    assert request.headers["Authorization"] == f"Bearer {KEY}"


def test_the_row_sent_is_the_row_the_local_index_would_store():
    """One row builder, two backends. A divergence here is a silent data fork."""
    remote_archive, seen = archive(lambda request: ok([{"line_hash": "a"}]))
    row = loader.signal_row(line(JOURNAL_LINE))

    remote_archive.push(SIGNALS, [row])

    (sent,) = json.loads(seen[0].content)
    assert sent == row
    assert sent["ticker"] == "NVDA"
    assert sent["conviction"] == 0.72
    assert json.loads(sent["raw"]) == JOURNAL_LINE  # byte-exact original


def test_executions_go_to_their_own_table():
    remote_archive, seen = archive(lambda request: ok([{"line_hash": "a"}]))
    row = loader.execution_row(line(AUDIT_LINE))

    remote_archive.push(EXECUTIONS, [row])
    assert "/rest/v1/executions" in str(seen[0].url)


# --------------------------------------------------------------------------- #
# Batching and counting
# --------------------------------------------------------------------------- #


def test_a_large_push_is_split_into_batches():
    """Journal rows carry a full context each; one giant body would be refused."""
    remote_archive, seen = archive(
        lambda request: ok([{"line_hash": "x"} for _ in json.loads(request.content)])
    )
    rows = [
        loader.signal_row(line({**JOURNAL_LINE, "ts_utc": f"2026-09-15T14:{n:02d}:00+00:00"}))
        for n in range(60)
    ]
    rows *= 9  # 540 distinct-enough rows
    result = remote_archive.push(SIGNALS, rows)

    assert len(seen) == 3  # 540 rows at 200 per batch
    assert all(len(json.loads(r.content)) <= remote.BATCH_SIZE for r in seen)
    assert result.sent == 540


def test_counts_come_from_what_the_remote_stored_not_what_was_sent():
    """With duplicates ignored, "sent" and "stored" differ -- and only one is true."""
    remote_archive, _ = archive(lambda request: ok([{"line_hash": "only-one"}]))
    rows = [
        loader.signal_row(line({**JOURNAL_LINE, "ts_utc": f"2026-09-15T14:0{n}:00+00:00"}))
        for n in range(3)
    ]

    result = remote_archive.push(SIGNALS, rows)

    assert result.inserted == 1
    assert result.already_present == 2
    assert result.sent == 3
    assert "1 pushed, 2 already there" in result.describe()


def test_pushing_nothing_sends_no_request():
    remote_archive, seen = archive(lambda request: ok([]))
    result = remote_archive.push(SIGNALS, [])
    assert seen == [] and result.sent == 0


# --------------------------------------------------------------------------- #
# The watermark
# --------------------------------------------------------------------------- #


def test_the_watermark_asks_for_the_newest_row():
    remote_archive, seen = archive(lambda request: ok([{"ts_utc": "2026-09-16T14:05:02+00:00"}]))

    assert remote_archive.latest_timestamp(SIGNALS) == "2026-09-16T14:05:02+00:00"
    url = str(seen[0].url)
    assert "order=ts_utc.desc.nullslast" in url
    assert "limit=1" in url


def test_an_empty_remote_has_no_watermark():
    remote_archive, _ = archive(lambda request: ok([]))
    assert remote_archive.latest_timestamp(SIGNALS) is None


def test_selection_is_inclusive_at_the_boundary():
    """Rows share timestamps. An exclusive cut would drop a row's siblings."""
    rows = [
        {"ts_utc": "2026-09-15T14:00:00+00:00"},
        {"ts_utc": "2026-09-16T14:00:00+00:00"},
        {"ts_utc": "2026-09-16T14:00:00+00:00"},  # a sibling of the watermark
        {"ts_utc": "2026-09-17T14:00:00+00:00"},
    ]
    picked = remote.select_new(rows, "2026-09-16T14:00:00+00:00")
    assert len(picked) == 3


def test_a_row_with_no_timestamp_is_always_sent():
    """The malformed cycles are the ones worth keeping, not the ones to drop."""
    rows = [{"ts_utc": None}, {"ts_utc": "2026-09-01T00:00:00+00:00"}]
    picked = remote.select_new(rows, "2026-09-16T14:00:00+00:00")
    assert picked == [{"ts_utc": None}]


def test_no_watermark_selects_everything():
    rows = [{"ts_utc": "2026-09-15T14:00:00+00:00"}, {"ts_utc": None}]
    assert remote.select_new(rows, None) == rows


# --------------------------------------------------------------------------- #
# Failure
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("status", [401, 403, 404, 409, 500])
def test_an_http_error_carries_the_remotes_own_complaint(status):
    remote_archive, _ = archive(
        lambda request: httpx.Response(status, text='{"message":"relation does not exist"}')
    )
    with pytest.raises(RemoteArchiveError) as excinfo:
        remote_archive.latest_timestamp(SIGNALS)

    assert str(status) in str(excinfo.value)
    assert "relation does not exist" in str(excinfo.value)


def test_a_transport_failure_is_a_remote_archive_error():
    def boom(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("no route to host")

    remote_archive, _ = archive(boom)
    with pytest.raises(RemoteArchiveError):
        remote_archive.push(SIGNALS, [loader.signal_row(line(JOURNAL_LINE))])


def test_a_non_json_body_does_not_crash_the_count():
    """A proxy returning HTML on a 200 must not become a traceback."""
    remote_archive, _ = archive(lambda request: httpx.Response(200, text="<html>hi"))
    result = remote_archive.push(SIGNALS, [loader.signal_row(line(JOURNAL_LINE))])
    assert result.inserted == 0 and result.already_present == 1


# --------------------------------------------------------------------------- #
# The remote schema's security properties
# --------------------------------------------------------------------------- #


def read_remote_schema() -> str:
    from store import push_remote

    return push_remote.SCHEMA_PATH.read_text(encoding="utf-8")


def test_both_remote_tables_enable_row_level_security():
    sql = read_remote_schema().lower()
    for table in ("signals", "executions"):
        assert f"alter table public.{table} enable row level security" in sql


def test_the_schema_grants_no_policies():
    """RLS on with no policies is the design: the publishable key can do nothing.

    A policy appearing here would silently open the archive to anyone holding
    a key that is meant to be safe to publish.
    """
    sql = read_remote_schema().lower()
    assert "create policy" not in sql


def test_the_decisions_view_enforces_the_callers_permissions():
    """A view runs as its CREATOR unless told otherwise.

    Without ``security_invoker``, ``decisions`` reads straight through the RLS
    on the tables under it -- the tables closed, the view over them wide open.
    The first version of this schema shipped without it, and an anon-role probe
    read 0 rows from ``signals`` and 1 from ``decisions``. This is the
    regression test for that.
    """
    sql = read_remote_schema().lower()
    assert "alter view public.decisions set (security_invoker = on)" in sql

    # And it must come after the view exists, or the statement errors.
    assert sql.index("create or replace view public.decisions") < sql.index(
        "alter view public.decisions set (security_invoker = on)"
    )


def test_the_raw_line_is_stored_verbatim_not_as_jsonb():
    """jsonb reformats: key order, whitespace, number rendering.

    The archive's claim is that it kept what was written, so ``raw`` stays
    text and the parsed form rides alongside in a generated column.
    """
    sql = read_remote_schema().lower()
    assert "raw                text not null" in sql or "raw          text not null" in sql
    assert "generated always as (raw::jsonb) stored" in sql


def test_the_remote_key_is_the_content_hash():
    """What makes a re-send free, and therefore the whole push design work."""
    sql = read_remote_schema().lower()
    assert sql.count("line_hash          text primary key") + sql.count(
        "line_hash    text primary key"
    ) == 2


def test_the_watermark_survives_postgres_trimming_trailing_zeros():
    """Postgres renders `...02.331+00:00`; Python pads to `...02.331000+00:00`.

    The same instant, two spellings. This one happens to survive a text
    comparison too -- `0` sorts above `+` -- so it is a regression test for
    behaviour rather than evidence of a bug. The two spellings that did break
    it are below.
    """
    rows = [
        {"ts_utc": "2026-09-16T14:05:02.331000+00:00"},   # == the watermark
        {"ts_utc": "2026-09-16T14:05:03.100000+00:00"},   # after it
        {"ts_utc": "2026-09-16T14:05:01.900000+00:00"},   # before it
    ]
    picked = remote.select_new(rows, "2026-09-16T14:05:02.331+00:00")

    assert [r["ts_utc"] for r in picked] == [
        "2026-09-16T14:05:02.331000+00:00",
        "2026-09-16T14:05:03.100000+00:00",
    ]


def test_a_z_suffixed_watermark_is_understood():
    """Text comparison sends NOTHING here: "...02+00:00" >= "...02Z" is false."""
    rows = [{"ts_utc": "2026-09-16T14:05:02+00:00"}]
    assert remote.select_new(rows, "2026-09-16T14:05:02Z") == rows


def test_an_unparseable_watermark_sends_everything_rather_than_guessing():
    """Text comparison drops every timestamped row against a garbage watermark."""
    rows = [{"ts_utc": "2026-09-16T14:05:02+00:00"}, {"ts_utc": None}]
    assert remote.select_new(rows, "not-a-timestamp") == rows


def test_a_row_with_an_unparseable_timestamp_is_sent():
    """Better a duplicate the remote ignores than a line quietly dropped."""
    rows = [{"ts_utc": "garbage"}]
    assert remote.select_new(rows, "2026-09-16T14:05:02+00:00") == rows
