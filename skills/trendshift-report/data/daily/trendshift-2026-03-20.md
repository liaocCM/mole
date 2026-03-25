# Trendshift Report — 2026-03-20
**Total:** 25 repositories

---

## 1. [skills](https://github.com/mattpocock/skills)
> My personal directory of skills, straight from my .claude directory.

**Language:** Shell  |  **Stars:** 9,379  |  **Forks:** 769  |  **Score:** 19,146  |  **Created:** 2026-02-03

**Background:** Skills is a collection of agent skills by Matt Pocock, the TypeScript educator known for Total TypeScript. The repository provides installable skills for AI coding agents covering planning (PRD writing, implementation planning, issue decomposition), development (TDD loops, bug triage, codebase architecture improvement), tooling (pre-commit hooks, git guardrails), and writing (skill authoring, article editing, Obsidian vault management). Each skill is distributed via `npx skills@latest add` for one-command installation.

**Problem it solves:** Coding agents have powerful reasoning capabilities but lack structured workflows for common development tasks. Writing a good PRD, decomposing it into vertical slices, or running a disciplined red-green-refactor TDD loop requires explicit process guidance that most agents do not ship with. Pocock's skills encode these workflows so the agent executes them consistently.

**Why another one?** The differentiating angle is Pocock's TypeScript community reach and his opinionated development philosophy — skills like "grill-me" (relentless interview until every design branch is resolved) and "improve-codebase-architecture" (deepening shallow modules) reflect a specific software craftsmanship perspective. The collection is also notably compact and focused compared to larger skill frameworks like Superpowers.

---

## 2. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 108,363  |  **Forks:** 8,701  |  **Score:** 13,622  |  **Created:** 2025-10-09

**Background:** Superpowers is a composable skills framework and structured software development methodology created by Jesse Vincent (obra), designed to install into coding agents such as Claude Code, Cursor, Codex, OpenCode, and Gemini CLI via their plugin marketplaces. It enforces a multi-stage workflow: brainstorming and spec refinement before any code is written, detailed implementation planning with bite-sized tasks, then subagent-driven development with two-stage code review. The project has surpassed 108,000 stars since its October 2025 launch.

**Problem it solves:** Coding agents left to their own defaults tend to dive directly into writing code, skip test-driven development, and drift from the original intent mid-session. Superpowers installs guard rails — mandatory spec approval, red-green-refactor TDD enforcement, and plan checkpoints — so an agent can work autonomously for hours without derailing from what was agreed.

**Why another one?** Rather than being a new coding agent itself, Superpowers is a methodology layer that works across multiple agents via their plugin systems. The differentiating angle is portability (same skills install in Claude Code, Cursor, Codex, OpenCode, and Gemini CLI) and the emphasis on subagent delegation rather than a single long-running context, which limits drift.

---

## 3. [NemoClaw](https://github.com/NVIDIA/NemoClaw)
> Run OpenClaw more securely inside NVIDIA OpenShell with managed inference

**Language:** JavaScript  |  **Stars:** 16,028  |  **Forks:** 1,685  |  **Score:** 10,885  |  **Created:** 2026-03-15

**Background:** NVIDIA NemoClaw is an open-source reference stack released in alpha on March 16, 2026, that simplifies running OpenClaw always-on assistants inside NVIDIA's OpenShell sandboxed runtime. It installs the OpenShell container environment (part of NVIDIA Agent Toolkit), which provides security isolation for autonomous agents, and bundles open-source NVIDIA Nemotron models for local inference. The installer runs a guided onboarding wizard that creates the sandbox, configures inference, and applies security policies.

**Problem it solves:** Running an always-on AI assistant like OpenClaw with full system access is a security liability — the agent can execute arbitrary commands, access sensitive files, and make network requests without containment. NemoClaw addresses this by placing the entire OpenClaw instance inside a sandboxed container with managed inference, so the agent operates within defined security boundaries.

**Why another one?** NemoClaw is NVIDIA's entry into the agent security infrastructure space, leveraging their existing OpenShell runtime and Nemotron model family. The differentiation is the combination of hardware-vendor-backed security (NVIDIA's container isolation) with open-source models that can run on NVIDIA GPUs without external API dependencies. The DGX Spark setup guide signals enterprise and edge deployment as primary targets.

---

## 4. [gstack](https://github.com/garrytan/gstack)
> Use Garry Tan's exact Claude Code setup: 15 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**Language:** TypeScript  |  **Stars:** 39,705  |  **Forks:** 4,906  |  **Score:** 6,435  |  **Created:** 2026-03-11

**Background:** gstack is Garry Tan's personal Claude Code configuration, open-sourced under MIT license. Tan, the President and CEO of Y Combinator, shares the exact setup he uses to ship 10,000-20,000 lines of production code per day while running YC full-time. The system turns Claude Code into a virtual engineering team via 20+ slash commands — `/plan-ceo-review` for product rethinking, `/review` for code review, `/qa` for browser-based QA using Playwright, `/cso` for security audits (OWASP + STRIDE), and `/ship` for release engineering.

**Problem it solves:** Claude Code ships with minimal default configuration, and most developers start with a blank prompt. gstack provides a structured, role-based setup so that a solo developer or founder can access the equivalent of a full engineering team's review, QA, design, and release processes through slash commands.

**Why another one?** The credibility angle is unique: Tan has worked with thousands of YC startups (Coinbase, Instacart, Rippling) and was an early engineer at Palantir. The README's claim of 600,000+ lines of production code in 60 days, with concrete GitHub contribution graphs comparing 2013 vs 2026, provides a verifiable productivity narrative that most configuration repositories lack.

---

## 5. [claude-hud](https://github.com/jarrodwatts/claude-hud)
> A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress

**Language:** JavaScript  |  **Stars:** 12,154  |  **Forks:** 505  |  **Score:** 6,401  |  **Created:** 2026-01-02

**Background:** Claude HUD is a Claude Code plugin by Jarrod Watts that adds a persistent status display below the input prompt, showing real-time context window usage, active tool invocations, running subagent status, and todo progress. It uses Claude Code's native statusline API — no separate window or tmux required — and updates every 300ms by parsing the session transcript for tool and agent activity.

**Problem it solves:** Claude Code sessions provide no persistent visibility into how much context has been consumed, what tools are actively running, or how far along a multi-step task is. Developers often hit context limits unexpectedly or cannot tell if a long-running subagent has stalled. The HUD surfaces this information continuously without interrupting the workflow.

**Why another one?** Claude HUD is narrowly scoped to observability rather than being a full skill or workflow framework. The use of native token data from Claude Code (not estimated) and support for 1M-context sessions makes it accurate for the latest model configurations. The plugin marketplace distribution model and interactive `/claude-hud:configure` setup flow lower the adoption barrier compared to manual configuration approaches.

---

## 6. [unsloth](https://github.com/unslothai/unsloth)
> Unsloth Studio is a web UI for training and running open models like Qwen, DeepSeek, gpt-oss and Gemma locally.

**Language:** Python  |  **Stars:** 57,675  |  **Forks:** 4,860  |  **Score:** 5,349  |  **Created:** 2023-11-29

**Background:** Unsloth Studio is a local-first web UI for running and fine-tuning open-source AI models, supporting text, audio, embedding, and vision models on Windows, Linux, and macOS. It provides inference features (model search, download, GGUF/LoRA/safetensors support, tool calling, code execution) and training features (2x faster fine-tuning with 70% less VRAM using custom Triton kernels, reinforcement learning with 80% less VRAM for GRPO, data recipe workflows from PDF/CSV/DOCX). The project collaborates directly with teams behind gpt-oss, Qwen3, Llama 4, and Gemma.

**Problem it solves:** Running and fine-tuning open models locally requires cobbling together multiple tools — model downloaders, quantization scripts, inference servers, training frameworks — each with its own configuration and compatibility issues. Unsloth Studio provides a unified interface that handles the entire workflow from model discovery through training to export.

**Why another one?** Unsloth's differentiation is the custom kernel engineering that delivers measurable performance gains: 2x faster training and 70% less VRAM is backed by collaborations with PyTorch and Hugging Face. The direct partnerships with model teams (fixing bugs in Qwen3, Llama 4, Gemma) mean Unsloth often has day-one optimized support for new model releases.

---

## 7. [opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf)
> PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.

**Language:** Java  |  **Stars:** 9,094  |  **Forks:** 662  |  **Score:** 4,737  |  **Created:** 2025-05-13

**Background:** OpenDataLoader PDF is an Apache-2.0-licensed PDF parser optimized for AI data extraction pipelines, with SDKs for Python, Node.js, and Java. It claims the top position in extraction benchmarks (0.90 overall accuracy, 0.93 table extraction across 200 real-world PDFs) and supports both a deterministic local mode (0.05s/page) and an AI hybrid mode for complex pages with OCR, formulas, and charts. A secondary mission is PDF accessibility automation — the first open-source tool to generate Tagged PDFs end-to-end (planned Q2 2026), developed in collaboration with the PDF Association.

**Problem it solves:** PDF extraction for RAG and LLM pipelines is notoriously unreliable — tables break, reading order scrambles, scanned documents fail, and multi-column layouts confuse parsers. OpenDataLoader addresses these with XY-Cut++ reading order, bounding boxes for every element, and a hybrid AI mode for complex pages, producing structured Markdown, JSON, or HTML suitable for direct chunking and retrieval.

**Why another one?** The benchmark-first positioning (claiming #1 across 200 real-world PDFs) and the dual mission of AI extraction plus accessibility compliance set it apart from competitors like PyMuPDF, Marker, or Docling. The upcoming auto-tagging feature for Tagged PDF output addresses a regulatory need (accessibility compliance costs $50-200 per document manually) that no other open-source tool currently covers.

---

## 8. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 60,953  |  **Forks:** 9,146  |  **Score:** 4,168  |  **Created:** 2025-10-13

**Background:** Agency Agents is a collection of meticulously crafted AI agent personalities by Maciej Sitarzewski, each with deep domain expertise, unique communication style, and deliverable-focused workflows. The roster spans engineering (frontend, backend, mobile, AI, DevOps, security), growth (SEO, content, social media, community management), design (UX researcher, brand strategist), management (product manager, Scrum master), and creative divisions. Each agent file contains identity traits, core workflows, technical deliverables with code examples, and success metrics.

**Problem it solves:** Generic AI prompting produces generic outputs. When you ask an AI to "build a React component," it lacks the persona context that shapes how a senior frontend developer would approach the problem versus a rapid prototyper versus a security engineer. Agency Agents provides pre-built specialist personas so the AI approaches each task with domain-appropriate expertise, processes, and quality standards.

**Why another one?** The differentiating angle is the breadth and depth of the personality engineering — over 60,000 stars suggest the community values the "specialist with personality" approach over generic role prompts. The multi-tool integration (Claude Code, Cursor, Aider, Windsurf, Gemini CLI, OpenCode) via conversion and install scripts makes the collection portable across the fragmented AI coding tool landscape.

---

## 9. [open-swe](https://github.com/langchain-ai/open-swe)
> An Open-Source Asynchronous Coding Agent

**Language:** Python  |  **Stars:** 8,172  |  **Forks:** 964  |  **Score:** 4,040  |  **Created:** 2025-05-21

**Background:** Open SWE is an open-source framework by LangChain for building internal coding agents, modeled after the architecture that companies like Stripe (Minions), Ramp (Inspect), and Coinbase (Cloudbot) built internally. It is built on LangGraph and the Deep Agents framework, providing cloud sandboxes (Modal, Daytona, Runloop, LangSmith), Slack and Linear invocation, subagent orchestration, and automatic PR creation. Every task runs in an isolated cloud sandbox with full shell access and zero production risk.

**Problem it solves:** Elite engineering organizations are building internal coding agents — Slackbots, CLIs, and web apps that meet engineers where they already work — but doing so requires significant custom infrastructure. Open SWE packages the common architectural patterns (sandbox isolation, invocation from chat/project management tools, subagent delegation, PR automation) into an open-source framework that any organization can customize.

**Why another one?** Open SWE differentiates by composing on the Deep Agents framework rather than forking an existing agent, giving users an upgrade path as upstream improves. The explicit multi-sandbox-provider support and the Slack/Linear integration target the enterprise "internal tooling" use case rather than individual developer productivity, filling a gap between general coding agents and fully custom internal builds.

---

## 10. [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)
> Open Multi-Agent Interactive Classroom — Get an immersive, multi-agent learning experience in just one click

**Language:** TypeScript  |  **Stars:** 11,788  |  **Forks:** 1,763  |  **Score:** 3,751  |  **Created:** 2026-03-11

**Background:** OpenMAIC (Open Multi-Agent Interactive Classroom) is an open-source AI education platform from Tsinghua University's MAIC group, published in JCST 2026. It turns any topic or document into an interactive classroom experience with AI teachers and AI classmates who lecture, discuss, draw on whiteboards, and engage in real-time conversations. Built with Next.js 16, React 19, TypeScript, LangGraph, and Tailwind CSS, it supports one-click lesson generation, slides, quizzes, interactive HTML simulations, and project-based learning.

**Problem it solves:** Self-directed learning with AI typically means a chat interface where the learner must drive the entire interaction. OpenMAIC creates a structured classroom environment — complete with multi-agent discussion, whiteboard explanations, quizzes, and simulations — that provides the pedagogical scaffolding of a real classroom without requiring a human instructor.

**Why another one?** The multi-agent classroom metaphor is the differentiator: rather than a single AI tutor, OpenMAIC deploys multiple agents (teachers and peers) that discuss, debate, and explain from different angles. The integration with OpenClaw enables classroom generation from messaging apps (Feishu, Slack, Telegram), and the one-click Vercel deployment lowers the barrier for educators who want to self-host.

---

## 11. [arnis](https://github.com/louis-e/arnis)
> Generate any location from the real world in Minecraft with a high level of detail.

**Language:** Rust  |  **Stars:** 13,042  |  **Forks:** 1,058  |  **Score:** 3,750  |  **Created:** 2022-09-10

**Background:** Arnis is a free, open-source tool written in Rust that generates detailed Minecraft Java Edition (1.17+) and Bedrock Edition worlds reflecting real-world geography, topography, and architecture. It processes geospatial data from OpenStreetMap and elevation data to create accurate Minecraft representations of terrain and buildings. A companion web app, MapSmith, enables browser-based generation without local installation. The project features a GUI for selecting map areas and customizing generation settings.

**Problem it solves:** Manually recreating real-world locations in Minecraft is extremely time-consuming — a single neighborhood can take hundreds of hours. Arnis automates the entire process: select a rectangle on a map, choose your Minecraft world, and click "Start Generation." The algorithm handles building placement, road networks, terrain elevation, and architectural detail from open geographic data.

**Why another one?** Arnis has been maintained since September 2022, giving it stability and feature maturity that newer competitors lack. The Rust implementation provides performance optimization for large-scale geographic data processing, and the dual support for Java and Bedrock editions covers the full Minecraft player base. MapSmith's browser-based generation also extends accessibility to mobile users and those who cannot install native software.

---

## 12. [AIClient-2-API](https://github.com/justlovemaki/AIClient-2-API)
> Simulates Gemini CLI, Antigravity, Qwen Code, and Kiro client requests, compatible with the OpenAI API.

**Language:** JavaScript  |  **Stars:** 6,228  |  **Forks:** 916  |  **Score:** 3,378  |  **Created:** 2025-07-20

**Background:** AIClient-2-API is a Node.js proxy service that converts free large models restricted to client-only use (Gemini CLI, Antigravity, Qwen Code, Kiro) into standard OpenAI-compatible API interfaces callable by any application. It supports intelligent conversion between OpenAI, Claude, and Gemini protocols, with built-in account pool management, intelligent polling, automatic failover, and health check mechanisms. Recent updates added Grok protocol support (xAI Grok 3/4 via Cookie/SSO) and Codex OAuth authorization access.

**Problem it solves:** Several AI model providers offer free access through their official clients but do not expose standard API endpoints. Developers wanting to use these models in their own applications, tools like Cherry-Studio or NextChat, or coding assistants like Cline are blocked by the client-only restriction. AIClient-2-API bridges this gap by simulating client requests and re-exposing the models through a standard OpenAI-compatible interface.

**Why another one?** The project covers a broader set of client protocols than alternatives — Gemini CLI, Antigravity, Qwen Code, Kiro, and Grok — with a modular architecture based on strategy and adapter patterns that makes adding new providers straightforward. The account pool management with automatic failover and health checks targets reliability at scale, claiming 99.9% service availability.

---

## 13. [genlayer-project-boilerplate](https://github.com/genlayerlabs/genlayer-project-boilerplate)
> Sample GenLayer project with intelligent contracts

**Language:** TypeScript  |  **Stars:** 8,592  |  **Forks:** 312  |  **Score:** 3,280  |  **Created:** 2024-06-28

**Background:** This is the official boilerplate repository for GenLayer, a blockchain platform by GenLayer Labs (formerly YeagerAI) that supports "intelligent contracts" — smart contracts that can access the web and use AI models as part of their execution logic. The boilerplate includes a football bets example contract written in Python, end-to-end tests, and a production-ready Next.js 15 frontend with TypeScript, TanStack Query, and Radix UI. Deployment targets include local, studio, and test networks via the GenLayer CLI.

**Problem it solves:** Traditional smart contracts are deterministic and isolated — they cannot access external data or perform reasoning. GenLayer's intelligent contracts can fetch web content and invoke AI models during execution, enabling use cases like sports betting where the contract itself can verify match results from web sources without relying on a separate oracle.

**Why another one?** GenLayer occupies a niche between traditional blockchain platforms and AI agent frameworks by embedding AI directly into the smart contract execution layer. The intelligent contract paradigm — where the on-chain logic itself can reason and access external data — is architecturally distinct from bolting an AI agent onto a standard blockchain via oracles.

---

## 14. [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
> An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

**Language:** Python  |  **Stars:** 49,030  |  **Forks:** 4,747  |  **Score:** 3,124  |  **Created:** 2025-11-30

**Background:** UI UX Pro Max is an AI skill that provides design intelligence for building professional UI/UX across multiple platforms and frameworks. Version 2.0 introduced an intelligent Design System Generator — a reasoning engine with 161 rules and 67 UI styles that analyzes project requirements and generates a complete, tailored design system. It includes pattern recommendations (hero-centric, social proof, dashboard), color theory, typography, and component specifications. The skill is installable via npm CLI or manual setup.

**Problem it solves:** AI coding agents can generate functional UI code but tend to produce generic, aesthetically poor interfaces — the "AI slop" problem. UI UX Pro Max injects design reasoning into the agent's workflow, providing contextual decisions about layout patterns, color palettes, typography scales, and component styling based on the specific project type and audience.

**Why another one?** The 161 reasoning rules and 67 curated UI styles represent a depth of design knowledge that generic prompt engineering cannot match. The Design System Generator's ability to analyze project context and produce a complete, coherent design system — not just individual component styles — addresses the systematic nature of good UI/UX design rather than treating it as decoration applied after the fact.

---

## 15. [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)
> GEO-first SEO skill for Claude Code. Comprehensive AI search optimization for any website.

**Language:** Python  |  **Stars:** 3,698  |  **Forks:** 577  |  **Score:** 3,108  |  **Created:** 2026-02-18

**Background:** GEO-SEO Claude is a Claude Code skill by Zubair Trabzada that optimizes websites for AI-powered search engines (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews) while maintaining traditional SEO foundations. It provides 12 commands including full GEO audits, citability scoring, AI crawler access analysis, llms.txt generation, brand mention scanning, platform-specific optimization, schema markup analysis, and PDF report generation. The skill uses 5 parallel subagents for comprehensive analysis.

**Problem it solves:** AI search is growing rapidly (527% year-over-year traffic growth) but only 23% of marketers are investing in GEO (Generative Engine Optimization). Traditional SEO tools do not measure whether content is citable by AI systems, whether AI crawlers can access it, or whether brand mentions appear in AI-cited platforms. This skill fills that gap with AI-specific auditing and optimization.

**Why another one?** The GEO-first positioning is the differentiator — most SEO tools treat AI search as an afterthought. The citability scoring engine, AI crawler access analysis (robots.txt configuration for AI bots), and llms.txt standard support address the specific mechanics of how AI systems discover and cite content, rather than retrofitting traditional SEO metrics.

---

## 16. [PhotoGIMP](https://github.com/Diolinux/PhotoGIMP)
> A Patch for GIMP 3+ for Photoshop Users

**Language:** CSS  |  **Stars:** 7,923  |  **Forks:** 231  |  **Score:** 3,030  |  **Created:** 2020-06-19

**Background:** PhotoGIMP is a free, community-driven configuration patch by Diolinux that transforms GIMP (GNU Image Manipulation Program) into a layout familiar to Adobe Photoshop users. It provides Photoshop-like tool layout, keyboard shortcuts following Adobe's official documentation, a maximized canvas workspace, a custom splash screen, and a dedicated desktop icon. The project supports GIMP 3.0+ on Linux (Flatpak and native), macOS, and Windows.

**Problem it solves:** Switching from Photoshop to GIMP involves a steep learning curve because GIMP's default interface, tool positions, and keyboard shortcuts differ significantly from Photoshop's conventions. PhotoGIMP eliminates this friction by making GIMP look and behave like Photoshop, allowing designers to transition without relearning muscle memory.

**Why another one?** PhotoGIMP has been maintained since June 2020 and is now updated for GIMP 3.0, which represents a major release with significant UI changes. The timing of this trending appearance likely corresponds to GIMP 3.0's release, driving new interest from Photoshop users exploring the free alternative. The project is purely a configuration overlay, requiring no code changes to GIMP itself.

---

## 17. [TradingAgents](https://github.com/TauricResearch/TradingAgents)
> TradingAgents: Multi-Agents LLM Financial Trading Framework

**Language:** Python  |  **Stars:** 39,393  |  **Forks:** 7,323  |  **Score:** 2,938  |  **Created:** 2024-12-28

**Background:** TradingAgents is an open-source multi-agent trading framework by Tauric Research that mirrors the dynamics of real-world trading firms. It deploys specialized LLM-powered agents — fundamental analysts, sentiment experts, technical analysts, a trader, and a risk management team — that collaboratively evaluate market conditions and inform trading decisions. Version 0.2.2 (March 2026) added GPT-5.4, Gemini 3.1, and Claude 4.6 model coverage, a five-tier rating scale, and cross-platform stability improvements. An associated paper is published on arXiv.

**Problem it solves:** Individual AI trading models typically analyze a single dimension (price patterns, or sentiment, or fundamentals) in isolation. TradingAgents replicates how actual trading firms operate: multiple specialists with different analytical perspectives debate and synthesize a collective trading decision, with a dedicated risk management layer that applies portfolio-level constraints.

**Why another one?** The academic backing (arXiv paper, Trading-R1 technical report) and the multi-agent firm simulation architecture differentiate it from single-model trading bots. The v0.2.2 release's multi-provider LLM support means the framework is not locked into a single model vendor, and the five-tier rating scale provides more nuanced signals than binary buy/sell recommendations.

---

## 18. [llm-app](https://github.com/pathwaycom/llm-app)
> Ready-to-run cloud templates for RAG, AI pipelines, and enterprise search with live data.

**Language:** Jupyter Notebook  |  **Stars:** 58,639  |  **Forks:** 1,392  |  **Score:** 2,880  |  **Created:** 2023-07-19

**Background:** Pathway AI Pipelines provides ready-to-deploy LLM application templates that offer high-accuracy RAG and AI enterprise search at scale using live data. The templates connect and sync with data sources on file systems, Google Drive, Sharepoint, S3, Kafka, PostgreSQL, and real-time APIs, with built-in vector search, hybrid search, and full-text search — all done in-memory with caching. Templates scale to millions of pages and include question-answering RAG, live document indexing, multimodal RAG, and agentic pipelines.

**Problem it solves:** Building production RAG pipelines requires solving data synchronization (keeping indexes current as documents change), multi-source integration, and choosing between vector, hybrid, and full-text search strategies. Pathway provides this infrastructure layer with live sync so that indexes are always up-to-date without manual re-indexing jobs.

**Why another one?** The live data synchronization is the core differentiator — most RAG frameworks treat indexing as a batch process. Pathway's streaming architecture means that when a document is added, deleted, or modified in Sharepoint or Google Drive, the index updates automatically. The 58,000+ stars and Docker-friendly deployment reflect production readiness rather than tutorial-grade implementations.

---

## 19. [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)
> Bash is all you need - A nano claude code-like agent harness, built from 0 to 1

**Language:** TypeScript  |  **Stars:** 37,344  |  **Forks:** 5,917  |  **Score:** 2,818  |  **Created:** 2025-06-29

**Background:** Learn Claude Code is an educational project by shareAI-lab that teaches agent harness engineering by building a minimal Claude Code-like system from scratch. The repository argues that "the model IS the agent" — drawing on the lineage from DeepMind DQN (2013) through AlphaStar (2019) to modern LLM agents — and that the surrounding code is merely a harness, not the agent itself. It provides a nano implementation to demonstrate how tool use, environment interaction, and agentic loops work at the most fundamental level.

**Problem it solves:** The AI agent ecosystem has become heavily framework-dependent, with developers using LangChain, CrewAI, or AutoGen without understanding the underlying mechanics. Learn Claude Code strips away all abstraction to show that an agent harness is fundamentally about connecting a model to tools via a loop — "bash is all you need" — providing the conceptual foundation that makes framework choices informed rather than cargo-culted.

**Why another one?** The philosophical framing is the differentiator: by tracing the lineage of AI agents from Atari DQN through Dota 2 to modern coding agents, the repository makes a case that understanding what an agent is (a trained model that acts) is more important than learning any specific framework. The 37,000+ stars suggest significant demand for this first-principles approach to agent engineering education.

---

## 20. [opencli](https://github.com/jackwener/opencli)
> Make Any Website & Tool Your CLI. A universal CLI Hub and AI-native runtime.

**Language:** TypeScript  |  **Stars:** 6,006  |  **Forks:** 487  |  **Score:** 2,804  |  **Created:** 2026-03-14

**Background:** OpenCLI is a TypeScript-based tool that turns any website, Electron app, or local binary into a standardized command-line interface. It supports 50+ sites across global and Chinese platforms (Bilibili, Zhihu, Xiaohongshu, Reddit, HackerNews, YouTube), plus desktop Electron apps via Chrome DevTools Protocol and AppleScript. It reuses Chrome's logged-in session for account safety, and provides AI agent integration via AGENT.md configuration and a `register` command for custom tools.

**Problem it solves:** AI agents need structured, reliable access to web services and desktop applications, but browser automation tools like Browser-Use and Stagehand are LLM-driven (expensive, non-deterministic). OpenCLI provides deterministic, zero-LLM-cost command-line access to websites and apps — same command, same output schema, every time — making it suitable for scripting, CI, and agent tool use at scale.

**Why another one?** The dual-engine architecture (YAML declarative pipelines plus TypeScript runtime injections) and the explicit "CLI-ify Electron apps" capability are unique. No other tool turns desktop Electron applications into CLI commands via CDP. The zero-LLM-cost, deterministic execution model positions it as infrastructure rather than another AI-powered browser agent.

---

## 21. [frontend-slides](https://github.com/zarazhangrui/frontend-slides)
> Create beautiful slides on the web using Claude's frontend skills

**Language:** CSS  |  **Stars:** 11,081  |  **Forks:** 818  |  **Score:** 2,772  |  **Created:** 2026-01-28

**Background:** Frontend Slides is a Claude Code skill by Zara Zhang Rui for creating animation-rich HTML presentations or converting PowerPoint files to web format. It produces single HTML files with inline CSS and JavaScript — zero dependencies, no build tools, no frameworks. The skill includes 12 curated visual styles (dark, light, and specialty themes like neon cyber and terminal green), a "show don't tell" approach with visual previews for style selection, and an anti-AI-slop design philosophy.

**Problem it solves:** Non-designers who need professional presentations face a choice between PowerPoint (limited web interactivity), web frameworks like reveal.js (require coding knowledge), or AI-generated slides (generic aesthetics). Frontend Slides lets non-technical users describe their content and desired feeling, then generates a complete, production-quality HTML presentation with animations and responsive design.

**Why another one?** The anti-AI-slop positioning is the key differentiator — the curated styles explicitly avoid generic AI aesthetics (no purple gradients on white). The zero-dependency output (single HTML file) makes the presentations universally shareable and hostable. The PPT conversion feature also bridges the gap for teams transitioning existing slide decks to web format.

---

## 22. [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
> The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**Language:** JavaScript  |  **Stars:** 102,648  |  **Forks:** 13,375  |  **Score:** 2,492  |  **Created:** 2026-01-18

**Background:** Everything Claude Code is a performance optimization system for AI agent harnesses, assembled by Affaan Mustafa, winner of an Anthropic hackathon, over 10+ months of intensive daily use building real products. It provides skills, instincts, memory optimization, continuous learning hooks, security scanning (AgentShield), and research-first development configurations across Claude Code, Codex, Cowork, and other agent harnesses. The project supports 7 languages (TypeScript, Python, Go, Java, Shell, Perl, Markdown) and has surpassed 102,000 stars.

**Problem it solves:** AI agent harnesses ship with minimal default configuration, and building effective agents, memory persistence, token optimization, and security scanning from scratch requires substantial trial-and-error. This repository short-circuits that process by providing battle-tested configurations that encode lessons about token budgeting, continuous learning from sessions, subagent orchestration, and verification loops.

**Why another one?** The repository keeps trending because the agent harness ecosystem is still maturing rapidly and there is no official reference for advanced configuration patterns. The hackathon winner provenance, 102k stars, and accompanying guides (shorthand, longform, and security) give it more credibility than generic dotfiles repos. The cross-harness compatibility (not just Claude Code) broadens its audience.

---

## 23. [next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io)
> A next.js web application that integrates AI capabilities with draw.io diagrams.

**Language:** TypeScript  |  **Stars:** 24,290  |  **Forks:** 2,559  |  **Score:** 2,444  |  **Created:** 2025-03-23

**Background:** Next AI Draw.io is a Next.js web application by Dayuan Jiang that integrates AI capabilities with draw.io diagrams, allowing users to create, modify, and enhance diagrams through natural language commands. It supports cloud architecture diagrams (GCP, AWS, Azure with vendor icons), animated connector diagrams, and general-purpose visualizations. The project offers a live demo, desktop applications, Docker deployment, and multi-provider support. A preview MCP server enables integration with Claude Code CLI.

**Problem it solves:** Creating technical diagrams (architecture diagrams, flowcharts, entity relationships) requires learning diagramming tools and manually placing and connecting elements. Next AI Draw.io lets users describe what they want in natural language and generates draw.io-compatible diagrams with proper icons, layouts, and connections.

**Why another one?** The draw.io integration is the differentiator — rather than generating static images, the output is an editable draw.io diagram that users can refine manually. The vendor-specific icon support (GCP, AWS, Azure) targets the architecture diagram use case that developers create frequently. The MCP server preview enables direct diagram generation from Claude Code sessions.

---

## 24. [autoresearch](https://github.com/karpathy/autoresearch)
> AI agents running research on single-GPU nanochat training automatically

**Language:** Python  |  **Stars:** 50,773  |  **Forks:** 7,078  |  **Score:** 2,334  |  **Created:** 2026-03-06

**Background:** Autoresearch is a project by Andrej Karpathy that gives an AI agent a small but real LLM training setup and lets it experiment autonomously overnight. The agent modifies training code (`train.py`), trains for a fixed 5-minute budget, checks if validation loss improved, keeps or discards the change, and repeats. The training setup is a simplified single-GPU implementation of nanochat, and the metric is validation bits per byte (val_bpb). The human's role is to program `program.md` — the Markdown instructions that set up the autonomous research organization — rather than touching Python files directly.

**Problem it solves:** ML research involves repetitive experimentation cycles: modify a hyperparameter, train, evaluate, repeat. Karpathy's approach automates this loop entirely — the AI agent runs the research overnight, trying architectural changes, optimizer modifications, and hyperparameter sweeps, producing a log of experiments and (hopefully) a better model by morning.

**Why another one?** The project comes from Karpathy, whose credibility in ML (former OpenAI, former Tesla AI) gives it unique authority. The philosophical framing — "one day, frontier AI research used to be done by meat computers" — and the deliberately minimal design (three files that matter) make it both a practical tool and a statement about the future of research. The `program.md`-as-research-org-code paradigm is a novel abstraction.

---

## 25. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster.

**Language:** Shell  |  **Stars:** 81,726  |  **Forks:** 6,816  |  **Score:** 2,252  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official agentic coding tool that lives in the terminal, understands codebases, and helps developers code faster through natural language commands. It handles routine tasks, explains complex code, manages git workflows, and can be used in the terminal, IDE, or via @claude tagging on GitHub. Installation is available via curl (macOS/Linux), Homebrew, PowerShell (Windows), WinGet, or npm (deprecated). The repository also includes plugins that extend functionality with custom commands and agents.

**Problem it solves:** Developers spend significant time on routine coding tasks — navigating unfamiliar codebases, writing boilerplate, debugging, managing git workflows — that interrupt higher-level thinking. Claude Code provides an always-available AI assistant that understands the full codebase context and can execute these tasks directly in the terminal workflow, without switching to a web interface or separate application.

**Why another one?** Claude Code is the first-party tool from Anthropic, meaning it receives model-specific optimizations and is the reference implementation for Claude's agentic capabilities. The 81,000+ stars and the ecosystem of third-party plugins, skills, and configurations (many of which appear elsewhere on this list) demonstrate its position as the de facto standard for Claude-based coding workflows.

---

> **Day's theme:** The dominant narrative across today's 25 repos is the maturation of the AI coding agent ecosystem — from foundational tools (Claude Code, Superpowers, gstack) through specialized skills (UI/UX design, GEO-SEO, presentation generation, diagram creation) to infrastructure layers (NVIDIA security sandboxing, enterprise coding agent frameworks, deterministic CLI bridges). The Claude Code skill economy is rapidly expanding, while autonomous AI research and multi-agent financial trading signal that agent-driven automation is extending well beyond software development into scientific experimentation and quantitative finance.
