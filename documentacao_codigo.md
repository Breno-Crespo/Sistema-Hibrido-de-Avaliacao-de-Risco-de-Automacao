# Documentação Passo a Passo: modelo.ipynb

Este documento explica de forma simples, e bloco a bloco, tudo o que o código atual faz e **por que** essas escolhas técnicas foram feitas.

---

## 1. Importação e Configuração Inicial (Cells 0 e 1)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score, f1_score
from experta import *
import kagglehub
from kagglehub import KaggleDatasetAdapter
```
* **O que faz:** Traz para o projeto todas as "caixas de ferramentas" (bibliotecas) necessárias. `pandas` e `numpy` para manipular planilhas, `matplotlib` e `seaborn` para desenhar gráficos, `tensorflow` para criar a rede neural (IA) e `sklearn` para preparar os dados e avaliar os resultados. O `experta` é o motor de regras do sistema especialista.
* **Por que:** Sem essas bibliotecas, teríamos que escrever a matemática complexa da Inteligência Artificial ou desenhar gráficos do total zero.

### Bloco de Correção do Experta e Temas Visuais
* Foi incluído um bloco de código remapeando o módulo `collections` para suportar versões de Python 3.10+, garantindo que a biblioteca de sistemas especialistas (`experta`) não trave.
* Em seguida (Cell 1), configuramos um tema "Dark Mode" azul cibernético no `matplotlib` para que todos os gráficos criados fiquem automaticamente mais bonitos e adequados ao tema do projeto.

---

## 2. Carga e Análise dos Dados (Cells 2 a 8)
```python
df_rnn = pd.read_csv("dataset/ai_job_dataset.csv")
```
* **O que faz:** Carrega a planilha (onde estão as vagas de emprego, salários e níveis de experiência) para a memória sob a variável `df_rnn`.
* Usamos comandos como `df_rnn.head()`, `df_rnn.shape`, `df_rnn.info()`, `df_rnn.describe()` e `df_rnn.isnull().sum()`.
* **Por que:** Faz parte do EDA (Análise Exploratória de Dados). Queremos entender os tipos de dados (texto vs número) e garantir que não tem nenhum dado vazio (`null`) na planilha, o que quebraria a Rede Neural.

---

## 3. Pré-processamento e Transformações (Cell 9 a 11)

```python
df_rnn_encoded = pd.get_dummies(df_rnn, columns=['experience_level', 'education_required', 'industry', 'employment_type', 'company_size'], drop_first=True)
```
* **O que faz:** Pega todas as colunas de texto (categorias categóricas, ex: Media, Automotive, etc.) e as converte em diversas colunas contendo 0 ou 1 (One-Hot Encoding).
* **Por que:** **MUITO IMPORTANTE!** As Redes Neurais só entendem números. Se usássemos `1=Media` e `2=Automotive`, a rede neural iria pensar que Automotivo é o duplo de valor matemático que Mídia. O Formato One-Hot Encoding impede esse viés.

```python
media_salarial = df_rnn['salary_usd'].median()
df_rnn['risco_score'] = (1 / (df_rnn['years_experience'] + 1)) * (media_salarial / df_rnn['salary_usd'])
df_rnn['target_risco'] = (df_rnn['risco_score'] > df_rnn['risco_score'].median()).astype(int)
```
* **O que faz:** Cria a regra básica (Target) que precisamos prever. Ele calcula a média salarial da base toda. Se a vaga pagar abaixo da média salarial e além disso pedir pouca experiência, o risco sobe. Depois criamos uma coluna `target_risco` binária (1 = Risco Alto de Automação, 0 = Risco Baixo).
* **Por que:** Todo modelo de IA (Aprendizado Supervisionado) precisa de uma resposta "Alvo" para aprender. Construímos isso sinteticamente aqui baseado no cenário econômico simples de "baixo custo de mão de obra + pouca especialização = alto risco de automação".

---

## 4. Geração dos Gráficos EDA (Cells 12 a 15)

O código roda uma série de `sns.scatterplot()`, `sns.countplot()`, `sns.barplot()` e `sns.heatmap()`.
* **Por que Scatterplot:** Para plotar ponto a ponto e observar como Salário e Experiência caminham de mãos dadas para gerar o tal "risco".
* **Por que Bar/Count plots:** Para mostrar ranqueamentos claros de risco probabilístico de acordo com Escolaridade ou segmento Industrial de forma rápida.
* **Por que Matriz de Correlação:** Para ajudar engenheiros de dados a bater o olho e ver que fator (exemplo: taxa de trabalho remoto vs salário) tem maior força positiva (vermelho) ou negativa (azul) sobre o desfecho final.

---

## 5. Treinamento do Modelo de Deep Learning (Cells 17 a 21)

```python
features_reais = [col for col in df_rnn_encoded.columns if col not in ['job_id', ... , 'target_risco', 'risco_score']]
X = df_rnn_encoded[features_reais].values
y = df_rnn_encoded['target_risco'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
* **O que faz:** Separa 20% das linhas do arquivo para "prova final" (X_test) e 80% para a máquina estudar e aprender as correlações (X_train). Retira também as variáveis indesejáveis pro aprendizado numérico (`job_id`, etc).

```python
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
```
* **O que faz:** Ajusta o volume ou magnitude de todos os números na mesma proporção estatística (z-scoring). 
* **Por que:** O salário tem a escala de "90.000", já a proporção de home office tem escala "50". Sem o StandardScaler para forçar as medidas a oscilarem próximas a zero, a rede neural pensaria erroneamente que salário importa absurdamente muito mais apenas porque a ordem de grandeza do número é enorme.

### A Arquitetura Oculta Múltipla (MLP)
```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(len(features_reais),)),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.2), # Dropout extra para regularização 
    tf.keras.layers.Dense(1, activation='sigmoid')
])
```
* **O que faz:** O cérebro virtual do modelo. 
    * Ele possui uma camada gigante extraindo 128 recortes escondidos das características e outra com 64. A `relu` apenas diz "se a correlação for negativa, ignore e repasse 0 para o próximo nó, senão deixe passar inteiro".
    * A função matemática da última linha `sigmoid` é uma função estatística que cospe um número variando apenas de 0.000 a 1.000 (exatamente a Probabilidade de Risco!).
* **Por que o Dropout:** Desliga neurônios de propósito durante o treino. Se você não fizer isso, o modelo decora as repostas "viciadas" da prova ao invés de "generalizar" aprender os conceitos abstratos (Problema clássico conhecido como *Overfitting* simulado).

```python
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
model.fit(X_train, y_train, epochs=30, validation_split=0.2, callbacks=[early_stopping])
```
* **O que faz:** Roda o relógio de treinamento em até 30 repetições (`epochs=30`), porém o `EarlyStopping` vigia para onde a curva de aprendizado do modelo está indo e se ela começar a piorar e continuar ruim depois de 5 etapas (`patience=5`), ele suspende o código e diz "pronto, você já aprendeu o máximo que pode".

---

## 6. Motor do Sistema Especialista e Teste Real (Cells 22 a 23)

```python
class AnalisadorRisco(KnowledgeEngine):
    @Rule(ProfissaoFact(years_experience=P(lambda x: x <= 2), salary_usd=P(lambda x: x < 50000)))
    def risco_alto_entrada(self): ...
    
    @Rule(ProfissaoFact(education_required="Master", industry="Media"))
...
```
* **O que faz:** O framework `experta` imita um ser humano pensando usando a filosofia Lógica de Primeira Ordem da antiga Inteligência Artificial simbólica ("SE A E B então faça C"). Nós colocamos regras descritas com texto natural que fazem o módulo disparar "tags" de conhecimento.

```python
def testar_sistema_real(index_linha):
   ...
    # Extrato modelo IA para prever a probabilidade P (0.01 = seguro, 0.99 = Risco Absoluto)
    prob = model.predict(input_scaled, verbose=0)[0][0]
    
    # Motor simula o disparo de texto humano pelas regras do Experta explicitando O PORQUE
    engine = AnalisadorRisco()
    engine.run()
```
* **O que faz:** É a interface de união inteligente final. Ela busca uma linha da planilha (simulando a submissão de uma nova vaga), entrega ela para a `Rede Neural` prever o perigo oculto na casa probabilística (com o array padronizado) E AO MESMO TEMPO entrega os dados "brutos" textuais para o Sistema Especialista `Experta` tentar nos devolver sua "Opinião humana justificada" do porquê os fatores explícitos combinados causaram aquilo baseado na instrução estrita que demos passo a passo. 
