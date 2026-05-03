# The Complete Developer's Guide to Claude Code Commands

**Type:** article
**URL:** https://timdietrich.me/blog/claude-code-commands-guide/
**Topic:** Productivity & Keyboard Shortcuts
**Published:** unknown

## Content

# The Complete Developer's Guide to Claude Code Commands | Tim Dietrich
[Skip to main content](https://timdietrich.me/blog/claude-code-commands-guide/#main-content)

[Tim Dietrich](https://timdietrich.me/)
*   [Home](https://timdietrich.me/)
*   [Services](https://timdietrich.me/services/)
*   [Products](https://timdietrich.me/products/)
*   [Resources](https://timdietrich.me/resources/)
*   [Blog](https://timdietrich.me/blog/)
*   [Contact](https://timdietrich.me/contact/)

# The Complete Developer's Guide to Claude Code Commands

Published on March 2, 2026

[AI](https://timdietrich.me/blog/?tag=AI)

[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) has quietly become one of the most capable AI coding tools available. Yet most developers are only scratching the surface. They know how to type a prompt and accept a suggestion, but the real power lies in the command system.

This guide covers every major slash command, CLI flag, and keyboard shortcut, grouped so you can build from the everyday essentials to the advanced capabilities that most users never find.

### The Daily Essentials

These are the commands you'll reach for every session. Master these first.

**`/compact`** is the token lifesaver. When a long session fills the context window, `/compact` compresses the conversation history into a dense summary. You can pass instructions to steer what it retains: `/compact Focus on the auth module and current test failures`. Without it, long sessions hit the context ceiling abruptly or force you to start fresh. Use it when context usage exceeds 80%, or whenever you see the "context is getting large" warning.

**`/clear`** (also `/reset` or `/new`) is the hard reset. It wipes the conversation history entirely and frees all context. Use it at task boundaries when you're switching to something unrelated. The key distinction: `/compact` summarizes and maintains awareness. `/clear` resets completely.

**`/model`** lets you switch models mid-session without losing your conversation. `/model sonnet` for exploration and file reading, `/model opus` when you hit a genuinely complex problem. Switch back once the hard part is solved. This can reduce token costs significantly without sacrificing quality where it counts.

**`/diff`** opens an interactive diff viewer showing all changes made during the session. You can toggle between a full git diff and per-turn diffs, and navigate between files with arrow keys. The per-turn view is especially useful: it shows what changed at each step, making it easy to isolate when a particular modification happened. Make this a habit before every commit.

**`/cost`** (for API users) and **`/stats`** (for Pro/Max subscribers) show what you're spending. A single agentic loop can burn through tokens faster than you'd expect. Checking regularly builds intuition for which tasks are expensive and helps you decide when to switch models or compact context.

### Session Management

These commands let you work across multiple tasks without losing context.

**`/resume`** (also `/continue`) picks up where you left off. Without arguments, it opens a session picker. With a name, it jumps directly there. From the CLI: `claude -c` resumes the most recent session, `claude -r "name"` resumes by name. Real development involves constant context-switching. `/resume` means you never have to re-explain what you were doing.

**`/rename`** gives your sessions meaningful names. Without arguments, it auto-generates one from the conversation context. Without names, your session history is an indecipherable list of timestamps. With them, you can find "auth-refactor" weeks later and pick up immediately.

**`/fork`** creates a branch of the current conversation at its current state. You can explore one approach, then `/resume` back to the fork point and try a different one. This is genuinely underused. It's the conversational equivalent of a git branch: you get to experiment without destroying a working state.

**`/export`** exports the conversation as plain text, useful for documentation, postmortems, or sharing a session's output with a teammate.

### The Hidden Gems

This is where most developers' knowledge ends, but it's also where Claude Code gets genuinely interesting.

**`/rewind`** (also `/checkpoint`, or double-tap `Esc`) lets you roll back the conversation to a previous point. The selective rollback option is the key feature: you can choose "Rewind code only" to revert all file changes while keeping the conversation history intact. Try an aggressive refactoring approach, discuss the results, decide it didn't work, then revert only the code while keeping the diagnostic conversation. No more `git stash` gymnastics.

**`/plan`** (also toggled via `Shift+Tab`) puts Claude in read-only mode. It can read files and analyze your codebase but can't make changes. All proposed modifications are presented as plans requiring explicit approval. Use this for production-critical files, database migrations, and any task where you want to understand the scope before committing. The Claude Code team themselves recommend planning before implementing.

**`/insights`** reads your past month of usage and compiles a detailed HTML report covering patterns, costs, tool usage, and session history. Most developers have no data on how they actually use AI coding tools. Running this once a month surfaces the information you need to improve your workflow.

**`/security-review`** analyzes changes on your current git branch specifically for security vulnerabilities. Not a general code review. Scoped and targeted. Run it before opening any PR that touches authentication, authorization, data handling, or external integrations.

**`/simplify`** runs a three-agent review pipeline checking for architectural issues, duplicate logic, and performance inefficiencies. Designed as a quality gate before PRs, not during active development. Claude writes code fast, but fast isn't always clean. This catches the accumulated complexity that creeps in across many turns.

**`/batch`** runs large-scale changes across multiple files in parallel using isolated git worktrees, then automatically creates pull requests. Before this, applying a pattern change across 50 files meant writing a bespoke script. Now it's a single command.

**`/btw`** lets you ask a side question without it becoming part of the main conversation thread. Claude answers, and the thread continues from where it was. Useful when you're deep in a debugging session and need a quick conceptual clarification without adding noise to the context.

**`/remote-control`** (also `/rc`) enables remote control of your local Claude Code session from [claude.ai](https://claude.ai/). Long-running tasks don't require you to be at your desk. Monitor progress, send instructions, and review results from anywhere.

### Project Configuration

These commands manage how Claude Code understands and interacts with your project.

**`/init`** analyzes your project and generates a `CLAUDE.md` file, the configuration that persists project-specific rules, conventions, and context across all sessions. Without it, you re-explain your project's conventions every time. With it, Claude always knows your stack, testing framework, and coding standards.

**`/memory`** opens the `CLAUDE.md` editing interface for adding, updating, or removing project rules. Worth investing 10 minutes after project setup. It pays back in every subsequent session.

**`/hooks`** manages automation that triggers on tool events: before file edits, after bash commands, on session start. The critical difference between hooks and prompts: hooks guarantee execution, prompts merely suggest it. If you need linting after every file write, hooks are the right mechanism. Recent versions also support HTTP hooks for external service integrations.

**`/permissions`** and **`/allowed-tools`** control which tools Claude can use and what file paths are permitted. Essential for CI/CD pipelines and security-sensitive environments where you want to restrict the blast radius.

**`/agents`** manages subagent configurations: specialized Claude instances with their own context windows, personas, and tool access. Complex tasks benefit from delegation. A "code-reviewer" subagent paired with a "debugger" subagent produces better results than a single generalist handling everything in one context window.

### CLI Flags for Scripting and Automation

These flags are set when launching Claude Code from the terminal and are essential for CI/CD integration.

**`--print` / `-p`** sends a query and exits without starting an interactive session. This is the gateway to scripting: `claude -p "Explain this repository" > overview.txt`. Paired with `--output-format json`, it makes Claude's output machine-readable and composable with other tools.

**`--worktree` / `-w`** creates an isolated git worktree and starts a session inside it. Changes are isolated from your main branch. Worktrees are automatically cleaned up if no changes are made. The `/batch` command uses this internally.

**`--allowedTools`** limits which tools Claude can use in a given session. For automated analysis where you want read-only behavior: `claude -p --allowedTools "Read" "Grep" "Glob" "Find issues in this codebase"`.

**`--max-turns`** caps the number of agentic turns before stopping. A circuit breaker for automated pipelines where runaway execution would be costly.

**`--agents`** defines custom subagents inline at launch without requiring configuration files. Useful for CI/CD pipelines where you want to define agent behavior in the pipeline config rather than checked-in files.

### Keyboard Shortcuts Worth Memorizing

*   **`Shift+Tab`** (or `Alt+M`) cycles through Normal, Auto-Accept, and Plan modes without typing a command. These mode switches happen constantly during productive sessions.
*   **`!` prefix** runs a bash command immediately, bypassing Claude's interpretation. `! git status` executes and puts raw output in context without Claude narrating the command. Fewer tokens, faster results.
*   **`@`** triggers intelligent file path completion. `@src/components/Header.tsx Fix the responsive layout` is faster than describing the file and waiting for Claude to find it.
*   **`Esc` + `Esc`** opens the rewind menu, including selective code-only or conversation-only rollback.
*   **`Alt+P`** switches the active model while preserving whatever you've typed in the input field.
*   **`Alt+T`** toggles extended thinking (deep reasoning mode) for the next turn. Run `/terminal-setup` first to activate this in your terminal.

### Session Health Check

A set of commands worth running as a regular check-in during long sessions:

```
/cost      # (API users) How much have I spent?
/stats     # (Pro/Max users) How much have I used?
/context   # How full is my context window?
/usage     # Am I near my rate limit?
```

If costs are climbing, use `/compact` to reduce context or switch to Sonnet with `/model sonnet`. If you're near the rate limit, check `/extra-usage` to configure what happens when you hit the ceiling.

### Closing Thoughts

The developers getting the most out of Claude Code aren't necessarily writing better prompts. They're using the command system deliberately. They compact context before it overflows, switch models based on task complexity, use Plan Mode before touching critical files, and name their sessions so they can resume them.

The less-known commands, `/fork` for safe experimentation, `/rewind` for selective rollback, `/insights` for understanding your own patterns, `/batch` for large-scale changes, `/remote-control` for working from anywhere, represent the gap between casual use and genuine productivity leverage.

Start with the daily essentials. Build habits around `/compact`, `/diff`, and `/cost`. Then add the advanced commands one by one as you encounter situations where they'd help. The system is extensive, but it was designed to be discovered incrementally, and each new command you internalize makes the whole tool meaningfully more powerful.

_For the most current command reference, type `/help` inside Claude Code or check the [official documentation](https://docs.anthropic.com/en/docs/claude-code/overview)._

### Related Posts

[Designing How AI Thinks: An Introduction to Cognitive Systems Design](https://timdietrich.me/blog/designing-how-ai-thinks/)
April 12, 2026

[Improve Vendor Rebate Management With AI](https://timdietrich.me/blog/improve-vendor-rebate-management-with-ai/)
April 8, 2026

[Yeah, We Use AI. So What.](https://timdietrich.me/blog/yeah-we-use-ai-so-what/)
March 29, 2026

[← Back to all posts](https://timdietrich.me/blog/)

© 2026 Tim Dietrich

[See what I'm working on now](https://timdietrich.me/now/), or view my [resume](https://timdietrich.me/resume/).
