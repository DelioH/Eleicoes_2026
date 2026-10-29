import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
#Importado numpy para resolver os casos em que o candidato ficou com resultado 0 para que ao tentar calcular o crescimento do candidato, não se use os dados = 0, pois desta não forma não consigo saber a media.
import numpy as np

base = Path(__file__).parent.parent / "dados"

df = pd.read_csv(
    base / "base_correlacao_2026.csv",
    sep=";",
    encoding="latin1"
)

corr_cand1 = df["Candidato1_T1"].corr(df["Candidato1_T2"])

corr_cand2 = df["Candidato2_T1"].corr(df["Candidato2_T2"])

print("=== ESTABILIDADE ELEITORAL ===")

print(f"\nCorrelação Candidato 1:")
print(f"{corr_cand1:.10f}")

print(f"\nCorrelação Candidato 2:")
print(f"{corr_cand2:.10f}")

#Verificando a correlação dos ganhos
corr_ganhos_cand1 = df["GanhoCandidato1"].corr(df["Candidato1_T1"])
corr_ganhos_cand2 = df["GanhoCandidato2"].corr(df["Candidato2_T1"])

print("=== CORRELAÇÃO DOS GANHOS ===")
print(f"\nCorrelação Ganhos Candidato 1:")
print(f"{corr_ganhos_cand1:.10f}")

print(f"\nCorrelação Ganhos Candidato 2:")
print(f"{corr_ganhos_cand2:.10f}")

#Criando variáveis de crescimento com o percentual de cada candidato
df["CrescimentoPerc_Candidato1"] = np.where(
    df["Candidato1_T1"] > 0,
    (df["GanhoCandidato1"] / df["Candidato1_T1"]) * 100,
    np.nan
)

df["CrescimentoPerc_Candidato2"] = (
    df["GanhoCandidato2"]
    / df["Candidato2_T1"]
) * 100

#Agora exibindo as medidas analíticas
print("Crescimento do Candidato 1")
print(df["CrescimentoPerc_Candidato1"].describe())
print("Crescimento do Candidato 2")
print(df["CrescimentoPerc_Candidato2"].describe())

#Geração de gráfico de dispersão
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Candidato 1
axs[0].scatter(
    df["Candidato1_T1"],
    df["Candidato1_T2"],
    alpha=0.4
)

axs[0].set_title("Candidato 1")
axs[0].set_xlabel("1º Turno")
axs[0].set_ylabel("2º Turno")

# Candidato 2
axs[1].scatter(
    df["Candidato2_T1"],
    df["Candidato2_T2"],
    alpha=0.4
)

axs[1].set_title("Candidato 2")
axs[1].set_xlabel("1º Turno")
axs[1].set_ylabel("2º Turno")

plt.tight_layout()
plt.show()