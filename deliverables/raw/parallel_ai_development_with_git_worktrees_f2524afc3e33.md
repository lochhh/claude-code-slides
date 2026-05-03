# Parallel Development with ClaudeCode and Git Worktrees | by Yee Fei

**Type:** article
**URL:** https://medium.com/@ooi_yee_fei/parallel-ai-development-with-git-worktrees-f2524afc3e33
**Topic:** Git Worktrees
**Published:** unknown

## Content

# Parallel Development with ClaudeCode and Git Worktrees | by Yee Fei | Medium

[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40ooi_yee_fei%2Fparallel-ai-development-with-git-worktrees-f2524afc3e33&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40ooi_yee_fei%2Fparallel-ai-development-with-git-worktrees-f2524afc3e33&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Image 1](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Press enter or click to view image in full size

![Image 2](https://miro.medium.com/v2/resize:fit:700/1*PtVSdhmd8XGmBCKHJF6msg.png)

# Parallel Development with ClaudeCode and Git Worktrees

[![Image 3: Yee Fei](https://miro.medium.com/v2/resize:fill:32:32/1*HO3S8PKbbi7FY-cLk9nlbQ.png)](https://medium.com/@ooi_yee_fei?source=post_page---byline--f2524afc3e33---------------------------------------)

[Yee Fei](https://medium.com/@ooi_yee_fei?source=post_page---byline--f2524afc3e33---------------------------------------)

Follow

6 min read

·

Aug 17, 2025

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Ff2524afc3e33&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ooi_yee_fei%2Fparallel-ai-development-with-git-worktrees-f2524afc3e33&user=Yee+Fei&userId=6a41a10003b2&source=---header_actions--f2524afc3e33---------------------clap_footer------------------)

55

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff2524afc3e33&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ooi_yee_fei%2Fparallel-ai-development-with-git-worktrees-f2524afc3e33&source=---header_actions--f2524afc3e33---------------------bookmark_footer------------------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Df2524afc3e33&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ooi_yee_fei%2Fparallel-ai-development-with-git-worktrees-f2524afc3e33&source=---header_actions--f2524afc3e33---------------------post_audio_button------------------)

Share

My dev workflow with Claude Code has become a lot more flexible. It’s no longer about a single agent working on one thing at a time. It’s about orchestrating a team of agents across multiple tasks simultaneously. The key to making this work? Git worktrees.

I’m using GitHub for my project, so a big part of my learning journey is figuring out how to achieve best-practice SDLC with this new way of development and Git. A lot of that comes down to a simple idea: maximizing parallel development.

## The Challenge: A Project with Parallel Paths

Some of my projects have bugs/refactoring/new feature development plans, with both dependent and independent tasks. Waiting for one to finish before starting the next would have been too slow. I needed a way to accelerate velocity without creating chaos.

### The Solution: Git Worktrees

What is Git Worktree?

Git worktrees allow you to manage multiple development efforts from a single repository. It creates an entirely new working directory for a branch, giving you a fresh, isolated workspace without having to re-clone the entire project. This frees you up to jump between different tasks without worrying about one set of changes bleeding into another. No more `git stash` headaches, just clean, uninterrupted focus.

The main benefit is also peace of mind. I can experiment on a new feature without worrying that my files will get messed up. It’s much cleaner than trying to manage everything in a single branch and a single folder.

### Parallelism: My Experience

I was excited about the idea of parallel workstreams, but I learned it’s not a silver bullet. Sometimes, what seems like a great parallel task can end up causing merge conflicts that take more time to resolve than the original task.

My new process has become more intentional:

*   **Plan First**: I (I asked Claude because they are way better than me :) ) analyze the project to find components with the lowest possibility of overlapping.
*   **Assess Risks**: I’ve also started asking Claude to help (sometimes leveraging Zen MCP and Gemini to ‘discuss’ from different perspectives) to assess the risk of a new parallel stream. It helps me decide if a task is truly independent or if it should be done sequentially.
*   **Expect the Unexpected**: I now know to expect potential conflicts. This happened to me recently, which was a big learning moment. I had one stream that created new *-enhanced files and left the old ones untouched. It felt like I was creating a “parallel universe” inside my codebase. That was a big red flag. No matter how matured a model gets to, or how ‘perfect’ you think your system has been, always make sure you are the one who steers, don’t let them steer your project astray.

After identifying and deciding on the parallel workflow I want to work on, we can set up with Git worktree.

Here’s an example of how I use Git worktrees with Claude Code. Let’s say I’m tackling three different tasks:

*   A major refactor for authentication.
*   Building a new AI chat feature.
*   Fixing a high-priority bug.

Instead of jumping between branches and losing context, I create three separate worktrees, each dedicated to a specific task.

### Directory Structure

Git worktrees create a clean, organized directory structure. The new worktree folders are created outside the parent directory but are still linked to the original `.git` folder.

/projects/

├── my-project-folder/

│ └── .git/ # The actual Git repository data

│

├── auth-refactor/

│ └── .git # A text file linking to the real .git

│

├── ai-chat-feature/

│ └── .git # Another link to the real .git

│

└── bug-fix-patch/

 └── .git # And another link…
### Commands & Steps

Here’s the sequence of commands I use to set up a new worktree

*   Set up the main branch: Always start by ensuring your main branch is up-to-date.

git checkout main

git pull origin main
Create a new worktree and branch: I create a new worktree and a new branch simultaneously. This command creates a new directory, checks out a new branch, and isolates the work all at once.

# For authentication refactor

git worktree add -b feat/auth-refactor ../auth-refactor

# For AI chat feature

git worktree add -b feat/ai-chat ../ai-chat

#For bug fix

git worktree add -b fix/bug-patch ../bug-patch
Manage and Remove worktrees: When a task is complete and merged, I clean up the worktree. I can run these commands from any branch in the repository.

git worktree remove ../my-new-feature

git branch -d feat/my-new-feature #to delete the local branch

git push origin --delete feat/my-new-feature #to delete the remote branch

git worktree list #to verify all worktrees are cleaned up
This process ensures I don’t leave behind a cluttered project.

### Conflict Management

Even with a structured workflow, conflicts can happen. This is where I’ve started leveraging Claude to help analyze and manage potential conflicts. I’ll provide a high-level overview of open issues and ask Claude to analyze them for conflict potential.

## Get Yee Fei’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

- [x] 

Remember me for faster sign in

 

Here’s an example of the kind of analysis Claude provides if you prompt it to help you:

Based on the provided issues, Claude identified two workstreams with minimal overlap.

*   Stream A — Low Conflict (Database & Backend): Issues related to database indexes (#20), query refactoring (#19), and resolving N+1 queries (#21). These are largely backend tasks that affect data retrieval, but not necessarily frontend components or authentication.
*   Stream B — Medium Conflict (Data Layer): Issues like installing a data fetching library (#16) and creating new data hooks (#17, #18). This stream has medium conflict potential because it interacts with the database layer (Stream A) but primarily affects frontend data handling.

This analysis helps me make informed decisions about what I can work on in parallel.

(I’ve tested with more, but I ended up realising my own brain is the bottleneck, it doesn’t do good to my sanity :’) )

## The “Rebase Before PR” Model

Using Git worktrees works best with a clear branching strategy. My core principle is the “Rebase Before PR” model. This ensures my work is always built on top of the most recent code, which keeps the project history clean and minimizes merge headaches.

Rule of thumb (for my forgetful brain)

*   Start: Always branch new features from an up-to-date main.
*   Work: Work in isolated feature branches and worktrees.
*   Finish: Before you create any Pull Request to staging, always run git fetch origin and git rebase origin/main.
*   Push: After rebasing, push with git push — force-with-lease.
*   Merge: PR to staging for testing, then staging to main for production.
*   Clean: Delete your worktree and branch after it’s merged to main.

### My Key Learnings from Parallel Development

While parallelism is exciting, I’ve learned a few hard lessons.

*   Parallelism is a double-edged sword. While it feels productive, the conflicts you have to resolve can sometimes take up more time than if you had worked on the tasks sequentially. For critical, major refactors, it’s often better to stick with a planned, sequential approach.
*   After completing a checkpoint, I make it a habit to pull and merge updates from the main branch. This prevents my worktree from drifting too far from the main codebase, which would otherwise result in massive, hard-to-resolve conflicts down the road.

I’ve also started using Claude to automate many parts of my Git workflow. For example, I now instruct it to always handle the rebase before pull model for me, and even tell it to prioritize changes from a more important branch if a conflict occurs. Automating these Git changes and pushes with GitHub issues has been a game-changer for keeping my dev tasks structured. More on these next time.

Video version of what’s being discussed in this blog:

[Claude](https://medium.com/tag/claude?source=post_page-----f2524afc3e33---------------------------------------)

[Claude Code](https://medium.com/tag/claude-code?source=post_page-----f2524afc3e33---------------------------------------)

[Git](https://medium.com/tag/git?source=post_page-----f2524afc3e33---------------------------------------)

[Anthropic Claude](https://medium.com/tag/anthropic-claude?source=post_page-----f2524afc3e33---------------------------------------)

[Agentic Ai](https://medium.com/tag/agentic-ai?source=post_page-----f2524afc3e33---------------------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Ff2524afc3e33&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ooi_yee_fei%2Fparallel-ai-development-with-git-worktrees-f2524afc3e33&user=Yee+Fei&userId=6a41a10003b2&source=---footer_actions--f2524afc3e33---------------------clap_footer------------------)

55

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Ff2524afc3e33&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ooi_yee_fei%2Fparallel-ai-development-with-git-worktrees-f2524afc3e33&user=Yee+Fei&userId=6a41a10003b2&source=---footer_actions--f2524afc3e33---------------------clap_footer------------------)

55

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff2524afc3e33&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ooi_yee_fei%2Fparallel-ai-development-with-git-worktrees-f2524afc3e33&source=---footer_actions--f2524afc3e33---------------------bookmark_footer------------------)

[![Image 4: Yee Fei](https://miro.medium.com/v2/resize:fill:48:48/1*HO3S8PKbbi7FY-cLk9nlbQ.png)](https://medium.com/@ooi_yee_fei?source=post_page---post_author_info--f2524afc3e33---------------------------------------)

[![Image 5: Yee Fei](https://miro.medium.com/v2/resize:fill:64:64/1*HO3S8PKbbi7FY-cLk9nlbQ.png)](https://medium.com/@ooi_yee_fei?source=post_page---post_author_info--f2524afc3e33---------------------------------------)

Follow

## [Written by Yee Fei](https://medium.com/@ooi_yee_fei?source=post_page---post_author_info--f2524afc3e33---------------------------------------)

[176 followers](https://medium.com/@ooi_yee_fei/followers?source=post_page---post_author_info--f2524afc3e33---------------------------------------)

·[8 following](https://medium.com/@ooi_yee_fei/following?source=post_page---post_author_info--f2524afc3e33---------------------------------------)

[https://www.linkedin.com/in/yeefei](https://www.linkedin.com/in/yeefei)

Follow

## No responses yet

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--f2524afc3e33---------------------------------------)

![Image 6](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ooi_yee_fei%2Fparallel-ai-development-with-git-worktrees-f2524afc3e33&source=---post_responses--f2524afc3e33---------------------respond_sidebar------------------)

Cancel

Respond

[Help](https://help.medium.com/hc/en-us?source=post_page-----f2524afc3e33---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----f2524afc3e33---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----f2524afc3e33---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----f2524afc3e33---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----f2524afc3e33---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----f2524afc3e33---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----f2524afc3e33---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----f2524afc3e33---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----f2524afc3e33---------------------------------------)
