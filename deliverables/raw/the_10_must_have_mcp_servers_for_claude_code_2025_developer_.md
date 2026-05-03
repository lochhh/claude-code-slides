# The 10 Must-Have MCP Servers for Claude Code (2025 Developer ...

**Type:** article
**URL:** https://roobia.medium.com/the-10-must-have-mcp-servers-for-claude-code-2025-developer-edition-43dc3c15c887
**Topic:** MCP Servers
**Published:** unknown

## Content

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Froobia.medium.com%2Fthe-10-must-have-mcp-servers-for-claude-code-2025-developer-edition-43dc3c15c887&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Froobia.medium.com%2Fthe-10-must-have-mcp-servers-for-claude-code-2025-developer-edition-43dc3c15c887&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

# The 10 Must-Have MCP Servers for Claude Code (2025 Developer Edition)

[Roobia William](/?source=post_page---byline--43dc3c15c887---------------------------------------)

6 min readAug 18, 2025

Modern developers crave tools that automate, integrate, and accelerate their coding experience. Claude Code, Anthropic’s command-line AI assistant, is powerful on its own — but when you connect it to Model Context Protocol (MCP) servers, it becomes a true coding powerhouse. MCP servers act as bridges, letting Claude Code interact with external APIs, databases, file systems, and more, all in real time. The result? You can automate tasks, access live data, and streamline your workflow — without ever leaving your terminal.

## What is MCP and Why Does It Matter?

Model Context Protocol (MCP) is Anthropic’s open standard for connecting AI models like Claude to external tools. Think of MCP as a universal adapter: it lets Claude Code “talk” to servers that expose specific functions, from file operations to API calls. This modular approach means you can customize your AI assistant’s capabilities with plug-and-play ease.

MCP has three main parts:

* **Host:** The app (Claude Code, Cursor, etc.) that makes requests
* **Client:** The go-between for host and servers
* **Server:** The tool or service (like GitHub, Apidog, or your local file system)

With MCP, Claude Code isn’t just a chatbot — it’s a full-featured automation and productivity engine. Here are the top 10 MCP servers every developer should know in 2025.

## 1. GitHub MCP Server: Version Control, Automated

GitHub MCP server connects Claude Code to GitHub’s API. Read issues, manage PRs, trigger CI/CD, and analyze commits — all from your terminal.

**Why use it?**

* Automate GitHub tasks (comment, merge, etc.)
* Pull commit histories for debugging
* Stay focused — no more context switching

**Setup:**

* Install Node.js, run `npm install @composio/mcp@latest`
* `npx @composio/mcp@latest setup github --client claude`
* Authenticate via OAuth in Claude Code’s settings
* Restart Claude Code

**Example:**

Ask Claude Code to “find all issues about authentication” — get instant results.

## 2. Apidog MCP Server: Connect AI to API Specifications

[Apidog MCP server](https://bit.ly/41ItNSS) bridges the gap between your API specifications and AI-powered development workflows. This essential MCP server allows Claude and other AI assistants to directly access and work with your API documentation, making code generation more accurate and contextually aware.

[## Apidog MCP Server: The Bridge Between Your API Specifications and AI Coding Assistants

### Software development is undergoing a profound transformation as artificial intelligence becomes increasingly integrated…

roobia.medium.com](/apidog-mcp-server-the-bridge-between-your-api-specifications-and-ai-coding-assistants-12d39cd44d12?source=post_page-----43dc3c15c887---------------------------------------)

### Key Capabilities

* **API Specification Integration:** Connects AI to your Apidog project, online API documentation published by Apidog, or local OpenAPI/Swagger files
* **Intelligent Code Generation:** Generate DTOs, controllers, and client code based on your actual API contracts
* **Real-time Updates:** AI can refresh cached API data to work with the latest specification changes

### Why Developers Love It

The Apidog MCP Server eliminates the guesswork from API-driven development. Instead of manually translating API specs into code, developers can simply ask Claude to “generate Java records for the Product schema” or “add the new fields to the User DTO based on the API specification.” The AI pulls directly from your authoritative API documentation, ensuring generated code matches your exact contracts.

## Setup Process

Let’s say, now we want to use local OpenAPI/Swagger files as the data source for Claude AI.

1. Open Claude Code’s settings and navigate to the MCP tab.
2. Add the Apidog MCP server configuration to `mcp.json`:

```
//for macOS/Linux:{  "mcpServers": {    "API specification": {      "command": "npx",      "args": [        "-y",        "apidog-mcp-server@latest",        "--oas=<oas-url-or-path>"      ]    }  }}//for Windows:{  "mcpServers": {    "API specification": {      "command": "cmd",      "args": [        "/c",        "npx",        "-y",        "apidog-mcp-server@latest",        "--oas=<oas-url-or-path>"      ]    }  }}
```

3. Test the connection by asking Claude Code to fetch one of the endpoint specifications.

4. If the AI successfully returns information that meets the expectations, the connection is established!

## 3. File System MCP Server: Local File Power

This server lets Claude Code read, write, and edit files on your machine. Perfect for project management, log analysis, or quick edits.

**Why use it?**

* Automate file operations (CRUD)
* Keep project context at your fingertips
* Refactor or clean up files with a prompt

**Setup:**

* Clone: `git clone https://github.com/modelcontextprotocol/servers.git`
* Go to `src/filesystem`, run `npm install`
* Configure in `claude_desktop_config.json`
* Restart Claude Code

**Example:**

“Update the README.md with a new section” — done in seconds.

## 4. Sequential Thinking MCP Server: Smarter Problem Solving

This server helps Claude Code break down complex tasks into logical steps — great for architecture, refactoring, or planning.

**Why use it?**

* Guides Claude Code to think step-by-step
* Handles big projects with clear logic
* Makes debugging and design easier

**Setup:**

* `npm install -g @modelcontextprotocol/server-sequential-thinking`
* Add to `claude_desktop_config.json`:

```
{  "mcpServers": {    "sequential-thinking": {      "command": "node",      "args": ["sequential-thinking.js"]    }  }}
```

* Restart and test with “Break down the steps to refactor this module.”

**Example:**

“Outline the steps to decouple this service” — get a detailed plan.

## 5. Puppeteer MCP Server: Web Automation

Control browsers for scraping, testing, or automating workflows. Navigate pages, take screenshots, and interact with web elements.

**Why use it?**

* Automate browser tasks
* Run UI tests
* Scrape web data for analysis

**Setup:**

* `npm install puppeteer`
* Clone the repo, install dependencies
* Configure Claude Code and restart

**Example:**

## Get Roobia William’s stories in your inbox

Join Medium for free to get updates from this writer.

“Take a screenshot of this webpage” — get the image instantly.

## 6. PostgreSQL MCP Server: Natural Language Database Queries

Query your database using plain English. No more manual SQL — just ask and get results.

**Why use it?**

* Translate natural language to SQL
* Retrieve and manipulate data easily
* Boost productivity for non-SQL experts

**Setup:**

* Clone: `git clone https://github.com/modelcontextprotocol/servers.git`
* Go to `src/postgres`, install dependencies
* Configure with your DB credentials

**Example:**

“Summarize sales data from the past month” — get a formatted report.

## 7. Notion MCP Server: Docs and Tasks, Synced

Connect Claude Code to Notion for instant access to docs, tasks, and project specs.

**Why use it?**

* Update Notion tasks from the terminal
* Fetch project specs for context
* Sync team workflows with AI

**Setup:**

* `npx @composio/mcp@latest setup notion --client claude`
* Authenticate via OAuth

**Example:**

“Add a new task to Notion for code review” — no browser needed.

## 8. Memory Bank MCP Server: Persistent Context

Give Claude Code a memory! Retain context across sessions, perfect for big projects or long-term tracking.

**Why use it?**

* Recall prior interactions
* Maintain coherence in large codebases
* Reduce repetitive explanations

**Setup:**

* Clone: `git clone https://github.com/modelcontextprotocol/server-memory.git`
* Install and configure

**Example:**

“Resume work on the last module I edited” — Claude Code remembers.

## 9. Figma MCP Server: Design-to-Code Magic

Bridge the gap between design and code. Convert Figma layouts into code snippets or UI components.

**Why use it?**

* Turn Figma designs into code
* Rapid prototyping
* Align devs and designers

**Setup:**

* `npx @composio/mcp@latest setup figma --client claude`
* Authenticate via OAuth

**Example:**

“Convert this Figma layout to React components” — get production-ready code.

## 10. Zapier MCP Server: Automate Everything

Connect Claude Code to Zapier for cross-app automation — trigger actions in Slack, Gmail, Trello, and more.

**Why use it?**

* Automate multi-app workflows
* Streamline notifications and updates
* Integrate with hundreds of services

**Setup:**

* `npx @composio/mcp@latest setup zapier --client claude`
* Authenticate with Zapier

**Example:**

“Send a Slack message when a new PR is opened” — team communication, automated.

## How to Choose the Right MCP Server

* **Task type:** Web automation? Use Puppeteer. Database work? PostgreSQL.
* **Setup:** Look for clear docs and OAuth support (Apidog, Notion).
* **Scale:** Use Memory Bank for big projects, Sequential Thinking for complex logic.
* **Integration:** Zapier for cross-app, GitHub for version control.

Test servers with simple prompts, and always secure sensitive data by restricting access.

## Tips for Getting the Most from MCP Servers

* Keep configs clean — avoid typos in `claude_desktop_config.json`
* Use debug flags (`--mcp-debug`) to troubleshoot
* Store prompt templates in `.claude/commands`
* Combine servers for powerful workflows
* Limit active servers to avoid slowdowns

## Why MCP Servers Are a Game-Changer for Claude Code

MCP servers turn Claude Code into a true AI-powered development assistant. By connecting to tools like GitHub, Apidog, and PostgreSQL, you can automate, integrate, and accelerate your workflow. The modular design means new servers are always being developed, so your setup stays future-proof.

Ready to level up your coding? Start experimenting with these top MCP servers — and don’t forget to download Apidog for free to make your API-driven projects even smoother.

[Mcps](https://medium.com/tag/mcps?source=post_page-----43dc3c15c887---------------------------------------)

[Mcp Server](https://medium.com/tag/mcp-server?source=post_page-----43dc3c15c887---------------------------------------)

[Mcp Client](https://medium.com/tag/mcp-client?source=post_page-----43dc3c15c887---------------------------------------)

[Claude Code](https://medium.com/tag/claude-code?source=post_page-----43dc3c15c887---------------------------------------)

[Mcp Tool](https://medium.com/tag/mcp-tool?source=post_page-----43dc3c15c887---------------------------------------)

[## Written by Roobia William](/?source=post_page---post_author_info--43dc3c15c887---------------------------------------)

[39 followers](/followers?source=post_page---post_author_info--43dc3c15c887---------------------------------------)

·[0 following](/following?source=post_page---post_author_info--43dc3c15c887---------------------------------------)

A seasoned backend developer with a deep expertise in API development.

## Responses (1)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Froobia.medium.com%2Fthe-10-must-have-mcp-servers-for-claude-code-2025-developer-edition-43dc3c15c887&source=---post_responses--43dc3c15c887---------------------respond_sidebar------------------)

[Tangi Vass](https://medium.com/@tangi.vass?source=post_page---post_responses--43dc3c15c887----0-----------------------------------)

[Sep 17, 2025](https://medium.com/@tangi.vass/claude-code-is-the-only-coding-agents-that-natively-supports-and-prefers-the-gh-cli-f4e72fbd6589?source=post_page---post_responses--43dc3c15c887----0-----------------------------------)

```


Claude Code is the only coding agents that natively supports and prefers the gh cli. Much better than the alternative MCP server you have to use with the other CA.


```

## More from Roobia William

[Roobia William](/?source=post_page---author_recirc--43dc3c15c887----0---------------------87291f3e_474d_4b22_8b94_660ab404d105--------------)

[## Running Uncensored DeepSeek R1 on Local Machine

### The rise of open-source language models has democratized access to powerful AI tools, enabling developers, researchers, and enthusiasts to…](/running-uncensored-deepseek-r1-on-local-machine-b1d4b4d3a0d6?source=post_page---author_recirc--43dc3c15c887----0---------------------87291f3e_474d_4b22_8b94_660ab404d105--------------)

May 22, 2025

[Roobia William](/?source=post_page---author_recirc--43dc3c15c887----1---------------------87291f3e_474d_4b22_8b94_660ab404d105--------------)

[## Reduce Your Cursor AI Bill: How to Use Claude Code Without the 20% Markup

### Cursor is quickly becoming a favorite IDE for AI-assisted developers, but there’s a cost catch: Cursor adds a 20% markup to built-in AI API…](/reduce-your-cursor-ai-bill-how-to-use-claude-code-without-the-20-markup-09ab06778eaa?source=post_page---author_recirc--43dc3c15c887----1---------------------87291f3e_474d_4b22_8b94_660ab404d105--------------)

Aug 18, 2025

[Roobia William](/?source=post_page---author_recirc--43dc3c15c887----2---------------------87291f3e_474d_4b22_8b94_660ab404d105--------------)

[## OpenAI API Pricing and How to Calculate Cost Automatically

### OpenAI API is a popular tool for accessing AI services like ChatGPT and DALL·E 3. However, usage requires payment. This guide covers the…](/openai-api-pricing-and-how-to-calculate-cost-automatically-e20e108eabdb?source=post_page---author_recirc--43dc3c15c887----2---------------------87291f3e_474d_4b22_8b94_660ab404d105--------------)

Sep 9, 2024

[Roobia William](/?source=post_page---author_recirc--43dc3c15c887----3---------------------87291f3e_474d_4b22_8b94_660ab404d105--------------)

[## Build Your Own AI Command Center: A Self-Hosted MCP Server with guMCP

### Imagine having full control over how different AI models interact with your applications — all within a secure, self-hosted environment…](/build-your-own-ai-command-center-a-self-hosted-mcp-server-with-gumcp-d9973ece8b5a?source=post_page---author_recirc--43dc3c15c887----3---------------------87291f3e_474d_4b22_8b94_660ab404d105--------------)

May 16, 2025

[See all from Roobia William](/?source=post_page---author_recirc--43dc3c15c887---------------------------------------)

## Recommended from Medium

In

[Towards AI](https://pub.towardsai.net/?source=post_page---read_next_recirc--43dc3c15c887----0---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

by

[Rick Hightower](https://medium.com/@richardhightower?source=post_page---read_next_recirc--43dc3c15c887----0---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

[## Claude Code Agent Skills 2.0: From Custom Instructions to Programmable Agents

### Skills are no longer instructions. They are programs.](https://medium.com/@richardhightower/claude-code-agent-skills-2-0-from-custom-instructions-to-programmable-agents-ab6e4563c176?source=post_page---read_next_recirc--43dc3c15c887----0---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

Mar 9

[352

6](https://medium.com/@richardhightower/claude-code-agent-skills-2-0-from-custom-instructions-to-programmable-agents-ab6e4563c176?source=post_page---read_next_recirc--43dc3c15c887----0---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

In

[AI Software Engineer](https://medium.com/ai-software-engineer?source=post_page---read_next_recirc--43dc3c15c887----1---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

by

[Joe Njenga](https://medium.com/@joe.njenga?source=post_page---read_next_recirc--43dc3c15c887----1---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

[## Anthropic Just Released Claude Code Course (And I Earned My Certificate)

### Anthropic just launched their Claude Code in Action course, and I’ve just passed — how about you?](https://medium.com/@joe.njenga/anthropic-just-released-claude-code-course-and-i-earned-my-certificate-ad68745d46de?source=post_page---read_next_recirc--43dc3c15c887----1---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

Jan 21

[4K

63](https://medium.com/@joe.njenga/anthropic-just-released-claude-code-course-and-i-earned-my-certificate-ad68745d46de?source=post_page---read_next_recirc--43dc3c15c887----1---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

[Agent Native](https://agentnativedev.medium.com/?source=post_page---read_next_recirc--43dc3c15c887----0---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

[## Local LLMs That Can Replace Claude Code

### Editor’s note: While hardware tiers remain valuable context for this article, we’ve published an updated list for the models themselves:](https://agentnativedev.medium.com/local-llms-that-can-replace-claude-code-6f5b6cac93bf?source=post_page---read_next_recirc--43dc3c15c887----0---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

Jan 20

[1.7K

51](https://agentnativedev.medium.com/local-llms-that-can-replace-claude-code-6f5b6cac93bf?source=post_page---read_next_recirc--43dc3c15c887----0---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

[unicodeveloper](https://medium.com/@unicodeveloper?source=post_page---read_next_recirc--43dc3c15c887----1---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

[## 10 Must-Have Skills for Claude (and Any Coding Agent) in 2026

### The definitive guide to agent skills that change how Claude Code, Cursor, Gemini CLI, and other AI coding assistants perform in production.](https://medium.com/@unicodeveloper/10-must-have-skills-for-claude-and-any-coding-agent-in-2026-b5451b013051?source=post_page---read_next_recirc--43dc3c15c887----1---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

Mar 9

[695

9](https://medium.com/@unicodeveloper/10-must-have-skills-for-claude-and-any-coding-agent-in-2026-b5451b013051?source=post_page---read_next_recirc--43dc3c15c887----1---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

[## Run Claude Code with Local & Cloud Models in 5 Minutes (Ollama, LM Studio, llama.cpp, OpenRouter)

### This post exists because the old guides were written back when using non-Anthropic models in Claude Code required hacks and weird adapters…](https://medium.com/@luongnv89/run-claude-code-on-local-cloud-models-in-5-minutes-ollama-openrouter-llama-cpp-6dfeaee03cda?source=post_page---read_next_recirc--43dc3c15c887----2---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

Jan 30

[492

14](https://medium.com/@luongnv89/run-claude-code-on-local-cloud-models-in-5-minutes-ollama-openrouter-llama-cpp-6dfeaee03cda?source=post_page---read_next_recirc--43dc3c15c887----2---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

[## 10 Claude Code Commands That Cut My Dev Time 60%: A Practical Guide

### Custom slash commands, subagents, and automation workflows that transformed my team’s productivity — with copy-paste templates you can use](https://alirezarezvani.medium.com/10-claude-code-commands-that-cut-my-dev-time-60-a-practical-guide-60036faed17f?source=post_page---read_next_recirc--43dc3c15c887----3---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

Nov 20, 2025

[1.95K

37](https://alirezarezvani.medium.com/10-claude-code-commands-that-cut-my-dev-time-60-a-practical-guide-60036faed17f?source=post_page---read_next_recirc--43dc3c15c887----3---------------------4bd03852_8c99_435d_9d50_ebcb4e60bfc4--------------)

[See more recommendations](https://medium.com/?source=post_page---read_next_recirc--43dc3c15c887---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----43dc3c15c887---------------------------------------)
