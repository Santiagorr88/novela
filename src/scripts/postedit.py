"""
Utility functions for post-LLM chapter editing in the pipeline.

Functions:
- take_rewritten_text_or_fallback(llm_output: str, fallback_text: str) -> str
- apply_inline_patches(llm_report: str, base_text: str) -> str

Expected upstream agent formats:

Repetition Sentinel output:
===JSON===
{ ...json... }
===REVISED CHAPTER===
<full revised chapter>

Rhythm & Contrast Coach output:
===METRICS===
...
===FIXES===
...
===PATCHES===
(near para 18) ...one-sentence or two-sentence patch...
"""

from __future__ import annotations
import json
import re
from typing import List, Optional

JSON_MARK = "===JSON==="
REVISED_MARK = "===REVISED CHAPTER==="
METRICS_MARK = "===METRICS==="
FIXES_MARK = "===FIXES==="
PATCHES_MARK = "===PATCHES==="


def _find_section(text: str, start_marker: str, end_markers: Optional[List[str]] = None) -> Optional[str]:
    """Return text between start_marker and the earliest of end_markers (or end of text)."""
    if text is None:
        return None
    start_idx = text.find(start_marker)
    if start_idx == -1:
        return None
    start = start_idx + len(start_marker)
    if not end_markers:
        return text[start:].strip()
    ends = [text.find(m, start) for m in end_markers]
    ends = [e for e in ends if e != -1]
    end = min(ends) if ends else len(text)
    return text[start:end].strip()


def _split_paragraphs(text: str) -> List[str]:
    """Split on blank-line boundaries to get coarse paragraphs."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    paras = re.split(r"\n{2,}", text)
    return [p.strip() for p in paras] if paras else []


def _join_paragraphs(paras: List[str]) -> str:
    return "\n\n".join(p for p in paras if p is not None)


def take_rewritten_text_or_fallback(llm_output: str, fallback_text: str) -> str:
    """
    Prefer the fully revised chapter after the '===REVISED CHAPTER===' marker.
    If not present, attempt to apply JSON 'rewritten_paragraphs' patches.
    Otherwise, return the fallback_text unchanged.
    """
    if not llm_output or not isinstance(llm_output, str):
        return fallback_text

    # 1) Try to take the full revised chapter section
    revised = _find_section(llm_output, REVISED_MARK)
    if revised and len(revised.split()) > 10:
        return revised.strip()

    # 2) Try to parse the JSON section and apply 'rewritten_paragraphs'
    json_section = _find_section(llm_output, JSON_MARK, end_markers=[REVISED_MARK, METRICS_MARK, FIXES_MARK, PATCHES_MARK])
    if json_section:
        try:
            payload = json.loads(json_section)
            paras = _split_paragraphs(fallback_text)
            changed = False
            for item in payload.get("rewritten_paragraphs", []):
                idx = item.get("idx")
                new_text = item.get("after") or item.get("rewrite") or item.get("text")
                if isinstance(idx, int) and new_text:
                    # support both 0-based and 1-based indices
                    if idx < 0:
                        continue
                    target = idx if idx < len(paras) else (idx - 1 if idx - 1 < len(paras) else None)
                    if target is not None and 0 <= target < len(paras):
                        paras[target] = new_text.strip()
                        changed = True
                    elif idx == len(paras):
                        paras.append(new_text.strip())
                        changed = True
            if changed:
                return _join_paragraphs(paras)
        except Exception:
            pass

    return fallback_text


def apply_inline_patches(llm_report: str, base_text: str) -> str:
    """
    Parse the '===PATCHES===' section. Each patch line should look like:
        (near para 18) New sentence(s) here...
    Optionally lines may start with "- " for bullets.
    Insert the patch AFTER the indicated paragraph. Index is 0-based if 0 exists; otherwise treat as 1-based.
    If the index is out of range, append at the end.
    """
    if not llm_report or not isinstance(llm_report, str):
        return base_text

    patches = _find_section(llm_report, PATCHES_MARK)
    if not patches:
        return base_text

    paras = _split_paragraphs(base_text)
    if not paras:
        paras = [base_text.strip()] if base_text else []

    for raw_line in [ln for ln in patches.splitlines() if ln.strip()]:
        line = raw_line.strip()
        if line.startswith("- "):
            line = line[2:].strip()

        m = re.match(r"\(near\s+para\s+(\d+)\)\s*(.+)", line, flags=re.IGNORECASE)
        if not m:
            paras.append(line)
            continue

        idx_str, content = m.groups()
        try:
            idx = int(idx_str)
        except ValueError:
            paras.append(content.strip())
            continue

        insert_after = idx if (0 <= idx < len(paras)) else (idx - 1 if (idx - 1) >= 0 and (idx - 1) < len(paras) else None)

        if insert_after is None:
            paras.append(content.strip())
        else:
            insert_pos = insert_after + 1
            paras.insert(insert_pos, content.strip())

    return _join_paragraphs(paras)
