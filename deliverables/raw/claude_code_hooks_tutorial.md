# Claude Code Hooks Tutorial: 5 Production Hooks From Scratch

**Type:** article
**URL:** https://blakecrosley.com/blog/claude-code-hooks-tutorial
**Topic:** Hooks
**Published:** unknown

## Content

# Claude Code Hooks Tutorial: 5 Production Hooks From Scratch

Claude Code executes the right action the vast majority of the time. The remaining edge cases include force-pushing to main, skipping your formatter, and committing code that fails lint. Hooks eliminate those edge cases by adding deterministic gates at 17 lifecycle points in Claude’s workflow.[1](#fn:1) This tutorial is part of my [AI engineering](/writing/ai-engineering) series on building production-grade agent systems. They fire every time, without exception, regardless of prompt phrasing or model behavior.

**TL;DR:** Hooks are shell commands triggered by Claude Code lifecycle events.[1](#fn:1) `PreToolUse` hooks inspect and block actions (exit code 2 = block, exit 0 = allow).[2](#fn:2) `PostToolUse` hooks validate and format after the fact. Configure them in `.claude/settings.json` with a `matcher` regex and a nested `hooks` array.[3](#fn:3) The tutorial below builds five production hooks: auto-formatter, security gate, test runner, notification alert, and pre-commit quality check.

`PreToolUse`
`PostToolUse`
`.claude/settings.json`
`matcher`
`hooks`

## Key Takeaways

`.claude/settings.json`
`exit 2`

## What Are Hooks?

Hooks are shell commands that execute at specific lifecycle events during a Claude Code session. They run outside the LLM as plain scripts triggered by Claude’s actions, not prompts interpreted by the model.

Four key categories cover the most common use cases (Claude Code supports 17 event types total):[1](#fn:1)

`SessionStart`
`Stop`
`PreToolUse`
`PostToolUse`
`Notification`
`SubagentStop`

**Exit code semantics matter.**[2](#fn:2) Exit 0 means success (proceed). Exit 2 means block the action. Exit 1 means a non-blocking hook error where the action still proceeds. Every security-critical hook must use `exit 2` to actually enforce its gate.

`exit 2`

## The Mental Model: Three Types of Guarantees

Before writing any hook, ask: what kind of guarantee do I need?

**Formatting guarantees** ensure consistency after the fact. PostToolUse hooks on Write/Edit run your formatter after every file change. The model’s output does not matter because the formatter normalizes everything. These hooks are idempotent and safe to run on every edit.

**Safety guarantees** prevent dangerous actions before they execute. PreToolUse hooks on Bash inspect commands and block destructive patterns with exit code 2. These hooks must be fast (under 500ms) because they gate every matched tool call, and they must use exit 2 (not exit 1) because exit 1 only warns without blocking.

**Quality guarantees** validate state at decision points. PreToolUse hooks on `git commit` commands run your linter or test suite and block the commit if quality checks fail. Unlike formatting hooks (which fire on every edit), quality hooks fire only at specific moments, keeping the overhead low.

`git commit`

The conceptual ancestor is Git hooks[8](#fn:8): `pre-commit`, `pre-push`, and `post-commit` serve the same three roles. Claude Code hooks extend the pattern from Git operations to every tool action the agent takes. I dissect this evolution in [every hook is a scar](/blog/every-hook-is-a-scar) — each hook exists because something went wrong without it.

`pre-commit`
`pre-push`
`post-commit`

## Hook Configuration Basics

Hooks live in your settings files:

`.claude/settings.json`
`~/.claude/settings.json`

The JSON structure:

`{
 "hooks": {
 "PreToolUse": [
 {
 "matcher": "Bash",
 "hooks": [
 {
 "type": "command",
 "command": "/path/to/your/script.sh"
 }
 ]
 }
 ],
 "PostToolUse": [
 {
 "matcher": "Write|Edit",
 "hooks": [
 {
 "type": "command",
 "command": "/path/to/another-script.sh"
 }
 ]
 }
 ]
 }
}`

Each entry has a `matcher` (regex matching tool names like `Bash`, `Write`, `Edit`, `Read`, `Glob`, `Grep`, or `Agent`) and a `hooks` array of hook definitions. Each hook specifies a `type` (`"command"` for shell commands) and the `command` to run. The matcher `Write|Edit` matches both tool types.

`matcher`
`Bash`
`Write`
`Edit`
`Read`
`Glob`
`Grep`
`Agent`
`hooks`
`type`
`"command"`
`command`
`Write|Edit`

You can also manage hooks interactively with the `/hooks` slash command inside a Claude Code session.[5](#fn:5)

`/hooks`

When a hook fires, Claude Code passes context via environment variables (`$FILE_PATH` for file operations) and stdin (a JSON object containing the tool name, parameters, and session metadata).[6](#fn:6) Your script reads this context to make decisions.

`$FILE_PATH`

## 5 Practical Hooks

Each hook below solves a real problem I encountered while using Claude Code as my primary development tool. All examples use the correct nested hook schema from the Claude Code source[7](#fn:7).

### 1. Auto-Format on File Edit

Claude writes functionally correct code that occasionally breaks your project’s formatting rules. I initially tried adding “always run black after editing Python files” to my CLAUDE.md, but the instruction worked only about 80% of the time. The model would sometimes skip the formatting step when it was focused on a complex multi-file change. A PostToolUse hook eliminates the inconsistency entirely: your formatter runs after every file write, regardless of what the model chose to do.

`{
 "hooks": {
 "PostToolUse": [
 {
 "matcher": "Write|Edit",
 "hooks": [
 {
 "type": "command",
 "command": "bash -c 'if [[ \"$FILE_PATH\" == *.py ]]; then black --quiet \"$FILE_PATH\" 2>/dev/null; elif [[ \"$FILE_PATH\" == *.js ]] || [[ \"$FILE_PATH\" == *.ts ]]; then npx prettier --write \"$FILE_PATH\" 2>/dev/null; fi'"
 }
 ]
 }
 ]
 }
}`

Claude Code sets `$FILE_PATH` to the modified file. The hook checks the extension and runs the appropriate formatter. Python files get `black`, JavaScript and TypeScript files get `prettier`. The `2>/dev/null` suppresses noisy output so you only see actual errors.

`$FILE_PATH`
`black`
`prettier`
`2>/dev/null`

For larger projects, move the inline command to a standalone script for readability.

### 2. Security Gate for Dangerous Commands

PreToolUse hooks on the Bash tool inspect the command Claude is about to run and block it if the command matches a dangerous pattern. I wrote the first version of this hook after Claude force-pushed to main during a refactoring session. (I explore the broader implications of agent autonomy in [anatomy of a claw](/blog/anatomy-of-a-claw) and [Claude Code as infrastructure](/blog/claude-code-as-infrastructure).) The model had been asked to “push the changes” and interpreted that as `git push --force origin main` because the branch had diverged. The fix took seconds; the incident motivated a permanent gate.

`git push --force origin main`
`{
 "hooks": {
 "PreToolUse": [
 {
 "matcher": "Bash",
 "hooks": [
 {
 "type": "command",
 "command": "bash -c 'INPUT=$(cat); CMD=$(echo \"$INPUT\" | jq -r \".tool_input.command\"); if echo \"$CMD\" | grep -qE \"rm\\s+-rf\\s+/|git\\s+push\\s+(-f|--force)\\s+(origin\\s+)?main|git\\s+reset\\s+--hard|DROP\\s+TABLE|:(){ :|:& };:\"; then echo \"BLOCKED: Dangerous command detected: $CMD\" >&2; exit 2; fi'"
 }
 ]
 }
 ]
 }
}`

When this hook exits with code 2, Claude Code cancels the pending command. The error message prints to both your terminal and Claude’s context, so the model understands why the action failed and suggests a safer alternative.

Blocked patterns:
- `rm -rf /` (recursive deletion from root)
- `git push --force main` and `git push -f main` (force pushing to the main branch)
- `git reset --hard` (destroying uncommitted work)
- `DROP TABLE` (accidental database destruction)
- Fork bombs

`rm -rf /`
`git push --force main`
`git push -f main`
`git reset --hard`
`DROP TABLE`

Customize this list for your environment. Production databases need destructive SQL patterns. CLI-based deployments need deployment command guards.

### 3. Test Runner After Changes

When Claude edits a Python file, automatically run the relevant tests. Immediate test execution catches regressions before they compound across three or four subsequent file edits.

`{
 "hooks": {
 "PostToolUse": [
 {
 "matcher": "Write|Edit",
 "hooks": [
 {
 "type": "command",
 "command": "bash -c 'if [[ \"$FILE_PATH\" == *.py ]] && [[ \"$FILE_PATH\" != *test_* ]]; then TEST_FILE=\"tests/test_$(basename \"$FILE_PATH\")\"; if [[ -f \"$TEST_FILE\" ]]; then python -m pytest \"$TEST_FILE\" -x --tb=short 2>&1 | tail -20; fi; fi'"
 }
 ]
 }
 ]
 }
}`

The hook checks whether the edited file is a Python source file (not a test file itself), looks for a corresponding test file using the `test_` prefix naming convention, and runs it if found. The `-x` flag stops at the first failure, and `tail -20` keeps the output concise.

`test_`
`-x`
`tail -20`

**Note:** The hook above assumes a flat `tests/` directory with `test_` prefix naming. For projects that mirror the source tree (e.g., `tests/api/test_users.py` matching `src/api/users.py`), replace the `TEST_FILE` line with:

`tests/`
`test_`
`tests/api/test_users.py`
`src/api/users.py`
`TEST_FILE`
`TEST_FILE="tests/$(echo "$FILE_PATH" | sed 's|.*/src/||; s|/\([^/]*\)\.py|/test_\1.py|')"`

The test runner hook proves particularly valuable during refactoring sessions where Claude touches multiple files. Without immediate feedback, errors compound: Claude edits file A, breaking file B’s tests, then edits file C based on the broken state of B. By the time you discover the failure, three files need fixing instead of one. Running tests after each edit catches the first break immediately.

### 4. Notification on Session End

Long-running Claude Code sessions can take minutes. Rather than watching the terminal, get a notification when the session finishes.

`{
 "hooks": {
 "Stop": [
 {
 "matcher": "",
 "hooks": [
 {
 "type": "command",
 "command": "osascript -e 'display notification \"Claude Code session ended\" with title \"Claude Code\"'"
 }
 ]
 }
 ]
 }
}`

The macOS variant above uses `osascript` to trigger a native notification. For Linux, replace the `osascript` line with `notify-send "Claude Code" "Session ended"`. For Slack notifications, use a webhook:

`osascript`
`osascript`
`notify-send "Claude Code" "Session ended"`
`curl -s -X POST "$SLACK_WEBHOOK_URL" \
 -H 'Content-type: application/json' \
 -d '{"text": "Claude Code session ended"}'`

I use the Slack variant for background tasks kicked off with `& <task>` (Claude Code’s background mode). The desktop notification handles interactive sessions.

`& <task>`

### 5. Quality Check Before Commit

Before Claude runs `git commit`, validate that the code passes linting. A pre-commit lint gate catches issues that formatting alone misses: unused imports, undefined variables, type errors.

`git commit`
`{
 "hooks": {
 "PreToolUse": [
 {
 "matcher": "Bash",
 "hooks": [
 {
 "type": "command",
 "command": "bash -c 'INPUT=$(cat); CMD=$(echo \"$INPUT\" | jq -r \".tool_input.command\"); if echo \"$CMD\" | grep -qE \"^git\\s+commit\"; then if ! LINT_OUTPUT=$(ruff check . --select E,F,W 2>&1); then echo \"LINT FAILED -- fix before committing:\" >&2; echo \"$LINT_OUTPUT\" >&2; exit 2; fi; fi'"
 }
 ]
 }
 ]
 }
}`

The quality gate activates only when the Bash command starts with `git commit`. It runs `ruff` (a fast Python linter) with error, pyflakes, and warning rules. If any issues exist, the hook blocks the commit (exit 2) and Claude sees the lint output, which typically causes it to fix the issues and retry.

`git commit`
`ruff`

You can layer multiple quality checks: `mypy` for type checking, `bandit` for security scanning, or your project’s custom validation scripts. PreToolUse hooks on Bash commands give you a programmable gate before any shell action.

`mypy`
`bandit`

## Hook Debugging Tips

Hooks fail silently more often than you would expect. Five techniques I use to debug them:

`echo '{"tool_input":{"command":"git commit -m test"}}' | bash your-hook.sh`
`echo "DEBUG: matched $CMD" >&2`
`jq`
`null`
`jq`
`exit 1`
`exit 2`

**The most common hook mistake:** writing a security gate with `exit 1` instead of `exit 2`. The hook appears to work during testing because the warning message prints to the terminal. But exit 1 is a non-blocking warning. The dangerous command still executes. I have seen this mistake in three different teams’ hook configurations, each of which believed they had blocked force pushes. Test every security hook by triggering the blocked pattern and verifying the action was actually prevented, not just warned about.

`exit 1`
`exit 2`

## Next Steps

These five hooks cover the fundamentals: formatting, security, testing, notifications, and quality gates. Once you are comfortable with these patterns, you can build hooks for context injection (adding project-specific instructions at session start), recursion guards (preventing infinite subagent loops), and workflow orchestration (chaining multi-step processes).

For hook architecture, all 17 lifecycle events, and advanced patterns, see the hooks section of my full [Claude Code guide](/guides/claude-code#how-do-hooks-work).

I also wrote about the origin stories behind my 95 production hooks in [Claude Code Hooks: Why Each of My 95 Hooks Exists](/blog/claude-code-hooks), which covers the incidents that motivated each one.

## References

## FAQ

### Can hooks block Claude Code from running a command?

Yes. PreToolUse hooks block any tool action by exiting with code 2. Claude Code cancels the pending action and shows the hook’s stderr output to the model. Exit 1 is a non-blocking hook error where the action still proceeds. The exit code distinction matters: every security hook must use `exit 2`, not `exit 1`.[2](#fn:2) Claude sees the rejection reason and suggests a safer alternative.

`exit 2`
`exit 1`

### Where do I put hook configuration files?

Hook configurations go in `.claude/settings.json` for project-level hooks (committed to your repository, shared with your team) or `~/.claude/settings.json` for user-level hooks (personal, applied to every project). Project-level hooks take precedence when both exist. I recommend using absolute paths for script files to avoid working-directory issues.

`.claude/settings.json`
`~/.claude/settings.json`

### Do hooks work with subagents?

Yes. Hooks fire for subagent actions too.[4](#fn:4) If Claude spawns a subagent via the Agent tool, your PreToolUse and PostToolUse hooks execute for every tool the subagent uses. Without recursive hook enforcement, a subagent could bypass your safety gates. The `SubagentStop` event lets you run cleanup or validation when a subagent completes its task.[4](#fn:4)

`SubagentStop`

### How many hooks is too many?

Performance, not count, is the constraint. Each hook runs synchronously, so total hook execution time adds to every matched tool call. I run 95 hooks across user-level and project-level settings without noticeable latency because each hook completes in under 200ms. The threshold I watch: if a PostToolUse hook adds more than 500ms to every file edit, the session feels sluggish. Profile your hooks with `time` before deploying them. Ten fast hooks outperform two slow ones.

`time`

Anthropic, “Claude Code Hooks: Lifecycle Events.” [docs.anthropic.com/en/docs/claude-code/hooks](https://docs.anthropic.com/en/docs/claude-code/hooks) [↩](#fnref:1 "Jump back to footnote 1 in the text")[↩](#fnref2:1 "Jump back to footnote 1 in the text")[↩](#fnref3:1 "Jump back to footnote 1 in the text")

Anthropic, “Claude Code Hooks: Exit Codes.” [docs.anthropic.com/en/docs/claude-code/hooks#exit-codes](https://docs.anthropic.com/en/docs/claude-code/hooks#exit-codes) [↩](#fnref:2 "Jump back to footnote 2 in the text")[↩](#fnref2:2 "Jump back to footnote 2 in the text")[↩](#fnref3:2 "Jump back to footnote 2 in the text")[↩](#fnref4:2 "Jump back to footnote 2 in the text")

Anthropic, “Claude Code Hooks: Configuration.” [docs.anthropic.com/en/docs/claude-code/hooks#configuration](https://docs.anthropic.com/en/docs/claude-code/hooks#configuration) [↩](#fnref:3 "Jump back to footnote 3 in the text")[↩](#fnref2:3 "Jump back to footnote 3 in the text")[↩](#fnref3:3 "Jump back to footnote 3 in the text")

Anthropic, “Claude Code Hooks: Subagent Events.” [docs.anthropic.com/en/docs/claude-code/hooks#subagent-hooks](https://docs.anthropic.com/en/docs/claude-code/hooks#subagent-hooks) [↩](#fnref:4 "Jump back to footnote 4 in the text")[↩](#fnref2:4 "Jump back to footnote 4 in the text")[↩](#fnref3:4 "Jump back to footnote 4 in the text")

Anthropic, “Claude Code Overview.” [docs.anthropic.com/en/docs/claude-code/overview](https://docs.anthropic.com/en/docs/claude-code/overview) [↩](#fnref:5 "Jump back to footnote 5 in the text")

Anthropic, “Claude Code Hooks: Hook Input.” [docs.anthropic.com/en/docs/claude-code/hooks#hook-input](https://docs.anthropic.com/en/docs/claude-code/hooks#hook-input) [↩](#fnref:6 "Jump back to footnote 6 in the text")

Anthropic, “Claude Code: Source and Hook Schema.” [github.com/anthropics/claude-code](https://github.com/anthropics/claude-code) [↩](#fnref:7 "Jump back to footnote 7 in the text")

Git Documentation, “Customizing Git: Git Hooks.” [git-scm.com/book/en/v2/Customizing-Git-Git-Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) [↩](#fnref:8 "Jump back to footnote 8 in the text")

jq Manual, “Command-line JSON processor.” [jqlang.github.io/jq/manual](https://jqlang.github.io/jq/manual/) [↩](#fnref:9 "Jump back to footnote 9 in the text")

## Claude Code Resources

## AI Engineering Post 30 of 63

## Related Posts

### Codex CLI vs Claude Code 2026: Architecture, Pricing, and China Access

Deep comparison of Codex CLI and Claude Code: kernel sandboxing vs 26-hook governance, Opus 4.7 vs GPT-5.4 benchmarks, p…

### Claude Code Hooks: Why Each of My 95 Hooks Exists

I built 95 hooks for Claude Code. Each one exists because something went wrong. Here are the origin stories and the arch…

Designer, developer, and maker of things.

### Navigate

### Guides

### Projects

### Connect

© 2026 Blake Crosley. All rights reserved.

Pasadena, California
