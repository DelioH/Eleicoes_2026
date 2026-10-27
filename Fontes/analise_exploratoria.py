import pandas as pd
from pathlib import Path

base = Path(__file__).parent.parent / "dados"

df = pd.read_csv(
    base / "votacao_agrupada_2026.csv",
    sep=";",
    encoding="latin1"
)

# TOP 5 cidades com mais votos nulos/brancos
print("3. Incidência de Votos Inválidos: Em quais cinco municípios ocorreu a maior proporção de votos brancos e nulos, indicando menor engajamento direto com as chapas finalistas?")
invalidos = (
    df[df["NM_VOTAVEL"].isin(["VOTO BRANCO", "VOTO NULO"])]
    .groupby(["NR_TURNO", "SG_UF", "NM_MUNICIPIO"], as_index=False)["QT_VOTOS"]
    .sum()
)

for turno in [1, 2]:
    ranking = (
        invalidos[invalidos["NR_TURNO"] == turno]
        .sort_values("QT_VOTOS", ascending=False)
        .head(5)
    )

    print(f"\nTop 5 Nulos/Brancos - {turno}º Turno")
    print(ranking[["SG_UF", "NM_MUNICIPIO", "QT_VOTOS"]].to_string(index=False))


# Variação de engajamento
print("2. Variação de Engajamento: Quais cinco cidades apresentaram a maior variação absoluta no total de votos registrados (crescimento ou queda) entre o primeiro e o segundo turno?")
engajamento = (
    df.groupby(["SG_UF", "NM_MUNICIPIO", "NR_TURNO"], as_index=False)["QT_VOTOS"]
    .sum()
    .pivot(
        index=["SG_UF", "NM_MUNICIPIO"],
        columns="NR_TURNO",
        values="QT_VOTOS"
    )
    .reset_index()
)

engajamento.columns = ["SG_UF", "NM_MUNICIPIO", "VOTOS_1T", "VOTOS_2T"]
engajamento["VARIACAO"] = engajamento["VOTOS_2T"] - engajamento["VOTOS_1T"]

print("\nMaiores quedas:")
print(engajamento.sort_values("VARIACAO").head(5).to_string(index=False))

print("\nMaiores aumentos:")
print(engajamento.sort_values("VARIACAO", ascending=False).head(5).to_string(index=False))

# Questão: 1. Vantagem Proporcional: Quais são os cinco municípios onde cada um dos dois candidatos finalistas obteve a maior margem percentual de votos?
# Vantagem proporcional no 2º turno
print("1. Vantagem Proporcional: Quais são os cinco municípios onde cada um dos dois candidatos finalistas obteve a maior margem percentual de votos?")
df_2t = df[
    (df["NR_TURNO"] == 2)
    & (~df["NM_VOTAVEL"].isin(["VOTO BRANCO", "VOTO NULO"]))
]

finalistas = df_2t["NM_VOTAVEL"].unique()

validos = (
    df_2t.groupby(["SG_UF", "NM_MUNICIPIO"], as_index=False)["QT_VOTOS"]
    .sum()
    .rename(columns={"QT_VOTOS": "VOTOS_VALIDOS"})
)

vantagem = pd.merge(
    df_2t,
    validos,
    on=["SG_UF", "NM_MUNICIPIO"]
)

vantagem["PERCENTUAL"] = (
    vantagem["QT_VOTOS"] / vantagem["VOTOS_VALIDOS"] * 100
)

for candidato in finalistas:
    ranking = (
        vantagem[vantagem["NM_VOTAVEL"] == candidato]
        .sort_values("PERCENTUAL", ascending=False)
        .head(5)
    )

    print(f"\nTop 5 cidades de {candidato}")
    print(
        ranking[
            ["SG_UF", "NM_MUNICIPIO", "PERCENTUAL", "QT_VOTOS", "VOTOS_VALIDOS"]
        ].to_string(index=False)
    )