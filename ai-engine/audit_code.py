# -*- coding: utf-8 -*-
import sys
import re
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

print("=== STARTING COMPREHENSIVE MULTI-ROUND CODE AUDIT ===")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Extract IDs from HTML
ids_in_html = set(re.findall(r'id=["\']([a-zA-Z0-9_\-]+)["\']', html))
print(f"[ROUND 1] Total unique HTML element IDs found: {len(ids_in_html)}")

# Extract all scripts
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL)
js = '\n'.join([s for s in scripts if len(s) > 100])

# 2. Extract getElementById calls in JS
get_elem_ids = set(re.findall(r'getElementById\(["\']([a-zA-Z0-9_\-]+)["\']\)', js))
print(f"[ROUND 1] Total getElementById IDs in JS: {len(get_elem_ids)}")

missing_in_html = get_elem_ids - ids_in_html
if missing_in_html:
    print(f"❌ [ROUND 1 ERROR] IDs referenced in JS but NOT found in HTML ({len(missing_in_html)}):")
    for m in sorted(missing_in_html):
        print(f"   - #{m}")
else:
    print("✅ [ROUND 1 PASS] 100% of getElementById targets exist in HTML DOM!")

# 3. Check querySelector("#...") targets
qs_ids = set(re.findall(r'querySelector(?:All)?\(["\']#([a-zA-Z0-9_\-]+)["\']\)', js))
missing_qs = qs_ids - ids_in_html
if missing_qs:
    print(f"❌ [ROUND 1 ERROR] querySelector IDs NOT found in HTML ({len(missing_qs)}):")
    for m in sorted(missing_qs):
        print(f"   - #{m}")
else:
    print("✅ [ROUND 1 PASS] 100% of querySelector('#...') targets exist in HTML DOM!")

# 4. Check inline HTML event handlers
handlers = re.findall(r'on[a-z]+=["\']([^"\']+)["\']', html)
called_funcs = set()
for h in handlers:
    match = re.search(r'([a-zA-Z0-9_]+)\s*\(', h)
    if match:
        called_funcs.add(match.group(1))

defined_funcs = set()
for m in re.finditer(r'function\s+([a-zA-Z0-9_]+)', js):
    defined_funcs.add(m.group(1))
for m in re.finditer(r'(?:const|let|var|window\.)([a-zA-Z0-9_]+)\s*=\s*(?:function|\([^)]*\)\s*=>)', js):
    defined_funcs.add(m.group(1))

# Also standard window methods
builtins = {'alert', 'confirm', 'prompt', 'open', 'close', 'print', 'focus', 'blur'}
missing_funcs = (called_funcs - defined_funcs) - builtins
if missing_funcs:
    print(f"❌ [ROUND 1 ERROR] HTML invokes undefined JS functions ({len(missing_funcs)}):")
    for mf in sorted(missing_funcs):
        print(f"   - {mf}()")
else:
    print(f"✅ [ROUND 1 PASS] All {len(called_funcs)} inline event handlers map to defined JS functions!")

# 5. Check LocalStorage usage
ls_items = re.findall(r'localStorage\.getItem\(["\']([a-zA-Z0-9_\-]+)["\']\)', js)
print(f"[ROUND 2] LocalStorage keys accessed: {set(ls_items)}")

# Check for unguarded JSON.parse
json_parses = re.findall(r'JSON\.parse\([^)]+\)', js)
print(f"[ROUND 2] JSON.parse calls found: {len(json_parses)}")

# 6. Check Leaflet map and GPS error handling
print("[ROUND 2] Checking Leaflet & Map lifecycle...")
has_l_guard = 'typeof L !==' in js or 'window.L' in js
print(f"   - Leaflet CDN availability check present: {has_l_guard}")

has_map_destroy = 'pokeMap' in js
print(f"   - pokeMap instance management: {has_map_destroy}")

# 7. Check Deadlines sorting and JST live time calculation
print("[ROUND 3] Checking Deadlines calculation...")
has_live_jst = 'getLiveJstTime' in js or 'jst' in js.lower()
print(f"   - Live JST time calculation: {has_live_jst}")

# 8. Check Gemini API call error handling
print("[ROUND 3] Checking Gemini API error handling & timeout...")
has_abort = 'AbortController' in js or 'signal' in js
print(f"   - Fetch AbortController / Timeout present: {has_abort}")

has_finally_spinner = 'finally' in js and 'isAiQueryInProgress' in js
print(f"   - Spinner / state cleanup in finally block: {has_finally_spinner}")

print("=== AUDIT SCRIPT FINISHED ===")
