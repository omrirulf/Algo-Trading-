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
    assert "Fund test:</b> not started (it starts the first trading day after calibration passes)" in text
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
HELPERS = ("isNum", "esc", "money", "kMoney", "signed", "plain", "pts", "tone", "bar2", "asObj", "day", "israel",
           "HUE", "SHORT", "DASH", "key", "bandKey", "plotHost", "tiles", "VERDICT", "warnIcon")

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
    # "four" keeps its name but also checks the two exploratory funds
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

    label = "The funds' integrity check (the four and the two exploratory):</span> "
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
    assert "the first one lands after the first close" not in shown
    assert "the first one lands after the first close" in pages[1]                    # no problem: the usual line
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
def test_the_fund_test_is_read_at_the_races_next_look(tmp_path, built_funds_page):
    ft = {"status": "running", "start": "2027-01-04", "sessions": 7, "independent": 2, "next_checkpoint": None}
    own = dict(ft, next_checkpoint={"independent": 30, "entry_days": 90, "estimated": "2027-03-01", "bar": 2.5})
    decided = dict(RACE_SAMPLE, decided=True, next=None, outcome_text="The model beat both rules.")
    source = _page_functions(built_funds_page, "nextText", "fundTestBanner")
    out = _run_js(tmp_path, source, "CASES.map(([ft, R])=>fundTestBanner(ft, R))",
                  [[ft, RACE_SAMPLE], [own, RACE_SAMPLE], [ft, {}], [ft, decided],
                   [{"status": "not_started", "next_checkpoint": None}, RACE_SAMPLE]])
    assert "Next checkpoint: 12 Nov 2026, bar t &gt; 2.96" in out[0] and "the race's next look" in out[0]
    assert "No checkpoint left to reach" not in out[0]
    assert "Next checkpoint: 1 Mar 2027, bar t &gt; 2.50" in out[1]                    # its own, when it has one
    assert "No checkpoint left to reach" not in out[2] and "decision gate writes its record" in out[2]
    assert "No checkpoint left to reach" in out[3]                                     # the race has no look left
    assert "not started" in out[4]


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
    assert "Report only: the buying order (watchlist order) is not changed." in card
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
#: days since: day 15 or the fix + 5 days is now day 17, and the fund test's
#: plan has moved off the registered one.
WITH_FIX = {
    "days_done": 8, "days_needed": 17, "days_passed": 5,
    "fixes": [{"day": "2026-10-05", "what": "an earlier fix"},
              {"day": "2026-10-12", "what": "stops re-placed <b>after</b> a partial fill"}],
    "last_fix": "2026-10-12", "days_since_fix": 2, "days_after_fix_needed": 5, "end_estimate": "2026-10-23",
    "fund_test_plan": {"start": "2026-10-26", "sessions": [41, 101, 161], "bars": [3.91, 2.52, 2.01],
                       "exact": [3.912, 2.518, 2.006], "registered": [3.8, 2.5, 2.0],
                       "registered_start": "2026-10-19", "matches_registered": False},
}
#: The same fields with nothing fixed: the plan is still the registered one.
NO_FIX = {
    "days_done": 4, "days_needed": 15, "days_passed": 4, "fixes": [], "last_fix": None, "days_since_fix": None,
    "days_after_fix_needed": 5, "end_estimate": "2026-10-16",
    "fund_test_plan": {"start": "2026-10-19", "sessions": [46, 106, 166], "bars": [3.8, 2.5, 2.0],
                       "exact": [3.797, 2.501, 1.999], "registered": [3.8, 2.5, 2.0],
                       "registered_start": "2026-10-19", "matches_registered": True},
}


def _text(html: str) -> str:
    """The page's text, as a reader sees it: each tag a space, runs of space as one."""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


@needs_node
def test_calibration_says_the_days_passed_the_last_fix_and_the_days_since_it(tmp_path, built_funds_page):
    null_bar = json.loads(json.dumps(WITH_FIX))
    null_bar["fund_test_plan"]["bars"] = [None, 2.6, 2.05]
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
        assert "Calibration ends at day 15 or 5 days after the last fix, whichever is later." in text
        assert "If nothing more fails, it ends 23 Oct 2026." in text
        assert "All 2 fixes" in text
        assert "Fund test would start 26 Oct 2026; bars 3.91, 2.52, 2.01" in text
        # The plan moved: an amber note, in the owner's words, with what was registered.
        assert 'class="amber"' in html
        assert "differs from the registered start/bars: they must be re-registered before the fund test starts" in text
        assert "Registered: start 19 Oct 2026; bars 3.80, 2.50, 2.00." in text

    text = _text(clean)
    assert "Days passed: 4 of 15" in text and "No fix yet" in text
    assert "Days since the last fix" not in text and " of 5" not in text          # "X of 5" only with a fix
    assert "Calibration ends at day 15 or 5 days after the last fix, whichever is later." in text
    assert "Fund test would start 19 Oct 2026; bars 3.80, 2.50, 2.00" in text
    assert 'class="amber"' not in clean and "re-registered" not in text
    assert "The same start and bars as registered." in text
    assert "fixes" not in text                                                     # no list of fixes to open

    assert "bars none, 2.60, 2.05" in _text(null_bars)                             # a look before the start has no bar

    assert out[4:10] == ["", "", "", "", "", ""]                                   # old, not started, missing: nothing
    odd = _text(out[10])
    assert "No fix yet" in odd and "Days passed" not in odd and "Fund test would start" not in odd


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
    assert "must be re-registered before the fund test starts" in text
    old_text = _text(pages[1])
    assert "3 of 15 closes compared" in old_text
    assert "Days passed" not in old_text and "No fix yet" not in old_text and "Fund test would start" not in old_text


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
    assert "Exploratory: does the order or the size matter?" in text
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
    assert re.search(r"The decision race's trades since 23 Sept? 2026, after costs\.", text)   # "Sep" or "Sept"
    assert 'A group or side reads "too few" until it has 20 trades.' in text
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
