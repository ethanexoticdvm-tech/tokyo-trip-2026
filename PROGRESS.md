# 專案進度與架構快照 (PROGRESS.md)
> 快照時間：2026-11-04 23:40:00 (v1.5.2 PRO 封裝完成)

## 1. 核心目標
- **專案定位**：`tokyo-trip-assistant` (新宿・橫濱・箱根 6日遊隨身戰情室)
- **當前版本**：`v1.5.2 PRO` (極致無破圖自適應 ＋ 楓葉偏好設定視窗 ＋ 全域字體縮放 ＋ AI純淨版)
- **核心目標**：為使用者及全家 2 大 2 小（11 歲與 12 歲青少年國小高年級/國中生，2026/11/26～12/01）提供出國隨身攜帶、整合 Gemini 3.8 Flash 實時時空雙感知、5 大導遊實質決策模式與 Funliday 動態行程聯動的手機端旅行戰情指揮中心。

## 2. 已完成工作 (Completed)
- [x] **5大截圖問題全面修復與手機極限自適應重構 (v1.5.2 PRO)**：
  - 🍁 **楓葉點擊進入設定彈窗 (`#settingsModal`)**：頂欄左側品牌按鈕改為彈性按鈕（內含 🍁 圖標、版本號、小齒輪，點擊帶 `navigator.vibrate` 觸感）。整合 **Google Gemini API Key 管理**（明文/密文眼睛切換、儲存、清除、狀態晶片、AI Studio 免費連結）與 **5 段字體縮放系統**（90%、100%、112%、125%、140%，即時切換 `--font-scale` 與 `html` 基準根字級，localStorage 持久化）。
  - ✂️ **刪除 AI 大腦舊版冗餘 API 佔位卡片**：自 `#viewGemini` 分頁徹底移除 `.key-status-bar`，釋放垂直空間；若未填 Key 提問，自動於對話泡泡引導一鍵開啟楓葉設定。
  - ✂️ **徹底扣除頂部 Hero 卡片**：完全清除 `FAMILY TOKYO TRIP` 橫幅，首屏直接以 Funliday 實時行程開展。
  - 📐 **修復「下方破圖」**：`.bottom-bar` 底部內距升級為 `max(16px, env(safe-area-inset-bottom, 16px))`，`.bottom-tab` 改為自適應高度與文字溢出保護，Android 虛擬手勢條與 iOS Home Indicator 100% 避讓，零壓字。
  - 📱 **修復「右側破圖」與全站自適應加強**：頂欄邊距微調至 10px，按鈕彈性收縮；加入 `@media (max-width: 375px)` 窄螢幕斷點（自動隱藏微型版本徽章），全站套用 `*, *::before, *::after { box-sizing: border-box; }` 與 `html, body { max-width: 100vw; overflow-x: hidden; }`，360px~375px 窄螢幕 100% 容納無橫向捲軸。
- [x] **無頭 Chrome (CDP) 自動化測試與像素級驗證 (0 Errors / 0 Warnings)**：
  - `ai-engine/e2e_browser_test.mjs`：8 大單元端對端測試全數通過（5 大分頁、5 種模式、打卡持久化、地圖平移、死線切換、話題管理、0 運行時例外與 0 主控台錯誤）。
  - `ai-engine/capture_cdp_screenshots.mjs`：全真機 390x844 與 375x667 像素截圖生成，留存於專案 artifacts。
- [x] **EGM 深度代碼審查與前置缺陷修復 (v1.5.1 PRO)**：
  - 🔴 動態 DOM 破壞致命修復 (`pokePercentText` 獨立節點重構)。
  - 🛡️ 本地儲存韌性防禦 (`safeGetJson` 攔截損壞快取)。
  - ⏱️ 35 秒 AbortController 弱網超時中斷與狀態防呆。
  - 🈳 CJK IME 拼字 Enter 防誤送 (`!event.isComposing`)。
- [x] **雙軌發布與跨設備同步**：
  - 🚀 **GitHub Pages**：已自動部署至 `https://ethanexoticdvm-tech.github.io/tokyo-trip-2026/`
  - 💾 **Google Drive 交付目錄**：已產出至 `G:\我的雲端硬碟\AI-Programe\新宿6日遊隨身戰情室_v1.5.2\`
  - 🔄 **Bare Repo**：已推送至 `G:\我的雲端硬碟\antigravity_repos\tokyo-trip-assistant.git`

## 3. 關鍵架構決策與重要檔案
- **核心單檔入口**：[`index.html`](file:///c:/Users/inche/Antigravity/tokyo-trip-assistant/index.html)（自包含所有 CSS/JS/離線資源，免伺服器直接離線雙擊運行）。
- **生成與建置引擎**：[`ai-engine/generate_v152.py`](file:///c:/Users/inche/Antigravity/tokyo-trip-assistant/ai-engine/generate_v152.py)（集中管理知識庫與 HTML 模板，單元維護）。
- **跨平台雙機啟動器**：`啟動_隨身戰情室.bat`（診斷與自適應）與 `啟動_隨身戰情室.vbs`（靜默啟動）。
- **字體縮放架構**：採用 CSS 變數 `--font-scale` 配合動態 `html.style.fontSize`，全站所有尺寸依 `rem` 等比縮放，不破壞排版佈局。
- **邊距防禦原則**：涉及手機邊緣浮動元素，一律強制 `max(16px, env(safe-area-...))` 雙重保險。

## 4. 測試與驗證方法
1. **端對端自動化測試**：`node ai-engine/e2e_browser_test.mjs`（驗證全站邏輯、分頁切換與 0 異常）。
2. **無頭 CDP 截圖產出**：`node ai-engine/capture_cdp_screenshots.mjs`（於 390px/375px 真實尺寸擷取渲染畫面）。
3. **本機快速開起**：雙擊 `啟動_隨身戰情室.bat` 或在終端輸入 `cmd.exe /c 啟動_隨身戰情室.bat`。

## 5. 下一步待辦事項 (Next Steps)
1. **出發前行前檢核 (11月中旬)**：
   - 橫濱紅磚倉庫聖誕市集 asoview! 優先入場券開賣搶票。
   - TableCheck 新宿牛舌檸檬訂位代碼與人數最終覆核。
2. **家人實機手機測試**：
   - 請家人以手機瀏覽器開啟 GitHub Pages 網址，實測設定彈窗（API Key 與字體大小調整）及離線車票與寶可夢打卡。

## 6. 給接續 Agent 的執行建議
- 本專案採用純靜態高相容性單檔架構，任何 HTML/CSS/JS 修改建議透過 `ai-engine/generate_v152.py`（或後續遞增版本）產生，避免手動編輯 `index.html` 時發生標籤未閉合或特殊字元轉義問題。
- 每次更動後必須執行 `node ai-engine/e2e_browser_test.mjs` 確保 0 console errors，並依全域規範自動遞增版本號及同步交付至 Google Drive。
