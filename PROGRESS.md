# 專案進度與架構快照 (PROGRESS.md)

## 1. 專案目標與定位
- **專案名稱**：`tokyo-trip-assistant` (新宿・橫濱・箱根 6日遊隨身戰情室)
- **當前版本**：`v1.2.0` (Funliday 原生直通 ＋ Gemini 3.8 Flash 多輪上下文記憶版)
- **核心目標**：為使用者及全家 2 大 2 小（2026/11/26～12/01）提供出國隨身攜帶、離線可用、整合 Gemini 3.8 Flash 多輪對話記憶與 Funliday 動態行程聯動的手機端一頁式旅行戰情指揮中心。

---

## 2. 已完成工作 (Done)
- [x] **Gemini 3.8 Flash 多輪連貫對話記憶 (Multi-turn Memory)**：
  - 徹底解決手機端 AI 無上下文記憶、無法延續討論問題。
  - 對話歷史以結構化 JSON 陣列存入手機 `localStorage`，重新整理或關閉分頁對話紀錄不遺失。
  - 注入完整 6 天精確行程、班次座位、死線備忘與飯店座標知識庫。
  - 附帶「清空對話紀錄」按鈕隨時重啟話題。
- [x] **Funliday 原生實時聯動 (Native App Linking)**：
  - 行程部分移除重複的靜態清單，全面升級為「一鍵直達 Funliday App / 網頁版」。
  - 後續任何動態調動皆直接以 Funliday 為準，手機 Web App 永遠保持最新狀態。
- [x] **橫濱 7 大寶可夢尋寶打卡全數保留**：
  - 完整保留 7 大皮卡丘人孔蓋與立體郵筒座標導航、獨立打卡記憶與進度計算。
- [x] **離線車票速查、核心死線告警、實戰日文手指卡、Google 翻譯 App 直達全數到位**。
- [x] **零外洩安全架構**：
  - 程式碼 100% 零硬編碼 API Key，密鑰僅加密儲存於手機端本機。
- [x] **雙軌發布與跨設備同步就緒**：
  - **GitHub Pages**：已正式部署至 `https://ethanexoticdvm-tech.github.io/tokyo-trip-2026/`。
  - **Google Drive Bare Repo**：已註冊並同步至 `G:\我的雲端硬碟\antigravity_repos\tokyo-trip-assistant.git`。
  - **Google Drive 交付目錄**：`G:\我的雲端硬碟\AI-Programe\新宿6日遊隨身戰情室_v1.2.0\`。

---

## 3. 關鍵架構與設計決策
1. **單檔極簡架構 (Single-File Architecture)**：
   - 全 HTML/CSS/JS 合一於 `index.html`，零外部打包依賴，離線秒開，極速省流量。
2. **多端同步機制 (Dual Remote Strategy)**：
   - `origin` 指向 GitHub（供 GitHub Pages 公開部署與全家手機隨時刷新）。
   - `gdrive` 指向 Google Drive Bare Repo（供跨電腦開發與版本備份）。
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

---

## 5. 驗證與測試方式
- **本地預覽**：雙擊 `G:\我的雲端硬碟\AI-Programe\新宿6日遊隨身戰情室_v1.1.0\啟動_本機預覽.bat`。
- **線上驗證**：手機瀏覽器訪問 `https://ethanexoticdvm-tech.github.io/tokyo-trip-2026/`。
- **同步測試**：執行 `python C:\Users\inche\.gemini\antigravity\tools\sync_engine\sync_core.py --sync tokyo-trip-assistant`。
