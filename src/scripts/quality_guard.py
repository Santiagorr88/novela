import re


def _word_count(text: str) -> int:
    if not text:
        return 0
    return len(re.findall(r"\b\w+\b", text))


def _paragraph_count(text: str) -> int:
    if not text:
        return 0
    parts = [p for p in re.split(r"\n{2,}", text.strip()) if p.strip()]
    return len(parts)


def check_chapter_quality(chapter_text: str, min_words: int, max_words: int, min_paragraphs: int = 1) -> str:
    """
    Return 'PASS' or 'FIX:\\n- ...' with objective chapter quality violations.
    """
    words = _word_count(chapter_text)
    paras = _paragraph_count(chapter_text)
    issues = []

    if words < int(min_words):
        issues.append(f"Word count too low: {words} < {int(min_words)}")
    if words > int(max_words):
        issues.append(f"Word count too high: {words} > {int(max_words)}")
    if paras < int(min_paragraphs):
        issues.append(f"Paragraph count too low: {paras} < {int(min_paragraphs)}")

    if not issues:
        return "PASS"
    return "FIX:\n" + "\n".join(f"- {i}" for i in issues)
