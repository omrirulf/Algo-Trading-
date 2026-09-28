# Summary: the rules that run live, tested on 2000 to 2026

This is the short version of [the report](report.md). All numbers come from
[`results.json`](results.json). The screen replays momentum, A, B and C on past
prices with the real code: production's technicals, the race's own scoring and
the production fund engine. Costs are 0.10% per side, with no taxes. It
covers 80 names (today's watchlist) from 2000 to 25 Sep 2026.

**Nothing here changes the locked test, its rules or its decisions.** The live
race was not looked at.

## What history cannot give

- **No live price in the past.** The previous session's final close stands in
  for it. A's veto and C's limit use this stand-in.
- **The technicals stop at the previous close.** A live line also has the
  current session's partial bar, so a history line knows a little less.
- **Survivorship.** The list is today's list. Funds and companies that closed
  are missing, and some names on the list were big winners (NVDA, LLY, MELI).
  This flatters "always long" and the long side.
- **Fewer names early on.** Many ETFs on the list started after 2000, so the
  early years have fewer names (about 36 in 2000, 78 to 80 from 2015).
- **Split-adjusted prices.** Early NVDA trades at under $1. There the
  engine's stops are rounded to the cent and are coarse. These trades are few
  and counted in the report.

## The answers in short

| Rule | Race (3-session trades) | Fund | In one line |
| --- | --- | --- | --- |
| Momentum | No clear difference from a coin flip (t -0.07). Behind always long since 2010 (t -2.3 on the same lines). | Loses 3.5% a year (2000-2026). Far behind the VT fund since 2010 (t -3.0). | No edge at 3 days; the fund's trading costs eat it. |
| A (200-day veto) | Vetoes 5.7% of signals. A minus momentum: +0.007% a day (t +1.7); from 2010, t +3.0. | A fund minus momentum fund: t +1.6. Also far behind VT. | A little better than momentum, but still momentum; under 10% vetoed, so it says little. |
| B (VT or T-bills) | not a race rule | B on VT from April 2009: 6.5% a year against 11.3% for VT, and almost the same worst fall (28% against 29%). B minus VT: t -2.0. | About 5% a year behind VT since April 2009 (3.5% from 2010), with no crash protection: VT's data starts after 2008. |
| B's rule on SPY (check) | not a race rule | From June 2007: 7.8% a year against 9.0% for SPY, worst fall 25% against 50%. Since 2010: 4.1% a year less. | Halves the 2008 crash; costs 4% a year in calm years. |
| C (pullback limit) | Fills 61% of signals. Missed +0.88% against filled -0.93% per trade: built in. | C fund minus momentum fund: +0.003% a day (t +0.7). Most fills could not be bought: the book was full. | No clear difference from momentum. |

## Where my results differ from your quick test, and why

| Your quick test (38 ETFs, 2000-2026, 2 x ATR stop) | This screen (80 names, real code) | Why |
| --- | --- | --- |
| Momentum, 3-day trades: no better than a coin flip. | **The same.** Minus a coin flip: -0.002% a day, t -0.07. Before 2010: t +0.29. From 2010: t -0.51. | Same answer. At 3 days the moves are mostly noise, and 0.2% per round trip is bigger than any edge. |
| At 1-3 months it worked in 2000-2009. | **Not tested at 1-3 months.** The registered race is 3 sessions, and a new horizon would be a new trial. The fund (the closest thing, positions held about 10 sessions) lost 28% in 2000-2009, while SPY lost 8%. Only in the 2008-2009 crash did it beat VT (+10.6% a year against -8.1%). | Different holding time. The production stop and profit ladder close positions after about 2 weeks, not 1-3 months. The fund also pays about 4% a year in costs, holds 16 companies, and when full it buys in watchlist order. |
| Since 2010 its buys trailed holding all the ETFs. | **Same direction, weaker.** Race longs minus buying every line on the same days: -0.020% a day (t -0.9). All trades (longs and shorts) minus always long on every line: -0.091% a day (t -2.1). | My "every line" includes the companies. The longs pick about as well as buying everything; the loss comes from the shorts. |
| Its shorts lost about 3.7% per 3-month short. | **Smaller, but still losing.** Race shorts from 2010: -0.37% per 3-session trade (after 0.2% costs). Fund shorts from 2010: -0.74% per closed trade. | Much shorter trades, and the stop cuts a short that goes wrong. Over 3 months, a short in a rising market loses more. |
| A: removed only about 4% of signals, no clear difference. | **Similar share, slightly positive.** 5.7% vetoed. A minus momentum: +0.007% a day (t +1.7); from 2010, t +3.0; fund t +1.6. | More names, and the conviction floor (0.30) leaves stronger signals. The t of 3.0 is one slice out of many, with 33 trials in N. Treat it as a hint, not proof. Under 10% vetoed means A is almost momentum. |
| C: filled 63%; missed +1.0% against filled -1.0%. | **The same.** Filled 61.2%; missed +0.88% against filled -0.93%. | Same rule; the small gap is the names and the stand-in price. As you said, this is built in: a fill means the price fell first, inside the same 3 sessions. The fair test is the C fund against the momentum fund: no clear difference (t +0.7). |
| B on SPY and VT: smaller crashes, but 3-4% a year less return since 2007. | **The same from 2010 (3.5-4% a year less). Since 2007 only on SPY: 1.2% a year less, with half the worst fall.** On VT the rule starts in April 2009, so there is no 2008 crash in it. | VT's prices start in June 2008, and the rule needs 10 month-ends first. On SPY, 2007-2009 counts and B avoided most of 2008, which pays back much of the later lag. The real code also pays 0.10% per switch and buys T-bills (BIL), not cash. |

## Context for the live race

At a 3-day horizon, momentum on history is close to a coin flip. So in the
live race, **"the AI beats momentum" may mean little more than "the AI beats
random"**. The race's other floor, the coin flip on the model's own lines, is
also weak for a model that is mostly long: on history, simply buying every
line that momentum picked scores far above the coin flip's band, with no
skill at all. The real test is the index: the winner must beat VT. On
history, none of the rules did that from 2010.

This is context only. The locked test does not change.

## What the screen adds to the graveyard

N is now 33:
- 18 ideas
- 10 quick history tests of yours (rows 19 to 28)
- 5 rows for this screen (rows 29 to 33)

Your 1-3 month momentum test is one row; if 1, 2 and 3 months were separate
settings, it is three rows, and N is 35.
