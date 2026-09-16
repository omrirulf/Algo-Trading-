"""The blend is pure arithmetic, so every property it promises is checkable here.

Nothing in these tests touches a file, a price, or the engine.
"""

from __future__ import annotations

import math
import random
from datetime import date, timedelta

import pytest

from analysis import blend
from analysis.blend import (
    EQUAL_KEY,
    EQUAL_WEIGHTS,
    GLOBAL_KEY,
    Observation,
    WeightsArtifact,
    apply,
    chain_for,
    composite,
    decay_weight,
    fit_hierarchy,
    fit_raw,
    normalise,
)
from analysis.reader import SCORE_FIELDS

TODAY = date(2026, 9, 16)


def scores(**values):
    """All five fields, null unless given."""
    return {name: values.get(name.replace("_score", "")) for name in SCORE_FIELDS}


# --- composite ---------------------------------------------------------------


def test_equal_weights_average_the_scores_that_exist():
    out = composite(scores(news=0.5, technical=-0.5, fundamental=1.0, analyst=0.0, insider=0.5))
    assert out is not None
    assert out.value == pytest.approx((0.5 - 0.5 + 1.0 + 0.0 + 0.5) / 5)
    assert out.coverage == pytest.approx(1.0)
    assert out.used == SCORE_FIELDS


def test_a_missing_dimension_contributes_nothing_and_lowers_coverage():
    full = composite(scores(news=1.0, technical=1.0, fundamental=1.0, analyst=1.0, insider=1.0))
    partial = composite(scores(news=1.0, technical=1.0))
    assert full is not None and partial is not None
    assert full.value == pytest.approx(1.0)
    # Two of five equal weights had data: the composite cannot exceed 0.4.
    assert partial.value == pytest.approx(0.4)
    assert partial.coverage == pytest.approx(0.4)
    assert partial.used == ("news_score", "technical_score")


def test_nothing_to_blend_is_none_not_zero():
    assert composite(scores()) is None


def test_weights_are_normalised_by_absolute_value_so_negatives_are_allowed():
    weights = {"news_score": 3.0, "technical_score": -1.0}
    normalised = normalise(weights)
    assert normalised["news_score"] == pytest.approx(0.75)
    assert normalised["technical_score"] == pytest.approx(-0.25)
    assert sum(abs(w) for w in normalised.values()) == pytest.approx(1.0)
    out = composite(scores(news=1.0, technical=1.0), weights)
    assert out is not None
    assert out.value == pytest.approx(0.5)


def test_zero_or_nonfinite_weights_fall_back_to_equal():
    assert normalise({name: 0.0 for name in SCORE_FIELDS}) == EQUAL_WEIGHTS
    assert normalise({"news_score": float("nan")}) == EQUAL_WEIGHTS


def test_composite_never_leaves_the_unit_interval():
    out = composite(scores(news=1.0, technical=1.0, fundamental=1.0, analyst=1.0, insider=1.0),
                    {name: 7.0 for name in SCORE_FIELDS})
    assert out is not None and out.value == pytest.approx(1.0)
    out = composite(scores(news=-1.0), {"news_score": 1.0})
    assert out is not None and out.value == pytest.approx(-1.0)


def test_a_zero_score_is_a_read_and_counts_as_present():
    out = composite(scores(news=0.0))
    assert out is not None
    assert out.used == ("news_score",)
    assert out.value == 0.0


# --- decay and the raw fit ---------------------------------------------------


def test_an_observation_one_half_life_old_counts_half():
    half_life = 60.0
    calendar_days = round(half_life * 365 / blend.SESSIONS_PER_YEAR)
    assert decay_weight(TODAY - timedelta(days=calendar_days), TODAY, half_life) == pytest.approx(0.5, abs=0.01)
    assert decay_weight(TODAY, TODAY, half_life) == 1.0
    # A future-dated line cannot count more than today's.
    assert decay_weight(TODAY + timedelta(days=30), TODAY, half_life) == 1.0


def planted(n: int, seed: int = 7, *, missing=()):
    """Scores drawn at random, target = 0.6*news - 0.4*technical + 0.1, no noise."""
    rng = random.Random(seed)
    out = []
    for i in range(n):
        s = {name: rng.uniform(-1, 1) for name in SCORE_FIELDS}
        for name in missing:
            s[name] = None
        target = 0.6 * s["news_score"] - 0.4 * s["technical_score"] + 0.1
        out.append(Observation("NVDA", TODAY - timedelta(days=i), s, target))
    return out


def test_the_raw_fit_recovers_planted_weights_and_intercept():
    fit = fit_raw(planted(400), as_of=TODAY, half_life=1e9, ridge=1e-6)
    assert fit.weights["news_score"] == pytest.approx(0.6, abs=0.01)
    assert fit.weights["technical_score"] == pytest.approx(-0.4, abs=0.01)
    for name in ("fundamental_score", "analyst_score", "insider_score"):
        assert fit.weights[name] == pytest.approx(0.0, abs=0.01)
    assert fit.intercept == pytest.approx(0.1, abs=0.01)
    assert fit.n_raw == 400
    assert fit.n_effective == pytest.approx(400)


def test_decay_makes_the_effective_count_smaller_than_the_raw_one():
    fit = fit_raw(planted(400), as_of=TODAY, half_life=20.0)
    assert fit.n_raw == 400
    assert 0 < fit.n_effective < 100


def test_a_dimension_that_never_had_data_gets_zero_weight_without_crashing():
    fit = fit_raw(planted(50, missing=("insider_score",)), as_of=TODAY)
    assert fit.weights["insider_score"] == 0.0
    assert fit.n_raw == 50


def test_nonfinite_targets_are_skipped_and_an_empty_fit_is_all_zero():
    empty = fit_raw([], as_of=TODAY)
    assert empty.n_raw == 0 and empty.n_effective == 0.0
    assert all(w == 0.0 for w in empty.weights.values())
    bad = [Observation("NVDA", TODAY, scores(news=1.0), float("nan"))]
    assert fit_raw(bad, as_of=TODAY).n_raw == 0


# --- the hierarchy -----------------------------------------------------------


def test_chain_reads_ticker_then_kind_then_global():
    assert chain_for("nvda") == ("ticker:NVDA", "kind:equity", GLOBAL_KEY)
    assert chain_for("GLD") == ("ticker:GLD", "kind:commodity fund", GLOBAL_KEY)
    assert chain_for("RSP")[1] == "kind:broad fund"


def test_a_level_with_no_evidence_is_its_parent_and_the_global_root_is_equal_weights():
    artifact = fit_hierarchy([], model="m", horizon=5, as_of=TODAY)
    assert artifact.levels == {}
    assert artifact.trained_through is None
    assert artifact.weights_for("NVDA") == (EQUAL_WEIGHTS, EQUAL_KEY)


def test_a_thin_ticker_leans_on_its_kind_and_a_rich_one_on_itself():
    rich = planted(400)
    # One MSFT observation says the opposite of what NVDA's four hundred say.
    contrary = [Observation("MSFT", TODAY, {**scores(news=1.0, technical=1.0)}, -1.0)]
    artifact = fit_hierarchy(rich + contrary, model="m", horizon=5, as_of=TODAY, half_life=1e9)

    nvda = artifact.levels["ticker:NVDA"]
    msft = artifact.levels["ticker:MSFT"]
    kind = artifact.levels["kind:equity"]

    assert nvda.own_share == pytest.approx(400 / 420)
    assert msft.own_share == pytest.approx(1 / 21)
    # NVDA's final weights are essentially its own fit: news 0.6, technicals -0.4.
    assert nvda.weights["news_score"] == pytest.approx(0.6, abs=0.03)
    assert nvda.weights["technical_score"] == pytest.approx(-0.4, abs=0.03)
    # MSFT's are within a twentieth of the kind's, whatever its one line said.
    for name in SCORE_FIELDS:
        assert abs(msft.weights[name] - kind.weights[name]) < 0.06
    assert msft.parent == "kind:equity" and kind.parent == GLOBAL_KEY
    assert artifact.levels[GLOBAL_KEY].parent is None


def test_every_stored_level_has_unit_absolute_weight():
    artifact = fit_hierarchy(planted(30) + planted(5, seed=3), model="m", horizon=5, as_of=TODAY)
    for level in artifact.levels.values():
        assert sum(abs(w) for w in level.weights.values()) == pytest.approx(1.0)


def test_an_unseen_ticker_falls_back_to_its_kind_then_global():
    artifact = fit_hierarchy(planted(100), model="m", horizon=5, as_of=TODAY)
    weights, key = artifact.weights_for("MSFT")
    assert key == "kind:equity"
    assert weights == artifact.levels["kind:equity"].weights
    weights, key = artifact.weights_for("GLD")
    assert key == GLOBAL_KEY


def test_apply_labels_where_the_weights_came_from():
    artifact = fit_hierarchy(planted(100), model="m", horizon=5, as_of=TODAY)
    out, key = apply(artifact, "NVDA", scores(news=1.0))
    assert key == "ticker:NVDA" and out is not None
    out, key = apply(None, "NVDA", scores(news=1.0))
    assert key == EQUAL_KEY and out is not None and out.value == pytest.approx(0.2)


# --- storage -----------------------------------------------------------------


def test_round_trip_is_lossless_and_the_digest_tracks_content():
    artifact = fit_hierarchy(planted(60), model="claude-opus-5", horizon=5, as_of=TODAY)
    payload = artifact.to_dict()
    back = WeightsArtifact.from_dict(payload)
    assert back == artifact
    assert back.digest() == artifact.digest()
    assert len(artifact.digest()) == 12
    other = fit_hierarchy(planted(61), model="claude-opus-5", horizon=5, as_of=TODAY)
    assert other.digest() != artifact.digest()


def test_a_foreign_version_is_refused_rather_than_misread():
    payload = fit_hierarchy([], model="m", horizon=5, as_of=TODAY).to_dict()
    payload["version"] = 99
    with pytest.raises(ValueError):
        WeightsArtifact.from_dict(payload)


def test_the_payload_is_plain_json():
    import json
    artifact = fit_hierarchy(planted(10), model="m", horizon=5, as_of=TODAY)
    text = json.dumps(artifact.to_dict())
    assert "ticker:NVDA" in text
    assert math.isfinite(json.loads(text)["levels"]["global"]["intercept"])
