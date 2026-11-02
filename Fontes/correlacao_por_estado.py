import pandas as pd
import numpy as np
from pathlib import Path

# 1. CARREGAMENTO DOS DADOS
diretorio_atual = Path(__file__).resolve().parent
caminho_base = diretorio_atual.parent / "dados" / "base_correlacao_2026.csv"

df = pd.read_csv(caminho_base, sep=';', encoding='latin1')

print("=== ANÁLISE DE CORRELAÇÃO E RITMO DA VIRADA POR ESTADO (UF) ===")

# 2. CÁLCULO DAS MÉTRICAS E CORRELAÇÃO POR UF
resultados_uf = []

for uf, grupo in df.groupby('SG_UF'):
    qtd_municipios = len(grupo)
    
    # Evita erro em UFs com menos de 2 registros de cidades
    if qtd_municipios > 2:
        corr_c1 = grupo['Outros_T1'].corr(grupo['GanhoCandidato1'])
        corr_c2 = grupo['Outros_T1'].corr(grupo['GanhoCandidato2'])
    else:
        corr_c1 = np.nan
        corr_c2 = np.nan
        
    tot_outros = grupo['Outros_T1'].sum()
    ganho_c1 = grupo['GanhoCandidato1'].sum()
    ganho_c2 = grupo['GanhoCandidato2'].sum()
    
    # Média do crescimento percentual nos municípios do estado
    cresc_med_c1 = (grupo['GanhoCandidato1'] / grupo['Candidato1_T1'].replace(0, 1) * 100).mean()
    cresc_med_c2 = (grupo['GanhoCandidato2'] / grupo['Candidato2_T1'].replace(0, 1) * 100).mean()
    
    resultados_uf.append({
        'UF': uf,
        'Municípios': qtd_municipios,
        'Estoque Outros (1ºT)': tot_outros,
        'Ganho Cand 1': ganho_c1,
        'Ganho Cand 2': ganho_c2,
        'Corr (Outros x Ganho C1)': round(corr_c1, 4),
        'Corr (Outros x Ganho C2)': round(corr_c2, 4),
        'Cresc. Médio C1 (%)': round(cresc_med_c1, 2),
        'Cresc. Médio C2 (%)': round(cresc_med_c2, 2)
    })

df_estados = pd.DataFrame(resultados_uf)

# Ordenar pelos estados com maior volume de votos de terceiros (estoque em disputa)
df_estados = df_estados.sort_values(by='Estoque Outros (1ºT)', ascending=False)

print("\n📊 RESUMO ESTATÍSTICO POR ESTADO (UF):")
print(df_estados.to_string(index=False))

# Salvar o resumo em CSV para uso na documentação ou no Streamlit
caminho_saida = diretorio_atual.parent / "dados" / "correlacao_estados_2026.csv"
df_estados.to_csv(caminho_saida, sep=';', encoding='latin1', index=False)
print(f"\n✅ Relatório estadual salvo em: {caminho_saida}")