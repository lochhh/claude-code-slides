# 7 Claude MCP servers you can set up right now

**Type:** article
**URL:** https://zapier.com/blog/claude-mcp-servers/
**Topic:** MCP Servers
**Published:** unknown

## Content

[Skip to content](#main)

[Log in](/app/login)[Sign up](/sign-up)



* [Home](/blog)
* [Productivity](/blog/categories/productivity)
* [App tips](/blog/categories/app-tips)

[App tips](/blog/all-articles/app-tips)6 min read

# 7 Claude MCP servers you can set up right now

By Maddy Osman · June 17, 2025

![A hero image with the logo of Anthropic, the makers of Claude](https://images.ctfassets.net/lzny33ho1g45/1SZ6jOtAZmR4WeR685pjkj/4d2f78102cc68470b86c5c7c48ca55cc/anthropic-app-tips.jpg?fm=jpg&q=31&fit=thumb&w=1520&h=760)

**Claude** **MCP (Model Context Protocol) servers** let you securely pull in data and interact with external apps or systems directly from Claude. In practice, it means you can work directly with services like Zapier while chatting with Claude.

MCP servers facilitate the connection between AI tools like Claude and all the other apps you use. They make it possible to direct the AI to take actions—like adding new records to a database or CRM—without leaving the chat. If you live in Claude, you can see how useful this would be.

Here, I'll walk you through the MCP servers that I've found the most useful when working in Claude. I'll show you how to set them up and give you some examples of how you might use them.

**Table of contents:**

* [What is an MCP server?](#what)
* [How to set up an MCP server in Claude](#setup)
* [MCP servers you can start using with Claude right now](#examples)
* [Start using MCP with all your favorite apps](#start)

## What is an MCP server?

[Model Context Protocol (MCP)](/blog/mcp/) acts as a bridge between AI and the tools and data you want the AI to use. An MCP server allows you to interact with a specific tool straight from Claude or other AI tools (and still using natural language).

There are official MCP servers that brands offer and MCP servers that other individuals and organizations have created themselves.

For example, one of my favorite unofficial MCP servers creates a connection to my Google Search Console data and allows me to query it for trends and create data visualizations straight from Claude.

![The unofficial GSC server in Claude](https://images.ctfassets.net/lzny33ho1g45/4btGjojm4Q2wqz9KRpUPI9/bb252c0718ff854d5606b4e0ee4869b8/claude-mcp-servers-image13.png)

**A word of caution**: MCP servers can provide powerful access to your computer and any connected tools or resources. Always ensure you trust the clients or individuals you grant access to, and review permissions carefully before connecting your MCP to external services. Start with MCPs from official sources (like the ones I suggest in this article) for the safest and most secure introduction to this concept.

## How to set up a Claude MCP server

Using an MCP server involves following the MCP and client-specific setup instructions. So even within Claude, it'll look slightly different for each MCP server.

Having said that, here are the general steps to follow to set up an MCP server to work with Claude desktop:

1. Open Claude desktop.
2. Navigate to **File** > **Settings** > **Developer**.
3. Click the **Edit Config** button.
4. Open the highlighted file (`claude_desktop_config.json`) in a code editor like Sublime Text.
5. Add the MCP server JSON code to the `claude_desktop_config.json` file. (JSON code for each MCP server featured in this article is included in the linked resources.) For each server, you may also need to add a personal access token (like an API key).

   If you're implementing more than one MCP server, you can ask Claude to weave together the MCP servers' JSON code so it's ready to add without unintentionally introducing code formatting errors.
6. Save the `claude_desktop_config.json` file.
7. Relaunch Claude desktop to start using the new MCP server and its associated tools.
8. Click the **Search and tools** (toggle slider) icon to view connected MCP servers and tools, and make sure to toggle on the tools you want Claude to have access to.
9. Chat with Claude using natural language to take action in the apps you've connected.

## Claude MCP servers you can start using right now

Now that you have a solid understanding of the basics, here are seven official MCP servers you can set up right now in Claude.

### 1. Zapier MCP server

With [Zapier MCP](https://zapier.com/mcp), you can connect Claude to thousands of other apps, all with one MCP server. It's a great way to facilitate secure interactions between Claude and all the other apps you use.

To use Zapier MCP, follow this step-by-step video and take a look at Zapier's article on [how to use Zapier MCP](/blog/zapier-mcp-claude-guide/#how).

You'll notice this process is slightly different from the general setup process I described earlier. To use Zapier MCP, you'll instead navigate to **Settings** > **Integrations** within Claude desktop and then click **+ Add integration**. Name the integration (I went with the highly original "Zapier"), then add the Integration URL from the Zapier MCP setup process.

For a test, I connected Claude with all of Zapier's available Airtable actions. I currently use the [Airtable Web Clipper](https://chromewebstore.google.com/detail/airtable-web-clipper/fehcbmngdgagfalpnfphdhojfdcoblgc?hl=en) Chrome extension to add relevant records to my bases while browsing the web. It's useful, but it can be inflexible. After testing a version of this workflow with Zapier MCP, the experience has me shifting more of these processes over to Claude + Zapier MCP.

Here's what it's like to use, with Claude effectively filling in details I didn't need to explicitly provide.

[Try Zapier MCP](https://zapier.com/mcp)

### 2. GitHub MCP server

You can use the official [GitHub MCP server](https://github.blog/changelog/2025-04-04-github-mcp-server-public-preview/) to connect your AI to GitHub, extracting and analyzing specific data in repositories. For example, you could search repositories and get a list of commits and their details, straight from Claude.

Note that to run the server in a container, you'll need to install and run [Docker](https://www.docker.com/)—this will work on the free plan. (Using a container provides a safe environment for developers to build, test, and use code, providing another level of security for using MCP by protecting your local machine.) You'll also need to create a GitHub Personal Access Token and grant relevant permissions.

I tested the GitHub MCP server by asking about my most regularly active GitHub repositories, and it delivered.

### 3. HubSpot MCP server

While Zapier MCP empowers you to connect with many of your favorite tools in one place, you can also use the official MCP servers provided by the connected apps themselves.

The official [HubSpot MCP server](https://www.npmjs.com/package/@hubspot/mcp-server) is a great example—it facilitates a secure bridge between Claude and your HubSpot data.

Here's how I used it to get updated data about the HubSpot CRM deals I have in progress, without having to log in to my HubSpot account dashboard. So much less context-switching.

There are unofficial MCP servers for other popular CRMs like Salesforce, but for the safest experience, I recommend using Zapier MCP instead.

### 4. Notion MCP server

The [Notion MCP](https://developers.notion.com/docs/mcp) server lets you make updates to your internal knowledge base straight from Claude. If you [organize your life with Notion](/blog/organize-your-life-with-notion/) and use Claude for all your AI needs, this is huge.

I ran a few different tests to understand what works and where the current limitations lie.

In this case, and with multiple tests, Notion didn't quite capture the nuance of what I was looking for in the end result. There were several limitations in terms of what data the MCP actually had access to or actions it could execute. That said, we're still in the early days of MCP, and I anticipate that fine-tuning will make it exponentially more useful over time.

### 5. Supabase MCP server

Tools like [Supabase and Firebase](/blog/supabase-vs-firebase/) are essential for certain [vibe coding projects](/blog/vibe-coding-examples/), but they can be difficult to set up for non-technical users. And when using Supabase specifically, navigating the nuances of SQL can be painful if you don't use it regularly.

The official [Supabase MCP](https://supabase.com/blog/mcp-server) lets you perform database queries and operations using natural language. It's something I wish I knew about (and how to use) when I first started vibe coding because integrating databases and properly setting structure and rules has been a challenging concept to wrap my head around.

Here's an example where I asked it to list my active projects and a list of associated Edge Functions.

If you're more of a Firebase user, there's also an official [Firebase MCP server](https://firebase.google.com/docs/cli/mcp-server) that you can use to access similar tools for database management.

### 6. Apify MCP server

You won't find too many official MCP servers for [web scraping](/blog/web-scraping) because they're based on popular open source libraries, not maintained by enterprise brands or other governing bodies.

But Apify is an exception. Its [Web Scraper MCP](https://apify.com/apify/web-scraper/api/mcp) uses JavaScript to extract structured data from web pages. Note that every time you use the MCP, it expends credits in line with [Apify's pricing](https://apify.com/pricing).

Here's what happened when I asked it to scrape my blog for article URLs, page titles, and a list of subheadings.

Navigating the web and extracting the most important information from websites can be tricky without the right approach, so this is a useful tool to add to an AI workflow.

### 7. Pinecone MCP server

If the phrase [vector embeddings](/blog/vector-embeddings/) means something to you, you might want to get to know the [Pinecone MCP server](https://docs.pinecone.io/guides/operations/mcp-server).

You can use it to do everything from interfacing directly with Pinecone documentation to accessing important account and index details. It can also provide a method to search your vector database records in an index based on a text prompt.

Here's an example of how Pinecone's MCP tools helped me investigate a query without leaving Claude.

## Start using MCP with all your favorite apps

Integrating Claude with MCP servers isn't as complicated as it may sound. Sure, it's a little intimidating at first, but the juice is worth the squeeze. The easiest way to get started is to add [Zapier MCP](https://zapier.com/mcp), so you can access your entire tech stack straight from Claude.

[Try Zapier MCP](https://zapier.com/mcp)

**Related reading:**

* [How to use Zapier MCP to create meetings from a prompt](/blog/create-meetings-with-zapier-mcp/)
* [Keep Google Sheets updated automatically with Zapier MCP](/blog/google-sheets-with-zapier-mcp/)
* [Send emails from a prompt with Zapier MCP](/blog/send-emails-with-zapier-mcp/)
* [What is Claude Cowork?](/blog/claude-cowork)

Get productivity tips delivered straight to your inbox

We’ll email you 1-3 times per week—and never share your information.

[![Maddy Osman picture](https://images.ctfassets.net/lzny33ho1g45/3ms4zH20KYBZkFUWm2rEtB/572e6c25bc61fb67ab8f3a214954e08c/maddy-osman-headshot.png)

Maddy Osman

Maddy Osman is the founder of The Blogsmith, a content agency specializing in B2B technology brands, a content operations consultant, and the bestselling author of "Writing for Humans and Robots: The New Rules of Content Style."](/blog/author/maddy-osman)

**tags**



[* Artificial intelligence (AI)](/blog/tags/artificial-intelligence)

**mentioned apps**



[* Anthropic (Claude)](/blog/apps/anthropic-claude)

## Related articles

* [![The AI Guardrails by Zapier logo against a dark green grid](https://images.ctfassets.net/lzny33ho1g45/6gDIZ6HkKgVGB2yYOEWZPz/f43ad5bfd0de63c31258721539cc8732/Hero.jpg?fm=jpg&q=31&fit=thumb&w=896)](/blog/ai-guardrails-guide/)

  [Zapier feature guides](/blog/all-articles/zapier-feature-guides)[AI Guardrails: Add safety and compliance checks to your workflows

  AI Guardrails: Add safety and compliance...](/blog/ai-guardrails-guide/)
* [Business tips](/blog/all-articles/business-tips)[AI frameworks: The building blocks of business intelligence

  AI frameworks: The building blocks of...](/blog/ai-frameworks/)
* [App tips](/blog/all-articles/app-tips)[70+ AI art styles to use in your AI prompts

  70+ AI art styles to use in your AI prompts](/blog/ai-art-styles/)
* [App tips](/blog/all-articles/app-tips)[OpenAI models: Every model (including GPT-5.4) and what it's best for

  OpenAI models: Every model (including...](/blog/openai-models/)
* [Product news](/blog/all-articles/product-news)[Inline Formulas: Instantly transform data exactly where you need it

  Inline Formulas: Instantly transform data...](/blog/transform-data-with-inline-formulas/)
* [Zapier feature guides](/blog/all-articles/zapier-feature-guides)[Which AI models can you automate on Zapier? (GPT 5.4 mini, Opus 4.6, and more)

  Which AI models can you automate on Zapier?...](/blog/ai-models-on-zapier/)
* [Automation inspiration](/blog/all-articles/automation-inspiration)[How to automate ChatGPT (GPT-5.4 nano, GPT-5.4 mini, and more)

  How to automate ChatGPT (GPT-5.4 nano,...](/blog/automate-chatgpt/)
* [App tips](/blog/all-articles/app-tips)[How to use Fellow to record meetings without compromising your data

  How to use Fellow to record meetings without...](/blog/fellow-features/)

## Improve your productivity automatically. Use Zapier to get your apps working together.

[Sign up](/sign-up)

[See how Zapier works](/how-it-works)

![A Zap with the trigger 'When I get a new lead from Facebook,' and the action 'Notify my team in Slack'](https://res.cloudinary.com/zapier-media/image/upload/f_auto/q_auto/v1667941775/Blog/Generic/backgroundArtwork.png)
