SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        1912
entries                   1912
  produced a signal       1443
  directional             147  (NEUTRAL: 1296)
  scored                  134
  unscored, pending         13  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.29 (n=134)

conviction        n   hit rate      mean    median
0.30-0.45        59      28.8%     -0.9%     -0.5%
0.45-0.60        56      55.4%     +0.2%     +0.6%
0.60-0.75        18      66.7%     +0.9%     +0.8%
0.75-1.00         1     100.0%     +0.5%     +0.5%  (thin)

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=134   hit 45.5%  mean -0.2%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            134         -0.04
technical       134         -0.12
fundamental     134         -0.03
analyst          95         +0.04
insider          91         -0.14

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   1305     134         -0.02     45.5%
equal weights      1305    1244         -0.03     47.2%
learned blend       914     874         -0.06     47.4%
  learned composites from fitted weights: 586; from the equal-weight fallback: 328

  model and blend called opposite directions  n=24    model hit 45.8%  blend hit 54.2%

  the model's conviction still carries more information than the learned blend; keep it in shadow

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=501   mean conviction 0.112
  at least one dissents  n=942   mean conviction 0.183
  gap -0.071 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.24 (n=1443) (negative is correct)
    ...but spread vs loudest single score: +0.82 (n=1443) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.12 (n=1443) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=721   mean 0.251  above floor 29.1%
  second half  n=722   mean 0.066  above floor 13.6%
  change -0.184

Input health
------------
  cycles with a context gap  96/1912 (5.0%)
    news unavailable                         96

  bias distribution (1443 signals)
    BULLISH       97  6.7%
    BEARISH       50  3.5%
    NEUTRAL     1296  89.8%
  cycles that produced no signal: 129

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
