"""The null test and self-consistency, and the batch helper they ride on.

Nothing here reaches the network: the batch client is a fake with the three
methods the helper calls, and the sanity scoring is exercised on constructed
trials.
"""

from __future__ import annotations

import json
import re
import types
from pathlib import Path

import pytest
import yaml

from app.schemas import Bias, LLMSignal
from config import settings as cfg
from orchestrator import llm
from orchestrator.context import TickerContext
from replay import signal_sanity as ss


# --------------------------------------------------------------------------- #
# batch helper
# --------------------------------------------------------------------------- #

class _Result:
    def __init__(self, custom_id, kind, text=None, error=None):
        self.custom_id = custom_id
        msg = None
        if kind == "succeeded":
            block = types.SimpleNamespace(type="text", text=text)
            usage = types.SimpleNamespace(input_tokens=100, output_tokens=50,
                                          cache_read_input_tokens=0, cache_creation_input_tokens=0)
            msg = types.SimpleNamespace(content=[block], usage=usage, model="claude-opus-5",
                                        stop_reason="end_turn")
        self.result = types.SimpleNamespace(type=kind, message=msg, error=error)


class _FakeBatches:
    def __init__(self, results, statuses=("in_progress", "ended")):
        self.created = None
        self._results = results
        self._statuses = list(statuses)
        self.retrieves = 0

    def create(self, requests):
        self.created = requests
        return types.SimpleNamespace(id="batch_test", processing_status="in_progress")

    def retrieve(self, batch_id):
        self.retrieves += 1
        status = self._statuses.pop(0) if len(self._statuses) > 1 else self._statuses[0]
        return types.SimpleNamespace(id=batch_id, processing_status=status)

    def results(self, batch_id):
        return iter(self._results)


def _provider(batches):
    p = llm.AnthropicSignalProvider("test-key")
    p._client = types.SimpleNamespace(messages=types.SimpleNamespace(batches=batches))
    return p


def _req(cid, model=None, effort=None):
    return llm.BatchRequest(cid, "SYS", "USER", {"type": "object", "properties": {}},
                            model=model, effort=effort)


def test_batch_params_match_the_live_shape_minus_fallbacks():
    p = _provider(_FakeBatches([]))
    params = p._batch_params(_req("a", effort="low"))
    assert params["model"] == llm.MODEL
    assert params["cache_control"] == {"type": "ephemeral"}
    assert params["thinking"] == {"type": "adaptive"}
    assert params["output_config"]["effort"] == "low"
    assert params["output_config"]["format"]["type"] == "json_schema"
    # Batches rejects server-side fallbacks; the helper must not send them.
    assert "fallbacks" not in params and "betas" not in params


def test_submit_rejects_duplicate_ids_and_empty_batches():
    p = _provider(_FakeBatches([]))
    with pytest.raises(llm.LLMError):
        p.submit_batch([])
    with pytest.raises(llm.LLMError):
        p.submit_batch([_req("same"), _req("same")])


def test_results_are_keyed_by_custom_id_not_position():
    good = json.dumps({"ok": 1})
    batches = _FakeBatches([_Result("b", "succeeded", good), _Result("a", "succeeded", good)])
    p = _provider(batches)
    out = p.complete_batch([_req("a"), _req("b")], sleep=lambda s: None)
    assert set(out) == {"a", "b"}
    assert isinstance(out["a"], llm.Completion) and isinstance(out["b"], llm.Completion)
    assert batches.retrieves == 2  # polled once while in_progress, once ended


def test_an_errored_item_is_an_error_not_a_missing_key():
    batches = _FakeBatches([_Result("a", "errored", error="boom"),
                            _Result("b", "expired")])
    p = _provider(batches)
    out = p.complete_batch([_req("a"), _req("b")], sleep=lambda s: None)
    assert isinstance(out["a"], llm.LLMError) and "boom" in str(out["a"])
    assert isinstance(out["b"], llm.LLMError) and "expired" in str(out["b"])


def test_non_json_output_is_an_error_row():
    batches = _FakeBatches([_Result("a", "succeeded", "not json")])
    p = _provider(batches)
    out = p.complete_batch([_req("a")], sleep=lambda s: None)
    assert isinstance(out["a"], llm.LLMError)


def test_a_stuck_batch_times_out_with_a_resumable_id(monkeypatch):
    batches = _FakeBatches([], statuses=("in_progress",))
    p = _provider(batches)
    clock = iter([0.0, 0.0, 10.0, 10.0])
    monkeypatch.setattr(llm.time, "monotonic", lambda: next(clock))
    with pytest.raises(llm.BatchTimeout) as excinfo:
        p.collect_batch("batch_test", timeout_seconds=5, sleep=lambda s: None)
    assert excinfo.value.batch_id == "batch_test"
    assert "--resume batch_test" in str(excinfo.value)


# --------------------------------------------------------------------------- #
# scramble construction
# --------------------------------------------------------------------------- #

def _ctx(t):
    return TickerContext(ticker=t, headlines=[f"{t} headline"])


def _sp(t):
    return "ETF-PROMPT" if t in ("RSP", "IWM", "GLD") else "EQUITY-PROMPT"


def _up(ctx):
    return ctx.as_prompt()


def test_scramble_keeps_the_label_and_swaps_all_evidence():
    donor = _ctx("NVDA").as_prompt()
    out = ss.scramble_prompt("MSFT", donor, "NVDA")
    assert out.startswith("TICKER: MSFT")
    assert "NVDA headline" in out          # the donor's evidence survives
    assert "MSFT headline" not in out      # none of the target's own


def test_scramble_refuses_a_donor_prompt_that_is_not_the_donors():
    with pytest.raises(ValueError):
        ss.scramble_prompt("MSFT", "TICKER: LLY\n...", "NVDA")


def test_derangement_never_maps_an_item_to_itself():
    m = ss.derange(["A", "B", "C"])
    assert set(m) == {"A", "B", "C"}
    assert all(k != v for k, v in m.items())
    assert ss.derange(["ONLY"]) == {}


def test_trials_scramble_within_instrument_kind_only():
    contexts = {t: _ctx(t) for t in ("MSFT", "NVDA", "RSP", "IWM", "GLD")}
    trials = ss.build_trials(contexts, _sp, _up)
    scr = {t.ticker: t for t in trials if t.condition == ss.SCRAMBLED}
    from config.instruments import kind_for
    for target, trial in scr.items():
        assert kind_for(target) == kind_for(trial.donor), (target, trial.donor)
        assert trial.system_prompt == _sp(target)     # own prompt, donor evidence
    # every ticker gets a real and a repeat trial with identical prompts
    real = {t.ticker: t for t in trials if t.condition == ss.REAL}
    rep = {t.ticker: t for t in trials if t.condition == ss.REPEAT}
    assert set(real) == set(rep) == set(contexts)
    assert all(real[t].user_prompt == rep[t].user_prompt for t in real)


def test_custom_ids_are_unique_across_all_trials():
    contexts = {t: _ctx(t) for t in ("MSFT", "NVDA", "RSP", "IWM")}
    trials = ss.build_trials(contexts, _sp, _up)
    ids = [t.custom_id for t in trials]
    assert len(ids) == len(set(ids))


# --------------------------------------------------------------------------- #
# scoring
# --------------------------------------------------------------------------- #

def _sig(t, bias, conv=0.7):
    return LLMSignal(ticker=t, bias=bias, conviction=conv, rationale="x")


def _trial(t, cond, sig):
    tr = ss.Trial(t, cond, "S", "U")
    tr.signal = sig
    return tr


def _report(real, repeat, scrambled):
    return ss.Report(
        tickers=len(real),
        real={t: _trial(t, ss.REAL, s) for t, s in real.items()},
        repeat={t: _trial(t, ss.REPEAT, s) for t, s in repeat.items()},
        scrambled={t: _trial(t, ss.SCRAMBLED, s) for t, s in scrambled.items()},
    )


B, S, N = Bias.BULLISH, Bias.BEARISH, Bias.NEUTRAL


def test_kappa_is_chance_corrected():
    """All-NEUTRAL columns agree perfectly by chance; kappa says so by being undefined."""
    assert ss.kappa([("neutral", "neutral")] * 10) is None
    assert ss.kappa([("bullish", "bullish"), ("bearish", "bearish")]) == pytest.approx(1.0)
    assert ss.kappa([("bullish", "bearish"), ("bearish", "bullish")]) == pytest.approx(-1.0)
    assert ss.kappa([]) is None


def test_theater_when_the_answer_survives_scrambling():
    tick = list("ABCDEFGH")
    real = {t: _sig(t, B if i % 2 else S) for i, t in enumerate(tick)}
    r = _report(real, real, real)             # scrambled answers identical to real
    assert r.scramble_kappa == pytest.approx(1.0)
    assert r.verdicts.theater
    assert "THEATER" in r.verdicts.as_list()


def test_pass_when_scrambling_changes_the_answer_and_repeats_do_not():
    tick = list("ABCDEFGH")
    real = {t: _sig(t, B if i % 2 else S) for i, t in enumerate(tick)}
    flipped = {t: _sig(t, S if i % 2 else B) for i, t in enumerate(tick)}
    r = _report(real, real, flipped)
    assert r.self_agreement == 1.0
    assert r.scramble_kappa == pytest.approx(-1.0)
    assert r.verdicts.passed


def test_noise_when_the_model_disagrees_with_itself():
    tick = list("ABCDEFGHIJ")
    real = {t: _sig(t, B) for t in tick}
    repeat = {t: _sig(t, B if i < 5 else S) for i, t in enumerate(tick)}   # 50% agreement
    r = _report(real, repeat, {})
    assert r.self_agreement == pytest.approx(0.5)
    assert r.verdicts.noise


def test_silent_when_nothing_clears_the_floor():
    tick = list("ABCDEFGHIJ")
    real = {t: _sig(t, N, conv=0.2) for t in tick}
    r = _report(real, real, {})
    assert r.trade_rate(r.real) == 0.0
    assert r.verdicts.silent
    assert r.self_kappa is None            # undefined, not a false pass


def test_trades_uses_the_engines_conviction_floor():
    assert ss.trades(_sig("A", B, cfg.MIN_CONVICTION)) is True
    assert ss.trades(_sig("A", B, cfg.MIN_CONVICTION - 0.01)) is False
    assert ss.trades(_sig("A", N, 0.99)) is False
    assert ss.trades(None) is False


def test_thresholds_are_the_pre_registered_ones():
    """Pinned so that moving a threshold after seeing a result is a visible diff."""
    assert ss.SILENT_TRADE_RATE == 0.10
    assert ss.NOISE_SELF_AGREEMENT == 0.70
    assert ss.THEATER_SCRAMBLE_KAPPA == 0.40


def test_report_renders_and_serialises():
    tick = list("ABCDEF")
    real = {t: _sig(t, B if i % 2 else S) for i, t in enumerate(tick)}
    flipped = {t: _sig(t, S if i % 2 else B) for i, t in enumerate(tick)}
    r = _report(real, real, flipped)
    text = ss.render(r)
    assert "SIGNAL SANITY" in text and "VERDICT: PASS" in text
    d = json.loads(json.dumps(r.as_dict()))
    assert d["passed"] is True and d["verdicts"] == ["PASS"]


def test_apply_results_routes_errors_to_the_failed_list():
    trials = [ss.Trial("A", ss.REAL, "S", "U"), ss.Trial("B", ss.REAL, "S", "U")]
    good = llm.Completion(text=_sig("A", B).model_dump_json(), usage=None)
    ss.apply_results(trials, {"A_real": good, "B_real": llm.LLMError("nope")},
                     LLMSignal.model_validate_json)
    r = ss.assemble(trials, 2)
    assert "A" in r.real and "B" not in r.real
    assert [t.custom_id for t in r.failed] == ["B_real"]


# --------------------------------------------------------------------------- #
# the two clocks
# --------------------------------------------------------------------------- #

def _write_trials(tmp_path):
    path = tmp_path / "trials.json"
    path.write_text(json.dumps({"tickers": 1, "trials": [
        {"ticker": "AAA", "condition": "real", "system_prompt": "S",
         "user_prompt": "U", "donor": None},
    ]}))
    return path


def test_collect_passes_its_own_clock_to_the_batch(tmp_path, monkeypatch):
    """The CLI's --timeout-minutes must reach collect_batch.

    The workflow sets it from its own job timeout so the collector gives up
    first and prints a resumable id. A flag that never arrived would leave the
    module default in force and the runner would be killed holding the batch.
    """
    seen = {}

    class _Provider:
        def __init__(self, key):
            pass

        def collect_batch(self, batch_id, **kw):
            seen.update(kw, batch=batch_id)
            return {}

    monkeypatch.setattr(llm, "AnthropicSignalProvider", _Provider)
    ss.main(["collect", "--trials", str(_write_trials(tmp_path)),
                 "--batch", "msgbatch_x", "--timeout-minutes", "215"])
    assert seen["batch"] == "msgbatch_x"
    assert seen["timeout_seconds"] == 215 * 60


def test_collect_without_the_flag_falls_back_to_the_module_default(tmp_path, monkeypatch):
    seen = {}

    class _Provider:
        def __init__(self, key):
            pass

        def collect_batch(self, batch_id, **kw):
            seen.update(kw)
            return {}

    monkeypatch.setattr(llm, "AnthropicSignalProvider", _Provider)
    ss.main(["collect", "--trials", str(_write_trials(tmp_path)), "--batch", "b"])
    assert seen["timeout_seconds"] == pytest.approx(llm.BATCH_TIMEOUT_SECONDS)


def test_the_collector_gives_up_before_the_job_does():
    """The inner clock must be under the outer one, or the id is never printed.

    A job killed by GitHub prints nothing, and a batch id that was never
    printed cannot be resumed -- the only way back to a batch that is already
    finished and already paid for. The margin also has to cover planning and
    submitting, which happen inside the same step before the wait begins.
    """
    workflow = yaml.safe_load(
        (Path(__file__).resolve().parents[1] / ".github/workflows/signal-sanity.yml").read_text()
    )
    job = workflow["jobs"]["sanity"]
    outer = job["timeout-minutes"]
    script = next(s["run"] for s in job["steps"] if s.get("name") == "Plan, submit, collect")
    waits = [float(m) for m in re.findall(r"--timeout-minutes (\d+(?:\.\d+)?)", script)]
    assert waits, "the collect call must set its own clock explicitly"
    assert max(waits) < outer, f"inner wait {max(waits)} is not under the job's {outer}"
    assert outer - max(waits) >= 15, "leave room for planning and submitting"
