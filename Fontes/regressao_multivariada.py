import pandas as pd
import numpy as np
import statsmodels.api as sm
from pathlib import Path

# --- 1. CARREGAMENTO DOS DADOS ---
diretorio_atual = Path(__file__).resolve().parent
caminho_agrupado = diretorio_atual.parent / "dados" / "votacao_agrupada_2026.csv"
caminho_base_correlacao = diretorio_atual.parent / "dados" / "base_correlacao_2026.csv"

df_agrupado = pd.read_csv(caminho_agrupado, sep=';', encoding='latin1')
base_correlacao = pd.read_csv(caminho_base_correlacao, sep=';', encoding='latin1')

print("=== MENSURAÇÃO DA TAXA DE TRANSFERÊNCIA DE VOTOS (MODELO DE REGRESSÃO MULTIVARIADA) ===")

# --- 2. ANONIMIZAÇÃO E AGRUPAMENTO DOS CANDIDATOS ELIMINADOS ---
finalistas = df_agrupado[df_agrupado['NR_TURNO'] == 2]['NM_VOTAVEL'].unique().tolist()
finalistas = [c for c in finalistas if c not in ['VOTO BRANCO', 'VOTO NULO']]

df_t1_outros = df_agrupado[
    (df_agrupado['NR_TURNO'] == 1) & 
    (~df_agrupado['NM_VOTAVEL'].isin(finalistas + ['VOTO BRANCO', 'VOTO NULO']))
]

# Ranking nacional dos candidatos eliminados
ranking_outros = df_t1_outros.groupby('NM_VOTAVEL')['QT_VOTOS'].sum().sort_values(ascending=False).reset_index()

mapeamento_candidatos = {row['NM_VOTAVEL']: f"Candidato {i + 3}" for i, row in ranking_outros.iterrows()}

df_t1_outros['NM_ANONIMO'] = df_t1_outros['NM_VOTAVEL'].map(mapeamento_candidatos)

df_pivot_outros = df_t1_outros.pivot_table(
    index=['SG_UF', 'NM_MUNICIPIO'],
    columns='NM_ANONIMO',
    values='QT_VOTOS',
    aggfunc='sum',
    fill_value=0
).reset_index()

# Unir com a base de ganhos
df_modelo = pd.merge(base_correlacao, df_pivot_outros, on=['SG_UF', 'NM_MUNICIPIO'], how='left').fillna(0)

# --- 3. CONSTRUÇÃO DO MODELO DE REGRESSÃO LINEAR MÚLTIPLA ---
colunas_preditoras = list(mapeamento_candidatos.values())
X = df_modelo[colunas_preditoras]

# Adiciona o termo constante (Intercepto \beta_0)
X = sm.add_constant(X)

# A) Regressão para o Ganho do Candidato 1
y_cand1 = df_modelo['GanhoCandidato1']
modelo_cand1 = sm.OLS(y_cand1, X).fit()

# B) Regressão para o Ganho do Candidato 2
y_cand2 = df_modelo['GanhoCandidato2']
modelo_cand2 = sm.OLS(y_cand2, X).fit()

# --- 4. CONSOLIDAÇÃO DA TABELA DE TAXAS DE CONVERSÃO ---
tabela_transferencia = []

for cand in colunas_preditoras:
    beta_c1 = modelo_cand1.params[cand]
    beta_c2 = modelo_cand2.params[cand]
    
    total_votos_origem = df_modelo[cand].sum()
    estimado_ganho_c1 = total_votos_origem * beta_c1
    estimado_ganho_c2 = total_votos_origem * beta_c2
    
    tabela_transferencia.append({
        'Candidato de Origem (1ºT)': cand,
        'Votos Totais 1ºT': total_votos_origem,
        'Taxa Conversão Cand 1 (β)': round(beta_c1, 4),
        'Ganho Estimado Cand 1': int(estimado_ganho_c1),
        'Taxa Conversão Cand 2 (β)': round(beta_c2, 4),
        'Ganho Estimado Cand 2': int(estimado_ganho_c2)
    })

df_resultado = pd.DataFrame(tabela_transferencia)

print("\n📊 ESTIMAÇÃO DA MIGRACÃO E TAXA DE CONVERSÃO POR CANDIDATO ELIMINADO:")
print(df_resultado.to_string(index=False))

print(f"\n📈 Ajuste do Modelo (R² Candidato 1): {modelo_cand1.rsquared:.4f}")
print(f"📈 Ajuste do Modelo (R² Candidato 2): {modelo_cand2.rsquared:.4f}")