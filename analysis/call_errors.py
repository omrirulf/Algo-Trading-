"""Why a model call failed: our own setup, or the model.

The owner's decision of 24 Sep 2026 splits failed calls in two:

* **setup** -- the call never had a chance: a bad or missing key, an
  account the provider refuses, a model name it does not know. Our side,
  fixed by fixing the configuration. On 2026-09-24 every one of 58 calls
  got HTTP 401 because the key chain picked another provider's key.
* **model** -- the call was made properly and the model did not give a
  usable answer: a timeout, a server error, a rate limit, an empty or
  off-schema answer, an answer about another ticker.

Only model errors count toward trigger (c). Setup errors are logged and
shown, and both kinds count toward the same-day phone alert (more than 20%
of one run's calls failed).

The test is on the error text the cycle journals. Anything not recognised as
setup is a model error: when in doubt, the failure counts against the model,
never quietly for it.
"""

from __future__ import annotations

import re
from typing import Optional

SETUP = "setup"
MODEL = "model"

#: What the cycle writes when the model itself answered badly. These quote
#: the model's own text (or the provider's body), which may contain any word
#: at all -- "Unauthorized trading scandal..." -- so they are decided by
#: their prefix and never searched for setup words.
_MODEL_PREFIXES = ("invalid LLM output:", "model returned non-JSON", "answered for ", "model declined",
                   "response hit max_tokens")
#: A status from the provider, in the OpenAI-compatible client's wording
#: ("returned HTTP 401") or the Anthropic SDK's ("Error code: 401"). When
#: there is one it decides alone: the body after it is the provider's text.
_STATUS = re.compile(r"(?:\bHTTP\s*|Error code:\s*)(\d{3})\b")
#: Unauthorised, payment required, forbidden, not found (a model or endpoint
#: name the provider does not know): refused before any model ran.
_SETUP_STATUSES = frozenset({"401", "402", "403", "404"})
_SETUP_WORDS = re.compile(
    r"not authori[sz]ed|unauthori[sz]ed|authentication|permission denied|forbidden"
    r"|invalid[ _-]?api[ _-]?key|incorrect api key|no api key|api[ _-]?key (is )?(missing|not set|empty)"
    r"|missing (api )?key|key not configured|asked anonymously|credentials",
    re.IGNORECASE,
)
#: The SDKs' own class names for the same refusals.
_SETUP_CLASSES = re.compile(r"\b(AuthenticationError|PermissionDeniedError|NotFoundError)\b")


def failure_kind(error: Optional[str]) -> str:
    """``"setup"`` or ``"model"`` for a failed call's journalled error text."""
    text = (error or "").strip()
    if text.startswith(_MODEL_PREFIXES):
        return MODEL
    status = _STATUS.search(text)
    if status:
        return SETUP if status.group(1) in _SETUP_STATUSES else MODEL
    if _SETUP_WORDS.search(text) or _SETUP_CLASSES.search(text):
        return SETUP
    return MODEL


__all__ = ["MODEL", "SETUP", "failure_kind"]
