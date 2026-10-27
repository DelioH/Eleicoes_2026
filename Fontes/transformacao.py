import pandas as pd
from pathlib import Path

def transformar_dados():
    base = Path(__file__).parent.parent / "dados"
# Utilizadas somente as colunas que farão mais sentido na análise
    df = pd.read_csv(
        base / "votacao_secao_2026_BR.csv",
        sep=";",
        encoding="latin1",
        usecols=[
            "NR_TURNO",
            "SG_UF",
            "CD_MUNICIPIO",
            "NM_MUNICIPIO",
            "DS_CARGO",
            "NM_VOTAVEL",
            "QT_VOTOS",
        ],
    )
# Filtradas as colunas para trazer somente os resultados de presidente e agrupadas  por:
# Turno das eleições, Estado, Código município e nome do município e nome do candidato.
# No agrupamento, somar a coluna QT_VOTOS
    df = (
        df[df["DS_CARGO"] == "Presidente"]
        .groupby(
            ["NR_TURNO", "SG_UF", "CD_MUNICIPIO", "NM_MUNICIPIO", "NM_VOTAVEL"],
            as_index=False,
        )["QT_VOTOS"]
        .sum()
    )
# Criando um arquivo com os dados agrupados.
    df.to_csv(
        base / "votacao_agrupada_2026.csv",
        sep=";",
        encoding="latin1",
        index=False,
    )
# Avaliar resultado
    print(df.head())
# Quantidade de linhas
    print("Quantidade de registros:")
    print(len(df))

if __name__ == "__main__":
    transformar_dados()