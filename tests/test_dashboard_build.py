"""The dashboard page is built from the template and the book snapshot."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

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
    assert names == ["icon-192.png", "icon-512.png", "icon.svg", "index.html", "manifest.webmanifest", "sw.js"]
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
    assert any("dashboard/build.py --site _site" in r for r in runs)
    publish = next(r for r in runs if "git push" in r)
    assert "gh-pages" in publish and "git init -q -b gh-pages" in publish     # one commit, rewritten each time
    assert "touch .nojekyll" in publish
    assert "${GH_TOKEN}" in publish and "echo" not in publish.split("git push")[1]


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
    assert "<\\/script>" in data               # the closing tag inside the data is escaped ...
    assert "</script>" not in data               # ... so it cannot end the script block early


def test_the_build_never_reaches_a_broker_or_the_network():
    source = (ROOT / "dashboard" / "build.py").read_text()
    for banned in ("broker_client", "alpaca", "anthropic", "httpx", "requests", "urllib"):
        assert banned not in source, banned
