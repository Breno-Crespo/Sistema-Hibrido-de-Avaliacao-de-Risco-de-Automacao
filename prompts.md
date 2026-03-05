# Documentação de Engenharia de Prompts (Fase 3)
**Autor:** Breno Crespo

## Prompt #01 — Matriz de Risco e Análise de Tarefas
**Técnica:** Chain-of-Thought (CoT)
**LLM Utilizado:** Gemini 1.5 Pro
**Objetivo:** Analisar o risco de automação de ocupações no nível operacional, exigindo raciocínio passo a passo.

**Prompt:**
"Atue como um especialista em economia do trabalho do WEF. Analise a profissão de Analista de Suporte de TI. 
Passo 1: Liste as 5 tarefas principais do dia a dia desta profissão. 
Passo 2: Para cada tarefa, avalie o risco de automação por IA (0 a 10) e justifique brevemente. 
Passo 3: Calcule a média do risco e classifique a profissão geral como Baixo, Médio ou Alto risco. 
Passo 4: Sugira 2 áreas de upskilling para este profissional."

**Resposta Gerada (resumo):**
"Passo 1: 1. Redefinição de senhas. 2. Instalação de software. 3. Diagnóstico de rede. 4. Atendimento humano a utilizadores em pânico. 5. Manutenção de servidores.
Passo 2: Redefinição de senhas (Risco 10/10 - totalmente automatizável por chatbots)... Atendimento humano (Risco 2/10 - exige empatia).
Passo 3: Risco Médio (6/10).
Passo 4: Upskilling recomendado: Gestão de Cloud Computing e Cibersegurança."

**Análise do Resultado:**
O prompt foi eficaz para gerar uma análise estruturada. A técnica CoT garantiu que o modelo raciocinou tarefa por tarefa antes de concluir o risco médio, evitando respostas rasas e criando dados perfeitos para a nossa matriz.

---

## Prompt #02 — Previsão de Ocupações Emergentes
**Técnica:** Few-Shot Learning
**LLM Utilizado:** ChatGPT-4o
**Objetivo:** Gerar novas profissões baseadas em IA para o setor agrícola brasileiro (visando o nível estratégico).

**Prompt:**
"Vou fornecer exemplos do formato de resposta esperado. Com base no formato, gere 3 novas ocupações para o setor de Agronegócio no Brasil até 2030:
Exemplo 1: Prompt Engineer -> Salário Estimado: R$ 15K. Skills: Python, NLP, Pensamento Crítico.
Exemplo 2: Auditor de Viés de IA -> Salário Estimado: R$ 18K. Skills: Ética de Dados, Estatística, Direito Digital.
Agora é a sua vez. Gere 3 ocupações para o Agronegócio brasileiro."

**Resposta Gerada (resumo):**
"1. Otimizador de Colheita Algorítmica -> Salário Estimado: R$ 14K. Skills: IoT Agrícola, Machine Learning, Meteorologia de Dados.
2. Engenheiro de Prompt para Drones -> Salário Estimado: R$ 12K. Skills: Visão Computacional, Pilotagem de Drones, Automação.
3. Arquiteto de Solo Digital -> Salário Estimado: R$ 20K. Skills: Análise de Dados Geoespaciais, IA Preditiva, Biologia do Solo."

**Análise do Resultado:**
O Few-Shot Learning foi essencial. Ao fornecer os dois exemplos iniciais, o modelo replicou exatamente o padrão de saída (Cargo, Salário, Skills), permitindo extrair dados estruturados rapidamente para a apresentação.

---

## Prompt #03 — Plano de Transformação Corporativa
**Técnica:** Role-Playing
**LLM Utilizado:** Claude 3.5 Sonnet
**Objetivo:** Elaborar recomendações táticas e estratégicas para empresas, com foco no cenário brasileiro.

**Prompt:**
"Você é o Diretor de RH (CHRO) do Nubank, um banco digital brasileiro com milhares de funcionários. A sua análise mostra que a IA Generativa vai automatizar 40% das tarefas operacionais de atendimento ao cliente em 2 anos. 
Aja como este Diretor e elabore um plano de transição de 3 etapas para requalificar (upskilling) esses atendentes para cargos táticos, evitando demissões em massa."

**Resposta Gerada (resumo):**
"Como CHRO, proponho o 'Plano NuTransition':
1. Mapeamento de Skills: Avaliar os atendentes com maior inteligência emocional e resolução de problemas complexos.
2. Academia de IA: Treinar 30% da base operacional para se tornarem "Curadores de IA", revisando as respostas dadas pelos bots.
3. Transição para Consultoria: Mover os melhores perfis para atendimento Premium hiper-personalizado."

**Análise do Resultado:**
O Role-Playing inserido no contexto de uma empresa real (Nubank) forçou o LLM a abandonar respostas genéricas e gerar recomendações maduras e acionáveis, perfeitamente alinhadas com as exigências do Relatório Executivo.

---

## Prompt #04 — Construção do Motor de Inferência (Código)
**Técnica:** Chain-of-Thought (CoT) + Role-Playing
**LLM Utilizado:** Gemini 1.5 Pro
**Objetivo:** Projetar a arquitetura híbrida entre Redes Neurais e Sistemas Especialistas.

**Prompt:**
"Atue como um Arquiteto de Software Especialista em IA. Quero construir um sistema híbrido em Python.
Passo 1: Explique teoricamente como uma Rede Neural (Keras) pode trabalhar em conjunto com um Sistema Especialista (biblioteca experta).
Passo 2: Escreva o código Python simulando essa orquestração, onde a RNA prevê a probabilidade, mas se o risco estiver na zona de incerteza, o Especialista intervém."

**Resposta Gerada (resumo):**
"Passo 1: A RNA atua como a intuição (detectando padrões matemáticos não lineares). O SE atua como a razão (impondo regras de negócio explícitas). A integração ocorre delegando zonas de incerteza da RNA para as regras simbólicas.
Passo 2: [Código gerado com a função decisao_hibrida e a lógica de threshold]."

**Análise do Resultado:**
O raciocínio passo a passo permitiu não apenas gerar o código funcional para o Colab, mas também compreender a teoria da arquitetura híbrida para defendê-la com segurança perante a banca.

---

## Prompt #05 — Formulação de Recomendações Governamentais
**Técnica:** Role-Playing
**LLM Utilizado:** ChatGPT-4o
**Objetivo:** Gerar insights de políticas públicas de IA para o Governo Brasileiro.

**Prompt:**
"Você é o Ministro de Ciência, Tecnologia e Inovação do Brasil em 2026. Levando em conta os dados da FGV e IBGE sobre desigualdade tecnológica regional, proponha 3 políticas públicas concretas para evitar que a automação por IA cause desemprego estrutural no Norte e Nordeste do país."

**Resposta Gerada (resumo):**
"1. Fundo de Alfabetização Algorítmica Regional: Subsídios fiscais para empresas que ensinem lógica de IA.
2. Hubs Agro-Tech no Norte: Criação de centros de pesquisa focados em usar IA para biotecnologia da Amazônia.
3. Renda Mínima de Transição: Auxílio financeiro temporário atrelado a microcertificações digitais."

**Análise do Resultado:**
A técnica de atribuição de papel garantiu um tom governamental e focado em soluções macroeconômicas nacionais, fornecendo o conteúdo exato para os slides finais da apresentação.

---

## Prompt #06 — O Prompt Dinâmico do Código (Prompt Injection)
**Técnica:** Few-Shot Learning
**LLM Utilizado:** Google Gemini API
**Objetivo:** Gerar justificativas dinâmicas no Sistema Especialista para evitar respostas engessadas.

**Prompt:**
"[CONTEXTO CRÍTICO]: Você é um Auditor de Riscos. Analise o cargo '{job_title}' na indústria '{industry}'.
Exemplo de resposta esperada: 'Como Desenvolvedor Front-end, o risco é médio. IAs geram código básico, mas você deve transitar para Arquitetura de Software.'
Sua tarefa: Explique o risco baseado em '{contexto_regra}'. Máximo de 2 linhas em Português."

**Resposta Gerada (resumo):**
"Como Data Scientist em Tecnologia, o risco é baixo. Ferramentas automatizam a limpeza, mas o desenho estratégico do modelo e o alinhamento de negócio exigem validação humana."

**Análise do Resultado:**
O uso de Few-Shot no prompt injetado no código Python garantiu que a API gerasse textos sempre no mesmo padrão e tamanho, evitando que a interface do Streamlit ficasse deformada.

---

## Prompt #07 — Aconselhamento de Carreira Profissional
**Técnica:** Chain-of-Thought (CoT) + Role-Playing
**LLM Utilizado:** Claude 3.5 Sonnet
**Objetivo:** Obter conselhos táticos para a adaptação profissional até 2030.

**Prompt:**
"Aja como um Mentor Executivo de Carreira. O seu cliente é um Contabilista Pleno de 35 anos muito preocupado com IAs generativas lendo faturas.
Passo 1: Valide a dor dele com dados sobre automação.
Passo 2: Liste 3 ferramentas de IA que ele DEVE aprender para não ser demitido.
Passo 3: Mapeie a transição dele de uma posição 'operacional' para uma 'estratégica'."

**Resposta Gerada (resumo):**
"Passo 1: A McKinsey prevê automação pesada em tarefas contábeis, mas o julgamento não é automatizável.
Passo 2: Aprenda: Advanced Data Analysis, Power BI integrado com IA e OCR cognitivo.
Passo 3: Transição: De Processador de Dados Fiscais para Consultor Financeiro Estratégico."

**Análise do Resultado:**
A união das duas técnicas gerou respostas altamente empáticas e estruturadas, alimentando perfeitamente a seção 'Recomendações para Profissionais' do Relatório Executivo.

---

## Prompt #08 — Geração do Estilo Visual (CSS/Tech Noir)
**Técnica:** Few-Shot Learning
**LLM Utilizado:** ChatGPT-4o
**Objetivo:** Criar a configuração visual do projeto de acordo com as restrições da faculdade.

**Prompt:**
"Eu preciso criar um arquivo config.toml para o meu Streamlit Dashboard seguindo a estética 'Tech Noir'.
Exemplo de cores exigidas:
- Fundo: #0A1428 (Azul-petróleo escuro)
- Destaques: #00FFFF (Cyan) ou #FF00FF (Magenta)
- Texto: #FFFFFF (Branco)
Baseado no exemplo acima, gere o conteúdo exato do config.toml para aplicar esse tema à minha interface."

**Resposta Gerada (resumo):**
"[theme]
base='dark'
primaryColor='#00FFFF'
backgroundColor='#0A1428'
textColor='#FFFFFF'"

**Análise do Resultado:**
Passar os códigos HEX exatos como exemplos (Few-Shot) garantiu que a IA não inventasse cores fora do padrão exigido, resultando em um dashboard 100% alinhado à rubrica visual.

---

## Prompt #09 — Extração de Métricas de Avaliação
**Técnica:** Chain-of-Thought (CoT)
**LLM Utilizado:** Gemini 1.5 Pro
**Objetivo:** Assegurar que as exigências estatísticas da rubrica foram implementadas no código.

**Prompt:**
"Atue como um Engenheiro de Machine Learning.
Passo 1: Escreva o código Python usando 'sklearn' para gerar a Matriz de Confusão e o classification_report da minha Rede Neural.
Passo 2: Adicione o cálculo exato da curva ROC-AUC.
Passo 3: Gere o código matplotlib para salvar o gráfico com as cores do tema 'Tech Noir'."

**Resposta Gerada (resumo):**
"Passo 1: [Código com accuracy_score implementado].
Passo 2: roc_auc = roc_auc_score(y_test, y_pred_probs).
Passo 3: [Código sns.heatmap configurado com plt.rcParams escuro e cor '#00FFFF']."

**Análise do Resultado:**
Este prompt garantiu a criação técnica das métricas avançadas (como ROC-AUC e F1-Score), fundamentais para alcançar a pontuação máxima de avaliação técnica do modelo.

---

## Prompt #10 — Resumo Estruturado de Relatórios Longos
**Técnica:** Few-Shot Learning
**LLM Utilizado:** Claude 3.5 Sonnet
**Objetivo:** Sintetizar relatórios do WEF e McKinsey (Fontes Primárias).

**Prompt:**
"Dada uma extração do relatório da McKinsey, condense os achados no seguinte formato de tópicos rápidos para um slide de PowerPoint:
Exemplo:
- Dado Chave: 50% das tarefas operacionais.
- Setor Atingido: Manufatura.
- Ano Base: 2025.
Agora, faça o mesmo para o texto abaixo sobre o impacto de 13 Trilhões de Dólares da IA."

**Resposta Gerada (resumo):**
"- Dado Chave: Acréscimo de US$ 13 Trilhões no PIB Global.
- Setor Atingido: Logística, Varejo e Serviços Financeiros.
- Ano Base: Projeção para 2030 (McKinsey Global Institute)."

**Análise do Resultado:**
A técnica garantiu o cumprimento da regra de 'máximo de 5 itens por slide', formatando os dados perfeitamente e evitando blocos densos de texto na apresentação final.