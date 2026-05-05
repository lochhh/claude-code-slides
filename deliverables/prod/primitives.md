# Claude Code primitives

[← Back to index](index.md)

> Start here. These are the building blocks everything else builds on.

---

<!-- Basic -->

<a id="claude-md"></a>
## CLAUDE.md

**What it is:** A markdown file placed at your project root (and optionally in sub-packages) that Claude reads at the start of every session.

**Why it matters:** It is the primary lever against context rot — the session-to-session amnesia that causes Claude to reintroduce banned patterns, forget build commands, and ignore architectural decisions you already made.

**Example:**
````markdown
# CLAUDE.md

## Build & test
```bash
uv run python -m pytest tests/ -x --tb=short
uv run python -m pytest tests/test_auth.py -x   # auth module only
```

## Never do
- Never use `pip install` — always `uv add` or `uv sync`
- Never modify `src/auth/` without explicit confirmation
- Never throw exceptions — always return `Result[T, E]`

## Known footguns
- The legacy endpoint `/api/v1` is frozen; all new work goes to `/api/v2`
- `User.created_at` is stored as UTC but the ORM returns local time; convert on read

## Architecture
See `docs/architecture.md` for full system design.
````

> **Usage level:** Basic

---

<a id="tool-use"></a>
## Tool use

**What it is:** The mechanism by which Claude calls shell commands, reads and writes files, runs bash scripts, and invokes MCP tools — all controlled by the permissions layer.

**Why it matters:** Understanding which tools Claude can call (and which are blocked) lets you tune the permission model instead of being surprised by what Claude does or refuses to do.

**Example:**
```bash
# Claude invokes these tools internally; you observe them in the session trace:
# Bash("pytest tests/ -x")
# Read("src/services/payment.py")
# Write("src/services/payment.py", <new content>)
# WebSearch("FastAPI dependency injection docs")

# To see which tools are available in the current session:
/tools
```

> **Usage level:** Basic

---

<a id="project-structure"></a>
## Project structure

**What it is:** The layout of files Claude navigates when it explores your repository — including where it looks for CLAUDE.md files, `.claude/` directories, and MCP configs.

**Why it matters:** Knowing the load order means you can place instructions, commands, and settings exactly where they take effect — per-project, per-package in a monorepo, or globally.

**Example:**
```
my-project/
├── CLAUDE.md                      # root: shared conventions
├── .claude/
│   ├── settings.json              # team hooks & tool permissions (commit this)
│   ├── settings.local.json        # personal overrides (gitignore this)
│   ├── commands/                  # custom slash commands
│   │   ├── review-auth.md
│   │   └── fix-issue.md
│   ├── agents/                    # reusable subagent specs
│   │   └── security-reviewer.md
│   └── context-essentials.md     # critical rules for post-compaction re-injection
├── packages/
│   ├── auth/
│   │   └── CLAUDE.md              # auth-specific rules (JWT patterns, security)
│   └── payments/
│       └── CLAUDE.md              # payments-specific rules
└── .mcp.json                      # project MCP server config (commit this)
```

> **Usage level:** Basic

---

<a id="permissions-and-settings"></a>
## Permissions & settings

**What it is:** A three-tier settings hierarchy (`~/.claude/settings.json` → `.claude/settings.json` → `.claude/settings.local.json`) that controls which tools Claude can call, which paths it can write to, and how hooks are configured.

**Why it matters:** The hierarchy means you can share safe defaults with your team via a committed project-level file while letting individuals override locally — without fighting over a single global config.

**Example:**
```json
// .claude/settings.json  (committed — shared team defaults)
{
  "permissions": {
    "allow": [
      "Bash(git:*)",
      "Bash(pytest:*)",
      "Bash(uv:*)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Write(**/.env)"
    ]
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python tools/format_on_save.py"
          }
        ]
      }
    ]
  }
}
```

```json
// .claude/settings.local.json  (gitignored — personal override)
{
  "model": "claude-opus-4-5"
}
```

> **Usage level:** Basic

---

<a id="context-model"></a>
## Context model

**What it is:** Claude's fixed-size token window that holds the entire conversation history — every prompt, response, file read, and tool result — until you compact or clear it.

**Why it matters:** The window is finite and performance degrades before the hard limit. Engineers who treat it as a managed resource (rather than an infinite buffer) maintain quality across arbitrarily long sessions.

**Example:**
```bash
# Check current context utilisation inside a session:
/status

# The output shows something like:
# Context: 58% (116k / 200k tokens)

# Rule of thumb: compact at ~60% — before the 80% warning appears.
# At 80%+ the oldest, most foundational context is already compressed.
/compact "Keep: decision to use PostgreSQL, the three functions earmarked for refactor, current error in auth.py. Clear: grep output, full file reads."
```

> **Usage level:** Basic

---

<!-- Novice -->

<a id="context-compaction"></a>
## Context compaction

**What it is:** The `/compact` slash command that replaces the full conversation transcript with a Claude-generated summary, freeing space for continued work in the same session.

**Why it matters:** Compaction is lossy by design — what survives the summary depends on what you tell Claude to preserve. Engineers who append explicit preservation instructions get clean continuations; those who run `/compact` alone often lose architectural decisions.

**Example:**
```bash
# Bare compact — Claude decides what survives (risky):
/compact

# Guided compact — you control the signal:
/compact Keep: (1) decision to use Redis for rate limiting and why we ruled out in-memory, (2) the three endpoints identified as bottlenecks, (3) current failing test in test_api.py line 142. Clear: full file reads (can be re-fetched), grep output (can be re-run).

# After compacting, verify state immediately:
# "Summarise where we are and what we're working on next."
```

> **Usage level:** Novice

---

<a id="memory"></a>
## Memory

**What it is:** Persistent notes written to files or external storage that outlive session clears and compaction boundaries — distinct from in-context history.

**Why it matters:** A `/clear` or new session wipes all in-context history; memory files do not. They are the bridge between sessions for decisions, discoveries, and constraints that must survive.

**Example:**
```python
# Claude can write session findings to a memory file on request:
# "Save the following to notes/session-decisions.md: [decisions]"

# Or automate it via a Stop hook in settings.json:
# {
#   "hooks": {
#     "Stop": [{
#       "type": "command",
#       "command": "python tools/append_session_summary.py"
#     }]
#   }
# }

# tools/append_session_summary.py
import sys, json, pathlib, datetime

data = json.load(sys.stdin)
summary = data.get("result", "")
path = pathlib.Path("notes/session-log.md")
path.parent.mkdir(exist_ok=True)
with path.open("a") as f:
    f.write(f"\n## {datetime.date.today()}\n{summary}\n")
```

> **Usage level:** Novice

---

<a id="slash-commands-and-skills"></a>
## Slash commands & skills

**What it is:** Custom `/command-name` shortcuts defined as markdown files in `.claude/commands/` (manual invocation) and skills with optional auto-invocation triggers — both live in version control and are shareable with the team.

**Why it matters:** Every repeated prompt pattern is a candidate for a command. Codifying it means consistent execution, team-wide reuse, and the ability to add constraints (allowed tools, context isolation) that ad-hoc prompts cannot express.

**Example:**
```markdown
<!-- .claude/commands/fix-issue.md -->
---
description: Fix a GitHub issue following project error-handling conventions
allowed-tools: Read, Edit, Write, Bash
---

Fix GitHub issue #$ARGUMENTS following these constraints:
- Read the relevant source files before writing any code
- Use the `Result[T, E]` pattern — never raise exceptions
- Write or update the corresponding test in `tests/`
- Run `uv run python -m pytest tests/ -x` and confirm it passes before finishing
```

```bash
# Invoke it:
/fix-issue 247
```

> **Usage level:** Novice

---

<a id="plan-mode"></a>
## Plan mode

**What it is:** A session mode where Claude researches and proposes changes without executing them — toggled by pressing Shift+Tab twice from the default mode.

**Why it matters:** High-risk or multi-file changes deserve review before they land. Plan mode lets you inspect the full change set, request adjustments, and only then approve execution — separating intent from impact.

**Example:**
```bash
# Cycle modes with Shift+Tab:
# default → acceptEdits → plan → default → ...

# Practical pattern for risky refactors:
# 1. Press Shift+Tab twice to enter plan mode
# 2. Prompt: "Refactor the payment module to use the new Stripe SDK. Show me every file you'll touch and what changes you'll make."
# 3. Review the proposed plan in the output
# 4. Request adjustments: "Don't touch payments/legacy.py — that file is frozen."
# 5. Press Shift+Tab once to switch to acceptEdits, then approve

# In headless / CI mode, set via flag:
claude --mode plan "Audit all SQL queries for injection risks and report findings"
```

> **Usage level:** Novice

---

<!-- Intermediate -->

<a id="agents"></a>
## Agents

**What it is:** Subagent instances of Claude spawned by an orchestrating session, each with its own isolated context window, that can run in parallel across independent tasks.

**Why it matters:** Subagents unlock throughput that sequential sessions cannot achieve — ten independent tasks that each take 5 minutes finish in 5 minutes total rather than 50. The isolation also means one subagent's context pollution does not affect the others.

**Example:**
```bash
# Ask the orchestrating session to spawn parallel subagents:
# "Research these five Python async patterns in parallel using separate sub-agents.
#  Each agent should: (1) read the relevant stdlib docs, (2) write a 50-line example
#  to examples/<pattern-name>.py, (3) note any Python version constraints.
#  Once all five complete, synthesise findings into docs/async-patterns.md."

# Control the model used by subagents (save cost vs. orchestrator):
export CLAUDE_CODE_SUBAGENT_MODEL="claude-sonnet-4-6"

# Define reusable specialist agents in .claude/agents/:
# .claude/agents/security-reviewer.md
# .claude/agents/test-writer.md
```

```markdown
<!-- .claude/agents/test-writer.md -->
---
description: Writes pytest tests for a given Python module
allowed-tools: Read, Write, Bash
---
Given a Python module path, read the source, identify all public functions and
classes, and write comprehensive pytest tests to `tests/test_<module>.py`.
Run the tests and fix any failures before finishing.
```

> **Usage level:** Intermediate

---

<a id="hooks"></a>
## Hooks

**What it is:** Shell scripts (or Python scripts) triggered by Claude Code lifecycle events — `PreToolUse`, `PostToolUse`, `Stop`, `SessionStart`, `Notification`, `UserPromptSubmit` — configured in `settings.json`.

**Why it matters:** Hooks are deterministic code running outside the LLM. They enforce rules Claude cannot reliably self-enforce: auto-formatting after every edit, blocking writes to sensitive files, re-injecting context after compaction, running tests before Claude moves on.

**Example:**
```json
// .claude/settings.json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python tools/post_edit_hook.py"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python tools/block_dangerous_commands.py"
          }
        ]
      }
    ]
  }
}
```

```python
# tools/post_edit_hook.py — auto-format and run corresponding test
import sys, json, subprocess, pathlib

data = json.load(sys.stdin)
file_path = data.get("tool_input", {}).get("file_path", "")

if file_path.endswith(".py"):
    subprocess.run(["uv", "run", "ruff", "format", file_path])
    test_file = pathlib.Path("tests") / f"test_{pathlib.Path(file_path).name}"
    if test_file.exists():
        result = subprocess.run(
            ["uv", "run", "python", "-m", "pytest", str(test_file), "-x", "--tb=short"],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(result.stdout + result.stderr)
            sys.exit(1)   # exit 1 warns; exit 2 blocks the tool call
```

> **Usage level:** Intermediate

---

<a id="mcp-servers"></a>
## MCP servers

**What it is:** External servers that implement the Model Context Protocol, exposing additional tools (GitHub, databases, browsers, internal APIs) to Claude's tool palette without modifying Claude Code itself.

**Why it matters:** The right 2–3 MCP servers eliminate the context switches that break flow — Claude can read a GitHub issue, query your database, and interact with the browser without you switching tabs.

**Example:**
```bash
# Add a user-scoped MCP server (persists across projects):
claude mcp add sequential-thinking -s user -- \
  npx -y @modelcontextprotocol/server-sequential-thinking

# Add a project-scoped server (shared via .mcp.json):
claude mcp add github -s project -- \
  npx -y @modelcontextprotocol/server-github
```

```json
// .mcp.json  (commit this — team shares the same MCPs)
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "${POSTGRES_READONLY_URL}"
      },
      "lazy": true
    }
  }
}
```

```bash
# Inspect running servers and their tools:
/mcp

# Debug a failed connection:
# /mcp shows auth failures, missing packages, and tool availability
```

> **Usage level:** Intermediate

---

<!-- Advanced -->

<a id="plugins"></a>
## Plugins

**What it is:** User-installable extensions that bundle their own hooks, slash commands, and MCP server configurations into a single installable package — distributed and versioned independently of Claude Code itself.

**Why it matters:** Plugins let teams distribute a standardised Claude Code environment (linting rules, project-specific commands, safety hooks) as a single install rather than a manual checklist of settings to copy.

**Example:**
```bash
# Install a plugin from a registry or local path:
claude plugin install @my-org/python-standards

# A plugin package typically contains:
# plugin.json          — manifest declaring hooks, commands, and MCPs
# commands/            — slash command markdown files
# hooks/               — hook scripts
# mcp-servers/         — bundled MCP server configs

# Example plugin.json manifest:
```

```json
{
  "name": "@my-org/python-standards",
  "version": "1.2.0",
  "description": "Enforces project Python standards: ruff, mypy, Result types",
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "hooks/format_and_typecheck.py"
      }
    ]
  },
  "commands": ["commands/fix-issue.md", "commands/review-pr.md"]
}
```

> **Usage level:** Advanced

---

<a id="git-worktrees"></a>
## Git worktrees

**What it is:** A git feature (`git worktree add`) that creates additional working directories sharing the same repository history but with independent working trees — one Claude session per worktree, each with isolated context and filesystem state.

**Why it matters:** Worktrees provide the filesystem isolation that subagents alone cannot: each Claude session works in its own directory, so parallel feature branches never collide on file writes, dev server ports, or database state.

**Example:**
```bash
# Create a worktree for a parallel feature branch:
git worktree add ../my-project-auth -b feature/auth-refactor main
cd ../my-project-auth
claude   # opens a fresh Claude session with isolated context

# Or use Claude's built-in worktree flag (creates worktree + opens session):
claude -w feature/payments-v2

# Recommended directory layout for parallel worktrees:
# ~/projects/my-project/           (main — port 8000, db: myapp_main)
# ~/projects/my-project-auth/      (auth branch — port 8001, db: myapp_auth)
# ~/projects/my-project-payments/  (payments branch — port 8002, db: myapp_payments)

# Configure per-worktree environment in .env:
```

```python
# tools/worktree_env.py — generate per-worktree .env based on directory name
import pathlib, hashlib, os

branch = pathlib.Path.cwd().name          # e.g. "my-project-auth"
port_offset = int(hashlib.md5(branch.encode()).hexdigest(), 16) % 900 + 8100
db_name = branch.replace("-", "_")

env_content = f"""
PORT={port_offset}
DATABASE_URL=postgresql://localhost:5432/{db_name}
REDIS_URL=redis://localhost:6379/{port_offset % 16}
""".strip()

pathlib.Path(".env").write_text(env_content)
print(f"Configured: PORT={port_offset}, DB={db_name}")
```

```bash
# Clean up a finished worktree:
git worktree remove ../my-project-auth
git branch -d feature/auth-refactor
```

> **Usage level:** Advanced

---

*Part of the [Claude Code master guide](index.md)*
