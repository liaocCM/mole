# Trendshift Weekly Report — 2026-02-16 to 2026-02-22
**Total unique repositories:** 84 (from 175 daily entries across 7 days)

---

## 1. [zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)
> Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything

**Language:** Rust  |  **Stars:** 16846  |  **Forks:** 1937  |  **Best Score:** 15263  |  **Best Rank:** #1  |  **Days on chart:** 2/7  |  **Created:** 2026-02-13

**Background:** Zeroclaw is a newly released autonomous AI assistant infrastructure project written in Rust, emphasizing raw performance and minimal binary size. It launched on February 13, 2026 and accumulated nearly 17,000 stars within days, signaling strong pent-up demand for a Rust-native alternative to the TypeScript-heavy assistant platforms that dominate the space. The project is built around a pluggable architecture that allows any LLM backend, tool, or deployment target to be swapped without touching core infrastructure code.

**Problem it solves:** Existing AI assistant platforms are predominantly written in Python or TypeScript and carry substantial runtime overhead, making them difficult to deploy on edge hardware or in resource-constrained environments. Zeroclaw compiles to a single small binary with no interpreter dependency, enabling deployment on devices and environments where Python runtimes or Node.js are unavailable or impractical. Its swap-anything design also removes vendor lock-in at the model layer.

**Why another one?** The Rust ecosystem has lacked a first-class autonomous agent infrastructure library to rival what LangChain or the Anthropic Agents SDK offer for Python and TypeScript. Zeroclaw fills that gap with memory safety guarantees from the Rust type system and deterministic performance characteristics. The timing — shortly after several high-profile AI assistant platforms reported reliability issues under load — appears to have accelerated adoption.

---

## 2. [cs-video-courses](https://github.com/Developer-Y/cs-video-courses)
> List of Computer Science courses with video lectures.

**Language:** N/A  |  **Stars:** 74570  |  **Forks:** 9957  |  **Best Score:** 11544  |  **Best Rank:** #2  |  **Days on chart:** 2/7  |  **Created:** 2016-10-21

**Background:** cs-video-courses is a community-maintained curated list of free Computer Science courses that include video lectures, organized by subject area — algorithms, operating systems, machine learning, distributed systems, and more. Started by Developer-Y in October 2016, it has grown into one of the largest single-file references for self-directed CS education on GitHub. The list links directly to lecture series hosted on YouTube, Coursera, MIT OpenCourseWare, and similar platforms.

**Problem it solves:** High-quality CS lecture content is scattered across dozens of university websites, YouTube channels, and MOOC platforms with inconsistent tagging and discoverability. This repository consolidates them into a single, browsable index organized by topic, saving learners the time of hunting down what is actually available for free.

**Why another one?** cs-video-courses recurrently trends because it is the most comprehensive single-repository index of its kind and is continuously updated by community pull requests as new courses appear. Its staying power comes from the fact that it covers the full CS curriculum rather than a single subject, making it relevant to learners at any stage.

---

## 3. [picoclaw](https://github.com/sipeed/picoclaw)
> Tiny, Fast, and Deployable anywhere — automate the mundane, unleash your creativity

**Language:** Go  |  **Stars:** 17835  |  **Forks:** 2110  |  **Best Score:** 9288  |  **Best Rank:** #1  |  **Days on chart:** 4/7  |  **Created:** 2026-02-04

**Background:** Picoclaw is a Go-based automation and deployment platform from Sipeed, designed to be minimal in footprint while capable of running across diverse hardware targets. It launched in early February 2026 and accumulated nearly 18,000 stars in under two weeks, suggesting strong word-of-mouth within the embedded and edge computing communities. The project emphasizes portability, targeting environments ranging from developer laptops to resource-constrained microcontrollers.

**Problem it solves:** Deploying automation workflows to heterogeneous hardware — including low-power boards and embedded systems — typically requires environment-specific toolchains and heavy runtime dependencies. Picoclaw provides a single binary that can be dropped onto almost any target and begin executing workflows immediately, eliminating the bootstrapping friction that plagues conventional CI/CD tools on edge hardware.

**Why another one?** Most automation platforms are designed for cloud or server-class hardware and carry runtimes that are too large for constrained targets. Picoclaw differentiates by treating tiny devices as first-class deployment targets rather than afterthoughts. Its rapid star growth suggests it is filling a genuine gap for teams building on Sipeed's embedded hardware ecosystem.

---

## 4. [vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands)
> VSCode theme based off the easemate IDE and Jetbrains islands theme

**Language:** PowerShell  |  **Stars:** 3740  |  **Forks:** 108  |  **Best Score:** 8115  |  **Best Rank:** #1  |  **Days on chart:** 2/7  |  **Created:** 2026-02-14

**Background:** vscode-dark-islands is a color theme for Visual Studio Code that draws aesthetic inspiration from the easemate IDE and the JetBrains Islands theme family. It was created just days before this report, yet rapidly accumulated thousands of stars, signaling strong latent demand for this visual style. The theme is distributed and configured via PowerShell tooling targeting Windows-first developer workflows.

**Problem it solves:** Many developers who switch between JetBrains IDEs and VS Code miss the familiar Islands color palette in their new editor. This theme bridges that aesthetic gap without requiring a full IDE switch. It provides a cohesive dark environment that reduces context-switching friction for polyglot developers.

**Why another one?** The JetBrains Islands theme has a devoted following, and no prior VS Code port matched its fidelity closely enough. Its explosive launch-week growth suggests it filled a specific niche that generic dark themes had left unaddressed.

---

## 5. [pentagi](https://github.com/vxcontrol/pentagi)
> Fully autonomous AI Agents system capable of performing complex penetration testing tasks

**Language:** Go  |  **Stars:** 4228  |  **Forks:** 588  |  **Best Score:** 7012  |  **Best Rank:** #1  |  **Days on chart:** 4/7  |  **Created:** 2025-01-06

**Background:** PentAGI is a self-hosted autonomous agent system for penetration testing, built in Go by vxcontrol. It bundles over 20 professional security tools — including nmap, Metasploit, and sqlmap — inside isolated Docker containers and uses a multi-agent architecture where a lead agent delegates to specialized sub-agents for research, development, and infrastructure tasks. A Neo4j-backed knowledge graph provides long-term memory across testing sessions.

**Problem it solves:** Security testing requires orchestrating dozens of tools in sequence, interpreting intermediate outputs, and adapting attack paths based on findings — a process that demands deep expertise and significant time. PentAGI automates this orchestration layer, allowing the system to autonomously chain tools together and produce detailed vulnerability reports with exploitation guidance.

**Why another one?** PentAGI is fully self-hosted and open-source, distinguishing it from commercial AI-assisted security platforms. Its architecture includes a full REST and GraphQL API, Grafana/Prometheus monitoring integration, and a bundled scraper container for browser-based OSINT — a level of completeness uncommon in open-source security tooling.

---

## 6. [nanoclaw](https://github.com/qwibitai/nanoclaw)
> A lightweight alternative to Clawdbot / OpenClaw that runs in containers for security. Connects to WhatsApp, has memory, scheduled jobs, and runs directly on Anthropic's Agents SDK

**Language:** TypeScript  |  **Stars:** 10547  |  **Forks:** 1504  |  **Best Score:** 6356  |  **Best Rank:** #1  |  **Days on chart:** 1/7  |  **Created:** 2026-01-31

**Background:** Nanoclaw is a containerized personal AI assistant built on Anthropic's Agents SDK, positioned as a lightweight alternative to both Clawdbot and OpenClaw. It connects natively to WhatsApp as its primary messaging interface and ships with persistent memory and scheduled job support out of the box. The project launched at the end of January 2026 and has rapidly accumulated over 10,000 stars.

**Problem it solves:** OpenClaw is a full-featured assistant platform with a massive codebase and complex deployment requirements. Nanoclaw strips the concept down to a containerized runtime that is simpler to deploy and secure, while retaining the core features most users need: messaging integration, persistent memory, and task scheduling. Running inside containers provides process-level isolation without requiring a full VM or orchestration layer.

**Why another one?** The key differentiator is the direct integration with Anthropic's Agents SDK rather than building a custom agent runtime, which means Nanoclaw benefits from upstream improvements to the SDK without reimplementation. The container-first architecture also makes it easier to deploy on any Docker-compatible host, from a Raspberry Pi to a cloud VM, without the dependency sprawl of larger assistant platforms.

---

## 7. [openclaw](https://github.com/openclaw/openclaw)
> Your own personal AI assistant. Any OS. Any Platform. The lobster way.

**Language:** TypeScript  |  **Stars:** 215287  |  **Forks:** 40386  |  **Best Score:** 6129  |  **Best Rank:** #2  |  **Days on chart:** 6/7  |  **Created:** 2025-11-24

**Background:** OpenClaw is a personal AI assistant platform that runs on any operating system and claims compatibility with any underlying AI model or API. It is built in TypeScript and has accumulated over 215,000 stars since its November 2025 launch, making it one of the fastest-growing open-source repositories in the personal assistant category. Its branding around "the lobster way" reflects a community identity that has developed rapidly around the project.

**Problem it solves:** Proprietary AI assistants are locked to specific platforms, app stores, or subscription services, limiting user control over data and model choice. OpenClaw provides a self-hosted alternative that works on any OS, connects to any AI provider, and keeps all data under the user's control — addressing privacy and portability concerns simultaneously.

**Why another one?** OpenClaw keeps trending because its star count places it in a category by itself among personal assistant platforms — its 215,000+ stars dwarf most comparable projects. Its cross-platform universality and active community ecosystem of skills and plugins drive continued discovery and repeat appearances on trending lists.

---

## 8. [heretic](https://github.com/p-e-w/heretic)
> Fully automatic censorship removal for language models

**Language:** Python  |  **Stars:** 8887  |  **Forks:** 884  |  **Best Score:** 5620  |  **Best Rank:** #3  |  **Days on chart:** 4/7  |  **Created:** 2025-09-21

**Background:** Heretic is a Python tool authored by p-e-w that automates the removal of content filters and refusal behaviors from language models. It operates on locally run models rather than API-accessed services, using techniques to modify model behavior at inference time. Since its September 2025 release it has attracted nearly 9,000 stars and significant community discussion around the ethics and legality of model censorship removal.

**Problem it solves:** Language models fine-tuned for public deployment often refuse legitimate requests from researchers, security professionals, and developers working on sensitive but lawful domains. Heretic provides a local, automated method to remove these restrictions for users running models on their own hardware, without requiring manual fine-tuning or dataset curation.

**Why another one?** The project occupies a deliberately controversial niche — automated, no-expertise-required censorship removal — that distinguishes it from manual jailbreaking or fine-tuning approaches. Its automation and local-first design mean users do not need to send data to a third party. The ongoing public debate about AI content moderation keeps it in the spotlight.

---

## 9. [voicebox](https://github.com/jamiepine/voicebox)
> The open-source voice synthesis studio powered by Qwen3-TTS.

**Language:** TypeScript  |  **Stars:** 9955  |  **Forks:** 1040  |  **Best Score:** 4707  |  **Best Rank:** #2  |  **Days on chart:** 5/7  |  **Created:** 2026-01-25

**Background:** Voicebox is an open-source voice synthesis studio built in TypeScript that uses the Qwen3-TTS model as its inference backend. It provides a graphical studio interface for generating, editing, and exporting synthesized speech. The project targets content creators, developers building voice applications, and researchers evaluating TTS model quality.

**Problem it solves:** High-quality TTS systems have historically been locked behind expensive API tiers or required deep ML expertise to run locally. Voicebox wraps Qwen3-TTS in an accessible studio UI, making professional-grade voice synthesis available without per-character billing. It also exposes batch processing and voice parameter controls not available in most SaaS alternatives.

**Why another one?** Qwen3-TTS represents a step change in open-weight TTS quality, and voicebox was among the first polished front-ends built specifically for it. Its rapid star growth reflects demand for a production-ready interface to pair with the new model capability.

---

## 10. [awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources)
> Learn System Design concepts and prepare for interviews using free resources.

**Language:** Java  |  **Stars:** 33577  |  **Forks:** 7447  |  **Best Score:** 4667  |  **Best Rank:** #2  |  **Days on chart:** 2/7  |  **Created:** 2023-10-25

**Background:** Maintained by Ashish Pratap Singh, this repository is a curated collection of free learning materials covering distributed systems fundamentals, common architecture patterns, and practical interview preparation guides. It organizes resources by topic — from CAP theorem and consensus protocols to real-world case studies of systems at companies like Netflix and Uber. The repository has grown steadily since October 2023 to over 33,000 stars.

**Problem it solves:** System design interview preparation is fragmented across paid courses, scattered blog posts, and YouTube videos of varying quality. This repository consolidates high-quality free resources into a single structured reference, reducing the time candidates spend hunting for reliable material. It also serves as a self-study curriculum for engineers who want to deepen their distributed systems knowledge outside of an interview context.

**Why another one?** It keeps trending because system design interviews remain a high-stakes bottleneck in engineering hiring, and the repository continues to receive active updates with new case studies and resource links. Its Java code examples alongside the conceptual writeups give it broader utility than a purely textual resource list.

---

## 11. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 56468  |  **Forks:** 4282  |  **Best Score:** 4288  |  **Best Rank:** #3  |  **Days on chart:** 6/7  |  **Created:** 2025-10-09

**Background:** Superpowers is a composable skills framework and structured software development methodology created by Jesse Vincent (obra). It installs into coding agents such as Claude Code, Cursor, Codex, and OpenCode via their plugin systems, enforcing a multi-stage workflow: brainstorm and refine a spec, produce a detailed implementation plan, then execute through subagent-driven development with two-stage code review. The project has accumulated over 56,000 stars since October 2025.

**Problem it solves:** Coding agents left to default settings tend to skip planning, ignore test-driven development, and drift from the original intent mid-session. Superpowers installs guard rails — mandatory spec approval, red-green-refactor TDD enforcement, and plan checkpoints — so an agent can work autonomously for extended periods without derailing from what was agreed upon.

**Why another one?** Rather than being a new coding agent, Superpowers is a methodology layer that works across multiple agents via their plugin systems. The portability — same skills install in Claude Code, Cursor, Codex, and OpenCode — and the emphasis on subagent delegation rather than a single long-running context are the primary differentiators. It continues trending as new agentic coding users discover cross-agent compatibility.

---

## 12. [zvec](https://github.com/alibaba/zvec)
> A lightweight, lightning-fast, in-process vector database

**Language:** C++  |  **Stars:** 5951  |  **Forks:** 330  |  **Best Score:** 4236  |  **Best Rank:** #5  |  **Days on chart:** 4/7  |  **Created:** 2025-12-05

**Background:** Zvec is an in-process vector database developed by Alibaba, written in C++ for minimal overhead and maximum throughput. Unlike standalone vector database servers, it embeds directly into the calling application's process, eliminating the network round-trip cost for every similarity search. It was released in December 2025 and has grown to nearly 6,000 stars in roughly ten weeks.

**Problem it solves:** Running a vector database as a separate service introduces latency, operational complexity, and infrastructure cost that is difficult to justify for applications with moderate embedding workloads. Zvec brings vector search in-process alongside the application, allowing similarity queries to execute at memory speeds without inter-process communication or serialization overhead.

**Why another one?** Most widely adopted vector databases — Pinecone, Weaviate, Qdrant — are designed as standalone services. Zvec occupies the in-process niche, comparable to SQLite's position relative to full database servers. Alibaba's backing and C++ implementation give it credibility and performance benchmarks that attract teams frustrated by the operational burden of running a separate vector service.

---

## 13. [OpenViking](https://github.com/volcengine/OpenViking)
> OpenViking is an open-source context database designed specifically for AI Agents.

**Language:** Python  |  **Stars:** 3160  |  **Forks:** 231  |  **Best Score:** 4150  |  **Best Rank:** #4  |  **Days on chart:** 2/7  |  **Created:** 2026-01-05

**Background:** OpenViking is an open-source context database developed by Volcengine, ByteDance's cloud infrastructure division. It is designed specifically for AI agent workflows, treating agent memory, tool outputs, and intermediate reasoning artifacts as a unified file system rather than a heterogeneous collection of data stores. The project launched in January 2026 and targets production agent deployments that require durable and queryable context across sessions.

**Problem it solves:** AI agents today typically manage context through a mix of in-context text, vector stores, and key-value caches, each with separate APIs and consistency guarantees. OpenViking unifies these under a single file-system abstraction, allowing agents to read and write context using familiar path-based operations regardless of the underlying storage backend.

**Why another one?** Existing context management solutions such as mem0 and Zep are either embedded libraries or hosted services. OpenViking is a standalone, self-hostable database with a file-system interface, filling a gap for teams that need persistent agent context without cloud vendor lock-in. Its Volcengine backing provides production-grade engineering resources behind the project.

---

## 14. [Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)
> Official code repo for the O'Reilly Book - "Hands-On Large Language Models"

**Language:** Jupyter Notebook  |  **Stars:** 22267  |  **Forks:** 5198  |  **Best Score:** 3676  |  **Best Rank:** #4  |  **Days on chart:** 2/7  |  **Created:** 2024-06-28

**Background:** This repository contains all code notebooks for the O'Reilly book "Hands-On Large Language Models" by Jay Alammar and Maarten Grootendorst, sometimes called "The Illustrated LLM Book" for its nearly 300 custom figures. Each chapter has a corresponding Google Colab-compatible Jupyter notebook, covering topics from tokenization and embeddings through fine-tuning, retrieval, and agents. Jay Alammar is known for his illustrated transformer explanations; Maarten Grootendorst is the author of BERTopic.

**Problem it solves:** Most LLM learning resources are either purely theoretical (academic papers) or purely practical (vendor tutorials that assume a specific platform). The book and code bridge that gap with visual explanations of how models work internally, paired with runnable notebooks that do not require a local GPU.

**Why another one?** The book continues to trend because it remains one of the most accessible entry points to LLM internals for practitioners without a deep ML background. The combination of Alammar's illustration-heavy style with Grootendorst's applied NLP expertise covers a different audience than fast.ai (which targets training from scratch) or LangChain tutorials (which focus on application building rather than model internals).

---

## 15. [prompts.chat](https://github.com/f/prompts.chat)
> a.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**Language:** HTML  |  **Stars:** 146140  |  **Forks:** 19286  |  **Best Score:** 3674  |  **Best Rank:** #3  |  **Days on chart:** 2/7  |  **Created:** 2022-12-05

**Background:** Launched in December 2022 as "Awesome ChatGPT Prompts" by Fatih Kadir Akin, prompts.chat was the first major open-source prompt collection for AI chat models. It has since evolved into a full community platform with a web frontend, a Hugging Face dataset, a self-hosting option, and an interactive book on prompt engineering. The repo has 40+ academic citations and was referenced by Harvard and Columbia.

**Problem it solves:** Early ChatGPT users had no shared repository of system prompts and persona-based instructions, making prompt discovery purely word-of-mouth. The repository provided a structured, community-maintained library of role and task prompts that could be used as a starting point, reducing the trial-and-error required to get useful outputs from general-purpose models.

**Why another one?** This repository trends recurrently because it is the canonical reference for prompt collections. Its evolution from a static markdown file into a full web platform with community submission workflows, Hugging Face dataset mirroring, and self-hosting capability has kept it relevant as a living resource rather than an archived list.

---

## 16. [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)
> The Ultimate Collection of 800+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents.

**Language:** Python  |  **Stars:** 13791  |  **Forks:** 2590  |  **Best Score:** 3616  |  **Best Rank:** #4  |  **Days on chart:** 4/7  |  **Created:** 2026-01-14

**Background:** Antigravity Awesome Skills is a community-curated registry of over 800 reusable agentic skills compatible with Claude Code, Cursor, and the Antigravity agent framework. It bundles official skills from Anthropic and Vercel alongside community contributions, and organizes them by functional category — code review, testing, deployment, documentation, and more. The repository launched in January 2026 and has rapidly become a go-to resource for teams building agentic workflows.

**Problem it solves:** Building effective agentic workflows from scratch requires significant prompt engineering and tool-calling expertise. This collection provides battle-tested, ready-to-install skills that encode best practices for common development tasks, allowing teams to adopt agentic workflows without investing weeks in custom skill development.

**Why another one?** The breadth of 800+ skills and multi-agent compatibility — covering Claude Code, Antigravity, and Cursor — gives it a wider appeal than single-platform skill collections. Its inclusion of official Anthropic and Vercel skills signals institutional backing that many community repositories lack, contributing to its rapid growth and recurring trend appearances.

---

## 17. [ProxyBridge](https://github.com/InterceptSuite/ProxyBridge)
> Proxifier Alternative to redirect any Windows/MacOS/Linux TCP and UDP traffic to HTTP/Socks5 proxy

**Language:** C  |  **Stars:** 2300  |  **Forks:** 153  |  **Best Score:** 3406  |  **Best Rank:** #5  |  **Days on chart:** 1/7  |  **Created:** 2025-10-13

**Background:** ProxyBridge is a cross-platform transparent proxy redirect tool written in C, created by InterceptSuite as an open-source alternative to the commercial Proxifier application. It intercepts TCP and UDP traffic at the system level and routes it through a user-specified HTTP or Socks5 proxy, without requiring applications to have built-in proxy support. It targets Windows, macOS, and Linux with a single consistent interface.

**Problem it solves:** Many applications do not respect system proxy settings or lack configurable proxy options, making it difficult to route their traffic through corporate proxies, VPNs, or interception tools during security testing. ProxyBridge solves this by redirecting traffic transparently at the OS level, regardless of whether the application cooperates.

**Why another one?** Proxifier is closed-source, Windows-primary, and subscription-licensed. ProxyBridge offers full cross-platform support, open-source transparency, and zero licensing cost — all critical properties for security researchers and developers who need to inspect or redirect traffic across multiple operating systems. The C implementation keeps the binary small and dependency-free.

---

## 18. [rowboat](https://github.com/rowboatlabs/rowboat)
> Open-source AI coworker, with memory

**Language:** TypeScript  |  **Stars:** 8002  |  **Forks:** 685  |  **Best Score:** 3223  |  **Best Rank:** #6  |  **Days on chart:** 2/7  |  **Created:** 2025-01-13

**Background:** Rowboat is an open-source AI coworker platform built by Rowboat Labs, featuring persistent memory that allows the agent to accumulate context across sessions. It is designed to act as a team-embedded assistant rather than a stateless chat interface, maintaining awareness of ongoing projects, decisions, and team preferences over time. The project launched in January 2025 and has grown to over 8,000 stars.

**Problem it solves:** Most AI assistants reset context between sessions, requiring users to re-explain their project state and preferences repeatedly. Rowboat's persistent memory layer allows it to build a working model of the team's projects and conventions over time, making it progressively more useful the longer it is deployed.

**Why another one?** Rowboat positions itself as an open-source alternative to commercial AI coworker products, giving teams full control over where memory is stored and how the agent is configured. The combination of persistent memory with an open, self-hostable architecture is its primary differentiator from both stateless open-source assistants and proprietary coworker platforms.

---

## 19. [polymarket-kalshi-arbitrage-bot](https://github.com/ryan26craf/polymarket-kalshi-arbitrage-bot)
> Kalshi open source trading bot to automate copy trading and arbitrage strategies on crypto prediction markets

**Language:** Python  |  **Stars:** 738  |  **Forks:** 2  |  **Best Score:** 3154  |  **Best Rank:** #9  |  **Days on chart:** 1/7  |  **Created:** 2026-02-06

**Background:** This is an open-source Python bot for automating arbitrage and copy trading strategies across Polymarket and Kalshi, two regulated prediction market platforms. It was published in February 2026 and targets traders looking to exploit price discrepancies between the same event contracts listed on different platforms. The codebase interfaces with both platforms' APIs to monitor prices and execute trades programmatically.

**Problem it solves:** Prediction market arbitrage requires monitoring multiple platforms simultaneously, calculating spread opportunities in real time, and executing trades faster than is practical manually. This bot automates the detection and execution of cross-platform arbitrage opportunities, lowering the technical barrier for traders who understand the strategy but cannot implement it from scratch.

**Why another one?** Polymarket and Kalshi have both gained significant user bases following increased regulatory clarity around prediction markets. The combination of two specific, widely-used platforms in a single bot is novel, and the open-source nature allows traders to audit and modify the strategy logic — something impossible with proprietary trading bots.

---

## 20. [Kiro](https://github.com/kirodotdev/Kiro)
> Kiro is an agentic IDE that works alongside you from prototype to production.

**Language:** TypeScript  |  **Stars:** 3041  |  **Forks:** 149  |  **Best Score:** 3133  |  **Best Rank:** #5  |  **Days on chart:** 1/7  |  **Created:** 2025-06-17

**Background:** Kiro is an agentic IDE built by the team at kirodot.dev, launched in June 2025. It provides an integrated development environment where AI agents work alongside the developer throughout the full lifecycle from prototyping to production deployment. The IDE is built in TypeScript and has accumulated over 3,000 stars.

**Problem it solves:** Most AI coding tools are bolted onto existing editors as extensions or operate as separate terminal agents, creating a disconnect between the AI's understanding and the IDE's capabilities. Kiro integrates agentic assistance directly into the IDE itself, so the AI has native access to project structure, debugging, build systems, and deployment pipelines without requiring external tool integrations.

**Why another one?** While Cursor and Windsurf added AI to VS Code forks, Kiro is built from the ground up as an agent-native IDE rather than retrofitting AI into an existing editor. The focus on the full prototype-to-production lifecycle differentiates it from tools that primarily assist with code generation but leave deployment and operations to the developer.

---

## 21. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster.

**Language:** Shell  |  **Stars:** 68067  |  **Forks:** 5340  |  **Best Score:** 3116  |  **Best Rank:** #5  |  **Days on chart:** 2/7  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official terminal-based agentic coding tool, launched in February 2025. It operates directly in the developer's terminal, understanding the full codebase context and executing tasks through natural language commands. The tool handles routine development tasks, explains complex code, manages git workflows, and supports an extensible skills and hooks system for customization.

**Problem it solves:** Developers spend significant time on repetitive coding tasks, navigating unfamiliar codebases, and managing version control workflows. Claude Code automates these tasks directly in the terminal where developers already work, eliminating the context-switching overhead of moving between an IDE, a browser-based AI chat, and the command line.

**Why another one?** Claude Code keeps trending because it is Anthropic's first-party coding agent and has become a reference implementation for terminal-based agentic development. Its growing ecosystem of community skills, hooks, and configurations drives continuous adoption. The extensibility through the skills framework means the tool's capabilities expand with community contributions rather than only through official releases.

---

## 22. [cmux](https://github.com/manaflow-ai/cmux)
> Ghostty-based macOS terminal with vertical tabs and notifications for AI coding agents

**Language:** Swift  |  **Stars:** 762  |  **Forks:** 13  |  **Best Score:** 2800  |  **Best Rank:** #6  |  **Days on chart:** 2/7  |  **Created:** 2026-01-28

**Background:** Cmux is a native macOS terminal application built on Ghostty's terminal emulation library, developed by Manaflow AI. It is designed specifically for AI coding agent workflows, featuring vertical tabs for managing multiple agent sessions, built-in notifications when agents complete tasks, and a streamlined interface optimized for monitoring concurrent agent runs.

**Problem it solves:** Developers running multiple AI coding agents simultaneously struggle with terminal management — standard terminals lack notifications for long-running agent tasks and make it difficult to monitor multiple sessions at a glance. Cmux provides purpose-built UI for this workflow with vertical tabs and completion notifications.

**Why another one?** Existing terminals like iTerm2, Warp, and Ghostty itself are general-purpose tools not optimized for the specific pattern of running and monitoring AI agents. Cmux narrows its scope to this single use case, providing agent-aware notifications and a vertical tab layout designed for concurrent session monitoring rather than traditional shell workflows.

---

## 23. [fluxer](https://github.com/fluxerapp/fluxer)
> A free and open source instant messaging and VoIP platform built for friends, groups, and communities.

**Language:** TypeScript  |  **Stars:** 4321  |  **Forks:** 172  |  **Best Score:** 2718  |  **Best Rank:** #7  |  **Days on chart:** 4/7  |  **Created:** 2026-01-01

**Background:** Fluxer is an open-source instant messaging and VoIP platform built in TypeScript, targeting friend groups and online communities as its primary audience. It launched on January 1, 2026 and has grown to over 4,300 stars in its first six weeks. The platform is positioned as a free, self-hostable alternative to proprietary communication platforms, offering text messaging, voice, and community organization features.

**Problem it solves:** Popular communication platforms like Discord are closed-source, hosted entirely by a single company, and subject to policy changes that can affect entire communities. Fluxer provides a self-hostable alternative, giving community operators control over their infrastructure, data retention policies, and moderation tooling without dependence on a third-party platform.

**Why another one?** The demand for open-source Discord alternatives is ongoing and has produced multiple projects, but few achieve the full feature parity of text, voice, and community management in a single self-hostable package. Fluxer's TypeScript stack makes it approachable for contributors familiar with modern web development tooling.

---

## 24. [RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)
> Showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems.

**Language:** Jupyter Notebook  |  **Stars:** 25501  |  **Forks:** 2991  |  **Best Score:** 2706  |  **Best Rank:** #6  |  **Days on chart:** 2/7  |  **Created:** 2024-07-13

**Background:** RAG_Techniques is a comprehensive Jupyter Notebook collection by Nir Diamant demonstrating advanced retrieval-augmented generation techniques beyond basic vector search. It covers approaches such as hybrid retrieval, re-ranking, multi-query expansion, contextual compression, and agentic RAG patterns. The repository has grown to over 25,000 stars since its launch in July 2024 and is regularly updated with new techniques.

**Problem it solves:** Basic RAG implementations using a single embedding model and cosine similarity often produce poor retrieval quality for complex queries. The techniques in this repository address specific failure modes — query ambiguity, semantic drift, context overflow, and relevance degradation — with concrete, runnable notebook implementations rather than theoretical descriptions.

**Why another one?** RAG_Techniques trends recurrently because it is the most comprehensive open-source collection of practical RAG patterns with working code. As new retrieval techniques are published in research papers, Diamant adds notebook implementations, keeping the repository current and making it a first stop for ML engineers building production RAG systems.

---

## 25. [humanizer](https://github.com/blader/humanizer)
> Claude Code skill that removes signs of AI-generated writing from text

**Language:** N/A  |  **Stars:** 6015  |  **Forks:** 457  |  **Best Score:** 2666  |  **Best Rank:** #7  |  **Days on chart:** 1/7  |  **Created:** 2026-01-18

**Background:** Humanizer is a Claude Code skill created by blader that rewrites AI-generated text to remove telltale signs of machine authorship. It operates as a plugin within the Claude Code environment, analyzing text for common AI writing patterns — such as excessive hedging, formulaic transitions, and unnatural phrasing — and rewrites them to read more naturally. The project has gained over 6,000 stars since January 2026.

**Problem it solves:** AI-generated text often exhibits recognizable patterns that make it obvious to readers and detectors alike: overly formal tone, repetitive sentence structure, and characteristic filler phrases. Humanizer processes such text to produce output that reads as naturally written, addressing both readability concerns and detection avoidance.

**Why another one?** Unlike standalone paraphrasing tools or web-based rewriters, Humanizer integrates directly into the Claude Code workflow as a skill, allowing users to apply it immediately to any text output without leaving their development environment. The tight integration with Claude Code's skill system makes it a single-command operation rather than a separate tool.

---

## 26. [airllm](https://github.com/lyogavin/airllm)
> AirLLM 70B inference with single 4GB GPU

**Language:** Jupyter Notebook  |  **Stars:** 11717  |  **Forks:** 1066  |  **Best Score:** 2626  |  **Best Rank:** #7  |  **Days on chart:** 1/7  |  **Created:** 2023-06-12

**Background:** AirLLM is a library that enables running 70-billion-parameter language models on a single GPU with as little as 4GB of VRAM. Created by Gavin Li and first released in June 2023, it uses layer-by-layer inference with aggressive memory management to fit models that would normally require multiple high-end GPUs. The project has steadily grown to nearly 12,000 stars.

**Problem it solves:** Running large language models locally typically requires expensive multi-GPU setups or cloud instances with 80+ GB of VRAM. AirLLM makes 70B-class models accessible to developers and researchers with consumer-grade hardware by trading inference speed for dramatically reduced memory requirements.

**Why another one?** While quantization libraries like GPTQ and AWQ reduce model size, they still require fitting the entire quantized model in memory. AirLLM takes a fundamentally different approach by streaming layers through GPU memory, which means the VRAM requirement is bounded by the largest single layer rather than the full model. This architectural choice enables a class of hardware that quantization alone cannot serve.

---

## 27. [summarize](https://github.com/steipete/summarize)
> Point at any URL/YouTube/Podcast or file. Get the gist. CLI and Chrome Extension.

**Language:** TypeScript  |  **Stars:** 3905  |  **Forks:** 240  |  **Best Score:** 2606  |  **Best Rank:** #8  |  **Days on chart:** 1/7  |  **Created:** 2025-12-17

**Background:** Summarize is a TypeScript tool by steipete that accepts a URL, YouTube video, podcast feed, or local file and returns a concise summary using an underlying language model. It ships as both a CLI utility and a Chrome extension, covering both terminal and browser workflows. The project focuses on minimal configuration — paste a link and receive output.

**Problem it solves:** Consuming long-form content like podcasts and technical articles is time-consuming when the reader only needs the key points. Summarize automates the transcription and condensation step, making it practical to triage large content queues quickly. The dual CLI/extension delivery means users are not forced to switch contexts to use it.

**Why another one?** Most summarization tools are web services that require accounts and send user data to third-party servers. Summarize is self-hosted and model-agnostic, appealing to privacy-conscious users who already have API access to a preferred model provider.

---

## 28. [hummingbot](https://github.com/hummingbot/hummingbot)
> Open source software that helps you create and deploy high-frequency crypto trading bots

**Language:** Python  |  **Stars:** 17391  |  **Forks:** 4464  |  **Best Score:** 2423  |  **Best Rank:** #10  |  **Days on chart:** 3/7  |  **Created:** 2019-04-02

**Background:** Hummingbot is a mature open-source framework for building and deploying high-frequency cryptocurrency trading bots, originally released in April 2019. It supports market-making, arbitrage, and directional strategies across dozens of centralized and decentralized exchanges through a unified connector interface. The project has over 17,000 stars, nearly 4,500 forks, and a long track record of production use by both individual traders and market-making firms.

**Problem it solves:** Building a high-frequency trading bot that connects reliably to multiple exchanges, handles order lifecycle management, and executes strategies with low latency requires significant engineering effort. Hummingbot abstracts the exchange connectivity and order management layers, allowing traders to implement and backtest strategies without rebuilding infrastructure from scratch for each exchange.

**Why another one?** Hummingbot continues to trend because it remains one of the few open-source HFT frameworks with broad exchange coverage and an active governance community. New exchange listings, strategy additions, and periodic market volatility that drives trader interest keep it visible on trending lists years after its initial release.

---

## 29. [cs249r_book](https://github.com/harvard-edge/cs249r_book)
> Introduction to Machine Learning Systems

**Language:** JavaScript  |  **Stars:** 20499  |  **Forks:** 2359  |  **Best Score:** 2416  |  **Best Rank:** #11  |  **Days on chart:** 2/7  |  **Created:** 2023-09-06

**Background:** cs249r_book is the open-source textbook for Harvard's CS249r course, "Tiny Machine Learning," developed by the Harvard Edge Computing Lab. The book covers the full stack of ML systems from model design and hardware constraints to deployment on edge devices and embedded systems. It is authored collaboratively on GitHub using Quarto and rendered as a web book, allowing community contributions via pull requests.

**Problem it solves:** Most ML educational resources focus on model accuracy and training techniques without addressing the systems-level concerns that arise when deploying models on constrained hardware. This textbook bridges that gap by covering quantization, hardware-software co-design, inference optimization, and real-world deployment considerations in a structured academic format.

**Why another one?** The book trends recurrently because it is one of the few openly licensed, university-quality textbooks covering ML systems end-to-end rather than just ML theory. As edge AI deployment becomes more mainstream, interest in practical systems knowledge has grown, and this remains the most comprehensive free resource in the space.

---

## 30. [worldmonitor](https://github.com/koala73/worldmonitor)
> Real-time global intelligence dashboard — AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking

**Language:** TypeScript  |  **Stars:** 8834  |  **Forks:** 1068  |  **Best Score:** 2225  |  **Best Rank:** #9  |  **Days on chart:** 1/7  |  **Created:** 2026-01-08

**Background:** WorldMonitor is a TypeScript-based real-time dashboard that aggregates global news, geopolitical events, and infrastructure status into a unified situational awareness interface. It uses AI to classify and prioritize incoming signals, surfacing the most actionable intelligence for users monitoring global developments. Launched in January 2026, it has grown to nearly 9,000 stars in under six weeks.

**Problem it solves:** Analysts and researchers monitoring global events must manually aggregate information from dozens of news sources, RSS feeds, and government advisories, then filter noise from signal. WorldMonitor automates the aggregation and AI-powered triage step, presenting a consolidated view of geopolitical and infrastructure events ranked by significance.

**Why another one?** Existing commercial intelligence dashboards are expensive and designed for enterprise procurement cycles. WorldMonitor is self-hostable and open-source, making real-time global situational awareness accessible to independent researchers, journalists, and security teams who cannot afford commercial platforms.

---

## 31. [convert](https://github.com/p2r3/convert)
> Truly universal online file converter

**Language:** TypeScript  |  **Stars:** 1931  |  **Forks:** 173  |  **Best Score:** 2185  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2025-12-07

**Background:** convert is a TypeScript-based online file conversion tool created by p2r3 in December 2025 that aims to support a broader range of file formats than existing converters by composing multiple underlying conversion libraries. It is designed to run as a self-hostable web application rather than requiring upload to a third-party service. The project has reached nearly 2,000 stars within roughly two months of release.

**Problem it solves:** Existing online file converters either support a narrow set of formats, impose file size limits, or require uploading sensitive files to cloud services. Developers and power users who need to convert uncommon formats, work with large files, or avoid sending data to third parties have had limited self-hostable options. convert bundles a wide range of conversion backends behind a single unified interface.

**Why another one?** The "truly universal" positioning reflects a genuine gap in self-hostable converters: most open-source alternatives focus on a single media type such as video or document conversion. By composing multiple libraries into one deployable application, convert avoids the need to run and maintain separate tools for different format families. Its high score relative to its star count indicates rapid recent growth and strong trending momentum.

---

## 32. [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
> GitNexus: The Zero-Server Code Intelligence Engine - a client-side knowledge graph creator that runs entirely in your browser.

**Language:** TypeScript  |  **Stars:** 885  |  **Forks:** 82  |  **Best Score:** 2174  |  **Best Rank:** #10  |  **Days on chart:** 2/7  |  **Created:** 2025-08-02

**Background:** GitNexus is a client-side code intelligence tool that generates interactive knowledge graphs from GitHub repositories or ZIP files, running entirely in the browser with no server component. It includes a built-in Graph RAG Agent that allows users to query the generated knowledge graph conversationally. The project was created by Abhigyan Patwari and launched in August 2025.

**Problem it solves:** Understanding an unfamiliar codebase typically requires cloning, setting up a local environment, and manually tracing dependencies and relationships between modules. GitNexus eliminates the setup step entirely — users drop in a repo URL or ZIP file in their browser and immediately get a visual knowledge graph of the codebase's structure with an AI agent for exploration.

**Why another one?** The zero-server, fully client-side architecture is the primary differentiator against code intelligence tools like Sourcegraph or CodeSee, which require server-side indexing. Running entirely in the browser means no data leaves the user's machine, addressing privacy concerns for proprietary codebases. The integrated Graph RAG Agent adds conversational exploration on top of the visual graph.

---

## 33. [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
> System Prompts, Internal Tools & AI Models of major AI coding tools

**Language:** N/A  |  **Stars:** 115359  |  **Forks:** 29733  |  **Best Score:** 2172  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2025-03-05

**Background:** This repository is a comprehensive archive of extracted system prompts, internal tool definitions, and model configurations from over 30 major AI coding and assistant tools. It covers products from Anthropic, Cursor, Devin AI, Replit, Windsurf, Perplexity, and many others. The repository has amassed over 115,000 stars since March 2025, making it one of the most-starred prompt extraction collections on GitHub.

**Problem it solves:** AI tool system prompts are proprietary and hidden from users, making it difficult to understand how these tools work internally, what constraints they operate under, or how to build similar capabilities. This repository surfaces those prompts for study, comparison, and educational purposes, enabling developers to learn from production-grade prompt engineering.

**Why another one?** The repository keeps trending because new AI coding tools launch frequently and existing ones update their system prompts regularly, creating ongoing demand for documentation of changes. With coverage of over 30 tools and nearly 30,000 forks, it has become the de facto reference for comparing how different AI products are prompted and configured.

---

## 34. [awesome-software-design](https://github.com/QDenka/awesome-software-design)
> Organizing and structuring software through patterns, decisions, and verified design rules

**Language:** N/A  |  **Stars:** 737  |  **Forks:** 48  |  **Best Score:** 2154  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2026-02-11

**Background:** Awesome Software Design is a curated list repository by QDenka focused on software architecture patterns, architectural decision records, and verified design principles. It launched on February 11, 2026 — just five days before this report — and already shows enough traffic to appear in trending rankings. The repository organizes its content around structure and decision-making frameworks rather than specific technologies.

**Problem it solves:** Software design knowledge is scattered across books, conference talks, and blog posts with inconsistent quality. This repository attempts to consolidate authoritative references on patterns and design decisions into a single structured list, giving engineers a starting point for learning or revisiting architectural concepts without wading through low-quality content.

**Why another one?** Its fresh launch date means it is still accumulating early adopter momentum. The focus on decision records and verified design rules — rather than just listing pattern names — gives it a more practical orientation than older awesome-lists in the architecture space, which may explain its early traction.

---

## 35. [daytona](https://github.com/daytonaio/daytona)
> Daytona is a Secure and Elastic Infrastructure for Running AI-Generated Code

**Language:** TypeScript  |  **Stars:** 59524  |  **Forks:** 5058  |  **Best Score:** 2139  |  **Best Rank:** #12  |  **Days on chart:** 1/7  |  **Created:** 2024-02-06

**Background:** Daytona is a self-hostable development environment management platform that has evolved into infrastructure specifically optimized for executing AI-generated code securely. It provisions isolated development environments on demand and manages their lifecycle, originally focusing on standardized dev containers for human developers before pivoting to serve AI code execution workloads. The project has over 59,000 stars and a large fork base accumulated over two years.

**Problem it solves:** Running AI-generated code safely requires sandboxed environments with controlled network access, resource limits, and rapid spin-up and tear-down. General-purpose container orchestration tools like Docker Compose or Kubernetes are too heavyweight for the sub-second provisioning that agentic workflows require. Daytona provides a purpose-built runtime layer with the security isolation and elasticity that AI coding agents need to execute untrusted code.

**Why another one?** Daytona occupies a specific niche: infrastructure for AI code execution rather than for human development workflows. As coding agents become more common in production pipelines, the need for a dedicated, secure execution layer that integrates with agent orchestration systems has grown. The project's existing star count keeps it on the trending radar, and each wave of interest in agentic coding tools brings new users to its deployment story.

---

## 36. [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
> An AI SKILL that provides design intelligence for building professional UI/UX

**Language:** Python  |  **Stars:** 33111  |  **Forks:** 3278  |  **Best Score:** 2131  |  **Best Rank:** #12  |  **Days on chart:** 1/7  |  **Created:** 2025-11-30

**Background:** ui-ux-pro-max-skill is an AI agent skill that injects design system awareness and UI/UX best practices into coding assistants like Claude Code and Cursor. It provides structured prompting, component pattern libraries, and platform-specific design guidance for web, mobile, and desktop targets. The skill is authored in Python and integrates with the standard agentic skill invocation protocol.

**Problem it solves:** AI coding assistants generate functionally correct code but frequently produce visually inconsistent or accessibility-deficient interfaces. This skill closes the gap by encoding professional design principles — spacing, typography, color contrast, and component hierarchy — as agent-accessible context. Developers without a dedicated designer can produce more polished outputs by invoking the skill alongside their coding assistant.

**Why another one?** Generic code generation skills ignore design entirely, and dedicated design tools operate outside the developer's coding environment. This skill is unique in embedding design intelligence directly into the agentic coding loop rather than treating design as a separate, later step.

---

## 37. [seerr](https://github.com/seerr-team/seerr)
> Open-source media request and discovery manager for Jellyfin, Plex, and Emby.

**Language:** TypeScript  |  **Stars:** 9534  |  **Forks:** 624  |  **Best Score:** 2120  |  **Best Rank:** #12  |  **Days on chart:** 3/7  |  **Created:** 2022-03-09

**Background:** Seerr is a self-hosted media request and discovery management tool that integrates with Jellyfin, Plex, and Emby home media servers. It provides a Netflix-style discovery interface for browsing and requesting new content, backed by automated download workflows through Sonarr and Radarr. The project was created in March 2022 and has grown to over 9,500 stars through the home media server community.

**Problem it solves:** Home media server operators typically need to manually field content requests from family members and friends, then queue downloads themselves. Seerr gives non-technical users a polished request interface while automating the fulfillment pipeline — a user requests a title, and Seerr passes it to the appropriate download manager without operator intervention.

**Why another one?** Seerr gained traction by supporting Jellyfin — a fully open-source media server — in addition to Plex and Emby, giving it a broader audience than Jellyseerr (Jellyfin-only) or Overseerr (Plex-only). Its unified multi-server support is the primary differentiator that keeps it visible across the home server community.

---

## 38. [qwen-code](https://github.com/QwenLM/qwen-code)
> An open-source AI agent that lives in your terminal.

**Language:** TypeScript  |  **Stars:** 19129  |  **Forks:** 1657  |  **Best Score:** 2112  |  **Best Rank:** #13  |  **Days on chart:** 1/7  |  **Created:** 2025-06-26

**Background:** Qwen-code is QwenLM's open-source terminal coding agent, analogous in concept to Claude Code but powered by the Qwen model family. It integrates directly into the developer's terminal, understands codebase context, and can execute multi-step coding tasks through natural language commands. Released in June 2025, it has accumulated over 19,000 stars as part of Alibaba Cloud's effort to build a full developer toolchain around the Qwen models.

**Problem it solves:** Terminal coding agents have been dominated by proprietary offerings tied to specific model providers, leaving developers using open-weight models without a comparable tool. Qwen-code provides the same category of agentic coding capability — codebase understanding, file editing, git operations — but backed by a model that can be run locally or accessed through Alibaba Cloud's API.

**Why another one?** The key differentiator is the tight integration with the Qwen model family, including locally hosted variants, which allows developers in regions or organizations that cannot use Anthropic or OpenAI APIs to access a comparable coding agent experience. It also serves as a reference implementation for Qwen's function-calling and tool-use capabilities, making it useful for developers building on top of those models.

---

## 39. [stremio-web](https://github.com/Stremio/stremio-web)
> Stremio - Freedom to Stream

**Language:** JavaScript  |  **Stars:** 9274  |  **Forks:** 1035  |  **Best Score:** 1966  |  **Best Rank:** #9  |  **Days on chart:** 1/7  |  **Created:** 2018-06-04

**Background:** Stremio is a media center application that aggregates content from multiple streaming services and torrent sources into a unified interface. The stremio-web repository is the web-based frontend of the Stremio platform, built in JavaScript and first released in June 2018. The project has accumulated over 9,000 stars and supports an extensive add-on ecosystem for content discovery.

**Problem it solves:** Users with subscriptions to multiple streaming services must switch between different apps to find and watch content, with no unified search or library view. Stremio aggregates catalogs from multiple sources into a single interface where users can search, discover, and stream content regardless of the source.

**Why another one?** Stremio keeps trending because its add-on architecture allows the community to extend content sources without changes to the core application. Unlike Plex or Jellyfin which focus on locally-hosted media libraries, Stremio is designed for aggregating external streaming sources. The web client enables access from any device with a browser without requiring native app installation.

---

## 40. [evershop](https://github.com/evershopcommerce/evershop)
> Typescript E-commerce Platform

**Language:** TypeScript  |  **Stars:** 9479  |  **Forks:** 2145  |  **Best Score:** 1964  |  **Best Rank:** #12  |  **Days on chart:** 1/7  |  **Created:** 2021-05-06

**Background:** EverShop is an open-source e-commerce platform built entirely in TypeScript, launched in May 2021. It provides a complete online store solution with product management, order processing, and a modular extension system. The platform uses a GraphQL API and is designed for both developers who want to customize and merchants who need a production-ready storefront.

**Problem it solves:** Most open-source e-commerce platforms (WooCommerce, Magento, PrestaShop) are built on PHP, which creates friction for JavaScript/TypeScript-focused development teams. EverShop provides a full e-commerce stack in TypeScript, eliminating the need to context-switch between languages and enabling teams to share code and tooling across their frontend and backend.

**Why another one?** The TypeScript-native approach is the primary differentiator against established PHP-based platforms, while the modular extension architecture differentiates it from newer Node.js alternatives like Medusa or Saleor that may require more custom development. EverShop targets the middle ground of being opinionated enough to deploy quickly while remaining extensible through its module system.

---

## 41. [pyrite64](https://github.com/HailToDodongo/pyrite64)
> N64 Game-Engine and Editor using libdragon & tiny3d

**Language:** C++  |  **Stars:** 2221  |  **Forks:** 86  |  **Best Score:** 1961  |  **Best Rank:** #15  |  **Days on chart:** 2/7  |  **Created:** 2025-09-23

**Background:** pyrite64 is a Nintendo 64 game engine and accompanying editor built on top of the libdragon open-source N64 SDK and the tiny3d rendering library. Written in C++, it provides a structured engine layer above the raw SDK, including scene management, asset pipeline tooling, and an interactive editor for assembling game content. The project targets hobbyist N64 homebrew developers who want a higher-level framework than bare libdragon.

**Problem it solves:** Developing for the N64 with libdragon alone requires writing significant boilerplate for scene management, asset loading, and rendering pipelines. pyrite64 abstracts this into a reusable engine, reducing the setup time for new homebrew projects and allowing developers to focus on game logic rather than hardware-level plumbing.

**Why another one?** The N64 homebrew scene has seen renewed interest following libdragon's maturation and the release of tiny3d as a practical 3D rendering library. pyrite64 is the first editor-equipped engine built on these modern foundations, filling a gap that exists between raw SDK usage and full game development.

---

## 42. [claude-quickstarts](https://github.com/anthropics/claude-quickstarts)
> A collection of projects to help developers get started with the Claude API

**Language:** Python  |  **Stars:** 14715  |  **Forks:** 2455  |  **Best Score:** 1950  |  **Best Rank:** #13  |  **Days on chart:** 3/7  |  **Created:** 2024-08-29

**Background:** Claude Quickstarts is Anthropic's official repository of starter projects for developers building production applications on the Claude API. Each quickstart covers a specific use case — RAG pipelines, tool use, multi-turn agents, document analysis — with complete, runnable Python code and deployment guidance. The repository is maintained by Anthropic and updated alongside new API capabilities.

**Problem it solves:** Developers evaluating the Claude API often struggle to move from documentation to a working, deployable prototype quickly. The quickstarts provide complete end-to-end examples that demonstrate best practices for context management, error handling, and production deployment patterns. This reduces the time from API key to working application from days to hours.

**Why another one?** As Anthropic releases new Claude models and API features, the quickstarts repository is updated to showcase them, generating recurring trending events. Each new capability announcement drives developers back to the repository to find canonical usage examples.

---

## 43. [wifi-densepose](https://github.com/ruvnet/wifi-densepose)
> WiFi-based dense human pose estimation system for real-time full-body tracking through walls

**Language:** Python  |  **Stars:** 7201  |  **Forks:** 609  |  **Best Score:** 1931  |  **Best Rank:** #13  |  **Days on chart:** 2/7  |  **Created:** 2025-06-07

**Background:** WiFi-DensePose is a Python implementation of InvisPose, a system for estimating dense human body pose using WiFi signal perturbations rather than cameras. It processes channel state information (CSI) from commodity mesh routers to track full-body movement through walls and in low-light environments. The project is described as production-ready and ships with preprocessing, inference, and visualization pipelines.

**Problem it solves:** Camera-based human pose estimation requires line of sight, adequate lighting, and raises significant privacy concerns. WiFi-based tracking works through walls, in darkness, and without any visible sensor — enabling applications in fall detection, smart home automation, and security monitoring where camera placement is impractical or unacceptable.

**Why another one?** Research implementations of WiFi pose estimation have historically been inaccessible — requiring custom hardware or proprietary CSI extraction tools. This project targets commodity mesh routers and emphasizes production readiness, making the technology approachable for developers and researchers without specialized RF hardware backgrounds.

---

## 44. [gogcli](https://github.com/steipete/gogcli)
> Google Suite CLI: Gmail, GCal, GDrive, GContacts.

**Language:** Go  |  **Stars:** 4410  |  **Forks:** 344  |  **Best Score:** 1926  |  **Best Rank:** #14  |  **Days on chart:** 2/7  |  **Created:** 2025-12-12

**Background:** GoGCLI is a command-line interface for the Google Workspace suite — Gmail, Google Calendar, Google Drive, and Google Contacts — written in Go by Peter Steinberger (steipete). It provides terminal-first access to Google services for developers and power users who prefer keyboard-driven workflows or need to script interactions with their Google accounts. The project launched in December 2025 and has reached over 4,400 stars.

**Problem it solves:** Google's web applications require a browser and offer no native scripting interface, making automation of common tasks — archiving emails, creating calendar events in bulk, querying contacts — unnecessarily difficult. GoGCLI exposes these services via a consistent CLI, enabling shell scripting, cron-based automation, and integration with other terminal tools.

**Why another one?** Existing Google API clients are language-specific SDKs that require writing code rather than issuing commands. GoGCLI fills the direct CLI gap with a single compiled binary that covers the four most-used Workspace services, making it immediately useful without any boilerplate.

---

## 45. [KittenTTS](https://github.com/KittenML/KittenTTS)
> State-of-the-art TTS model under 25MB

**Language:** Python  |  **Stars:** 10384  |  **Forks:** 559  |  **Best Score:** 1895  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2025-08-05

**Background:** KittenTTS is an open-source text-to-speech model family from KittenML (operating under Stellon Labs) designed for extreme lightweight deployment. The flagship nano model has 15 million parameters, and its int8-quantized variant fits in 25MB, making it deployable on any CPU without a GPU. The project offers four model tiers — mini (80M), micro (40M), nano (15M), and nano-int8 — with a demo on Hugging Face Spaces.

**Problem it solves:** Most high-quality open-source TTS models require several gigabytes of weights and GPU inference to achieve acceptable latency. KittenTTS targets the opposite constraint: devices where storage, memory, or compute are limited, such as IoT hardware, mobile devices, or edge servers.

**Why another one?** The model family fills a gap between toy TTS systems (intelligible but robotic) and full-scale models like XTTS or Kokoro (high quality but large). KittenTTS claims state-of-the-art quality at the sub-25MB size tier and provides multiple premium voice options rather than a single default speaker.

---

## 46. [agent-zero](https://github.com/agent0ai/agent-zero)
> Agent Zero AI framework

**Language:** Python  |  **Stars:** 14953  |  **Forks:** 3105  |  **Best Score:** 1892  |  **Best Rank:** #15  |  **Days on chart:** 1/7  |  **Created:** 2024-06-10

**Background:** Agent Zero is a Python-based AI agent framework by agent0ai that provides a general-purpose scaffolding for building autonomous agents capable of using tools, spawning sub-agents, and maintaining memory across tasks. Launched in June 2024, it has grown to nearly 15,000 stars and nearly 3,100 forks, reflecting heavy community use and customization. It supports multiple underlying models and exposes a flexible tool-use and communication layer for agent orchestration.

**Problem it solves:** Building capable AI agents from scratch requires implementing tool execution, memory management, sub-agent delegation, and error recovery from the ground up. Agent Zero provides these primitives as a composable framework, allowing developers to focus on defining what their agent should do rather than how it should manage its own execution.

**Why another one?** Agent Zero distinguishes itself by its emphasis on transparency and hackability — the framework is intentionally minimal and readable, making it easier to understand and modify than heavier alternatives like AutoGen or CrewAI. Its recurring presence on trending lists reflects continued community interest in lightweight, extensible agent frameworks.

---

## 47. [awesome](https://github.com/sindresorhus/awesome)
> Awesome lists about all kinds of interesting topics

**Language:** N/A  |  **Stars:** 439784  |  **Forks:** 33277  |  **Best Score:** 1867  |  **Best Rank:** #13  |  **Days on chart:** 1/7  |  **Created:** 2014-07-11

**Background:** Sindre Sorhus's awesome repository is the root meta-list that spawned the entire "awesome list" convention on GitHub, created in July 2014. It is a curated index of other curated lists covering programming languages, frameworks, platforms, developer tools, theory, media, and more. With nearly 439,000 stars it is one of the most starred repositories on GitHub.

**Problem it solves:** Before the awesome list pattern existed, there was no consistent convention for community-maintained topic indexes on GitHub. The repository established both the format and the badge/quality standard that thousands of downstream awesome lists now follow, making it the canonical entry point for discovering curated resources on any technical topic.

**Why another one?** This repository trends periodically because it is the authoritative meta-index — every new awesome list that gains traction links back to it, and every developer who discovers the pattern for the first time stars the original. Its age (over 11 years) and star count make it effectively an infrastructure piece of GitHub's knowledge graph rather than a project competing with alternatives.

---

## 48. [FineTune](https://github.com/ronitsingh10/FineTune)
> FineTune, a macOS menu bar app for per-app volume control, multi-device output, audio routing, and 10-band EQ.

**Language:** Swift  |  **Stars:** 2785  |  **Forks:** 93  |  **Best Score:** 1863  |  **Best Rank:** #14  |  **Days on chart:** 1/7  |  **Created:** 2026-01-18

**Background:** FineTune is a free, open-source macOS menu bar application written in Swift that provides per-application volume control, multi-device audio output, audio routing, and a 10-band equalizer. It positions itself as a free alternative to Rogue Amoeba's SoundSource, which is a paid commercial application. The project launched in January 2026 and has quickly gained nearly 2,800 stars.

**Problem it solves:** macOS provides only system-wide volume control by default, with no built-in way to set different volume levels for individual applications or route specific apps to different audio output devices. SoundSource solves this but costs money. FineTune provides the same per-app audio control capabilities at no cost.

**Why another one?** The primary appeal is being a free and open-source alternative to a well-known paid tool. SoundSource costs $39 and is closed-source; FineTune provides comparable functionality — per-app volume, multi-device output, audio routing, and equalization — without a license fee. The menu bar integration follows the same UX pattern macOS users expect from audio utilities.

---

## 49. [Mole](https://github.com/tw93/Mole)
> Deep clean and optimize your Mac.

**Language:** Shell  |  **Stars:** 35825  |  **Forks:** 971  |  **Best Score:** 1829  |  **Best Rank:** #12  |  **Days on chart:** 1/7  |  **Created:** 2025-09-23

**Background:** Mole is a macOS system cleaning and optimization tool created by tw93, written in Shell and released in September 2025. It performs deep cleaning of caches, logs, temporary files, and other accumulated system debris that slows down macOS over time. The project has grown to over 35,000 stars.

**Problem it solves:** macOS accumulates significant disk space usage from application caches, system logs, Xcode derived data, Homebrew caches, and other temporary files that are not automatically cleaned. Commercial tools like CleanMyMac charge subscription fees for this functionality. Mole provides the same deep cleaning capability as a free, open-source shell script that users can audit.

**Why another one?** Being a transparent shell script rather than a compiled binary is the key trust differentiator — users can read exactly what will be deleted before running it. This addresses the trust problem inherent in system cleaning tools that request broad filesystem access. The open-source approach also means the community can add cleanup targets for new applications without waiting for a vendor update.

---

## 50. [posthog](https://github.com/PostHog/posthog)
> PostHog is an all-in-one developer platform for building successful products.

**Language:** Python  |  **Stars:** 31713  |  **Forks:** 2317  |  **Best Score:** 1828  |  **Best Rank:** #13  |  **Days on chart:** 1/7  |  **Created:** 2020-01-23

**Background:** PostHog is an open-source, all-in-one product analytics platform that bundles product analytics, web analytics, session replay, error tracking, feature flags, experimentation, surveys, a data warehouse, a CDP, and an AI product assistant into a single self-hostable product. Founded in January 2020, it has grown to over 31,000 stars and serves as a self-hosted alternative to the combination of Amplitude, Mixpanel, LaunchDarkly, and Hotjar.

**Problem it solves:** Product teams typically stitch together multiple SaaS tools for analytics, session replay, feature flags, and experimentation, creating data silos and increasing vendor costs. PostHog consolidates these capabilities into one platform with a unified data model, reducing integration complexity and ensuring all product data lives in one place.

**Why another one?** PostHog keeps trending because it continues to expand its product surface — adding error tracking, a data warehouse, and an AI assistant on top of its original analytics core. The self-hosting option appeals to companies with data sovereignty requirements, and the open-source model allows the community to contribute integrations. Each new capability announcement drives renewed visibility.

---

## 51. [opencode](https://github.com/anomalyco/opencode)
> The open source coding agent.

**Language:** TypeScript  |  **Stars:** 107795  |  **Forks:** 10640  |  **Best Score:** 1782  |  **Best Rank:** #14  |  **Days on chart:** 1/7  |  **Created:** 2025-04-30

**Background:** OpenCode is an open-source terminal-based coding agent developed by Anomaly, launched in April 2025. It provides an agentic coding assistant that operates in the terminal, understands codebases, and executes development tasks through natural language commands. With over 107,000 stars, it is one of the most popular open-source coding agents on GitHub.

**Problem it solves:** Developers need AI coding assistance that integrates into their existing terminal workflow without being locked into a specific IDE or vendor. OpenCode provides a fully open-source alternative to proprietary coding agents, giving users the freedom to inspect, modify, and self-host the entire system while retaining terminal-native convenience.

**Why another one?** OpenCode keeps trending because it occupies the open-source counterpart position to proprietary coding agents. Its fully open codebase allows the community to add model backends, customize behaviors, and build extensions without vendor approval. The 107,000-star milestone reflects the demand for a transparent, community-driven coding agent.

---

## 52. [nautilus_trader](https://github.com/nautechsystems/nautilus_trader)
> A high-performance algorithmic trading platform and event-driven backtester

**Language:** Rust  |  **Stars:** 20083  |  **Forks:** 2356  |  **Best Score:** 1749  |  **Best Rank:** #14  |  **Days on chart:** 2/7  |  **Created:** 2018-06-25

**Background:** Nautilus Trader is a high-performance algorithmic trading platform and event-driven backtester developed by Nautech Systems, with its performance-critical components implemented in Rust and its user-facing API exposed through Python. It has been in development since June 2018 and has grown to over 20,000 stars, making it one of the most mature open-source algorithmic trading frameworks available. It supports live trading across multiple venues as well as historical backtesting with microsecond-resolution event replay.

**Problem it solves:** Backtesting trading strategies accurately requires event-driven simulation that faithfully reproduces the order of market events, including partial fills, latency, and market impact. Most open-source backtesting frameworks use vectorized computation that approximates this behavior. Nautilus Trader's event-driven architecture provides higher-fidelity simulation that reduces the gap between backtest and live performance.

**Why another one?** Nautilus Trader's Rust core gives it performance characteristics — microsecond event processing, low GC pressure — that pure-Python alternatives cannot match. Its longevity (active since 2018) and steady feature additions mean it keeps accumulating attention from professional quantitative developers who need production-grade tooling rather than research prototypes.

---

## 53. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> The awesome collection of OpenClaw Skills.

**Language:** N/A  |  **Stars:** 17555  |  **Forks:** 1799  |  **Best Score:** 1739  |  **Best Rank:** #16  |  **Days on chart:** 6/7  |  **Created:** 2026-01-25

**Background:** Awesome OpenClaw Skills is a curated collection of community-built skills for the OpenClaw AI assistant platform, maintained by VoltAgent. The project has undergone two rebrands — originally Clawdbot, then Moltbot — before settling on its current name to align with the OpenClaw ecosystem. It launched in late January 2026 and has accumulated over 17,500 stars, reflecting the rapid growth of the OpenClaw community.

**Problem it solves:** OpenClaw is a powerful personal assistant platform, but building custom skills requires knowledge of its plugin API and prompt engineering conventions. This collection provides ready-made, community-tested skills that users can install directly, lowering the barrier to extending OpenClaw with new capabilities without writing skills from scratch.

**Why another one?** The project's lineage — Clawdbot to Moltbot to its current form — reflects its evolution alongside the OpenClaw platform itself. As OpenClaw has grown to become one of the most-starred personal assistant platforms, the demand for a canonical skills repository has grown with it, keeping this collection prominently visible in trending lists.

---

## 54. [FossFLOW](https://github.com/stan-smith/FossFLOW)
> Make beautiful isometric infrastructure diagrams

**Language:** TypeScript  |  **Stars:** 17565  |  **Forks:** 1147  |  **Best Score:** 1726  |  **Best Rank:** #15  |  **Days on chart:** 1/7  |  **Created:** 2025-06-30

**Background:** FossFLOW is an open-source tool for creating isometric infrastructure diagrams, built in TypeScript. It provides a visual interface for generating polished, three-dimensional architecture diagrams commonly used in cloud infrastructure documentation, DevOps presentations, and system design discussions. The project has grown to over 17,500 stars since its June 2025 launch.

**Problem it solves:** Creating professional isometric infrastructure diagrams typically requires either expensive design software (Figma, Illustrator) with manual drawing skills or proprietary diagramming tools with limited export options. FossFLOW automates the isometric rendering, letting users focus on describing their infrastructure rather than drawing it.

**Why another one?** While tools like draw.io and Excalidraw support general diagramming, they do not specialize in isometric infrastructure views. FossFLOW's narrow focus on isometric rendering produces more visually polished output for this specific use case than general-purpose diagramming tools, and being open-source differentiates it from commercial alternatives like Cloudcraft.

---

## 55. [freemocap](https://github.com/freemocap/freemocap)
> Free Motion Capture for Everyone

**Language:** Python  |  **Stars:** 5617  |  **Forks:** 444  |  **Best Score:** 1721  |  **Best Rank:** #15  |  **Days on chart:** 2/7  |  **Created:** 2021-04-12

**Background:** FreeMoCap is an open-source markerless motion capture system that uses standard webcams and computer vision to record 3D skeletal motion data without specialized hardware. Built in Python, it uses MediaPipe for pose estimation and Anipose for multi-camera 3D triangulation, outputting data in formats compatible with Blender, Unity, and biomechanics analysis tools. The project targets researchers, educators, and indie animators who cannot afford commercial mocap systems.

**Problem it solves:** Professional motion capture requires either marker-based suits with infrared camera arrays costing tens of thousands of dollars or high-end markerless systems that are similarly expensive. FreeMoCap enables accurate full-body motion capture using consumer webcams arranged in a multi-camera setup, bringing the capability within reach of university labs, independent game developers, and clinical researchers working with limited budgets.

**Why another one?** Commercial markerless mocap systems such as Theia3D and Vicon Shogun are priced for film production budgets. FreeMoCap is the most complete open-source alternative, with active development, documented calibration workflows, and direct Blender integration that makes it immediately usable for animation. It trends recurrently as new users in the animation and biomechanics communities discover that it produces usable results with hardware they already own.

---

## 56. [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
> Master programming by recreating your favorite technologies from scratch.

**Language:** Markdown  |  **Stars:** 467978  |  **Forks:** 43866  |  **Best Score:** 1675  |  **Best Rank:** #16  |  **Days on chart:** 2/7  |  **Created:** 2018-05-09

**Background:** Build Your Own X is one of the most-starred repositories on GitHub, curating tutorials for reimplementing well-known technologies — databases, compilers, operating systems, web servers — from scratch in various languages. The collection is organized by technology category and links to high-quality external tutorials. It is maintained by Codecrafters as both a community resource and a companion to their paid interactive courses.

**Problem it solves:** Developers who want deep understanding of how fundamental technologies work struggle to find structured, high-quality learning resources beyond textbooks. This repository provides a single entry point to hands-on reimplementation tutorials that build genuine internals knowledge. The "build it to understand it" philosophy produces more durable learning than reading documentation alone.

**Why another one?** At nearly 468,000 stars, this repository trends persistently because new developers continuously discover it and because new tutorials are added as technology evolves. It is a perennial recommendation in programming learning communities worldwide.

---

## 57. [awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
> A community collection of OpenClaw use cases for making life easier.

**Language:** N/A  |  **Stars:** 4893  |  **Forks:** 353  |  **Best Score:** 1656  |  **Best Rank:** #17  |  **Days on chart:** 1/7  |  **Created:** 2026-02-08

**Background:** Awesome OpenClaw Usecases is a community-curated collection of practical use cases for the OpenClaw personal AI assistant, assembled by Hesam Sheikh and launched in early February 2026. It documents real-world applications people have built using OpenClaw's skills and multi-channel architecture, organized by category. The repository has rapidly accumulated nearly 5,000 stars in just two weeks.

**Problem it solves:** OpenClaw has over 5,700 skills in its ClawHub registry, but discovering which combinations of skills solve specific real-world problems requires experimentation. This collection provides documented, tested use cases that show how to combine OpenClaw capabilities for practical tasks, reducing the trial-and-error discovery process.

**Why another one?** While awesome-openclaw-skills catalogs individual skills with security vetting, this repository focuses on complete use-case recipes that combine multiple skills into workflows. The distinction is between a tool catalog (skills) and a cookbook (use cases), serving users who know what they want to accomplish but not which tools to combine.

---

## 58. [opencti](https://github.com/OpenCTI-Platform/opencti)
> Open Cyber Threat Intelligence Platform

**Language:** TypeScript  |  **Stars:** 8848  |  **Forks:** 1258  |  **Best Score:** 1641  |  **Best Rank:** #16  |  **Days on chart:** 2/7  |  **Created:** 2018-12-17

**Background:** OpenCTI is an open-source cyber threat intelligence platform developed by Filigran, originally launched in December 2018. It provides a structured environment for ingesting, storing, correlating, and sharing threat intelligence using the STIX 2.1 standard. The platform includes a graph-based knowledge base, connector ecosystem for integrating with external threat feeds, and role-based access control for multi-team use.

**Problem it solves:** Security teams that consume threat intelligence from multiple sources face the challenge of correlating indicators across feeds, maintaining a structured knowledge graph of threat actors and TTPs, and sharing findings with partners in a standardized format. OpenCTI provides a single platform for all of these functions without requiring a commercial TIP subscription.

**Why another one?** OpenCTI has established itself as the leading open-source threat intelligence platform and trends periodically as new connectors are released and as organizations standardize on STIX-based intelligence workflows. Its active Filigran-backed development and broad connector ecosystem make it difficult to displace with a newer alternative.

---

## 59. [pinchtab](https://github.com/pinchtab/pinchtab)
> High-performance browser automation bridge and multi-instance orchestrator

**Language:** Go  |  **Stars:** 1086  |  **Forks:** 53  |  **Best Score:** 1592  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2026-02-15

**Background:** Pinchtab is a very recently released Go-based browser automation bridge designed to orchestrate multiple browser instances simultaneously with advanced stealth capabilities to avoid bot detection. It provides a real-time dashboard for monitoring automation sessions and exposes an API for programmatic control of browser fleets. The project was created on February 15, 2026 and has already attracted over 1,000 stars within days of release.

**Problem it solves:** Playwright and Puppeteer are the dominant browser automation tools but are frequently detected and blocked by anti-bot systems because they modify browser fingerprints in predictable ways. Pinchtab focuses specifically on stealth injection — manipulating browser internals to defeat fingerprinting detection — and adds a multi-instance orchestration layer that these libraries lack natively, making it suited for large-scale automation tasks.

**Why another one?** The Go implementation provides significantly lower resource overhead per browser instance compared to Node.js-based orchestrators, which matters when managing dozens of simultaneous browser sessions. The integrated real-time dashboard also fills a gap in existing tools, which typically require third-party monitoring to observe automation sessions at scale. Its extreme recency and high score indicate rapid organic discovery.

---

## 60. [claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
> Official, Anthropic-managed directory of high quality Claude Code Plugins.

**Language:** Python  |  **Stars:** 7985  |  **Forks:** 781  |  **Best Score:** 1588  |  **Best Rank:** #16  |  **Days on chart:** 1/7  |  **Created:** 2025-11-20

**Background:** Claude Plugins Official is Anthropic's curated directory of high-quality Claude Code plugins, launched in November 2025. It serves as the official, vetted collection of plugins that extend Claude Code's capabilities, with each plugin reviewed and maintained to Anthropic's quality and security standards. The repository has accumulated nearly 8,000 stars.

**Problem it solves:** The growing ecosystem of community-built Claude Code plugins varies widely in quality, security, and maintenance. This official directory provides a trusted source where users can find plugins that have been reviewed by Anthropic, reducing the risk of installing poorly maintained or potentially malicious extensions.

**Why another one?** As the official Anthropic-managed directory, it provides a level of trust and quality assurance that community-maintained lists cannot guarantee. Each plugin undergoes security review and is tested for compatibility with current Claude Code versions, addressing the same trust gap that official app stores address for mobile platforms.

---

## 61. [SparkyFitness](https://github.com/CodeWithCJ/SparkyFitness)
> SparkyFitness: Built for Families. Powered by AI. Track food, fitness, water, and health — together.

**Language:** TypeScript  |  **Stars:** 2447  |  **Forks:** 114  |  **Best Score:** 1534  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2025-06-21

**Background:** SparkyFitness is an AI-powered family health tracking application built in TypeScript. It provides collaborative tracking for food intake, fitness activities, water consumption, and general health metrics, designed for family use rather than individual users. The application uses AI to assist with meal logging, nutritional analysis, and fitness recommendations.

**Problem it solves:** Most health and fitness tracking apps are designed for individual use and lack shared family features. Families trying to improve their health together must each use separate apps with no shared visibility. SparkyFitness provides a unified platform where family members can track and view each other's health data collaboratively.

**Why another one?** The family-first design is the primary differentiator against established apps like MyFitnessPal, Cronometer, or Apple Health, which are all individual-centric. The AI-powered food logging and nutritional analysis lower the barrier for less tech-savvy family members, and the open-source nature allows self-hosting for families who want full control over their health data.

---

## 62. [moonshine](https://github.com/moonshine-ai/moonshine)
> Fast and accurate automatic speech recognition (ASR) for edge devices

**Language:** C  |  **Stars:** 4265  |  **Forks:** 212  |  **Best Score:** 1527  |  **Best Rank:** #17  |  **Days on chart:** 1/7  |  **Created:** 2024-10-04

**Background:** Moonshine is a C-implemented automatic speech recognition engine from Moonshine AI, optimized specifically for edge devices with constrained compute budgets. It is designed to run on hardware such as Raspberry Pi, microcontrollers, and embedded Linux boards while delivering accuracy competitive with much heavier models. The project launched in October 2024 and has grown to over 4,200 stars.

**Problem it solves:** Cloud ASR services introduce latency, require network connectivity, and raise privacy concerns by transmitting audio off-device. Running models like Whisper on edge hardware is feasible but slow without careful optimization. Moonshine delivers fast, accurate transcription locally on devices where running a full neural network is otherwise impractical.

**Why another one?** Moonshine's C implementation — rather than Python with native extensions — means it can be compiled and deployed on targets that lack a Python runtime. This makes it genuinely usable on bare-metal embedded systems where competing edge ASR projects cannot run at all.

---

## 63. [tambo](https://github.com/tambo-ai/tambo)
> Generative UI SDK for React

**Language:** TypeScript  |  **Stars:** 10829  |  **Forks:** 525  |  **Best Score:** 1517  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2024-06-15

**Background:** Tambo is a TypeScript SDK by tambo-ai that enables generative UI patterns within React applications, allowing AI models to dynamically compose and render UI components based on natural language or structured model outputs. It launched in June 2024 and has grown to over 10,000 stars by providing a practical bridge between language model outputs and React component trees.

**Problem it solves:** Displaying AI-generated content in React applications typically requires manually parsing model output and mapping it to components — a fragile and bespoke process. Tambo provides a structured SDK that handles the component selection and rendering logic, allowing developers to declare what components are available and let the model decide how to compose them based on context.

**Why another one?** Generative UI is an emerging pattern without a dominant open-source solution. Tambo targets React specifically — the most widely used UI framework — and provides a production-oriented SDK rather than a research prototype, which gives it practical appeal for product teams wanting to ship AI-driven interfaces without building the integration layer themselves.

---

## 64. [apkstudio](https://github.com/vaibhavpandeyvpz/apkstudio)
> Open-source, cross platform Qt6 based IDE for reverse-engineering Android application packages.

**Language:** C++  |  **Stars:** 3722  |  **Forks:** 619  |  **Best Score:** 1517  |  **Best Rank:** #16  |  **Days on chart:** 1/7  |  **Created:** 2014-09-09

**Background:** APKStudio is a cross-platform C++ IDE built on Qt6 that provides a graphical interface for decompiling, inspecting, modifying, and recompiling Android APK packages. It wraps command-line tools like apktool and jadx into a cohesive desktop application. The project has been under continuous development since 2014, accumulating a stable user base among mobile security researchers and developers.

**Problem it solves:** Android reverse engineering traditionally requires chaining multiple command-line tools with complex flags and manual file management. APKStudio consolidates the workflow into a single GUI application with project management, syntax highlighting, and integrated build controls. This significantly lowers the barrier for security analysts and developers who need to inspect or patch APKs.

**Why another one?** The Qt6 migration and continued maintenance have kept APKStudio competitive with newer tools. Its trending reflects periodic rediscovery by mobile security practitioners who prefer a native desktop GUI over web-based or terminal-only alternatives.

---

## 65. [get-shit-done](https://github.com/gsd-build/get-shit-done)
> A meta-prompting, context engineering and spec-driven development system for Claude Code and OpenCode.

**Language:** JavaScript  |  **Stars:** 17523  |  **Forks:** 1588  |  **Best Score:** 1432  |  **Best Rank:** #19  |  **Days on chart:** 2/7  |  **Created:** 2025-12-14

**Background:** Get-Shit-Done (GSD) is a JavaScript-based meta-prompting and context engineering system for Claude Code and OpenCode, built around spec-driven development principles. It provides a structured workflow where developers write specs first, then use GSD's prompt templates and context management to guide AI coding agents through implementation. The project launched in December 2025 and rapidly accumulated over 17,000 stars.

**Problem it solves:** AI coding agents with no structured input tend to interpret requirements loosely and produce implementations that drift from the original intent. GSD enforces a spec-first workflow with carefully engineered context and meta-prompts that constrain the agent's behavior, increasing the reliability of outputs for complex multi-step development tasks.

**Why another one?** GSD's focus on context engineering — the craft of structuring what information the model sees and when — distinguishes it from skill frameworks that focus on tool-calling. Its lightweight JavaScript implementation makes it easy to drop into existing Claude Code or OpenCode setups without a heavy dependency footprint.

---

## 66. [nanobot](https://github.com/HKUDS/nanobot)
> nanobot: The Ultra-Lightweight OpenClaw

**Language:** Python  |  **Stars:** 22520  |  **Forks:** 3492  |  **Best Score:** 1430  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2026-02-01

**Background:** nanobot is an ultra-lightweight Python implementation of the OpenClaw AI assistant framework, developed by HKUDS. It strips the OpenClaw feature set down to its minimal viable core, targeting environments where the full OpenClaw stack is too heavy to deploy. The project launched in early February 2026 and quickly gained traction among edge AI and resource-constrained deployment communities.

**Problem it solves:** The full OpenClaw runtime has dependencies and resource requirements that make it impractical for embedded systems, minimal Docker containers, and serverless functions. nanobot implements the essential OpenClaw interfaces in pure Python with minimal dependencies, enabling skill compatibility without the full stack overhead. This makes OpenClaw skills portable to environments previously excluded from the ecosystem.

**Why another one?** As OpenClaw has grown in features and complexity, a lightweight compatibility shim has become increasingly valuable for the long tail of constrained deployments. nanobot fills that niche while maintaining skill API compatibility, avoiding the need to rewrite skills for different runtimes.

---

## 67. [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)
> the best agent harness

**Language:** TypeScript  |  **Stars:** 32679  |  **Forks:** 2466  |  **Best Score:** 1430  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2025-12-03

**Background:** Oh My OpenCode is a community-driven configuration and plugin framework for the OpenCode coding agent, built in TypeScript by code-yeongyu. Similar in concept to oh-my-zsh for the Zsh shell, it provides a curated collection of themes, plugins, and configurations that enhance the OpenCode experience. The project launched in December 2025 and has grown to over 32,000 stars.

**Problem it solves:** OpenCode's default configuration provides a baseline experience, but customizing it requires manually sourcing and configuring plugins, themes, and settings from scattered community repositories. Oh My OpenCode bundles these into a single installable framework with a plugin manager, making customization a one-command operation.

**Why another one?** The oh-my-* pattern (proven by oh-my-zsh with 180,000+ stars) has demonstrated that configuration frameworks for popular tools attract massive adoption. Oh My OpenCode applies this proven model to the second most-starred coding agent, providing the same convenience of curated defaults and easy plugin discovery that made oh-my-zsh successful.

---

## 68. [readest](https://github.com/readest/readest)
> Readest is a modern, feature-rich ebook reader designed for avid readers.

**Language:** TypeScript  |  **Stars:** 17791  |  **Forks:** 960  |  **Best Score:** 1424  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2024-10-12

**Background:** Readest is a cross-platform ebook reader built in TypeScript, launched in October 2024. It supports major ebook formats and provides features such as annotations, highlights, customizable reading themes, and cross-device synchronization. The application is designed for avid readers who want a modern, polished reading experience across desktop and mobile platforms.

**Problem it solves:** Existing open-source ebook readers like Calibre prioritize library management over reading experience, while commercial options like Kindle lock users into a single ecosystem. Readest focuses on the reading experience itself — typography, annotation tools, and cross-platform sync — without vendor lock-in or format restrictions.

**Why another one?** Readest differentiates by prioritizing the reading UX over library management. While Calibre is the standard for ebook management and conversion, its reader interface is dated. Readest inverts the priority, offering a modern reading experience with an intuitive interface while remaining open-source and cross-platform.

---

## 69. [skills](https://github.com/huggingface/skills)
> Hugging Face Skills

**Language:** Python  |  **Stars:** 1872  |  **Forks:** 153  |  **Best Score:** 1417  |  **Best Rank:** #22  |  **Days on chart:** 1/7  |  **Created:** 2025-11-24

**Background:** Hugging Face Skills is an official repository from Hugging Face providing a collection of reusable AI agent skills in Python. Launched alongside the broader agent skills ecosystem in November 2025, it provides building blocks for constructing AI agent workflows using Hugging Face's model and dataset ecosystem. The repository has grown to nearly 1,900 stars.

**Problem it solves:** Building AI agent capabilities from scratch requires significant boilerplate — model loading, inference pipelines, tool definitions, and error handling. This repository provides pre-built, tested skill implementations that can be composed into agent workflows, reducing the time from concept to working agent.

**Why another one?** As an official Hugging Face project, these skills are designed to integrate natively with the Hugging Face ecosystem — models, datasets, Spaces, and inference endpoints. This tight integration differentiates them from framework-agnostic skill collections that require additional glue code to connect to Hugging Face resources.

---

## 70. [AstrBot](https://github.com/AstrBotDevs/AstrBot)
> Agentic IM Chatbot infrastructure that integrates IM platforms, LLMs, plugins and AI features.

**Language:** Python  |  **Stars:** 17341  |  **Forks:** 1332  |  **Best Score:** 1393  |  **Best Rank:** #20  |  **Days on chart:** 1/7  |  **Created:** 2022-12-08

**Background:** AstrBot is a Python-based agentic chatbot infrastructure platform created in December 2022 that connects multiple instant messaging platforms — including QQ, WeChat, Telegram, and Discord — to a variety of LLM backends through a unified plugin architecture. It supports local models via Ollama as well as cloud APIs and ships with features including multi-model routing, image generation, and voice interaction. The project has over 17,000 stars across more than three years of development.

**Problem it solves:** Developers building AI chatbots for Chinese IM platforms like QQ and WeChat face a fragmented landscape: each platform has its own API, authentication system, and message format. AstrBot provides a unified abstraction layer so that skills and plugins written once work across all supported platforms without modification. It also handles the LLM routing and session management that every bot needs but that each team otherwise reimplements from scratch.

**Why another one?** AstrBot's primary differentiator in a crowded chatbot framework space is its specific focus on Chinese IM platforms alongside international ones, filling a gap left by frameworks that prioritize Telegram and Discord. Its long maintenance history also means it has accumulated a mature plugin ecosystem and robust documentation that newer projects cannot match. It trends when new LLM releases prompt users to connect fresh models to their existing bot deployments.

---

## 71. [llm-checker](https://github.com/Pavelevich/llm-checker)
> Advanced CLI tool that scans your hardware and tells you which LLM models you can run locally.

**Language:** JavaScript  |  **Stars:** 906  |  **Forks:** 62  |  **Best Score:** 1325  |  **Best Rank:** #21  |  **Days on chart:** 1/7  |  **Created:** 2025-07-06

**Background:** llm-checker is a CLI tool by Pavelevich that inspects a machine's hardware — GPU VRAM, system RAM, and CPU capabilities — and produces a ranked list of LLM models the machine can run locally. It integrates with Ollama to provide direct download links for compatible models and shows estimated inference speed and memory headroom for each option. The tool launched in July 2025 and targets users new to local LLM deployment.

**Problem it solves:** Users new to running LLMs locally often download models that exceed their hardware's capabilities, resulting in out-of-memory errors or unusably slow inference. llm-checker removes the guesswork by automatically reading hardware specifications and mapping them to a curated model compatibility database before the user commits to a download.

**Why another one?** While Ollama itself lists available models, it does not filter or rank them based on the user's actual hardware. llm-checker fills this gap with hardware-aware filtering and direct Ollama integration, making the model selection step accessible to users who do not know how to calculate VRAM requirements manually.

---

## 72. [qmd](https://github.com/tobi/qmd)
> mini cli search engine for your docs, knowledge bases, meeting notes. All local.

**Language:** TypeScript  |  **Stars:** 9753  |  **Forks:** 531  |  **Best Score:** 1310  |  **Best Rank:** #22  |  **Days on chart:** 1/7  |  **Created:** 2025-12-08

**Background:** qmd is a lightweight command-line search engine for local document collections — markdown files, knowledge bases, and meeting notes — written in TypeScript by Tobi. It builds a local index of document content and provides fast full-text and semantic search without any cloud dependency or running server process. The tool is designed to be invoked on the command line and integrated into terminal workflows.

**Problem it solves:** Personal knowledge bases and document collections grow large enough that grep-based search becomes slow and misses semantic relationships between documents. Cloud-based tools like Notion search and Google Drive require uploading documents to external servers. qmd provides fast local search with semantic understanding while keeping all data on the user's machine.

**Why another one?** qmd occupies the gap between full-featured local RAG systems that require significant setup and simple grep-based search. Its single-command invocation, zero-server architecture, and TypeScript implementation make it easy to install and use without configuring a vector database or embedding server.

---

## 73. [hyperbrowser-app-examples](https://github.com/hyperbrowserai/hyperbrowser-app-examples)
> Fully functional Hyperbrowser powered web apps

**Language:** TypeScript  |  **Stars:** 583  |  **Forks:** 89  |  **Best Score:** 1306  |  **Best Rank:** #21  |  **Days on chart:** 1/7  |  **Created:** 2025-05-28

**Background:** This repository contains a collection of fully functional example web applications built using Hyperbrowser, an AI-powered browser automation platform. Created by the Hyperbrowser AI team in May 2025, it provides reference implementations for common web automation tasks and serves as both documentation and starter templates for new Hyperbrowser users.

**Problem it solves:** Browser automation platforms have steep learning curves, and official documentation often lacks complete, end-to-end examples. This repository provides working applications that demonstrate real-world use cases, reducing the time from initial interest to a functional application by providing copy-and-modify starting points.

**Why another one?** Unlike documentation snippets that show isolated API calls, these are complete, deployable applications that handle edge cases, error states, and production concerns. Each example demonstrates a full user-facing workflow rather than just the automation layer, making them directly usable as starting points for production applications.

---

## 74. [llmfit](https://github.com/AlexsJones/llmfit)
> 157 models. 30 providers. One command to find what runs on your hardware.

**Language:** Rust  |  **Stars:** 1337  |  **Forks:** 79  |  **Best Score:** 1293  |  **Best Rank:** #23  |  **Days on chart:** 2/7  |  **Created:** 2026-02-15

**Background:** llmfit is a Rust CLI tool by AlexsJones that inventories a machine's hardware and cross-references it against a database of 157 models from 30 providers to determine which models are compatible with the available resources. Created just three days before this report date, its rapid star accumulation reflects immediate demand for hardware-aware model selection tooling. The Rust implementation produces a fast, dependency-free binary.

**Problem it solves:** As the number of locally-runnable LLM models has exploded across providers including Ollama, LM Studio, and llama.cpp, determining which specific model variant fits a given machine's GPU and RAM configuration has become increasingly time-consuming. llmfit automates this cross-reference with a comprehensive, up-to-date model database covering multiple providers simultaneously.

**Why another one?** Compared to llm-checker (also on this list), llmfit's differentiator is its breadth — 30 providers and 157 models — and its Rust implementation, which produces a smaller, faster binary with no Node.js dependency. The two tools address the same problem with different scope and implementation tradeoffs.

---

## 75. [agents](https://github.com/cloudflare/agents)
> Build and deploy AI Agents on Cloudflare

**Language:** TypeScript  |  **Stars:** 3278  |  **Forks:** 381  |  **Best Score:** 1292  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2025-01-29

**Background:** Cloudflare Agents is an official TypeScript framework from Cloudflare for building and deploying AI agents on Cloudflare's edge network. It leverages Durable Objects for stateful agent sessions, Workers for serverless execution, and integrates with Cloudflare's AI Gateway for model routing. The framework launched in January 2025 and provides templates and examples for common agent patterns.

**Problem it solves:** Deploying AI agents typically requires managing server infrastructure, handling WebSocket connections for real-time interaction, and implementing state persistence — all of which add complexity and cost. Cloudflare Agents abstracts these concerns into the Cloudflare platform, providing globally distributed, stateful agent execution with minimal infrastructure management.

**Why another one?** The edge deployment model is the differentiator: agents run on Cloudflare's global network rather than in a single region, reducing latency for users worldwide. The integration with Durable Objects provides built-in state persistence without an external database, and the Workers runtime offers automatic scaling. For teams already on Cloudflare, it eliminates the need to set up separate agent infrastructure.

---

## 76. [n8n-workflows](https://github.com/Zie619/n8n-workflows)
> all of the workflows of n8n i could find (also from the site itself)

**Language:** Python  |  **Stars:** 51740  |  **Forks:** 6551  |  **Best Score:** 1277  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2025-05-14

**Background:** This repository is a comprehensive collection of n8n workflow templates assembled by Zie619, aggregating workflows from the official n8n site and community sources. N8n is an open-source workflow automation platform similar to Zapier, and this repository serves as an unofficial but extensive library of pre-built automations. It has accumulated over 51,000 stars since May 2025.

**Problem it solves:** Building n8n workflows from scratch requires understanding the platform's node system and experimenting with connections between services. This collection provides ready-made workflow templates that users can import directly, covering common automation patterns and reducing the learning curve for new n8n users.

**Why another one?** While n8n has an official template library, this repository aggregates workflows from multiple community sources into a single searchable collection. The unofficial curation includes workflows the official library may not feature, and the GitHub-based format makes it easier to browse, fork, and adapt workflows than the official web-based template browser.

---

## 77. [gemini-voyager](https://github.com/Nagi-ovo/gemini-voyager)
> An all-in-one enhancement suite for Google Gemini & AI Studio

**Language:** TypeScript  |  **Stars:** 7252  |  **Forks:** 230  |  **Best Score:** 1275  |  **Best Rank:** #22  |  **Days on chart:** 1/7  |  **Created:** 2025-10-04

**Background:** Gemini Voyager is a TypeScript browser extension and enhancement suite created by Nagi-ovo that augments Google Gemini and AI Studio with additional features not provided natively by Google. It launched in October 2025 and has grown to over 7,200 stars by addressing quality-of-life gaps in the official Gemini interface. The extension targets power users who rely on Gemini or AI Studio for daily work.

**Problem it solves:** Google's official Gemini and AI Studio interfaces lack productivity features that regular users expect — conversation management, export options, keyboard shortcuts, and customizable UI elements. Gemini Voyager layers these enhancements on top of the existing interface without requiring API key changes or alternative frontends.

**Why another one?** Rather than building a new AI frontend, Gemini Voyager enhances the existing Google interface that users are already logged into, preserving session state and billing context. This positions it as a complement to the official product rather than a replacement, making it less risky to adopt than a fully alternative frontend.

---

## 78. [timesfm](https://github.com/google-research/timesfm)
> TimesFM (Time Series Foundation Model) by Google Research for time-series forecasting.

**Language:** Python  |  **Stars:** 8851  |  **Forks:** 732  |  **Best Score:** 1262  |  **Best Rank:** #23  |  **Days on chart:** 2/7  |  **Created:** 2024-04-29

**Background:** TimesFM is a pretrained time-series foundation model released by Google Research in April 2024 that performs zero-shot forecasting across a wide range of time-series domains without requiring task-specific fine-tuning. It was trained on a large corpus of real-world time series data and is available as a Python library with JAX and PyTorch backends. The model targets practitioners who need accurate forecasting without the cost of training or fine-tuning a domain-specific model.

**Problem it solves:** Traditional time-series forecasting requires either statistical models that must be tuned per-series or deep learning models that require substantial training data and compute for each new domain. TimesFM enables zero-shot forecasting — accurate predictions on new time-series without any fine-tuning — by transferring patterns learned from its broad pretraining corpus to novel domains at inference time.

**Why another one?** TimesFM's Google Research provenance and demonstrated zero-shot accuracy set it apart from earlier neural forecasting libraries like NeuralForecast or PyTorch Forecasting, which still require training. It trends periodically as new practitioners discover that a foundation model approach can outperform their existing per-series statistical models without any training pipeline. The growing interest in AI-native data infrastructure also drives recurrent traffic to the repository.

---

## 79. [PaperKnife](https://github.com/potatameister/PaperKnife)
> Privacy-first PDF utility (Zero-Server Architecture). Merge, split, compress, and edit PDFs 100% locally.

**Language:** TypeScript  |  **Stars:** 553  |  **Forks:** 28  |  **Best Score:** 1251  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2026-01-26

**Background:** PaperKnife is a browser-based PDF utility built with a zero-server architecture, meaning all PDF processing — merging, splitting, compression, and editing — happens entirely in the browser using WebAssembly without any file ever being uploaded to a server. Written in TypeScript, it was launched in January 2026 by potatameister and targets users who need PDF manipulation tools but are unwilling to send sensitive documents to cloud services.

**Problem it solves:** Popular online PDF tools such as ilovepdf and Smallpdf process documents on their servers, raising privacy concerns for documents containing sensitive personal, legal, or financial information. PaperKnife provides the same functionality entirely client-side, ensuring that document contents never leave the user's device.

**Why another one?** While PDF.js and similar libraries enable client-side PDF rendering, building a full-featured utility on top of them requires significant engineering. PaperKnife packages this into a polished, ready-to-use application that non-technical users can access without installation, occupying a space between complex desktop applications and privacy-invasive web tools.

---

## 80. [LobsterBoard](https://github.com/Curbob/LobsterBoard)
> OpenClaw Dashboard Builder - Create custom dashboards

**Language:** JavaScript  |  **Stars:** 498  |  **Forks:** 64  |  **Best Score:** 1245  |  **Best Rank:** #23  |  **Days on chart:** 1/7  |  **Created:** 2026-02-06

**Background:** LobsterBoard is a JavaScript application for building custom dashboards on top of the OpenClaw AI assistant platform. It provides a drag-and-drop interface for composing skill outputs, data visualizations, and status widgets into persistent dashboard views. The project launched in early February 2026 as part of the broader OpenClaw ecosystem expansion.

**Problem it solves:** OpenClaw skill outputs are ephemeral — they appear in chat and disappear with the conversation. LobsterBoard provides persistent, composable views of skill data, making it practical to monitor ongoing automations, track metrics, and surface recurring information without re-invoking skills manually. This transforms OpenClaw from a conversational tool into a persistent information workspace.

**Why another one?** No prior OpenClaw tool addressed the persistence and composability gap for recurring information needs. LobsterBoard is novel within the ecosystem rather than a duplicate of existing functionality, explaining its rapid early traction despite a small absolute star count.

---

## 81. [n8n](https://github.com/n8n-io/n8n)
> Fair-code workflow automation platform with native AI capabilities.

**Language:** TypeScript  |  **Stars:** 175786  |  **Forks:** 55068  |  **Best Score:** 1225  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2019-06-22

**Background:** n8n is a fair-code licensed workflow automation platform founded in 2019 that allows users to build automated pipelines by connecting hundreds of pre-built integrations through a visual node editor. It can be self-hosted or used via n8n Cloud and has added native AI node types that allow LLM calls, vector store interactions, and agent orchestration to be integrated directly into automation workflows. With over 175,000 stars and 55,000 forks it is among the most widely adopted open-source automation platforms.

**Problem it solves:** Business automation typically requires choosing between powerful but expensive SaaS platforms like Zapier or Make, or writing custom integration code that is difficult to maintain. n8n provides a self-hostable alternative with a visual workflow editor that supports complex branching logic, data transformation, and now AI-native steps, without the per-operation pricing of cloud automation services.

**Why another one?** n8n keeps trending because its star count places it on GitHub's visible trending surface at very low daily velocity, and each new AI node or integration release generates fresh press coverage that drives new users. Its fair-code license also attracts users who want Zapier-like automation without subscription costs. The integration of native AI capabilities has made it newly relevant to users building agentic workflows who want a no-code orchestration layer.

---

## 82. [electrobun](https://github.com/blackboardsh/electrobun)
> Build ultra fast, tiny, and cross-platform desktop apps with Typescript.

**Language:** C++  |  **Stars:** 6274  |  **Forks:** 115  |  **Best Score:** 1196  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2024-02-28

**Background:** Electrobun is a desktop application framework from Blackboard.sh that uses Bun to run the main process and bundle webview TypeScript, with native bindings written in Zig. It aims to produce self-extracting app bundles around 12MB (using the system webview) and app updates as small as 14KB via bsdiff binary patching between versions. It targets the same niche as Electron but with a dramatically different architecture, offering typed RPC between main and webview processes.

**Problem it solves:** Electron apps are large — shipping a full Chromium runtime per app means bundles of 100–200MB and high memory usage at runtime. Electrobun sidesteps this by using the OS-provided webview and Bun instead of Node.js, producing much smaller distributions and faster startup times.

**Why another one?** The differentiating angle against Tauri is the choice of Bun plus Zig over Rust, and the first-class TypeScript RPC layer between processes. Electrobun's update mechanism — binary patching rather than full downloads — is also distinct. The framework gained renewed attention because one of its showcase apps (Audio TTS) is built on Qwen3-TTS, linking it to the TTS trend elsewhere on this list.

---

## 83. [notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli)
> NotebookLM MCP CLI tool

**Language:** Python  |  **Stars:** 1500  |  **Forks:** 319  |  **Best Score:** 1186  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2025-12-23

**Background:** NotebookLM MCP CLI is a Python command-line tool by jacob-bd that exposes Google NotebookLM's functionality through the Model Context Protocol (MCP), enabling AI agents to interact with NotebookLM notebooks programmatically. It launched in December 2025 and has accumulated 1,500 stars, primarily from developers building MCP-compatible agent workflows. The tool bridges the gap between the NotebookLM interface and the broader MCP ecosystem.

**Problem it solves:** Google NotebookLM has no official API, making it inaccessible to automated workflows and AI agents that need to query or manage notebooks programmatically. This tool wraps NotebookLM's underlying interface with an MCP-compatible CLI, allowing agents that speak MCP to treat NotebookLM as a tool they can invoke directly.

**Why another one?** The MCP ecosystem is growing rapidly as a standard protocol for agent-tool communication, and NotebookLM is a widely used research tool with no official programmatic interface. This project fills a specific integration gap — NotebookLM as an MCP tool — that no official or competing project currently addresses.

---

## 84. [midday](https://github.com/midday-ai/midday)
> Invoicing, Time tracking, File reconciliation, Storage, Financial Overview & your own Assistant made for Freelancers

**Language:** TypeScript  |  **Stars:** 14034  |  **Forks:** 1349  |  **Best Score:** 1184  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2023-09-18

**Background:** Midday is an open-source business management platform built by midday-ai and targeted specifically at freelancers and independent contractors. It bundles invoicing, time tracking, file reconciliation, financial overviews, and an embedded AI assistant into a single TypeScript application. Launched in September 2023, it has grown to over 14,000 stars by addressing the fragmented tooling that freelancers typically assemble from multiple paid services.

**Problem it solves:** Freelancers typically use separate tools for invoicing, time tracking, document storage, and financial reporting — each with its own subscription cost and data silo. Midday consolidates these functions into a single self-hostable platform with an AI assistant that can answer questions about earnings, outstanding invoices, and time allocations directly from the unified data.

**Why another one?** Midday's differentiation is its freelancer-specific focus combined with an AI assistant that has access to all financial and time-tracking data in the platform. General-purpose accounting tools are not designed for project-based income patterns, and freelancer-focused SaaS products are expensive. Midday offers a self-hosted alternative with a purpose-built data model for freelance business management.

---

> **Week's theme:** AI agents, agentic coding tools, and autonomous infrastructure dominated the chart, with OpenClaw ecosystem projects and terminal-based AI assistants leading the trend.
