# 🧠 Sistema Híbrido de Avaliação de Risco de Automação

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange)
![Google Gemini](https://img.shields.io/badge/LLM-Google%20Gemini-success)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)

Este projeto apresenta um **Sistema de Inteligência Artificial Híbrido** desenvolvido para prever e auditar o risco de automação de diversas profissões no mercado de trabalho. A solução combina a capacidade de reconhecimento de padrões não-lineares de uma Rede Neural com a explicabilidade e rigor lógico de um Sistema Especialista suportado por IA Generativa.

---

## 🎯 O Desafio e a Solução

Modelos de *Machine Learning* puros (caixa-preta) muitas vezes carecem de **explicabilidade**, um fator crítico em decisões de alto impacto como a análise de risco de carreiras. 

Para resolver este problema, este projeto implementa uma arquitetura de orquestração inovadora:
1. **IA Conexionista (Rede Neural):** Avalia os dados quantitativos e extrai uma probabilidade puramente matemática.
2. **IA Simbólica (Sistema Especialista):** Atua como um auditor. Se a Rede Neural estiver numa "zona de incerteza" (ex: confiança entre 2% e 98%), o sistema de regras de negócio é acionado.
3. **IA Generativa (LLM):** Injetada no motor de inferência, a API do Google Gemini transforma os factos lógicos em justificações técnicas e legíveis para o utilizador final, garantindo 100% de explicabilidade.



---

## ⚙️ Arquitetura Tecnológica

* **Processamento de Dados:** `pandas`, `numpy`, `scikit-learn` (StandardScaler, One-Hot Encoding).
* **Deep Learning (RNA):** `tensorflow.keras` (Modelo sequencial, Dropout para evitar *overfitting*).
* **Motor de Inferência (Regras):** `experta` (Lógica de primeira ordem, Factos e Regras).
* **LLM / GenAI:** `google-generativeai` (Modelo *gemini-1.5-flash* para geração dinâmica de *prompts*).
* **Interface Gráfica (Dashboard):** `streamlit` (Com injeção de CSS via `config.toml` para o tema *Tech Noir*).
* **Segurança e DevSecOps:** `python-dotenv` (Gestão de variáveis de ambiente).

---

## 🚀 Como Executar o Projeto Localmente


Configurar o Ambiente Virtual (Recomendado)
Bash
python -m venv .venv
# Em Windows:
.venv\Scripts\activate
# Em Linux/Mac:
source .venv/bin/activate

Instalar as Dependências
Bash
pip install -r requirements.txt

Configurar a Chave da API (Segurança)
Na raiz do projeto, crie um ficheiro oculto chamado .env e adicione a sua chave do Google AI Studio:

Snippet de código
GEMINI_API_KEY=sua_chave_api_aqui

Iniciar o Dashboard
Execute o comando abaixo para abrir a interface gráfica no seu navegador:

Bash
streamlit run app.py


📊 Avaliação e Métricas de Desempenho
O modelo foi submetido a testes de stress rigorosos para validar o alinhamento entre a predição matemática e a auditoria baseada em regras. As métricas de desempenho da Rede Neural (antes da intervenção do especialista) incluem:

Acurácia Global e F1-Score: Validadas através do classification_report.

Curva ROC-AUC: Para garantir a capacidade de separação do modelo independentemente do limiar (threshold).

Taxa de Resolução de Conflitos: Monitorização de quantas vezes o Sistema Especialista precisou de intervir para corrigir falsos positivos/negativos da RNA.

👨‍💻 Autor
Breno Crespo Desenvolvido no âmbito de Pós-Graduação em Inteligência Artificial. 


***