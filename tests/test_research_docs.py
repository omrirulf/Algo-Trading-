"""The research routine's records: the graveyard's count is N, and every card is filled.

Pre-registration section 13.6 reads N from ``docs/research/graveyard.md``;
13.8 says every idea has a card and a row before it runs.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "docs" / "research"
FIELDS = ("Date", "Source", "Exact rule and settings", "Data used", "Compared against", "Acting differently",
          "Main metric", "Read on", "Promising if", "Dead if", "Trial number")


def trials() -> list[list[str]]:
    rows = [line for line in (RESEARCH / "graveyard.md").read_text().splitlines()
            if re.match(r"^\| \d+ \|", line)]
    return [[cell.strip() for cell in row.strip("|").split("|")] for row in rows]


def test_the_graveyard_is_numbered_one_by_one_and_states_its_count():
    rows = trials()
    assert [int(r[0]) for r in rows] == list(range(1, len(rows) + 1))
    text = (RESEARCH / "graveyard.md").read_text()
    assert f"**N = {len(rows)}**" in text
    # 18 ideas when section 13 was registered, then the 15 history screens of 2026-09-27 and 28.
    assert len(rows) == 33


def test_the_checkpoints_read_n_from_every_numbered_row_history_screens_included():
    from analysis.multiple_tests import graveyard_n

    assert graveyard_n() == len(trials())
    history = [r for r in trials() if r[2].startswith("history screen")]
    assert [int(r[0]) for r in history] == list(range(19, 34))


def test_no_row_is_left_with_a_placeholder_and_every_real_code_screen_links_its_report():
    text = (RESEARCH / "graveyard.md").read_text()
    assert not re.search(r"\b(RESULT|DETAIL)_\d+\b", text)
    for row in trials():
        if row[2] == "history screen (real code)":
            link = re.search(r"\((history/[^)]+)\)", row[6])
            assert link and (RESEARCH / link.group(1)).exists(), row[0]


def test_the_pre_registration_still_names_the_n_it_was_registered_with():
    """Section 13.6 reads N from the graveyard on the checkpoint day; 18 is the count on the day it was
    registered, and stays as written while the graveyard grows."""
    text = (ROOT / "docs" / "horse-race-preregistration.md").read_text()
    assert "checkpoint day (18 when this was registered)" in text


def test_the_card_template_asks_for_the_history_screen_and_the_backlog_says_history_first():
    template = (RESEARCH / "cards" / "_template.md").read_text()
    assert "**History screen:**" in template and "not possible (uses the AI)" in template
    backlog = (RESEARCH / "backlog.md").read_text()
    assert "## History first, live second" in backlog
    for words in ("after its source was published", "0.10% per side", "using the real code",
                  "skips the history screen", "do not use live slots", "counts in N"):
        assert words in backlog, words
    waiting = backlog.split("## Waiting", 1)[1].split("##", 1)[0]
    assert "otation" not in waiting and "urn-of-the-month" not in waiting


def test_the_dropped_fifty_day_version_is_kept_and_counted():
    row = next(r for r in trials() if "50-day moving-average veto" in r[1])
    assert row[3] == "dropped before it ran" and "signal counts only" in row[5]


def test_every_linked_card_exists_and_has_every_field():
    for row in trials():
        link = re.search(r"\(cards/([^)]+)\)", row[6])
        if not link:
            continue
        card = (RESEARCH / "cards" / link.group(1)).read_text()
        for field in FIELDS:
            assert f"**{field}:**" in card, (link.group(1), field)
        assert f"**Trial number:** {row[0]}" in card, link.group(1)
    names = {p.name for p in (RESEARCH / "cards").glob("*.md")} - {"_template.md"}
    linked = {re.search(r"\(cards/([^)]+)\)", r[6]).group(1) for r in trials() if "(cards/" in r[6]}
    assert names == linked
