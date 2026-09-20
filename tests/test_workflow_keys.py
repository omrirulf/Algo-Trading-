"""Every keyed source the probe proves is a key the cycle receives.

On 18 Sep the first real cycle showed the model a stated blank for the
energy inventories, the price outlook, the crop condition, the rate path
and the earnings record: the four keys were wired into the data-sources
probe and never into the heartbeat, so a runner proved sources the cycle
could not read. This pins the two lists to each other and to the names
orchestrator/sources.py reads first.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from config.settings import Settings
from orchestrator import llm, sources

ROOT = Path(__file__).resolve().parents[1]


def _step(workflow: str, job: str, name: str) -> dict:
    wf = yaml.safe_load((ROOT / ".github/workflows" / workflow).read_text())
    return next(s for s in wf["jobs"][job]["steps"] if s.get("name") == name)


def test_the_cycle_receives_every_keyed_source_the_probe_does():
    cycle = _step("heartbeat.yml", "cycle", "Run one cycle")["env"]
    first_names = {spellings[0] for spellings in sources.KEY_ENV_VARS.values()}
    assert first_names == {"EIA_API_KEY", "USDA_NASS_KEY", "FRED_API_KEY", "FINNHUB_API_KEY"}
    for name in first_names:
        assert cycle.get(name) == "${{ secrets.%s }}" % name, name


def test_the_probe_and_the_cycle_name_the_same_secrets():
    wf = yaml.safe_load((ROOT / ".github/workflows/data-sources.yml").read_text())
    probe_names = set()
    for step in wf["jobs"]["probe"]["steps"]:
        for k, v in (step.get("env") or {}).items():
            if isinstance(v, str) and v.startswith("${{ secrets.") and k != "NTFY_TOPIC":
                probe_names.add(k)
    # The probe's first step also passes every alternative spelling, to say
    # which one carries a key stored under another name; the cycle needs
    # only the canonical four, and the probe must prove exactly those.
    first_names = {spellings[0] for spellings in sources.KEY_ENV_VARS.values()}
    assert first_names <= probe_names
    cycle = _step("heartbeat.yml", "cycle", "Run one cycle")["env"]
    for name in first_names:
        assert name in cycle, f"{name} is proven by the probe but never reaches the cycle"


def test_the_cycle_receives_the_screening_endpoint_settings():
    """A screening endpoint set only as a secret would never be read.

    settings.py names the three fields; the scheduled cycle is the only
    place they matter, and a field that is never passed to the step is a
    field the cycle sees blank -- the 18 Sep failure again, one funnel
    stage further down.
    """
    cycle = _step("heartbeat.yml", "cycle", "Run one cycle")["env"]
    for field in ("screening_base_url", "screening_model", "screening_api_key"):
        assert field in Settings.model_fields, field
        assert field.upper() in cycle, f"{field} is configurable but never reaches the cycle"


def test_every_screening_key_spelling_reaches_the_canonical_name():
    """A key under a name nothing reads is the same as no key.

    GEMINI_API_KEY is the obvious thing to call a Gemini key, and nothing in
    the code reads it: the cycle reads SCREENING_API_KEY only. The workflow
    collapses the alternatives onto that one name, and this pins the chain to
    the tuple, so adding a spelling to llm.py without wiring it fails here.
    """
    cycle = _step("heartbeat.yml", "cycle", "Run one cycle")["env"]
    expected = " || ".join("secrets.%s" % n for n in llm.SCREENING_KEY_ENV_VARS)
    assert cycle["SCREENING_API_KEY"] == "${{ %s }}" % expected


def test_the_screening_probe_is_offered_every_spelling_separately():
    """The probe's job is to say which name carried the key, so it cannot be
    handed the collapsed value -- it needs them one by one."""
    step = _step("screening-check.yml", "screening",
                 "Is the screening endpoint wired, and does it answer")["env"]
    for name in llm.SCREENING_KEY_ENV_VARS:
        assert step[name] == "${{ secrets.%s }}" % name, name
    assert step["SCREENING_BASE_URL"] == "${{ vars.SCREENING_BASE_URL }}"
    assert step["SCREENING_MODEL"] == "${{ vars.SCREENING_MODEL }}"


def test_the_canonical_spelling_is_the_field_settings_declares():
    assert llm.SCREENING_KEY_ENV_VARS[0].lower() in Settings.model_fields
    assert llm.SCREENING_KEY_ENV_VARS[0] == "SCREENING_API_KEY"


def test_the_recall_grading_step_gets_the_same_endpoint_the_probe_does():
    """Grading a different endpoint than the one the cycle would use makes
    the verdict meaningless, and the failure is invisible -- it still prints
    a number."""
    probe = _step("screening-check.yml", "screening",
                  "Is the screening endpoint wired, and does it answer")["env"]
    grade = _step("screening-check.yml", "screening",
                  "Does it agree with the screen it would replace")["env"]
    assert grade["SCREENING_BASE_URL"] == probe["SCREENING_BASE_URL"]
    assert grade["SCREENING_MODEL"] == probe["SCREENING_MODEL"]
    cycle = _step("heartbeat.yml", "cycle", "Run one cycle")["env"]
    assert grade["SCREENING_API_KEY"] == cycle["SCREENING_API_KEY"], (
        "the graded key must be the one the cycle resolves, spellings included"
    )
