# src/scripts/title_utils.py

import re
import unicodedata

def extract_title_line(markdown_text: str) -> str:
    """
    Devuelve la primera línea que empiece por '# ' (heading 1).
    """
    for line in markdown_text.splitlines():
        if line.lstrip().startswith("#"):
            return line.strip()
    raise ValueError("No H1 title line found.")

def extract_title_only(h1_line: str) -> str:
    """
    De '# B1C17 – Stone Doors' devuelve 'Stone Doors'
    """
    no_hash = h1_line.lstrip("#").strip()
    m = re.split(r"\s[-–:]\s", no_hash, maxsplit=1)
    if len(m) == 2:
        return m[1].strip()
    parts = no_hash.split(" ", 1)
    return parts[1].strip() if len(parts) > 1 else no_hash

def extract_prefix(h1_line: str) -> str:
    """
    De '# B1C17 – Stone Doors' extrae 'B1C17'
    """
    raw = h1_line.lstrip("#").strip()
    return raw.split(" ", 1)[0]

def slugify(text: str) -> str:
    """
    Slug básico: minúsculas, guiones, sin acentos.
    """
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text
