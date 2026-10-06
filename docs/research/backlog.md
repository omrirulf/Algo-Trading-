# Research backlog

Ideas that might become exploratory tests one day. **Updated monthly** (the
first working day of each month). Nothing here runs live: an idea runs live
only after it has a card in `cards/`, a row in `graveyard.md`, a registration
in the pre-registration (section 13), and, if it needs no AI, a history
screen it survived (below).

## History first, live second (the owner's process, 2026-09-27)

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
   possible (uses the AI)".
4. **History screens do not use live slots**, but every screen gets its row
   in `graveyard.md` before it runs (the row links to the screen's folder in
   `docs/research/history/`, and the workflow refuses a screen no row names)
   and **counts in N**, whatever it shows (pre-registration, section 13.6).

## The limits (pre-registration, section 13.8; unchanged)

Section 13.8 says "new ideas"; the owner's reading of 2026-09-27 is that these
are **live** ideas, and a history screen is not one.

- A, B and C are the starting set. **No other new exploratory test before
  the first checkpoint (2026-12-22).**
- **From 2027-01-01: at most 2 new live ideas per quarter, registered only
  at checkpoints** (the race's looks). History screens are not live ideas
  and do not use these slots.
- Every idea tried, including one dropped before it runs and every history
  screen, gets a row in `graveyard.md`, and the count there is N for the
  Deflated Sharpe Ratio. So every idea added makes every other result a
  little harder to believe.

## How to add an idea

One row below: the idea in one sentence, its published source, what it
would be compared with, whether it needs the AI, and the date it was added.
When it is picked: write its card from `cards/_template.md`, add its
graveyard row, run its history screen (if it needs no AI), and only then, at
a checkpoint, register it.

## Waiting

| Added | Idea | Source | Compared with | Needs the AI? | Notes |
| --- | --- | --- | --- | --- | --- |
| | *(none yet)* | | | | |

## Dropped after a history screen

Not to be proposed again without a new reason, written down here first.

| Dropped | Idea | Why | Graveyard |
| --- | --- | --- | --- |
| 2026-09-27 | Rotation among sectors | Failed its history screen (the owner's quick test). | trial 26 |
| 2026-09-27 | Rotation among countries | Failed its history screen (the owner's quick test). | trial 27 |
| 2026-09-27 | Turn-of-the-month | Failed its history screen (the owner's quick test). | trial 28 |

## Monthly updates

| Month | What changed |
| --- | --- |
| 2026-09 | Started, with A, B and C registered (section 13) and the graveyard at N = 18. |
| 2026-09 | 27 Sep: the history-first process added. Every history test so far logged in the graveyard (N = 33 by the end of the day's edits). Rotation (sectors, countries) and turn-of-the-month dropped: both failed their history screen. They were never in the Waiting table, so they are recorded under "Dropped after a history screen". |
| 2026-09 | 28 Sep: the owner's decisions. The momentum quick test counts as three rows (held 3, 21 and 63 sessions), so N goes from 33 to 34; the quick tests of momentum, A and C stay counted; the survival rule above is approved; the owner's note on when the quick tests of A, B and C were run is under pre-registration section 13. |
| 2026-10 | 2 Oct: the owner's instructions. Graveyard rows 35 to 41 (N from 34 to 41): the IC report of the model's scores on two universes (prepared; registered at the 2026-12-22 checkpoint; one idea against the quarterly limit, if the owner confirms), the stress-period history screens of momentum, A, B and C (descriptive; they use no live slot), and the regime split (descriptive). Not built, by the owner's decision: a 1-to-5 ranking arm (only if the IC report shows the scores are too coarse), an ILS fund, and any change of model, provider or broker. |
