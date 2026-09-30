// Sintonia — métricas agregadas do funil pra rotina de monitoramento (GET ?k=<METRICS_KEY>).
const SB_URL = Deno.env.get("SUPABASE_URL")!;
const SVC = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const KEY = Deno.env.get("METRICS_KEY") || "";
const H = { apikey: SVC, Authorization: "Bearer " + SVC };
function json(obj: unknown, status = 200) {
  return new Response(JSON.stringify(obj), { status, headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" } });
}
async function countOf(q: string): Promise<number> {
  const r = await fetch(`${SB_URL}/rest/v1/${q}${q.includes("?") ? "&" : "?"}select=created_at`, { headers: { ...H, Prefer: "count=exact", Range: "0-0" } });
  return parseInt((r.headers.get("content-range") || "*/0").split("/")[1] || "0", 10);
}
Deno.serve(async (req) => {
  const url = new URL(req.url);
  if (KEY && url.searchParams.get("k") !== KEY) return json({ ok: false, motivo: "nao_autorizado" }, 401);
  try {
    const ev = ["visit", "engaged", "seo_land", "quiz_start", "quiz_criado", "convite_share", "b_open", "b_respondeu", "resultado_view", "stories_share", "paywall_view", "checkout_open", "relatorio_view"];
    const [casais, completos, pagos, ...n] = await Promise.all([countOf("quiz_casais"), countOf("quiz_casais?resp_b=not.is.null"), countOf("quiz_casais?unlocked=eq.true"), ...ev.map((e) => countOf(`quiz_eventos?evento=eq.${e}`))]);
    const funil: Record<string, number> = {};
    ev.forEach((e, i) => (funil[e] = n[i]));
    return json({ ok: true, as_of: new Date().toISOString(), receita_estimada: Math.round(pagos * 14.9 * 100) / 100, pedidos_pagos: pagos, casais, completos, funil });
  } catch (e) {
    return json({ ok: false, motivo: "excecao", detalhe: String(e) }, 200);
  }
});
