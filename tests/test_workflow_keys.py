"""Every keyed source the probe proves is a key the cycle receives.

On 18 Sep the first real cycle showed the model a stated blank for the
energy inventories, the price outlook, the crop condition, the rate path
and the earnings record: the four keys were wired into the data-sources
probe and never into the heartbeat, so a runner proved sources the cycle
could not read. This pins the two lists to each other and to the names
orchestrator/sources.py reads first.
"""

from __future__ import annotations

import fnmatch
import math
import re
from pathlib import Path

import pytest
import yaml

from replay import news_ablation

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
        assert f"secrets.{name}" in step[name], name
    # Each still falls back to what production reads when nothing is named.
    assert "vars.SCREENING_BASE_URL" in step["SCREENING_BASE_URL"]
    assert "vars.SCREENING_MODEL" in step["SCREENING_MODEL"]


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
    # The grading step resolves one key rather than the four spellings the
    # probe is handed, because compare_screening.py reads a single value. It
    # must still fall back to every spelling the cycle would, so a run with
    # no override grades the endpoint production would actually have used.
    cycle = _step("heartbeat.yml", "cycle", "Run one cycle")["env"]
    for name in llm.SCREENING_KEY_ENV_VARS:
        assert f"secrets.{name}" in grade["SCREENING_API_KEY"], name
        assert f"secrets.{name}" in cycle["SCREENING_API_KEY"], name


def test_the_screening_check_can_outlast_the_grading_it_runs():
    """A job timeout sized for the probe silently truncates the recall run.

    The probe is one call. Grading is one call per journal line, sequentially,
    and a hosted endpoint answers in seconds -- so the default 200 lines is
    minutes, not seconds. While this job's timeout was 10 minutes (what the
    probe alone needed) the first grading run was cancelled at 9m29s, one step
    before it printed the number: every call was paid for and nothing learned.

    Derived from compare_screening.py's own default rather than from a number
    typed here, so raising that default without raising the timeout fails
    instead of truncating the next run.
    """
    wf = yaml.safe_load((ROOT / ".github/workflows/screening-check.yml").read_text())
    timeout_s = wf["jobs"]["screening"]["timeout-minutes"] * 60

    default_limit = int(
        re.search(r'"--limit".*?default=(\d+)',
                  (ROOT / "replay/compare_screening.py").read_text(), re.S).group(1)
    )
    # The bound has to be the slowest run the workflow can be asked for, not
    # the typical one: `effort` turns reasoning on, and a reasoning answer is
    # thousands of tokens where the screen's is a hundred. 2.4s measured for a
    # screen-shaped call; 20s is the conservative reasoning case.
    # YAML parses a bare `on:` key as the boolean True, not the string "on".
    triggers = wf.get("on") or wf[True]
    offers_effort = "effort" in (triggers["workflow_dispatch"]["inputs"] or {})
    seconds_per_call = 20 if offers_effort else 5
    setup_s = 120  # checkout, python, pip install, and the probe itself

    needed = default_limit * seconds_per_call + setup_s
    assert timeout_s >= needed, (
        f"timeout-minutes={timeout_s // 60} cannot finish {default_limit} graded "
        f"calls; needs at least {needed // 60} minutes"
    )


def test_the_screen_effort_reaches_the_cycle_too():
    """It changes which tickers reach the full model, so a value set on GitHub
    and never passed to the step would be a setting that looks applied and
    is not -- the same silence this file exists to catch."""
    cycle = _step("heartbeat.yml", "cycle", "Run one cycle")["env"]
    assert "screening_effort" in Settings.model_fields
    assert cycle["SCREENING_EFFORT"] == "${{ vars.SCREENING_EFFORT }}"


def test_the_model_compare_workflow_is_read_only_about_trading():
    """It replays recorded contexts against a candidate. Handing it broker
    credentials would make a measurement tool able to move money."""
    wf = yaml.safe_load((ROOT / ".github/workflows/model-compare.yml").read_text())
    for step in wf["jobs"]["compare"]["steps"]:
        env = step.get("env") or {}
        for name in env:
            assert "ALPACA" not in name.upper(), name
            assert "WEBHOOK" not in name.upper(), name


def test_the_model_compare_workflow_resolves_the_same_candidate_key():
    """One DeepInfra account, one key, whichever spelling it was stored under."""
    step = _step("model-compare.yml", "compare",
                 "Could this answer the question Opus answers")["env"]
    expected = " || ".join("secrets.%s" % n for n in llm.SCREENING_KEY_ENV_VARS)
    assert step["CANDIDATE_KEY"] == "${{ %s }}" % expected


def test_every_comparison_workflow_can_dial_concurrency_down():
    """The failure report tells the reader to lower --concurrency when it
    blames 429s on us. Advice you cannot follow from where you read it is
    not advice."""
    for workflow, job in (("screening-check.yml", "screening"),
                          ("model-compare.yml", "compare"),
                          ("determinism-check.yml", "determinism")):
        wf = yaml.safe_load((ROOT / ".github/workflows" / workflow).read_text())
        triggers = wf.get("on") or wf[True]
        inputs = triggers["workflow_dispatch"]["inputs"] or {}
        assert "concurrency" in inputs, workflow
        run = " ".join(s.get("run", "") for s in wf["jobs"][job]["steps"])
        assert "--concurrency" in run, workflow


def test_the_model_compare_workflow_scores_both_sides():
    """Emitting the pair and never scoring it would leave the question the
    run exists to answer unasked, while looking complete."""
    wf = yaml.safe_load((ROOT / ".github/workflows/model-compare.yml").read_text())
    steps = wf["jobs"]["compare"]["steps"]
    runs = " ".join(s.get("run", "") for s in steps)
    assert "--emit-pairs" in runs
    assert "score_journal.py" in runs
    # The filenames are built in a shell loop, so the sides are what to pin:
    # scoring only one of them answers nothing, since the question is which
    # of the two did better on the contexts where they differed.
    assert "incumbent candidate" in runs or "candidate incumbent" in runs
    assert "compare-$side.jsonl" in runs


def test_the_model_compare_workflow_saves_pairs_for_a_free_later_rescore():
    """--limit takes the most recent recorded contexts, so most lines have not
    aged past the horizon when the run finishes -- the first 400-context run
    scored 5 lines on one side, 1 on the other. Without this, getting a real
    returns verdict later means paying for the same calls twice."""
    wf = yaml.safe_load((ROOT / ".github/workflows/model-compare.yml").read_text())
    steps = wf["jobs"]["compare"]["steps"]
    upload = next(s for s in steps if s.get("uses", "").startswith("actions/upload-artifact"))
    assert upload.get("if") == "always()", "a failed or partial run still has pairs worth keeping"
    assert "pairs.jsonl" in upload["with"]["path"]


def test_replay_never_opens_a_file_for_writing():
    """The CI guardrail enforces this, and it is worth stating why in the
    suite too: compare_models.py runs often and casually while iterating, and
    a path argument aimed at logs/signal_journal.log would destroy the only
    record of what the model actually said. The harness prints; the caller
    stores."""
    import re

    offenders = []
    for path in (ROOT / "replay").rglob("*.py"):
        text = path.read_text(encoding="utf-8")
        if re.search(r'\.write_text\(|open\([^)]*["\'][wa]', text):
            offenders.append(path.name)
    assert not offenders, f"replay/ must not write files: {offenders}"


def test_a_candidate_can_be_graded_without_touching_production_config():
    """Editing the live SCREENING_* variables to run a test is how a screen
    later measured at 5% escalation recall came within hours of deciding real
    trades. A test must be able to name its own endpoint."""
    wf = yaml.safe_load((ROOT / ".github/workflows/screening-check.yml").read_text())
    triggers = wf.get("on") or wf[True]
    inputs = triggers["workflow_dispatch"]["inputs"] or {}
    for name in ("base_url", "model", "key"):
        assert name in inputs, name
        assert inputs[name].get("default") == "", f"{name} must default to production"

    for step in wf["jobs"]["screening"]["steps"]:
        env = step.get("env") or {}
        for setting in ("SCREENING_BASE_URL", "SCREENING_MODEL"):
            if setting in env:
                assert "inputs." + setting.split("SCREENING_")[1].lower() in env[setting], setting
                assert "vars." + setting in env[setting], f"{setting} must still fall back"


def test_naming_a_key_sends_only_that_one():
    """The probe's job is to say WHICH spelling carried the key. Passing all
    of them while a specific one was asked for would send whichever the chain
    prefers and report the wrong name -- against the wrong endpoint."""
    wf = yaml.safe_load((ROOT / ".github/workflows/screening-check.yml").read_text())
    probe = _step("screening-check.yml", "screening",
                  "Is the screening endpoint wired, and does it answer")["env"]
    for name in llm.SCREENING_KEY_ENV_VARS:
        expression = probe[name]
        assert f"inputs.key == '{name}'" in expression, name
        assert "inputs.key == ''" in expression, f"{name} must still pass when none is named"


def test_the_determinism_check_workflow_is_read_only_about_trading():
    """It repeats recorded contexts against one configuration. Handing it
    broker credentials would make a measurement tool able to move money."""
    wf = yaml.safe_load((ROOT / ".github/workflows/determinism-check.yml").read_text())
    for step in wf["jobs"]["determinism"]["steps"]:
        env = step.get("env") or {}
        for name in env:
            assert "ALPACA" not in name.upper(), name
            assert "WEBHOOK" not in name.upper(), name


def test_the_determinism_check_workflow_resolves_the_same_candidate_key():
    """One DeepInfra account, one key, whichever spelling it was stored under
    -- the same chain model-compare.yml resolves, since both may be asked to
    test the same non-Claude candidate."""
    step = _step("determinism-check.yml", "determinism", "Does this model agree with itself")["env"]
    expected = " || ".join("secrets.%s" % n for n in llm.SCREENING_KEY_ENV_VARS)
    assert step["CANDIDATE_KEY"] == "${{ %s }}" % expected


def test_the_determinism_check_can_outlast_the_calls_it_makes():
    """A job timeout sized for the default --limit/--repeats would truncate a
    larger run silently: every call paid for, some of them never counted.

    Derived from determinism_check.py's own defaults rather than a number
    typed here, so raising a default without raising the timeout fails
    instead of truncating the next run.
    """
    wf = yaml.safe_load((ROOT / ".github/workflows/determinism-check.yml").read_text())
    timeout_s = wf["jobs"]["determinism"]["timeout-minutes"] * 60

    text = (ROOT / "replay/determinism_check.py").read_text()
    default_limit = int(re.search(r"DEFAULT_LIMIT\s*=\s*(\d+)", text).group(1))
    default_repeats = int(re.search(r"DEFAULT_REPEATS\s*=\s*(\d+)", text).group(1))
    default_calls = default_limit * default_repeats

    # This job is NOT sequential, and the first version of this test modelled
    # it as if it were: it budgeted 20s per call and ignored --concurrency
    # entirely, which is right for screening-check.yml (one call at a time)
    # and wrong here. It under-estimated the real thing by about 1.6x and
    # passed only because the ceiling happened to be generous -- it would
    # have waved through a configuration that then died mid-run, losing every
    # call already paid for, since the report only prints once all of them
    # are back.
    #
    # Measured on the first real run: 150 calls at concurrency 4 finished in
    # 80 minutes, i.e. ~127s of latency per call spread over 4 workers. 130
    # is that rounded up.
    triggers = wf.get("on") or wf[True]
    inputs = triggers["workflow_dispatch"]["inputs"] or {}
    default_concurrency = max(1, int(inputs["concurrency"]["default"]))
    seconds_per_call = 130
    setup_s = 120

    rounds = math.ceil(default_calls / default_concurrency)
    needed = rounds * seconds_per_call + setup_s
    assert timeout_s >= needed, (
        f"timeout-minutes={timeout_s // 60} cannot finish {default_calls} calls "
        f"({default_limit} contexts x {default_repeats} repeats, {default_concurrency} "
        f"at a time); needs at least {needed // 60} minutes"
    )


def test_the_determinism_check_workflow_can_dial_concurrency_down():
    wf = yaml.safe_load((ROOT / ".github/workflows/determinism-check.yml").read_text())
    triggers = wf.get("on") or wf[True]
    inputs = triggers["workflow_dispatch"]["inputs"] or {}
    assert "concurrency" in inputs
    run = " ".join(s.get("run", "") for s in wf["jobs"]["determinism"]["steps"])
    assert "--concurrency" in run


def test_the_determinism_check_workflow_passes_effort_even_when_blank():
    """A workflow_dispatch text input left blank arrives as '', not absent,
    so the step must still pass --effort with whatever value it has --
    determinism_check.py is what turns '' back into 'no effort asked'
    (tests/test_determinism_check.py pins that half)."""
    run = " ".join(
        s.get("run", "") for s in
        yaml.safe_load((ROOT / ".github/workflows/determinism-check.yml").read_text())
        ["jobs"]["determinism"]["steps"]
    )
    assert "--effort" in run


def test_the_baseline_compare_workflow_needs_no_credentials_at_all():
    """Its whole cost argument is that it needs none: yfinance is
    unauthenticated, the journal is already in the repo, and no model is
    called. A secret wired in here later would quietly make a free, safe
    measurement into something with a bill and a blast radius."""
    text = (ROOT / ".github/workflows/baseline-compare.yml").read_text()
    assert "secrets." not in text, "baseline-compare must stay credential-free"

    wf = yaml.safe_load(text)
    for step in wf["jobs"]["measure"]["steps"]:
        for name in (step.get("env") or {}):
            assert "ALPACA" not in name.upper(), name
            assert "WEBHOOK" not in name.upper(), name
            assert "API_KEY" not in name.upper(), name


def test_the_baseline_compare_workflow_runs_before_it_is_merged():
    """workflow_dispatch does not exist until the file reaches the default
    branch. A measurement whose purpose is to inform a decision about the
    code in its own PR has to be able to run on that PR -- the same
    reasoning correlations.yml states for its own pull_request trigger."""
    wf = yaml.safe_load((ROOT / ".github/workflows/baseline-compare.yml").read_text())
    triggers = wf.get("on") or wf[True]
    assert "pull_request" in triggers
    watched = triggers["pull_request"]["paths"]
    assert "analysis/baseline_compare.py" in watched
    # The thing it actually measures with, not just its own entry point.
    assert "backtest/simulate.py" in watched


def test_the_determinism_check_can_actually_reach_claude():
    """The incumbent is a Claude model, so a self-agreement check that cannot
    ask Claude cannot measure the thing that matters most.

    It could not. base_url defaulted to a DeepInfra URL, and GitHub replaces
    an EMPTY workflow_dispatch input with the declared default rather than
    passing the empty string -- so dispatching base_url="" to mean "ask
    Claude" silently asked DeepInfra for a claude-* model instead, and all
    100 calls of the first real run failed. A choice input cannot collapse
    into a default that way, so the intent rides on that instead.
    """
    wf = yaml.safe_load((ROOT / ".github/workflows/determinism-check.yml").read_text())
    triggers = wf.get("on") or wf[True]
    inputs = triggers["workflow_dispatch"]["inputs"] or {}
    assert "claude" in inputs["provider"]["options"]

    run = " ".join(s.get("run", "") for s in wf["jobs"]["determinism"]["steps"])
    # There must be a path that hands the script an EMPTY --base-url, which
    # is what routes it to the Anthropic provider.
    assert 'BASE_URL=""' in run
    assert '--base-url "$BASE_URL"' in run
    assert "ANTHROPIC_API_KEY" in str(
        _step("determinism-check.yml", "determinism", "Does this model agree with itself")["env"]
    )


def test_the_horse_race_workflow_needs_no_credentials_at_all():
    """The rule arms are pure functions of the journal, yfinance is
    unauthenticated, and no model is called. A key wired in later would
    make a free, safe race into something with a bill -- and would hand an
    arm information the model did not have."""
    text = (ROOT / ".github/workflows/horse-race.yml").read_text()
    assert "secrets." not in text, "horse-race must stay credential-free"

    wf = yaml.safe_load(text)
    for step in wf["jobs"]["race"]["steps"]:
        for name in (step.get("env") or {}):
            assert "ALPACA" not in name.upper(), name
            assert "WEBHOOK" not in name.upper(), name
            assert "API_KEY" not in name.upper(), name


def test_the_horse_race_runs_before_it_is_merged_and_keeps_running_after():
    """Before: workflow_dispatch does not exist until the file is on the
    default branch, so the first race has to fire from its own PR. After: it
    is the 'keep measuring' half of the experiment, so it runs on a schedule
    rather than when someone remembers."""
    wf = yaml.safe_load((ROOT / ".github/workflows/horse-race.yml").read_text())
    triggers = wf.get("on") or wf[True]
    assert "pull_request" in triggers
    watched = triggers["pull_request"]["paths"]
    assert "rules/**" in watched
    assert "analysis/horse_race.py" in watched
    # The arithmetic every arm's trade goes through, not just the entry point.
    assert "backtest/simulate.py" in watched

    crons = [entry["cron"] for entry in triggers["schedule"]]
    assert len(crons) == 1
    # Trading days only, and after both heartbeat crons and the US close, so
    # the day's journal is committed and the day's closing bar exists.
    minute, hour, _, _, dow = crons[0].split()
    assert dow == "1-5"
    assert int(hour) >= 21, "must run after the 20:00/21:00 UTC close"


def test_the_horse_race_is_a_pull_request_check_on_every_arm_source():
    """Each rule module must be able to see its own race before it merges."""
    wf = yaml.safe_load((ROOT / ".github/workflows/horse-race.yml").read_text())
    triggers = wf.get("on") or wf[True]
    watched = triggers["pull_request"]["paths"]
    for path in (ROOT / "rules").glob("*.py"):
        assert any(
            fnmatch.fnmatch(f"rules/{path.name}", pattern) for pattern in watched
        ), f"a change to {path.name} would not run the race"


def test_the_news_ablation_workflow_is_read_only_about_trading():
    """It asks the full model about recorded contexts. Handing it broker
    credentials would make a measurement tool able to move money."""
    wf = yaml.safe_load((ROOT / ".github/workflows/news-ablation.yml").read_text())
    for step in wf["jobs"]["ablate"]["steps"]:
        for name in (step.get("env") or {}):
            assert "ALPACA" not in name.upper(), name
            assert "WEBHOOK" not in name.upper(), name


def test_the_news_ablation_costs_money_so_it_never_runs_on_a_schedule():
    """The only workflow here that asks the FULL model rather than reading
    the journal. A cron on it would spend real money every night with nobody
    having asked a question."""
    wf = yaml.safe_load((ROOT / ".github/workflows/news-ablation.yml").read_text())
    triggers = wf.get("on") or wf[True]
    assert set(triggers) == {"workflow_dispatch"}


def test_the_news_ablation_keeps_the_record_stream_off_the_report():
    """stdout is split into journal lines by a later step; a human report
    mixed into it would corrupt the split."""
    step = _step("news-ablation.yml", "ablate", "Ask each context with the news and without it")
    assert "--emit-pairs" in step["run"]
    assert '> "$RUNNER_TEMP/pairs.jsonl" 2> "$RUNNER_TEMP/ablation.txt"' in step["run"]


def test_the_news_ablation_resolves_the_same_candidate_key():
    """One account, one key, whichever spelling it was stored under -- the
    same chain determinism-check.yml and model-compare.yml resolve, since
    all three may be pointed at the same non-Claude candidate."""
    step = _step("news-ablation.yml", "ablate", "Ask each context with the news and without it")
    expected = " || ".join("secrets.%s" % n for n in llm.SCREENING_KEY_ENV_VARS)
    assert step["env"]["CANDIDATE_KEY"] == "${{ %s }}" % expected


def test_the_news_ablation_asks_claude_without_a_base_url():
    """An empty workflow_dispatch input is replaced by its declared default,
    so base_url="" could never mean 'ask Claude'. The provider choice
    carries that intent, exactly as determinism-check.yml learned to."""
    wf = yaml.safe_load((ROOT / ".github/workflows/news-ablation.yml").read_text())
    inputs = (wf.get("on") or wf[True])["workflow_dispatch"]["inputs"]
    assert inputs["provider"]["default"] == "claude"
    assert set(inputs["provider"]["options"]) == {"claude", "openai-compatible"}

    run = _step("news-ablation.yml", "ablate", "Ask each context with the news and without it")["run"]
    assert "--base-url" in run
    assert "inputs.provider" in run and '!= \'claude\'' not in run


def test_the_news_ablation_defaults_to_measuring_its_own_noise_floor():
    """Without the repeat arm the floor falls back to the journalled answer,
    which a funnel wrote with a mix of models -- and for a candidate the
    journal never ran there is no floor at all."""
    wf = yaml.safe_load((ROOT / ".github/workflows/news-ablation.yml").read_text())
    inputs = (wf.get("on") or wf[True])["workflow_dispatch"]["inputs"]
    assert inputs["repeat_with_news"]["default"] is True

    run = _step("news-ablation.yml", "ablate", "Ask each context with the news and without it")["run"]
    assert "--repeat-with-news" in run


def test_the_news_ablation_can_outlast_the_calls_it_makes():
    """Every call is paid for whether or not it is counted, so a timeout
    sized under the default sample would burn money for a truncated answer.

    Derived from the script's own default rather than a number typed here,
    so raising the default without raising the timeout fails this test.
    """
    wf = yaml.safe_load((ROOT / ".github/workflows/news-ablation.yml").read_text())
    calls = news_ablation.DEFAULT_LIMIT * 3   # the repeat arm is on by default
    # Measured: 100 sequential Opus calls at low effort took ~15 minutes.
    seconds_per_call = 9
    minutes = math.ceil(calls * seconds_per_call / 60)
    assert wf["jobs"]["ablate"]["timeout-minutes"] >= minutes * 2, (
        f"{calls} calls need about {minutes} minutes; leave room for a slower model"
    )


def test_the_rescore_workflow_calls_no_model_and_holds_no_key():
    """It re-reads answers that were already paid for. A key wired in here
    would turn a free re-read into a second bill for the same calls -- and
    the whole reason this workflow exists is not to pay twice."""
    text = (ROOT / ".github/workflows/rescore-pairs.yml").read_text()
    assert "secrets." not in text, "rescore-pairs must stay credential-free"

    wf = yaml.safe_load(text)
    # The only token is the run's own read-only GITHUB_TOKEN, which is what
    # lets one run read another run's artifact.
    assert wf["permissions"] == {"contents": "read", "actions": "read"}
    for step in wf["jobs"]["rescore"]["steps"]:
        for name in (step.get("env") or {}):
            assert "ALPACA" not in name.upper(), name
            assert "WEBHOOK" not in name.upper(), name
            assert "API_KEY" not in name.upper(), name


def test_the_rescore_workflow_reads_the_shape_both_producers_write():
    """news-ablation and model-compare both emit {"_side", "line"} records
    and both keep them for 90 days. If either stops, this stops working."""
    for name in ("news-ablation.yml", "model-compare.yml"):
        wf = yaml.safe_load((ROOT / f".github/workflows/{name}").read_text())
        job = next(iter(wf["jobs"].values()))
        saved = [s for s in job["steps"] if "upload-artifact" in str(s.get("uses", ""))]
        assert saved, f"{name} no longer saves its pairs"
        assert saved[0]["with"]["retention-days"] == 90
        assert "pairs" in saved[0]["with"]["name"]


def _rescore_splitter() -> str:
    """The python heredoc the workflow runs, lifted out so it can be tested."""
    run = _step("rescore-pairs.yml", "rescore", "Score each side against what the market did")["run"]
    # YAML strips the block scalar's common indentation before bash -- and
    # before this -- so the heredoc arrives already at column zero.
    return run.split("python - <<'SPLIT'\n", 1)[1].split("\nSPLIT", 1)[0]


def test_the_rescore_splitter_refuses_a_side_name_that_is_a_path(tmp_path, monkeypatch):
    """The side name comes out of a downloaded artifact, so it is data. Used
    unchecked it is the filename the splitter opens for writing, and an
    artifact naming a side '../../analysis/score_journal' would have this
    workflow overwrite the repository it is scoring with."""
    pairs = tmp_path / "pairs"
    pairs.mkdir()
    (pairs / "pairs.jsonl").write_text(
        '{"_side": "../../../etc/passwd", "line": {"ticker": "SPY"}}\n'
    )
    monkeypatch.setenv("RUNNER_TEMP", str(tmp_path))
    with pytest.raises(SystemExit) as raised:
        exec(compile(_rescore_splitter(), "<splitter>", "exec"), {"__name__": "__main__"})
    assert "refusing side name" in str(raised.value)


def test_the_rescore_splitter_writes_one_file_per_side(tmp_path, monkeypatch):
    """Both producers' artifacts are read the same way, and the side names
    are discovered rather than listed here: the ablation writes with-news
    and without-news, model compare writes candidate and incumbent."""
    pairs = tmp_path / "pairs"
    pairs.mkdir()
    (pairs / "pairs.jsonl").write_text(
        '{"_side": "with-news", "line": {"ticker": "SPY"}}\n'
        "\n"
        '{"_side": "without-news", "line": {"ticker": "SPY"}}\n'
        '{"_side": "with-news", "line": {"ticker": "QQQ"}}\n'
    )
    monkeypatch.setenv("RUNNER_TEMP", str(tmp_path))
    exec(compile(_rescore_splitter(), "<splitter>", "exec"), {"__name__": "__main__"})
    assert (tmp_path / "sides.txt").read_text().split() == ["with-news", "without-news"]
    assert (tmp_path / "side-with-news.jsonl").read_text().count("\n") == 2
    assert (tmp_path / "side-without-news.jsonl").read_text().count("\n") == 1


def test_the_cycle_is_handed_the_full_model_s_key():
    """A secret that is never passed to the step is a secret the cycle cannot
    read -- the lesson that left four source keys unused until 18 September.

    It costs more here than it did there. An unreadable screening key only
    loses the saving; an unreadable full-model key fails every ticker's model
    stage, because the screen that used to stand behind a failure is off.
    """
    cycle = _step("heartbeat.yml", "cycle", "Run one cycle")["env"]
    assert "FULL_MODEL_API_KEY" in cycle
    assert "full_model_api_key" in Settings.model_fields


def test_the_full_model_key_accepts_the_names_it_may_already_be_stored_under():
    """Same collapsing chain as the screen, for the same reason: a key stored
    under the name it was first pasted in as is otherwise silent."""
    cycle = _step("heartbeat.yml", "cycle", "Run one cycle")["env"]
    for name in ("FULL_MODEL_API_KEY", "DEEPINFRA_API_KEY", *llm.SCREENING_KEY_ENV_VARS):
        assert f"secrets.{name}" in cycle["FULL_MODEL_API_KEY"], name


def test_the_cycle_can_outlast_the_calls_it_has_to_make():
    """There is no batch on an OpenAI-compatible endpoint, so the full-model
    stage is the whole watchlist asked live. Its worst case is arithmetic --
    rounds times the per-call ceiling -- and it has to fit the job's clock
    alongside the context gathering, or the cycle is killed having traded
    nothing and recorded nothing.

    Derived from the constants rather than typed here, so widening the
    watchlist, lengthening the timeout or narrowing the concurrency fails
    this test instead of failing a cycle.
    """
    import math

    from config import settings as _cfg

    if not llm.MODEL_BASE_URL:
        pytest.skip("the Anthropic path batches; BATCH_DEADLINE_SECONDS sizes it instead")

    # The bound is the stage's own budget, not rounds times the per-call
    # ceiling. That arithmetic came to 100 minutes, was used to argue a
    # timed-out call could not be asked again, and described a cycle that
    # would already be broken: the measured stage on 23 September took 32
    # minutes and lost three tickers to the retry it forbade.
    budget_minutes = _cfg.FULL_MODEL_STAGE_BUDGET_SECONDS / 60
    # Measured on 18-22 September: the cycle spends about 42 minutes gathering
    # context before it asks anything.
    gathering = 42

    wf = yaml.safe_load((ROOT / ".github/workflows/heartbeat.yml").read_text())
    clock = wf["jobs"]["cycle"]["timeout-minutes"]
    assert clock >= budget_minutes + gathering, (
        f"a {budget_minutes:.0f} min full-model budget plus ~{gathering} min "
        f"gathering context does not fit a {clock} min clock"
    )

    # And the budget has to be worth having: a single ticker's worst case
    # must fit inside it several times over, or one slow name spends the lot.
    worst_call = llm.FULL_MODEL_TIMEOUT_SECONDS + llm.TRANSPORT_RETRY_TIMEOUT_SECONDS
    names = len([t for t in _cfg.get_settings().watchlist.split(",") if t.strip()])
    rounds = math.ceil(names / _cfg.FULL_MODEL_MAX_CONCURRENCY)
    assert _cfg.FULL_MODEL_STAGE_BUDGET_SECONDS >= 2 * worst_call, (
        f"a {budget_minutes:.0f} min budget is too tight for a {worst_call:.0f}s "
        f"worst-case call over {rounds} rounds"
    )
