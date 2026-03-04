import streamlit as st # Biblioteca principal para criação do dashboard web interativo.
import pandas as pd # Biblioteca para manipulação e análise dos dados em formato tabular (DataFrames).

# --------------------------------------------------------------------------------
# 1. CONFIGURAÇÃO DA PÁGINA
# --------------------------------------------------------------------------------

# set_page_config - Define o título da aba do navegador e expande o layout para aproveitar toda a tela.
st.set_page_config(page_title="Dashboard IA 2030", layout="wide", initial_sidebar_state="expanded") 

# --------------------------------------------------------------------------------
# 2. INJEÇÃO DE CSS
# --------------------------------------------------------------------------------
# O st.markdown com unsafe_allow_html=True permite contornar o estilo padrão do Streamlit e injetar CSS customizado.
st.markdown("""
    <style>
    /* Fundo da aplicação em Azul-petróleo escuro (#0A1428) e texto base em branco para contraste */
    .stApp {
        background-color: #0A1428;
        color: #FFFFFF;
        font-family: 'Segoe UI', Calibri, sans-serif; 
    }
    
    /* Estiliza os títulos com a cor de destaque Cyan (#00FFFF) e fonte em negrito */
    h1, h2, h3 {
        color: #00FFFF !important;
        font-family: 'Calibri', sans-serif;
        font-weight: bold;
    }
    
    /* Escurece a barra lateral e adiciona uma borda Magenta (#FF00FF) para separação visual */
    [data-testid="stSidebar"] {
        background-color: #0D0D0D;
        border-right: 2px solid #FF00FF;
    }
    
    /* 'cyber-card': Classe customizada para os blocos de informação simulando caixas com bordas coloridas */
    .cyber-card {
        background-color: #10203A; /* Fundo ligeiramente mais claro para destacar da página */
        padding: 20px;
        border-radius: 8px;
        border: 1.5px solid #00FFFF; /* Borda Cyan obrigatória do design system */
        margin-bottom: 15px; /* Espaçamento entre os cards */
        box-shadow: 0 0 10px rgba(0, 255, 255, 0.2); /* Efeito sutil de brilho neon */
    }
    
    /* 'cyber-source': Fonte monoespaçada de código (Courier New) em verde neon para referências bibliográficas */
    .cyber-source {
        font-family: 'Courier New', Courier, monospace;
        color: #00FF88;
        font-size: 0.9em;
        margin-top: 10px;
    }/* 1. Cor do título do seletor ("Selecione a dimensão...") */
    div[data-testid="stRadio"] > label, div[data-testid="stSelectbox"] > label {
        color: #00FFFF !important; /* Ciano brilhante */
        font-size: 18px !important;
        font-weight: bold !important;
    }
    
    /* 2. Cor do texto das opções ("Todas", "Habilidades", etc.) */
    div[role="radiogroup"] label, div[data-baseweb="select"] {
        color: #FFFFFF !important; /* Branco puro para contraste máximo */
        font-size: 16px !important;
    }

    /* 3. Cor da bolinha de seleção quando ativada (Opcional, mas fica legal) */
    div[data-testid="stRadio"] span[data-baseweb="radio"] div:first-child {
        background-color: #FF00FF !important; /* Magenta */
    }
    </style>
""", unsafe_allow_html=True)

# --------------------------------------------------------------------------------
# 3. CARREGAMENTO E TRATAMENTO DOS DADOS (ETL Básico)
# --------------------------------------------------------------------------------
# O decorador @st.cache_data armazena o dataframe em cache na memória. Isso evita que o Python precise ler o arquivo .csv do disco a cada clique do usuário nos filtros, otimizando a performance.
@st.cache_data
def load_data():
    # Carrega os dados coletados na Fase 1
    df = pd.read_csv("dados_fase1.csv")
    
    # Tratamento de integridade dos dados
    df = df.dropna(how='all')
    df = df.dropna(subset=['Categoria'])
    return df.fillna("")

# Bloco try-except de segurança: Impede que o sistema quebre exibindo erros do Python na tela do usuário.
try:
    df = load_data()
except FileNotFoundError:
    st.error("⚠️ Arquivo 'dados_fase1.csv' não encontrado! Verifique se ele está no mesmo diretório do app.py.")
    st.stop() # Interrompe a execução da interface de forma controlada.
except pd.errors.ParserError:
    st.error("⚠️ Erro de parsing. Verifique se o CSV está salvo com formatação UTF-8 e delimitadores corretos.")
    st.stop()

# --------------------------------------------------------------------------------
# 4. CONSTRUÇÃO DA INTERFACE DO DASHBOARD
# --------------------------------------------------------------------------------
# Cabeçalho principal
st.title("🌐 Futuro do Mercado de Trabalho com IA")
st.markdown("### Análise Multidimensional (2022 - 2030)")
st.markdown("---") # Desenha uma linha separadora

# -- Sidebar (Barra Lateral de Filtros) --
st.sidebar.title("Filtros de Análise")
st.sidebar.markdown("Selecione a dimensão de dados que deseja explorar:")

# Extrai dinamicamente as categorias únicas da planilha e adiciona a opção "Todas" no início da lista.
categorias = ["Todas"] + list(df['Categoria'].unique())

# Renderiza os botões de rádio para o usuário selecionar o filtro desejado.
filtro_categoria = st.sidebar.radio("Categoria de Dados:", categorias)

# -- Motor de Filtragem --
# Aplica a máscara booleana do Pandas para filtrar o DataFrame apenas com a categoria selecionada.
if filtro_categoria != "Todas":
    df_filtrado = df[df['Categoria'] == filtro_categoria]
else:
    df_filtrado = df

# Feedback visual para confirmar qual filtro está ativo (usando a cor Magenta).
st.markdown(f"Exibindo resultados para: **<span style='color:#FF00FF'>{filtro_categoria}</span>**", unsafe_allow_html=True)

# --------------------------------------------------------------------------------
# 5. RENDERIZAÇÃO DOS CARDS DE DADOS
# --------------------------------------------------------------------------------
# Itera sobre cada linha do DataFrame filtrado para gerar os cards dinamicamente na tela.
for index, row in df_filtrado.iterrows():
    # Utiliza HTML injetado para formatar cada componente da pesquisa (Categoria, Dado, Contexto, Fonte e Ano).
    st.markdown(f"""
    <div class="cyber-card">
        <h4 style="color: #FFD700; margin-bottom: 5px;">{row['Categoria']}</h4>
        <p style="font-size: 1.1em; margin-bottom: 10px;">{row['Informação / Dado Extraído']}</p>
        <p style="color: #AAAAAA; font-style: italic;">Contexto: {row['Contexto / Dado Temporal']}</p>
        <div class="cyber-source">▶ FONTE: {row['Fonte']}, {row['Ano']}</div>
    </div>
    """, unsafe_allow_html=True)

# Rodapé estético da barra lateral para manter a imersão visual da apresentação.
st.sidebar.markdown("---")
st.sidebar.markdown("<div style='text-align: center; font-family: Courier New; color: #00FF88;'>STATUS: ONLINE<br>SISTEMA: ATIVO</div>", unsafe_allow_html=True)