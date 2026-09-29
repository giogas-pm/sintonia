-- Sintonia (quiz de compatibilidade do casal). Guarda só primeiro nome + 20 respostas de múltipla escolha. Nada sensível.
-- Anon NUNCA lê a tabela: tudo passa por RPC security definer. As respostas de A nunca saem antes de B responder,
-- e as respostas individuais (relatório completo) só saem depois do pagamento (unlocked, gravado pelo webhook).
create table if not exists public.quiz_casais (
  slug text primary key,
  nome_a text not null,
  nome_b text not null,
  resp_a smallint[] not null,
  resp_b smallint[],
  unlocked boolean not null default false,
  valor numeric,
  payment_id text,
  created_at timestamptz not null default now(),
  respondido_b_at timestamptz
);
create table if not exists public.quiz_eventos (
  id uuid primary key default gen_random_uuid(),
  evento text not null, slug text, meta jsonb,
  created_at timestamptz not null default now()
);
alter table public.quiz_casais enable row level security;
alter table public.quiz_eventos enable row level security;
revoke all on public.quiz_casais from anon, authenticated;
revoke select, update, delete on public.quiz_eventos from anon, authenticated;
drop policy if exists quiz_eventos_ins on public.quiz_eventos;
create policy quiz_eventos_ins on public.quiz_eventos for insert to anon
  with check (char_length(evento) <= 40 and (slug is null or char_length(slug) <= 24) and (meta is null or pg_column_size(meta) < 400));

create or replace function public.quiz_valida(p smallint[]) returns boolean
language sql immutable as $$
  select p is not null and array_length(p, 1) = 20 and array_ndims(p) = 1
     and not exists (select 1 from unnest(p) x where x is null or x < 0 or x > 3)
$$;

create or replace function public.quiz_criar(p_slug text, p_nome_a text, p_nome_b text, p_resp smallint[]) returns boolean
language plpgsql security definer set search_path = public as $$
begin
  if p_slug !~ '^[a-z0-9]{10}$' then return false; end if;
  if char_length(trim(coalesce(p_nome_a,''))) not between 1 and 30 or char_length(trim(coalesce(p_nome_b,''))) not between 1 and 30 then return false; end if;
  if not quiz_valida(p_resp) then return false; end if;
  insert into quiz_casais(slug, nome_a, nome_b, resp_a) values (p_slug, trim(p_nome_a), trim(p_nome_b), p_resp);
  return true;
exception when unique_violation then return false;
end $$;

-- B responde uma única vez.
create or replace function public.quiz_responder(p_slug text, p_resp smallint[]) returns boolean
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  if not quiz_valida(p_resp) then return false; end if;
  update quiz_casais set resp_b = p_resp, respondido_b_at = now() where slug = p_slug and resp_b is null;
  get diagnostics n = row_count;
  return n = 1;
end $$;

create or replace function public.quiz_get(p_slug text) returns json
language plpgsql stable security definer set search_path = public as $$
declare c quiz_casais; acertos int; areas int[];
begin
  select * into c from quiz_casais where slug = p_slug;
  if not found then return null; end if;
  if c.resp_b is not null then
    select count(*) into acertos from generate_subscripts(c.resp_a, 1) i where c.resp_a[i] = c.resp_b[i];
    select array_agg(n order by k) into areas from (
      select k, (count(*) filter (where c.resp_a[i] = c.resp_b[i]))::int * 25 as n
      from generate_series(0, 4) k, generate_series(k*4+1, k*4+4) i group by k) t;
  end if;
  return json_build_object(
    'nome_a', c.nome_a, 'nome_b', c.nome_b,
    'respondido', c.resp_b is not null,
    'acertos', acertos,
    'areas', areas, -- % por área (grátis: o app mostra só a mais forte; o resto fica no relatório pago)
    'unlocked', c.unlocked,
    'resp_a', case when c.unlocked and c.resp_b is not null then c.resp_a end,
    'resp_b', case when c.unlocked and c.resp_b is not null then c.resp_b end
  );
end $$;

revoke all on function public.quiz_criar(text, text, text, smallint[]) from public;
revoke all on function public.quiz_responder(text, smallint[]) from public;
revoke all on function public.quiz_get(text) from public;
grant execute on function public.quiz_criar(text, text, text, smallint[]) to anon, authenticated;
grant execute on function public.quiz_responder(text, smallint[]) to anon, authenticated;
grant execute on function public.quiz_get(text) to anon, authenticated;
