SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        1672
entries                   1672
  produced a signal       1305
  directional             134  (NEUTRAL: 1171)
  scored                  115
  unscored, pending         19  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.26 (n=115)

conviction        n   hit rate      mean    median
0.30-0.45        55      27.3%     -0.9%     -0.5%
0.45-0.60        47      53.2%     +0.2%     +0.5%
0.60-0.75        13      61.5%     +1.0%     +0.8%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=115   hit 41.7%  mean -0.2%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            115         -0.08
technical       115         -0.16
fundamental     115         -0.00
analyst          78         +0.03
insider          72         -0.22

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   1124     115         -0.03     41.7%
equal weights      1124    1076         -0.06     45.6%
learned blend       733     697         -0.09     47.1%
  learned composites from fitted weights: 405; from the equal-weight fallback: 328

  model and blend called opposite directions  n=23    model hit 43.5%  blend hit 56.5%

  the model's conviction still carries more information than the learned blend; keep it in shadow

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=436   mean conviction 0.126
  at least one dissents  n=869   mean conviction 0.188
  gap -0.063 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.24 (n=1305) (negative is correct)
    ...but spread vs loudest single score: +0.81 (n=1305) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.10 (n=1305) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=652   mean 0.270  above floor 30.7%
  second half  n=653   mean 0.065  above floor 13.5%
  change -0.204

Input health
------------
  cycles with a context gap  83/1672 (5.0%)
    news unavailable                         83

  bias distribution (1305 signals)
    BULLISH       84  6.4%
    BEARISH       50  3.8%
    NEUTRAL     1171  89.7%
  cycles that produced no signal: 81

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
