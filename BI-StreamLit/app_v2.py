import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Análise da Dinâmica e Virada Eleitoral 2026", layout="wide")

# --- CARREGAMENTO DOS DADOS ---
@st.cache_data
def carregar_dados():
    # Sobe um nível para encontrar a pasta 'dados' e ler a base consolidada de correlação
    diretorio_atual = Path(__file__).resolve().parent
    caminho = diretorio_atual.parent / "dados" / "base_correlacao_2026.csv"
    
    try:
        df = pd.read_csv(caminho, sep=';', encoding='latin1')
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo de dados em: {caminho}. Detalhe: {e}")
        st.stop()
    return df

df = carregar_dados()

# --- CABEÇALHO DO DASHBOARD ---
st.title("📊 Dinâmica e Virada Eleitoral (1º e 2º Turno - 2026)")
st.markdown("""
Painel analítico desenvolvido para responder à pergunta central: **Como se deu a virada de votos no 2º turno?** 
A investigação cruza o comportamento macroeconômico/eleitoral com a estabilidade geográfica e a transferência de votos de candidatos eliminados.
""")
st.divider()

# ==========================================
# PARTE 1: O CENÁRIO DO 1º TURNO (Lado a Lado)
# ==========================================
st.header("1. O Ponto de Partida: Cenário do 1º Turno")
st.markdown("Comparação inicial entre o volume de votos nominais dos candidatos, votos válidos e o peso dos votos brancos e nulos.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Votos Nominais (1º Turno)")
    # Somatório macro dos candidatos e outros
    total_c1_t1 = df['Candidato1_T1'].sum()
    total_c2_t1 = df['Candidato2_T1'].sum()
    total_outros_t1 = df['Outros_T1'].sum()
    
    df_t1_nominal = pd.DataFrame({
        'Candidato': ['Candidato 1 (PL)', 'Candidato 2 (PT)', 'Outros Candidatos'],
        'Votos': [total_c1_t1, total_c2_t1, total_outros_t1]
    })
    
    fig_t1 = px.bar(df_t1_nominal, x='Candidato', y='Votos', text_auto='.2s',
                    color='Candidato', color_discrete_sequence=['#1f77b4', '#d62728', '#7f7f7f'])
    fig_t1.update_layout(showlegend=False)
    st.plotly_chart(fig_t1, use_container_width=True)

with col2:
    st.subheader("Votos Válidos vs. Brancos e Nulos")
    total_validos_t1 = total_c1_t1 + total_c2_t1 + total_outros_t1
    total_brancos_nulos_t1 = df['BrancosNulos_T1'].sum()
    
    df_brancos = pd.DataFrame({
        'Tipo': ['Votos Válidos', 'Brancos e Nulos'],
        'Quantidade': [total_validos_t1, total_brancos_nulos_t1]
    })
    
    fig_pie = px.pie(df_brancos, values='Quantidade', names='Tipo', hole=0.5,
                     color_discrete_sequence=['#2ca02c', '#ff7f0e'])
    st.plotly_chart(fig_pie, use_container_width=True)

st.divider()

# ==========================================
# PARTE 2: A MECÂNICA DA VIRADA (O que sobrou dos votos)
# ==========================================
st.header("2. A Mecânica da Virada no 2º Turno")
st.markdown("""
Para explicar a virada, quantificamos o 'estoque' de votos em disputa deixado pelo 1º turno:
* **Aumento de Votantes:** +2.960.239 votos a mais no 2º turno.
* **Redução de Brancos/Nulos:** 1.816.000 votos que migraram para validos.
* **Votos de Terceiros (Outros):** 9.321.993 votos de candidatos eliminados.
""")

col3, col4 = st.columns(2)

with col3:
    st.subheader("O Estoque de Oportunidades (Potencial da Virada)")
    # Gráfico Waterfall ou de Barras mostrando os potenciais calculados na sua EDA
    df_estoque = pd.DataFrame({
        'Fator': ['Redução Abstenção', 'Redução Brancos/Nulos', 'Votos Outros Candidatos'],
        'Votos Potenciais': [2960239, 1816000, 9321993]
    })
    fig_est = px.bar(df_estoque, x='Fator', y='Votos Potenciais', text_auto='.2s',
                     color='Fator', color_discrete_sequence=['#9467bd', '#8c564b', '#e377c2'])
    st.plotly_chart(fig_est, use_container_width=True)

with col4:
    st.subheader("O Salto de Desempenho (1º vs 2º Turno)")
    total_c1_t2 = df['Candidato1_T2'].sum()
    total_c2_t2 = df['Candidato2_T2'].sum()
    
    df_comparativo_turnos = pd.DataFrame({
        'Turno': ['1º Turno', '1º Turno', '2º Turno', '2º Turno'],
        'Candidato': ['Candidato 1', 'Candidato 2', 'Candidato 1', 'Candidato 2'],
        'Votos': [total_c1_t1, total_c2_t1, total_c1_t2, total_c2_t2]
    })
    
    fig_comp = px.bar(df_comparativo_turnos, x='Turno', y='Votos', color='Candidato', barmode='group',
                      text_auto='.2s', color_discrete_sequence=['#1f77b4', '#d62728'])
    st.plotly_chart(fig_comp, use_container_width=True)

st.divider()

# ==========================================
# PARTE 3: ESTATÍSTICA, CORRELAÇÃO E CRESCIMENTO (%)
# ==========================================
st.header("3. Análise Estatística: Estabilidade e Origem dos Votos")

col5, col6 = st.columns(2)

with col5:
    st.subheader("Dispersão: Votos 1ºT vs Ganho no 2ºT")
    st.markdown("Mostra a **Estabilidade Eleitoral**: correlação geográfica altíssima (~0.999), indicando que os candidatos mantiveram suas bases regionais.")
    
    fig_scatter = go.Figure()
    fig_scatter.add_trace(go.Scatter(
        x=df['Candidato1_T1'], y=df['GanhoCandidato1'],
        mode='markers', name='Candidato 1 (r ≈ 0.95)', marker=dict(color='#1f77b4', opacity=0.5)
    ))
    fig_scatter.add_trace(go.Scatter(
        x=df['Candidato2_T1'], y=df['GanhoCandidato2'],
        mode='markers', name='Candidato 2 (r ≈ 0.98)', marker=dict(color='#d62728', opacity=0.5)
    ))
    fig_scatter.update_layout(xaxis_title="Votos no 1º Turno", yaxis_title="Ganho Absoluto no 2º Turno")
    st.plotly_chart(fig_scatter, use_container_width=True)

with col6:
    st.subheader("Taxa de Crescimento Municipal (Média vs Mediana)")
    st.markdown("""
    Evidência da superioridade no ritmo de crescimento do Candidato 2:
    * **Candidato 1:** Média de crescimento de **5.2%** (Mediana: 5.9%)
    * **Candidato 2:** Média de crescimento de **17.1%** (Mediana: 16.6%)
    """)
    
    # Gráfico demonstrando as médias de crescimento que você calculou
    df_crescimento_resumo = pd.DataFrame({
        'Candidato': ['Candidato 1', 'Candidato 2'],
        'Crescimento Médio (%)': [5.20, 17.16],
        'Crescimento Mediano (%)': [5.91, 16.66]
    })
    
    fig_box = px.bar(df_crescimento_resumo, x='Candidato', y=['Crescimento Médio (%)', 'Crescimento Mediano (%)'],
                     barmode='group', text_auto=True, color_discrete_sequence=['#aec7e8', '#ff9896'])
    st.plotly_chart(fig_box, use_container_width=True)

st.divider()

# ==========================================
# PARTE 4: MATRIZ DE DADOS MUNICIPAIS (Tabela Dinâmica)
# ==========================================
st.header("4. Matriz de Dados Municipais (Exploração Detalhada)")
st.markdown("Explore os municípios, ordene pelas colunas de ganho e analise a transferência de votos.")

# Selecionando colunas relevantes da base de correlação
df_tabela = df[['UF', 'Município', 'Candidato1_T1', 'Candidato2_T1', 'Outros_T1', 
                'Candidato1_T2', 'Candidato2_T2', 'GanhoCandidato1', 'GanhoCandidato2']].copy()

# Cálculo percentual de crescimento individual por cidade
df_tabela['Cresc_Cand1 (%)'] = round((df_tabela['GanhoCandidato1'] / df_tabela['Candidato1_T1'].replace(0, 1)) * 100, 2)
df_tabela['Cresc_Cand2 (%)'] = round((df_tabela['GanhoCandidato2'] / df_tabela['Candidato2_T1'].replace(0, 1)) * 100, 2)

# Exibição interativa com barras de progresso nativas do Streamlit
st.dataframe(
    df_tabela,
    column_config={
        "GanhoCandidato1": st.column_config.ProgressColumn("Ganho Abs. C1", format="%d", min_value=0, max_value=int(df_tabela['GanhoCandidato1'].max())),
        "GanhoCandidato2": st.column_config.ProgressColumn("Ganho Abs. C2", format="%d", min_value=0, max_value=int(df_tabela['GanhoCandidato2'].max())),
        "Cresc_Cand1 (%)": st.column_config.NumberColumn(format="%.2f %%"),
        "Cresc_Cand2 (%)": st.column_config.NumberColumn(format="%.2f %%"),
    },
    hide_index=True,
    use_container_width=True
)