"""The cycle report: every score shown next to the evidence behind it."""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone

import pytest

from analysis import cycle_report as cr


def _line(ticker="AAPL", when="2026-09-15T15:06:00+00:00", **kw):
    entry = {
        "ticker": ticker,
        "ts_utc": when,
        "context": {
            "ticker": ticker,
            "headlines": ["Apple beats on earnings — Revenue up 8% (Reuters, 2 hours ago)"],
            "sources": [{
                "title": "Apple beats on earnings", "snippet": "Revenue up 8%",
                "source": "Reuters", "when": "2 hours ago", "url": "https://example.com/a",
            }],
            "technicals": {"rsi14": 61.2, "last_close": 195.3},
            "fundamentals": {"trailing_pe": 34.2},
            "analysts": {"recommendation": "buy"},
            "insiders": {"buys": [], "sells": []},
            "gaps": [],
        },
        "signal": {
            "ticker": ticker, "bias": "BULLISH", "conviction": 0.72,
            "rationale": "Guidance raise corroborated by an uptrend.",
            "news_score": 0.8, "technical_score": 0.5,
            "fundamental_score": 0.1, "analyst_score": 0.6, "insider_score": 0.0,
            "key_factors": ["Guidance raised 8%"],
        },
        "outcome": {"status": "ACCEPTED", "reason": "ok", "quantity": 50},
        "error": None,
    }
    entry.update(kw)
    return cr.Line(entry)


def test_a_headline_is_rendered_as_a_link():
    text = "\n".join(cr.render_ticker(_line()))
    assert "[Apple beats on earnings](https://example.com/a)" in text
    assert "Reuters, 2 hours ago" in text


def test_each_score_sits_next_to_its_own_evidence():
    """The reason this report exists: a score out of reach of its inputs is an assertion."""
    text = "\n".join(cr.render_ticker(_line()))
    news_at = text.index("NEWS</b> — scored +0.80")
    tech_at = text.index("TECHNICALS</b> — scored +0.50")
    assert news_at < text.index("Apple beats on earnings") < tech_at
    assert "rsi14" in text[tech_at:]


def test_a_journal_without_urls_still_renders_and_says_so():
    """Lines written before URLs were captured must not render as empty."""
    line = _line()
    line.raw["context"]["sources"] = []
    text = "\n".join(cr.render_ticker(line))
    assert "Links were not captured" in text
    assert "Apple beats on earnings" in text


def test_a_failed_ticker_names_its_failure():
    line = _line(signal=None, outcome=None, error="Bright Data HTTP 401")
    text = "\n".join(cr.render_ticker(line))
    assert "Bright Data HTTP 401" in text


def test_a_screened_ticker_says_the_full_model_was_not_asked():
    line = _line(
        signal={"ticker": "AAPL", "bias": "NEUTRAL", "conviction": 0.2},
        outcome=None,
        screen={"model": "claude-haiku-4-5", "bias": "NEUTRAL"},
    )
    text = "\n".join(cr.render_ticker(line))
    assert "Screened out" in text


def test_the_latest_cycle_excludes_yesterday():
    now = datetime(2026, 9, 15, 15, 6, tzinfo=timezone.utc)
    lines = [
        _line("OLD", when=(now - timedelta(days=1)).isoformat()),
        _line("NEW", when=now.isoformat()),
        _line("ALSO", when=(now - timedelta(minutes=3)).isoformat()),
    ]
    picked = {l.ticker for l in cr.latest_cycle(lines)}
    assert picked == {"NEW", "ALSO"}


def test_the_report_leads_with_the_strongest_conviction():
    quiet = _line("QUIET")
    quiet.raw["signal"]["conviction"] = 0.10
    loud = _line("LOUD")
    loud.raw["signal"]["conviction"] = 0.90
    text = cr.render([quiet, loud])
    assert text.index("### LOUD") < text.index("### QUIET")


def test_a_truncated_line_is_skipped_not_fatal(tmp_path):
    path = tmp_path / "journal.log"
    path.write_text(
        json.dumps(_line().raw) + "\n{ truncated\n" + json.dumps(_line("MSFT").raw) + "\n"
    )
    assert [l.ticker for l in cr.read_lines(path)] == ["AAPL", "MSFT"]


def test_a_missing_journal_is_empty_not_an_exception(tmp_path):
    assert cr.read_lines(tmp_path / "nope.log") == []


def test_the_header_counts_what_happened():
    text = cr.render([_line("AAPL"), _line("MSFT", outcome=None, error="down")])
    assert "2 tickers" in text and "1 accepted" in text and "1 failed" in text


def test_the_report_never_places_an_order():
    """Read-only by construction: it must not import the broker or the engine."""
    src = (cr.__file__ and open(cr.__file__).read()) or ""
    assert "broker_client" not in src
    assert "execution_engine" not in src
    assert "submit" not in src


def test_a_price_keeps_its_cents():
    """A report that rounds 184.55 to 184.6 is not the number the model saw."""
    line = _line()
    line.raw["context"]["technicals"] = {"last_close": 184.55, "shares": 37000000.0}
    text = "\n".join(cr.render_ticker(line))
    assert "184.55" in text
    assert "37,000,000" in text
