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
    # 2026-10-02 the IC report's two universes, the four stress-period screens and the regime split, then on
    # 2026-10-04 the voting arm and the thesis check.
    assert len(rows) == 43


def test_the_checkpoints_read_n_from_every_numbered_row_history_screens_included():
    from analysis.multiple_tests import graveyard_n

    assert graveyard_n() == len(trials())
    history = [r for r in trials() if r[2].startswith("history screen")]
    assert [int(r[0]) for r in history] == list(range(19, 35)) + list(range(37, 41))


def test_the_bar_n_sets_is_computed_exactly_and_names_today_s_n():
    """The owner's request of 2026-10-06: the bar for N = 43 next to the bar for N = 18, computed exactly."""
    import math

    from analysis.multiple_tests import dsr_t_bar

    text = (RESEARCH / "graveyard.md").read_text()
    head, rows = None, []
    for line in text.split("### The bar N sets", 1)[1].splitlines():
        if line.startswith("| The look"):
            head = [cell.strip() for cell in line.strip("|").split("|")]
        elif head and line.startswith("| ") and not line.startswith("| ---"):
            rows.append([cell.strip() for cell in line.strip("|").split("|")])
        elif head and rows and not line.startswith("|"):
            break
    ns = [int(re.match(r"N = (\d+)", cell).group(1)) for cell in head[1:]]
    assert ns == [18, 41, 43] and len(trials()) == 43 and head[-1] == "N = 43 (now)"
    sessions = [int(re.search(r"T = (\d+)", row[0]).group(1)) if "T =" in row[0] else 10**8 for row in rows]
    assert sessions == [61, 121, 181, 10**8]
    from datetime import date, timedelta

    from config.market_calendar import is_trading_day

    def count(first: date, last: date) -> int:
        return sum(is_trading_day(first + timedelta(days=i)) for i in range((last - first).days + 1))

    for row, t_days in zip(rows[:3], sessions):
        assert count(date(2026, 9, 28), date.fromisoformat(row[0][:10])) == t_days
    assert count(date(2026, 12, 22), date(2027, 3, 22)) == 61 and count(date(2027, 1, 1), date(2027, 3, 22)) == 54
    for row, t_days in zip(rows, sessions):
        for cell, n in zip(row[1:], ns):
            assert cell == f"t {dsr_t_bar(n, t_days):.2f}", (row[0], n)
    # The lines under the table, recomputed.
    assert f"t {dsr_t_bar(43, 121):.2f} is an\nannualised Sharpe ratio of about {dsr_t_bar(43, 121) / math.sqrt(121) * math.sqrt(252):.1f}" in text
    assert f"(t {dsr_t_bar(18, 121):.2f}, N = 18: about {dsr_t_bar(18, 121) / math.sqrt(121) * math.sqrt(252):.1f})" in text
    assert f"T = 61, t {dsr_t_bar(43, 61):.2f} at N = 43; the shadow universe, from 2027-01-01, T = 54,\nt {dsr_t_bar(43, 54):.2f})" in text
    assert round(dsr_t_bar(43, 121) - dsr_t_bar(18, 121), 2) == 0.37
    assert round(dsr_t_bar(44, 121) - dsr_t_bar(43, 121), 2) == 0.01


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


def test_the_backlog_is_in_three_sections_and_lists_every_ai_idea():
    """The owner, 4 Oct 2026: AI ideas, trading rules and index-first reports, in that order; each AI idea with
    its status, cost and trial number."""
    backlog = (RESEARCH / "backlog.md").read_text()
    heads = re.findall(r"^## (.+)$", backlog, re.M)
    assert [h for h in heads if h in ("AI ideas", "Trading rules", "Index-first reports")] == [
        "AI ideas", "Trading rules", "Index-first reports"]
    ai = backlog.split("\n## AI ideas\n", 1)[1].split("\n## ", 1)[0]
    rules = backlog.split("\n## Trading rules\n", 1)[1].split("\n## ", 1)[0]
    assert "### History first, live second" in rules and "### Waiting" in rules
    assert "### Dropped after a history screen" in rules
    rows = {}
    for line in ai.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("| ") and len(cells) == 5 and cells[0] not in ("Idea", "---"):
            rows[cells[0]] = cells
    assert len(rows) == 7
    assert all(cells[1] and cells[2] and cells[3] for cells in rows.values())     # status, cost and trial on every row
    by_word = {word: next(c for name, c in rows.items() if word in name)
               for word in ("IC report", "Shadow stock universe", "model_vote", "Thesis check", "1-to-5 ranking arm",
                            "cross-model vote", "Event tags and annual-report flags")}
    assert by_word["IC report"][3] == "35" and "Built, switched off" in by_word["IC report"][1]
    assert by_word["Shadow stock universe"][3] == "36" and "until 2027-01-01" in by_word["Shadow stock universe"][1]
    assert by_word["model_vote"][3] == "42" and "until 2026-12-22" in by_word["model_vote"][1]
    assert "$1.00 a day" in by_word["model_vote"][2] and "$0.80" in by_word["model_vote"][2]
    assert by_word["Thesis check"][3] == "43" and "until 2027-04-01" in by_word["Thesis check"][1]
    assert "$0.10 a week" in by_word["Thesis check"][2]
    assert "Deferred" in by_word["1-to-5 ranking arm"][1] and "too coarse" in by_word["1-to-5 ranking arm"][1]
    assert "not registered" in by_word["cross-model vote"][1]
    assert "Dropped: too few events" in by_word["Event tags and annual-report flags"][1]


def test_the_index_first_reports_list_each_item_with_its_status():
    """The owner's instructions of 4 Oct 2026: each index-first item with its status. Tools, not tests."""
    backlog = (RESEARCH / "backlog.md").read_text()
    index_first = backlog.split("\n## Index-first reports\n", 1)[1].split("\n## ", 1)[0]
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
    assert "*(none yet)*" in cpa.split("## Answers", 1)[1]
    assert rows["Accountant questions"] == f"**Open: {asked} questions, none answered yet**"
    flat = " ".join(index_first.split())
    for item in ("A private notification channel", "Make the repository private", "Where personal numbers live",
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


def test_the_owners_items_of_4_oct_have_their_rows_and_cards_before_they_run():
    """The voting arm (one trial in N, a race arm and a fund) and the thesis check (a log and a description)."""
    from config import model_vote as mv
    from config import thesis_check as tc

    rows = {int(r[0]): r for r in trials()}
    assert mv.TRIAL == 42 and tc.TRIAL == 43
    assert "`model_vote`" in rows[42][1] and rows[42][2] == "exploratory arm and fund (prepared)"
    assert "(cards/model_vote.md)" in rows[42][6] and "until 2026-12-22" in rows[42][3]
    assert "Thesis check" in rows[43][1] or "thesis check" in rows[43][1]
    assert rows[43][2] == "exploratory report (prepared)" and "(cards/thesis-check.md)" in rows[43][6]
    assert "until 2027-04-01" in rows[43][3]
    for card in ("model_vote.md", "thesis-check.md"):
        text = (RESEARCH / "cards" / card).read_text()
        assert "**Survives its history screen if:** No history screen (uses the AI)." in text
        assert "**History screen:** Not possible (uses the AI)." in text


def test_the_vote_card_says_what_the_owner_asked_it_to_say():
    """The owner, 4 Oct 2026: same-model repetition reduces sampling noise, not shared bias; the crowd study used
    12 different models and forecasting questions, not stock returns; a cross-model vote is a separate later idea."""
    card = " ".join((RESEARCH / "cards" / "model_vote.md").read_text().split())
    assert "Repeating the same model only reduces sampling noise, not shared bias." in card
    assert "Schoenegger et al. (*Science Advances*, 2024) used 12 different models, and forecasting questions, not stock returns." in card
    assert "A cross-model vote would be a separate, later idea" in card
    for words in ("at least 3 successful votes", "if it has at least 3 of the 5", "A tie for the most votes is NEUTRAL",
                  "Conviction = (votes for that side ÷ 5) × (the mean conviction of those votes)",
                  "0.30", "Newey-West t (lag 3)", "Newey-West t (lag 5)", "$1.00 a day", "$0.80", "23:15 UTC",
                  "fewer than 20 such lines by the final checkpoint", "Benjamini-Hochberg family"):
        assert words.lower() in card.lower(), words


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


def test_the_checkpoint_verdict_is_logged_in_the_amendments_table_in_date_order():
    """The owner's approval of 6 Oct 2026: one Amendments row, the dates still in order, and each section
    the five readings touch says so (sections 5c, 5d, 11.6, 11.7, 11.8)."""
    text = (ROOT / "docs" / "horse-race-preregistration.md").read_text()
    table = text.split("## Amendments", 1)[1]
    dates = re.findall(r"^\| (\d{4}-\d{2}-\d{2}) \|", table, re.M)
    # In date order, with the row present; later rows (the 9 Oct re-ask fix) may follow it.
    assert dates == sorted(dates) and "2026-10-06" in dates
    row = next(line for line in table.splitlines() if line.startswith("| 2026-10-06 | **Checkpoint verdict"))
    for words in ("yes to all five, as you proposed", "Addition 1", "Addition 2", "TEST DATA",
                  "the race's bars are the fixed 3.47, 2.45 and 2.00", "Made before any checkpoint result existed",
                  "estimated for 2026-12-22"):
        assert words in row, words
    sections = re.split(r"^#{2,3} ", text, flags=re.M)
    for number in ("5c.", "5d.", "11.6", "11.7", "11.8"):
        body = next(part for part in sections if part.startswith(number))
        assert "(Amendment 2026-10-06)" in body, number
