# model_sized (exploratory fund)

**Date:** 2026-09-25 (section 11.1)

**Source:** None: the owner's question (does sizing by conviction help?).

**Exact rule and settings:** The model fund, each new position sized at the normal size times 0.25, 0.5, 1.0 or 1.5 for conviction 0.30-0.40, 0.40-0.50, 0.50-0.60, 0.60 and above.

**Data used:** The journal's model answers; the funds' prices.

**Compared against:** The model fund.

**Main metric:** Mean daily difference, Newey-West t (lag 5); maximum drawdown beside the model fund's.

**Read on:** At each checkpoint only: the race's looks (estimated 2026-12-22, 2027-03-22, 2027-06-16). Between them, only the counters (section 13.1).

**Promising if:** At a checkpoint, it beats its comparator and passes Benjamini-Hochberg at 5% (section 13.5). The Deflated Sharpe Ratio is shown beside it (13.6).

**Dead if:** At any checkpoint it trails its comparator and passes Benjamini-Hochberg in that direction; or at the final checkpoint its mean difference is zero or below (section 13.7).

**Trial number:** 10
