import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pathlib import Path

# --- 1. CARREGAMENTO DOS DADOS ---
diretorio_atual = Path(__file__).resolve().parent
caminho_agrupado = diretorio_atual.parent / "dados" / "votacao_agrupada_2026.csv"
caminho_base_correlacao = diretorio_atual.parent / "dados" / "base_correlacao_2026.csv"

print("=== PROCESSANDO SANKEY COM TODOS OS CANDIDATOS ===")

df_agrupado = pd.read_csv(caminho_agrupado, sep=';', encoding='latin1')
base_correlacao = pd.read_csv(caminho_base_correlacao, sep=';', encoding='latin1')

# --- 2. IDENTIFICAÇÃO E ANONIMIZAÇÃO DOS OUTROS CANDIDATOS ---
finalistas = df_agrupado[df_agrupado['NR_TURNO'] == 2]['NM_VOTAVEL'].unique().tolist()
finalistas = [c for c in finalistas if c not in ['VOTO BRANCO', 'VOTO NULO']]

# Isola os votos do 1º turno dos candidatos eliminados
df_t1_outros = df_agrupado[
    (df_agrupado['NR_TURNO'] == 1) & 
    (~df_agrupado['NM_VOTAVEL'].isin(finalistas + ['VOTO BRANCO', 'VOTO NULO']))
]

# Ranking nacional para mapear do Candidato 3 ao 13
ranking_outros = df_t1_outros.groupby('NM_VOTAVEL')['QT_VOTOS'].sum().sort_values(ascending=False).reset_index()
mapeamento = {row['NM_VOTAVEL']: f"Candidato {i + 3}" for i, row in ranking_outros.iterrows()}
df_t1_outros['NM_ANONIMO'] = df_t1_outros['NM_VOTAVEL'].map(mapeamento)

# Total de votos no 1ºT por candidato anonimizado
votos_candidatos = df_t1_outros.groupby('NM_ANONIMO')['QT_VOTOS'].sum().to_dict()

# Adiciona os estoques de Votantes Novos e Redução de Nulos/Brancos
reducao_nulos = max(0, base_correlacao['BrancosNulos_T1'].sum() - base_correlacao['BrancosNulos_T2'].sum())
novos_votantes = max(0, base_correlacao['Var_Votantes'].sum())

# --- 3. MONTAGEM DOS NÓS DO DIAGRAMA ---
candidatos_lista = list(mapeamento.values()) # Candidato 3 ao 13
nos_origem = candidatos_lista + ["Redução Brancos/Nulos", "Novos Votantes (Abstenção)"]
nos_destino = ["Ganho Candidato 1", "Ganho Candidato 2"]

todos_nos = nos_origem + nos_destino
indice_nos = {nome: idx for idx, nome in enumerate(todos_nos)}

# --- 4. CÁLCULO DOS FLUXOS (LINKS) ---
# Distribuição proporcional de transferência baseada no ganho total de cada finalista
ganho_tot_c1 = base_correlacao['GanhoCandidato1'].sum()
ganho_tot_c2 = base_correlacao['GanhoCandidato2'].sum()
prop_c1 = ganho_tot_c1 / (ganho_tot_c1 + ganho_tot_c2)
prop_c2 = ganho_tot_c2 / (ganho_tot_c1 + ganho_tot_c2)

sources = []
targets = []
values = []
colors_links = []

# Mapeia cada origem (Candidatos 3-13, Nulos, Votantes Novos) dividida entre C1 e C2
for item in nos_origem:
    if item in votos_candidatos:
        vol = votos_candidatos[item]
    elif item == "Redução Brancos/Nulos":
        vol = reducao_nulos
    else:
        vol = novos_votantes
        
    val_c1 = vol * prop_c1
    val_c2 = vol * prop_c2
    
    # Conexão para Candidato 1
    sources.append(indice_nos[item])
    targets.append(indice_nos["Ganho Candidato 1"])
    values.append(val_c1)
    colors_links.append("rgba(31, 119, 180, 0.3)") # Transparência Azul
    
    # Conexão para Candidato 2
    sources.append(indice_nos[item])
    targets.append(indice_nos["Ganho Candidato 2"])
    values.append(val_c2)
    colors_links.append("rgba(214, 39, 40, 0.3)") # Transparência Vermelha

# --- 5. CRIAÇÃO DO SANKEY INTERATIVO (PLOTLY) ---
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=12,
        thickness=18,
        line=dict(color="black", width=0.5),
        label=[f"{nome}" for nome in todos_nos],
        color=["#7f7f7f"] * len(nos_origem) + ["#1f77b4", "#d62728"]
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=colors_links
    )
)])

fig.update_layout(
    title_text="<b>Fluxo Completo de Votos do 1º para o 2º Turno (Todos os Candidatos Eliminados)</b>",
    font_size=11,
    height=800
)

print("🌐 Abrindo o Diagrama de Sankey no navegador...")
fig.show()

# Salvar HTML local para inspeção
caminho_html = diretorio_atual.parent / "dados" / "sankey_todos_candidatos.html"
fig.write_html(str(caminho_html))
print(f"💾 Gráfico salvo em: {caminho_html}")