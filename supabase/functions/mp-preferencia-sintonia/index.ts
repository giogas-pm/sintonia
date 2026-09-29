// Sintonia — cria a preferência de pagamento (R$14,90) do relatório completo do casal no Mercado Pago e devolve o link do checkout.
// Mesma receita do Bodas: só o slug aleatório passa por aqui.
const REF = "diemqzngskmcuytkzjhr";
const WEBHOOK_URL = `https://${REF}.supabase.co/functions/v1/mp-webhook-sintonia`;
const SITE = "https://giogas-pm.github.io/sintonia/";
const PRECO = 14.9;
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
function json(obj: unknown) {
  return new Response(JSON.stringify(obj), { headers: { ...CORS, "Content-Type": "application/json" } });
}
Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  try {
    const token = Deno.env.get("MP_ACCESS_TOKEN");
    if (!token) return json({ ok: false, motivo: "sem_token" });
    const { slug } = await req.json().catch(() => ({} as any));
    if (!slug || !/^[a-z0-9]{10}$/.test(String(slug))) return json({ ok: false, motivo: "sem_slug" });
    const pref = {
      items: [{ title: "Sintonia: relatório completo do casal", quantity: 1, unit_price: PRECO, currency_id: "BRL" }],
      external_reference: String(slug),
      metadata: { slug: String(slug), produto: "sintonia" },
      statement_descriptor: "SINTONIA",
      notification_url: WEBHOOK_URL,
      back_urls: {
        success: `${SITE}?pago=ok#c=${slug}`,
        pending: `${SITE}?pago=pendente#c=${slug}`,
        failure: `${SITE}?pago=falhou#c=${slug}`,
      },
      auto_return: "approved",
    };
    const r = await fetch("https://api.mercadopago.com/checkout/preferences", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: "Bearer " + token },
      body: JSON.stringify(pref),
    });
    const j = await r.json();
    if (j && j.init_point) return json({ ok: true, init_point: j.init_point });
    return json({ ok: false, motivo: "mp_erro", detalhe: (j && (j.message || j.error)) || null });
  } catch (e) {
    return json({ ok: false, motivo: "excecao", detalhe: String(e) });
  }
});
