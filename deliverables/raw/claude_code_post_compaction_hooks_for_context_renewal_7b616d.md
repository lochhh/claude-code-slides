# Claude Code: Post-Compaction Hooks for Context Renewal

**Type:** article
**URL:** https://medium.com/@porter.nicholas/claude-code-post-compaction-hooks-for-context-renewal-7b616dcaa204
**Topic:** Context Management
**Published:** unknown

## Content

# Claude Code: Post-Compaction Hooks for Context Renewal | by Nick Porter | Mar, 2026 | Medium

[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40porter.nicholas%2Fclaude-code-post-compaction-hooks-for-context-renewal-7b616dcaa204&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40porter.nicholas%2Fclaude-code-post-compaction-hooks-for-context-renewal-7b616dcaa204&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Image 1](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

# Claude Code: Post-Compaction Hooks for Context Renewal

[![Image 2: Nick Porter](https://miro.medium.com/v2/da:true/resize:fill:32:32/0*rZ7mPK45Co0PX60-)](https://medium.com/@porter.nicholas?source=post_page---byline--7b616dcaa204---------------------------------------)

[Nick Porter](https://medium.com/@porter.nicholas?source=post_page---byline--7b616dcaa204---------------------------------------)

Follow

5 min read

·

Mar 4, 2026

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F7b616dcaa204&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40porter.nicholas%2Fclaude-code-post-compaction-hooks-for-context-renewal-7b616dcaa204&user=Nick+Porter&userId=6b18eabac222&source=---header_actions--7b616dcaa204---------------------clap_footer------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F7b616dcaa204&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40porter.nicholas%2Fclaude-code-post-compaction-hooks-for-context-renewal-7b616dcaa204&source=---header_actions--7b616dcaa204---------------------bookmark_footer------------------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D7b616dcaa204&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40porter.nicholas%2Fclaude-code-post-compaction-hooks-for-context-renewal-7b616dcaa204&source=---header_actions--7b616dcaa204---------------------post_audio_button------------------)

Share

Hiya! My name is Nick and I have been writing Web apps since ’98. I love the ability to share what I wrote with anyone in the world anytime. I have been using Claude for writing my code for the last 7 months and have become an expert at manipulating context over the course of long-running tasks. By automating my system around preserving a healthy context I found the best way to achieve the highest quality code possible.

How do I measure high quality? 

 — React 19 standards (no useEffect)

 — Components and DB written for scalability

 — Test Driven Development (TDD)

 — Always sticking to workflow rules: Explore, Plan then Execute

Press enter or click to view image in full size

![Image 3](https://miro.medium.com/v2/resize:fit:700/1*JEDXdewyKs-6_XuoZF3p_Q.png)

Image Credit Gemini

> The compaction preserved the code but lost the rules.

### Where Things Can Go Wrong

You have been coding for about 8–12 hours across sleep boundaries. Fortunately you named the sessions for each Claude so you know you have used up a handful of different sessions and or compactions. At each stage interval you made sure to test what Claude had produced and so far so good. Then all the sudden after a compaction Claude thinks the files and in-flight and failing tests are from another session and not Claude’s responsibility.

The compaction preserved the code but lost the rules and even the scope of the full effort. This is often why I fire up a new Claude sessions to begin with and pass it a session file. This is also violating exactly the thing I hoped the CLAUDE.md would prevent!

## [Teaching Claude To Remember: Part 3 — Sessions And Resumable Workflow ### Hiya! My name is Nick and if you have been following my series on Claude Code you know now is when we get to the fun… medium.com](https://medium.com/@porter.nicholas/teaching-claude-to-remember-part-3-sessions-and-resumable-workflow-1c356d9e442f?source=post_page-----7b616dcaa204---------------------------------------)

> Claude determines what should survive compaction based on recency, relevance, and frequency.

### How Auto-Compaction Works (And Why It Drops Things)

When you context fills up Claude Code automatically summarizes the conversation to free up space. A typical compaction frees up 60–70% of your context. The coding community as a whole is reporting that working past 70% context can reduce code quality and lead to errors.

## [Compaction ### Server-side context compaction for managing long conversations that approach context window limits. platform.claude.com](https://platform.claude.com/docs/en/build-with-claude/compaction?source=post_page-----7b616dcaa204---------------------------------------)

Compaction is a lossy summarization process. Claude determines what should survive compaction based on recency, relevance, and frequency. The result is the Claude’s knowledge of the code and its immediate task is preserved but what is lost project conventions — the things that prevent bugs — are mentioned once at the beginning of each conversation. They are prime candidates for compression.

CLAUDE.md can help mitigate the problem but it is also part of the conversation context. After compaction it is summarized alongside everything else you discussed during that session.

I would need to often remind Claude to double check things post-compaction like was TDD followed? What I needed was a reliable way to inject project specific critical context without thinking about it.

## [Hooks reference - Claude Code Docs ### Reference for Claude Code hook events, configuration schema, JSON input/output formats, exit codes, async hooks, HTTP… code.claude.com](https://code.claude.com/docs/en/hooks?source=post_page-----7b616dcaa204---------------------------------------)

### The Pattern: PostToolUse Hook + Context Essentials

Using Claude Code’s hook system we fire shell commands at specific lifecycle events. For our post-compaction hook we want to use the `PostToolUse` lifecycle event with the `compact` matcher. When compaction happens, this hook fires and its `stdout` gets injected as a system message, and Claude immediately has your rules back!!

That’s what I’m talkin about my friends! Even as Claude Code has improvements like Auto-Memory and Agent Teams (still in beta) added that help make context preservation possible post-compaction rule injection is STILL important.

### Step 1: Create Your Context Essentials File

You should get Claude to read this article then tailor your context essentials based on your project type but to give you an idea of what I have in mine running a NextJS app with TanStack, Zustand, React 19 and Mantine.

## Get Nick Porter’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

- [x] 

Remember me for faster sign in

 

Keep this under 50 lines. Every line costs tokens and this will be loaded on every single compaction so be frugal. Think of this as a sticky note on your monitor, no not the horoscope you cut out from the coffee shop, the one that reminds you of the things you often forget.

<!-- .claude/context-essentials.md -->

# Context Essentials (Re-injected After Compaction)

## Critical Rules

- Use dateCore with timezone for ALL date operations — NEVER new Date() or direct Luxon

- Use protectedProcedure + ctx.userId — NEVER accept userId from client input

- Supabase: execute _sql for reads only. NEVER apply_ migration without human approval

- Quality gates: npm test && npm run type-check && npm run lint before commit

- SSR auth: 'use client' uses getSupabaseClient(); server components use createClient from server

## Banned Patterns

- No @ts-ignore, @ts-expect-error, eslint-disable

- No new Date(), Date.now(), direct Luxon DateTime import

- No dateCore without explicit timezone parameter

- No SELECT * — always specify columns

- No --no-verify on git operations
### Step 2: Configure The Hook

Now with this configured the hook will fire every time compaction occurs. In .claude/settings.json make this addition.

{

 "hooks": {

 "PostToolUse": [

 {

 "matcher": "compact",

 "command": "cat .claude/context-essentials.md"

 }

 ]

 }

}

Press enter or click to view image in full size

![Image 4](https://miro.medium.com/v2/resize:fit:700/1*IUZxHZfRAkcNwKQPUreWfg.png)

Image Credit Gemini

### Why This Does More Than Just CLAUDE.md

You may wonder _“my rules are already in (or referenced in) CLAUDE.md, why do I need another file?”_.

> Context Essentials = this ‘Before You Ship’

CLAUDE.md is meant to be a comprehensive guide. Architecture decisions, workflow instructions, coding standard, available commands. It is (or should be) around 200 lines and is loaded at session start and lives in context permanently.

Context essentials is 10–50 lines surgically injection post-compaction. Think of it like this.

— CLAUDE.md = the employee handbook

 — Context Essentials = this ‘Before You Ship’ checklist

## [Best Practices for Claude Code - Claude Code Docs ### Tips and patterns for getting the most out of Claude Code, from configuring your environment to scaling across parallel… code.claude.com](https://code.claude.com/docs/en/best-practices?source=post_page-----7b616dcaa204---------------------------------------)

Press enter or click to view image in full size

![Image 5](https://miro.medium.com/v2/resize:fit:700/1*UgKrA7sBcBB2eutPJORU1A.png)

Image Credit Gemini

### What To Include

— Project enforced rules like the aforementioned date library

 — Authentication Patterns

 — Database access rules

 — Import path rules (client vs server)

 — Banned anti-patterns

### What To Leave Out

— Full CLAUDE.md content (already loaded)

 — Architecture documentation (use skills/docs)

 — Code examples (these should be available in app)

 — Style preferences 

 — Historical decisions

### Summary

I hope this pattern helps you with your Claude use and when determining what workflow is most optimal for you! So tell me what are you using in your workflow? Please tell me what you’re doing to preserve context?

[Anthropic Claude](https://medium.com/tag/anthropic-claude?source=post_page-----7b616dcaa204---------------------------------------)

[Claude Code](https://medium.com/tag/claude-code?source=post_page-----7b616dcaa204---------------------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F7b616dcaa204&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40porter.nicholas%2Fclaude-code-post-compaction-hooks-for-context-renewal-7b616dcaa204&user=Nick+Porter&userId=6b18eabac222&source=---footer_actions--7b616dcaa204---------------------clap_footer------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F7b616dcaa204&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40porter.nicholas%2Fclaude-code-post-compaction-hooks-for-context-renewal-7b616dcaa204&user=Nick+Porter&userId=6b18eabac222&source=---footer_actions--7b616dcaa204---------------------clap_footer------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F7b616dcaa204&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40porter.nicholas%2Fclaude-code-post-compaction-hooks-for-context-renewal-7b616dcaa204&source=---footer_actions--7b616dcaa204---------------------bookmark_footer------------------)

[![Image 6: Nick Porter](https://miro.medium.com/v2/resize:fill:48:48/0*rZ7mPK45Co0PX60-)](https://medium.com/@porter.nicholas?source=post_page---post_author_info--7b616dcaa204---------------------------------------)

[![Image 7: Nick Porter](https://miro.medium.com/v2/resize:fill:64:64/0*rZ7mPK45Co0PX60-)](https://medium.com/@porter.nicholas?source=post_page---post_author_info--7b616dcaa204---------------------------------------)

Follow

## [Written by Nick Porter](https://medium.com/@porter.nicholas?source=post_page---post_author_info--7b616dcaa204---------------------------------------)

[38 followers](https://medium.com/@porter.nicholas/followers?source=post_page---post_author_info--7b616dcaa204---------------------------------------)

·[24 following](https://medium.com/@porter.nicholas/following?source=post_page---post_author_info--7b616dcaa204---------------------------------------)

Follow

## No responses yet

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--7b616dcaa204---------------------------------------)

![Image 8](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40porter.nicholas%2Fclaude-code-post-compaction-hooks-for-context-renewal-7b616dcaa204&source=---post_responses--7b616dcaa204---------------------respond_sidebar------------------)

Cancel

Respond

[Help](https://help.medium.com/hc/en-us?source=post_page-----7b616dcaa204---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----7b616dcaa204---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----7b616dcaa204---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----7b616dcaa204---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----7b616dcaa204---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----7b616dcaa204---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----7b616dcaa204---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----7b616dcaa204---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----7b616dcaa204---------------------------------------)
