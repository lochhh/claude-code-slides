# Claude Code IDE Integration — VS Code, JetBrains, Cursor Setup | Claude Code 플레이북

**Type:** article
**URL:** https://claude-code-playbook.pages.dev/en/docs/level-1/ide-integration/
**Topic:** IDE Integrations
**Published:** unknown

## Content

![Claude Code 플레이북 로고](/en/img/logo.svg)
![Claude Code 플레이북 로고](/en/img/logo.svg)

# IDE Integration

**What you'll learn**: VS Code Extension setup, JetBrains plugin, and how to use Claude Code with just a terminal

IDE integration is optional. Claude Code is **fully functional from the terminal alone**.
IDE integration adds convenience like one-click launch and side-by-side code/AI views.

## VS Code Integration[​](#vs-code-integration "Direct link to VS Code Integration")

Requires VS Code 1.98.0 or higher. The same extension works in Cursor IDE.

### Installing the Official Extension[​](#installing-the-official-extension "Direct link to Installing the Official Extension")

`Ctrl+Shift+X`
`Cmd+Shift+X`

### Launching Claude Code in VS Code[​](#launching-claude-code-in-vs-code "Direct link to Launching Claude Code in VS Code")

After installation, you can launch Claude Code several ways:

`Cmd+Shift+P`
`Ctrl+Shift+P`
`claude`

### VS Code Extension Features[​](#vs-code-extension-features "Direct link to VS Code Extension Features")

The extension is a GUI wrapper for the CLI, adding these features:

`@filename`
`@filename#5-10`
`Open in New Tab`
`Open in New Window`
`@terminal:name`
`/plugins`
`/mcp`

Select code in the editor and Claude automatically recognizes it. Press `Option+K` (macOS) / `Alt+K` (Windows/Linux) to insert a @reference with file path and line numbers into your prompt.

`Option+K`
`Alt+K`

### VS Code Keyboard Shortcuts[​](#vs-code-keyboard-shortcuts "Direct link to VS Code Keyboard Shortcuts")

| Shortcut | Description |
| --- | --- |
| `Cmd+Esc` / `Ctrl+Esc` | Toggle focus between editor and Claude |
| `Cmd+Shift+Esc` / `Ctrl+Shift+Esc` | Open conversation in new tab |
| `Cmd+N` / `Ctrl+N` | Start new conversation (when Claude is focused) |
| `Option+K` / `Alt+K` | Insert @reference for current file + selection |

`Cmd+Esc`
`Ctrl+Esc`
`Cmd+Shift+Esc`
`Ctrl+Shift+Esc`
`Cmd+N`
`Ctrl+N`
`Option+K`
`Alt+K`

## JetBrains IDE Integration[​](#jetbrains-ide-integration "Direct link to JetBrains IDE Integration")

Works with IntelliJ IDEA, PyCharm, WebStorm, GoLand, and other JetBrains products.

### Plugin Installation[​](#plugin-installation "Direct link to Plugin Installation")

`Ctrl+Alt+S`
`Cmd+,`

### Launching Claude Code in JetBrains[​](#launching-claude-code-in-jetbrains "Direct link to Launching Claude Code in JetBrains")

## Terminal-Only Usage (No IDE)[​](#terminal-only-usage-no-ide "Direct link to Terminal-Only Usage (No IDE)")

Claude Code works fully from the terminal without any IDE. This is especially useful for server environments or SSH sessions.

`# Navigate to your project  
cd ~/my-project  
  
# Start Claude Code  
claude`

Claude Code uses the current directory as its workspace.

## Which Approach Should I Use?[​](#which-approach-should-i-use "Direct link to Which Approach Should I Use?")

| Situation | Recommended |
| --- | --- |
| General development | VS Code Extension |
| Cursor users | Install Claude Code extension in Cursor |
| JetBrains power users | JetBrains Plugin |
| Server/remote work | Terminal only |
| Just getting started | Terminal only (simplest) |

## Key Takeaways[​](#key-takeaways "Direct link to Key Takeaways")

`claude`

## Next Step[​](#next-step "Direct link to Next Step")

→ [Chrome Integration](/en/docs/level-1/chrome-integration) — Learn how to connect Claude Code with Chrome for web app testing and debugging directly from the terminal
