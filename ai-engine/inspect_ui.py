# -*- coding: utf-8 -*-
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Top bar
m1 = re.search(r'<header.*?</header>', html, re.DOTALL)
if m1:
    print("=== TOP BAR HTML ===")
    print(m1.group(0))

# Bottom nav
m2 = re.search(r'<nav id="bottomNav".*?</nav>', html, re.DOTALL)
if m2:
    print("\n=== BOTTOM NAV HTML ===")
    print(m2.group(0))

# Search for keyStatusCard or promptApiKey
m3 = re.search(r'<div[^>]*id="keyStatusCard".*?</div>\s*</div>', html, re.DOTALL)
if m3:
    print("\n=== KEY STATUS CARD HTML ===")
    print(m3.group(0))
else:
    # search where promptApiKey is called
    for line in html.split('\n'):
        if 'promptApiKey' in line or 'keyStatusText' in line:
            print("Found:", line.strip())

# Extract CSS for top-bar, bottom-nav, body
print("\n=== CSS RULES ===")
for selector in [r'\.top-bar\s*\{[^}]+\}', r'\.bottom-nav\s*\{[^}]+\}', r'\.bottom-tab\s*\{[^}]+\}', r'body\s*\{[^}]+\}']:
    matches = re.findall(selector, html)
    for m in matches:
        print(m)
        print("-" * 40)
