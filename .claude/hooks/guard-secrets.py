#!/usr/bin/env python3
import json, os, re, sys

try:
    data = json.loads(sys.stdin.read())
except Exception:
    sys.exit(0)

file_path = data.get("tool_input", {}).get("file_path", "")
if not file_path:
    sys.exit(0)

name = os.path.basename(file_path).lower()
path = file_path.lower().replace("\\", "/")

name_patterns = [
    r"^\.env$", r"^\.env\.", r"^secrets?\.", r"^credentials?\.",
    r"\.pem$", r"^id_rsa", r"^id_ed25519", r"^id_dsa", r"^id_ecdsa",
    r"\.key$", r"\.p12$", r"\.pfx$", r"\.gpg$", r"private.?key",
]
path_patterns = [r"/\.ssh/"]

blocked = any(re.search(p, name) for p in name_patterns) or \
          any(re.search(p, path) for p in path_patterns)

if blocked:
    print(f"BLOCKED: Write to sensitive file '{file_path}'. Edit secrets manually outside Claude.", file=sys.stderr)
    sys.exit(2)
