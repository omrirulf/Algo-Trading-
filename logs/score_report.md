SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        2472
entries                   2472
  produced a signal       1891
  directional             190  (NEUTRAL: 1701)
  scored                  173
  unscored, pending         17  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.17 (n=173)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        62      29.0%     -0.9%     -0.5%
0.45-0.60        74      56.8%     +0.2%     +0.4%
0.60-0.75        32      59.4%     +0.4%     +0.8%
0.75-1.00         4       0.0%     -1.2%     -1.4%  (thin)

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=172   hit 45.9%  mean -0.2%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.6% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            173         -0.12
technical       173         -0.15
fundamental     173         -0.10
analyst         134         +0.00
insider         130         -0.15

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   1689     172         -0.02     45.9%
equal weights      1689    1597         -0.01     48.5%
learned blend      1298    1238         -0.02     48.9%
  learned composites from fitted weights: 970; from the equal-weight fallback: 328

  model and blend called opposite directions  n=42    model hit 42.9%  blend hit 57.1%

  the learned blend beats the model's conviction but not equal weights; the fitted weights are not yet earning their keep

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=731   mean conviction 0.092
  at least one dissents  n=1160  mean conviction 0.168
  gap -0.076 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.27 (n=1891) (negative is correct)
    ...but spread vs loudest single score: +0.83 (n=1891) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.14 (n=1891) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=945   mean 0.199  above floor 23.8%
  second half  n=946   mean 0.077  above floor 15.6%
  change -0.122

Input health
------------
  cycles with a context gap  179/2472 (7.2%)
    news unavailable                         179

  bias distribution (1891 signals)
    BULLISH      135  7.1%
    BEARISH       55  2.9%
    NEUTRAL     1701  90.0%
  cycles that produced no signal: 145

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
