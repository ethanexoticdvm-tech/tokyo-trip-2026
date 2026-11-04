# -*- coding: utf-8 -*-
import subprocess
import os
import sys
import re

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

artifact_dir = r"C:\Users\inche\.gemini\antigravity\brain\91597ac8-c416-4cbe-bae7-680f6b777a9a"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
scratch_dir = os.path.join(artifact_dir, "scratch")
os.makedirs(scratch_dir, exist_ok=True)

with open(r"C:\Users\inche\Antigravity\tokyo-trip-assistant\index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

tabs = [
    ("funliday", "01_方案概覽_Funliday與6天動線.png"),
    ("gemini", "02_AI隨身導遊大腦_5大模式與HUD.png"),
    ("pokemon", "03_橫濱寶可夢尋寶任務_進度達成率.png"),
    ("deadlines", "04_行程關鍵死線與交通陷阱.png"),
    ("tickets", "05_離線小田急浪漫特快擬真車票.png"),
]

# All views in DOM
view_ids = {
    "funliday": "viewFunliday",
    "gemini": "viewGemini",
    "pokemon": "viewPokemon",
    "deadlines": "viewDeadlines",
    "tickets": "viewTickets"
}

for active_key, filename in tabs:
    html = base_html
    
    # Adjust each view container style
    for key, vid in view_ids.items():
        if key == active_key:
            # ensure visible
            html = re.sub(
                rf'(<div id="{vid}"[^>]*?)style="[^"]*display:\s*none;?[^"]*"',
                r'\1style="display: block;"',
                html
            )
            # if no style attr exists (like funliday which had none by default)
            if f'id="{vid}"' in html and 'style=' not in re.search(rf'<div id="{vid}"[^>]*>', html).group(0):
                html = html.replace(f'id="{vid}"', f'id="{vid}" style="display: block;"')
        else:
            # ensure hidden
            if f'id="{vid}"' in html:
                tag = re.search(rf'<div id="{vid}"[^>]*>', html).group(0)
                if 'style=' in tag:
                    new_tag = re.sub(r'style="[^"]*"', 'style="display: none;"', tag)
                else:
                    new_tag = tag.replace(f'id="{vid}"', f'id="{vid}" style="display: none;"')
                html = html.replace(tag, new_tag)

    # Adjust bottom bar active tab
    # remove active from all tabs
    html = html.replace('class="bottom-tab active"', 'class="bottom-tab"')
    # add active to current tab
    html = html.replace(
        f'onclick="switchNavTab(\'{active_key}\')"',
        f'onclick="switchNavTab(\'{active_key}\')" class="bottom-tab active"'
    )

    tmp_path = os.path.join(scratch_dir, f"snap_{active_key}.html")
    with open(tmp_path, "w", encoding="utf-8") as f_out:
        f_out.write(html)

    out_png = os.path.join(artifact_dir, filename)
    file_url = f"file:///{tmp_path.replace(os.sep, '/')}"

    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=414,920",
        f"--screenshot={out_png}",
        file_url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(out_png):
        print(f"✅ Generated {filename}: {os.path.getsize(out_png)} bytes")
    else:
        print(f"❌ Failed {filename}: {res.stderr}")

print("Snapshots rendering completed.")
