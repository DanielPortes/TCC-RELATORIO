"""Cobertura de PM2,5 e de variáveis meteorológicas nas 38 estações da rede FEAM (números citados na Introdução)."""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT.parent / "TCC-wsl" / "data" / "OUTRAS_USINAS"
MET = ["Temperatura", "Umidade Relativa", "Velocidade do Vento", "Direcao do Vento",
       "Precipitacao", "Radiacao Solar", "Pressao Atmosferica"]

rows = []
for path in sorted(DATA.glob("consolidado-*.csv")):
    df = pd.read_csv(path, low_memory=False)
    pm25 = pd.to_numeric(df["PM2.5"], errors="coerce").notna().mean() if "PM2.5" in df else 0.0
    met = {c: pd.to_numeric(df[c], errors="coerce").notna().mean() for c in MET if c in df}
    rows.append({"estacao": path.stem.removeprefix("consolidado-"), "pm25_medido": pm25,
                 "maior_cobertura_meteo": max(met.values(), default=0.0)})
out = pd.DataFrame(rows)
out.to_csv(ROOT / "artefatos" / "cobertura_rede_feam.csv", index=False)
print(f"estações: {len(out)}")
print(f"sem nenhuma medição meteorológica: {(out.maior_cobertura_meteo == 0).sum()}")
print(f"PM2,5 medido em menos de 80% das horas: {(out.pm25_medido < 0.8).sum()}")
