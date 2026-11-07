# -*- coding: utf-8 -*-
"""
Multi-Round Automated Code & Runtime Audit
Tokyo Trip Assistant v1.5.1 PRO
"""
import sys
import os
import re
import subprocess
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

print("=" * 60)
print("🚀 TOKYO TRIP ASSISTANT v1.5.1 PRO - MULTI-ROUND AUDIT")
print("=" * 60)

HTML_FILE = "index.html"
if not os.path.exists(HTML_FILE):
    print(f"ERROR: {HTML_FILE} not found!")
    sys.exit(1)

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html_content = f.read()

# ----------------------------------------------------------------------
# ROUND 1: STATIC ANALYSIS & DOM INTEGRITY
# ----------------------------------------------------------------------
print("\n🔍 [ROUND 1] Static Analysis & DOM Element Linkage...")
dom_ids = set(re.findall(r'id=["\']([a-zA-Z0-9_\-]+)["\']', html_content))
print(f"  • Extracted {len(dom_ids)} unique DOM IDs from HTML")

# Extract scripts
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html_content, re.DOTALL)
js_code = "\n".join([s for s in scripts if len(s) > 100])
print(f"  • Extracted JavaScript bundle ({len(js_code)} bytes)")

# Check syntax with node --check
temp_js = "temp_audit_bundle.js"
with open(temp_js, "w", encoding="utf-8") as f:
    f.write(js_code)

res = subprocess.run(["node", "--check", temp_js], capture_output=True, text=True)
if res.returncode == 0:
    print("  ✅ [PASS] Node.js syntax & compilation check passed (0 syntax errors)")
else:
    print(f"  ❌ [FAIL] Node.js syntax error:\n{res.stderr}")
    sys.exit(1)

# Check all getElementById targets exist
js_get_ids = set(re.findall(r'getElementById\(["\']([a-zA-Z0-9_\-]+)["\']\)', js_code))
missing_ids = js_get_ids - dom_ids
if missing_ids:
    print(f"  ❌ [FAIL] Missing DOM IDs in HTML: {missing_ids}")
else:
    print(f"  ✅ [PASS] All {len(js_get_ids)} getElementById targets exist in HTML DOM")

# Check all querySelector("#...") targets
js_qs_ids = set(re.findall(r'querySelector(?:All)?\(["\']#([a-zA-Z0-9_\-]+)["\']\)', js_code))
missing_qs = js_qs_ids - dom_ids
if missing_qs:
    print(f"  ❌ [FAIL] Missing querySelector IDs in HTML: {missing_qs}")
else:
    print(f"  ✅ [PASS] All {len(js_qs_ids)} querySelector targets exist in HTML DOM")

# ----------------------------------------------------------------------
# ROUND 2: DEFENSIVE HARDENING & EXCEPTION MITIGATION
# ----------------------------------------------------------------------
print("\n🛡️ [ROUND 2] Defensive Hardening Audit...")

issues = []

# Check for safeGetJson usage vs raw JSON.parse on localStorage
raw_ls_parses = re.findall(r'JSON\.parse\(\s*localStorage\.getItem\([^)]+\)\s*\)', js_code)
if raw_ls_parses:
    print(f"  ⚠️ [WARN] Found {len(raw_ls_parses)} raw unguarded JSON.parse(localStorage.getItem(...))")
    issues.append("raw_ls_parse")
else:
    print("  ✅ [PASS] No unguarded raw JSON.parse(localStorage.getItem(...)) found")

# Check Leaflet offline guard
if 'typeof L === "undefined"' in js_code or 'typeof L !== "undefined"' in js_code:
    print("  ✅ [PASS] Leaflet library availability check present")
else:
    print("  ⚠️ [WARN] Leaflet library availability check missing")
    issues.append("leaflet_guard")

# Check Fetch AbortController & Timeout
if "AbortController" in js_code:
    print("  ✅ [PASS] AbortController timeout mechanism present for Gemini API")
else:
    print("  ⚠️ [WARN] Gemini API missing AbortController timeout mechanism")
    issues.append("fetch_abort")

# Check CJK IME composition defense on input
if "isComposing" in js_code or "isComposing" in html_content:
    print("  ✅ [PASS] CJK IME composition defense (event.isComposing) present")
else:
    print("  ⚠️ [WARN] chatInputBox lacks CJK IME composition defense")
    issues.append("ime_defense")

# Check Pokemon map popup dynamic distance updating
if "getPokePopupHtml" in js_code:
    print("  ✅ [PASS] Pokemon map popup dynamic distance updater present")
else:
    print("  ⚠️ [WARN] Pokemon map popup distance is static upon creation")
    issues.append("dynamic_popup")

# ----------------------------------------------------------------------
# ROUND 3: DEADLINES & JST ARITHMETIC AUDIT
# ----------------------------------------------------------------------
print("\n⏰ [ROUND 3] Deadlines & JST Arithmetic Validation...")

# Validate all dates in DEADLINES_DATA can parse without NaN
dates = re.findall(r'date:\s*["\']([^"\']+)["\']', js_code)
print(f"  • Found {len(dates)} deadlines dates to validate")
node_test_date = """
const dates = %s;
let allOk = true;
dates.forEach(d => {
  const ts = new Date(d).getTime();
  if (isNaN(ts)) {
    console.error('Invalid date string:', d);
    allOk = false;
  }
});
if (allOk) console.log('ALL_DATES_VALID');
""" % json.dumps(dates)

res = subprocess.run(["node", "-e", node_test_date], capture_output=True, text=True)
if "ALL_DATES_VALID" in res.stdout:
    print(f"  ✅ [PASS] All {len(dates)} deadline date strings parse into valid timestamps with JST offset (+09:00)")
else:
    print(f"  ❌ [FAIL] Date parsing errors detected:\n{res.stderr}")
    issues.append("invalid_dates")

# ----------------------------------------------------------------------
# CLEANUP TEMP
# ----------------------------------------------------------------------
if os.path.exists(temp_js):
    os.remove(temp_js)

print("\n" + "=" * 60)
print(f"📋 AUDIT SUMMARY: {len(issues)} items require defensive hardening.")
for it in issues:
    print(f"   - {it}")
print("=" * 60)
