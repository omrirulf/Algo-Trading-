# The checkpoint verdict: layout and readings for the owner

**Status: for the owner's approval (3 Oct 2026). Nothing here is built yet.** The owner's item 6 of 3 Oct 2026:
"Build the automatic checkpoint verdict for both the race and the fund test, with unit tests … Show me the layout
of the verdict table before you build it."

## 1. What exists today, and what is missing

- **The race already decides in code** (`analysis/decision_gate.py`): the keep rule, the replacement rule, the early
  stops, index first, the after-tax gate (5c), the coin-flip condition, the bars 3.47 / 2.45 / 2.00 and the
  "not tested in a downturn" label. What it lacks is a **table**: today it prints one line of free text.
- **The fund test does not decide anywhere** (section 11.6). Nothing computes its paired t values at a look, its
  coin-flip condition, its own bar (3.40 / 2.41 / 2.02 if the looks fall as planned), its skip when calibration has
  not passed, or its verdict.
- **The combined answer** (section 11.8: real money only if the same arm wins both) is not computed anywhere.

The build adds the two tables and the combined line, and the fund test's verdict. It changes no rule, no bar and
no arm; the race's own decision code and its words stay exactly as they are.

## 2. The layout

Every table has the same six columns. A result is PASS, FAIL, WAITING (its record is not made yet), CANNOT PASS
(calibration had not passed), NOT APPLIED (no arm reached that step), n/a (a row that does not apply at this look)
or LABEL.

**EXAMPLE: every number below is made up. None is a result.**

### (i) The race, at a checkpoint

**Race, checkpoint 1 of 3:** 20 independent days (60 entry days), window 2026-09-23 to 2026-12-22, bar t > 3.47.
Readable tonight: yes. VT priced on 60 of 60 entry days.

| # | Rule (section) | What is measured | Value | Bar | Result |
|---|---|---|---|---|---|
| 1 | Keep (a), 5 and 5a | model − momentum, mean daily net return, Newey-West t, lag 3 | t = −3.62 | > 3.47 | FAIL |
| 2 | Keep (b), 5 and 5a | model − hybrid, the same test | t = −1.05 | > 3.47 | FAIL |
| 3 | Keep (c), coin flip, 5 | model's mean daily net return against the 95th percentile of 1,000 coin flips on its own lines | +0.012% vs +0.071% | above | FAIL |
| 4 | Keep rule, 5 | rows 1, 2 and 3 all pass | 0 of 3 | all 3 | NOT KEPT |
| 5 | Replacement, 5 | hybrid − momentum, Newey-West t, lag 3 | t = 0.84 | > 3.47 | FAIL, so momentum |
| 6 | Early stop, 5a (looks 1 and 2 only) | against the model: model − momentum (the replacement) | t = −3.62 | < −3.47 | PASS: momentum is the candidate |
| 7 | Index first, 5 and 5a | momentum − VT, same entry days and windows, Newey-West t, lag 3 | t = 3.55 | > 3.47 beats VT; < −3.47 hold the index | PASS |
| 8 | After-tax gate, 5c | momentum fund − VT fund, daily after-tax return "if sold today", Newey-West t, lag 5, 2026-09-29 to 2026-12-22 | t = 3.52 | > 3.47 | PASS |
| 9 | Downturn, 5d | VT's largest fall from its high, dividends added back, 2026-09-23 to 2026-12-22 | 4.1% | 10% or more = tested | LABEL |
| → | **Race verdict** | | | | **EARLY STOP AT 20: REPLACE THE MODEL WITH MOMENTUM — NOT TESTED IN A DOWNTURN** |

At the final look row 6 reads "n/a (final look)", and row 7's bar is "> 2.00, or no arm trades".

### (ii) The fund test, at the same checkpoint

**Fund test, checkpoint 1 of 3**, read on the race's look day: fund sessions 2026-09-29 to 2026-12-22, 60 of 180
planned (share 0.333); bar t > 3.40 (by the spending rule of 11.7; planned 3.40); calibration passed 2026-10-19;
1,000 coin-flip funds.

| # | Rule (section) | What is measured | Value | Bar | Result |
|---|---|---|---|---|---|
| 1 | Keep (a), 11.6 | model fund − momentum fund, daily net return, Newey-West t, lag 5 | t = −2.31 | > 3.40 | FAIL |
| 2 | Keep (b), 11.6 | model fund − hybrid fund, the same test | t = −0.40 | > 3.40 | FAIL |
| 3 | Keep (c), coin flip, 11.5 | model fund's total return since 2026-09-29 against the 95th percentile of the 1,000 coin-flip funds' total returns | +3.90% vs +2.70% | above | PASS |
| 4 | Keep rule, 11.6 | rows 1, 2 and 3 all pass | 1 of 3 | all 3 | NOT KEPT |
| 5 | Replacement, 11.6 | hybrid fund − momentum fund, Newey-West t, lag 5 | t = −1.90 | > 3.40 | FAIL, so the momentum fund |
| 6 | Early stop, 11.6 (as 5a) | against the model: model fund − momentum fund | t = −2.31 | < −3.40 | FAIL: no early stop |
| 7 | Index first, before tax, 11.6 | momentum fund − VT fund, daily, Newey-West t, lag 5 | t = 1.12 | > 3.40 / < −3.40 | NOT APPLIED |
| 8 | Index first, after tax, 11.6 and 5c | momentum fund − VT fund after tax (the same record as race row 8) | t = 0.98 | > 3.40 | NOT APPLIED |
| 9 | Downturn, 5d | the same number as the race's | 4.1% | 10% or more = tested | no label (nothing decided) |
| → | **Fund-test verdict** | | | | **NO DECISION AT THIS LOOK — read again at checkpoint 2 (about 2027-03-22; planned bar 2.41)** |

### (iii) The one combined line

```
CHECKPOINT 1 (2026-12-22) — race: REPLACE THE MODEL WITH MOMENTUM (early stop) · fund test: no decision ·
combined: NO DECISION YET — waiting for the fund test (checkpoint 2, about 2027-03-22).
No real money before the June 2027 verdict (section 9).
```

| Race | Fund test | Combined |
|---|---|---|
| no arm trades | anything | HOLD THE INDEX — the race decided "no arm trades" (11.8) |
| anything | no arm trades | HOLD THE INDEX — the fund test decided "no arm trades" (11.8) |
| arm X | arm Y, not X | HOLD THE INDEX — the race picked X, the fund test picked Y (11.8) |
| arm X | arm X | X WINS BOTH — no real money before the June 2027 verdict (section 9); after it, real money for X, starting small if NOT TESTED IN A DOWNTURN |
| not decided | anything but "no arm" | NO DECISION YET — waiting for the race |
| arm X | not decided | NO DECISION YET — waiting for the fund test |
| final look | skipped at every look | HOLD THE INDEX — the fund test could not be read (calibration never passed) |

### (iv) Before the first checkpoint

The existing header line stays as it is (section 4: "… — NO DECISION YET"). The new verdict block prints only:

```
CHECKPOINT VERDICT
no decision yet
```

The JSON says `"verdict": {"text": "no decision yet"}` in `logs/race_gate.json` and `logs/funds.json`, and the
4 Funds page shows one card: "Checkpoint verdict: no decision yet".

### (v) When calibration has not passed at a checkpoint

The race's row 8 reads "record UNAVAILABLE: calibration had not passed when the race reached this look" with the
result CANNOT PASS (an early look then picks no arm; at the final look no arm trades). The fund test's whole table
is replaced by one block:

> **Fund test, checkpoint 1 of 3: SKIPPED.** Calibration had not passed on the night the race's look was readable.
> Not read, no part of the 5% spent, no bar used. The next bars come from the same rule using only the looks
> actually read (planned: checkpoint 2 at 2.41, checkpoint 3 at 2.02).

## 3. Readings the owner decides before the build

The rules leave these points open. Each proposed reading is the one closest to the text; none is a new rule. The
owner's answers go into the Amendments table before any checkpoint result exists.

1. **How the two verdicts combine.** Each test stops at its own first deciding look and is then frozen. The answer
   is the index as soon as either test says "no arm trades", or the two pick different arms; it is the arm when
   both pick the same one; otherwise "no decision yet". An early answer is final; section 9 only delays the money
   to June 2027. Later looks are still shown, for reading only.
2. **The fund test uses its own bar for every step,** including its after-tax step (section 5c: "the bar of the step
   it belongs to"). The race keeps its bar. Both tables show which bar was used.
3. **An after-tax failure at an early look decides nothing** in the fund test either; at the final look it means
   no arm trades. (The same as the race, section 5c.)
4. **The fund test's window ends at the race look's last close** (the after-tax record's close), never at a later
   night's close. Its record is made once and frozen, like the after-tax record, and made again only if a bug fix
   moves the window (the old one kept inside it).
5. **Calibration is judged on the first night the race's look is readable** — the same night the after-tax record
   uses — so the fund test's skip and the race's "unavailable" record can never disagree.
6. **One downturn number:** the race's VT figure for both tests and the combined line. If it cannot be measured,
   the verdict says "downturn not measured" and the owner decides.
7. **The fund test's bar at a look** comes from the spending rule of 11.7 with the fund sessions actually there;
   the rounded bars of earlier looks count as used. The verdict prints "bar X (planned Y): log it in the Amendments
   table" for the owner, because code cannot write an amendment.
8. **The fund-test record is made only with the registered 1,000 coin-flip funds.** A by-hand run with fewer waits
   and says why.
9. **A tie with the coin-flip 95th percentile fails** (the rule says "above").
10. **The 4 Funds page's fund-test banner** shows fund sessions of 180 and the fund test's own next bar, not the
    race's (a display fix).

## 4. Where it appears

- `logs/race_gate.json` (`verdict`, a new last key) and the horse-race report (a "CHECKPOINT VERDICT" block after
  the gate).
- `logs/funds.json`: the frozen fund-test records (`fund_test.looks`), the fund-test table (`fund_test.verdict`)
  and the combined line (`verdict`).
- The 4 Funds page: one "Checkpoint verdict" card with both tables and the combined line.

## 5. Tests that come with it

Every row of every table against the race's existing decision code on every branch (keep, replacement, early stop
both ways, index beats / trails / neither, after-tax pass / fail / waiting / unavailable, unreadable); the bars at
each look; the fund test's spending-rule bars (60 sessions → 3.40, 61 → 3.37, a skipped first look → 2.41 / 2.02,
the final look alone → 1.96); the coin-flip tie; the skip; the frozen record and its replacement; the combined
line in every row of the table above; "no decision yet" before the first look; the JSON key order kept
(`prices_sha256` last); and the page drawing nothing for an older file.
