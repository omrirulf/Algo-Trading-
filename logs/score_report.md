SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        1432
entries                   1432
  produced a signal       1124
  directional             115  (NEUTRAL: 1009)
  scored                  97
  unscored, pending         18  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.38 (n=97)

conviction        n   hit rate      mean    median
0.30-0.45        50      24.0%     -1.0%     -0.5%
0.45-0.60        38      60.5%     +0.6%     +0.8%
0.60-0.75         9      77.8%     +1.9%     +0.8%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=97    hit 43.3%  mean -0.1%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news             97         -0.01
technical        97         -0.14
fundamental      97         +0.10
analyst          61         +0.08
insider          54         -0.19

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction    948      97         -0.03     43.3%
equal weights       948     911         -0.03     46.5%
learned blend       557     526         -0.16     43.7%
  learned composites from fitted weights: 229; from the equal-weight fallback: 328

  model and blend called opposite directions  n=12    model hit 50.0%  blend hit 50.0%

  the model's conviction still carries more information than the learned blend; keep it in shadow

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=365   mean conviction 0.135
  at least one dissents  n=759   mean conviction 0.200
  gap -0.065 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.25 (n=1124) (negative is correct)
    ...but spread vs loudest single score: +0.81 (n=1124) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               +0.09 (n=1124) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=562   mean 0.283  above floor 31.7%
  second half  n=562   mean 0.075  above floor 13.5%
  change -0.208

Input health
------------
  cycles with a context gap  57/1432 (4.0%)
    news unavailable                         57

  bias distribution (1124 signals)
    BULLISH       68  6.0%
    BEARISH       47  4.2%
    NEUTRAL     1009  89.8%
  cycles that produced no signal: 78

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
