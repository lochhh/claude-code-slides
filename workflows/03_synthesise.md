# Workflow 03: Synthesise Master Guide

## Objective

Transform analytical output into polished, navigable, pedagogically structured documentation for software engineers mastering Claude Code. Output: primitives reference + index + one file per theme in `deliverables/prod/`. GitHub Pages ready (plain GFM, relative links, no build tools).

## Prerequisites

- Phase 2 complete: `deliverables/analysis.md` exists and has been reviewed
- `uv sync` already run

## Steps

1. **Run synthesis tool:**
   ```
   uv run python tools/synthesise_guide.py
   ```
2. **Review output files:**
   - `deliverables/prod/primitives.md` — core Claude Code primitives with definitions, purpose, examples
   - `deliverables/prod/index.md` — landing page with learning path, usage levels, and theme overview
   - `deliverables/prod/<theme-slug>.md` per theme
   - `deliverables/prod/glossary.md` — key terms
   - `deliverables/prod/references.md` — all sources listed, linkable per theme
3. **Spot-check primitives page** for:
   - All primitives covered in usage-level order — basic: CLAUDE.md, tool use, project structure, permissions & settings, context model; novice: context compaction, memory, slash commands & skills, plan mode; intermediate: agents, hooks, MCP servers; advanced: plugins, git worktrees
   - Each primitive has: definition, purpose explanation, concrete example (Python-specific where possible; otherwise general with Python adaptation note)
4. **Spot-check each theme file** for:
   - Summary paragraph present
   - Tips numbered, ranked, rewritten for clarity/consistency
   - At least one concrete example per tip (real command, prompt snippet, or CLAUDE.md excerpt)
   - Pitfalls, misconceptions, and "when to use this" guidance
   - Cross-links to related themes
   - Relative links working (no absolute paths to prod/)
5. **Verify index** includes: beginner → expert learning path, usage levels, recommended reading order, cross-theme insights, link to primitives page
6. **Verify GitHub Pages compatibility:** relative links between files, no JS required, no build output

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
- [ ] Each theme file has: summary paragraph, numbered ranked tips, ≥1 concrete example per tip, pitfalls/misconceptions, "when to use this", cross-links to related themes
- [ ] `deliverables/prod/references.md` exists listing all sources with type, URL, and theme links
- [ ] Each theme file links to relevant entries in `references.md` (not directly to raw files)
- [ ] `deliverables/prod/glossary.md` exists with key terms
- [ ] All links are relative and resolve correctly
- [ ] No build tools or JS required to read the files

## Lessons Learned

_Update this section as you encounter quirks during execution._
