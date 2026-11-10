# Gráficos de barras horizontais (SVG estático) com dados de fontes oficiais.
# Cores: destaque #2457D6 e contexto #7C8A9E (valores sempre escritos ao lado de cada barra + tabela).

ACCENT = "#2457D6"
CONTEXT = "#7C8A9E"

def fmt(v, suffix):
    s = f"{v:.1f}".replace(".", ",") if isinstance(v, float) else str(v)
    return s + suffix

def bar_chart(cid, title, subtitle, rows, vmax, ticks, suffix, source_html, aria):
    """rows: lista de (rótulo, valor, destaque: bool). Rótulo acima de cada barra, para ler bem no celular."""
    W, PAD_R, ROW, TOP, BAR = 400, 56, 60, 8, 22
    plot_w = W - PAD_R
    H = TOP + ROW * len(rows) + 26
    x = lambda v: plot_w * v / vmax
    def gl(t):
        segs = "".join(f'<line x1="{x(t):.1f}" y1="{TOP + i*ROW + 20}" x2="{x(t):.1f}" y2="{TOP + i*ROW + 22 + BAR + 2}" stroke="#D5DDE8" stroke-width="1"/>' for i in range(len(rows)))
        return segs + f'<text x="{x(t):.1f}" y="{H-6}" text-anchor="{"start" if t == ticks[0] else "middle"}" font-size="12" fill="#4F5D70">{fmt(t, suffix)}</text>'
    grid = "".join(gl(t) for t in ticks)
    bars = ""
    for i, (label, v, hi) in enumerate(rows):
        ty = TOP + i * ROW + 14
        y = ty + 8
        w = max(x(v), 2)
        color = ACCENT if hi else CONTEXT
        r = min(4, w / 2)
        path = (f"M0 {y} H{w - r:.1f} Q{w:.1f} {y} {w:.1f} {y + r} "
                f"V{y + BAR - r} Q{w:.1f} {y + BAR} {w - r:.1f} {y + BAR} H0 Z")
        bars += (f'<g class="bar"><title>{label}: {fmt(v, suffix)}</title>'
                 f'<rect x="0" y="{ty-14}" width="{W}" height="{ROW}" fill="transparent"/>'
                 f'<text x="0" y="{ty}" font-size="15" fill="#16202E">{label}</text>'
                 f'<path class="bar-mark" d="{path}" fill="{color}"/>'
                 f'<text x="{w + 8:.1f}" y="{y + BAR/2 + 5}" font-size="16" font-weight="700" fill="#16202E">{fmt(v, suffix)}</text></g>')
    axis = "".join(f'<line x1="0.75" y1="{TOP + i*ROW + 20}" x2="0.75" y2="{TOP + i*ROW + 24 + BAR}" stroke="#4F5D70" stroke-width="1.5"/>' for i in range(len(rows)))
    table_rows = "".join(f"<tr><th scope=\"row\">{l}</th><td>{fmt(v, suffix)}</td></tr>" for l, v, _ in rows)
    return f'''
<figure class="chart" id="{cid}">
  <figcaption><h3 class="chart-title">{title}</h3><p class="chart-sub">{subtitle}</p></figcaption>
  <svg viewBox="-2 0 {W + 4} {H}" role="img" aria-label="{aria}">{grid}{axis}{bars}</svg>
  <details class="chart-data"><summary>Ver os dados em tabela</summary>
    <table><thead><tr><th scope="col">Categoria</th><th scope="col">Valor</th></tr></thead><tbody>{table_rows}</tbody></table>
  </details>
  <p class="chart-source">{source_html}</p>
</figure>'''

SRC_CETIC = 'Fonte: <a href="https://cetic.br/en/tics/pesquisa/2025/empresas/H9/" target="_blank" rel="noopener">Cetic.br/NIC.br, pesquisa TIC Empresas 2025 (indicador H9)</a>. Empresas com 10 ou mais pessoas ocupadas.'
SRC_IBGE = 'Fonte: <a href="https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-noticias/noticias/44551-de-2022-a-2024-percentual-de-empresas-industriais-utilizando-inteligencia-artificial-subiu-de-16-9-para-41-9" target="_blank" rel="noopener">IBGE, Pintec Semestral 2024</a>. Indústrias extrativas e de transformação com 100 ou mais pessoas ocupadas.'
SRC_NBER = 'Fonte: <a href="https://www.nber.org/papers/w31161" target="_blank" rel="noopener">Brynjolfsson, Li e Raymond, "Generative AI at Work", NBER (2023); The Quarterly Journal of Economics (2025)</a>. Estudo com 5.179 atendentes; produtividade medida em atendimentos resolvidos por hora.'
SRC_BCB = 'Fonte: <a href="https://www.bcb.gov.br/" target="_blank" rel="noopener">Banco Central do Brasil, comunicado da 282ª reunião do Copom (04/11/2026)</a>.'
SRC_MCK = 'Fonte: <a href="https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai" target="_blank" rel="noopener">McKinsey, The state of AI in 2026 (agosto de 2026)</a>.'

CHART_PORTE = bar_chart(
    "grafico-porte", "Pequenas empresas ainda usam pouca IA",
    "Empresas que usaram inteligência artificial em 2025, por porte (% do total; porte pelo número de pessoas ocupadas)",
    [("Pequenas (10 a 49 pessoas)", 15, True), ("Médias (50 a 249 pessoas)", 32, True), ("Grandes (250 pessoas ou mais)", 50, False)],
    60, [0, 20, 40, 60], "%", SRC_CETIC,
    "Gráfico de barras: em 2025, 15% das pequenas empresas, 32% das médias e 50% das grandes usaram inteligência artificial.")

CHART_INDUSTRIA = bar_chart(
    "grafico-industria", "Na indústria, o uso de IA mais que dobrou em dois anos",
    "Empresas industriais que utilizam inteligência artificial (% do total)",
    [("2022", 16.9, False), ("2024", 41.9, True)],
    50, [0, 10, 20, 30, 40, 50], "%", SRC_IBGE,
    "Gráfico de barras: 16,9% das empresas industriais usavam inteligência artificial em 2022 e 41,9% em 2024.")

CHART_PRODUTIVIDADE = bar_chart(
    "grafico-produtividade", "IA no atendimento: mais atendimentos resolvidos por hora",
    "Aumento de produtividade de atendentes com acesso a um assistente de IA generativa (%)",
    [("Média de todos", 14, False), ("Atendentes iniciantes", 34, True)],
    40, [0, 10, 20, 30, 40], "%", SRC_NBER,
    "Gráfico de barras: com um assistente de IA, a produtividade dos atendentes aumentou 14% em média e 34% entre os iniciantes.")

def stat(value, text, source_html):
    return f'''
        <article class="stat"><p class="stat-value">{value}</p><p class="stat-text">{text}</p><p class="stat-source">{source_html}</p></article>'''

STATS = "".join([
  stat("90,3%", "das indústrias que adotaram tecnologias digitais avançadas apontam aumento da eficiência como benefício.",
       '<a href="https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-noticias/noticias/44551-de-2022-a-2024-percentual-de-empresas-industriais-utilizando-inteligencia-artificial-subiu-de-16-9-para-41-9" target="_blank" rel="noopener">IBGE, Pintec Semestral 2024</a>'),
  stat("+14%", "de produtividade no atendimento com um assistente de IA, chegando a +34% entre os atendentes iniciantes.",
       '<a href="https://www.nber.org/papers/w31161" target="_blank" rel="noopener">NBER e Quarterly Journal of Economics</a>'),
  stat("15%", "das pequenas empresas brasileiras usaram IA em 2025, contra 50% das grandes.",
       '<a href="https://cetic.br/en/tics/pesquisa/2025/empresas/H9/" target="_blank" rel="noopener">Cetic.br, TIC Empresas 2025</a>'),
  stat("78,6%", "das indústrias que usam essas tecnologias citam o custo alto das soluções como dificuldade.",
       '<a href="https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-noticias/noticias/44551-de-2022-a-2024-percentual-de-empresas-industriais-utilizando-inteligencia-artificial-subiu-de-16-9-para-41-9" target="_blank" rel="noopener">IBGE, Pintec Semestral 2024</a>'),
])
