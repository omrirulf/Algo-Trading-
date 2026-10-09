"""The dashboard pages are built from their templates and the snapshots."""

from __future__ import annotations

import importlib.util
import json
import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def test_the_template_carries_the_placeholder_and_reads_the_live_file():
    text = (ROOT / "dashboard" / "template.html").read_text()
    assert "/*__SEED__*/{}" in text
    assert '"logs/book.json"' in text and "raw.githubusercontent.com" in text
    assert "<title>Algo Trading Desk</title>" in text
    # No key, no connector, no Claude runtime: the page reads a public file.
    assert "window.claude" not in text and "get_file_contents" not in text


def test_the_page_is_installable_and_survives_offline():
    text = (ROOT / "dashboard" / "template.html").read_text()
    assert '<link rel="manifest" href="manifest.webmanifest">' in text
    assert 'serviceWorker.register("sw.js")' in text
    assert '<meta name="viewport"' in text
    assert "localStorage" in text                       # the last good copy stays on the phone
    manifest = json.loads((ROOT / "dashboard" / "manifest.webmanifest").read_text())
    assert manifest["display"] == "standalone" and manifest["start_url"] == "./"
    for icon in manifest["icons"]:
        assert (ROOT / "dashboard" / icon["src"]).exists(), icon["src"]
    sw = (ROOT / "dashboard" / "sw.js").read_text()
    assert "caches.match" in sw and "fetch(event.request)" in sw


def test_the_site_build_writes_the_page_and_everything_beside_it(tmp_path):
    book = tmp_path / "book.json"
    book.write_text(json.dumps({"day": "2026-09-17", "positions": []}))
    site = tmp_path / "site"
    subprocess.run([sys.executable, str(ROOT / "dashboard" / "build.py"), "--book", str(book), "--site", str(site)],
                   check=True, capture_output=True)
    names = sorted(p.name for p in site.iterdir())
    assert names == ["funds.html", "icon-192.png", "icon-512.png", "icon.svg", "index.html", "manifest.webmanifest", "sw.js"]
    assert '/*__SEED__*/{"day":"2026-09-17"' in (site / "index.html").read_text()
    assert (site / "icon-192.png").read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"


def test_the_pages_workflow_deploys_the_site_after_every_snapshot():
    import yaml

    wf = yaml.safe_load((ROOT / ".github/workflows/pages.yml").read_text())
    on = wf[True] if True in wf else wf["on"]          # PyYAML reads the bare key `on` as True
    assert "logs/book.json" in on["push"]["paths"] and "dashboard/**" in on["push"]["paths"]
    job = wf["jobs"]["deploy"]
    assert wf["permissions"] == {"contents": "write"}
    runs = [s.get("run", "") for s in job["steps"]]
    assert any("bash dashboard/publish.sh" in r for r in runs)
    script = (ROOT / "dashboard" / "publish.sh").read_text()
    assert "dashboard/build.py --site" in script
    assert "git init -q -b gh-pages" in script and "touch .nojekyll" in script   # one commit, rewritten each time
    assert "${GH_TOKEN}" in script and "echo" not in script.split("git push")[1].split("\n")[0]
    assert "set -euo pipefail" in script


def test_the_build_embeds_the_snapshot_and_escapes_a_closing_tag(tmp_path):
    book = tmp_path / "book.json"
    book.write_text(json.dumps({"day": "2026-09-17", "positions": [], "note": "</script>"}))
    out = tmp_path / "desk.html"
    subprocess.run([sys.executable, str(ROOT / "dashboard" / "build.py"), "--book", str(book), "--out", str(out)],
                   check=True, capture_output=True)
    html = out.read_text()
    assert '/*__SEED__*/{"day":"2026-09-17"' in html
    seed_line = html.split("/*__SEED__*/", 1)[1].split("\n", 1)[0]
    data = seed_line.rsplit("</script>", 1)[0]  # the seed's own closing tag comes after the JSON
    assert "\\u003c/script>" in data           # the closing tag inside the data is escaped ...
    assert "</script>" not in data               # ... so it cannot end the script block early
    assert json.loads(data)["note"] == "</script>"   # and reads back unchanged


def test_the_build_never_reaches_a_broker_or_the_network():
    source = (ROOT / "dashboard" / "build.py").read_text()
    for banned in ("broker_client", "alpaca", "anthropic", "httpx", "requests", "urllib"):
        assert banned not in source, banned


# --------------------------------------------------------------------------- #
# The four-fund page
# --------------------------------------------------------------------------- #

FUNDS_SAMPLE = {
    "generated_at": "2026-10-20T22:10:00+00:00", "final_through": "2026-10-20", "simulated": True,
    "calibration": {
        "status": "not_started", "start": None, "days_done": 0, "days_needed": 15,
        "pass_rule": {"text": ["Within 0.5% of the real account at every close."], "approved": False},
        "series": [], "differences": [],
        "metrics": {"max_abs_gap_pct": None, "tracking_error_pct": None, "matched_share": None, "unexplained": None},
        "holding_days": {"median": 3.0, "min": 1, "max": 9, "closed": 23, "open_median": 2.0},
    },
    "funds": None,
    "fund_test": {"status": "not_started", "start": None, "independent": None, "next_checkpoint": None},
}
RACE_SAMPLE = {
    "generated_at": "2026-10-20T21:30:00+00:00", "status_line": "independent days: 4 of 60 (= 180 trading days) — NO DECISION YET",
    "independent": 4, "of": 60, "trading_days": 180, "decided": False, "outcome": None, "outcome_text": None,
    "next": {"independent": 20, "entry_days": 60, "estimated": "2026-11-12", "bar": 2.9612},
    "looks": [{"independent": 20, "bar": 2.9612, "reached": False, "outcome": None, "reason": ""}],
}


def _build_module():
    # Loaded from its path (dashboard/ is not a package), with bytecode off so
    # the test leaves no __pycache__ inside the repository.
    spec = importlib.util.spec_from_file_location("dashboard_build", ROOT / "dashboard" / "build.py")
    module = importlib.util.module_from_spec(spec)
    was, sys.dont_write_bytecode = sys.dont_write_bytecode, True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = was
    return module


def _build_site(tmp_path, funds, race):
    book = tmp_path / "book.json"
    book.write_text(json.dumps({"day": "2026-10-20", "positions": []}))
    site = tmp_path / "site"
    done = subprocess.run([sys.executable, str(ROOT / "dashboard" / "build.py"), "--book", str(book),
                           "--funds", str(funds), "--race", str(race), "--site", str(site)],
                          check=True, capture_output=True, text=True)
    return site, done


def _seed(html: str, marker: str):
    """The JSON embedded after ``marker``, read back the way the page reads it."""
    block = html.split(marker, 1)[1].split("</script>", 1)[0]
    return json.loads(block)


def test_the_funds_page_is_labelled_simulated_and_linked_from_the_desk():
    text = (ROOT / "dashboard" / "funds.html").read_text()
    assert "/*__FUNDS__*/{}" in text and "/*__RACE__*/{}" in text
    assert "Simulated, not real money" in text
    assert '<a href="index.html">Desk</a>' in text and '<a href="funds.html" aria-current="page">4 Funds</a>' in text
    desk = (ROOT / "dashboard" / "template.html").read_text()
    assert 'href="funds.html"' in desk and 'href="index.html"' in desk
    # The same live-read pattern as the desk: public raw files, a copy kept
    # on the phone, the same service worker, and no key anywhere.
    assert "raw.githubusercontent.com" in text
    assert '"logs/funds.json"' in text and '"logs/race_gate.json"' in text
    assert "localStorage" in text and 'serviceWorker.register("sw.js")' in text
    assert "window.claude" not in text and "get_file_contents" not in text
    # The banners in the owner's words.
    assert "independent days (= " in text and "NO DECISION YET" in text and "Next checkpoint: " in text
    assert "bar t &gt; " in text
    # The owner's decision of 26 Sep 2026: a fixed start, read only after calibration passes.
    assert "and counts only after calibration passes." in text
    assert "Hidden until calibration passes" in text
    assert "not in force yet" in text


def test_both_pages_build_from_the_seeds(tmp_path):
    funds, race = tmp_path / "funds.json", tmp_path / "race_gate.json"
    funds.write_text(json.dumps(FUNDS_SAMPLE))
    race.write_text(json.dumps(RACE_SAMPLE))
    site, _ = _build_site(tmp_path, funds, race)
    assert (site / "index.html").exists() and (site / "funds.html").exists()
    page = (site / "funds.html").read_text()
    assert _seed(page, "/*__FUNDS__*/") == FUNDS_SAMPLE
    assert _seed(page, "/*__RACE__*/") == RACE_SAMPLE
    assert '/*__SEED__*/{"day":"2026-10-20"' in (site / "index.html").read_text()


def test_missing_data_files_still_build_on_the_empty_states(tmp_path):
    site, _ = _build_site(tmp_path, tmp_path / "no-funds.json", tmp_path / "no-race.json")
    page = (site / "funds.html").read_text()
    assert _seed(page, "/*__FUNDS__*/") == {} and _seed(page, "/*__RACE__*/") == {}
    assert "Simulated, not real money" in page


def test_an_unreadable_data_file_embeds_nothing_and_says_so(tmp_path):
    funds = tmp_path / "funds.json"
    funds.write_text('{"generated_at": "2026-10-20", "calibr')       # a redirect cut short
    site, done = _build_site(tmp_path, funds, tmp_path / "no-race.json")
    assert _seed((site / "funds.html").read_text(), "/*__FUNDS__*/") == {}
    assert "could not be read" in done.stderr


def test_the_funds_build_escapes_a_closing_tag(tmp_path):
    crafted = json.loads(json.dumps(FUNDS_SAMPLE))
    crafted["calibration"]["differences"] = [
        {"day": "2026-10-20", "ticker": "EWZ", "real": "no trade", "sim": "short 40", "reason": "</script><b>x</b>"}]
    funds, race = tmp_path / "funds.json", tmp_path / "race_gate.json"
    funds.write_text(json.dumps(crafted))
    race.write_text(json.dumps(dict(RACE_SAMPLE, status_line="</script>")))
    page = _build_module().build_funds(ROOT / "dashboard" / "funds.html", funds, race)
    for marker in ("/*__FUNDS__*/", "/*__RACE__*/"):
        data = page.split(marker, 1)[1].split("</script>", 1)[0]
        assert "\\u003c/script>" in data             # escaped, so the block cannot end early
    assert _seed(page, "/*__FUNDS__*/") == crafted
    assert _seed(page, "/*__RACE__*/")["status_line"] == "</script>"


def test_funds_stay_hidden_while_calibration_runs(tmp_path):
    crafted = json.loads(json.dumps(FUNDS_SAMPLE))
    crafted["calibration"]["status"] = "running"
    crafted["funds"] = {"start": "2026-10-01", "days": ["2026-10-01"], "band": {"p5": [99000.0], "p95": [101000.0], "funds": 1000},
                        "list": [{"name": "model", "label": "Model", "equity": [100500.0], "total_return": 0.005, "vs_vt": 0.001,
                                  "max_drawdown": 0.0, "trades": 3, "win_rate": None, "open_positions": 3, "cash": 40000.0}]}
    funds, race = tmp_path / "funds.json", tmp_path / "race_gate.json"
    funds.write_text(json.dumps(crafted))
    race.write_text(json.dumps(RACE_SAMPLE))
    site, _ = _build_site(tmp_path, funds, race)
    page = (site / "funds.html").read_text()
    assert _seed(page, "/*__FUNDS__*/")["funds"]["list"][0]["equity"] == [100500.0]   # the data is embedded ...
    # ... and the page decides in its script to show none of it: the funds
    # are drawn only when the record says calibration passed.
    assert "function fundsVisible(data){" in page
    assert 'return !!(data && data.funds && data.calibration && data.calibration.status === "passed");' in page
    assert "if(!fundsVisible(data))" in page and "Hidden until calibration passes" in page


def test_the_service_worker_keeps_both_pages_offline():
    sw = (ROOT / "dashboard" / "sw.js").read_text()
    shell = re.search(r"const SHELL = \[(.*?)\];", sw).group(1)
    assert '"./index.html"' in shell and '"./funds.html"' in shell


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_both_pages_scripts_parse_as_javascript(tmp_path):
    funds, race = tmp_path / "funds.json", tmp_path / "race_gate.json"
    funds.write_text(json.dumps(FUNDS_SAMPLE))
    race.write_text(json.dumps(RACE_SAMPLE))
    site, _ = _build_site(tmp_path, funds, race)
    for name in ("index.html", "funds.html"):
        scripts = re.findall(r"<script>(.*?)</script>", (site / name).read_text(), re.S)
        assert len(scripts) == 1, name
        source = tmp_path / (name + ".js")
        source.write_text(scripts[0])
        done = subprocess.run(["node", "--check", str(source)], capture_output=True, text=True)
        assert done.returncode == 0, f"{name}: {done.stderr}"


# --------------------------------------------------------------------------- #
# The four-fund page's own functions, run under node
#
# The page is one script in a browser; the functions below are pure (data in,
# HTML or a verdict out), so each is cut out of the built page with what it
# calls and run on crafted records. Nothing touches the network or the repo.
# --------------------------------------------------------------------------- #

NODE = shutil.which("node")
needs_node = pytest.mark.skipif(NODE is None, reason="node is not installed")

#: The helpers the page's pure functions call, in the order they are defined.
HELPERS = ("isNum", "esc", "DOCS", "DOC_ICON", "doc", "money", "kMoney", "signed", "plain", "pts", "tone", "bar2",
           "asObj", "day", "israel", "HUE", "SHORT", "DASH", "key", "bandKey", "plotHost", "tiles", "VERDICT", "warnIcon")

#: The proposed rule's lines as shadow/calibration.py writes them: a heading,
#: then conditions that already carry their numbers.
RULE_TEXT = [
    "PROPOSED, NOT APPROVED. Calibration passes only if all five hold over 15 trading days:",
    "1. On every one of the 15 closes, the simulated equity is within 1.0% of the real account's equity.",
    "2. The tracking error of daily returns is at most 0.20% a day.",
    "3. At least 90% of the real account's trades are matched by the same trade in the sim within one session.",
    "4. No 'unexplained' difference: every trade that differs names a reason from the fixed list.",
    "5. Integrity: no unexpected engine error, no position-manager error, stops cover every position.",
]
#: What evaluate_pass_rule writes: a header, a note per problem, then one
#: line per condition.
VERDICTS = [
    "PROPOSED rule, not approved: 3 of 15 closes compared.",
    "Note: the seed is the 2026-10-01 snapshot rolled forward to the close",
    "1. every close within 1.00%: FAIL (worst 1.42% on 2026-10-03)",
    "2. tracking error at most 0.20% a day: PENDING (0.11% a day so far)",
    "3. at least 90% of real trades matched: PENDING (9 of 10, 90.0%; 2 a session apart)",
    "4. no unexplained difference: PENDING (0 of 1 difference(s) unexplained)",
    "5. integrity: PASS (clean)",
]


def _calibration(status, **extra):
    record = json.loads(json.dumps(FUNDS_SAMPLE))
    record["calibration"].update(status=status, pass_rule={"text": RULE_TEXT, "approved": False, "verdicts": []})
    record["calibration"].update(extra)
    return record


@pytest.fixture(scope="module")
def built_funds_page(tmp_path_factory):
    folder = tmp_path_factory.mktemp("funds-page")
    funds, race = folder / "funds.json", folder / "race_gate.json"
    funds.write_text(json.dumps(FUNDS_SAMPLE))
    race.write_text(json.dumps(RACE_SAMPLE))
    return _build_module().build_funds(ROOT / "dashboard" / "funds.html", funds, race)


def _main_script(page: str) -> str:
    scripts = re.findall(r"<script>(.*?)</script>", page, re.S)
    assert len(scripts) == 1
    return scripts[0]


def _js_pieces(script: str, names) -> str:
    """The source of each named one-line ``const`` or ``function`` in the page's script."""
    pieces = []
    for name in names:
        line = re.search(r"^[ \t]*const " + re.escape(name) + r" = .*$", script, re.M)
        if line:
            pieces.append(line.group(0).strip())
            continue
        start = script.index("function " + name + "(")
        at = script.index("{", script.index(")", start))
        depth = 0
        for end in range(at, len(script)):
            depth += {"{": 1, "}": -1}.get(script[end], 0)
            if depth == 0:
                break
        pieces.append(script[start:end + 1])
    return "\n".join(pieces)


def _run_js(tmp_path, source: str, expression: str, cases):
    """``expression`` evaluated under node after ``source``, with ``CASES`` bound to ``cases``."""
    program = source + "\nconst CASES = " + json.dumps(cases) + ";\nprocess.stdout.write(JSON.stringify(" + expression + "));\n"
    path = tmp_path / "probe.js"
    path.write_text(program)
    done = subprocess.run([NODE, str(path)], capture_output=True, text=True, timeout=60)
    assert done.returncode == 0, done.stderr
    return json.loads(done.stdout)


def _page_functions(page: str, *names) -> str:
    # A stand-in for the page's $: each id gets an object whose innerHTML
    # the function under test writes.
    stub = "const ELEMENTS = {};\nconst $ = (id)=> (ELEMENTS[id] = ELEMENTS[id] || {innerHTML:\"\"});\n"
    return stub + _js_pieces(_main_script(page), HELPERS + names)


@needs_node
def test_fundsVisible_shows_the_funds_only_once_calibration_passed(tmp_path, built_funds_page):
    funds = {"start": "2026-10-01", "days": ["2026-10-01"], "list": [], "band": {"p5": [], "p95": [], "funds": 0}}
    cases = [
        _calibration("running") | {"funds": funds},              # funds in the file, calibration still running
        _calibration("passed") | {"funds": funds},               # passed, with funds
        _calibration("passed") | {"funds": None},                # passed, no fund record yet
        _calibration("failed") | {"funds": funds},
        {},                                                      # no record at all
    ]
    source = _js_pieces(_main_script(built_funds_page), ["fundsVisible"])
    assert _run_js(tmp_path, source, "CASES.map(fundsVisible)", cases) == [False, True, False, False, False]
    # renderFunds asks the same function, and hides the funds otherwise.
    assert "if(!fundsVisible(data))" in built_funds_page


@needs_node
def test_problems_reach_the_owner_in_a_warning_card(tmp_path, built_funds_page):
    running = _calibration("running", start="2026-10-01", days_done=0, series=[],
                           problems=["no real close after 2026-10-01 yet", "a <b>tag</b> in a problem"])
    running["calibration"]["pass_rule"]["verdicts"] = VERDICTS
    # "four" keeps its name but also checks the three exploratory funds
    # (shadow/run.py), so a problem in one of those is filed under a label
    # that covers it.
    four_broken = _calibration("passed") | {"integrity": {
        "four": {"ok": False, "problems": ["model: EWZ stops cover 10 of 40", "model_sized: SPY stops cover 0 of 10"]},
        "coin": {"ok": True, "problems": []}}}
    coin_broken = _calibration("passed") | {"integrity": {
        "four": {"ok": True, "problems": []}, "coin": {"ok": False, "problems": []}}}
    clean = _calibration("passed") | {"integrity": {"four": {"ok": True, "problems": []},
                                                    "coin": {"ok": True, "problems": []}}}
    not_started = _calibration("not_started")
    not_started["calibration"]["pass_rule"]["verdicts"] = VERDICTS      # ignored before calibration runs
    source = _page_functions(built_funds_page, "verdictRow", "problemList", "problemsHtml")
    cards = _run_js(tmp_path, source, "CASES.map(problemsHtml)", [running, four_broken, coin_broken, clean, not_started, {}])

    card = cards[0]
    assert 'class="alert bad"' in card and "3 problems in the record" in card
    assert "no real close after 2026-10-01 yet" in card
    assert "a &lt;b&gt;tag&lt;/b&gt; in a problem" in card and "<b>tag" not in card    # escaped
    assert "Pass rule:</span> 1. every close within 1.00%: FAIL (worst 1.42% on 2026-10-03)" in card
    assert "PENDING" not in card and "PASS" not in card.replace("Pass rule", "")      # only failures are problems
    assert "integrity check" not in card                                             # integrity is null

    label = "The funds' integrity check (the four and the three exploratory):</span> "
    assert label + "model: EWZ stops cover 10 of 40" in cards[1]
    assert label + "model_sized: SPY stops cover 0 of 10" in cards[1]
    assert "The four funds'" not in cards[1]                                         # not a label that rules them out
    assert "coin-flip" not in cards[1]                                               # ok is true: nothing to say
    assert "The coin-flip funds' integrity check:</span> failed, and the record names no problem" in cards[2]
    assert cards[3] == "" and cards[4] == "" and cards[5] == ""


@needs_node
def test_a_gap_in_the_price_data_is_a_note_not_a_failure(tmp_path, built_funds_page):
    holed = _calibration("passed") | {"integrity": {
        "four": {"ok": True, "problems": [], "data_holes": 3,
                 "data_hole_examples": ["model: 2026-09-22 IEF: no bar; the manager left the position as it was"]},
        "coin": {"ok": True, "problems": [], "data_holes": 0, "data_hole_examples": []}}}
    source = _page_functions(built_funds_page, "verdictRow", "problemList", "problemsHtml")
    [card] = _run_js(tmp_path, source, "CASES.map(problemsHtml)", [holed])
    assert 'class="alert"' in card and 'class="alert bad"' not in card                # amber, not red
    assert "3 ticker-day(s) had no price bar" in card and "2026-09-22 IEF" in card
    assert "coin-flip" not in card


@needs_node
def test_calibration_shows_the_verdicts_and_the_reason_no_day_is_recorded(tmp_path, built_funds_page):
    running = _calibration("running", start="2026-10-01", days_done=0, series=[],
                           problems=["no real close after 2026-10-01 yet"])
    running["calibration"]["pass_rule"]["verdicts"] = VERDICTS
    quiet = _calibration("running", start="2026-10-01", days_done=0, series=[])
    with_days = _calibration("running", start="2026-10-01", days_done=2, series=[
        {"day": "2026-10-02", "sim": 100100.0, "real": 100000.0, "diff_pct": 0.001},
        {"day": "2026-10-05", "sim": 100900.0, "real": 101000.0, "diff_pct": -0.00099}],
        differences=[{"day": "2026-10-05", "ticker": "EWZ", "real": "no trade", "sim": "short 40",
                      "reason": "sim acts at the next open"}])
    with_days["calibration"]["pass_rule"]["verdicts"] = VERDICTS
    not_started = _calibration("not_started")
    not_started["calibration"]["pass_rule"]["verdicts"] = VERDICTS
    source = _page_functions(built_funds_page, "verdictRow", "ruleHtml", "verdictsHtml", "calibrationFixHtml",
                             "renderCalibration")
    pages = _run_js(tmp_path, source, "CASES.map(c=>{ renderCalibration(c); return $(\"calibration\").innerHTML; })",
                    [running, quiet, with_days, not_started])

    shown = pages[0]
    assert "No calibration day recorded yet" in shown and "no real close after 2026-10-01 yet" in shown
    assert '<div class="card muted small">No calibration day recorded yet.</div>' not in shown
    assert '<div class="card muted small">No calibration day recorded yet.</div>' in pages[1]   # no problem: the usual card
    for page in (pages[0], pages[2]):
        assert "Where each condition stands" in page
        assert '<span class="chip bad">FAIL</span><span>1. every close within 1.00% <span class="faint">(worst 1.42% on 2026-10-03)</span>' in page
        assert '<span class="chip run">PENDING</span><span>2. tracking error at most 0.20% a day' in page
        assert '<span class="chip good">PASS</span><span>5. integrity <span class="faint">(clean)</span>' in page
        assert "PROPOSED rule, not approved: 3 of 15 closes compared." in page
    assert "EWZ" in pages[2] and "Trades that differ" in pages[2]
    assert "Where each condition stands" not in pages[3]                               # not started: no verdicts


@needs_node
def test_the_pass_rule_is_not_numbered_twice(tmp_path, built_funds_page):
    html = _run_js(tmp_path, _page_functions(built_funds_page, "ruleHtml"), "CASES.map(ruleHtml)",
                   [RULE_TEXT, ["Within 0.5% of the real account at every close."]])
    rule = html[0]
    assert "<ol" not in rule and '<ul class="rule">' in rule
    assert rule.startswith('<p class="rule-head"><strong>PROPOSED, NOT APPROVED. Calibration passes only if')
    for n in range(1, 6):
        assert rule.count(f">{n}.<") == 1                  # each number once, the rule's own
    assert re.search(r"<li><span class=\"n num\">1\.</span><span>On every one of the 15 closes", rule)
    assert "<strong>" not in html[1] and "Within 0.5% of the real account" in html[1]  # no numbered line: no heading
    assert ".rule{list-style:none;" in built_funds_page and '<ol class="rule">' not in built_funds_page


@needs_node
def test_an_older_fund_test_record_is_read_at_the_races_next_look(tmp_path, built_funds_page):
    """A record from before the checkpoint verdict (no ``planned_sessions``): the race's next look stands in."""
    ft = {"status": "running", "start": "2027-01-04", "sessions": 7, "independent": 2, "next_checkpoint": None}
    decided = dict(RACE_SAMPLE, decided=True, next=None, outcome_text="The model beat both rules.")
    source = _page_functions(built_funds_page, "nextText", "fundNextText", "fundTestBanner")
    out = _run_js(tmp_path, source, "CASES.map(([ft, R])=>fundTestBanner(ft, R))",
                  [[ft, RACE_SAMPLE], [ft, {}], [ft, decided],
                   [{"status": "not_started", "next_checkpoint": None}, RACE_SAMPLE]])
    assert "Fund test:</b> 7 of 180 fund sessions, <b>NO DECISION YET</b>" in out[0]   # sessions, not independent days
    assert "independent days" not in out[0]
    assert "Next checkpoint: 12 Nov 2026, bar t &gt; 2.96" in out[0] and "the race's next look" in out[0]
    assert "No checkpoint left to reach" not in out[0]
    assert "No checkpoint left to reach" not in out[1] and "decision gate writes its record" in out[1]
    assert "No checkpoint left to reach" in out[2]                                     # the race has no look left
    # Not running: the fixed start, and the reading waits for calibration.
    assert "starts 29 Sept 2026 (on the 28 Sept 2026 cycle)" in out[3]
    assert "counts only after calibration passes" in out[3]


@needs_node
def test_the_fund_test_banner_counts_fund_sessions_and_names_its_own_next_bar(tmp_path, built_funds_page):
    """Owner reading 5 (6 Oct 2026): fund sessions of 180 and the fund test's own next bar, never the race's."""
    base = {"status": "running", "start": "2026-09-29", "sessions": 12, "independent": 4, "planned_sessions": 180,
            "looks": [], "verdict": {"text": "no decision yet", "decided_at": None, "outcome": None}}
    base = dict(base, next_checkpoint=None)                     # always null, as before the verdict
    planned = dict(base, next_look={"look": 1, "estimated": "2026-12-22", "bar": 3.4, "planned_bar": 3.4})
    moved = dict(base, sessions=70, next_look={"look": 2, "estimated": "2027-03-22", "bar": 2.43,
                                              "planned_bar": 2.41})
    none_left = dict(base, sessions=181, next_look=None)
    no_bar = dict(base, next_look={"look": 2, "estimated": "2027-03-22", "bar": None, "planned_bar": 2.41})
    decided = dict(base, sessions=61, next_look=None, verdict={
        "text": "EARLY STOP AT CHECKPOINT 1: REPLACE THE MODEL FUND WITH THE MOMENTUM FUND", "decided_at": 1,
        "outcome": "momentum"})
    other_planned = dict(planned, planned_sessions=150)
    source = _page_functions(built_funds_page, "nextText", "fundNextText", "fundTestBanner")
    out = _run_js(tmp_path, source, "CASES.map(([ft, R])=>fundTestBanner(ft, R))",
                  [[planned, RACE_SAMPLE], [moved, RACE_SAMPLE], [none_left, RACE_SAMPLE], [no_bar, {}],
                   [decided, RACE_SAMPLE], [other_planned, RACE_SAMPLE], ["junk", 5]])
    assert "Fund test:</b> 12 of 180 fund sessions, <b>NO DECISION YET</b>" in out[0]
    assert "Next checkpoint 1 of 3, about 22 Dec 2026: the fund test's own bar t &gt; 3.40" in out[0]
    assert "planned" not in out[0] and "2.96" not in out[0] and "race's next look" not in out[0]
    assert "Next checkpoint 2 of 3, about 22 Mar 2027: the fund test's own bar t &gt; 2.43 (planned 2.41)" in out[1]
    assert "70 of 180 fund sessions" in out[1]
    assert "No checkpoint left to read." in out[2] and "race's next look" not in out[2]   # its own: none left
    assert "set by the spending rule at the look (planned 2.41)" in out[3]
    assert 'class="banner decided"' in out[4] and "decided at checkpoint 1" in out[4]
    assert "REPLACE THE MODEL FUND WITH THE MOMENTUM FUND" in out[4] and "NO DECISION YET" not in out[4]
    assert "12 of 150 fund sessions" in out[5]
    assert "starts 29 Sept 2026" in out[6]                                        # a damaged record: not running


def test_a_seed_holding_script_markup_cannot_break_out_of_its_block(tmp_path):
    # "<!--" then "<script>" puts the HTML parser in the script-escape states,
    # where the seed's own "</script>" no longer closes it and the page's main
    # script is swallowed. With every "<" escaped nothing in the data is markup.
    nasty = ["<!--<script>", "</script>", "a <!-- b --> c", "<script>alert(1)</script>"]
    crafted = json.loads(json.dumps(FUNDS_SAMPLE))
    crafted["calibration"]["problems"] = nasty
    race_record = dict(RACE_SAMPLE, status_line="<!--<script> then </script>")
    funds, race = tmp_path / "funds.json", tmp_path / "race_gate.json"
    funds.write_text(json.dumps(crafted))
    race.write_text(json.dumps(race_record))
    module = _build_module()
    page = module.build_funds(ROOT / "dashboard" / "funds.html", funds, race)
    book = tmp_path / "book.json"
    book.write_text(json.dumps({"day": "2026-10-20", "positions": [], "alarms": [{"title": t} for t in nasty]}))
    desk = module.build(ROOT / "dashboard" / "template.html", book)

    for html, marker, expected in ((page, "/*__FUNDS__*/", crafted), (page, "/*__RACE__*/", race_record),
                                   (desk, "/*__SEED__*/", json.loads(book.read_text()))):
        block = html.split(marker, 1)[1].split("</script>", 1)[0]
        assert "<" not in block, marker                      # nothing the parser could read as a tag
        assert json.loads(block) == expected, marker
        if NODE:                                             # and the browser's JSON.parse reads it back unchanged
            probe = tmp_path / "seed.json"
            probe.write_text(block)
            done = subprocess.run([NODE, "-e", "process.stdout.write(JSON.stringify(JSON.parse(require('fs')"
                                   ".readFileSync(process.argv[1], 'utf8'))))", str(probe)],
                                  capture_output=True, text=True, timeout=60)
            assert done.returncode == 0, done.stderr
            assert json.loads(done.stdout) == expected, marker
        # The main script still follows the seed, whole.
        rest = html.split(marker, 1)[1].split("</script>", 1)[1]
        assert re.search(r"<script>\n\(function\(\)\{.*\}\)\(\);\n</script>", rest, re.S), marker
    assert "function fundsVisible(data){" in _main_script(page)


def test_nan_or_infinity_in_a_data_file_embeds_nothing_and_says_so(tmp_path):
    funds, race = tmp_path / "funds.json", tmp_path / "race_gate.json"
    funds.write_text('{"simulated": true, "calibration": {"status": "running"}, "x": NaN}')
    race.write_text('{"independent": Infinity, "of": 60}')
    site, done = _build_site(tmp_path, funds, race)
    page = (site / "funds.html").read_text()
    assert _seed(page, "/*__FUNDS__*/") == {} and _seed(page, "/*__RACE__*/") == {}
    assert done.stderr.count("could not be read") == 2
    assert "NaN is not valid JSON" in done.stderr and "Infinity is not valid JSON" in done.stderr
    minus = tmp_path / "minus.json"
    minus.write_text("[-Infinity]")
    assert _build_module()._seed(minus) == {}


def test_the_service_worker_keeps_one_copy_per_url_whatever_the_query():
    sw = (ROOT / "dashboard" / "sw.js").read_text()
    assert 'u.search = ""' in sw
    assert "c.put(key, copy)" in sw and "c.put(event.request" not in sw
    assert "caches.match(key, {ignoreSearch: true})" in sw
    assert "fetch(event.request)" in sw                   # still network first


@needs_node
def test_the_service_worker_overwrites_one_entry_per_poll_and_serves_it_offline(tmp_path):
    harness = r"""
const fs = require("fs"), vm = require("vm");
const store = new Map(), handlers = {};
let online = true, served = 0;
const urlOf = (r) => typeof r === "string" ? r : r.url;
const strip = (u) => u.split("?")[0];
const cache = {
  put: async (req, res) => { store.set(urlOf(req), res); },
  keys: async () => [...store.keys()].map((url) => ({url})),
  delete: async (req) => store.delete(urlOf(req)),
  addAll: async () => {},
};
const caches = {
  open: async () => cache,
  keys: async () => ["algo-desk-v1"],
  delete: async () => true,
  match: async (req, opts) => {
    const want = opts && opts.ignoreSearch ? strip(urlOf(req)) : urlOf(req);
    for (const [k, v] of store) if ((opts && opts.ignoreSearch ? strip(k) : k) === want) return v;
    return undefined;
  },
};
const self = {addEventListener: (type, fn) => { handlers[type] = fn; }, skipWaiting() {}, clients: {claim() {}}};
const fetchStub = async () => {
  if (!online) throw new TypeError("offline");
  const body = "copy " + (++served);
  return {ok: true, body, clone() { return {ok: true, body}; }};
};
const context = vm.createContext({self, caches, fetch: fetchStub, URL, Response: {error: () => ({error: true})}});
vm.runInContext(fs.readFileSync(process.argv[2], "utf8"), context);
const settle = () => new Promise((r) => setTimeout(r, 20));
async function get(url) {
  let answer;
  handlers.fetch({request: {method: "GET", url}, respondWith: (p) => { answer = p; }});
  const response = await answer;
  await settle();
  return response;
}
(async () => {
  const file = "https://raw.githubusercontent.com/o/r/main/logs/funds.json";
  for (const t of [1, 2, 3]) await get(file + "?t=" + t);
  const afterPolls = [...store.keys()];
  online = false;
  const offline = await get(file + "?t=4");
  store.set(file + "?t=old", {body: "left by an older worker"});
  let done;
  handlers.activate({waitUntil: (p) => { done = p; }});
  await done;
  process.stdout.write(JSON.stringify({afterPolls, offline: offline.body, afterActivate: [...store.keys()]}));
})();
"""
    path = tmp_path / "harness.js"
    path.write_text(harness)
    done = subprocess.run([NODE, str(path), str(ROOT / "dashboard" / "sw.js")], capture_output=True, text=True, timeout=60)
    assert done.returncode == 0, done.stderr
    result = json.loads(done.stdout)
    file = "https://raw.githubusercontent.com/o/r/main/logs/funds.json"
    assert result["afterPolls"] == [file]                 # three polls, one entry, the newest
    assert result["offline"] == "copy 3"                  # offline, the last copy is served
    assert result["afterActivate"] == [file]              # an older worker's "?t=" copies are dropped


def test_the_funds_page_states_its_contract():
    text = (ROOT / "dashboard" / "funds.html").read_text()
    start = text.index("<!--")
    assert start < text.index("<style>")                 # near the top, before any code
    comment = text[start + 4:text.index("-->", start)]
    assert "<!--" not in comment and "--!>" not in comment
    for unit in ("FRACTIONS", "DOLLARS", "ISO dates", "ISO date-time"):
        assert unit in comment, unit
    for field in ("generated_at", "final_through", "simulated", "calibration.status", "calibration.start",
                  "calibration.days_done", "calibration.days_needed", "calibration.pass_rule.text[]",
                  "calibration.pass_rule.approved", "calibration.pass_rule.verdicts[]", "calibration.series[]",
                  "diff_pct", "calibration.differences[]", "calibration.metrics", "max_abs_gap_pct",
                  "tracking_error_pct", "matched_share", "unexplained", "calibration.holding_days", "open_median",
                  "calibration.problems[]", "funds.list[]", "total_return", "vs_vt", "max_drawdown", "win_rate",
                  "open_positions", "cash", "funds.band", "p5[]", "p95[]", "fund_test.status", "fund_test.start",
                  "fund_test.independent", "fund_test.next_checkpoint", "integrity",
                  "status_line", "independent, of", "trading_days", "decided", "outcome_text", "next",
                  "estimated", "bar", "looks[]", "reached", "reason",
                  "order_matters.real", "calibration.order_matters", "funds.list[].order_matters",
                  "integrity.coin.order_days", "cycle_days", "outranked_days", "by_kind", "outranks[]", "conviction"):
        assert field in comment, field


def test_long_alarm_text_wraps_on_the_desk():
    desk = (ROOT / "dashboard" / "template.html").read_text()
    # A flex child's min-width defaults to its content, so one long word in
    # an alarm pushed the desk wider than a phone. The text box may shrink
    # now, and a long word breaks inside it.
    assert ".stripe > div{min-width:0;overflow-wrap:anywhere}" in desk


# --------------------------------------------------------------------------- #
# How often the buying order mattered (a report only)
# --------------------------------------------------------------------------- #

def _order(cycle_days, days, outranked, listed=(), **by_kind):
    return {"cycle_days": cycle_days, "days": days, "skipped": sum(len(d["skipped"]) for d in listed),
            "outranked_days": outranked, "by_kind": by_kind, "list": list(listed)}


ORDER_REAL = _order(7, 2, 1, [
    {"day": "2026-09-18", "bought": [{"ticker": "TEVA", "conviction": 0.52}, {"ticker": "RSP", "conviction": None}],
     "skipped": [{"ticker": "XHB", "conviction": 0.4, "kind": "sleeve budget", "outranks": []}]},
    {"day": "2026-09-22", "bought": [{"ticker": "KRE", "conviction": 0.32}, {"ticker": "<b>X</b>", "conviction": 0.35}],
     "skipped": [{"ticker": "ASML", "conviction": 0.55, "kind": "sleeve budget", "outranks": ["KRE", "<b>X</b>"]},
                 {"ticker": "<i>Y</i>", "conviction": None, "kind": "<gross>", "outranks": []}]},
], **{"sleeve budget": 2, "<gross>": 1})

ORDER_FUNDS = {"start": "2026-10-01", "days": ["2026-10-01"], "band": {"p5": [99000.0], "p95": [101000.0], "funds": 1000},
               "list": [dict(name=name, label=label, equity=[100000.0], total_return=0.0, vs_vt=None if name == "vt" else 0.0,
                             max_drawdown=0.0, trades=0, win_rate=None, open_positions=0, cash=100000.0,
                             order_matters=None if name == "vt" else _order(15, n, k))
                        for name, label, n, k in (("model", "Model", 3, 1), ("momentum", "Momentum", 5, 0),
                                                  ("hybrid", "Hybrid", 0, 0), ("vt", "VT", 0, 0))]}


def _with_order(status, calibration_order=None, funds=None, coin=None):
    record = _calibration(status) | {"order_matters": {"real": ORDER_REAL}, "funds": funds}
    if calibration_order is not None:
        record["calibration"]["order_matters"] = calibration_order
    if coin is not None:
        record["integrity"] = {"four": {"ok": True, "problems": []}, "coin": {"ok": True, "problems": [], "order_days": coin}}
    return record


def _order_cards(tmp_path, page, cases):
    return _run_js(tmp_path, _page_functions(page, "fundsVisible", "orderHtml"), "CASES.map(orderHtml)", cases)


@needs_node
def test_the_order_report_gives_the_real_account_its_days_and_escapes_every_string(tmp_path, built_funds_page):
    [card] = _order_cards(tmp_path, built_funds_page, [_with_order("not_started")])
    assert "<h2>How often the buying order mattered</h2>" in card
    text = re.sub(r"<[^>]+>", "", card)
    assert ("Real paper account: ran out of room before the end of the list on 2 of 7 cycle days. "
            "On 1 of those days, a skipped signal had a higher conviction than one that was bought.") in text
    # Kinds as chips with their counts, escaped.
    assert '<span class="chip idle">sleeve budget: <span class="num">2</span></span>' in card
    assert "&lt;gross&gt;: " in card and "<gross>" not in card
    # The days, most recent first, with the skipped signal that outranked a bought one highlighted.
    assert card.index("22 Sep") < card.index("18 Sep")          # "Sep" or "Sept", as the ICU writes it
    assert "<mark>higher than KRE, &lt;b&gt;X&lt;/b&gt;</mark>" in card
    assert card.count("<mark>") == 1                           # only where outranks is non-empty
    assert "<b>X</b>" not in card and "<i>Y</i>" not in card and "&lt;i&gt;Y&lt;/i&gt;" in card
    assert 'RSP <span class="num">—</span>' in card and 'KRE <span class="num">0.32</span>' in card   # null conviction
    assert "Report only; the order is not changed." in card
    # Not started: no calibration copy line, no fund line.
    assert "Calibration copy" not in card and " fund:" not in card and "Coin-flip" not in card


@needs_node
def test_the_order_report_shows_no_fund_while_calibration_runs(tmp_path, built_funds_page):
    running = _with_order("running", calibration_order=_order(4, 1, 0), funds=ORDER_FUNDS,
                          coin={"median": 2.0, "p5": 0.0, "p95": 5.0})
    failed = _with_order("failed", calibration_order=_order(15, 6, 2), funds=ORDER_FUNDS,
                         coin={"median": 2.0, "p5": 0.0, "p95": 5.0})
    not_started = _with_order("not_started", calibration_order=_order(4, 1, 0))     # ignored before it starts
    cards = _order_cards(tmp_path, built_funds_page, [running, failed, not_started])
    text = [re.sub(r"<[^>]+>", "", c) for c in cards]
    assert "Calibration copy: 1 of 4 cycle days (0 with a higher-conviction signal skipped)." in text[0]
    assert "Calibration copy: 6 of 15 cycle days (2 with a higher-conviction signal skipped)." in text[1]
    for t in text[:2]:
        assert "Model fund" not in t and "Momentum fund" not in t and "Coin-flip" not in t
        assert "3 of 15" not in t
    assert "Calibration copy" not in text[2]


@needs_node
def test_the_order_report_shows_the_funds_once_calibration_passed(tmp_path, built_funds_page):
    passed = _with_order("passed", calibration_order=_order(15, 2, 0), funds=ORDER_FUNDS,
                         coin={"median": 4.5, "p5": 1.0, "p95": 9.0})
    no_coin = _with_order("passed", funds=ORDER_FUNDS)
    cards = _order_cards(tmp_path, built_funds_page, [passed, no_coin])
    text = [re.sub(r"<[^>]+>", "", c) for c in cards]
    assert "Calibration copy: 2 of 15 cycle days" in text[0]
    assert "Model fund: 3 of 15 days (1 with a higher-conviction signal skipped)." in text[0]
    assert "Momentum fund: 5 of 15 days (0 with a higher-conviction signal skipped)." in text[0]
    assert "Hybrid fund: 0 of 15 days" in text[0]
    assert "VT fund" not in text[0]
    assert "Coin-flip funds: median 4.5 days (5th–95th: 1–9)." in text[0]
    assert "Model fund: 3 of 15 days" in text[1] and "Coin-flip" not in text[1] and "Calibration copy" not in text[1]
    # The fund cards carry the same count, VT none.
    source = _page_functions(built_funds_page, "fundsVisible", "orderCell", "isExploratory", "sidesLine", "sidesCell",
                             "renderFunds")
    [html] = _run_js(tmp_path, source, "CASES.map(c=>{ renderFunds(c); return $(\"funds\").innerHTML; })", [passed])
    assert html.count("<dt>Order mattered</dt>") == 3
    assert '<dt>Order mattered</dt><dd class="num">3 of 15 days</dd>' in html


@needs_node
def test_the_order_report_is_absent_without_data_and_says_no_cycle_yet(tmp_path, built_funds_page):
    old = _calibration("running")                                              # an older file: no order_matters
    empty = _calibration("passed") | {"order_matters": {}, "funds": ORDER_FUNDS}
    null = _calibration("passed") | {"order_matters": {"real": None}}
    zero = _calibration("not_started") | {"order_matters": {"real": _order(0, 0, 0)}}
    cards = _order_cards(tmp_path, built_funds_page, [old, empty, null, {}, None, zero])
    assert cards[:5] == ["", "", "", "", ""]
    text = re.sub(r"<[^>]+>", "", cards[5])
    assert "Real paper account: No cycle yet." in text
    assert "<details" not in cards[5] and 'class="kinds"' not in cards[5]
    assert "Report only" in text
    # The page draws the section from the same render pass as the rest.
    assert '<section id="order"' in built_funds_page and '$("order").innerHTML = orderHtml(F)' in built_funds_page


# --------------------------------------------------------------------------- #
# The owner's decisions of 25 Sep 2026 on the page: the calibration fail rule,
# the two exploratory funds, longs vs shorts, and the race's two reports
# --------------------------------------------------------------------------- #

#: A calibration that failed on day 6, was fixed on 12 Oct and has run two
#: days since: day 15 or the fix + 5 days is now day 17. The fund test's
#: start is fixed; this plan is one whose calibration ran past the first
#: look, so that look is skipped and the bars are off the planned ones.
WITH_FIX = {
    "days_done": 8, "days_needed": 17, "days_passed": 5,
    "fixes": [{"day": "2026-10-05", "what": "an earlier fix"},
              {"day": "2026-10-12", "what": "stops re-placed <b>after</b> a partial fill"}],
    "last_fix": "2026-10-12", "days_since_fix": 2, "days_after_fix_needed": 5, "end_estimate": "2026-10-23",
    "fund_test_plan": {"start": "2026-09-29", "first_cycle": "2026-09-28", "sessions": [60, 120, 180],
                       "skipped": [True, False, False], "bars": [None, 2.4, 2.01],
                       "exact": [None, 2.4, 2.015], "registered": [3.4, 2.41, 2.02],
                       "registered_start": "2026-09-29", "matches_registered": False},
}
#: The same fields with nothing fixed: the plan is still the planned one.
NO_FIX = {
    "days_done": 4, "days_needed": 15, "days_passed": 4, "fixes": [], "last_fix": None, "days_since_fix": None,
    "days_after_fix_needed": 5, "end_estimate": "2026-10-16",
    "fund_test_plan": {"start": "2026-09-29", "first_cycle": "2026-09-28", "sessions": [60, 120, 180],
                       "skipped": [False, False, False], "bars": [3.4, 2.41, 2.02],
                       "exact": [3.395, 2.407, 2.015], "registered": [3.4, 2.41, 2.02],
                       "registered_start": "2026-09-29", "matches_registered": True},
}


def _text(html: str) -> str:
    """The page's text, as a reader sees it: each tag a space, runs of space as one."""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


@needs_node
def test_calibration_says_the_days_passed_the_last_fix_and_the_days_since_it(tmp_path, built_funds_page):
    null_bar = json.loads(json.dumps(WITH_FIX))
    null_bar["fund_test_plan"]["bars"] = [None, 2.6, 2.05]
    null_bar["fund_test_plan"]["skipped"] = "junk"
    cases = [
        dict(WITH_FIX, status="running"),
        dict(NO_FIX, status="running"),
        dict(WITH_FIX, status="failed"),
        null_bar | {"status": "running"},
        {"status": "running", "days_done": 3, "days_needed": 15},                 # an older record: none of the new fields
        dict(NO_FIX, status="not_started"),                                        # not started: nothing to say yet
        {}, None, "junk", [1],
        {"status": "running", "days_passed": "x", "fixes": "no", "last_fix": 5, "fund_test_plan": [1]},
    ]
    source = _page_functions(built_funds_page, "calibrationFixHtml")
    out = _run_js(tmp_path, source, "CASES.map(calibrationFixHtml)", cases)
    fixed, clean, failed, null_bars = out[0], out[1], out[2], out[3]

    for html in (fixed, failed):
        text = _text(html)
        assert "Days passed: 5 of 17" in text
        assert "Last fix: 12 Oct 2026 (stops re-placed &lt;b&gt;after&lt;/b&gt; a partial fill)" in text
        assert "<b>after" not in html                                              # the fix's text is escaped
        assert "Days since the last fix: 2 of 5" in text
        assert "If nothing more fails, it ends 23 Oct 2026." in text
        assert "All 2 fixes" in text
        assert "Fund test starts 29 Sept 2026 (fixed); bars none, 2.40, 2.01; look 1 skipped" in text
        # The plan moved: an amber note, with the planned bars and the rule that replaces them.
        assert 'class="amber"' in html
        assert "Differs from the planned bars (3.40, 2.41, 2.02): computed at each look by the spending rule" in text
        assert "logged in the Amendments table" in text

    text = _text(clean)
    assert "Days passed: 4 of 15" in text and "No fix yet" in text
    assert "Days since the last fix" not in text and " of 5" not in text          # "X of 5" only with a fix
    assert "If nothing more fails, it ends 16 Oct 2026." in text
    assert "Fund test starts 29 Sept 2026 (fixed); bars 3.40, 2.41, 2.02" in text and "skipped" not in text
    assert 'class="amber"' not in clean and "Amendments" not in text
    assert "The same start and bars as planned." in text
    assert "fixes" not in text                                                     # no list of fixes to open

    assert "bars none, 2.60, 2.05" in _text(null_bars)                             # a skipped look has no bar
    assert "look 1 skipped" not in _text(null_bars)                                # junk "skipped" says nothing

    assert out[4:10] == ["", "", "", "", "", ""]                                   # old, not started, missing: nothing
    odd = _text(out[10])
    assert "No fix yet" in odd and "Days passed" not in odd and "Fund test starts" not in odd


@needs_node
def test_the_calibration_card_carries_the_fail_rule_lines(tmp_path, built_funds_page):
    running = _calibration("running", start="2026-10-01", series=[])
    running["calibration"].update(WITH_FIX)
    old = _calibration("running", start="2026-10-01", days_done=3, series=[])
    source = _page_functions(built_funds_page, "verdictRow", "ruleHtml", "verdictsHtml", "calibrationFixHtml",
                             "renderCalibration")
    pages = _run_js(tmp_path, source, "CASES.map(c=>{ renderCalibration(c); return $(\"calibration\").innerHTML; })",
                    [running, old])
    text = _text(pages[0])
    assert "8 of 17 closes compared · started 1 Oct 2026" in text
    assert "Days passed: 5 of 17" in text and "Days since the last fix: 2 of 5" in text
    assert "computed at each look by the spending rule" in text
    old_text = _text(pages[1])
    assert "3 of 15 closes compared" in old_text
    assert "Days passed" not in old_text and "No fix yet" not in old_text and "Fund test starts" not in old_text


def _css_rules(page: str) -> list[tuple[list[str], str]]:
    """The page's CSS rules as (selectors, declarations with no spaces); comments dropped."""
    css = re.sub(r"/\*.*?\*/", "", re.search(r"<style>(.*?)</style>", page, re.S).group(1), flags=re.S)
    return [([s.strip() for s in sel.split(",")], body.replace(" ", ""))
            for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css)]


class _AroundText(HTMLParser):
    """For each run of text holding ``needle``, the classes of the elements around it, innermost first."""

    VOID = {"br", "hr", "img", "input", "meta", "link", "wbr"}

    def __init__(self, needle: str):
        super().__init__()
        self.needle, self.open, self.found = needle, [], []

    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID:
            self.open.append((tag, (dict(attrs).get("class") or "").split()))

    def handle_endtag(self, tag):
        for at in range(len(self.open) - 1, -1, -1):
            if self.open[at][0] == tag:
                del self.open[at:]
                break

    def handle_data(self, data):
        if self.needle in data:
            self.found.append([c for _, classes in reversed(self.open) for c in classes])


@needs_node
def test_a_fix_named_by_one_long_word_wraps_on_a_phone(tmp_path, built_funds_page):
    # A fix's text is free text from the record, and may be one long word: a
    # code path or a link. It sits in a grid list, and a grid column is as
    # wide as its widest word unless the word may break, so at 360px a
    # 70-character word pushed the page 275px sideways (checked in Chromium).
    # overflow-wrap is inherited, so the box around the word, or any box
    # between it and the card, must let it break anywhere.
    long = "shadow/broker.py::SimBroker._replace_stops_after_partial_fill_and_short_refusal"
    assert len(long) > 70 and " " not in long
    fixed = dict(WITH_FIX, status="running")
    fixed["fixes"] = [{"day": "2026-10-05", "what": "an earlier fix"}, {"day": "2026-10-12", "what": long}]
    source = _page_functions(built_funds_page, "calibrationFixHtml")
    [html] = _run_js(tmp_path, source, "CASES.map(calibrationFixHtml)", [fixed])

    around = _AroundText(long)
    around.feed(html)
    assert len(around.found) == 2                          # "Last fix: ... (<what>)" and the list of all fixes
    breaks_anywhere = {sel[1:] for sels, body in _css_rules(built_funds_page) if "overflow-wrap:anywhere" in body
                       for sel in sels if re.fullmatch(r"\.[\w-]+", sel)}
    for classes in around.found:
        assert "facts" in classes
        assert breaks_anywhere & set(classes), classes     # some box around the word lets it break


SIDES ={"long": {"n": 24, "mean_return": 0.0085, "hit_rate": 0.5833, "too_few": False},
         "short": {"n": 7, "mean_return": -0.0512, "hit_rate": 0.1428, "too_few": True}}


@needs_node
def test_longs_and_shorts_say_too_few_instead_of_the_numbers(tmp_path, built_funds_page):
    cases = [
        SIDES,
        {"long": {"n": 1, "mean_return": -0.02, "hit_rate": 0.0, "too_few": False},
         "short": {"n": 0, "mean_return": None, "hit_rate": None, "too_few": True}},
        {"long": {"n": 5, "mean_return": 0.01, "hit_rate": 0.6}},                  # no too_few: the owner's 20 trades
        {"long": {"n": 25, "mean_return": 0.01, "hit_rate": 0.6}},
        {"long": {"n": "<b>7</b>", "mean_return": 0.3, "hit_rate": 0.9, "too_few": False}},   # no count: too few
        None, {}, "x", [], {"long": None, "short": "x"},
    ]
    out = _run_js(tmp_path, _page_functions(built_funds_page, "sidesLine"), "CASES.map(sidesLine)", cases)
    assert out[0] == "Longs: 24 trades, mean +0.9%, hit 58% | Shorts: too few (n=7)"
    assert "5.1" not in out[0] and "14%" not in out[0]                             # the too-few side's numbers are hidden
    assert out[1] == "Longs: 1 trade, mean −2.0%, hit 0% | Shorts: too few (n=0)"
    assert out[2] == "Longs: too few (n=5)"
    assert out[3] == "Longs: 25 trades, mean +1.0%, hit 60%"
    assert out[4] == "Longs: too few (n=n/a)" and "<b>" not in out[4] and "30" not in out[4]
    assert out[5:] == ["", "", "", "", ""]


def _fund_row(name, label, total, **extra):
    row = dict(name=name, label=label, equity=[100000.0, round(100000.0 * (1 + total), 2)], total_return=total,
               vs_vt=None if name == "vt" else round(total - 0.004, 6), max_drawdown=0.012,
               trades=1 if name == "vt" else 30, win_rate=None if name == "vt" else 0.55, open_positions=3,
               cash=40000.0, order_matters=None if name == "vt" else _order(15, 2, 1),
               sides=None if name == "vt" else SIDES, exploratory=False)
    return row | extra


SIX_FUNDS = {
    "start": "2026-10-19", "days": ["2026-10-19", "2026-10-20"],
    "band": {"p5": [99000.0, 98800.0], "p95": [101000.0, 101300.0], "funds": 1000},
    "list": [
        _fund_row("model", "Model", 0.012), _fund_row("momentum", "Momentum", 0.004),
        _fund_row("hybrid", "Hybrid", -0.003), _fund_row("vt", "VT (world index, held)", 0.004),
        _fund_row("model_by_conviction", "Model, highest conviction first", 0.015, exploratory=True,
                  compare_to="model",
                  vs_model={"total_return_diff": 0.003, "max_drawdown": 0.011, "model_max_drawdown": 0.012,
                            "mean_daily_diff": 0.00015, "t": 1.234, "days": 20}),
        _fund_row("model_sized", "Model, sized by conviction", 0.009, exploratory=True, compare_to="model",
                  vs_model={"total_return_diff": -0.003, "max_drawdown": 0.031, "model_max_drawdown": 0.012,
                            "mean_daily_diff": None, "t": None, "days": 20}),
    ],
}


@needs_node
def test_the_exploratory_funds_are_set_against_the_model_fund(tmp_path, built_funds_page):
    passed = _calibration("passed") | {"funds": SIX_FUNDS}
    hostile = json.loads(json.dumps(passed))
    hostile["funds"]["list"][4]["label"] = "<b>Model</b> first"
    bare = _calibration("passed") | {"funds": {"list": [{"name": "model_sized", "exploratory": True}]}}
    cases = [passed, hostile,
             _calibration("running") | {"funds": SIX_FUNDS},                   # calibration not passed: hidden
             _calibration("failed") | {"funds": SIX_FUNDS},
             _calibration("passed") | {"funds": ORDER_FUNDS},                  # an older record: no exploratory row
             _calibration("passed") | {"funds": {"list": "x"}},
             {}, None, bare]
    source = _page_functions(built_funds_page, "fundsVisible", "sidesLine", "isExploratory", "exploratoryHtml")
    out = _run_js(tmp_path, source, "CASES.map(exploratoryHtml)", cases)
    card, text = out[0], _text(out[0])
    assert "Exploratory: does the order, the size or the entry day matter?" in text
    assert card.count('<span class="chip idle">exploratory; cannot change the decision</span>') == 2
    assert text.index("Model, highest conviction first") < text.index("Model, sized by conviction")
    # Highest conviction first: its return against the model's, the difference, the daily mean and its t.
    first = text.split("Model, sized by conviction")[0]
    assert "Total return +1.50% vs the model's +1.20%" in first
    assert "Difference +0.30 pts" in first
    assert "Mean daily difference +0.015% a day" in first
    assert "t 1.23 over 20 days" in first
    assert "Max drawdown" not in first                                         # drawdown only for the sized fund
    # Sized by conviction: the same, and its max drawdown next to the model's.
    sized = text.split("Model, sized by conviction")[1]
    assert "Total return +0.90% vs the model's +1.20%" in sized
    assert "Difference −0.30 pts" in sized and "Mean daily difference n/a" in sized and "t n/a over 20 days" in sized
    assert "Max drawdown −3.1% vs the model's −1.2%" in sized
    assert text.count("Longs: 24 trades, mean +0.9%, hit 58% | Shorts: too few (n=7)") == 2

    assert "&lt;b&gt;Model&lt;/b&gt; first" in out[1] and "<b>Model</b>" not in out[1]
    assert out[2:8] == ["", "", "", "", "", ""]
    bare_text = _text(out[8])                                                  # no model row, no vs_model: n/a, no throw
    assert "Total return n/a vs the model's n/a" in bare_text and "Max drawdown n/a vs the model's n/a" in bare_text


@needs_node
def test_the_chart_table_and_cards_stay_the_four_funds(tmp_path, built_funds_page):
    passed = _calibration("passed") | {"funds": SIX_FUNDS}
    source = _page_functions(built_funds_page, "fundsVisible", "orderCell", "isExploratory", "sidesLine", "sidesCell",
                             "renderFunds")
    # chart() draws into the DOM; here it only records which lines it was given.
    probe = ("CASES.map(c=>{ const drawn = []; globalThis.chart = (host, spec)=>drawn.push(spec.series.map(s=>s.label));"
             " const todo = renderFunds(c); $(\"funds\").querySelector = ()=>null; todo.forEach(([, fn])=>fn());"
             " return {html: $(\"funds\").innerHTML, drawn}; })")
    [got] = _run_js(tmp_path, source, probe, [passed])
    html = got["html"]
    assert got["drawn"] == [["VT", "Hybrid", "Momentum", "Model"]]             # the chart: exactly the four
    assert "<th>Day</th><th>Model</th><th>Momentum</th><th>Hybrid</th><th>VT</th><th>Band 5th</th>" in html
    assert html.count('<article class="card fund">') == 4
    assert "highest conviction first" not in html and "sized by conviction" not in html
    # Each fund but VT has its longs-and-shorts line.
    assert html.count('<p class="sides">') == 3
    assert "Longs: 24 trades, mean +0.9%, hit 58% | Shorts: too few (n=7)" in html
    # The order report lists the four as before; the exploratory funds have their own card.
    [order] = _run_js(tmp_path, _page_functions(built_funds_page, "fundsVisible", "orderHtml"), "CASES.map(orderHtml)",
                      [passed | {"order_matters": {"real": ORDER_REAL}}])
    order_text = _text(order)
    assert "Model fund:" in order_text and "Momentum fund:" in order_text and "Hybrid fund:" in order_text
    assert "conviction first fund" not in order_text and "sized by conviction fund" not in order_text
    # The page draws the exploratory card from the same render pass.
    assert '<section id="explore"' in built_funds_page and '$("explore").innerHTML = exploratoryHtml(F)' in built_funds_page


def _split(n, mean, hit, few=None):
    return {"n": n, "mean_net": mean, "hit_rate": hit, "too_few": n < 20 if few is None else few}


RACE_REPORTS = dict(
    RACE_SAMPLE, report_since="2026-09-23",
    conviction_groups={
        "model": [dict(_split(24, 0.0085, 0.5833), group="0.30-0.40"),
                  dict(_split(7, 0.0512, 0.8571), group="0.40-0.50"),
                  dict(_split(0, None, None), group="0.50-0.60"),
                  dict(_split(21, -0.0031, 0.4286), group="0.60+")],
        "momentum": [dict(_split(n, 0.01, 0.5), group=g)
                     for n, g in ((3, "0.30-0.40"), (5, "0.40-0.50"), (2, "0.50-0.60"), (1, "0.60+"))],
        "hybrid": [dict(_split(n, 0.01, 0.5), group=g)
                   for n, g in ((12, "0.30-0.40"), (4, "0.40-0.50"), (0, "0.50-0.60"), (0, "0.60+"))],
    },
    sides={
        "model": {"long": _split(45, 0.004, 0.53), "short": _split(1, 0.02, 1.0)},
        "momentum": {"long": _split(10, 0.001, 0.5), "short": _split(9, -0.002, 0.44)},
        "hybrid": {"long": _split(12, 0.0, 0.5), "short": _split(3, 0.01, 0.67)},
        "random": {"long": _split(20, -0.001, 0.49), "short": _split(22, 0.0007, 0.5)},
    },
)


@needs_node
def test_the_race_reports_show_too_few_until_twenty_trades(tmp_path, built_funds_page):
    hostile = json.loads(json.dumps(RACE_REPORTS))
    hostile["conviction_groups"]["<i>x</i>"] = [dict(_split(30, 0.01, 0.5), group="<b>g</b>")]
    cases = [RACE_REPORTS, hostile,
             RACE_SAMPLE,                                                       # an older record: no reports
             {}, None, "x",
             {"report_since": "2026-09-23", "conviction_groups": {}, "sides": {}},
             {"conviction_groups": "x", "sides": [1]},
             {"conviction_groups": {"model": "x"}, "sides": {"model": None}},
             {"sides": {"model": {"long": {"n": 19, "mean_net": 0.01, "hit_rate": 0.5}}}}]
    source = _page_functions(built_funds_page, "ARM", "raceReportsHtml")
    out = _run_js(tmp_path, source, "CASES.map(raceReportsHtml)", cases)
    card, text = out[0], _text(out[0])
    assert "Race: by conviction, and longs vs shorts (exploratory, report only)" in text
    assert re.search(r"Trades since 23 Sept? 2026, after costs", text)             # "Sep" or "Sept"
    assert '"too few" below 20 trades' in text
    assert text.index("Does higher conviction mean better trades?") < text.index("Longs vs shorts")
    conviction, sides = card.split("<h4>Longs vs shorts</h4>")
    # A table per arm, in the race's order; the coin flip only in longs vs shorts.
    assert re.findall(r"<caption>(.*?)</caption>", conviction) == ["Model", "Momentum", "Hybrid"]
    assert re.findall(r"<caption>(.*?)</caption>", sides) == ["Model", "Momentum", "Hybrid", "Random (coin flip)"]
    assert "<th>Conviction</th><th>n</th><th>Mean net</th><th>Hit rate</th>" in conviction
    # Twenty trades or more: the numbers. Fewer: "too few", and none of the numbers.
    assert '<tr><td>0.30-0.40</td><td>24</td><td class="up">+0.85%</td><td>58%</td></tr>' in card
    assert '<tr><td>0.60+</td><td>21</td><td class="down">−0.31%</td><td>43%</td></tr>' in card
    assert '<tr><td>0.40-0.50</td><td colspan="3" class="few">too few (n=7)</td></tr>' in card
    assert '<tr><td>0.50-0.60</td><td colspan="3" class="few">too few (n=0)</td></tr>' in card
    assert "+5.12%" not in card and "86%" not in card
    assert '<tr><td>Longs</td><td>45</td><td class="up">+0.40%</td><td>53%</td></tr>' in sides
    assert '<tr><td>Shorts</td><td colspan="3" class="few">too few (n=1)</td></tr>' in sides
    assert "+2.00%" not in sides and "100%" not in sides
    assert '<tr><td>Longs</td><td>20</td><td class="down">−0.10%</td><td>49%</td></tr>' in sides   # exactly 20: shown
    # Every string from the record is escaped.
    assert "&lt;i&gt;x&lt;/i&gt;" in out[1] and "&lt;b&gt;g&lt;/b&gt;" in out[1]
    assert "<i>x" not in out[1] and "<b>g" not in out[1]
    # Old, missing or odd records draw nothing, and nothing throws.
    assert out[2:9] == ["", "", "", "", "", "", ""]
    assert "too few (n=19)" in out[9] and "+1.00%" not in out[9]               # no too_few given: the owner's 20
    # Race data, not fund data: drawn from the race record alone, near the race banner.
    assert '$("race-reports").innerHTML = raceReportsHtml(R)' in built_funds_page
    assert (built_funds_page.index('<section id="banners"') < built_funds_page.index('<section id="race-reports"')
            < built_funds_page.index("<h2>Calibration</h2>"))


def test_the_contract_names_the_fields_of_the_25_sep_decisions():
    text = (ROOT / "dashboard" / "funds.html").read_text()
    start = text.index("<!--")
    comment = text[start + 4:text.index("-->", start)]
    assert "<!--" not in comment and "--!>" not in comment
    for field in ("calibration.days_passed", "calibration.fixes[]", "calibration.last_fix",
                  "calibration.days_since_fix", "calibration.days_after_fix_needed", "calibration.end_estimate",
                  "calibration.fund_test_plan", "registered_start", "matches_registered",
                  "model_by_conviction", "model_sized", "funds.list[].exploratory", "funds.list[].compare_to",
                  "funds.list[].vs_model", "total_return_diff", "model_max_drawdown", "mean_daily_diff",
                  "funds.list[].sides", "mean_return", "hit_rate", "too_few",
                  "report_since", "conviction_groups", "mean_net", '"0.30-0.40"', '"0.60+"', "random",
                  "integrity.four"):
        assert field in comment, field


# --------------------------------------------------------------------------- #
# The owner's decisions of 26 Sep 2026 on the page: the same-day fund, the
# price source's gaps by month, and the names the paper account held
# --------------------------------------------------------------------------- #

SAME_DAY_ROW = _fund_row("model_same_day", "Model, entered the same day", 0.010, exploratory=True, compare_to="model",
                         vs_model={"total_return_diff": -0.002, "max_drawdown": 0.02, "model_max_drawdown": 0.012,
                                   "mean_daily_diff": -0.0001, "t": -0.5, "days": 20},
                         not_entered={"no_price": 3, "outside_hours": 2, "other_day": 0, "total": 5})


@needs_node
def test_the_same_day_fund_says_which_lines_it_could_not_enter(tmp_path, built_funds_page):
    seven = json.loads(json.dumps(SIX_FUNDS))
    seven["list"].append(SAME_DAY_ROW)
    passed = _calibration("passed") | {"funds": seven}
    odd = json.loads(json.dumps(passed))
    odd["funds"]["list"][6]["not_entered"] = {"no_price": "x", "other_day": 1}
    source = _page_functions(built_funds_page, "fundsVisible", "sidesLine", "isExploratory", "exploratoryHtml")
    out = _run_js(tmp_path, source, "CASES.map(exploratoryHtml)", [passed, odd,
                                                                    _calibration("running") | {"funds": seven}])
    text = _text(out[0])
    assert out[0].count('<span class="chip idle">exploratory; cannot change the decision</span>') == 3
    same = text.split("Model, entered the same day")[1]
    assert "Total return +1.00% vs the model's +1.20%" in same and "t -0.50 over 20 days" in same
    assert "Lines not entered 5 3 no recorded price, 2 outside regular hours" in same
    assert "another day" not in same and "Lines not entered" not in text.split("Model, entered the same day")[0]
    assert "Lines not entered 1 0 no recorded price, 0 outside regular hours, 1 on another day" in _text(out[1])
    assert out[2] == ""                                                        # hidden until calibration passes


@needs_node
def test_price_gaps_and_held_names_are_shown_before_calibration_passes(tmp_path, built_funds_page):
    data = _calibration("running") | {
        "price_gaps": {"from": "2026-09-29", "through": "2026-10-09", "tickers": 80, "limit": 0.02, "months": [
            {"month": "2026-09", "sessions": 2, "missing": 27, "share": 27 / 160, "over": True, "by_day": {}},
            {"month": "2026-10", "sessions": 7, "missing": 3, "share": 3 / 560, "over": False, "by_day": {}}]},
        "held_names": {"from": "2026-09-28", "days": [
            {"day": f"2026-10-{d:02d}", "names": 20 + d, "lines": 20 + d, "of": 80} for d in range(1, 13)]},
    }
    source = _page_functions(built_funds_page, "dataHtml")
    out = _run_js(tmp_path, source, "CASES.map(dataHtml)",
                  [data, _calibration("running"), {}, None, {"price_gaps": {"months": "x"}, "held_names": 5}])
    html, text = out[0], _text(out[0])
    assert "Price gaps and held names" in text and "not a fund result" in text
    assert "Over 80 watchlist tickers" in text and "limit 2% a month" in text
    assert "2026-09 2 27 16.88% above 2%" in text and '<tr class="over">' in html
    assert "2026-10 7 3 0.54%" in text and html.count('<tr class="over">') == 1
    assert "12 Oct 2026: 32 names held of 80" in text                         # newest first
    assert text.index("12 Oct 2026") < text.index("3 Oct 2026")
    assert "2 earlier days" in text                                           # ten shown, the rest folded
    assert out[1:] == ["", "", "", ""]


def test_the_contract_names_the_fields_of_the_26_sep_decisions():
    text = (ROOT / "dashboard" / "funds.html").read_text()
    comment = text[text.index("<!--") + 4:text.index("-->")]
    assert "<!--" not in comment and "--!>" not in comment
    for field in ("model_same_day", "funds.list[].not_entered", "no_price", "outside_hours", "other_day",
                  "price_gaps", "price_gaps.months[]", "by_day", "held_names", "held_names.days[]",
                  "fund_test.first_cycle", "fund_test.waiting_for", "skipped[]", "not_shortable_since"):
        assert field in comment, field


# --------------------------------------------------------------------------- #
# The words live in the docs; the pages link to them
# --------------------------------------------------------------------------- #

def _docs_anchors() -> dict[str, set[str]]:
    """Each docs page (its path under docs/, no extension) and the anchors of its headings, the way Mintlify slugs them."""
    def slug(heading: str) -> str:
        heading = heading.lower().replace("'", "").replace("’", "")
        return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", heading)).strip("-")
    pages = {}
    for path in (ROOT / "docs").rglob("*.mdx"):
        prose = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)         # a "#" inside a code block is a comment
        pages[str(path.relative_to(ROOT / "docs")).removesuffix(".mdx")] = {
            slug(m.group(1)) for m in re.finditer(r"^#{1,4} (.+?)\s*$", prose, re.M)}
    return pages


def test_every_docs_link_on_both_pages_reaches_a_page_and_a_heading():
    # The pages explain nothing themselves: each part links to the docs page
    # that does. A renamed heading would leave a link pointing at the top of
    # the page, so every anchor is checked against the docs' headings.
    pages = _docs_anchors()
    assert _docs_anchors()["shadow-funds"] >= {"calibration-first", "late-runs"}   # the slug rule, on known headings
    for name in ("template.html", "funds.html"):
        page = (ROOT / "dashboard" / name).read_text()
        assert 'const DOCS = "https://algotrade.mintlify.site/";' in page
        links = set(re.findall(r'href="https://algotrade\.mintlify\.site/([^"]*)"', page)) | set(re.findall(r'doc\("([^"]+)"', page))
        assert len(links) >= 6, name
        for link in links:
            target, _, anchor = link.partition("#")
            assert target == "" or target in pages, (name, link)
            assert not anchor or anchor in pages[target], (name, link)
        # Opened in the browser, beside the app, never inside it.
        assert 'target="_blank" rel="noopener"' in page
        # The explanations that moved to the docs are gone from the page.
        for gone in ("Every position has a stop, every ticker was judged once", "if every stop fires at once",
                     "Every fund on this page is a simulation", "The two lines should lie on top of each other",
                     "the daily health check warns the owner",
                     "so the copy did not do what the real account could not"):
            assert gone not in page, (name, gone)


def test_every_link_that_leaves_the_app_says_so():
    # A link that opens a new tab carries the outward arrow after its label
    # and a note for screen readers, in the markup and in the doc() helper
    # the renderers use; every one of them is rel="noopener".
    arrow = 'M4 12 12 4M6 4h6v6'
    note = '<span class="sr-only">(opens in a new tab)</span>'
    for name in ("template.html", "funds.html"):
        page = (ROOT / "dashboard" / name).read_text()
        markup = page.split("<script>")[0]
        anchors = re.findall(r'<a [^>]*target="_blank"[^>]*>.*?</a>', markup)
        assert len(anchors) >= 3, name                                        # the nav's Docs link and the footer
        for a in anchors:
            assert 'rel="noopener"' in a and arrow in a and a.endswith(note + "</a>"), (name, a)
            assert a.index(arrow) > a.index(">"), (name, a)                     # the arrow trails the label
        helper = re.search(r"const doc = .*", page).group(0)
        assert "${label}${DOC_ICON}" + note + "</a>`;" in helper, name
        assert arrow in re.search(r"const DOC_ICON = .*", page).group(0), name
        assert ".sr-only{position:absolute;width:1px;height:1px;" in page, name
        # Big enough to tap, and a focus ring on every control a keyboard reaches.
        assert "a.doc{" in page and "min-height:28px" in page.split("a.doc{", 1)[1].split("}", 1)[0], name
        assert "summary:focus-visible" in page and "a:focus-visible" in page, name
        assert "min-height:40px" in page.split("button{", 1)[1].split("}", 1)[0], name


def _tokens(css: str) -> dict[str, str]:
    return dict(re.findall(r"--([a-z0-9-]+):(#[0-9a-f]{6})", css))


def _contrast(a: str, b: str) -> float:
    def lum(h):
        r, g, b_ = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
        f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b_)
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


@pytest.mark.parametrize("name", ["template.html", "funds.html"])
def test_the_theme_tokens_clear_the_contrast_floors(name):
    # WCAG AA: 4.5:1 for the small text the muted and status inks are used
    # for, on every surface they sit on; 3:1 for a chart line on its card.
    # Both themes, since dark mode is its own set of tokens, not a flip.
    page = (ROOT / "dashboard" / name).read_text()
    css = re.search(r"<style>(.*?)</style>", page, re.S).group(1)
    light = _tokens(css.split("@media", 1)[0])
    dark = _tokens(css.split('[data-theme="dark"]', 1)[1].split("}", 1)[0])
    for theme in (light, dark):
        for ink, on in (("ink-3", "bg"), ("ink-3", "surface"), ("ink-3", "surface-2"), ("ink-2", "bg"), ("ink-2", "surface"),
                        ("accent", "surface"), ("accent", "bg"), ("good", "good-bg"), ("warn", "warn-bg"), ("bad", "bad-bg"),
                        ("good", "surface"), ("bad", "surface"), ("accent-ink", "accent")):
            assert _contrast(theme[ink], theme[on]) >= 4.5, (name, ink, on, theme[ink], theme[on])
        assert _contrast(theme["ink-3"], theme["bg"]) < _contrast(theme["ink-2"], theme["bg"])   # muted stays lighter
        assert _contrast(theme["bar-fill"], theme["bar"]) >= 3.0
        if "s-model" in theme:
            for series in ("s-model", "s-momentum", "s-hybrid"):
                assert _contrast(theme[series], theme["surface"]) >= 3.0, (name, series)


# --------------------------------------------------------------------------- #
# After Israeli tax and in shekels (pre-registration sections 5c and 11.9)
# --------------------------------------------------------------------------- #

def _tax_view(equity, after, ils, ils_after, from_fx, paid, if_sold):
    return {"from": "2026-09-10", "through": "2026-10-02", "days": 17,
            "usd": {"start": 100000, "equity": equity, "after_tax": after, "return": equity / 1e5 - 1,
                    "after_tax_return": after / 1e5 - 1},
            "ils": {"start": 304000, "equity": ils, "after_tax": ils_after, "return": ils / 304000 - 1,
                    "after_tax_return": ils_after / 304000 - 1, "from_usd_ils": from_fx, "after_tax_from_usd_ils": from_fx},
            "tax_ils": {"paid_so_far": paid, "if_sold_today": if_sold},
            "usd_ils": {"start": 3.04, "end": 3.08, "change": 0.013}, "unpriced": []}


@needs_node
def test_the_after_tax_view_shows_the_paper_account_now_and_the_funds_once_calibration_passed(tmp_path, built_funds_page):
    paper = _tax_view(101761.67, 101500.0, 313426.0, 312620.0, 0.0131, 120.0, 925.0)
    running = _calibration("running") | {"after_tax": {
        "fx": {"available": True, "first": "2026-09-10", "counts": {"boi": 16, "ecb": 1, "carried": 0}},
        "paper": paper, "paper_lots": {"checked": True, "mismatches": ["XBI"]}, "funds": None,
        "looks": [{"look": 1, "made_on": "2026-12-22", "status": "unavailable", "reason": "calibration had not passed"}],
        "breakeven": {"years": 20, "growth": 0.06, "dividend_yield": 0.02, "extra_per_year": 0.00816}}}
    passed = _calibration("passed") | {"after_tax": running["after_tax"] | {
        "funds": {n: _tax_view(100500, 100400, 309500, 309200, 0.01, 0, 100) for n in ("model", "momentum", "hybrid", "vt")},
        "looks": [{"look": 1, "made_on": "2026-12-23", "status": "ready",
                   "tests": {"model": {"t": 1.234}, "momentum": {"t": -0.5}, "hybrid": {"t": 3.6}}}]}}
    no_rates = {"after_tax": {"fx": {"available": False, "reason": "no rate table was given"}}}
    source = _page_functions(built_funds_page, "afterTaxHtml")
    out = _run_js(tmp_path, source, "CASES.map(afterTaxHtml)", [running, passed, no_rates, {}, None, {"after_tax": 5}])
    text = _text(out[0])
    assert "After Israeli tax and in shekels" in text and "Paper account (real)" in text
    assert "$101,762 +1.76%" in text and "$101,500 +1.50%" in text and "₪313,426" in text
    assert "+1.31 pts" in text and "₪120" in text and "₪925" in text
    assert "once calibration has passed" in text and "Model fund" not in text
    assert "differ from its positions for XBI" in text
    assert "Look 1 (made 22 Dec 2026): not available: calibration had not passed" in text
    assert "1 day from another source" in text and "0.82 points a year" in text and "not a gate" in text
    both = _text(out[1])
    assert all(f"{n} fund" in both for n in ("Model", "Momentum", "Hybrid", "VT")) and "once calibration" not in both
    assert "Model t 1.23 · Momentum t -0.50 · Hybrid t 3.60" in both
    assert "No rate table tonight (no rate table was given)" in _text(out[2])
    assert out[3:] == ["", "", ""]


def _verdict_records():
    """A race gate and a funds record at checkpoint 1, their tables made by ``analysis.verdict`` itself.

    The plan's examples (i) and (ii): the race stops early for momentum, the
    fund test decides nothing, and the combined line waits for the fund test.
    Real dates inside the experiment, so ``table_json`` writes them as a real
    output would.
    """
    from datetime import date

    from analysis import verdict
    from tests.test_verdict import fund_record, plan_inputs, race

    race_table = verdict.table_json(race(plan_inputs()))
    record = fund_record()
    record["table"] = verdict.table_json(verdict.fund_test_table(record, planned_next=(2, date(2027, 3, 22), 2.41)))
    side = {"final_read": False, "skipped_all": False, "look": 1, "window_end": "2026-12-22"}
    line = verdict.combined(dict(side, decided_at=1, outcome="momentum", next=None),
                            dict(side, decided_at=None, outcome=None, next={"look": 2, "estimated": "2027-03-22"}))
    R = dict(RACE_SAMPLE, verdict={"text": race_table["verdict"], "decided_at": 1, "looks": [
        {"look": 1, "made_on": "2026-12-23", "window_end": "2026-12-22", "table": race_table}]})
    F = dict(FUNDS_SAMPLE, verdict=line, fund_test=dict(
        FUNDS_SAMPLE["fund_test"], looks=[record], note=None,
        verdict={"text": "no decision yet", "decided_at": None, "outcome": None}))
    return F, R


@needs_node
def test_the_verdict_card_draws_nothing_for_an_older_record_or_a_damaged_one(tmp_path, built_funds_page):
    source = _page_functions(built_funds_page, "VT_COLUMNS", "verdictTable", "verdictHtml")
    out = _run_js(tmp_path, source, "CASES.map(([F, R])=>verdictHtml(F, R))",
                  [[{}, {}], [None, None], [FUNDS_SAMPLE, RACE_SAMPLE], [5, "x"], [[1], [2]],
                   [{"verdict": 5, "fund_test": "x"}, {"verdict": [1]}],
                   [{"fund_test": {"verdict": "no", "looks": 3}}, {"verdict": None}]])
    assert out == [""] * 7


@needs_node
def test_the_verdict_card_says_no_decision_yet_before_the_first_look(tmp_path, built_funds_page):
    """The plan's (iv): one card, "Checkpoint verdict: no decision yet", and no table."""
    F = dict(FUNDS_SAMPLE, verdict={"text": "no decision yet"}, fund_test=dict(
        FUNDS_SAMPLE["fund_test"], looks=[], note=None,
        verdict={"text": "no decision yet", "decided_at": None, "outcome": None}))
    R = dict(RACE_SAMPLE, verdict={"text": "no decision yet"})
    note = dict(F, fund_test=dict(F["fund_test"], note="checkpoint 1: this run had 40 coin-flip funds, not 1,000"))
    source = _page_functions(built_funds_page, "VT_COLUMNS", "verdictTable", "verdictHtml")
    out = _run_js(tmp_path, source, "CASES.map(([F, R])=>verdictHtml(F, R))",
                  [[F, R], [F, RACE_SAMPLE], [FUNDS_SAMPLE, R], [note, R]])
    for html in out:
        assert "<h3>Checkpoint verdict: no decision yet</h3>" in html and "<table" not in html
        assert html.count('class="card verdict"') == 1 and "shadow-funds#the-checkpoint-verdict" in html
    assert "this run had 40 coin-flip funds" in _text(out[3])


@needs_node
def test_the_verdict_card_draws_both_tables_and_the_combined_line(tmp_path, built_funds_page):
    F, R = _verdict_records()
    source = _page_functions(built_funds_page, "VT_COLUMNS", "verdictTable", "verdictHtml")
    out = _run_js(tmp_path, source, "CASES.map(([F, R])=>verdictHtml(F, R))", [[F, R]])
    html, text = out[0], _text(out[0])
    assert html.count('<table class="vt">') == 2 and html.count('<tr class="to">') == 2
    assert "# Rule (section) What is measured Value Bar Result" in text
    # The race: the plan's (i), word for word from the record.
    assert ("Race, checkpoint 1 of 3: 20 independent days (60 entry days), window 2026-09-23 to 2026-12-22, "
            "bar t &gt; 3.47.") in html
    assert "Keep (a), 5 and 5a model − momentum, mean daily net return, Newey-West t, lag 3 t = −3.62 &gt; 3.47 FAIL" in text
    assert "EARLY STOP AT 20: REPLACE THE MODEL WITH MOMENTUM — NOT TESTED IN A DOWNTURN" in text
    # The fund test: the plan's (ii).
    assert "Fund test, checkpoint 1 of 3, read on the race's look day" in text
    assert "NO DECISION AT THIS LOOK — read again at checkpoint 2 (about 2027-03-22; planned bar 2.41)" in text
    # The combined line and its note, then the tables.
    assert "CHECKPOINT 1 (2026-12-22) — race: REPLACE THE MODEL WITH MOMENTUM (early stop)" in text
    assert "NO DECISION YET — waiting for the fund test (checkpoint 2, about 2027-03-22)" in text
    assert "No real money before the June 2027 verdict (section 9)." in text
    assert text.index("CHECKPOINT 1 (2026-12-22)") < text.index("The race") < text.index("The fund test")
    assert "amber" not in html                                              # nothing differs


@needs_node
def test_the_verdict_card_shows_each_tests_deciding_look_else_its_latest(tmp_path, built_funds_page):
    F, R = _verdict_records()
    race_one = R["verdict"]["looks"][0]
    later = dict(race_one, look=2, table=dict(race_one["table"], look=2, title="Race, checkpoint 2 of 3: LATER",
                                              verdict="FOR READING ONLY"))
    decided = dict(R, verdict=dict(R["verdict"], looks=[later, race_one]))            # decided at 1: look 1 shown
    undecided = dict(R, verdict=dict(R["verdict"], decided_at=None, looks=[race_one, later]))  # else the latest
    record = F["fund_test"]["looks"][0]
    skipped = {"look": 2, "made_on": "2027-03-23", "window_end": "2027-03-22", "status": "skipped",
               "table": {"kind": "fund_test", "look": 2, "title": "Fund test, checkpoint 2 of 3: SKIPPED.", "rows": [],
                         "verdict": "SKIPPED. Calibration had not passed on the night the race's look was readable.",
                         "complete": True, "status": "skipped", "outcome": None}}
    with_skip = dict(F, fund_test=dict(F["fund_test"], looks=[record, skipped]))
    differs = dict(R, verdict=dict(R["verdict"], looks=[dict(race_one, differs_tonight="NO DECISION AT THIS LOOK")]))
    moved = dict(F, fund_test=dict(F["fund_test"], looks=[dict(record, bar=3.37, planned_bar=3.40, bar_differs=True)]))
    source = _page_functions(built_funds_page, "VT_COLUMNS", "verdictTable", "verdictHtml")
    out = _run_js(tmp_path, source, "CASES.map(([F, R])=>verdictHtml(F, R))",
                  [[F, decided], [F, undecided], [with_skip, R], [F, differs], [moved, R]])
    assert "Race, checkpoint 1 of 3" in out[0] and "LATER" not in out[0]
    assert "LATER" in out[1] and "Race, checkpoint 1 of 3" not in out[1]
    skip = _text(out[2])
    assert "Fund test, checkpoint 2 of 3: SKIPPED." in skip and "Calibration had not passed" in skip
    assert out[2].count('<table class="vt">') == 1                          # the skipped block has no rows
    assert "Tonight's data reads checkpoint 1 differently: NO DECISION AT THIS LOOK. The frozen table stays." in _text(out[3])
    assert "Bar 3.37 (planned 3.40)" in _text(out[4]) and "log it in the Amendments table" in out[4]


@needs_node
def test_the_verdict_card_escapes_every_string_it_draws(tmp_path, built_funds_page):
    F, R = _verdict_records()
    nasty = '<img src=x onerror="alert(1)">'
    table = R["verdict"]["looks"][0]["table"]
    # Every field of every row (the "→" row keeps its mark, so its own branch draws its rule and result).
    fields = ("n", "rule", "measured", "value", "bar", "result")
    crafted_rows = [dict(r, **{f: nasty for f in fields if not (r["n"] == "→" and f == "n")}) for r in table["rows"]]
    crafted_table = dict(table, title=nasty, rows=crafted_rows)
    assert any(r["n"] == "→" for r in crafted_table["rows"]) and any(r["n"] == nasty for r in crafted_table["rows"])
    crafted_R = dict(R, verdict=dict(R["verdict"], looks=[dict(R["verdict"]["looks"][0], table=crafted_table,
                                                               differs_tonight=nasty)]))
    crafted_F = dict(F, verdict=dict(F["verdict"], line=nasty, note=nasty),
                     fund_test=dict(F["fund_test"], note=nasty))
    # A skipped look's table has no rows: its title and verdict alone.
    skipped_F = dict(F, fund_test=dict(F["fund_test"], looks=[
        {"look": 1, "status": "skipped", "table": {"title": nasty, "rows": [], "verdict": nasty}}]))
    # Before any look: the no-decision card, with the fund test's note.
    waiting_F = dict(F, verdict={"text": "no decision yet"}, fund_test=dict(
        F["fund_test"], looks=[], note=nasty, verdict={"text": "no decision yet", "decided_at": None, "outcome": None}))
    source = _page_functions(built_funds_page, "VT_COLUMNS", "verdictTable", "verdictHtml")
    out = _run_js(tmp_path, source, "CASES.map(([F, R])=>verdictHtml(F, R))",
                  [[crafted_F, crafted_R], [skipped_F, {}], [waiting_F, {}]])
    for html in out:
        assert "<img" not in html and "&lt;img src=x onerror=&quot;alert(1)&quot;&gt;" in html
    assert "no decision yet" in out[2]
    # The fund-test banner, decided: the verdict's words.
    decided = {"status": "running", "start": "2026-09-29", "sessions": 61, "planned_sessions": 180,
               "next_checkpoint": None, "next_look": None, "verdict": {"text": nasty, "decided_at": 1}}
    banner = _run_js(tmp_path, _page_functions(built_funds_page, "nextText", "fundNextText", "fundTestBanner"),
                     "CASES.map(([ft, R])=>fundTestBanner(ft, R))", [[decided, RACE_SAMPLE]])
    assert "<img" not in banner[0] and "decided at checkpoint 1" in banner[0]


def test_the_contract_names_the_checkpoint_verdict_fields():
    text = (ROOT / "dashboard" / "funds.html").read_text()
    comment = text[text.index("<!--") + 4:text.index("-->")]
    for field in ("fund_test.sessions", "fund_test.planned_sessions", "fund_test.next_look", "planned_bar",
                  "fund_test.looks[]", "bar_differs", "fund_test.verdict", "fund_test.note", "decided_at",
                  "differs_tonight", "A Table", "table_json"):
        assert field in comment, field
    assert "fund_test.sessions" not in comment.split("Not read here:")[1]
    page = (ROOT / "dashboard" / "funds.html").read_text()
    assert '<section id="verdict" aria-label="Checkpoint verdict"></section>' in page
    assert page.index('<section id="problems"') < page.index('<section id="verdict"') < page.index('<section id="race-reports"')
    assert 'safely("verdict", ()=>{ $("verdict").innerHTML = verdictHtml(F, R); return []; });' in page


@needs_node
def test_the_counters_card_shows_counts_and_nothing_else(tmp_path, built_funds_page):
    counters = {"ic": {"production": {"answered_lines": 233, "line_days": 4,
                                      "lines_with_score": {"blend": 233, "analyst": 189}},
                       "shadow": {"answered_lines": 0, "line_days": 0, "lines_with_score": {"blend": 0}}},
                "regimes": {"sessions": 4, "first": "2026-09-29", "last": "2026-10-02",
                            "trend": {"above": 4, "below": 0, "unknown": 0}, "vol": "cut-offs not fixed yet"}}
    source = _page_functions(built_funds_page, "countersHtml")
    out = _run_js(tmp_path, source, "CASES.map(countersHtml)",
                  [{"exploratory": {"counters": counters}}, {"exploratory": {"counters": {}}}, {}, None])
    text = _text(out[0])
    assert "Counters until the checkpoints" in text and "no result is shown before a checkpoint" in text
    assert "IC report, production names: 233 answered lines on 4 days" in text and "analyst 189" in text
    assert "shadow stock universe (off until 1 Jan 2027): 0 answered lines" in text
    assert "VT above its 200-day average on 4 sessions" in text and "cut-offs not fixed yet" in text
    assert out[1:] == ["", "", ""]
