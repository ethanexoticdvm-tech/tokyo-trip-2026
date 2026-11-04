# -*- coding: utf-8 -*-
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('ai-engine/generate_v151.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1345, 1385):
    print(f'{i+1}: {lines[i].rstrip()}')
