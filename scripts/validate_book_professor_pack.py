#!/usr/bin/env python3
"""Validate a professor-book-skill pack for required structure."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED = [
    "00-学习路线与进度.md",
    "01-全书脉络地图.md",
    "02-教授带学会话状态.md",
    "chapters",
    "concepts",
    "arguments",
    "applications/方法卡.md",
    "applications/项目触发器.md",
    "applications/决策检查清单.md",
    "skill-candidates",
    "source-map.json",
    "index.md",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pack", help="book pack directory")
    args = parser.parse_args()
    root = Path(args.pack).expanduser().resolve()

    problems = []
    for rel in REQUIRED:
        path = root / rel
        if not path.exists():
            problems.append(f"missing: {rel}")
        elif path.is_file() and path.stat().st_size == 0:
            problems.append(f"empty: {rel}")

    sm = root / "source-map.json"
    if sm.exists():
        try:
            json.loads(sm.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            problems.append(f"invalid source-map.json: {exc}")

    if problems:
        print(json.dumps({"ok": False, "problems": problems}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps({"ok": True, "pack": str(root)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
