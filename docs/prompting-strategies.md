# Prompting strategies

[← Back to index](index.md)

The gap between engineers who stay productive with Claude Code and those who constantly fight it comes down to prompting discipline. Vague prompts produce vague output; micromanaging a debugging session leads Claude astray; over-long sessions accumulate stale context that quietly degrades quality. The tips here are ordered by impact: the first four cover the habits that immediately shift outcomes, the next four sharpen your technique for specific scenarios. Pair these prompts with a well-maintained [CLAUDE.md](primitives.md#claude-md) and a clear mental model of how Claude's [context model](primitives.md#context-model) works, and you stop correcting Claude and start directing it.

**Level:** Novice

## Tips

### 1. Be explicit — Claude does what you say, not what you mean

Vague prompts force Claude to fill in blanks with assumptions, and those assumptions are often wrong. Specify the language, the framework, the exact file to modify, any constraints, and the expected output format before Claude writes a single token.[^1][^2]

**Example:**

```bash
# Bad
claude "Add authentication."

# Good
claude "Add JWT authentication to src/middleware/auth.py.
Use the existing User model in src/models/user.py.
Return 401 if the token is invalid, 403 if expired.
Do not modify any other files."
```

Anthropic's own guidance frames this as the "new employee" heuristic: show your prompt to a colleague with minimal context. If they would be confused, Claude will be too.[^1]

> **When to use:** Every time. Specificity is not just for complex tasks — even simple requests benefit from named files and clear constraints.
>
> **Pitfalls:** Do not specify the *how* if you do not need to. Specifying the file and the expected behaviour is enough; specifying the algorithm invites over-engineering. Save implementation opinions for when you have a strong reason.

---

### 2. Force Claude to think before coding

Claude Code defaults to what one author calls "junior mode": read the ticket, open the file, start typing.[^3] Senior engineers read before writing — they check the tests, verify the git history, map the relationships. You can impose the same discipline with a single sentence.

Prepend your request with an explicit explore-then-plan gate. This is especially valuable when using [plan mode](primitives.md#plan-mode), which enforces a read-only planning phase before any writes.[^4]

**Example:**

```text
Before implementing:
1. Read src/auth/middleware.py
2. Read tests/test_auth.py
3. Check git log --oneline -10 src/auth/middleware.py
4. Write out your approach in plain English

Only start coding after I confirm the plan.
```

The `/wizard` pattern formalises this into an 8-phase methodology: plan → explore → write failing tests → implement the minimum → verify regressions → document → adversarial review → PR cycle. In one real project this sequence caught a race condition, a nullable datetime crash, and hardcoded enum strings — none of which tests alone would have surfaced.[^3]

> **When to use:** Any task that touches more than two files, any unfamiliar codebase, any change with architectural impact.
>
> **Pitfalls:** Do not skip the confirmation step. If you let Claude proceed without reviewing the plan, you lose the entire point of the exercise. For trivial single-file changes, this overhead is not worth it — use it where the cost of a wrong direction is high.

---

### 3. Use `@file` references to stack context incrementally

Describing files in prose is inefficient and error-prone. Use [@ file references](glossary.md#at-file-reference) to point Claude at the exact files it needs, and build context from high-level to specific. Claude processes file references efficiently and avoids hallucinating method signatures it cannot see.[^5][^6]

**Example:**

```bash
# First: anchor Claude to the high-level architecture
claude "@docs/architecture.md @src/auth/ \
  Summarise the current auth flow and identify where OAuth2 would plug in."

# Then: narrow to the implementation
claude "@src/auth/middleware.py @src/auth/jwt_handler.py \
  Add OAuth2 support following the same pattern as the existing JWT flow."
```

The structured exploration prompt below is a reliable onboarding pattern for unfamiliar services:[^7]

```text
Explore @src/services/payments and create documentation covering:
1. Core purpose
2. Architecture (with ASCII diagram if helpful)
3. Key files and their roles
4. External dependencies
5. Important gotchas — what breaks, what is undocumented
```

> **When to use:** Whenever Claude needs to understand a specific part of the codebase before acting. Reference the smallest set of files that gives Claude enough context — not the whole directory.
>
> **Pitfalls:** Do not use `@` on an entire large directory as your first move. Claude will read everything and your [context window](glossary.md#context-window) fills before you ask the actual question. Start with the entry point, then drill down.

---

### 4. Paste the error and say "fix" — do not micromanage the solution

When debugging, your instinct is to help Claude by pointing it toward the likely cause. Resist this. Speculative framing ("the error is probably in X, try Y first") introduces [anchoring bias](glossary.md#anchoring-bias) — Claude will reason toward your hypothesis even when it is wrong, and the session degrades from there.[^2][^4]

Paste the full stack trace and say "fix." Claude's debugging ability is stronger than most engineers expect; let it work.

**Example:**

```bash
# Paste the full traceback, then:
claude "$(python -m pytest tests/test_auth.py 2>&1) 

fix"

# Or pipe it directly:
python -m pytest tests/test_auth.py 2>&1 | claude "fix the failing tests"
```

If it fails after two attempts, stop. Use `/clear` and approach the problem from a different angle with a cleaner framing.[^2] The failed reasoning is still in context and actively hurts the next attempt.

> **When to use:** Any time you encounter an exception, failing test, or CI failure. Give Claude the raw data — logs, tracebacks, CI output — not your interpretation of it.
>
> **Pitfalls:** Two failed attempts is the signal to reset, not to add more explanation. Adding more words to a stuck session usually makes it worse. `/clear` and reframe.

---

### 5. Ask Claude to verify its own work

Claude can hallucinate API signatures, library methods, and version-specific behaviour with complete confidence. A one-line follow-up prompt catches a large proportion of these mistakes before they waste your time.[^4][^8]

**Example:**

```text
# After Claude proposes a solution using a specific library:
"Double-check that pydantic.v1.BaseModel still exists in Pydantic v2 before proceeding."

# After a longer implementation:
"Review what you just wrote. Are there any assumptions about the FastAPI 0.115 
API that you are not certain about? List them."

# The classic catch-all:
"Are you sure about this?"
```

This is especially effective for third-party integrations, version-specific features, and anything that involves external API calls. The model's confidence is not calibrated to its accuracy — ask it to check anyway.[^3]

> **When to use:** After any response that references a specific library version, an external API endpoint, or a language feature you are less familiar with.
>
> **Pitfalls:** Do not use this as a blanket follow-up on every response — it adds cost and dilutes the signal. Reserve it for claims Claude cannot verify by running code.

---

### 6. Use [constraint-based prompting](glossary.md#constraint-based-prompting) to prevent over-engineering

Without explicit scope boundaries, Claude will often introduce abstractions for hypothetical future requirements. A plugin system for a script that runs once. An async queue for a synchronous workflow. Constraints defined upfront prevent this and produce code you can actually read.[^5][^9]

**Example:**

```text
"In under 50 lines, using only the Python standard library, 
implement a file watcher that calls process_file(path) when 
a .json file is created in /tmp/incoming.

Do not add abstractions for hypothetical future requirements.
Do not add a configuration system.
Do not make it async unless required."
```

Pair this with an explicit instruction not to modify files outside the scope of the task:[^4]

```text
"Only modify src/parsers/json_parser.py. 
Do not touch any other files, even if you think they need changes."
```

> **When to use:** Tasks where you have a clear, bounded requirement. Any time you have been burned by Claude adding unwanted layers of abstraction.
>
> **Pitfalls:** Do not over-constrain exploratory work. When you genuinely want Claude to surface architectural options, leave room for it to think broadly.

---

### 7. Use [structured exploration prompts](glossary.md#structured-exploration-prompt) for unfamiliar codebases

When you join a new service or investigate an unfamiliar module, a consistent exploration template prevents wasted context and produces reusable documentation. Feed the output back to Claude in future sessions and it avoids re-reading the same files.[^7][^5]

**Example:**

```text
"Explore @src/services/billing and create a markdown document at 
docs/ai/billing-service.md covering:

1. Executive summary — what does this service do?
2. Architecture — how is it structured? Include an ASCII diagram.
3. Data flows — how does data move in and out?
4. Key files — where is the important logic?
5. External dependencies — what other services does it call?
6. Common gotchas — what breaks? What is undocumented?
7. Common operations — how do you test and debug it?"
```

Save the output under a consistent path (e.g. `docs/ai/`). When you start a new session involving the same service, reference the document with `@docs/ai/billing-service.md` rather than asking Claude to re-explore.[^5]

> **When to use:** First time you work on a service, after major refactors, or when onboarding Claude to a new project.
>
> **Pitfalls:** The generated documentation reflects Claude's understanding at the time it ran. Treat it as a living document and update it when you discover something Claude got wrong.

---

### 8. Match model to task — use cheaper models for mechanical work

Opus for every task is like running a database on a supercomputer: the extra capability is wasted and the cost compounds fast. A realistic model-routing policy handles 80 % of daily work at a fraction of the cost.[^10][^9]

**Example:**

```bash
# Switch to Haiku for style review, lookups, and boilerplate
/model haiku
"Review this PR diff for PEP 8 violations and unused imports."

# Switch to Sonnet for routine implementation
/model sonnet
"Implement the changes from the review above."

# Switch to Opus only for architecture and hard debugging
/model opus
"This race condition in the task queue only appears under high concurrency. 
Here is the full trace: [paste]. Diagnose the root cause."
```

A practical cost reference: a multi-file refactoring task costs roughly $0.45 with Sonnet and $5.25 with Opus at API pricing. Over hundreds of tasks per month the difference is significant.[^10]

> **When to use:** Establish a personal routing rule and encode it in your workflow. A useful default: Haiku for review and lookup, Sonnet for implementation, Opus only when Sonnet fails.
>
> **Pitfalls:** Do not switch to Haiku for tasks that require codebase understanding across many files — it will miss context and produce worse output than a cheaper Sonnet session would. Match model capability to the actual reasoning requirement.

---

## Related themes

- [CLAUDE.md & project memory](claudemd-setup.md) — good prompts complement CLAUDE.md: CLAUDE.md handles session-persistent rules and project conventions, while prompts handle task-specific constraints and scope boundaries
- [Context management](context-management.md) — `@file` references, structured exploration prompts, and the practice of clearing between tasks all directly control what ends up in Claude's context window
- [Commands, skills & plan mode](commands-skills-plan-mode.md) — encode your most effective prompt patterns as slash commands and skills so they are reusable without retyping

---

[^1]: [Claude prompting best practices](references.md#claude-prompting-best-practices)
[^2]: [10 essential Claude Code best practices](references.md#174731)
[^3]: [I made Claude Code think before it codes](references.md#i-made-claude-code-think-before-it-codes-heres-the-prompt-bf)
[^4]: [32 Claude Code tips from basics to advanced](references.md#32-claude-code-tips-from-basics-to)
[^5]: [How I use Claude Code to accelerate my software engineering job](references.md#how-i-use-claude-code-to-accelerate-my-software-engineering-)
[^6]: [Claude Code tips best practices](references.md#claude-code-tips-best-practices)
[^7]: [Claude Code best practices: lessons from real projects](references.md#claude-code-best-practices-lessons-from-real-projects)
[^8]: [Claude Code tips](references.md#claude-code-tips)
[^9]: [Claude Code best practices: 12 patterns agentic engineers use](references.md#claude-code-best-practices-12-patterns-agentic-engineers-use)
[^10]: [Claude Code cost optimisation](references.md#claude-code-cost-optimisation)
