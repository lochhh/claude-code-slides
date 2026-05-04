# claude-code-slides

I want to create a reusable research automation tool that searches the web for the most useful and practical resources on using Claude Code as a software engineer. These information should then become the master guide for software engineers.

Here's the workflow I want you to follow:

1. RESEARCH AUTOMATION: Build an automation that uses web search/scrape to find the best Youtube videos, articles, guides, GitHub repos, and community tips about getting the most out of Claude Code, covering basic to advanced usage. Example topics can include (but are not limited to) CLAUDE.md setup, context management, MCP servers, hooks, subagents, git worktrees, slash commands/skills, plan mode, prompting strategies, and productivity workflows. Save raw findings in deliverables/raw as markdown files, one per source/topic. The general assumption is that the target audience is familiar with raw prompting, e.g. they open Claude Code, describe what they want, and it builds, but they hit the ceiling where their project grows past what fits in a single conversation and the agent forgets their conventions, introduces patterns they don't use, and they spend more time correcting than building.

2. ANALYSE: Read all collected files. Identify overlapping advice, deduplicate, and cluster into 6-8 major themes. Provide a summary table with all themes (linked to the corresponding subsections within the analysis), their ranks (by source frequency, also include the frequency), usage levels (e.g. basic, novice, intermediate, advanced, expert). In the main body, organise the themes by the 5 usage levels. Within each theme, rank tips by how often they appear across sources. Save the analysis to deliverables/analysis.md.

3. SYNTHESISE: Transform the analytical output into a polished, navigable, pedagogically structured documentation set targeted at software engineers looking to master Claude Code. Create a master index page at deliverables/prod/index.md that introduces the beginner → expert learning path, usage levels, and theme overview. For each theme, create a dedicated markdown file in deliverables/prod/ that includes:

- a one‑paragraph conceptual summary
- ranked tips rewritten for clarity and consistency
- at least one concrete example per tip (commands, prompt snippets, code, CLAUDE.md excerpts)
- pitfalls, misconceptions, and "when to use this" guidance
- cross‑links to related themes

There must also be a page for References listing all sources, and individual theme pages should link to the relevant sources in the References. Ensure all files follow a consistent structure, tone, and style guide. Add a glossary, recommended reading order, and cross‑theme insights. All files should be plain GitHub-flavoured markdown with relative links between pages, no build tools required, so the deliverables/prod folder can be served via GitHub Pages as-is.

4. PRESENT: Generate a polished HackMD reveal.js slide deck called "Becoming a Pro with Claude Code Pro" targeted at software engineers based on the master guide. Aim for ~20-30 slides covering all major themes, with speaker notes for a 1-hour session.

Start with Phase 1 — research automation. Aim for at least 10 distinct sources. 
Let me know:
- if there are any skills you think will be helpful,
- if you have any questions, or
- if you have any recommendations for things I haven't considered for this automation system.