# Research backlog

Ideas that might become exploratory tests one day. **Updated monthly** (the
first working day of each month). Nothing here runs live: an idea runs live
only after it has a card in `cards/`, a row in `graveyard.md`, a registration
in the pre-registration (section 13), and, if it needs no AI, a history
screen it survived ("History first, live second", under Trading rules).

Three sections since 2026-10-04 (the owner's reorganisation): **AI ideas**,
**Trading rules** and **Index-first reports**. The rules just below apply to
all three; the record of monthly changes is at the end.

## Rules for every idea

### The limits (pre-registration, section 13.8; unchanged)

Section 13.8 says "new ideas"; the owner's reading of 2026-09-27 is that these
are **live** ideas, and a history screen is not one.

- A, B and C are the starting set. **No other new exploratory test before
  the first checkpoint (2026-12-22).**
- **From 2027-01-01: at most 2 new live ideas per quarter, registered only
  at checkpoints** (the race's looks). History screens are not live ideas
  and do not use these slots. The first quarter of 2027 is full: the IC test
  and the vote, both registered at the 2026-12-22 checkpoint. The thesis
  check is an idea of the second quarter of 2027.
- Every idea tried, including one dropped before it runs and every history
  screen, gets a row in `graveyard.md`, and the count there is N for the
  Deflated Sharpe Ratio. So every idea added makes every other result a
  little harder to believe.

### How to add an idea

One row in its section's table: the idea in one sentence, its published
source, what it would be compared with, whether it needs the AI, and the
date it was added. When it is picked: write its card from
`cards/_template.md`, add its graveyard row, run its history screen (if it
needs no AI), and only then, at a checkpoint, register it.

## AI ideas

Ideas that use the AI. They skip the history screen: it is not possible,
because the AI has read about the past, so the past cannot test it (rule 3
of "History first, live second"). Each card says "History screen: not
possible (uses the AI)". Every one below is shadow-only: none trades.

| Idea | Status | Cost | Trial | Card |
| --- | --- | --- | --- | --- |
| IC report: do the model's scores rank the next session's returns? (the 80 production names) | **Built, switched off**: counters only until it is registered at the 2026-12-22 checkpoint (pre-registration section 13.9). The first new idea of the first quarter of 2027. | None: it reads the journal and the prices, and asks no model. | 35 | [card](cards/ic-model-scores.md) |
| Shadow stock universe: the same IC test on 251 more names, scored every day by the same model | **Built, switched off until 2027-01-01** (`SHADOW_UNIVERSE_ENABLED`). The IC test's second universe: same card, same idea. | About $1.05 a day (the model about $0.65, the news searches about $0.40); cap $1.50 a day, phone alert at $1.20. | 36 | [card](cards/ic-model-scores.md) |
| Voting arm `model_vote`: the production answer and four more calls of the same model on the same input; a side needs 3 of 5 votes | **Built, switched off until 2026-12-22** (`MODEL_VOTE_ENABLED`), registered at that checkpoint (section 13.11). The second new idea of the first quarter of 2027. A race arm and a fund against the model, one call, on the same lines. | About $0.70 a day; cap $1.00 a day, phone alert at $0.80. | 42 | [card](cards/model_vote.md) |
| Thesis check: once a week, does the reason each held name was bought still hold? (VALID, WEAKENED or BROKEN) | **Built, switched off until 2027-04-01** (`THESIS_CHECK_ENABLED`), registered at the 2027-03-22 checkpoint as an idea of the second quarter of 2027 (section 13.12). Log only; BROKEN against VALID names described at the checkpoints after that. | About $0.06 a week; cap $0.10 a week. | 43 | [card](cards/thesis-check.md) |
| A 1-to-5 ranking arm: the model ranks names instead of calling each one | **Deferred**: built only if the IC report shows the scores are too coarse (the owner's decision of 2026-10-02). Not registered. | Not estimated. | None (no card, no row) | |
| A cross-model vote: different models vote on each line | **A later idea, not registered.** The wisdom-of-the-crowd result (12 different models) is about different models; `model_vote` (one model, five calls) does not test it. It would need its own card, row and registration. | Not estimated. | None (no card, no row) | |
| Event tags and annual-report flags | **Dropped: too few events** to judge. Dropped before a card was written. | | None (no card, no row) | |

## Trading rules

Rules that need no AI. The owner's next message fills this section; what
follows is the process every such rule goes through, and the rules already
waiting or dropped.

### History first, live second (the owner's process, 2026-09-27)

1. **A new rule idea that does not need the AI must first pass a registered
   history screen**, before it can be proposed for a live slot:
   - its card is written first (`cards/_template.md`), with every setting
     fixed; the screen runs on those settings and nothing is tuned after;
   - it is tested on the years **after its source was published** (an idea
     with no published source: every year there are prices for, and the card
     says so);
   - with the registered cost, 0.10% per side;
   - **using the real code**: the code that would run it live, through the
     history screen (the `history/` package, run by hand with the workflow
     `.github/workflows/history-screen.yml`; its reports go to
     `docs/research/history/`).
2. **Only an idea that survives its screen can be proposed for a live
   slot.** What "survives" means is written on the card before the screen
   runs (its "Survives its history screen if" field). When the card says
   nothing else: it beats its comparator on its main metric, after costs,
   over the years after its source, with a Newey-West t above 2 (approved by
   the owner, 2026-09-28).
3. **An idea that uses the AI skips the history screen** (it is not
   possible: the AI has read about the past, so the past cannot test it) and
   goes straight to the live queue. Its card says "History screen: not
   possible (uses the AI)". Those ideas are listed under AI ideas, above.
4. **History screens do not use live slots**, but every screen gets its row
   in `graveyard.md` before it runs (the row links to the screen's folder in
   `docs/research/history/`, and the workflow refuses a screen no row names)
   and **counts in N**, whatever it shows (pre-registration, section 13.6).

### Waiting

| Added | Idea | Source | Compared with | Needs the AI? | Notes |
| --- | --- | --- | --- | --- | --- |
| | *(none yet)* | | | | |

### Dropped after a history screen

Not to be proposed again without a new reason, written down here first.

| Dropped | Idea | Why | Graveyard |
| --- | --- | --- | --- |
| 2026-09-27 | Rotation among sectors | Failed its history screen (the owner's quick test). | trial 26 |
| 2026-09-27 | Rotation among countries | Failed its history screen (the owner's quick test). | trial 27 |
| 2026-09-27 | Turn-of-the-month | Failed its history screen (the owner's quick test). | trial 28 |

## Index-first reports

The owner's next message fills this section.

## Monthly updates

| Month | What changed |
| --- | --- |
| 2026-09 | Started, with A, B and C registered (section 13) and the graveyard at N = 18. |
| 2026-09 | 27 Sep: the history-first process added. Every history test so far logged in the graveyard (N = 33 by the end of the day's edits). Rotation (sectors, countries) and turn-of-the-month dropped: both failed their history screen. They were never in the Waiting table, so they are recorded under "Dropped after a history screen". |
| 2026-09 | 28 Sep: the owner's decisions. The momentum quick test counts as three rows (held 3, 21 and 63 sessions), so N goes from 33 to 34; the quick tests of momentum, A and C stay counted; the survival rule above is approved; the owner's note on when the quick tests of A, B and C were run is under pre-registration section 13. |
| 2026-10 | 2 Oct: the owner's instructions. Graveyard rows 35 to 41 (N from 34 to 41): the IC report of the model's scores on two universes (prepared; registered at the 2026-12-22 checkpoint; one idea against the quarterly limit, if the owner confirms), the stress-period history screens of momentum, A, B and C (descriptive; they use no live slot), and the regime split (descriptive). Not built, by the owner's decision: a 1-to-5 ranking arm (only if the IC report shows the scores are too coarse), an ILS fund, and any change of model, provider or broker. |
| 2026-10 | 4 Oct: the owner's instructions. The backlog is now in three sections (AI ideas, trading rules, index-first reports); the AI ideas are listed with their status, cost and trial. Graveyard rows 42 and 43 (N from 41 to 43): the voting arm `model_vote` (built, switched off until 2026-12-22; registered at that checkpoint as the second idea of the first quarter of 2027) and the thesis check (built, switched off until 2027-04-01; an idea of the second quarter of 2027). A cross-model vote is a later idea, not registered; event tags and annual-report flags are dropped (too few events). |
