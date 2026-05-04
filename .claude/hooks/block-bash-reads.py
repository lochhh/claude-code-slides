#!/usr/bin/env python3
# Blocks bash cat/head/tail — use Read tool instead.
import json, re, sys

try:
    data = json.loads(sys.stdin.read())
except Exception:
    sys.exit(0)

cmd = data.get("tool_input", {}).get("command", "")
if re.search(r"\b(cat|head|tail)\b", cmd):
    print("BLOCKED: Use the Read tool instead of bash cat/head/tail.")
    sys.exit(2)

sys.exit(0)
