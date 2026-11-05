SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        3192
entries                   3192
  produced a signal       2457
  directional             242  (NEUTRAL: 2215)
  scored                  227
  unscored, pending         15  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.10 (n=227)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        69      34.8%     -0.7%     -0.3%
0.45-0.60        98      53.1%     -0.4%     +0.1%
0.60-0.75        49      57.1%     -0.1%     +0.8%
0.75-1.00        10      30.0%     -1.0%     -1.2%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=226   hit 47.3%  mean -0.4%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.3% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            227         -0.08
technical       227         -0.04
fundamental     227         -0.21
analyst         187         -0.07
insider         184         -0.07

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   2273     226         -0.02     47.3%
equal weights      2273    2121         +0.01     50.0%
learned blend      1882    1783         -0.00     50.0%
  learned composites from fitted weights: 1554; from the equal-weight fallback: 328

  model and blend called opposite directions  n=77    model hit 44.2%  blend hit 55.8%

  the learned blend beats the model's conviction but not equal weights; the fitted weights are not yet earning their keep

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=1023  mean conviction 0.077
  at least one dissents  n=1434  mean conviction 0.156
  gap -0.079 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.27 (n=2457) (negative is correct)
    ...but spread vs loudest single score: +0.84 (n=2457) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.15 (n=2457) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=1228  mean 0.173  above floor 22.4%
  second half  n=1229  mean 0.073  above floor 14.2%
  change -0.100

Input health
------------
  cycles with a context gap  294/3192 (9.2%)
    news unavailable                         293
    CFTC positioning unavailable             1

  bias distribution (2457 signals)
    BULLISH      180  7.3%
    BEARISH       62  2.5%
    NEUTRAL     2215  90.2%
  cycles that produced no signal: 159

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
