# How to Use Git Worktrees with Claude Code for Parallel Development

**Type:** article
**URL:** https://www.mindstudio.ai/blog/git-worktrees-claude-code-parallel-development/
**Topic:** Git Worktrees
**Published:** unknown

## Content

![MindStudio](/MindStudio-lockup-blk.svg)
![MindStudio](/MindStudio-lockup-blk.svg)

# How to Use Git Worktrees with Claude Code for Parallel Development

Git worktrees let multiple Claude Code agents work on separate branches simultaneously. Learn how to set them up, isolate databases, and avoid port conflicts.

![How to Use Git Worktrees with Claude Code for Parallel Development](https://i.mscdn.ai/70cbb1ad-08d7-4fdc-ab31-e343780966a6/generated-images/cc93d407-10ef-4b73-a1a8-3a9b85c10d53.png?fm=auto&w=1200&fit=cover?fm=auto&w=1200&fit=cover)

## Why Sequential AI Development Is Holding You Back

Running Claude Code one feature at a time is like having a team of developers and only letting one person work at once. The capability is there. The bottleneck is artificial.

Git worktrees change that. With worktrees, you can run multiple Claude Code agents simultaneously — each on its own branch, in its own directory, with its own database and ports. One agent handles the auth refactor while another builds the payment flow. Neither waits for the other.

This guide covers how to set up Git worktrees for parallel Claude Code development, how to isolate databases per worktree, and how to eliminate port conflicts so everything runs cleanly at the same time.

If you’re new to Git concepts, [what Git is and how version control works](https://www.mindstudio.ai/blog/what-is-git-version-control-explained) is a solid primer before continuing.

## What Git Worktrees Are (and Why They Matter Here)

A Git worktree is a separate working directory linked to the same Git repository. It’s not a full clone. It shares the `.git` folder and the object store with your main repo, but it checks out a different branch into a different directory on disk.

`.git`

Normally, one Git repo means one checked-out branch at a time. Worktrees remove that constraint. You can have:

`my-project/ ← main branch checked out here
my-project-auth/ ← feature/auth-refactor checked out here
my-project-payments/ ← feature/payment-flow checked out here`

## Day one: idea. Day one: app.

Not a sprint plan. Not a quarterly OKR. A finished product by end of day.

![Remy](/remy/lockup-h-sm.svg)

All three are the same repo. All three can run simultaneously. And all three can have an independent Claude Code session running inside them.

This is the foundation of [the Claude Code git worktree pattern](https://www.mindstudio.ai/blog/claude-code-git-worktree-parallel-branches) — using filesystem isolation to let multiple AI agents work on the same codebase without stepping on each other.

## Prerequisites

Before setting up worktrees, make sure you have:

## Step-by-Step: Setting Up Git Worktrees for Parallel Claude Code

### Step 1: Create a Worktree for Each Feature

From your main project directory, create worktrees for each feature branch you want to work on simultaneously.

`# Create a worktree for a new branch
git worktree add ../my-project-auth -b feature/auth-refactor

# Create another worktree for a different branch
git worktree add ../my-project-payments -b feature/payment-flow`

The first argument is the path to the new directory. The `-b` flag creates a new branch checked out into that directory. If the branch already exists, drop the `-b` and just specify the branch name:

`-b`
`-b`
`git worktree add ../my-project-auth feature/auth-refactor`

To list all your active worktrees:

`git worktree list`

### Step 2: Install Dependencies in Each Worktree

Each worktree directory is a full working copy of your project files, but it doesn’t inherit `node_modules` or other generated artifacts. Run your install step in each directory:

`node_modules`
`cd ../my-project-auth && npm install
cd ../my-project-payments && npm install`

For large projects, you can use `npm ci` instead of `npm install` for faster, reproducible installs. Some teams also symlink a shared `node_modules` directory across worktrees to save time and disk space — this works for many projects, but can cause issues if dependencies vary across branches.

`npm ci`
`npm install`
`node_modules`

### Step 3: Configure Environment Variables Per Worktree

Each worktree needs its own `.env` file (or equivalent) with environment variables that differ from the main project. At minimum, you need different values for:

`.env`

Copy your main `.env` file into each worktree and modify the relevant values:

`.env`
`cp .env ../my-project-auth/.env
cp .env ../my-project-payments/.env`

Then edit each copy — covered in detail in the sections below.

### Step 4: Open Claude Code in Each Worktree

In separate terminal windows or tabs, navigate to each worktree directory and start Claude Code:

`# Terminal 1
cd ../my-project-auth
claude

# Terminal 2
cd ../my-project-payments
claude`

Each session is independent. Claude Code reads the directory it’s launched from. The agents don’t share context, don’t share state, and can’t interfere with each other’s work.

This is the foundation of [running parallel Claude Code sessions](https://www.mindstudio.ai/blog/claude-code-parallel-sessions) across multiple features simultaneously.

## Isolating Databases Per Worktree

Database isolation is the part people get wrong most often. If two agents share the same database, they’ll conflict — running migrations that step on each other, writing test data that poisons the other agent’s work, or causing hard-to-debug schema inconsistencies.

The right approach depends on your database.

### SQLite

## Not a coding agent. A product manager.

Remy doesn't type the next file. Remy runs the project — manages the agents, coordinates the layers, ships the app.

![Remy](/remy/lockup-h-sm.svg)

SQLite is file-based, so isolation is straightforward. Point each worktree to a different database file:

`# .env in my-project-auth/
DATABASE_URL=./db/auth-dev.sqlite

# .env in my-project-payments/
DATABASE_URL=./db/payments-dev.sqlite`

Since each worktree is a separate directory, you can also use the same relative path in each `.env` file — they resolve to different absolute paths:

`.env`
`# Both use ./dev.sqlite, but resolve to different files
DATABASE_URL=./dev.sqlite`

This is the simplest approach. Just make sure `./dev.sqlite` isn’t tracked by Git so you don’t accidentally commit a test database.

`./dev.sqlite`

### PostgreSQL

With PostgreSQL, create a separate database for each worktree:

`CREATE DATABASE myproject_auth_dev;
CREATE DATABASE myproject_payments_dev;`

Then update the database name in each worktree’s `.env`:

`.env`
`# .env in my-project-auth/
DATABASE_URL=postgresql://localhost:5432/myproject_auth_dev

# .env in my-project-payments/
DATABASE_URL=postgresql://localhost:5432/myproject_payments_dev`

Run migrations independently in each worktree after creating the databases:

`cd ../my-project-auth && npm run db:migrate
cd ../my-project-payments && npm run db:migrate`

### MySQL / MariaDB

Same principle as PostgreSQL — create a named database per worktree and reference it in the connection string. You can script this if you’re creating worktrees frequently:

`#!/bin/bash
# create-worktree.sh
FEATURE=$1
git worktree add ../my-project-$FEATURE -b feature/$FEATURE
mysql -u root -e "CREATE DATABASE IF NOT EXISTS myproject_${FEATURE}_dev;"
cp .env ../my-project-$FEATURE/.env
sed -i "s/myproject_dev/myproject_${FEATURE}_dev/" ../my-project-$FEATURE/.env
cd ../my-project-$FEATURE && npm install && npm run db:migrate`

This kind of automation pays off quickly when you’re creating worktrees regularly.

## Avoiding Port Conflicts

If your application starts a dev server, test runner, or any other process that binds to a network port, parallel worktrees will collide unless each uses different port assignments.

The main ports to think about:

### Assign Port Ranges Per Worktree

A simple convention: offset ports by a fixed increment for each worktree. For example:

| Worktree | Dev Server | API Server |
| --- | --- | --- |
| main | 3000 | 3001 |
| auth-refactor | 3010 | 3011 |
| payment-flow | 3020 | 3021 |

In each worktree’s `.env`:

`.env`
`# .env in my-project-auth/
PORT=3010
API_PORT=3011

# .env in my-project-payments/
PORT=3020
API_PORT=3021`

Your application code should read these from environment variables rather than hardcoding them. If your framework uses a config file, update it to respect `process.env.PORT`.

`process.env.PORT`

### Using the PORT Environment Variable Inline

If you don’t want to edit `.env` files, you can override the port at startup time:

`.env`
`PORT=3010 npm run dev`

Claude Code will pick up on this when running commands. You can also set it as part of your workspace configuration or pass it in your instructions to the agent.

### Checking for Port Conflicts

Before starting a new worktree session, verify the ports you plan to use aren’t already in use:

`# macOS / Linux
lsof -i :3010

# Windows
netstat -ano | findstr :3010`

If something is already bound to the port, you’ll need to either kill that process or pick a different port.

## Managing Multiple Claude Code Agents Effectively

Running worktrees in parallel is only useful if you can keep track of what each agent is doing. A few practices that help.

## Remy doesn't write the code. It manages the agents who do.

Remy runs the project. The specialists do the work. You work with the PM, not the implementers.

![Remy](/remy/lockup-h-sm.svg)

### Use Clear Branch and Directory Naming

Your directory names tell you at a glance what’s in each worktree. Use names that match the feature, ticket number, or both:

`my-project-feat-123-auth/
my-project-feat-456-payments/
my-project-bugfix-789-login/`

### Give Each Agent a Focused Task

Claude Code works best with clear, bounded instructions. When launching a parallel session, give each agent a specific task rather than a broad mandate. “Refactor the authentication middleware to use JWT” is better than “improve authentication.”

This also helps with [context rot](https://www.mindstudio.ai/blog/context-rot-ai-coding-agents-explained) — the degradation in response quality that happens when a conversation thread gets too long. Focused tasks keep contexts lean.

### Coordinate with a Shared Task File

For teams or complex multi-agent setups, a `TASKS.md` file at the repo root (tracked in Git) can serve as a coordination mechanism. Each agent reads from and writes to the task list as it progresses. This is the approach described in more detail in the [Claude Code agent teams pattern for parallel collaboration](https://www.mindstudio.ai/blog/claude-code-agent-teams-parallel-collaboration).

`TASKS.md`

### Merging Worktrees Back

When an agent finishes its work, you merge the branch back to main through a normal pull request or direct merge:

`# From main worktree
git merge feature/auth-refactor

# Or create a PR in your standard workflow`

Then remove the worktree and clean up the branch:

`git worktree remove ../my-project-auth
git branch -d feature/auth-refactor`

## Common Mistakes and How to Fix Them

### Shared Config Files Getting Modified

If a config file is part of the repo and both worktrees modify it, you’ll get merge conflicts. Either avoid modifying shared config files in feature branches, or use environment-variable-based config that’s excluded from version control.

### Migrations Running Against the Wrong Database

This usually happens when the `DATABASE_URL` in `.env` hasn’t been updated in the worktree. Double-check the environment variables before running migrations. A quick `echo $DATABASE_URL` after activating your environment is a good habit.

`DATABASE_URL`
`.env`
`echo $DATABASE_URL`

### Forgetting to Install Dependencies

When switching to a branch that has new packages added, `node_modules` in the worktree may be out of date. Run `npm install` (or your equivalent) after switching or creating a worktree on a branch with recent dependency changes.

`node_modules`
`npm install`

### Running Out of Worktrees to Track

Git doesn’t impose a limit on worktrees, but it’s easy to accumulate stale ones. Periodically run `git worktree list` and prune old ones with `git worktree remove` and `git worktree prune`.

`git worktree list`
`git worktree remove`
`git worktree prune`

## Combining Worktrees with Other Parallel Patterns

Worktrees aren’t the only way to run Claude Code in parallel. They’re the right tool when you need branch-level isolation — different features on different branches, each with independent state.

For different scenarios, other patterns apply:

Understanding which pattern fits which scenario makes a real difference. The [Claude Code agentic workflow patterns overview](https://www.mindstudio.ai/blog/claude-code-agentic-workflow-patterns) covers the full landscape.

![](/remy/logo-64.svg)

Introducing Remy

Ship a working app before your next meeting.

Remy handles the infrastructure. You describe what the app does, and it builds it end-to-end.

01

Describe

Write the spec

02

Compile

Remy builds it

03

Preview

Run in browser

04

Deploy

Live on a URL

For managing cost across parallel sessions, [token budget management](https://www.mindstudio.ai/blog/ai-agent-token-budget-management-claude-code) is worth reviewing — parallel agents burn through API credits faster than sequential workflows.

## Where Remy Fits In

Worktrees solve a real problem in Claude Code workflows, but they also expose a more fundamental limitation: you’re still working at the code level. The agent edits TypeScript, you review diffs, manage conflicts, and coordinate branches.

Remy approaches this differently. Instead of working from code, you work from a spec — an annotated markdown document that describes what the application does. The code is compiled output. When you want to change the app, you change the spec.

This shifts where parallel work happens. You’re not managing multiple branches with diverging code. You’re editing different sections of a structured document. Remy handles the compilation, the backend, the database schema, the auth system, and the deployment. The infrastructure runs on MindStudio’s platform — the same stack that’s been running production AI workloads for years.

If you’re spending significant time coordinating Git branches, managing port configs, and syncing worktree databases, it’s worth asking whether the right abstraction is a better worktree setup or a different starting point entirely.

You can try Remy at [mindstudio.ai/remy](https://mindstudio.ai/remy).

## Frequently Asked Questions

### Can I use Git worktrees with any project type?

Yes. Git worktrees work with any Git repository regardless of language or framework. The setup steps — creating the worktree, configuring environment variables, managing ports — apply equally to Node.js, Python, Go, Ruby, or any other stack. The specifics of database isolation may vary by database type, but the principle is the same.

### Do Git worktrees use more disk space?

Not significantly. Worktrees share the Git object store with the main repo, so you’re not duplicating the entire repository. What you do get for each worktree is a separate copy of your working files and `node_modules`. The files themselves are typically small; `node_modules` is the expensive part. For disk-constrained environments, symlinking a shared `node_modules` directory can help.

`node_modules`
`node_modules`
`node_modules`

### Can multiple Claude Code agents write to the same files across worktrees?

Each worktree checks out a different branch, so each agent writes to its own version of the files. When you merge branches back to main, you’ll resolve any conflicts through the normal Git merge or rebase process. Agents in different worktrees don’t directly conflict in real time — the conflict surface appears at merge time, just as it would with any multi-developer workflow.

### How many worktrees can I run at once?

Git doesn’t impose a hard limit. The practical limit is your machine’s resources: RAM, CPU, and disk space. Each running dev server and Claude Code session consumes memory. On a modern development machine with 16GB+ RAM, 3–5 simultaneous worktrees with active processes is typical. More than that and you’ll start to feel the constraint.

### What happens if two worktrees modify shared config files?

## Hire a contractor. Not another power tool.

Cursor, Bolt, Lovable, v0 are tools. You still run the project.  
With Remy, the project runs itself.

![Remy](/remy/lockup-h-sm.svg)

You’ll get merge conflicts when you try to merge both branches back to main. The cleanest solution is to move shared config values into environment variables (excluded from version control) so the config files in the repo don’t need to change per feature. If you must modify shared config in a feature branch, coordinate the merge order and resolve conflicts manually.

### Is this the same as just cloning the repo multiple times?

Similar outcome, different mechanics. A full clone creates a separate Git database for each copy — more disk space, no shared history, and no built-in coordination. Worktrees share the Git object store. That means branches stay synchronized, `git fetch` in one worktree updates all of them, and pruning old branches is cleaner. For parallel AI development, worktrees are generally the better choice over full clones.

`git fetch`

## Key Takeaways

`.env`
`.env`
`git worktree list`
`git worktree remove`
`git worktree prune`

For a fundamentally different approach to parallel full-stack development — one that starts from a spec rather than a codebase — [try Remy](https://mindstudio.ai/remy).

## Related Articles

![](https://i.mscdn.ai/70cbb1ad-08d7-4fdc-ab31-e343780966a6/generated-images/f0830b99-4426-4238-8210-145ffdeb2965.png?fm=auto&w=1200&fit=cover)

### How to Run Parallel AI Coding Agents With Git Worktrees

Run multiple Claude Code sessions simultaneously without conflicts. This guide covers git worktrees, database branching, and port isolation for parallel agents.

![](https://i.mscdn.ai/70cbb1ad-08d7-4fdc-ab31-e343780966a6/generated-images/0d3cf2ee-6178-4472-b778-f25795c18283.png?fm=auto&w=1200&fit=cover)

### How to Set Up Claude Code on Mac and Windows: Complete Installation Guide

Install Claude Code on Mac or Windows step by step. Covers VS Code, Git, Node.js, permissions, and connecting your Claude subscription to get started fast.

![](https://i.mscdn.ai/70cbb1ad-08d7-4fdc-ab31-e343780966a6/generated-images/3c6f08aa-9c57-4166-8a10-66192d6e68ef.png?fm=auto&w=1200&fit=cover)

### How to Set Up a Managed Database for Your Web App

A practical guide to choosing and setting up a managed database for your web app — covering SQL vs NoSQL, migrations, and what to look for.

![](https://i.mscdn.ai/70cbb1ad-08d7-4fdc-ab31-e343780966a6/generated-images/fb3a86af-23fa-4846-85f2-506e21ca511d.png?fm=auto&w=1200&fit=cover)

### How to Use AI to Build a Web App Faster

A practical guide to using AI tools to build web apps faster — covering where AI helps most, where it falls short, and how to avoid common traps.

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
