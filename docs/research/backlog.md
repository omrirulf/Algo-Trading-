# Research backlog

**Updated monthly** (the first working day of each month). Three parts
(the owner's layout of 4 Oct 2026):

- **[AI ideas](#ai-ideas)**: ideas that use the AI. They might become
  exploratory tests one day.
- **[Trading rules](#trading-rules)**: rule ideas that do not use the AI.
  They might become exploratory tests one day, after a history screen.
- **[Index-first reports](#index-first-reports)**: reports and tools for the
  owner as an index investor. They are not tests: they use no experiment
  slot, get no card and no graveyard row, and never trade.

Nothing in the first two parts runs live: an idea runs live only after it
has a card in `cards/`, a row in `graveyard.md`, a registration in the
pre-registration (section 13), and, if it needs no AI, a history screen it
survived (below).

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

An idea that might become a test: one row in the Waiting table of its part
(AI ideas or Trading rules): the idea in one sentence, its published source,
what it would be compared with, and the date it was added. When it is
picked: write its card from `cards/_template.md`, add its graveyard row, run
its history screen (if it needs no AI), and only then, at a checkpoint,
register it.

A report or a tool for the owner as an index investor: one row under
Index-first reports, with its status. It is not a test, so it needs no card,
no graveyard row and no slot.

## AI ideas

Ideas that use the AI. They skip the history screen (rule 3 above) and go
straight to the live queue, under the limits above.

### Waiting

| Added | Idea | Source | Compared with | Notes |
| --- | --- | --- | --- | --- |
| | *(none yet)* | | | |

## Trading rules

Rule ideas that do not use the AI. Each one passes a registered history
screen first (rules 1, 2 and 4 above).

### Waiting

| Added | Idea | Source | Compared with | Notes |
| --- | --- | --- | --- | --- |
| | *(none yet)* | | | |

### Dropped after a history screen

Not to be proposed again without a new reason, written down here first.

| Dropped | Idea | Why | Graveyard |
| --- | --- | --- | --- |
| 2026-09-27 | Rotation among sectors | Failed its history screen (the owner's quick test). | trial 26 |
| 2026-09-27 | Rotation among countries | Failed its history screen (the owner's quick test). | trial 27 |
| 2026-09-27 | Turn-of-the-month | Failed its history screen (the owner's quick test). | trial 28 |

## Index-first reports

Reports and tools for the owner as an index investor: what the money would
do after Israeli tax and in shekels, and what to check before any real money.
They are **tools, not tests**: they use no experiment slot, get no card and
no graveyard row, and do not count in N. They are **shadow-only and never
trade**. The owner's personal numbers (lots, holdings, income, savings) never
go into this repository, a log, an artifact or a phone push.

"Built in PR #140" means built in that pull request, which stays a draft
until the owner has read it and says OK; it is not merged yet.

| Item | Status | Where | Notes |
| --- | --- | --- | --- |
| After-tax gate and report | **Built** (PR #140) | Pre-registration section 5c; `config/israel_tax.py`, `analysis/israel_tax.py`, `shadow/after_tax.py`; `docs/after-tax.mdx` | The owner's tax cases T1 to T10 are unit tests; T5 still needs the accountant's confirmation (question 1). The gate can only stop an arm from winning. |
| ILS report | **Built** (PR #140) | Pre-registration section 11.9; `analysis/boi_rates.py`; the 4 Funds page and `logs/after_tax.md` | Every result also in shekels at the Bank of Israel's rate, and how much of it came from the dollar's move. The first real night of rates comes after merge. |
| Monthly coach | **Checklist built; data entry not built** | `coach/checklist.py`, `.github/workflows/coach.yml`; plan in `monthly-coach-plan.md` | Fixed questions on the first working day of each month, from Sunday 1 Nov 2026. No model, no personal number, nothing collected. The data entry waits until the owner confirms that they want to enter numbers. |
| Investor simulator | **Plan, waiting for the owner's approval.** Nothing built. | [`investor-simulator-plan.md`](investor-simulator-plan.md) | The owner's lots, FIFO per account, Israeli tax, rebalancing and harvest suggestions, the annual report pack, and buy-and-hold VT and VWRA after tax in shekels. A tool, not a test: no experiment slot. Never trades. The plan recommends keeping the lots in a private GitHub repository of the owner's own, where a job with no key of the owner's (while this repository is public) runs this repository's engine and writes the report as a Markdown file there. 20 decisions wait for the owner (each with a recommendation), and 3 new accountant questions are proposed, not added. Built and tested with sample data only, after the owner approves the plan and the private-data design. |
| Accountant questions | **Open: 12 questions, none answered yet** | [`cpa-questions.md`](cpa-questions.md) | The owner's 10 of 3 Oct 2026 and the 2 added on 2 Oct. An answer changes a setting only through a dated row in the pre-registration's Amendments table. |
| Before-real-money checklist | **Open: every item** | `docs/next-steps.mdx`, "Before real money: the checklist" | The items are listed below. No real money goes in before the June 2027 verdict (pre-registration, section 9). |

The before-real-money checklist, item by item (all open; the same numbers as
in `docs/next-steps.mdx`):

1. **A private notification channel.** The phone push goes through the
   public ntfy.sh server, so nothing personal is pushed until it moves.
2. **Make the repository private.** The journal, the account snapshots and
   the model-call artifacts are public today. Worth knowing first (the
   simulator plan, section 2.3): on GitHub's free plan this takes the
   dashboard's Pages site offline; the repository's Actions runs (about
   4,000 minutes a month, an estimate) are about twice the 2,000 free
   minutes a month for private repositories, so the extra would cost money
   or the runs would stop until the next month; and the simulator's private
   job would need a GitHub access setting or a read-only token to fetch the
   engine.
3. **Where personal numbers live.** The coach's approved plan says a private
   Supabase project; the simulator's plan proposes a private GitHub
   repository for the lots, and asks whether the coach's numbers should go
   there too (decisions D1 to D3). No app or token that reaches all the
   owner's repositories may reach that place. The owner decides; nothing
   personal is collected before that.
4. **The paper-only literal** in `app/broker_client.py` is removed last, by
   an explicit, reviewed code change, after every other item here.
5. **The broker decision** (stay with Alpaca or move, for example to
   Interactive Brokers: `docs/broker-evaluation.mdx`). Waits for the June 2027
   verdict.
6. **The fund-domicile decision** (a US-listed fund such as VT, or an Irish
   one such as VWRA: tax on dividends, US estate tax, accountant question 5).
   Waits for the June 2027 verdict.

## Monthly updates

| Month | What changed |
| --- | --- |
| 2026-09 | Started, with A, B and C registered (section 13) and the graveyard at N = 18. |
| 2026-09 | 27 Sep: the history-first process added. Every history test so far logged in the graveyard (N = 33 by the end of the day's edits). Rotation (sectors, countries) and turn-of-the-month dropped: both failed their history screen. They were never in the Waiting table, so they are recorded under "Dropped after a history screen". |
| 2026-09 | 28 Sep: the owner's decisions. The momentum quick test counts as three rows (held 3, 21 and 63 sessions), so N goes from 33 to 34; the quick tests of momentum, A and C stay counted; the survival rule above is approved; the owner's note on when the quick tests of A, B and C were run is under pre-registration section 13. |
| 2026-10 | 2 Oct: the owner's instructions. Graveyard rows 35 to 41 (N from 34 to 41): the IC report of the model's scores on two universes (prepared; registered at the 2026-12-22 checkpoint; one idea against the quarterly limit, if the owner confirms), the stress-period history screens of momentum, A, B and C (descriptive; they use no live slot), and the regime split (descriptive). Not built, by the owner's decision: a 1-to-5 ranking arm (only if the IC report shows the scores are too coarse), an ILS fund, and any change of model, provider or broker. |
| 2026-10 | 4 Oct: the owner's layout. The backlog now has three parts: AI ideas, Trading rules (each with its own Waiting table; the three dropped rule ideas moved under Trading rules) and Index-first reports, a new part for tools that are not tests (no slot, no card, no graveyard row; N unchanged at 41). Index-first reports lists six items: the after-tax gate and report and the ILS report (built in PR #140), the monthly coach (checklist built, data entry not built), the investor simulator (plan waiting for the owner's approval, nothing built), the accountant questions (12 open) and the before-real-money checklist (every item open). |
