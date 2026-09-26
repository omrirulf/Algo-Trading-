"""Push the archive to a remote Postgres, over Supabase's REST interface.

This is the half SQLite does not solve. The local index makes the logs
*queryable*; it does not stop them being the thing git has to carry forever.
A remote archive does, and it is readable from anywhere without a clone.

Three properties shape everything below.

**It is never in the trading path.** The heartbeat writes its JSON-lines exactly
as before, and the push is a separate step afterwards. A failed push costs
nothing: the lines are already on disk and already committed, and the next
push catches up. That is why the credential lives here rather than in
``orchestrator/journal.py`` -- which a CI invariant forbids from reading one at
all, and rightly: journalling must not be able to fail a cycle, and a network
call is a thing that fails.

**It is idempotent, by the same key as the local index.** ``line_hash`` is the
remote primary key, and the insert is ``on conflict do nothing``. Re-sending a
line the remote already has is free, so the push does not have to be exact
about where it left off -- it only has to not miss anything.

**It shares the row builders.** Rows come from ``store.loader``, the same
functions that fill SQLite, which come in turn from the same parser the scorer
uses. One line of the journal cannot mean three different things in three
places.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Iterable, Optional, Sequence

import httpx

log = logging.getLogger(__name__)

#: PostgREST rejects an over-large body, and journal rows carry a full context
#: apiece -- several kilobytes each. 200 keeps a batch comfortably small
#: without making a backfill take thousands of round trips.
BATCH_SIZE = 200

REQUEST_TIMEOUT_SECONDS = 30.0

SIGNALS = "signals"
EXECUTIONS = "executions"


def _is_legacy_jwt(key: str) -> bool:
    """Whether ``key`` is one of the old JWT-based keys (``anon``/``service_role``).

    A JWT is three base64url parts joined by dots, and a JSON header always
    base64-encodes to a string starting ``eyJ``. The new keys look nothing like
    that: ``sb_secret_...`` and ``sb_publishable_...`` are opaque strings.
    """
    parts = key.split(".")
    return key.startswith("eyJ") and len(parts) == 3 and all(parts)


def auth_headers(key: str) -> dict[str, str]:
    """The headers that authenticate a request with ``key``, for either kind of key.

    Supabase has two kinds of API key. The legacy ``service_role`` key is a JWT
    and was sent twice: as ``apikey`` and as ``Authorization: Bearer``. The new
    secret key (``sb_secret_...``) is not a JWT, and Supabase's migration guide
    says to send it on the ``apikey`` header **only**: "If you also pass the key
    on the Authorization: Bearer header ... the platform tries to parse it as a
    JWT and rejects the request". The legacy keys keep working only until the
    end of 2026 (the same guide), and this archive has to outlive that, so the
    push must work with the new key.

    Measured against this project on 26 Sep 2026, from inside its own database
    through pg_net, with the new-format publishable key (which follows the same
    header rule as the secret key):

    * the key on ``apikey`` alone: HTTP 200;
    * the key on ``apikey`` and the SAME value on ``Bearer``: HTTP 200 -- the
      gateway tolerates an exact copy, although the guide says not to rely on
      it (and Edge Functions do reject it);
    * a DIFFERENT non-JWT value on ``Bearer``: HTTP 401, PostgREST's
      "Expected 3 parts in JWT; got 1";
    * a made-up ``sb_secret_`` key on ``apikey``: HTTP 401 "Invalid API key" --
      the gateway checks the new keys itself.

    So: ``apikey`` always, ``Authorization`` only for a legacy JWT key, where it
    is still what the old key needs. Nothing else about the request changes.
    """
    headers = {"apikey": key}
    if _is_legacy_jwt(key):
        headers["Authorization"] = f"Bearer {key}"
    return headers


class RemoteArchiveError(RuntimeError):
    """The remote refused, or could not be reached.

    ``status`` is the HTTP status the remote answered with, or None when it
    never answered (a refused connection, a timeout, a name that does not
    resolve). Carried apart from the message so a caller can say what went
    wrong in a few words -- "HTTP 401", "project paused or unreachable" --
    without repeating the message, which holds the remote's own text.
    """

    def __init__(self, message: str, status: Optional[int] = None) -> None:
        super().__init__(message)
        self.status = status


@dataclass
class PushResult:
    """What one push did, counted from what the remote said it stored."""

    table: str
    #: Rows the remote reports it actually inserted.
    inserted: int = 0
    #: Rows sent that the remote already had. Not an error -- the expected
    #: result of an overlapping window.
    already_present: int = 0

    @property
    def sent(self) -> int:
        return self.inserted + self.already_present

    def describe(self) -> str:
        return (
            f"{self.table}: {self.inserted} pushed, "
            f"{self.already_present} already there ({self.sent} sent)"
        )


class RemoteArchive:
    """A Supabase project, addressed through PostgREST.

    Over HTTP rather than a Postgres driver on purpose: ``httpx`` is already a
    dependency of this project and already the way it talks to every other
    service, so this adds a backend without adding a package -- and without
    putting a database driver into an image that also runs the trading cycle.
    """

    def __init__(
        self,
        url: str,
        service_key: str,
        client: httpx.Client | None = None,
    ) -> None:
        url = (url or "").strip().rstrip("/")
        service_key = (service_key or "").strip()
        if not url or not service_key:
            raise RemoteArchiveError(
                "a remote archive needs SUPABASE_URL and SUPABASE_SERVICE_KEY. "
                "Leave them unset to keep everything local."
            )
        self._url = url
        self._key = service_key
        self._client = client

    @classmethod
    def from_settings(cls, client: httpx.Client | None = None) -> "RemoteArchive":
        """Build from the configured credential.

        The only place in this project that reads the Supabase key, mirroring
        how ``broker_client.py`` is the only place that reads the broker's. A
        CI invariant enforces it: a credential with exactly one reader is one
        whose blast radius can be reasoned about.
        """
        from config.settings import get_settings

        settings = get_settings()
        return cls(settings.supabase_url, settings.supabase_service_key, client=client)

    @staticmethod
    def is_configured() -> bool:
        """Whether a remote is set up at all. Absent is a state, not an error."""
        from config.settings import get_settings

        settings = get_settings()
        return bool(settings.supabase_url.strip() and settings.supabase_service_key.strip())

    # -- reads ------------------------------------------------------------- #

    def latest_timestamp(self, table: str) -> Optional[str]:
        """The newest ``ts_utc`` the remote holds, or None if it holds nothing.

        This is the high-water mark the push starts from. It is read from the
        remote rather than tracked locally because the runner is discarded
        after every cycle -- any local bookmark would be wrong on the next one.
        """
        response = self._request(
            "GET",
            table,
            params={
                "select": "ts_utc",
                "order": "ts_utc.desc.nullslast",
                "limit": "1",
            },
        )
        payload = self._json(response)
        if not isinstance(payload, list) or not payload:
            return None
        row = payload[0]
        value = row.get("ts_utc") if isinstance(row, dict) else None
        return value if isinstance(value, str) and value.strip() else None

    def rows(self, table: str, params: dict[str, str]) -> list[dict[str, Any]]:
        """The rows a PostgREST query on ``table`` returns, as dicts.

        A read for the heartbeat's own bookkeeping (``store/starter_status.py``
        reads the Supabase starter's log with it), through the same one
        reader of the key as every push. An answer that is not a list of
        objects is an empty list: the caller says "no row", it does not guess.
        """
        payload = self._json(self._request("GET", table, params=params))
        if not isinstance(payload, list):
            return []
        return [row for row in payload if isinstance(row, dict)]

    def count(self, table: str) -> Optional[int]:
        """Row count, from the Content-Range header PostgREST returns."""
        response = self._request(
            "GET", table, params={"select": "line_hash", "limit": "1"},
            headers={"Prefer": "count=exact"},
        )
        content_range = response.headers.get("content-range", "")
        _, _, total = content_range.partition("/")
        try:
            return int(total)
        except ValueError:
            return None

    # -- writes ------------------------------------------------------------ #

    def push(self, table: str, rows: Sequence[dict[str, Any]]) -> PushResult:
        """Insert rows the remote does not already have.

        Counts come from what the remote echoes back, not from what was sent:
        with ``resolution=ignore-duplicates`` the response carries exactly the
        rows that were actually written, so "pushed" means stored rather than
        attempted.
        """
        result = PushResult(table=table)
        for batch in _batched(rows, BATCH_SIZE):
            response = self._request(
                "POST",
                table,
                params={"on_conflict": "line_hash", "select": "line_hash"},
                headers={
                    "Content-Type": "application/json",
                    # ignore-duplicates is the idempotence; representation is
                    # what makes the count honest rather than assumed.
                    "Prefer": "resolution=ignore-duplicates,return=representation",
                },
                json=list(batch),
            )
            stored = self._json(response)
            inserted = len(stored) if isinstance(stored, list) else 0
            result.inserted += inserted
            result.already_present += len(batch) - inserted
        return result

    # -- plumbing ---------------------------------------------------------- #

    def _request(
        self,
        method: str,
        table: str,
        params: dict[str, str] | None = None,
        headers: dict[str, str] | None = None,
        json: Any = None,
    ) -> httpx.Response:
        url = f"{self._url}/rest/v1/{table}"
        # The new secret key goes on ``apikey`` only; see auth_headers.
        merged = {**auth_headers(self._key), **(headers or {})}
        try:
            if self._client is not None:
                response = self._client.request(
                    method, url, params=params, headers=merged, json=json
                )
            else:
                with httpx.Client(timeout=REQUEST_TIMEOUT_SECONDS) as client:
                    response = client.request(
                        method, url, params=params, headers=merged, json=json
                    )
        except httpx.HTTPError as exc:
            raise RemoteArchiveError(f"{method} {table} failed: {exc}") from exc

        if response.status_code >= 400:
            # The body carries PostgREST's actual complaint (a missing table, a
            # type mismatch). The status alone has sent people to the wrong
            # problem often enough to be worth the extra 300 characters.
            raise RemoteArchiveError(
                f"{method} {table} returned HTTP {response.status_code}: "
                f"{response.text[:300]}",
                status=response.status_code,
            )
        return response

    @staticmethod
    def _json(response: httpx.Response) -> Any:
        try:
            return response.json()
        except ValueError:
            return None


#: What a caller writes down when the remote is not set up at all.
NOT_CONFIGURED = "not configured"

#: What a caller writes down when the project did not answer as a database:
#: no answer at all (a refused connection, a timeout, a name that does not
#: resolve), a gateway that could not reach it (502, 503, 504), or one of
#: the 52x-59x answers a proxy in front of a stopped backend gives. A free
#: Supabase project that nothing touched for a week is paused, and a paused
#: project answers this way until someone restores it (Supabase answers a
#: paused project's API with its own 540). The owner is told to restore it.
UNREACHABLE = "project paused or unreachable"


def describe_failure(exc: RemoteArchiveError) -> str:
    """A remote failure in a few words, never the remote's own text.

    ``project paused or unreachable`` or ``HTTP <code>``. Only the status
    number is used: the message can hold the project's URL and whatever the
    server said, and this text is committed to a public repository and sent
    to a phone. The key is never in either, but a few fixed words are
    easier to prove safe than a truncated message.
    """
    status = getattr(exc, "status", None)
    if not isinstance(status, int) or status in (502, 503, 504) or status >= 520:
        return UNREACHABLE
    return f"HTTP {status}"


def _batched(rows: Sequence[dict[str, Any]], size: int) -> Iterable[Sequence[dict]]:
    for start in range(0, len(rows), size):
        yield rows[start : start + size]


def select_new(
    rows: Sequence[dict[str, Any]], since: Optional[str]
) -> list[dict[str, Any]]:
    """Rows at or after the remote's high-water mark.

    Inclusive at the boundary, and that is the point: several rows can share a
    timestamp, so an exclusive comparison would drop the siblings of whichever
    one happened to be newest. The overlap it creates costs nothing, because
    ``on conflict do nothing`` absorbs it.

    Rows with no timestamp are always sent. There is no honest way to place
    them relative to a watermark, and the alternative -- dropping them -- would
    quietly lose exactly the malformed cycles most worth looking at.
    """
    if not since:
        return list(rows)
    cutoff = _moment(since)
    if cutoff is None:
        # An unparseable watermark is not a reason to guess. Send everything
        # and let the content hash sort it out.
        return list(rows)

    picked = []
    for row in rows:
        raw = row.get("ts_utc")
        if not raw:
            picked.append(row)
            continue
        moment = _moment(str(raw))
        if moment is None or moment >= cutoff:
            picked.append(row)
    return picked


def _moment(value: str) -> Optional[datetime]:
    """Parse an ISO-8601 instant, or None.

    Compared as datetimes rather than as strings, because the two sides do not
    agree on spelling. Python's ``isoformat`` pads to microseconds
    (``...02.331000+00:00``); Postgres renders a timestamptz with trailing
    zeros trimmed (``...02.331+00:00``); and an offset may be written ``Z``.

    Not every mismatch actually breaks a text comparison -- the trimmed-zeros
    pair happens to survive it, since ``0`` sorts above ``+``. A ``Z`` suffix
    does not: ``"...02+00:00" >= "...02Z"`` is false for every row, so a
    watermark in that spelling would quietly send nothing at all. An
    unparseable watermark is worse again, silently dropping everything with a
    timestamp.

    Both were real against the string version and are pinned by tests. Parsing
    removes the class rather than the two instances: the failure mode here is
    rows never sent, in an archive nobody watches closely enough to spot a gap.
    """
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None


__all__ = [
    "BATCH_SIZE",
    "EXECUTIONS",
    "NOT_CONFIGURED",
    "SIGNALS",
    "UNREACHABLE",
    "PushResult",
    "RemoteArchive",
    "RemoteArchiveError",
    "describe_failure",
    "select_new",
]
