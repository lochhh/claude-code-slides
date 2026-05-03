# Claude Code Token Optimization: Full System Guide (2026)

**Type:** article
**URL:** https://buildtolaunch.substack.com/p/claude-code-token-optimization
**Topic:** Cost & Token Management
**Published:** unknown

## Content

# [Build to Launch](/)

# Claude Code Token Optimization: Stop the $1,600 Bill (2026 Guide)

### The setup changes, session habits, and Desktop tips that keep costs from compounding

[Jenny Ouyang](https://substack.com/@jennyouyang)

Apr 14, 2026

The [Claude Code](https://buildtolaunch.substack.com/p/claude-code-beginners-guide?utm_source=publication-search) billing complaints have been hard to miss lately: in communities, on Reddit, in my DMs. The numbers people are sharing are not edge cases. I wrote a separate guide on [cost-effective AI building](https://buildtolaunch.substack.com/p/cost-effective-ai-building-guide) if you want the broader picture, but this article is specifically about the token mechanics inside [Claude Code](https://buildtolaunch.substack.com/p/claude-code-hub?utm_source=publication-search) and [Desktop](https://buildtolaunch.substack.com/p/claude-onboarding-setup-guide?utm_source=publication-search).

Two months ago, mine hit $1,600.

I had dramatically ramped up my Claude Code usage in the weeks before that (building, writing, experimenting). I thought I was being cautious. But when that invoice arrived, I was genuinely shocked. On a second thought, it made sense.

Sure, I was starting each session clean. But every file I asked Claude to read added its entire contents to the context window permanently, for that session. Every MCP tool response got the full JSON, not a summary. Every log Claude scanned. All of it stacking, invisibly.

And because Claude re-reads the full context on every single message, the 40th message in a session was paying for everything that came before it.

I wasn’t burning tokens on bad prompts. I was burning them on invisible architecture.

The fix wasn’t a list of tips. It was understanding the mechanism first, then building a system around it.

## **What’s inside:**

* **[Why Claude Code Gets Expensive: The 3 Token Drains Nobody Warns You About](https://buildtolaunch.substack.com/i/193860342/why-claude-code-gets-expensive-the-3-token-drains-nobody-warns-you-about)** — the mechanism behind invisible token spend and why my $1,600 bill made sense once I understood it
* **[One-Time Claude Code Setup to Reduce Your Token Baseline](https://buildtolaunch.substack.com/i/193860342/one-time-claude-code-setup-to-reduce-your-token-baseline)** — .claudeignore, context-mode, and CLAUDE.md changes you do once and benefit from every session
* **[Claude Code Session Habits That Cut Token Usage](https://buildtolaunch.substack.com/i/193860342/claude-code-session-habits-that-cut-token-usage)** — /compact, model-switching, subagents, and 6 more habits for every session
* **[Reducing Token Costs on Claude.ai and the $20 Plan](https://buildtolaunch.substack.com/i/193860342/reducing-token-costs-on-claudeai-and-the-20-plan)** — Cowork, artifacts, and session notes on the subscription tier
* **[How to Track and Measure Claude Code Token Savings](https://buildtolaunch.substack.com/i/193860342/how-to-track-and-measure-claude-code-token-savings)** — baseline method, red flags, and what healthy usage actually looks like
* **[Claude Code Token Costs: Frequently Asked Questions](https://buildtolaunch.substack.com/i/193860342/claude-code-token-costs-frequently-asked-questions)** — savings ranges, /compact reliability, context-mode safety, API vs subscription billing, and more

*Hi, I’m Jenny 👋  
I build AI systems and tools, then share how I did it. I run the [Practical AI Builder program](https://buildtolaunch.substack.com/p/practical-ai-builder-program) for people who already use AI and want to build real things with it. Check it out if that sounds like you.*

*If you’re new to Build to Launch, welcome! Here’s what you might enjoy:*

* *[15 Claude Code Project Ideas (with prompts to get you started)](https://buildtolaunch.substack.com/p/claude-code-project-ideas)*
* *[Best Claude Code Prompts](https://buildtolaunch.substack.com/p/best-claude-code-prompts)*
* *[Claude Master Hub](https://buildtolaunch.substack.com/p/claude-code-hub)*

## **Why Claude Code Gets Expensive: The 3 Token Drains Nobody Warns You About**

Not your prompts. Prompts are usually fine.

#### How Tool Call Outputs Silently Drain Your Claude Code Budget

Every time Claude reads a file, runs a shell command, or calls an MCP server, the full output gets appended to context. Not a summary. The whole thing.

A 10,000-line log file stays in context for every subsequent message in that session. A large JSON response from an MCP server lands the same way. Tool output volume is almost always larger than the conversational messages themselves — and it compounds the same way. This is the biggest silent drain.

Tool call outputs from Claude Code (top) & Claude Desktop (bottom)

> *The single biggest Claude Code cost driver is not your messages. It is the full, unfiltered output of every tool call accumulating in context for the rest of the session.*

#### Why Long Sessions Cost More: How Context Accumulation Works

Claude re-reads the entire conversation from the top on every message. Message 50 costs more than message 5 not because you asked something harder, but because Claude is re-reading 49 prior messages first. Long sessions become token furnaces.

> *Long sessions don’t just cost more. They also make Claude worse. Quality degrades as older context loses weight and earlier instructions get deprioritized. That’s context rot — a separate problem, but the fixes overlap.*

#### How Your CLAUDE.md File Costs Tokens Before Every Single Message

Your CLAUDE.md loads before Claude reads your code, before it reads your task, before anything. A 5,000-token CLAUDE.md costs 5,000 tokens before you’ve typed a word. Every turn. Every session. A constant baseline you carry at all times.

Extended thinking is real too — it burns output tokens and the default budget can run into the tens of thousands per request. But it’s number four. Fix the three above first.

> *The March 2026 caching incident is worth knowing about: two bugs in Anthropic’s prompt caching caused 10–20x token inflation with no warning. Users had to reverse-engineer the Claude Code binary to find them ([GitHub issue #40524](https://github.com/anthropics/claude-code/issues/40524)). The billing layer is more opaque than most builders assume.*

What works against all three: a layered approach. Control what goes in. Control how sessions accumulate. Control what tools dump into context. Each layer is independent. Each one compounds with the others.

## **One-Time Claude Code Setup to Reduce Your Token Baseline**

These are one-time changes. Do them once, benefit every session after.

#### Set Up .claudeignore to Block Expensive Files From Claude’s View

Claude Code respects a `.claudeignore` file that works exactly like `.gitignore`. If something is in the ignore list, Claude can’t read it or accidentally load it during tool searches.

Starting template:

```
node_modules/ .next/ dist/ build/ *.log *.lock coverage/ .env* __pycache__/ *.pyc 
```

Adjust for your stack. The principle is the same: anything Claude doesn’t need to see in order to do its job should not be visible to it.

What NOT to ignore: the files Claude actually needs. Over-pruning causes Claude to miss relevant context and make worse calls. The goal is surgical, not scorched earth.

#### Disconnect Unused MCP Servers to Eliminate Per-Request Overhead

I’ll be honest: I’m [obsessed with MCPs](https://buildtolaunch.substack.com/p/best-mcp-servers-claude-code?utm_source=publication-search) and have accumulated [a collection of all sorts](https://buildtolaunch.substack.com/p/best-mcp-servers-claude-code?utm_source=publication-search). That’s part of why this one bit me. (If you’re still setting up [MCP servers for Claude Code](https://buildtolaunch.substack.com/p/mcp-server-types-installation-guide-claude-cursor), that guide covers types and installation.)

Every connected MCP server adds to what Claude has to reason about at session start, even if you never call it during that session. There’s a small but real overhead per connected server on every request.

Go through your MCP list. If you haven’t used a server in a week, disconnect it. Reconnect when you need it. This is a 10-second operation with compounding savings.

> *Also applies to Claude Desktop: remove unused servers from* `claude_desktop_config.json`*. Same overhead, same fix.*

*If you're setting up MCP from scratch across clients — [MCP Servers in Every AI Client](https://buildtolaunch.substack.com/p/mcp-setup-claude-chatgpt-vscode-cursor) covers which servers to connect, which to skip, and how to configure them across Claude, Cursor, and VS Code.*

#### Disable Unused Claude Code Plugins to Reduce Baseline Token Load

Same story with plugins. I had more running than I actually needed. Active plugins in Claude Code add overhead whether you invoke them or not. Keep only what you’re using for the current project or workflow.

> *Also applies to Claude Desktop: you can disable integrations in Settings. Same principle — if you’re not using it for the current workflow, turn it off.*

*I ran 11 Claude Code plugins through real work to see what they actually cost versus deliver — [Best Claude Code Plugins: 11 Tested, 4 Worth Keeping](https://buildtolaunch.substack.com/p/best-claude-code-plugins-tested-review) has the full breakdown with keep/skip verdicts.*

#### Install context-mode to Cut MCP Token Output 50–90%

Context-mode is an [open source MCP plugin](https://github.com/mksglu/context-mode) that routes tool outputs into a sandbox knowledge base instead of dumping them into your conversation. (It’s one of the [Claude Code plugins I actually use](https://buildtolaunch.substack.com/p/best-claude-code-plugins-tested-review) daily.)

When an MCP server returns 10,000 tokens of raw JSON, context-mode indexes it. Claude gets a summary and can search the indexed content when it needs specifics. Your main context stays clean.

I run this daily. It cuts MCP-related token usage 50 to 90% in sessions where tools are active. If you use multiple MCP servers regularly, this is the highest-leverage single change in this entire guide.

*For which MCP servers worth installing— [Best MCP Servers for Claude Code](https://buildtolaunch.substack.com/p/best-mcp-servers-claude-code) covers the 16 I've tested on real projects with notes on output volume.*

#### Keep CLAUDE.md Under 500 Tokens to Lower Your Constant Baseline

CLAUDE.md should give Claude the *shape* of your project, not the full documentation.

Five rules and three file pointers is the right size. Put project-specific workflows and reference material in separate files, referenced by path. Claude reads those files when it’s working on something relevant. Not every single turn.

Target: under 500 tokens.

```
# CLAUDE.md ## Rules - Use TypeScript strict mode - Write tests for every new function - Follow existing patterns in the codebase ## Key Files - API routes: see src/api/README.md - Database schema: see docs/schema.md - Style guide: see docs/style-guide.md 
```

Three rules. Three pointers. Under 200 tokens. Claude reads the linked files only when working on something relevant to them.

## **Claude Code Session Habits That Cut Token Usage**

These are habits: things you do (or stop doing) every time you open Claude Code. The setup layer cut the baseline. This layer controls how context accumulates from there.

#### Use One Topic Per Chat to Avoid Invisible Context Waste

Carrying context from a previous topic into a new one is invisible waste. If you were debugging a database issue and now you want to work on the UI, start a new conversation. The old context does nothing for the new task. It just adds cost to every message.

New topic = new chat. No exceptions.

> *Applies to all Claude interfaces — Claude Desktop, Claude.ai, Claude Code all accumulate context the same way.*

#### When to Use /clear vs. /compact in Claude Code

Two different tools. Know which does what.

`/clear` wipes the entire conversation. Clean slate, zero context. Use it when switching tasks completely. You don’t need any of what came before.

`/compact` summarizes the conversation and restarts from the summary. Use it when context is getting long but you still need the thread of what happened. It compresses; it doesn’t erase.

Using `/clear` when you wanted `/compact` means re-explaining context that was already there. Using `/compact` when you wanted `/clear` means carrying old context that actively bloats the new task.

> *On Claude Desktop and Claude.ai:* `/clear` *= start a new chat. There’s no* `/compact` *equivalent — your only option is the fresh start.*

#### Point Claude at Specific Files Instead of the Full Repository

If you’ve used Claude Code for any length of time, you’ve probably said something like “read the codebase” or “look through the project.” That’s expensive. Claude loads and processes every file it can see.

Be specific. Tell Claude exactly which files are relevant to the task. Most tasks touch two or three files. Point directly to those.

This is also where a well-organized project structure pays off: when the directory makes sense, you always know where to point Claude without guessing. The [Claude Code Hub](https://buildtolaunch.substack.com/p/claude-code-hub) covers the full setup if you’re starting from scratch.

#### Use Scripts for Data You’ll Read Yourself, Not Claude

If the goal is to fetch something and read it with your own eyes, write a script. Don’t ask Claude to load it.

Every `read_file` tool call appends the full file contents to context permanently for that session. If you’re going to read a log file, pull an API response, or look at a data file yourself, use a shell script instead. Claude doesn’t need to be in the loop.

I do this regularly. Fetch locally, read myself. The context stays clean.

> *Universal habit: applies whether you’re in Claude Code, Claude Desktop, or Claude.ai.*

#### Use CLI Tools Instead of MCP for Targeted, Low-Token Reads

When a CLI equivalent exists for what an MCP server does, use it. CLI tools return targeted, scoped output. MCP tools dump full responses into your context whether you needed all of it or not.

A shell command that returns 10 lines costs 10 tokens of context. The same request through an MCP server might return a structured JSON blob that’s 100x that. Over a session, the difference compounds.

Before defaulting to MCP: does a CLI tool already do this? If yes, use the CLI.

#### Switching Between Haiku, Sonnet, and Opus to Control Costs

Claude Code’s three main models serve different jobs.

**Opus** for architecture decisions, complex reasoning, multi-file refactoring, hard debugging problems.  
**Sonnet** for implementation, writing tests, explaining code, most daily work.  
**Haiku** for mechanical tasks: renaming, formatting, quick lookups, repetitive edits.

The cost difference is significant. Haiku is around 5x cheaper per input token than Opus at [current pricing](https://www.anthropic.com/pricing). If a task takes Claude under 30 seconds to answer, it probably doesn’t need Opus. Switch with `/model` before starting.

Where Haiku fails: tasks that look simple but require reading code and making judgment calls. It will get the wrong answer faster and cheaper than Opus, which then costs you a correction cycle. When in doubt, Sonnet is the reliable middle ground.

> *Also applies to Claude Desktop: model selection is available in the same session. Switch before the heavy task, not after.*

*For the full Claude Code setup including model tiers, MCP configuration, and how to go from installation to a real working project — [Claude Code Hub](https://buildtolaunch.substack.com/p/claude-code-hub) is the complete reference.*

#### Limit Extended Thinking Token Budget with `/effort` and `MAX_THINKING_TOKENS`

Extended thinking is billed as output tokens, and the default budget can run into the tens of thousands of tokens per request without notice.

For tasks that don’t need deep reasoning:

```
/effort low
```

Or set a hard environment cap:

```
MAX_THINKING_TOKENS=8000
```

That still allows meaningful reasoning while preventing runaway costs on tasks that would have worked fine without it.

When NOT to optimize: complex planning, architecture decisions, multi-step problem decomposition. The Opus + extended thinking cost is worth it when the quality difference is real. Don’t under-invest on decisions that matter.

#### Load Claude Code Skills On Demand, Not at Session Start

In Claude Code, skills only load their actual content when explicitly invoked. They don’t auto-load just because they’re installed.

The skill list loads automatically at session start. That’s the Claude Code harness, and there’s no built-in toggle to exclude it. But the content of a skill (which can be hundreds of lines) stays dormant until you call it with `/skill-name`.

The implication: don’t invoke skills you don’t need for the current task. Don’t call them at session start out of reflex. Load what you need, when you need it.

#### Use Subagents to Isolate Heavy Context

When a task requires reading a lot of files, running a long analysis, or generating substantial tool output, delegate it to a subagent.

Subagents run in separate sessions. Their context accumulates separately from your main conversation. When they finish, you get the result without their session weight appearing in your costs going forward.

Anything that would require Claude to read more than three or four large files is a solid subagent candidate. The context stays clean in your main session, and the subagent can go as deep as it needs to.

*The mechanics of how subagents work under the hood — [What Are Claude Code Subagents?](https://buildtolaunch.substack.com/p/claude-code-subagents-explained) covers why they're useful for context isolation and how to structure tasks so you get the result without the accumulated session weight.*

## **Reducing Token Costs on Claude.ai and the $20 Plan**

This section is for claude.ai users (Cowork, Chat, the web interface). Different tool, same core problem.

#### Avoid Claude.ai Cowork on the $20 Plan for Exploratory Work

Cowork is powerful. It’s also expensive. Every session reads your project folder before starting any task. Tokens burned before you’ve asked anything.

On the $20 plan, use Chat for most work. Think through the structure in Chat, nail the details, get the plan right. Then move to Cowork only when you know exactly what you want built. Do the thinking in the cheaper product and the building in the expensive one, only when it’s worth it.

#### Load Only the Files Relevant to the Current Task

Don’t dump your entire folder into a Cowork session. Select only files relevant to the specific task. Zero folders selected means zero local file context, which is exactly right for tasks that don’t need your files at all.

#### Keep Your Own Session Notes Instead of Relying on AI Memory

Letting Claude remember everything is a token tax on every session.

Keep your own notes. Use a `session-notes.md` pattern: at the end of a session, ask Claude to summarize key decisions and next steps. Start the next session by loading that file. You carry forward exactly what matters. Nothing else.

> *Works in Claude Code, Claude Desktop, and Claude.ai. The interface doesn’t matter, the habit does.*

#### Plan in Chat Before Generating Artifacts to Avoid Wasted Token Spend

Artifacts (spreadsheets, documents, slides) cost more than chat messages. Plan the structure in Chat. Then build the artifact once you know exactly what you want.

Exploring ideas in an artifact is expensive; exploring ideas in Chat is cheap.

Same logic applies to images. Generating one is useful. But ask: is this actually useful for what you’re doing right now? If yes, generate it. If you’re experimenting, skip it.

> *Same principle in Claude Code: plan in Chat before spinning up agents or artifacts. The cheaper thinking pass saves the expensive execution pass.*

#### Re-Use Existing Skills and Workflows Instead of Re-Prompting From Scratch

If you’ve built a workflow, use it. If a skill exists for the task, invoke it instead of re-prompting from scratch.

The same workflow run twice from scratch burns twice the tokens for the same result. Build once, reuse it. The [Build to Launch MCP](https://buildtolaunch.substack.com/p/custom-mcps-claude-code-cursor) has research and content skills built in. Invoke them instead of reconstructing the workflow every session.

If you want to build your own, [how to build custom MCPs](https://buildtolaunch.substack.com/p/how-to-build-mcp-server-complete-guide?utm_source=publication-search) covers that end to end.

## **How to Track and Measure Claude Code Token Savings**

The easiest thing to skip with token optimization: setting a baseline before you start. Without one, you have no way to know if anything actually improved.

#### Set a Claude Code Token Baseline Before Optimizing

First, know your tool. On API billing, use `/cost` at the end of a session. It shows token count and estimated spend.

For cross-session history, check `console.anthropic.com → Usage`. On a subscription (Pro, Max), `/cost` just confirms your plan and nothing else. Go to `claude.ai → Settings → Usage` instead, which shows remaining quota and when your window resets.

Either way: pick a representative task, note your number, apply the changes from this article, run the same task, check again. That comparison is your signal. Without it, you’re guessing.

Settings —> Usage on Claude app

#### Red Flag: Same Work Costs Significantly More Than Yesterday

API users see it as a cost spike: same task, 10x the bill from yesterday. Subscription users see it as quota drain: the same workload burning through the window hours faster than usual. Both point to the same cause: a caching issue.

Check: did you change models mid-session? Long gap between messages? Conversation restructured in a way that broke cache continuity? If nothing explains it and the pattern persists, check whether you’ve hit a caching bug similar to the March 2026 incident before assuming it’s permanent.

#### Red Flag: Context Overload Shows Up as ECONNRESET and 500 Errors

Context overload doesn’t always show up as a bill. Sometimes it shows up as errors, and the error type tells you roughly where you are:

* `Internal server error (500)`: the server struggled to process your request. Often context-related when it happens consistently, not randomly.
* `ECONNRESET` **/** `EPIPE`: the server dropped the connection mid-request. Usually means processing took too long because the context was large. Looks like a network problem. Usually isn’t.
* **“Chat has reached its limit”**: hard context window hit. Happens fast when you spin up multiple subagents and their outputs all return into the same main session at once.

These three are a progression. If you’re seeing any of them regularly, the fix isn’t your network or a retry. Use `/compact` or start a fresh session. I hit all three while working on large projects.

#### What Low-Cost Claude Code Sessions Actually Look Like

Sessions that stay focused and scoped use dramatically less (in cost or quota) than sessions that sprawl. A full day of focused work should feel well within your limits. The difference is measurable. Not theoretical.

## **Claude Code Token Optimization: Full System Summary**

The question worth shifting: not just how do I use Claude Code better, but how do I architect my sessions so the mechanism works for me instead of against me?

The answer is this system:

This system is available as a live guide inside the [Build to Launch MCP](https://buildtolaunch.substack.com/p/custom-mcps-claude-code-cursor). Once the MCP is connected, ask Claude to load `guide-claude-token-optimizer`. It runs directly in Claude Code or Claude Desktop and walks you through each change — what to do, what to watch for, and what to skip.

#### Beginner: start with the setup layer

Install context-mode, add a `.claudeignore`, and trim your CLAUDE.md under 500 tokens. These are one-time changes that improve every session without requiring any new habits.

#### Intermediate: add session discipline

Run one task per chat. Use `/compact` instead of letting sessions run long. Start pointing Claude at specific files instead of “the whole project.” Track a few sessions with `/cost` to see what changes.

#### Advanced: redesign around subagents

For any workflow that requires reading large amounts of context or running multi-step analyses, move it to a subagent pattern. Keep your main session for direction and review. Let the subagent accumulate the heavy context where it doesn’t affect your ongoing work.

If any of this is useful, share it with one person who’d find it valuable.

[Upgrade](https://buildtolaunch.ai/subscribe)

## **Claude Code Token Costs: Frequently Asked Questions**

**How much can I actually save with these techniques?**  
Reported savings vary: 40% to 70% on focused tasks, with higher reductions when context-mode handles heavy MCP use. The more tools you’re running, the larger the impact. Set a baseline first and measure your own workflow. Generic percentages won’t tell you what your actual situation looks like.

**Does** `/compact` **actually work well, or does it lose important context?**  
It works well for most use cases. The summary captures key decisions and progress. What it loses is fine-grained detail from early in the session: exact error messages, precise outputs. If you need to reference those later, note them before running `/compact`.

**Is context-mode safe to install?**  
The code is open source at github.com/mksglu/context-mode, readable and auditable. It runs locally and indexes tool outputs to a local sandbox. It doesn’t send data anywhere external. Review the source before installing if you want to verify.

**Will this get outdated as Anthropic updates Claude Code?**  
Some of it will. The mechanism (context compounds on every message) is fundamental and won’t change. Specific commands like `/effort` and `MAX_THINKING_TOKENS` may evolve. The setup layer and session habits stay relevant regardless of product updates.

**Should I always use Haiku for simple tasks?**  
For genuinely mechanical work (renaming, formatting, quick lookups), yes. Where Haiku breaks down is tasks that look simple but require reading code and making judgment calls. It gives wrong answers faster, which costs you a correction cycle. When in doubt, Sonnet is the reliable middle ground.

**How does Claude Code billing work on API vs subscription?**  
On API, you pay per token, with input and output billed separately. Haiku, Sonnet, and Opus have different per-token rates, with Opus roughly 5x more expensive per input token than Haiku at current pricing. On subscription (Pro, Max), you pay a flat monthly rate and hit a quota limit rather than a dollar bill. The optimization strategies in this article apply to both, but the measurement method differs: API users track `/cost`; subscription users track quota in `claude.ai → Settings → Usage`.

**What are Claude Code’s daily usage limits?**  
On subscription plans, Anthropic doesn’t publish hard daily token caps. The quota varies based on plan and current load. In practice, focused sessions applying the habits in this article rarely hit limits on Pro or Max. Heavy, sprawling sessions without scoping or /compact regularly do. If you’re consistently hitting limits on Pro, the Max plans (5x and 20x) are designed for high-volume builders.

**How do I estimate my Claude Code costs before starting a project?**  
For API users: run one representative task, check `/cost`, and multiply by your expected session count. Typical Claude Code sessions run 10,000 to 50,000 input tokens depending on tool usage. For subscription users: scope tasks tightly and use /compact to control session length. If you’re evaluating whether Max versus API makes sense, heavy daily builders often find Max cheaper than API at scale once token volume crosses a threshold.

*I run the [Practical AI Builder program](https://buildtolaunch.substack.com/p/practical-ai-builder-program) for people who already use AI and want to go from chatting with it to building real systems. If that sounds like where you’re stuck, take a look.*

**What’s the one thing from this article you’re trying this week?**

— Jenny

**[Why Upgrade](https://buildtolaunch.substack.com/p/why-subscribe) · [Practical AI Builder Program](https://buildtolaunch.substack.com/p/practical-ai-builder-program) · [Templates](https://buildtolaunch.substack.com/p/complete-ai-builder-resources) · [Builder Showcase](https://vibecodingbuilders.com/)**

#### Discussion about this post

[Dana Forfa](https://substack.com/profile/113167242-dana-forfa?utm_source=substack-feed-item)

[Apr 15](https://buildtolaunch.substack.com/p/claude-code-token-optimization/comment/244082184 "Apr 15, 2026, 10:33 PM")

I wrote about this same topic today!

Share

[1 reply by Jenny Ouyang](https://buildtolaunch.substack.com/p/claude-code-token-optimization/comment/244082184)

[Alejandro Aboy](https://substack.com/profile/22949723-alejandro-aboy?utm_source=substack-feed-item)

[Apr 15](https://buildtolaunch.substack.com/p/claude-code-token-optimization/comment/243956441 "Apr 15, 2026, 6:06 PM")

Amazing Jenny! Some extras you could find interesting: RTK for token compression, claude-hud plugin to track usage and other artifacts in the terminal. They are really cool tools!

ReplyShare

[1 reply by Jenny Ouyang](https://buildtolaunch.substack.com/p/claude-code-token-optimization/comment/243956441)

[24 more comments...](https://buildtolaunch.substack.com/p/claude-code-token-optimization/comments)

No posts

### Ready for more?

© 2026 Jenny Ouyang · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great culture

 
