SIGNAL JOURNAL SCORING
----------------------
horizon 3 session(s) | entry rule 'auto' | conviction floor 0.30

Coverage
--------
journal lines read        552
entries                   552
  produced a signal       536
  directional             71  (NEUTRAL: 465)
  scored                  48
  unscored, pending         23  (too recent — no outcome yet)

Does conviction predict the outcome?
------------------------------------
rank correlation, conviction vs signed return: +0.22 (n=48)

conviction        n   hit rate      mean    median
0.30-0.45        35       8.6%     -1.2%     -0.7%
0.45-0.60        13      46.2%     +0.1%     -0.7%

Floor at 0.30 — did it filter the right signals?
  acted on (>= floor)  n=48    hit 18.8%  mean -0.9%
  filtered (< floor)   n=0     hit n/a  mean n/a

Which dimension actually carried information?
---------------------------------------------
Each score against the ticker's raw forward return.

dimension         n     rank corr
news             48         -0.25
technical        48         -0.20
fundamental      48         +0.04
analyst          17+0.08 — too few
insider          11-0.01 — too few

Does the learned blend carry information?
-----------------------------------------
The five scores blended into one, against the ticker's raw forward return.
Every line with a signal and a score counts here, NEUTRAL included: the
blend takes a side on those too. 'learned blend' is the composite as it
was journalled, with whatever weights that cycle had -- the walk-forward
record, never a refit that has seen the return it is judged on.

policy                n  called     rank corr  hit rate
model conviction    261      48         -0.13     18.8%
equal weights       261     261         -0.06     46.4%
learned blend        69      68         +0.16     50.0%
  learned composites from fitted weights: 0; from the equal-weight fallback: 69

  the learned blend ranks outcomes better than the model but was right only 50% of the time; not a direction to trade on

Does conviction fall when the dimensions disagree?
--------------------------------------------------
The prompt requires it. This needs no price data, so it is answerable
from the first cycle onward.

  all dimensions agree   n=148   mean conviction 0.271
  at least one dissents  n=388   mean conviction 0.289
  gap -0.018 — conviction is HIGHER when dimensions conflict — the opposite of the instruction
  rank corr, score spread vs conviction: +0.33 (n=536) (negative is correct)
    ...but spread vs loudest single score: +0.79 (n=536) — the two are nearly the same series,
    so the raw number above mostly asks 'is something shouting?', and charges
    the model for being confident about a strong signal -- which the prompt asks for.
  holding magnitude fixed:               -0.06 (n=536) <- THE FINER MEASURE
  The instruction is directional ('bullish news on a technically broken,
  richly valued name'), so what counts is conviction falling when the
  dimensions CONFLICT, not when one of them is merely large.

Is conviction drifting?
-----------------------
A model that creeps toward always-confident makes the floor a no-op.

  first half   n=268   mean 0.293  above floor 39.9%
  second half  n=268   mean 0.275  above floor 24.3%
  change -0.018

Input health
------------
  cycles with a context gap  0/552 (0.0%)

  bias distribution (536 signals)
    BULLISH       29  5.4%
    BEARISH       42  7.8%
    NEUTRAL      465  86.8%
  cycles that produced no signal: 3

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
