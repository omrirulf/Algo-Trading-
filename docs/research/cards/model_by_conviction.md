# model_by_conviction (exploratory fund)

**Date:** 2026-09-25 (section 11.1)

**Source:** None: the owner's question (does the buying order matter?).

**Exact rule and settings:** The model fund, with each cycle's lines dispatched highest conviction first (ties in watchlist order).

**Data used:** The journal's model answers; the funds' prices.

**Compared against:** The model fund.

**Main metric:** Mean daily difference, Newey-West t (lag 5).

**Read on:** At each checkpoint only: the race's looks (estimated 2026-12-22, 2027-03-22, 2027-06-16). Between them, only the counters (section 13.1).

**Acting differently:** A session on which the buying order changed what was bought, compared with the model fund (counted at the checkpoint).

**Promising if:** At a checkpoint, it beats its comparator and passes Benjamini-Hochberg at 5% (section 13.5). The Deflated Sharpe Ratio is shown beside it (13.6).

**Dead if:** At any checkpoint it trails its comparator and passes Benjamini-Hochberg in that direction; or at the final checkpoint its mean difference is zero or below (section 13.7). At the final checkpoint, fewer than 20 times acting differently is "not tested", whatever the numbers (section 13.7).

**Trial number:** 9
