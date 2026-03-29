#!/usr/bin/env python3
"""
pdf_to_text.py — Extract text from a PDF file using PyMuPDF (fitz).

Usage:
    python scripts/pdf_to_text.py <path/to/file.pdf> [--pages 1-10]

Requirements:
    pip install pymupdf

Output:
    Prints extracted text to stdout, page by page.
    Redirect to a file to capture:
        python scripts/pdf_to_text.py doc/parallel/TPLDataflow.pdf > /tmp/tpl.txt
"""

import sys
import argparse

# Ensure stdout can handle the full Unicode range on Windows (cp1252 terminals)
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def parse_page_range(spec: str, total: int) -> range:
    """Parse a '1-10' or '3' style page spec into a range (0-indexed)."""
    if "-" in spec:
        start, end = spec.split("-", 1)
        return range(int(start) - 1, min(int(end), total))
    else:
        p = int(spec) - 1
        return range(p, p + 1)


def extract(pdf_path: str, pages_spec: str | None = None) -> None:
    try:
        import fitz  # PyMuPDF
    except ImportError:
        sys.exit("PyMuPDF is not installed. Run: pip install pymupdf")

    doc = fitz.open(pdf_path)
    total = len(doc)
    page_range = parse_page_range(pages_spec, total) if pages_spec else range(total)

    print(f"# PDF: {pdf_path}  ({total} pages total)\n")
    for i in page_range:
        page = doc[i]
        text = page.get_text()
        print(f"\n{'='*60}")
        print(f"## Page {i + 1}")
        print("=" * 60)
        print(text)

    doc.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract text from a PDF via PyMuPDF.")
    parser.add_argument("pdf", help="Path to the PDF file")
    parser.add_argument(
        "--pages",
        metavar="RANGE",
        help="Page range to extract, e.g. '1-10' or '5' (1-indexed). Default: all pages.",
    )
    args = parser.parse_args()
    extract(args.pdf, args.pages)


if __name__ == "__main__":
    main()