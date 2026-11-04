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
data_str = json.loads(raw_js_str)
data = json.loads(data_str)

# In Turbo-JSON (SuperJSON / Remix Devalue / flatted),
# The first object data[0] represents the root object.
# Negative numbers are special or null/undefined, positive integers are pointers to data[index].
# Let's inspect data[0] and data[2]
print("data[0]:", data[0])
print("data[2]:", data[2])

# Let's write a recursive resolver or inspect the keys of trip
def resolve(val, depth=0):
    if depth > 8:
        return "<max_depth>"
    if isinstance(val, int):
        if val < 0:
            return None
        if val < len(data):
            return resolve(data[val], depth+1)
        return val
    elif isinstance(val, dict):
        res = {}
        for k, v in val.items():
            # if key is _number, the real key is data[number]
            real_key = k
            if k.startswith("_") and k[1:].isdigit():
                k_idx = int(k[1:])
                if k_idx < len(data) and isinstance(data[k_idx], str):
                    real_key = data[k_idx]
            res[real_key] = resolve(v, depth+1)
        return res
    elif isinstance(val, list):
        return [resolve(x, depth+1) for x in val]
    else:
        return val

# Let's find "trip" or "container" in data
for i, item in enumerate(data):
    if isinstance(item, dict):
        # check if it has keys like "days" or "nodes" or "name" or "trip"
        resolved_keys = []
        for k in item.keys():
            if k.startswith("_") and k[1:].isdigit():
                ki = int(k[1:])
                if ki < len(data):
                    resolved_keys.append(str(data[ki]))
            else:
                resolved_keys.append(k)
        if "days" in resolved_keys or "trip" in resolved_keys or "title" in resolved_keys:
            print(f"Index {i} has interesting keys: {resolved_keys[:10]}")
            # print resolved
            try:
                r = resolve(i)
                # save to json
                with open(f"resolved_{i}.json", "w", encoding="utf-8") as f_res:
                    json.dump(r, f_res, ensure_ascii=False, indent=2)
                print(f"Saved resolved_{i}.json")
            except Exception as e:
                print(f"Resolve error for {i}: {e}")
