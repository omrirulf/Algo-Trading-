SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        632
entries                   632
  produced a signal       602
  directional             75  (NEUTRAL: 527)
  scored                  56
  unscored, pending         19  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.39 (n=56)

conviction        n   hit rate      mean    median
0.30-0.45        37      13.5%     -1.2%     -0.6%
0.45-0.60        19      63.2%     +1.1%     +1.5%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=56    hit 30.4%  mean -0.4%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news             56         -0.11
technical        56         -0.12
fundamental      56         +0.20
analyst          25         +0.42
insider          19+0.40 — too few

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction    390      56         -0.07     30.4%
equal weights       390     389         -0.03     47.3%
learned blend       124     123         +0.17     58.5%
  learned composites from fitted weights: 0; from the equal-weight fallback: 124

  READY TO LEAVE SHADOW: the learned blend carries more information than the model's conviction and than equal weights, and was right more often than not

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=161   mean conviction 0.271
  at least one dissents  n=441   mean conviction 0.286
  gap -0.015 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.33 (n=602) (negative is correct)
    ...but spread vs loudest single score: +0.79 (n=602) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               -0.05 (n=602) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=301   mean 0.291  above floor 38.5%
  second half  n=301   mean 0.274  above floor 23.9%
  change -0.017

Input health
------------
  cycles with a context gap  0/632 (0.0%)

  bias distribution (602 signals)
    BULLISH       31  5.1%
    BEARISH       44  7.3%
    NEUTRAL      527  87.5%
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
