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

#: HTTP statuses that mean the provider refused who we are or what we asked
#: for, before any model ran: unauthorised, payment required, forbidden, not
#: found (a model or endpoint name it does not know).
_SETUP_STATUS = re.compile(r"\bHTTP\s*(401|402|403|404)\b", re.IGNORECASE)
_SETUP_WORDS = re.compile(
    r"not authori[sz]ed|unauthori[sz]ed|authentication|permission denied|forbidden"
    r"|invalid[ _-]?api[ _-]?key|incorrect api key|no api key|api key (is )?(missing|not set)"
    r"|missing (api )?key|key not configured|not configured|credentials",
    re.IGNORECASE,
)
#: The SDKs' own class names for the same refusals.
_SETUP_CLASSES = re.compile(r"\b(AuthenticationError|PermissionDeniedError|NotFoundError)\b")


def failure_kind(error: Optional[str]) -> str:
    """``"setup"`` or ``"model"`` for a failed call's journalled error text."""
    text = error or ""
    if _SETUP_STATUS.search(text) or _SETUP_WORDS.search(text) or _SETUP_CLASSES.search(text):
        return SETUP
    return MODEL


__all__ = ["MODEL", "SETUP", "failure_kind"]
