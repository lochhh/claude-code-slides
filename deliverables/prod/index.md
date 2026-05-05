# Becoming a Pro with Claude Code Pro

> A master guide for software engineers who've hit the ceiling with basic Claude Code usage.

## Learning path

**Beginner → Novice → Intermediate → Advanced → Expert**

**Beginner** engineers know how to open Claude Code and type a prompt. They get useful output on small, self-contained tasks.

**Novice** engineers understand that Claude needs context to work well. They write a meaningful CLAUDE.md, specify constraints in prompts, and know when to clear and restart a session. At this level, Claude stops feeling like a slot machine.

**Intermediate** engineers treat the context window as a resource to manage deliberately. They use context compaction on a schedule, connect MCP servers to eliminate tool switches, define slash commands for repeated workflows, and route tasks to the right model. Claude becomes a reliable collaborator rather than an unpredictable assistant.

**Advanced** engineers automate the scaffolding. Hooks enforce quality gates deterministically — formatting, linting, secret protection — without relying on prompts. The workflow runs the same way every time, regardless of how the session unfolded.

**Expert** engineers run parallel workstreams. Git worktrees with isolated context windows, specialist subagents dispatched from an orchestrating session, per-worktree environment isolation — at this level, one engineer with Claude Code produces the output of a small team.

---

## Recommended reading order

Start here if you are working through the guide from scratch. Each theme builds on the concepts introduced before it.

1. **[Productivity, IDE & cost](productivity-ide-cost.md)** — Set up your environment correctly before developing habits around the wrong defaults. Model routing, context compaction milestones, and IDE extensions all belong at session setup, not retrofit.

2. **[CLAUDE.md & project memory](claudemd-setup.md)** — CLAUDE.md is the highest-leverage file in any project. Get this right before every other habit. Novice-level but foundational: every downstream theme depends on a well-structured CLAUDE.md.

3. **[Prompting strategies](prompting-strategies.md)** — Good CLAUDE.md rules compound with good prompts. Learn the difference between vague and precise, when to let Claude reason freely and when to constrain it hard.

4. **[Context management](context-management.md)** — Once you have CLAUDE.md and prompting discipline, the next ceiling is the context window. Understand how compaction works, when to compact vs. clear, and how to preserve decisions across session boundaries.

5. **[Commands, skills & plan mode](commands-skills-plan-mode.md)** — Convert your most effective prompts into reusable commands and skills. Plan mode gives you a review checkpoint before files change. These three primitives raise the floor on every session.

6. **[MCP servers](mcp-servers.md)** — Eliminate context switches to GitHub, databases, and live documentation. The right 2–3 MCP servers turn Claude Code into a single interface for your entire stack.

7. **[Hooks & automation](hooks-automation.md)** — Make guarantees the model cannot break. Hooks are the most underused power feature in Claude Code. Use them to enforce what CLAUDE.md can only request.

8. **[Parallel development](parallel-development.md)** — Run multiple independent workstreams simultaneously using git worktrees and subagents. Read this only after you are comfortable with context management and hooks — the failure modes at this level are expensive if you are not prepared.

---

## Themes

| # | Theme | Level | Summary |
|---|-------|-------|---------|
| 1 | [Productivity, IDE & cost](productivity-ide-cost.md) | Basic | Small, repeatable habits — model routing, compaction milestones, IDE extensions, keybindings, and token spend monitoring — that compound into days of saved time across hundreds of sessions. |
| 2 | [CLAUDE.md & project memory](claudemd-setup.md) | Novice | CLAUDE.md is Claude's standing orders for every session; structured correctly with explicit prohibitions, layered imports, and a gotchas section, it eliminates the correction loops that define the basic-usage ceiling. |
| 3 | [Prompting strategies](prompting-strategies.md) | Novice | Specificity, explore-before-code discipline, targeted file references, and constraint-based scoping are the habits that separate engineers who direct Claude from those who correct it. |
| 4 | [Context management](context-management.md) | Intermediate | Treating compaction, clearing, and phase boundaries as first-class workflow tools — not reactive fixes — is what keeps Claude's quality consistent across sessions that span hours or days. |
| 5 | [Commands, skills & plan mode](commands-skills-plan-mode.md) | Intermediate | Custom slash commands and skills codify your best prompts into repeatable, team-shareable operations; plan mode adds a read-only review gate before any changes land. |
| 6 | [MCP servers](mcp-servers.md) | Intermediate | MCP servers expose GitHub, databases, live docs, and Playwright as tools Claude calls natively — eliminating the most common context switches and making Claude Code a single interface for your stack. |
| 7 | [Hooks & automation](hooks-automation.md) | Advanced | Hooks execute deterministic shell commands and Python scripts at 25+ lifecycle points outside the LLM, turning CLAUDE.md's polite instructions into hard, unconditional guarantees. |
| 8 | [Parallel development](parallel-development.md) | Expert | Git worktrees with filesystem isolation plus explicitly scoped subagents let one engineer run three to five independent workstreams simultaneously, merging back through standard PR discipline. |

---

## Cross-theme insights

The most important insight across all eight themes is that Claude Code's primitives are designed to compose. CLAUDE.md sets standing rules; hooks enforce those rules at execution time; commands and skills package your best prompts into reusable units; MCP servers connect those commands to external services; and worktrees with subagents let the whole system run in parallel. Engineers who treat these as independent features plateau at each level. Engineers who wire them together keep improving.

Context is the shared resource that all eight themes orbit. CLAUDE.md, hooks, commands, MCP servers, and worktrees are all ultimately mechanisms for controlling what ends up in Claude's context window, and when. CLAUDE.md loads project rules into every session; the `@`-import pattern and PostCompact hooks re-inject critical rules after compaction; line-range file references keep irrelevant content out; MCP servers pull live data in on demand rather than stuffing it in upfront; and worktrees give each parallel task its own clean window so nothing bleeds across. Build a mental model of the context window as the constraint, and the purpose of each primitive becomes immediately clear.

Automation unlocks the productivity ceiling that prompting alone cannot reach. Hooks running formatters, test runners, and security guards on every file write — without any prompt — are more reliable than any instruction in CLAUDE.md. Skills with `context: fork` run heavy audits in isolated subagents without polluting the main session. The `/loop` skill monitors a long-running process in the background while you work on something else. At the highest level of usage, the proportion of tasks you direct manually shrinks and the proportion handled by hooks, skills, and agents grows. The engineer's job shifts from prompting to orchestration.

---

## Reference

- [Primitives](primitives.md) — the 14 building blocks all eight themes build on, from CLAUDE.md to git worktrees
- [Glossary](glossary.md) — definitions for every technical term used across the guide
- [References](references.md) — all 82 sources cited inline across the eight theme files

---

*Generated from 82 sources. See [analysis](../analysis.md) for source details.*
