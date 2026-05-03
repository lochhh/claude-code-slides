# How to Set Up a Claude.md File That Actually Works - MindStudio

**Type:** article
**URL:** https://www.mindstudio.ai/blog/how-to-set-up-claude-md-file/
**Topic:** CLAUDE.md Setup
**Published:** unknown

## Content

![MindStudio](/MindStudio-lockup-blk.svg)
![MindStudio](/MindStudio-lockup-blk.svg)

# How to Set Up a Claude.md File That Actually Works

The claude.md file is your AI agent's system prompt. Learn the five-question framework for writing one that keeps Claude focused across every session.

![How to Set Up a Claude.md File That Actually Works](https://i.mscdn.ai/70cbb1ad-08d7-4fdc-ab31-e343780966a6/generated-images/85bfb2b2-9f0b-4f4f-af29-36582a1315bf.png?fm=auto&w=1200&fit=cover?fm=auto&w=1200&fit=cover)

## The Problem With Most Claude.md Files

Most Claude.md files don’t work. Not because the concept is flawed, but because they’re written as a brain dump. Someone pastes in a list of vague instructions, saves the file, and assumes the agent will figure out the rest. It won’t.

The Claude.md file is your AI agent’s system prompt. It’s the first thing Claude Code reads at the start of every session. If it’s written well, Claude knows exactly what it’s working on, what you care about, and how you want it to behave. If it’s written poorly — or left empty — Claude starts from scratch every time, making reasonable guesses that may or may not match your actual preferences.

This guide walks through a five-question framework for writing a Claude.md file that holds up across sessions, projects, and teammates.

If you’re new to what the file is and why it exists, start with [what the claude.md file is and why it matters](https://www.mindstudio.ai/blog/what-is-claude-md-file) before coming back here. This article is focused on the practical setup.

## Why Claude.md Is Treated Like an Afterthought

The irony is that the Claude.md file is the single most important thing you’ll configure in a Claude Code setup. But most people spend 90% of their time on prompts and almost nothing on the persistent context layer that governs every single session.

Here’s why that’s backwards.

## Remy doesn't write the code. It manages the agents who do.

Remy runs the project. The specialists do the work. You work with the PM, not the implementers.

![Remy](/remy/lockup-h-sm.svg)

Every time you start a new Claude Code session, the context window is empty. Claude doesn’t remember what you said yesterday. It doesn’t know your project’s conventions, your naming preferences, or the fact that you never want it to touch the auth module without asking first. Without a Claude.md file, you’re re-explaining your project from scratch every session — or accepting that Claude will operate on defaults that don’t match your setup.

The Claude.md file solves this. It’s a persistent markdown document that Claude reads automatically at the start of every session. Think of it as [standing orders that survive sessions](https://www.mindstudio.ai/blog/rules-file-ai-agents-standing-orders-claude-code) — instructions that don’t evaporate when the context resets.

But the file only works if it’s written to answer the right questions. That’s where most people go wrong.

## The Five-Question Framework

A Claude.md file that actually works answers five specific questions. Each one corresponds to a type of information Claude needs to operate effectively. If you’re missing any of them, you’ll feel it — usually as confusion, repeated corrections, or outputs that are technically fine but miss the point.

Here are the five questions:

We’ll go through each one in detail.

## Question 1: What Is This Project?

This sounds obvious. It isn’t. Most Claude.md files skip it entirely because people assume Claude will infer it from the files in the repo. That assumption is wrong.

Claude doesn’t run a full analysis of your codebase before responding to your first message. It reads your Claude.md file and uses that as the starting frame. If your file says nothing about the project, Claude is working from a blank slate.

What to include:

Example:

`## Project Overview

This is a B2B SaaS application for property management companies. 
It handles tenant communication, maintenance request tracking, and 
lease document storage. The codebase is approximately three years 
old. The frontend is React. The backend is Node with PostgreSQL. 
We're in an active growth phase, adding features to the tenant 
portal while trying to minimize changes to the core lease engine.`

Short. Functional. Gives Claude a meaningful frame before it sees a single line of code.

## Question 2: How Should Claude Behave?

This is where you define the agent’s working style. Not personality quirks — actual behavioral patterns that affect output quality.

Think about the things you find yourself correcting repeatedly. Those are your behavioral rules. Common ones:

## Day one: idea. Day one: app.

Not a sprint plan. Not a quarterly OKR. A finished product by end of day.

![Remy](/remy/lockup-h-sm.svg)

Be specific. “Be concise” means almost nothing. “Keep explanations under three sentences unless I ask for more detail” is actionable.

Example:

`## Behavior Guidelines

- Before starting any task that touches more than one file, summarize 
 your plan in bullet points and wait for confirmation.
- Use TypeScript's strict mode conventions throughout. No `any` types 
 without a comment explaining why.
- When adding new functions, include a JSDoc comment with param types 
 and return type.
- Keep responses short. No preamble. Get to the output.
- If a task is ambiguous, ask one clarifying question — not five.`

This is [prompt engineering](https://www.mindstudio.ai/blog/prompt-engineering-ai-agents) applied at the session level. You’re not writing a prompt for a single task — you’re writing defaults that apply to every task.

## Question 3: What Should Claude Never Do?

Explicit prohibitions matter. Claude is capable and generally sensible, but it will make reasonable choices that sometimes aren’t the right choices for your specific project. The only way to prevent those choices reliably is to name them.

Common prohibitions:

Example:

`## Hard Rules

- Never modify anything in /src/auth/ without explicit confirmation. 
 Auth changes require a separate review step.
- Don't install new npm packages without asking first. List what you'd 
 install and why, then wait.
- Never write inline styles. All styling goes through the design system 
 tokens in /src/styles/tokens.ts.
- Don't delete files. Mark them as deprecated with a comment instead, 
 and flag them for manual removal.`

Think of this as your guardrails layer. [Context rot](https://www.mindstudio.ai/blog/what-is-context-rot-claude-code) — where Claude starts drifting from your standards as a session gets longer — is much less likely when the core prohibitions are written down and loaded at the start. Claude can reference these rules even deep into a long session.

## Question 4: What Does Claude Need to Know About the Codebase?

This is the technical context section. It covers the things Claude would take time to discover on its own, or might get wrong without explicit guidance.

What to include:

Example:

`## Codebase Context

Directory structure:
/src
 /api — Express routes and controllers
 /services — Business logic layer
 /models — Sequelize models (PostgreSQL)
 /frontend — React app (separate build process)
 /scripts — One-off migration and seeding scripts

Key files:
- /src/models/index.ts — exports all models, imports sequelize instance
- /src/config.ts — all environment variable access goes through here, 
 never process.env directly
- /src/services/billing.ts — do not modify without checking with the 
 billing team first

Known issues:
- The `date-fns` library is pinned to 2.29.x due to a breaking change 
 in 3.x that affected our timezone logic. Do not upgrade it.`

## Other agents start typing. Remy starts asking.

Scoping, trade-offs, edge cases — the real work. Before a line of code.

![Remy](/remy/lockup-h-sm.svg)

This layer is what separates a generic agent from one that actually knows your project. When Claude understands [the business brain pattern](https://www.mindstudio.ai/blog/business-brain-pattern-claude-code-shared-brand-context) — where key context is loaded upfront rather than discovered mid-task — it makes faster and better decisions.

## Question 5: What Workflows and Tools Does Claude Use Here?

This section covers process. How do things get done in this project?

Example:

`## Workflows and Tools

Testing:
- Run tests with `npm test` from the root
- Integration tests: `npm run test:integration` (requires running DB)
- Always run tests before marking a task complete

Development:
- Local dev: `npm run dev` (starts both API on :3001 and frontend on :3000)
- Database migrations: `npm run migrate` after any model changes

Linting:
- ESLint and Prettier are configured. `npm run lint:fix` auto-fixes 
 most issues.
- CI will fail on lint errors. Don't skip this.

Git:
- Branch naming: feature/short-description, fix/short-description
- Commit messages follow conventional commits format`

This is especially useful if you’re [building Claude Code skills](https://www.mindstudio.ai/blog/what-are-claude-code-skills) that automate multi-step workflows. The skills can reference the process context in your Claude.md file, which keeps everything consistent.

## How to Format the File

The format matters, but not as much as the content. A few practical rules:

**Use headers to separate sections.** Claude reads your file sequentially. Clear H2 headers make it easy to find and reference specific sections during a session.

**Keep it scannable.** Bullet points over paragraphs wherever you’re listing rules, files, or commands. Claude handles both, but bullet points are faster to scan.

**Put the most important things first.** The project overview and hard rules should appear before the codebase details. If Claude is going to internalize anything, make sure it’s the constraints.

**Keep it honest.** Don’t include things you don’t actually enforce. If you say “always ask before installing packages” and then type “just install it,” you’ve trained Claude to ignore that rule. Write what you’ll actually hold to.

**Length.** There’s no fixed length, but a good Claude.md file is usually between 300 and 800 words. Long enough to be useful, short enough that Claude reads it properly rather than skimming. If yours is approaching 1,000+ words, you probably have detail that belongs in a separate reference file rather than the system prompt.

## Where to Put the File

Claude Code looks for the CLAUDE.md file in your project root by default. The filename is case-insensitive on most systems, but the convention is uppercase `CLAUDE.md`.

`CLAUDE.md`

## Coding agents automate the 5%. Remy runs the 95%.

The bottleneck was never typing the code. It was knowing what to build.

![Remy](/remy/lockup-h-sm.svg)

If you want session-level instructions that override the project-level file, Claude Code also supports a user-level CLAUDE.md in your home directory. That file loads for every session, regardless of project. It’s a good place for personal preferences that stay consistent across all your work — things like “always use British English” or “I prefer verbose output when debugging.”

If you’re running a project with multiple distinct components — say, a separate frontend and backend repo — you can have a CLAUDE.md in each. Claude Code will load whichever one is closest to the working directory.

## The Maintenance Loop

Your Claude.md file isn’t a one-time document. It should evolve with the project.

The most common trigger for an update is the correction loop. When you find yourself correcting Claude for the same thing twice, that’s a signal. Add it to the file. If Claude keeps using `var` when you want `const`, that’s a rule. If Claude keeps generating functions without error handling, that’s a behavioral instruction. Turn corrections into permanent context.

`var`
`const`

This is how [the compounding knowledge loop](https://www.mindstudio.ai/blog/compounding-knowledge-loop-claude-code) actually works in practice. You don’t get a smarter agent by waiting for the model to improve. You get one by systematically capturing what you’ve learned about how the agent needs to be directed.

Some teams do a monthly Claude.md review — just five minutes of scanning to remove outdated instructions and add anything that came up in recent sessions. That’s enough to keep the file accurate.

Claude Code also has an [auto-memory feature](https://www.mindstudio.ai/blog/what-is-claude-code-auto-memory) that can propose updates to your CLAUDE.md based on corrections and patterns it notices during sessions. It’s worth enabling if you want the file to stay current without manual upkeep.

## A Complete Example

Here’s a minimal but complete Claude.md file using the five-question framework:

`# Project

This is an internal inventory management tool for a wholesale 
distributor. It tracks product levels, purchase orders, and supplier 
contacts. The frontend is Vue 3. The backend is a Python FastAPI app. 
Database is PostgreSQL. The project has been running in production for 
18 months.

# Behavior

- Before modifying more than one file, outline the changes and confirm.
- Keep code comments brief. Only comment non-obvious logic.
- Use snake_case for Python, camelCase for JavaScript/TypeScript.
- If I give you a task that's ambiguous, ask one clarifying question 
 before starting.

# Hard Rules

- Never touch /app/auth/ without explicit confirmation.
- Don't modify the database migration files. Create new ones instead.
- Don't add new Python dependencies without listing them and asking first.

# Codebase Context

- /app/models/ — SQLAlchemy models
- /app/routers/ — FastAPI route handlers
- /frontend/src/stores/ — Pinia stores (our global state)
- Known issue: Pillow is pinned to 9.x due to a deployment constraint. 
 Do not suggest upgrading it.

# Workflows

- Run backend: `uvicorn app.main:app --reload`
- Run frontend: `npm run dev` from /frontend
- Tests: `pytest` from the root
- Linting: `ruff check .` for Python, `npm run lint` for frontend`

Clean, direct, and answers all five questions. Claude can load this and have a meaningful frame for the project before the first message.

## How Remy Handles Persistent Context

## Hire a contractor. Not another power tool.

Cursor, Bolt, Lovable, v0 are tools. You still run the project.  
With Remy, the project runs itself.

![Remy](/remy/lockup-h-sm.svg)

If you’ve been working with Claude Code and building up a solid CLAUDE.md practice, you’re already thinking at the right level. The insight — that AI agents need persistent, structured context to do consistent work — is exactly what drives how Remy works.

Remy takes this a step further. Instead of writing context into a markdown file and hoping the agent reads it correctly, Remy uses a spec as the source of truth for the entire application. The spec is annotated prose that both humans and the agent can read and reason about. When you describe how the app should behave, that description stays in sync with the code — it doesn’t drift the way a CLAUDE.md file can drift when the codebase changes faster than the docs.

The effect is that you stop worrying about whether your agent has the right context. It does, because the context is the program.

If you’re curious what that looks like in practice, [try Remy at mindstudio.ai/remy](https://mindstudio.ai/remy).

## Common Mistakes to Avoid

**Writing rules you don’t enforce.** If your CLAUDE.md says “always run tests before marking done” but you routinely skip it, Claude will pick up on the inconsistency and the instruction will lose weight. Only write rules you actually follow.

**Too much detail on things that change.** Specific line numbers, exact function names, current bug statuses — these go stale fast. The CLAUDE.md file should contain stable context, not a changelog.

**Skipping the prohibitions section.** This is the most commonly skipped section and the one that causes the most friction. Without explicit “never do X” rules, Claude makes judgment calls. Sometimes those calls are wrong. Write the list.

**Treating it as a one-time setup.** The file is most valuable when it’s maintained. Budget five minutes every few weeks to keep it current. The payoff is an agent that stays calibrated as the project evolves.

**Putting too much in the root file.** If you have detailed, task-specific instructions, those belong in [skill files](https://www.mindstudio.ai/blog/claude-code-skills-architecture-skill-md-reference-files) or reference documents, not in the CLAUDE.md file. The system prompt should be lean. Load extra context when it’s needed, not upfront for every session.

## FAQ

### What is a Claude.md file?

A CLAUDE.md file is a markdown document that Claude Code loads at the start of every session. It functions as a system prompt — providing Claude with persistent context about your project, your preferences, and any rules it needs to follow. Without it, Claude starts each session with no memory of previous work. With it, Claude operates within a defined frame that you set and maintain.

### Where does the Claude.md file go?

Place it in your project root directory. The filename is typically `CLAUDE.md` (uppercase). Claude Code will also read a user-level CLAUDE.md from your home directory, which applies across all projects. If you have multiple CLAUDE.md files at different directory levels, Claude Code loads the one closest to the current working directory.

`CLAUDE.md`

### How long should a Claude.md file be?

The one that tells the coding agents what to build.

![Remy](/remy/lockup-h-sm.svg)

Most effective CLAUDE.md files are between 300 and 800 words. If you’re going longer, consider whether some content belongs in a separate reference file instead. The system prompt should load quickly and be easy for Claude to process at the start of every session — not a comprehensive manual for the entire project.

### How often should I update the Claude.md file?

Update it whenever you find yourself correcting Claude for the same issue twice. That’s the main trigger. A monthly review — five to ten minutes to remove outdated instructions and add new ones — is usually enough for active projects. You can also enable [Claude Code’s auto-memory feature](https://www.mindstudio.ai/blog/what-is-claude-code-auto-memory) to get suggested updates based on patterns Claude notices in your sessions.

### Can I have multiple Claude.md files in one project?

Yes. Claude Code supports CLAUDE.md files at multiple directory levels. In a monorepo, you might have a root-level file covering shared context and separate files in each package directory covering package-specific rules. Claude loads the most local file for the current working directory.

### Is the Claude.md file the same as a system prompt?

Functionally, yes. It’s the closest equivalent in a Claude Code workflow to a system prompt in a chat API call. The difference is that you maintain it as a file in your project rather than passing it programmatically. If you’re used to thinking about [prompt engineering for developers](https://www.mindstudio.ai/blog/prompt-engineering-for-developers), the CLAUDE.md file is where your persistent prompt engineering lives.

## Key Takeaways

## Related Articles

![](https://i.mscdn.ai/70cbb1ad-08d7-4fdc-ab31-e343780966a6/generated-images/c91f1552-8b94-4906-aab6-3511b7b2cf5b.png?fm=auto&w=1200&fit=cover)

### Claude Code Skills vs Slash Commands: When to Use Each

Claude Code Skills auto-invoke based on context while slash commands require manual triggers. Learn the difference and when each approach wins.

![](https://i.mscdn.ai/70cbb1ad-08d7-4fdc-ab31-e343780966a6/generated-images/4d16e693-b9d5-4018-b616-078f8c6cbd45.png?fm=auto&w=1200&fit=cover)

### Claude Code Skills: How to Build Standard Operating Procedures for Your AI Agent

Claude Code skills are reusable process documents that load context at the right time. Learn how to build skills that produce expert-level outputs.

![](https://i.mscdn.ai/70cbb1ad-08d7-4fdc-ab31-e343780966a6/generated-images/99b1a97b-0ebb-4675-abcf-a7affe57ce57.png?fm=auto&w=1200&fit=cover)

### What Is the Claude.md File and Why It's the Most Important Part of Your AI Agent

The claude.md file acts as your AI agent's system prompt and memory. Learn how to write one that makes Claude Code produce consistent, high-quality results.

![](https://i.mscdn.ai/70cbb1ad-08d7-4fdc-ab31-e343780966a6/generated-images/def6c6cc-f03c-4bdb-9f10-9adb1d679edb.png?fm=auto&w=1200&fit=cover)

### What Is the Claude.md File and Why Does It Matter for AI Agents?

The claude.md file acts as your AI agent's system prompt, loaded at the start of every session. Learn how to write one that actually improves output quality.

Presented by MindStudio

## 

No spam. Unsubscribe anytime.

You're in! Check your inbox.

Get weekly AI insights from MindStudio

### Compare

### Use Cases

### Capabilities

### MindStudio

### Programs
