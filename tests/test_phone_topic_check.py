"""The phone topic check: long and random, judged without ever printing the topic (the owner, 3 Oct 2026)."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "phone-topic-check.yml"


def _workflow() -> dict:
    return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))


def _script() -> str:
    run = _workflow()["jobs"]["check"]["steps"][0]["run"]
    start = run.index("<<'EOF'\n") + len("<<'EOF'\n")
    return run[start:run.index("\nEOF", start)]


def _check(topic: str) -> str:
    env = {k: v for k, v in os.environ.items() if k != "NTFY_TOPIC"} | {"NTFY_TOPIC": topic}
    return subprocess.run([sys.executable, "-"], input=_script(), capture_output=True, text=True,
                          env=env, check=True).stdout


def test_a_long_random_topic_passes_and_is_never_printed():
    topic = "algo-desk-k7Qx2mPz9wLr4Tb"
    out = _check(topic)
    assert "The phone topic looks long and random." in out and "::warning::" not in out
    assert topic not in out and "k7Qx" not in out and str(len(topic)) not in out


def test_the_docs_example_shape_passes():
    # docs/phone.mdx: "algo-desk-" followed by twelve letters and digits.
    assert "looks long and random" in _check("algo-desk-a8f3k29dm4q7")


def test_weak_topics_are_warned_about_without_saying_which_test_failed():
    for weak in ("algotrading", "algo-desk-alerts", "algo-desk-123456789012", "mytopicmytopicmytopic",
                 "algo-desk-aaaaaaaaaaa1", "algo.desk.k7Qx2mPz9wLr4Tb!", "algo-desk-" + "k7Qx2mPz9w" * 7):
        out = _check(weak)
        assert "::warning::The phone topic does not look long and random" in out, weak
        assert weak not in out and "yes " not in out and "NO" not in out, weak   # the log is public


def test_an_unset_topic_says_so():
    assert "NTFY_TOPIC is not set" in _check("")


def test_the_workflow_holds_only_the_topic_and_commits_nothing():
    text = WORKFLOW.read_text(encoding="utf-8")
    wf = _workflow()
    triggers = wf.get("on") or wf[True]
    assert set(triggers) == {"workflow_dispatch", "pull_request"}
    assert wf["permissions"] == {"contents": "read"}
    assert set(re.findall(r"secrets\.([A-Z_]+)", text)) == {"NTFY_TOPIC"}
    for word in ("curl", "ntfy.sh/", "git push", "upload-artifact", "print(topic", "len(topic))"):
        assert word not in text, word
