"""CLI entry: python -m bob_naira_assist"""

from __future__ import annotations

import os

from bob_naira_assist.agent import demo_mode_enabled, run_demo_script


def main() -> None:
    os.environ.setdefault("DEMO_MODE", "1")
    if not demo_mode_enabled():
        print("DEMO_MODE is off. Offline MVP only supports DEMO_MODE=1 for now.")
        return
    print(run_demo_script())


if __name__ == "__main__":
    main()
