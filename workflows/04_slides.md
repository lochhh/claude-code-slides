# Workflow 04: Generate Slide Deck

## Objective

Generate a polished HackMD reveal.js slide deck called "Go Pro with Claude Code", based on the content from `docs/`. ~20–30 slides, speaker notes for a 1-hour session. In the last slide, link to the master guide on https://lochhh.github.io/claude-code-slides/.

## Prerequisites

- Phase 3 complete: all files in `docs/` reviewed and approved
- `uv sync` already run

## Steps

1. **Run slide generator:**
   ```
   uv run python tools/generate_slides.py
   ```
2. **Review output:** open `deliverables/slides.md`
3. **Paste into HackMD** (hackmd.io) and verify reveal.js renders correctly:
   - All slides present and readable
   - Speaker notes visible in presenter view (press `S`)
   - Code blocks syntax-highlighted
4. **Adjust timing** in speaker notes if needed (target ~2–3 min per slide)

## reveal.js Syntax Reference

| Element | Syntax |
|---------|--------|
| Slide separator (horizontal) | `---` on its own line |
| Slide separator (vertical/sub) | `----` on its own line |
| Speaker notes | `Note: <text>` after slide content |
| Slide title | `## Title` (h2 = slide heading) |
| Fragment (appear on click) | `<!-- .element: class="fragment" -->` |
| Background colour | `<!-- .slide: data-background="#hex" -->` |
| Code block | standard fenced ` ``` ` |

**HackMD front matter:**
```yaml
---
title: Go Pro with Claude Code
tags: claude-code, engineering, productivity
slideOptions:
  transition: slide
---
```

## Target Deck Structure

| Slide # | Content |
|---------|---------|
| 1 | Title: "Go Pro with Claude Code" + subtitle |
| 2 | About this session (goals, audience) |
| 3 | Agenda (theme list) |
| 4–6 | Productivity & IDE |
| 7–9 | CLAUDE.md & project memory |
| 10–12 | Prompting Strategies |
| 13–15 | Context Management |
| 16–18 | Commands, skills & plan mode |
| 19–21 | MCP Servers |
| 22–24 | Hooks & Automation |
| 25–27 | Parallel Development |
| 28 | Summary: top 5 things to do tomorrow |
| 29 | Resources & links |

## Speaker Notes Format

Each slide's `Note:` block should include:
- **Talking points:** 2–3 bullet sentences to expand on
- **Demo cue** (if applicable): "DEMO: show CLAUDE.md in VS Code"

## Completion Criteria

- [ ] `deliverables/slides.md` exists
- [ ] Front matter with `slideOptions` present
- [ ] 20–30 slides separated by `---`
- [ ] Every slide has a speaker note (`Note:`)
- [ ] At least one code block example per theme section
- [ ] Renders correctly when pasted into HackMD

## Lessons Learned

_Update this section as you encounter quirks during execution._

- **Slide overflow**: Content overflows the viewport silently — no error, just hidden text. Slides with multiple code blocks or long tables are highest risk. Break into subslides or trim to bullet points. Rule of thumb: one code block + 3–5 bullet points max per slide. Test by pasting into HackMD and checking each slide visually.
