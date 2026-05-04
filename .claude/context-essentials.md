# Context Essentials (Re-injected After Compaction)

> **Agent instruction:** On session start or post-compact, output a brief state recap (current phase, what's done, what's next) before answering the user's first message.

## Project Status
- Phase 1 (research): DONE — 82 files in deliverables/raw/
- Phase 2 (analyse): DONE — deliverables/analysis.md (8 themes, 74 tips)
- Phase 3 (synthesise): PENDING — write deliverables/prod/ (index.md + 8 theme files)
- Phase 4 (slides): PENDING — write deliverables/slides.md (HackMD reveal.js)

## Critical Rules
- WAT framework: read workflows/ SOP first, use tools/ before creating new scripts
- No Anthropic API key — phases 2-4: agent reads files in-conversation, no Python LLM calls
- Tavily API for search: `uv run python tools/search_web.py "<query>" --topic "<name>"`
- Package manager: uv (NOT pip). Install: `uv sync`. Run tools: `uv run python tools/<script>`
- Skip-if-exists: all tools check output file before re-fetching — don't force re-run
- Don't create or overwrite workflows/ files without asking the user first

## Banned Patterns
- `pip install` — use `uv add` or `uv sync`
- Calling Anthropic API (no key in .env)
- Re-searching topics already saved in deliverables/raw/

## Phase Contract
Current phase: Phase 3 — Synthesise (write deliverables/prod/)
Next phase: Phase 4 — Slides (write deliverables/slides.md)

Operating in a phase-based workflow. At a phase boundary, you MUST:
1. Edit this file — advance "Current phase" to the next phase and update "Next phase" accordingly
2. Produce a concise summary of the completed phase: goals, key decisions, constraints, outputs
3. Start fresh (i.e. clear) for the next phase: treat prior content as read-only background, do not continue old threads, re-establish goals, request missing inputs if needed

These rules override conversational momentum.

## Key Facts
- Slide title: "Becoming a Pro with Claude Code Pro"
- Audience: intermediate/advanced software engineers who mostly develop in Python and hit the Claude Code raw prompting ceiling
- 8 themes: CLAUDE.md Setup, Context Management, Hooks & Automation, MCP Servers, Parallel Dev (Subagents + Worktrees), Commands/Skills/Plan Mode, Prompting Strategies, Productivity/IDE/Cost
- deliverables/prod/: GitHub Pages compatible, relative links, no build tools required
