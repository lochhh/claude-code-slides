# Workflow 03: Synthesise Master Guide

## Objective

Write a clean, structured master guide to `deliverables/prod/` — one index file and one file per theme. GitHub Pages ready (plain GFM, relative links, no build tools).

## Prerequisites

- Phase 2 complete: `deliverables/analysis.md` exists and has been reviewed
- `uv sync` already run

## Steps

1. **Run synthesis tool:**
   ```
   uv run python tools/synthesise_guide.py
   ```
2. **Review output files:**
   - `deliverables/prod/index.md` — landing page with theme summaries and links
   - `deliverables/prod/<theme-slug>.md` per theme
3. **Spot-check each theme file** for:
   - Summary paragraph present
   - Tips numbered and ranked
   - At least one concrete example per tip (real command, prompt snippet, or CLAUDE.md excerpt)
   - Relative links working (no absolute paths to prod/)
4. **Verify GitHub Pages compatibility:** relative links between files, no JS required, no build output

## Output Format

### `deliverables/prod/index.md`

```markdown
# Becoming a Pro with Claude Code Pro

> A master guide for software engineers who've hit the ceiling with basic Claude Code usage.

## Themes

| # | Theme | Summary |
|---|-------|---------|
| 1 | [CLAUDE.md & Setup](claudemd-setup.md) | ... |
| 2 | [Context Management](context-management.md) | ... |
...

---
*Generated from N sources. See [analysis](../analysis.md) for source details.*
```

### `deliverables/prod/<theme-slug>.md`

```markdown
# <Theme Name>

[← Back to index](index.md)

<One-paragraph summary — what this theme is, why it matters for engineers at the ceiling.>

## Tips

### 1. <Tip Title>

<Brief explanation — why this works, when to use it.>

**Example:**
```<language>
<real command, config snippet, or prompt>
```

### 2. ...

---
*Sources: [file1](../../raw/file1.md), [file2](../../raw/file2.md)*
```

## Completion Criteria

- [ ] `deliverables/prod/index.md` exists with links to all theme files
- [ ] One `.md` file per theme in `deliverables/prod/`
- [ ] Each theme file has: summary paragraph, numbered ranked tips, ≥1 concrete example per tip
- [ ] All links are relative and resolve correctly
- [ ] No build tools or JS required to read the files

## Lessons Learned

_Update this section as you encounter quirks during execution._
