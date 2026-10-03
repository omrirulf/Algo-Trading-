"""The code-only relevance check (the owner, 3 Oct 2026): "a headline counts as relevant if the company name,
or the ticker as a whole word, appears in the title or the first sentence"."""

from __future__ import annotations

import ast
import json
from datetime import date
from pathlib import Path

import pytest

from analysis import news_relevance as nr
from config.watchlist import DEFAULT_WATCHLIST
from orchestrator.news import Headline

SOURCE = Path(nr.__file__)


@pytest.mark.parametrize("title, snippet, relevant", [
    ("Southern Company raises its outlook", "", True),                      # the name in the title
    ("Utilities rally", "Southern Co shares rose 2%. Peers followed.", True),  # the name in the first sentence
    ("Utilities rally", "Peers rose. Southern Company followed.", False),    # only in the second sentence
    ("Why SO is a buy", "", True),                                           # the ticker as a whole word
    ("$SO jumps", "", True),
    ("Utilities rally (NYSE:SO)", "", True),
    ("So what now for utilities?", "", False),                               # not in capitals: a word
    ("SOUTHERN COMPANY DIVIDEND", "", True),                                 # the name in capitals
    ("southern company towns", "", False),                                   # a proper noun, as written
    ("ALSO SEEN: utilities", "", False),                                     # not a whole word
])
def test_the_owner_s_rule(title, snippet, relevant):
    matcher = nr.Matcher("SO", ("Southern Company", "Southern Co"))
    assert matcher.relevant(title, snippet) is relevant


def test_a_hyphen_or_ampersand_joins_a_ticker_to_the_next_word():
    att = nr.Matcher("T", ("AT&T",))
    assert not att.relevant("T-Mobile beats estimates")
    assert att.relevant("AT&T beats estimates") and att.relevant("Telecoms: T rises")
    citi = nr.Matcher("C", ("Citigroup", "Citi"))
    assert not citi.relevant("C-suite turnover rises")
    # A capital standing alone counts by the rule, but not by name: the report shows both.
    assert citi.relevant("Class C shares added") and not citi.named("Class C shares added")


def test_proper_nouns_only():
    visa = nr.Matcher("V", ("Visa",))
    assert not visa.relevant("New visa rules for students")
    assert visa.relevant("Visa beats estimates") and visa.relevant("VISA SHARES SLIDE")
    assert not visa.relevant("A V-shaped recovery")


def test_first_sentence():
    assert nr.first_sentence("One. Two.") == "One."
    assert nr.first_sentence("Up 3%! Then down") == "Up 3%!"
    assert nr.first_sentence("No end") == "No end"
    assert nr.first_sentence("Revenue was $1.5 billion. Next") == "Revenue was $1.5 billion."
    assert nr.first_sentence("") == ""


def test_share_takes_headlines_journal_records_and_prompt_lines():
    items = [Headline(title="State Street names a new chief"),
             {"title": "Banks slip", "snippet": "State Street fell 1%. Others too."},
             "Markets wrap — stocks mixed (Reuters, 1h ago)"]
    found = nr.share("STT", ("State Street",), items)
    assert (found.headlines, found.relevant, found.named) == (3, 2, 2)
    assert found.share == pytest.approx(2 / 3) and not found.fails


@pytest.mark.parametrize("relevant, total, fails", [(3, 10, False), (2, 10, True), (0, 0, True), (1, 1, False)])
def test_a_name_fails_under_30_percent_or_with_no_headline(relevant, total, fails):
    assert nr.Share("X", total, relevant, relevant).fails is fails
    assert nr.FAIL_BELOW == 0.30


def test_the_report_has_the_share_per_name_the_names_under_30_and_the_overall_share():
    shares = [nr.Share("SO", 10, 9, 9), nr.Share("STT", 0, 0, 0), nr.Share("C", 10, 2, 1)]
    text = nr.report(shares, "Check")
    assert "**Overall: 55% relevant** (11 of 20 headlines, 3 names)." in text
    assert "**Under 30% (or no headline): 2 name(s)**: STT (n/a), C (20%)" in text
    assert "| SO | 10 | 9 | 90% | 90% |" in text and "| C | 10 | 2 | 20% | 10% |" in text
    assert nr.overall([]) is None


def test_universe_share_uses_the_universe_s_names():
    found = nr.universe_share("TGT", ["Target Corp. cuts prices", "Analysts lift price Target"])
    assert (found.relevant, found.named) == (1, 1)


def test_the_race_names_cover_the_80_names_exactly():
    assert set(nr.RACE_NAMES) == set(DEFAULT_WATCHLIST) and len(nr.RACE_NAMES) == 80
    assert all(nr.RACE_NAMES.values())


def test_journal_headlines_reads_each_line_s_news_from_a_day_on(tmp_path):
    def line(ticker, ts, sources):
        return json.dumps({"ticker": ticker, "ts_utc": ts, "context": {"sources": sources}})

    (tmp_path / "2026-09.log").write_text("\n".join([
        line("NVDA", "2026-09-22T14:00:00+00:00", [{"title": "too early"}]),
        line("NVDA", "2026-09-23T14:00:00+00:00", [{"title": "Nvidia rises", "snippet": "s"}]),
        line("MSFT", "2026-09-24T14:00:00+00:00", []),
        "not json",
        json.dumps({"no": "ticker"}),
    ]) + "\n", encoding="utf-8")
    found = nr.journal_headlines(tmp_path, date(2026, 9, 23))
    assert found == {"NVDA": [{"title": "Nvidia rises", "snippet": "s"}], "MSFT": []}
    assert nr.journal_headlines(tmp_path, date(2026, 9, 23), until=date(2026, 9, 23)) == {
        "NVDA": [{"title": "Nvidia rises", "snippet": "s"}]}


def test_answered_only_keeps_the_lines_the_model_answered_and_drops_held_and_failed_ones(tmp_path):
    """The news the model read, by the race's rule: a signal about this ticker, and not held."""
    def line(ticker, title, **extra):
        return json.dumps({"ticker": ticker, "ts_utc": "2026-09-24T14:00:00+00:00",
                           "context": {"sources": [{"title": title}]}, **extra})

    answered = {"signal": {"ticker": "NVDA", "bias": "NEUTRAL", "conviction": 0.0}}
    (tmp_path / "2026-09.log").write_text("\n".join([
        line("NVDA", "answered", **answered),
        line("NVDA", "held", held=True),
        line("NVDA", "failed", error="read timeout"),
    ]) + "\n", encoding="utf-8")
    every = nr.journal_headlines(tmp_path, date(2026, 9, 23))
    read = nr.journal_headlines(tmp_path, date(2026, 9, 23), answered_only=True)
    assert [r["title"] for r in every["NVDA"]] == ["answered", "held", "failed"]
    assert [r["title"] for r in read["NVDA"]] == ["answered"]


def test_the_module_is_pure():
    """No network, no model, no file written."""
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    imported = {alias.name.split(".")[0] for node in ast.walk(tree) if isinstance(node, ast.Import)
                for alias in node.names}
    imported |= {(node.module or "").split(".")[0] for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)}
    assert not imported & {"httpx", "requests", "urllib", "anthropic", "orchestrator", "socket"}
    text = SOURCE.read_text(encoding="utf-8")
    for call in ("write_text", "write_bytes", "open("):
        assert call not in text, call
