import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# --- 1. CARREGAMENTO DOS DADOS ---
diretorio_atual = Path(__file__).resolve().parent
caminho_agrupado = diretorio_atual.parent / "dados" / "votacao_agrupada_2026.csv"
caminho_base_correlacao = diretorio_atual.parent / "dados" / "base_correlacao_2026.csv"

print("=== INICIANDO ANÁLISE DE CORRELAÇÃO DE CANDIDATOS ELIMINADOS ===")

df_agrupado = pd.read_csv(caminho_agrupado, sep=';', encoding='latin1')
base_correlacao = pd.read_csv(caminho_base_correlacao, sep=';', encoding='latin1')

# --- 2. IDENTIFICAÇÃO E ANONIMIZAÇÃO DOS OUTROS CANDIDATOS ---
# Identifica os 2 finalistas do 2º turno
finalistas = df_agrupado[df_agrupado['NR_TURNO'] == 2]['NM_VOTAVEL'].unique().tolist()
finalistas = [c for c in finalistas if c not in ['VOTO BRANCO', 'VOTO NULO']]

# Isola apenas os dados do 1º turno para os candidatos eliminados
df_t1_outros = df_agrupado[
    (df_agrupado['NR_TURNO'] == 1) & 
    (~df_agrupado['NM_VOTAVEL'].isin(finalistas + ['VOTO BRANCO', 'VOTO NULO']))
]

# Ranking nacional dos candidatos eliminados no 1º turno (por total de votos)
ranking_outros = df_t1_outros.groupby('NM_VOTAVEL')['QT_VOTOS'].sum().sort_values(ascending=False).reset_index()

# Mapeamento para anonimizar: 3º colocado -> Candidato 3, 4º colocado -> Candidato 4, etc.
mapeamento_candidatos = {}
for i, row in ranking_outros.iterrows():
    mapeamento_candidatos[row['NM_VOTAVEL']] = f"Candidato {i + 3}"

print("\n📍 Ranking Nacional dos Candidatos Eliminados (Anonimizados):")
for orig, anon in mapeamento_candidatos.items():
    votos_totais = ranking_outros[ranking_outros['NM_VOTAVEL'] == orig]['QT_VOTOS'].values[0]
    print(f" - {anon} ({orig}): {votos_totais:,} votos")

# --- 3. AGRUPAMENTO POR MUNICÍPIO ---
# Tabela com os votos de cada candidato eliminado por município
df_t1_outros['NM_ANONIMO'] = df_t1_outros['NM_VOTAVEL'].map(mapeamento_candidatos)
df_pivot_outros = df_t1_outros.pivot_table(
    index=['SG_UF', 'NM_MUNICIPIO'],
    columns='NM_ANONIMO',
    values='QT_VOTOS',
    aggfunc='sum',
    fill_value=0
).reset_index()

# Unir os votos anonimizados com os ganhos dos 2 finalistas
df_analise = pd.merge(base_correlacao, df_pivot_outros, on=['SG_UF', 'NM_MUNICIPIO'], how='left').fillna(0)

# --- 4. GERAÇÃO DA MATRIZ DE CORRELAÇÃO ---
colunas_outros_anonimos = list(mapeamento_candidatos.values())
colunas_ganhos = ['GanhoCandidato1', 'GanhoCandidato2']
colunas_matriz = colunas_outros_anonimos + colunas_ganhos

matriz_correlacao = df_analise[colunas_matriz].corr()

print("\n📊 MATRIZ DE CORRELAÇÃO DE PEARSON (Votos 1ºT vs Ganhos 2ºT):")
print(matriz_correlacao[colunas_ganhos].loc[colunas_outros_anonimos].round(4))

# Visualização da Matriz de Correlação (Heatmap)
plt.figure(figsize=(10, 8))
sns.heatmap(
    matriz_correlacao.loc[colunas_outros_anonimos, colunas_ganhos], 
    annot=True, 
    cmap='coolwarm', 
    fmt='.4f', 
    vmin=-1, 
    vmax=1,
    cbar_kbar_kws={'label': 'Coeficiente de Pearson (r)'}
)
plt.title('Matriz de Correlação: Votos de Candidatos Eliminados (1ºT) vs Ganho dos Finalistas (2ºT)')
plt.tight_layout()
plt.show()

# --- 5. GRÁFICOS DE DISPERSÃO INDIVIDUAIS (SCATTER PLOTS) ---
# Gerar um par de gráficos de dispersão para cada candidato eliminado
print("\n📈 Gerando gráficos de dispersão individuais...")

sns.set_theme(style="whitegrid")
num_candidatos = len(colunas_outros_anonimos)

# Criar um grid de subplots
fig, axes = plt.subplots(nrows=num_candidatos, ncols=2, figsize=(14, 4 * num_candidatos))
fig.suptitle('Dispersão Municipal: Votos 1ºT dos Eliminados vs Ganhos no 2ºT', fontsize=16, y=1.002)

for idx, cand_anonimo in enumerate(colunas_outros_anonimos):
    # Gráfico 1: Votos do Candidato Anonimizado vs Ganho do Candidato 1
    sns.scatterplot(
        data=df_analise, 
        x=cand_anonimo, 
        y='GanhoCandidato1', 
        ax=axes[idx, 0], 
        color='#1f77b4', 
        alpha=0.6
    )
    r1 = matriz_correlacao.loc[cand_anonimo, 'GanhoCandidato1']
    axes[idx, 0].set_title(f'{cand_anonimo} vs Ganho Candidato 1 (r = {r1:.4f})')
    axes[idx, 0].set_xlabel(f'Votos no {cand_anonimo} (1ºT)')
    axes[idx, 0].set_ylabel('Ganho Candidato 1 (2ºT)')

    # Gráfico 2: Votos do Candidato Anonimizado vs Ganho do Candidato 2
    sns.scatterplot(
        data=df_analise, 
        x=cand_anonimo, 
        y='GanhoCandidato2', 
        ax=axes[idx, 1], 
        color='#d62728', 
        alpha=0.6
    )
    r2 = matriz_correlacao.loc[cand_anonimo, 'GanhoCandidato2']
    axes[idx, 1].set_title(f'{cand_anonimo} vs Ganho Candidato 2 (r = {r2:.4f})')
    axes[idx, 1].set_xlabel(f'Votos no {cand_anonimo} (1ºT)')
    axes[idx, 1].set_ylabel('Ganho Candidato 2 (2ºT)')

plt.tight_layout()
plt.show()