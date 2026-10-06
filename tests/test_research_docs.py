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
    # 18 ideas when section 13 was registered, then the 16 history screens of 2026-09-27 and 28, then on
    # 2026-10-02 the IC report's two universes, the four stress-period screens and the regime split.
    assert len(rows) == 41


def test_the_checkpoints_read_n_from_every_numbered_row_history_screens_included():
    from analysis.multiple_tests import graveyard_n

    assert graveyard_n() == len(trials())
    history = [r for r in trials() if r[2].startswith("history screen")]
    assert [int(r[0]) for r in history] == list(range(19, 35)) + list(range(37, 41))


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
    tables = [part.split("\n#", 1)[0] for part in backlog.split("### Waiting\n")[1:]]
    assert len(tables) == 2                                 # one under AI ideas, one under Trading rules
    for waiting in tables:
        assert "otation" not in waiting and "urn-of-the-month" not in waiting


def test_the_backlog_has_the_owners_three_parts_and_the_index_first_items():
    """The owner's layout of 4 Oct 2026: AI ideas, Trading rules, Index-first reports, each item with its status."""
    backlog = (RESEARCH / "backlog.md").read_text()
    heads = re.findall(r"^## (.+)$", backlog, re.M)
    parts = ["AI ideas", "Trading rules", "Index-first reports"]
    assert [h for h in heads if h in parts] == parts
    index_first = backlog.split("## Index-first reports", 1)[1].split("\n## ", 1)[0]
    rows = {cells[0]: cells[1] for cells in ([c.strip() for c in line.strip("|").split("|")]
                                             for line in index_first.splitlines() if line.startswith("| "))}
    assert rows["After-tax gate and report"].startswith("**Built**")
    assert rows["ILS report"].startswith("**Built**")
    assert rows["Monthly coach"] == "**Checklist built; data entry not built**"
    assert rows["Investor simulator"].startswith("**Plan, waiting for the owner's approval.** Nothing built.")
    assert rows["Before-real-money checklist"].startswith("**Open")
    # The count of accountant questions is the file's own, and none is answered while its Answers table is empty.
    cpa = (RESEARCH / "cpa-questions.md").read_text()
    asked = len(re.findall(r"^\d+\. \*\*", cpa, re.M))
    answers = cpa.split("## Answers", 1)[1]
    assert "*(none yet)*" in answers
    assert rows["Accountant questions"] == f"**Open: {asked} questions, none answered yet**"
    flat = " ".join(index_first.split())
    for item in ("Make the repository private", "A private notification channel", "Where personal numbers live",
                 "The broker decision", "The fund-domicile decision"):
        assert f"**{item}" in flat, item
    assert flat.count("Waits for the June 2027 verdict") == 2
    assert "use no experiment slot" in flat and "never trade" in flat
    assert (RESEARCH / "investor-simulator-plan.md").exists()


def test_the_two_before_real_money_checklists_have_the_same_items_in_the_same_order():
    """The backlog's copy and the checklist's home (docs/next-steps.mdx) number the items alike, and in both the
    paper-only literal is removed last, after the broker and fund-domicile decisions."""
    def items(text: str) -> list[str]:
        """Each numbered item with its continuation lines, as one line of text."""
        found: list[str] = []
        for line in text.splitlines():
            if re.match(r"^\d\. \*\*", line):
                found.append(line)
            elif found and line.startswith("   ") and line.strip():
                found[-1] += " " + line.strip()
        return found

    home = (ROOT / "docs" / "next-steps.mdx").read_text().split("### Before real money: the checklist", 1)[1]
    copy = (RESEARCH / "backlog.md").read_text().split("The before-real-money checklist, item by item", 1)[1]
    copy = copy.split("\n## ", 1)[0]
    subjects = ("notification", "repository private", "personal numbers", "paper-only literal", "broker", "domicile")
    for listed in (items(home), items(copy)):
        assert len(listed) == 6, listed
        for number, (item, subject) in enumerate(zip(listed, subjects), start=1):
            assert item.startswith(f"{number}. ") and subject in item.split("**")[1], (number, item[:60])
        assert "last" in listed[3]


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


def test_the_owners_items_of_2_oct_have_their_rows_before_they_run():
    """The IC report's two universes (one card), the four stress-period screens (one folder, which the history
    workflow refuses to run without) and the regime split."""
    rows = {int(r[0]): r for r in trials()}
    assert "production names" in rows[35][1] and "(cards/ic-model-scores.md)" in rows[35][6]
    assert "shadow stock universe" in rows[36][1] and "cards/ic-model-scores.md" in rows[36][5]
    for trial in (37, 38, 39, 40):
        assert rows[trial][2] == "history screen (real code)" and "Stress periods" in rows[trial][1]
        assert "(history/2026-10-stress-periods/report.md)" in rows[trial][6]
    assert "history/2026-10-stress-periods/" in (RESEARCH / "graveyard.md").read_text()
    assert "market state" in rows[41][1] and rows[41][2] == "exploratory report"


def test_the_accountant_questions_are_the_owners_ten_then_the_two_added_earlier():
    text = (RESEARCH / "cpa-questions.md").read_text()
    numbered = re.findall(r"^(\d+)\. \*\*", text, re.M)
    assert numbered == [str(n) for n in range(1, 13)]
    # The owner's list of 3 Oct 2026, in order, in the owner's words.
    owners = [
        "is the allowable loss zero under Circular 10/2025?",
        "Must a current-year capital loss first be offset against foreign dividends",
        "may I use specific-lot identification instead of FIFO",
        "Which Bank of Israel representative rate applies: the trade date or the settlement date?",
        "For an accumulating Irish UCITS ETF bought abroad in USD",
        "exposed to section 86 (artificial transaction)?",
        "Do the half-year advance-payment reports net losses realized in the same half?",
        "What are the penalties for late filing and late payment",
        "What does Form 1324 cover",
        "With automatic withholding through HYBRID and Form 867",
    ]
    flat = " ".join(text.split())
    places = [flat.index(" ".join(q.split())) for q in owners]
    assert places == sorted(places)
    assert flat.index("ILS-hedged fund") > places[-1] and "kupat gemel lehashkaa" in text
    assert "Arbitrage Committee" in text
    # T5 is question 1 and stays unconfirmed; the switch it does not decide is question 2.
    first = flat[places[0] - 200:places[1]]
    assert "T5" in first and "needs confirmation" in first
    assert "OFFSET_LOSSES_VS_DIVIDENDS" in flat[places[1]:places[2]]


def test_the_card_states_the_replacement_rule_and_the_five_replaced_names():
    """The owner, 3 Oct 2026: the rule for the five replaced names is written on the card before the list freezes."""
    from config import shadow_universe

    card = " ".join((RESEARCH / "cards" / "ic-model-scores.md").read_text().split())
    assert "Replacement rule (written 2026-10-03, before the list freezes)" in card
    assert "never because of its price, its returns or its scores" in card
    assert {old: new for old, (new, _) in shadow_universe.REPLACED.items()} == {
        "JNJ": "EW", "MDT": "IDXX", "SPGI": "MET", "DOW": "MLM", "ASX": "UMC", "BK": "STT", "AVB": "IRM"}
    for old, (new, rule) in shadow_universe.REPLACED.items():
        assert f"({old}" in card and f"({new})" in card and f"by rule ({rule})" in card
        assert old not in shadow_universe.TICKERS and new in shadow_universe.TICKERS


def test_the_ic_card_carries_the_shadow_universe_exactly_as_the_code_lists_it():
    """Published in the card on the registration date and never changed after (pre-registration 13.9)."""
    from config import shadow_universe

    card = (RESEARCH / "cards" / "ic-model-scores.md").read_text()
    assert shadow_universe.markdown_table() in card


def test_the_regime_cut_offs_are_the_numbers_the_registered_rule_gave():
    """Pre-registration 13.10: fixed once from VT's history to 2026-09-30, by the stress screen's run."""
    import json

    from analysis import regimes

    found = json.loads((RESEARCH / "history" / "2026-10-stress-periods" / "results.json").read_text())["regime_cutoffs"]
    assert found["complete"] is True and found["window_end"] == regimes.VT_CUTOFF_WINDOW_END.isoformat()
    assert tuple(found["cutoffs"]) == regimes.VOL_CUTOFFS
    text = " ".join((ROOT / "docs" / "horse-race-preregistration.md").read_text().split())
    assert "low up to **11.30%** a year" in text and "up to **16.97%**" in text
    assert "0.11302353418809083 and 0.16965241927688823" in text


def test_the_ic_card_states_the_settings_the_code_registers():
    """The card is what is registered on 2026-12-22; its numbers must be the code's (``analysis.ic``)."""
    from analysis import ic

    card = " ".join((RESEARCH / "cards" / "ic-model-scores.md").read_text().split())
    assert ic.IC_START.isoformat() in card and ic.IC_REGISTRATION.isoformat() in card
    assert (ic.MIN_NAMES, ic.N_EFF_MIN_RETURNS, ic.N_EFF_MIN_DATES, ic.MDE_T) == (10, 20, 20, 2.4)
    assert ic.N_EFF_MIN_COVERAGE == 0.9 and ic.NW_LAG == {1: 1, 3: 3} and ic.HORIZONS == (1, 3)
    for phrase in ("at least 10 of them", "fewer than 20 returns", "fewer than 90% of the window's dates",
                   "at least 20 of them", "t = 2.4", "lag equal to the horizon (1 and 3)", "h = 1 and h = 3",
                   "the blended score's mean daily rank-IC at 1 session (Newey-West t, lag 1)",
                   "only IC members of the Benjamini-Hochberg family", "the IC at 3 sessions",
                   "two trials in N (two universes) and one idea against the quarterly limit",
                   "the production names split by sleeve", "for the 16 single names and for the 64 funds separately",
                   "not in the Benjamini-Hochberg family, no Deflated Sharpe Ratio, no trial in N",
                   "The split by sleeve and the pooled number are hidden the same way",
                   "labelled \"descriptive, very noisy\"", "The minimum stays 10 names a day",
                   "after each entry day's average return across the lines with that score is taken out",
                   "(a day with fewer than two such lines is left out)", "too far from zero, in either direction",
                   "the number of lines used and a t with errors clustered by entry day"):
        assert phrase in card, phrase
    assert (ic.MAIN_SCORE, ic.MAIN_HORIZON) == ("blend", 1)
    assert ic.GROUPS == ("single_names", "funds")
    text = " ".join((ROOT / "docs" / "horse-race-preregistration.md").read_text().split())
    assert "**Split by sleeve, descriptive only (Amendment 2026-10-03):**" in text
    assert '**Pooled number for the single names, "descriptive, very noisy" (Amendment 2026-10-04):**' in text
    assert ic.POOLED_LABEL == "descriptive, very noisy"


def test_only_the_two_primary_ic_tests_are_in_the_family():
    """The owner's decision of 3 Oct 2026: one primary IC test per universe in the Benjamini-Hochberg family;
    the 3-session IC and the single scores are descriptive only."""
    from shadow import run as shadow_run

    ic_rows = [row for row in shadow_run.FAMILY if row[0].startswith("IC") or row[1].startswith("ic")]
    assert [row[1:3] for row in ic_rows] == [("ic_main", "production"), ("ic_main", "shadow")]
    text = " ".join((ROOT / "docs" / "horse-race-preregistration.md").read_text().split())
    assert "these two primary tests are the only IC members of the Benjamini-Hochberg family" in text
