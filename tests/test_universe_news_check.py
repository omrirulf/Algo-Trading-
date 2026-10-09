"""The universe news check: does the universe's own query find the company? (The owner, 3 Oct 2026.)"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "universe-news-check.yml"


def _workflow() -> dict:
    return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))


def _script() -> str:
    return _workflow()["jobs"]["check"]["steps"][-1]["run"]


def test_it_asks_every_name_with_the_universe_query_and_counts_by_code():
    """All 251 names (the replacements included), the universe's own search, the code-only rule."""
    script = _script()
    assert "from config.shadow_universe import CANDIDATES, REPLACED, TICKERS, news_query" in script
    assert "pool.map(ask, names)" in script and "if only else list(TICKERS)" in script
    assert "from orchestrator.universe_news import fetch" in script
    assert "fetch_news" not in script and "heartbeat" not in script   # not production's search
    assert "from analysis.news_relevance import FAIL_BELOW, report, universe_share" in script
    for word in ("llm", "anthropic", "call_llm", "model"):
        assert word not in script.lower().replace("no model", ""), word
    # The share per name, the names under 30%, the overall share: report() writes all three.
    assert "report(shares" in script and "GITHUB_STEP_SUMMARY" in script


def test_it_runs_on_a_trading_day_by_hand_or_by_label_and_keeps_nothing():
    text = WORKFLOW.read_text(encoding="utf-8")
    wf = _workflow()
    triggers = wf.get("on") or wf[True]
    assert set(triggers) == {"workflow_dispatch", "pull_request"}
    assert triggers["pull_request"] == {"types": ["labeled"]}
    assert wf["jobs"]["check"]["if"] == ("${{ github.event_name == 'workflow_dispatch' || "
                                         "github.event.label.name == 'universe-news-check' }}")
    assert "if not is_trading_day(today):" in _script()
    assert wf["permissions"] == {"contents": "read"}
    for word in ("git push", "git commit", "upload-artifact", "ALPACA", "ANTHROPIC", "SUPABASE", "NTFY"):
        assert word not in text, word


def test_it_holds_only_the_news_key_and_zone_the_cycle_uses():
    text = WORKFLOW.read_text(encoding="utf-8")
    assert set(re.findall(r"secrets\.([A-Z_]+)", text)) == {"BRIGHTDATA_API_TOKEN"}
    env = _workflow()["jobs"]["check"]["steps"][-1]["env"]
    assert {k: v for k, v in env.items() if k != "ONLY_NAMES"} == {
        "BRIGHTDATA_API_KEY": "${{ secrets.BRIGHTDATA_API_TOKEN }}",
        "BRIGHTDATA_UNLOCKER_ZONE": "${{ vars.BRIGHTDATA_SERP_ZONE || 'cli_unlocker' }}"}


def test_a_failed_search_is_asked_again_and_never_counted_as_irrelevant():
    """5 Oct 2026: Bright Data answered many requests with an empty body; a broken request is not a finding."""
    script = _script()
    assert "max_workers=2" in script and "for _round in range(3):" in script and "time.sleep(60)" in script
    assert "shares = [universe_share(t, found[t][0]) for t in names if t not in broken]" in script
    assert 'print("FAILED " + json.dumps(broken))' in script
    # ONLY_NAMES lists names of the list only; an unknown ticker stops the check. By hand it comes from the
    # run's input (a same-day recheck), through the environment, never pasted into the script.
    assert 'sys.exit(f"not in the list:' in script
    env = _workflow()["jobs"]["check"]["steps"][-1]["env"]
    assert env["ONLY_NAMES"] == "${{ inputs.only || '' }}" and "inputs.only" not in script


def test_by_hand_it_can_run_the_universes_own_news_step_instead():
    """The owner, 6 Oct 2026: once in the week of 14 Dec, every name's search as the universe makes it."""
    wf = _workflow()
    triggers = wf.get("on") or wf[True]
    assert triggers["workflow_dispatch"]["inputs"]["mode"]["options"] == ["relevance", "news-step"]
    steps = {s.get("name"): s for s in wf["jobs"]["check"]["steps"]}
    step = steps["The universe's own news step, every name"]
    assert step["if"] == "${{ inputs.mode == 'news-step' }}"
    assert steps["How relevant is each name's news?"]["if"] == "${{ inputs.mode != 'news-step' }}"
    script = step["run"]
    assert "news_step(TICKERS, WORKERS)" in script and "from orchestrator.universe import WORKERS" in script
    assert "if not is_trading_day(today):" in script and 'print("NEWS_STEP " + json.dumps(found))' in script
    for word in ("llm", "anthropic", "call_llm", "journal"):
        assert word not in script.lower(), word
    assert step["env"] == {"BRIGHTDATA_API_KEY": "${{ secrets.BRIGHTDATA_API_TOKEN }}",
                           "BRIGHTDATA_UNLOCKER_ZONE": "${{ vars.BRIGHTDATA_SERP_ZONE || 'cli_unlocker' }}"}


def test_a_candidate_replacement_is_asked_only_by_name_and_has_time_to_finish():
    """Card rule (2), Amendment 2026-10-06: a replacement passes the news check on a weekday before it joins."""
    script = _script()
    assert "unknown = sorted(set(only) - set(TICKERS) - set(CANDIDATES))" in script
    assert "names = [t for t in (*TICKERS, *CANDIDATES) if t in only] if only else list(TICKERS)" in script
    assert _workflow()["jobs"]["check"]["timeout-minutes"] == 180
