"""
Search for high-quality sources on a Claude Code topic using Tavily.
Saves each result as deliverables/raw/<slug>.md and prints a source list.

Usage:
    uv run python tools/search_web.py "CLAUDE.md setup" --topic "CLAUDE.md Setup"
    uv run python tools/search_web.py "Claude Code MCP servers"

Env:
    TAVILY_API_KEY — required
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

YOUTUBE_RE = re.compile(r"(youtube\.com/watch|youtu\.be/)")
GITHUB_RE = re.compile(r"github\.com/")

# Topics that tend to surface poor results — boost with extra keywords
QUALITY_SUFFIX = "site:reddit.com OR site:github.com OR site:news.ycombinator.com OR site:anthropic.com OR advanced tips engineer"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def url_to_slug(url: str) -> str:
    path = url.rstrip("/").split("/")
    segment = next((p for p in reversed(path) if p), "page")
    clean = re.sub(r"[^a-z0-9]+", "_", segment.lower()).strip("_")
    return clean[:60] or "page"


def infer_type(url: str) -> str:
    if YOUTUBE_RE.search(url):
        return "video"
    if GITHUB_RE.search(url):
        return "repo"
    if "reddit.com" in url or "news.ycombinator.com" in url:
        return "community"
    if "docs.anthropic.com" in url or "anthropic.com" in url:
        return "docs"
    return "article"


def save_source(result: dict, topic: str, out_dir: Path) -> Path | None:
    url = result["url"]
    src_type = infer_type(url)

    if src_type == "video":
        # YouTube — save stub only; agent will run fetch_youtube.py separately
        slug = "yt_" + re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url).group(1) \
            if re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url) else slugify(url)[-20:]
        path = out_dir / f"{slug}.md"
        if path.exists():
            return path
        content = f"""# {result['title']}

**Type:** video
**URL:** {url}
**Topic:** {topic}

## Description

{result.get('content', '_No description available._')}

_Run `uv run python tools/fetch_youtube.py "{url}"` to add full transcript._
"""
        path.write_text(content, encoding="utf-8")
        return path

    # For all other types: save Tavily content (raw_content if available, else snippet)
    raw = result.get("raw_content") or result.get("content") or ""
    if len(raw) < 100:
        return None  # too thin — skip, agent can fetch_page manually

    slug = url_to_slug(url)
    path = out_dir / f"{slug}.md"
    if path.exists():
        return path

    truncated = raw[:32_000] + "\n\n[Content truncated]" if len(raw) > 32_000 else raw

    content = f"""# {result['title']}

**Type:** {src_type}
**URL:** {url}
**Topic:** {topic}
**Published:** {result.get('published_date', 'unknown')}

## Content

{truncated}
"""
    path.write_text(content, encoding="utf-8")
    return path


def search_topic(topic: str, query: str, out_dir: Path) -> list[dict]:
    client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=7,
        include_raw_content=True,
    )

    results = response.get("results", [])
    saved: list[dict] = []

    for r in results:
        url = r.get("url", "")
        if not url:
            continue

        out_dir.mkdir(parents=True, exist_ok=True)
        path = save_source(r, topic, out_dir)

        entry = {
            "title": r.get("title", url),
            "url": url,
            "type": infer_type(url),
            "summary": (r.get("content") or "")[:200],
            "saved_to": str(path) if path else None,
            "needs_fetch": infer_type(url) == "video" or not path,
        }
        saved.append(entry)
        status = "saved" if path else "skipped (thin content)"
        print(f"  [{entry['type']}] {entry['title'][:60]} — {status}")

    return saved


def main():
    parser = argparse.ArgumentParser(description="Search for Claude Code sources using Tavily.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--topic", help="Human-readable topic name", default=None)
    parser.add_argument("--outdir", help="Output directory (default: deliverables/raw)", default="deliverables/raw")
    args = parser.parse_args()

    topic = args.topic or args.query
    out_dir = Path(args.outdir)

    print(f"Searching: {topic}")
    sources = search_topic(topic, args.query, out_dir)

    print(f"\nFound {len(sources)} sources. Summary:")
    for s in sources:
        flag = " [needs fetch_youtube]" if s["type"] == "video" else ""
        flag = " [needs fetch_page — thin]" if s["needs_fetch"] and s["type"] != "video" else flag
        print(f"  {s['url']}{flag}")

    print("\n---JSON---")
    print(json.dumps(sources, indent=2))


if __name__ == "__main__":
    main()
