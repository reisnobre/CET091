select relname as "table_name", pg_size_pretty(pg_table_size(C.oid)) as "table_size" from pg_class C left join pg_namespace N on (N.oid = C.relnamespace)
where nspname not in ('pg_catalog', 'information_schema')
and nspname !~ '^pg_toast' and relkind in ('r')
order by pg_table_size(C.oid)
desc limit 1;
