# Trendshift Report — 2026-04-04
**Total:** 25 repositories

---

## 1. [claw-code](https://github.com/ultraworkers/claw-code)
> The repo is finally unlocked. enjoy the party! The fastest repo in history to surpass 100K stars. Join Discord. Built in Rust using oh-my-codex.

**Language:** Rust  |  **Stars:** 173,712  |  **Forks:** 105,051  |  **Score:** 62,850  |  **Created:** 2026-03-31

**Background:** Claw Code by UltraWorkers is a Rust-based coding agent that exploded onto GitHub less than a week ago and has already surpassed 173,000 stars — making it the fastest repository in GitHub history to cross the 100K milestone. Built on top of the oh-my-codex framework, it offers a Rust workspace with documented parity tracking and a public roadmap.

**Problem it solves:** Existing coding agents built in JavaScript or Python face performance bottlenecks and memory overhead when processing large codebases. Claw Code rewrites the agent loop in Rust, delivering significantly faster file operations, lower memory usage, and native concurrency for parallel tool execution.

**Why another one?** The Rust foundation is the primary differentiator — while most coding agents rely on interpreted languages, Claw Code's compiled binary delivers measurably faster startup and execution. The oh-my-codex integration provides an extensible plugin system, and the project's meteoric star growth signals a community eager for performance-first agent tooling.

---

## 2. [openscreen](https://github.com/siddharthvaddem/openscreen)
> Create stunning demos for free. Open-source, no subscriptions, no watermarks, and free for commercial use. An alternative to Screen Studio.

**Language:** TypeScript  |  **Stars:** 24,842  |  **Forks:** 1,650  |  **Score:** 8,283  |  **Created:** 2025-10-10

**Background:** OpenScreen by siddharthvaddem is an open-source screen recording and demo creation tool positioned as a free alternative to Screen Studio. Still in beta, it has steadily grown to nearly 25,000 stars since its October 2025 launch, offering watermark-free commercial use with no subscription required.

**Problem it solves:** Creating polished product demos and screen recordings typically requires expensive tools like Screen Studio, which charge subscriptions and impose watermarks on free tiers. OpenScreen eliminates these barriers, providing professional-quality demo creation at zero cost.

**Why another one?** The fully open-source, no-watermark, commercially-free licensing model sets OpenScreen apart from both proprietary tools and other open-source alternatives that restrict commercial use. Its focus on demo creation rather than generic screen recording means it includes purpose-built features like zoom effects and smooth transitions out of the box.

---

## 3. [goose](https://github.com/block/goose)
> An open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM.

**Language:** Rust  |  **Stars:** 35,868  |  **Forks:** 3,369  |  **Score:** 7,714  |  **Created:** 2024-08-23

**Background:** Goose by Block (formerly Square) is an open-source AI agent that has recently moved to the Agentic AI Foundation (AAIF) at the Linux Foundation. Available as a desktop app, CLI, and API, it supports any LLM backend and has grown to nearly 36,000 stars. The move to a Linux Foundation project signals institutional maturation.

**Problem it solves:** Most AI coding tools are limited to code suggestions or completions. Goose acts as a full agent — it can install dependencies, execute commands, edit files, and run tests autonomously, bridging the gap between suggestion and execution.

**Why another one?** Goose's LLM-agnostic design means users are not locked into a single provider, and its multi-interface approach (desktop, CLI, API) meets developers wherever they work. The Linux Foundation backing and Block's enterprise heritage provide governance and stability that single-developer projects cannot match.

---

## 4. [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex)
> OmX - Oh My codeX: Your codex is not alone. Add hooks, agent teams, HUDs, and so much more.

**Language:** TypeScript  |  **Stars:** 18,118  |  **Forks:** 1,711  |  **Score:** 7,456  |  **Created:** 2026-02-02

**Background:** Oh My Codex (OMX) by Yeachan Heo is an extensibility layer for OpenAI's Codex agent, adding hooks, agent teams, heads-up displays, and runtime enhancements. Launched just two months ago, it has already reached over 18,000 stars and notably serves as the foundation for the top-ranked Claw Code project.

**Problem it solves:** Codex out of the box lacks workflow customization — there is no way to add pre/post hooks, coordinate multiple agents, or get real-time visibility into agent operations. OMX fills these gaps with a plugin architecture that layers additional capabilities onto the base agent.

**Why another one?** OMX positions itself as a meta-framework rather than a competing agent — it enhances Codex rather than replacing it. The hooks system enables workflow automation (linting before commits, tests after edits), while agent teams allow task decomposition across specialized sub-agents, a pattern increasingly demanded by complex development workflows.

---

## 5. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 138,686  |  **Forks:** 11,746  |  **Score:** 7,025  |  **Created:** 2025-10-09

**Background:** Superpowers by obra is a complete software development workflow built on composable skills for coding agents. With nearly 139,000 stars, it is one of the most popular agent framework repositories on GitHub. Its methodology centers on specification-first development — agents do not write code until they have teased out a clear spec from the user.

**Problem it solves:** Coding agents that jump straight into writing code often produce output that misses the actual requirement. Superpowers enforces a structured workflow: specification, design, implementation, and verification, ensuring agents build the right thing before building it right.

**Why another one?** The methodology-first approach is the differentiator. While most agent frameworks focus on tool capabilities, Superpowers prescribes a complete development methodology with composable skills that can be mixed and matched. Its massive star count reflects community validation that structured agent workflows produce better outcomes than ad-hoc prompting.

---

## 6. [OpenHarness](https://github.com/HKUDS/OpenHarness)
> OpenHarness: Open Agent Harness.

**Language:** Python  |  **Stars:** 6,934  |  **Forks:** 1,195  |  **Score:** 6,487  |  **Created:** 2026-04-01

**Background:** OpenHarness by HKUDS is a lightweight agent infrastructure framework released just three days ago that has quickly amassed nearly 7,000 stars. It delivers core agent primitives — tool-use, skills, memory, and multi-agent coordination — as a minimal, composable harness rather than a monolithic framework.

**Problem it solves:** Building agents from scratch requires implementing tool calling, memory persistence, skill loading, and coordination from the ground up. OpenHarness provides these primitives as reusable infrastructure, letting developers focus on agent logic rather than plumbing.

**Why another one?** OpenHarness prioritizes minimalism over features. Where frameworks like LangChain or CrewAI bundle opinionated abstractions, OpenHarness provides lightweight infrastructure that developers compose as needed. Its community-driven "Harness" contribution model encourages open development of shared agent building blocks.

---

## 7. [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks)
> Extracted system prompts from ChatGPT (GPT-5.4, GPT-5.3, Codex), Claude (Opus 4.6, Sonnet 4.6, Claude Code), Gemini (3.1 Pro, 3 Flash, CLI), Grok (4.2, 4), Perplexity, and more. Updated regularly.

**Language:** N/A  |  **Stars:** 37,709  |  **Forks:** 6,211  |  **Score:** 6,254  |  **Created:** 2025-05-03

**Background:** System Prompts Leaks by asgeirtj is a regularly updated collection of extracted system prompts from major AI products including ChatGPT, Claude, Gemini, Grok, and Perplexity. With nearly 38,000 stars, it serves as a transparency resource for researchers and developers studying how commercial AI products are configured.

**Problem it solves:** System prompts that shape AI behavior are proprietary and undocumented, making it impossible for researchers and developers to understand how commercial models are instructed. This repository provides extracted prompts that reveal guardrails, persona instructions, and capability boundaries across major platforms.

**Why another one?** This is the most comprehensive and actively maintained collection of its kind, covering the latest model versions (GPT-5.4, Opus 4.6, Gemini 3.1) as they release. Its breadth across providers and regular updates make it the de facto reference for system prompt research.

---

## 8. [awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
> Collection of DESIGN.md files that capture design systems from popular websites. Drop one into your project and let coding agents build matching UI.

**Language:** HTML  |  **Stars:** 15,726  |  **Forks:** 1,933  |  **Score:** 6,240  |  **Created:** 2026-03-31

**Background:** Awesome Design MD by VoltAgent is a curated collection of DESIGN.md files that encode the visual design systems of popular websites into structured markdown. Released just four days ago, it has already surpassed 15,000 stars — reflecting strong demand for bridging design and AI-assisted development.

**Problem it solves:** Coding agents can generate functional UI but struggle to match existing design systems because they lack structured design context. DESIGN.md files provide agents with explicit typography, color, spacing, and component specifications, enabling them to produce UI that matches a target design system.

**Why another one?** The DESIGN.md format creates a new category — design-system-as-code specifically optimized for AI consumption. Unlike Figma files or style guides intended for humans, these files are structured for coding agents to parse and apply directly, making design consistency achievable without manual design review.

---

## 9. [onyx](https://github.com/onyx-dot-app/onyx)
> Open Source AI Platform - AI Chat with advanced features that works with every LLM.

**Language:** Python  |  **Stars:** 25,588  |  **Forks:** 3,411  |  **Score:** 5,462  |  **Created:** 2023-04-27

**Background:** Onyx is an open-source AI chat platform that supports every major LLM provider and includes advanced features like RAG, document ingestion, and multi-model conversations. Launched in April 2023, it has steadily grown to over 25,000 stars as a self-hostable alternative to commercial AI chat products.

**Problem it solves:** Organizations that want to use AI chat internally face a choice between vendor-locked commercial products and building custom solutions from scratch. Onyx provides a complete, self-hostable AI chat platform with enterprise features — document search, permissions, and multi-model support — out of the box.

**Why another one?** Onyx's LLM-agnostic architecture and self-hosting model give organizations full control over their data and model choices. The integrated RAG pipeline means users can chat with their own documents without configuring separate vector databases or embedding pipelines, reducing the operational complexity of enterprise AI deployment.

---

## 10. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Language:** Shell  |  **Stars:** 110,318  |  **Forks:** 18,343  |  **Score:** 5,335  |  **Created:** 2025-02-22

**Background:** Claude Code by Anthropic is the official agentic coding tool for the Claude model family, operating directly in the terminal. With over 110,000 stars, it remains one of the most popular developer tools on GitHub. Its deep codebase understanding and natural language interface have made it a staple in many developers' workflows.

**Problem it solves:** Developers spend significant time on routine tasks — navigating unfamiliar codebases, writing boilerplate, managing git workflows, and debugging. Claude Code automates these tasks through natural language commands while maintaining the developer's terminal-native workflow.

**Why another one?** As Anthropic's first-party tool, Claude Code has direct access to the latest Claude model capabilities and optimizations. Its terminal-native design avoids the context-switching of IDE plugins, and its deep codebase understanding (file reading, search, git integration) provides more accurate assistance than tools that operate on isolated code snippets.

---

## 11. [autoagent](https://github.com/kevinrgu/autoagent)
> Autonomous harness engineering.

**Language:** Python  |  **Stars:** 3,726  |  **Forks:** 422  |  **Score:** 5,000  |  **Created:** 2026-04-02

**Background:** AutoAgent by kevinrgu (Third Layer) is a Python framework for autonomous harness engineering — the practice of having AI agents configure, optimize, and extend their own agent harnesses. Released just two days ago, it has quickly gained nearly 4,000 stars, riding the wave of interest in self-configuring agent systems.

**Problem it solves:** Setting up and tuning agent harnesses — tool configurations, memory settings, skill selections — is a manual, iterative process. AutoAgent lets agents autonomously configure their own infrastructure, reducing the human effort needed to optimize agent performance for specific tasks.

**Why another one?** AutoAgent introduces the concept of agents engineering their own harnesses rather than humans configuring them. This meta-agent approach moves beyond static configuration to dynamic self-optimization, positioning it as a next-generation take on agent infrastructure that learns and adapts to the task at hand.

---

## 12. [pretext](https://github.com/chenglou/pretext)
> Fast, accurate & comprehensive text measurement & layout.

**Language:** TypeScript  |  **Stars:** 39,924  |  **Forks:** 2,122  |  **Score:** 4,966  |  **Created:** 2026-03-07

**Background:** Pretext by chenglou is a pure JavaScript/TypeScript library for multiline text measurement and layout that bypasses DOM measurements entirely. With nearly 40,000 stars in just under a month, it has become one of the most popular new frontend libraries, supporting rendering to DOM, Canvas, SVG, and soon server-side environments.

**Problem it solves:** DOM-based text measurement using getBoundingClientRect or offsetHeight triggers expensive layout reflows that degrade application performance. Pretext implements its own text measurement logic using the browser's font engine as ground truth, eliminating reflow overhead while maintaining pixel-perfect accuracy.

**Why another one?** Pretext's reflow-free architecture provides a fundamental performance advantage over any library that relies on DOM measurements. Its multi-target rendering (DOM, Canvas, SVG) makes it uniquely versatile, and its comprehensive language support handles complex scripts and bidirectional text that simpler measurement libraries ignore.

---

## 13. [sherlock](https://github.com/sherlock-project/sherlock)
> Hunt down social media accounts by username across social networks.

**Language:** Python  |  **Stars:** 80,033  |  **Forks:** 9,304  |  **Score:** 4,926  |  **Created:** 2018-12-24

**Background:** Sherlock is a long-standing open-source OSINT tool that searches for usernames across hundreds of social networks simultaneously. With over 80,000 stars and more than seven years of development, it remains the definitive tool for cross-platform username reconnaissance.

**Problem it solves:** Manually checking whether a username exists across dozens of social media platforms is tedious and time-consuming. Sherlock automates this by querying hundreds of sites in parallel and reporting which platforms have accounts matching the target username.

**Why another one?** Sherlock's longevity and community maintenance mean it has the broadest platform coverage of any username search tool. Its continuous updates keep pace with new social networks and API changes, and its simplicity (single command, instant results) keeps it relevant against more complex OSINT frameworks.

---

## 14. [opencli](https://github.com/jackwener/opencli)
> Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime.

**Language:** TypeScript  |  **Stars:** 14,025  |  **Forks:** 1,286  |  **Score:** 4,526  |  **Created:** 2026-03-14

**Background:** OpenCLI by jackwener transforms any website, Electron app, or local binary into a standardized command-line interface. It reuses Chrome login sessions for zero-risk authentication and provides AI-powered discovery of available commands. With over 14,000 stars in three weeks, it has established itself as a leading tool for CLI-native workflows.

**Problem it solves:** Developers constantly context-switch between web UIs, desktop apps, and terminal tools, each with different interfaces and authentication flows. OpenCLI unifies all of these behind a consistent CLI interface, allowing both users and AI agents to interact with any tool through a single command-line hub.

**Why another one?** The browser session reuse is the killer feature — OpenCLI leverages existing Chrome logins rather than requiring separate API keys or OAuth flows. The AGENT.md integration positions it uniquely for AI-native workflows where agents need to discover and invoke tools programmatically.

---

## 15. [mlx-vlm](https://github.com/Blaizzy/mlx-vlm)
> MLX-VLM is a package for inference and fine-tuning of Vision Language Models (VLMs) on your Mac using MLX.

**Language:** Python  |  **Stars:** 4,134  |  **Forks:** 439  |  **Score:** 4,332  |  **Created:** 2024-04-16

**Background:** MLX-VLM by Blaizzy is a package for running and fine-tuning Vision Language Models on Apple Silicon using the MLX framework. It supports both vision-language and omni models (with audio and video support), making it one of the most complete local multimodal AI packages for Mac users.

**Problem it solves:** Running vision language models locally on Mac hardware requires navigating incompatible frameworks and limited Apple Silicon support. MLX-VLM provides a unified package that handles inference and fine-tuning of VLMs natively on Apple's MLX framework, fully utilizing the GPU and unified memory architecture.

**Why another one?** MLX-VLM is purpose-built for Apple Silicon, unlike ports of CUDA-first libraries that run suboptimally on Mac hardware. Its support for omni models (audio + video + vision) goes beyond what most local inference packages offer, and the fine-tuning capability enables domain-specific model adaptation directly on consumer Mac hardware.

---

## 16. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 74,280  |  **Forks:** 11,645  |  **Score:** 4,068  |  **Created:** 2025-10-13

**Background:** Agency Agents by msitarzewski is a collection of specialized AI agent personas, each designed as a domain expert with distinct personality, processes, and deliverables. With over 74,000 stars, it has become one of the most popular agent persona libraries, offering roles from frontend development to community management.

**Problem it solves:** AI agents without specialized persona definitions produce generic, undifferentiated outputs. Agency Agents provides pre-built expert personas that encode domain-specific knowledge, workflows, and quality standards, enabling agents to produce work that reflects genuine specialization.

**Why another one?** The depth of persona engineering sets Agency Agents apart — each agent has not just a role description but defined processes, deliverable templates, and personality traits. This goes well beyond simple system prompts, creating agents that behave like experienced specialists rather than generic assistants.

---

## 17. [emdash](https://github.com/emdash-cms/emdash)
> EmDash is a full-stack TypeScript CMS based on Astro; the spiritual successor to WordPress.

**Language:** TypeScript  |  **Stars:** 7,578  |  **Forks:** 548  |  **Score:** 4,014  |  **Created:** 2026-04-01

**Background:** EmDash is a full-stack TypeScript CMS built on Astro and Cloudflare, positioning itself as the spiritual successor to WordPress. Released just three days ago, it has already gained over 7,500 stars. Its key innovation is running plugins in sandboxed Worker isolates, solving the fundamental security problem of WordPress's plugin architecture.

**Problem it solves:** WordPress's PHP plugin system runs untrusted code with full server access, creating a massive attack surface. EmDash rebuilds the plugin concept on Cloudflare Workers with sandboxed execution, type-safe APIs, and serverless deployment, eliminating entire categories of security vulnerabilities.

**Why another one?** The sandboxed plugin architecture is the defining feature. While other modern CMS platforms (Strapi, Payload) offer TypeScript and modern stacks, EmDash uniquely solves the plugin security problem through Worker isolates. Its Astro foundation provides excellent performance and developer experience, and the Cloudflare deployment model offers global edge delivery.

---

## 18. [magic-resume](https://github.com/JOYCEQL/magic-resume)
> Free online AI resume editor, the only official website is https://magicv.art.

**Language:** TypeScript  |  **Stars:** 4,975  |  **Forks:** 576  |  **Score:** 2,618  |  **Created:** 2024-05-19

**Background:** Magic Resume by JOYCEQL is a free, open-source AI-powered resume editor built with TanStack Start and Framer Motion. Licensed under Apache 2.0, it provides a polished editing experience with AI-assisted content suggestions and smooth animations, all without requiring a subscription.

**Problem it solves:** Professional resume builders charge subscriptions and lock users into proprietary formats. Magic Resume provides a free, self-hostable alternative with AI-powered content improvement, modern animations, and export capabilities — all without cost barriers or vendor lock-in.

**Why another one?** The combination of AI-powered content suggestions with a modern, animation-rich editing experience sets Magic Resume apart from static resume templates. Its open-source nature means users retain full control over their data, and the TanStack Start foundation provides a fast, modern web experience.

---

## 19. [opencode](https://github.com/anomalyco/opencode)
> The open source coding agent.

**Language:** TypeScript  |  **Stars:** 138,763  |  **Forks:** 15,332  |  **Score:** 2,490  |  **Created:** 2025-04-30

**Background:** OpenCode by Anomaly is the leading open-source coding agent, with nearly 139,000 stars making it one of the most popular developer tools on GitHub. Originally launched in April 2025, it provides a complete agent experience with a console UI, multi-provider LLM support, and an extensible tool system.

**Problem it solves:** Proprietary coding agents lock developers into specific models and ecosystems. OpenCode provides a fully open-source alternative that supports any LLM provider, giving developers freedom of choice while maintaining feature parity with commercial tools.

**Why another one?** OpenCode's massive community and open-source governance ensure it evolves with developer needs rather than vendor priorities. Its multi-provider support means developers can switch between Claude, GPT, Gemini, and local models without changing their workflow, and the console UI provides a rich terminal experience beyond simple command-line interactions.

---

## 20. [frontend-slides](https://github.com/zarazhangrui/frontend-slides)
> Create beautiful slides on the web using Claude's frontend skills.

**Language:** Shell  |  **Stars:** 13,289  |  **Forks:** 990  |  **Score:** 2,464  |  **Created:** 2026-01-28

**Background:** Frontend Slides by zarazhangrui is a Claude Code skill for creating animation-rich HTML presentations from scratch or by converting PowerPoint files. It uses a "show, don't tell" approach — instead of asking users to describe aesthetic preferences in words, it generates visual previews and lets users pick what they like.

**Problem it solves:** Non-designers struggle to create visually compelling presentations because tools like PowerPoint require manual layout and design decisions. Frontend Slides leverages Claude's frontend skills to generate beautiful, animated HTML presentations from natural language descriptions.

**Why another one?** The visual preview workflow is the key differentiator. Rather than iterating on text-based prompts, users see multiple design options rendered as actual web pages and select their preferred style. The PowerPoint conversion feature bridges the gap between existing slide decks and modern web-based presentations.

---

## 21. [skills](https://github.com/anthropics/skills)
> Public repository for Agent Skills.

**Language:** Python  |  **Stars:** 112,019  |  **Forks:** 12,695  |  **Score:** 2,374  |  **Created:** 2025-09-22

**Background:** Anthropic's Skills repository is the official home for Claude agent skills — structured instruction sets that teach Claude how to complete specialized tasks repeatably. With over 112,000 stars, it is the most popular skills repository and serves as the reference implementation for the Agent Skills standard defined at agentskills.io.

**Problem it solves:** AI agents produce inconsistent results on specialized tasks because they rely on general knowledge rather than domain-specific workflows. Skills provide structured, repeatable instructions — including scripts, resources, and validation steps — that ensure consistent, high-quality output for specific task types.

**Why another one?** As Anthropic's official repository, it defines the skills standard that third-party skills are built against. Its integration with Claude Code means skills are loaded dynamically based on task context, and the repository's scale (112K stars) ensures a broad, community-vetted collection of skills across domains.

---

## 22. [fff.nvim](https://github.com/dmtrKovalenko/fff.nvim)
> The fastest and the most accurate file search toolkit for AI agents, Neovim, Rust, C, and NodeJS.

**Language:** Rust  |  **Stars:** 3,829  |  **Forks:** 160  |  **Score:** 2,346  |  **Created:** 2025-07-31

**Background:** FFF (Fast File Finder) by dmtrKovalenko is a high-performance file search toolkit written in Rust with bindings for Neovim, C, and NodeJS, plus an MCP server for AI agent integration. Its built-in memory system provides persistent search context, making it particularly effective for AI agents that need fast, contextual file discovery.

**Problem it solves:** AI agents waste tokens and time on slow file searches, especially in large codebases. FFF provides sub-millisecond file search with built-in memory that remembers previous search context, dramatically reducing the number of search iterations agents need to find relevant files.

**Why another one?** The Rust-native performance combined with the built-in memory system creates a unique value proposition. While tools like ripgrep are fast, FFF adds semantic memory on top of raw speed, and its MCP server integration means any AI agent can use it as a tool without custom integration work.

---

## 23. [pi-mono](https://github.com/badlogic/pi-mono)
> AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods.

**Language:** TypeScript  |  **Stars:** 32,635  |  **Forks:** 3,567  |  **Score:** 2,267  |  **Created:** 2025-08-09

**Background:** Pi-mono by badlogic is a comprehensive AI agent toolkit that bundles a coding agent CLI, unified LLM API, terminal and web UI libraries, a Slack bot, and vLLM pod management into a single monorepo. With over 32,000 stars, it has grown into a full-stack agent platform. The project is currently in an OSS weekend maintenance period through April 13.

**Problem it solves:** Building a complete agent platform requires stitching together separate tools for LLM access, UI rendering, chat interfaces, and model hosting. Pi-mono provides all of these as a cohesive, tested package — from the CLI agent to the vLLM inference pods — eliminating integration friction.

**Why another one?** The monorepo approach means all components (CLI, API, UI, bot, inference) are designed to work together and are versioned as a unit. Unlike ecosystems where each component has its own release cycle and compatibility matrix, pi-mono guarantees cross-component compatibility and provides a single codebase to learn.

---

## 24. [ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills)
> Open-source AI marketing skills — growth experiments, sales pipeline, content ops, outbound, SEO, and finance automation.

**Language:** Python  |  **Stars:** 1,608  |  **Forks:** 351  |  **Score:** 2,240  |  **Created:** 2026-03-28

**Background:** AI Marketing Skills by Eric Osiu (Single Brain) is a collection of Claude Code skills specifically designed for marketing and sales teams. Battle-tested on real pipelines generating millions in revenue, it provides complete workflows for growth experiments, sales pipeline management, content operations, outbound campaigns, SEO, and finance automation.

**Problem it solves:** Marketing teams adopting AI coding agents lack domain-specific workflows — generic prompts produce generic marketing output. These skills encode proven marketing processes (scoring algorithms, expert panels, automation pipelines) that translate directly into executable agent workflows.

**Why another one?** These are not prompts but complete, executable workflows with scripts, scoring algorithms, and automation pipelines built from real revenue-generating operations. The marketing-specific focus fills a gap in the skills ecosystem, which is heavily skewed toward engineering tasks, and the production battle-testing provides credibility that theoretical skills lack.

---

## 25. [prompts.chat](https://github.com/f/prompts.chat)
> f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-hostable.

**Language:** HTML  |  **Stars:** 157,821  |  **Forks:** 20,657  |  **Score:** 2,216  |  **Created:** 2022-12-05

**Background:** Prompts.chat (formerly Awesome ChatGPT Prompts) is the world's largest open-source prompt library for AI, with nearly 158,000 stars and over three years of community curation. It provides a platform for sharing, discovering, and collecting prompts that work across all major AI models, and is now self-hostable.

**Problem it solves:** AI users spend time crafting prompts from scratch for common tasks when effective prompts already exist. Prompts.chat provides a searchable, community-curated library of proven prompts, reducing the effort needed to get high-quality outputs from AI models.

**Why another one?** With 158,000 stars and years of community contributions, prompts.chat has achieved network effects that newer prompt libraries cannot match. Its evolution from a GitHub list to a self-hostable platform with cross-model support reflects the maturation of prompt sharing from a novelty to essential infrastructure.

---

> **Day's theme:** The agent ecosystem fragments into specialized layers — from blazing-fast Rust runtimes and self-configuring harnesses to design-system-as-code files and marketing-specific skills — as the community moves beyond building monolithic agents toward composable, domain-specific tooling where performance, security isolation, and workflow specialization matter more than general-purpose capabilities.
