# Trendshift Report — 2026-03-22
**Total:** 25 repositories

---

## 1. [Understand-Anything](https://github.com/Lum1104/Understand-Anything)
> Claude Code skills that turn any codebase into an interactive knowledge graph you can explore, search, and ask questions about (Multi-platform e.g., Codex are supported).

**Language:** TypeScript  |  **Stars:** 5,462  |  **Forks:** 423  |  **Score:** 10,000  |  **Created:** 2026-03-15

**Background:** Understand-Anything is a Claude Code plugin by Lum1104 that analyzes a codebase using a multi-agent pipeline, builds a knowledge graph of every file, function, class, and dependency, and presents it through an interactive web dashboard. It supports multiple agent platforms including Claude Code, Codex, and others, and has gained over 5,400 stars in its first week since launching on March 15, 2026.

**Problem it solves:** Onboarding to a large, unfamiliar codebase is slow and painful — documentation is perpetually outdated, and reading code blind without understanding the architecture is inefficient. Understand-Anything generates a living, explorable map with plain-English explanations for every component, turning weeks of archaeology into a single command.

**Why another one?** Most code analysis tools either produce static documentation or require manual setup of graph databases. Understand-Anything differentiates by combining LLM intelligence with static analysis inside the coding agent itself — the knowledge graph is built and queryable directly from slash commands (`/understand-chat`, `/understand-diff`) without leaving the development workflow.

---

## 2. [project-nomad](https://github.com/Crosstalk-Solutions/project-nomad)
> Project N.O.M.A.D, is a self-contained, offline survival computer packed with critical tools, knowledge, and AI to keep you informed and empowered — anytime, anywhere.

**Language:** TypeScript  |  **Stars:** 14,627  |  **Forks:** 1,375  |  **Score:** 9,066  |  **Created:** 2025-06-24

**Background:** Project N.O.M.A.D. (Node for Offline Media, Archives, and Data) is a self-contained, offline-first knowledge and education server by Crosstalk Solutions. It orchestrates a collection of containerized tools — Ollama for local AI chat with RAG via Qdrant, Kiwix for offline Wikipedia and medical references, Kolibri for Khan Academy courses, ProtoMaps for offline maps, and CyberChef for data tools — all managed through a browser-based Command Center UI.

**Problem it solves:** In scenarios without reliable internet — remote locations, emergencies, or censored networks — access to critical knowledge, education, and AI capabilities disappears. Project N.O.M.A.D. bundles everything into a single Debian-based installation that runs on any local hardware, keeping information and AI assistance available regardless of connectivity.

**Why another one?** The differentiating angle is the breadth of integrated offline capabilities in a single managed deployment: AI chat, encyclopedias, education platforms, offline maps, and data tools, all orchestrated through Docker with a setup wizard. Most offline knowledge projects cover one domain; N.O.M.A.D. provides a curated all-in-one survival computing stack.

---

## 3. [TradingAgents](https://github.com/TauricResearch/TradingAgents)
> TradingAgents: Multi-Agents LLM Financial Trading Framework

**Language:** Python  |  **Stars:** 39,393  |  **Forks:** 7,323  |  **Score:** 7,047  |  **Created:** 2024-12-28

**Background:** TradingAgents is an open-source multi-agent trading framework by Tauric Research that mirrors the dynamics of real-world trading firms. It deploys specialized LLM-powered agents — fundamental analysts, sentiment experts, technical analysts, traders, and a risk management team — that collaboratively evaluate market conditions. Version 0.2.2, released in March 2026, added support for GPT-5.4, Gemini 3.1, and Claude 4.6, along with a five-tier rating scale and cross-platform stability improvements.

**Problem it solves:** Individual trading analysis requires synthesizing fundamentals, sentiment, and technical signals — a process that demands broad expertise and significant time. TradingAgents automates this by distributing each analysis type to a specialized agent, then aggregating their findings through a structured debate and risk assessment process before producing a trading recommendation.

**Why another one?** Most AI trading tools are either black-box signal generators or simple single-model wrappers. TradingAgents' multi-agent architecture mirrors real trading desks where specialists argue and challenge each other's views, producing more robust analysis. The multi-provider LLM support also means users are not locked into a single model vendor.

---

## 4. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 108,363  |  **Forks:** 8,701  |  **Score:** 6,190  |  **Created:** 2025-10-09

**Background:** Superpowers is a composable set of agent skills and a structured software development workflow by Jesse Vincent (obra), designed to install into coding agents such as Claude Code, Cursor, Codex, Gemini CLI, and OpenCode via their plugin systems. It enforces a multi-stage methodology: brainstorming and spec refinement before any code, detailed implementation planning, then subagent-driven development with two-stage code review. The project has accumulated over 108,000 stars since its October 2025 launch.

**Problem it solves:** Coding agents left to their defaults tend to dive directly into writing code, skip test-driven development, and drift from the original intent mid-session. Superpowers installs guard rails — mandatory spec approval, red-green-refactor TDD enforcement, and plan checkpoints — so an agent can work autonomously for hours without derailing.

**Why another one?** Rather than being a new coding agent, Superpowers is a methodology layer portable across multiple platforms. The differentiating angle is cross-agent compatibility (same skills install in Claude Code, Cursor, Codex, Gemini CLI, and OpenCode) and the emphasis on subagent delegation rather than a single long-running context, which limits drift.

---

## 5. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips — From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 60,953  |  **Forks:** 9,146  |  **Score:** 5,039  |  **Created:** 2025-10-13

**Background:** The Agency is a growing collection of meticulously crafted AI agent personalities by msitarzewski, organized into divisions: Engineering (frontend, backend, mobile, AI, DevOps, security), Marketing, Product, Operations, and more. Each agent file contains a full identity with personality traits, core workflows, technical deliverables with code examples, and success metrics. It supports Claude Code, Cursor, Aider, Windsurf, Copilot, and Gemini CLI through conversion scripts.

**Problem it solves:** General-purpose AI prompts produce generic output lacking domain expertise and consistent voice. The Agency provides pre-built specialist personas with deep domain knowledge, structured workflows, and measurable deliverables — turning a single AI session into an entire team of experts.

**Why another one?** The differentiating angle is the depth and personality of each agent — these are not simple prompt templates but fully realized personas with defined responsibilities, escalation paths, communication styles, and quality gates. The multi-tool integration (six supported platforms via conversion scripts) and MIT license make adoption frictionless.

---

## 6. [MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2)
> Automate the process of making money online.

**Language:** Python  |  **Stars:** 22,154  |  **Forks:** 2,294  |  **Score:** 4,656  |  **Created:** 2024-02-12

**Background:** MoneyPrinterV2 (MPV2) is a Python automation tool by FujiwaraChoki that automates various online income generation strategies. It includes a Twitter bot with CRON scheduling, a YouTube Shorts automater, Amazon affiliate marketing integration, and local business discovery with cold outreach capabilities. The project is a complete rewrite of the original MoneyPrinter with a more modular architecture and requires Python 3.12.

**Problem it solves:** Running multiple online monetization channels — social media posting, short-form video creation, affiliate link management, and business outreach — requires constant manual effort and switching between platforms. MPV2 automates these workflows end-to-end from a single application with configurable schedules.

**Why another one?** MPV2's scope is broader than typical single-channel automation tools. Rather than automating just video creation or just social media, it bundles multiple income strategies (content creation, affiliate marketing, local business outreach) into one orchestrated system. The modular architecture and community forks (including a Chinese version, MoneyPrinterTurbo) reflect a growing ecosystem around the approach.

---

## 7. [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
> Turn Claude Code into a full game dev studio — 48 AI agents, 36 workflow skills, and a complete coordination system mirroring real studio hierarchy.

**Language:** Shell  |  **Stars:** 2,995  |  **Forks:** 398  |  **Score:** 4,478  |  **Created:** 2026-02-12

**Background:** Claude Code Game Studios by Donchitos turns a single Claude Code session into a structured game development studio with 48 specialized agents organized into a three-tier hierarchy: directors (Opus-level), department leads (Sonnet-level), and specialists (Sonnet/Haiku-level). It includes 37 workflow skills, 8 hooks for automated validation, 11 path-scoped coding rules, and 29 document templates for GDDs, ADRs, sprint plans, and more.

**Problem it solves:** Building a game solo with AI lacks structure — there is no QA pass, no design review, no one guarding the creative vision or catching architectural mistakes. This project installs the organizational structure of a real studio so the AI session has defined responsibilities, escalation paths, and quality gates across design, programming, art, audio, narrative, QA, and production.

**Why another one?** Most AI coding assistants and skill sets are domain-agnostic. Claude Code Game Studios is purpose-built for game development, with agents and workflows specific to game design documents, economy balancing, narrative direction, and level design — a level of domain specialization that generic agent frameworks do not provide.

---

## 8. [autoresearch](https://github.com/karpathy/autoresearch)
> AI agents running research on single-GPU nanochat training automatically

**Language:** Python  |  **Stars:** 50,773  |  **Forks:** 7,078  |  **Score:** 3,925  |  **Created:** 2026-03-06

**Background:** Autoresearch is a project by Andrej Karpathy that gives an AI agent a small but real LLM training setup and lets it experiment autonomously overnight. The agent modifies the training code (`train.py`), trains for a fixed 5-minute time budget on a single GPU, checks if the result improved via validation bits per byte (val_bpb), keeps or discards the change, and repeats. The training code is a simplified single-GPU implementation of nanochat, and the human programs `program.md` Markdown files that provide context and instructions to the agent.

**Problem it solves:** Traditional ML research requires a human in the loop for every experiment iteration — hypothesize, modify code, run training, evaluate, repeat. Autoresearch removes the human from the inner loop: the agent autonomously generates hypotheses, implements changes, and evaluates results, allowing overnight research runs that produce logs of experiments and (hopefully) a better model by morning.

**Why another one?** The novelty is the deliberate inversion of what the human and agent each control. The human writes `program.md` (the research org instructions), never touching Python. The agent edits `train.py` (the model and training code). This separation creates a meta-research loop where the human optimizes the research methodology while the agent optimizes the model — a fundamentally different interaction pattern from typical coding agents.

---

## 9. [MSA](https://github.com/EverMind-AI/MSA)
> Memory Sparse Attention: A scalable, end-to-end trainable latent-memory framework for 100M-token contexts.

**Language:** —  |  **Stars:** 1,908  |  **Forks:** 109  |  **Score:** 3,680  |  **Created:** 2025-10-29

**Background:** MSA (Memory Sparse Attention) is a research framework by EverMind AI that introduces an end-to-end trainable, scalable sparse latent-state memory layer for LLMs. It achieves near-linear complexity in both training and inference through scalable sparse attention with document-wise RoPE, KV cache compression with a Memory Parallel inference engine delivering 100M-token throughput on 2xA800 GPUs, and Memory Interleave for multi-round, multi-hop reasoning across scattered memory segments.

**Problem it solves:** Full attention bottlenecks constrain most LLMs' effective context length to 128K-1M tokens. Existing workarounds — hybrid linear attention, fixed-size state memory (RNNs), and external storage like RAG/agents — either suffer rapid precision decay at extreme scales, lack end-to-end differentiability, or require complex pipelines. MSA scales from 16K to 100M tokens with less than 9% degradation while remaining fully differentiable.

**Why another one?** MSA's core contribution is decoupling memory capacity from reasoning within a single differentiable model. Unlike RAG-based approaches that require separate retrieval pipelines, MSA fuses top-k selection with sparse attention inside the model itself. The document-wise RoPE design enables training at 64K tokens to extrapolate to 100M at inference — a 1,500x context length extrapolation that competing approaches cannot match.

---

## 10. [gstack](https://github.com/garrytan/gstack)
> Use Garry Tan's exact Claude Code setup: 15 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA.

**Language:** TypeScript  |  **Stars:** 39,705  |  **Forks:** 4,906  |  **Score:** 3,643  |  **Created:** 2026-03-11

**Background:** Gstack is the open-source "software factory" of Garry Tan, President and CEO of Y Combinator. It turns Claude Code into a virtual engineering team with 20 specialists and 8 power tools — a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production bugs, a QA lead who opens a real browser, a security officer who runs OWASP/STRIDE audits, and a release engineer who ships the PR. Tan reports shipping 600,000+ lines of production code in 60 days using this setup while running YC full-time.

**Problem it solves:** A blank Claude Code prompt requires the developer to mentally hold all the roles of a software team — product vision, architecture, design quality, code review, QA, security, and release management. Gstack encodes each role as a structured slash command so a single person can invoke an entire team's worth of checks and balances on every feature.

**Why another one?** The credibility angle is distinctive: this is the exact toolchain the CEO of YC uses daily, with before/after GitHub contribution graphs as evidence. Unlike generic skill sets, gstack is an opinionated end-to-end workflow from product ideation (`/office-hours`, `/plan-ceo-review`) through review (`/review`), QA (`/qa`), security (`/cso`), and deployment (`/ship`, `/land-and-deploy`) — covering the full lifecycle rather than individual tasks.

---

## 11. [browser-use](https://github.com/browser-use/browser-use)
> Make websites accessible for AI agents. Automate tasks online with ease.

**Language:** Python  |  **Stars:** 83,544  |  **Forks:** 9,722  |  **Score:** 3,386  |  **Created:** 2024-10-31

**Background:** Browser Use is a Python library that enables AI agents to interact with websites through a real browser. It provides a clean API for LLMs to navigate, click, type, and extract information from web pages, supporting models from OpenAI, Anthropic, Google, and its own ChatBrowserUse model. It offers both a self-hosted open-source library and a cloud service with stealth-enabled browser automation for scalable deployments.

**Problem it solves:** Most AI agents operate in a text-only world and cannot interact with web interfaces, fill forms, or navigate multi-step web workflows. Browser Use bridges that gap by giving agents a real Chromium browser to control, enabling automation of tasks that require visual web interaction — from data extraction to multi-step form completion.

**Why another one?** Browser Use continues to trend because of its developer experience — a simple three-line setup with `uv`, multi-model support out of the box, and a dedicated `Agents.md` endpoint for LLM-assisted integration. The cloud tier for stealth-enabled automation (anti-bot bypass) addresses a pain point that self-hosted Playwright wrappers cannot solve alone.

---

## 12. [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
> The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**Language:** JavaScript  |  **Stars:** 102,648  |  **Forks:** 13,375  |  **Score:** 3,384  |  **Created:** 2026-01-18

**Background:** Everything Claude Code is a performance optimization system for AI agent harnesses assembled by Affaan Mustafa, an Anthropic hackathon winner. It includes production-ready agents, skills, hooks, slash commands, rules files, and MCP configurations evolved over 10+ months of intensive daily use, supporting Claude Code, Codex, Cowork, and other agent harnesses across 7 languages. The project has crossed 102,000 stars with an interactive installation wizard and PM2 multi-agent orchestration.

**Problem it solves:** AI coding agents ship with minimal default configuration, and building effective token optimization, memory persistence, continuous learning, security scanning, and verification loops from scratch requires extensive trial-and-error. This repository provides a complete, battle-tested system that encodes lessons about these patterns into ready-to-install configurations.

**Why another one?** The Claude Code ecosystem is maturing rapidly and there is no official reference for advanced configuration patterns. Everything Claude Code serves as the de facto community standard — its hackathon winner provenance, cross-platform support (Claude Code, Codex, Cowork), security scanning (AgentShield), and accompanying guides on token optimization and memory persistence differentiate it from simpler dotfiles repositories.

---

## 13. [parameter-golf](https://github.com/openai/parameter-golf)
> Train the smallest LM you can that fits in 16MB. Best model wins!

**Language:** Python  |  **Stars:** 3,663  |  **Forks:** 2,116  |  **Score:** 3,225  |  **Created:** 2026-02-09

**Background:** Parameter Golf is an OpenAI-sponsored challenge to train the best language model that fits in a 16MB artifact and trains in under 10 minutes on 8xH100s, evaluated by compression on the FineWeb validation set using tokenizer-agnostic bits per byte. OpenAI is providing $1,000,000 in compute credits for participants. The challenge runs from March 18 to April 30, 2026, and is designed in the spirit of elite mathematics and programming competitions.

**Problem it solves:** Most LLM research optimizes for raw performance without parameter constraints, producing ever-larger models. Parameter Golf inverts the optimization target — minimizing model size while maximizing quality — pushing the community toward creative architectures like depth recurrence, aggressive parameter tying, low-rank training, QAT, bitnets, and novel tokenizers that would otherwise receive less attention.

**Why another one?** The challenge is explicitly designed as an L(N) optimization — lowest loss given fixed parameters — complementing the NanoGPT Speedrun (L(T), fixed time) and NanoGPT Slowrun (L(D), fixed dataset). The leaderboard shows active competition with scores around 1.12 bpb, and the recruiting angle (OpenAI plans to hire from exceptional participants) adds stakes beyond academic interest.

---

## 14. [TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN)
> 基于多智能体LLM的中文金融交易框架 - TradingAgents中文增强版

**Language:** Python  |  **Stars:** 20,308  |  **Forks:** 4,281  |  **Score:** 2,594  |  **Created:** 2025-06-26

**Background:** TradingAgents-CN is a Chinese-enhanced fork of TauricResearch's TradingAgents framework, maintained by hsliuping. Version 1.0.0-preview features a complete architectural rewrite from Streamlit to FastAPI + Vue 3, MongoDB + Redis dual database architecture, Docker multi-architecture support (amd64 + arm64), and full A-share (Chinese mainland), Hong Kong, and US stock market support. It positions itself as a multi-agent learning and research platform for Chinese-speaking users.

**Problem it solves:** The original TradingAgents framework is English-centric with no native Chinese market data integration. TradingAgents-CN provides full Chinese localization, integrates Chinese data sources (Tushare, AkShare, BaoStock), and adds enterprise features like user authentication, batch analysis, stock screening, and simulated trading — all with a modern web frontend rather than a Streamlit demo.

**Why another one?** The Chinese financial market operates with different data providers, regulatory frameworks, and market structures (A-shares, Hong Kong connect). TradingAgents-CN is not just a translation but a substantially enhanced fork with a production-grade web application, multi-tier deployment options (green package, Docker, local code), and a learning center designed for the Chinese financial AI community.

---

## 15. [spec-kit](https://github.com/github/spec-kit)
> Toolkit to help you get started with Spec-Driven Development

**Language:** Python  |  **Stars:** 81,494  |  **Forks:** 6,949  |  **Score:** 2,480  |  **Created:** 2025-08-21

**Background:** Spec Kit is an open-source toolkit by GitHub that implements Spec-Driven Development — a methodology where specifications become executable, directly generating working implementations rather than just guiding them. It includes the `specify` CLI tool for initializing and managing projects, supports multiple AI agents (Claude Code and others), and offers community extensions and presets for customization. The project has amassed over 81,000 stars since its August 2025 launch.

**Problem it solves:** Traditional software development treats specs as disposable scaffolding discarded once coding begins, leading to implementation drift and wasted effort. Spec Kit makes specifications the primary artifact — they are machine-readable, validated, and used to generate implementations, ensuring the code always matches the agreed-upon behavior.

**Why another one?** Spec Kit is published by GitHub itself, giving it institutional credibility and integration potential that third-party alternatives lack. The `specify` CLI, community extension system, and preset marketplace create an ecosystem around the methodology rather than a one-off tool, and the explicit support for multiple AI agents makes it agent-agnostic.

---

## 16. [opencode](https://github.com/anomalyco/opencode)
> The open source coding agent.

**Language:** TypeScript  |  **Stars:** 128,939  |  **Forks:** 13,654  |  **Score:** 2,479  |  **Created:** 2025-04-30

**Background:** OpenCode is an open-source AI coding agent by Anomaly that runs in the terminal and as a desktop application (beta). It supports installation via npm, Homebrew, Scoop, Chocolatey, pacman, Nix, and a direct install script, with desktop apps for macOS (Apple Silicon and Intel), Windows, and Linux. The project has grown to nearly 129,000 stars and offers translations in 21 languages. It is model-agnostic, supporting providers including OpenAI, Anthropic, Google, and open-source models.

**Problem it solves:** Developers who want an open-source alternative to proprietary terminal coding agents need a tool that is model-agnostic, extensible, and available across all major platforms. OpenCode fills this gap with a mature terminal UI, a desktop app, and broad installation support, all under an open-source license.

**Why another one?** OpenCode's trajectory to 129K stars makes it the most-starred open-source coding agent. The desktop app (beta) extends its reach beyond terminal-native developers, and the 21-language translation effort signals a global community investment. The model-agnostic architecture means users can switch between providers without changing their workflow.

---

## 17. [ClawRouter](https://github.com/BlockRunAI/ClawRouter)
> The agent-native LLM router for OpenClaw. 41+ models, <1ms routing, USDC payments on Base & Solana via x402.

**Language:** TypeScript  |  **Stars:** 6,323  |  **Forks:** 518  |  **Score:** 2,362  |  **Created:** 2026-02-03

**Background:** ClawRouter is an open-source LLM router by BlockRunAI that is designed specifically for autonomous AI agents. It analyzes each request across 15 dimensions and routes to the cheapest capable model in under 1ms, entirely locally. The key differentiator is its agent-native authentication: wallet signatures instead of API keys, and USDC micropayments via the x402 protocol on Base and Solana instead of credit cards. It supports 55+ models from OpenAI, Anthropic, Google, xAI, DeepSeek, and more. Winner of the USDC Hackathon Agentic Commerce category.

**Problem it solves:** Every other LLM router was built for human developers — create an account, get an API key, pick a model, pay with a credit card. Agents cannot do any of that. ClawRouter removes all human-gated steps: a wallet is generated locally, the wallet signature is the authentication, 15-dimension scoring picks the model automatically, and agents pay per-request with USDC.

**Why another one?** The agent-native architecture is the clear differentiator from OpenRouter, LiteLLM, Martian, and Portkey, all of which assume a human operator. ClawRouter's combination of local routing (no external API call for model selection), x402 micropayments (agents can pay autonomously), and zero-trust authentication (wallet signatures) addresses the specific needs of a future where agents operate independently.

---

## 18. [production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course)
> The Mother of AI Project — Phase 1 RAG Systems: arXiv Paper Curator

**Language:** Python  |  **Stars:** 5,081  |  **Forks:** 1,214  |  **Score:** 2,299  |  **Created:** 2025-08-06

**Background:** This is a learner-focused, week-by-week course by jamwithai that builds a complete production-grade RAG system for academic paper research. It progresses from infrastructure setup (Docker, FastAPI, PostgreSQL, OpenSearch, Airflow) through data pipelines, BM25 keyword search, hybrid search with semantic understanding, a complete RAG pipeline with local LLM, production monitoring with Langfuse, and culminates in Week 7 with agentic RAG using LangGraph and a Telegram bot for mobile access.

**Problem it solves:** Most RAG tutorials jump straight to vector search and skip the professional foundations — keyword search, proper indexing, monitoring, and caching. This course follows the production path: master BM25 search foundations first, then layer on vectors for hybrid retrieval, then add agents, mirroring how successful companies actually build RAG systems.

**Why another one?** The differentiating angle is the progressive, hands-on approach that mirrors real production engineering. Each week builds on the last with runnable code, and the final agentic RAG system with LangGraph decision nodes, document grading, query rewriting, and guardrails goes well beyond typical "intro to RAG" tutorials. The Telegram bot integration adds a practical mobile access layer.

---

## 19. [pentagi](https://github.com/vxcontrol/pentagi)
> Fully autonomous AI Agents system capable of performing complex penetration testing tasks

**Language:** Go  |  **Stars:** 12,992  |  **Forks:** 1,616  |  **Score:** 2,267  |  **Created:** 2025-01-06

**Background:** PentAGI (Penetration testing Artificial General Intelligence) is a self-hosted, Dockerized autonomous agent system for security testing by vxcontrol. It bundles 20+ professional pen-testing tools — including nmap, Metasploit, and sqlmap — inside isolated Docker containers, using a multi-agent team-of-specialists architecture with a lead agent that delegates to sub-agents for research, development, and infrastructure tasks. A Graphiti-powered knowledge graph using Neo4j tracks semantic relationships across testing sessions.

**Problem it solves:** Security testing requires orchestrating dozens of tools in sequence, interpreting intermediate outputs, and adapting the attack path based on discoveries — demanding expertise and significant time even for professionals. PentAGI automates the orchestration layer, with intelligent task planning for smaller models and optional execution monitoring for enhanced reliability.

**Why another one?** PentAGI is self-hosted and open-source, distinguishing it from commercial AI-assisted security platforms. Its architecture is notably complete: full REST and GraphQL APIs, Bearer token authentication, Grafana/Prometheus integration, a built-in scraper container for browser-based OSINT, and integration with seven search systems (Tavily, Perplexity, DuckDuckGo, Google, Sploitus, Traversaal, Searxng). The knowledge graph provides long-term memory that most comparable tools lack.

---

## 20. [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)
> A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic

**Language:** Python  |  **Stars:** 30,953  |  **Forks:** 2,156  |  **Score:** 2,241  |  **Created:** 2025-04-19

**Background:** Awesome Claude Code is a selectively curated index of skills, agents, plugins, hooks, and tools for enhancing Claude Code workflows, maintained by hesreallyhim. It covers agent skills, workflows and knowledge guides, tooling (IDE integrations, usage monitors, orchestrators, config managers), status lines, hooks, and slash commands. The list is organized in multiple styles (awesome, extra, classic, flat) and features recent additions like prompt injection scanners, permission management tools, and tmux integration.

**Problem it solves:** The Claude Code ecosystem is expanding rapidly with community-built extensions scattered across thousands of repositories. Discovering trustworthy, useful skills and tools requires browsing GitHub trending, Twitter threads, and Discord channels. This curated list applies quality filters and categorizes the ecosystem into navigable sections.

**Why another one?** As the canonical awesome list for Claude Code, it serves as the community's entry point for discovering extensions. The multiple display styles, detailed descriptions with editorial commentary, and regular updates with "Latest Additions" sections keep it a living resource rather than a static link collection.

---

## 21. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows — all through natural language commands.

**Language:** Shell  |  **Stars:** 81,726  |  **Forks:** 6,816  |  **Score:** 2,176  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official agentic coding tool that operates in the terminal, IDE, or via @claude mentions on GitHub. It understands codebases and executes tasks through natural language commands. The project has reached over 81,000 stars and features a plugin ecosystem, installation via curl, Homebrew, WinGet, and npm, and supports macOS, Linux, and Windows. Installation via npm is now deprecated in favor of native installers.

**Problem it solves:** Developers spend significant time on routine tasks — navigating unfamiliar code, managing git workflows, running repetitive operations — that require context about the codebase but not deep creative thinking. Claude Code automates these tasks by understanding project structure and executing commands directly in the terminal, reducing context-switching overhead.

**Why another one?** As the official Anthropic product, Claude Code benefits from tight integration with Claude models and first-party plugin support. The GitHub @claude mention feature for PR reviews, the growing plugin marketplace, and the migration from npm to native installers signal maturation from a developer tool into a platform. Its consistent presence on trending reflects the broader ecosystem of skills and extensions being built around it.

---

## 22. [skills](https://github.com/mattpocock/skills)
> My personal directory of skills, straight from my .claude directory.

**Language:** Shell  |  **Stars:** 9,379  |  **Forks:** 769  |  **Score:** 2,099  |  **Created:** 2026-02-03

**Background:** This is Matt Pocock's personal collection of Claude Code skills, installable via `npx skills@latest add`. It includes planning and design skills (write-a-prd, prd-to-plan, prd-to-issues, grill-me, design-an-interface, request-refactor-plan), development skills (tdd, triage-issue, improve-codebase-architecture), tooling skills (setup-pre-commit, git-guardrails-claude-code), and writing/knowledge skills (write-a-skill, edit-article, ubiquitous-language, obsidian-vault).

**Problem it solves:** Claude Code's power scales with the quality of skills installed, but crafting effective skills from scratch requires trial-and-error. Matt Pocock, known in the TypeScript community for his teaching and Total TypeScript, publishes his battle-tested personal workflow as installable skills, providing a curated starting point for developers.

**Why another one?** The skills reflect an opinionated TypeScript-focused workflow: PRDs filed as GitHub issues, vertical-slice TDD, DDD ubiquitous language extraction, and Obsidian vault integration. The one-command install via npx and the author's community reputation make these skills particularly influential as templates for how the ecosystem thinks about Claude Code skill design.

---

## 23. [TaxHacker](https://github.com/vas3k/TaxHacker)
> Self-hosted AI accounting app. LLM analyzer for receipts, invoices, transactions with custom prompts and categories

**Language:** TypeScript  |  **Stars:** 2,352  |  **Forks:** 334  |  **Score:** 1,994  |  **Created:** 2025-03-10

**Background:** TaxHacker is a self-hosted accounting application by vas3k designed for freelancers, indie hackers, and small businesses. It uses AI (OpenAI, Google Gemini, or Mistral) to analyze photos of receipts, invoices, and PDFs, automatically extracting product names, amounts, dates, merchants, taxes, and line items into a structured database. It features automatic currency conversion for 170+ currencies and 14 cryptocurrencies using historical exchange rates, multi-project support, and customizable AI prompts for extracting specific information.

**Problem it solves:** Freelancers and small businesses spend hours manually entering receipt data, categorizing expenses, and converting currencies for tax reporting. TaxHacker automates the entire receipt-to-database pipeline with AI, handling multilingual documents, multiple currencies, and custom categorization — all self-hosted so financial data stays on the user's own infrastructure.

**Why another one?** The self-hosted angle differentiates TaxHacker from cloud accounting services that require uploading financial documents to third-party servers. The custom AI prompts feature lets users extract domain-specific information beyond standard fields, and cryptocurrency support (with historical rates) targets a user base that commercial accounting tools often underserve.

---

## 24. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> practice made claude perfect

**Language:** HTML  |  **Stars:** 21,330  |  **Forks:** 1,863  |  **Score:** 1,986  |  **Created:** 2025-10-31

**Background:** Claude Code Best Practice by shanraisshan is a comprehensive reference covering every Claude Code extensibility mechanism — subagents, commands, skills, workflows, hooks, MCP servers, and orchestration patterns. It includes both best practice guides and concrete implementations for each feature, with an orchestration workflow document that demonstrates multi-agent coordination. The repository references Boris Cherny's tips and tracks updates against each Claude Code release (currently v2.1.81).

**Problem it solves:** Claude Code's documentation covers individual features but does not provide opinionated guidance on how to combine them effectively. This repository bridges that gap with structured best practices for each extensibility mechanism, paired with working implementations that demonstrate the patterns in practice.

**Why another one?** The repository is organized as a reference manual rather than a collection of skills — each feature has both a best practice document and a matching implementation, making it a learning resource for understanding Claude Code's architecture. The orchestration workflow guide, which shows how to combine subagents, commands, and hooks into coordinated workflows, addresses a gap in the official documentation.

---

## 25. [deer-flow](https://github.com/bytedance/deer-flow)
> An open-source SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skills, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.

**Language:** Python  |  **Stars:** 39,355  |  **Forks:** 4,624  |  **Score:** 1,818  |  **Created:** 2025-05-07

**Background:** DeerFlow (Deep Exploration and Efficient Research Flow) version 2.0 is a ground-up rewrite by ByteDance that evolved from a deep research framework into a full super agent harness. It orchestrates sub-agents, memory, and sandboxes with extensible skills, supports Docker deployment, MCP servers, and IM channel integrations. DeerFlow 2.0 claims the #1 spot on GitHub Trending following its February 2026 launch, recommends Doubao-Seed-2.0-Code, DeepSeek v3.2, and Kimi 2.5 as primary models, and integrates BytePlus InfoQuest for intelligent search and crawling.

**Problem it solves:** Complex tasks that span research, coding, and content creation often exceed the capability of a single agent session — they require long-running execution, persistent memory, sandboxed code execution, and coordination between specialized sub-agents. DeerFlow provides the orchestration layer that manages all of these across tasks that can take minutes to hours.

**Why another one?** DeerFlow's backing by ByteDance provides engineering resources and model partnerships (Volcengine, BytePlus) that independent projects cannot match. The 2.0 rewrite sharing no code with v1 signals a serious architectural commitment. The combination of sandboxes, long-term memory, sub-agent delegation, context engineering, and IM channel integration (Telegram, Discord, Slack) in a single MIT-licensed harness covers a broader surface area than most competing frameworks.

---

> **Day's theme:** The dominant narrative across today's 25 repos is the industrialization of the coding agent ecosystem — from methodology frameworks (Superpowers, Spec Kit, gstack) and domain-specific agent studios (Game Studios, TradingAgents) to the infrastructure layer enabling agents to operate autonomously (ClawRouter's wallet-based payments, MSA's 100M-token memory, autoresearch's overnight experimentation loops). The Claude Code ecosystem in particular shows signs of maturation, with multiple curated skill directories, best practice references, and specialized extensions competing for mindshare as the platform transitions from tool to platform.
