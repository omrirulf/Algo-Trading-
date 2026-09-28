# Summary: the rules that run live, tested on 2000 to 2026

This is the short version of [the report](report.md). All numbers come from
[`results.json`](results.json) (workflow run 36382668730). The screen replays
momentum, A, B and C on past prices with the real code: production's
technicals, the race's own scoring and the production fund engine. Costs are
0.10% per side, with no taxes. It covers 80 names (today's watchlist) from
3 Jan 2000 to 25 Sep 2026. It adds 5 rows to the graveyard (30 to 34).

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
- **Split-adjusted prices.** Early NVDA and HDB trade under $1. There the
  engine's stops are rounded to the cent and are coarse. This touches 1% of
  momentum's race trades and 2% of the fund's entries; they are counted, not
  removed.

## The answers in short

| Rule | Race (3-session trades) | Fund | In one line |
| --- | --- | --- | --- |
| Momentum | No clear difference from a coin flip (t -0.07). Behind always long since 2010 (t -2.3 on the same lines). | -3.5% a year (2000-2026). Far behind the VT fund since 2010 (t -3.0). Positions last about 11 days; costs take 4.8% a year. | No edge at 3 days; in the fund, trading costs eat what little there is. |
| A (200-day veto) | Vetoes 5.7% of signals. A minus momentum: +0.007% a day (t +1.7); from 2010, t +3.0. | A fund minus momentum fund: t +1.6. Also far behind VT. | A little better than momentum, but it is still almost momentum (under 10% vetoed). |
| B (VT or T-bills) | not a race rule | From April 2009: 6.5% a year against 11.3% for the VT fund; worst fall 28% against 29%. B minus VT: t -2.0. | About 5% a year behind VT since April 2009 (3.5% from 2010), with no crash protection: VT's data starts after 2008. |
| B's rule on SPY (check) | not a race rule | From June 2007: 7.8% a year against 9.0% for SPY; worst fall 25% against 50%. From 2010: 4.1% a year less. | Halves the 2008 crash; costs about 4% a year in calm years. |
| C (pullback limit) | Fills 61% of signals. Missed +0.88% against filled -0.93% per trade: built in. | C fund minus momentum fund: +0.003% a day (t +0.7). Most limits that were reached could not be bought: the book was full. | No clear difference from momentum. |

## Where my results differ from your quick test, and why

| Your quick test (38 ETFs, 2000-2026, 2 x ATR stop) | This screen (80 names, real code) | Why |
| --- | --- | --- |
| Momentum, 3-day trades: no better than a coin flip. | **The same.** Minus a coin flip: -0.002% a day, t -0.07. Before 2010: t +0.29. From 2010: t -0.51. | Same answer. At 3 days the moves are mostly noise, and 0.2% per round trip is bigger than any edge. |
| At 1-3 months it worked in 2000-2009. | **Not tested at 1-3 months.** The registered race is 3 sessions, and a new holding time would be a new trial. The fund is the closest thing, but it holds positions for about 11 days. It lost 28% in 2000-2009, while SPY lost 8%. Only in the 2008-2009 crash did it beat VT (+10.6% a year against -8.1%). | Different holding time: the production stop and profit ladder close positions after about 2 weeks, not 1-3 months. The fund also pays 4.8% a year in costs, holds 16 companies, and when it is full (90% of days) it buys in watchlist order. |
| Since 2010 its buys trailed holding all the ETFs. | **Same direction, weaker.** From 2010, race longs minus buying every line on the same days: -0.020% a day (t -0.9). All trades minus always long on every line: -0.091% a day (t -2.1). | My "every line" includes the companies. Neither side picks names better than taking that side on every line (longs t -0.9, shorts t +1.1 from 2010). The loss comes from shorting at all in a rising market. |
| Its shorts lost about 3.7% per 3-month short. | **Smaller, but still losing.** From 2010: race shorts -0.37% per 3-session trade (after 0.2% costs); fund shorts -0.74% per closed trade. | Much shorter trades, and the stop cuts a short that goes wrong. Over 3 months, a short in a rising market loses more. |
| A: removed only about 4% of signals, no clear difference. | **Similar share, slightly positive.** 5.7% vetoed. A minus momentum: +0.007% a day (t +1.7); from 2010, t +3.0; fund, t +1.6. | More names, and the conviction floor (0.30) keeps only the stronger signals. The t of 3.0 is one slice out of many, with N = 34 trials: a hint, not proof. With under 10% vetoed, A is almost momentum. |
| C: filled 63%; missed +1.0% against filled -1.0%. | **The same.** Filled 61.2%; missed +0.88% against filled -0.93%. | Same rule; the small gap comes from the names and the stand-in price. As you said, this is built in: a fill means the price fell first, inside the same 3 sessions. The fair test is the C fund against the momentum fund, and it shows no clear difference (t +0.7). |
| B on SPY and VT: smaller crashes, but 3-4% a year less return since 2007. | **The same from 2010 (3.5% a year less on VT, 4.1% on SPY).** On SPY since June 2007: only 1.2% a year less, and half the worst fall. On VT the rule starts in April 2009, so there is no 2008 crash in it, and its worst fall is almost VT's. | VT's prices start in June 2008, and the rule needs 10 month-ends first. On SPY, 2007-2009 counts, and B avoided most of 2008, which pays back much of the later lag. The real code also pays 0.10% per switch and holds T-bills (BIL), not plain cash. |

## Context for the live race

At a 3-day horizon, momentum on history is close to a coin flip. So in the
live race, **"the AI beats momentum" may mean little more than "the AI beats
random"**.

The race's other floor, the coin flip on the model's own lines, is also weak
for a model that is mostly long. On history, simply buying every line that
momentum picked sits at the 100th percentile of the coin flip's band, with no
skill at all.

The real test is the index: the winner must beat VT. On history, none of these
rules did that from 2010.

This is context only. The locked test does not change.

## What the screen adds to the graveyard

N is now 34:
- 18 ideas
- 11 quick history tests of yours (rows 19 to 29; the momentum test is three
  rows, held 3, 21 and 63 sessions)
- 5 rows for this screen (rows 30 to 34)
