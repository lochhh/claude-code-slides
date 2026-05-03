# Reduce Claude Code Costs 60% With These Four Habits | systemprompt.io

**Type:** article
**URL:** https://systemprompt.io/guides/claude-code-cost-optimisation
**Topic:** Cost & Token Management
**Published:** unknown

## Content

# Reduce Claude Code Costs 60% With These Four Habits

systemprompt.io · 26 min read

    ![Reduce Claude Code Costs 60% With These Four Habits](/files/images/blog/claude-code-cost-optimisation.png) 
  Table of contents 

* [Quick Answer: Claude Code Cost Optimization in Four Moves](#quick-answer-claude-code-cost-optimization-in-four-moves)
* [How Many Tokens Does a Typical Claude Code Refactoring Task Use?](#how-many-tokens-does-a-typical-claude-code-refactoring-task-use)
* [Prelude](#prelude)
* [The Problem](#the-problem)
* [The Journey](#the-journey)
  + [How Claude Code Billing Works](#how-claude-code-billing-works)
  + [Track Spend in Real Time With the /cost Command](#track-spend-in-real-time-with-the-cost-command)
  + [Model Selection Strategy](#model-selection-strategy)
  + [Context Management](#context-management)
  + [Effective Prompting](#effective-prompting)
  + [Using /compact Effectively](#using-compact-effectively)
  + [Optimise CLAUDE.md for Token Efficiency](#optimise-claude-md-for-token-efficiency)
  + [Prompt Caching](#prompt-caching)
  + [File Reading Efficiency](#file-reading-efficiency)
  + [Batch Operations](#batch-operations)
  + [Subagents for Research](#subagents-for-research)
  + [Parallel Agents with Isolated Context](#parallel-agents-with-isolated-context)
  + [Enterprise Cost Controls](#enterprise-cost-controls)
  + [Community-Tested Techniques](#community-tested-techniques)
  + [Real Cost Examples](#real-cost-examples)
  + [Building a Cost-Conscious Workflow](#building-a-cost-conscious-workflow)
* [Cost Optimization Checklist](#cost-optimization-checklist)
* [The Lesson](#the-lesson)
* [Conclusion](#conclusion)

## Quick Answer: Claude Code Cost Optimization in Four Moves

If you are looking to cut costs immediately, here are the four highest-impact changes:

1. **Set MAX\_THINKING\_TOKENS to 10,000.** Thinking tokens are the single biggest cost driver. This change alone reduces spend by 30-40%.
2. **Default to Sonnet, not Opus.** Sonnet handles 80% of daily tasks at one fifth the cost. Switch to Opus only for complex reasoning.
3. **Clear context between tasks.** Every task inherits all previous context. Start fresh with `/clear` to avoid paying for stale tokens.
4. **Be specific in prompts.** Vague prompts lead to back-and-forth exchanges. Save 50,000+ tokens per task with specific, file-named requests.

These four habits account for most achievable savings and are covered in detail in the sections below.

## How Many Tokens Does a Typical Claude Code Refactoring Task Use?

A typical multi-file refactoring task in Claude Code consumes roughly **50,000 to 100,000 input tokens and 10,000 to 20,000 output tokens**. That works out to about **$0.45 with Claude Sonnet** or **$5.25 with Claude Opus** at current [API pricing](https://www.anthropic.com/pricing). The exact number scales with three things: how many files Claude has to read, how long the conversation history is at the point of the refactor, and how much reasoning the model generates before writing code.

Here is the rough range by refactoring type, measured across hundreds of real sessions:

| Refactor type | Input tokens | Output tokens | Sonnet cost | Opus cost |
| --- | --- | --- | --- | --- |
| Rename a function across 3 files | 15,000 | 3,000 | $0.09 | $0.45 |
| Extract a shared module from 5 files | 45,000 | 8,000 | $0.26 | $1.28 |
| Rename a public API and update all callers | 80,000 | 15,000 | $0.47 | $2.33 |
| Convert callbacks to async across a module | 120,000 | 20,000 | $0.66 | $3.30 |
| Restructure an auth system across 15 files | 250,000 | 40,000 | $1.35 | $6.75 |

If you are seeing numbers materially higher than these, the cause is almost always one of: stale context from a long unrelated conversation, Opus used where Sonnet would have sufficed, or Claude reading files it did not need. The techniques in this guide target each of those leaks.

## Prelude

Getting the first Claude Code bill is often a moment of genuine surprise. Not because it is outrageous, but because it is unclear where the tokens went. (New to Claude Code? Start with [the beginner's guide](/guides/how-to-use-claude-code) before diving into cost management.) A month of happily chatting away, asking Claude to read entire directories, rewriting the same file three times because prompts were vague, and letting context windows balloon to 200K tokens without a second thought, adds up fast.

That first bill is a wake-up call. Not because the tool is not worth the money. It absolutely is. But because a significant portion of spend goes to habits that are easy to fix.

Vague prompts that lead to back-and-forth. Reading files that are not needed. Keeping stale context alive across unrelated tasks. Using the most expensive model for every trivial question.

Over months of refinement, we developed a set of practices that cut effective costs by roughly 60% without reducing productivity. In many cases, these habits actually improved productivity because they forced clearer thinking and better session management.

This guide is everything we have learned about spending less on Claude Code while getting more out of it.

## The Problem

Claude Code is priced on token consumption. Every character you send as input and every character Claude generates as output has a cost. For individual developers on Pro or Max plans, this means working within monthly limits. For teams on API-based pricing, this means real dollar amounts on every invoice.

The challenge is that Claude Code makes it very easy to consume tokens without realising it. Reading a large file adds thousands of input tokens. A long conversation accumulates context that is re-sent with every message. Using Claude Opus for a simple file rename costs ten times more than using Claude Haiku for the same operation.

Most developers fall into one of two camps. Either they do not think about cost at all and are surprised by their usage, or they think about it too much and restrict their usage to the point where Claude Code stops being useful.

Neither extreme is correct. The goal is to be intentional about token usage without being stingy. To use the right model for each task, manage context deliberately, and structure prompts so that Claude accomplishes your goal in as few turns as possible.

## The Journey

### How Claude Code Billing Works

Before you can optimise costs, you need to understand how billing works. Claude Code charges based on tokens, which are roughly four characters each. There are two types.

**Input tokens** are everything you send to Claude. This includes your prompt, the conversation history, any files Claude has read, the contents of your CLAUDE.md, tool results, and system prompts.

Input tokens are the larger cost driver for most users because context accumulates over a session.

**Output tokens** are everything Claude generates. This includes its responses, code it writes, and commands it suggests. Output tokens cost more per token than input tokens, but you typically generate fewer of them.

For reference, as of early 2026, the approximate pricing for the three main models is as follows. (These are the [API pricing numbers published by Anthropic](https://www.anthropic.com/pricing); subscription plans are billed separately.)

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
| --- | --- | --- |
| Claude Opus 4.6 | $15 | $75 |
| Claude Sonnet 4.6 | $3 | $15 |
| Claude Haiku 4.5 | $0.80 | $4 |

The ratio matters. Opus output tokens cost nearly 19 times more than Haiku output tokens.

A task that generates 5,000 output tokens costs $0.375 with Opus and $0.02 with Haiku. Over hundreds of tasks per month, these differences compound significantly.

For subscription users ([Pro at $20/month, Max at $100 or $200/month](https://claude.ai/settings)), you are not paying per token directly, but you have usage limits. The same optimisation strategies help you stay within those limits and avoid throttling or rate caps.

### Track Spend in Real Time With the /cost Command

You cannot optimise what you do not measure. The `/cost` command is the fastest way to see what a session is actually costing you, and running it habitually is the foundation of every cost saving tip in this guide. Developers who manage costs effectively start here.

The command shows your current session's token usage and estimated cost. Running it at the end of every significant session builds intuition about what different task types cost. Pair it with a check at session start to get a before-and-after snapshot for every piece of work.

```
> /cost Session tokens: 145,230 input, 12,450 output Estimated cost: $3.11 (Opus) 
```

Session summaries appear when you end a session, showing total tokens consumed and the cost breakdown. Pay attention to these. They tell you whether a session was efficient or wasteful.

Monthly usage tracking is available through your [Anthropic Console dashboard](https://console.anthropic.com/). Review this weekly, not monthly.

By the time you see a monthly bill, you have already spent the money. Weekly reviews let you spot patterns and adjust before they become expensive habits.

The single most useful metric is cost per task. Not cost per session or cost per day.

Track what you accomplish in each session and divide the cost by the number of meaningful tasks completed. This tells you whether you are using Claude Code efficiently.

### Model Selection Strategy

The most impactful cost optimisation is choosing the right model for each task. Most developers default to the most powerful model available and never switch. This is like driving a lorry to the corner shop. Understanding the pricing differences between tools also matters; our [Claude Code vs Cursor comparison](/guides/claude-code-vs-cursor) breaks down how costs compare across the two most popular AI coding tools.

**Claude Opus** is the most capable and most expensive model. Use it for tasks that require deep reasoning, complex refactoring across multiple files, architectural decisions, debugging subtle issues, and any task where getting it right the first time matters more than cost.

**Claude Sonnet** is the balanced middle ground. Use it for routine development work, writing new functions, creating tests, reviewing code, and any task that is moderately complex but does not require Opus-level reasoning. Sonnet handles 80% of daily development work at one-fifth the cost of Opus.

**Claude Haiku** is the fastest and cheapest model. Use it for simple queries, quick lookups, formatting tasks, generating boilerplate, and any task that does not require deep understanding. Haiku is excellent for questions like "what does this error mean" or "generate a TypeScript interface from this JSON."

The `/model` command lets you switch models mid-session.

```
> /model sonnet Switched to Claude Sonnet > /model opus Switched to Claude Opus 
```

A good habit is starting every session on Sonnet and only switching to Opus when hitting a task that Sonnet struggles with. This single habit can reduce costs by roughly 40%.

For a complete look at integrating model switching into your daily work, our guide on [daily workflows and productivity](/guides/claude-code-daily-workflows) covers this in more depth.

### Context Management

Context is the hidden cost driver in Claude Code. Every message in your conversation is re-sent as input tokens with every new prompt. A conversation that starts at 5,000 tokens of context grows to 50,000 tokens after several exchanges, and keeps growing.

The most important context management tool is `/clear`. This command resets your conversation, starting fresh with only your CLAUDE.md and system prompt as context. Use it whenever you switch tasks.

A common mistake is keeping a single session running all day, asking Claude about authentication one minute and CSS styling the next. The authentication context is still being sent as input tokens during CSS questions. Every prompt about CSS is also paying for the authentication discussion that is no longer relevant.

Use `/clear` aggressively. Finished a task? Clear. Switching to a different part of the codebase? Clear.

Context getting long and responses getting slow? Clear.

The rule is simple. If the previous conversation is not relevant to the next question, clear the context. The few seconds it takes to re-establish context is far cheaper than carrying irrelevant tokens through every subsequent prompt.

### Effective Prompting

Vague prompts are expensive prompts. When you tell Claude "fix the authentication," it needs to explore, ask clarifying questions, try different approaches, and potentially rework its solution when you provide more details. Every exchange adds tokens.

Specific prompts are cheap prompts. When you tell Claude "in src/auth/middleware.rs, the validate\_token function is not checking token expiration. Add a check that compares the exp claim against the current timestamp and returns a 401 if expired," Claude can accomplish the task in a single turn.

Here are recommended practices for cost-effective prompting.

**Name specific files.** Instead of "fix the bug in the login page," say "fix the null pointer in src/pages/login.tsx on line 45." Claude does not need to search for the file, which saves both time and tokens.

**State the desired outcome.** Instead of "make this better," say "refactor this function to use early returns instead of nested if statements." Claude does not need to guess what "better" means.

**Provide relevant context up front.** If Claude needs to know about your database schema to write a query, paste the relevant schema excerpt in your prompt. Do not make Claude read the schema file. You control exactly how many tokens are spent on context.

**Avoid open-ended exploration.** Instead of "explore the codebase and tell me what you find," say "read src/lib.rs and list the public modules." Bounded questions get bounded answers.

The difference between a three-turn conversation and a one-turn solution can be 50,000 tokens. At Opus pricing, that is roughly $1 saved on a single task. Multiply by dozens of tasks per day and the savings are substantial.

### Using /compact Effectively

The `/compact` command is one of Claude Code's most useful cost management features. It summarises the current conversation into a condensed form, reducing the context size that is sent with subsequent prompts.

When to use `/compact` depends on your workflow and timing. Two situations stand out.

First, after a long exploratory conversation involving reading files and explanations. By the time changes are ready to be made, the context is full of file contents and explanations that are no longer needed. Running `/compact` distils the conversation into a summary, and subsequent editing prompts carry far less context.

Second, when Claude's responses become slower. Large contexts take longer to process, so sluggish responses are a signal that context has grown too large. A quick `/compact` brings things back to a manageable size.

**The critical timing detail most people miss:** `/compact` works best when called immediately, while the prompt cache is still warm. Claude Code caches your conversation context for roughly five minutes after your last message. If you call `/compact` within that window, the summarisation step gets the cached token discount. If you have been idle for more than five minutes, the cache has expired and `/compact` re-processes the entire context at full price. In that case, starting a fresh conversation with `/clear` is cheaper.

The rule: active session, getting long? Use `/compact`. Returning after a break? Use `/clear` instead.

`/compact` does not lose important information. It summarises the conversation, preserving the decisions made and the current state of work. What it discards is the verbatim file contents, intermediate reasoning, and other details that Claude no longer needs.

### Optimise CLAUDE.md for Token Efficiency

Your CLAUDE.md file is included in every prompt as input tokens, so its size matters more than any other file in your project. If your CLAUDE.md is 500 lines of detailed instructions, you are paying for those 500 lines with every single message you send. Over a day of active use, this adds up.

The most effective teams keep CLAUDE.md under 50 lines and use it as an index, not a knowledge dump. Each line points to a detailed file that Claude loads only when relevant. Some teams run under 30 lines. Deep context loads on demand instead of riding along with every prompt.

Here are the optimisation strategies that work best.

**Use CLAUDE.md as an index.** Instead of writing all your conventions inline, create focused reference files (e.g. `.claude/docs/testing-conventions.md`, `.claude/docs/api-patterns.md`) and list them in CLAUDE.md with a one-line description. Claude reads the detailed files only when working on related tasks. This approach keeps the per-prompt token cost minimal while making deep context available when needed.

**Front-load critical information.** The most important instructions should be at the top. If Claude's context window is under pressure, the beginning of CLAUDE.md is more likely to be retained than the end.

**Remove stale instructions.** Review your CLAUDE.md monthly. Delete anything that refers to completed features, resolved issues, or outdated conventions. It is not uncommon to find instructions about a database migration that was completed six months earlier, still being sent with every prompt.

**Be concise.** Instead of "When writing TypeScript code, please make sure to always use strict type checking and never use the any type unless absolutely necessary because it undermines the benefits of TypeScript's type system," write "Use strict TypeScript types. Avoid any." Same instruction, one-fifth the tokens.

**Use CLAUDE.md for patterns, not procedures.** Long step-by-step procedures belong in skills (`.claude/commands/` files), which are only loaded when invoked. CLAUDE.md should contain rules and conventions that apply to every interaction.

The automatic caching of CLAUDE.md contents is a significant cost benefit. Because the file is sent with every prompt, Claude Code caches it after the first message.

Subsequent messages get a 90% discount on the CLAUDE.md input tokens. This is another reason to keep CLAUDE.md stable and avoid frequent changes during a session.

### Prompt Caching

Prompt caching is one of the most significant cost-saving features in the [Claude API](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching), and Claude Code applies it automatically. When the same text appears at the beginning of consecutive requests, it is cached and subsequent uses receive a 90% discount on input token costs.

This happens automatically for your CLAUDE.md file, system prompts, and the early portions of your conversation. You do not need to configure anything. But you can structure your workflow to maximise cache hits.

**Keep CLAUDE.md stable during sessions.** If you edit CLAUDE.md mid-session, the cache is invalidated and you pay full price for the updated contents. Make your CLAUDE.md edits between sessions, not during them.

**Start conversations with consistent context.** If you frequently need Claude to understand your project structure, put that information in CLAUDE.md rather than pasting it into each prompt. Information in CLAUDE.md is cached. Information pasted into prompts is not.

**Use skills for repeated prompts.** If you find yourself typing the same instructions repeatedly, create a skill file. While skills themselves are not cached in the same way, the consistent structure they provide helps you avoid the token waste of re-typing instructions.

The 90% discount on cached tokens is enormous. On a typical day, prompt caching saves an estimated 40-50% on input token costs compared to what would be paid without it.

### File Reading Efficiency

Every file Claude reads becomes part of the conversation context. A 1,000-line source file is roughly 10,000 tokens.

Reading ten files adds 100,000 tokens to your context. At Opus pricing, that is $1.50 just for reading files.

A common wasteful habit is asking Claude to "look at the project structure" or "read the relevant files." Claude dutifully reads a dozen files, most of which are not needed for the actual task.

A better approach is to follow a strict protocol. Before asking Claude to read files, use `grep` and `glob` to identify exactly which files are relevant. Then ask Claude to read only those specific files.

```
> Read src/auth/middleware.rs and fix the token expiration check 
```

Not this.

```
> Look through the auth module and find and fix the token bug 
```

The first prompt reads one file. The second prompt might read five or ten files before finding the right one. The token difference is significant.

For large files, consider whether Claude needs the entire file or just a portion. If you know the bug is on line 45, tell Claude to focus on that area. Less context means fewer tokens and often better results, because Claude is not distracted by irrelevant code.

### Batch Operations

Grouping related changes into a single prompt is more efficient than making them one at a time. Each separate prompt carries the full context overhead. Five separate prompts about five related changes cost roughly five times more than a single prompt that addresses all five.

Here is an example. Instead of five separate prompts asking Claude to add error handling to five different functions, write one prompt.

```
Add error handling to the following functions in src/api/handlers.rs: 1. create_user - handle duplicate email errors 2. update_user - handle not found errors 3. delete_user - handle foreign key constraint errors 4. list_users - handle pagination out of range 5. get_user - handle not found errors Use the AppError type from src/errors.rs for all error returns. 
```

Claude handles all five in a single turn, with a single context load. The savings scale with the number of related changes.

Planning work in batches pays off. Before starting a Claude Code session, list the changes needed.

If several changes are in the same area of the codebase, group them into a single prompt. This takes a minute of planning and can save thousands of tokens.

### Subagents for Research

Claude Code's subagent tool delegates tasks to a separate context window. This is powerful for cost management because the subagent's context is independent of your main conversation.

When you need Claude to research something, the subagent reads files, searches the codebase, and returns a summary to your main context. Your main context only receives the summary, not all the files the subagent read.

Consider the difference. If you ask Claude to "find all places where we handle authentication errors and summarise the patterns," Claude might read 15 files in your main context, adding 150,000 tokens.

With a subagent, those 15 files are read in a separate context. Your main context receives a 500-token summary.

Use subagents for codebase exploration, pattern analysis, dependency tracking, and any research task where you need a summary rather than the raw data.

**A warning on subagent model selection.** You might be tempted to set `CLAUDE_CODE_SUBAGENT_MODEL` to Haiku for maximum savings. This is risky. That environment variable also controls the planning agent, and a weak planner causes compounding mistakes downstream. Sonnet is the safer subagent default: roughly 40% cheaper than Opus with minimal quality loss on research and exploration tasks.

### Parallel Agents with Isolated Context

A related technique is spawning separate agents per task, each with a fresh context window. Instead of one long conversation that accumulates tokens across multiple tasks, you run parallel agents that work independently. Each agent starts clean, processes its task, and returns results.

This saves tokens because no agent carries context from unrelated tasks. It also speeds up work because agents run concurrently. If you have three independent changes to make, three parallel agents finish faster than one sequential conversation and use fewer total tokens because none inherits the accumulated context of the others.

### Enterprise Cost Controls

For teams and enterprises, to manage costs effectively you need controls beyond individual practices. The [enterprise managed settings](/guides/enterprise-claude-code-managed-settings) system provides organisational controls that prevent runaway costs.

**Spending limits** can be set per user, per team, or per project. When a limit is reached, usage is throttled or paused until the next billing cycle. This prevents any single developer or project from consuming a disproportionate share of the budget. CI pipelines deserve their own budget allocation; if you run [Claude Code in GitHub Actions](/guides/claude-code-github-actions), use concurrency controls and path filters to avoid redundant runs that waste tokens.

**Usage dashboards** provide visibility into who is spending what and on which projects. Review these weekly with your team leads.

Identify developers whose usage is unusually high or low. High usage might indicate inefficient habits that coaching can fix. Low usage might indicate that developers are not getting enough value from the tool.

**Model restrictions** can limit which models are available for different contexts. You might allow Opus only for senior developers or specific project types, while defaulting everyone else to Sonnet. This ensures that the most expensive model is used only when its capabilities are genuinely needed.

**Approved plugins and MCP servers** affect costs indirectly. Some tools are chatty, making many API calls or returning large responses. Claude Code now uses deferred tool search, which reduces the context window impact of registered MCP servers compared to earlier versions. Tool definitions are loaded on demand rather than all at once, so the effective overhead of having many MCP servers configured is smaller than it used to be. That said, controlling which tools are available still helps manage the token overhead from tool outputs. For a breakdown of which plugins deliver the best value, see our guide on the [best Claude Code plugins in 2026](/guides/best-claude-code-plugins-2026). For teams deploying custom MCP servers, our guides on [MCP authentication and security](/guides/mcp-server-authentication-security) and [production MCP deployment](/guides/mcp-servers-production-deployment) cover the operational patterns that keep costs predictable.

The most effective enterprise cost strategy is not restriction but education. Teams that understand how token costs work and have visibility into their usage naturally optimise. Teams that are simply given limits without context tend to either ignore the tool or resent the constraints.

### Community-Tested Techniques

After publishing the original version of this guide, 74 developers contributed corrections and additional techniques through LinkedIn discussion. Several of these additions address blind spots in the original guide. The following techniques have been validated by the community and are presented with credit to those who contributed them.

**Cap thinking tokens (the single biggest lever).** Set `MAX_THINKING_TOKENS` to 10,000. Claude's extended thinking can consume tens of thousands of tokens per response, and in most routine development tasks, the additional reasoning depth beyond 10,000 tokens provides diminishing returns. This was confirmed by multiple community members as the highest-impact single change for reducing spend.

**Strip tool output noise before it enters context.** Every `ls`, `find`, `git diff`, and similar command feeds raw output into the context window, and those tokens get re-read on every subsequent turn. A token-reduction proxy or a PreToolUse hook can trim this noise automatically — filter long listings, collapse repeated lines, drop colour codes and whitespace runs — before Claude sees the output. The effect compounds across a session.

**Keep context indexed, not loaded.** Session data, large files, and reference material belong in a sandbox that Claude queries on demand, not pasted into the prompt. The principle is the same as CLAUDE.md-as-index: load context when needed, not by default.

These techniques stack. Thinking token caps reduce output costs. Tool-output trimming reduces input costs from the command shell. Context indexing reduces input costs from session data. CLAUDE.md as an index reduces input costs from project instructions. Applied together, they compound into significant savings.

### Real Cost Examples

To make the abstract concrete, here are typical costs for different task types. These assume API pricing with Claude Sonnet unless noted.

**Quick question (e.g. "what does this error mean"):** 2,000-5,000 input tokens, 500-1,000 output tokens. Cost with Sonnet is roughly $0.02. With Haiku, it would be roughly $0.006.

**Single file edit (e.g. "add error handling to this function"):** 10,000-20,000 input tokens (including file contents), 2,000-5,000 output tokens. Cost with Sonnet is roughly $0.10.

**Multi-file refactoring (e.g. "rename this API and update all callers"):** 50,000-100,000 input tokens, 10,000-20,000 output tokens. Cost with Sonnet is roughly $0.45. This is where Opus might be worth the premium if the refactoring is complex.

**Full feature implementation (e.g. "add user preferences with database, API, and UI"):** 100,000-200,000 input tokens, 30,000-50,000 output tokens. Cost with Sonnet is roughly $1.05. With Opus, roughly $5.25. Over a long session with multiple turns, these can double or triple.

**Codebase exploration (e.g. "understand the authentication system"):** 150,000-300,000 input tokens, 5,000-10,000 output tokens. Cost with Sonnet is roughly $0.79. This is where subagents provide the most value, as they keep the large context out of your main session.

A productive developer using Claude Code full-time with good habits typically uses $5-15 per day on API pricing. Without good habits, the same work might cost $20-40 per day. The optimisation strategies in this guide close that gap.

### Building a Cost-Conscious Workflow

Pulling everything together, here is a recommended daily workflow.

**Morning.** Start a fresh session. Review the tasks for the day. Plan which tasks can be batched together. Set the model to Sonnet.

**Per task.** Clear the context with `/clear` before each new task. Use specific, detailed prompts. Name the files involved. Switch to Opus only for genuinely complex tasks, then switch back to Sonnet when done.

**Mid-session.** Run `/compact` if the context is growing large. Check `/cost` periodically to stay aware of usage. Use subagents for research and exploration.

**End of day.** Review the session cost. Note any tasks that were unusually expensive and think about why. Adjust CLAUDE.md if you notice patterns that could be addressed with better instructions.

This is not a rigid process. It is a set of habits that, once internalised, run on autopilot. The savings compound over time, and the discipline of thinking about context management actually makes you more productive.

## Cost Optimization Checklist

If you want a single page you can paste into a team wiki, here is the checklist. These are the habits that keep costs predictable without turning cost control into a second job.

**Daily habits**

1. Start the day on Sonnet, not Opus. Switch up only when a task truly needs it.
2. Run `/cost` at the start and end of every session so you have a baseline.
3. Use `/clear` between unrelated tasks. The rule is one conversation per intent.
4. Write specific prompts that name files and state the desired outcome in a single sentence.
5. Set `MAX_THINKING_TOKENS=10000` in your environment once and forge

[Content truncated]
