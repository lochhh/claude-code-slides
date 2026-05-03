# Workflow 02: Analyse Sources

## Objective

Read all collected raw files, deduplicate overlapping advice, cluster into 6–8 themes, rank tips by frequency across sources, and save analysis to `deliverables/analysis.md`.

## Prerequisites

- Phase 1 complete: `deliverables/raw/` contains 10+ `.md` files
- `uv sync` already run

## Steps

1. **Run analysis tool:**
   ```
   uv run python tools/analyse_sources.py
   ```
2. **Review output:** open `deliverables/analysis.md`, verify:
   - 6–8 distinct themes identified
   - Each theme has 3+ ranked tips
   - Concrete examples (commands, config snippets) captured per tip
3. **Spot-check**: if a theme looks thin (<3 tips), consider adding more raw sources for that topic (re-run Phase 1 for that topic)

## Suggested Themes

The tool will determine themes from the content, but expect something like:

| # | Theme | Slug |
|---|-------|------|
| 1 | CLAUDE.md & Project Setup | `claudemd-setup` |
| 2 | Context Management | `context-management` |
| 3 | MCP Servers | `mcp-servers` |
| 4 | Hooks & Automation | `hooks` |
| 5 | Multi-Agent & Worktrees | `multi-agent` |
| 6 | Prompting & Plan Mode | `prompting` |
| 7 | Productivity & IDE | `productivity` |
| 8 | Cost & Token Management | `cost-management` |

## Output Format

`deliverables/analysis.md`:

```markdown
# Analysis: Claude Code Research

## Themes

### 1. <Theme Name>

**Summary:** One-sentence description.

**Tips (ranked by frequency):**
1. <Tip> — seen in N sources
   - Example: `<command or config snippet>`
   - Sources: [file1.md], [file2.md]
2. ...

---
### 2. ...
```

## Completion Criteria

- [ ] `deliverables/analysis.md` exists
- [ ] 6–8 themes with clear boundaries
- [ ] Each theme has 3+ tips, ranked by source frequency
- [ ] At least one concrete example per tip
- [ ] Source attribution present

## Lessons Learned

_Update this section as you encounter quirks during execution._
