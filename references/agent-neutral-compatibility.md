# Agent-Neutral Compatibility

Use this when installing, copying, packaging, or adapting `professor-book-skill` for any skills-aware agent.

## Compatibility Contract

The skill is portable if the host agent can:

1. discover or be told to read `SKILL.md`
2. read relative files under `references/`
3. optionally run Python scripts under `scripts/`
4. write Markdown outputs when the user requests durable files

If the host cannot run scripts, the skill still works manually: ask the user for extracted text or chapter excerpts, then follow the reference protocols.

## Folder Layout

Keep this folder intact:

```text
professor-book-skill/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

Do not require host-specific UI metadata. A host may add its own metadata outside this portable package, but the portable skill itself should work from `SKILL.md` plus relative resources.

## Common Install Locations

Use whichever location your agent host discovers. Common patterns include:

```text
<agent-home>/skills/professor-book-skill/
<user-home>/.agents/skills/professor-book-skill/
<project-root>/skills/professor-book-skill/
<project-root>/.agents/skills/professor-book-skill/
```

When unsure, put the folder in a project-local `skills` directory and explicitly tell the agent: "Use the skill at `<path>/professor-book-skill`."

## Tool-Agnostic Use

Do not rely on host-specific tool names such as named file readers, terminal tools, patch tools, or platform-only functions. Translate actions to the available host tools:

- "read a file" means use the host's file-read capability
- "run a script" means use the host's shell or terminal capability
- "write a pack" means create Markdown files in the requested output directory
- "validate" means run the validator script if possible, otherwise check required files manually

## Script Requirements

The bundled scripts use Python 3 and the standard library. PDF extraction optionally needs `pdftotext`; if unavailable, ask the user for text, EPUB, DOCX, Markdown, or another extractable format.

## Packaging Rule

For cross-agent sharing, package the directory itself. Do not package only `SKILL.md`; the reference files are part of the skill's reasoning system.

## Adaptation Rule

When adapting to another host:

- keep YAML frontmatter in `SKILL.md`
- preserve relative resource paths
- avoid adding host-specific mandatory steps to the main workflow
- put host-specific notes in this compatibility file
