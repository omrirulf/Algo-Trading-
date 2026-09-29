"""The weekly risk digest: code lists earnings dates and flags operational events by fixed words.

The owner's request (27 Sep 2026), made smaller on 28 Sep 2026: flags only,
each with a link; earnings dates and headlines naming a fund closing, a
delisting, a ticker or name change, a split or a merger; no model call.
"""

from __future__ import annotations

import json
from datetime import date

import pytest

from orchestrator import digest, heartbeat

TODAY = date(2026, 10, 5)


def account(*positions, at="2026-10-05T15:00:00Z"):
    return json.dumps({"at": at, "positions": [{"ticker": t, "qty": q} for t, q in positions]})


def jline(ticker, day="2026-10-05", sources=(), earnings=None, held=True):
    return "2026-10-05 15:00:00,000 " + json.dumps({
        "ts_utc": f"{day}T15:00:00+00:00", "ticker": ticker, "held": held,
        "context": {"ticker": ticker, "sources": list(sources),
                    "fundamentals": {"next_earnings_date": earnings} if earnings else None},
    })


def src(n, title=None, url=None):
    return {"title": title or f"Headline {n}", "snippet": f"Snippet {n}", "source": "Reuters",
            "when": "1 hour ago", "url": url or f"https://news.example.com/{n}"}


def test_held_names_come_from_the_last_snapshot_with_their_side():
    lines = [account(("MSFT", 3)), account(("XLE", -5), ("NVDA", 2), ("bad name", 1), at="2026-10-05T16:00:00Z")]
    assert digest.held_names(lines) == {"NVDA": "long", "XLE": "short"}
    assert digest.held_names([]) == {}


def test_the_week_s_headlines_are_deduplicated_capped_and_numbered():
    held = {"NVDA": "long", "XLE": "short"}
    lines = [jline("NVDA", sources=[src(k) for k in range(20)]),
             jline("NVDA", day="2026-10-02", sources=[src(1)]),                       # the same link, seen earlier
             jline("XLE", day="2026-09-20", sources=[src(99)]),                       # older than the week
             jline("AAPL", sources=[src(50)]),                                        # not held
             jline("XLE", sources=[src(7, url="http://plain.example/x"), src(8, url="javascript:alert(1)")])]
    facts = digest.gather(lines, held, TODAY)
    ids = [i["id"] for i in facts["items"]]
    assert ids == [f"H{k}" for k in range(1, len(ids) + 1)]
    assert {i["ticker"] for i in facts["items"]} == {"NVDA"}           # XLE's links were not https
    assert len(facts["items"]) == digest.PER_NAME
    assert all(i["link"].startswith("https://") for i in facts["items"])
    # The newest are kept: headline 1 was first seen on 2 Oct, so it gave way.
    assert "https://news.example.com/1" not in {i["link"] for i in facts["items"]}
    few = digest.gather([jline("NVDA", sources=[src(1), src(2)]),
                         jline("NVDA", day="2026-10-02", sources=[src(1)])], held, TODAY)
    one = [i for i in few["items"] if i["link"] == "https://news.example.com/1"]
    assert len(few["items"]) == 2 and len(one) == 1 and one[0]["seen"].startswith("2026-10-02")


def test_earnings_dates_are_listed_by_code_for_companies_within_two_weeks():
    held = {"MSFT": "long", "NVDA": "long", "XLE": "long"}
    lines = [jline("MSFT", earnings="2026-10-14"), jline("NVDA", earnings="2026-11-19"),
             jline("XLE", earnings="2026-10-08")]
    facts = digest.gather(lines, held, TODAY)
    assert [(e["ticker"], e["date"], e["days_away"]) for e in facts["earnings"]] == [("MSFT", "2026-10-14", 9)]
    assert facts["earnings"][0]["link"] == "https://finance.yahoo.com/calendar/earnings?symbol=MSFT"


@pytest.mark.parametrize("title,kind", [
    ("Invesco to liquidate three ETFs next month", "closure"),
    ("Company X shares to be delisted from Nasdaq", "closure"),
    ("Fund to close to new investors, then shut down the fund", "closure"),
    ("Provider changes its ticker to XYZ on Monday", "ticker_or_name_change"),
    ("Fund renamed after index switch", "ticker_or_name_change"),
    ("Board approves 10-for-1 stock split", "split"),
    ("Company announces 1-for-8 reverse split", "split"),
    ("Chipmaker agrees to be acquired for $40bn", "merger"),
    ("Two funds to merge into one", "merger"),
    ("Fund merges into a larger sister fund", "merger"),
    ("Stocks rise as investors weigh rate cut", None),
    ("Analyst raises price target to $200", None),
])
def test_the_fixed_words_find_operational_events_and_nothing_else(title, kind):
    item = {"ticker": "XLE", "title": title, "snippet": "", "source": "Reuters",
            "seen": "2026-10-05T15:00:00+00:00", "link": "https://news.example.com/x"}
    flags = digest.flag([item])
    assert [f["kind"] for f in flags] == ([kind] if kind else [])
    if kind:
        assert flags[0]["link"] == item["link"] and flags[0]["title"] == title
        assert flags[0]["note"].startswith('headline mentions "') and flags[0]["seen"] == "2026-10-05"


def test_the_week_s_digest_is_code_only_and_costs_nothing():
    held_lines = [account(("NVDA", 2), ("XLE", -5))]
    lines = [jline("NVDA", earnings="2026-10-14", sources=[src(1, "Chipmaker agrees to be acquired"), src(2)]),
             jline("XLE", sources=[src(3, "Energy fund to liquidate")])]
    record = digest.run(today=TODAY, account_lines=held_lines, journal_lines=lines)
    assert record["status"] == "ok" and record["cost_usd"] == 0.0 and record["headlines_read"] == 3
    assert [(f["ticker"], f["kind"]) for f in record["flags"]] == [("NVDA", "merger"), ("XLE", "closure")]
    assert [e["ticker"] for e in record["earnings"]] == ["NVDA"]
    json.loads(json.dumps(record))
    none = digest.run(today=TODAY, account_lines=[], journal_lines=lines)
    assert none["status"] == "no held names" and none["flags"] == []


def test_flags_are_capped():
    items = [{"ticker": "XLE", "title": f"Fund {k} to liquidate", "snippet": "", "source": "",
              "seen": "2026-10-05", "link": f"https://n.example/{k}"} for k in range(40)]
    assert len(digest.flag(items)) == digest.MAX_FLAGS


def test_the_heartbeat_mode_reads_no_key_and_builds_nothing_that_trades(monkeypatch):
    def refuse(*a, **k):
        raise AssertionError("the digest must not build a provider, a dispatcher or run a cycle")

    monkeypatch.setattr(heartbeat, "build_dispatcher", refuse)
    monkeypatch.setattr(heartbeat, "run_cycle", refuse)
    monkeypatch.setattr(heartbeat, "full_model_provider", refuse)
    record = heartbeat.weekly_digest(today=TODAY)
    assert record["kind"] == "risk-digest" and record["week"] == "2026-W41" and record["cost_usd"] == 0.0


def test_the_digest_imports_no_model_and_no_price():
    import inspect
    source = inspect.getsource(digest)
    assert "orchestrator import llm" not in source and "pricing" not in source
