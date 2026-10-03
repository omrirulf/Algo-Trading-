SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        1272
entries                   1272
  produced a signal       1009
  directional             103  (NEUTRAL: 906)
  scored                  90
  unscored, pending         13  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.28 (n=90)

conviction        n   hit rate      mean    median
0.30-0.45        50      24.0%     -1.0%     -0.5%
0.45-0.60        34      58.8%     +0.6%     +0.8%
0.60-0.75         6      66.7%     -0.8%     +0.3%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=90    hit 40.0%  mean -0.3%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news             90         -0.13
technical        90         -0.11
fundamental      90         +0.10
analyst          54         -0.01
insider          47         -0.37

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction    829      90         -0.07     40.0%
equal weights       829     802         -0.09     44.9%
learned blend       438     413         +0.01     47.9%
  learned composites from fitted weights: 110; from the equal-weight fallback: 328

  model and blend called opposite directions  n=9     model hit 33.3%  blend hit 66.7%

  the learned blend ranks outcomes better than the model but was right only 48% of the time; not a direction to trade on

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=324   mean conviction 0.148
  at least one dissents  n=685   mean conviction 0.211
  gap -0.063 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.25 (n=1009) (negative is correct)
    ...but spread vs loudest single score: +0.81 (n=1009) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.06 (n=1009) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=504   mean 0.284  above floor 32.1%
  second half  n=505   mean 0.097  above floor 14.3%
  change -0.187

Input health
------------
  cycles with a context gap  30/1272 (2.4%)
    news unavailable                         30

  bias distribution (1009 signals)
    BULLISH       56  5.6%
    BEARISH       47  4.7%
    NEUTRAL      906  89.8%
  cycles that produced no signal: 74

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
