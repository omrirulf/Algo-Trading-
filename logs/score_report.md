SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        1032
entries                   1032
  produced a signal       829
  directional             90  (NEUTRAL: 739)
  scored                  84
  unscored, pending         6  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.29 (n=84)

conviction        n   hit rate      mean    median
0.30-0.45        50      24.0%     -1.0%     -0.5%
0.45-0.60        31      58.1%     +0.6%     +0.8%
0.60-0.75         3      66.7%     -0.9%     +0.8%  (thin)

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=84    hit 38.1%  mean -0.4%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news             84         -0.12
technical        84         -0.15
fundamental      84         +0.10
analyst          48         +0.05
insider          41         -0.27

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction    664      84         -0.07     38.1%
equal weights       664     650         -0.07     46.6%
learned blend       273     260         +0.07     54.2%
  learned composites from fitted weights: 53; from the equal-weight fallback: 220

  model and blend called opposite directions  n=7     model hit 28.6%  blend hit 71.4%

  READY TO LEAVE SHADOW: the learned blend carries more information than the model's conviction and than equal weights, and was right more often than not

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=249   mean conviction 0.184
  at least one dissents  n=580   mean conviction 0.236
  gap -0.052 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.26 (n=829) (negative is correct)
    ...but spread vs loudest single score: +0.81 (n=829) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.02 (n=829) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=414   mean 0.291  above floor 36.7%
  second half  n=415   mean 0.150  above floor 14.9%
  change -0.140

Input health
------------
  cycles with a context gap  27/1032 (2.6%)
    news unavailable                         27

  bias distribution (829 signals)
    BULLISH       44  5.3%
    BEARISH       46  5.5%
    NEUTRAL      739  89.1%
  cycles that produced no signal: 73

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
