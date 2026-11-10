# One more ask after a Bright Data server error (5xx): the plan

**Status: planned.** The owner's decision of 10 Nov 2026 ("yes to both", item 5a) to the proposal of 4 Nov
2026: retry a failed news request once when Bright Data answers a server error. An operational change to the
news fetch, logged in the pre-registration's Amendments table as planned; the code changes only after the owner
says "build". The owner is working on Bright Data's search results in another session: this plan touches only
what happens to a 5xx status, never the request itself (the zone, the exit country, the search URL, the parser,
the headline limit and the Bing fallback are left exactly as they are).

## 1. What happens today

`orchestrator/news.py`, `_fetch_items`: one POST to Bright Data per name. The request is sent again once only
when the socket fails (`httpx.TransportError`, after `RETRY_PAUSE_SECONDS`, 2 seconds). A 200 whose body the
parser refuses is asked once more after `EMPTY_RETRY_PAUSE_SECONDS` (10 seconds; the owner's decision of 16 Oct).
Any other status -- a 500, 502, 503 or 504 from Bright Data itself -- raises `NewsFetchError` at once, and since
4 Nov the cycle then asks Bing's feed for the name; with no headline naming it there, the name is judged
without news (a "news unavailable" gap, counted by the health check).

The record: on 15 Oct two names met HTTP 500 from the vendor's proxy; on 3 Nov the whole cycle did (80 of 80
names without news, six entries made on a day with no news: ASML, EWY and CAT among them, stopped out on 5 Nov
at 8-9% losses). A server error is the one answer the fetch never asks again about.

## 2. The change

- In `_fetch_items`, a status in the 500 family is treated like a refused 200: the same request once more
  after `EMPTY_RETRY_PAUSE_SECONDS` (10 seconds), with Bright Data's own headers (`x-brd-status-code`,
  `x-brd-error`) in the warning, then the Bing fallback as today if the second answer is bad too.
- A 4xx is not asked again: the request itself is wrong, and asking again only spends the day's time.
- Bright Data's own "try again later, after a minimum of 15 seconds" (an `x-brd-status-code 429` first seen on
  10 Nov, on XLY's retry) is read when present: the pause before the second ask is at least that many seconds
  (capped at 60), so the retry is not thrown away under the vendor's own minimum. The 10-second pause stays
  the default.
- One retry, not more: the context stage is sequential over 80 names, and a dead vendor must not turn 17
  minutes into an hour.

## 3. What it costs and what it risks

- At most one more request per failed name (about $0.001 each at the zone's price), and 10 to 15 seconds of
  the context stage per failed name. On a day the vendor is down for good, the stage grows by about 15 to 20
  minutes (80 names); the context stage has taken 13 to 38 minutes this month and the job cap is 180 minutes,
  so the cycle keeps its margin. The model stage is unaffected.
- Nothing changes for the race, the funds or the calibration copy: the journal line records the same gap or
  the same headlines, only more often the headlines.

## 4. Tests and record

- `tests/test_news.py`: a 503 is asked once more after the pause and then parsed; a second 503 raises with
  Bright Data's headers in the message and the Bing fallback is asked; a 404 is not asked again; the vendor's
  minimum wait is honoured; the existing refused-200 and transport-error tests unchanged.
- The daily check already reports every POST by status and the retries that failed again; the weekly report's
  "production news fetches that failed" line counts the names, not the requests, so it is unchanged.
- The Amendments row below is marked planned; when the change is merged the row gets its effective date.

## 5. The Amendments row (planned)

| 2026-11-10 | **News fetch: one more ask after a Bright Data server error** (planned; the owner's "yes" of
2026-11-10, item 5a; operational; no rule of the race changes; the search URL, the zone, the exit country, the
parser, the headline limit and the Bing fallback are unchanged) | A 5xx from Bright Data was the one answer the
news fetch never asked again about: two names on 2026-10-15, the whole list on 2026-11-03 (80 of 80 names
judged without news, six entries made that day). The plan (`docs/research/news-server-error-retry-plan.md`): in
`orchestrator/news.py` a 500-family status is asked once more after the same 10-second pause as a refused 200
(longer when Bright Data's own headers name a minimum wait, up to 60 s), then the Bing fallback as today; a 4xx
is not asked again. At most one request and 10-15 seconds more per failed name. Built only after the owner
says "build". |
