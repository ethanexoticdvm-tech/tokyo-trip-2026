import os

content = """@echo off
chcp 65001 >nul
title Push to GitHub Pages
echo ======================================================
echo  Shinjuku Trip Assistant - Push to GitHub Pages
echo ======================================================
echo.
cd /d "c:\\Users\\inche\\Antigravity\\tokyo-trip-assistant"
echo [1/2] Checking git status...
git status -s
echo.
echo [2/2] Pushing to https://github.com/ethanexoticdvm-tech/tokyo-trip-2026.git ...
echo (If Git Credential Manager opens in browser, please authorize)
echo.
git push github main
if %ERRORLEVEL% EQU 0 (
    echo.
    echo ======================================================
    echo  SUCCESS: Pushed to GitHub Pages!
    echo  URL: https://ethanexoticdvm-tech.github.io/tokyo-trip-2026/
    echo ======================================================
) else (
    echo.
    echo [FAILED] Please check GitHub authentication.
)
echo.
pause
"""

path1 = r"c:\Users\inche\Antigravity\tokyo-trip-assistant\一鍵推送到GitHub.bat"
path2 = r"G:\我的雲端硬碟\AI-Programe\新宿6日遊隨身戰情室_v1.4.1\一鍵推送到GitHub.bat"

with open(path1, "w", encoding="utf-8", newline="") as f:
    f.write(content)

with open(path2, "w", encoding="utf-8", newline="") as f:
    f.write(content)

print("Generated bat scripts successfully!")
