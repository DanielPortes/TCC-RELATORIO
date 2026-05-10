from __future__ import annotations

import json
import math
import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
TECH_ROOT = ROOT.parent / "TCC-wsl"
MLFLOW_DB = TECH_ROOT / "mlflow.db"
SUMMARY_PATH = TECH_ROOT / "runtime/reports/sapo_final_pre_delivery_suite_20260510/cv_hpo_summary.csv"
FIG_DIR = ROOT / "figuras"
ART_DIR = ROOT / "artefatos"

WARMUP_EPOCHS = 3

MODEL_SPECS = [
    {
        "name": "cv_hpo_lstm_direct_clean_pm10",
        "label": "LSTM direta",
        "color": "#4C78A8",
    },
    {
        "name": "cv_hpo_lstm_recursive_clean_pm10",
        "label": "LSTM recursiva",
        "color": "#B279A2",
    },
    {
        "name": "cv_hpo_weighted_l1_clean_pm10",
        "label": "Seq2Seq atenção + L1 ponderada",
        "color": "#54A24B",
    },
]


plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    }
)


def _load_metric(conn: sqlite3.Connection, run_id: str, key: str) -> pd.DataFrame:
    rows = conn.execute(
        """
        SELECT v.step, e.value AS epoch, v.value AS value, v.timestamp
        FROM metrics v
        LEFT JOIN metrics e
          ON e.run_uuid = v.run_uuid
         AND e.key = 'epoch'
         AND e.step = v.step
         AND e.timestamp = v.timestamp
        WHERE v.run_uuid = ?
          AND v.key = ?
        ORDER BY v.timestamp, v.step
        """,
        (run_id, key),
    ).fetchall()
    df = pd.DataFrame(rows, columns=["step", "epoch", key, "timestamp"])
    if df.empty:
        raise RuntimeError(f"Metrica {key!r} ausente para run {run_id}")
    if df["epoch"].isna().any():
        df["epoch"] = range(len(df))
    df["epoch"] = df["epoch"].astype(int)
    return df[["epoch", key]]


def _lr_at_epoch(epoch: int, max_epochs: int, lr_max: float) -> float:
    eta_min = lr_max * 0.01
    start_factor = 1e-5
    if WARMUP_EPOCHS >= max_epochs:
        return lr_max
    if epoch <= WARMUP_EPOCHS:
        factor = start_factor + (1.0 - start_factor) * (epoch / WARMUP_EPOCHS)
        return lr_max * factor
    progress = min(max((epoch - WARMUP_EPOCHS) / (max_epochs - WARMUP_EPOCHS), 0.0), 1.0)
    return eta_min + 0.5 * (lr_max - eta_min) * (1.0 + math.cos(math.pi * progress))


def _load_curves() -> pd.DataFrame:
    summary = pd.read_csv(SUMMARY_PATH)
    conn = sqlite3.connect(MLFLOW_DB)
    frames = []

    for spec in MODEL_SPECS:
        row = summary.loc[summary["name"] == spec["name"]].iloc[0]
        run_id = str(row["run_id"])
        params = json.loads(row["best_params_json"])
        lr_max = float(params["lr"])
        max_epochs = int(row["final_max_epochs"])
        best_epoch = int(row["best_checkpoint_epoch"])

        val_mae = _load_metric(conn, run_id, "val/mae")
        val_loss = _load_metric(conn, run_id, "val/loss")
        curve = val_mae.merge(val_loss, on="epoch", how="outer").sort_values("epoch")
        curve["model"] = spec["label"]
        curve["color"] = spec["color"]
        curve["run_id"] = run_id
        curve["lr_nominal"] = lr_max
        curve["max_epochs"] = max_epochs
        curve["best_checkpoint_epoch"] = best_epoch
        curve["stop_epoch"] = int(curve["epoch"].max())
        curve["lr"] = curve["epoch"].map(lambda epoch: _lr_at_epoch(int(epoch), max_epochs, lr_max))
        frames.append(curve)

    conn.close()
    return pd.concat(frames, ignore_index=True)


def _value_at_epoch(curve: pd.DataFrame, epoch: int, column: str) -> float:
    nearest = curve.iloc[(curve["epoch"] - epoch).abs().argsort()].iloc[0]
    return float(nearest[column])


def _plot(curves: pd.DataFrame) -> None:
    fig, axes = plt.subplots(
        2,
        1,
        figsize=(7.4, 5.2),
        sharex=True,
        gridspec_kw={"height_ratios": [1.55, 1.0], "hspace": 0.12},
    )
    ax_mae, ax_lr = axes

    for spec in MODEL_SPECS:
        curve = curves[curves["model"] == spec["label"]].sort_values("epoch")
        color = spec["color"]
        best_epoch = int(curve["best_checkpoint_epoch"].iloc[0])
        stop_epoch = int(curve["stop_epoch"].iloc[0])

        ax_mae.plot(curve["epoch"], curve["val/mae"], color=color, lw=2.0, label=spec["label"])
        ax_lr.plot(curve["epoch"], curve["lr"], color=color, lw=2.0)

        best_mae = _value_at_epoch(curve, best_epoch, "val/mae")
        stop_mae = _value_at_epoch(curve, stop_epoch, "val/mae")
        ax_mae.scatter(
            [best_epoch],
            [best_mae],
            marker="*",
            s=120,
            color=color,
            edgecolor="white",
            linewidth=0.8,
            zorder=5,
        )
        ax_mae.scatter(
            [stop_epoch],
            [stop_mae],
            marker="o",
            s=46,
            facecolor="white",
            edgecolor=color,
            linewidth=1.6,
            zorder=5,
        )
        ax_mae.annotate(
            f"{best_epoch}",
            xy=(best_epoch, best_mae),
            xytext=(4, 8),
            textcoords="offset points",
            color=color,
            fontsize=8.5,
            weight="bold",
        )

    for ax in axes:
        ax.grid(True, color="#e5e7eb", linewidth=0.8)
        ax.set_axisbelow(True)

    ax_mae.set_ylabel("MAE de validação ($\\mu$g/m$^3$)")
    ax_lr.set_ylabel("Taxa de aprendizado")
    ax_lr.set_xlabel("Época")
    ax_lr.set_yscale("log")

    ax_mae.text(0.01, 0.93, "(a)", transform=ax_mae.transAxes, weight="bold", color="#334155")
    ax_lr.text(0.01, 0.88, "(b)", transform=ax_lr.transAxes, weight="bold", color="#334155")

    model_handles = [
        Line2D([0], [0], color=spec["color"], lw=2.0, label=spec["label"])
        for spec in MODEL_SPECS
    ]
    marker_handles = [
        Line2D([0], [0], marker="*", color="#334155", lw=0, markersize=9, label="melhor checkpoint"),
        Line2D(
            [0],
            [0],
            marker="o",
            color="#334155",
            markerfacecolor="white",
            lw=0,
            markersize=6,
            label="parada antecipada",
        ),
    ]
    ax_mae.legend(
        handles=model_handles + marker_handles,
        loc="upper right",
        frameon=True,
        framealpha=0.95,
        edgecolor="#e5e7eb",
        fontsize=8.5,
        ncol=1,
    )

    FIG_DIR.mkdir(parents=True, exist_ok=True)
    ART_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / "curvas_validacao_lr_modelos_finais.png", dpi=300, bbox_inches="tight", pad_inches=0.16)
    fig.savefig(FIG_DIR / "curvas_validacao_lr_modelos_finais.pdf", bbox_inches="tight", pad_inches=0.16)
    plt.close(fig)


def main() -> None:
    curves = _load_curves()
    curves.to_csv(ART_DIR / "curvas_validacao_lr_modelos_finais.csv", index=False)
    _plot(curves)


if __name__ == "__main__":
    main()
