# claude-code-slides

I want to create a reusable research automation tool that searches the web for the most useful and practical resources on using Claude Code as a software engineer. These information should then become the master guide for software engineers.

Here's the workflow I want you to follow:

1. RESEARCH AUTOMATION: Build an automation that uses web search/scrape to find the best Youtube videos, articles, guides, GitHub repos, and community tips about getting the most out of Claude Code, covering basic to advanced usage. Example topics can include (but are not limited to) CLAUDE.md setup, context management, MCP servers, hooks, subagents, git worktrees, slash commands/skills, plan mode, prompting strategies, and productivity workflows. Save raw findings in deliverables/raw as markdown files, one per source/topic. The general assumption is that the target audience is familiar with raw prompting, e.g. they open Claude Code, describe what they want, and it builds, but they hit the ceiling where their project grows past what fits in a single conversation and the agent forgets their conventions, introduces patterns they don't use, and they spend more time correcting than building.

2. ANALYSE: Read all collected files. Identify overlapping advice, deduplicate, and cluster into 6-8 major themes. Provide a summary table with all themes (linked to the corresponding subsections within the analysis), their ranks (by source frequency, also include the frequency), usage levels (e.g. basic, novice, intermediate, advanced, expert). In the main body, organise the themes by the 5 usage levels. Within each theme, rank tips by how often they appear across sources. Save the analysis to deliverables/analysis.md.

3. SYNTHESISE: Write a clean, structured master guide to deliverables/prod/index.md as the index page. Each major theme should be its own markdown file in deliverables/prod. Every theme file must include: a one-paragraph summary, ranked tips with brief explanations, and at least one concrete example per tip (e.g. a real command, a prompt snippet, or a CLAUDE.md excerpt). All files should be plain GitHub-flavoured markdown with relative links between pages, no build tools required, so the deliverables/prod folder can be served via GitHub Pages as-is.

4. PRESENT: Generate a polished HackMD reveal.js slide deck called "Becoming a Pro with Claude Code Pro" targeted at software engineers based on the master guide. Aim for ~20-30 slides covering all major themes, with speaker notes for a 1-hour session.

Start with Phase 1 — research automation. Aim for at least 10 distinct sources. 
Let me know:
- if there are any skills you think will be helpful,
- if you have any questions, or
- if you have any recommendations for things I haven't considered for this automation system.