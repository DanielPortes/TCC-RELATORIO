from pathlib import Path
from math import atan2, cos, sin

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figuras"
PNG_PATH = FIG_DIR / "diagrama_neuronio_artificial_proprio.png"
PDF_PATH = FIG_DIR / "diagrama_neuronio_artificial_proprio.pdf"

SCALE = 3
WIDTH = 1500
HEIGHT = 720
BLACK = "#111111"
WHITE = "#ffffff"


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    font_name = "cambriab.ttf" if bold else "cambria.ttc"
    font_path = Path("C:/Windows/Fonts") / font_name
    return ImageFont.truetype(str(font_path), size * SCALE)


def _xy(x: float, y: float) -> tuple[int, int]:
    return int(round(x * SCALE)), int(round(y * SCALE))


def text(draw: ImageDraw.ImageDraw, x: float, y: float, value: str, size=26, bold=False, anchor="mm") -> None:
    draw.text(_xy(x, y), value, font=_font(size, bold), fill=BLACK, anchor=anchor)


def multiline_text(draw: ImageDraw.ImageDraw, x: float, y: float, value: str, size=25, bold=False) -> None:
    draw.multiline_text(
        _xy(x, y),
        value,
        font=_font(size, bold),
        fill=BLACK,
        anchor="mm",
        align="center",
        spacing=8 * SCALE,
    )


def indexed_symbol(draw: ImageDraw.ImageDraw, x: float, y: float, base: str, subscript: str, size=34) -> None:
    base_dx = -5 if base == "x" else -7
    sub_dx = 12 if base == "x" else 16
    text(draw, x + base_dx, y, base, size=size, bold=True)
    text(draw, x + sub_dx, y + 10, subscript, size=int(size * 0.56), bold=True)


def circle(draw: ImageDraw.ImageDraw, cx, cy, r, width=3) -> None:
    x0, y0 = _xy(cx - r, cy - r)
    x1, y1 = _xy(cx + r, cy + r)
    draw.ellipse((x0, y0, x1, y1), fill=WHITE, outline=BLACK, width=width * SCALE)


def box(draw: ImageDraw.ImageDraw, xy, width=3) -> None:
    scaled_xy = tuple(int(round(v * SCALE)) for v in xy)
    draw.rectangle(scaled_xy, fill=WHITE, outline=BLACK, width=width * SCALE)


def line(draw: ImageDraw.ImageDraw, points, width=3) -> None:
    draw.line([_xy(x, y) for x, y in points], fill=BLACK, width=width * SCALE)


def vertical_dots(draw: ImageDraw.ImageDraw, x: float, y: float) -> None:
    for offset in (-18, 0, 18):
        cx, cy = _xy(x, y + offset)
        r = 3 * SCALE
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=BLACK)


def arrow(draw: ImageDraw.ImageDraw, start, end, width=4, head=18) -> None:
    x0, y0 = start
    x1, y1 = end
    draw.line((_xy(x0, y0), _xy(x1, y1)), fill=BLACK, width=width * SCALE)
    angle = atan2(y1 - y0, x1 - x0)
    spread = 0.48
    p1 = (
        x1 - head * cos(angle - spread),
        y1 - head * sin(angle - spread),
    )
    p2 = (
        x1 - head * cos(angle + spread),
        y1 - head * sin(angle + spread),
    )
    draw.polygon([_xy(x1, y1), _xy(*p1), _xy(*p2)], fill=BLACK)


def draw_png() -> None:
    img = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), WHITE)
    draw = ImageDraw.Draw(img)

    line(draw, [(24, 24), (1476, 24), (1476, 696), (24, 696), (24, 24)], 3)

    text(draw, 112, 410, "Entradas", size=34, bold=True)
    line(draw, [(205, 240), (185, 240), (185, 560), (205, 560)], 3)

    rows = [
        (250, "1"),
        (380, "2"),
        (540, "d"),
    ]
    for y, subscript in rows:
        indexed_symbol(draw, 275, y, "x", subscript, size=34)
        arrow(draw, (345, y), (460, y), 4, 18)
        circle(draw, 545, y, 57, 3)
        indexed_symbol(draw, 545, y, "w", subscript, size=35)

    vertical_dots(draw, 275, 460)
    vertical_dots(draw, 545, 460)
    text(draw, 545, 630, "Pesos", size=34, bold=True)

    arrow(draw, (600, 270), (770, 330), 4, 18)
    arrow(draw, (604, 380), (765, 380), 4, 18)
    arrow(draw, (600, 520), (770, 430), 4, 18)

    text(draw, 850, 80, "Viés", size=34, bold=True)
    circle(draw, 850, 160, 48, 3)
    text(draw, 850, 160, "b", size=35, bold=True)
    arrow(draw, (850, 208), (850, 275), 4, 18)

    circle(draw, 850, 380, 95, 3)
    text(draw, 850, 363, "Σ", size=62, bold=True)
    text(draw, 850, 500, "Soma ponderada", size=29, bold=True)

    arrow(draw, (945, 380), (1060, 380), 5, 20)
    box(draw, (1060, 315, 1200, 445), 3)
    text(draw, 1130, 380, "φ", size=45, bold=True)
    multiline_text(draw, 1130, 520, "Função de\nativação", size=29, bold=True)

    arrow(draw, (1200, 380), (1320, 380), 5, 20)
    text(draw, 1372, 380, "ŷ", size=42, bold=True)
    text(draw, 1372, 465, "Saída", size=34, bold=True)

    FIG_DIR.mkdir(parents=True, exist_ok=True)
    img = img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    img.save(PNG_PATH)


def draw_pdf() -> None:
    page = landscape((WIDTH, HEIGHT))
    c = canvas.Canvas(str(PDF_PATH), pagesize=page)
    c.drawImage(ImageReader(str(PNG_PATH)), 0, 0, width=WIDTH, height=HEIGHT)
    c.showPage()
    c.save()


if __name__ == "__main__":
    draw_png()
    draw_pdf()
