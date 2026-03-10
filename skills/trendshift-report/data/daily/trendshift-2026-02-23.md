# Trendshift Report — 2026-02-23
**Total:** 25 repositories

---

## 1. [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
> FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**Language:** N/A  |  **Stars:** 129,730  |  **Forks:** 33,055  |  **Score:** 18,432  |  **Created:** 2025-03-05

**Background:** This repository is a comprehensive archive of extracted system prompts, internal tool definitions, and model configurations from over 30 major AI coding and assistant tools. It covers products from Anthropic, Cursor, Devin AI, Replit, Windsurf, Perplexity, and many others. With nearly 130,000 stars since March 2025, it is the most-starred prompt extraction collection on GitHub.

**Problem it solves:** AI tool system prompts are proprietary and hidden from users, making it difficult to understand how these tools work internally, what constraints they operate under, or how to build similar capabilities. This repository surfaces those prompts for study, comparison, and educational purposes, enabling developers to learn from production-grade prompt engineering.

**Why another one?** The repository dominates the chart today with an 18,432 score — more than double the next entry — because AI coding tools are releasing updates at a rapid pace and each update refreshes interest in how these tools are configured. Its breadth of coverage (30+ tools) and consistent maintenance make it the de facto reference for comparing how different AI products are prompted.

---

## 2. [nanoclaw](https://github.com/qwibitai/nanoclaw)
> A lightweight alternative to OpenClaw that runs in containers for security. Connects to WhatsApp, Telegram, Slack, Discord, Gmail and other messaging apps, has memory, scheduled jobs, and runs directly on Anthropic's Agents SDK

**Language:** TypeScript  |  **Stars:** 20,096  |  **Forks:** 3,310  |  **Score:** 7,223  |  **Created:** 2026-01-31

**Background:** Nanoclaw is a containerized personal AI assistant built on Anthropic's Agents SDK, positioned as a lightweight alternative to OpenClaw. Launched at the end of January 2026, it connects natively to WhatsApp, Telegram, Slack, Discord, Gmail, and other messaging platforms, shipping with persistent memory and scheduled job support. It has doubled from 10,000 to 20,000 stars in a single day.

**Problem it solves:** OpenClaw is a full-featured assistant platform with a massive codebase and complex deployment requirements. Nanoclaw strips the concept down to a containerized runtime that is simpler to deploy and secure, while retaining the core features most users need: multi-channel messaging integration, persistent memory, and task scheduling.

**Why another one?** The direct integration with Anthropic's Agents SDK rather than a custom agent runtime means Nanoclaw benefits from upstream SDK improvements without reimplementation. The container-first architecture makes it deployable on any Docker-compatible host without the dependency sprawl of larger assistant platforms, hitting the sweet spot between OpenClaw's full power and the simplicity users want for personal use.

---

## 3. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 75,000  |  **Forks:** 5,793  |  **Score:** 5,905  |  **Created:** 2025-10-09

**Background:** Superpowers is a composable skills framework and structured software development methodology created by Jesse Vincent (obra). It installs into coding agents such as Claude Code, Cursor, Codex, and OpenCode via their plugin systems, enforcing a multi-stage workflow: brainstorm and refine a spec, produce a detailed implementation plan, then execute through subagent-driven development with two-stage code review. The project has reached 75,000 stars since October 2025.

**Problem it solves:** Coding agents left to default settings tend to skip planning, ignore test-driven development, and drift from the original intent mid-session. Superpowers installs guard rails — mandatory spec approval, red-green-refactor TDD enforcement, and plan checkpoints — so an agent can work autonomously for extended periods without derailing from what was agreed upon.

**Why another one?** Rather than being a new coding agent, Superpowers is a methodology layer that works across multiple agents via their plugin systems. The portability (same skills install in Claude Code, Cursor, Codex, and OpenCode) and the emphasis on subagent delegation rather than a single long-running context are the primary differentiators. It keeps trending as new users discover its cross-agent compatibility.

---

## 4. [skills](https://github.com/huggingface/skills)
> Hugging Face Skills

**Language:** Python  |  **Stars:** 8,521  |  **Forks:** 503  |  **Score:** 5,068  |  **Created:** 2025-11-24

**Background:** Hugging Face Skills is the official skills repository from Hugging Face, providing reusable agent skills that integrate with the Hugging Face ecosystem of models, datasets, and Spaces. Launched in November 2025, it offers a framework for creating, sharing, and composing skills that leverage Hugging Face's model hub, targeting the intersection of agent tooling and the ML model ecosystem.

**Problem it solves:** Building agent skills that interact with ML models requires boilerplate for model loading, inference, and output parsing. Hugging Face Skills standardizes this integration layer so developers can compose agent capabilities that tap into the Hub's 800,000+ models without writing custom glue code for each one.

**Why another one?** Hugging Face's unique position as the largest ML model registry gives its skills framework direct access to an unmatched model catalog. While other skill frameworks focus on tool use and API calls, Hugging Face Skills natively bridges the gap between agent workflows and model inference, making it the natural choice for ML-heavy agent pipelines.

---

## 5. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Language:** Shell  |  **Stars:** 75,677  |  **Forks:** 6,100  |  **Score:** 4,902  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official terminal-based agentic coding tool, launched in February 2025. It operates directly in the developer's terminal, understanding the full codebase context and executing tasks through natural language commands. The tool handles routine development tasks, explains complex code, manages git workflows, and supports an extensible skills and hooks system.

**Problem it solves:** Developers spend significant time on repetitive coding tasks, navigating unfamiliar codebases, and managing version control workflows. Claude Code automates these tasks directly in the terminal where developers already work, eliminating the context-switching overhead of moving between an IDE, a browser-based AI chat, and the command line.

**Why another one?** Claude Code continues trending just past its first anniversary, now at 75,677 stars. The growing ecosystem of community skills, hooks, and configurations — evidenced by multiple ecosystem projects on this list — keeps driving adoption. As Anthropic's first-party coding agent, it serves as a reference implementation that other tools build compatibility with.

---

## 6. [awesome](https://github.com/sindresorhus/awesome)
> Awesome lists about all kinds of interesting topics

**Language:** N/A  |  **Stars:** 443,800  |  **Forks:** 33,445  |  **Score:** 3,847  |  **Created:** 2014-07-11

**Background:** Sindre Sorhus's awesome repository is the root meta-list that spawned the entire "awesome list" convention on GitHub, created in July 2014. It serves as a curated index of other curated lists spanning programming languages, frameworks, platforms, developer tools, theory, media, and more. With nearly 444,000 stars, it is one of the most-starred repositories on all of GitHub.

**Problem it solves:** Before the awesome list pattern existed, there was no consistent convention for community-maintained topic indexes on GitHub. This repository established both the format and the quality standard that thousands of downstream awesome lists now follow, making it the canonical entry point for discovering curated resources on any technical topic.

**Why another one?** This repository trends periodically because it is the authoritative meta-index. Every new awesome list that gains traction links back to it, and every developer who discovers the pattern for the first time stars the original. Its 11-year maintenance history and unmatched star count make it infrastructure in GitHub's knowledge graph rather than a project competing with alternatives.

---

## 7. [pentagi](https://github.com/vxcontrol/pentagi)
> Fully autonomous AI Agents system capable of performing complex penetration testing tasks

**Language:** Go  |  **Stars:** 9,294  |  **Forks:** 1,073  |  **Score:** 3,807  |  **Created:** 2025-01-06

**Background:** PentAGI is a self-hosted autonomous agent system for penetration testing, built in Go by vxcontrol. It bundles over 20 professional security tools — including nmap, Metasploit, and sqlmap — inside isolated Docker containers and uses a multi-agent architecture where a lead agent delegates tasks to specialized sub-agents for research, development, and infrastructure. A Neo4j-backed knowledge graph provides long-term memory across testing sessions.

**Problem it solves:** Security testing requires orchestrating dozens of tools in sequence, interpreting intermediate outputs, and adapting attack paths based on findings — a process that demands deep expertise and significant time. PentAGI automates this orchestration layer, allowing the system to autonomously chain tools together and produce detailed vulnerability reports with exploitation guidance.

**Why another one?** PentAGI is fully self-hosted and open-source, distinguishing it from commercial AI-assisted security platforms. Its architecture is notably complete: a full REST and GraphQL API, Grafana/Prometheus monitoring integration, and a bundled scraper container for browser-based OSINT. The long-term semantic memory via knowledge graphs sets it apart from simpler tool-chaining approaches.

---

## 8. [llmfit](https://github.com/AlexsJones/llmfit)
> Hundreds of models & providers. One command to find what runs on your hardware.

**Language:** Rust  |  **Stars:** 12,559  |  **Forks:** 709  |  **Score:** 3,757  |  **Created:** 2026-02-15

**Background:** LLMFit is a Rust-based CLI tool that scans your hardware — GPU VRAM, system RAM, disk space — and tells you which LLMs from hundreds of models and providers can actually run on your machine. Created by Alex Jones and launched just a week before this report, it has rapidly accumulated over 12,500 stars. The tool covers models from Ollama, Hugging Face, and other providers.

**Problem it solves:** The local LLM landscape has hundreds of models in various quantizations and sizes, and figuring out which ones fit your specific hardware requires manually checking VRAM requirements, comparing quantization trade-offs, and cross-referencing compatibility lists. LLMFit automates this entire process with a single command.

**Why another one?** The Rust implementation provides a fast, dependency-free binary that runs without Python or Node.js. While model recommendation features exist in some LLM runners, LLMFit is provider-agnostic — it checks compatibility across Ollama, Hugging Face, and other sources simultaneously rather than being locked to one ecosystem. The one-week-old project hitting 12,500 stars signals strong demand for this specific capability.

---

## 9. [worldmonitor](https://github.com/koala73/worldmonitor)
> Real-time global intelligence dashboard — AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface

**Language:** TypeScript  |  **Stars:** 34,697  |  **Forks:** 5,833  |  **Score:** 3,692  |  **Created:** 2026-01-08

**Background:** WorldMonitor is a real-time situational awareness dashboard that aggregates global news, geopolitical events, and infrastructure status into a unified interface. Built in TypeScript and launched in January 2026, it uses AI to categorize, summarize, and surface trending developments across multiple source feeds. The project has reached nearly 35,000 stars in under two months.

**Problem it solves:** Monitoring global events typically requires manually checking dozens of news sources, government feeds, and infrastructure status pages. WorldMonitor consolidates these into a single dashboard with AI-powered summarization and categorization, reducing the time required to maintain situational awareness for security teams, analysts, and journalists.

**Why another one?** The combination of news aggregation, geopolitical monitoring, and infrastructure tracking in one tool is the differentiator. Existing solutions typically focus on only one of these domains — RSS readers for news, specialized platforms for OSINT, separate dashboards for infrastructure. WorldMonitor merges all three with an AI layer that surfaces cross-domain connections.

---

## 10. [awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
> A community collection of OpenClaw use cases for making life easier.

**Language:** N/A  |  **Stars:** 22,126  |  **Forks:** 1,817  |  **Score:** 2,837  |  **Created:** 2026-02-08

**Background:** Awesome OpenClaw Usecases is a community-curated collection of practical use cases for the OpenClaw personal AI assistant, assembled by Hesam Sheikh and launched in early February 2026. It documents real-world applications people have built using OpenClaw's skills and multi-channel architecture, organized by category. The repository has quadrupled to over 22,000 stars in just two weeks.

**Problem it solves:** OpenClaw has over 5,700 skills in its ClawHub registry, but discovering which combinations of skills solve specific real-world problems requires experimentation. This collection provides documented, tested use cases that show how to combine OpenClaw capabilities for practical tasks, reducing the trial-and-error discovery process.

**Why another one?** While awesome-openclaw-skills catalogs individual skills with security vetting, this repository focuses on complete use-case recipes that combine multiple skills into workflows. The distinction is between a tool catalog (skills) and a cookbook (use cases), serving users who know what they want to accomplish but not which tools to combine.

---

## 11. [drone-logbook](https://github.com/arpanghosh8453/drone-logbook)
> DJI Fly Log analyzer: A high-performance universal dashboard application for organizing and analyzing DJI drone flight logs privately in one place. Built with Tauri v2, DuckDB, and React.

**Language:** TypeScript  |  **Stars:** 323  |  **Forks:** 34  |  **Score:** 2,834  |  **Created:** 2026-02-06

**Background:** Drone Logbook is a desktop application for analyzing DJI flight logs, built with Tauri v2, DuckDB, and React by Arpan Ghosh. It provides a local-first dashboard for organizing, visualizing, and analyzing drone flight data without uploading logs to any cloud service. Despite only 323 stars, its high trendshift score indicates a strong velocity of engagement.

**Problem it solves:** DJI's official Fly app provides limited log analysis, and third-party flight log services require uploading potentially sensitive location and flight data to remote servers. Drone Logbook keeps all data local while providing detailed analytics — flight paths, telemetry visualization, and aggregate statistics — in a native desktop application.

**Why another one?** The privacy-first, local-only approach using Tauri v2 and DuckDB is the differentiator. Most DJI log analyzers are web-based services that require data uploads. The DuckDB backend enables fast analytical queries over large log datasets without a database server, and Tauri v2 produces a lightweight native binary compared to Electron alternatives.

---

## 12. [prompts.chat](https://github.com/f/prompts.chat)
> f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**Language:** HTML  |  **Stars:** 151,166  |  **Forks:** 19,861  |  **Score:** 2,828  |  **Created:** 2022-12-05

**Background:** Originally launched as "Awesome ChatGPT Prompts" by Fatih Kadir Akin in December 2022, prompts.chat has evolved into a full community platform for sharing, discovering, and collecting AI prompts. It now includes a web frontend, a Hugging Face dataset mirror, a self-hosting option for organizational privacy, and an interactive prompt engineering book. The repository has over 151,000 stars.

**Problem it solves:** Users of AI chat models face a cold-start problem: crafting effective system prompts and persona-based instructions requires trial and error. Prompts.chat provides a structured, community-maintained library of tested prompts that serve as starting points, reducing the experimentation needed to get useful outputs from general-purpose models.

**Why another one?** This repository trends recurrently because it remains the canonical reference for prompt collections. Its evolution from a static markdown file into a full web platform with community submissions, Hugging Face dataset mirroring, and self-hosting capability has kept it relevant as a living resource. The organizational self-hosting feature addresses enterprise privacy concerns that the public site cannot.

---

## 13. [taste-skill](https://github.com/Leonxlnx/taste-skill)
> Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, "slop"

**Language:** N/A  |  **Stars:** 2,484  |  **Forks:** 160  |  **Score:** 2,705  |  **Created:** 2026-02-19

**Background:** Taste-Skill is an agent skill that injects design sensibility into AI-generated frontend code, aiming to eliminate the generic, template-like output that coding agents typically produce. Created by Leonxlnx and launched just four days before this report, it has already gathered nearly 2,500 stars. The skill works by providing design principles and aesthetic constraints to the agent during frontend code generation.

**Problem it solves:** AI coding agents generate functional but visually bland frontends — the same rounded corners, the same card layouts, the same color palettes. Taste-Skill addresses this "AI slop" problem by guiding agents toward more distinctive, intentional design choices rather than the default patterns embedded in training data.

**Why another one?** Most agent skills focus on functionality, architecture, or workflow process. Taste-Skill targets the aesthetic dimension that other skills ignore, operating at the intersection of design and code generation. The rapid star accumulation in four days suggests that "AI-generated UI looks generic" is a widely shared frustration that existing tools have not addressed.

---

## 14. [OpenBB](https://github.com/OpenBB-finance/OpenBB)
> Financial data platform for analysts, quants and AI agents.

**Language:** Python  |  **Stars:** 62,737  |  **Forks:** 6,144  |  **Score:** 2,704  |  **Created:** 2020-12-20

**Background:** OpenBB is an open-source financial data platform originally launched as "OpenBB Terminal" in December 2020, providing analysts, quants, and now AI agents with programmatic access to financial data from dozens of providers. It has evolved from a Bloomberg Terminal alternative into a broader data platform with a Python SDK, API layer, and agent-compatible interfaces. The project has over 62,700 stars.

**Problem it solves:** Financial data is fragmented across dozens of paid and free providers, each with different APIs, formats, and authentication methods. OpenBB provides a unified interface to query across providers with consistent data models, eliminating the need to write and maintain separate integrations for each data source.

**Why another one?** OpenBB's positioning has expanded beyond human analysts to explicitly support AI agents, which is likely driving its renewed trending. The platform's standardized data access layer makes it a natural tool-use target for financial AI agents. Its five-year track record and 62,700 stars give it credibility that newer financial data projects lack.

---

## 15. [airllm](https://github.com/lyogavin/airllm)
> AirLLM 70B inference with single 4GB GPU

**Language:** Jupyter Notebook  |  **Stars:** 13,698  |  **Forks:** 1,345  |  **Score:** 2,658  |  **Created:** 2023-06-12

**Background:** AirLLM is a library that enables running 70-billion-parameter language models on a single GPU with as little as 4GB of VRAM. Created by Gavin Li and first released in June 2023, it uses layer-by-layer inference with aggressive memory management to fit models that would normally require multiple high-end GPUs. The project has grown to nearly 14,000 stars.

**Problem it solves:** Running large language models locally typically requires expensive multi-GPU setups or cloud instances with 80+ GB of VRAM. AirLLM makes 70B-class models accessible to developers and researchers with consumer-grade hardware by trading inference speed for dramatically reduced memory requirements.

**Why another one?** While quantization libraries like GPTQ and AWQ reduce model size, they still require fitting the entire quantized model in memory. AirLLM takes a fundamentally different approach by streaming layers through GPU memory, meaning the VRAM requirement is bounded by the largest single layer rather than the full model. This architectural choice enables hardware that quantization alone cannot serve.

---

## 16. [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
> GitNexus: The Zero-Server Code Intelligence Engine - GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph with a built in Graph RAG Agent.

**Language:** TypeScript  |  **Stars:** 11,399  |  **Forks:** 1,361  |  **Score:** 2,613  |  **Created:** 2025-08-02

**Background:** GitNexus is a client-side code intelligence tool that generates interactive knowledge graphs from GitHub repositories or ZIP files, running entirely in the browser with no server component. It includes a built-in Graph RAG Agent for conversational exploration of the generated graph. Created by Abhigyan Patwari in August 2025, it has grown to over 11,000 stars.

**Problem it solves:** Understanding an unfamiliar codebase typically requires cloning, setting up a local environment, and manually tracing dependencies and relationships between modules. GitNexus eliminates the setup step — users drop in a repo URL or ZIP file in their browser and immediately get a visual knowledge graph of the codebase's structure with an AI agent for exploration.

**Why another one?** The zero-server, fully client-side architecture differentiates it from code intelligence tools like Sourcegraph or CodeSee that require server-side indexing. Running entirely in the browser means no data leaves the user's machine, addressing privacy concerns for proprietary codebases. The integrated Graph RAG Agent adds conversational exploration on top of the visual graph.

---

## 17. [agents](https://github.com/cloudflare/agents)
> Build and deploy AI Agents on Cloudflare

**Language:** TypeScript  |  **Stars:** 4,471  |  **Forks:** 450  |  **Score:** 2,402  |  **Created:** 2025-01-29

**Background:** Cloudflare Agents is a framework for building and deploying AI agents on Cloudflare's edge network, launched in January 2025. It leverages Cloudflare Workers, Durable Objects, and the broader Cloudflare developer platform to provide a serverless runtime for AI agents with built-in state management, scheduling, and WebSocket support.

**Problem it solves:** Deploying AI agents that need persistent state, scheduled execution, and real-time communication typically requires managing servers, databases, and WebSocket infrastructure. Cloudflare Agents bundles all of this into a serverless framework that deploys to Cloudflare's global edge network, eliminating infrastructure management for agent developers.

**Why another one?** The edge deployment model is the primary differentiator — agents run on Cloudflare's global network with sub-50ms latency to most users, rather than in a central data center. The tight integration with Durable Objects for state and Workers for compute means agents get persistence and scheduling without external databases or cron services.

---

## 18. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> practice made claude perfect

**Language:** HTML  |  **Stars:** 12,317  |  **Forks:** 1,158  |  **Score:** 2,390  |  **Created:** 2025-10-31

**Background:** Claude Code Best Practice is a community-maintained guide documenting effective patterns, configurations, and workflows for getting the most out of Claude Code. Created by Shan Raisshan in October 2025, it compiles practical advice from power users into an HTML-based reference covering CLAUDE.md configuration, hook patterns, skill usage, and session management strategies.

**Problem it solves:** Claude Code's flexibility means there are many ways to configure and use it, but official documentation focuses on features rather than opinionated best practices. This guide fills the gap by collecting battle-tested patterns from the community — what works, what does not, and how to structure projects for optimal agent performance.

**Why another one?** While Anthropic maintains official documentation, this community guide captures the practical knowledge that emerges from daily use across diverse codebases and workflows. The 12,300 stars indicate significant demand for this type of practitioner-driven guidance, and it keeps trending alongside Claude Code itself as new users seek to optimize their setup.

---

## 19. [Scrapling](https://github.com/D4Vinci/Scrapling)
> An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

**Language:** Python  |  **Stars:** 26,976  |  **Forks:** 1,985  |  **Score:** 2,384  |  **Created:** 2024-10-13

**Background:** Scrapling is a Python web scraping framework created by D4Vinci that adapts its approach based on the target site's anti-scraping measures. It handles everything from simple HTTP requests to full browser automation, automatically escalating its strategy as needed. Launched in October 2024, it has accumulated nearly 27,000 stars.

**Problem it solves:** Web scraping requires different tools depending on a site's defenses — simple requests for static pages, headless browsers for JavaScript-rendered content, and specialized techniques for sites with bot detection. Scrapling unifies these approaches in a single framework that automatically selects the appropriate strategy.

**Why another one?** Unlike Scrapy (focused on spider orchestration) or Playwright (focused on browser automation), Scrapling's adaptive approach means developers write one scraping pipeline that automatically adjusts to different anti-bot measures. The framework detects what level of sophistication is needed per-request rather than requiring the developer to choose upfront.

---

## 20. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry.

**Language:** N/A  |  **Stars:** 33,181  |  **Forks:** 3,144  |  **Score:** 2,303  |  **Created:** 2026-01-25

**Background:** Awesome OpenClaw Skills is a curated index of over 5,400 community-built skills for the OpenClaw assistant, maintained by VoltAgent. It draws from ClawHub, OpenClaw's public registry, but filters out spam, duplicates, and skills identified as malicious by security researchers. The project has nearly doubled from 17,500 to 33,000 stars since the previous day's report.

**Problem it solves:** The ClawHub registry is large and unfiltered, making it difficult to find trustworthy, useful skills without wading through spam, duplicates, and potentially malicious entries. This curated list applies documented quality and security filters, providing reasonable confidence that listed skills are functional and safe.

**Why another one?** The OpenClaw skill ecosystem is the primary extensibility mechanism for the most-starred personal assistant on GitHub. The security angle — explicitly cataloguing malicious skills and providing guidance on VirusTotal partnership checks — adds a layer of value that the raw ClawHub registry does not provide. The explosive star growth reflects the broader OpenClaw ecosystem momentum.

---

## 21. [Mole](https://github.com/tw93/Mole)
> Deep clean and optimize your Mac.

**Language:** Shell  |  **Stars:** 38,889  |  **Forks:** 1,074  |  **Score:** 2,275  |  **Created:** 2025-09-23

**Background:** Mole is a macOS system cleaning and optimization utility by tw93, built primarily in Shell. It provides deep cleaning capabilities for removing cached files, broken symlinks, unused dependencies, and other accumulated system debris. Since its September 2025 launch, it has grown to nearly 39,000 stars, making it one of the most popular Mac maintenance tools on GitHub.

**Problem it solves:** macOS accumulates cache files, temporary data, old logs, and orphaned application support files over time, consuming disk space and potentially degrading performance. Commercial tools like CleanMyMac solve this but cost money and require broad system permissions from a closed-source vendor. Mole provides comparable cleaning capabilities as a free, auditable Shell script.

**Why another one?** Being a Shell script is both the simplicity argument and the trust argument — users can read every line before running it, unlike compiled commercial cleaners. The 39,000 stars indicate strong demand for a trustworthy, free alternative to CleanMyMac. Mole keeps trending because macOS users continuously discover it as they search for open-source system maintenance tools.

---

## 22. [FossFLOW](https://github.com/stan-smith/FossFLOW)
> Make beautiful isometric infrastructure diagrams

**Language:** TypeScript  |  **Stars:** 19,026  |  **Forks:** 1,240  |  **Score:** 2,183  |  **Created:** 2025-06-30

**Background:** FossFLOW is an open-source tool for creating isometric infrastructure diagrams, built in TypeScript. It provides a visual interface for generating polished, three-dimensional architecture diagrams commonly used in cloud infrastructure documentation, DevOps presentations, and system design discussions. The project has grown to over 19,000 stars since its June 2025 launch.

**Problem it solves:** Creating professional isometric infrastructure diagrams typically requires either expensive design software with manual drawing skills or proprietary diagramming tools with limited export options. FossFLOW automates the isometric rendering, letting users focus on describing their infrastructure rather than drawing it.

**Why another one?** While tools like draw.io and Excalidraw support general diagramming, they do not specialize in isometric infrastructure views. FossFLOW's narrow focus on isometric rendering produces more visually polished output for this specific use case, and being open-source differentiates it from commercial alternatives like Cloudcraft.

---

## 23. [openclaw](https://github.com/openclaw/openclaw)
> Your own personal AI assistant. Any OS. Any Platform. The lobster way.

**Language:** TypeScript  |  **Stars:** 289,626  |  **Forks:** 54,924  |  **Score:** 2,078  |  **Created:** 2025-11-24

**Background:** OpenClaw is the most-starred personal AI assistant on GitHub, running as a locally-hosted gateway that routes conversations through messaging platforms users already have: WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Microsoft Teams, Matrix, and more. It supports voice input and output on macOS, iOS, and Android, and can render an interactive Canvas. With nearly 290,000 stars since November 2025, it anchors an entire ecosystem of skills, use cases, and derivative projects.

**Problem it solves:** Personal AI assistants typically require a dedicated app or web interface, creating friction for users who want to interact through channels already open on their phone or desktop. OpenClaw turns existing messaging clients into AI frontends so the assistant is reachable through whatever app the user already has.

**Why another one?** OpenClaw itself at rank 23 (score 2,078) is less the story than its ecosystem dominance on this list: nanoclaw (#2), awesome-openclaw-usecases (#10), and awesome-openclaw-skills (#20) all orbit this project. The ecosystem effect is self-reinforcing — more skills attract more users, who build more skills and use-case guides. Four OpenClaw-related entries in a single day's chart is a strong signal of platform maturity.

---

## 24. [system-design](https://github.com/karanpratapsingh/system-design)
> Learn how to design systems at scale and prepare for system design interviews

**Language:** N/A  |  **Stars:** 41,434  |  **Forks:** 5,240  |  **Score:** 2,038  |  **Created:** 2022-08-15

**Background:** This repository by Karan Pratap Singh is a comprehensive system design course covering fundamental concepts like databases, caching, message queues, and distributed systems, along with real-world case studies of architectures used by companies like Twitter, Netflix, and Uber. Created in August 2022, it has steadily grown to over 41,000 stars as a free alternative to paid interview prep resources.

**Problem it solves:** System design interview preparation typically relies on paid courses (Grokking the System Design Interview, ByteByteGo) or scattered blog posts with inconsistent depth. This repository provides a structured, free curriculum that covers both foundational concepts and practical design exercises in a single, well-organized reference.

**Why another one?** The repository keeps trending because the demand for system design interview preparation is continuous and growing. Its free, open-source nature and comprehensive coverage make it discoverable to each new wave of engineers preparing for interviews. The 41,000 stars reflect cumulative discovery over three and a half years rather than a single viral moment.

---

## 25. [humanizer](https://github.com/blader/humanizer)
> Claude Code skill that removes signs of AI-generated writing from text

**Language:** N/A  |  **Stars:** 7,984  |  **Forks:** 604  |  **Score:** 2,015  |  **Created:** 2026-01-18

**Background:** Humanizer is a Claude Code skill that post-processes AI-generated text to remove telltale patterns of machine writing — formulaic transitions, excessive hedging, repetitive sentence structures, and other markers that AI detection tools flag. Created by blader in January 2026, it has quickly accumulated nearly 8,000 stars.

**Problem it solves:** AI-generated text has recognizable patterns that both human readers and automated detection tools can identify: overuse of phrases like "it's worth noting," predictable paragraph structures, and a tendency toward excessive qualification. Humanizer applies targeted rewrites to eliminate these patterns while preserving the original meaning.

**Why another one?** While paraphrasing tools exist, Humanizer operates as a Claude Code skill rather than a standalone service, integrating directly into the writing workflow. It targets the specific artifacts of AI writing — not random synonym swapping but pattern-level corrections informed by what detection tools actually flag. The high star count suggests significant demand for this capability within the Claude Code skill ecosystem.

---

> **Day's theme:** The OpenClaw ecosystem dominates with four related entries, while agent skills frameworks, coding agent tooling, and local-first applications continue to define what developers build and share on GitHub.
