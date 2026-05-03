# Claude Code Best Practices: 12 Patterns Agentic Engineers Use

**Type:** article
**URL:** https://levelup.gitconnected.com/claude-code-best-practices-12-patterns-agentic-engineers-use-65264e3eb919
**Topic:** Prompting Strategies
**Published:** unknown

## Content

# Claude Code Best Practices: 12 Patterns Agentic Engineers Use | by huizhou92 | Apr, 2026 | Level Up Coding

[Sitemap](https://levelup.gitconnected.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fclaude-code-best-practices-12-patterns-agentic-engineers-use-65264e3eb919&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fclaude-code-best-practices-12-patterns-agentic-engineers-use-65264e3eb919&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Image 1](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

## [Level Up Coding](https://levelup.gitconnected.com/?source=post_page---publication_nav-5517fd7b58a6-65264e3eb919---------------------------------------)

·
Follow publication

[![Image 2: Level Up Coding](https://miro.medium.com/v2/resize:fill:76:76/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page---post_publication_sidebar-5517fd7b58a6-65264e3eb919---------------------------------------)
Coding tutorials and news. The developer homepage [gitconnected.com](http://gitconnected.com/)&&[skilled.dev](http://skilled.dev/)&&[levelup.dev](http://levelup.dev/)

Follow publication

Member-only story

## CLAUDE CODE

# Claude Code Best Practices: 12 Patterns Agentic Engineers Use

## Extracted from 69 Tips in GitHub’s #1 Trending Repo — with Input from Boris Cherny, the Engineer Who Built Claude Code at Anthropic.

[![Image 3: huizhou92](https://miro.medium.com/v2/resize:fill:64:64/1*bXNC8hwzijiKSx0TEL6lng.png)](https://medium.huizhou92.com/?source=post_page---byline--65264e3eb919---------------------------------------)

[huizhou92](https://medium.huizhou92.com/?source=post_page---byline--65264e3eb919---------------------------------------)

Follow

9 min read

·

Apr 15, 2026

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2F65264e3eb919&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fclaude-code-best-practices-12-patterns-agentic-engineers-use-65264e3eb919&user=huizhou92&userId=30f3b510c805&source=---header_actions--65264e3eb919---------------------clap_footer------------------)

361

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F65264e3eb919&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fclaude-code-best-practices-12-patterns-agentic-engineers-use-65264e3eb919&source=---header_actions--65264e3eb919---------------------bookmark_footer------------------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D65264e3eb919&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fclaude-code-best-practices-12-patterns-agentic-engineers-use-65264e3eb919&source=---header_actions--65264e3eb919---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![Image 4](https://miro.medium.com/v2/resize:fit:700/1*5W5oBUA-0UZkMt75SXJTjw.png)

generate by gemini

The third time I watched Claude delete the wrong branch, I stopped blaming the model.

The real problem was how I was using it. Every session started fresh — no structure, no constraints, no reusable configuration. I’d type a prompt, approve permissions one by one, get a result I half-wanted, then repeat. When something went wrong, I’d add another sentence to the prompt.

*   Only analyze, don’t modify files.
*   Don’t touch anything in `/cmd`.
*   Remember, we're using Go 1.22.

I was vibe coding. I didn’t have a word for it yet.

That word came from `shanraisshan/claude-code-best-practice` — a repo that hit GitHub Trending Day #1 in March 2026. Its subtitle: "from vibe coding to agentic engineering." The author had compiled 69 actionable tips across 11 categories, with input from Boris Cherny, the engineer who built Claude Code at Anthropic.

I read the whole thing. These are the 12 patterns that actually changed how I…

## Create an account to read the full story.

The author made this story available to Medium members only.

If you’re new to Medium, create a new account to read this story on us.

[Continue in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3Dregwall&source=-----65264e3eb919---------------------post_regwall------------------)

Or, continue in mobile web

[Sign up with Google](https://medium.com/m/connect/google?state=google-%7Chttps%3A%2F%2Flevelup.gitconnected.com%2Fclaude-code-best-practices-12-patterns-agentic-engineers-use-65264e3eb919%3Fsource%3D-----65264e3eb919---------------------post_regwall------------------%26skipOnboarding%3D1%7Cregister%7Cremember_me&source=-----65264e3eb919---------------------post_regwall------------------)

[Sign up with Facebook](https://medium.com/m/connect/facebook?state=facebook-%7Chttps%3A%2F%2Flevelup.gitconnected.com%2Fclaude-code-best-practices-12-patterns-agentic-engineers-use-65264e3eb919%3Fsource%3D-----65264e3eb919---------------------post_regwall------------------%26skipOnboarding%3D1%7Cregister%7Cremember_me&source=-----65264e3eb919---------------------post_regwall------------------)

Sign up with email

Already have an account? [Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fclaude-code-best-practices-12-patterns-agentic-engineers-use-65264e3eb919&source=-----65264e3eb919---------------------post_regwall------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2F65264e3eb919&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fclaude-code-best-practices-12-patterns-agentic-engineers-use-65264e3eb919&user=huizhou92&userId=30f3b510c805&source=---footer_actions--65264e3eb919---------------------clap_footer------------------)

361

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2F65264e3eb919&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fclaude-code-best-practices-12-patterns-agentic-engineers-use-65264e3eb919&user=huizhou92&userId=30f3b510c805&source=---footer_actions--65264e3eb919---------------------clap_footer------------------)

361

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F65264e3eb919&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fclaude-code-best-practices-12-patterns-agentic-engineers-use-65264e3eb919&source=---footer_actions--65264e3eb919---------------------bookmark_footer------------------)

[![Image 5: Level Up Coding](https://miro.medium.com/v2/resize:fill:96:96/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page---post_publication_info--65264e3eb919---------------------------------------)

[![Image 6: Level Up Coding](https://miro.medium.com/v2/resize:fill:128:128/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page---post_publication_info--65264e3eb919---------------------------------------)

Follow

## [Published in Level Up Coding](https://levelup.gitconnected.com/?source=post_page---post_publication_info--65264e3eb919---------------------------------------)

[325K followers](https://levelup.gitconnected.com/followers?source=post_page---post_publication_info--65264e3eb919---------------------------------------)

·[Last published 12 hours ago](https://levelup.gitconnected.com/gorilla-mux-is-dead-and-while-you-were-migrating-your-database-became-the-real-problem-912f65d77a06?source=post_page---post_publication_info--65264e3eb919---------------------------------------)

Coding tutorials and news. The developer homepage [gitconnected.com](http://gitconnected.com/)&&[skilled.dev](http://skilled.dev/)&&[levelup.dev](http://levelup.dev/)

Follow

[![Image 7: huizhou92](https://miro.medium.com/v2/resize:fill:96:96/1*bXNC8hwzijiKSx0TEL6lng.png)](https://medium.huizhou92.com/?source=post_page---post_author_info--65264e3eb919---------------------------------------)

[![Image 8: huizhou92](https://miro.medium.com/v2/resize:fill:128:128/1*bXNC8hwzijiKSx0TEL6lng.png)](https://medium.huizhou92.com/?source=post_page---post_author_info--65264e3eb919---------------------------------------)

Follow

## [Written by huizhou92](https://medium.huizhou92.com/?source=post_page---post_author_info--65264e3eb919---------------------------------------)

[2.7K followers](https://medium.huizhou92.com/followers?source=post_page---post_author_info--65264e3eb919---------------------------------------)

·[438 following](https://medium.com/@hxzhouh/following?source=post_page---post_author_info--65264e3eb919---------------------------------------)

Golang backend engineer. Specializes in cloud, data, and security. Lifelong learner. Efficiency enthusiast.

Follow

## No responses yet

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--65264e3eb919---------------------------------------)

![Image 9](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fclaude-code-best-practices-12-patterns-agentic-engineers-use-65264e3eb919&source=---post_responses--65264e3eb919---------------------respond_sidebar------------------)

Cancel

Respond

[Help](https://help.medium.com/hc/en-us?source=post_page-----65264e3eb919---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----65264e3eb919---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----65264e3eb919---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----65264e3eb919---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----65264e3eb919---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----65264e3eb919---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----65264e3eb919---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----65264e3eb919---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----65264e3eb919---------------------------------------)
