# My Top 10 Claude Code Tips from 11 Months of Intense Usage

**Type:** community
**URL:** https://www.reddit.com/r/ClaudeAI/comments/1qcan9z/my_top_10_claude_code_tips_from_11_months_of/
**Topic:** Productivity & Keyboard Shortcuts
**Published:** unknown

## Content

# My Top 10 Claude Code Tips from 11 Months of Intense Usage : r/ClaudeAI
[Skip to main content](https://www.reddit.com/r/ClaudeAI/comments/1qcan9z/my_top_10_claude_code_tips_from_11_months_of/#main-content)My Top 10 Claude Code Tips from 11 Months of Intense Usage : r/ClaudeAI

Open menu Open navigation[](https://www.reddit.com/)Go to Reddit Home

r/ClaudeAI

Get App Get the Reddit app [Log In](https://www.reddit.com/login/)Log in to Reddit

Expand user menu Open settings menu

[![Image 1](https://styles.redditmedia.com/t5_7t8hvt/styles/communityIcon_97yk0vsmp4cf1.png?width=96&height=96&frame=1&auto=webp&crop=96%3A96%2Csmart&s=de73db6eb89604488f2125b81c2080f7a14c2a38) Go to ClaudeAI](https://www.reddit.com/r/ClaudeAI/)

[r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/)•3mo ago

[yksugi](https://www.reddit.com/user/yksugi/)

# My Top 10 Claude Code Tips from 11 Months of Intense Usage

[Productivity](https://www.reddit.com/r/ClaudeAI/?f=flair_name%3A%22Productivity%22)

I've been using Claude Code intensely over the past 11 months since its launch, and I've even compiled [a list of 40+ tips](https://github.com/ykdojo/claude-code-tips).

Here, I wanted to share what I think are the 10 most important ones to get you started on this journey.

# 1. Minimize the provided context

The longer the given context, the worse it performs. So make sure to learn different ways of minimizing the provided context.

The simple one to get started with is starting a fresh conversation whenever you start a new topic.

Another quick one is:

*   In the first conversation, find which files you need to edit to solve your problem

*   In the second, fresh conversation, figure out how to edit them exactly

Remember, AI context is like milk; it's best served fresh and condensed.

# 2. Solve a problem step by step

Claude models tend to be pretty good at long-lasting tasks, but they're not perfect.

Sometimes they make mistakes and they mess up things especially when it's given a problem that's too large.

So in that case, just break your problem down into smaller steps. And if they're still too big for Claude to solve in one shot, then break them down further.

# 3. Don't always jump into writing code

AI gets a bad rep for low quality code because a lot of people just primarily use it for writing code.

But understand that it's great for understanding a codebase, doing research, brainstorming, architectural discussions, etc.

Doing enough preparation before jumping into writing code is one of the essential keys for producing high quality code.

# 4. Learn to use Git and GitHub well

Just ask Claude to handle your Git and GitHub CLI tasks. This includes committing (so you don't have to write commit messages manually), branching, pulling, and pushing.

I personally allow pull automatically but not push, because push is riskier.

You can even let it run `git bisect` to find the exact commit that broke something. It'll need a way to test each commit, so you might need to give it a test script.

# 5. Learn to check the output of AI in different ways

One way to verify its output if it's code is to have it write tests.

Another thing is you can use a visual Git client like GitHub Desktop for example. I personally use it. It's not a perfect product, but it's good enough for checking changes quickly.

Having it generate a draft PR is a great way as well. You can review everything before marking it ready for review.

# 6. Learn to let AI verify its own code and other output

You can let it check itself, its own work. If it gives you some sort of output, let's say from some research, you can say "are you sure about this? Can you double check?"

One of my favorite prompts is to say "double check everything, every single claim in what you produced and at the end make a table of what you were able to verify." That seems to work really well.

If you're building a web app, you can use Playwright MCP or Claude's native browser integration (through `/chrome`) to let it verify that everything works correctly.

For Claude for Chrome, I recommend adding this to your CLAUDE.md so it uses accessibility tree refs instead of coordinates (better for speed and accuracy):

# Claude for Chrome

- Use `read_page` to get element refs from the accessibility tree
- Use `find` to locate elements by description
- Click/interact using `ref`, not coordinates
- NEVER take screenshots unless explicitly requested by the user
For interactive CLIs, you can use tmux. The pattern is: start a tmux session, send commands to it, capture the output, and verify it's what you expect.

# 7. Set up a custom status line

You can customize the status line at the bottom of Claude Code. [I set mine up](https://github.com/ykdojo/claude-code-tips?tab=readme-ov-file#tip-0-customize-your-status-line) to show the model, current directory, git branch, uncommitted file count, sync status with origin, and a visual progress bar for token usage.

It's really helpful for keeping an eye on your context usage and remembering what you were working on.

# 8. Learn how to pass context to the next session

There's a `/compact` command in Claude Code that summarizes your conversation to free up context space. But I found that it's better to proactively manage context yourself.

The way I do this is to ask Claude to write a handoff document before starting fresh. Something like: "Put the rest of the plan in HANDOFF.md. Explain what you have tried, what worked, what didn't work, so that the next agent with fresh context is able to just load that file and nothing else to get started on this task and finish it up."

Then you start a fresh conversation and give it just the path of that file, and it should work just fine.

I also created a [half-clone command](https://github.com/ykdojo/claude-code-tips?tab=readme-ov-file#half-clone-to-reduce-context) that clones the current conversation but keeps only the later half. It's a quick way to reduce context while preserving your recent work.

# 9. Learn to use voice input well

I found that you can communicate much faster with your voice than typing with your hands. Using a voice transcription system on your local machine is really helpful for this.

On my Mac, I've tried a few different options like superwhisper, MacWhisper, and [Super Voice Assistant](https://github.com/ykdojo/super-voice-assistant). Even when there are mistakes or typos in the transcription, Claude is smart enough to understand what you're trying to say.

I think the best way to think about this is like you're trying to communicate with your friend. If you want to communicate faster, why wouldn't you get on a quick phone call? You can just send voice messages. It's faster, at least for me. For a majority of people, it's going to be faster too.

# 10. Learn to juggle a few sessions at the same time

When you're running multiple Claude Code instances, staying organized matters more than any specific technical setup. I'd say focus on at most three or four tasks at a time, at least at the beginning.

My personal method is what I call a "cascade." Whenever I start a new task, I just open a new tab on the right. Then I sweep left to right, left to right, going from oldest tasks to newest. The general direction stays consistent, except when I need to check on certain tasks.

# 11. (Bonus) Alias 'claude' to 'c'

Since I use the terminal more because of Claude Code, I found it helpful to set up short aliases so I can launch things quickly. The one I use the most is `c` for Claude Code.

To set it up, add this line to your shell config file (`~/.zshrc` or `~/.bashrc`):

alias c='claude'
Once you have this alias, you can combine it with flags: `c -c` continues your last conversation, and `c -r` shows a list of recent conversations to resume.

 Share 

New to Reddit? 
Create your account and connect with a world of communities.

 Continue with Email 

 Continue With Phone Number 

By continuing, you agree to our[User Agreement](https://www.redditinc.com/policies/user-agreement)and acknowledge that you understand the[Privacy Policy](https://www.redditinc.com/policies/privacy-policy). 

# Related Answers Section

 Related Answers 

[Top Claude Code tips for effective usage](https://www.reddit.com/answers/3dbd778f-c78f-402a-b169-554c89f4cd27/?q=Top+Claude+Code+tips+for+effective+usage&source=PDP)

[Claude Code best practices recommendations](https://www.reddit.com/answers/4323a175-5132-4564-9eb2-c415f2776baa/?q=Claude+Code+best+practices+recommendations&source=PDP)

[Claude Code usage limits and checks](https://www.reddit.com/answers/17f62f25-a9fc-4fdd-9440-e0c57a3fc962/?q=Claude+Code+usage+limits+and+checks&source=PDP)

[Best use cases for ClaudeAI in business](https://www.reddit.com/answers/33a85ac0-8d5d-411d-a3ea-180d9c402890/?q=Best+use+cases+for+ClaudeAI+in+business&source=PDP)

[How ClaudeAI compares to other AI models](https://www.reddit.com/answers/29123b1a-0499-47bc-9d89-cc556af14e01/?q=How+ClaudeAI+compares+to+other+AI+models&source=PDP)

![Image 2: hp](https://emoji.redditmedia.com/jud91dthlhcf1_t5_7t8hvt/hp)![Image 3: hp](https://emoji.redditmedia.com/jud91dthlhcf1_t5_7t8hvt/hp)

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
