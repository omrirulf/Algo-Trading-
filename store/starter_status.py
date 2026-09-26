#!/usr/bin/env python3
"""What the Supabase starter did today, read from its own log.

    python store/starter_status.py                  # today's record, one JSON object on stdout
    python store/starter_status.py --day 2026-09-28

Since 26 Sep 2026 the day's trading run is started by a pg_cron job in the
Supabase project, not by GitHub's cron: at 14:40 UTC it asks GitHub to
dispatch heartbeat.yml (``supabase/heartbeat_starter.sql``), and it writes
one row per request to ``public.starter_log``. GitHub's answer arrives a few
seconds later and a second job copies its status code onto that row. The
answer to a good request is **204** (No Content): GitHub accepted the
dispatch and says nothing else.

The heartbeat run reads that row here, before it writes the book snapshot,
so the daily brief can say whether the starter's own request worked -- the
one thing the run itself cannot see. A run started by a backup (the Claude
bridge, a Routine, the watchdog, GitHub's cron) says only *that* a backup
started it; this says *why* the starter did not: GitHub refused its request
(a 401 is an expired or revoked token), the request never got an answer, or
no request was made at all (the job is not scheduled, or the project is
paused).

It prints, and the workflow redirects that into ``logs/starter_status.json``:

* ``{"day", "requested_at", "status_code", "error"}`` from today's latest
  request; ``status_code`` is null while no answer has been copied yet;
* ``{"day", "status": "unknown", "why"}`` when there is nothing to read:
  the secrets are not set, the project did not answer, the table is not
  there, or the starter made no request today.

Read-only, and it never fails: every answer exits 0. Only the status code
and a short, checked error text are ever written -- never a header, never
the response body, never the token (which lives only in Supabase Vault and
is never in this table in the first place). The Supabase key is read the
one way it may be, through ``store.remote.RemoteArchive``.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Optional

# Allow ``python store/starter_status.py`` from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from store.remote import (  # noqa: E402
    NOT_CONFIGURED, RemoteArchive, RemoteArchiveError, describe_failure,
)

#: The starter's log, written by ``public.start_heartbeat()``.
TABLE = "starter_log"

#: The starter's name on every row it writes; the same token the heartbeat's
#: run block records for a run it started (``analysis/cycle_day.py``).
SOURCE = "supabase-cron"

#: How much of an error text is kept. pg_net's errors are one short line
#: ("Timeout of 10000 ms reached"); anything longer is not one of those.
MAX_ERROR_CHARS = 160

#: Text that must never be written, whatever the error says: a GitHub token
#: (classic, fine-grained, app or OAuth), a bearer header, an API key header.
#: The token is never put in the table, so this should never match; if it
#: ever does, the error is withheld whole rather than trimmed around.
_SECRET_LOOKING = re.compile(
    r"(gh[pousr]_[A-Za-z0-9]|github_pat_|bearer\s|authorization|apikey|eyJ[A-Za-z0-9_-]{8,})",
    re.IGNORECASE,
)


def query(day: date) -> dict[str, str]:
    """The PostgREST query for ``day``'s requests, newest first, five at most."""
    return {
        "select": "requested_at,source,request_id,status_code,error",
        "requested_at": f"gte.{day.isoformat()}T00:00:00Z",
        "order": "requested_at.desc",
        "limit": "5",
    }


def unknown(day: date, why: str) -> dict[str, Any]:
    return {"day": day.isoformat(), "status": "unknown", "why": why}


def _moment(value: Any) -> Optional[datetime]:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        moment = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=timezone.utc)
    return moment.astimezone(timezone.utc)


def clean_error(value: Any) -> Optional[str]:
    """An error text safe to commit and to send to a phone, or None.

    One line, at most ``MAX_ERROR_CHARS``; withheld whole if anything in it
    looks like a credential.
    """
    if not isinstance(value, str):
        return None
    text = " ".join(value.split())
    if not text:
        return None
    if _SECRET_LOOKING.search(text):
        return "error text withheld: it looked like it held a credential"
    return text[:MAX_ERROR_CHARS]


def status_from_rows(rows: Any, day: date) -> dict[str, Any]:
    """Today's record from the rows PostgREST returned.

    The newest request made on ``day`` (UTC) by the starter. A row whose
    time cannot be read, or that is from another day, is left out: this
    answers "what did the starter do today", nothing else.
    """
    todays = []
    for row in rows if isinstance(rows, list) else ():
        if not isinstance(row, dict):
            continue
        at = _moment(row.get("requested_at"))
        if at is None or at.date() != day:
            continue
        if row.get("source") not in (None, SOURCE):
            continue
        todays.append((at, row))
    if not todays:
        return unknown(day, "the starter recorded no request today")
    at, row = max(todays, key=lambda pair: pair[0])
    code = row.get("status_code")
    return {
        "day": day.isoformat(),
        "requested_at": at.isoformat(timespec="seconds"),
        "status_code": code if isinstance(code, int) and not isinstance(code, bool) else None,
        "error": clean_error(row.get("error")),
    }


def read(day: date, archive: Optional[RemoteArchive] = None) -> dict[str, Any]:
    """Today's record, or why there is none. Never raises."""
    if archive is None:
        if not RemoteArchive.is_configured():
            return unknown(day, f"{NOT_CONFIGURED}: SUPABASE_URL / SUPABASE_SERVICE_KEY are not set")
        try:
            archive = RemoteArchive.from_settings()
        except RemoteArchiveError:
            return unknown(day, NOT_CONFIGURED)
    try:
        rows = archive.rows(TABLE, query(day))
    except RemoteArchiveError as exc:
        why = describe_failure(exc)
        if getattr(exc, "status", None) == 404:
            why += ": no starter_log table (supabase/heartbeat_starter.sql not applied?)"
        return unknown(day, why)
    except Exception as exc:  # noqa: BLE001 - a record of the starter must never fail the run
        return unknown(day, f"could not read the starter's log ({type(exc).__name__})")
    return status_from_rows(rows, day)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="starter_status", description="What the Supabase starter did today, as one JSON object.",
    )
    parser.add_argument("--day", default=None, help="ISO date, default today in UTC")
    args = parser.parse_args(argv)
    try:
        day = date.fromisoformat(args.day) if args.day else datetime.now(timezone.utc).date()
    except ValueError:
        parser.error(f"--day is not an ISO date: {args.day!r}")
    print(json.dumps(read(day)))
    return 0


__all__ = ["SOURCE", "TABLE", "clean_error", "query", "read", "status_from_rows", "unknown"]


if __name__ == "__main__":
    raise SystemExit(main())
