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
positions can mean bigger losses. In this system the "normal size" is the
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
   metric at the bar. If it does not, no arm trades: hold the index.
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
its fund beats the VT fund at that look's bar.** If the race and the fund
test disagree — different winners, or one of them decides "no arm trades" —
the answer is the index. And section 9 still holds: no real money in this
system before the June 2027 verdict, whatever an earlier look says.

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
account snapshot exists: planned 2026-09-28 (checked after that day's cycle;
if the snapshot is incomplete, calibration starts on the next trading day
with a complete one). The fund test's start stays 2026-09-28 either way
(11.3).

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
