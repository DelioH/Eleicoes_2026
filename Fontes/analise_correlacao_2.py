import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
#Importado numpy para resolver os casos em que o candidato ficou com resultado 0 para que ao tentar calcular o crescimento do candidato, não se use os dados = 0, pois desta não forma não consigo saber a media.
import numpy as np
import matplotlib.pyplot as plt

base = Path(__file__).parent.parent / "dados"

df = pd.read_csv(
    base / "base_correlacao_2026.csv",
    sep=";",
    encoding="latin1"
)

# Entendendo a correlação dos ganhos dos candidatos com os votos dos candidatos que perderam o primeiro turno
corr_outros_cand1 = (
    df["Outros_T1"]
    .corr(df["GanhoCandidato1"])
)

corr_outros_cand2 = (
    df["Outros_T1"]
    .corr(df["GanhoCandidato2"])
)

print("\n=== ORIGEM DOS VOTOS: OUTROS CANDIDATOS ===")

print(
    f"\nOutros_T1 x GanhoCandidato1: "
    f"{corr_outros_cand1:.10f}"
)

print(
    f"\nOutros_T1 x GanhoCandidato2: "
    f"{corr_outros_cand2:.10f}"
)

# Entendendo a associação dos votos dos outros candidatos para os candidatos que ficaram para o segundo turno.

df["AssociacaoOutros_Candidato1"] = (
    df["GanhoCandidato1"] /
    df["Outros_T1"]
)

df["AssociacaoOutros_Candidato2"] = (
    df["GanhoCandidato2"] /
    df["Outros_T1"]
)

print(
    df["AssociacaoOutros_Candidato1"]
    .describe()
)

print(
    df["AssociacaoOutros_Candidato2"]
    .describe()
)