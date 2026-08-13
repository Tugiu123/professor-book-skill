#!/usr/bin/env python3
"""Create a standard professor-book-skill output pack."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT_FILES = {
    "00-学习路线与进度.md": "# 00-学习路线与进度\n\n",
    "01-全书脉络地图.md": "# 01-全书脉络地图\n\n",
    "02-教授带学会话状态.md": "# 02-教授带学会话状态\n\n## 当前模式\n\n尚未选择。待用户选择：A. 高处总览；B. 从0一步步学习。\n\n## 内容类型与讲解策略\n\n- 内容类型：待识别\n- 主导讲解风格：待选择\n- 进度单位：待选择\n- 密度规则：待选择\n\n## 当前进度\n\n尚未开始。示例：0/<total> 为总览，1/<total> 为第一段正式学习；总数必须来自全源建模后的动态课程分段计划。\n\n## 当前学习位置\n\n尚未开始真实教授带学会话。\n\n## 总课程序列\n\n待全源建模和内容类型识别后生成。可以按章节、概念、发现、论证、任务、案例或模块计数。\n\n## 动态课程分段计划\n\n| 序号 | 主题 | 在全篇中的作用 | 权重 | 密度 | 可延后内容 |\n|---|---|---|---|---|---|\n\n## 已生成支撑材料\n\n## 真实会话中已经讲过\n\n## 用户问题与困惑\n\n## 下一段计划\n\n",
    "index.md": "# Index\n\n",
}

SUB_FILES = {
    "chapters/ch01-课后复习.md": "# ch01-课后复习\n\n",
    "concepts/核心概念卡.md": "# 核心概念卡\n\n",
    "arguments/论证链与证据.md": "# 论证链与证据\n\n",
    "applications/方法卡.md": "# 方法卡\n\n",
    "applications/项目触发器.md": "# 项目触发器\n\n",
    "applications/决策检查清单.md": "# 决策检查清单\n\n",
    "skill-candidates/可转化为skill的方法论单元.md": "# 可转化为skill的方法论单元\n\n",
}


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff-]+", "", text)
    return text.strip("-") or "book"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="book title")
    parser.add_argument("--author", default="", help="book author")
    parser.add_argument("--out", default="books", help="parent output directory")
    parser.add_argument("--slug", default="", help="book slug")
    args = parser.parse_args()

    slug = args.slug or slugify(args.title)
    root = Path(args.out).expanduser().resolve() / slug
    root.mkdir(parents=True, exist_ok=True)

    for dirname in ["chapters", "concepts", "arguments", "applications", "skill-candidates"]:
        (root / dirname).mkdir(exist_ok=True)

    front = f"---\ntitle: {args.title}\nauthor: {args.author}\n---\n\n"
    for name, body in ROOT_FILES.items():
        path = root / name
        if not path.exists():
            path.write_text(front + body, encoding="utf-8")
    for name, body in SUB_FILES.items():
        path = root / name
        if not path.exists():
            path.write_text(front + body, encoding="utf-8")

    source_map = root / "source-map.json"
    if not source_map.exists():
        source_map.write_text(json.dumps({"sources": [], "claims": []}, ensure_ascii=False, indent=2), encoding="utf-8")

    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
