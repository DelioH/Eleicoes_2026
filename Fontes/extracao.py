import pandas as pd
from pathlib import Path

def extrair_dados_tse(nome_arquivo):
    caminho = Path(__file__).parent.parent / "dados" / nome_arquivo
    return pd.read_csv(caminho, sep=";", encoding="latin1")

if __name__ == "__main__":
    df = extrair_dados_tse("votacao_secao_2026_BR.csv")
# Mostrar as primeiras linhas
    print(df.head())
# Mostra todas as colunas
    print(df.columns.tolist())
# Quantidade de linhas
    print("Quantidade de registros:")
    print(len(df))