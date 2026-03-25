# Trendshift Report — 2026-03-17
**Total:** 25 repositories

---

## 1. [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
> Master programming by recreating your favorite technologies from scratch.

**Language:** Markdown  |  **Stars:** 482,545  |  **Forks:** 45,406  |  **Score:** 20,166  |  **Created:** 2018-05-09

**Background:** Build Your Own X is a curated compilation of step-by-step tutorials for recreating popular technologies from scratch, maintained by CodeCrafters since 2018. It covers over 30 categories — 3D renderers, databases, Docker, operating systems, programming languages, search engines, web servers, and more — with guides in dozens of languages including C++, Python, JavaScript, Rust, and Go. At nearly 483k stars it is one of the most-starred repositories on all of GitHub.

**Problem it solves:** Learning how a technology truly works is difficult when you only use it as a black box. This repository aggregates the best "build it from scratch" tutorials so that developers can deepen their understanding of systems they rely on daily, following the Feynman principle: "What I cannot create, I do not understand."

**Why another one?** Unlike scattered blog posts or video courses, this is a single maintained index with a strict quality bar — only well-written, step-by-step guides that produce a working artifact. Its longevity (eight years of continuous curation) and community size make it the canonical reference for project-based systems learning.

---

## 2. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 108,363  |  **Forks:** 8,701  |  **Score:** 15,199  |  **Created:** 2025-10-09

**Background:** Superpowers is a composable skills framework and structured software development workflow created by Jesse Vincent (obra) that installs into coding agents — Claude Code, Cursor, Codex, OpenCode, and Gemini CLI — via their plugin systems. It enforces a multi-stage methodology: the agent brainstorms and refines a spec before writing code, produces a detailed implementation plan, then executes through subagent-driven development with two-stage code review per task. The project has surpassed 108k stars since its October 2025 launch.

**Problem it solves:** Coding agents left to their own defaults dive directly into writing code, skip test-driven development, and drift from the original intent mid-session. Superpowers installs guard rails — mandatory spec approval, red-green-refactor TDD enforcement, and plan checkpoints — so an agent can work autonomously for hours without derailing from what was agreed.

**Why another one?** Rather than being a new coding agent, Superpowers is a methodology layer portable across multiple agents via their plugin systems. The same skills install in Claude Code, Cursor, Codex, OpenCode, and Gemini CLI. The emphasis on subagent delegation rather than a single long-running context limits drift and scales to complex multi-hour tasks.

---

## 3. [Crucix](https://github.com/calesthio/Crucix)
> Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

**Language:** JavaScript  |  **Stars:** 6,567  |  **Forks:** 1,003  |  **Score:** 10,266  |  **Created:** 2026-03-14

**Background:** Crucix is a self-contained, Jarvis-style OSINT dashboard that pulls from 27 open-source intelligence feeds — satellite fire detection, flight tracking, radiation monitoring, satellite constellation tracking, economic indicators, live market prices, conflict data, sanctions lists, and social sentiment — in parallel every 15 minutes, rendering everything on a single self-hosted dashboard. It requires only Node.js and Express as its sole dependency.

**Problem it solves:** Keeping track of geopolitical events, infrastructure disruptions, and market signals requires monitoring dozens of disparate feeds and paid OSINT platforms. Crucix consolidates these into one local dashboard with multi-tier alerts to Telegram and Discord, LLM-powered briefings via commands like `/brief` and `/sweep`, and actionable trade ideas grounded in cross-domain data — all without cloud dependencies, telemetry, or subscriptions.

**Why another one?** Crucix targets the individual operator rather than enterprise OSINT teams. Its single-dependency architecture (`node server.mjs` and you are running), combined with two-way LLM integration that turns the dashboard into an interactive intelligence assistant reachable from a phone, differentiates it from heavier commercial OSINT tools and read-only dashboards.

---

## 4. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers.

**Language:** Shell  |  **Stars:** 60,953  |  **Forks:** 9,146  |  **Score:** 9,444  |  **Created:** 2025-10-13

**Background:** The Agency is a growing collection of meticulously crafted AI agent personalities created by msitarzewski, born from a Reddit thread and months of iteration. Each agent is a specialized expert with a unique voice, communication style, structured workflows, and measurable deliverables. The roster spans engineering (frontend, backend, mobile, AI, DevOps, security), marketing, content, design, and operations divisions, installable into Claude Code, Cursor, Aider, Windsurf, Copilot, and Gemini CLI.

**Problem it solves:** Generic AI prompts produce generic output. The Agency provides deeply specialized agent personas — each with domain expertise, personality traits, and production-ready workflows — so that users get focused, role-appropriate responses instead of one-size-fits-all answers. The agents come with concrete code examples, success metrics, and communication styles.

**Why another one?** Unlike single-purpose prompt libraries, The Agency provides an entire organizational structure of specialized agents with cross-tool portability. Conversion scripts generate integration files for all major coding assistants, and the install script auto-detects which tools are present on the user's machine, making it a plug-and-play virtual team rather than a collection of isolated prompts.

---

## 5. [deepagents](https://github.com/langchain-ai/deepagents)
> Agent harness built with LangChain and LangGraph. Equipped with a planning tool, a filesystem backend, and the ability to spawn subagents.

**Language:** Python  |  **Stars:** 17,096  |  **Forks:** 2,411  |  **Score:** 7,400  |  **Created:** 2025-07-27

**Background:** Deep Agents is an opinionated, batteries-included agent harness from LangChain, built on LangGraph. Out of the box it provides planning via a `write_todos` tool, filesystem operations (read, write, edit, ls, glob, grep), shell access with sandboxing, sub-agent delegation with isolated context windows, auto-summarization when conversations grow long, and smart defaults that teach the model how to use these tools effectively. It also ships a CLI for terminal-based coding agent workflows.

**Problem it solves:** Building a capable coding agent from scratch requires wiring up prompts, tools, context management, and sub-agent coordination — substantial boilerplate before the agent can do useful work. Deep Agents provides a working agent immediately: install, invoke, and customize only what you need. MCP support is included via langchain-mcp-adapters.

**Why another one?** Deep Agents is LangGraph-native, meaning every component is a composable graph node that can be extended, rewired, or deployed to LangGraph Cloud. Unlike standalone agent frameworks, it inherits LangChain's ecosystem — model swapping, tool libraries, LangSmith observability — while providing the opinionated defaults that make the agent productive out of the box.

---

## 6. [gstack](https://github.com/garrytan/gstack)
> Use Garry Tan's exact Claude Code setup: 15 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA.

**Language:** TypeScript  |  **Stars:** 39,705  |  **Forks:** 4,906  |  **Score:** 7,219  |  **Created:** 2026-03-11

**Background:** gstack is Garry Tan's open-source software factory for Claude Code, turning it into a virtual engineering team. Tan — President and CEO of Y Combinator, former early engineer at Palantir, cofounder of Posterous — reports shipping 600,000+ lines of production code in 60 days (10,000-20,000 lines per day) part-time while running YC full-time. The toolkit provides 20+ slash commands acting as specialized roles: a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer, a QA lead that opens a real browser, a security officer running OWASP+STRIDE audits, and a release engineer.

**Problem it solves:** A blank Claude Code prompt gives no structure for complex product development. gstack provides opinionated roles and workflows — `/office-hours` for product discussion, `/plan-ceo-review` for feature planning, `/review` for code review, `/qa` for browser-based QA, `/ship` for release — so a solo builder can operate with the rigor of a full engineering team.

**Why another one?** The credibility angle is explicit: this is the exact setup a YC CEO uses daily to ship at scale. The differentiator is breadth — not just code review or planning, but the full product lifecycle from ideation through security audit to deployment, all as slash commands, all MIT-licensed.

---

## 7. [claude-mem](https://github.com/thedotmack/claude-mem)
> A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI, and injects relevant context back into future sessions.

**Language:** TypeScript  |  **Stars:** 39,927  |  **Forks:** 2,937  |  **Score:** 6,897  |  **Created:** 2025-08-31

**Background:** Claude-Mem is a persistent memory compression system built for Claude Code. It automatically captures everything Claude does during coding sessions — file changes, tool calls, decisions, reasoning — compresses these records using the Claude Agent SDK, and injects relevant context back into future sessions. The system maintains a structured memory store that grows smarter over time, giving Claude Code continuity across sessions that it otherwise lacks.

**Problem it solves:** Claude Code starts each session with a blank slate, forcing users to re-explain project context, past decisions, and ongoing work. Claude-Mem eliminates this cold-start problem by automatically recording session activity, compressing it into retrievable memory, and injecting the most relevant context when a new session begins — without requiring the user to manually write notes or maintain documentation.

**Why another one?** Most memory solutions for AI agents store raw conversation logs, which bloat quickly and retrieve poorly. Claude-Mem's differentiator is AI-powered compression: it uses Claude itself to distill session activity into concise, semantically rich memory entries, keeping the memory store compact while preserving the information that actually matters for future sessions.

---

## 8. [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)
> Bash is all you need - A nano claude code-like agent harness, built from 0 to 1.

**Language:** TypeScript  |  **Stars:** 37,344  |  **Forks:** 5,917  |  **Score:** 5,126  |  **Created:** 2025-06-29

**Background:** Learn Claude Code is an educational project by shareAI-lab that reconstructs a Claude Code-like agent harness from scratch, demonstrating that the core architecture — a model with bash access — is sufficient to build a capable coding agent. The project argues that the agent is the model itself, not the surrounding framework, drawing parallels to DeepMind's DQN, OpenAI Five, and AlphaStar to illustrate that agent capability comes from training, not orchestration plumbing.

**Problem it solves:** The proliferation of "AI agent" frameworks creates the impression that building an effective coding agent requires complex orchestration layers, drag-and-drop workflow builders, or prompt-chain libraries. This project strips away that complexity to show that a well-prompted model with filesystem and shell access is the core of what makes agents like Claude Code work, making the architecture accessible to anyone who wants to understand or extend it.

**Why another one?** The explicit pedagogical stance — "the model IS the agent, not the framework" — sets it apart from agent frameworks that add abstraction layers. By building from zero to a working agent harness in transparent, readable code, it serves as both a learning resource and a philosophical statement about where agent capability actually resides.

---

## 9. [paperclip](https://github.com/paperclipai/paperclip)
> Open-source orchestration for zero-human companies.

**Language:** TypeScript  |  **Stars:** 32,589  |  **Forks:** 4,578  |  **Score:** 4,322  |  **Created:** 2026-03-02

**Background:** Paperclip is a Node.js server and React UI that orchestrates teams of AI agents to run a business autonomously. The framing is explicit: "If OpenClaw is an employee, Paperclip is the company." Users define business goals, hire a team (CEO, CTO, engineers, designers, marketers — any bot, any provider), set budgets, and monitor from a dashboard. It supports OpenClaw, Claude Code, Codex, Cursor, and any agent that can receive a heartbeat, with org charts, governance, goal alignment, and cost tracking.

**Problem it solves:** Running 20 simultaneous AI agent sessions means losing track of who is doing what, how much it costs, and whether agents are aligned with the overall goal. Paperclip provides the management layer — task assignment, budget enforcement, work auditing, and goal cascading — that turns a collection of independent agents into a coordinated organization.

**Why another one?** Existing agent orchestration tools focus on task execution within a single project. Paperclip operates at the business level: org charts, budgets, governance, and cross-agent coordination toward revenue goals. The upcoming Clipmart marketplace for downloadable company templates further positions it as infrastructure for autonomous businesses, not just autonomous coding.

---

## 10. [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
> The Zero-Server Code Intelligence Engine - a client-side knowledge graph creator that runs entirely in your browser.

**Language:** TypeScript  |  **Stars:** 19,212  |  **Forks:** 2,222  |  **Score:** 4,206  |  **Created:** 2025-08-02

**Background:** GitNexus indexes any codebase into a knowledge graph — capturing every dependency, call chain, cluster, and execution flow — then exposes it through smart tools so AI agents never miss code relationships. It offers two modes: a CLI+MCP server for daily development with Cursor, Claude Code, Codex, and OpenCode, and a browser-based Web UI for visual graph exploration and AI chat. All processing runs locally or in-browser with no server required; the CLI uses Tree-sitter native bindings and LadybugDB for persistent storage.

**Problem it solves:** AI coding agents frequently miss dependencies, break call chains, and ship blind edits because they lack architectural awareness of the codebase. GitNexus gives agents a deep structural view — not just file contents but relationship graphs — so that even smaller models can make architecturally sound edits. The tagline comparison: "Like DeepWiki, but deeper."

**Why another one?** DeepWiki helps you understand code through descriptions; GitNexus lets you analyze it through a knowledge graph that tracks every relationship. The MCP integration means agents can query the graph directly during their workflow, and the bridge mode lets the Web UI browse all CLI-indexed repos without re-uploading, combining visual exploration with programmatic agent access.

---

## 11. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> Practice made claude perfect.

**Language:** HTML  |  **Stars:** 21,330  |  **Forks:** 1,863  |  **Score:** 4,046  |  **Created:** 2025-10-31

**Background:** Claude Code Best Practice is a comprehensive reference guide maintained by shanraisshan that documents best practices for every Claude Code extensibility mechanism — subagents, commands, skills, workflows, hooks, and MCP servers. Each feature includes both a best-practice guide and a working implementation example, plus an orchestration workflow pattern showing how the pieces compose. The repository reached #1 on GitHub Trending and is regularly updated alongside Claude Code releases.

**Problem it solves:** Claude Code's extensibility surface — subagents, commands, skills, hooks, MCP — is powerful but poorly documented for real-world patterns. This repository provides battle-tested examples for each mechanism, showing not just the API but the recommended architecture: when to use a subagent vs. a command vs. a skill, how to structure orchestration workflows, and how to wire hooks for event-driven automation.

**Why another one?** Official documentation covers the APIs; this project covers the patterns. The combination of best-practice guides with working implementations, plus tips from practitioners like Boris Cherny, makes it the community's go-to reference for getting the most out of Claude Code's extensibility system.

---

## 12. [daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)
> LLM-powered stock analysis system for A/H/US markets.

**Language:** Python  |  **Stars:** 24,734  |  **Forks:** 25,594  |  **Score:** 3,849  |  **Created:** 2026-01-10

**Background:** Daily Stock Analysis is an AI-powered stock intelligence system by ZhuLinsen that covers A-share, Hong Kong, and US markets. It performs multi-dimensional analysis — technical indicators (MA, multi-head alignment), chip distribution, sentiment intelligence, and real-time market data — then generates a "decision dashboard" with precise buy/sell levels and an operation checklist. It supports multiple LLM backends via LiteLLM (Gemini, OpenAI, DeepSeek, Claude, Ollama local models) and pushes reports to WeChat Work, Feishu, Telegram, Discord, Slack, DingTalk, and email.

**Problem it solves:** Individual investors typically lack the infrastructure for systematic daily stock analysis across multiple markets. This system automates the entire pipeline — data collection from AkShare/Tushare/YFinance, multi-source news aggregation via Tavily/SerpAPI, LLM-driven analysis, and multi-channel push notifications — running on GitHub Actions with zero server cost.

**Why another one?** The combination of three-market coverage (A/H/US), built-in backtesting for historical accuracy validation, a conversational "ask about stocks" agent supporting 11 built-in strategies, and zero-cost GitHub Actions automation differentiates it from simpler stock notification tools. The portfolio management module with position tracking and trade validation adds a layer most open-source alternatives lack.

---

## 13. [OpenViking](https://github.com/volcengine/OpenViking)
> An open-source context database designed specifically for AI Agents.

**Language:** Python  |  **Stars:** 18,516  |  **Forks:** 1,270  |  **Score:** 3,832  |  **Created:** 2026-01-05

**Background:** OpenViking is an open-source context database from Volcengine (ByteDance's cloud platform) designed specifically for AI agents. It abandons the fragmented vector storage model of traditional RAG and adopts a "file system paradigm" to unify the structured organization of memories, resources, and skills that agents need. The system provides a three-tier context loading architecture (L0/L1/L2), directory-recursive retrieval combining positioning with semantic search, and visualized retrieval trajectories for debugging.

**Problem it solves:** When building AI agents, developers face fragmented context (memories in code, resources in vector databases, skills scattered), surging context demand from long-running tasks, poor retrieval from flat storage lacking global view, unobservable retrieval chains that are hard to debug, and limited memory that only records user interactions without task-level memory. OpenViking addresses all five challenges through its unified filesystem paradigm.

**Why another one?** Traditional RAG systems use flat vector storage without structural organization, making retrieval a black box. OpenViking's filesystem paradigm lets developers manage agent context like managing local files — with directories, hierarchies, and explicit paths — while the tiered loading (L0/L1/L2) significantly reduces token consumption by loading context on demand rather than all at once.

---

## 14. [MiroFish](https://github.com/666ghj/MiroFish)
> A Simple and Universal Swarm Intelligence Engine, Predicting Anything.

**Language:** Python  |  **Stars:** 40,933  |  **Forks:** 5,565  |  **Score:** 3,702  |  **Created:** 2025-11-26

**Background:** MiroFish is a next-generation AI prediction engine developed by Shanda that uses multi-agent simulation to forecast outcomes. It takes seed information from the real world — breaking news, policy drafts, financial signals — and automatically constructs a high-fidelity parallel digital world. Within this space, thousands of agents with independent personalities, long-term memory, and behavioral logic interact and evolve socially, allowing users to dynamically inject variables from a "god's-eye view" and observe emergent outcomes.

**Problem it solves:** Traditional prediction models rely on statistical patterns from historical data and cannot account for emergent social dynamics — how individuals with different motivations interact and collectively shift outcomes. MiroFish simulates these interactions at scale, letting decision-makers preview the consequences of policy changes, PR strategies, or market interventions in a zero-risk digital sandbox before committing to real-world action.

**Why another one?** Rather than forecasting from data curves, MiroFish forecasts from simulated social dynamics. The swarm intelligence approach — thousands of autonomous agents with distinct personas interacting — captures emergent phenomena that statistical models structurally cannot. The platform serves both serious use cases (policy simulation, crisis response planning) and creative ones (exploring novel plot directions, running thought experiments).

---

## 15. [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
> The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**Language:** JavaScript  |  **Stars:** 102,648  |  **Forks:** 13,375  |  **Score:** 3,651  |  **Created:** 2026-01-18

**Background:** Everything Claude Code is a comprehensive performance optimization system for agent harnesses, created by affaan-m. Winner of an Anthropic Hackathon, it packages skills, instincts, memory management, security protocols, and research-first development methodology for Claude Code, Codex, OpenCode, Cursor, and other agent platforms. Supporting 7 languages and maintained by 30+ contributors, the project provides a holistic framework for making coding agents more effective, secure, and consistent across sessions.

**Problem it solves:** Out-of-the-box coding agents lack optimized workflows for real-world software development — no structured memory, inconsistent security practices, no research-before-code methodology. Everything Claude Code provides a curated, tested set of optimizations that improve agent performance across the board, from context management to security auditing.

**Why another one?** While tools like Superpowers focus on methodology and gstack on role-based workflows, Everything Claude Code focuses on performance optimization — making the agent harness itself faster, more memory-efficient, and more secure. The cross-platform support (six agent platforms) and multi-language documentation make it accessible to the broadest possible user base.

---

## 16. [taste-skill](https://github.com/Leonxlnx/taste-skill)
> Taste-Skill (High-Agency Frontend) - gives your AI good taste. Stops the AI from generating boring, generic, "slop."

**Language:** —  |  **Stars:** 5,385  |  **Forks:** 497  |  **Score:** 3,484  |  **Created:** 2026-02-19

**Background:** Taste Skill is a collection of AI skills by Leonxlnx that improve how AI coding tools write frontend code. Instead of generating generic interfaces, the AI builds modern, premium designs with proper animations, spacing, and visual quality. It installs via a universal CLI command (`npx skills add`) and works with all major AI coding agents — Cursor, Claude Code, Codex, Windsurf, Copilot, and more. The package includes the main taste-skill, a redesign-skill for upgrading existing projects, and a soft-skill for premium soft UI aesthetics.

**Problem it solves:** AI-generated frontend code tends toward generic, visually flat interfaces — what the community calls "AI slop." Taste Skill injects design intelligence into the generation process so the AI produces layouts, typography, colors, spacing, and motion that look professionally designed rather than template-generated.

**Why another one?** Most AI coding tools optimize for functionality, not aesthetics. Taste Skill specifically targets the visual quality gap, providing design-focused skills rather than code-focused ones. The redesign-skill variant that audits and fixes existing projects acknowledges that many codebases already have AI slop that needs upgrading, not just new projects that need better defaults.

---

## 17. [Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders)
> Practical marketing resources to get the first 10 / 100 / 1000 users for your SaaS / App / Startup.

**Language:** —  |  **Stars:** 5,850  |  **Forks:** 553  |  **Score:** 3,423  |  **Created:** 2025-05-19

**Background:** Marketing for Founders is a curated collection of practical marketing resources by EdoStra, specifically targeting technical founders taking their first steps with a startup. It covers launch platforms, Product Hunt strategy, social media marketing, sales and cold outreach, SEO, LLM SEO (AEO/GEO), Reddit marketing, email marketing, and content marketing — all focused on the zero-to-1,000 users phase rather than scaling an already-funded company.

**Problem it solves:** Most marketing advice targets companies with established budgets scaling to $1M ARR and 100,000 users — inspirational but not actionable for a solo founder with no marketing budget. This collection focuses exclusively on the earliest stages: finding the first 10, 100, and 1,000 users with no budget, providing immediately actionable tactics rather than high-level strategy.

**Why another one?** The explicit focus on the pre-budget, pre-traction phase fills a gap that generic marketing resources ignore. The inclusion of LLM SEO (optimizing for AI search engines, not just Google) reflects the 2025-2026 shift in how users discover products, making it more current than older marketing guides that assume traditional search as the primary discovery channel.

---

## 18. [project-nomad](https://github.com/Crosstalk-Solutions/project-nomad)
> Project N.O.M.A.D, is a self-contained, offline survival computer packed with critical tools, knowledge, and AI.

**Language:** TypeScript  |  **Stars:** 14,627  |  **Forks:** 1,375  |  **Score:** 3,391  |  **Created:** 2025-06-24

**Background:** Project N.O.M.A.D. (Node for Offline Media, Archives, and Data) is a self-contained, offline-first knowledge and education server by Crosstalk Solutions. It installs on any Debian-based OS via a single curl command, runs all tools and resources through a browser interface, and requires no desktop environment — making it suitable for headless server deployment. All content is designed to function completely without internet connectivity.

**Problem it solves:** In scenarios where internet access is unavailable — remote locations, disaster response, censored networks, or intentional disconnection — access to educational resources, reference materials, medical information, and AI assistance disappears entirely. Project N.O.M.A.D. packages critical knowledge and tools into a portable, self-contained server that works anywhere with hardware and power.

**Why another one?** Most offline knowledge projects focus on a single domain (e.g., Wikipedia mirrors, offline documentation). N.O.M.A.D. bundles a comprehensive stack — education, AI, reference, and practical tools — into a single installable system with a browser-based interface, targeting true off-grid scenarios rather than intermittent connectivity.

---

## 19. [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
> An AI SKILL that provides design intelligence for building professional UI/UX across multiple platforms.

**Language:** Python  |  **Stars:** 49,030  |  **Forks:** 4,747  |  **Score:** 3,134  |  **Created:** 2025-11-30

**Background:** UI UX Pro Max is an AI skill by nextlevelbuilder that provides design intelligence for building professional user interfaces across multiple platforms and frameworks. Version 2.0 introduced an intelligent Design System Generator — an AI-powered reasoning engine that analyzes project requirements and generates a complete, tailored design system including patterns, conversion strategies, CTA placement, section ordering, color palettes, and typography hierarchies in seconds.

**Problem it solves:** AI-generated UIs lack design coherence — random spacing, inconsistent typography, no systematic color usage, and no conversion-oriented layout strategy. UI UX Pro Max provides a structured design system upfront, so the AI generates interfaces that follow professional design principles rather than producing visually inconsistent output.

**Why another one?** While Taste Skill focuses on making generated code look premium, UI UX Pro Max operates at the design system level — generating the underlying rules and patterns that ensure consistency across an entire application. The Design System Generator produces conversion-optimized layouts with specific CTA placement strategies, targeting business outcomes rather than just visual polish.

---

## 20. [openchamber](https://github.com/openchamber/openchamber)
> Desktop and web interface for OpenCode AI agent.

**Language:** TypeScript  |  **Stars:** 2,359  |  **Forks:** 231  |  **Score:** 3,026  |  **Created:** 2025-09-11

**Background:** OpenChamber is a rich desktop and web interface for the OpenCode AI agent, providing a visual layer on top of the terminal-based agent. It lets users review diffs, manage multiple agents, run dev servers, and maintain an overview of ongoing work — available as a desktop app, in the browser, and on mobile. The tagline: "OpenCode, everywhere."

**Problem it solves:** Terminal-based coding agents like OpenCode are powerful but limited in their ability to present visual information — diffs are hard to review in a terminal, managing multiple concurrent agents requires multiple terminal windows, and there is no mobile access. OpenChamber provides the visual interface layer that makes these workflows accessible and manageable.

**Why another one?** OpenChamber is specifically built for OpenCode rather than being a generic agent UI. This tight integration means it can surface OpenCode-specific features (tool outputs, agent state, settings) in a native way. The cross-platform availability — desktop, browser, and phone — means users can monitor and interact with their agents from any device.

---

## 21. [OpenAlice](https://github.com/TraderAlice/OpenAlice)
> File-driven AI trading agent engine for crypto and securities markets.

**Language:** TypeScript  |  **Stars:** 2,800  |  **Forks:** 364  |  **Score:** 2,892  |  **Created:** 2026-02-18

**Background:** Open Alice is a file-driven AI trading agent that gives users their own research desk, quant team, trading floor, and risk management — all running on a laptop 24/7. The entire system is file-based: Markdown defines persona and tasks, JSON defines configuration, JSONL stores conversations. Both humans and AI control Alice by reading and modifying files, applying the same read/write primitives from vibe coding to vibe trading. No database, no containers — just files.

**Problem it solves:** Algorithmic trading typically requires complex infrastructure — databases, message queues, containerized services, and proprietary platforms. Open Alice reduces the entire stack to local files, making it possible to inspect, modify, and version-control every aspect of the trading agent's behavior using the same tools developers already use for code.

**Why another one?** The file-driven architecture is the key differentiator. Where other trading bots use databases and APIs, Alice uses Markdown and JSON files that are readable, editable, and version-controllable with git. The OS-native design lets Alice interact with the user's browser, Telegram, and local devices, and the reasoning-driven approach means every trade decision includes explicit rationale rather than opaque signal execution.

---

## 22. [autoresearch](https://github.com/karpathy/autoresearch)
> AI agents running research on single-GPU nanochat training automatically.

**Language:** Python  |  **Stars:** 50,773  |  **Forks:** 7,078  |  **Score:** 2,874  |  **Created:** 2026-03-06

**Background:** Autoresearch is Andrej Karpathy's experiment in autonomous AI research: give an AI agent a small but real LLM training setup (a simplified single-GPU implementation of nanochat) and let it experiment autonomously overnight. The agent modifies the training code, runs a 5-minute training run, checks if the result improved, keeps or discards the change, and repeats. Users wake up to a log of experiments and — hopefully — a better model. Karpathy frames it as the beginning of a future where research is done by autonomous AI swarms.

**Problem it solves:** ML research iteration is bottlenecked by human attention: a researcher can only run and analyze so many experiments per day, and sleeping hours are wasted. Autoresearch automates the experiment loop — hypothesis, implementation, training, evaluation, decision — so that research runs continuously without human intervention.

**Why another one?** This is not a framework or a product but a philosophical prototype from one of the most influential ML practitioners. The framing is deliberately provocative: Karpathy describes it as "how it all began" for a future where AI research is done entirely by autonomous agents. The simplicity — one GPU, one training script, one agent loop — makes the concept reproducible and extensible.

---

## 23. [browser](https://github.com/lightpanda-io/browser)
> Lightpanda: the headless browser designed for AI and automation.

**Language:** Zig  |  **Stars:** 24,137  |  **Forks:** 960  |  **Score:** 2,692  |  **Created:** 2023-02-07

**Background:** Lightpanda is an open-source headless browser written from scratch in Zig — not a Chromium fork, not a WebKit patch. It is designed specifically for AI agents and automation, with JavaScript execution, partial Web API support, and compatibility with Playwright, Puppeteer, and chromedp through the Chrome DevTools Protocol. Benchmarks on real web pages show 11x faster execution and 9x lower memory usage compared to Chrome headless, with instant startup.

**Problem it solves:** Chrome headless is the default for web automation, scraping, and AI agent browsing, but it was designed as a full desktop browser — carrying massive overhead in memory and CPU for tasks that do not need rendering, extensions, or a GUI. Lightpanda provides the web interaction layer AI agents need at a fraction of the resource cost, making it feasible to run many concurrent browser instances for agent swarms.

**Why another one?** Existing headless browser options are either Chrome/Chromium forks (inheriting the full browser's resource overhead) or lightweight HTTP clients that cannot execute JavaScript or interact with modern web applications. Lightpanda occupies the middle ground: real JavaScript execution and CDP compatibility with an ultra-lean Zig implementation purpose-built for the headless use case.

---

## 24. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster.

**Language:** Shell  |  **Stars:** 81,726  |  **Forks:** 6,816  |  **Score:** 2,689  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official agentic coding tool, operating in the terminal with full codebase understanding. It executes routine tasks, explains complex code, handles git workflows, and supports natural language commands. Available via the terminal, IDE integration, or GitHub @claude mentions, it has become the canonical reference implementation for terminal-based AI coding agents. Installation is now via direct system installers (curl/brew on macOS/Linux, PowerShell/WinGet on Windows) rather than npm.

**Problem it solves:** Developers spend significant time on routine coding tasks — writing boilerplate, navigating unfamiliar codebases, managing git workflows, debugging — that can be accelerated or fully automated by an AI agent that understands the project context. Claude Code provides that agent directly in the terminal where developers already work.

**Why another one?** Claude Code is not "another" coding agent — it is Anthropic's first-party tool, meaning it has the deepest integration with Claude's capabilities. The ecosystem that has grown around it (Superpowers, gstack, Claude-Mem, Everything Claude Code, and more — many of which appear in today's top 25) demonstrates that it has become the platform other tools build upon.

---

## 25. [claude-hud](https://github.com/jarrodwatts/claude-hud)
> A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress.

**Language:** JavaScript  |  **Stars:** 12,154  |  **Forks:** 505  |  **Score:** 2,590  |  **Created:** 2026-01-02

**Background:** Claude HUD is a Claude Code plugin by Jarrod Watts that renders a persistent status display below the input line, showing context usage, active tools, running agents, and todo progress in real time. It installs via the Claude Code plugin marketplace and configures through a `/claude-hud:setup` slash command, providing at-a-glance visibility into what the agent is doing without interrupting the workflow.

**Problem it solves:** Claude Code operates as a black box during complex tasks — users cannot easily see how much context window is consumed, which tools are active, how many sub-agents are running, or what progress has been made on the todo list. Claude HUD makes this state visible at all times, reducing the anxiety of not knowing what the agent is doing and enabling better decisions about when to intervene.

**Why another one?** Existing Claude Code extensions focus on adding capabilities (memory, skills, workflows). Claude HUD focuses purely on observability — showing what is already happening rather than changing what happens. The always-visible statusline approach means no extra commands or windows are needed; the information is simply there.

---

> **Day's theme:** The Claude Code ecosystem has reached critical mass — seven of today's top 25 repos are Claude Code plugins, skills, or optimization layers, while the remaining entries split between agent orchestration infrastructure (Paperclip for autonomous companies, Deep Agents for agent harnesses, OpenViking for context databases) and domain-specific agents (trading, stock analysis, OSINT, autonomous ML research), signaling a shift from "can AI code?" to "how do we organize, observe, and scale entire teams of AI agents?"
