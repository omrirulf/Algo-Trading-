SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        1592
entries                   1592
  produced a signal       1242
  directional             129  (NEUTRAL: 1113)
  scored                  113
  unscored, pending         16  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.28 (n=113)

conviction        n   hit rate      mean    median
0.30-0.45        55      25.5%     -0.9%     -0.5%
0.45-0.60        47      53.2%     +0.1%     +0.5%
0.60-0.75        11      63.6%     +1.4%     +0.8%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=113   hit 40.7%  mean -0.3%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news            113         -0.08
technical       113         -0.17
fundamental     113         -0.01
analyst          76         +0.02
insider          70         -0.28

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction   1067     113         -0.04     40.7%
equal weights      1067    1022         -0.07     45.1%
learned blend       676     642         -0.07     47.7%
  learned composites from fitted weights: 348; from the equal-weight fallback: 328

  model and blend called opposite directions  n=23    model hit 34.8%  blend hit 65.2%

  the model's conviction still carries more information than the learned blend; keep it in shadow

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=409   mean conviction 0.127
  at least one dissents  n=833   mean conviction 0.193
  gap -0.066 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.25 (n=1242) (negative is correct)
    ...but spread vs loudest single score: +0.82 (n=1242) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.09 (n=1242) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=621   mean 0.282  above floor 32.0%
  second half  n=621   mean 0.060  above floor 12.4%
  change -0.223

Input health
------------
  cycles with a context gap  77/1592 (4.8%)
    news unavailable                         77

  bias distribution (1242 signals)
    BULLISH       79  6.4%
    BEARISH       50  4.0%
    NEUTRAL     1113  89.6%
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
