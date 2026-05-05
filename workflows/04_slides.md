# Workflow 04: Generate Slide Deck

## Objective

Generate a polished HackMD reveal.js slide deck called "Becoming a Pro with Claude Code Pro" targeting software engineers. ~20–30 slides, speaker notes for a 1-hour session.

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
title: Becoming a Pro with Claude Code Pro
tags: claude-code, engineering, productivity
slideOptions:
  theme: moon
  transition: slide
---
```

## Target Deck Structure

| Slide # | Content |
|---------|---------|
| 1 | Title: "Becoming a Pro with Claude Code Pro" + subtitle |
| 2 | About this session (goals, audience) |
| 3 | Agenda (theme list) |
| 4–6 | Theme 1: CLAUDE.md & Setup |
| 7–9 | Theme 2: Context Management |
| 10–12 | Theme 3: MCP Servers |
| 13–15 | Theme 4: Hooks & Automation |
| 16–18 | Theme 5: Multi-Agent & Worktrees |
| 19–21 | Theme 6: Prompting & Plan Mode |
| 22–24 | Theme 7: Productivity & IDE |
| 25–27 | Theme 8: Cost & Token Management |
| 28 | Summary: top 5 things to do tomorrow |
| 29 | Resources & links |
| 30 | Q&A |

## Speaker Notes Format

Each slide's `Note:` block should include:
- **Time guidance:** "~2 min" or "~3 min — pause for questions"
- **Talking points:** 2–3 bullet sentences to expand on
- **Demo cue** (if applicable): "DEMO: show CLAUDE.md in VS Code"
- **Audience check:** questions to ask if energy drops

## Completion Criteria

- [ ] `deliverables/slides.md` exists
- [ ] Front matter with `slideOptions` present
- [ ] 20–30 slides separated by `---`
- [ ] Every slide has a speaker note (`Note:`)
- [ ] At least one code block example per theme section
- [ ] Renders correctly when pasted into HackMD

## Lessons Learned

_Update this section as you encounter quirks during execution._
