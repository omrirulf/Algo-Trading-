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
    assert "from config.shadow_universe import REPLACED, TICKERS, news_query" in script
    assert "pool.map(ask, TICKERS)" in script
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
    assert env == {"BRIGHTDATA_API_KEY": "${{ secrets.BRIGHTDATA_API_TOKEN }}",
                   "BRIGHTDATA_UNLOCKER_ZONE": "${{ vars.BRIGHTDATA_SERP_ZONE || 'cli_unlocker' }}"}
