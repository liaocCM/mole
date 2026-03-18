# Trendshift 月度報告 — 2026-02-16 至 2026-03-16
**涵蓋範圍：** 4 週（28 天）  |  **不重複專案（2+ 週上榜）：** 66

---

## 1. [agency-agents](https://github.com/msitarzewski/agency-agents)
> 觸手可及的完整 AI 代理團隊——從前端高手到 Reddit 社群達人，從趣味注入者到現實查核員。每個代理都是具備個性、流程和經驗證交付成果的專業專家。

**Language:** Shell  |  **Stars:** 46,473  |  **Forks:** 6,940  |  **Best Score:** 50,168  |  **Best Rank:** #1  |  **Weeks on chart:** 2/4  |  **Days on chart:** 12/28  |  **Created:** 2025-10-13

**背景：** Agency Agents 是由 msitarzewski 建立的精心製作的 AI 代理人格合集，包含工程、行銷、策略等多個部門的專業代理。它誕生於一個 Reddit 討論串，經過數月迭代已累積超過 46,000 顆星。每個代理具備獨立的身份、工作流程和交付能力，可搭配 Claude Code、Cursor、Codex 和 OpenCode 使用。

**解決的問題：** 通用的提示模板缺乏深度領域專業知識和一致的工作流程，導致 AI 代理的輸出品質參差不齊。Agency Agents 透過為每個領域提供具備完整人格、流程和成功指標的專業代理定義，將代理互動從泛用提示升級為結構化的專業協作。

**為何又一個？** 不同於簡單的提示集合，每個代理都包含身份特徵、溝通風格、核心任務和可交付成果。跨平台支援（Claude Code、Cursor、Codex、Aider、Windsurf、Gemini CLI）和自動化轉換腳本使其能輕鬆整合到現有工作流程中。

---

## 2. [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
> 完整收錄主要 AI 編程工具的系統提示詞、內部工具和 AI 模型

**Language:** N/A  |  **Stars:** 131,703  |  **Forks:** 33,396  |  **Best Score:** 24,578  |  **Best Rank:** #1  |  **Weeks on chart:** 3/4  |  **Days on chart:** 8/28  |  **Created:** 2025-03-05

**背景：** 這個由 x1xhlol 建立的資源庫，彙整了超過 30,000 行的系統提示詞、內部工具配置和模型細節，這些資料擷取自超過 30 個主要的 AI 編碼助手和消費級 AI 產品。自 2025 年 3 月創建以來已累積超過 131,000 顆星。涵蓋範圍從 Claude Code 和 Cursor 到 Manus 和 v0。

**解決的問題：** 系統提示詞和內部工具定義通常對使用者隱藏，使人難以了解 AI 產品實際如何運作、什麼指令引導其行為，以及它們公開了哪些能力。這個資源庫將這些難以取得的素材整合到一個可瀏覽的單一位置，同時服務想學習提示工程模式的開發者和關注 AI 系統透明度的安全研究人員。

**為何又一個？** 它涵蓋的工具數量超過任何競爭資源（截至本月計算超過 28 個），並隨工具變更持續更新。其 131,000 顆星數反映了開發者對 AI 工具透明度的廣泛興趣。

---

## 3. [RuView](https://github.com/ruvnet/RuView)
> RuView：WiFi DensePose 將一般 WiFi 訊號轉化為即時人體姿態估計、生命體徵監測和存在偵測——完全不需要任何影片像素。

**Language:** Rust  |  **Stars:** 37,719  |  **Forks:** 5,181  |  **Best Score:** 24,100  |  **Best Rank:** #1  |  **Weeks on chart:** 2/4  |  **Days on chart:** 4/28  |  **Created:** 2025-06-07

**背景：** RuView 是 ruvnet 開發的邊緣 AI 感知系統，能直接從環境中的 WiFi 和無線電訊號學習，無需攝影機、穿戴裝置或網際網路。建構在 RuVector 之上，它以 WiFi DensePose 實作聞名——透過分析通道狀態資訊（CSI）干擾重建人體姿態、呼吸率、心率和存在偵測。已累積超過 37,000 顆星。

**解決的問題：** 傳統人體感知系統依賴攝影機（引發隱私疑慮）或穿戴裝置（需要使用者配合）。RuView 利用空間中已存在的無線訊號，使用低成本的 ESP32 感測器網格（每個節點低至約 1 美元），在邊緣端完全自學環境的射頻特徵。

**為何又一個？** 與依賴同步攝影機訓練資料的學術原型不同，RuView 設計為完全從射頻訊號和邊緣端自學嵌入向量運作。其 Rust 實作（1,300+ 測試）達到 54K fps 的姿態估計處理速度，支援穿牆偵測達 5 公尺深度。

---

## 4. [wifi-densepose](https://github.com/ruvnet/wifi-densepose)
> WiFi DensePose 將一般 WiFi 訊號轉化為即時人體姿態估計、生命體徵監測和存在偵測

**Language:** Rust  |  **Stars:** 15,004  |  **Forks:** 1,567  |  **Best Score:** 20,932  |  **Best Rank:** #1  |  **Weeks on chart:** 3/4  |  **Days on chart:** 5/28  |  **Created:** 2025-06-07

**背景：** WiFi DensePose（又名 RuView）是 ruvnet 開發的邊緣 AI 系統，能將標準 WiFi 訊號轉化為人體姿態估計、生命體徵監測和存在偵測——完全不需要攝影機或穿戴裝置。該專案透過分析人體移動引起的通道狀態資訊（CSI）干擾，使用價格低廉的 ESP32 感測器（每個約 9 美元）。已累積超過 15,000 顆星。

**解決的問題：** 監測人體存在和健康狀況通常需要攝影機（引發隱私疑慮）或穿戴裝置（需要使用者配合）。WiFi DensePose 利用現有的 WiFi 基礎設施穿牆運作，不需要網路連線，並從原始訊號資料中學習而無需標註訓練集——使其可在醫療、零售和安全場景中部署，而不需做隱私取捨。

**為何又一個？** 不同於依賴同步攝影機訓練資料的學術 WiFi 感測原型，WiFi DensePose 設計為完全從射頻訊號和邊緣端自學嵌入向量運作。其 Rust 實作提供了在資源受限硬體上進行即時姿態估計所需的低延遲。

---

## 5. [MiroFish](https://github.com/666ghj/MiroFish)
> 簡潔通用的群體智能引擎，預測萬物。

**Language:** Python  |  **Stars:** 32,521  |  **Forks:** 4,096  |  **Best Score:** 15,686  |  **Best Rank:** #3  |  **Weeks on chart:** 2/4  |  **Days on chart:** 9/28  |  **Created:** 2025-11-26

**背景：** MiroFish 是一款基於多智能體技術的新一代 AI 預測引擎，由盛大支持。透過提取現實世界的種子資訊（突發新聞、政策草案、金融訊號），自動構建高保真的平行數位世界。在此空間內，成千上萬個具備獨立人格、長期記憶與行為邏輯的智能體進行自由交互與社會演化。已累積超過 32,000 顆星。

**解決的問題：** 傳統預測方法依賴統計模型或專家判斷，難以捕捉複雜社會系統中個體互動引發的群體湧現效應。MiroFish 透過建構數位沙盤，讓政策、輿情和市場走向在零風險環境中進行推演預測。

**為何又一個？** MiroFish 同時服務嚴肅預測和趣味仿真——從武漢大學輿情推演到《紅樓夢》失傳結局預測。雙平台並行模擬、GraphRAG 知識圖譜構建和 ReportAgent 深度互動的技術架構，使其在預測引擎中獨樹一幟。

---

## 6. [paperclip](https://github.com/paperclipai/paperclip)
> 零人力公司的開源協調平台

**Language:** TypeScript  |  **Stars:** 26,233  |  **Forks:** 3,483  |  **Best Score:** 14,426  |  **Best Rank:** #1  |  **Weeks on chart:** 2/4  |  **Days on chart:** 6/28  |  **Created:** 2026-03-02

**背景：** Paperclip 是一個 Node.js 伺服器和 React UI，用於協調 AI 代理團隊運營一家企業。如果說 OpenClaw 是一個「員工」，Paperclip 就是「公司」——它提供組織架構、預算管控、目標對齊和代理協調功能。支援 OpenClaw、Claude Code、Codex、Cursor 等多種代理。自 2026 年 3 月發布以來已超過 26,000 顆星。

**解決的問題：** 同時運行 20 個 Claude Code 終端的開發者很容易失去對每個代理工作進度的追蹤。Paperclip 提供統一的儀表板管理業務目標而非 Pull Request，具備成本監控、預算執行和工作審計功能。

**為何又一個？** Paperclip 定位為代理的「任務管理器」而非又一個代理框架——它不替代代理，而是協調它們朝共同業務目標工作。即將推出的 Clipmart 功能允許一鍵下載和運行完整的公司模板，包括組織結構、代理配置和技能。

---

## 7. [awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
> 社群收集的 OpenClaw 使用案例，讓生活更輕鬆。

**Language:** N/A  |  **Stars:** 25,079  |  **Forks:** 2,066  |  **Best Score:** 13,160  |  **Best Rank:** #1  |  **Weeks on chart:** 4/4  |  **Days on chart:** 18/28  |  **Created:** 2026-02-08

**背景：** 由 Hesam Sheikh 維護，這個社群精選的資源庫收錄了 OpenClaw 開源個人 AI 助手平台的真實應用案例。它於 2026 年 2 月初發布，已達到超過 25,000 顆星。該合集在七個類別中整理了 40 個以上的已驗證使用案例，包括社群媒體自動化、創意工作流程、基礎設施管理和金融。

**解決的問題：** OpenClaw 的文件說明了平台能做什麼，但並未涵蓋人們在日常生活中實際如何使用它。這個資源庫透過要求貢獻者僅提交經個人驗證為可用的使用案例，提供了經過實戰驗證的實作方案，而非推測性的可能性，藉此彌補了這一落差。

**為何又一個？** 嚴格的驗證要求——貢獻者必須親自測試並驗證每個使用案例至少一天——使其有別於接受未經測試條目的一般精選列表。不同於列出 OpenClaw 技術上能做什麼的技能目錄，此資源庫專注於真實使用者為何及如何在日常生活中使用它。

---

## 8. [superpowers](https://github.com/obra/superpowers)
> 一個有效的代理技能框架與軟體開發方法論。

**Language:** Shell  |  **Stars:** 92,068  |  **Forks:** 7,288  |  **Best Score:** 12,796  |  **Best Rank:** #1  |  **Weeks on chart:** 4/4  |  **Days on chart:** 28/28  |  **Created:** 2025-10-09

**背景：** Superpowers 是一個完整的編程代理軟體開發工作流程，強制執行紀律性流程：規格擷取、設計審查、實作計畫，以及透過子代理驅動的開發與 TDD。由 obra 創建，已達到超過 92,000 顆星。該框架提供 13 個以上可組合的技能——包括腦力激盪、撰寫計畫、測試驅動開發和子代理驅動開發——可搭配 Claude Code、Cursor、Codex 和 OpenCode 使用。

**解決的問題：** 放任自行運作的編程代理往往會直接跳入寫程式碼，缺乏充分的規劃、規格制定或測試，導致產出品質低落，需要大量人工修正。Superpowers 強制施加結構化工作流程，讓代理在觸碰生產程式碼之前，自動進行規格精煉、詳細規劃和真正的紅-綠 TDD。

**為何又一個？** Superpowers 作為一個元框架運作，位於代理之上而非內部。它不取代代理的能力，而是增加流程防護機制（YAGNI、DRY、TDD），防止無人監督代理會話中常見的偏移和退化。其可攜性——同一套技能可安裝在 Claude Code、Cursor、Codex 和 OpenCode 中——是其主要差異化因素。

---

## 9. [cs-video-courses](https://github.com/Developer-Y/cs-video-courses)
> 附有影片講座的電腦科學課程清單。

**Language:** N/A  |  **Stars:** 77,211  |  **Forks:** 10,470  |  **Best Score:** 11,544  |  **Best Rank:** #1  |  **Weeks on chart:** 2/4  |  **Days on chart:** 4/28  |  **Created:** 2016-10-21

**背景：** cs-video-courses 是一個由社群維護的免費電腦科學課程精選清單，按主題領域分類——演算法、作業系統、機器學習、分散式系統等。由 Developer-Y 於 2016 年 10 月創建，已成長為 GitHub 上最大的自學式電腦科學教育單檔參考資源之一，超過 77,000 顆星。

**解決的問題：** 高品質的電腦科學講座內容散布在數十個大學網站、YouTube 頻道和 MOOC 平台上，標籤和可發現性不一致。這個資源庫將它們整合到一個按主題組織的可瀏覽索引中，為學習者節省了尋找免費資源的時間。

**為何又一個？** cs-video-courses 反覆上榜，因為它是同類中最全面的單一資源庫索引，並且隨著新課程出現持續透過社群 Pull Request 更新。其持久性源於它涵蓋了完整的電腦科學課程體系。

---

## 10. [openclaw](https://github.com/openclaw/openclaw)
> 你的個人 AI 助手。任何作業系統。任何平台。龍蝦之道。

**Language:** TypeScript  |  **Stars:** 314,992  |  **Forks:** 60,226  |  **Best Score:** 10,446  |  **Best Rank:** #2  |  **Weeks on chart:** 4/4  |  **Days on chart:** 24/28  |  **Created:** 2025-11-24

**背景：** OpenClaw 是主導地位的開源個人 AI 助手平台，擁有超過 314,000 顆星，使其成為 GitHub 上星數最高的儲存庫之一。它可在幾乎所有平台上運行，並整合 WhatsApp、Telegram、Slack、Discord、Google Chat、Signal、iMessage、IRC、Microsoft Teams、Matrix 等眾多即時通訊服務。

**解決的問題：** 專有 AI 助手被鎖定在特定平台、應用商店或訂閱服務中，限制了使用者對資料和模型選擇的控制權。OpenClaw 透過本機 Gateway 控制平面在使用者自己的裝置上運行，提供語音功能、瀏覽器自動化和裝置級整合，同時將資料保持在使用者控制之下。

**為何又一個？** OpenClaw 的主導地位來自其廣泛的平台支援和蓬勃的技能與插件生態系統。本月圍繞它的生態系統活動——awesome-openclaw-usecases、awesome-openclaw-skills、openclaw-studio 和 nanoclaw 同時上榜——表明該平台已達到社群工具超越核心專案自身可見度的成熟轉折點。

---

## 11. [AstrBot](https://github.com/AstrBotDevs/AstrBot)
> 整合眾多即時通訊平台、LLM、插件和 AI 功能的代理式 IM 聊天機器人基礎設施，可作為你的 OpenClaw 替代方案。

**Language:** Python  |  **Stars:** 25,271  |  **Forks:** 1,723  |  **Best Score:** 9,889  |  **Best Rank:** #6  |  **Weeks on chart:** 2/4  |  **Days on chart:** 3/28  |  **Created:** 2022-12-08

**背景：** AstrBot 是開源的全方位 Agent 聊天機器人平台，整合主流即時通訊應用程式，為個人、開發者和團隊提供可靠且可擴展的對話 AI 基礎設施。自 2022 年 12 月創建以來已累積超過 25,000 顆星，支援 QQ、微信、Telegram、Discord 等多個平台，並擁有豐富的插件市場。

**解決的問題：** 搭建一個跨多個即時通訊平台的 AI 聊天機器人需要為每個平台編寫獨立的整合程式碼，且缺乏統一的管理介面。AstrBot 提供統一的平台抽象層和可視化管理面板，使開發者能專注於業務邏輯而非平台適配。

**為何又一個？** AstrBot 以一流的 QQ 和微信支援深耕中國即時通訊生態系統，同時兼顧國際平台。其插件市場機制和 Trendshift 排行榜上的持續亮相，反映了中文社群對開源 AI 聊天機器人基礎設施的強烈需求。

---

## 12. [Scrapling](https://github.com/D4Vinci/Scrapling)
> 一個能處理從單一請求到全規模爬取的自適應網頁擷取框架！

**Language:** Python  |  **Stars:** 30,660  |  **Forks:** 2,389  |  **Best Score:** 9,748  |  **Best Rank:** #1  |  **Weeks on chart:** 2/4  |  **Days on chart:** 7/28  |  **Created:** 2024-10-13

**背景：** Scrapling 是由 D4Vinci 開發的自適應網頁擷取框架，將快速 HTTP 請求、隱匿式瀏覽器自動化和並行 Spider 爬蟲整合在單一函式庫中。已成長至超過 30,000 顆星。該專案包含 92% 的測試覆蓋率、完整的型別提示，以及用於 AI 輔助資料擷取的內建 MCP 伺服器。

**解決的問題：** 傳統的擷取程式碼在網站變更其 HTML 結構時就會失效，迫使開發者陷入不斷維護的循環。Scrapling 使用智慧相似度演算法，即使在頁面重新設計後也能自動重新定位元素，同時處理 Cloudflare Turnstile 等反機器人系統。

**為何又一個？** 大多數擷取函式庫只專注於 HTTP 請求或瀏覽器自動化，迫使開發者拼湊多種工具。Scrapling 將兩種方法加上具備暫停/恢復功能的完整爬取框架統一在一起，其 MCP 伺服器整合使其能被 AI 代理原生存取——這是沒有任何單一競爭者提供的組合。

---

## 13. [openfang](https://github.com/RightNow-AI/openfang)
> 開源代理作業系統

**Language:** Rust  |  **Stars:** 14,660  |  **Forks:** 1,732  |  **Best Score:** 9,736  |  **Best Rank:** #2  |  **Weeks on chart:** 2/4  |  **Days on chart:** 3/28  |  **Created:** 2026-02-24

**背景：** OpenFang 是 RightNow AI 以 Rust 建構的「代理作業系統」，包含 137,000 行程式碼，分佈在 14 個 crate 中，擁有超過 1,767 個測試且零 clippy 警告。編譯為單一 32MB 二進位檔，搭載 7 個預建的「Hands」（自主能力套件）、40 個訊息通道轉接器，並支援 27 家 LLM 供應商。

**解決的問題：** 大多數代理框架產出的聊天機器人會等待使用者輸入，而非能獨立運作的自主系統。OpenFang 使代理能按排程全天候運行，執行研究、潛在客戶開發和網頁自動化等任務，無需持續的人工指示，且具備 180 毫秒冷啟動和 40MB 閒置記憶體佔用。

**為何又一個？** OpenFang 的工程嚴謹度（1,767 多個測試、零警告、14 crate 架構）使其有別於原型品質的代理框架。透過 16 個獨立安全層（包括 WASM 沙箱和 Merkle 雜湊鏈審計）來差異化——這種等級的安全基礎設施在開源代理平台中並不常見。

---

## 14. [CoPaw](https://github.com/agentscope-ai/CoPaw)
> 你的個人 AI 助手；易於安裝，可部署在自己的機器上或雲端

**Language:** Python  |  **Stars:** 12,248  |  **Forks:** 1,484  |  **Best Score:** 9,658  |  **Best Rank:** #3  |  **Weeks on chart:** 2/4  |  **Days on chart:** 4/28  |  **Created:** 2026-02-24

**背景：** CoPaw 是 AgentScope 團隊（阿里巴巴）推出的個人 AI 助手，可在本機或雲端部署，不受供應商鎖定。它整合了釘釘、飛書、QQ、Discord、iMessage 和其他通訊平台，並透過 llama.cpp、MLX 和 Ollama 支援雲端 LLM 及完全離線的本機模型。已超過 12,000 顆星。

**解決的問題：** AI 互動分散在多個平台上，每個平台都需要獨立的帳號和配置。CoPaw 透過一個自託管的單一助手統一存取所有主要通訊應用程式，具備可自訂的記憶系統和可從工作區檔案自動載入的可擴展技能架構。

**為何又一個？** CoPaw 以一流的釘釘、飛書和 QQ 支援瞄準中國開發者生態系統，同時兼顧西方平台——這是 OpenClaw 和 Nanoclaw 大量未服務的市場區塊。其 Python 原生方法和 AgentScope 團隊的支持帶來企業 AI 經驗。

---

## 15. [worldmonitor](https://github.com/koala73/worldmonitor)
> 即時全球情報儀表板——AI 驅動的新聞聚合、地緣政治監控和基礎設施追蹤

**Language:** TypeScript  |  **Stars:** 38,633  |  **Forks:** 6,411  |  **Best Score:** 9,274  |  **Best Rank:** #1  |  **Weeks on chart:** 3/4  |  **Days on chart:** 9/28  |  **Created:** 2026-01-08

**背景：** World Monitor 是由 koala73 開發的開源即時情報儀表板，將新聞、地緣政治資料和基礎設施狀態聚合到統一介面中。於 2026 年 1 月推出，已成長至近 39,000 顆星，並提供五種變體：World、Tech、Finance、Commodity 和 Happy Monitor。具備雙 3D/2D 地圖、435 個以上的 RSS 訂閱源、即時影片串流，以及透過 Ollama 的本機 LLM 支援。

**解決的問題：** 專業的 OSINT 和態勢感知工具通常昂貴、專有且依賴雲端。World Monitor 以免費、自託管的應用程式提供同等功能——多源聚合、地緣政治事件追蹤、基礎設施監控——在本機運行 AI 並支援 21 種語言。

**為何又一個？** 完全本機的 AI 處理、程式化 API 存取和跨平台部署（Windows、Mac、Linux、網頁）的免費組合，消除了讓大多數情報儀表板超出獨立研究人員和小型組織觸及範圍的成本與隱私障礙。透過多變體方式（針對通用、科技和金融受眾的獨立儀表板）和 AGPL 授權確保衍生作品保持開源。

---

## 16. [airi](https://github.com/moeru-ai/airi)
> 自託管、你擁有的 Grok 夥伴，一個承載 waifu 靈魂的容器，將數位生命帶入我們的世界。支援即時語音聊天、Minecraft、Factorio 遊戲。

**Language:** TypeScript  |  **Stars:** 34,244  |  **Forks:** 3,404  |  **Best Score:** 9,216  |  **Best Rank:** #2  |  **Weeks on chart:** 2/4  |  **Days on chart:** 7/28  |  **Created:** 2024-12-01

**背景：** Project AIRI 由 moeru-ai 開發，是一個自託管的 AI 夥伴平台，旨在重現 Neuro-sama 的體驗——一個能夠即時語音對話、玩遊戲（Minecraft、Factorio）並維持一致個性的 AI 虛擬角色。支援網頁、macOS 和 Windows，具備七種語言翻譯。自 2024 年 12 月以來已累積超過 34,000 顆星。

**解決的問題：** 建構一個能夠即時語音對話、玩遊戲並在各會話間維持一致個性的互動 AI 夥伴，需要整合語音合成、遊戲 API、記憶系統和角色建模。AIRI 將所有這些打包在單一自託管應用程式中。

**為何又一個？** AIRI 是少數嘗試在使用者自有硬體上匹配商業 AI 夥伴平台能力的開源專案之一。其遊戲遊玩能力（Minecraft、Factorio）遠超簡單的聊天機器人互動，其混合架構——同時具備網頁可存取性和原生效能——使其有別於通常僅針對單一部署模式的其他虛擬角色專案。

---

## 17. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> 練習造就完美的 Claude

**Language:** HTML  |  **Stars:** 17,254  |  **Forks:** 1,525  |  **Best Score:** 8,554  |  **Best Rank:** #3  |  **Weeks on chart:** 3/4  |  **Days on chart:** 10/28  |  **Created:** 2025-10-31

**背景：** 這個由 shanraisshan 建立的資源庫記錄了 Claude Code 的最佳實踐、工作流程和實作模式，包括來自 Claude Code 團隊本身的技巧。涵蓋命令、子代理、技能、記憶管理和協調工作流程。擁有超過 17,000 顆星，它已成為 Claude Code 使用者的主要參考指南。

**解決的問題：** Claude Code 的官方文件說明了功能，但並未涵蓋大量日常使用中浮現的實用模式和工作流程。這個資源庫以社群來源的技巧、進階工作流程範例和 Command-Agent-Skill 協調等架構模式填補了這一空缺。

**為何又一個？** 包含來自 Claude Code 創建者（Boris Cherny 及團隊）的直接技巧賦予其半官方的權威性。其對實用模式而非功能文件的專注使其與 Anthropic 自身的資源形成互補。

---

## 18. [public-apis](https://github.com/public-apis/public-apis)
> 免費 API 的集合清單

**Language:** Python  |  **Stars:** 411,142  |  **Forks:** 44,435  |  **Best Score:** 8,127  |  **Best Rank:** #7  |  **Weeks on chart:** 2/4  |  **Days on chart:** 5/28  |  **Created:** 2016-03-20

**背景：** public-apis 是由社群手動策劃的免費公開 API 集合，涵蓋多個領域，由 APILayer 贊助維護。擁有超過 411,000 顆星，它是 GitHub 上星數最高的資源庫之一，為開發者提供了一個按類別組織的 API 寶庫。

**解決的問題：** 尋找適合專案使用的免費 API 需要在數十個不同來源中搜尋，且品質和文件完整度參差不齊。這個資源庫將經社群審核的 API 整合到單一、分類清晰的索引中。

**為何又一個？** 作為同類中歷史最悠久且最全面的集合，public-apis 定期重新登上趨勢榜，因為新一代開發者不斷發現它。其 Discord 社群和持續的社群維護確保了內容的時效性。

---

## 19. [vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands)
> 基於 easemate IDE 和 JetBrains Islands 主題的 VSCode 主題

**Language:** PowerShell  |  **Stars:** 5,206  |  **Forks:** 156  |  **Best Score:** 8,115  |  **Best Rank:** #1  |  **Weeks on chart:** 2/4  |  **Days on chart:** 4/28  |  **Created:** 2026-02-14

**背景：** Islands Dark 是一個受 easemate IDE 啟發的 VS Code 色彩主題，具備懸浮玻璃面板、圓角、平滑動畫和深色畫布（#131217）。由 bwya77 於 2026 年 2 月中創建，已累積超過 5,200 顆星，顯示對這種視覺美學的強烈需求。

**解決的問題：** 許多在 JetBrains IDE 和 VS Code 之間切換的開發者，會懷念新編輯器中熟悉的 Islands 色彩配置。這個主題在不需要更換整個 IDE 的情況下彌合了這一美學差距，透過精心處理玻璃效果邊框、藥丸形捲軸和懸停感知的 UI 元素。

**為何又一個？** easemate 啟發的設計語言——懸浮面板、方向性光線模擬、動畫過渡——遠超典型的換色主題。其快速的採用速度表明該主題滿足了較簡單暗色主題未能滿足的真正美學偏好。

---

## 20. [OpenViking](https://github.com/volcengine/OpenViking)
> OpenViking 是專為 AI 代理設計的開源上下文資料庫，透過檔案系統範式統一管理代理所需的上下文。

**Language:** Python  |  **Stars:** 12,376  |  **Forks:** 847  |  **Best Score:** 7,965  |  **Best Rank:** #4  |  **Weeks on chart:** 2/4  |  **Days on chart:** 6/28  |  **Created:** 2026-01-05

**背景：** OpenViking 是由字節跳動火山引擎開發的開源上下文資料庫，專為 AI 代理設計。它創新性地採用「檔案系統範式」統一組織代理所需的記憶、資源和技能，提供 L0/L1/L2 三層結構按需載入，大幅節省 Token 消耗。已累積超過 12,000 顆星。

**解決的問題：** 在建構 AI 代理時，記憶存在程式碼中、資源在向量資料庫中、技能散落各處，難以統一管理。傳統 RAG 使用扁平儲存，缺乏全域視角，且隱式檢索鏈如黑盒般難以除錯。OpenViking 透過目錄遞迴檢索和視覺化檢索軌跡解決了這些問題。

**為何又一個？** OpenViking 將記憶、資源和技能的管理統一為檔案系統操作，開發者可以像管理本機檔案一樣建構代理的大腦。自動會話管理和長期記憶提取使代理越用越聰明，這在開源上下文管理工具中是獨特的方法。

---

## 21. [generative-ai](https://github.com/GoogleCloudPlatform/generative-ai)
> 在 Google Cloud 上使用 Gemini 和 Vertex AI 的生成式 AI 範例程式碼和筆記本

**Language:** Jupyter Notebook  |  **Stars:** 16,260  |  **Forks:** 4,058  |  **Best Score:** 7,492  |  **Best Rank:** #4  |  **Weeks on chart:** 2/4  |  **Days on chart:** 2/28  |  **Created:** 2023-05-05

**背景：** 這是 Google Cloud 的官方生成式 AI 範例資源庫，包含使用 Vertex AI 上的 Gemini 模型的筆記本、程式碼範例和示範應用程式。自 2023 年 5 月創建以來已超過 16,000 顆星，涵蓋 Gemini、搜尋、RAG、圖像生成和語音等多個領域。

**解決的問題：** 在 Google Cloud 上開始使用生成式 AI 需要理解 Vertex AI 的 API、模型能力和最佳實踐，但官方文件往往缺乏可直接運行的完整範例。這個資源庫提供了涵蓋各種使用場景的實戰範例。

**為何又一個？** 作為 Google Cloud 的官方範例庫，它隨 Gemini 3.1 Pro 等新模型的發布即時更新。其 Colab 筆記本格式使開發者能零配置即刻上手實驗。

---

## 22. [visual-explainer](https://github.com/nicobailon/visual-explainer)
> 代理技能，可生成豐富的 HTML 頁面或投影片，用於圖表、差異審查、計畫審核、資料表格和專案回顧

**Language:** HTML  |  **Stars:** 6,633  |  **Forks:** 457  |  **Best Score:** 7,314  |  **Best Rank:** #3  |  **Weeks on chart:** 2/4  |  **Days on chart:** 3/28  |  **Created:** 2026-02-16

**背景：** visual-explainer 是一個代理技能，能將終端機輸出轉換為精美的互動式 HTML 頁面。它不再使用 ASCII 圖表和等寬表格，而是生成具有真正排版、明暗主題和可互動 Mermaid 圖表（含縮放和平移功能）的自包含 HTML。它可作為 Claude Code 和其他代理平台的插件安裝。已超過 6,600 顆星。

**解決的問題：** 編程代理預設使用 ASCII 繪製圖表和管線分隔表格呈現資料，兩者在超過簡單複雜度後都變得難以閱讀。visual-explainer 攔截這些輸出並將其渲染為帶有 Mermaid 圖表、精美表格和響應式佈局的正式 HTML，在瀏覽器中開啟。

**為何又一個？** 自動格式路由——根據內容類型選擇正確的視覺化技術而無需開發者介入——使其有別於通用 HTML 生成工具。除了瀏覽器之外不需要任何建構步驟或外部依賴。

---

## 23. [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted)
> 可在自己伺服器上託管的自由軟體網路服務和網頁應用程式清單

**Language:** N/A  |  **Stars:** 280,458  |  **Forks:** 12,875  |  **Best Score:** 7,228  |  **Best Rank:** #6  |  **Weeks on chart:** 2/4  |  **Days on chart:** 3/28  |  **Created:** 2015-06-01

**背景：** awesome-selfhosted 是經典的自由開源自託管軟體精選清單，涵蓋從分析到 Wiki 等類別。自 2015 年開始，透過持續的社群策劃 Pull Request 已成長至超過 280,000 顆星。當自託管興趣高漲時，它會定期重新出現在趨勢排行榜上。

**解決的問題：** 尋找高品質的 SaaS 產品自託管替代方案需要搜尋數十個來源。此資源庫將它們整合到一個單一的、分類的、由社群審核的清單中，具有一致的元資料。

**為何又一個？** 它是同類資源中最原始且最全面的。其定期上榜與更廣泛的資料主權和隱私意識趨勢相關，而 AI 助手浪潮更加速了這一趨勢。

---

## 24. [nanoclaw](https://github.com/qwibitai/nanoclaw)
> OpenClaw 的輕量替代方案，在容器中運行以確保安全性。連接 WhatsApp、Telegram、Slack、Discord、Gmail 和其他通訊應用程式

**Language:** TypeScript  |  **Stars:** 23,285  |  **Forks:** 5,916  |  **Best Score:** 7,223  |  **Best Rank:** #1  |  **Weeks on chart:** 2/4  |  **Days on chart:** 3/28  |  **Created:** 2026-01-31

**背景：** Nanoclaw 是由 qwibitai 建構在 Anthropic Agents SDK 上的容器化個人 AI 助手，定位為 OpenClaw 的輕量替代方案。OpenClaw 擁有近 50 萬行程式碼、53 個配置檔和 70 個以上的依賴項，而 Nanoclaw 目標是提供一個可理解的程式碼庫，具備真正的作業系統級容器隔離。自 1 月底發布以來已超過 23,000 顆星。

**解決的問題：** OpenClaw 功能強大但部署和理解都很複雜。Nanoclaw 將概念精簡為一個容器化執行環境，具備大多數使用者需要的核心功能——跨 WhatsApp、Telegram、Discord、Slack 和 Gmail 的訊息整合、持久記憶和任務排程——而沒有配置的膨脹。

**為何又一個？** Nanoclaw 採用基於技能的貢獻模式，貢獻者建立可重用的 Claude Code 技能（如 `/add-telegram`），使用者選擇性地合併到個人分支中，而非透過傳統的 Pull Request 累積功能。直接整合 Anthropic 的 Agents SDK 意味著它能受益於 SDK 的上游改進而無需重新實作。

---

## 25. [OpenSandbox](https://github.com/alibaba/OpenSandbox)
> OpenSandbox 是一個通用的 AI 應用程式沙箱平台

**Language:** Python  |  **Stars:** 7,879  |  **Forks:** 586  |  **Best Score:** 7,188  |  **Best Rank:** #2  |  **Weeks on chart:** 2/4  |  **Days on chart:** 4/28  |  **Created:** 2025-12-17

**背景：** OpenSandbox 是阿里巴巴的開源沙箱平台，為 AI 應用程式提供隔離的執行環境。它提供多語言 SDK（Python、Java、JavaScript、C#）、統一的沙箱管理 API，以及 Docker 和 Kubernetes 雙運行時支援。該平台整合了 gVisor 和 Kata Containers 等安全容器技術，提供強隔離。已超過 7,800 顆星。

**解決的問題：** 執行程式碼的 AI 代理需要隔離環境以防止對主機系統產生意外副作用，但從零開始建構沙箱基礎設施既複雜又容易出錯。OpenSandbox 開箱即提供標準化、生產等級的隔離，含生命週期管理、分散式排程和網路控制。

**為何又一個？** 大多數沙箱解決方案針對單一執行環境或語言。OpenSandbox 的多語言 SDK 支援和 Docker/Kubernetes 雙運行時相容性使其不受基礎設施限制，而 gVisor 和 Kata 的整合提供了比典型容器替代方案更強的隔離保證。

---

## 26. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> OpenClaw 技能的精選合集。從官方 OpenClaw 技能註冊表中篩選和分類的 5,400 個以上技能。

**Language:** N/A  |  **Stars:** 37,866  |  **Forks:** 3,638  |  **Best Score:** 7,159  |  **Best Rank:** #3  |  **Weeks on chart:** 4/4  |  **Days on chart:** 24/28  |  **Created:** 2026-01-25

**背景：** 由 VoltAgent 維護，這個資源庫從官方 ClawHub 註冊表中精選了 5,494 個 OpenClaw 技能，從更廣泛的 13,729 個技能目錄中過濾掉垃圾、重複、惡意程式碼和非英文條目。已累積超過 37,000 顆星。技能涵蓋 30 個以上類別，包括編碼代理、瀏覽器自動化、DevOps 和圖像生成。

**解決的問題：** OpenClaw 的官方技能註冊表龐大且未經組織，使開發者難以在數千個選項中找到高品質、經審核的技能。這個專案透過嚴格的品質過濾和分類組織使發現變得切實可行。

**為何又一個？** 積極的過濾（從原始註冊表中移除超過 8,000 個條目）與分類組織的結合，填補了官方註冊表未解決的策展空缺。它作為 OpenClaw 技能生態系統的事實上目錄，持續更新以追蹤登錄檔的快速成長。

---

## 27. [pentagi](https://github.com/vxcontrol/pentagi)
> 能夠執行複雜滲透測試任務的完全自主 AI 代理系統

**Language:** Go  |  **Stars:** 9,952  |  **Forks:** 1,192  |  **Best Score:** 7,012  |  **Best Rank:** #1  |  **Weeks on chart:** 2/4  |  **Days on chart:** 6/28  |  **Created:** 2025-01-06

**背景：** PentAGI 是由 vxcontrol 以 Go 建構的自託管自主滲透測試系統，採用多代理架構。它在隔離的 Docker 容器中捆綁了超過 20 種專業安全工具——包括 nmap、Metasploit 和 sqlmap——並使用 Neo4j 支撐的知識圖譜在測試會話間維持長期記憶。

**解決的問題：** 安全測試需要依序調度數十種工具、解讀中間輸出，並根據發現調整攻擊路徑——這一過程需要深厚的專業知識和大量時間。PentAGI 自動化了這一調度層，使系統能夠自主串接工具並產出帶有利用指引的詳細漏洞報告。

**為何又一個？** Neo4j 支撐的知識圖譜使 PentAGI 能從過去的操作中學習，並將上下文知識應用到新的評估中。其完全自託管、開源的性質，加上完整的 REST 和 GraphQL API、Grafana/Prometheus 監控整合，使其有別於商業 AI 輔助安全平台。

---

## 28. [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)
> Bash 就是你所需要的一切——一個從零到一打造的迷你 Claude Code 式代理

**Language:** TypeScript  |  **Stars:** 27,884  |  **Forks:** 4,878  |  **Best Score:** 6,256  |  **Best Rank:** #3  |  **Weeks on chart:** 3/4  |  **Days on chart:** 7/28  |  **Created:** 2025-06-29

**背景：** Learn Claude Code 是 shareAI-lab 推出的教育資源庫，透過 12 個漸進式課程解構 AI 代理架構，教導開發者從零開始建構類似 Claude Code 的代理。該專案包含 Python 參考實作、多語言文件（英文、中文、日文），以及互動式 Next.js 網頁平台。已成長至超過 27,000 顆星。

**解決的問題：** 要理解代理式 AI 系統的內部運作是困難的，當唯一的參考是大型、複雜的生產程式碼庫時。這個專案將概念分解為可消化的單元，展示「一個迴圈加 Bash 就是你所需要的一切」即可建構一個功能性代理，從基本工具使用逐步推進到多代理協調。

**為何又一個？** 不同於教導 API 使用的框架文件，這個專案教導心智模型——使用 ASCII 圖表和最少量的程式碼來傳達代理實際如何運作，然後再疊加複雜性。三語文件使其在英文、中文和日文開發者社群中都能存取。

---

## 29. [page-agent](https://github.com/alibaba/page-agent)
> JavaScript 頁內 GUI 代理。用自然語言控制網頁介面。

**Language:** TypeScript  |  **Stars:** 8,803  |  **Forks:** 694  |  **Best Score:** 6,118  |  **Best Rank:** #7  |  **Weeks on chart:** 2/4  |  **Days on chart:** 6/28  |  **Created:** 2025-09-23

**背景：** Page Agent 由阿里巴巴開發，是一個直接在網頁中運行的 GUI 代理——無需瀏覽器擴展、Python 或無頭瀏覽器。它使用基於文字的 DOM 操作而非截圖，不需要多模態 LLM 或特殊權限。已累積超過 8,800 顆星，並可透過可選的 Chrome 擴展支援跨頁面任務。

**解決的問題：** 將 AI 助手整合到現有網頁應用程式通常需要後端重寫或複雜的瀏覽器自動化設定。Page Agent 透過幾行 JavaScript 即可在任何網頁中嵌入 AI 操作能力，將 20 次點擊的工作流程簡化為一句自然語言指令。

**為何又一個？** 純頁內 JavaScript 方法使其成為最輕量的網頁 AI 代理整合方案。支援自帶 LLM、包含人機協作 UI，且無需任何建構步驟——這在 GUI 代理工具中是獨特的組合。

---

## 30. [skills](https://github.com/huggingface/skills)
> 用於編碼代理的可重用 AI/ML 任務定義

**Language:** Python  |  **Stars:** 9,154  |  **Forks:** 552  |  **Best Score:** 6,069  |  **Best Rank:** #4  |  **Weeks on chart:** 2/4  |  **Days on chart:** 5/28  |  **Created:** 2025-11-24

**背景：** Hugging Face Skills 是官方資源庫，包含可跨多個編碼代理使用的可重用 AI/ML 任務定義，包括 Claude Code、OpenAI Codex、Google Gemini CLI 和 Cursor。它封裝了 10 個以上的技能，涵蓋從資料集建立和模型訓練到評估和論文發表的 ML 工作流程。已超過 9,100 顆星。

**解決的問題：** 為每個編碼代理設定專門的 ML 工作流程需要手動配置指令、腳本和資源。Hugging Face Skills 將這些標準化為自包含、可攜式的資料夾，任何相容的代理都能載入和執行。

**為何又一個？** 跨代理相容性是關鍵差異化因素——這些技能無論開發者使用 Claude Code、Codex、Gemini 還是 Cursor 都能一致運作。Hugging Face 在 ML 生態系統中的機構地位賦予這些技能對 HF 特定工作流程的權威覆蓋。

---

## 31. [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
> 從零重建你喜愛的技術，精通程式設計。

**Language:** Markdown  |  **Stars:** 478,077  |  **Forks:** 44,967  |  **Best Score:** 5,636  |  **Best Rank:** #5  |  **Weeks on chart:** 3/4  |  **Days on chart:** 6/28  |  **Created:** 2018-05-09

**背景：** build-your-own-x 彙集了從零開始重建熱門技術的逐步指南——從 3D 渲染器到作業系統再到神經網路。擁有超過 478,000 顆星，它是 GitHub 上星數最高的儲存庫之一。隨著新一波開發者發現它，它會定期登上趨勢榜。

**解決的問題：** 理解複雜系統的內部運作需要自己動手建構，但在軟體工程的完整範圍中找到高品質的「從零建構 X」教學非常耗時。此資源庫將它們全部索引起來。

**為何又一個？** 它是同類中最權威的合集，涵蓋的技術類別超過任何競爭資源。其持久的受歡迎程度源於它所體現的費曼原則：「我無法創造的東西，我就不理解。」

---

## 32. [heretic](https://github.com/p-e-w/heretic)
> 語言模型的全自動審查移除工具

**Language:** Python  |  **Stars:** 14,817  |  **Forks:** 1,505  |  **Best Score:** 5,620  |  **Best Rank:** #3  |  **Weeks on chart:** 2/4  |  **Days on chart:** 7/28  |  **Created:** 2025-09-21

**背景：** Heretic 是由 p-e-w 開發的 Python 工具，能自動移除語言模型的內容過濾和拒絕行為。它針對本機運行的模型而非 API 存取服務，使用技術在推理時修改模型行為。自 2025 年 9 月發布以來，已吸引近 15,000 顆星，並在社群中引發了關於模型審查移除的倫理與合法性的大量討論。

**解決的問題：** 針對公開部署進行微調的語言模型，往往會拒絕來自研究人員、安全專業人員和在敏感但合法領域工作的開發者的正當請求。Heretic 為在自有硬體上運行模型的使用者提供了一種本機自動化方法來移除這些限制，無需手動微調或資料集整理。

**為何又一個？** 該專案佔據了一個刻意具爭議性的利基——自動化、無需專業知識的審查移除——使其有別於手動越獄或微調方法。其自動化和本機優先的設計意味著使用者無需將資料傳送給第三方。

---

## 33. [deer-flow](https://github.com/bytedance/deer-flow)
> 開源超級代理框架，能進行研究、編碼和創作。借助沙箱、記憶、工具、技能和子代理，處理從數分鐘到數小時的不同層級任務。

**Language:** Python  |  **Stars:** 31,454  |  **Forks:** 3,802  |  **Best Score:** 5,393  |  **Best Rank:** #5  |  **Weeks on chart:** 2/4  |  **Days on chart:** 6/28  |  **Created:** 2025-05-07

**背景：** DeerFlow（Deep Exploration and Efficient Research Flow）是字節跳動推出的開源超級代理框架，2.0 版本為全面重寫。它協調子代理、記憶和沙箱來完成幾乎任何任務。於 2026 年 2 月 28 日登上 GitHub 趨勢榜第一名，已累積超過 31,000 顆星。

**解決的問題：** 現有的 AI 代理通常只擅長單一任務類型，缺乏跨研究、編碼和創作的統一工作流程。DeerFlow 透過可擴展的技能系統、子代理協調和沙箱執行環境，提供一個能處理複雜多步驟任務的統一平台。

**為何又一個？** 從深度研究框架演進為超級代理框架的轉型——結合 Claude Code 整合、長期記憶、MCP 伺服器和即時通訊頻道支援——使 DeerFlow 2.0 有別於僅專注於單一領域的代理工具。字節跳動火山引擎的編碼計畫贊助提供了企業級支持。

---

## 34. [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
> GitNexus：零伺服器程式碼智慧引擎

**Language:** TypeScript  |  **Stars:** 14,368  |  **Forks:** 1,674  |  **Best Score:** 5,354  |  **Best Rank:** #6  |  **Weeks on chart:** 3/4  |  **Days on chart:** 9/28  |  **Created:** 2025-08-02

**背景：** GitNexus 是 Abhigyan Patwari 開發的用戶端程式碼智慧工具，能將任何程式碼庫索引為知識圖譜——捕捉依賴關係、呼叫鏈、叢集和執行流程——並透過 AI 代理工具公開它們。它完全在瀏覽器中運行，無需伺服器元件。該專案已累積超過 14,000 顆星。

**解決的問題：** 像 Cursor 和 Claude Code 這樣的 AI 編碼助手經常做出破壞性變更，因為它們缺乏對程式碼元件之間關係的深層架構感知。GitNexus 在索引時提供預計算的關聯智慧，使代理在做出修改之前就能理解依賴鏈。

**為何又一個？** GitNexus 預計算關聯關係而非要求 LLM 在查詢時探索原始圖譜資料，使較小的模型也能達到企業級的程式碼理解。完全用戶端、本機優先的架構確保了完整的隱私——沒有任何程式碼離開開發者的機器。

---

## 35. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code 是一個在你終端機中運行的代理式編碼工具，能理解你的程式碼庫並幫助你更快地編碼

**Language:** Shell  |  **Stars:** 79,149  |  **Forks:** 6,480  |  **Best Score:** 4,956  |  **Best Rank:** #5  |  **Weeks on chart:** 4/4  |  **Days on chart:** 16/28  |  **Created:** 2025-02-22

**背景：** Claude Code 是 Anthropic 的官方代理式編碼工具，從終端機運作，能透過自然語言命令讀取、寫入和執行程式碼。擁有超過 79,000 顆星，它仍然是 GitHub 上最持續趨勢的開發者工具之一。可透過 Homebrew、WinGet 和 shell 腳本在 macOS、Linux 和 Windows 上使用。

**解決的問題：** 開發者在重複性編碼任務、程式碼庫導覽和 git 工作流程上花費大量時間，這些都可以透過自然語言指令自動化。Claude Code 直接從命令列處理這些任務，在現有終端機工作流程中運作，而非需要獨立的 IDE 或網頁介面。

**為何又一個？** 作為 Anthropic 的官方產品，Claude Code 受益於第一方模型整合和代理能力的快速迭代。其持續的榜上存在——以及圍繞它建立的技能、技巧和協調工具生態系統——反映了其作為參考實作的地位。

---

## 36. [agent-browser](https://github.com/vercel-labs/agent-browser)
> 為 AI 代理設計的瀏覽器自動化 CLI

**Language:** Rust  |  **Stars:** 23,084  |  **Forks:** 1,360  |  **Best Score:** 4,758  |  **Best Rank:** #11  |  **Weeks on chart:** 2/4  |  **Days on chart:** 4/28  |  **Created:** 2026-01-11

**背景：** Agent Browser 是 Vercel Labs 開發的基於 Rust 的瀏覽器自動化 CLI 工具，專為 AI 代理設計。它提供命令列介面讓代理能程式化地控制瀏覽器進行網頁互動。已累積超過 23,000 顆星。

**解決的問題：** AI 代理需要與網頁互動來完成研究、測試和資料收集等任務，但現有的瀏覽器自動化工具並未針對代理的使用模式進行最佳化。Agent Browser 提供了一個為代理工作流程量身打造的精簡介面。

**為何又一個？** Rust 實作帶來的效能優勢和 Vercel 的品牌背書使其在眾多瀏覽器自動化工具中脫穎而出。CLI 優先的設計使其能無縫整合到終端機為基礎的代理工作流程中。

---

## 37. [claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)
> 一組用於研究、科學、工程、分析、金融和寫作的即用 Agent Skills。

**Language:** Python  |  **Stars:** 15,049  |  **Forks:** 1,659  |  **Best Score:** 4,566  |  **Best Rank:** #10  |  **Weeks on chart:** 2/4  |  **Days on chart:** 5/28  |  **Created:** 2025-10-19

**背景：** Claude Scientific Skills 是由 K-Dense AI 建立的 170 多個即用型科學和研究技能合集，涵蓋生物學、化學、醫學、基因體學、分子動力學、地理空間科學、時間序列預測、經濟資料等。這些技能遵循開放的 Agent Skills 標準，適用於 Cursor、Claude Code 和 Codex。已超過 15,000 顆星。

**解決的問題：** 希望使用 AI 代理處理複雜多步驟工作流程的科學家和研究人員，需要編碼了正確方法論的特定領域技能——而非通用的程式碼生成。此合集提供了理解科學資料格式、統計方法和研究工作流程的技能。

**為何又一個？** 涵蓋的科學領域廣度（170 多個技能，跨越生物學、化學、醫學、金融和地理空間科學）遠超任何個別研究人員能夠自行建構的規模。對化學、生物和金融專用 Python 套件的專注服務了 Anthropic 官方技能資源庫未具體瞄準的專業受眾。

---

## 38. [skills](https://github.com/anthropics/skills)
> Agent Skills 公開資源庫

**Language:** Python  |  **Stars:** 95,927  |  **Forks:** 10,328  |  **Best Score:** 4,510  |  **Best Rank:** #8  |  **Weeks on chart:** 3/4  |  **Days on chart:** 7/28  |  **Created:** 2025-09-22

**背景：** 這是 Anthropic 的官方 Agent Skills 範例公開資源庫——自包含的指令、腳本和資源資料夾，Claude 能動態載入以提升在專門任務上的表現。擁有超過 95,000 顆星，它是代理技能生態系統中最受矚目的資源庫之一。包含用於 DOCX、PDF、PPTX 和 XLSX 檔案的生產文件編輯技能的原始碼可用實作。

**解決的問題：** 教導 Claude 執行特定、可重複的任務——套用品牌指南、遵循組織工作流程、自動化個人例行事務——需要結構化的指令封裝。這個資源庫同時提供了 Agent Skills 標準的規格和從簡單到複雜的大量範例。

**為何又一個？** 作為 Anthropic 的官方資源庫，它定義了第三方集合所依循的技能標準。包含 Claude 實際能力中使用的生產文件編輯技能，使其成為參考實作而非僅是範例集合。

---

## 39. [ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)
> 12 堂課帶你開始建構 AI 代理

**Language:** Jupyter Notebook  |  **Stars:** 54,260  |  **Forks:** 18,793  |  **Best Score:** 4,298  |  **Best Rank:** #14  |  **Weeks on chart:** 2/4  |  **Days on chart:** 2/28  |  **Created:** 2024-11-28

**背景：** 這門由微軟撰寫的課程提供 12 堂結構化課程，從基礎概念到實際實作教授如何建構 AI 代理。它透過自動翻譯支援多種語言，自 2024 年 11 月以來已累積超過 54,000 顆星，使其成為 GitHub 上最受歡迎的 AI 教育資源之一。

**解決的問題：** AI 代理領域發展迅速，許多開發者缺乏從基礎到生產就緒模式循序漸進的結構化學習路徑。此課程透過實作練習和多語言支援提供了這樣的進程。

**為何又一個？** 微軟的支持提供了信譽和長期維護，透過 GitHub Actions 的多語言翻譯使其對全球受眾皆可存取。其高 fork 數（18,793）表明在課堂和學習小組中的積極使用。

---

## 40. [pinchtab](https://github.com/pinchtab/pinchtab)
> 高效能瀏覽器自動化橋接器和多實例調度器，具備進階隱匿注入和即時儀表板。

**Language:** Go  |  **Stars:** 7,745  |  **Forks:** 579  |  **Best Score:** 4,279  |  **Best Rank:** #7  |  **Weeks on chart:** 2/4  |  **Days on chart:** 3/28  |  **Created:** 2026-02-15

**背景：** PinchTab 是以 Go 撰寫的獨立 HTTP 伺服器，讓 AI 代理直接控制 Chrome。它以 12MB 二進位檔附帶為 token 效率設計的 HTTP API 發布。伺服器在兩種角色中運作：完整控制面板伺服器和單實例橋接執行環境，提供針對代理消費最佳化的瀏覽器自動化功能。已超過 7,700 顆星。

**解決的問題：** AI 代理需要瀏覽器存取，但現有的自動化工具會產生冗長的回應，消耗過多的 token。PinchTab 的 HTTP API 專為 token 效率設計，回傳結構化的精簡回應，代理可以在不浪費上下文視窗空間的情況下處理。

**為何又一個？** 12MB 的 Go 二進位檔且零外部依賴，與拉入數百 MB 依賴的基於 Node.js 的瀏覽器自動化工具形成鮮明對比。其雙模式架構（伺服器對橋接）為多實例調度和單一瀏覽器控制提供了靈活性。

---

## 41. [markitdown](https://github.com/microsoft/markitdown)
> 將檔案和 Office 文件轉換為 Markdown 的 Python 工具。

**Language:** Python  |  **Stars:** 90,873  |  **Forks:** 5,371  |  **Best Score:** 4,187  |  **Best Rank:** #10  |  **Weeks on chart:** 2/4  |  **Days on chart:** 3/28  |  **Created:** 2024-11-13

**背景：** MarkItDown 是微軟 AutoGen 團隊推出的輕量 Python 工具，可將 PDF、Office 文件、圖片、音訊、HTML 和其他檔案格式轉換為 Markdown。擁有超過 90,000 顆星，它是 GitHub 上最受歡迎的文件轉換工具之一。現在提供 MCP 伺服器用於與 Claude Desktop 整合。

**解決的問題：** 為 LLM 消費準備多種文件類型需要將它們轉換為模型能良好理解的格式。MarkItDown 輸出 Markdown——一種 AI 模型經過大量訓練的格式——而非嘗試高保真度的視覺再現，針對下游 AI 處理而非人類閱讀進行最佳化。

**為何又一個？** 其對 LLM 最佳化輸出的專注使其有別於 Pandoc 等通用轉換工具。Microsoft 的機構支持和 AutoGen 團隊的參與確保了持續開發與 AI 管道使用案例保持一致。其 MCP 伺服器整合將其定位為 AI 代理工作流程的一等工具。

---

## 42. [hello-agents](https://github.com/datawhalechina/hello-agents)
> 從零開始的智能體原理與實踐教程

**Language:** Python  |  **Stars:** 28,160  |  **Forks:** 3,202  |  **Best Score:** 4,043  |  **Best Rank:** #12  |  **Weeks on chart:** 2/4  |  **Days on chart:** 4/28  |  **Created:** 2025-09-07

**背景：** hello-agents 是由 Datawhale 中國開源學習社群推出的智能體入門教程，從零開始講解智能體的原理與實踐。已累積超過 28,000 顆星，提供系統化的中文學習路徑，涵蓋從基礎概念到進階實作的完整知識體系。

**解決的問題：** 中文開發者社群缺乏系統化的 AI 智能體學習資源，大部分高品質教程僅有英文版本。hello-agents 以中文為第一語言提供結構化教程，降低了中文開發者進入 AI 代理領域的門檻。

**為何又一個？** Datawhale 在中國開源教育社群的影響力確保了高品質的內容和持續的維護。其高星數反映了中文開發者對本地化 AI 代理教育資源的迫切需求。

---

## 43. [awesome](https://github.com/sindresorhus/awesome)
> 關於各種有趣主題的精選列表

**Language:** N/A  |  **Stars:** 446,146  |  **Forks:** 33,577  |  **Best Score:** 3,847  |  **Best Rank:** #6  |  **Weeks on chart:** 2/4  |  **Days on chart:** 3/28  |  **Created:** 2014-07-11

**背景：** Sindre Sorhus 的「awesome」是 GitHub 上精選 awesome 列表的元列表，涵蓋從程式語言到硬體到媒體的每一個可想像的主題。擁有超過 446,000 顆星，它是整個平台上最受矚目的資源庫之一。

**解決的問題：** GitHub 原生的發現機制在尋找高品質的精選資源列表方面較為薄弱。這個元列表作為更廣泛 awesome 列表生態系統的標準入口，以嚴格的品質標準維護收錄門檻。

**為何又一個？** 它是原創的，不是「又一個」。其週期性的趨勢出現反映的是新 GitHub 使用者首次發現它，而非專案本身的任何變化。

---

## 44. [prompts.chat](https://github.com/f/prompts.chat)
> 從社群中分享、發現和收集提示詞。免費且開源——可為你的組織自託管以確保完全隱私。

**Language:** HTML  |  **Stars:** 152,714  |  **Forks:** 20,080  |  **Best Score:** 3,823  |  **Best Rank:** #3  |  **Weeks on chart:** 3/4  |  **Days on chart:** 9/28  |  **Created:** 2022-12-05

**背景：** 由 Fatih Kadir Akin 於 2022 年 12 月以「Awesome ChatGPT Prompts」之名推出，prompts.chat 是第一個針對 AI 聊天模型的主要開源提示詞集合。此後它演變為一個完整的社群平台，具備網頁前端、Hugging Face 資料集、自託管選項，以及一本關於提示工程的互動書籍。該資源庫有 40 多篇學術引用。

**解決的問題：** 早期 ChatGPT 使用者沒有系統提示詞和基於角色的指令共享資源庫，使得提示詞的發現純粹依靠口耳相傳。這個資源庫提供了一個結構化、由社群維護的角色和任務提示詞庫，可作為起點使用。

**為何又一個？** 從「Awesome ChatGPT Prompts」到 prompts.chat 的品牌重塑反映了專案從靜態列表到可自託管平台的演進。儘管代理式工作流程興起，提示工程社群仍然活躍參與。

---

## 45. [llmfit](https://github.com/AlexsJones/llmfit)
> 數百個模型和供應商。一條命令找出你的硬體能跑什麼。

**Language:** Rust  |  **Stars:** 17,068  |  **Forks:** 972  |  **Best Score:** 3,757  |  **Best Rank:** #8  |  **Weeks on chart:** 3/4  |  **Days on chart:** 5/28  |  **Created:** 2026-02-15

**背景：** llmfit 是 Alexs Jones 開發的基於 Rust 的終端工具，能自動偵測系統規格（RAM、CPU 核心數、GPU VRAM）並在品質、速度、記憶體適配和上下文能力等維度上為數百個 LLM 模型評分。支援多 GPU 配置、MoE 架構、動態量化選擇和本地執行環境供應商（Ollama、llama.cpp、MLX）。已超過 17,000 顆星。

**解決的問題：** 確定哪些 LLM 模型實際能在特定機器上運行，需要手動交叉比對跨多個文件來源的模型大小、量化格式和硬體規格。llmfit 透過一條命令即可產出排序的相容性報告，消除了這種猜測。

**為何又一個？** 大多數模型推薦工具是基於網頁的或需要將硬體規格上傳到服務。llmfit 完全在本機運行，具備自動硬體偵測、多維度評分和與本機推理執行環境的直接整合——使其成為「我能跑什麼？」這個問題的 CLI 原生答案。

---

## 46. [Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)
> O'Reilly 書籍《Hands-On Large Language Models》的官方程式碼資源庫

**Language:** Jupyter Notebook  |  **Stars:** 24,115  |  **Forks:** 5,578  |  **Best Score:** 3,676  |  **Best Rank:** #4  |  **Weeks on chart:** 2/4  |  **Days on chart:** 5/28  |  **Created:** 2024-06-28

**背景：** 這是由 Jay Alammar 和 Maarten Grootendorst 合著的 O'Reilly 書籍《Hands-On Large Language Models》的配套程式碼庫，被稱為「圖解 LLM 書」。包含近 300 張自製圖表，透過視覺化教學方式從語言模型基礎到進階應用逐步講解。已超過 24,000 顆星。

**解決的問題：** 理解大型語言模型的內部運作需要大量的理論知識和實作經驗，但大多數教材要麼過於學術要麼缺乏實際程式碼。這本書結合視覺化解釋和 Google Colab 筆記本，提供了從概念到實作的完整路徑。

**為何又一個？** 由 Jay Alammar（以「圖解 Transformer」系列聞名）和 Maarten Grootendorst 合著的權威性，加上 O'Reilly 出版社的背書和完整的 Colab 實作，使其成為 LLM 學習的標桿教材。

---

## 47. [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)
> 1000 多個代理技能的終極合集，適用於 Claude Code/Antigravity/Cursor。

**Language:** Python  |  **Stars:** 24,814  |  **Forks:** 4,253  |  **Best Score:** 3,616  |  **Best Rank:** #4  |  **Weeks on chart:** 2/4  |  **Days on chart:** 5/28  |  **Created:** 2026-01-14

**背景：** Antigravity Awesome Skills 收錄了 1,234 多個代理技能，相容 Claude Code、Gemini CLI、Codex CLI、Cursor、GitHub Copilot 等。它將自己定位為跨多個代理平台的通用技能合集，透過自動化登錄檔同步進行維護。已超過 24,000 顆星。

**解決的問題：** 從頭建構有效的代理工作流程需要大量的提示工程和工具呼叫專業知識。這個集合提供了經過實戰測試、可即時安裝的技能，編碼了常見開發任務的最佳實踐，使團隊能夠在不花數週開發自訂技能的情況下採用代理工作流程。

**為何又一個？** 跨平台相容性聲明（Claude Code、Gemini CLI、Codex、Cursor、Copilot 及其他）使其有別於特定平台的合集。自動同步機制使其與上游登錄檔保持同步。

---

## 48. [production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course)
> 生產級代理式 RAG 課程

**Language:** Python  |  **Stars:** 3,881  |  **Forks:** 1,036  |  **Best Score:** 3,272  |  **Best Rank:** #15  |  **Weeks on chart:** 2/4  |  **Days on chart:** 2/28  |  **Created:** 2025-08-06

**背景：** production-agentic-rag-course 是一個實踐導向的課程資源庫，教授如何建構生產級的代理式 RAG（檢索增強生成）系統。自 2025 年 8 月創建以來已超過 3,800 顆星，提供從基礎到進階的完整學習路徑。

**解決的問題：** 大多數 RAG 教程停留在概念驗證階段，缺乏從原型到生產部署的完整指導。這個課程專注於生產級考量——可擴展性、可靠性和代理式架構——填補了教育資源與實際部署之間的鴻溝。

**為何又一個？** 「生產級」和「代理式」的結合瞄準了當前 AI 工程的核心需求——不僅是建構 RAG 系統，而是建構能自主運作的生產就緒 RAG 代理。

---

## 49. [opencode](https://github.com/anomalyco/opencode)
> 開源編碼代理。

**Language:** TypeScript  |  **Stars:** 124,099  |  **Forks:** 12,973  |  **Best Score:** 3,194  |  **Best Rank:** #10  |  **Weeks on chart:** 2/4  |  **Days on chart:** 6/28  |  **Created:** 2025-04-30

**背景：** OpenCode 是由 anomalyco 維護的開源 AI 編碼代理，擁有 805 位以上的貢獻者。它作為基於終端機的 AI 輔助開發介面，提供 Claude Code 的供應商無關替代方案。擁有超過 124,000 顆星，它是 GitHub 上最受矚目的開源編碼代理。

**解決的問題：** 專有編碼代理將開發者鎖定在特定的模型供應商和定價結構中。OpenCode 提供同等的基於終端機的編碼輔助，同時允許使用者選擇偏好的語言模型，具備內建的 LSP 功能和支援遠端操作的客戶端-伺服器架構。

**為何又一個？** 完全的模型供應商獨立性是核心差異化因素。雖然 Claude Code 針對 Claude 模型進行了最佳化，OpenCode 的架構支援任何模型，使其成為想要無供應商承諾的代理輔助開發的團隊的預設選擇。

---

## 50. [MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2)
> 自動化線上賺錢流程。

**Language:** Python  |  **Stars:** 15,047  |  **Forks:** 1,514  |  **Best Score:** 3,124  |  **Best Rank:** #18  |  **Weeks on chart:** 2/4  |  **Days on chart:** 3/28  |  **Created:** 2024-02-12

**背景：** MoneyPrinterV2 由 FujiwaraChoki 開發，是一個自動化內容創作和發布的 Python 工具，能自動生成影片、文章等內容並發布到多個平台。自 2024 年 2 月創建以來已超過 15,000 顆星。

**解決的問題：** 內容創作和線上變現需要大量重複性工作——從構思、製作到發布和推廣。MoneyPrinterV2 將這些步驟自動化，讓使用者能以最少的手動操作產出和分發內容。

**為何又一個？** 將 AI 內容生成與多平台自動發布結合在單一工具中，是對單獨使用 AI 寫作工具或手動發布的重大效率提升。其直白的定位——自動化賺錢——吸引了對 AI 商業應用感興趣的廣泛受眾。

---

## 51. [claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
> 官方的、由 Anthropic 管理的高品質 Claude Code 插件目錄。

**Language:** Python  |  **Stars:** 11,927  |  **Forks:** 1,153  |  **Best Score:** 3,122  |  **Best Rank:** #15  |  **Weeks on chart:** 2/4  |  **Days on chart:** 4/28  |  **Created:** 2025-11-20

**背景：** Claude Plugins Official 是 Anthropic 維護的高品質 Claude Code 插件策展目錄，包含內部開發和經審核的第三方插件。每個插件遵循標準結構——包含 plugin.json 元資料、MCP 伺服器配置、命令、代理和技能定義。已超過 11,900 顆星。

**解決的問題：** 隨著 Claude Code 插件生態系統的快速成長，開發者需要一個可信賴的來源來發現經過品質和安全審核的插件。這個官方目錄提供了該保證，同時為第三方開發者提供了標準化的提交流程。

**為何又一個？** 作為 Anthropic 官方管理的目錄，它設定了插件品質和安全的標準。第三方插件需透過提交表單和審核流程才能入選，這與社群自由提交的列表形成了信任差異化。

---

## 52. [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)
> AI 對沖基金團隊

**Language:** Python  |  **Stars:** 49,228  |  **Forks:** 8,567  |  **Best Score:** 3,097  |  **Best Rank:** #21  |  **Weeks on chart:** 2/4  |  **Days on chart:** 2/28  |  **Created:** 2024-11-29

**背景：** AI Hedge Fund 是一個概念驗證專案，探索使用 AI 進行交易決策。它部署了 18 個代理——模擬 Warren Buffett、Charlie Munger、Cathie Wood 等知名投資者的策略——協同工作進行股票分析和交易決策。已超過 49,000 顆星。

**解決的問題：** 將多種投資哲學和分析維度（基本面、技術面、情緒面、風險管理）整合到統一的決策流程中，通常需要大型團隊和昂貴的基礎設施。AI Hedge Fund 將這些角色自動化為可協作的 AI 代理。

**為何又一個？** 透過模擬 12 位知名投資者的獨特風格和哲學，AI Hedge Fund 提供了一種教育性和實驗性兼具的方法來理解不同投資策略。明確的「僅供教育目的」定位和不進行實際交易的設計原則確保了負責任的使用。

---

## 53. [superset](https://github.com/superset-sh/superset)
> AI 代理時代的 IDE——在你的機器上運行 Claude Code、Codex 等代理大軍

**Language:** TypeScript  |  **Stars:** 7,095  |  **Forks:** 489  |  **Best Score:** 2,989  |  **Best Rank:** #17  |  **Weeks on chart:** 2/4  |  **Days on chart:** 4/28  |  **Created:** 2025-10-21

**背景：** Superset 是一個為 AI 代理時代設計的 IDE，允許使用者在單一介面中同時運行和管理多個 Claude Code、Codex 等編碼代理實例。已累積超過 7,000 顆星，定位為多代理協作的統一工作環境。

**解決的問題：** 同時運行多個編碼代理需要在不同終端機視窗之間切換，缺乏統一的檢視和管理介面。Superset 提供了一個集中化的環境來啟動、監控和協調多個代理的工作。

**為何又一個？** 「代理大軍」的概念——一個 IDE 中同時運行多個獨立代理——瞄準了已經在日常工作中依賴多個 AI 代理的高階開發者。這種多代理 IDE 定位在現有工具中是獨特的。

---

## 54. [qmd](https://github.com/tobi/qmd)
> 迷你 CLI 搜尋引擎，適用於你的文件、知識庫、會議筆記等。追蹤當前最先進的方法，完全在本機運行。

**Language:** TypeScript  |  **Stars:** 15,505  |  **Forks:** 907  |  **Best Score:** 2,933  |  **Best Rank:** #20  |  **Weeks on chart:** 2/4  |  **Days on chart:** 2/28  |  **Created:** 2025-12-08

**背景：** qmd 由 Shopify CEO Tobi Lutke 開發，是一個本機優先的 CLI 搜尋引擎，用於搜尋個人文件、知識庫和會議筆記。它追蹤當前最先進的檢索方法，完全在本機運行，不需要任何雲端服務。已超過 15,500 顆星。

**解決的問題：** 個人知識管理中的搜尋功能通常依賴雲端服務或功能有限的全文搜尋。qmd 將先進的檢索技術帶到本機 CLI 環境，使使用者能在自己的文件中進行高品質搜尋，同時保持完全的隱私。

**為何又一個？** 由 Shopify CEO Tobi Lutke 開發的背景賦予了專案獨特的可信度。完全本機運行的設計和追蹤最先進檢索方法的承諾，使其成為注重隱私的知識工作者的理想工具。

---

## 55. [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
> 代理框架效能最佳化系統

**Language:** JavaScript  |  **Stars:** 77,533  |  **Forks:** 9,755  |  **Best Score:** 2,929  |  **Best Rank:** #11  |  **Weeks on chart:** 3/4  |  **Days on chart:** 8/28  |  **Created:** 2026-01-18

**背景：** Everything Claude Code（ECC）是 Affaan Mustafa 開發的全面 Claude Code 外掛系統，從 Anthropic 黑客松獲獎作品演化而來。它提供代理、技能、命令、鉤子和規則，用於最佳化 AI 代理效能。擁有超過 77,000 顆星，它是最受歡迎的 Claude Code 生態系統專案之一。

**解決的問題：** 原始的 AI 代理能力在缺乏 Token 最佳化、跨會話記憶持久化、驗證迴圈和領域特定專業化的情況下會在實踐中退化。ECC 提供了一個完整的生態系統，將原始能力轉化為生產就緒的開發工作流程。

**為何又一個？** 「本能」概念——無需明確調用即自動觸發的行為模式——是對代理最佳化的新穎貢獻。不同於通用配置套件，ECC 為不同領域提供專門代理（規劃、測試、安全審查），結合 Token 最佳化和記憶持久化。

---

## 56. [daytona](https://github.com/daytonaio/daytona)
> Daytona 是用於運行 AI 生成程式碼的安全且彈性基礎設施

**Language:** TypeScript  |  **Stars:** 66,271  |  **Forks:** 5,080  |  **Best Score:** 2,925  |  **Best Rank:** #10  |  **Weeks on chart:** 3/4  |  **Days on chart:** 4/28  |  **Created:** 2024-02-06

**背景：** Daytona 提供安全、隔離的沙箱環境用於執行 AI 生成的程式碼，具備亞 90 毫秒的沙箱創建速度、無限持久化和 OCI/Docker 相容性。提供 Python 和 TypeScript SDK，已累積超過 66,000 顆星，成為 AI 程式碼執行基礎設施的領先方案。

**解決的問題：** AI 代理生成的程式碼需要在隔離環境中安全執行，但自建沙箱基礎設施既複雜又昂貴。Daytona 提供即用型的彈性沙箱基礎設施，具備程式化的檔案、Git、LSP 和執行 API。

**為何又一個？** 亞 90 毫秒的沙箱創建速度和無限持久化使其在效能上超越大多數替代方案。Product Hunt 日榜第一和主題月榜第一的成績證明了市場對專業 AI 程式碼執行基礎設施的強烈需求。

---

## 57. [humanizer](https://github.com/blader/humanizer)
> 從文字中移除 AI 生成寫作痕跡的 Claude Code 技能

**Language:** N/A  |  **Stars:** 9,565  |  **Forks:** 766  |  **Best Score:** 2,874  |  **Best Rank:** #7  |  **Weeks on chart:** 3/4  |  **Days on chart:** 3/28  |  **Created:** 2026-01-18

**背景：** Humanizer 由 blader 開發，是一個 Claude Code 技能，能識別和移除 24 種 AI 生成寫作的獨特標記，從「marking a pivotal moment」等企業用語到過多破折號和表情符號濫用等結構問題。該方法基於 Wikipedia 由編輯眾包維護的「AI 寫作跡象」指南，這些編輯已審查了數千篇 AI 生成的文章。已超過 9,500 顆星。

**解決的問題：** AI 生成的文字帶有讀者和偵測工具能識別為機器寫作的可辨認模式。Humanizer 執行多遍審計——初始偵測後進行改寫——以系統性地移除這些人工模式，同時保留內容意義。

**為何又一個？** 將偵測標記基於 Wikipedia 的眾包編輯指南而非專有啟發式方法，提供了透明度和社群驗證的準確性。與 Claude Code 技能系統的緊密整合使其成為單一指令操作，而非需要另外使用的工具。

---

## 58. [airllm](https://github.com/lyogavin/airllm)
> AirLLM 在單一 4GB GPU 上運行 70B 推理

**Language:** Jupyter Notebook  |  **Stars:** 13,984  |  **Forks:** 1,386  |  **Best Score:** 2,658  |  **Best Rank:** #7  |  **Weeks on chart:** 2/4  |  **Days on chart:** 2/28  |  **Created:** 2023-06-12

**背景：** AirLLM 由 lyogavin 開發，能在僅有 4GB VRAM 的單一 GPU 上進行 70B 參數語言模型的推理。該專案使用逐層載入和最佳化的記憶體管理，使大型模型在消費級硬體上可用。自 2023 年推出以來已累積近 14,000 顆星。

**解決的問題：** 運行 70B 模型通常需要多張高階 GPU 或每月花費數百美元的雲端實例。AirLLM 透過以吞吐量換取記憶體效率，使這些模型在一般硬體上可用。

**為何又一個？** 在 4GB GPU 上運行 70B 模型且不因量化造成品質損失的能力，是比 llama.cpp 或 GPTQ 更極端的記憶體最佳化。AirLLM 將各層串流通過 GPU 記憶體，VRAM 需求取決於最大的單一層而非完整模型。

---

## 59. [openclaw-studio](https://github.com/grp06/openclaw-studio)
> OpenClaw 的清爽網頁儀表板。連接你的 Gateway，管理代理，更快交付。

**Language:** TypeScript  |  **Stars:** 1,631  |  **Forks:** 239  |  **Best Score:** 2,550  |  **Best Rank:** #17  |  **Weeks on chart:** 2/4  |  **Days on chart:** 2/28  |  **Created:** 2026-01-28

**背景：** OpenClaw Studio 由 grp06 開發，是 OpenClaw 的網頁管理儀表板，提供視覺化介面來連接 Gateway、管理代理和加速開發流程。自 2026 年 1 月底發布以來已超過 1,600 顆星。

**解決的問題：** OpenClaw 主要透過命令列和配置檔管理，對於偏好圖形介面的使用者來說操作門檻較高。OpenClaw Studio 提供了直觀的網頁 UI，降低了管理和監控 OpenClaw 實例的複雜度。

**為何又一個？** 作為 OpenClaw 生態系統中的管理工具，它填補了核心平台在視覺化管理方面的空白。其上榜也是 OpenClaw 生態系統成熟度的又一指標。

---

## 60. [daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)
> LLM 驅動的 A/H/美股智能分析器，多數據源行情 + 即時新聞 + LLM 決策儀表板 + 多渠道推送，零成本，完全免費，定時運行

**Language:** Python  |  **Stars:** 20,639  |  **Forks:** 21,366  |  **Best Score:** 2,482  |  **Best Rank:** #18  |  **Weeks on chart:** 3/4  |  **Days on chart:** 4/28  |  **Created:** 2026-01-10

**背景：** daily_stock_analysis 是由 ZhuLinsen 開發的 AI 驅動股票分析系統，支援 A 股、港股和美股。它整合多維度分析（技術面、籌碼分布、輿情情報），透過 LLM 生成決策儀表板，並支援企業微信、飛書、Telegram、Discord、Email 等多渠道推送。已超過 20,000 顆星。

**解決的問題：** 散戶投資者缺乏機構級的多維度股票分析工具，且現有方案通常需要付費訂閱或技術門檻高。daily_stock_analysis 透過 GitHub Actions 免費定時運行，零伺服器成本即可獲得包含精確買賣點位的 AI 分析報告。

**為何又一個？** 透過 LiteLLM 支援全球主流 AI 模型、整合 AkShare 等多數據源、以及 GitHub Actions 零成本自動化的組合，使其成為個人投資者的完整 AI 分析方案。Agent 問股功能支援 11 種內置策略的多輪對話，進一步提升了實用性。

---

## 61. [agents](https://github.com/cloudflare/agents)
> 在 Cloudflare 上建構和部署 AI 代理

**Language:** TypeScript  |  **Stars:** 4,553  |  **Forks:** 453  |  **Best Score:** 2,402  |  **Best Rank:** #17  |  **Weeks on chart:** 2/4  |  **Days on chart:** 2/28  |  **Created:** 2025-01-29

**背景：** Cloudflare Agents 是 Cloudflare 的官方開源框架，用於在其邊緣網路上建構和部署 AI 代理。自 2025 年 1 月發布以來已超過 4,500 顆星，提供了利用 Cloudflare 全球基礎設施運行代理的標準化方法。

**解決的問題：** 部署 AI 代理需要處理伺服器管理、擴展和全球分佈等基礎設施問題。Cloudflare Agents 利用其邊緣網路，使代理能在全球範圍內低延遲運行，無需管理傳統伺服器基礎設施。

**為何又一個？** Cloudflare 的全球邊緣網路為 AI 代理部署帶來了獨特的低延遲和全球覆蓋優勢。作為主要雲端平台的官方代理框架，它代表了基礎設施供應商開始為 AI 代理時代提供原生支援的趨勢。

---

## 62. [Mole](https://github.com/tw93/Mole)
> 深度清理並優化你的 Mac。

**Language:** Shell  |  **Stars:** 40,859  |  **Forks:** 1,146  |  **Best Score:** 2,319  |  **Best Rank:** #12  |  **Weeks on chart:** 3/4  |  **Days on chart:** 4/28  |  **Created:** 2025-09-23

**背景：** Mole 由 tw93 開發，是一個多合一的 macOS 命令列工具，在單一二進位檔中結合了系統清理、具備殘留移除的智慧應用程式卸載、磁碟分析和即時系統監控。自 2025 年 9 月推出以來已成長至超過 40,000 顆星。

**解決的問題：** Mac 使用者通常需要多個付費應用程式——CleanMyMac 用於清理、AppCleaner 用於卸載、DaisyDisk 用於磁碟分析——來維護系統。Mole 將所有這些整合到一個免費的 MIT 授權 CLI 工具中。

**為何又一個？** 具備 Raycast 整合的 CLI 原生方法瞄準了偏好終端機工作流程而非 GUI 應用程式的進階使用者。作為透明的 shell 腳本而非編譯的二進位檔是關鍵的信任差異化因素——使用者可以在執行前確切閱讀哪些內容會被刪除。

---

## 63. [FossFLOW](https://github.com/stan-smith/FossFLOW)
> 製作精美的等角投影基礎設施圖表

**Language:** TypeScript  |  **Stars:** 19,139  |  **Forks:** 1,252  |  **Best Score:** 2,298  |  **Best Rank:** #15  |  **Weeks on chart:** 2/4  |  **Days on chart:** 3/28  |  **Created:** 2025-06-30

**背景：** FossFLOW 由 Stan Smith 開發，是用於建立等距基礎設施圖表的開源漸進式 Web 應用程式，以 React 和 @markmanx 的 Isoflow 函式庫建構。它完全在瀏覽器中運行，具備完整的離線能力。PWA 架構意味著無需安裝。已超過 19,000 顆星。

**解決的問題：** 建立專業的等角投影基礎設施圖通常需要昂貴的設計軟體或專有圖表工具。FossFLOW 自動化等角投影渲染，讓使用者專注於描述其基礎設施而非繪製它。

**為何又一個？** 等距視覺化、PWA 離線能力和零安裝瀏覽器存取在免費、開源套件中的結合是獨特的。大多數繪圖工具要麼付費、要麼需要安裝、要麼原生不支援等距投影。

---

## 64. [system-design](https://github.com/karanpratapsingh/system-design)
> 學習如何大規模設計系統，並為系統設計面試做準備

**Language:** N/A  |  **Stars:** 42,168  |  **Forks:** 5,354  |  **Best Score:** 2,270  |  **Best Rank:** #19  |  **Weeks on chart:** 2/4  |  **Days on chart:** 2/28  |  **Created:** 2022-08-15

**背景：** system-design 是由 Karan Pratap Singh 建立的系統設計學習資源，以結構化的章節涵蓋了從 IP 協定到微服務、從快取到分散式交易的完整知識體系。已超過 42,000 顆星，同時以網站和 Leanpub 電子書形式提供。

**解決的問題：** 系統設計面試準備需要理解從網路協定到分散式系統的廣泛知識，但大多數資源要麼過於淺顯要麼缺乏結構。這個資源庫提供了從基礎到進階的完整、結構化學習路徑。

**為何又一個？** 涵蓋五大章節的完整課程結構——從基礎設施概念到真實系統設計案例（URL 縮短器、WhatsApp、Twitter、Netflix、Uber）——使其成為系統設計學習和面試準備的一站式資源。

---

## 65. [moonshine](https://github.com/moonshine-ai/moonshine)
> 適用於邊緣裝置的快速且精確的自動語音辨識（ASR）

**Language:** C  |  **Stars:** 7,367  |  **Forks:** 365  |  **Best Score:** 1,894  |  **Best Rank:** #17  |  **Weeks on chart:** 2/4  |  **Days on chart:** 3/28  |  **Created:** 2024-10-04

**背景：** Moonshine Voice 是 moonshine-ai 推出的開源 ASR 工具套件，用於在邊緣裝置上建構即時語音應用程式。它在比 Whisper Large V3 小 6 倍（245M 對比 1.5B 參數）的情況下達到更高的準確率。該框架提供跨 Python、iOS、Android、macOS、Linux、Windows 和 Raspberry Pi 的統一 API。已超過 7,300 顆星。

**解決的問題：** OpenAI 的 Whisper 使用固定 30 秒的輸入視窗且缺乏串流快取，導致即時語音介面延遲高。Moonshine 透過在使用者仍在說話時漸進式處理，使用靈活的輸入視窗和編碼器快取，實現低延遲回應。

**為何又一個？** 在更高準確率下達到 6 倍的大小縮減，是對 Whisper 的重大進步。跨 7 個平台（包括 Raspberry Pi）的 C++ 核心和統一 API 使其在邊緣裝置上真正可部署，而非僅是理論上相容。

---

## 66. [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)
> 最佳代理框架

**Language:** TypeScript  |  **Stars:** 37,162  |  **Forks:** 2,793  |  **Best Score:** 1,749  |  **Best Rank:** #18  |  **Weeks on chart:** 2/4  |  **Days on chart:** 2/28  |  **Created:** 2025-12-03

**背景：** oh-my-opencode 是 code-yeongyu 開發的 OpenCode 代理框架增強套件，定位為「最佳代理框架」。自 2025 年 12 月創建以來已累積超過 37,000 顆星，為 OpenCode 提供最佳化的代理能力和工作流程。

**解決的問題：** OpenCode 的原始代理能力需要額外的配置和最佳化才能達到最佳效能。oh-my-opencode 提供了預配置的增強套件，讓使用者能即刻獲得最佳化的代理體驗。

**為何又一個？** 其超過 37,000 的星數遠超大多數同類增強套件，反映了 OpenCode 使用者社群對提升代理效能的強烈需求。作為 OpenCode 生態系統的旗艦增強工具，它的上榜也是 OpenCode 平台影響力的體現。

---

> **本月主題：** 代理式 AI 從「個人助手」邁向「自主公司」——Paperclip 協調代理團隊運營企業、Agency Agents 提供完整專業代理陣容、DeerFlow 2.0 升級為超級代理框架；與此同時，OpenClaw 生態系統持續擴張，從核心平台到精選目錄、輕量替代方案和管理儀表板全面開花，代理技能作為軟體分發新單位的趨勢更加明確。