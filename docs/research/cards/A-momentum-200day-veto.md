# A: momentum with a 200-day moving-average veto

**Date:** 2026-09-27 (registered 2026-09-28, section 13.2)

**Source:** Brock, Lakonishok and LeBaron (1992), price against its 200-day moving average.

**Exact rule and settings:** The locked momentum signal on each line; keep a LONG only if the line's live price (`live.price`) is above the 200-day simple moving average, a SHORT only if it is below; otherwise NEUTRAL. The average: the last 200 final daily closes up to the close of the session before the signal's day. Strict above/below. No live price, or fewer than 200 closes: the momentum signal is kept, counted. Conviction unchanged.

**Data used:** Journal lines from the 2026-09-28 cycle (technicals, live price); final daily closes.

**Compared against:** The momentum race arm, and the momentum fund.

**Main metric:** Race arm: mean daily net return, A minus momentum, all names, Newey-West t (lag 3). Fund: mean daily net return, A fund minus momentum fund, Newey-West t (lag 5).

**Read on:** At each checkpoint only: the race's looks (estimated 2026-12-22, 2027-03-22, 2027-06-16). Between them, only the counters (section 13.1). Counter: the share of momentum's signals the veto removes; under about 10% is said at the first checkpoint.

**Promising if:** At a checkpoint, it beats its comparator and passes Benjamini-Hochberg at 5% (section 13.5). The Deflated Sharpe Ratio is shown beside it (13.6).

**Dead if:** At any checkpoint it trails its comparator and passes Benjamini-Hochberg in that direction; or at the final checkpoint its mean difference is zero or below (section 13.7).

**Trial number:** 16 (the dropped 50-day version is trial 15)
