SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        3672
entries                   3672
  produced a signal       2839
  directional             284  (NEUTRAL: 2555)
  scored                  262
  unscored, pending         22  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.16 (n=262)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        74      33.8%     -1.0%     -0.4%
0.45-0.60       109      55.0%     -0.4%     +0.1%
0.60-0.75        65      60.0%     +0.6%     +0.8%
0.75-1.00        13      30.8%     -0.8%     -1.1%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=261   hit 49.0%  mean -0.3%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.4% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            262         -0.06
technical       262         -0.06
fundamental     262         -0.18
analyst         222         -0.07
insider         219         -0.11

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   2653     261         -0.01     49.0%
equal weights      2653    2456         +0.02     49.8%
learned blend      2262    2135         -0.01     50.6%
  learned composites from fitted weights: 1934; from the equal-weight fallback: 328

  model and blend called opposite directions  n=103   model hit 48.5%  blend hit 51.5%

  the learned blend beats the model's conviction but not equal weights; the fitted weights are not yet earning their keep

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=1232  mean conviction 0.070
  at least one dissents  n=1607  mean conviction 0.151
  gap -0.082 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.28 (n=2839) (negative is correct)
    ...but spread vs loudest single score: +0.84 (n=2839) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.15 (n=2839) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=1419  mean 0.161  above floor 21.7%
  second half  n=1420  mean 0.070  above floor 13.2%
  change -0.091

Input health
------------
  cycles with a context gap  338/3672 (9.2%)
    news unavailable                         337
    CFTC positioning unavailable             1

  bias distribution (2839 signals)
    BULLISH      219  7.7%
    BEARISH       65  2.3%
    NEUTRAL     2555  90.0%
  cycles that produced no signal: 162

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
