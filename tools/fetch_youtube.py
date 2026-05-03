"""
Fetch YouTube video metadata and auto-generated transcript using yt-dlp.
Saves title, channel, description, view count, and cleaned transcript to markdown.

Usage:
    uv run python tools/fetch_youtube.py "https://youtube.com/watch?v=VIDEO_ID" --topic "Hooks"
    uv run python tools/fetch_youtube.py "https://youtu.be/VIDEO_ID"

Requirements:
    yt-dlp must be installed: uv add yt-dlp  OR  pip install yt-dlp
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


MAX_TRANSCRIPT_CHARS = 20_000


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def extract_video_id(url: str) -> str:
    m = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url)
    return m.group(1) if m else slugify(url)[-20:]


def parse_vtt(vtt_content: str) -> str:
    """Convert WebVTT subtitle file to clean plain text."""
    lines = vtt_content.split("\n")
    text_parts: list[str] = []
    for line in lines:
        line = line.strip()
        # Skip header, timestamps, and empty lines
        if not line or line.startswith("WEBVTT") or "-->" in line or re.match(r"^\d+$", line):
            continue
        # Strip VTT inline tags like <00:00:00.000> and <c>
        line = re.sub(r"<[^>]+>", "", line)
        line = line.strip()
        if line:
            text_parts.append(line)

    # Deduplicate consecutive identical segments (common in auto-captions)
    deduped: list[str] = []
    prev = None
    for part in text_parts:
        if part != prev:
            deduped.append(part)
            prev = part

    return " ".join(deduped)


def fetch_youtube(url: str, topic: str = "", output_path: Path | None = None) -> dict:
    video_id = extract_video_id(url)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        out_template = str(tmp / "%(id)s")

        # Fetch metadata + write auto-subtitles to temp dir
        result = subprocess.run(
            [
                "yt-dlp",
                "--dump-json",
                "--write-auto-sub",
                "--skip-download",
                "--sub-lang", "en",
                "--sub-format", "vtt",
                "-o", out_template,
                url,
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )

        if result.returncode != 0:
            print(f"yt-dlp error:\n{result.stderr[:1000]}", file=sys.stderr)
            sys.exit(1)

        try:
            meta = json.loads(result.stdout)
        except json.JSONDecodeError:
            # yt-dlp sometimes emits multiple JSON lines; take first valid one
            for line in result.stdout.splitlines():
                line = line.strip()
                if line.startswith("{"):
                    meta = json.loads(line)
                    break
            else:
                print("Error: could not parse yt-dlp JSON output.", file=sys.stderr)
                sys.exit(1)

        # Find transcript VTT file in temp dir
        vtt_files = list(tmp.glob(f"{meta['id']}*.vtt"))
        transcript = ""
        if vtt_files:
            transcript = parse_vtt(vtt_files[0].read_text(encoding="utf-8", errors="replace"))
            if len(transcript) > MAX_TRANSCRIPT_CHARS:
                transcript = transcript[:MAX_TRANSCRIPT_CHARS] + " [Transcript truncated]"
        else:
            print("Warning: no English auto-captions found — saving metadata only.", file=sys.stderr)

    data = {
        "title": meta.get("title", ""),
        "channel": meta.get("uploader", meta.get("channel", "")),
        "url": url,
        "description": (meta.get("description") or "")[:600],
        "view_count": meta.get("view_count", 0),
        "upload_date": meta.get("upload_date", ""),
        "duration": meta.get("duration_string", ""),
        "transcript": transcript,
    }

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        views = f"{data['view_count']:,}" if data["view_count"] else "N/A"
        md = f"""# {data['title']}

**Type:** video
**URL:** {url}
**Topic:** {topic}
**Channel:** {data['channel']}
**Views:** {views}
**Uploaded:** {data['upload_date']}
**Duration:** {data['duration']}

## Description

{data['description']}

## Transcript

{data['transcript'] or '_No transcript available._'}
"""
        output_path.write_text(md, encoding="utf-8")
        print(f"Saved → {output_path} (transcript: {len(data['transcript'])} chars)")

    return data


def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube video metadata and transcript.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--topic", help="Topic name for output file header", default="")
    parser.add_argument("--output", help="Output .md file path", default=None)
    args = parser.parse_args()

    video_id = extract_video_id(args.url)

    if args.output:
        output = Path(args.output)
    else:
        output = Path(f"deliverables/raw/yt_{video_id}.md")

    if output.exists():
        print(f"Skip: {output} already exists.")
        return

    data = fetch_youtube(args.url, topic=args.topic, output_path=output)
    print(f"Title: {data['title']}")
    print(f"Channel: {data['channel']}")
    print(f"Transcript length: {len(data['transcript'])} chars")


if __name__ == "__main__":
    main()
