# How I use Claude Code to accelerate my software engineering job ...

**Type:** article
**URL:** https://dev.to/juandj/how-i-use-claude-code-to-accelerate-my-software-engineering-job-and-improve-my-life-8o7
**Topic:** Prompting Strategies
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
![Juan Pablo Djeredjian](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F299631%2F77ba682e-3eeb-42df-813e-03214bb9795a.jpeg)

Posted on Jan 26

![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)
![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)

# How I use Claude Code to accelerate my software engineering job and improve my life

Claude Code has taken the software engineering world by storm and it's changing how the field looks in leaps and bounds. Prominent engineers are proudly saying that they're writing 0 lines of code already. [Jaana Dogan](https://x.com/rakyll/status/2007239758158975130), a Principal Engineer at Google working on Gemini, recently shared that she gave Claude Code a description of a distributed agent orchestrator problem, and it generated in about an hour what her team had been trying to build for the past year. She was careful to clarify: this was a proof-of-concept, not production-ready code. It still required validation, security reviews, performance testing. But still. An hour versus a year. Even with all the caveats, that's a staggering shift.

My feeling after working with Claude Code this year is actually: the upside is so huge that I'm surprised I'm not seeing it reflected in the amount of apps, features, and sheer progress in the software world. And I don't think we're in an early adoption phase anymore, as many argue. I think writing code has been commoditized already, and that just means the bottleneck has simply moved elsewhere: to generating new ideas, to testing and releasing, and above all, to distribution. The AI-generated apps might already be there, flooding the market; we're just not aware of them. They simply don't reach us.

And yet, while this is all exciting, it's also incredibly anxiety inducing. If you're a software engineer, you're probably feeling it too. Every week there's a new announcement, a new capability, a new "this changes everything" moment. And you're left wondering: am I keeping up? Am I falling behind? Will I still have a job in two years?

I don't have answers to those questions, I think nobody does yet for sure. But what I can tell you is how I've been using these tools to become significantly more productive, and how that productivity has actually made my job more enjoyable, not less. The more I use AI, the more I realize that the engineers who learn to collaborate effectively with these tools will have a massive advantage. That's what this post is about.

## Section 1: Software Engineering

I'm not here to rehash Claude Code's features. Plenty of guides cover CLAUDE.md files, /commands, and skills. If you want a great starting point, [Boris Cherny's thread](https://x.com/bcherny/status/2007179832300581177) (he created Claude Code) is excellent. His most striking revelation: "In the last thirty days, 100% of my contributions to Claude Code were written by Claude Code." And that includes 100% of the code written for the Claude Cowork project!

So, let me share what I've actually learned from almost a year of daily use. These aren't smart ways to use Claude's features, they're habits, workflows, and mental models that emerged from daily use. Things that simply weren't practical before Claude Code made them possible, but now are the very core of how I work as a software engineer.

### Understand EVERYTHING

Joining a company used to mean months of gradual ramp-up. You'd slowly build mental models of different features, ask the same questions repeatedly, and forget half of what you learned. Today, there's no excuse for that.

With Claude Code, I send agents to investigate entire services, and point it to Jira tickets, GitHub PRs, Slack threads, whatever expands context. Then I have it produce an exhaustive, didactic guide in markdown and save it to a dedicated `AI_DOCS/` folder in my repo.

`AI_DOCS/`

Ask it to make extensive use of ASCII diagrams. Claude Code with Opus 4.5 really excels at this and is a wonder at explaining complex, multi-repo data flows and architectures.

Here's what I have Claude document for every major service:

One of my guides distills dozens of conversations, PRs, and debugging sessions into a single source of truth. That's months of accumulated understanding I never have to rebuild.

The prompt pattern I use looks something like this:

`Explore [SERVICE/FEATURE] and create comprehensive documentation:
1. Executive Summary - what is its core purpose?
2. Architecture - how is it structured? Include ASCII diagrams.
3. Data Flows - how does data move in and out? Visualize with diagrams.
4. API Routes - what endpoints does it expose?
5. Database - what does it store? Include schema overview.
6. External Dependencies - what other services does it call? How?
7. Key Files - where's the important logic?
8. Common Gotchas - what breaks? What's confusing? What's undocumented?
9. Common Operations - how do you test/deploy/debug it?`

This is your treasure. Every time you revisit that system, debug something adjacent, or tackle a related feature, you have instant context, both for yourself and to feed back to Claude. The knowledge compounds instead of evaporating.

### Give Claude access to every possible tool

Claude will be able to use all tools at your disposal faster, more efficiently and deeper than you. There are some tools which I think are essential, and you'd be shooting yourself in the foot by not having them.

💡 If both options exist, I prefer CLIs to MCPs (which fill up the context and can be slow). CLIs are extremely capable and fast and will give you the same features (or more) than its respective MCP.

Here's my essential toolkit:

### Make all knowledge LLM-consumable

Every startup has that ONE person who knows how feature X works, what that esoteric Clojure project does, or how to wire up Salesforce in local dev. In the past, you'd schedule a meeting, frantically take notes, maybe record it. Then good luck rewatching that hour-long video every time you needed to follow the steps.

Here's the trick: AI can extract that tribal knowledge and turn it into permanent, queryable documentation.

A Meeting Copilot summary won't cut it here. When you need extensive detail (steps to follow, historical decisions, specific commands), a summary loses too much. You need the raw material: video + transcript.

Here's what I do:

**Record the knowledge transfer.** Send a Meeting Copilot, or just screen-record while the expert walks you through the process.

**Get video + transcript.** You want both. The transcript captures what was said, but the screen shares show what was *done*.

**Extract frames from the video.** Claude can't process video directly (yet), but it can process images. I use ffmpeg to grab a frame every few seconds:

`ffmpeg -i meeting_recording.mp4 -vf "fps=1/3" frames/frame_%04d.png`

The results are remarkable. Claude produced a step-by-step guide with screenshots accurately selected based on what was being discussed at each moment, pulling information from both the transcript and the shared screen.

Now you have a guide you'll never need to remake. But here's the real payoff: feed that guide back to Claude, and it can probably do the task for you.

This is what I mean by making knowledge LLM-consumable. Extract tribal knowledge once, and it becomes available to AI forever. The expert's time is captured, not lost.

### Learn in context

Learning a new technology used to be tedious. Read the docs, try their toy examples, maybe spin up a starter boilerplate. But those never felt like real use cases. You'd understand the syntax without understanding how it fits into a real codebase with real constraints.

Claude Code flips this. Instead of learning in isolation, I learn in context: my actual app, my actual complexity, my actual requirements.

Here's what that looks like:

A real example: I was building an app that needed agentic workflows and wanted to evaluate frameworks: OpenAI Agents SDK, Claude Agents SDK, Google ADK, and AWS Strands. I had Claude build a POC with the OpenAI SDK first, explaining the architecture and tradeoffs as it went. Once I understood how that worked, I opened multiple Claude terminals and asked it to rebuild the same functionality with each of the other frameworks, documenting the differences.

Within an afternoon, I had four working implementations and a clear sense of the tradeoffs. All in running code I could modify and extend.

Then I pushed further. I'd heard vaguely that Temporal could help with "long-running workflows" and human-in-the-loop patterns, but I didn't know how that would fit or help my app.

So I asked Claude: "What Temporal features could help me here?" It returned seven specific use cases, including the exact scenario I needed, each with proposal of parts of my codebase where it could help, with diffs and explanations for each.

But I didn't stop there. After going through the recommendations and understanding the proposals, I asked: "So, why is Temporal necessary? Can't I achieve this without it?" And it showed me a side-by-side comparison of both architectures, with side by side code samples pulled directly from the app I'd already built.

That's the difference. Real comparisons, in your code, for your use case. So you can learn and understand by making sense of new things in a context that actually matters and makes senses to you.

### Use multiple AI tools together

Every model has blind spots. On any given run, one might miss an edge case, another might over-engineer, another might take a completely different architectural approach. When you run the same complex task through multiple models and compare their outputs, the differences themselves reveal tradeoffs you wouldn't have considered.

For any non-trivial task, I'll prompt:

Then I compare their approaches. Sometimes one spots edge cases the others missed. Sometimes they propose completely different architectures. By combining insights from multiple outputs, I often end up with a more robust implementation than any single model would have produced alone.

I also do cross-model review. After one AI generates a plan or code, I have another review it:

`Here is a plan that Claude generated for [TASK]:
[Paste the plan]
Please review this plan and identify:
1. Potential edge cases not covered
2. Security concerns
3. Performance implications
4. Missing error handling
5. Simpler alternative approaches`

Think of it as an AI forum. You put models in healthy competition, letting them challenge and refine each other's thinking. The result is better than what any single model would produce, and you get there faster than going back and forth with just one.

## Section 2: How to use Claude Code to improve your life

A few weeks ago I read [Molly Cantillon's "The Personal Panopticon"](https://x.com/mollycantillon/status/2008918474006122936) and it broke something in my brain.

Her core insight is this: we are drowning in data about ourselves and yet we remain catastrophically blind. Our commitments exist in six different apps and cohere in none. Our finances are scattered across brokerages that refuse to talk to each other. Our goals live in some forgotten note from January. We have more information about ourselves than any human in history, and we can barely see any of it.

Her solution to this problem is simple: Build your own panopticon. Put yourself in the tower. Use Claude Code as the apparatus of sight, but point it inward.

She runs multiple Claude Code instances in parallel, each watching a different part of her life. Finances, health, email, personal projects. Her finances get synthesized overnight from multiple brokerages, cross-referenced with market data, and she wakes up to a brief. Her product metrics get pulled automatically and turned into actionable insights. Her email reaches inbox zero with auto-drafted replies she just reviews.

I'm not there yet. But I started building toward it.

I have a main folder with a `CLAUDE.md` file where I let Claude know basically everything about me, or tell it what external data sources to pull from to know:

`CLAUDE.md`

Yes, basically everything there is to know about me. I know how that sounds. But I've realized that the more Claude knows, the more useful it becomes. When I ask "should I take this job offer?" it doesn't give me generic advice about pros and cons. It knows my financial situation, my career trajectory, my family plans, my risk tolerance. It can actually reason about MY situation, not some hypothetical person's.

To start this out, I asked ChatGPT (which has the memory feature) to create a comprehensive personal profile guide to be consumed by Claude Code. Since ChatGPT already knew a lot about me from our conversations over the past year, it was able to compile a pretty good starting point. Then I reviewed it, added details, corrected things it got wrong, and now I keep it updated as things change.

Some real question Claude has helped me answer:

And unlike a human advisor who you'd have to re-explain your whole situation to every single time, Claude just reads the file and has full context immediately.

I'm also starting to play with [Clawdbot](https://github.com/clawdbot/clawdbot), a self-hosted assistant that connects Claude to my messaging apps. So instead of opening a terminal, I can just message my AI through WhatsApp or Telegram, from anywhere.

Cantillon ends her essay with: "The tools of synthesis belong to the individual now. Govern yourself accordingly."

I'm trying to.

## Top comments (2)

![pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

Templates let you quickly answer FAQs or store snippets for re-use.

Some comments may only be visible to logged-in visitors. [Sign in](/enter) to view all comments.

Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's [permalink](#).

Hide child comments as well

Confirm

For further actions, you may consider blocking this person and/or [reporting abuse](/report-abuse)

![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F299631%2F77ba682e-3eeb-42df-813e-03214bb9795a.jpeg)

### Trending on [DEV Community](https://dev.to) Hot

![Ben Halpern profile image](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1%2Fbabb96d0-9cd2-49bc-a412-2dc4caf94c2a.png)
![Konark Sharma profile image](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2928108%2Ffb504115-5d98-486b-bee9-c2de7cb7b632.png)
![Tombri Bowei profile image](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1745361%2Fa5ccba4b-d4ad-4f12-8265-dcd18c3775cd.jpg)

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
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)
