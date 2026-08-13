# Skill Distillation Bridge

Use this only when the user wants the book turned into one or more skills. Read `methodology-skill-generation.md` first for the cangjie-style pipeline.

## Entry Gate

Do not distill skills until these exist:

- full-book ingestion model
- whole-book map
- key concept cards
- argument or method map
- limitations and boundaries
- source map
- at least one professor teaching pass or user confirmation that the method is understood

## Candidate Types

Good skill candidates are:

- repeatable methods
- decision frameworks
- diagnostic checklists
- thinking moves
- procedures with clear triggers
- anti-pattern detectors

Poor skill candidates are:

- inspirational quotes
- one-off stories
- pure facts
- vague principles
- broad "be like the author" personas

## Candidate Record

Each candidate must include:

- skill name
- trigger condition
- source anchor
- method summary
- steps
- boundary
- expected output
- related sibling skills
- test prompts: should trigger, should not trigger, ambiguous

## Validation

Use three checks before creating a skill:

1. **Cross-source support**: at least two source locations or one source plus strong structural role.
2. **Predictive power**: can the method guide a new case not directly described in the book?
3. **Distinctiveness**: not generic advice any competent person would give.

## Output

Write candidates under `skill-candidates/` first. Create installable skills only after user confirmation.

Static candidates are not enough. The agent must explain the candidate skills conversationally so the user understands what each skill will do and where it came from in the book.
