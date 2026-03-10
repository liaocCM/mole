# Trendshift 每週報告 — 2026-03-02 至 2026-03-08
**不重複專案總數：** 83（來自 7 天共 175 筆每日上榜紀錄）

---

## 1. [cli](https://github.com/googleworkspace/cli)
> Google Workspace CLI — 一個命令列工具涵蓋 Drive、Gmail、Calendar、Sheets、Docs、Chat、Admin 等服務。從 Google Discovery Service 動態建構。包含 AI 代理技能。

**Language:** Rust  |  **Stars:** 16595  |  **Forks:** 641  |  **Best Score:** 56923  |  **Best Rank:** #1  |  **Days on chart:** 2/7  |  **Created:** 2026-03-02

**背景：** gws 是在 googleworkspace GitHub 組織下發布的新 CLI 工具（雖非 Google 官方支援的產品），為所有 Google Workspace API 提供單一命令列介面。以 Rust 撰寫並透過 npm 分發，它於 3 月 2 日發布後立即登上 Trendshift 排行榜首位，獲得本週最高分數。該工具在執行時讀取 Google 的 Discovery Service 動態建構其命令介面，意味著當 Google 新增 API 端點時，它會自動獲得新功能。

**解決的問題：** 從命令列與 Google Workspace API 互動，歷來需要針對各服務的 SDK、OAuth 樣板程式碼和手寫的 HTTP 請求。gws 將這些整合為一個處理認證並輸出結構化 JSON 的單一二進位檔，使其既適合人工操作者，也適合作為 AI 代理的工具呼叫目標。

**為何又一個？** 不同於在 Google 發布新端點時需要手動更新的靜態 CLI 封裝工具，gws 從 Google 自身的服務定義中動態發現其整個命令介面。它還內建了 40 多個代理技能，將自己定位為 AI 編程助手的一等工具，而非僅供人工使用的實用程式。

---

## 2. [symphony](https://github.com/openai/symphony)
> Symphony 將專案工作轉化為隔離的自主實作執行環境，讓團隊管理工作而非監督編程代理。

**Language:** Elixir  |  **Stars:** 9439  |  **Forks:** 653  |  **Best Score:** 34254  |  **Best Rank:** #2  |  **Days on chart:** 4/7  |  **Created:** 2026-02-26

**背景：** Symphony 是 OpenAI 的專案，連接專案管理看板（如 Linear）與自主編程代理（如 Codex）。以 Elixir 撰寫並作為「工程預覽版」發布，它監控任務看板上的工作項目，生成隔離的代理實例來實作，並回報 CI 狀態、PR 審查、複雜度分析和導覽影片。規格是開放的，OpenAI 鼓勵以任何語言重新實作。

**解決的問題：** 目前的編程代理需要工程師全程陪伴、撰寫提示詞、審查輸出並管理上下文。Symphony 將互動層從「監督代理」提升至「管理待辦事項」，讓工程師描述需要做什麼，而非如何引導代理完成工作。

**為何又一個？** Symphony 值得注意的是它以規格形式發布，而非僅作為實作，明確邀請社群建構替代執行環境。其 Elixir 參考實作利用了 OTP 的進程隔離模型來運行多個並行代理會話，與 OpenAI 的 Codex 整合為其提供了原生的模型基礎設施通道。

---

## 3. [RuView](https://github.com/ruvnet/RuView)
> WiFi DensePose 將一般 WiFi 訊號轉化為即時人體姿態估計、生命體徵監測和存在偵測——完全不需要任何像素的影片。

**Language:** Rust  |  **Stars:** 31832  |  **Forks:** 4198  |  **Best Score:** 24100  |  **Best Rank:** #1  |  **Days on chart:** 3/7  |  **Created:** 2025-06-07

**背景：** RuView 是由 ruvnet 以 Rust 建構的邊緣 AI 感知系統，使用 WiFi 通道狀態資訊（CSI）在完全不使用攝影機的情況下偵測和重建人體姿態、生命體徵和房間存在。它建立在卡內基美隆大學學術研究中首次展示的 WiFi DensePose 概念之上，並使用 RuVector 函式庫將其擴展為實用的邊緣可部署系統。

**解決的問題：** 基於攝影機的監控系統引發嚴重的隱私問題且需要視線範圍內放置。RuView 用一般 WiFi 硬體取代光學感測器，分析人體運動引起的訊號擾動，使用基於物理的訊號處理和機器學習，即時重建身體位置、呼吸速率、心率和存在狀態。

**為何又一個？** 不同於依賴同步攝影機訓練資料的學術 WiFi 感測原型，RuView 設計為完全從射頻訊號和邊緣端自學嵌入向量運作。其 Rust 實作提供了在資源受限硬體上進行即時姿態估計所需的低延遲。

---

## 4. [wifi-densepose](https://github.com/ruvnet/wifi-densepose)
> WiFi DensePose 將一般 WiFi 訊號轉化為即時人體姿態估計、生命體徵監測和存在偵測——完全不需要任何像素的影片。

**Language:** Rust  |  **Stars:** 15004  |  **Forks:** 1567  |  **Best Score:** 20932  |  **Best Rank:** #1  |  **Days on chart:** 1/7  |  **Created:** 2025-06-07

**背景：** wifi-densepose 是 RuView 演化而來的原始儲存庫，同樣由 ruvnet 開發。它共享相同的核心技術——使用 WiFi CSI 資料進行人體姿態估計——並作為更廣泛 RuView 感知平台的基礎程式碼庫。自 2025 年 6 月發布以來已累積 15,000 顆星。

**解決的問題：** 與 RuView 相同：透過利用 WiFi 訊號在人體內部和周圍傳播的物理特性，實現無攝影機的人體感測。系統僅使用標準 WiFi 硬體即可偵測存在、估計身體位置和監測生命體徵。

**為何又一個？** 此儲存庫代表 WiFi 感測概念在擴展為完整 RuView 平台之前的早期、更聚焦的版本。對於專門對 WiFi DensePose 技術感興趣而不需要更廣泛感知框架的團隊，它仍然是一個有用的獨立參考實作。

---

## 5. [paperclip](https://github.com/paperclipai/paperclip)
> 零人力公司的開源調度引擎

**Language:** TypeScript  |  **Stars:** 9517  |  **Forks:** 1062  |  **Best Score:** 14426  |  **Best Rank:** #1  |  **Days on chart:** 2/7  |  **Created:** 2026-03-02

**背景：** Paperclip 是一個 Node.js 伺服器搭配 React 儀表板，用於調度 AI 代理團隊自主運行業務營運。它在本報告同一週發布，將自己定位為個別 AI 助手之上的一層：「如果 OpenClaw 是員工，Paperclip 就是公司。」它為多代理工作流程提供組織架構圖、預算、治理結構和成本追蹤。

**解決的問題：** 個別 AI 代理可以執行任務，但協調跨業務功能——銷售、客服、工程、財務——的多個代理需要組織結構，而這是單一代理所無法提供的。Paperclip 增加了管理層：指派目標、追蹤成本、執行治理，並呈現統一的儀表板。

**為何又一個？** 大多數代理調度工具專注於技術工作流程（CI/CD、程式碼審查）。Paperclip 針對業務層級的調度，借用企業結構的概念——組織架構圖、預算、審批鏈——而非軟體工程管線。其「零人力公司」的定位雖然挑釁，但反映了工具生態中的真實缺口。

---

## 6. [agency-agents](https://github.com/msitarzewski/agency-agents)
> 一個完整的 AI 代理團隊觸手可及——從前端精靈到 Reddit 社群忍者，從趣味注入者到現實檢查者。

**Language:** Shell  |  **Stars:** 18396  |  **Forks:** 2842  |  **Best Score:** 13037  |  **Best Rank:** #1  |  **Days on chart:** 5/7  |  **Created:** 2025-10-13

**背景：** The Agency 是一個由社群維護的專業 AI 代理個性模板合集，誕生於 Reddit 討論串，經過數月的反覆迭代。每個代理模板都包含深度領域專業知識、獨特的溝通風格，以及帶有可衡量成功指標的生產就緒工作流程。該專案設計用於 Claude Code 和類似的 AI 編程助手。

**解決的問題：** 通用的 AI 提示詞產生通用的結果。透過提供精心打造的代理人設——具備特定領域專業知識、以交付物為導向的工作流程和獨特的溝通風格——The Agency 讓使用者無需自行設計複雜提示詞即可獲得專家級輸出。

**為何又一個？** 不同於提供單行提示的提示詞模板合集，The Agency 中的每個代理都是一個完整的個性體，包含流程、成功指標和文件化的交付物。本週五天的上榜紀錄反映了社群對策劃型、個性驅動的代理配置持續的興趣。

---

## 7. [ironclaw](https://github.com/nearai/ironclaw)
> IronClaw 是受 OpenClaw 啟發的 Rust 實作，專注於隱私和安全

**Language:** Rust  |  **Stars:** 8629  |  **Forks:** 908  |  **Best Score:** 12272  |  **Best Rank:** #2  |  **Days on chart:** 2/7  |  **Created:** 2026-02-03

**背景：** IronClaw 是由 NEAR AI 開發的基於 Rust 的個人 AI 助手，建立在「你的 AI 助手應該為你工作，而非與你對立」的理念上。它從 OpenClaw 汲取靈感，但以 Rust 重寫核心，強調本地優先的資料儲存、加密和透明運作。所有使用者資料都儲存在本地並加密，絕不會離開使用者的控制。

**解決的問題：** 主流 AI 助手將對話路由到雲端伺服器，資料處理方式不透明，且與企業利益而非使用者利益保持一致。IronClaw 將所有資訊保存在本地並加密，讓使用者完全擁有其資料，同時仍提供完善的 AI 助手體驗。

**為何又一個？** Rust 重寫提供了 TypeScript 助手無法匹敵的記憶體安全保證和效能特性，而隱私優先的架構使其與 OpenClaw 和雲端助手均有所區別。其 MIT/Apache 雙重授權和 NEAR AI 的支持表明了對開放開發的長期承諾。

---

## 8. [worldmonitor](https://github.com/koala73/worldmonitor)
> 即時全球情報儀表板——AI 驅動的新聞聚合、地緣政治監控和基礎設施追蹤，整合於統一的態勢感知介面中

**Language:** TypeScript  |  **Stars:** 34697  |  **Forks:** 5833  |  **Best Score:** 9274  |  **Best Rank:** #1  |  **Days on chart:** 4/7  |  **Created:** 2026-01-08

**背景：** World Monitor 是一個開源態勢感知平台，將即時新聞、地緣政治事件和基礎設施狀態聚合到單一儀表板中。以 TypeScript 建構，提供多種專業變體（通用、科技導向、金融導向），透過網頁存取。自 2026 年 1 月發布以來已成長至近 35,000 顆星。

**解決的問題：** 掌握全球事件動態需要監控數十個新聞來源、社交媒體訊息源和基礎設施狀態頁面。World Monitor 將這些整合到單一 AI 驅動的介面中，即時過濾、分類並呈現相關資訊。

**為何又一個？** World Monitor 透過多變體方式（針對通用、科技和金融受眾的獨立儀表板）和 AGPL 授權（確保衍生作品保持開源）實現差異化。本週四天的上榜紀錄顯示這是穩定的自然增長，而非單次病毒式爆發。

---

## 9. [airi](https://github.com/moeru-ai/airi)
> 自託管、你擁有的 Grok 夥伴，一個承載 waifu 靈魂的容器，將數位生命帶入我們的世界。支援即時語音聊天、Minecraft、Factorio 遊戲。

**Language:** TypeScript  |  **Stars:** 31704  |  **Forks:** 3103  |  **Best Score:** 9216  |  **Best Rank:** #2  |  **Days on chart:** 5/7  |  **Created:** 2024-12-01

**背景：** Project AIRI 由 moeru-ai 開發，是一個自託管的 AI 夥伴平台，旨在重現 Neuro-sama 的體驗——一個能夠即時語音對話、玩遊戲（Minecraft、Factorio）並維持一致個性的 AI 虛擬角色。支援網頁、macOS 和 Windows，具備七種語言翻譯。自 2024 年 12 月以來已累積超過 31,000 顆星。

**解決的問題：** 建構一個能夠即時語音對話、玩遊戲並在各會話間維持一致個性的互動 AI 夥伴，需要整合語音合成、遊戲 API、記憶系統和角色建模。AIRI 將所有這些打包在單一自託管應用程式中。

**為何又一個？** AIRI 是少數嘗試在使用者自有硬體上匹配商業 AI 夥伴平台能力的開源專案之一。其遊戲遊玩能力（Minecraft、Factorio）遠超簡單的聊天機器人互動，本週五天的上榜紀錄表明社群的持續參與。

---

## 10. [shannon](https://github.com/KeygraphHQ/shannon)
> Shannon Lite 是一個完全自主的 AI 滲透測試工具，用於網頁應用程式和 API。在無提示、原始碼感知的 XBOW 基準測試變體中達到 96.15%（100/104 個漏洞利用）。

**Language:** TypeScript  |  **Stars:** 32869  |  **Forks:** 3275  |  **Best Score:** 7734  |  **Best Rank:** #3  |  **Days on chart:** 3/7  |  **Created:** 2025-09-27

**背景：** Shannon 是 Keygraph 開發的自主白盒 AI 滲透測試工具。它分析原始碼以識別攻擊向量，然後執行真實的漏洞利用以在漏洞進入生產環境之前加以證明。該專案在原始碼感知的 XBOW 基準測試變體中得分 96.15%，展示了對已知網頁應用程式漏洞利用類別的近乎完全覆蓋。

**解決的問題：** 手動滲透測試昂貴、緩慢且需要專業知識。Shannon 自動化了整個工作流程——從原始碼分析到攻擊向量識別再到實際漏洞利用執行——產出附帶概念驗證漏洞利用的可操作漏洞報告。

**為何又一個？** Shannon 的白盒方法（分析原始碼而非僅探測端點）比黑盒掃描工具提供更深入的覆蓋。其在 XBOW 上 96% 的基準分數證明 AI 驅動的滲透測試可以接近熟練人工測試者的徹底程度，且最近新增的透過 AWS Bedrock 和 Google Vertex AI 對 Claude 模型的支援擴大了其模型相容性。

---

## 11. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> 練習造就完美的 Claude

**Language:** HTML  |  **Stars:** 12935  |  **Forks:** 1213  |  **Best Score:** 7543  |  **Best Rank:** #5  |  **Days on chart:** 4/7  |  **Created:** 2025-10-31

**背景：** claude-code-best-practice 是由 shanraisshan 維護的社群資源庫，記錄有效使用 Claude Code 的最佳實踐。它涵蓋 Command-Agent-Skill 調度工作流程、實作模式，以及從社群收集的實用技巧。自 2025 年 10 月以來已成長至近 13,000 顆星。

**解決的問題：** Claude Code 是一個強大的工具，但要從中獲取最大價值需要理解其調度模型、技能系統和有效的提示模式。此資源庫將社群知識整合為可操作的指南，並附有具體的實作範例。

**為何又一個？** 不同於通用的提示工程指南，此資源庫專門針對 Claude Code 的架構——命令、代理和技能——量身打造，並在文件旁提供已實作的範例。其四天的上榜紀錄反映了社群對 Claude Code 優化知識的持續需求。

---

## 12. [visual-explainer](https://github.com/nicobailon/visual-explainer)
> 代理技能，可生成豐富的 HTML 頁面或投影片，用於圖表、差異審查、計畫審核、資料表格和專案回顧

**Language:** HTML  |  **Stars:** 5918  |  **Forks:** 405  |  **Best Score:** 7314  |  **Best Rank:** #3  |  **Days on chart:** 2/7  |  **Created:** 2026-02-16

**背景：** visual-explainer 是一個代理技能，能將終端機輸出轉換為精美的互動式 HTML 頁面。它不再使用 ASCII 圖表和等寬表格，而是生成具有真正排版、明暗主題和可互動 Mermaid 圖表（含縮放和平移功能）的自包含 HTML。它可作為 Claude Code 和其他代理平台的插件安裝。

**解決的問題：** 編程代理預設使用 ASCII 繪製圖表和管線分隔表格呈現資料，兩者在超過簡單複雜度後都變得難以閱讀。visual-explainer 攔截這些輸出並將其渲染為帶有 Mermaid 圖表、精美表格和響應式佈局的正式 HTML，在瀏覽器中開啟。

**為何又一個？** 大多數代理輸出格式化工具專注於 Markdown 渲染。visual-explainer 更進一步，生成具有互動功能（可縮放的圖表、可排序的表格）的完全自包含 HTML 頁面，無需建構步驟或瀏覽器以外的外部依賴。

---

## 13. [openclaw](https://github.com/openclaw/openclaw)
> 你的個人 AI 助手。任何作業系統。任何平台。龍蝦之道。

**Language:** TypeScript  |  **Stars:** 289626  |  **Forks:** 54924  |  **Best Score:** 7303  |  **Best Rank:** #3  |  **Days on chart:** 7/7  |  **Created:** 2025-11-24

**背景：** OpenClaw 是主導地位的開源個人 AI 助手平台，擁有近 290,000 顆星，使其成為 GitHub 上星數最高的儲存庫之一。它可在幾乎所有平台上運行，並整合 WhatsApp、Telegram、Slack、Discord、Google Chat、Signal、iMessage、IRC、Microsoft Teams、Matrix 等眾多即時通訊服務。本週全部七天上榜凸顯了其持續的社群動能。

**解決的問題：** 使用者希望擁有一個可跨所有通訊管道——即時通訊、電子郵件、語音——存取的單一 AI 助手，而無需將資料交給集中式服務。OpenClaw 作為使用者完全控制的自託管應用程式提供了這一功能。

**為何又一個？** OpenClaw 的主導地位來自其廣泛的平台支援和蓬勃的技能與插件生態系統。七天的上榜紀錄和龐大的星數使其成為個人 AI 助手生態系統的引力中心，本排行榜上的許多其他專案明確為其建構或與其整合。

---

## 14. [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted)
> 可在自己伺服器上託管的自由軟體網路服務和網頁應用程式清單

**Language:** N/A  |  **Stars:** 278701  |  **Forks:** 12754  |  **Best Score:** 7228  |  **Best Rank:** #6  |  **Days on chart:** 2/7  |  **Created:** 2015-06-01

**背景：** awesome-selfhosted 是經典的自由開源自託管軟體精選清單，涵蓋從分析到 Wiki 等類別。自 2015 年開始，透過持續的社群策劃 Pull Request 已成長至近 279,000 顆星。當自託管興趣高漲時，它會定期重新出現在趨勢排行榜上。

**解決的問題：** 尋找高品質的 SaaS 產品自託管替代方案需要搜尋數十個來源。此資源庫將它們整合到一個單一的、分類的、由社群審核的清單中，具有一致的元資料（授權、語言、最後更新）。

**為何又一個？** 它是同類資源中最原始且最全面的。其定期上榜與更廣泛的資料主權和隱私意識趨勢相關，而 AI 助手浪潮更加速了這一趨勢。

---

## 15. [OpenSandbox](https://github.com/alibaba/OpenSandbox)
> OpenSandbox 是一個通用的 AI 應用程式沙箱平台，提供多語言 SDK、統一的沙箱 API，以及 Docker/Kubernetes 執行環境。

**Language:** Python  |  **Stars:** 7180  |  **Forks:** 526  |  **Best Score:** 7188  |  **Best Rank:** #2  |  **Days on chart:** 3/7  |  **Created:** 2025-12-17

**背景：** OpenSandbox 是阿里巴巴的開源沙箱平台，設計為 AI 應用程式提供隔離的執行環境。它提供多語言 SDK 和統一 API，可跨 Docker 和 Kubernetes 執行環境運作。目標使用場景包括編程代理、GUI 代理、代理評估、AI 程式碼執行和強化學習訓練。

**解決的問題：** 執行程式碼的 AI 代理需要安全、隔離的環境，以防止對主機系統造成意外的副作用。OpenSandbox 提供一致的 API 層，用於建立、管理和銷毀沙箱環境，無論底層執行環境是 Docker 或 Kubernetes。

**為何又一個？** 阿里巴巴為沙箱問題帶來了企業規模的經驗，支援更簡單沙箱方案未涵蓋的場景（GUI 代理、強化學習訓練）。其多語言 SDK 方法意味著團隊不會被鎖定在單一程式語言上建構代理基礎設施。

---

## 16. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> 精選的 OpenClaw 技能合集。從官方 OpenClaw Skills Registry 篩選和分類的 5,400 多個技能。

**Language:** N/A  |  **Stars:** 33181  |  **Forks:** 3144  |  **Best Score:** 6619  |  **Best Rank:** #3  |  **Days on chart:** 7/7  |  **Created:** 2026-01-25

**背景：** 由 VoltAgent 維護，此資源庫收錄了超過 5,400 個社群建構的 OpenClaw 技能，按類別組織。它從官方 OpenClaw Skills Registry 取得資料，並進行篩選和分類，使不斷成長的生態系統易於瀏覽。其七天的上榜紀錄與 OpenClaw 本身一致的能見度相匹配。

**解決的問題：** OpenClaw 技能生態系統已成長到相當龐大的規模，發現相關技能需要直接搜尋登錄檔或事先知道要找什麼。此精選清單按類別組織瀏覽，並附帶品質篩選。

**為何又一個？** 它作為 OpenClaw 技能生態系統的事實上目錄，持續更新以追蹤登錄檔的快速成長。其持續的上榜紀錄表明新使用者在採用 OpenClaw 時繼續發現它。

---

## 17. [Perplexica](https://github.com/ItzCrazyKns/Perplexica)
> Perplexica 是一個 AI 驅動的答案引擎。

**Language:** TypeScript  |  **Stars:** 32359  |  **Forks:** 3474  |  **Best Score:** 6298  |  **Best Rank:** #4  |  **Days on chart:** 2/7  |  **Created:** 2024-04-09

**背景：** Perplexica（現在也稱為 Vane）是一個注重隱私的 AI 答案引擎，完全在使用者自己的硬體上運行。它結合網路搜尋與本地及雲端 LLM 支援（Ollama、OpenAI、Claude、Groq），在保持搜尋隱私的同時提供帶有來源引用的答案。自 2024 年 4 月以來已累積超過 32,000 顆星。

**解決的問題：** 商業 AI 搜尋引擎如 Perplexity 在其伺服器上處理查詢，使用者無法控制資料處理。Perplexica 提供等效功能——結合 LLM 推理和來源引用的網路搜尋——同時完全在本地運行。

**為何又一個？** Perplexica 的多供應商方式（同時支援透過 Ollama 的本地模型和雲端供應商）讓使用者可以靈活選擇隱私/能力的權衡。其基於 Docker 的部署使非技術使用者也能輕鬆使用私密 AI 搜尋。

---

## 18. [canopy](https://github.com/canopy-network/canopy)
> Canopy Network 協定的官方 Go 實作

**Language:** Go  |  **Stars:** 4262  |  **Forks:** 9293  |  **Best Score:** 6246  |  **Best Rank:** #5  |  **Days on chart:** 3/7  |  **Created:** 2024-10-30

**背景：** Canopy 是 Canopy Network Protocol 的官方 Go 實作，一個建立在遞迴架構上的區塊鏈平台，各鏈彼此引導走向獨立。目前處於 alphanet 狀態，它提供了建構區塊鏈的框架，並運營啟動遞迴循環的種子鏈。

**解決的問題：** 啟動新的區塊鏈網路通常需要從零開始引導安全性、驗證者集合和經濟激勵。Canopy 的遞迴架構讓新鏈可以從現有鏈繼承安全性和功能，降低了冷啟動問題。

**為何又一個？** 遞迴鏈引導概念在架構上與現有區塊鏈框架截然不同。其異常高的 fork 對星數比（9,293 個 fork 對 4,262 顆星）表明開發者對程式碼庫進行了大量實驗。

---

## 19. [superpowers](https://github.com/obra/superpowers)
> 一個有效的代理技能框架與軟體開發方法論。

**Language:** Shell  |  **Stars:** 75000  |  **Forks:** 5793  |  **Best Score:** 6075  |  **Best Rank:** #7  |  **Days on chart:** 7/7  |  **Created:** 2025-10-09

**背景：** Superpowers 是一個完整的編程代理軟體開發工作流程，強制執行紀律性流程：規格擷取、設計審查、實作計畫，以及透過子代理驅動的開發與 TDD。由 obra 創建，已達到 75,000 顆星，且在本週全部七天上榜。當代理偵測到建構任務時，框架會自動觸發。

**解決的問題：** 放任自行運作的編程代理往往會直接跳入寫程式碼，而不理解需求、建立計畫或測試。Superpowers 強制施加結構化方法論——規格、計畫、實作、審查——使代理能在無人干預下持續生產性工作數小時。

**為何又一個？** Superpowers 作為一個元框架運作，位於代理之上而非內部。它不取代代理的能力，而是增加流程防護機制（YAGNI、DRY、TDD），防止無人監督代理會話中常見的偏移和退化。其 75,000 顆星數使其成為最受歡迎的代理工作流程工具之一。

---

## 20. [awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
> OpenClaw 使用案例的社群合集，讓生活更輕鬆。

**Language:** N/A  |  **Stars:** 22126  |  **Forks:** 1817  |  **Best Score:** 6069  |  **Best Rank:** #3  |  **Days on chart:** 7/7  |  **Created:** 2026-02-08

**背景：** 此資源庫由 hesamsheikh 整理，收集 OpenClaw 的真實生活使用案例，專注的不是技能或技術能力，而是改善日常生活的實際應用。它記錄了 36 多個使用案例，並附有關於第三方依賴的安全警告。該專案僅一個月內已成長至超過 22,000 顆星。

**解決的問題：** OpenClaw 採用的瓶頸不是技能的可用性，而是想像力差距——使用者難以設想 AI 助手如何改善他們的特定工作流程。此合集透過具體的、經社群驗證的範例彌合了這一差距。

**為何又一個？** 不同於列出 OpenClaw 技術上能做什麼的技能目錄，此資源庫專注於真實使用者為何及如何在日常生活中使用它。其七天的上榜紀錄和快速的星數增長表明此類靈感驅動的文件具有強勁的產品-市場契合度。

---

## 21. [CoPaw](https://github.com/agentscope-ai/CoPaw)
> 你的個人 AI 助手；易於安裝，部署在自己的機器或雲端上；支援多種聊天應用程式，具有易於擴展的功能。

**Language:** Python  |  **Stars:** 9613  |  **Forks:** 1072  |  **Best Score:** 5787  |  **Best Rank:** #5  |  **Days on chart:** 3/7  |  **Created:** 2026-02-24

**背景：** CoPaw 是由 AgentScope 團隊（阿里巴巴）開發的基於 Python 的個人 AI 助手，設計用於輕鬆部署在個人機器或雲端基礎設施上。它支援多種聊天應用程式並提供可擴展的功能系統。於 2026 年 2 月底發布，迅速累積近 10,000 顆星。

**解決的問題：** 設置一個功能完善的個人 AI 助手通常涉及複雜的依賴管理、服務配置和特定平台的整合。CoPaw 透過 pip 安裝部署和內建的多訊息平台支援簡化了這一過程。

**為何又一個？** CoPaw 透過其 Python 原生方法（相對於 TypeScript 主導的替代方案如 OpenClaw）和 AgentScope 團隊的支持（帶來企業 AI 經驗）實現差異化。它面向偏好 Python 工具且希望與更廣泛 AgentScope 生態系統緊密整合的使用者。

---

## 22. [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
> 從零重建你喜愛的技術，精通程式設計。

**Language:** Markdown  |  **Stars:** 473392  |  **Forks:** 44374  |  **Best Score:** 5636  |  **Best Rank:** #5  |  **Days on chart:** 2/7  |  **Created:** 2018-05-09

**背景：** build-your-own-x 彙集了從零開始重建熱門技術的逐步指南——從 3D 渲染器到作業系統再到神經網路。擁有超過 473,000 顆星，它是 GitHub 上星數最高的儲存庫之一。隨著新一波開發者發現它，它會定期登上趨勢榜。

**解決的問題：** 理解複雜系統的內部運作需要自己動手建構，但在軟體工程的完整範圍中找到高品質的「從零建構 X」教學非常耗時。此資源庫將它們全部索引起來。

**為何又一個？** 它是同類中最權威的合集，涵蓋的技術類別超過任何競爭資源。其持久的受歡迎程度源於它所體現的費曼原則：「我無法創造的東西，我就不理解。」

---

## 23. [openfang](https://github.com/RightNow-AI/openfang)
> 開源代理作業系統

**Language:** Rust  |  **Stars:** 12521  |  **Forks:** 1385  |  **Best Score:** 5379  |  **Best Rank:** #4  |  **Days on chart:** 2/7  |  **Created:** 2026-02-24

**背景：** OpenFang 是 RightNow AI 以 Rust 建構的「代理作業系統」，包含 137,000 行程式碼，分佈在 14 個 crate 中，擁有超過 1,767 個測試且零 clippy 警告。目前為 v0.3.30（安全強化版本），編譯為單一二進位檔，提供運行自主代理的基礎設施。

**解決的問題：** 建構生產級代理系統需要處理進程隔離、安全性、排程和資源管理——本質上是應用於 AI 代理的作業系統層級問題。OpenFang 將這些能力打包成一個經過測試、強化的執行環境。

**為何又一個？** OpenFang 的工程嚴謹度（1,767 多個測試、零警告、14 crate 架構）使其有別於原型品質的代理框架。其 Rust 實作提供了對長時間運行自主代理工作負載至關重要的記憶體安全和效能保證。

---

## 24. [prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)
> Anthropic 的互動式提示工程教學

**Language:** Jupyter Notebook  |  **Stars:** 33102  |  **Forks:** 3371  |  **Best Score:** 5176  |  **Best Rank:** #7  |  **Days on chart:** 3/7  |  **Created:** 2024-04-02

**背景：** 這是 Anthropic 官方的 Claude 提示工程互動課程，結構為九個章節，附有練習、實驗遊樂場和答案解析。它教授解決常見提示失敗模式的 80/20 技巧。該課程已達到超過 33,000 顆星。

**解決的問題：** 有效的提示工程需要理解模型的優勢和失敗模式。此課程提供結構化的實作練習，附帶即時反饋，從基本提示結構到進階技巧循序漸進。

**為何又一個？** 作為 Anthropic 的官方教學，它提供關於 Claude 特定能力和限制的權威指導。本週三天的上榜紀錄表明新的 Claude 使用者持續發現它。

---

## 25. [How-To-Secure-A-Linux-Server](https://github.com/imthenachoman/How-To-Secure-A-Linux-Server)
> 一份持續演進的 Linux 伺服器安全加固指南。

**Language:** N/A  |  **Stars:** 25751  |  **Forks:** 1687  |  **Best Score:** 4972  |  **Best Rank:** #9  |  **Days on chart:** 2/7  |  **Created:** 2019-02-09

**背景：** 這是一份全面的、由社群維護的 Linux 伺服器安全加固指南，涵蓋 SSH 加固、防火牆配置、入侵偵測等。始於 2019 年，已成長至超過 25,000 顆星，並定期更新新的安全實踐。本週的出現可能與 AI 助手趨勢帶動的自託管活動增加有關。

**解決的問題：** 保護 Linux 伺服器需要分散在數十個 man page、部落格文章和供應商文件中的知識。此指南將必要步驟整合成一個單一的結構化教學，並解釋每項措施的重要性。

**為何又一個？** 它仍然是最完整的單一文件伺服器加固指南之一。其定期的上榜紀錄往往與自託管興趣的高峰相關，而目前的自託管 AI 工具浪潮正在推動這一趨勢。

---

## 26. [agent-browser](https://github.com/vercel-labs/agent-browser)
> 為 AI 代理設計的瀏覽器自動化 CLI

**Language:** Rust  |  **Stars:** 20352  |  **Forks:** 1189  |  **Best Score:** 4758  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2026-01-11

**背景：** agent-browser 是 Vercel Labs 以 Rust 撰寫的無頭瀏覽器自動化 CLI，附帶 Node.js 後備方案。它透過命令列介面為 AI 代理提供直接的瀏覽器控制，全域安裝時解析開銷低於亞毫秒級。可透過 npm、Homebrew 和原始碼建構取得。

**解決的問題：** AI 代理經常需要與網頁互動——填寫表單、點擊按鈕、擷取內容——但現有的瀏覽器自動化工具（Playwright、Puppeteer）是為撰寫測試腳本的人類開發者設計的，而非為發出指令的代理。agent-browser 提供了針對代理工具呼叫模式最佳化的 CLI 原生介面。

**為何又一個？** Rust 實作提供了純 JavaScript 方案無法匹敵的效能，而 CLI 優先的設計意味著代理可以將其作為工具使用，無需匯入函式庫或程式化管理瀏覽器上下文。Vercel 的支持表明了對代理工具生態系統的承諾。

---

## 27. [vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands)
> 基於 easemate IDE 和 JetBrains Islands 主題的 VSCode 主題

**Language:** PowerShell  |  **Stars:** 5123  |  **Forks:** 151  |  **Best Score:** 4724  |  **Best Rank:** #10  |  **Days on chart:** 2/7  |  **Created:** 2026-02-14

**背景：** Islands Dark 是一個受 easemate IDE 啟發的 VS Code 色彩主題，具備懸浮玻璃面板、圓角、平滑動畫和深色畫布（#131217）。由 bwya77 於 2026 年 2 月中創建，兩週內累積超過 5,000 顆星，顯示對這種視覺美學的強烈需求。

**解決的問題：** 欣賞 easemate IDE 視覺設計但使用 VS Code 的開發者，過去沒有忠實移植其獨特玻璃面板美學的版本。此主題透過精心處理玻璃效果邊框、藥丸形捲軸和懸停感知的 UI 元素彌合了這一差距。

**為何又一個？** easemate 啟發的設計語言——懸浮面板、方向性光線模擬、動畫過渡——遠超典型的換色主題。其快速的採用速度表明該主題滿足了較簡單暗色主題未能滿足的真正美學偏好。

---

## 28. [public-apis](https://github.com/public-apis/public-apis)
> 免費 API 的集合清單

**Language:** Python  |  **Stars:** 405531  |  **Forks:** 43795  |  **Best Score:** 4697  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2016-03-20

**背景：** public-apis 是 GitHub 上最大的免費 API 精選目錄，擁有超過 405,000 顆星。它涵蓋數十個領域的 API——天氣、金融、娛樂、政府資料等——由社群貢獻者維護，並獲得 APILayer 的支持。

**解決的問題：** 為副專案和原型尋找免費、可用的 API 需要搜尋供應商文件、開發者論壇和過時的部落格文章。此資源庫提供了一個單一的、分類的索引，格式一致。

**為何又一個？** 它是此領域的經典資源，自 2016 年以來持續維護。本週的上榜反映了其對建構新專案的開發者永恆的實用價值。

---

## 29. [claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)
> 一套即用型代理技能，用於研究、科學、工程、分析、金融和寫作。

**Language:** Python  |  **Stars:** 14105  |  **Forks:** 1530  |  **Best Score:** 4566  |  **Best Rank:** #10  |  **Days on chart:** 4/7  |  **Created:** 2025-10-19

**背景：** Claude Scientific Skills 是由 K-Dense AI 建立的 170 多個即用型科學和研究技能合集，涵蓋生物學、化學、醫學、基因體學、分子動力學、地理空間科學、時間序列預測、經濟資料等。這些技能遵循開放的 Agent Skills 標準，適用於 Cursor、Claude Code 和 Codex。

**解決的問題：** 希望使用 AI 代理處理複雜多步驟工作流程的科學家和研究人員，需要編碼了正確方法論的特定領域技能——而非通用的程式碼生成。此合集提供了理解科學資料格式、統計方法和研究工作流程的技能。

**為何又一個？** 涵蓋的科學領域廣度（170 多個技能，跨越生物學、化學、醫學、金融和地理空間科學）遠超任何個別研究人員能夠自行建構的規模。四天的上榜紀錄反映了科學社群的持續採用。

---

## 30. [ANE](https://github.com/maderix/ANE)
> 透過逆向工程的私有 API 在 Apple Neural Engine 上訓練神經網路

**Language:** Objective-C  |  **Stars:** 5948  |  **Forks:** 855  |  **Best Score:** 4476  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2026-02-28

**背景：** ANE Training 是一個研究專案，展示了使用逆向工程的私有 API（_ANEClient 和 _ANECompiler）在 Apple Neural Engine 上進行反向傳播。Apple 透過 CoreML 將 ANE 限制為僅推論用途；此專案繞過了該限制，證明硬體上的訓練是可能的。作者明確將其定位為研究專案而非生產框架。

**解決的問題：** Apple Silicon 的 Neural Engine 是一個強大的加速器，但在模型訓練期間處於閒置狀態，因為 Apple 僅透過 CoreML 將其開放用於推論。此專案證明了硬體有能力處理訓練工作負載，表明這一限制是軟體強加的，而非硬體的固有限制。

**為何又一個？** 沒有其他公開專案展示過透過私有 API 介面直接進行 ANE 訓練。記錄 ANE 吞吐量、功耗和 SRAM 行為的基準測試提供了 ML 研究社群之前無法獲得的資料。

---

## 31. [ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)
> 12 堂課帶你開始建構 AI 代理

**Language:** Jupyter Notebook  |  **Stars:** 53475  |  **Forks:** 18576  |  **Best Score:** 4298  |  **Best Rank:** #14  |  **Days on chart:** 1/7  |  **Created:** 2024-11-28

**背景：** 這門由微軟撰寫的課程提供 12 堂結構化課程，從基礎概念到實際實作教授如何建構 AI 代理。它透過自動翻譯支援多種語言，自 2024 年 11 月以來已累積超過 53,000 顆星，使其成為 GitHub 上最受歡迎的 AI 教育資源之一。

**解決的問題：** AI 代理領域發展迅速，許多開發者缺乏從基礎到生產就緒模式循序漸進的結構化學習路徑。此課程透過實作練習和多語言支援提供了這樣的進程。

**為何又一個？** 微軟的支持提供了信譽和長期維護，透過 GitHub Actions 的多語言翻譯使其對全球受眾皆可存取。其高 fork 數（18,576）表明在課堂和學習小組中的積極使用。

---

## 32. [pinchtab](https://github.com/pinchtab/pinchtab)
> 高效能瀏覽器自動化橋接器和多實例調度器，具備進階隱匿注入和即時儀表板。

**Language:** Go  |  **Stars:** 5553  |  **Forks:** 377  |  **Best Score:** 4279  |  **Best Rank:** #7  |  **Days on chart:** 2/7  |  **Created:** 2026-02-15

**背景：** PinchTab 是以 Go 撰寫的獨立 HTTP 伺服器，讓 AI 代理直接控制 Chrome。它以 12MB 二進位檔附帶為 token 效率設計的 HTTP API 發布。伺服器在兩種角色中運作：完整控制面板伺服器和單實例橋接執行環境，提供針對代理消費最佳化的瀏覽器自動化功能。

**解決的問題：** AI 代理需要瀏覽器存取，但現有的自動化工具會產生冗長的回應，消耗過多的 token。PinchTab 的 HTTP API 專為 token 效率設計，回傳結構化的精簡回應，代理可以在不浪費上下文視窗空間的情況下處理。

**為何又一個？** 12MB 的 Go 二進位檔且零外部依賴，與拉入數百 MB 依賴的基於 Node.js 的瀏覽器自動化工具形成鮮明對比。其雙模式架構（伺服器對橋接）為多實例調度和單一瀏覽器控制提供了靈活性。

---

## 33. [nullclaw](https://github.com/nullclaw/nullclaw)
> 以 Zig 撰寫的最快、最小且完全自主的 AI 助手基礎設施

**Language:** Zig  |  **Stars:** 6052  |  **Forks:** 719  |  **Best Score:** 4084  |  **Best Rank:** #9  |  **Days on chart:** 1/7  |  **Created:** 2026-02-16

**背景：** NullClaw 是 AI 助手基礎設施領域的 Zig 方案，編譯為 678 KB 的靜態二進位檔，啟動時間低於 2 毫秒，運行時約 1 MB 峰值 RSS。它支援 23 多個供應商、18 個訊息管道，並通過 3,230 多個測試。該專案針對連 Rust 替代方案都被認為過於沉重的極端資源受限環境。

**解決的問題：** 即使最小的基於 Rust 的助手二進位檔也有個位數 MB 級別。NullClaw 將界限推至亞 MB 領域，使部署在 5 美元的 ARM 板卡、微控制器和其他深度受限環境上成為可能。

**為何又一個？** Zig 的 comptime 元程式設計和零開銷抽象，使其能實現 Rust 標準函式庫無法匹敵的二進位大小和啟動時間。在 678 KB 下，NullClaw 大約是其最接近 Rust 競爭者的十分之一大小，使其在幾 MB 都很重要的環境中具有可行性。

---

## 34. [generative-ai](https://github.com/GoogleCloudPlatform/generative-ai)
> Google Cloud 生成式 AI 的範例程式碼和 notebook，使用 Vertex AI 上的 Gemini

**Language:** Jupyter Notebook  |  **Stars:** 14626  |  **Forks:** 3912  |  **Best Score:** 4046  |  **Best Rank:** #4  |  **Days on chart:** 1/7  |  **Created:** 2023-05-05

**背景：** 這是 Google Cloud 官方的範例程式碼和 Jupyter notebook 儲存庫，用於在 Vertex AI 上使用生成式 AI 服務。它涵蓋 Gemini 模型（包括最近發布的 Gemini 3.1 Pro）、搜尋、RAG 和代理架構。自 2023 年 5 月以來已累積超過 14,000 顆星。

**解決的問題：** 開始使用 Google Cloud 的生成式 AI 服務需要理解 Vertex AI 的 API 介面、認證和模型特定功能。此儲存庫提供了展示每項功能並附帶生產就緒模式的可運行 notebook。

**為何又一個？** 作為 Google Cloud 的官方資源，它是 Vertex AI 開發的經典參考。本週的上榜與 Gemini 3.1 Pro 的發布同步，該發布為儲存庫新增了新的 notebook。

---

## 35. [react-grab](https://github.com/aidenybai/react-grab)
> 直接從你的網站為編程代理選取上下文

**Language:** TypeScript  |  **Stars:** 6362  |  **Forks:** 292  |  **Best Score:** 3984  |  **Best Rank:** #9  |  **Days on chart:** 1/7  |  **Created:** 2025-10-17

**背景：** React Grab 是一個開發者工具，讓你指向 React 網站上的任何元素，按 Cmd+C 即可將檔案名稱、React 元件名稱和 HTML 原始碼直接複製到剪貼簿。這些上下文可以貼上到 Cursor、Claude Code 或 Copilot 等編程代理中，使其速度和準確度提高最多 3 倍。

**解決的問題：** 使用編程代理處理前端程式碼時，開發者浪費時間手動辨識哪些檔案和元件對應他們想修改的 UI 元素。React Grab 用單一鍵盤快捷鍵自動化了這一上下文收集過程。

**為何又一個？** React Grab 在框架層級運作（掛鉤到 React 的元件樹）而非僅在 DOM 層級，為代理提供包含元件名稱和原始檔路徑的更豐富上下文。其 MCP 伺服器整合允許直接連接到支援的代理。

---

## 36. [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)
> 建立在 Qwen>=3.0 之上的代理框架和應用程式，支援函式呼叫、MCP、程式碼直譯器、RAG、Chrome 擴充功能等。

**Language:** Python  |  **Stars:** 15235  |  **Forks:** 1462  |  **Best Score:** 3866  |  **Best Rank:** #10  |  **Days on chart:** 2/7  |  **Created:** 2023-09-22

**背景：** Qwen-Agent 是阿里巴巴 Qwen 語言模型系列（3.0 以上版本）的官方代理框架。它提供函式呼叫、MCP 支援、程式碼直譯器、RAG 功能和 Chrome 擴充功能。該專案已成長至超過 15,000 顆星，是在 Qwen 模型之上建構代理應用程式的主要方式。

**解決的問題：** 在 Qwen 模型上建構代理應用程式需要一個理解 Qwen 特定函式呼叫格式、工具使用模式和多輪對話處理的框架。Qwen-Agent 原生提供了這些功能。

**為何又一個？** 模型特定的代理框架可以利用通用框架無法利用的能力和格式。Qwen-Agent 與 Qwen 的架構緊密耦合，提供通用框架僅作為附帶功能處理的最佳化工具使用和對話管理。

---

## 37. [MiroFish](https://github.com/666ghj/MiroFish)
> 一個簡單且通用的群體智慧引擎，可預測任何事物。

**Language:** Python  |  **Stars:** 10216  |  **Forks:** 1069  |  **Best Score:** 3821  |  **Best Rank:** #6  |  **Days on chart:** 2/7  |  **Created:** 2025-11-26

**背景：** MiroFish 是盛大開發的群體智慧預測引擎，設計用於將多個預測來源聚合為共識預測。它將群體智慧原理——結合許多簡單預測器形成湧現的集體智慧——應用於跨任意領域的預測生成。

**解決的問題：** 單一預測模型具有特定領域的偏差和盲點。MiroFish 將多個預測器作為群體進行調度，使用集體智慧演算法產生比任何單一模型更穩健的預測。

**為何又一個？** 大多數預測框架專注於提高單一模型的準確性。MiroFish 採取正交方法，將聚合機制本身視為核心創新，以領域無關的方式將群體智慧理論應用於模型集成。

---

## 38. [llmfit](https://github.com/AlexsJones/llmfit)
> 數百個模型和供應商。一個指令找到適合你硬體的模型。

**Language:** Rust  |  **Stars:** 13738  |  **Forks:** 760  |  **Best Score:** 3723  |  **Best Rank:** #17  |  **Days on chart:** 1/7  |  **Created:** 2026-02-15

**背景：** llmfit 是一個 Rust 終端工具，將 LLM 模型適配到系統的 RAM、CPU 和 GPU 能力。它偵測硬體，從品質、速度、適配度和上下文四個維度評分每個模型，並推薦哪些模型能在本地良好運行。支援多 GPU 配置、MoE 架構、動態量化選擇和本地執行環境供應商（Ollama、llama.cpp、MLX）。

**解決的問題：** 選擇在本地運行哪個 LLM 需要交叉參照模型需求與硬體規格，然後在心裡調整量化選項和執行環境開銷。llmfit 用一個指令和互動式 TUI 自動化了這一過程。

**為何又一個？** 現有的模型推薦工具要麼是基於網頁的（需要分享資料），要麼是手動查找表。llmfit 在本地偵測硬體，同時從四個維度評分模型，並提供互動式探索——全部來自一個快速的 Rust 二進位檔。

---

## 39. [cs-video-courses](https://github.com/Developer-Y/cs-video-courses)
> 附有影片講座的電腦科學課程清單。

**Language:** N/A  |  **Stars:** 76781  |  **Forks:** 10386  |  **Best Score:** 3528  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2016-10-21

**背景：** cs-video-courses 是一個由社群維護的免費電腦科學課程索引，包含影片講座，涵蓋從入門課程到分散式系統、機器學習和電腦圖學等進階主題的完整 CS 課程體系。由 Developer-Y 於 2016 年開始，已成長至超過 76,000 顆星。

**解決的問題：** 高品質的 CS 講座內容散布在大學網站、YouTube 頻道和 MOOC 平台上。此資源庫將它們整合到一個按主題組織的單一可瀏覽索引中。

**為何又一個？** 它仍然是最全面的 CS 影片課程單一儲存庫索引，並透過社群貢獻持續更新。其定期的上榜紀錄反映了自學式 CS 教育興趣的持續浪潮。

---

## 40. [waoowaoo](https://github.com/waoowaooAI/waoowaoo)
> 業界首個專業 AI 代理平台，用於可控的影視製作。

**Language:** TypeScript  |  **Stars:** 8285  |  **Forks:** 1700  |  **Best Score:** 3496  |  **Best Rank:** #17  |  **Days on chart:** 1/7  |  **Created:** 2026-01-22

**背景：** waoowaoo 是一個 AI 驅動的影視製作工作室，自動化從小說文字到成品影片的管線。它將腳本解析為分鏡、生成一致的角色和場景圖像、合成多角色語音演出，並將輸出組裝成完整影片。目前由一位獨立開發者以 beta 版發布。

**解決的問題：** 從書面故事製作短影片內容需要協調多個 AI 工具——圖像生成、語音合成、影片合成——按照特定的管線。waoowaoo 將這些整合到一個具有 Docker 部署的單一工作流程中。

**為何又一個？** 大多數 AI 影片工具專注於管線的個別階段（文字到圖像、文字到語音）。waoowaoo 值得注意的是提供了從原始文字到成品影片的完整端到端管線，包括跨場景的角色一致性——這是單一階段工具無法解決的問題。

---

## 41. [yesitsme](https://github.com/0x0be/yesitsme)
> 透過姓名和電子郵件/電話尋找 Instagram 個人資料的簡單 OSINT 腳本

**Language:** Python  |  **Stars:** 2092  |  **Forks:** 220  |  **Best Score:** 3260  |  **Best Rank:** #13  |  **Days on chart:** 1/7  |  **Created:** 2021-12-23

**背景：** yesitsme 是一個 Python OSINT 工具，用於尋找與特定姓名、電子郵件和電話號碼關聯的 Instagram 帳號。它使用 dumpor.com 索引來檢索使用者名稱，並自動比較 toutatis 提供的模糊化聯絡資訊與使用者提供的資料。最初於 2021 年創建，它定期重新出現在趨勢排行榜上。

**解決的問題：** 當你只有一個人的姓名和部分聯絡資訊時，辨識哪個 Instagram 帳號屬於特定人員是一個常見的 OSINT 任務。yesitsme 自動化了搜尋、比較模糊化資料和匹配帳號的繁瑣過程。

**為何又一個？** 該工具的價值在於自動化比較模糊化資料（Instagram 只顯示電子郵件的首尾字母、部分電話號碼）——在跨多個潛在匹配項手動操作時非常耗時的步驟。

---

## 42. [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)
> Bash 就是你所需要的——一個極小的類 Claude Code 代理，從 0 到 1 建構

**Language:** TypeScript  |  **Stars:** 24497  |  **Forks:** 4467  |  **Best Score:** 3235  |  **Best Rank:** #7  |  **Days on chart:** 2/7  |  **Created:** 2025-06-29

**背景：** learn-claude-code 由 shareAI-lab 開發，是一個教育專案，教授如何在 12 個漸進式課程中從零建構一個類 Claude Code 的代理。每個課程新增一個機制——從基本的工具使用循環（「一個循環和 Bash 就是你所需要的」）到隔離的自主執行——每個課程配有一句指導格言。

**解決的問題：** 理解 AI 編程代理的內部運作很困難，因為生產代理將許多機制層疊在一起。此專案將代理分解為 12 個遞增步驟，每步只新增一個概念，使架構變得可學習。

**為何又一個？** 其教學方法——12 個課程，每個有一句格言和一個機制——比直接閱讀生產代理原始碼更有結構。該專案已吸引近 25,000 顆星和 4,467 個 fork，表明作為學習資源被廣泛使用。

---

## 43. [skills](https://github.com/openai/skills)
> Codex 的技能目錄

**Language:** Python  |  **Stars:** 13583  |  **Forks:** 762  |  **Best Score:** 3165  |  **Best Rank:** #13  |  **Days on chart:** 2/7  |  **Created:** 2025-11-25

**背景：** 這是 OpenAI 官方的 Codex 技能目錄，包含系統技能（自動安裝）、精選技能和實驗性技能。技能是由指令、腳本和資源組成的資料夾，Codex 在執行時發現和使用。此儲存庫實作了來自 agentskills.io 的開放 Agent Skills 標準。

**解決的問題：** 當 Codex 擁有針對專業任務的特定領域指導時表現更好。技能系統將這些指導打包為可攜帶、可發現的單元，可在團隊間安裝和共享。

**為何又一個？** 作為 OpenAI 的官方技能儲存庫，它定義了 Agent Skills 標準的參考實作。其精選/實驗分級提供了品質梯度，幫助使用者找到生產就緒的技能。

---

## 44. [rtk](https://github.com/rtk-ai/rtk)
> CLI 代理，可將常見開發指令的 LLM token 消耗降低 60-90%。單一 Rust 二進位檔，零依賴

**Language:** Rust  |  **Stars:** 5497  |  **Forks:** 294  |  **Best Score:** 3156  |  **Best Rank:** #15  |  **Days on chart:** 2/7  |  **Created:** 2026-01-22

**背景：** RTK（Rust Token Killer）是一個 CLI 代理，位於 AI 代理和系統指令之間，攔截冗長的輸出並在消耗 LLM 上下文視窗 token 之前進行壓縮。以 Rust 撰寫為零依賴的單一二進位檔，它將常見開發指令的 token 消耗降低 60-90%。

**解決的問題：** 當 AI 代理運行 shell 指令時，原始輸出通常包含數千個 token 的雜訊——ANSI 碼、重複的日誌行、建構元資料——消耗昂貴的上下文視窗空間卻不增加有用資訊。RTK 過濾並壓縮這些輸出。

**為何又一個？** Token 成本對代理使用者來說是一個具體、可衡量的痛點，RTK 在系統層級解決它，無需修改代理或正在運行的指令。其 Rust 實作為指令管線增加的延遲可以忽略不計。

---

## 45. [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
> 主要 AI 編程工具的完整系統提示詞、內部工具和 AI 模型

**Language:** N/A  |  **Stars:** 129730  |  **Forks:** 33055  |  **Best Score:** 3156  |  **Best Rank:** #14  |  **Days on chart:** 1/7  |  **Created:** 2025-03-05

**背景：** 此資源庫收集了主要 AI 編程工具使用的完整系統提示詞、內部工具定義和模型配置，包括 Claude Code、Cursor、Devin、Windsurf、Codex 和其他 25 個以上的工具。擁有近 130,000 顆星，它已成為理解商業 AI 工具配置方式的首選參考。

**解決的問題：** AI 編程工具在系統提示詞和內部工具配置方面大多不透明。此資源庫將這些資訊公開，讓開發者能夠理解、比較和學習不同工具如何建構其 AI 互動。

**為何又一個？** 它涵蓋的工具數量超過任何競爭資源（截至本週計算超過 28 個），並隨工具變更持續更新。其 130,000 顆星數反映了開發者對 AI 工具透明度的廣泛興趣。

---

## 46. [Scrapling](https://github.com/D4Vinci/Scrapling)
> 自適應網頁爬取框架，處理從單一請求到全面爬取的一切！

**Language:** Python  |  **Stars:** 26976  |  **Forks:** 1985  |  **Best Score:** 3147  |  **Best Rank:** #13  |  **Days on chart:** 1/7  |  **Created:** 2024-10-13

**背景：** Scrapling 是一個 Python 網頁爬取框架，能自適應網站變化，處理從簡單請求到全面爬取的一切。它提供多語言文件，自 2024 年 10 月以來已累積近 27,000 顆星。該專案最近新增了 MCP 整合以供 AI 代理使用。

**解決的問題：** 網頁爬取很脆弱，因為網站經常變更其 HTML 結構。Scrapling 自動適應這些變化，降低了使傳統爬蟲變得脆弱的維護負擔。

**為何又一個？** Scrapling 的自適應方法——自動調整以適應結構性變化——使其有別於靜態選擇器式爬蟲。其最近的 MCP 整合將其連接到 AI 代理生態系統，允許代理將爬取作為工具呼叫使用。

---

## 47. [MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2)
> 自動化線上賺錢流程。

**Language:** Python  |  **Stars:** 14944  |  **Forks:** 1502  |  **Best Score:** 3124  |  **Best Rank:** #18  |  **Days on chart:** 2/7  |  **Created:** 2024-02-12

**背景：** MoneyPrinterV2 是一個 Python 應用程式，自動化線上賺錢工作流程，主要透過自動化內容創建和發布。它是原始 MoneyPrinter 專案的完全重寫，具有更廣泛的功能集和更模組化的架構。需要 Python 3.12。

**解決的問題：** 為了變現而大規模創建和發布內容，需要跨多個平台和工具進行重複性的手動工作。MoneyPrinterV2 自動化了從內容生成到發布的管線。

**為何又一個？** V2 重寫解決了原始專案的限制，採用模組化架構支援更廣泛的變現策略和內容類型。

---

## 48. [Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI)
> 為你的 OpenClaw 打造的像素辦公室：將看不見的工作狀態變成溫馨小空間，配有角色、每日記事和訪客代理。

**Language:** HTML  |  **Stars:** 3785  |  **Forks:** 421  |  **Best Score:** 3118  |  **Best Rank:** #20  |  **Days on chart:** 2/7  |  **Created:** 2026-02-26

**背景：** Star Office UI 是一個像素風格儀表板，即時視覺化 AI 助手的工作狀態。它透過虛擬辦公室場景中的動畫像素角色顯示哪些代理正在活動、正在做什麼以及其最近的歷史。它與 OpenClaw 深度整合，支援中文、英文和日文。

**解決的問題：** AI 助手在背景中隱形工作，使人難以得知其當前狀態、工作量或最近活動。Star Office UI 透過迷人的像素藝術視覺化讓代理工作狀態變得具象。

**為何又一個？** 遊戲化角度——將代理狀態監控轉化為帶有角色、裝飾和 AI 生成房間自訂的像素辦公室模擬——是真正的新穎之處。它將一個平凡的監控任務變成使用者想要觀看的東西。

---

## 49. [agentscope](https://github.com/agentscope-ai/agentscope)
> 建構和運行你能看見、理解和信任的代理。

**Language:** Python  |  **Stars:** 17869  |  **Forks:** 1583  |  **Best Score:** 3074  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2024-01-12

**背景：** AgentScope 是阿里巴巴的 Python 框架，用於建構以透明度和信任為核心的多代理應用程式。它提供視覺化工具用於理解代理行為、除錯工作流程和監控執行。擁有近 18,000 顆星，它已成長為一個成熟的平台，具有學術支持（arXiv 論文）和活躍的路線圖。

**解決的問題：** 多代理系統因代理間互動不透明而極難除錯和理解。AgentScope 提供視覺化和監控工具，使代理行為變得可觀察和可信賴。

**為何又一個？** 對可觀察性的強調（「你能看見、理解和信任的代理」）使 AgentScope 有別於主要最佳化代理能力的框架。其視覺化優先的方法對於重視問責制的企業採用至關重要。

---

## 50. [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)
> 1000 多個代理技能的終極合集，適用於 Claude Code/Antigravity/Cursor。

**Language:** Python  |  **Stars:** 21559  |  **Forks:** 3753  |  **Best Score:** 3017  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2026-01-14

**背景：** 此資源庫收錄了 1,234 多個代理技能，相容 Claude Code、Gemini CLI、Codex CLI、Cursor、GitHub Copilot 等。它將自己定位為跨多個代理平台的通用技能合集，透過自動化登錄檔同步進行維護。

**解決的問題：** 代理技能散布在特定平台的儲存庫和登錄檔中。此合集將來自多個生態系統的技能聚合到一個單一的、跨平台的目錄中，具有一致的分類。

**為何又一個？** 跨平台相容性聲明（Claude Code、Gemini CLI、Codex、Cursor、Copilot 及其他）使其有別於特定平台的合集。自動同步機制使其與上游登錄檔保持同步。

---

## 51. [AFFiNE](https://github.com/toeverything/AFFiNE)
> 不只有 Notion 和 Miro。AFFiNE 是新一代知識庫，將規劃、整理和創作融為一體。

**Language:** TypeScript  |  **Stars:** 65229  |  **Forks:** 4554  |  **Best Score:** 3008  |  **Best Rank:** #12  |  **Days on chart:** 3/7  |  **Created:** 2022-07-31

**背景：** AFFiNE 是一個注重隱私、本地優先的 Notion 和 Miro 替代方案，將文件、白板和資料庫結合在單一應用程式中。擁有超過 65,000 顆星，它已確立為領先的開源知識管理工具之一。同時提供網頁應用和桌面應用。

**解決的問題：** Notion 和 Miro 需要雲端帳號並將資料儲存在其伺服器上。AFFiNE 提供等效功能——文件、看板、白板——並以本地優先的資料儲存和可選的同步。

**為何又一個？** AFFiNE 的本地優先架構意味著資料預設停留在使用者的裝置上，解決了阻止某些團隊使用雲端替代方案的隱私問題。其文件+白板+資料庫的組合方法減少了工具的分散。

---

## 52. [superset](https://github.com/superset-sh/superset)
> AI 代理時代的 IDE——在你的機器上運行一支 Claude Code、Codex 等的軍隊

**Language:** TypeScript  |  **Stars:** 6327  |  **Forks:** 403  |  **Best Score:** 2989  |  **Best Rank:** #18  |  **Days on chart:** 3/7  |  **Created:** 2025-10-21

**背景：** Superset 是一款終端應用程式，設計用於同時運行多個編程代理。它將每個代理任務隔離在自己的 git worktree 中，從一個介面監控所有代理，並提供內建的差異審查工具。目前適用於 macOS。

**解決的問題：** 在不同任務上運行多個編程代理需要在終端之間切換、手動管理分支隔離，並追蹤哪個代理需要關注。Superset 為平行代理調度提供了統一介面。

**為何又一個？** git worktree 隔離策略特別巧妙——每個代理在自己的 worktree 中工作，防止並行任務之間的合併衝突和交叉汙染。監控儀表板提供所有運行中代理的即時可見性。

---

## 53. [qmd](https://github.com/tobi/qmd)
> 為你的文件、知識庫、會議記錄等打造的迷你 CLI 搜尋引擎。

**Language:** TypeScript  |  **Stars:** 13649  |  **Forks:** 788  |  **Best Score:** 2933  |  **Best Rank:** #20  |  **Days on chart:** 1/7  |  **Created:** 2025-12-08

**背景：** QMD（Query Markup Documents）是一個在裝置上運行的個人文件搜尋引擎，結合 BM25 全文搜尋、向量語義搜尋和 LLM 重新排序——全部透過 node-llama-cpp 使用 GGUF 模型在本地運行。由 tobi 建立，自 2025 年 12 月以來已累積超過 13,000 顆星。

**解決的問題：** 在個人筆記、會議紀錄和文件中尋找資訊需要記住哪個檔案包含什麼。QMD 在本地索引一切，支援關鍵字和自然語言查詢，並透過層次化上下文改善 LLM 結果選擇。

**為何又一個？** QMD 的層次化上下文系統——集合層級的元資料向下流向子文件——是其關鍵差異化因素。這讓 LLM 在選擇匹配文件時能做出更好的上下文決策，作者強調這是關鍵創新。

---

## 54. [markitdown](https://github.com/microsoft/markitdown)
> 將檔案和 Office 文件轉換為 Markdown 的 Python 工具。

**Language:** Python  |  **Stars:** 90419  |  **Forks:** 5324  |  **Best Score:** 2926  |  **Best Rank:** #21  |  **Days on chart:** 2/7  |  **Created:** 2024-11-13

**背景：** MarkItDown 是微軟 AutoGen 團隊開發的 Python 實用工具，將各種檔案格式（Office 文件、PDF、圖像等）轉換為 Markdown 供 LLM 使用。擁有超過 90,000 顆星，它已成為 LLM 資料準備管線中的標準工具。現在提供 MCP 伺服器用於與 Claude Desktop 整合。

**解決的問題：** LLM 最適合處理文字輸入，但世界上大量資訊存在於二進位格式中——Word 文件、PowerPoint 投影片、PDF、圖像。MarkItDown 將這些轉換為 LLM 可以直接處理的乾淨 Markdown。

**為何又一個？** MarkItDown 廣泛的格式支援和 AutoGen 團隊的支持，使其相比臨時轉換腳本具有可靠性優勢。其 MCP 伺服器整合將其定位為 AI 代理工作流程的一等工具。

---

## 55. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code 是一款代理式編程工具，運行在你的終端機中，理解你的程式碼庫，幫助你更快地編寫程式碼。

**Language:** Shell  |  **Stars:** 75677  |  **Forks:** 6100  |  **Best Score:** 2924  |  **Best Rank:** #15  |  **Days on chart:** 4/7  |  **Created:** 2025-02-22

**背景：** Claude Code 是 Anthropic 官方的代理式編程助手，從終端機運作。它執行例行任務、解釋複雜程式碼、處理 git 工作流程，並可在 GitHub 上被標記進行程式碼審查。擁有超過 75,000 顆星，它是 AI 編程領域中最受歡迎的開發者工具之一。現在建議透過直接安裝器而非 npm 進行安裝。

**解決的問題：** 開發者在例行編程任務——撰寫樣板程式碼、理解不熟悉的程式碼、管理 git 操作——上花費大量時間。Claude Code 透過終端機中的自然語言指令自動化這些任務，具有完整的程式碼庫上下文。

**為何又一個？** 作為 Anthropic 的第一方編程代理，Claude Code 受益於直接的模型整合和快速的功能迭代。本週四天的上榜紀錄反映的是持續的日常使用，而非新鮮感驅動的興趣。

---

## 56. [MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles)
> 某個方塊遊戲

**Language:** C++  |  **Stars:** 4286  |  **Forks:** 808  |  **Best Score:** 2866  |  **Best Rank:** #22  |  **Days on chart:** 2/7  |  **Created:** 2026-03-01

**背景：** MinecraftConsoles 包含 Minecraft Legacy Console Edition v1.6.0560.0（TU19）的原始碼，並附帶修復和改進。它支援透過 Visual Studio 2022 建構 Windows 版本，並新增了鍵盤/滑鼠輸入、全螢幕模式、區域網路多人遊戲和自適應螢幕解析度。於 3 月 1 日發布，立即吸引了社群關注。

**解決的問題：** Minecraft 的 Legacy Console Edition 已停止更新且不再受官方維護。此專案保留並改進了該版本，允許玩家在現代硬體上運行，並支援鍵盤/滑鼠和區域網路多人遊戲等功能。

**為何又一個？** Legacy Console Edition 有一群忠實的玩家，他們偏好其遊戲機制和 UI 而非更新版本。此專案值得注意的是它是社群維護的原始碼移植而非 mod，能夠接收停產的官方版本無法獲得的貢獻和修復。

---

## 57. [Flowise](https://github.com/FlowiseAI/Flowise)
> 視覺化建構 AI 代理

**Language:** TypeScript  |  **Stars:** 50527  |  **Forks:** 23896  |  **Best Score:** 2858  |  **Best Rank:** #19  |  **Days on chart:** 2/7  |  **Created:** 2023-03-31

**背景：** Flowise 是一個 AI 代理的視覺化建構器，提供拖放介面用於建構代理工作流程。擁有超過 50,000 顆星和近 24,000 個 fork，它已成為最受歡迎的無程式碼/低程式碼 AI 開發工具之一。支援自託管和雲端部署。

**解決的問題：** 建構 AI 代理工作流程需要撰寫程式碼來連接 LLM、工具、記憶系統和資料來源。Flowise 用視覺化畫布取代了這一過程，元件透過圖形化方式連接，使非程式設計人員也能進行代理開發。

**為何又一個？** Flowise 的視覺化方法大幅降低了代理開發的門檻。其龐大的 fork 數（23,896）表明廣泛的自訂和部署，顯示它已成為基礎設施而非僅僅是工具。

---

## 58. [ReMe](https://github.com/agentscope-ai/ReMe)
> ReMe：代理記憶管理工具包——記住我，精煉我。

**Language:** Python  |  **Stars:** 2088  |  **Forks:** 156  |  **Best Score:** 2856  |  **Best Rank:** #20  |  **Days on chart:** 1/7  |  **Created:** 2024-08-29

**背景：** ReMe 是 AgentScope 團隊開發的 AI 代理記憶管理工具包，為代理提供跨會話記住上下文和隨時間精煉理解的機制。它與更廣泛的 AgentScope 生態系統整合，可透過 pip 安裝的 Python 套件取得。

**解決的問題：** AI 代理在會話之間忘記一切，使用者需要每次重新建立上下文。ReMe 提供結構化的記憶儲存和檢索，跨會話持久化，讓代理能夠建立累積的理解。

**為何又一個？** ReMe 專門聚焦於記憶問題，而非試圖成為完整的代理框架。這種專業化允許對記憶儲存、檢索和精煉模式進行比通用代理框架更深入的處理。

---

## 59. [fara](https://github.com/microsoft/fara)
> Fara-7B：一個高效的電腦使用代理模型

**Language:** Python  |  **Stars:** 4383  |  **Forks:** 400  |  **Best Score:** 2850  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2025-10-29

**背景：** Fara-7B 是微軟首個專為電腦使用設計的代理式小型語言模型（SLM）。僅有 70 億參數，它在同尺寸級別的電腦使用代理（CUA）任務中達到了最先進的表現——點擊、輸入、導航桌面應用程式。可在本地運行，並在 Hugging Face 和 Azure Foundry 上提供。

**解決的問題：** 基於大型模型的電腦使用代理昂貴且緩慢。Fara-7B 在足夠小到可以本地運行的模型中提供相當的能力，無需雲端 API 成本即可實現自主桌面互動。

**為何又一個？** 以 70 億參數而言，Fara-7B 比競爭的 CUA 模型小得多，同時在基準測試中保持競爭力。隨之發布的 WebTailBench 資料集為電腦使用代理提供了標準化的評估。

---

## 60. [seomachine](https://github.com/TheCraigHewitt/seomachine)
> 一個專為任何企業建立長篇 SEO 最佳化部落格內容的 Claude Code 工作區。

**Language:** Python  |  **Stars:** 2399  |  **Forks:** 400  |  **Best Score:** 2761  |  **Best Rank:** #21  |  **Days on chart:** 3/7  |  **Created:** 2025-10-29

**背景：** SEO Machine 是一個 Claude Code 工作區，提供自訂指令（/research、/write、/analyze、/optimize）、內容分析和 SEO 最佳化的專業代理，以及 26 個行銷技能。它整合了 Google Analytics 4、Google Search Console 和 DataForSEO 以獲取即時效能洞察。

**解決的問題：** 建立 SEO 最佳化的內容需要研究、關鍵字分析、內容結構化、元素創建和內部連結——手動操作時這是一個繁瑣的多步驟工作流程。SEO Machine 透過專業的 Claude Code 指令和代理自動化了這一過程。

**為何又一個？** SEO Machine 將特定領域的 SEO 知識（關鍵字叢集、搜尋意圖偵測、可讀性評分、SEO 品質評級）打包到 Claude Code 的工作流程中，超越了通用的內容生成，產出專門設計用來排名的內容。

---

## 61. [scrapy](https://github.com/scrapy/scrapy)
> Scrapy，一個快速的高階 Python 網頁爬取與抓取框架。

**Language:** Python  |  **Stars:** 60646  |  **Forks:** 11344  |  **Best Score:** 2756  |  **Best Rank:** #16  |  **Days on chart:** 1/7  |  **Created:** 2010-02-22

**背景：** Scrapy 是歷史最悠久、最受歡迎的 Python 網頁爬取框架之一，擁有超過 60,000 顆星，歷史可追溯到 2010 年。它提供了一個完整的框架用於從網站擷取資料，包括請求排程、回應解析、資料管線和中介軟體支援。

**解決的問題：** 建構可靠的網頁爬蟲需要處理並行性、速率限制、重試邏輯、資料擷取和輸出格式化。Scrapy 以完善的文件和可擴展的架構開箱即用地提供了所有這些功能。

**為何又一個？** Scrapy 的成熟度、文件和生態系統使其成為 Python 生產級網頁爬取的預設選擇。本週的上榜紀錄可能反映了 AI 資料收集趨勢帶動的新興趣。

---

## 62. [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
> 代理效能最佳化系統。為 Claude Code、Codex、Opencode、Cursor 等提供技能、本能、記憶、安全和研究優先的開發。

**Language:** JavaScript  |  **Stars:** 69024  |  **Forks:** 8618  |  **Best Score:** 2739  |  **Best Rank:** #20  |  **Days on chart:** 3/7  |  **Created:** 2026-01-18

**背景：** everything-claude-code 是一個全面的 AI 編程代理最佳化系統，涵蓋技能、「本能」（自動行為模式）、記憶管理和安全強化。擁有近 69,000 顆星，它已成為最受歡迎的代理最佳化元工具之一。它包含 npm 套件（ecc-universal、ecc-agentshield）和 GitHub App。

**解決的問題：** 預設的代理配置未能充分發揮效能。此系統提供最佳化的技能、行為模式和安全措施，使代理更有效、更安全、在各編程會話中更一致。

**為何又一個？** 「本能」概念——無需明確調用即自動觸發的行為模式——是對代理最佳化的新穎貢獻。多平台支援（Claude Code、Codex、Cursor 等）和基於 npm 的分發使其廣泛適用。

---

## 63. [ClawRouter](https://github.com/BlockRunAI/ClawRouter)
> OpenClaw 的代理原生 LLM 路由器。41 多個模型，<1ms 路由，透過 x402 在 Base 和 Solana 上以 USDC 支付。

**Language:** TypeScript  |  **Stars:** 5282  |  **Forks:** 405  |  **Best Score:** 2672  |  **Best Rank:** #20  |  **Days on chart:** 3/7  |  **Created:** 2026-02-03

**背景：** ClawRouter 是為 OpenClaw 設計的 LLM 路由系統，從 15 個維度對請求評分，並在 1 毫秒內將其路由到 41 多個模型選項中的最佳模型。它使用透過 x402 協定在 Base 和 Solana 上的非託管 USDC 支付，消除了對個別 API 金鑰的需求。

**解決的問題：** 使用多個 LLM 供應商需要管理獨立的 API 金鑰、計費關係和路由邏輯。ClawRouter 將這些整合為一個具有自動模型選擇和加密貨幣支付的單一端點。

**為何又一個？** 亞毫秒級本地路由、15 維模型評分和加密原生支付（無需 API 金鑰）的組合，針對 OpenClaw 生態系統的特定需求。x402 支付協定整合尤其值得注意，它實現了無需供應商帳號的按請求計費。

---

## 64. [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
> Claude Code 技能和 500 多個來自官方開發團隊和社群的代理技能，相容 Codex、Antigravity、Gemini CLI、Cursor 等。

**Language:** N/A  |  **Stars:** 10076  |  **Forks:** 875  |  **Best Score:** 2629  |  **Best Rank:** #10  |  **Days on chart:** 1/7  |  **Created:** 2025-10-28

**背景：** 同樣由 VoltAgent 維護，此資源庫是一個精選的 549 多個代理技能合集，來自官方開發團隊和社群。不同於批量生成的合集，它專注於由實際工程團隊建立和使用的技能，相容 Claude Code、Codex、Antigravity、Gemini CLI 和 Cursor。

**解決的問題：** 將高品質、經團隊測試的技能與大量生成的技能區分開來需要人工策劃。此合集運用編輯判斷力來呈現經過實際使用驗證的技能。

**為何又一個？** 編輯策劃標準（「由實際工程團隊建立和使用的真實 Agent Skills，而非大量 AI 生成的」）使其有別於更大但策劃程度較低的合集。品質重於數量是其明確的設計選擇。

---

## 65. [ui](https://github.com/shadcn-ui/ui)
> 一套精心設計、無障礙的元件和程式碼分發平台。

**Language:** TypeScript  |  **Stars:** 108588  |  **Forks:** 8067  |  **Best Score:** 2572  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2023-01-04

**背景：** shadcn/ui 是一個元件函式庫和程式碼分發平台，提供精心設計、無障礙的 React 元件。擁有超過 108,000 顆星，它已成為 React 生態系統中最受歡迎的 UI 元件系統之一。不同於傳統元件函式庫，shadcn/ui 設計為被複製和自訂，而非作為依賴匯入。

**解決的問題：** 傳統元件函式庫難以深度自訂，因為樣式和行為被封裝。shadcn/ui 將元件作為原始碼提供，開發者複製到專案中並完全擁有。

**為何又一個？** 複製並擁有的分發模式是其關鍵差異化因素。開發者從第一天起就完全控制元件程式碼，無需與函式庫的抽象作鬥爭。其 108,000 顆星數驗證了這種方法。

---

## 66. [openclaw-studio](https://github.com/grp06/openclaw-studio)
> 一個簡潔的 OpenClaw 網頁儀表板。連接你的 Gateway，管理代理，更快地交付。

**Language:** TypeScript  |  **Stars:** 1532  |  **Forks:** 227  |  **Best Score:** 2550  |  **Best Rank:** #17  |  **Days on chart:** 1/7  |  **Created:** 2026-01-28

**背景：** OpenClaw Studio 是一個網頁儀表板，連接到 OpenClaw Gateway 並提供視覺化介面用於管理代理、查看對話、處理審批和配置工作。它作為本地網頁應用程式運行，可連接到本地或雲端託管的 gateway。

**解決的問題：** OpenClaw 的命令列介面雖然強大，但缺乏有效管理多個代理、審查對話歷史和處理審批工作流程所需的視覺化概覽。Studio 提供了該圖形化層。

**為何又一個？** 作為專為 OpenClaw 建構的儀表板，它提供了通用管理面板無法提供的功能（代理管理、審批工作流程、成本追蹤）。其 Tailscale 遠端存取整合展示了深思熟慮的營運設計。

---

## 67. [hello-agents](https://github.com/datawhalechina/hello-agents)
> 從零開始建構智慧代理——原理與實作教學

**Language:** Python  |  **Stars:** 26281  |  **Forks:** 2949  |  **Best Score:** 2511  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2025-09-07

**背景：** Hello-Agents 是來自 Datawhale 社群——中國領先的開源 AI 教育組織——的系統化智慧代理學習教學。它涵蓋從基礎到進階的代理原理和實作實務。擁有超過 26,000 顆星，它已成為學習代理開發的主要中文語言資源之一。

**解決的問題：** 建構代理系統的系統化實作教學非常稀缺，尤其是中文教學。Hello-Agents 提供了理論與實作並重的結構化課程。

**為何又一個？** Datawhale 社群的教育方法論——結合理論基礎、實作練習和社群支援——產生了孤立的部落格文章和文件無法比擬的學習體驗。其中文優先的方法服務了一個未被充分服務的受眾。

---

## 68. [codebuff](https://github.com/CodebuffAI/codebuff)
> 從終端機生成程式碼！

**Language:** TypeScript  |  **Stars:** 4143  |  **Forks:** 473  |  **Best Score:** 2484  |  **Best Rank:** #23  |  **Days on chart:** 2/7  |  **Created:** 2024-07-09

**背景：** Codebuff 是一個開源 AI 編程助手，使用多代理架構：獨立的代理分別負責檔案挑選、規劃、編輯和審查，協同處理每個任務。它在 175 多個編程任務中聲稱 61% 的通過率，相比 Claude Code 在同一評估套件上的 53%。

**解決的問題：** 單一模型的編程工具經常做出不準確的編輯，因為它們試圖在單次推論中同時處理上下文理解、規劃、編輯和審查。Codebuff 將這些分解為各專注一個方面的專業代理。

**為何又一個？** 多代理架構（檔案挑選器、規劃器、編輯器、審查器）是 Codebuff 的核心主張。透過專業化每個階段，它在其公開的評估套件上比單體方法實現了更好的上下文理解和更少的錯誤。

---

## 69. [skills](https://github.com/anthropics/skills)
> Agent Skills 的公開儲存庫

**Language:** Python  |  **Stars:** 88119  |  **Forks:** 9339  |  **Best Score:** 2479  |  **Best Rank:** #24  |  **Days on chart:** 2/7  |  **Created:** 2025-09-22

**背景：** 這是 Anthropic 官方的 Claude 技能公開儲存庫，實作了來自 agentskills.io 的 Agent Skills 標準。它包含從創意應用（藝術、音樂、設計）到技術任務（測試、MCP 伺服器生成）再到企業工作流程（溝通、品牌）的示範技能。擁有超過 88,000 顆星，是 Anthropic 最受歡迎的儲存庫之一。

**解決的問題：** Claude 的技能系統允許自訂的任務特定指導，但從零建立技能需要理解 SKILL.md 格式和最佳實踐。此儲存庫提供了跨多個領域的參考實作。

**為何又一個？** 作為 Anthropic 的官方技能儲存庫，它定義了技能品質和結構的黃金標準。每個技能都是自包含的，附有自己的 SKILL.md，使其既是使用資源也是自訂技能開發的模板。

---

## 70. [page-agent](https://github.com/alibaba/page-agent)
> JavaScript 頁面內 GUI 代理。用自然語言控制網頁介面。

**Language:** TypeScript  |  **Stars:** 2399  |  **Forks:** 194  |  **Best Score:** 2450  |  **Best Rank:** #13  |  **Days on chart:** 1/7  |  **Created:** 2025-09-23

**背景：** Page Agent 由阿里巴巴開發，是一個 JavaScript 函式庫，將 GUI 代理直接嵌入網頁中，允許使用者透過自然語言指令控制網頁介面。它作為頁面內腳本運行，而非瀏覽器擴充功能或外部工具，提供對 DOM 的直接存取以進行 UI 自動化。

**解決的問題：** 現有的瀏覽器自動化方法（Playwright、Puppeteer、瀏覽器擴充功能）在頁面外部運作，需要序列化頁面狀態。Page Agent 在頁面內部運行，直接存取 DOM、JavaScript 上下文和框架狀態。

**為何又一個？** 頁面內方法消除了困擾外部自動化工具的序列化開銷和狀態同步問題。在頁面內部意味著 Page Agent 可以與外部工具難以處理的單頁應用程式和動態內容互動。

---

## 71. [baoyu-skills](https://github.com/JimLiu/baoyu-skills)
> Baoyu 分享的技能，用於提高使用 Claude Code 的日常工作效率。

**Language:** TypeScript  |  **Stars:** 8006  |  **Forks:** 883  |  **Best Score:** 2411  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2026-01-13

**背景：** baoyu-skills 是開發者 Baoyu（JimLiu）分享的 Claude Code 生產力導向技能合集。它涵蓋圖像生成、Markdown 轉 HTML 轉換和其他日常工作流程最佳化。這些技能可透過 npx、Claude Code 插件市場或單獨發布到 ClawHub 進行安裝。

**解決的問題：** 圖像生成、文件格式轉換和內容管理等常見生產力任務需要在工具之間切換。這些技能將這些功能直接帶入 Claude Code 工作流程中。

**為何又一個？** 這些技能源自一位開發者的日常工作流程策劃，確保它們解決的是真實而非假設性的問題。多分發支援（npx、插件市場、ClawHub）使安裝更加靈活。

---

## 72. [ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5)
> 最強大的本地音樂生成模型，超越大多數商業替代方案。

**Language:** Python  |  **Stars:** 7459  |  **Forks:** 830  |  **Best Score:** 2358  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2025-09-04

**背景：** ACE-Step 1.5 是一個開源音樂生成基礎模型，聲稱具有商業級品質，同時可在消費級硬體上運行。在 A100 上不到 2 秒、在 RTX 3090 上不到 10 秒即可生成完整歌曲，所需 VRAM 不到 4GB。支援 Mac、AMD、Intel 和 CUDA 裝置。

**解決的問題：** 商業音樂生成服務昂貴且在遠端伺服器上處理音訊。ACE-Step 1.5 在本地提供等效品質，具備在消費級 GPU 上運行的速度和記憶體效率。

**為何又一個？** 商業級品質、消費級 GPU 上亞 10 秒生成和低於 4GB VRAM 需求的組合，為本地音樂生成設立了新標桿。多平台支援（包括 Mac 和 AMD）擴大了超越僅 NVIDIA 替代方案的可及性。

---

## 73. [goose](https://github.com/block/goose)
> 一個開源、可擴展的 AI 代理，超越程式碼建議

**Language:** Rust  |  **Stars:** 32693  |  **Forks:** 3006  |  **Best Score:** 2316  |  **Best Rank:** #22  |  **Days on chart:** 1/7  |  **Created:** 2024-08-23

**背景：** Goose 由 Block（前身為 Square）開發，是一個本地、可擴展的 AI 代理，端到端自動化工程任務——從零建構專案、撰寫和執行程式碼、除錯故障，以及與外部 API 互動。以 Rust 撰寫，支援任何 LLM、多模型配置和 MCP 伺服器整合。提供桌面應用和 CLI 兩種形式。

**解決的問題：** 大多數 AI 編程工具止於程式碼建議。Goose 自主執行完整的工作流程：原型設計、程式碼精煉、管線調度和與外部服務互動——無需在每個步驟進行人工監督。

**為何又一個？** Block 的企業支持提供了穩定性，Rust 實作為長時間運行的自主任務提供效能。多模型配置允許針對不同工作流程階段最佳化成本和能力。

---

## 74. [daytona](https://github.com/daytonaio/daytona)
> Daytona 是用於運行 AI 生成程式碼的安全且彈性基礎設施

**Language:** TypeScript  |  **Stars:** 63165  |  **Forks:** 5072  |  **Best Score:** 2286  |  **Best Rank:** #16  |  **Days on chart:** 1/7  |  **Created:** 2024-02-06

**背景：** Daytona 提供安全、彈性的基礎設施用於執行 AI 生成的程式碼。擁有超過 63,000 顆星，它已從開發環境管理器演化為專為 AI 程式碼生成時代設計的沙箱化執行平台。採用 AGPL-3 授權。

**解決的問題：** AI 生成的程式碼需要在安全的地方執行，然後才能信任用於生產。Daytona 提供隔離、可擴展的環境，生成的程式碼可以在其中運行、測試和驗證，而不會危及生產基礎設施。

**為何又一個？** Daytona 從開發環境到 AI 程式碼執行基礎設施的演化反映了真正的市場轉變。其 AGPL 授權確保即使作為服務部署，平台仍保持開源。

---

## 75. [terraink](https://github.com/yousifamanuel/terraink)
> TerraInk：地圖海報引擎，創建獨特且可自訂的地圖海報

**Language:** TypeScript  |  **Stars:** 891  |  **Forks:** 84  |  **Best Score:** 2104  |  **Best Rank:** #17  |  **Days on chart:** 1/7  |  **Created:** 2026-02-10

**背景：** TerraInk 是一個用於創建可自訂地圖海報——任何地點的風格化地圖印刷品——的網頁應用程式。它提供排版、色彩方案、地圖風格和佈局的設計控制，輸出可列印的海報檔案。以 Bun 和 Vite 建構。

**解決的問題：** 創建自訂地圖海報傳統上需要圖形設計技能和 GIS 軟體。TerraInk 提供網頁介面，任何人都可以透過選擇地點和自訂視覺參數來設計專業外觀的地圖海報。

**為何又一個？** TerraInk 對列印品質和設計自訂化的聚焦使其有別於地圖截圖工具。其開源特性允許自託管，消除了商業地圖海報服務每張收取的費用。

---

## 76. [daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)
> LLM 驅動的 A 股/港股/美股智慧分析器，具備多來源資料 + 即時新聞 + Gemini 決策儀表板 + 多管道推送

**Language:** Python  |  **Stars:** 17898  |  **Forks:** 18310  |  **Best Score:** 2083  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2026-01-10

**背景：** daily_stock_analysis 是一個 AI 驅動的股票分析系統，涵蓋 A 股（中國）、H 股（香港）和美股。它結合多個資料來源與即時新聞聚合和基於 Gemini 的分析，產出每日「決策儀表板」推送到企業微信、飛書、Telegram 和電子郵件。設計在 GitHub Actions 上運行以實現零成本營運。

**解決的問題：** 跨不同時區監控多個股票市場需要從多個來源聚合資料、分析新聞影響並產出可操作的摘要。此系統自動化了整個管線，將每日分析推送到使用者偏好的訊息平台。

**為何又一個？** 跨市場覆蓋（A 股/H 股/美股）、零成本 GitHub Actions 部署和多管道推送通知支援，使其特別適合追蹤多個市場的中國投資者。其 fork 數（18,310）實際上超過了星數（17,898），顯示大量的自訂使用。

---

## 77. [Siftly](https://github.com/viperrcrypto/Siftly)
> 本地 Twitter/X 書籤管理器，具備 AI 分類和心智圖視覺化

**Language:** TypeScript  |  **Stars:** 1279  |  **Forks:** 102  |  **Best Score:** 2080  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2026-03-04

**背景：** Siftly 是一個自託管的 Twitter/X 書籤管理器，對儲存的書籤運行 4 階段 AI 管線（匯入、實體擷取、視覺分析、分類）。它將書籤轉化為可搜尋、分類的知識庫，附帶心智圖視覺化。所有資料保留在本地；只有 AI API 呼叫離開機器。

**解決的問題：** Twitter/X 書籤快速累積但缺乏任何組織、搜尋或分類功能。Siftly 將這個無結構的集合轉化為具有 AI 生成分類、實體擷取和視覺化探索的可搜尋知識庫。

**為何又一個？** 4 階段管線——特別是從圖像、GIF 和影片縮圖中讀取文字和上下文的視覺分析步驟——擷取了純文字書籤工具遺漏的資訊。心智圖視覺化提供了獨特的探索介面。

---

## 78. [free-for-dev](https://github.com/ripienaar/free-for-dev)
> SaaS、PaaS 和 IaaS 產品清單，提供對 DevOps 和基礎設施開發者有用的免費方案

**Language:** HTML  |  **Stars:** 119167  |  **Forks:** 12312  |  **Best Score:** 2079  |  **Best Rank:** #20  |  **Days on chart:** 1/7  |  **Created:** 2015-03-18

**背景：** free-for-dev 是一個由社群策劃的 SaaS、PaaS 和 IaaS 服務免費方案清單，專注於基礎設施和 DevOps 工具。擁有超過 119,000 顆星和 1,600 多位貢獻者，它是開發者免費方案服務的權威索引。服務必須提供永久免費方案（而非僅限試用）。

**解決的問題：** 找出哪些基礎設施服務提供真正的免費方案（而非限時試用）需要逐一檢查每個供應商的定價頁面。此清單以一致的標準整合了這些資訊。

**為何又一個？** 它是同類中最原始且最全面的資源，自 2015 年以來持續維護，具有嚴格的收錄標準（必須是永久免費方案、必須包含 TLS、不只是試用）。其定期的上榜紀錄反映了新一波開發者發現它。

---

## 79. [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)
> 一個 AI 對沖基金團隊

**Language:** Python  |  **Stars:** 47031  |  **Forks:** 8174  |  **Best Score:** 2074  |  **Best Rank:** #21  |  **Days on chart:** 1/7  |  **Created:** 2024-11-29

**背景：** ai-hedge-fund 是一個概念驗證的 AI 交易系統，使用多個以著名投資者為範本的專業代理——Warren Buffett、Charlie Munger、Cathie Wood、Michael Burry 等。每個代理運用其同名者的投資哲學分析股票，投資組合管理代理綜合他們的建議。明確標示為教育用途，不適用於真實交易。

**解決的問題：** 理解不同的投資哲學以及它們如何評估同一支股票需要深厚的知識。此系統使這些哲學變得可執行，讓使用者看到不同投資框架如何得出不同結論。

**為何又一個？** 具有個性驅動分析的多代理方法（每個代理體現特定投資者的哲學）既具教育意義又在架構上有趣。其 47,000 顆星數表明遠超交易社群的廣泛吸引力。

---

## 80. [aipyapp](https://github.com/knownsec/aipyapp)
> AI 驅動的 Python 與 Python 驅動的 AI（Python-Use）

**Language:** HTML  |  **Stars:** 3861  |  **Forks:** 378  |  **Best Score:** 2016  |  **Best Rank:** #23  |  **Days on chart:** 1/7  |  **Created:** 2025-04-06

**背景：** Python-Use 由 Knownsec 開發，提出了一種新的 AI 代理範式，LLM 可直接存取 Python 直譯器，建立 Task-Plan-Code-Execute-Feedback 循環。它將自己定位為「Agent 2.0」，認為傳統的函式呼叫和基於 MCP 的代理是「義肢」，造成了不必要的間接層。

**解決的問題：** 傳統 AI 代理依賴預定義工具、函式呼叫介面和插件架構，這些都需要開發者的設置和維護工作。Python-Use 賦予 LLM 完整的 Python 環境，讓它撰寫和執行任意程式碼來完成任務。

**為何又一個？** 其哲學論點——給 LLM 一個 Python 直譯器比建構工具呼叫介面更自然、更有能力——是一個有意義的架構賭注。如果正確，它消除了目前主導代理生態系統的大部分工具/插件基礎設施的需求。

---

## 81. [mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)
> 透過真實世界、跨語言範例介紹 Model Context Protocol（MCP）的開源課程。

**Language:** Jupyter Notebook  |  **Stars:** 15163  |  **Forks:** 4918  |  **Best Score:** 1960  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2025-04-04

**背景：** mcp-for-beginners 是微軟的開源課程，用於學習 Model Context Protocol（MCP），提供 .NET、Java、TypeScript、JavaScript、Rust 和 Python 的範例。它透過實務的跨語言練習涵蓋會話設置、工具註冊、資源管理和服務調度。

**解決的問題：** MCP 正在成為 AI 工具整合的標準，但學習它需要理解協定規格和語言特定的實作模式。此課程提供跨六種程式語言的結構化、實作式學習。

**為何又一個？** 跨語言方法（6 種語言）確保開發者可以在偏好的生態系統中學習 MCP。微軟的教育方法論——透過其「for beginners」系列已經過驗證——提供了僅靠協定文件無法提供的結構化學習路徑。

---

## 82. [production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course)
> AI 專案之母——第一階段 RAG 系統：arXiv 論文策展器

**Language:** Python  |  **Stars:** 3767  |  **Forks:** 1010  |  **Best Score:** 1931  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2025-08-06

**背景：** 此課程透過建構 arXiv 論文策展器來教授生產級 RAG（檢索增強生成）系統。它遵循專業路徑：首先精通關鍵字搜尋，然後新增語義搜尋，再加入 LLM 重新排序——而非直接跳到向量資料庫。目前進行到第 7 週，包含進階功能。

**解決的問題：** 大多數 RAG 教學跳過基礎直接進入向量搜尋，讓開發者缺乏除錯和最佳化生產系統所需的理解。此課程從 BM25 關鍵字搜尋到語義搜尋再到 LLM 重新排序逐層建構，教授每一層的優勢和限制。

**為何又一個？** 漸進式複雜度方法（關鍵字搜尋先於向量搜尋先於 LLM 重新排序）和真實應用（arXiv 論文策展）提供了基於生產工程而非玩具範例的學習體驗。

---

## 83. [system-design-primer](https://github.com/donnemartin/system-design-primer)
> 學習如何設計大規模系統。準備系統設計面試。

**Language:** Python  |  **Stars:** 338012  |  **Forks:** 54751  |  **Best Score:** 1784  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2017-02-26

**背景：** system-design-primer 是 GitHub 上星數最高的儲存庫之一，擁有 338,000 顆星，提供全面的大規模系統設計學習材料。它涵蓋核心概念（CAP 定理、一致性雜湊、資料庫分片）並包含用於面試準備的 Anki 閃卡。支援 17 種以上語言。

**解決的問題：** 系統設計面試需要跨分散式系統、資料庫、快取、負載均衡等領域的廣泛知識。此資源庫在單一位置提供結構化的學習材料，附帶圖表、權衡分析和閃卡。

**為何又一個？** 自 2017 年以來它一直是權威的系統設計學習資源，沒有競爭者能匹配其深度、廣度和社群驅動的翻譯。其上榜反映了它作為面試準備資源的常青相關性。

---

> **本週主題：** 代理基礎設施堆疊持續分層，Google、OpenAI 和 Anthropic 發布第一方工具（gws CLI、Symphony、Claude Code 技能），而開源生態系統則圍繞主導的 OpenClaw 平台，競相填補代理調度、瀏覽器自動化、記憶管理和跨平台技能分發方面的缺口。
