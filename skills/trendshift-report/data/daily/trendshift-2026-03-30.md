# Trendshift Report — 2026-03-30
**Total:** 25 repositories

---

## 1. [pretext](https://github.com/chenglou/pretext)
> Fast, accurate & comprehensive text measurement & layout

**Language:** TypeScript  |  **Stars:** 39,924  |  **Forks:** 2,122  |  **Score:** 37,848  |  **Created:** 2026-03-07

**Background:** Pretext by chenglou is a pure JavaScript/TypeScript library for multiline text measurement and layout that sidesteps DOM measurements entirely. Released just three weeks ago, it has exploded to nearly 40,000 stars, claiming the top trending spot with a score nearly four times the runner-up.

**Problem it solves:** DOM-based text measurement methods like `getBoundingClientRect` and `offsetHeight` trigger layout reflow — one of the most expensive operations in the browser. Pretext implements its own measurement logic using the browser's font engine as ground truth, enabling fast text layout without costly reflows.

**Why another one?** Pretext supports rendering to DOM, Canvas, SVG, and soon server-side — a breadth no existing library matches. Its pure-JS approach means zero native dependencies, and its comprehensive support for complex scripts and languages goes far beyond what typical text measurement utilities handle.

---

## 2. [VibeVoice](https://github.com/microsoft/VibeVoice)
> Open-Source Frontier Voice AI

**Language:** Python  |  **Stars:** 36,265  |  **Forks:** 4,144  |  **Score:** 10,272  |  **Created:** 2025-08-25

**Background:** VibeVoice is Microsoft's open-source frontier voice AI platform, covering text-to-speech, automatic speech recognition, and audio processing. With over 36,000 stars since its August 2025 launch, it has established itself as a leading open-source voice AI toolkit with published research papers on both TTS and ASR.

**Problem it solves:** Building production-quality voice AI requires piecing together separate TTS, ASR, and audio processing systems, each with different APIs, model formats, and quality levels. VibeVoice provides a unified, research-backed platform that covers the full voice AI pipeline in one package.

**Why another one?** Microsoft's research backing gives VibeVoice published, peer-reviewed quality benchmarks that most open-source voice tools lack. The unified architecture across TTS and ASR means consistent quality and simpler integration compared to stitching together independent projects.

---

## 3. [TREK](https://github.com/mauriceboe/TREK)
> A self-hosted travel/trip planner with real-time collaboration, interactive maps, PWA support, SSO, budgets, packing lists, and more.

**Language:** TypeScript  |  **Stars:** 3,714  |  **Forks:** 327  |  **Score:** 8,794  |  **Created:** 2026-03-19

**Background:** TREK by mauriceboe is a self-hosted travel and trip planner built with TypeScript, offering real-time collaboration, interactive maps, and PWA support. Released just eleven days ago, it has already gained over 3,700 stars, reflecting strong demand for privacy-respecting travel planning tools.

**Problem it solves:** Cloud-based trip planners like Google Trips or TripIt lock users into proprietary platforms with limited customization. TREK gives travelers full ownership of their data while providing features like budgets, packing lists, SSO, and real-time collaboration with travel companions.

**Why another one?** The self-hosted angle is the differentiator — users maintain full control over their travel data, itineraries, and personal information. The real-time collaboration feature and PWA support make it practical for group travel planning without requiring everyone to create accounts on a third-party service.

---

## 4. [claude-howto](https://github.com/luongnv89/claude-howto)
> A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value.

**Language:** Python  |  **Stars:** 20,611  |  **Forks:** 2,462  |  **Score:** 8,667  |  **Created:** 2025-11-07

**Background:** Claude HowTo by luongnv89 is a comprehensive, visual guide to Claude Code that covers everything from basic concepts to advanced agent orchestration. With over 20,000 stars and a former number-one GitHub trending position, it has become one of the most popular Claude Code learning resources available.

**Problem it solves:** Claude Code's capabilities are vast but poorly documented through official channels alone. Developers need practical, copy-paste examples that demonstrate real workflows — from simple file editing to multi-agent orchestration — rather than abstract API references.

**Why another one?** The visual, example-driven approach distinguishes it from text-heavy documentation. Each concept comes with ready-to-use templates that deliver immediate value, lowering the barrier from "understanding the concept" to "using it in production" to a single copy-paste.

---

## 5. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 135,699  |  **Forks:** 11,370  |  **Score:** 8,260  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent is the dominant agentic skills framework and development methodology, now at over 135,000 stars. It enforces a structured spec-plan-implement-review workflow where the agent teases out a spec, presents it in digestible chunks, builds an implementation plan, then executes through subagent-driven development with review cycles.

**Problem it solves:** Coding agents left to their own devices jump straight into writing code without understanding requirements. Superpowers enforces discipline: spec first, then plan, then implement with TDD and YAGNI principles, ensuring agents produce well-planned, maintainable code rather than rushed implementations.

**Why another one?** At 135,000 stars, Superpowers has become the reference implementation for structured agent development. Its composable skills architecture allows teams to adopt individual practices or the full methodology, and its sustained growth demonstrates that the community has validated this approach at massive scale.

---

## 6. [prompt-master](https://github.com/nidhinjs/prompt-master)
> A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention

**Language:** N/A  |  **Stars:** 4,690  |  **Forks:** 448  |  **Score:** 5,812  |  **Created:** 2026-03-11

**Background:** Prompt Master by nidhinjs is a Claude skill that generates optimized prompts for any AI tool — from Claude and ChatGPT to Midjourney and Stable Diffusion. Released less than three weeks ago, it has gained nearly 4,700 stars by promising zero wasted tokens and full context retention across interactions.

**Problem it solves:** Users waste significant tokens and credits iterating on poorly structured prompts across different AI tools. Prompt Master writes accurate, tool-specific prompts on the first attempt, eliminating the re-prompting cycle that burns through API credits and context windows.

**Why another one?** The breadth of supported tools is the standout feature — it handles not just LLMs (Claude, ChatGPT, Gemini) but also image generators (Midjourney, DALL-E), video tools (Sora, Runway), and automation platforms (Zapier, Make). This cross-tool coverage means users learn one skill instead of mastering prompt engineering for each tool individually.

---

## 7. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> practice made claude perfect

**Language:** HTML  |  **Stars:** 32,070  |  **Forks:** 2,930  |  **Score:** 5,421  |  **Created:** 2025-10-31

**Background:** Claude Code Best Practice by shanraisshan is a community-maintained guide documenting proven patterns, tips, and implementation strategies for Claude Code. Actively maintained and recently updated for Claude Code v2.1.92, it has grown to over 32,000 stars as the go-to practitioner reference.

**Problem it solves:** Claude Code is powerful but has a steep learning curve — users discover effective patterns only through weeks of trial and error. This repository consolidates community-learned best practices, orchestration workflows, and implementation patterns into a single, continuously updated reference.

**Why another one?** Unlike official documentation that focuses on features and APIs, this repository captures the practitioner perspective — what actually works in daily use, common pitfalls, and workflow patterns that emerge from real-world usage across diverse projects and team sizes.

---

## 8. [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)
> Teams-first Multi-agent orchestration for Claude Code

**Language:** TypeScript  |  **Stars:** 24,305  |  **Forks:** 2,215  |  **Score:** 4,988  |  **Created:** 2026-01-09

**Background:** Oh My ClaudeCode by Yeachan Heo is a teams-first multi-agent orchestration framework for Claude Code, available as an npm package. With over 24,000 stars and translations in seven languages (Korean, Chinese, Japanese, Spanish, Vietnamese, Portuguese), it has built a global community around collaborative agent workflows.

**Problem it solves:** Running Claude Code as a single agent limits throughput on complex projects. Oh My ClaudeCode enables teams to orchestrate multiple Claude Code agents simultaneously, with coordination mechanisms that prevent conflicts and ensure consistent output across parallel workstreams.

**Why another one?** The "teams-first" philosophy prioritizes collaboration patterns that existing orchestration tools treat as secondary. The seven-language README translations demonstrate a commitment to global accessibility, and the npm-based distribution makes installation trivial for any TypeScript/JavaScript project.

---

## 9. [hackingtool](https://github.com/Z4nzu/hackingtool)
> ALL IN ONE Hacking Tool For Hackers

**Language:** Python  |  **Stars:** 57,819  |  **Forks:** 6,421  |  **Score:** 4,796  |  **Created:** 2020-04-11

**Background:** HackingTool by Z4nzu is an all-in-one hacking toolkit for security researchers and pentesters, now at version 2.0 with over 57,000 stars. Originally launched in 2020, it bundles dozens of security tools into a single menu-driven interface covering reconnaissance, exploitation, post-exploitation, and forensics.

**Problem it solves:** Security researchers need to install, configure, and learn dozens of separate tools for different phases of penetration testing. HackingTool provides a unified launcher that organizes these tools by category — from AnonSurf to SQLMap — reducing setup time and context switching.

**Why another one?** The six-year track record and 57,000-star community validate its approach as a curated meta-tool rather than yet another security framework. Version 2.0's modernization (Python 3.10+, SVG branding) shows continued investment, and its menu-driven interface makes it accessible to security professionals who are not command-line experts.

---

## 10. [paperclip](https://github.com/paperclipai/paperclip)
> Open-source orchestration for zero-human companies

**Language:** TypeScript  |  **Stars:** 47,959  |  **Forks:** 7,734  |  **Score:** 4,482  |  **Created:** 2026-03-02

**Background:** Paperclip by PaperclipAI is an open-source orchestration platform designed for fully autonomous, zero-human companies. Released less than a month ago, it has already reached nearly 48,000 stars — a staggering growth rate that reflects intense interest in fully autonomous business operations.

**Problem it solves:** Running a company without human operators requires orchestrating AI agents across all business functions — from customer service to engineering to finance — with reliable handoffs and decision-making. Paperclip provides the coordination layer that makes autonomous business operations possible.

**Why another one?** The "zero-human companies" framing is deliberately provocative and positions Paperclip at the extreme end of automation. While other orchestration tools optimize human-AI collaboration, Paperclip is architected for full autonomy, making it the natural choice for teams exploring the boundary of what AI can run independently.

---

## 11. [ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)
> Clone any website with one command using AI coding agents

**Language:** TypeScript  |  **Stars:** 7,790  |  **Forks:** 1,037  |  **Score:** 4,145  |  **Created:** 2026-03-13

**Background:** AI Website Cloner Template by JCodesMore is a reusable template for reverse-engineering any website into a clean, production-ready codebase using AI coding agents. Released just over two weeks ago, it has accumulated nearly 8,000 stars and over 1,000 forks, indicating strong community interest in AI-driven website reproduction.

**Problem it solves:** Recreating an existing website's design and functionality from scratch is time-consuming, requiring manual inspection of layouts, styles, and interactions. This template automates the process — a single command analyzes a target website and generates a clean implementation.

**Why another one?** The template approach is the differentiator. Rather than being a standalone tool, it provides a reusable starting point that developers can customize for their specific needs. The high fork count relative to stars suggests developers are actively adapting it for their own projects rather than just starring for reference.

---

## 12. [timesfm](https://github.com/google-research/timesfm)
> TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting.

**Language:** Python  |  **Stars:** 15,252  |  **Forks:** 1,336  |  **Score:** 4,004  |  **Created:** 2024-04-29

**Background:** TimesFM by Google Research is a pretrained time-series foundation model for forecasting, published at ICML 2024. With over 15,000 stars and checkpoints available on Hugging Face, it brings the foundation model paradigm to time-series analysis — a domain traditionally dominated by statistical and classical ML methods.

**Problem it solves:** Time-series forecasting typically requires domain-specific feature engineering and model tuning for each new dataset. TimesFM provides a decoder-only foundation model that generalizes across domains, enabling zero-shot and few-shot forecasting without the overhead of traditional pipeline construction.

**Why another one?** Google Research's backing and ICML publication provide academic credibility that most time-series libraries lack. The decoder-only architecture is a novel approach to time-series that leverages insights from language modeling, and BigQuery integration makes it accessible to enterprise users who work within the Google Cloud ecosystem.

---

## 13. [hermes-agent](https://github.com/NousResearch/hermes-agent)
> The agent that grows with you

**Language:** Python  |  **Stars:** 26,562  |  **Forks:** 3,478  |  **Score:** 3,719  |  **Created:** 2025-07-22

**Background:** Hermes Agent by Nous Research is an adaptive AI agent framework that emphasizes learning and growing alongside its users. With over 26,000 stars and comprehensive documentation, it has built a strong community around the concept of agents that accumulate skills and knowledge over time rather than starting fresh each session.

**Problem it solves:** Most AI agents start from zero with each interaction, losing all context and learned behaviors between sessions. Hermes Agent provides persistent growth — the agent remembers past interactions, learns user preferences, and accumulates capabilities, becoming more useful over time.

**Why another one?** The "grows with you" philosophy fundamentally differentiates Hermes Agent from stateless agent frameworks. Nous Research's expertise in open-source model development brings model-level insights to agent architecture, and the community-driven skill ecosystem means the agent benefits from collective user contributions.

---

## 14. [Agent-Reach](https://github.com/Panniantong/Agent-Reach)
> Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

**Language:** Python  |  **Stars:** 15,203  |  **Forks:** 1,277  |  **Score:** 3,532  |  **Created:** 2026-02-24

**Background:** Agent Reach by Panniantong gives AI agents the ability to read and search across major internet platforms — Twitter, Reddit, YouTube, GitHub, Bilibili, and XiaoHongShu — through a single CLI with zero API fees. At over 15,000 stars in about a month, it has found a large audience among developers building internet-connected agents.

**Problem it solves:** AI agents are effectively blind to the live internet — they cannot read social media discussions, watch videos, or browse forums without expensive API subscriptions or brittle web scraping. Agent Reach provides unified, free access to these platforms through a clean CLI interface.

**Why another one?** The "zero API fees" promise is the killer feature. By avoiding official APIs entirely, Agent Reach eliminates the cost barrier that prevents most agents from accessing internet data. Its bilingual support (Chinese and English) and coverage of both Western (Twitter, Reddit) and Chinese (Bilibili, XiaoHongShu) platforms make it uniquely comprehensive.

---

## 15. [TaxHacker](https://github.com/vas3k/TaxHacker)
> Self-hosted AI accounting app. LLM analyzer for receipts, invoices, transactions with custom prompts and categories

**Language:** TypeScript  |  **Stars:** 4,601  |  **Forks:** 715  |  **Score:** 2,844  |  **Created:** 2025-03-10

**Background:** TaxHacker by vas3k is a self-hosted AI accounting application that uses LLMs to analyze receipts, invoices, and transactions. With over 4,600 stars and a year of development, it provides a privacy-first alternative to cloud accounting services, with custom prompts and categories for personalized financial management.

**Problem it solves:** Managing personal and small business finances requires manually categorizing transactions, scanning receipts, and reconciling invoices — tedious work that cloud services handle but at the cost of sharing sensitive financial data with third parties. TaxHacker automates this locally with AI.

**Why another one?** The self-hosted, privacy-first design is the core differentiator. Financial data is among the most sensitive personal information, and TaxHacker ensures it never leaves the user's infrastructure. The custom prompt system allows users to define their own categorization rules, adapting to any tax jurisdiction or accounting methodology.

---

## 16. [fli](https://github.com/punitarani/fli)
> Google Flights MCP and Python Library

**Language:** Python  |  **Stars:** 1,465  |  **Forks:** 165  |  **Score:** 2,672  |  **Created:** 2025-01-06

**Background:** Fli by punitarani is a Python library and MCP server that provides programmatic access to Google Flights data through reverse-engineered API access. Unlike scraping-based alternatives, it interacts directly with Google Flights' internal API for fast, reliable flight search results.

**Problem it solves:** Searching for flights programmatically requires either expensive commercial APIs or fragile web scrapers that break with every UI change. Fli provides direct API access to Google Flights data without scraping overhead, enabling developers and AI agents to search flights reliably.

**Why another one?** The reverse-engineered direct API approach eliminates the fragility of web scraping and the cost of commercial flight APIs. The MCP server integration makes it natively accessible to AI agents, and the elegant CLI interface serves developers who want quick flight searches from the terminal.

---

## 17. [Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam)
> real time face swap and one-click video deepfake with only a single image

**Language:** Python  |  **Stars:** 89,167  |  **Forks:** 12,954  |  **Score:** 2,561  |  **Created:** 2023-09-24

**Background:** Deep-Live-Cam 2.1 by hacksider is a real-time face swap and video deepfake tool that requires only a single image. With nearly 90,000 stars and over two years of active development, it remains one of the most popular open-source deepfake projects, continuing to trend thanks to version 2.1 improvements.

**Problem it solves:** Creating face swaps and deepfake videos traditionally requires multiple reference images, significant GPU resources, and complex setup. Deep-Live-Cam reduces this to a single image and one click, with real-time processing that enables live streaming applications.

**Why another one?** The real-time capability is the distinguishing feature. While most deepfake tools operate on pre-recorded video, Deep-Live-Cam processes frames live, enabling use cases from entertainment to video conferencing. The single-image requirement lowers the barrier to entry dramatically compared to tools that need training datasets.

---

## 18. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 71,854  |  **Forks:** 11,138  |  **Score:** 2,443  |  **Created:** 2025-10-13

**Background:** Agency Agents by Mark Sitarzewski provides a collection of pre-built AI agent personas for professional roles, now at over 71,000 stars. Each agent has defined personality traits, processes, and deliverable templates covering roles from frontend development to community management, making it a comprehensive agency-in-a-box solution.

**Problem it solves:** Teams adopting AI agents need role-specific system prompts and workflow definitions for every business function. Agency Agents provides these ready-made, eliminating the prompt engineering overhead of creating effective, personality-rich personas from scratch.

**Why another one?** The personality-driven approach — agents with names, quirks, and strong opinions — makes them entertaining and shareable, driving viral adoption. The explosive growth from 61,000 to 72,000 stars in one week demonstrates that the community values opinionated, ready-to-use personas over generic agent templates.

---

## 19. [compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)
> Office Compound Engineering plugin for Claude Code, Codex, and more

**Language:** TypeScript  |  **Stars:** 13,023  |  **Forks:** 999  |  **Score:** 2,388  |  **Created:** 2025-10-09

**Background:** Compound Engineering by Every Inc is a plugin marketplace centered on a development methodology where each unit of engineering work makes subsequent work easier. With over 13,000 stars, it provides AI skills and agents that enforce an 80/20 split — 80% planning and review, 20% execution — to build compounding returns on engineering investment.

**Problem it solves:** Traditional development accumulates technical debt — every feature adds complexity, making the codebase harder to work with over time. Compound Engineering inverts this by codifying knowledge from each task, ensuring that learnings are captured and reused systematically.

**Why another one?** The philosophy of engineering work compounding rather than degrading is the core innovation. While other plugins focus on making individual tasks faster, Compound Engineering optimizes for long-term codebase health. The plugin marketplace model allows the community to contribute reusable components that benefit everyone.

---

## 20. [OpenBB](https://github.com/OpenBB-finance/OpenBB)
> Financial data platform for analysts, quants and AI agents.

**Language:** Python  |  **Stars:** 65,513  |  **Forks:** 6,491  |  **Score:** 2,318  |  **Created:** 2020-12-20

**Background:** OpenBB is a financial data platform for analysts, quants, and AI agents, with over 65,000 stars accumulated since its December 2020 launch. Originally known as OpenBB Terminal, it has evolved into a comprehensive data platform that serves both human analysts and AI-powered financial workflows.

**Problem it solves:** Financial analysts and quants need aggregated data from dozens of sources — market feeds, SEC filings, economic indicators, alternative data — each with different APIs and formats. OpenBB provides a unified platform that normalizes this data for analysis, whether accessed by humans or AI agents.

**Why another one?** OpenBB's five-year track record and 65,000 stars demonstrate staying power in a space littered with abandoned financial tools. The explicit support for AI agents as first-class consumers, alongside human analysts, positions it uniquely at the intersection of traditional finance and the agent economy.

---

## 21. [agent-lightning](https://github.com/microsoft/agent-lightning)
> The absolute trainer to light up AI agents.

**Language:** Python  |  **Stars:** 16,536  |  **Forks:** 1,430  |  **Score:** 2,300  |  **Created:** 2025-06-18

**Background:** Agent Lightning by Microsoft is a training and optimization framework for AI agents, providing tools to evaluate, benchmark, and improve agent performance. With over 16,000 stars and published documentation on GitHub Pages, it offers a structured approach to making agents faster and more capable.

**Problem it solves:** AI agents are difficult to evaluate and optimize systematically — developers typically rely on ad-hoc testing and subjective quality assessments. Agent Lightning provides standardized training, benchmarking, and optimization pipelines that make agent improvement measurable and reproducible.

**Why another one?** Microsoft's institutional backing brings engineering rigor to agent optimization. While most agent frameworks focus on building and running agents, Agent Lightning focuses on the training loop — making existing agents better through systematic evaluation and iteration, a gap few open-source tools address.

---

## 22. [last30days-skill](https://github.com/mvanhorn/last30days-skill)
> AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

**Language:** Python  |  **Stars:** 18,665  |  **Forks:** 1,503  |  **Score:** 2,170  |  **Created:** 2026-01-23

**Background:** Last30Days by mvanhorn is a Claude Code skill that researches any topic across Reddit, X, YouTube, Hacker News, Polymarket, and the broader web from the last 30 days, then synthesizes a grounded summary. At over 18,000 stars, it has become a go-to tool for developers who need to stay current on fast-moving topics.

**Problem it solves:** The AI world and technology landscape reinvent themselves monthly. Staying current requires manually scanning multiple platforms — Reddit threads, X discussions, YouTube videos, Hacker News comments — and synthesizing what the community is actually saying, upvoting, and betting on.

**Why another one?** The 30-day time window is the defining constraint. Unlike general research tools that return stale results, Last30Days guarantees recency. Its multi-platform coverage (including Polymarket prediction markets) provides sentiment and conviction data that pure text analysis misses.

---

## 23. [twenty](https://github.com/twentyhq/twenty)
> Building a modern alternative to Salesforce, powered by the community.

**Language:** TypeScript  |  **Stars:** 43,594  |  **Forks:** 5,820  |  **Score:** 2,157  |  **Created:** 2022-12-01

**Background:** Twenty is the number-one open-source CRM, building a modern alternative to Salesforce with over 43,000 stars and three years of development. It provides a full-featured customer relationship management platform that teams can self-host and customize without enterprise licensing fees.

**Problem it solves:** Salesforce and similar enterprise CRMs are expensive, complex, and opaque. Twenty provides the same core CRM functionality — contact management, deal tracking, email integration, analytics — with full source code access, self-hosting options, and community-driven development.

**Why another one?** The open-source CRM space has had several contenders, but Twenty's sustained three-year development, 43,000 stars, and active community set it apart from projects that launch with fanfare but stall. Its modern tech stack (TypeScript, GraphQL) makes it extensible by today's developers rather than requiring legacy platform expertise.

---

## 24. [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp)
> freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**Language:** TypeScript  |  **Stars:** 441,907  |  **Forks:** 44,140  |  **Score:** 2,146  |  **Created:** 2014-12-24

**Background:** freeCodeCamp is the most-starred project on GitHub with nearly 442,000 stars, providing a comprehensive, free curriculum for learning math, programming, and computer science. After over eleven years of continuous development, it remains a perennial trending presence thanks to its massive community and regular curriculum updates.

**Problem it solves:** Quality programming education is expensive and gatekept by institutions. freeCodeCamp provides a complete, structured curriculum — from basic HTML to machine learning — entirely for free, with certifications that carry real-world recognition from employers.

**Why another one?** As GitHub's most-starred repository, freeCodeCamp's scale is unmatched. Its curriculum is maintained by thousands of contributors and has been used by millions of learners. The longevity (eleven years) and consistent trending presence validate that free, comprehensive programming education has enduring demand.

---

## 25. [OpenSpace](https://github.com/HKUDS/OpenSpace)
> "OpenSpace: Make Your Agents: Smarter, Low-Cost, Self-Evolving" -- Community: https://open-space.cloud/

**Language:** Python  |  **Stars:** 4,204  |  **Forks:** 488  |  **Score:** 1,767  |  **Created:** 2026-03-24

**Background:** OpenSpace by HKUDS is a framework for building smarter, low-cost, self-evolving AI agents. Released just six days ago, it has quickly gained over 4,200 stars by promising 46% fewer tokens, self-evolving skills, and cross-agent experience sharing. Its community platform at open-space.cloud provides a hub for agent collaboration.

**Problem it solves:** AI agents consume excessive tokens because they lack mechanisms to learn from past executions or share knowledge across instances. OpenSpace provides self-evolving skills that improve with use and an experience-sharing system that lets agents benefit from each other's learnings.

**Why another one?** The economics-first framing — 46% fewer tokens, $11K earned in 6 hours — distinguishes OpenSpace from agent frameworks that focus solely on capability. The self-evolving skill architecture means agents improve autonomously over time, and the cross-agent experience sharing creates network effects as more agents join the ecosystem.

---

> **Day's theme:** The trending landscape reveals a maturing agent ecosystem converging on two fronts — infrastructure refinement (text layout engines, voice AI platforms, time-series models, flight APIs) and meta-level optimization (prompt engineering skills, best practice guides, agent training frameworks, self-evolving skill systems) — as the community shifts from building agents to making them systematically better, cheaper, and more specialized across every domain from travel planning to financial trading to autonomous companies.
