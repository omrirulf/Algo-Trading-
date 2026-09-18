SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        472
entries                   472
  produced a signal       469
  directional             66  (NEUTRAL: 403)
  scored                  23
  unscored, pending         43  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.15 (n=23)

conviction        n   hit rate      mean    median
0.30-0.45        14       7.1%     -1.7%     -1.5%
0.45-0.60         9      22.2%     -1.2%     -0.6%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=23    hit 13.0%  mean -1.5%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news             23         -0.59
technical        23         -0.54
fundamental      23         -0.05
analyst           6+0.09 — too few
insider           6+0.09 — too few

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction    105      23         -0.34     13.0%
equal weights       105     105         -0.32     36.2%
learned blend         0       0           n/a       n/a

  no line carries a learned composite yet; the equal-weight row is the floor the fitted weights have to clear

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=137   mean conviction 0.270
  at least one dissents  n=332   mean conviction 0.292
  gap -0.022 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.36 (n=469) (negative is correct)
  Across several dimensions unanimity is rare and 'at least one dissents' is
  the common case — read the spread correlation as the finer measure.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=234   mean 0.294  above floor 41.5%
  second half  n=235   mean 0.276  above floor 25.1%
  change -0.018

Input health
------------
  cycles with a context gap  0/472 (0.0%)

  bias distribution (469 signals)
    BULLISH       26  5.5%
    BEARISH       40  8.5%
    NEUTRAL      403  85.9%
  cycles that produced no signal: 3

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
