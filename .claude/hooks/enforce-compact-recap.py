#!/usr/bin/env python3
# Blocks non-Bash tools until compact recap flag is cleared.
import sys
from pathlib import Path

flag_path = Path(__file__).parent / ".compact-flag"
if flag_path.exists():
    print("BLOCKED: Output state recap first, then run: rm .claude/hooks/.compact-flag")
    sys.exit(2)

sys.exit(0)
