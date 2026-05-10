from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
from matplotlib.ticker import FormatStrFormatter


ROOT = Path(__file__).resolve().parents[1]
TCC_WSL = (ROOT / ".." / "TCC-wsl").resolve()
FIG_DIR = ROOT / "figuras"
OUT_DIR = ROOT / "artefatos"
DATASET_PATH = TCC_WSL / "runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/datasets/sapo_clean_pm10_decoder_proxy.parquet"

RUNS = {
    "Seq2Seq attention HPO": {
        "ckpt": TCC_WSL
        / "runtime/training/Sapo_Clean_PM10_HPO_All_Models_2026_05_09/166e7cd1d95e4503bbf2cf44182174f2/checkpoints/best_model.ckpt",
        "diag": TCC_WSL
        / "runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/artifacts/seq2seq_attention_clean_pm10_hpo/test_outputs/attention_diagnostics.json",
    },
    "Seq2Seq weighted L1": {
        "ckpt": TCC_WSL
        / "runtime/training/Seq2Seq_Weighted_L1_HPO_2026_05_09/eb94b33d27484a20ad509492ebeb6b5d/checkpoints/best_model.ckpt",
        "diag": TCC_WSL
        / "runtime/reports/seq2seq_weighted_l1_hpo_20260509/artifacts/weighted_l1_hpo_mae/test_outputs/test_outputs/attention_diagnostics.json",
    },
}

sys.path.insert(0, str(TCC_WSL))
from src.data import processing  # noqa: E402
from src.data.datasets import Seq2SeqDataset  # noqa: E402
from src.models.seq2seq_attention import Seq2SeqAttnScheduledLightningModule  # noqa: E402


plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "axes.spines.top": False,
        "axes.spines.right": False,
    }
)


def _save(fig: plt.Figure, name: str) -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / f"{name}.png", dpi=300, bbox_inches="tight", pad_inches=0.18)
    fig.savefig(FIG_DIR / f"{name}.pdf", bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)


def _to_list(value):
    if value is None:
        return None
    if isinstance(value, (list, tuple)):
        return list(value)
    try:
        return list(value)
    except TypeError:
        return value


def _position_label(idx: int, seq_len: int) -> str:
    rel = idx - (seq_len - 1)
    return "t" if rel == 0 else f"t{rel}"


def _load_split_and_stats() -> tuple[pd.DataFrame, pd.DataFrame, dict, list[str]]:
    df = pd.read_parquet(DATASET_PATH)
    df["Data e Hora"] = pd.to_datetime(df["Data e Hora"])
    df = df.sort_values(["Estacao", "Data e Hora"]).reset_index(drop=True)
    numeric_cols = sorted(
        c
        for c in df.columns
        if c not in {"Data e Hora", "Estacao"} and pd.api.types.is_numeric_dtype(df[c])
    )
    unique_dates = sorted(df["Data e Hora"].unique())
    train_dates, _, test_dates = processing.resolve_holdout_split_dates(
        unique_dates,
        split_cfg={"split_strategy": "ratio", "val_ratio": 0.15, "test_ratio": 0.15},
        default_val_ratio=0.15,
        default_test_ratio=0.15,
    )
    df_train = df[df["Data e Hora"].isin(train_dates)].copy()
    df_test = df[df["Data e Hora"].isin(test_dates)].copy()
    station_stats = processing.compute_station_stats(df_train, numeric_cols, ignore_imputed_values=False)
    return df_train, df_test, station_stats, numeric_cols


def _build_test_dataset(model: Seq2SeqAttnScheduledLightningModule, df_test, station_stats) -> Seq2SeqDataset:
    hp = model.hparams
    return Seq2SeqDataset(
        df_test,
        in_seq_len=48,
        out_seq_len=24,
        target_col="PM2.5",
        station_stats=station_stats,
        freq="h",
        device="cpu",
        fast_indexing=False,
        return_station=True,
        decoder_exog_exclude_prefixes=_to_list(hp.get("decoder_exog_exclude_prefixes", None)),
        decoder_exog_allowlist_prefixes=_to_list(hp.get("decoder_exog_allowlist_prefixes", None)),
        decoder_exog_allowlist_exact=_to_list(hp.get("decoder_exog_allowlist_exact", None)),
        decoder_exog_mode=hp.get("decoder_exog_mode", "default"),
        include_station_features=True,
        known_future_mode=hp.get("known_future_mode", "strict_causal"),
        known_future_allowlist_prefixes=_to_list(hp.get("known_future_allowlist_prefixes", None)),
        known_future_allowlist_exact=_to_list(hp.get("known_future_allowlist_exact", None)),
        known_future_exclude_prefixes=_to_list(hp.get("known_future_exclude_prefixes", None)),
        window_stride=1,
        return_encoder_target_observed_mask=bool(hp.get("residual_baseline_use_observed_mask", False)),
    )


@torch.inference_mode()
def _extract_attention(run: dict, df_test, station_stats, batch_size: int = 192) -> np.ndarray:
    model = Seq2SeqAttnScheduledLightningModule.load_from_checkpoint(
        str(run["ckpt"]),
        map_location="cpu",
        weights_only=False,
    )
    model.eval()
    ds = _build_test_dataset(model, df_test, station_stats)
    chunks = []
    for start in range(0, len(ds), batch_size):
        idx = torch.arange(start, min(start + batch_size, len(ds)), dtype=torch.long)
        batch = ds.get_batch(idx)
        means, stds, attention, event_logits = model.model(
            batch["encoder_input"],
            batch["decoder_input"],
            target_normalized=None,
            teacher_forcing_ratio=0.0,
            encoder_target_observed_mask=batch.get("encoder_target_observed_mask"),
        )
        chunks.append(attention.detach().cpu().numpy().astype(np.float32))
    return np.concatenate(chunks, axis=0)


def _summarize_attention(attn: np.ndarray) -> dict[str, float]:
    eps = 1e-8
    seq_len = attn.shape[2]
    entropy = -(np.clip(attn, eps, None) * np.log(np.clip(attn, eps, None))).sum(axis=2)
    entropy_norm = entropy / np.log(seq_len)
    top3 = np.sort(attn, axis=2)[:, :, -3:].sum(axis=2)
    horizon = attn.shape[1]
    lag24_idx = np.arange(horizon) + seq_len - 24
    lag48_idx = np.arange(horizon) + seq_len - 48
    lag24 = [attn[:, k, idx].mean() for k, idx in enumerate(lag24_idx) if 0 <= idx < seq_len]
    lag48 = [attn[:, k, idx].mean() for k, idx in enumerate(lag48_idx) if 0 <= idx < seq_len]
    return {
        "samples": float(attn.shape[0]),
        "attention_entropy_norm": float(entropy_norm.mean()),
        "attention_max_weight": float(attn.max(axis=2).mean()),
        "attention_top3_mass": float(top3.mean()),
        "attention_last_step_mass": float(attn[:, :, -1].mean()),
        "attention_last6_mass": float(attn[:, :, -6:].sum(axis=2).mean()),
        "attention_lag24_aligned_mass": float(np.mean(lag24)),
        "attention_lag48_aligned_mass": float(np.mean(lag48)),
    }


def _plot_profile(attentions: dict[str, np.ndarray]) -> None:
    fig, ax = plt.subplots(figsize=(11, 4.8))
    seq_len = next(iter(attentions.values())).shape[2]
    x = np.arange(-(seq_len - 1), 1)
    colors = ["#2563eb", "#d97706"]
    for (label, attn), color in zip(attentions.items(), colors):
        profile = attn.mean(axis=(0, 1))
        ax.plot(x, profile, linewidth=2.3, label=label, color=color)
    uniform = 1.0 / seq_len
    ax.axhline(uniform, linestyle="--", linewidth=1.5, color="#64748b", label=f"Uniforme (1/{seq_len})")
    ax.axvspan(-5, 0, color="#f59e0b", alpha=0.10, label="Ultimas 6h")
    ax.axvline(0, color="#94a3b8", linewidth=1.0)
    ax.axvline(-24, color="#94a3b8", linewidth=1.0)
    y0, y1 = ax.get_ylim()
    top = y0 + (y1 - y0) * 0.96
    ax.text(0, top, "t", ha="right", va="top", color="#64748b", fontsize=9)
    ax.text(-24, top, "t-24 fixo", ha="right", va="top", color="#64748b", fontsize=9)
    ax.set_title("Perfil medio dos pesos de atencao no encoder", weight="bold", pad=12)
    ax.set_xlabel("Posicao no historico de entrada (horas em relacao ao instante t)")
    ax.set_ylabel("Peso medio de atencao")
    ax.set_xlim(x.min(), x.max())
    ax.yaxis.set_major_formatter(FormatStrFormatter("%.4f"))
    ax.grid(axis="y", alpha=0.25)
    ax.legend(frameon=False, ncol=4, loc="upper center", bbox_to_anchor=(0.5, -0.18))
    _save(fig, "perfil_medio_atencao_seq2seq")


def _plot_heatmap(attn: np.ndarray) -> None:
    mean_matrix = attn.mean(axis=0)
    profile_from_matrix = mean_matrix.mean(axis=0)
    horizon, seq_len = mean_matrix.shape
    fig, (ax, ax_profile) = plt.subplots(
        2,
        1,
        figsize=(11.2, 7.1),
        sharex=True,
        gridspec_kw={"height_ratios": [3.0, 1.05], "hspace": 0.08},
    )
    im = ax.imshow(
        mean_matrix,
        aspect="auto",
        origin="lower",
        cmap="viridis",
        vmin=float(mean_matrix.min()),
        vmax=float(mean_matrix.max()),
    )
    ax.set_title("Matriz media de atencao do Seq2Seq weighted L1", weight="bold", pad=12)
    ax.set_ylabel("Horizonte previsto")
    xticks = [0, 12, 24, 36, seq_len - 1]
    yticks = [0, 5, 11, 17, 23]
    ax.set_yticks(yticks)
    ax.set_yticklabels([f"H{y + 1}" for y in yticks])
    # Diagonal do lag24 alinhado ao horizonte: y_{t+k} consulta y_{t+k-24}.
    ys = np.arange(0, horizon)
    xs = ys + seq_len - 24
    valid = (xs >= 0) & (xs < seq_len)
    xs = xs[valid]
    ys = ys[valid]
    ax.plot(xs, ys, color="white", linewidth=1.6, linestyle="--", label="lag24 alinhado")
    ax.axvspan(seq_len - 6.5, seq_len - 0.5, color="white", alpha=0.16, label="ultimas 6h")
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.035)
    cbar.set_label("peso medio")
    cbar_ticks = np.linspace(float(mean_matrix.min()), float(mean_matrix.max()), 5)
    cbar.set_ticks(cbar_ticks)
    cbar.set_ticklabels([f"{tick:.4f}" for tick in cbar_ticks])
    ax.legend(frameon=True, framealpha=0.92, loc="upper left")

    x_idx = np.arange(seq_len)
    uniform = 1.0 / seq_len
    ax_profile.plot(x_idx, profile_from_matrix, color="#d97706", linewidth=2.0, label="media por posicao")
    ax_profile.axhline(uniform, linestyle="--", linewidth=1.3, color="#64748b", label="1/48")
    ax_profile.axvspan(seq_len - 6.5, seq_len - 0.5, color="#f59e0b", alpha=0.10, label="ultimas 6h")
    fixed_lag24_idx = seq_len - 1 - 24
    ax_profile.axvline(fixed_lag24_idx, color="#94a3b8", linewidth=1.0)
    ax_profile.text(
        fixed_lag24_idx,
        ax_profile.get_ylim()[1],
        "t-24 fixo",
        ha="right",
        va="top",
        color="#64748b",
        fontsize=9,
    )
    ax_profile.set_ylabel("Media\npor posicao")
    ax_profile.set_xlabel("Posicao no historico de entrada")
    ax_profile.set_xticks(xticks)
    ax_profile.set_xticklabels([_position_label(i, seq_len) for i in xticks])
    ax_profile.yaxis.set_major_formatter(FormatStrFormatter("%.4f"))
    ax_profile.grid(axis="y", alpha=0.25)
    ax_profile.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.42))
    _save(fig, "heatmap_medio_atencao_weighted_l1")


def _export_attention_artifacts(attentions: dict[str, np.ndarray]) -> dict[str, float]:
    profile_rows = []
    for label, attn in attentions.items():
        seq_len = attn.shape[2]
        profile = attn.mean(axis=(0, 1))
        for idx, weight in enumerate(profile):
            profile_rows.append(
                {
                    "modelo": label,
                    "posicao_encoder": idx,
                    "posicao_relativa_horas": idx - (seq_len - 1),
                    "rotulo_posicao": _position_label(idx, seq_len),
                    "peso_medio": float(weight),
                }
            )
    pd.DataFrame(profile_rows).to_csv(OUT_DIR / "attention_profile_tcc.csv", index=False)

    weighted = attentions["Seq2Seq weighted L1"]
    mean_matrix = weighted.mean(axis=0)
    horizon, seq_len = mean_matrix.shape
    matrix_rows = []
    for h in range(horizon):
        for idx in range(seq_len):
            matrix_rows.append(
                {
                    "horizonte": h + 1,
                    "posicao_encoder": idx,
                    "posicao_relativa_horas": idx - (seq_len - 1),
                    "rotulo_posicao": _position_label(idx, seq_len),
                    "peso_medio": float(mean_matrix[h, idx]),
                }
            )
    pd.DataFrame(matrix_rows).to_csv(OUT_DIR / "attention_heatmap_weighted_l1_tcc.csv", index=False)

    profile_direct = weighted.mean(axis=(0, 1))
    profile_from_heatmap = mean_matrix.mean(axis=0)
    comparison = {
        "max_abs_diff_profile_vs_heatmap_column_mean": float(
            np.max(np.abs(profile_direct - profile_from_heatmap))
        ),
        "weighted_l1_profile_min": float(profile_direct.min()),
        "weighted_l1_profile_max": float(profile_direct.max()),
        "weighted_l1_heatmap_cell_min": float(mean_matrix.min()),
        "weighted_l1_heatmap_cell_max": float(mean_matrix.max()),
        "weighted_l1_heatmap_cell_p02": float(np.percentile(mean_matrix, 2)),
        "weighted_l1_heatmap_cell_p98": float(np.percentile(mean_matrix, 98)),
    }
    (OUT_DIR / "attention_consistency_tcc.json").write_text(
        json.dumps(comparison, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return comparison


def _plot_diagnostics(summary_df: pd.DataFrame) -> None:
    metrics = [
        ("attention_entropy_norm", "Entropia\nnormalizada"),
        ("attention_top3_mass", "Massa\ntop-3"),
        ("attention_last6_mass", "Ultimas\n6h"),
        ("attention_lag24_aligned_mass", "Lag24\nalinhado"),
        ("attention_lag48_aligned_mass", "Lag48\nalinhado"),
    ]
    labels = [m[1] for m in metrics]
    x = np.arange(len(metrics))
    width = 0.36
    fig, ax = plt.subplots(figsize=(11, 4.8))
    colors = ["#2563eb", "#d97706"]
    for offset, (_, row) in zip([-width / 2, width / 2], summary_df.iterrows()):
        values = [row[m[0]] for m in metrics]
        ax.bar(x + offset, values, width=width, label=row["modelo"], color=colors.pop(0), alpha=0.92)
    ax.axhline(1 / 48, linestyle=":", color="#64748b", linewidth=1.5, label="1/48")
    ax.axhline(6 / 48, linestyle="--", color="#64748b", linewidth=1.5, label="6/48")
    ax.set_title("Diagnosticos agregados da atencao temporal", weight="bold", pad=12)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Valor medio")
    ax.grid(axis="y", alpha=0.25)
    ax.legend(frameon=False, ncol=4, loc="upper center", bbox_to_anchor=(0.5, -0.2))
    _save(fig, "diagnosticos_atencao_seq2seq")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    _, df_test, station_stats, _ = _load_split_and_stats()
    attentions = {}
    summaries = []
    for label, run in RUNS.items():
        attn = _extract_attention(run, df_test, station_stats)
        attentions[label] = attn
        summary = {"modelo": label, **_summarize_attention(attn)}
        if run["diag"].exists():
            summary["diagnostics_json"] = str(run["diag"])
            summary["diagnostics_json_values"] = json.dumps(json.loads(run["diag"].read_text()), sort_keys=True)
        summaries.append(summary)

    summary_df = pd.DataFrame(summaries)
    summary_df.to_csv(OUT_DIR / "attention_summary_tcc.csv", index=False)
    (OUT_DIR / "attention_summary_tcc.json").write_text(
        json.dumps(summaries, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    comparison = _export_attention_artifacts(attentions)

    _plot_profile(attentions)
    _plot_heatmap(attentions["Seq2Seq weighted L1"])
    _plot_diagnostics(summary_df)
    print(summary_df[[
        "modelo",
        "samples",
        "attention_entropy_norm",
        "attention_max_weight",
        "attention_top3_mass",
        "attention_last6_mass",
        "attention_lag24_aligned_mass",
        "attention_lag48_aligned_mass",
    ]].to_string(index=False))
    print(json.dumps(comparison, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
