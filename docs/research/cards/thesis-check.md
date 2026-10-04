# The thesis check: does the reason a held name was bought still hold? (logger)

**Date:** 2026-10-04 (prepared; **registered at the race's second planned look, estimated 2027-03-22, as an idea of the second quarter of 2027, and on from 2027-04-01**; pre-registration section 13.12). Built now and switched off: `THESIS_CHECK_ENABLED` is off until 2027-04-01, and a test fails if it is turned on before that date. Nothing on this card is changed after registration.

**Source:** None: the owner's fixed choice of 2026-10-04.

**Exact rule and settings:** Every number is in `config/thesis_check.py`.
- *When:* once a week, on the first trading day of each ISO week on which the production cycle is journalled, after the vote (the same workflow run, never at the same time as production, the shadow universe or the vote). A name not checked that day (time, the cost cap, a failed call) is tried again on the next trading day of the same week, while it is still held.
- *Which names:* every name the paper account holds that day: the tickers with a held line in that day's production cycle.
- *The question:* one call per name to the same model, with production's settings (`openai/gpt-oss-120b`, reasoning level high): given the entry reasoning archived with the entry (the rationale and key factors of the signal that opened the position: the latest accepted `signal_processed` record for the name in the execution audit log, the rule `analysis/book.py` uses) and today's headlines for the name (the ones production gathered on its held line that day; none is said as none), is the thesis VALID, WEAKENED or BROKEN? With one sentence of reason (at most 300 characters). The prompt's words are fixed in `orchestrator/thesis.py`.
- *Log only:* one line per name per week in `logs/thesis_check/`. It never trades, never changes a stop, never feeds any arm or fund, and nothing in the cycle reads it.
- *Cost:* a hard cap of $0.10 a week (about $0.06 expected: about 20 held names at about $0.003 a call); every HTTP ask counted. No news search is paid.

**Data used:** The production journal's held lines (their headlines), the execution audit log (the entry's signal), the logger's own lines (`logs/thesis_check/`), and, at the checkpoints, final daily bars (open and close) from the race's price source.

**Compared against:** VALID checks: the forward returns of the names checked BROKEN against those of the names checked VALID. WEAKENED is shown on its own.

**Main metric:** None: it is a report, not a test. At each checkpoint after its registration, as a description only: for every check from 2027-04-01, the forward return from the open of the first session after the check's day to the close of the 5th session (one week, the time to the next check), price only, signed by the position's side (+1 bought, −1 sold short). For BROKEN, WEAKENED and VALID: the number, mean and hit rate; and BROKEN minus VALID, with a Welch t for reading only (checks made on the same day are not independent). Not in the Benjamini-Hochberg family, no Deflated Sharpe Ratio.

**Survives its history screen if:** No history screen (uses the AI).

**History screen:** Not possible (uses the AI).

**Read on:** At each checkpoint after its registration: the estimated 2027-06-16 look (the race's final one). Between checkpoints, from 2027-04-01, only counters (checks made, names, weeks, failed checks). Nothing at all before 2027-04-01.

**Acting differently:** Not a test, so nothing acts differently in section 13.7's sense. Its count is the BROKEN checks: fewer than 20 by the final checkpoint and the comparison is "not tested".

**Promising if:** Nothing is promising or dead: it is a description. A clear difference (BROKEN names doing worse than VALID ones) would only be a candidate for a later registration, for example as an exit rule, with its own card, graveyard row and registration.

**Dead if:** Nothing: see above.

**Trial number:** 43 (one trial in N)
