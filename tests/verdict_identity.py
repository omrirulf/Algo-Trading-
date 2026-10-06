"""Fixed inputs for proving that the checkpoint verdict moved no existing value.

Not a test module (no ``test_`` prefix): ``tests/test_fund_test_verdict.py``
runs these documents in a fresh interpreter and compares every existing key
of ``logs/funds.json`` (``shadow.run.build``) and ``logs/race_gate.json``
(``horse_race.gate_json``) with hashes recorded from the code BEFORE the
verdict was wired in (commit ccdb477), the new keys removed. The owner's
identity condition (26 Sep 2026): no number in a race or fund output moves;
the verdict only adds keys.

Uses nothing the verdict added, so the same file ran on the code before it.
Floats are written to 12 significant digits before hashing: Python 3.12's
compensated ``sum()`` moves the last bits of a few sums (see
``tests/test_shadow_same_day.py``), and the CI runs 3.11 and 3.12.
"""

from __future__ import annotations

import hashlib
import json
import tempfile
from contextlib import contextmanager
from dataclasses import replace
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

#: The keys the verdict adds. It fills no existing key: ``fund_test.next_checkpoint``
#: stays null, as it always was, and the fund test's next look and bar (the
#: owner's reading 5) go in the new key ``fund_test.next_look``.
NEW_FUNDS_KEYS = ("verdict",)
NEW_FUND_TEST_KEYS = ("looks", "verdict", "planned_sessions", "next_look", "note")
FILLED_FUND_TEST_KEYS: tuple[str, ...] = ()
NEW_GATE_KEYS = ("verdict",)


def _normal(value):
    if isinstance(value, float):
        return float(f"{value:.12g}")
    if isinstance(value, dict):
        return {k: _normal(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_normal(v) for v in value]
    return value


def digest(value) -> str:
    return hashlib.sha256(json.dumps(_normal(value), sort_keys=True, separators=(",", ":"),
                                     allow_nan=False).encode()).hexdigest()


def parts(document: dict, prefix: str) -> dict[str, str]:
    """The hash of every top-level key, and of every key one level down, by path."""
    out = {f"{prefix}:keys": digest(list(document))}
    for key, value in document.items():
        out[f"{prefix}:{key}"] = digest(value)
        if isinstance(value, dict):
            out[f"{prefix}:{key}:keys"] = digest(list(value))
            for sub, inner in value.items():
                out[f"{prefix}:{key}.{sub}"] = digest(inner)
    return out


def without_new_keys(document: dict, kind: str) -> dict:
    """The document as the code before the verdict wrote it: the new keys removed."""
    out = {k: v for k, v in document.items() if k not in (NEW_GATE_KEYS if kind == "gate" else NEW_FUNDS_KEYS)}
    if kind == "funds" and isinstance(out.get("fund_test"), dict):
        out["fund_test"] = {k: (None if k in FILLED_FUND_TEST_KEYS else v)
                            for k, v in out["fund_test"].items() if k not in NEW_FUND_TEST_KEYS}
    return out


@contextmanager
def patched(*changes):
    """``(object, name, value)`` set for the block and put back after."""
    saved = [(obj, name, getattr(obj, name)) for obj, name, _ in changes]
    try:
        for obj, name, value in changes:
            setattr(obj, name, value)
        yield
    finally:
        for obj, name, value in reversed(saved):
            setattr(obj, name, value)


RUNNING = {"status": "running", "days": 3, "of": 15, "end_estimate": "2026-10-19",
           "fund_test_plan": {"bars": [3.4, 2.41, 2.02], "matches_registered": True}}
LOOK_1 = {"independent": 20, "bar": 3.47, "reached": True, "outcome": None, "reason": "x", "after_tax": "waiting",
          "vt_max_drawdown": 0.041, "window_end": "2026-12-22", "readable": True}
NOT_REACHED = {"reached": False}


def _args(folder: Path, race: dict, previous: dict):
    from types import SimpleNamespace

    journal = folder / "journal"
    journal.mkdir(exist_ok=True)
    (journal / "2026-10.log").write_text("")
    gate = folder / "race_gate.json"
    gate.write_text(json.dumps(race))
    prev = folder / "funds.json"
    prev.write_text(json.dumps(previous))
    return SimpleNamespace(journal=journal, audit=folder / "audit.log", account=folder / "account.jsonl",
                           random=2, processes=1, race_gate=gate, previous=prev)


def funds_documents() -> dict[str, dict]:
    """``shadow.run.build`` on fixed inputs, by name.

    * ``running_1``, ``running_2``: calibration running (the funds are not run)
      on the night look 1 is reached and readable, and the night after it
      (the first night's document as ``--previous``).
    * ``passed``: calibration passed, the real four funds and two coin-flip
      funds on ``tests/shadow_golden.py``'s rounded prices, no look reached.
    """
    from shadow import calibration as calib
    from shadow import run as shadow_run
    from shadow import schedule
    from tests.shadow_golden import REFUSED, SESSIONS, golden_inputs
    from tests.test_exploratory import NoPrices
    from tests.test_shadow_variants import Walks

    out = {}
    night = datetime(2026, 12, 22, 23, 0, tzinfo=timezone.utc)
    race = {"looks": [LOOK_1, NOT_REACHED, NOT_REACHED]}
    with tempfile.TemporaryDirectory() as tmp, patched(
            (schedule, "CALIBRATION_START", date(2026, 9, 28)),
            (calib, "calibration_report", lambda **kw: dict(RUNNING)),
            (shadow_run, "OhlcFetcher", NoPrices)):
        first = shadow_run.build(_args(Path(tmp), race, {}), night)
        out["running_1"] = json.loads(json.dumps(first))
        second = shadow_run.build(_args(Path(tmp), race, out["running_1"]), night + timedelta(days=1))
        out["running_2"] = json.loads(json.dumps(second))

    entries, bars = golden_inputs()
    real = shadow_run.run_funds

    def funds(_entries, _start, _final, _fetcher, **kw):
        # ``fund_test`` exists only since the verdict; the code before never passed it.
        extra = {"fund_test": kw["fund_test"]} if "fund_test" in kw else {}
        return real(entries, SESSIONS[0], SESSIONS[-1], Walks(bars), random_funds=kw["random_funds"],
                    processes=1, shortable_no=REFUSED, exploratory=kw.get("exploratory", True), **extra)

    with tempfile.TemporaryDirectory() as tmp, patched(
            (schedule, "CALIBRATION_START", date(2026, 4, 1)),
            (schedule, "FUND_START", SESSIONS[0]),
            (calib, "calibration_report", lambda **kw: {"status": "passed"}),
            (shadow_run, "OhlcFetcher", NoPrices),
            (shadow_run, "run_funds", funds)):
        done = shadow_run.build(_args(Path(tmp), {"looks": [NOT_REACHED] * 3}, {}),
                                datetime(2026, 6, 6, 23, 0, tzinfo=timezone.utc))
        out["passed"] = json.loads(json.dumps(done))
    return out


def gate_documents() -> dict[str, dict]:
    """``horse_race.gate_json`` on fixed views, by name: before any look, the
    crafted 60-day race of ``tests/test_horse_race.py`` (decided at look 1 for
    momentum), a look waiting for its after-tax record, and a final look."""
    from analysis import decision_gate as gate
    from analysis import horse_race
    from rules import control, hybrid, momentum
    from tests.test_horse_race import STAMP, _arm, scored

    def view(looks, independent, entry_days):
        return horse_race.GateView(registered=True, mismatches=(), window_lines=entry_days,
                                   window_cycle_days=entry_days, unanswered_in_window=0, entry_days=entry_days,
                                   independent=independent, looks=tuple(looks), next_estimate=None)

    out = {"none": horse_race.gate_json(view(gate.evaluate({}), 0, 0), 3, STAMP)}
    days = [date(2026, 10, 1) + timedelta(days=i) for i in range(60)]
    noise = lambda i: 0.001 * ((i * 7) % 5 - 2)
    stamp = lambda d: datetime.combine(d, datetime.min.time(), tzinfo=timezone.utc)
    make = lambda arm, r, d, conviction, side: scored(r, arm=arm, entry=d.isoformat(), ticker=f"T{d.toordinal()}",
                                                      stamp=stamp(d), conviction=conviction, side=side)
    results = [
        _arm("model", [make("model", -0.02 + noise(i), d, 0.3 + 0.01 * (i % 40), "buy" if i % 3 else "sell")
                       for i, d in enumerate(days)]),
        _arm(momentum.NAME, [make(momentum.NAME, 0.02 + noise(i + 1), d, 0.5, "buy") for i, d in enumerate(days)]),
        _arm(hybrid.NAME, [make(hybrid.NAME, noise(i + 2), d, 0.55, "buy") for i, d in enumerate(days)]),
        _arm(control.NAME, []),
    ]
    raw = horse_race.look_inputs(results, {}, days, {d: 0.0 for d in days}, 60, 3, 10)
    decided = replace(raw, after_tax=gate.AfterTax(gate.AFTER_TAX_READY, {momentum.NAME: 9.0}),
                      window_end=date(2026, 12, 2), vt_max_drawdown=0.041)
    splits = horse_race.trade_splits(results)
    out["crafted"] = horse_race.gate_json(view(gate.evaluate({20: decided}), 20, 60), 3, STAMP, splits=splits)
    out["waiting"] = horse_race.gate_json(view(gate.evaluate({20: replace(decided, after_tax=None)}), 20, 60),
                                          3, STAMP)
    final = replace(decided, t_vs_index={momentum.NAME: 9.0, "model": 0.0, "hybrid": 0.0})
    out["final"] = horse_race.gate_json(view(gate.evaluate({20: None, 40: None, 60: final}), 60, 180), 3, STAMP)
    return {name: json.loads(json.dumps(doc)) for name, doc in out.items()}


def identity_parts() -> dict[str, str]:
    """Every part of every document, the verdict's new keys removed, by path."""
    found: dict[str, str] = {}
    for name, document in funds_documents().items():
        found |= parts(without_new_keys(document, "funds"), f"funds/{name}")
    for name, document in gate_documents().items():
        found |= parts(without_new_keys(document, "gate"), f"gate/{name}")
    return found


__all__ = ["digest", "funds_documents", "gate_documents", "identity_parts", "parts", "without_new_keys"]


if __name__ == "__main__":
    print(json.dumps(identity_parts(), sort_keys=True))
