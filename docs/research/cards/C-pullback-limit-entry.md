# C: pullback limit entry

**Date:** 2026-09-27 (registered 2026-09-28, section 13.4)

**Source:** None published for these settings: the owner's fixed choice.

**Exact rule and settings:** The momentum fund's signals; a limit buy at signal price − 0.5 × ATR14 (short: + 0.5 × ATR14), valid 3 sessions, then cancelled. Signal price: the line's live price, else its technicals price. ATR14: the line's own. Fill at the open if it opens at or past the limit, else at the limit if the day's range reaches it. Sized and checked at the fill.

**Data used:** Journal lines from the 2026-09-28 cycle; daily open, high, low, close.

**Compared against:** The momentum fund.

**Main metric:** Mean daily net return, C fund minus momentum fund, Newey-West t (lag 5).

**Read on:** At each checkpoint only: the race's looks (estimated 2026-12-22, 2027-03-22, 2027-06-16). Between them, only the counters (section 13.1). Counters: fill rate, filled and missed signals. Prediction: fill rate well below 100%, and missed signals do better than filled ones (read at checkpoints, Welch t for reading only).

**Acting differently:** A momentum signal on which C and the momentum fund did differently: one bought it and the other did not, or both bought it at different prices. A signal both funds skipped (the name held in both, or no room in either) is not a difference (counted at the checkpoint).

**Promising if:** At a checkpoint, it beats its comparator and passes Benjamini-Hochberg at 5% (section 13.5). The Deflated Sharpe Ratio is shown beside it (13.6).

**Dead if:** At any checkpoint it trails its comparator and passes Benjamini-Hochberg in that direction; or at the final checkpoint its mean difference is zero or below (section 13.7). At the final checkpoint, fewer than 20 times acting differently is "not tested", whatever the numbers (section 13.7).

**Trial number:** 18
