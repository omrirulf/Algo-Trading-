SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        1512
entries                   1512
  produced a signal       1182
  directional             122  (NEUTRAL: 1060)
  scored                  103
  unscored, pending         19  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.33 (n=103)

conviction        n   hit rate      mean    median
0.30-0.45        52      26.9%     -0.9%     -0.5%
0.45-0.60        42      59.5%     +0.3%     +0.7%
0.60-0.75         9      77.8%     +1.9%     +0.8%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=103   hit 44.7%  mean -0.2%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            103         -0.02
technical       103         -0.16
fundamental     103         +0.05
analyst          66         +0.07
insider          60         -0.15

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   1009     103         -0.03     44.7%
equal weights      1009     968         -0.04     46.4%
learned blend       618     585         -0.12     45.3%
  learned composites from fitted weights: 290; from the equal-weight fallback: 328

  model and blend called opposite directions  n=15    model hit 53.3%  blend hit 46.7%

  the model's conviction still carries more information than the learned blend; keep it in shadow

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=383   mean conviction 0.130
  at least one dissents  n=799   mean conviction 0.197
  gap -0.067 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.25 (n=1182) (negative is correct)
    ...but spread vs loudest single score: +0.82 (n=1182) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.09 (n=1182) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=591   mean 0.283  above floor 31.5%
  second half  n=591   mean 0.067  above floor 13.2%
  change -0.216

Input health
------------
  cycles with a context gap  65/1512 (4.3%)
    news unavailable                         65

  bias distribution (1182 signals)
    BULLISH       74  6.3%
    BEARISH       48  4.1%
    NEUTRAL     1060  89.7%
  cycles that produced no signal: 80

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
