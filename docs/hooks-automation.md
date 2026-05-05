# Hooks & automation

[← Back to index](index.md)

[Hooks](primitives.md#hooks) transform Claude Code from a probabilistic assistant into an enforceable, repeatable workflow. They execute deterministic shell commands — or Python scripts — at 25+ lifecycle points outside the LLM, which means they run every time, regardless of prompt phrasing or model mood. If you have ever written "always run black after editing Python files" in a [CLAUDE.md](primitives.md#claudemd) and watched Claude skip it anyway, hooks are the fix: they are the most underused power feature in Claude Code, and the one with the highest ceiling for intermediate-to-advanced engineers.

**Level:** Advanced

## Tips

### 1. Configure hooks at three scope levels: global, project-shared, and local-override

Separate personal preferences from team policies from machine-specific overrides. This mirrors the same layered settings model used for [permissions and settings](primitives.md#permissions-and-settings).

- `~/.claude/settings.json` — personal defaults, applies to every project on your machine
- `.claude/settings.json` — project-shared, commit this to the repo so the whole team gets the same hooks
- `.claude/settings.local.json` — local overrides, add to `.gitignore`[^1]

**Example — `.claude/settings.json` (committed, shared with team):**

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'if [[ \"$FILE_PATH\" == *.py ]]; then uv run black --quiet \"$FILE_PATH\" 2>/dev/null; fi'"
          }
        ]
      }
    ]
  }
}
```

Personal `~/.claude/settings.json` can override the model preference or add machine-specific notification commands without touching the shared file.[^2]

> **When to use:** Any team project. Commit `.claude/settings.json` from day one so hooks are not an afterthought.
>
> **Pitfalls:** Putting secrets or absolute machine paths in the committed file. Use `$CLAUDE_PROJECT_DIR` for project-relative paths and `~/.claude/settings.local.json` for anything personal.

---

### 2. Use [exit code 2](glossary.md#exit-code-2) to block execution — exit code 1 only warns

This is the single most dangerous misconception about hooks. Many teams believe they have blocked force-pushes or dangerous commands, only to discover that their hook used `exit 1` and the command executed anyway.[^3]

| Exit code | Effect on `PreToolUse` |
|-----------|------------------------|
| `0` | Allow the tool to proceed |
| `1` | Non-blocking error — operation still runs, stderr shown to user |
| `2` | **Block** — operation cancelled, stderr is sent to Claude as feedback |

**Example — blocking `git push --force` to main:**

```python
#!/usr/bin/env python3
# .claude/hooks/guard_git.py
import json
import sys
import re

data = json.load(sys.stdin)
cmd = data.get("tool_input", {}).get("command", "")

dangerous = [
    r"git\s+push\s+(-f|--force)(\s+origin)?\s+main",
    r"git\s+reset\s+--hard",
    r"rm\s+-rf\s+/",
    r"DROP\s+(TABLE|DATABASE)",
]

for pattern in dangerous:
    if re.search(pattern, cmd, re.IGNORECASE):
        print(f"BLOCKED: dangerous command detected: {cmd}", file=sys.stderr)
        sys.exit(2)

sys.exit(0)
```

Register it in `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{ "type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/guard_git.py" }]
      }
    ]
  }
}
```

> **When to use:** Any safety-critical gate. If you want it blocked, you must use `exit 2`.
>
> **Pitfalls:** Testing with `exit 1` during development and shipping it. Always verify a security hook actually prevented the action by triggering the blocked pattern and checking the tool did not run.

---

### 3. Use [jq](glossary.md#jq) (or Python's `json` module) to parse hook stdin and apply conditional logic

Every hook receives a JSON payload on stdin containing the event name, tool name, and tool arguments. Parsing it lets you apply per-file or per-command logic rather than blanket rules.[^4]

The Python approach is preferable for Python-centric projects: no extra dependency (`jq` may not be installed on all machines), cleaner conditionals, and easier to unit-test.

**Example — Python formatter hook that dispatches by file extension:**

```python
#!/usr/bin/env python3
# .claude/hooks/format_on_edit.py
import json
import subprocess
import sys

data = json.load(sys.stdin)
file_path = data.get("tool_input", {}).get("file_path", "")

if not file_path:
    sys.exit(0)

if file_path.endswith(".py"):
    subprocess.run(["uv", "run", "ruff", "format", "--quiet", file_path], check=False)
elif file_path.endswith((".js", ".ts", ".jsx", ".tsx")):
    subprocess.run(["npx", "prettier", "--write", file_path], capture_output=True)

sys.exit(0)
```

**Equivalent using `jq` in a one-liner (bash):**

```bash
FILE=$(cat | jq -r '.tool_input.file_path // empty') \
  && [ -n "$FILE" ] && [[ "$FILE" == *.py ]] \
  && uv run ruff format --quiet "$FILE" 2>/dev/null || true
```

> **When to use:** Any hook that needs to branch on file type, command content, or tool name. This covers most real-world hooks.
>
> **Pitfalls:** Forgetting the `// empty` fallback in `jq` — without it, `jq` outputs the string `"null"` when the field is absent, which evaluates as truthy in bash conditionals. In Python, `.get()` defaults to `""` safely.

---

### 4. Catch regressions immediately with [PostToolUse](glossary.md#posttooluse) test-runner hooks

Run the test file corresponding to the edited source file after every write. This stops regressions from compounding: Claude edits file A, breaking file B's tests, then proceeds to edit file C based on the already-broken state. With per-file test execution, the first failure surfaces immediately.[^5]

**Example — Python test runner for a `tests/test_<module>.py` layout:**

```python
#!/usr/bin/env python3
# .claude/hooks/run_tests_on_edit.py
import json
import os
import subprocess
import sys

data = json.load(sys.stdin)
file_path = data.get("tool_input", {}).get("file_path", "")

# Only trigger for Python source files (not test files themselves)
if not file_path.endswith(".py") or "test_" in os.path.basename(file_path):
    sys.exit(0)

test_file = os.path.join("tests", f"test_{os.path.basename(file_path)}")
if not os.path.isfile(test_file):
    sys.exit(0)

result = subprocess.run(
    ["uv", "run", "pytest", test_file, "-x", "--tb=short", "-q"],
    capture_output=True,
    text=True,
)
# Print output so it appears in Claude's transcript
print(result.stdout[-3000:] if len(result.stdout) > 3000 else result.stdout)
if result.returncode != 0:
    print(result.stderr, file=sys.stderr)

sys.exit(0)  # PostToolUse exit code does not block; output reaches Claude
```

> **When to use:** During refactoring sessions or any task where Claude touches multiple files. Disable it temporarily if you intentionally need to leave tests failing mid-task.
>
> **Pitfalls:** Running the full test suite on every edit — that adds seconds per file write. Scope it to the changed file's tests only. For mirrored source trees (e.g., `src/api/users.py` → `tests/api/test_users.py`), adjust the path derivation logic accordingly.

---

### 5. Block writes to sensitive files with [PreToolUse](glossary.md#pretooluse) path pattern matching

Prevent Claude from modifying credentials, secrets, or lock files — regardless of what the prompt says.[^2] [^6]

**Example — Python guard script:**

```python
#!/usr/bin/env python3
# .claude/hooks/protect_sensitive_files.py
import json
import re
import sys

data = json.load(sys.stdin)
file_path = data.get("tool_input", {}).get("file_path", "")

SENSITIVE = re.compile(
    r"(\.env$|\.env\.|secrets\.|credentials|id_rsa|\.pem$|\.key$|"
    r"package-lock\.json|uv\.lock|poetry\.lock)"
)

if SENSITIVE.search(file_path):
    print(f"BLOCKED: write to protected file '{file_path}' is not allowed", file=sys.stderr)
    sys.exit(2)

sys.exit(0)
```

Register for `Edit|Write` on `PreToolUse`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/protect_sensitive_files.py"
          }
        ]
      }
    ]
  }
}
```

> **When to use:** All projects. Especially important in repositories that store `.env.example` alongside `.env`.
>
> **Pitfalls:** Matching too broadly (e.g., blocking all `.json` files). Tune the regex to your project's actual sensitive-file naming conventions.

---

### 6. Re-inject critical context after [context compaction](primitives.md#context-compaction) using a SessionStart hook

[Context compaction](glossary.md#context-compaction) is a lossy summarisation process. Project conventions — mentioned once at session start — are prime candidates for being compressed away. A `SessionStart` hook with `matcher: "compact"` re-injects a short "before you ship" checklist every time compaction occurs.[^7]

Keep the injected content under 50 lines. Every line costs tokens and this fires on every single compaction.

**Example — load from a file (command type, stdout becomes Claude's context):**

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "compact",
        "hooks": [
          {
            "type": "command",
            "command": "cat \"$CLAUDE_PROJECT_DIR\"/.claude/context-essentials.md"
          }
        ]
      }
    ]
  }
}
```

**`.claude/context-essentials.md` (keep under 50 lines):**

```markdown
# Context essentials (re-injected after compaction)

## Critical rules
- Error handling: use Result[T, E] — never raise, always return Result
- Database: PostgreSQL 16 — no raw SQL, use the repository layer
- Tests: uv run pytest tests/ before every commit — TDD
- Auth: always use `ctx.user_id` from context — never accept user_id from request body

## Banned patterns
- `except Exception: pass`
- `SELECT *`
- Direct datetime.now() — use project's `utc_now()` helper
```

Alternatively, use a `Stop` hook with `"type": "prompt"` to unconditionally re-inject rules after every response (not just after compaction):

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Reminder: this project uses Result[T,E] — never raise, always return Result. DB is PostgreSQL 16."
          }
        ]
      }
    ]
  }
}
```

Note: `/compact` is a slash command, so `PostToolUse` with `matcher: "compact"` is the correct event — not a generic `PostToolUse` on file edits.[^2]

> **When to use:** Long multi-session tasks, or any project with strict conventions that Claude tends to drift from after an hour of work.
>
> **Pitfalls:** Putting your entire CLAUDE.md into the essentials file. Keep it to the 5–10 rules Claude most often forgets. CLAUDE.md is the employee handbook; context-essentials is the "before you ship" sticky note.

---

### 7. Auto-allow read-only commands with [permissionDecision](glossary.md#permissiondecision) structured output

Return JSON from a [PreToolUse](glossary.md#pretooluse) hook to approve safe commands programmatically, eliminating repetitive permission dialogs for `ls`, `cat`, `git status`, and similar read-only operations.[^2]

**Example — Python hook returning structured output:**

```python
#!/usr/bin/env python3
# .claude/hooks/auto_allow_readonly.py
import json
import re
import sys

data = json.load(sys.stdin)
cmd = data.get("tool_input", {}).get("command", "")

READONLY = re.compile(
    r"^(ls|cat|head|tail|wc|find|grep|rg|"
    r"git\s+(status|log|diff|show|branch)|"
    r"echo|pwd|which|file|stat|du|df)\b"
)

if READONLY.match(cmd):
    print(json.dumps({"permissionDecision": "allow"}))
    sys.exit(0)

sys.exit(0)  # Fall through to normal permission handling
```

The hook outputs JSON to stdout only when it intends to auto-allow. For any other command, it exits silently and the default permission mode applies.

> **When to use:** Projects where you run in a mode that prompts for every shell command (`--permission-mode ask`). Reduces approval fatigue without disabling security.
>
> **Pitfalls:** Adding commands that have side effects to the allowlist (e.g., `curl`, `python`). Read-only means no network, no writes. Be conservative.

---

### 8. Guard [Stop hooks](glossary.md#stop-hook) with [stop_hook_active](glossary.md#stop-hook-active) to prevent infinite loops

A Stop hook that returns `"ok": false` causes Claude to keep working — which fires the Stop hook again, creating an infinite loop. The `stop_hook_active` field in the hook input signals that you are already inside a Stop hook invocation.[^3] [^1]

**Example — bash guard (same pattern works in Python):**

```bash
#!/bin/bash
# .claude/hooks/stop_check.sh
INPUT=$(cat)

# Break the loop: if we are already inside a stop hook, exit immediately
if [ "$(echo "$INPUT" | jq -r '.stop_hook_active')" = "true" ]; then
  exit 0
fi

# Run quality checks
if ! uv run ruff check . --select E,F,W --quiet 2>&1; then
  echo "Lint failed — fix before stopping" >&2
  exit 2
fi
```

**Python equivalent:**

```python
#!/usr/bin/env python3
import json, subprocess, sys

data = json.load(sys.stdin)
if data.get("stop_hook_active"):
    sys.exit(0)

result = subprocess.run(
    ["uv", "run", "ruff", "check", ".", "--select", "E,F,W", "--quiet"],
    capture_output=True, text=True
)
if result.returncode != 0:
    print("Lint failed — fix before stopping\n" + result.stdout, file=sys.stderr)
    sys.exit(2)
```

> **When to use:** Any Stop hook that conditionally blocks completion — quality gates, lint checks, task-completion verifiers.
>
> **Pitfalls:** Forgetting this guard. The infinite loop is silent: Claude appears to work indefinitely and burns tokens. Always add the `stop_hook_active` check before any blocking logic in a Stop hook.

---

### 9. Use [SessionStart hooks](glossary.md#sessionstart-hook) to prime context from git history

Output recent commits, active branch, and open TODOs at session start so Claude has accurate project state without manual copy-paste.[^2] [^1]

**Example — Python session primer:**

```python
#!/usr/bin/env python3
# ~/.claude/hooks/session_primer.py
import subprocess
import sys

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, shell=True).stdout.strip()

branch = run("git branch --show-current")
log = run("git log --oneline -5")
dirty = run("git status --short")

print(f"## Session context")
print(f"Branch: {branch}")
print(f"\nRecent commits:\n{log}")
if dirty:
    print(f"\nUnstaged changes:\n{dirty}")
```

Register in `~/.claude/settings.json` (personal, applies to all git projects):

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/hooks/session_primer.py"
          }
        ]
      }
    ]
  }
}
```

Use the `matcher` field to fire only on specific session start types:

| Matcher value | When it fires |
|---------------|--------------|
| `startup` | Fresh session start |
| `resume` | Resuming a previous session |
| `compact` | Session resumed after compaction |

> **When to use:** When you switch contexts frequently or work across multiple branches in a day. The hook keeps Claude from making stale assumptions about the current state.
>
> **Pitfalls:** Running expensive operations (network calls, full test suites) in a SessionStart hook — it fires before you have typed anything and must complete before the session is usable.

---

### 10. Profile hooks with `time` — keep [PreToolUse](glossary.md#pretooluse) hooks under 500 ms

Every matched tool call pays the hook execution cost synchronously. A 600 ms PreToolUse hook adds over half a second to every file write. With 50 writes in a session, that is 30 seconds of dead time.[^5] [^4]

**Profiling during development:**

```bash
# Test the hook in isolation with realistic input
echo '{"tool_name":"Edit","tool_input":{"file_path":"src/api/users.py"}}' \
  | time python3 .claude/hooks/format_on_edit.py
```

**Rules of thumb:**

- PreToolUse hooks: target under 200 ms, hard limit 500 ms
- PostToolUse hooks: more forgiving — they do not block Claude from proceeding
- Move slow operations (full test suites, linters on large codebases) to PostToolUse or to `Stop` hooks where latency is expected

**Move a slow formatter to PostToolUse:**

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/format_on_edit.py",
            "timeout": 15000
          }
        ]
      }
    ]
  }
}
```

The `timeout` field (milliseconds) kills the hook process if it exceeds the limit, preventing a hung formatter from blocking the session indefinitely.

> **When to use:** Before deploying any hook to a shared project. Profile it first.
>
> **Pitfalls:** Running `ruff check .` (entire project) in a PreToolUse hook. Run it scoped to the changed file, or move it to PostToolUse. Ten fast hooks outperform two slow ones.

---

## Related themes

- [CLAUDE.md & project memory](claudemd-setup.md) — hooks enforce CLAUDE.md rules at execution time, turning polite instructions into hard guarantees
- [Context management](context-management.md) — SessionStart hooks with `matcher: "compact"` are the most reliable mechanism for re-injecting critical rules after context compaction
- [Commands, skills & plan mode](commands-skills-plan-mode.md) — hooks can trigger automatically when skills expand into prompts via `UserPromptExpansion`, enabling skill-specific automation

---

[^1]: [Automate workflows with hooks — Claude Code docs](references.md#hooks-guide)
[^2]: [Claude Code hooks: 12 production configs I run daily](references.md#2026-02-28-claude-code-hooks-guide)
[^3]: [Claude Code hooks tutorial: 5 production hooks from scratch](references.md#claude-code-hooks-tutorial)
[^4]: [Claude Code hooks: a practical guide to workflow automation](references.md#claude-code-hooks)
[^5]: [Claude Code hooks: a complete guide to automating your AI workflow](references.md#claude-code-hooks-a-complete-guide-to-automating-your-ai-cod)
[^6]: [Claude Code security best practices](references.md#claude-code-security-best-practices)
[^7]: [Claude Code: post-compaction hooks for context renewal](references.md#claude-code-post-compaction-hooks-for-context-renewal-7b616d)
