# -*- coding: utf-8 -*-
import subprocess
import os
import sys

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
    html = f.read()

tabs = [
    ("funliday", "01_funliday_itinerary.png"),
    ("gemini", "02_gemini_ai_brain.png"),
    ("pokemon", "03_pokemon_hunt.png"),
    ("deadlines", "04_deadlines_traps.png"),
    ("tickets", "05_romancecar_tickets.png"),
]

for tab, filename in tabs:
    # Inject switchNavTab directly
    modified = html.replace(
        "// Deep link support",
        f"switchNavTab('{tab}');\n    // Deep link support"
    )
    tmp_html = os.path.join(scratch_dir, f"view_{tab}.html")
    with open(tmp_html, "w", encoding="utf-8") as tf:
        tf.write(modified)

    out_path = os.path.join(artifact_dir, filename)
    file_url = f"file:///{tmp_html.replace(os.sep, '/')}"

    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--virtual-time-budget=2000",
        "--window-size=414,920",
        f"--screenshot={out_path}",
        file_url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(out_path):
        size = os.path.getsize(out_path)
        print(f"✅ Generated {filename}: {size} bytes")
    else:
        print(f"❌ Failed to generate {filename}: {res.stderr}")

print("All tab views generated successfully.")
