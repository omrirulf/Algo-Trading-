-- The model-io bucket takes xz instead of gzip, 26 Sep 2026 (later the same day).
--
-- The owner chose stronger compression in a format any computer opens: xz
-- (LZMA2) makes the model-call files about 60% smaller than gzip -- about
-- 85 MB a year of Storage instead of about 205 MB. `store/model_calls.py`
-- now writes `<run>.jsonl.xz` objects as `application/x-xz`, and the
-- bucket is told to accept exactly that. The size column is named for what
-- it holds whatever the format.
--
-- APPLIED to algo-trading-archive on 26 Sep 2026 (migration
-- "model_io_xz"), before the code that needs it was merged, while the
-- bucket and the table were still empty. Safe to run again.

update storage.buckets
   set allowed_mime_types = array['application/x-xz']
 where id = 'model-io';

do $$
begin
    if exists (select 1 from information_schema.columns
               where table_schema = 'public' and table_name = 'model_io_files'
                 and column_name = 'gz_bytes') then
        alter table public.model_io_files rename column gz_bytes to compressed_bytes;
    end if;
end $$;
