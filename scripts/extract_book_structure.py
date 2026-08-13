#!/usr/bin/env python3
"""Extract rough text and structure for professor-book-skill.

Stdlib-first extractor for txt/md/html/docx/epub plus optional pdftotext for PDF.
It writes full_text.txt and source-map.json to an output directory.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


HEADING_RE = re.compile(
    r"^\s*(#{1,6}\s+.+|第[一二三四五六七八九十百千万0-9]+[章节部篇].*|"
    r"(chapter|part|section)\s+[0-9ivxlcdm]+[:.\s-].+|\d+(\.\d+)*\s+.+)\s*$",
    re.IGNORECASE,
)


def strip_tags(text: str) -> str:
    text = re.sub(r"(?is)<(script|style).*?</\1>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\n{3,}", "\n\n", text)


def read_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml")
    root = ET.fromstring(xml)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    chunks = []
    for para in root.findall(".//w:p", ns):
        text = "".join(node.text or "" for node in para.findall(".//w:t", ns))
        if text.strip():
            chunks.append(text.strip())
    return "\n\n".join(chunks)


def read_epub(path: Path) -> str:
    chunks = []
    with zipfile.ZipFile(path) as zf:
        names = sorted(n for n in zf.namelist() if n.lower().endswith((".xhtml", ".html", ".htm")))
        for name in names:
            raw = zf.read(name).decode("utf-8", errors="ignore")
            text = strip_tags(raw)
            if text.strip():
                chunks.append(f"\n\n=== {name} ===\n\n{text.strip()}")
    return "\n".join(chunks)


def read_pdf(path: Path) -> str:
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        raise RuntimeError("PDF extraction needs pdftotext in this lightweight extractor.")
    result = subprocess.run(
        [pdftotext, "-layout", str(path), "-"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "pdftotext failed")
    return result.stdout


def assess_extraction_quality(path: Path, text: str, headings: list[dict[str, object]]) -> dict[str, object]:
    clean = re.sub(r"\s+", "", text)
    replacement_chars = text.count("\ufffd")
    approx_words = len(re.findall(r"\w+", text))
    is_pdf = path.suffix.lower() == ".pdf"
    reasons = []

    if is_pdf and len(clean) < 2000:
        reasons.append("very_low_text_for_pdf")
    if is_pdf and approx_words < 500:
        reasons.append("low_word_count_for_pdf")
    if is_pdf and len(headings) < 3:
        reasons.append("few_headings_found")
    if replacement_chars > 20:
        reasons.append("garbled_replacement_characters")

    return {
        "status": "ocr_recommended" if reasons else "ok",
        "ocr_recommended": bool(reasons),
        "reasons": reasons,
        "characters_no_space": len(clean),
        "replacement_characters": replacement_chars,
    }


def read_source(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {".txt", ".md", ".markdown", ".rst"}:
        return path.read_text(encoding="utf-8", errors="ignore")
    if ext in {".html", ".htm"}:
        return strip_tags(path.read_text(encoding="utf-8", errors="ignore"))
    if ext == ".docx":
        return read_docx(path)
    if ext == ".epub":
        return read_epub(path)
    if ext == ".pdf":
        return read_pdf(path)
    raise RuntimeError(f"Unsupported file type: {ext}")


def collect_headings(text: str) -> list[dict[str, object]]:
    headings = []
    for i, line in enumerate(text.splitlines(), start=1):
        clean = line.strip()
        if clean and len(clean) <= 120 and HEADING_RE.match(clean):
            headings.append({"line": i, "text": clean})
    return headings[:300]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("sources", nargs="+", help="book files")
    parser.add_argument("--out", default="book-professor-work", help="output directory")
    args = parser.parse_args()

    outdir = Path(args.out).expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    all_text = []
    source_map = {"sources": [], "headings": []}
    for item in args.sources:
        path = Path(item).expanduser().resolve()
        if not path.exists():
            print(f"missing: {path}", file=sys.stderr)
            continue
        try:
            text = read_source(path)
        except Exception as exc:  # noqa: BLE001
            source_map["sources"].append({"path": str(path), "error": str(exc)})
            continue
        start_line = sum(part.count("\n") + 1 for part in all_text) + 1
        marked = f"\n\n=== SOURCE: {path.name} ===\n\n{text.strip()}\n"
        all_text.append(marked)
        headings = collect_headings(text)
        quality = assess_extraction_quality(path, text, headings)
        source_map["sources"].append({
            "path": str(path),
            "characters": len(text),
            "approx_words": len(re.findall(r"\w+", text)),
            "start_line": start_line,
            "headings_found": len(headings),
            "extraction_quality": quality,
        })
        for h in headings:
            source_map["headings"].append({"source": path.name, **h})

    full_text = "\n".join(all_text).strip() + "\n"
    (outdir / "full_text.txt").write_text(full_text, encoding="utf-8")
    (outdir / "source-map.json").write_text(
        json.dumps(source_map, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps({"outdir": str(outdir), "sources": len(source_map["sources"])}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
