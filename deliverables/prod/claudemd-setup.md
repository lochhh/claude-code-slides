# CLAUDE.md & project memory

[← Back to index](index.md)

[`CLAUDE.md`](primitives.md#claude-md) is the single highest-leverage file in any Claude Code project. It is loaded at the start of every session and acts as Claude's standing orders — the one place that survives context resets and gives the model a coherent frame before it sees a single line of your code. Engineers who hit the ceiling with basic Claude Code usage almost always have the same root cause: a CLAUDE.md that is either empty, bloated, or never updated. Fixing it cuts down correction loops, reduces [context rot](glossary.md#context-rot), and makes Claude behave consistently across sessions that span hours or days.

**Level:** Novice

## Tips

### 1. Include only what Claude cannot infer from reading the codebase

Put build commands, test commands, branch-naming conventions, and architectural decisions that are not visible in the code. Leave out naming conventions and patterns that are already obvious from the existing files — Claude will read those itself.[^1][^3]

**Example:**

```markdown
## Commands
- Install: `uv sync`
- Test: `uv run pytest tests/ -x --tb=short`
- Lint: `uv run ruff check . && uv run mypy src/`

## Branch naming
feature/<ticket-id>-short-description
fix/<ticket-id>-short-description

## Architecture
- All DB access goes through `src/db/session.py` — never import SQLAlchemy directly in routers
- Config is loaded once in `src/config.py` — never read `os.environ` elsewhere
```

> **When to use:** At project start, and whenever you notice Claude making a decision you have a strong opinion about that isn't reflected in the code.
>
> **Pitfalls:** Adding obvious things ("use snake_case for Python") wastes instruction budget and dilutes the signal of rules Claude actually needs.

### 2. Encode prohibitions as explicit "Never X" rules

Claude responds more reliably to `Never modify /src/auth/ without explicit confirmation` than to `Be careful with auth`. Vague guidance is treated as a soft preference; an explicit prohibition is treated as a hard constraint.[^2][^4]

**Example:**

```markdown
## Hard rules
- Never run database migrations without showing the full SQL first and waiting for confirmation
- Never commit `.env` files or any file containing credentials
- Never use `pip install` — always use `uv add` or `uv sync`
- Never modify `/src/auth/` without explicit sign-off — auth changes require a separate review
- Never use `SELECT *` — always name columns explicitly
```

> **When to use:** For any action that is irreversible, security-sensitive, or that Claude has already done wrong at least once.
>
> **Pitfalls:** Writing prohibitions you do not enforce trains Claude to ignore them. Only add a rule you will actually hold to.

### 3. Keep CLAUDE.md well under 100 lines; reference files for everything else

[Context rot](glossary.md#context-rot) sets in before Anthropic's stated 200-line limit. Empirically, compliance degrades around 145 lines — Claude follows the top rules and silently ignores the rest. Trimming to ~77 lines restores full compliance. Put detailed docs in `docs/architecture.md`, `docs/db-schema.md`, and similar files, then reference them from CLAUDE.md.[^1][^5]

**Example:**

```markdown
# CLAUDE.md

@.claude/context-essentials.md

## Commands
- Test: `uv run pytest tests/ -x --tb=short`
- Lint: `uv run ruff check .`
- Run: `uvicorn app.main:app --reload`

## Hard rules
- Never use `pip` — always `uv`
- Never touch `/src/auth/` without confirmation
- Never commit `.env` files

## References
- Architecture: see `docs/architecture.md`
- DB schema: see `docs/db-schema.md`
- API conventions: see `docs/api-conventions.md`
```

> **When to use:** Any time your CLAUDE.md crosses 80 lines. Move the lowest-signal content out first.
>
> **Pitfalls:** Referencing files that do not exist yet, or that go stale faster than CLAUDE.md itself.

### 4. Update CLAUDE.md reactively — every time Claude repeats the same mistake

When Claude makes the same error twice in a session, that is a missing rule. Add it immediately. CLAUDE.md should grow with the project rather than being set once and forgotten.[^6][^7]

**Example:**

If Claude generates a function that raises an exception instead of returning a `Result` type:

```markdown
## Project conventions
- This codebase uses `Result[T, E]` from `returns` — NEVER raise exceptions,
  always return `Result.failure(...)`. See `src/types/result.py`.
```

If Claude calls `pip install` despite your toolchain:

```markdown
## Hard rules
- Never use `pip install` — always `uv add <package>` or edit `pyproject.toml` and run `uv sync`
```

> **When to use:** Immediately after the second occurrence of the same mistake — not at the end of the session.
>
> **Pitfalls:** Waiting until a "cleanup session" to update CLAUDE.md. By then you have had the same correction three or four times.

### 5. Use layered CLAUDE.md files in monorepos

Root CLAUDE.md carries shared context — global toolchain, coding standards, common prohibitions. Each sub-package gets its own CLAUDE.md for service-specific rules. Claude loads the most local file, so service-specific rules do not pollute the shared context.[^5][^6] This is called [layered CLAUDE.md](glossary.md#layered-claudemd).

**Example:**

```
/CLAUDE.md                          # shared: uv, ruff, mypy, branch naming, global prohibitions
/services/auth/CLAUDE.md            # auth-specific: JWT patterns, session rules, "never touch X"
/services/billing/CLAUDE.md         # billing-specific: Stripe webhook handling, idempotency rules
/packages/shared-db/CLAUDE.md       # db-specific: migration conventions, query patterns
```

Root `/CLAUDE.md`:

```markdown
## Monorepo conventions
- Package manager: `uv` — never `pip`
- Each service has its own CLAUDE.md — check it before making service-specific changes
- Branch naming: `feature/<service>/<ticket>-description`
```

`/services/auth/CLAUDE.md`:

```markdown
## Auth service rules
- JWT signing key is in `src/auth/keys.py` — never log or print it
- Session tokens expire in 15 minutes — never extend this without a security review
- Never bypass `require_auth` decorator
```

> **When to use:** Any project with two or more independently deployable services.
>
> **Pitfalls:** Duplicating rules across the root and per-package files. Global rules live only at the root; move them there if you find yourself copying.

### 6. Add a `context-essentials.md` for post-compaction rule re-injection

[Context compaction](primitives.md#context-compaction) is lossy — conventions mentioned at session start get compressed alongside the full conversation history. A separate 10–50 line file containing your highest-priority rules survives compaction if re-injected automatically.[^8]

Important caveat: `/compact` is a slash command, not a tool call, so a `PostToolUse` hook with a `"compact"` matcher will never fire — the compaction event is not exposed via `PostToolUse`. The reliable approach is to import [context-essentials.md](glossary.md#context-essentials) directly in CLAUDE.md using the `@` import syntax, which causes Claude to re-read it at session start.[^9]

**Example — `.claude/context-essentials.md`:**

```markdown
# Context essentials (re-injected after compaction)

## Critical rules
- Package manager: `uv` only — NEVER `pip install`
- All date operations: use `arrow` — NEVER `datetime.now()` without timezone
- DB access: always go through `src/db/session.py` — NEVER import engine directly
- Auth: use `require_auth` decorator — NEVER accept user_id from request body

## Banned patterns
- No `# type: ignore` without an explanatory comment
- No bare `except:` — always catch a specific exception type
- No `SELECT *` queries
- No `--no-verify` on git operations
```

**CLAUDE.md import line:**

```markdown
@.claude/context-essentials.md
```

> **When to use:** Any project where sessions routinely run long enough to trigger compaction, or where correctness rules are critical enough that drift is dangerous.
>
> **Pitfalls:** Making context-essentials.md a copy of CLAUDE.md. Keep it to 10–50 lines of the highest-signal rules only — every line costs tokens on every compaction.

### 7. Structure skills as folders with progressive disclosure, not monolithic files

A flat `SKILL.md` file crammed with all instructions degrades quickly as it grows. Structure each skill as a directory: a `SKILL.md` entry point that references `references/`, `scripts/`, and `examples/` subdirectories. Claude reads the subdirectory content only when relevant, keeping the [context window](glossary.md#context-window) clean.[^1][^10]

**Example:**

```
.claude/skills/
  code-review/
    SKILL.md              # entry point: what this skill does, when to use it, index of subdirs
    references/
      checklist.md        # full review checklist (loaded on demand)
      security-patterns.md
    examples/
      good-pr-review.md
      bad-pr-review.md
```

`.claude/skills/code-review/SKILL.md`:

```markdown
# Code review skill

Run a structured code review on the current diff.

## Steps
1. Read `references/checklist.md` for the full checklist
2. Check each item against the changed files
3. Output findings grouped by severity: Critical / Warning / Suggestion

## Scope
Focus on logic correctness and security. Skip style — linter handles that.
```

> **When to use:** When a skill's instructions exceed one screen, or when it requires reference data (checklists, examples, templates) that are only sometimes needed.
>
> **Pitfalls:** Putting everything in `SKILL.md` "for now." Skills grow; plan for the folder structure from the first iteration.

### 8. Add a gotchas section documenting project-specific failure modes

Every time Claude makes a project-specific mistake — one that is not a general coding error but a consequence of your particular codebase decisions — document it under a [gotchas section](glossary.md#gotchas-section). Over time this becomes the highest signal-to-noise content in CLAUDE.md.[^1][^3]

**Example:**

```markdown
## Known footguns

- `Result[T, E]` everywhere — this codebase never raises exceptions. Returning a bare value
  or raising an exception is always wrong. Use `returns.result.Success` / `returns.result.Failure`.

- `/api/v1` is frozen — all new endpoints go in `/api/v2`. Never add routes to `src/api/v1/`.

- `date-fns` pinned to 2.29.x — do NOT upgrade. v3 broke our timezone logic. See ADR-004.

- Pydantic v2 — we migrated. Never use `.dict()` (deprecated); always use `.model_dump()`.

- Tests use real Postgres via `pytest-postgresql` — never mock the DB layer.
  Integration tests run with `uv run pytest tests/integration/ --db-reset`.
```

> **When to use:** After every session where Claude encountered a project-specific trap. Add it before closing the session.
>
> **Pitfalls:** Writing gotchas that are really general Python conventions ("don't use mutable default arguments"). Those belong in a linter rule, not CLAUDE.md.

## Related themes

- [Context management](context-management.md) — compaction breaks CLAUDE.md rules mid-session; context-essentials.md and proactive compaction strategies are the fix
- [Hooks & automation](hooks-automation.md) — Stop hooks can re-inject critical rules after compaction and enforce conventions that CLAUDE.md alone cannot guarantee
- [Commands, skills & plan mode](commands-skills-plan-mode.md) — skill folder structure lives alongside CLAUDE.md in `.claude/` and depends on the same progressive-disclosure principles

---

[^1]: [10 essential Claude Code best practices you need to know](references.md#174731)
[^2]: [How to set up a Claude.md file that actually works](references.md#how-to-set-up-claude-md-file)
[^3]: [Claude Code best practices: lessons from real projects](references.md#claude-code-best-practices-lessons-from-real-projects)
[^4]: [Claude Code security best practices](references.md#claude-code-security-best-practices)
[^5]: [My Claude Code setup](references.md#my-claude-code-setup)
[^6]: [My top 10 Claude Code tips from 11 months of intense usage](references.md#my-top-10-claude-code-tips-from-11-months-of)
[^7]: [Claude Code best practices: 12 patterns agentic engineers use](references.md#claude-code-best-practices-12-patterns-agentic-engineers-use)
[^8]: [Claude Code: post-compaction hooks for context renewal](references.md#claude-code-post-compaction-hooks-for-context-renewal-7b616d)
[^9]: [Claude Code hooks guide](references.md#2026-02-28-claude-code-hooks-guide)
[^10]: [How to use Claude Code skills to automate repetitive workflows](references.md#claude-code-skills-automate-workflows)
