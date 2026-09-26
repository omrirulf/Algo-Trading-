"""The guardrail that keeps the archive out of everything that scores or trades, and its SQL.

The CI step "Nothing that scores or trades can read the archive" is Python
inside a workflow file, so it is tested the only honest way: its own code,
lifted out of ci.yml and run against a small tree that breaks the rule in
each way it forbids -- and against the real repository, which must pass.
Then the SQL: the migration and the schema describe the same tables, every
one of them closed to the publishable key, the bucket private, and the
stored copy of every line gone.
"""

from __future__ import annotations

import re
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
STEP = "Nothing that scores or trades can read the archive"
MIGRATION = ROOT / "supabase" / "2026-09-26_archive_capture.sql"
XZ_MIGRATION = ROOT / "supabase" / "2026-09-26_model_io_xz.sql"
SCHEMA = ROOT / "store" / "remote_schema.sql"
NEW_TABLES = ("account_snapshots", "account_fills", "model_calls", "model_io_files",
              "scoring_prices", "scoring_runs")


def _step_python() -> str:
    steps = yaml.safe_load((ROOT / ".github/workflows/ci.yml").read_text())["jobs"]["guardrails"]["steps"]
    run = next(s["run"] for s in steps if s.get("name") == STEP)
    body = run.split("python3 - <<'PY'\n", 1)[1].split("\nPY\n", 1)[0]
    return textwrap.dedent(body)


def _check(tree: Path) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-c", _step_python()], cwd=tree, capture_output=True, text=True,
                          timeout=120)


def _tree(tmp_path: Path, files: dict[str, str]) -> Path:
    base = {
        "analysis/__init__.py": "", "analysis/horse_race.py": "from analysis import helper\n",
        "analysis/helper.py": "X = 1\n", "shadow/__init__.py": "", "shadow/run.py": "import shadow.market\n",
        "shadow/market.py": "", "shadow/smoke.py": "", "store/__init__.py": "", "store/remote.py": "",
        "config/__init__.py": "", "config/settings.py": 'MODEL_IO_DIR = "logs/model_io"\n',
    }
    for name, text in {**base, **files}.items():
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    return tmp_path


def test_the_repository_passes_it():
    done = _check(ROOT)
    assert done.returncode == 0, done.stdout + done.stderr
    assert "OK: nothing that scores or trades reads the archive" in done.stdout


def test_a_clean_small_tree_passes(tmp_path):
    done = _check(_tree(tmp_path, {}))
    assert done.returncode == 0, done.stdout + done.stderr


@pytest.mark.parametrize("path, source", [
    ("analysis/bad.py", "from store import remote\n"),
    ("shadow/bad.py", "import store.push_remote\n"),
    ("rules/bad.py", "from store.starter_status import read\n"),
    ("learn/bad.py", "from store.model_calls import package\n"),
    ("replay/bad.py", "import store.scoring_prices as sp\n"),
    ("orchestrator/bad.py", "def f():\n    from store.remote import RemoteArchive\n"),
])
def test_an_import_of_the_archive_side_is_caught(tmp_path, path, source):
    done = _check(_tree(tmp_path, {path: source}))
    assert done.returncode != 0
    assert "imports the archive's side of store/" in done.stdout + done.stderr
    assert path in done.stdout


def test_the_local_index_side_of_store_is_not_forbidden(tmp_path):
    """store.loader and store.database never touch Supabase; importing them is not reading the archive."""
    done = _check(_tree(tmp_path, {"analysis/fine.py": "from store import loader, database\n",
                                   "store/loader.py": "", "store/database.py": ""}))
    assert done.returncode == 0, done.stdout + done.stderr


@pytest.mark.parametrize("helper", [
    'STATUS = "logs/archive_status.json"\n',
    'import json\ndef f(p):\n    return json.loads(open(p / "starter_status.json").read())\n',
    "from config import settings\nDIR = settings.MODEL_IO_DIR\n",
])
def test_a_module_behind_the_race_that_names_an_archive_file_is_caught(tmp_path, helper):
    done = _check(_tree(tmp_path, {"analysis/helper.py": helper}))
    assert done.returncode != 0
    assert "the race or the funds can reach something the archive's side writes" in done.stdout + done.stderr


def test_prose_about_those_files_is_not_a_read(tmp_path):
    done = _check(_tree(tmp_path, {"analysis/helper.py": '"""Never reads logs/archive_status.json."""\n'}))
    assert done.returncode == 0, done.stdout + done.stderr


def test_the_step_also_keeps_every_secret_out_of_the_race_and_funds_workflows():
    steps = yaml.safe_load((ROOT / ".github/workflows/ci.yml").read_text())["jobs"]["guardrails"]["steps"]
    run = next(s["run"] for s in steps if s.get("name") == STEP)
    assert "grep -nE 'secrets\\.' .github/workflows/horse-race.yml .github/workflows/funds.yml " \
           ".github/workflows/funds-smoke.yml" in run


# --------------------------------------------------------------------------- #
# The SQL
# --------------------------------------------------------------------------- #


def _table(sql: str, name: str) -> str:
    match = re.search(rf"create table if not exists public\.{name} \((.*?)\n\);", sql, flags=re.S)
    assert match, name
    return match.group(1)


def test_the_migration_and_the_schema_make_the_same_new_tables():
    migration, schema = MIGRATION.read_text(), SCHEMA.read_text()
    # The later migration (xz, the same day) renames one column; a project
    # brought up to date by both files matches a fresh schema.
    later = XZ_MIGRATION.read_text()
    assert "rename column gz_bytes to compressed_bytes" in later
    migration_after = migration.replace("    gz_bytes     bigint,", "    compressed_bytes  bigint,")
    for name in NEW_TABLES:
        assert _table(migration_after, name) == _table(schema, name), name
        assert f"alter table public.{name} enable row level security;" in migration
        assert f"alter table public.{name} enable row level security;" in schema


def test_the_migration_drops_the_stored_copy_and_parses_on_read_behind_the_callers_permissions():
    sql = MIGRATION.read_text().lower()
    code = "\n".join(line for line in sql.splitlines() if not line.lstrip().startswith("--"))
    assert "alter table public.signals drop column if exists raw_json;" in code
    assert "alter table public.executions drop column if exists raw_json;" in code
    assert "cascade" not in code                              # nothing of the owner's goes silently
    # decisions is dropped before the column and made again after it.
    assert code.index("drop view if exists public.decisions") < code.index("drop column if exists raw_json")
    assert code.index("drop column if exists raw_json") < code.index("create or replace view public.decisions")
    for view in ("decisions", "signals_json", "executions_json"):
        assert code.index(f"create or replace view public.{view}") < code.index(
            f"alter view public.{view} set (security_invoker = on);")
    assert "vacuum" not in code                               # it cannot run in the transaction...
    assert "vacuum full public.signals;" in sql               # ...so it is named, to run on its own
    assert code.strip().startswith("begin;") and code.strip().endswith("commit;")


def test_the_bucket_is_private_and_nothing_opens_a_policy():
    for path in (MIGRATION, SCHEMA):
        code = "\n".join(l for l in path.read_text().lower().splitlines() if not l.lstrip().startswith("--"))
        assert "values ('model-io', 'model-io', false," in code
        assert "set public = false" in code
        assert "create policy" not in code and "grant " not in code
    # And every view in the schema enforces the caller's permissions.
    schema = SCHEMA.read_text().lower()
    views = re.findall(r"create or replace view public\.(\w+)", schema)
    assert sorted(views) == ["decisions", "executions_json", "signals_json"]
    for view in views:
        assert f"alter view public.{view} set (security_invoker = on);" in schema


def test_every_column_a_row_builder_sends_exists_in_the_schema():
    """A key the table lacks is a failed push (PostgREST's PGRST204). Checked for every new table."""
    import json

    from store import loader, model_calls, scoring_prices

    schema = SCHEMA.read_text()

    def columns(name):
        return {line.split()[0] for line in _table(schema, name).splitlines() if line.strip()}

    snapshot = json.dumps({"at": "2026-09-25T16:21:20Z", "account": {}, "fills": [{"id": "f", "at": None}]})
    assert set(loader.account_row(snapshot)) == columns("account_snapshots")
    assert set(loader.fill_rows(snapshot)[0]) == columns("account_fills")
    assert set(model_calls.call_row({"call_id": "c"}, "x")) == columns("model_calls")
    package = model_calls.Package(source=Path("x"), object_path="2026/09/2026-09-26/x.jsonl.xz", data=b"",
                                  sha256="0")
    assert set(package.file_row("1")) == columns("model_io_files")
    tape = {"consumer": "funds", "prices_sha256": "0" * 64, "coverage": {},
            "rows": [{"instance": "ohlc", "kind": "ohlc", "ticker": "VT", "date": "2026-09-18", "open": 1.0,
                      "high": 1.0, "low": 1.0, "close": 1.0, "dividends": 0.0}]}
    assert set(scoring_prices.price_rows(tape, "1")[0]) == columns("scoring_prices")
    assert set(scoring_prices.run_row(tape, "1")) == columns("scoring_runs")
    # And the two old tables still take exactly what the loader sends.
    from tests.test_store_loader import AUDIT_LINE, JOURNAL_LINE, line

    assert set(loader.signal_row(line(JOURNAL_LINE))) == columns("signals")
    assert set(loader.execution_row(line(AUDIT_LINE))) == columns("executions")
