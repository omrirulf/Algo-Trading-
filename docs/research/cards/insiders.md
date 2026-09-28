# Insider cluster buying (exploratory arm)

**Date:** 2026-09-22 (section 2)

**Source:** Lakonishok and Lee (2001), six-month insider purchase aggregation.

**Exact rule and settings:** BULLISH when, in the 180 days before the line, two or more distinct insiders made open-market purchases and bought more shares than they sold; else NEUTRAL. Conviction 0.50.

**Data used:** The line's insider section.

**Compared against:** Momentum, on the lines the insider arm took a side on.

**Main metric:** Its net return minus momentum's on the same lines (0 where momentum did not trade), averaged per entry day, Newey-West t (lag 3); section 13.5.

**Read on:** At each checkpoint only: the race's looks (estimated 2026-12-22, 2027-03-22, 2027-06-16), in the checkpoint table with Benjamini-Hochberg and the DSR. Between them, only its counters: lines it took a side on, and trades at each horizon (section 13.1). Its results were printed nightly from 2026-09-22 to 2026-09-28, before section 13 existed; nothing is undone.

**Acting differently:** A trade of the insider arm (its counter, at each horizon).

**Promising if:** At a checkpoint, it beats its comparator and passes Benjamini-Hochberg at 5% (section 13.5). The Deflated Sharpe Ratio is shown beside it (13.6).

**Dead if:** At any checkpoint it trails its comparator and passes Benjamini-Hochberg in that direction; or at the final checkpoint its mean difference is zero or below (section 13.7). At the final checkpoint, fewer than 20 times acting differently is "not tested", whatever the numbers (section 13.7).

**Trial number:** 5
