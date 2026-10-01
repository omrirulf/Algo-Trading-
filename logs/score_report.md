SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        1192
entries                   1192
  produced a signal       948
  directional             97  (NEUTRAL: 851)
  scored                  87
  unscored, pending         10  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.30 (n=87)

conviction        n   hit rate      mean    median
0.30-0.45        50      24.0%     -1.0%     -0.5%
0.45-0.60        33      57.6%     +0.6%     +0.8%
0.60-0.75         4      75.0%     -0.7%     +0.4%  (thin)

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=87    hit 39.1%  mean -0.4%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news             87         -0.13
technical        87         -0.15
fundamental      87         +0.09
analyst          51         +0.05
insider          44         -0.33

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction    772      87         -0.07     39.1%
equal weights       772     750         -0.09     45.1%
learned blend       381     359         +0.03     48.7%
  learned composites from fitted weights: 53; from the equal-weight fallback: 328

  model and blend called opposite directions  n=7     model hit 28.6%  blend hit 71.4%

  the learned blend ranks outcomes better than the model but was right only 49% of the time; not a direction to trade on

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=298   mean conviction 0.157
  at least one dissents  n=650   mean conviction 0.218
  gap -0.061 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.25 (n=948) (negative is correct)
    ...but spread vs loudest single score: +0.82 (n=948) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.05 (n=948) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=474   mean 0.286  above floor 34.0%
  second half  n=474   mean 0.111  above floor 13.5%
  change -0.175

Input health
------------
  cycles with a context gap  30/1192 (2.5%)
    news unavailable                         30

  bias distribution (948 signals)
    BULLISH       51  5.4%
    BEARISH       46  4.9%
    NEUTRAL      851  89.8%
  cycles that produced no signal: 73

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
