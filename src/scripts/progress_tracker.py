# src/scripts/progress_tracker.py
import json
import ast

def _coerce_to_dict(obj):
    """Acepta dict, JSON str o str estilo dict de Python y devuelve dict."""
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, str):
        # intenta JSON primero
        try:
            return json.loads(obj)
        except Exception:
            # fallback: literal_eval para "{'a':1}" etc.
            try:
                return ast.literal_eval(obj)
            except Exception as e:
                raise ValueError(f"No se pudo parsear progreso/estado: {e}")
    raise TypeError(f"Tipo no soportado: {type(obj)}")


def load_progress(path="output/position.json"):
    """Carga el estado de progreso. Soporta JSON o str con dict de Python.
       Si no existe, devuelve estado inicial (C1, P1, total_parts=-1)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
    except FileNotFoundError:
        return {"current_chapter": 1, "current_part": 1, "total_parts": -1}

    # Normaliza comillas simples mal guardadas
    s = data.strip()
    if s.startswith("{") and "'" in s and '"' not in s:
        s = s.replace("'", '"')

    # Intentos de parseo seguros
    try:
        return json.loads(s)
    except Exception:
        try:
            return ast.literal_eval(s)
        except Exception as e:
            raise ValueError(f"No se pudo parsear position.json: {e}")


def _coerce_to_int(x, default=0):
    try:
        return int(x)
    except Exception:
        return default


def step_progress(current_state, actual_parts=None):
    """
    MODO POR-PARTE.
    Avanza a la siguiente parte. Si la parte actual es la última (== actual_parts),
    salta al siguiente capítulo y reinicia parte a 1. Pone total_parts=-1 para forzar
    recálculo la próxima vez.
    """
    state = current_state if isinstance(current_state, dict) else load_progress()
    chapter = _coerce_to_int(state.get("current_chapter", 1), 1)
    part = _coerce_to_int(state.get("current_part", 1), 1)
    total = _coerce_to_int(state.get("total_parts", -1), -1)

    if actual_parts is not None:
        total = _coerce_to_int(actual_parts, total)

    if total > 0 and part >= total:
        # Última parte -> pasar a siguiente capítulo
        chapter += 1
        part = 1
        total = -1
    else:
        part += 1

    return {"current_chapter": chapter, "current_part": part, "total_parts": total}


# === NUEVO: avanzar por capítulo completo (modo capítulo one-shot) ===
def step_progress_full_chapter(current_state, actual_parts=None):
    """
    MODO CAPÍTULO COMPLETO.
    Se asume que acabas de generar *todas* las partes del capítulo actual.
    - Incrementa el capítulo en +1
    - Reinicia current_part=1
    - Resetea total_parts a -1 (para recálculo en el nuevo capítulo)
    - (Opcional) guarda el recuento real en 'last_total_parts' a modo de histórico
    """
    state = current_state if isinstance(current_state, dict) else load_progress()
    chapter = _coerce_to_int(state.get("current_chapter", 1), 1)
    last_total = _coerce_to_int(actual_parts if actual_parts is not None else state.get("total_parts", -1), -1)
    return {
        "current_chapter": chapter + 1,
        "current_part": 1,
        "total_parts": -1,
        "last_total_parts": last_total,  # no imprescindible; útil para logs/analítica
    }


def save_progress(progress, path="output/position.json"):
    # Acepta dict o str y normaliza (sin eval)
    if not isinstance(progress, dict):
        try:
            progress = json.loads(progress)
        except Exception:
            try:
                progress = ast.literal_eval(progress)
            except Exception as e:
                raise ValueError(f"No se pudo serializar progreso: {e}")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def build_step_position(chapter_number: int, part_number: int, total_parts: int) -> dict:
    """Factory legacy (modo por-parte)."""
    return {
        "current_chapter": int(chapter_number),
        "current_part": int(part_number),
        "total_parts": int(total_parts),
    }


# === NUEVO: factory para modo capítulo completo ===
def build_chapter_position(chapter_number: int, total_parts: int) -> dict:
    """
    Construye un estado para capítulo *completo* (sin interés en la parte actual).
    current_part queda en 1 por convención.
    """
    return {
        "current_chapter": int(chapter_number),
        "current_part": 1,
        "total_parts": int(total_parts),
    }


def set_total_parts(current_state, total_parts: int):
    """
    Devuelve un nuevo estado con total_parts actualizado (útil si lo calculas
    a partir de chapter_parts_list).
    """
    state = current_state if isinstance(current_state, dict) else load_progress()
    state["total_parts"] = int(total_parts)
    return state


# Utilidad para extraer ints de un estado que puede ser str o dict
def get_int_field(state, key):
    state = _coerce_to_dict(state)
    return int(state.get(key, 0))


def count(*, items) -> int:
    try:
        return len(items)
    except Exception:
        return 0