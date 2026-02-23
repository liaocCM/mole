# Trendshift Report — 2026-02-16
**Total:** 25 repositories

---

## 1. [picoclaw](https://github.com/sipeed/picoclaw)
> Tiny, Fast, and Deployable anywhere — automate the mundane, unleash your creativity

**Language:** Go  |  **Stars:** 17,835  |  **Forks:** 2,110  |  **Score:** 9,288  |  **Created:** 2026-02-04

**Background:** Picoclaw is a Go-based automation and deployment platform from Sipeed, designed to be minimal in footprint while capable of running across diverse hardware targets. It launched in early February 2026 and accumulated nearly 18,000 stars in under two weeks, suggesting strong word-of-mouth within the embedded and edge computing communities. The project emphasizes portability, targeting environments ranging from developer laptops to resource-constrained microcontrollers.

**Problem it solves:** Deploying automation workflows to heterogeneous hardware — including low-power boards and embedded systems — typically requires environment-specific toolchains and heavy runtime dependencies. Picoclaw provides a single binary that can be dropped onto almost any target and begin executing workflows immediately, eliminating the bootstrapping friction that plagues conventional CI/CD tools on edge hardware.

**Why another one?** Most automation platforms are designed for cloud or server-class hardware and carry runtimes that are too large for constrained targets. Picoclaw differentiates by treating tiny devices as first-class deployment targets rather than afterthoughts. Its rapid star growth suggests it is filling a genuine gap for teams building on Sipeed's embedded hardware ecosystem.

---

## 2. [awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources)
> Learn System Design concepts and prepare for interviews using free resources.

**Language:** Java  |  **Stars:** 33,577  |  **Forks:** 7,447  |  **Score:** 4,667  |  **Created:** 2023-10-25

**Background:** Maintained by Ashish Pratap Singh, this repository is a curated collection of free learning materials covering distributed systems fundamentals, common architecture patterns, and practical interview preparation guides. It organizes resources by topic — from CAP theorem and consensus protocols to real-world case studies of systems at companies like Netflix and Uber. The repository has grown steadily since October 2023 to over 33,000 stars.

**Problem it solves:** System design interview preparation is fragmented across paid courses, scattered blog posts, and YouTube videos of varying quality. This repository consolidates high-quality free resources into a single structured reference, reducing the time candidates spend hunting for reliable material. It also serves as a self-study curriculum for engineers who want to deepen their distributed systems knowledge outside of an interview context.

**Why another one?** It keeps trending because system design interviews remain a high-stakes bottleneck in engineering hiring, and the repository continues to receive active updates with new case studies and resource links. Its Java code examples alongside the conceptual writeups give it broader utility than a purely textual resource list.

---

## 3. [zvec](https://github.com/alibaba/zvec)
> A lightweight, lightning-fast, in-process vector database

**Language:** C++  |  **Stars:** 5,951  |  **Forks:** 330  |  **Score:** 3,941  |  **Created:** 2025-12-05

**Background:** Zvec is an in-process vector database developed by Alibaba, written in C++ for minimal overhead and maximum throughput. Unlike standalone vector database servers, it embeds directly into the calling application's process, eliminating the network round-trip cost for every similarity search. It was released in December 2025 and has grown to nearly 6,000 stars in roughly ten weeks.

**Problem it solves:** Running a vector database as a separate service introduces latency, operational complexity, and infrastructure cost that is difficult to justify for applications with moderate embedding workloads. Zvec brings vector search in-process alongside the application, allowing similarity queries to execute at memory speeds without inter-process communication or serialization overhead.

**Why another one?** Most widely adopted vector databases — Pinecone, Weaviate, Qdrant — are designed as standalone services. Zvec occupies the in-process niche, comparable to SQLite's position relative to full database servers. Alibaba's backing and C++ implementation give it credibility and performance benchmarks that attract teams frustrated by the operational burden of running a separate vector service.

---

## 4. [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)
> The Ultimate Collection of 800+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

**Language:** Python  |  **Stars:** 13,791  |  **Forks:** 2,590  |  **Score:** 3,616  |  **Created:** 2026-01-14

**Background:** Antigravity Awesome Skills is a community-curated registry of over 800 reusable agentic skills compatible with Claude Code, Cursor, and the Antigravity agent framework. It bundles official skills from Anthropic and Vercel alongside community contributions, and organizes them by functional category — code review, testing, deployment, documentation, and more. The repository launched in January 2026 and has rapidly become a go-to resource for teams building agentic workflows.

**Problem it solves:** Building effective agentic workflows from scratch requires significant prompt engineering and tool-calling expertise. This collection provides battle-tested, ready-to-install skills that encode best practices for common development tasks, allowing teams to adopt agentic workflows without investing weeks in custom skill development.

**Why another one?** The breadth of 800+ skills and multi-agent compatibility — covering Claude Code, Antigravity, and Cursor — gives it a wider appeal than single-platform skill collections. Its inclusion of official Anthropic and Vercel skills signals institutional backing that many community repositories lack, contributing to its rapid growth and recurring trend appearances.

---

## 5. [ProxyBridge](https://github.com/InterceptSuite/ProxyBridge)
> Proxifier Alternative to redirect any Windows/MacOS/Linux TCP and UDP traffic to HTTP/Socks5 proxy

**Language:** C  |  **Stars:** 2,300  |  **Forks:** 153  |  **Score:** 3,406  |  **Created:** 2025-10-13

**Background:** ProxyBridge is a cross-platform transparent proxy redirect tool written in C, created by InterceptSuite as an open-source alternative to the commercial Proxifier application. It intercepts TCP and UDP traffic at the system level and routes it through a user-specified HTTP or Socks5 proxy, without requiring applications to have built-in proxy support. It targets Windows, macOS, and Linux with a single consistent interface.

**Problem it solves:** Many applications do not respect system proxy settings or lack configurable proxy options, making it difficult to route their traffic through corporate proxies, VPNs, or interception tools during security testing. ProxyBridge solves this by redirecting traffic transparently at the OS level, regardless of whether the application cooperates.

**Why another one?** Proxifier is closed-source, Windows-primary, and subscription-licensed. ProxyBridge offers full cross-platform support, open-source transparency, and zero licensing cost — all critical properties for security researchers and developers who need to inspect or redirect traffic across multiple operating systems. The C implementation keeps the binary small and dependency-free.

---

## 6. [rowboat](https://github.com/rowboatlabs/rowboat)
> Open-source AI coworker, with memory

**Language:** TypeScript  |  **Stars:** 8,002  |  **Forks:** 685  |  **Score:** 3,223  |  **Created:** 2025-01-13

**Background:** Rowboat is an open-source AI coworker platform built by Rowboat Labs, featuring persistent memory that allows the agent to accumulate context across sessions. It is designed to act as a team-embedded assistant rather than a stateless chat interface, maintaining awareness of ongoing projects, decisions, and team preferences over time. The project launched in January 2025 and has grown to over 8,000 stars.

**Problem it solves:** Most AI assistants reset context between sessions, requiring users to re-explain their project state and preferences repeatedly. Rowboat's persistent memory layer allows it to build a working model of the team's projects and conventions over time, making it progressively more useful the longer it is deployed.

**Why another one?** Rowboat positions itself as an open-source alternative to commercial AI coworker products, giving teams full control over where memory is stored and how the agent is configured. The combination of persistent memory with an open, self-hostable architecture is its primary differentiator from both stateless open-source assistants and proprietary coworker platforms.

---

## 7. [openclaw](https://github.com/openclaw/openclaw)
> Your own personal AI assistant. Any OS. Any Platform. The lobster way.

**Language:** TypeScript  |  **Stars:** 215,287  |  **Forks:** 40,386  |  **Score:** 2,859  |  **Created:** 2025-11-24

**Background:** OpenClaw is a personal AI assistant platform that runs on any operating system and claims compatibility with any underlying AI model or API. It is built in TypeScript and has accumulated over 215,000 stars since its November 2025 launch, making it one of the fastest-growing open-source repositories in the personal assistant category. Its branding around "the lobster way" reflects a community identity that has developed rapidly around the project.

**Problem it solves:** Proprietary AI assistants are locked to specific platforms, app stores, or subscription services, limiting user control over data and model choice. OpenClaw provides a self-hosted alternative that works on any OS, connects to any AI provider, and keeps all data under the user's control — addressing privacy and portability concerns simultaneously.

**Why another one?** OpenClaw keeps trending because its star count places it in a category by itself among personal assistant platforms — its 215,000+ stars dwarf most comparable projects. Its cross-platform universality and active community ecosystem of skills and plugins drive continued discovery and repeat appearances on trending lists.

---

## 8. [heretic](https://github.com/p-e-w/heretic)
> Fully automatic censorship removal for language models

**Language:** Python  |  **Stars:** 8,887  |  **Forks:** 884  |  **Score:** 2,804  |  **Created:** 2025-09-21

**Background:** Heretic is a Python tool authored by p-e-w that automates the removal of content filters and refusal behaviors from language models. It operates on locally run models rather than API-accessed services, using techniques to modify model behavior at inference time. Since its September 2025 release it has attracted nearly 9,000 stars and significant community discussion around the ethics and legality of model censorship removal.

**Problem it solves:** Language models fine-tuned for public deployment often refuse legitimate requests from researchers, security professionals, and developers working on sensitive but lawful domains. Heretic provides a local, automated method to remove these restrictions for users running models on their own hardware, without requiring manual fine-tuning or dataset curation.

**Why another one?** The project occupies a deliberately controversial niche — automated, no-expertise-required censorship removal — that distinguishes it from manual jailbreaking or fine-tuning approaches. Its automation and local-first design mean users do not need to send data to a third party. The ongoing public debate about AI content moderation keeps it in the spotlight.

---

## 9. [worldmonitor](https://github.com/koala73/worldmonitor)
> Real-time global intelligence dashboard — AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface

**Language:** TypeScript  |  **Stars:** 8,834  |  **Forks:** 1,068  |  **Score:** 2,225  |  **Created:** 2026-01-08

**Background:** WorldMonitor is a TypeScript-based real-time dashboard that aggregates global news, geopolitical events, and infrastructure status into a unified situational awareness interface. It uses AI to classify and prioritize incoming signals, surfacing the most actionable intelligence for users monitoring global developments. Launched in January 2026, it has grown to nearly 9,000 stars in under six weeks.

**Problem it solves:** Analysts and researchers monitoring global events must manually aggregate information from dozens of news sources, RSS feeds, and government advisories, then filter noise from signal. WorldMonitor automates the aggregation and AI-powered triage step, presenting a consolidated view of geopolitical and infrastructure events ranked by significance.

**Why another one?** Existing commercial intelligence dashboards are expensive and designed for enterprise procurement cycles. WorldMonitor is self-hostable and open-source, making real-time global situational awareness accessible to independent researchers, journalists, and security teams who cannot afford commercial platforms.

---

## 10. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 56,468  |  **Forks:** 4,282  |  **Score:** 2,196  |  **Created:** 2025-10-09

**Background:** Superpowers is a composable skills framework and structured software development methodology created by Jesse Vincent (obra). It installs into coding agents such as Claude Code, Cursor, Codex, and OpenCode via their plugin systems, enforcing a multi-stage workflow: brainstorm and refine a spec, produce a detailed implementation plan, then execute through subagent-driven development with two-stage code review. The project has accumulated over 56,000 stars since October 2025.

**Problem it solves:** Coding agents left to default settings tend to skip planning, ignore test-driven development, and drift from the original intent mid-session. Superpowers installs guard rails — mandatory spec approval, red-green-refactor TDD enforcement, and plan checkpoints — so an agent can work autonomously for extended periods without derailing from what was agreed upon.

**Why another one?** Rather than being a new coding agent, Superpowers is a methodology layer that works across multiple agents via their plugin systems. The portability — same skills install in Claude Code, Cursor, Codex, and OpenCode — and the emphasis on subagent delegation rather than a single long-running context are the primary differentiators. It continues trending as new agentic coding users discover cross-agent compatibility.

---

## 11. [awesome-software-design](https://github.com/QDenka/awesome-software-design)
> Organizing and structuring software through patterns, decisions, and verified design rules

**Language:** N/A  |  **Stars:** 737  |  **Forks:** 48  |  **Score:** 2,154  |  **Created:** 2026-02-11

**Background:** Awesome Software Design is a curated list repository by QDenka focused on software architecture patterns, architectural decision records, and verified design principles. It launched on February 11, 2026 — just five days before this report — and already shows enough traffic to appear in trending rankings. The repository organizes its content around structure and decision-making frameworks rather than specific technologies.

**Problem it solves:** Software design knowledge is scattered across books, conference talks, and blog posts with inconsistent quality. This repository attempts to consolidate authoritative references on patterns and design decisions into a single structured list, giving engineers a starting point for learning or revisiting architectural concepts without wading through low-quality content.

**Why another one?** Its fresh launch date means it is still accumulating early adopter momentum. The focus on decision records and verified design rules — rather than just listing pattern names — gives it a more practical orientation than older awesome-lists in the architecture space, which may explain its early traction.

---

## 12. [seerr](https://github.com/seerr-team/seerr)
> Open-source media request and discovery manager for Jellyfin, Plex, and Emby.

**Language:** TypeScript  |  **Stars:** 9,534  |  **Forks:** 624  |  **Score:** 2,120  |  **Created:** 2022-03-09

**Background:** Seerr is a self-hosted media request and discovery management tool that integrates with Jellyfin, Plex, and Emby home media servers. It provides a Netflix-style discovery interface for browsing and requesting new content, backed by automated download workflows through Sonarr and Radarr. The project was created in March 2022 and has grown to over 9,500 stars through the home media server community.

**Problem it solves:** Home media server operators typically need to manually field content requests from family members and friends, then queue downloads themselves. Seerr gives non-technical users a polished request interface while automating the fulfillment pipeline — a user requests a title, and Seerr passes it to the appropriate download manager without operator intervention.

**Why another one?** Seerr gained traction by supporting Jellyfin — a fully open-source media server — in addition to Plex and Emby, giving it a broader audience than Jellyseerr (Jellyfin-only) or Overseerr (Plex-only). Its unified multi-server support is the primary differentiator that keeps it visible across the home server community.

---

## 13. [wifi-densepose](https://github.com/ruvnet/wifi-densepose)
> Production-ready implementation of InvisPose - a revolutionary WiFi-based dense human pose estimation system that enables real-time full-body tracking through walls using commodity mesh routers

**Language:** Python  |  **Stars:** 7,201  |  **Forks:** 609  |  **Score:** 1,931  |  **Created:** 2025-06-07

**Background:** WiFi-DensePose is a Python implementation of InvisPose, a system for estimating dense human body pose using WiFi signal perturbations rather than cameras. It processes channel state information (CSI) from commodity mesh routers to track full-body movement through walls and in low-light environments. The project is described as production-ready and ships with preprocessing, inference, and visualization pipelines.

**Problem it solves:** Camera-based human pose estimation requires line of sight, adequate lighting, and raises significant privacy concerns. WiFi-based tracking works through walls, in darkness, and without any visible sensor — enabling applications in fall detection, smart home automation, and security monitoring where camera placement is impractical or unacceptable.

**Why another one?** Research implementations of WiFi pose estimation have historically been inaccessible — requiring custom hardware or proprietary CSI extraction tools. This project targets commodity mesh routers and emphasizes production readiness, making the technology approachable for developers and researchers without specialized RF hardware backgrounds.

---

## 14. [gogcli](https://github.com/steipete/gogcli)
> Google Suite CLI: Gmail, GCal, GDrive, GContacts.

**Language:** Go  |  **Stars:** 4,410  |  **Forks:** 344  |  **Score:** 1,926  |  **Created:** 2025-12-12

**Background:** GoGCLI is a command-line interface for the Google Workspace suite — Gmail, Google Calendar, Google Drive, and Google Contacts — written in Go by Peter Steinberger (steipete). It provides terminal-first access to Google services for developers and power users who prefer keyboard-driven workflows or need to script interactions with their Google accounts. The project launched in December 2025 and has reached over 4,400 stars.

**Problem it solves:** Google's web applications require a browser and offer no native scripting interface, making automation of common tasks — archiving emails, creating calendar events in bulk, querying contacts — unnecessarily difficult. GoGCLI exposes these services via a consistent CLI, enabling shell scripting, cron-based automation, and integration with other terminal tools.

**Why another one?** Existing Google API clients are language-specific SDKs that require writing code rather than issuing commands. GoGCLI fills the direct CLI gap with a single compiled binary that covers the four most-used Workspace services, making it immediately useful without any boilerplate.

---

## 15. [agent-zero](https://github.com/agent0ai/agent-zero)
> Agent Zero AI framework

**Language:** Python  |  **Stars:** 14,953  |  **Forks:** 3,105  |  **Score:** 1,892  |  **Created:** 2024-06-10

**Background:** Agent Zero is a Python-based AI agent framework by agent0ai that provides a general-purpose scaffolding for building autonomous agents capable of using tools, spawning sub-agents, and maintaining memory across tasks. Launched in June 2024, it has grown to nearly 15,000 stars and nearly 3,100 forks, reflecting heavy community use and customization. It supports multiple underlying models and exposes a flexible tool-use and communication layer for agent orchestration.

**Problem it solves:** Building capable AI agents from scratch requires implementing tool execution, memory management, sub-agent delegation, and error recovery from the ground up. Agent Zero provides these primitives as a composable framework, allowing developers to focus on defining what their agent should do rather than how it should manage its own execution.

**Why another one?** Agent Zero distinguishes itself by its emphasis on transparency and hackability — the framework is intentionally minimal and readable, making it easier to understand and modify than heavier alternatives like AutoGen or CrewAI. Its recurring presence on trending lists reflects continued community interest in lightweight, extensible agent frameworks.

---

## 16. [hummingbot](https://github.com/hummingbot/hummingbot)
> Open source software that helps you create and deploy high-frequency crypto trading bots

**Language:** Python  |  **Stars:** 17,391  |  **Forks:** 4,464  |  **Score:** 1,874  |  **Created:** 2019-04-02

**Background:** Hummingbot is a mature open-source framework for building and deploying high-frequency cryptocurrency trading bots, originally released in April 2019. It supports market-making, arbitrage, and directional strategies across dozens of centralized and decentralized exchanges through a unified connector interface. The project has over 17,000 stars, nearly 4,500 forks, and a long track record of production use by both individual traders and market-making firms.

**Problem it solves:** Building a high-frequency trading bot that connects reliably to multiple exchanges, handles order lifecycle management, and executes strategies with low latency requires significant engineering effort. Hummingbot abstracts the exchange connectivity and order management layers, allowing traders to implement and backtest strategies without rebuilding infrastructure from scratch for each exchange.

**Why another one?** Hummingbot continues to trend because it remains one of the few open-source HFT frameworks with broad exchange coverage and an active governance community. New exchange listings, strategy additions, and periodic market volatility that drives trader interest keep it visible on trending lists years after its initial release.

---

## 17. [moonshine](https://github.com/moonshine-ai/moonshine)
> Fast and accurate automatic speech recognition (ASR) for edge devices

**Language:** C  |  **Stars:** 4,265  |  **Forks:** 212  |  **Score:** 1,527  |  **Created:** 2024-10-04

**Background:** Moonshine is a C-implemented automatic speech recognition engine from Moonshine AI, optimized specifically for edge devices with constrained compute budgets. It is designed to run on hardware such as Raspberry Pi, microcontrollers, and embedded Linux boards while delivering accuracy competitive with much heavier models. The project launched in October 2024 and has grown to over 4,200 stars.

**Problem it solves:** Cloud ASR services introduce latency, require network connectivity, and raise privacy concerns by transmitting audio off-device. Running models like Whisper on edge hardware is feasible but slow without careful optimization. Moonshine delivers fast, accurate transcription locally on devices where running a full neural network is otherwise impractical.

**Why another one?** Moonshine's C implementation — rather than Python with native extensions — means it can be compiled and deployed on targets that lack a Python runtime. This makes it genuinely usable on bare-metal embedded systems where competing edge ASR projects cannot run at all.

---

## 18. [tambo](https://github.com/tambo-ai/tambo)
> Generative UI SDK for React

**Language:** TypeScript  |  **Stars:** 10,829  |  **Forks:** 525  |  **Score:** 1,517  |  **Created:** 2024-06-15

**Background:** Tambo is a TypeScript SDK by tambo-ai that enables generative UI patterns within React applications, allowing AI models to dynamically compose and render UI components based on natural language or structured model outputs. It launched in June 2024 and has grown to over 10,000 stars by providing a practical bridge between language model outputs and React component trees.

**Problem it solves:** Displaying AI-generated content in React applications typically requires manually parsing model output and mapping it to components — a fragile and bespoke process. Tambo provides a structured SDK that handles the component selection and rendering logic, allowing developers to declare what components are available and let the model decide how to compose them based on context.

**Why another one?** Generative UI is an emerging pattern without a dominant open-source solution. Tambo targets React specifically — the most widely used UI framework — and provides a production-oriented SDK rather than a research prototype, which gives it practical appeal for product teams wanting to ship AI-driven interfaces without building the integration layer themselves.

---

## 19. [get-shit-done](https://github.com/gsd-build/get-shit-done)
> A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code and OpenCode.

**Language:** JavaScript  |  **Stars:** 17,523  |  **Forks:** 1,588  |  **Score:** 1,432  |  **Created:** 2025-12-14

**Background:** Get-Shit-Done (GSD) is a JavaScript-based meta-prompting and context engineering system for Claude Code and OpenCode, built around spec-driven development principles. It provides a structured workflow where developers write specs first, then use GSD's prompt templates and context management to guide AI coding agents through implementation. The project launched in December 2025 and rapidly accumulated over 17,000 stars.

**Problem it solves:** AI coding agents with no structured input tend to interpret requirements loosely and produce implementations that drift from the original intent. GSD enforces a spec-first workflow with carefully engineered context and meta-prompts that constrain the agent's behavior, increasing the reliability of outputs for complex multi-step development tasks.

**Why another one?** GSD's focus on context engineering — the craft of structuring what information the model sees and when — distinguishes it from skill frameworks that focus on tool-calling. Its lightweight JavaScript implementation makes it easy to drop into existing Claude Code or OpenCode setups without a heavy dependency footprint.

---

## 20. [fluxer](https://github.com/fluxerapp/fluxer)
> A free and open source instant messaging and VoIP platform built for friends, groups, and communities.

**Language:** TypeScript  |  **Stars:** 4,321  |  **Forks:** 172  |  **Score:** 1,416  |  **Created:** 2026-01-01

**Background:** Fluxer is an open-source instant messaging and VoIP platform built in TypeScript, targeting friend groups and online communities as its primary audience. It launched on January 1, 2026 and has grown to over 4,300 stars in its first six weeks. The platform is positioned as a free, self-hostable alternative to proprietary communication platforms, offering text messaging, voice, and community organization features.

**Problem it solves:** Popular communication platforms like Discord are closed-source, hosted entirely by a single company, and subject to policy changes that can affect entire communities. Fluxer provides a self-hostable alternative, giving community operators control over their infrastructure, data retention policies, and moderation tooling without dependence on a third-party platform.

**Why another one?** The demand for open-source Discord alternatives is ongoing and has produced multiple projects, but few achieve the full feature parity of text, voice, and community management in a single self-hostable package. Fluxer's TypeScript stack makes it approachable for contributors familiar with modern web development tooling.

---

## 21. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> The awesome collection of OpenClaw Skills. Formerly known as Moltbot, originally Clawdbot.

**Language:** N/A  |  **Stars:** 17,555  |  **Forks:** 1,799  |  **Score:** 1,392  |  **Created:** 2026-01-25

**Background:** Awesome OpenClaw Skills is a curated collection of community-built skills for the OpenClaw AI assistant platform, maintained by VoltAgent. The project has undergone two rebrands — originally Clawdbot, then Moltbot — before settling on its current name to align with the OpenClaw ecosystem. It launched in late January 2026 and has accumulated over 17,500 stars, reflecting the rapid growth of the OpenClaw community.

**Problem it solves:** OpenClaw is a powerful personal assistant platform, but building custom skills requires knowledge of its plugin API and prompt engineering conventions. This collection provides ready-made, community-tested skills that users can install directly, lowering the barrier to extending OpenClaw with new capabilities without writing skills from scratch.

**Why another one?** The project's lineage — Clawdbot to Moltbot to its current form — reflects its evolution alongside the OpenClaw platform itself. As OpenClaw has grown to become one of the most-starred personal assistant platforms, the demand for a canonical skills repository has grown with it, keeping this collection prominently visible in trending lists.

---

## 22. [gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager)
> An all-in-one enhancement suite for Google Gemini & AI Studio

**Language:** TypeScript  |  **Stars:** 7,252  |  **Forks:** 230  |  **Score:** 1,275  |  **Created:** 2025-10-04

**Background:** Gemini Voyager is a TypeScript browser extension and enhancement suite created by Nagi-ovo that augments Google Gemini and AI Studio with additional features not provided natively by Google. It launched in October 2025 and has grown to over 7,200 stars by addressing quality-of-life gaps in the official Gemini interface. The extension targets power users who rely on Gemini or AI Studio for daily work.

**Problem it solves:** Google's official Gemini and AI Studio interfaces lack productivity features that regular users expect — conversation management, export options, keyboard shortcuts, and customizable UI elements. Gemini Voyager layers these enhancements on top of the existing interface without requiring API key changes or alternative frontends.

**Why another one?** Rather than building a new AI frontend, Gemini Voyager enhances the existing Google interface that users are already logged into, preserving session state and billing context. This positions it as a complement to the official product rather than a replacement, making it less risky to adopt than a fully alternative frontend.

---

## 23. [nautilus_trader](https://github.com/nautechsystems/nautilus_trader)
> A high-performance algorithmic trading platform and event-driven backtester

**Language:** Rust  |  **Stars:** 20,083  |  **Forks:** 2,356  |  **Score:** 1,253  |  **Created:** 2018-06-25

**Background:** Nautilus Trader is a high-performance algorithmic trading platform and event-driven backtester developed by Nautech Systems, with its performance-critical components implemented in Rust and its user-facing API exposed through Python. It has been in development since June 2018 and has grown to over 20,000 stars, making it one of the most mature open-source algorithmic trading frameworks available. It supports live trading across multiple venues as well as historical backtesting with microsecond-resolution event replay.

**Problem it solves:** Backtesting trading strategies accurately requires event-driven simulation that faithfully reproduces the order of market events, including partial fills, latency, and market impact. Most open-source backtesting frameworks use vectorized computation that approximates this behavior. Nautilus Trader's event-driven architecture provides higher-fidelity simulation that reduces the gap between backtest and live performance.

**Why another one?** Nautilus Trader's Rust core gives it performance characteristics — microsecond event processing, low GC pressure — that pure-Python alternatives cannot match. Its longevity (active since 2018) and steady feature additions mean it keeps accumulating attention from professional quantitative developers who need production-grade tooling rather than research prototypes.

---

## 24. [notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli)
> NotebookLM MCP CLI tool

**Language:** Python  |  **Stars:** 1,500  |  **Forks:** 319  |  **Score:** 1,186  |  **Created:** 2025-12-23

**Background:** NotebookLM MCP CLI is a Python command-line tool by jacob-bd that exposes Google NotebookLM's functionality through the Model Context Protocol (MCP), enabling AI agents to interact with NotebookLM notebooks programmatically. It launched in December 2025 and has accumulated 1,500 stars, primarily from developers building MCP-compatible agent workflows. The tool bridges the gap between the NotebookLM interface and the broader MCP ecosystem.

**Problem it solves:** Google NotebookLM has no official API, making it inaccessible to automated workflows and AI agents that need to query or manage notebooks programmatically. This tool wraps NotebookLM's underlying interface with an MCP-compatible CLI, allowing agents that speak MCP to treat NotebookLM as a tool they can invoke directly.

**Why another one?** The MCP ecosystem is growing rapidly as a standard protocol for agent-tool communication, and NotebookLM is a widely used research tool with no official programmatic interface. This project fills a specific integration gap — NotebookLM as an MCP tool — that no official or competing project currently addresses.

---

## 25. [midday](https://github.com/midday-ai/midday)
> Invoicing, Time tracking, File reconciliation, Storage, Financial Overview & your own Assistant made for Freelancers

**Language:** TypeScript  |  **Stars:** 14,034  |  **Forks:** 1,349  |  **Score:** 1,184  |  **Created:** 2023-09-18

**Background:** Midday is an open-source business management platform built by midday-ai and targeted specifically at freelancers and independent contractors. It bundles invoicing, time tracking, file reconciliation, financial overviews, and an embedded AI assistant into a single TypeScript application. Launched in September 2023, it has grown to over 14,000 stars by addressing the fragmented tooling that freelancers typically assemble from multiple paid services.

**Problem it solves:** Freelancers typically use separate tools for invoicing, time tracking, document storage, and financial reporting — each with its own subscription cost and data silo. Midday consolidates these functions into a single self-hostable platform with an AI assistant that can answer questions about earnings, outstanding invoices, and time allocations directly from the unified data.

**Why another one?** Midday's differentiation is its freelancer-specific focus combined with an AI assistant that has access to all financial and time-tracking data in the platform. General-purpose accounting tools are not designed for project-based income patterns, and freelancer-focused SaaS products are expensive. Midday offers a self-hosted alternative with a purpose-built data model for freelance business management.

---

> **Day's theme:** Agentic skills, personal AI assistants, and developer tooling for autonomous workflows dominated trending on February 16, 2026, reflecting the industry's rapid shift toward composable, self-hosted AI infrastructure.
