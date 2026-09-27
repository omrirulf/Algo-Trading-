"""The research routine's records: the graveyard's count is N, and every card is filled.

Pre-registration section 13.6 reads N from ``docs/research/graveyard.md``;
13.8 says every idea has a card and a row before it runs.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "docs" / "research"
FIELDS = ("Date", "Source", "Exact rule and settings", "Data used", "Compared against",
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
    assert len(rows) == 18


def test_the_pre_registration_names_the_same_n():
    text = (ROOT / "docs" / "horse-race-preregistration.md").read_text()
    assert f"checkpoint day ({len(trials())} when this was registered)" in text


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
