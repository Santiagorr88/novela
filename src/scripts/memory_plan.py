# src/scripts/memory_plan.py
import os
import json
from pathlib import Path
from typing import Optional
import ast, re

# Rutas base (alineadas con tu estructura actual)
RECAP_DIR = Path("src/chapters/recap")
MEM_DIR   = Path("src/chapters/memory")


# -------------------------------
# Helpers internos
# -------------------------------

def _cid(ch: int) -> str:
    """Devuelve el código de capítulo con formato B1Cxx."""
    return f"B1C{int(ch):02d}"


def _ensure_dir(p: Path):
    """Crea el directorio padre si no existe."""
    p.parent.mkdir(parents=True, exist_ok=True)


def _first_prose_paragraph(md: str) -> str:
    """
    Extrae el primer párrafo de PROSA útil desde un markdown, evitando:
    - Encabezados (#, ##, etc.)
    - Listas iniciales (*, -, +)
    - Separadores (---, ***, —)
    - Líneas típicas de TOC/headers (Part, Parts, Chapter, B1Cxx)
    """
    if not md:
        return ""

    md = md.replace("\r\n", "\n")
    lines = md.split("\n")

    cleaned = []
    skipping_front = True
    for ln in lines:
        l = ln.strip()

        if skipping_front and (
            l.startswith("#") or
            l.startswith(("* ", "- ", "+ ")) or
            l.startswith(("Part ", "Parts ", "Chapter ", "B1C")) or
            l in ("---", "—", "***", "")
        ):
            # Saltamos front matter, títulos, listas o separadores del arranque
            continue

        skipping_front = False
        cleaned.append(ln)

    body = "\n".join(cleaned).strip()
    if not body:
        body = md.strip()

    # Primer párrafo de prosa (no encabezado/lista)
    paras = [p.strip() for p in body.split("\n\n") if p.strip()]
    if not paras:
        return ""

    for p in paras:
        if not p.startswith("#") and not p.startswith(("* ", "- ", "+ ")):
            return p

    return paras[0]


# -------------------------------
# API PÚBLICA
# -------------------------------


SEP = "\n\n---\n\n"

def get_rolling_memory(chapter_no, part_no: Optional[int] = None, max_chars: int = 12000) -> str:
    """
    Devuelve memoria narrativa consolidada como TEXTO:

      1) Recaps de capítulos anteriores (o full_recap si existe).
      2) Si se está en modo por-parte y part_no > 1:
         añade un bloque con P01..P(part_no-1) del capítulo actual,
         leídos de src/chapters/memory/B1Cxx/B1CxxPyy.json

    MODO CAPÍTULO (recomendado cuando generas todo el capítulo de una vez):
      - Llama con part_no=None o part_no=0 → NO se añade ningún resumen de partes del capítulo actual.

    max_chars: si se especifica, recorta la memoria resultante por el principio
               (deja lo más reciente) para mantenerla dentro de ese tamaño aprox.
    """
    chapter_no = int(chapter_no)
    pn = None if part_no is None else int(part_no)

    # 1) Carga recaps previos
    full_path = RECAP_DIR / "full_recap.md"
    if full_path.exists():
        try:
            prev_text = full_path.read_text(encoding="utf-8")
        except Exception:
            prev_text = ""
    else:
        prev_text = ""
        for i in range(1, chapter_no):
            path = RECAP_DIR / f"{_cid(i)}_recap.md"
            if path.exists():
                try:
                    prev_text += f"{SEP}# {_cid(i)} Recap\n" + path.read_text(encoding="utf-8")
                except Exception:
                    continue

    # 2) Añade partes previas del capítulo actual (solo modo por-parte con pn > 1)
    current_parts_text = ""
    if pn is not None and pn > 1:
        cid = _cid(chapter_no)
        part_lines = []
        for p in range(1, pn):
            j = MEM_DIR / cid / f"{cid}P{p:02d}.json"
            if j.exists():
                try:
                    data = json.loads(j.read_text(encoding="utf-8"))
                    summary = (data.get("summary") or "").strip()
                    if summary:
                        part_lines.append(f"- {cid}P{p:02d}: {summary}")
                except Exception:
                    continue
        if part_lines:
            header = f"{SEP}# {cid} — Current Chapter So Far (Parts 01–{pn-1:02d})\n"
            current_parts_text = header + "\n".join(part_lines) + "\n"

    out = (prev_text + current_parts_text).strip()

    # 3) Recorte opcional por tamaño (con corte limpio en separador si aparece pronto)
    if max_chars and len(out) > max_chars:
        out = out[-max_chars:]  # mantiene lo más reciente
        cut = out.find(SEP)
        if 0 < cut < 2000:      # si el separador aparece al inicio del recorte, limpia hasta después de SEP
            out = out[cut + len(SEP):]

    return out

# === Wrappers explícitos (recomendado para el YAML) ===

def get_rolling_memory_for_chapter(*, chapter_no: int, max_chars: int = 12000) -> str:
    """Modo capítulo: ignora partes del capítulo actual."""
    return get_rolling_memory(chapter_no=chapter_no, part_no=None, max_chars=max_chars)

def get_rolling_memory_for_part(*, chapter_no: int, part_no: int, max_chars: int = 12000) -> str:
    """Modo por-parte: incluye P01..P(part_no-1) si part_no > 1."""
    return get_rolling_memory(chapter_no=chapter_no, part_no=part_no, max_chars=max_chars)


def get_last_n_recaps(chapter_no: int, n: int = 3) -> str:
    """Devuelve los últimos N recaps para memoria compacta."""
    content = ""
    for i in range(max(1, chapter_no - n), chapter_no):
        path = RECAP_DIR / f"{_cid(i)}_recap.md"
        if path.exists():
            try:
                content += f"\n\n---\n\n# {_cid(i)} Recap\n" + path.read_text(encoding="utf-8")
            except Exception:
                continue
    return content


def get_chapter_plan(chapter_no: int) -> str:
    """Genera un esquema base genérico del capítulo usando su número."""
    return (
        f"Plan for Chapter {chapter_no}:\n"
        "- Opening tension beat\n- Reveal or mystery beat\n"
        "- Character decision or interaction\n- Twist or complication\n"
        "- Hook to next chapter"
    )


def get_previous_recap(chapter_no: int) -> str:
    """Carga el resumen del capítulo anterior si existe."""
    chapter_no = int(chapter_no)
    if chapter_no <= 1:
        return ""
    recap_path = RECAP_DIR / f"{_cid(chapter_no - 1)}_recap.md"
    if recap_path.exists():
        try:
            return recap_path.read_text(encoding="utf-8")
        except Exception:
            return ""
    return ""


def build_part_memory_delta(chapter_no: int, part_no: int, text_en: str):
    """
    Extrae una memoria compacta de la PARTE.
    Estrategia robusta:
      - Limpia headers/TOC del inicio
      - Toma el primer párrafo de prosa real
      - Lo limita a ~600 chars
    (Puedes enriquecer con 'events', 'open_threads', 'characters', 'locations')
    """
    summary = ""
    if text_en:
        summary = _first_prose_paragraph(text_en)[:600]

    delta = {
        "chapter": int(chapter_no),
        "part": int(part_no),
        "summary": summary,
        "events": [],          # opcional: si integras extractor por parte
        "open_threads": [],    # opcional: pistas o preguntas abiertas
        "characters": {},      # opcional: estados clave por personaje
        "locations": []        # opcional
    }
    return delta


def update_memory_from_part(delta: dict) -> str:
    """
    Persiste el delta como JSON en:
      src/chapters/memory/B1Cxx/B1CxxPyy.json

    Acepta:
      - dict
      - str con JSON estricto
      - str con dict estilo Python ({'a':1})
      - str con claves sin comillas ({a:1})
      - str que es ruta a archivo JSON
    """
    # Normalizar 'delta' a dict
    if isinstance(delta, str):
        s = delta.strip()
        # 1) ¿Es ruta a archivo?
        if os.path.exists(s):
            try:
                delta = json.loads(Path(s).read_text(encoding="utf-8"))
            except Exception as e:
                raise TypeError(f"update_memory_from_part: archivo no es JSON válido: {e}")
        else:
            # 2) Intento JSON estricto
            try:
                delta = json.loads(s)
            except Exception:
                # 3) Intento literal_eval de dict Python
                try:
                    maybe = ast.literal_eval(s)
                    if isinstance(maybe, dict):
                        delta = maybe
                    else:
                        raise ValueError("literal_eval no devolvió dict")
                except Exception:
                    # 4) Arreglo laxo: comillar claves y cambiar comillas simples→dobles
                    try:
                        # comilla claves sin comillas: {a: 1, b_c2: 3} -> {"a": 1, "b_c2": 3}
                        s_fixed = re.sub(r'([{,]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:',
                                         r'\1"\2":', s)
                        s_fixed = s_fixed.replace("'", '"')
                        delta = json.loads(s_fixed)
                    except Exception as e2:
                        preview = s[:200].replace("\n", "\\n")
                        raise TypeError(
                            f"update_memory_from_part: 'delta' inválido ({type(delta)}). "
                            f"No pude parsear. Muestra: {preview} ... Error: {e2}"
                        )

    if not isinstance(delta, dict):
        raise TypeError(f"update_memory_from_part: se esperaba dict, llegó {type(delta)}")

    try:
        ch = int(delta.get("chapter"))
        pn = int(delta.get("part"))
    except Exception as e:
        raise ValueError(f"update_memory_from_part: 'chapter'/'part' faltan o no son enteros: {e}")

    cid = _cid(ch)
    out = MEM_DIR / cid / f"{cid}P{pn:02d}.json"
    _ensure_dir(out)
    out.write_text(json.dumps(delta, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(out)


def build_chapter_memory_delta(chapter_no: int, text_en: str):
    """
    Crea un delta de MEMORIA a nivel CAPÍTULO.
    - summary: primer párrafo de prosa útil (limpia H1/H3/listas)
    - parts: títulos H3 detectados (orden)
    """
    summary = _first_prose_paragraph(text_en)[:900] if text_en else ""
    # extrae H3 como lista de títulos de partes
    import re
    h3_titles = re.findall(r'^\s*###\s+(.+?)\s*$', text_en or "", flags=re.M)
    return {
        "chapter": int(chapter_no),
        "summary": summary,
        "parts": h3_titles,
        "events": [],          # opcional: puedes rellenar con event_extractor
        "themes": [],          # opcional
        "characters": {}       # opcional: estados clave
    }

def update_memory_from_chapter(delta: dict) -> str:
    """
    Persiste capítulo a: src/chapters/memory/B1Cxx/B1Cxx.json
    """
    if not isinstance(delta, dict):
        import json, ast
        try:
            delta = json.loads(delta)
        except Exception:
            delta = ast.literal_eval(delta)

    ch = int(delta.get("chapter"))
    cid = _cid(ch)
    out = MEM_DIR / cid / f"{cid}.json"
    _ensure_dir(out)
    out.write_text(json.dumps(delta, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(out)