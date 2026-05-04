#!/usr/bin/env python3
import json
import re
import subprocess
import sys

try:
    data = json.loads(sys.stdin.read())
except Exception:
    sys.exit(0)

file_path = data.get("tool_input", {}).get("file_path", "")
if not file_path or not re.search(r"README\.md$", file_path.replace("\\", "/")):
    sys.exit(0)

try:
    result = subprocess.run(
        ["git", "diff", "HEAD", "--", "README.md"],
        capture_output=True, text=True
    )
    diff = result.stdout
except Exception:
    sys.exit(0)

if not diff:
    sys.exit(0)

# Walk diff lines: track which section we're in, flag any +/- inside Initial Prompt
in_section = False
changed = False
for line in diff.splitlines():
    prefix = line[0] if line else " "
    content = line[1:] if prefix in ("+", "-", " ") else line

    if content.startswith("## Initial Prompt"):
        in_section = True
    elif content.startswith("## ") and in_section:
        break  # entered next section

    if in_section and prefix in ("+", "-"):
        changed = True
        break

if changed:
    print("README.md Initial Prompt section changed. Run /sync-workflows to update any affected workflows/ files.")

sys.exit(0)
