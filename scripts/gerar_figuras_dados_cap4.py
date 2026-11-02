"""Figuras e números da descrição dos dados (Capítulo 4).

Gera, a partir do conjunto de dados final do protocolo e do arquivo bruto da estação:

* ``serie_pm25_sapo_2017_2023``: série horária de PM2,5 (2017 a 2023) com a média diária;
* ``eda_sapo_cobertura_lacunas``: cobertura mensal de PM2,5 por bloco cronológico e maiores lacunas (em horas);
* ``serie_temporal_componentes_sapo``: decomposição aditiva calculada só com horas medidas de 2017 a 2020,
  mostrada em um trecho do treino;
* ``artefatos/dados_cap4_resumo.json``: cobertura das colunas do arquivo, estatísticas descritivas,
  participação de cada componente na variância e maiores lacunas.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TCC_WSL = ROOT.parent / "TCC-wsl"
FIG_DIR = ROOT / "figuras"
ART_DIR = ROOT / "artefatos"
DATASET_PATH = TCC_WSL / "runtime/reports/thesis_protocol/datasets/clean_pm10_decoder_proxy.parquet"
RAW_CSV = TCC_WSL / "data/OUTRAS_USINAS/consolidado-conceicao-do-mato-dentro-sapo.csv"

TRAIN_END = pd.Timestamp("2019-10-21 14:30:00")
VAL_END = pd.Timestamp("2020-05-27 06:30:00")
FINAL_TEST_START = pd.Timestamp("2021-01-01 00:00:00")

BLOCKS = ["treino", "validação", "teste preliminar", "teste final"]
COLORS = {
    "treino": "#4C72B0",
    "validação": "#E08A2E",
    "teste preliminar": "#C44E52",
    "teste final": "#55A868",
}

plt.rcParams.update(
    {
        "font.size": 10.5,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "savefig.facecolor": "white",
    }
)


def save(fig: plt.Figure, name: str) -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / f"{name}.png", dpi=300, bbox_inches="tight", pad_inches=0.12)
    fig.savefig(FIG_DIR / f"{name}.pdf", bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)


def block_of(ts: pd.Series) -> pd.Series:
    out = pd.Series("teste final", index=ts.index)
    out[ts < FINAL_TEST_START] = "teste preliminar"
    out[ts < VAL_END] = "validação"
    out[ts < TRAIN_END] = "treino"
    return out


def load_dataset() -> pd.DataFrame:
    df = pd.read_parquet(DATASET_PATH)
    df["Data e Hora"] = pd.to_datetime(df["Data e Hora"])
    df = df.sort_values("Data e Hora").set_index("Data e Hora")
    df["observado"] = df["PM2.5__miss"].astype(float).eq(0)
    df["bloco"] = block_of(pd.Series(df.index, index=df.index))
    return df


def raw_column_coverage() -> dict:
    raw = pd.read_csv(RAW_CSV, low_memory=False)
    raw = raw.drop_duplicates(subset=["Data e Hora"], keep="last")
    meta = {"Municipio", "Estacao", "Ano", "Arquivo Origem", "Data e Hora"}
    value_cols = [c for c in raw.columns if c not in meta]
    coverage = {c: float(pd.to_numeric(raw[c], errors="coerce").notna().mean() * 100) for c in value_cols}
    pm25 = pd.to_numeric(raw["PM2.5"], errors="coerce")
    pm10 = pd.to_numeric(raw["PM10"], errors="coerce")
    pts = pd.to_numeric(raw["PTS"], errors="coerce")
    stats = {}
    for name, s in (("PM2.5", pm25), ("PM10", pm10), ("PTS", pts)):
        d = s.describe()
        stats[name] = {k: float(d[k]) for k in ("count", "mean", "std", "min", "25%", "50%", "75%", "max")}
    return {
        "linhas": int(len(raw)),
        "inicio": str(raw["Data e Hora"].min()),
        "fim": str(raw["Data e Hora"].max()),
        "colunas_de_medicao": len(value_cols),
        "colunas_vazias": int(sum(v == 0 for v in coverage.values())),
        "cobertura_pct": {k: v for k, v in coverage.items() if v > 0},
        "estatisticas": stats,
        "corr_pts_pm10": float(pts.corr(pm10)),
        "corr_pts_pm25": float(pts.corr(pm25)),
        "corr_pm10_pm25": float(pm10.corr(pm25)),
        "frac_pts_menor_que_pm10": float((pts < pm10)[pts.notna() & pm10.notna()].mean()),
    }


def gap_runs(df: pd.DataFrame) -> pd.DataFrame:
    miss = (~df["observado"]).astype(int)
    run_id = (miss.diff().fillna(0) != 0).cumsum()
    rows = []
    for _, g in df[miss == 1].groupby(run_id[miss == 1]):
        rows.append({"inicio": g.index.min(), "fim": g.index.max(), "horas": len(g), "bloco": g["bloco"].mode().iat[0]})
    return pd.DataFrame(rows).sort_values("horas", ascending=False).reset_index(drop=True)


def plot_series(df: pd.DataFrame) -> None:
    y = df["PM2.5"].where(df["observado"])
    daily = y.resample("D").mean()
    fig, ax = plt.subplots(figsize=(12, 3.6))
    ax.plot(y.index, y.values, color="#9DB4D8", linewidth=0.35, label="valor horário medido")
    ax.plot(daily.index, daily.values, color="#1F3B73", linewidth=0.9, label="média diária")
    ax.axhline(35, color="#C44E52", linestyle="--", linewidth=0.9, label="35 µg/m³")
    ax.set_ylabel("PM2,5 (µg/m³)")
    ax.set_xlim(pd.Timestamp("2017-01-01"), pd.Timestamp("2024-01-01"))
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.legend(loc="upper right", frameon=False, ncol=3, fontsize=9.5)
    save(fig, "serie_pm25_sapo_2017_2023")


def plot_coverage(df: pd.DataFrame, gaps: pd.DataFrame) -> None:
    monthly = df.groupby(pd.Grouper(freq="MS")).agg(
        cobertura=("observado", lambda s: 100 * s.mean()),
        bloco=("bloco", lambda s: s.mode().iat[0]),
    )
    fig, axes = plt.subplots(2, 1, figsize=(12, 6.6), gridspec_kw={"height_ratios": [1.35, 1], "hspace": 0.45})
    ax = axes[0]
    ax.bar(monthly.index, monthly["cobertura"], width=25, color=[COLORS[b] for b in monthly["bloco"]], align="edge")
    ax.axhline(80, color="gray", linestyle="--", linewidth=0.9)
    ax.set_ylabel("Horas medidas (%)")
    ax.set_ylim(0, 105)
    ax.set_title("Cobertura mensal de PM2,5 na estação Sapo", fontsize=11.5, weight="bold")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    handles = [plt.Rectangle((0, 0), 1, 1, color=COLORS[b]) for b in BLOCKS]
    handles.append(plt.Line2D([0], [0], color="gray", linestyle="--"))
    ax.legend(handles, [*BLOCKS, "80% das horas"], loc="lower center", bbox_to_anchor=(0.5, -0.32), ncol=5, frameon=False, fontsize=9.5)

    ax = axes[1]
    top = gaps.head(8).iloc[::-1]
    labels = [f"{a:%d/%m/%Y} a {b:%d/%m/%Y}" for a, b in zip(top["inicio"], top["fim"])]
    ax.barh(labels, top["horas"], color=[COLORS[b] for b in top["bloco"]])
    for i, h in enumerate(top["horas"]):
        ax.text(h + 8, i, f"{h} h", va="center", fontsize=9)
    ax.set_xlabel("Duração da lacuna (horas)")
    ax.set_title("Maiores lacunas de PM2,5 no conjunto de dados", fontsize=11.5, weight="bold")
    ax.set_xlim(0, top["horas"].max() * 1.12)
    ax.grid(axis="y", alpha=0)
    save(fig, "eda_sapo_cobertura_lacunas")


def decomposition(df: pd.DataFrame) -> dict:
    dev = df[df.index < FINAL_TEST_START]
    y = dev["PM2.5"].where(dev["observado"])
    trend = y.rolling(24 * 7, center=True, min_periods=24).mean()
    detrended = y - trend
    profile = detrended.groupby(dev.index.hour).mean()
    seasonal = pd.Series(dev.index.hour, index=dev.index).map(profile).astype(float)
    resid = y - trend - seasonal
    ok = y.notna() & trend.notna()
    var_y = y[ok].var()
    shares = {
        "tendencia": float(trend[ok].var() / var_y),
        "padrao_horario": float(seasonal[ok].var() / var_y),
        "residuo": float(resid[ok].var() / var_y),
        "amplitude_padrao_horario": float(profile.max() - profile.min()),
        "hora_min": int(profile.idxmin()),
        "hora_max": int(profile.idxmax()),
    }

    start, end = pd.Timestamp("2019-06-01"), pd.Timestamp("2019-09-30 23:59")
    sl = slice(start, end)
    fig, axes = plt.subplots(4, 1, figsize=(12, 8.0), sharex=True, gridspec_kw={"hspace": 0.18})
    panels = [
        (y[sl], "Série medida", "#1F3B73"),
        (trend[sl], "Tendência\n(média móvel de 7 dias)", "#2E8B57"),
        (seasonal[sl], "Padrão horário", "#E08A2E"),
        (resid[sl], "Resíduo", "#7B4FC9"),
    ]
    for ax, (s, label, color) in zip(axes, panels):
        ax.plot(s.index, s.values, color=color, linewidth=0.9)
        ax.set_ylabel(label, fontsize=9.5)
    axes[3].axhline(0, color="black", linewidth=0.6, linestyle="--")
    axes[0].set_title(
        "Decomposição aditiva do PM2,5 (µg/m³) — trecho de jun. a set. de 2019, no treino",
        fontsize=11.5, weight="bold",
    )
    axes[3].xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
    save(fig, "serie_temporal_componentes_sapo")
    return shares


def main() -> None:
    df = load_dataset()
    gaps = gap_runs(df)
    plot_series(df)
    plot_coverage(df, gaps)
    shares = decomposition(df)
    summary = {
        "conjunto": {
            "linhas": int(len(df)),
            "inicio": str(df.index.min()),
            "fim": str(df.index.max()),
            "pm25_medido_pct": float(df["observado"].mean() * 100),
            "horas_por_bloco": df["bloco"].value_counts().reindex(BLOCKS).astype(int).to_dict(),
        },
        "arquivo_bruto": raw_column_coverage(),
        "decomposicao_2017_2020": shares,
        "maiores_lacunas": [
            {"inicio": str(r.inicio), "fim": str(r.fim), "horas": int(r.horas), "bloco": r.bloco}
            for r in gaps.head(8).itertuples()
        ],
        "maior_trecho_continuo_h": int(
            df["observado"].astype(int).groupby((~df["observado"]).cumsum()).sum().max()
        ),
    }
    ART_DIR.mkdir(parents=True, exist_ok=True)
    (ART_DIR / "dados_cap4_resumo.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
