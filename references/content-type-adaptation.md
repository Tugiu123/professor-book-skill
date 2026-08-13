# Content-Type Adaptation

Use this before choosing the teaching style for any book, report, paper, manual, transcript, or long-form source.

## Primary Rule

Do not force every source into a book-course format. First classify the source, then choose the progress unit, voice, density, and output shape.

## Classification Pass

Infer the dominant source type from title, table of contents, headings, abstract, introduction, conclusion, diagrams, and repeated section patterns.

If the source is mixed, choose a dominant type and a secondary type.

Use this compact statement internally or in the session state:

```text
Source type:
Dominant goal:
Best progress unit:
Teaching style:
Dynamic lesson count:
Density rule:
Skill extraction target:
```

## Source Types And Teaching Strategy

| Type | How to recognize | Progress unit | Teaching style | Lesson count basis | Skill extraction target |
|---|---|---|---|---|---|
| Theory or framework book | concepts, chapters, arguments, named models | concept or chapter | conceptual professor | load-bearing concepts plus major parts | frameworks, diagnostic lenses, decision rules |
| Practical how-to book | steps, exercises, cases, checklists | procedure or chapter | practical mentor | workflows, decisions, practice loops | procedures, checklists, practice routines |
| Textbook | definitions, examples, exercises, prerequisites | module or concept | patient instructor | prerequisite chain plus modules | concept maps, problem-solving routines |
| Research paper | abstract, method, results, discussion | claim, method, finding | research discussant | research question, method, findings, limits | evaluation criteria, experimental protocol |
| Industry report | executive summary, trends, data, recommendations | finding or section | synthesis analyst | key findings and decision implications | decision brief, evidence map, risk checklist |
| Technical manual/spec | requirements, API, commands, constraints | task, interface, rule | technical instructor | tasks, interfaces, constraints, validation paths | operational steps, validation checklist |
| Memoir/biography | chronology, episodes, life decisions | episode or theme | narrative guide | turning points and recurring themes | principles, decision patterns, cautionary cases |
| Philosophy/humanities | concepts, distinctions, objections | argument or concept | slow concept professor | distinctions, arguments, objections | argument maps, distinctions, interpretive frames |
| Course transcript | lectures, Q&A, examples | lesson or concept | seminar professor | lecture modules and prerequisite concepts | lesson map, exercises, practice prompts |
| Policy/legal/standard | clauses, definitions, obligations | clause or obligation | careful interpreter | obligations, definitions, exceptions, procedures | compliance checklist, boundary conditions |

## Dynamic Lesson Plan

Build a lesson plan after the whole-source model, not before.

The total count must come from the source:

- short executive report: often 5-10 episodes
- ordinary nonfiction book: often 10-25 episodes
- dense theory book or textbook: often 25-60 episodes
- research paper: often 5-12 episodes
- technical manual/spec: one episode per task/interface/constraint cluster
- memoir/biography: one episode per turning point or theme
- mixed source: one episode per load-bearing idea, not per page

These are ranges, not defaults. If the source asks for 8, use 8. If it asks for 40, use 40.

For each planned episode, assign:

```text
Episode:
Role in whole source:
Weight: light | normal | load-bearing | dense
Density: brief | standard | deep | technical
Must include:
Can defer:
Progress marker:
```

## Dynamic Density Control

Do not use a fixed per-episode recipe. Decide density from the episode's role:

- **Light**: orientation, recap, bridge, or low-risk background. Keep short; use no example unless needed.
- **Normal**: one meaningful idea or finding. Use one clear explanation and only the support needed.
- **Load-bearing**: later episodes depend on it. Add contrast, example, precision, source anchor, and application.
- **Dense/technical**: method, proof, legal clause, API behavior, or mathematically precise idea. Slow down and include definitions, constraints, failure modes, and validation.

Expand only when:

- the idea supports many later ideas
- the user asks for depth
- misunderstanding would cause misuse
- evidence or method is subtle
- the source itself is technical, legal, philosophical, or mathematical

Compress when:

- the point is background
- the previous episode was long
- the user is in overview mode
- the source is a report or manual where decision/action matters more than exposition
- one example already teaches the point

If an episode starts feeling long, stop adding examples and move the rest to the next episode or sidecar note.

## Style Selection

Choose the style from the source:

- **Conceptual professor**: for theory, frameworks, philosophy, complex nonfiction. Use high-level framing and concept dependencies.
- **Practical mentor**: for how-to and methods books. Teach by task, decision point, and practice.
- **Research discussant**: for papers. Teach research question, method, evidence, result, limitation, implication.
- **Synthesis analyst**: for reports. Teach headline, evidence, confidence, implication, decision use.
- **Technical instructor**: for manuals/specs. Teach task flow, constraints, commands/interfaces, validation, failure modes.
- **Narrative guide**: for memoirs and biographies. Teach arc, decisions, turning points, principles, and limits.

Do not mix all styles at once. Use one dominant style per episode.

## Mode A Overview Adaptation

When the user chooses `A`, adapt the overview:

- Book: thesis, parts, core concepts, learning route.
- Report: executive thesis, key findings, evidence base, decision implications, risk caveats.
- Paper: research question, method, main result, contribution, limitations.
- Manual/spec: purpose, task map, main interfaces/rules, prerequisites, failure modes.
- Memoir/biography: life arc, turning points, themes, lessons, limits.
- Philosophy/humanities: central question, conceptual distinctions, argument map, objections.

## Mode B Episode Adaptation

When the user chooses `B`, the first episode must match the source:

- Book: why this source exists and what problem it solves.
- Report: what decision or uncertainty the report helps resolve.
- Paper: what research question the paper asks and why it matters.
- Manual/spec: what task the user can perform after learning it.
- Memoir/biography: what life or decision pattern the source reveals.
- Philosophy/humanities: what question or distinction opens the text.

## Anti-Patterns

- Do not teach a report like a chapter-by-chapter book if findings are the real structure.
- Do not teach a paper like a self-help book; preserve method and evidence.
- Do not teach a manual with literary exposition; prioritize actions and validation.
- Do not teach a philosophical text as a list of takeaways; preserve distinctions and objections.
- Do not force a 15-part plan, six-part template, or any fixed denominator. Let the source determine the total.
- Do not make every episode long to prove depth.
- Do not compress load-bearing concepts just because the default mode is brief.
