# OCR And Scanned PDF Gate

Use this when a provided PDF, image, or long document cannot be reliably extracted with the lightweight extractor.

## Trigger Conditions

Treat the source as OCR-needed when any of these are true:

- extracted text is empty or extremely short compared with page count
- most pages contain image scans rather than selectable text
- text is garbled, duplicated, badly ordered, or missing headings
- table of contents and chapter headings cannot be found in a book that visibly has them
- formulas, tables, sidebars, or multi-column layout are central to understanding

Do not claim the professor has read the book until OCR output is good enough for whole-source modeling.

## First Response

Say plainly:

```text
这份 PDF 可能是扫描件或图片型 PDF，普通文本提取读不到足够内容。我现在还不能说已经通读了整本书。
```

Then choose the least disruptive path:

1. If a reliable OCR/parser is already installed, use it and continue.
2. If not installed, ask the user before installing anything or sending files to an online service.
3. If the user declines OCR, ask for a text/Markdown/EPUB version or teach only from readable excerpts.

## Preferred OCR Parser

MinerU is the preferred optional parser for scanned PDFs, complex layouts, formulas, tables, and PDF-to-Markdown/JSON workflows when available.

Use MinerU because the official project describes support for:

- scanned documents and OCR
- PDF, image, DOCX, PPTX, and XLSX inputs
- Markdown and JSON outputs
- reading-order reconstruction
- formula and table conversion
- local CLI/API/WebUI usage

But treat MinerU as optional, not built-in:

- It is a separate dependency and may require model downloads, disk space, RAM, and platform-specific setup.
- Official docs warn that complex layouts, scanned pages, and handwriting may still produce imperfect results.
- OCR must be quality-checked before teaching.

## MinerU CLI Route

Use this route only when the current agent can run local CLI commands and the user has allowed local parsing. Keep paths generic; never bake a user's local folder into the skill.

Preferred command shape:

```bash
mineru -p "$INPUT_FILE" -o "$OUTPUT_DIR" -b pipeline -m auto
```

Prefer `-m auto` for unknown PDFs and Chinese books. Do not default to `-m txt` just because selectable text exists; some Chinese PDFs expose a broken text layer that produces severe mojibake while OCR/layout parsing is readable.

Use a staged conversion:

1. Run ordinary/lightweight extraction first.
2. If extraction is empty, sparse, garbled, or structurally poor, try MinerU on a small page range first, such as the cover, table of contents, and 3-20 representative pages.
3. Inspect the sample Markdown before running the whole source.
4. Run the full source only after the sample passes the quality gate.
5. Preserve MinerU's Markdown, content JSON, layout PDF, span PDF, images folder, logs, and command notes in the user's output directory when durable output is requested.

If the installed CLI supports page ranges, use them for sampling. Common examples are `-s <start_page>` and `-e <end_page>`, but confirm with `mineru --help` because CLI options may change.

## MinerU Setup Problems To Anticipate

Do not treat MinerU as a zero-cost built-in feature. If setup fails, explain the blocking condition and ask before making heavier changes.

Common issues:

- Python version mismatch.
- Base install succeeds but `pipeline` parsing fails because ML dependencies such as `torch` are missing.
- The local package may miss a transitive dependency such as `six`.
- First run may download models and take noticeably longer.
- Network access may block Hugging Face or other model sources.
- The virtual environment and models may use significant disk space.
- Very large or complex PDFs may need page-range batching.
- OCR output can look polished while still containing reading-order, table, formula, or recognition errors.

If a local source checkout exists, prefer an isolated virtual environment and avoid polluting the user's global Python. If official installation documentation is available, follow it rather than relying on stale commands.

## Install Policy

Never silently install MinerU.

If MinerU is missing, ask:

```text
我建议用 MinerU 先把扫描版 PDF 转成 Markdown/JSON。它比较适合扫描件、表格、公式和复杂排版，但需要额外安装和模型下载。是否允许我在本机安装/调用 MinerU？如果不想安装，也可以改用在线解析或提供可复制文本版本。
```

If the user approves, follow the current official MinerU installation documentation for the host system. Do not hard-code stale commands if current docs are unavailable; look up or ask the user to provide the install method.

## Quality Gate After OCR

After OCR conversion, inspect the output before teaching:

- check that total text length is plausible for the page count
- verify table of contents or major headings
- sample beginning, middle, and end pages
- compare `txt` and `auto`/OCR samples when selectable text looks suspicious
- check for mojibake markers, replacement characters, excessive Latin-letter corruption, missing Chinese headings, repeated lines, and obviously broken ordering
- check 3-5 random source anchors against the PDF images when possible
- mark unreliable sections as OCR-uncertain

Only then continue with whole-book ingestion.

Sample acceptance rule:

- Accept MinerU output when the title, table of contents or headings, and several continuous paragraphs are readable and structurally ordered.
- Reject or retry when headings are garbled, Chinese text is corrupted, pages are missing, or the Markdown has too little continuous prose for the page count.
- If a sample passes but some sections are layout-heavy, proceed while marking those sections for later source-image spot checks.

## Fallbacks

If MinerU fails or output quality is poor:

- try another installed OCR/parser if available
- ask the user for a better source format
- split the PDF into smaller ranges and OCR again
- teach from reliable sections only, with explicit uncertainty boundaries

Do not let OCR confidence leak into teaching confidence. A polished Markdown file can still contain recognition or reading-order errors.
