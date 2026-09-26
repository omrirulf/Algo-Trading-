"""What a credential looks like, for the checks that keep one out of the record.

One list, used twice: by the model-call capture in the cycle
(``orchestrator/model_io.py``), which withholds a record before it is ever
written to disk, and by the archive push (``store/model_calls.py``), which
checks every record again before it leaves the runner. Here rather than in
either package because the cycle may not import ``store/`` (a CI guardrail)
and ``store/`` should not import the cycle; ``config`` is below both.

Nothing in this module reads a credential. It only knows their shapes:

* the prefixes the providers put on their keys -- Supabase's new keys
  (``sb_secret_``, ``sb_publishable_``) and access tokens (``sbp_``), GitHub
  tokens, Anthropic and OpenAI-style keys (``sk-``), Groq (``gsk_``), Google
  (``AIza``), AWS access key ids, Slack tokens, and Alpaca's key ids;
* a JSON Web Token (three base64url parts, the first starting ``eyJ``), which
  is what the legacy Supabase keys are;
* a header written out with its value: ``Bearer <token>``, or
  ``authorization`` / ``apikey`` / ``x-api-key`` followed by ``:`` or ``=``
  and a long token.

The last kind asks for the value too, on purpose. The records this checks
are full model prompts, which carry news: "Emergency Use Authorization" is a
headline, not a header. A bare word would withhold whole days of prompts for
nothing, and a check that cries wolf is a check people learn to switch off.

It is a net, not a proof: a key with no recognisable shape (a random hex
string) passes it. That is why the capture also compares every record with
the exact key the provider was built with, which is the check that cannot
miss the one credential a model request could actually carry.
"""

from __future__ import annotations

import re
from typing import Iterable, Optional

#: (name, pattern). The name is what a withheld record says it looked like --
#: never the matched text, which is the thing being kept out.
CREDENTIAL_SHAPES: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("supabase key", re.compile(r"\bsb_(?:secret|publishable)_[A-Za-z0-9_-]{8,}")),
    ("supabase access token", re.compile(r"\bsbp_[A-Za-z0-9]{8,}")),
    ("github token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{8,}|github_pat_[A-Za-z0-9_]{8,})")),
    # ``sk-`` then up to two short prefix parts (``ant-api03-``, ``proj-``)
    # and a long unbroken run. Not ``sk-[A-Za-z0-9-]{20,}``: that is every
    # news URL about SK Hynix ("/sk-hynix-intel-may-make-memories-..."),
    # five of them in the journal's first month alone.
    ("api key", re.compile(r"\bsk-(?:[a-z0-9]{1,8}-){0,2}[A-Za-z0-9_]{20,}")),
    ("groq key", re.compile(r"\bgsk_[A-Za-z0-9]{20,}")),
    ("google key", re.compile(r"\bAIza[0-9A-Za-z_-]{30,}")),
    ("aws key id", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}")),
    ("alpaca key id", re.compile(r"\b[PA]K[A-Z0-9]{18}\b")),
    ("json web token", re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}")),
    ("bearer header", re.compile(r"\bBearer\s+[A-Za-z0-9_.~+/-]{12,}", re.IGNORECASE)),
    ("key header", re.compile(
        r"\b(?:authorization|apikey|api[-_]key|x-api-key)[\"']?\s*[:=]\s*[\"']?"
        r"(?:bearer\s+)?[A-Za-z0-9_.~+/-]{16,}",
        re.IGNORECASE,
    )),
)

#: A known value shorter than this is not compared: an empty or two-letter
#: "key" (a local endpoint that wants none) would match half of every prompt.
MIN_KNOWN_VALUE = 8


def credential_shape(text: str, known: Iterable[Optional[str]] = ()) -> Optional[str]:
    """The name of the first credential ``text`` seems to hold, or None.

    ``known`` are exact values that must not appear -- the key a request
    was actually authenticated with. They are compared, never returned or
    logged: the answer for one is "known credential", nothing more.
    """
    if not isinstance(text, str) or not text:
        return None
    for value in known:
        if isinstance(value, str) and len(value.strip()) >= MIN_KNOWN_VALUE and value.strip() in text:
            return "known credential"
    for name, pattern in CREDENTIAL_SHAPES:
        if pattern.search(text):
            return name
    return None


__all__ = ["CREDENTIAL_SHAPES", "MIN_KNOWN_VALUE", "credential_shape"]
