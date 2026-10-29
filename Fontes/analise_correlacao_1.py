import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

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
print(f"{corr_cand1:.4f}")

print(f"\nCorrelação Candidato 2:")
print(f"{corr_cand2:.4f}")

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