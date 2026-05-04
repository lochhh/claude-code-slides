# Workflow 03: Synthesise Master Guide

## Objective

Transform analytical output into polished, navigable, pedagogically structured documentation for software engineers mastering Claude Code. Output: primitives reference + index + one file per theme in `deliverables/prod/`. GitHub Pages ready (plain GFM, relative links, no build tools).

## Prerequisites

- Phase 2 complete: `deliverables/analysis.md` exists and has been reviewed
- `uv sync` already run

## Steps

1. **Pre-flight:** Read `deliverables/analysis.md`. For each theme, extract the section verbatim and note the raw file paths cited per tip (source citations appear inline).

2. **Batch 1 — support files (3 agents in parallel):** Spawn 3 `theme-writer` subagents simultaneously. These must complete before any theme file is written, since theme files cross-link to them.
   - Agent 1 → `deliverables/prod/primitives.md`
   - Agent 2 → `deliverables/prod/glossary.md`
   - Agent 3 → `deliverables/prod/references.md`

   Pass to each agent: `FILE_TYPE: support`, `FILE: <primitives|glossary|references>`, `ANALYSIS_MD_PATH`, `RAW_DIR`.

3. **Batch 2 — themes 1–4 (4 agents in parallel):** Pass each agent their `ANALYSIS_SECTION` inline, `RAW_FILES` list, and `RELATED_THEMES`. Theme files must cross-link primitive names to `primitives.md`, technical terms to `glossary.md`, and cite sources as footnotes linking to `references.md`.
   - Agent 1 → `deliverables/prod/claudemd-setup.md` (CLAUDE.md & Project Memory, Novice)
   - Agent 2 → `deliverables/prod/context-management.md` (Context Management, Intermediate)
   - Agent 3 → `deliverables/prod/hooks-automation.md` (Hooks & Automation, Advanced)
   - Agent 4 → `deliverables/prod/mcp-servers.md` (MCP Servers, Intermediate)

4. **Batch 3 — themes 5–8 (4 agents in parallel):**
   - Agent 1 → `deliverables/prod/prompting-strategies.md` (Prompting Strategies, Novice)
   - Agent 2 → `deliverables/prod/productivity-ide-cost.md` (Productivity/IDE/Cost, Basic)
   - Agent 3 → `deliverables/prod/parallel-development.md` (Parallel Development, Expert)
   - Agent 4 → `deliverables/prod/commands-skills-plan-mode.md` (Commands/Skills/Plan Mode, Intermediate)

5. **Final — index (1 agent):** Spawn 1 `theme-writer` subagent. Pass `FILE_TYPE: index` and all 11 completed file paths so the agent can read and extract summaries.
   - Agent → `deliverables/prod/index.md`

6. **Rate-limit fallback:** If any batch hits rate limits, split into [3]+[1] or [2]+[2] sub-batches.

   > **Model config:** Theme-writer subagents run on `claude-sonnet-4-6`. The orchestrating agent runs on Opus.

7. **Review output files:**
   - `deliverables/prod/primitives.md` — core Claude Code primitives with definitions, purpose, examples
   - `deliverables/prod/index.md` — landing page with learning path, usage levels, and theme overview
   - `deliverables/prod/<theme-slug>.md` per theme
   - `deliverables/prod/glossary.md` — key terms
   - `deliverables/prod/references.md` — all sources listed, linkable per theme

9. **Spot-check primitives page** for:
   - All 14 primitives covered in usage-level order — basic: CLAUDE.md, tool use, project structure, permissions & settings, context model; novice: context compaction, memory, slash commands & skills, plan mode; intermediate: agents, hooks, MCP servers; advanced: plugins, git worktrees
   - Each primitive has: definition, purpose explanation, concrete example (Python-specific where possible; otherwise general with Python adaptation note)
   - Each primitive heading has an HTML anchor (`<a id="...">`) matching the slug used in theme file cross-links
10. **Spot-check glossary** for:
    - Key terms from all 8 themes present (check a sample: one term per theme)
    - Each row has an HTML anchor (`<a id="...">`) matching the slug used in theme file cross-links
    - Definitions are one sentence, plain English
11. **Spot-check references** for:
    - Sources cited in theme footnotes have a matching row and anchor in this file
    - Each row has `<a id="...">` anchor in the title cell
    - Type column filled for every row (Article / Video / Repo / Community / Docs)
    - Theme links in the Themes column resolve to correct slugs
12. **Spot-check each theme file** for:
    - Summary paragraph present
    - Tips numbered, ranked, rewritten for clarity/consistency
    - At least one concrete example per tip (real command, prompt snippet, or CLAUDE.md excerpt)
    - Pitfalls, misconceptions, and "when to use this" guidance
    - Primitive names cross-linked to `primitives.md`, technical terms cross-linked to `glossary.md`
    - Source footnotes at end of file linking to `references.md`
    - Cross-links to related themes with one-line rationale
    - Relative links only (no absolute paths to prod/)
13. **Verify index** includes: beginner → expert learning path, usage levels, recommended reading order, cross-theme insights, link to primitives page
14. **Verify GitHub Pages compatibility:** relative links between files, no JS required, no build output

## Output Format

### `deliverables/prod/primitives.md`

```markdown
# Claude Code Primitives

[← Back to index](index.md)

> Start here. These are the building blocks everything else builds on.

## <Primitive Name> (e.g. CLAUDE.md)

**What it is:** <one-sentence definition>

**Why it matters:** <one-sentence purpose>

**Example:**
```<language>
<concrete example>
```

<!-- Basic -->
## CLAUDE.md
## Tool Use
## Project Structure
## Permissions & Settings
## Context Model
<!-- Novice -->
## Context Compaction
## Memory
## Slash Commands & Skills
## Plan Mode
<!-- Intermediate -->
## Agents
## Hooks
## MCP Servers
<!-- Advanced -->
## Plugins
## Git Worktrees
```

### `deliverables/prod/index.md`

```markdown
# Becoming a Pro with Claude Code Pro

> A master guide for software engineers who've hit the ceiling with basic Claude Code usage.

## Learning Path

beginner → novice → intermediate → advanced → expert

<Brief description of what changes at each level.>

## Recommended Reading Order

<Ordered list of themes with rationale.>

## Themes

| # | Theme | Level | Summary |
|---|-------|-------|---------|
| 1 | [CLAUDE.md & Setup](claudemd-setup.md) | Basic | ... |
| 2 | [Context Management](context-management.md) | Intermediate | ... |
...

## Cross-Theme Insights

<2-3 paragraphs on how themes interact and reinforce each other.>

---
*Generated from N sources. See [analysis](../analysis.md) for source details.*
```

### `deliverables/prod/<theme-slug>.md`

```markdown
# <Theme Name>

[← Back to index](index.md)

<One-paragraph conceptual summary — what this theme is, why it matters for engineers at the ceiling.>

**Level:** <Basic / Novice / Intermediate / Advanced / Expert>

## Tips

### 1. <Tip Title>

<Brief explanation — why this works, when to use it.>

**Example:**
```<language>
<real command, config snippet, or prompt>
```

> **When to use:** <context/trigger>
>
> **Pitfalls:** <common mistake or misconception>

### 2. ...

## Related Themes

- [<Theme>](<slug>.md) — <one-line reason for cross-link>

## Sources

See [References](references.md#source-slug-1), [References](references.md#source-slug-2)
```

### `deliverables/prod/references.md`

```markdown
# References

[← Back to index](index.md)

All sources used across the master guide.

| # | Title | Type | URL | Themes |
|---|-------|------|-----|--------|
| 1 | <title> | Article / Video / Repo / Community | <url> | [CLAUDE.md & Setup](claudemd-setup.md), ... |
...
```

### `deliverables/prod/glossary.md`

```markdown
# Glossary

[← Back to index](index.md)

| Term | Definition |
|------|------------|
| CLAUDE.md | ... |
| MCP | ... |
...
```

## Style Guide

All files must follow consistent structure, tone, and style:
- Tone: clear, direct, practical — written for engineers not beginners
- Tips: active voice, imperative mood ("Use X to Y", not "You can use X")
- Examples: real, runnable — no pseudocode placeholders
- Headings: sentence case
- Cross-links: always include a one-line rationale

## Completion Criteria

- [ ] `deliverables/prod/primitives.md` exists covering all 14 primitives in usage-level order (basic → advanced) — each with definition, purpose, and example (Python-specific where possible; general otherwise)
- [ ] `deliverables/prod/index.md` exists with learning path, usage levels, reading order, cross-theme insights, link to primitives page, and links to all theme files
- [ ] One `.md` file per theme in `deliverables/prod/`
- [ ] Each theme file has: summary paragraph, numbered ranked tips, ≥1 concrete example per tip, pitfalls/misconceptions, "when to use this", cross-links to related themes with one-line rationale
- [ ] Each theme file cross-links primitive names to `primitives.md` and technical terms to `glossary.md` on first use per tip
- [ ] Each theme file cites sources as inline footnotes linking to `references.md#<anchor>`
- [ ] `deliverables/prod/references.md` exists listing all sources with type, URL, and theme links — each row has an HTML anchor matching footnote slugs
- [ ] `deliverables/prod/glossary.md` exists with key terms — each row has an HTML anchor matching cross-link slugs
- [ ] All links are relative and resolve correctly
- [ ] No build tools or JS required to read the files

## Lessons Learned

_Update this section as you encounter quirks during execution._
