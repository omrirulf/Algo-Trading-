# Graveyard: every idea ever tried

Every strategy idea this project has tried, run, or dropped, including the
ones dropped before they ran, and every test of an idea on history. Rows are
never deleted: an idea that dies stays here with the reason. **The number of
numbered rows in the two tables below (the ideas, then the history screens)
is N**, the number of trials the Deflated Sharpe Ratio corrects for at each
checkpoint (pre-registration, section 13.6; `analysis/multiple_tests.py`
counts them). A new idea gets its row (and its card in `cards/`) before it
runs, and a history screen gets its row before it runs.

**N = 31** (2026-09-27: 18 ideas and 13 history screens).

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
setting changed is a new row. Rows 19 to 27 are the owner's quick tests: the
owner's own code, not the registered code, on 38 ETFs from 2000 to 2026,
with a 2 x ATR stop assumed. Rows 28 to 31 are the first screen with the real
code (`history/`), of the rules already running live; it changes nothing in
the locked test.

| Trial | Idea | Kind | Status | Dates | Why it is here / what happened | Card |
| --- | --- | --- | --- | --- | --- | --- |
| 19 | Momentum (the 63-day rule), 3-session trades, on 38 ETFs | history screen (the owner's quick test) | no edge on history | by 2026-09-27 | No better than a coin flip. | |
| 20 | Momentum held 1 to 3 months, on 38 ETFs | history screen (the owner's quick test) | no edge since 2010 | by 2026-09-27 | Worked in 2000-2009. Since 2010 its buys trailed holding all the ETFs, and its shorts lost about 3.7% per 3-month short. | |
| 21 | A: momentum with a 200-day average veto, on 38 ETFs | history screen (the owner's quick test) | no clear difference | by 2026-09-27 | The veto removed only about 4% of signals, with no clear difference. | |
| 22 | C: pullback limit entry, on 38 ETFs | history screen (the owner's quick test) | prediction as expected | by 2026-09-27 | Filled 63% of signals; missed signals did better than filled ones (+1.0% against -1.0%). Partly built in: a fill means the price fell first. | |
| 23 | The 10-month average on SPY and on VT (B's rule) | history screen (the owner's quick test) | smaller crashes, lower return | by 2026-09-27 | Smaller crashes, but 3-4% a year less return since 2007. | |
| 24 | Rotation among sectors | history screen (the owner's quick test) | failed; dropped | by 2026-09-27 | Failed its history screen. Dropped from the backlog. | |
| 25 | Rotation among countries | history screen (the owner's quick test) | failed; dropped | by 2026-09-27 | Failed its history screen. Dropped from the backlog. | |
| 26 | Turn-of-the-month | history screen (the owner's quick test) | failed; dropped | by 2026-09-27 | Failed its history screen. Dropped from the backlog. | |
| 27 | Volatility targeting on SPY | history screen (the owner's quick test) | tested, not taken further | by 2026-09-27 | Tested on history by the owner; its result is not written down in this repository. | |
| 28 | Momentum (the locked rule), race and fund | history screen (real code) | RESULT_28 | 2026-09-27 | DETAIL_28 | [report](history/2026-09-rules-running-live/report.md) |
| 29 | A: momentum with the 200-day veto, race and fund | history screen (real code) | RESULT_29 | 2026-09-27 | DETAIL_29 | [report](history/2026-09-rules-running-live/report.md) |
| 30 | B: 10-month timing on VT (and the same code on SPY, as a check of row 23) | history screen (real code) | RESULT_30 | 2026-09-27 | DETAIL_30 | [report](history/2026-09-rules-running-live/report.md) |
| 31 | C: pullback limit entry, fund | history screen (real code) | RESULT_31 | 2026-09-27 | DETAIL_31 | [report](history/2026-09-rules-running-live/report.md) |

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
