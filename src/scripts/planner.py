# src/scripts/planner.py
import pathlib, json

BASE = pathlib.Path("output/planner")
BASE.mkdir(parents=True, exist_ok=True)

# === Helpers ===
def _path(name):
    return BASE / f"{name}.json"

def _load(name):
    p = _path(name)
    return json.loads(p.read_text()) if p.exists() else {}

def _save(name, data):
    _path(name).write_text(json.dumps(data, indent=2))

# === Public ===
def get_chapter_plan(chapter_number: int) -> str:
    plan = _load("plan").get(str(chapter_number), "")
    return plan

def get_previous_recap(chapter_number: int) -> str:
    recaps = _load("recaps")
    prev = str(chapter_number - 1)
    return recaps.get(prev, "")

def update_memory(chapter_number: int, chapter_text: str):
    mem = _load("memory")
    mem[str(chapter_number)] = chapter_text[-1000:]  # simple tail memory
    _save("memory", mem)

def get_rolling_memory(chapter_number: int) -> str:
    mem = _load("memory")
    keys = sorted([int(k) for k in mem if int(k) < chapter_number])
    return "\n".join([mem[str(k)] for k in keys[-3:]])  # últimos 3 caps
