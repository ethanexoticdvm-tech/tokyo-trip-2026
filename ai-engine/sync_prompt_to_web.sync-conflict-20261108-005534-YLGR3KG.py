#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_prompt_to_web.py - 自動將 ai-engine/system_instruction.md 注入同步至 index.html
讓 Prompt 的調優與更新無須手動複製貼上，一鍵同步發布！
"""

import os
import sys
import re

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

AI_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(AI_DIR)
SYSTEM_MD = os.path.join(AI_DIR, "system_instruction.md")
INDEX_HTML = os.path.join(PROJECT_DIR, "index.html")

def sync():
    if not os.path.exists(SYSTEM_MD):
        print(f"❌ 找不到系統提示詞檔案: {SYSTEM_MD}")
        sys.exit(1)
    if not os.path.exists(INDEX_HTML):
        print(f"❌ 找不到目標前端檔案: {INDEX_HTML}")
        sys.exit(1)

    with open(SYSTEM_MD, "r", encoding="utf-8") as f:
        new_prompt = f.read().strip()

    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # Match `const SYSTEM_KNOWLEDGE = `...`;`
    pattern = r'(const SYSTEM_KNOWLEDGE = `)[\s\S]*?(`;)'
    if not re.search(pattern, html):
        print("❌ 在 index.html 中未匹配到 const SYSTEM_KNOWLEDGE 常數！")
        sys.exit(1)

    # Escape any backticks in prompt if exist
    escaped_prompt = new_prompt.replace("`", "\\`")
    replacement = r'\g<1>' + "\n" + escaped_prompt + "\n" + r'\g<2>'
    updated_html = re.sub(pattern, replacement, html, count=1)

    with open(INDEX_HTML, "w", encoding="utf-8", newline="") as f:
        f.write(updated_html)

    print(f"✅ 成功將 system_instruction.md ({len(new_prompt)} 字元) 注入 index.html！")

if __name__ == "__main__":
    sync()
