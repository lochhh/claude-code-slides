# Automatic context compaction | Claude Cookbook

**Type:** article
**URL:** https://platform.claude.com/cookbook/tool-use-automatic-context-compaction
**Topic:** Context Management
**Published:** unknown

## Content

# Automatic context compaction

Manage context limits in long-running agentic workflows by automatically compressing conversation history.

![Pedram Navid](https://avatars.githubusercontent.com/u/1045990)

# Automatic Context Compaction

Long-running agentic tasks can often exceed context limits. Tool heavy workflows or long conversations quickly consume the token context window. In [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), we discussed how managing context can help avoid performance degradation and context rot.

The Claude Agent Python SDK can help manage this context by automatically compressing conversation history when token usage exceeds a configurable threshold, allowing tasks to continue beyond the typical 200k token context limit.

In this cookbook, we'll demonstrate context compaction through an **agentic customer service workflow**. Imagine you've built an AI customer service agent tasked with processing a queue of support tickets. For each ticket, you must classify the issue, search the knowledge base, set priority, route to the appropriate team, draft a response, and mark it complete. As you process ticket after ticket, the conversation history fills with classifications, knowledge base searches, and drafted responses—quickly consuming thousands of tokens.

## What is Context Compaction?

When building agentic workflows with tool use, conversations can grow very large as the agent iterates on complex tasks. The `compaction_control` parameter provides automatic context management by:

`compaction_control`
`<summary></summary>`

## By the end of this cookbook, you'll be able to:

## Prerequisites

Before following this guide, ensure you have:

**Required Knowledge**

**Required Tools**

**Using Opus 4.6?** We recommend using [server-side compaction](https://docs.anthropic.com/en/docs/build-with-claude/compaction), which handles context management automatically without any SDK-level configuration.

This cookbook covers **SDK-based compaction**, which is useful if you're using an older model or want to use a different (cheaper) model for summarization.

## Setup

First, install the required dependencies:

`# %pip install -qU anthropic python-dotenv`

Note: Ensure your .env file contains:

`ANTHROPIC_API_KEY=your_key_here`

`ANTHROPIC_API_KEY=your_key_here`

Load your environment variables and configure the client. We also load a helper utility to visualize Claude message responses.

`from dotenv import load_dotenv
 
load_dotenv()
 
MODEL = "claude-sonnet-4-6"`

## Setting the Stage

In [utils/customer\_service\_tools.py](https://github.com/anthropics/claude-cookbooks/blob/main/tool_use/utils/customer_service_tools.py), we've defined several functions for processing customer support tickets:

`get_next_ticket()`
`classify_ticket(ticket_id, category)`
`search_knowledge_base(query)`
`set_priority(ticket_id, priority)`
`route_to_team(ticket_id, team)`
`draft_response(ticket_id, response_text)`
`mark_complete(ticket_id)`

For a customer service agent, these tools enable processing tickets systematically. Each ticket requires classification, research, prioritization, routing, and response drafting. When processing 20-30 tickets in sequence, the conversation history fills with tool results from every classification, every knowledge base search, and every drafted response, causing linear token growth.

The `beta_tool` decorator is used on the tools to make them accessible to the Claude agent. The decorator extracts the function arguments and docstring and provides these to Claude as tool metadata.

`beta_tool`
`import anthropic
from anthropic import beta_tool
 
@beta_tool
def get_next_ticket() -> dict:
 """Retrieve the next unprocessed support ticket from the queue."""
 ...`
`import anthropic
from utils.customer_service_tools import (
 classify_ticket,
 draft_response,
 get_next_ticket,
 initialize_ticket_queue,
 mark_complete,
 route_to_team,
 search_knowledge_base,
 set_priority,
)
 
client = anthropic.Anthropic()
 
tools = [
 get_next_ticket,
 classify_ticket,
 search_knowledge_base,
 set_priority,
 route_to_team,
 draft_response,
 mark_complete,
]`

## Baseline: Running Without Compaction

Let's start with a realistic customer service scenario: Processing a queue of support tickets.

The workflow looks like this:

**For Each Ticket:**

`get_next_ticket()`

**The Challenge**: With 5 tickets in the queue, and each requiring 7 tool calls, Claude will make 35 or more tool calls. The results from each step including classification knowledge base search, and drafted responses accumulate in the conversation history. Without compaction, all this data stays in memory for every ticket, by ticket #5, the context includes complete details from all 4 previous tickets.

Let's run this workflow **without compaction** first and observe what happens:

`from anthropic.types.beta import BetaMessageParam
 
num_tickets = 5
initialize_ticket_queue(num_tickets)
 
messages: list[BetaMessageParam] = [
 {
 "role": "user",
 "content": f"""You are an AI customer service agent. Your task is to process support tickets from a queue.
 
For EACH ticket, you must complete ALL these steps:
 
1. **Fetch ticket**: Call get_next_ticket() to retrieve the next unprocessed ticket
2. **Classify**: Call classify_ticket() to categorize the issue (billing/technical/account/product/shipping)
3. **Research**: Call search_knowledge_base() to find relevant information for this ticket type
4. **Prioritize**: Call set_priority() to assign priority (low/medium/high/urgent) based on severity
5. **Route**: Call route_to_team() to assign to the appropriate team
6. **Draft**: Call draft_response() to create a helpful customer response using KB information
7. **Complete**: Call mark_complete() to finalize this ticket
8. **Continue**: Immediately fetch the next ticket and repeat
 
IMPORTANT RULES:
- Process tickets ONE AT A TIME in sequence
- Complete ALL 7 steps for each ticket before moving to the next
- Keep fetching and processing tickets until you get an error that the queue is empty
- There are {num_tickets} tickets total - process all of them
- Be thorough but efficient
 
Begin by fetching the first ticket.""",
 }
]
 
total_input = 0
total_output = 0
turn_count = 0
 
runner = client.beta.messages.tool_runner(
 model=MODEL,
 max_tokens=4096,
 tools=tools,
 messages=messages,
)
 
for message in runner:
 messages_list = list(runner._params["messages"])
 turn_count += 1
 total_input += message.usage.input_tokens
 total_output += message.usage.output_tokens
 print(
 f"Turn {turn_count:2d}: Input={message.usage.input_tokens:7,} tokens | "
 f"Output={message.usage.output_tokens:5,} tokens | "
 f"Messages={len(messages_list):2d} | "
 f"Cumulative In={total_input:8,}"
 )
 
print(f"\n{'=' * 60}")
print("BASELINE RESULTS (NO COMPACTION)")
print(f"{'=' * 60}")
print(f"Total turns: {turn_count}")
print(f"Input tokens: {total_input:,}")
print(f"Output tokens: {total_output:,}")
print(f"Total tokens: {total_input + total_output:,}")
print(f"{'=' * 60}")`

Now that we have our baseline, we have a better picture of how context grows without compaction. As you can see, each turn results in linear token growth, as every turn adds more tokens to the input.

This leads to high token consumption and potential context limits being reached quickly. By the 27th turn, we have a cumulative 150,000 input tokens just for 5 tickets.

Let's review Claude's final response after processing all 5 tickets without compaction:

`print(message.content[-1].text)`

### Understanding the Problem

In the baseline workflow above, Claude had to:

**Why This Happens**:

**What We Actually Need**: After completing Ticket A, we only need a **brief summary** (ticket resolved, category, priority) - not the full classification result, knowledge base search, and complete drafted response. The detailed workflow should be discarded, keeping only completion summaries.

Let's see how automatic context compaction solves this problem.

## Enabling Automatic Context Compaction

Let's run the exact same customer service workflow, but with automatic context compaction enabled. We simply add the `compaction_control` parameter to our tool runner.

`compaction_control`

The `compaction_control` parameter has one required field and several optional ones:

`compaction_control`
`enabled`
`context_token_threshold`
`model`
`summary_prompt`

For this customer service workflow, we'll use a **5,000 token threshold**. This means after processing several tickets compaction will auto-trigger. This allows Claude to:

This mimics how a real support agent works: resolve the ticket, document it briefly, move to the next case.

`# Re-initialize queue and run with compaction
initialize_ticket_queue(num_tickets)
 
total_input_compact = 0
total_output_compact = 0
turn_count_compact = 0
compaction_count = 0
prev_msg_count = 0
 
runner = client.beta.messages.tool_runner(
 model=MODEL,
 max_tokens=4096,
 tools=tools,
 messages=messages,
 compaction_control={
 "enabled": True,
 "context_token_threshold": 5000,
 },
)
 
for message in runner:
 turn_count_compact += 1
 total_input_compact += message.usage.input_tokens
 total_output_compact += message.usage.output_tokens
 messages_list = list(runner._params["messages"])
 curr_msg_count = len(messages_list)
 
 if curr_msg_count < prev_msg_count:
 # We can identify compaction when the message count decreases
 compaction_count += 1
 
 print(f"\n{'=' * 60}")
 print(f"🔄 Compaction occurred! Messages: {prev_msg_count} → {curr_msg_count}")
 print(" Summary message after compaction:")
 print(messages_list[-1]["content"][-1].text) # type: ignore
 print(f"\n{'=' * 60}")
 
 prev_msg_count = curr_msg_count
 print(
 f"Turn {turn_count_compact:2d}: Input={message.usage.input_tokens:7,} tokens | "
 f"Output={message.usage.output_tokens:5,} tokens | "
 f"Messages={len(messages_list):2d} | "
 f"Cumulative In={total_input_compact:8,}"
 )
 
print(f"\n{'=' * 60}")
print("OPTIMIZED RESULTS (WITH COMPACTION)")
print(f"{'=' * 60}")
print(f"Total turns: {turn_count_compact}")
print(f"Compactions: {compaction_count}")
print(f"Input tokens: {total_input_compact:,}")
print(f"Output tokens: {total_output_compact:,}")
print(f"Total tokens: {total_input_compact + total_output_compact:,}")
print(f"{'=' * 60}")`

With automatic context compaction enabled, we can see that our token usage per turn does not grow linearly, but is reduced after each compaction event. There were two compaction events during the processing of tickets, and the follow turn shows a reduction in total token usage.

Compared to the baseline version, we only used 79,000 tokens. We've also printed out the summary messages generated after each compaction event, showing how Claude effectively condensed prior ticket details into summaries.

Let's look at the final response after processing all 5 tickets with compaction enabled.

`print(message.content[-1].text)`

### Comparing Results

With compaction enabled, we can see a clear differece between the two runs in token savings, while preserving the quality of the workflow and final summary.

Here's what changed with automatic context compaction:

**Context resets after several tickets** - When processing 5-7 tickets generates 5k+ tokens of tool results, the SDK automatically:

`<summary></summary>`

**Input tokens stay bounded** - Instead of accumulating to 100k+ as we process more tickets, input tokens reset after each compaction. When processing Ticket #5, we're NOT carrying the full tool results from Tickets #1-4.

**Task completes successfully** - The workflow continues smoothly through all tickets without hitting context limits

**Quality is preserved** - The summaries retain critical information:

All tickets are still properly classified, prioritized, routed, and responded to.

**Natural workflow** - This mirrors how real support agents work: resolve a ticket, document it briefly in the system, close it, move to the next one. You don't keep every knowledge base article and full response draft open while working on new tickets.

Let's visualize the token savings:

`# Compare baseline vs compaction
print("=" * 70)
print("TOKEN USAGE COMPARISON")
print("=" * 70)
print(f"{'Metric':<30} {'Baseline':<20} {'With Compaction':<20}")
print("-" * 70)
print(f"{'Input tokens:':<30} {total_input:>19,} {total_input_compact:>19,}")
print(f"{'Output tokens:':<30} {total_output:>19,} {total_output_compact:>19,}")
print(
 f"{'Total tokens:':<30} {total_input + total_output:>19,} {total_input_compact + total_output_compact:>19,}"
)
print(f"{'Compactions:':<30} {'N/A':>19} {compaction_count:>19}")
print("=" * 70)
 
# Calculate savings
token_savings = (total_input + total_output) - (total_input_compact + total_output_compact)
savings_percent = (
 (token_savings / (total_input + total_output)) * 100 if (total_input + total_output) > 0 else 0
)
 
print(f"\n💰 Token Savings: {token_savings:,} tokens ({savings_percent:.1f}% reduction)")`

## How Compaction Works Under the Hood

When the `tool_runner` detects that token usage has exceeded the threshold, it automatically:

`tool_runner`
`<summary></summary>`

## Customizing Compaction Configuration

You can customize how compaction works to fit your specific use case. Here are the key configuration options:

### Adjusting the Threshold

The `context_token_threshold` determines when compaction triggers:

`context_token_threshold`
`compaction_control={
 "enabled": True,
 "context_token_threshold": 5000, # Compact after processing 5-7 tickets
}`

The threshold should not be set too low, otherwise the summary itself could trigger a compaction. We set a threshold of 5,000 tokens for demonstration purposes, but in practice, experiment with different settings to find what works best for your workflow.

Here some general guidelines:

**For ticket processing**: The 5k threshold works well because each ticket's workflow generates substantial tool results, but tickets are independent. After resolving Ticket A, you don't need its detailed KB searches when processing Ticket B.

### Using a Different Model for Summarization

You can also use a faster/cheaper model for generating summaries:

`compaction_control={
 "enabled": True,
 "model": "claude-haiku-4-5", # Use Haiku for cost-effective summaries
}`

### Custom Summary Prompts

You can provide a custom prompt to guide how summaries are generated. This is especially useful for customer service workflows where you need to preserve specific types of information.

For example, we could define a custom prompt based on our requirements:

`compaction_control={
 "enabled": True,
 "summary_prompt": """You are processing customer support tickets from a queue.
 
Create a focused summary that preserves:
 
1. **COMPLETED TICKETS**: For each ticket you've fully processed:
 - Ticket ID and customer name
 - Issue category and priority assigned
 - Team routed to
 - Brief outcome
 
2. **PROGRESS STATUS**: 
 - How many tickets you've completed
 - Approximately how many remain in the queue
 
3. **NEXT STEPS**: Continue processing the next ticket
 
Format with clear sections and wrap in <summary></summary> tags."""
}`

## Compaction Without Tools: Simple Chat Loop

While the examples above focus on tool-heavy agentic workflows, context compaction is also valuable for **simple conversational applications** where users drive the conversation.

**Note:** The `compaction_control` parameter demonstrated above works with `tool_runner` for agentic workflows with tools. For simple chat applications without tools, you'll implement compaction manually using the same principles.

`compaction_control`
`tool_runner`

Consider a chat application where users are having extended conversations with Claude—discussing complex topics, iterating on ideas, or working through problems. As the conversation grows, you face the same context accumulation challenges.

**The Difference**: Instead of tool use triggering token growth, it's the back-and-forth conversation itself. Each exchange adds messages to the history:

Without compaction, by turn 50 you're sending the entire conversation history (all 50 exchanges) on every API call.

**The Solution**: Implement compaction manually in your chat loop using the same pattern:

Let's see how to implement this:

`#!/usr/bin/env python3
"""
Simple Compaction Example - User-Driven Chat Loop
 
This shows the basic pattern for a chat application with compaction.
No tools required - just a simple loop where the user drives continuation.
"""
 
# Configuration
COMPACTION_THRESHOLD = 3000 # Compact when tokens exceed this (low for demo purposes)
 
# Structured summarization prompt for compaction
SUMMARY_PROMPT = """You have been working on the task described above but have not yet completed it. Write a continuation summary that will allow you (or another instance of yourself) to resume work efficiently in a future context window where the conversation history will be replaced with this summary. Your summary should be structured, concise, and actionable. Include:
 
1. **Task Overview**
 - The user's core request and success criteria
 - Any clarifications or constraints they specified
 
2. **Current State**
 - What has been completed so far
 - Files created, modified, or analyzed (with paths if relevant)
 - Key outputs or artifacts produced
 
3. **Important Discoveries**
 - Technical constraints or requirements uncovered
 - Decisions made and their rationale
 - Errors encountered and how they were resolved
 - What approaches were tried that didn't work (and why)
 
4. **Next Steps**
 - Specific actions needed to complete the task
 - Any blockers or open questions to resolve
 - Priority order if multiple steps remain
 
5. **Context to Preserve**
 - User preferences or style requirements
 - Domain-specific details that aren't obvious
 - Any promises made to the user
 
Be concise but complete—err on the side of including information that would prevent duplicate work or repeated mistakes.
 Write in a way that enables immediate resumption of the task.
 
Wrap your summary in <summary></summary> tags."""
 
# Message history
messages = []
 
print("Chat with Claude (type 'quit' to exit, or just hit Enter to continue)")
print("This is a demonstration - try having a conversation and watch compaction trigger")
print("=" * 60)
 
# Simulate a conversation for demo purposes
demo_messages = [
 "Help me understand how Python decorators work",
 "Can you show me an example with a timing decorator?",
 "How would I make a decorator that takes arguments?",
]
 
for user_input in demo_messages:
 print(f"\nYou: {user_input}")
 
 # Add user message
 messages.append({"role": "user", "content": user_input})
 
 # Get Claude's response
 response = client.messages.create(
 model=MODEL,
 max_tokens=2048,
 messages=messages,
 )
 
 messages.append(
 {
 "role": "assistant",
 "content": response.content,
 }
 )
 
 print("\nClaude: ", end="")
 for block in response.content:
 if block.type == "text":
 print(f"{block.text[:300]} ...")
 
 # Check if we should compact
 usage = response.usage
 
 # Calculate total tokens (includes cache tokens)
 total_input_tokens = (
 usage.input_tokens
 + (usage.cache_creation_input_tokens or 0)
 + (usage.cache_read_input_tokens or 0)
 )
 total_tokens = total_input_tokens + usage.output_tokens
 
 cache_info = ""
 if usage.cache_creation_input_tokens or usage.cache_read_input_tokens:
 cache_info = f" (cache: {usage.cache_creation_input_tokens or 0} write + {usage.cache_read_input_tokens or 0} read)"
 
 print(
 f"\n[Tokens: {total_input_tokens} in{cache_info} + {usage.output_tokens} out = {total_tokens} total]"
 )
 
 if total_tokens > COMPACTION_THRESHOLD:
 print(f"\n{'=' * 60}")
 print(f"🔄 Compacting conversation... {len(messages)} messages → ", end="", flush=True)
 
 # Get summary using structured prompt
 summary_response = client.messages.create(
 model=MODEL,
 max_tokens=4096,
 messages=messages + [{"role": "user", "content": SUMMARY_PROMPT}],
 )
 
 summary_text = "".join(
 block.text for block in summary_response.content if block.type == "text"
 )
 
 # Replace history with summary
 messages = [{"role": "user", "content": summary_text}]
 
 print("1 message")
 print(f"{'=' * 60}\n")
 
print(f"Final conversation messages: {messages[-1].get('content')}")
 
print("\nDemo complete! In a real application, this loop would continue with user input.")`

### Understanding the Chat Loop Pattern

The example above demonstrates manual compaction in a conversational context. Here's how it works:

**Key Components**:

**When to Use This Pattern**:

**Key Differences from Tool Runner**:

| Aspect | Tool Runner (Automatic) | Chat Loop (Manual) |
| --- | --- | --- |
| **Trigger** | Automatic when threshold reached | You implement threshold check |
| **Summary** | SDK handles summary request | You make explicit API call |
| **History Management** | SDK replaces messages | You manually replace list |
| **Use Case** | Agentic workflows with tools | User-driven conversations |

**Production Considerations**:

This pattern gives you full control over when and how compaction happens, making it ideal for conversational applications where the SDK's automatic tool-runner compaction isn't available.

## Limitations and Considerations

While automatic context compaction is powerful, there are important limitations to understand:

### Server-Side Sampling Loops

**Current Limitation**: Compaction does not work optimally with server-side sampling loops, such as server-side web search tools.

**Why**: Cache tokens accumulate across sampling loops, which can trigger compaction prematurely based on cached content rather than actual conversation history.

This feature works best with:

### Information Loss

**Trade-off**: Summaries inherently lose some information. While Claude is good at identifying key points, some details will be compressed or omitted.

**In ticket processing**:

This is usually acceptable, you don't need every KB article and full response text in perpetuity, just the completion records.

**Mitigation**:

### When NOT to Use Compaction

Avoid compaction for:

### When TO Use Compaction

Compaction is ideal for:

**Ticket processing is a perfect use case** because:

## Summary

Automatic context compaction is a powerful feature that enables long-running agentic workflows to exceed typical context limits. In this cookbook, we've explored compaction through a customer service ticket processing workflow.

### Next Steps

Try implementing compaction in your own workflows:

For more on effective context management, see [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
