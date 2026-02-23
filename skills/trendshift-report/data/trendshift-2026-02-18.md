# Trendshift Report — 2026-02-18
**Total:** 25 repositories

---

## 1. [cs-video-courses](https://github.com/Developer-Y/cs-video-courses)
> List of Computer Science courses with video lectures.

**Language:** N/A  |  **Stars:** 74,570  |  **Forks:** 9,957  |  **Score:** 10,548  |  **Created:** 2016-10-21

**Background:** cs-video-courses is a community-maintained curated list of free Computer Science courses that include video lectures, organized by subject area — algorithms, operating systems, machine learning, distributed systems, and more. Started by Developer-Y in October 2016, it has grown into one of the largest single-file references for self-directed CS education on GitHub. The list links directly to lecture series hosted on YouTube, Coursera, MIT OpenCourseWare, and similar platforms.

**Problem it solves:** High-quality CS lecture content is scattered across dozens of university websites, YouTube channels, and MOOC platforms with inconsistent tagging and discoverability. This repository consolidates them into a single, browsable index organized by topic, saving learners the time of hunting down what is actually available for free.

**Why another one?** cs-video-courses recurrently trends because it is the most comprehensive single-repository index of its kind and is continuously updated by community pull requests as new courses appear. Its staying power comes from the fact that it covers the full CS curriculum rather than a single subject, making it relevant to learners at any stage.

---

## 2. [voicebox](https://github.com/jamiepine/voicebox)
> The open-source voice synthesis studio powered by Qwen3-TTS.

**Language:** TypeScript  |  **Stars:** 9,955  |  **Forks:** 1,040  |  **Score:** 4,412  |  **Created:** 2026-01-25

**Background:** Voicebox is a local-first voice cloning and speech synthesis desktop application created by Jamie Pine, built with Tauri for native performance. It features a DAW-like multi-track timeline editor for composing multi-voice audio projects and runs entirely on the user's machine using the open-source Qwen3-TTS model. On Apple Silicon it leverages an MLX backend with Metal acceleration for faster inference than CPU-only alternatives.

**Problem it solves:** Commercial voice synthesis platforms charge subscription fees, store voice data on remote servers, and impose rate limits. Voicebox removes all three constraints: voice models and profiles stay local, there is no per-character billing, and generation is rate-unlimited. Most open-source TTS tools expose only a CLI or Gradio demo; Voicebox wraps inference in a professional multi-track editor targeting content creators.

**Why another one?** The key differentiator is the studio-grade editing interface layered on top of an open-source model, a combination that did not previously exist in the open-source ecosystem. Launched in late January 2026, it is still early enough in its trajectory that each wave of social media attention brings a fresh surge of stars and contributors.

---

## 3. [openclaw](https://github.com/openclaw/openclaw)
> Your own personal AI assistant. Any OS. Any Platform. The lobster way.

**Language:** TypeScript  |  **Stars:** 215,287  |  **Forks:** 40,386  |  **Score:** 4,257  |  **Created:** 2025-11-24

**Background:** OpenClaw is a cross-platform personal AI assistant that launched in November 2025 and rapidly became one of the most-starred repositories on GitHub. It runs on any operating system, integrates with multiple AI providers, and supports an extensible skills system for customizing and extending its behavior. The "lobster way" branding reflects its community-driven, open development philosophy.

**Problem it solves:** Most AI assistant applications are either cloud-only, locked to a single operating system, or tied to a specific model provider. OpenClaw provides a unified assistant runtime that works across OS and provider boundaries, letting users switch models and platforms without relearning a new tool or losing their configuration and history.

**Why another one?** With over 215,000 stars, OpenClaw keeps trending because it has established itself as the de facto open-source alternative to commercial AI assistant products. Its growing ecosystem of community-contributed skills and integrations, along with frequent releases, generates ongoing activity that consistently surfaces it in trending rankings.

---

## 4. [OpenViking](https://github.com/volcengine/OpenViking)
> OpenViking is an open-source context database designed specifically for AI Agents. Unifies context management through a file system paradigm.

**Language:** Python  |  **Stars:** 3,160  |  **Forks:** 231  |  **Score:** 4,150  |  **Created:** 2026-01-05

**Background:** OpenViking is an open-source context database developed by Volcengine, ByteDance's cloud infrastructure division. It is designed specifically for AI agent workflows, treating agent memory, tool outputs, and intermediate reasoning artifacts as a unified file system rather than a heterogeneous collection of data stores. The project launched in January 2026 and targets production agent deployments that require durable and queryable context across sessions.

**Problem it solves:** AI agents today typically manage context through a mix of in-context text, vector stores, and key-value caches, each with separate APIs and consistency guarantees. OpenViking unifies these under a single file-system abstraction, allowing agents to read and write context using familiar path-based operations regardless of the underlying storage backend.

**Why another one?** Existing context management solutions such as mem0 and Zep are either embedded libraries or hosted services. OpenViking is a standalone, self-hostable database with a file-system interface, filling a gap for teams that need persistent agent context without cloud vendor lock-in. Its Volcengine backing provides production-grade engineering resources behind the project.

---

## 5. [heretic](https://github.com/p-e-w/heretic)
> Fully automatic censorship removal for language models

**Language:** Python  |  **Stars:** 8,887  |  **Forks:** 884  |  **Score:** 3,481  |  **Created:** 2025-09-21

**Background:** Heretic is a Python tool by p-e-w that automates the removal of refusal and safety filtering behaviors from open-source language models. It works by identifying and modifying the specific weights responsible for refusal behavior rather than requiring fine-tuning on new data. The project has attracted significant attention in the open-source ML community since its September 2025 launch.

**Problem it solves:** Users running locally-hosted open-source models often encounter safety filters that refuse to engage with legitimate technical, creative, or research prompts. Fine-tuning away these restrictions requires labeled datasets, GPU time, and ML expertise. Heretic automates the process without a fine-tuning step, making uncensored model variants accessible to users without ML training infrastructure.

**Why another one?** Heretic's distinguishing characteristic is that it operates directly on model weights rather than relying on system prompt injection, jailbreaks, or fine-tuning. This makes its modifications persistent and immune to prompt-level countermeasures. It continues to trend as new base models are released and users seek uncensored variants without waiting for community fine-tunes.

---

## 6. [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)
> The Ultimate Collection of 800+ Agentic Skills for Claude Code/Antigravity/Cursor.

**Language:** Python  |  **Stars:** 13,791  |  **Forks:** 2,590  |  **Score:** 3,473  |  **Created:** 2026-01-14

**Background:** antigravity-awesome-skills is a community-curated repository of over 800 reusable agentic skills compatible with Claude Code, Antigravity, and Cursor. Skills are structured prompt templates and tool definitions that extend what a coding agent can do within a session, covering areas such as code review, documentation generation, refactoring, and testing. The repository launched in January 2026 and has grown rapidly as skill authoring tooling has matured.

**Problem it solves:** Writing effective agent skills from scratch requires understanding the prompt formats and tool schemas expected by each agent runtime, which is non-obvious and time-consuming. This repository provides a ready-made library of tested, community-reviewed skills that users can drop into their agent configuration without writing a single line of prompt engineering.

**Why another one?** With Claude Code's skills system and similar mechanisms in Cursor gaining mainstream adoption, demand for a centralized skill library has grown significantly. The repository fills the same role that awesome-lists have historically filled for libraries: a single authoritative index that the community rallies around rather than fragmenting across individual author repositories.

---

## 7. [pentagi](https://github.com/vxcontrol/pentagi)
> Fully autonomous AI Agents system capable of performing complex penetration testing tasks

**Language:** Go  |  **Stars:** 4,228  |  **Forks:** 588  |  **Score:** 3,372  |  **Created:** 2025-01-06

**Background:** PentAGI is a self-hosted autonomous agent system for penetration testing, built in Go by vxcontrol. It bundles over 20 professional security tools — including nmap, Metasploit, and sqlmap — inside isolated Docker containers and uses a multi-agent architecture where a lead agent delegates to specialized sub-agents for research, development, and infrastructure tasks. A Neo4j-backed knowledge graph provides long-term memory across testing sessions.

**Problem it solves:** Security testing requires orchestrating dozens of tools in sequence, interpreting intermediate outputs, and adapting attack paths based on findings — a process that demands deep expertise and significant time. PentAGI automates this orchestration layer, allowing the system to autonomously chain tools together and produce detailed vulnerability reports with exploitation guidance.

**Why another one?** PentAGI is fully self-hosted and open-source, distinguishing it from commercial AI-assisted security platforms. Its architecture includes a full REST and GraphQL API, Grafana/Prometheus monitoring integration, and a bundled scraper container for browser-based OSINT — a level of completeness uncommon in open-source security tooling.

---

## 8. [vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands)
> VSCode theme based off the easemate IDE and Jetbrains islands theme

**Language:** PowerShell  |  **Stars:** 3,740  |  **Forks:** 108  |  **Score:** 3,212  |  **Created:** 2026-02-14

**Background:** vscode-dark-islands is a Visual Studio Code color theme created by bwya77, drawing aesthetic inspiration from the Easemate IDE and JetBrains' Islands theme family. It was created just four days before this report date, in February 2026, making its score notable for such a new project. The theme targets developers who prefer the visual style of JetBrains IDEs but work primarily in VS Code.

**Problem it solves:** JetBrains' Islands theme is not officially available for VS Code, leaving users who switch between IDEs without a consistent visual environment. vscode-dark-islands ports that aesthetic to VS Code, reducing visual context-switching for developers who use both editors or who prefer that particular color palette.

**Why another one?** The VS Code theme ecosystem is large, but faithful ports of specific IDE themes have their own dedicated audiences. This theme's rapid star accumulation within days of launch suggests a pent-up demand from the JetBrains user community for an official-feeling VS Code equivalent of the Islands aesthetic.

---

## 9. [polymarket-kalshi-arbitrage-bot](https://github.com/ryan26craf/polymarket-kalshi-arbitrage-bot)
> Kalshi open source trading bot to automate copy trading and arbitrage strategies on crypto prediction markets

**Language:** Python  |  **Stars:** 738  |  **Forks:** 2  |  **Score:** 3,154  |  **Created:** 2026-02-06

**Background:** This is an open-source Python bot for automating arbitrage and copy trading strategies across Polymarket and Kalshi, two regulated prediction market platforms. It was published in February 2026 and targets traders looking to exploit price discrepancies between the same event contracts listed on different platforms. The codebase interfaces with both platforms' APIs to monitor prices and execute trades programmatically.

**Problem it solves:** Prediction market arbitrage requires monitoring multiple platforms simultaneously, calculating spread opportunities in real time, and executing trades faster than is practical manually. This bot automates the detection and execution of cross-platform arbitrage opportunities, lowering the technical barrier for traders who understand the strategy but cannot implement it from scratch.

**Why another one?** Polymarket and Kalshi have both gained significant user bases following increased regulatory clarity around prediction markets. The combination of two specific, widely-used platforms in a single bot is novel, and the open-source nature allows traders to audit and modify the strategy logic — something impossible with proprietary trading bots.

---

## 10. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 56,468  |  **Forks:** 4,282  |  **Score:** 3,090  |  **Created:** 2025-10-09

**Background:** Superpowers is a composable skills framework and structured software development methodology created by Jesse Vincent (obra). It installs into coding agents such as Claude Code, Cursor, Codex, and OpenCode via their plugin systems, enforcing a multi-stage workflow: brainstorm and refine a spec, produce a detailed implementation plan, then execute through subagent-driven development with two-stage code review. The project has accumulated over 56,000 stars since October 2025.

**Problem it solves:** Coding agents left to default settings tend to skip planning, ignore test-driven development, and drift from the original intent mid-session. Superpowers installs guard rails — mandatory spec approval, red-green-refactor TDD enforcement, and plan checkpoints — so an agent can work autonomously for extended periods without derailing from what was agreed upon.

**Why another one?** Rather than being a new coding agent, Superpowers is a methodology layer that works across multiple agents via their plugin systems. The portability across Claude Code, Cursor, Codex, and OpenCode, combined with an emphasis on subagent delegation rather than a single long-running context, keeps it trending as each new wave of coding agent adopters discovers it.

---

## 11. [cs249r_book](https://github.com/harvard-edge/cs249r_book)
> Introduction to Machine Learning Systems

**Language:** JavaScript  |  **Stars:** 20,499  |  **Forks:** 2,359  |  **Score:** 2,416  |  **Created:** 2023-09-06

**Background:** cs249r_book is the open-source textbook for Harvard's CS249r course, "Tiny Machine Learning," developed by the Harvard Edge Computing Lab. The book covers the full stack of ML systems from model design and hardware constraints to deployment on edge devices and embedded systems. It is authored collaboratively on GitHub using Quarto and rendered as a web book, allowing community contributions via pull requests.

**Problem it solves:** Most ML educational resources focus on model accuracy and training techniques without addressing the systems-level concerns that arise when deploying models on constrained hardware. This textbook bridges that gap by covering quantization, hardware-software co-design, inference optimization, and real-world deployment considerations in a structured academic format.

**Why another one?** The book trends recurrently because it is one of the few openly licensed, university-quality textbooks covering ML systems end-to-end rather than just ML theory. As edge AI deployment becomes more mainstream, interest in practical systems knowledge has grown, and this remains the most comprehensive free resource in the space.

---

## 12. [hummingbot](https://github.com/hummingbot/hummingbot)
> Open source software that helps you create and deploy high-frequency crypto trading bots

**Language:** Python  |  **Stars:** 17,391  |  **Forks:** 4,464  |  **Score:** 2,337  |  **Created:** 2019-04-02

**Background:** Hummingbot is an open-source Python framework for building and running algorithmic cryptocurrency trading bots, originally developed by the Hummingbot Foundation. It supports dozens of centralized and decentralized exchange connectors and includes pre-built market-making, arbitrage, and directional trading strategies. The project has been in active development since 2019 and has a large community of strategy developers and liquidity providers.

**Problem it solves:** Building a production-grade crypto trading bot from scratch requires implementing exchange API connectors, order management, risk controls, and execution logic for each venue individually — a months-long engineering effort. Hummingbot provides all of these components as a reusable framework, letting users focus on strategy logic rather than infrastructure.

**Why another one?** Hummingbot's longevity and the breadth of its exchange connector library — covering both centralized and decentralized venues — make it difficult to replace with a newer alternative. It trends periodically as crypto market activity increases, drawing in new traders who want an open-source alternative to expensive proprietary trading platforms.

---

## 13. [claude-quickstarts](https://github.com/anthropics/claude-quickstarts)
> A collection of projects to help developers quickly get started with the Claude API

**Language:** Python  |  **Stars:** 14,715  |  **Forks:** 2,455  |  **Score:** 1,950  |  **Created:** 2024-08-29

**Background:** claude-quickstarts is Anthropic's official repository of starter projects and example applications demonstrating how to use the Claude API. Launched in August 2024, it covers common integration patterns including chat interfaces, tool use, computer use, and multi-turn conversation management. Each quickstart is self-contained and intended to be a working starting point rather than a minimal toy example.

**Problem it solves:** API documentation alone is often insufficient for developers starting a new integration — they need runnable examples that demonstrate how to combine multiple API features into a coherent application pattern. claude-quickstarts provides these working examples, shortening the time from API key acquisition to a functioning prototype.

**Why another one?** As Anthropic's first-party example repository, claude-quickstarts trends whenever Claude API features are updated or a new capability is announced. Developers looking for official guidance naturally start here rather than third-party tutorials, keeping it consistently visible in trending lists.

---

## 14. [zvec](https://github.com/alibaba/zvec)
> A lightweight, lightning-fast, in-process vector database

**Language:** C++  |  **Stars:** 5,951  |  **Forks:** 330  |  **Score:** 1,908  |  **Created:** 2025-12-05

**Background:** zvec is a lightweight in-process vector database developed by Alibaba, written in C++ for minimal overhead. It is designed to be embedded directly into application processes rather than run as a separate service, enabling high-throughput vector search without network round-trips or serialization costs. The project launched in December 2025 as Alibaba's open-source contribution to the embedded AI infrastructure space.

**Problem it solves:** Running a separate vector database service introduces latency, operational complexity, and infrastructure cost that is excessive for applications with moderate dataset sizes. zvec embeds vector indexing and search directly in the application process, making it suitable for single-machine deployments, edge devices, and applications where simplicity of deployment matters more than distributed scale.

**Why another one?** While Chroma and Qdrant have established themselves as the dominant open-source vector databases, both are designed as external services. zvec occupies the embedded-database niche, more comparable to SQLite than to PostgreSQL, targeting a deployment model that neither Chroma nor Qdrant optimizes for.

---

## 15. [picoclaw](https://github.com/sipeed/picoclaw)
> Tiny, Fast, and Deployable anywhere — automate the mundane, unleash your creativity

**Language:** Go  |  **Stars:** 17,835  |  **Forks:** 2,110  |  **Score:** 1,788  |  **Created:** 2026-02-04

**Background:** picoclaw is a lightweight automation and agent runtime developed by Sipeed, written in Go for minimal resource consumption and fast startup. It is designed to be deployable on constrained hardware including microcontrollers and single-board computers, extending the AI assistant and automation space to devices that cannot run heavier runtimes. The project was created in February 2026 and has grown rapidly given its focus on embedded and edge deployment.

**Problem it solves:** Most AI agent frameworks assume a general-purpose computer with several gigabytes of RAM and a network connection to a cloud API. picoclaw targets the opposite end of the deployment spectrum, enabling automation workflows to run on resource-constrained devices entirely locally or with minimal cloud dependency.

**Why another one?** Sipeed's background in RISC-V hardware and embedded systems gives picoclaw credibility in the constrained-device space that general-purpose agent frameworks lack. Its Go implementation produces small static binaries with no runtime dependencies, which is a concrete technical advantage for edge deployment scenarios.

---

## 16. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> The awesome collection of OpenClaw Skills.

**Language:** N/A  |  **Stars:** 17,555  |  **Forks:** 1,799  |  **Score:** 1,739  |  **Created:** 2026-01-25

**Background:** awesome-openclaw-skills is a community-curated index of skills, plugins, and extensions for the OpenClaw AI assistant platform, maintained by VoltAgent. It follows the established awesome-list format, organizing community contributions by category — productivity, coding, research, and creative tasks among others. The repository launched the same day as several other OpenClaw ecosystem projects, suggesting a coordinated community launch.

**Problem it solves:** As OpenClaw's skill ecosystem grows, discovering high-quality, community-vetted skills becomes harder without a central index. awesome-openclaw-skills provides the community reference point for finding, comparing, and contributing skills, reducing the effort required to extend OpenClaw beyond its defaults.

**Why another one?** The awesome-list format has proven effective at becoming the canonical reference for ecosystems ranging from Kubernetes add-ons to VS Code extensions. With OpenClaw occupying the top spot in terms of stars among AI assistant projects, its skills ecosystem was large enough by January 2026 to justify a dedicated curated list.

---

## 17. [fluxer](https://github.com/fluxerapp/fluxer)
> A free and open source instant messaging and VoIP platform.

**Language:** TypeScript  |  **Stars:** 4,321  |  **Forks:** 172  |  **Score:** 1,719  |  **Created:** 2026-01-01

**Background:** Fluxer is a free and open-source instant messaging and VoIP platform built in TypeScript, launched on January 1, 2026. It provides text messaging, voice calls, and video communication in a self-hostable package, positioning itself as a privacy-respecting alternative to commercial communication platforms. The project targets communities and organizations that want full control over their communication infrastructure.

**Problem it solves:** Popular communication platforms such as Discord and Slack are closed-source, store message data on third-party servers, and can change pricing or terms of service without notice. Fluxer allows organizations to host their own instance, keeping communication data under their own control with no external service dependency.

**Why another one?** While Matrix/Element and Rocket.Chat address similar needs, Fluxer aims for a simpler deployment experience and a more modern TypeScript codebase that is easier for contributors to work with. Its January 2026 launch timed well with growing organizational interest in communication sovereignty following policy changes at major platforms.

---

## 18. [RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques)
> Showcases various advanced techniques for Retrieval-Augmented Generation (RAG) systems.

**Language:** Jupyter Notebook  |  **Stars:** 25,501  |  **Forks:** 2,991  |  **Score:** 1,696  |  **Created:** 2024-07-13

**Background:** RAG_Techniques is a comprehensive Jupyter Notebook collection by Nir Diamant demonstrating advanced retrieval-augmented generation techniques beyond basic vector search. It covers approaches such as hybrid retrieval, re-ranking, multi-query expansion, contextual compression, and agentic RAG patterns. The repository has grown to over 25,000 stars since its launch in July 2024 and is regularly updated with new techniques.

**Problem it solves:** Basic RAG implementations using a single embedding model and cosine similarity often produce poor retrieval quality for complex queries. The techniques in this repository address specific failure modes — query ambiguity, semantic drift, context overflow, and relevance degradation — with concrete, runnable notebook implementations rather than theoretical descriptions.

**Why another one?** RAG_Techniques trends recurrently because it is the most comprehensive open-source collection of practical RAG patterns with working code. As new retrieval techniques are published in research papers, Diamant adds notebook implementations, keeping the repository current and making it a first stop for ML engineers building production RAG systems.

---

## 19. [pyrite64](https://github.com/HailToDodongo/pyrite64)
> N64 Game-Engine and Editor using libdragon & tiny3d

**Language:** C++  |  **Stars:** 2,221  |  **Forks:** 86  |  **Score:** 1,682  |  **Created:** 2025-09-23

**Background:** pyrite64 is a Nintendo 64 game engine and accompanying editor built on top of the libdragon open-source N64 SDK and the tiny3d rendering library. Written in C++, it provides a structured engine layer above the raw SDK, including scene management, asset pipeline tooling, and an interactive editor for assembling game content. The project targets hobbyist N64 homebrew developers who want a higher-level framework than bare libdragon.

**Problem it solves:** Developing for the N64 with libdragon alone requires writing significant boilerplate for scene management, asset loading, and rendering pipelines. pyrite64 abstracts this into a reusable engine, reducing the setup time for new homebrew projects and allowing developers to focus on game logic rather than hardware-level plumbing.

**Why another one?** The N64 homebrew scene has seen renewed interest following libdragon's maturation and the release of tiny3d as a practical 3D rendering library. pyrite64 is the first editor-equipped engine built on these modern foundations, filling a gap that exists between raw SDK usage and full game development.

---

## 20. [opencti](https://github.com/OpenCTI-Platform/opencti)
> Open Cyber Threat Intelligence Platform

**Language:** TypeScript  |  **Stars:** 8,848  |  **Forks:** 1,258  |  **Score:** 1,346  |  **Created:** 2018-12-17

**Background:** OpenCTI is an open-source cyber threat intelligence platform developed by Filigran, originally launched in December 2018. It provides a structured environment for ingesting, storing, correlating, and sharing threat intelligence using the STIX 2.1 standard. The platform includes a graph-based knowledge base, connector ecosystem for integrating with external threat feeds, and role-based access control for multi-team use.

**Problem it solves:** Security teams that consume threat intelligence from multiple sources face the challenge of correlating indicators across feeds, maintaining a structured knowledge graph of threat actors and TTPs, and sharing findings with partners in a standardized format. OpenCTI provides a single platform for all of these functions without requiring a commercial TIP subscription.

**Why another one?** OpenCTI has established itself as the leading open-source threat intelligence platform and trends periodically as new connectors are released and as organizations standardize on STIX-based intelligence workflows. Its active Filigran-backed development and broad connector ecosystem make it difficult to displace with a newer alternative.

---

## 21. [llm-checker](https://github.com/Pavelevich/llm-checker)
> Advanced CLI tool that scans your hardware and tells you exactly which LLM models you can run locally, with full Ollama integration.

**Language:** JavaScript  |  **Stars:** 906  |  **Forks:** 62  |  **Score:** 1,325  |  **Created:** 2025-07-06

**Background:** llm-checker is a CLI tool by Pavelevich that inspects a machine's hardware — GPU VRAM, system RAM, and CPU capabilities — and produces a ranked list of LLM models the machine can run locally. It integrates with Ollama to provide direct download links for compatible models and shows estimated inference speed and memory headroom for each option. The tool launched in July 2025 and targets users new to local LLM deployment.

**Problem it solves:** Users new to running LLMs locally often download models that exceed their hardware's capabilities, resulting in out-of-memory errors or unusably slow inference. llm-checker removes the guesswork by automatically reading hardware specifications and mapping them to a curated model compatibility database before the user commits to a download.

**Why another one?** While Ollama itself lists available models, it does not filter or rank them based on the user's actual hardware. llm-checker fills this gap with hardware-aware filtering and direct Ollama integration, making the model selection step accessible to users who do not know how to calculate VRAM requirements manually.

---

## 22. [qmd](https://github.com/tobi/qmd)
> mini cli search engine for your docs, knowledge bases, meeting notes. All local.

**Language:** TypeScript  |  **Stars:** 9,753  |  **Forks:** 531  |  **Score:** 1,310  |  **Created:** 2025-12-08

**Background:** qmd is a lightweight command-line search engine for local document collections — markdown files, knowledge bases, and meeting notes — written in TypeScript by Tobi. It builds a local index of document content and provides fast full-text and semantic search without any cloud dependency or running server process. The tool is designed to be invoked on the command line and integrated into terminal workflows.

**Problem it solves:** Personal knowledge bases and document collections grow large enough that grep-based search becomes slow and misses semantic relationships between documents. Cloud-based tools like Notion search and Google Drive require uploading documents to external servers. qmd provides fast local search with semantic understanding while keeping all data on the user's machine.

**Why another one?** qmd occupies the gap between full-featured local RAG systems that require significant setup and simple grep-based search. Its single-command invocation, zero-server architecture, and TypeScript implementation make it easy to install and use without configuring a vector database or embedding server.

---

## 23. [llmfit](https://github.com/AlexsJones/llmfit)
> 157 models. 30 providers. One command to find what runs on your hardware.

**Language:** Rust  |  **Stars:** 1,337  |  **Forks:** 79  |  **Score:** 1,270  |  **Created:** 2026-02-15

**Background:** llmfit is a Rust CLI tool by AlexsJones that inventories a machine's hardware and cross-references it against a database of 157 models from 30 providers to determine which models are compatible with the available resources. Created just three days before this report date, its rapid star accumulation reflects immediate demand for hardware-aware model selection tooling. The Rust implementation produces a fast, dependency-free binary.

**Problem it solves:** As the number of locally-runnable LLM models has exploded across providers including Ollama, LM Studio, and llama.cpp, determining which specific model variant fits a given machine's GPU and RAM configuration has become increasingly time-consuming. llmfit automates this cross-reference with a comprehensive, up-to-date model database covering multiple providers simultaneously.

**Why another one?** Compared to llm-checker (also on this list), llmfit's differentiator is its breadth — 30 providers and 157 models — and its Rust implementation, which produces a smaller, faster binary with no Node.js dependency. The two tools address the same problem with different scope and implementation tradeoffs.

---

## 24. [PaperKnife](https://github.com/potatameister/PaperKnife)
> Privacy-first PDF utility (Zero-Server Architecture). Merge, split, compress, and edit PDFs 100% locally.

**Language:** TypeScript  |  **Stars:** 553  |  **Forks:** 28  |  **Score:** 1,251  |  **Created:** 2026-01-26

**Background:** PaperKnife is a browser-based PDF utility built with a zero-server architecture, meaning all PDF processing — merging, splitting, compression, and editing — happens entirely in the browser using WebAssembly without any file ever being uploaded to a server. Written in TypeScript, it was launched in January 2026 by potatameister and targets users who need PDF manipulation tools but are unwilling to send sensitive documents to cloud services.

**Problem it solves:** Popular online PDF tools such as ilovepdf and Smallpdf process documents on their servers, raising privacy concerns for documents containing sensitive personal, legal, or financial information. PaperKnife provides the same functionality entirely client-side, ensuring that document contents never leave the user's device.

**Why another one?** While PDF.js and similar libraries enable client-side PDF rendering, building a full-featured utility on top of them requires significant engineering. PaperKnife packages this into a polished, ready-to-use application that non-technical users can access without installation, occupying a space between complex desktop applications and privacy-invasive web tools.

---

## 25. [seerr](https://github.com/seerr-team/seerr)
> Open-source media request and discovery manager for Jellyfin, Plex, and Emby.

**Language:** TypeScript  |  **Stars:** 9,534  |  **Forks:** 624  |  **Score:** 1,241  |  **Created:** 2022-03-09

**Background:** Seerr is an open-source media request and discovery management tool that integrates with self-hosted media servers — Jellyfin, Plex, and Emby — allowing users to browse available content and submit requests for media they want added to the library. It provides a polished web interface with user authentication, request approval workflows, and notifications, serving as the user-facing discovery layer on top of a media server stack.

**Problem it solves:** Self-hosted media server administrators often receive ad-hoc requests from family or household members for specific content without a structured workflow for tracking, approving, and fulfilling those requests. Seerr formalizes this process with a request queue, approval controls, and automatic integration with media automation tools.

**Why another one?** Seerr explicitly supports Jellyfin alongside Plex and Emby, which distinguishes it from Overseerr (Plex-only originally). As Jellyfin adoption has grown among users seeking a fully open-source media server stack, Seerr has become the preferred request manager for Jellyfin-based setups, which sustains its recurring appearance in trending lists.

---

> **Day's theme:** A day dominated by local-first and open-source alternatives — from hardware-matched LLM selection and privacy-preserving PDF tools to self-hosted communication platforms — reflecting a broad push toward user sovereignty over data, compute, and AI.
