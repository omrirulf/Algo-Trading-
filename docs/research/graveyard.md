# Graveyard: every idea ever tried

Every strategy idea this project has tried, run, or dropped, including the
ones dropped before they ran, and every test of an idea on history. Rows are
never deleted: an idea that dies stays here with the reason. **The number of
numbered rows in the tables below (the ideas, the history screens, and the
rows added from 2026-10-02) is N**, the number of trials the Deflated Sharpe
Ratio corrects for at each
checkpoint (pre-registration, section 13.6; `analysis/multiple_tests.py`
counts them). A new idea gets its row (and its card in `cards/`) before it
runs, and a history screen gets its row before it runs.

**N = 41** (2026-10-02: 18 ideas and 16 history screens by 2026-09-28, then the IC report's two universes, the
four stress-period screens and the regime split, added on 2026-10-02).

| Trial | Idea | Kind | Status | Dates | Why it is here / what happened | Card |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Model v1: `claude-haiku-4-5` screen, then `claude-opus-5` on escalated names | main arm (old) | replaced | 2026-09-14 to 2026-09-22 | Replaced by model v2 for cost (Amendment 1, 2026-09-23). Its lines are kept, marked pre-registration. | |
| 2 | Model v2: `openai/gpt-oss-120b`, high reasoning, every name | main arm | running | from 2026-09-23 | The race's incumbent. | |
| 3 | Momentum: 63-day return confirmed by the 50-day average | main arm | running | registered 2026-09-22 | Main comparator. | |
| 4 | Hybrid: momentum with the model's news-score veto | main arm | running | registered 2026-09-22 | Second main comparator. | |
| 5 | Insider cluster buying | exploratory arm | running | from 2026-09-22 | Section 2; reported on its own lines. | [card](cards/insiders.md) |
| 6 | Learned blend of the five dimension scores | shadow | running | from 2026-09-16 | Scored nightly in the score report; never trades. Includes the single scores and the equal-weight composite it is compared with. | |
| 7 | Trades grouped by conviction | exploratory report | running | from 2026-09-25 | Reporting only (Amendments, 2026-09-25). | |
| 8 | Longs against shorts | exploratory report | running | from 2026-09-25 | Reporting only (Amendments, 2026-09-25). | |
| 9 | `model_by_conviction` fund | exploratory fund | registered | from 2026-09-28 | Section 11.1. Results only at checkpoints (13.1). | [card](cards/model_by_conviction.md) |
| 10 | `model_sized` fund | exploratory fund | registered | from 2026-09-28 | Section 11.1. Results only at checkpoints (13.1). | [card](cards/model_sized.md) |
| 11 | `model_same_day` fund | exploratory fund | registered | from 2026-09-28 | Section 11.1. Results only at checkpoints (13.1). | [card](cards/model_same_day.md) |
| 12 | The model without news (news ablation) | replay | dropped | 2026-09-22 (rescored 2026-09-25) | Run three times as a measurement; never registered as an arm. | |
| 13 | Historical replay of the model on past data | replay | dropped | 2026-09-14 to 2026-09-15 | Ran three times; results not kept in the repository. | |
| 14 | "Buy fear": sizing by VIX regime | sizing rule | dropped | 2026-09-20 | Tested on 2007-2026 data; the normal sizing was kept. | |
| 15 | Momentum with a 50-day moving-average veto | exploratory (proposed) | dropped before it ran | 2026-09-27 | Redundant: the momentum rule already confirms against the 50-day average, so it would have removed only about 1-3% of signals. Decided from signal counts only; no returns were looked at. Replaced by trial 16. | |
| 16 | A: momentum with a 200-day moving-average veto | exploratory arm and fund | registered | from 2026-09-28 | Section 13.2. | [card](cards/A-momentum-200day-veto.md) |
| 17 | B: 10-month moving-average timing on VT | exploratory fund | registered | from 2026-09-30 | Section 13.3. | [card](cards/B-vt-10-month-timing.md) |
| 18 | C: pullback limit entry | exploratory fund | registered | from 2026-09-28 | Section 13.4. | [card](cards/C-pullback-limit-entry.md) |

## History screens

Every test of an idea on past prices so far (the owner's process of
2026-09-27, `backlog.md`, "History first, live second"). They count in N like
every other trial. One row for each rule and set of names tested; a screen
re-run because its code had a bug is the same row, and a screen run with any
setting changed is a new row.

Rows 19 to 29 are the owner's quick tests: the owner's own code, not the
registered code, run outside this repository by 2026-09-27. Their exact
settings are not recorded here. Rows 19 to 23 used 38 ETFs from 2000 to 2026
with a 2 x ATR stop assumed; rows 24, 25 and 29 used SPY or VT. The momentum
test had three settings, held 3, 21 and 63 sessions, so it is three rows
(the owner's decision of 2026-09-28).

Rows 22 to 25 tested ideas that became A, B and C (pre-registration section
13, registered 2026-09-28). That registration says it was made before any
result of A, B or C existed, meaning their live results, computed by this
repository's code. The owner ran these quick tests on 2026-09-27, after A, B
and C's settings were fixed and before section 13 was committed; no setting
was changed after seeing them (the owner's note under section 13, added
2026-09-28).

Rows 30 to 34 are the first screen with the real code (`history/`), of the
rules already running live. It changes nothing in the locked test.

| Trial | Idea | Kind | Status | Dates | Why it is here / what happened | Card |
| --- | --- | --- | --- | --- | --- | --- |
| 19 | Momentum (the 63-day rule) held 3 sessions, on 38 ETFs | history screen (the owner's quick test) | no edge on history | by 2026-09-27 | No better than a coin flip. |  |
| 20 | Momentum (the 63-day rule) held 21 sessions (1 month), on 38 ETFs | history screen (the owner's quick test) | no edge since 2010 | by 2026-09-27 | Worked in 2000-2009. Since 2010 its buys trailed holding all the ETFs. |  |
| 21 | Momentum (the 63-day rule) held 63 sessions (3 months), on 38 ETFs | history screen (the owner's quick test) | no edge since 2010 | by 2026-09-27 | Worked in 2000-2009. Since 2010 its buys trailed holding all the ETFs, and its shorts lost about 3.7% per 3-month short. |  |
| 22 | A: momentum with a 200-day average veto, on 38 ETFs | history screen (the owner's quick test) | no clear difference | 2026-09-27 | The veto removed only about 4% of signals, with no clear difference. |  |
| 23 | C: pullback limit entry, on 38 ETFs | history screen (the owner's quick test) | prediction as expected | 2026-09-27 | Filled 63% of signals; missed signals did better than filled ones (+1.0% against -1.0%). Partly built in: a fill means the price fell first. |  |
| 24 | The 10-month average on SPY (B's rule) | history screen (the owner's quick test) | smaller crashes, lower return | 2026-09-27 | Smaller crashes, but 3-4% a year less return since 2007 (with row 25). |  |
| 25 | The 10-month average on VT (B's rule) | history screen (the owner's quick test) | smaller crashes, lower return | 2026-09-27 | Smaller crashes, but 3-4% a year less return since 2007 (with row 24). |  |
| 26 | Rotation among sectors | history screen (the owner's quick test) | failed | by 2026-09-27 | Failed its history screen. Recorded as dropped in `backlog.md` (it was never in the Waiting table). |  |
| 27 | Rotation among countries | history screen (the owner's quick test) | failed | by 2026-09-27 | Failed its history screen. Recorded as dropped in `backlog.md` (it was never in the Waiting table). |  |
| 28 | Turn-of-the-month | history screen (the owner's quick test) | failed | by 2026-09-27 | Failed its history screen. Recorded as dropped in `backlog.md` (it was never in the Waiting table). |  |
| 29 | Volatility targeting on SPY | history screen (the owner's quick test) | tested, not taken further | by 2026-09-27 | Tested on history by the owner; its result is not written down in this repository. |  |
| 30 | Momentum (the locked rule), race and fund, 80 names | history screen (real code) | no edge at 3 sessions; fund behind VT | 2026-09-28 | Race: no clear difference from a coin flip (minus a coin flip -0.002% a day, t -0.07; from 2010 t -0.51); behind always long on the same lines from 2010 (t -2.3). Fund: -3.5% a year 2000-2026, behind the VT fund from 2010 (t -3.0); positions held about 11 days, costs 4.8% a year. | [report](history/2026-09-rules-running-live/report.md) |
| 31 | A: momentum with the 200-day veto, race and fund, 80 names | history screen (real code) | almost momentum; a small plus | 2026-09-28 | Vetoed 5.7% of momentum's signals (under 10%: A is almost momentum). A minus momentum: race +0.007% a day (t +1.7; from 2010 t +3.0, one slice of many); fund +0.004% a day (t +1.6). Behind the VT fund like momentum. | [report](history/2026-09-rules-running-live/report.md) |
| 32 | B: 10-month timing on VT (the registered rule) | history screen (real code) | behind VT; no crash in its data | 2026-09-28 | Holds from 2009-04 (VT's prices start 2008-06): 6.5% a year against 11.3% for the VT fund, worst fall 27.6% against 29.1%; B minus VT fund -0.019% a day (t -2.0). From 2010: 3.5% a year less. | [report](history/2026-09-rules-running-live/report.md) |
| 33 | B's rule on SPY (the same code; a check of row 24) | history screen (real code) | smaller crash, lower return | 2026-09-28 | From 2007-06: 7.8% a year against 9.0% for the SPY fund, worst fall 25.3% against 49.6%; from 2010: 4.1% a year less (t -1.9). Same code as B; a check of row 24, not the registered rule. | [report](history/2026-09-rules-running-live/report.md) |
| 34 | C: pullback limit entry, fund, 80 names | history screen (real code) | no clear difference from momentum | 2026-09-28 | Fill rate 61.2%; missed signals +0.88% against filled -0.93% per race trade (built in: a fill means the price fell first). C fund minus momentum fund +0.003% a day (t +0.7); most limits that were reached could not be bought, because the book was full. | [report](history/2026-09-rules-running-live/report.md) |

## Added from 2026-10-02

Rows in the order they were added, ideas and history screens together (the owner's instructions of 2026-10-02,
items 4 to 7). The IC report's two rows are the owner's proposal of two trials in N and one idea against the
quarterly limit, which the owner confirms or changes when it is registered at the 2026-12-22 checkpoint
(pre-registration section 13.9). The stress-period screens are one row per rule over the four periods, as one
screen (workflow run 37013435615, `history/2026-10-stress-periods/`); they are descriptive, with no t and no
verdict. VT and SPY in it are benchmarks, not counted.

| Trial | Idea | Kind | Status | Dates | Why it is here / what happened | Card |
| --- | --- | --- | --- | --- | --- | --- |
| 35 | IC of the model's scores (blended and the five dimensions) against the forward return, production names | exploratory test (prepared) | card written; registers at the 2026-12-22 checkpoint | lines from 2026-09-28 | Pre-registration section 13.9. Counters only (lines with scores, days) until the checkpoint; no IC value is written before it. | [card](cards/ic-model-scores.md) |
| 36 | The same IC test on the shadow stock universe (about 250 US large and mid caps and ADRs) | exploratory test (prepared) | built, switched off until 2027-01-01 | scored from 2027-01-01 | The second universe of trial 35's rule, on the same card (`cards/ic-model-scores.md`). Its list is published in the card on the registration date. Off by a flag; a test fails if the flag is on before 2027-01-01. |  |
| 37 | Stress periods: momentum (the locked rule), fund, 80 names, in 2000-2002, 2008, 2020 and 2022 | history screen (real code) | descriptive: no t, no verdict | 2026-10-02 | Total return (worst fall): 2000-2002 -29.5% (33.7%) against SPY -37.5% (46.6%), VT did not exist; 2008 -3.2% (19.0%) against SPY -36.6% (47.1%); 2020 -3.1% (21.5%) against VT +15.5% (34.2%); 2022 -12.4% (19.2%) against VT -18.4% (26.0%). Fell less than the index in the falls, and trailed it by 18.6 points in 2020's quick recovery. Run 37013435615. | [report](history/2026-10-stress-periods/report.md) |
| 38 | Stress periods: A (200-day veto), fund, 80 names | history screen (real code) | descriptive: no t, no verdict | 2026-10-02 | 2000-2002 -27.9% (33.0%); 2008 +5.8% (17.4%); 2020 -1.8% (21.5%); 2022 -10.1% (16.0%). A little ahead of momentum in every period. Same screen as row 37. | [report](history/2026-10-stress-periods/report.md) |
| 39 | Stress periods: B (10-month timing on VT) | history screen (real code) | descriptive: no t, no verdict | 2026-10-02 | Not possible in 2000-2002 and 2008 (VT's prices start 2008-06-26; BIL's 2007-05-30). 2020 +13.0% (worst fall 11.1%) against VT +15.5% (34.2%); 2022 -8.8% (9.9%) against VT -18.4% (26.0%): much smaller falls, as its purpose says. Same screen as row 37. | [report](history/2026-10-stress-periods/report.md) |
| 40 | Stress periods: C (pullback limit entry), fund, 80 names | history screen (real code) | descriptive: no t, no verdict | 2026-10-02 | 2000-2002 -23.4% (27.1%); 2008 -5.5% (20.3%); 2020 +0.5% (23.5%); 2022 -14.2% (18.3%). Same screen as row 37. | [report](history/2026-10-stress-periods/report.md) |
| 41 | The race's and the funds' results split by market state (VT's 200-day average; VT's 21-day volatility terciles) | exploratory report | registered | from 2026-10-02 | Pre-registration section 13.10. Descriptive; hidden until the checkpoints; like rows 7 and 8. |  |

## Not counted, and why

- **Controls and benchmarks**, which are not candidates to be picked: the
  coin flip and the 1,000 coin-flip funds, VT bought and held, SPY and the
  watchlist bought and held, and the "always long, no stop" baseline.
- **Checks with no strategy returns**: signal sanity, the determinism check,
  the model and effort comparisons, the gpt-oss agreement checks, the
  zero-shorts replay, the prompt replay, and the screening candidates graded
  on recall only.
- **Risk, execution and operations settings** applied to every arm alike
  (stops, caps, sleeves, the conviction floor, the profit ladder, run timing,
  the journal split, calibration and the reports around it).
- **The after-tax gate, the after-tax and shekel views and the verdict label**
  (pre-registration sections 5c, 5d and 11.9, 2026-10-02): the same results,
  taxed or in shekels, and rules applied to every arm alike. The break-even
  simulator has no strategy returns. VT and SPY in the stress-period screen
  are benchmarks.
