#!/usr/bin/env python3
"""Gera o site estático da Korberg & Müller.

Uso:
  python3 build.py prod   <pasta-de-saida>   # links limpos (/servicos/x/), para a Cloudflare
  python3 build.py preview <pasta-de-saida>  # links para .../index.html, para a prévia
"""
import sys, os, json, shutil, datetime
from urllib.parse import quote
from content import SERVICES, GROUPS, ICONS
from illos import SERVICE_ILLOS, HOME_WIDE
from articles import ARTICLES

MODE, OUT = sys.argv[1], sys.argv[2]
SRC = os.path.dirname(os.path.abspath(__file__))
BASE = "https://site---k-m.pages.dev/"   # endereço oficial: troque aqui ao ter domínio próprio
TODAY = datetime.date.today().isoformat()
WA_NUMBER = "5551998107741"
WA_DISPLAY = "(51) 99810-7741"
LEGAL = "NBNG COMERCIO E SERVICOS LTDA - ME, CNPJ 24.206.394/0001-05"
BY_SLUG = {s["slug"]: s for s in SERVICES}

# ---------- caminhos ----------
ABS = False   # páginas servidas em qualquer endereço (404) usam caminhos absolutos
def pref(depth): return "/" if ABS else "../" * depth
def page_href(path, depth):
    """path: '' (home), 'servicos/', 'servicos/x/'."""
    if ABS: return "/" + path
    p = pref(depth) + path
    if MODE == "preview":
        return p + "index.html"
    return p if p else "./"
def home_anchor(anchor, depth):
    if ABS: return "/#" + anchor
    if depth == 0: return "#" + anchor
    return page_href("", depth) + "#" + anchor
def url(path): return BASE + path

def wa_link(subject=None):
    msg = "Olá! Vim pelo site da Korberg & Müller e gostaria de conversar sobre " + (subject.lower() if subject else "um projeto") + "."
    return "https://wa.me/%s?text=%s" % (WA_NUMBER, quote(msg, safe=""))

def esc(s): return s.replace('"', "&quot;")
def strip_amp(s): return s.replace("&amp;", "&")

# ---------- partes comuns ----------
BRAND_SVG = '''<svg class="brand-mark" viewBox="0 0 36 36" aria-hidden="true">
        <rect x=".75" y=".75" width="34.5" height="34.5" fill="none" stroke="#fff" stroke-opacity=".55" stroke-width="1.5"/>
        <path d="M7 11.5v13M7 19l8.5-7.5M10.5 16.5l5.5 8" stroke="#fff" stroke-width="1.8" fill="none" stroke-linejoin="miter"/>
        <path d="M19 24.5v-13l5 8 5-8v13" stroke="#8DB3FF" stroke-width="1.8" fill="none" stroke-linejoin="miter"/>
      </svg>'''
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
WA_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5l1.3-3.7A8 8 0 1 1 8.4 18.8z"/><path d="M9 10.5h.01M12 10.5h.01M15 10.5h.01"/></svg>'

def head(depth, title, desc, path, jsonld, extra_robots=None):
    p = pref(depth)
    ld = "\n".join('<script type="application/ld+json">\n%s\n</script>' % json.dumps(j, ensure_ascii=False, indent=2) for j in jsonld)
    t_plain = strip_amp(title)
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{extra_robots or 'index, follow, max-image-preview:large'}">
<link rel="canonical" href="{url(path)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Korberg &amp; Müller Consulting">
<meta property="og:url" content="{url(path)}">
<meta property="og:title" content="{esc(t_plain)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{url('og-image.png')}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Korberg &amp; Müller Consulting: Inteligência artificial, resultado real.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(t_plain)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{url('og-image.png')}">
<meta name="theme-color" content="#0A2342">
<link rel="icon" href="{p}favicon.ico" sizes="48x48">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
{ld}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&amp;family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&amp;display=swap" rel="stylesheet">
<script src="{p}assets/js-flag.js"></script>
<link rel="stylesheet" href="{p}assets/site.css">
</head>
<body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
'''

def header(depth, current=None):
    def cur(k): return ' aria-current="page"' if current == k else ""
    return f'''
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{page_href('', depth)}" aria-label="Korberg &amp; Müller Consulting, página inicial">
      {BRAND_SVG}
      <span class="brand-name">Korberg &amp; Müller<small>CONSULTING</small></span>
    </a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu" aria-label="Abrir menu">
      <svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><path d="M2 5h16M2 10h16M2 15h16" stroke="currentColor" stroke-width="1.8"/></svg>
    </button>
    <nav class="nav" id="menu" aria-label="Principal">
      <a href="{page_href('servicos/', depth)}"{cur('servicos')}>Serviços</a>
      <a href="{page_href('insights/', depth)}"{cur('insights')}>Insights</a>
      <a href="{home_anchor('abordagem', depth)}">Abordagem</a>
      <a href="{home_anchor('metodo', depth)}">Método</a>
      <a href="{home_anchor('lideranca', depth)}">Liderança</a>
      <a class="nav-cta" href="{home_anchor('contato', depth)}">Fale conosco</a>
    </nav>
  </div>
</header>
'''

def footer(depth, wa_subject=None):
    cols = ""
    for gkey, gname in GROUPS:
        links = "\n".join(f'          <a href="{page_href("servicos/%s/" % s["slug"], depth)}">{s["name"]}</a>' for s in SERVICES if s["group"] == gkey)
        cols += f'''
      <nav class="foot-col" aria-label="{gname}">
        <p class="foot-title">{gname}</p>
{links}
      </nav>'''
    return f'''
<footer>
  <div class="wrap">
    <div class="top">
      <div>
        <span class="brand-name" style="color:#fff">Korberg &amp; Müller<small>CONSULTING</small></span>
        <p class="slogan">Inteligência artificial, resultado real.</p>
      </div>
      <div class="foot-cols">{cols}
      <nav class="foot-col" aria-label="Institucional">
        <p class="foot-title">Institucional</p>
          <a href="{page_href('servicos/', depth)}">Todos os serviços</a>
          <a href="{page_href('insights/', depth)}">Insights</a>
          <a href="{home_anchor('abordagem', depth)}">Abordagem</a>
          <a href="{home_anchor('lideranca', depth)}">Liderança</a>
          <a href="{home_anchor('contato', depth)}">Contato</a>
      </nav>
      </div>
    </div>
    <div class="bottom">
      <span>© <span id="ano">{datetime.date.today().year}</span> Korberg &amp; Müller Consulting (Korberg &amp; Muller), Porto Alegre, RS. Todos os direitos reservados.</span>
      <span>{LEGAL}</span>
    </div>
  </div>
</footer>

<a class="wa-float" href="{wa_link(wa_subject)}" target="_blank" rel="noopener" aria-label="Conversar com a Korberg &amp; Müller no WhatsApp">
  {WA_ICON}
  <span>WhatsApp</span>
</a>

<script src="{pref(depth)}assets/site.js" defer></script>
</body>
</html>
'''

ORG_REF = {"@type": "ProfessionalService", "@id": BASE + "#empresa", "name": "Korberg & Müller Consulting", "url": BASE}
AREA = [
  {"@type": "City", "name": "Porto Alegre"},
  {"@type": "AdministrativeArea", "name": "Região Metropolitana de Porto Alegre"},
  {"@type": "State", "name": "Rio Grande do Sul"},
  {"@type": "Country", "name": "Brasil"},
]

def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": url(p)} for i, (n, p) in enumerate(items)]}

def card(s, depth):
    href = page_href("servicos/%s/" % s["slug"], depth)
    if s["group"] == "gestao":
        lis = "".join(f"<li>{x}</li>" for x in s["card_list"])
        return f'''
        <article class="cap-wide">
          <div>
            <h3><a href="{href}">{s["name"]}</a></h3>
            <p class="offer">{s["offer"]}</p>
            <p>{s["card"]}</p>
            <span class="more" aria-hidden="true">Conheça o serviço</span>
          </div>
          <ul>{lis}</ul>
        </article>'''
    return f'''
        <article class="cap">
          <svg viewBox="0 0 28 28" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">{ICONS[s["icon"]]}</svg>
          <h3><a href="{href}">{s["name"]}</a></h3>
          <p>{s["card"]}</p>
          <span class="more" aria-hidden="true">Conheça o serviço</span>
        </article>'''

def services_groups(depth):
    out = ""
    for gkey, gname in GROUPS:
        items = [s for s in SERVICES if s["group"] == gkey]
        inner = "".join(card(s, depth) for s in items)
        grid = f'<div class="cap-grid">{inner}\n      </div>' if gkey == "tec" else inner
        out += f'''
      <div class="group">
        <h3 class="group-title">{gname}</h3>
        {grid}
      </div>'''
    return out

IMG_DIR_CANDIDATES = []
def has_img(name):
    return any(os.path.exists(os.path.join(d, "images", name)) for d in [OUT] + IMG_DIR_CANDIDATES)
def img_tag(name, alt, w, h, depth, cls="", eager=False):
    if not has_img(name): return ""
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img class="{cls}" src="{pref(depth)}images/{name}" width="{w}" height="{h}" alt="{esc(alt)}" {load} decoding="async">'

def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or OUT, exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)

# ---------- página inicial ----------
def wide_photo(name, alt, depth):
    t = img_tag(name, alt, 1600, 686, depth, "wide-photo") or HOME_WIDE
    return f"\n      <figure class=\"wide-figure illo-wrap\">{t}</figure>"

def build_home():
    d = 0
    org = {
      "@context": "https://schema.org", "@type": "ProfessionalService", "@id": BASE + "#empresa",
      "name": "Korberg & Müller Consulting", "legalName": "NBNG COMERCIO E SERVICOS LTDA - ME", "taxID": "24.206.394/0001-05",
      "alternateName": ["Korberg & Müller", "Korberg & Muller", "Korberg Mueller", "K&M Consulting"],
      "slogan": "Inteligência artificial, resultado real.",
      "description": "Consultoria empresarial, de RH e de inteligência artificial para pequenas e médias empresas de Porto Alegre e região, com atendimento presencial.",
      "url": BASE, "telephone": "+55-51-99810-7741", "logo": url("icon-192.png"), "image": url("og-image.png"),
      "address": {"@type": "PostalAddress", "addressLocality": "Porto Alegre", "addressRegion": "RS", "addressCountry": "BR"},
      "areaServed": AREA, "inLanguage": "pt-BR",
      "knowsAbout": ["Consultoria empresarial", "Consultoria de RH", "Gestão de pessoas", "Inteligência artificial", "Automação de processos", "Agentes de IA", "Integração de sistemas", "Funis de vendas", "LGPD"],
      "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Serviços", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": strip_amp(s["name"]), "url": url("servicos/%s/" % s["slug"])}} for s in SERVICES]},
    }
    opts = "\n".join(f"              <option>{s['name']}{' (' + s['offer'] + ')' if s.get('offer') else ''}</option>" for s in SERVICES)
    html = head(d, "Consultoria empresarial e IA em Porto Alegre | Korberg &amp; Müller",
                "Consultoria empresarial, de RH e de IA para pequenas e médias empresas de Porto Alegre: gestão de pessoas, automação de processos e agentes de IA. Vamos até a sua empresa.",
                "", [org]) + header(d) + f'''
<main id="conteudo">
  <section class="hero" id="topo" aria-labelledby="hero-title">
    <div class="wrap">
      <div>
        <h1 id="hero-title">Consultoria empresarial e IA para pequenas e médias empresas em Porto Alegre</h1>
        <p class="slogan"><span>Inteligência</span><span>artificial,</span><span class="real">resultado real.</span></p>
        <p class="lede">Vamos até a sua empresa entender os processos e as pessoas antes de propor qualquer solução. Em seguida, entregamos uma estratégia clara, automações que funcionam no dia a dia, agentes de IA sob medida e uma gestão de pessoas estruturada.</p>
        <div class="btn-row">
          <a class="btn btn-light" href="#contato">Agendar uma conversa</a>
          <a class="btn btn-ghost" href="#capacidades">Ver o que fazemos</a>
        </div>
      </div>
      <figure class="signal-fig" style="margin:0">
        <svg id="signal" viewBox="0 0 560 420" role="img" aria-label="Ilustração: uma linha irregular que se organiza em uma curva de crescimento">
          <g stroke="rgba(255,255,255,.08)" stroke-width="1">
            <line x1="0" y1="70" x2="560" y2="70"/><line x1="0" y1="140" x2="560" y2="140"/>
            <line x1="0" y1="210" x2="560" y2="210"/><line x1="0" y1="280" x2="560" y2="280"/>
            <line x1="0" y1="350" x2="560" y2="350"/>
            <line x1="112" y1="0" x2="112" y2="420"/><line x1="224" y1="0" x2="224" y2="420"/>
            <line x1="336" y1="0" x2="336" y2="420"/><line x1="448" y1="0" x2="448" y2="420"/>
          </g>
          <path id="signal-area" fill="url(#fade)" d=""/>
          <path id="signal-line" fill="none" stroke="#8DB3FF" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" d=""/>
          <circle id="signal-dot" r="6" fill="#fff" cx="-20" cy="-20"/>
          <defs>
            <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0" stop-color="#8DB3FF" stop-opacity=".22"/>
              <stop offset="1" stop-color="#8DB3FF" stop-opacity="0"/>
            </linearGradient>
          </defs>
        </svg>
        <figcaption class="signal-cap"><span>Dados dispersos</span><span>Decisão e resultado</span></figcaption>
      </figure>
    </div>
  </section>

  <section class="sec manifesto" id="abordagem" aria-labelledby="abordagem-title">
    <div class="wrap">
      <div class="cols">
        <div>
          <h2 id="abordagem-title" style="margin-bottom:36px">Nossa abordagem</h2>
          <blockquote>Tecnologia de ponta só gera valor quando muda a forma como a empresa decide e opera.</blockquote>
        </div>
        <div>
          <p>A Korberg &amp; Müller traduz para pequenas e médias empresas os métodos que as grandes consultorias aplicam em grandes organizações. Unimos visão de gestão, cuidado com as pessoas e domínio técnico, e começamos pelo problema de negócio, não pela ferramenta: onde está o gargalo, quanto ele custa e qual decisão precisa ser agilizada.</p>
          <p>Em seguida, desenhamos e construímos a solução com a sua equipe, integrada aos sistemas que a empresa já utiliza, com segurança de dados desde o primeiro dia e indicadores que mostram o retorno.</p>
          <p>Somos uma consultoria enxuta por opção: quem desenha a estratégia é quem acompanha a entrega. Atendemos pessoalmente pequenas e médias empresas de Porto Alegre e região.</p>
        </div>
      </div>{wide_photo('abordagem.jpg', 'Consultores e equipe do cliente reunidos em torno de uma mesa de trabalho', d)}
    </div>
  </section>

  <section class="sec principles" aria-labelledby="princ-title">
    <div class="wrap">
      <div class="sec-head">
        <h2 id="princ-title">Estratégia de grande empresa, no tamanho da sua</h2>
        <p>Os métodos das maiores consultorias do mundo foram desenhados para organizações com milhares de pessoas. Nós os adaptamos à realidade de uma pequena ou média empresa.</p>
      </div>
      <div class="princ-grid">
        <article><h3>Escopo proporcional</h3><p>Uma ou duas áreas por vez, escolhidas pelo valor que geram e pela facilidade de implantar. Nada de projetos que tentam mudar tudo de uma só vez.</p></article>
        <article><h3>Pessoas e tecnologia juntas</h3><p>Ferramenta nenhuma funciona sem uma equipe preparada. Por isso cuidamos da gestão de pessoas e da tecnologia no mesmo projeto.</p></article>
        <article><h3>Adoção faz parte do projeto</h3><p>Treinamento, ajuste das rotinas e acompanhamento até a solução ser usada no dia a dia. Uma solução que ninguém usa não gera resultado.</p></article>
      </div>
    </div>
  </section>

  <section class="sec caps" id="capacidades" aria-labelledby="caps-title">
    <div class="wrap">
      <div class="sec-head">
        <h2 id="caps-title">Serviços de gestão, RH e inteligência artificial</h2>
        <p>Duas áreas de atuação que podem ser contratadas separadamente ou combinadas em um programa de transformação.</p>
      </div>{services_groups(d)}
    </div>
  </section>

  <section class="sec method" id="metodo" aria-labelledby="metodo-title">
    <div class="wrap">
      <div class="sec-head">
        <h2 id="metodo-title">Como implementamos IA na sua empresa</h2>
        <p>Um ciclo curto e mensurável, com indicadores definidos no início. Cada etapa termina com uma entrega que a liderança pode avaliar antes de seguirmos para a próxima.</p>
      </div>
      <ol class="steps">
        <li><h3>Diagnóstico</h3><p>Visitas presenciais, entrevistas e leitura dos processos e dos dados para identificar onde a IA gera mais valor.</p></li>
        <li><h3>Desenho</h3><p>Solução, arquitetura, custos e indicadores de sucesso definidos com os responsáveis.</p></li>
        <li><h3>Construção</h3><p>Desenvolvimento em ciclos curtos, com testes reais e revisão de segurança.</p></li>
        <li><h3>Adoção e escala</h3><p>Treinamento da equipe, revisões periódicas de resultado e expansão para novas áreas. O projeto só termina quando a solução faz parte da rotina.</p></li>
      </ol>
    </div>
  </section>

  <section class="sec insights-teaser" aria-labelledby="ins-title">
    <div class="wrap">
      <div class="sec-head">
        <h2 id="ins-title">Insights</h2>
        <p>Leituras e reflexões sobre gestão, pessoas e inteligência artificial, traduzidas para pequenas e médias empresas.</p>
      </div>
      <div class="post-list">{post_cards(d)}
      </div>
    </div>
  </section>

  <section class="sec" id="lideranca" aria-labelledby="lideranca-title">
    <div class="wrap">
      <div class="sec-head">
        <h2 id="lideranca-title">Liderança</h2>
        <p>Sócios que acompanham pessoalmente cada projeto, do diagnóstico aos resultados.</p>
      </div>
      <div class="lead-grid">
        <div class="person">
          <div class="avatar empty">[FOTO]</div>
          <div>
            <h3>Felipe [SOBRENOME]</h3>
            <p class="role">Sócio fundador</p>
            <p>[Resumo da trajetória: formação, experiência em gestão e tecnologia, setores em que atuou.]</p>
          </div>
        </div>
        <div class="person">
          <div class="avatar"><img src="images/mariana.jpg" width="480" height="600" alt="Retrato de Mariana, sócia fundadora da Korberg &amp; Müller" loading="lazy" decoding="async"></div>
          <div>
            <h3>Mariana [SOBRENOME]</h3>
            <p class="role">Sócia fundadora</p>
            <p>[Resumo da trajetória: formação, experiência em gestão e tecnologia, setores em que atuou.]</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="sec contact" id="contato" aria-labelledby="contato-title">
    <div class="wrap">
      <div class="cols">
        <div class="intro">
          <h2 id="contato-title" style="margin-bottom:24px">Vamos conversar sobre o seu desafio</h2>
          <p>Conte em poucas linhas o que você quer melhorar. Respondemos em até dois dias úteis com uma proposta para a próxima etapa.</p>
          <dl>
            <div><dt>E-mail</dt><dd>[contato@seudominio.com.br]</dd></div>
            <div><dt>WhatsApp</dt><dd><a href="{wa_link()}" target="_blank" rel="noopener">{WA_DISPLAY}</a></dd></div>
            <div><dt>Atendimento</dt><dd>Presencial em Porto Alegre e região metropolitana; remoto para todo o Brasil.</dd></div>
          </dl>
        </div>
        <form id="form-contato" novalidate>
          <div class="row2">
            <div class="field"><label for="nome">Nome</label><input id="nome" name="nome" autocomplete="name" required maxlength="100"></div>
            <div class="field"><label for="empresa">Empresa</label><input id="empresa" name="empresa" autocomplete="organization" maxlength="100"></div>
          </div>
          <div class="field"><label for="email">E-mail corporativo</label><input id="email" name="email" type="email" autocomplete="email" required maxlength="150"></div>
          <div class="field">
            <label for="interesse">Interesse principal</label>
            <select id="interesse" name="interesse">
{opts}
            </select>
          </div>
          <div class="field"><label for="mensagem">Mensagem</label><textarea id="mensagem" name="mensagem" required maxlength="2000"></textarea></div>
          <button class="btn btn-dark" type="submit">Enviar mensagem</button>
          <p class="form-note">Ao clicar em Enviar mensagem, seu aplicativo de e-mail será aberto com o texto pronto. Usamos seus dados apenas para responder a este contato.</p>
          <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </div>
  </section>
</main>
''' + footer(d)
    write("index.html", html)

# ---------- página de serviços ----------
def build_hub():
    d = 1
    path = "servicos/"
    lds = [crumbs_ld([("Início", ""), ("Serviços", path)]),
           {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
             {"@type": "ListItem", "position": i + 1, "name": strip_amp(s["name"]), "url": url("servicos/%s/" % s["slug"])} for i, s in enumerate(SERVICES)]}]
    html = head(d, "Serviços de consultoria empresarial, RH e IA em Porto Alegre | Korberg &amp; Müller",
                "Conheça os serviços da Korberg & Müller para pequenas e médias empresas de Porto Alegre: consultoria de RH, estratégia de IA, automação de processos, agentes de IA e mais.",
                path, lds) + header(d, "servicos") + f'''
<main id="conteudo">
  <section class="page-hero" aria-labelledby="page-title">
    <div class="wrap">
      <ol class="crumbs" aria-label="Você está em"><li><a href="{page_href('', d)}">Início</a></li><li aria-current="page">Serviços</li></ol>
      <h1 id="page-title">Serviços de consultoria empresarial, RH e inteligência artificial</h1>
      <p class="lede">Atendemos pequenas e médias empresas de Porto Alegre e região em duas frentes: tecnologia e IA, para tornar a operação mais eficiente, e gestão e pessoas, para estruturar a liderança e a área de RH.</p>
      <div class="btn-row">
        <a class="btn btn-light" href="{home_anchor('contato', d)}">Agendar uma conversa</a>
      </div>
    </div>
  </section>

  <section class="sec caps" aria-label="Lista de serviços">
    <div class="wrap">{services_groups(d)}
    </div>
  </section>
</main>
''' + footer(d)
    write("servicos/index.html", html)

# ---------- páginas de cada serviço ----------
def build_service(s):
    d = 2
    path = "servicos/%s/" % s["slug"]
    name_plain = strip_amp(s["name"]) + (" (" + s["offer"] + ")" if s.get("offer") else "")
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": name_plain,
              "serviceType": strip_amp(s["name"]), "description": strip_amp(s["desc"]), "url": url(path),
              "provider": ORG_REF, "areaServed": AREA}
    lds = [svc_ld, crumbs_ld([("Início", ""), ("Serviços", "servicos/"), (strip_amp(s["name"]), path)])]

    offer = f'\n      <p class="offer">{s["offer"]}</p>' if s.get("offer") else ""
    intro = ""
    if s.get("intro"):
        ps = "".join(f"<p>{x}</p>" for x in s["intro"])
        intro = f'''
  <section class="sec" aria-labelledby="intro-title">
    <div class="wrap">
      <div class="sec-head" style="margin-bottom:0">
        <h2 id="intro-title">{s["intro_h"]}</h2>
        <div class="prose">{ps}</div>
      </div>
    </div>
  </section>'''
    callout = ""
    if s.get("callout"):
        ps = "".join(f"<p>{x}</p>" for x in s["callout"])
        callout = f'''
  <section class="sec callout" aria-labelledby="callout-title">
    <div class="wrap">
      <div class="cols">
        <div>
          <h2 id="callout-title" class="visually-hidden">Por que um RH externo</h2>
          <blockquote>{s["callout_q"]}</blockquote>
        </div>
        <div>{ps}</div>
      </div>
    </div>
  </section>'''
    deliv = "".join(f'\n        <article><h3>{t}</h3><p>{p}</p></article>' for t, p in s["deliv"])
    fit = "".join(f'\n        <li>{CHECK}<span>{x}</span></li>' for x in s["fit"])
    steps = "".join(f'\n        <li><h3>{t}</h3><p>{p}</p></li>' for t, p in s["steps"])
    faq = "".join(f'\n        <details><summary>{q}</summary><p>{a}</p></details>' for q, a in s["faq"])
    related = [x for x in SERVICES if x["slug"] != s["slug"]]
    if s["group"] == "gestao":
        related = [x for x in related if x["slug"] in ("automacao-de-processos", "estrategia-de-ia", "agentes-de-ia")]
    else:
        related = [x for x in related if x["group"] == "tec"][:2] + [BY_SLUG["consultoria-de-rh"]]
    rel = "".join(f'\n        <li><a href="{page_href("servicos/%s/" % x["slug"], d)}">{x["name"]}</a></li>' for x in related)
    alt_bg = "" if not s.get("callout") else ""
    photo = img_tag(s["slug"] + ".jpg", s.get("img_alt", ""), 960, 1200, d, "hero-photo", eager=True) or SERVICE_ILLOS.get(s["slug"], "")
    hero_cls = "page-hero has-photo" if photo else "page-hero"
    photo_html = f'\n      <figure class="hero-figure illo-wrap">{photo}</figure>' if photo else ""
    html = head(d, s["title"], s["desc"], path, lds) + header(d, "servicos") + f'''
<main id="conteudo">
  <section class="{hero_cls}" aria-labelledby="page-title">
    <div class="wrap"><div class="hero-text">
      <ol class="crumbs" aria-label="Você está em"><li><a href="{page_href('', d)}">Início</a></li><li><a href="{page_href('servicos/', d)}">Serviços</a></li><li aria-current="page">{s["name"]}</li></ol>
      <h1 id="page-title">{s["h1"]}</h1>{offer}
      <p class="lede">{s["lede"]}</p>
      <div class="btn-row">
        <a class="btn btn-light" href="{home_anchor('contato', d)}">Agendar uma conversa</a>
        <a class="btn btn-ghost" href="{wa_link(strip_amp(s['name']))}" target="_blank" rel="noopener">Conversar no WhatsApp</a>
      </div>
    </div>{photo_html}
    </div>
  </section>
{callout}{intro}
  <section class="sec" aria-labelledby="deliv-title">
    <div class="wrap">
      <div class="sec-head">
        <h2 id="deliv-title">O que entregamos</h2>
        <p>Cada entrega é ajustada ao porte e ao momento da empresa, com presença em Porto Alegre e região.</p>
      </div>
      <div class="deliv">{deliv}
      </div>
    </div>
  </section>

  <section class="sec caps" aria-labelledby="fit-title">
    <div class="wrap">
      <div class="sec-head">
        <h2 id="fit-title">Quando faz sentido</h2>
        <p>Situações comuns em pequenas e médias empresas que costumam indicar a necessidade deste serviço.</p>
      </div>
      <ul class="fit">{fit}
      </ul>
    </div>
  </section>

  <section class="sec method" aria-labelledby="steps-title">
    <div class="wrap">
      <div class="sec-head">
        <h2 id="steps-title">Como funciona</h2>
        <p>Etapas curtas, com entregas que a liderança avalia antes de seguirmos para a próxima.</p>
      </div>
      <ol class="steps">{steps}
      </ol>
    </div>
  </section>

  <section class="sec" aria-labelledby="faq-title">
    <div class="wrap">
      <div class="sec-head">
        <h2 id="faq-title">Perguntas frequentes</h2>
      </div>
      <div class="faq">{faq}
      </div>
    </div>
  </section>

  <section class="cta-band" aria-labelledby="cta-title">
    <div class="wrap">
      <div>
        <h2 id="cta-title">Vamos conversar sobre a sua empresa</h2>
        <p>Conte o seu desafio. Respondemos em até dois dias úteis e, se fizer sentido, marcamos uma visita.</p>
      </div>
      <div class="btn-row">
        <a class="btn btn-light" href="{home_anchor('contato', d)}">Agendar uma conversa</a>
        <a class="btn btn-ghost" href="{wa_link(strip_amp(s['name']))}" target="_blank" rel="noopener">WhatsApp</a>
      </div>
    </div>
  </section>

  <section class="sec" aria-labelledby="rel-title" style="padding-top:88px;padding-bottom:88px">
    <div class="wrap">
      <h2 id="rel-title" style="font-size:clamp(28px,3vw,38px);margin-bottom:24px">Outros serviços</h2>
      <ul class="related">{rel}
      </ul>
    </div>
  </section>
</main>
''' + footer(d, strip_amp(s["name"]))
    write(path + "index.html", html)

# ---------- Insights ----------
def post_cards(depth):
    out = ""
    for a in sorted(ARTICLES, key=lambda x: x["date"], reverse=True):
        href = page_href("insights/%s/" % a["slug"], depth)
        out += f'''
        <article class="post-card">
          <p class="post-meta"><time datetime="{a['date']}">{a['date_br']}</time>, {a['read']}</p>
          <h3><a href="{href}">{a['h1']}</a></h3>
          <p>{a['card']}</p>
          <span class="more" aria-hidden="true">Ler o artigo</span>
        </article>'''
    return out

def build_insights_hub():
    d = 1
    path = "insights/"
    lds = [crumbs_ld([("Início", ""), ("Insights", path)])]
    html = head(d, "Insights sobre gestão, pessoas e IA para PMEs | Korberg &amp; Müller",
                "Artigos da Korberg & Müller sobre gestão, pessoas e inteligência artificial para pequenas e médias empresas.",
                path, lds) + header(d, "insights") + f'''
<main id="conteudo">
  <section class="page-hero" aria-labelledby="page-title">
    <div class="wrap">
      <ol class="crumbs" aria-label="Você está em"><li><a href="{page_href('', d)}">Início</a></li><li aria-current="page">Insights</li></ol>
      <h1 id="page-title">Insights</h1>
      <p class="lede">Leituras e reflexões sobre gestão, pessoas e inteligência artificial, com o que as grandes empresas fazem traduzido para a realidade de pequenas e médias empresas.</p>
    </div>
  </section>
  <section class="sec" aria-label="Artigos">
    <div class="wrap">
      <div class="post-list">{post_cards(d)}
      </div>
    </div>
  </section>
</main>
''' + footer(d)
    write("insights/index.html", html)

def build_article(a):
    d = 2
    path = "insights/%s/" % a["slug"]
    art_ld = {"@context": "https://schema.org", "@type": "Article", "headline": strip_amp(a["h1"]),
              "description": strip_amp(a["desc"]), "datePublished": a["date"], "dateModified": a["date"],
              "inLanguage": "pt-BR", "mainEntityOfPage": url(path), "image": url("og-image.png"),
              "author": ORG_REF, "publisher": {**ORG_REF, "logo": {"@type": "ImageObject", "url": url("icon-192.png")}}}
    lds = [art_ld, crumbs_ld([("Início", ""), ("Insights", "insights/"), (strip_amp(a["h1"]), path)])]
    rel = "".join(f'\n        <li><a href="{page_href("servicos/%s/" % sl, d)}">{BY_SLUG[sl]["name"]}</a></li>' for sl in a["related"])
    html = head(d, a["title"], a["desc"], path, lds) + header(d, "insights") + f'''
<main id="conteudo">
  <article>
  <section class="page-hero" aria-labelledby="page-title">
    <div class="wrap">
      <ol class="crumbs" aria-label="Você está em"><li><a href="{page_href('', d)}">Início</a></li><li><a href="{page_href('insights/', d)}">Insights</a></li><li aria-current="page">Artigo</li></ol>
      <h1 id="page-title">{a["h1"]}</h1>
      <p class="lede">{a["lede"]}</p>
      <p class="post-meta post-meta-dark">Por Korberg &amp; Müller, <time datetime="{a['date']}">{a['date_br']}</time>, {a['read']}</p>
    </div>
  </section>
  <section class="sec article-sec">
    <div class="wrap">
      <div class="article-body">{a["body"]}
      </div>
    </div>
  </section>
  </article>

  <section class="cta-band" aria-labelledby="cta-title">
    <div class="wrap">
      <div>
        <h2 id="cta-title">Quer aplicar isso na sua empresa?</h2>
        <p>Conte o seu desafio. Respondemos em até dois dias úteis e, se fizer sentido, marcamos uma visita.</p>
      </div>
      <div class="btn-row">
        <a class="btn btn-light" href="{home_anchor('contato', d)}">Agendar uma conversa</a>
        <a class="btn btn-ghost" href="{wa_link('o artigo sobre o Rewired')}" target="_blank" rel="noopener">WhatsApp</a>
      </div>
    </div>
  </section>

  <section class="sec" aria-labelledby="rel-title" style="padding-top:88px;padding-bottom:88px">
    <div class="wrap">
      <h2 id="rel-title" style="font-size:clamp(28px,3vw,38px);margin-bottom:24px">Serviços relacionados</h2>
      <ul class="related">{rel}
      </ul>
    </div>
  </section>
</main>
''' + footer(d)
    write(path + "index.html", html)

# ---------- 404 ----------
def build_404():
    global ABS
    ABS = True
    d = 0
    html = head(d, "Página não encontrada | Korberg &amp; Müller", "A página procurada não existe ou mudou de endereço.", "404.html", [], "noindex") + header(d) + f'''
<main id="conteudo">
  <section class="page-hero notfound" aria-labelledby="page-title">
    <div class="wrap">
      <h1 id="page-title">Página não encontrada</h1>
      <p class="lede">O endereço pode ter mudado. Veja os nossos serviços ou volte para a página inicial.</p>
      <div class="btn-row">
        <a class="btn btn-light" href="/servicos/">Ver serviços</a>
        <a class="btn btn-ghost" href="/">Página inicial</a>
      </div>
    </div>
  </section>
</main>
''' + footer(d)
    ABS = False
    write("404.html", html)

# ---------- arquivos de apoio ----------
def build_assets():
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    css = "".join(open(os.path.join(SRC, f), encoding="utf-8").read() for f in ("base.css", "extra.css", "motion.css", "content.css"))
    css += '''
/* Rodapé com colunas de links */
.foot-cols{display:flex;flex-wrap:wrap;gap:40px 56px}
.foot-col{display:flex;flex-direction:column;gap:10px;min-width:180px}
.foot-title{margin:0 0 6px;font-weight:600;color:#fff;font-size:15px}
.foot-col a{color:#DCE5F1;text-decoration:none;font-size:15px}
.foot-col a:hover{color:#fff;text-decoration:underline}
.visually-hidden{position:absolute!important;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.nav a[aria-current="page"]{color:#fff;text-decoration:underline;text-underline-offset:6px}
'''
    open(os.path.join(OUT, "assets/site.css"), "w", encoding="utf-8").write(css)
    shutil.copy(os.path.join(SRC, "site.js"), os.path.join(OUT, "assets/site.js"))
    open(os.path.join(OUT, "assets/js-flag.js"), "w").write('document.documentElement.classList.add("js");\n')

def build_seo():
    pages = [("", "1.0"), ("servicos/", "0.9")] + [("servicos/%s/" % s["slug"], "0.8") for s in SERVICES] + [("insights/", "0.7")] + [("insights/%s/" % a["slug"], "0.7") for a in ARTICLES]
    urls = "\n".join(f"  <url>\n    <loc>{url(p)}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </url>" for p, _ in pages)
    open(os.path.join(OUT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /_fonte/\n\nSitemap: {url('sitemap.xml')}\n")
    csp = ("default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
           "font-src https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self'; form-action 'none'; "
           "base-uri 'self'; object-src 'none'; frame-ancestors 'none'; upgrade-insecure-requests")
    open(os.path.join(OUT, "_headers"), "w").write(f"""/*
  Content-Security-Policy: {csp}
  Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: DENY
  Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()

/assets/*
  Cache-Control: public, max-age=3600
""")

build_assets(); build_home(); build_hub(); build_insights_hub()
for a in ARTICLES: build_article(a)
for s in SERVICES: build_service(s)
build_404(); build_seo()
print("ok:", MODE, OUT)
