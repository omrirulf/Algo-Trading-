"""The universe news check: does "<ticker> stock" find the company? (The card's rule (2), 3 Oct 2026.)"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from config import shadow_universe as su

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "universe-news-check.yml"


def test_it_checks_every_replacement_and_the_common_word_tickers():
    text = WORKFLOW.read_text(encoding="utf-8")
    checked = set(re.findall(r'"([A-Z]{1,5})": r"', text))
    replacements = {new for new, _ in su.REPLACED.values()}
    common_words = {"ICE", "NOW", "SO", "ED", "O", "T", "V", "C", "F", "D"}
    assert replacements | common_words <= checked


def test_it_holds_only_the_news_token_and_commits_nothing():
    text = WORKFLOW.read_text(encoding="utf-8")
    wf = yaml.safe_load(text)
    triggers = wf.get("on") or wf[True]
    assert set(triggers) == {"workflow_dispatch", "pull_request"}
    assert triggers["pull_request"] == {"paths": [".github/workflows/universe-news-check.yml"]}
    assert wf["permissions"] == {"contents": "read"}
    assert set(re.findall(r"secrets\.([A-Z_]+)", text)) == {"BRIGHTDATA_API_TOKEN"}
    for word in ("git push", "git commit", "upload-artifact", "ALPACA", "API_KEY", "SUPABASE"):
        assert word not in text, word
    assert "from orchestrator.heartbeat import fetch_news" in text   # production's own search
