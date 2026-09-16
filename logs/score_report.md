SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        261
entries                   261
  produced a signal       261
  directional             48  (NEUTRAL: 213)
  scored                  0
  unscored, pending         48  (too recent — no outcome yet)

No signal has a realised return yet. Everything below needs price
outcomes; the agreement check is the exception and runs anyway.

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=98    mean conviction 0.267
  at least one dissents  n=163   mean conviction 0.303
  gap -0.036 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.44 (n=261) (negative is correct)
  Across several dimensions unanimity is rare and 'at least one dissents' is
  the common case — read the spread correlation as the finer measure.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=130   mean 0.309  above floor 53.1%
  second half  n=131   mean 0.270  above floor 23.7%
  change -0.038

Input health
------------
  cycles with a context gap  0/261 (0.0%)

  bias distribution (261 signals)
    BULLISH       15  5.7%
    BEARISH       33  12.6%
    NEUTRAL      213  81.6%

How to read this
----------------
* Returns are close-to-close over 3 session(s) and ignore the stop-loss,
  slippage and commission. They measure the signal, not the strategy's P&L.
* Entry rule 'auto': same-session close when the signal fired before the close
  and carried an exact UTC timestamp, next session's close otherwise.
* Anything marked 'too few' has fewer than 20 observations. It is
  arithmetic, not evidence — the sign can flip on one more data point.
* A single earnings day can dominate a small sample; rank correlations are
  used throughout to blunt that, not to eliminate it.
