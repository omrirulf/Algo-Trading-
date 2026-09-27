# Insider cluster buying (exploratory arm)

**Date:** 2026-09-22 (section 2)

**Source:** Lakonishok and Lee (2001), six-month insider purchase aggregation.

**Exact rule and settings:** BULLISH when, in the 180 days before the line, two or more distinct insiders made open-market purchases and bought more shares than they sold; else NEUTRAL. Conviction 0.50.

**Data used:** The line's insider section.

**Compared against:** Momentum, on the lines the insider arm took a side on.

**Main metric:** Its net return minus momentum's on the same lines (0 where momentum did not trade), averaged per entry day, Newey-West t (lag 3); section 13.5.

**Read on:** Printed nightly by the race since 2026-09-22 (registered before section 13); in the checkpoint table with Benjamini-Hochberg and the DSR.

**Promising if:** At a checkpoint, it beats its comparator and passes Benjamini-Hochberg at 5% (section 13.5). The Deflated Sharpe Ratio is shown beside it (13.6).

**Dead if:** At any checkpoint it trails its comparator and passes Benjamini-Hochberg in that direction; or at the final checkpoint its mean difference is zero or below (section 13.7).

**Trial number:** 5
