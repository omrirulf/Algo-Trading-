"""A learned blend of the five dimension scores into one composite.

The model reports a score in [-1, 1] for each of news, technicals,
fundamentals, the analyst view and insider activity. This module turns those
five numbers into one, with weights learned from what the market did next,
and it is pure: no file is read or written here, no order can be placed, and
nothing in it knows about the engine. The trainer in ``learn/`` feeds it
observations and stores what it returns; the heartbeat applies what was
stored. Both sides share this one definition so they cannot drift.

Four decisions decide what the numbers mean.

**Weights are normalised to unit absolute sum.** A weight may be negative --
a dimension can be contrarian -- so the composite of five full scores lies in
[-1, 1] by construction, and a weight reads as "this share of the blend".

**A missing dimension contributes nothing.** The prompt leaves a score null
when its data was unavailable. Here that is a zero feature: it adds nothing
to the sum, and the composite's magnitude is capped by the share of weight
that actually had a score. A signal built on technicals alone cannot look as
confident as a full one, and the regression sees exactly the same zero, so
the weights it learns already account for it.

**Weights are learned per level and shrunk toward the level above.** The
hierarchy is ticker, then instrument kind, then global. Kind is the unit
because it decides which prompt scored the dimensions, so an ETF's
``insider_score`` (CFTC positioning) and a company's (Form 4 filings) are not
pooled as if they meant the same thing. Each level's own fit is blended with
its parent's final weights in the ratio ``n / (n + prior_strength)``, where
``n`` is the level's decayed observation count. A ticker with five scored
signals is nearly its kind; with two hundred it is mostly itself; a level
with no data at all is exactly its parent, and the global parent with no
data is equal weights. This is what makes per-ticker weights safe before
they are meaningful.

**Old observations count less.** Every observation carries a weight of
``0.5 ** (age / half_life)``, with age in sessions, so the fit tracks the
recent regime without forgetting a quarter in a bad week. The decayed count
is also the ``n`` above, so a level that has not seen data lately drifts
back toward its parent rather than trusting a stale fit.

The regression itself is a ridge least squares of the target on the five
scores plus an intercept, solved from the normal equations in pure Python.
The intercept absorbs whatever the market did on average over the window so
the weights measure the dimensions' incremental read; it is not part of the
composite, which must be symmetric. The ridge is one pseudo-observation
toward zero, there for numerical safety, not for shrinkage -- shrinkage
happens toward the parent, above, where it means something.
"""

from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass
from datetime import date
from typing import Any, Iterable, Mapping, Optional

from analysis.reader import SCORE_FIELDS
from config.instruments import kind_for

#: Bumped when the stored shape changes incompatibly. ``from_dict`` refuses
#: anything else rather than misreading it.
ARTIFACT_VERSION = 1

GLOBAL_KEY = "global"

#: The blend with nothing learned: a plain average of whatever scores exist.
EQUAL_WEIGHTS: dict[str, float] = {name: 1.0 / len(SCORE_FIELDS) for name in SCORE_FIELDS}

#: How the composite is labelled when it was not read from any fitted level.
EQUAL_KEY = "equal"

#: Sessions over which an observation's weight halves.
DEFAULT_HALF_LIFE = 60.0

#: Pseudo-observations a level's parent is worth. Mirrors the scorer's
#: ``MIN_SAMPLE``: below about twenty observations a level is mostly its parent.
DEFAULT_PRIOR_STRENGTH = 20.0

#: Pseudo-observations pulling each raw coefficient toward zero. Keeps the
#: normal equations solvable when a dimension never varied; nothing more.
DEFAULT_RIDGE = 1.0

SESSIONS_PER_YEAR = 252

#: Journalled composites a calibration needs before it is stored at all.
#: Mirrors the scorer's ``MIN_SAMPLE``: below it, nothing is stored for a
#: live mode to read.
MIN_CALIBRATION = 20


# --------------------------------------------------------------------------- #
# Applying weights
# --------------------------------------------------------------------------- #


def normalise(weights: Mapping[str, float]) -> dict[str, float]:
    """Scale weights to unit absolute sum; equal weights when there is nothing to scale."""
    total = sum(abs(float(weights.get(name, 0.0))) for name in SCORE_FIELDS)
    if not total > 0.0 or not math.isfinite(total):
        return dict(EQUAL_WEIGHTS)
    return {name: float(weights.get(name, 0.0)) / total for name in SCORE_FIELDS}


@dataclass(frozen=True)
class Composite:
    """One blended read, with enough beside it to see how it was built."""

    value: float
    #: Share of absolute weight whose dimension had a score, in [0, 1].
    coverage: float
    #: Dimensions that contributed, in report order.
    used: tuple[str, ...]
    #: The normalised weights that were applied, all five.
    weights: dict[str, float]

    def as_dict(self) -> dict[str, Any]:
        return {
            "value": round(self.value, 6),
            "coverage": round(self.coverage, 6),
            "used": list(self.used),
            "weights": {name: round(w, 6) for name, w in self.weights.items()},
        }


def composite(
    scores: Mapping[str, Optional[float]], weights: Mapping[str, float] = EQUAL_WEIGHTS
) -> Optional[Composite]:
    """Blend the scores that exist; ``None`` when none do."""
    applied = normalise(weights)
    used = tuple(name for name in SCORE_FIELDS if _finite(scores.get(name)))
    if not used:
        return None
    value = sum(applied[name] * float(scores[name]) for name in used)  # type: ignore[arg-type]
    coverage = sum(abs(applied[name]) for name in used)
    return Composite(
        value=max(-1.0, min(1.0, value)),
        coverage=min(1.0, coverage),
        used=used,
        weights=applied,
    )


def chain_for(ticker: str) -> tuple[str, ...]:
    """The levels a ticker reads from, most specific first."""
    symbol = ticker.strip().upper()
    return (f"ticker:{symbol}", f"kind:{kind_for(symbol).value}", GLOBAL_KEY)


# --------------------------------------------------------------------------- #
# Calibration: composite magnitude -> how often that direction was right
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Calibration:
    """A monotone map from the composite's magnitude to a hit probability.

    Fitted by isotonic regression on the composites the journal recorded and
    the returns that followed, so a conviction of 0.6 read off it means the
    direction was right six times in ten at that strength -- the same thing
    the engine's floor has always assumed conviction meant.
    """

    #: ``(magnitude, probability)`` knots, ascending in magnitude.
    knots: tuple[tuple[float, float], ...]
    #: Observations behind the fit.
    n: int

    def probability(self, magnitude: float) -> float:
        """Linear between knots, flat beyond the ends."""
        magnitude = abs(float(magnitude))
        if magnitude <= self.knots[0][0]:
            return self.knots[0][1]
        for (left_m, left_p), (right_m, right_p) in zip(self.knots, self.knots[1:]):
            if magnitude <= right_m:
                span = right_m - left_m
                share = (magnitude - left_m) / span if span > 0 else 1.0
                return left_p + share * (right_p - left_p)
        return self.knots[-1][1]

    def as_dict(self) -> dict[str, Any]:
        return {"knots": [[m, p] for m, p in self.knots], "n": self.n}

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "Calibration":
        knots = tuple((float(m), float(p)) for m, p in payload["knots"])
        if not knots:
            raise ValueError("a calibration needs at least one knot")
        return cls(knots=knots, n=int(payload.get("n", 0)))


def fit_calibration(
    observations: Iterable[tuple[float, bool, float]],
    *,
    minimum: int = MIN_CALIBRATION,
) -> Optional[Calibration]:
    """Isotonic regression of hit on composite magnitude.

    ``observations`` are ``(magnitude, hit, weight)``. Pool-adjacent-violators
    over the magnitudes in ascending order: any run where a stronger composite
    was right less often than a weaker one is pooled into one block, so the
    map can only rise. ``None`` below ``minimum`` observations -- a curve
    through a dozen points is a drawing, not a calibration.
    """
    # Points at one magnitude are one block from the start: isotonic
    # regression is over distinct magnitudes, and a block's probability is
    # the weighted hit rate of everything at or pooled into it.
    grouped: dict[float, list[float]] = {}
    count = 0
    for magnitude, hit, weight in observations:
        if not (_finite(magnitude) and _finite(weight)) or weight <= 0:
            continue
        count += 1
        block = grouped.setdefault(abs(float(magnitude)), [0.0, 0.0])
        block[0] += float(weight)
        block[1] += float(weight) * (1.0 if hit else 0.0)
    if count < minimum:
        return None
    # Each block: [weight, weighted hits, lowest magnitude, highest magnitude].
    blocks: list[list[float]] = []
    for magnitude in sorted(grouped):
        weight, hits = grouped[magnitude]
        blocks.append([weight, hits, magnitude, magnitude])
        while len(blocks) > 1 and blocks[-2][1] / blocks[-2][0] > blocks[-1][1] / blocks[-1][0]:
            last = blocks.pop()
            prev = blocks[-1]
            blocks[-1] = [prev[0] + last[0], prev[1] + last[1], prev[2], last[3]]
    # Flat across each block's range, linear across the gap to the next: the
    # step function the regression fitted, joined so a magnitude between two
    # blocks is not a cliff.
    knots: list[tuple[float, float]] = []
    for weight, hits, low, high in blocks:
        probability = hits / weight
        knots.append((low, probability))
        if high > low:
            knots.append((high, probability))
    return Calibration(knots=tuple(knots), n=count)


# --------------------------------------------------------------------------- #
# The stored artifact
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class LevelWeights:
    """One node of the hierarchy: its own fit, and what it resolved to."""

    key: str
    parent: Optional[str]
    #: Raw ridge coefficients, one per score field. Zero when nothing was fitted.
    fitted: dict[str, float]
    intercept: float
    #: Decayed observation count behind ``fitted``.
    n_effective: float
    #: Undecayed count of observations that went in.
    n_raw: int
    #: Final normalised weights after shrinking toward the parent. What is applied.
    weights: dict[str, float]
    #: ``n_effective / (n_effective + prior_strength)``: how much of ``weights``
    #: is this level's own fit rather than its parent's.
    own_share: float

    def as_dict(self) -> dict[str, Any]:
        return {
            "key": self.key,
            "parent": self.parent,
            "fitted": {name: self.fitted.get(name, 0.0) for name in SCORE_FIELDS},
            "intercept": self.intercept,
            "n_effective": self.n_effective,
            "n_raw": self.n_raw,
            "weights": {name: self.weights.get(name, 0.0) for name in SCORE_FIELDS},
            "own_share": self.own_share,
        }

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "LevelWeights":
        return cls(
            key=str(payload["key"]),
            parent=payload.get("parent"),
            fitted={name: float(payload["fitted"].get(name, 0.0)) for name in SCORE_FIELDS},
            intercept=float(payload.get("intercept", 0.0)),
            n_effective=float(payload.get("n_effective", 0.0)),
            n_raw=int(payload.get("n_raw", 0)),
            weights={name: float(payload["weights"].get(name, 0.0)) for name in SCORE_FIELDS},
            own_share=float(payload.get("own_share", 0.0)),
        )


@dataclass(frozen=True)
class WeightsArtifact:
    """Everything the applier needs, and everything a report needs to say where it came from."""

    #: The LLM whose scores were fitted. A different model's scores mean
    #: something else, so the trainer starts a fresh artifact for it.
    model: str
    #: Date the decay was measured from.
    fitted_on: date
    #: Last observation date that went in; ``None`` for an empty fit.
    trained_through: Optional[date]
    #: Sessions of forward return the target measured.
    horizon: int
    half_life: float
    prior_strength: float
    ridge: float
    levels: dict[str, LevelWeights]
    #: Magnitude-to-hit-rate map fitted on the composites the journal recorded.
    #: ``None`` until enough have a realised return behind them.
    calibration: Optional[Calibration] = None
    version: int = ARTIFACT_VERSION

    def to_dict(self) -> dict[str, Any]:
        return {
            "version": self.version,
            "model": self.model,
            "fitted_on": self.fitted_on.isoformat(),
            "trained_through": self.trained_through.isoformat() if self.trained_through else None,
            "horizon": self.horizon,
            "half_life": self.half_life,
            "prior_strength": self.prior_strength,
            "ridge": self.ridge,
            "levels": {key: level.as_dict() for key, level in sorted(self.levels.items())},
            "calibration": self.calibration.as_dict() if self.calibration else None,
        }

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "WeightsArtifact":
        version = payload.get("version")
        if version != ARTIFACT_VERSION:
            raise ValueError(f"weights artifact version {version!r}; this code reads {ARTIFACT_VERSION}")
        trained = payload.get("trained_through")
        return cls(
            model=str(payload["model"]),
            fitted_on=date.fromisoformat(payload["fitted_on"]),
            trained_through=date.fromisoformat(trained) if trained else None,
            horizon=int(payload["horizon"]),
            half_life=float(payload["half_life"]),
            prior_strength=float(payload["prior_strength"]),
            ridge=float(payload.get("ridge", DEFAULT_RIDGE)),
            levels={key: LevelWeights.from_dict(value) for key, value in payload["levels"].items()},
            calibration=(
                Calibration.from_dict(payload["calibration"]) if payload.get("calibration") else None
            ),
            version=int(version),
        )

    def digest(self) -> str:
        """Short content hash, journalled beside every composite so it can be recomputed."""
        canonical = json.dumps(self.to_dict(), sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:12]

    def weights_for(self, ticker: str) -> tuple[dict[str, float], str]:
        """The deepest fitted level this ticker reads from, and its key.

        Every stored level already carries its shrinkage toward the levels
        above, so the deepest one present is the right one. A ticker no level
        covers gets equal weights, labelled as such.
        """
        for key in chain_for(ticker):
            level = self.levels.get(key)
            if level is not None:
                return dict(level.weights), key
        return dict(EQUAL_WEIGHTS), EQUAL_KEY


def apply(
    artifact: Optional[WeightsArtifact], ticker: str, scores: Mapping[str, Optional[float]]
) -> tuple[Optional[Composite], str]:
    """Blend one signal's scores with the weights its ticker resolves to."""
    if artifact is None:
        return composite(scores, EQUAL_WEIGHTS), EQUAL_KEY
    weights, key = artifact.weights_for(ticker)
    return composite(scores, weights), key


# --------------------------------------------------------------------------- #
# Fitting
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Observation:
    """One scored signal joined to what followed it."""

    ticker: str
    when: date
    scores: Mapping[str, Optional[float]]
    #: Forward return over the horizon, in whatever units the trainer chose.
    #: Non-finite targets are skipped.
    target: float


def decay_weight(when: date, as_of: date, half_life: float) -> float:
    """``0.5 ** (age / half_life)`` with age in sessions; never more than 1."""
    age_days = max(0, (as_of - when).days)
    age_sessions = age_days * SESSIONS_PER_YEAR / 365.0
    return 0.5 ** (age_sessions / half_life) if half_life > 0 else 1.0


@dataclass(frozen=True)
class RawFit:
    weights: dict[str, float]
    intercept: float
    n_effective: float
    n_raw: int


def fit_raw(
    observations: Iterable[Observation],
    *,
    as_of: date,
    half_life: float = DEFAULT_HALF_LIFE,
    ridge: float = DEFAULT_RIDGE,
) -> RawFit:
    """Decayed ridge regression of target on the five scores plus an intercept.

    A missing score is a zero feature. With no usable observations the
    coefficients are all zero and the counts say so.
    """
    k = len(SCORE_FIELDS)
    size = k + 1  # the last index is the intercept
    a = [[0.0] * size for _ in range(size)]
    b = [0.0] * size
    n_effective = 0.0
    n_raw = 0
    for obs in observations:
        if not _finite(obs.target):
            continue
        x = [float(obs.scores.get(name)) if _finite(obs.scores.get(name)) else 0.0 for name in SCORE_FIELDS]
        x.append(1.0)
        d = decay_weight(obs.when, as_of, half_life)
        n_effective += d
        n_raw += 1
        for i in range(size):
            b[i] += d * x[i] * obs.target
            row = a[i]
            for j in range(size):
                row[j] += d * x[i] * x[j]
    if n_raw == 0:
        return RawFit({name: 0.0 for name in SCORE_FIELDS}, 0.0, 0.0, 0)
    for i in range(size):
        a[i][i] += ridge
    theta = _solve(a, b)
    return RawFit(
        weights={name: theta[i] for i, name in enumerate(SCORE_FIELDS)},
        intercept=theta[k],
        n_effective=n_effective,
        n_raw=n_raw,
    )


def fit_hierarchy(
    observations: Iterable[Observation],
    *,
    model: str,
    horizon: int,
    as_of: date,
    half_life: float = DEFAULT_HALF_LIFE,
    prior_strength: float = DEFAULT_PRIOR_STRENGTH,
    ridge: float = DEFAULT_RIDGE,
) -> WeightsArtifact:
    """Fit every level the observations touch and shrink each toward its parent."""
    observations = [o for o in observations if _finite(o.target)]
    members: dict[str, list[Observation]] = {}
    parents: dict[str, Optional[str]] = {}
    depth: dict[str, int] = {}
    for obs in observations:
        chain = chain_for(obs.ticker)
        for level_index, key in enumerate(chain):
            members.setdefault(key, []).append(obs)
            parents[key] = chain[level_index + 1] if level_index + 1 < len(chain) else None
            depth[key] = len(chain) - 1 - level_index  # global is 0

    levels: dict[str, LevelWeights] = {}
    for key in sorted(members, key=lambda k: (depth[k], k)):
        raw = fit_raw(members[key], as_of=as_of, half_life=half_life, ridge=ridge)
        parent = parents[key]
        parent_weights = levels[parent].weights if parent in levels else dict(EQUAL_WEIGHTS)
        learned_anything = sum(abs(w) for w in raw.weights.values()) > 0.0
        own_share = raw.n_effective / (raw.n_effective + prior_strength) if learned_anything else 0.0
        own = normalise(raw.weights) if learned_anything else parent_weights
        blended = {
            name: own_share * own[name] + (1.0 - own_share) * parent_weights[name]
            for name in SCORE_FIELDS
        }
        levels[key] = LevelWeights(
            key=key,
            parent=parent,
            fitted=raw.weights,
            intercept=raw.intercept,
            n_effective=raw.n_effective,
            n_raw=raw.n_raw,
            weights=normalise(blended),
            own_share=own_share,
        )

    return WeightsArtifact(
        model=model,
        fitted_on=as_of,
        trained_through=max((o.when for o in observations), default=None),
        horizon=horizon,
        half_life=half_life,
        prior_strength=prior_strength,
        ridge=ridge,
        levels=levels,
    )


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #


def _finite(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _solve(a: list[list[float]], b: list[float]) -> list[float]:
    """Gaussian elimination with partial pivoting. ``a`` is ridge-augmented, so it is invertible."""
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(m[r][col]))
        if abs(m[pivot][col]) < 1e-12:
            raise ValueError("singular normal equations; the ridge should have prevented this")
        m[col], m[pivot] = m[pivot], m[col]
        for r in range(col + 1, n):
            factor = m[r][col] / m[col][col]
            if factor != 0.0:
                for c in range(col, n + 1):
                    m[r][c] -= factor * m[col][c]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (m[r][n] - sum(m[r][c] * x[c] for c in range(r + 1, n))) / m[r][r]
    return x
