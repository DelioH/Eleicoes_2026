import pandas as pd
from pathlib import Path

base = Path(__file__).parent.parent / "dados"

df = pd.read_csv(
    base / "votacao_agrupada_2026.csv",
    sep=";",
    encoding="latin1"
)

# Descobrir automaticamente os finalistas
finalistas = (
    df[
        (df["NR_TURNO"] == 2)
        & (~df["NM_VOTAVEL"].isin(["VOTO BRANCO", "VOTO NULO"]))
    ]["NM_VOTAVEL"]
    .unique()
)

cand1 = finalistas[0]
cand2 = finalistas[1]

linhas = []

for (uf, cod, municipio), grupo in df.groupby(
    ["SG_UF", "CD_MUNICIPIO", "NM_MUNICIPIO"]
):

    linha = {
        "SG_UF": uf,
        "CD_MUNICIPIO": cod,
        "NM_MUNICIPIO": municipio
    }

    # ---------- 1º turno ----------

    df_1t = grupo[grupo["NR_TURNO"] == 1]

    linha["CAND1_1T"] = df_1t.loc[
        df_1t["NM_VOTAVEL"] == cand1,
        "QT_VOTOS"
    ].sum()

    linha["CAND2_1T"] = df_1t.loc[
        df_1t["NM_VOTAVEL"] == cand2,
        "QT_VOTOS"
    ].sum()

    linha["BRANCOS_1T"] = df_1t.loc[
        df_1t["NM_VOTAVEL"] == "VOTO BRANCO",
        "QT_VOTOS"
    ].sum()

    linha["NULOS_1T"] = df_1t.loc[
        df_1t["NM_VOTAVEL"] == "VOTO NULO",
        "QT_VOTOS"
    ].sum()

    linha["OUTROS_1T"] = df_1t.loc[
        ~df_1t["NM_VOTAVEL"].isin(
            [cand1, cand2, "VOTO BRANCO", "VOTO NULO"]
        ),
        "QT_VOTOS"
    ].sum()

    linha["TOTAL_1T"] = df_1t["QT_VOTOS"].sum()

    # ---------- 2º turno ----------

    df_2t = grupo[grupo["NR_TURNO"] == 2]

    linha["CAND1_2T"] = df_2t.loc[
        df_2t["NM_VOTAVEL"] == cand1,
        "QT_VOTOS"
    ].sum()

    linha["CAND2_2T"] = df_2t.loc[
        df_2t["NM_VOTAVEL"] == cand2,
        "QT_VOTOS"
    ].sum()

    linha["BRANCOS_2T"] = df_2t.loc[
        df_2t["NM_VOTAVEL"] == "VOTO BRANCO",
        "QT_VOTOS"
    ].sum()

    linha["NULOS_2T"] = df_2t.loc[
        df_2t["NM_VOTAVEL"] == "VOTO NULO",
        "QT_VOTOS"
    ].sum()

    linha["TOTAL_2T"] = df_2t["QT_VOTOS"].sum()

    # ---------- métricas derivadas ----------

    linha["GANHO_CAND1"] = (
        linha["CAND1_2T"] - linha["CAND1_1T"]
    )

    linha["GANHO_CAND2"] = (
        linha["CAND2_2T"] - linha["CAND2_1T"]
    )

    linha["VAR_COMPARECIMENTO"] = (
        linha["TOTAL_2T"] - linha["TOTAL_1T"]
    )

    linhas.append(linha)

df_correlacao = pd.DataFrame(linhas)

df_correlacao.to_csv(
    base / "base_correlacao_2026.csv",
    sep=";",
    encoding="latin1",
    index=False
)

print(df_correlacao.head())