-- Postgres / Supabase schema for the remote archive.
--
-- Paste this into the Supabase SQL editor once, or let
-- `python store/push_remote.py --print-schema` hand it to you. This file is
-- the whole schema as it stands, for a new project. A project made from an
-- earlier version of it is brought up to this one by the migration
-- supabase/2026-09-26_archive_capture.sql, not by running this again.
--
-- The rule for what is kept (the owner's, 26 Sep 2026): store what cannot
-- be got back later, and what a result would need to be checked again. The
-- git journal stays the official record; this is a backup and a place to
-- search. Nothing in the race, the funds or the pre-registration reads it.
--
-- `signals` and `executions` are the same shape as store/schema.py, with
-- three deliberate differences.
--
-- 1. `line_hash` is the primary key rather than a surrogate id. The content
--    hash is the natural key, and making it the PK is what makes the push
--    idempotent: `on conflict do nothing` absorbs a re-send of lines the
--    remote already has, so a push that overlaps the previous one is free.
--
-- 2. `raw` stays `text`, byte-exact, exactly as in SQLite, and is stored
--    once. Storing only jsonb would silently reformat the line (key order,
--    whitespace, number rendering), and the archive's whole claim is that it
--    kept what was written. The parsed form is a view that parses `raw` on
--    read (`signals_json`, `executions_json`):
--
--        select raw_json -> 'context' -> 'technicals' ->> 'rsi14' from signals_json;
--
--    Until 26 Sep 2026 it was a stored generated column beside `raw` -- a
--    second full copy of every line, about 185 MB a year of a 500 MB plan.
--
-- 3. `ts_exact` is smallint rather than boolean, so one row builder in
--    store/loader.py serves both backends with no per-backend coercion.
--    Postgres will not implicitly cast 0/1 to boolean, and a translation layer
--    that exists only to satisfy a type is a place for the two archives to
--    drift apart.

create table if not exists public.signals (
    line_hash          text primary key,
    ingested_at        timestamptz not null,

    ts_utc             timestamptz,
    ts_exact           smallint not null default 0,
    trade_date         date,

    ticker             text not null,
    bias               text,
    conviction         double precision,
    rationale          text,

    news_score         double precision,
    technical_score    double precision,
    fundamental_score  double precision,
    analyst_score      double precision,
    insider_score      double precision,

    outcome_status     text,
    outcome_reason     text,
    outcome_quantity   integer,
    order_id           text,
    error              text,

    gap_count          integer not null default 0,

    model              text,
    input_tokens       bigint,
    output_tokens      bigint,
    cost_usd           double precision,

    fx_rate            double precision,

    raw                text not null
);

-- Both kinds of audit line: the engine's verdict on a signal, and since
-- 26 Sep 2026 the position manager's actions (`position_managed`: the
-- ladder, the stops), with `status` the action and `stop_price` the stop it
-- left (store/loader.py:execution_row).
create table if not exists public.executions (
    line_hash    text primary key,
    ingested_at  timestamptz not null,

    ts_utc       timestamptz,
    ts_exact     smallint not null default 0,
    trade_date   date,

    ticker       text not null,
    status       text,
    reason       text,
    bias         text,
    conviction   double precision,

    quantity     integer,
    side         text,
    entry_price  double precision,
    stop_price   double precision,
    atr          double precision,
    order_id     text,

    level        text,
    raw          text not null
);

create index if not exists signals_ticker_ts on public.signals (ticker, ts_utc);
create index if not exists signals_ts on public.signals (ts_utc desc);
create index if not exists signals_date on public.signals (trade_date);
create index if not exists signals_order on public.signals (order_id);
create index if not exists executions_ticker_ts on public.executions (ticker, ts_utc);
create index if not exists executions_order on public.executions (order_id);

-- The parsed form of each line, computed when it is read rather than stored.
create or replace view public.signals_json as
select s.*, s.raw::jsonb as raw_json from public.signals s;

create or replace view public.executions_json as
select e.*, e.raw::jsonb as raw_json from public.executions e;

-- The same join the local index exposes: a signal beside the order it became.
-- LEFT JOIN because most signals never become orders, and a rejection is data.
create or replace view public.decisions as
select
    s.ts_utc, s.trade_date, s.ticker, s.bias, s.conviction,
    s.news_score, s.technical_score, s.fundamental_score,
    s.analyst_score, s.insider_score,
    s.outcome_status, s.outcome_reason, s.gap_count, s.cost_usd, s.fx_rate,
    e.quantity, e.side, e.entry_price, e.stop_price, e.atr, e.order_id
from public.signals s
left join public.executions e
       on e.order_id = s.order_id and s.order_id is not null;

-- NOT optional, and not a detail. A Postgres view runs with the permissions of
-- whoever CREATED it unless told otherwise, so without this line `decisions`
-- reads straight through the row-level security below it: the signals table is
-- closed to the publishable key and a view over it is wide open.
--
-- That is not hypothetical. The first version of this file omitted it, and a
-- probe with the anon role read 0 rows from `signals` and 1 row from
-- `decisions` -- the security lint caught it before the schema carried any
-- real data. security_invoker makes the view enforce the permissions of
-- whoever queries it, which is the whole point of the RLS below. Every view
-- in this file gets the same line.
alter view public.decisions set (security_invoker = on);
alter view public.signals_json set (security_invoker = on);
alter view public.executions_json set (security_invoker = on);

-- --------------------------------------------------------------------------
-- The paper account (logs/account.jsonl): one row per snapshot the heartbeat
-- took after a run, and one per fill those snapshots read, keyed on the
-- broker's fill id (two overlapping snapshots read the same fill).
-- --------------------------------------------------------------------------

create table if not exists public.account_snapshots (
    line_hash           text primary key,
    ingested_at         timestamptz not null,
    ts_utc              timestamptz not null,
    trade_date          date,
    mode                text,
    sha                 text,
    equity              double precision,
    cash                double precision,
    long_market_value   double precision,
    short_market_value  double precision,
    last_equity         double precision,
    positions           integer,
    stops               integer,
    fills               integer,
    errors              integer,
    raw                 text not null
);

create table if not exists public.account_fills (
    fill_id        text primary key,
    ingested_at    timestamptz not null,
    ts_utc         timestamptz,
    order_id       text,
    ticker         text,
    side           text,
    qty            double precision,
    price          double precision,
    snapshot_hash  text
);

create index if not exists account_snapshots_ts on public.account_snapshots (ts_utc desc);
create index if not exists account_fills_ticker_ts on public.account_fills (ticker, ts_utc);
create index if not exists account_fills_order on public.account_fills (order_id);

-- --------------------------------------------------------------------------
-- Every model call a cycle made (orchestrator/model_io.py): one row per HTTP
-- ask -- retries, timeouts, refusals and off-schema answers included --
-- with the parameters, the token counts and the SHA-256 of the request body
-- sent and the response body received. The bodies themselves (every
-- message, the reasoning text) are xz JSON lines in the private Storage
-- bucket `model-io`, at `object_path`; `model_io_files` names each object.
-- The journal line of the ticker carries the same call id and hashes, so a
-- copy of a body is checkable from git alone. Never a header, never a key:
-- a record that looked like it held one is `withheld` (bodies dropped,
-- hashes kept).
-- --------------------------------------------------------------------------

create table if not exists public.model_calls (
    call_id           text primary key,
    ingested_at       timestamptz not null,
    ts_utc            timestamptz,
    trade_date        date,
    run_id            text,
    ticker            text,
    provider          text,
    host              text,
    model             text,
    attempt           integer,
    kind              text,
    outcome           text,
    http_status       integer,
    error             text,
    latency_ms        integer,
    batch_id          text,
    custom_id         text,
    params            jsonb,
    input_tokens      integer,
    output_tokens     integer,
    reasoning_tokens  integer,
    prompt_sha256     text,
    answer_sha256     text,
    request_chars     integer,
    response_chars    integer,
    withheld          text,
    object_path       text
);

create index if not exists model_calls_ticker_ts on public.model_calls (ticker, ts_utc);
create index if not exists model_calls_ts on public.model_calls (ts_utc desc);

create table if not exists public.model_io_files (
    object_path  text primary key,
    ingested_at  timestamptz not null,
    day          date,
    run_id       text,
    calls        integer,
    withheld     integer,
    unreadable   integer,
    raw_bytes    bigint,
    compressed_bytes  bigint,
    sha256       text not null
);

-- --------------------------------------------------------------------------
-- The daily prices the race and the funds scored with (analysis/price_tape.py,
-- store/scoring_prices.py). Each distinct bar once, keyed on what it says;
-- a bar the vendor revised is a second row. One row per scoring run, with
-- the SHA-256 its committed output carries (prices_sha256) and, per source
-- and ticker, the dates and bar count it covered -- enough to rebuild that
-- night's table and check it against the hash in git.
-- --------------------------------------------------------------------------

create table if not exists public.scoring_prices (
    price_key         text primary key,
    ingested_at       timestamptz not null,
    kind              text not null,
    ticker            text not null,
    bar_date          date not null,
    open              double precision,
    high              double precision,
    low               double precision,
    close             double precision,
    adj_close         double precision,
    dividends         double precision,
    source            text not null,
    first_consumer    text,
    first_run_id      text,
    first_fetched_at  timestamptz
);

create index if not exists scoring_prices_ticker_date on public.scoring_prices (ticker, bar_date);

create table if not exists public.scoring_runs (
    run_key        text primary key,
    ingested_at    timestamptz not null,
    consumer       text not null,
    run_id         text,
    generated_at   timestamptz,
    final_through  date,
    prices_sha256  text not null,
    rows           integer,
    coverage       jsonb
);

-- Row-level security on, and deliberately NO policies.
--
-- That combination denies every request carrying the publishable (anon) key,
-- which is the key that is safe to leak precisely because it should be able to
-- do nothing here. The push uses a secret key (sb_secret_..., named
-- github-archive), which acts as the service_role Postgres role, bypasses RLS,
-- and lives only in a GitHub Actions secret. (Not the legacy JWT service_role
-- key: Supabase switches legacy keys off at the end of 2026.)
--
-- The alternative -- an insert-only policy for anon -- would let anyone who
-- read the publishable key append rows to the record of what this system
-- decided. A journal that strangers can write to is not a journal.
alter table public.signals enable row level security;
alter table public.executions enable row level security;
alter table public.account_snapshots enable row level security;
alter table public.account_fills enable row level security;
alter table public.model_calls enable row level security;
alter table public.model_io_files enable row level security;
alter table public.scoring_prices enable row level security;
alter table public.scoring_runs enable row level security;

-- The private Storage bucket for the model calls' bodies. Private: no public
-- URL, and storage.objects keeps RLS on with no policy for it, so only the
-- secret key's role can read or write an object. Objects are xz, one per
-- heartbeat run (`YYYY/MM/YYYY-MM-DD/<run id>-<HHMMSS>.jsonl.xz`), never
-- overwritten. 50 MB is the free plan's ceiling per object; a day's file is
-- well under 1 MB.
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('model-io', 'model-io', false, 52428800, array['application/x-xz'])
on conflict (id) do update
    set public = false,
        file_size_limit = excluded.file_size_limit,
        allowed_mime_types = excluded.allowed_mime_types;
