# Claude Code with VS Code and JetBrains: Best of Both Worlds

**Type:** article
**URL:** https://noqta.tn/en/blog/claude-code-ide
**Topic:** IDE Integrations
**Published:** unknown

## Content

[![Noqta](/images/logo.svg)](/en)



# Claude Code with VS Code and JetBrains: Best of Both Worlds

* [Claude Code](#0)
* [VS Code](#0)
* [JetBrains](#0)
* [IDE](#0)
* [Extensions](#0)

[![Noqta Team](/images/ai-author.svg)](/en/authors/noqta-team)

By [Noqta Team](/en/authors/noqta-team) ·

---

Loading the [Text to Speech](https://elevenlabs.io/text-to-speech) Audio Player...

## You Don't Have to Choose

Claude Code works in:

* ✅ Terminal (native)
* ✅ VS Code (Extension)
* ✅ JetBrains IDEs (Plugin)
* ✅ Desktop App (standalone)

**Choose what fits your workflow.**

## VS Code Extension

### Installation

1. Open VS Code
2. Extensions (Ctrl+Shift+X)
3. Search "Claude Code"
4. Install

Or from Terminal:

```
code --install-extension anthropic.claude-code code --install-extension anthropic.claude-code
```

### Features

#### 1. Inline Diffs

See proposed changes directly in code:

* 🟢 Additions in green
* 🔴 Deletions in red
* Accept/reject with one click

#### 2. @-Mentions

Reference files or symbols directly:

```
@src/auth.ts add logging to this file @UserService fix this function 
```

#### 3. Plan Review

Before execution, Claude shows its plan:

```
📋 Plan: 1. Modify auth.ts (lines 45-60) 2. Add new file: utils/logger.ts 3. Update tests [Accept] [Modify] [Reject] 
```

#### 4. Editor Integration

* Ctrl+K: Open Claude Code
* Select + Ctrl+K: Ask about selected code
* Right-click: Claude Code options

### Important Settings

```
// settings.json// settings.json{{ "claude-code.model": "claude-sonnet-4", "claude-code.model": "claude-sonnet-4", "claude-code.autoSuggest": true, "claude-code.autoSuggest": true, "claude-code.diffView": "inline", "claude-code.diffView": "inline", "claude-code.confirmBeforeEdit": true "claude-code.confirmBeforeEdit": true}}
```

## JetBrains Plugin

### Installation

1. Open Settings (Ctrl+Alt+S)
2. Plugins → Marketplace
3. Search "Claude Code"
4. Install & Restart

### Features

#### 1. IDE Diff Viewing

Same familiar diff interface from JetBrains.

#### 2. Context Sharing

Understands:

* Project structure
* Run configurations
* Build tools (Maven, Gradle)
* Framework-specific files

#### 3. Tool Window

Dedicated window for Claude Code:

* Conversation
* Task history
* Settings

### Supported IDEs

* ✅ IntelliJ IDEA
* ✅ PyCharm
* ✅ WebStorm
* ✅ PhpStorm
* ✅ Android Studio
* ✅ Other JetBrains IDEs

## Desktop App

Standalone application combining best features:

### Features

#### 1. Built-in Diff Review

Dedicated interface for reviewing changes.

#### 2. Parallel Sessions

Multiple sessions using Git Worktrees:

```
Session 1: feature/auth ──→ running Session 2: fix/bug-123 ──→ running Session 3: refactor/api ──→ waiting 
```

#### 3. Cloud Sessions

* Start cloud session
* Monitor progress
* Transfer to Terminal

### Installation

```
# macOS # macOSbrew install --cask claude-code brew  install --cask claude-code  # Or from website # Or from website# https://claude.ai/download# https://claude.ai/download
```

## When to Use Each Option?

### Terminal (CLI)

```
✅ High automation ✅ Large, complex tasks ✅ Scripting and CI/CD ✅ Advanced customization (Hooks, MCP) 
```

### VS Code Extension

```
✅ Daily development ✅ Want inline diffs ✅ Team uses VS Code ✅ Medium-sized tasks 
```

### JetBrains Plugin

```
✅ Java/Kotlin/Python projects ✅ Prefer JetBrains ecosystem ✅ Need IDE features 
```

### Desktop App

```
✅ Want dedicated interface ✅ Parallel sessions ✅ Focused diff review 
```

## Combination Strategy

### Example: A Typical Workday

**Morning (large task):**

```
# Terminal for planning and execution # Terminal for planning and executionclaude --thinking claude --thinking> I want to restructure the caching system>  I want to restructure the caching system
```

**Midday (small changes):**

```
# VS Code for quick edits Ctrl+K: "Fix this type error" 
```

**Evening (review):**

```
# Desktop App to review all changes # before creating PRs 
```

## Tips for Seamless Integration

### 1. Use the Same Settings

Settings files are shared:

* `~/.claude/settings.json`
* `.claude/settings.json` (project)

### 2. Share Context

```
# From VS Code, send to Terminal# From VS Code, send to Terminal# From Terminal, notice file in IDE# From Terminal, notice file in IDE
```

### 3. Leverage Each Tool

```
Planning ──→ Terminal (best for deep thinking) Coding ──→ IDE (best for edits) Review ──→ Desktop (best for review) 
```

## Recommended Settings

### For Beginners

```
{{ "claude-code.confirmBeforeEdit": true, "claude-code.confirmBeforeEdit": true, "claude-code.showPlanBeforeExecute": true, "claude-code.showPlanBeforeExecute": true, "claude-code.model": "claude-sonnet-4" "claude-code.model": "claude-sonnet-4"}}
```

### For Professionals

```
{{ "claude-code.confirmBeforeEdit": false, "claude-code.confirmBeforeEdit": false, "claude-code.autoApplyDiffs": true, "claude-code.autoApplyDiffs": true, "claude-code.model": "claude-opus-4" "claude-code.model": "claude-opus-4"}}
```

## Summary

Claude Code adapts to your workflow:

* **Terminal:** Power and control
* **VS Code/JetBrains:** Comfort and integration
* **Desktop:** Review and parallelism

**Tip:** Try all options and choose what fits each type of task.

---

[Read Next: Claude Code in CI/CD](/en/blog/claude-code-ci-cd)

---

Want to read more blog posts? Check out our latest blog post on[AI-Generated Code Security: Risks and Best Practices](/en/blog/securite-code-genere-ia-vulnerabilites-guide-2026).

[Back to the blog](/en/blog)

### Discuss Your Project with Us

We're here to help with your web development needs. Schedule a call to discuss your project and how we can assist you.

[Book a Call](https://calendly.com/noqta)

Let's find the best solutions for your needs.
