# Claude Code Hooks: 12 Production Configs I Run Daily (with Failure Modes)

**Type:** article
**URL:** https://www.heyuan110.com/posts/ai/2026-02-28-claude-code-hooks-guide/
**Topic:** Hooks
**Published:** unknown

## Content

[Bruce on AI Engineering](https://www.heyuan110.com/)

[🇨🇳 中文](/zh/posts/ai/2026-02-28-claude-code-hooks-guide/)

* [Posts](https://www.heyuan110.com/posts/)
* [Tags](https://www.heyuan110.com/tags/)
* [Tools](https://www.usemagictools.com/)
* [About](https://www.heyuan110.com/about/)

Feb 26, 2026

# Claude Code Hooks: 12 Production Configs I Run Daily (with Failure Modes)

The 12 Claude Code hook configs running on my machine right now — PreToolUse guards, PostToolUse formatters, Stop notifiers — plus the 4 failure modes that silently broke my workflow before I caught them.

[Claude Code](https://www.heyuan110.com/tags/claude-code)[Hooks](https://www.heyuan110.com/tags/hooks)[Automation](https://www.heyuan110.com/tags/automation)[Configuration](https://www.heyuan110.com/tags/configuration)

[AI Guides](https://www.heyuan110.com/categories/ai-guides)

3692  Words

---

[Claude Code](https://github.com/anthropics/claude-code) is probabilistic. You give it the same prompt twice and get different results. That’s fine for creative work — but your engineering workflow needs deterministic guarantees.

You need files auto-formatted on every save. You need `.env` files locked down. You need `rm -rf /` blocked before it ever reaches your shell. You need these things to happen every single time, not just when the AI remembers.

That’s what Claude Code Hooks do. They’re lifecycle scripts that run at specific points during Claude’s operation — before a tool runs, after a file is edited, when a session starts, when Claude stops. They give you programmatic control over the parts of your workflow that can’t be left to chance.

This guide gives you 12 production-ready hook configurations you can copy-paste into your project right now, plus the technical details to build your own.

## What Are Claude Code Hooks?

Hooks are shell commands or scripts that Claude Code executes at specific points in its lifecycle. They’re defined in your settings files and run automatically — no manual intervention, no prompting, no hoping the AI remembers your preferences.

Think of them as Git hooks, but for your AI coding assistant.

### Why Use Hooks Instead of Prompting?

You could tell Claude “always run Prettier after editing files.” But:

* Claude might forget
* Claude might decide it’s not necessary this time
* Claude can’t block its own operations before they happen
* You can’t enforce security policies through natural language

Hooks solve all of these. They’re deterministic, they run every time, and they can block operations before they execute.

## Core Concepts

### 3 Hook Types

Every hook has a `type` field that determines what it does:

| Type | What It Does | When to Use |
| --- | --- | --- |
| `command` | Runs a shell command | Auto-formatting, logging, notifications, file operations |
| `prompt` | Injects text into Claude’s conversation | Re-injecting context, adding reminders, guiding behavior |
| `agent` | Spawns a sub-agent (a separate Claude instance) | Complex validation, running test suites, multi-step checks |

The `command` type is by far the most common. The `prompt` type is useful for context injection. The `agent` type is powerful but expensive (it uses additional tokens).

### 15 Lifecycle Events

Hooks can attach to these events:

| Event | When It Fires | Common Uses |
| --- | --- | --- |
| `PreToolUse` | Before Claude runs any tool | Block dangerous commands, protect files, auto-allow safe operations |
| `PostToolUse` | After Claude runs any tool | Auto-format code, git staging, logging |
| `Notification` | When Claude needs user attention | Desktop alerts, Slack messages, sound effects |
| `Stop` | When Claude finishes its response | Run tests, verify completion, quality checks |
| `SubagentStop` | When a sub-agent finishes | Validate sub-agent output |
| `PreCompact` | Before context compaction | Save important context |
| `PostCompact` | After context compaction | Re-inject lost context |
| `SessionStart` | When a new session begins | Load project context, set up environment |
| `SessionEnd` | When a session ends | Cleanup, save state |

The most useful events for everyday automation are `PreToolUse`, `PostToolUse`, `Notification`, and `Stop`.

### Config File Locations

Hooks live in your Claude Code settings files. There are three scopes:

| Scope | File Path | Applies To |
| --- | --- | --- |
| **Project** | `.claude/settings.json` (in your repo) | This project only — commit to Git for team sharing |
| **User** | `~/.claude/settings.json` | All your projects |
| **Enterprise** | Managed by your organization | All users in the org |

Project-level hooks are the most common. Put them in `.claude/settings.json` so your entire team gets the same automation.

## Your First Hook: Desktop Notification

Let’s start simple. This hook sends a desktop notification whenever Claude needs your attention — perfect for long-running tasks where you switch to another window.

### macOS

```
{ { { "hooks": {  "hooks": { "hooks":{ "Notification": [  "Notification": [ "Notification":[ {  { { "type": "command",  "type": "command", "type": "command", "command": "osascript -e 'display notification \"Claude needs your attention\" with title \"Claude Code\"'"  "command": "osascript -e 'display notification \"Claude needs your attention\" with title \"Claude Code\"'" "command":"osascript -e 'display notification \"Claude needs your attention\" with title \"Claude Code\"'" }  } } ]  ] ] }  } }} } }
```

### Linux

```
{ { { "hooks": {  "hooks": { "hooks":{ "Notification": [  "Notification": [ "Notification":[ {  { { "type": "command",  "type": "command", "type": "command", "command": "notify-send 'Claude Code' 'Claude needs your attention'"  "command": "notify-send 'Claude Code' 'Claude needs your attention'" "command":"notify-send 'Claude Code' 'Claude needs your attention'" }  } } ]  ] ] }  } }} } }
```

Save this to `~/.claude/settings.json` (user-level, so it works across all projects). The next time Claude pauses for input, you’ll get a system notification.

## Config Structure Deep Dive

Every hook entry has the following fields:

```
{ { { "hooks": {  "hooks": { "hooks":{ "EventName": [  "EventName": [ "EventName":[ {  { { "type": "command",  "type": "command", "type": "command", "command": "your-shell-command",  "command": "your-shell-command", "command":"your-shell-command", "matcher": "regex-pattern",  "matcher": "regex-pattern", "matcher":"regex-pattern", "timeout": 30000  "timeout": 30000 "timeout": 30000 }  } } ]  ] ] }  } }} } }
```

| Field | Required | Default | Description |
| --- | --- | --- | --- |
| `type` | Yes | — | `"command"`, `"prompt"`, or `"agent"` |
| `command` | Yes (for `command` type) | — | Shell command to execute |
| `matcher` | No | Match all | Regex to filter which tools trigger this hook |
| `timeout` | No | 60000 ms | Max execution time in milliseconds before the hook is killed |

### Matcher Rules

The `matcher` field uses **regex** and is **case-sensitive**. This is where most beginners trip up.

| Matcher Value | What It Matches | Example Tools |
| --- | --- | --- |
| `"Bash"` | The Bash tool only | Shell commands |
| `"Edit"` | The Edit tool only | File edits |
| `"Write"` | The Write tool only | File creation |
| `"Edit|Write"` | Edit OR Write | Any file modification |
| `"Bash|Edit|Write"` | Bash, Edit, or Write | Most common operations |
| `"mcp__.*"` | All MCP tools | Any MCP server tool |
| `"mcp__github__.*"` | GitHub MCP tools only | GitHub-specific operations |
| Not specified | All tools | Everything |

**Important**: Tool names are case-sensitive. `"Bash"` works but `"bash"` does not. `"Edit"` works but `"edit"` does not.

### Input/Output Mechanism

Hooks receive context via **stdin** as JSON. The exact structure depends on the event type. For `PreToolUse` and `PostToolUse`, the JSON includes:

```
{ { { "session_id": "abc123",  "session_id": "abc123", "session_id": "abc123", "tool_name": "Bash",  "tool_name": "Bash", "tool_name": "Bash", "tool_input": {  "tool_input": { "tool_input":{ "command": "rm -rf /tmp/old-files"  "command": "rm -rf /tmp/old-files" "command":"rm -rf /tmp/old-files" }  } }} } }
```

For `PostToolUse`, it also includes `tool_output` with the result.

Use `jq` to parse specific fields:

```
# Extract the file path from an Edit operation # Extract the file path from an Edit operation # Extract the file path from an Edit operationjq -r '.tool_input.file_path' jq -r '.tool_input.file_path' '.tool_input.file_path'   # Extract the bash command # Extract the bash command # Extract the bash commandjq -r '.tool_input.command' jq -r '.tool_input.command' '.tool_input.command'
```

### Exit Codes

For `PreToolUse` hooks, exit codes control what happens next:

| Exit Code | Effect |
| --- | --- |
| `0` | Allow the operation to proceed |
| `2` | **Block** the operation — stderr is sent to Claude as feedback |
| Other | Hook error — operation proceeds, error is logged |

For `PostToolUse` hooks, the exit code doesn’t block anything (the operation already happened), but stderr output is still sent to Claude.

### Structured JSON Output

For `PreToolUse` hooks, you can return structured JSON to stdout for more fine-grained control:

```
{ { { "permissionDecision": "allow"  "permissionDecision": "allow" "permissionDecision": "allow"} } }
```

Valid values for `permissionDecision`:

* `"allow"` — Skip the permission prompt, auto-approve
* `"deny"` — Block the operation (same as exit code 2)
* `"ask"` — Show the normal permission prompt to the user

This is especially useful for auto-allowing safe operations while still prompting for dangerous ones.

## 12 Ready-to-Use Configs

Here are 12 production-tested hook configurations. Each one is a complete, copy-pasteable JSON snippet you can drop into your `.claude/settings.json`.

### #1: Auto-Format with Prettier (PostToolUse)

Automatically run Prettier on any file Claude edits or creates. No more “can you format that?” follow-ups.

```
{ { { "hooks": {  "hooks": { "hooks":{ "PostToolUse": [  "PostToolUse": [ "PostToolUse":[ {  { { "type": "command",  "type": "command", "type": "command", "matcher": "Edit|Write",  "matcher": "Edit|Write", "matcher": "Edit|Write", "command": "FILE=$(cat | jq -r '.tool_input.file_path // empty') && [ -n \"$FILE\" ] && npx prettier --write \"$FILE\" 2>/dev/null || true"  "command": "FILE=$(cat | jq -r '.tool_input.file_path // empty') && [ -n \"$FILE\" ] && npx prettier --write \"$FILE\" 2>/dev/null || true" "command":"FILE=$(cat | jq -r '.tool_input.file_path // empty') && [ -n \"$FILE\" ] && npx prettier --write \"$FILE\" 2>/dev/null || true" }  } } ]  ] ] }  } }} } }
```

**How it works**: After every `Edit` or `Write` operation, the hook extracts the file path from stdin, then runs Prettier on that file. The `2>/dev/null || true` ensures the hook doesn’t fail on files Prettier doesn’t support (like images or binary files).

**Prerequisite**: Prettier installed in your project (`npm install --save-dev prettier`).

### #2: Auto-Format with ESLint (PostToolUse)

If you use ESLint with auto-fix instead of (or alongside) Prettier:

```
{ { { "hooks": {  "hooks": { "hooks":{ "PostToolUse": [  "PostToolUse": [ "PostToolUse":[ {  { { "type": "command",  "type": "command", "type": "command", "matcher": "Edit|Write",  "matcher": "Edit|Write", "matcher": "Edit|Write", "command": "FILE=$(cat | jq -r '.tool_input.file_path // empty') && [ -n \"$FILE\" ] && [[ \"$FILE\" =~ \\.(js|ts|jsx|tsx)$ ]] && npx eslint --fix \"$FILE\" 2>/dev/null || true"  "command": "FILE=$(cat | jq -r '.tool_input.file_path // empty') && [ -n \"$FILE\" ] && [[ \"$FILE\" =~ \\.(js|ts|jsx|tsx)$ ]] && npx eslint --fix \"$FILE\" 2>/dev/null || true" "command":"FILE=$(cat | jq -r '.tool_input.file_path // empty') && [ -n \"$FILE\" ] && [[ \"$FILE\" =~ \\.(js|ts|jsx|tsx)$ ]] && npx eslint --fix \"$FILE\" 2>/dev/null || true" }  } } ]  ] ] }  } }} } }
```

**How it works**: Same as Prettier, but only triggers on JavaScript/TypeScript files (`.js`, `.ts`, `.jsx`, `.tsx`). The regex check prevents ESLint from running on files it can’t handle.

**Prerequisite**: ESLint configured in your project.

### #3: Protect Sensitive Files (PreToolUse)

Block Claude from editing `.env` files, lockfiles, and other files that should never be AI-modified:

```
{ { { "hooks": {  "hooks": { "hooks":{ "PreToolUse": [  "PreToolUse": [ "PreToolUse":[ {  { { "type": "command",  "type": "command", "type": "command", "matcher": "Edit|Write",  "matcher": "Edit|Write", "matcher": "Edit|Write", "command": "FILE=$(cat | jq -r '.tool_input.file_path // empty') && if echo \"$FILE\" | grep -qE '(\\.env|\\.lock|secrets\\.yaml|credentials|id_rsa|\\.pem)'; then echo \"BLOCKED: Cannot modify protected file: $FILE\" >&2; exit 2; fi"  "command": "FILE=$(cat | jq -r '.tool_input.file_path // empty') && if echo \"$FILE\" | grep -qE '(\\.env|\\.lock|secrets\\.yaml|credentials|id_rsa|\\.pem)'; then echo \"BLOCKED: Cannot modify protected file: $FILE\" >&2; exit 2; fi" "command":"FILE=$(cat | jq -r '.tool_input.file_path // empty') && if echo \"$FILE\" | grep -qE '(\\.env|\\.lock|secrets\\.yaml|credentials|id_rsa|\\.pem)'; then echo \"BLOCKED: Cannot modify protected file: $FILE\" >&2; exit 2; fi" }  } } ]  ] ] }  } }} } }
```

**How it works**: Before any `Edit` or `Write` operation, the hook checks the target file path against a list of sensitive patterns. If matched, it exits with code 2 (block) and sends an error message to Claude via stderr. Claude will see the message and understand why the operation was blocked.

**Protected patterns**: `.env`, `.lock`, `secrets.yaml`, `credentials`, `id_rsa`, `.pem`. Customize the grep pattern to match your project’s sensitive files.

### #4: Block Dangerous Shell Commands (PreToolUse)

Prevent Claude from running destructive commands, even if it somehow generates them:

```
{ { { "hooks": {  "hooks": { "hooks":{ "PreToolUse": [  "PreToolUse": [ "PreToolUse":[ {  { { "type": "command",  "type": "command", "type": "command", "matcher": "Bash",  "matcher": "Bash", "matcher": "Bash", "command": "CMD=$(cat | jq -r '.tool_input.command // empty') && if echo \"$CMD\" | grep -qEi '(rm\\s+-rf\\s+/|DROP\\s+TABLE|DROP\\s+DATABASE|mkfs\\.|:\\(\\)\\{|chmod\\s+-R\\s+777\\s+/|dd\\s+if=.*of=/dev/)'; then echo \"BLOCKED: Dangerous command detected: $CMD\" >&2; exit 2; fi"  "command": "CMD=$(cat | jq -r '.tool_input.command // empty') && if echo \"$CMD\" | grep -qEi '(rm\\s+-rf\\s+/|DROP\\s+TABLE|DROP\\s+DATABASE|mkfs\\.|:\\(\\)\\{|chmod\\s+-R\\s+777\\s+/|dd\\s+if=.*of=/dev/)'; then echo \"BLOCKED: Dangerous command detected: $CMD\" >&2; exit 2; fi" "command":"CMD=$(cat | jq -r '.tool_input.command // empty') && if echo \"$CMD\" | grep -qEi '(rm\\s+-rf\\s+/|DROP\\s+TABLE|DROP\\s+DATABASE|mkfs\\.|:\\(\\)\\{|chmod\\s+-R\\s+777\\s+/|dd\\s+if=.*of=/dev/)'; then echo \"BLOCKED: Dangerous command detected: $CMD\" >&2; exit 2; fi" }  } } ]  ] ] }  } }} } }
```

**Blocked commands**:

* `rm -rf /` — recursive delete from root
* `DROP TABLE` / `DROP DATABASE` — SQL destructive operations
* `mkfs.` — format filesystem
* `:(){ :|:& };:` — fork bomb
* `chmod -R 777 /` — recursive permission change on root
* `dd if=... of=/dev/` — raw disk writes

**How it works**: The hook inspects the command Claude wants to run. If it matches any dangerous pattern (case-insensitive), the operation is blocked before it ever reaches your shell.

### #5: Git Auto-Stage (PostToolUse)

Automatically `git add` any file Claude modifies, so changes are always staged and ready to commit:

```
{ { { "hooks": {  "hooks": { "hooks":{ "PostToolUse": [  "PostToolUse": [ "PostToolUse":[ {  { { "type": "command",  "type": "command", "type": "command", "matcher": "Edit|Write",  "matcher": "Edit|Write", "matcher": "Edit|Write", "command": "FILE=$(cat | jq -r '.tool_input.file_path // empty') && [ -n \"$FILE\" ] && [ -f \"$FILE\" ] && git add \"$FILE\" 2>/dev/null || true"  "command": "FILE=$(cat | jq -r '.tool_input.file_path // empty') && [ -n \"$FILE\" ] && [ -f \"$FILE\" ] && git add \"$FILE\" 2>/dev/null || true" "command":"FILE=$(cat | jq -r '.tool_input.file_path // empty') && [ -n \"$FILE\" ] && [ -f \"$FILE\" ] && git add \"$FILE\" 2>/dev/null || true" }  } } ]  ] ] }  } }} } }
```

**How it works**: After every file edit or creation, the hook stages the file with `git add`. The `[ -f \"$FILE\" ]` check ensures we don’t try to stage deleted files. Pair this with a good `.gitignore` to prevent staging unwanted files.

**When to use**: Projects where you want every AI change immediately staged. Particularly useful when you review changes with `git diff --cached` before committing.

### #6: Log All Bash Commands (PostToolUse)

Keep a log of every shell command Claude runs — useful for auditing, debugging, and understanding what Claude did in a session:

```
{ { { "hooks": {  "hooks": { "hooks":{ "PostToolUse": [  "PostToolUse": [ "PostToolUse":[ {  { { "type": "command",  "type": "command", "type": "command", "matcher": "Bash",  "matcher": "Bash", "matcher": "Bash", "command": "cat | jq -r '\"[\" + (now | strftime(\"%Y-%m-%d %H:%M:%S\")) + \"] \" + .tool_input.command' >> \"${CLAUDE_PROJECT_DIR:-.}/.claude/command_log.txt\""  "command": "cat | jq -r '\"[\" + (now | strftime(\"%Y-%m-%d %H:%M:%S\")) + \"] \" + .tool_input.command' >> \"${CLAUDE_PROJECT_DIR:-.}/.claude/command_log.txt\"" "command":"cat | jq -r '\"[\" + (now | strftime(\"%Y-%m-%d %H:%M:%S\")) + \"] \" + .tool_input.command' >> \"${CLAUDE_PROJECT_DIR:-.}/.claude/command_log.txt\"" }  } } ]  ] ] }  } }} } }
```

**How it works**: After every Bash command, the hook appends a timestamped entry to `.claude/command_log.txt` in your project directory. Uses the `$CLAUDE_PROJECT_DIR` environment variable (set automatically by Claude Code) to find the project root.

**Output example**:

```
[2026-02-28 14:32:15] npm test [2026-02-28 14:32:15] npm test [2026-02-28 14:32:48] git status [2026-02-28 14:32:48] git status [2026-02-28 14:33:02] cat src/index.ts [2026-02-28 14:33:02] cat src/index.ts 
```

**Tip**: Add `.claude/command_log.txt` to your `.gitignore`.

### #7: Re-Inject Context After Compaction (PostCompact)

When Claude compacts its context window, it can lose important project details. This hook re-injects critical context automatically:

```
{ { { "hooks": {  "hooks": { "hooks":{ "PostCompact": [  "PostCompact": [ "PostCompact":[ {  { { "type": "prompt",  "type": "prompt", "type": "prompt", "command": "IMPORTANT CONTEXT (re-injected after compaction):\n- We are working on the payments microservice\n- Database is PostgreSQL 16 with pgvector extension\n- All API endpoints must return JSON:API format\n- Test files go in __tests__/ next to source files\n- Never use console.log — use the Winston logger"  "command": "IMPORTANT CONTEXT (re-injected after compaction):\n- We are working on the payments microservice\n- Database is PostgreSQL 16 with pgvector extension\n- All API endpoints must return JSON:API format\n- Test files go in __tests__/ next to source files\n- Never use console.log — use the Winston logger" "command":"IMPORTANT CONTEXT (re-injected after compaction):\n- We are working on the payments microservice\n- Database is PostgreSQL 16 with pgvector extension\n- All API endpoints must return JSON:API format\n- Test files go in __tests__/ next to source files\n- Never use console.log — use the Winston logger" }  } } ]  ] ] }  } }} } }
```

**How it works**: The `prompt` type hook injects text directly into Claude’s conversation after context compaction. This ensures critical project rules survive the compaction process.

**Alternative — load from a file**:

```
{ { { "hooks": {  "hooks": { "hooks":{ "PostCompact": [  "PostCompact": [ "PostCompact":[ {  { { "type": "command",  "type": "command", "type": "command", "command": "cat \"${CLAUDE_PROJECT_DIR}/.claude/compaction-context.md\""  "command": "cat \"${CLAUDE_PROJECT_DIR}/.claude/compaction-context.md\"" "command":"cat \"${CLAUDE_PROJECT_DIR}/.claude/compaction-context.md\"" }  } } ]  ] ] }  } }} } }
```

With the `command` type, stdout is sent to Claude as context. Create a `.claude/compaction-context.md` file with your critical project details.

### #8: Stop Hook — Verify Task Completion (Stop)

Use a `prompt` type Stop hook to make Claude self-check its work before finishing:

```
{ { { "hooks": {  "hooks": { "hooks":{ "Stop": [  "Stop": [ "Stop":[ {  { { "type": "prompt",  "type": "prompt", "type": "prompt", "command": "Before finishing, verify:\n1. Did you run the tests? If not, run them now.\n2. Did you update the relevant documentation?\n3. Are there any TODO comments left in the code?\nIf any check fails, continue working. Only stop when all checks pass.\nIMPORTANT: If stop_hook_active is true in your context, do NOT trigger this check again — just finish."  "command": "Before finishing, verify:\n1. Did you run the tests? If not, run them now.\n2. Did you update the relevant documentation?\n3. Are there any TODO comments left in the code?\nIf any check fails, continue working. Only stop when all checks pass.\nIMPORTANT: If stop_hook_active is true in your context, do NOT trigger this check again — just finish." "command":"Before finishing, verify:\n1. Did you run the tests? If not, run them now.\n2. Did you update the relevant documentation?\n3. Are there any TODO comments left in the code?\nIf any check fails, continue working. Only stop when all checks pass.\nIMPORTANT: If stop_hook_active is true in your context, do NOT trigger this check again — just finish." }  } } ]  ] ] }  } }} } }
```

**How it works**: When Claude decides to stop, this prompt hook injects a checklist. Claude reads it and either continues working (if checks fail) or confirms completion. The `stop_hook_active` guard prevents infinite loops — without it, Claude would trigger the Stop hook again after completing the checklist, creating an endless cycle.

**Warning**: This hook makes Claude do more work (and use more tokens) on every task. Use it selectively on projects where thoroughness matters more than speed.

### #9: Agent Hook — Auto-Run Tests (Stop)

Use an `agent` type Stop hook to spawn a sub-agent that runs your test suite:

```
{ { { "hooks": {  "hooks": { "hooks":{ "Stop": [  "Stop": [ "Stop":[ {  { { "type": "agent",  "type": "agent", "type": "agent", "command": "Run the project's test suite with 'npm test'. If any tests fail, report which tests failed and suggest fixes. Do not modify any files — only report results."  "command": "Run the project's test suite with 'npm test'. If any tests fail, report which tests failed and suggest fixes. Do not modify any files — only report results." "command":"Run the project's test suite with 'npm test'. If any tests fail, report which tests failed and suggest fixes. Do not modify any files — only report results." }  } } ]  ] ] }  } }} } }
```

**How it works**: When Claude finishes a task, a separate Claude instance (sub-agent) runs `npm test` and reports results. The sub-agent has access to all the same tools but operates independently.

**Cost warning**: Agent hooks spawn a new Claude instance, which uses additional tokens. For a typical test run, expect 2,000–5,000 extra input tokens plus whatever output the sub-agent generates. Use this for critical workflows, not every minor edit.

### #10: Auto-Allow Read-Only Operations (PreToolUse)

Skip permission prompts for safe, read-only operations while still prompting for writes:

```
{ { { "hooks": {  "hooks": { "hooks":{ "PreToolUse": [  "PreToolUse": [ "PreToolUse":[ {  { { "type": "command",  "type": "command", "type": "command", "matcher": "Bash",  "matcher": "Bash", "matcher": "Bash", "command": "CMD=$(cat | jq -r '.tool_input.command // empty') && if echo \"$CMD\" | grep -qE '^(ls|cat|head|tail|wc|find|grep|rg|git\\s+(status|log|diff|show|branch)|echo|pwd|which|file|stat|du|df)\\b'; then echo '{\"permissionDecision\": \"allow\"}'; fi"  "command": "CMD=$(cat | jq -r '.tool_input.command // empty') && if echo \"$CMD\" | grep -qE '^(ls|cat|head|tail|wc|find|grep|rg|git\\s+(status|log|diff|show|branch)|echo|pwd|which|file|stat|du|df)\\b'; then echo '{\"permissionDecision\": \"allow\"}'; fi" "command":"CMD=$(cat | jq -r '.tool_input.command // empty') && if echo \"$CMD\" | grep -qE '^(ls|cat|head|tail|wc|find|grep|rg|git\\s+(status|log|diff|show|branch)|echo|pwd|which|file|stat|du|df)\\b'; then echo '{\"permissionDecision\": \"allow\"}'; fi" }  } } ]  ] ] }  } }} } }
```

**How it works**: The hook checks if the command starts with a known safe command (`ls`, `cat`, `grep`, `git status`, etc.). If it does, the hook outputs a JSON object with `permissionDecision: "allow"`, which tells Claude Code to skip the permission prompt. For any other command, the hook produces no output and exits normally, falling through to the default permission behavior.

**Commands auto-allowed**: `ls`, `cat`, `head`, `tail`, `wc`, `find`, `grep`, `rg`, `git status/log/diff/show/branch`, `echo`, `pwd`, `which`, `file`, `stat`, `du`, `df`.

**Security note**: This is a convenience hook. Review the list and remove any commands you consider potentially dangerous for your environment.

### #11: Replace Inefficient Commands (PreToolUse)

Claude sometimes uses slow or inefficient commands. This hook suggests better alternatives:

```
{ { { "hooks": {  "hooks": { "hooks":{ "PreToolUse": [  "PreToolUse": [ "PreToolUse":[ {  { { "type": "command",  "type": "command", "type": "command", "matcher": "Bash",  "matcher": "Bash", "matcher": "Bash", "command": "CMD=$(cat | jq -r '.tool_input.command // empty') && if echo \"$CMD\" | grep -qE 'find .* -name.*\\|.*grep'; then echo 'SUGGESTION: Use fd or find with -path instead of piping to grep. Example: fd --type f \"pattern\" or find . -path \"*pattern*\"' >&2; exit 2; elif echo \"$CMD\" | grep -qE 'cat .* \\| head'; then echo 'SUGGESTION: Use head -n N file directly instead of cat | head. This avoids an unnecessary pipe.' >&2; exit 2; fi"  "command": "CMD=$(cat | jq -r '.tool_input.command // empty') && if echo \"$CMD\" | grep -qE 'find .* -name.*\\|.*grep'; then echo 'SUGGESTION: Use fd or find with -path instead of piping to grep. Example: fd --type f \"pattern\" or find . -path \"*pattern*\"' >&2; exit 2; elif echo \"$CMD\" | grep -qE 'cat .* \\| head'; then echo 'SUGGESTION: Use head -n N file directly instead of cat | head. This avoids an unnecessary pipe.' >&2; exit 2; fi" "command":"CMD=$(cat | jq -r '.tool_input.command // empty') && if echo \"$CMD\" | grep -qE 'find .* -name.*\\|.*grep'; then echo 'SUGGESTION: Use fd or find with -path instead of piping to grep. Example: fd --type f \"pattern\" or find . -path \"*pattern*\"' >&2; exit 2; elif echo \"$CMD\" | grep -qE 'cat .* \\| head'; then echo 'SUGGESTION: Use head -n N file directly instead of cat | head. This avoids an unnecessary pipe.' >&2; exit 2; fi" }  } } ]  ] ] }  } }} } }
```

**How it works**: The hook detects common anti-patterns like `find ... | grep` and `cat file | head`, blocks them, and sends Claude a suggestion for a more efficient alternative via stderr. Claude will then retry with the better command.

**Patterns caught**:

* `find ... | grep` → suggests `fd` or `find -path`
* `cat file | head` → suggests `head file` directly

You can extend this with additional patterns specific to your workflow.

### #12: Slack Notification (Notification)

Send a Slack message when Claude needs your attention. Great for long-running tasks:

```
{ { { "hooks": {  "hooks": { "hooks":{ "Notification": [  "Notification": [ "Notification":[ {  { { "type": "command",  "type": "command", "type": "command", "command": "TITLE=$(cat | jq -r '.title // \"Claude Code\"') && MSG=$(cat | jq -r '.message // \"Needs attention\"') && curl -s -X POST \"$SLACK_WEBHOOK_URL\" -H 'Content-Type: application/json' -d \"{\\\"text\\\": \\\"*${TITLE}*: ${MSG}\\\"}\""  "command": "TITLE=$(cat | jq -r '.title // \"Claude Code\"') && MSG=$(cat | jq -r '.message // \"Needs attention\"') && curl -s -X POST \"$SLACK_WEBHOOK_URL\" -H 'Content-Type: application/json' -d \"{\\\"text\\\": \\\"*${TITLE}*: ${MSG}\\\"}\"" "command":"TITLE=$(cat | jq -r '.title // \"Claude Code\"') && MSG=$(cat | jq -r '.message // \"Needs attention\"') && curl -s -X POST \"$SLACK_WEBHOOK_URL\" -H 'Content-Type: application/json' -d \"{\\\"text\\\": \\\"*${TITLE}*: ${MSG}\\\"}\"" }  } } ]  ] ] }  } }} } }
```

**Prerequisites**:

1. Create a Slack Incoming Webhook at [api.slack.com/messaging/webhooks](https://api.slack.com/messaging/webhooks)
2. Set the environment variable: `export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"`

**How it works**: When Claude triggers a notification event, the hook extracts the title and message from stdin, then sends them to your Slack channel via webhook. You’ll see messages like: **Claude Code**: Task completed, waiting for review.

**Alternative — pipe stdin directly**:

```
{ { { "hooks": {  "hooks": { "hooks":{ "Notification": [  "Notification": [ "Notification":[ {  { { "type": "command",  "type": "command", "type": "command", "command": "MSG=$(cat | jq -r '.message // \"Needs attention\"') && curl -s -X POST \"$SLACK_WEBHOOK_URL\" -H 'Content-Type: application/json' -d \"{\\\"text\\\": \\\"Claude Code: ${MSG}\\\"}\""  "command": "MSG=$(cat | jq -r '.message // \"Needs attention\"') && curl -s -X POST \"$SLACK_WEBHOOK_URL\" -H 'Content-Type: application/json' -d \"{\\\"text\\\": \\\"Claude Code: ${MSG}\\\"}\"" "command":"MSG=$(cat | jq -r '.message // \"Needs attention\"') && curl -s -X POST \"$SLACK_WEBHOOK_URL\" -H 'Content-Type: application/json' -d \"{\\\"text\\\": \\\"Claude Code: ${MSG}\\\"}\"" }  } } ]  ] ] }  } }} } }
```

## Combined Config: A Complete Project Setup

Here’s a real-world `.claude/settings.json` that combines several hooks into a production-ready configuration:

```
{ { { "hooks": {  "hooks": { "hooks":{ "PreToolUse": [  "PreToolUse": [ "PreToolUse":[ {  { { "type": "command",  "type": "command", "type": "command", "matcher": "Edit|Write",  "matcher": "Edit|Write", "matcher": "Edit|Write", "command": "FILE=$(cat | jq -r '.tool_input.file_path // empty') && if echo \"$FILE\" | grep -qE '(\\.env|\\.lock|secrets\\.yaml|credentials)'; then echo \"BLOCKED: Cannot modify protected file: $FILE\" >&2; exit 2; fi"  "command": "FILE=$(cat | jq -r '.tool_input.file_path // empty') && if echo \"$FILE\" | grep -qE '(\\.env|\\.lock|secrets\\.yaml|credentials)'; then echo \"BLOCKED: Cannot modify protected file: $FILE\" >&2; exit 2; fi" "command":"FILE=$(cat | jq -r '.tool_input.file_path // empty') && if echo \"$FILE\" | grep -qE '(\\.env|\\.lock|secrets\\.yaml|credentials)'; then echo \"BLOCKED: Cannot modify protected file: $FILE\" >&2; exit 2; fi" },  }, }, {  { { "type": "command",  "type": "command", "type": "command", "matcher": "Bash",  "matcher": "Bash", "matcher": "Bash", "command": "CMD=$(cat | jq -r '.tool_input.command // empty') && if echo \"$CMD\" | grep -qEi '(rm\\s+-rf\\s+/|DROP\\s+TABLE|DROP\\s+DATABASE)'; then echo \"BLOCKED: Dangerous command detected\" >&2; exit 2; fi"  "command": "CMD=$(cat | jq -r '.tool_input.command // empty') && if echo \"$CMD\" | grep -qEi '(rm\\s+-rf\\s+/|DROP\\s+TABLE|DROP\\s+DATABASE)'; then echo \"BLOCKED: Dangerous command detected\" >&2; exit 2; fi" "command":"CMD=$(cat | jq -r '.tool_input.command // empty') && if echo \"$CMD\" | grep -qEi '(rm\\s+-rf\\s+/|DROP\\s+TABLE|DROP\\s+DATABASE)'; then echo \"BLOCKED: Dangerous command detected\" >&2; exit 2; fi" },  }, }, {  { { "type": "command",  "type": "command", "type": "command", "matcher": "Bash",  "matcher": "Bash", "matcher": "Bash", "command": "CMD=$(cat | jq -r '.tool_input.command // empty') && if echo \"$CMD\" | grep -qE '^(ls|cat|head|tail|wc|grep|rg|git\\s+(status|log|diff|show)|pwd|which)\\b'; then echo '{\"permissionDecision\": \"allow\"}'; fi"  "command": "CMD=$(ca

[Content truncated]
