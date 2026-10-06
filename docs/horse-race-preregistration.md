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
| Fund test | the funds act on the cycle of **2026-09-28**, first fund session **2026-09-29**; counted only after calibration passes; read at the race's looks, planned bars **t > 3.40, 2.41, 2.02**. See sections 11 and 12. |
| Exploratory tests | A (momentum with a 200-day average veto), B (10-month average timing on VT), C (pullback limit entry), and the three exploratory funds: results only at the race's looks, with Benjamini-Hochberg and the Deflated Sharpe Ratio. They cannot change the decision. See section 13. |
| After-tax gate | **from 2026-10-02**: the arm that would win must also beat the VT fund after Israeli tax, "if sold today", at the same bar, with the fund test's Newey-West test (lag 5). Every tax number is in `config/israel_tax.py`. See section 5c. |
| Verdict disclosure | **from 2026-10-02**: if VT never fell 10% from its high inside the test window, the verdict is labelled "not tested in a downturn" and any real-money step starts small. A label and a policy, not a rule. See section 5d. |
| Prepared, not registered | the IC report of the model's scores: **registered at the 2026-12-22 checkpoint**, counters only until then. Shadow stock universe (`SHADOW_UNIVERSE_ENABLED`): **off** until **2027-01-01**; `tests/test_shadow_universe.py` fails if it is turned on before that date. See section 13.9. Voting arm `model_vote` (`MODEL_VOTE_ENABLED`): **off** until **2026-12-22**, registered at that checkpoint; `tests/test_model_vote_runner.py` fails if it is turned on before that date. See section 13.11. Thesis-check logger (`THESIS_CHECK_ENABLED`): **off** until **2027-04-01**, registered at the 2027-03-22 checkpoint; `tests/test_thesis_check_runner.py` fails if it is turned on before that date. See section 13.12. |

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

**Then the after-tax gate (Amendment 2026-10-02, section 5c).** The arm that
beats VT must also beat the VT fund after Israeli tax, on an "if sold today"
basis, at the same bar. If it does not, it does not win: at the final look no
arm trades.

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
  test and its after-tax gate (section 5c): one of the four outcomes, always,
  once the look's after-tax record exists.
- **At looks 1 and 2** an early stop is allowed in either direction, but only
  if the bar is met in the direction it stops:
  - *for the model*: it beats momentum and the hybrid at t above the bar,
    and its coin-flip condition holds; or
  - *against the model*: it trails the replacement (momentum, or the hybrid
    if the hybrid beat momentum at the bar) at t below minus the bar.
  
  The index test then has to be decisive too: the picked arm beats VT at t
  above the bar (that arm is the answer, if its fund also beats the VT fund
  after Israeli tax at the bar, section 5c; otherwise the look decides
  nothing), or trails it at t below minus the bar (no arm trades). Anything
  else decides nothing, and the race goes on.
- **No decisions between looks**, and none after a look has decided. Each
  look is computed on its own first 60, 120 or 180 entry days only, so it
  says the same thing every night after it is reached.

## 5b. Where the gate lives

`analysis/decision_gate.py` holds the cutoff, the minimum sample, the looks,
their bars and the index ticker; `analysis/horse_race.py` applies them on
every run and prints the verdict of every look reached. `tests/test_horse_race.py`
fails if any of them differs from this file.

## 5c. The after-tax gate (Amendment 2026-10-02)

The owner's new registration of 2026-10-02. It adds one condition to the
index-first step, in the race (sections 5 and 5a) and in the fund test
(section 11.6, step 3, and section 11.8): **the arm that would win must also
beat the VT fund after Israeli tax, on an "if sold today" basis, at the same
bar and with the same Newey-West test.** It changes no arm, no metric, no
look and no bar.

**The series.** For the picked arm's fund (`model`, `momentum` or `hybrid`,
section 11.1) and for the VT fund, on every fund session:

- *after-tax equity* = the fund's equity at the close minus the tax that
  would be due if every position were sold at that close. A year's tax is
  never below 0;
- *after-tax daily return* = after-tax equity today ÷ after-tax equity at
  the previous close − 1 (the first session from the $100,000 start);
- the paired difference is the arm's fund minus the VT fund, day by day,
  over the fund sessions from 2026-09-29 to the close of the look's last
  trades, with the fund test's Newey-West t, **lag 5** (section 11.4).

**The bar** is the bar of the step it belongs to: the race's look bar in
section 5a (3.47, 2.45, 2.00), the fund test's bar in section 11.7.

**When it is made.** Once, by the funds run (`shadow/run.py`,
`shadow/after_tax.py`), on the first night from the night the race reaches
the look on which the race can read the look, the funds run has its rate
table, and the funds' prices reach the close of the look's last trades. It is
cut at that close, kept unchanged after, and the race reads it back
(`analysis/horse_race.py`, `analysis/decision_gate.py`). A record cut at
another close (a bug fix re-ran the race and moved the look's window) is not
read: the look waits, and the record is made again at the new close on the
first night the same conditions hold, with the old one kept inside it; a
record that says the test could not be met (calibration had not passed) is
never made again. A look that would pick an arm waits for its record, as it
waits for a price. If calibration has not passed
on the night the race reaches the look, no fund is run, and the test cannot
be met at that look: an early look then decides nothing for an arm, and at
the final look no arm trades.

**It only stops an arm from winning.** It never decides anything by itself.
At an early look, "no arm trades" still comes only from the index test
before tax (the arm trails VT at t below minus the bar).

**The tax rules** (the owner's, 2026-10-02; every number in
`config/israel_tax.py`; applied by `analysis/israel_tax.py`):

a. Gains and losses on USD securities are measured in shekels with the
   exchange rate as the index (Income Tax Ordinance s.88; Tax Authority
   Circular 10/2025). cost_ILS = cost_USD × fx_buy. proceeds_ILS =
   proceeds_USD × fx_sell. nominal = proceeds_ILS − cost_ILS. infl =
   cost_ILS × (fx_sell / fx_buy − 1). If nominal ≥ 0: taxable gain =
   max(0, nominal − max(infl, 0)). If nominal < 0: allowable loss =
   min(0, nominal − min(infl, 0)). So the tax is on the smaller of the
   shekel gain and the dollar gain at the sale-day rate, and a loss caused
   only by the exchange rate is not deductible.
b. Rate 25%. A surtax, as parameters: 3% on taxable income above
   721,560 ILS, plus 2% on capital income above the same line. Off by
   default at these account sizes; the salary is an input and is never
   stored in the repository.
c. FIFO lots, per account. Every reinvested dividend is a new lot.
d. Dividends: Israeli tax is 25% of the gross shekel amount, with a credit
   for the US tax withheld (25% with a W-8BEN). Extra tax = the difference
   (usually 0).
e. Loss offset: this year's capital losses go first against this year's
   capital gains. `offset_losses_vs_dividends` (default on, the harsher
   case for an actively traded fund) also sets a year's net capital loss
   against that year's dividends; it waits for the accountant's answer.
   What is left carries forward against future capital gains only,
   nominal, with no expiry.
f. The exchange rate is the Bank of Israel's representative rate on the
   trade date. Another source (the European Central Bank's reference rates,
   crossed through the euro) only for a day the Bank did not publish; if
   neither has the day, the Bank's latest earlier rate. Every such day is
   counted (`analysis/boi_rates.py`).

Five conventions the rules leave open, fixed here: (1) a short sale is a lot
opened by a sale and closed by a purchase, with the purchase as the cost (at
its day's rate) and the sale as the proceeds (at its day's rate); (2) a
dividend a short position pays is an allowable loss on the day it is
charged; (3) the funds credit dividends gross, so the after-tax equity also
takes off the US tax withheld, a dollar amount; (4) "if sold today" sells at
the close with no selling cost, as the equity it is taken from is marked;
(5) tax for a finished year is turned into dollars at that year's last rate
in the walk, the current year's at the day's own rate. The first two are not
among the owner's questions to the accountant of 3 Oct 2026 and stay as
written here; the third, fourth and fifth are how the books are kept, not tax
questions. When tax is really paid during the year (the half-year advance
payments) is the accountant's question 7 (`docs/research/cpa-questions.md`).

The owner's ten cases (fees 0, tax 25%) are unit tests,
`tests/test_israel_tax.py`, T1 to T10. T5 (a nominal loss smaller than the
exchange-rate loss is not deductible) is the owner's reading of the
circular's two-step rule and **needs confirmation** by the accountant
(`docs/research/cpa-questions.md`, question 1); it is not treated as
confirmed.

**For information only, not a gate:** the extra pre-tax return a year an
actively traded fund needs to tie with VT held for 20 years, from the
simulator (`analysis/tax_breakeven.py`; inputs: growth and dividend yield).
At 6% growth and a 2% yield it is 0.82 points a year (the owner's rough
estimate was about 0.8); at 5% growth, 0.62; at 8%, 1.26.

**Made before any checkpoint result existed**: on 2026-10-02 the first
checkpoint was estimated for 2026-12-22, the race had 1 of 20 independent
days, and no fund result had been computed (calibration was on day 2 of 15).

## 5d. Verdict disclosure (Amendment 2026-10-02)

The owner's new registration of 2026-10-02. **If VT's maximum drawdown from
its high inside the test window is below 10%, the final report labels the
verdict "not tested in a downturn", and any real-money step starts small.**

- The test window runs from 2026-09-23 (the decision cutoff) to the close of
  the last trades of the look that decides. The drawdown is measured on
  VT's final closes with each dividend added back on its ex-date (the index
  test's own treatment: a dividend is not a fall), from the highest level
  inside the window (`analysis/decision_gate.py`, `vt_max_drawdown`,
  `DOWNTURN_DRAWDOWN`; `analysis/horse_race.py`, `total_return_closes`).
- The race prints it at every look reached, and on the look that decides it
  adds the label to the verdict and to the status line.
- This is a label and a policy. It does not extend the test, move a look,
  or change an outcome.

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
- **Tests A, B and C, and the three exploratory funds** (sections 11.1 and
  13). Their results are read at the checkpoints only.
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
test and its after-tax gate (section 5c) — is met. If it is not met, the
answer is to hold the index. If the verdict is labelled "not tested in a
downturn" (section 5d), any real-money step starts small. Until then every
arm is shadow-only and the book is Alpaca's paper account.

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

## 11. The fund test (Amendment 2026-09-24)

The race (sections 1 to 5a) judges each arm's calls one trade at a time:
three sessions each, no portfolio, no cash. The fund test asks the question
the race cannot: what does each arm do with a whole book, run by the same
machinery that runs the paper account?

### 11.1 The funds

| Fund | Signals | Machinery |
| --- | --- | --- |
| `model` | the journal's own answers | the production `ExecutionEngine` and `PositionManager` |
| `momentum` | `rules/momentum.py` on each line's technicals | the same |
| `hybrid` | `rules/hybrid.py` on each line's technicals and `news_score` | the same |
| `vt` | none: VT bought once at the first open with all the cash, and held | outside the engine (the engine would size VT at 5% and put a stop under it) |
| 1,000 coin-flip funds | `rules/control.py`, seeds 0 to 999, on every line | the same as `model` |
| `model_by_conviction` (exploratory) | the model's own answers | the same as `model`, except that each cycle's lines are dispatched highest conviction first (ties in watchlist order) instead of in watchlist order |
| `model_sized` (exploratory) | the model's own answers | the same as `model`, except that each new position's size is the normal size times 0.25, 0.5, 1.0 or 1.5 for conviction 0.30-0.40, 0.40-0.50, 0.50-0.60, 0.60 and above |
| `model_same_day` (exploratory) | the model's own answers | the same as `model`, except that each line is entered on its own day, at the price recorded when its signal was made, instead of at the next open |

Each starts with **$100,000 of cash**. The machinery is the production code,
not a copy: position sizing, the ATR stop, the profit ladder (a third off at
+1R with the stop to break-even, a third off at +3R with the stop to +1R),
the trailing stop, the exposure-group caps and trims, the conviction floor,
the position count and the gross, sleeve and stock-market limits
(`shadow/fund.py`). Only the broker is simulated (`shadow/broker.py`).

**The three exploratory funds** (the owner's decisions of 2026-09-25 and,
for `model_same_day`, 2026-09-26) start on the same day, pay the same costs
and follow the same rules as the others. Each answers one question against
the `model` fund, which uses the same signals: does the buying order matter
(`model_by_conviction`), does sizing by conviction help (`model_sized`), and
does buying on the signal's own day, as the paper account does, change the
result (`model_same_day`)? They **cannot change the decision** (section 11.6
reads the four funds only). For each, the fund
output and the 4 Funds page show its total return against the model fund's,
the mean daily difference with its Newey-West t (lag 5), and, for
`model_sized`, its maximum drawdown beside the model fund's, since bigger
positions can mean bigger losses. These are shown only at the checkpoints
(section 13.1, Amendment 2026-09-28); between them, only counters. In this system the "normal size" is the
per-ticker cap (5% of equity for a company, 12% for a broad fund, and so
on); the ATR only sets the stop. `model_sized`'s engine reads that cap times
the conviction factor, for its own entries only: production code is not
changed, and every portfolio limit (exposure groups, sleeve budget, gross
exposure, stock-market, position count) still applies. Production and the
calibration copy keep watchlist order and the normal size.

**`model_same_day`** uses the price recorded on each journal line when its
signal was made (the line's `live` record, on every cycle line since
2026-09-28): a buy fills at the recorded ask, a short at the recorded bid,
or at the recorded last trade when there is no quote, plus the same 0.10%
cost. The entry is made after that session's stop checks for the positions
already held, so a new position's stop is first checked at the next
session's open. A line with no recorded price, or recorded outside regular
New York hours (when the real broker would have refused the order), is not
entered by this fund, and each one is counted. Everything else (the position
manager, sizing, stops, caps, costs) is the same as `model`.

Every fund's closed trades are also reported split into longs and shorts
(number, mean net return, hit rate; "too few" under 20). Report only.

Signals come only from the journal (`logs/journal/`, one file per month,
read joined): no new model call. A line the model gave
no answer on, or that the paper account held (so the model was not asked),
is skipped by every fund that day — the race's own rule (section 3). That
holds for both kinds of failed call (section 10): a setup error and a model
error alike leave the line with no answer, so no fund trades it.

**Known limitation: held names.** The model is not asked about a name the
paper account already holds (22 of the 80 names on 2026-09-26), so no fund
can trade that name that day, whatever its own book holds. This is the same
for every fund, so it is fair between them, but it ties every fund to the
real account's positions: a name the real account holds for weeks is out
of every fund's reach for those weeks. The number of names skipped for this
reason is reported every day (in `logs/funds.json` and on the 4 Funds page).

### 11.2 The day, for every fund alike

A cycle journalled on day D is acted on at the open of the next session,
the race's entry rule. At that open: stops the price gapped through fill at
the open; the position manager runs; then the entries, one line at a time.
During the session, stops the day's low (high, for a short) reaches fill at
the stop. At the close: dividends are credited to longs and charged to
shorts; the book is marked. That mark is the fund's equity for the day.

- **Prices and finality**: the race's own (`OhlcFetcher`, `auto_adjust=False`,
  final closes only). The exact price table each nightly run used is kept:
  its SHA-256 in `logs/funds.json` (`prices_sha256`, in git) and the table
  itself in the Supabase archive (and as a 90-day workflow artifact), so any
  fund result can be checked again on the prices it was computed from.
  Nothing in the fund test reads the archive; git stays the record.
- **Costs**: 0.10% of notional per side on every fill, stops included.
- **Priority** (the owner's decision, 2026-09-24): when there is more to buy
  than the caps allow, lines are dispatched in **watchlist order**, one at a
  time, each seeing the fills before it — the order production uses, which
  calibration needs. It is not changed, in the simulation or in production.
  How often it matters is reported, not acted on: for the real account and
  every fund, the days the book ran out of room (cash, the gross cap, the
  sleeve budget, an exposure-group cap, the stock-market limit, the position
  count) before the end of the list, the signals skipped with their
  conviction, and whether a skipped signal had a higher conviction than one
  that was bought (`shadow/order_matters.py`; a running count on the 4 Funds
  page and in `logs/funds.json`).
- **Held names**: a fund never adds to a name it already holds, as production.
- **Shorts** (the owner's decision, 2026-09-26): a fund may not short a name
  the paper account has refused to short (LQD, XHB, HYG, EWA, TUR, USO so
  far, read from the live audit log). A refusal counts only from the day it
  happened, never backwards: a fund acting on a cycle journalled on day D is
  blocked only by refusals recorded on day D or earlier, so a new refusal
  can never change a past fund result. No borrow fee.
- **Cash**: may go below zero, as on a margin account; the engine's 95%
  gross cap is what bounds it at entry, live and simulated alike.
- **Price gaps** (the owner's decision, 2026-09-26): the price source
  sometimes has no bar for a ticker on a day it traded (on 22 Sep 2026 it
  had none for 27 names, VT among them, while it had SPY's). On such a day
  that ticker's position is left as it was (no stop check, no management, no
  new entry in it) and marked at its last close; its move lands on the next
  day it has a bar. The same for every fund, VT included. Every such
  ticker-day is counted and shown, never hidden, and the share of missing
  ticker-days is reported for each calendar month (missing ticker-days ÷
  watchlist tickers × sessions). If a month's share goes above 2%, the
  daily health check raises a warning and the owner's phone is told.

### 11.3 Start date

(The owner's decision of 2026-09-26, made before any fund result existed.)
The funds act on the cycle journalled on **Monday 2026-09-28**, from the
next open: the first fund session is **2026-09-29**, and the fund test's
sample runs from that session. Days before it are not counted, whatever
they would have shown, and are never computed for display.

The fund test still **counts only after calibration passes** (section 12).
Until then no fund result is calculated or shown. When calibration passes,
every fund is run with the final, checked code from 2026-09-28 onward. If
calibration needs fixes, fund results are calculated only with the fixed
code, always from 2026-09-28. A fix made during calibration may be motivated
only by a calibration difference (section 12), never by a fund result, since
none exists until calibration has passed. The start date does not move if
calibration is delayed; only the reading waits.

A look that comes before calibration has passed is skipped by the fund
test: it is not read, no part of the 5% is spent at it, and the next look's
bar comes from the same rule (11.7).

### 11.4 The metric

**Mean daily net return, fund minus fund, paired, with a Newey-West t.**

- A fund's daily net return is its equity at the close over its equity at
  the previous close, minus one: costs and dividends are already in it.
- The paired series is fund A's daily return minus fund B's, on every
  session from the start date, every fund on the same sessions.
- **Lag 5** (the owner's decision, 2026-09-26), one trading week. Unlike the race, a fund's daily
  returns do not overlap by construction — each day's return is that day's
  price change on the book held — so the lag of 3 that the race needs for
  its overlapping 3-session trades has no counterpart here. What remains is
  residual autocorrelation from a book that changes slowly and from
  volatility that clusters. The textbook plug-in lag,
  floor(4 × (T/100)^(2/9)), is 3 at 60 sessions and 4 at 120 and 180; a
  fixed 5 is slightly more conservative than all of them and does not move
  between looks.

### 11.5 The random band

The 1,000 coin-flip funds give, each day, the 5th to 95th percentile of what
luck alone did with the same machinery on the same lines. Like race
condition 3 (the owner's decision, 2026-09-26), the model fund is kept only
if its total return from the start date is above the **95th percentile of
the coin-flip funds' total returns** at that look.

This condition is weak for a buy-only model in a rising market: a coin flip
goes short about half the time, so in a market that mostly rises almost any
fund that only buys will beat most coin-flip funds, whether or not its
choices are any good. The real protection is the index rule (11.6, step 3):
the picked fund must also beat VT, bought and held.

### 11.6 The decision rule, at each look

The same shape as the race (sections 5, 5a):

1. **Keep the model fund** if, at the look's bar, it beats the momentum fund
   and the hybrid fund on the paired metric, and condition 11.5 holds.
2. Otherwise the replacement is the momentum fund, unless the hybrid fund
   beats the momentum fund at the bar.
3. **Index first**: the picked fund must beat the VT fund on the same paired
   metric at the bar, and also after Israeli tax (section 5c). If it does
   not, no arm trades: hold the index.
4. Early stops at looks 1 and 2 only, in either direction, only with the bar
   met in the direction the look stops — exactly as section 5a.

### 11.7 Looks: the race's days, the fund test's own bars

The fund test is read **on the same days as the race's looks** — the day
the race reaches 20, 40 and 60 independent days (estimated 2026-12-22,
2027-03-22, 2027-06-16) — using every fund session from its start date to
that day. So both tests are read together, never one without the other.

Its **bars are its own** (the owner's decision, 2026-09-24): they follow the
fund test's own share of its final data at each look, not the race's.
Planned: the first fund session 2026-09-29 (11.3). That gives **60, 120 and
180** fund sessions at the three looks — shares of 1/3, 2/3 and 1.

**How the bars are set** (the owner's decision, 2026-09-26: one rule, fixed
now, no judgment later). The bars come from an **O'Brien-Fleming-type
alpha-spending rule** (Lan and DeMets): by a share t of the final data, at
most α(t) = 2 − 2Φ(1.96 / √t) of the 5% may have been spent, and at the
final look all of it. At each look, the bar is the one that brings the
chance of having crossed any bar so far, when there is no difference,
exactly to α(t) at that look's share — given the bars already used at the
earlier looks, which never change. The share is the look's actual fund
sessions ÷ the planned final sessions (180); the final look always counts
as share 1. Computed exactly by numerical integration
(`analysis.decision_gate.spending_bars`, the same integration that gives the
race's bars), rounded up to two decimals, so a registered bar is never below the exact one.

With the planned sessions this gives:

| Look | Fund sessions | Share | Spent by then | Bar (exact) | Bar (planned) |
| --- | --- | --- | --- | --- | --- |
| 1 (≈ 2026-12-22) | 60 | 0.333 | 0.069% | 3.395 | **3.40** |
| 2 (≈ 2027-03-22) | 120 | 0.667 | 1.64% | 2.407 | **2.41** |
| 3 (≈ 2027-06-16) | 180 | 1 | 5% | 2.015 | **2.02** |

These are within 0.08 of the classic O'Brien-Fleming bars for the same
shares (3.47, 2.45, 2.00, the race's own), which a spending rule
approximates; unlike them, a spending rule stays correct when a look falls
on another day than planned. The same caveat as the race: the Newey-West t is close to normal,
not exactly, so the true error rate at the first look may be a little
higher.

**If the look days move** (the race's looks land on other days), or a look
is skipped because calibration has not passed (11.3), nobody chooses new
bars: at each look the bar is computed by
the rule above from the fund sessions actually there, and the number is
logged in the Amendments table the day it is used. Bars already used at
earlier looks stay as they were. The planned numbers are pinned in the code
(`shadow/schedule.py`, and a test that recomputes them).

### 11.8 What decides real money (the owner's default)

**Real money only if the same arm wins both the race and the fund test, and
its fund beats the VT fund at that look's bar, before and after Israeli tax
(section 5c).** If the race and the fund
test disagree — different winners, or one of them decides "no arm trades" —
the answer is the index. And section 9 still holds: no real money in this
system before the June 2027 verdict, whatever an earlier look says.

### 11.9 After-tax and shekel reports (Amendment 2026-10-02; reporting only)

Asked by the owner on 2026-10-02. They use the rules of section 5c, never a
flat 25%, and decide nothing beyond section 5c's own test.

- **After tax.** For the real paper account, the four funds (`model`,
  `momentum`, `hybrid`, `vt`): before and after tax side by side, in
  dollars and in shekels, with "tax paid so far" (the tax due on everything
  realised so far: every finished year, plus this year's gains, losses and
  dividends as if the year ended today) and "if sold today" (that, plus
  every open position sold at the day's close). The paper account is shown
  every night from now; the funds like every fund result, once calibration
  has passed. **Exploratory funds: after-tax results only at the
  checkpoints**, in the checkpoint record (section 13.1). If the rate table
  is missing on a checkpoint's night, that record says the exploratory
  funds' after-tax view is not available, and it is not made later.
- **In shekels.** The same results in shekels at the Bank of Israel's
  representative rate (daily; another source only for a missing day, and
  those days are counted), next to the dollar results, and **how much of
  each result came from the USD/ILS change** (the shekel return minus the
  dollar return). The rate table is kept like the price table: its SHA-256
  (`rates_sha256`) in `logs/fx_rates.json` and `logs/funds.json` in git, the
  table itself in the archive (the scoring-prices artifact).
- **The paper account** is rebuilt from its own fills in `logs/account.jsonl`
  (FIFO, at the prices Alpaca filled; no fees, as the paper account charges
  none). Alpaca's record carries no dividends, so none are taxed there; the
  lots rebuilt are checked against the positions the account reports.
- Where: `logs/funds.json` (`after_tax`), `logs/after_tax.md`, and the
  4 Funds page.

## 12. Calibration (before the fund test counts)

A copy of the model fund starts from the paper account's real positions,
cash and stops (from `logs/account.jsonl`, recorded read-only by the
heartbeat) and follows the same signals for **15 trading days**. It pays no
trading cost, because the paper account charges none (the owner agreed).
Every day: its equity against the real account's closing equity, and every
trade that differs, with the reason. During calibration only this match is
reported; the four funds are not run.

**The pass rule (approved by the owner on 2026-09-24).** Calibration passes
only if all six hold over the 15 trading days:

1. On every one of the 15 closes, the simulated equity is within 1.0% of
   the real account's equity.
2. The tracking error of daily returns (the spread of sim minus real, day
   by day) is at most 0.20% a day.
3. At least 90% of the real account's trades (entries, ladder/trim closes,
   stop exits) are matched by the same trade in the sim within one session.
4. No unexplained difference: every trade that differs names a reason from
   the fixed list.
5. Integrity: no unexpected engine error, no position-manager error, every
   sim position's stops cover it, and no line reached the live audit log.
6. The other way round: at least 90% of the sim's trades are also made by
   the real account within one session.

**If calibration fails** (the owner's rule of 2026-09-25):

- the cause is fixed and logged in the Amendments table (and in
  `shadow/schedule.py`'s `CALIBRATION_FIXES`);
- the fixed simulation is re-run on every calibration day recorded so far,
  from the same starting snapshot, and every day must pass all the
  conditions again;
- at least **5 calibration days must come after the last fix**, so
  calibration ends at day 15 or at the last fix + 5 days, whichever is
  later;
- if a re-run fails on an earlier day, that is a new fail: fix, log and
  re-run again;
- a difference whose stated reason turns out to be a bug counts as a fail;
- if the calibration end date moves, the fund test's start does not
  (section 11.3); a look that comes before calibration has passed is
  skipped, and the bars are computed by the rule in section 11.7.

**Late runs** (the owner's decision of 2026-09-25; calibration only, not the
race and not the funds): on a day the real account's run fell outside
market hours, the sim does not make the entries the real broker refused as
'market is closed', nor a profit-ladder pass that could not run; each is
counted and shown. If more than 2 calibration days need this, calibration
stops and the owner is told. A refusal made during market hours is never
mirrored: it stays a difference. A stopped calibration gives neither a pass
nor a fail and no end date, and the fund test's start is not worked out
from it, until the owner decides.

The 4 Funds page shows the calibration days passed, the date of the last
fix and the days since it (X of 5). The fund test does not start on a failed
calibration.

The rule takes effect with the start date, as soon as the first complete
account snapshot exists: 2026-09-28 (checked after that day's cycle: the
account, positions and stops were all read). The rule is in force and
calibration started with that day's close (Amendments, 2026-09-28). The
fund test's start is 2026-09-28 too (11.3).

## 13. Exploratory tests A, B and C (Amendment 2026-09-28)

Three exploratory tests, asked by the owner on 2026-09-27. They are
exploratory in the sense of section 6: **none of them can change the
decision** (sections 5, 5a, 11.6 and 11.8 read the registered arms and the
four funds only), and none changes any rule, look or bar. Every setting is
fixed here, from a published source where there is one. No model takes part
in them: code computes everything.

**The owner's note (2026-09-28):** History screens of A, B and C were run
by the owner on 2026-09-27, after their settings were fixed (including A's
200-day average) and before this section was committed. No setting was
changed after seeing them. No live result of A, B or C existed.

### 13.1 Hidden until the checkpoints

- A **checkpoint** is the day the race reaches one of its planned looks
  (section 5a: 20, 40 and 60 independent days; estimated 2026-12-22,
  2027-03-22, 2027-06-16).
- **Between checkpoints, only the counters listed below are computed,
  kept or shown** for A, B and C, for the three exploratory funds of
  section 11.1 (`model_by_conviction`, `model_sized`, `model_same_day`),
  and for the insider arm (section 2). No equity, return, mean, t, hit rate
  or drawdown of theirs is written to any file, page or log. The three
  exploratory funds' counter is the lines `model_same_day` could not enter
  and why, from the 2026-09-28 cycle (the fund's start; earlier lines are not
  part of the test), counted from the journal without running the fund;
  everything else about them (their order-matters counts included) comes at
  the checkpoints. The insider arm's counters are the lines it took a side
  on and its trades, at each horizon. Its results were printed nightly from
  2026-09-22 to 2026-09-28, before this section existed; nothing is undone.
- **At each checkpoint** their results are computed once, over every day
  from their start to that checkpoint, and written to a record that is
  kept unchanged until the next checkpoint.
- Like every fund, the A, B and C funds are computed only after
  calibration has passed (section 12). A checkpoint before that shows
  their counters only.

### 13.2 Test A: momentum with a 200-day moving-average veto (race arm and fund)

- **Source:** Brock, Lakonishok and LeBaron (1992), the moving-average
  rule of price against its 200-day average. Nothing tuned. (A 50-day
  version was dropped before it ran: the momentum rule already confirms
  against the 50-day average, so it would have removed only about 1-3% of
  signals. Decided from signal counts only, with no returns looked at; it
  is in the graveyard and counts in N.)
- **Rule:** take the momentum rule's signal on each line (section 2,
  unchanged). Keep a LONG only if the live price at signal time is above
  the 200-day simple moving average; keep a SHORT only if it is below.
  Otherwise the line is NEUTRAL for this arm. Conviction is unchanged.
  - *Live price at signal time:* the line's recorded last trade
    (`live.price`, section 11.1).
  - *200-day simple moving average:* the mean of the name's last 200 final
    daily closes up to and including the close of the session before the
    signal's day, so it never uses a price from after the signal. A name
    with fewer than 200 final closes has no average, and keeps the
    momentum signal as it is; counted.
  - "Above" and "below" are strict: equal means NEUTRAL.
  - A line with no recorded live price keeps the momentum signal as it is.
    Each such line is counted.
- **Race arm:** scored exactly like momentum (3 sessions, next open, same
  stop, cost and floor), on lines journalled from 2026-09-28 (the first
  cycle with a live price). **Main metric:** mean daily net return,
  A minus momentum, over all names, on the same entry days, Newey-West t
  (lag 3), as in section 3.
- **Fund:** the momentum fund with A's signals; everything else
  identical (section 11, start 2026-09-28). **Main metric:** mean daily
  net return, A fund minus momentum fund, paired, Newey-West t (lag 5).
- **Counter:** the share of momentum's signals (LONG or SHORT, at or above
  the conviction floor) that the veto turns NEUTRAL, and the numbers of
  lines with no live price and of names with no average. **If the veto
  removes under about 10% of signals, the first checkpoint's report says
  so**: A is then almost the momentum rule, and its result says little.

### 13.3 Test B: 10-month moving-average timing on VT (fund)

- **Source:** Faber (2007; updated 2013 and 2018). Nothing tuned.
- **Rule:** on the last trading day of each month, compare VT's close with
  the average of its last 10 month-end closes (that close and the 9
  month-ends before it). **Above:** hold VT with all the fund's cash, like
  the VT fund. **Not above:** hold T-bills through BIL (SPDR Bloomberg 1-3
  Month T-Bill ETF), as Faber used T-bills. Trade at the next session's
  open, 0.10% per side: a switch sells one and buys the other at the same
  open (two sides). Dividends are credited for whichever fund is held, as
  for the VT fund. No stop and no position manager, like the VT fund.
- **Prices:** the race's daily closes, final closes only. If the price
  source never prints VT on a month's last trading day, VT's last close
  earlier in that month is used, and this is counted. Each leg of a trade
  happens at the first open where that fund has a bar; in between, the
  money is cash at 0%. Counted.
- **Start:** the first month-end after this amendment: **2026-09-30**.
  Until then the fund holds its $100,000 in cash; its first trade is at
  the next open (2026-10-01), and its sample starts on that session.
- **Compared with:** the VT fund (section 11.1). **Main metric:** mean
  daily net return, B minus VT fund, paired over B's sessions, Newey-West t
  (lag 5). Also shown at checkpoints: each fund's total return and maximum
  drawdown.
- **Counter:** the number of switches so far and the current state (in VT
  or in BIL), with the date of the last month-end signal.

### 13.4 Test C: pullback limit entry (fund)

- **Source:** none published for these settings: the owner's fixed
  choice of 2026-09-27. Nothing tuned.
- **Rule:** the same signals as the momentum fund. Instead of buying at
  the next open, place a limit buy at *signal price − 0.5 × ATR14*, valid
  for the 3 sessions after the signal's day, then cancelled. A short is a
  limit sell at *signal price + 0.5 × ATR14*.
  - *Signal price:* the line's recorded last trade (`live.price`); if none
    was recorded, the price the momentum rule read (`technicals.last_close`),
    counted.
  - *ATR14:* the line's own 14-day ATR (`technicals.atr14`), fixed when the
    signal was made.
- **Fill rule:** if a session opens at or past the limit, fill at the open;
  otherwise, if the day's range reaches the limit, fill at the limit. Cost
  0.10% per side. A session with no bar for the name (section 11.2, price
  gaps) is one of the 3 and cannot fill.
- **Everything else is identical to the momentum fund**, with these
  necessary details:
  - The engine sizes and checks the entry when the order fills, at the
    fill price. If it refuses then (no room), the order is dropped and
    counted. A pending order reserves nothing.
  - A name already held gets no order (as production). A new signal on a
    name with an order pending is ignored while that order stands; counted.
  - Order of a session: stops gapped through fill at the open; the
    position manager runs; limit orders the open fills (watchlist order);
    stops touched during the session; then limit orders filled during the
    session (watchlist order). A position filled during the session has its
    stop checked first at the next open, as in `model_same_day`, because
    the bar cannot say whether the low came before or after the fill.
- **Compared with:** the momentum fund. **Main metric:** mean daily net
  return, C fund minus momentum fund, paired, Newey-West t (lag 5).
- **Pre-registered prediction:** the fill rate is well below 100%, and the
  missed signals do better than the filled ones.
- **Counters:** for every momentum signal the funds see (from the
  2026-09-28 cycle), whether its limit would have filled within its 3
  sessions: the fill rate, and the number of filled and missed signals.
  Counted from prices alone, without running the fund.
- **At checkpoints:** the forward return of filled against missed
  signals, measured the same way for both (each signal's momentum race
  trade: next open, 3 sessions, same stop, net of cost): number, mean net
  return and hit rate of each group, and the difference, missed minus
  filled, with a Welch t. Signals on the same day are not independent, so
  that t is for reading only and is not one of the tests in 13.5. And the
  C fund against the momentum fund (its main metric).

### 13.5 At every checkpoint: Benjamini-Hochberg across all exploratory tests

- **The family:** every exploratory test with a main metric at that
  checkpoint: the insider arm (on the lines it took a side on, its net
  return minus momentum's on the same lines, 0 where momentum did not
  trade, averaged per entry day, Newey-West t lag 3), A's race arm, A's fund,
  B, C, `model_by_conviction`, `model_sized` and `model_same_day` (each
  against the fund named in section 11.1). A test with no data yet is left
  out, and the report says so.
- **p-value:** two-sided, from the normal distribution, for each test's
  Newey-West t.
- **Adjustment:** Benjamini and Hochberg (1995). With the m p-values in
  order p(1) ≤ … ≤ p(m), the adjusted p-value of p(i) is the smallest of
  m × p(j) / j over j ≥ i, capped at 1. A test **passes** if its adjusted
  p-value is at most 0.05.

### 13.6 At every checkpoint: the Deflated Sharpe Ratio

- **Source:** Bailey and López de Prado (2014).
- For each test in 13.5, on the same daily series as its main metric:
  SR = mean ÷ standard deviation (per day, not annualised), T = number of
  days, γ3 = skewness, γ4 = kurtosis (3 for a normal distribution).
- **N** = the number of trials in `docs/research/graveyard.md` on the
  checkpoint day (18 when this was registered).
- SR0 = √V × ((1 − γ) × Φ⁻¹(1 − 1/N) + γ × Φ⁻¹(1 − 1/(N × e))), with
  γ = 0.5772 (Euler's constant) and **V = 1/T**, the variance of a Sharpe
  ratio estimated from T returns when the true one is zero (Lo 2002).
- DSR = Φ((SR − SR0) × √(T − 1) ÷ √(1 − γ3 × SR + (γ4 − 1)/4 × SR²)).
- Reported for every test. **Above 0.95** means the result survives the
  number of ideas tried, at 5%. For the race arms (overlapping 3-session
  trades) the DSR is optimistic; the Newey-West t is the careful number.

### 13.7 What a result can lead to

- **Promising:** at a checkpoint, the idea beats its comparator and passes
  Benjamini-Hochberg (13.5).
- **Dead:** at any checkpoint it trails its comparator and passes
  Benjamini-Hochberg in that direction; or at the final checkpoint its
  mean difference is zero or below. **Not for B:** its purpose is crash
  protection, which 9 months may not test, so the final "zero or below"
  rule does not apply to B; B can be dead only through Benjamini-Hochberg.
- **Not tested:** at the final checkpoint, an idea that acted differently
  from its comparator fewer than 20 times, whatever its numbers: it cannot
  show anything, so it is not called dead. Acting differently is, for A,
  a signal the veto removed; for the insider arm, a trade; for
  `model_by_conviction`, a session on which the buying order changed what
  was bought; for B, a trading day spent out of VT; for C, a momentum
  signal on which C and the momentum fund did differently: one bought it
  and the other did not, or both bought it at different prices (a signal
  both skipped, because the name was held in both or neither had room, is
  not a difference); for `model_sized`, a trade whose size factor is not
  1.0 (conviction outside 0.50-0.60). `model_same_day` enters every trade
  on another day at another price, so it always counts as acting. Counted by
  code at the checkpoint.
- **Not proven:** anything else. It stays until the final checkpoint.
- A promising idea is only a candidate for a later registration. It
  changes nothing in this one.

### 13.8 Research limits

- A, B and C are the starting set. **No other new exploratory test before
  the first checkpoint (2026-12-22).**
- **From 2027-01-01: at most 2 new ideas per quarter, registered only at
  checkpoints.**
- Every idea gets a card in `docs/research/cards/` and a row in
  `docs/research/graveyard.md` before it runs, and stays in the graveyard
  after it is dropped. The graveyard's count is N in 13.6.

### 13.9 Prepared for the first checkpoint: the IC report and the shadow stock universe (Amendment 2026-10-02; not yet registered)

Asked by the owner on 2026-10-02. **Built now, registered at the first
checkpoint (2026-12-22).** Nothing here is in force as a test until then.

- **The IC report** (card `docs/research/cards/ic-model-scores.md`; code
  `analysis/ic.py`). For every journal line the model answered: its blended
  score (`blend.composite`) and its five dimension scores (news, technical,
  fundamental, analyst, insider). Each day, the cross-sectional rank
  correlation (IC) of each score with the forward return at 1 and at 3
  sessions (entry at the next open, the race's rule), and the same for the
  momentum score as a comparator. Reported: the mean IC, a Newey-West t,
  the number of days, the effective number of independent names measured
  from the return correlations, and the smallest IC that could be detected
  at t = 2.4. Registered at the 2026-12-22 checkpoint over all lines from
  2026-09-28.
- **Hidden until the checkpoint.** Between checkpoints only counters are
  computed or shown: lines with scores, and days. No IC value is written to
  any file, page or log before the checkpoint.
- **Two universes, one rule**: the production names, and the shadow stock
  universe below. **The owner's decision (Amendment 2026-10-03, before any
  IC value existed):** two trials in N (graveyard rows 35 and 36, one per
  universe) and one idea against the quarterly limit (section 13.8),
  counted in the first quarter of 2027, when its second universe starts,
  since it is the same rule.
- **One primary test per universe (Amendment 2026-10-03):** the blended
  score's mean daily rank-IC at 1 session (Newey-West t, lag 1). From the
  checkpoint at which it is registered, these two primary tests are the
  only IC members of the Benjamini-Hochberg family (13.5), and each gets
  its Deflated Sharpe Ratio (13.6). The IC at 3 sessions, the five single
  scores and the momentum comparison are secondary and descriptive only;
  they are not in the family.
- **Split by sleeve, descriptive only (Amendment 2026-10-03):** for the
  production names, the same numbers made the same way for the single
  names and for the funds separately (`config.instruments.is_fund`), each
  group on its own lines and names. Not tests: not in the
  Benjamini-Hochberg family, no Deflated Sharpe Ratio, no trial in N, and
  hidden until the checkpoints like every other IC value.
- **Pooled number for the single names, "descriptive, very noisy"
  (Amendment 2026-10-04):** the minimum stays 10 names a day. For the
  single names only, the record also shows the rank correlation across all
  their answered lines pooled, after each entry day's average return across
  the lines with that score is taken out (a day with fewer than two such
  lines is left out), with the number of lines used and a t with errors
  clustered by entry day, for each score and horizon. Not a test: not in the Benjamini-Hochberg family, no trial in N,
  and hidden until the checkpoints like the rest of the IC record.
- **The shadow stock universe** (`config/shadow_universe.py`,
  `orchestrator/universe.py`): a fixed list of about 250 US-listed large and
  mid-cap stocks and ADRs, none of them production names, published in the
  card on the registration date and never changed afterwards. From
  2027-01-01 the model scores each name daily with production's model,
  settings and prompt, one call per name. It runs only once the day's
  production cycle is journalled, so the two never ask the model provider
  at the same time (a day with no production cycle has no universe lines),
  and it starts no name from 23:15 UTC, so no line is dated the next day.
  No trading. The existing insider,
  analyst and earnings sources are used where they exist; the news comes
  from production's provider with the universe's own query, company name
  plus ticker (for example "Southern Company SO stock"; Amendment
  2026-10-03; production's query is unchanged). Cost cap $1.50 a day for
  the model and the Bright Data news searches together (Amendment
  2026-10-03, approved by the owner on 2026-10-03; it was $1 for the model
  alone), with an alert to the owner's phone when the day's cost passes
  $1.20 and another when the cap is reached (estimate about $1.05 a day:
  the model about $0.65, the news about $0.40, about $102 a year). Until
  the registration date a name may be replaced for one of three reasons
  only, and never because of its price, its returns or its scores (the
  card's replacement rule, word for word): (1) a merger, buy-out, spin-off
  or split-off announced for 2026-2027 that could fall inside the scoring
  window; (2) the news search for it finds something else: with the
  universe's query, under 30% of its headlines are relevant by the
  code-only check (the company name, or the ticker as a whole word, in the
  title or the first sentence), on a weekday check of every name; (3) it
  does not resolve in the verify check. From the registration
  date nothing is replaced. Its lines are evaluated by the IC report, at 1
  and 3 sessions, hidden until the checkpoints. **The flag
  `SHADOW_UNIVERSE_ENABLED` keeps it off**; `tests/test_shadow_universe.py`
  fails if the flag is on before 2027-01-01, the date in the header table.
- Section 13.8's "no other new exploratory test before the first
  checkpoint" holds: this test is registered at the checkpoint, and its
  counters before it are not results.

### 13.10 Regime split (Amendment 2026-10-02; descriptive)

Asked by the owner on 2026-10-02. **Descriptive only**: it decides nothing,
is not in the Benjamini-Hochberg family, and changes no rule.

- The race's and the funds' results (the main arms' and funds' daily
  results, and each against VT) are split by market state
  (`analysis/regimes.py`):
  - **trend**: VT's previous final close above, or not above, the mean of
    its last 200 final closes up to that close;
  - **volatility**: VT's 21-day realized volatility (the annualised
    standard deviation of its last 21 daily log returns, up to the previous
    close) in terciles, low, mid and high, by two cut-offs fixed at
    registration.
- **The cut-offs** are the terciles of VT's 21-day realized volatility over
  every session from its first 21 returns to 2026-09-30, a window that ends
  before this registration (`analysis.regimes.tercile_cutoffs`). They are
  computed once, by that rule, and written into `analysis/regimes.py`
  (`VOL_CUTOFFS`) and this section, with a dated Amendments row of its own
  (the numbers the registered rule gives; nothing else changes). Nothing can
  be fitted to them: the rule and its window are fixed here.
- **The cut-offs, fixed on 2026-10-02**: low up to **11.30%** a year, mid
  over 11.30% up to **16.97%**, high above 16.97% (at full precision
  0.11302353418809083 and 0.16965241927688823), from 4,573 sessions,
  2008-07-28 to 2026-09-30, computed by the history screen's stress kind
  (workflow run 37013435615, `docs/research/history/2026-10-stress-periods/`).
- **Hidden until the checkpoints**, like section 13.1: between checkpoints
  only the number of sessions in each state is shown; at each checkpoint
  the split is computed once and kept in the checkpoint record.
- It counts as one trial in N (graveyard row 41), like the conviction and
  side reports (rows 7 and 8). It is a report, not a test with a main
  metric, so section 13.8's "no other new exploratory test before the first
  checkpoint" is not touched by it.

### 13.11 Prepared for the first checkpoint: the voting arm `model_vote` (Amendment 2026-10-04; not yet registered)

Asked by the owner on 2026-10-04. **Built now, switched off, registered at
the first checkpoint (2026-12-22)**, as the second new idea of the first
quarter of 2027 (the IC test of 13.9 is the first; section 13.8). Nothing
here is in force as a test until then, and no result of it is computed,
written or shown before that date. Card
`docs/research/cards/model_vote.md`; graveyard row 42 (one trial in N).
Code: `config/model_vote.py` (every number of the rule),
`orchestrator/vote.py` (the calls), `analysis/vote.py` and `shadow/vote.py`
(the answers, the race arm and the fund).

- **Votes.** For every production line the model answered (the race's
  rule: a signal about this ticker, not held), journalled on or after
  2026-12-22 (UTC): vote 1 is the production answer, as journalled. Votes 2
  to 5 are four more calls to the same model with the same settings, each
  re-sending the archived request body of that line's first ask (the
  heartbeat's model-call capture, `orchestrator/model_io.py`, kept as the
  run's artifact) through production's own call path, so its retries and
  re-asks are production's. Before any call, the body that path would send
  is rebuilt, and its SHA-256 must equal the one the production line
  carries (`model_calls`); if it does not (the model, a setting or the
  prompt changed since) or the archive has no copy, the line is not voted,
  and it is counted. Each answer is read as production reads one
  (`parse_signal`, a score with no source set to null); a failed call, an
  answer that cannot be read and an answer about another ticker are failed
  votes. The first ask's body, because when production had to ask again
  (3 lines in 122 on 1-2 Oct 2026) the second body carries a complaint
  about an answer the other votes never gave; each vote call is asked again
  the same way if it needs it.
- **Answer.** Each vote's side is its own bias as answered (BULLISH is
  LONG, BEARISH is SHORT, NEUTRAL), before any floor. With at least 3
  successful votes (vote 1 counted): the side with the most votes, if it
  has at least 3 of the 5; otherwise NEUTRAL, and a tie for the most is
  NEUTRAL. Conviction = (votes for that side ÷ 5) × (their mean
  conviction): a failed vote counts as a vote that does not agree. The
  conviction floor is production's, 0.30 (section 2). With fewer than 3
  successful votes the line has **no answer, and it is dropped for the vote
  and for its comparator alike**: the rule production applies to a line
  with no answer (section 3). The registered arms and funds are not
  touched.
- **Timing.** Once a trading day, after the day's production run and the
  shadow universe's run have finished, and never at the same time as
  either: the vote is a job of the shadow universe's workflow run, after
  its scoring job, the workflow's one concurrency group never runs two of
  its runs at once, and the job first checks that the production run has
  completed. No new line is started from 23:15 UTC. A line not voted that
  day has no answer (dropped as above), and is counted: a line the cost
  cap or the cut-off stopped gets a record saying so, and every answered
  line with no vote record at all (a failed download, a run that never
  came) is counted from the journal.
- **Cost.** About $0.70 a day expected; a hard cap of **$1.00 a day**, with
  an alert to the owner's phone when the day's cost passes **$0.80** and
  another when the cap stops a run, like the shadow universe's. Every HTTP
  ask is counted, retries and re-asks included; an ask with no price is
  charged at an estimate.
- **Race arm.** Scored exactly like the model arm (3 sessions, the next
  open, the same stop, cost and floor), on the lines with a vote answer.
  **Compared with:** the model, one call, on the same lines. **Main
  metric:** mean daily net return, vote minus model, Newey-West t (lag 3),
  as section 3.
- **Fund.** The model fund's machinery with the vote's signals
  (`model_vote`), against a fund that runs the model's own answers on
  exactly the same lines (`model_vote_comparator`): the same start, costs
  and rules. The four funds of 11.1 are unchanged. **Main metric:** mean
  daily net return, vote fund minus comparator, paired over the sessions
  after 2026-12-22, Newey-West t (lag 5), as section 11.4.
- **The family.** From the checkpoint at which it is registered, the race
  arm and the fund are two members of the Benjamini-Hochberg family (13.5),
  each with its Deflated Sharpe Ratio (13.6). One trial in N (graveyard row
  42), as A's race arm and fund are one.
- **Secondary, descriptive only.** The daily IC of the vote score (the mean
  blended score of the successful votes, each blended with the weights the
  production line itself applied) minus the daily IC of the single call's
  blended score, on the same lines, by the IC report's rule (13.9) at 1 and
  3 sessions, with a Newey-West t (lag = horizon). Not in the family, no
  Deflated Sharpe Ratio.
- **Acting differently** (13.7): a line where the vote's signal differs
  from the single call's: after the 0.30 floor, one trades and the other
  does not, or they take opposite sides. Fewer than 20 such lines by the
  final checkpoint is "not tested".
- **Hidden until the checkpoints** (13.1). Between them, from 2026-12-22,
  only counters: lines voted, lines with an answer, lines dropped, lines
  not voted (no archived input, an input that differs), lines not asked
  (the cost cap, the cut-off), answered lines with no vote record, calls
  and failed calls. The 2026-12-22 checkpoint can carry at most that day's
  own lines: counts only, since no trade on them has finished, so no t. Its
  first results are at the 2027-03-22 checkpoint.
- **What it can and cannot show.** Repeating the same model only reduces
  sampling noise, not the bias all its calls share. The wisdom-of-the-crowd
  study (Schoenegger et al., *Science Advances*, 2024) used 12 different
  models on forecasting questions, not stock returns. A vote across
  different models would be a separate, later idea, with its own card, row
  and registration.
- **History screen:** not possible (it uses the AI).
- **The flag** `MODEL_VOTE_ENABLED` keeps the calls off;
  `tests/test_model_vote_runner.py` fails if it is on before 2026-12-22,
  the date in the header table.

### 13.12 Prepared for the second quarter of 2027: the thesis-check logger (Amendment 2026-10-04; not yet registered)

Asked by the owner on 2026-10-04 ("register it in Q2 2027"). **Built now,
switched off, registered at the race's second planned look (estimated
2027-03-22) as an idea of the second quarter of 2027, and on from
2027-04-01**: the same pattern as the IC test, registered at the 2026-12-22
checkpoint, counted in the first quarter of 2027, its second universe on
from 2027-01-01. Card `docs/research/cards/thesis-check.md`; graveyard row
43 (one trial in N). Code: `config/thesis_check.py`,
`orchestrator/thesis.py`, `analysis/thesis.py`.

- **The check.** Once a week, on the first trading day of each ISO week
  with a production cycle, for each name the paper account holds that day
  (the cycle's held lines): one call to the same model, with production's
  settings. Given the entry reasoning archived with the entry (the
  rationale and key factors of the signal that opened the position, from
  the execution audit log) and today's headlines for the name (the ones
  production gathered on its held line that day, so no news search is
  paid), is the thesis VALID, WEAKENED or BROKEN? With one sentence of
  reason. A name not checked that day because of time or a failed call is
  tried again on the next trading day of the same week, while it is still
  held; a name the weekly cost cap stopped, or with no entry record, waits
  for the next week, with one line saying so.
- **Log only.** At most one check with a verdict per name per week in
  `logs/thesis_check/`; every attempt is its own line. It never trades,
  never changes a stop, never feeds any arm or fund, and nothing in the
  cycle reads it.
- **Cost.** A hard cap of **$0.10 a week** (about $0.06 expected); every
  ask counted. It runs in the same workflow run as the vote, after it.
- **At the checkpoints after its registration: a description only.** For
  every check from 2027-04-01: the forward return from the open of the
  first session after the check's day to the close of the 5th session (one
  week, the time to the next check), price only, signed by the position's
  side. The number, mean and hit rate of the BROKEN, WEAKENED and VALID
  checks, and BROKEN minus VALID with a Welch t, for reading only (checks
  on the same day are not independent). It is not a test: not in the
  Benjamini-Hochberg family, no Deflated Sharpe Ratio. Fewer than 20 BROKEN
  checks by the final checkpoint: "not tested". A clear difference would
  only be a candidate for a later registration (for example as an exit
  rule), with its own card, row and registration.
- **Hidden until the checkpoints**, like 13.1: between them, from
  2027-04-01, only counters (checks with a verdict, names, weeks, failed
  calls, names with no entry record, names the cap stopped).
- **History screen:** not possible (it uses the AI).
- **The flag** `THESIS_CHECK_ENABLED` keeps it off;
  `tests/test_thesis_check_runner.py` fails if it is on before 2027-04-01,
  the date in the header table.

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
| 2026-09-26 | **Fund test** (new registration) | Asked by the owner on 2026-09-24; approved by the owner on 2026-09-26. Sections 11 and 12, with the owner's decisions of 2026-09-24 (the calibration pass rule with its two-way match, the watchlist order kept and how often it matters reported, no cost in the calibration copy, the fund test's own bars), of 2026-09-25 (the calibration fail rule: re-run every day after a fix, at least 5 days after the last fix; the late-run mirroring in calibration, stopped if more than 2 calibration days need it; the exploratory funds `model_by_conviction` and `model_sized`) and of 2026-09-26 (short refusals count only from the day they happen; the monthly share of missing price days with a warning above 2%; lag 5; the 95th-percentile coin-flip condition, noted as weak for a buy-only model with the index rule as the real protection; held names as a known limitation, counted daily; bars by an O'Brien-Fleming-type spending rule, recomputed by the same rule from the actual sessions if any look moves; and the exploratory fund `model_same_day`). No exploratory fund can change the decision. Made before any fund was run: no fund result exists, and none will until calibration passes. |
| 2026-09-26 | **Fund test start: 2026-09-28** (the owner's decision; made before any fund result existed) | The funds act on the 2026-09-28 cycle from the next open (first fund session 2026-09-29) instead of starting on the first trading day after calibration passes. Reason: it adds about 15 sessions to every look (planned 60, 120 and 180 fund sessions instead of 45, 105 and 165; bars 3.40, 2.41, 2.02 by the spending rule, rounded up). Calibration is unchanged: the fund test counts only after it passes, no fund result is calculated or shown before that, the funds are then run from 2026-09-28 with the final checked code only (after any calibration fix, with the fixed code only), and a delayed calibration delays the reading, never the start. A look before calibration has passed is skipped by the fund test, spending nothing. No fund had been run and no fund result existed. |
| 2026-09-28 | **Exploratory tests A, B and C** (new registration; exploratory) | Asked by the owner on 2026-09-27; decided by the owner on 2026-09-27. Section 13: A, the momentum rule with a 200-day moving-average veto from final closes up to the session before the signal (race arm and fund; a 50-day version was dropped before it ran as redundant with the momentum rule's own 50-day check, decided from signal counts only, and counts in N); B, 10-month moving-average timing on VT with T-bills through BIL (fund, from the 2026-09-30 month-end); C, pullback limit entry (fund). Counters only between checkpoints, results only at the race's looks, for A, B and C **and for the three exploratory funds of section 11.1** (`model_by_conviction`, `model_sized`, `model_same_day`), which until now were to be shown nightly once calibration passed, **and for the insider arm, whose results were printed nightly from 2026-09-22 to 2026-09-28, before this section existed** (nothing is undone; from now on it shows counters only); at each look, Benjamini-Hochberg across all exploratory tests and the Deflated Sharpe Ratio with N from `docs/research/graveyard.md` (18); the outcomes of section 13.7, including **"not tested"** for an idea that acted differently from its comparator fewer than 20 times by the final checkpoint (C counted as a signal one of C and the momentum fund bought and the other did not, or both bought at different prices, a signal both skipped not counted; `model_sized` as a trade whose size factor is not 1.0), and **B exempt from the final "zero or below" rule** (its purpose is crash protection, which 9 months may not test); the `model_same_day` counter from the 2026-09-28 cycle only; the research limits. None can change the decision. **Made before any result of A, B or C existed, and before any exploratory fund result existed:** none has been computed (no fund is run before calibration passes), and the rules were written by the owner on 2026-09-27, before the first line they read (the 2026-09-28 cycle). |
| 2026-09-28 | **The owner's note on the history screens of A, B and C** (a disclosure; no rule change) | Added under section 13 at the owner's decision of 2026-09-28: the owner's own history screens of A, B and C (`docs/research/graveyard.md`, rows 22 to 25) were run on 2026-09-27, after their settings were fixed and before section 13 was committed; no setting was changed after seeing them; no live result of A, B or C existed. The row above's "any result of A, B or C" means their live results, computed by this repository's code from the 2026-09-28 cycle on; the owner's quick tests on history are not those. The owner's process for history screens is in `docs/research/backlog.md` ("History first, live second"); a history screen changes nothing here. |
| 2026-09-28 | **Calibration started** (the owner's decisions of 2026-09-24 and 2026-09-25; calibration of the shadow funds, not a rule of the race) | The pass rule (the six conditions, the fail rule and late-run copying with a 2-day limit) is in force, and calibration starts with the 2026-09-28 close: the first complete account snapshot (account, positions and stops all read, no error), checked after that day's cycle. `PASS_RULE.approved` and `CALIBRATION_START` changed together in one reviewed change. The fund test's start, sessions and bars are unchanged (start 2026-09-28; 60/120/180 sessions; bars 3.40/2.41/2.02); fund results are still computed only after calibration passes. |
| 2026-09-29 | **Bug fix**: an answer with a value outside the schema gets the same one re-ask as an off-schema answer (the owner's decision; not a decision rule) | On 2026-09-28 the model answered XBI with conviction -0.35 (conviction must be 0 to 1). The answer was readable, so the off-schema re-ask of 2026-09-26 did not apply; the value check came later, and the name was lost for every arm and fund. It was the first such answer in about 230 from `openai/gpt-oss-120b`. Now the model is asked once more, with the problem stated (`orchestrator/llm.py`, `INVALID_VALUES_INSTRUCTION`); the two kinds of bad answer share the one re-ask. The code never mends a value: if the second answer is bad too, it is rejected and journalled exactly as before, and it counts as a model error for trigger (c). The first answer stays in the call record, marked `invalid_values`. The re-ask never depends on the side the answer takes. The new sentence is part of the prompt fingerprint, so the drift report shows one "prompt fingerprint changed" alert the day it ships. No model, provider, prompt text of the first ask, answer length or reasoning effort changes; no decision rule, arm, fund or calibration rule changes. |
| 2026-09-29 | **Bug fix**: the full model's read timeout is 480 seconds instead of 300 (the owner's decision; not a decision rule) | About one first ask in fifteen reasons until the answer's 16,000-token limit (`MAX_TOKENS`) and gives no answer. At 300 seconds such an answer ends in time only when the model writes faster than 53 tokens a second. On 2026-09-28 (about 57 a second) 4 of 58 first asks ran to the limit in 255-284 seconds, got the off-schema re-ask of 2026-09-26, and all 4 answered. On 2026-09-29 (about 41 a second) no answer reached the limit: 3 first asks timed out instead (one in a slow spell of 16-31 tokens a second), the retry after a timeout asked the same question again, 2 were answered and EWU was lost after two timeouts. The first ask and the retry now wait 480 seconds (`orchestrator/llm.py`, `FULL_MODEL_TIMEOUT_SECONDS`; `TRANSPORT_RETRY_TIMEOUT_SECONDS` follows it), so an answer at the limit ends in time down to 33 tokens a second and reaches the re-ask that states the complaint. This changes no model, provider, prompt, answer length or reasoning effort; only how long we wait. The full-model stage's 90-minute budget is unchanged. Trigger (c) is unchanged: its window is not reset and timeouts still count as model errors. The weekly report's step gets 20 minutes and the article probe's workflow 80 (operational). In force from the first cycle after the change is merged. No decision rule changes. |
| 2026-10-02 | **After-tax gate** (new registration of the decision rule, not a bug fix) | Asked by the owner on 2026-10-02. Section 5c, and one clause each in sections 5, 5a, 9, 11.6 and 11.8: the arm that would win must also beat the VT fund after Israeli tax, on an "if sold today" basis, at the same bar and with the same Newey-West test (the fund test's paired daily test, lag 5): after-tax equity = equity minus the tax due if every position were sold at that day's close (floored at 0), after-tax daily return = after-tax equity today ÷ yesterday − 1, then the same paired difference against VT. The tax rules are the owner's (shekel gains with the exchange rate as the index, Income Tax Ordinance s.88 and Circular 10/2025; 25%; a surtax as parameters, off; FIFO lots per account; dividends at 25% with a credit for the US tax withheld; this year's losses against this year's gains, `offset_losses_vs_dividends` on by default until the accountant answers, the rest carried forward against future capital gains only; the Bank of Israel's representative rate on the trade date), every number in `config/israel_tax.py`, the owner's ten cases T1 to T10 as unit tests (T5 needs confirmation), and five conventions the rules leave open written in section 5c. The record is made once by the funds run, on the first night from the night the race reaches a look on which the look is readable, the rate table is there and the funds' prices reach the look's last close; it is cut at that close and read back by the race, which does not read a record cut at another close (the look waits, and the record is made again at the new close); a look waits for it; before calibration has passed it cannot be met. It can only stop an arm from winning and never decides by itself. Also reported, for information only and not a gate: the break-even simulator (0.82 points a year at 6% growth and a 2% yield). **It adds a gate, it changes no arm and no metric, and it was made before any checkpoint result existed**: the first checkpoint is estimated for 2026-12-22, the race had 1 of 20 independent days, and no fund result had been computed (calibration on day 2 of 15). |
| 2026-10-02 | **Reporting only: the after-tax and shekel reports** | Asked by the owner on 2026-10-02. Section 11.9: the paper account, the four funds and (at checkpoints only) the exploratory funds, before and after tax side by side, with "tax paid so far" and "if sold today", by the rules of section 5c; the same results in shekels at the Bank of Israel's representative rate, with how much of each came from the USD/ILS change; the rate table kept like the price table (SHA-256 in git, the table in the archive), its fallback days counted (a checkpoint night without a rate table records the exploratory funds' after-tax view as not available, and it is not made later). The paper account is shown from now; the funds once calibration has passed, like every fund result. They decide nothing beyond section 5c's test and change no rule. |
| 2026-10-02 | **Prepared, not registered: the IC report and the shadow stock universe** | Asked by the owner on 2026-10-02. Section 13.9, the card `docs/research/cards/ic-model-scores.md`, and graveyard rows 35 and 36: built now, **registered at the 2026-12-22 checkpoint** over all lines from 2026-09-28; counters only (lines with scores, days) until then, and no IC value written anywhere before it. The shadow stock universe is built with its flag off (`SHADOW_UNIVERSE_ENABLED`, off until 2027-01-01; a test fails if it is on before that date), runs only after the day's production cycle is journalled and starts no name from 23:15 UTC; its list is published in the card on the registration date and never changed after. **Two decisions are the owner's**, logged before the funds run of the night the race reaches the first look (before any IC value exists): whether it counts as two trials in N and one idea against the quarterly limit, counted in the first quarter of 2027 (the owner's proposal), and the main test of each universe (proposed: the blended score's IC at 3 sessions); if nothing is logged by then, the proposals stand. No result of it exists: nothing has been computed. |
| 2026-10-02 | **Regime split** (reporting only; descriptive) | Asked by the owner on 2026-10-02. Section 13.10: the race's and the funds' results split by VT above or not above its 200-day average and by VT's 21-day realized volatility in terciles, with cut-offs fixed by a rule over a window that ends on 2026-09-30, before this registration. Hidden until the checkpoints (sessions per state only between them); decides nothing, not in the Benjamini-Hochberg family; counts as one trial in N (graveyard row 41). Made before any checkpoint result existed. |
| 2026-10-02 | **Verdict disclosure** (new registration; a label and a policy, not a rule) | Asked by the owner on 2026-10-02. Section 5d and a clause in section 9: if VT's maximum drawdown from its high inside the test window (2026-09-23 to the close of the deciding look's last trades, final closes with dividends added back, as the index test treats them) is below 10%, the verdict is labelled "not tested in a downturn" and any real-money step starts small. It does not extend the test, move a look or change an outcome. Made before any checkpoint result existed. |
| 2026-10-02 | **Regime split: the volatility cut-offs fixed** (the numbers the registered rule of section 13.10 gives; nothing else changes) | The rule of the row above, run once by the history screen's stress kind (workflow run 37013435615, from VT's final closes 2008-07-28 to 2026-09-30, 4,573 sessions; `docs/research/history/2026-10-stress-periods/results.json`, key `regime_cutoffs`): low up to 11.30% a year, mid up to 16.97%, high above (0.11302353418809083 and 0.16965241927688823), written into section 13.10 and `analysis/regimes.py` (`VOL_CUTOFFS`). The window ends before this registration; no race or fund result was read. |
| 2026-10-03 | **The IC test's main metric and trial count** (the owner's decisions, which section 13.9 left to the owner; registered with the card on 2026-12-22) | Decided by the owner on 2026-10-03, **before any IC value existed**: until the 2026-12-22 checkpoint the IC report writes counters only, and no IC has been computed. Two trials in N (graveyard rows 35 and 36, one per universe) and one idea against the quarterly limit, counted in the first quarter of 2027. One primary test per universe: the blended score's mean daily rank-IC at 1 session (Newey-West t, lag 1), in place of the proposed 3 sessions; these two primary tests are the only IC members of the Benjamini-Hochberg family. The IC at 3 sessions, the five single scores and the momentum comparison are secondary and descriptive only, not in the family. Section 13.9, the card `docs/research/cards/ic-model-scores.md`, graveyard rows 35 and 36, and `analysis/ic.py` (`MAIN_HORIZON` = 1). No arm, bar or rule of the race changes. |
| 2026-10-03 | **Cross-references only: the accountant's questions** (no rule changes) | The owner replaced the eight questions to the accountant written on 2026-10-02 with the owner's own list of ten (`docs/research/cpa-questions.md`, followed by the two added on 2026-10-02). Section 5c now points at the new numbers: T5 is question 1 and still **needs confirmation** (it is not treated as confirmed); conventions (1) and (2), on short sales, are no longer put to the accountant and stay as written; convention (5), the dollar conversion of a finished year's tax, was put with the old question 5 and is now listed with (3) and (4) as how the books are kept; when tax is really paid during the year is question 7. No setting, number or rule changes. |
| 2026-10-03 | **Shadow stock universe: the news searches in the cost cap, and the replacement rule** (operational; no rule of the race or of the IC test changes) | Asked by the owner on 2026-10-03. The cost cap of section 13.9 now counts the Bright Data news searches as well as the model: about 270 requests a day at $1.50 per 1,000 (pay as you go), about $0.40 a day and about $102 a year, so about $1.05 a day with the model. A $1 cap would stop the run before the end of the list every day, so the cap is **$1.50 a day for the two together, proposed on 2026-10-03; the owner confirms it before the pull request is merged**. Every request sent is charged, written on the line, and counted again by a same-day re-run; the phone alert names the model and the news. The replacement rule for the list, written on the card before the list freezes and copied into section 13.9: until 2026-12-22 a name may be replaced for one of three reasons only, and never because of its price, its returns or its scores: (1) a merger, buy-out, spin-off or split-off announced for 2026-2027 that could fall inside the scoring window; (2) the news search for its ticker finds something else; (3) it does not resolve in the verify check; the five names replaced on 2026-10-02 (JNJ, MDT, SPGI by EW, IDXX, MET; DOW, ASX by MLM, UMC) are listed there, and the two replaced on 2026-10-03 by rule (3), because they did not resolve in three verify runs that day while the other 249 names did (BK, AVB by STT, IRM). The verify check now also runs on every pull request that changes the list. The universe is still off until 2027-01-01 and has no line yet. |
| 2026-10-03 | **Shadow stock universe: the $1.50 cap approved, a $1.20 alert, and its own news query** (operational; no rule of the race or of the IC test changes) | Decided by the owner on 2026-10-03, after reading the row above. (a) The cost cap of $1.50 a day for the model and the news searches together is **approved** (expected about $1.05 a day). (b) A phone alert when the day's cost passes $1.20 (`DAILY_COST_WARN_USD`): only an alert, the run goes on to the cap; at most once a day, and not from a run whose cap alert is sent. (c) The universe's news searches use their own query, company name plus ticker (for example "Southern Company SO stock"; `config/shadow_universe.py`, `orchestrator/universe_news.py`), because a news check the same day found that "<ticker> stock" finds other things for short tickers (SO, C, D and MET: none of ten headlines named the company; EW: none of two; T, ED, NOW, V, ICE, O and F: one to three of ten). Production's query and code are unchanged, because they feed the main race. Those names are kept. (d) A code-only relevance check, with no model: a headline is relevant if the company name, or the ticker as a whole word, is in its title or first sentence (`analysis/news_relevance.py`), run once on a weekday over all 251 names (`.github/workflows/universe-news-check.yml`). Replacement rule (2) of the card and of section 13.9 now reads: "the news search for it finds something else: with the universe's query, under 30% of its headlines are relevant by the code-only check (the company name, or the ticker as a whole word, in the title or the first sentence), on a weekday check of every name". A name is replaced by it only for that reason, never for its returns, and each replacement is recorded with its reason. (e) The same check, once and as a description only, on the news the race used for its 80 names (`docs/research/news-relevance.md`); nothing in production changes because of it. The universe is still off until 2027-01-01 and has no line yet. |
| 2026-10-03 | **Reporting only: the IC report's split of the production names into single names and funds** (descriptive; no test and no rule changes) | Asked by the owner on 2026-10-03, after the news audit (`docs/research/news-relevance.md`) found the race's news relevant for 76% of single-name headlines but 23% of fund headlines on every journalled line (74% and 23% on the lines the model answered, held lines left out). Section 13.9 and the card `docs/research/cards/ic-model-scores.md`: at each checkpoint the IC record also carries, for the production names, the same numbers made the same way for the 16 single names and for the 64 funds separately (`config.instruments.is_fund`; `analysis/ic.py`, `groups_record`), each group on its own lines and names, with the same minimum of 10 names a day. Descriptive only: not a test, not in the Benjamini-Hochberg family, no Deflated Sharpe Ratio, no trial in N (the graveyard's N is unchanged), and hidden until the checkpoints exactly like every other IC value (only the checkpoint record carries it; the nightly counters are unchanged). On the lines so far only 4 to 7 single names a day were answered (the others were held), so on such days the single names have fewer than 10 names and no IC; the minimum is not changed for the split. No IC value has been computed. |
| 2026-10-04 | **Reporting only: a pooled number for the single names in the IC report's split, "descriptive, very noisy"** (no test and no rule changes) | Decided by the owner on 2026-10-04, after the row above showed that only 4 to 7 single names a day are answered, so their daily IC (at least 10 names a day) will often be missing. The owner kept the registered minimum of 10 names a day. Section 13.9 and the card `docs/research/cards/ic-model-scores.md`: for the single names only, the checkpoint record also shows a pooled number (`analysis/ic.py`, `pooled`): the rank correlation of each score with the return across all the single names' answered lines pooled, after each entry day's average return across the lines with that score is taken out (a day with fewer than two such lines is left out), with the number of lines used and a t with errors clustered by entry day (CR1), for each score and horizon. Labelled "descriptive, very noisy". Not a test: not in the Benjamini-Hochberg family, no Deflated Sharpe Ratio, no trial in N (the graveyard's N is unchanged), and hidden until the checkpoints like the rest of the IC record (only the checkpoint record carries it; the nightly counters are unchanged). At 3 sessions the windows of nearby days overlap, which clustering by day does not cover, so that its t is too far from zero, in either direction. No IC value has been computed. |
| 2026-10-04 | **Prepared, not registered: the voting arm `model_vote`** (registered at the 2026-12-22 checkpoint; exploratory, shadow only) | Asked by the owner on 2026-10-04. Section 13.11, the card `docs/research/cards/model_vote.md` and graveyard row 42 (N from 41 to 43 with row 43 below): four more calls of the same model on each answered line, re-sending the archived first-ask body (checked by its SHA-256 before any call), with the production answer five votes; the side with at least 3 of 5 (a tie or no such side is NEUTRAL), conviction = share agreeing × their mean conviction, the 0.30 floor; fewer than 3 successful votes: no answer, the line dropped for the vote and its comparator alike. A race arm (lag 3) and a fund (lag 5) against the model on the same lines, both in the Benjamini-Hochberg family and the Deflated Sharpe table from registration; the IC of the vote score minus the single call's, descriptive only; fewer than 20 lines acting differently by the final checkpoint is "not tested". Cost cap $1.00 a day, phone alert at $0.80; the cap alert reaches the phone at most once a day. A line the cap or the 23:15 cut-off stops gets a record saying so, and every answered line with no vote record is counted. Operational: two jobs added to the shadow universe's workflow (the vote, then the weekly thesis check of the row below), after its scoring job, so the three never ask the model provider at the same time (a cancelled run stops them; each holds the full model's key only); and one read-only helper in `orchestrator/llm.py` (`request_body`, the body a call would send), production's calls unchanged. Built with its flag off (`MODEL_VOTE_ENABLED`, off until 2026-12-22; a test fails if it is on before that date). **Made before any vote exists**: no call has been made and nothing has been computed. |
| 2026-10-04 | **Prepared, not registered: the thesis-check logger** (registered at the 2027-03-22 checkpoint as an idea of the second quarter of 2027, on from 2027-04-01; log only) | Asked by the owner on 2026-10-04. Section 13.12, the card `docs/research/cards/thesis-check.md` and graveyard row 43: once a week, for each held name, the same model is asked whether the entry reasoning still holds given today's headlines (VALID, WEAKENED or BROKEN, with one sentence); it never trades, never changes a stop and never feeds any arm. At the checkpoints after its registration, the forward returns of BROKEN against VALID names, as a description only (not in the family). Cost cap $0.10 a week; its alert reaches the phone at most once a week, and a name the cap stops waits for the next week. The owner's "register it in Q2 2027" is read as the IC test was: registered at the checkpoint before the quarter, counted in it, on from its first day. Built with its flag off (`THESIS_CHECK_ENABLED`, off until 2027-04-01; a test fails if it is on before that date). **Made before any check exists.** |
| 2026-10-04 | **The research backlog in three sections** (documentation only; no rule changes) | Asked by the owner on 2026-10-04. `docs/research/backlog.md` is now in three sections, AI ideas, trading rules and index-first reports; the AI ideas section lists each idea with its status, cost and trial number (the IC report and the shadow universe, the vote and the thesis check: built and switched off, with their dates; a 1-to-5 ranking arm: deferred, only if the IC report shows the scores are too coarse; a cross-model vote: a later idea, not registered; event tags and annual-report flags: dropped, too few events). The other two sections are filled by the owner's next message. Nothing moved out of the backlog's rules. |
| 2026-10-05 | **Shadow stock universe: the first weekday news check, and the search name of 18 names** (operational; no rule changes, no name replaced) | The check decided by the owner on 2026-10-03 ran on Monday 2026-10-05 (runs 37345386044 and 37351217326; `docs/research/news-relevance.md`). Bright Data throttled the requests all through the first run (an empty body with its 200, or "auto-throttled"), and 29 names had no answer; they were asked again the same day. The run also showed that 18 names had their ticker as their search name, so they were searched as "<ticker> stock", not as company name plus ticker as decided on 2026-10-03; their company names now lead (`config/shadow_universe.py`, for example "United Parcel Service UPS stock"), and they were checked again the same day. Result: 250 of 251 names answered (ZTO did not, after four asks); 75% of 1,537 headlines are relevant; 19 names are under 30% or had no headline (OKE, APD, ECL, GD, BKNG, ORLY, HSY, INTU, FOXA, PEG, SO, GSK, NMR, IBN, AMX, CHKP, ICL, PKX, SHG), most on 0 to 7 headlines. STT: 80% (4 of 5), kept. IRM: 1 of 1, kept. No name is replaced on this one day: rule (2) allows a replacement and does not require one, and with a median of 6 headlines a name, one day's share is not yet evidence that the search finds something else; the owner decides. The check now asks two names at a time, asks a failed search up to four times, and lists a name it could not ask apart, with no share. |
