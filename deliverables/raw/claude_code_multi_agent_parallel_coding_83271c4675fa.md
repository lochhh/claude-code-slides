# Multi-agent parallel coding with Claude Code Subagents - Medium

**Type:** article
**URL:** https://medium.com/@codecentrevibe/claude-code-multi-agent-parallel-coding-83271c4675fa
**Topic:** Subagents & Parallel Execution
**Published:** unknown

## Content

# Multi-agent parallel coding with Claude Code Subagents | by Cuong Tham | Medium

[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Image 1](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

# Multi-agent parallel coding with Claude Code Subagents

[![Image 2: Cuong Tham](https://miro.medium.com/v2/resize:fill:64:64/1*GcuTZKegfWRfb7g_knzF7Q.png)](https://medium.com/@codecentrevibe?source=post_page---byline--83271c4675fa---------------------------------------)

[Cuong Tham](https://medium.com/@codecentrevibe?source=post_page---byline--83271c4675fa---------------------------------------)

Follow

7 min read

·

Jul 17, 2025

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F83271c4675fa&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&user=Cuong+Tham&userId=cec6f23a097f&source=---header_actions--83271c4675fa---------------------clap_footer------------------)

63

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F83271c4675fa&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=---header_actions--83271c4675fa---------------------bookmark_footer------------------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D83271c4675fa&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=---header_actions--83271c4675fa---------------------post_audio_button------------------)

Share

Today I am going to explore a concept called “subagent” in Claude Code. I could not find any official documentation about it, but I found some references in the [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices) article.

Press enter or click to view image in full size

![Image 3](https://miro.medium.com/v2/resize:fit:700/1*Y8V5T67zBSycJ7_LYbStgw.png)

## What is a Subagent?

After some experimentation, I think “subagent” is a lightweight instance of Claude Code running in a task via the [Task Tool](https://cuong.io/blog/2025/06/24-claude-code-what-is-task-tool). When a subagent is running, you can actually see that the output says “Task(Performing task X)”.

One interesting fact is that you can actually run **multiple subagents** in parallel. For example, you can launch 4 parallel tasks with this prompt:

Explore the codebase using 4 tasks in parallel. Each agent should explore different directories.
As far as I can tell, each subagent will have its own context window, so this is a neat way to gain additional context window for large codebases.

Here’s an example run of the prompt:

> Explore the code base using 4 tasks in parallel. 

Each agent should explore different directories.● I'll explore the codebase using 4 parallel tasks to understand the project structure and implementation.● Task(Explore backend structure)

 ⎿ Done (17 tool uses · 56.6k tokens · 1m…

## Create an account to read the full story.

The author made this story available to Medium members only.

If you’re new to Medium, create a new account to read this story on us.

[Continue in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3Dregwall&source=-----83271c4675fa---------------------post_regwall------------------)

Or, continue in mobile web

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa%3Fsource%3D-----83271c4675fa---------------------post_regwall------------------%26skipOnboarding%3D1%7Cregister%7Cremember_me&source=-----83271c4675fa---------------------post_regwall------------------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa%3Fsource%3D-----83271c4675fa---------------------post_regwall------------------%26skipOnboarding%3D1%7Cregister%7Cremember_me&source=-----83271c4675fa---------------------post_regwall------------------)

Sign up with email

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=-----83271c4675fa---------------------post_regwall------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F83271c4675fa&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&user=Cuong+Tham&userId=cec6f23a097f&source=---footer_actions--83271c4675fa---------------------clap_footer------------------)

63

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F83271c4675fa&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&user=Cuong+Tham&userId=cec6f23a097f&source=---footer_actions--83271c4675fa---------------------clap_footer------------------)

63

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F83271c4675fa&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=---footer_actions--83271c4675fa---------------------bookmark_footer------------------)

[![Image 4: Cuong Tham](https://miro.medium.com/v2/resize:fill:96:96/1*GcuTZKegfWRfb7g_knzF7Q.png)](https://medium.com/@codecentrevibe?source=post_page---post_author_info--83271c4675fa---------------------------------------)

[![Image 5: Cuong Tham](https://miro.medium.com/v2/resize:fill:128:128/1*GcuTZKegfWRfb7g_knzF7Q.png)](https://medium.com/@codecentrevibe?source=post_page---post_author_info--83271c4675fa---------------------------------------)

Follow

## [Written by Cuong Tham](https://medium.com/@codecentrevibe?source=post_page---post_author_info--83271c4675fa---------------------------------------)

[32 followers](https://medium.com/@codecentrevibe/followers?source=post_page---post_author_info--83271c4675fa---------------------------------------)

·[4 following](https://medium.com/@codecentrevibe/following?source=post_page---post_author_info--83271c4675fa---------------------------------------)

A vibe coding enthusiast.

Follow

## No responses yet

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--83271c4675fa---------------------------------------)

![Image 6](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=---post_responses--83271c4675fa---------------------respond_sidebar------------------)

Cancel

Respond

## More from Cuong Tham

![Image 7: Claude Code Best Practices: Memory Management](https://miro.medium.com/v2/resize:fit:679/format:webp/1*CqiyWKqMYjJCNu0P8bkB7w.png)

[![Image 8: Cuong Tham](https://miro.medium.com/v2/resize:fill:20:20/1*GcuTZKegfWRfb7g_knzF7Q.png)](https://medium.com/@codecentrevibe?source=post_page---author_recirc--83271c4675fa----0---------------------976ef243_0307_400e_a01c_5320d5d28f3e--------------)

[Cuong Tham](https://medium.com/@codecentrevibe?source=post_page---author_recirc--83271c4675fa----0---------------------976ef243_0307_400e_a01c_5320d5d28f3e--------------)

## [Claude Code Best Practices: Memory Management ### Dive into Claude Code’s memory management mechanism. Clear up misconceptions and be more context efficient with Claude Code.](https://medium.com/@codecentrevibe/claude-code-best-practices-memory-management-7bc291a87215?source=post_page---author_recirc--83271c4675fa----0---------------------976ef243_0307_400e_a01c_5320d5d28f3e--------------)

Aug 8, 2025

[43](https://medium.com/@codecentrevibe/claude-code-best-practices-memory-management-7bc291a87215?source=post_page---author_recirc--83271c4675fa----0---------------------976ef243_0307_400e_a01c_5320d5d28f3e--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=---author_recirc--83271c4675fa----0-----------------explicit_signal----976ef243_0307_400e_a01c_5320d5d28f3e--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F7bc291a87215&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-best-practices-memory-management-7bc291a87215&source=---author_recirc--83271c4675fa----0-----------------bookmark_preview----976ef243_0307_400e_a01c_5320d5d28f3e--------------)

![Image 9: What is Vibe Coding: My Personal Take](https://miro.medium.com/v2/resize:fit:679/format:webp/1*M4pmlXmJyQpZ2FwzMkhaag.png)

[![Image 10: Cuong Tham](https://miro.medium.com/v2/resize:fill:20:20/1*GcuTZKegfWRfb7g_knzF7Q.png)](https://medium.com/@codecentrevibe?source=post_page---author_recirc--83271c4675fa----1---------------------976ef243_0307_400e_a01c_5320d5d28f3e--------------)

[Cuong Tham](https://medium.com/@codecentrevibe?source=post_page---author_recirc--83271c4675fa----1---------------------976ef243_0307_400e_a01c_5320d5d28f3e--------------)

## [What is Vibe Coding: My Personal Take ### Vibe coding has become extremely popular nowadays that even non-tech people are aware of it. What’s your definition of vibe coding?](https://medium.com/@codecentrevibe/what-is-vibe-coding-my-personal-take-9dfdeaf6cadb?source=post_page---author_recirc--83271c4675fa----1---------------------976ef243_0307_400e_a01c_5320d5d28f3e--------------)

Aug 17, 2025

[](https://medium.com/@codecentrevibe/what-is-vibe-coding-my-personal-take-9dfdeaf6cadb?source=post_page---author_recirc--83271c4675fa----1---------------------976ef243_0307_400e_a01c_5320d5d28f3e--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=---author_recirc--83271c4675fa----1-----------------explicit_signal----976ef243_0307_400e_a01c_5320d5d28f3e--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9dfdeaf6cadb&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fwhat-is-vibe-coding-my-personal-take-9dfdeaf6cadb&source=---author_recirc--83271c4675fa----1-----------------bookmark_preview----976ef243_0307_400e_a01c_5320d5d28f3e--------------)

[See all from Cuong Tham](https://medium.com/@codecentrevibe?source=post_page---author_recirc--83271c4675fa---------------------------------------)

## Recommended from Medium

![Image 11: CLAUDE.md Best Practices](https://miro.medium.com/v2/resize:fit:679/format:webp/1*grkcAnwIvZ62EI_cy4KSSA.png)

[![Image 12: UX Planet](https://miro.medium.com/v2/resize:fill:20:20/1*A0FnBy5FBoVQC02SZXLXPg.png)](https://medium.com/ux-planet?source=post_page---read_next_recirc--83271c4675fa----0---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

In

[UX Planet](https://medium.com/ux-planet?source=post_page---read_next_recirc--83271c4675fa----0---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

by

[Nick Babich](https://medium.com/@101?source=post_page---read_next_recirc--83271c4675fa----0---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

## [CLAUDE.md Best Practices ### 10 Sections to Include in your CLAUDE.md](https://medium.com/ux-planet/claude-md-best-practices-1ef4f861ce7c?source=post_page---read_next_recirc--83271c4675fa----0---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

Mar 6

[886 17](https://medium.com/ux-planet/claude-md-best-practices-1ef4f861ce7c?source=post_page---read_next_recirc--83271c4675fa----0---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=---read_next_recirc--83271c4675fa----0-----------------explicit_signal----1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F1ef4f861ce7c&operation=register&redirect=https%3A%2F%2Fuxplanet.org%2Fclaude-md-best-practices-1ef4f861ce7c&source=---read_next_recirc--83271c4675fa----0-----------------bookmark_preview----1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

![Image 13: Build Your First Claude Code Agent Skill: A Simple Project Memory System That Saves Hours](https://miro.medium.com/v2/resize:fit:679/format:webp/1*O2_piSNfbAuTTlXEy4i-oA.png)

[![Image 14: Artificial Intelligence in Plain English](https://miro.medium.com/v2/resize:fill:20:20/1*9zAmnK08gUCmZX7q0McVKw@2x.png)](https://medium.com/ai-in-plain-english?source=post_page---read_next_recirc--83271c4675fa----1---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

In

[Artificial Intelligence in Plain English](https://medium.com/ai-in-plain-english?source=post_page---read_next_recirc--83271c4675fa----1---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

by

[Rick Hightower](https://medium.com/@richardhightower?source=post_page---read_next_recirc--83271c4675fa----1---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

## [Build Your First Claude Code Agent Skill: A Simple Project Memory System That Saves Hours ### How a 300-line skill became my most-used productivity tool for AI-assisted development.](https://medium.com/ai-in-plain-english/build-your-first-claude-code-skill-a-simple-project-memory-system-that-saves-hours-1d13f21aff9e?source=post_page---read_next_recirc--83271c4675fa----1---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

Jan 12

[1.7K 34](https://medium.com/ai-in-plain-english/build-your-first-claude-code-skill-a-simple-project-memory-system-that-saves-hours-1d13f21aff9e?source=post_page---read_next_recirc--83271c4675fa----1---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=---read_next_recirc--83271c4675fa----1-----------------explicit_signal----1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F1d13f21aff9e&operation=register&redirect=https%3A%2F%2Fai.plainenglish.io%2Fbuild-your-first-claude-code-skill-a-simple-project-memory-system-that-saves-hours-1d13f21aff9e&source=---read_next_recirc--83271c4675fa----1-----------------bookmark_preview----1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

![Image 15: How I Made Claude Code Agents Coordinate 100% and Solved Context Amnesia](https://miro.medium.com/v2/resize:fit:679/format:webp/1*fb18n15Eu2IwELvioRax7w.png)

[![Image 16: Ilyas Ibrahim Mohamed](https://miro.medium.com/v2/resize:fill:20:20/1*dmbNkD5D-u45r44go_cf0g.png)](https://medium.com/@ilyas.ibrahim?source=post_page---read_next_recirc--83271c4675fa----0---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[Ilyas Ibrahim Mohamed](https://medium.com/@ilyas.ibrahim?source=post_page---read_next_recirc--83271c4675fa----0---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

## [How I Made Claude Code Agents Coordinate 100% and Solved Context Amnesia ### Claude Code coordinating multiple agents to implement fixes from my code audit](https://medium.com/@ilyas.ibrahim/how-i-made-claude-code-agents-coordinate-100-and-solved-context-amnesia-5938890ea825?source=post_page---read_next_recirc--83271c4675fa----0---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

Nov 16, 2025

[134 3](https://medium.com/@ilyas.ibrahim/how-i-made-claude-code-agents-coordinate-100-and-solved-context-amnesia-5938890ea825?source=post_page---read_next_recirc--83271c4675fa----0---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=---read_next_recirc--83271c4675fa----0-----------------explicit_signal----1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F5938890ea825&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ilyas.ibrahim%2Fhow-i-made-claude-code-agents-coordinate-100-and-solved-context-amnesia-5938890ea825&source=---read_next_recirc--83271c4675fa----0-----------------bookmark_preview----1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

![Image 17: How to Write Product Specs in 2025 (Spoiler: It Takes 10 Minutes Now)](https://miro.medium.com/v2/resize:fit:679/format:webp/1*aDSvlBbpfLO4w45gzCIBKw.jpeg)

[![Image 18: Lucas Didier](https://miro.medium.com/v2/resize:fill:20:20/2*n5CLaVVNnQ6V8MVT_xT2PQ.jpeg)](https://medium.com/@lucdid?source=post_page---read_next_recirc--83271c4675fa----1---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[Lucas Didier](https://medium.com/@lucdid?source=post_page---read_next_recirc--83271c4675fa----1---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

## [How to Write Product Specs in 2025 (Spoiler: It Takes 10 Minutes Now) ### There’s a particular kind of irony that only product managers truly appreciate: I used to spend hours writing specifications about features…](https://medium.com/@lucdid/how-to-write-product-specs-in-2025-spoiler-it-takes-10-minutes-now-d249c43a7c95?source=post_page---read_next_recirc--83271c4675fa----1---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

Dec 10, 2025

[6 2](https://medium.com/@lucdid/how-to-write-product-specs-in-2025-spoiler-it-takes-10-minutes-now-d249c43a7c95?source=post_page---read_next_recirc--83271c4675fa----1---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=---read_next_recirc--83271c4675fa----1-----------------explicit_signal----1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd249c43a7c95&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40lucdid%2Fhow-to-write-product-specs-in-2025-spoiler-it-takes-10-minutes-now-d249c43a7c95&source=---read_next_recirc--83271c4675fa----1-----------------bookmark_preview----1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

![Image 19: Claude Design vs designers](https://miro.medium.com/v2/resize:fit:679/format:webp/1*uEpYU8djlQk1vA5DhHIQ8A.png)

[![Image 20: Michal Malewicz](https://miro.medium.com/v2/resize:fill:20:20/1*149zXrb2FXvS_mctL4NKSg.png)](https://medium.com/@michalmalewicz?source=post_page---read_next_recirc--83271c4675fa----2---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[Michal Malewicz](https://medium.com/@michalmalewicz?source=post_page---read_next_recirc--83271c4675fa----2---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

## [Will Claude Design replace designers? ### It’s complicated, but very simple.](https://medium.com/@michalmalewicz/will-claude-design-replace-designers-f92623f3befe?source=post_page---read_next_recirc--83271c4675fa----2---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

Apr 17

[2.2K 68](https://medium.com/@michalmalewicz/will-claude-design-replace-designers-f92623f3befe?source=post_page---read_next_recirc--83271c4675fa----2---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=---read_next_recirc--83271c4675fa----2-----------------explicit_signal----1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff92623f3befe&operation=register&redirect=https%3A%2F%2Fmichalmalewicz.medium.com%2Fwill-claude-design-replace-designers-f92623f3befe&source=---read_next_recirc--83271c4675fa----2-----------------bookmark_preview----1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

![Image 21: A Practical Development Guide Based on OpenSpec + Claude CLI](https://miro.medium.com/v2/resize:fit:679/format:webp/7280ed8cf2fe1568aa4891c4276068a914da03949aa4a328b4fd77614007fdbb)

[![Image 22: HBLOG](https://miro.medium.com/v2/resize:fill:20:20/0*UF50ZLx1zFUgmdYR)](https://medium.com/@jxausea?source=post_page---read_next_recirc--83271c4675fa----3---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[HBLOG](https://medium.com/@jxausea?source=post_page---read_next_recirc--83271c4675fa----3---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

## [A Practical Development Guide Based on OpenSpec + Claude CLI ### I. Why do we need new ways of developing AI?](https://medium.com/@jxausea/a-practical-development-guide-based-on-openspec-claude-cli-26da7df71356?source=post_page---read_next_recirc--83271c4675fa----3---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

Dec 17, 2025

[64 1](https://medium.com/@jxausea/a-practical-development-guide-based-on-openspec-claude-cli-26da7df71356?source=post_page---read_next_recirc--83271c4675fa----3---------------------1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40codecentrevibe%2Fclaude-code-multi-agent-parallel-coding-83271c4675fa&source=---read_next_recirc--83271c4675fa----3-----------------explicit_signal----1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F26da7df71356&operation=register&redirect=https%3A%2F%2Fjxausea.medium.com%2Fa-practical-development-guide-based-on-openspec-claude-cli-26da7df71356&source=---read_next_recirc--83271c4675fa----3-----------------bookmark_preview----1a54dfa1_143b_41ae_8664_f3517370fed4--------------)

[See more recommendations](https://medium.com/?source=post_page---read_next_recirc--83271c4675fa---------------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----83271c4675fa---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----83271c4675fa---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----83271c4675fa---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----83271c4675fa---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----83271c4675fa---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----83271c4675fa---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----83271c4675fa---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----83271c4675fa---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----83271c4675fa---------------------------------------)
