import json
import pandas as pd
from pathlib import Path
import logging

RAW_DIR = Path("data/raw")
TRATADA_DIR = Path("data/tratada")

def carregar_raw() -> dict:
    """Carrega o JSON bruto mais recente."""

    arquivos = sorted(RAW_DIR.glob("*.json"))

    if not arquivos:
        raise FileNotFoundError("Nenhum arquivo encontrado em data/raw.")

    ultimo = arquivos[-1]

    with open(ultimo, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def transformar(dados: dict) -> pd.DataFrame:
    """Transforma o JSON em DataFrame."""

    linhas = []

    for codigo, info in dados.items():
        linhas.append(info)

    return pd.DataFrame(linhas)

def salvar_tratada(df: pd.DataFrame) -> Path:
    """Salva o DataFrame em CSV."""

    TRATADA_DIR.mkdir(parents=True, exist_ok=True)

    caminho = TRATADA_DIR / "cotacoes.csv"

    df.to_csv(caminho, index=False)

    return caminho


if __name__ == "__main__":
    dados = carregar_raw()
    df = transformar(dados)
    caminho = salvar_tratada(df)

    print(df)
    print(f"\nArquivo salvo em: {caminho}")

