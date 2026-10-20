SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        2232
entries                   2232
  produced a signal       1689
  directional             173  (NEUTRAL: 1516)
  scored                  155
  unscored, pending         18  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.25 (n=155)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        60      28.3%     -0.9%     -0.5%
0.45-0.60        63      58.7%     +0.3%     +0.5%
0.60-0.75        29      65.5%     +0.7%     +0.8%
0.75-1.00         2       0.0%     -0.7%     -0.7%  (thin)

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=154   hit 47.4%  mean -0.1%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.6% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            155         -0.04
technical       155         -0.10
fundamental     155         -0.09
analyst         116         -0.01
insider         112         -0.15

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   1506     154         -0.01     47.4%
equal weights      1506    1431         -0.03     47.7%
learned blend      1115    1066         -0.04     48.2%
  learned composites from fitted weights: 787; from the equal-weight fallback: 328

  model and blend called opposite directions  n=28    model hit 46.4%  blend hit 53.6%

  the model's conviction still carries more information than the learned blend; keep it in shadow

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=632   mean conviction 0.101
  at least one dissents  n=1057  mean conviction 0.173
  gap -0.072 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.26 (n=1689) (negative is correct)
    ...but spread vs loudest single score: +0.83 (n=1689) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.14 (n=1689) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=844   mean 0.219  above floor 25.8%
  second half  n=845   mean 0.074  above floor 14.9%
  change -0.145

Input health
------------
  cycles with a context gap  165/2232 (7.4%)
    news unavailable                         165

  bias distribution (1689 signals)
    BULLISH      119  7.0%
    BEARISH       54  3.2%
    NEUTRAL     1516  89.8%
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
