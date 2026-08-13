# Methodology Skill Generation

Use this when turning the book's methods into one or more reusable skills. This is inspired by cangjie-style distillation, but adapted for a professor-first learning workflow.

## Entry Gate

Do not generate methodology skills directly from raw extraction. Require:

- full-book ingestion pass
- professor teaching path
- whole-book map
- concept dependency model
- argument or method map
- limitations and boundaries
- source anchors

## Pipeline

### Stage 0: Whole-Book Understanding

Build the whole-book model first. Identify what the author is actually teaching, where it appears, and how it fits the book.

### Stage 1: Candidate Extraction

Extract candidate units:

- frameworks
- principles
- procedures
- diagnostic checklists
- decision rules
- anti-pattern detectors
- practice routines
- application templates

Reject pure stories, slogans, facts, and vague inspiration.

### Stage 1.5: Triple Verification

For every candidate:

1. **Cross-source support**: supported by multiple book locations or one load-bearing chapter.
2. **Predictive/application power**: can guide a new real problem outside the exact book example.
3. **Distinctiveness**: not generic advice any competent person would say.

### Stage 2: Skill Construction

Each skill must include:

- `name`
- trigger-heavy `description`
- source basis
- what problem it solves
- execution steps
- decision criteria
- output shape
- boundaries and anti-patterns
- examples
- sibling-skill distinctions

### Stage 3: Linking

Create an index that explains:

- which skills are prerequisites
- which are alternatives
- which combine together
- where each skill came from in the book

### Stage 4: Test Prompts

For each generated skill, write tests:

- should trigger
- should not trigger
- ambiguous case
- sibling-skill confusion case
- misuse or boundary case

### Stage 5: Teach Before Install

Before installing or using generated skills, teach the user what each skill is for. A skill created from a misunderstood method is dangerous.

### Stage 6: Save And Report Status

At the end of the learning session, report the exact status:

- `已保存为候选 skill`: candidate files exist but are not installable.
- `已生成 installable skill`: a skill folder with `SKILL.md` exists.
- `已验证`: the installable skill passed the host's skill validation.

Give the saved path for every generated candidate or installable skill. Do not say "已经生成本书的方法论 skill" unless at least candidate files exist. Do not say "已安装" unless installation actually happened.

## Candidate Template

```text
Skill candidate:
Source:
Core method:
Trigger:
Steps:
Boundary:
Misuse:
Sibling distinction:
Test prompts:
```

## Quality Red Lines

- No source anchor, no skill.
- No trigger condition, no skill.
- No boundary, no skill.
- No tests, no install.
- No user confirmation before creating installable skills.
- No saved files, no saved-skill claim.
