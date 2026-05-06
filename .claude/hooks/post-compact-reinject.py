#!/usr/bin/env python3
# Fires on SessionStart(compact). Reinjects context-essentials and enforces recap.
import sys
from pathlib import Path

hooks_dir = Path(__file__).parent
essentials = (hooks_dir.parent / "context-essentials.md").read_text()

print(f"""COMPACTION DETECTED. Output a state recap before anything else: current phase, what is done, what is next.

--- REINJECTED CONTEXT ---
{essentials}
--- END REINJECTED CONTEXT ---""")

sys.exit(0)
