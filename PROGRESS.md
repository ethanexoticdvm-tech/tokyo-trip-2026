# 專案進度與架構快照 (PROGRESS.md)

## 1. 專案目標與定位
- **專案名稱**：`tokyo-trip-assistant` (新宿・橫濱・箱根 6日遊隨身戰情室)
- **當前版本**：`v1.4.0` (AI實時時間/GPS雙感知 ＋ 多話題Session管理 ＋ Funliday動態異動覆蓋版)
- **核心目標**：為使用者及全家 2 大 2 小（2026/11/26～12/01）提供出國隨身攜帶、極致俐落、整合 Gemini 3.8 Flash 實時時空環境感知與 Funliday 動態行程聯動的手機端一頁式旅行戰情指揮中心。

---

## 2. 已完成工作 (Done)
- [x] **AI 隨身導遊大腦升級 (v1.4.0)**：
  - **實時日本時間與進度感知 (JST & Stage Engine)**：前端自動換算日本 JST 時間，自動感知旅程階段（行前 D-XX 籌備期、Day 1~6 當日上下午時段），並隱形注入每次提問。
  - **即時 GPS 空間感知與 18 大地標反向錨定**：預設啟用瀏覽器 GPS 定位 (`navigator.geolocation`)，透過 Haversine 公式即時計算距離最近之 18 處行程核心錨點（如新宿東南口、橫濱泡麵館、箱根元箱根港），提問時自動注入，精準破解「找廁所」、「推車捷徑（非 Google Map 盲區）」與「在地電梯連通道」。
  - **多話題 Session 管理系統 (Multi-Topic Manager)**：
    - 支援獨立開新話題（「➕ 新話題」）、自由切換、重新命名、刪除與本話題記憶清空。
    - 採用手機本機 LocalStorage 儲存，零延遲、離線可用、關閉分頁絕不遺失。
    - 支援「📥 備份」一鍵導出所有話題 JSON 歸檔，解決雲端同步依賴痛點。
  - **Funliday 行程動態異動覆蓋 (Dynamic Itinerary Override)**：
    - 提供摺疊式「📝 行程臨時異動備忘」，在手機上輸入臨時改動（例如取消景點或改時間），AI 每次發話自動優先依此重整順路推算與死線告警。
- [x] **底欄防破圖與 Android Intent 適配 (v1.3.1)**：
  - 底欄 5 大模組絕對防破圖：寶可夢標籤純文字、打卡獨立紅色 Badge、按鈕等比平分。
  - Android Intent 喚起 Funliday 原生 App，未安裝時自動平滑切換至 Chrome 網頁版。
- [x] **界面極簡化與架構精粹 (v1.3.0)**：
  - 移除頂部橫向滑動列與手指日語卡，全面下移至單一底部導航。
- [x] **iOS Standalone PWA 零閃退防護 (v1.2.1 基礎)**：
  - 原生獨立通道防止 iOS PWA 閃退。
- [x] **零外洩安全架構**：
  - 程式碼 100% 零硬編碼 API Key，密鑰加密儲存於手機本地。
- [x] **雙軌發布與跨設備同步就緒**：
  - **GitHub Pages**：部署至 `https://ethanexoticdvm-tech.github.io/tokyo-trip-2026/`。
  - **Google Drive Bare Repo**：同步至 `G:\我的雲端硬碟\antigravity_repos\tokyo-trip-assistant.git`。
  - **Google Drive 交付目錄**：`G:\我的雲端硬碟\AI-Programe\新宿6日遊隨身戰情室_v1.4.0\`。

---

## 3. 關鍵架構與設計決策
1. **隱形雙感知協定 (Hidden Dynamic Context Injection)**：
   - 使用者聊天畫面上僅保留精簡乾淨的輸入文字，而在背景送出給 Gemini 時，前端自動包裝包含 JST 時間、Day 進度、即時 GPS 座標/地標距離、旅客成員（2大2小推車避辣）與自訂行程異動的結構化情境快照。
2. **本機優先多話題儲存 (Local-First Multi-Session Storage)**：
   - 避免每發一句話就去請求 Google Drive API 造成漫遊卡頓或 Token 失效，保證出國現場 0 延遲秒開秒回。
3. **Funliday 實時動態更動 0 秒消化機制**：
   - 旅客在對話中告知或填寫覆蓋欄，AI 大腦立刻在當前話題以新時間表為準，重新驗算順路與死線。

---

## 4. 下一步待辦事項 (Next Steps)
1. **出發前一週 (11月中旬)**：
   - 複核橫濱紅磚倉庫聖誕市集 asoview! 優先入場票開賣與購票狀態。
   - 複核 Day 1 新宿牛舌檸檬 TableCheck 訂位代碼。
2. **家人手機部署實機測試**：
   - 請家人以手機打開網址並測試多話題建立、GPS 定位授權與 AI 提問。
