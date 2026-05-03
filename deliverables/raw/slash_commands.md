# Slash Commands in the SDK - Claude Code Docs

**Type:** article
**URL:** https://code.claude.com/docs/en/agent-sdk/slash-commands
**Topic:** Slash Commands & Skills
**Published:** unknown

## Content

![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)
![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)
![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

##### Agent SDK

##### Core concepts

##### Input and output

##### Extend with tools

##### Customize behavior

##### Control and observability

##### Deployment

##### SDK references

# Slash Commands in the SDK

Learn how to use slash commands to control Claude Code sessions through the SDK

`/`
`system/init`

## [​](#discovering-available-slash-commands) Discovering Available Slash Commands

`import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
 prompt: "Hello Claude",
 options: { maxTurns: 1 }
})) {
 if (message.type === "system" && message.subtype === "init") {
 console.log("Available slash commands:", message.slash_commands);
 // Example output: ["/compact", "/context", "/usage"]
 }
}`

## [​](#sending-slash-commands) Sending Slash Commands

`import { query } from "@anthropic-ai/claude-agent-sdk";

// Send a slash command
for await (const message of query({
 prompt: "/compact",
 options: { maxTurns: 1 }
})) {
 if (message.type === "result") {
 console.log("Command executed:", message.result);
 }
}`

## [​](#common-slash-commands) Common Slash Commands

### [​](#/compact-compact-conversation-history) `/compact` - Compact Conversation History

`/compact`
`/compact`
`import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
 prompt: "/compact",
 options: { maxTurns: 1 }
})) {
 if (message.type === "system" && message.subtype === "compact_boundary") {
 console.log("Compaction completed");
 console.log("Pre-compaction tokens:", message.compact_metadata.pre_tokens);
 console.log("Trigger:", message.compact_metadata.trigger);
 }
}`

### [​](#clearing-the-conversation) Clearing the conversation

`/clear`
`query()`
`query()`
`resume`

## [​](#creating-custom-slash-commands) Creating Custom Slash Commands

`.claude/commands/`
`.claude/skills/<name>/SKILL.md`
`/name`
`.claude/commands/`

### [​](#file-locations) File Locations

`.claude/commands/`
`.claude/skills/`
`~/.claude/commands/`
`~/.claude/skills/`

### [​](#file-format) File Format

`.md`

#### [​](#basic-example) Basic Example

`.claude/commands/refactor.md`
`Refactor the selected code to improve readability and maintainability.
Focus on clean code principles and best practices.`
`/refactor`

#### [​](#with-frontmatter) With Frontmatter

`.claude/commands/security-check.md`
`---
allowed-tools: Read, Grep, Glob
description: Run security vulnerability scan
model: claude-opus-4-7
---

Analyze the codebase for security vulnerabilities including:
- SQL injection risks
- XSS vulnerabilities
- Exposed credentials
- Insecure configurations`

### [​](#using-custom-commands-in-the-sdk) Using Custom Commands in the SDK

`import { query } from "@anthropic-ai/claude-agent-sdk";

// Use a custom command
for await (const message of query({
 prompt: "/refactor src/auth/login.ts",
 options: { maxTurns: 3 }
})) {
 if (message.type === "assistant") {
 console.log("Refactoring suggestions:", message.message);
 }
}

// Custom commands appear in the slash_commands list
for await (const message of query({
 prompt: "Hello",
 options: { maxTurns: 1 }
})) {
 if (message.type === "system" && message.subtype === "init") {
 // Will include both built-in and custom commands
 console.log("Available commands:", message.slash_commands);
 // Example: ["/compact", "/context", "/usage", "/refactor", "/security-check"]
 }
}`

### [​](#advanced-features) Advanced Features

#### [​](#arguments-and-placeholders) Arguments and Placeholders

`.claude/commands/fix-issue.md`
`---
argument-hint: [issue-number] [priority]
description: Fix a GitHub issue
---

Fix issue #$1 with priority $2.
Check the issue description and implement the necessary changes.`
`import { query } from "@anthropic-ai/claude-agent-sdk";

// Pass arguments to custom command
for await (const message of query({
 prompt: "/fix-issue 123 high",
 options: { maxTurns: 5 }
})) {
 // Command will process with $1="123" and $2="high"
 if (message.type === "result") {
 console.log("Issue fixed:", message.result);
 }
}`

#### [​](#bash-command-execution) Bash Command Execution

`.claude/commands/git-commit.md`
`---
allowed-tools: Bash(git add *), Bash(git status *), Bash(git commit *)
description: Create a git commit
---

## Context

- Current status: !`git status`
- Current diff: !`git diff HEAD`

## Task

Create a git commit with appropriate message based on the changes.`

#### [​](#file-references) File References

`@`
`.claude/commands/review-config.md`
`---
description: Review configuration files
---

Review the following configuration files for issues:
- Package config: @package.json
- TypeScript config: @tsconfig.json
- Environment config: @.env

Check for security issues, outdated dependencies, and misconfigurations.`

### [​](#organization-with-namespacing) Organization with Namespacing

`.claude/commands/
├── frontend/
│ ├── component.md # Creates /component (project:frontend)
│ └── style-check.md # Creates /style-check (project:frontend)
├── backend/
│ ├── api-test.md # Creates /api-test (project:backend)
│ └── db-migrate.md # Creates /db-migrate (project:backend)
└── review.md # Creates /review (project)`

### [​](#practical-examples) Practical Examples

#### [​](#code-review-command) Code Review Command

`.claude/commands/code-review.md`
`---
allowed-tools: Read, Grep, Glob, Bash(git diff *)
description: Comprehensive code review
---

## Changed Files
!`git diff --name-only HEAD~1`

## Detailed Changes
!`git diff HEAD~1`

## Review Checklist

Review the above changes for:
1. Code quality and readability
2. Security vulnerabilities
3. Performance implications
4. Test coverage
5. Documentation completeness

Provide specific, actionable feedback organized by priority.`

#### [​](#test-runner-command) Test Runner Command

`.claude/commands/test.md`
`---
allowed-tools: Bash, Read, Edit
argument-hint: [test-pattern]
description: Run tests with optional pattern
---

Run tests matching pattern: $ARGUMENTS

1. Detect the test framework (Jest, pytest, etc.)
2. Run tests with the provided pattern
3. If tests fail, analyze and fix them
4. Re-run to verify fixes`
`import { query } from "@anthropic-ai/claude-agent-sdk";

// Run code review
for await (const message of query({
 prompt: "/code-review",
 options: { maxTurns: 3 }
})) {
 // Process review feedback
}

// Run specific tests
for await (const message of query({
 prompt: "/test auth",
 options: { maxTurns: 5 }
})) {
 // Handle test results
}`

## [​](#see-also) See Also

Was this page helpful?

![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)
![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)

Company

Help and security

Learn

Terms and policies
