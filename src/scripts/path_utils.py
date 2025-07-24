# src/scripts/path_utils.py
import unicodedata
import re
import pathlib

def h1_to_filename(folder: str, h1_line: str, lang: str) -> str:
    """
    Convierte '# B1C6 – My Title' -> 'B1C6_My_Title_EN.pdf'
    """
    # Extrae H1 sin el '#' y lo limpia
    raw = h1_line.lstrip("#").strip()

    # Normaliza separador: "B1C6 – My Title" => ["B1C6", "My Title"]
    parts = re.split(r"\s[-–:]\s", raw, maxsplit=1)
    if len(parts) == 2:
        prefix, title = parts
    else:
        # fallback si no hay separador
        prefix = raw.split()[0]
        title = " ".join(raw.split()[1:])

    # Quitar acentos, mantener nombre seguro
    title_clean = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    title_safe = title_clean.strip().replace(" ", "_")

    full_name = f"{prefix}_{title_safe}_{lang.upper()}.pdf"
    path = pathlib.Path(folder) / lang.lower()
    path.mkdir(parents=True, exist_ok=True)
    return str(path / full_name)


def build_filename_h1_style(folder: str, prefix: str, title: str, lang: str) -> str:

    title_clean = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    safe_title = re.sub(r"[^a-zA-Z0-9]+", "_", title_clean).strip("_")

    path = pathlib.Path(folder) / lang.lower()
    path.mkdir(parents=True, exist_ok=True)

    filename = f"{prefix}_{safe_title}_{lang.upper()}.pdf"
    return str(path / filename)

