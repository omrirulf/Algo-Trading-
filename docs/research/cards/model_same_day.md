# model_same_day (exploratory fund)

**Date:** 2026-09-26 (section 11.1)

**Source:** None: the owner's question (does buying on the signal's own day change the result?).

**Exact rule and settings:** The model fund, each line entered on its own day at the price recorded with its signal (ask for a buy, bid for a short, else last trade), after that session's stop checks.

**Data used:** The journal's model answers and live prices; the funds' prices.

**Compared against:** The model fund.

**Main metric:** Mean daily difference, Newey-West t (lag 5).

**Read on:** At each checkpoint only: the race's looks (estimated 2026-12-22, 2027-03-22, 2027-06-16). Between them, only the counters (section 13.1). Counters: lines not entered, and why, from the 2026-09-28 cycle (the fund's start).

**Acting differently:** Always: every trade is entered on another day at another price, so it always counts as acting.

**Promising if:** At a checkpoint, it beats its comparator and passes Benjamini-Hochberg at 5% (section 13.5). The Deflated Sharpe Ratio is shown beside it (13.6).

**Dead if:** At any checkpoint it trails its comparator and passes Benjamini-Hochberg in that direction; or at the final checkpoint its mean difference is zero or below (section 13.7).

**Trial number:** 11
