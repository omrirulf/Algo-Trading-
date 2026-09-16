"""The live side of the blend: read the weights once, blend in shadow, never raise."""

from __future__ import annotations

import json
from datetime import date, timedelta

import pytest

from analysis.blend import EQUAL_KEY, EQUAL_WEIGHTS, Observation, fit_hierarchy
from analysis.reader import SCORE_FIELDS
from app.schemas import Bias, LLMSignal
from orchestrator import blend

TODAY = date(2026, 9, 16)
MODEL = "claude-opus-5"


def signal(**scores) -> LLMSignal:
    return LLMSignal(ticker="NVDA", bias=Bias.BULLISH, conviction=0.6, rationale="r", **scores)


def planted(n=60):
    out = []
    for i in range(n):
        s = {name: ((i * 7 + k * 3) % 11 - 5) / 5 for k, name in enumerate(SCORE_FIELDS)}
        out.append(Observation("NVDA", TODAY - timedelta(days=i), s, 0.6 * s["news_score"]))
    return out


@pytest.fixture
def weights_file(tmp_path):
    artifact = fit_hierarchy(planted(), model=MODEL, horizon=5, as_of=TODAY)
    path = tmp_path / "blend_weights.json"
    path.write_text(json.dumps(artifact.to_dict()))
    return path, artifact


# --- loading -----------------------------------------------------------------


def test_a_missing_file_is_equal_weights_with_the_reason(tmp_path):
    loaded = blend.load_weights(tmp_path / "nope.json", model=MODEL, today=TODAY)
    assert loaded.artifact is None
    assert loaded.source == blend.SOURCE_MISSING
    assert "nope.json" in (loaded.note or "")
    assert loaded.stale is False


def test_an_unreadable_file_is_equal_weights_not_an_exception(tmp_path):
    path = tmp_path / "blend_weights.json"
    path.write_text("{not json")
    loaded = blend.load_weights(path, model=MODEL, today=TODAY)
    assert loaded.artifact is None and loaded.source == blend.SOURCE_UNREADABLE
    path.write_text(json.dumps({"version": 99}))
    assert blend.load_weights(path, model=MODEL, today=TODAY).source == blend.SOURCE_UNREADABLE


def test_weights_fitted_for_another_model_are_not_applied(weights_file):
    path, artifact = weights_file
    loaded = blend.load_weights(path, model="claude-haiku-4-5", today=TODAY)
    assert loaded.artifact is None
    assert loaded.source == blend.SOURCE_OTHER_MODEL
    assert loaded.digest == artifact.digest()
    assert "claude-opus-5" in (loaded.note or "")


def test_a_good_file_loads_with_its_digest_and_age(weights_file):
    path, artifact = weights_file
    loaded = blend.load_weights(path, model=MODEL, today=TODAY + timedelta(days=3))
    assert loaded.artifact == artifact
    assert loaded.source == blend.SOURCE_FILE
    assert loaded.digest == artifact.digest()
    assert loaded.age_days == 3 and loaded.stale is False


def test_old_weights_are_still_applied_but_flagged_stale(weights_file):
    path, _ = weights_file
    loaded = blend.load_weights(path, model=MODEL, today=TODAY + timedelta(days=15))
    assert loaded.artifact is not None
    assert loaded.stale is True


# --- blending ----------------------------------------------------------------


def test_without_weights_the_record_is_the_plain_average_and_says_so(tmp_path):
    loaded = blend.load_weights(tmp_path / "none.json", model=MODEL, today=TODAY)
    record = blend.blend_signal(signal(news_score=1.0, technical_score=0.5), loaded)
    assert record["mode"] == "shadow"
    assert record["source"] == blend.SOURCE_MISSING
    assert record["weights"] is None
    assert record["level"] == EQUAL_KEY
    assert record["composite"] == pytest.approx(0.3)
    assert record["coverage"] == pytest.approx(0.4)
    assert record["used"] == ["news_score", "technical_score"]
    assert record["applied"] == {name: pytest.approx(0.2) for name in SCORE_FIELDS}
    assert record["stale"] is False


def test_with_weights_the_record_names_the_level_and_the_digest(weights_file):
    path, artifact = weights_file
    loaded = blend.load_weights(path, model=MODEL, today=TODAY)
    record = blend.blend_signal(signal(news_score=1.0), loaded)
    assert record["level"] == "ticker:NVDA"
    assert record["weights"] == artifact.digest()
    assert record["applied"] == {
        name: pytest.approx(w, abs=1e-6) for name, w in artifact.levels["ticker:NVDA"].weights.items()
    }
    assert record["composite"] == pytest.approx(artifact.levels["ticker:NVDA"].weights["news_score"], abs=1e-6)


def test_a_signal_with_no_scores_at_all_records_no_composite(tmp_path):
    loaded = blend.load_weights(tmp_path / "none.json", model=MODEL, today=TODAY)
    record = blend.blend_signal(signal(), loaded)
    assert record["composite"] is None and record["coverage"] is None
    assert record["used"] == [] and record["applied"] is None


def test_the_record_is_json_serialisable(weights_file):
    path, _ = weights_file
    loaded = blend.load_weights(path, model=MODEL, today=TODAY)
    json.dumps(blend.blend_signal(signal(news_score=0.2, insider_score=-0.4), loaded))
