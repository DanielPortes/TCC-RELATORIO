from __future__ import annotations

import json
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
TECH_ROOT = ROOT.parent / "TCC-wsl"
FIG_DIR = ROOT / "figuras"
ART_DIR = ROOT / "artefatos"

DATASET_PATH = (
    TECH_ROOT
    / "runtime/reports/sapo_final_pre_delivery_suite_20260510/datasets/clean_pm10_decoder_proxy.parquet"
)
RANKING_PATH = (
    TECH_ROOT
    / "docs/generated/eda_outras_usinas/metricas/usina_pm25_resumo_ranking.csv"
)

TIMELINES = {
    "LSTM direta": (
        TECH_ROOT
        / "runtime/reports/sapo_final_pre_delivery_suite_20260510/artifacts/cv_hpo_lstm_direct_clean_pm10/test_outputs/test_predictions_timeline.csv",
        "#4C78A8",
    ),
    "LSTM recursiva": (
        TECH_ROOT
        / "runtime/reports/sapo_final_pre_delivery_suite_20260510/artifacts/cv_hpo_lstm_recursive_clean_pm10/test_outputs/test_predictions_timeline.csv",
        "#B279A2",
    ),
    "Seq2Seq atenção + L1 ponderada": (
        TECH_ROOT
        / "runtime/reports/sapo_final_pre_delivery_suite_20260510/artifacts/cv_hpo_weighted_l1_clean_pm10/test_outputs/test_predictions_timeline.csv",
        "#54A24B",
    ),
    "XGBoost": (
        TECH_ROOT
        / "runtime/reports/sapo_final_pre_delivery_suite_20260510/artifacts/cv_hpo_xgboost_clean_pm10/test_outputs/test_predictions_timeline.csv",
        "#F58518",
    ),
}

HORIZON_FILES = {
    "LSTM direta": (
        TECH_ROOT
        / "runtime/reports/sapo_final_pre_delivery_suite_20260510/artifacts/cv_hpo_lstm_direct_clean_pm10/test_outputs/per_horizon_metrics.csv",
        "#4C78A8",
    ),
    "LSTM recursiva": (
        TECH_ROOT
        / "runtime/reports/sapo_final_pre_delivery_suite_20260510/artifacts/cv_hpo_lstm_recursive_clean_pm10/test_outputs/per_horizon_metrics.csv",
        "#B279A2",
    ),
    "Seq2Seq atenção + L1 ponderada": (
        TECH_ROOT
        / "runtime/reports/sapo_final_pre_delivery_suite_20260510/artifacts/cv_hpo_weighted_l1_clean_pm10/test_outputs/per_horizon_metrics.csv",
        "#54A24B",
    ),
    "XGBoost": (
        TECH_ROOT
        / "runtime/reports/sapo_final_pre_delivery_suite_20260510/artifacts/cv_hpo_xgboost_clean_pm10/test_outputs/per_horizon_metrics.csv",
        "#F58518",
    ),
}
# TODO(resultados): incluir Seq2Seq básico e Seq2Seq atenção canônica nas figuras
# quando forem reexecutados no mesmo protocolo final dos demais modelos.

COLORS = {
    "train": "#2563eb",
    "val": "#d97706",
    "test": "#059669",
    "ink": "#1f2937",
    "muted": "#64748b",
    "grid": "#e5e7eb",
    "threshold": "#8b8b8b",
    "sapo": "#d97706",
    "other": "#94a3b8",
}

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "axes.edgecolor": "#111827",
        "axes.labelcolor": "#111827",
        "xtick.color": "#111827",
        "ytick.color": "#111827",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    }
)


def save(fig: plt.Figure, name: str) -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / f"{name}.png", dpi=300, bbox_inches="tight", pad_inches=0.18)
    fig.savefig(FIG_DIR / f"{name}.pdf", bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)


def assign_splits(df: pd.DataFrame) -> pd.DataFrame:
    out = df.sort_values("Data e Hora").reset_index(drop=True).copy()
    n = len(out)
    val_n = int(n * 0.15)
    test_n = int(n * 0.15)
    train_n = n - val_n - test_n
    split = np.array(["train"] * train_n + ["val"] * val_n + ["test"] * test_n)
    out["split"] = split
    return out


def load_dataset() -> pd.DataFrame:
    df = pd.read_parquet(DATASET_PATH)
    df["Data e Hora"] = pd.to_datetime(df["Data e Hora"])
    return assign_splits(df)


def split_summary(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for split, g in df.groupby("split", sort=False):
        obs = g["PM2.5__miss"].eq(0)
        observed = g.loc[obs, "PM2.5"]
        rows.append(
            {
                "split": split,
                "inicio": g["Data e Hora"].min(),
                "fim": g["Data e Hora"].max(),
                "timestamps": len(g),
                "pm25_observado_pct": 100 * obs.mean(),
                "pm25_missing_pct": 100 * (1 - obs.mean()),
                "pm10_observado_pct": 100 * g["PM10__miss"].eq(0).mean(),
                "pm25_media_obs": observed.mean(),
                "pm25_mediana_obs": observed.median(),
                "pm25_p95_obs": observed.quantile(0.95),
                "pm25_p99_obs": observed.quantile(0.99),
                "pm25_eventos_ge35_pct": 100 * observed.ge(35).mean(),
            }
        )
    return pd.DataFrame(rows)


def gap_runs(df: pd.DataFrame, flag_col: str = "PM2.5__miss") -> pd.DataFrame:
    work = df[["Data e Hora", flag_col, "split"]].sort_values("Data e Hora").copy()
    work["is_gap"] = work[flag_col].eq(1)
    groups = work["is_gap"].ne(work["is_gap"].shift()).cumsum()
    rows = []
    for _, g in work.groupby(groups):
        if not bool(g["is_gap"].iloc[0]):
            continue
        rows.append(
            {
                "split": g["split"].mode().iat[0],
                "inicio_lacuna": g["Data e Hora"].min(),
                "fim_lacuna": g["Data e Hora"].max(),
                "duracao_h": len(g),
                "duracao_dias": len(g) / 24.0,
            }
        )
    return pd.DataFrame(rows).sort_values("duracao_h", ascending=False).reset_index(drop=True)


def observed_runs(df: pd.DataFrame, flag_col: str = "PM2.5__miss") -> pd.DataFrame:
    work = df[["Data e Hora", flag_col, "split"]].sort_values("Data e Hora").copy()
    work["is_observed"] = work[flag_col].eq(0)
    groups = work["is_observed"].ne(work["is_observed"].shift()).cumsum()
    rows = []
    for _, g in work.groupby(groups):
        if not bool(g["is_observed"].iloc[0]):
            continue
        rows.append(
            {
                "split": g["split"].mode().iat[0],
                "inicio_continuo": g["Data e Hora"].min(),
                "fim_continuo": g["Data e Hora"].max(),
                "duracao_h": len(g),
                "duracao_dias": len(g) / 24.0,
            }
        )
    return pd.DataFrame(rows).sort_values("duracao_h", ascending=False).reset_index(drop=True)


def plot_coverage_and_gaps(df: pd.DataFrame, gaps: pd.DataFrame) -> None:
    monthly = (
        df.assign(month=df["Data e Hora"].dt.to_period("M").dt.to_timestamp())
        .groupby("month")
        .agg(observed_pct=("PM2.5__miss", lambda s: 100 * s.eq(0).mean()), split=("split", lambda s: s.mode().iat[0]))
        .reset_index()
    )

    fig, axes = plt.subplots(2, 1, figsize=(12.2, 7.0), gridspec_kw={"height_ratios": [1.2, 1]})
    ax = axes[0]
    bar_colors = [COLORS[s] for s in monthly["split"]]
    ax.bar(monthly["month"], monthly["observed_pct"], width=24, color=bar_colors, alpha=0.88, edgecolor="white", linewidth=0.8)
    ax.axhline(80, color=COLORS["threshold"], linestyle="--", linewidth=1.4)
    ax.set_title("Cobertura mensal observada de PM2.5 - Sapo", fontsize=13.2, weight="bold")
    ax.set_ylabel("Cobertura observada (%)")
    ax.set_ylim(0, 105)
    ax.grid(axis="y", color=COLORS["grid"], linewidth=0.8)
    legend_handles = [
        Patch(facecolor=COLORS["train"], label="Treino"),
        Patch(facecolor=COLORS["val"], label="Validação"),
        Patch(facecolor=COLORS["test"], label="Teste"),
        Line2D([0], [0], color=COLORS["threshold"], linestyle="--", linewidth=1.4, label="80% de cobertura"),
    ]
    ax.legend(
        handles=legend_handles,
        loc="lower right",
        frameon=True,
        facecolor="white",
        framealpha=0.9,
        edgecolor="white",
        ncol=4,
        fontsize=8.8,
    )
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    for tick in ax.get_xticklabels():
        tick.set_rotation(0)

    ax = axes[1]
    top = gaps.head(6).iloc[::-1].copy()
    labels = [f"{r.inicio_lacuna:%Y-%m-%d} a {r.fim_lacuna:%Y-%m-%d}" for r in top.itertuples()]
    colors = [COLORS[s] for s in top["split"]]
    ax.barh(labels, top["duracao_dias"], color=colors, alpha=0.9)
    ax.set_title("Maiores lacunas originais de PM2.5 no artefato final", fontsize=12.4, weight="bold")
    ax.set_xlabel("Duração da lacuna (dias)")
    ax.grid(axis="x", color=COLORS["grid"], linewidth=0.8)
    for i, value in enumerate(top["duracao_dias"]):
        ax.text(value + 0.15, i, f"{value:.1f}d", va="center", fontsize=9, color=COLORS["ink"])

    fig.tight_layout()
    save(fig, "eda_sapo_cobertura_lacunas")


def plot_distribution(df: pd.DataFrame, summary: pd.DataFrame) -> None:
    observed = df[df["PM2.5__miss"].eq(0)].copy()
    order = ["train", "val", "test"]
    labels = ["Treino", "Validação", "Teste"]
    data = [observed.loc[observed["split"].eq(s), "PM2.5"].dropna() for s in order]

    fig, axes = plt.subplots(1, 2, figsize=(12.3, 4.8), gridspec_kw={"width_ratios": [1.25, 1]})
    ax = axes[0]
    bp = ax.boxplot(data, tick_labels=labels, patch_artist=True, showfliers=False, widths=0.55)
    for patch, s in zip(bp["boxes"], order):
        patch.set_facecolor(COLORS[s])
        patch.set_alpha(0.35)
        patch.set_edgecolor(COLORS[s])
    for median in bp["medians"]:
        median.set_color(COLORS["ink"])
        median.set_linewidth(1.8)
    ax.axhline(35, color=COLORS["threshold"], linestyle="--", linewidth=1.4, label="Limiar 35")
    ax.set_title("Distribuição observada de PM2.5 por partição", fontsize=13.2, weight="bold")
    ax.set_ylabel("PM2.5")
    ax.grid(axis="y", color=COLORS["grid"], linewidth=0.8)
    ax.legend(frameon=False)

    ax = axes[1]
    rates = summary.set_index("split").loc[order, "pm25_eventos_ge35_pct"]
    ax.bar(labels, rates, color=[COLORS[s] for s in order], alpha=0.86)
    ax.set_title("Eventos observados PM2.5 >= 35", fontsize=13.2, weight="bold")
    ax.set_ylabel("% dos pontos observados")
    ax.grid(axis="y", color=COLORS["grid"], linewidth=0.8)
    for i, value in enumerate(rates):
        ax.text(i, value + 0.03, f"{value:.2f}%", ha="center", va="bottom", fontsize=10)

    fig.tight_layout()
    save(fig, "eda_sapo_distribuicao_pm25")


def plot_external_holdout_split(summary: pd.DataFrame) -> None:
    labels = {
        "train": "Treino final",
        "val": "Validação\nde treinamento",
        "test": "Teste final",
    }
    fig, ax = plt.subplots(figsize=(12.2, 3.35))
    y = 0.0
    height = 0.55
    for row in summary.itertuples(index=False):
        start = pd.Timestamp(row.inicio)
        end = pd.Timestamp(row.fim) + pd.Timedelta(hours=1)
        left = mdates.date2num(start)
        width = mdates.date2num(end) - left
        ax.broken_barh(
            [(left, width)],
            (y, height),
            facecolors=COLORS[row.split],
            edgecolors="white",
            linewidth=1.2,
            alpha=0.86,
        )
        ax.text(
            left + width / 2,
            y + height / 2,
            f"{labels[row.split]}\n{int(row.timestamps):,}".replace(",", "."),
            ha="center",
            va="center",
            color="white",
            fontsize=10.6,
            weight="bold",
            linespacing=1.05,
        )

    ax.set_title("Divisão cronológica externa 70/15/15 - Sapo", fontsize=14.0, weight="bold")
    ax.text(
        0.5,
        0.89,
        "A HPO por validação temporal ocorre apenas nos 85% anteriores ao teste final",
        transform=ax.transAxes,
        ha="center",
        va="center",
        color=COLORS["muted"],
        fontsize=10.1,
    )
    ax.set_yticks([])
    ax.set_xlabel("Tempo")
    ax.set_ylim(-0.12, 0.8)
    ax.grid(axis="x", color=COLORS["grid"], linewidth=0.8)
    ax.xaxis_date()
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    for spine in ("left", "right", "top"):
        ax.spines[spine].set_visible(False)
    ax.tick_params(axis="x", labelsize=9.8)
    fig.tight_layout()
    save(fig, "split_70_15_15_sapo")


def plot_station_ranking() -> pd.DataFrame:
    ranking = pd.read_csv(RANKING_PATH)
    top = ranking.sort_values("rank_previsibilidade_pm25_pm10").head(10).copy()
    top["short_label"] = top.apply(
        lambda r: "CMD / Sapo"
        if r["usina_slug"] == "conceicao-do-mato-dentro-sapo"
        else f"{r['municipio']} / {r['estacao']}",
        axis=1,
    )
    fig, ax = plt.subplots(figsize=(10.8, 5.4))
    top_plot = top.iloc[::-1]
    colors = [COLORS["sapo"] if s == "conceicao-do-mato-dentro-sapo" else COLORS["other"] for s in top_plot["usina_slug"]]
    ax.barh(top_plot["short_label"], top_plot["score_previsibilidade_pm25_pm10"], color=colors, alpha=0.92)
    ax.set_title("Classificação preliminar de estações por PM2.5 + contexto PM10", fontsize=13.4, weight="bold")
    ax.set_xlabel("Pontuação de previsibilidade PM2.5 + PM10")
    ax.set_xlim(0, max(90, top["score_previsibilidade_pm25_pm10"].max() + 3))
    ax.grid(axis="x", color=COLORS["grid"], linewidth=0.8)
    for y, (_, row) in enumerate(top_plot.iterrows()):
        ax.text(row["score_previsibilidade_pm25_pm10"] + 0.6, y, f"{row['score_previsibilidade_pm25_pm10']:.1f}", va="center", fontsize=9.5)
    ax.text(
        0.98,
        0.04,
        "Fonte: EDA OUTRAS_USINAS, 38 estações com PM2.5",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=9,
        color=COLORS["muted"],
    )
    fig.tight_layout()
    save(fig, "eda_ranking_estacoes_pm25_pm10")
    return top


def read_timeline(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["datetime"])
    return df.groupby("datetime", as_index=True)[["y_true", "y_pred"]].mean().sort_index()


def plot_prediction_panels() -> None:
    series = {name: (read_timeline(path), color) for name, (path, color) in TIMELINES.items()}
    base = next(iter(series.values()))[0]
    peak_time = base["y_true"].idxmax()
    start = peak_time - pd.Timedelta(days=5)
    end = peak_time + pd.Timedelta(days=5)
    grid = pd.date_range(start=start, end=end, freq="h")

    fig_height = 1.95 * len(series) + 0.9
    fig, axes = plt.subplots(len(series), 1, figsize=(11.4, fig_height), sharex=True, sharey=True)
    for ax, (name, (df, color)) in zip(axes, series.items()):
        window = df.loc[(df.index >= start) & (df.index <= end)].reindex(grid)
        ax.plot(window.index, window["y_true"], color="#202020", linewidth=1.55, label="Observado")
        ax.plot(window.index, window["y_pred"], color=color, linewidth=1.55, label=name)
        ax.axhline(35, color=COLORS["threshold"], linestyle="--", linewidth=1.1, label="Limiar 35")
        ax.set_title(name, loc="left", fontsize=11.2, weight="bold", pad=3)
        ax.set_ylabel("PM2.5", fontsize=9.8)
        ax.grid(color=COLORS["grid"], linewidth=0.8)
        ax.legend(loc="upper right", frameon=False, ncol=3, fontsize=8.8, handlelength=2.5)
        ax.tick_params(axis="both", labelsize=9.4)
        ax.set_ylim(0, 60)
    axes[-1].set_xlabel("Data", fontsize=10.2)
    locator = mdates.DayLocator(interval=1)
    formatter = mdates.DateFormatter("%d/%m")
    axes[-1].xaxis.set_major_locator(locator)
    axes[-1].xaxis.set_major_formatter(formatter)
    fig.tight_layout()
    save(fig, "predito_observado_pico_sapo")


def plot_horizon_errors() -> None:
    fig, ax = plt.subplots(figsize=(10.8, 4.9))
    for name, (path, color) in HORIZON_FILES.items():
        df = pd.read_csv(path)
        ax.plot(
            df["horizon_step"],
            df["mae"],
            color=color,
            linewidth=2.1,
            marker="o",
            markersize=3.2,
            label=name,
        )
    ax.set_title("MAE por horizonte no teste externo", fontsize=13.4, weight="bold")
    ax.set_xlabel("Horizonte previsto (horas)")
    ax.set_ylabel("MAE")
    ax.set_xlim(1, 24)
    ax.set_xticks([1, 6, 12, 18, 24])
    ax.grid(color=COLORS["grid"], linewidth=0.8)
    ax.legend(frameon=False, ncol=2, fontsize=9.2)
    fig.tight_layout()
    save(fig, "erro_por_horizonte_sapo")


def write_artifacts(
    df: pd.DataFrame,
    summary: pd.DataFrame,
    gaps: pd.DataFrame,
    observed: pd.DataFrame,
    ranking_top: pd.DataFrame,
) -> None:
    ART_DIR.mkdir(parents=True, exist_ok=True)
    summary.to_csv(ART_DIR / "eda_sapo_split_summary_tcc.csv", index=False)
    gaps.head(20).to_csv(ART_DIR / "eda_sapo_pm25_gaps_tcc.csv", index=False)
    observed.head(20).to_csv(ART_DIR / "eda_sapo_pm25_continuous_runs_tcc.csv", index=False)
    ranking_top.to_csv(ART_DIR / "eda_sapo_station_ranking_top10_tcc.csv", index=False)

    sapo_rank = ranking_top[ranking_top["usina_slug"].eq("conceicao-do-mato-dentro-sapo")]
    full = {
        "dataset_path": str(DATASET_PATH),
        "rows": int(len(df)),
        "start": str(df["Data e Hora"].min()),
        "end": str(df["Data e Hora"].max()),
        "pm25_missing_pct": float(100 * df["PM2.5__miss"].eq(1).mean()),
        "pm10_missing_pct": float(100 * df["PM10__miss"].eq(1).mean()),
        "split_summary": summary.assign(inicio=summary["inicio"].astype(str), fim=summary["fim"].astype(str)).to_dict(orient="records"),
        "top_pm25_gaps": gaps.head(6).assign(
            inicio_lacuna=gaps.head(6)["inicio_lacuna"].astype(str),
            fim_lacuna=gaps.head(6)["fim_lacuna"].astype(str),
        ).to_dict(orient="records"),
        "top_pm25_observed_runs": observed.head(6).assign(
            inicio_continuo=observed.head(6)["inicio_continuo"].astype(str),
            fim_continuo=observed.head(6)["fim_continuo"].astype(str),
        ).to_dict(orient="records"),
        "sapo_ranking_row": sapo_rank.to_dict(orient="records"),
    }
    (ART_DIR / "eda_sapo_summary_tcc.json").write_text(json.dumps(full, indent=2, ensure_ascii=False))


def main() -> None:
    df = load_dataset()
    summary = split_summary(df)
    gaps = gap_runs(df)
    observed = observed_runs(df)
    plot_external_holdout_split(summary)
    plot_coverage_and_gaps(df, gaps)
    plot_distribution(df, summary)
    ranking_top = plot_station_ranking()
    plot_horizon_errors()
    plot_prediction_panels()
    write_artifacts(df, summary, gaps, observed, ranking_top)
    print(summary.to_string(index=False))
    print(gaps.head(6).to_string(index=False))
    print(observed.head(6).to_string(index=False))


if __name__ == "__main__":
    main()
