import pandas as pd
from pathlib import Path

base = Path(__file__).parent.parent / "dados"

df = pd.read_csv(
    base / "votacao_agrupada_2026.csv",
    sep=";",
    encoding="latin1"
)

# Descobre automaticamente os finalistas
finalistas = (
    df[
        (df["NR_TURNO"] == 2)
        & (~df["NM_VOTAVEL"].isin(["VOTO BRANCO", "VOTO NULO"]))
    ]["NM_VOTAVEL"]
    .unique()
)

finalistas = sorted(finalistas)

cand1 = finalistas[0]
cand2 = finalistas[1]

linhas = []

for (uf, municipio), grupo in df.groupby(["SG_UF", "NM_MUNICIPIO"]):

    t1 = grupo[grupo["NR_TURNO"] == 1]
    t2 = grupo[grupo["NR_TURNO"] == 2]

    candidato1_t1 = t1.loc[
        t1["NM_VOTAVEL"] == cand1,
        "QT_VOTOS"
    ].sum()

    candidato2_t1 = t1.loc[
        t1["NM_VOTAVEL"] == cand2,
        "QT_VOTOS"
    ].sum()

    outros_t1 = t1.loc[
        ~t1["NM_VOTAVEL"].isin(
            [cand1, cand2, "VOTO BRANCO", "VOTO NULO"]
        ),
        "QT_VOTOS"
    ].sum()

    brancosnulos_t1 = t1.loc[
        t1["NM_VOTAVEL"].isin(
            ["VOTO BRANCO", "VOTO NULO"]
        ),
        "QT_VOTOS"
    ].sum()

    candidato1_t2 = t2.loc[
        t2["NM_VOTAVEL"] == cand1,
        "QT_VOTOS"
    ].sum()

    candidato2_t2 = t2.loc[
        t2["NM_VOTAVEL"] == cand2,
        "QT_VOTOS"
    ].sum()

    brancosnulos_t2 = t2.loc[
        t2["NM_VOTAVEL"].isin(
            ["VOTO BRANCO", "VOTO NULO"]
        ),
        "QT_VOTOS"
    ].sum()

    votantes_t1 = (
        candidato1_t1 +
        candidato2_t1 +
        outros_t1 +
        brancosnulos_t1
    )

    votantes_t2 = (
        candidato1_t2 +
        candidato2_t2 +
        brancosnulos_t2
    )

    ganho_candidato1 = candidato1_t2 - candidato1_t1
    ganho_candidato2 = candidato2_t2 - candidato2_t1

    var_votantes = votantes_t2 - votantes_t1

    var_votantes_perc = (
        var_votantes / votantes_t1 * 100
        if votantes_t1 > 0
        else 0
    )

    linhas.append({
        "SG_UF": uf,
        "NM_MUNICIPIO": municipio,

        "Candidato1_T1": candidato1_t1,
        "Candidato2_T1": candidato2_t1,
        "Outros_T1": outros_t1,
        "BrancosNulos_T1": brancosnulos_t1,

        "Votantes_T1": votantes_t1,

        "Candidato1_T2": candidato1_t2,
        "Candidato2_T2": candidato2_t2,
        "BrancosNulos_T2": brancosnulos_t2,

        "Votantes_T2": votantes_t2,

        "GanhoCandidato1": ganho_candidato1,
        "GanhoCandidato2": ganho_candidato2,

        "Var_Votantes": var_votantes,
        "Var_Votantes_Perc": round(var_votantes_perc, 2)
    })

df_correlacao = pd.DataFrame(linhas)

df_correlacao.to_csv(
    base / "base_correlacao_2026.csv",
    sep=";",
    encoding="latin1",
    index=False
)

print(df_correlacao.head())
print(f"\nTotal de municípios: {len(df_correlacao)}")