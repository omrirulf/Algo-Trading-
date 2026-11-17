SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        3832
entries                   3832
  produced a signal       2888
  directional             287  (NEUTRAL: 2601)
  scored                  275
  unscored, pending         12  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.13 (n=275)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        75      33.3%     -1.0%     -0.5%
0.45-0.60       115      53.0%     -0.5%     +0.1%
0.60-0.75        69      58.0%     +0.6%     +0.8%
0.75-1.00        15      26.7%     -0.7%     -0.7%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=274   hit 47.4%  mean -0.4%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.4% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            275         -0.07
technical       275         -0.03
fundamental     275         -0.21
analyst         235         -0.07
insider         232         -0.12

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   2777     274         -0.02     47.4%
equal weights      2777    2569         +0.01     48.9%
learned blend      2386    2253         +0.00     50.7%
  learned composites from fitted weights: 2058; from the equal-weight fallback: 328

  model and blend called opposite directions  n=113   model hit 45.1%  blend hit 54.9%

  the learned blend beats the model's conviction but not equal weights; the fitted weights are not yet earning their keep

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=1254  mean conviction 0.068
  at least one dissents  n=1634  mean conviction 0.150
  gap -0.081 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.28 (n=2888) (negative is correct)
    ...but spread vs loudest single score: +0.84 (n=2888) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.15 (n=2888) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=1444  mean 0.159  above floor 21.4%
  second half  n=1444  mean 0.070  above floor 13.2%
  change -0.089

Input health
------------
  cycles with a context gap  350/3832 (9.1%)
    news unavailable                         349
    CFTC positioning unavailable             1

  bias distribution (2888 signals)
    BULLISH      222  7.7%
    BEARISH       65  2.3%
    NEUTRAL     2601  90.1%
  cycles that produced no signal: 230

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
