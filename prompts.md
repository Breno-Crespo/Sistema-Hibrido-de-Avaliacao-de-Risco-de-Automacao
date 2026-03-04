Documentação de Engenharia de Prompts (Fase 3)
Prompt #01 — Matriz de Risco e Análise de Tarefas
Técnica: Chain-of-Thought (CoT)
LLM Utilizado: Gemini 1.5 Pro
Objetivo: Analisar o risco de automação de ocupações no nível operacional, exigindo raciocínio passo a passo.

Prompt:

Plaintext
Atue como um especialista em economia do trabalho do WEF. Analise a profissão de "Analista de Suporte de TI". 
Passo 1: Liste as 5 tarefas principais do dia a dia desta profissão. 
Passo 2: Para cada tarefa, avalie o risco de automação por IA (0 a 10) e justifique brevemente. 
Passo 3: Calcule a média do risco e classifique a profissão geral como Baixo, Médio ou Alto risco. 
Passo 4: Sugira 2 áreas de upskilling para este profissional.
Resposta Gerada (resumo):

Plaintext
Passo 1: 1. Redefinição de senhas. 2. Instalação de software. 3. Diagnóstico de rede. 4. Atendimento humano a utilizadores em pânico. 5. Manutenção de servidores.
Passo 2: Redefinição de senhas (Risco 10/10 - totalmente automatizável por chatbots)... Atendimento humano (Risco 2/10 - exige empatia).
Passo 3: Risco Médio (6/10).
Passo 4: Upskilling recomendado: Gestão de Cloud Computing e Cibersegurança.
Análise do Resultado:
A técnica CoT foi essencial para evitar que o LLM apenas gerasse um número aleatório. Ao forçar a análise tarefa a tarefa, os insights gerados tornaram-se perfeitos para alimentar a secção "Matriz de Risco" da nossa apresentação.

Prompt #02 — Previsão de Ocupações Emergentes
Técnica: Few-Shot Learning
LLM Utilizado: ChatGPT-4o
Objetivo: Gerar novas profissões baseadas em IA para o setor agrícola brasileiro (visando o nível estratégico).

Prompt:

Plaintext
Vou fornecer exemplos de novas ocupações geradas pela IA. Com base no formato, gere 3 novas ocupações para o setor de Agronegócio no Brasil até 2030:

Exemplo 1: Prompt Engineer -> Salário Estimado: R$ 15K. Skills: Python, NLP, Pensamento Crítico.
Exemplo 2: Auditor de Viés de IA -> Salário Estimado: R$ 18K. Skills: Ética de Dados, Estatística, Direito Digital.

Agora é a sua vez. Gere 3 ocupações para o Agronegócio brasileiro.
Resposta Gerada (resumo):

Plaintext
1. Otimizador de Colheita Algorítmica -> Salário Estimado: R$ 14K. Skills: IoT Agrícola, Machine Learning, Meteorologia de Dados.
2. Engenheiro de Prompt para Drones -> Salário Estimado: R$ 12K. Skills: Visão Computacional, Pilotagem de Drones, Automação.
3. Arquiteto de Solo Digital -> Salário Estimado: R$ 20K. Skills: Análise de Dados Geoespaciais, IA Preditiva, Biologia do Solo.
Análise do Resultado:
O Few-Shot garantiu que a formatação da resposta fosse exatamente a desejada (Cargo, Salário, Skills), permitindo a extração rápida de dados estruturados para usar nos diapositivos de "Visão 2030".

Prompt #03 — Plano de Transformação Corporativa
Técnica: Role-Playing
LLM Utilizado: Claude 3.5 Sonnet
Objetivo: Elaborar recomendações táticas e estratégicas para empresas, com foco no cenário brasileiro.

Prompt:

Plaintext
Você é o Diretor de RH (CHRO) do Nubank, um banco digital brasileiro com milhares de funcionários. A sua análise mostra que a IA Generativa vai automatizar 40% das tarefas operacionais de atendimento ao cliente em 2 anos. 
Aja como este Diretor e elabore um plano de transição de 3 etapas para requalificar (upskilling) esses atendentes para cargos táticos, evitando demissões em massa.
Resposta Gerada (resumo):

Plaintext
Como CHRO, proponho o 'Plano NuTransition':
1. Mapeamento de Skills: Avaliar os atendentes com maior inteligência emocional e resolução de problemas complexos.
2. Academia de IA: Treinar 30% da base operacional para se tornarem "Curadores de IA", revisando as respostas dadas pelos bots.
3. Transição para Consultoria: Mover os melhores perfis para atendimento *Premium* hiper-personalizado, utilizando as ferramentas de IA como copilotos.
Análise do Resultado:
O Role-Playing inserido no contexto de uma empresa brasileira gerou recomendações extremamente maduras e realistas, que serão utilizadas diretamente no Entregável 3 (Relatório Executivo) na secção "Recomendações para Empresas".

Prompt #04 — Construção do Motor de Inferência (Código)
Técnica: Chain-of-Thought (CoT) + Role-Playing
LLM Utilizado: Gemini 1.5 Pro
Objetivo: Projetar a arquitetura híbrida entre Redes Neurais e Sistemas Especialistas.

Prompt:

Plaintext
Atue como um Arquiteto de Software Especialista em IA. Quero construir um sistema híbrido em Python.
Passo 1: Explique teoricamente como uma Rede Neural (Keras) pode trabalhar em conjunto com um Sistema Especialista (biblioteca experta).
Passo 2: Escreva o código Python simulando essa orquestração, onde a RNA prevê a probabilidade, mas se estiver entre 30% e 70%, o Especialista intervém.
Resposta Gerada (resumo):

Plaintext
Passo 1: A RNA atua como a intuição (detetando padrões matemáticos não lineares). O SE atua como a razão (impondo regras de negócio explícitas). A integração ocorre delegando zonas de incerteza da RNA para as regras simbólicas.
Passo 2: [Código gerado com a função decisao_hibrida e o limite de threshold para acionar as @Rules].
Análise do Resultado:
O prompt foi crucial para estruturar o "Entregável 2". O raciocínio passo a passo permitiu não apenas gerar o código, mas também compreender a teoria para a defender durante a apresentação do trabalho.

Prompt #05 — Formulação de Recomendações Governamentais
Técnica: Role-Playing
LLM Utilizado: ChatGPT-4o
Objetivo: Gerar insights de políticas públicas de IA para o Governo Brasileiro.

Prompt:

Plaintext
Você é o Ministro de Ciência, Tecnologia e Inovação do Brasil em 2026. Levando em conta os dados da FGV e IBGE sobre desigualdade tecnológica regional, proponha 3 políticas públicas concretas para evitar que a automação por IA cause desemprego estrutural no Norte e Nordeste do país.
Resposta Gerada (resumo):

Plaintext
1. Fundo de Alfabetização Algorítmica Regional: Subsídios fiscais para empresas que ensinem lógica de IA e uso de LLMs em estados do Nordeste.
2. Hubs Agro-Tech no Norte: Criação de centros de pesquisa focados em usar IA para biotecnologia da Amazónia, criando funções "IA-First" que não existem no Sudeste.
3. Renda Mínima de Transição: Auxílio financeiro temporário atrelado a microcertificações em ferramentas digitais.
Análise do Resultado:
A resposta forneceu o conteúdo perfeito para o slide final de "Recomendações para o Governo". O Role-Playing garantiu um tom governamental e focado em soluções macroeconómicas nacionais.

Prompt #06 — O Prompt Dinâmico do Código (Prompt Injection)
Técnica: Few-Shot Learning (Embutido no Código)
LLM Utilizado: Google Gemini API (em tempo real)
Objetivo: Gerar justificações dinâmicas no Sistema Especialista para evitar respostas genéricas.

Prompt (Usado dentro da classe Python):

Plaintext
[CONTEXTO CRÍTICO]: Você é um Auditor de Riscos. Analise o cargo '{job_title}' na indústria '{industry}'.
Exemplo de resposta esperada: "Como Desenvolvedor Front-end, o risco é médio. IAs geram código básico, mas você deve transitar para Arquitetura de Software."

Sua tarefa: Explique o risco baseado em '{contexto_regra}'. Máximo de 2 linhas em Português.
Resposta Gerada (exemplo para Data Scientist):

Plaintext
"Como Data Scientist em Tecnologia, o risco é baixo. Ferramentas automatizam a limpeza, mas o desenho estratégico do modelo e o alinhamento de negócio exigem validação humana."
Análise do Resultado:
O uso de Few-Shot no prompt do código garantiu que a API do Gemini gerasse textos sempre no mesmo padrão e tamanho, evitando que a interface do Streamlit ficasse deformada com respostas excessivamente longas.

Prompt #07 — Aconselhamento de Carreira Profissional
Técnica: Role-Playing + Chain-of-Thought
LLM Utilizado: Claude 3.5 Sonnet
Objetivo: Obter conselhos táticos para a adaptação profissional até 2030.

Prompt:

Plaintext
Aja como um Mentor Executivo de Carreira. O seu cliente é um Contabilista Pleno de 35 anos muito preocupado com IAs generativas lendo faturas e planilhas.
Passo 1: Valide a dor dele com dados sobre automação.
Passo 2: Liste 3 ferramentas de IA que ele DEVE aprender para não ser demitido.
Passo 3: Mapeie a transição dele de uma posição "operacional" para uma posição "estratégica".
Resposta Gerada (resumo):

Plaintext
Passo 1: Compreendo o medo. A McKinsey prevê automação pesada em tarefas contábeis repetitivas. Mas o julgamento contábil não é automatizável.
Passo 2: Aprenda: ChatGPT Advanced Data Analysis, Power BI integrado com IA e ferramentas de OCR cognitivo.
Passo 3: Transição: De "Processador de Dados Fiscais" para "Consultor Financeiro Estratégico", ajudando empresas a prever fluxo de caixa usando modelos da IA.
Análise do Resultado:
As respostas são altamente empáticas e acionáveis, alimentando perfeitamente a secção "Recomendações para Profissionais" exigida no relatório executivo do Entregável 3.

Prompt #08 — Geração do Estilo Visual (CSS/Tech Noir)
Técnica: Few-Shot Learning
LLM Utilizado: ChatGPT-4o
Objetivo: Criar a configuração visual do projeto de acordo com as restrições da faculdade.

Prompt:

Plaintext
Eu preciso criar um arquivo config.toml para o meu Streamlit Dashboard seguindo a estética "Tech Noir / Cyberpunk" exigida pelo meu professor.
Exemplo de cores exigidas:
- Fundo: #0A1428 (Azul-petróleo escuro)
- Destaques: #00FFFF (Cyan) ou #FF00FF (Magenta)
- Texto: #FFFFFF (Branco)

Baseado no exemplo acima, gere o conteúdo exato do config.toml para aplicar esse tema à minha interface Python.
Resposta Gerada (resumo):

Plaintext
[theme]
base="dark"
primaryColor="#00FFFF"
backgroundColor="#0A1428"
secondaryBackgroundColor="#10203A"
textColor="#FFFFFF"
font="sans serif"
Análise do Resultado:
A técnica Few-Shot passando os códigos HEX exatos exigidos pelo professor na Fase 4 garantiu que a IA não inventasse cores. O resultado foi um dashboard 100% alinhado à rubrica.

Prompt #09 — Extração de Métricas de Avaliação
Técnica: Chain-of-Thought (CoT)
LLM Utilizado: Gemini 1.5 Pro
Objetivo: Assegurar que as exigências do Critério 2 (Acurácia, F1-Score, AUC-ROC) foram implementadas no código.

Prompt:

Plaintext
Atue como um Engenheiro de Machine Learning.
Passo 1: Escreva o código Python usando 'sklearn' para gerar a Matriz de Confusão e o classification_report da minha Rede Neural.
Passo 2: Adicione o cálculo exato da curva ROC-AUC.
Passo 3: Gere o código matplotlib para salvar o gráfico com as cores do tema 'Tech Noir' (fundo escuro e letras Cyan).
Resposta Gerada (resumo):

Plaintext
Passo 1: [Código com accuracy_score e classification_report implementados].
Passo 2: roc_auc = roc_auc_score(y_test, y_pred_probs).
Passo 3: [Código sns.heatmap configurado com plt.rcParams escuro e cor '#00FFFF']
Análise do Resultado:
Este prompt foi fundamental para a "Fase 2" do projeto. Garantiu a criação técnica das métricas avançadas (como ROC-AUC), que dão acesso à pontuação máxima (Excelente) na avaliação do código Colab.

Prompt #10 — Resumo Estruturado de Relatórios Longos
Técnica: Few-Shot Learning
LLM Utilizado: Claude 3.5 Sonnet
Objetivo: Sintetizar relatórios do WEF e McKinsey (Fontes Primárias).

Prompt:

Plaintext
Dada uma extração do relatório da McKinsey sobre automação, condense os achados no seguinte formato de tópicos rápidos para um slide de PowerPoint:
Exemplo:
- **Dado Chave:** 50% das tarefas operacionais.
- **Setor Atingido:** Manufatura.
- **Ano Base:** 2025.

Agora, faça o mesmo para o texto abaixo sobre o impacto de 13 Triliões de Dólares da IA na economia global até 2030.
Resposta Gerada (resumo):

Plaintext
- **Dado Chave:** Acréscimo de US$ 13 Triliões no PIB Global.
- **Setor Atingido:** Logística, Varejo e Serviços Financeiros (Liderança).
- **Ano Base:** Projeção para 2030 (McKinsey Global Institute).
Análise do Resultado:
A técnica garantiu que o modelo não gerasse blocos densos de texto, formatando os dados perfeitamente de acordo com a regra "Não coloque mais de 5 itens de texto por slide"  descrita nos Erros Comuns a Evitar do roteiro.