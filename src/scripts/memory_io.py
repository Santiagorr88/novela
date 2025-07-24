import os, json, pathlib

BASE = pathlib.Path(__file__).parent.parent.parent
DATA = BASE / "output" / "memory.json"
COUNTER_DIR = BASE / "output" / "memory"

DATA.parent.mkdir(parents=True, exist_ok=True)
COUNTER_DIR.mkdir(parents=True, exist_ok=True)

if not DATA.exists():
    DATA.write_text(json.dumps({"chapters": []}, indent=2))

def _load():
    return json.loads(DATA.read_text())

def _save(obj):
    DATA.write_text(json.dumps(obj, indent=2))

# 1. Obtener número consecutivo e incrementar
def next_chapter_number(book_no: int = 1, counter_path: str = None) -> int:
    if counter_path:
        path = pathlib.Path(counter_path)
    else:
        path = COUNTER_DIR / f"book_{book_no}_counter.txt"

    if path.exists():
        try:
            n = int(path.read_text().strip()) + 1
        except ValueError:
            n = 1
    else:
        n = 1

    path.write_text(str(n))
    return int(n)  # ← Garantiza que devuelve un entero

# 2. Obtener número actual sin incrementarlo
def get_current_chapter_number(book_no: int = 1) -> int:
    path = COUNTER_DIR / f"book_{book_no}_counter.txt"
    if path.exists():
        try:
            return int(path.read_text().strip())
        except ValueError:
            return 1
    return 1

# 3. Añadir capítulo completo
def append_chapter(text, text_es):
    db = _load()
    db["chapters"].append({"en": text, "es": text_es})
    _save(db)

# 4. Contador rápido
def chapter_count() -> int:
    return len(_load()["chapters"])

# 5. Registrar el siguiente número (solo cuando todo se completa bien)
def register_next_chapter_number(book_no: int, current_chapter: int):
    path = COUNTER_DIR / f"book_{book_no}_counter.txt"
    next_ch = int(current_chapter) + 1  # ← por si viene como str
    path.write_text(str(next_ch))
