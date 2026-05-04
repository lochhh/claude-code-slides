#!/usr/bin/env python3
# Fires on SessionStart(compact). Reinjects context-essentials and enforces recap.
import sys
from pathlib import Path

hooks_dir = Path(__file__).parent
flag_path = hooks_dir / ".compact-flag"
flag_path.write_text("1")

essentials = (hooks_dir.parent / "context-essentials.md").read_text()

print(f"""COMPACTION DETECTED. You MUST do the following before anything else:

1. Output a state recap covering: current phase, what is done, what is next.
2. Then run: rm .claude/hooks/.compact-flag (via Bash) to unblock tool use.

--- REINJECTED CONTEXT ---
{essentials}
--- END REINJECTED CONTEXT ---""")

sys.exit(0)
