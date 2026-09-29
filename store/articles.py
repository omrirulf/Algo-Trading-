#!/usr/bin/env python3
"""The article archive: the articles behind a cycle's news, kept privately for a later test.

    python -m store.articles                 # the latest cycle not archived yet
    python -m store.articles --cycle 36584368928
    python -m store.articles --no-upload     # fetch and count only; store nothing
    python -m store.articles --dry-run       # which links; no network

The owner's decision of 29 Sep 2026, after the article probe
(``docs/article-probe.mdx``): do not hand the model article text yet, but
start saving it, so the first checkpoint (2026-12-22) can test on many days
whether the model would have done better with it. After each cycle:

* for each company (not a fund) the cycle asked about,
* each news result whose headline or snippet names the company,
* the page behind it is fetched through the Web Unlocker zone the news fetch
  uses, and the story is cut out of it (``orchestrator/article_text.py``);
* its first ``KEEP_WORDS`` words go, one JSON line per article, into one
  xz-compressed object per cycle in the archive's private Storage bucket,
  under ``articles/``.

What it is not:

* **Shown to the model.** Nothing in the cycle reads it; the prompt is
  unchanged, so the race is untouched.
* **In the repository.** The repository is public and the articles are other
  people's work, so their text goes only to the private bucket: never to
  git, a workflow artifact or a log line. What this prints, and the workflow
  commits to ``logs/article_archive.jsonl``, is one line of counts per cycle
  with the object's path, size and SHA-256.
* **In the cycle.** It runs after the heartbeat run ends, in its own
  workflow (``.github/workflows/article-archive.yml``); it cannot slow a
  cycle down or fail one.

The pages are fetched when this runs, an hour or two after the cycle read
the headlines; each line says when. A story edited in between is kept as it
was then.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import lzma
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx  # noqa: E402

from config import journal_files  # noqa: E402
from config import settings as cfg  # noqa: E402
from config.instruments import is_fund  # noqa: E402
from orchestrator import news  # noqa: E402
from orchestrator.article_text import (  # noqa: E402
    ARTICLE, GOOGLE_REDIRECT, Extractor, Http, Page, classify, fetch_page, mentions_company, paragraphs,
    read_page, trafilatura_extract,
)
from store.remote import MODEL_IO_BUCKET, RemoteArchive, RemoteArchiveError  # noqa: E402

#: Words kept from each article. The probe hands the model the first 300;
#: keeping more lets the checkpoint try other cuts without fetching again.
KEEP_WORDS = 1000
#: Pages in flight at once, as the probe fetches them.
FETCH_WORKERS = 4
#: At most this many pages a cycle. A cycle has had 72 to 106.
MAX_PAGES = 200
#: No new page is started after this long; the rest are counted as not fetched.
TIME_BUDGET_SECONDS = 25 * 60

#: The one line per cycle the workflow commits: counts, never text.
INDEX_PATH = cfg.LOG_DIR / "article_archive.jsonl"
#: Where in the private bucket the objects go: ``articles/YYYY/MM/YYYY-MM-DD/<cycle>.jsonl.xz``.
OBJECT_PREFIX = "articles"
#: The same fixed xz settings as the model calls' objects (store/model_calls.py):
#: xz writes no timestamp, so the same lines always make the same bytes.
XZ_PRESET = 9
MEDIA_TYPE = "application/x-xz"

_SAFE_CYCLE = re.compile(r"[^A-Za-z0-9._-]")


@dataclass(frozen=True)
class Link:
    """One news result worth fetching: a company's, naming the company, pointing at a story."""

    ticker: str
    ts_utc: str
    index: int
    source: str
    headline: str
    url: str


# --------------------------------------------------------------------------- #
# Which cycle, and which of its links
# --------------------------------------------------------------------------- #


def cycle_of(line: dict) -> str:
    """The heartbeat run a journal line came from; its day when the line predates the field."""
    run = line.get("run") if isinstance(line.get("run"), dict) else {}
    run_id = str(run.get("run_id") or "").strip()
    return _SAFE_CYCLE.sub("", run_id) or f"day-{str(line.get('ts_utc') or '')[:10]}"


def cycles(lines: Iterable[str]) -> dict[str, list[dict]]:
    """The journal's lines that carry news, by cycle, in journal order."""
    out: dict[str, list[dict]] = {}
    for raw in lines:
        try:
            line = json.loads(raw)
        except ValueError:
            continue
        context = line.get("context") if isinstance(line, dict) else None
        if not isinstance(context, dict) or not context.get("sources") or not line.get("ticker"):
            continue
        out.setdefault(cycle_of(line), []).append(line)
    return out


def archived(index_lines: Iterable[str]) -> set[str]:
    """The cycles the index already has a stored object for."""
    done = set()
    for raw in index_lines:
        try:
            row = json.loads(raw)
        except ValueError:
            continue
        if isinstance(row, dict) and row.get("ok") and row.get("object"):
            done.add(str(row.get("cycle") or ""))
    return done


def links_of(lines: list[dict], limit: int = MAX_PAGES) -> list[Link]:
    """The results to fetch: a company's, whose headline or snippet names it, with a story behind it.

    A fund's results are left out (the probe found them mostly about
    something else), and so is any result that never names the company:
    a story about another company is noise the checkpoint does not need.
    One ticker's repeated link is fetched once.
    """
    out: list[Link] = []
    for line in lines:
        ticker = str(line.get("ticker") or "").upper()
        if not ticker or is_fund(ticker):
            continue
        seen: set[str] = set()
        for index, item in enumerate(line["context"]["sources"]):
            if not isinstance(item, dict):
                continue
            url = news.absolute_url(str(item.get("url") or ""))
            title = str(item.get("title") or "")
            if classify(url) not in (ARTICLE, GOOGLE_REDIRECT) or url in seen:
                continue
            if not mentions_company(f"{title} {item.get('snippet') or ''}", ticker):
                continue
            seen.add(url)
            out.append(Link(ticker=ticker, ts_utc=str(line.get("ts_utc") or ""), index=index,
                            source=str(item.get("source") or ""), headline=title, url=url))
    return out[:limit]


# --------------------------------------------------------------------------- #
# Fetching, reading, packing
# --------------------------------------------------------------------------- #


def fetch_links(
    http: Http, token: str, zone: str, links: list[Link], *, workers: int = FETCH_WORKERS,
    budget: float = TIME_BUDGET_SECONDS, clock: Callable[[], float] = time.monotonic,
    now: Callable[[], datetime] = lambda: datetime.now(timezone.utc),
) -> list[tuple[Page, str]]:
    """Each link's page and the moment it was asked for. Never raises; stops starting pages at ``budget``."""
    started = clock()

    def one(link: Link) -> tuple[Page, str]:
        stamp = now().isoformat(timespec="seconds")
        if clock() - started > budget:
            page = Page(index=link.index, source=link.source, url=link.url, kind=classify(link.url))
            page.error = "not fetched: the time budget ran out"
            return page, stamp
        return fetch_page(http, token, zone, link.index, link.source, link.url), stamp

    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        return list(pool.map(one, links))


def kept(page: Page, limit: int = KEEP_WORDS) -> tuple[list[str], int]:
    """The article's paragraphs up to ``limit`` words, and how many words that is."""
    out: list[str] = []
    count = 0
    for paragraph in paragraphs(page.text, page.title) if page.text else []:
        room = limit - count
        if room <= 0:
            break
        words = paragraph.split()[:room]
        out.append(" ".join(words))
        count += len(words)
    return out, count


def record(cycle: str, link: Link, page: Page, fetched_at: str) -> dict[str, Any]:
    """One article, as the archive keeps it. The page's HTML is not kept."""
    parts, count = kept(page)
    return {
        "cycle": cycle, "ticker": link.ticker, "ts_utc": link.ts_utc, "index": link.index,
        "source": link.source, "headline": link.headline, "url": link.url,
        "final_url": page.final_url, "fetched_at": fetched_at, "status": page.status,
        "error": page.error, "page_bytes": page.page_bytes, "seconds": round(page.seconds, 1),
        "title": page.title, "date": page.date,
        "article_words": len(page.text.split()) if page.text else 0,
        "kept_words": count, "paragraphs": parts,
        "paywall_suspected": page.paywall, "names_the_company": page.mentions,
    }


def pack(records: list[dict[str, Any]]) -> bytes:
    """The records as JSON lines, xz-compressed with fixed settings."""
    body = "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in records)
    return lzma.compress(body.encode("utf-8"), format=lzma.FORMAT_XZ, check=lzma.CHECK_CRC64, preset=XZ_PRESET)


def object_path(cycle: str, day: str) -> str:
    return f"{OBJECT_PREFIX}/{day[:4]}/{day[5:7]}/{day}/{cycle}.jsonl.xz"


def failure_kind(record: dict[str, Any]) -> Optional[str]:
    """Why an article has no text, in a few words; None when it has text."""
    if record["kept_words"]:
        return None
    error = str(record.get("error") or "")
    if error.startswith("HTTP "):
        return " ".join(error.split()[:2])
    if error.startswith("not fetched"):
        return "out of time"
    if error:
        return error.split(":")[0][:40]
    return "no article text on the page"


def summary(cycle: str, day: str, lines: list[dict], links: list[Link], records: list[dict],
            **extra: Any) -> dict[str, Any]:
    """The index line: counts only. No article text, no headline, no link."""
    with_text = [r for r in records if r["kept_words"]]
    return {
        "ts_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "cycle": cycle, "cycle_day": day,
        "companies": len({str(l.get("ticker") or "").upper() for l in lines
                          if l.get("ticker") and not is_fund(str(l.get("ticker")))}),
        "links": len(links),
        "with_text": len(with_text),
        "words_kept": sum(r["kept_words"] for r in records),
        "names_the_company": sum(1 for r in with_text if r["names_the_company"]),
        "paywall_suspected": sum(1 for r in with_text if r["paywall_suspected"]),
        "no_text": dict(Counter(k for k in (failure_kind(r) for r in records) if k).most_common()),
        **extra,
    }


# --------------------------------------------------------------------------- #
# The command line
# --------------------------------------------------------------------------- #


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Save the articles behind a cycle's news to the private archive.")
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH)
    parser.add_argument("--index", type=Path, default=INDEX_PATH,
                        help="the committed index of archived cycles (read only; the workflow appends)")
    parser.add_argument("--cycle", default="", help="archive this cycle (its heartbeat run id); default: the latest")
    parser.add_argument("--no-upload", action="store_true", help="fetch and count, but store nothing")
    parser.add_argument("--dry-run", action="store_true", help="say which links would be fetched; no network")
    return parser.parse_args(argv)


def run(
    args: argparse.Namespace, *, http: Optional[Http] = None, archive: Optional[RemoteArchive] = None,
    token: str = "", zone: str = "", extract: Extractor = trafilatura_extract,
    say: Callable[[str], None] = lambda text: print(text, file=sys.stderr),
    fetch_kwargs: Optional[dict] = None,
) -> tuple[Optional[dict[str, Any]], int]:
    """``(index line or None, exit code)``. The line is None when there is nothing new to archive."""
    by_cycle = cycles(journal_files.iter_lines(args.journal))
    if not by_cycle:
        say("the journal has no cycle with news to archive")
        return None, 0
    wanted = _SAFE_CYCLE.sub("", args.cycle.strip())
    if wanted and wanted not in by_cycle:
        say(f"no cycle {wanted} in the journal")
        return None, 1
    cycle = wanted or list(by_cycle)[-1]
    lines = by_cycle[cycle]
    day = min(str(l.get("ts_utc") or "") for l in lines)[:10]
    index_lines = args.index.read_text(encoding="utf-8").splitlines() if args.index.exists() else []
    if not wanted and cycle in archived(index_lines):
        say(f"cycle {cycle} ({day}) is already archived; nothing to do")
        return None, 0

    links = links_of(lines)
    say(f"cycle {cycle} ({day}): {len(links)} link(s) naming the company, from "
        f"{len({l.ticker for l in links})} companies")
    if args.dry_run:
        for link in links:
            say(f"  {link.ticker:<6} #{link.index + 1:<2} {link.source[:24]:<24} {link.url[:90]}")
        return None, 0
    if not token or not zone:
        return summary(cycle, day, lines, links, [], ok=False,
                       error="no Bright Data token or zone: set BRIGHTDATA_API_TOKEN"), 1
    if not args.no_upload and archive is None:
        return summary(cycle, day, lines, links, [], ok=False,
                       error="no archive configured: set SUPABASE_URL and SUPABASE_SERVICE_KEY"), 1

    fetched = fetch_links(http or Http(), token, zone, links, **(fetch_kwargs or {}))
    records = [record(cycle, link, read_page(page, link.ticker, KEEP_WORDS, extract), stamp)
               for link, (page, stamp) in zip(links, fetched)]
    data = pack(records)
    path = object_path(cycle, day)
    extra: dict[str, Any] = {"object": f"{MODEL_IO_BUCKET}/{path}", "bytes": len(data),
                             "sha256": hashlib.sha256(data).hexdigest()}
    if args.no_upload:
        return summary(cycle, day, lines, links, records, **extra, stored=None, ok=True, error=""), 0
    try:
        stored = archive.upload_object(MODEL_IO_BUCKET, path, data, MEDIA_TYPE)
    except (RemoteArchiveError, httpx.HTTPError) as exc:
        return summary(cycle, day, lines, links, records, **extra, stored=False, ok=False,
                       error=f"upload failed: {exc}"[:300]), 1
    return summary(cycle, day, lines, links, records, **extra, stored=stored, ok=True, error=""), 0


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    token = zone = ""
    archive = None
    if not args.dry_run:
        from config.settings import get_settings

        settings = get_settings()
        token = news.resolve_token(settings.brightdata_api_token) or ""
        zone = news.resolve_zone(settings.brightdata_serp_zone, settings.brightdata_unlocker_zone)
        if not args.no_upload and RemoteArchive.is_configured():
            archive = RemoteArchive.from_settings()
    line, code = run(args, archive=archive, token=token, zone=zone)
    if line is not None:
        print(json.dumps(line, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
