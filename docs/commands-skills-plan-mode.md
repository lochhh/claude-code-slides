# Commands, skills & plan mode

[← Back to index](index.md)

[Slash commands and skills](primitives.md#slash-commands-and-skills) are how you codify your workflow — turning ad-hoc prompts into repeatable, shareable, automatable operations. As of Claude Code 2.1.3, commands and skills run on the same underlying framework: a markdown file in `.claude/commands/` and a `SKILL.md` in `.claude/skills/<name>/` are interchangeable — both appear in the `/` menu and behave identically. The choice between them is structural: flat files for simple definitions, folders when you need supporting assets alongside the skill. [Plan mode](primitives.md#plan-mode) closes the loop by giving you a review checkpoint before any changes land. Together these primitives let you move from "type a prompt and hope" to "define once, invoke consistently."

**Level:** Intermediate

## Tips

### 1. Define custom slash commands in `.claude/commands/` for repeated prompts

Every prompt you type more than twice a week belongs in a command file. Any `.md` file placed in `.claude/commands/` is discovered automatically at session start and becomes a `/command-name` you can invoke from the prompt. Commit the directory to version control and the entire team shares the same shorthand.[^1][^2]

**Example:**

```
# .claude/commands/review-auth.md
---
allowed-tools: Read, Grep, Glob
description: Code review focused on the authentication module
---

Review the authentication module for security issues, covering:
- Session token handling and expiry
- Password hashing and storage
- Input validation on login/register endpoints
- Privilege escalation paths

Read all files under src/auth/ and report findings by severity.
```

Invoke with `/review-auth`. No arguments needed — the scope is already encoded.

> **When to use:** Any time you run the same prompt structure more than a few times a week. Good first candidates: code review checklists, release preflight checks, architecture consistency audits.
>
> **Pitfalls:** Letting command files drift out of date. Treat them like code — review them when the underlying conventions change. A stale command produces confidently wrong output.

### 2. Use `$ARGUMENTS` in custom commands for dynamic input

The [`$ARGUMENTS`](glossary.md#arguments) placeholder is replaced at invocation time with whatever text follows the command name. This makes a single command file flexible enough to target different files, GitHub issues, or PR numbers without duplicating the file.[^2][^3]

**Example:**

```
# .claude/commands/fix-issue.md
---
argument-hint: <issue-number>
description: Fix a GitHub issue following project error-handling conventions
allowed-tools: Read, Edit, Bash(git diff *), Bash(gh issue view *)
---

Fix GitHub issue #$ARGUMENTS following our error handling conventions
(defined in CLAUDE.md under "Error Handling Rules").

Steps:
1. Run: gh issue view $ARGUMENTS
2. Identify affected files
3. Implement the fix
4. Add or update tests covering the fix
5. Show a diff before committing
```

Invoke with `/fix-issue 123` — the number propagates into every `$ARGUMENTS` reference in the file.

> **When to use:** Any command that operates on a variable target: a file, a PR number, a test pattern, a module name.
>
> **Pitfalls:** Passing multiple tokens when the command expects one. `$ARGUMENTS` captures the full text after the command name as a single string. Use positional variants `$1`, `$2` (or `$ARGUMENTS[0]`, `$ARGUMENTS[1]`) when you need to split individual tokens.

### 3. Add YAML frontmatter to constrain tools and improve discoverability

[YAML frontmatter](glossary.md#yaml-frontmatter) in a command file does two things: it restricts which tools Claude can invoke during that command's execution, and it provides the description shown in the `/` menu. Tool restriction is especially valuable for read-only audit commands — it enforces the boundary at the framework level, not just in the prompt text.[^1][^2]

**Example:**

```
# .claude/commands/security-check.md
---
allowed-tools: Read, Grep, Glob
description: Scan codebase for security vulnerabilities (read-only)
model: claude-opus-4-7
---

Analyze the codebase for security vulnerabilities including:
- SQL injection risks in database query construction
- Hardcoded secrets or API keys in source files
- Insecure configurations in settings files
- Missing input validation on public endpoints

Output findings grouped by severity: Critical, High, Medium, Low.
```

The `allowed-tools: Read, Grep, Glob` line guarantees Claude cannot write or execute anything — even if the prompt is ambiguous.

> **When to use:** Any command where unintended writes would be dangerous (security audits, dependency reviews, architecture checks). Also use `description` on every command so `/` browsing stays navigable as the library grows.
>
> **Pitfalls:** Omitting `allowed-tools` on commands that should be read-only. Claude will default to its full tool set if the field is absent. Explicit is always safer.

### 4. Choose directory structure based on complexity, not capability

As of Claude Code 2.1.3, commands and skills share the same framework. A file at `.claude/commands/deploy.md` and a file at `.claude/skills/deploy/SKILL.md` produce identical `/deploy` commands — same autocomplete, same frontmatter support (`context: fork`, `user-invocable`, `allowed-tools`), same behaviour. Existing files in either location continue to work without changes.[^4][^5]

The only meaningful difference is structure: the folder form (`.claude/skills/<name>/`) lets you co-locate supporting assets (templates, reference files, sub-prompts) alongside the skill definition. Use the flat file form for anything self-contained; use the folder form when the command needs to reference local files.

**Example — identical commands, different layouts:**

```
# Flat form — simple, self-contained
# .claude/commands/pr-review.md
---
name: pr-review
description: Review the current PR for bugs, style, and test coverage
allowed-tools: Read, Grep, Glob, Bash(gh pr diff *), Bash(gh pr view *)
---

## Current PR diff
!`gh pr diff`

Review for logic errors, missing tests, style inconsistencies, and security implications.
Provide actionable feedback ordered by priority.
```

```
# Folder form — when supporting files are needed
# .claude/skills/pr-review/SKILL.md
---
name: pr-review
description: Review the current PR for bugs, style, and test coverage
allowed-tools: Read, Grep, Glob, Bash(gh pr diff *), Bash(gh pr view *)
---

## Current PR diff
!`gh pr diff`

## Review checklist
!`cat .claude/skills/pr-review/checklist.md`

Review for logic errors, missing tests, style inconsistencies, and security implications.
```

> **When to use:** Start with the flat form in `.claude/commands/`. Migrate to the folder form only when you have real supporting files to co-locate — not speculatively.
>
> **Pitfalls:** Packing skill files with background context (architecture notes, philosophy, style guides). Skill files should describe *what to do*, not *why everything works*. Bloated definitions degrade reliability over time.

### 5. Use plan mode before executing high-risk changes

[Plan mode](glossary.md#plan-mode) puts Claude into a read-only state: it can explore the codebase and reason about changes, but it cannot write files or execute shell commands. Use it before touching production-critical paths, database migrations, or any task where you want to review scope before committing.[^6][^7][^8]

Press `Shift+Tab` twice from the default mode to cycle: `default → acceptEdits → plan`. You can also enter it directly with `/plan`.[^9]

**Example:**

```
# Press Shift+Tab twice, then type:
/plan refactor the authentication module to support OAuth2
      alongside the existing API key auth
```

Claude will read relevant files, identify affected paths, and present a step-by-step implementation plan — without touching anything. Discuss, adjust, iterate until satisfied, then exit plan mode and approve execution.

> **When to use:** Any task touching more than three files, any database migration, any change to authentication or authorization logic. Make `/plan` a habit before starting complex agentic tasks.
>
> **Pitfalls:** Skipping plan mode because the task "seems simple." Claude can misinterpret scope on ambiguous prompts and make wide changes before you can interrupt. Plan mode costs a few seconds and prevents hours of `/rewind`.

### 6. Inject live shell output into commands with `!` backtick syntax

Embed shell command output directly into a command's prompt before it reaches Claude by prefixing a backtick expression with `!`. This gives Claude up-to-date context (current git state, active errors, environment variables) without you having to copy-paste anything manually.[^1][^2]

**Example:**

```
# .claude/commands/smart-commit.md
---
allowed-tools: Bash(git add *), Bash(git status *), Bash(git commit *)
description: Create a conventional commit from current changes
---

## Current git status
!`git status`

## Staged diff
!`git diff --cached`

## Changed files
!`git diff --name-only HEAD`

Write a conventional commit message for the above changes.
Format: <type>(<scope>): <description>
Types: feat, fix, refactor, test, docs, chore

Stage all modified tracked files and commit.
```

The `!` expressions execute at invocation time — Claude receives their output, not the expression itself.

> **When to use:** Any command that needs runtime state: current branch, test results, open ports, environment flags. Also useful for injecting `cat pyproject.toml` or `python --version` to keep Claude aware of the active environment.
>
> **Pitfalls:** Commands that inject large outputs (full `git diff` on a large codebase) can fill the [context window](glossary.md#context-window) quickly. Scope the shell expressions tightly — `git diff --name-only` instead of `git diff`.

### 7. Use `context: fork` in skills to isolate research tasks from the main session

The `context: fork` frontmatter key runs the skill in a dedicated [subagent](primitives.md#agents) with its own context window. The skill executes independently, then returns a summary to the main session. Use this for research, audits, and analysis tasks that would otherwise flood the working context with intermediate output.[^4][^5]

**Example:**

```
# .claude/skills/security-audit/SKILL.md
---
description: "Conduct an autonomous security audit for secrets and vulnerabilities (runs in subagent)"
subagent: true
disable-model-invocation: false
---

# /security-audit
Conduct a thorough security audit of the codebase in a subagent. 

**Output Requirements:**
- Provide ONLY the final structured report in the main session.
- Do not stream intermediate file reads or tool outputs to the user.
- Include file paths, line numbers, and risk levels (Low/Medium/High).

**Scan Focus:**
1. Hardcoded credentials, API keys, and environment secrets.
2. SQL injection vectors (e.g., raw query string concatenation).
3. Missing authentication/authorization checks on routes.
4. Insecure deserialization or dangerous `eval()` patterns.
5. Exposed debug endpoints or verbose error handling.

**Constraints:**
- Use `grep`, `glob`, and `read` only.
- Do NOT use `write` or `edit` tools.
```

> **When to use:** Security audits, large-codebase searches, dependency vulnerability checks, any analysis that reads many files but only needs to return a compact result. Forked skills keep the main session's context clean.
>
> **Pitfalls:** Forked skills cannot write files in the main session's working tree directly. If the skill needs to produce an artifact, write it to a known path (e.g., `/tmp/audit-report.md`) and reference it from the main session.

### 8. Run `/simplify` after AI-generated code to catch redundancy

AI-generated code frequently contains unnecessary indirection, duplicate logic, and missed reuse opportunities. The [`/simplify`](glossary.md#simplify) built-in skill spawns three parallel review agents, each examining recent changes from a different angle, and then applies fixes.[^5][^10]

**Example:**

```
# After generating a new feature:
/review          # check for correctness and edge cases

# After fixing anything /review flagged:
/simplify        # catch redundancy and unnecessary complexity

# Focused variant — narrow the review scope:
/simplify error handling
/simplify reduce duplication in the repository layer
```

The typical post-generation sequence is: generate → `/review` for correctness → `/simplify` for quality. The two commands are complementary: `/review` finds bugs, `/simplify` finds bloat.

> **When to use:** After any significant AI-generated code block, after a refactoring session, before opening a pull request. Run it as a quality gate, not during active development.
>
> **Pitfalls:** Running `/simplify` on code you haven't reviewed yet. It optimises what exists — if the underlying logic is wrong, simplification just makes the wrong code cleaner.

### 9. Use `/loop` for background monitoring during long sessions

The `/loop` built-in skill runs a prompt repeatedly on a schedule while the session remains open. Give it an interval and a monitoring task; it fires at that cadence without requiring you to switch focus.[^5]

**Example:**

```
# Watch the dev server for new errors every 5 minutes:
/loop 5m check dev server logs at /tmp/server.log for new errors since last check

# Run the test suite every 10 minutes and report failures:
/loop 10m run pytest tests/ -x --tb=short and report any new failures

# Monitor a long-running build:
/loop 2m check if the Docker build process has completed or errored
```

The interval is parsed from the first token (`5m`, `10m`, `1h`). The rest of the line becomes the recurring prompt.

> **When to use:** Long sessions where you want background visibility without switching terminals — watching a staging deploy, monitoring a test suite during a refactor, tailing error logs while implementing a fix.
>
> **Pitfalls:** Forgetting that `/loop` consumes tokens at every interval. An expensive prompt running every 2 minutes across a 3-hour session adds up. Use targeted, specific prompts — not broad codebase sweeps.

### 10. Schedule skills in headless mode via cron for unattended automation

Claude Code's `--print` flag runs a session non-interactively and exits — no terminal required. Combined with a scheduled skill invocation, this turns any command into a recurring automated job. Use `--dangerously-skip-permissions` only in sandboxed environments where the skill's tool access has already been reviewed.[^11][^10]

**Example:**

```bash
# crontab -e entry — daily report at 07:00
0 7 * * * /usr/local/bin/claude --print \
    "Run /project:generate-daily-report" \
    --dangerously-skip-permissions \
    >> /var/log/claude-reports/daily.log 2>&1
```

```bash
# Shell script: run a skill and pipe output to Slack
#!/usr/bin/env bash
set -euo pipefail

RESULT=$(claude --print \
    "Run /project:summarize-test-failures /tmp/latest-test.log" \
    --dangerously-skip-permissions)

curl -s -X POST -H 'Content-type: application/json' \
    --data "{\"text\": \"${RESULT}\"}" \
    "${SLACK_WEBHOOK_URL}"
```

> **When to use:** Nightly codebase audits, daily status reports, post-deploy verification checks, any skill that should run on a schedule without a developer present.
>
> **Pitfalls:** Using `--dangerously-skip-permissions` without first running the skill interactively and reviewing every tool action it takes. Headless skills with write access and ambiguous instructions can cause real damage. Always test interactively first, log all headless output, and restrict `allowed-tools` in the skill's frontmatter.

## Related themes

- [CLAUDE.md & project memory](claudemd-setup.md) — commands encode your best prompts; CLAUDE.md encodes your project rules; both belong in version control and they work together to give Claude consistent, project-specific behaviour
- [Hooks & automation](hooks-automation.md) — [hooks](primitives.md#hooks) can trigger skills automatically on lifecycle events; combining hooks with skills produces fully automated workflows that require no manual invocation
- [Prompting strategies](prompting-strategies.md) — the best ad-hoc prompts are the ones worth crystallising into commands; commands enforce consistent prompting across the team without relying on individual memory

---

[^1]: [Slash commands in the SDK](references.md#slash-commands)
[^2]: [Creating reusable shortcuts with custom slash commands](references.md#creating-custom-slash-commands)
[^3]: [Claude Code deep dive: slash commands](references.md#claude-code-deep-dive-slash-commands-9cd6ff4c33cb)
[^4]: [Claude Code skills vs slash commands: when to use each](references.md#claude-code-skills-vs-slash-commands)
[^5]: [Essential Claude Code skills and commands](references.md#essential-claude-code-skills-and-commands)
[^6]: [10 essential Claude Code best practices you need to know](references.md#174731)
[^7]: [The complete developer's guide to Claude Code commands](references.md#claude-code-commands-guide)
[^8]: [Claude Code cheatsheet](references.md#14553413-claude-code-cheatsheet)
[^9]: [5 Claude Code agentic workflow patterns](references.md#claude-code-agentic-workflow-patterns)
[^10]: [Claude Code best practices: 12 patterns agentic engineers use](references.md#claude-code-best-practices-12-patterns-agentic-engineers-use)
[^11]: [How to use Claude Code skills to automate repetitive workflows](references.md#claude-code-skills-automate-workflows)
