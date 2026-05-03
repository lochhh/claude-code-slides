"""
Fetch and clean a web page, saving the main content as markdown.
Strips navigation, footers, ads. Truncates at ~32 000 chars (~8 000 tokens).

Usage:
    uv run python tools/fetch_page.py "https://example.com/article" --topic "CLAUDE.md Setup"
    uv run python tools/fetch_page.py "https://example.com/article" --output deliverables/raw/my_article.md
"""

import argparse
import re
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

NOISE_TAGS = ["nav", "footer", "header", "aside", "script", "style", "form", "iframe", "noscript"]
MAX_CHARS = 32_000
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; research-bot/1.0; +https://github.com/lochhh/claude-code-slides)",
    "Accept": "text/html,application/xhtml+xml",
}


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def url_to_slug(url: str) -> str:
    path = url.rstrip("/").split("/")[-1] or url.rstrip("/").split("/")[-2]
    clean = re.sub(r"[^a-z0-9]+", "_", path.lower()).strip("_")
    return clean[:60] or "page"


def fetch_page(url: str, topic: str = "", output_path: Path | None = None) -> str:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        sys.exit(1)

    soup = BeautifulSoup(resp.text, "html.parser")

    # Remove noise elements
    for tag in soup(NOISE_TAGS):
        tag.decompose()

    # Prefer semantic content containers
    main = (
        soup.find("main")
        or soup.find("article")
        or soup.find(id=re.compile(r"content|main|article", re.I))
        or soup.find(class_=re.compile(r"content|main|article|post", re.I))
        or soup.find("body")
    )

    raw_text = main.get_text(separator="\n", strip=True) if main else soup.get_text(separator="\n", strip=True)

    # Collapse excessive blank lines
    lines = [line.strip() for line in raw_text.split("\n")]
    collapsed: list[str] = []
    prev_blank = False
    for line in lines:
        if not line:
            if not prev_blank:
                collapsed.append("")
            prev_blank = True
        else:
            collapsed.append(line)
            prev_blank = False

    content = "\n".join(collapsed).strip()

    if len(content) > MAX_CHARS:
        content = content[:MAX_CHARS] + "\n\n[Content truncated at 32 000 chars]"

    if len(content) < 200:
        print(f"Warning: extracted only {len(content)} chars from {url} — page may require JS or be paywalled.", file=sys.stderr)

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        header = f"# {soup.title.string.strip() if soup.title else url}\n\n"
        header += f"**Type:** article\n"
        header += f"**URL:** {url}\n"
        if topic:
            header += f"**Topic:** {topic}\n"
        header += "\n## Content\n\n"
        output_path.write_text(header + content, encoding="utf-8")
        print(f"Saved → {output_path} ({len(content)} chars)")

    return content


def main():
    parser = argparse.ArgumentParser(description="Fetch and clean a web page.")
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument("--topic", help="Topic name for output file header", default="")
    parser.add_argument("--output", help="Output .md file path", default=None)
    args = parser.parse_args()

    if args.output:
        output = Path(args.output)
    else:
        slug = url_to_slug(args.url)
        output = Path(f"deliverables/raw/{slug}.md")

    if output.exists():
        print(f"Skip: {output} already exists.")
        return

    fetch_page(args.url, topic=args.topic, output_path=output)


if __name__ == "__main__":
    main()
