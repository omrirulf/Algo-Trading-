---
title: "Pre-registration"
description: "The question, the arms, the metric, the minimum sample and the decision rule, written down before the numbers"
---

# Pre-registration: does the daily model call earn its keep?

**Status: IN FORCE from the date this file was merged to `main`.** Nothing
below changes without a dated entry in [Amendments](#amendments), and the
only permitted amendments are bug fixes. The numbers already accumulated are
never re-scored under a changed rule.

| | |
| --- | --- |
| Registered on | 2026-09-22 (the merge of the pull request that added this file) |
| Journal starts | 2026-09-15 |
| First entry day counted | the first entry day after **2026-09-23**, the date the `model` arm changed (Amendment 1). Days before it are reported but do not count toward the minimum sample or the decision: before 2026-09-22 the rule was not yet written, and on 2026-09-22 a different model was answering. |

## 1. The question

Does the full model's daily judgement, as journalled, produce a higher mean
daily net return than a fixed time-series-momentum rule that reads only the
price, on the same lines, over the same days, after the same costs?

## 2. The arms

| Arm | Role | Where | Reads |
| --- | --- | --- | --- |
| `model` | incumbent | `logs/signal_journal.log`, as written | everything in the prompt |

The `model` arm is whatever production actually answered with, which is the point of it and also its one fragility: changing the production model changes the contestant. Since 2026-09-23 that is `openai/gpt-oss-120b` at high reasoning, asked on every name. Until 2026-09-22 it was a funnel — `claude-haiku-4-5` screening, `claude-opus-5` on what it escalated — so the arm's own history is two different answerers and only the later one counts. See Amendment 1.
| `momentum` | main comparator | `rules/momentum.py` | `TechnicalSnapshot` only |
| `hybrid` | second main comparator | `rules/hybrid.py` | `TechnicalSnapshot` + the line's own `news_score` |
| `random` | floor | `rules/control.py`, 1000 seeds | nothing |
| `insiders` | secondary, exploratory | `rules/insider_buying.py` | `InsiderSnapshot` only |

Every arm goes through the identical conviction floor (`MIN_CONVICTION`,
0.30), the identical stop and sizing (`backtest.simulate.simulate_trade`),
the identical cost, and the identical prices, cut to final closes
(`analysis.returns.last_final_session`).

Parameters are fixed here and will not be tuned:

- **momentum**: 63-bar return confirmed by the 50-day SMA; conviction
  `|return_63d| / annualised_volatility`, clamped to [0, 1].
- **hybrid**: momentum's direction; NEUTRAL when the line's `news_score`
  points the other way (`news_score × direction < 0`); conviction is the
  equal-weight mean of momentum's conviction and `|news_score|`. No weight
  is fitted.
- **insiders**: BULLISH when, in the 180 calendar days before the line, two
  or more distinct insiders (not the issuer, not a 10% owner) made
  open-market purchases and open-market shares bought exceed open-market
  shares sold; else NEUTRAL, never BEARISH. Conviction 0.50. Grants, option
  exercises, gifts and tax withholding are not purchases
  (`orchestrator/insiders.py` excludes them, with tests). 180 days is the
  window the snapshot itself carries and the six-month aggregation of
  Lakonishok and Lee (2001).
- **cost**: 0.10% per side, 0.20% a round trip, on every trade of every arm.
- **horizon**: 3 sessions for every arm. The insider arm is also scored at
  20 sessions, for reading only.
- **entry**: the session after the signal, at the open; exit at the close of
  the horizon bar or at the stop, whichever comes first.

### The hybrid is not model-free

The hybrid's `news_score` is the one the journal carries for the line, and
that number comes from the **current model calls**. Until 2026-09-22 that
was a mix decided by the screen's outcome — Opus on lines the screen
escalated, Haiku on lines it ended. Since 2026-09-23 it is
`openai/gpt-oss-120b` on every line. Two consequences:

1. If the hybrid is chosen, production **still needs a daily news-scoring
   call**. The saving is the full-model call on escalated lines, not the
   model altogether.
2. A cheaper news-scoring model may score the same headlines differently
   from the mix tested here. Choosing the hybrid on this race's numbers does
   not license swapping the scorer without a new comparison.

The second of those has already happened: Amendment 1 swapped the scorer. So
the hybrid arm's history is split on the same date as the `model` arm's and
for the same reason, and only the days after 2026-09-23 count. `momentum`,
`random` and `insiders` read nothing a model wrote, so their histories are
continuous — but the primary metric is a paired difference against `model`,
which is not, so the restart is the whole race's.

## 3. The primary metric

**Mean daily net return, model minus momentum**, where a day's net return
for an arm is the equal-weighted mean net return of the trades it opened on
that entry day, and 0 on a day it opened none. Net return is the trade's
signed return through the stop and sizing minus the round trip.

The paired difference is computed over the calendar of every entry day any
main arm traded, **over all 80 names**. Its standard error is Newey-West
with lag 3 (the horizon). The non-overlapping check uses every 3rd entry day
with a plain standard error.

The same metric, model minus hybrid, is the second main comparison.

## 4. Minimum sample before any decision

**60 non-overlapping entry days** — every 3rd entry day, so about 180 entry
days, roughly nine months of trading days from the registration date. No
decision, in either direction, is taken before that. A good or bad number at
30 days is reported and ignored.

Secondary arms report "too few" until they have 20 scored trades on at least
20 distinct entry days, and never count toward or against the primary
decision whatever they show.

## 5. The decision rule

At 60 non-overlapping entry days, **keep the full model in the daily loop
only if all three hold**:

1. Its mean daily net return exceeds momentum's, with the Newey-West t of
   the paired difference above 2.0.
2. Its mean daily net return exceeds the hybrid's, with the Newey-West t of
   that paired difference above 2.0.
3. Its mean daily net return is above the 95th percentile of the coin-flip
   band drawn on its own lines (1000 seeds).

**If the model does not meet the keep rule, the replacement is momentum**,
unless the hybrid beats momentum on the same primary metric — mean daily net
return, hybrid minus momentum, over all names, at the 3-session horizon —
with a Newey-West t above 2.0, in which case the replacement is the hybrid,
subject to the note in section 2 that it still needs a news-scoring call.

Hit rate, median return, the per-trade table and the coin-flip percentiles
of the other arms are reported for reading, not for deciding.

## 6. What is exploratory and cannot change the decision

- **The splits.** Funds-only and companies-only tables are printed for
  reading. The decision uses all names only.
- **Any horizon other than the primary 3 sessions**, including the insider
  arm's 20-session table.
- **Every secondary arm.** An exploratory arm is a hypothesis for the next
  registration, not evidence in this one.
- **A rule parameter moved after seeing the numbers.** The parameters above
  are frozen; a new rule is a new arm with a new registration.
- **A re-scoring under a changed cost, horizon or floor.** The defaults above
  are the ones the decision reads; other settings may be printed as
  sensitivity.
- **A partial window.** The primary window runs from the registration date
  to the day the minimum sample is reached, inclusive of every entry day in
  it.

## 7. Locked

From the registration date, **no changes to the arm definitions, the costs
or the decision rule, except bug fixes.** A bug fix is a change that makes
the code do what this file already says; anything else is a new
registration. Every bug fix is logged below with its date and reason, and
the race is re-run over the whole journal so the log and the numbers agree.

## 8. What is reported meanwhile

The race runs nightly (`.github/workflows/horse-race.yml`) and prints
everything above on the whole journal, including the days before
registration, marked as such. Reading it is allowed. Acting on it is not.

## Amendments

| Date | Kind | Reason |
| --- | --- | --- |
| 2026-09-23 | **New registration of the `model` arm** (not a bug fix) | The owner moved production off Claude: `SCREENING_ENABLED` off, and the full model from the `claude-haiku-4-5` → `claude-opus-5` funnel to `openai/gpt-oss-120b` at high reasoning on every name, for cost (~$1.39 a cycle to ~$0.20). Section 7 allows only bug fixes, and this is not one — it replaces the contestant. The metric, the sample size and the decision rule are unchanged. What changed is who the `model` arm is — and, with it, the `news_score` the `hybrid` arm reads, which comes from the same calls (section 2, "The hybrid is not model-free"). `momentum`, `random` and `insiders` are untouched. **The 60-day count therefore restarts from 2026-09-23.** The 2026-09-22 lines stay in the journal and in the printed tables, marked pre-registration, and cannot be added to the new model's days: a mean over two different models is a mean over neither. |
