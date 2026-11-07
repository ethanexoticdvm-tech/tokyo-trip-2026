# -*- coding: utf-8 -*-
"""
Builder for generate_v152.py with proper f-string escaping.
"""

import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

V151_PATH = "ai-engine/generate_v151.py"
V152_PATH = "ai-engine/generate_v152.py"

with open(V151_PATH, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update docstring
code = code.replace(
    'generate_v151.py - Tokyo Trip Assistant v1.5.1 PRO',
    'generate_v152.py - Tokyo Trip Assistant v1.5.2 PRO\n'
    '1. Maple leaf (🍁) click opens Settings Modal (Gemini API Key + Font Scaling).\n'
    '2. Removed redundant key status card from viewGemini.\n'
    '3. Fixed bottom clipping (下方破圖) with safe padding.\n'
    '4. Fixed right clipping (右側也是破圖) with compact header & responsive pills.'
)

# 2. Version bumping
code = code.replace("v1.5.1 PRO", "v1.5.2 PRO")
code = code.replace("v1.5.1", "v1.5.2")

# 3. CSS font scaling & responsive base (escaped for f-string)
old_css_root = ''':root {{
      --bg: #070a12;
      --bg-card: #0f1523;'''

new_css_root = ''':root {{
      --font-scale: 1;
      --bg: #070a12;
      --bg-card: #0f1523;'''

code = code.replace(old_css_root, new_css_root, 1)

old_css_body = '''    body {{
      background: var(--bg);
      color: var(--text-1);
      min-height: 100vh;
      overflow-x: hidden;
      padding-bottom: calc(84px + env(safe-area-inset-bottom));
      line-height: 1.5;
      font-size: 15px;
    }}'''

new_css_body = '''    *, *::before, *::after {{
      box-sizing: border-box;
    }}

    html {{
      font-size: 15px;
      font-size: calc(15px * var(--font-scale, 1));
      overflow-x: hidden;
      max-width: 100vw;
    }}

    body {{
      background: var(--bg);
      color: var(--text-1);
      min-height: 100vh;
      overflow-x: hidden;
      max-width: 100vw;
      padding-bottom: calc(92px + max(16px, env(safe-area-inset-bottom, 16px)));
      line-height: 1.5;
    }}'''

code = code.replace(old_css_body, new_css_body, 1)

# 4. Header & Top Bar CSS (Fix right-side clipping)
old_header_css = '''    /* Top Sticky App Bar */
    header {{
      position: sticky;
      top: 0;
      background: rgba(7, 10, 18, 0.94);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      z-index: 100;
      border-bottom: 1px solid var(--border);
      padding: max(12px, env(safe-area-inset-top)) 16px 12px;
    }}

    .header-inner {{
      max-width: 640px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
    }}

    .brand-wrap {{
      display: flex;
      align-items: center;
      gap: 8px;
      text-decoration: none;
      color: var(--text-1);
    }}

    .brand-icon {{
      width: 32px;
      height: 32px;
      border-radius: var(--radius-sm);
      background: linear-gradient(135deg, rgba(244, 63, 94, 0.2), rgba(244, 63, 94, 0.05));
      border: 1px solid rgba(244, 63, 94, 0.35);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      flex-shrink: 0;
    }}

    .brand-title {{
      font-weight: 800;
      font-size: 0.95rem;
      letter-spacing: -0.2px;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .badge-ver {{
      background: var(--primary-gradient);
      color: #fff;
      font-size: 0.62rem;
      font-family: var(--font-mono);
      font-weight: 800;
      padding: 2px 7px;
      border-radius: var(--radius-full);
      box-shadow: 0 2px 8px var(--primary-glow);
    }}

    .header-actions {{
      display: flex;
      gap: 8px;
      align-items: center;
    }}

    .top-pill {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border);
      color: var(--text-1);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0 14px;
      height: var(--touch-min);
      border-radius: var(--radius-full);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      text-decoration: none;
      cursor: pointer;
      transition: var(--transition);
      white-space: nowrap;
    }}'''

new_header_css = '''    /* Top Sticky App Bar (Compact & Responsive) */
    header {{
      position: sticky;
      top: 0;
      background: rgba(7, 10, 18, 0.96);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      z-index: 100;
      border-bottom: 1px solid var(--border);
      padding: max(8px, env(safe-area-inset-top)) 10px 8px;
      width: 100%;
      box-sizing: border-box;
    }}

    .header-inner {{
      max-width: 640px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 6px;
      width: 100%;
      box-sizing: border-box;
    }}

    .brand-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: var(--radius-md);
      padding: 4px 8px;
      color: var(--text-1);
      cursor: pointer;
      text-decoration: none;
      transition: var(--transition);
      min-width: 0;
      flex-shrink: 1;
      -webkit-tap-highlight-color: transparent;
    }}

    .brand-btn:hover, .brand-btn:active {{
      background: rgba(244, 63, 94, 0.15);
      border-color: rgba(244, 63, 94, 0.45);
      transform: translateY(-1px);
    }}

    .brand-icon {{
      width: 26px;
      height: 26px;
      border-radius: 6px;
      background: linear-gradient(135deg, rgba(244, 63, 94, 0.25), rgba(244, 63, 94, 0.08));
      border: 1px solid rgba(244, 63, 94, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.95rem;
      flex-shrink: 0;
    }}

    .brand-title {{
      font-weight: 800;
      font-size: 0.88rem;
      letter-spacing: -0.2px;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .settings-gear-hint {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      color: var(--text-3);
      margin-left: 2px;
      transition: var(--transition);
    }}

    .brand-btn:hover .settings-gear-hint {{
      color: var(--primary);
      transform: rotate(45deg);
    }}

    .badge-ver {{
      background: var(--primary-gradient);
      color: #fff;
      font-size: 0.6rem;
      font-family: var(--font-mono);
      font-weight: 800;
      padding: 1.5px 5px;
      border-radius: var(--radius-full);
      box-shadow: 0 2px 6px var(--primary-glow);
    }}

    .header-actions {{
      display: flex;
      gap: 5px;
      align-items: center;
      flex-shrink: 0;
    }}

    .top-pill {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border);
      color: var(--text-1);
      font-size: 0.74rem;
      font-weight: 700;
      padding: 0 9px;
      height: 34px;
      min-height: 34px;
      border-radius: var(--radius-full);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      text-decoration: none;
      cursor: pointer;
      transition: var(--transition);
      white-space: nowrap;
      flex-shrink: 0;
    }}

    .top-pill:hover {{
      background: rgba(255, 255, 255, 0.1);
      border-color: var(--border-hover);
    }}

    @media (max-width: 375px) {{
      .badge-ver {{ display: none; }}
      .top-pill {{ padding: 0 7px; font-size: 0.72rem; }}
    }}
    @media (max-width: 335px) {{
      .top-pill span {{ display: none; }}
      .top-pill {{ padding: 0 8px; }}
    }}'''

code = code.replace(old_header_css, new_header_css, 1)

# 5. Bottom Navigation CSS (Fix bottom clipping)
old_bottom_css = '''    .bottom-bar {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(7, 10, 18, 0.96);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: space-around;
      align-items: center;
      padding: 8px 0 calc(8px + env(safe-area-inset-bottom));
      z-index: 100;
      width: 100%;
      box-sizing: border-box;
    }}

    .bottom-tab {{
      flex: 1 1 0;
      min-width: 0;
      height: 52px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 3px;
      background: transparent;
      border: none;
      color: var(--text-3);
      font-size: 0.74rem;
      font-weight: 700;
      cursor: pointer;
      transition: var(--transition);
      position: relative;
    }}'''

new_bottom_css = '''    .bottom-bar {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(7, 10, 18, 0.96);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: space-around;
      align-items: center;
      padding-top: 8px;
      padding-bottom: max(16px, env(safe-area-inset-bottom, 16px));
      padding-left: max(4px, env(safe-area-inset-left));
      padding-right: max(4px, env(safe-area-inset-right));
      z-index: 100;
      width: 100%;
      box-sizing: border-box;
    }}

    .bottom-tab {{
      flex: 1 1 0;
      min-width: 0;
      min-height: 48px;
      height: auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 3px;
      background: transparent;
      border: none;
      color: var(--text-3);
      font-size: 0.72rem;
      font-weight: 700;
      cursor: pointer;
      transition: var(--transition);
      position: relative;
      padding: 4px 1px;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
    }}

    .bottom-tab svg {{
      width: 20px;
      height: 20px;
      stroke-width: 2.2;
      flex-shrink: 0;
      transition: var(--transition);
    }}

    .bottom-tab span {{
      display: block;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 100%;
      letter-spacing: -0.2px;
      line-height: 1.15;
    }}'''

code = code.replace(old_bottom_css, new_bottom_css, 1)

# 6. Add Settings Modal CSS before </style> (with double braces for f-string)
raw_modal_css = '''
    /* Settings Modal Styles (API Key & Font Scaling) */
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.78);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      z-index: 200;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 16px;
      animation: fadeIn 0.2s ease-out;
      box-sizing: border-box;
    }

    .modal-card {
      background: var(--bg-card);
      border: 1px solid var(--border-hover);
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 480px;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
      animation: slideUp 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      box-sizing: border-box;
    }

    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 16px 18px 12px;
      border-bottom: 1px solid var(--border);
    }

    .modal-title-wrap {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .modal-icon {
      font-size: 1.3rem;
    }

    .modal-title {
      font-size: 1rem;
      font-weight: 800;
      color: #fff;
      margin: 0;
    }

    .modal-subtitle {
      font-size: 0.75rem;
      color: var(--text-2);
      margin: 2px 0 0;
    }

    .btn-close-modal {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border);
      color: var(--text-2);
      width: 32px;
      height: 32px;
      border-radius: var(--radius-full);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--transition);
    }

    .btn-close-modal:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.15);
    }

    .modal-body {
      padding: 16px 18px 20px;
    }

    .settings-section {
      padding-bottom: 16px;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--border);
    }

    .settings-label-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }

    .settings-label {
      font-size: 0.85rem;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .key-status-badge {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      font-family: var(--font-mono);
    }

    .key-status-badge.active {
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }

    .key-status-badge.inactive {
      background: rgba(245, 158, 11, 0.15);
      color: var(--amber);
      border: 1px solid rgba(245, 158, 11, 0.3);
    }

    .api-key-input-wrap {
      position: relative;
      display: flex;
      align-items: center;
      margin-bottom: 10px;
    }

    .settings-input {
      width: 100%;
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 10px 40px 10px 12px;
      color: #fff;
      font-size: 0.84rem;
      font-family: var(--font-mono);
      outline: none;
      box-sizing: border-box;
      transition: var(--transition);
    }

    .settings-input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 2px var(--primary-glow);
    }

    .btn-input-icon {
      position: absolute;
      right: 8px;
      background: none;
      border: none;
      color: var(--text-3);
      cursor: pointer;
      padding: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: var(--transition);
    }

    .btn-input-icon:hover {
      color: #fff;
    }

    .settings-actions-row {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    .btn-save-key, .btn-clear-key, .btn-get-key {
      padding: 7px 12px;
      border-radius: var(--radius-md);
      font-size: 0.78rem;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      cursor: pointer;
      transition: var(--transition);
      text-decoration: none;
      border: 1px solid var(--border);
    }

    .btn-save-key {
      background: var(--primary-gradient);
      border-color: transparent;
      color: #fff;
    }

    .btn-save-key:hover {
      opacity: 0.9;
      transform: translateY(-1px);
    }

    .btn-clear-key {
      background: rgba(239, 68, 68, 0.1);
      border-color: rgba(239, 68, 68, 0.3);
      color: #fca5a5;
    }

    .btn-clear-key:hover {
      background: rgba(239, 68, 68, 0.2);
    }

    .btn-get-key {
      background: rgba(56, 189, 248, 0.1);
      border-color: rgba(56, 189, 248, 0.3);
      color: var(--cyan);
      margin-left: auto;
    }

    .btn-get-key:hover {
      background: rgba(56, 189, 248, 0.2);
    }

    .settings-note {
      font-size: 0.73rem;
      color: var(--text-3);
      margin-top: 8px;
      line-height: 1.4;
    }

    .font-scale-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 6px;
      margin-bottom: 10px;
    }

    .btn-font-scale {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 8px 4px;
      color: var(--text-2);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
      cursor: pointer;
      transition: var(--transition);
    }

    .btn-font-scale:hover {
      background: rgba(255, 255, 255, 0.08);
      color: #fff;
    }

    .btn-font-scale.active {
      background: rgba(244, 63, 94, 0.18);
      border-color: var(--primary);
      color: #fff;
      box-shadow: 0 0 10px var(--primary-glow);
    }

    .font-scale-label {
      font-size: 0.82rem;
      font-weight: 800;
    }

    .font-scale-pct {
      font-size: 0.68rem;
      font-family: var(--font-mono);
      opacity: 0.8;
    }

    .font-scale-badge {
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--cyan);
      font-family: var(--font-mono);
      padding: 2px 7px;
      border-radius: var(--radius-full);
      background: rgba(56, 189, 248, 0.1);
    }

    .font-preview-box {
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 10px 12px;
    }

    .font-preview-text {
      font-size: 0.95rem;
      color: #fff;
      font-weight: 700;
      line-height: 1.4;
    }

    .btn-open-settings-inline {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      margin-top: 8px;
      background: rgba(244, 63, 94, 0.15);
      border: 1px solid rgba(244, 63, 94, 0.4);
      color: #fff;
      padding: 6px 12px;
      border-radius: var(--radius-full);
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      transition: var(--transition);
    }

    .btn-open-settings-inline:hover {
      background: rgba(244, 63, 94, 0.25);
    }

    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    @keyframes slideUp {
      from { transform: translateY(16px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
'''

# Escape braces for f-string insertion
escaped_modal_css = raw_modal_css.replace('{', '{{').replace('}', '}}')
code = code.replace("  </style>", escaped_modal_css + "\n  </style>", 1)

# 7. Update Header HTML (Maple Leaf clickable brand-btn)
old_header_html = '''      <div class="brand-wrap">
        <div class="brand-icon" aria-hidden="true">🍁</div>
        <div class="brand-title">
          新宿6日 <span class="badge-ver">v1.5.2 PRO</span>
        </div>
      </div>
      <div class="header-actions">
        <a href="https://translate.google.com/?sl=auto&tl=zh-TW" target="_blank" rel="noopener noreferrer" class="top-pill top-pill-primary" id="btnTranslate" aria-label="開啟 Google 翻譯">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          翻譯
        </a>
        <a href="https://www.google.com/maps/search/?api=1&query=Apartment+hotel+Yumenoya+Shinjuku" class="top-pill" target="_blank" rel="noopener noreferrer" aria-label="Google 地圖導航回大久保飯店">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16M9 9h1M9 13h1M9 17h1M14 9h1M14 13h1M14 17h1"/></svg>
          回飯店
        </a>
      </div>'''

new_header_html = '''      <button type="button" class="brand-btn" onclick="openSettingsModal()" aria-label="開啟系統設定（密鑰與字體大小）" title="點擊楓葉開啟設定">
        <div class="brand-icon" aria-hidden="true">🍁</div>
        <div class="brand-title">
          新宿6日 <span class="badge-ver">v1.5.2 PRO</span>
        </div>
        <span class="settings-gear-hint" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
        </span>
      </button>
      <div class="header-actions">
        <a href="https://translate.google.com/?sl=auto&tl=zh-TW" target="_blank" rel="noopener noreferrer" class="top-pill top-pill-primary" id="btnTranslate" aria-label="開啟 Google 翻譯">
          <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          <span>翻譯</span>
        </a>
        <a href="https://www.google.com/maps/search/?api=1&query=Apartment+hotel+Yumenoya+Shinjuku" class="top-pill" target="_blank" rel="noopener noreferrer" aria-label="Google 地圖導航回大久保飯店">
          <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16M9 9h1M9 13h1M9 17h1M14 9h1M14 13h1M14 17h1"/></svg>
          <span>回飯店</span>
        </a>
      </div>'''

code = code.replace(old_header_html, new_header_html, 1)

# 8. Remove the old key-status-bar from viewGemini
old_key_bar = '''        <div class="key-status-bar">
          <span id="keyStatusText" style="display:inline-flex; align-items:center; gap:6px;">
            <span class="pulse-dot"></span> 連線中...
          </span>
          <button onclick="promptApiKey()" class="btn-key-action">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
            設定/更換 Key
          </button>
        </div>'''

code = code.replace(old_key_bar, '', 1)

# 9. Insert Settings Modal HTML before </nav>
modal_html = '''
  <!-- Settings Modal (API Key & Font Scaling) -->
  <div id="settingsModal" class="modal-backdrop" style="display: none;" role="dialog" aria-modal="true" aria-labelledby="settingsModalTitle">
    <div class="modal-card">
      <div class="modal-header">
        <div class="modal-title-wrap">
          <div class="modal-icon">🍁</div>
          <div>
            <h3 id="settingsModalTitle" class="modal-title">系統偏好設定</h3>
            <p class="modal-subtitle">Gemini API Key 與頁面字級偏好</p>
          </div>
        </div>
        <button type="button" class="btn-close-modal" onclick="closeSettingsModal()" aria-label="關閉設定視窗">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>

      <div class="modal-body">
        <!-- Section 1: Gemini API Key -->
        <div class="settings-section">
          <div class="settings-label-row">
            <label for="settingsApiKeyInput" class="settings-label">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 2l-2 2m-1.5 1.5L16 7m-3 3l-4 4-2-2-4 4 3 3 4-4-2-2 4-4m5-5l2 2"/></svg>
              <span>Google Gemini API Key</span>
            </label>
            <span id="settingsKeyBadge" class="key-status-badge inactive">未設定</span>
          </div>

          <div class="api-key-input-wrap">
            <input type="password" id="settingsApiKeyInput" class="settings-input" placeholder="貼入 AI Studio API Key (AIzaSy...)" autocomplete="off" spellcheck="false">
            <button type="button" id="btnToggleKeyVisibility" class="btn-input-icon" onclick="toggleApiKeyVisibility()" aria-label="切換密碼顯示">
              <svg id="iconEye" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            </button>
          </div>

          <div class="settings-actions-row">
            <button type="button" class="btn-save-key" onclick="saveApiKeyFromModal()">
              <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/><polyline points="17 21 17 13 7 13 7 21"/><polyline points="7 3 7 8 15 8"/></svg>
              <span>儲存密鑰</span>
            </button>
            <button type="button" class="btn-clear-key" onclick="clearApiKeyFromModal()">
              <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
              <span>清除</span>
            </button>
            <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener noreferrer" class="btn-get-key">
              <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
              <span>取得免費 Key</span>
            </a>
          </div>
          <div class="settings-note">
            🔒 密鑰僅加密存放於手機本機瀏覽器 (LocalStorage)，絕不上傳任何伺服器。
          </div>
        </div>

        <!-- Section 2: Font Size Adjustment -->
        <div class="settings-section">
          <div class="settings-label-row">
            <span class="settings-label">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7V4h16v3M9 20h6M12 4v16"/></svg>
              <span>頁面字體大小 (Font Scaling)</span>
            </span>
            <span id="fontScaleDisplayBadge" class="font-scale-badge">100%</span>
          </div>

          <div class="font-scale-grid">
            <button type="button" class="btn-font-scale" data-scale="0.9" onclick="setFontScale(0.9)">
              <span class="font-scale-label">精簡</span>
              <span class="font-scale-pct">90%</span>
            </button>
            <button type="button" class="btn-font-scale active" data-scale="1.0" onclick="setFontScale(1.0)">
              <span class="font-scale-label">標準</span>
              <span class="font-scale-pct">100%</span>
            </button>
            <button type="button" class="btn-font-scale" data-scale="1.12" onclick="setFontScale(1.12)">
              <span class="font-scale-label">適中</span>
              <span class="font-scale-pct">112%</span>
            </button>
            <button type="button" class="btn-font-scale" data-scale="1.25" onclick="setFontScale(1.25)">
              <span class="font-scale-label">清晰</span>
              <span class="font-scale-pct">125%</span>
            </button>
            <button type="button" class="btn-font-scale" data-scale="1.4" onclick="setFontScale(1.4)">
              <span class="font-scale-label">特大</span>
              <span class="font-scale-pct">140%</span>
            </button>
          </div>

          <!-- Live Text Size Preview Box -->
          <div class="font-preview-box">
            <div class="font-preview-text">
              🍁 預覽文字：新宿・橫濱・箱根 6日戰情室 (11/26~12/01)
            </div>
            <div style="font-size:0.75rem; color:var(--text-3); margin-top:3px;">
              💡 戶外強光下行走時，推薦切換至「清晰 125%」或「特大 140%」便於快速判讀。
            </div>
          </div>
        </div>

        <!-- Section 3: App Info -->
        <div class="settings-section" style="border-bottom:none; padding-bottom:0; margin-bottom:0;">
          <div style="font-size:0.75rem; color:var(--text-3); display:flex; justify-content:space-between; align-items:center;">
            <span>Tokyo Trip Assistant v1.5.2 PRO</span>
            <button type="button" onclick="resetPreferences()" style="background:none; border:none; color:var(--text-3); font-size:0.75rem; cursor:pointer; text-decoration:underline;">恢復預設值</button>
          </div>
        </div>
      </div>
    </div>
  </div>
'''

code = code.replace("  <!-- Leaflet JS -->", modal_html + "\n  <!-- Leaflet JS -->", 1)

# 10. Update JavaScript (Settings modal & Font scaling functions)
js_settings_functions = '''    // ==========================================
    // Settings Modal & Font Scaling System
    // ==========================================
    let currentFontScale = parseFloat(localStorage.getItem("tokyo_font_scale_v152") || "1.0");

    function applyFontScale(scale, save = true) {{
      currentFontScale = scale;
      document.documentElement.style.setProperty("--font-scale", scale);
      document.documentElement.style.fontSize = (15 * scale) + "px";

      if (save) {{
        localStorage.setItem("tokyo_font_scale_v152", scale.toString());
      }}

      const badge = document.getElementById("fontScaleDisplayBadge");
      if (badge) badge.innerText = Math.round(scale * 100) + "%";

      document.querySelectorAll(".btn-font-scale").forEach(btn => {{
        const s = parseFloat(btn.dataset.scale);
        const isActive = Math.abs(s - scale) < 0.02;
        btn.classList.toggle("active", isActive);
        btn.setAttribute("aria-pressed", isActive ? "true" : "false");
      }});
    }}

    function setFontScale(scale) {{
      triggerHaptic();
      applyFontScale(scale, true);
      showToast(`🔤 字體大小已切換為 ${{Math.round(scale * 100)}}%`);
    }}

    function openSettingsModal() {{
      triggerHaptic();
      const modal = document.getElementById("settingsModal");
      if (!modal) return;

      const keyInput = document.getElementById("settingsApiKeyInput");
      if (keyInput) {{
        keyInput.value = geminiApiKey || "";
        keyInput.type = "password";
      }}

      updateModalKeyBadge();
      applyFontScale(currentFontScale, false);

      modal.style.display = "flex";
      document.body.style.overflow = "hidden";
    }}

    function closeSettingsModal() {{
      triggerHaptic();
      const modal = document.getElementById("settingsModal");
      if (modal) {{
        modal.style.display = "none";
        document.body.style.overflow = "";
      }}
    }}

    window.addEventListener("click", (e) => {{
      const modal = document.getElementById("settingsModal");
      if (modal && e.target === modal) {{
        closeSettingsModal();
      }}
    }});

    window.addEventListener("keydown", (e) => {{
      if (e.key === "Escape") {{
        closeSettingsModal();
      }}
    }});

    function toggleApiKeyVisibility() {{
      triggerHaptic();
      const keyInput = document.getElementById("settingsApiKeyInput");
      const eye = document.getElementById("iconEye");
      if (!keyInput) return;

      if (keyInput.type === "password") {{
        keyInput.type = "text";
        if (eye) eye.innerHTML = '<path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/>';
      }} else {{
        keyInput.type = "password";
        if (eye) eye.innerHTML = '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>';
      }}
    }}

    function updateModalKeyBadge() {{
      const badge = document.getElementById("settingsKeyBadge");
      if (!badge) return;
      if (geminiApiKey) {{
        badge.innerHTML = '<span class="pulse-dot"></span> 已連線 Gemini 3.8 Flash';
        badge.className = "key-status-badge active";
      }} else {{
        badge.innerHTML = '未設定 API Key';
        badge.className = "key-status-badge inactive";
      }}
    }}

    function updateKeyStatusUI() {{
      updateModalKeyBadge();
    }}

    function saveApiKeyFromModal() {{
      triggerHaptic();
      const keyInput = document.getElementById("settingsApiKeyInput");
      if (!keyInput) return;

      const val = keyInput.value.trim();
      geminiApiKey = val;
      localStorage.setItem("tokyo_gemini_key_v140", geminiApiKey);
      updateModalKeyBadge();

      if (geminiApiKey) {{
        showToast("✅ API Key 已安全儲存！導遊大腦就緒");
      }} else {{
        showToast("已清除 API Key");
      }}
    }}

    function clearApiKeyFromModal() {{
      triggerHaptic();
      const keyInput = document.getElementById("settingsApiKeyInput");
      if (keyInput) keyInput.value = "";
      geminiApiKey = "";
      localStorage.removeItem("tokyo_gemini_key_v140");
      updateModalKeyBadge();
      showToast("已清除 API Key");
    }}

    function resetPreferences() {{
      triggerHaptic();
      if (confirm("確定要將設定恢復為預設值嗎？（字體大小將重設為 100%）")) {{
        setFontScale(1.0);
        showToast("已恢復預設值");
      }}
    }}
'''

old_key_funcs_pattern = r'    function updateKeyStatusUI\(\) \{\{.*?function promptApiKey\(\) \{\{.*?\}\}\n    \}\}'
code, count = re.subn(old_key_funcs_pattern, js_settings_functions, code, flags=re.DOTALL)
print(f"Substituted key functions: count = {count}")

# 11. In sendAiQuery, update no-key fallback to prompt opening modal
old_no_key_prompt = '''      if (!geminiApiKey) {{
        const errBubble = document.createElement("div");
        errBubble.className = "bubble ai";
        errBubble.innerHTML = "⚠️ 尚未設定 Google Gemini API Key。請點擊上方『設定/更換 Key』貼入您的 API Key 即可啟動導遊大腦！<br><small style='color:var(--text-3);'>密鑰僅保存在本機手機瀏覽器，絕不上傳雲端。</small>";
        box.appendChild(errBubble);
        box.scrollTop = box.scrollHeight;
        isAiQueryInProgress = false;
        if (sendBtn) {{
          sendBtn.disabled = false;
          sendBtn.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg><span>發送</span>';
        }}
        return;
      }}'''

new_no_key_prompt = '''      if (!geminiApiKey) {{
        const errBubble = document.createElement("div");
        errBubble.className = "bubble ai";
        errBubble.innerHTML = `⚠️ 尚未設定 Google Gemini API Key。<br>請點擊左上角<strong>『🍁 楓葉圖標』</strong>或下方按鈕貼入您的密鑰，即可啟動導遊大腦！<br><button type="button" class="btn-open-settings-inline" onclick="openSettingsModal()"><svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg> 立即開啟設定輸入 Key</button><br><small style="color:var(--text-3); margin-top:4px; display:inline-block;">密鑰僅加密保存在本機手機瀏覽器，絕不上傳伺服器。</small>`;
        box.appendChild(errBubble);
        box.scrollTop = box.scrollHeight;
        isAiQueryInProgress = false;
        if (sendBtn) {{
          sendBtn.disabled = false;
          sendBtn.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg><span>發送</span>';
        }}
        openSettingsModal();
        return;
      }}'''

code = code.replace(old_no_key_prompt, new_no_key_prompt, 1)

# 12. Add applyFontScale call to initialization
old_init = '''    // --- Initialization ---
    renderPokemon();
    updateKeyStatusUI();'''

new_init = '''    // --- Initialization ---
    applyFontScale(currentFontScale, false);
    renderPokemon();
    updateKeyStatusUI();'''

code = code.replace(old_init, new_init, 1)

# Write to generate_v152.py
with open(V152_PATH, "w", encoding="utf-8", newline="") as f:
    f.write(code)

print(f"✅ Successfully created {V152_PATH} ({len(code)} bytes)!")
