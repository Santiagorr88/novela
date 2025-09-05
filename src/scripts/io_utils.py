import os
import re
def save_text_to_file(text: str, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def multiply_ints(a, b):
    return int(a) * int(b)

def count_words(text: str) -> int:
    if not text:
        return 0
    words = re.findall(r"\b\w+\b", text)
    return len(words)
