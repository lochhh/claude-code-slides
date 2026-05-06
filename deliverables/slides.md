---
title: Go Pro with Claude Code
tags: claude-code, engineering, productivity
slideOptions:
  transition: slide
---

## Becoming a Pro with Claude Code

**From "Claude is helpful" → "Claude is a force multiplier"**

Note:
- Talking points: This session is for engineers who already use Claude Code daily but keep running into the same walls — Claude forgets context, introduces unwanted patterns, and you spend more time correcting than building. We'll cover 8 themes that compound, from basic habits to expert-level parallel workstreams.
- Target audience: engineers comfortable prompting Claude on individual tasks; today we rewire the workflow.
- No demos until slide 7 — first 6 slides set the mental model.

---

## The problem

> "My project has grown past what fits in one conversation. Claude forgets conventions, introduces unwanted patterns, and I spend more time correcting than building."

----

Root cause is usually one of three things:
- No standing rules (CLAUDE.md)
- No context management discipline
- No enforcement layer (hooks)

Note:
- Target session length: 55 min content + 5 min Q&A.

---

## The 5 Levels

- **Beginner** — Small, self-contained tasks. 
- **Novice** — Meaningful CLAUDE.md. Knows when to restart.
- **Intermediate** — Context as a resource. MCP servers. Slash commands.
- **Advanced** — Hooks enforce quality gates. Workflow is deterministic.
- **Expert** — Parallel worktrees. Subagents. One engineer = small team.

Note:
Most engineers plateau at **Novice** — never invest in CLAUDE.md. That jump is the highest-ROI move in this session.

---

## Themes

1. **Productivity & IDE** — habits that save hours per week
2. **CLAUDE.md** — standing orders that survive context resets
3. **Prompting strategies** — directing vs. correcting
4. **Context management** — keeping quality consistent across sessions

----

5. **Commands & plan mode** — define once, invoke consistently
6. **MCP servers** — single interface for your whole stack
7. **Hooks & automation** — deterministic quality gates
8. **Parallel development** — one engineer, three workstreams

Note:
- Talking points: Themes 1–3 are Beginner/Novice. Themes 4–6 are Intermediate. Themes 7–8 are Advanced/Expert. Each theme assumes the previous ones.
- The cross-cutting insight: all 8 themes are ultimately about controlling what ends up in Claude's context window, and when. Keep that frame.

---

## Theme 1: Productivity & IDE

- `Shift+Tab` cycles permission modes (default → acceptEdits → plan)
- `ccusage daily` — per-day spend, not just session totals
- `MAX_THINKING_TOKENS=10000` — cap extended thinking costs
- `Option+K` / `Alt+K` — insert `@filename#line-range` from selection
- Default to Sonnet; Haiku for reviews; Opus sparingly
- Model routing alone: 70% cost reduction on review/test tasks, zero quality loss

Note:
- DEMO: show `ccusage daily` live to illustrate what "per-day breakdown" looks like vs. `/cost`.

----

## Key Shortcuts

```bash
# Permission modes
Shift+Tab  →  default → acceptEdits → plan

# VS Code extension
Cmd+Esc / Ctrl+Esc      # Toggle editor ↔ Claude
Option+K / Alt+K        # Insert @filename#line-range
Cmd+N / Ctrl+N          # New conversation

# Cost monitoring
npm install -g @ryoppippi/ccusage
ccusage daily           # Per-day breakdown
ccusage blocks --live   # Live 5-hour billing window

# Cap extended thinking
export MAX_THINKING_TOKENS=10000
```

- `ccusage blocks --live` — catches expensive sessions in real time; add to shell profile
- VS Code extension auto-shares current file, selection, Problems panel — no manual copy-pasting
- Compact at session milestones, not reactively

Note:

---

## Theme 2: CLAUDE.md

- Loaded at **every session start**
- Survives context resets
- Eliminates correction loops
- Scales with project complexity via layered files
- Not a README — a briefing. Commands, prohibitions, gotchas Claude can't infer from code
- ~77 lines sweet spot; compliance degrades past ~145 lines — use `@`-imports for the rest

Note:
- DEMO: open a real CLAUDE.md in VS Code and walk through the structure live.

----

## CLAUDE.md Structure

```markdown
# CLAUDE.md

@.claude/context-essentials.md   ← imports critical rules

## Commands
- Test: `uv run pytest tests/ -x --tb=short`
- Lint: `uv run ruff check . && uv run mypy src/`

## Hard rules
- Never use `pip` — always `uv`
- Never touch `/src/auth/` without explicit confirmation
- Never commit `.env` files

## Known footguns
- `Result[T, E]` everywhere — never raise, always return Result
- `/api/v1` frozen — all new endpoints go in `/api/v2`
- Pydantic v2 — always `.model_dump()`, never `.dict()`

## References
- Architecture: see `docs/architecture.md`
```


Note:
- "Never X" for hard rules — vague guidance = soft preference; explicit prohibitions = hard constraints
- `footguns` section has highest signal-to-noise — add every time Claude hits a project-specific trap

----

## Layered CLAUDE.md for Monorepos

```
/CLAUDE.md                     # shared: uv, ruff, global prohibitions
/services/auth/CLAUDE.md       # JWT patterns, "never touch X"
/services/billing/CLAUDE.md    # Stripe webhooks, idempotency rules
/packages/shared-db/CLAUDE.md  # migration conventions, query patterns
```

----

Claude loads the **most local** file — service rules don't pollute shared context.

- Global rules at root only — if you're copying a rule across files, move it to root
- Update reactively: repeated mistake = missing rule. Add it immediately.

Note:

---

## Theme 3: Prompting Strategies

1. **Be explicit** — specify file, language, constraints, format
2. **Explore before code** — force a plan, confirm before implementing
3. **Use `@file` references** — stack context incrementally

----

4. **Paste the error, say "fix"** — avoid anchoring bias
5. **Verify after** — "Are you sure about this?"
6. **Constrain scope** — "under 50 lines, stdlib only, no abstractions"

Note:
- Heuristic: show your prompt to a colleague with no context — if they'd be confused, Claude will be too
- Anchoring bias: speculative framing ("probably X, try Y") locks Claude onto your hypothesis even when wrong
- Two failed attempts = `/clear` and reframe; more words in a stuck session makes it worse

----

## Prompt Patterns

```bash
# Bad
claude "Add authentication."

# Good
claude "Add JWT authentication to src/middleware/auth.py.
Use the existing User model in src/models/user.py.
Return 401 if the token is invalid, 403 if expired.
```

- File paths + constraints + error codes = no room for guesswork
- Two failed attempts = `/clear` and reframe; more words in a stuck session makes it worse

Note:

----

## Explore-Then-Plan Gate

```text
Before implementing:
1. Read src/auth/middleware.py
2. Read tests/test_auth.py
3. Check git log --oneline -10 src/auth/middleware.py
4. Write out your approach in plain English

Only start coding after I confirm the plan.
```

Note:
- Pair with plan mode (Shift+Tab ×2) — review plan, catch misunderstandings, then acceptEdits
- `@file` refs: build context high-to-low — architecture first, implementation second

---

## Theme 4: Context Management

As sessions grow, foundational decisions get compressed while recent noise stays sharp.

- Context rot is silent — by the time Claude contradicts an earlier decision, you're past clean recovery
- 80% warning is a lagging indicator — compact proactively at 60%
- Phase-based: architecture → implementation → testing, each seeded from HANDOFF.md

----

**Three strategies that compose:**

| Strategy | What it targets |
|----------|----------------|
| `/compact` with preservation | Whole-window growth |
| Tool-result clearing | Bulky re-fetchable payloads |
| Memory/notes files | Cross-session persistence |

Note:

----

## Compact Discipline

```text
# Check before the warning fires
/statusline   →  58% — compact now

# Targeted preservation instructions
/compact Keep: (1) decision to use PostgreSQL not SQLite and why,
(2) the three functions identified for refactoring in payments.py,
(3) current unresolved KeyError in auth.py line 142.
Clear: grep output, file reads (re-fetchable).

# Verify state immediately after
Summarize where we are and what we're working on next.
```

----

```text
# Phase boundary: produce a handoff
Write a summary of all decisions made this session to HANDOFF.md.
Include: data model, auth approach, API surface, open questions.

# New session: seed from handoff
Read HANDOFF.md. Implementing auth module based on those decisions.
```

----

- `/compact` cheapest when cache is warm (within 5 min of last message) — been away longer? Use `/clear`
- `/rewind` for drift — erroneous reasoning persists and contaminates; don't correct in the same context

Note:

----

## Re-inject Context Post-Compact

```markdown
# .claude/context-essentials.md  (keep under 50 lines)
## Critical rules
- Use dateutil for ALL date parsing — never datetime.strptime
- DB: execute reads via db.execute_read(); writes require db.transaction()
- Auth: validate tokens in middleware — never accept user_id from request body
```

----

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "compact",
        "hooks": [{
          "type": "command",
          "command": "cat \"$CLAUDE_PROJECT_DIR\"/.claude/context-essentials.md"
        }]
      }
    ]
  }
}
```

----

- `@` import in CLAUDE.md = fires every session; SessionStart hook with `matcher: "compact"` = post-compaction only
- **Pitfall:** `PostToolUse` with `matcher: "compact"` never fires — `/compact` is a slash command, not a tool call

Note:

---

## Theme 5: Commands & Plan Mode

```
.claude/
  commands/
    review-auth.md      →  /review-auth
    fix-issue.md        →  /fix-issue 123
    smart-commit.md     →  /smart-commit
  skills/
    security-audit/
      SKILL.md          →  /security-audit  (context: fork)
```

- Any prompt typed 2+ times/week belongs in a command file
- Commit `.claude/commands/` to version control — whole team shares the shorthand

----

**Plan mode** = read-only review gate before any changes land

```
Shift+Tab ×2  →  plan mode
Shift+Tab ×1  →  acceptEdits
```

- Plan mode costs seconds, prevents hours of `/rewind` — habit before touching >3 files

Note:
- DEMO: show /fix-issue command file with $ARGUMENTS and YAML frontmatter live.

----

## Command Anatomy

```markdown
# .claude/commands/fix-issue.md
---
argument-hint: <issue-number>
description: Fix a GitHub issue following project error-handling conventions
allowed-tools: Read, Edit, Bash(git diff *), Bash(gh issue view *)
---

Fix GitHub issue #$ARGUMENTS following our error handling conventions.

Steps:
1. Run: gh issue view $ARGUMENTS
2. Identify affected files
3. Implement the fix
4. Add or update tests covering the fix
5. Show a diff before committing
```

Note:
- `allowed-tools` enforced at framework level — not just prompt text; critical for read-only audits
- `$ARGUMENTS` replaced at invocation time; `!` backtick syntax injects live shell output

----

## Skills vs Commands

```markdown
# .claude/skills/security-audit/SKILL.md
---
description: "Perform a security audit using grep and glob (runs in subagent)"
subagent: true
disable-model-invocation: false
---

# /security-audit
Claude, please use the `grep` and `read` tools to scan for secrets, 
open ports, or vulnerable dependencies. Do not make changes.
```

----

## Commands: Manual Execution

- Trigger: User-initiated via /slash syntax.
- Purpose: Immediate shortcuts for one-off actions.
- Best For: Side effects requiring timing (e.g., /deploy, /commit).
- Usage: You provide explicit arguments and tell Claude exactly when to act.

----

## Skills: Autonomous Expertise

- Trigger: Context-aware; Claude decides when to use them.
- Purpose: Recurring workflows and domain-specific knowledge.
- Best For: Enforcing style guides or complex, multi-step logic.
- Efficiency: "Lazy-loads" only when needed to save tokens.

## Unified Implementation

- Flexibility: Modern Claude Code treats both **skills** and **commands** as part of a single extensibility layer.
- Graduation: Start with a manual Command, then transition to an autonomous Skill as trust grows.
- MCP Integration: Skills act as the "brain" that tells Claude how to use external MCP tools.

Note:

---

## Theme 6: MCP Servers

**Default trio for Python developers:**

```bash
# Register once, available everywhere
claude mcp add sequential-thinking -s user \
  -- npx -y @modelcontextprotocol/server-sequential-thinking

claude mcp add github -s user \
  -- npx -y @modelcontextprotocol/server-github

claude mcp add context7 -s user \
  -- npx -y @context7/mcp-server
```

----

- Each MCP adds startup time — don't register speculatively; this trio covers 80% of daily needs
- Context7 fetches live docs (FastAPI, Pydantic, SQLAlchemy) — eliminates hallucinated APIs
- Add DB/Playwright MCPs per-project, not globally

Note:

----

## MCP Configuration

```json
// .mcp.json — safe to commit (tokens via env vars)
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}" }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": { "POSTGRES_CONNECTION_STRING": "${DATABASE_URL}" }
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"],
      "lazy": true      ← only starts when first tool is called
    }
  }
}
```

Note:
- Always `${VAR_NAME}` for secrets — hardcoded tokens end up in reflog and PR history
- `lazy: true` defers server spawn until first call — use for heavy MCPs you only need occasionally
- Postgres: always read-only credentials; natural language → SQL makes destructive queries easy to trigger

----

## MCP in Practice

```
# Full PR lifecycle from terminal
Review PR #456 in the current repo. Focus on whether the database queries in user_service.py will cause N+1 issues with SQLAlchemy.
```

```
# Live docs prevent hallucinated APIs
Using the current FastAPI docs, show me how to add dependency injection for a SQLAlchemy async session.
```

```
# E2E test generation
Navigate to http://localhost:8000/login, fill in the test credentials, submit the form, and generate a Playwright pytest fixture.
```

Note:
- GitHub MCP: no browser context switch — issues, PRs, diffs stay in terminal
- Context7 needs connectivity; in air-gapped envs it silently falls back to training data — verify with `claude mcp list`

---

## Theme 7: Hooks & Automation

Hooks execute deterministic shell commands at **25+ lifecycle points** — outside the LLM, every time, regardless of prompt phrasing.

| Hook | Trigger | Use case |
|------|---------|---------|
| `PreToolUse` | Before any tool call | Block dangerous ops, auto-allow reads |
| `PostToolUse` | After any tool call | Run formatter, run tests |
| `Stop` | Before Claude stops | Lint gate, quality check |
| `SessionStart` | Session begins | Prime context from git history |

----

- Written "always run black" in CLAUDE.md and Claude keeps skipping it? Hooks are the fix.
- **Critical:** `exit 1` = warn only; `exit 2` = block — most teams get this wrong and never notice

Note:
- DEMO: show a PostToolUse formatter hook firing live as Claude edits a Python file.

----

## Hook Anatomy

```python
#!/usr/bin/env python3
# .claude/hooks/guard_git.py
import json, sys, re

data = json.load(sys.stdin) # event, tool name, args
cmd = data.get("tool_input", {}).get("command", "")

dangerous = [
    r"git\s+push\s+(-f|--force)(\s+origin)?\s+main",
    r"git\s+reset\s+--hard",
    r"DROP\s+(TABLE|DATABASE)",
]
for pattern in dangerous:
    if re.search(pattern, cmd, re.IGNORECASE):
        print(f"BLOCKED: {cmd}", file=sys.stderr)
        sys.exit(2)   # exit 2 = BLOCK. exit 1 = warn only.
sys.exit(0)
```

Note:

----

## Wiring Hooks

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash", // targets specific tool names
      "hooks": [{"type": "command",
        "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/guard_git.py"}]
    }]
  }
}
```

- Three scope levels: `~/.claude/settings.json` (personal) → `.claude/settings.json` (project, commit it) → `.claude/settings.local.json` (local, gitignore)

Note:
- Talking points: DEMO — show a PostToolUse formatter hook firing live as Claude edits a Python file.
- Stop hooks: a Stop hook returning "ok": false fires again, creating an infinite loop. Always check the stop_hook_active field.
- Hooks are the most underused power feature in Claude Code. If you've ever written "always run black" in CLAUDE.md and watched Claude skip it — hooks are the fix.
- `matcher` targets specific tool names (`Bash`, `Edit`, `Write`)
- Hooks fire **outside** the LLM — no prompt phrasing bypasses them
- Stop hooks need `stop_hook_active` guard to avoid infinite loops

---

## Production Hook Stack

```python
# PostToolUse: auto-format on every file write to eliminate "Claude skipped the formatter" correction loops
if file_path.endswith(".py"):
    subprocess.run(["uv", "run", "ruff", "format", "--quiet", file_path])
elif file_path.endswith((".js", ".ts")):
    subprocess.run(["npx", "prettier", "--write", file_path])
```

```python
# PostToolUse: run matching test file after every source edit to catch regressions immediately
test_file = f"tests/test_{os.path.basename(file_path)}"
if os.path.isfile(test_file):
    subprocess.run(["uv", "run", "pytest", test_file, "-x", "--tb=short"])
```

Note:
- DEMO: show a PostToolUse formatter hook firing live as Claude edits a Python file.

---

## Hook Performance & Guards

```python
# PreToolUse: block writes to sensitive files
SENSITIVE = re.compile(r"(\.env$|secrets\.|credentials|\.pem$|uv\.lock)")
if SENSITIVE.search(file_path):
    sys.exit(2)  # BLOCKED
```

- **PreToolUse** is synchronous — target <200ms, hard limit 500ms
- 50 writes × 600ms = 30s dead time; move slow ops to PostToolUse
- Profile: `echo '{"tool_name":"Edit","tool_input":{"file_path":"x.py"}}' | time python3 hook.py`

Note:
- Talking points: Performance matters most for PreToolUse hooks — they block the tool call. PostToolUse runs after the fact and can afford more time.
- The sensitive-files guard is the easiest high-value hook to add — prevents `.env` and key files from being overwritten in one line.
- Stop hooks need stop_hook_active guard to avoid infinite loops.

---

## Theme 8: Parallel Development

```bash
# Each worktree = separate directory + own branch + own context window  — no git stash, no context bleed
git worktree add ../myapp-auth     -b feature/auth-refactor    main
git worktree add ../myapp-payments -b feature/payment-flow     main

cd ../myapp-auth     && claude   # Terminal 1
cd ../myapp-payments && claude   # Terminal 2

# Or use the -w shortcut
claude -w feature/email-verification   # creates worktree + opens session
```

Note:
- Worktrees share history but have independent file trees and context windows

---

## Task Decomposition First

| Task | Agent | Primary files | Never touches |
|------|-------|--------------|--------------|
| Auth system | Agent 1 | `src/auth/*` | `src/api/*` |
| API routes | Agent 2 | `src/routes/*` | `src/auth/*` |
| DB migrations | Agent 3 | `migrations/*` | `src/` |
| Test coverage | Agent 4 | `tests/` | `src/` (read only) |

Any file-level overlap = merge conflicts that cost more than sequential execution.

----

- 10-minute planning step replaces hours of conflict resolution — do before every parallel run
- Shared config files (`pyproject.toml`, root `__init__.py`) are the most common surprise conflicts
- Encode file ownership (in CLAUDE.md) so each agent knows its zone without prompting

Note:

---

## Subagents & Cost Control

```bash
# Explicit parallelisation prompt
Research these 5 packages using separate sub-agents:
- Sub-agent 1: httpx — async support, timeout handling
- Sub-agent 2: pydantic v2 — validation performance
...
Each produces /tmp/research/<package>.md.
Synthesize findings into /tmp/research/comparison-matrix.md.
```

----

```bash
# Use cheaper models for bounded subagent work
export CLAUDE_CODE_SUBAGENT_MODEL="claude-sonnet-4-6"

# Stagger starts to avoid 429 rate-limit errors
claude -w feature/auth &
sleep 30 && claude -w feature/payments &
sleep 30 && claude -w test/integration &
```

----

- Claude defaults to sequential — must explicitly request parallel with named scopes
- Max 2–4 parallel agents; 5+ triggers 429 errors that abort tasks mid-run
- Subagents cannot spawn subagents — coordinate through parent session or shared files

Note:

---

## Cross-Theme: The Composing Stack

```
CLAUDE.md         →  standing rules for every session
    ↓
Hooks             →  enforce those rules at execution time
    ↓
Commands/Skills   →  package best prompts as reusable ops
    ↓
MCP servers       →  connect those commands to external services
    ↓
Worktrees/agents  →  run the whole system in parallel
```

**Context window = the shared constraint all 8 themes orbit.**

Note:
- Engineers who treat these as independent features plateau at each level — wire them together to keep improving
- Automation unlocks the productivity ceiling prompting alone cannot reach. At the highest level, the proportion of tasks you direct manually shrinks; hooks, skills, and agents handle the rest.

---

## Top 5 Things to Try

1. **Write a real CLAUDE.md** — commands, hard rules, gotchas. Keep it under 80 lines.
2. **Add `@.claude/context-essentials.md`** + SessionStart hook with `matcher: "compact"`
3. **Create one skill** for your most-repeated prompt pattern
4. **Add a PostToolUse formatter hook** for your primary language
5. **Install the VS Code extension** + set `MAX_THINKING_TOKENS=10000`

Note:
- Talking points: Don't try to do everything at once. Start with CLAUDE.md — it's the highest single-variable ROI. Add hooks in week 2 after you know what Claude keeps getting wrong.
- The formatter hook alone eliminates a class of "Claude skipped the formatter" correction loops entirely.
- Revisit context-essentials.md every two weeks and prune it — only keep the rules Claude most often forgets.

---

## Additional Resources

- [Master guide](https://lochhh.github.io/claude-code-slides/): 82 sources synthesised
- [Ready-to-use Claude Code configurations](https://www.aitmpl.com/)
- [Claude Code best practices collection](https://github.com/shanraisshan/claude-code-best-practice)
- [Claude Code docs](https://code.claude.com/docs)
- `ccusage` — token spend monitoring
- [Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) + [GitHub](https://github.com/github/github-mcp-server) + [Context7](https://github.com/upstash/context7) MCP trio

Note:
- Talking points: The master guide at docs/ covers all 8 themes with full tip lists, code examples, pitfalls, and related themes cross-linking. Today was a survey — use the guide for depth.
- The references file lists all 82+ sources with links, grouped by theme.
- Q&A: common questions are usually about CLAUDE.md structure, hook exit codes, and when to use /compact vs /clear.
