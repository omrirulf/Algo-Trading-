SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        391
entries                   391
  produced a signal       389
  directional             56  (NEUTRAL: 333)
  scored                  0
  unscored, pending         56  (too recent — no outcome yet)

No signal has a realised return yet. Everything below needs price
outcomes; the agreement check is the exception and runs anyway.

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=123   mean conviction 0.268
  at least one dissents  n=266   mean conviction 0.295
  gap -0.026 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.40 (n=389) (negative is correct)
  Across several dimensions unanimity is rare and 'at least one dissents' is
  the common case — read the spread correlation as the finer measure.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=194   mean 0.296  above floor 42.3%
  second half  n=195   mean 0.277  above floor 26.7%
  change -0.020

Input health
------------
  cycles with a context gap  0/391 (0.0%)

  bias distribution (389 signals)
    BULLISH       23  5.9%
    BEARISH       33  8.5%
    NEUTRAL      333  85.6%
  cycles that produced no signal: 2

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
