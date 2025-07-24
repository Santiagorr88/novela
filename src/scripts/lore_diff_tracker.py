import difflib
from pathlib import Path

LORE_PATH = Path("src/lore/prompt_universo.md")

def load_lore():
    return LORE_PATH.read_text().strip()

def find_lore_conflicts(chapter_text: str, threshold: float = 0.85) -> list[str]:
    """
    Compara cada oración del capítulo con el lore base.
    Retorna oraciones con alta similitud que podrían implicar contradicción.
    """
    lore = load_lore()
    lore_lines = [l.strip() for l in lore.splitlines() if l.strip()]
    chapter_lines = [l.strip() for l in chapter_text.splitlines() if l.strip()]

    issues = []

    for c_line in chapter_lines:
        for l_line in lore_lines:
            ratio = difflib.SequenceMatcher(None, c_line.lower(), l_line.lower()).ratio()
            if ratio > threshold and c_line.lower() != l_line.lower():
                issues.append(f"⚠️ Posible contradicción:\n - Capítulo: \"{c_line}\"\n - Lore: \"{l_line}\"")

    return issues


def check_lore_conflicts(chapter_text: str, lore_path: str = "src/lore/prompt_universo.md") -> str:
    """Compara el capítulo contra el lore base y detecta contradicciones sospechosas."""
    lore = Path(lore_path).read_text()
    conflicts = []

    lore_lines = [line.strip() for line in lore.splitlines() if line.strip()]
    chapter_lines = [line.strip() for line in chapter_text.splitlines() if line.strip()]

    for lore_line in lore_lines:
        matches = difflib.get_close_matches(lore_line, chapter_lines, n=1, cutoff=0.7)
        if not matches:
            conflicts.append(f"❗ Posible contradicción con lore: «{lore_line}»")

    if not conflicts:
        return "PASS"
    return "FIX:\n" + "\n".join(conflicts)
