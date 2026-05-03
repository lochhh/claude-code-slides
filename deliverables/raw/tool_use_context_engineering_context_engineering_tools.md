# Context engineering: memory, compaction, and tool clearing

**Type:** article
**URL:** https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools
**Topic:** Context Management
**Published:** unknown

## Content

# Context engineering: memory, compaction, and tool clearing

Compare context engineering strategies for long-running agents and learn when each applies, what it costs, and how they compose.

![Isabella He](https://avatars.githubusercontent.com/u/247469474?v=4)

# Context Engineering for AI Agents: Memory vs. Compaction vs. Tool Clearing

## Introduction

A common challenge when building long-horizon agents is managing context. Tool results, the model's own reasoning, and user messages all accumulate, and eventually you either hit the token limit or start paying for context that isn't helping anymore. Studies on needle-in-a-haystack style benchmarking have uncovered the concept of [context rot](https://research.trychroma.com/context-rot): as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases. So, even before the hard context limit is reached, the agent may be getting less out of each token.

Our engineering blog on [effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) frames this as a resource problem: context is finite with diminishing marginal returns, and the core discipline is finding the smallest set of high-signal tokens that maximize the likelihood of your desired outcome. There are several levers for this: subagents that isolate work in their own context, programmatic tool calling that keeps large results out of the window entirely, and others.

This cookbook focuses on three: **compaction**, **tool-result clearing**, and **memory**. All three are effective strategies for context engineering, but since they all operate to make the context window more efficient in different ways, they can be hard to distinguish. Understanding those distinctions is what lets you map each tool to the part of your workload it actually helps with. Alongside other core context management strategies like utilizing subagents, these three are crucial for teams building long-running agents to understand. They also all have first-party API support, so you can adopt them without building orchestration infrastructure.

[Claude Code](https://claude.com/product/claude-code) employs multiple of these strategies in production: compaction for long conversations and two complementary memory systems for cross-session persistence. Our API offers first-party implementations of all three: [server-side compaction](https://platform.claude.com/docs/en/build-with-claude/compaction), [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) (which includes tool-result clearing), and the [memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool). This cookbook works through how to think about designing with them: when each one applies, how to configure them, what changes when you use them independently vs. together, and sample use-cases where different combinations make sense.

The examples center on a **long-running research agent**: one that reads a corpus of documents, takes notes, and builds on its findings across multiple sessions. It's a useful test case because it naturally hits all three problems: bulky document reads (clearing), long analytical conversations (compaction), and knowledge that needs to survive between sessions (memory).

### What you'll learn

`clear_tool_uses`
`compaction`
`/memories`

### Prerequisites

To run this notebook, you will need:

`ANTHROPIC_API_KEY`
`.env`
`anthropic`
`python-dotenv`
`matplotlib`
`research_corpus.py`
`CORPUS`

**Running from the cookbooks repo?** Ensure your working directory is `tool_use/context_engineering` before running the notebook.

`tool_use/context_engineering`

## Step 0: Environment Setup

Create a `.env` file in this directory with your Anthropic API key:

`.env`
`ANTHROPIC_API_KEY=your-key-here`
`%%capture
%pip install anthropic python-dotenv matplotlib`
`import json
import os
import tempfile
from collections import namedtuple
from pathlib import Path
 
import anthropic
import matplotlib.pyplot as plt
from dotenv import load_dotenv
 
load_dotenv()
 
if not os.environ.get("ANTHROPIC_API_KEY"):
 raise ValueError("ANTHROPIC_API_KEY not set. Add it to a .env file or export it.")
 
CORPUS_PATH = Path("research_corpus.py")
assert CORPUS_PATH.exists(), (
 f"research_corpus.py not found in {Path.cwd()}. It should be alongside this notebook."
)
 
client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-6"
print(f"anthropic SDK {anthropic.__version__}, model {MODEL}")`
`# Force-reload the corpus module in case this kernel has a stale cached version
import importlib
 
import research_corpus
 
importlib.reload(research_corpus)
from research_corpus import COMPACTION_PROBES, CORPUS
 
# Count tokens via the API (cached in-memory so repeat kernel runs are fast).
_token_cache: dict[str, int] = {}
 
 
def count_tokens(text: str) -> int:
 if text not in _token_cache:
 _token_cache[text] = client.messages.count_tokens(
 model=MODEL, messages=[{"role": "user", "content": text}]
 ).input_tokens
 return _token_cache[text]
 
 
print(f"CORPUS is a dict of {len(CORPUS)} synthetic documents held in Python memory.")
print("When the agent calls read_file, the content is served from this dict and")
print("lands directly in the agent's context window — no disk I/O involved.\n")
_total_tokens = 0
for path, content in CORPUS.items():
 n_tok = count_tokens(content)
 _total_tokens += n_tok
 # Strip the virtual directory prefix for display clarity
 display_name = path.removeprefix("/research/")
 print(f" {display_name:<26} ~{n_tok:>6,} tokens")
print(f"\n Total corpus: ~{_total_tokens:,} tokens")
 
# Sanity check: the corpus should be large enough to push context well past
# 200K in a single read-pass. If this fires, research_corpus.py may be stale.
assert _total_tokens > 250_000, (
 f"Corpus is only {_total_tokens:,} tokens; expected >250K. "
 "Restart the kernel and re-run, or verify research_corpus.py is current."
)`

## The Problem: A Long-Running Research Agent

The agent in this cookbook plays the role of a biology researcher writing a comparative review of model organisms for aging and longevity research. The task is realistic enough to matter: it involves reading through a corpus of review documents (one per organism), extracting comparable facts (lifespan, genetic tractability, translational relevance), taking structured notes, and synthesizing findings across everything read.

This kind of work is where context management starts to bite. Each document is around 40K tokens (narrative plus extensive appendix tables of intervention data), and the task asks the agent to read them in two batches: four high-throughput organisms (C. elegans, Drosophila, yeast, killifish) first, then four low-throughput organisms (mouse, zebrafish, naked mole-rat, rhesus). The two-batch structure is an experimental design choice for this cookbook: it produces a context trajectory that climbs past the compaction trigger on the first batch and past the 200K reference line on the second, so each primitive's effect on the trajectory is visible in the same run. Without context management, the agent's context grows to hundreds of thousands of tokens mid-task. And since the work spans sessions, even a completed run starts the next session with no memory of what was learned.

### The research task

The agent's concrete assignment: compare the model organisms in `/research/` on three dimensions (lifespan and experimental throughput, genetic tractability, and translational relevance to human aging), reading the eight review documents in two batches and taking notes as it goes, then writing a comparative synthesis.

`/research/`

## How the Three APIs Map to the Problem

Each API targets a different kind of context growth. Understanding which kind you're facing is the first step to picking the right tool.

### Conceptually

**Compaction** is the practice of taking a conversation nearing the context window limit, summarizing its contents, and reinitiating with that summary. It aims to distill the context window in a high-fidelity manner so the agent can continue with minimal performance degradation. The art of compaction lies in what to keep versus what to discard: overly aggressive compaction can lose subtle but critical context whose importance only becomes apparent later. The summary preserves architectural decisions, unresolved questions, and key facts while discarding redundant content; it's lossy by design, but handles all context growth, not just tool results. Compaction is a *whole-transcript* operation: user messages, assistant messages, tool calls, tool results, even prior compaction blocks are all flattened into the summary.

**Tool-result clearing**, by contrast, is a *sub-transcript* operation. It walks the message list and surgically replaces `tool_result` content blocks, leaving everything else — user messages, assistant reasoning, the `tool_use` record — untouched. When an agent calls tools, the results become part of the conversation history and count against the context budget on every subsequent turn. Much of that content is re-fetchable: file contents the agent can re-read, API responses it can re-request. Clearing replaces old `tool_result` blocks with a short placeholder, keeping the `tool_use` record so the model still knows it made the call, but dropping the bulky payload. Once a tool has been called deep in the message history, the agent rarely needs to see the raw result again; clearing is one of the safest, lightest-touch ways to recover that space. If the agent does need the data, it just calls the tool again.

`tool_result`
`tool_use`
`tool_result`
`tool_use`

**Memory**, or structured note-taking, is a technique where the agent regularly writes notes persisted outside the context window, then pulls them back in at later times. This provides persistent memory with minimal overhead: the agent tracks progress across complex tasks, maintaining critical context that would otherwise be lost across dozens of tool calls or across context resets. After a reset (a new session, or after compaction), the agent reads its own notes and continues. You implement the storage backend, so you control what's stored and for how long.

Beyond enabling these primitives, it's also important to understand how to implement them most effectively: the default behavior gets you started, but the quality of a compaction summary and the usefulness of what lands in memory both depend on guidance you provide. Each primitive's section below includes a subsection on effective implementation.

### Tactically

| API | Identifier | Beta header | Triggered by | Configurable knobs |
| --- | --- | --- | --- | --- |
| Compaction | `compact_20260112` | `compact-2026-01-12` | Token threshold (server-side, min 50K) | `trigger` (default 150K), `instructions`, `pause_after_compaction` |
| Tool clearing | `clear_tool_uses_20250919` | `context-management-2025-06-27` | Token threshold (server-side) | `trigger` (default 100K), `keep` (default 3 tool uses), `clear_at_least`, `exclude_tools`, `clear_tool_inputs` |
| Memory tool | `memory_20250818` | none (standalone) | The model (it's a tool call) | Client implements: `view`, `create`, `str_replace`, `insert`, `delete`, `rename` |

`compact_20260112`
`compact-2026-01-12`
`trigger`
`instructions`
`pause_after_compaction`
`clear_tool_uses_20250919`
`context-management-2025-06-27`
`trigger`
`keep`
`clear_at_least`
`exclude_tools`
`clear_tool_inputs`
`memory_20250818`
`view`
`create`
`str_replace`
`insert`
`delete`
`rename`

### Mapped to the research agent

For the research agent specifically, the three problems line up cleanly:

A rough mental model for prioritizing: compaction compresses the whole window when it grows too large, clearing drops stale re-fetchable data inside the window, and memory moves information out of the window so it survives across sessions. Each layer adds config to tune and interactions to understand, so it's worth starting with the one that matches the bottleneck you're actually observing.

## The Research Agent

Before exploring each primitive, we set up the agent itself: tool schemas, tool execution, and an agent loop that can be run with or without any context-management configuration. Everything is inline so you can see the full loop.

`# ── Tool schemas ─────────────────────────────────────────────────────────
RESEARCH_TASK = """Compare the model organisms in /research/ on three dimensions:
1. Lifespan and experimental throughput (how fast can you get a lifespan result?)
2. Genetic tractability (what tools exist for manipulation and screening?)
3. Translational relevance (how well do findings transfer to human aging?)
 
Work through the organisms in two batches, recording a note after each
batch before moving on:
 
BATCH 1 (high-throughput models): Read celegans_review.md,
drosophila_review.md, yeast_review.md, and killifish_review.md. Record a
single detailed note covering all four organisms on all three dimensions.
Do not begin Batch 2 until this note is recorded.
 
BATCH 2 (low-throughput models): Read mouse_review.md,
zebrafish_review.md, nmr_review.md, and rhesus_review.md. Record a
single detailed note covering all four organisms on all three
dimensions.
 
After both batches, write a comprehensive comparative synthesis
contrasting the high-throughput and low-throughput models."""
 
BASE_TOOLS: list[dict] = [
 {
 "name": "search_files",
 "description": "Search document filenames and contents for a keyword. Returns matching paths with a short excerpt.",
 "input_schema": {
 "type": "object",
 "properties": {"query": {"type": "string", "description": "Search term"}},
 "required": ["query"],
 },
 },
 {
 "name": "read_file",
 "description": "Read the full content of a document by path.",
 "input_schema": {
 "type": "object",
 "properties": {
 "path": {"type": "string", "description": "e.g. /research/celegans_review.md"}
 },
 "required": ["path"],
 },
 },
 {
 "name": "record_finding",
 "description": "Record a research finding (freeform text). Findings are held for the duration of this session only; they are not persisted across sessions.",
 "input_schema": {
 "type": "object",
 "properties": {"finding": {"type": "string"}},
 "required": ["finding"],
 },
 },
]
 
# The memory tool spec is defined here but only added to the agent's tool
# list when a memory_handler is passed to run_research_session. Baseline
# and clearing/compaction runs do NOT get the memory tool.
MEMORY_TOOL_SPEC = {"type": "memory_20250818", "name": "memory"}
 
SYSTEM_PROMPT = """You are a biology research analyst writing a comparative review of model organisms for aging research.
 
Work systematically: search and read review documents, take notes on key facts (lifespans, genetic tools, translational strengths and caveats), and build a comparative picture.
 
Be concise in your reasoning text; the goal is notes, not essays."""`
`# ── Tool execution ───────────────────────────────────────────────────────
def execute_research_tool(name: str, tool_input: dict, notes: list[str]) -> str:
 if name == "search_files":
 query = tool_input.get("query", "").lower()
 if not query:
 return "Error: query is required."
 hits: list[str] = []
 for path, content in CORPUS.items():
 if query in path.lower() or query in content.lower():
 for line in content.split("\n"):
 if query in line.lower():
 hits.append(f" {path}\n → {line.strip()[:120]}")
 break
 else:
 hits.append(f" {path}")
 return (
 f"Found {len(hits)} match(es):\n" + "\n".join(hits)
 if hits
 else f"No matches for '{query}'."
 )
 
 if name == "read_file":
 path = tool_input.get("path", "")
 content = CORPUS.get(path)
 if content is None:
 return f"Error: '{path}' not found. Available: {', '.join(CORPUS.keys())}"
 return content
 
 if name == "record_finding":
 finding = tool_input.get("finding", "")
 notes.append(finding)
 return f"Finding #{len(notes)} recorded (session-local)."
 
 return f"Error: unknown tool '{name}'"`
`# ── Session result container ─────────────────────────────────────────────
SessionResult = namedtuple(
 "SessionResult",
 [
 "messages", # final message list
 "notes", # notes taken this session
 "token_trajectory", # list of (turn, total_context_tokens)
 "events", # list of dicts describing compaction / clearing events
 "tool_counts", # dict of tool_name -> call count
 "file_reads", # list of (turn, path) for each read_file call
 "hit_limit", # True if the session stopped because it hit the context window
 "final_text", # final assistant text (convenience)
 ],
)
 
 
def _format_tool_arg(name: str, tool_input: dict) -> str:
 """Human-readable one-line summary of a tool call's arguments for verbose output."""
 if name == "search_files":
 return repr(tool_input.get("query", ""))
 if name == "read_file":
 return tool_input.get("path", "?")
 if name == "record_finding":
 finding = tool_input.get("finding", "")
 preview = finding[:50].replace("\n", " ")
 return f'"{preview}{"..." if len(finding) > 50 else ""}"'
 if name == "memory":
 cmd = tool_input.get("command", "?")
 path = tool_input.get("path", tool_input.get("old_path", ""))
 return f"{cmd} {path}"
 return str(tool_input)[:60]
 
 
# ── Agent loop ───────────────────────────────────────────────────────────
def run_research_session(
 initial_prompt: str,
 *,
 context_management: dict | None = None,
 betas: list[str] | None = None,
 memory_handler=None,
 max_turns: int = 12,
 label: str = "session",
 verbose: bool = True,
) -> SessionResult:
 """Run the research agent. Catches context-window overflow gracefully."""
 tools = list(BASE_TOOLS)
 if memory_handler is not None:
 tools.append(MEMORY_TOOL_SPEC)
 
 messages: list[dict] = [{"role": "user", "content": initial_prompt}]
 notes: list[str] = []
 token_trajectory: list[tuple[int, int]] = []
 events: list[dict] = []
 tool_counts: dict[str, int] = {}
 file_reads: list[tuple[int, str]] = [] # (turn, path) for each read_file
 hit_limit = False
 final_text = ""
 
 if verbose:
 print(f"┌─ [{label}]")
 
 for turn in range(1, max_turns + 1):
 kwargs: dict = dict(
 model=MODEL,
 max_tokens=4096,
 system=SYSTEM_PROMPT,
 tools=tools,
 messages=messages,
 )
 if context_management:
 kwargs["context_management"] = context_management
 if betas:
 kwargs["betas"] = betas
 
 # Call the API; catch context-window overflow
 try:
 if betas:
 response = client.beta.messages.create(**kwargs)
 else:
 response = client.messages.create(**kwargs)
 except anthropic.BadRequestError as e:
 # Context window exceeded (or similar input-too-large error)
 hit_limit = True
 if verbose:
 print(f"│ ⚠ CONTEXT WINDOW LIMIT REACHED at turn {turn} (API rejected)")
 print(f"│ {str(e)[:200]}")
 break
 
 # Track TOTAL context size: uncached + cache-read + cache-created.
 # usage.input_tokens alone excludes cached tokens, which makes the
 # plot show dips that are just cache hits, not context management.
 u = response.usage
 total_in = (
 u.input_tokens
 + (getattr(u, "cache_read_input_tokens", None) or 0)
 + (getattr(u, "cache_creation_input_tokens", None) or 0)
 )
 token_trajectory.append((turn, total_in))
 
 # Surface context-management events on their own prominent lines
 cm = getattr(response, "context_management", None)
 if cm is not None and getattr(cm, "applied_edits", None):
 for edit in cm.applied_edits:
 cleared_uses = getattr(edit, "cleared_tool_uses", None)
 cleared_toks = getattr(edit, "cleared_input_tokens", None)
 events.append(
 {
 "turn": turn,
 "kind": "clearing",
 "cleared_tool_uses": cleared_uses,
 "cleared_input_tokens": cleared_toks,
 }
 )
 if verbose:
 print(
 f"│ ✂ CLEARING (turn {turn}): {cleared_uses or '?'} tool results cleared, "
 f"~{cleared_toks:,} tokens freed"
 if cleared_toks
 else f"│ ✂ CLEARING (turn {turn}): applied"
 )
 
 # Serialize assistant content, track tool calls and compaction
 serialized: list[dict] = []
 tool_calls: list[dict] = []
 turn_tool_calls: list[tuple[str, dict]] = [] # (name, input) for verbose display
 compaction_this_turn = False
 for block in response.content:
 if block.type == "text":
 serialized.append({"type": "text", "text": block.text})
 if block.text.strip():
 final_text = block.text
 elif block.type == "tool_use":
 serialized.append(
 {
 "type": "tool_use",
 "id": block.id,
 "name": block.name,
 "input": block.input,
 }
 )
 tool_calls.append({"id": block.id, "name": block.name, "input": block.input})
 turn_tool_calls.append((block.name, block.input))
 tool_counts[block.name] = tool_counts.get(block.name, 0) + 1
 # Track file reads specifically so we can show what clearing drops
 if block.name == "read_file":
 file_reads.append((turn, block.input.get("path", "?")))
 elif block.type == "thinking":
 serialized.append(
 {"type": "thinking", "thinking": block.thinking, "signature": block.signature}
 )
 elif block.type == "compaction":
 serialized.append({"type": "compaction", "content": block.content})
 events.append({"turn": turn, "kind": "compaction", "summary": block.content})
 compaction_this_turn = True
 if verbose:
 print(
 f"│ ⊟ COMPACTION (turn {turn}): "
 f"~{count_tokens(block.content):,}-token summary replaces prior turns"
 )
 messages.append({"role": "assistant", "content": serialized})
 
 if not tool_calls:
 if verbose and not compaction_this_turn:
 print(f"│ turn {turn:2d} ctx={total_in:>7,} (final answer)")
 break
 
 # Execute tools, collecting result sizes so the verbose print
 # can show how much each call added to context
 tool_results: list[dict] = []
 result_sizes: list[int] = []
 for call in tool_calls:
 if call["name"] == "memory" and memory_handler is not None:
 result = memory_handler.handle(call["input"])
 else:
 result = execute_research_tool(call["name"], call["input"], notes)
 tool_results.append(
 {
 "type": "tool_result",
 "tool_use_id": call["id"],
 "content": result,
 }
 )
 result_sizes.append(len(result) if isinstance(result, str) else 0)
 messages.append({"role": "user", "content": tool_results})
 
 if verbose and not compaction_this_turn:
 # Header with context size, then one line per tool call with
 # its argument and approximate result size (so you can see
 # which calls are responsible for the next turn's ctx jump)
 print(f"│ turn {turn:2d} ctx={total_in:>7,}")
 for (name, tinput), rsize in zip(turn_tool_calls, result_sizes, strict=False):
 size_note = f" → ~{rsize // 4:,} tok" if rsize > 200 else ""
 print(f"│ {name:<16} {_format_tool_arg(name, tinput)}{size_note}")
 
 if verbose:
 if token_trajectory:
 peak = max(t for _, t in token_trajectory)
 status = "⚠ HIT CONTEXT LIMIT" if hit_limit else "completed"
 print(
 f"└─ {status}: {len(token_trajectory)} turns, peak ctx {peak:,}, "
 f"final ctx {token_trajectory[-1][1]:,}, {len(events)} context event(s)\n"
 )
 else:
 print("└─ HIT CONTEXT LIMIT on first turn: 0 turns completed\n")
 
 return SessionResult(
 messages, notes, token_trajectory, events, tool_counts, file_reads, hit_limit, final_text
 )
 
 
def show_cleared_reads(result: SessionResult, keep: int):
 """Show which file reads are no longer in context after clearing.
 
 Clearing replaces tool results older than the last `keep` tool uses
 with placeholders. We reconstruct the tool-use order and mark any
 read that falls outside the surviving `keep`-window as cleared.
 
 Note: if clearing fires multiple times, only the last event's
 boundary is considered and earlier cleared-then-re-read files may
 be misclassified.
 """
 if not result.file_reads:
 print("No file reads in this session.")
 return
 clearing_events = [e for e in result.events if e["kind"] == "clearing"]
 if not clearing_events:
 print("Clearing never fired; all file reads remain in context.")
 return
 
 # Walk messages in order to reconstruct the sequence of tool_use blocks
 # and which turn each one came from. The last `keep` of these survive
 # the most recent clearing; earlier ones are cleared.
 tool_use_seq: list[tuple[int, str, str]] = [] # (turn, name, path-if-read)
 turn = 0
 for msg in result.messages:
 if msg["role"] == "assistant" and isinstance(msg["content"], list):
 turn += 1
 for block in msg["content"]:
 if block.get("type") == "tool_use":
 name = block.get("name", "?")
 path = block.get("input", {}).get("path", "") if name == "read_file" else ""
 tool_use_seq.append((turn, name, path))
 
 last_clear_turn = clearing_events[-1]["turn"]
 seq_before = [t for t in tool_use_seq if t[0] < last_clear_turn]
 cleared_reads = [(t, p) for (t, n, p) in seq_before[:-keep] if n == "read_file"]
 surviving_reads = [
 (t, p) for tu in seq_before[-keep:] for (t, n, p) in [tu] if n == "read_file"
 ]
 # Reads at or after the last clearing turn are untouched by it.
 surviving_reads += [
 (t, p) for (t, n, p) in tool_use_seq if t >= last_clear_turn and n == "read_file"
 ]
 
 total = len(result.file_reads)
 print(f"Total file reads across session: {total}")
 print(f"Last clearing event fired at turn {last_clear_turn} (keep={keep})")
 print(f"\nReads cleared from context: {len(cleared_reads)}")
 for turn, path in cleared_reads[:12]:
 print(f" ✗ turn {turn:2d}: {path}")
 if len(cleared_reads) > 12:
 print(f" ... and {len(cleared_reads) - 12} more")
 print(
 f"\nReads still in context (within the keep={keep} window or after "
 f"the last clearing): {len(surviving_reads)}"
 )
 for turn, path in surviving_reads[:6]:
 print(f" ✓ turn {turn:2d}: {path}")
 if len(surviving_reads) > 6:
 print(f" ... and {len(surviving_reads) - 6} more")
 
 
# ── Plot helpers ─────────────────────────────────────────────────────────
 
 
def plot_trajectories(
 results: dict[str, SessionResult],
 title: str = "Context size per turn",
 triggers: dict[str, int] | None = None,
 project_growth_for: str | None = None,
):
 """Line plot of context tokens per turn.
 
 Vertical dashed lines mark turns where clearing fired; dash-dot lines
 mark compaction. Horizontal dotted lines mark configured trigger
 thresholds (pass triggers={"clearing": 20000, "compaction": 50000} etc).
 
 project_growth_for: label of a run to extrapolate. Fits a line to the
 last 5 points and draws a dotted segment forward ~8 turns to show where
 unmanaged growth is heading.
 """
 fig, ax = plt.subplots(figsize=(10, 4.5))
 colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
 
 for i, (label, res) in enumerate(results.items()):
 turns = [t for t, _ in res.token_trajectory]
 tokens = [tok for _, tok in res.token_trajectory]
 color = colors[i % len(colors)]
 ax.plot(turns, tokens, marker="o", label=label, markersize=4, color=color)
 # Mark events on the x-axis
 for ev in res.events:
 style = "--" if ev["kind"] == "clearing" else "-."
 ax.axvline(x=ev["turn"], color=color, linestyle=style, alpha=0.25, linewidth=1)
 # Dotted growth projection for the named run, capped at 1M
 if label == project_growth_for and len(turns) >= 3:
 HARD_LIMIT = 1_000_000
 fit_n = min(5, len(turns))
 xs, ys = turns[-fit_n:], tokens[-fit_n:]
 n = len(xs)
 sx, sy = sum(xs), sum(ys)
 slope = (n * sum(x * y for x, y in zip(xs, ys, strict=False)) - sx * sy) / (
 n * sum(x * x for x in xs) - sx * sx
 )
 intercept = (sy - slope * sx) / n
 proj_x, proj_y = [], []
 for x in range(turns[-1], turns[-1] + 9):
 y = slope * x + intercept
 if y > HARD_LIMIT:
 # Clip the last segment to the 1M ceiling and stop
 if proj_y and slope > 0:
 proj_x.append(proj_x[-1] + (HARD_LIMIT - proj_y[-1]) / slope)
 proj_y.append(HARD_LIMIT)
 break
 proj_x.append(x)
 proj_y.append(y)
 if proj_y:
 ax.plot(proj_x, proj_y, linestyle=":", color=color, alpha=0.6, linewidth=1.5)
 
 # Horizontal reference lines for trigger thresholds
 if triggers:
 for name, value in triggers.items():
 ax.axhline(y=value, color="gray", linestyle=":", alpha=0.6, linewidth=1)
 ax.annotate(
 f"{name} trigger: {value:,}",
 xy=(ax.get_xlim()[1], value),
 xytext=(-5, 3),
 textcoords="offset points",
 ha="right",
 va="bottom",
 fontsize=8,
 color="gray",
 )
 
 # 200K reference: earlier models cap here and would hard-stop
 if ax.get_ylim()[1] > 30_000:
 ax.axhline(y=200_000, color="gray", linestyle="--", alpha=0.5, linewidth=1)
 ax.annotate(
 "200K: earlier models stop here",
 xy=(ax.get_xlim()[0], 200_000),
 xytext=(5, -12),
 textcoords="offset points",
 ha="left",
 va="top",
 fontsize=8,
 color="gray",
 alpha=0.8,
 )
 
 ax.set_xlabel("Turn")
 ax.set_ylabel("Context tokens (incl. cached)")
 ax.set_title(title)
 ax.legend(loc="best")
 ax.grid(alpha=0.3)
 plt.tight_layout()
 plt.show()
 
 
def plot_summary_bars(results: dict[str, SessionResult], title: str = "Session outcomes"):
 """Side-by-side bars: final context, file reads."""
 labels = list(results.keys())
 final_ctx = [r.token_trajectory[-1][1] for r in results.values()]
 reads = [r.tool_counts.get("read_file", 0) for r in results.values()]
 
 fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
 fig.suptitle(title, y=1.02)
 
 for ax, values, ylabel in zip(
 axes,
 [final_ctx, reads],
 ["Final context (tokens)", "File reads"],
 strict=False,
 ):
 bars = ax.bar(range(len(labels)), values, color=plt.cm.Set2(range(len(labels))))
 ax.set_ylabel(ylabel)
 ax.set_xticks(range(len(labels)))
 ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=8)
 ax.grid(axis="y", alpha=0.3)
 for bar, val in zip(bars, values, strict=False):
 ax.text(
 bar.get_x() + bar.get_width() / 2,
 bar.get_height(),
 f"{val:,}" if val > 1000 else str(val),
 ha="center",
 va="bottom",
 fontsize=7,
 )
 
 plt.tight_layout()
 plt.show()`

### Baseline: no context management

First we run the agent with no context-management configuration. With the large corpus (each document is ~40K tokens with its appendix tables), context accumulates fast. We'll look at the same run under two lenses: what happens on a 1M-token window, and what would happen on a 200K window.

#### Part 1: On a 1M-token window

Claude Sonnet 4.6 and Claude Opus 4.6 both provide a [1M-token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows). For this task, the baseline's total input stays under that limit: the agent reads the full corpus and synthesizes without hitting a hard wall. The trajectory below shows the run climbing to hundreds of thousands of tokens, with the dotted line projecting continued growth at the same rate.

`baseline = run_research_session(RESEARCH_TASK, label="baseline", max_turns=12)
 
plot_trajectories(
 {"baseline": baseline},
 "Baseline on a 1M window: context grows past 200K",
 project_growth_for="baseline",
)
 
peak = max(t for _, t in baseline.token_trajectory)
n_turns = len(baseline.token_trajectory)
print(f"Peak context: {peak:,} tokens across {n_turns} turns")
print(f"File reads: {baseline.tool_counts.get('read_file', 0)}, Notes: {len(baseline.notes)}")
if baseline.hit_limit:
 print("\n⚠ This run hit the 1M hard limit.")
else:
 print(
 "\nThe run stayed within the 1M window. The dotted line projects "
 "where continued growth at the same rate would land, capped at 1M."
 )`

![Output image](/cookbook/images/notebooks/tool-use-context-engineering-context-engineering-tools/tool-use-context-engineering-context-engineering-tools_cell12_out1_400138b0.png)

![Output image](/cookbook/images/notebooks/tool-use-context-engineering-context-engineering-tools/tool-use-context-engineering-context-engineering-tools_cell12_out1_400138b0.png)
`# ── What's actually sitting in the context window at the end of the run ──
# Walk the message list and bucket everything by type. This is what the
# model has to attend to on every turn: no hard wall stopped it, but the
# pile keeps growing and every fact from early turns is buried deeper.
 
 
def _bucket_context(messages: list[dict]) -> dict[str, tuple[int, int]]:
 """Categorize message content into (count, approx_tokens) per bucket."""
 buckets: dict[str, list[int]] = {
 "File-read results": [],
 "Other tool results": [],
 "Agent reasoning text": [],
 "Tool-call records": [],
 "User/task prompts": [],
 }
 for msg in messages:
 content = msg.get("content")
 if isinstance(con

[Content truncated]
