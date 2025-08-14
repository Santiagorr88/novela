# src/scripts/chapter_assembler.py
from pathlib import Path
import re, json, ast
import os
from typing import List, Dict

def _coerce_part_titles(part_titles):
    if isinstance(part_titles, list):
        return part_titles
    if isinstance(part_titles, str):
        s = part_titles.strip()
        # JSON list
        if s.startswith("[") and s.endswith("]"):
            try:
                return json.loads(s)
            except Exception:
                pass
        # Python list literal
        try:
            return ast.literal_eval(s)
        except Exception:
            pass
        # CSV simple
        if "," in s:
            return [t.strip() for t in s.split(",")]
        return [s]
    return [str(part_titles)]

def _find_part_file(chapter_id: str, idx: int):
    # nombres posibles
    fnames = [
        f"{chapter_id}P{idx}.md",
        f"{chapter_id}P{idx:02d}.md",
        f"{chapter_id}P{idx}_texto.md",
        f"{chapter_id}P{idx:02d}_texto.md",
    ]
    # carpetas donde buscar (de más probable a menos)
    search_dirs = [
        Path("project") / "Chronicles_of_the_Sundering_Judgment" / "parts",
        # por si cambia la saga_title
        *[p for p in Path("project").glob("*/parts")],
        Path("src/chapters/parts"),
        Path("src/plan_cache"),
        Path("."),  # raíz como último recurso
    ]
    for d in search_dirs:
        for fn in fnames:
            p = d / fn
            if p.exists():
                return p
    return None

def assemble_chapter_from_files(
    chapter_id: str,
    part_number: int,
    chapter_title: str,
    part_titles: list[str],
    folder: str = "src/plan_cache"
) -> str:
    print(f"[assemble_chapter] ✅ chapter_id: {chapter_id}")
    print(f"[assemble_chapter] ✅ part_number (input): {part_number}")
    print(f"[assemble_chapter] ✅ part_titles: {part_titles}")
    print(f"[assemble_chapter] ✅ part_titles type: {type(part_titles)}")

    # Convertir títulos si vienen como string
    if isinstance(part_titles, str):
        try:
            part_titles = ast.literal_eval(part_titles)
        except Exception as e:
            raise ValueError(f"Error al convertir part_titles de str a list: {e}")

    # Tope por si viene mayor que la lista
    max_parts = min(int(part_number), len(part_titles) if part_titles else int(part_number))

    parts = [f"# {chapter_title}\n"]

    for i in range(1, max_parts + 1):
        # Probar múltiples patrones:
        candidates = [
            f"{chapter_id}P{i}_texto.md",
            f"{chapter_id}P{i}.md",
            f"{chapter_id}P{i:02d}_texto.md",
            f"{chapter_id}P{i:02d}.md",
        ]
        found_path = None
        for fname in candidates:
            path = os.path.join(folder, fname)
            if os.path.exists(path):
                found_path = path
                break

        if not found_path:
            print(f"[assemble_chapter] ⚠️ Parte no encontrada: {chapter_id}P{i}(.md|_texto.md)")
            continue

        with open(found_path, "r", encoding="utf-8") as f:
            content = f.read()
        lines = content.strip().splitlines()

        # Elimina encabezados H1 residuales del tipo "# BxCyPz – ..."
        filtered = [line for line in lines if not re.match(r"^#\s*B\d+C\d+P\d+", line)]

        title = part_titles[i - 1] if i - 1 < len(part_titles) else f"Part {i}"
        parts.append(f"## B{chapter_id[1]}C{chapter_id[-2:]}P{str(i).zfill(2)} — {title}\n")
        parts.append("\n".join(filtered))
        parts.append("")

    return "\n".join(parts).strip()


def prepend_headers(chapter_title: str, part_number: int, part_titles, content: str) -> str:
    """
    Prepara el archivo final de la PARTE (no del capítulo).
    Añade H1 del capítulo y H3 con el título de la parte actual.
    Elimina un H1/H2 residual si ya venía en 'content'.
    """
    part_number = int(part_number)
    titles = _coerce_part_titles(part_titles)

    # limpiar encabezado H1/H2 si el narrador lo puso
    lines = content.strip().splitlines()
    if lines and re.match(r"^#{1,3}\s*B\d+C\d+P\d+\s[-–:]", lines[0]):
        lines = lines[1:]
    cleaned = "\n".join(lines).strip()

    part_title = titles[part_number - 1].rstrip(":") if part_number - 1 < len(titles) else f"Part {part_number}"

    return f"# {chapter_title}\n\n### {part_title}\n\n{cleaned}"

def split_full_chapter_markdown(full_text: str, chapter_id: str, part_titles: List[str], folder: str = "src/plan_cache") -> Dict[int, str]:
    """
    Divide el capítulo completo en partes por cabeceras H1:
    '# B1CxxPyy – Título'
    Escribe cada parte en {folder}/{chapter_id}P{y}_texto.md
    Devuelve {parte_index: texto_parte}.
    """
    if not full_text or "# B" not in full_text:
        return {}

    # Patrón de H1 de parte
    pat = re.compile(r"^#\s*(B\d+C\d+P(\d+))\s*[-–]\s*(.+)$", re.MULTILINE)

    parts = {}
    matches = list(pat.finditer(full_text))
    for idx, m in enumerate(matches):
        start = m.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(full_text)
        block = full_text[start:end].strip()

        pnum = int(m.group(2))
        fname = f"{chapter_id}P{pnum}_texto.md"
        out_path = os.path.join(folder, fname)
        os.makedirs(folder, exist_ok=True)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(block)

        parts[pnum] = block

    return parts

def get_part_text(chapter_id: str, part_number: int, folder: str = "src/plan_cache") -> str:
    path = os.path.join(folder, f"{chapter_id}P{part_number}_texto.md")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

H_BCP   = re.compile(r'^\s*#{1,6}\s*B(\d+)C(\d+)P(\d+)\s*[-–—]\s*(.+?)\s*$', re.M)
H2_LINE = re.compile(r'^\s*##\s+(.+?)\s*$', re.M)
H3_LINE = re.compile(r'^\s*###\s+(.+?)\s*$', re.M)

def _normalize_titles(parts) -> List[str]:
    if isinstance(parts, list):
        return [str(x) for x in parts]
    if isinstance(parts, str):
        s = parts.strip()
        # intenta JSON primero
        try:
            maybe = json.loads(s)
            if isinstance(maybe, list):
                return [str(x) for x in maybe]
        except Exception:
            pass
        # intenta literal_eval (p. ej. "['a','b']")
        try:
            maybe = ast.literal_eval(s)
            if isinstance(maybe, list):
                return [str(x) for x in maybe]
        except Exception:
            pass
        # fallback: separa por comas si parece lista
        if "," in s and "[" in s and "]" in s:
            items = [t.strip(" '\"\t") for t in s.strip("[]").split(",")]
            return [t for t in items if t]
        # último recurso: un solo título
        return [s]
    # otro tipo: fuerza a str
    return [str(parts)]

def assemble_full_chapter_h1_h3(*, raw_content: str, chapter_title: str, chapter_parts) -> str:
    titles = _normalize_titles(chapter_parts)
    text = (raw_content or "").strip()

    # 1) "## BxCyPz – Título" -> "### {título canónico por Pz}"
    def repl_bcp(m):
        p_idx = int(m.group(3))
        fallback = m.group(4).strip()
        title = titles[p_idx-1] if 1 <= p_idx <= len(titles) else fallback
        return f"### {title}"
    text = H_BCP.sub(repl_bcp, text)

    # 2) H2 llanos -> H3
    text = H2_LINE.sub(r'### \1', text)

    # 3) Si ya hay H3, reescribe los N primeros con títulos canónicos
    h3 = list(H3_LINE.finditer(text))
    if h3:
        out, last = [], 0
        for i, m in enumerate(h3[:len(titles)], start=1):
            out.append(text[last:m.start()])
            out.append(f"### {titles[i-1]}")
            last = m.end()
        out.append(text[last:])
        body = "".join(out).lstrip()
        return f"# {chapter_title}\n\n{body}\n"

    # 4) Si no hay headings, al menos inserta los títulos en orden
    body = "\n\n".join([f"### {t}\n" for t in titles]) + "\n" + text
    return f"# {chapter_title}\n\n{body}\n"