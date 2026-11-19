SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        3912
entries                   3912
  produced a signal       2937
  directional             291  (NEUTRAL: 2646)
  scored                  284
  unscored, pending         7  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.10 (n=284)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        77      32.5%     -1.1%     -0.5%
0.45-0.60       118      51.7%     -0.6%     +0.1%
0.60-0.75        72      55.6%     +0.2%     +0.8%
0.75-1.00        16      25.0%     -0.9%     -1.0%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=283   hit 45.9%  mean -0.5%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.2% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            284         -0.08
technical       284         -0.04
fundamental     284         -0.23
analyst         244         -0.06
insider         241         -0.13

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   2839     283         -0.03     45.9%
equal weights      2839    2625         -0.01     48.3%
learned blend      2448    2311         +0.01     50.9%
  learned composites from fitted weights: 2120; from the equal-weight fallback: 328

  model and blend called opposite directions  n=119   model hit 42.9%  blend hit 57.1%

  READY TO LEAVE SHADOW: the learned blend carries more information than the model's conviction and than equal weights, and was right more often than not

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=1271  mean conviction 0.068
  at least one dissents  n=1666  mean conviction 0.149
  gap -0.081 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.28 (n=2937) (negative is correct)
    ...but spread vs loudest single score: +0.84 (n=2937) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.15 (n=2937) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=1468  mean 0.159  above floor 21.7%
  second half  n=1469  mean 0.069  above floor 12.9%
  change -0.091

Input health
------------
  cycles with a context gap  351/3912 (9.0%)
    news unavailable                         350
    CFTC positioning unavailable             1

  bias distribution (2937 signals)
    BULLISH      225  7.7%
    BEARISH       66  2.2%
    NEUTRAL     2646  90.1%
  cycles that produced no signal: 247

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
