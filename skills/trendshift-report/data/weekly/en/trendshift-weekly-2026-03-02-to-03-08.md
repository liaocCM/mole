# Trendshift Weekly Report — 2026-03-02 to 2026-03-08
**Total unique repositories:** 83 (from 175 daily entries across 7 days)

---

## 1. [cli](https://github.com/googleworkspace/cli)
> Google Workspace CLI — one command-line tool for Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, and more. Dynamically built from Google Discovery Service. Includes AI agent skills.

**Language:** Rust  |  **Stars:** 16595  |  **Forks:** 641  |  **Best Score:** 56923  |  **Best Rank:** #1  |  **Days on chart:** 2/7  |  **Created:** 2026-03-02

**Background:** gws is a new CLI tool released under the googleworkspace GitHub organization (though not an officially supported Google product) that provides a single command-line interface for all Google Workspace APIs. Written in Rust and distributed via npm, it launched on March 2 and immediately topped the Trendshift chart with the highest score of the week. The tool dynamically builds its command surface by reading Google's Discovery Service at runtime, meaning it automatically gains new capabilities when Google adds API endpoints.

**Problem it solves:** Interacting with Google Workspace APIs from the command line has historically required per-service SDKs, OAuth boilerplate, and hand-written HTTP requests. gws collapses this into a single binary that handles authentication and outputs structured JSON, making it usable both for human operators and as tool-call targets for AI agents.

**Why another one?** Unlike static CLI wrappers that need manual updates when Google ships new endpoints, gws discovers its entire command surface dynamically from Google's own service definitions. It also ships with 40+ built-in agent skills, positioning it as a first-class tool for AI coding assistants rather than a human-only utility.

---

## 2. [symphony](https://github.com/openai/symphony)
> Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervising coding agents.

**Language:** Elixir  |  **Stars:** 9439  |  **Forks:** 653  |  **Best Score:** 34254  |  **Best Rank:** #2  |  **Days on chart:** 4/7  |  **Created:** 2026-02-26

**Background:** Symphony is an OpenAI project that bridges project management boards (like Linear) with autonomous coding agents (like Codex). Written in Elixir and released as an "engineering preview," it monitors task boards for work items, spawns isolated agent instances to implement them, and reports back with CI status, PR reviews, complexity analysis, and walkthrough videos. The spec is open, and OpenAI encourages reimplementation in any language.

**Problem it solves:** Today's coding agents require engineers to sit alongside them, write prompts, review output, and manage context. Symphony lifts the interaction layer from "supervise the agent" to "manage the backlog," letting engineers describe what needs to be done rather than how to guide the agent through doing it.

**Why another one?** Symphony is notable for being published as a spec rather than just an implementation, explicitly inviting the community to build alternative runtimes. Its Elixir reference implementation leverages OTP's process isolation model for running many concurrent agent sessions, and its integration with OpenAI's Codex gives it a native path to their model infrastructure.

---

## 3. [RuView](https://github.com/ruvnet/RuView)
> WiFi DensePose turns commodity WiFi signals into real-time human pose estimation, vital sign monitoring, and presence detection — all without a single pixel of video.

**Language:** Rust  |  **Stars:** 31832  |  **Forks:** 4198  |  **Best Score:** 24100  |  **Best Rank:** #1  |  **Days on chart:** 3/7  |  **Created:** 2025-06-07

**Background:** RuView is an edge AI perception system built in Rust by ruvnet that uses WiFi Channel State Information (CSI) to detect and reconstruct human poses, vital signs, and room presence without any cameras. It builds on the WiFi DensePose concept first demonstrated in academic research at Carnegie Mellon University and extends it into a practical edge-deployable system using the RuVector library.

**Problem it solves:** Camera-based monitoring systems raise serious privacy concerns and require line-of-sight placement. RuView replaces optical sensors with commodity WiFi hardware, analyzing signal disturbances caused by human movement to reconstruct body position, breathing rate, heart rate, and presence in real time using physics-based signal processing and machine learning.

**Why another one?** Unlike academic WiFi sensing prototypes that depend on synchronized cameras for training data, RuView is designed to operate entirely from radio signals and self-learned embeddings at the edge. Its Rust implementation delivers the low latency needed for real-time pose estimation on resource-constrained hardware.

---

## 4. [wifi-densepose](https://github.com/ruvnet/wifi-densepose)
> WiFi DensePose turns commodity WiFi signals into real-time human pose estimation, vital sign monitoring, and presence detection — all without a single pixel of video.

**Language:** Rust  |  **Stars:** 15004  |  **Forks:** 1567  |  **Best Score:** 20932  |  **Best Rank:** #1  |  **Days on chart:** 1/7  |  **Created:** 2025-06-07

**Background:** wifi-densepose is the original repository from which RuView evolved, also by ruvnet. It shares the same core technology — using WiFi CSI data for human pose estimation — and serves as the foundational codebase for the broader RuView perception platform. The project accumulated 15,000 stars since its June 2025 launch.

**Problem it solves:** Same as RuView: it enables camera-free human sensing by exploiting the physical properties of WiFi signal propagation through and around human bodies. The system detects presence, estimates body position, and monitors vital signs using only standard WiFi hardware.

**Why another one?** This repository represents the earlier, more focused version of the WiFi sensing concept before it was expanded into the full RuView platform. It remains relevant as a standalone reference implementation for teams interested specifically in the WiFi DensePose technique without the broader perception framework.

---

## 5. [paperclip](https://github.com/paperclipai/paperclip)
> Open-source orchestration for zero-human companies

**Language:** TypeScript  |  **Stars:** 9517  |  **Forks:** 1062  |  **Best Score:** 14426  |  **Best Rank:** #1  |  **Days on chart:** 2/7  |  **Created:** 2026-03-02

**Background:** Paperclip is a Node.js server with a React dashboard that orchestrates teams of AI agents to run business operations autonomously. Launched the same week as this report, it positions itself as a layer above individual AI assistants: "If OpenClaw is an employee, Paperclip is the company." It provides org charts, budgets, governance structures, and cost tracking for multi-agent workflows.

**Problem it solves:** Individual AI agents can execute tasks, but coordinating multiple agents across business functions — sales, support, engineering, finance — requires organizational structure that no single agent provides. Paperclip adds the management layer: assigning goals, tracking costs, enforcing governance, and presenting a unified dashboard.

**Why another one?** Most agent orchestration tools focus on technical workflows (CI/CD, code review). Paperclip targets business-level orchestration with concepts borrowed from corporate structure — org charts, budgets, approval chains — rather than software engineering pipelines. Its "zero-human company" framing is provocative but reflects a genuine gap in the tooling landscape.

---

## 6. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers.

**Language:** Shell  |  **Stars:** 18396  |  **Forks:** 2842  |  **Best Score:** 13037  |  **Best Rank:** #1  |  **Days on chart:** 5/7  |  **Created:** 2025-10-13

**Background:** The Agency is a community-maintained collection of specialized AI agent personality templates, born from a Reddit thread and refined over months of iteration. Each agent template includes deep domain expertise, a unique communication style, and production-ready workflows with measurable success metrics. The project is designed for use with Claude Code and similar AI coding assistants.

**Problem it solves:** Generic AI prompts produce generic results. By providing meticulously crafted agent personas with domain-specific expertise, deliverable-focused workflows, and distinct communication styles, The Agency gives users specialist-level output without needing to engineer complex prompts themselves.

**Why another one?** Unlike prompt template collections that offer one-liners, each agent in The Agency is a fully realized personality with processes, success metrics, and documented deliverables. Its five-day presence on the chart this week reflects sustained community interest in curated, personality-driven agent configurations.

---

## 7. [ironclaw](https://github.com/nearai/ironclaw)
> IronClaw is OpenClaw inspired implementation in Rust focused on privacy and security

**Language:** Rust  |  **Stars:** 8629  |  **Forks:** 908  |  **Best Score:** 12272  |  **Best Rank:** #2  |  **Days on chart:** 2/7  |  **Created:** 2026-02-03

**Background:** IronClaw is a Rust-based personal AI assistant developed by NEAR AI, built on the philosophy that "your AI assistant should work for you, not against you." It draws inspiration from OpenClaw but rewrites the core in Rust with an emphasis on local-first data storage, encryption, and transparent operation. All user data is stored locally and encrypted, never leaving the user's control.

**Problem it solves:** Mainstream AI assistants route conversations through cloud servers where data handling is opaque and aligned with corporate interests rather than user interests. IronClaw keeps all information local and encrypted, giving users full ownership of their data while still providing a capable AI assistant experience.

**Why another one?** The Rust rewrite provides memory safety guarantees and performance characteristics that TypeScript-based assistants cannot match, while the privacy-first architecture differentiates it from both OpenClaw and cloud-based assistants. Its MIT/Apache dual license and backing by NEAR AI signal long-term commitment to open development.

---

## 8. [worldmonitor](https://github.com/koala73/worldmonitor)
> Real-time global intelligence dashboard — AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface

**Language:** TypeScript  |  **Stars:** 34697  |  **Forks:** 5833  |  **Best Score:** 9274  |  **Best Rank:** #1  |  **Days on chart:** 4/7  |  **Created:** 2026-01-08

**Background:** World Monitor is an open-source situational awareness platform that aggregates real-time news, geopolitical events, and infrastructure status into a single dashboard. Built in TypeScript, it offers multiple specialized variants (general, tech-focused, finance-focused) accessible via web. The project has grown to nearly 35,000 stars since its January 2026 launch.

**Problem it solves:** Staying informed about global events requires monitoring dozens of news sources, social media feeds, and infrastructure status pages. World Monitor consolidates these into a single AI-powered interface that filters, categorizes, and surfaces relevant information in real time.

**Why another one?** World Monitor differentiates through its multi-variant approach (separate dashboards for general, tech, and finance audiences) and its AGPL license, which ensures derivative works remain open source. Its four-day chart presence this week suggests steady organic interest rather than a single viral spike.

---

## 9. [airi](https://github.com/moeru-ai/airi)
> Self hosted, you-owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds. Capable of realtime voice chat, Minecraft, Factorio playing.

**Language:** TypeScript  |  **Stars:** 31704  |  **Forks:** 3103  |  **Best Score:** 9216  |  **Best Rank:** #2  |  **Days on chart:** 5/7  |  **Created:** 2024-12-01

**Background:** Project AIRI by moeru-ai is a self-hosted AI companion platform that aims to recreate the Neuro-sama experience — an AI virtual character capable of real-time voice conversation, game playing (Minecraft, Factorio), and persistent personality. It supports web, macOS, and Windows, with translations in seven languages. The project has accumulated over 31,000 stars since December 2024.

**Problem it solves:** Building an interactive AI companion that can hold real-time voice conversations, play games, and maintain a consistent personality across sessions requires integrating voice synthesis, game APIs, memory systems, and character modeling. AIRI packages all of these into a single self-hosted application.

**Why another one?** AIRI is one of the few open-source projects attempting to match the capabilities of commercial AI companion platforms while keeping all data and processing on the user's own hardware. Its game-playing capabilities (Minecraft, Factorio) go well beyond simple chatbot interactions, and its five-day chart presence this week indicates sustained community engagement.

---

## 10. [shannon](https://github.com/KeygraphHQ/shannon)
> Shannon Lite is a fully autonomous AI pentester for web apps and APIs. 96.15% (100/104 exploits) on a hint-free, source-aware variant of the XBOW benchmark.

**Language:** TypeScript  |  **Stars:** 32869  |  **Forks:** 3275  |  **Best Score:** 7734  |  **Best Rank:** #3  |  **Days on chart:** 3/7  |  **Created:** 2025-09-27

**Background:** Shannon is an autonomous white-box AI penetration testing tool developed by Keygraph. It analyzes source code to identify attack vectors and then executes real exploits to prove vulnerabilities before they reach production. The project scored 96.15% on a source-aware variant of the XBOW benchmark, demonstrating near-complete coverage of known web application exploit categories.

**Problem it solves:** Manual penetration testing is expensive, slow, and requires specialized expertise. Shannon automates the entire workflow — from source code analysis to attack vector identification to actual exploit execution — producing actionable vulnerability reports with proof-of-concept exploits.

**Why another one?** Shannon's white-box approach (analyzing source code rather than just probing endpoints) gives it deeper coverage than black-box scanning tools. Its 96% benchmark score on XBOW demonstrates that AI-driven pentesting can approach the thoroughness of skilled human testers, and its recent addition of Claude model support via AWS Bedrock and Google Vertex AI broadens its model compatibility.

---

## 11. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> practice made claude perfect

**Language:** HTML  |  **Stars:** 12935  |  **Forks:** 1213  |  **Best Score:** 7543  |  **Best Rank:** #5  |  **Days on chart:** 4/7  |  **Created:** 2025-10-31

**Background:** claude-code-best-practice is a community-maintained repository by shanraisshan that documents best practices for using Claude Code effectively. It covers the Command-Agent-Skill orchestration workflow, implementation patterns, and practical tips gathered from the community. The project has grown to nearly 13,000 stars since October 2025.

**Problem it solves:** Claude Code is a powerful tool, but extracting maximum value from it requires understanding its orchestration model, skill system, and effective prompt patterns. This repository consolidates community knowledge into actionable guidance with concrete implementation examples.

**Why another one?** Unlike generic prompt engineering guides, this repository is specifically tailored to Claude Code's architecture — commands, agents, and skills — and provides implemented examples alongside the documentation. Its four-day chart appearance reflects ongoing community demand for Claude Code optimization knowledge.

---

## 12. [visual-explainer](https://github.com/nicobailon/visual-explainer)
> Agent skill that generates rich HTML pages or slide decks for diagrams, diff reviews, plan audits, data tables, and project recaps

**Language:** HTML  |  **Stars:** 5918  |  **Forks:** 405  |  **Best Score:** 7314  |  **Best Rank:** #3  |  **Days on chart:** 2/7  |  **Created:** 2026-02-16

**Background:** visual-explainer is an agent skill that transforms terminal output into styled, interactive HTML pages. Instead of ASCII art diagrams and monospace tables, it generates self-contained HTML with real typography, dark/light themes, and interactive Mermaid diagrams with zoom and pan. It installs as a plugin for Claude Code and other agent platforms.

**Problem it solves:** Coding agents default to ASCII art for diagrams and pipe-delimited tables for data, both of which become unreadable beyond trivial complexity. visual-explainer intercepts these outputs and renders them as proper HTML with Mermaid diagrams, styled tables, and responsive layouts that open in the browser.

**Why another one?** Most agent output formatters focus on markdown rendering. visual-explainer goes further by generating fully self-contained HTML pages with interactive features (zoomable diagrams, sortable tables) and no build step or external dependencies beyond a browser.

---

## 13. [openclaw](https://github.com/openclaw/openclaw)
> Your own personal AI assistant. Any OS. Any Platform. The lobster way.

**Language:** TypeScript  |  **Stars:** 289626  |  **Forks:** 54924  |  **Best Score:** 7303  |  **Best Rank:** #3  |  **Days on chart:** 7/7  |  **Created:** 2025-11-24

**Background:** OpenClaw is the dominant open-source personal AI assistant platform, with nearly 290,000 stars making it one of the most-starred repositories on GitHub. It runs on virtually every platform and integrates with WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, IRC, Microsoft Teams, Matrix, and many more messaging services. Its appearance on all seven days of this week's chart underscores its persistent community momentum.

**Problem it solves:** Users want a single AI assistant accessible across all their communication channels — messaging apps, email, voice — without surrendering their data to a centralized service. OpenClaw provides this as a self-hosted application that the user controls entirely.

**Why another one?** OpenClaw's dominance comes from its breadth of platform support and its vibrant ecosystem of skills and plugins. Its seven-day chart presence and massive star count make it the gravitational center of the personal AI assistant ecosystem, with many other projects on this chart explicitly building for or integrating with it.

---

## 14. [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted)
> A list of Free Software network services and web applications which can be hosted on your own servers

**Language:** N/A  |  **Stars:** 278701  |  **Forks:** 12754  |  **Best Score:** 7228  |  **Best Rank:** #6  |  **Days on chart:** 2/7  |  **Created:** 2015-06-01

**Background:** awesome-selfhosted is the canonical curated list of free and open-source self-hosted software, covering categories from analytics to wikis. Started in 2015, it has grown to nearly 279,000 stars through continuous community curation via pull requests. It periodically resurfaces on trend charts when self-hosting interest spikes.

**Problem it solves:** Finding quality self-hosted alternatives to SaaS products requires searching across dozens of sources. This repository consolidates them into a single, categorized, community-vetted list with consistent metadata (license, language, last update).

**Why another one?** It is the original and most comprehensive resource of its kind. Its periodic chart appearances correlate with broader trends toward data sovereignty and privacy awareness, which the AI assistant wave has amplified.

---

## 15. [OpenSandbox](https://github.com/alibaba/OpenSandbox)
> OpenSandbox is a general-purpose sandbox platform for AI applications, offering multi-language SDKs, unified sandbox APIs, and Docker/Kubernetes runtimes.

**Language:** Python  |  **Stars:** 7180  |  **Forks:** 526  |  **Best Score:** 7188  |  **Best Rank:** #2  |  **Days on chart:** 3/7  |  **Created:** 2025-12-17

**Background:** OpenSandbox is Alibaba's open-source sandbox platform designed to provide isolated execution environments for AI applications. It offers SDKs in multiple languages and unified APIs that work across Docker and Kubernetes runtimes. Target use cases include coding agents, GUI agents, agent evaluation, AI code execution, and reinforcement learning training.

**Problem it solves:** AI agents that execute code need secure, isolated environments to prevent unintended side effects on host systems. OpenSandbox provides a consistent API layer for creating, managing, and tearing down sandboxed environments regardless of whether the underlying runtime is Docker or Kubernetes.

**Why another one?** Alibaba brings enterprise-scale experience to the sandbox problem, supporting scenarios (GUI agents, RL training) that simpler sandboxing solutions do not address. Its multi-language SDK approach means teams are not locked into a single programming language for their agent infrastructure.

---

## 16. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry.

**Language:** N/A  |  **Stars:** 33181  |  **Forks:** 3144  |  **Best Score:** 6619  |  **Best Rank:** #3  |  **Days on chart:** 7/7  |  **Created:** 2026-01-25

**Background:** Maintained by VoltAgent, this repository catalogs over 5,400 community-built OpenClaw skills organized by category. It sources from the official OpenClaw Skills Registry and applies filtering and categorization to make the growing ecosystem navigable. Its seven-day chart presence matches OpenClaw's own consistent visibility.

**Problem it solves:** The OpenClaw skill ecosystem has grown so large that discovering relevant skills requires either searching the registry directly or knowing what to look for. This curated list provides organized browsing by category with quality filtering.

**Why another one?** It serves as the de facto directory for the OpenClaw skill ecosystem, continuously updated to track the registry's rapid growth. Its consistent chart presence indicates that new users continue to discover it as they adopt OpenClaw.

---

## 17. [Perplexica](https://github.com/ItzCrazyKns/Perplexica)
> Perplexica is an AI-powered answering engine.

**Language:** TypeScript  |  **Stars:** 32359  |  **Forks:** 3474  |  **Best Score:** 6298  |  **Best Rank:** #4  |  **Days on chart:** 2/7  |  **Created:** 2024-04-09

**Background:** Perplexica (now also known as Vane) is a privacy-focused AI answering engine that runs entirely on the user's own hardware. It combines web search with local and cloud LLM support (Ollama, OpenAI, Claude, Groq) to deliver answers with cited sources while keeping searches private. The project has accumulated over 32,000 stars since April 2024.

**Problem it solves:** Commercial AI search engines like Perplexity process queries on their servers, giving users no control over data handling. Perplexica provides equivalent functionality — web search augmented with LLM reasoning and source citations — while running entirely locally.

**Why another one?** Perplexica's multi-provider approach (supporting both local models via Ollama and cloud providers) gives users flexibility to choose their privacy/capability tradeoff. Its Docker-based deployment makes it accessible to non-technical users who want private AI search.

---

## 18. [canopy](https://github.com/canopy-network/canopy)
> The official go implementation of the Canopy Network protocol

**Language:** Go  |  **Stars:** 4262  |  **Forks:** 9293  |  **Best Score:** 6246  |  **Best Rank:** #5  |  **Days on chart:** 3/7  |  **Created:** 2024-10-30

**Background:** Canopy is the official Go implementation of the Canopy Network Protocol, a blockchain platform built on a recursive architecture where chains bootstrap each other into independence. Currently in alphanet status, it provides a framework for building blockchains and operates the seed chain that starts the recursive cycle.

**Problem it solves:** Launching new blockchain networks typically requires bootstrapping security, validator sets, and economic incentives from scratch. Canopy's recursive architecture lets new chains inherit security and utility from existing ones, reducing the cold-start problem.

**Why another one?** The recursive chain-bootstrapping concept is architecturally distinct from existing blockchain frameworks. Its unusually high fork-to-star ratio (9,293 forks vs 4,262 stars) suggests significant developer experimentation with the codebase.

---

## 19. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 75000  |  **Forks:** 5793  |  **Best Score:** 6075  |  **Best Rank:** #7  |  **Days on chart:** 7/7  |  **Created:** 2025-10-09

**Background:** Superpowers is a complete software development workflow for coding agents that enforces a disciplined process: spec extraction, design review, implementation planning, and subagent-driven development with TDD. Created by obra, it has reached 75,000 stars and appeared on all seven days of this week's chart. The framework triggers automatically when an agent detects a building task.

**Problem it solves:** Coding agents left to their own devices tend to jump straight into writing code without understanding requirements, creating plans, or testing. Superpowers imposes a structured methodology — spec, plan, implement, review — that keeps agents productive for hours without human intervention.

**Why another one?** Superpowers works as a meta-framework that sits above the agent, not inside it. It does not replace the agent's capabilities but adds process guardrails (YAGNI, DRY, TDD) that prevent the drift and regression common in unsupervised agent sessions. Its 75,000-star count places it among the most popular agent workflow tools.

---

## 20. [awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
> A community collection of OpenClaw use cases for making life easier.

**Language:** N/A  |  **Stars:** 22126  |  **Forks:** 1817  |  **Best Score:** 6069  |  **Best Rank:** #3  |  **Days on chart:** 7/7  |  **Created:** 2026-02-08

**Background:** This repository by hesamsheikh collects real-life use cases for OpenClaw, focusing not on skills or technical capabilities but on practical applications that improve daily life. It documents 36+ use cases with security warnings about third-party dependencies. The project has grown to over 22,000 stars in just one month.

**Problem it solves:** The bottleneck for OpenClaw adoption is not the availability of skills but the imagination gap — users struggle to envision how an AI assistant can improve their specific workflows. This collection bridges that gap with concrete, community-validated examples.

**Why another one?** Unlike skill catalogs that list what OpenClaw can do technically, this repository focuses on why and how real users employ it in their daily lives. Its seven-day chart presence and rapid star growth indicate strong product-market fit for this type of inspiration-driven documentation.

---

## 21. [CoPaw](https://github.com/agentscope-ai/CoPaw)
> Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

**Language:** Python  |  **Stars:** 9613  |  **Forks:** 1072  |  **Best Score:** 5787  |  **Best Rank:** #5  |  **Days on chart:** 3/7  |  **Created:** 2026-02-24

**Background:** CoPaw is a Python-based personal AI assistant from the AgentScope team (Alibaba), designed for easy deployment on personal machines or cloud infrastructure. It supports multiple chat applications and provides an extensible capability system. Released in late February 2026, it quickly accumulated nearly 10,000 stars.

**Problem it solves:** Setting up a capable personal AI assistant typically involves complex dependency management, service configuration, and platform-specific integrations. CoPaw simplifies this with pip-installable deployment and built-in support for multiple messaging platforms.

**Why another one?** CoPaw differentiates through its Python-native approach (vs TypeScript-heavy alternatives like OpenClaw) and its backing by the AgentScope team, which brings enterprise AI experience. It targets users who prefer Python tooling and want tight integration with the broader AgentScope ecosystem.

---

## 22. [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
> Master programming by recreating your favorite technologies from scratch.

**Language:** Markdown  |  **Stars:** 473392  |  **Forks:** 44374  |  **Best Score:** 5636  |  **Best Rank:** #5  |  **Days on chart:** 2/7  |  **Created:** 2018-05-09

**Background:** build-your-own-x is a compilation of step-by-step guides for recreating popular technologies from scratch — from 3D renderers to operating systems to neural networks. With over 473,000 stars, it is one of the most-starred repositories on all of GitHub. It periodically trends as new waves of developers discover it.

**Problem it solves:** Understanding how complex systems work internally requires building them yourself, but finding quality tutorials for "build X from scratch" across the full spectrum of software engineering is time-consuming. This repository indexes them all.

**Why another one?** It is the definitive collection of its kind, covering more technology categories than any competing resource. Its enduring popularity stems from the Feynman principle it embodies: "What I cannot create, I do not understand."

---

## 23. [openfang](https://github.com/RightNow-AI/openfang)
> Open-source Agent Operating System

**Language:** Rust  |  **Stars:** 12521  |  **Forks:** 1385  |  **Best Score:** 5379  |  **Best Rank:** #4  |  **Days on chart:** 2/7  |  **Created:** 2026-02-24

**Background:** OpenFang is a Rust-based "Agent Operating System" from RightNow AI, comprising 137,000 lines of code across 14 crates with over 1,767 tests and zero clippy warnings. Currently at v0.3.30 (Security Hardening Release), it compiles to a single binary and provides the infrastructure for running autonomous agents.

**Problem it solves:** Building production-grade agent systems requires handling process isolation, security, scheduling, and resource management — essentially operating system concerns applied to AI agents. OpenFang packages these capabilities into a tested, hardened runtime.

**Why another one?** OpenFang's engineering rigor (1,767+ tests, zero warnings, 14-crate architecture) sets it apart from prototype-quality agent frameworks. Its Rust implementation provides memory safety and performance guarantees that are important for long-running autonomous agent workloads.

---

## 24. [prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)
> Anthropic's Interactive Prompt Engineering Tutorial

**Language:** Jupyter Notebook  |  **Stars:** 33102  |  **Forks:** 3371  |  **Best Score:** 5176  |  **Best Rank:** #7  |  **Days on chart:** 3/7  |  **Created:** 2024-04-02

**Background:** This is Anthropic's official interactive course on prompt engineering for Claude, structured as nine chapters with exercises, an example playground for experimentation, and an answer key. It teaches the 80/20 techniques for addressing common prompt failure modes. The course has reached over 33,000 stars.

**Problem it solves:** Effective prompt engineering requires understanding both the model's strengths and its failure modes. This course provides structured, hands-on practice with immediate feedback, building from basic prompt structure to advanced techniques.

**Why another one?** As the official Anthropic tutorial, it offers authoritative guidance on Claude's specific capabilities and limitations. Its three-day chart presence this week suggests continued discovery by new Claude users.

---

## 25. [How-To-Secure-A-Linux-Server](https://github.com/imthenachoman/How-To-Secure-A-Linux-Server)
> An evolving how-to guide for securing a Linux server.

**Language:** N/A  |  **Stars:** 25751  |  **Forks:** 1687  |  **Best Score:** 4972  |  **Best Rank:** #9  |  **Days on chart:** 2/7  |  **Created:** 2019-02-09

**Background:** This is a comprehensive, community-maintained guide for securing Linux servers, covering SSH hardening, firewall configuration, intrusion detection, and more. Started in 2019, it has grown to over 25,000 stars and is periodically updated with new security practices. Its appearance this week likely correlates with increased self-hosting activity driven by the AI assistant trend.

**Problem it solves:** Securing a Linux server requires knowledge spread across dozens of man pages, blog posts, and vendor documentation. This guide consolidates the essential steps into a single, structured walkthrough with explanations of why each measure matters.

**Why another one?** It remains one of the most complete single-document server hardening guides available. Its periodic chart appearances tend to correlate with spikes in self-hosting interest, which the current wave of self-hosted AI tools is driving.

---

## 26. [agent-browser](https://github.com/vercel-labs/agent-browser)
> Browser automation CLI for AI agents

**Language:** Rust  |  **Stars:** 20352  |  **Forks:** 1189  |  **Best Score:** 4758  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2026-01-11

**Background:** agent-browser is a headless browser automation CLI from Vercel Labs, written in Rust with a Node.js fallback. It provides AI agents with direct browser control through a command-line interface, with sub-millisecond parsing overhead when installed globally. Available via npm, Homebrew, and source builds.

**Problem it solves:** AI agents frequently need to interact with web pages — filling forms, clicking buttons, extracting content — but existing browser automation tools (Playwright, Puppeteer) are designed for human developers writing test scripts, not for agents issuing commands. agent-browser provides a CLI-native interface optimized for agent tool-call patterns.

**Why another one?** The Rust implementation delivers performance that JavaScript-only solutions cannot match, and the CLI-first design means agents can use it as a tool without importing libraries or managing browser contexts programmatically. Vercel's backing signals commitment to the agent tooling ecosystem.

---

## 27. [vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands)
> VSCode theme based off the easemate IDE and Jetbrains islands theme

**Language:** PowerShell  |  **Stars:** 5123  |  **Forks:** 151  |  **Best Score:** 4724  |  **Best Rank:** #10  |  **Days on chart:** 2/7  |  **Created:** 2026-02-14

**Background:** Islands Dark is a VS Code color theme inspired by the easemate IDE, featuring floating glass-like panels, rounded corners, smooth animations, and a deeply dark canvas (#131217). Created by bwya77 in mid-February 2026, it accumulated over 5,000 stars in two weeks, signaling strong demand for this visual aesthetic.

**Problem it solves:** Developers who admire the easemate IDE's visual design but use VS Code had no faithful port of its distinctive glass-panel aesthetic. This theme bridges that gap with careful attention to glass-effect borders, pill-shaped scrollbars, and hover-aware UI elements.

**Why another one?** The easemate-inspired design language — floating panels, directional light simulation, animated transitions — goes well beyond typical color-swap themes. Its rapid adoption suggests the theme addresses a genuine aesthetic preference that simpler dark themes have not satisfied.

---

## 28. [public-apis](https://github.com/public-apis/public-apis)
> A collective list of free APIs

**Language:** Python  |  **Stars:** 405531  |  **Forks:** 43795  |  **Best Score:** 4697  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2016-03-20

**Background:** public-apis is the largest curated directory of free APIs on GitHub, with over 405,000 stars. It covers APIs across dozens of domains — weather, finance, entertainment, government data, and more — and is maintained by community contributors with backing from APILayer.

**Problem it solves:** Finding free, working APIs for side projects and prototypes requires searching across vendor documentation, developer forums, and outdated blog posts. This repository provides a single, categorized index with consistent formatting.

**Why another one?** It is the canonical resource in this space, continuously maintained since 2016. Its chart appearance this week reflects its evergreen utility for developers building new projects.

---

## 29. [claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)
> A set of ready to use Agent Skills for research, science, engineering, analysis, finance and writing.

**Language:** Python  |  **Stars:** 14105  |  **Forks:** 1530  |  **Best Score:** 4566  |  **Best Rank:** #10  |  **Days on chart:** 4/7  |  **Created:** 2025-10-19

**Background:** Claude Scientific Skills is a collection of 170+ ready-to-use scientific and research skills for AI agents, created by K-Dense AI. It covers biology, chemistry, medicine, genomics, molecular dynamics, geospatial science, time series forecasting, economic data, and more. The skills follow the open Agent Skills standard and work with Cursor, Claude Code, and Codex.

**Problem it solves:** Scientists and researchers who want to use AI agents for complex multi-step workflows need domain-specific skills that encode proper methodologies — not generic code generation. This collection provides skills that understand scientific data formats, statistical methods, and research workflows.

**Why another one?** The breadth of scientific domains covered (170+ skills across biology, chemistry, medicine, finance, and geospatial science) far exceeds what any individual researcher would build. Its four-day chart presence reflects ongoing adoption across scientific communities.

---

## 30. [ANE](https://github.com/maderix/ANE)
> Training neural networks on Apple Neural Engine via reverse-engineered private APIs

**Language:** Objective-C  |  **Stars:** 5948  |  **Forks:** 855  |  **Best Score:** 4476  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2026-02-28

**Background:** ANE Training is a research project that demonstrates backpropagation on Apple's Neural Engine using reverse-engineered private APIs (_ANEClient and _ANECompiler). Apple restricts the ANE to inference-only use through CoreML; this project bypasses that restriction to show that training is possible on the hardware. The author characterizes it explicitly as a research project, not a production framework.

**Problem it solves:** Apple Silicon's Neural Engine is a powerful accelerator that sits idle during model training because Apple only exposes it for inference via CoreML. This project proves the hardware is capable of training workloads, demonstrating that the limitation is software-imposed rather than hardware-based.

**Why another one?** No other public project has demonstrated direct ANE training via the private API surface. The benchmarks documenting ANE throughput, power consumption, and SRAM behavior provide data that was previously unavailable to the ML research community.

---

## 31. [ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)
> 12 Lessons to Get Started Building AI Agents

**Language:** Jupyter Notebook  |  **Stars:** 53475  |  **Forks:** 18576  |  **Best Score:** 4298  |  **Best Rank:** #14  |  **Days on chart:** 1/7  |  **Created:** 2024-11-28

**Background:** This Microsoft-authored course provides 12 structured lessons on building AI agents, from foundational concepts to practical implementation. It supports multiple languages through automated translation and has accumulated over 53,000 stars since November 2024, making it one of the most popular educational AI resources on GitHub.

**Problem it solves:** The AI agent space evolves rapidly, and many developers lack structured learning paths that build from fundamentals to production-ready patterns. This course provides that progression with hands-on exercises and multi-language support.

**Why another one?** Microsoft's backing provides credibility and long-term maintenance, and the multi-language translation (via GitHub Actions) makes it accessible to a global audience. Its high fork count (18,576) indicates active use in classrooms and study groups.

---

## 32. [pinchtab](https://github.com/pinchtab/pinchtab)
> High-performance browser automation bridge and multi-instance orchestrator with advanced stealth injection and real-time dashboard.

**Language:** Go  |  **Stars:** 5553  |  **Forks:** 377  |  **Best Score:** 4279  |  **Best Rank:** #7  |  **Days on chart:** 2/7  |  **Created:** 2026-02-15

**Background:** PinchTab is a standalone HTTP server written in Go that gives AI agents direct control over Chrome. It ships as a 12MB binary with an HTTP API designed for token efficiency. The server operates in two roles: a full control-plane server and a single-instance bridge runtime, providing browser automation capabilities optimized for agent consumption.

**Problem it solves:** AI agents need browser access, but existing automation tools generate verbose responses that consume excessive tokens. PinchTab's HTTP API is designed for token efficiency, returning structured, minimal responses that agents can process without wasting context window space.

**Why another one?** The 12MB Go binary with zero external dependencies contrasts sharply with Node.js-based browser automation tools that pull in hundreds of megabytes of dependencies. Its dual-mode architecture (server vs bridge) gives flexibility for both multi-instance orchestration and single-browser control.

---

## 33. [nullclaw](https://github.com/nullclaw/nullclaw)
> Fastest, smallest, and fully autonomous AI assistant infrastructure written in Zig

**Language:** Zig  |  **Stars:** 6052  |  **Forks:** 719  |  **Best Score:** 4084  |  **Best Rank:** #9  |  **Days on chart:** 1/7  |  **Created:** 2026-02-16

**Background:** NullClaw is the Zig entry in the AI assistant infrastructure space, compiling to a 678 KB static binary that boots in under 2 milliseconds and runs at approximately 1 MB peak RSS. It supports 23+ providers, 18 messaging channels, and passes 3,230+ tests. The project targets extreme resource constraints where even Rust-based alternatives are considered too heavy.

**Problem it solves:** Even the smallest Rust-based assistant binaries measure in the single-digit megabytes. NullClaw pushes the boundary to sub-megabyte territory, enabling deployment on $5 ARM boards, microcontrollers, and other deeply constrained environments.

**Why another one?** Zig's comptime metaprogramming and zero-overhead abstractions enable a binary size and startup time that Rust's standard library cannot match. At 678 KB, NullClaw is roughly one-tenth the size of its closest Rust competitor, making it viable for environments where even a few megabytes matter.

---

## 34. [generative-ai](https://github.com/GoogleCloudPlatform/generative-ai)
> Sample code and notebooks for Generative AI on Google Cloud, with Gemini on Vertex AI

**Language:** Jupyter Notebook  |  **Stars:** 14626  |  **Forks:** 3912  |  **Best Score:** 4046  |  **Best Rank:** #4  |  **Days on chart:** 1/7  |  **Created:** 2023-05-05

**Background:** This is Google Cloud's official repository of sample code and Jupyter notebooks for using generative AI services on Vertex AI. It covers Gemini models (including the recently released Gemini 3.1 Pro), search, RAG, and agent architectures. The repository has accumulated over 14,000 stars since May 2023.

**Problem it solves:** Getting started with Google Cloud's generative AI services requires understanding Vertex AI's API surface, authentication, and model-specific capabilities. This repository provides working notebooks that demonstrate each feature with production-ready patterns.

**Why another one?** As the official Google Cloud resource, it is the canonical reference for Vertex AI development. Its chart appearance this week coincides with the Gemini 3.1 Pro release, which added new notebooks to the repository.

---

## 35. [react-grab](https://github.com/aidenybai/react-grab)
> Select context for coding agents directly from your website

**Language:** TypeScript  |  **Stars:** 6362  |  **Forks:** 292  |  **Best Score:** 3984  |  **Best Rank:** #9  |  **Days on chart:** 1/7  |  **Created:** 2025-10-17

**Background:** React Grab is a developer tool that lets you point at any element on a React website and press Cmd+C to copy the file name, React component name, and HTML source code directly to your clipboard. This context can then be pasted into coding agents like Cursor, Claude Code, or Copilot to make them up to 3x faster and more accurate.

**Problem it solves:** When working with coding agents on frontend code, developers waste time manually identifying which files and components correspond to the UI elements they want to change. React Grab automates this context gathering with a single keyboard shortcut.

**Why another one?** React Grab works at the framework level (hooking into React's component tree) rather than just the DOM, giving agents richer context including component names and source file paths. Its MCP server integration allows direct connection to supported agents.

---

## 36. [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)
> Agent framework and applications built upon Qwen>=3.0, featuring Function Calling, MCP, Code Interpreter, RAG, Chrome extension, etc.

**Language:** Python  |  **Stars:** 15235  |  **Forks:** 1462  |  **Best Score:** 3866  |  **Best Rank:** #10  |  **Days on chart:** 2/7  |  **Created:** 2023-09-22

**Background:** Qwen-Agent is the official agent framework for Alibaba's Qwen language model family (version 3.0+). It provides function calling, MCP support, a code interpreter, RAG capabilities, and a Chrome extension. The project has grown to over 15,000 stars and serves as the primary way to build agent applications on top of Qwen models.

**Problem it solves:** Building agent applications on top of Qwen models requires a framework that understands Qwen's specific function calling format, tool-use patterns, and multi-turn conversation handling. Qwen-Agent provides these capabilities natively.

**Why another one?** Model-specific agent frameworks can exploit capabilities and formats that generic frameworks cannot. Qwen-Agent is tightly coupled to Qwen's architecture, providing optimized tool use and conversation management that general-purpose frameworks treat as afterthoughts.

---

## 37. [MiroFish](https://github.com/666ghj/MiroFish)
> A Simple and Universal Swarm Intelligence Engine, Predicting Anything.

**Language:** Python  |  **Stars:** 10216  |  **Forks:** 1069  |  **Best Score:** 3821  |  **Best Rank:** #6  |  **Days on chart:** 2/7  |  **Created:** 2025-11-26

**Background:** MiroFish is a swarm intelligence prediction engine from Shanda, designed to aggregate multiple prediction sources into consensus forecasts. It applies swarm intelligence principles — combining many simple predictors into emergent collective intelligence — to produce predictions across arbitrary domains.

**Problem it solves:** Individual prediction models have domain-specific biases and blind spots. MiroFish orchestrates multiple predictors as a swarm, using collective intelligence algorithms to produce forecasts that are more robust than any single model.

**Why another one?** Most prediction frameworks focus on improving individual model accuracy. MiroFish takes an orthogonal approach by treating the aggregation mechanism itself as the core innovation, applying swarm intelligence theory to model ensembling in a domain-agnostic way.

---

## 38. [llmfit](https://github.com/AlexsJones/llmfit)
> Hundreds of models & providers. One command to find what runs on your hardware.

**Language:** Rust  |  **Stars:** 13738  |  **Forks:** 760  |  **Best Score:** 3723  |  **Best Rank:** #17  |  **Days on chart:** 1/7  |  **Created:** 2026-02-15

**Background:** llmfit is a Rust terminal tool that right-sizes LLM models to a system's RAM, CPU, and GPU capabilities. It detects hardware, scores each model across quality, speed, fit, and context dimensions, and recommends which models will run well locally. It supports multi-GPU setups, MoE architectures, dynamic quantization selection, and local runtime providers (Ollama, llama.cpp, MLX).

**Problem it solves:** Choosing which LLM to run locally requires cross-referencing model requirements against hardware specs, then mentally adjusting for quantization options and runtime overhead. llmfit automates this with a single command and interactive TUI.

**Why another one?** Existing model recommendation tools are either web-based (requiring data sharing) or manual lookup tables. llmfit detects hardware locally, scores models against four dimensions simultaneously, and provides interactive exploration — all from a fast Rust binary.

---

## 39. [cs-video-courses](https://github.com/Developer-Y/cs-video-courses)
> List of Computer Science courses with video lectures.

**Language:** N/A  |  **Stars:** 76781  |  **Forks:** 10386  |  **Best Score:** 3528  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2016-10-21

**Background:** cs-video-courses is a community-maintained index of free Computer Science courses that include video lectures, covering the full CS curriculum from introductory courses to advanced topics in distributed systems, machine learning, and computer graphics. Started in 2016 by Developer-Y, it has grown to over 76,000 stars.

**Problem it solves:** High-quality CS lecture content is scattered across university websites, YouTube channels, and MOOC platforms. This repository consolidates them into a single browsable index organized by topic.

**Why another one?** It remains the most comprehensive single-repository index of CS video courses and is continuously updated by community contributions. Its periodic chart appearances reflect ongoing waves of self-directed CS education interest.

---

## 40. [waoowaoo](https://github.com/waoowaooAI/waoowaoo)
> Industry-first professional AI Agent platform for controllable film & video production.

**Language:** TypeScript  |  **Stars:** 8285  |  **Forks:** 1700  |  **Best Score:** 3496  |  **Best Rank:** #17  |  **Days on chart:** 1/7  |  **Created:** 2026-01-22

**Background:** waoowaoo is an AI-powered film and video production studio that automates the pipeline from novel text to finished video. It parses scripts into storyboards, generates consistent character and scene images, synthesizes multi-character voice acting, and assembles the output into complete videos. Currently in beta by a solo developer.

**Problem it solves:** Producing short-form video content from written stories requires coordinating multiple AI tools — image generation, voice synthesis, video composition — in a specific pipeline. waoowaoo integrates these into a single workflow with Docker-based deployment.

**Why another one?** Most AI video tools focus on individual pipeline stages (text-to-image, text-to-speech). waoowaoo is notable for providing the full end-to-end pipeline from raw text to finished video, including character consistency across scenes — a problem that single-stage tools do not address.

---

## 41. [yesitsme](https://github.com/0x0be/yesitsme)
> Simple OSINT script to find Instagram profiles by name and e-mail/phone

**Language:** Python  |  **Stars:** 2092  |  **Forks:** 220  |  **Best Score:** 3260  |  **Best Rank:** #13  |  **Days on chart:** 1/7  |  **Created:** 2021-12-23

**Background:** yesitsme is a Python OSINT tool that finds Instagram accounts associated with a specific name, email, and phone number. It uses dumpor.com indexing to retrieve usernames and automatically compares obfuscated contact information from toutatis with user-provided data. Originally created in 2021, it periodically resurfaces on trend charts.

**Problem it solves:** Identifying which Instagram account belongs to a specific person when you only have their name and partial contact information is a common OSINT task. yesitsme automates the tedious process of searching, comparing obfuscated data, and matching accounts.

**Why another one?** The tool's value lies in automating the comparison of obfuscated data (Instagram shows only first and last letters of emails, partial phone numbers) — a step that is time-consuming when done manually across many potential matches.

---

## 42. [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)
> Bash is all you need - A nano Claude Code-like agent, built from 0 to 1

**Language:** TypeScript  |  **Stars:** 24497  |  **Forks:** 4467  |  **Best Score:** 3235  |  **Best Rank:** #7  |  **Days on chart:** 2/7  |  **Created:** 2025-06-29

**Background:** learn-claude-code by shareAI-lab is an educational project that teaches how to build a Claude Code-like agent from scratch in 12 progressive sessions. Each session adds one mechanism — from the basic tool-use loop ("One loop & Bash is all you need") to isolated autonomous execution — with a single guiding motto per session.

**Problem it solves:** Understanding how AI coding agents work internally is difficult because production agents layer many mechanisms together. This project decomposes the agent into 12 incremental steps, each adding exactly one concept, making the architecture learnable.

**Why another one?** Its pedagogical approach — 12 sessions, each with one motto and one mechanism — is more structured than reading production agent source code. The project has attracted nearly 25,000 stars and 4,467 forks, indicating widespread use as a learning resource.

---

## 43. [skills](https://github.com/openai/skills)
> Skills Catalog for Codex

**Language:** Python  |  **Stars:** 13583  |  **Forks:** 762  |  **Best Score:** 3165  |  **Best Rank:** #13  |  **Days on chart:** 2/7  |  **Created:** 2025-11-25

**Background:** This is OpenAI's official skills catalog for Codex, containing system skills (auto-installed), curated skills, and experimental skills. Skills are folders of instructions, scripts, and resources that Codex discovers and uses at runtime. The repository implements the open Agent Skills standard from agentskills.io.

**Problem it solves:** Codex performs better when it has domain-specific guidance for specialized tasks. The skills system packages this guidance into portable, discoverable units that can be installed and shared across teams.

**Why another one?** As the official OpenAI skills repository, it defines the reference implementation for the Agent Skills standard. Its curated/experimental tiering provides a quality gradient that helps users find production-ready skills.

---

## 44. [rtk](https://github.com/rtk-ai/rtk)
> CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies

**Language:** Rust  |  **Stars:** 5497  |  **Forks:** 294  |  **Best Score:** 3156  |  **Best Rank:** #15  |  **Days on chart:** 2/7  |  **Created:** 2026-01-22

**Background:** RTK (Rust Token Killer) is a CLI proxy that sits between AI agents and system commands, intercepting verbose outputs and compressing them before they consume LLM context window tokens. Written in Rust as a single binary with zero dependencies, it reduces token consumption by 60-90% on common development commands.

**Problem it solves:** When AI agents run shell commands, the raw output often contains thousands of tokens of noise — ANSI codes, repetitive log lines, build metadata — that consume expensive context window space without adding useful information. RTK strips and compresses this output.

**Why another one?** Token cost is a concrete, measurable pain point for agent users, and RTK addresses it at the system level without requiring changes to the agent or the commands being run. Its Rust implementation adds negligible latency to the command pipeline.

---

## 45. [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
> FULL system prompts, internal tools & AI models of major AI coding tools

**Language:** N/A  |  **Stars:** 129730  |  **Forks:** 33055  |  **Best Score:** 3156  |  **Best Rank:** #14  |  **Days on chart:** 1/7  |  **Created:** 2025-03-05

**Background:** This repository collects the full system prompts, internal tool definitions, and model configurations used by major AI coding tools including Claude Code, Cursor, Devin, Windsurf, Codex, and over 25 others. With nearly 130,000 stars, it has become the go-to reference for understanding how commercial AI tools are configured.

**Problem it solves:** AI coding tools are largely opaque about their system prompts and internal tool configurations. This repository makes that information public, enabling developers to understand, compare, and learn from how different tools structure their AI interactions.

**Why another one?** It covers more tools than any competing resource (28+ as of this week's count) and is continuously updated as tools change. Its 130,000-star count reflects the broad developer interest in AI tool transparency.

---

## 46. [Scrapling](https://github.com/D4Vinci/Scrapling)
> An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

**Language:** Python  |  **Stars:** 26976  |  **Forks:** 1985  |  **Best Score:** 3147  |  **Best Rank:** #13  |  **Days on chart:** 1/7  |  **Created:** 2024-10-13

**Background:** Scrapling is a Python web scraping framework that adapts to website changes, handling everything from simple requests to full-scale crawls. It provides multi-language documentation and has accumulated nearly 27,000 stars since October 2024. The project recently added MCP integration for use with AI agents.

**Problem it solves:** Web scraping is fragile because websites change their HTML structure frequently. Scrapling adapts to these changes automatically, reducing the maintenance burden that makes traditional scraping brittle.

**Why another one?** Scrapling's adaptive approach — automatically adjusting to structural changes — differentiates it from static selector-based scrapers. Its recent MCP integration connects it to the AI agent ecosystem, allowing agents to scrape as a tool call.

---

## 47. [MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2)
> Automate the process of making money online.

**Language:** Python  |  **Stars:** 14944  |  **Forks:** 1502  |  **Best Score:** 3124  |  **Best Rank:** #18  |  **Days on chart:** 2/7  |  **Created:** 2024-02-12

**Background:** MoneyPrinterV2 is a Python application that automates online money-making workflows, primarily through automated content creation and publishing. It is a complete rewrite of the original MoneyPrinter project with a broader feature set and more modular architecture. Requires Python 3.12.

**Problem it solves:** Creating and publishing content at scale for monetization requires repetitive manual work across multiple platforms and tools. MoneyPrinterV2 automates the pipeline from content generation to publication.

**Why another one?** The V2 rewrite addresses the limitations of the original project with a modular architecture that supports a wider range of monetization strategies and content types.

---

## 48. [Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI)
> A pixel office for your OpenClaw: turn invisible work states into a cozy little space with characters, daily notes, and guest agents.

**Language:** HTML  |  **Stars:** 3785  |  **Forks:** 421  |  **Best Score:** 3118  |  **Best Rank:** #20  |  **Days on chart:** 2/7  |  **Created:** 2026-02-26

**Background:** Star Office UI is a pixel-art-style dashboard that visualizes AI assistant work states in real time. It shows which agents are active, what they are doing, and their recent history through animated pixel characters in a virtual office setting. It integrates deeply with OpenClaw and supports Chinese, English, and Japanese.

**Problem it solves:** AI assistants work invisibly in the background, making it hard to know their current status, workload, or recent activity. Star Office UI makes agent work states tangible through a charming pixel-art visualization.

**Why another one?** The gamification angle — turning agent status monitoring into a pixel office simulation with characters, decorations, and AI-generated room customization — is genuinely novel. It transforms a mundane monitoring task into something users want to look at.

---

## 49. [agentscope](https://github.com/agentscope-ai/agentscope)
> Build and run agents you can see, understand and trust.

**Language:** Python  |  **Stars:** 17869  |  **Forks:** 1583  |  **Best Score:** 3074  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2024-01-12

**Background:** AgentScope is a Python framework from Alibaba for building multi-agent applications with a focus on transparency and trust. It provides visual tools for understanding agent behavior, debugging workflows, and monitoring execution. With nearly 18,000 stars, it has grown into a mature platform with academic backing (arXiv paper) and an active roadmap.

**Problem it solves:** Multi-agent systems are notoriously difficult to debug and understand because interactions between agents are opaque. AgentScope provides visualization and monitoring tools that make agent behavior observable and trustworthy.

**Why another one?** The emphasis on observability ("agents you can see, understand and trust") distinguishes AgentScope from frameworks that optimize primarily for agent capability. Its visualization-first approach is critical for enterprise adoption where accountability matters.

---

## 50. [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)
> The Ultimate Collection of 1000+ Agentic Skills for Claude Code/Antigravity/Cursor.

**Language:** Python  |  **Stars:** 21559  |  **Forks:** 3753  |  **Best Score:** 3017  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2026-01-14

**Background:** This repository catalogs 1,234+ agentic skills compatible with Claude Code, Gemini CLI, Codex CLI, Cursor, GitHub Copilot, and more. It positions itself as a universal skill collection that works across multiple agent platforms, maintained with automated registry synchronization.

**Problem it solves:** Agent skills are scattered across platform-specific repositories and registries. This collection aggregates skills from multiple ecosystems into a single, cross-platform catalog with consistent categorization.

**Why another one?** The cross-platform compatibility claim (Claude Code, Gemini CLI, Codex, Cursor, Copilot, and others) distinguishes it from platform-specific collections. The automated sync mechanism keeps it current with upstream registries.

---

## 51. [AFFiNE](https://github.com/toeverything/AFFiNE)
> There can be more than Notion and Miro. AFFiNE is a next-gen knowledge base that brings planning, sorting and creating all together.

**Language:** TypeScript  |  **Stars:** 65229  |  **Forks:** 4554  |  **Best Score:** 3008  |  **Best Rank:** #12  |  **Days on chart:** 3/7  |  **Created:** 2022-07-31

**Background:** AFFiNE is a privacy-focused, local-first alternative to Notion and Miro that combines documents, whiteboards, and databases in a single application. With over 65,000 stars, it has established itself as one of the leading open-source knowledge management tools. Available as both a web app and desktop application.

**Problem it solves:** Notion and Miro require cloud accounts and store data on their servers. AFFiNE provides equivalent functionality — docs, kanban boards, whiteboards — with local-first data storage and optional sync.

**Why another one?** AFFiNE's local-first architecture means data stays on the user's device by default, addressing the privacy concerns that prevent some teams from using cloud-based alternatives. Its combined doc+whiteboard+database approach reduces tool sprawl.

---

## 52. [superset](https://github.com/superset-sh/superset)
> IDE for the AI Agents Era - Run an army of Claude Code, Codex, etc. on your machine

**Language:** TypeScript  |  **Stars:** 6327  |  **Forks:** 403  |  **Best Score:** 2989  |  **Best Rank:** #18  |  **Days on chart:** 3/7  |  **Created:** 2025-10-21

**Background:** Superset is a terminal application designed for running multiple coding agents simultaneously. It isolates each agent task in its own git worktree, monitors all agents from one interface, and provides built-in diff review tools. Currently available for macOS.

**Problem it solves:** Running multiple coding agents on different tasks requires switching between terminals, manually managing branch isolation, and tracking which agent needs attention. Superset provides a unified interface for parallel agent orchestration.

**Why another one?** The git worktree isolation strategy is particularly clever — each agent works on its own worktree, preventing merge conflicts and cross-contamination between concurrent tasks. The monitoring dashboard provides real-time visibility across all running agents.

---

## 53. [qmd](https://github.com/tobi/qmd)
> mini cli search engine for your docs, knowledge bases, meeting notes, whatever.

**Language:** TypeScript  |  **Stars:** 13649  |  **Forks:** 788  |  **Best Score:** 2933  |  **Best Rank:** #20  |  **Days on chart:** 1/7  |  **Created:** 2025-12-08

**Background:** QMD (Query Markup Documents) is an on-device search engine for personal documents, combining BM25 full-text search, vector semantic search, and LLM re-ranking — all running locally via node-llama-cpp with GGUF models. Created by tobi, it has accumulated over 13,000 stars since December 2025.

**Problem it solves:** Finding information across personal notes, meeting transcripts, and documentation requires remembering which file contains what. QMD indexes everything locally and supports both keyword and natural language queries with hierarchical context that improves LLM result selection.

**Why another one?** QMD's hierarchical context system — where metadata at the collection level flows down to sub-documents — is its key differentiator. This allows LLMs to make better contextual choices when selecting matching documents, a feature the author emphasizes as the key innovation.

---

## 54. [markitdown](https://github.com/microsoft/markitdown)
> Python tool for converting files and office documents to Markdown.

**Language:** Python  |  **Stars:** 90419  |  **Forks:** 5324  |  **Best Score:** 2926  |  **Best Rank:** #21  |  **Days on chart:** 2/7  |  **Created:** 2024-11-13

**Background:** MarkItDown is a Python utility from Microsoft's AutoGen team that converts various file formats (Office documents, PDFs, images, and more) to Markdown for use with LLMs. With over 90,000 stars, it has become a standard tool in the LLM data preparation pipeline. It now offers an MCP server for integration with Claude Desktop.

**Problem it solves:** LLMs work best with text input, but much of the world's information lives in binary formats — Word documents, PowerPoint slides, PDFs, images. MarkItDown converts these into clean Markdown that LLMs can process directly.

**Why another one?** MarkItDown's breadth of format support and its backing by the AutoGen team give it a reliability advantage over ad-hoc conversion scripts. Its MCP server integration positions it as a first-class tool for AI agent workflows.

---

## 55. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster.

**Language:** Shell  |  **Stars:** 75677  |  **Forks:** 6100  |  **Best Score:** 2924  |  **Best Rank:** #15  |  **Days on chart:** 4/7  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official agentic coding assistant that operates from the terminal. It executes routine tasks, explains complex code, handles git workflows, and can be tagged on GitHub for code review. With over 75,000 stars, it is one of the most popular developer tools in the AI coding space. Installation is now recommended via direct installer rather than npm.

**Problem it solves:** Developers spend significant time on routine coding tasks — writing boilerplate, understanding unfamiliar code, managing git operations. Claude Code automates these through natural language commands in the terminal, with full codebase context.

**Why another one?** As Anthropic's first-party coding agent, Claude Code benefits from direct model integration and rapid feature iteration. Its four-day chart presence this week reflects sustained daily use rather than novelty-driven interest.

---

## 56. [MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles)
> A certain block game

**Language:** C++  |  **Stars:** 4286  |  **Forks:** 808  |  **Best Score:** 2866  |  **Best Rank:** #22  |  **Days on chart:** 2/7  |  **Created:** 2026-03-01

**Background:** MinecraftConsoles contains the source code of Minecraft Legacy Console Edition v1.6.0560.0 (TU19) with fixes and improvements applied. It supports Windows builds through Visual Studio 2022 and adds keyboard/mouse input, fullscreen mode, LAN multiplayer, and adaptive screen resolution. Released March 1, it immediately drew community attention.

**Problem it solves:** The Legacy Console Edition of Minecraft was discontinued and is no longer officially maintained. This project preserves and improves that version, allowing players to run it on modern hardware with features like keyboard/mouse support and LAN multiplayer.

**Why another one?** The Legacy Console Edition has a dedicated following that prefers its gameplay mechanics and UI to later versions. This project is notable for being a community-maintained source port rather than a mod, enabling contributions and fixes that the discontinued official version cannot receive.

---

## 57. [Flowise](https://github.com/FlowiseAI/Flowise)
> Build AI Agents, Visually

**Language:** TypeScript  |  **Stars:** 50527  |  **Forks:** 23896  |  **Best Score:** 2858  |  **Best Rank:** #19  |  **Days on chart:** 2/7  |  **Created:** 2023-03-31

**Background:** Flowise is a visual builder for AI agents that provides a drag-and-drop interface for constructing agent workflows. With over 50,000 stars and nearly 24,000 forks, it has become one of the most popular no-code/low-code AI development tools. It supports self-hosting and cloud deployment.

**Problem it solves:** Building AI agent workflows requires writing code to connect LLMs, tools, memory systems, and data sources. Flowise replaces this with a visual canvas where components are connected graphically, making agent development accessible to non-programmers.

**Why another one?** Flowise's visual approach lowers the barrier to agent development significantly. Its massive fork count (23,896) indicates widespread customization and deployment, suggesting it has become infrastructure rather than just a tool.

---

## 58. [ReMe](https://github.com/agentscope-ai/ReMe)
> ReMe: Memory Management Kit for Agents - Remember Me, Refine Me.

**Language:** Python  |  **Stars:** 2088  |  **Forks:** 156  |  **Best Score:** 2856  |  **Best Rank:** #20  |  **Days on chart:** 1/7  |  **Created:** 2024-08-29

**Background:** ReMe is a memory management toolkit for AI agents from the AgentScope team, providing mechanisms for agents to remember context across sessions and refine their understanding over time. It integrates with the broader AgentScope ecosystem and is available as a pip-installable Python package.

**Problem it solves:** AI agents forget everything between sessions, requiring users to re-establish context each time. ReMe provides structured memory storage and retrieval that persists across sessions, allowing agents to build cumulative understanding.

**Why another one?** ReMe focuses exclusively on the memory problem rather than trying to be a full agent framework. This specialization allows deeper treatment of memory storage, retrieval, and refinement patterns than general-purpose agent frameworks provide.

---

## 59. [fara](https://github.com/microsoft/fara)
> Fara-7B: An Efficient Agentic Model for Computer Use

**Language:** Python  |  **Stars:** 4383  |  **Forks:** 400  |  **Best Score:** 2850  |  **Best Rank:** #24  |  **Days on chart:** 1/7  |  **Created:** 2025-10-29

**Background:** Fara-7B is Microsoft's first agentic small language model (SLM) designed specifically for computer use. With only 7 billion parameters, it achieves state-of-the-art performance within its size class for Computer Use Agent (CUA) tasks — clicking, typing, navigating desktop applications. It runs locally and is available on Hugging Face and Azure Foundry.

**Problem it solves:** Computer use agents based on large models are expensive and slow. Fara-7B provides comparable capability in a model small enough to run locally, enabling autonomous desktop interaction without cloud API costs.

**Why another one?** At 7 billion parameters, Fara-7B is dramatically smaller than competing CUA models while remaining competitive on benchmarks. The WebTailBench dataset released alongside it provides a standardized evaluation for computer use agents.

---

## 60. [seomachine](https://github.com/TheCraigHewitt/seomachine)
> A specialized Claude Code workspace for creating long-form, SEO-optimized blog content for any business.

**Language:** Python  |  **Stars:** 2399  |  **Forks:** 400  |  **Best Score:** 2761  |  **Best Rank:** #21  |  **Days on chart:** 3/7  |  **Created:** 2025-10-29

**Background:** SEO Machine is a Claude Code workspace that provides custom commands (/research, /write, /analyze, /optimize), specialized agents for content analysis and SEO optimization, and 26 marketing skills. It integrates with Google Analytics 4, Google Search Console, and DataForSEO for real-time performance insights.

**Problem it solves:** Creating SEO-optimized content requires research, keyword analysis, content structuring, meta element creation, and internal linking — a multi-step workflow that is tedious when done manually. SEO Machine automates this through specialized Claude Code commands and agents.

**Why another one?** SEO Machine packages domain-specific SEO knowledge (keyword clustering, search intent detection, readability scoring, SEO quality rating) into Claude Code's workflow, going beyond generic content generation to produce content that is specifically engineered to rank.

---

## 61. [scrapy](https://github.com/scrapy/scrapy)
> Scrapy, a fast high-level web crawling & scraping framework for Python.

**Language:** Python  |  **Stars:** 60646  |  **Forks:** 11344  |  **Best Score:** 2756  |  **Best Rank:** #16  |  **Days on chart:** 1/7  |  **Created:** 2010-02-22

**Background:** Scrapy is one of the longest-running and most popular Python web scraping frameworks, with over 60,000 stars and a history dating back to 2010. It provides a complete framework for extracting data from websites, including request scheduling, response parsing, data pipelines, and middleware support.

**Problem it solves:** Building a reliable web scraper requires handling concurrency, rate limiting, retry logic, data extraction, and output formatting. Scrapy provides all of these out of the box with a well-documented, extensible architecture.

**Why another one?** Scrapy's maturity, documentation, and ecosystem make it the default choice for production web scraping in Python. Its chart appearance this week likely reflects renewed interest driven by the AI data collection trend.

---

## 62. [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
> The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**Language:** JavaScript  |  **Stars:** 69024  |  **Forks:** 8618  |  **Best Score:** 2739  |  **Best Rank:** #20  |  **Days on chart:** 3/7  |  **Created:** 2026-01-18

**Background:** everything-claude-code is a comprehensive optimization system for AI coding agents, covering skills, "instincts" (automatic behavioral patterns), memory management, and security hardening. With nearly 69,000 stars, it has become one of the most popular meta-tools for agent optimization. It includes npm packages (ecc-universal, ecc-agentshield) and a GitHub App.

**Problem it solves:** Default agent configurations leave performance on the table. This system provides optimized skills, behavioral patterns, and security measures that make agents more effective, safer, and more consistent across coding sessions.

**Why another one?** The "instincts" concept — automatic behavioral patterns that fire without explicit invocation — is a novel contribution to agent optimization. The multi-platform support (Claude Code, Codex, Cursor, and others) and npm-based distribution make it broadly applicable.

---

## 63. [ClawRouter](https://github.com/BlockRunAI/ClawRouter)
> The agent-native LLM router for OpenClaw. 41+ models, <1ms routing, USDC payments on Base & Solana via x402.

**Language:** TypeScript  |  **Stars:** 5282  |  **Forks:** 405  |  **Best Score:** 2672  |  **Best Rank:** #20  |  **Days on chart:** 3/7  |  **Created:** 2026-02-03

**Background:** ClawRouter is an LLM routing system designed for OpenClaw that scores requests across 15 dimensions and routes them to the optimal model among 41+ options in under 1 millisecond. It uses non-custodial USDC payments on Base and Solana via the x402 protocol, eliminating the need for individual API keys.

**Problem it solves:** Using multiple LLM providers requires managing separate API keys, billing relationships, and routing logic. ClawRouter consolidates this into a single endpoint with automatic model selection and cryptocurrency-based payments.

**Why another one?** The combination of sub-millisecond local routing, 15-dimension model scoring, and crypto-native payments (no API keys needed) targets the OpenClaw ecosystem's specific needs. The x402 payment protocol integration is particularly notable for enabling per-request billing without vendor accounts.

---

## 64. [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
> Claude Code Skills and 500+ agent skills from official dev teams and the community, compatible with Codex, Antigravity, Gemini CLI, Cursor and others.

**Language:** N/A  |  **Stars:** 10076  |  **Forks:** 875  |  **Best Score:** 2629  |  **Best Rank:** #10  |  **Days on chart:** 1/7  |  **Created:** 2025-10-28

**Background:** Also maintained by VoltAgent, this repository is a curated collection of 549+ agent skills from official development teams and the community. Unlike bulk-generated collections, it focuses on skills created and used by actual engineering teams, compatible with Claude Code, Codex, Antigravity, Gemini CLI, and Cursor.

**Problem it solves:** Separating high-quality, team-tested skills from mass-generated ones requires manual curation. This collection applies editorial judgment to surface skills that have been validated through actual use.

**Why another one?** The editorial curation standard ("real-world Agent Skills created and used by actual engineering teams, not mass AI-generated") distinguishes it from larger but less curated collections. Quality over quantity is the explicit design choice.

---

## 65. [ui](https://github.com/shadcn-ui/ui)
> A set of beautifully-designed, accessible components and a code distribution platform.

**Language:** TypeScript  |  **Stars:** 108588  |  **Forks:** 8067  |  **Best Score:** 2572  |  **Best Rank:** #11  |  **Days on chart:** 1/7  |  **Created:** 2023-01-04

**Background:** shadcn/ui is a component library and code distribution platform that provides beautifully designed, accessible React components. With over 108,000 stars, it has become one of the most popular UI component systems in the React ecosystem. Unlike traditional component libraries, shadcn/ui is designed to be copied and customized rather than imported as a dependency.

**Problem it solves:** Traditional component libraries are difficult to customize deeply because styles and behavior are encapsulated. shadcn/ui provides components as source code that developers copy into their projects and own completely.

**Why another one?** The copy-and-own distribution model is the key differentiator. Instead of fighting a library's abstractions, developers get full control of the component code from day one. Its 108,000-star count validates this approach.

---

## 66. [openclaw-studio](https://github.com/grp06/openclaw-studio)
> A clean web dashboard for OpenClaw. Connect your Gateway, manage agents, and ship faster.

**Language:** TypeScript  |  **Stars:** 1532  |  **Forks:** 227  |  **Best Score:** 2550  |  **Best Rank:** #17  |  **Days on chart:** 1/7  |  **Created:** 2026-01-28

**Background:** OpenClaw Studio is a web dashboard that connects to an OpenClaw Gateway and provides a visual interface for managing agents, viewing conversations, handling approvals, and configuring jobs. It runs as a local web app and connects to either local or cloud-hosted gateways.

**Problem it solves:** OpenClaw's command-line interface, while powerful, lacks the visual overview needed to manage multiple agents, review conversation history, and handle approval workflows efficiently. Studio provides that graphical layer.

**Why another one?** As a purpose-built dashboard for OpenClaw, it provides features (agent management, approval workflows, cost tracking) that generic admin panels cannot. Its Tailscale integration for remote access shows thoughtful operational design.

---

## 67. [hello-agents](https://github.com/datawhalechina/hello-agents)
> From zero to building intelligent agents — principles and practices tutorial

**Language:** Python  |  **Stars:** 26281  |  **Forks:** 2949  |  **Best Score:** 2511  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2025-09-07

**Background:** Hello-Agents is a systematic intelligent agent learning tutorial from the Datawhale community, China's leading open-source AI education organization. It covers agent principles and practical implementation from fundamentals to advanced topics. With over 26,000 stars, it has become one of the primary Chinese-language resources for learning agent development.

**Problem it solves:** Systematic, practical tutorials for building agent systems are scarce, especially in Chinese. Hello-Agents provides a structured curriculum that balances theory with hands-on implementation.

**Why another one?** The Datawhale community's educational methodology — combining theoretical foundations with practical exercises and community support — produces a learning experience that isolated blog posts and documentation cannot match. Its Chinese-first approach serves an underserved audience.

---

## 68. [codebuff](https://github.com/CodebuffAI/codebuff)
> Generate code from the terminal!

**Language:** TypeScript  |  **Stars:** 4143  |  **Forks:** 473  |  **Best Score:** 2484  |  **Best Rank:** #23  |  **Days on chart:** 2/7  |  **Created:** 2024-07-09

**Background:** Codebuff is an open-source AI coding assistant that uses a multi-agent architecture: separate agents for file picking, planning, editing, and reviewing work together on each task. It claims a 61% pass rate on 175+ coding tasks, compared to 53% for Claude Code on the same eval suite.

**Problem it solves:** Single-model coding tools often make inaccurate edits because they try to handle context understanding, planning, editing, and review in a single inference pass. Codebuff decomposes this into specialized agents that each focus on one aspect.

**Why another one?** The multi-agent architecture (file picker, planner, editor, reviewer) is Codebuff's key claim. By specializing each stage, it achieves better context understanding and fewer errors than monolithic approaches, at least on its published eval suite.

---

## 69. [skills](https://github.com/anthropics/skills)
> Public repository for Agent Skills

**Language:** Python  |  **Stars:** 88119  |  **Forks:** 9339  |  **Best Score:** 2479  |  **Best Rank:** #24  |  **Days on chart:** 2/7  |  **Created:** 2025-09-22

**Background:** This is Anthropic's official public repository of skills for Claude, implementing the Agent Skills standard from agentskills.io. It contains demonstration skills ranging from creative applications (art, music, design) to technical tasks (testing, MCP server generation) to enterprise workflows (communications, branding). With over 88,000 stars, it is one of the most popular Anthropic repositories.

**Problem it solves:** Claude's skill system allows custom task-specific guidance, but creating skills from scratch requires understanding the SKILL.md format and best practices. This repository provides reference implementations across multiple domains.

**Why another one?** As the official Anthropic skills repository, it defines the gold standard for skill quality and structure. Each skill is self-contained with its own SKILL.md, making it both a usage resource and a template for custom skill development.

---

## 70. [page-agent](https://github.com/alibaba/page-agent)
> JavaScript in-page GUI agent. Control web interfaces with natural language.

**Language:** TypeScript  |  **Stars:** 2399  |  **Forks:** 194  |  **Best Score:** 2450  |  **Best Rank:** #13  |  **Days on chart:** 1/7  |  **Created:** 2025-09-23

**Background:** Page Agent by Alibaba is a JavaScript library that embeds a GUI agent directly inside web pages, allowing users to control web interfaces through natural language commands. It runs as an in-page script rather than a browser extension or external tool, providing direct DOM access for UI automation.

**Problem it solves:** Existing browser automation approaches (Playwright, Puppeteer, browser extensions) operate outside the page, requiring serialization of page state. Page Agent runs inside the page, giving it direct access to the DOM, JavaScript context, and framework state.

**Why another one?** The in-page approach eliminates the serialization overhead and state synchronization problems that plague external automation tools. Being inside the page means Page Agent can interact with single-page applications and dynamic content that external tools struggle with.

---

## 71. [baoyu-skills](https://github.com/JimLiu/baoyu-skills)
> Skills shared by Baoyu for improving daily work efficiency with Claude Code.

**Language:** TypeScript  |  **Stars:** 8006  |  **Forks:** 883  |  **Best Score:** 2411  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2026-01-13

**Background:** baoyu-skills is a collection of productivity-focused skills for Claude Code shared by developer Baoyu (JimLiu). It covers image generation, markdown-to-HTML conversion, and other daily workflow optimizations. The skills can be installed via npx, the Claude Code plugin marketplace, or published individually to ClawHub.

**Problem it solves:** Common productivity tasks like generating images, converting document formats, and managing content require switching between tools. These skills bring those capabilities directly into the Claude Code workflow.

**Why another one?** The skills are curated from one developer's daily workflow, ensuring they solve real rather than hypothetical problems. The multi-distribution support (npx, plugin marketplace, ClawHub) makes installation flexible.

---

## 72. [ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5)
> The most powerful local music generation model that outperforms most commercial alternatives.

**Language:** Python  |  **Stars:** 7459  |  **Forks:** 830  |  **Best Score:** 2358  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2025-09-04

**Background:** ACE-Step 1.5 is an open-source music generation foundation model that claims commercial-grade quality while running on consumer hardware. It generates full songs in under 2 seconds on an A100 and under 10 seconds on an RTX 3090, requiring less than 4GB of VRAM. It supports Mac, AMD, Intel, and CUDA devices.

**Problem it solves:** Commercial music generation services are expensive and process audio on remote servers. ACE-Step 1.5 provides equivalent quality locally, with the speed and memory efficiency to run on consumer GPUs.

**Why another one?** The combination of commercial-grade quality, sub-10-second generation on consumer GPUs, and under 4GB VRAM requirement sets a new bar for local music generation. Multi-platform support (including Mac and AMD) broadens accessibility beyond NVIDIA-only alternatives.

---

## 73. [goose](https://github.com/block/goose)
> an open source, extensible AI agent that goes beyond code suggestions

**Language:** Rust  |  **Stars:** 32693  |  **Forks:** 3006  |  **Best Score:** 2316  |  **Best Rank:** #22  |  **Days on chart:** 1/7  |  **Created:** 2024-08-23

**Background:** Goose by Block (formerly Square) is a local, extensible AI agent that automates engineering tasks end-to-end — building projects from scratch, writing and executing code, debugging failures, and interacting with external APIs. Written in Rust, it supports any LLM, multi-model configuration, and MCP server integration. Available as both desktop app and CLI.

**Problem it solves:** Most AI coding tools stop at code suggestions. Goose executes complete workflows autonomously: prototyping, refining code, orchestrating pipelines, and interacting with external services — without requiring human supervision at each step.

**Why another one?** Block's corporate backing provides stability, and the Rust implementation delivers performance for long-running autonomous tasks. The multi-model configuration allows optimizing different workflow stages for cost and capability.

---

## 74. [daytona](https://github.com/daytonaio/daytona)
> Daytona is a Secure and Elastic Infrastructure for Running AI-Generated Code

**Language:** TypeScript  |  **Stars:** 63165  |  **Forks:** 5072  |  **Best Score:** 2286  |  **Best Rank:** #16  |  **Days on chart:** 1/7  |  **Created:** 2024-02-06

**Background:** Daytona provides secure, elastic infrastructure for executing AI-generated code. With over 63,000 stars, it has evolved from a development environment manager into a sandboxed execution platform specifically designed for the AI code generation era. Licensed under AGPL-3.

**Problem it solves:** AI-generated code needs to be executed somewhere safe before being trusted in production. Daytona provides isolated, scalable environments where generated code can run, be tested, and be validated without risking production infrastructure.

**Why another one?** Daytona's evolution from dev environments to AI code execution infrastructure reflects a genuine market shift. Its AGPL license ensures the platform remains open source even when deployed as a service.

---

## 75. [terraink](https://github.com/yousifamanuel/terraink)
> TerraInk: The Cartographic Poster Engine that creates unique and customizable map posters

**Language:** TypeScript  |  **Stars:** 891  |  **Forks:** 84  |  **Best Score:** 2104  |  **Best Rank:** #17  |  **Days on chart:** 1/7  |  **Created:** 2026-02-10

**Background:** TerraInk is a web application for creating customizable cartographic posters — stylized map prints of any location. It provides design controls for typography, color schemes, map styles, and layout, outputting print-ready poster files. Built with Bun and Vite.

**Problem it solves:** Creating custom map posters traditionally requires graphic design skills and GIS software. TerraInk provides a web interface where anyone can design professional-looking map posters by selecting a location and customizing visual parameters.

**Why another one?** TerraInk's focus on print quality and design customization distinguishes it from map screenshot tools. Its open-source nature allows self-hosting, eliminating the per-poster fees that commercial map poster services charge.

---

## 76. [daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)
> LLM-driven A/H/US stock smart analyzer with multi-source data + real-time news + Gemini decision dashboard + multi-channel push

**Language:** Python  |  **Stars:** 17898  |  **Forks:** 18310  |  **Best Score:** 2083  |  **Best Rank:** #18  |  **Days on chart:** 1/7  |  **Created:** 2026-01-10

**Background:** daily_stock_analysis is an AI-powered stock analysis system covering A-shares (China), H-shares (Hong Kong), and US stocks. It combines multiple data sources with real-time news aggregation and Gemini-based analysis to produce daily "decision dashboards" pushed to WeChat Work, Feishu, Telegram, and email. Designed to run on GitHub Actions for zero-cost operation.

**Problem it solves:** Monitoring multiple stock markets across different time zones requires aggregating data from multiple sources, analyzing news impact, and producing actionable summaries. This system automates the entire pipeline, delivering daily analysis to the user's preferred messaging platform.

**Why another one?** The cross-market coverage (A/H/US), zero-cost GitHub Actions deployment, and multi-channel push notification support make it uniquely suited for Chinese investors who track multiple markets. Its fork count (18,310) actually exceeds its star count (17,898), suggesting heavy customization.

---

## 77. [Siftly](https://github.com/viperrcrypto/Siftly)
> Local Twitter/X bookmark organizer with AI categorization and mindmap visualization

**Language:** TypeScript  |  **Stars:** 1279  |  **Forks:** 102  |  **Best Score:** 2080  |  **Best Rank:** #19  |  **Days on chart:** 1/7  |  **Created:** 2026-03-04

**Background:** Siftly is a self-hosted Twitter/X bookmark manager that runs a 4-stage AI pipeline (import, entity extraction, vision analysis, categorization) on saved bookmarks. It turns bookmarks into a searchable, categorized knowledge base with mindmap visualization. All data stays local; only AI API calls leave the machine.

**Problem it solves:** Twitter/X bookmarks accumulate rapidly but lack any organization, search, or categorization capabilities. Siftly transforms this unstructured collection into a searchable knowledge base with AI-generated categories, entity extraction, and visual exploration.

**Why another one?** The 4-stage pipeline — especially the vision analysis step that reads text and context from images, GIFs, and video thumbnails — extracts information that text-only bookmark tools miss. The mindmap visualization provides a unique exploration interface.

---

## 78. [free-for-dev](https://github.com/ripienaar/free-for-dev)
> A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev

**Language:** HTML  |  **Stars:** 119167  |  **Forks:** 12312  |  **Best Score:** 2079  |  **Best Rank:** #20  |  **Days on chart:** 1/7  |  **Created:** 2015-03-18

**Background:** free-for-dev is a community-curated list of SaaS, PaaS, and IaaS services with free tiers, focused on infrastructure and DevOps tools. With over 119,000 stars and contributions from 1,600+ people, it is the definitive index of free-tier services for developers. Services must offer permanent free tiers (not just trials).

**Problem it solves:** Finding which infrastructure services offer genuine free tiers (not time-limited trials) requires checking each vendor's pricing page individually. This list consolidates that information with consistent criteria.

**Why another one?** It is the original and most comprehensive resource of its kind, maintained since 2015 with strict inclusion criteria (must be a permanent free tier, must include TLS, not just a trial). Its periodic chart appearances reflect waves of new developers discovering it.

---

## 79. [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)
> An AI Hedge Fund Team

**Language:** Python  |  **Stars:** 47031  |  **Forks:** 8174  |  **Best Score:** 2074  |  **Best Rank:** #21  |  **Days on chart:** 1/7  |  **Created:** 2024-11-29

**Background:** ai-hedge-fund is a proof-of-concept AI trading system that uses multiple specialized agents modeled after famous investors — Warren Buffett, Charlie Munger, Cathie Wood, Michael Burry, and others. Each agent applies its namesake's investment philosophy to analyze stocks, and a portfolio management agent synthesizes their recommendations. Explicitly educational, not for real trading.

**Problem it solves:** Understanding different investment philosophies and how they would evaluate the same stock requires deep knowledge of each approach. This system makes those philosophies executable, allowing users to see how different investment frameworks reach different conclusions.

**Why another one?** The multi-agent approach with personality-driven analysis (each agent embodies a specific investor's philosophy) is both educational and architecturally interesting. Its 47,000 stars suggest broad appeal beyond the trading community.

---

## 80. [aipyapp](https://github.com/knownsec/aipyapp)
> AI-Powered Python & Python-Powered AI (Python-Use)

**Language:** HTML  |  **Stars:** 3861  |  **Forks:** 378  |  **Best Score:** 2016  |  **Best Rank:** #23  |  **Days on chart:** 1/7  |  **Created:** 2025-04-06

**Background:** Python-Use by Knownsec proposes a new AI agent paradigm where the LLM is given direct access to a Python interpreter, creating a Task-Plan-Code-Execute-Feedback loop. It positions itself as "Agent 2.0," arguing that traditional function-calling and MCP-based agents are "prosthetics" that create unnecessary indirection.

**Problem it solves:** Traditional AI agents rely on pre-defined tools, function calling interfaces, and plugin architectures that require developer effort to set up and maintain. Python-Use gives the LLM the full Python environment, letting it write and execute arbitrary code to accomplish tasks.

**Why another one?** The philosophical argument — that giving LLMs a Python interpreter is more natural and capable than building tool-calling interfaces — is a meaningful architectural bet. If correct, it eliminates the need for most of the tool/plugin infrastructure that dominates the current agent ecosystem.

---

## 81. [mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)
> Open-source curriculum introducing Model Context Protocol (MCP) through real-world, cross-language examples.

**Language:** Jupyter Notebook  |  **Stars:** 15163  |  **Forks:** 4918  |  **Best Score:** 1960  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2025-04-04

**Background:** mcp-for-beginners is Microsoft's open-source curriculum for learning the Model Context Protocol (MCP), providing examples in .NET, Java, TypeScript, JavaScript, Rust, and Python. It covers session setup, tool registration, resource management, and service orchestration through practical, cross-language exercises.

**Problem it solves:** MCP is becoming a standard for AI tool integration, but learning it requires understanding both the protocol specification and language-specific implementation patterns. This curriculum provides structured, hands-on learning across six programming languages.

**Why another one?** The cross-language approach (6 languages) ensures developers can learn MCP in their preferred ecosystem. Microsoft's educational methodology — proven through their "for beginners" series — provides a structured learning path that protocol documentation alone does not.

---

## 82. [production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course)
> The Mother of AI Project — Phase 1 RAG Systems: arXiv Paper Curator

**Language:** Python  |  **Stars:** 3767  |  **Forks:** 1010  |  **Best Score:** 1931  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2025-08-06

**Background:** This course teaches production-grade RAG (Retrieval-Augmented Generation) systems through building an arXiv paper curator. It follows a professional path: master keyword search first, then add semantic search, then LLM re-ranking — rather than jumping directly to vector databases. Currently in week 7 with advanced features.

**Problem it solves:** Most RAG tutorials skip the fundamentals and jump to vector search, leaving developers without the understanding needed to debug and optimize production systems. This course builds up from BM25 keyword search through semantic search to LLM re-ranking, teaching each layer's strengths and limitations.

**Why another one?** The progressive complexity approach (keyword search before vector search before LLM re-ranking) and the real-world application (arXiv paper curation) provide a learning experience grounded in production engineering rather than toy examples.

---

## 83. [system-design-primer](https://github.com/donnemartin/system-design-primer)
> Learn how to design large-scale systems. Prep for the system design interview.

**Language:** Python  |  **Stars:** 338012  |  **Forks:** 54751  |  **Best Score:** 1784  |  **Best Rank:** #25  |  **Days on chart:** 1/7  |  **Created:** 2017-02-26

**Background:** system-design-primer is one of the most-starred repositories on GitHub at 338,000 stars, providing comprehensive material for learning large-scale system design. It covers core concepts (CAP theorem, consistent hashing, database sharding) and includes Anki flashcards for interview preparation. Available in 17+ languages.

**Problem it solves:** System design interviews require broad knowledge across distributed systems, databases, caching, load balancing, and more. This repository provides structured study material with diagrams, tradeoff analysis, and flashcards in a single location.

**Why another one?** It has been the definitive system design study resource since 2017, and no competitor has matched its depth, breadth, and community-driven translations. Its chart appearance reflects its evergreen relevance as an interview preparation resource.

---

> **Week's theme:** The agent infrastructure stack continued to stratify, with Google, OpenAI, and Anthropic shipping first-party tooling (gws CLI, Symphony, Claude Code skills) while the open-source ecosystem raced to fill gaps in agent orchestration, browser automation, memory management, and cross-platform skill distribution around the dominant OpenClaw platform.
