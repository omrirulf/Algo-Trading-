SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        712
entries                   712
  produced a signal       664
  directional             84  (NEUTRAL: 580)
  scored                  56
  unscored, pending         28  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.25 (n=56)

conviction        n   hit rate      mean    median
0.30-0.45        37      13.5%     -1.2%     -0.6%
0.45-0.60        19      52.6%     +0.5%     +0.7%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=56    hit 26.8%  mean -0.6%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news             56         -0.17
technical        56         -0.17
fundamental      56         +0.06
analyst          25         +0.29
insider          19-0.06 — too few

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction    390      56         -0.12     26.8%
equal weights       390     389         -0.04     48.1%
learned blend       124     123         +0.06     55.3%
  learned composites from fitted weights: 0; from the equal-weight fallback: 124

  READY TO LEAVE SHADOW: the learned blend carries more information than the model's conviction and than equal weights, and was right more often than not

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=184   mean conviction 0.245
  at least one dissents  n=480   mean conviction 0.274
  gap -0.028 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.33 (n=664) (negative is correct)
    ...but spread vs loudest single score: +0.80 (n=664) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               -0.02 (n=664) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=332   mean 0.286  above floor 34.9%
  second half  n=332   mean 0.246  above floor 25.6%
  change -0.040

Input health
------------
  cycles with a context gap  4/712 (0.6%)
    news unavailable                         4

  bias distribution (664 signals)
    BULLISH       40  6.0%
    BEARISH       44  6.6%
    NEUTRAL      580  87.3%
  cycles that produced no signal: 6

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
