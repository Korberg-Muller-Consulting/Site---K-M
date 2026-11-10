# Artigos da seção Insights. Corpo em HTML; textos originais da Korberg & Müller.
from charts import CHART_PORTE, CHART_INDUSTRIA, CHART_PRODUTIVIDADE, SRC_BCB, SRC_MCK

ARTICLES = [
 {
  "slug": "rewired-mckinsey-pequenas-e-medias-empresas",
  "date": "2026-11-10",
  "date_br": "10 de novembro de 2026",
  "read": "7 min de leitura",
  "title": "O que pequenas e médias empresas podem aprender com o Rewired, da McKinsey | Korberg &amp; Müller",
  "h1": "O que pequenas e médias empresas podem aprender com o Rewired, da McKinsey",
  "desc": "As principais lições do livro Rewired, da McKinsey, sobre transformação digital e IA, traduzidas para a realidade de pequenas e médias empresas.",
  "lede": "O livro em que a McKinsey reúne o seu método de transformação digital e IA foi escrito para grandes empresas. As lições centrais, porém, valem para qualquer porte, desde que sejam traduzidas para a escala de uma pequena ou média empresa.",
  "card": "As lições centrais do livro sobre transformação digital e IA, adaptadas para quem não tem a estrutura nem o orçamento de uma grande empresa.",
  "body": """
<p><em>Rewired</em> foi publicado em 2023 por três sócios da McKinsey, Eric Lamarre, Kate Smaje e Rodney Zemmel. É o manual que a consultoria usa para conduzir transformações digitais e de inteligência artificial em grandes organizações: como escolher onde começar, como montar as equipes, como organizar a tecnologia e os dados e, principalmente, como fazer as soluções serem de fato usadas.</p>
<p>O ponto de partida do livro é uma constatação conhecida: muitas empresas investem em transformação digital e colhem pouco resultado. A explicação dos autores é que não existe atalho. O que diferencia quem tem sucesso é um conjunto de capacidades construídas com método e mantidas ao longo do tempo.</p>
<p>A seguir, as lições que consideramos mais úteis para pequenas e médias empresas, e o que muda quando aplicamos cada uma delas a uma empresa com dezenas, e não milhares, de funcionários.</p>

<h2>1. Comece por poucas áreas, bem escolhidas</h2>
<p>O livro descreve dois erros opostos. O primeiro é começar pequeno demais, com testes isolados que não mudam nada de relevante. O segundo é tentar transformar a empresa inteira de uma vez, o que gera custo alto, confusão e pouca entrega. A recomendação é escolher alguns domínios do negócio, bem delimitados, e transformá-los por completo.</p>
<p><strong>Na pequena e média empresa:</strong> o equivalente é escolher uma ou duas áreas por vez, como atendimento, comercial ou financeiro. Para decidir qual, use dois filtros que o próprio livro propõe:</p>
<ul>
  <li><strong>Valor:</strong> qual é o impacto para o cliente, o ganho financeiro e a rapidez com que o retorno aparece.</li>
  <li><strong>Viabilidade:</strong> se há apoio dos sócios, se os dados necessários existem e se a equipe vai conseguir adotar a mudança.</li>
</ul>
<p>Uma área que pontua bem nos dois critérios é o melhor ponto de partida. O resultado obtido nela financia e dá confiança para a próxima.</p>

<h2>2. Transformação é sobre pessoas antes de ser sobre tecnologia</h2>
<p>Uma parte inteira do livro trata de talento. A mensagem é que a transformação depende de pessoas que entendem o negócio trabalhando junto com quem domina a tecnologia, e que montar essa equipe é justamente o que leva mais tempo. Os autores recomendam avaliar as competências reais das pessoas, e não apenas os cargos que elas ocupam, e decidir com clareza o que deve ficar dentro da empresa e o que pode ser buscado fora.</p>
<p><strong>Na pequena e média empresa:</strong> ninguém vai montar um departamento de tecnologia com dezenas de pessoas. A pergunta passa a ser outra: quem, na equipe atual, tem interesse e capacidade para assumir as novas ferramentas, o que precisa de treinamento e o que faz mais sentido contratar como serviço. Esse mapeamento é trabalho de gestão de pessoas tanto quanto de tecnologia, e é por isso que tratamos os dois temas juntos.</p>

<h2>3. Adoção vale tanto quanto o desenvolvimento</h2>
<p>Esta talvez seja a lição mais importante do livro. Construir a solução é só o começo: o desafio de verdade é fazer as pessoas usarem e espalhar o benefício pela empresa. Os autores defendem que, para cada real investido em desenvolver uma solução, seja investido o mesmo ou mais em adoção, com treinamento, mudança de processos e acompanhamento.</p>
<p>O livro também nomeia um problema comum: projetos que funcionam bem no teste, mas nunca chegam à operação. É o que chamam de purgatório do piloto.</p>
<p><strong>Na pequena e média empresa:</strong> o risco é ainda maior, porque a rotina engole qualquer novidade que não esteja bem encaixada no dia a dia. Uma automação ou um agente de IA só entrega resultado quando a equipe confia nele e sabe o que fazer quando algo foge do padrão. Por isso, o projeto só termina quando a solução está na rotina, e não quando ela está pronta.</p>

<h2>4. Meça o que importa e revise com frequência</h2>
<p>Os autores insistem em ligar cada iniciativa a metas claras e acompanhar os resultados em revisões periódicas, para ajustar o rumo antes que o investimento se perca.</p>
<p><strong>Na pequena e média empresa:</strong> bastam poucos indicadores, definidos antes de começar, como horas economizadas, tempo de resposta ao cliente ou taxa de conversão de vendas, e uma conversa trimestral entre os sócios para avaliar o que avançou e decidir o próximo passo.</p>

<h2>5. Segurança e confiança desde o início</h2>
<p>O livro trata segurança da informação, privacidade de dados e ética no uso de IA como parte do processo de desenvolvimento, e não como uma verificação feita no final.</p>
<p><strong>Na pequena e média empresa:</strong> isso significa pensar na LGPD, nos acessos e nos dados dos clientes no momento em que a solução é desenhada. Corrigir depois custa mais caro e pode custar a confiança do cliente.</p>

<h2>6. É uma jornada, não um projeto com data para acabar</h2>
<p>Os autores lembram que a transformação digital não tem linha de chegada: é uma capacidade que a empresa desenvolve e aprimora continuamente.</p>
<p><strong>Na pequena e média empresa:</strong> a boa notícia é que a escala menor permite aprender mais rápido. Cada área transformada deixa a equipe mais preparada para a seguinte.</p>

<h2>O que não vale copiar das grandes empresas</h2>
<p>Parte do livro trata de estruturas pensadas para organizações com centenas de profissionais de tecnologia, como dezenas de equipes ágeis trabalhando em paralelo, plataformas internas de desenvolvimento e grandes migrações para a nuvem. Para uma pequena ou média empresa, copiar essas estruturas gera custo sem retorno. O que se aproveita é a lógica por trás delas: foco, pessoas preparadas, adoção cuidadosa e resultados medidos.</p>

<h2>Como aplicamos essas lições</h2>
<p>Na Korberg &amp; Müller, nosso trabalho é justamente essa tradução: levar os métodos que as grandes consultorias aplicam em grandes empresas para a realidade de pequenas e médias empresas de Porto Alegre e região. Começamos por um diagnóstico presencial, escolhemos uma ou duas áreas com critério, cuidamos das pessoas junto com a tecnologia e só consideramos o projeto concluído quando a solução faz parte da rotina.</p>

<aside class="source">
  <p><strong>Referência:</strong> LAMARRE, Eric; SMAJE, Kate; ZEMMEL, Rodney. <em>Rewired: The McKinsey Guide to Outcompeting in the Age of Digital and AI</em>. Hoboken: Wiley, 2023. Veja também a <a href="https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/what-really-works-when-it-comes-to-digital-and-ai-transformations" target="_blank" rel="noopener">entrevista dos autores no site da McKinsey</a>. Este artigo apresenta uma leitura independente da Korberg &amp; Müller, sem vínculo com a McKinsey &amp; Company.</p>
</aside>
""",
  "related": ["estrategia-de-ia", "automacao-de-processos", "consultoria-de-rh"],
 },
 {
  "slug": "ia-reduzir-custos-eficiencia-dados",
  "date": "2026-11-10",
  "date_br": "10 de novembro de 2026",
  "read": "6 min de leitura",
  "title": "IA para reduzir custos e ganhar eficiência: o que dizem os dados | Korberg &amp; Müller",
  "h1": "IA para reduzir custos e ganhar eficiência: o que dizem os dados",
  "desc": "Dados do IBGE, do Cetic.br, do Banco Central e de estudos acadêmicos sobre eficiência, produtividade e uso de IA nas empresas brasileiras, e como transformar isso em redução de custos.",
  "lede": "Com juros altos e a atividade econômica perdendo fôlego, cada real gasto na operação pesa mais. Reunimos os dados de fontes oficiais sobre o que a inteligência artificial já entrega em eficiência, e sobre onde as pequenas e médias empresas estão nessa corrida.",
  "card": "Dados do IBGE, do Cetic.br, do Banco Central e de pesquisas acadêmicas sobre eficiência, produtividade e o uso de IA nas empresas brasileiras.",
  "body": """
<h2>O cenário: crédito caro e economia desacelerando</h2>
<p>Em 4 de novembro de 2026, o Banco Central manteve a taxa Selic em 13,75% ao ano. A taxa havia ficado em 15% de junho de 2025 a março de 2026, o nível mais alto em quase duas décadas. No comunicado, o Copom citou uma desaceleração mais acentuada da atividade econômica doméstica entre os fatores de risco.</p>
<p>Para uma pequena ou média empresa, isso significa capital de giro caro e clientes mais cautelosos. Nesse ambiente, reduzir custos sem cortar a capacidade de atender e de vender passa a ser questão de sobrevivência.</p>
<p class="chart-source">""" + SRC_BCB + """</p>

<h2>Eficiência é o principal ganho relatado pelas empresas</h2>
<p>A pesquisa de inovação do IBGE acompanha mais de 10 mil indústrias com 100 ou mais pessoas ocupadas. Entre as que adotaram tecnologias digitais avançadas, como inteligência artificial, computação em nuvem e automação, 97,9% relataram algum benefício. O mais citado foi o aumento da eficiência, apontado por 90,3% delas, seguido de mais flexibilidade nos processos administrativos, produtivos e organizacionais (89,5%).</p>
""" + CHART_INDUSTRIA + """
<p>O mesmo levantamento mostra o principal freio: 78,6% das indústrias que já usam essas tecnologias citaram o custo alto das soluções como dificuldade. Ou seja, o retorno existe, mas depende de escolher bem onde investir.</p>

<h2>Produtividade medida, e não estimada</h2>
<p>Um dos estudos mais citados sobre o tema acompanhou 5.179 atendentes de suporte ao cliente antes e depois de receberem um assistente de IA generativa. A produtividade, medida em atendimentos resolvidos por hora, subiu 14% em média. Entre os atendentes iniciantes, o ganho foi de 34%: a ferramenta espalhou as boas práticas dos mais experientes. O estudo também registrou clientes mais satisfeitos e menor rotatividade da equipe.</p>
""" + CHART_PRODUTIVIDADE + """
<p>Na pesquisa global da McKinsey publicada em agosto de 2026, cerca de 80% das empresas dizem buscar ganhos de eficiência com IA, e as reduções de custo são mais relatadas em cadeia de suprimentos, operações de atendimento e produção. A mesma pesquisa traz um alerta: só 37% dos entrevistados veem impacto positivo no resultado da empresa como um todo. A diferença está em como a IA é implantada, e não apenas em usá-la.</p>
<p class="chart-source">""" + SRC_MCK + """</p>

<h2>As pequenas empresas ainda estão no começo</h2>
<p>Segundo a pesquisa TIC Empresas, do Cetic.br, 17% das empresas brasileiras usaram inteligência artificial em 2025, contra 13% em 2024. O avanço foi puxado pelas pequenas, que passaram de 10% para 15%. Ainda assim, a distância para as grandes é grande.</p>
""" + CHART_PORTE + """
<p>Para quem compete com empresas maiores, essa distância é um risco e também uma oportunidade: quem adotar primeiro, com método, ganha eficiência enquanto a maior parte do mercado ainda não começou.</p>

<h2>Como transformar eficiência em redução de custo</h2>
<p>Ganho de eficiência só vira economia quando é medido e aproveitado. Na prática, recomendamos três passos:</p>
<ul>
  <li><strong>Escolha um processo com custo claro,</strong> como atendimento, emissão de documentos ou conciliação financeira, e meça hoje quantas horas por mês ele consome.</li>
  <li><strong>Calcule o custo dessas horas</strong> (salários e encargos das pessoas envolvidas) e compare com o custo da solução, incluindo implantação, ferramentas e treinamento.</li>
  <li><strong>Decida o que fazer com o tempo liberado:</strong> atender mais clientes com a mesma equipe, evitar uma contratação ou realocar pessoas para vendas. Sem essa decisão, a eficiência se dilui na rotina.</li>
</ul>
<p><em>Exemplo ilustrativo, com números hipotéticos:</em> se três pessoas gastam, juntas, 60 horas por mês respondendo às mesmas perguntas de clientes, e cada hora custa R$ 40 para a empresa, esse processo custa R$ 2.400 por mês. Um agente de IA que resolva metade dessas perguntas libera 30 horas, o equivalente a R$ 1.200 por mês, que devem ser comparados com o custo mensal da solução.</p>

<h2>Como trabalhamos esse tema</h2>
<p>Na Korberg &amp; Müller, começamos pelo diagnóstico presencial: medimos o custo atual dos processos, escolhemos uma ou duas áreas com retorno claro e só recomendamos uma solução quando a conta fecha. Depois, acompanhamos os indicadores para mostrar a economia real, e não apenas a estimada.</p>
""",
  "related": ["automacao-de-processos", "agentes-de-ia", "estrategia-de-ia"],
 },
]
