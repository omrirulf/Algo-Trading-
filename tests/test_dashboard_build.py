"""The dashboard pages are built from their templates and the snapshots."""

from __future__ import annotations

import importlib.util
import json
import re
import shutil
import subprocess
import sys
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
    assert "proposed, not approved" in text


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
HELPERS = ("isNum", "esc", "money", "kMoney", "signed", "plain", "pts", "tone", "bar2", "day", "israel",
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
    four_broken = _calibration("passed") | {"integrity": {
        "four": {"ok": False, "problems": ["model: EWZ stops cover 10 of 40"]},
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

    assert "The four funds' integrity check:</span> model: EWZ stops cover 10 of 40" in cards[1]
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
    source = _page_functions(built_funds_page, "verdictRow", "ruleHtml", "verdictsHtml", "renderCalibration")
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
                  "estimated", "bar", "looks[]", "reached", "reason"):
        assert field in comment, field


def test_long_alarm_text_wraps_on_the_desk():
    desk = (ROOT / "dashboard" / "template.html").read_text()
    # A flex child's min-width defaults to its content, so one long word in
    # an alarm pushed the desk wider than a phone. The text box may shrink
    # now, and a long word breaks inside it.
    assert ".stripe > div{min-width:0;overflow-wrap:anywhere}" in desk
