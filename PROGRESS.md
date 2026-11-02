# 專案進度與架構快照 (PROGRESS.md)

## 1. 專案目標與定位
- **專案名稱**：`tokyo-trip-assistant` (新宿・橫濱・箱根 6日遊隨身戰情室)
- **當前版本**：`v1.1.0` (自適應旗艦版 ＋ GitHub Pages 雲端發布)
- **核心目標**：為使用者及全家 2 大 2 小（2026/11/26～12/01）提供出國隨身攜帶、離線可用、整合 Gemini 3.8 Flash AI 大腦與 Google 翻譯的手機端一頁式旅行戰情指揮中心。

---

## 2. 已完成工作 (Done)
- [x] **行程深度稽核與衝突修正**：
  - 修正 Day 4 浪漫特快與江之島仲見世通時差（對齊 08:20 新宿出發車次）。
  - 鎖定 Day 5 箱根大環線 07:37 新宿出發、15:15 大涌谷下山死線、17:46 回程浪漫特快。
  - 修正 Day 3 橫濱紅磚倉庫聖誕市集最新收費與優先入場資訊。
  - 提醒 Day 4 鎌倉往長谷寺認明「江之電」（切勿搭單軌電車）。
- [x] **單一獨立 PWA / Web App 建置 (v1.1.0)**：
  - 自適應排版（適配 iPhone 動態島/瀏海屏與 Android 安全區）。
  - 離線車票速查卡（EXE10 / MSE6 車次與 4 車 8C/8D/9C/9D 座位）。
  - 橫濱 7 大寶可夢人孔蓋打卡任務（LocalStorage 本機獨立記憶 ＋ Maps 導航）。
  - 8 大實戰日文手指卡（點擊超大字體全螢幕彈窗）。
  - 頂部 Google 翻譯 App 智慧跳轉（iOS/Android 原生協議）。
  - 對接 Google 最新 `gemini-3.8-flash` 隨身導遊大腦（內建 5 大快捷提問晶片）。
- [x] **零外洩安全架構落盤**：
  - 程式碼 100% 零硬編碼 API Key。
  - API Key 僅儲存於使用者各自行動設備的 `localStorage`。
- [x] **雙軌發布與跨設備同步就緒**：
  - **GitHub Pages**：已正式部署至 `https://ethanexoticdvm-tech.github.io/tokyo-trip-2026/`（狀態：200 OK）。
  - **Google Drive Bare Repo**：已註冊並同步至 `G:\我的雲端硬碟\antigravity_repos\tokyo-trip-assistant.git`。
  - **Google Drive 交付目錄**：`G:\我的雲端硬碟\AI-Programe\新宿6日遊隨身戰情室_v1.1.0\`。

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
