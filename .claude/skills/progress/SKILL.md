---
description: Check project status across all phases
allowed-tools: Read, Glob
---

# /progress — Project status across all phases

Report current pipeline state without running anything.

## What to do

1. **Phase 1 — Research**
   - Count `.md` files in `deliverables/raw/` (target: 10+)
   - List which of the 12 topics from `workflows/01_research.md` have coverage (match filenames to topic slugs)
   - Flag any topic with no file

2. **Phase 2 — Analyse**
   - Check `deliverables/analysis.md` exists
   - If exists: count themes found (scan for `### ` headings), count total tips
   - Report: DONE / MISSING

3. **Phase 3 — Synthesise**
   - Check `docs/` exists
   - Check for: `index.md`, `primitives.md`, `references.md`, `glossary.md`
   - Check for one file per theme (8 expected slugs: `claudemd-setup.md`, `context-management.md`, `hooks-automation.md`, `mcp-servers.md`, `parallel-dev.md`, `commands-skills-plan-mode.md`, `prompting-strategies.md`, `productivity-ide-cost.md`)
   - Report: DONE / IN PROGRESS (N/12 files) / MISSING

4. **Phase 4 — Slides**
   - Check `deliverables/slides.md` exists
   - If exists: count slides (count `---` separators)
   - Report: DONE / MISSING

## Output format

```
## Project Status — <today's date>

Phase 1 · Research    ✅ DONE      82 files · all 12 topics covered
Phase 2 · Analyse     ✅ DONE      8 themes · 74 tips
Phase 3 · Synthesise  🔄 PENDING   0/12 files in docs/
Phase 4 · Slides      🔄 PENDING   deliverables/slides.md missing

Current phase: 3 — Synthesise
Next action: <what to do next>
```

No arguments needed.
