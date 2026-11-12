SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        3592
entries                   3592
  produced a signal       2777
  directional             275  (NEUTRAL: 2502)
  scored                  254
  unscored, pending         21  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.15 (n=254)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        72      33.3%     -1.0%     -0.4%
0.45-0.60       108      53.7%     -0.4%     +0.1%
0.60-0.75        61      60.7%     +0.7%     +0.8%
0.75-1.00        12      25.0%     -1.0%     -1.2%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=253   hit 48.2%  mean -0.3%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.4% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            254         -0.07
technical       254         -0.04
fundamental     254         -0.19
analyst         214         -0.07
insider         211         -0.11

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   2589     253         -0.02     48.2%
equal weights      2589    2397         +0.03     51.1%
learned blend      2198    2075         -0.01     50.3%
  learned composites from fitted weights: 1870; from the equal-weight fallback: 328

  model and blend called opposite directions  n=96    model hit 46.9%  blend hit 53.1%

  the learned blend beats the model's conviction but not equal weights; the fitted weights are not yet earning their keep

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=1201  mean conviction 0.070
  at least one dissents  n=1576  mean conviction 0.152
  gap -0.082 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.28 (n=2777) (negative is correct)
    ...but spread vs loudest single score: +0.84 (n=2777) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.15 (n=2777) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=1388  mean 0.164  above floor 22.1%
  second half  n=1389  mean 0.068  above floor 12.9%
  change -0.096

Input health
------------
  cycles with a context gap  335/3592 (9.3%)
    news unavailable                         334
    CFTC positioning unavailable             1

  bias distribution (2777 signals)
    BULLISH      210  7.6%
    BEARISH       65  2.3%
    NEUTRAL     2502  90.1%
  cycles that produced no signal: 161

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
