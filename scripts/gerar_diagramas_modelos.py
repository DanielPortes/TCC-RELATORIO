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


def draw_seq2seq_attention():
    with plt.rc_context({"font.family": "DejaVu Serif", "mathtext.fontset": "dejavuserif"}):
        fig, ax = setup_ax(6.15, 2.45)

        ink = "#111827"
        muted = "#586174"
        line = "#303744"
        rule = "#bcc6d4"
        fill = "#fbfcfe"
        fill_dark = "#eef2f7"
        fill_mid = "#e7edf4"
        accent = "#334155"
        accent_fill = "#f2f6fa"

        def text(x, y, s, fs=7.6, weight="normal", color=ink, ha="center", va="center", rotation=0):
            ax.text(x, y, s, ha=ha, va=va, fontsize=fs, weight=weight, color=color, linespacing=1.16, rotation=rotation)

        def rect(x, y, w, h, s, fc=fill, ec=line, fs=7.2, weight="normal", lw=0.85, radius=0.28):
            ax.add_patch(
                FancyBboxPatch(
                    (x, y),
                    w,
                    h,
                    boxstyle=f"round,pad=0.012,rounding_size={radius}",
                    facecolor=fc,
                    edgecolor=ec,
                    linewidth=lw,
                )
            )
            text(x + w / 2, y + h / 2, s, fs=fs, weight=weight)

        def arr(start, end, lw=0.85, color=line, rad=0.0, ms=8.2, style="-|>"):
            ax.add_patch(
                FancyArrowPatch(
                    start,
                    end,
                    arrowstyle=style,
                    mutation_scale=ms,
                    linewidth=lw,
                    color=color,
                    connectionstyle=f"arc3,rad={rad}",
                    shrinkA=2,
                    shrinkB=2,
                )
            )

        def section(x, y, label, width):
            text(x, y, label, fs=8.9, weight="bold")
            ax.plot([x - width / 2, x + width / 2], [y - 3.6, y - 3.6], color=rule, linewidth=0.8)

        def attention_matrix(x, y, cell_w=4.05, cell_h=3.75):
            values = [
                [0.18, 0.32, 0.74, 0.58, 0.26],
                [0.12, 0.28, 0.48, 0.76, 0.43],
                [0.20, 0.36, 0.42, 0.62, 0.71],
                [0.30, 0.24, 0.38, 0.54, 0.68],
            ]

            for r, row in enumerate(values):
                for c, val in enumerate(row):
                    shade = 0.98 - 0.50 * val
                    fc = (shade, shade, shade)
                    ax.add_patch(
                        Rectangle(
                            (x + c * cell_w, y + (3 - r) * cell_h),
                            cell_w,
                            cell_h,
                            facecolor=fc,
                            edgecolor="white",
                            linewidth=0.72,
                        )
                    )
            ax.add_patch(Rectangle((x, y), 5 * cell_w, 4 * cell_h, facecolor="none", edgecolor=line, linewidth=0.9))
            for c, lab in enumerate(["$h_1$", "$h_2$", "$\\cdots$", "", "$h_L$"]):
                xpos = x + (c + 0.5) * cell_w
                if lab:
                    text(xpos, y - 3.0, lab, fs=6.8, color=muted)
            text(x + 5 * cell_w + 3.0, y + 2 * cell_h, "$k$", fs=6.9, color=muted, rotation=90)

        section(17, 90, "Codificador", 25)
        section(50, 90, "Atenção temporal", 30)
        section(83, 90, "Decodificador", 25)

        xs = [8.0, 17.5, 27.0]
        inputs = ["$x_{t-L+1}$", "$\\cdots$", "$x_t$"]
        hids = ["$h_1$", "$\\cdots$", "$h_L$"]
        for x, inp, hid in zip(xs, inputs, hids):
            rect(x - 3.8, 73.0, 7.6, 7.0, inp, fc="white", fs=6.7, weight="bold")
            rect(x - 3.8, 55.0, 7.6, 7.1, hid, fc=fill_dark, fs=7.2, weight="bold")
            arr((x, 73.0), (x, 62.2), lw=0.9, ms=8.2)
        text(17.5, 47.5, "janela histórica ($L$ instantes)", fs=7.2, color=muted)
        arr((31.0, 58.5), (38.1, 65.4), lw=0.95, ms=8.8)

        text(50, 77.5, "matriz de pesos $\\alpha_{k,j}$", fs=8.1, weight="bold")
        attention_matrix(39.9, 59.0)
        arr((50, 59.0), (50, 49.5), lw=0.9, ms=8.5)
        rect(
            41.1,
            39.2,
            17.8,
            9.5,
            "$c_k=\\sum_j \\alpha_{k,j}h_j$",
            fc=accent_fill,
            ec=accent,
            fs=7.6,
            weight="bold",
        )
        text(50, 33.0, "contexto do horizonte $k$", fs=6.9, color=muted)
        arr((59.1, 44.0), (70.3, 44.0), lw=0.95, ms=8.8)

        rect(70.6, 72.7, 24.8, 8.0, "$\\tilde{y}_{t+k-1}$  e  $z_{t+k}$", fc=fill_dark, fs=7.0, weight="bold")
        rect(75.7, 57.5, 14.6, 7.8, "$s_k$", fc=fill_mid, fs=8.3, weight="bold")
        rect(71.4, 40.2, 23.2, 8.1, "$g_{\\theta}(s_k,c_k,z_{t+k})$", fc="white", fs=6.9, weight="bold")
        arr((83.0, 72.7), (83.0, 65.5), lw=0.9, ms=8.2)
        arr((83.0, 57.5), (83.0, 48.4), lw=0.9, ms=8.2)
        text(71.0, 67.6, "$k=1,\\ldots,H$", fs=6.9, color=muted, ha="left")

        out_x = [75.0, 83.0, 91.0]
        output_labels = ["$\\hat{y}_{t+1}$", "$\\cdots$", "$\\hat{y}_{t+H}$"]
        for x, out in zip(out_x, output_labels):
            rect(x - 3.4, 25.7, 6.8, 6.9, out, fc="white", fs=6.7, weight="bold")
            arr((x, 40.2), (x, 32.8), lw=0.78, ms=7.5)
        ax.plot([75.0, 91.0], [22.1, 22.1], color=rule, linewidth=0.8)
        ax.plot([75.0, 75.0], [22.1, 23.6], color=rule, linewidth=0.8)
        ax.plot([91.0, 91.0], [22.1, 23.6], color=rule, linewidth=0.8)
        text(83, 18.8, "sequência prevista ($H$ passos)", fs=6.8, color=muted)

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

    label(ax, 50, 94, "XGBoost com saída múltipla: janela temporal supervisionada", fs=16.5, weight="bold")
    label(ax, 50, 89, "Uma janela com L instantes é transformada em vetor de atributos; a saída contém H previsões", fs=10, color=COLORS["muted"])

    group(ax, 3, 18, 26, 62, "Janela temporal com L instantes", COLORS["blue"])
    table_x, table_y = 5.4, 33
    col_w, row_h = 4.75, 5.1
    headers = ["alvo", "exóg.\n1", "exóg.\n2", "tempo"]
    rows = ["t-L+1", "...", "t"]
    for c, head in enumerate(headers):
        box(ax, table_x + c * col_w, table_y + 18, col_w, row_h, head, COLORS["blue_light"], COLORS["blue"], lw=1.1, fs=7.0, weight="bold")
    for r, row in enumerate(rows):
        label(ax, table_x - 2.2, table_y + 14 - r * row_h, row, fs=8.5, color=COLORS["muted"])
        for c in range(len(headers)):
            fc = COLORS["white"] if r != 1 else COLORS["slate_light"]
            ax.add_patch(Rectangle((table_x + c * col_w, table_y + 11 - r * row_h), col_w, row_h, facecolor=fc, edgecolor=COLORS["blue"], linewidth=0.9))
    label(ax, 15.8, 26, "defasagens,\nindicadores e atributos", fs=9.5, color=COLORS["muted"])

    arrow(ax, (29, 49), (36, 49), COLORS["line"], lw=2.4)
    label(ax, 32.4, 55, "vetorização +\natributos", fs=9, color=COLORS["muted"])

    group(ax, 36, 18, 23, 62, "Vetor de atributos", COLORS["violet"])
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

    group(ax, 90, 18, 8, 62, "Saída", COLORS["amber"])
    ys = [68, 61, 54, 47, 40, 33]
    labels = ["$\\hat{y}_{t+1}$", "$\\hat{y}_{t+2}$", "$\\cdots$", "$\\hat{y}_{t+H-1}$", "$\\hat{y}_{t+H}$", "$H$ previsões"]
    for y, text in zip(ys, labels):
        fc = COLORS["amber_light"] if text != "$H$ previsões" else COLORS["slate_light"]
        box(ax, 92.0, y - 2.6, 4.3, 5.2, text, fc, COLORS["amber"], lw=1.1, fs=7.4, weight="bold")

    label(ax, 50, 8, "Os atributos derivados da janela alimentam árvores impulsionadas com saída multi-horizonte.", fs=10, color=COLORS["muted"])
    save(fig, "diagrama_xgboost_multioutput_proprio")


if __name__ == "__main__":
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    draw_seq2seq_attention()
    draw_xgboost()
