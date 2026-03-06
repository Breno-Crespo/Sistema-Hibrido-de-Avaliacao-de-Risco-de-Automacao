import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import joblib
import qrcode
from io import BytesIO

# --------------------------------------------------------------------------------
# 1. CONFIGURAÇÃO DA PÁGINA E ESTILO TECH NOIR
# --------------------------------------------------------------------------------
st.set_page_config(page_title="IA 2030: Dashboard Híbrido", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    /* Estética de Fundo e Texto */
    .stApp { background-color: #0A1428; color: #FFFFFF; font-family: 'Segoe UI', sans-serif; }
    
    /* Títulos em Cyan Neon */
    h1, h2, h3 { color: #00FFFF !important; font-weight: bold; }
    
    /* Barra Lateral com Borda Magenta */
    [data-testid="stSidebar"] { background-color: #0D0D0D; border-right: 2px solid #FF00FF; }
    
    /* Cards de Dados (Fase 1) */
    .cyber-card {
        background-color: #10203A;
        padding: 20px;
        border-radius: 8px;
        border: 1.5px solid #00FFFF;
        margin-bottom: 15px;
        box-shadow: 0 0 10px rgba(0, 255, 255, 0.2);
    }
    
    /* Estilo de Código e Fontes */
    .cyber-source {
        font-family: 'Courier New', monospace;
        color: #00FF88;
        font-size: 0.9em;
        margin-top: 10px;
    }
    
    /* Widgets e Botões */
    div[data-testid="stRadio"] > label { color: #00FFFF !important; font-weight: bold; }
    .stButton>button {
        background-color: transparent;
        color: #00FFFF;
        border: 2px solid #00FFFF;
        border-radius: 5px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #00FFFF; color: #0A1428; }
    </style>
""", unsafe_allow_html=True)

# --------------------------------------------------------------------------------
# 2. CARREGAMENTO DOS "CÉREBROS" DO PROJETO (CACHE)
# --------------------------------------------------------------------------------

@st.cache_resource
def load_ai_assets():
    """Carrega o modelo Keras, o Scaler e a lista de Features do Colab."""
    try:
        model = tf.keras.models.load_model('modelo_rna_breno.h5')
        scaler = joblib.load('scaler_breno.pkl')
        features = joblib.load('features_breno.pkl')
        return model, scaler, features
    except:
        return None, None, None

@st.cache_data
def load_bibliografia():
    """Carrega os dados da Fase 1."""
    try:
        df = pd.read_csv("dados_fase1.csv")
        return df.dropna(subset=['Categoria']).fillna("")
    except:
        return None

# Instanciando os recursos
model_rna, scaler_rna, features_reais = load_ai_assets()
df_biblio = load_bibliografia()

# --------------------------------------------------------------------------------
# 3. INTERFACE PRINCIPAL (ABAS)
# --------------------------------------------------------------------------------
st.title("🌐 Futuro do Trabalho & IA 2030")
st.markdown("### Orquestração Neuro-Simbólica para Auditoria de Risco")

tab1, tab2 = st.tabs(["🔍 Explorador de Dados (Fase 1)", "🤖 Simulador Híbrido (IA Real)"])

# --- ABA 1: PESQUISA BIBLIOGRÁFICA ---
with tab1:
    st.header("Base de Conhecimento Estratégica")
    if df_biblio is not None:
        st.sidebar.subheader("Filtros do Explorador")
        categorias = ["Todas"] + list(df_biblio['Categoria'].unique())
        filtro = st.sidebar.selectbox("Selecione a Dimensão:", categorias)

        df_disp = df_biblio if filtro == "Todas" else df_biblio[df_biblio['Categoria'] == filtro]

        for _, row in df_disp.iterrows():
            st.markdown(f"""
                <div class="cyber-card">
                    <h4 style="color: #FFD700; margin:0;">{row['Categoria']}</h4>
                    <p style="font-size: 1.1em; margin: 10px 0;">{row['Informação / Dado Extraído']}</p>
                    <p style="color: #AAAAAA; font-style: italic; font-size: 0.9em;">Contexto: {row['Contexto / Dado Temporal']}</p>
                    <div class="cyber-source">▶ FONTE: {row['Fonte']}, {row['Ano']}</div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Arquivo 'dados_fase1.csv' não encontrado. Suba o arquivo para o repositório.")

# --- ABA 2: SIMULADOR DE RISCO COM IA REAL ---
with tab2:
    st.header("Auditoria de Risco Algorítmico")
    
    if model_rna is not None:
        c1, c2 = st.columns([1, 1.2])
        
        with c1:
            st.subheader("Parâmetros do Cargo")
            cargo_nome = st.text_input("Nome da Profissão:", "Analista de Dados")
            
            # Inputs que alimentam as features reais
            exp = st.slider("Anos de Experiência:", 0, 40, 5)
            sal = st.number_input("Salário Anual Estimado (USD):", 15000, 300000, 55000)
            
            # Seletores para One-Hot Encoding
            ind_list = ["Technology", "Healthcare", "Finance", "Education", "Manufacturing"]
            industria = st.selectbox("Indústria/Setor:", ind_list)
            
            if st.button("EXECUTAR PREDICÃO"):
                # PREPARAÇÃO DO VETOR DE ENTRADA (Mapeia para as colunas do One-Hot Encoding)
                input_data = {f: [0] for f in features_reais}
                
                # Preenche valores numéricos
                if 'years_experience' in input_data: input_data['years_experience'] = [exp]
                if 'salary_usd' in input_data: input_data['salary_usd'] = [sal]
                
                # Ativa a categoria correta (One-Hot)
                col_industria = f"industry_{industria}"
                if col_industria in input_data: input_data[col_industria] = [1]
                
                # Processamento e Predição
                df_input = pd.DataFrame(input_data)
                input_scaled = scaler_rna.transform(df_input.values)
                prob = model_rna.predict(input_scaled, verbose=0)[0][0]
                
                with c2:
                    st.subheader("Veredito do Sistema")
                    cor_resultado = "#FF00FF" if prob > 0.5 else "#00FFFF"
                    texto_resultado = "ALTO RISCO" if prob > 0.5 else "BAIXO RISCO"
                    
                    st.markdown(f"""
                        <div style="background-color: {cor_resultado}; color: #000; padding: 30px; border-radius: 10px; text-align: center;">
                            <h1 style="color: #000 !important; margin: 0;">{texto_resultado}</h1>
                            <p style="font-weight: bold; font-size: 1.2em;">Confiança Estatística: {prob:.2%}</p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Lógica do Sistema Especialista (Explicabilidade)
                    st.write("---")
                    if 0.35 < prob < 0.65:
                        st.info(f"🔍 **ZONA DE DÚVIDA:** A Rede Neural sugere auditoria complementar para {cargo_nome} devido à proximidade do limiar crítico.")
                    else:
                        st.success(f"✅ **DECISÃO CONSISTENTE:** O padrão de {industria} para este nível salarial está bem definido na base histórica.")
                    
                    st.progress(prob)
    else:
        st.error("❌ Erro ao carregar modelo. Certifique-se de que 'modelo_rna_breno.h5' e 'scaler_breno.pkl' estão na pasta.")

# --------------------------------------------------------------------------------
# 4. SIDEBAR: QR CODE E STATUS
# --------------------------------------------------------------------------------
st.sidebar.markdown("---")
# Coloque a URL que o Streamlit Cloud gerar aqui:
url_final = "https://dashboard-interativo-trabalho-pos.streamlit.app/" 

# Gerador de QR Code com cores do trabalho
qr = qrcode.QRCode(box_size=10, border=1)
qr.add_data(url_final)
qr.make(fit=True)
img_qr = qr.make_image(fill_color="#00FFFF", back_color="#0A1428")

buf = BytesIO()
img_qr.save(buf, format="PNG")
st.sidebar.image(buf.getvalue(), caption="Acesse a versão Mobile", use_container_width=True)

st.sidebar.markdown("<div style='text-align: center; font-family: Courier New; color: #00FF88;'>STATUS: HÍBRIDO ONLINE<br>MODELO: RNA-MLP v1.0</div>", unsafe_allow_html=True)