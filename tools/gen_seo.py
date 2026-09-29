# Gera as páginas de SEO do Sintonia em /sintonia/teste-de-casal/ + sitemap.xml + robots.txt
import json, os, html
ROOT = os.path.join(os.path.dirname(__file__), '..')
SITE = 'https://giogas-pm.github.io/sintonia/'
HUB = 'teste-de-casal'

P = {}
P[''] = dict(
 title='Teste de Casal Online Grátis: descubram a sintonia de vocês',
 h1='Teste de casal online: cada um responde no seu celular',
 desc='Teste de casal grátis: 20 perguntas sobre rotina, dinheiro, lazer, futuro e carinho. Cada um responde sem ver o outro e vocês descobrem a % de sintonia.',
 kw='teste de casal',
 intro='A maioria dos testes de casal da internet tem um defeito: uma pessoa só responde pelos dois. Aí não é teste, é chute. No Sintonia, <b>cada um responde no próprio celular</b>, sem ver as respostas do outro, e o resultado só aparece quando os dois terminaram.',
 body=[('Por que fazer um teste de casal', '<p>Não é pra decidir se o relacionamento dá certo (nenhum quiz faz isso). É pra rir, se conhecer melhor e descobrir assuntos que vocês nunca conversaram. As divergências são a melhor parte: é nelas que aparecem as conversas boas.</p>'),
  ('As 5 áreas do teste', '<ul><li><b>Rotina:</b> fim de semana, horário, bagunça, tarefas de casa.</li><li><b>Dinheiro:</b> guardar ou gastar, conta conjunta, compras grandes.</li><li><b>Lazer:</b> viagem, filme, festa, redes sociais.</li><li><b>Futuro:</b> filhos, onde morar, casamento, pet.</li><li><b>Carinho:</b> linguagem do amor, brigas, datas especiais, ciúme.</li></ul>'),
  ('Tipos de teste de casal', '<p>Neste guia você encontra variações pra cada momento: <a href="perguntas-para-casal/">perguntas para casal</a> (pra conversar), <a href="quiz-de-namorados/">quiz de namorados</a> (pra jogar), <a href="teste-de-compatibilidade-amorosa/">teste de compatibilidade amorosa</a> (pra ver a %) e <a href="quanto-voce-conhece-seu-namorado/">quanto você conhece seu namorado</a> (pra provocar).</p>')],
 faq=[('O teste de casal é grátis?', 'Sim. Responder, ver a % de sintonia e gerar a imagem pros Stories é grátis. O relatório completo, com as respostas lado a lado e a sintonia por área, é opcional (R$14,90, pagamento único).'),
  ('Meu par vê minhas respostas antes de responder?', 'Não. As respostas de cada um ficam escondidas até os dois terminarem. Só o relatório completo mostra as respostas lado a lado.'),
  ('Precisa de cadastro?', 'Não. Só o primeiro nome de cada um.')])
P['perguntas-para-casal'] = dict(
 title='Perguntas para Casal: 40 perguntas pra conversar (e um teste pros dois)',
 h1='40 perguntas para casal (pra conversar de verdade)',
 desc='Lista de perguntas para casal por tema: rotina, dinheiro, futuro, lazer e carinho. E um teste em que cada um responde no seu celular e vocês veem a % de sintonia.',
 kw='perguntas para casal',
 intro='Boas perguntas para casal não têm resposta certa: servem pra descobrir o que o outro pensa. Separamos 40 por tema. Dica: façam o <a href="../../">teste de sintonia</a> antes — as perguntas em que vocês divergirem são as melhores pra conversar.',
 body=[('Rotina', '<ol><li>Qual seria nosso domingo perfeito?</li><li>Que mania minha você acha fofa?</li><li>Qual tarefa de casa você faria pra sempre?</li><li>Qual você nunca mais quer fazer?</li><li>Você prefere acordar cedo ou dormir tarde?</li><li>O que te irrita em casa e você nunca falou?</li><li>Qual hábito nosso você quer manter pra sempre?</li><li>Qual hábito você quer mudar?</li></ol>'),
  ('Dinheiro', '<ol start="9"><li>Dinheiro pra você é segurança ou liberdade?</li><li>Como sua família lidava com dinheiro?</li><li>A partir de que valor a gente deveria combinar uma compra?</li><li>Conta conjunta: sim ou não?</li><li>Qual foi a compra mais impulsiva da sua vida?</li><li>Com o que vale a pena gastar sem culpa?</li><li>Qual nosso sonho mais caro?</li><li>Se ganhássemos na loteria, o que mudaria?</li></ol>'),
  ('Futuro', '<ol start="17"><li>Onde você se imagina morando daqui a 10 anos?</li><li>Filhos: quantos, quando, se?</li><li>Como seria um casamento perfeito pra você?</li><li>Que pet a gente teria?</li><li>Qual meta você quer que eu te ajude a bater?</li><li>O que você quer ter feito até os 40?</li><li>Moraria fora do Brasil?</li><li>Como imagina a gente velhinhos?</li></ol>'),
  ('Lazer', '<ol start="25"><li>Qual a viagem dos seus sonhos?</li><li>Qual filme você veria comigo mil vezes?</li><li>Festa ou sofá?</li><li>Qual programa você topa só porque eu gosto?</li><li>Qual foi nosso melhor rolê?</li><li>O que você posta e o que prefere guardar só pra gente?</li><li>Qual hobby você queria que a gente tivesse junto?</li><li>Que show a gente precisa ver?</li></ol>'),
  ('Carinho', '<ol start="33"><li>Quando você se sentiu mais amado(a) por mim?</li><li>Palavras, tempo, presentes ou toque: o que mais te toca?</li><li>Como você prefere fazer as pazes?</li><li>O que te deixa inseguro(a)?</li><li>Qual data você não quer que eu esqueça?</li><li>O que eu faço que te faz rir?</li><li>Qual foi o momento em que você soube que gostava de mim?</li><li>O que eu posso fazer mais por você?</li></ol>')],
 faq=[('Quantas perguntas fazer de uma vez?', 'Três a cinco por conversa rende mais que 40 de uma vez. Escolham um tema por noite.'),
  ('E se a gente discordar?', 'Ótimo. Divergência é assunto, não problema. O teste do Sintonia mostra exatamente onde vocês pensam diferente.')])
P['quiz-de-namorados'] = dict(
 title='Quiz de Namorados: jogo de perguntas pra fazer a dois (grátis)',
 h1='Quiz de namorados: o jogo em que ninguém pode colar',
 desc='Quiz de namorados online e grátis: cada um responde no seu celular, sem ver o outro. No fim, a % de sintonia do casal e uma imagem pra postar nos Stories.',
 kw='quiz de namorados',
 intro='Quiz de namorados bom é aquele em que ninguém consegue colar. Por isso, no Sintonia, <b>você responde, manda o link e seu par responde no celular dele(a)</b>. O placar só aparece no fim.',
 body=[('Como jogar', '<ol><li>Digite os dois nomes e responda as 20 perguntas sobre você.</li><li>Mande o link pro seu namorado ou namorada pelo WhatsApp.</li><li>Quando o outro terminar, os dois veem a % de sintonia.</li><li>Postem o resultado nos Stories e desafiem um casal amigo.</li></ol>'),
  ('Ideias pra deixar mais divertido', '<ul><li><b>Aposta:</b> quem errar mais a previsão da % paga o jantar.</li><li><b>Chute antes:</b> cada um chuta a % antes de ver o resultado.</li><li><b>Liga dos casais:</b> mandem pra casais amigos e comparem quem tem mais sintonia.</li><li><b>Revanche:</b> refaçam daqui a 6 meses e vejam o que mudou.</li></ul>'),
  ('Pra namoro à distância', '<p>Funciona igual: cada um está no seu celular de qualquer jeito. É um bom programa pra chamada de vídeo — respondam ao mesmo tempo e revelem o resultado juntos.</p>')],
 faq=[('Dá pra fazer com namoro recente?', 'Dá, e é até mais divertido: vocês descobrem coisas que ainda não sabiam.'),
  ('Funciona no celular?', 'Sim, foi feito pro celular. Não precisa instalar nada.')])
P['teste-de-compatibilidade-amorosa'] = dict(
 title='Teste de Compatibilidade Amorosa com % (os dois respondem)',
 h1='Teste de compatibilidade amorosa: a % real do casal',
 desc='Teste de compatibilidade amorosa em que os dois respondem de verdade, cada um no seu celular. Veja a % de compatibilidade e onde vocês combinam mais.',
 kw='teste de compatibilidade amorosa',
 intro='Calculadora do amor que mistura os nomes é brincadeira. Uma % de compatibilidade que faça sentido precisa das <b>respostas dos dois</b>. No Sintonia, a % é simplesmente quantas das 20 respostas vocês deram iguais.',
 body=[('Como a % é calculada', '<p>São 20 perguntas de múltipla escolha, 4 por área. Cada resposta igual conta 5 pontos. Sem fórmula mágica, sem signo: o resultado é o retrato de como vocês pensam hoje.</p>'),
  ('O que significa cada faixa', '<ul><li><b>80% ou mais — Almas gêmeas:</b> pensam parecido em quase tudo.</li><li><b>65–79% — Muita sintonia:</b> combinam no que importa.</li><li><b>50–64% — Opostos que se completam:</b> metade igual, metade diferente.</li><li><b>35–49% — Aprendendo juntos:</b> muitas visões diferentes.</li><li><b>Menos de 35% — Caos apaixonado:</b> quase tudo diferente, e mesmo assim juntos.</li></ul><p>Nenhuma faixa é ruim. Casais com visões diferentes podem ser ótimos — desde que conversem sobre elas.</p>'),
  ('Compatibilidade por área', '<p>O relatório completo mostra a % em cada área (rotina, dinheiro, lazer, futuro, carinho). É comum um casal ter 90% em lazer e 40% em dinheiro — e saber disso ajuda a evitar briga.</p>')],
 faq=[('Compatibilidade baixa quer dizer que não vai dar certo?', 'Não. O teste mede semelhança de respostas, não a qualidade do relacionamento. É ponto de partida pra conversa, não diagnóstico.'),
  ('Tem a ver com signo?', 'Não. É feito só com as respostas de vocês dois.')])
P['quanto-voce-conhece-seu-namorado'] = dict(
 title='Quanto Você Conhece Seu Namorado? Teste pra fazer juntos',
 h1='Quanto você conhece seu namorado (ou namorada)?',
 desc='Teste pra descobrir quanto vocês se conhecem: cada um responde no seu celular e vocês comparam as respostas. Grátis, 3 minutos, resultado em %.',
 kw='quanto você conhece seu namorado',
 intro='Você acha que sabe o que seu namorado faria com R$1.000 sobrando? Ou como ele(a) prefere fazer as pazes depois de uma briga? Façam o teste: <b>cada um responde sobre si</b> e vocês descobrem o quanto pensam parecido.',
 body=[('Chute antes de ver', '<p>A graça: antes de abrir o resultado, cada um chuta quantas respostas vão bater. Quem chegar mais perto ganha. Com o relatório completo, dá pra ver pergunta por pergunta quem pensou o quê.</p>'),
  ('Perguntas que mais surpreendem os casais', '<ul><li>O que fazer com dinheiro que sobra no mês.</li><li>Como o outro se sente amado (palavras, tempo, presentes ou toque).</li><li>Onde morar daqui a 10 anos.</li><li>Ciúme: quanto é normal pra cada um.</li></ul>'),
  ('Para namorada e namorado', '<p>Serve pros dois lados e pra qualquer casal. Mande o link pelo WhatsApp e esperem o resultado juntos.</p>')],
 faq=[('Posso fazer sozinho(a)?', 'Não dá: o teste compara as respostas dos dois. Você responde e manda o link pro seu par.'),
  ('Quanto tempo leva?', 'Uns 3 minutos pra cada um.')])

CSS = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read().split('<style>')[1].split('</style>')[0]

def page(slug, d):
    depth = 1 if slug == '' else 2
    base = '../' * depth
    url = SITE + HUB + '/' + (slug + '/' if slug else '')
    crumbs = [('Sintonia', SITE), ('Teste de casal', SITE + HUB + '/')] + ([(d['h1'], url)] if slug else [])
    ld = [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d['faq']]}]
    others = ''.join(f'<li><a href="{base}{HUB}/{s + "/" if s else ""}">{html.escape(P[s]["kw"].capitalize())}</a></li>' for s in P if s != slug)
    cta = f'<a class="btn" href="{base}?src=seo&amp;p={slug or HUB}">Fazer o teste com meu par — grátis</a>'
    body = ''.join(f'<h2>{h}</h2>{c}' for h, c in d['body'])
    faq = ''.join(f'<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>' for q, a in d['faq'])
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(d['title'])}</title><meta name="description" content="{html.escape(d['desc'])}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(d['title'])}"><meta property="og:description" content="{html.escape(d['desc'])}"><meta property="og:image" content="{SITE}og.png"><meta property="og:type" content="article">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script><style>{CSS}</style></head><body><div class="wrap">
<a class="logo" href="{base}">♥ Sintonia</a> <span class="mut">› <a href="{base}{HUB}/" style="color:inherit">Teste de casal</a></span>
<h1>{d['h1']}</h1><p>{d['intro']}</p><div class="card center">{cta}<p class="mut" style="margin:.5em 0 0">20 perguntas · 3 minutos · cada um no seu celular</p></div>
{body}<div class="card center"><h2 style="margin-top:0">Bora descobrir a sintonia de vocês?</h2>{cta}</div>
<h2>Perguntas frequentes</h2>{faq}<h2>Veja também</h2><ul>{others}</ul>
<footer><p>Sintonia é um teste para diversão e conversa, não um diagnóstico.</p></footer></div></body></html>'''

urls = [SITE]
for s, d in P.items():
    out = os.path.join(ROOT, HUB, s) if s else os.path.join(ROOT, HUB)
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(page(s, d))
    urls.append(SITE + HUB + '/' + (s + '/' if s else ''))
open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{u}</loc></url>' for u in urls) + '</urlset>\n')
open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
print(len(urls), 'urls')
