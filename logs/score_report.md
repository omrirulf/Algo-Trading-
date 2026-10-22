SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        2392
entries                   2392
  produced a signal       1824
  directional             185  (NEUTRAL: 1639)
  scored                  168
  unscored, pending         17  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.20 (n=168)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        62      29.0%     -0.9%     -0.5%
0.45-0.60        71      59.2%     +0.2%     +0.4%
0.60-0.75        31      61.3%     +0.5%     +0.8%
0.75-1.00         3       0.0%     -1.0%     -1.1%  (thin)

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=167   hit 47.3%  mean -0.1%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.6% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            168         -0.09
technical       168         -0.13
fundamental     168         -0.12
analyst         129         -0.02
insider         125         -0.14

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   1624     167         -0.02     47.3%
equal weights      1624    1539         -0.01     48.5%
learned blend      1233    1177         -0.03     48.1%
  learned composites from fitted weights: 905; from the equal-weight fallback: 328

  model and blend called opposite directions  n=39    model hit 46.2%  blend hit 53.8%

  the model's conviction still carries more information than the learned blend; keep it in shadow

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=701   mean conviction 0.093
  at least one dissents  n=1123  mean conviction 0.171
  gap -0.078 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.28 (n=1824) (negative is correct)
    ...but spread vs loudest single score: +0.83 (n=1824) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.15 (n=1824) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=912   mean 0.206  above floor 24.7%
  second half  n=912   mean 0.076  above floor 15.4%
  change -0.130

Input health
------------
  cycles with a context gap  177/2392 (7.4%)
    news unavailable                         177

  bias distribution (1824 signals)
    BULLISH      131  7.2%
    BEARISH       54  3.0%
    NEUTRAL     1639  89.9%
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
