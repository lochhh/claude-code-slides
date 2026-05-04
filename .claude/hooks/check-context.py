#!/usr/bin/env python3
import json, os, sys

try:
    data = json.loads(sys.stdin.read())
except Exception:
    sys.exit(0)

transcript = data.get("transcript_path", "")
if not transcript or not os.path.exists(transcript):
    sys.exit(0)

kb = os.path.getsize(transcript) // 1024

# ~480KB ≈ 60% of 200k-token context (4 bytes/token + JSONL overhead)
if kb > 480:
    print(f"BLOCKED: Context >60% (transcript {kb}KB). Run /compact before continuing.", file=sys.stderr)
    sys.exit(2)
