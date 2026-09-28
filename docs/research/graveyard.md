# Graveyard: every idea ever tried

Every strategy idea this project has tried, run, or dropped, including the
ones dropped before they ran. Rows are never deleted: an idea that dies stays
here with the reason. **The number of rows in the table below is N**, the
number of trials the Deflated Sharpe Ratio corrects for at each checkpoint
(pre-registration, section 13.6). A new idea gets its row (and its card in
`cards/`) before it runs.

**N = 18** (2026-09-28).

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
