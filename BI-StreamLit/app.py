import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Dashboard Eleitoral - Virada 2026", layout="wide")

# --- CARREGAMENTO DOS DADOS ---
@st.cache_data
def carregar_dados():
    # Usando a base de correlação que você já preparou com todos os cálculos!
    diretorio_atual = Path(__file__).resolve().parent
    caminho = diretorio_atual.parent / "dados" / "base_correlacao_2026.csv"
    
    # Se o arquivo não existir para teste, criamos dados mockados baseados nos seus achados
    try:
        df = pd.read_csv(caminho, sep=';', encoding='latin1')
    except:
        st.error("Arquivo 'base_correlacao_2026.csv' não encontrado. Verifique a pasta 'dados'.")
        st.stop()
    return df

df = carregar_dados()

# Variáveis globais baseadas no seu EDA para os gráficos Macro
VOTOS_T1_CAND1 = df['Candidato1_T1'].sum()
VOTOS_T1_CAND2 = df['Candidato2_T1'].sum()
VOTOS_T1_OUTROS = df['Outros_T1'].sum()
BRANCOS_NULOS_T1 = df['BrancosNulos_T1'].sum()

VOTOS_T2_CAND1 = df['Candidato1_T2'].sum()
VOTOS_T2_CAND2 = df['Candidato2_T2'].sum()
BRANCOS_NULOS_T2 = df['BrancosNulos_T2'].sum()

# --- CABEÇALHO ---
st.title("📊 Dinâmica da Virada Eleitoral 2026")
st.markdown("Uma análise matemática e estatística da origem dos votos entre o 1º e o 2º Turno.")
st.divider()

# ==========================================
# PARTE 1: O CENÁRIO DO 1º TURNO
# ==========================================
st.header("1. O Cenário Inicial (1º Turno)")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribuição de Votos Nominais")
    dados_t1 = pd.DataFrame({
        'Candidato': ['Candidato 1', 'Candidato 2', 'Outros'],
        'Votos': [VOTOS_T1_CAND1, VOTOS_T1_CAND2, VOTOS_T1_OUTROS]
    })
    fig_bar1 = px.bar(dados_t1, x='Candidato', y='Votos', text_auto='.2s', 
                      color='Candidato', color_discrete_sequence=['#1f77b4', '#d62728', '#7f7f7f'])
    fig_bar1.update_traces(textposition='outside')
    st.plotly_chart(fig_bar1, use_container_width=True)

with col2:
    st.subheader("Votos Válidos vs Brancos/Nulos")
    dados_validos = pd.DataFrame({
        'Categoria': ['Válidos', 'Brancos e Nulos'],
        'Quantidade': [VOTOS_T1_CAND1 + VOTOS_T1_CAND2 + VOTOS_T1_OUTROS, BRANCOS_NULOS_T1]
    })
    fig_pie1 = px.pie(dados_validos, values='Quantidade', names='Categoria', hole=0.4,
                      color_discrete_sequence=['#2ca02c', '#c7c7c7'])
    st.plotly_chart(fig_pie1, use_container_width=True)

st.divider()

# ==========================================
# PARTE 2: A MECÂNICA DA VIRADA (2º TURNO)
# ==========================================
st.header("2. A Mecânica da Virada e o Resultado")
st.markdown("Como o segundo candidato obteve mais de 10 milhões de votos de diferença? De onde eles vieram?")

col3, col4 = st.columns(2)

with col3:
    st.subheader("O 'Estoque' de Votos Disponíveis")
    # Usando Waterfall Chart para mostrar de onde sobrou voto
    reducao_abstensao = 2960239
    reducao_nulos = BRANCOS_NULOS_T1 - BRANCOS_NULOS_T2
    
    fig_waterfall = go.Figure(go.Waterfall(
        name="Origem", orientation="v",
        measure=["relative", "relative", "relative", "total"],
        x=["Redução Abstenção", "Redução Brancos/Nulos", "Votos 'Outros'", "Total Disponível"],
        textposition="outside",
        text=["+2.96M", f"+{reducao_nulos/1e6:.2f}M", f"+{VOTOS_T1_OUTROS/1e6:.2f}M", "14.1M Votos"],
        y=[reducao_abstensao, reducao_nulos, VOTOS_T1_OUTROS, 0],
        connector={"line":{"color":"rgb(63, 63, 63)"}}
    ))
    fig_waterfall.update_layout(title="Volume máximo de votos que entraram em disputa")
    st.plotly_chart(fig_waterfall, use_container_width=True)

with col4:
    st.subheader("O Salto no 2º Turno")
    # Gráfico de barras agrupadas comparando T1 e T2
    dados_salto = pd.DataFrame({
        'Turno': ['1º Turno', '1º Turno', '2º Turno', '2º Turno'],
        'Candidato': ['Candidato 1', 'Candidato 2', 'Candidato 1', 'Candidato 2'],
        'Votos': [VOTOS_T1_CAND1, VOTOS_T1_CAND2, VOTOS_T2_CAND1, VOTOS_T2_CAND2]
    })
    fig_salto = px.bar(dados_salto, x='Turno', y='Votos', color='Candidato', barmode='group',
                       text_auto='.2s', color_discrete_sequence=['#1f77b4', '#d62728'])
    fig_salto.update_layout(title="O crescimento exponencial do Candidato 2")
    st.plotly_chart(fig_salto, use_container_width=True)

st.divider()

# ==========================================
# PARTE 3: ESTATÍSTICA REGIONAL E CRESCIMENTO
# ==========================================
st.header("3. Estabilidade e Taxa de Crescimento Municipal")

col5, col6 = st.columns(2)

with col5:
    st.subheader("Dispersão: Votos 1ºT vs Ganho no 2ºT")
    st.markdown("Mostra que os ganhos mantiveram uma correlação geográfica perfeita (0.99).")
    
    # Criando o scatter plot com os 2 candidatos no mesmo gráfico
    fig_scatter = go.Figure()
    fig_scatter.add_trace(go.Scatter(
        x=df['Candidato1_T1'], y=df['GanhoCandidato1'],
        mode='markers', name='Candidato 1', marker=dict(color='#1f77b4', opacity=0.6)
    ))
    fig_scatter.add_trace(go.Scatter(
        x=df['Candidato2_T1'], y=df['GanhoCandidato2'],
        mode='markers', name='Candidato 2', marker=dict(color='#d62728', opacity=0.6)
    ))
    fig_scatter.update_layout(xaxis_title="Votos no 1º Turno", yaxis_title="Ganho Absoluto no 2º Turno")
    st.plotly_chart(fig_scatter, use_container_width=True)

with col6:
    st.subheader("Evolução e Média de Crescimento (%)")
    st.markdown("Candidato 1 cresceu, em média, **5.2%**. O Candidato 2 cresceu **17.1%**.")
    
    # Gráfico de linhas simulando a evolução e taxa
    dados_crescimento = pd.DataFrame({
        'Candidato': ['Candidato 1', 'Candidato 2'],
        '1º Turno': [VOTOS_T1_CAND1, VOTOS_T1_CAND2],
        '2º Turno': [VOTOS_T2_CAND1, VOTOS_T2_CAND2],
        'Taxa': ['+6.7% Global (5.2% Média Mun.)', '+19.2% Global (17.1% Média Mun.)']
    })
    
    # Derretendo (Melt) para o Plotly traçar a linha de evolução
    dados_melt = pd.melt(dados_crescimento, id_vars=['Candidato', 'Taxa'], value_vars=['1º Turno', '2º Turno'], var_name='Turno', value_name='Votos')
    
    fig_line = px.line(dados_melt, x='Turno', y='Votos', color='Candidato', markers=True, text='Taxa',
                       color_discrete_sequence=['#1f77b4', '#d62728'])
    fig_line.update_traces(textposition="top center")
    fig_line.update_layout(yaxis_range=[50000000, 70000000])
    st.plotly_chart(fig_line, use_container_width=True)

st.divider()

# ==========================================
# PARTE 4: TABELA INTERATIVA (MATRIZ DE DADOS)
# ==========================================
st.header("4. Matriz Municipal de Transferência e Crescimento")
st.markdown("Explore as cidades, ordene pelos ganhos absolutos e analise o crescimento proporcional.")

# Selecionando colunas relevantes da sua base_correlacao_2026.csv
df_tabela = df[['SG_UF', 'NM_MUNICIPIO', 'Votantes_T1', 'Candidato1_T1', 'Candidato2_T1', 
                'Candidato1_T2', 'Candidato2_T2', 'GanhoCandidato1', 'GanhoCandidato2']].copy()

# Tratamento para evitar divisão por zero no cálculo de %
df_tabela['Crescimento_Cand1 (%)'] = round((df_tabela['GanhoCandidato1'] / df_tabela['Candidato1_T1'].replace(0, 1)) * 100, 2)
df_tabela['Crescimento_Cand2 (%)'] = round((df_tabela['GanhoCandidato2'] / df_tabela['Candidato2_T1'].replace(0, 1)) * 100, 2)

# Exibindo como um dataframe iterativo com barras de dados nativas do Streamlit
st.dataframe(
    df_tabela,
    column_config={
        "GanhoCandidato1": st.column_config.ProgressColumn("Ganho Abs. Cand 1", format="%d", min_value=0, max_value=int(df_tabela['GanhoCandidato1'].max())),
        "GanhoCandidato2": st.column_config.ProgressColumn("Ganho Abs. Cand 2", format="%d", min_value=0, max_value=int(df_tabela['GanhoCandidato2'].max())),
        "Crescimento_Cand1 (%)": st.column_config.NumberColumn(format="%.2f %%"),
        "Crescimento_Cand2 (%)": st.column_config.NumberColumn(format="%.2f %%"),
    },
    hide_index=True,
    use_container_width=True
)