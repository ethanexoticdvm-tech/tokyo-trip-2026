import json

with open("funliday_dump.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
s7 = scripts[7]

prefix = "enqueue("
idx = s7.find(prefix) + len(prefix)
end_idx = s7.rfind(");")
raw_js_str = s7[idx:end_idx].strip()
data = json.loads(json.loads(raw_js_str))

print("data[21]:", data[21])
print("data[22]:", data[22])

route_layout = data[22]
# let's map keys of data[22]
for k, v in route_layout.items():
    real_k = data[int(k[1:])] if k.startswith("_") and k[1:].isdigit() else k
    val_repr = str(v)
    if isinstance(v, int) and 0 <= v < len(data):
        target = data[v]
        val_repr = f"-> idx {v}: {type(target)} " + (str(list(target.keys())[:5]) if isinstance(target, dict) else str(target)[:40])
    print(f"  {real_k}: {val_repr}")
