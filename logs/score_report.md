SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        4312
entries                   4312
  produced a signal       3255
  directional             317  (NEUTRAL: 2938)
  scored                  300
  unscored, pending         17  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.08 (n=300)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        77      32.5%     -1.1%     -0.5%
0.45-0.60       131      49.6%     -0.6%     -0.1%
0.60-0.75        74      54.1%     +0.1%     +0.6%
0.75-1.00        17      23.5%     -1.0%     -1.1%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=299   hit 44.8%  mean -0.6%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.2% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            300         -0.11
technical       300         -0.01
fundamental     300         -0.26
analyst         260         -0.05
insider         257         -0.14

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   3058     299         -0.03     44.8%
equal weights      3058    2821         -0.02     47.7%
learned blend      2667    2514         +0.01     50.8%
  learned composites from fitted weights: 2339; from the equal-weight fallback: 328

  model and blend called opposite directions  n=128   model hit 40.6%  blend hit 59.4%

  READY TO LEAVE SHADOW: the learned blend carries more information than the model's conviction and than equal weights, and was right more often than not

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=1356  mean conviction 0.064
  at least one dissents  n=1899  mean conviction 0.142
  gap -0.078 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.28 (n=3255) (negative is correct)
    ...but spread vs loudest single score: +0.85 (n=3255) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.14 (n=3255) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=1627  mean 0.150  above floor 20.8%
  second half  n=1628  mean 0.069  above floor 12.7%
  change -0.081

Input health
------------
  cycles with a context gap  381/4312 (8.8%)
    news unavailable                         360
    fund equity_holdings unavailable         20
    fund bond_holdings unavailable           20
    fund bond_ratings unavailable            20
    fund fund_operations unavailable         20
    fund fund_overview unavailable           20

  bias distribution (3255 signals)
    BULLISH      241  7.4%
    BEARISH       76  2.3%
    NEUTRAL     2938  90.3%
  cycles that produced no signal: 266

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
