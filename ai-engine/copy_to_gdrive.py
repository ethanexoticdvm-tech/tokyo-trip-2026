# -*- coding: utf-8 -*-
import os
import shutil
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

src_dir = r"C:\Users\inche\Antigravity\tokyo-trip-assistant"
target_dir = r"G:\我的雲端硬碟\AI-Programe\新宿6日遊隨身戰情室_v1.5.0"

os.makedirs(target_dir, exist_ok=True)

files_to_copy = [
    "index.html",
    "README.md",
    "PROGRESS.md",
    "📖_使用說明與操作SOP.md",
    "啟動_隨身戰情室.bat",
    "一鍵推送到GitHub.bat",
]

for f in files_to_copy:
    src = os.path.join(src_dir, f)
    dst = os.path.join(target_dir, f)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied: {f}")

ai_src = os.path.join(src_dir, "ai-engine")
ai_dst = os.path.join(target_dir, "ai-engine")
if os.path.exists(ai_src):
    shutil.copytree(ai_src, ai_dst, dirs_exist_ok=True)
    print("Copied: ai-engine folder")

print(f"✅ 交付成功至 Google Drive：{target_dir}")
