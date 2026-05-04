#!/usr/bin/env python3
import json, re, sys

try:
    data = json.loads(sys.stdin.read())
except Exception:
    sys.exit(0)

tool = data.get("tool_name", "")

# Read-only Claude tools — always safe
safe_tools = {"Read", "Glob", "Grep", "LS", "WebSearch", "WebFetch", "TodoRead"}
if tool in safe_tools:
    print('{"permissionDecision": "allow"}')
    sys.exit(0)

# Bash — auto-allow known read-only commands with no output redirection
if tool == "Bash":
    cmd = data.get("tool_input", {}).get("command", "")
    if not cmd:
        sys.exit(0)

    # Reject if command writes to files
    if re.search(r">\s*\S", cmd):
        sys.exit(0)

    safe_patterns = [
        r"^ls\b", r"^cat\b", r"^head\b", r"^tail\b", r"^wc\b",
        r"^echo\b", r"^pwd\b", r"^which\b", r"^file\b", r"^stat\b",
        r"^du\b", r"^df\b", r"^grep\b", r"^rg\b", r"^find\b",
        r"^git (status|log|diff|show|branch|remote|describe)\b",
        r"^type\b",
        # clear compact flag — both Unix and Windows shells
        r"^rm\s+\.claude[/\\]hooks[/\\]\.compact-flag\b",
        r"^Remove-Item\s+\.claude[/\\]hooks[/\\]\.compact-flag\b",
    ]

    cmd_trimmed = cmd.strip()
    for p in safe_patterns:
        if re.search(p, cmd_trimmed):
            print('{"permissionDecision": "allow"}')
            sys.exit(0)

sys.exit(0)
