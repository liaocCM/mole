# Trendshift Report — 2026-02-22
**Total:** 25 repositories

---

## 1. [nanoclaw](https://github.com/qwibitai/nanoclaw)
> A lightweight alternative to Clawdbot / OpenClaw that runs in containers for security. Connects to WhatsApp, has memory, scheduled jobs, and runs directly on Anthropic's Agents SDK

**Language:** TypeScript  |  **Stars:** 10,547  |  **Forks:** 1,504  |  **Score:** 6,356  |  **Created:** 2026-01-31

**Background:** Nanoclaw is a containerized personal AI assistant built on Anthropic's Agents SDK, positioned as a lightweight alternative to both Clawdbot and OpenClaw. It connects natively to WhatsApp as its primary messaging interface and ships with persistent memory and scheduled job support out of the box. The project launched at the end of January 2026 and has rapidly accumulated over 10,000 stars.

**Problem it solves:** OpenClaw is a full-featured assistant platform with a massive codebase and complex deployment requirements. Nanoclaw strips the concept down to a containerized runtime that is simpler to deploy and secure, while retaining the core features most users need: messaging integration, persistent memory, and task scheduling. Running inside containers provides process-level isolation without requiring a full VM or orchestration layer.

**Why another one?** The key differentiator is the direct integration with Anthropic's Agents SDK rather than building a custom agent runtime, which means Nanoclaw benefits from upstream improvements to the SDK without reimplementation. The container-first architecture also makes it easier to deploy on any Docker-compatible host, from a Raspberry Pi to a cloud VM, without the dependency sprawl of larger assistant platforms.

---

## 2. [pentagi](https://github.com/vxcontrol/pentagi)
> Fully autonomous AI Agents system capable of performing complex penetration testing tasks

**Language:** Go  |  **Stars:** 4,228  |  **Forks:** 588  |  **Score:** 6,192  |  **Created:** 2025-01-06

**Background:** PentAGI is a self-hosted autonomous agent system for penetration testing, built in Go by vxcontrol. It bundles over 20 professional security tools — including nmap, Metasploit, and sqlmap — inside isolated Docker containers and uses a multi-agent architecture where a lead agent delegates tasks to specialized sub-agents for research, development, and infrastructure. A Neo4j-backed knowledge graph provides long-term memory across testing sessions.

**Problem it solves:** Security testing requires orchestrating dozens of tools in sequence, interpreting intermediate outputs, and adapting attack paths based on findings — a process that demands deep expertise and significant time. PentAGI automates this orchestration layer, allowing the system to autonomously chain tools together and produce detailed vulnerability reports with exploitation guidance.

**Why another one?** PentAGI is fully self-hosted and open-source, which distinguishes it from commercial AI-assisted security platforms. Its architecture is notably complete: a full REST and GraphQL API, Grafana/Prometheus monitoring integration, and a bundled scraper container for browser-based OSINT. The long-term semantic memory via knowledge graphs also sets it apart from simpler tool-chaining approaches.

---

## 3. [prompts.chat](https://github.com/f/prompts.chat)
> a.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**Language:** HTML  |  **Stars:** 146,140  |  **Forks:** 19,286  |  **Score:** 3,674  |  **Created:** 2022-12-05

**Background:** Originally launched as "Awesome ChatGPT Prompts" by Fatih Kadir Akin in December 2022, prompts.chat has grown into a full community platform for sharing, discovering, and collecting AI prompts. It now includes a web frontend, a Hugging Face dataset mirror, a self-hosting option for organizational privacy, and an interactive prompt engineering book. The repository has over 40 academic citations from institutions including Harvard and Columbia.

**Problem it solves:** Users of AI chat models face a cold-start problem: crafting effective system prompts and persona-based instructions requires trial and error. Prompts.chat provides a structured, community-maintained library of tested prompts that serve as starting points, reducing the experimentation needed to get useful outputs from general-purpose models.

**Why another one?** This repository trends recurrently because it remains the canonical reference for prompt collections. Its evolution from a static markdown file into a full web platform with community submissions, Hugging Face dataset mirroring, and self-hosting capability has kept it relevant as a living resource. The addition of organizational self-hosting addresses enterprise privacy concerns that the public site cannot.

---

## 4. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 56,468  |  **Forks:** 4,282  |  **Score:** 3,303  |  **Created:** 2025-10-09

**Background:** Superpowers is a composable skills framework and structured software development methodology created by Jesse Vincent (obra). It installs into coding agents such as Claude Code, Cursor, Codex, and OpenCode via their plugin systems, enforcing a multi-stage workflow: brainstorm and refine a spec, produce a detailed implementation plan, then execute through subagent-driven development with two-stage code review. The project has accumulated over 56,000 stars since October 2025.

**Problem it solves:** Coding agents left to default settings tend to skip planning, ignore test-driven development, and drift from the original intent mid-session. Superpowers installs guard rails — mandatory spec approval, red-green-refactor TDD enforcement, and plan checkpoints — so an agent can work autonomously for extended periods without derailing from what was agreed upon.

**Why another one?** Rather than being a new coding agent, Superpowers is a methodology layer that works across multiple agents via their plugin systems. The portability (same skills install in Claude Code, Cursor, Codex, and OpenCode) and the emphasis on subagent delegation rather than a single long-running context are the primary differentiators. It keeps trending as new users discover its cross-agent compatibility.

---

## 5. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Language:** Shell  |  **Stars:** 68,067  |  **Forks:** 5,340  |  **Score:** 3,116  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official terminal-based agentic coding tool, launched in February 2025. It operates directly in the developer's terminal, understanding the full codebase context and executing tasks through natural language commands. The tool handles routine development tasks, explains complex code, manages git workflows, and supports an extensible skills and hooks system for customization.

**Problem it solves:** Developers spend significant time on repetitive coding tasks, navigating unfamiliar codebases, and managing version control workflows. Claude Code automates these tasks directly in the terminal where developers already work, eliminating the context-switching overhead of moving between an IDE, a browser-based AI chat, and the command line.

**Why another one?** Claude Code keeps trending because it is Anthropic's first-party coding agent and has become a reference implementation for terminal-based agentic development. Its first anniversary (February 22, 2025) coincides with this report date, likely contributing to renewed attention. The growing ecosystem of community skills, hooks, and configurations continues to drive adoption and visibility.

---

## 6. [voicebox](https://github.com/jamiepine/voicebox)
> The open-source voice synthesis studio powered by Qwen3-TTS.

**Language:** TypeScript  |  **Stars:** 9,955  |  **Forks:** 1,040  |  **Score:** 2,801  |  **Created:** 2026-01-25

**Background:** Voicebox is a local-first voice cloning and speech synthesis desktop application created by Jamie Pine, built with Tauri for native performance rather than Electron. It features a DAW-like multi-track timeline editor for composing multi-voice projects and runs entirely on the user's machine with no cloud dependency. On Apple Silicon it uses an MLX backend with Metal acceleration for significantly faster inference than CPU-only alternatives.

**Problem it solves:** Commercial voice synthesis services like ElevenLabs charge subscription fees, store voice data on remote servers, and impose generation limits. Voicebox removes all three constraints: models and voice profiles stay local, there is no per-character billing, and there is no rate limiting. It also ships as a self-contained binary requiring no Python installation.

**Why another one?** The differentiator is the studio-grade editing interface layered on top of the open-source Qwen3-TTS model. Most open-source TTS projects expose only a CLI or a Gradio demo. Voicebox wraps inference in a professional multi-track editor with audio trimming and conversation mixing, targeting content creators rather than ML researchers.

---

## 7. [airllm](https://github.com/lyogavin/airllm)
> AirLLM 70B inference with single 4GB GPU

**Language:** Jupyter Notebook  |  **Stars:** 11,717  |  **Forks:** 1,066  |  **Score:** 2,626  |  **Created:** 2023-06-12

**Background:** AirLLM is a library that enables running 70-billion-parameter language models on a single GPU with as little as 4GB of VRAM. Created by Gavin Li and first released in June 2023, it uses layer-by-layer inference with aggressive memory management to fit models that would normally require multiple high-end GPUs. The project has steadily grown to nearly 12,000 stars.

**Problem it solves:** Running large language models locally typically requires expensive multi-GPU setups or cloud instances with 80+ GB of VRAM. AirLLM makes 70B-class models accessible to developers and researchers with consumer-grade hardware by trading inference speed for dramatically reduced memory requirements.

**Why another one?** While quantization libraries like GPTQ and AWQ reduce model size, they still require fitting the entire quantized model in memory. AirLLM takes a fundamentally different approach by streaming layers through GPU memory, which means the VRAM requirement is bounded by the largest single layer rather than the full model. This architectural choice enables a class of hardware that quantization alone cannot serve.

---

## 8. [cmux](https://github.com/manaflow-ai/cmux)
> Ghostty-based macOS terminal with vertical tabs and notifications for AI coding agents

**Language:** Swift  |  **Stars:** 762  |  **Forks:** 13  |  **Score:** 2,369  |  **Created:** 2026-01-28

**Background:** Cmux is a native macOS terminal application built on Ghostty's terminal emulation library, developed by Manaflow AI. It is designed specifically for AI coding agent workflows, featuring vertical tabs for managing multiple agent sessions, built-in notifications when agents complete tasks, and a streamlined interface optimized for watching and managing concurrent agent runs.

**Problem it solves:** Developers running multiple AI coding agents simultaneously (such as Claude Code across several projects) struggle with terminal management — standard terminals lack notifications for long-running agent tasks and make it difficult to monitor multiple sessions at a glance. Cmux provides purpose-built UI for this workflow with vertical tabs and completion notifications.

**Why another one?** Existing terminals like iTerm2, Warp, and Ghostty itself are general-purpose tools not optimized for the specific pattern of running and monitoring AI agents. Cmux narrows its scope to this single use case, providing agent-aware notifications and a vertical tab layout designed for concurrent session monitoring rather than traditional shell workflows.

---

## 9. [Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)
> Official code repo for the O'Reilly Book - "Hands-On Large Language Models"

**Language:** Jupyter Notebook  |  **Stars:** 22,267  |  **Forks:** 5,198  |  **Score:** 2,223  |  **Created:** 2024-06-28

**Background:** This repository contains all code notebooks for the O'Reilly book "Hands-On Large Language Models" by Jay Alammar and Maarten Grootendorst, often called "The Illustrated LLM Book" for its nearly 300 custom figures. Each chapter has a corresponding Google Colab-compatible Jupyter notebook covering topics from tokenization and embeddings through fine-tuning, retrieval, and agents. Alammar is known for his illustrated transformer explanations, and Grootendorst is the author of BERTopic.

**Problem it solves:** Most LLM learning resources are either purely theoretical (academic papers) or purely practical (vendor tutorials assuming a specific platform). This book and its code bridge that gap with visual explanations of how models work internally, paired with runnable notebooks that do not require a local GPU.

**Why another one?** The book continues to trend because it remains one of the most accessible entry points to LLM internals for practitioners without a deep ML background. The combination of Alammar's illustration-heavy style with Grootendorst's applied NLP expertise covers a different audience than fast.ai or LangChain tutorials, focusing on understanding model internals rather than just using APIs.

---

## 10. [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
> GitNexus: The Zero-Server Code Intelligence Engine - GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph with a built in Graph RAG Agent. Perfect for code exploration

**Language:** TypeScript  |  **Stars:** 885  |  **Forks:** 82  |  **Score:** 2,174  |  **Created:** 2025-08-02

**Background:** GitNexus is a client-side code intelligence tool that generates interactive knowledge graphs from GitHub repositories or ZIP files, running entirely in the browser with no server component. It includes a built-in Graph RAG Agent that allows users to query the generated knowledge graph conversationally. The project was created by Abhigyan Patwari and launched in August 2025.

**Problem it solves:** Understanding an unfamiliar codebase typically requires cloning, setting up a local environment, and manually tracing dependencies and relationships between modules. GitNexus eliminates the setup step entirely — users drop in a repo URL or ZIP file in their browser and immediately get a visual knowledge graph of the codebase's structure with an AI agent for exploration.

**Why another one?** The zero-server, fully client-side architecture is the primary differentiator against code intelligence tools like Sourcegraph or CodeSee, which require server-side indexing. Running entirely in the browser means no data leaves the user's machine, addressing privacy concerns for proprietary codebases. The integrated Graph RAG Agent adds conversational exploration on top of the visual graph.

---

## 11. [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
> FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**Language:** N/A  |  **Stars:** 115,359  |  **Forks:** 29,733  |  **Score:** 2,172  |  **Created:** 2025-03-05

**Background:** This repository is a comprehensive archive of extracted system prompts, internal tool definitions, and model configurations from over 30 major AI coding and assistant tools. It covers products from Anthropic, Cursor, Devin AI, Replit, Windsurf, Perplexity, and many others. The repository has amassed over 115,000 stars since March 2025, making it one of the most-starred prompt extraction collections on GitHub.

**Problem it solves:** AI tool system prompts are proprietary and hidden from users, making it difficult to understand how these tools work internally, what constraints they operate under, or how to build similar capabilities. This repository surfaces those prompts for study, comparison, and educational purposes, enabling developers to learn from production-grade prompt engineering.

**Why another one?** The repository keeps trending because new AI coding tools launch frequently and existing ones update their system prompts regularly, creating ongoing demand for documentation of changes. With coverage of over 30 tools and nearly 30,000 forks, it has become the de facto reference for comparing how different AI products are prompted and configured.

---

## 12. [evershop](https://github.com/evershopcommerce/evershop)
> Typescript E-commerce Platform

**Language:** TypeScript  |  **Stars:** 9,479  |  **Forks:** 2,145  |  **Score:** 1,964  |  **Created:** 2021-05-06

**Background:** EverShop is an open-source e-commerce platform built entirely in TypeScript, launched in May 2021. It provides a complete online store solution with product management, order processing, and a modular extension system. The platform uses a GraphQL API and is designed for both developers who want to customize and merchants who need a production-ready storefront.

**Problem it solves:** Most open-source e-commerce platforms (WooCommerce, Magento, PrestaShop) are built on PHP, which creates friction for JavaScript/TypeScript-focused development teams. EverShop provides a full e-commerce stack in TypeScript, eliminating the need to context-switch between languages and enabling teams to share code and tooling across their frontend and backend.

**Why another one?** The TypeScript-native approach is the primary differentiator against established PHP-based platforms, while the modular extension architecture differentiates it from newer Node.js alternatives like Medusa or Saleor that may require more custom development. EverShop targets the middle ground of being opinionated enough to deploy quickly while remaining extensible through its module system.

---

## 13. [awesome](https://github.com/sindresorhus/awesome)
> Awesome lists about all kinds of interesting topics

**Language:** N/A  |  **Stars:** 439,784  |  **Forks:** 33,277  |  **Score:** 1,867  |  **Created:** 2014-07-11

**Background:** Sindre Sorhus's awesome repository is the root meta-list that spawned the entire "awesome list" convention on GitHub, created in July 2014. It serves as a curated index of other curated lists spanning programming languages, frameworks, platforms, developer tools, theory, media, and more. With nearly 440,000 stars, it is one of the most-starred repositories on all of GitHub.

**Problem it solves:** Before the awesome list pattern existed, there was no consistent convention for community-maintained topic indexes on GitHub. This repository established both the format and the quality standard that thousands of downstream awesome lists now follow, making it the canonical entry point for discovering curated resources on any technical topic.

**Why another one?** This repository trends periodically because it is the authoritative meta-index — every new awesome list that gains traction links back to it, and every developer who discovers the pattern for the first time stars the original. Its 11-year maintenance history and unmatched star count make it an infrastructure piece of GitHub's knowledge graph rather than a project competing with alternatives.

---

## 14. [FineTune](https://github.com/ronitsingh10/FineTune)
> FineTune, a macOS menu bar app for per-app volume control, multi-device output, audio routing, and 10-band EQ. Free and open-source alternative to SoundSource.

**Language:** Swift  |  **Stars:** 2,785  |  **Forks:** 93  |  **Score:** 1,863  |  **Created:** 2026-01-18

**Background:** FineTune is a free, open-source macOS menu bar application written in Swift that provides per-application volume control, multi-device audio output, audio routing, and a 10-band equalizer. It positions itself as a free alternative to Rogue Amoeba's SoundSource, which is a paid commercial application. The project launched in January 2026 and has quickly gained nearly 2,800 stars.

**Problem it solves:** macOS provides only system-wide volume control by default, with no built-in way to set different volume levels for individual applications or route specific apps to different audio output devices. SoundSource solves this but costs money. FineTune provides the same per-app audio control capabilities at no cost.

**Why another one?** The primary appeal is being a free and open-source alternative to a well-known paid tool. SoundSource costs $39 and is closed-source; FineTune provides comparable functionality — per-app volume, multi-device output, audio routing, and equalization — without a license fee. The menu bar integration follows the same UX pattern macOS users expect from audio utilities.

---

## 15. [FossFLOW](https://github.com/stan-smith/FossFLOW)
> Make beautiful isometric infrastructure diagrams

**Language:** TypeScript  |  **Stars:** 17,565  |  **Forks:** 1,147  |  **Score:** 1,726  |  **Created:** 2025-06-30

**Background:** FossFLOW is an open-source tool for creating isometric infrastructure diagrams, built in TypeScript. It provides a visual interface for generating polished, three-dimensional architecture diagrams commonly used in cloud infrastructure documentation, DevOps presentations, and system design discussions. The project has grown to over 17,500 stars since its June 2025 launch.

**Problem it solves:** Creating professional isometric infrastructure diagrams typically requires either expensive design software (Figma, Illustrator) with manual drawing skills or proprietary diagramming tools with limited export options. FossFLOW automates the isometric rendering, letting users focus on describing their infrastructure rather than drawing it.

**Why another one?** While tools like draw.io and Excalidraw support general diagramming, they do not specialize in isometric infrastructure views. FossFLOW's narrow focus on isometric rendering produces more visually polished output for this specific use case than general-purpose diagramming tools, and being open-source differentiates it from commercial alternatives like Cloudcraft.

---

## 16. [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
> Master programming by recreating your favorite technologies from scratch.

**Language:** Markdown  |  **Stars:** 467,978  |  **Forks:** 43,866  |  **Score:** 1,675  |  **Created:** 2018-05-09

**Background:** Build Your Own X is a curated collection of tutorials for recreating popular technologies from scratch — databases, compilers, operating systems, web servers, game engines, and more. Maintained by CodeCrafters since May 2018, it has become one of the most-starred repositories on GitHub with nearly 468,000 stars. Each entry links to a step-by-step tutorial that walks through building a real implementation.

**Problem it solves:** Understanding how complex systems work internally is difficult from documentation or source code alone. These tutorials provide structured, hands-on paths to build working replicas of technologies like Redis, Git, Docker, and SQLite, giving developers deep understanding through implementation rather than theory.

**Why another one?** The repository keeps trending because it is the definitive collection for this learning approach, and new tutorials are continuously added. Each wave of developers discovering the "build it yourself" learning method finds this repository as the canonical starting point. Its nearly 468,000 stars reflect cumulative discovery over eight years rather than a single viral moment.

---

## 17. [awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
> A community collection of OpenClaw use cases for making life easier.

**Language:** N/A  |  **Stars:** 4,893  |  **Forks:** 353  |  **Score:** 1,656  |  **Created:** 2026-02-08

**Background:** Awesome OpenClaw Usecases is a community-curated collection of practical use cases for the OpenClaw personal AI assistant, assembled by Hesam Sheikh and launched in early February 2026. It documents real-world applications people have built using OpenClaw's skills and multi-channel architecture, organized by category. The repository has rapidly accumulated nearly 5,000 stars in just two weeks.

**Problem it solves:** OpenClaw has over 5,700 skills in its ClawHub registry, but discovering which combinations of skills solve specific real-world problems requires experimentation. This collection provides documented, tested use cases that show how to combine OpenClaw capabilities for practical tasks, reducing the trial-and-error discovery process.

**Why another one?** While awesome-openclaw-skills catalogs individual skills with security vetting, this repository focuses on complete use-case recipes that combine multiple skills into workflows. The distinction is between a tool catalog (skills) and a cookbook (use cases), serving users who know what they want to accomplish but not which tools to combine.

---

## 18. [openclaw](https://github.com/openclaw/openclaw)
> Your own personal AI assistant. Any OS. Any Platform. The lobster way.

**Language:** TypeScript  |  **Stars:** 215,287  |  **Forks:** 40,386  |  **Score:** 1,596  |  **Created:** 2025-11-24

**Background:** OpenClaw is a personal AI assistant that runs as a locally-hosted gateway, routing conversations through messaging platforms users already have: WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Microsoft Teams, Matrix, and others. It supports voice input and output on macOS, iOS, and Android, and can render an interactive Canvas. With over 215,000 stars since November 2025, it is the most-starred personal assistant project on GitHub.

**Problem it solves:** Personal AI assistants typically require a dedicated app or web interface, creating friction for users who want to interact through channels already open on their phone or desktop. OpenClaw turns existing messaging clients into AI frontends so the assistant is reachable through whatever app the user already has, with no additional app installation required.

**Why another one?** OpenClaw keeps trending because of its massive skill ecosystem (over 5,700 community skills in ClawHub), its multi-channel architecture, and its local-first approach. The ecosystem effect is self-reinforcing: more skills attract more users, who build more skills. Multiple related repositories on this list (nanoclaw, awesome-openclaw-skills, awesome-openclaw-usecases) reflect the breadth of its community.

---

## 19. [SparkyFitness](https://github.com/CodeWithCJ/SparkyFitness)
> SparkyFitness: Built for Families. Powered by AI. Track food, fitness, water, and health — together.

**Language:** TypeScript  |  **Stars:** 2,447  |  **Forks:** 114  |  **Score:** 1,534  |  **Created:** 2025-06-21

**Background:** SparkyFitness is an AI-powered family health tracking application built in TypeScript. It provides collaborative tracking for food intake, fitness activities, water consumption, and general health metrics, designed for family use rather than individual users. The application uses AI to assist with meal logging, nutritional analysis, and fitness recommendations.

**Problem it solves:** Most health and fitness tracking apps are designed for individual use and lack shared family features. Families trying to improve their health together must each use separate apps with no shared visibility. SparkyFitness provides a unified platform where family members can track and view each other's health data collaboratively.

**Why another one?** The family-first design is the primary differentiator against established apps like MyFitnessPal, Cronometer, or Apple Health, which are all individual-centric. The AI-powered food logging and nutritional analysis lower the barrier for less tech-savvy family members, and the open-source nature allows self-hosting for families who want full control over their health data.

---

## 20. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> The awesome collection of OpenClaw Skills. Formerly known as Moltbot, originally Clawdbot.

**Language:** N/A  |  **Stars:** 17,555  |  **Forks:** 1,799  |  **Score:** 1,467  |  **Created:** 2026-01-25

**Background:** Awesome OpenClaw Skills is a curated index of over 3,000 community-built skills for the OpenClaw assistant, maintained by VoltAgent. It draws from ClawHub, OpenClaw's public registry of over 5,700 skills, but filters out spam, crypto content, duplicates, and 396 skills identified as malicious by security researchers. The project was formerly known as Moltbot and originally as Clawdbot.

**Problem it solves:** The ClawHub registry is large and unfiltered, making it difficult to find trustworthy, useful skills without wading through spam, duplicates, and potentially malicious entries. This curated list applies documented quality and security filters, providing reasonable confidence that listed skills are functional and safe.

**Why another one?** The OpenClaw skill ecosystem is the primary extensibility mechanism for the most-starred personal assistant on GitHub, and no official curated list existed. The security angle — explicitly cataloguing 396 malicious skills and providing guidance on VirusTotal partnership checks — adds a layer of value that the raw ClawHub registry does not provide. The name changes reflect the rapid evolution of the broader ecosystem.

---

## 21. [zvec](https://github.com/alibaba/zvec)
> A lightweight, lightning-fast, in-process vector database

**Language:** C++  |  **Stars:** 5,951  |  **Forks:** 330  |  **Score:** 1,425  |  **Created:** 2025-12-05

**Background:** Zvec is an in-process vector database written in C++ by Alibaba, designed for scenarios where a full client-server vector database is unnecessary overhead. It runs as a library embedded directly in the application process rather than as a separate service, targeting extremely low-latency vector similarity search. The project launched in December 2025 and has accumulated nearly 6,000 stars.

**Problem it solves:** Vector databases like Milvus, Qdrant, and Weaviate run as external services requiring network communication, deployment management, and operational overhead. For applications that need fast vector search but do not need distributed multi-tenant infrastructure — such as desktop apps, CLI tools, or single-server deployments — zvec provides in-process vector search with no network latency.

**Why another one?** The in-process architecture is the key differentiator. Where Milvus (also from Alibaba) targets distributed cloud deployments, zvec targets the opposite end: embedded use cases where the vector index lives in the same process as the application. The C++ implementation and Alibaba's backing signal production-quality performance tuning for high-throughput scenarios.

---

## 22. [skills](https://github.com/huggingface/skills)
> (no description provided)

**Language:** Python  |  **Stars:** 1,872  |  **Forks:** 153  |  **Score:** 1,417  |  **Created:** 2025-11-24

**Background:** Hugging Face Skills is an official repository from Hugging Face providing a collection of reusable AI agent skills in Python. Launched alongside the broader agent skills ecosystem in November 2025, it provides building blocks for constructing AI agent workflows using Hugging Face's model and dataset ecosystem. The repository has grown to nearly 1,900 stars.

**Problem it solves:** Building AI agent capabilities from scratch requires significant boilerplate — model loading, inference pipelines, tool definitions, and error handling. This repository provides pre-built, tested skill implementations that can be composed into agent workflows, reducing the time from concept to working agent.

**Why another one?** As an official Hugging Face project, these skills are designed to integrate natively with the Hugging Face ecosystem — models, datasets, Spaces, and inference endpoints. This tight integration differentiates them from framework-agnostic skill collections that require additional glue code to connect to Hugging Face resources.

---

## 23. [llmfit](https://github.com/AlexsJones/llmfit)
> 157 models. 30 providers. One command to find what runs on your hardware.

**Language:** Rust  |  **Stars:** 1,337  |  **Forks:** 79  |  **Score:** 1,293  |  **Created:** 2026-02-15

**Background:** LLMFit is a Rust-based CLI tool that scans the user's hardware — GPU VRAM, system RAM, and disk space — and reports which LLM models from 30 providers can actually run locally. It covers 157 models and produces a compatibility report with a single command. The project launched in mid-February 2026 and has quickly gained over 1,300 stars.

**Problem it solves:** Developers interested in running LLMs locally must manually check each model's requirements against their hardware specs, navigating inconsistent documentation across providers for VRAM requirements, quantization options, and minimum RAM. LLMFit automates this discovery, instantly telling users which of 157 models will fit on their specific hardware.

**Why another one?** No existing tool provides a unified hardware compatibility check across this many models and providers. Ollama and LM Studio help with running local models but do not proactively tell users what their hardware can support before downloading. LLMFit fills this specific gap in the local LLM workflow — hardware discovery before model selection.

---

## 24. [agents](https://github.com/cloudflare/agents)
> Build and deploy AI Agents on Cloudflare

**Language:** TypeScript  |  **Stars:** 3,278  |  **Forks:** 381  |  **Score:** 1,292  |  **Created:** 2025-01-29

**Background:** Cloudflare Agents is an official TypeScript framework from Cloudflare for building and deploying AI agents on Cloudflare's edge network. It leverages Durable Objects for stateful agent sessions, Workers for serverless execution, and integrates with Cloudflare's AI Gateway for model routing. The framework launched in January 2025 and provides templates and examples for common agent patterns.

**Problem it solves:** Deploying AI agents typically requires managing server infrastructure, handling WebSocket connections for real-time interaction, and implementing state persistence — all of which add complexity and cost. Cloudflare Agents abstracts these concerns into the Cloudflare platform, providing globally distributed, stateful agent execution with minimal infrastructure management.

**Why another one?** The edge deployment model is the differentiator: agents run on Cloudflare's global network rather than in a single region, reducing latency for users worldwide. The integration with Durable Objects provides built-in state persistence without an external database, and the Workers runtime offers automatic scaling. For teams already on Cloudflare, it eliminates the need to set up separate agent infrastructure.

---

## 25. [n8n-workflows](https://github.com/Zie619/n8n-workflows)
> all of the workflows of n8n i could find (also from the site itself)

**Language:** Python  |  **Stars:** 51,740  |  **Forks:** 6,551  |  **Score:** 1,277  |  **Created:** 2025-05-14

**Background:** This repository is a comprehensive collection of n8n workflow templates assembled by Zie619, aggregating workflows from the official n8n site and community sources. N8n is an open-source workflow automation platform similar to Zapier, and this repository serves as an unofficial but extensive library of pre-built automations. It has accumulated over 51,000 stars since May 2025.

**Problem it solves:** Building n8n workflows from scratch requires understanding the platform's node system and experimenting with connections between services. This collection provides ready-made workflow templates that users can import directly, covering common automation patterns and reducing the learning curve for new n8n users.

**Why another one?** While n8n has an official template library, this repository aggregates workflows from multiple community sources into a single searchable collection. The unofficial curation includes workflows the official library may not feature, and the GitHub-based format makes it easier to browse, fork, and adapt workflows than the official web-based template browser.

---

> **Day's theme:** The OpenClaw ecosystem dominates with four related entries (the platform itself, a lightweight alternative, a skills catalog, and a use-case cookbook), while the remaining repos reflect a maturing AI tooling landscape where infrastructure layers — hardware compatibility checkers, in-process vector databases, edge agent runtimes, and purpose-built terminals — are catching up to the agents they support.
