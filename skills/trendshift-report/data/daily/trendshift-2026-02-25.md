# Trendshift Report — 2026-02-25
**Total:** 25 repositories

---

## 1. [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
> Full collection of system prompts, internal tools, and AI models from Augment Code, Claude Code, Cursor, Devin AI, Windsurf, Replit, and dozens more

**Language:** -  |  **Stars:** 129,187  |  **Forks:** 32,952  |  **Score:** 20,768  |  **Created:** 2025-03-05

**Background:** This repository is the largest community-maintained archive of leaked and reverse-engineered system prompts from major AI coding and productivity tools. Started in March 2025, it covers over two dozen products including Claude Code, Cursor, Devin AI, Windsurf, Kiro, Lovable, Manus, and v0. At nearly 130,000 stars it functions as a living encyclopedia of how AI tools are instructed to behave.

**Problem it solves:** AI tool makers keep their system prompts proprietary, making it difficult to understand how these tools are constrained, what capabilities they expose, and how different vendors approach the same design decisions. This repository centralizes that knowledge for researchers, competitors, and power users.

**Why another one?** The repository holds the top spot for a second consecutive day because its scope continuously expands with each new AI tool launch or prompt extraction. It has become the de facto monitoring station for the AI tooling industry, and no comparable alternative has emerged.

---

## 2. [Scrapling](https://github.com/D4Vinci/Scrapling)
> An adaptive web scraping framework that handles everything from a single request to a full-scale crawl

**Language:** Python  |  **Stars:** 25,289  |  **Forks:** 1,834  |  **Score:** 7,745  |  **Created:** 2024-10-13

**Background:** Scrapling is a Python web scraping framework by D4Vinci that handles anti-bot measures, dynamic content rendering, and large-scale crawling through a unified adaptive API. Its adaptive selector system can survive page redesigns without breaking, and it integrates stealth browser automation natively. It has accumulated over 25,000 stars since October 2024.

**Problem it solves:** Modern web scraping requires dealing with JavaScript-rendered pages, CAPTCHAs, rate limiting, fingerprint detection, and constantly changing page structures. Most scraping libraries handle only a subset of these challenges. Scrapling bundles anti-detection, headless browser management, and adaptive selectors into one framework.

**Why another one?** Scrapling was built from the ground up for the modern anti-bot landscape rather than being retrofitted onto older architectures. Its MCP integration also positions it for use by AI agents that need autonomous web browsing and data extraction, a use case that legacy scraping libraries were never designed for.

---

## 3. [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
> A comprehensive collection of Agent Skills for context engineering, multi-agent architectures, and production agent systems

**Language:** Python  |  **Stars:** 13,540  |  **Forks:** 1,042  |  **Score:** 5,473  |  **Created:** 2025-12-21

**Background:** This repository by Murat Can Koylan provides agent skills focused on context engineering -- the discipline of managing what information enters an LLM's context window. It covers multi-agent architectures, production agent system patterns, and strategies for effective context management, all packaged as installable skills for coding agents.

**Problem it solves:** Context engineering is distinct from prompt engineering: rather than crafting better instructions, it addresses the holistic curation of all information that enters the model's limited attention window. As agent systems scale from single-turn interactions to complex multi-step workflows, context management becomes the primary bottleneck.

**Why another one?** The jump from rank 8 to rank 3 reflects growing recognition that context engineering is a distinct discipline. While other skill collections cover broad task categories, this one targets the meta-problem of context management -- teaching agents how to manage their own context budgets and coordinate information flow across multi-agent systems.

---

## 4. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework and software development methodology that works

**Language:** Shell  |  **Stars:** 73,211  |  **Forks:** 5,624  |  **Score:** 5,366  |  **Created:** 2025-10-09

**Background:** Superpowers is Jesse Vincent's composable skills framework that plugs into Claude Code, Cursor, Codex, and OpenCode, enforcing a structured development workflow: requirements gathering, spec approval in reviewable chunks, implementation planning, then subagent-driven TDD with two-stage code review. At over 73,000 stars, it remains one of the most adopted agent methodology layers.

**Problem it solves:** Coding agents without guardrails skip planning, ignore tests, and drift from original intent during long sessions. Superpowers imposes mandatory spec approval, red-green-refactor TDD enforcement, and plan checkpoints to keep autonomous agents on track.

**Why another one?** Superpowers is not a coding agent but a methodology layer that works across multiple agents. Its sustained trending reflects the growing consensus that agent capability alone is insufficient -- structured workflows are necessary to channel that capability into reliable, reviewable outputs.

---

## 5. [skills](https://github.com/huggingface/skills)
> Hugging Face Skills for AI/ML tasks like dataset creation, model training, and evaluation

**Language:** Python  |  **Stars:** 8,521  |  **Forks:** 503  |  **Score:** 4,396  |  **Created:** 2025-11-24

**Background:** Hugging Face Skills is the official repository of agent skill definitions for AI and ML workflows from Hugging Face. The skills follow the standardized Agent Skill format and are interoperable with Claude Code, Codex, Gemini CLI, and Cursor. Each skill is a self-contained folder packaging instructions, scripts, and resources for an AI agent to execute ML tasks.

**Problem it solves:** Setting up ML workflows involves significant boilerplate and domain knowledge. These skills package the necessary scripts and instructions into self-contained folders that an AI agent can load and execute, turning multi-step ML workflows into single-command agent tasks.

**Why another one?** Hugging Face's position as the dominant open-source ML platform makes their skills uniquely authoritative for ML tasks. The skills have direct access to the Hugging Face ecosystem -- Hub, Transformers, and Datasets libraries -- providing integration depth that third-party skill authors cannot match.

---

## 6. [SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB)
> Development at the speed of light

**Language:** Rust  |  **Stars:** 22,961  |  **Forks:** 867  |  **Score:** 4,256  |  **Created:** 2023-06-17

**Background:** SpacetimeDB by Clockwork Labs is a database designed for multiplayer games and real-time applications. Written in Rust, it combines a relational database with application server logic, allowing developers to write server-side code that runs directly inside the database as stored procedures. The project has grown to nearly 23,000 stars since June 2023.

**Problem it solves:** Building real-time multiplayer systems traditionally requires separate database, application server, and networking layers, each with its own latency characteristics and consistency guarantees. SpacetimeDB collapses these layers by running application logic inside the database, eliminating network round-trips between the app server and the data layer and providing transactional guarantees over game state.

**Why another one?** Unlike general-purpose databases adapted for gaming (like using Redis for game state), SpacetimeDB was purpose-built for the multiplayer use case from day one. Its stored-procedure-like execution model, where game logic runs inside the database engine, provides latency and consistency properties that a separate app-server-plus-database architecture cannot achieve.

---

## 7. [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
> The Zero-Server Code Intelligence Engine -- a client-side knowledge graph creator with a built-in Graph RAG Agent

**Language:** TypeScript  |  **Stars:** 10,745  |  **Forks:** 1,312  |  **Score:** 4,134  |  **Created:** 2025-08-02

**Background:** GitNexus is a browser-based code intelligence tool that generates interactive knowledge graphs from GitHub repositories or ZIP files, running entirely client-side with no server component. It builds a navigable graph of code relationships queryable through a built-in Graph RAG agent. The jump from rank 23 to rank 7 signals accelerating adoption.

**Problem it solves:** Understanding relationships within a large codebase typically requires cloning the repository and navigating files locally. GitNexus generates a visual knowledge graph directly in the browser, making code exploration accessible without any local setup or server-side processing.

**Why another one?** The zero-server architecture means no code is sent to external servers, addressing privacy concerns that prevent teams from using cloud-based code intelligence tools. The built-in Graph RAG agent combines visual graph exploration with natural-language querying, offering a dual-modality interface that neither static graph tools nor pure chat-based code assistants provide.

---

## 8. [openclaw](https://github.com/openclaw/openclaw)
> Your own personal AI assistant. Any OS. Any Platform. The lobster way.

**Language:** TypeScript  |  **Stars:** 275,394  |  **Forks:** 52,562  |  **Score:** 4,106  |  **Created:** 2025-11-24

**Background:** OpenClaw is the most-starred personal AI assistant on GitHub with over 275,000 stars. Built in TypeScript, it runs on every major platform and provides a fully open, user-controlled alternative to closed-source assistants. Its skills-based extensibility system has spawned a massive third-party ecosystem of thousands of community-built skills.

**Problem it solves:** Closed-source AI assistants control user data, limit customization, and restrict integrations. OpenClaw provides a self-hosted alternative where users own their data, install community skills for any use case, and run the assistant on any platform from mobile to desktop to server.

**Why another one?** OpenClaw's network effects are its competitive moat. With over 275,000 stars, a skills registry with thousands of community contributions, and multiple ecosystem projects trending simultaneously (awesome-openclaw-skills, awesome-openclaw-usecases), it has become the gravitational center for open-source personal AI assistants.

---

## 9. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> The awesome collection of OpenClaw skills -- 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry

**Language:** -  |  **Stars:** 30,591  |  **Forks:** 2,943  |  **Score:** 3,849  |  **Created:** 2026-01-25

**Background:** Maintained by VoltAgent, this curated directory of over 5,400 OpenClaw skills organizes the official Skills Registry by category, filters low-quality entries, and provides brief descriptions. At over 30,000 stars, it has become one of the primary discovery mechanisms for the OpenClaw ecosystem.

**Problem it solves:** The official OpenClaw Skills Registry contains thousands of skills in a flat structure that makes discovery difficult. This curated list provides categorical organization and quality filtering, making it practical to browse and find skills for specific use cases.

**Why another one?** The scale of curation (5,400+ skills from a larger registry) and the categorical organization provide discovery value that the official registry's search interface does not match. Inclusion acts as a quality signal, saving users from trial-and-error evaluation of raw registry listings.

---

## 10. [worldmonitor](https://github.com/koala73/worldmonitor)
> Real-time global intelligence dashboard -- AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking

**Language:** TypeScript  |  **Stars:** 33,136  |  **Forks:** 5,554  |  **Score:** 3,573  |  **Created:** 2026-01-08

**Background:** World Monitor is an open-source situational awareness dashboard that aggregates real-time news, geopolitical events, and infrastructure status into a unified interface using AI-powered categorization and prioritization. Launched in January 2026, it has grown to over 33,000 stars, reflecting strong demand for open-source OSINT tooling.

**Problem it solves:** Monitoring global events requires switching between multiple news feeds, government alert systems, and infrastructure status pages. World Monitor consolidates these data streams with AI-powered filtering, so analysts and security teams can track developments from a single dashboard.

**Why another one?** Most OSINT dashboards are either commercial SaaS products or static aggregators without intelligence features. World Monitor combines open-source transparency with AI-powered event classification under an AGPL license. Its geopolitical monitoring angle fills a gap that developer-focused dashboards typically ignore.

---

## 11. [prompts.chat](https://github.com/f/prompts.chat)
> f.k.a. Awesome ChatGPT Prompts. The world's largest open-source prompt library for AI.

**Language:** HTML  |  **Stars:** 150,503  |  **Forks:** 19,769  |  **Score:** 3,262  |  **Created:** 2022-12-05

**Background:** Originally "Awesome ChatGPT Prompts" by Fatih Kadir Akin, prompts.chat has evolved into the largest open-source prompt library supporting all major LLMs. It now offers a full web platform with community submissions, Hugging Face dataset mirroring, self-hosting for organizational privacy, and an interactive prompt engineering book. It has over 150,000 stars and 40+ academic citations.

**Problem it solves:** Crafting effective system prompts and persona-based instructions requires trial and error. Prompts.chat provides a structured, community-maintained library of tested prompts that serve as starting points, reducing experimentation time across any AI model.

**Why another one?** Prompts.chat trends recurrently as the canonical prompt reference. Its transformation from a static markdown file into a full platform with cross-model compatibility, community curation, and organizational self-hosting has sustained its relevance across multiple generations of AI models.

---

## 12. [awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
> A community collection of OpenClaw use cases for making life easier

**Language:** -  |  **Stars:** 20,415  |  **Forks:** 1,679  |  **Score:** 2,971  |  **Created:** 2026-02-08

**Background:** This repository curates 36 real-world use cases showing how people actually use OpenClaw daily. Created by Hesam Sheikh in early February 2026, it has surpassed 20,000 stars in under three weeks, indicating strong appetite for practical guidance in the OpenClaw ecosystem.

**Problem it solves:** OpenClaw has thousands of available skills but new users struggle to understand which combinations are useful in practice. This collection bridges the gap between capability and practicality by showcasing tested, real-world workflows.

**Why another one?** Unlike skill catalogs that list individual capabilities, this repository focuses on complete end-to-end workflows composed of multiple skills. The emphasis on daily-life applications rather than technical capabilities makes it accessible to non-technical users evaluating whether OpenClaw can replace their existing tools.

---

## 13. [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
> The agent harness performance optimization system -- skills, instincts, memory, security, and research-first development

**Language:** JavaScript  |  **Stars:** 64,496  |  **Forks:** 7,992  |  **Score:** 2,929  |  **Created:** 2026-01-18

**Background:** Everything Claude Code is a comprehensive performance optimization system for agent harnesses, primarily targeting Claude Code but compatible with Codex, OpenCode, and Cursor. It packages skills, instincts, memory management, security configurations, and research-first development workflows into a single installable framework, accumulating over 64,000 stars since January 2026.

**Problem it solves:** Out-of-the-box coding agents produce inconsistent results across task types. This system provides a tuned set of skills, memory management strategies, and security guardrails that improve agent reliability and output quality for complex multi-step development workflows.

**Why another one?** Cross-agent compatibility and comprehensive scope -- covering skills, instincts, memory, and security rather than just one dimension -- distinguish it from single-purpose skill collections. The research-first development methodology provides a structured approach beyond simple configuration tuning.

---

## 14. [opencode](https://github.com/anomalyco/opencode)
> The open source coding agent

**Language:** TypeScript  |  **Stars:** 117,759  |  **Forks:** 12,014  |  **Score:** 2,870  |  **Created:** 2025-04-30

**Background:** OpenCode is an open-source AI coding agent built in TypeScript by Anomaly, with nearly 118,000 stars since its April 2025 launch. It provides a terminal-based coding interface with support for multiple LLM providers and an extensible architecture for community contributions.

**Problem it solves:** Proprietary coding agents lock users into specific vendors and pricing models. OpenCode provides a fully open-source alternative that users can self-host, modify, and connect to any LLM provider, maintaining control over their data and tool selection.

**Why another one?** OpenCode's massive community creates a self-reinforcing ecosystem of plugins and configurations. Its provider-agnostic design lets users switch between Claude, GPT, Gemini, or local models without changing their workflow -- a flexibility that proprietary alternatives cannot offer.

---

## 15. [clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev)
> A modern GUI client based on Tauri, designed to run on Windows, macOS, and Linux for tailored proxy experience

**Language:** TypeScript  |  **Stars:** 101,301  |  **Forks:** 7,378  |  **Score:** 2,856  |  **Created:** 2023-11-21

**Background:** Clash Verge Rev is a continuation of the original Clash Verge project, built with Tauri as a modern GUI for Clash Meta proxy management. It provides a polished desktop interface for configuring and managing proxy rules across Windows, macOS, and Linux. With over 101,000 stars, it is one of the most popular proxy management tools available.

**Problem it solves:** Managing complex proxy configurations -- routing rules, server selection, traffic splitting -- typically requires editing YAML files or using command-line tools. Clash Verge Rev provides a visual interface that makes proxy management accessible to non-technical users while preserving the full configurability that power users need.

**Why another one?** After the original Clash project's removal and its derivatives' disruption, Clash Verge Rev became one of the primary maintained forks. Its Tauri-based architecture provides a lightweight, native-feeling experience compared to Electron-based alternatives, and the active maintainer community ensures continued compatibility with the latest Clash Meta kernel updates.

---

## 16. [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
> A web interface for Stable Diffusion, implemented using Gradio library

**Language:** Python  |  **Stars:** 161,557  |  **Forks:** 30,136  |  **Score:** 2,480  |  **Created:** 2022-08-22

**Background:** AUTOMATIC1111's Stable Diffusion web UI is the most widely used local interface for running Stable Diffusion image generation. Launched in August 2022, it provides a comprehensive Gradio-based web interface for txt2img, img2img, inpainting, upscaling, and dozens of other image generation workflows. At over 161,000 stars, it remains the dominant local AI image generation tool.

**Problem it solves:** Running Stable Diffusion from the command line or through API calls requires significant technical knowledge. This web UI wraps the full Stable Diffusion pipeline in a browser-based interface with visual controls for every parameter, making image generation accessible to artists and non-programmers.

**Why another one?** Despite newer alternatives like ComfyUI, AUTOMATIC1111's web UI continues to trend due to its enormous extension ecosystem, comprehensive documentation, and the sheer volume of community knowledge built around it. Its straightforward UI paradigm (fill in parameters, click generate) remains more approachable than node-based alternatives for the majority of users.

---

## 17. [visual-explainer](https://github.com/nicobailon/visual-explainer)
> Agent skill that generates rich HTML pages or slide decks for diagrams, diff reviews, plan audits, data tables, and project recaps

**Language:** HTML  |  **Stars:** 5,918  |  **Forks:** 405  |  **Score:** 2,437  |  **Created:** 2026-02-16

**Background:** Visual-explainer is an agent skill by Nico Bailon that transforms complex terminal output into styled, self-contained HTML pages. Instead of ASCII art and box-drawing tables, it generates visual HTML pages for architecture diagrams, diff reviews, plan audits, and data tables that open directly in the browser. Created in mid-February 2026, it has quickly grown to nearly 6,000 stars.

**Problem it solves:** Terminal-based coding agents produce text-only output that struggles to communicate complex structures like architecture diagrams, multi-file diffs, or comparison tables. Visual-explainer bridges this gap by rendering agent output as rich HTML, making complex information legible and shareable.

**Why another one?** The concept of an agent skill that generates visual output rather than text is relatively novel. While agents can already produce markdown, visual-explainer generates styled HTML with CSS animations and interactive elements, producing output that looks like a designed document rather than a developer tool's dump. Its format-agnostic approach -- diagrams, diffs, tables, and recaps all through one skill -- is also distinctive.

---

## 18. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster

**Language:** Shell  |  **Stars:** 74,864  |  **Forks:** 6,008  |  **Score:** 2,268  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official terminal-based agentic coding tool, launched in February 2025. It operates directly in the developer's terminal with full codebase context, supports an extensible skills and hooks system, and integrates with IDEs and GitHub workflows via @claude mentions.

**Problem it solves:** Developers spend significant time on repetitive coding tasks, navigating unfamiliar codebases, and managing version control workflows. Claude Code automates these tasks in the terminal, eliminating context-switching between IDE, browser chat, and command line.

**Why another one?** As Anthropic's first-party coding agent, Claude Code is the reference implementation for terminal-based agentic development. Its growing skills ecosystem and native GitHub integration continue to drive adoption and sustained trending.

---

## 19. [taste-skill](https://github.com/Leonxlnx/taste-skill)
> Taste-Skill (High-Agency Frontend) -- gives your AI good taste, stops the AI from generating boring, generic UI

**Language:** -  |  **Stars:** 2,484  |  **Forks:** 160  |  **Score:** 2,079  |  **Created:** 2026-02-19

**Background:** Taste-Skill is a collection of agent skills by Leonxlnx that improve how AI tools write frontend code. Instead of generating generic interfaces, the AI builds modern designs with proper animations, spacing, and visual quality. Created just days ago on February 19, 2026, it has already accumulated nearly 2,500 stars.

**Problem it solves:** AI coding agents default to producing functional but visually bland frontend code -- generic layouts, no animations, poor spacing, stock component styles. Taste-Skill injects design sensibility into the agent's output, producing interfaces that look professionally designed rather than auto-generated.

**Why another one?** Most agent skills focus on logic, architecture, or workflow. Taste-Skill targets aesthetics specifically -- a dimension that is typically ignored in the agent skills ecosystem. The focus on "taste" as a teachable, installable capability rather than an inherent model property is a novel framing that resonates with frontend developers frustrated by AI-generated UI quality.

---

## 20. [OpenBB](https://github.com/OpenBB-finance/OpenBB)
> Financial data platform for analysts, quants, and AI agents

**Language:** Python  |  **Stars:** 62,737  |  **Forks:** 6,144  |  **Score:** 2,051  |  **Created:** 2020-12-20

**Background:** OpenBB is an open-source financial data platform that has evolved from a terminal application into a comprehensive data layer serving both human analysts and AI agents. It provides a unified API for accessing market data from multiple providers with consistent interfaces. At over 62,000 stars, it is one of the most popular open-source finance projects.

**Problem it solves:** Financial data is fragmented across dozens of providers with different APIs, authentication mechanisms, and data formats. OpenBB normalizes these into a single, consistent interface, eliminating the need for separate integrations with each data source.

**Why another one?** OpenBB's expanding role as a data backbone for AI agents in financial workflows keeps it relevant. As agent-based trading and analysis tools proliferate, its standardized data layer becomes the canonical open-source data source that agents can query without vendor-specific integrations.

---

## 21. [GhostTrack](https://github.com/HunxByts/GhostTrack)
> Useful tool to track location or mobile number

**Language:** Python  |  **Stars:** 7,999  |  **Forks:** 1,059  |  **Score:** 1,972  |  **Created:** 2023-04-15

**Background:** GhostTrack is a Python OSINT tool for IP geolocation and phone number lookups, running on both Linux and Termux (Android). It consolidates multiple lookup services into a single CLI and has been maintained since April 2023.

**Problem it solves:** Performing IP geolocation and phone number lookups typically requires using multiple web services. GhostTrack consolidates these into a local CLI tool, avoiding the need to enter data into third-party websites.

**Why another one?** GhostTrack's Termux compatibility and minimal setup requirements make it popular in the mobile security and OSINT hobbyist community. It trends periodically as new users in that community discover it.

---

## 22. [ruvector](https://github.com/ruvnet/ruvector)
> RuVector is a high-performance, real-time, self-learning vector graph neural network and database built in Rust

**Language:** Rust  |  **Stars:** 2,932  |  **Forks:** 311  |  **Score:** 1,818  |  **Created:** 2025-11-19

**Background:** RuVector is a Rust-based system that combines a vector database, graph neural network, and self-learning capabilities into what it calls an "agentic operating system." It won a CES 2026 Innovation Award and provides real-time processing of vector and graph data with continuous self-improvement. The project launched in November 2025.

**Problem it solves:** Traditional vector databases are passive stores that require external orchestration for learning and adaptation. RuVector integrates active learning directly into the database layer, allowing the system to improve its representations and query strategies over time without requiring a separate training pipeline.

**Why another one?** The convergence of vector database, graph neural network, and self-learning capabilities in a single Rust binary is architecturally distinct from both traditional vector databases (Pinecone, Qdrant) and separate GNN frameworks. The CES Innovation Award adds credibility beyond typical open-source projects.

---

## 23. [skills](https://github.com/anthropics/skills)
> Public repository for Agent Skills

**Language:** Python  |  **Stars:** 86,452  |  **Forks:** 9,147  |  **Score:** 1,811  |  **Created:** 2025-09-22

**Background:** This is Anthropic's official implementation of skills for Claude, containing first-party and curated community skills that Claude can dynamically load to improve performance on specialized tasks. With over 86,000 stars since September 2025, it is one of the largest official agent skill repositories.

**Problem it solves:** Claude's general-purpose training does not cover every specialized workflow, organizational standard, or domain-specific task. Skills provide a mechanism for teaching Claude specific task completion patterns -- from brand-compliant document creation to data analysis using organization-specific workflows.

**Why another one?** As Anthropic's first-party skills repository, it carries vendor authority and direct integration with Claude Code's skills loading system. Skills here are tested against Claude's behavior and maintained alongside the agent itself, providing reliability guarantees that community-only repositories cannot match.

---

## 24. [Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever)
> Multiple Shadowrocket rules with strong ad filtering capabilities, rebuilt daily at 8 AM

**Language:** -  |  **Stars:** 23,345  |  **Forks:** 1,534  |  **Score:** 1,790  |  **Created:** 2021-12-06

**Background:** This repository provides regularly updated ad-blocking rule sets for Shadowrocket, the popular iOS proxy client. The rules are automatically rebuilt daily at 8 AM to incorporate the latest ad network domains and tracking endpoints. Since December 2021, it has grown to over 23,000 stars.

**Problem it solves:** Maintaining effective ad-blocking rules for proxy-based filtering requires constant updates as ad networks rotate domains and tracking infrastructure. This repository automates that maintenance with daily rebuilds, so users always have current rules without manual curation.

**Why another one?** The automated daily rebuild cycle and focus specifically on Shadowrocket (rather than generic ad-blocking lists) distinguish it from general filter lists like EasyList. The repository's longevity (over four years of daily updates) has established it as the most reliable Shadowrocket-specific ad-blocking resource.

---

## 25. [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)
> The best agent harness

**Language:** TypeScript  |  **Stars:** 37,162  |  **Forks:** 2,793  |  **Score:** 1,749  |  **Created:** 2025-12-03

**Background:** Oh-My-OpenCode is an agent harness built on top of OpenCode, providing a curated set of configurations, plugins, and workflow enhancements that improve the default OpenCode experience. At over 37,000 stars since December 2025, it has become one of the most popular OpenCode ecosystem projects. The project has had to issue security warnings about an impersonation site attempting to monetize downloads.

**Problem it solves:** OpenCode out of the box requires configuration and plugin selection to reach optimal performance. Oh-My-OpenCode provides an opinionated, pre-configured setup that bundles the community's best practices, plugins, and configurations into a single installation.

**Why another one?** The relationship to OpenCode mirrors the oh-my-zsh relationship to zsh -- it is not a replacement but an opinionated configuration layer that lowers the barrier to getting the most out of the underlying tool. The 37,000+ stars suggest this curated approach resonates more broadly than DIY configuration.

---

> **Day's theme:** The agent skills ecosystem is maturing rapidly, with specialized skills for context engineering, visual output, frontend aesthetics, and ML workflows joining a growing constellation of curated skill directories and methodology frameworks that collectively shape how coding agents actually work.
