# 專案進度與架構快照 (PROGRESS.md)

## 1. 專案目標與定位
- **專案名稱**：`tokyo-trip-assistant` (新宿・橫濱・箱根 6日遊隨身戰情室)
- **當前版本**：`v1.3.0` (極簡單一底欄 ＋ 移除日語手指卡專版)
- **核心目標**：為使用者及全家 2 大 2 小（2026/11/26～12/01）提供出國隨身攜帶、極致俐落、整合 Gemini 3.8 Flash 多輪對話記憶與 Funliday 動態行程聯動的手機端一頁式旅行戰情指揮中心。

---

## 2. 已完成工作 (Done)
- [x] **界面極簡化與架構精粹 (v1.3.0)**：
  - **刪除上方冗餘導航列**：移除舊版上方橫向滑動分段列 (`.seg-bar`)，介面重心全面下移至單一底部導航。
  - **刪除日語手指溝通卡**：完全移除手指卡清單與放大彈窗，介面視覺負擔降低 30%。
  - **精煉 5 大底欄核心入口**：Funliday (✈️)、AI大腦 (🤖)、寶可夢 (⭐，附即時打卡計數)、核心死線 (⚡)、車票座位 (🎫)。
- [x] **iOS Standalone PWA 零閃退防護 (v1.2.1 基礎)**：
  - 徹底解決 iOS「加入主畫面」點擊外部連結閃退與 URL 覆寫問題，採用原生獨立通道 (`target="_blank" rel="noopener noreferrer"`)。
- [x] **Gemini 3.8 Flash 多輪連貫對話記憶 (Multi-turn Memory)**：
  - 對話歷史以結構化 JSON 陣列存入手機 `localStorage`，重新整理不遺失，附清空按鈕。
  - 注入 6 天完整班次座位、死線備忘與飯店座標。
- [x] **Funliday 原生實時動態聯動**：
  - 一鍵直達 Funliday App / 網頁版，任何微調直接以 Funliday 為準。
- [x] **橫濱 7 大寶可夢尋寶打卡全數保留**：
  - 7 大皮卡丘人孔蓋與立體郵筒座標導航、獨立打卡記憶與進度計算。
- [x] **零外洩安全架構**：
  - 程式碼 100% 零硬編碼 API Key，密鑰僅加密儲存於手機端本機。
- [x] **雙軌發布與跨設備同步就緒**：
  - **GitHub Pages**：部署至 `https://ethanexoticdvm-tech.github.io/tokyo-trip-2026/`。
  - **Google Drive Bare Repo**：同步至 `G:\我的雲端硬碟\antigravity_repos\tokyo-trip-assistant.git`。
  - **Google Drive 交付目錄**：`G:\我的雲端硬碟\AI-Programe\新宿6日遊隨身戰情室_v1.3.0\`。

---

## 3. 關鍵架構與設計決策
1. **極簡單檔架構 (Single-File Architecture)**：
   - 全 HTML/CSS/JS 合一於 `index.html`，零外部打包依賴，離線秒開，極速省流量。
2. **單一底部導航列 (Single Bottom Navigation)**：
   - 移除頂部重複分段按鈕，單手拇指操作更自然，視野更大。
3. **安全隔離原則**：
   - 行程公開共享，AI 密鑰本機私有化。

---

## 4. 下一步待辦事項 (Next Steps)
1. **出發前一週 (11月中旬)**：
   - 複核橫濱紅磚倉庫聖誕市集 asoview! 優先入場票開賣與購票狀態。
   - 複核 Day 1 新宿牛舌檸檬 TableCheck 訂位代碼。
2. **家人手機部署實機測試**：
   - 請家人以手機打開 GitHub Pages 網址並「加入主畫面」。
   - 測試 Google 翻譯 App 跳轉與 Google Maps 導航連結是否順暢。
