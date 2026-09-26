---
title: "Pre-registration"
description: "The question, the arms, the metric, the minimum sample and the decision rule, written down before the numbers"
---

# Pre-registration: does the daily model call earn its keep?

**Status: IN FORCE from the date this file was merged to `main`.** Nothing
below changes without a dated entry in [Amendments](#amendments). An
amendment is either a bug fix — the code made to do what this file already
says — or a new registration made by the owner, which says so, says why, and
says whether any result it could have been fitted to existed when it was
made. The numbers already accumulated are never re-scored under a changed
rule; a bug fix re-runs the race over the whole journal.

| | |
| --- | --- |
| Registered on | 2026-09-22 (the merge of the pull request that added this file) |
| Journal starts | 2026-09-15 |
| First entry day counted | the first entry day after **2026-09-23**, the date the `model` arm changed (Amendment 1). Days before it are reported but do not count toward the minimum sample or the decision: before 2026-09-22 the rule was not yet written, and on 2026-09-22 a different model was answering. |
| Decision window | lines journalled on or after **2026-09-23** (UTC). Applied by `analysis/decision_gate.py` (`DECISION_CUTOFF`), not by a reader. The first entry day counted is the session after the first line in it. |
| Model arm settings | `openai/gpt-oss-120b`, reasoning level **high**. Screening (`SCREENING_ENABLED`): **off**. Every journal line records both from the first cycle after this was written (2026-09-25); the lines of 2026-09-23 and 2026-09-24 predate the fields, and the race counts window lines that carry no recorded level. It warns if any line in the window was made otherwise. Turning the screen on, or changing the reasoning level, needs an amendment here first — `tests/test_horse_race.py` fails until there is one. |
| Planned looks | at **20, 40 and 60 independent days** (60, 120 and 180 trading days), bars **t > 3.47, 2.45, 2.00**. See section 5a. |
| Real money | **none before the June 2027 verdict.** See section 9. |

## 1. The question

Does the full model's daily judgement, as journalled, produce a higher mean
daily net return than a fixed time-series-momentum rule that reads only the
price, on the same lines, over the same days, after the same costs?

## 2. The arms

| Arm | Role | Where | Reads |
| --- | --- | --- | --- |
| `model` | incumbent | the journal (`logs/journal/`, one file per month since 2026-09-26; before that `logs/signal_journal.log`), as written | everything in the prompt |

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

A line the model gave no answer on — a timed-out or failed call — is removed
for **every** arm, not only the model (Amendment 2026-09-24, bug fix). Every
arm is judged on exactly the same lines.

The same metric, model minus hybrid, is the second main comparison.

## 4. Minimum sample before any decision

**60 non-overlapping entry days** — every 3rd entry day, so about 180 entry
days, roughly nine months of trading days from 2026-09-23. No
decision, in either direction, is taken before that, except at a planned
look whose bar is met (section 5a). A good or bad number between looks is
reported and ignored.

Counted by the code, in the decision window only: **independent days =
complete blocks of 3 scored entry days** (59 entry days are 19 independent
days, not 20). The race prints, on every run,
`independent days since 2026-09-23: X of 60 (= 180 trading days) — NO DECISION YET`
until a look decides.

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

**Then the index test (Amendment 2026-09-24, index first).** Whichever arm
the rule above picks must also beat a world index fund, **VT**, bought and
held: its mean daily net return minus VT's, measured on the same entry days
and over the same 3-session windows (VT bought at the entry day's open and
held to the close of the horizon bar), with a Newey-West t (lag 3) above
the bar. VT pays no per-window cost — holding the index is one purchase,
not a trade every three sessions — and a dividend going ex inside a window
is added back. **If the winner does not beat VT, no arm trades: the answer is
to hold the index**, and the repo stays for learning and research.

A day VT cannot be priced is an outage and the look waits for it — unless
the price source has published five later VT sessions and still not that
day. Then it is a gap that will not be filled, and that entry day is left
out of the index comparison only, for every arm alike; the race prints how
many days were left out (Amendment 2026-09-24, bug fix).

So there are four possible outcomes: keep the model; replace it with
momentum; replace it with the hybrid; **no arm trades**.

Hit rate, median return, the per-trade table and the coin-flip percentiles
of the other arms are reported for reading, not for deciding.

## 5a. Planned looks (Amendment 2026-09-24)

The rule above is read at three fixed looks, and only there:

| Look | Independent days | Entry days | Bar (Newey-West t) | Estimated date* |
| --- | --- | --- | --- | --- |
| 1 | 20 | 60 | 3.47 | 2026-12-22 |
| 2 | 40 | 120 | 2.45 | 2027-03-22 |
| 3 (final) | 60 | 180 | 2.00 | 2027-06-16 |

\*The trading day the look's last trades close, if no further cycle is lost.
The cycle of 2026-09-24 produced no model answer, so one entry day is
already lost; each further lost day moves every later look back by one
trading day. The race prints its own current estimate for the next look.

The bars are the O'Brien-Fleming boundaries for three equally spaced looks
at an overall two-sided alpha of 0.05: 2.004 × √(3/k) for look k = 1, 2, 3,
i.e. 3.471, 2.454 and 2.004, rounded to 3.47, 2.45 and 2.00. The final bar
is the registered 2.0. `tests/test_decision_gate.py` recomputes them.

At every look, "t above 2.0" in section 5 reads "t above that look's bar",
for both paired tests, for the hybrid-versus-momentum test that picks the
replacement, and for the index test. Condition 3 (the model above the 95th
percentile of its coin flip) is unchanged at every look: it is one more
condition that must also hold, so it cannot loosen the look.

- **At the final look** the rule is read as in section 5, then the index
  test: one of the four outcomes, always.
- **At looks 1 and 2** an early stop is allowed in either direction, but only
  if the bar is met in the direction it stops:
  - *for the model*: it beats momentum and the hybrid at t above the bar,
    and its coin-flip condition holds; or
  - *against the model*: it trails the replacement (momentum, or the hybrid
    if the hybrid beat momentum at the bar) at t below minus the bar.
  
  The index test then has to be decisive too: the picked arm beats VT at t
  above the bar (that arm is the answer), or trails it at t below minus the
  bar (no arm trades). Anything else decides nothing, and the race goes on.
- **No decisions between looks**, and none after a look has decided. Each
  look is computed on its own first 60, 120 or 180 entry days only, so it
  says the same thing every night after it is reached.

## 5b. Where the gate lives

`analysis/decision_gate.py` holds the cutoff, the minimum sample, the looks,
their bars and the index ticker; `analysis/horse_race.py` applies them on
every run and prints the verdict of every look reached. `tests/test_horse_race.py`
fails if any of them differs from this file.

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
- **A partial window, except a planned look.** The primary window is the
  lines journalled on or after 2026-09-23, up to the look that decides
  (section 5a) — its first 60, 120 or 180 entry days, every one of them
  inclusive. Any other slice of it is for reading only.

## 7. Locked

From the registration date, **no changes to the arm definitions, the costs
or the decision rule, except bug fixes and the owner's new registrations
logged under the Status rule at the top of this file.** A bug fix is a change that makes
the code do what this file already says; anything else is a new
registration. Every bug fix is logged below with its date and reason, and
the race is re-run over the whole journal so the log and the numbers agree.

## 8. What is reported meanwhile

The race runs nightly (`.github/workflows/horse-race.yml`). It prints the
decision gate first, then everything above on the decision window, then the
whole journal — including the days before 2026-09-23 — after it, marked as
for reading only. It also prints what the model calls cost over the window
(the journal's own `usage.cost_usd`), and VT bought and held beside SPY and
the watchlist. Reading it is allowed. Acting on it is not, except at a look.

## 9. No real money before the verdict (Amendment 2026-09-24)

No real money goes into this system before the June 2027 verdict (the final
look, section 5a). After it, only if the decision rule — including the index
test — is met. If it is not, the answer is to hold the index. Until then
every arm is shadow-only and the book is Alpaca's paper account.

## 10. Model watch (Amendment 2026-09-24; operational, not a decision rule)

The owner's triggers stop the process and go to the owner. None of them
switches, reverts or trades anything by itself; the owner decides what
happens next.

- (a) the zero-shorts replay — `openai/gpt-oss-120b` re-asked, with the
  production settings, on the lines `claude-opus-5` answered from 2026-09-15
  to 2026-09-22 — shows it shorting on fewer than a quarter of the lines
  where Opus shorted. **Closed on 2026-09-25**: a one-time check, it tripped
  (gpt-oss shorted 1 of the 31 lines where Opus shorted), and the owner kept
  gpt-oss (see the Amendments table);
- (b) 5 answered cycle days in a row with no SHORT call while SPY fell over
  those days. **Retired on 2026-09-26** (the owner's decision): the model is
  long-only by the owner's decision of 2026-09-25, so (b) would only say that
  SPY fell. Replaced by (d) (see the Amendments table);
- (c) model errors above 5% of the calls that reached the model over any 5
  cycle days, counted from **2026-09-25**;
- (d) the real paper account: its equity more than **8%** below its highest
  close since **2026-09-23**, or its return more than **5 percentage
  points** behind VT's over the same period. Judged on closing equity only:
  a reading taken during the session is shown as a mid-day warning and
  never trips (d). From 2026-09-26; the exact definitions are in the
  Amendments table.

Failed calls are of two kinds (`analysis/call_errors.py`). **Setup errors**
are our own: a bad or missing key, an account or a model name the provider
refuses (HTTP 401, 402, 403, 404 and their wording). They are logged and
shown on every run and do not count toward (c). **Model errors** are
everything else — timeouts, server errors, rate limits, empty or off-schema
answers, an answer about another ticker — and they count. Anything not
recognised as a setup error is a model error.

Separately, if more than **20%** of one run's calls fail, of either kind,
the day's record raises a critical alarm, which is pushed to the owner's
phone that day.

The race prints (c) and (d) on every run, with (d)'s current numbers whether
or not it tripped, and (d) is in `logs/race_gate.json` under `watch.d`; when
that record says (d) tripped, the daily health check raises a warning that
reaches the owner's phone through the brief. A mid-day warning is printed
and recorded beside it (`watch.d.midday_warning`) and raises no alarm. Changing the model because of
one is a new registration of the model arm, like Amendment 1.

## Amendments

| Date | Kind | Reason |
| --- | --- | --- |
| 2026-09-23 | **New registration of the `model` arm** (not a bug fix) | The owner moved production off Claude: `SCREENING_ENABLED` off, and the full model from the `claude-haiku-4-5` → `claude-opus-5` funnel to `openai/gpt-oss-120b` at high reasoning on every name, for cost (~$1.39 a cycle to ~$0.20). Section 7 allows only bug fixes, and this is not one — it replaces the contestant. The metric, the sample size and the decision rule are unchanged. What changed is who the `model` arm is — and, with it, the `news_score` the `hybrid` arm reads, which comes from the same calls (section 2, "The hybrid is not model-free"). `momentum`, `random` and `insiders` are untouched. **The 60-day count therefore restarts from 2026-09-23.** The 2026-09-22 lines stay in the journal and in the printed tables, marked pre-registration, and cannot be added to the new model's days: a mean over two different models is a mean over neither. |
| 2026-09-24 | **Index first** (new registration of the decision rule, not a bug fix) | Asked by the owner. The arm the rule picks must also beat VT, bought and held, on mean daily net return over the same entry days and 3-session windows, with a Newey-West t above the bar; otherwise no arm trades and the answer is to hold the index. Adds a fourth outcome. **Made before any trade in the decision window resolved:** the first ones entered on 2026-09-24 and exit at the 2026-09-28 close. One morning of unrealised paper P&L on the 2026-09-23 calls had been logged by the paper account's position manager (for example XOM at +0.38R), and this rule depends on none of it. |
| 2026-09-24 | **Planned looks** (new registration, not a bug fix) | Asked by the owner. Three looks at 20, 40 and 60 independent days, O'Brien-Fleming bars 3.47, 2.45, 2.00 (verified: 2.004 × √(3/k)); an early stop in either direction only at a look whose bar is met in that direction; the index test at every look; no decisions between looks. Section 5a. **Made before any trade in the decision window resolved**, as for the row above. |
| 2026-09-24 | **No real money before the verdict** (new registration) | Asked by the owner. No real money in this system before the June 2027 verdict, and then only if the decision rule, including the index test, is met. Section 9. Made before any trade in the decision window resolved; it depends on no result either way. |
| 2026-09-24 | **Bug fix**: a line with no model answer is dropped for every arm | Section 3 compares the arms "on the same lines". The code offered a timed-out or failed line to the rules and not to the model, so the rules traded it while the model sat in cash: the paired difference charged the model for an outage and compared the arms on different lines. Such a line is now offered to no arm. On the 2026-09-24 cycle every one of the 58 asked names failed (HTTP 401), so that day is out of the race for every arm. The race is re-run over the whole journal. |
| 2026-09-24 | **Bug fix**: the gate is applied by code | Sections 4 and 5 were applied by a person reading the race. The cutoff, the minimum sample (counted as complete blocks of 3 scored entry days), the looks, their bars and the index ticker now live in `analysis/decision_gate.py`, are pinned to this file by a test, and the race prints the verdict itself. This makes the code do what the file says; it changes no rule. |
| 2026-09-24 | **Settings pinned** (enforcement, no rule change) | The model arm's reasoning level (high) and screening (off) are named in the header table and pinned by the test; turning the screen on or changing the level needs an amendment first. Every journal line records both from the first cycle after this change (2026-09-25; the 2026-09-23 and 2026-09-24 lines predate the fields), and the race warns if any line in the window was made otherwise. |
| 2026-09-24 | **Reporting only** | The race now prints the LLM spend over the window and VT bought and held beside SPY and the watchlist, and its stale note "the screen drops lines" is gone: since 2026-09-23 the screen is off and no-answer lines leave every arm. Section 8. |
| 2026-09-24 | **Model watch** (operational, not a decision rule) | The owner replaced a standing "never revert to Opus" instruction with three triggers that stop and go to the owner. Section 10. |
| 2026-09-24 | **Amendment policy** (new registration) | Asked by the owner, with the rules above. The Status paragraph and section 7 said only bug fixes could amend this file; they now also allow the owner's dated new registrations, each of which must say why and whether any result it could have been fitted to existed. Made before any trade in the decision window resolved. |
| 2026-09-24 | **Bug fix**: a VT day the price source never prints no longer holds every look | The index test treated any unpriced VT day as an outage and made the look wait. The price source has no VT bar for 2026-09-22 (it has SPY's and NVDA's; confirmed from its raw rows on 2026-09-24), so one such day inside the window would have held every look unreadable for good and the race could never decide. A missing day now makes the look wait until the source has published five later VT sessions without it; then that entry day is left out of the index comparison only, for every arm alike, and the count is printed. Five is a week of data after the gap, well past the day or two a late bar takes. 2026-09-22 is before the cutoff, so no look is affected today; no trade in the decision window had resolved. |
| 2026-09-24 | **Incident: trigger (c) tripped; the owner decided to continue** | On 2026-09-23 and 2026-09-24, 61 of 123 calls failed: 3 read timeouts on 2026-09-23, and all 58 calls on 2026-09-24 got HTTP 401 because the key chain picked another provider's key (fixed in PR #112). Trigger (c) tripped and the process stopped for the owner, as section 10 requires. The owner decided the failures were our setup, not the model, and the experiment continues. No rule of the race changed. |
| 2026-09-24 | **Model watch: setup errors are not model errors** (the owner's decision) | Failed calls are split into setup errors (our key or configuration; shown, not counted) and model errors (counted by (c)); (c) counts from 2026-09-25; and a run with more than 20% of its calls failed, of either kind, pages the owner the same day. Section 10. Operational: it touches no decision rule and no result. |
| 2026-09-24 | **Made consistent with the planned looks** (no rule change) | Section 6 called any partial window exploratory and section 4 counted from the registration date; both now read as the planned looks and the 2026-09-23 cutoff require, so an early stop at a look is not contradicted by this file's own text. |
| 2026-09-25 | **Trigger (a) tripped; the owner kept gpt-oss** (the owner's decision) | The zero-shorts replay (gpt-oss-120b at the production settings on the lines Opus answered 2026-09-15 to 2026-09-22; 171 of 256 contexts paired, the rest lost to timeouts and rate limits under the test's own load; cost $0.39) found gpt-oss shorting on 1 of the 31 lines where Opus shorted, far below a quarter, so trigger (a) tripped and the process stopped for the owner. The owner decided to keep gpt-oss in production and not revert to Opus, because there is no evidence yet that shorts added value, and the index-first rule already means a long-only model must beat VT to win. The model arm is therefore effectively long-only. Trigger (a) was a one-time check and is closed; (b) and (c) stay active. No rule of the race changed. |
| 2026-09-25 | **Reporting only** (exploratory) | Asked by the owner. The race also prints, from 2026-09-23, the model's, momentum's and the hybrid's trades by conviction group (0.30-0.40, 0.40-0.50, 0.50-0.60, 0.60 and above; the coin flip's conviction is one fixed number, so it is not split), and every arm's trades split into longs and shorts, with the number of trades, the mean net return and the hit rate, and "too few" until a group or side has 20 trades. Shown on the 4 Funds page too. They decide nothing and change no rule. |
| 2026-09-25 | **Calibration fail rule** (the owner's decision; calibration of the shadow funds, not a rule of the race) | Replaces "restart the 15 days from zero". A fail is fixed and logged in this table; the fixed simulation is re-run on every calibration day so far from the same starting snapshot and every day must pass again; at least 5 calibration days must come after the last fix, so calibration ends at day 15 or the last fix + 5 days, whichever is later; a re-run that fails on an earlier day is a new fail; a "reason" that turns out to be a bug is a fail. If the end moves, the fund test's start date and bars are recalculated and logged. `docs/shadow-funds.mdx`. |
| 2026-09-25 | **Run timing and late runs** (operational, not a decision rule) | GitHub delivered the heartbeat's scheduled runs hours late on every day so far: the 12:35 UTC pre-market slot arrived between 17:11 and 18:17 UTC on 21-24 Sep and had not arrived by 15:00 UTC on 25 Sep, and every cycle since 21 Sep was started by a backup dispatch at about 15:05 UTC. Every cycle day so far (2026-09-15 to 2026-09-25) ran during the session, 44 to 154 minutes after its schedule; **none ran before the open.** The daily run now starts after the open (14:40 UTC: 10:40 New York in summer, 09:40 in winter), with a watchdog that starts a missing run and pages the owner, and no cycle starts after 14:30 New York (11:30 on a half day) unless a person re-runs the day by hand. From the first heartbeat cycle after this change, every journal line the cycle writes records what started its run and how late it was (the run block), and the race prints each cycle day's timing with late-run days marked (`analysis/run_timing.py`; `run_timing` in `logs/race_gate.json`); nothing that decides reads it. **The entry rule is unchanged**: every arm, the coin flip and VT enter at the open of the next session after the signal's day, checked by reading the code and pinned by `tests/test_race_entry_timing.py` for lines in the session, after the close, after midnight UTC, before the open, on a Friday, before a holiday and on a day the price source never printed, so a late run changes when a signal is made, never the price it is entered at. The code reads section 2's "the session after the signal" as the first session after the signal's UTC calendar day: a line written before the open, or after midnight UTC (20:00 New York in summer, 19:00 in winter), can enter up to one session later than the earliest open after it, never earlier; no line has been written at either time. No decision rule changes. This file stated no run time, so nothing else in it needed correcting. |
| 2026-09-25 | **Calibration: late-run mirroring** (the owner's decision; calibration of the shadow funds, not a rule of the race) | Changes calibration only: not the race, not the funds. On a day the real paper account's run fell outside market hours (before 09:30 or after the close in New York: 16:00, or 13:00 on a half day), the calibration copy does not make the entries the real broker refused as "market is closed", nor a profit-ladder pass the journal says could not run; each is counted and shown on the 4 Funds page, and none is a difference. A refusal made during market hours is never mirrored: it stays a difference. The mirror goes line by line: when a later run the same day traded the name, the refused line is still not made and the accepted line is traded as usual. **If more than 2 calibration days need this, calibration stops** and the owner is told (a warning in the daily health check and the brief): late runs on that many days are a schedule problem to fix, not something to copy around. A day is counted the evening its cycle is journalled, not when the copy reaches it. A stopped calibration gives neither a pass nor a fail and no end date, and the fund test's start is not worked out from it, until the owner decides. The line is added to the calibration pass rule (`shadow/calibration.py`) and to `docs/shadow-funds.mdx`. Made before calibration started: no calibration day exists yet. |
| 2026-09-26 | **Trigger (b) retired, drawdown trigger (d) added** (the owner's decision; operational, not a decision rule) | The owner's words: "Trigger (b): replace it. The model is now long-only by my decision, so (b) would only tell us that SPY fell. Retire it. Replace it with a drawdown trigger on the real paper account: stop and tell me if equity falls more than 8% below its highest point since 23 Sep, or if it falls more than 5 percentage points behind VT over the same period." (b) is no longer evaluated; the race prints that it is retired. (a) stays closed and (c) is unchanged, its window not reset. **Definitions of (d)** (`analysis/decision_gate.py`, `drawdown_watch`): the account's equity is its daily closing equity as Alpaca's portfolio history reports it, recorded read-only after every heartbeat run in `logs/account.jsonl` (every line's history, a later line winning a day, and a value taken only from a line recorded after that day's 16:00 New York close), plus the latest line's own equity for its New York day when that is a trading day newer than every close and the line was recorded after that day's close; days before 2026-09-23 are ignored. **(d) trips only on closing equity** (final closes, after the 16:00 New York close). A latest line recorded during the session is a mid-day reading: the race shows it on its own line and in `logs/race_gate.json` (`watch.d.midday`), measured the same way (against the peak of the closes before it, and against VT's last final close), and when it is below the 8% line or more than 5 points behind it adds a separate warning marked mid-day (`watch.d.midday_warning`). A mid-day warning does not trip (d), moves no peak, and raises no (d) alarm in the daily health check; that day is judged at its close. *Drawdown*: the peak is the highest closing equity from 2026-09-23 to the day, that day included; the day trips when equity < peak × (1 − 0.08), i.e. more than 8% below the peak (exactly 8% does not). *Behind VT*: both returns run from the same base, the 2026-09-23 close, to the same day's close: account equity ÷ its 2026-09-23 close − 1, and VT's close ÷ its 2026-09-23 close − 1, VT final closes only. 2026-09-23 is the base because it is the first day of the period with a close for both (the price source has no VT bar for 2026-09-22). The day trips when account return − VT return < −0.05, i.e. more than 5 percentage points behind (exactly 5 does not). A day with no final VT close is not judged on this part; the drawdown part still is. Every day that trips counts; the race shows the latest drawdown from the peak and the latest gap to VT in points whether or not it tripped, and a missing or unreadable account record reads "not judged: no account record". A trip means stop and tell the owner: the race prints it, `logs/race_gate.json` carries it (`watch.d`), and the daily health check raises a warning (not critical) that the brief sends to the owner's phone. Nothing reverts or trades because of it, and nothing that decides the race reads it: no look, bar or verdict changes. |
| 2026-09-26 | **Bug fix**: the model call's retry had a limit it could almost never meet (the owner's decision) | A full-model call that timed out was asked once more with a 120-second limit, against 300 seconds for the first ask. Only 29-45% of the model's successful answers on 23 and 25 Sep arrived within 120 seconds (median 130-146 s), so the second try almost never succeeded: on 25 Sep it failed 7 times out of 7, and all 7 names were lost. The second try now gets the same 300 seconds (`orchestrator/llm.py`, `TRANSPORT_RETRY_TIMEOUT_SECONDS`). This changes no model, provider, prompt, answer length or reasoning effort; only how long we wait. Each ask is now logged (ticker, first or second try, start, duration, answer length), and the error text counts the asks actually made. Trigger (c) is unchanged: its window is not reset and timeouts still count as model errors. No decision rule changes. |
| 2026-09-26 | **Storage change: the journal is one file per month** (the owner's decision; not a rule change) | The journal grows by about 0.64 MB a trading day, and GitHub refuses a push carrying a file over 100 MB, which the single file `logs/signal_journal.log` would have reached in spring 2027, before the verdict; from then no cycle's journal could have been committed. The owner approved splitting it into one file per UTC month, `logs/journal/YYYY-MM.log`, before the fund test starts. The old file was moved whole to `logs/journal/2026-09.log` (every line in it was from September); a line is written exactly as before, only into its month's file; and every reader joins the months in order (`config/journal_files.py`), so every reader sees the old file byte for byte. Checked: the joined months hash to the old file (sha256 `26b6e7a2…a483d`, 6,972,754 bytes; `tests/test_journal_files.py`), and the race, its gate and the funds, calibration included, give byte-identical output before and after the split on the same prices (`.github/workflows/journal-split-check.yml`). No line, rule, window, bar or result changes. |
