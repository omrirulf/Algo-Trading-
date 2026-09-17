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
    assert '"logs/book.json"' in text and '"get_file_contents"' in text
    assert "<title>Algo Trading Desk</title>" in text


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
