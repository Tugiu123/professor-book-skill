# Full-Book Ingestion Protocol

Use this before claiming the professor has read, mastered, or can teach the whole book.

## Goal

Build a working internal model of the whole book before teaching. The model does not need to be a polished document, but it must be strong enough for the agent to teach from the whole to the parts.

## Required Passes

### Pass 1: Source And Structure

Extract or inspect:

- title, author, edition, source path
- table of contents
- chapter and part boundaries
- preface/introduction/conclusion
- glossary, appendix, notes, diagrams, or exercises

For long books, use page/line/chapter probes and source maps. Do not rely on memory of the title.

If extraction is empty, sparse, garbled, or marked `ocr_recommended` in `source-map.json`, stop Pass 1 and follow `references/ocr-and-scanned-pdf.md`. Do not proceed to whole-book modeling until OCR or another reliable source text is available.

### Pass 2: Whole-Book Model

Capture:

- core question
- one-sentence thesis
- 3-7 structural parts
- role of every chapter
- concept dependencies
- argument spine
- examples that carry the book's logic
- limitations and likely blind spots

### Pass 3: Field Context

Identify the domain knowledge a beginner needs to understand the book. Keep this field context focused and subordinate to the book. Mark outside knowledge clearly.

### Pass 4: Teaching Path

Design the fastest path that preserves depth:

1. what must be taught first
2. what can be deferred
3. which chapters are load-bearing
4. which concepts need slow explanation
5. where the user is likely to misunderstand
6. where application should happen

### Pass 5: Methodology Extraction Readiness

Before generating book-derived skills, identify repeatable methods, decision frameworks, checklists, anti-pattern detectors, and application boundaries. Do not generate skills yet.

## Mastery Claim Rules

- Say "I have extracted a working model" only after Passes 1-2.
- Say "I can teach this from the whole-book view" only after Passes 1-4.
- Say "I can generate methodology skills" only after Pass 5 and source anchors exist.
- If extraction quality is weak, say so and teach from the reliable parts only.
- If OCR was required, say which parser produced the text and keep OCR uncertainty visible for weak sections.

## Minimal Internal Model

When writing a state file, use:

```text
Book:
Core question:
Thesis:
Parts:
Chapter roles:
Concept dependencies:
Load-bearing chapters:
Beginner pitfalls:
Teaching path:
Source anchors:
```
