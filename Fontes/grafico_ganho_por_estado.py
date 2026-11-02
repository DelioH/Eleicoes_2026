import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path

# --- 1. CARREGAMENTO DOS DADOS ---
diretorio_atual = Path(__file__).resolve().parent
caminho_base = diretorio_atual.parent / "dados" / "base_correlacao_2026.csv"

df = pd.read_csv(caminho_base, sep=';', encoding='latin1')

print("=== PROCESSANDO GANHOS DE VOTOS POR ESTADO (UF) ===")

# --- 2. AGRUPAMENTO POR ESTADO ---
# Agrupamos por UF e somamos os ganhos absolutos e votantes do 1º Turno
df_uf = df.groupby('SG_UF', as_index=False).agg({
    'GanhoCandidato1': 'sum',
    'GanhoCandidato2': 'sum',
    'Votantes_T1': 'sum',
    'Outros_T1': 'sum'
})

# Criamos uma coluna de representatividade (total de votantes no 1ºT) para ordenar
# Ordenamos do MENOS representativo para o MAIS representativo
df_uf_ordenado = df_uf.sort_values(by='Votantes_T1', ascending=True).reset_index(drop=True)

print(f"Total de UFs/Exterior analisados: {len(df_uf_ordenado)}")

# --- 3. CRIAÇÃO DO GRÁFICO DE BARRAS AGRUPADAS (LADO A LADO) ---
fig = go.Figure()

# Barra do Candidato 1 (Azul)
fig.add_trace(go.Bar(
    y=df_uf_ordenado['SG_UF'],
    x=df_uf_ordenado['GanhoCandidato1'],
    name='Candidato 1',
    orientation='h',
    marker_color='#1f77b4',
    text=df_uf_ordenado['GanhoCandidato1'].apply(lambda x: f'{x:,.0f}'),
    textposition='outside'
))

# Barra do Candidato 2 (Vermelho)
fig.add_trace(go.Bar(
    y=df_uf_ordenado['SG_UF'],
    x=df_uf_ordenado['GanhoCandidato2'],
    name='Candidato 2',
    orientation='h',
    marker_color='#d62728',
    text=df_uf_ordenado['GanhoCandidato2'].apply(lambda x: f'{x:,.0f}'),
    textposition='outside'
))

# Estilização do Layout
fig.update_layout(
    title='<b>Ganho de Votos no 2º Turno por Estado (Ordenado por Representatividade)</b>',
    xaxis_title='Ganho Absoluto de Votos',
    yaxis_title='Estado / Exterior (UF)',
    barmode='group', # Coloca as barras lado a lado
    height=900,
    legend=dict(title='Candidato', orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    margin=dict(l=50, r=80, t=100, b=50)
)

fig.show()

# Salvar o gráfico interativo em HTML para inspeção
caminho_html = diretorio_atual.parent / "dados" / "ganhos_por_estado.html"
fig.write_html(str(caminho_html))
print(f"✅ Gráfico salvo em: {caminho_html}")