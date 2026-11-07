# 📖 新宿・橫濱・箱根 6日遊 AI導遊大腦設計架構與操作SOP

## 1. 模組定位與設計目標
本目錄 (`ai-engine/`) 為「新宿・橫濱・箱根 6日遊隨身戰情室」的專屬 **AI 導遊大腦研發中心**。
旨在達成：
1. **多輪連貫記憶 (Multi-turn Continuity)**：在手機斷網重連或重開時，完美延續上下文，不失憶。
2. **全行程死線預警 (Zero-Miss Deadlines)**：永遠以 15:15 大涌谷下山、12:00 龍宮殿計程車、10:45 泡麵博物館等核心死線為最高決策防線。
3. **親子家庭視角 (Family & Kids Friendly)**：以 2 大 2 小同行情境為基準，所有餐飲、景點與交通皆考量兒童推車、換尿布與避辣需求。
4. **Prompt 調優與前端發布解耦**：在此單獨維護 Markdown 格式的提示詞與測試情境，測試滿意後一鍵同步至手機 Web App。

---

## 2. 目錄檔案清單

| 檔案名稱 | 核心功能說明 |
|:---|:---|
| [`system_instruction.md`](./system_instruction.md) | **AI 核心系統知識庫**（完整 6 天行程、班次座位、死線、飯店座標、交通避坑） |
| [`scenarios.json`](./scenarios.json) | **實戰情境庫**（小孩安撫、避辣菜單、龍宮殿計程車、大涌谷死線、江之電防呆） |
| [`test_chat.py`](./test_chat.py) | **本機調試終端**（直接串接 Gemini 3.8 Flash，支援多輪對話與情境庫自動回歸） |
| [`sync_prompt_to_web.py`](./sync_prompt_to_web.py) | **一鍵同步腳本**（自動將 `system_instruction.md` 注入 `../index.html`） |

---

## 3. 日常調試與同步操作 SOP

### 步驟 1：調整或擴充知識庫
直接編輯 [`system_instruction.md`](./system_instruction.md)，補充最新確認的餐廳、雨天備案或特別叮嚀。

### 步驟 2：本機終端連貫對話測試
在終端機執行：
```bash
python test_chat.py
```
- 輸入問題即可即時測試 Gemini 3.8 Flash 導遊大腦的回應品質、延遲與 Token 消耗。
- 輸入 `clear` 可清空上下文重啟對話；輸入 `exit` 退出。

### 步驟 3：自動跑 5 大實戰情境回歸
```bash
python test_chat.py --test
```
自動送出 5 大刁鑽情境（小孩哭鬧、避辣點餐、死線提醒、防搭錯車），檢驗 AI 是否準確攔截風險。

### 步驟 4：一鍵同步至手機戰情室
確認回答品質優異後，執行：
```bash
python sync_prompt_to_web.py
```
即會自動將最新版 Prompt 替換至前端 `index.html`，隨後推送到 GitHub Pages 與手機端！
