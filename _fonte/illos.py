# Ilustrações originais da Korberg & Müller (SVG inline, animadas por CSS).
# Classes: pop (surge), draw (traço se desenha; usar pathLength="1"), flow (tracejado em movimento),
# pulse (anel pulsando), spin (giro lento), grow (barra cresce), fall (ponto caindo), blink (pontos digitando).
# Camadas <g class="layer" style="--k:.."> se movem com o mouse.

L = "#8DB3FF"; W = "#FFFFFF"; M = "#C9D5E6"; N1 = "#0A2342"; N2 = "#12345E"; N3 = "#1B4475"; B = "#3E7BFA"; S = "#2457D6"

def d(x): return f'style="--d:{x}s"'

def person(x, y, s=1.0, head=M, body=None, cls="pop", delay=0):
    body = body or head
    r = 11 * s
    return (f'<g class="{cls}" {d(delay)}><circle cx="{x}" cy="{y}" r="{r:.1f}" fill="{head}"/>'
            f'<path d="M{x-20*s:.1f} {y+44*s:.1f} Q{x-20*s:.1f} {y+17*s:.1f} {x} {y+17*s:.1f} Q{x+20*s:.1f} {y+17*s:.1f} {x+20*s:.1f} {y+44*s:.1f} Z" fill="{body}"/></g>')

def frame(label, inner):
    grid = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="560"/>' for x in range(40, 480, 40)) + \
           "".join(f'<line x1="0" y1="{y}" x2="480" y2="{y}"/>' for y in range(40, 560, 40))
    return (f'<svg class="illo" viewBox="0 0 480 560" role="img" aria-label="{label}">'
            f'<rect x=".5" y=".5" width="479" height="559" rx="6" fill="{N2}" stroke="rgba(255,255,255,.1)"/>'
            f'<g stroke="rgba(255,255,255,.045)" stroke-width="1">{grid}</g>{inner}</svg>')

def lines(x, y, n, w, gap=12, color="rgba(255,255,255,.55)", sw=4):
    return "".join(f'<line x1="{x}" y1="{y+i*gap}" x2="{x+(w if i < n-1 else w*0.6):.0f}" y2="{y+i*gap}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>' for i in range(n))

# ---------------- Estratégia de IA: roteiro ----------------
ESTRATEGIA = frame("Ilustração: notas de planejamento e um roteiro com marcos que sobe até uma bandeira", f'''
<g class="layer" style="--k:.5">
  <g class="pop" {d(.15)}><rect x="56" y="70" width="64" height="64" rx="4" fill="{N3}" stroke="rgba(255,255,255,.18)"/>{lines(68, 90, 3, 40)}</g>
  <g class="pop" {d(.3)}><rect x="132" y="70" width="64" height="64" rx="4" fill="{B}"/>{lines(144, 90, 3, 40, color="rgba(255,255,255,.85)")}</g>
  <g class="pop" {d(.45)}><rect x="56" y="146" width="64" height="64" rx="4" fill="{N3}" stroke="rgba(255,255,255,.18)"/>{lines(68, 166, 3, 40)}</g>
</g>
<g class="layer" style="--k:1">
  <line x1="56" y1="470" x2="424" y2="470" stroke="rgba(255,255,255,.25)" stroke-width="2"/>
  <path class="draw" pathLength="1" {d(.4)} d="M60 440 C150 425 190 360 250 330 S370 210 410 170" fill="none" stroke="{L}" stroke-width="4" stroke-linecap="round"/>
  <g class="pop" {d(.9)}><circle cx="122" cy="423" r="12" fill="{N1}" stroke="{L}" stroke-width="4"/></g>
  <g class="pop" {d(1.25)}><circle cx="250" cy="330" r="12" fill="{N1}" stroke="{L}" stroke-width="4"/></g>
  <g class="pop" {d(1.6)}><circle cx="410" cy="170" r="14" fill="{L}"/></g>
  <g class="pop" {d(1.9)}><line x1="410" y1="156" x2="410" y2="96" stroke="{W}" stroke-width="3"/><path d="M410 96 L448 110 L410 124 Z" fill="{W}"/></g>
  <g class="pop" {d(1.0)}>{lines(102, 492, 1, 40, color="rgba(255,255,255,.35)")}</g>
  <g class="pop" {d(1.35)}>{lines(230, 492, 1, 40, color="rgba(255,255,255,.35)")}</g>
  <g class="pop" {d(1.7)}>{lines(388, 492, 1, 40, color="rgba(255,255,255,.35)")}</g>
</g>
<g class="layer" style="--k:1.4">
  <circle class="pulse" cx="410" cy="170" r="14" fill="none" stroke="{L}" stroke-width="2"/>
</g>''')

# ---------------- Automação de processos: fluxo ----------------
def box(x, y, w, h, fill, inner, delay):
    return f'<g class="pop" {d(delay)}><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="rgba(255,255,255,.18)"/>{inner}</g>'

GEAR = lambda cx, cy: (f'<circle cx="{cx}" cy="{cy}" r="13" fill="none" stroke="{W}" stroke-width="4"/>'
                       + "".join(f'<line x1="{cx}" y1="{cy-22}" x2="{cx}" y2="{cy-16}" stroke="{W}" stroke-width="5" stroke-linecap="round" transform="rotate({a} {cx} {cy})"/>' for a in range(0, 360, 45)))
SPARK = lambda cx, cy, r=18, c=W: f'<path d="M{cx} {cy-r} Q{cx+r*.18} {cy-r*.18} {cx+r} {cy} Q{cx+r*.18} {cy+r*.18} {cx} {cy+r} Q{cx-r*.18} {cy+r*.18} {cx-r} {cy} Q{cx-r*.18} {cy-r*.18} {cx} {cy-r} Z" fill="{c}"/>'

AUTOMACAO = frame("Ilustração: etapas de um processo ligadas por fluxos automáticos até um resultado concluído", f'''
<g class="layer" style="--k:.6">
  <path class="flow" d="M196 128 H284" stroke="{L}" stroke-width="3" fill="none"/>
  <path class="flow" d="M352 166 V250" stroke="{L}" stroke-width="3" fill="none"/>
  <path class="flow" d="M284 290 H196" stroke="{L}" stroke-width="3" fill="none"/>
  <path class="flow" d="M128 328 V410" stroke="{L}" stroke-width="3" fill="none"/>
</g>
<g class="layer" style="--k:1">
  {box(60, 90, 136, 76, N3, GEAR(128, 128), .1)}
  {box(284, 90, 136, 76, N3, lines(306, 116, 3, 92), .35)}
  {box(284, 250, 136, 76, B, SPARK(352, 288), .6)}
  {box(60, 250, 136, 76, N3, "".join(f'<rect x="{88+i*22}" y="{304-h}" width="14" height="{h}" fill="{L}"/>' for i, h in enumerate([18, 30, 24, 40])), .85)}
  <g class="pop" {d(1.15)}><rect x="60" y="410" width="360" height="92" rx="6" fill="{W}"/>
    <circle cx="112" cy="456" r="24" fill="{S}"/><path d="M100 456 L109 466 L126 446" stroke="{W}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    {lines(156, 444, 2, 220, gap=22, color="#C9D5E6", sw=6)}</g>
</g>''')

# ---------------- Agentes de IA: celular com conversa ----------------
def bubble(x, y, w, fill, delay, right=False):
    return f'<g class="pop" {d(delay)}><rect x="{x}" y="{y}" width="{w}" height="44" rx="14" fill="{fill}"/>{lines(x+14, y+16, 2, w-34, gap=12, color="rgba(255,255,255,.8)", sw=4)}</g>'

AGENTES = frame("Ilustração: celular com uma conversa entre um cliente e um agente de IA", f'''
<g class="layer" style="--k:.5">
  {person(78, 404, 1.15, M, cls="pop", delay=.2)}
  <path class="flow" d="M104 420 C130 420 140 380 150 380" stroke="rgba(255,255,255,.4)" stroke-width="2" fill="none"/>
</g>
<g class="layer" style="--k:1">
  <rect x="150" y="56" width="190" height="420" rx="26" fill="{N1}" stroke="rgba(255,255,255,.55)" stroke-width="3"/>
  <rect x="212" y="70" width="66" height="8" rx="4" fill="rgba(255,255,255,.25)"/>
  {bubble(166, 108, 130, N3, .4)}
  {bubble(194, 166, 130, S, .9)}
  {bubble(166, 224, 110, N3, 1.4)}
  {bubble(194, 282, 130, S, 1.9)}
  <g class="pop" {d(2.3)}><rect x="166" y="346" width="70" height="36" rx="14" fill="{N3}"/>
    <circle class="blink" {d(0)} cx="186" cy="364" r="4" fill="{W}"/><circle class="blink" {d(.2)} cx="201" cy="364" r="4" fill="{W}"/><circle class="blink" {d(.4)} cx="216" cy="364" r="4" fill="{W}"/></g>
</g>
<g class="layer" style="--k:1.5">
  <circle class="spin" cx="396" cy="170" r="46" fill="none" stroke="{L}" stroke-width="2" stroke-dasharray="4 10"/>
  <g class="pop" {d(.6)}><circle cx="396" cy="170" r="30" fill="{B}"/>{SPARK(396, 170, 15)}</g>
  <path class="flow" d="M366 186 C352 196 346 196 340 196" stroke="{L}" stroke-width="2" fill="none"/>
</g>''')

# ---------------- Dados e integrações: hub ----------------
import math
def tile(cx, cy, kind, delay):
    x, y = cx - 38, cy - 30
    inner = {
      "table": lines(x+12, y+18, 3, 52, gap=11, sw=3),
      "bars": "".join(f'<rect x="{x+14+i*14}" y="{y+46-h}" width="9" height="{h}" fill="{L}"/>' for i, h in enumerate([14, 24, 18, 32])),
      "kanban": "".join(f'<rect x="{x+12+i*19}" y="{y+12}" width="14" height="{h}" rx="2" fill="rgba(255,255,255,.6)"/>' for i, h in enumerate([34, 22, 28])),
      "doc": f'<rect x="{x+22}" y="{y+8}" width="32" height="44" rx="3" fill="none" stroke="{W}" stroke-width="3"/>' + lines(x+29, y+22, 3, 18, gap=8, sw=3),
      "mail": f'<rect x="{x+14}" y="{y+14}" width="48" height="32" rx="3" fill="none" stroke="{W}" stroke-width="3"/><path d="M{x+14} {y+16} L{x+38} {y+34} L{x+62} {y+16}" fill="none" stroke="{W}" stroke-width="3"/>',
      "chat": f'<path d="M{x+16} {y+14} h44 a4 4 0 0 1 4 4 v20 a4 4 0 0 1 -4 4 h-28 l-10 8 v-8 h-6 a4 4 0 0 1 -4 -4 v-20 a4 4 0 0 1 4 -4z" fill="none" stroke="{W}" stroke-width="3"/>',
    }[kind]
    return f'<g class="pop" {d(delay)}><rect x="{x}" y="{y}" width="76" height="60" rx="6" fill="{N3}" stroke="rgba(255,255,255,.2)"/>{inner}</g>'

_kinds = ["table", "bars", "kanban", "doc", "mail", "chat"]
_pos = [(240 + 168*math.cos(math.radians(a)), 290 + 178*math.sin(math.radians(a))) for a in range(-90, 270, 60)]
INTEGRACOES = frame("Ilustração: sistemas como planilha, CRM, e-mail e gestão de projetos conectados a um ponto central", f'''
<g class="layer" style="--k:.6">
  {"".join(f'<path class="flow" d="M240 290 L{x:.0f} {y:.0f}" stroke="{L}" stroke-width="2.5" fill="none"/>' for x, y in _pos)}
</g>
<g class="layer" style="--k:1">
  {"".join(tile(x, y, k, .3 + i*.15) for i, ((x, y), k) in enumerate(zip(_pos, _kinds)))}
</g>
<g class="layer" style="--k:1.3">
  <circle class="pulse" cx="240" cy="290" r="44" fill="none" stroke="{L}" stroke-width="2"/>
  <g class="pop" {d(.1)}><circle cx="240" cy="290" r="44" fill="{B}"/><circle cx="240" cy="290" r="26" fill="none" stroke="{W}" stroke-width="3"/><circle cx="240" cy="290" r="8" fill="{W}"/></g>
</g>''')

# ---------------- Marketing e funis ----------------
MARKETING = frame("Ilustração: funil de vendas recebendo contatos e gerando oportunidades, ao lado de um gráfico em alta", f'''
<g class="layer" style="--k:.6">
  <g class="pop" {d(.2)}><rect x="300" y="60" width="140" height="110" rx="6" fill="{N3}" stroke="rgba(255,255,255,.2)"/>
  {"".join(f'<rect class="grow" {d(.5+i*.15)} x="{318+i*28}" y="{154-h}" width="18" height="{h}" fill="{L}"/>' for i, h in enumerate([26, 40, 56, 76]))}</g>
</g>
<g class="layer" style="--k:1">
  <path d="M60 210 H340 L262 330 V430 H138 V330 Z" fill="{N3}"/>
  <path d="M60 210 H340 L314 250 H86 Z" fill="{S}"/>
  <path d="M98 268 H302 L276 308 H124 Z" fill="{B}"/>
  <path class="draw" pathLength="1" {d(.2)} d="M60 210 H340 L262 330 V430 H138 V330 Z" fill="none" stroke="{L}" stroke-width="3" stroke-linejoin="round"/>
  {"".join(f'<circle class="fall" {d(i*.45)} cx="{x}" cy="150" r="7" fill="{W}"/>' for i, x in enumerate([110, 170, 230, 290, 140, 260]))}
</g>
<g class="layer" style="--k:1.4">
  {"".join(f'<g class="pop" {d(1.2+i*.25)}><circle cx="{x}" cy="486" r="18" fill="{W}"/><path d="M{x-8} 486 L{x-2} 492 L{x+9} 480" stroke="{S}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>' for i, x in enumerate([160, 200, 240]))}
</g>''')

# ---------------- Governança e segurança ----------------
def lock(cx, cy, s, delay):
    return (f'<g class="pop" {d(delay)}><path d="M{cx-9*s} {cy-6*s} V{cy-14*s} a{9*s} {9*s} 0 0 1 {18*s} 0 V{cy-6*s}" fill="none" stroke="{L}" stroke-width="{3*s}"/>'
            f'<rect x="{cx-14*s}" y="{cy-6*s}" width="{28*s}" height="{22*s}" rx="{3*s}" fill="{L}"/></g>')

GOVERNANCA = frame("Ilustração: escudo com sinal de aprovação, cadeados e dados protegidos", f'''
<g class="layer" style="--k:.5">
  <circle class="spin" cx="240" cy="270" r="190" fill="none" stroke="{L}" stroke-opacity=".35" stroke-width="2" stroke-dasharray="3 14"/>
  {"".join(f'<rect class="pop" {d(.2+((i*7)%10)*.08)} x="{330+(i%4)*22}" y="{60+(i//4)*22}" width="14" height="14" rx="2" fill="{L if i in (1,4,6,9,11) else "rgba(255,255,255,.18)"}"/>' for i in range(12))}
</g>
<g class="layer" style="--k:1">
  <path d="M240 110 L360 158 V270 C360 360 300 420 240 452 C180 420 120 360 120 270 V158 Z" fill="{N3}"/>
  <path class="draw" pathLength="1" {d(.1)} d="M240 110 L360 158 V270 C360 360 300 420 240 452 C180 420 120 360 120 270 V158 Z" fill="none" stroke="{L}" stroke-width="4" stroke-linejoin="round"/>
  <path class="draw" pathLength="1" {d(1.0)} d="M188 280 L228 320 L296 238" fill="none" stroke="{W}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
</g>
<g class="layer" style="--k:1.5">
  {lock(80, 470, 1.2, 1.3)}{lock(400, 470, 1.2, 1.5)}{lock(76, 120, .9, 1.7)}
</g>''')

# ---------------- Consultoria de RH: organograma ----------------
def link(x1, y1, x2, y2, delay):
    my = (y1 + y2) / 2
    return f'<path class="draw" pathLength="1" {d(delay)} d="M{x1} {y1} V{my} H{x2} V{y2}" fill="none" stroke="rgba(255,255,255,.4)" stroke-width="2.5"/>'

RH = frame("Ilustração: organograma de pessoas ligado a uma liderança central, com uma balança que representa imparcialidade", f'''
<g class="layer" style="--k:.5">
  {link(240, 178, 120, 268, .5)}{link(240, 178, 240, 268, .55)}{link(240, 178, 360, 268, .6)}
  {link(120, 330, 80, 410, 1.0)}{link(120, 330, 160, 410, 1.05)}{link(240, 330, 220, 410, 1.1)}{link(240, 330, 290, 410, 1.15)}{link(360, 330, 360, 410, 1.2)}{link(360, 330, 420, 410, 1.25)}
</g>
<g class="layer" style="--k:1">
  {person(120, 278, 1.0, M, delay=.7)}{person(240, 278, 1.0, M, delay=.8)}{person(360, 278, 1.0, M, delay=.9)}
  {"".join(person(x, 420, .8, "#6F8DB8", delay=1.3 + i*.08) for i, x in enumerate([80, 160, 220, 290, 360, 420]))}
</g>
<g class="layer" style="--k:1.4">
  <circle class="pulse" cx="240" cy="132" r="40" fill="none" stroke="{L}" stroke-width="2"/>
  <g class="pop" {d(.1)}><circle cx="240" cy="132" r="40" fill="{B}"/></g>
  {person(240, 116, 1.05, W, delay=.2)}
  <g class="pop" {d(1.7)}>
    <line x1="392" y1="74" x2="392" y2="122" stroke="{L}" stroke-width="3"/><line x1="362" y1="84" x2="422" y2="84" stroke="{L}" stroke-width="3"/>
    <path d="M362 84 L350 108 H374 Z" fill="none" stroke="{L}" stroke-width="2.5" stroke-linejoin="round"/><path d="M422 84 L410 108 H434 Z" fill="none" stroke="{L}" stroke-width="2.5" stroke-linejoin="round"/>
    <line x1="380" y1="122" x2="404" y2="122" stroke="{L}" stroke-width="3"/></g>
</g>''')

SERVICE_ILLOS = {
  "estrategia-de-ia": ESTRATEGIA, "automacao-de-processos": AUTOMACAO, "agentes-de-ia": AGENTES,
  "integracoes": INTEGRACOES, "marketing-e-funis": MARKETING, "governanca-de-ia": GOVERNANCA, "consultoria-de-rh": RH,
}

# ---------------- Página inicial: pessoas, gestão e tecnologia (faixa larga, fundo claro) ----------------
def hperson(x, y, s, c, delay):
    return person(x, y, s, c, delay=delay)

HOME_WIDE = f'''<svg class="illo illo-wide" viewBox="0 0 1400 520" role="img" aria-label="Ilustração: pessoas reunidas em torno de uma mesa, um painel de gestão com indicadores em alta e uma rede de tecnologia conectada">
<rect x="0" y="0" width="1400" height="520" fill="#EEF2F7"/>
<g stroke="rgba(10,35,66,.05)">{"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="520"/>' for x in range(50, 1400, 50))}{"".join(f'<line x1="0" y1="{y}" x2="1400" y2="{y}"/>' for y in range(50, 520, 50))}</g>
<g class="layer" style="--k:.8">
  {hperson(170, 250, 1.5, N1, .1)}{hperson(290, 222, 1.5, S, .25)}{hperson(410, 250, 1.5, "#6F8DB8", .4)}
  <g class="pop" {d(.5)}><rect x="110" y="330" width="360" height="18" rx="4" fill="{N1}"/><rect x="140" y="348" width="10" height="70" fill="{N1}"/><rect x="430" y="348" width="10" height="70" fill="{N1}"/></g>
  <text x="290" y="470" text-anchor="middle" font-size="26" font-weight="600" fill="{N1}" class="pop" {d(.7)}>Pessoas</text>
</g>
<path class="flow-dark" d="M480 270 C530 270 540 250 580 250" stroke="{S}" stroke-width="3" fill="none"/>
<g class="layer" style="--k:1.1">
  <g class="pop" {d(.6)}><rect x="580" y="90" width="300" height="300" rx="10" fill="#FFFFFF" stroke="rgba(10,35,66,.15)"/>
    <rect x="580" y="90" width="300" height="40" rx="10" fill="{N1}"/><rect x="580" y="118" width="300" height="12" fill="{N1}"/>
    <circle cx="604" cy="110" r="6" fill="{L}"/><circle cx="624" cy="110" r="6" fill="rgba(255,255,255,.5)"/><circle cx="644" cy="110" r="6" fill="rgba(255,255,255,.5)"/></g>
  {"".join(f'<rect class="grow" {d(.9+i*.12)} x="{612+i*46}" y="{360-h}" width="30" height="{h}" fill="{S if i==4 else "#C9D5E6"}"/>' for i, h in enumerate([60, 90, 80, 130, 180]))}
  <path class="draw" pathLength="1" {d(1.2)} d="M612 260 L658 236 L704 246 L750 196 L796 150 L846 140" fill="none" stroke="{N1}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="730" y="470" text-anchor="middle" font-size="26" font-weight="600" fill="{N1}" class="pop" {d(.8)}>Gestão</text>
</g>
<path class="flow-dark" d="M880 240 C930 240 940 260 990 260" stroke="{S}" stroke-width="3" fill="none"/>
<g class="layer" style="--k:1.4">
  {"".join(f'<path class="flow-dark" d="M1150 250 L{x} {y}" stroke="#6F8DB8" stroke-width="2.5" fill="none"/>' for x, y in [(1040,150),(1270,130),(1300,300),(1050,360),(1180,400)])}
  {"".join(f'<g class="pop" {d(1.0+i*.12)}><circle cx="{x}" cy="{y}" r="22" fill="#FFFFFF" stroke="{N1}" stroke-width="3"/><circle cx="{x}" cy="{y}" r="7" fill="{S}"/></g>' for i, (x, y) in enumerate([(1040,150),(1270,130),(1300,300),(1050,360),(1180,400)]))}
  <circle class="pulse" cx="1150" cy="250" r="44" fill="none" stroke="{S}" stroke-width="2"/>
  <g class="pop" {d(.9)}><circle cx="1150" cy="250" r="44" fill="{N1}"/>{SPARK(1150, 250, 20, L)}</g>
  <text x="1160" y="470" text-anchor="middle" font-size="26" font-weight="600" fill="{N1}" class="pop" {d(1.0)}>Tecnologia</text>
</g>
</svg>'''
