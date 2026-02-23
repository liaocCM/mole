# Trendshift Report — 2026-02-21
**Total:** 25 repositories

---

## 1. [pentagi](https://github.com/vxcontrol/pentagi)
> Fully autonomous AI Agents system capable of performing complex penetration testing tasks

**Language:** Go  |  **Stars:** 4,228  |  **Forks:** 588  |  **Score:** 7,012  |  **Created:** 2025-01-06

**Background:** PentAGI is a self-hosted autonomous agent system for penetration testing, built in Go by vxcontrol. It orchestrates over 20 professional security tools — including nmap, Metasploit, and sqlmap — inside isolated Docker containers using a multi-agent architecture where a lead agent delegates tasks to specialized sub-agents. The project launched in January 2025 and uses a Neo4j-backed knowledge graph for persistent memory across testing sessions.

**Problem it solves:** Penetration testing requires chaining dozens of tools in sequence, interpreting intermediate outputs, and adapting attack strategies based on findings — a process that demands deep security expertise and significant time. PentAGI automates this orchestration, allowing the system to autonomously plan and execute multi-step attack chains while producing detailed vulnerability reports.

**Why another one?** PentAGI is fully self-hosted and open-source, distinguishing it from commercial AI-assisted security platforms that require cloud access to sensitive network data. Its architecture is unusually complete for an open-source project, including a full REST and GraphQL API, Grafana/Prometheus monitoring, and a browser-based OSINT scraper. The knowledge graph memory also sets it apart from simpler tool-chaining approaches that lose context between sessions.

---

## 2. [voicebox](https://github.com/jamiepine/voicebox)
> The open-source voice synthesis studio powered by Qwen3-TTS.

**Language:** TypeScript  |  **Stars:** 9,955  |  **Forks:** 1,040  |  **Score:** 4,707  |  **Created:** 2026-01-25

**Background:** Voicebox is a local-first voice cloning and speech synthesis desktop application created by Jamie Pine, built with Tauri for native performance. It features a DAW-like multi-track timeline editor for composing multi-voice projects and runs entirely on the user's machine with no cloud dependency. On Apple Silicon it uses an MLX backend with Metal acceleration for significantly faster inference than CPU-only alternatives.

**Problem it solves:** Commercial voice synthesis services like ElevenLabs charge subscription fees, store voice data on remote servers, and impose generation limits. Voicebox removes all three constraints: models and voice profiles stay local, there is no per-character billing, and there is no rate limiting. It also ships as a self-contained binary requiring no Python installation.

**Why another one?** The differentiator is the studio-grade editing interface layered on top of the open-source Qwen3-TTS model. Most open-source TTS projects expose only a CLI or a Gradio demo, while Voicebox wraps inference in a professional multi-track editor with audio trimming and conversation mixing. This targets content creators rather than ML researchers.

---

## 3. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 56,468  |  **Forks:** 4,282  |  **Score:** 4,007  |  **Created:** 2025-10-09

**Background:** Superpowers is a composable skills framework and structured software development methodology created by Jesse Vincent (obra). It installs into coding agents such as Claude Code, Cursor, Codex, and OpenCode via their plugin systems, enforcing a multi-stage workflow: brainstorm and refine a spec, produce a detailed implementation plan, then execute through subagent-driven development with two-stage code review. The project has accumulated over 56,000 stars since October 2025.

**Problem it solves:** Coding agents left to default settings tend to skip planning, ignore test-driven development, and drift from the original intent mid-session. Superpowers installs guard rails — mandatory spec approval, red-green-refactor TDD enforcement, and plan checkpoints — so an agent can work autonomously for extended periods without derailing from what was agreed upon.

**Why another one?** Rather than being a new coding agent, Superpowers is a methodology layer that works across multiple agents via their plugin systems. The portability across Claude Code, Cursor, Codex, and OpenCode, combined with its emphasis on subagent delegation rather than a single long-running context, are the primary differentiators. It keeps trending as new users discover its cross-agent compatibility.

---

## 4. [Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)
> Official code repo for the O'Reilly Book - "Hands-On Large Language Models"

**Language:** Jupyter Notebook  |  **Stars:** 22,267  |  **Forks:** 5,198  |  **Score:** 3,676  |  **Created:** 2024-06-28

**Background:** This repository contains all code notebooks for the O'Reilly book "Hands-On Large Language Models" by Jay Alammar and Maarten Grootendorst, often called "The Illustrated LLM Book" for its nearly 300 custom figures. Each chapter has a corresponding Google Colab-compatible Jupyter notebook covering topics from tokenization and embeddings through fine-tuning, retrieval, and agents. Alammar is known for his illustrated transformer explanations, and Grootendorst is the author of BERTopic.

**Problem it solves:** Most LLM learning resources are either purely theoretical (academic papers) or purely practical (vendor tutorials assuming a specific platform). This book and its code bridge that gap with visual explanations of how models work internally, paired with runnable notebooks that do not require a local GPU.

**Why another one?** The book continues to trend because it remains one of the most accessible entry points to LLM internals for practitioners without a deep ML background. The combination of Alammar's illustration-heavy style with Grootendorst's applied NLP expertise covers a different audience than fast.ai or LangChain tutorials, focusing on understanding model internals rather than just using APIs.

---

## 5. [Kiro](https://github.com/kirodotdev/Kiro)
> Kiro is an agentic IDE that works alongside you from prototype to production.

**Language:** TypeScript  |  **Stars:** 3,041  |  **Forks:** 149  |  **Score:** 3,133  |  **Created:** 2025-06-17

**Background:** Kiro is an agentic IDE built by the team at kirodot.dev, launched in June 2025. It provides an integrated development environment where AI agents work alongside the developer throughout the full lifecycle from prototyping to production deployment. The IDE is built in TypeScript and has accumulated over 3,000 stars.

**Problem it solves:** Most AI coding tools are bolted onto existing editors as extensions or operate as separate terminal agents, creating a disconnect between the AI's understanding and the IDE's capabilities. Kiro integrates agentic assistance directly into the IDE itself, so the AI has native access to project structure, debugging, build systems, and deployment pipelines without requiring external tool integrations.

**Why another one?** While Cursor and Windsurf added AI to VS Code forks, Kiro is built from the ground up as an agent-native IDE rather than retrofitting AI into an existing editor. The focus on the full prototype-to-production lifecycle differentiates it from tools that primarily assist with code generation but leave deployment and operations to the developer.

---

## 6. [cmux](https://github.com/manaflow-ai/cmux)
> Ghostty-based macOS terminal with vertical tabs and notifications for AI coding agents

**Language:** Swift  |  **Stars:** 762  |  **Forks:** 13  |  **Score:** 2,800  |  **Created:** 2026-01-28

**Background:** Cmux is a native macOS terminal application built on Ghostty's terminal emulation library, developed by Manaflow AI. It is designed specifically for AI coding agent workflows, featuring vertical tabs for managing multiple agent sessions, built-in notifications when agents complete tasks, and a streamlined interface optimized for monitoring concurrent agent runs.

**Problem it solves:** Developers running multiple AI coding agents simultaneously struggle with terminal management — standard terminals lack notifications for long-running agent tasks and make it difficult to monitor multiple sessions at a glance. Cmux provides purpose-built UI for this workflow with vertical tabs and completion notifications.

**Why another one?** Existing terminals like iTerm2, Warp, and Ghostty itself are general-purpose tools not optimized for the specific pattern of running and monitoring AI agents. Cmux narrows its scope to this single use case, providing agent-aware notifications and a vertical tab layout designed for concurrent session monitoring rather than traditional shell workflows.

---

## 7. [humanizer](https://github.com/blader/humanizer)
> Claude Code skill that removes signs of AI-generated writing from text

**Language:** N/A  |  **Stars:** 6,015  |  **Forks:** 457  |  **Score:** 2,666  |  **Created:** 2026-01-18

**Background:** Humanizer is a Claude Code skill created by blader that rewrites AI-generated text to remove telltale signs of machine authorship. It operates as a plugin within the Claude Code environment, analyzing text for common AI writing patterns — such as excessive hedging, formulaic transitions, and unnatural phrasing — and rewrites them to read more naturally. The project has gained over 6,000 stars since January 2026.

**Problem it solves:** AI-generated text often exhibits recognizable patterns that make it obvious to readers and detectors alike: overly formal tone, repetitive sentence structure, and characteristic filler phrases. Humanizer processes such text to produce output that reads as naturally written, addressing both readability concerns and detection avoidance.

**Why another one?** Unlike standalone paraphrasing tools or web-based rewriters, Humanizer integrates directly into the Claude Code workflow as a skill, allowing users to apply it immediately to any text output without leaving their development environment. The tight integration with Claude Code's skill system makes it a single-command operation rather than a separate tool.

---

## 8. [openclaw](https://github.com/openclaw/openclaw)
> Your own personal AI assistant. Any OS. Any Platform. The lobster way.

**Language:** TypeScript  |  **Stars:** 215,287  |  **Forks:** 40,386  |  **Score:** 2,065  |  **Created:** 2025-11-24

**Background:** OpenClaw is a personal AI assistant that runs as a locally-hosted gateway, routing conversations through messaging platforms users already have: WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Microsoft Teams, Matrix, and others. It supports voice input and output on macOS, iOS, and Android, and can render an interactive Canvas. With over 215,000 stars since November 2025, it is the most-starred personal assistant project on GitHub.

**Problem it solves:** Personal AI assistants typically require a dedicated app or web interface, creating friction for users who want to interact through channels already open on their phone or desktop. OpenClaw turns existing messaging clients into AI frontends so the assistant is reachable through whatever app the user already has, with no additional app installation required.

**Why another one?** OpenClaw keeps trending because of its massive skill ecosystem (over 5,700 community skills in ClawHub), its multi-channel architecture, and its local-first approach. The ecosystem effect is self-reinforcing: more skills attract more users, who build more skills. The platform's ubiquity across messaging clients creates a network effect that competing assistants have not matched.

---

## 9. [stremio-web](https://github.com/Stremio/stremio-web)
> Stremio - Freedom to Stream

**Language:** JavaScript  |  **Stars:** 9,274  |  **Forks:** 1,035  |  **Score:** 1,966  |  **Created:** 2018-06-04

**Background:** Stremio is a media center application that aggregates content from multiple streaming services and torrent sources into a unified interface. The stremio-web repository is the web-based frontend of the Stremio platform, built in JavaScript and first released in June 2018. The project has accumulated over 9,000 stars and supports an extensive add-on ecosystem for content discovery.

**Problem it solves:** Users with subscriptions to multiple streaming services must switch between different apps to find and watch content, with no unified search or library view. Stremio aggregates catalogs from multiple sources into a single interface where users can search, discover, and stream content regardless of the source.

**Why another one?** Stremio keeps trending because its add-on architecture allows the community to extend content sources without changes to the core application. Unlike Plex or Jellyfin which focus on locally-hosted media libraries, Stremio is designed for aggregating external streaming sources. The web client enables access from any device with a browser without requiring native app installation.

---

## 10. [prompts.chat](https://github.com/f/prompts.chat)
> a.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**Language:** HTML  |  **Stars:** 146,140  |  **Forks:** 19,286  |  **Score:** 1,921  |  **Created:** 2022-12-05

**Background:** Originally launched as "Awesome ChatGPT Prompts" by Fatih Kadir Akin in December 2022, prompts.chat has grown into a full community platform for sharing, discovering, and collecting AI prompts. It now includes a web frontend, a Hugging Face dataset mirror, a self-hosting option for organizational privacy, and an interactive prompt engineering book. The repository has over 146,000 stars and 40 academic citations.

**Problem it solves:** Crafting effective system prompts and persona-based instructions for AI models requires extensive trial and error. Prompts.chat provides a structured, community-maintained library of tested prompts that serve as starting points, reducing the experimentation needed to get useful outputs from general-purpose models.

**Why another one?** This repository trends recurrently because it remains the canonical reference for prompt collections. Its evolution from a static markdown file into a full web platform with community submissions, Hugging Face dataset mirroring, and self-hosting capability has kept it relevant as a living resource. The self-hosting option addresses enterprise privacy concerns that the public site cannot.

---

## 11. [KittenTTS](https://github.com/KittenML/KittenTTS)
> State-of-the-art TTS model under 25MB

**Language:** Python  |  **Stars:** 10,384  |  **Forks:** 559  |  **Score:** 1,895  |  **Created:** 2025-08-05

**Background:** KittenTTS is an extremely compact text-to-speech model developed by KittenML that achieves state-of-the-art quality in under 25MB. Built in Python and released in August 2025, it demonstrates that high-quality speech synthesis does not require multi-gigabyte model files. The project has gained over 10,000 stars.

**Problem it solves:** Most high-quality TTS models require hundreds of megabytes to several gigabytes of storage and significant compute resources, making them impractical for edge devices, mobile applications, and resource-constrained environments. KittenTTS delivers competitive voice quality at a fraction of the size, enabling TTS in contexts where larger models cannot run.

**Why another one?** The sub-25MB size class is the primary differentiator. While models like Qwen3-TTS and Bark prioritize quality at the expense of size, KittenTTS prioritizes extreme compression while maintaining state-of-the-art quality. This makes it uniquely suited for embedded systems, mobile apps, and offline use cases where bandwidth and storage are constrained.

---

## 12. [Mole](https://github.com/tw93/Mole)
> Deep clean and optimize your Mac.

**Language:** Shell  |  **Stars:** 35,825  |  **Forks:** 971  |  **Score:** 1,829  |  **Created:** 2025-09-23

**Background:** Mole is a macOS system cleaning and optimization tool created by tw93, written in Shell and released in September 2025. It performs deep cleaning of caches, logs, temporary files, and other accumulated system debris that slows down macOS over time. The project has grown to over 35,000 stars.

**Problem it solves:** macOS accumulates significant disk space usage from application caches, system logs, Xcode derived data, Homebrew caches, and other temporary files that are not automatically cleaned. Commercial tools like CleanMyMac charge subscription fees for this functionality. Mole provides the same deep cleaning capability as a free, open-source shell script that users can audit.

**Why another one?** Being a transparent shell script rather than a compiled binary is the key trust differentiator — users can read exactly what will be deleted before running it. This addresses the trust problem inherent in system cleaning tools that request broad filesystem access. The open-source approach also means the community can add cleanup targets for new applications without waiting for a vendor update.

---

## 13. [posthog](https://github.com/PostHog/posthog)
> PostHog is an all-in-one developer platform for building successful products. We offer product analytics, web analytics, session replay, error tracking, feature flags, experimentation, surveys, data warehouse, a CDP, and an AI product assistant.

**Language:** Python  |  **Stars:** 31,713  |  **Forks:** 2,317  |  **Score:** 1,828  |  **Created:** 2020-01-23

**Background:** PostHog is an open-source, all-in-one product analytics platform that bundles product analytics, web analytics, session replay, error tracking, feature flags, experimentation, surveys, a data warehouse, a CDP, and an AI product assistant into a single self-hostable product. Founded in January 2020, it has grown to over 31,000 stars and serves as a self-hosted alternative to the combination of Amplitude, Mixpanel, LaunchDarkly, and Hotjar.

**Problem it solves:** Product teams typically stitch together multiple SaaS tools for analytics, session replay, feature flags, and experimentation, creating data silos and increasing vendor costs. PostHog consolidates these capabilities into one platform with a unified data model, reducing integration complexity and ensuring all product data lives in one place.

**Why another one?** PostHog keeps trending because it continues to expand its product surface — adding error tracking, a data warehouse, and an AI assistant on top of its original analytics core. The self-hosting option appeals to companies with data sovereignty requirements, and the open-source model allows the community to contribute integrations. Each new capability announcement drives renewed visibility.

---

## 14. [opencode](https://github.com/anomalyco/opencode)
> The open source coding agent.

**Language:** TypeScript  |  **Stars:** 107,795  |  **Forks:** 10,640  |  **Score:** 1,782  |  **Created:** 2025-04-30

**Background:** OpenCode is an open-source terminal-based coding agent developed by Anomaly, launched in April 2025. It provides an agentic coding assistant that operates in the terminal, understands codebases, and executes development tasks through natural language commands. With over 107,000 stars, it is one of the most popular open-source coding agents on GitHub.

**Problem it solves:** Developers need AI coding assistance that integrates into their existing terminal workflow without being locked into a specific IDE or vendor. OpenCode provides a fully open-source alternative to proprietary coding agents, giving users the freedom to inspect, modify, and self-host the entire system while retaining terminal-native convenience.

**Why another one?** OpenCode keeps trending because it occupies the open-source counterpart position to proprietary coding agents. Its fully open codebase allows the community to add model backends, customize behaviors, and build extensions without vendor approval. The 107,000-star milestone reflects the demand for a transparent, community-driven coding agent.

---

## 15. [freemocap](https://github.com/freemocap/freemocap)
> Free Motion Capture for Everyone

**Language:** Python  |  **Stars:** 5,617  |  **Forks:** 444  |  **Score:** 1,721  |  **Created:** 2021-04-12

**Background:** FreeMoCap is a free and open-source markerless motion capture system built in Python, created in April 2021. It uses standard webcams to perform full-body motion capture without requiring specialized hardware, expensive suits, or reflective markers. The system processes multi-camera video streams to reconstruct 3D skeletal motion data.

**Problem it solves:** Professional motion capture systems from Vicon or OptiTrack cost tens of thousands of dollars and require dedicated studio spaces with specialized cameras and reflective markers. FreeMoCap democratizes motion capture by using consumer webcams and computer vision, making it accessible to independent animators, researchers, and hobbyists who cannot afford professional setups.

**Why another one?** The zero-cost hardware requirement is the fundamental differentiator — any setup with two or more webcams can produce usable motion capture data. While other markerless solutions like MediaPipe provide 2D pose estimation, FreeMoCap reconstructs full 3D skeletal data from multiple camera angles. The Python-based pipeline also integrates easily with Blender and other animation tools.

---

## 16. [claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
> Official, Anthropic-managed directory of high quality Claude Code Plugins.

**Language:** Python  |  **Stars:** 7,985  |  **Forks:** 781  |  **Score:** 1,588  |  **Created:** 2025-11-20

**Background:** Claude Plugins Official is Anthropic's curated directory of high-quality Claude Code plugins, launched in November 2025. It serves as the official, vetted collection of plugins that extend Claude Code's capabilities, with each plugin reviewed and maintained to Anthropic's quality and security standards. The repository has accumulated nearly 8,000 stars.

**Problem it solves:** The growing ecosystem of community-built Claude Code plugins varies widely in quality, security, and maintenance. This official directory provides a trusted source where users can find plugins that have been reviewed by Anthropic, reducing the risk of installing poorly maintained or potentially malicious extensions.

**Why another one?** As the official Anthropic-managed directory, it provides a level of trust and quality assurance that community-maintained lists cannot guarantee. Each plugin undergoes security review and is tested for compatibility with current Claude Code versions, addressing the same trust gap that official app stores address for mobile platforms.

---

## 17. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Language:** Shell  |  **Stars:** 68,067  |  **Forks:** 5,340  |  **Score:** 1,581  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official terminal-based agentic coding tool, launched in February 2025. It operates directly in the developer's terminal, understanding the full codebase context and executing tasks through natural language commands. The tool handles routine development tasks, explains complex code, manages git workflows, and supports an extensible skills and hooks system for customization.

**Problem it solves:** Developers spend significant time on repetitive coding tasks, navigating unfamiliar codebases, and managing version control workflows. Claude Code automates these tasks directly in the terminal where developers already work, eliminating the context-switching overhead of moving between an IDE, a browser-based AI chat, and the command line.

**Why another one?** Claude Code keeps trending because it is Anthropic's first-party coding agent and has become a reference implementation for terminal-based agentic development. Its growing ecosystem of community skills, hooks, and configurations drives continuous adoption. The extensibility through the skills framework means the tool's capabilities expand with community contributions rather than only through official releases.

---

## 18. [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)
> the best agent harness

**Language:** TypeScript  |  **Stars:** 32,679  |  **Forks:** 2,466  |  **Score:** 1,430  |  **Created:** 2025-12-03

**Background:** Oh My OpenCode is a community-driven configuration and plugin framework for the OpenCode coding agent, built in TypeScript by code-yeongyu. Similar in concept to oh-my-zsh for the Zsh shell, it provides a curated collection of themes, plugins, and configurations that enhance the OpenCode experience. The project launched in December 2025 and has grown to over 32,000 stars.

**Problem it solves:** OpenCode's default configuration provides a baseline experience, but customizing it requires manually sourcing and configuring plugins, themes, and settings from scattered community repositories. Oh My OpenCode bundles these into a single installable framework with a plugin manager, making customization a one-command operation.

**Why another one?** The oh-my-* pattern (proven by oh-my-zsh with 180,000+ stars) has demonstrated that configuration frameworks for popular tools attract massive adoption. Oh My OpenCode applies this proven model to the second most-starred coding agent, providing the same convenience of curated defaults and easy plugin discovery that made oh-my-zsh successful.

---

## 19. [readest](https://github.com/readest/readest)
> Readest is a modern, feature-rich ebook reader designed for avid readers offering seamless cross-platform access, powerful tools, and an intuitive interface to elevate your reading experience.

**Language:** TypeScript  |  **Stars:** 17,791  |  **Forks:** 960  |  **Score:** 1,424  |  **Created:** 2024-10-12

**Background:** Readest is a cross-platform ebook reader built in TypeScript, launched in October 2024. It supports major ebook formats and provides features such as annotations, highlights, customizable reading themes, and cross-device synchronization. The application is designed for avid readers who want a modern, polished reading experience across desktop and mobile platforms.

**Problem it solves:** Existing open-source ebook readers like Calibre prioritize library management over reading experience, while commercial options like Kindle lock users into a single ecosystem. Readest focuses on the reading experience itself — typography, annotation tools, and cross-platform sync — without vendor lock-in or format restrictions.

**Why another one?** Readest differentiates by prioritizing the reading UX over library management. While Calibre is the standard for ebook management and conversion, its reader interface is dated. Readest inverts the priority, offering a modern reading experience with an intuitive interface while remaining open-source and cross-platform.

---

## 20. [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
> GitNexus: The Zero-Server Code Intelligence Engine - a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph with a built in Graph RAG Agent. Perfect for code exploration.

**Language:** TypeScript  |  **Stars:** 885  |  **Forks:** 82  |  **Score:** 1,410  |  **Created:** 2025-08-02

**Background:** GitNexus is a client-side code intelligence tool that generates interactive knowledge graphs from GitHub repositories or ZIP files, running entirely in the browser with no server component. It includes a built-in Graph RAG Agent that allows users to query the generated knowledge graph conversationally. The project was created by Abhigyan Patwari and launched in August 2025.

**Problem it solves:** Understanding an unfamiliar codebase typically requires cloning, setting up a local environment, and manually tracing dependencies and relationships between modules. GitNexus eliminates the setup step entirely — users drop in a repo URL or ZIP file in their browser and immediately get a visual knowledge graph of the codebase's structure with an AI agent for exploration.

**Why another one?** The zero-server, fully client-side architecture is the primary differentiator against code intelligence tools like Sourcegraph or CodeSee, which require server-side indexing. Running entirely in the browser means no data leaves the user's machine, addressing privacy concerns for proprietary codebases. The integrated Graph RAG Agent adds conversational exploration on top of the visual graph.

---

## 21. [hyperbrowser-app-examples](https://github.com/hyperbrowserai/hyperbrowser-app-examples)
> This repo contains fully functional Hyperbrowser powered web apps

**Language:** TypeScript  |  **Stars:** 583  |  **Forks:** 89  |  **Score:** 1,306  |  **Created:** 2025-05-28

**Background:** This repository contains a collection of fully functional example web applications built using Hyperbrowser, an AI-powered browser automation platform. Created by the Hyperbrowser AI team in May 2025, it provides reference implementations for common web automation tasks and serves as both documentation and starter templates for new Hyperbrowser users.

**Problem it solves:** Browser automation platforms have steep learning curves, and official documentation often lacks complete, end-to-end examples. This repository provides working applications that demonstrate real-world use cases, reducing the time from initial interest to a functional application by providing copy-and-modify starting points.

**Why another one?** Unlike documentation snippets that show isolated API calls, these are complete, deployable applications that handle edge cases, error states, and production concerns. Each example demonstrates a full user-facing workflow rather than just the automation layer, making them directly usable as starting points for production applications.

---

## 22. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> The awesome collection of OpenClaw Skills. Formerly known as Moltbot, originally Clawdbot.

**Language:** N/A  |  **Stars:** 17,555  |  **Forks:** 1,799  |  **Score:** 1,262  |  **Created:** 2026-01-25

**Background:** Awesome OpenClaw Skills is a curated index of over 3,000 community-built skills for the OpenClaw assistant, maintained by VoltAgent. It draws from ClawHub, OpenClaw's public registry of over 5,700 skills, but filters out spam, crypto content, duplicates, and skills identified as malicious by security researchers. The project was formerly known as Moltbot and originally as Clawdbot.

**Problem it solves:** The ClawHub registry is large and unfiltered, making it difficult to find trustworthy, useful skills without wading through spam, duplicates, and potentially malicious entries. This curated list applies documented quality and security filters, providing reasonable confidence that listed skills are functional and safe to install.

**Why another one?** The OpenClaw skill ecosystem is the primary extensibility mechanism for the most-starred personal assistant on GitHub, and no official curated list exists. The security angle — explicitly cataloguing malicious skills and providing guidance on VirusTotal partnership checks — adds a layer of value that the raw ClawHub registry does not provide. The name changes reflect the rapid evolution of the broader ecosystem.

---

## 23. [zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)
> Fast, small, and fully autonomous AI assistant infrastructure — deploy anywhere, swap anything

**Language:** Rust  |  **Stars:** 16,846  |  **Forks:** 1,937  |  **Score:** 1,223  |  **Created:** 2026-02-13

**Background:** Zeroclaw is an AI assistant infrastructure written in Rust by zeroclaw-labs, launched in mid-February 2026. It provides a minimal, high-performance runtime for deploying autonomous AI assistants with a modular architecture that allows swapping out any component — model backend, messaging interface, storage, and skills. The project has already reached nearly 17,000 stars in just over a week.

**Problem it solves:** Existing AI assistant platforms like OpenClaw are feature-rich but come with significant deployment overhead and opinionated architecture choices. Zeroclaw strips the concept down to a minimal Rust runtime where every component is pluggable, allowing developers to deploy lightweight assistants on resource-constrained hardware or customize the stack for specific use cases.

**Why another one?** The Rust implementation targets a performance and size class that TypeScript-based assistants like OpenClaw cannot match — faster startup, lower memory usage, and smaller binary size. The fully modular architecture means developers can swap any component without forking the project, and the "deploy anywhere" philosophy supports environments from Raspberry Pis to cloud VMs with the same binary.

---

## 24. [electrobun](https://github.com/blackboardsh/electrobun)
> Build ultra fast, tiny, and cross-platform desktop apps with Typescript.

**Language:** C++  |  **Stars:** 6,274  |  **Forks:** 115  |  **Score:** 1,196  |  **Created:** 2024-02-28

**Background:** Electrobun is a desktop application framework developed by Blackboard that enables building cross-platform applications with TypeScript. Unlike Electron, which bundles Chromium, Electrobun uses a C++ core with the system's native webview to produce ultra-fast, tiny application binaries. The project launched in February 2024 and has accumulated over 6,200 stars.

**Problem it solves:** Electron applications are notoriously large (100MB+ just for the runtime) and memory-hungry because each app bundles its own Chromium instance. Electrobun dramatically reduces both binary size and memory usage by leveraging the operating system's native webview while still allowing developers to write their application logic in TypeScript.

**Why another one?** Electrobun occupies the space between Electron (easy but heavy) and Tauri (lightweight but requires Rust). By using C++ for the native layer while keeping the developer-facing API in TypeScript, it avoids requiring developers to learn a systems language while achieving binary sizes and performance closer to native applications than Electron can deliver.

---

## 25. [timesfm](https://github.com/google-research/timesfm)
> TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting.

**Language:** Python  |  **Stars:** 8,851  |  **Forks:** 732  |  **Score:** 1,138  |  **Created:** 2024-04-29

**Background:** TimesFM is a pretrained time-series foundation model developed by Google Research, released in April 2024. It applies the foundation model paradigm — pretraining on large diverse datasets followed by zero-shot or few-shot inference — to time-series forecasting. The model is built in Python and has accumulated nearly 9,000 stars.

**Problem it solves:** Traditional time-series forecasting requires training separate models for each dataset, which demands domain expertise in feature engineering, model selection, and hyperparameter tuning. TimesFM provides a pretrained model that can produce forecasts on new time-series data without task-specific training, dramatically reducing the effort required to deploy forecasting capabilities.

**Why another one?** TimesFM is backed by Google Research and applies the foundation model approach that succeeded in NLP and vision to time-series data. Unlike statistical methods (ARIMA, Prophet) that require per-series fitting, or deep learning models (N-BEATS, PatchTST) that require task-specific training, TimesFM offers zero-shot forecasting from a single pretrained checkpoint. The Google Research pedigree provides confidence in the model's evaluation rigor.

---

> **Day's theme:** AI-powered development tools dominate the chart with coding agents, IDE integrations, and skill ecosystems accounting for over half the entries, while a strong undercurrent of local-first, open-source alternatives to commercial products — from voice synthesis to motion capture to Mac optimization — reflects the community's push toward sovereignty over both code and data.
