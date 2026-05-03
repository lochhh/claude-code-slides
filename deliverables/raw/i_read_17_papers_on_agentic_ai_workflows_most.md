# I read 17 papers on agentic AI workflows. Most Claude Code advice ...

**Type:** community
**URL:** https://www.reddit.com/r/ClaudeAI/comments/1s8mbqm/i_read_17_papers_on_agentic_ai_workflows_most/
**Topic:** Plan Mode & Agentic Workflows
**Published:** unknown

## Content

# I read 17 papers on agentic AI workflows. Most Claude Code advice is measurably wrong : r/ClaudeAI
[Skip to main content](https://www.reddit.com/r/ClaudeAI/comments/1s8mbqm/i_read_17_papers_on_agentic_ai_workflows_most/#main-content)I read 17 papers on agentic AI workflows. Most Claude Code advice is measurably wrong : r/ClaudeAI

Open menu Open navigation[](https://www.reddit.com/)Go to Reddit Home

r/ClaudeAI

Get App Get the Reddit app [Log In](https://www.reddit.com/login/)Log in to Reddit

Expand user menu Open settings menu

[![Image 1](https://styles.redditmedia.com/t5_7t8hvt/styles/communityIcon_97yk0vsmp4cf1.png?width=96&height=96&frame=1&auto=webp&crop=96%3A96%2Csmart&s=de73db6eb89604488f2125b81c2080f7a14c2a38) Go to ClaudeAI](https://www.reddit.com/r/ClaudeAI/)

[r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/)•10d ago

[jdforsythe](https://www.reddit.com/user/jdforsythe/)

# I read 17 papers on agentic AI workflows. Most Claude Code advice is measurably wrong

[Other](https://www.reddit.com/r/ClaudeAI/?f=flair_name%3A%22Other%22)

I lead a small engineering team doing a greenfield SaaS rewrite. I've been testing agentic coding but could never get reliable enough output to integrate it into our workflow. I spent months building agent pipelines that worked great in demos and fell apart in production.

When I finally read the actual research, I found out why:

*   Telling Claude "you are the world's best programmer" **degrades** output quality. PRISM persona research shows flattery activates motivational and marketing text in the training distribution instead of technical expertise. Brief identities under 50 tokens outperform elaborate persona descriptions.

*   At 19 requirements in a system prompt, accuracy is **lower** than at 5. More instructions isn't better - it's measurably worse.

*   A 5-agent team costs 7x the tokens of a single agent but produces only 3.1x the output (DeepMind, 2025). At 7+ agents, you're likely getting **less** output than a team of 4.

*   If a single well-prompted agent achieves >45% of optimal performance on a task, adding more agents yields diminishing returns. Always start with one. Measure. Escalate only when the data justifies it.

*   Rubber-stamp approval is the single most frequently observed quality failure in multi-agent systems (MAST FM-3.1). Your review agent says "LGTM" to everything because agreement is the path of least resistance in the training distribution.

*   When critical information is placed in the middle of long context (rather than beginning or end), accuracy drops by >30% (Liu et al., 2024). MIT traced this to architectural causes in the transformer itself.

I distilled 17 papers into 10 actionable principles and wrote them up as an article series (linked below). The series is live now.

I also built two open-source tools that encode the principles:

**Forge** - science-backed agent team assembly ([https://github.com/jdforsythe/forge](https://github.com/jdforsythe/forge)). Vocabulary routing, PRISM identities, the 45% threshold, all encoded into a Claude Code plugin.

**jig** - selective context loading for Claude Code ([https://github.com/jdforsythe/jig](https://github.com/jdforsythe/jig)). Define profiles with specific tools per session. Load only what you need so your context stays clean.

Article series: [https://jdforsythe.github.io/10-principles](https://jdforsythe.github.io/10-principles)

Happy to answer questions about any of the research or the tools.

 Share 

New to Reddit? 
Create your account and connect with a world of communities.

 Continue with Email 

 Continue With Phone Number 

By continuing, you agree to our[User Agreement](https://www.redditinc.com/policies/user-agreement)and acknowledge that you understand the[Privacy Policy](https://www.redditinc.com/policies/privacy-policy). 

# Related Answers Section

 Related Answers 

[Overview of Claude AI and agentic workflows](https://www.reddit.com/answers/d7a3c9c5-b9c8-4ce7-9a3d-abfe26f5ebff/?q=Overview+of+Claude+AI+and+agentic+workflows&source=PDP)

[Best practices for agentic coding](https://www.reddit.com/answers/a2157881-8b9c-42cf-a06f-f9ff4c2beb81/?q=Best+practices+for+agentic+coding&source=PDP)

[Comparison of Claude AI and Devin CLI](https://www.reddit.com/answers/e2e07208-1a4b-483b-9d43-b9c35f68382a/?q=Comparison+of+Claude+AI+and+Devin+CLI&source=PDP)

[Features of Claude's agentic coding tools](https://www.reddit.com/answers/6bf0a6f3-8635-49eb-af8d-7d4155608986/?q=Features+of+Claude%27s+agentic+coding+tools&source=PDP)

[Agentic AI coding challenges and solutions](https://www.reddit.com/answers/057f596f-da89-4fba-8a74-6bd26a7f0160/?q=Agentic+AI+coding+challenges+and+solutions&source=PDP)

![Image 2: hp](https://emoji.redditmedia.com/jud91dthlhcf1_t5_7t8hvt/hp)

![Image 3: hp](https://emoji.redditmedia.com/jud91dthlhcf1_t5_7t8hvt/hp)

[Check Claude service status.](http://status.claude.com/)

 Public 

Anyone can view, post, and comment to this community

0 0

[Reddit Rules](https://www.redditinc.com/policies/content-policy)[Privacy Policy](https://www.reddit.com/policies/privacy-policy)[User Agreement](https://www.redditinc.com/policies/user-agreement)[Your Privacy Choices](https://support.reddithelp.com/hc/articles/43980704794004)[Accessibility](https://support.reddithelp.com/hc/sections/38303584022676-Accessibility)[Reddit, Inc. © 2026. All rights reserved.](https://redditinc.com/)

Expand Navigation Collapse Navigation

*   &nbsp; 
*   &nbsp; 
*   &nbsp; 

* * *

* * *

*   RESOURCES 

*   [About Reddit](https://www.redditinc.com/)
*   [Advertise](https://ads.reddit.com/register?utm_source=web3x_consumer&utm_name=left_nav_cta)
*   [Developer Platform](https://developers.reddit.com/?utm_source=reddit&utm_medium=left_nav_resources)
*   [Reddit Pro BETA](https://www.reddit.com/reddit-pro?utm_source=reddit&utm_medium=left_nav_resources)
*   [Help](https://support.reddithelp.com/hc?utm_source=reddit&utm_medium=footer&utm_campaign=evergreen)
*   [Blog](https://redditblog.com/)
*   [Careers](https://www.redditinc.com/careers)
*   [Press](https://www.redditinc.com/press)

* * *

*   [Best of Reddit](https://www.reddit.com/posts/2026/global/)

* * *

*   [Reddit Rules](https://www.redditinc.com/policies/content-policy)
*   [Privacy Policy](https://www.reddit.com/policies/privacy-policy)
*   [User Agreement](https://www.redditinc.com/policies/user-agreement)
*   [Your Privacy Choices](https://support.reddithelp.com/hc/articles/43980704794004)
*   [Accessibility](https://support.reddithelp.com/hc/sections/38303584022676-Accessibility)

[Reddit, Inc. © 2026. All rights reserved.](https://redditinc.com/)

![Image 4](https://id.rlcdn.com/472486.gif)
