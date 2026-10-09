"""The output identity check: the owner's condition for merging while calibration runs (6 Oct 2026).

"Show that the funds' output and the calibration copy's output are byte-identical before and after this PR,
on the same prices and journal, like the journal-split check. If anything differs, tell me what and why."
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "output-identity-check.yml"
FUNDS = ROOT / ".github" / "workflows" / "funds.yml"


def _workflow() -> dict:
    return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))


def _text() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def test_it_runs_by_label_or_by_hand_holds_no_credential_and_keeps_nothing():
    wf = _workflow()
    triggers = wf.get("on") or wf[True]
    assert set(triggers) == {"workflow_dispatch", "pull_request"}
    assert "output-identity-check" in wf["jobs"]["compare"]["if"]
    assert wf["permissions"] == {"contents": "read"}
    text = _text()
    assert "secrets." not in text
    for word in ("git push", "git commit", "upload-artifact", "ALPACA", "ANTHROPIC", "SUPABASE", "NTFY", "BRIGHTDATA"):
        assert word not in text, word


def test_both_sides_read_the_same_journal_prices_and_clock():
    text = _text()
    assert 'before=$(git rev-parse HEAD^1)' in text            # the base as the merge would land on it
    assert 'git diff --quiet "$before" HEAD -- logs/' in text  # the same logs/, or no comparison
    assert 'tape[key] = original_history(self, *args, **kwargs)' in text
    assert 'module._now = lambda: frozen' in text and 'FROZEN_NOW' in text
    assert _workflow()["jobs"]["compare"]["env"] == {"PYTHONHASHSEED": "0"}


def test_the_funds_run_as_the_nightly_workflow_runs_them_both_ways():
    text = _text()
    # Before and after-same with the before side's funds.yml, so only the code differs; after-production
    # with the after side's own funds.yml (6 Oct 2026, PR #142: each command line is read from its funds.yml).
    assert 'side.sh" "$RUNNER_TEMP/before" before "$RUNNER_TEMP/before/.github/workflows/funds.yml"' in text
    assert 'side.sh" "$GITHUB_WORKSPACE" after-same "$RUNNER_TEMP/before/.github/workflows/funds.yml"' in text
    assert 'side.sh" "$GITHUB_WORKSPACE" after-production "$GITHUB_WORKSPACE/.github/workflows/funds.yml"' in text
    assert ("shadow.run --processes 1 --random 1000 --with-prices \\\n"
            '            --race-gate "$out/gate.json" --previous logs/funds.json "${extra[@]}"') in text
    funds = FUNDS.read_text(encoding="utf-8")
    for argument in ("--with-prices", "--race-gate", "--previous logs/funds.json", "--fx-table",
                     "--universe logs/shadow_universe", "--votes logs/model_vote", "--thesis logs/thesis_check"):
        assert argument in funds, argument
    for argument in ("--universe logs/shadow_universe", "--votes logs/model_vote", "--thesis logs/thesis_check"):
        assert f"extra+=({argument})" in text, argument
    assert "analysis.boi_rates --start 2026-09-10" in text and "analysis.boi_rates --start 2026-09-10" in funds
    # One rate table, fetched once, given to every side.
    assert 'fx="$RUNNER_TEMP/out/fx-rates.json"' in text and 'extra+=(--fx-table "$fx")' in text


def _flags(tmp_path: Path, workflow: Path) -> "subprocess.CompletedProcess[str]":
    """Run side.sh's own flag reading, as the job writes it, on ``workflow``."""
    import os
    import subprocess
    import sys

    step = next(s for s in _workflow()["jobs"]["compare"]["steps"]
                if s.get("name") == "Write the price tape and the side runner")
    env = dict(os.environ, RUNNER_TEMP=str(tmp_path),
               PATH=f"{Path(sys.executable).parent}{os.pathsep}{os.environ.get('PATH', '')}")
    subprocess.run(["bash", "-e", "-c", step["run"]], env=env, check=True, capture_output=True, text=True)
    side = (tmp_path / "side.sh").read_text(encoding="utf-8")
    block = side[side.index("# The flags of funds.yml"):side.index("has() {")]
    script = f"set -euo pipefail\nlabel=test workflow={str(workflow)!r}\n{block}echo \"FLAGS: $flags\"\n"
    return subprocess.run(["bash", "-c", script], env=env, capture_output=True, text=True)


def test_the_command_line_is_read_from_funds_yml_and_an_unknown_flag_fails_the_job(tmp_path):
    import re as _re

    seen = _flags(tmp_path, FUNDS)
    assert seen.returncode == 0, seen.stderr
    flags = seen.stdout.split("FLAGS: ", 1)[1].split()
    # The command itself (the file's header names it too, in a comment, before it).
    command = FUNDS.read_text(encoding="utf-8").rsplit("python -m shadow.run", 1)[1].split(">", 1)[0]
    assert flags == _re.findall(r"(?<!\S)--[a-z][a-z-]*", command)
    assert flags == ["--processes", "--random", "--with-prices", "--race-gate", "--previous", "--fx-table",
                     "--universe", "--votes", "--thesis"]
    odd = tmp_path / "odd.yml"
    odd.write_text("x:\n  run: |\n    python -m shadow.run --random 1 \\\n      --a-new-flag x\n", encoding="utf-8")
    (tmp_path / "again").mkdir()
    refused = _flags(tmp_path / "again", odd)
    assert refused.returncode == 1 and "--a-new-flag" in refused.stdout and "FLAGS:" not in refused.stdout


def test_it_fails_on_any_change_to_calibration_or_to_a_value_the_funds_had():
    text = _text()
    assert "`calibration` (the calibration copy): **byte-identical**" in text
    assert 'failures.append(f"{label}: the calibration copy\'s output differs")' in text
    assert re.search(r'if keys != \("prices_sha256",\):\n\s+failures\.append', text)
    assert "sys.exit(1 if failures else 0)" in text
    # Added keys are listed, and the rest checked byte for byte without them. A price table's fetch-time
    # stamps (the wall clock when the fetcher ran) are set aside and counted, never a price; its rows are
    # compared as a set, so a bar that is new or gone is named.
    assert 'f" Without {taken}, the rest is **byte-identical** to before."' in text
    assert 'return bool(keys) and keys[-1] == "fetched_at" and "coverage" in keys' in text
    assert 'keys[-1] == "rows"' in text
