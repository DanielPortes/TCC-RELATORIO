from __future__ import annotations

import json
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
TCC_WSL = (ROOT / ".." / "TCC-wsl").resolve()
DATASET_PATH = (
    TCC_WSL
    / "runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/datasets/sapo_clean_pm10_decoder_proxy.parquet"
)
FIG_DIR = ROOT / "figuras"
OUT_DIR = ROOT / "artefatos"

COLORS = {
    "ink": "#1f2937",
    "muted": "#64748b",
    "line": "#334155",
    "blue": "#2563eb",
    "blue_light": "#dbeafe",
    "green": "#059669",
    "green_light": "#d1fae5",
    "amber": "#d97706",
    "amber_light": "#fef3c7",
    "red": "#dc2626",
    "red_light": "#fee2e2",
    "violet": "#7c3aed",
    "violet_light": "#ede9fe",
    "slate_light": "#f1f5f9",
    "white": "#ffffff",
}


plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    }
)


def _save(fig: plt.Figure, name: str) -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / f"{name}.png", dpi=300, bbox_inches="tight", pad_inches=0.18)
    fig.savefig(FIG_DIR / f"{name}.pdf", bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)


def _box(ax, x, y, w, h, text, fc, ec=None, fs=10.5, weight="normal") -> None:
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.04",
        linewidth=1.4,
        edgecolor=ec or COLORS["line"],
        facecolor=fc,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=fs,
        weight=weight,
        color=COLORS["ink"],
        linespacing=1.12,
    )


def _arrow(ax, start, end, color=None, lw=1.9, rad=0.0) -> None:
    arr = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=13,
        linewidth=lw,
        color=color or COLORS["line"],
        connectionstyle=f"arc3,rad={rad}",
        shrinkA=2,
        shrinkB=2,
    )
    ax.add_patch(arr)


def _load_sapo() -> pd.DataFrame:
    df = pd.read_parquet(DATASET_PATH)
    df["Data e Hora"] = pd.to_datetime(df["Data e Hora"])
    df = df[df["Estacao"] == "Sapo"].sort_values("Data e Hora").copy()
    df = df.set_index("Data e Hora")
    return df


def _component_frame(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, float]]:
    y = pd.to_numeric(df["PM2.5"], errors="coerce").astype(float)
    miss = pd.to_numeric(df["PM2.5__miss"], errors="coerce").fillna(0.0).astype(float)

    trend = y.rolling(24 * 7, center=True, min_periods=24).mean().bfill().ffill()
    detrended = y - trend
    seasonal_profile = detrended.groupby(df.index.hour).mean()
    seasonal = pd.Series(df.index.hour, index=df.index).map(seasonal_profile).astype(float)
    remainder = y - trend - seasonal

    comp = pd.DataFrame(
        {
            "pm25": y,
            "pm25_missing_flag": miss,
            "trend_7d_ma": trend,
            "seasonal_hourly": seasonal,
            "remainder": remainder,
        },
        index=df.index,
    )

    observed = y[miss == 0]
    summary = {
        "autocorr_1h": float(observed.autocorr(lag=1)),
        "autocorr_24h": float(observed.autocorr(lag=24)),
        "autocorr_168h": float(observed.autocorr(lag=168)),
        "seasonal_hourly_amplitude": float(seasonal_profile.max() - seasonal_profile.min()),
        "trend_7d_ma_min": float(trend.min()),
        "trend_7d_ma_max": float(trend.max()),
    }
    return comp, summary


def draw_time_series_components() -> None:
    df = _load_sapo()
    comp, summary = _component_frame(df)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    comp.to_csv(OUT_DIR / "fundamentacao_decomposicao_sapo.csv")
    (OUT_DIR / "fundamentacao_decomposicao_sapo_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    start = pd.Timestamp("2020-08-01 00:30:00")
    end = pd.Timestamp("2020-11-30 23:30:00")
    plot_df = comp.loc[start:end].copy()
    if plot_df.empty:
        plot_df = comp.tail(24 * 120).copy()

    fig, axes = plt.subplots(4, 1, figsize=(12.5, 8.2), sharex=True, gridspec_kw={"hspace": 0.12})
    fig.suptitle("Série temporal de PM2.5 e decomposição descritiva - Sapo", fontsize=15, weight="bold", y=0.98)

    axes[0].plot(plot_df.index, plot_df["pm25"], color=COLORS["blue"], linewidth=1.15, label="PM2.5 regularizado")
    missing = plot_df["pm25_missing_flag"] > 0
    if missing.any():
        axes[0].scatter(
            plot_df.index[missing],
            plot_df.loc[missing, "pm25"],
            s=8,
            color=COLORS["red"],
            alpha=0.5,
            label="ponto originalmente ausente",
        )
    axes[0].set_ylabel("Série\noriginal")
    axes[0].legend(frameon=False, loc="upper left", ncol=2)

    axes[1].plot(plot_df.index, plot_df["trend_7d_ma"], color=COLORS["green"], linewidth=1.7)
    axes[1].set_ylabel("Tendência-\nciclo")
    axes[1].text(
        0.01,
        0.82,
        "média móvel de 7 dias",
        transform=axes[1].transAxes,
        fontsize=9,
        color=COLORS["muted"],
    )

    axes[2].plot(plot_df.index, plot_df["seasonal_hourly"], color=COLORS["amber"], linewidth=1.25)
    axes[2].axhline(0, color=COLORS["muted"], linewidth=0.8, linestyle="--")
    axes[2].set_ylabel("Padrão\nhorário")

    axes[3].plot(plot_df.index, plot_df["remainder"], color=COLORS["violet"], linewidth=1.05)
    axes[3].axhline(0, color=COLORS["muted"], linewidth=0.8, linestyle="--")
    axes[3].set_ylabel("Resíduo\ne picos")
    axes[3].set_xlabel("Tempo")

    for ax in axes:
        ax.grid(axis="y", alpha=0.25)
        ax.tick_params(axis="both", labelsize=9)
    axes[-1].xaxis.set_major_locator(mdates.MonthLocator())
    axes[-1].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    fig.text(
        0.5,
        0.005,
        (
            "Decomposição aditiva descritiva: PM2.5 = tendência-ciclo + sazonalidade horária + resíduo. "
            "Os componentes não foram usados como entrada direta dos modelos finais."
        ),
        ha="center",
        fontsize=9.5,
        color=COLORS["muted"],
    )
    _save(fig, "serie_temporal_componentes_sapo")


def draw_teacher_forcing_scheduled_sampling() -> None:
    fig = plt.figure(figsize=(13.0, 7.1))
    gs = GridSpec(1, 2, figure=fig, width_ratios=[1.52, 1.0], wspace=0.22)
    ax = fig.add_subplot(gs[0, 0])
    ax_curve = fig.add_subplot(gs[0, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(
        0.5,
        0.97,
        "Teacher forcing vs. scheduled sampling",
        ha="center",
        va="top",
        fontsize=14.5,
        weight="bold",
        color=COLORS["ink"],
    )
    ax.text(
        0.5,
        0.92,
        "A diferença está no valor realimentado para o próximo passo do decoder",
        ha="center",
        va="top",
        fontsize=9.8,
        color=COLORS["muted"],
    )

    rows = [
        (0.72, "Teacher forcing", "$y_{t+k-1}$\nvalor real", COLORS["blue_light"], COLORS["blue"]),
        (0.47, "Free running", "$\\hat{y}_{t+k-1}$\npredição", COLORS["green_light"], COLORS["green"]),
        (0.22, "Scheduled\nsampling", "sorteio\n$u \\sim U(0,1)$", COLORS["amber_light"], COLORS["amber"]),
    ]
    for y, title, left_text, fc, ec in rows:
        ax.text(0.02, y + 0.065, title, ha="left", va="center", fontsize=11.2, weight="bold", color=ec, linespacing=1.0)
        _box(ax, 0.28, y, 0.16, 0.12, left_text, fc, ec, fs=10.0, weight="bold")
        _arrow(ax, (0.44, y + 0.06), (0.54, y + 0.06), COLORS["line"])
        _box(ax, 0.54, y, 0.16, 0.12, "Decoder\n$Dec_\\theta$", COLORS["slate_light"], COLORS["line"], fs=10.0, weight="bold")
        _arrow(ax, (0.70, y + 0.06), (0.81, y + 0.06), COLORS["line"])
        _box(ax, 0.81, y, 0.13, 0.12, "$\\hat{y}_{t+k}$\nsaída", COLORS["violet_light"], COLORS["violet"], fs=10.0, weight="bold")

    _box(ax, 0.18, 0.13, 0.22, 0.07, "se $u < p_{TF}$:\nusa valor real", COLORS["blue_light"], COLORS["blue"], fs=8.8)
    _box(ax, 0.43, 0.13, 0.24, 0.07, "caso contrário:\nusa predição", COLORS["green_light"], COLORS["green"], fs=8.8)
    _arrow(ax, (0.29, 0.20), (0.34, 0.22), COLORS["amber"], lw=1.4, rad=0.08)
    _arrow(ax, (0.55, 0.20), (0.38, 0.22), COLORS["amber"], lw=1.4, rad=-0.12)

    ax.text(
        0.5,
        0.055,
        "$p_{TF}=1$ equivale a teacher forcing puro; $p_{TF}=0$ equivale a treino igual a inferência autoregressiva.",
        ha="center",
        va="center",
        fontsize=9.7,
        color=COLORS["muted"],
    )

    epochs = np.arange(0, 21)
    p_tf_original = np.maximum(0.2, 1.0 - 0.04 * epochs)
    p_model = 1.0 - p_tf_original
    p_tf_increase = np.minimum(1.0, 0.05 * epochs)
    ax_curve.plot(epochs, p_tf_original, color=COLORS["blue"], linewidth=2.4, label="$p_{TF}$ decrescente")
    ax_curve.plot(epochs, p_model, color=COLORS["green"], linewidth=2.4, label="$1-p_{TF}$")
    ax_curve.plot(
        epochs,
        p_tf_increase,
        color=COLORS["red"],
        linewidth=1.9,
        linestyle="--",
        label="$p_{TF}$ crescente (ITF)",
    )
    ax_curve.set_title("Agendas de probabilidade", fontsize=13, weight="bold")
    ax_curve.set_xlabel("Época de treinamento")
    ax_curve.set_ylabel("Probabilidade")
    ax_curve.set_ylim(-0.03, 1.03)
    ax_curve.set_xlim(epochs.min(), epochs.max())
    ax_curve.grid(alpha=0.25)
    ax_curve.legend(frameon=False, loc="center right")
    ax_curve.text(
        0.03,
        0.05,
        "Bengio: $p_{TF}$ diminui.\nITF: $p_{TF}$ aumenta.",
        transform=ax_curve.transAxes,
        fontsize=9,
        color=COLORS["muted"],
    )
    _save(fig, "teacher_forcing_scheduled_sampling")


if __name__ == "__main__":
    draw_time_series_components()
    draw_teacher_forcing_scheduled_sampling()
