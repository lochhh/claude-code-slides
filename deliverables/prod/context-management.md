# Context management

[← Back to index](index.md)

[Context rot](glossary.md#context-rot) is the root cause of the "hitting the ceiling" problem. As a session grows, Claude's older foundational decisions — the ones that define your architecture, your constraints, your in-progress bugs — get compressed or discarded while recent noise stays sharp. Engineers who understand the [context model](primitives.md#context-model) and treat compaction, clearing, and phase boundaries as first-class workflow tools maintain Claude's quality across arbitrarily long sessions. Those who wait for warning signs are already past the point of clean recovery.

**Level:** Intermediate

## Tips

### 1. Compact at ~60% context utilization — before warnings appear

[Context utilization](glossary.md#context-utilization) degrades silently before the hard limit. The 80% warning in the UI is a lagging indicator: by the time it fires, the foundational context from early in your session has already been partially compressed.[^1] Monitor with `/statusline` and run [/compact](glossary.md#compact) proactively at 60%.

**Example:**
```text
# Check context status
/statusline

# Context shows 58% — compact now, not at 80%
/compact
```

> **When to use:** Any session lasting more than 30–45 minutes on a non-trivial task. Make it habitual: every time `/statusline` crosses 60%, stop and compact before continuing.[^2]
>
> **Pitfalls:** Treating the 80% warning as the trigger. By that point, the session summary Claude produces will already be working from compressed material. The quality of the compaction summary depends directly on the quality of the context being summarized.

---

### 2. Append explicit preservation instructions to `/compact`

Without preservation instructions, Claude decides what survives compaction based on recency, relevance, and frequency. Architectural decisions made early in a session — mentioned once, never repeated — are prime candidates for loss.[^3] Append a targeted list to `/compact` to anchor the summary around what actually matters.

**Example:**
```text
/compact Keep: (1) decision to use PostgreSQL not SQLite and why, (2) the three functions identified for refactoring in payments.py, (3) current unresolved KeyError in auth.py line 142, (4) completed modules: auth.py, middleware.py. Clear: grep output, file reads (re-fetchable).
```

Four categories worth preserving explicitly:
- Architectural decisions (choices that can't be reconstructed from code alone)
- Active bugs (what you're mid-way through debugging)
- File and scope context (what's in scope, what's deliberately excluded)
- Constraints (compatibility requirements, API surface limits, client mandates)[^1]

> **When to use:** Every compaction where your session contains a decision or in-flight problem that was discussed early and not repeated recently.
>
> **Pitfalls:** Over-specifying. If your preservation instruction is three paragraphs, you're preserving noise alongside signal. Aim for five to ten items at most. The goal is a lean, high-signal summary — not a verbatim record.

---

### 3. Verify state immediately after compaction

After [context compaction](primitives.md#context-compaction), Claude's working state has changed. A 30-second state check catches dropped context while it's still fresh and correctable.[^1]

**Example:**
```text
# Immediately after /compact completes:
Summarize where we are and what we're working on next.
```

If the summary omits a critical decision or the in-progress bug, correct it in the same turn. Adding context back immediately is cheap; discovering the omission three turns later is not.

> **When to use:** After every compaction, without exception.
>
> **Pitfalls:** Skipping the check because "it probably got it." The most expensive dropped context is the kind you don't notice until Claude produces code that contradicts a decision made an hour ago.

---

### 4. Use post-compaction hooks to re-inject critical rules automatically

[CLAUDE.md](primitives.md#claude-md) is part of the conversation context — after compaction, it gets summarized alongside everything else. Project conventions mentioned once at session start are exactly what gets compressed.[^3]

The most reliable fix is a single `@`-import line in CLAUDE.md pointing to a tight context-essentials file. Claude re-reads it at session start and after any compaction event restores the file to context.[^4]

**Example — `.claude/context-essentials.md`:**
```markdown
# Context Essentials (Re-injected After Compaction)

## Critical Rules
- Use dateutil for ALL date parsing — never datetime.strptime directly
- Database: execute read queries only via db.execute_read(); writes require db.transaction()
- Quality gates: pytest && ruff check && mypy before any commit
- Auth: always validate tokens in middleware — never accept user_id from request body

## Banned Patterns
- No bare except clauses
- No SELECT * — always specify columns
- No --no-verify on git operations
```

**Example — `CLAUDE.md` import line:**
```markdown
@.claude/context-essentials.md
```

Keep the essentials file under 50 lines. Every line costs tokens on every turn where it is active.

Alternatively, use a `PostCompact` [hook](primitives.md#hooks) in `.claude/settings.json` to `cat` the file:[^5]

```json
{
  "hooks": {
    "PostCompact": [
      {
        "type": "command",
        "command": "cat \"${CLAUDE_PROJECT_DIR}/.claude/context-essentials.md\""
      }
    ]
  }
}
```

> **When to use:** Any project with enforced conventions (linting, auth patterns, banned imports). Set it up once per project, then stop thinking about it.
>
> **Pitfalls:** Attempting to use `PostToolUse` with `"matcher": "compact"` — `/compact` is a slash command, not a tool call, so `PostToolUse` never fires for it. Use `PostCompact` or the `@`-import approach instead.[^4]

---

### 5. Use phase-based sessions — clear between major work phases

Carrying a full conversation history into a new work phase is expensive and noisy. Each phase — architecture, implementation, testing, review — benefits from a clean context window seeded with only what the next phase needs.[^6]

**Example — ending an architecture phase:**
```text
# In the current session, ask Claude to produce a handoff:
Write a summary of all decisions made this session to HANDOFF.md.
Include: chosen data model, auth approach, API surface, constraints, and open questions.
```

Then start a fresh session:
```text
# First message of the new session:
Read HANDOFF.md. We're now implementing the auth module based on those decisions.
```

A phase summary as the first message of a new session is cheaper than carrying the whole history, and produces better results because Claude's attention isn't diluted by irrelevant prior turns.[^7]

> **When to use:** Any time you transition between distinct phases of work — especially architecture-to-implementation and implementation-to-testing.
>
> **Pitfalls:** Treating phase boundaries as optional. The discomfort of starting a new session is outweighed by the quality gain from a clean context. If the transition feels painful, the handoff document is too thin.

---

### 6. Distinguish re-fetchable data from irreplaceable information

Not all context is equally important to preserve. File contents, grep output, and API responses can be re-fetched on demand. Architectural decisions, discovered constraints, and mid-debug state cannot.[^1]

This distinction should drive both what you include in preservation instructions and when you use tool-result clearing.[^8]

**Example — targeted compaction:**
```text
/compact Keep: decision to use Redis for session caching instead of database (performance reason). Clear: grep output from earlier file scan (can be re-run), file reads of config.py and models.py (re-fetchable).
```

**Example — tool-result clearing via API (for agent workflows):**
```python
import anthropic

client = anthropic.Anthropic()

# After a heavy file-read pass, clear old tool results
# while keeping the agent's reasoning and decisions intact
response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    messages=messages,
    context_management={
        "type": "clear_tool_uses_20250919",
        "trigger": 100000,
        "keep": 3,  # keep last 3 tool results, clear the rest
    },
    betas=["context-management-2025-06-27"],
)
```

> **When to use:** Before any compaction. Spend 30 seconds categorizing what's in context before writing preservation instructions.
>
> **Pitfalls:** Treating all context as equally valuable and trying to preserve everything. That defeats the purpose. The constraint is real: you cannot preserve everything, so preserving decisions at the expense of re-fetchable data is always the right trade-off.

---

### 7. Use `/rewind` when Claude drifts — don't correct within the same context

Erroneous reasoning persists in context. When you try to correct Claude's drift in the same conversation, the mistaken reasoning stays visible and continues to influence subsequent turns.[^2] [/rewind](glossary.md#rewind) reverts to the last clean checkpoint and lets you re-prompt with a clearer instruction.

**Example:**
```text
# Claude has gone off track — press Esc Esc or run:
/rewind

# Claude reverts to previous checkpoint.
# Now re-prompt more precisely:
Implement only the token validation function in auth.py.
Do not touch middleware.py — that module is complete.
```

If Claude drifts twice on the same issue after rewinding, use `/clear` to start the session fresh rather than compounding corrections.

> **When to use:** The moment you notice Claude has misunderstood your intent and produced work that needs to be discarded. Act early — the longer erroneous reasoning sits in context, the more it contaminates subsequent turns.
>
> **Pitfalls:** Trying to correct drift by explaining what went wrong inside the same context. This adds more tokens to an already-compromised window and often makes things worse. Rewind first, re-prompt second.

---

### 8. Layer three complementary strategies: compaction, clearing, and memory

Each strategy targets a different kind of context growth. [Memory](primitives.md#memory) (structured notes to external storage) addresses cross-session persistence; compaction addresses whole-transcript growth; tool-result clearing addresses bulky re-fetchable payloads inside the window. The strategies compose.[^8]

**Example — layered workflow for a long research or refactoring session:**
```python
# Step 1: Save irreplaceable findings to a file that survives resets
with open("notes/research-findings.md", "a") as f:
    f.write(f"\n## Session {date.today()}\n{claude_summary}\n")

# Step 2: Compact when context hits 60% — passing preservation instructions
# /compact Keep: decision to use asyncio over threading (GIL reason),
#               unresolved race condition in worker.py line 89.
#               Clear: file reads, search results.

# Step 3: At phase boundary, start fresh and reload only what matters
# New session first message:
# "Load notes/research-findings.md. We're now implementing the worker module."
```

Mental model for choosing:
- Compaction: whole window is growing too large
- Tool-result clearing: specific bulky payloads (file reads, API responses) are the bottleneck
- Memory/notes files: information needs to survive across sessions or resets[^8]

> **When to use:** Multi-hour sessions, multi-day projects, or any agent workflow where context pressure is a recurring bottleneck.
>
> **Pitfalls:** Treating these as alternatives. They are complementary layers. A session that uses only compaction will still lose cross-session context. A session that uses only memory files will still accumulate in-session noise. Use all three where relevant.

---

## Related themes

- [CLAUDE.md & project setup](claudemd-setup.md) — the `@`-import pattern for `context-essentials.md` is the lowest-friction solution to compaction data loss and lives entirely in your project setup
- [Hooks & automation](hooks-automation.md) — `PostCompact` hooks re-inject critical rules after every compaction without any manual intervention; `Stop` hooks can also unconditionally re-inject rules every response turn
- [Parallel development](parallel-development.md) — git worktrees give each agent its own isolated context window, eliminating compaction pressure from the main session entirely

---

[^1]: [How to use the /compact command in Claude Code to prevent context rot](references.md#claude-code-compact-command-context-management)
[^2]: [10 essential Claude Code best practices you need to know](references.md#174731)
[^3]: [Claude Code: post-compaction hooks for context renewal](references.md#claude-code-post-compaction-hooks-for-context-renewal-7b616d)
[^4]: [Claude Code hooks guide](references.md#2026-02-28-claude-code-hooks-guide)
[^5]: [Claude Code hooks guide](references.md#2026-02-28-claude-code-hooks-guide)
[^6]: [Managing context with Claude Code: approaches and experiences](references.md#simondholmes-ive-been-figuring-out-how-to-manage-context-act)
[^7]: [Claude Code best practices: 12 patterns agentic engineers use](references.md#claude-code-best-practices-12-patterns-agentic-engineers-use)
[^8]: [Context engineering: memory, compaction, and tool clearing](references.md#tool-use-context-engineering-context-engineering-tools)
