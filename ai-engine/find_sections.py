# -*- coding: utf-8 -*-
with open('ai-engine/generate_v151.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '<header>' in l:
        print(f'Header starts at line: {i+1}')
    if 'id="viewGemini"' in l:
        print(f'viewGemini starts at line: {i+1}')
    if 'keyStatusCard' in l:
        print(f'keyStatusCard at line: {i+1}')
    if '<nav class="bottom-bar"' in l:
        print(f'bottom-bar starts at line: {i+1}')
