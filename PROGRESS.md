# 專案進度與架構快照 (PROGRESS.md)

## 1. 專案目標與定位
- **專案名稱**：`tokyo-trip-assistant` (新宿・橫濱・箱根 6日遊隨身戰情室)
- **當前版本**：`v1.4.3` (EGM金魚審查閉環 ＋ API穩健度與跨架構時鐘修復版)
- **核心目標**：為使用者及全家 2 大 2 小（**小孩年齡 11 歲與 12 歲國小高年級/國中生**，2026/11/26～12/01）提供出國隨身攜帶、整合 Gemini 3.8 Flash 實時時空雙感知、5 大導遊實質決策模式與 Funliday 動態行程聯動的手機端旅行戰情指揮中心。

---

## 2. 已完成工作 (Done)
- [x] **UI/UX Pro Max 戰情室全面升級 (v1.5.0)**：
  - 🎨 **OLED Tactical Midnight 戰情視覺規範**：導入 dark-mode-oled，深黑基底搭配 Aurora 柔光，達成戶外抗反光與 OLED 極致省電。
  - 📐 **全結構性向量 SVG 圖標系統**：全域剔除結構性 Emoji，全面改採 crisp 2px stroke SVG 向量圖標（Lucide 風格），跨 iOS/Android/PC 渲染一致。
  - 🔘 **觸控靶區與無障礙 (A11y/WCAG AA) 合規**：所有點擊元件強制達標 ≥44x44px 觸控靶區，對比度達 4.5:1 ~ 15:1，適配 :focus-visible 與 prefers-reduced-motion。
  - 🎫 **擬真小田急浪漫特快車票 (Skeuomorphic Ticket)**：加入左右打孔邊緣、路線指示、金色高對比大字座位車廂標籤，斷網行走時秒讀。
  - 🎮 **寶可夢進度光條與觸覺震動 (Haptic Feedback)**：新增百分比進度條與打卡震動 (
avigator.vibrate)，提升尋寶沉浸感。
  - 📅 **Funliday 6天動線分日步進器 (Day Filter Stepper)**：支援 [全部] [D1] [D2] [D3] [D4] [D5] [D6] 快速切換過濾，免除長篇滾動。
  - 🎭 **5 大導遊模式觸感膠囊 (Tactile Grid Pills)**：視覺化膠囊按鈕與實時推演說明提示框。
  - 📋 **AI 訊息一鍵複製與 Toast 浮動氣泡**：方便旅途中快速複製地址與日語問句。
- [x] **EGM 金魚審查閉環與 API 穩健度全面強化 (v1.4.3)**：
  - 🔴 **語法阻斷修復**：修復 `promptApiKey()` 內未轉義換行引發之 `SyntaxError`，保障 iOS/Android 首次載入 100% 正常。
  - 🔴 **Gemini API 交替規範防禦**：確保切片歷史 (`historySlice`) 永遠以 `user` turn 起始，阻絕 HTTP 400 Bad Request。
  - 🟡 **Thinking 思考 Token 穿透防護**：於 `ThinkingLevel: HIGH` 模式下精準過濾 `thought: true` 部分，平滑拼接多 part 文字。
  - 🟡 **防連擊並發鎖定**：引入 `isAiQueryInProgress` 狀態旗標與按鈕停用防護，避免弱網環境重複請求。
  - 🟡 **時區計算跨設備強化**：改採 `Intl.DateTimeFormat` 取得標準 `Asia/Tokyo` JST 時間，徹底杜絕跨時區/夏令時 Epoch 偏斜。
  - 🟡 **iOS Funliday App 退避回退**：iOS 端若呼叫 `funliday://` 協議無反應，1.5 秒自動優雅回退至 Web 版網址。
  - 🟢 **青少年細節與 UI 狀態同步**：歡迎訊息移除推車殘留文字，頁面初始化主動呼叫 `onModeChange()` 同步輸入框提示。
- [x] **青少年（11、12 歲）量身深度適配與去除嬰幼兒邏輯 (v1.4.1)**：
  - **全面剔除嬰兒設定**：徹底移除推車、尿布台、哺乳室與幼童安全座椅等不適用需求。
  - **體能與節奏升級**：確認 11/12 歲體能近成人、步速快、能自行爬樓梯疾走。
  - **青少年興趣與飲食鎖定**：聚焦動漫電玩（寶可夢、吉卜力、鋼彈、哥吉拉、一番賞、夾娃娃機、大型扭蛋店）、酷炫體驗（合味道杯麵 DIY、橫濱纜車、箱根海賊船、大涌谷火山黑玉子）與發育期成人份量美食小吃。
- [x] **5 大導遊實質決策模式體系 (v1.4.1)**：
  - **☕ 輕鬆模式 (Relaxed - 青少年潮玩慢活 ＋ 美食放鬆)**：`Thinking: LOW`。主動砍掉枯燥景點，推薦夾娃娃、扭蛋、一番賞與人氣街頭點心，避免青少年走太多無聊路產生厭世情緒。
  - **📝 詳細模式 (Detailed - 深度全景推演 ＋ Plan B 備案 ＋ 份量預約全攻略)**：**Gemini 3.8 Flash ＋ `Thinking: HIGH`**。精算 2大2小成人份量配餐、手作 DIY 攻略、周遊券邊界精算與適合青少年的文化趣味歷史。
  - **🛡️ 嚴肅模式 (Serious - 軍事級死線防禦 ＋ 危機預警 ＋ 安全第一)**：**Gemini 3.8 Flash ＋ `Thinking: HIGH`**。強制倒推 30~45 分鐘安全撤退線，嚴格防範江之島搭錯單軌電車、月台迷航、人潮走失與急診藥局對策。
  - **💨 精簡模式 (Brief - HUD 抬頭顯示戰報 ＋ 1秒速讀指令)**：`Thinking: MINIMAL`。極簡儀表板輸出（目標、路線/月台、耗時、死線倒數），走路趕路時單手 1 秒掌握指令。
  - **⚡ 簡潔模式 (Concise - 標準敏捷行動派 - 預設)**：`Thinking: MEDIUM`。2~4 點直擊核心，平衡效率與趣味。
- [x] **AI 隨身導遊大腦升級 (v1.4.0 基礎)**：
  - 實時日本時間與進度感知 (JST & Stage Engine)。
  - 即時 GPS 空間感知與 18 大地標反向錨定。
  - 多話題 Session 管理系統 (Multi-Topic Manager)。
  - Funliday 行程動態異動覆蓋 (Dynamic Itinerary Override)。
- [x] **底欄防破圖與 Android Intent 適配 (v1.3.1)**。
- [x] **iOS Standalone PWA 零閃退防護 (v1.2.1)**。
- [x] **零外洩安全架構**：100% 零硬編碼 API Key，密鑰加密存於手機本地。
- [x] **雙軌發布與跨設備同步就緒**：
  - **GitHub Pages**：部署至 `https://ethanexoticdvm-tech.github.io/tokyo-trip-2026/`。
  - **Google Drive Bare Repo**：同步至 `G:\我的雲端硬碟\antigravity_repos\tokyo-trip-assistant.git`。
  - **Google Drive 交付目錄**：`G:\我的雲端硬碟\AI-Programe\新宿6日遊隨身戰情室_v1.4.1\`。

---

## 3. 關鍵架構與設計決策
1. **實質決策分流與 High 深度思考**：
   - 當使用者選擇「詳細」或「嚴肅」時，API 調用 `gemini-3.8-flash` 且代入 `generationConfig: { thinkingConfig: { thinkingLevel: "HIGH" } }`，執行最深層推理運算。
2. **青少年心理與生理適配**：
   - 拒絕把 11/12 歲當幼童，重視食量、自主行動力與專屬青少年的動漫潮玩熱點。

---

## 4. 下一步待辦事項 (Next Steps)
1. **出發前一週 (11月中旬)**：
   - 複核橫濱紅磚倉庫聖誕市集 asoview! 優先入場票開賣與購票狀態。
   - 複核 Day 1 新宿牛舌檸檬 TableCheck 訂位代碼。
2. **家人手機部署實機測試**：
   - 請家人以手機打開網址並實測 5 種模式切換、GPS 定位與 AI 提問。
