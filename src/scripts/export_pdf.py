# src/scripts/export_pdf.py
import markdown
from weasyprint import HTML, CSS
from markdown import markdown
import pathlib


def md_to_pdf(markdown_text: str, filename: str, css_path: str = None):
    ...

    html = markdown(markdown_text, output_format="html5")
    out = pathlib.Path(filename)
    out.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html).write_pdf(out)
    return str(out)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--title", required=False)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    markdown_text = pathlib.Path(args.file).read_text(encoding="utf-8")
    css_path = "src/css/chapter.css"  # puedes dejarlo hardcodeado si usas uno fijo

    md_to_pdf(markdown_text, filename=args.output, css_path=css_path)
    print(f"✅ PDF generado: {args.output}")