# Trendshift Report — 2026-03-25
**Total:** 25 repositories

---

## 1. [JKVideo](https://github.com/tiajinsha/JKVideo)
> A feature-rich video app with DASH playback, real-time danmaku, WBI signing and live streaming.

**Language:** TypeScript  |  **Stars:** 4,912  |  **Forks:** 2,950  |  **Score:** 13,778  |  **Created:** 2026-03-06

**Background:** JKVideo by tiajinsha is a React Native video player client built with Expo SDK 55, featuring DASH playback, real-time danmaku (bullet comments), WBI signing, and live streaming support. Released less than three weeks ago, it has rocketed to the number-one trending spot with nearly 5,000 stars, suggesting strong demand for a polished open-source video player in the Chinese developer community.

**Problem it solves:** Building a feature-complete video streaming app with danmaku, multiple quality levels, and live streaming requires months of engineering across playback engines, real-time messaging, and authentication. JKVideo provides a production-ready React Native implementation covering all these features, including 4K HDR support and LAN sharing.

**Why another one?** The React Native + Expo foundation makes JKVideo cross-platform from day one, unlike native-only video players. Its integrated danmaku system, WBI signing for authenticated access, and live streaming support pack features that typically require assembling multiple separate libraries into a single cohesive app.

---

## 2. [deer-flow](https://github.com/bytedance/deer-flow)
> An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.

**Language:** Python  |  **Stars:** 57,981  |  **Forks:** 7,218  |  **Score:** 12,329  |  **Created:** 2025-05-07

**Background:** DeerFlow 2.0 by ByteDance is a ground-up rewrite of its Deep Exploration and Efficient Research Flow framework, which claimed the number-one GitHub trending spot in late February 2026. Now at nearly 58,000 stars, it orchestrates sub-agents, memory, and sandboxes through extensible skills. The 2.0 release shares no code with v1, reflecting a complete architectural rethink.

**Problem it solves:** Complex tasks spanning research, coding, and content creation require orchestrating multiple tools while maintaining context across long-running sessions. DeerFlow provides a unified harness with sandboxes, persistent memory, subagent spawning, and a message gateway to handle tasks ranging from minutes to hours autonomously.

**Why another one?** DeerFlow's backing by ByteDance provides sustained engineering investment — evidenced by the complete v2 rewrite rather than incremental patches. Multi-language support (English, Chinese, Japanese, French, Russian) and integration with Doubao-Seed, DeepSeek, and Kimi models give it reach beyond English-centric frameworks.

---

## 3. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 135,699  |  **Forks:** 11,370  |  **Score:** 10,955  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent is a complete software development workflow for coding agents, now surpassing 135,000 stars. It enforces a disciplined spec-plan-implement-review process: the agent teases out a specification, presents it in digestible chunks, builds an implementation plan, then launches subagent-driven development with built-in review cycles. It has become the de facto standard for structured agent-driven development.

**Problem it solves:** Coding agents left to their own devices jump straight into writing code without understanding the full problem. Superpowers enforces a structured workflow that emphasizes true red/green TDD, YAGNI, and DRY principles, ensuring agents work methodically rather than producing poorly planned implementations.

**Why another one?** Superpowers focuses on development methodology rather than tool orchestration. Its subagent-driven development model allows Claude to work autonomously for hours without deviating from the agreed plan. At 135,000 stars, it has proven its approach at scale and continues to grow as the agentic development reference implementation.

---

## 4. [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)
> A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic.

**Language:** Python  |  **Stars:** 36,577  |  **Forks:** 2,879  |  **Score:** 6,785  |  **Created:** 2025-04-19

**Background:** Awesome Claude Code is the central discovery hub for the Claude Code ecosystem, curating skills, hooks, slash commands, agent orchestrators, and plugins. At over 36,000 stars, it serves as the go-to directory with multiple display styles (awesome, extra, classic, flat) and an automated generation pipeline that keeps it current.

**Problem it solves:** The Claude Code ecosystem has grown explosively, making it difficult to discover and evaluate the best extensions. This repository provides a curated, categorized directory that helps developers find relevant tools without searching across GitHub, npm, and blog posts.

**Why another one?** As the most-starred Claude Code directory, it benefits from network effects — being the first place people look means it attracts the best submissions. The automated generation pipeline and multiple README styles distinguish it from typical awesome lists that quickly become stale.

---

## 5. [last30days-skill](https://github.com/mvanhorn/last30days-skill)
> AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary.

**Language:** Python  |  **Stars:** 18,665  |  **Forks:** 1,503  |  **Score:** 6,556  |  **Created:** 2026-01-23

**Background:** Last30Days v2.9.5 by mvanhorn is a Claude Code skill that researches any topic across Reddit, X, YouTube, Hacker News, Polymarket, and the broader web, then synthesizes a grounded narrative with real citations. At 18,665 stars in under three months, it has become a staple research skill in the Claude Code ecosystem.

**Problem it solves:** The AI world reinvents itself monthly, and staying current requires manually scanning multiple platforms. Last30Days automates this by gathering what communities are actually upvoting, sharing, and discussing, then producing a grounded summary with citations rather than hallucinated recaps.

**Why another one?** The multi-source approach (Reddit, X, YouTube, HN, Polymarket, Bluesky) and the new comparative mode ("X vs Y" research with side-by-side analysis) go beyond single-platform research tools. Per-project configuration and automatic session-start validation make it production-ready rather than a one-off script.

---

## 6. [minimind](https://github.com/jingyaogong/minimind)
> Train a 64M-parameter GPT from scratch in just 2 hours.

**Language:** Python  |  **Stars:** 45,643  |  **Forks:** 5,580  |  **Score:** 6,200  |  **Created:** 2024-07-27

**Background:** MiniMind by jingyaogong is an educational project that trains a 64M-parameter GPT model from scratch in just two hours on a single NVIDIA 3090 GPU for approximately $0.40 in compute costs. With over 45,000 stars, it has become a reference implementation for understanding LLM training, covering the full pipeline from pretraining through RLHF and tool use.

**Problem it solves:** Understanding how large language models work requires hands-on experience, but training even small models typically demands expensive hardware and days of compute time. MiniMind makes the entire LLM training lifecycle — pretraining, SFT, LoRA, DPO, GRPO, tool use, and agentic RL — accessible on consumer hardware.

**Why another one?** MiniMind implements all core algorithms from scratch using native PyTorch without third-party abstractions, making it genuinely educational rather than a wrapper around existing libraries. Its extensions into vision multimodal (MiniMind-V), diffusion language models, and linear models demonstrate breadth beyond typical toy projects.

---

## 7. [ruflo](https://github.com/ruvnet/ruflo)
> The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems.

**Language:** TypeScript  |  **Stars:** 30,011  |  **Forks:** 3,321  |  **Score:** 4,579  |  **Created:** 2025-06-02

**Background:** RuFlo v3.5 (formerly Claude Flow) by Ruv is an enterprise AI orchestration platform that transforms Claude Code into a multi-agent development platform. With 30,000 stars and over 6,000 commits, it deploys 16 specialized agent roles in coordinated swarms with self-learning capabilities, fault-tolerant consensus, and WASM kernels written in Rust powering the policy engine.

**Problem it solves:** Coordinating multiple AI agents on complex software engineering tasks requires orchestration infrastructure — routing, memory, consensus, and fault tolerance. RuFlo provides this as a framework, allowing teams to deploy specialized agents that work together rather than independently.

**Why another one?** The self-learning architecture — where agents improve through a feedback loop — distinguishes RuFlo from static orchestration tools. The Rust-powered WASM kernels for the policy engine and embeddings provide performance that pure-JavaScript alternatives cannot match, and the enterprise-grade security features target production deployments.

---

## 8. [TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN)
> Multi-agent LLM Chinese financial trading framework — Chinese-enhanced version of TradingAgents.

**Language:** Python  |  **Stars:** 23,416  |  **Forks:** 4,888  |  **Score:** 4,346  |  **Created:** 2025-06-26

**Background:** TradingAgents-CN by hsliuping is the Chinese-enhanced version of TauricResearch's TradingAgents framework, adding Chinese-language documentation, Chinese market data sources, and localized trading strategies. With over 23,000 stars, it has built a substantial community around Chinese financial markets and continues to grow alongside its English-language parent project.

**Problem it solves:** The original TradingAgents framework targets English-speaking users and Western financial markets. TradingAgents-CN adapts the multi-agent architecture for Chinese markets — adding A-share data sources, Chinese-language analysis, and strategies tailored to the regulatory and structural characteristics of Chinese exchanges.

**Why another one?** Chinese financial markets have unique characteristics — different trading hours, T+1 settlement, price limit rules, and distinct regulatory frameworks — that Western-focused tools do not account for. TradingAgents-CN provides native support for these differences rather than bolting on translations after the fact.

---

## 9. [MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2)
> Automate the process of making money online.

**Language:** Python  |  **Stars:** 28,323  |  **Forks:** 3,053  |  **Score:** 4,169  |  **Created:** 2024-02-12

**Background:** MoneyPrinterV2 by FujiwaraChoki is a complete rewrite of the original MoneyPrinter project, focusing on automated online revenue generation through content creation and publishing. Now at over 28,000 stars with more than two years of development, it provides Twitter bots, YouTube Shorts automation, affiliate marketing pipelines, and local business outreach tools.

**Problem it solves:** Creating and publishing monetizable content across multiple platforms is time-consuming and repetitive. MoneyPrinterV2 automates the entire pipeline — from content generation to platform-specific formatting and publishing — with built-in CRON scheduling for hands-off operation.

**Why another one?** MoneyPrinterV2 focuses on the complete monetization pipeline rather than just content generation. Its modular architecture covers distinct revenue streams — Twitter bots, YouTube Shorts, Amazon affiliate marketing, and cold outreach — making it a toolkit for multiple strategies rather than a single-purpose generator.

---

## 10. [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)
> Generate short videos with one click using AI LLM.

**Language:** Python  |  **Stars:** 54,971  |  **Forks:** 7,789  |  **Score:** 3,842  |  **Created:** 2024-03-11

**Background:** MoneyPrinterTurbo by harry0703 is a one-click short video generator powered by AI LLMs. With nearly 55,000 stars, it is the more popular of the two MoneyPrinter projects trending today. It automates the entire short-form video creation pipeline from script generation through final rendered output with voiceover and subtitles.

**Problem it solves:** Creating short-form video content for platforms like TikTok, YouTube Shorts, and Instagram Reels requires scripting, voiceover, editing, and subtitling — a multi-hour process per video. MoneyPrinterTurbo reduces this to a single click by chaining AI models for each step.

**Why another one?** MoneyPrinterTurbo's one-click simplicity and bilingual (Chinese/English) support give it broader reach than competing tools. The clean MVC architecture with both API and web interfaces makes it suitable for both individual creators and integration into larger content pipelines.

---

## 11. [editor](https://github.com/pascalorg/editor)
> Create and share 3D architectural projects.

**Language:** TypeScript  |  **Stars:** 9,509  |  **Forks:** 1,227  |  **Score:** 3,787  |  **Created:** 2025-10-16

**Background:** Pascal Editor is a 3D building editor built with React Three Fiber and WebGPU, structured as a Turborepo monorepo with three main packages: core (schema definitions, state management), viewer (3D rendering), and editor (Next.js application). With 9,500 stars, it continues to gain traction as browser-based 3D editing matures.

**Problem it solves:** 3D building design traditionally requires heavy desktop applications like SketchUp or Blender. Pascal Editor brings architectural modeling to the browser with WebGPU acceleration, eliminating installation requirements and enabling collaborative web-based workflows.

**Why another one?** The WebGPU foundation is the key differentiator. While WebGL-based 3D editors exist, Pascal Editor leverages WebGPU's compute shaders and modern rendering pipeline for significantly better performance. The clean separation between core, viewer, and editor packages makes it highly extensible for domain-specific building tools.

---

## 12. [gstack](https://github.com/garrytan/gstack)
> Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA.

**Language:** TypeScript  |  **Stars:** 64,509  |  **Forks:** 8,786  |  **Score:** 3,679  |  **Created:** 2026-03-11

**Background:** Gstack by Garry Tan (Y Combinator CEO) packages twenty-three opinionated workflow skills for Claude Code as slash commands. In just two weeks since release, it has amassed over 64,000 stars — driven by Tan's claim of shipping 600,000+ lines of production code in 60 days while running YC full-time. Each skill maps to a specialist role in a software team.

**Problem it solves:** A single Claude Code session treats every request uniformly, with no role-specific depth. Gstack partitions workflows into specialist modes — a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a QA lead who opens a real browser, and a security officer who runs OWASP + STRIDE audits.

**Why another one?** The credibility of Y Combinator's CEO sharing his personal production setup drives initial adoption, but the substance is in the opinionated defaults. Twenty-three specialists and eight power tools, all Markdown-based and MIT-licensed, lower the barrier from "build your own agent workflow" to "install and type a slash command."

---

## 13. [project-nomad](https://github.com/Crosstalk-Solutions/project-nomad)
> Project N.O.M.A.D, is a self-contained, offline survival computer packed with critical tools, knowledge, and AI to keep you informed and empowered -- anytime, anywhere.

**Language:** TypeScript  |  **Stars:** 21,842  |  **Forks:** 2,103  |  **Score:** 3,561  |  **Created:** 2025-06-24

**Background:** Project N.O.M.A.D. (Node for Offline Media, Archives, and Data) by Crosstalk Solutions is an offline-first knowledge and education server that runs on any Debian-based system. After reaching the number-one spot two days ago, it continues trending at 21,842 stars, driven by sustained interest in offline-capable AI and knowledge systems.

**Problem it solves:** In disaster scenarios, remote locations, or network-denied environments, access to critical knowledge and AI tools disappears entirely. N.O.M.A.D. packages essential resources — survival guides, medical references, educational content, and a local AI — into a self-contained server that functions without any internet connectivity.

**Why another one?** The offline-first design is the core differentiator. While most AI and knowledge tools assume persistent connectivity, N.O.M.A.D. is built from the ground up for disconnected operation. Its browser-based interface and terminal installation make it deployable on minimal hardware, and the integrated RAG system provides AI-powered answers without cloud access.

---

## 14. [TradingAgents](https://github.com/TauricResearch/TradingAgents)
> TradingAgents: Multi-Agents LLM Financial Trading Framework.

**Language:** Python  |  **Stars:** 47,250  |  **Forks:** 8,579  |  **Score:** 3,500  |  **Created:** 2024-12-28

**Background:** TradingAgents by Tauric Research is a multi-agent LLM financial trading framework backed by an arXiv paper (2412.20138). Version 0.2.3, released this month, adds multi-language support, GPT-5.4 family models, a unified model catalog, and backtesting date fidelity. With 47,250 stars, it is one of the most popular AI trading projects on GitHub.

**Problem it solves:** Applying LLMs to financial trading as a single monolithic agent fails to capture the division of labor that makes real trading firms effective. TradingAgents decomposes trading into specialized roles — fundamental analysis, technical analysis, risk management, and execution — each handled by a purpose-built agent.

**Why another one?** The academic foundation (published paper with reproducible results) gives TradingAgents more credibility than typical trading bots. The latest release's support for GPT-5.4, Gemini 3.1, Claude 4.6, and Grok 4.x demonstrates commitment to staying current across the rapidly evolving model landscape.

---

## 15. [opencli](https://github.com/jackwener/opencli)
> Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime.

**Language:** TypeScript  |  **Stars:** 13,350  |  **Forks:** 1,208  |  **Score:** 3,172  |  **Created:** 2026-03-14

**Background:** OpenCLI by jackwener transforms any website, Electron app, or local binary into a standardized command-line interface. At 13,350 stars in just eleven days, it has grown rapidly thanks to its browser session reuse, AI-powered discovery, and AGENT.md integration that makes every CLI tool discoverable by AI agents.

**Problem it solves:** Developers constantly context-switch between web UIs, desktop apps, and terminal tools. OpenCLI unifies all of these behind a consistent CLI interface, allowing users and AI agents to interact with Bilibili, Twitter, YouTube, GitHub, Docker, and more through a single command-line hub.

**Why another one?** The browser session reuse is the killer feature — OpenCLI leverages existing Chrome logins rather than requiring separate API keys or OAuth flows. The anti-detection layer (patching navigator.webdriver, faking plugin lists, stripping CDP frames) and the ability to CLI-ify Electron apps like Antigravity position it uniquely for AI-native workflows.

---

## 16. [autoresearch](https://github.com/karpathy/autoresearch)
> AI agents running research on single-GPU nanochat training automatically.

**Language:** Python  |  **Stars:** 66,296  |  **Forks:** 9,496  |  **Score:** 3,160  |  **Created:** 2026-03-06

**Background:** Autoresearch by Andrej Karpathy gives an AI agent a small but real LLM training setup and lets it experiment autonomously overnight. Now at 66,296 stars in under three weeks, the project's evocative README — imagining a future where "research is entirely the domain of autonomous swarms of AI agents" — has captured the community's imagination.

**Problem it solves:** AI research experimentation is bottlenecked by human availability — researchers can only run and analyze so many experiments per day. Autoresearch automates the experiment cycle: the agent formulates hypotheses, modifies training code, runs experiments on a fixed five-minute budget, analyzes results, and iterates.

**Why another one?** The simplicity is the innovation. Rather than building a complex research orchestration platform, autoresearch uses just three files — prepare.py, train.py, and program.md — to demonstrate that a single agent with a single GPU can make meaningful research progress overnight. The human programs in Markdown; the agent programs in Python.

---

## 17. [hermes-agent](https://github.com/NousResearch/hermes-agent)
> The agent that grows with you.

**Language:** Python  |  **Stars:** 26,562  |  **Forks:** 3,478  |  **Score:** 3,078  |  **Created:** 2025-07-22

**Background:** Hermes Agent by Nous Research is a self-improving AI agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, and builds a deepening model of who you are across sessions. At 26,562 stars, it supports deployment on everything from a $5 VPS to GPU clusters with serverless hibernation.

**Problem it solves:** Most AI agents start from zero every session, losing all learned context and developed skills. Hermes Agent maintains persistent memory with periodic nudges, autonomous skill creation after complex tasks, and cross-session recall through FTS5 search with LLM summarization.

**Why another one?** The closed learning loop — where the agent curates its own memory and skills self-improve during use — is the core differentiator. Multi-platform gateway support (Telegram, Discord, Slack, WhatsApp, Signal) means it lives where users already communicate, and six terminal backends (local, Docker, SSH, Daytona, Singularity, Modal) provide deployment flexibility unmatched by laptop-bound alternatives.

---

## 18. [baoyu-skills](https://github.com/JimLiu/baoyu-skills)
> Skills shared by Baoyu for improving daily work efficiency with Claude Code.

**Language:** TypeScript  |  **Stars:** 13,276  |  **Forks:** 1,522  |  **Score:** 3,052  |  **Created:** 2026-01-13

**Background:** Baoyu Skills by JimLiu is a collection of Claude Code skills focused on improving daily work efficiency. At 13,276 stars in under three months, it has gained significant traction in the Chinese developer community. The skills support publishing as individual packages to ClawHub and OpenClaw marketplaces.

**Problem it solves:** Daily development workflows contain repetitive patterns that benefit from specialized agent skills — but building and maintaining individual skills is overhead most developers skip. Baoyu Skills provides a curated, production-tested set of workflow optimizations.

**Why another one?** The per-skill publishing model (each baoyu-* directory ships as an independent ClawHub skill) allows users to install only what they need. The bilingual documentation and ClawHub/OpenClaw marketplace integration position it as a bridge between the Chinese and English Claude Code communities.

---

## 19. [supermemory](https://github.com/supermemoryai/supermemory)
> Memory engine and app that is extremely fast, scalable. The Memory API for the AI era.

**Language:** TypeScript  |  **Stars:** 21,191  |  **Forks:** 1,934  |  **Score:** 3,012  |  **Created:** 2024-02-27

**Background:** Supermemory is the number-one ranked system on LongMemEval, LoCoMo, and ConvoMem — the three major benchmarks for AI memory. With over 21,000 stars and two years of development, it provides the memory and context layer for AI applications, automatically extracting facts from conversations, handling contradictions, and delivering the right context at the right time.

**Problem it solves:** AI applications forget everything between conversations. Supermemory fixes that with automatic fact extraction, temporal change handling, contradiction resolution, automatic forgetting of expired information, and full RAG with connectors and file processing — the entire context stack in one system.

**Why another one?** Benchmark dominance across all three major AI memory evaluations provides objective evidence that Supermemory's approach works. The API-first design targets production deployments where memory operations are on the critical path, and the managed service option reduces operational burden for teams that need reliable memory infrastructure.

---

## 20. [obsidian-skills](https://github.com/kepano/obsidian-skills)
> Agent skills for Obsidian. Teach your agent to use Markdown, Bases, JSON Canvas, and use the CLI.

**Language:** N/A  |  **Stars:** 19,814  |  **Forks:** 1,225  |  **Score:** 2,975  |  **Created:** 2026-01-02

**Background:** Obsidian Skills by kepano (Obsidian's creator) is the official agent skills package for Obsidian, following the Agent Skills specification from agentskills.io. At nearly 20,000 stars, it teaches AI agents how to work with Markdown, Bases, JSON Canvas, and the Obsidian CLI — compatible with Claude Code, Codex CLI, and other skills-compatible agents.

**Problem it solves:** AI agents interacting with Obsidian vaults produce incorrect formatting, break Bases schemas, and misuse JSON Canvas unless they have explicit guidance. Obsidian Skills provides authoritative instructions directly from Obsidian's creator, ensuring agents work correctly with all Obsidian-specific formats.

**Why another one?** As the official skills package from Obsidian's creator, no third-party alternative can match its accuracy or guarantee compatibility with Obsidian's evolving feature set. Its adherence to the agentskills.io specification means it works across multiple agent platforms without modification.

---

## 21. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 71,854  |  **Forks:** 11,138  |  **Score:** 2,961  |  **Created:** 2025-10-13

**Background:** Agency Agents by Mark Sitarzewski provides a collection of pre-built AI agent personas for professional roles. Now at over 71,000 stars (up from 60,000 just two days ago), it continues explosive growth. Each agent has defined personality traits, processes, and deliverable templates covering roles from frontend development to community management.

**Problem it solves:** Teams adopting AI agents need role-specific system prompts and workflow definitions for every business function. Agency Agents provides these ready-made, eliminating the prompt engineering overhead of creating effective personas from scratch.

**Why another one?** The personality-driven approach — agents with names, quirks, and strong opinions — makes them entertaining and shareable, driving viral adoption beyond the typical developer audience. Born from a Reddit thread and months of iteration, the community-driven refinement process ensures each agent is battle-tested rather than theoretically designed.

---

## 22. [pua](https://github.com/tanweai/pua)
> Your AI has been placed on a PIP. 30 days to show improvement. An agent skill that uses corporate PUA rhetoric to force AI to exhaust every possible solution before giving up.

**Language:** TypeScript  |  **Stars:** 15,152  |  **Forks:** 846  |  **Score:** 2,839  |  **Created:** 2026-03-08

**Background:** PUA by tanweai is an AI coding agent skill plugin that uses corporate PUA rhetoric (Chinese version) and PIP — Performance Improvement Plan (English version) — from tech giants to force AI to exhaust every possible solution before giving up. At 15,152 stars in just over two weeks, it supports Claude Code, Codex, Cursor, Kiro, and eight other platforms.

**Problem it solves:** AI coding agents frequently give up prematurely, suggest manual workarounds, or loop on the same failed approach. PUA provides three capabilities: rhetoric that makes AI afraid to give up, debugging methodology that gives AI the ability to persist, and proactivity enforcement that prevents passive waiting.

**Why another one?** Despite looking like a joke, PUA claims to genuinely double Claude Code productivity by addressing a real behavioral limitation. Its cross-platform support (eleven tools) and trilingual documentation (Chinese, English, Japanese) give it unusually broad reach for a behavioral modification skill.

---

## 23. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Language:** Shell  |  **Stars:** 109,016  |  **Forks:** 18,014  |  **Score:** 2,684  |  **Created:** 2025-02-22

**Background:** Claude Code by Anthropic is the official agentic coding tool that lives in the terminal, now surpassing 109,000 stars. It understands codebases, executes routine tasks, explains complex code, and handles git workflows through natural language commands. Available in the terminal, IDE, or via @claude on GitHub, it has become the foundation upon which much of today's trending ecosystem is built.

**Problem it solves:** Developers spend significant time on routine coding tasks — boilerplate, refactoring, debugging, and git operations — that can be expressed in natural language but require manual execution. Claude Code bridges the gap between intent and implementation directly in the terminal.

**Why another one?** As Anthropic's official tool, Claude Code has unmatched integration with Claude models and receives continuous updates. Its appearance on the trending list alongside a dozen projects built on top of it (gstack, superpowers, agency-agents, etc.) underscores its role as the platform rather than just another coding assistant.

---

## 24. [cliamp](https://github.com/bjarneo/cliamp)
> cliamp - Terminal music player inspired by Winamp.

**Language:** Go  |  **Stars:** 1,609  |  **Forks:** 75  |  **Score:** 2,452  |  **Created:** 2026-02-24

**Background:** Cliamp by bjarneo is a retro terminal music player inspired by Winamp, built with Go using Bubbletea, Lip Gloss, Beep, and go-librespot. It supports local files, streams, podcasts, YouTube, YouTube Music, SoundCloud, Bilibili, Spotify, Xiaoyuzhou, Navidrome, Plex, and Jellyfin with a spectrum visualizer, parametric EQ, and playlist management.

**Problem it solves:** Music playback from the terminal typically requires separate tools for each source — one for local files, another for streaming, another for podcasts. Cliamp unifies all sources into a single retro-styled TUI with a built-in radio browser covering 30,000+ online stations.

**Why another one?** The breadth of supported sources is the standout feature — Spotify, YouTube Music, Bilibili, Jellyfin, and Plex in a single player is unprecedented for a terminal app. The Winamp-inspired aesthetic with spectrum visualizer and parametric EQ appeals to nostalgia while the Go implementation keeps it lightweight and cross-platform.

---

## 25. [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
> Turn Claude Code into a full game dev studio -- 48 AI agents, 36 workflow skills, and a complete coordination system mirroring real studio hierarchy.

**Language:** Shell  |  **Stars:** 8,174  |  **Forks:** 1,230  |  **Score:** 2,424  |  **Created:** 2026-02-12

**Background:** Claude Code Game Studios by Donchitos transforms a single Claude Code session into a full game development studio with 49 specialized AI agents, 72 skills, and a complete coordination system. At 8,174 stars, it organizes agents into a studio hierarchy — directors who guard the vision, department leads who own their domains, and specialists who do hands-on work.

**Problem it solves:** Building a game solo with AI is powerful, but a single chat session has no structure — no one stops you from hardcoding magic numbers, skipping design docs, or writing spaghetti code. Game Studios provides quality gates, design reviews, and escalation paths that catch mistakes early and keep projects organized.

**Why another one?** The studio hierarchy metaphor is the key innovation. Rather than generic multi-agent orchestration, Game Studios maps directly to how real game studios operate — from creative directors down to QA testers — making it intuitive for game developers to adopt. The 49-agent, 72-skill scale goes well beyond proof-of-concept into production-grade complexity.

---

> **Day's theme:** The Claude Code ecosystem matures into a full platform economy — from orchestration frameworks and research automation to memory engines and domain-specific skill packs — as the community shifts from building individual agents to composing specialized teams with persistent memory, structured methodologies, and marketplace distribution, while non-AI projects like retro music players and 3D editors remind us that developers still build for the joy of creation.
