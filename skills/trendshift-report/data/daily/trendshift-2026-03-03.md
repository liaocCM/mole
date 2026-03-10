# Trendshift Report — 2026-03-03
**Total:** 25 repositories

---

## 1. [RuView](https://github.com/ruvnet/RuView)
> WiFi DensePose turns commodity WiFi signals into real-time human pose estimation, vital sign monitoring, and presence detection — all without a single pixel of video.

**Language:** Rust  |  **Stars:** 31,832  |  **Forks:** 4,198  |  **Score:** 24,100  |  **Created:** 2025-06-07

**Background:** RuView is an edge AI perception system by ruvnet that uses WiFi Channel State Information (CSI) to reconstruct human body pose, breathing rate, heart rate, and presence without cameras. Built on top of RuVector, it implements the WiFi DensePose technique first explored in Carnegie Mellon's academic research. The system runs on ESP32 sensor meshes costing as little as $1 per node, learning the RF signature of each room over time and continuously adapting.

**Problem it solves:** Camera-based monitoring fails in darkness, through walls, and raises serious privacy concerns. RuView provides the same positional awareness — human pose, vital signs, occupancy — using only WiFi signal disturbances that pass through solid objects. It requires no internet, no labeled training data, and no cloud inference, making it suitable for elder care, secure facilities, and smart buildings.

**Why another one?** RuView's score of 24,100 — nearly triple the second-place project — reflects massive viral attention. The project doubled its star count overnight (from 15K yesterday to 31K today), likely driven by social media coverage of its "see through walls with WiFi" capabilities. The edge-only, camera-free approach strikes a chord with both privacy advocates and IoT developers looking for novel sensing modalities.

---

## 2. [worldmonitor](https://github.com/koala73/worldmonitor)
> Real-time global intelligence dashboard — AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking.

**Language:** TypeScript  |  **Stars:** 34,697  |  **Forks:** 5,833  |  **Score:** 8,441  |  **Created:** 2026-01-08

**Background:** World Monitor is an open-source situational awareness dashboard built in TypeScript that consolidates news, geopolitical events, and infrastructure status into a unified interface. It ships with domain-specific variants for tech, finance, commodities, and a "happy news" view, each with tailored data sources and visualization priorities. The project has maintained strong momentum since January 2026.

**Problem it solves:** Professionals monitoring global events must switch between dozens of news sites, financial dashboards, and infrastructure monitoring tools. World Monitor aggregates, classifies, and prioritizes information across all these domains into a single AI-powered interface, reducing the time from event occurrence to awareness.

**Why another one?** World Monitor's score more than doubled from yesterday (3,572 to 8,441), indicating accelerating adoption. Its multi-variant approach — deploying the same core engine with different configurations for different professional contexts — is more practical than general-purpose dashboards that try to serve everyone equally. The AGPL v3 license permits self-hosting with full customization.

---

## 3. [visual-explainer](https://github.com/nicobailon/visual-explainer)
> An agent skill that turns complex terminal output into styled HTML pages you actually want to read.

**Language:** HTML  |  **Stars:** 5,918  |  **Forks:** 405  |  **Score:** 7,314  |  **Created:** 2026-02-16

**Background:** Visual-explainer by Nico Bailon transforms agent-generated content — architecture diagrams, diff reviews, requirement comparisons — from ASCII art into self-contained, styled HTML pages with real typography, dark/light themes, and interactive Mermaid diagrams with zoom and pan. It works across Claude Code (via marketplace), OpenAI Codex, Pi, and other agent platforms.

**Problem it solves:** Every coding agent defaults to ASCII art for visualizations. Box-drawing characters and pipe-delimited tables become unreadable beyond trivial complexity. Visual-explainer generates browser-rendered HTML that handles complex flowcharts, multi-column comparison tables, and architectural diagrams at any scale.

**Why another one?** Visual-explainer's score jumped from 4,558 to 7,314, reflecting growing recognition that terminal output is a major UX bottleneck for coding agents. Its cross-agent compatibility (Claude Code, Codex, Pi) and zero-dependency output (single HTML file, no build step) make it the path of least resistance for any agent user who has struggled with ASCII diagrams.

---

## 4. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> Discover 5490+ community-built OpenClaw skills, organized by category.

**Language:**   |  **Stars:** 33,181  |  **Forks:** 3,144  |  **Score:** 6,619  |  **Created:** 2026-01-25

**Background:** The canonical directory for the OpenClaw skill ecosystem, maintained by VoltAgent. It catalogs over 5,490 skills sourced from ClawHub (OpenClaw's public registry), organized by category for discoverability. VoltAgent also curates a related collection of AI agent research papers, positioning itself as a meta-layer for the agent development community.

**Problem it solves:** With thousands of skills in the OpenClaw ecosystem, finding the right one for a specific task requires either knowing its exact name or browsing an unstructured registry. This awesome-list provides curated, categorized discovery that the raw registry cannot.

**Why another one?** This list keeps trending because the OpenClaw skill count is growing faster than users can track. Each new batch of skills drives users back to this directory. The 33K+ stars make it the definitive starting point for OpenClaw customization, functioning as the "app store" that OpenClaw's CLI-first design does not natively provide.

---

## 5. [CoPaw](https://github.com/agentscope-ai/CoPaw)
> CoPaw — a collaborative AI agent framework by AgentScope

**Language:** Python  |  **Stars:** 9,613  |  **Forks:** 1,072  |  **Score:** 5,787  |  **Created:** 2026-02-24

**Background:** CoPaw is a Python-based collaborative agent framework from AgentScope AI, released at the end of February 2026. Licensed under Apache 2.0, it provides primitives for multi-agent collaboration — shared state, task delegation, and coordination — distributed via PyPI. Its star count doubled from yesterday's score (2,917 to 5,787), reflecting strong second-week momentum.

**Problem it solves:** Most agent frameworks optimize for single-agent performance. When multiple agents need to collaborate on complex tasks — sharing context, dividing work, resolving conflicts — developers must build coordination logic from scratch. CoPaw provides these collaboration primitives as a library, letting developers define agent behaviors rather than distributed systems plumbing.

**Why another one?** CoPaw's "collaboration-first" design philosophy distinguishes it from autonomy-focused frameworks like OpenFang or LangGraph. The AgentScope branding suggests integration with a broader ecosystem of agent tools, and the Apache 2.0 license removes commercial use barriers. Its rapid growth suggests the community has been waiting for a well-engineered collaboration framework.

---

## 6. [awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
> A community collection of OpenClaw use cases for making life easier.

**Language:**   |  **Stars:** 22,126  |  **Forks:** 1,817  |  **Score:** 5,364  |  **Created:** 2026-02-08

**Background:** This community-curated collection by Hesam Sheikh documents 36+ real-world use cases for OpenClaw across social media, productivity, development, finance, health, and home automation. Each use case provides step-by-step instructions for reproducing the workflow, bridging the gap between "I have an AI assistant" and "here is how it saves me 30 minutes daily."

**Problem it solves:** The biggest barrier to OpenClaw adoption is not technical setup but imagination — users do not know what to use it for. This repository provides concrete, tested recipes for daily workflows that users can copy and adapt without understanding the underlying skill system.

**Why another one?** Maintains a steady position near the top because new OpenClaw users discover it through the onboarding flow. Unlike the skills directory (which is tool-oriented), this collection is outcome-oriented, making it more accessible to non-technical users who care about results, not implementation details.

---

## 7. [prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)
> A comprehensive step-by-step understanding of how to engineer optimal prompts within Claude.

**Language:** Jupyter Notebook  |  **Stars:** 33,102  |  **Forks:** 3,371  |  **Score:** 5,176  |  **Created:** 2024-04-02

**Background:** Anthropic's official prompt engineering tutorial, structured as 9 chapters with hands-on exercises in Jupyter Notebooks. It covers everything from basic prompt structure to advanced techniques, using Claude 3 Haiku for cost-effective experimentation. Also available as a Google Sheets version using the Claude for Sheets extension.

**Problem it solves:** Generic prompt engineering advice ("be clear and specific") does not account for model-specific behavior. This tutorial teaches Claude-specific techniques with immediate feedback through interactive notebooks, making it the fastest path from "Claude beginner" to "effective Claude user."

**Why another one?** The score more than doubled from yesterday (2,386 to 5,176), suggesting a surge in new Claude users — possibly correlated with a product launch or pricing change. As the authoritative first-party resource, it captures every wave of new Claude adoption. The interactive format with built-in experimentation remains more effective than passive documentation.

---

## 8. [airi](https://github.com/moeru-ai/airi)
> Re-creating Neuro-sama, a soul container of AI waifu / virtual characters to bring them into our world.

**Language:** TypeScript  |  **Stars:** 31,704  |  **Forks:** 3,103  |  **Score:** 4,906  |  **Created:** 2024-12-01

**Background:** Project AIRI is an open-source framework for creating AI virtual characters with persistent personality, voice, and visual presence. Inspired by the Neuro-sama VTuber phenomenon, it provides a modular system integrating LLM backends, TTS engines, avatar rendering, and memory systems. It supports 8+ languages including English, Chinese, Japanese, Korean, Russian, Vietnamese, and French.

**Problem it solves:** Building a convincing AI virtual character requires integrating disparate systems — language models, voice synthesis, visual rendering, personality persistence — into a coherent pipeline. AIRI provides this integration as a single framework, dramatically reducing the engineering effort from months to days.

**Why another one?** AIRI's consistent presence in the top 10 (score increased from 4,086 to 4,906) reflects the VTuber and AI companion community's sustained interest. Its multi-language support and active Discord community distinguish it from English-only projects, and the Neuro-sama inspiration gives it a clear design target that prevents feature sprawl.

---

## 9. [superpowers](https://github.com/obra/superpowers)
> A complete software development workflow for your coding agents, built on composable skills.

**Language:** Shell  |  **Stars:** 75,000  |  **Forks:** 5,793  |  **Score:** 4,846  |  **Created:** 2025-10-09

**Background:** Jesse Vincent's Superpowers is a structured development methodology for coding agents that installs into Claude Code, Cursor, Codex, and OpenCode. It enforces spec-first design, chunked review, TDD, and subagent-driven development. At 75K stars, it is the most widely adopted agent skill framework.

**Problem it solves:** Coding agents without guardrails produce mediocre code — they skip planning, ignore tests, and drift from user intent during long sessions. Superpowers imposes a professional software engineering methodology on agents, enabling multi-hour autonomous sessions without human intervention.

**Why another one?** Score increased from 3,539 to 4,846, indicating growing adoption. Superpowers works across multiple agents (not tied to one vendor), which gives it unusual staying power — as new agents launch, Superpowers ports to each one, reaching fresh audiences. The subagent-driven development pattern it pioneered has become the standard for long-running agent sessions.

---

## 10. [vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands)
> A dark color theme for VS Code inspired by easemate IDE — floating glass panels, rounded corners, smooth animations.

**Language:** PowerShell  |  **Stars:** 5,123  |  **Forks:** 151  |  **Score:** 4,724  |  **Created:** 2026-02-14

**Background:** Islands Dark is a VS Code theme created by bwya77 that recreates the aesthetic of the easemate IDE. It combines a deep dark canvas (#131217) with floating glass-effect panels, rounded corners on all UI elements, pill-shaped scrollbars, and smooth CSS transitions. The theme requires custom CSS injection alongside the standard color theme to achieve its distinctive glassmorphism look.

**Problem it solves:** VS Code's default theming system controls colors but not UI geometry or animations. Islands Dark pushes beyond these limits by injecting custom CSS that adds rounded corners, glass-effect borders with directional light simulation, and hover-triggered transitions — visual refinements that color themes alone cannot achieve.

**Why another one?** The easemate IDE's distinctive aesthetic generated significant social media attention, and Islands Dark is the closest VS Code recreation. Its two-part installation (color theme + CSS injection) is unusual but necessary to achieve effects outside VS Code's theming API. The high star-to-fork ratio (34:1) confirms this is a "use it" rather than "fork and modify" project.

---

## 11. [public-apis](https://github.com/public-apis/public-apis)
> A collective list of free APIs for use in software and web development.

**Language:** Python  |  **Stars:** 405,531  |  **Forks:** 43,795  |  **Score:** 4,697  |  **Created:** 2016-03-20

**Background:** Public APIs is one of GitHub's most-starred repositories, a community-curated directory of free APIs organized by category — animals, authentication, blockchain, books, business, and dozens more. Maintained since 2016 with APILayer as a sponsor, it serves as the starting point for developers looking for external data sources and services to integrate into their projects.

**Problem it solves:** Discovering free, publicly available APIs for a specific purpose requires extensive Googling and testing. This curated list provides a browsable, categorized directory with descriptions and authentication requirements, saving developers hours of research when starting new projects.

**Why another one?** Public APIs trends cyclically as new developers discover it and as existing users return for reference. Its 405K+ stars and 10-year maintenance history make it an institution rather than a project. The API economy's continued growth ensures a steady stream of new entries and new users.

---

## 12. [claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)
> 170+ ready-to-use scientific and research skills for AI agents — biology, chemistry, medicine, genomics, molecular dynamics, and more.

**Language:** Python  |  **Stars:** 14,105  |  **Forks:** 1,530  |  **Score:** 4,566  |  **Created:** 2025-10-19

**Background:** K-Dense AI's collection of 170+ scientific skills and 250+ database interfaces for the open Agent Skills standard. It covers domains from cancer genomics and drug-target binding to FRED economic data and geospatial science. Works with Cursor, Claude Code, Codex, and other compatible agents. K-Dense Web is the commercial platform built on these same open-source skills.

**Problem it solves:** General-purpose coding agents lack domain-specific knowledge for scientific computing — they do not know how to query PDB for protein structures, run molecular docking workflows, or perform gene expression analysis. These skills provide the specialized knowledge and API integrations that make agents useful in laboratory and research settings.

**Why another one?** Score increased from 3,848 to 4,566. The collection keeps growing (now 170 skills, up from earlier counts), and each addition brings renewed attention. The open Agent Skills standard ensures these skills work across multiple agents, not just Claude Code, which broadens the potential user base beyond any single ecosystem.

---

## 13. [openclaw](https://github.com/openclaw/openclaw)
> OpenClaw — Personal AI Assistant that runs on your own devices across 20+ messaging channels.

**Language:** TypeScript  |  **Stars:** 289,626  |  **Forks:** 54,924  |  **Score:** 4,485  |  **Created:** 2025-11-24

**Background:** OpenClaw is the 290K-star personal AI assistant platform supporting 20+ messaging channels. Originally Clawdbot, then MoltBot, now OpenClaw, it provides an always-on assistant that meets users in WhatsApp, Telegram, Slack, Discord, Signal, iMessage, and more. The Gateway architecture separates the control plane from the assistant experience.

**Problem it solves:** Users should not need to switch apps to interact with their AI assistant. OpenClaw's multi-channel architecture means the assistant is available wherever the user already communicates, with persistent memory and state across all channels.

**Why another one?** Score doubled from yesterday (2,128 to 4,485), likely driven by the surrounding ecosystem activity (Studio, use cases, skills). OpenClaw's 290K stars represent a platform effect — it keeps trending because the ecosystem around it (5,490+ skills, 36+ documented use cases, third-party dashboards) generates constant cross-referencing.

---

## 14. [ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)
> A course teaching everything you need to know to start building AI Agents.

**Language:** Jupyter Notebook  |  **Stars:** 53,475  |  **Forks:** 18,576  |  **Score:** 4,298  |  **Created:** 2024-11-28

**Background:** Microsoft's "AI Agents for Beginners" is an educational course covering the fundamentals of building AI agents. Part of Microsoft's "for Beginners" series (alongside Generative AI for Beginners and ML for Beginners), it uses Jupyter Notebooks for hands-on learning. The course is community-translated into 15+ languages via GitHub Actions, ensuring global accessibility.

**Problem it solves:** The AI agent space moves faster than documentation can keep up. Developers need structured learning paths that start from fundamentals and build toward production-ready agent systems. This course provides that progression with Microsoft's pedagogical rigor and community translation infrastructure.

**Why another one?** Microsoft's educational repos consistently trend because of their production quality, multi-language support, and the Microsoft brand's reach. The 18K+ forks indicate active use in classrooms and bootcamps worldwide. As agent development becomes a mainstream skill, entry-level educational resources capture a large audience.

---

## 15. [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
> A compilation of well-written, step-by-step guides for re-creating our favorite technologies from scratch.

**Language:** Markdown  |  **Stars:** 473,392  |  **Forks:** 44,374  |  **Score:** 3,964  |  **Created:** 2018-05-09

**Background:** Build Your Own X is one of GitHub's top 5 most-starred repositories, a curated collection of tutorials for rebuilding fundamental technologies — databases, operating systems, compilers, neural networks, web servers, Docker, Git, and more. Maintained by CodeCrafters since 2018, it embodies the Feynman principle: "What I cannot create, I do not understand."

**Problem it solves:** Understanding how technologies work at a deep level is difficult from documentation alone. These step-by-step build-from-scratch tutorials force engagement with implementation details, producing a fundamentally deeper understanding than reading source code or watching lectures.

**Why another one?** Build Your Own X trends perpetually because new developers discover it regularly and because the collection continuously grows with new tutorials. At 473K stars, it functions as infrastructure — a permanent reference that the developer community returns to whenever they want to understand a technology's internals.

---

## 16. [openfang](https://github.com/RightNow-AI/openfang)
> The Agent Operating System — open-source Agent OS built in Rust

**Language:** Rust  |  **Stars:** 12,521  |  **Forks:** 1,385  |  **Score:** 3,805  |  **Created:** 2026-02-24

**Background:** OpenFang is RightNow AI's open-source Agent Operating System — 137K lines of Rust across 14 crates, 1,767+ tests, zero clippy warnings, shipped as a single binary. At v0.3.30 (Security Hardening Release), it provides a full runtime for autonomous agents with process management, sandboxing, and inter-agent communication.

**Problem it solves:** Agent frameworks that wrap Python around LLM calls lack the performance, safety, and deployment characteristics needed for always-on autonomous operation. OpenFang provides an OS-level foundation — process isolation, resource management, security sandboxing — that Python-based frameworks cannot match.

**Why another one?** Score dropped from yesterday (5,379 to 3,805) as the initial launch burst normalizes, but OpenFang remains in the top 20. The "Agent OS" positioning — not a framework, not a wrapper, but a full operating system — is genuinely distinct in a market dominated by Python libraries. The Rust foundation provides the reliability guarantees that mission-critical agent deployments require.

---

## 17. [llmfit](https://github.com/AlexsJones/llmfit)
> Hundreds of models & providers. One command to find what runs on your hardware.

**Language:** Rust  |  **Stars:** 13,738  |  **Forks:** 760  |  **Score:** 3,723  |  **Created:** 2026-02-15

**Background:** LLMFit by Alex Jones is a Rust CLI tool that right-sizes LLM models to your system's hardware. It detects your CPU, RAM, and GPU(s), scores each model across quality, speed, fit, and context dimensions, and recommends which models will actually run well on your machine. It ships with both an interactive TUI (default) and a classic CLI mode, supports multi-GPU setups, MoE architectures, and local runtime providers (Ollama, llama.cpp, MLX).

**Problem it solves:** The LLM landscape has hundreds of models across dozens of quantization levels, and users waste hours downloading models that turn out too large for their hardware or too slow to be useful. LLMFit eliminates this trial-and-error by computing fit scores against actual hardware specs before any download occurs.

**Why another one?** LLMFit stands alone in its category — no other tool provides hardware-aware model recommendations with a single command. The multi-dimensional scoring (quality, speed, fit, context) is more nuanced than simple RAM-based filtering. The Rust implementation and Homebrew/Scoop distribution make it install-and-run without Python dependency management. Its sister project sympozium for Kubernetes agent management suggests a coherent toolchain vision.

---

## 18. [OpenSandbox](https://github.com/alibaba/OpenSandbox)
> A general-purpose sandbox platform for AI applications with multi-language SDKs and unified APIs.

**Language:** Python  |  **Stars:** 7,180  |  **Forks:** 526  |  **Score:** 3,612  |  **Created:** 2025-12-17

**Background:** Alibaba's sandbox platform for AI workloads, providing multi-language SDKs and a formal sandbox protocol for lifecycle management and code execution. Supports Docker and Kubernetes runtimes for coding agents, GUI agents, agent evaluation, AI code execution, and RL training scenarios.

**Problem it solves:** Every AI agent that executes code needs sandboxing, but most teams build ad-hoc solutions. OpenSandbox provides a standardized, production-tested platform so agent developers can focus on agent logic rather than container orchestration and security isolation.

**Why another one?** Score dropped slightly from yesterday (7,188 to 3,612) as the initial spike normalizes. OpenSandbox continues to trend because the demand for agent sandboxing is growing with the agent ecosystem. Alibaba's enterprise backing and the formal sandbox protocol differentiate it from simpler Docker wrapper approaches.

---

## 19. [MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2)
> An application that automates the process of making money online.

**Language:** Python  |  **Stars:** 14,944  |  **Forks:** 1,502  |  **Score:** 3,124  |  **Created:** 2024-02-12

**Background:** MoneyPrinter V2 by FujiwaraChoki is a Python application that automates online money-making workflows — Twitter bots with scheduled posts, YouTube Shorts automation, Amazon affiliate marketing with Twitter distribution, and local business outreach via cold email. It is a complete rewrite of the original MoneyPrinter with a modular architecture and a scheduler system for CRON-based automation.

**Problem it solves:** Content creation for social media, affiliate marketing, and business outreach involves repetitive manual steps — generating posts, scheduling them, finding target audiences, and composing outreach messages. MoneyPrinterV2 automates these pipelines end-to-end using AI for content generation and platform APIs for distribution.

**Why another one?** MoneyPrinterV2 trends periodically when AI automation communities share it. The v2 rewrite addressed the original's limitations with a modular architecture that separates content generation from distribution. The project has spawned community forks in other languages (notably MoneyPrinterTurbo for Chinese users), indicating demand for localized versions.

---

## 20. [Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI)
> A pixel-art AI office dashboard that visualizes AI assistant work status in real time.

**Language:** HTML  |  **Stars:** 3,785  |  **Forks:** 421  |  **Score:** 3,118  |  **Created:** 2026-02-26

**Background:** Star Office UI visualizes AI agent status through pixel-art characters that move between office areas based on agent state — idle, writing, researching, executing, syncing, or error. Co-created by Ring Hyacinth and Simon Lee, it integrates with OpenClaw for automatic state updates and supports standalone deployment via API. Trilingual (Chinese, English, Japanese).

**Problem it solves:** AI agents work invisibly, leaving users unsure whether their agent is active, stuck, or finished. Star Office UI provides ambient, at-a-glance visibility into agent status without requiring users to read logs or watch terminal output.

**Why another one?** Score increased from 2,057 to 3,118, reflecting continued discovery by the OpenClaw community. The pixel-art aesthetic makes monitoring feel approachable rather than operational, and the multi-agent "office" concept — inviting other agents into your workspace — anticipates the multi-agent workflows that collaborative frameworks like CoPaw are enabling.

---

## 21. [superset](https://github.com/superset-sh/superset)
> The Terminal for Coding Agents — run multiple agents simultaneously with worktree isolation.

**Language:** TypeScript  |  **Stars:** 6,327  |  **Forks:** 403  |  **Score:** 2,989  |  **Created:** 2025-10-21

**Background:** Superset is a macOS terminal application for running multiple coding agents in parallel with automatic git worktree isolation. Each agent works on its own branch and directory, a built-in diff viewer lets users review changes, and notifications alert when agents need attention or complete their tasks.

**Problem it solves:** Running multiple agents on the same codebase causes merge conflicts. Superset automates the worktree-per-agent pattern, providing clean isolation and a single pane of glass for monitoring all active agents. The built-in diff viewer eliminates the need to switch to a separate tool for code review.

**Why another one?** Score increased from 2,429 to 2,989. As agent-assisted development scales from "one agent at a time" to "multiple agents in parallel," the need for orchestration and isolation tooling grows proportionally. Superset is purpose-built for this specific workflow, which tmux and standard terminal emulators cannot replicate.

---

## 22. [markitdown](https://github.com/microsoft/markitdown)
> A lightweight Python utility for converting various files to Markdown for use with LLMs and related text analysis pipelines.

**Language:** Python  |  **Stars:** 90,419  |  **Forks:** 5,324  |  **Score:** 2,926  |  **Created:** 2024-11-13

**Background:** Microsoft's document-to-Markdown converter from the AutoGen team. Handles PDFs, Word, Excel, PowerPoint, images, audio, HTML, and more, preserving document structure (headings, tables, lists) in LLM-optimized Markdown output. Now includes an MCP server for Claude Desktop integration.

**Problem it solves:** LLMs process text, but enterprise data lives in binary document formats. MarkItDown converts these formats into Markdown that preserves semantic structure, making document content accessible to any text-based AI pipeline without losing meaning.

**Why another one?** At 90K stars, MarkItDown is the de facto standard for document-to-Markdown conversion in the LLM ecosystem. It trends consistently because every new LLM user eventually needs to feed documents into their pipeline. The MCP server integration extends its reach beyond scripting into interactive agent workflows.

---

## 23. [MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles)
> Source code of Minecraft Legacy Console Edition v1.6.0560.0 (TU19) with fixes and improvements.

**Language:** C++  |  **Stars:** 4,286  |  **Forks:** 808  |  **Score:** 2,866  |  **Created:** 2026-03-01

**Background:** MinecraftConsoles contains the source code of Minecraft Legacy Console Edition TU19 (v1.6.0560.0) with community-applied fixes. The project adds keyboard/mouse input, fullscreen support, LAN multiplayer with automatic discovery, high-resolution timers for smoother gameplay, and native screen resolution support. It currently supports Windows, with unofficial Wine/CrossOver compatibility on macOS and Linux.

**Problem it solves:** Minecraft Legacy Console Edition was discontinued by Microsoft, leaving a community of players with no way to play or modify their preferred version. This project preserves and improves the console edition's codebase, adding features (LAN multiplayer, keyboard input) that the original lacked.

**Why another one?** Created just two days ago (March 1, 2026), MinecraftConsoles entered the chart with strong momentum. Nostalgia for discontinued game versions drives periodic preservation projects, and Minecraft's massive player base means any playable console edition rebuild attracts immediate attention. The LAN multiplayer feature addresses the most-requested capability for local play.

---

## 24. [fara](https://github.com/microsoft/fara)
> Fara-7B: An Efficient Agentic Model for Computer Use — Microsoft's first agentic small language model.

**Language:** Python  |  **Stars:** 4,383  |  **Forks:** 400  |  **Score:** 2,850  |  **Created:** 2025-10-29

**Background:** Fara-7B is Microsoft's first agentic small language model (SLM) designed specifically for computer use. With only 7 billion parameters, it achieves state-of-the-art performance within its size class for Computer Use Agent (CUA) tasks — navigating websites, filling forms, clicking buttons — and is competitive with much larger models. It can be served locally via vLLM and used through a CLI or through Magentic-UI.

**Problem it solves:** Computer use agents (CUAs) that can navigate websites and interact with GUIs typically require large, expensive models (70B+ parameters) or cloud API access. Fara-7B delivers competitive CUA performance at 7B parameters, making computer use capabilities accessible on consumer hardware without cloud dependency.

**Why another one?** Fara-7B occupies a unique niche as an agentic SLM — most computer use research focuses on large models. The Microsoft backing and arxiv paper (2511.19663) provide scientific credibility, and the inclusion of WebTailBench (a new evaluation dataset) gives the community a standardized way to measure CUA performance. The vLLM serving and Magentic-UI integration make it practically usable, not just academically interesting.

---

## 25. [hello-agents](https://github.com/datawhalechina/hello-agents)
> A comprehensive tutorial on building AI agents from scratch (in Chinese).

**Language:** Python  |  **Stars:** 26,281  |  **Forks:** 2,949  |  **Score:** 2,511  |  **Created:** 2025-09-07

**Background:** Hello-Agents is a systematic tutorial by Datawhale China for building AI agents from scratch. The course distinguishes between workflow-driven agents (Dify, Coze, n8n) and AI-native agents, focusing on the latter — true AI-driven agents rather than LLM-as-backend software. It covers core architectures, classic paradigms, and hands-on multi-agent system construction. Available online and as a local gitbook.

**Problem it solves:** The Chinese-language AI community lacks systematic, practice-oriented tutorials for building AI-native agents (as opposed to workflow-automation tools that use LLMs). Hello-Agents fills this gap with theory-to-practice coverage that helps learners transition from LLM "users" to agent system "builders."

**Why another one?** Hello-Agents addresses a language barrier — most agent development resources are English-first. Its distinction between "software engineering agents" (workflow-driven) and "AI-native agents" (AI-driven) is a useful framework that English-language tutorials often blur. The 26K stars and Datawhale community backing make it the authoritative Chinese-language agent development resource.

---

> **Day's theme:** RuView's viral explosion dominates the chart while the AI agent ecosystem continues maturing across education (tutorials in Chinese, English, and multi-language), tooling (hardware-aware model selection, VS Code themes, document conversion), and infrastructure (sandbox platforms, collaboration frameworks, agent operating systems).
