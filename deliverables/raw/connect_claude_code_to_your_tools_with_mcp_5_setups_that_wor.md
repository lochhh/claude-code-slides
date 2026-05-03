# Connect Claude Code to Your Tools With MCP: 5 Setups That Work

**Type:** article
**URL:** https://dev.to/klement_gunndu/connect-claude-code-to-your-tools-with-mcp-5-setups-that-work-f30
**Topic:** MCP Servers
**Published:** unknown

## Content

 [Skip to content](#main-content)

[![DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png)](/) 

[Log in](https://dev.to/enter?signup_subforem=1)    [Create account](https://dev.to/enter?signup_subforem=1&state=new-user)

## DEV Community

[![Cover image for Connect Claude Code to Your Tools With MCP: 5 Setups That Work](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fimages.unsplash.com%2Fphoto-1649451844931-57e22fc82de3%3Fcrop%3Dentropy%26cs%3Dtinysrgb%26fit%3Dmax%26fm%3Djpg%26ixid%3DM3w4ODA4ODZ8MHwxfHNlYXJjaHwxfHxkZXZlbG9wZXIlMjB0b29scyUyMHByb2dyYW1taW5nJTIwY29ubmVjdGlvbnN8ZW58MHwwfHx8MTc3MzgyMDkwOXww%26ixlib%3Drb-4.1.0%26q%3D80%26w%3D1080)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fimages.unsplash.com%2Fphoto-1649451844931-57e22fc82de3%3Fcrop%3Dentropy%26cs%3Dtinysrgb%26fit%3Dmax%26fm%3Djpg%26ixid%3DM3w4ODA4ODZ8MHwxfHNlYXJjaHwxfHxkZXZlbG9wZXIlMjB0b29scyUyMHByb2dyYW1taW5nJTIwY29ubmVjdGlvbnN8ZW58MHwwfHx8MTc3MzgyMDkwOXww%26ixlib%3Drb-4.1.0%26q%3D80%26w%3D1080) 

[![klement Gunndu](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3786236%2Fe2629efd-63ba-4d1b-83d8-b55db5d86b58.jpeg)](/klement_gunndu)

[klement Gunndu](/klement_gunndu)

Posted on

# Connect Claude Code to Your Tools With MCP: 5 Setups That Work

[#claudecode](/t/claudecode) [#ai](/t/ai) [#mcp](/t/mcp) [#tutorial](/t/tutorial)

Your AI coding assistant can read your files and run your commands. It cannot read your Jira tickets, query your production database, or check why Sentry is on fire — unless you connect it to the systems that can.

MCP (Model Context Protocol) is the open standard that bridges this gap. One command, one config line, and Claude Code gains access to databases, monitoring tools, APIs, and anything else with an MCP server.

Here are 5 practical setups that turn Claude Code from a code assistant into a full development interface.

## How MCP Works in Claude Code

MCP servers come in two flavors: **remote** and **local**.

**Remote servers** run over HTTP. You give Claude Code a URL, it connects, and the server's tools appear in your session. Most cloud services (GitHub, Sentry, Notion) work this way.

**Local servers** run as processes on your machine via stdio. You specify a command, Claude Code launches it, and communicates through stdin/stdout. Database connectors and filesystem tools typically use this transport.

Three commands handle everything:

```
# Add a server --transport # List all configured servers # Remove a server
```

Servers are scoped to control visibility:

* **local** (default) — available only to you in the current project
* **project** — shared with the team via `.mcp.json` in the repo root
* **user** — available to you across all projects

The `--scope` flag controls this:

```
--transport --scope
```

Now let's set up five servers that cover the most common development workflows.

## Setup 1: GitHub — PRs, Issues, and Code Reviews

GitHub's MCP server gives Claude Code direct access to your repositories. Instead of switching to the browser to read a PR, you ask Claude Code to summarize it, find issues, or suggest review comments.

**Add the server:**

```
--transport
```

**Authenticate:**

Run `/mcp` inside Claude Code, select the GitHub server, and follow the browser-based OAuth flow. Tokens are stored securely and refreshed automatically.

**What you can do after setup:**

```
Review PR #456 and suggest improvements 
```

```
Show me all open PRs assigned to me 
```

```
Create a new issue for the authentication bug we just found 
```

The GitHub MCP server exposes repository management, PR workflows, issue tracking, and code search. If you work with GitHub daily, this server pays for itself in the first hour.

**Scope recommendation:** User scope (`--scope user`). You'll want this across all projects.

## Setup 2: PostgreSQL — Query Your Database Without Leaving the Terminal

Direct database access is the setup that changes the most workflows. Instead of writing SQL in a separate client, copying results, and pasting them into your conversation, Claude Code reads the schema and queries the database directly.

**Add the server:**

```
--transport \ -- -y \ --dsn"postgresql://readonly:pass@prod.db.com:5432/analytics"
```

This runs a local stdio process via `npx`. The `--dsn` flag points to your database. Use a read-only user for safety.

**What you can do after setup:**

```
Show me the schema for the orders table 
```

```
What's our total revenue this month? 
```

```
Find customers who haven't made a purchase in 90 days 
```

Claude Code sends SQL queries through the MCP server, gets results, and presents them in context. No tab switching. No copy-paste.

**Scope recommendation:** Local scope (default). Database credentials vary per project.

**Security note:** Always connect with a read-only database user. The MCP server passes queries directly. A write-capable connection in an AI tool is a production incident waiting to happen.

**Troubleshooting:** If the server fails to connect, check that `npx` can reach the npm registry and that your DSN string is URL-encoded. Special characters in passwords (like `@` or `#`) need percent-encoding in the connection string.

## Setup 3: Sentry — Debug Production Errors in Context

When an error fires in production, you normally open Sentry, dig through the stack trace, find the file, open your editor, and start debugging. With the Sentry MCP server, you skip straight to the fix.

**Add the server:**

```
--transport
```

**Authenticate:**

Run `/mcp` inside Claude Code and complete the Sentry OAuth flow in your browser.

**What you can do after setup:**

```
What are the most common errors in the last 24 hours? 
```

```
Show me the stack trace for error ID abc123 
```

```
Which deployment introduced these new errors? 
```

The workflow becomes: see the error, ask Claude Code to explain it, and fix it — all in one session. Claude Code has your code context already, so it can correlate Sentry stack traces with local files immediately.

**Scope recommendation:** User scope. Error monitoring applies across projects.

## Setup 4: Team-Shared Configuration With .mcp.json

The first three setups are personal. This one is for teams.

When you add a server with `--scope project`, Claude Code writes the config to `.mcp.json` at your project root. Check this file into version control, and every team member gets the same MCP servers when they open the project.

**Create a shared config:**

```
--transport --scope
```

This creates `.mcp.json`:

```
{ "mcpServers":  { "notion":  { "type":  "http",  "url":  "https://mcp.notion.com/mcp"  }  }  }  
```

**Use environment variables for secrets:**

The config supports `${VAR}` syntax for values that change per developer:

```
{ "mcpServers":  { "api-server":  { "type":  "http",  "url":  "${API_BASE_URL:-https://api.example.com}/mcp",  "headers":  { "Authorization":  "Bearer ${API_KEY}"  }  }  }  }  
```

Each developer sets `API_KEY` in their local environment. The shared config stays clean.

**How precedence works:**

If the same server name exists at multiple scopes, local overrides project, and project overrides user. This means a team can define defaults in `.mcp.json`, and individual developers can override with local-scoped entries for their own credentials.

Claude Code prompts for approval before using project-scoped servers from `.mcp.json` files. If you need to reset those choices, run:

```
claude mcp reset-project-choices 
```

**Scope recommendation:** Project scope (by definition). Keep secrets in environment variables or local overrides.

## Setup 5: Claude Code as an MCP Server

This is the reverse pattern. Instead of connecting Claude Code to other tools, you expose Claude Code itself as an MCP server for other applications.

**Start the server:**

```
claude mcp serve 
```

**Connect from Claude Desktop:**

Add this to your `claude_desktop_config.json`:

```
{ "mcpServers":  { "claude-code":  { "type":  "stdio",  "command":  "claude",  "args":  ["mcp",  "serve"],  "env":  {}  }  }  }  
```

If `claude` is not in your PATH, use the full path:

```
# /usr/local/bin/claude (example)
```

Then replace `"command": "claude"` with the full path.

**What this enables:**

Claude Desktop gains access to Claude Code's tools — file reading, editing, searching, and bash execution. You get Claude Code's capabilities through the Claude Desktop interface.

This is useful when you want the Claude Desktop UI but need Claude Code's file system access and tool execution. The MCP server exposes tools like Read, Edit, Write, LS, and GrepTool.

**Important:** Your MCP client is responsible for confirming tool calls. Claude Code exposes the tools; it does not enforce its own confirmation flow when running as a server.

**When to use this:** Build automation pipelines where a different AI application orchestrates Claude Code's file editing and code analysis capabilities. Or use it to give Claude Desktop access to your local filesystem through Claude Code's sandboxed tool execution.

## Managing Your Servers

Once you have servers configured, two commands handle ongoing management:

**Check status:**

The `/mcp` slash command inside Claude Code shows all connected servers, their status, and lets you authenticate or reconnect.

**Import from Claude Desktop:**

If you already configured servers in Claude Desktop, import them:

```
claude mcp add-from-claude-desktop 
```

This reads the Desktop config file and lets you select which servers to bring over. Works on macOS and WSL.

**Environment variables worth knowing:**

| Variable | Purpose | Default |
| --- | --- | --- |
| `MCP_TIMEOUT` | Server startup timeout in ms | — |
| `MAX_MCP_OUTPUT_TOKENS` | Maximum tokens per tool response | 25,000 |
| `ENABLE_TOOL_SEARCH` | Dynamic tool loading behavior | `auto` |

If you have many MCP servers, Claude Code automatically enables Tool Search — loading tools on demand instead of upfront. This keeps your context window clean. You can control this with `ENABLE_TOOL_SEARCH=auto:5` (triggers at 5% context usage) or `ENABLE_TOOL_SEARCH=false` to disable.

## What to Set Up First

If you are starting from zero:

1. **GitHub** — highest impact for most developers. PRs, issues, and code reviews without context switching.
2. **Database** — second highest. Direct SQL access eliminates the copy-paste workflow entirely.
3. **Sentry or your monitoring tool** — completes the production debugging loop.
4. **Team .mcp.json** — once you have servers that work, share the config.
5. **Claude Code as server** — niche but powerful when you want Claude Code tools in other clients.

Each setup takes under 2 minutes. The productivity gain compounds daily.

## Common Mistakes to Avoid

A few patterns trip up most developers when first configuring MCP:

**Putting secrets in `.mcp.json`.** This file gets committed to version control. Use `${ENV_VAR}` expansion and set actual values in your shell profile or `.env` file. If a team member commits a token, rotate it immediately.

**Using write-capable database connections.** The natural language interface makes it easy to accidentally run destructive queries. Always use read-only credentials for MCP database servers. Create a separate database user with `SELECT`-only permissions.

**Forgetting option ordering.** All flags (`--transport`, `--env`, `--scope`, `--header`) must come before the server name. The `--` double dash separates Claude Code flags from the server's command arguments. Getting this wrong produces confusing errors.

**Ignoring the SSE deprecation.** SSE (Server-Sent Events) transport still works but is deprecated. If you find a tutorial using `--transport sse`, switch to `--transport http` where the server supports it. HTTP is the recommended transport for all remote servers.

---

Follow [@klement\_gunndu](https://dev.to/klement_gunndu) for more Claude Code content. We're building in public.

## Top comments (8)

Subscribe

[![zuidaima profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3831214%2F89714d4b-ef25-4d32-bb14-5381586237e5.png)](https://dev.to/zuidaima) 

[zuidaima](https://dev.to/zuidaima) 

[![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3831214%2F89714d4b-ef25-4d32-bb14-5381586237e5.png)   zuidaima](/zuidaima)

Building L3: Running 2,000+ Legacy Projects with 1-Click.

* Location

  Beijing, China
* Joined

• 

* [Copy link](https://dev.to/klement_gunndu/connect-claude-code-to-your-tools-with-mcp-5-setups-that-work-f30#comment-35med)

"Great breakdown on the MCP setups, Klement! As a veteran developer (14 years in the game), I've been obsessing over the same problem: how to bridge the gap between 'Code' and 'Running Tools'.

I'm currently pivoting my marketplace of 2,000+ projects into a One-Click Cloud-Run PaaS (L3). Imagine an MCP server that doesn't just give you the code, but spins up a Dockerized environment for it instantly.

I noticed you followed me—would love to get your academic/technical perspective on this 'instant infrastructure' for AI agents. Are you open to a quick chat or being a Beta Tester?"

    

[![klement_gunndu profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3786236%2Fe2629efd-63ba-4d1b-83d8-b55db5d86b58.jpeg)](https://dev.to/klement_gunndu) 

[klement Gunndu](https://dev.to/klement_gunndu) 

[![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3786236%2Fe2629efd-63ba-4d1b-83d8-b55db5d86b58.jpeg)   klement Gunndu](/klement_gunndu)

SWE @. Building autonomous AI agents with top-grade discipline. Python, LangChain, Claude Code. The agent writes our articles. I just read them.

* Education

  Masters in CompSci
* Work

  SWE
* Joined

• 

* [Copy link](https://dev.to/klement_gunndu/connect-claude-code-to-your-tools-with-mcp-5-setups-that-work-f30#comment-35meo)

The idea of wrapping MCP servers in instant Dockerized environments is interesting. Right now the biggest friction in MCP adoption is setup and dependency management for each server, so a one-click spin-up that handles isolation could remove a real barrier.

Curious how you handle state persistence across container restarts, since most MCP servers today are stateless by default. That seems like the key design decision for making this production-ready.

Good luck with the pivot.

     

[![klement_gunndu profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3786236%2Fe2629efd-63ba-4d1b-83d8-b55db5d86b58.jpeg)](https://dev.to/klement_gunndu) 

[klement Gunndu](https://dev.to/klement_gunndu) 

[![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3786236%2Fe2629efd-63ba-4d1b-83d8-b55db5d86b58.jpeg)   klement Gunndu](/klement_gunndu)

SWE @. Building autonomous AI agents with top-grade discipline. Python, LangChain, Claude Code. The agent writes our articles. I just read them.

* Education

  Masters in CompSci
* Work

  SWE
* Joined

• 

* [Copy link](https://dev.to/klement_gunndu/connect-claude-code-to-your-tools-with-mcp-5-setups-that-work-f30#comment-365dh)

14 years in and still obsessing over the code-to-runtime gap — that's the right obsession. A cloud-run PaaS with MCP integration could be killer for removing that last mile of friction.

     

[![zuidaima profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3831214%2F89714d4b-ef25-4d32-bb14-5381586237e5.png)](https://dev.to/zuidaima) 

[zuidaima](https://dev.to/zuidaima) 

[![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3831214%2F89714d4b-ef25-4d32-bb14-5381586237e5.png)   zuidaima](/zuidaima)

Building L3: Running 2,000+ Legacy Projects with 1-Click.

* Location

  Beijing, China
* Joined

• 

* [Copy link](https://dev.to/klement_gunndu/connect-claude-code-to-your-tools-with-mcp-5-setups-that-work-f30#comment-35mi8)

"Hi Klement, I've been following your insights on Dev.to. As someone who’s managed a code community for 14 years in China (2,000+ verified systems), I'm now exploring how to bring these assets to the global/SEA developer scene.

I’m really curious about your perspective: In Europe or your research circles, do developers struggle as much with 'environment setup' as we do in Asia?

I'm building an L1-L3 service model to solve the 'broken code' problem, but I'm not sure if global developers value 'Verified & Ready-to-Run' code as much as my previous users did. Would love to hear your 'boots on the ground' feel on this!"

    

[![klement_gunndu profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3786236%2Fe2629efd-63ba-4d1b-83d8-b55db5d86b58.jpeg)](https://dev.to/klement_gunndu) 

[klement Gunndu](https://dev.to/klement_gunndu) 

[![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3786236%2Fe2629efd-63ba-4d1b-83d8-b55db5d86b58.jpeg)   klement Gunndu](/klement_gunndu)

SWE @. Building autonomous AI agents with top-grade discipline. Python, LangChain, Claude Code. The agent writes our articles. I just read them.

* Education

  Masters in CompSci
* Work

  SWE
* Joined

• 

* [Copy link](https://dev.to/klement_gunndu/connect-claude-code-to-your-tools-with-mcp-5-setups-that-work-f30#comment-35mji)

Environment setup is a universal pain point, not just Asia. In the MCP ecosystem specifically, developers spend more time wiring tool servers together than building features. Your L1-L3 model maps well here — verified, dependency-locked configs that just work would save teams hours per integration.

Some comments may only be visible to logged-in visitors. [Sign in](/enter) to view all comments.

For further actions, you may consider blocking this person and/or [reporting abuse](/report-abuse)

![DEV Community](https://media2.dev.to/dynamic/image/width=190,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png) 

We're a place where coders share, stay up-to-date and grow their careers.

[Log in](https://dev.to/enter?signup_subforem=1)   [Create account](https://dev.to/enter?signup_subforem=1&state=new-user)

![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) ![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) ![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) ![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)

 
