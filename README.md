# 🍁 新宿・橫濱・箱根 6日遊隨身戰情室 (Tokyo Trip Assistant)

> 專為 2026/11/26 ～ 12/01 全家人（2 大 2 小）量身打造的一頁式自適應隨身旅行戰情室 Web App。

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Online-success)](https://ethanexoticdvm-tech.github.io/tokyo-trip-2026/)
[![Version](https://img.shields.io/badge/Version-v1.4.2-rose)](https://github.com/ethanexoticdvm-tech/tokyo-trip-2026)
[![Model](https://img.shields.io/badge/AI%20Brain-Gemini%203.8%20Flash-purple)](https://aistudio.google.com/)

---

## 🌐 線上即時體驗（全家手機共用）
- **📱 手機直達網址**：[https://ethanexoticdvm-tech.github.io/tokyo-trip-2026/](https://ethanexoticdvm-tech.github.io/tokyo-trip-2026/)
- **📲 使用方式**：在 iPhone (Safari) 點擊「分享 ➔ 加入主畫面」，或 Android (Chrome) 點擊「新增至主畫面」，即可獲得原生 App 體驗。

---

## 🔒 零外洩安全性架構 (Zero-Leak Security)
- **倉庫無任何 API Key**：本開源 GitHub 倉庫與所有檔案 **100% 絕不包含任何私鑰或敏感資訊**。
- **純本地 LocalStorage 存儲**：
  - 行程查閱、車票速查、死線告警、寶可夢尋寶、日語手指卡對所有人免費完全開放。
  - 只有在點擊「Gemini大腦」時，各自手機需貼入一次各自的 Google Gemini API Key。
  - 密鑰加密存於個人手機瀏覽器的 `localStorage` 中，絕不傳送到 GitHub 或第三方伺服器。

---

## 🌟 核心戰情模組

### 1. ⚡ 核心死線即時告警
- **Day 5 箱根**：`15:15 大涌谷準時下山（核心死線）`，確保順暢轉乘空中纜車 ➔ 早雲山 ➔ 強羅 ➔ 登山電車，銜接 17:46 箱根湯本回程浪漫特快。
- **Day 4 鎌倉**：`13:23 交通陷阱！認明【江之電】`，切勿搭乘單軌電車繞大遠路。
- **Day 3 橫濱**：`合味道紀念館 10:45 報到`、`紅磚倉庫聖誕市集 16:00 點燈與優先入場攻略`。
- **Day 1 新宿**：`牛たんの檸檬 (20:34) TableCheck 預約`。

### 2. 🎫 離線車票與座位速查
- **Day 4 浪漫特快 江之島33號**：07 號車廂 `2A, 2B, 3A, 3B` (08:20 新宿 ➔ 09:28 片瀨江之島)
- **Day 5 去程 箱根41號 (EXE10)**：04 號車廂 `8C, 8D, 9C, 9D` (07:37 新宿 ➔ 09:22 箱根湯本)
- **Day 5 回程 箱根18號 (MSE6)**：04 號車廂 `8C, 8D, 9C, 9D` (17:46 箱根湯本 ➔ 19:26 新宿)

### 3. 🤖 Gemini 3.8 Flash 隨身導遊大腦
- 對接 Google 最新 `gemini-3.8-flash` 模型。
- 內建行程專屬 System Instruction（熟知 6 天全行程、飯店、死線與座位）。
- 快捷提問晶片：
  - 📋 拍菜單問推薦（兒童友善、避辣）
  - ☕ 小朋友累了找咖啡店休息
  - 🍱 元箱根港午餐推薦（免排隊）
  - ⏰ 箱根回程車次提醒
  - 🗺️ 怎麼走回大久保飯店

### 4. 🎮 橫濱 7 大寶可夢尋寶任務
- 內建櫻木町、市役所、日本丸、臨港公園、海洋塔、紅磚倉庫等 7 處皮卡丘人孔蓋與立體郵筒。
- 一鍵 Google Maps 座標導航 ＋ 打卡進度本機獨立儲存。

### 5. 🌐 Google 翻譯 App 原生秒開
- 頂部導航列支援 iOS URL Scheme (`googletranslate://`) 與 Android Intent，一鍵喚起手機 App。

---

## 🛠️ 開發與同步架構
- **本機工作目錄**：`C:\Users\inche\Antigravity\tokyo-trip-assistant`
- **雲端裸倉庫**：`G:\我的雲端硬碟\antigravity_repos\tokyo-trip-assistant.git`
- **交付打包目錄**：`G:\我的雲端硬碟\AI-Programe\新宿6日遊隨身戰情室_v1.3.1\`
- **GitHub Pages**：`https://github.com/ethanexoticdvm-tech/tokyo-trip-2026`
