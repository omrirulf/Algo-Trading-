"""Apply the learned blend inside a cycle -- in shadow.

``analysis.blend`` turns the model's five dimension scores into one composite
using weights a separate trainer fitted from the journal. This module is the
live side of that: it reads the weights file once per cycle, blends each
full-model signal, and hands the result to the journal beside the model's own
answer.

Nothing here reaches the engine. ``BLEND_MODE`` is ``shadow``, the only
consumer of what this module produces is the journal line, and the signal
that goes to ``post_signal`` is the model's, untouched; a CI invariant pins
all three. That is deliberate: the composite has to sit next to realised
returns for a while before anyone can say whether it beats the model's own
conviction, and the walk-forward report is what will say so.

Failure is a labelled fallback, never an exception. No file, an unreadable
file, a file fitted for another model: each becomes equal weights with the
reason journalled, and the cycle runs exactly as it did before this existed.
Only the full model's signal is blended. The screening model's scores are a
different model's reads, and weights fitted to one are not weights for the
other, so a screened line carries no composite rather than a misleading one.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Optional

from analysis.blend import WeightsArtifact, apply as blend_scores
from analysis.reader import SCORE_FIELDS
from app.schemas import LLMSignal
from config import settings as cfg

log = logging.getLogger("blend")

#: Where the weights a cycle applied came from. Journalled on every line.
SOURCE_FILE = "file"
SOURCE_MISSING = "missing"
SOURCE_UNREADABLE = "unreadable"
SOURCE_OTHER_MODEL = "other model"


@dataclass(frozen=True)
class LoadedWeights:
    """The weights file as one cycle saw it, or why it fell back."""

    artifact: Optional[WeightsArtifact]
    source: str
    digest: Optional[str] = None
    #: Days since the file was fitted; ``None`` when nothing was loaded.
    age_days: Optional[int] = None
    note: Optional[str] = None

    @property
    def stale(self) -> bool:
        return self.age_days is not None and self.age_days > cfg.BLEND_STALE_AFTER_DAYS


def load_weights(
    path: Path | str | None = None,
    *,
    model: str,
    today: Optional[date] = None,
) -> LoadedWeights:
    """Read the weights once for a cycle. Never raises.

    The path defaults to ``BLEND_WEIGHTS_PATH`` at call time rather than at
    import, so a test can point it somewhere harmless.
    """
    path = Path(path) if path is not None else Path(cfg.BLEND_WEIGHTS_PATH)
    if not path.exists():
        log.info("no blend weights at %s; blending with equal weights", path)
        return LoadedWeights(None, SOURCE_MISSING, note=f"no file at {path.name}")
    try:
        artifact = WeightsArtifact.from_dict(json.loads(path.read_text(encoding="utf-8")))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        log.warning("blend weights at %s unreadable (%s); blending with equal weights", path, exc)
        return LoadedWeights(None, SOURCE_UNREADABLE, note=f"{type(exc).__name__}: {exc}"[:200])
    if artifact.model != model:
        log.warning(
            "blend weights were fitted for %s, not %s; blending with equal weights",
            artifact.model, model,
        )
        return LoadedWeights(
            None, SOURCE_OTHER_MODEL, digest=artifact.digest(), note=f"fitted for {artifact.model}"
        )
    today = today or datetime.now(timezone.utc).date()
    age = max(0, (today - artifact.fitted_on).days)
    loaded = LoadedWeights(artifact, SOURCE_FILE, digest=artifact.digest(), age_days=age)
    if loaded.stale:
        log.warning("blend weights are %d days old; still applied, flagged stale", age)
    else:
        log.info("blend weights %s loaded, %d level(s), fitted %s", loaded.digest, len(artifact.levels), artifact.fitted_on)
    return loaded


def blend_signal(signal: LLMSignal, loaded: LoadedWeights) -> dict[str, Any]:
    """The blend record journalled beside one full-model signal.

    Enough is written to recompute the composite from the line alone: the
    weights digest, the level the ticker resolved to, the five normalised
    weights actually applied and which dimensions had a score.
    """
    scores = {name: getattr(signal, name) for name in SCORE_FIELDS}
    result, level = blend_scores(loaded.artifact, signal.ticker, scores)
    record: dict[str, Any] = {
        "mode": cfg.BLEND_MODE,
        "source": loaded.source,
        "weights": loaded.digest,
        "stale": loaded.stale,
        "level": level,
        "composite": None,
        "coverage": None,
        "used": [],
        "applied": None,
    }
    if loaded.note:
        record["note"] = loaded.note
    if result is not None:
        record.update(
            composite=round(result.value, 6),
            coverage=round(result.coverage, 6),
            used=list(result.used),
            applied={name: round(w, 6) for name, w in result.weights.items()},
        )
    return record
