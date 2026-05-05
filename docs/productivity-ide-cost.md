# Productivity, IDE & cost

[← Back to index](index.md)

The compounding returns in Claude Code come from small, repeatable habits — not from any single trick. This theme covers the mechanics of working efficiently: cycling permission modes without breaking flow, monitoring token spend before it surprises you, choosing the right model for each task, configuring your IDE for zero-friction context sharing, and keeping [context compaction](primitives.md#context-compaction) predictable. Each tip here saves minutes per session; across hundreds of sessions, that adds up to days. None of these require advanced setup — but most developers using Claude Code daily have never touched them.

**Level:** Basic

## Tips

### 1. Use Shift+Tab to cycle permission modes without typing

[Plan mode](primitives.md#plan-mode) and acceptEdits mode are your two most powerful session-management tools, and Shift+Tab is the fastest way to move between them. Each press cycles through: `default → acceptEdits → plan`. No command to type, no menus to open.[^1]

The highest-leverage pattern: start every non-trivial session in plan mode (press Shift+Tab twice from default). Review the proposed approach, catch misunderstandings early, then press Shift+Tab once to drop into acceptEdits for hands-off execution. You only need to confirm shell commands — file edits happen automatically.[^2]

**Example:**

```bash
# Launch Claude Code (defaults to 'default' mode)
claude

# Press Shift+Tab twice → enters plan mode
# Claude proposes an approach; you review without any files changing

# Press Shift+Tab once → enters acceptEdits mode
# Claude executes; file edits auto-approved, shell commands still prompt
```

> **When to use:** At the start of any session touching more than one file, or when you're unsure whether Claude's interpretation matches your intent.
>
> **Pitfalls:** Skipping plan mode and heading straight to acceptEdits means the first wrong move is also the first executed move. If Claude misunderstands the task, it has already written files before you can intervene.

### 2. Monitor spend with `ccusage` — not just `/cost`

The built-in `/cost` command shows total session spend. [ccusage](glossary.md#ccusage) shows you per-day breakdowns, per-model breakdowns, and a live view of your current 5-hour billing window — the information you need to spot expensive patterns before they repeat.[^3]

Install once, use throughout:

**Example:**

```bash
npm install -g @ryoppippi/ccusage

# Daily breakdown (most useful for habit-building)
ccusage daily

# Live view of the current 5-hour billing window
ccusage blocks --live

# Monthly aggregation for budget tracking
ccusage monthly

# Per-model cost breakdown for a date range
ccusage daily --breakdown --since 20260101 --until 20260131
```

> **When to use:** Run `ccusage daily` at the end of each working day for a week after adopting any new Claude Code habit. The before/after comparison is the fastest way to verify whether a technique is actually saving tokens.
>
> **Pitfalls:** Relying solely on `/cost` gives you session totals but hides which model, which task type, and which time of day drives your spend. Without per-model visibility, model selection optimisations (see tip 4) are invisible.

### 3. Use prompt caching to cut costs on repeated large contexts

[Prompt caching](glossary.md#prompt-caching) is enabled by default in Claude Code. When the same content appears at the start of consecutive requests — your [CLAUDE.md](primitives.md#claude-md), system prompts, stable architecture docs — Claude caches it after the first use and charges approximately 10% of the normal input token rate on subsequent hits.[^4]

The compounding effect is significant: a 2,000-token CLAUDE.md loaded across 100 sessions per month costs 200,000 tokens without caching and roughly 22,000 tokens with it (first load + 99 cached loads at 10%). On Sonnet API pricing, that difference is approximately $5.40 saved per month on one file alone.[^5]

**Example:**

```bash
# Verify caching is active (it is by default — only disable for debugging)
# To disable globally for a single session:
export DISABLE_PROMPT_CACHING=1

# To see cache hit behaviour, watch the token breakdown in /cost:
# "cache_read_input_tokens" > 0 means caching is working

# Keep CLAUDE.md stable during sessions to preserve cache validity:
# Edit CLAUDE.md between sessions, not mid-session — edits invalidate the cache
```

> **When to use:** Always. This is on by default. The actionable habit is keeping CLAUDE.md stable within a session and putting frequently-referenced content there rather than pasting it into each prompt.
>
> **Pitfalls:** Editing CLAUDE.md mid-session invalidates the cache for that file, costing you full-price tokens for the rest of the session. Make CLAUDE.md changes between sessions.

### 4. Default to Sonnet; drop to Haiku for reviews and tests; use Opus sparingly

Model selection is the highest single-variable cost lever. Sonnet handles 80% of daily development work. Haiku costs roughly 70% less than Sonnet and is sufficient for code review, test generation, linting commentary, and quick lookups. Opus is appropriate for complex architecture decisions, subtle debugging across many files, or tasks where correctness on the first attempt saves significant rework cost.[^6]

**Example:**

```bash
# Switch models mid-session with /model
/model claude-haiku-4-5

# Or pass the model flag at session start
claude --model claude-haiku-4-5 "Review src/auth/middleware.py for obvious bugs"

# Back to Sonnet for implementation
claude --model claude-sonnet-4-6 "Implement the token refresh logic in src/auth/tokens.py"

# Opus only for hard problems
claude --model claude-opus-4-6 "Design the caching layer for this distributed system"
```

> **When to use:** Set Sonnet as your default. Before starting a review or test-generation task, switch to Haiku. Before a complex multi-file architectural discussion, switch to Opus and switch back when done.
>
> **Pitfalls:** Leaving the session on Opus after finishing a hard planning task is a common expensive habit. One 5,000-token Opus response costs what 18 equivalent Haiku responses would. Always switch back. Also note: the `opusplan` model alias uses Opus during plan mode and automatically drops to Sonnet for execution — a useful hybrid if you want Opus-quality planning without paying Opus rates for every line written.[^7]

### 5. Use the VS Code and JetBrains extensions for inline diffs and context sharing

The IDE extensions eliminate the most common flow-breaking habit: context switching between editor and terminal to describe what you're looking at. With the extension installed, Claude sees your current file, selected text, and error messages from the Problems panel automatically.[^8]

Key VS Code shortcuts added by the extension:

| Shortcut (macOS / Windows) | Action |
|---|---|
| `Cmd+Esc` / `Ctrl+Esc` | Toggle focus between editor and Claude |
| `Option+K` / `Alt+K` | Insert `@filename#line-range` reference for current selection |
| `Cmd+Shift+Esc` / `Ctrl+Shift+Esc` | Open conversation in new tab |
| `Cmd+N` / `Ctrl+N` | Start new conversation (when Claude is focused) |

**Example:**

```bash
# Install the extension from the VS Code marketplace:
# Search "Claude Code" in Extensions (Ctrl+Shift+X / Cmd+Shift+X)

# Or launch Claude from within VS Code's integrated terminal —
# the extension auto-installs on first run:
claude

# With code selected in the editor, press Alt+K (Win/Linux) or Option+K (macOS)
# to insert a precise reference into your prompt:
# @src/auth/middleware.py#42-67
```

> **When to use:** Any time you're working in VS Code or a JetBrains IDE. The extension is a zero-config improvement — install it once and the context sharing works automatically.
>
> **Pitfalls:** Without the extension, developers habitually paste entire file contents into the prompt instead of referencing them, which pushes stale file versions into the [context window](glossary.md#context-window) and increases costs unnecessarily.

### 6. Reference specific line ranges with `@filename#L5-10` syntax

The `@filename` reference syntax tells Claude to read a file. The `@filename#5-10` variant narrows the read to specific lines, keeping irrelevant context out of the prompt entirely. In the VS Code extension, pressing `Option+K` / `Alt+K` with a selection active auto-inserts the full `@filename#start-end` reference — no typing required.[^9]

**Example:**

```bash
# Reference a specific function by line range
@src/auth/middleware.py#42-67 Why does this token validation sometimes fail on refresh tokens?

# Reference a class definition without pulling in the entire module
@src/models/user.py#1-35 Does this dataclass handle nullable fields correctly?

# In the terminal, use @ references in any prompt:
claude "@src/api/routes.py#88-120 This endpoint returns 500 on empty payloads — find why"
```

> **When to use:** Whenever you know which section of a file is relevant. Don't ask Claude to read a 500-line file to answer a question about 10 lines.
>
> **Pitfalls:** Over-narrowing is also possible. If the bug stems from an interaction between the function you referenced and a caller you didn't include, Claude won't see the full picture. Use line-range references for targeted questions; use full-file references for understanding relationships.

### 7. Set up custom keybindings for common operations

Claude Code's [keybindings.json](glossary.md#keybindings-json) file (at `~/.claude/keybindings.json`) lets you rebind any action in any context. High-value bindings to set up: fast-mode toggle, external editor open, and any workflow-specific actions you invoke repeatedly. Run `/keybindings` inside a session to create or open the file.[^10]

**Example:**

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "$docs": "https://code.claude.com/docs/en/keybindings",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+e": "chat:externalEditor",
        "meta+o": "chat:fastMode",
        "meta+t": "chat:thinkingToggle",
        "ctrl+u": null
      }
    },
    {
      "context": "Global",
      "bindings": {
        "ctrl+t": "app:toggleTodos"
      }
    }
  ]
}
```

> **When to use:** After your first week of regular Claude Code usage, when you know which actions you reach for most. Don't optimise keybindings before you know your actual patterns.
>
> **Pitfalls:** `Ctrl+C`, `Ctrl+D`, and `Ctrl+M` are reserved and cannot be rebound. Some shortcuts conflict with tmux (`Ctrl+B`) and GNU screen (`Ctrl+A`) — check `/doctor` if bindings don't take effect as expected.

### 8. Set `MAX_THINKING_TOKENS=10000` to cap extended thinking costs

[Extended thinking](glossary.md#extended-thinking) is the single largest token-spend lever in Claude Code. The default budget is uncapped, and on complex tasks it can run into tens of thousands of output tokens per response — at output token pricing, which is 5x the input rate. Setting [MAX_THINKING_TOKENS](glossary.md#max-thinking-tokens) to 10,000 caps deep reasoning cost without breaking the majority of tasks.[^11]

Community data from developers tracking spend confirms this as the highest-impact single change for reducing API costs — reported to cut thinking-related spend by 30–40%.[^4]

**Example:**

```bash
# Add to your shell profile (~/.zshrc or ~/.bashrc) for a persistent cap:
export MAX_THINKING_TOKENS=10000

# Or set per-session before launching:
MAX_THINKING_TOKENS=10000 claude

# Alternatively, use the /effort command to dial reasoning per-task:
/effort low   # Minimal reasoning, fast responses, cheap
/effort high  # Full extended thinking, for genuinely hard problems

# Toggle extended thinking on/off with Meta+T (Alt+T on Windows/Linux)
```

> **When to use:** Set it once in your shell profile and leave it. Override with `/effort high` for architecture decisions, hard debugging sessions, or any task where the quality difference is real.
>
> **Pitfalls:** Setting `MAX_THINKING_TOKENS` too low (under 5,000) degrades quality on multi-step reasoning tasks in ways that aren't obvious until you compare outputs. 10,000 is a well-validated threshold across the community.

### 9. Compact at session-defined milestones, not ad hoc

Reactive [context compaction](primitives.md#context-compaction) — running `/compact` when Claude starts forgetting things — is too late. By that point, context rot has already degraded response quality and the summary is compressing a degraded signal. The better pattern is proactive compaction at a milestone you define in advance: after each feature, after each PR, or after every 30 minutes of active work.[^12]

The timing of `/compact` also matters relative to prompt cache state. `/compact` runs cheapest when the cache is warm — within roughly five minutes of your last message. If you've been away longer, use `/clear` instead and restart fresh.[^4]

**Example:**

```bash
# Compact with optional preservation instructions to control what survives:
/compact Keep: the authentication refactor decisions, the error handling pattern we settled on, and the list of files we've touched. Discard: all intermediate reasoning and the initial exploration of approaches we rejected.

# Personal milestone rule (add to CLAUDE.md as a session norm):
# /compact after every 2 files modified, or every 30 minutes of active work

# To check context fill level before deciding compact vs clear:
/context

# Rule: active session growing large → /compact
#       switching to unrelated task → /clear
```

> **When to use:** Set a milestone rule before starting a session. "I will compact after completing the auth module" is more reliable than "I will compact when things feel slow."
>
> **Pitfalls:** Running `/compact` reactively after you notice degraded responses means the summary is generated from a context that's already partially compressed — the least useful time to compact. Run it while the context is still clean and coherent.

### 10. Run multiple Claude sessions in parallel with tmux or split terminals

Claude Code is designed for parallel use. While one session thinks or executes a long task, you can make progress in another. This is the terminal equivalent of pair programming across multiple workstreams — and unlike git worktrees (which add branch isolation), it requires zero setup beyond a terminal multiplexer.[^13]

**Example:**

```bash
# Set up a three-pane tmux layout:
tmux new-session -s work
tmux split-window -h   # Vertical split → two panes
tmux split-window -v   # Horizontal split of right pane → three panes

# Pane 1: Feature implementation
claude
# > Implement the OAuth callback handler in src/auth/oauth.py

# Pane 2: Test generation (running in parallel while pane 1 executes)
claude
# > Write pytest tests for src/auth/tokens.py covering expiry edge cases

# Pane 3: Documentation or review
claude
# > Review the diff in src/api/routes.py for security issues

# Alias for quick multi-session launch (add to ~/.zshrc):
alias c='claude'
alias cc='claude --continue'
alias cr='claude --resume'
```

> **When to use:** Any time you have a task that runs for more than 30 seconds — tests, large refactors, codebase exploration. Don't wait for it to finish before starting the next task.
>
> **Pitfalls:** Keep parallel sessions scoped to independent work. Two sessions editing the same file simultaneously will produce conflicting changes. Use git branches or separate directories to isolate parallel work if the scopes overlap.

## Related themes

- [Context management](context-management.md) — milestone-based compaction (tip 9) is a session strategy; context management covers the underlying mechanics of context windows, compaction triggers, and handoff documents
- [Parallel development](parallel-development.md) — tmux parallel sessions (tip 10) scale directly into full worktree-based parallel development with branch isolation and independent file trees
- [Prompting strategies](prompting-strategies.md) — line-range references (tip 6) are a prompting technique as much as an IDE feature; both themes converge on reducing wasted tokens through precise, scoped requests

---

[^1]: [Claude Code cheatsheet](references.md#14553413-claude-code-cheatsheet)
[^2]: [Claude Code commands guide](references.md#claude-code-commands-guide)
[^3]: [Usage optimization](references.md#usage-optimization)
[^4]: [Reduce Claude Code costs 60% with these four habits](references.md#claude-code-cost-optimisation)
[^5]: [Claude Code token optimization](references.md#claude-code-token-optimization)
[^6]: [Claude Code best practices: 12 patterns agentic engineers use](references.md#claude-code-best-practices-12-patterns-agentic-engineers-use)
[^7]: [Claude Code token limits and cost optimization](references.md#claude-code-token-limits-cost-optimization-apac-teams)
[^8]: [Claude Code Part 7: IDE integration with VS Code and JetBrains](references.md#2025-08-05-claude-code-part-7-ide-integration-vscode-jetbrai)
[^9]: [IDE integration](references.md#ide-integration)
[^10]: [Customize keyboard shortcuts](references.md#keybindings)
[^11]: [10 tips to stop burning your tokens in Claude Code](references.md#10-tip-to-stop-burning-your-tokens-in-claude-code-4776d4ac89)
[^12]: [How to use the /compact command in Claude Code](references.md#claude-code-compact-command-context-management)
[^13]: [My top 10 Claude Code tips from 11 months of intense usage](references.md#my-top-10-claude-code-tips-from-11-months-of)
