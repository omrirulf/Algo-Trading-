"""The article archive must keep the right articles, privately, and nothing else.

It runs after every cycle and saves the text of the articles behind the
news results, for a checkpoint to test later. Each test below is a way it
could quietly go wrong: fetching a fund's or another company's news,
fetching a cycle twice, sending the Bright Data token anywhere but Bright
Data, or -- because the repository is public and the articles are other
people's work -- letting article text out anywhere but the private bucket.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import lzma
import math
from pathlib import Path

import pytest
import yaml

from orchestrator import article_text, news
from store import articles as sa
from store.remote import MODEL_IO_BUCKET, RemoteArchiveError

ROOT = Path(__file__).resolve().parents[1]

YAHOO = "https://finance.yahoo.com/markets/stocks/articles/novo-buyback-135000341.html"
VALERO = "https://stocktwits.com/news-articles/markets/equity/vlo-stock-best-year-1982"
QUOTE = "https://finance.yahoo.com/quote/NVO/"
GOOGLE_STUB = "/goto?url=CAESmAEB6z"
PUBLISHER = "https://www.benzinga.com/news/26/09/61806602/novo-nordisk-cuts-guidance"
FUND_NEWS = "https://www.etf.com/sections/news/iwm-small-caps-rally"

NOVO_TEXT = (
    "Novo Nordisk said on Monday it would buy back up to 5 billion kroner of shares.\n"
    "Sales of Wegovy rose 12% in the quarter, below the 15% analysts expected."
)
BENZINGA_TEXT = "Novo Nordisk cut its full-year sales guidance to growth of 8% to 11%."
GOOGLE_NOTICE = (
    "<html><head><title>Redirect Notice</title></head><body>"
    f'The page you were on is trying to send you to <a href="{PUBLISHER}">{PUBLISHER}</a></body></html>'
)

NVO_SOURCES = [
    {"title": "Novo Nordisk A/S - share repurchase programme", "snippet": "Buyback", "source": "Yahoo Finance",
     "url": YAHOO},
    {"title": "VLO Stock Heads For Best Year Since 1982", "snippet": "Valero", "source": "Stocktwits",
     "url": VALERO},
    {"title": "Novo Nordisk A/S (NVO) Stock Price, News, Quote", "snippet": "", "source": "Yahoo Finance",
     "url": QUOTE},
    {"title": "Guidance cut", "snippet": "Novo Nordisk cut its sales guidance", "source": "Benzinga",
     "url": GOOGLE_STUB},
    {"title": "Novo Nordisk A/S - share repurchase programme", "snippet": "again", "source": "Yahoo Finance",
     "url": YAHOO},
]


def line(ticker, run_id, ts, sources):
    return json.dumps({
        "ts_utc": ts, "ticker": ticker, "event": "signal_generated",
        "run": {"run_id": run_id} if run_id else None,
        "context": {"ticker": ticker, "headlines": [s["title"] for s in sources], "sources": sources},
        "signal": {"ticker": ticker, "bias": "NEUTRAL", "conviction": 0.1, "rationale": "x"},
    })


def journal(tmp_path, *lines):
    path = tmp_path / "journal.log"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def two_cycles(tmp_path):
    iwm = [{"title": "IWM small caps rally", "snippet": "IWM", "source": "ETF.com", "url": FUND_NEWS}]
    return journal(
        tmp_path,
        line("NVO", "111", "2026-09-28T14:42:00+00:00", NVO_SOURCES),
        line("NVO", "222", "2026-09-29T15:10:00+00:00", NVO_SOURCES),
        line("IWM", "222", "2026-09-29T15:12:00+00:00", iwm),
    )


class FakeResponse:
    def __init__(self, status=200, text="", headers=None):
        self.status_code = status
        self.text = text
        self.headers = headers or {}

    def json(self):
        return json.loads(self.text)


class FakeUnlocker:
    """The Unlocker's request API: serves ``pages`` by the URL in the body."""

    def __init__(self, pages):
        self.pages = pages
        self.posts: list = []

    def post(self, url, body, headers):
        self.posts.append((url, body, headers))
        status, text = self.pages.get(body["url"], (502, "<html>502 Bad Gateway</html>"))
        return FakeResponse(status, text)

    def get(self, url, headers):  # pragma: no cover - the archive only posts
        raise AssertionError(f"unexpected GET {url}")


class FakeArchive:
    def __init__(self, fail=None, exists=False):
        self.fail = fail
        self.exists = exists
        self.uploads: list = []

    def upload_object(self, bucket, path, data, content_type):
        self.uploads.append((bucket, path, data, content_type))
        if self.fail:
            raise self.fail
        return not self.exists


PAGES = {
    YAHOO: (200, NOVO_TEXT),
    news.absolute_url(GOOGLE_STUB): (200, GOOGLE_NOTICE),
    PUBLISHER: (200, BENZINGA_TEXT),
}


def plain_text(page, url):
    """A fake extractor: the 'page' is already the article's text."""
    return page, "", ""


def args_for(path, tmp_path, **kw):
    base = dict(journal=path, index=tmp_path / "article_archive.jsonl", cycle="", no_upload=False, dry_run=False)
    base.update(kw)
    return argparse.Namespace(**base)


def archive_run(tmp_path, *, archive=None, pages=PAGES, token="tok", zone="z", **kw):
    http = FakeUnlocker(pages)
    said: list = []
    result = sa.run(args_for(two_cycles(tmp_path), tmp_path, **kw), http=http,
                    archive=archive if archive is not None else FakeArchive(), token=token, zone=zone,
                    extract=plain_text, say=said.append, fetch_kwargs={"workers": 1})
    return result, http, said


# --------------------------------------------------------------------------- #
# Which cycle, which links
# --------------------------------------------------------------------------- #


def test_links_are_a_companys_results_that_name_it_and_point_at_a_story(tmp_path):
    lines = sa.cycles(two_cycles(tmp_path).read_text().splitlines())["222"]
    links = sa.links_of(lines)
    # Not the fund's result, not Valero's story, not the quote page, and the
    # repeated Yahoo link once.
    assert [(l.ticker, l.index, l.url) for l in links] == [
        ("NVO", 0, YAHOO), ("NVO", 3, news.absolute_url(GOOGLE_STUB))]


def test_the_latest_cycle_is_taken_when_none_is_named(tmp_path):
    (line_, code), http, _ = archive_run(tmp_path)
    assert code == 0 and line_["cycle"] == "222" and line_["cycle_day"] == "2026-09-29"


def test_a_cycle_already_archived_is_not_fetched_again(tmp_path):
    (tmp_path / "article_archive.jsonl").write_text(
        json.dumps({"cycle": "222", "ok": True, "object": "model-io/articles/x.jsonl.xz"}) + "\n")
    (line_, code), http, said = archive_run(tmp_path)
    assert line_ is None and code == 0 and not http.posts
    assert "already archived" in said[-1]


def test_a_failed_archive_is_not_counted_as_done(tmp_path):
    (tmp_path / "article_archive.jsonl").write_text(json.dumps({"cycle": "222", "ok": False}) + "\n")
    (line_, code), http, _ = archive_run(tmp_path)
    assert line_["ok"] and http.posts


def test_a_named_cycle_is_archived_even_when_the_index_has_it(tmp_path):
    (tmp_path / "article_archive.jsonl").write_text(
        json.dumps({"cycle": "111", "ok": True, "object": "model-io/articles/x.jsonl.xz"}) + "\n")
    (line_, code), http, _ = archive_run(tmp_path, cycle="111")
    assert code == 0 and line_["cycle"] == "111" and http.posts


def test_a_cycle_not_in_the_journal_is_a_clear_failure(tmp_path):
    (line_, code), http, said = archive_run(tmp_path, cycle="999")
    assert line_ is None and code == 1 and "no cycle 999" in said[-1] and not http.posts


def test_a_line_from_before_the_run_field_is_grouped_by_its_day(tmp_path):
    path = journal(tmp_path, line("NVO", None, "2026-09-22T15:00:00+00:00", NVO_SOURCES))
    assert list(sa.cycles(path.read_text().splitlines())) == ["day-2026-09-22"]


# --------------------------------------------------------------------------- #
# What is stored, and what comes out
# --------------------------------------------------------------------------- #


def test_the_text_goes_to_the_private_bucket_and_only_counts_come_out(tmp_path):
    archive = FakeArchive()
    (line_, code), http, _ = archive_run(tmp_path, archive=archive)
    assert code == 0 and line_["ok"] and line_["stored"] is True
    [(bucket, path, data, media)] = archive.uploads
    assert bucket == MODEL_IO_BUCKET and path == "articles/2026/09/2026-09-29/222.jsonl.xz"
    assert media == "application/x-xz"
    assert line_["object"] == f"{MODEL_IO_BUCKET}/{path}"
    assert line_["bytes"] == len(data) and line_["sha256"] == hashlib.sha256(data).hexdigest()

    records = [json.loads(r) for r in lzma.decompress(data).decode("utf-8").splitlines()]
    assert [(r["ticker"], r["index"]) for r in records] == [("NVO", 0), ("NVO", 3)]
    assert records[0]["paragraphs"] == NOVO_TEXT.splitlines()
    assert records[1]["final_url"] == PUBLISHER and records[1]["paragraphs"] == [BENZINGA_TEXT]
    assert all("html" not in r for r in records)
    assert all(r["form"] == "raw" for r in records) and line_["read_in_json_form"] == 0

    # The index line carries counts: no text, no headline, no link.
    printed = json.dumps(line_)
    for secret in ("Wegovy", "guidance", "buy back", "repurchase", YAHOO, PUBLISHER):
        assert secret not in printed
    assert line_["links"] == 2 and line_["with_text"] == 2 and line_["companies"] == 1


def test_the_bright_data_token_goes_only_to_bright_data(tmp_path):
    (_, code), http, _ = archive_run(tmp_path)
    assert http.posts and all(url == news.BRIGHTDATA_REQUEST_URL for url, *_ in http.posts)
    assert all(headers["Authorization"] == "Bearer tok" for *_, headers in http.posts)


def test_an_object_already_in_the_bucket_is_not_a_failure(tmp_path):
    (line_, code), _, _ = archive_run(tmp_path, archive=FakeArchive(exists=True))
    assert code == 0 and line_["ok"] and line_["stored"] is False


def test_a_failed_upload_is_reported_and_fails_the_run(tmp_path):
    (line_, code), _, _ = archive_run(tmp_path, archive=FakeArchive(fail=RemoteArchiveError("HTTP 500", 500)))
    assert code == 1 and not line_["ok"] and line_["error"].startswith("upload failed")


def test_no_upload_fetches_and_counts_but_stores_nothing(tmp_path):
    archive = FakeArchive()
    (line_, code), http, _ = archive_run(tmp_path, archive=archive, no_upload=True)
    assert code == 0 and line_["ok"] and line_["stored"] is None and http.posts and not archive.uploads


@pytest.mark.parametrize("token, zone", [("", "z"), ("tok", "")])
def test_no_token_or_zone_stops_before_any_page(tmp_path, token, zone):
    (line_, code), http, _ = archive_run(tmp_path, token=token, zone=zone)
    assert code == 1 and not line_["ok"] and "BRIGHTDATA_API_TOKEN" in line_["error"] and not http.posts


def test_no_archive_stops_before_any_page_is_paid_for(tmp_path):
    http = FakeUnlocker(PAGES)
    line_, code = sa.run(args_for(two_cycles(tmp_path), tmp_path), http=http, archive=None, token="tok",
                         zone="z", extract=plain_text, say=lambda _: None)
    assert code == 1 and "SUPABASE_URL" in line_["error"] and not http.posts


def test_a_page_the_raw_form_cannot_read_is_read_in_the_json_form(tmp_path):
    """The Yahoo case of 1 Oct 2026: the archive gets the story, and the index says how."""
    class JsonUnlocker(FakeUnlocker):
        def post(self, url, body, headers):
            if body.get("format") == "json" and body["url"] == YAHOO:
                self.posts.append((url, body, headers))
                return FakeResponse(200, json.dumps({"status_code": 200, "headers": {}, "body": NOVO_TEXT}))
            return super().post(url, body, headers)

    http = JsonUnlocker({news.absolute_url(GOOGLE_STUB): (200, GOOGLE_NOTICE), PUBLISHER: (200, BENZINGA_TEXT)})
    archive = FakeArchive()
    line_, code = sa.run(args_for(two_cycles(tmp_path), tmp_path), http=http, archive=archive, token="tok",
                         zone="z", extract=plain_text, say=lambda _: None, fetch_kwargs={"workers": 1})
    assert code == 0 and line_["with_text"] == 2 and line_["read_in_json_form"] == 1 and line_["no_text"] == {}
    records = [json.loads(r) for r in lzma.decompress(archive.uploads[0][2]).decode("utf-8").splitlines()]
    assert [(r["index"], r["form"]) for r in records] == [(0, "json"), (3, "raw")]


def test_a_page_with_no_text_is_counted_by_why(tmp_path):
    pages = {news.absolute_url(GOOGLE_STUB): (200, GOOGLE_NOTICE), PUBLISHER: (200, BENZINGA_TEXT)}
    (line_, code), _, _ = archive_run(tmp_path, pages=pages)   # Yahoo answers 502
    assert line_["with_text"] == 1 and line_["no_text"] == {"HTTP 502": 1}


def test_an_article_is_kept_to_its_first_words_paragraph_by_paragraph():
    page = article_text.Page(index=0, source="x", url=YAHOO, kind=article_text.ARTICLE,
                             text="one two three\nfour five\nsix seven eight nine")
    assert sa.kept(page, limit=6) == (["one two three", "four five", "six"], 6)
    assert sa.kept(article_text.Page(index=0, source="x", url=YAHOO, kind=article_text.ARTICLE)) == ([], 0)


def test_the_same_lines_make_the_same_object():
    records = [{"cycle": "222", "paragraphs": ["a"], "kept_words": 1}]
    assert sa.pack(records) == sa.pack(records)
    assert lzma.decompress(sa.pack(records)).decode() == json.dumps(records[0], sort_keys=True) + "\n"


def test_the_time_budget_stops_new_pages_not_the_run():
    ticks = iter([0, 0, 10_000, 10_000, 10_000])
    links = [sa.Link("NVO", "t", i, "s", "h", YAHOO) for i in range(3)]
    http = FakeUnlocker(PAGES)
    fetched = sa.fetch_links(http, "tok", "z", links, workers=1, budget=60, clock=lambda: next(ticks))
    assert fetched[0][0].status == 200
    assert [p.error for p, _ in fetched[1:]] == ["not fetched: the time budget ran out"] * 2
    assert len(http.posts) == 1


# --------------------------------------------------------------------------- #
# The command line
# --------------------------------------------------------------------------- #


def test_a_dry_run_needs_no_network_and_no_credentials(tmp_path, capsys, monkeypatch):
    path = two_cycles(tmp_path)
    monkeypatch.setattr(sa, "Http", lambda *a, **k: pytest.fail("a dry run must not build a client"))
    assert sa.main(["--journal", str(path), "--index", str(tmp_path / "i.jsonl"), "--dry-run"]) == 0
    out = capsys.readouterr()
    assert out.out == "" and "2 link(s) naming the company" in out.err and "NVO" in out.err


# --------------------------------------------------------------------------- #
# The workflow
# --------------------------------------------------------------------------- #


def _workflow() -> dict:
    return yaml.safe_load((ROOT / ".github/workflows/article-archive.yml").read_text())


def _triggers() -> dict:
    wf = _workflow()
    return wf.get("on") or wf[True]


def _steps() -> list[dict]:
    return _workflow()["jobs"]["archive"]["steps"]


def test_it_runs_after_each_heartbeat_run_on_main():
    run = _triggers()["workflow_run"]
    assert run == {"workflows": ["heartbeat"], "types": ["completed"], "branches": ["main"]}
    heartbeat = yaml.safe_load((ROOT / ".github/workflows/heartbeat.yml").read_text())
    assert heartbeat["name"] == "heartbeat"


def test_article_text_never_reaches_the_repository():
    """The repository is public: no artifact, and the only file committed is the index."""
    for step in _steps():
        assert "upload-artifact" not in step.get("uses", "")
    commit = next(s for s in _steps() if s.get("name") == "Commit the index line")
    adds = [l.strip() for l in commit["run"].splitlines() if l.strip().startswith("git add")]
    assert adds == ["git add logs/article_archive.jsonl 2>/dev/null || true"]


def test_a_pull_request_run_stores_nothing_and_commits_nothing():
    save = next(s for s in _steps() if s.get("name") == "Save the articles behind the latest cycle's news")
    assert '[ "$EVENT" = "pull_request" ] && args+=(--no-upload)' in save["run"]
    assert 'if [ "$EVENT" != "pull_request" ]; then' in save["run"]
    commit = next(s for s in _steps() if s.get("name") == "Commit the index line")
    assert "github.event_name != 'pull_request'" in commit["if"]
    assert "github.repository" in _workflow()["jobs"]["archive"]["if"]


def test_it_holds_the_bright_data_and_archive_keys_and_nothing_else():
    env = next(s for s in _steps() if s.get("name") == "Save the articles behind the latest cycle's news")["env"]
    secrets = sorted(k for k, v in env.items() if "secrets." in str(v))
    assert secrets == ["BRIGHTDATA_API_TOKEN", "SUPABASE_SERVICE_KEY", "SUPABASE_URL"]
    cycle = yaml.safe_load((ROOT / ".github/workflows/heartbeat.yml").read_text())
    cycle_env = next(s for s in cycle["jobs"]["cycle"]["steps"] if s.get("name") == "Run one cycle")["env"]
    for name in ("BRIGHTDATA_API_TOKEN", "BRIGHTDATA_SERP_ZONE"):
        assert env[name] == cycle_env[name], name


def test_inputs_reach_the_script_as_variables_never_as_shell_text():
    save = next(s for s in _steps() if s.get("name") == "Save the articles behind the latest cycle's news")
    assert "${{" not in save["run"]


def test_one_run_at_a_time():
    assert _workflow()["concurrency"] == {"group": "article-archive", "cancel-in-progress": False}


def test_the_job_outlasts_the_fetch():
    """Derived from the constants: the budget, the pages still in flight (a
    Google redirect doubles one), and five minutes to install and push."""
    minutes = (sa.TIME_BUDGET_SECONDS + 2 * article_text.UNLOCKER_TIMEOUT_SECONDS) / 60 + 5
    assert _workflow()["jobs"]["archive"]["timeout-minutes"] >= math.ceil(minutes)


def test_the_extractor_is_installed_here_and_not_in_requirements():
    runs = " ".join(s.get("run", "") for s in _steps())
    assert "trafilatura==" in runs
    assert "trafilatura" not in (ROOT / "requirements.txt").read_text()
