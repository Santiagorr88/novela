#!/usr/bin/env python3
"""Build an editorial-quality PDF for any book (1-3) from its numbered chapter .md files.

Usage: python3 build_pdf.py <book_num> <LANG>
  e.g. python3 build_pdf.py 1 EN
       python3 build_pdf.py 2 ES
"""
import json
import os
import re
import subprocess
import sys

BOOK_NUM = sys.argv[1] if len(sys.argv) > 1 else "1"
LANG = sys.argv[2] if len(sys.argv) > 2 else "EN"

BASE = os.path.dirname(os.path.abspath(__file__))
BOOK_DIR = os.path.join(BASE, f"Libro{BOOK_NUM}")
SRC_DIR = os.path.join(BOOK_DIR, LANG)
OUT_HTML = os.path.join(BOOK_DIR, f"Libro{BOOK_NUM}_{LANG}.html")
OUT_PDF = os.path.join(BOOK_DIR, f"Libro{BOOK_NUM}_{LANG}.pdf")

SERIES_TITLE = "CHRONICLES OF JUDGMENT" if LANG == "EN" else "LAS CRÓNICAS DEL JUICIO"
TOC_LABEL = "Contents" if LANG == "EN" else "Índice"

BOOK_LABELS_EN = {"1": "Book One", "2": "Book Two", "3": "Book Three"}
BOOK_LABELS_ES = {"1": "Libro Uno", "2": "Libro Dos", "3": "Libro Tres"}
BOOK_TITLES_EN = {
    "1": "THE ECHO OF THE SWORD",
    "2": "THE FORGOTTEN VOICES",
    "3": "THE THROBBING VOID",
}
BOOK_TITLES_ES = {
    "1": "EL ECO DE LA ESPADA",
    "2": "LAS VOCES OLVIDADAS",
    "3": "EL VACÍO PALPITANTE",
}

BOOK_LABEL = (BOOK_LABELS_EN if LANG == "EN" else BOOK_LABELS_ES)[BOOK_NUM]
BOOK_TITLE = (BOOK_TITLES_EN if LANG == "EN" else BOOK_TITLES_ES)[BOOK_NUM]


def md_inline(text):
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return text


def md_to_html_body(md_text):
    lines = md_text.split("\n")
    # drop the H1 title line, we render our own chapter header
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    html = []
    para = []

    def flush():
        if para:
            joined = " ".join(p.strip() for p in para if p.strip())
            if joined:
                html.append(f"<p>{md_inline(joined)}</p>")
            para.clear()

    for line in lines:
        stripped = line.strip()
        if stripped == "---":
            flush()
            html.append('<p class="scenebreak">&#10022;</p>')
        elif stripped == "":
            flush()
        else:
            para.append(line)
    flush()
    return "\n".join(html)


def main():
    manifest_path = os.path.join(SRC_DIR, "_manifest.json")
    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)

    toc_items = []
    chapters_html = []
    for entry in manifest:
        n = entry["n"]
        fname = entry["file"]
        title = entry["title"]
        with open(os.path.join(SRC_DIR, fname), encoding="utf-8") as f:
            md_text = f.read()
        body_html = md_to_html_body(md_text)
        chap_label = f"Chapter {n}" if LANG == "EN" else f"Capítulo {n}"
        chapters_html.append(f"""
<section class="chapter">
  <div class="chapter-head">
    <div class="chapter-num">{chap_label}</div>
    <h1 class="chapter-title">{title}</h1>
  </div>
  <div class="chapter-body">
  {body_html}
  </div>
</section>
""")
        toc_items.append(f'<li><span class="toc-num">{n}.</span> <span class="toc-title">{title}</span></li>')

    css = """
@font-face { font-family: 'Libertine'; src: local('Linux Libertine O'); }
@font-face { font-family: 'Biolinum'; src: local('Linux Biolinum O'); }
html, body { margin:0; padding:0; }
body { font-family: 'Libertine', 'Georgia', serif; font-size: 11.3pt; line-height: 1.5; color: #1a1a1a; }
.cover { height: 7.2in; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; page-break-after: always; }
.cover .kicker { font-family:'Biolinum', sans-serif; letter-spacing: 0.35em; font-size:10pt; color:#555; margin-bottom: 2.2em; text-transform: uppercase;}
.cover h1 { font-family:'Biolinum', sans-serif; font-weight: 400; font-size: 27pt; letter-spacing: 0.06em; margin: 0 0.4in; line-height:1.25; }
.cover .rule { width: 2.2in; border-top: 1.4pt solid #333; margin: 0.5in auto; }
.cover .subtitle { font-family:'Biolinum', sans-serif; font-size: 14pt; letter-spacing: 0.25em; text-transform: uppercase; color:#333; }
.toc { page-break-after: always; padding-top: 0.4in; }
.toc h2 { font-family:'Biolinum', sans-serif; font-weight:400; letter-spacing:0.15em; text-transform:uppercase; font-size:14pt; text-align:center; margin-bottom: 0.5in; }
.toc ul { list-style:none; padding:0; margin:0; column-count:1; }
.toc li { font-size: 10.3pt; margin-bottom: 0.11in; display:flex; }
.toc-num { width: 0.4in; color:#666; }
.toc-title { flex:1; }
.chapter { page-break-before: always; }
.chapter-head { text-align:center; margin: 0.55in 0 0.5in 0; }
.chapter-num { font-family:'Biolinum', sans-serif; letter-spacing:0.3em; text-transform:uppercase; font-size: 9.5pt; color:#777; margin-bottom: 0.12in; }
.chapter-title { font-family:'Biolinum', sans-serif; font-weight:400; font-size: 18pt; letter-spacing:0.02em; margin:0; }
.chapter-body p { text-align: justify; text-indent: 1.4em; margin: 0; hyphens: auto; -webkit-hyphens: auto; orphans: 2; widows: 2; }
.chapter-body p:first-of-type { text-indent: 0; }
.chapter-body p:first-of-type::first-letter { font-family:'Biolinum', sans-serif; font-size: 3.1em; float:left; line-height: 0.8; padding-right: 0.08em; padding-top: 0.05em; color:#111; }
.chapter-body p.scenebreak { text-align:center; text-indent:0; margin: 1em 0; color:#888; font-size: 11pt; letter-spacing: 0.4em; }
.chapter-body p.scenebreak + p { text-indent: 0; }
"""

    html_doc = f"""<!doctype html>
<html lang="{'en' if LANG=='EN' else 'es'}">
<head>
<meta charset="utf-8">
<style>{css}</style>
</head>
<body>
<div class="cover">
  <div class="kicker">{SERIES_TITLE}</div>
  <h1>{BOOK_TITLE}</h1>
  <div class="rule"></div>
  <div class="subtitle">{BOOK_LABEL}</div>
</div>
<div class="toc">
  <h2>{TOC_LABEL}</h2>
  <ul>
  {''.join(toc_items)}
  </ul>
</div>
{''.join(chapters_html)}
</body>
</html>
"""

    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_doc)

    print(f"HTML escrito en {OUT_HTML}")

    wkhtmltopdf_bin = os.path.expanduser("~/.local/wkhtmltopdf/bin/wkhtmltopdf")
    if not os.path.exists(wkhtmltopdf_bin):
        wkhtmltopdf_bin = "wkhtmltopdf"

    cmd = [
        wkhtmltopdf_bin,
        "--enable-local-file-access",
        "--page-width", "6in",
        "--page-height", "9in",
        "--margin-top", "0.85in",
        "--margin-bottom", "0.9in",
        "--margin-left", "0.8in",
        "--margin-right", "0.8in",
        "--footer-center", "[page]",
        "--footer-font-size", "9",
        "--footer-font-name", "Linux Libertine O",
        "--footer-spacing", "8",
        OUT_HTML, OUT_PDF,
    ]
    subprocess.run(cmd, check=True)
    print(f"PDF generado en {OUT_PDF} (usando {wkhtmltopdf_bin})")


if __name__ == "__main__":
    main()
