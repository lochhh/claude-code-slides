# Parallel development (subagents + git worktrees)

[← Back to index](index.md)

Sequential AI-assisted development is an artificial bottleneck. Claude Code supports two orthogonal isolation mechanisms that, used together, turn a single-agent workflow into a genuine parallel team: [git worktrees](primitives.md#git-worktrees) provide filesystem isolation so multiple sessions never share a working directory, and [agents](primitives.md#agents) provide [context window](glossary.md#context-window) isolation so each task keeps its own reasoning thread clean. The combination lets you run three to five independent workstreams simultaneously — one agent refactoring auth, another building a payment flow, a third writing tests — each unaware of the others, merging back through standard git pull-request discipline. This theme covers the full workflow: worktree setup, task decomposition to prevent merge conflicts, subagent orchestration, environment isolation per worktree, and cost control.

**Level:** Expert

## Tips

### 1. Use `git worktree add` to create fully isolated parallel workspaces

Each [git worktree](glossary.md#git-worktree) is a separate directory sharing git history but with its own checked-out branch and working tree. Open one Claude session per worktree — each session has independent file state and its own context window. No `git stash`, no context bleed between tasks.[^1]

**Example:**

```bash
# Create two worktrees from main, each on its own feature branch
git worktree add ../myapp-auth -b feature/auth-refactor main
git worktree add ../myapp-payments -b feature/payment-flow main

# Open a Claude session in each — run in separate terminals
cd ../myapp-auth && claude
# (new terminal)
cd ../myapp-payments && claude

# When done, review, merge, and clean up
git merge feature/auth-refactor
git worktree remove ../myapp-auth
git branch -d feature/auth-refactor

# List all active worktrees at any time
git worktree list

# Prune stale references from deleted worktrees
git worktree prune
```

> **When to use:** Any time you have two or more independent features, bug fixes, or experiments to run in parallel. Use it even for solo work to keep context clean between unrelated tasks.
>
> **Pitfalls:** Two worktrees cannot check out the same branch simultaneously — git enforces this with a hard error. Each worktree also starts without your `node_modules`, virtualenv, or other generated artifacts; run your install step in each directory before expecting tests to pass. Old worktrees accumulate on disk — run `git worktree list` regularly and prune finished ones.

### 2. Plan task decomposition and file ownership before creating worktrees

The most expensive failure mode in parallel development is launching agents on tasks that touch the same files. Map [file ownership](glossary.md#file-ownership) before creating a single worktree. Any file-level overlap between tasks means merge conflicts that cost more time than sequential execution would have.[^2]

Build a decomposition table before you start:

| Task | Agent | Primary files | Dependencies | Integration point |
|------|-------|--------------|--------------|-------------------|
| Auth system | Agent 1 | `src/auth/*` | None | PR after completion |
| API routes | Agent 2 | `src/routes/*` | None | PR after completion |
| DB migrations | Agent 3 | `migrations/*` | None | Sequential merge |
| Frontend forms | Agent 4 | `src/components/forms/*` | Auth system | After Agent 1 merges |

**Example:**

```python
# scripts/plan_worktrees.py — print a file-ownership map from your task list
import sys

tasks = [
    {"name": "auth-refactor",  "files": ["src/auth/", "src/middleware/auth.py"]},
    {"name": "payment-flow",   "files": ["src/payments/", "src/api/payments.py"]},
    {"name": "test-coverage",  "files": ["tests/unit/", "tests/integration/"]},
]

# Detect overlaps before creating worktrees
all_paths = []
for task in tasks:
    for path in task["files"]:
        for other in tasks:
            if other["name"] == task["name"]:
                continue
            if any(path.startswith(p) or p.startswith(path) for p in other["files"]):
                print(f"CONFLICT: {task['name']} and {other['name']} both touch {path}")
                sys.exit(1)
        all_paths.append((path, task["name"]))

for path, owner in sorted(all_paths):
    print(f"{owner:<20} {path}")
```

> **When to use:** Before every parallel run, without exception. This 10-minute planning step replaces hours of conflict resolution.
>
> **Pitfalls:** Shared config files (`pyproject.toml`, root `__init__.py`, shared type stubs) are the most common source of surprise conflicts. Either make them read-only for parallel agents or coordinate their modification sequentially.

### 3. Be explicit about parallelisation in prompts to subagents

Claude defaults to sequential execution unless you explicitly request parallel. Name each [subagent](glossary.md#subagent)'s scope, specify the number of agents, and ask for synthesis at the end. Vague delegation produces vague decomposition.[^3]

**Example:**

```
Research these 5 Python packages in parallel using separate sub-agents:
- Sub-agent 1: httpx — async support, connection pooling, timeout handling
- Sub-agent 2: pydantic v2 — validation performance, migration from v1
- Sub-agent 3: sqlalchemy 2.0 — async ORM patterns, session management
- Sub-agent 4: fastapi — dependency injection, lifespan events
- Sub-agent 5: celery — task routing, result backends, beat scheduler

Each sub-agent should produce a structured markdown report in /tmp/research/<package>.md.
Once all five complete, synthesize findings into /tmp/research/comparison-matrix.md
with columns: async_support, performance_notes, migration_complexity, recommended_use_case.
```

> **When to use:** Any research, codebase analysis, batch document generation, or multi-module refactor where tasks are genuinely independent.
>
> **Pitfalls:** Subagents cannot spawn other subagents (no nesting). They also cannot communicate directly — they coordinate only through the parent session or shared files. Keep each subagent's scope self-contained: tasks that need the output of another agent must be sequenced, not parallelised.

### 4. Isolate databases and port ranges per worktree

Dev servers collide when they share ports. Databases corrupt each other's schemas when agents run migrations against the same instance simultaneously. Assign a [port-offset](glossary.md#port-offset) convention per worktree and use separate database names.[^4]

Use a Python script to generate per-worktree `.env` files rather than editing them by hand:

**Example:**

```python
# scripts/setup_worktree_env.py
"""Generate a .env file for a named worktree with non-conflicting ports and DB name."""
import argparse
import pathlib
import shutil

# Port-offset convention: each worktree slot gets a block of 10 ports
WORKTREE_SLOTS = {
    "main":     0,
    "auth":     1,
    "payments": 2,
    "testing":  3,
}

BASE_PORT = 3000
BASE_DB_NAME = "myapp"

def generate_env(worktree_name: str, source_env: pathlib.Path) -> None:
    slot = WORKTREE_SLOTS.get(worktree_name)
    if slot is None:
        raise ValueError(f"Unknown worktree '{worktree_name}'. Add it to WORKTREE_SLOTS.")

    offset = slot * 10
    env_vars = {
        "PORT":         str(BASE_PORT + offset),
        "API_PORT":     str(BASE_PORT + offset + 1),
        "DATABASE_URL": f"postgresql://localhost:5432/{BASE_DB_NAME}_{worktree_name}_dev",
    }

    # Read existing .env, override relevant keys
    lines = source_env.read_text().splitlines()
    result = []
    overridden = set()
    for line in lines:
        key = line.split("=", 1)[0].strip()
        if key in env_vars:
            result.append(f"{key}={env_vars[key]}")
            overridden.add(key)
        else:
            result.append(line)
    for key, val in env_vars.items():
        if key not in overridden:
            result.append(f"{key}={val}")

    output_path = source_env.parent.parent / f"myapp-{worktree_name}" / ".env"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(result) + "\n")
    print(f"Written: {output_path}")
    print(f"  PORT={env_vars['PORT']}, API_PORT={env_vars['API_PORT']}")
    print(f"  DATABASE_URL={env_vars['DATABASE_URL']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("worktree_name", choices=list(WORKTREE_SLOTS.keys()))
    parser.add_argument("--source-env", default=".env", type=pathlib.Path)
    args = parser.parse_args()
    generate_env(args.worktree_name, args.source_env)
```

```bash
# Usage: generate .env for the auth and payments worktrees
python scripts/setup_worktree_env.py auth
python scripts/setup_worktree_env.py payments

# Create each PostgreSQL database before running migrations
psql -c "CREATE DATABASE myapp_auth_dev;"
psql -c "CREATE DATABASE myapp_payments_dev;"
```

> **When to use:** Every time you create a new worktree for a project that runs a dev server or uses a local database.
>
> **Pitfalls:** Do not symlink `.env` across worktrees — if one agent modifies it, the change propagates to all others unexpectedly. Copy or generate separate files. Verify `echo $DATABASE_URL` before running migrations to confirm you are targeting the right database.

### 5. Use the `-w` flag to create a worktree automatically from Claude Code

`claude -w <branch-name>` (or `claude --worktree <branch-name>`) creates the worktree, checks out the branch, and opens a Claude session scoped to that directory — one command instead of three.[^5]

**Example:**

```bash
# Terminal 1: feature work
claude -w feature/email-verification

# Terminal 2: bug fix running in parallel
claude -w bugfix/pagination-race

# Terminal 3: test coverage running in parallel
claude -w test/checkout-integration

# Claude places worktrees at .claude/worktrees/<branch-name>/ inside your repo.
# Add this path to .gitignore so they don't appear as untracked files:
echo ".claude/worktrees/" >> .gitignore
```

When you exit a session started with `-w`, Claude prompts you to keep or remove the worktree. Keep it if you plan to resume; remove it once the branch is merged.

> **When to use:** Prefer `-w` over manual `git worktree add` for any single-feature task where you want branch-per-task discipline enforced automatically.
>
> **Pitfalls:** The `-w` flag names the branch based on your argument, so use the same branch-naming convention your team uses. If the branch already exists remotely, pass the full branch name and Claude will check it out rather than create a new one.

### 6. Assign directory ownership to prevent merge conflicts in agent teams

At team level, encode [file ownership](glossary.md#file-ownership) directly in [CLAUDE.md](primitives.md#claude-md) so each agent knows its zone without prompting. No agent touches files outside its assigned directories. This eliminates the most common source of parallel conflicts before they happen.[^6]

**Example:**

```markdown
# CLAUDE.md (root of repo)

## Agent file ownership

These boundaries are enforced for all parallel agent sessions. Do not
read or write files outside your assigned directories without an explicit
handoff instruction from the orchestrator.

| Agent role     | Owns                                    | Never touches                     |
|----------------|-----------------------------------------|-----------------------------------|
| Frontend agent | src/components/, src/pages/, src/styles/ | src/api/, src/services/, migrations/ |
| Backend agent  | src/api/, src/services/, src/models/    | src/components/, src/pages/       |
| Test agent     | tests/, src/__tests__/                  | src/ (except reading for context) |
| DB agent       | migrations/, prisma/schema.prisma       | src/                              |

Shared files (pyproject.toml, src/types/, root config): coordinate with
orchestrator before modifying. These must be handled sequentially.
```

> **When to use:** Any project where multiple Claude sessions will be running simultaneously, including solo workflows with multiple worktrees. Establish this at project initialisation, not after the first conflict.
>
> **Pitfalls:** Shared type definitions, root configuration files, and shared utility modules are the most common boundary violations. List these explicitly as "coordinate before modifying" rather than assigning them to any single agent.

### 7. Define specialist agents in `.claude/agents/` for recurring patterns

Create persistent specialist agents as Markdown files with YAML frontmatter in `.claude/agents/`. These agents are available to the [orchestrator](glossary.md#orchestrator) automatically in every session, eliminating the need to retype role prompts for recurring parallel patterns.[^7]

**Example:**

```markdown
<!-- .claude/agents/security-reviewer.md -->
---
name: security-reviewer
description: Reviews Python code for security vulnerabilities and dependency risks
tools: ["read_file", "search_files", "bash"]
---

You are a security-focused code reviewer specialising in Python web applications.

When invoked, you:
1. Scan all modified files in your assigned directory for: SQL injection, unsafe
   deserialization, hardcoded secrets, insecure random usage, and missing input validation.
2. Check requirements.txt or pyproject.toml for known-vulnerable dependency versions
   using `pip-audit` if available.
3. Output findings as a structured markdown report with severity (critical/high/medium/low),
   affected file, line number, and remediation steps.
4. Do NOT modify any files — report only.
```

```markdown
<!-- .claude/agents/test-writer.md -->
---
name: test-writer
description: Writes pytest unit and integration tests for Python modules
tools: ["read_file", "write_file", "bash"]
---

You write pytest tests following the project's testing conventions in CLAUDE.md.
Focus only on the files listed in your task. Aim for 80%+ branch coverage.
Run `pytest --tb=short` to verify tests pass before reporting completion.
```

```bash
# Project agents live in the repo (shared with team)
ls .claude/agents/
# security-reviewer.md  test-writer.md  doc-generator.md

# User agents work across all your projects
ls ~/.claude/agents/
# python-profiler.md  dependency-auditor.md
```

> **When to use:** Any workflow you run more than twice. Common candidates: security review, test generation, documentation generation, dependency auditing, and code style enforcement.
>
> **Pitfalls:** Agents defined in `.claude/agents/` inherit the project's CLAUDE.md context automatically — do not duplicate conventions in the agent file itself. User agents in `~/.claude/agents/` do not have project context by default; keep them general-purpose.

### 8. Add routing rules to CLAUDE.md for orchestration decisions

Without explicit rules, the [orchestrator](glossary.md#orchestrator) defaults to conservative sequential execution. Document when to use parallel vs. sequential vs. background dispatch in [CLAUDE.md](primitives.md#claude-md) so the orchestrating session makes smarter delegation decisions automatically.[^8]

**Example:**

```markdown
# CLAUDE.md

## Sub-agent routing rules

### Parallel dispatch (ALL conditions must be met)
- 3 or more unrelated tasks with no shared state
- Clear file boundaries with zero overlap between tasks
- Each task is self-contained and produces a discrete deliverable

### Sequential dispatch (ANY condition triggers sequential)
- Task B requires output from Task A (dependency)
- Tasks share mutable files or database schema
- Scope is unclear — understand before executing

### Background dispatch
- Research, documentation lookups, codebase analysis
- Security audits, performance profiling, linting runs
- Results are not blocking the current implementation task

### Concurrency limit
- Maximum 4 parallel sub-agents on standard API tier
- If hitting 429 errors, reduce to 2 and add a 30-second stagger between spawns
```

> **When to use:** Add this section when your project regularly spawns subagents — typically once a project exceeds two or three concurrent development threads.
>
> **Pitfalls:** Without the concurrency limit note, Claude may spawn more agents than your API tier supports, causing 429 rate-limit errors mid-task. Explicitly document the limit rather than discovering it at runtime.

### 9. Set `CLAUDE_CODE_SUBAGENT_MODEL` to use cheaper models for subagents

[CLAUDE_CODE_SUBAGENT_MODEL](glossary.md#claude-code-subagent-model) controls which model subagents run on, independently of the orchestrating session. Run the orchestrator on Opus for complex reasoning and dispatch subagents on Sonnet for focused, well-scoped execution tasks. This cuts parallel-run costs significantly without sacrificing output quality on bounded subagent work.[^9]

**Example:**

```bash
# Set in your shell profile or project .env (not committed to git)
export CLAUDE_CODE_SUBAGENT_MODEL="claude-sonnet-4-6"

# Verify it's picked up before a long parallel run
echo $CLAUDE_CODE_SUBAGENT_MODEL

# Or set it inline for a single session
CLAUDE_CODE_SUBAGENT_MODEL="claude-sonnet-4-6" claude
```

For Python projects, set it in your development environment activation script:

```python
# scripts/activate_dev_env.py — run with: eval $(python scripts/activate_dev_env.py)
import os

env_vars = {
    "CLAUDE_CODE_SUBAGENT_MODEL": "claude-sonnet-4-6",
    # Add other project-specific env vars here
}

for key, val in env_vars.items():
    print(f"export {key}={val}")
```

> **When to use:** Any session that will spawn three or more subagents. The cost difference between Opus and Sonnet at scale is substantial — parallel agents burn through tokens at multiplied rates, so the model choice compounds.
>
> **Pitfalls:** Do not set this variable for subagents that require complex architectural reasoning or multi-step synthesis. Use it for focused, well-defined tasks (test generation, documentation, security scanning) where Sonnet is genuinely sufficient.

### 10. Keep parallel agent count to 2–4 unless you have higher-tier API access

Standard Claude API tiers rate-limit concurrent requests. Running more than four simultaneous sessions triggers 429 errors that abort tasks mid-run and leave worktrees in a partially modified state. Start at two or three parallel agents and scale up only after confirming your tier supports it.[^10]

**Example:**

```bash
# Recommended: stagger session starts by 30 seconds to reduce burst pressure
claude -w feature/auth &
sleep 30
claude -w feature/payments &
sleep 30
claude -w test/integration &

# Monitor for rate-limit errors in each session
# If you see 429s, kill one session and reduce concurrency:
# kill %3  # terminates the third background job
```

For tmux-based parallel management:

```bash
# Create named sessions for each worktree
tmux new-session -d -s auth     -c ../myapp-auth
tmux new-session -d -s payments -c ../myapp-payments
tmux new-session -d -s tests    -c ../myapp-tests

# View all sessions at a glance
tmux list-sessions

# Attach to any session by name
tmux attach -t auth
```

> **When to use:** Always check your plan's concurrent request limits before designing a parallel workflow that depends on a specific agent count.
>
> **Pitfalls:** Parallel agents consume tokens in parallel — a four-agent run uses roughly four times the tokens of a sequential run of the same tasks. Calculate the cost-versus-speed tradeoff before running large parallel jobs on API billing. Use `CLAUDE_CODE_SUBAGENT_MODEL` (tip 9) to reduce per-agent cost.

## Related themes

- [CLAUDE.md & project memory](claudemd-setup.md) — agent routing rules and file ownership declarations belong in CLAUDE.md, making them available to every session automatically
- [Context management](context-management.md) — each worktree gets its own context window; filesystem isolation eliminates cross-task compaction pressure and prevents one agent's token usage from affecting another's
- [Hooks & automation](hooks-automation.md) — hooks can enforce per-worktree environment setup (copying `.env`, running `uv sync`, setting `CLAUDE_CODE_SUBAGENT_MODEL`) automatically on session start

---

[^1]: [How to use git worktrees with Claude Code for parallel development](references.md#git-worktrees-claude-code-parallel-development)
[^2]: [Parallel agentic development with git worktrees: a practical playbook](references.md#parallel-agentic-development-git-worktrees)
[^3]: [How to use Claude Code sub-agents for parallel work](references.md#claude-code-parallel-subagents)
[^4]: [Mastering git worktrees with Claude Code for parallel development workflow](references.md#mastering-git-worktrees-with-claude-code-for-parallel-develo)
[^5]: [Parallel vibe coding: using git worktrees with Claude Code](references.md#parallel-vibe-coding-with-git-worktrees)
[^6]: [Claude Code agent teams: how to run multiple AI agents in parallel](references.md#claude-code-agent-teams-parallel-workflows)
[^7]: [Claude Code sub-agents: parallel vs sequential patterns](references.md#sub-agent-best-practices)
[^8]: [Claude Code sub-agents: parallel vs sequential patterns](references.md#sub-agent-best-practices)
[^9]: [How Claude Code parallel agents coordinate through an orchestrator](references.md#claude-code-agent-teams-parallel-agents)
[^10]: [How Claude Code parallel agents coordinate through an orchestrator](references.md#claude-code-agent-teams-parallel-agents)
