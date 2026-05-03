# Workflow 01: Research Automation

## Objective

Find 10+ high-quality sources on using Claude Code effectively for software engineers. Save raw findings to `deliverables/raw/` as markdown, one file per source.

## Prerequisite Setup

1. Ensure `.env` exists with:
   - `ANTHROPIC_API_KEY=<your-key>` (used for analyse/synthesise/slides phases)
   - `TAVILY_API_KEY=<your-key>` (used for web search in this phase)
2. Run `uv sync` to install dependencies
3. Ensure `yt-dlp` is available: `uv run yt-dlp --version`

## Target Audience Context

Engineers already using Claude Code for basic prompting who hit the ceiling: project grows past single conversation, agent forgets conventions, introduces wrong patterns, user spends more time correcting than building. Content should be intermediate-to-advanced, not beginner.

## Topics to Research (12)

| # | Topic | Search Query |
|---|-------|-------------|
| 1 | CLAUDE.md setup | `"CLAUDE.md setup Claude Code best practices"` |
| 2 | Context management | `"Claude Code context management compaction tips"` |
| 3 | MCP servers | `"Claude Code MCP servers setup recommended"` |
| 4 | Hooks | `"Claude Code hooks pre-tool post-tool session"` |
| 5 | Subagents | `"Claude Code subagents parallel execution multi-agent"` |
| 6 | Git worktrees | `"Claude Code git worktrees workflow"` |
| 7 | Slash commands / skills | `"Claude Code slash commands custom skills"` |
| 8 | Plan mode | `"Claude Code plan mode agentic workflow"` |
| 9 | Prompting strategies | `"Claude Code prompting strategies best practices engineer"` |
| 10 | Productivity workflows | `"Claude Code productivity keyboard shortcuts workflow tips"` |
| 11 | IDE integrations | `"Claude Code VS Code JetBrains IDE extension"` |
| 12 | Cost management | `"Claude Code token cost management efficiency"` |

## Per-Topic Steps

For each topic in order:

1. **Check skip condition:** if `deliverables/raw/<topic_slug>_sources.md` already exists, skip to next topic
2. **Search:** `uv run python tools/search_web.py "<search query>" --topic "<topic name>"`
3. **Read output:** open the generated `_sources.md` file, get the URL list
4. **Fetch top 3–5 sources** per topic:
   - YouTube URL → `uv run python tools/fetch_youtube.py "<url>"`
   - All others → `uv run python tools/fetch_page.py "<url>"`
5. **Verify output:** confirm the `.md` file in `deliverables/raw/` has >200 words

## Quality Signals

**Prefer:**
- Official Anthropic docs (`docs.anthropic.com`)
- GitHub repos with >100 stars (e.g. `awesome-claude-code`)
- Blog posts from engineers with hands-on Claude Code experience (concrete commands, config examples)
- Reddit `r/ClaudeAI` or `r/aicoding` threads with >50 upvotes
- Hacker News discussions with >50 points
- YouTube tutorials with >1 000 views from practitioners
- Content dated 2024 or later

**Skip:**
- Generic AI hype articles with no concrete tips
- Pure beginner "how to install" content
- Marketing copy / press releases
- Paywalled content (unless a substantial free portion exists)
- Content with no commands, examples, or config snippets

## Output Format for Raw Files

Each `deliverables/raw/<slug>.md` should contain:

```markdown
# <Source Title>

**Type:** article | video | repo | community | docs
**URL:** <url>
**Topic:** <one of the 12 topics above>
**Date:** <publication/upload date if known>

## Content

<cleaned text / transcript — minimum 200 words>
```

## Completion Criteria

- [ ] At least 10 distinct source files in `deliverables/raw/`
- [ ] Each file has >200 words of substantive content
- [ ] Sources cover at least 8 of the 12 topics
- [ ] No duplicate URLs across files
- [ ] All files follow the output format above

## Error Handling

| Error | Action |
|-------|--------|
| Tavily API rate limit | Wait 30s and retry; Tavily free tier allows ~100 searches/month |
| Page fetch timeout | Skip the URL, move to next source in list |
| yt-dlp transcript not available | Save metadata-only file (title, description, URL) |
| yt-dlp not found | Install: `pip install yt-dlp` or `uv add yt-dlp` |
| BeautifulSoup extracts empty content | Try `fetch_page.py` with `--raw` flag (falls back to raw text) |

## Lessons Learned

_Update this section as you encounter quirks during execution._
