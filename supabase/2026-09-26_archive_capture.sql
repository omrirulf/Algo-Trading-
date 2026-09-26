-- The archive's capture migration, 26 Sep 2026.
--
-- Run once, by hand, in the SQL editor of the Supabase project
-- "algo-trading-archive" (as the postgres role), BEFORE the code that
-- pushes to the new tables is merged. Nothing in this repository applies it.
--
-- APPLIED to algo-trading-archive on 26 Sep 2026 (migration
-- "archive_capture"), before this code was merged. Both tables were still
-- empty then, so the two `vacuum full` lines below were not needed.
-- Safe to run again: every statement is idempotent. It brings a project
-- made from the earlier store/remote_schema.sql to the current one.
--
-- WHAT IT DOES
--
-- 1. The size fix. `signals` (and `executions`) stored every line twice:
--    `raw` as text and a generated `raw_json` jsonb copy of it -- about
--    185 MB a year of the free plan's 500 MB. The copy is dropped and
--    replaced by views that parse `raw` on read, `signals_json` and
--    `executions_json` (security_invoker, like every view here). Queries
--    that read `raw_json` from `signals` read it from `signals_json` now.
--    The `decisions` view is dropped and made again around the change, as
--    it was, with security_invoker. If something else of yours depends on
--    `raw_json` (a view you made by hand), the `drop column` below fails and
--    the whole transaction rolls back, changing nothing: drop or change that
--    first. Nothing is cascaded away silently.
--
-- 2. Six new tables, row-level security on and no policy (the publishable
--    key can do nothing; the secret key the push uses bypasses RLS):
--    account_snapshots, account_fills, model_calls, model_io_files,
--    scoring_prices, scoring_runs. What each holds is in
--    store/remote_schema.sql and docs/database.mdx.
--
-- 3. The private Storage bucket `model-io`, for the model calls' full
--    request and response bodies (gzip JSON lines, one object per run).
--
-- AFTER IT
--
-- Dropping a column does not give its space back by itself: the old rows
-- still carry it until they are rewritten. Run these two lines ON THEIR OWN
-- afterwards (VACUUM cannot run inside a transaction, and the SQL editor
-- runs a pasted script as one). They lock each table for a moment, which
-- only a push running at that very moment would notice -- and a push that
-- fails is retried by the next one.
--
--     vacuum full public.signals;
--     vacuum full public.executions;
--
-- Then check the push works with the new secret key on Storage too -- the
-- one thing not measured before this was written (docs/database.mdx, "The
-- model-io bucket"): run archive-push.yml once, or wait for the next
-- heartbeat, and look for "model-io/...: stored" in its log and "ok": true
-- in logs/archive_status.json.

begin;

-- 1. The size fix -------------------------------------------------------------

drop view if exists public.decisions;
alter table public.signals drop column if exists raw_json;
alter table public.executions drop column if exists raw_json;

create or replace view public.signals_json as
select s.*, s.raw::jsonb as raw_json from public.signals s;

create or replace view public.executions_json as
select e.*, e.raw::jsonb as raw_json from public.executions e;

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

-- A view runs as its creator unless told otherwise, and would read straight
-- through the RLS on the tables under it (store/remote_schema.sql says how
-- that was found). Every view here enforces the caller's permissions.
alter view public.decisions set (security_invoker = on);
alter view public.signals_json set (security_invoker = on);
alter view public.executions_json set (security_invoker = on);

-- 2. The new tables -----------------------------------------------------------

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
    gz_bytes     bigint,
    sha256       text not null
);

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

alter table public.account_snapshots enable row level security;
alter table public.account_fills enable row level security;
alter table public.model_calls enable row level security;
alter table public.model_io_files enable row level security;
alter table public.scoring_prices enable row level security;
alter table public.scoring_runs enable row level security;

-- 3. The private bucket -------------------------------------------------------

insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('model-io', 'model-io', false, 52428800, array['application/gzip'])
on conflict (id) do update
    set public = false,
        file_size_limit = excluded.file_size_limit,
        allowed_mime_types = excluded.allowed_mime_types;

commit;
