SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        2072
entries                   2072
  produced a signal       1567
  directional             161  (NEUTRAL: 1406)
  scored                  141
  unscored, pending         20  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.22 (n=141)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        59      28.8%     -0.9%     -0.5%
0.45-0.60        57      56.1%     +0.3%     +0.7%
0.60-0.75        23      60.9%     +0.4%     +0.8%
0.75-1.00         1       0.0%     -1.1%     -1.1%  (thin)

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=140   hit 45.0%  mean -0.2%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.5% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            141         -0.08
technical       141         -0.11
fundamental     141         -0.06
analyst         102         +0.03
insider          98         -0.15

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   1380     140         -0.02     45.0%
equal weights      1380    1315         -0.04     47.2%
learned blend       989     947         -0.05     47.7%
  learned composites from fitted weights: 661; from the equal-weight fallback: 328

  model and blend called opposite directions  n=25    model hit 44.0%  blend hit 56.0%

  the model's conviction still carries more information than the learned blend; keep it in shadow

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=571   mean conviction 0.106
  at least one dissents  n=996   mean conviction 0.179
  gap -0.073 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.26 (n=1567) (negative is correct)
    ...but spread vs loudest single score: +0.82 (n=1567) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.13 (n=1567) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=783   mean 0.233  above floor 27.3%
  second half  n=784   mean 0.071  above floor 14.5%
  change -0.162

Input health
------------
  cycles with a context gap  152/2072 (7.3%)
    news unavailable                         152

  bias distribution (1567 signals)
    BULLISH      108  6.9%
    BEARISH       53  3.4%
    NEUTRAL     1406  89.7%
  cycles that produced no signal: 138

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
