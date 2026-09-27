# B: 10-month moving-average timing on VT

**Date:** 2026-09-27 (registered 2026-09-28, section 13.3)

**Source:** Faber (2007; updated 2013 and 2018).

**Exact rule and settings:** On each month's last trading day: VT's close above the mean of its last 10 month-end closes (that one included) → all in VT; otherwise all in BIL. Trade at the next open, 0.10% per side; dividends credited. Start: the 2026-09-30 month-end, first trade 2026-10-01.

**Data used:** Final daily closes and dividends of VT and BIL.

**Compared against:** The VT fund (bought and held).

**Main metric:** Mean daily net return, B minus VT fund, paired over B's sessions, Newey-West t (lag 5). Also total return and maximum drawdown of both.

**Read on:** At each checkpoint only: the race's looks (estimated 2026-12-22, 2027-03-22, 2027-06-16). Between them, only the counters (section 13.1). Counters: switches so far and the current state (VT or BIL).

**Promising if:** At a checkpoint, it beats its comparator and passes Benjamini-Hochberg at 5% (section 13.5). The Deflated Sharpe Ratio is shown beside it (13.6).

**Dead if:** At any checkpoint it trails its comparator and passes Benjamini-Hochberg in that direction; or at the final checkpoint its mean difference is zero or below (section 13.7).

**Trial number:** 17
