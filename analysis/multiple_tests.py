"""The checkpoint arithmetic of pre-registration sections 13.5 and 13.6.

Pure functions, standard library only:

* ``p_two_sided``: a Newey-West t read against the normal distribution.
* ``bh_adjust``: Benjamini and Hochberg (1995). With the m p-values in
  order p(1) <= ... <= p(m), the adjusted p-value of p(i) is the smallest
  of m x p(j) / j over j >= i, capped at 1.
* ``series_stats`` and ``deflated_sharpe``: Bailey and Lopez de Prado
  (2014). SR = mean / standard deviation of the daily series, T its length,
  skewness and kurtosis (3 for a normal distribution);
  SR0 = sqrt(V) x ((1 - g) Phi^-1(1 - 1/N) + g Phi^-1(1 - 1/(N e))),
  g = 0.5772 (Euler's constant), V = 1/T (Lo 2002: the variance of a
  Sharpe ratio estimated from T returns when the true one is zero);
  DSR = Phi((SR - SR0) sqrt(T - 1) / sqrt(1 - skew SR + (kurt - 1)/4 SR^2)).
* ``graveyard_n``: N, the number of trials in ``docs/research/graveyard.md``.

Nothing here decides anything: the numbers are read at the checkpoints and
can change no rule (section 13).
"""

from __future__ import annotations

import math
import re
import statistics
from pathlib import Path
from statistics import NormalDist
from typing import Optional, Sequence

#: A test passes Benjamini-Hochberg when its adjusted p-value is at most this.
BH_LEVEL = 0.05
#: A result survives the number of ideas tried when its DSR is above this.
DSR_LEVEL = 0.95
EULER_GAMMA = 0.5772156649015329

GRAVEYARD = Path(__file__).resolve().parent.parent / "docs" / "research" / "graveyard.md"

_NORMAL = NormalDist()


def p_two_sided(t: Optional[float]) -> Optional[float]:
    """Two-sided p-value of ``t`` under the standard normal; None without a t."""
    if t is None or not math.isfinite(t):
        return None
    return 2.0 * (1.0 - _NORMAL.cdf(abs(t)))


def bh_adjust(p_values: Sequence[float]) -> list[float]:
    """Benjamini-Hochberg adjusted p-values, in the order given."""
    m = len(p_values)
    if m == 0:
        return []
    order = sorted(range(m), key=lambda i: p_values[i])
    adjusted = [0.0] * m
    running = 1.0
    for rank in range(m, 0, -1):
        i = order[rank - 1]
        running = min(running, m * p_values[i] / rank)
        adjusted[i] = min(1.0, running)
    return adjusted


def series_stats(series: Sequence[float]) -> Optional[dict[str, float]]:
    """Mean, SR (per period), T, skewness and kurtosis of a daily series; None under 3 values or no spread."""
    xs = [float(x) for x in series]
    n = len(xs)
    if n < 3:
        return None
    mean = statistics.fmean(xs)
    sd = statistics.stdev(xs)
    if sd <= 0:
        return None
    m2 = sum((x - mean) ** 2 for x in xs) / n
    m3 = sum((x - mean) ** 3 for x in xs) / n
    m4 = sum((x - mean) ** 4 for x in xs) / n
    return {"mean": mean, "sd": sd, "sr": mean / sd, "t_days": n,
            "skew": m3 / m2 ** 1.5 if m2 > 0 else 0.0, "kurt": m4 / m2 ** 2 if m2 > 0 else 3.0}


def expected_max_sr(n_trials: int, t_days: int) -> float:
    """SR0: the Sharpe ratio the best of N ideas with no edge would show, on T days."""
    if n_trials < 2:
        return 0.0
    v = 1.0 / t_days
    z = _NORMAL.inv_cdf
    return math.sqrt(v) * ((1 - EULER_GAMMA) * z(1 - 1 / n_trials)
                           + EULER_GAMMA * z(1 - 1 / (n_trials * math.e)))


def deflated_sharpe(stats: dict[str, float], n_trials: int) -> Optional[float]:
    """The DSR of one series' stats (``series_stats``) against N trials; None if undefined."""
    sr, t, skew, kurt = stats["sr"], int(stats["t_days"]), stats["skew"], stats["kurt"]
    if t < 3:
        return None
    denominator = 1.0 - skew * sr + (kurt - 1.0) / 4.0 * sr * sr
    if denominator <= 0:
        return None
    sr0 = expected_max_sr(n_trials, t)
    return _NORMAL.cdf((sr - sr0) * math.sqrt(t - 1) / math.sqrt(denominator))


def graveyard_n(path: Path = GRAVEYARD) -> int:
    """The number of trials in the graveyard: its numbered table rows."""
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines()
               if re.match(r"^\| \d+ \|", line))


def checkpoint_table(tests: Sequence[dict], n_trials: int) -> list[dict]:
    """Every test of the family with its p-value, BH-adjusted p-value and DSR.

    Each test is ``{"name", "t", "stats"}``; a test with no t is listed as
    having no data and left out of the adjustment (section 13.5).
    """
    with_p = [(test, p_two_sided(test.get("t"))) for test in tests]
    counted = [(test, p) for test, p in with_p if p is not None]
    adjusted = bh_adjust([p for _, p in counted])
    by_name = {test["name"]: a for (test, _), a in zip(counted, adjusted)}
    out = []
    for test, p in with_p:
        stats = test.get("stats")
        dsr = deflated_sharpe(stats, n_trials) if stats else None
        q = by_name.get(test["name"])
        out.append({"name": test["name"], "t": test.get("t"), "p": p, "p_bh": q,
                    "passes_bh": q is not None and q <= BH_LEVEL,
                    "dsr": dsr, "survives_dsr": dsr is not None and dsr > DSR_LEVEL,
                    "no_data": p is None})
    return out


__all__ = ["BH_LEVEL", "DSR_LEVEL", "bh_adjust", "checkpoint_table", "deflated_sharpe", "expected_max_sr",
           "graveyard_n", "p_two_sided", "series_stats"]
