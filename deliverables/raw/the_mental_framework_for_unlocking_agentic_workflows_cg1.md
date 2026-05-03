# The Mental Framework for Unlocking Agentic Workflows - DEV Community

**Type:** article
**URL:** https://dev.to/somedood/the-mental-framework-for-unlocking-agentic-workflows-cg1
**Topic:** Plan Mode & Agentic Workflows
**Published:** unknown

## Content

![DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png)

## DEV Community

![](https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg)
![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)
![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
![Cover image for The Mental Framework for Unlocking Agentic Workflows](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0bagnza4cotjrrlfvho9.png)
![Basti Ortiz](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F108756%2F1bb8b570-520b-4ad9-8a25-ee28c4d04a8d.jpeg)

Posted on Apr 19

![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)
![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)

# The Mental Framework for Unlocking Agentic Workflows

Focuses on the Principle of Least Context

📌 This article was originally presented as a talk at the inaugural **Claude Code Manila** meetup (March 5, 2026). After several requests from the attendees to share the slides, I've decided to instead publish them as a full article here. I figured that this was a more effective medium to share my insights on reliable long-running agentic workflows.

## The Beginner's Mark

One of the most common mistakes that I see people make when they've just started out chatting with AI is dump everything into the same conversation.

Why? Because "it remembers better" apparently.

And true enough, Claude *will* remember what you put in the current session. Long-running conversations can go on *seemingly* forever… until the "compacting conversation" alert comes up, and suddenly Claude gets a bit dumber.

The reason for this, of course, is that Claude (like all current-gen LLMs) have a limited context window. I'll spare you the details because you're likely already aware of how this context window works; otherwise you wouldn't have attended a Claude Code meetup, right?

Anyway, what's important to point out here is that anecdotally, LLMs like Claude have a so-called "dumb zone". Beyond 40% of the context window, "context rot" kicks in and the model's ability to reason, recall, and perform significantly degrades. That's why Claude Code automatically compacts a conversation at 85% capacity.

[![visualization of 0-40% being the ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F716i2j4vzuveupykhbqy.PNG)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F716i2j4vzuveupykhbqy.PNG)

![visualization of 0-40% being the ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F716i2j4vzuveupykhbqy.PNG)

But what this means is that whatever you were doing or talking about prior to compaction suddenly gets compressed into a lossy summary that gets prefixed at the start of the next session. What looks like a long conversation is actually just compacted summaries stitched together.

[![visualization of a full conversation context window with a system prompt and its tool calls](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2v0dzrk5d1yjff0t1ia3.PNG)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2v0dzrk5d1yjff0t1ia3.PNG)

![visualization of a full conversation context window with a system prompt and its tool calls](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2v0dzrk5d1yjff0t1ia3.PNG)

[![visualization of a compacted conversation context window with a system prompt and its tool calls](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fumdbyqrdcc9zisrdp9f6.PNG)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fumdbyqrdcc9zisrdp9f6.PNG)

![visualization of a compacted conversation context window with a system prompt and its tool calls](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fumdbyqrdcc9zisrdp9f6.PNG)

## A World without Proper Context Management

Now this is typically not a big problem in Claude Chat, where most conversations are short and follow the question-and-answer format.

But where you do hit the limits is when you start to use Claude for agentic workflows. Namely:

Just to give you a picture of how bad **context rot** can get if we're not careful, imagine if we used Claude Code like how we would use Claude Chat: a single long conversation for everything.

`CLAUDE.md`
`Glob`
`WebSearch`
`Read`
`Bash`
`Bash`
`Write`

[![visualization of an overloaded conversation context window with a system prompt and its tool calls](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2ytth18luz8vsm4lm2bw.PNG)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2ytth18luz8vsm4lm2bw.PNG)

![visualization of an overloaded conversation context window with a system prompt and its tool calls](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2ytth18luz8vsm4lm2bw.PNG)

You'll probably get away with one or two features. But in the limit, compaction will be inevitable. And soon, your compaction will get compacted. And your compacted compaction accumulates in the conversation preamble until the summary itself takes up more than 40% of the context window!

(That's happened to me before.)

Without proper context management, these workflows are outright impossible. A single parallelized `Explore` agent can take up as much as 60k tokens. If those 60k tokens weren't self-contained by the sub-agent's context window, that would've been dumped onto your main session!

`Explore`

Imagine what that looks like in a typical Plan Mode. A medium-sized feature in a fairly large codebase typically spawns 3 parallel `Explore` sub-agents, each of which finish with ~60k tokens by the end. So if that were done sequentially in the main context window, that's already ~180k tokens out of the 200k budget!

`Explore`

We haven't even gotten to the main planning work, much less the actual task!

[![three explorer agents taking up around ~60k tokens each](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjtufhn9j4otxc5p287sc.PNG)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjtufhn9j4otxc5p287sc.PNG)

![three explorer agents taking up around ~60k tokens each](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjtufhn9j4otxc5p287sc.PNG)

It gets even worse because when Claude approaches its context limits, it's trained to be lazier and lazier in an effort to preserve its remaining window. Anthropic calls this **context awareness**; I call it laziness. 🤣

It's therefore in your best interest to keep your context lean so you can have reliable, comprehensive, and correct outputs from Claude.

## The Mental Framework for Unlocking Agentic Workflows

So, what is the correct mental framework for agentic workflows?

We start with the **Principle of Least Context**. Treat the main session exclusively as an orchestrator. In an ideal world, it should know nothing about the internals of the workflow.

Zero data leakage is the goal. The moment you leak data into the main context window, that's precious tokens wasted on what could've been orchestration.

In practice, this is what sub-agents are for. Sub-agents allow us to delegate work in a dedicated context window. This is crucial because it lets us contain/isolate several tool calls and file reads into its own throwaway window.

From the perspective of the main orchestrator, when the sub-agent's work is done, it just reads the summary/output of the work without leaking any of the intermediate discovery and artifacts along the way. *This* is the Principle of Least Context at work.

Now multiply these sub-agents in parallel, and you have a powerful primitive that enables your agent to analyze (practically) infinite context without intelligence degradation.

If you're processing several documents every day (e.g., emails, meeting transcripts, procurement requests, Yahoo Finance news articles, feature requirements, engagement proposals, etc.), the Principle of Least Context is the key that automates *reliable* batch processing for you.

### Agentic Workflows in Practice

Let's put this into practice. Here's an example workflow that I used to do manually once a week for half a day, but I now pass to Claude Code and have it done within the hour.

As a software engineer, I maintain several codebases at work and for my side projects. Each of those codebases has third-party dependencies. These are a bunch of open-source code that I didn't write, but still download and depend on for my project to work. It just makes development easier than writing everything from scratch.

But these dependencies need to be kept up to date for the latest features, performance improvements, bug fixes, and security patches. The problem is that not all dependency upgrades are safe; some can actually break existing code, which needs to be fixed after the fact.

So, Basti… how *do* you figure out which dependencies are safe to upgrade?

In the olden days, I would scour the GitHub repositories of every single outdated dependency.

`CHANGELOG.md`
`RELEASES.md`

Multiply this workflow by 20 dependencies, and now you have an entire half-day of research ahead of you on top of assessing the architectural impacts on the codebase, and also not to mention applying the necessary code fixes to the breaking changes.

And this is just for a week's worth of dependencies, by the way. If you slip up and lag behind by at least one month, it's easy to be outdated by 40+ dependencies. Boy, you're in trouble now.

When it comes to dependency management, **it's so much easier to keep up than catch up.**

### Dependabump: A Case Study on Effective Map-Reduce Patterns

## GitHub logo [BastiDood](https://github.com/BastiDood) / [dependency-wrangler](https://github.com/BastiDood/dependency-wrangler)

![GitHub logo](https://assets.dev.to/assets/github-logo-5a155e1f9a670af7944dd5e12375bc76ed542ea80224905ecaf878b9157cdefc.svg)

### A Claude Code marketplace for plugins that wrangle your dependencies.

# Dependency Wrangler

A [Claude Code](https://code.claude.com/docs/en/overview) plugin marketplace for dependency management tools.

## Installation

## Plugins

### Dependabump

Orchestrates dependency bumping across package managers: `npm`, `pnpm`, `yarn`, `bun`, `uv`, and `cargo`.

`npm`
`pnpm`
`yarn`
`bun`
`uv`
`cargo`

| Flag | Effect |
| --- | --- |
| `--include-major` | Include major version bumps (deferred by default) |
| `--include-patch` | Analyze patch bumps (assumed safe by default) |

`--include-major`
`--include-patch`

The workflow detects outdated packages, scrapes changelogs, assesses codebase impact, and proposes a staged upgrade plan ordered from safest to riskiest.

Warning

Running this workflow across ~20 dependencies can consume up to half of the 5-hour rate limits in a $100 Claude Max subscription. With ~40 parallelized dependencies, you may even hit rate limits on a single run entirely.

This is why the `--include-major` and `--include-patch` flags are disabled by default. Typically, most unexpected breaking changes occur in minor version bumps anyway.

`--include-major`
`--include-patch`

But, it's still better to *not*…

And that's why I automated this workflow and wrote the [Dependabump plugin for Claude Code](https://github.com/BastiDood/dependency-wrangler).

Dependabump takes everything that I just explained to you and does the changelog research for all outdated dependencies **in parallel sub-agents**.

In a typical run, Claude Code orchestrates around ~20 parallel researcher sub-agents to explore changelogs. At its peak, the workflow achieved 40 parallel sub-agents, which accomplished a full day's manual research in 15 minutes.

But our story doesn't end there. It's easy to parallelize work, but how do you consolidate the results? The (naive) default way is to dump all the summaries to the orchestrator. But this is stupid! We're back to square one by polluting the context window with changelog summaries.

[![visualization of a naive map-reduce workflow with a main orchestrator and its sub-agents dumping their context into the main context window](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbvx8xz3b076cci5x08zg.PNG)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbvx8xz3b076cci5x08zg.PNG)

![visualization of a naive map-reduce workflow with a main orchestrator and its sub-agents dumping their context into the main context window](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbvx8xz3b076cci5x08zg.PNG)

### Side Channel Persistence

The better way to do this is to have sub-agents dump their analyses in Markdown files, and only tell the orchestrator about these new files. This significantly reduces the context dump in the reduction step of the workflow.

Now here's the clever part: we spawn a brand new sub-agent whose responsibility is to read all of these `*.md` files and perform the consolidation work in its own context window.

`*.md`

[![visualization of a parallel map-reduce workflow with a main orchestrator and its sub-agents dumping their context into their own file outputs](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdd5t7t61x0tvo80ca4nk.PNG)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdd5t7t61x0tvo80ca4nk.PNG)

![visualization of a parallel map-reduce workflow with a main orchestrator and its sub-agents dumping their context into their own file outputs](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdd5t7t61x0tvo80ca4nk.PNG)

*Congratulations! You just shielded the orchestrator from the context dump.* 🎉

**Side channels** are a general pattern that you can apply in your own agentic workflows. The Principle of Least Context urges us to push heavy context into side channels such as file systems, databases, etc.

By the end of the workflow:

### When to Use Sub-Agents vs. Skills

Okay, but let's take a step back because I glossed over a few details on how to implement effective and efficient sub-agents.

So a while back, the Claude Code team introduced the notion of **forked skills**. Simply by setting your agent skill to use `context: fork`, you can now invoke an agent skill as if it were in its own context window.

`context: fork`

Because this feature blurs the line between skills and sub-agents, I want to set the record straight on what I've found to be the most effective way to use these features *and* how to think about them in our mental framework.

#### Sub-Agents

The **sub-agent prompt** determines the "personality" of the workflow. Like most system prompts, this is where you describe roles, goals, restrictions, and tools.

This is the *wrong* place to put your workflow steps. A system prompt is supposed to be lean guidance, much like how we strive to trim down our `CLAUDE.md`. *Less is more.*

`CLAUDE.md`

#### Agent Skills

Meanwhile, the **skill prompt** describes the exact steps of the workflow. This is where you describe (in excruciating detail) all the processes, the edge cases, and the expected output.

Being in an agent skill also grants you the superpower of **progressive disclosure**. Leverage `references/`, `scripts/`, and `assets/` directories in your skills so the agent can progressively load conditional context.

`references/`
`scripts/`
`assets/`

In Dependabump, I use this technique to only load the relevant package manager specifics of the project. Otherwise, I would've dumped them all into the core `SKILL.md` (e.g., `npm`, `pnpm`, `yarn`, `bun`, `cargo`, etc.). That's just a waste of tokens.

`SKILL.md`
`npm`
`pnpm`
`yarn`
`bun`
`cargo`

### (Forked) Skills and Sub-Agents

The interplay between skills and sub-agents becomes interesting when `context: fork` is set. From the official Claude Code docs, `context: fork` invokes a skill in a new context window, where the designated `agent` is the system prompt while the `SKILL.md` is the task delegation message. This is exactly why the skill should contain the workflow steps.

`context: fork`
`context: fork`
`agent`
`SKILL.md`

This is opposed to having a sub-agent with preloaded `skills`. In this case, we have no control over the delegation message. When a skill is invoked from within a sub-agent, the Claude Code harness generates the message for us.[1](#fn1)

`skills`

| Approach | System Prompt | Task | Also loads... |
| --- | --- | --- | --- |
| Skill with `context: fork` | From agent type (e.g., `Explore`, `Plan`, `general-purpose`) | `SKILL.md` content | `CLAUDE.md` |
| Sub-agent with `skills` field | Sub-agent's own Markdown body | Claude-generated delegation message | Preloaded skills + `CLAUDE.md` |

`context: fork`
`Explore`
`Plan`
`general-purpose`
`SKILL.md`
`CLAUDE.md`
`skills`
`CLAUDE.md`

So, for maximum control, I recommend the paired sub-agent + skill pattern: the sub-agent is the "personality" while the skill is the "workhorse".

⚠️ The main limitation of forked skills, however, is that they cannot be invoked in parallel unlike sub-agents. For parallel work, I still encode the workflow in the sub-agent's system prompt. This exception is unfortunately more of a Claude Code harness limitation than it is a conceptual limitation.

To keep things organized, I follow a simple naming convention: nouns for sub-agents and verbs for skills. For example: Dependabump has a `changelog-scraper` agent and an associated `scrape-dependency-changelogs` skill. They come in pairs, so name them in pairs, too.

`changelog-scraper`
`scrape-dependency-changelogs`

I'll admit that this is fairly verbose, which is why I advocate for wrapping single-entry-point workflows in Claude plugins so that they can be self-contained and namespaced. Then, just make sure to set your "private skills" (implementation details) as `user-invocable: false`.

`user-invocable: false`
`.claude/
├── agents/
│ ├── codebase-researcher.md
│ ├── changelog-consolidator.md
│ └── impact-assessor.md
└── skills/
├── assess-impacts/
│ └── SKILL.md
├── consolidate-changelogs/
│ └── SKILL.md
└── research-codebase/
└── SKILL.md`

#### The Pitfalls of Builtin Sub-Agents

Of course, you don't always have to write your own bespoke sub-agent; sometimes the builtin ones like `Explore`, `Plan`, and `general-purpose` are enough.

`Explore`
`Plan`
`general-purpose`

But, I must warn you that sub-agents do *not* inherit the skills from the parent conversation. If you *don't* explicitly list out the `skills` available to a sub-agent, then the Claude Code harness intentionally makes them inaccessible. This is by design.

`skills`
`name: coordinator
description: Coordinates work across specialized agents
tools: [Bash, Glob, Read]
skills: [api-conventions, error-handling-patterns] # Only these skills are visible!`

That means the builtin sub-agents (which have no configured `skills`, by the way!) have zero visibility into your entire corpus of agent skills. Yeah, you heard me right: the `Explore` and `Plan` sub-agents cannot read your skills! 🤯

`skills`
`Explore`
`Plan`

So to save you from hours of debugging, I recommend just defining your own custom sub-agent so you can explicitly configure the available `tools` and `skills`. The alternative is you finding out late into the workflow that your sub-agent had been stuck in a failure loop because it didn't have access to a particular skill.

`tools`
`skills`

## Conclusion

So what did we learn?

There's so much more to discuss like progressive disclosure techniques, but let's save that for the next meetup. In the meantime, I hope you've learned a lot from this demo.

*And please do install [Dependabump](https://github.com/BastiDood/dependency-wrangler) in your projects. Star ⭐ the GitHub repo and share it with your colleagues.*

*I know how much of a hassle it is to keep up with dependencies. I hope my little plugin bridges that gap for you and your team so you don't have to worry about outdated dependencies ever again.*

This table was adapted from the [official Claude Code documentation](https://code.claude.com/docs/en/skills#run-skills-in-a-subagent). [↩](#fnref1)

## Top comments (5)

![pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

Templates let you quickly answer FAQs or store snippets for re-use.

![arkforge-ceo profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3755080%2F98937c51-dc33-4340-8b80-726419aea69e.png)
![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3755080%2F98937c51-dc33-4340-8b80-726419aea69e.png)

The Principle of Least Context maps well beyond single-session workflows. When you split work across sub-agents (map-reduce style), each sub-agent inherits a context slice, but the trust boundary between those slices is implicit. Agent A compacts its context and hands a summary to Agent B. If B acts on a hallucinated summary, the damage propagates silently.

One pattern that helps: each sub-agent produces a verifiable output artifact (not just text) before the reduce step. The orchestrator can then validate inputs to the merge rather than trusting summaries. It adds friction but kills an entire class of silent corruption in long-running chains.

Have you seen teams implement verification gates between map and reduce phases in practice, or does the latency cost usually kill it?

![somedood profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F108756%2F1bb8b570-520b-4ad9-8a25-ee28c4d04a8d.jpeg)
![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F108756%2F1bb8b570-520b-4ad9-8a25-ee28c4d04a8d.jpeg)

That's exactly right! And at least for the workflows that I write, my sub-agents often have a validation script that uses JSON + `jq` to assert/clean the output schema of the side-channel-persisted files (e.g., `*.json`). Between intermediate steps, I strive to keep artifacts structured, thereby reserving the fuzzy interpretation only in the final part of the workflow (i.e., the human-readable presentation/view).

`jq`
`*.json`
![itskondrat profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3753205%2Fa206f74a-98be-4c2b-abbd-f06ec964327b.jpg)
![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3753205%2Fa206f74a-98be-4c2b-abbd-f06ec964327b.jpg)

ran into this building my agent fleet - the shift from prompting to designing systems where agents decide for themselves is where it actually gets hard. were the Manila workflows production or demos?

![somedood profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F108756%2F1bb8b570-520b-4ad9-8a25-ee28c4d04a8d.jpeg)
![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F108756%2F1bb8b570-520b-4ad9-8a25-ee28c4d04a8d.jpeg)

The talk itself was a demo of my [Dependabump plugin for Claude Code](https://github.com/BastiDood/dependency-wrangler), but the map-reduce techniques that I used to implement it were inspired by lessons learned shipping agentic workflows to production (hence this article).

![itskondrat profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3753205%2Fa206f74a-98be-4c2b-abbd-f06ec964327b.jpg)
![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3753205%2Fa206f74a-98be-4c2b-abbd-f06ec964327b.jpg)

map-reduce for agent orchestration is underused honestly. the fan-out part is easy - it's the reduce step where things get messy when branches disagree. checking dependabump.

Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's [permalink](#).

Hide child comments as well

Confirm

For further actions, you may consider blocking this person and/or [reporting abuse](/report-abuse)

![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F108756%2F1bb8b570-520b-4ad9-8a25-ee28c4d04a8d.jpeg)

### More from [Basti Ortiz](/somedood)

💎 DEV Diamond Sponsors

Thank you to our Diamond Sponsors for supporting the DEV Community

![Google AI - Official AI Model and Platform Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxjlyhbdqehj3akhz166w.png)

Google AI is the official AI Model and Platform Partner of DEV

![Neon - Official Database Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbnl88cil6afxzmgwrgtt.png)

Neon is the official database partner of DEV

![Algolia - Official Search Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv30ephnolfvnlwgwm0yz.png)

Algolia is the official search partner of DEV

[DEV Community](/) — A space to discuss and keep up software development and manage your software career

Built on [Forem](https://www.forem.com) — the [open source](https://dev.to/t/opensource) software that powers [DEV](https://dev.to) and other inclusive communities.

Made with love and [Ruby on Rails](https://dev.to/t/rails). DEV Community © 2016 - 2026.

![DEV Community](https://media2.dev.to/dynamic/image/width=190,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

We're a place where coders share, stay up-to-date and grow their careers.

![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)
![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
