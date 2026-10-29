SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        2792
entries                   2792
  produced a signal       2152
  directional             219  (NEUTRAL: 1933)
  scored                  196
  unscored, pending         23  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.13 (n=196)

conviction        n   hit rate      mean    median
0.00-0.30         1       0.0%     -0.7%     -0.7%  (thin)
0.30-0.45        63      30.2%     -0.8%     -0.5%
0.45-0.60        84      53.6%     +0.0%     +0.1%
0.60-0.75        41      53.7%     +0.2%     +0.3%
0.75-1.00         7      28.6%     +0.1%     -1.1%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=195   hit 45.1%  mean -0.2%
  filtered (< floor)   n=1     hit 0.0%  mean -0.7%
  edge +0.5% — the floor is keeping the better signals
  too few to conclude anything (n=1, want 20+)

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            196         -0.10
technical       196         -0.13
fundamental     196         -0.14
analyst         157         -0.09
insider         153         -0.16

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   1957     195         -0.03     45.1%
equal weights      1957    1833         +0.01     49.4%
learned blend      1566    1484         -0.02     49.9%
  learned composites from fitted weights: 1238; from the equal-weight fallback: 328

  model and blend called opposite directions  n=59    model hit 42.4%  blend hit 57.6%

  the learned blend beats the model's conviction but not equal weights; the fitted weights are not yet earning their keep

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=869   mean conviction 0.085
  at least one dissents  n=1283  mean conviction 0.163
  gap -0.079 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.27 (n=2152) (negative is correct)
    ...but spread vs loudest single score: +0.83 (n=2152) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.15 (n=2152) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=1076  mean 0.187  above floor 23.6%
  second half  n=1076  mean 0.076  above floor 14.8%
  change -0.111

Input health
------------
  cycles with a context gap  195/2792 (7.0%)
    news unavailable                         194
    CFTC positioning unavailable             1

  bias distribution (2152 signals)
    BULLISH      159  7.4%
    BEARISH       60  2.8%
    NEUTRAL     1933  89.8%
  cycles that produced no signal: 151

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
