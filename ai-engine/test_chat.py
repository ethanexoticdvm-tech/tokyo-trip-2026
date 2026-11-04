#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_chat.py - 本機 Gemini 3.8 Flash 隨身導遊大腦測試腳本
支援多輪連續對話、情境庫自動回歸測試與 Token 消耗統計。
"""

import os
import sys
import json
import time
import urllib.request
import urllib.error

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_FILE = os.path.join(SCRIPT_DIR, "system_instruction.md")
SCENARIOS_FILE = os.path.join(SCRIPT_DIR, "scenarios.json")

def load_system_prompt() -> str:
    if os.path.exists(PROMPT_FILE):
        with open(PROMPT_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "你是日本東京隨身全能導遊大腦。"

def get_api_key() -> str:
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        # Check config in .gemini or prompt user
        config_path = os.path.expanduser(r"~\.gemini\config\config.json")
        if os.path.exists(config_path):
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    cfg = json.load(f)
                    key = cfg.get("gemini_api_key") or cfg.get("api_key")
            except Exception:
                pass
    return key or ""

def call_gemini_38_flash(contents: list, system_instruction: str, api_key: str) -> dict:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"
    payload = {
        "system_instruction": {
            "parts": [{"text": system_instruction}]
        },
        "contents": contents
    }
    data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data_bytes,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    start_t = time.time()
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            dur = time.time() - start_t
            res_json = json.loads(resp.read().decode("utf-8"))
            candidate = res_json.get("candidates", [{}])[0]
            text = candidate.get("content", {}).get("parts", [{}])[0].get("text", "")
            usage = res_json.get("usageMetadata", {})
            return {
                "success": True,
                "text": text,
                "latency_sec": round(dur, 2),
                "prompt_tokens": usage.get("promptTokenCount", 0),
                "candidates_tokens": usage.get("candidatesTokenCount", 0),
                "total_tokens": usage.get("totalTokenCount", 0)
            }
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8", errors="replace")
        return {"success": False, "error": f"HTTP {e.code}: {err_msg}"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def run_interactive_mode(api_key: str):
    system_prompt = load_system_prompt()
    print("==================================================================")
    print("🍁 新宿・橫濱・箱根 6日遊 AI導遊大腦 (Gemini 3.8 Flash) 本機測試終端")
    print("==================================================================")
    print(f"📖 系統知識庫載入成功: {len(system_prompt)} 字元")
    print("💡 支援多輪連貫討論。輸入 'exit' 或 'q' 退出，輸入 'clear' 清空上下文記憶。\n")

    history = []
    turn = 1

    while True:
        try:
            user_input = input(f"[第 {turn} 輪] 您: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n👋 測試結束。")
            break

        if not user_input:
            continue
        if user_input.lower() in ("exit", "q", "quit"):
            print("👋 測試結束。")
            break
        if user_input.lower() == "clear":
            history = []
            turn = 1
            print("🧹 已清空所有上下文對話紀錄。\n")
            continue

        history.append({"role": "user", "parts": [{"text": user_input}]})

        print("🤖 Gemini 3.8 Flash 思考中...", end="\r", flush=True)
        res = call_gemini_38_flash(history[-16:], system_prompt, api_key)

        if res.get("success"):
            ai_text = res["text"]
            history.append({"role": "model", "parts": [{"text": ai_text}]})
            print(" " * 35, end="\r")  # Clear thinking text
            print(f"🤖 導遊大腦 ({res['latency_sec']}s | Tokens: {res['total_tokens']}):")
            print(ai_text)
            print("-" * 60)
            turn += 1
        else:
            print("❌ 連線或回傳失敗:", res.get("error"))
            history.pop()  # remove failed turn
            print("-" * 60)

def run_scenario_tests(api_key: str):
    system_prompt = load_system_prompt()
    if not os.path.exists(SCENARIOS_FILE):
        print("❌ 找不到情境庫 scenarios.json")
        return

    with open(SCENARIOS_FILE, "r", encoding="utf-8") as f:
        scenarios = json.load(f)

    print(f"🧪 開始執行 {len(scenarios)} 項隨身旅行實戰情境回歸測試...\n")

    for idx, sc in enumerate(scenarios, 1):
        print(f"【情境 {idx}/{len(scenarios)}】{sc['title']}")
        print(f"❓ 提問: {sc['prompt']}")
        history = [{"role": "user", "parts": [{"text": sc['prompt']}]}]
        res = call_gemini_38_flash(history, system_prompt, api_key)
        if res.get("success"):
            print(f"✅ 回應成功 ({res['latency_sec']}s | Tokens: {res['total_tokens']}):")
            print(res["text"][:300] + ("..." if len(res["text"]) > 300 else ""))
            print(f"📋 驗證要點: {', '.join(sc['expected_checks'])}")
        else:
            print(f"❌ 測試失敗: {res.get('error')}")
        print("=" * 60)

if __name__ == "__main__":
    key = get_api_key()
    if not key:
        print("⚠️ 未檢測到環境變數 GEMINI_API_KEY。")
        key = input("請貼入您的 Google Gemini API Key: ").strip()

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_scenario_tests(key)
    else:
        run_interactive_mode(key)
