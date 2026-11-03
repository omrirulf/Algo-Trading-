SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        3032
entries                   3032
  produced a signal       2334
  directional             233  (NEUTRAL: 2101)
  scored                  219
  unscored, pending         14  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.12 (n=219)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        68      33.8%     -0.8%     -0.4%
0.45-0.60        94      53.2%     -0.3%     +0.1%
0.60-0.75        46      58.7%     +0.2%     +0.8%
0.75-1.00        10      30.0%     -0.9%     -1.2%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=218   hit 47.2%  mean -0.4%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.4% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            219         -0.09
technical       219         -0.07
fundamental     219         -0.19
analyst         179         -0.09
insider         176         -0.09

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   2152     218         -0.02     47.2%
equal weights      2152    2016         +0.00     49.5%
learned blend      1761    1673         +0.00     50.3%
  learned composites from fitted weights: 1433; from the equal-weight fallback: 328

  model and blend called opposite directions  n=72    model hit 44.4%  blend hit 55.6%

  READY TO LEAVE SHADOW: the learned blend carries more information than the model's conviction and than equal weights, and was right more often than not

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=955   mean conviction 0.079
  at least one dissents  n=1379  mean conviction 0.159
  gap -0.080 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.27 (n=2334) (negative is correct)
    ...but spread vs loudest single score: +0.83 (n=2334) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.15 (n=2334) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=1167  mean 0.177  above floor 22.6%
  second half  n=1167  mean 0.076  above floor 14.9%
  change -0.101

Input health
------------
  cycles with a context gap  287/3032 (9.5%)
    news unavailable                         286
    CFTC positioning unavailable             1

  bias distribution (2334 signals)
    BULLISH      172  7.4%
    BEARISH       61  2.6%
    NEUTRAL     2101  90.0%
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
