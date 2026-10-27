import pandas as pd
from pathlib import Path

base = Path(__file__).parent.parent / "dados"

df = pd.read_csv(
    base / "votacao_agrupada_2026.csv",
    sep=";",
    encoding="latin1"
)

print("\n=== RESUMO GERAL DA ELEIÇÃO ===")

# Total de votos por turno
totais_turno = df.groupby("NR_TURNO")["QT_VOTOS"].sum()

# Votos brancos e nulos por turno
invalidos = (
    df[df["NM_VOTAVEL"].isin(["VOTO BRANCO", "VOTO NULO"])]
    .groupby(["NR_TURNO", "NM_VOTAVEL"])["QT_VOTOS"]
    .sum()
    .unstack(fill_value=0)
)

for turno in sorted(df["NR_TURNO"].unique()):

    total = totais_turno.get(turno, 0)

    brancos = invalidos.loc[turno, "VOTO BRANCO"] \
        if "VOTO BRANCO" in invalidos.columns else 0

    nulos = invalidos.loc[turno, "VOTO NULO"] \
        if "VOTO NULO" in invalidos.columns else 0

    print(f"""
{turno}º TURNO
  Total de votos: {total:,}
  Votos brancos: {brancos:,}
  Votos nulos:   {nulos:,}
  Brancos + Nulos: {(brancos + nulos):,}
""".replace(",", "."))

# Votação dos candidatos
resumo = (
    df[~df["NM_VOTAVEL"].isin(["VOTO BRANCO", "VOTO NULO"])]
    .groupby(["NM_VOTAVEL", "NR_TURNO"])["QT_VOTOS"]
    .sum()
    .unstack(fill_value=0)
    .reset_index()
)

resumo.columns = ["CANDIDATO", "VOTOS_1T", "VOTOS_2T"]
resumo["DIFERENCA"] = resumo["VOTOS_2T"] - resumo["VOTOS_1T"]

print("\n=== VOTAÇÃO DOS CANDIDATOS ===")

for _, linha in resumo.iterrows():

    sinal = "+" if linha["DIFERENCA"] >= 0 else ""

    print(f"""
{linha['CANDIDATO']}
  1º Turno: {linha['VOTOS_1T']:,}
  2º Turno: {linha['VOTOS_2T']:,}
  Diferença: {sinal}{linha['DIFERENCA']:,}
""".replace(",", "."))