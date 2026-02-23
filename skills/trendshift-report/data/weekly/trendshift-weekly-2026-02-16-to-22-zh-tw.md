# Trendshift 每週報告 — 2026-02-16 至 2026-02-22
**不重複專案總數：** 84（來自 7 天共 175 筆每日上榜紀錄）

---

## 1. [zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)
> 快速、輕巧且完全自主的 AI 助手基礎設施 — 隨處部署，任意替換

**Language:** Rust  |  **Stars:** 16846  |  **Forks:** 1937  |  **Best Score:** 15263  |  **Best Rank:** #1  |  **Days on chart:** 2/7  |  **Created:** 2026-02-13

**背景：** Zeroclaw 是一個以 Rust 撰寫的全新自主 AI 助手基礎設施專案，強調原生效能與極小的二進位檔案大小。它於 2026 年 2 月 13 日發布，數天內即累積近 17,000 顆星，顯示市場對 Rust 原生替代方案有強烈的潛在需求，以取代目前以 TypeScript 為主的助手平台。該專案採用可插拔架構，允許在不修改核心基礎設施程式碼的情況下替換任何 LLM 後端、工具或部署目標。

**解決的問題：** 現有的 AI 助手平台主要以 Python 或 TypeScript 撰寫，帶有大量的執行期開銷，使其難以部署在邊緣硬體或資源受限的環境中。Zeroclaw 編譯為單一小型二進位檔，不依賴任何直譯器，能夠部署在 Python 執行環境或 Node.js 不可用或不切實際的裝置和環境上。其任意替換的設計也消除了模型層的供應商鎖定。

**為何又一個？** Rust 生態系一直缺乏一個一流的自主代理基礎設施函式庫，以對標 LangChain 或 Anthropic Agents SDK 在 Python 和 TypeScript 上所提供的功能。Zeroclaw 以 Rust 型別系統的記憶體安全保證和確定性效能特性填補了這一空缺。發布時機——恰在數個知名 AI 助手平台在高負載下報告可靠性問題之後——似乎加速了其採用。

---

## 2. [cs-video-courses](https://github.com/Developer-Y/cs-video-courses)
> 附有影片講座的電腦科學課程清單。

**Language:** N/A  |  **Stars:** 74570  |  **Forks:** 9957  |  **Best Score:** 11544  |  **Best Rank:** #2  |  **Days on chart:** 2/7  |  **Created:** 2016-10-21

**背景：** cs-video-courses 是一個由社群維護的免費電腦科學課程精選清單，按主題領域分類——演算法、作業系統、機器學習、分散式系統等。由 Developer-Y 於 2016 年 10 月創建，已成長為 GitHub 上最大的自學式電腦科學教育單檔參考資源之一。該清單直接連結到 YouTube、Coursera、MIT OpenCourseWare 等平台上的講座系列。

**解決的問題：** 高品質的電腦科學講座內容散布在數十個大學網站、YouTube 頻道和 MOOC 平台上，標籤和可發現性不一致。這個資源庫將它們整合到一個按主題組織的可瀏覽索引中，為學習者節省了尋找免費資源的時間。

**為何又一個？** cs-video-courses 反覆上榜，因為它是同類中最全面的單一資源庫索引，並且隨著新課程出現持續透過社群 Pull Request 更新。其持久性源於它涵蓋了完整的電腦科學課程體系，而非單一科目，使其對任何學習階段的學習者都有參考價值。

---

## 3. [picoclaw](https://github.com/sipeed/picoclaw)
> 極小、快速、隨處部署 — 自動化繁瑣工作，釋放你的創造力

**Language:** Go  |  **Stars:** 17835  |  **Forks:** 2110  |  **Best Score:** 9288  |  **Best Rank:** #1  |  **Days on chart:** 4/7  |  **Created:** 2026-02-04

**背景：** Picoclaw 是由 Sipeed 推出的基於 Go 的自動化與部署平台，設計為佔用空間極小，同時能在多種硬體目標上運行。它於 2026 年 2 月初發布，不到兩週即累積近 18,000 顆星，顯示在嵌入式和邊緣運算社群中有強大的口碑傳播。該專案強調可攜性，目標環境涵蓋開發者筆記型電腦到資源受限的微控制器。

**解決的問題：** 將自動化工作流程部署到異質硬體——包括低功耗板卡和嵌入式系統——通常需要特定環境的工具鏈和龐大的執行期依賴。Picoclaw 提供一個單一二進位檔，幾乎可以放到任何目標上並立即開始執行工作流程，消除了傳統 CI/CD 工具在邊緣硬體上的啟動摩擦。

**為何又一個？** 大多數自動化平台是為雲端或伺服器等級硬體設計的，所附帶的執行環境對受限目標來說過於龐大。Picoclaw 的差異化在於將小型裝置視為一等部署目標，而非事後才考慮的對象。其快速的星數增長表明，它正在為在 Sipeed 嵌入式硬體生態系統上開發的團隊填補一個真正的空缺。

---

## 4. [vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands)
> 基於 easemate IDE 和 JetBrains Islands 主題的 VSCode 主題

**Language:** PowerShell  |  **Stars:** 3740  |  **Forks:** 108  |  **Best Score:** 8115  |  **Best Rank:** #1  |  **Days on chart:** 2/7  |  **Created:** 2026-02-14

**背景：** vscode-dark-islands 是一個 Visual Studio Code 色彩主題，其美學靈感來自 easemate IDE 和 JetBrains Islands 主題系列。它在本報告的數天前創建，卻迅速累積了數千顆星，顯示對這種視覺風格有強烈的潛在需求。該主題透過 PowerShell 工具進行分發和配置，針對以 Windows 為主的開發者工作流程。

**解決的問題：** 許多在 JetBrains IDE 和 VS Code 之間切換的開發者，會懷念新編輯器中熟悉的 Islands 色彩配置。這個主題在不需要更換整個 IDE 的情況下彌合了這一美學差距，為多語言開發者提供了一個連貫的暗色環境，減少了上下文切換的摩擦。

**為何又一個？** JetBrains Islands 主題有一群忠實的追隨者，而之前沒有任何 VS Code 移植版能足夠忠實地還原它。其爆發式的首週增長表明，它填補了通用暗色主題未曾滿足的特定利基需求。

---

## 5. [pentagi](https://github.com/vxcontrol/pentagi)
> 能夠執行複雜滲透測試任務的完全自主 AI 代理系統

**Language:** Go  |  **Stars:** 4228  |  **Forks:** 588  |  **Best Score:** 7012  |  **Best Rank:** #1  |  **Days on chart:** 4/7  |  **Created:** 2025-01-06

**背景：** PentAGI 是由 vxcontrol 以 Go 建構的自託管自主代理滲透測試系統。它在隔離的 Docker 容器中捆綁了超過 20 種專業安全工具——包括 nmap、Metasploit 和 sqlmap——並使用多代理架構，由領導代理委派任務給專門負責研究、開發和基礎設施的子代理。基於 Neo4j 的知識圖譜提供跨測試會話的長期記憶。

**解決的問題：** 安全測試需要依序調度數十種工具、解讀中間輸出，並根據發現調整攻擊路徑——這一過程需要深厚的專業知識和大量時間。PentAGI 自動化了這一調度層，使系統能夠自主串接工具並產出帶有利用指引的詳細漏洞報告。

**為何又一個？** PentAGI 完全自託管且開源，使其有別於商業 AI 輔助安全平台。其架構包含完整的 REST 和 GraphQL API、Grafana/Prometheus 監控整合，以及一個用於瀏覽器端 OSINT 的內建爬蟲容器——這種完整程度在開源安全工具中並不常見。

---

## 6. [nanoclaw](https://github.com/qwibitai/nanoclaw)
> Clawdbot / OpenClaw 的輕量替代方案，在容器中運行以確保安全性。連接 WhatsApp，具備記憶功能、排程任務，並直接運行在 Anthropic 的 Agents SDK 上

**Language:** TypeScript  |  **Stars:** 10547  |  **Forks:** 1504  |  **Best Score:** 6356  |  **Best Rank:** #1  |  **Days on chart:** 1/7  |  **Created:** 2026-01-31

**背景：** Nanoclaw 是建構在 Anthropic Agents SDK 上的容器化個人 AI 助手，定位為 Clawdbot 和 OpenClaw 的輕量替代方案。它原生連接 WhatsApp 作為主要通訊介面，並內建持久記憶和排程任務支援。該專案於 2026 年 1 月底發布，已迅速累積超過 10,000 顆星。

**解決的問題：** OpenClaw 是一個功能齊全的助手平台，擁有龐大的程式碼庫和複雜的部署需求。Nanoclaw 將概念精簡為一個容器化執行環境，部署和安全防護更為簡單，同時保留大多數使用者需要的核心功能：訊息整合、持久記憶和任務排程。在容器中運行提供了程序級隔離，無需完整的虛擬機或編排層。

**為何又一個？** 關鍵差異化在於直接整合 Anthropic 的 Agents SDK，而非建構自訂的代理執行環境，這意味著 Nanoclaw 能受益於 SDK 的上游改進而無需重新實作。容器優先的架構也使其更容易部署在任何 Docker 相容主機上，從 Raspberry Pi 到雲端虛擬機，而不會出現大型助手平台的依賴膨脹問題。

---

## 7. [openclaw](https://github.com/openclaw/openclaw)
> 你的個人 AI 助手。任何作業系統。任何平台。龍蝦之道。

**Language:** TypeScript  |  **Stars:** 215287  |  **Forks:** 40386  |  **Best Score:** 6129  |  **Best Rank:** #2  |  **Days on chart:** 6/7  |  **Created:** 2025-11-24

**背景：** OpenClaw 是一個個人 AI 助手平台，可在任何作業系統上運行，並聲稱相容任何底層 AI 模型或 API。它以 TypeScript 建構，自 2025 年 11 月推出以來已累積超過 215,000 顆星，使其成為個人助手類別中成長最快的開源專案之一。其圍繞「龍蝦之道」的品牌定位反映了一個圍繞該專案迅速形成的社群認同。

**解決的問題：** 專有 AI 助手被鎖定在特定平台、應用商店或訂閱服務中，限制了使用者對資料和模型選擇的控制權。OpenClaw 提供了一個可自託管的替代方案，能在任何作業系統上運行、連接任何 AI 供應商，並將所有資料保持在使用者的控制下——同時解決了隱私和可攜性問題。

**為何又一個？** OpenClaw 持續上榜，因為其星數使它在個人助手平台中獨樹一幟——超過 215,000 顆星遠超大多數同類專案。其跨平台通用性和活躍的技能與插件社群生態系統推動了持續的發現和在趨勢列表上的反覆出現。

---

## 8. [heretic](https://github.com/p-e-w/heretic)
> 語言模型的全自動審查移除工具

**Language:** Python  |  **Stars:** 8887  |  **Forks:** 884  |  **Best Score:** 5620  |  **Best Rank:** #3  |  **Days on chart:** 4/7  |  **Created:** 2025-09-21

**背景：** Heretic 是由 p-e-w 開發的 Python 工具，能自動移除語言模型的內容過濾和拒絕行為。它針對本機運行的模型而非 API 存取服務，使用技術在推理時修改模型行為。自 2025 年 9 月發布以來，已吸引近 9,000 顆星，並在社群中引發了關於模型審查移除的倫理與合法性的大量討論。

**解決的問題：** 針對公開部署進行微調的語言模型，往往會拒絕來自研究人員、安全專業人員和在敏感但合法領域工作的開發者的正當請求。Heretic 為在自有硬體上運行模型的使用者提供了一種本機自動化方法來移除這些限制，無需手動微調或資料集整理。

**為何又一個？** 該專案佔據了一個刻意具爭議性的利基——自動化、無需專業知識的審查移除——使其有別於手動越獄或微調方法。其自動化和本機優先的設計意味著使用者無需將資料傳送給第三方。圍繞 AI 內容審核的持續公共辯論使其持續受到關注。

---

## 9. [voicebox](https://github.com/jamiepine/voicebox)
> 基於 Qwen3-TTS 的開源語音合成工作室。

**Language:** TypeScript  |  **Stars:** 9955  |  **Forks:** 1040  |  **Best Score:** 4707  |  **Best Rank:** #2  |  **Days on chart:** 5/7  |  **Created:** 2026-01-25

**背景：** Voicebox 是一個以 TypeScript 建構的開源語音合成工作室，使用 Qwen3-TTS 模型作為推理後端。它提供圖形化工作室介面，用於生成、編輯和匯出合成語音。該專案面向內容創作者、開發語音應用程式的開發者，以及評估 TTS 模型品質的研究人員。

**解決的問題：** 高品質的 TTS 系統歷來被鎖定在昂貴的 API 定價層級之後，或需要深厚的機器學習專業知識才能在本機運行。Voicebox 將 Qwen3-TTS 包裝在一個易用的工作室 UI 中，使專業級語音合成無需按字元計費即可使用。它還提供了大多數 SaaS 替代方案所不具備的批次處理和語音參數控制功能。

**為何又一個？** Qwen3-TTS 代表了開放權重 TTS 品質的跨越式進步，而 voicebox 是最早專門為其建構的精緻前端之一。其快速的星數增長反映了市場對一個能與新模型能力配對的生產就緒介面的需求。

---

## 10. [awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources)
> 使用免費資源學習系統設計概念並準備面試。

**Language:** Java  |  **Stars:** 33577  |  **Forks:** 7447  |  **Best Score:** 4667  |  **Best Rank:** #2  |  **Days on chart:** 2/7  |  **Created:** 2023-10-25

**背景：** 由 Ashish Pratap Singh 維護，這個資源庫是一個精選的免費學習材料集合，涵蓋分散式系統基礎、常見架構模式和實用的面試準備指南。它按主題組織資源——從 CAP 定理和共識協定到 Netflix 和 Uber 等公司的真實系統案例研究。該資源庫自 2023 年 10 月以來穩定成長至超過 33,000 顆星。

**解決的問題：** 系統設計面試準備分散在付費課程、零散的部落格文章和品質參差不齊的 YouTube 影片中。這個資源庫將高品質的免費資源整合到一個結構化的參考中，減少了求職者尋找可靠材料的時間。它同樣適合想在面試情境之外深化分散式系統知識的工程師作為自學課程。

**為何又一個？** 它持續上榜，因為系統設計面試仍然是工程師招聘中的高風險瓶頸，而該資源庫持續收到新案例研究和資源連結的更新。其 Java 程式碼範例與概念性文章的結合，使其比純文字資源清單具有更廣泛的實用性。

---

## 11. [superpowers](https://github.com/obra/superpowers)
> 一個有效的代理技能框架與軟體開發方法論。

**Language:** Shell  |  **Stars:** 56468  |  **Forks:** 4282  |  **Best Score:** 4288  |  **Best Rank:** #3  |  **Days on chart:** 6/7  |  **Created:** 2025-10-09

**背景：** Superpowers 是由 Jesse Vincent（obra）創建的可組合技能框架和結構化軟體開發方法論。它透過插件系統安裝到 Claude Code、Cursor、Codex 和 OpenCode 等編碼代理中，強制執行多階段工作流程：腦力激盪並精煉規格、產出詳細的實作計畫，然後透過子代理驅動的開發和兩階段程式碼審查來執行。該專案自 2025 年 10 月以來已累積超過 56,000 顆星。

**解決的問題：** 使用預設設定的編碼代理往往會跳過規劃、忽略測試驅動開發，並在會話中途偏離原始意圖。Superpowers 安裝了防護機制——強制規格核准、紅-綠-重構 TDD 執行，以及計畫檢查點——使代理能夠在長時間自主工作而不偏離既定目標。

**為何又一個？** Superpowers 並非一個新的編碼代理，而是一個透過插件系統跨多個代理運作的方法論層。其可攜性——同一套技能可安裝在 Claude Code、Cursor、Codex 和 OpenCode 中——以及對子代理委派而非單一長時間上下文的強調，是其主要差異化因素。隨著新的代理編碼使用者發現跨代理相容性，它持續上榜。

---

## 12. [zvec](https://github.com/alibaba/zvec)
> 輕量、極速的行程內向量資料庫

**Language:** C++  |  **Stars:** 5951  |  **Forks:** 330  |  **Best Score:** 4236  |  **Best Rank:** #5  |  **Days on chart:** 4/7  |  **Created:** 2025-12-05

**背景：** Zvec 是阿里巴巴開發的行程內向量資料庫，以 C++ 撰寫以實現最小開銷和最大吞吐量。與獨立的向量資料庫伺服器不同，它直接嵌入呼叫應用程式的行程中，消除了每次相似性搜尋的網路往返成本。它於 2025 年 12 月發布，在大約十週內成長至近 6,000 顆星。

**解決的問題：** 將向量資料庫作為獨立服務運行會引入延遲、營運複雜性和基礎設施成本，對於嵌入工作量適中的應用程式來說難以合理化。Zvec 將向量搜尋帶入應用程式的行程內，允許相似性查詢以記憶體速度執行，無需行程間通訊或序列化開銷。

**為何又一個？** 最廣泛採用的向量資料庫——Pinecone、Weaviate、Qdrant——都被設計為獨立服務。Zvec 佔據了行程內利基，類似於 SQLite 相對於完整資料庫伺服器的定位。阿里巴巴的支持和 C++ 實作為其提供了信譽和效能基準，吸引了對運行獨立向量服務的營運負擔感到沮喪的團隊。

---

## 13. [OpenViking](https://github.com/volcengine/OpenViking)
> OpenViking 是一個專為 AI 代理設計的開源上下文資料庫。

**Language:** Python  |  **Stars:** 3160  |  **Forks:** 231  |  **Best Score:** 4150  |  **Best Rank:** #4  |  **Days on chart:** 2/7  |  **Created:** 2026-01-05

**背景：** OpenViking 是由字節跳動的雲端基礎設施部門 Volcengine 開發的開源上下文資料庫。它專為 AI 代理工作流程設計，將代理記憶、工具輸出和中間推理產物視為統一的檔案系統，而非異質的資料儲存集合。該專案於 2026 年 1 月發布，針對需要跨會話持久且可查詢上下文的生產代理部署。

**解決的問題：** 如今的 AI 代理通常透過上下文文字、向量儲存和鍵值快取的混合方式來管理上下文，每種方式有各自的 API 和一致性保證。OpenViking 將這些統一在單一檔案系統抽象之下，允許代理使用熟悉的路徑操作來讀寫上下文，無論底層儲存後端為何。

**為何又一個？** 現有的上下文管理方案如 mem0 和 Zep 要麼是嵌入式函式庫，要麼是託管服務。OpenViking 是一個獨立的、可自託管的資料庫，具有檔案系統介面，為需要持久代理上下文但不想被雲端供應商鎖定的團隊填補了空缺。其 Volcengine 的支持為該專案提供了生產等級的工程資源。

---

## 14. [Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)
> O'Reilly 書籍《Hands-On Large Language Models》的官方程式碼資源庫

**Language:** Jupyter Notebook  |  **Stars:** 22267  |  **Forks:** 5198  |  **Best Score:** 3676  |  **Best Rank:** #4  |  **Days on chart:** 2/7  |  **Created:** 2024-06-28

**背景：** 這個資源庫包含 Jay Alammar 和 Maarten Grootendorst 所著 O'Reilly 書籍《Hands-On Large Language Models》的所有程式碼 notebook，該書有時因其近 300 張自製圖表而被稱為「圖解 LLM 書」。每一章都有對應的 Google Colab 相容 Jupyter notebook，涵蓋從分詞和嵌入到微調、檢索和代理的主題。Jay Alammar 以其圖解 Transformer 說明聞名；Maarten Grootendorst 是 BERTopic 的作者。

**解決的問題：** 大多數 LLM 學習資源要麼純粹是理論性的（學術論文），要麼純粹是實務性的（假設特定平台的供應商教學）。這本書和程式碼透過對模型內部運作的視覺化解釋，搭配不需要本機 GPU 的可執行 notebook，彌合了這一差距。

**為何又一個？** 這本書持續上榜，因為它仍然是非深度機器學習背景的從業者了解 LLM 內部原理的最易入門資源之一。Alammar 的插圖密集風格與 Grootendorst 的應用 NLP 專業知識的結合，覆蓋了與 fast.ai（針對從頭訓練）或 LangChain 教學（專注於應用建構而非模型內部）不同的受眾。

---

## 15. [prompts.chat](https://github.com/f/prompts.chat)
> 又名 Awesome ChatGPT Prompts。分享、探索並收集來自社群的提示詞。免費且開源——可為你的組織自託管以確保完全隱私。

**Language:** HTML  |  **Stars:** 146140  |  **Forks:** 19286  |  **Best Score:** 3674  |  **Best Rank:** #3  |  **Days on chart:** 2/7  |  **Created:** 2022-12-05

**背景：** 由 Fatih Kadir Akin 於 2022 年 12 月以「Awesome ChatGPT Prompts」之名推出，prompts.chat 是第一個針對 AI 聊天模型的主要開源提示詞集合。此後它演變為一個完整的社群平台，具備網頁前端、Hugging Face 資料集、自託管選項，以及一本關於提示工程的互動書籍。該資源庫有 40 多篇學術引用，並被哈佛和哥倫比亞大學引用。

**解決的問題：** 早期 ChatGPT 使用者沒有系統提示詞和基於角色的指令共享資源庫，使得提示詞的發現純粹依靠口耳相傳。這個資源庫提供了一個結構化、由社群維護的角色和任務提示詞庫，可作為起點使用，減少了從通用模型獲取有用輸出所需的反覆試錯。

**為何又一個？** 這個資源庫反覆上榜，因為它是提示詞集合的經典參考。它從靜態 Markdown 檔案演變為具有社群提交工作流程、Hugging Face 資料集映射和自託管功能的完整網頁平台，使其作為一個持續更新的資源而非存檔清單保持了相關性。

---

## 16. [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)
> 800 多個代理技能的終極合集，適用於 Claude Code/Antigravity/Cursor。經過實戰測試的高效能 AI 代理技能。

**Language:** Python  |  **Stars:** 13791  |  **Forks:** 2590  |  **Best Score:** 3616  |  **Best Rank:** #4  |  **Days on chart:** 4/7  |  **Created:** 2026-01-14

**背景：** Antigravity Awesome Skills 是一個由社群策劃的登錄檔，收錄了超過 800 個可重用的代理技能，相容 Claude Code、Cursor 和 Antigravity 代理框架。它捆綁了來自 Anthropic 和 Vercel 的官方技能以及社群貢獻，並按功能類別組織——程式碼審查、測試、部署、文件等。該資源庫於 2026 年 1 月推出，已迅速成為建構代理工作流程團隊的首選資源。

**解決的問題：** 從頭建構有效的代理工作流程需要大量的提示工程和工具呼叫專業知識。這個集合提供了經過實戰測試、可即時安裝的技能，編碼了常見開發任務的最佳實踐，使團隊能夠在不花數週開發自訂技能的情況下採用代理工作流程。

**為何又一個？** 超過 800 個技能的廣度和多代理相容性——涵蓋 Claude Code、Antigravity 和 Cursor——使其比單一平台技能集合具有更廣泛的吸引力。其包含 Anthropic 和 Vercel 官方技能，標誌著許多社群資源庫所缺乏的機構支持，促進了其快速成長和反覆上榜。

---

## 17. [ProxyBridge](https://github.com/InterceptSuite/ProxyBridge)
> Proxifier 替代方案，可將任何 Windows/MacOS/Linux 的 TCP 和 UDP 流量重新導向至 HTTP/Socks5 代理

**Language:** C  |  **Stars:** 2300  |  **Forks:** 153  |  **Best Score:** 3406  |  **Best Rank:** #5  |  **Days on chart:** 1/7  |  **Created:** 2025-10-13

**背景：** ProxyBridge 是由 InterceptSuite 以 C 撰寫的跨平台透明代理重新導向工具，作為商業 Proxifier 應用程式的開源替代方案。它在系統層級攔截 TCP 和 UDP 流量，並透過使用者指定的 HTTP 或 Socks5 代理進行路由，無需應用程式具備內建的代理支援。它以單一一致的介面支援 Windows、macOS 和 Linux。

**解決的問題：** 許多應用程式不遵循系統代理設定或缺乏可配置的代理選項，使得將其流量透過企業代理、VPN 或安全測試攔截工具進行路由變得困難。ProxyBridge 透過在作業系統層級透明地重新導向流量來解決這個問題，無論應用程式是否配合。

**為何又一個？** Proxifier 是閉源、以 Windows 為主的訂閱制授權軟體。ProxyBridge 提供完整的跨平台支援、開源透明度和零授權成本——對需要在多個作業系統上檢查或重新導向流量的安全研究人員和開發者而言，這些都是關鍵屬性。C 語言實作使二進位檔保持小巧且無依賴。

---

## 18. [rowboat](https://github.com/rowboatlabs/rowboat)
> 具備記憶功能的開源 AI 同事

**Language:** TypeScript  |  **Stars:** 8002  |  **Forks:** 685  |  **Best Score:** 3223  |  **Best Rank:** #6  |  **Days on chart:** 2/7  |  **Created:** 2025-01-13

**背景：** Rowboat 是由 Rowboat Labs 建構的開源 AI 同事平台，具備持久記憶功能，允許代理跨會話累積上下文。它被設計為嵌入團隊的助手，而非無狀態的聊天介面，能隨時間維持對進行中專案、決策和團隊偏好的感知。該專案於 2025 年 1 月推出，已成長至超過 8,000 顆星。

**解決的問題：** 大多數 AI 助手在會話之間重置上下文，要求使用者反覆重新解釋其專案狀態和偏好。Rowboat 的持久記憶層允許它隨時間建立團隊專案和慣例的工作模型，使其部署越久越有用。

**為何又一個？** Rowboat 將自己定位為商業 AI 同事產品的開源替代方案，讓團隊完全控制記憶儲存位置和代理的配置方式。持久記憶與開放、可自託管架構的結合，是其與無狀態開源助手和專有同事平台之間的主要差異化因素。

---

## 19. [polymarket-kalshi-arbitrage-bot](https://github.com/ryan26craf/polymarket-kalshi-arbitrage-bot)
> Kalshi 開源交易機器人，用於在加密預測市場上自動化跟單交易和套利策略

**Language:** Python  |  **Stars:** 738  |  **Forks:** 2  |  **Best Score:** 3154  |  **Best Rank:** #9  |  **Days on chart:** 1/7  |  **Created:** 2026-02-06

**背景：** 這是一個開源 Python 機器人，用於在 Polymarket 和 Kalshi 這兩個受監管的預測市場平台上自動化套利和跟單交易策略。它於 2026 年 2 月發布，目標是希望利用不同平台上相同事件合約之間價差的交易者。程式碼庫與兩個平台的 API 對接，以程式化方式監控價格並執行交易。

**解決的問題：** 預測市場套利需要同時監控多個平台、即時計算價差機會，並以比手動操作更快的速度執行交易。這個機器人自動化了跨平台套利機會的偵測和執行，降低了理解策略但無法從頭實作的交易者的技術門檻。

**為何又一個？** 在圍繞預測市場的監管更加明確之後，Polymarket 和 Kalshi 都獲得了大量使用者。在單一機器人中結合這兩個特定且廣泛使用的平台是新穎的，而其開源性質允許交易者審計和修改策略邏輯——這是專有交易機器人所無法做到的。

---

## 20. [Kiro](https://github.com/kirodotdev/Kiro)
> Kiro 是一個代理式 IDE，從原型到上線全程與你並肩工作。

**Language:** TypeScript  |  **Stars:** 3041  |  **Forks:** 149  |  **Best Score:** 3133  |  **Best Rank:** #5  |  **Days on chart:** 1/7  |  **Created:** 2025-06-17

**背景：** Kiro 是由 kirodot.dev 團隊建構的代理式 IDE，於 2025 年 6 月推出。它提供了一個整合開發環境，讓 AI 代理在從原型設計到生產部署的完整生命週期中與開發者並肩工作。該 IDE 以 TypeScript 建構，已累積超過 3,000 顆星。

**解決的問題：** 大多數 AI 編碼工具是作為擴充套件附加到現有編輯器上，或作為獨立的終端代理運行，在 AI 的理解和 IDE 的能力之間造成脫節。Kiro 將代理式輔助直接整合到 IDE 本身，使 AI 能原生存取專案結構、除錯、建構系統和部署管線，而無需外部工具整合。

**為何又一個？** 儘管 Cursor 和 Windsurf 將 AI 添加到 VS Code 分支中，Kiro 是從頭開始作為代理原生 IDE 建構的，而非將 AI 改裝到現有編輯器中。其對從原型到生產完整生命週期的關注，使其有別於主要協助程式碼生成但將部署和營運留給開發者的工具。

---
## 21. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code 是一款代理式編程工具，運行在你的終端機中，能理解你的程式碼庫，並幫助你更快地編寫程式碼。

**Language:** Shell  |  **Stars:** 68067  |  **Forks:** 5340  |  **Best Score:** 3116  |  **Best Rank:** #5  |  **Days on chart:** 2/7  |  **Created:** 2025-02-22

**背景：** Claude Code 是 Anthropic 官方推出的終端機代理式編程工具，於 2025 年 2 月發布。它直接在開發者的終端機中運行，理解完整的程式碼庫脈絡，並透過自然語言指令執行任務。該工具可處理日常開發任務、解釋複雜程式碼、管理 git 工作流程，並支援可擴展的技能和鉤子系統以進行自訂。

**解決的問題：** 開發者在重複性編程任務、瀏覽不熟悉的程式碼庫以及管理版本控制工作流程上花費大量時間。Claude Code 直接在開發者日常使用的終端機中自動化這些任務，消除了在 IDE、瀏覽器端 AI 聊天和命令列之間切換的額外負擔。

**為何又一個？** Claude Code 持續上榜是因為它是 Anthropic 的第一方編程代理，已成為終端機代理式開發的參考實作。其不斷增長的社群技能、鉤子和配置生態系統推動了持續採用。透過技能框架的可擴展性意味著該工具的能力隨著社群貢獻而擴展，而非僅依賴官方發布。

---

## 22. [cmux](https://github.com/manaflow-ai/cmux)
> 基於 Ghostty 的 macOS 終端機，具備垂直分頁和 AI 編程代理通知功能

**Language:** Swift  |  **Stars:** 762  |  **Forks:** 13  |  **Best Score:** 2800  |  **Best Rank:** #6  |  **Days on chart:** 2/7  |  **Created:** 2026-01-28

**背景：** Cmux 是一款基於 Ghostty 終端模擬器函式庫打造的原生 macOS 終端應用程式，由 Manaflow AI 開發。它專為 AI 編程代理工作流程設計，具備垂直分頁以管理多個代理會話、內建的任務完成通知功能，以及針對監控並行代理運行最佳化的精簡介面。

**解決的問題：** 同時運行多個 AI 編程代理的開發者在終端管理上面臨困難——標準終端缺乏長時間運行代理任務的通知功能，也難以一目了然地監控多個會話。Cmux 為此工作流程提供了專用 UI，包含垂直分頁和完成通知。

**為何又一個？** 現有的終端如 iTerm2、Warp 和 Ghostty 本身都是通用型工具，並未針對運行和監控 AI 代理的特定模式進行最佳化。Cmux 將範圍縮小到這個單一使用場景，提供代理感知的通知和為並行會話監控設計的垂直分頁佈局，而非傳統的 shell 工作流程。

---

## 23. [fluxer](https://github.com/fluxerapp/fluxer)
> 一個免費開源的即時通訊和 VoIP 平台，專為朋友、群組和社群打造。

**Language:** TypeScript  |  **Stars:** 4321  |  **Forks:** 172  |  **Best Score:** 2718  |  **Best Rank:** #7  |  **Days on chart:** 4/7  |  **Created:** 2026-01-01

**背景：** Fluxer 是一個以 TypeScript 建構的開源即時通訊和 VoIP 平台，主要面向朋友群組和線上社群。它於 2026 年 1 月 1 日推出，在最初六週內已成長至超過 4,300 顆星。該平台定位為專有通訊平台的免費、可自行託管替代方案，提供文字訊息、語音和社群組織功能。

**解決的問題：** Discord 等熱門通訊平台是閉源的、完全由單一公司託管，且可能因政策變更而影響整個社群。Fluxer 提供可自行託管的替代方案，讓社群營運者掌控自己的基礎設施、資料保留政策和管理工具，無需依賴第三方平台。

**為何又一個？** 對開源 Discord 替代方案的需求持續存在，且已產生多個專案，但少有能在單一可自行託管套件中實現文字、語音和社群管理完整功能對等的方案。Fluxer 的 TypeScript 技術棧使其對熟悉現代網頁開發工具的貢獻者更具親和力。

---

## 24. [RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)
> 展示各種進階的檢索增強生成（RAG）系統技術。

**Language:** Jupyter Notebook  |  **Stars:** 25501  |  **Forks:** 2991  |  **Best Score:** 2706  |  **Best Rank:** #6  |  **Days on chart:** 2/7  |  **Created:** 2024-07-13

**背景：** RAG_Techniques 是 Nir Diamant 整理的全面 Jupyter Notebook 合集，展示超越基本向量搜尋的進階檢索增強生成技術。它涵蓋混合檢索、重新排序、多查詢擴展、上下文壓縮和代理式 RAG 模式等方法。該儲存庫自 2024 年 7 月推出以來已成長至超過 25,000 顆星，並定期更新新技術。

**解決的問題：** 使用單一嵌入模型和餘弦相似度的基本 RAG 實作在處理複雜查詢時往往檢索品質不佳。本儲存庫中的技術針對特定失敗模式——查詢歧義、語義偏移、上下文溢出和相關性衰減——提供具體的、可運行的 notebook 實作，而非僅是理論描述。

**為何又一個？** RAG_Techniques 反覆上榜是因為它是最全面的開源實用 RAG 模式合集，且附有可運行的程式碼。隨著新的檢索技術在研究論文中發表，Diamant 會加入 notebook 實作，使儲存庫保持最新，成為建構生產級 RAG 系統的 ML 工程師的首選資源。

---

## 25. [humanizer](https://github.com/blader/humanizer)
> Claude Code 技能，可移除文字中 AI 生成寫作的痕跡

**Language:** N/A  |  **Stars:** 6015  |  **Forks:** 457  |  **Best Score:** 2666  |  **Best Rank:** #7  |  **Days on chart:** 1/7  |  **Created:** 2026-01-18

**背景：** Humanizer 是由 blader 建立的 Claude Code 技能，可重寫 AI 生成的文字以移除機器寫作的明顯痕跡。它作為 Claude Code 環境中的插件運行，分析文字中常見的 AI 寫作模式——如過度的模糊用語、公式化的過渡語和不自然的措辭——並重寫使其讀起來更自然。該專案自 2026 年 1 月以來已獲得超過 6,000 顆星。

**解決的問題：** AI 生成的文字通常呈現出可辨識的模式，讓讀者和偵測器都能一眼看出：過於正式的語調、重複的句子結構和特徵性的填充詞句。Humanizer 處理此類文字以產生讀起來像自然寫作的輸出，同時解決可讀性問題和偵測規避需求。

**為何又一個？** 與獨立的改寫工具或網頁端重寫器不同，Humanizer 直接整合到 Claude Code 工作流程中作為技能，允許使用者在不離開開發環境的情況下立即將其應用於任何文字輸出。與 Claude Code 技能系統的緊密整合使其成為單一指令操作，而非需要另外使用的工具。

---

## 26. [airllm](https://github.com/lyogavin/airllm)
> AirLLM 以單張 4GB GPU 進行 70B 推論

**Language:** Jupyter Notebook  |  **Stars:** 11717  |  **Forks:** 1066  |  **Best Score:** 2626  |  **Best Rank:** #7  |  **Days on chart:** 1/7  |  **Created:** 2023-06-12

**背景：** AirLLM 是一個函式庫，能在僅 4GB VRAM 的單張 GPU 上運行 700 億參數的語言模型。由 Gavin Li 建立並於 2023 年 6 月首次發布，它使用逐層推論和積極的記憶體管理，以容納通常需要多張高階 GPU 的模型。該專案已穩步成長至近 12,000 顆星。

**解決的問題：** 在本地運行大型語言模型通常需要昂貴的多 GPU 配置或 80+ GB VRAM 的雲端實例。AirLLM 透過以推論速度換取大幅降低的記憶體需求，使 70B 級別的模型對擁有消費級硬體的開發者和研究人員變得可及。

**為何又一個？** 雖然 GPTQ 和 AWQ 等量化函式庫可縮減模型大小，但仍需將整個量化模型載入記憶體。AirLLM 採取根本不同的方法，將各層串流通過 GPU 記憶體，這意味著 VRAM 需求取決於最大的單一層而非完整模型。這種架構選擇使得僅靠量化無法服務的硬體類別也能運行模型。

---

## 27. [summarize](https://github.com/steipete/summarize)
> 指向任何 URL/YouTube/Podcast 或檔案，獲取摘要。支援 CLI 和 Chrome 擴充功能。

**Language:** TypeScript  |  **Stars:** 3905  |  **Forks:** 240  |  **Best Score:** 2606  |  **Best Rank:** #8  |  **Days on chart:** 1/7  |  **Created:** 2025-12-17

**背景：** Summarize 是 steipete 開發的 TypeScript 工具，接受 URL、YouTube 影片、Podcast 訂閱源或本地檔案，並使用底層語言模型返回簡明摘要。它同時以 CLI 工具和 Chrome 擴充功能形式提供，覆蓋終端機和瀏覽器兩種工作流程。該專案專注於最小配置——貼上連結即可獲得輸出。

**解決的問題：** 消化長篇內容如 Podcast 和技術文章非常耗時，尤其當讀者只需要關鍵要點時。Summarize 自動化了轉錄和濃縮步驟，使快速篩選大量內容佇列成為可能。CLI/擴充功能的雙重提供方式意味著使用者不需切換使用場景。

**為何又一個？** 大多數摘要工具是需要帳號並將使用者資料發送到第三方伺服器的網路服務。Summarize 可自行託管且不綁定特定模型，吸引已擁有偏好模型供應商 API 存取權限的注重隱私使用者。

---

## 28. [hummingbot](https://github.com/hummingbot/hummingbot)
> 幫助你建立和部署高頻加密貨幣交易機器人的開源軟體

**Language:** Python  |  **Stars:** 17391  |  **Forks:** 4464  |  **Best Score:** 2423  |  **Best Rank:** #10  |  **Days on chart:** 3/7  |  **Created:** 2019-04-02

**背景：** Hummingbot 是一個成熟的開源框架，用於建構和部署高頻加密貨幣交易機器人，最初於 2019 年 4 月發布。它透過統一的連接器介面支援數十個中心化和去中心化交易所上的做市、套利和方向性策略。該專案擁有超過 17,000 顆星、近 4,500 個分支，以及由個人交易者和做市商公司長期生產使用的記錄。

**解決的問題：** 建構一個能可靠連接多個交易所、處理訂單生命週期管理並以低延遲執行策略的高頻交易機器人需要大量工程投入。Hummingbot 抽象化了交易所連接和訂單管理層，讓交易者能在不為每個交易所從頭重建基礎設施的情況下實作和回測策略。

**為何又一個？** Hummingbot 持續上榜是因為它仍然是少數具備廣泛交易所覆蓋範圍和活躍治理社群的開源高頻交易框架之一。新增的交易所支援、策略添加以及定期的市場波動帶動的交易者興趣，使其在首次發布多年後仍保持能見度。

---

## 29. [cs249r_book](https://github.com/harvard-edge/cs249r_book)
> 機器學習系統導論

**Language:** JavaScript  |  **Stars:** 20499  |  **Forks:** 2359  |  **Best Score:** 2416  |  **Best Rank:** #11  |  **Days on chart:** 2/7  |  **Created:** 2023-09-06

**背景：** cs249r_book 是哈佛大學 CS249r 課程「Tiny Machine Learning」的開源教科書，由哈佛邊緣運算實驗室開發。本書涵蓋從模型設計、硬體限制到邊緣裝置和嵌入式系統部署的完整 ML 系統技術棧。它在 GitHub 上使用 Quarto 協作編寫並渲染為網頁書籍，允許社群透過 pull request 貢獻。

**解決的問題：** 大多數 ML 教育資源專注於模型準確性和訓練技術，而未涉及在受限硬體上部署模型時出現的系統級問題。本教科書透過以結構化的學術格式涵蓋量化、硬體-軟體協同設計、推論最佳化和實際部署考量來彌補這一差距。

**為何又一個？** 本書反覆上榜是因為它是少數以開放授權、大學品質端到端涵蓋 ML 系統（而非僅 ML 理論）的教科書之一。隨著邊緣 AI 部署日益主流化，對實用系統知識的興趣持續增長，而這仍然是該領域最全面的免費資源。

---

## 30. [worldmonitor](https://github.com/koala73/worldmonitor)
> 即時全球情報儀表板——AI 驅動的新聞聚合、地緣政治監控和基礎設施追蹤

**Language:** TypeScript  |  **Stars:** 8834  |  **Forks:** 1068  |  **Best Score:** 2225  |  **Best Rank:** #9  |  **Days on chart:** 1/7  |  **Created:** 2026-01-08

**背景：** WorldMonitor 是一個基於 TypeScript 的即時儀表板，將全球新聞、地緣政治事件和基礎設施狀態聚合到統一的態勢感知介面中。它使用 AI 對傳入的訊號進行分類和排序，為監控全球動態的使用者呈現最具可操作性的情報。自 2026 年 1 月推出以來，不到六週已成長至近 9,000 顆星。

**解決的問題：** 監控全球事件的分析師和研究人員必須手動從數十個新聞來源、RSS 訂閱源和政府公告中聚合資訊，然後從雜訊中篩選出有價值的訊號。WorldMonitor 自動化了聚合和 AI 驅動的篩選步驟，呈現按重要性排列的地緣政治和基礎設施事件的綜合視圖。

**為何又一個？** 現有的商業情報儀表板價格昂貴且設計上面向企業採購流程。WorldMonitor 可自行託管且開源，使獨立研究人員、記者和無法負擔商業平台的安全團隊也能獲得即時全球態勢感知能力。

---

## 31. [convert](https://github.com/p2r3/convert)
> 真正通用的線上檔案轉換器

**Language:** TypeScript  |  **Stars:** 1931  |  **Forks:** 173  |  **Best Score:** 2185  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2025-12-07

**背景：** convert 是 p2r3 於 2025 年 12 月建立的基於 TypeScript 的線上檔案轉換工具，旨在透過組合多個底層轉換函式庫來支援比現有轉換器更廣泛的檔案格式。它設計為可自行託管的網頁應用程式，而非需要上傳到第三方服務。該專案在發布約兩個月內已達到近 2,000 顆星。

**解決的問題：** 現有的線上檔案轉換器要麼支援的格式範圍狹窄、施加檔案大小限制，要麼需要將敏感檔案上傳到雲端服務。需要轉換罕見格式、處理大型檔案或避免將資料發送給第三方的開發者和進階使用者，過去可自行託管的選項很有限。convert 將多種轉換後端整合到單一統一介面之後。

**為何又一個？** 「真正通用」的定位反映了可自行託管轉換器中的真實缺口：大多數開源替代方案專注於單一媒體類型，如影片或文件轉換。透過將多個函式庫組合成一個可部署的應用程式，convert 避免了為不同格式系列運行和維護獨立工具的需要。其相對於星數而言偏高的分數表明近期快速成長和強勁的上榜動能。

---

## 32. [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
> GitNexus：零伺服器程式碼智慧引擎——完全在瀏覽器中運行的客戶端知識圖譜建立器。

**Language:** TypeScript  |  **Stars:** 885  |  **Forks:** 82  |  **Best Score:** 2174  |  **Best Rank:** #10  |  **Days on chart:** 2/7  |  **Created:** 2025-08-02

**背景：** GitNexus 是一個客戶端程式碼智慧工具，可從 GitHub 儲存庫或 ZIP 檔案生成互動式知識圖譜，完全在瀏覽器中運行，無需伺服器元件。它包含一個內建的 Graph RAG Agent，允許使用者以對話方式查詢生成的知識圖譜。該專案由 Abhigyan Patwari 建立，於 2025 年 8 月推出。

**解決的問題：** 理解一個不熟悉的程式碼庫通常需要克隆、設定本地環境，並手動追蹤模組之間的依賴關係和關聯。GitNexus 完全消除了設定步驟——使用者在瀏覽器中輸入儲存庫 URL 或 ZIP 檔案，即可立即獲得程式碼庫結構的視覺化知識圖譜以及用於探索的 AI 代理。

**為何又一個？** 零伺服器、完全客戶端的架構是與 Sourcegraph 或 CodeSee 等需要伺服器端索引的程式碼智慧工具的主要差異點。完全在瀏覽器中運行意味著資料不會離開使用者的機器，解決了專有程式碼庫的隱私疑慮。整合的 Graph RAG Agent 在視覺化圖譜之上增加了對話式探索功能。

---

## 33. [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
> 主要 AI 編程工具的系統提示詞、內部工具和 AI 模型

**Language:** N/A  |  **Stars:** 115359  |  **Forks:** 29733  |  **Best Score:** 2172  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2025-03-05

**背景：** 該儲存庫是一個全面的存檔，收錄了從超過 30 個主要 AI 編程和助手工具中提取的系統提示詞、內部工具定義和模型配置。它涵蓋 Anthropic、Cursor、Devin AI、Replit、Windsurf、Perplexity 等多家公司的產品。該儲存庫自 2025 年 3 月以來已累積超過 115,000 顆星，使其成為 GitHub 上最多星的提示詞提取合集之一。

**解決的問題：** AI 工具的系統提示詞是專有的且對使用者隱藏的，使得難以了解這些工具在內部如何運作、受到哪些約束或如何建構類似功能。該儲存庫將這些提示詞公開以供研究、比較和教育用途，使開發者能從生產級提示詞工程中學習。

**為何又一個？** 該儲存庫持續上榜是因為新的 AI 編程工具頻繁推出，現有工具也定期更新其系統提示詞，產生了對變更記錄的持續需求。憑藉超過 30 個工具的覆蓋範圍和近 30,000 個分支，它已成為比較不同 AI 產品如何被提示和配置的事實標準參考。

---

## 34. [awesome-software-design](https://github.com/QDenka/awesome-software-design)
> 透過模式、決策和經過驗證的設計規則來組織和結構化軟體

**Language:** N/A  |  **Stars:** 737  |  **Forks:** 48  |  **Best Score:** 2154  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2026-02-11

**背景：** Awesome Software Design 是由 QDenka 策劃的精選清單儲存庫，聚焦於軟體架構模式、架構決策記錄和經過驗證的設計原則。它於 2026 年 2 月 11 日推出——距本報告僅五天——且已顯示出足夠的流量出現在趨勢排名中。該儲存庫圍繞結構和決策框架而非特定技術來組織其內容。

**解決的問題：** 軟體設計知識分散在書籍、會議演講和品質參差不齊的部落格文章中。該儲存庫試圖將關於模式和設計決策的權威參考整合到單一結構化清單中，為工程師提供學習或重新審視架構概念的起點，而無需費力篩選低品質內容。

**為何又一個？** 其新鮮的發布日期意味著它仍在累積早期採用者的動能。對決策記錄和經過驗證的設計規則的聚焦——而非僅列出模式名稱——使其比架構領域中較舊的 awesome 清單更具實用導向，這可能解釋了其早期的關注度。

---

## 35. [daytona](https://github.com/daytonaio/daytona)
> Daytona 是一個用於運行 AI 生成程式碼的安全且彈性的基礎設施

**Language:** TypeScript  |  **Stars:** 59524  |  **Forks:** 5058  |  **Best Score:** 2139  |  **Best Rank:** #12  |  **Days on chart:** 1/7  |  **Created:** 2024-02-06

**背景：** Daytona 是一個可自行託管的開發環境管理平台，已演變為專門針對安全執行 AI 生成程式碼最佳化的基礎設施。它按需配置隔離的開發環境並管理其生命週期，最初專注於為人類開發者提供標準化的開發容器，後來轉向服務 AI 程式碼執行工作負載。該專案在兩年間累積了超過 59,000 顆星和大量的分支數。

**解決的問題：** 安全運行 AI 生成的程式碼需要具備受控網路存取、資源限制以及快速建立和銷毀能力的沙盒環境。Docker Compose 或 Kubernetes 等通用容器編排工具對於代理式工作流程所需的亞秒級配置來說過於笨重。Daytona 提供了一個專門建構的運行時層，具備 AI 編程代理執行不受信任程式碼所需的安全隔離和彈性。

**為何又一個？** Daytona 佔據了一個特定的利基：為 AI 程式碼執行而非人類開發工作流程提供基礎設施。隨著編程代理在生產管線中變得更加普遍，對與代理編排系統整合的專用、安全執行層的需求也在增長。該專案現有的星數使其保持在趨勢雷達上，而每一波對代理式編程工具的興趣都會為其部署方案帶來新使用者。

---

## 36. [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
> 一個為建構專業 UI/UX 提供設計智慧的 AI 技能

**Language:** Python  |  **Stars:** 33111  |  **Forks:** 3278  |  **Best Score:** 2131  |  **Best Rank:** #12  |  **Days on chart:** 1/7  |  **Created:** 2025-11-30

**背景：** ui-ux-pro-max-skill 是一個 AI 代理技能，可將設計系統意識和 UI/UX 最佳實務注入 Claude Code 和 Cursor 等編程助手中。它提供結構化的提示、元件模式庫以及針對網頁、行動裝置和桌面目標的平台特定設計指南。該技能以 Python 編寫，並與標準代理技能調用協定整合。

**解決的問題：** AI 編程助手生成的程式碼在功能上正確，但經常產生視覺不一致或無障礙性不足的介面。此技能透過將專業設計原則——間距、字體排版、色彩對比度和元件層級——編碼為代理可存取的上下文來彌補這一差距。沒有專屬設計師的開發者可以在調用編程助手時同時調用此技能，以產出更精緻的成果。

**為何又一個？** 通用的程式碼生成技能完全忽略設計，而專門的設計工具則運行在開發者的編程環境之外。此技能的獨特之處在於將設計智慧直接嵌入代理式編程循環中，而非將設計視為獨立的後續步驟。

---

## 37. [seerr](https://github.com/seerr-team/seerr)
> 面向 Jellyfin、Plex 和 Emby 的開源媒體請求和發現管理器。

**Language:** TypeScript  |  **Stars:** 9534  |  **Forks:** 624  |  **Best Score:** 2120  |  **Best Rank:** #12  |  **Days on chart:** 3/7  |  **Created:** 2022-03-09

**背景：** Seerr 是一個可自行託管的媒體請求和發現管理工具，與 Jellyfin、Plex 和 Emby 家庭媒體伺服器整合。它提供類似 Netflix 的發現介面，用於瀏覽和請求新內容，並透過 Sonarr 和 Radarr 支援自動化下載工作流程。該專案於 2022 年 3 月建立，透過家庭媒體伺服器社群已成長至超過 9,500 顆星。

**解決的問題：** 家庭媒體伺服器營運者通常需要手動處理家人和朋友的內容請求，然後自己排隊下載。Seerr 為非技術使用者提供精緻的請求介面，同時自動化執行流程——使用者請求一個標題，Seerr 便將其傳遞給適當的下載管理器，無需營運者介入。

**為何又一個？** Seerr 之所以獲得關注，是因為除了 Plex 和 Emby 外還支援 Jellyfin——一個完全開源的媒體伺服器，使其擁有比 Jellyseerr（僅限 Jellyfin）或 Overseerr（僅限 Plex）更廣泛的受眾。其統一的多伺服器支援是使其在家庭伺服器社群中保持能見度的主要差異化因素。

---

## 38. [qwen-code](https://github.com/QwenLM/qwen-code)
> 一個運行在終端機中的開源 AI 代理。

**Language:** TypeScript  |  **Stars:** 19129  |  **Forks:** 1657  |  **Best Score:** 2112  |  **Best Rank:** #13  |  **Days on chart:** 1/7  |  **Created:** 2025-06-26

**背景：** Qwen-code 是 QwenLM 的開源終端機編程代理，概念上類似於 Claude Code，但由 Qwen 模型系列驅動。它直接整合到開發者的終端機中，理解程式碼庫上下文，並能透過自然語言指令執行多步驟編程任務。於 2025 年 6 月發布，作為阿里雲圍繞 Qwen 模型建構完整開發者工具鏈的一部分，已累積超過 19,000 顆星。

**解決的問題：** 終端機編程代理一直由綁定特定模型供應商的專有產品主導，使用開放權重模型的開發者缺乏可比的工具。Qwen-code 提供相同類別的代理式編程能力——程式碼庫理解、檔案編輯、git 操作——但由可在本地運行或透過阿里雲 API 存取的模型支援。

**為何又一個？** 關鍵差異點在於與 Qwen 模型系列的緊密整合，包括本地託管的變體，這使得在無法使用 Anthropic 或 OpenAI API 的地區或組織中的開發者也能獲得可比的編程代理體驗。它同時也是 Qwen 函式呼叫和工具使用能力的參考實作，對基於這些模型進行開發的開發者很有用。

---

## 39. [stremio-web](https://github.com/Stremio/stremio-web)
> Stremio - 串流自由

**Language:** JavaScript  |  **Stars:** 9274  |  **Forks:** 1035  |  **Best Score:** 1966  |  **Best Rank:** #9  |  **Days on chart:** 1/7  |  **Created:** 2018-06-04

**背景：** Stremio 是一個媒體中心應用程式，將來自多個串流服務和種子來源的內容聚合到統一介面中。stremio-web 儲存庫是 Stremio 平台的網頁前端，以 JavaScript 建構，於 2018 年 6 月首次發布。該專案已累積超過 9,000 顆星，並支援廣泛的內容發現附加元件生態系統。

**解決的問題：** 訂閱多個串流服務的使用者必須在不同的應用程式之間切換來尋找和觀看內容，沒有統一的搜尋或媒體庫檢視。Stremio 將多個來源的目錄聚合到單一介面中，使用者可以在此搜尋、發現和串流內容，不受來源限制。

**為何又一個？** Stremio 持續上榜是因為其附加元件架構允許社群在不修改核心應用程式的情況下擴展內容來源。與專注於本地託管媒體庫的 Plex 或 Jellyfin 不同，Stremio 的設計目標是聚合外部串流來源。網頁客戶端使任何有瀏覽器的裝置都能存取，無需安裝原生應用程式。

---

## 40. [evershop](https://github.com/evershopcommerce/evershop)
> TypeScript 電商平台

**Language:** TypeScript  |  **Stars:** 9479  |  **Forks:** 2145  |  **Best Score:** 1964  |  **Best Rank:** #12  |  **Days on chart:** 1/7  |  **Created:** 2021-05-06

**背景：** EverShop 是一個完全以 TypeScript 建構的開源電商平台，於 2021 年 5 月推出。它提供完整的線上商店解決方案，包含產品管理、訂單處理和模組化擴展系統。該平台使用 GraphQL API，設計上同時面向想要自訂的開發者和需要生產就緒店面的商家。

**解決的問題：** 大多數開源電商平台（WooCommerce、Magento、PrestaShop）以 PHP 建構，這對以 JavaScript/TypeScript 為主的開發團隊造成摩擦。EverShop 提供完整的 TypeScript 電商技術棧，消除了語言切換的需要，使團隊能在前端和後端之間共享程式碼和工具。

**為何又一個？** TypeScript 原生的方法是與成熟的 PHP 電商平台的主要差異化因素，而模組化擴展架構則與 Medusa 或 Saleor 等可能需要更多自訂開發的較新 Node.js 替代方案有所區別。EverShop 瞄準的是中間地帶——既足夠有主見以快速部署，又透過其模組系統保持可擴展性。

---

## 41. [pyrite64](https://github.com/HailToDodongo/pyrite64)
> 使用 libdragon 和 tiny3d 的 N64 遊戲引擎和編輯器

**Language:** C++  |  **Stars:** 2221  |  **Forks:** 86  |  **Best Score:** 1961  |  **Best Rank:** #15  |  **Days on chart:** 2/7  |  **Created:** 2025-09-23

**背景：** pyrite64 是一個建構在 libdragon 開源 N64 SDK 和 tiny3d 渲染函式庫之上的 Nintendo 64 遊戲引擎及配套編輯器。以 C++ 編寫，它在原始 SDK 之上提供了結構化的引擎層，包括場景管理、資產管線工具和用於組裝遊戲內容的互動式編輯器。該專案面向希望獲得比裸 libdragon 更高層級框架的業餘 N64 自製遊戲開發者。

**解決的問題：** 僅使用 libdragon 為 N64 開發需要為場景管理、資產載入和渲染管線編寫大量樣板程式碼。pyrite64 將這些抽象為可重用的引擎，減少新自製遊戲專案的設定時間，讓開發者能專注於遊戲邏輯而非硬體層面的管線工程。

**為何又一個？** 隨著 libdragon 的成熟和 tiny3d 作為實用 3D 渲染函式庫的發布，N64 自製遊戲場景重新獲得了關注。pyrite64 是第一個建構在這些現代基礎之上並配備編輯器的引擎，填補了原始 SDK 使用和完整遊戲開發之間的空白。

---
## 42. [claude-quickstarts](https://github.com/anthropics/claude-quickstarts)
> 一系列幫助開發者快速上手 Claude API 的專案

**Language:** Python  |  **Stars:** 14715  |  **Forks:** 2455  |  **Best Score:** 1950  |  **Best Rank:** #13  |  **Days on chart:** 3/7  |  **Created:** 2024-08-29

**背景：** Claude Quickstarts 是 Anthropic 官方維護的入門專案集，專為使用 Claude API 建構生產級應用的開發者所設計。每個 quickstart 涵蓋一個特定使用場景——RAG 管線、工具使用、多輪代理、文件分析——提供完整、可執行的 Python 程式碼與部署指引。此儲存庫由 Anthropic 維護，並隨新的 API 功能同步更新。

**解決的問題：** 評估 Claude API 的開發者經常難以快速從文件閱讀轉變為可運作、可部署的原型。這些 quickstarts 提供完整的端到端範例，展示上下文管理、錯誤處理與生產部署模式的最佳實踐，將從取得 API 金鑰到完成可運作應用的時間從數天縮短至數小時。

**為何又一個？** 隨著 Anthropic 發布新的 Claude 模型與 API 功能，quickstarts 儲存庫會同步更新以展示這些功能，從而產生反覆的趨勢事件。每次新功能公告都會驅使開發者回到這個儲存庫尋找標準使用範例。

---

## 43. [wifi-densepose](https://github.com/ruvnet/wifi-densepose)
> 基於 WiFi 的密集人體姿態估計系統，可透過牆壁進行即時全身追蹤

**Language:** Python  |  **Stars:** 7201  |  **Forks:** 609  |  **Best Score:** 1931  |  **Best Rank:** #13  |  **Days on chart:** 2/7  |  **Created:** 2025-06-07

**背景：** WiFi-DensePose 是 InvisPose 的 Python 實作，這是一個利用 WiFi 訊號擾動而非攝影機來估計密集人體姿態的系統。它處理來自一般 mesh 路由器的通道狀態資訊（CSI），以透過牆壁及低光環境追蹤全身動作。該專案標榜已達生產就緒狀態，並附帶前處理、推論及視覺化管線。

**解決的問題：** 基於攝影機的人體姿態估計需要視線直達、充足光線，且會引發重大隱私疑慮。基於 WiFi 的追蹤可穿透牆壁、在黑暗中運作，且無需任何可見感測器——適用於跌倒偵測、智慧家庭自動化及安全監控等攝影機部署不切實際或不可接受的應用場景。

**為何又一個？** WiFi 姿態估計的研究實作過去一直難以取得——需要客製硬體或專有的 CSI 擷取工具。此專案以一般 mesh 路由器為目標，強調生產就緒性，讓沒有專業射頻硬體背景的開發者與研究人員也能輕鬆上手。

---

## 44. [gogcli](https://github.com/steipete/gogcli)
> Google Suite CLI：Gmail、GCal、GDrive、GContacts。

**Language:** Go  |  **Stars:** 4410  |  **Forks:** 344  |  **Best Score:** 1926  |  **Best Rank:** #14  |  **Days on chart:** 2/7  |  **Created:** 2025-12-12

**背景：** GoGCLI 是由 Peter Steinberger（steipete）以 Go 語言撰寫的 Google Workspace 套件命令列介面——涵蓋 Gmail、Google 日曆、Google 雲端硬碟及 Google 聯絡人。它為偏好鍵盤驅動工作流程或需要腳本化操作 Google 帳戶的開發者與進階使用者提供終端優先的存取方式。該專案於 2025 年 12 月推出，已累積超過 4,400 顆星。

**解決的問題：** Google 的網頁應用需要瀏覽器且沒有原生的腳本化介面，使得常見任務的自動化——如封存郵件、批量建立日曆事件、查詢聯絡人——變得不必要地困難。GoGCLI 透過一致的 CLI 介面公開這些服務，實現 shell 腳本化、cron 排程自動化，以及與其他終端工具的整合。

**為何又一個？** 現有的 Google API 客戶端是特定語言的 SDK，需要撰寫程式碼而非直接下達指令。GoGCLI 以單一編譯二進位檔填補了直接 CLI 的空缺，涵蓋四個最常用的 Workspace 服務，無需任何樣板程式碼即可立即使用。

---

## 45. [KittenTTS](https://github.com/KittenML/KittenTTS)
> 小於 25MB 的最先進 TTS 模型

**Language:** Python  |  **Stars:** 10384  |  **Forks:** 559  |  **Best Score:** 1895  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2025-08-05

**背景：** KittenTTS 是 KittenML（隸屬 Stellon Labs）推出的開源文字轉語音模型系列，專為極致輕量部署設計。旗艦 nano 模型擁有 1,500 萬參數，其 int8 量化版本僅 25MB，可在任何 CPU 上部署而無需 GPU。該專案提供四個模型層級——mini（80M）、micro（40M）、nano（15M）及 nano-int8——並在 Hugging Face Spaces 上提供展示。

**解決的問題：** 大多數高品質的開源 TTS 模型需要數 GB 的權重和 GPU 推論才能達到可接受的延遲。KittenTTS 瞄準相反的約束條件：儲存空間、記憶體或運算能力有限的裝置，如 IoT 硬體、行動裝置或邊緣伺服器。

**為何又一個？** 該模型系列填補了玩具級 TTS 系統（可理解但機械化）與全規模模型（如 XTTS 或 Kokoro，品質高但體積大）之間的空缺。KittenTTS 宣稱在 25MB 以下的規模層級達到最先進品質，並提供多種優質語音選項，而非單一預設說話者。

---

## 46. [agent-zero](https://github.com/agent0ai/agent-zero)
> Agent Zero AI 框架

**Language:** Python  |  **Stars:** 14953  |  **Forks:** 3105  |  **Best Score:** 1892  |  **Best Rank:** #15  |  **Days on chart:** 1/7  |  **Created:** 2024-06-10

**背景：** Agent Zero 是 agent0ai 開發的基於 Python 的 AI 代理框架，提供通用型腳手架，用於建構能使用工具、產生子代理並在任務間維持記憶的自主代理。自 2024 年 6 月推出以來，已成長至近 15,000 顆星與近 3,100 個 fork，反映出社群的大量使用與客製化。它支援多種底層模型，並公開靈活的工具使用與通訊層，用於代理編排。

**解決的問題：** 從零開始建構有能力的 AI 代理需要實作工具執行、記憶管理、子代理委派及錯誤恢復等功能。Agent Zero 將這些基礎功能作為可組合的框架提供，讓開發者能專注於定義代理應該做什麼，而非如何管理其自身的執行。

**為何又一個？** Agent Zero 以其對透明度和可修改性的強調而與眾不同——該框架刻意保持精簡和可讀性，比 AutoGen 或 CrewAI 等較重的替代方案更容易理解和修改。它持續出現在趨勢榜上，反映了社群對輕量、可擴展代理框架的持續興趣。

---

## 47. [awesome](https://github.com/sindresorhus/awesome)
> 關於各種有趣主題的 awesome 清單

**Language:** N/A  |  **Stars:** 439784  |  **Forks:** 33277  |  **Best Score:** 1867  |  **Best Rank:** #13  |  **Days on chart:** 1/7  |  **Created:** 2014-07-11

**背景：** Sindre Sorhus 的 awesome 儲存庫是催生整個 GitHub「awesome 清單」慣例的根元清單，創建於 2014 年 7 月。它是一個精選索引，涵蓋程式語言、框架、平台、開發者工具、理論、媒體等其他精選清單。擁有近 439,000 顆星，它是 GitHub 上星數最多的儲存庫之一。

**解決的問題：** 在 awesome 清單模式出現之前，GitHub 上沒有社群維護的主題索引的一致慣例。此儲存庫建立了格式和品質標準（含徽章），數千個下游 awesome 清單現在都遵循此標準，使其成為探索任何技術主題精選資源的標準入口點。

**為何又一個？** 此儲存庫週期性地登上趨勢榜，因為它是權威的元索引——每個獲得關注的新 awesome 清單都會連結回它，每個第一次發現此模式的開發者都會為原始儲存庫加星。它的年齡（超過 11 年）和星數使其實際上已成為 GitHub 知識圖譜的基礎設施，而非與替代方案競爭的專案。

---

## 48. [FineTune](https://github.com/ronitsingh10/FineTune)
> FineTune，一款 macOS 選單列應用程式，用於逐應用程式音量控制、多裝置輸出、音訊路由及 10 段等化器。

**Language:** Swift  |  **Stars:** 2785  |  **Forks:** 93  |  **Best Score:** 1863  |  **Best Rank:** #14  |  **Days on chart:** 1/7  |  **Created:** 2026-01-18

**背景：** FineTune 是一款以 Swift 撰寫的免費、開源 macOS 選單列應用程式，提供逐應用程式音量控制、多裝置音訊輸出、音訊路由及 10 段等化器。它定位為 Rogue Amoeba 的 SoundSource（一款付費商業應用）的免費替代方案。該專案於 2026 年 1 月推出，已迅速累積近 2,800 顆星。

**解決的問題：** macOS 預設僅提供系統全域音量控制，沒有內建方式為個別應用程式設定不同音量或將特定應用程式路由到不同的音訊輸出裝置。SoundSource 解決了這個問題但需要付費。FineTune 免費提供相同的逐應用程式音訊控制功能。

**為何又一個？** 主要吸引力在於它是知名付費工具的免費開源替代方案。SoundSource 售價 39 美元且為閉源；FineTune 提供同等功能——逐應用程式音量、多裝置輸出、音訊路由及等化——且無需授權費。選單列整合遵循 macOS 使用者對音訊工具的一貫 UX 模式。

---

## 49. [Mole](https://github.com/tw93/Mole)
> 深度清理並優化你的 Mac。

**Language:** Shell  |  **Stars:** 35825  |  **Forks:** 971  |  **Best Score:** 1829  |  **Best Rank:** #12  |  **Days on chart:** 1/7  |  **Created:** 2025-09-23

**背景：** Mole 是 tw93 創建的 macOS 系統清理與優化工具，以 Shell 撰寫，於 2025 年 9 月發布。它執行快取、日誌、暫存檔及其他隨時間累積而拖慢 macOS 的系統碎片的深度清理。該專案已成長至超過 35,000 顆星。

**解決的問題：** macOS 會因應用程式快取、系統日誌、Xcode 衍生資料、Homebrew 快取及其他暫存檔而累積大量磁碟空間使用，這些不會被自動清理。CleanMyMac 等商業工具需要訂閱費才能提供此功能。Mole 以免費、開源的 shell 腳本形式提供相同的深度清理功能，使用者可自行審計。

**為何又一個？** 作為透明的 shell 腳本而非編譯的二進位檔是關鍵的信任差異化因素——使用者可以在執行前確切閱讀哪些內容會被刪除。這解決了需要廣泛檔案系統存取權限的系統清理工具固有的信任問題。開源方式也意味著社群可以為新應用程式新增清理目標，無需等待廠商更新。

---

## 50. [posthog](https://github.com/PostHog/posthog)
> PostHog 是一個為建構成功產品而設計的一體化開發者平台。

**Language:** Python  |  **Stars:** 31713  |  **Forks:** 2317  |  **Best Score:** 1828  |  **Best Rank:** #13  |  **Days on chart:** 1/7  |  **Created:** 2020-01-23

**背景：** PostHog 是一個開源、一體化的產品分析平台，將產品分析、網站分析、會話回放、錯誤追蹤、功能旗標、實驗、問卷調查、資料倉儲、CDP 及 AI 產品助手整合在一個可自行架設的產品中。創立於 2020 年 1 月，已成長至超過 31,000 顆星，作為 Amplitude、Mixpanel、LaunchDarkly 和 Hotjar 組合的自行架設替代方案。

**解決的問題：** 產品團隊通常需要拼湊多個 SaaS 工具來實現分析、會話回放、功能旗標和實驗功能，造成資料孤島並增加廠商成本。PostHog 將這些功能整合在一個具有統一資料模型的平台中，減少整合複雜度並確保所有產品資料集中在一處。

**為何又一個？** PostHog 持續登上趨勢榜，因為它不斷擴展產品範圍——在原始分析核心之上新增錯誤追蹤、資料倉儲和 AI 助手。自行架設選項吸引有資料主權要求的公司，開源模式則允許社群貢獻整合。每次新功能公告都帶來新的曝光。

---

## 51. [opencode](https://github.com/anomalyco/opencode)
> 開源的程式碼編寫代理。

**Language:** TypeScript  |  **Stars:** 107795  |  **Forks:** 10640  |  **Best Score:** 1782  |  **Best Rank:** #14  |  **Days on chart:** 1/7  |  **Created:** 2025-04-30

**背景：** OpenCode 是由 Anomaly 開發的開源終端程式碼編寫代理，於 2025 年 4 月推出。它提供在終端中運作的代理式程式碼助手，能理解程式碼庫並透過自然語言指令執行開發任務。擁有超過 107,000 顆星，它是 GitHub 上最受歡迎的開源程式碼編寫代理之一。

**解決的問題：** 開發者需要能融入現有終端工作流程的 AI 程式碼輔助，而不被綁定在特定的 IDE 或廠商上。OpenCode 提供了專有程式碼編寫代理的完全開源替代方案，讓使用者在保有終端原生便利性的同時，擁有檢視、修改及自行架設整個系統的自由。

**為何又一個？** OpenCode 持續登上趨勢榜，因為它佔據了專有程式碼編寫代理的開源對應位置。其完全開放的程式碼庫允許社群新增模型後端、自訂行為及建構擴充功能，無需廠商批准。107,000 顆星的里程碑反映了對透明、社群驅動的程式碼編寫代理的需求。

---

## 52. [nautilus_trader](https://github.com/nautechsystems/nautilus_trader)
> 高效能的演算法交易平台與事件驅動回測引擎

**Language:** Rust  |  **Stars:** 20083  |  **Forks:** 2356  |  **Best Score:** 1749  |  **Best Rank:** #14  |  **Days on chart:** 2/7  |  **Created:** 2018-06-25

**背景：** Nautilus Trader 是由 Nautech Systems 開發的高效能演算法交易平台與事件驅動回測引擎，其效能關鍵元件以 Rust 實作，使用者端 API 則透過 Python 公開。自 2018 年 6 月起開發，已成長至超過 20,000 顆星，是目前最成熟的開源演算法交易框架之一。它支援跨多個交易所的實盤交易，以及微秒級解析度事件回放的歷史回測。

**解決的問題：** 準確回測交易策略需要事件驅動模擬，忠實重現市場事件的順序，包括部分成交、延遲和市場衝擊。大多數開源回測框架使用向量化運算來近似此行為。Nautilus Trader 的事件驅動架構提供更高保真度的模擬，縮小回測與實盤表現之間的差距。

**為何又一個？** Nautilus Trader 的 Rust 核心賦予它純 Python 替代方案無法匹敵的效能特性——微秒級事件處理、低 GC 壓力。其長期開發歷史（自 2018 年活躍至今）和持續的功能新增，意味著它不斷吸引需要生產級工具而非研究原型的專業量化開發者的關注。

---

## 53. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> OpenClaw Skills 的精選集合。

**Language:** N/A  |  **Stars:** 17555  |  **Forks:** 1799  |  **Best Score:** 1739  |  **Best Rank:** #16  |  **Days on chart:** 6/7  |  **Created:** 2026-01-25

**背景：** Awesome OpenClaw Skills 是由 VoltAgent 維護的社群建構 OpenClaw AI 助手平台技能精選集。該專案經歷兩次更名——最初為 Clawdbot，然後是 Moltbot——最終改為現名以配合 OpenClaw 生態系統。它於 2026 年 1 月下旬推出，已累積超過 17,500 顆星，反映出 OpenClaw 社群的快速成長。

**解決的問題：** OpenClaw 是一個強大的個人助手平台，但建構自訂技能需要了解其外掛 API 和提示工程慣例。此集合提供現成的、經社群測試的技能，使用者可直接安裝，降低了從零開始撰寫技能來擴展 OpenClaw 新功能的門檻。

**為何又一個？** 該專案的發展歷程——從 Clawdbot 到 Moltbot 再到現有形式——反映了它與 OpenClaw 平台本身的共同演進。隨著 OpenClaw 成長為最多星數的個人助手平台之一，對標準技能儲存庫的需求也隨之增長，使此集合在趨勢榜上持續保持顯著位置。

---

## 54. [FossFLOW](https://github.com/stan-smith/FossFLOW)
> 製作精美的等角投影基礎設施圖表

**Language:** TypeScript  |  **Stars:** 17565  |  **Forks:** 1147  |  **Best Score:** 1726  |  **Best Rank:** #15  |  **Days on chart:** 1/7  |  **Created:** 2025-06-30

**背景：** FossFLOW 是一個以 TypeScript 建構的開源等角投影基礎設施圖表製作工具。它提供視覺化介面，用於產生雲端基礎設施文件、DevOps 簡報及系統設計討論中常用的精美三維架構圖。該專案自 2025 年 6 月推出以來已成長至超過 17,500 顆星。

**解決的問題：** 建立專業的等角投影基礎設施圖通常需要昂貴的設計軟體（Figma、Illustrator）加上手動繪圖技能，或匯出選項有限的專有圖表工具。FossFLOW 自動化等角投影渲染，讓使用者專注於描述其基礎設施而非繪製它。

**為何又一個？** 雖然 draw.io 和 Excalidraw 等工具支援通用圖表繪製，但它們並不專精於等角投影基礎設施視圖。FossFLOW 對等角投影渲染的專注使其在這個特定使用場景下產生比通用圖表工具更精美的輸出，且開源特性使其與 Cloudcraft 等商業替代方案形成差異化。

---

## 55. [freemocap](https://github.com/freemocap/freemocap)
> 人人皆可用的免費動態捕捉

**Language:** Python  |  **Stars:** 5617  |  **Forks:** 444  |  **Best Score:** 1721  |  **Best Rank:** #15  |  **Days on chart:** 2/7  |  **Created:** 2021-04-12

**背景：** FreeMoCap 是一個開源的無標記動態捕捉系統，使用標準網路攝影機和電腦視覺來記錄 3D 骨骼運動資料，無需專用硬體。以 Python 建構，使用 MediaPipe 進行姿態估計，使用 Anipose 進行多攝影機 3D 三角測量，輸出與 Blender、Unity 及生物力學分析工具相容的格式。該專案目標對象為無法負擔商業動態捕捉系統的研究人員、教育工作者及獨立動畫師。

**解決的問題：** 專業動態捕捉需要使用標記服裝搭配成本數萬美元的紅外線攝影機陣列，或同樣昂貴的高階無標記系統。FreeMoCap 使用排列成多攝影機設置的消費級網路攝影機，實現精確的全身動態捕捉，使此功能觸及預算有限的大學實驗室、獨立遊戲開發者及臨床研究人員。

**為何又一個？** Theia3D 和 Vicon Shogun 等商業無標記動態捕捉系統的定價是針對電影製作預算。FreeMoCap 是最完整的開源替代方案，擁有活躍的開發、完整的校準工作流程文件，以及直接的 Blender 整合使其可立即用於動畫。隨著動畫和生物力學社群的新使用者發現它能以已有的硬體產出可用成果，它反覆登上趨勢榜。

---

## 56. [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
> 透過從零重建你喜愛的技術來精通程式設計。

**Language:** Markdown  |  **Stars:** 467978  |  **Forks:** 43866  |  **Best Score:** 1675  |  **Best Rank:** #16  |  **Days on chart:** 2/7  |  **Created:** 2018-05-09

**背景：** Build Your Own X 是 GitHub 上星數最多的儲存庫之一，精選了以各種語言從零重新實作知名技術——資料庫、編譯器、作業系統、網頁伺服器——的教學。該集合按技術類別組織，連結至高品質的外部教學。它由 Codecrafters 維護，既是社群資源，也是其付費互動課程的配套。

**解決的問題：** 想深入了解基礎技術如何運作的開發者，往往難以找到教科書以外的結構化、高品質學習資源。此儲存庫提供了一個通往實作教學的單一入口點，這些教學能建立真正的內部原理知識。「透過建構來理解」的理念比單純閱讀文件產生更持久的學習效果。

**為何又一個？** 擁有近 468,000 顆星的此儲存庫持續登上趨勢榜，因為新開發者不斷發現它，且隨著技術演進持續有新教學加入。它是全球程式設計學習社群中的常年推薦資源。

---

## 57. [awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
> 讓生活更便利的 OpenClaw 使用案例社群集合。

**Language:** N/A  |  **Stars:** 4893  |  **Forks:** 353  |  **Best Score:** 1656  |  **Best Rank:** #17  |  **Days on chart:** 1/7  |  **Created:** 2026-02-08

**背景：** Awesome OpenClaw Usecases 是 Hesam Sheikh 彙整的社群精選 OpenClaw 個人 AI 助手實際使用案例集合，於 2026 年 2 月初推出。它記錄了人們使用 OpenClaw 的技能和多通道架構所建構的真實應用，按類別組織。該儲存庫在短短兩週內已迅速累積近 5,000 顆星。

**解決的問題：** OpenClaw 在其 ClawHub 登錄檔中擁有超過 5,700 個技能，但發現哪些技能組合能解決特定的真實問題需要反覆嘗試。此集合提供已記錄、已測試的使用案例，展示如何結合 OpenClaw 功能來完成實際任務，減少試錯式的探索過程。

**為何又一個？** 雖然 awesome-openclaw-skills 以安全審查的方式編錄個別技能，此儲存庫聚焦於將多個技能組合成工作流程的完整使用案例配方。這是工具目錄（技能）與食譜書（使用案例）之間的區別，服務那些知道想達成什麼但不知該組合哪些工具的使用者。

---

## 58. [opencti](https://github.com/OpenCTI-Platform/opencti)
> 開放式網路威脅情報平台

**Language:** TypeScript  |  **Stars:** 8848  |  **Forks:** 1258  |  **Best Score:** 1641  |  **Best Rank:** #16  |  **Days on chart:** 2/7  |  **Created:** 2018-12-17

**背景：** OpenCTI 是由 Filigran 開發的開源網路威脅情報平台，最初於 2018 年 12 月推出。它提供結構化環境，用於使用 STIX 2.1 標準來擷取、儲存、關聯及分享威脅情報。該平台包含基於圖形的知識庫、用於整合外部威脅來源的連接器生態系統，以及供多團隊使用的角色基礎存取控制。

**解決的問題：** 從多個來源取得威脅情報的安全團隊面臨跨來源關聯指標、維護威脅行為者和 TTP 的結構化知識圖譜，以及以標準化格式與合作夥伴分享發現等挑戰。OpenCTI 提供一個無需商業 TIP 訂閱即可完成所有這些功能的單一平台。

**為何又一個？** OpenCTI 已確立自身為領先的開源威脅情報平台，隨著新連接器的發布以及組織標準化基於 STIX 的情報工作流程而週期性地登上趨勢榜。其由 Filigran 支持的活躍開發和廣泛的連接器生態系統，使得後來者難以取代它。

---

## 59. [pinchtab](https://github.com/pinchtab/pinchtab)
> 高效能瀏覽器自動化橋接與多實例編排器

**Language:** Go  |  **Stars:** 1086  |  **Forks:** 53  |  **Best Score:** 1592  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2026-02-15

**背景：** Pinchtab 是一個非常新近發布的基於 Go 的瀏覽器自動化橋接器，設計用於同時編排多個瀏覽器實例，並具備進階隱匿功能以避開機器人偵測。它提供即時儀表板來監控自動化會話，並公開 API 用於程式化控制瀏覽器叢集。該專案於 2026 年 2 月 15 日建立，已在發布數天內吸引超過 1,000 顆星。

**解決的問題：** Playwright 和 Puppeteer 是主流的瀏覽器自動化工具，但經常被反機器人系統偵測和封鎖，因為它們以可預測的方式修改瀏覽器指紋。Pinchtab 專門聚焦於隱匿注入——操縱瀏覽器內部以擊敗指紋偵測——並新增了這些函式庫原生缺乏的多實例編排層，使其適合大規模自動化任務。

**為何又一個？** Go 實作使每個瀏覽器實例的資源開銷顯著低於基於 Node.js 的編排器，這在管理數十個同時瀏覽器會話時非常重要。整合的即時儀表板也填補了現有工具的空缺，現有工具通常需要第三方監控才能大規模觀察自動化會話。其極短的歷史和高分表明了快速的有機發現。

---

## 60. [claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
> 官方、由 Anthropic 管理的高品質 Claude Code 外掛目錄。

**Language:** Python  |  **Stars:** 7985  |  **Forks:** 781  |  **Best Score:** 1588  |  **Best Rank:** #16  |  **Days on chart:** 1/7  |  **Created:** 2025-11-20

**背景：** Claude Plugins Official 是 Anthropic 精選的高品質 Claude Code 外掛目錄，於 2025 年 11 月推出。它作為擴展 Claude Code 功能的官方、經審查外掛集合，每個外掛都經過 Anthropic 的品質和安全標準審查與維護。該儲存庫已累積近 8,000 顆星。

**解決的問題：** 不斷成長的社群建構 Claude Code 外掛生態系統在品質、安全性和維護方面差異很大。此官方目錄提供一個受信任的來源，使用者可在此找到經 Anthropic 審查的外掛，降低安裝維護不善或潛在惡意擴充功能的風險。

**為何又一個？** 作為 Anthropic 官方管理的目錄，它提供了社群維護清單無法保證的信任度和品質保證。每個外掛都經過安全審查並測試與當前 Claude Code 版本的相容性，解決了與官方應用商店為行動平台解決的相同信任差距。

---

## 61. [SparkyFitness](https://github.com/CodeWithCJ/SparkyFitness)
> SparkyFitness：為家庭打造，由 AI 驅動。一起追蹤食物、健身、飲水和健康。

**Language:** TypeScript  |  **Stars:** 2447  |  **Forks:** 114  |  **Best Score:** 1534  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2025-06-21

**背景：** SparkyFitness 是一個以 TypeScript 建構的 AI 驅動家庭健康追蹤應用程式。它提供食物攝取、健身活動、飲水量和一般健康指標的協作追蹤，專為家庭使用而非個人使用者所設計。該應用使用 AI 協助膳食記錄、營養分析和健身建議。

**解決的問題：** 大多數健康和健身追蹤應用是為個人使用設計的，缺乏共享的家庭功能。試圖一起改善健康的家庭必須各自使用沒有共享可見性的獨立應用程式。SparkyFitness 提供一個統一的平台，家庭成員可以協作追蹤和查看彼此的健康資料。

**為何又一個？** 家庭優先的設計是與 MyFitnessPal、Cronometer 或 Apple Health 等成熟應用的主要差異化因素，這些應用都以個人為中心。AI 驅動的食物記錄和營養分析降低了技術不熟練家庭成員的使用門檻，開源特性則允許注重隱私的家庭自行架設以完全掌控其健康資料。

---

## 62. [moonshine](https://github.com/moonshine-ai/moonshine)
> 適用於邊緣裝置的快速且精確的自動語音辨識（ASR）

**Language:** C  |  **Stars:** 4265  |  **Forks:** 212  |  **Best Score:** 1527  |  **Best Rank:** #17  |  **Days on chart:** 1/7  |  **Created:** 2024-10-04

**背景：** Moonshine 是 Moonshine AI 開發的以 C 語言實作的自動語音辨識引擎，專門針對運算資源受限的邊緣裝置進行優化。它設計可在 Raspberry Pi、微控制器和嵌入式 Linux 開發板等硬體上運行，同時提供與更重量級模型相競爭的精確度。該專案於 2024 年 10 月推出，已成長至超過 4,200 顆星。

**解決的問題：** 雲端 ASR 服務會引入延遲、需要網路連線，且因將音訊傳輸至裝置外而引發隱私疑慮。在邊緣硬體上運行 Whisper 等模型雖然可行，但在未經仔細優化的情況下速度很慢。Moonshine 在運行完整神經網路本不切實際的裝置上提供快速、精確的本地轉錄。

**為何又一個？** Moonshine 的 C 語言實作——而非使用原生擴充的 Python——意味著它可以在缺乏 Python 運行環境的目標上編譯和部署。這使其在裸機嵌入式系統上真正可用，而競爭對手的邊緣 ASR 專案根本無法在這些系統上運行。

---

## 63. [tambo](https://github.com/tambo-ai/tambo)
> React 的生成式 UI SDK

**Language:** TypeScript  |  **Stars:** 10829  |  **Forks:** 525  |  **Best Score:** 1517  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2024-06-15

**背景：** Tambo 是由 tambo-ai 開發的 TypeScript SDK，能在 React 應用程式中實現生成式 UI 模式，讓 AI 模型根據自然語言或結構化模型輸出動態組合並渲染 UI 元件。它於 2024 年 6 月推出，透過在語言模型輸出與 React 元件樹之間建立實用的橋樑，已成長至超過 10,000 顆星。

**解決的問題：** 在 React 應用程式中顯示 AI 生成的內容，通常需要手動解析模型輸出並將其對應到元件——這是一個脆弱且高度客製化的過程。Tambo 提供結構化的 SDK 來處理元件選擇與渲染邏輯，讓開發者宣告可用的元件，並讓模型根據上下文決定如何組合它們。

**為何又一個？** 生成式 UI 是一種新興模式，目前尚無主導的開源解決方案。Tambo 專門針對 React——最廣泛使用的 UI 框架——並提供以生產為導向的 SDK，而非研究原型，這使其對希望在不自行建構整合層的情況下交付 AI 驅動介面的產品團隊具有實際吸引力。

---

## 64. [apkstudio](https://github.com/vaibhavpandeyvpz/apkstudio)
> 開源、跨平台的 Qt6 IDE，用於逆向工程 Android 應用程式套件。

**Language:** C++  |  **Stars:** 3722  |  **Forks:** 619  |  **Best Score:** 1517  |  **Best Rank:** #16  |  **Days on chart:** 1/7  |  **Created:** 2014-09-09

**背景：** APKStudio 是一個基於 Qt6 的跨平台 C++ IDE，提供圖形介面來反編譯、檢視、修改和重新編譯 Android APK 套件。它將 apktool 和 jadx 等命令列工具整合到一個統一的桌面應用程式中。該專案自 2014 年以來持續開發，在行動安全研究人員和開發者中累積了穩定的使用者群。

**解決的問題：** Android 逆向工程傳統上需要串接多個帶有複雜參數的命令列工具，並手動管理檔案。APKStudio 將工作流程整合到單一 GUI 應用程式中，具備專案管理、語法高亮和整合式建構控制。這大幅降低了需要檢視或修補 APK 的安全分析師和開發者的門檻。

**為何又一個？** Qt6 遷移和持續維護使 APKStudio 在與新工具的競爭中保持優勢。它的上榜反映了行動安全從業者的週期性重新發現——他們偏好原生桌面 GUI 而非網頁版或純終端機替代方案。

---

## 65. [get-shit-done](https://github.com/gsd-build/get-shit-done)
> 用於 Claude Code 和 OpenCode 的 meta-prompting、上下文工程及規格驅動開發系統。

**Language:** JavaScript  |  **Stars:** 17523  |  **Forks:** 1588  |  **Best Score:** 1432  |  **Best Rank:** #19  |  **Days on chart:** 2/7  |  **Created:** 2025-12-14

**背景：** Get-Shit-Done（GSD）是一個基於 JavaScript 的 meta-prompting 和上下文工程系統，專為 Claude Code 和 OpenCode 設計，圍繞規格驅動開發原則建構。它提供結構化的工作流程：開發者先撰寫規格，然後使用 GSD 的提示範本和上下文管理來引導 AI 編碼代理完成實作。該專案於 2025 年 12 月推出，迅速累積超過 17,000 顆星。

**解決的問題：** 沒有結構化輸入的 AI 編碼代理往往會隨意解讀需求，產生偏離原始意圖的實作。GSD 透過精心設計的上下文和 meta-prompt 來強制執行規格優先的工作流程，約束代理的行為，提高複雜多步驟開發任務輸出的可靠性。

**為何又一個？** GSD 專注於上下文工程——即結構化模型看到什麼資訊以及何時看到的技藝——這使其有別於專注於工具呼叫的技能框架。其輕量的 JavaScript 實作使其易於整合到現有的 Claude Code 或 OpenCode 設定中，無需沉重的依賴負擔。

---

## 66. [nanobot](https://github.com/HKUDS/nanobot)
> nanobot：超輕量 OpenClaw

**Language:** Python  |  **Stars:** 22520  |  **Forks:** 3492  |  **Best Score:** 1430  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2026-02-01

**背景：** nanobot 是由 HKUDS 開發的 OpenClaw AI 助理框架超輕量 Python 實作。它將 OpenClaw 功能集精簡到最小可行核心，針對完整 OpenClaw 堆疊太過笨重而無法部署的環境。該專案於 2026 年 2 月初推出，迅速在邊緣 AI 和資源受限部署社群中獲得關注。

**解決的問題：** 完整的 OpenClaw 執行環境有大量依賴和資源需求，使其不適用於嵌入式系統、最小化 Docker 容器和無伺服器函式。nanobot 以純 Python 和最少依賴實作 OpenClaw 的核心介面，使技能相容性在無需完整堆疊開銷的情況下得以實現。這使得 OpenClaw 技能可移植到以前被排除在生態系統之外的環境。

**為何又一個？** 隨著 OpenClaw 功能和複雜度的增長，輕量級相容層對於大量資源受限的部署場景變得越來越有價值。nanobot 填補了這個利基市場，同時維持技能 API 相容性，避免了為不同執行環境重寫技能的需求。

---

## 67. [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)
> 最佳代理框架

**Language:** TypeScript  |  **Stars:** 32679  |  **Forks:** 2466  |  **Best Score:** 1430  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2025-12-03

**背景：** Oh My OpenCode 是由 code-yeongyu 以 TypeScript 建構的社群驅動 OpenCode 編碼代理配置和外掛框架。其概念類似於 Zsh shell 的 oh-my-zsh，提供精選的主題、外掛和配置集合來增強 OpenCode 體驗。該專案於 2025 年 12 月推出，已成長至超過 32,000 顆星。

**解決的問題：** OpenCode 的預設配置提供基本體驗，但自訂需要從分散的社群倉庫中手動取得和配置外掛、主題和設定。Oh My OpenCode 將這些打包到一個可安裝的框架中，附帶外掛管理器，使自訂成為一行命令即可完成的操作。

**為何又一個？** oh-my-* 模式（已被擁有 180,000+ 星的 oh-my-zsh 驗證）已證明熱門工具的配置框架能吸引大量採用。Oh My OpenCode 將此成功模式應用於星數第二高的編碼代理，提供與 oh-my-zsh 相同的精選預設和便捷外掛探索體驗。

---

## 68. [readest](https://github.com/readest/readest)
> Readest 是一款專為熱愛閱讀者設計的現代化、功能豐富的電子書閱讀器。

**Language:** TypeScript  |  **Stars:** 17791  |  **Forks:** 960  |  **Best Score:** 1424  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2024-10-12

**背景：** Readest 是一款以 TypeScript 建構的跨平台電子書閱讀器，於 2024 年 10 月推出。它支援主要的電子書格式，並提供註解、高亮、可自訂閱讀主題和跨裝置同步等功能。該應用程式專為想要在桌面和行動平台上獲得現代化、精緻閱讀體驗的熱愛閱讀者設計。

**解決的問題：** 現有的開源電子書閱讀器如 Calibre 優先考慮書庫管理而非閱讀體驗，而商業選項如 Kindle 則將使用者鎖定在單一生態系統中。Readest 專注於閱讀體驗本身——排版、註解工具和跨平台同步——不受供應商鎖定或格式限制。

**為何又一個？** Readest 透過將閱讀體驗置於書庫管理之上來做出差異化。Calibre 是電子書管理和轉換的標準，但其閱讀器介面已過時。Readest 反轉了優先順序，提供具有直覺介面的現代化閱讀體驗，同時保持開源和跨平台。

---

## 69. [skills](https://github.com/huggingface/skills)
> Hugging Face Skills

**Language:** Python  |  **Stars:** 1872  |  **Forks:** 153  |  **Best Score:** 1417  |  **Best Rank:** #22  |  **Days on chart:** 1/7  |  **Created:** 2025-11-24

**背景：** Hugging Face Skills 是 Hugging Face 官方倉庫，提供以 Python 編寫的可重複使用 AI 代理技能集合。它於 2025 年 11 月隨更廣泛的代理技能生態系統一起推出，為使用 Hugging Face 的模型和資料集生態系統建構 AI 代理工作流程提供基礎組件。該倉庫已成長至近 1,900 顆星。

**解決的問題：** 從零開始建構 AI 代理能力需要大量樣板程式碼——模型載入、推論管線、工具定義和錯誤處理。此倉庫提供預建且經過測試的技能實作，可組合成代理工作流程，縮短從概念到可運作代理的時間。

**為何又一個？** 作為 Hugging Face 官方專案，這些技能設計為與 Hugging Face 生態系統原生整合——模型、資料集、Spaces 和推論端點。這種緊密整合使其有別於需要額外黏合程式碼才能連接 Hugging Face 資源的框架無關技能集合。

---

## 70. [AstrBot](https://github.com/AstrBotDevs/AstrBot)
> 整合即時通訊平台、LLM、外掛和 AI 功能的代理式即時通訊聊天機器人基礎設施。

**Language:** Python  |  **Stars:** 17341  |  **Forks:** 1332  |  **Best Score:** 1393  |  **Best Rank:** #20  |  **Days on chart:** 1/7  |  **Created:** 2022-12-08

**背景：** AstrBot 是一個基於 Python 的代理式聊天機器人基礎設施平台，創建於 2022 年 12 月，透過統一的外掛架構將多個即時通訊平台——包括 QQ、微信、Telegram 和 Discord——連接到各種 LLM 後端。它透過 Ollama 支援本地模型以及雲端 API，並內建多模型路由、圖片生成和語音互動等功能。該專案在三年多的開發中累積了超過 17,000 顆星。

**解決的問題：** 為 QQ 和微信等中國即時通訊平台建構 AI 聊天機器人的開發者面臨碎片化的格局：每個平台都有自己的 API、認證系統和訊息格式。AstrBot 提供統一的抽象層，使得編寫一次的技能和外掛可在所有支援的平台上運作而無需修改。它也處理了每個機器人都需要但每個團隊否則需從頭實作的 LLM 路由和對話管理。

**為何又一個？** AstrBot 在擁擠的聊天機器人框架領域中的主要差異化在於其同時專注於中國即時通訊平台和國際平台，填補了那些以 Telegram 和 Discord 為優先的框架所留下的空白。其長期維護歷史也意味著它積累了成熟的外掛生態系統和完善的文件，這是新專案無法匹敵的。當新的 LLM 發布促使使用者將新模型連接到現有機器人部署時，它就會上榜。

---

## 71. [llm-checker](https://github.com/Pavelevich/llm-checker)
> 進階 CLI 工具，掃描你的硬體並告訴你可以在本地執行哪些 LLM 模型。

**Language:** JavaScript  |  **Stars:** 906  |  **Forks:** 62  |  **Best Score:** 1325  |  **Best Rank:** #21  |  **Days on chart:** 1/7  |  **Created:** 2025-07-06

**背景：** llm-checker 是 Pavelevich 開發的 CLI 工具，用於檢查機器的硬體——GPU VRAM、系統 RAM 和 CPU 能力——並產生該機器可在本地執行的 LLM 模型排名列表。它與 Ollama 整合，提供相容模型的直接下載連結，並顯示每個選項的預估推論速度和記憶體餘量。該工具於 2025 年 7 月推出，針對初次接觸本地 LLM 部署的使用者。

**解決的問題：** 初次在本地執行 LLM 的使用者經常下載超出其硬體能力的模型，導致記憶體不足錯誤或慢到無法使用的推論。llm-checker 在使用者開始下載之前，透過自動讀取硬體規格並將其對應到精選的模型相容性資料庫來消除猜測。

**為何又一個？** 雖然 Ollama 本身會列出可用模型，但它不會根據使用者的實際硬體進行篩選或排序。llm-checker 透過硬體感知篩選和直接 Ollama 整合填補了這個空白，使不知道如何手動計算 VRAM 需求的使用者也能輕鬆選擇模型。

---

## 72. [qmd](https://github.com/tobi/qmd)
> 用於你的文件、知識庫、會議記錄的迷你 CLI 搜尋引擎。完全本地運作。

**Language:** TypeScript  |  **Stars:** 9753  |  **Forks:** 531  |  **Best Score:** 1310  |  **Best Rank:** #22  |  **Days on chart:** 1/7  |  **Created:** 2025-12-08

**背景：** qmd 是由 Tobi 以 TypeScript 編寫的輕量命令列搜尋引擎，用於本地文件集合——markdown 檔案、知識庫和會議記錄。它建立本地文件內容索引，提供快速的全文和語意搜尋，無需任何雲端依賴或執行中的伺服器程序。該工具設計為在命令列中呼叫並整合到終端機工作流程中。

**解決的問題：** 個人知識庫和文件集合會成長到 grep 搜尋變得緩慢且無法捕捉文件間語意關係的程度。Notion 搜尋和 Google Drive 等雲端工具需要將文件上傳到外部伺服器。qmd 提供具有語意理解的快速本地搜尋，同時將所有資料保留在使用者的機器上。

**為何又一個？** qmd 佔據了需要大量設定的完整本地 RAG 系統與簡單 grep 搜尋之間的空白。其單一命令呼叫、零伺服器架構和 TypeScript 實作使其易於安裝和使用，無需配置向量資料庫或嵌入伺服器。

---

## 73. [hyperbrowser-app-examples](https://github.com/hyperbrowserai/hyperbrowser-app-examples)
> 完全可運作的 Hyperbrowser 驅動網頁應用程式

**Language:** TypeScript  |  **Stars:** 583  |  **Forks:** 89  |  **Best Score:** 1306  |  **Best Rank:** #21  |  **Days on chart:** 1/7  |  **Created:** 2025-05-28

**背景：** 此倉庫包含一系列使用 Hyperbrowser（一個 AI 驅動的瀏覽器自動化平台）建構的完整可運作範例網頁應用程式。由 Hyperbrowser AI 團隊於 2025 年 5 月創建，它為常見的網頁自動化任務提供參考實作，同時作為新 Hyperbrowser 使用者的文件和入門範本。

**解決的問題：** 瀏覽器自動化平台的學習曲線陡峭，官方文件通常缺乏完整的端到端範例。此倉庫提供可運作的應用程式來展示真實使用場景，透過提供可複製和修改的起點，縮短從初始興趣到可運作應用程式的時間。

**為何又一個？** 不同於僅展示單一 API 呼叫的文件片段，這些是完整、可部署的應用程式，處理了邊緣情況、錯誤狀態和生產環境考量。每個範例展示完整的面向使用者的工作流程，而非僅展示自動化層，使其可直接作為生產應用程式的起點使用。

---

## 74. [llmfit](https://github.com/AlexsJones/llmfit)
> 157 個模型。30 個供應商。一個命令找出你的硬體能執行什麼。

**Language:** Rust  |  **Stars:** 1337  |  **Forks:** 79  |  **Best Score:** 1293  |  **Best Rank:** #23  |  **Days on chart:** 2/7  |  **Created:** 2026-02-15

**背景：** llmfit 是 AlexsJones 開發的 Rust CLI 工具，用於盤點機器的硬體並與涵蓋 30 個供應商的 157 個模型資料庫進行交叉比對，以確定哪些模型與可用資源相容。在本報告日期三天前才創建，其快速的星數累積反映了對硬體感知模型選擇工具的即時需求。Rust 實作產生快速、無依賴的二進位檔。

**解決的問題：** 隨著可在本地執行的 LLM 模型數量在 Ollama、LM Studio 和 llama.cpp 等供應商間爆炸性增長，確定哪個特定模型變體適合給定機器的 GPU 和 RAM 配置變得越來越耗時。llmfit 透過涵蓋多個供應商的全面且最新的模型資料庫自動化了這個交叉比對過程。

**為何又一個？** 與 llm-checker（同樣在此榜單上）相比，llmfit 的差異化在於其廣度——30 個供應商和 157 個模型——以及 Rust 實作，產生更小、更快且無需 Node.js 依賴的二進位檔。這兩個工具以不同的範圍和實作取捨解決相同的問題。

---

## 75. [agents](https://github.com/cloudflare/agents)
> 在 Cloudflare 上建構和部署 AI 代理

**Language:** TypeScript  |  **Stars:** 3278  |  **Forks:** 381  |  **Best Score:** 1292  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2025-01-29

**背景：** Cloudflare Agents 是 Cloudflare 官方的 TypeScript 框架，用於在 Cloudflare 的邊緣網路上建構和部署 AI 代理。它利用 Durable Objects 實現有狀態的代理對話、Workers 實現無伺服器執行，並整合 Cloudflare 的 AI Gateway 進行模型路由。該框架於 2025 年 1 月推出，為常見的代理模式提供範本和範例。

**解決的問題：** 部署 AI 代理通常需要管理伺服器基礎設施、處理 WebSocket 連線以進行即時互動，以及實作狀態持久化——這些都增加了複雜度和成本。Cloudflare Agents 將這些關注點抽象到 Cloudflare 平台中，以最少的基礎設施管理提供全球分散式的有狀態代理執行。

**為何又一個？** 邊緣部署模型是其差異化因素：代理在 Cloudflare 的全球網路上運行而非在單一區域，為全球使用者降低延遲。與 Durable Objects 的整合提供內建的狀態持久化而無需外部資料庫，Workers 執行環境提供自動擴展。對於已在使用 Cloudflare 的團隊，它消除了設置獨立代理基礎設施的需求。

---

## 76. [n8n-workflows](https://github.com/Zie619/n8n-workflows)
> 我能找到的所有 n8n 工作流程（也包括來自官方網站的）

**Language:** Python  |  **Stars:** 51740  |  **Forks:** 6551  |  **Best Score:** 1277  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2025-05-14

**背景：** 這個倉庫是由 Zie619 整理的全面 n8n 工作流程範本集合，匯集了來自官方 n8n 網站和社群來源的工作流程。N8n 是一個類似 Zapier 的開源工作流程自動化平台，而這個倉庫則作為非官方但內容廣泛的預建自動化程式庫。自 2025 年 5 月以來已累積超過 51,000 顆星。

**解決的問題：** 從零開始建構 n8n 工作流程需要理解平台的節點系統，並嘗試服務之間的連接。此集合提供現成的工作流程範本，使用者可直接匯入，涵蓋常見的自動化模式，降低新 n8n 使用者的學習曲線。

**為何又一個？** 雖然 n8n 有官方範本庫，但此倉庫將來自多個社群來源的工作流程匯集到單一可搜尋的集合中。非官方的策展包含官方庫可能未收錄的工作流程，且基於 GitHub 的格式比官方的網頁範本瀏覽器更易於瀏覽、fork 和改編。

---

## 77. [gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager)
> Google Gemini 和 AI Studio 的一站式增強套件

**Language:** TypeScript  |  **Stars:** 7252  |  **Forks:** 230  |  **Best Score:** 1275  |  **Best Rank:** #22  |  **Days on chart:** 1/7  |  **Created:** 2025-10-04

**背景：** Gemini Voyager 是由 Nagi-ovo 建立的 TypeScript 瀏覽器擴充功能和增強套件，為 Google Gemini 和 AI Studio 增加 Google 原生未提供的額外功能。它於 2025 年 10 月推出，透過解決官方 Gemini 介面中的使用體驗不足，已成長至超過 7,200 顆星。該擴充功能針對每天依賴 Gemini 或 AI Studio 工作的進階使用者。

**解決的問題：** Google 官方的 Gemini 和 AI Studio 介面缺乏一般使用者期望的生產力功能——對話管理、匯出選項、鍵盤快捷鍵和可自訂的 UI 元素。Gemini Voyager 在現有介面之上疊加這些增強功能，無需更改 API 金鑰或使用替代前端。

**為何又一個？** Gemini Voyager 不是建構新的 AI 前端，而是增強使用者已登入的現有 Google 介面，保留對話狀態和帳單上下文。這使其定位為官方產品的補充而非替代品，使其比完全替代的前端更容易被採用。

---

## 78. [timesfm](https://github.com/google-research/timesfm)
> Google Research 的 TimesFM（時間序列基礎模型），用於時間序列預測。

**Language:** Python  |  **Stars:** 8851  |  **Forks:** 732  |  **Best Score:** 1262  |  **Best Rank:** #23  |  **Days on chart:** 2/7  |  **Created:** 2024-04-29

**背景：** TimesFM 是 Google Research 於 2024 年 4 月發布的預訓練時間序列基礎模型，可在廣泛的時間序列領域中執行零樣本預測，無需針對特定任務進行微調。它在大量真實世界時間序列資料上訓練，並以支援 JAX 和 PyTorch 後端的 Python 函式庫形式提供。該模型針對需要準確預測但不想承擔訓練或微調領域特定模型成本的從業者。

**解決的問題：** 傳統時間序列預測需要為每個序列調校統計模型，或需要大量訓練資料和算力為每個新領域訓練深度學習模型。TimesFM 實現零樣本預測——在無需任何微調的情況下對新時間序列做出準確預測——透過在推論時將其廣泛預訓練語料庫中學到的模式遷移到新領域。

**為何又一個？** TimesFM 的 Google Research 背景和已驗證的零樣本準確性使其有別於 NeuralForecast 或 PyTorch Forecasting 等仍需訓練的早期神經預測函式庫。當新的從業者發現基礎模型方法可以在不需要任何訓練管線的情況下超越他們現有的逐序列統計模型時，它就會週期性地上榜。對 AI 原生資料基礎設施日益增長的興趣也為該倉庫帶來了經常性的流量。

---

## 79. [PaperKnife](https://github.com/potatameister/PaperKnife)
> 隱私優先的 PDF 工具（零伺服器架構）。在本地 100% 合併、分割、壓縮和編輯 PDF。

**Language:** TypeScript  |  **Stars:** 553  |  **Forks:** 28  |  **Best Score:** 1251  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2026-01-26

**背景：** PaperKnife 是一個基於瀏覽器的 PDF 工具，採用零伺服器架構，這意味著所有 PDF 處理——合併、分割、壓縮和編輯——完全在瀏覽器中使用 WebAssembly 完成，沒有任何檔案被上傳到伺服器。以 TypeScript 編寫，由 potatameister 於 2026 年 1 月推出，針對需要 PDF 操作工具但不願將敏感文件發送到雲端服務的使用者。

**解決的問題：** ilovepdf 和 Smallpdf 等熱門線上 PDF 工具在伺服器上處理文件，這對包含敏感個人、法律或財務資訊的文件引發隱私疑慮。PaperKnife 完全在客戶端提供相同功能，確保文件內容永遠不會離開使用者的裝置。

**為何又一個？** 雖然 PDF.js 和類似函式庫可實現客戶端 PDF 渲染，但在其上建構完整功能的工具需要大量工程投入。PaperKnife 將其包裝成精緻、即可使用的應用程式，非技術使用者無需安裝即可存取，佔據了複雜桌面應用程式和侵犯隱私的網頁工具之間的空間。

---

## 80. [LobsterBoard](https://github.com/Curbob/LobsterBoard)
> OpenClaw 儀表板建構器——建立自訂儀表板

**Language:** JavaScript  |  **Stars:** 498  |  **Forks:** 64  |  **Best Score:** 1245  |  **Best Rank:** #23  |  **Days on chart:** 1/7  |  **Created:** 2026-02-06

**背景：** LobsterBoard 是一個 JavaScript 應用程式，用於在 OpenClaw AI 助理平台上建構自訂儀表板。它提供拖放介面，可將技能輸出、資料視覺化和狀態小工具組合成持久的儀表板視圖。該專案於 2026 年 2 月初推出，是更廣泛 OpenClaw 生態系統擴展的一部分。

**解決的問題：** OpenClaw 技能輸出是短暫的——它們出現在聊天中並隨對話消失。LobsterBoard 提供持久、可組合的技能資料視圖，使監控進行中的自動化、追蹤指標和顯示經常性資訊變得實際可行，無需手動重新呼叫技能。這將 OpenClaw 從對話式工具轉變為持久的資訊工作空間。

**為何又一個？** 先前沒有 OpenClaw 工具解決經常性資訊需求的持久性和可組合性差距。LobsterBoard 在生態系統中是新穎的，而非現有功能的複製，這解釋了儘管絕對星數不大但早期快速獲得關注的原因。

---

## 81. [n8n](https://github.com/n8n-io/n8n)
> 具備原生 AI 能力的公平程式碼工作流程自動化平台。

**Language:** TypeScript  |  **Stars:** 175786  |  **Forks:** 55068  |  **Best Score:** 1225  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2019-06-22

**背景：** n8n 是一個採用公平程式碼授權的工作流程自動化平台，成立於 2019 年，允許使用者透過視覺化節點編輯器連接數百個預建整合來建構自動化管線。它可以自行託管或使用 n8n Cloud，並已新增原生 AI 節點類型，允許將 LLM 呼叫、向量儲存互動和代理編排直接整合到自動化工作流程中。擁有超過 175,000 顆星和 55,000 個 fork，它是最廣泛採用的開源自動化平台之一。

**解決的問題：** 商業自動化通常需要在強大但昂貴的 SaaS 平台（如 Zapier 或 Make）與難以維護的自訂整合程式碼之間做選擇。n8n 提供可自行託管的替代方案，具有支援複雜分支邏輯、資料轉換以及現在的 AI 原生步驟的視覺化工作流程編輯器，無需雲端自動化服務的按操作計費。

**為何又一個？** n8n 持續上榜，因為其星數使其在很低的每日增速下就會出現在 GitHub 的趨勢頁面上，而且每次新 AI 節點或整合發布都會產生新的媒體報導吸引新使用者。其公平程式碼授權也吸引了想要類似 Zapier 的自動化但不想支付訂閱費的使用者。原生 AI 能力的整合使其對建構代理工作流程並需要無程式碼編排層的使用者來說有了新的相關性。

---

## 82. [electrobun](https://github.com/blackboardsh/electrobun)
> 使用 TypeScript 建構超快速、迷你且跨平台的桌面應用程式。

**Language:** C++  |  **Stars:** 6274  |  **Forks:** 115  |  **Best Score:** 1196  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2024-02-28

**背景：** Electrobun 是 Blackboard.sh 推出的桌面應用程式框架，使用 Bun 執行主程序並打包 webview TypeScript，原生綁定以 Zig 編寫。它的目標是產生約 12MB 的自解壓應用程式包（使用系統 webview），並透過版本間的 bsdiff 二進位修補實現小至 14KB 的應用程式更新。它針對與 Electron 相同的利基市場，但架構截然不同，提供主程序和 webview 程序之間的型別化 RPC。

**解決的問題：** Electron 應用程式體積龐大——每個應用程式附帶完整的 Chromium 執行環境意味著 100-200MB 的套件和高執行時記憶體使用。Electrobun 透過使用作業系統提供的 webview 和 Bun 取代 Node.js 來規避此問題，產生更小的發行版和更快的啟動時間。

**為何又一個？** 與 Tauri 的差異化角度在於選擇 Bun 加 Zig 而非 Rust，以及程序間一流的 TypeScript RPC 層。Electrobun 的更新機制——二進位修補而非完整下載——也是獨特的。該框架再次受到關注，因為其展示應用程式之一（Audio TTS）是基於 Qwen3-TTS 建構的，將其與此榜單其他地方的 TTS 趨勢連結起來。

---

## 83. [notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli)
> NotebookLM MCP CLI 工具

**Language:** Python  |  **Stars:** 1500  |  **Forks:** 319  |  **Best Score:** 1186  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2025-12-23

**背景：** NotebookLM MCP CLI 是 jacob-bd 開發的 Python 命令列工具，透過 Model Context Protocol（MCP）公開 Google NotebookLM 的功能，使 AI 代理能夠以程式化方式與 NotebookLM 筆記本互動。它於 2025 年 12 月推出，主要從建構 MCP 相容代理工作流程的開發者中累積了 1,500 顆星。該工具彌補了 NotebookLM 介面與更廣泛 MCP 生態系統之間的差距。

**解決的問題：** Google NotebookLM 沒有官方 API，使其無法被需要以程式化方式查詢或管理筆記本的自動化工作流程和 AI 代理存取。此工具以 MCP 相容的 CLI 包裝 NotebookLM 的底層介面，讓使用 MCP 的代理可以將 NotebookLM 當作可直接呼叫的工具。

**為何又一個？** MCP 生態系統作為代理與工具通訊的標準協定正在快速成長，而 NotebookLM 是一個廣泛使用但沒有官方程式化介面的研究工具。此專案填補了一個特定的整合空白——NotebookLM 作為 MCP 工具——目前沒有官方或競爭專案解決此問題。

---

## 84. [midday](https://github.com/midday-ai/midday)
> 為自由工作者打造的發票、時間追蹤、檔案對帳、儲存、財務概覽及專屬 AI 助理

**Language:** TypeScript  |  **Stars:** 14034  |  **Forks:** 1349  |  **Best Score:** 1184  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2023-09-18

**背景：** Midday 是由 midday-ai 建構的開源商務管理平台，專門針對自由工作者和獨立承包商。它將發票、時間追蹤、檔案對帳、財務概覽和內嵌 AI 助理整合到單一 TypeScript 應用程式中。於 2023 年 9 月推出，透過解決自由工作者通常從多個付費服務拼湊起來的碎片化工具問題，已成長至超過 14,000 顆星。

**解決的問題：** 自由工作者通常使用不同的工具來處理發票、時間追蹤、文件儲存和財務報告——每個工具都有自己的訂閱費用和資料孤島。Midday 將這些功能整合到單一可自行託管的平台中，附帶一個 AI 助理可直接從統一資料中回答有關收入、未付發票和時間分配的問題。

**為何又一個？** Midday 的差異化在於其專注於自由工作者，並結合能存取平台中所有財務和時間追蹤資料的 AI 助理。通用型會計工具不是為專案制收入模式設計的，而專注於自由工作者的 SaaS 產品價格昂貴。Midday 提供一個自行託管的替代方案，具有專為自由工作者商務管理量身打造的資料模型。

---
