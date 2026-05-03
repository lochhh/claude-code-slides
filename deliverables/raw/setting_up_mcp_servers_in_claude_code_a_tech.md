# Setting Up MCP Servers in Claude Code: A Tech Ritual for ... - Reddit

**Type:** community
**URL:** https://www.reddit.com/r/ClaudeAI/comments/1jf4hnt/setting_up_mcp_servers_in_claude_code_a_tech/
**Topic:** MCP Servers
**Published:** unknown

## Content

# Setting Up MCP Servers in Claude Code: A Tech Ritual for the Quietly Desperate : r/ClaudeAI
[Skip to main content](https://www.reddit.com/r/ClaudeAI/comments/1jf4hnt/setting_up_mcp_servers_in_claude_code_a_tech/#main-content)Setting Up MCP Servers in Claude Code: A Tech Ritual for the Quietly Desperate : r/ClaudeAI

Open menu Open navigation[](https://www.reddit.com/)Go to Reddit Home

r/ClaudeAI

Get App Get the Reddit app [Log In](https://www.reddit.com/login/)Log in to Reddit

Expand user menu Open settings menu

[![Image 1](https://styles.redditmedia.com/t5_7t8hvt/styles/communityIcon_97yk0vsmp4cf1.png?width=96&height=96&frame=1&auto=webp&crop=96%3A96%2Csmart&s=de73db6eb89604488f2125b81c2080f7a14c2a38) Go to ClaudeAI](https://www.reddit.com/r/ClaudeAI/)

[r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/)•1y ago

[mr_undeadpickle77](https://www.reddit.com/user/mr_undeadpickle77/)

# Setting Up MCP Servers in Claude Code: A Tech Ritual for the Quietly Desperate

[Feature: Claude Code tool](https://www.reddit.com/r/ClaudeAI/?f=flair_name%3A%22Feature%3A%20Claude%20Code%20tool%22)

## After much trial and error I finally got functioning MCP servers in Claude Code albeit with slightly less will to live.

### What are MCP Servers?

They're digital prosthetics that give Claude arms and legs to crawl around your computer with. Less poetically: extensions that let it do stuff beyond generating code you'll never actually use.

### The Tools (★ = Requires API Key)

*   **Sequential Thinking**: Helps Claude solve problems step‑by‑step

*   **Filesystem**: Lets Claude rummage through the folders you allow

*   **Playwright**: Modern multi‑browser automation

*   **Puppeteer**: Chrome‑only (deprecated)

*   **Web Fetching**: Grabs content from websites

*   **Browser Tools** (Chrome DevTools Integration): Capture and analyze browser data through a Chrome extension

*   **★ Brave Search**: Web searching capabilities

*   **★ Firecrawl**: Advanced web scraping

* * *

## 🏃‍♂️ One‑Command Installation (The "I Don't Have Time For This" Version)

Copy **everything** in the block, paste into a macOS/Linux terminal, and hit ↵.

bash <<'EOF'
echo "🔧  Installing Claude MCP servers (latest versions)…"

# Sequential Thinking — Claude's chain‑of‑thought engine
claude mcp add sequential-thinking -s user \
  -- npx -y @modelcontextprotocol/server-sequential-thinking || true

# Filesystem — give Claude access to local folders
claude mcp add filesystem -s user \
  -- npx -y @modelcontextprotocol/server-filesystem \
     ~/Documents ~/Desktop ~/Downloads ~/Projects || true

# Playwright — modern multi‑browser automation
claude mcp add playwright -s user \
  -- npx -y @playwright/mcp-server || true

# Puppeteer — Chrome‑only (deprecated but still works)
claude mcp add puppeteer -s user \
  -- npx -y @modelcontextprotocol/server-puppeteer || true

# Fetch — simple HTTP GET/POST
claude mcp add fetch -s user \
  -- npx -y @kazuph/mcp-fetch || true

# Browser‑Tools — DevTools logs, screenshots, etc.
claude mcp add browser-tools -s user \
  -- npx -y @agentdeskai/browser-tools-mcp || true

echo "--------------------------------------------------"
echo "✅  MCP registration finished."
echo ""
echo "🔴  To enable Browser‑Tools, run this in a *second* terminal and leave it open:"
echo "    npx -y @agentdeskai/browser-tools-server"
echo "--------------------------------------------------"
claude mcp list
EOF
Save this as `install-mcp-servers.sh`, make it executable (`chmod +x install-mcp-servers.sh`), and run it while questioning your life choices.

Windows users: you'll need a `.bat` file instead. Good luck with that!

## # Essential MCP Servers (Individual Installation)

### Sequential Thinking

claude mcp add sequential-thinking -s user \
  -- npx -y @modelcontextprotocol/server-sequential-thinking
Lets Claude actually think through problems instead of making things up with confidence.

### Filesystem Access (update paths as desired)

claude mcp add filesystem -s user \
  -- npx -y @modelcontextprotocol/server-filesystem \
     ~/Documents ~/Desktop ~/Downloads ~/Projects
Give Claude access to your files.

### Playwright (multi‑browser automation)

claude mcp add playwright -s user \
  -- npx -y @playwright/mcp
### Puppeteer (deprecated but still works)

claude mcp add puppeteer -s user \
  -- npx -y @modelcontextprotocol/server-puppeteer
Watch in existential dread as your browser operates itself.

### Web Fetching

claude mcp add fetch -s user \
  -- npx -y @kazuph/mcp-fetch
Grabs content from websites.

### Browser Tools

Gives Claude access to your browser's console logs, network traffic, and the ability to run performance/accessibility audits.

**Step 1:** Install the Chrome extension – download from the [releases page](https://github.com/AgentDeskAI/browser-tools-mcp/releases) and load it via Chrome’s extension manager. **Step 2:** Start the middleware server (keep this terminal open)

npx -y @agentdeskai/browser-tools-server@1.2.1
**Step 3:** Add the MCP server to Claude Code (in a separate terminal)

claude mcp add browser-tools -s user \
  -- npx -y @agentdeskai/browser-tools-mcp@1.2.1
**Step 4:** Open Chrome DevTools (F12) and find the _BrowserTools_ tab.

### ★ Brave Search (Requires API Key)

# Replace YOUR_API_KEY_HERE with your actual Brave Search API key
claude mcp add brave-search -s user \
  -- env BRAVE_API_KEY=YOUR_API_KEY_HERE \
     npx -y @modelcontextprotocol/server-brave-search
Let Claude search the web and bring back results.

### ★ Firecrawl (Advanced Web Scraping — Requires API Key)

# Replace fc-YOUR_API_KEY with your actual Firecrawl API key
claude mcp add firecrawl -s user \
  -- env FIRECRAWL_API_KEY=fc-YOUR_API_KEY \
     npx -y firecrawl-mcp
For when you need to scrape websites with industrial‑grade efficiency and minimal respect for robots.txt.

* * *

### # The -s user vs -s local Thing

*   `-s user`: Makes these tools available globally

*   `-s local`: Only works in your current directory

### # Troubleshooting

*   **Windows issues:** prepend `cmd /c` before npx commands

*   **Timeout errors:**`MCP_TIMEOUT=10000 claude`

*   **Connection problems:** Type `/mcp` in Claude Code to see which servers are napping

*   **Filesystem access:** Double‑check your paths

That's it. Save yourself the four hours of my life I'll never get back.

PS – Yes, this was written mostly with the help of Claude.

EDIT: Apparently there were some stupid Reddit formatting issues. It converted the "@" to "u/", I'm such a noob, sorry! I updated the script to include playwright which is a pretty good alternative to puppeteer. Thanks all for pointing out my numerous flaws.

Share

New to Reddit? 
Create your account and connect with a world of communities.

 Continue with Email 

 Continue With Phone Number 

By continuing, you agree to our[User Agreement](https://www.redditinc.com/policies/user-agreement)and acknowledge that you understand the[Privacy Policy](https://www.redditinc.com/policies/privacy-policy). 

# Related Answers Section

 Related Answers 

[Setting up MCP servers in Claude Code](https://www.reddit.com/answers/0d125eae-f89d-4ab2-a1eb-e12c91125674/?q=Setting+up+MCP+servers+in+Claude+Code&source=PDP)

[Best practices for using ClaudeAI effectively](https://www.reddit.com/answers/4993f42f-3f37-4dd2-abbc-9fe7162ae4a3/?q=Best+practices+for+using+ClaudeAI+effectively&source=PDP)

[Comparing ClaudeAI with other AI tools](https://www.reddit.com/answers/d1437ca4-860b-43cd-91ef-dd450500c54c/?q=Comparing+ClaudeAI+with+other+AI+tools&source=PDP)

[Common challenges when using Claude Code](https://www.reddit.com/answers/4921e09f-f3f7-47db-97be-db79a085b26b/?q=Common+challenges+when+using+Claude+Code&source=PDP)

![Image 2: hp](https://emoji.redditmedia.com/jud91dthlhcf1_t5_7t8hvt/hp)

![Image 3: hp](https://emoji.redditmedia.com/jud91dthlhcf1_t5_7t8hvt/hp)

[Check Claude service status.](http://status.claude.com/)

 Public 

Anyone can view, post, and comment to this community

0 0

## Top Posts

*   [Reddit reReddit: Top posts of March 19, 2025 * * *](https://www.reddit.com/posts/2025/march-19-1/global/)
*   [Reddit reReddit: Top posts of March 2025 * * *](https://www.reddit.com/posts/2025/march/global/)
*   [Reddit reReddit: Top posts of 2025 * * *](https://www.reddit.com/posts/2025/global/)

[Reddit Rules](https://www.redditinc.com/policies/content-policy)[Privacy Policy](https://www.reddit.com/policies/privacy-policy)[User Agreement](https://www.redditinc.com/policies/user-agreement)[Your Privacy Choices](https://support.reddithelp.com/hc/articles/43980704794004)[Accessibility](https://support.reddithelp.com/hc/sections/38303584022676-Accessibility)[Reddit, Inc. © 2026. All rights reserved.](https://redditinc.com/)

Expand Navigation Collapse Navigation

*   &nbsp; 
*   &nbsp; 
*   &nbsp; 

* * *

* * *

*   RESOURCES 

*   [About Reddit](https://www.redditinc.com/)
*   [Advertise](https://ads.reddit.com/register?utm_source=web3x_consumer&utm_name=left_nav_cta)
*   [Developer Platform](https://developers.reddit.com/?utm_source=reddit&utm_medium=left_nav_resources)
*   [Reddit Pro BETA](https://www.reddit.com/reddit-pro?utm_source=reddit&utm_medium=left_nav_resources)
*   [Help](https://support.reddithelp.com/hc?utm_source=reddit&utm_medium=footer&utm_campaign=evergreen)
*   [Blog](https://redditblog.com/)
*   [Careers](https://www.redditinc.com/careers)
*   [Press](https://www.redditinc.com/press)

* * *

*   [Best of Reddit](https://www.reddit.com/posts/2026/global/)

* * *

*   [Reddit Rules](https://www.redditinc.com/policies/content-policy)
*   [Privacy Policy](https://www.reddit.com/policies/privacy-policy)
*   [User Agreement](https://www.redditinc.com/policies/user-agreement)
*   [Your Privacy Choices](https://support.reddithelp.com/hc/articles/43980704794004)
*   [Accessibility](https://support.reddithelp.com/hc/sections/38303584022676-Accessibility)

[Reddit, Inc. © 2026. All rights reserved.](https://redditinc.com/)

![Image 4](https://id.rlcdn.com/472486.gif)
