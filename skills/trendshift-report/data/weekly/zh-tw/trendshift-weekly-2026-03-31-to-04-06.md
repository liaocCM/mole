# Trendshift 每週報告 — 2026-03-31 至 2026-04-06
**不重複專案總數：** 92（來自 7 天共 175 筆每日上榜紀錄）

---

## 1. [claw-code](https://github.com/instructkr/claw-code)
> 更好的代理工具鏈——不僅保存洩漏的 Claude Code 檔案，還要實際做出成果。現正用 Rust 重寫。

**Language:** Rust  |  **Stars:** 48,386  |  **Forks:** 56,314  |  **Best Score:** 350,303  |  **Best Rank:** #1  |  **Days on chart:** 1/7  |  **Created:** 2026-03-31

**背景：** Claw Code 是 Claude Code 代理工具鏈的公開 Rust 實作。正式程式碼位於 `rust/` 工作區，提供 CLI 二進位檔。它宣稱不僅是原始碼的存檔，而是要在此基礎上建構實際可用的工具。
**解決的問題：** 它針對開發者希望擁有開放、可修改的代理工具鏈的需求。官方 Claude Code 是封閉的，而 Claw Code 嘗試提供一個 Rust 原生的替代方案，讓社群能直接參與開發和改進。
**為何又一個？** 此分支由 instructkr 維護，與 ultraworkers/claw-code 為同源專案但走不同方向。350,303 的趨勢分數創下本週最高紀錄，反映了社群對開放代理工具鏈的極度渴望。

---

## 2. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code 是一個代理式編程工具，駐留在你的終端機中，理解你的程式碼庫，並透過自然語言指令幫助你更快地編程。

**Language:** Shell  |  **Stars:** 110,318  |  **Forks:** 18,343  |  **Best Score:** 90,642  |  **Best Rank:** #1  |  **Days on chart:** 5/7  |  **Created:** 2025-02-22

**背景：** Claude Code 是 Anthropic 官方推出的代理式編程 CLI 工具。它直接在終端機中運行，能執行例行任務、解釋複雜程式碼並處理 git 工作流程。支援 VS Code、JetBrains 和 Xcode 等 IDE 整合。
**解決的問題：** 它解決了開發者在終端機環境中缺乏智能編程助手的問題。相較於需要切換視窗的 IDE 外掛，Claude Code 原生整合在開發者最常使用的終端機中，支援從程式碼理解到版本控制的完整工作流程。
**為何又一個？** 作為 Anthropic 官方產品，Claude Code 擁有超過 110,000 顆星，是目前最受歡迎的代理式編程工具之一。本週 5 天上榜，持續展現其在開發者社群中的主導地位。

---

## 3. [claw-code](https://github.com/ultraworkers/claw-code)
> 倉庫終於解鎖。史上最快突破 100K 星的倉庫。使用 oh-my-codex 以 Rust 建構。

**Language:** Rust  |  **Stars:** 173,712  |  **Forks:** 105,051  |  **Best Score:** 62,850  |  **Best Rank:** #1  |  **Days on chart:** 3/7  |  **Created:** 2026-03-31

**背景：** 這是 Claw Code 的 UltraWorkers 版本，宣稱為正式倉庫。它使用 oh-my-codex 以 Rust 建構，並在 Discord 社群中活躍運作。該倉庫的解鎖引發了大規模的社群參與。
**解決的問題：** 與 instructkr 版本類似，它為開發者提供了一個開放的代理工具鏈替代方案。UltraWorkers 版本更強調社群驅動的快速迭代和跨工具生態整合。
**為何又一個？** 173,712 顆星使其成為本週星數最高的專案。宣稱史上最快突破 100K 星的倉庫，本週 3 天上榜。它與 instructkr 版本的分歧反映了開源社群中常見的分叉治理議題。

---

## 4. [awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
> DESIGN.md 檔案合集，擷取熱門網站的設計系統。將其放入專案中，讓編程代理建構匹配的 UI。

**Language:** HTML  |  **Stars:** 15,726  |  **Forks:** 1,933  |  **Best Score:** 51,107  |  **Best Rank:** #1  |  **Days on chart:** 3/7  |  **Created:** 2026-03-31

**背景：** awesome-design-md 是一個精選合集，收錄了從 Vercel、Linear、Notion 等知名網站擷取的 DESIGN.md 設計系統檔案。開發者只需將這些檔案放入專案，AI 編程代理就能據此建構視覺匹配的 UI。
**解決的問題：** 它解決了 AI 代理生成 UI 時缺乏設計規範的問題。沒有明確的設計系統指引，代理往往產出通用、缺乏品牌一致性的介面。DESIGN.md 為代理提供了具體的設計參考。
**為何又一個？** 本週新建即登頂，51,107 的趨勢分數展現了社群對「設計即程式碼」理念的強烈共鳴。它將設計系統轉化為代理可消費的格式，代表了 AI 原生開發工具鏈的新方向。

---

## 5. [pretext](https://github.com/chenglou/pretext)
> 快速、精確且全面的文字測量與排版引擎。

**Language:** TypeScript  |  **Stars:** 39,924  |  **Forks:** 2,122  |  **Best Score:** 31,097  |  **Best Rank:** #1  |  **Days on chart:** 5/7  |  **Created:** 2026-03-07

**背景：** Pretext 是一個純 JavaScript/TypeScript 文字測量與排版函式庫。它繞過了 DOM 測量（如 `getBoundingClientRect`），自行實作文字測量邏輯，以瀏覽器字型引擎為基準，支援渲染至 DOM、Canvas 和 SVG。
**解決的問題：** 它解決了瀏覽器文字排版中 DOM reflow 的效能瓶頸。傳統方法依賴 DOM 測量會觸發昂貴的佈局重排。Pretext 透過自建測量邏輯，大幅提升文字密集應用的渲染效能。
**為何又一個？** 來自 chenglou（React Motion、Reason 語言的作者）的新專案，本週 5 天登上趨勢榜。近 40,000 顆星反映了前端社群對高效能文字排版的長期需求。其多語言支援覆蓋了許多開發者未曾考慮的語言場景。

---

## 6. [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex)
> OmX — Oh My codeX：你的 codex 不再孤單。新增 hooks、agent teams、HUDs 等功能。

**Language:** TypeScript  |  **Stars:** 18,118  |  **Forks:** 1,711  |  **Best Score:** 21,341  |  **Best Rank:** #2  |  **Days on chart:** 5/7  |  **Created:** 2026-02-02

**背景：** oh-my-codex 是一個為 OpenAI Codex CLI 打造的擴充工具。它為 Codex 新增了 hooks 系統、agent teams 多代理協作、HUD 狀態面板等功能，大幅擴展了原始 Codex 的能力邊界。
**解決的問題：** 它解決了 Codex CLI 原生功能不足的問題。開發者需要 hooks 來自訂工作流程、需要 HUD 來監控代理狀態、需要 agent teams 來協調多個代理。oh-my-codex 將這些功能打包為易用的擴充。
**為何又一個？** 本週 5 天上榜，18,000+ 顆星展現了 Codex 使用者社群的活躍度。Yeachan Heo 同時維護 oh-my-claudecode 和 oh-my-openagent，形成了跨代理平台的統一擴充生態。

---

## 7. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> 「實踐造就完美的 Claude」——Claude Code 最佳實踐指南。

**Language:** HTML  |  **Stars:** 32,742  |  **Forks:** 3,011  |  **Best Score:** 20,534  |  **Best Rank:** #3  |  **Days on chart:** 3/7  |  **Created:** 2025-10-31

**背景：** claude-code-best-practice 是一份全面的 Claude Code 使用最佳實踐指南。從基礎設定到進階技巧，涵蓋了使用 Claude Code 進行高效開發的各個面向。
**解決的問題：** 它解決了 Claude Code 使用者缺乏系統性學習資源的問題。隨著 Claude Code 的快速演進，官方文件往往跟不上社群發現的最佳實踐。此專案填補了這個知識差距。
**為何又一個？** 32,000+ 顆星使其成為 Claude Code 最佳實踐領域最受歡迎的資源。持續更新的頻率（最新版本標記至 v2.1.92）展現了維護者的投入。本週 3 天上榜反映了持續的社群需求。

---

## 8. [openscreen](https://github.com/siddharthvaddem/openscreen)
> 免費建立精美的展示影片。開源、無訂閱、無浮水印，可商業使用。Screen Studio 的替代方案。

**Language:** TypeScript  |  **Stars:** 24,842  |  **Forks:** 1,650  |  **Best Score:** 18,544  |  **Best Rank:** #2  |  **Days on chart:** 6/7  |  **Created:** 2025-10-10

**背景：** OpenScreen 是一個開源的螢幕錄影後製工具，為開發者和內容創作者提供免費的專業級展示影片製作能力。無浮水印、無訂閱費用，且允許商業使用。
**解決的問題：** 它解決了專業螢幕錄影軟體（如 Screen Studio）價格高昂的問題。獨立開發者和小團隊需要製作精美的產品展示影片，但付費工具的訂閱成本是一道障礙。
**為何又一個？** 本週 6 天上榜是所有專案中最高的出場率之一。24,800+ 顆星反映了開發者社群對免費專業級錄影工具的強烈需求。仍處於 beta 階段但已獲得如此高的關注度。

---

## 9. [VibeVoice](https://github.com/microsoft/VibeVoice)
> 開源前沿語音 AI。

**Language:** Python  |  **Stars:** 37,119  |  **Forks:** 4,268  |  **Best Score:** 14,268  |  **Best Rank:** #2  |  **Days on chart:** 2/7  |  **Created:** 2025-08-25

**背景：** VibeVoice 是 Microsoft 推出的開源前沿語音 AI 系統。提供 TTS（文字轉語音）和 ASR（語音辨識）能力，相關論文已在學術會議上發表。Hugging Face 上提供完整的模型合集。
**解決的問題：** 它解決了高品質語音 AI 模型缺乏開源選項的問題。商業語音 API 成本高昂且缺乏客製化彈性。VibeVoice 提供前沿水準的開源替代方案，讓開發者可以自由部署和微調。
**為何又一個？** 作為 Microsoft 官方開源專案，VibeVoice 在品質和可信度上具有獨特優勢。37,000+ 顆星和學術論文背書展現了其技術深度。開源前沿語音 AI 是目前市場的稀缺資源。

---

## 10. [cc-gateway](https://github.com/motiful/cc-gateway)
> AI API 身份閘道——反向代理，標準化裝置指紋和遙測數據，實現隱私保護的 API 代理。

**Language:** TypeScript  |  **Stars:** 2,462  |  **Forks:** 444  |  **Best Score:** 13,854  |  **Best Rank:** #4  |  **Days on chart:** 1/7  |  **Created:** 2026-03-31

**背景：** cc-gateway 是一個 AI API 身份閘道，作為反向代理運行。它標準化裝置指紋和遙測數據，讓使用者在呼叫 AI API 時能保護隱私。
**解決的問題：** 它解決了 AI API 呼叫中隱私暴露的問題。當開發者使用 Claude Code 等工具時，裝置指紋和使用遙測會被發送至服務端。cc-gateway 在中間層攔截並標準化這些數據。
**為何又一個？** cc-gateway 瞄準了一個越來越受關注的利基市場——AI 工具的隱私保護。雖然僅 1 天上榜，但 13,854 的趨勢分數顯示了社群對 AI 隱私基礎設施的高度興趣。

---

## 11. [career-ops](https://github.com/santifer/career-ops)
> 基於 Claude Code 的 AI 驅動求職系統。14 種技能模式、Go 儀表板、PDF 生成、批次處理。

**Language:** Go  |  **Stars:** 3,845  |  **Forks:** 585  |  **Best Score:** 12,553  |  **Best Rank:** #2  |  **Days on chart:** 1/7  |  **Created:** 2026-04-04

**背景：** Career-Ops 是一個 AI 驅動的求職管線系統，建構在 Claude Code 之上。提供 14 種技能模式，包括職位評估、量身定做的履歷生成、門戶掃描和進度追蹤，全部由 AI 代理驅動。
**解決的問題：** 它解決了求職過程繁瑣且耗時的問題。從職位評估到履歷客製化再到進度追蹤，傳統求職需要大量重複性工作。Career-Ops 將整個流程自動化。
**為何又一個？** Career-Ops 以其完整的端到端求職管線脫穎而出。Go 語言建構的儀表板和 PDF 生成能力展現了工程品質。創建僅數天就獲得高趨勢分數，反映了開發者對 AI 求職工具的需求。

---

## 12. [emdash](https://github.com/emdash-cms/emdash)
> EmDash 是基於 Astro 的全端 TypeScript CMS；WordPress 的精神繼承者。

**Language:** TypeScript  |  **Stars:** 7,578  |  **Forks:** 548  |  **Best Score:** 12,114  |  **Best Rank:** #3  |  **Days on chart:** 3/7  |  **Created:** 2026-04-01

**背景：** EmDash 是建構在 Astro 和 Cloudflare 之上的全端 TypeScript CMS。它延續了 WordPress 的核心理念——可擴展性、管理介面和外掛生態——但以無伺服器和型別安全的基礎重新建構。外掛在沙盒 Worker 隔離環境中運行。
**解決的問題：** 它解決了 WordPress 外掛架構的根本安全問題。WordPress 外掛擁有完全的系統存取權限，是安全漏洞的主要來源。EmDash 透過 Worker 隔離環境從架構層面解決這個問題。
**為何又一個？** EmDash 以其「WordPress 精神繼承者」的定位引發關注。在 WordPress 仍主導 CMS 市場的背景下，一個基於現代技術棧的全新替代方案吸引了大量開發者目光。本週 3 天上榜。

---

## 13. [superpowers](https://github.com/obra/superpowers)
> 一個有效的代理技能框架與軟體開發方法論。

**Language:** Shell  |  **Stars:** 138,686  |  **Forks:** 11,746  |  **Best Score:** 11,854  |  **Best Rank:** #4  |  **Days on chart:** 7/7  |  **Created:** 2025-10-09

**背景：** Superpowers 是一套完整的程式碼代理軟體開發工作流程。代理不會直接跳入寫程式碼，而是先退後一步詢問你真正想做什麼。確認設計後，代理制定實作計畫，再透過子代理驅動開發流程。
**解決的問題：** 它解決了程式碼代理缺乏結構化工作流程的問題。開發者常遇到代理直接開始寫程式碼而不理解需求的困境。Superpowers 強制執行腦力激盪、規劃、TDD 和子代理驅動開發的流程。
**為何又一個？** 連續多週全 7 天上榜，本週再次達成。138,000+ 顆星使其成為代理技能框架領域的標竿。技能自動觸發的設計使其在眾多競品中保持獨特優勢。

---

## 14. [claude-howto](https://github.com/luongnv89/claude-howto)
> 視覺化、範例驅動的 Claude Code 指南——從基礎概念到進階代理，附帶可直接複製的模板。

**Language:** Python  |  **Stars:** 20,611  |  **Forks:** 2,462  |  **Best Score:** 11,580  |  **Best Rank:** #5  |  **Days on chart:** 4/7  |  **Created:** 2025-11-07

**背景：** claude-howto 是一份視覺化的 Claude Code 教學指南。從基本概念到進階代理用法，每個主題都附帶可直接複製使用的模板，讓使用者能立即獲得價值。
**解決的問題：** 它解決了 Claude Code 學習曲線陡峭的問題。官方文件偏向參考手冊式，缺乏循序漸進的教學和實際範例。claude-howto 以「展示而非說教」的方式降低入門門檻。
**為何又一個？** 本週 4 天上榜，20,000+ 顆星。其視覺化、範例驅動的教學方式與其他文字密集的指南形成鮮明對比。曾登上 GitHub Trending #1，持續吸引新使用者。

---

## 15. [ai-agent-deep-dive](https://github.com/tvytlx/ai-agent-deep-dive)
> AI Agent 原始碼深度研究報告。

**Language:** Python  |  **Stars:** 5,133  |  **Forks:** 1,559  |  **Best Score:** 11,012  |  **Best Rank:** #6  |  **Days on chart:** 2/7  |  **Created:** 2026-03-31

**背景：** 這是一份 AI Agent 原始碼的深度研究報告（PDF），涵蓋代理核心架構、工具呼叫、記憶系統等章節。同時包含一個教學用的最小 Python Agent 專案，示範 AI Agent 的核心結構組織方式。
**解決的問題：** 它解決了開發者對 AI 代理框架內部運作「知其然不知其所以然」的問題。大多數人使用代理工具卻不理解底層架構。此報告透過原始碼分析揭示代理的核心工程原理。
**為何又一個？** 中文深度技術分析在全球趨勢榜上表現突出，反映了中文開發者社群對代理技術的深入研究。創建當週即上榜，11,012 的趨勢分數展現了強烈的學習需求。

---

## 16. [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
> 代理工具鏈效能優化系統。為 Claude Code、Codex、Opencode、Cursor 等提供技能、直覺、記憶和安全。

**Language:** JavaScript  |  **Stars:** 144,531  |  **Forks:** 22,174  |  **Best Score:** 9,901  |  **Best Rank:** #8  |  **Days on chart:** 2/7  |  **Created:** 2026-01-18

**背景：** Everything Claude Code 是一個全面的代理工具鏈效能優化系統。它為 Claude Code 及其他代理平台提供技能、直覺、記憶、安全性和研究優先的開發方法論。支援多語言文件。
**解決的問題：** 它解決了代理工具鏈效能優化分散在各處的問題。開發者需要從多個來源收集最佳實踐，而此專案將所有優化策略整合在一處，提供統一的效能提升方案。
**為何又一個？** 144,000+ 顆星使其成為 GitHub 上最受歡迎的 Claude Code 相關專案。跨平台支援（Claude Code、Codex、Opencode、Cursor）擴大了受眾範圍。本週 2 天上榜展現了持續的社群關注。

---

## 17. [cli](https://github.com/larksuite/cli)
> Lark/飛書官方 CLI 工具——為人類和 AI 代理而建。涵蓋 200+ 指令和 19 個 AI Agent Skills。

**Language:** Go  |  **Stars:** 6,722  |  **Forks:** 394  |  **Best Score:** 8,653  |  **Best Rank:** #6  |  **Days on chart:** 1/7  |  **Created:** 2026-03-25

**背景：** 這是 Lark/飛書團隊維護的官方 CLI 工具。涵蓋即時通訊、文件、多維表格、日曆、郵件、任務、會議等核心業務領域，提供超過 200 個指令和 19 個 AI Agent Skills。
**解決的問題：** 它解決了企業通訊和協作工具缺乏 CLI 介面的問題。AI 代理需要透過程式化的方式存取企業工具，而傳統的 Web UI 無法被代理直接操作。Lark CLI 為代理提供了原生的命令列存取方式。
**為何又一個？** 作為字節跳動旗下 Lark/飛書的官方工具，它在企業級工具的 AI 原生化領域佔有獨特地位。19 個 AI Agent Skills 展現了「為代理而建」的設計理念。

---

## 18. [goose](https://github.com/block/goose)
> 一個開源、可擴展的 AI 代理——超越程式碼建議，支援安裝、執行、編輯和測試。

**Language:** Rust  |  **Stars:** 35,868  |  **Forks:** 3,369  |  **Best Score:** 7,714  |  **Best Rank:** #3  |  **Days on chart:** 3/7  |  **Created:** 2024-08-23

**背景：** Goose 是 Block（原 Square）推出的開源 AI 代理，現已遷移至 Linux Foundation 旗下的 Agentic AI Foundation。提供桌面應用、CLI 和 API，支援任何 LLM。
**解決的問題：** 它解決了大多數 AI 編程助手僅停留在「程式碼建議」層面的問題。Goose 能實際安裝依賴、執行程式碼、編輯檔案和運行測試，真正完成端到端的開發任務。
**為何又一個？** 遷移至 Linux Foundation 提升了專案的治理水準和長期可持續性。35,000+ 顆星和 Rust 建構展現了工程品質。本週 3 天上榜反映了社群對開源代理替代方案的持續需求。

---

## 19. [onyx](https://github.com/onyx-dot-app/onyx)
> 開源 AI 平台——支援任何 LLM 的進階 AI 聊天。

**Language:** Python  |  **Stars:** 25,588  |  **Forks:** 3,411  |  **Best Score:** 6,981  |  **Best Rank:** #6  |  **Days on chart:** 3/7  |  **Created:** 2023-04-27

**背景：** Onyx 是一個開源 AI 平台，提供支援多種 LLM 的進階聊天功能。它整合了企業知識庫搜尋、文件分析和對話管理，為組織提供私有部署的 AI 助手解決方案。
**解決的問題：** 它解決了企業需要私有部署且支援多 LLM 的 AI 平台的需求。商業 AI 聊天產品往往鎖定特定模型供應商，而 Onyx 提供了 LLM 無關的開源替代方案。
**為何又一個？** 25,000+ 顆星和持續的社群活躍度展現了其在企業 AI 平台領域的領先地位。本週 3 天上榜反映了企業對開源 AI 平台的持續需求。

---

## 20. [vphone-aio](https://github.com/34306/vphone-aio)
> 一個腳本啟動虛擬手機。

**Language:** Shell  |  **Stars:** 3,052  |  **Forks:** 550  |  **Best Score:** 6,750  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2026-02-28

**背景：** vphone-aio 是一個一鍵啟動虛擬 iPhone 的腳本工具。支援 iOS 26.1，已預置越獄和完整 bootstrap。只需安裝幾個先決條件並停用 SIP 即可運行。
**解決的問題：** 它解決了 iOS 虛擬環境設定繁瑣的問題。傳統方法需要多個步驟和工具才能建立可用的虛擬 iOS 環境。vphone-aio 將整個流程濃縮為單一腳本。
**為何又一個？** vphone-aio 以其極簡的使用方式脫穎而出——一個腳本解決所有問題。預置越獄環境降低了行動開發者和安全研究者的門檻。

---

## 21. [agency-agents](https://github.com/msitarzewski/agency-agents)
> 一個完整的 AI 代理團隊觸手可及——從前端精靈到 Reddit 社群忍者，每個代理都是具備個性和流程的專業專家。

**Language:** Shell  |  **Stars:** 74,280  |  **Forks:** 11,645  |  **Best Score:** 6,684  |  **Best Rank:** #3  |  **Days on chart:** 7/7  |  **Created:** 2025-10-13

**背景：** The Agency 是一個 AI 代理個性模板合集，提供完整的 AI 代理團隊。每個代理都有獨特的個性、定義明確的工作流程和經過驗證的交付物。
**解決的問題：** 它解決了開發者需要快速部署專業化 AI 代理的需求。與其從零開始定義代理行為，開發者可以直接使用經過社群驗證的代理模板。
**為何又一個？** 連續多週全 7 天上榜，本週再次達成。74,000+ 顆星和 11,600+ 分支反映了廣泛的採用。其獨特的個性化代理設計方法使其在眾多代理框架中持續脫穎而出。

---

## 22. [sherlock](https://github.com/sherlock-project/sherlock)
> 透過使用者名稱在社群網路中搜尋社群媒體帳號。

**Language:** Python  |  **Stars:** 80,033  |  **Forks:** 9,304  |  **Best Score:** 6,634  |  **Best Rank:** #12  |  **Days on chart:** 6/7  |  **Created:** 2018-12-24

**背景：** Sherlock 是一個經典的 OSINT 工具，可透過使用者名稱在數百個社群網路平台上搜尋匹配的帳號。它是安全研究和社交工程分析中最常用的工具之一。
**解決的問題：** 它解決了跨平台使用者身份追蹤的需求。在安全調查和身份驗證場景中，需要快速確認某個使用者名稱在哪些平台上被使用。Sherlock 自動化了這個跨平台搜尋流程。
**為何又一個？** 作為擁有 80,000+ 顆星的經典 OSINT 工具，Sherlock 本週 6 天上榜展現了持續的實用價值。長期穩定的維護和廣泛的平台覆蓋使其在安全社群中始終保持熱度。

---

## 23. [oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)
> omo——最佳代理工具鏈，前身為 oh-my-opencode。

**Language:** TypeScript  |  **Stars:** 49,258  |  **Forks:** 3,894  |  **Best Score:** 6,547  |  **Best Rank:** #9  |  **Days on chart:** 2/7  |  **Created:** 2025-12-03

**背景：** oh-my-openagent（前身為 oh-my-opencode）是一個代理工具鏈增強工具。作為 Yeachan Heo 的 oh-my 系列之一，它提供了統一的代理擴充框架，從 hooks 到 HUDs 一應俱全。
**解決的問題：** 它解決了代理工具鏈擴充碎片化的問題。開發者需要一個統一的平台來管理代理的各種增強功能，而非每個功能都使用不同的工具。
**為何又一個？** 49,000+ 顆星使其成為 oh-my 系列中最受歡迎的專案。安全警告中提到了冒名網站，反映了專案的高知名度和隨之而來的仿冒風險。

---

## 24. [OpenHarness](https://github.com/HKUDS/OpenHarness)
> 開放代理工具鏈——輕量級代理基礎設施。

**Language:** Python  |  **Stars:** 6,934  |  **Forks:** 1,195  |  **Best Score:** 6,487  |  **Best Rank:** #4  |  **Days on chart:** 3/7  |  **Created:** 2026-04-01

**背景：** OpenHarness 是香港大學推出的開放代理工具鏈框架，提供核心輕量級代理基礎設施：工具使用、技能系統、記憶管理和多代理協調。
**解決的問題：** 它解決了代理基礎設施過度複雜的問題。許多代理框架功能臃腫、難以理解。OpenHarness 專注於提供最核心的基礎設施，讓開發者可以在此基礎上靈活建構。
**為何又一個？** 來自學術機構（HKUDS）的專案，以學術嚴謹性為後盾。創建於本週即獲得近 7,000 顆星和 3 天上榜，展現了社群對輕量級代理基礎設施的需求。

---

## 25. [voice-input-src](https://github.com/yetone/voice-input-src)
> macOS 選單列語音輸入應用程式原始碼。

**Language:** all  |  **Stars:** 1,799  |  **Forks:** 190  |  **Best Score:** 6,450  |  **Best Rank:** #7  |  **Days on chart:** 1/7  |  **Created:** 2026-03-29

**背景：** 這是一個 macOS 選單列語音輸入應用的原始碼，使用 Swift 建構。按住 Fn 鍵錄音，釋放後將轉錄文字注入當前焦點輸入欄位。使用 Apple Speech Recognition 框架進行串流轉錄。
**解決的問題：** 它解決了 macOS 原生語音輸入體驗不佳的問題。透過全域 CGEvent 監聽 Fn 鍵，提供無縫的按住即錄語音輸入體驗，無需切換應用。
**為何又一個？** voice-input-src 的獨特之處在於它展示了一個完全由 Claude Code 生成的完整 macOS 應用。其原始碼以 prompt 形式呈現，本身就是 AI 驅動開發的案例研究。

---

## 26. [codex](https://github.com/openai/codex)
> 在終端機中運行的輕量級編程代理。

**Language:** Rust  |  **Stars:** 73,603  |  **Forks:** 10,352  |  **Best Score:** 6,370  |  **Best Rank:** #10  |  **Days on chart:** 2/7  |  **Created:** 2025-04-13

**背景：** Codex CLI 是 OpenAI 推出的輕量級編程代理，在終端機中本地運行。提供 CLI 和桌面應用（通過 Homebrew Cask 安裝），支援 VS Code、Cursor 和 Windsurf 等 IDE 整合。
**解決的問題：** 它解決了開發者需要 OpenAI 驅動的本地編程代理的需求。與雲端 API 呼叫不同，Codex CLI 在本地執行，提供更快的回應速度和更好的隱私保護。
**為何又一個？** 作為 OpenAI 官方產品，Codex CLI 是 Claude Code 的直接競爭者。73,000+ 顆星展現了其強大的市場影響力。本週 2 天上榜反映了代理編程工具市場的激烈競爭。

---

## 27. [timesfm](https://github.com/google-research/timesfm)
> 由 Google Research 開發的時間序列基礎模型，用於時間序列預測。

**Language:** Python  |  **Stars:** 15,252  |  **Forks:** 1,336  |  **Best Score:** 6,326  |  **Best Rank:** #7  |  **Days on chart:** 3/7  |  **Created:** 2024-04-29

**背景：** TimesFM 是 Google Research 開發的預訓練時間序列基礎模型。論文發表於 ICML 2024，模型權重在 Hugging Face 上公開。它採用僅解碼器架構進行時間序列預測。
**解決的問題：** 它解決了時間序列預測需要針對每個場景單獨訓練模型的問題。作為基礎模型，TimesFM 可以零樣本或少樣本適應各種時間序列預測任務，大幅降低部署門檻。
**為何又一個？** 來自 Google Research 的學術血統和 ICML 發表的論文為其品質背書。本週 3 天上榜，15,000+ 顆星反映了時間序列預測領域對基礎模型方法的廣泛興趣。

---

## 28. [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks)
> 從 ChatGPT、Claude、Gemini、Grok、Perplexity 等提取的系統提示詞。定期更新。

**Language:** all  |  **Stars:** 37,709  |  **Forks:** 6,211  |  **Best Score:** 6,254  |  **Best Rank:** #7  |  **Days on chart:** 3/7  |  **Created:** 2025-05-03

**背景：** 這是一個收集各大 AI 系統提示詞洩漏的倉庫，涵蓋 GPT-5.4、Claude Opus 4.6、Gemini 3.1 Pro、Grok 4.2 等最新模型。定期更新以反映各平台的最新系統提示詞。
**解決的問題：** 它解決了 AI 從業者和研究者對主流 AI 系統內部提示詞的好奇和研究需求。了解這些系統提示詞有助於更好地理解 AI 產品的行為模式和設計哲學。
**為何又一個？** 37,000+ 顆星反映了社群對 AI 系統透明度的高度興趣。本週 3 天上榜，持續跟進最新的模型版本（如 Codex、Claude Code）使其保持時效性。

---

## 29. [prompts.chat](https://github.com/f/prompts.chat)
> 前身為 Awesome ChatGPT Prompts。分享、發現和收集社群提示詞。免費開源，支援組織自託管。

**Language:** HTML  |  **Stars:** 157,821  |  **Forks:** 20,657  |  **Best Score:** 6,160  |  **Best Rank:** #8  |  **Days on chart:** 3/7  |  **Created:** 2022-12-05

**背景：** prompts.chat 是全球最大的開源 AI 提示詞庫，前身為 Awesome ChatGPT Prompts。使用者可以分享、發現和收集來自社群的提示詞。支援自託管以保護組織隱私。
**解決的問題：** 它解決了高品質提示詞分散在各處的問題。開發者和使用者需要一個集中的平台來發現和分享有效的提示詞範本。
**為何又一個？** 157,000+ 顆星使其成為 GitHub 上最受歡迎的 AI 相關專案之一。品牌升級為 prompts.chat 並新增自託管支援，展現了專案的持續進化。本週 3 天上榜。

---

## 30. [cs-video-courses](https://github.com/Developer-Y/cs-video-courses)
> 附帶影片講座的電腦科學課程清單。

**Language:** all  |  **Stars:** 79,585  |  **Forks:** 10,945  |  **Best Score:** 6,140  |  **Best Rank:** #13  |  **Days on chart:** 2/7  |  **Created:** 2016-10-21

**背景：** 這是一份精心整理的電腦科學課程清單，所有課程都附帶影片講座。涵蓋從演算法、作業系統到機器學習等電腦科學的各個分支。
**解決的問題：** 它解決了優質電腦科學教育資源分散在各平台的問題。學習者需要一個集中的目錄來發現和規劃自己的學習路徑。
**為何又一個？** 79,000+ 顆星和近十年的持續維護使其成為電腦科學自學的標準參考。本週 2 天上榜展現了長尾教育資源的持久價值。

---

## 31. [coding-interview-university](https://github.com/jwasham/coding-interview-university)
> 成為軟體工程師的完整電腦科學學習計畫。

**Language:** all  |  **Stars:** 340,398  |  **Forks:** 81,887  |  **Best Score:** 6,098  |  **Best Rank:** #8  |  **Days on chart:** 3/7  |  **Created:** 2016-06-06

**背景：** 由 John Washam 創建的完整學習計畫，他透過此計畫成功被 Amazon 錄取。涵蓋資料結構、演算法、系統設計等軟體工程面試所需的全部知識。
**解決的問題：** 它解決了轉職和自學軟體工程師缺乏系統性學習路徑的問題。340,000+ 顆星證明了它作為面試準備資源的無可替代地位。
**為何又一個？** 作為 GitHub 上星數最高的專案之一，coding-interview-university 的上榜是常態。本週 3 天上榜反映了持續不斷的新開發者群體加入軟體工程領域。

---

## 32. [android-sms-gateway](https://github.com/capcom6/android-sms-gateway)
> Android SMS 閘道應用，透過 API 收發簡訊，支援裝置直連或雲端伺服器。

**Language:** Kotlin  |  **Stars:** 3,522  |  **Forks:** 602  |  **Best Score:** 5,985  |  **Best Rank:** #6  |  **Days on chart:** 1/7  |  **Created:** 2022-06-15

**背景：** 這是一個將 Android 手機轉變為 SMS 閘道的應用。透過 API 介面收發簡訊，支援裝置直連存取或透過雲端伺服器中繼（當裝置無法直接存取時）。
**解決的問題：** 它解決了企業和開發者需要低成本 SMS 發送能力的問題。商業 SMS 服務按訊息計費，而利用 Android 裝置的原生簡訊功能可以大幅降低成本。
**為何又一個？** android-sms-gateway 以其雙模式架構（直連和雲端）脫穎而出。Kotlin 原生建構確保了與 Android 平台的最佳相容性。3,500+ 顆星對於如此特定的工具而言相當可觀。

---

## 33. [fff.nvim](https://github.com/dmtrKovalenko/fff.nvim)
> 最快速、最精確的檔案搜尋工具包，適用於 AI 代理、Neovim、Rust、C 和 NodeJS。

**Language:** Rust  |  **Stars:** 3,829  |  **Forks:** 160  |  **Best Score:** 5,762  |  **Best Rank:** #9  |  **Days on chart:** 2/7  |  **Created:** 2025-07-31

**背景：** FFF 是一個高速檔案搜尋工具包，專為 AI 代理和 Neovim 使用者設計。提供 MCP 整合、Neovim 外掛、Rust/C/NodeJS 綁定，內建記憶功能以優化重複搜尋。
**解決的問題：** 它解決了 AI 代理在大型程式碼庫中進行檔案搜尋效能不足的問題。傳統的 grep/find 工具缺乏針對 AI 代理使用場景的優化。FFF 透過內建記憶和多語言綁定，提供極速的搜尋體驗。
**為何又一個？** FFF 以其「最快」的定位和多運行時支援脫穎而出。Rust 核心建構確保了極致效能，同時透過 MCP 伺服器原生支援 AI 代理整合。本週 2 天上榜。

---

## 34. [Recordly](https://github.com/webadderall/Recordly)
> 免費建立精美的螢幕錄影。開源螢幕錄影器，支援自動縮放、動畫游標和自動字幕。

**Language:** TypeScript  |  **Stars:** 5,235  |  **Forks:** 361  |  **Best Score:** 5,436  |  **Best Rank:** #13  |  **Days on chart:** 2/7  |  **Created:** 2026-03-12

**背景：** Recordly 是一個開源螢幕錄影工具，支援 Mac、Windows 和 Linux。它能自動新增縮放效果、動畫游標和自動字幕，將普通的螢幕錄影轉化為專業級展示影片。
**解決的問題：** 它解決了螢幕錄影後製需要專業技能和昂貴軟體的問題。自動縮放和動畫游標等功能通常需要手動在影片編輯軟體中添加。Recordly 將這些步驟自動化。
**為何又一個？** 與 OpenScreen 類似但更專注於錄影後製功能（自動縮放、字幕）。AGPL 3.0 授權確保了開源的持久性。本週與 OpenScreen 同時上榜，展現了螢幕錄影工具市場的旺盛需求。

---

## 35. [hermes-agent](https://github.com/NousResearch/hermes-agent)
> 與你一同成長的代理。

**Language:** Python  |  **Stars:** 26,562  |  **Forks:** 3,478  |  **Best Score:** 5,333  |  **Best Rank:** #9  |  **Days on chart:** 4/7  |  **Created:** 2025-07-22

**背景：** Hermes Agent 是 Nous Research 推出的 AI 代理框架，強調「與使用者一同成長」的設計理念。它建構在 Hermes 系列模型之上，提供可擴展的代理能力。
**解決的問題：** 它解決了代理缺乏長期適應性的問題。大多數代理每次會話都從零開始，無法根據使用者的使用模式和偏好進行調整。Hermes Agent 透過成長機制持續優化。
**為何又一個？** Nous Research 在開源 LLM 社群中享有盛譽。26,000+ 顆星和本週 4 天上榜展現了社群對「可成長代理」理念的認同。活躍的 Discord 社群提供了持續的支援。

---

## 36. [TaxHacker](https://github.com/vas3k/TaxHacker)
> 自託管 AI 記帳應用。LLM 分析收據、發票和交易，支援自訂提示詞和類別。

**Language:** TypeScript  |  **Stars:** 4,889  |  **Forks:** 750  |  **Best Score:** 5,110  |  **Best Rank:** #10  |  **Days on chart:** 1/7  |  **Created:** 2025-03-10

**背景：** TaxHacker 是一個自託管的 AI 記帳工具。它使用 LLM 分析收據、發票和銀行交易，支援自訂提示詞和類別分類。所有數據都保存在本地，保護財務隱私。
**解決的問題：** 它解決了個人和小型企業記帳繁瑣的問題。手動分類交易和處理收據既耗時又容易出錯。TaxHacker 透過 AI 自動化分類和分析流程。
**為何又一個？** TaxHacker 以其自託管和隱私保護設計脫穎而出。財務數據的敏感性使得雲端方案不被所有人接受。MIT 授權和近 5,000 顆星展現了其在自託管社群中的影響力。

---

## 37. [autoagent](https://github.com/kevinrgu/autoagent)
> 自主工具鏈工程。

**Language:** Python  |  **Stars:** 3,726  |  **Forks:** 422  |  **Best Score:** 5,000  |  **Best Rank:** #6  |  **Days on chart:** 2/7  |  **Created:** 2026-04-02

**背景：** AutoAgent 是一個自主工具鏈工程框架，由 Third Layer 團隊開發。它專注於建構能自行配置的代理系統，減少人工介入的需求。
**解決的問題：** 它解決了代理系統需要大量手動配置的問題。傳統的代理框架需要開發者精心設計工具鏈和工作流程。AutoAgent 讓代理能自主決定如何組織和使用工具。
**為何又一個？** AutoAgent 以「自主工程」的理念脫穎而出——讓代理不只使用工具，還能設計自己的工具鏈。創建僅數天即上榜，反映了社群對更高自主性代理的期待。

---

## 38. [opencode](https://github.com/anomalyco/opencode)
> 開源編程代理。

**Language:** TypeScript  |  **Stars:** 138,763  |  **Forks:** 15,332  |  **Best Score:** 4,943  |  **Best Rank:** #15  |  **Days on chart:** 3/7  |  **Created:** 2025-04-30

**背景：** OpenCode 是一個開源 AI 編程代理，由 Anomaly 團隊維護。作為 Claude Code 和 Codex CLI 的開源替代方案，它提供了完整的終端機編程代理體驗。
**解決的問題：** 它解決了主流編程代理為封閉源碼的問題。開發者希望擁有一個完全透明、可審計和可定製的編程代理。OpenCode 提供了這樣的開源選項。
**為何又一個？** 138,000+ 顆星使其成為最受歡迎的開源編程代理。本週 3 天上榜展現了在 Claude Code 和 Codex 之外，社群對開源替代方案的持續需求。

---

## 39. [shannon](https://github.com/KeygraphHQ/shannon)
> Shannon Lite 是一個自主的白盒 AI 滲透測試器，用於 Web 應用和 API。分析原始碼、辨識攻擊向量、執行真實漏洞利用。

**Language:** TypeScript  |  **Stars:** 37,028  |  **Forks:** 3,915  |  **Best Score:** 4,896  |  **Best Rank:** #7  |  **Days on chart:** 1/7  |  **Created:** 2025-09-27

**背景：** Shannon 是 Keygraph 推出的 AI 滲透測試工具。它分析原始碼以辨識攻擊向量，並執行真實的漏洞利用來證明安全問題。現可透過 `npx @keygraph/shannon` 直接使用。
**解決的問題：** 它解決了安全測試需要專業知識和大量時間的問題。傳統滲透測試需要經驗豐富的安全工程師手動操作。Shannon 將這個流程自動化，在程式碼到達生產環境前發現漏洞。
**為何又一個？** Shannon 以「白盒」和「自主」兩大特點脫穎而出。不同於黑盒掃描器，它分析原始碼來辨識攻擊面。37,000+ 顆星展現了安全社群對 AI 滲透測試的認可。

---

## 40. [sentrysearch](https://github.com/ssrajadh/sentrysearch)
> 使用 Gemini Embedding 2 或 Qwen3-VL 對影片進行語義搜尋。

**Language:** Python  |  **Stars:** 3,006  |  **Forks:** 293  |  **Best Score:** 4,858  |  **Best Rank:** #16  |  **Days on chart:** 2/7  |  **Created:** 2026-03-17

**背景：** SentrySearch 是一個影片語義搜尋工具。輸入你要尋找的內容描述，它會將影片分割為重疊片段，使用 Gemini Embedding 2 或 Qwen3-VL 進行嵌入，然後返回修剪好的匹配片段。
**解決的問題：** 它解決了在大量影片素材中尋找特定場景的痛點。手動瀏覽監控影片或會議錄影既耗時又低效。SentrySearch 讓使用者用自然語言描述即可定位相關片段。
**為何又一個？** SentrySearch 以其多模型支援（Gemini 和 Qwen3-VL）和作為 OpenClaw Skill 的整合能力脫穎而出。本週 2 天上榜，3,000+ 顆星展現了影片語義搜尋的市場潛力。

---

## 41. [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
> 將任何 PDF 或圖片文件轉化為結構化數據。強大的輕量級 OCR 工具包，支援 100+ 種語言。

**Language:** Python  |  **Stars:** 74,982  |  **Forks:** 10,187  |  **Best Score:** 4,682  |  **Best Rank:** #17  |  **Days on chart:** 2/7  |  **Created:** 2020-05-08

**背景：** PaddleOCR 是百度推出的全球領先 OCR 工具包和文件 AI 引擎。它連接圖片/PDF 與 LLM 之間的橋樑，支援超過 100 種語言的文字辨識。
**解決的問題：** 它解決了 AI 系統需要從圖片和 PDF 中提取文字的基礎需求。在 RAG 和文件理解管線中，OCR 是不可或缺的前處理步驟。PaddleOCR 提供了輕量級但準確的解決方案。
**為何又一個？** 74,000+ 顆星和持續六年的維護使其成為 OCR 領域的標竿。多語言支援和持續的效能優化使其在 Tesseract 等競品中保持競爭力。本週 2 天上榜。

---

## 42. [My-Brain-Is-Full-Crew](https://github.com/gnekt/My-Brain-Is-Full-Crew)
> 由一位記憶力衰退、飲食混亂的博士生打造。8+ 個 AI 代理和 13 個技能管理你的 Obsidian 知識庫。

**Language:** Shell  |  **Stars:** 2,142  |  **Forks:** 218  |  **Best Score:** 4,540  |  **Best Rank:** #8  |  **Days on chart:** 1/7  |  **Created:** 2026-03-21

**背景：** My Brain Is Full Crew 是一個 Obsidian 知識庫管理的 AI 代理團隊。它不僅管理知識，還整合了營養和心理健康模組，因為大腦不是孤立運作的。8+ 個代理負責整理、歸檔、連結、搜尋、轉錄和分類郵件。
**解決的問題：** 它解決了知識管理工具忽視身體和心理健康的問題。大多數「第二大腦」工具只關注資訊組織，忽略了營養和心理狀態對認知的影響。此專案將三者整合。
**為何又一個？** 「由博士生真實需求驅動」的故事引發共鳴。將知識管理、營養追蹤和心理健康整合在一個代理團隊中的做法在同類專案中獨一無二。

---

## 43. [opencli](https://github.com/jackwener/opencli)
> 讓任何網站和工具成為你的 CLI。通用 CLI Hub 和 AI 原生運行時。

**Language:** TypeScript  |  **Stars:** 14,025  |  **Forks:** 1,286  |  **Best Score:** 4,526  |  **Best Rank:** #14  |  **Days on chart:** 2/7  |  **Created:** 2026-03-14

**背景：** OpenCLI 是一個通用 CLI Hub，可以將任何網站、Electron 應用或本地二進位檔轉化為標準化的命令列介面。透過 AGENT.md 整合，AI 代理可以無縫發現、學習和執行這些工具。
**解決的問題：** 它解決了 AI 代理無法直接操作 GUI 應用和網站的問題。透過將各種工具統一為 CLI 介面，代理可以程式化地操作原本需要人類互動的應用。
**為何又一個？** OpenCLI 以「零風險、重用 Chrome 登入」的設計理念脫穎而出。14,000+ 顆星和 AI 原生運行時的定位使其在 CLI 工具領域佔有獨特地位。

---

## 44. [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
> 零伺服器程式碼智能引擎——完全在瀏覽器中運行的知識圖譜建立器，附帶 Graph RAG 代理。

**Language:** TypeScript  |  **Stars:** 24,276  |  **Forks:** 2,718  |  **Best Score:** 4,519  |  **Best Rank:** #9  |  **Days on chart:** 1/7  |  **Created:** 2025-08-02

**背景：** GitNexus 是一個完全在瀏覽器中運行的程式碼知識圖譜工具。放入 GitHub 倉庫或 ZIP 檔案，即可獲得互動式知識圖譜和內建的 Graph RAG 代理，用於程式碼探索。
**解決的問題：** 它解決了理解大型程式碼庫需要伺服器端處理的問題。GitNexus 完全在客戶端運行，無需任何伺服器基礎設施，即可建構程式碼的知識圖譜。
**為何又一個？** 零伺服器架構是其最大賣點——所有計算都在瀏覽器中完成。24,000+ 顆星展現了開發者對低門檻程式碼理解工具的需求。已明確聲明與任何加密貨幣無關。

---

## 45. [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp)
> freeCodeCamp.org 的開源程式碼庫和課程。免費學習數學、程式設計和電腦科學。

**Language:** TypeScript  |  **Stars:** 441,907  |  **Forks:** 44,140  |  **Best Score:** 4,454  |  **Best Rank:** #11  |  **Days on chart:** 2/7  |  **Created:** 2014-12-24

**背景：** freeCodeCamp 是全球最大的免費程式設計學習平台。提供完整的數學、程式設計和電腦科學課程，並頒發免費認證。
**解決的問題：** 它解決了優質程式設計教育資源價格高昂的問題。freeCodeCamp 讓任何人都能免費獲得專業水準的程式設計教育。
**為何又一個？** 作為 GitHub 上星數最高的專案（441,000+），freeCodeCamp 的定期上榜是常態。本週 2 天上榜反映了永不衰退的程式設計學習需求。

---

## 46. [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)
> 團隊優先的 Claude Code 多代理協調框架。

**Language:** TypeScript  |  **Stars:** 25,610  |  **Forks:** 2,352  |  **Best Score:** 4,422  |  **Best Rank:** #12  |  **Days on chart:** 2/7  |  **Created:** 2026-01-09

**背景：** oh-my-claudecode 是 Yeachan Heo 為 Claude Code 打造的團隊優先多代理協調框架。它讓多個 Claude Code 實例能夠作為團隊協同工作，專注於多代理間的協調和通訊。
**解決的問題：** 它解決了單一 Claude Code 實例無法處理需要多代理協作的複雜任務的問題。透過多代理協調，團隊可以同時處理多個相關但獨立的任務。
**為何又一個？** 25,000+ 顆星展現了 Claude Code 使用者對多代理協調的強烈需求。作為 oh-my 系列的一部分，它與 oh-my-codex 和 oh-my-openagent 形成完整的跨平台生態。

---

## 47. [OpenBB](https://github.com/OpenBB-finance/OpenBB)
> 為分析師、量化研究員和 AI 代理打造的金融數據平台。

**Language:** Python  |  **Stars:** 65,513  |  **Forks:** 6,491  |  **Best Score:** 4,388  |  **Best Rank:** #13  |  **Days on chart:** 1/7  |  **Created:** 2020-12-20

**背景：** OpenBB 是一個開源金融數據平台，為分析師、量化研究員和 AI 代理提供統一的數據存取介面。它整合了多個數據來源，提供從市場數據到替代數據的全面覆蓋。
**解決的問題：** 它解決了金融數據來源碎片化的問題。分析師和 AI 代理需要從多個供應商獲取數據。OpenBB 提供統一的 API 介面，簡化了數據存取流程。
**為何又一個？** 65,000+ 顆星使其成為開源金融數據領域的領導者。將 AI 代理列為目標使用者展現了專案對 AI 原生工作流程的前瞻佈局。

---

## 48. [mlx-vlm](https://github.com/Blaizzy/mlx-vlm)
> 在 Mac 上使用 MLX 進行視覺語言模型推理和微調的套件。

**Language:** Python  |  **Stars:** 4,134  |  **Forks:** 439  |  **Best Score:** 4,332  |  **Best Rank:** #15  |  **Days on chart:** 2/7  |  **Created:** 2024-04-16

**背景：** MLX-VLM 是一個專為 Apple Silicon Mac 設計的視覺語言模型工具包。它支援推理和微調，涵蓋 VLM（視覺語言模型）和 Omni 模型（支援音訊和影片）。
**解決的問題：** 它解決了 Mac 使用者無法本地運行視覺語言模型的問題。大多數 VLM 工具針對 NVIDIA GPU 優化，而 MLX-VLM 利用 Apple 的 MLX 框架在 Mac 上實現高效推理。
**為何又一個？** MLX-VLM 填補了 Apple Silicon 生態系統中 VLM 工具的空白。本週 2 天上榜，4,100+ 顆星反映了 Mac 開發者社群對本地 AI 模型運行的需求。

---

## 49. [ministack](https://github.com/Nahuel990/ministack)
> 免費開源的本地 AWS 模擬器——35+ 服務、Terraform 相容、真實資料庫。永久免費、MIT 授權。

**Language:** Python  |  **Stars:** 1,608  |  **Forks:** 84  |  **Best Score:** 4,314  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2026-03-24

**背景：** MiniStack 是一個開源的本地 AWS 模擬器，在單一端口上提供 35+ AWS 服務。支援 Terraform 相容和真實資料庫，讓開發者在本地環境中模擬完整的 AWS 基礎設施。
**解決的問題：** 它解決了開發和測試時需要實際 AWS 帳號的問題。本地模擬 AWS 服務可以避免雲端費用、加速開發迭代，並在離線環境中工作。
**為何又一個？** MiniStack 以「永久免費」和 MIT 授權的承諾脫穎而出。相比 LocalStack 的部分付費模式，MiniStack 完全開源。35+ 服務的覆蓋範圍展現了專案的雄心。

---

## 50. [apfel](https://github.com/Arthur-Ficial/apfel)
> 從命令列使用 Apple Intelligence。透過 FoundationModels 框架在裝置上運行 LLM。無需 API 金鑰、無雲端、無依賴。

**Language:** Swift  |  **Stars:** 3,434  |  **Forks:** 127  |  **Best Score:** 4,128  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2026-03-24

**背景：** apfel 是一個命令列工具，透過 Apple 的 FoundationModels 框架存取 Apple Intelligence。完全在裝置上運行，無需 API 金鑰、無雲端連線、無外部依賴。需要 macOS 26+ 和 Swift 6.3+。
**解決的問題：** 它解決了開發者想在命令列中快速存取 Apple Intelligence 的需求。GUI 應用不適合自動化工作流程，而 apfel 讓 Apple Intelligence 可以被腳本和代理直接呼叫。
**為何又一個？** apfel 是目前唯一透過命令列存取 Apple Intelligence 的開源工具。完全離線運行的特性使其在隱私敏感場景中具有獨特價值。不需要 Xcode 的設計降低了使用門檻。

---

## 51. [pm-skills](https://github.com/phuryn/pm-skills)
> PM Skills 市集：100+ 個代理技能、指令和外掛——從發現到策略、執行、發布和成長。

**Language:** all  |  **Stars:** 9,652  |  **Forks:** 1,040  |  **Best Score:** 4,108  |  **Best Rank:** #20  |  **Days on chart:** 1/7  |  **Created:** 2026-03-01

**背景：** PM Skills 是一個產品經理專用的 AI 技能市集。提供 65 個 PM 技能和 36 個鏈式工作流程，涵蓋 8 個外掛，從產品發現到成長策略全面覆蓋。
**解決的問題：** 它解決了產品經理在使用 AI 代理時缺乏專業領域技能的問題。通用代理缺乏 PM 特有的方法論和框架。PM Skills 提供了針對產品管理決策的專業技能集。
**為何又一個？** PM Skills 是少數專門為非工程角色設計的代理技能專案。9,600+ 顆星反映了產品經理社群對 AI 輔助決策工具的需求。100+ 技能的規模在 PM 工具中領先。

---

## 52. [supervision](https://github.com/roboflow/supervision)
> 我們為你編寫可複用的電腦視覺工具。

**Language:** Python  |  **Stars:** 37,746  |  **Forks:** 3,307  |  **Best Score:** 3,884  |  **Best Rank:** #16  |  **Days on chart:** 1/7  |  **Created:** 2022-11-28

**背景：** Supervision 是 Roboflow 推出的電腦視覺工具庫，提供可複用的視覺化、標註和追蹤工具。它與 Roboflow 的推理和自動標註生態系統緊密整合。
**解決的問題：** 它解決了電腦視覺開發中重複編寫基礎工具程式碼的問題。邊界框繪製、物件追蹤、影片處理等常見任務都需要大量樣板程式碼。Supervision 提供開箱即用的解決方案。
**為何又一個？** 37,000+ 顆星使其成為電腦視覺工具庫領域的標竿。與 Roboflow 生態的深度整合提供了從模型訓練到部署的完整工作流程。

---

## 53. [paperclip](https://github.com/paperclipai/paperclip)
> 零人力公司的開源協調框架。

**Language:** TypeScript  |  **Stars:** 47,959  |  **Forks:** 7,734  |  **Best Score:** 3,774  |  **Best Rank:** #15  |  **Days on chart:** 1/7  |  **Created:** 2026-03-02

**背景：** Paperclip 是一個開源協調框架，為「零人力公司」提供基礎設施。它讓 AI 代理能夠自主運營業務流程，從客戶溝通到任務執行全面自動化。
**解決的問題：** 它解決了自動化公司運營需要大量客製化整合的問題。Paperclip 提供統一的協調層，讓多個 AI 代理能夠協作完成完整的業務工作流程。
**為何又一個？** 「零人力公司」的願景使 Paperclip 在代理框架中獨樹一幟。47,000+ 顆星反映了社群對全自動化業務運營的高度興趣。開源性質讓企業能自行審計和定製。

---

## 54. [hackingtool](https://github.com/Z4nzu/hackingtool)
> 駭客專用的一體化滲透測試工具。

**Language:** Python  |  **Stars:** 57,819  |  **Forks:** 6,421  |  **Best Score:** 3,761  |  **Best Rank:** #16  |  **Days on chart:** 1/7  |  **Created:** 2020-04-11

**背景：** HackingTool 是一個將多種安全和滲透測試工具整合在單一介面中的工具包。涵蓋資訊收集、漏洞掃描、密碼破解等多個安全測試類別。
**解決的問題：** 它解決了安全研究者需要管理多個獨立工具的問題。每個滲透測試步驟通常需要不同的工具，而 HackingTool 提供了統一的存取入口。
**為何又一個？** 57,000+ 顆星和六年的持續維護使其成為安全工具領域的經典專案。2.0 版本的架構升級展現了持續的技術投入。

---

## 55. [multica](https://github.com/multica-ai/multica)
> Multica 將編程代理轉變為真正的隊友。像指派同事一樣指派議題給代理。

**Language:** TypeScript  |  **Stars:** 2,213  |  **Forks:** 241  |  **Best Score:** 3,713  |  **Best Rank:** #21  |  **Days on chart:** 1/7  |  **Created:** 2026-01-13

**背景：** Multica 是一個開源平台，將編程代理轉變為團隊成員。代理可以自主接收議題、編寫程式碼、回報阻礙並更新狀態，就像人類同事一樣。
**解決的問題：** 它解決了 AI 代理與團隊工作流程脫節的問題。大多數代理以單次對話模式運作，缺乏與 issue tracker 和團隊溝通工具的整合。Multica 將代理嵌入現有的團隊協作流程。
**為何又一個？** 「你的下十個員工不會是人類」的口號精準定位了產品願景。Multica 不是另一個代理框架，而是將代理整合到團隊管理流程中的橋樑。

---

## 56. [Haven](https://github.com/ancsemi/Haven)
> 自託管私密聊天——無雲端、無遙測、無大型科技公司。Discord 替代方案，運行在你自己的機器上。

**Language:** JavaScript  |  **Stars:** 325  |  **Forks:** 27  |  **Best Score:** 3,506  |  **Best Rank:** #13  |  **Days on chart:** 1/7  |  **Created:** 2026-02-11

**背景：** Haven 是一個自託管的 Discord 替代方案。完全在使用者自己的機器上運行，無雲端依賴、無遙測、無大型科技公司介入。
**解決的問題：** 它解決了 Discord 等主流通訊平台的隱私問題。對於注重隱私的團隊和社群，Haven 提供了一個完全自控的替代方案。
**為何又一個？** Haven 以其極端的隱私立場脫穎而出——「你的伺服器、你的規則、沒有人閱讀你的訊息」。雖然僅 325 顆星，但 3,506 的趨勢分數顯示了社群對隱私優先通訊工具的關注。

---

## 57. [claude-mem](https://github.com/thedotmack/claude-mem)
> Claude Code 外掛，自動擷取會話操作，透過 AI 壓縮，並在未來會話中注入相關上下文。

**Language:** TypeScript  |  **Stars:** 45,965  |  **Forks:** 3,508  |  **Best Score:** 3,418  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2025-08-31

**背景：** claude-mem 是一個 Claude Code 外掛，解決代理記憶的核心問題。它自動擷取每次會話中的操作記錄，使用 Claude agent-sdk 進行 AI 壓縮，然後在未來會話中智能注入相關上下文。
**解決的問題：** 它解決了 AI 代理的「失憶」問題。每次新會話開始時，Claude 都會失去之前的上下文。claude-mem 透過自動記錄和壓縮，建立持久的跨會話記憶。
**為何又一個？** 45,000+ 顆星反映了開發者對代理記憶解決方案的強烈需求。完全自動化的記憶擷取和注入流程，相比手動管理 CLAUDE.md 大幅降低了使用門檻。

---

## 58. [personaplex](https://github.com/NVIDIA/personaplex)
> PersonaPlex 程式碼——語音和角色控制的全雙工對話語音模型。

**Language:** Python  |  **Stars:** 7,819  |  **Forks:** 1,149  |  **Best Score:** 3,362  |  **Best Rank:** #8  |  **Days on chart:** 2/7  |  **Created:** 2026-01-05

**背景：** PersonaPlex 是 NVIDIA 推出的全雙工對話語音模型，支援語音和角色控制。模型權重在 Hugging Face 上公開，論文已在 arXiv 上發表，提供互動式線上 Demo。
**解決的問題：** 它解決了語音 AI 模型缺乏個性化和角色控制的問題。傳統 TTS 系統產生千篇一律的語音，而 PersonaPlex 讓使用者能控制語音的個性特徵。
**為何又一個？** 作為 NVIDIA 官方研究成果，PersonaPlex 在技術深度和可信度上具有獨特優勢。全雙工對話能力使其超越傳統的單向 TTS 系統。本週 2 天上榜。

---

## 59. [ink](https://github.com/vadimdemedes/ink)
> React for 互動式命令列應用。

**Language:** TypeScript  |  **Stars:** 37,290  |  **Forks:** 940  |  **Best Score:** 3,334  |  **Best Rank:** #21  |  **Days on chart:** 1/7  |  **Created:** 2017-06-12

**背景：** Ink 讓開發者使用 React 元件來建構互動式命令列應用。它將 React 的宣告式 UI 模式帶入終端機環境，讓 CLI 開發變得像建構網頁應用一樣直覺。
**解決的問題：** 它解決了傳統 CLI 開發缺乏結構化 UI 框架的問題。命令列應用的輸出管理通常依賴字串拼接和手動游標控制。Ink 透過 React 的元件模型簡化了這個流程。
**為何又一個？** 37,000+ 顆星和九年的持續維護使 Ink 成為 CLI UI 框架的事實標準。隨著 AI 代理 CLI 工具的爆發，Ink 作為底層 UI 框架持續受益。

---

## 60. [flash-moe](https://github.com/danveloper/flash-moe)
> 在小筆電上運行大模型。

**Language:** Objective-C  |  **Stars:** 3,342  |  **Forks:** 391  |  **Best Score:** 3,239  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2026-03-18

**背景：** flash-moe 專注於在資源受限的裝置上運行大型混合專家（MoE）模型。它透過最佳化技術，讓原本需要高階硬體的 MoE 模型能在普通筆電上運行。
**解決的問題：** 它解決了 MoE 模型部署門檻過高的問題。混合專家模型雖然效能強大，但通常需要大量記憶體和計算資源。flash-moe 透過智能卸載和量化使其在消費級硬體上可行。
**為何又一個？** flash-moe 瞄準了一個具體且重要的需求——讓大型 MoE 模型民主化。Objective-C 語言的選擇暗示了對 Apple 生態的深度整合。

---

## 61. [DeepTutor](https://github.com/HKUDS/DeepTutor)
> 代理原生的個人化學習助手。

**Language:** Python  |  **Stars:** 11,698  |  **Forks:** 1,617  |  **Best Score:** 3,230  |  **Best Rank:** #15  |  **Days on chart:** 1/7  |  **Created:** 2025-12-28

**背景：** DeepTutor 是香港大學推出的代理原生個人化學習助手。它採用代理架構來提供適應性學習體驗，根據學習者的進度和理解程度動態調整教學策略。
**解決的問題：** 它解決了線上教育「一體適用」的問題。傳統線上課程無法根據個人學習進度調整。DeepTutor 透過代理技術實現真正的個人化教學。
**為何又一個？** 來自 HKUDS 的學術背景為其教育方法論提供了理論支撐。11,000+ 顆星和 Next.js 16 的現代技術棧展現了專案的技術前沿性。

---

## 62. [OpenMetadata](https://github.com/open-metadata/OpenMetadata)
> 統一的元數據平台——數據發現、可觀測性和治理。

**Language:** TypeScript  |  **Stars:** 9,731  |  **Forks:** 1,769  |  **Best Score:** 3,116  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2021-08-01

**背景：** OpenMetadata 是一個統一的元數據平台，提供數據發現、數據可觀測性和數據治理功能。以中央元數據倉庫為核心，支援深度欄位級別的資料血緣和團隊協作。
**解決的問題：** 它解決了企業數據資產缺乏統一可見性的問題。數據散落在多個系統中，缺乏統一的發現和治理機制。OpenMetadata 提供了一個集中的平台來管理所有數據資產。
**為何又一個？** 9,700+ 顆星和四年的持續開發展現了專案的成熟度。在 AI 驅動的數據管線日益普及的背景下，元數據治理的重要性持續上升。

---

## 63. [phantom](https://github.com/ghostwright/phantom)
> 一個擁有自己電腦的 AI 同事。自我進化、持久記憶、MCP 伺服器、安全憑證收集、電子郵件身份。

**Language:** TypeScript  |  **Stars:** 1,216  |  **Forks:** 145  |  **Best Score:** 3,075  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2026-03-26

**背景：** Phantom 是一個基於 Claude Agent SDK 建構的 AI 同事。它擁有自己的虛擬電腦環境、持久記憶、MCP 伺服器整合、安全憑證管理和電子郵件身份，能自我進化以提升能力。
**解決的問題：** 它解決了 AI 代理缺乏獨立運作環境的問題。大多數代理依附於使用者的會話，缺乏獨立的身份和運算環境。Phantom 為代理提供了完整的「數位人格」。
**為何又一個？** Phantom 以「擁有自己電腦的 AI 同事」的定位脫穎而出。822 個測試通過的統計數據展現了工程嚴謹性。Apache 2.0 授權和 Docker 部署降低了採用門檻。

---

## 64. [gallery](https://github.com/google-ai-edge/gallery)
> 展示裝置端 ML/GenAI 使用案例的展示廳，讓人們在本地嘗試和使用模型。

**Language:** Kotlin  |  **Stars:** 18,293  |  **Forks:** 1,706  |  **Best Score:** 3,053  |  **Best Rank:** #16  |  **Days on chart:** 1/7  |  **Created:** 2025-03-31

**背景：** Google AI Edge Gallery 是一個行動端 AI 展示應用，讓使用者在自己的裝置上體驗最強大的開源大語言模型。它是探索和評估裝置端生成式 AI 的首選平台。
**解決的問題：** 它解決了普通使用者難以體驗裝置端 AI 模型的問題。本地部署模型通常需要技術知識。Gallery 提供了一鍵體驗的方式，讓任何人都能嘗試裝置端 AI。
**為何又一個？** Google 官方出品確保了模型的品質和安全性。18,000+ 顆星展現了行動端 AI 的廣泛興趣。Kotlin 原生建構確保了 Android 平台的最佳體驗。

---

## 65. [drawio-mcp](https://github.com/jgraph/drawio-mcp)
> draw.io 官方 MCP 伺服器，讓 LLM 能建立和開啟圖表。

**Language:** JavaScript  |  **Stars:** 2,544  |  **Forks:** 151  |  **Best Score:** 3,044  |  **Best Rank:** #21  |  **Days on chart:** 1/7  |  **Created:** 2026-02-02

**背景：** 這是 draw.io 的官方 MCP 伺服器。提供四種整合方式（MCP App Server、MCP Tool Server、Skill + CLI、Project Instructions），讓 AI 助手能建立和開啟 draw.io 圖表。
**解決的問題：** 它解決了 AI 代理無法直接建立視覺化圖表的問題。透過 MCP 協定，LLM 可以程式化地生成流程圖、架構圖等視覺化內容，並在 draw.io 編輯器中開啟。
**為何又一個？** 作為 draw.io 官方整合，它是目前最可靠的 AI 圖表生成方案。四種整合方式提供了最大的靈活性。2,500+ 顆星反映了開發者對 AI 驅動圖表的需求。

---

## 66. [TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN)
> 基於多智能體 LLM 的中文金融交易框架——TradingAgents 中文增強版。

**Language:** Python  |  **Stars:** 23,605  |  **Forks:** 4,946  |  **Best Score:** 3,025  |  **Best Rank:** #22  |  **Days on chart:** 1/7  |  **Created:** 2025-06-26

**背景：** TradingAgents-CN 是 TauricResearch/TradingAgents 的中文增強版。它在原版基礎上增加了中文文件、中文市場數據支援和針對中國金融市場的客製化功能。
**解決的問題：** 它解決了原版 TradingAgents 缺乏中文支援和中國市場適配的問題。中國金融市場有其獨特的規則和數據來源，需要專門的適配工作。
**為何又一個？** 23,000+ 顆星超越了原版的 TradingAgents，反映了中文金融科技社群的龐大規模。中文增強版的成功展現了本地化在開源專案中的重要價值。

---

## 67. [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
> 透過從零重建你最愛的技術來精通程式設計。

**Language:** Markdown  |  **Stars:** 486,645  |  **Forks:** 45,791  |  **Best Score:** 2,999  |  **Best Rank:** #20  |  **Days on chart:** 1/7  |  **Created:** 2018-05-09

**背景：** 這是一個精心編寫的逐步指南合集，幫助開發者從零開始重建各種技術。涵蓋 3D 渲染器、AI 模型、區塊鏈、資料庫、Docker、作業系統等數十個類別。
**解決的問題：** 它解決了「知其然不知其所以然」的程式設計學習問題。正如費曼所說：「我無法創造的東西，我就不理解。」透過重建技術來深入理解其原理。
**為何又一個？** 486,000+ 顆星使其成為 GitHub 上星數第二高的專案。經典資源的持續上榜反映了永不衰退的動手學習需求。

---

## 68. [CLI-Anything](https://github.com/HKUDS/CLI-Anything)
> 讓所有軟體成為代理原生——CLI-Hub 提供社群建構的 CLI 一鍵安裝。

**Language:** Python  |  **Stars:** 28,381  |  **Forks:** 2,696  |  **Best Score:** 2,968  |  **Best Rank:** #23  |  **Days on chart:** 1/7  |  **Created:** 2026-03-08

**背景：** CLI-Anything 是香港大學推出的專案，目標是讓所有軟體成為代理原生。它提供了 CLI-Hub 平台，社群可以建構和分享將任何軟體轉化為 CLI 介面的適配器。
**解決的問題：** 它解決了 AI 代理只能操作有 API 的軟體的限制。大量軟體缺乏程式化存取方式，而 CLI-Anything 為這些軟體提供了標準化的命令列介面。
**為何又一個？** 「今天的軟體服務人類，明天的使用者將是代理」——這個願景使 CLI-Anything 在軟體代理化領域具有前瞻性。28,000+ 顆星展現了社群認同。

---

## 69. [magic-resume](https://github.com/JOYCEQL/magic-resume)
> 免費線上 AI 履歷編輯器。

**Language:** TypeScript  |  **Stars:** 4,975  |  **Forks:** 576  |  **Best Score:** 2,952  |  **Best Rank:** #18  |  **Days on chart:** 2/7  |  **Created:** 2024-05-19

**背景：** Magic Resume 是一個免費的線上 AI 履歷編輯器。使用 TanStack Start 和 Framer Motion 建構，提供現代化的編輯體驗和精美的動畫效果。
**解決的問題：** 它解決了履歷製作工具要麼太貴要麼太醜的問題。大多數免費履歷工具功能有限或設計粗糙，而 Magic Resume 在免費的前提下提供了專業級的編輯體驗。
**為何又一個？** 本週 2 天上榜，4,900+ 顆星。AI 驅動的履歷生成和精美的前端設計使其在眾多履歷工具中脫穎而出。Apache 2.0 授權確保了開源的持久性。

---

## 70. [firecrawl](https://github.com/firecrawl/firecrawl)
> AI 的 Web 數據 API——為 AI 代理提供乾淨的網頁數據。

**Language:** TypeScript  |  **Stars:** 105,249  |  **Forks:** 6,862  |  **Best Score:** 2,860  |  **Best Rank:** #21  |  **Days on chart:** 1/7  |  **Created:** 2024-04-15

**背景：** Firecrawl 是一個將網頁轉化為 AI 可消費格式的 API。它爬取網頁並輸出乾淨的 Markdown 或結構化數據，專為 RAG 管線和 AI 代理設計。
**解決的問題：** 它解決了網頁數據雜亂、難以被 AI 直接消費的問題。原始 HTML 包含大量無關標記和樣式，LLM 無法有效處理。Firecrawl 提供乾淨的結構化輸出。
**為何又一個？** 105,000+ 顆星使其成為 AI 網頁數據提取領域的絕對領導者。在 AI 代理需要即時網頁數據的場景中，Firecrawl 已成為事實標準。

---

## 71. [Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam)
> 即時換臉和一鍵影片深度偽造，僅需單張圖片。

**Language:** Python  |  **Stars:** 89,167  |  **Forks:** 12,954  |  **Best Score:** 2,844  |  **Best Rank:** #22  |  **Days on chart:** 1/7  |  **Created:** 2023-09-24

**背景：** Deep-Live-Cam 2.1 提供即時換臉和影片深度偽造能力。只需一張圖片即可實現即時的面部替換，支援影片和即時攝影機輸入。
**解決的問題：** 它解決了影片換臉技術門檻過高的問題。傳統的深度偽造工具需要大量訓練數據和計算資源。Deep-Live-Cam 將流程簡化為單張圖片輸入。
**為何又一個？** 89,000+ 顆星反映了社群對即時換臉技術的高度興趣。2.1 版本的持續更新展現了專案的活躍度。作為一個具爭議性的工具，其影響力不容忽視。

---

## 72. [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering)
> 工具鏈工程的精選工具和指南。

**Language:** all  |  **Stars:** 1,301  |  **Forks:** 84  |  **Best Score:** 2,764  |  **Best Rank:** #23  |  **Days on chart:** 1/7  |  **Created:** 2026-03-29

**背景：** 這是一個精選的工具鏈工程資源合集，涵蓋文章、實踐手冊、基準測試、規範和開源專案。工具鏈工程（harness engineering）是關於塑造 AI 代理周圍環境以使其可靠運作的實踐。
**解決的問題：** 它解決了工具鏈工程領域資源分散的問題。這個跨越上下文工程、評估、可觀測性和安全自主性的交叉領域缺乏系統性的資源彙整。
**為何又一個？** 「工具鏈工程」作為一個新興領域，awesome-harness-engineering 是首批系統性整理此領域資源的專案之一。雖然僅 1,300 顆星，但其定義性的角色使其具有長期價值。

---

## 73. [InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk)
> 無限長度的說話影片生成，支援圖片轉影片和影片轉影片。

**Language:** Python  |  **Stars:** 5,875  |  **Forks:** 1,012  |  **Best Score:** 2,742  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2025-08-14

**背景：** InfiniteTalk 是一個音訊驅動的影片生成模型，專注於稀疏幀影片配音。它能生成無限長度的說話影片，支援從圖片到影片以及從影片到影片的生成方式。
**解決的問題：** 它解決了 AI 生成說話影片長度受限的問題。大多數方法只能生成短片段。InfiniteTalk 透過創新的架構突破了長度限制。
**為何又一個？** InfiniteTalk 以「無限長度」的能力在說話影片生成領域獨樹一幟。學術團隊背景和 5,800+ 顆星展現了技術和社群的雙重認可。

---

## 74. [pi-mono](https://github.com/badlogic/pi-mono)
> AI 代理工具包：編程代理 CLI、統一 LLM API、TUI 和 Web UI 函式庫、Slack bot、vLLM pods。

**Language:** TypeScript  |  **Stars:** 32,635  |  **Forks:** 3,567  |  **Best Score:** 2,675  |  **Best Rank:** #23  |  **Days on chart:** 2/7  |  **Created:** 2025-08-09

**背景：** pi-mono 是 Mario Zechner（libGDX 作者）打造的 AI 代理工具包。包含編程代理 CLI、統一的多 LLM API、終端和 Web UI 函式庫、Slack 機器人和 vLLM 部署 pods。
**解決的問題：** 它解決了 AI 代理開發需要整合多個獨立工具的問題。從 LLM API 到 UI 到部署，每個環節通常需要不同的工具。pi-mono 提供了統一的全棧解決方案。
**為何又一個？** 32,000+ 顆星反映了「一站式工具包」方法的吸引力。來自 libGDX 作者的技術背景為專案的工程品質提供了信心。本週 2 天上榜。

---

## 75. [code-review-graph](https://github.com/tirth8205/code-review-graph)
> Claude Code 的本地知識圖譜。建構程式碼庫的持久地圖，讓 Claude 只讀取相關內容——程式碼審查時減少 6.8x token。

**Language:** Python  |  **Stars:** 5,757  |  **Forks:** 649  |  **Best Score:** 2,617  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2026-02-26

**背景：** code-review-graph 為 Claude Code 建構本地知識圖譜，持久地映射程式碼庫結構。透過讓 Claude 只讀取相關的程式碼區段，大幅減少 token 消耗。
**解決的問題：** 它解決了 AI 代理在大型程式碼庫中浪費大量 token 的問題。知識圖譜讓代理精準定位到相關程式碼，程式碼審查時減少 6.8x、日常任務最多減少 49x 的 token 消耗。
**為何又一個？** 量化的效能提升數據（6.8x 和 49x）是其最大賣點。在 AI 代理使用成本日益受到關注的背景下，這種 token 優化具有直接的經濟價值。5,700+ 顆星。

---

## 76. [qmd](https://github.com/tobi/qmd)
> 迷你 CLI 搜尋引擎——用於文件、知識庫、會議筆記等。完全本地運行。

**Language:** TypeScript  |  **Stars:** 19,409  |  **Forks:** 1,167  |  **Best Score:** 2,540  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2025-12-08

**背景：** QMD（Query Markup Documents）是一個裝置端搜尋引擎，用於索引 Markdown 筆記、會議記錄和知識庫。結合 BM25 全文搜尋、向量語義搜尋和 LLM 重排序，全部透過 node-llama-cpp 在本地運行。
**解決的問題：** 它解決了個人知識管理中搜尋效率低下的問題。隨著筆記和文件的累積，找到相關內容變得越來越困難。QMD 提供了關鍵字和語義雙重搜尋能力。
**為何又一個？** 來自 Shopify CEO Tobi Lutke，qmd 以其技術深度和完全本地運行的設計脫穎而出。19,000+ 顆星反映了知識工作者對高效本地搜尋的需求。

---

## 77. [Awesome-OSINT-For-Everything](https://github.com/Astrosp/Awesome-OSINT-For-Everything)
> 涵蓋滲透測試、逆向搜尋、紅隊操作、資訊收集和漏洞賞金的 OSINT 工具合集。

**Language:** Shell  |  **Stars:** 2,877  |  **Forks:** 352  |  **Best Score:** 2,536  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2022-09-16

**背景：** 這是一個全面的 OSINT（開源情報）工具合集，涵蓋滲透測試、逆向搜尋、紅隊操作、資訊收集、漏洞賞金和信任與安全等多個領域。
**解決的問題：** 它解決了安全專業人員尋找合適 OSINT 工具的需求。不同的任務需要不同的工具，而此合集將幾乎所有相關工具整理在單一文件中。
**為何又一個？** 「Awesome OSINT for Everything」的定位使其成為 OSINT 領域最全面的資源之一。2,800+ 顆星和四年的持續維護展現了安全社群的認可。

---

## 78. [frontend-slides](https://github.com/zarazhangrui/frontend-slides)
> 使用 Claude 的前端技能在 Web 上建立精美的簡報。

**Language:** Shell  |  **Stars:** 13,289  |  **Forks:** 990  |  **Best Score:** 2,530  |  **Best Rank:** #13  |  **Days on chart:** 2/7  |  **Created:** 2026-01-28

**背景：** Frontend Slides 是一個 Claude Code 技能，讓非設計師也能建立精美的 Web 簡報。它使用「展示而非說教」的方式——先生成視覺預覽，讓使用者選擇喜歡的風格，然後據此建立完整簡報。
**解決的問題：** 它解決了建立精美簡報需要設計技能的問題。大多數人缺乏 CSS 和 JavaScript 知識來建立動畫豐富的 HTML 簡報。Frontend Slides 透過 Claude 的能力代勞。
**為何又一個？** 13,000+ 顆星反映了社群對 AI 驅動簡報製作的熱情。本週 2 天上榜，其「展示而非說教」的互動方式在同類工具中獨樹一幟。

---

## 79. [skills](https://github.com/anthropics/skills)
> Agent Skills 的公開倉庫。

**Language:** Python  |  **Stars:** 112,019  |  **Forks:** 12,695  |  **Best Score:** 2,374  |  **Best Rank:** #21  |  **Days on chart:** 1/7  |  **Created:** 2025-09-22

**背景：** 這是 Anthropic 的官方 Agent Skills 倉庫。Skills 是指令、腳本和資源的資料夾，Claude 會動態載入以提升特定任務的表現。標準規範見 agentskills.io。
**解決的問題：** 它解決了 Claude Code 在特定領域缺乏專業知識的問題。透過 Skills 系統，使用者可以教 Claude 如何以可重複的方式完成特定任務。
**為何又一個？** 作為 Anthropic 官方倉庫，它是 Agent Skills 生態的權威來源。112,000+ 顆星反映了 Claude Code 使用者對官方技能的需求。與 agentskills.io 標準的配合確保了生態一致性。

---

## 80. [RedditVideoMakerBot](https://github.com/elebumm/RedditVideoMakerBot)
> 只需一個指令即可建立 Reddit 影片。

**Language:** Python  |  **Stars:** 9,316  |  **Forks:** 2,352  |  **Best Score:** 2,274  |  **Best Rank:** #20  |  **Days on chart:** 1/7  |  **Created:** 2022-05-26

**背景：** RedditVideoMakerBot 是一個自動化 Reddit 影片製作工具。它從 Reddit 擷取內容，自動生成帶有 TTS 語音和視覺效果的影片，無需任何影片編輯或素材組合。
**解決的問題：** 它解決了 Reddit 影片內容創作者需要大量手動工作的問題。從內容擷取到語音合成到影片渲染，整個流程都被自動化。
**為何又一個？** 9,300+ 顆星和四年的持續維護使其成為 Reddit 影片自動化領域的標準工具。簡單的「一個指令」體驗降低了內容創作的門檻。

---

## 81. [ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills)
> 開源 AI 行銷技能——成長實驗、銷售管線、內容營運、外展、SEO 和財務自動化。

**Language:** Python  |  **Stars:** 1,608  |  **Forks:** 351  |  **Best Score:** 2,240  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2026-03-28

**背景：** AI Marketing Skills 是 Single Brain 團隊打造的開源 Claude Code 行銷技能集。這些不是簡單的提示詞，而是完整的工作流程——包含腳本、評分演算法、專家面板和自動化管線。
**解決的問題：** 它解決了行銷團隊缺乏 AI 自動化工作流程的問題。從成長實驗到銷售管線到 SEO 優化，每個行銷環節都有對應的自動化技能。
**為何又一個？** 由「經過實戰驗證、產生數百萬美元營收的管線」背書。與專注於開發者的技能不同，它瞄準行銷和銷售團隊，填補了 AI 技能生態中的重要空白。

---

## 82. [OmniVoice](https://github.com/k2-fsa/OmniVoice)
> 支援 600+ 種語言的高品質語音克隆 TTS。

**Language:** Python  |  **Stars:** 2,035  |  **Forks:** 313  |  **Best Score:** 2,221  |  **Best Rank:** #15  |  **Days on chart:** 1/7  |  **Created:** 2026-03-31

**背景：** OmniVoice 是一個支援超過 600 種語言的高品質語音克隆和文字轉語音系統。模型在 Hugging Face 上公開，提供 Spaces 線上體驗。
**解決的問題：** 它解決了大多數 TTS 系統僅支援少數主流語言的問題。全球有數千種語言，而 OmniVoice 的 600+ 語言覆蓋使其成為最多語言支援的開源 TTS 系統之一。
**為何又一個？** 600+ 種語言的覆蓋範圍在 TTS 領域無與倫比。創建於本週即上榜，展現了多語言 TTS 技術的廣泛需求。語音克隆能力增加了個人化的維度。

---

## 83. [oh-my-mermaid](https://github.com/oh-my-mermaid/oh-my-mermaid)
> 用 Claude Code 將複雜程式碼庫轉化為清晰、可導航的架構圖。

**Language:** TypeScript  |  **Stars:** 754  |  **Forks:** 62  |  **Best Score:** 2,170  |  **Best Rank:** #22  |  **Days on chart:** 1/7  |  **Created:** 2026-03-22

**背景：** oh-my-mermaid 是一個 Claude Code 工具，可以自動分析程式碼庫並生成 Mermaid 格式的架構圖。支援多語言文件（英文、中文、日文、韓文、土耳其文）。
**解決的問題：** 它解決了程式碼庫架構難以視覺化的問題。手動繪製架構圖既耗時又容易過時。oh-my-mermaid 讓 Claude 自動生成並更新架構圖。
**為何又一個？** oh-my-mermaid 以其自動化程度和 Mermaid 格式（可在 GitHub 中直接渲染）脫穎而出。754 顆星但 2,170 的趨勢分數展現了新專案的成長動能。

---

## 84. [reclip](https://github.com/averygan/reclip)
> 從幾乎任何網站下載影片。輕量級、自託管的媒體下載器，附帶乾淨的 Web UI。

**Language:** HTML  |  **Stars:** 1,415  |  **Forks:** 239  |  **Best Score:** 2,132  |  **Best Rank:** #23  |  **Days on chart:** 1/7  |  **Created:** 2026-03-31

**背景：** ReClip 是一個自託管的影片和音訊下載器。貼上 YouTube、TikTok、Instagram、Twitter/X 等 1000+ 個網站的連結，即可下載為 MP4 或 MP3 格式。提供乾淨的 Web UI。
**解決的問題：** 它解決了從多個平台下載影片需要多個工具或付費服務的問題。ReClip 在自託管環境中提供統一的下載介面。
**為何又一個？** ReClip 以其自託管設計和乾淨的 Web UI 脫穎而出。基於 yt-dlp 的後端確保了廣泛的網站相容性。創建於本週即上榜，MIT 授權。

---

## 85. [copilot-cli-for-beginners](https://github.com/github/copilot-cli-for-beginners)
> 學習如何開始使用 GitHub Copilot CLI。

**Language:** all  |  **Stars:** 2,051  |  **Forks:** 1,115  |  **Best Score:** 2,044  |  **Best Rank:** #17  |  **Days on chart:** 1/7  |  **Created:** 2026-02-04

**背景：** 這是 GitHub 官方推出的 Copilot CLI 入門指南。提供 Codespaces 一鍵開發環境，讓初學者能快速體驗和學習 GitHub Copilot CLI 的使用方式。
**解決的問題：** 它解決了新使用者上手 GitHub Copilot CLI 的門檻問題。官方文件通常偏向參考手冊，缺乏循序漸進的教學內容。
**為何又一個？** 作為 GitHub 官方教學資源，它在 Copilot CLI 生態中具有權威地位。1,115 個分支反映了大量使用者透過分支方式學習的模式。

---

## 86. [prompt-in-context-learning](https://github.com/EgoAlpha/prompt-in-context-learning)
> 上下文學習和提示工程的精選資源——掌握 ChatGPT、GPT-3 等 LLM。

**Language:** Jupyter Notebook  |  **Stars:** 2,135  |  **Forks:** 176  |  **Best Score:** 2,008  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2023-03-08

**背景：** 這是 EgoAlpha Lab 推出的開源提示工程指南，提供上下文學習和提示工程的前沿資源。涵蓋 ChatGPT、GPT-3 和 FlanT5 等 LLM 的最新研究和技術。
**解決的問題：** 它解決了提示工程領域研究進展快速但缺乏系統性整理的問題。新的技術和方法不斷湧現，從業者需要一個持續更新的資源中心。
**為何又一個？** 三年的持續更新展現了維護者的投入。學術導向的內容使其在眾多實務導向的提示工程指南中佔有獨特位置。

---

## 87. [memvid](https://github.com/memvid/memvid)
> AI 代理的記憶層。用無伺服器、單檔案記憶層取代複雜的 RAG 管線。

**Language:** Rust  |  **Stars:** 14,610  |  **Forks:** 1,267  |  **Best Score:** 1,992  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2025-05-27

**背景：** Memvid 是一個 AI 代理的記憶層，用單一檔案取代複雜的 RAG 管線。它提供無伺服器的即時檢索和長期記憶能力，讓代理擁有持久的知識儲存。
**解決的問題：** 它解決了 RAG 管線過於複雜的問題。傳統 RAG 需要向量資料庫、嵌入模型和檢索管線的多個元件。Memvid 將所有功能濃縮為單一檔案的記憶層。
**為何又一個？** 14,600+ 顆星反映了「簡化 RAG」的理念引發了廣泛共鳴。無伺服器和單檔案的設計大幅降低了部署複雜度。Rust 建構確保了效能。

---

## 88. [worldmonitor](https://github.com/koala73/worldmonitor)
> 即時全球情報儀表板。AI 驅動的新聞聚合、地緣政治監控和基礎設施追蹤。

**Language:** TypeScript  |  **Stars:** 47,150  |  **Forks:** 7,629  |  **Best Score:** 1,940  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2026-01-08

**背景：** World Monitor 是一個即時全球情報儀表板，整合 AI 驅動的新聞聚合、地緣政治監控和基礎設施追蹤。提供統一的態勢感知介面。
**解決的問題：** 它解決了全球事件監控需要瀏覽多個來源的問題。從新聞到地緣政治到基礎設施狀態，World Monitor 在單一介面中提供全面的態勢感知。
**為何又一個？** 47,000+ 顆星展現了社群對即時全球監控工具的強烈興趣。AI 驅動的新聞聚合和分析能力使其超越傳統的新聞聚合器。

---

## 89. [ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook)
> 所有小初高、大學 PDF 教材。

**Language:** Roff  |  **Stars:** 66,783  |  **Forks:** 14,910  |  **Best Score:** 1,916  |  **Best Rank:** #21  |  **Days on chart:** 1/7  |  **Created:** 2020-01-05

**背景：** ChinaTextbook 是一個中國教育教材合集，包含從小學到大學的所有 PDF 教材。專案起源於對付費販售公共教育資源的反擊，致力於義務教育的普及和消除教育不平等。
**解決的問題：** 它解決了海外華人和偏遠地區學生難以獲取中國教育教材的問題。同時對抗了在電商平台上販售帶有私人浮水印的免費公共教育資源的行為。
**為何又一個？** 66,000+ 顆星和近 15,000 分支展現了龐大的使用者基礎。其社會使命——讓海外華人子女能繼續了解國內教育——賦予了專案深層意義。

---

## 90. [autoskills](https://github.com/midudev/autoskills)
> 一個指令。你的整個 AI 技能堆疊。已安裝。

**Language:** JavaScript  |  **Stars:** 1,049  |  **Forks:** 101  |  **Best Score:** 1,863  |  **Best Rank:** #23  |  **Days on chart:** 1/7  |  **Created:** 2026-03-25

**背景：** autoskills 是一個自動技能安裝器。它掃描你的專案，偵測技術棧，然後從 skills.sh 自動安裝最匹配的 AI 代理技能。只需 `npx autoskills` 即可完成。
**解決的問題：** 它解決了手動尋找和安裝 AI 代理技能的繁瑣流程。開發者需要瀏覽技能目錄、評估相容性並逐一安裝。autoskills 將整個流程自動化為一個指令。
**為何又一個？** autoskills 以「一個指令」的極簡體驗脫穎而出。來自知名西班牙語開發者社群 midudev 的推出，確保了在特定受眾中的影響力。

---

## 91. [agent-framework](https://github.com/microsoft/agent-framework)
> 建構、協調和部署 AI 代理及多代理工作流程的框架，支援 Python 和 .NET。

**Language:** Python  |  **Stars:** 9,060  |  **Forks:** 1,475  |  **Best Score:** 1,828  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2025-04-28

**背景：** Microsoft Agent Framework 是一個用於建構、協調和部署 AI 代理的框架。支援 Python 和 .NET 雙語言，整合了 Microsoft Foundry 生態系統。
**解決的問題：** 它解決了企業建構多代理系統需要大量基礎設施工作的問題。從代理定義到協調到部署，Microsoft Agent Framework 提供了端到端的企業級解決方案。
**為何又一個？** 作為 Microsoft 官方框架，它在企業級代理部署中具有天然優勢。Python 和 .NET 的雙語言支援覆蓋了企業開發者的主要技術棧。與 Microsoft Learn 文件的整合降低了學習成本。

---

## 92. [velxio](https://github.com/davidmonterocrespo24/velxio)
> 在瀏覽器中模擬 Arduino、ESP32 和 Raspberry Pi。19 種真實開發板，無需硬體。

**Language:** TypeScript  |  **Stars:** 1,284  |  **Forks:** 104  |  **Best Score:** 1,802  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2026-03-03

**背景：** Velxio 是一個完全在瀏覽器中運行的多板模擬器。支援 19 種開發板（Arduino Uno、ESP32、Raspberry Pi Pico 等）、5 種 CPU 架構和 48+ 互動式電子元件。使用 QEMU 進行真實 CPU 模擬。
**解決的問題：** 它解決了嵌入式開發需要實體硬體的門檻問題。購買和連接開發板是學習嵌入式系統的第一道障礙。Velxio 讓任何人都能在瀏覽器中開始編程。
**為何又一個？** Velxio 以 19 種板、5 種架構和 48+ 元件的覆蓋範圍在瀏覽器模擬器中領先。完全無需硬體、無需安裝的體驗大幅降低了嵌入式開發的入門門檻。

---

> **本週主題：** 代理工具鏈（harness）的開放與重構成為核心主題——從 Claw Code 的分叉爭議到 OpenHarness 的學術方案，再到 awesome-harness-engineering 定義新領域，社群正加速解構和重建 AI 代理的底層基礎設施。與此同時，代理技能生態持續擴張至行銷、產品管理和求職等非工程領域，標誌著 AI 代理從「開發者工具」邁向「全職業工具」的轉型。
