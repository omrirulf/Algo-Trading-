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
    assert "side.sh\" \"$RUNNER_TEMP/before\" before same" in text
    assert "side.sh\" \"$GITHUB_WORKSPACE\" after-same same" in text
    assert "side.sh\" \"$GITHUB_WORKSPACE\" after-production production" in text
    # The before side's command line is the nightly one without the new arguments; the production
    # side adds exactly what funds.yml adds.
    assert ("shadow.run --processes 1 --random 1000 --with-prices \\\n"
            '            --race-gate "$out/gate.json" --previous logs/funds.json "${extra[@]}"') in text
    assert 'extra=(--fx-table "$out/fx-rates.json" --universe logs/shadow_universe)' in text
    funds = FUNDS.read_text(encoding="utf-8")
    for argument in ("--with-prices", "--race-gate", "--previous logs/funds.json", "--fx-table",
                     "--universe logs/shadow_universe"):
        assert argument in funds, argument
    assert "analysis.boi_rates --start 2026-09-10" in text and "analysis.boi_rates --start 2026-09-10" in funds


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
