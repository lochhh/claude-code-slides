# MCP servers

[← Back to index](index.md)

[MCP servers](primitives.md#mcp-servers) are the fastest way to eliminate context switches between Claude Code and the rest of your stack. Each server exposes a set of tools that Claude can call the same way it calls built-in tools — reading a PR, querying a database, fetching live docs — all without leaving the terminal. The wrong configuration slows startup and pollutes the [context window](glossary.md#context-window) with tools you never invoke; the right 2–3 servers make Claude Code a single interface for code and external services. This theme covers how to pick, configure, secure, and debug [MCP](glossary.md#mcp) servers for a Python-heavy workflow.

**Level:** Intermediate

## Tips

### 1. Start with the default trio: Sequential Thinking + GitHub + Context7

Each [MCP server](primitives.md#mcp-servers) adds startup time and occupies tool slots in the context. Avoid registering servers speculatively. The highest-ROI default set for Python developers is Sequential Thinking (structured reasoning), GitHub (PR and issue access), and Context7 (live library docs). Add database or infra MCPs only inside the projects that need them.[^1]

**Example:**

```bash
# Register the trio at user scope so they're available in every project
claude mcp add sequential-thinking -s user -- npx -y @modelcontextprotocol/server-sequential-thinking
claude mcp add github -s user -- npx -y @modelcontextprotocol/server-github
claude mcp add context7 -s user -- npx -y @context7/mcp-server
```

> **When to use:** At initial Claude Code setup. Run once; all three servers stay available across projects.
>
> **Pitfalls:** Installing 8–10 MCPs at user scope slows every session. Each inactive server still initialises on startup unless you mark it lazy (see tip 8). Prune servers you haven't used in a week.

---

### 2. Use [Sequential Thinking MCP](glossary.md#sequential-thinking-mcp) for complex problem decomposition

Sequential Thinking makes Claude break a problem into explicit reasoning steps before writing code. On architecture decisions, subtle bug diagnosis, or multi-file refactors, this produces measurably fewer wrong first attempts compared to direct implementation requests.[^2]

**Example:**

```bash
claude mcp add sequential-thinking -s user \
  -- npx -y @modelcontextprotocol/server-sequential-thinking
```

Then in a session:

```
Outline the steps to decouple the authentication module from the user service,
then implement each step.
```

Claude will produce a numbered plan before touching any files.

> **When to use:** Architecture decisions, complex debugging sessions, any task where the solution space is large enough that jumping straight to code produces rework.
>
> **Pitfalls:** Sequential Thinking adds tokens to every reasoning trace. On trivial tasks it wastes context without benefit. Reserve it for problems that genuinely require multi-step planning.

---

### 3. Store credentials in environment variables, not in config files

[`.mcp.json`](glossary.md#mcp-json) and `~/.claude.json` both support `${VAR_NAME}` expansion. Use it for every secret. Hard-coded tokens in config files get committed to version control, rotated under pressure, and leaked in CI logs.[^3]

**Example:**

`.mcp.json` (safe to commit):

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "${DATABASE_URL}"
      }
    }
  }
}
```

Shell profile (`~/.bashrc` or `~/.zshrc`):

```bash
export GITHUB_TOKEN="ghp_your_actual_token_here"
export DATABASE_URL="postgresql://readonly_user:pass@localhost:5432/mydb"
```

> **When to use:** Always. No exceptions for dev environments — tokens committed to dev branches end up in reflog and PR history.
>
> **Pitfalls:** `${VAR}` expansion is evaluated at server startup, not at config parse time. If the variable is unset, the server will fail to start with a cryptic connection error rather than a clear "variable not set" message. Verify your shell exports before debugging the MCP.

---

### 4. Use [project-level MCP](glossary.md#project-level-mcp) config to share servers across the team

Commit `.mcp.json` at the project root with `--scope project`. Every developer who opens the project in Claude Code gets the same MCP servers automatically. Individual credentials stay out of the file via environment variable expansion.[^4]

**Example:**

```bash
# Add a postgres MCP scoped to this project (writes to .mcp.json)
claude mcp add postgres --scope project \
  -- npx -y @modelcontextprotocol/server-postgres
```

Resulting `.mcp.json` after adding postgres and a Sentry server:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "${DATABASE_URL}"
      }
    },
    "sentry": {
      "type": "http",
      "url": "https://mcp.sentry.io/mcp",
      "headers": {
        "Authorization": "Bearer ${SENTRY_TOKEN}"
      }
    }
  }
}
```

Commit this file. Each developer exports their own `DATABASE_URL` and `SENTRY_TOKEN` locally.

> **When to use:** Any project where ≥2 engineers use Claude Code. Eliminates the "which MCP do I need for this repo?" question entirely.
>
> **Pitfalls:** Claude Code prompts for approval the first time it loads a project-scoped `.mcp.json`. If a team member dismisses that prompt, their servers stay disconnected silently. Run `claude mcp reset-project-choices` to re-trigger the approval dialogue. Scope precedence is local > project > user, so a local override can mask the shared config.

---

### 5. Connect database MCPs with read-only credentials only

The natural language interface to a database MCP makes destructive queries easy to trigger accidentally. Create a dedicated read-only PostgreSQL user and use that connection string in every MCP config. Never point an AI tool at a write-capable production connection.[^5]

**Example:**

```sql
-- Run once in psql as a superuser
CREATE USER claude_readonly WITH PASSWORD 'secure_password';
GRANT CONNECT ON DATABASE mydb TO claude_readonly;
GRANT USAGE ON SCHEMA public TO claude_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO claude_readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO claude_readonly;
```

`.mcp.json`:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://claude_readonly:secure_password@localhost:5432/mydb"
      }
    }
  }
}
```

> **When to use:** Every time you connect a database MCP, including local development databases. SQLAlchemy models and Alembic migration history are also accessible once Claude has schema access — valuable for understanding constraints before writing queries.
>
> **Pitfalls:** Special characters in passwords (`@`, `#`, `!`) must be percent-encoded in the connection string. `@` becomes `%40`. An unencoded `@` in the password makes the URL parser treat part of the password as the hostname, producing a confusing "connection refused" error.

---

### 6. Use [Context7](glossary.md#context7) MCP to eliminate hallucinated Python APIs

Context7 fetches live documentation for 50+ frameworks and libraries. Claude's training data for FastAPI, SQLAlchemy, Pydantic, and similar fast-moving Python packages goes stale quickly. Context7 pulls the current version's API reference before generating code, which eliminates the "that method doesn't exist" class of errors.[^1]

**Example:**

```bash
claude mcp add context7 -s user -- npx -y @context7/mcp-server
```

In a session:

```
Using the current FastAPI docs, show me how to add dependency injection
for a SQLAlchemy async session.
```

Claude fetches the live FastAPI documentation before responding, ensuring the `Depends()` pattern and session factory it generates match the installed version.

> **When to use:** Any time you're working with a library that releases frequently (FastAPI, Pydantic v2, LangChain, SQLAlchemy 2.x). Also useful when upgrading between major versions — ask Claude to diff the old API usage in your codebase against the new docs.
>
> **Pitfalls:** Context7 makes an outbound HTTP request per documentation lookup. In air-gapped environments or behind strict firewalls, it will time out silently and Claude will fall back to training data without warning. Test connectivity with `claude mcp list` and check server status with `/mcp` if you suspect this.

---

### 7. Debug MCP connection failures with `/mcp`

The `/mcp` [slash command](primitives.md#slash-commands) inside a Claude Code session lists every registered server, its connection status, and its available [tool use](primitives.md#tool-use) entries. It is the first diagnostic step for any MCP that fails to respond. `/mcp` also surfaces OAuth flows for servers that require browser-based authentication (GitHub, Sentry, Notion).[^4]

**Example:**

If the GitHub MCP stops responding mid-session:

1. Type `/mcp` in the Claude Code prompt.
2. Find the `github` entry — status will show `disconnected`, `auth_required`, or a process error.
3. For auth failures: select the server in the `/mcp` output to re-trigger the OAuth flow.
4. For process errors: run the server command manually to see the raw error:

```bash
npx -y @modelcontextprotocol/server-github
# Look for: missing token, Node version mismatch, npm registry unreachable
```

5. Increase the startup timeout if the server is slow to initialise:

```bash
MCP_TIMEOUT=15000 claude
```

> **When to use:** Any time a tool that worked previously stops being invoked, or when Claude says it cannot access a service you know is configured.
>
> **Pitfalls:** `/mcp` shows the state at the moment you run it. A server can appear connected but have a stale auth token that only fails when a tool call is actually made. If `/mcp` shows connected but the tool still fails, re-authenticate via the `/mcp` interface.

---

### 8. Mark rarely-used MCPs as lazy to reduce session startup time

[Lazy loading](glossary.md#lazy-loading) defers a server's process spawn until the first time one of its tools is actually invoked. For heavy MCPs like Docker or Playwright that you only need occasionally, this cuts several seconds from session initialisation.[^1]

**Example:**

```json
{
  "mcpServers": {
    "docker": {
      "command": "npx",
      "args": ["-y", "@ckreiling/mcp-server-docker"],
      "lazy": true
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"],
      "lazy": true
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "${DATABASE_URL}"
      }
    }
  }
}
```

Postgres stays eager (always connected). Docker and Playwright start only when Claude calls a tool from them.

> **When to use:** MCPs used in fewer than half of your sessions. `lazy: true` adds a small latency spike on the first tool call, so keep frequent-use servers eager.
>
> **Pitfalls:** A lazy server that fails to start will not surface the error until the first tool call. If Claude says "I cannot access that tool" and the server is marked lazy, check startup errors with `MCP_TIMEOUT=15000 claude` or run the server command directly.

---

### 9. Use the GitHub MCP to handle the full PR lifecycle from the terminal

The GitHub MCP eliminates the most common Claude Code context switch: opening a browser to read issues, review pull requests, or manage branches. With the server connected, Claude can read issue descriptions, fetch PR diffs, leave review comments, and create new PRs — all as part of a single coding session.[^2]

**Example:**

```bash
claude mcp add github -s user \
  -- npx -y @modelcontextprotocol/server-github
```

Token setup (add to `~/.bashrc`):

```bash
export GITHUB_TOKEN="ghp_your_token_here"
# Minimum required scopes: repo, workflow, read:org
```

In a session:

```
Review PR #456 in the current repo. Focus on whether the database
queries in user_service.py will cause N+1 issues with SQLAlchemy.
```

Claude fetches the diff, reads the changed files, and produces review comments grounded in your actual code — not a generic checklist.

> **When to use:** Whenever you're working on a feature that touches an open issue or PR. Also useful for automated triage: "List all open issues labelled 'bug' and group them by affected module."
>
> **Pitfalls:** The GitHub MCP uses a Personal Access Token, not an app installation. Token expiry silently breaks the connection. Set a calendar reminder to rotate tokens before they expire, or use the GitHub CLI (`gh auth token`) to issue short-lived tokens and export the result into `GITHUB_TOKEN`.

---

### 10. Use Playwright MCP for E2E test generation and UI validation

Playwright MCP uses accessibility snapshots (not pixel-level vision) to understand page structure. This makes it reliable across different screen sizes and rendering states. Claude can capture screenshots, interact with form elements, navigate flows, and generate Playwright test code — all from the terminal.[^1]

**Example:**

```bash
claude mcp add playwright -s user -- npx -y @playwright/mcp@latest
```

In a session:

```
Navigate to http://localhost:8000/login, fill in the test credentials,
submit the form, and generate a Playwright pytest fixture that covers this flow.
```

Claude launches a browser, completes the interaction, and outputs a working `pytest` fixture using `playwright.sync_api`.

> **When to use:** When writing E2E tests for a FastAPI or Django application during feature development — before those tests go stale. Also useful for validating that a UI change didn't break an existing flow without setting up a full CI run.
>
> **Pitfalls:** Playwright MCP requires Node.js 18+ and downloads Chromium on first run (~300 MB). In Docker-based dev environments, confirm that `npx` has network access and sufficient disk space. Mark this server lazy if you use it infrequently; Chromium startup adds noticeable latency to session initialisation.

---

## Related themes

- [Hooks & automation](hooks-automation.md) — hooks handle code-side events (post-edit, pre-commit); MCPs handle service-side access — use both to cover the full automation surface
- [Parallel development](parallel-development.md) — each git worktree can carry its own `.mcp.json`, so project-specific MCPs (e.g. a staging database) stay scoped to the right branch context
- [Productivity, IDE & cost](productivity-ide-cost.md) — every eager MCP server adds startup latency; combine lazy loading with a minimal default set to keep session init under two seconds

---

[^1]: [Top 10 must-have Claude Code MCP recommendations](references.md#claude-code-mcp-top-10-must-install-en-html)
[^2]: [The 10 must-have MCP servers for Claude Code 2025 developer edition](references.md#the-10-must-have-mcp-servers-for-claude-code-2025-developer-)
[^3]: [Setting up MCP servers in Claude Code](references.md#setting-up-mcp-servers-in-claude-code-a-tech)
[^4]: [Connect Claude Code to your tools with MCP: 5 setups that work](references.md#connect-claude-code-to-your-tools-with-mcp-5-setups-that-wor)
[^5]: [Best MCP servers for Claude Code](references.md#best-mcp-servers-for-claude-code)
