# 30.10.2026 - Incluído barra lateral de filtros
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
    # Encontra o diretório pai (raiz do projeto) a partir de BI-StreamLit e acessa a pasta 'dados'
    diretorio_atual = Path(__file__).resolve().parent
    caminho = diretorio_atual.parent / "dados" / "base_correlacao_2026.csv"
    
    try:
        df = pd.read_csv(caminho, sep=';', encoding='latin1')
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo em {caminho}: {e}")
        st.stop()
    return df

df_bruto = carregar_dados()

# --- BARRA LATERAL (SIDEBAR) - FILTROS ---
st.sidebar.header("🔍 Filtros de Análise")

# 1. Filtro de Estado / Exterior (SG_UF)
# Lista de UFs disponíveis no dataset ordenada
lista_ufs = sorted(df_bruto['SG_UF'].unique().tolist())

# Seletor multisseleção com padrão selecionando todos os estados/exterior
ufs_selecionadas = st.sidebar.multiselect(
    "Estado / Exterior (ZZ):",
    options=lista_ufs,
    default=lista_ufs,
    help="Selecione um ou mais estados. 'ZZ' representa as urnas no Exterior."
)

# Filtragem inicial por UF
df_filtrado_uf = df_bruto[df_bruto['SG_UF'].isin(ufs_selecionadas)]

# 2. Filtro de Cidade (NM_MUNICIPIO)
# As opções de cidade são atualizadas dinamicamente de acordo com as UFs selecionadas
lista_cidades = sorted(df_filtrado_uf['NM_MUNICIPIO'].unique().tolist())

cidades_selecionadas = st.sidebar.multiselect(
    "Cidade:",
    options=lista_cidades,
    default=lista_cidades,
    help="Filtre por municípios específicos."
)

# DataFrame final filtrado pela combinação de UF e Cidade
df = df_filtrado_uf[df_filtrado_uf['NM_MUNICIPIO'].isin(cidades_selecionadas)]

# Alerta caso o filtro retorne 0 registros
if df.empty:
    st.warning("Nenhum dado encontrado para os filtros selecionados. Por favor, ajuste as opções na barra lateral.")
    st.stop()

# --- VARIÁVEIS GLOBAIS (CÁLCULO MACRO BASEADO NO FILTRO) ---
VOTOS_T1_CAND1 = df['Candidato1_T1'].sum()
VOTOS_T1_CAND2 = df['Candidato2_T1'].sum()
VOTOS_T1_OUTROS = df['Outros_T1'].sum()
BRANCOS_NULOS_T1 = df['BrancosNulos_T1'].sum()

VOTOS_T2_CAND1 = df['Candidato1_T2'].sum()
VOTOS_T2_CAND2 = df['Candidato2_T2'].sum()
BRANCOS_NULOS_T2 = df['BrancosNulos_T2'].sum()

# --- CABEÇALHO ---
st.title("📊 Dinâmica da Virada Eleitoral 2026")
st.markdown(f"Uma análise matemática e estatística da origem dos votos entre o 1º e o 2º Turno. **Registros exibidos:** {len(df):,} municípios.")
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
    st.subheader("Votos Válidos vs Brancos e Nulos")
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
st.markdown("De onde vieram os votos da virada eleitoral?")

col3, col4 = st.columns(2)

with col3:
    st.subheader("O 'Estoque' de Votos Disponíveis")
    reducao_nulos = BRANCOS_NULOS_T1 - BRANCOS_NULOS_T2
    # Caso haja filtro por Estado/Cidade, a variação de abstenção e nulos é calculada sobre o recorte
    total_disponivel = max(0, reducao_nulos) + VOTOS_T1_OUTROS
    
    fig_waterfall = go.Figure(go.Waterfall(
        name="Origem", orientation="v",
        measure=["relative", "relative", "total"],
        x=["Redução Brancos/Nulos", "Votos 'Outros'", "Total Disponível"],
        textposition="outside",
        text=[f"+{reducao_nulos/1e6:.2f}M" if reducao_nulos > 0 else "0", f"+{VOTOS_T1_OUTROS/1e6:.2f}M", f"{total_disponivel/1e6:.2f}M Votos"],
        y=[max(0, reducao_nulos), VOTOS_T1_OUTROS, 0],
        connector={"line":{"color":"rgb(63, 63, 63)"}}
    ))
    fig_waterfall.update_layout(title="Volume de votos em disputa no recorte")
    st.plotly_chart(fig_waterfall, use_container_width=True)

with col4:
    st.subheader("O Salto no 2º Turno")
    dados_salto = pd.DataFrame({
        'Turno': ['1º Turno', '1º Turno', '2º Turno', '2º Turno'],
        'Candidato': ['Candidato 1', 'Candidato 2', 'Candidato 1', 'Candidato 2'],
        'Votos': [VOTOS_T1_CAND1, VOTOS_T1_CAND2, VOTOS_T2_CAND1, VOTOS_T2_CAND2]
    })
    fig_salto = px.bar(dados_salto, x='Turno', y='Votos', color='Candidato', barmode='group',
                       text_auto='.2s', color_discrete_sequence=['#1f77b4', '#d62728'])
    fig_salto.update_layout(title="O crescimento dos finalistas no 2º Turno")
    st.plotly_chart(fig_salto, use_container_width=True)

st.divider()

# ==========================================
# PARTE 3: ESTATÍSTICA REGIONAL E DISPERSÃO INTERATIVA
# ==========================================
st.header("3. Estabilidade e Taxa de Crescimento Municipal")
st.markdown("Passe o cursor sobre os pontos para identificar o município. **Clique em um ponto do gráfico** para filtrar a cidade abaixo.")

col5, col6 = st.columns(2)

with col5:
    st.subheader("Dispersão: Votos 1ºT vs Ganho no 2ºT")
    
    fig_scatter = go.Figure()
    
    # Série Candidato 1
    fig_scatter.add_trace(go.Scatter(
        x=df['Candidato1_T1'], 
        y=df['GanhoCandidato1'],
        mode='markers', 
        name='Candidato 1',
        text=df['NM_MUNICIPIO'],
        customdata=df[['SG_UF', 'Candidato1_T1', 'GanhoCandidato1']],
        hovertemplate="<b>%{text} (%{customdata[0]})</b><br>Votos 1ºT: %{customdata[1]:,}<br>Ganho 2ºT: %{customdata[2]:,}<extra>Candidato 1</extra>",
        marker=dict(color='#1f77b4', opacity=0.6)
    ))
    
    # Série Candidato 2
    fig_scatter.add_trace(go.Scatter(
        x=df['Candidato2_T1'], 
        y=df['GanhoCandidato2'],
        mode='markers', 
        name='Candidato 2',
        text=df['NM_MUNICIPIO'],
        customdata=df[['SG_UF', 'Candidato2_T1', 'GanhoCandidato2']],
        hovertemplate="<b>%{text} (%{customdata[0]})</b><br>Votos 1ºT: %{customdata[1]:,}<br>Ganho 2ºT: %{customdata[2]:,}<extra>Candidato 2</extra>",
        marker=dict(color='#d62728', opacity=0.6)
    ))
    
    fig_scatter.update_layout(
        xaxis_title="Votos no 1º Turno", 
        yaxis_title="Ganho Absoluto no 2º Turno",
        legend_title="Candidatos"
    )
    
    evento_selecao = st.plotly_chart(
        fig_scatter, 
        use_container_width=True,
        on_select="rerun",
        selection_mode="points"
    )

with col6:
    st.subheader("Evolução Global no Recorte")
    
    dados_crescimento = pd.DataFrame({
        'Candidato': ['Candidato 1', 'Candidato 2'],
        '1º Turno': [VOTOS_T1_CAND1, VOTOS_T1_CAND2],
        '2º Turno': [VOTOS_T2_CAND1, VOTOS_T2_CAND2]
    })
    
    dados_melt = pd.melt(dados_crescimento, id_vars=['Candidato'], value_vars=['1º Turno', '2º Turno'], var_name='Turno', value_name='Votos')
    
    fig_line = px.line(dados_melt, x='Turno', y='Votos', color='Candidato', markers=True,
                       color_discrete_sequence=['#1f77b4', '#d62728'])
    fig_line.update_traces(textposition="top center")
    st.plotly_chart(fig_line, use_container_width=True)

st.divider()

# ==========================================
# PARTE 4: TABELA INTERATIVA (MATRIZ DE DADOS)
# ==========================================
st.header("4. Matriz Municipal de Transferência e Crescimento")

# Captura o clique em qualquer um dos pontos do gráfico
cidade_selecionada = None
if evento_selecao and "selection" in evento_selecao and "points" in evento_selecao["selection"]:
    pontos = evento_selecao["selection"]["points"]
    if len(pontos) > 0 and "text" in pontos[0]:
        cidade_selecionada = pontos[0]["text"]

df_tabela = df[['SG_UF', 'NM_MUNICIPIO', 'Votantes_T1', 'Candidato1_T1', 'Candidato2_T1', 
                'Candidato1_T2', 'Candidato2_T2', 'GanhoCandidato1', 'GanhoCandidato2']].copy()

df_tabela.rename(columns={'SG_UF': 'UF', 'NM_MUNICIPIO': 'Município'}, inplace=True)

# Cálculo do crescimento percentual
df_tabela['Crescimento_Cand1 (%)'] = round((df_tabela['GanhoCandidato1'] / df_tabela['Candidato1_T1'].replace(0, 1)) * 100, 2)
df_tabela['Crescimento_Cand2 (%)'] = round((df_tabela['GanhoCandidato2'] / df_tabela['Candidato2_T1'].replace(0, 1)) * 100, 2)

if cidade_selecionada:
    st.success(f"📍 Exibindo dados filtrados para a cidade selecionada no gráfico: **{cidade_selecionada}**")
    df_exibicao = df_tabela[df_tabela['Município'] == cidade_selecionada]
else:
    st.info("💡 Dica: Use os filtros da barra lateral para refinar o Estado/Cidade ou clique em um ponto do gráfico acima.")
    df_exibicao = df_tabela

st.dataframe(
    df_exibicao,
    column_config={
        "GanhoCandidato1": st.column_config.ProgressColumn("Ganho Abs. Cand 1", format="%d", min_value=0, max_value=int(df_tabela['GanhoCandidato1'].max() if not df_tabela.empty else 1)),
        "GanhoCandidato2": st.column_config.ProgressColumn("Ganho Abs. Cand 2", format="%d", min_value=0, max_value=int(df_tabela['GanhoCandidato2'].max() if not df_tabela.empty else 1)),
        "Crescimento_Cand1 (%)": st.column_config.NumberColumn(format="%.2f %%"),
        "Crescimento_Cand2 (%)": st.column_config.NumberColumn(format="%.2f %%"),
    },
    hide_index=True,
    use_container_width=True
)