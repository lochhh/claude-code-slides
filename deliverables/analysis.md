# Analysis: Claude Code Research Findings

**Sources analysed:** 82 markdown files across 12 topics  
**Themes identified:** 8  
**Target audience:** Engineers hitting the ceiling — project grows past single conversation, agent forgets conventions, introduces wrong patterns.

---

## Summary

| Rank | Theme | Sources | Usage Level |
|------|-------|---------|-------------|
| 1 | [Parallel Development (Subagents + Git Worktrees)](#theme-8-parallel-development-subagents--git-worktrees) | 14 | Expert |
| 2 | [Productivity, IDE & Cost](#theme-1-productivity-ide--cost) | 14 | Basic |
| 3 | [Prompting Strategies](#theme-2-prompting-strategies) | 10 | Novice |
| 4 | [Hooks & Automation](#theme-7-hooks--automation) | 7 | Advanced |
| 5 | [MCP Servers](#theme-5-mcp-servers) | 7 | Intermediate |
| 6 | [Context Management](#theme-4-context-management) | 6 | Intermediate |
| 7 | [CLAUDE.md & Project Memory](#theme-3-claudemd--project-memory) | 6 | Novice |
| 8 | [Commands, Skills & Plan Mode](#theme-6-commands-skills--plan-mode) | 6 | Intermediate |

> Rank = number of dedicated source files. Usage level = when in your Claude Code journey this theme becomes relevant.

---

## Basic

---

## Theme 1: Productivity, IDE & Cost

**Summary:** The mechanics of working with Claude Code efficiently — keyboard shortcuts, IDE features, and token spend control. Small habits here compound into significant daily time savings.

### Tips (ranked by source frequency)

#### 1. Use Shift+Tab to cycle permission modes without typing
- Seen in: [14553413_claude_code_cheatsheet.md], [claude_code_commands_guide.md], [claude_code_keyboard_shortcuts.md], [claude_code_tips_best_practices.md]
- **What:** Shift+Tab cycles: `default → acceptEdits → plan`. No need to type mode names. Most productive pattern: plan first, then switch to acceptEdits for execution.
- **Example:** Start session in `plan` mode (2× Shift+Tab) → review → Shift+Tab to `acceptEdits` for hands-off execution.

#### 2. Monitor spend with `ccusage` — not just `/cost`
- Seen in: [usage_optimization.md], [claude_code_cost_optimisation.md]
- **What:** `ccusage` gives granular per-session and per-day breakdowns, live billing window view, and model-by-model analysis. Much richer than `/cost`.
- **Example:** `ccusage daily` (breakdown by day), `ccusage blocks --live` (real-time 5-hour billing window), `ccusage monthly`

#### 3. Use prompt caching to cut costs on repeated large contexts
- Seen in: [claude_code_cost_optimisation.md], [claude_code_token_optimization.md], [10_tip_to_stop_burning_your_tokens_in_claude_code_4776d4ac89.md]
- **What:** The same large context (CLAUDE.md, architecture docs) referenced across requests is cached at ~90% discount after first use. CLAUDE.md is re-read every session — this compounds fast.
- **Example:** A 2K-token CLAUDE.md loaded in 100 sessions/month = 200K tokens vs. 20K tokens with caching = $5.40 saved/month on Sonnet alone.

#### 4. Default to Sonnet; drop to Haiku for reviews/tests; use Opus sparingly
- Seen in: [claude_code_cost_optimisation.md], [claude_code_token_limits_cost_optimization_apac_teams.md], [claude_code_best_practices_12_patterns_agentic_engineers_use.md], [usage_optimization.md]
- **What:** Haiku is ~70% cheaper than Sonnet and sufficient for code review, test generation, linting. Sonnet handles most implementation. Opus for complex architecture only.
- **Example:** `claude --model claude-haiku-4-5 "Review this PR for obvious bugs"` vs. `claude "Design the caching architecture"`

#### 5. Use the VS Code / JetBrains extensions for inline diffs and visual plan review
- Seen in: [2025_08_05_claude_code_part_7_ide_integration_vscode_jetbrai.md], [ide_plugins_claude_code.md], [claude_code_ide.md], [ide_integration.md]
- **What:** The IDE extensions surface plan review and diffs inside the editor. Approve individual file changes without touching the terminal.
- **Example:** Install "Claude Code" in VS Code → changes appear as diffs inline → approve/reject per file.

#### 6. Reference specific line ranges with `@filename#5-10` syntax
- Seen in: [2025_08_05_claude_code_part_7_ide_integration_vscode_jetbrai.md], [ide_integration.md], [claude_code_tips_best_practices.md]
- **What:** Narrow file references reduce tokens spent on irrelevant context. Select code in editor and press Alt+K to auto-insert the reference.
- **Example:** `@src/auth/middleware.ts#42-67 "Why does this token validation sometimes fail on refresh tokens?"`

#### 7. Set up custom keybindings for common operations
- Seen in: [keybindings.md], [claude_code_keyboard_shortcuts.md], [claude_code_commands_guide.md]
- **What:** Claude Code exposes keybindings.json for rebinding any action. Common high-value bindings: `acceptAll`, `rejectAll`, `openNewConversation`.
- **Example (keybindings.json):** `[{"key": "ctrl+shift+a", "command": "acceptAll"}, {"key": "ctrl+shift+r", "command": "rejectAll"}]`

#### 8. Set `MAX_THINKING_TOKENS=10000` to cap extended thinking costs
- Seen in: [claude_code_cost_optimisation.md], [claude_code_token_limits_cost_optimization_apac_teams.md]
- **What:** Extended thinking is the single biggest token spend lever. Default is uncapped. Setting 10K limits deep reasoning cost without breaking most tasks.
- **Example:** `export MAX_THINKING_TOKENS=10000` in `.env` or shell profile.

#### 9. Compact at session-defined milestones, not ad-hoc
- Seen in: [claude_code_compact_command_context_management.md], [my_top_10_claude_code_tips_from_11_months_of.md]
- **What:** Pick a consistent milestone (end of each feature, after each PR) to compact. Predictable compaction patterns = predictable quality.
- **Example:** Personal rule: compact after every 2 files modified or every 30 minutes of active session.

#### 10. Run multiple Claude sessions in parallel with tmux or split terminals
- Seen in: [my_top_10_claude_code_tips_from_11_months_of.md], [claude_code_tips_best_practices.md]
- **What:** While one session thinks or executes, work in another. Keep 2–3 sessions open with different scopes.
- **Example:** Session 1: feature implementation. Session 2: running tests + reviewing output. Session 3: documentation.

---

## Novice

---

## Theme 2: Prompting Strategies

**Summary:** The difference between engineers who get stuck and those who stay productive is mostly in how they prompt. Explicit context, thinking-first patterns, and short feedback loops outperform long, micromanaged prompts.

### Tips (ranked by source frequency)

#### 1. Be explicit — Claude does what you say, not what you mean
- Seen in: [claude_prompting_best_practices.md], [174731.md], [how_i_use_claude_code_to_accelerate_my_software_engineering_.md], [32_claude_code_tips_from_basics_to.md], [claude_code_tips_best_practices.md]
- **What:** Vague prompts produce vague output. Specify language, framework, file to modify, constraints, and expected output format upfront.
- **Example:** Bad: "Add authentication." Good: "Add JWT authentication to `src/middleware/auth.ts`. Use the existing `User` model in `src/models/user.ts`. Return 401 if token is invalid, 403 if expired."

#### 2. Force Claude to think before coding
- Seen in: [i_made_claude_code_think_before_it_codes_heres_the_prompt_bf.md], [claude_code_tips.md], [32_claude_code_tips_from_basics_to.md], [claude_code_best_practices_12_patterns_agentic_engineers_use.md]
- **What:** Prepend "Explore the codebase, then outline your approach before writing any code." Senior developers read before writing — Claude needs the same constraint.
- **Example:** `"Before implementing: (1) read auth.ts, (2) read the existing test file, (3) outline your approach. Only start coding after I confirm the plan."`

#### 3. Use @file references to stack context incrementally
- Seen in: [how_i_use_claude_code_to_accelerate_my_software_engineering_.md], [claude_code_tips.md], [claude_code_tips_best_practices.md], [claude_prompting_best_practices.md]
- **What:** Reference specific files rather than describing them. Build context from high-level to specific. Claude processes file references efficiently.
- **Example:** `@architecture.md @src/auth/middleware.ts "Now add OAuth2 support following the same pattern as the existing JWT flow"`

#### 4. Paste the error and say "fix" — don't micromanage the solution
- Seen in: [174731.md], [32_claude_code_tips_from_basics_to.md], [claude_code_tips.md]
- **What:** Let Claude's debugging ability work. Excessive guidance ("the error is probably in X, try Y") introduces anchoring bias and leads Claude astray. Paste the full stack trace and say "fix."
- **Example:** Paste the exact error → "fix" → if it fails twice: `/clear` and try a different angle.

#### 5. Ask Claude to double-check its own work
- Seen in: [32_claude_code_tips_from_basics_to.md], [claude_code_tips.md], [i_made_claude_code_think_before_it_codes_heres_the_prompt_bf.md]
- **What:** "Are you sure about this? Can you double check?" catches hallucinations, especially for API details and library specifics.
- **Example:** After Claude gives a solution: "Double-check that `AsyncIterator` exists in Node 18 before proceeding."

#### 6. Use constraint-based prompting to prevent over-engineering
- Seen in: [claude_code_tips_best_practices.md], [how_i_use_claude_code_to_accelerate_my_software_engineering_.md], [claude_code_best_practices_12_patterns_agentic_engineers_use.md]
- **What:** Scope constraints upfront prevent Claude from introducing unnecessary abstractions and building for hypothetical requirements.
- **Example:** `"In under 50 lines, using only stdlib, implement X. Do not add abstractions for hypothetical future requirements."`

#### 7. Use structured exploration prompts for unfamiliar codebases
- Seen in: [how_i_use_claude_code_to_accelerate_my_software_engineering_.md], [claude_code_best_practices_lessons_from_real_projects.md]
- **What:** A consistent pattern for onboarding Claude to a new service prevents wasted searches.
- **Example:** `"Explore @src/services/payments and create documentation: (1) core purpose, (2) architecture, (3) key files and their roles, (4) important gotchas."`

#### 8. Match model to task — use cheaper models for mechanical work
- Seen in: [claude_code_cost_optimisation.md], [claude_code_tips_best_practices.md], [claude_code_best_practices_12_patterns_agentic_engineers_use.md]
- **What:** Haiku for reviews, tests, linting. Sonnet for most implementation. Opus only for architecture and complex debugging.
- **Example:** `/model haiku` → "Review this PR for style" → `/model sonnet` → "Implement the changes."

---

## Theme 3: CLAUDE.md & Project Memory

**Summary:** The single highest-leverage investment. A well-structured CLAUDE.md prevents Claude from re-learning conventions every session. Most sources agree on what to include, what to exclude, and how to structure it.

### Tips (ranked by source frequency)

#### 1. Only include what Claude cannot infer from reading the codebase
- Seen in: [174731.md], [how_to_set_up_claude_md_file.md], [claude_code_best_practices_lessons_from_real_projects.md], [claude_code_best_practices_12_patterns_agentic_engineers_use.md]
- **What:** Build commands, test commands, branch naming, architectural decisions, known footguns. Exclude naming conventions and patterns already visible in the code.
- **Example:** `# CLAUDE.md\n## Test commands\nnpm test -- --testPathPattern\n## Never do\nNever use var; always const/let\nNever modify /src/auth/ without explicit confirmation`

#### 2. Encode prohibitions explicitly ("Never X") rather than vague guidance
- Seen in: [how_to_set_up_claude_md_file.md], [claude_code_security_best_practices.md], [174731.md], [claude_code_best_practices_lessons_from_real_projects.md]
- **What:** Claude responds more reliably to "Never modify /src/auth/ without confirmation" than "Be careful with auth."
- **Example:** `Never run destructive database migrations without showing the SQL first.\nNever commit .env files.\nNever use npm; always use pnpm.`

#### 3. Keep CLAUDE.md well under 100 lines; put everything else in reference files
- Seen in: [174731.md], [how_to_set_up_claude_md_file.md], [my_claude_code_setup.md]
- **What:** Compliance degrades before Anthropic's stated 200-line limit — empirically observed around 145 lines, where agents followed top rules and silently ignored the rest. Trimming to ~77 lines restored compliance immediately. Keep only the highest-signal rules; move detailed docs to `docs/architecture.md` etc. and reference them.
- **Example:** `# CLAUDE.md\nSee docs/architecture.md for the full system design.\nSee docs/db-schema.md for the database schema.`

#### 4. Update CLAUDE.md reactively — every time Claude repeats the same mistake
- Seen in: [how_to_set_up_claude_md_file.md], [claude_code_best_practices_lessons_from_real_projects.md], [my_top_10_claude_code_tips_from_11_months_of.md]
- **What:** When Claude makes an error twice on the same thing, that's a missing rule. Add it immediately. CLAUDE.md should evolve with the project.
- **Example:** If Claude keeps using `var` or generates functions without error handling → add a rule the same session.

#### 5. Use layered CLAUDE.md files in monorepos (root + per-package)
- Seen in: [how_to_set_up_claude_md_file.md], [my_claude_code_setup.md], [claude_code_best_practices_lessons_from_real_projects.md]
- **What:** Root CLAUDE.md for shared context; each sub-package has its own. Claude loads the most local file. Prevents polluting shared context with service-specific rules.
- **Example:** `/CLAUDE.md` (shared: conventions, tools)\n`/packages/auth/CLAUDE.md` (auth-specific: JWT patterns, security rules)

#### 6. Add a `context-essentials.md` for post-compaction rule re-injection
- Seen in: [claude_code_post_compaction_hooks_for_context_renewal_7b616d.md], [2026_02_28_claude_code_hooks_guide.md]
- **What:** Compaction is lossy — conventions mentioned at session start get compressed. A separate 10–50 line file with critical rules survives if re-injected automatically. Note: `/compact` is a slash command, not a tool — a `PostToolUse` matcher on `"compact"` will never fire. Instead, use a CLAUDE.md `@.claude/context-essentials.md` import (re-read every session) or a `Stop` hook to inject on every response.
- **Example (CLAUDE.md):** `@.claude/context-essentials.md` — Claude loads this at session start and after compaction restores CLAUDE.md context.

#### 7. Use Skill folder structures with progressive disclosure, not monolithic files
- Seen in: [174731.md], [claude_code_skills_automate_workflows.md]
- **What:** Structure as `SKILL.md` + `references/`, `scripts/`, `examples/` subdirs. Claude reads subdirectories only when needed, preventing context bloat.
- **Example:** `.claude/skills/code-review/SKILL.md` with `.claude/skills/code-review/checklist.md` (loaded on demand)

#### 8. Add a Gotchas section documenting failure modes
- Seen in: [174731.md], [claude_code_best_practices_lessons_from_real_projects.md]
- **What:** Every time Claude makes a project-specific mistake, document it. Over time this becomes the highest signal-to-noise content in CLAUDE.md.
- **Example:** `## Known footguns\n- This codebase uses custom Result<T,E> — never throw exceptions, always return Result\n- The legacy API at /api/v1 cannot be touched — use /api/v2`

---

## Intermediate

---

## Theme 4: Context Management

**Summary:** Context rot is the root cause of the "hitting the ceiling" problem. Engineers who master compaction, clearing, and phase boundaries maintain Claude's quality across arbitrarily long sessions.

### Tips (ranked by source frequency)

#### 1. Compact at ~60% context utilization — before warnings appear
- Seen in: [claude_code_compact_command_context_management.md], [174731.md], [simondholmes_ive_been_figuring_out_how_to_manage_context_act.md], [my_top_10_claude_code_tips_from_11_months_of.md], [claude_code_compact_command_context_management.md]
- **What:** Performance degrades before the hard limit. The 80% warning is already too late. Monitor with `/statusline` and compact at 60%.
- **Example:** `/statusline` shows context at 58% → run `/compact` proactively before quality dips.

#### 2. Append explicit preservation instructions to `/compact`
- Seen in: [claude_code_compact_command_context_management.md], [174731.md], [tool_use_context_engineering_context_engineering_tools.md]
- **What:** Without guidance, Claude decides what survives — and drops project conventions. Tell it exactly what to keep.
- **Example:** `/compact Keep: (1) decision to use PostgreSQL not SQLite and why, (2) the three functions identified for refactoring, (3) current error in auth.ts, (4) completed modules: auth.ts, middleware.ts`

#### 3. Verify state immediately after compaction
- Seen in: [claude_code_compact_command_context_management.md], [174731.md]
- **What:** Send a quick state-check prompt after compaction. Catches dropped context while it's fresh.
- **Example:** After `/compact` → "Summarize where we are and what we're working on next." If anything is wrong, correct it now.

#### 4. Use post-compaction hooks to re-inject critical rules automatically
- Seen in: [claude_code_post_compaction_hooks_for_context_renewal_7b616d.md], [2026_02_28_claude_code_hooks_guide.md]
- **What:** `/compact` is a slash command, not a tool — `PostToolUse` with `"matcher": "compact"` will never fire. The reliable alternative: `@`-import `context-essentials.md` in CLAUDE.md (Claude re-reads it every session start and after compaction restores the file) or use a `Stop` hook to unconditionally re-inject on every response turn.
- **Example (CLAUDE.md):** `@.claude/context-essentials.md` — single line that keeps critical rules in context without any hook wiring.

#### 5. Use phase-based sessions — clear between major work phases
- Seen in: [simondholmes_ive_been_figuring_out_how_to_manage_context_act.md], [174731.md], [claude_code_best_practices_12_patterns_agentic_engineers_use.md]
- **What:** Divide work into phases (architecture → implementation → testing). Start a fresh session at each phase boundary. Passing a phase summary as the first message is cheaper than carrying the whole history.
- **Example:** After completing architecture phase: start new session with "Summary of prior session: [decisions made]. Now implementing the auth module."

#### 6. Distinguish re-fetchable data from irreplaceable information
- Seen in: [claude_code_compact_command_context_management.md], [tool_use_context_engineering_context_engineering_tools.md]
- **What:** File contents and API responses can be re-fetched; architectural decisions and discovered constraints cannot. Preserve the latter; clear the former.
- **Example:** `/compact Keep: decision to use Redis for caching. Clear: grep output (can be re-run), file reads (can be re-fetched).`

#### 7. Use `/rewind` when Claude drifts — don't try to correct within the same context
- Seen in: [174731.md], [essential_claude_code_skills_and_commands.md]
- **What:** Erroneous reasoning stays in context and compounds. Rewind to the last good checkpoint, then re-prompt with a clearer instruction.
- **Example:** Press Esc Esc or run `/rewind` → Claude reverts to previous checkpoint → re-prompt correctly.

#### 8. Layer three complementary strategies: compaction + clearing + memory
- Seen in: [tool_use_context_engineering_context_engineering_tools.md], [simondholmes_ive_been_figuring_out_how_to_manage_context_act.md]
- **What:** Compaction = whole-transcript summarization. Clearing = surgical removal of bulky tool results. Memory = persistent notes to external storage (files/db) that survive resets.
- **Example:** Compact when context grows large → clear old file reads → save research findings to `notes/research.md` for next session.

---

## Theme 5: MCP Servers

**Summary:** MCPs are the fastest way to eliminate context switches. The right 2–3 MCPs make Claude Code a single interface for code + external services. The wrong configuration slows sessions and pollutes context.

### Tips (ranked by source frequency)

#### 1. Start with 2–3 core MCPs; add per-project on demand
- Seen in: [claude_code_mcp_top_10_must_install_en_html.md], [best_mcp_servers_for_claude_code.md], [setting_up_mcp_servers_in_claude_code_a_tech.md], [the_10_must_have_mcp_servers_for_claude_code_2025_developer_.md]
- **What:** Each MCP adds startup time and memory. Recommended default trio: Sequential Thinking + GitHub + Context7. Add database MCPs only in projects that need them.
- **Example:** `claude mcp add sequential-thinking -s user -- npx -y @modelcontextprotocol/server-sequential-thinking`

#### 2. Use Sequential Thinking MCP for complex problem decomposition
- Seen in: [claude_code_mcp_top_10_must_install_en_html.md], [the_10_must_have_mcp_servers_for_claude_code_2025_developer_.md], [setting_up_mcp_servers_in_claude_code_a_tech.md], [best_mcp_servers_for_claude_code.md]
- **What:** Makes Claude break down problems step-by-step before coding. Reduces incorrect implementations on complex tasks.
- **Example:** `claude mcp add sequential-thinking -s user -- npx -y @modelcontextprotocol/server-sequential-thinking`

#### 3. Store credentials in env vars, not in config files
- Seen in: [claude_code_mcp_top_10_must_install_en_html.md], [connect_claude_code_to_your_tools_with_mcp_5_setups_that_wor.md], [setting_up_mcp_servers_in_claude_code_a_tech.md]
- **What:** Use `${VAR_NAME}` expansion in `.mcp.json`; set values in shell profile or `.env` (gitignored). Prevents token leaks in committed configs.
- **Example (in .mcp.json):** `"env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }` then `export GITHUB_TOKEN=ghp_...` in `~/.zshrc`

#### 4. Use project-level `.mcp.json` to share MCPs across the team
- Seen in: [connect_claude_code_to_your_tools_with_mcp_5_setups_that_wor.md], [best_mcp_servers_for_claude_code.md], [setting_up_mcp_servers_in_claude_code_a_tech.md]
- **What:** Commit `.mcp.json` at project root so everyone on the team gets the same MCPs. Individual tokens added via local scope override.
- **Example:** Team shares database + GitHub MCPs via committed `.mcp.json`; each dev adds personal API keys locally.

#### 5. Connect database MCPs with read-only credentials only
- Seen in: [claude_code_mcp_top_10_must_install_en_html.md], [connect_claude_code_to_your_tools_with_mcp_5_setups_that_wor.md]
- **What:** Write-capable DB connections in an AI tool risk destructive queries. Create a dedicated read-only user.
- **Example:** `POSTGRES_CONNECTION_STRING: "postgresql://readonly_user:pass@localhost:5432/mydb"`

#### 6. Use Context7 MCP for up-to-date library documentation
- Seen in: [claude_code_mcp_top_10_must_install_en_html.md], [the_10_must_have_mcp_servers_for_claude_code_2025_developer_.md]
- **What:** Fetches current docs for React, Next.js, FastAPI etc. instead of relying on training data. Eliminates hallucinated APIs.
- **Example:** `claude mcp add context7 -- npx -y @context7/mcp-server`

#### 7. Debug MCP connection issues with `/mcp` command
- Seen in: [setting_up_mcp_servers_in_claude_code_a_tech.md], [connect_claude_code_to_your_tools_with_mcp_5_setups_that_wor.md]
- **What:** `/mcp` inside Claude Code lists all running servers, available tools, and auth status. First stop when an MCP fails to connect.
- **Example:** If GitHub MCP doesn't respond → `/mcp` → shows auth failures or missing npm packages.

#### 8. Use lazy loading (`"lazy": true`) for heavy MCPs
- Seen in: [claude_code_mcp_top_10_must_install_en_html.md], [setting_up_mcp_servers_in_claude_code_a_tech.md]
- **What:** Defers server startup until first tool call. Reduces session initialization time for MCPs not always needed.
- **Example (in .mcp.json):** `{ "mcpServers": { "docker": { "command": "...", "lazy": true } } }`

#### 9. GitHub MCP eliminates browser context switches for PR workflows
- Seen in: [claude_code_mcp_top_10_must_install_en_html.md], [connect_claude_code_to_your_tools_with_mcp_5_setups_that_wor.md], [the_10_must_have_mcp_servers_for_claude_code_2025_developer_.md]
- **What:** Read issues, review PRs, manage branches, and create pull requests from Claude Code without opening a browser.
- **Example:** "Review PR #456 and suggest improvements" → Claude fetches diff, reads comments, suggests code changes.

#### 10. Playwright MCP for E2E testing from the terminal
- Seen in: [claude_code_mcp_top_10_must_install_en_html.md], [the_10_must_have_mcp_servers_for_claude_code_2025_developer_.md]
- **What:** Accessibility-snapshot-based browser automation. Claude can take screenshots, interact with UI, and generate test cases.
- **Example:** "Take a screenshot of the login flow and validate it works" → Claude spins up browser, captures, analyzes.

---

## Theme 6: Commands, Skills & Plan Mode

**Summary:** Slash commands and skills are how you codify your workflow — turning ad-hoc prompts into repeatable, shareable, automatable operations. Plan mode closes the loop by giving you review control before changes land.

### Tips (ranked by source frequency)

#### 1. Define custom slash commands in `.claude/commands/` for repeated prompts
- Seen in: [creating_custom_slash_commands.md], [slash_commands.md], [claude_code_skills_vs_slash_commands.md], [essential_claude_code_skills_and_commands.md]
- **What:** Any markdown file in `.claude/commands/` becomes a `/command-name` invocable from the session. Commit to version control to share with team.
- **Example:** `.claude/commands/review-auth.md` → `/review-auth` runs a pre-written code review focused on the auth module.

#### 2. Use `$ARGUMENTS` in custom commands for dynamic input
- Seen in: [slash_commands.md], [creating_custom_slash_commands.md], [claude_code_deep_dive_slash_commands_9cd6ff4c33cb.md]
- **What:** The `$ARGUMENTS` placeholder gets replaced with whatever follows the command at invocation time.
- **Example:** `fix-issue.md` contains `"Fix GitHub issue #$ARGUMENTS following our error handling conventions"` → `/fix-issue 123` targets issue #123.

#### 3. Understand the difference: commands = manual one-off; skills = recurring with auto-invocation
- Seen in: [claude_code_skills_vs_slash_commands.md], [essential_claude_code_skills_and_commands.md], [claude_code_skills_automate_workflows.md]
- **What:** Commands are situational (you decide when). Skills can auto-invoke based on pattern detection. If you run the same command 3–4x/week, convert it to a skill.
- **Example:** `/compact` is a command. A code-review skill can be configured to auto-invoke after Claude makes a certain number of file edits.

#### 4. Use YAML frontmatter to restrict tools and add discoverability
- Seen in: [slash_commands.md], [creating_custom_slash_commands.md], [essential_claude_code_skills_and_commands.md]
- **What:** Frontmatter in command files constrains which tools Claude can call and documents the command's purpose.
- **Example:** `--- allowed-tools: Read, Grep, Glob description: Check color scheme consistency across all component files ---`

#### 5. Use Plan Mode (Shift+Tab) for high-risk changes before execution
- Seen in: [174731.md], [claude_code_commands_guide.md], [14553413_claude_code_cheatsheet.md], [claude_code_agentic_workflow_patterns.md]
- **What:** Plan Mode lets Claude research and propose changes without executing them. Review the plan, request adjustments, then approve. Shift+Tab cycles: `default → acceptEdits → plan`.
- **Example:** `Shift+Tab` twice → Claude shows proposed file changes without applying → you approve or reject each.

#### 6. Inject dynamic shell output into commands with backtick syntax
- Seen in: [slash_commands.md], [essential_claude_code_skills_and_commands.md]
- **What:** Embed live shell output into custom command prompts before they reach Claude.
- **Example:** Command file contains: `` ## Current git status:\n!`git status`\n\n## Changed files:\n!`git diff --name-only` ``

#### 7. Use `context: fork` in skills to run in isolated subagents
- Seen in: [essential_claude_code_skills_and_commands.md], [claude_code_skills_vs_slash_commands.md]
- **What:** Research and analysis tasks that shouldn't pollute the main conversation run in a forked context. Results are summarized back.
- **Example:** `--- context: fork --- # Deep security audit that runs independently`

#### 8. Run `/simplify` after AI-generated code to catch redundancy
- Seen in: [essential_claude_code_skills_and_commands.md], [claude_code_best_practices_12_patterns_agentic_engineers_use.md]
- **What:** Claude-generated code often contains unnecessary indirection and over-engineering. `/simplify` reviews for reuse opportunities and removes bloat.
- **Example:** Generate feature → `/review` for correctness → `/simplify` for code quality.

#### 9. Use `/loop` for recurring monitoring tasks during long sessions
- Seen in: [essential_claude_code_skills_and_commands.md]
- **What:** Set a repeating prompt that fires on an interval while the session is open.
- **Example:** `/loop 5m check dev server logs for new errors` or `/loop 10m run the test suite and report failures`

#### 10. Run skills on a schedule in headless mode via cron
- Seen in: [claude_code_skills_automate_workflows.md], [claude_code_skills_vs_slash_commands.md]
- **What:** Execute skills without an interactive session for CI/automated pipelines.
- **Example:** `0 7 * * * claude --print "Run /project:generate-daily-report" >> /logs/report.log 2>&1`

---

## Advanced

---

## Theme 7: Hooks & Automation

**Summary:** Hooks transform Claude Code from a conversational tool into a repeatable, enforceable workflow. They run outside the LLM as deterministic scripts — the most underused power feature.

### Tips (ranked by source frequency)

#### 1. Configure hooks at three scope levels: global, project-shared, local-override
- Seen in: [claude_code_hooks_a_complete_guide_to_automating_your_ai_cod.md], [hooks_guide.md], [2026_02_28_claude_code_hooks_guide.md], [hooks_in_claude_code.md]
- **What:** `~/.claude/settings.json` = personal defaults. `.claude/settings.json` = team-shared (commit this). `.claude/settings.local.json` = local overrides (gitignore this).
- **Example:** Team shares auto-formatter hook in committed `.claude/settings.json`; individuals override model in local settings.

#### 2. Use exit code 2 to BLOCK execution; exit code 1 only warns
- Seen in: [claude_code_hooks_tutorial.md], [2026_02_28_claude_code_hooks_guide.md], [hooks_guide.md]
- **What:** `exit 1` from a PreToolUse hook shows a warning but lets Claude proceed. `exit 2` actually prevents the tool from running.
- **Example:** `if [[ "$CMD" =~ "rm -rf" ]]; then echo "BLOCKED: rm -rf prohibited" >&2; exit 2; fi`

#### 3. Use jq to parse hook stdin and apply conditional logic
- Seen in: [claude_code_hooks.md], [2026_02_28_claude_code_hooks_guide.md], [claude_code_hooks_tutorial.md], [hooks_in_claude_code.md]
- **What:** Hook stdin is JSON containing tool name and input. Use `jq` to extract the file path, command, or other fields and conditionally trigger formatters or validators.
- **Example:** `FILE=$(cat | jq -r '.tool_input.file_path // empty') && [ -n "$FILE" ] && npx prettier --write "$FILE" 2>/dev/null || true`

#### 4. Run tests immediately after file edits with PostToolUse
- Seen in: [claude_code_hooks_tutorial.md], [claude_code_hooks_a_complete_guide_to_automating_your_ai_cod.md]
- **What:** Catch regressions before Claude compounds them across multiple edits. Run the test file corresponding to the edited source file.
- **Example:** `TEST_FILE="tests/test_$(basename "$FILE_PATH")"; [ -f "$TEST_FILE" ] && python -m pytest "$TEST_FILE" -x --tb=short`

#### 5. Block writes to sensitive files with path pattern matching
- Seen in: [hooks_guide.md], [2026_02_28_claude_code_hooks_guide.md], [claude_code_security_best_practices.md]
- **What:** PreToolUse hooks should exit 2 on writes to `.env`, `secrets.*`, `credentials`, `*.pem`, `id_rsa` etc.
- **Example:** `if echo "$FILE" | grep -qE '(\.env$|secrets\.|credentials|id_rsa|\.pem)'; then echo "Write to $FILE blocked" >&2; exit 2; fi`

#### 6. Use prompt-type hooks for context re-injection after compaction
- Seen in: [2026_02_28_claude_code_hooks_guide.md], [claude_code_post_compaction_hooks_for_context_renewal_7b616d.md]
- **What:** A hook with `"type": "prompt"` injects text into Claude's context (not just shell stdout). However, `/compact` is a slash command — `PostToolUse` won't catch it. A `Stop` hook fires after every response and can re-inject rules unconditionally; or pair a `UserPromptSubmit` hook with a CLAUDE.md `@` import so rules land at session start and survive compaction.
- **Example (settings.json):** `{"hooks": {"Stop": [{"type": "prompt", "prompt": "Reminder: this project uses Result<T,E> — never throw, always return Result. DB is PostgreSQL 16."}]}}`

#### 7. Auto-allow read-only commands with permissionDecision structured output
- Seen in: [2026_02_28_claude_code_hooks_guide.md], [hooks_guide.md]
- **What:** Return JSON from a PreToolUse hook to approve safe commands programmatically, eliminating repetitive permission dialogs.
- **Example:** `echo '{"permissionDecision": "allow"}' when command matches ^(ls|cat|head|tail|git log|git status)`

#### 8. Guard Stop hooks with stop_hook_active to prevent infinite loops
- Seen in: [hooks_guide.md], [claude_code_hooks_tutorial.md]
- **What:** A Stop hook that blocks completion re-triggers itself unless you check `stop_hook_active` in the input JSON.
- **Example:** `if [ "$(echo "$INPUT" | jq -r '.stop_hook_active')" = "true" ]; then exit 0; fi`

#### 9. Use SessionStart hooks to inject context from git history
- Seen in: [hooks_guide.md], [2026_02_28_claude_code_hooks_guide.md]
- **What:** Output recent commits, active branch, or project status at session start to prime Claude's context automatically.
- **Example:** `git log --oneline -5 && echo "Current branch: $(git branch --show-current)"`

#### 10. Profile hooks with `time` — keep PreToolUse under 500ms
- Seen in: [claude_code_hooks_tutorial.md], [hooks_in_claude_code.md]
- **What:** Every matched tool call pays the hook execution cost. Slow hooks make every file edit sluggish.
- **Example:** `time bash my-hook.sh` during development. Move slow operations to PostToolUse (non-blocking) instead.

---

## Expert

---

## Theme 8: Parallel Development (Subagents + Git Worktrees)

**Summary:** The most powerful throughput multiplier. Subagents and worktrees are two sides of the same coin — subagents handle context isolation, worktrees handle filesystem isolation. Used together they let you run multiple independent workstreams simultaneously.

### Tips (ranked by source frequency)

#### 1. Use `git worktree add` to create fully isolated parallel workspaces
- Seen in: [git_worktrees_claude_code_parallel_development.md], [mastering_git_worktrees_with_claude_code_for_parallel_develo.md], [parallel_vibe_coding_with_git_worktrees.md], [parallel_agentic_development_git_worktrees.md], [git_worktrees_for_parallel_ai_coding_agents.md]
- **What:** Each worktree is a separate directory sharing git history but with its own working tree. Open one Claude session per worktree — each has independent context.
- **Example:** `git worktree add ../project-auth -b feature/auth-refactor main && cd ../project-auth && claude`

#### 2. Plan task decomposition and file ownership before creating worktrees
- Seen in: [parallel_ai_development_with_git_worktrees_f2524afc3e33.md], [parallel_agentic_development_git_worktrees.md], [claude_code_agent_teams_parallel_workflows.md], [agents.md]
- **What:** Map which files each task touches before spawning agents. Any overlap = merge conflict. Create a table: Task → Agent → Primary Files → Dependencies.
- **Example:** `Frontend: src/components/**, src/pages/**\nBackend: src/api/**, src/services/**\nDB: migrations/**, prisma/schema.prisma`

#### 3. Be explicit about parallelization in prompts to subagents
- Seen in: [claude_code_parallel_subagents.md], [agents.md], [sub_agent_best_practices.md], [claude_code_agent_teams_parallel_workflows.md]
- **What:** Claude defaults to sequential unless you explicitly request parallel. Name each subagent's scope and ask for synthesis at the end.
- **Example:** `"Research these 5 topics in parallel using separate sub-agents. Once all complete, synthesize into a comparison matrix."`

#### 4. Isolate databases and port ranges per worktree
- Seen in: [git_worktrees_claude_code_parallel_development.md], [mastering_git_worktrees_with_claude_code_for_parallel_develo.md], [parallel_vibe_coding_with_git_worktrees.md]
- **What:** Dev servers collide if they share ports. Databases corrupt each other's schemas if shared. Use a port-offset convention per worktree.
- **Example:** `main: PORT=3000, DB=myapp_main\nauth-branch: PORT=3010, DB=myapp_auth\npayments-branch: PORT=3020, DB=myapp_payments`

#### 5. Set `CLAUDE_CODE_SUBAGENT_MODEL` to use cheaper models for subagents
- Seen in: [sub_agent_best_practices.md], [claude_code_agent_teams_parallel_agents.md]
- **What:** Subagents don't need the most powerful model. Run them on Sonnet while the orchestrator runs on Opus.
- **Example:** `export CLAUDE_CODE_SUBAGENT_MODEL="claude-sonnet-4-6"`

#### 6. Assign directory ownership to prevent merge conflicts in agent teams
- Seen in: [claude_code_agent_teams_parallel_workflows.md], [parallel_agentic_development_git_worktrees.md]
- **What:** At team level, explicitly assign directory ownership per agent. No agent touches files outside its zone.
- **Example (CLAUDE.md):** `## Agent file ownership\nFrontend agent: src/components/, src/pages/\nBackend agent: src/api/, src/services/\nTest agent: src/__tests__/`

#### 7. Define specialist agents in `.claude/agents/` for recurring patterns
- Seen in: [claude_code_parallel_subagents.md], [sub_agent_best_practices.md]
- **What:** Create persistent specialist agents as Markdown files with YAML frontmatter. Reuse them across sessions instead of retyping orchestration prompts.
- **Example:** `.claude/agents/security-reviewer.md`, `.claude/agents/test-writer.md`, `.claude/agents/doc-generator.md`

#### 8. Use the `-w` flag to create a worktree automatically from Claude Code
- Seen in: [what_is_claude_code_git_worktree_pattern_parallel_feature_br.md], [parallel_vibe_coding_with_git_worktrees.md]
- **What:** `claude -w <branch>` creates the worktree, checks out the branch, and opens a session in it — one command.
- **Example:** `claude -w feature/auth` or `claude --worktree feature/payments`

#### 9. Add routing rules to CLAUDE.md for orchestration decisions
- Seen in: [sub_agent_best_practices.md], [claude_code_agent_teams_parallel_workflows.md]
- **What:** Without explicit rules, Claude defaults to sequential. Document when to use parallel vs. sequential vs. background dispatch.
- **Example (CLAUDE.md):** `## Sub-agent routing\nParallel: 3+ unrelated tasks, no shared state, clear file boundaries\nSequential: tasks with dependencies, shared state mutations\nBackground: research, profiling, audit tasks`

#### 10. Keep parallel agent count to 2–4 unless you have higher-tier API access
- Seen in: [claude_code_agent_teams_parallel_agents.md], [claude_code_agent_teams_parallel_workflows.md]
- **What:** Standard API tiers rate-limit concurrent requests. 2–4 simultaneous sessions is the practical limit before hitting 429s.

---

## Cross-Theme Observations

- **Most frequent tip across all sources:** Compact proactively at ~50–60% context (mentioned in 8+ sources across context, cost, and productivity themes).
- **Most underused feature:** Hooks — only 7 of 82 sources covered them in depth, but they enable the highest-leverage automations.
- **Most common beginner-to-intermediate gap:** Engineers write long, vague prompts and wait. Experts write short, explicit prompts with explicit constraints and file references.
- **Theme with strongest consensus:** CLAUDE.md setup — near-universal agreement on "only include what Claude can't infer" and "use explicit prohibitions."
- **Theme with most disagreement:** Model selection — sources disagree on when Opus is worth the cost vs. Sonnet being sufficient.

---

*Generated from 82 sources. See `deliverables/raw/` for individual source files.*
