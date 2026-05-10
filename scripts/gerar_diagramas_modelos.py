from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Circle, Rectangle


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figuras"

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
    "violet": "#7c3aed",
    "violet_light": "#ede9fe",
    "red": "#dc2626",
    "red_light": "#fee2e2",
    "slate_light": "#f1f5f9",
    "white": "#ffffff",
}


plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 12,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    }
)


def setup_ax(width=14, height=7):
    fig, ax = plt.subplots(figsize=(width, height), dpi=180)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    return fig, ax


def save(fig, name):
    png = FIG_DIR / f"{name}.png"
    pdf = FIG_DIR / f"{name}.pdf"
    fig.savefig(png, dpi=300, bbox_inches="tight", pad_inches=0.22)
    fig.savefig(pdf, bbox_inches="tight", pad_inches=0.22)
    plt.close(fig)


def box(ax, x, y, w, h, text, fc, ec=None, lw=1.7, fs=11, weight="normal", color=None):
    ec = ec or COLORS["line"]
    color = color or COLORS["ink"]
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=1.6",
        linewidth=lw,
        edgecolor=ec,
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
        color=color,
        weight=weight,
        linespacing=1.16,
    )
    return patch


def label(ax, x, y, text, fs=12, weight="normal", color=None, ha="center", va="center"):
    ax.text(
        x,
        y,
        text,
        ha=ha,
        va=va,
        fontsize=fs,
        weight=weight,
        color=color or COLORS["ink"],
        linespacing=1.15,
    )


def arrow(ax, start, end, color=None, lw=2.2, ms=13, rad=0.0, style="-|>"):
    arr = FancyArrowPatch(
        start,
        end,
        arrowstyle=style,
        mutation_scale=ms,
        linewidth=lw,
        color=color or COLORS["line"],
        connectionstyle=f"arc3,rad={rad}",
        shrinkA=2,
        shrinkB=2,
    )
    ax.add_patch(arr)
    return arr


def group(ax, x, y, w, h, title, color):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=2.2",
        linewidth=1.4,
        edgecolor=color,
        facecolor="#ffffff",
    )
    ax.add_patch(patch)
    label(ax, x + 3, y + h - 4.5, title, fs=12, weight="bold", color=color, ha="left")
    return patch


def draw_lstm():
    fig, ax = setup_ax(14.4, 7.4)

    label(ax, 50, 95, "Celula LSTM: controle de memoria por portoes", fs=17, weight="bold")
    label(ax, 50, 90, "Fluxo no passo t para entrada x_t, memoria c_t e estado oculto h_t", fs=10, color=COLORS["muted"])

    group(ax, 3, 18, 22, 62, "Entradas", COLORS["blue"])
    box(ax, 7, 61, 14, 9.5, "$c_{t-1}$\nmemoria", COLORS["blue_light"], COLORS["blue"], fs=11, weight="bold")
    box(ax, 7, 44, 14, 9.5, "$x_t$\natributos", COLORS["blue_light"], COLORS["blue"], fs=11, weight="bold")
    box(ax, 7, 27, 14, 9.5, "$h_{t-1}$\nestado", COLORS["blue_light"], COLORS["blue"], fs=11, weight="bold")

    group(ax, 29, 14, 47, 70, "Transformacoes internas", COLORS["violet"])
    box(ax, 33, 43.5, 13, 10.5, "$[x_t;h_{t-1}]$\nconcat", COLORS["slate_light"], COLORS["line"], fs=10.5, weight="bold")
    label(ax, 39.5, 38.8, "entrada comum\ndos portoes", fs=9.5, color=COLORS["muted"])

    gates = [
        ("$f_t$\nesquecer", COLORS["red_light"], COLORS["red"], 59.5),
        ("$i_t$\nentrada", COLORS["green_light"], COLORS["green"], 47.0),
        ("$\\tilde{c}_t$\ncandidato", COLORS["amber_light"], COLORS["amber"], 34.5),
        ("$o_t$\nsaida", COLORS["violet_light"], COLORS["violet"], 22.0),
    ]
    for text, fc, ec, y in gates:
        box(ax, 51, y, 12, 9.5, text, fc, ec, fs=10.7, weight="bold")
        arrow(ax, (46, 48.8), (51, y + 4.75), COLORS["blue"], lw=1.7)

    box(ax, 66, 57.5, 7.5, 11.5, "$c_t$\nupdate", COLORS["slate_light"], COLORS["line"], fs=10.5, weight="bold")
    box(ax, 66, 27.5, 7.5, 11.5, "$h_t$\nupdate", COLORS["slate_light"], COLORS["line"], fs=10.5, weight="bold")

    arrow(ax, (21, 49), (33, 51.5), COLORS["blue"], lw=2.0, rad=-0.02)
    arrow(ax, (21, 31.8), (33, 46.5), COLORS["blue"], lw=2.0, rad=0.08)
    ax.plot([21, 34, 62], [66, 75, 75], color=COLORS["line"], linewidth=2.0)
    arrow(ax, (62, 75), (66, 67.2), COLORS["line"], lw=2.0)
    label(ax, 46, 78, "memoria anterior", fs=9.3, color=COLORS["muted"])

    arrow(ax, (63, 64.2), (66, 64.2), COLORS["red"], lw=2.0)
    arrow(ax, (63, 51.7), (66, 62.0), COLORS["green"], lw=1.9, rad=0.08)
    arrow(ax, (63, 39.2), (66, 59.8), COLORS["amber"], lw=1.9, rad=0.12)
    arrow(ax, (63, 26.7), (66, 33.2), COLORS["violet"], lw=2.0, rad=-0.03)
    arrow(ax, (69.8, 57.5), (69.8, 39), COLORS["line"], lw=2.0)

    group(ax, 81, 18, 16, 62, "Saidas", COLORS["green"])
    box(ax, 84, 61, 10, 9.5, "$c_t$\nmemoria", COLORS["green_light"], COLORS["green"], fs=10.8, weight="bold")
    box(ax, 84, 30, 10, 9.5, "$h_t$\nestado", COLORS["green_light"], COLORS["green"], fs=10.8, weight="bold")
    arrow(ax, (73.5, 63.2), (84, 65.8), COLORS["green"], lw=2.2)
    arrow(ax, (73.5, 33.2), (84, 34.8), COLORS["green"], lw=2.2)

    label(ax, 50, 7, "O fluxo separa entrada comum, atualizacao da memoria e emissao do estado oculto.", fs=10, color=COLORS["muted"])
    save(fig, "diagrama_lstm_proprio")


def draw_seq2seq_attention():
    fig, ax = setup_ax(15.4, 7.7)

    label(ax, 50, 96, "Seq2Seq com atencao para previsao multi-horizonte", fs=17, weight="bold")
    label(ax, 50, 91, "Entrada historica de 48h, decoder de 24h e covariaveis futuras conhecidas", fs=10, color=COLORS["muted"])

    group(ax, 3, 16, 29, 68, "Encoder: historico observado", COLORS["blue"])
    x_positions = [8.5, 17.5, 26.5]
    input_labels = ["$x_{t-47}$", "$\\cdots$", "$x_t$"]
    hidden_labels = ["$h_1$", "$\\cdots$", "$h_{48}$"]
    for x, inp, hid in zip(x_positions, input_labels, hidden_labels):
        box(ax, x - 3.4, 59, 6.8, 9.2, inp, COLORS["blue_light"], COLORS["blue"], fs=11.5, weight="bold")
        box(ax, x - 3.4, 40, 6.8, 9.2, hid, COLORS["slate_light"], COLORS["line"], fs=11.5, weight="bold")
        arrow(ax, (x, 59), (x, 49.2), COLORS["blue"], lw=2.0)
    arrow(ax, (11.9, 44.6), (14.1, 44.6), COLORS["line"], lw=2.0)
    arrow(ax, (20.9, 44.6), (23.1, 44.6), COLORS["line"], lw=2.0)
    box(ax, 20.8, 28, 8.5, 7.5, "$H$\nmemoria", COLORS["slate_light"], COLORS["line"], fs=10.5, weight="bold")
    arrow(ax, (26.5, 40), (25.0, 35.5), COLORS["line"], lw=2.0)
    label(ax, 17.5, 23.5, "PM2.5, PM10,\nflags e tempo", fs=9.5, color=COLORS["muted"])

    group(ax, 36, 16, 25, 68, "Atencao temporal", COLORS["violet"])
    label(ax, 48.5, 72, "pesos $\\alpha_{k,j}$", fs=12, weight="bold", color=COLORS["violet"])
    heat_x, heat_y = 42.2, 60
    cell = 2.9
    values = [
        [0.25, 0.45, 0.65, 0.35, 0.20],
        [0.15, 0.30, 0.75, 0.55, 0.25],
        [0.20, 0.35, 0.50, 0.80, 0.45],
        [0.30, 0.25, 0.40, 0.60, 0.70],
    ]
    for r, row in enumerate(values):
        for c, val in enumerate(row):
            color = (0.93 - 0.35 * val, 0.91 - 0.45 * val, 1.0)
            ax.add_patch(Rectangle((heat_x + c * cell, heat_y - r * cell), cell - 0.12, cell - 0.12, facecolor=color, edgecolor="white", linewidth=0.8))
    label(ax, 49.5, 44.8, "$c_k = \\sum_j \\alpha_{k,j}h_j$", fs=13, weight="bold")
    box(ax, 42.2, 27, 14.5, 8.5, "contexto\n$c_k$", COLORS["violet_light"], COLORS["violet"], fs=12, weight="bold")
    arrow(ax, (29.3, 31.8), (42.2, 54.5), COLORS["line"], lw=2.1, rad=0.04)
    arrow(ax, (49.5, 48.2), (49.5, 35.5), COLORS["violet"], lw=2.2)

    group(ax, 65, 16, 32, 68, "Decoder: horizonte previsto", COLORS["green"])
    box(ax, 69, 64, 24, 8.5, "covariaveis conhecidas\n$z_{t+1:t+24}$", COLORS["slate_light"], COLORS["line"], fs=10, weight="bold")
    dec_x = [72, 81, 90]
    y_labels = ["$\\hat{y}_{t+1}$", "$\\cdots$", "$\\hat{y}_{t+24}$"]
    s_labels = ["$s_1$", "$\\cdots$", "$s_{24}$"]
    ax.plot([72, 90], [61, 61], color=COLORS["line"], linewidth=2.0)
    arrow(ax, (81, 64), (81, 61.2), COLORS["line"], lw=1.9)
    for x, s, y in zip(dec_x, s_labels, y_labels):
        box(ax, x - 3.6, 48, 7.2, 9.5, s, COLORS["green_light"], COLORS["green"], fs=12, weight="bold")
        box(ax, x - 4.2, 29, 8.4, 9.5, y, COLORS["amber_light"], COLORS["amber"], fs=11, weight="bold")
        arrow(ax, (x, 61), (x, 57.8), COLORS["line"], lw=1.8)
        arrow(ax, (x, 48), (x, 38.8), COLORS["green"], lw=2.0)
    arrow(ax, (75.6, 52.8), (77.4, 52.8), COLORS["green"], lw=2.0)
    arrow(ax, (84.6, 52.8), (86.4, 52.8), COLORS["green"], lw=2.0)
    arrow(ax, (56.7, 31.2), (68.4, 52.8), COLORS["violet"], lw=2.4, rad=-0.05)
    label(ax, 82, 23.5, "calendario/Fourier + PM10 ex-ante", fs=9.5, color=COLORS["muted"])

    label(ax, 50, 7, "Os estados do encoder sao consolidados em H antes do calculo dos pesos de atencao.", fs=10, color=COLORS["muted"])
    save(fig, "diagrama_seq2seq_attention_proprio")


def draw_tree(ax, x, y, scale=1.0, color=None):
    color = color or COLORS["green"]
    nodes = [
        (x, y + 8 * scale),
        (x - 5 * scale, y),
        (x + 5 * scale, y),
        (x - 8 * scale, y - 7 * scale),
        (x - 2 * scale, y - 7 * scale),
        (x + 2 * scale, y - 7 * scale),
        (x + 8 * scale, y - 7 * scale),
    ]
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    for a, b in edges:
        ax.plot([nodes[a][0], nodes[b][0]], [nodes[a][1], nodes[b][1]], color=color, linewidth=1.8)
    for nx, ny in nodes:
        ax.add_patch(Circle((nx, ny), 1.25 * scale, facecolor=COLORS["white"], edgecolor=color, linewidth=1.5))


def draw_xgboost():
    fig, ax = setup_ax(15.4, 6.4)

    label(ax, 50, 94, "XGBoost multi-output: serie temporal como matriz supervisionada", fs=16.5, weight="bold")
    label(ax, 50, 89, "A janela de 48h e transformada em vetor tabular; a saida contem 24 previsoes", fs=10, color=COLORS["muted"])

    group(ax, 3, 18, 26, 62, "Janela temporal 48h", COLORS["blue"])
    table_x, table_y = 7, 33
    col_w, row_h = 4.1, 5.1
    headers = ["PM2.5", "PM10", "miss", "tempo"]
    rows = ["t-47", "...", "t"]
    for c, head in enumerate(headers):
        box(ax, table_x + c * col_w, table_y + 18, col_w, row_h, head, COLORS["blue_light"], COLORS["blue"], lw=1.1, fs=7.5, weight="bold")
    for r, row in enumerate(rows):
        label(ax, table_x - 2.2, table_y + 14 - r * row_h, row, fs=8.5, color=COLORS["muted"])
        for c in range(len(headers)):
            fc = COLORS["white"] if r != 1 else COLORS["slate_light"]
            ax.add_patch(Rectangle((table_x + c * col_w, table_y + 11 - r * row_h), col_w, row_h, facecolor=fc, edgecolor=COLORS["blue"], linewidth=0.9))
    label(ax, 15.8, 26, "lags, flags e\nproxies causais", fs=9.5, color=COLORS["muted"])

    arrow(ax, (29, 49), (36, 49), COLORS["line"], lw=2.4)
    label(ax, 32.4, 55, "flatten +\nfeatures", fs=9, color=COLORS["muted"])

    group(ax, 36, 18, 23, 62, "Vetor tabular", COLORS["violet"])
    for idx, y in enumerate([62, 53, 44, 35]):
        box(ax, 41.5, y, 12, 6.5, f"$u_{{i,{idx+1}}}$", COLORS["violet_light"], COLORS["violet"], fs=11, weight="bold")
    label(ax, 47.5, 28, "$\\mathbf{u}_i \\in \\mathbb{R}^{p}$", fs=12, weight="bold", color=COLORS["violet"])

    arrow(ax, (59, 49), (65, 49), COLORS["line"], lw=2.4)

    group(ax, 65, 18, 21, 62, "Boosting", COLORS["green"])
    draw_tree(ax, 71.2, 58, 0.53, COLORS["green"])
    label(ax, 71.2, 45.5, "$f_1$", fs=10.5, weight="bold", color=COLORS["green"])
    draw_tree(ax, 79.3, 58, 0.53, COLORS["green"])
    label(ax, 79.3, 45.5, "$f_2$", fs=10.5, weight="bold", color=COLORS["green"])
    label(ax, 75.2, 45.5, "$+$", fs=14, weight="bold", color=COLORS["green"])
    draw_tree(ax, 75.2, 37, 0.55, COLORS["green"])
    label(ax, 75.2, 24.2, "$f_K$", fs=10.5, weight="bold", color=COLORS["green"])
    label(ax, 75.2, 29.5, "$\\sum_k f_k(\\mathbf{u}_i)$", fs=12, weight="bold", color=COLORS["green"])

    arrow(ax, (86, 49), (90, 49), COLORS["line"], lw=2.4)

    group(ax, 90, 18, 8, 62, "Saida", COLORS["amber"])
    ys = [68, 61, 54, 47, 40, 33]
    labels = ["$\\hat{y}_{t+1}$", "$\\hat{y}_{t+2}$", "$\\cdots$", "$\\hat{y}_{t+23}$", "$\\hat{y}_{t+24}$", "24h"]
    for y, text in zip(ys, labels):
        fc = COLORS["amber_light"] if text != "24h" else COLORS["slate_light"]
        box(ax, 92.0, y - 2.6, 4.3, 5.2, text, fc, COLORS["amber"], lw=1.1, fs=7.4, weight="bold")

    label(ax, 50, 8, "O baseline usa a mesma divisao temporal, mas aprende sobre atributos tabulares derivados da janela.", fs=10, color=COLORS["muted"])
    save(fig, "diagrama_xgboost_multioutput_proprio")


if __name__ == "__main__":
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    draw_lstm()
    draw_seq2seq_attention()
    draw_xgboost()
