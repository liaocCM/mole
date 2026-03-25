# Trendshift Report — 2026-03-18
**Total:** 25 repositories

---

## 1. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 108,363  |  **Forks:** 8,701  |  **Score:** 22,804  |  **Created:** 2025-10-09

**Background:** Superpowers is a comprehensive software development workflow framework for coding agents, created by Jesse Vincent. It provides composable skills that guide an AI agent through the full development lifecycle — from brainstorming and specification writing through implementation planning and subagent-driven development. Since launching in October 2025, it has surpassed 108,000 stars and become a cornerstone of the agentic coding ecosystem, with installations available across Claude Code, Cursor, Codex, OpenCode, and Gemini CLI.

**Problem it solves:** Coding agents without structured guidance tend to jump straight into writing code without fully understanding the problem, leading to rework, poor architecture, and scope drift. Superpowers enforces a deliberate workflow — spec review, plan generation, and task-by-task execution with automated review — so agents produce well-tested, well-designed code with minimal human babysitting. Its subagent-driven development process can sustain autonomous work for hours at a time.

**Why another one?** Superpowers pioneered the concept of a complete agent methodology rather than individual tools or prompts. While many repositories offer prompt collections or single-purpose skills, Superpowers provides a full workflow that activates automatically and chains skills together. Its 108,000-star count reflects market validation that a structured, opinionated development process for AI agents is more valuable than an ad hoc collection of tips.

---

## 2. [NemoClaw](https://github.com/NVIDIA/NemoClaw)
> Run OpenClaw more securely inside NVIDIA OpenShell with managed inference

**Language:** JavaScript  |  **Stars:** 16,028  |  **Forks:** 1,685  |  **Score:** 17,981  |  **Created:** 2026-03-15

**Background:** NVIDIA NemoClaw is an open-source reference stack released on March 15, 2026, that simplifies running OpenClaw always-on assistants inside sandboxed environments. It integrates the NVIDIA OpenShell runtime — part of the NVIDIA Agent Toolkit — along with open-source models like NVIDIA Nemotron, providing additional security layers for autonomous agents. Despite being in alpha, it accumulated over 16,000 stars in three days.

**Problem it solves:** Running autonomous agents with persistent system access raises serious security concerns — unrestricted file system access, network calls, and command execution create a large attack surface. NemoClaw wraps OpenClaw inside an OpenShell sandbox with managed inference, applying security policies that constrain what the agent can do while preserving its usefulness. This reduces the operational risk of leaving an always-on agent running unattended.

**Why another one?** NVIDIA's name gives NemoClaw immediate credibility in enterprise environments where security is non-negotiable. While OpenClaw itself is the dominant always-on assistant, there was no official reference stack for running it safely with hardware-accelerated inference. NemoClaw fills this gap with container runtime support across Linux, macOS, and Windows WSL, along with a guided onboarding wizard.

---

## 3. [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
> Master programming by recreating your favorite technologies from scratch.

**Language:** Markdown  |  **Stars:** 482,545  |  **Forks:** 45,406  |  **Score:** 17,142  |  **Created:** 2018-05-09

**Background:** Build Your Own X is one of the highest-starred repositories on GitHub, maintained by CodeCrafters. It is a curated compilation of step-by-step tutorials for recreating foundational technologies from scratch — 3D renderers, databases, operating systems, Docker, Git, neural networks, and dozens more. Originally created in May 2018, it has grown to nearly 483,000 stars and continues to trend regularly as new tutorials are added and rediscovered.

**Problem it solves:** Understanding how core technologies work at a deep level is difficult to achieve through API documentation or high-level overviews alone. This repository provides hands-on implementation guides that force the learner to confront every design decision — from byte-level protocol parsing to memory allocation — building genuine understanding that transfers to production debugging and architecture decisions.

**Why another one?** It keeps re-entering trending because the demand for first-principles engineering knowledge is perennial, and the repository is continuously updated with new topics like LLMs, diffusion models, and RAG. Recent additions of AI model tutorials align with the current wave of engineers wanting to understand the systems they use daily rather than treating them as black boxes.

---

## 4. [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)
> Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper.

**Language:** Python  |  **Stars:** 8,119  |  **Forks:** 865  |  **Score:** 13,647  |  **Created:** 2026-03-15

**Background:** AutoResearchClaw, developed by the Aiming Lab, is a fully autonomous research pipeline that takes a natural-language research idea and produces a complete academic paper without human intervention. It supports multiple stages — literature review, hypothesis generation, experiment design, code generation, execution, analysis, and paper writing. Version 0.3.1, released on this date, added OpenCode Beast Mode and community contributions, while v0.3.2 brought cross-platform support across multiple agent backends.

**Problem it solves:** Academic research involves repetitive scaffolding work — surveying related literature, setting up experiment code, running baselines, formatting results, and writing boilerplate sections. AutoResearchClaw automates the entire pipeline end-to-end, allowing researchers to focus on the creative aspects of hypothesis formation while the system handles execution. It includes an anti-fabrication system with verified registries and experiment diagnosis loops to prevent hallucinated results.

**Why another one?** Previous autonomous research tools focused on narrow subtasks — literature search or experiment execution alone. AutoResearchClaw spans the full pipeline from idea to formatted paper, and its OpenClaw integration allows researchers to trigger runs from messaging apps like Discord, Telegram, and Lark. The cross-platform agent backend support in v0.3.2 means it is not locked to a single AI coding tool.

---

## 5. [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)
> Open Multi-Agent Interactive Classroom — Get an immersive, multi-agent learning experience in just one click

**Language:** TypeScript  |  **Stars:** 11,788  |  **Forks:** 1,763  |  **Score:** 13,281  |  **Created:** 2026-03-11

**Background:** OpenMAIC is an open-source AI education platform from Tsinghua University's MAIC group, built with Next.js 16, React 19, and LangGraph. It generates interactive classroom experiences from any topic or document using multi-agent orchestration — AI teachers and AI classmates who can lecture, discuss, draw on a whiteboard, and speak via TTS. It reached nearly 12,000 stars in its first week and includes built-in OpenClaw integration for generating classrooms from messaging platforms.

**Problem it solves:** Traditional online courses are static and passive — pre-recorded lectures with no interaction. OpenMAIC creates a dynamic classroom environment where AI agents take on different roles (instructor, peer students), generate slides and quizzes on the fly, run interactive HTML simulations, and engage in real-time discussion. This turns any topic into a hands-on learning session rather than a one-way information transfer.

**Why another one?** AI tutoring tools typically provide a single chatbot interface. OpenMAIC differentiates by simulating an entire classroom with multiple agent personalities, rich media output (slides, whiteboard drawings, simulations), and exportable content (PPTX). The Tsinghua backing and published paper in JCST give it academic credibility, while the one-click Vercel deployment makes it immediately accessible.

---

## 6. [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
> 734+ structured cybersecurity skills for AI agents · MITRE ATT&CK mapped · agentskills.io open standard

**Language:** Python  |  **Stars:** 3,627  |  **Forks:** 360  |  **Score:** 9,553  |  **Created:** 2026-02-25

**Background:** Anthropic Cybersecurity Skills is the largest open-source collection of cybersecurity skills for AI agents, providing 753 production-grade skills across 26 security domains. Each skill follows the agentskills.io open standard with YAML frontmatter for discovery and structured Markdown for step-by-step execution. The entire collection is mapped to MITRE ATT&CK (all 14 Enterprise tactics, 200+ techniques) and aligned to NIST CSF 2.0, and is compatible with Claude Code, GitHub Copilot, Cursor, Gemini CLI, and other platforms.

**Problem it solves:** Security practitioners carry deep procedural knowledge — how to perform memory forensics, hunt for C2 beaconing, audit Kubernetes RBAC, reverse .NET malware — that is difficult to encode for AI agents. This repository packages that knowledge into structured, agent-executable skills so that AI assistants can perform sophisticated security tasks with the same rigor as experienced professionals, reducing the expertise barrier for security operations.

**Why another one?** Generic AI skills collections lack the depth and precision required for security work, where incorrect procedures can compromise systems or destroy evidence. This collection's MITRE ATT&CK mapping and NIST CSF 2.0 alignment give it a framework-level structure that security teams can audit and trust. The agentskills.io open standard ensures portability across agent platforms rather than locking users into a single tool.

---

## 7. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers.

**Language:** Shell  |  **Stars:** 60,953  |  **Forks:** 9,146  |  **Score:** 8,394  |  **Created:** 2025-10-13

**Background:** The Agency is a collection of meticulously crafted AI agent personalities organized by division — engineering, marketing, content, and more. Each agent has a unique voice, communication style, domain expertise, and deliverable-focused workflows. Born from a Reddit thread and months of iteration, it has grown to nearly 61,000 stars and supports Claude Code, Cursor, Aider, Windsurf, Gemini CLI, and Copilot through automated conversion scripts.

**Problem it solves:** Generic AI prompts produce generic results. By giving an AI agent a detailed personality, domain expertise, success metrics, and specific deliverable templates, the output quality improves dramatically. The Agency provides ready-to-use specialist profiles — frontend developer, backend architect, security engineer, rapid prototyper — that encode years of domain knowledge into immediately activatable agent configurations.

**Why another one?** Most prompt template collections offer flat, personality-free instructions. The Agency's multi-tool integration (with automated conversion scripts for six platforms), personality-driven approach, and division-based organization make it function more like hiring a team of specialists than downloading a prompt pack. Its continued trending reflects ongoing demand for structured, high-quality agent personas.

---

## 8. [skills](https://github.com/mattpocock/skills)
> My personal directory of skills, straight from my .claude directory.

**Language:** Shell  |  **Stars:** 9,379  |  **Forks:** 769  |  **Score:** 7,684  |  **Created:** 2026-02-03

**Background:** Matt Pocock, a well-known TypeScript educator, published his personal collection of Claude Code agent skills covering the full development lifecycle. The skills span planning and design (PRD writing, interface design, refactor planning), development (TDD, codebase architecture improvement, issue triage), tooling (pre-commit hooks, git guardrails), and writing (skill authoring, article editing, ubiquitous language extraction). All skills are installable via the `npx skills@latest add` command.

**Problem it solves:** Developers adopting AI agents often struggle to define effective workflows beyond "write code." Pocock's skills encode specific, opinionated methodologies — like turning a PRD into vertical slices, running red-green-refactor TDD loops, or getting relentlessly interviewed about a design until every ambiguity is resolved. They provide structure that prevents agents from taking shortcuts.

**Why another one?** The value lies in curation by a respected practitioner rather than crowd-sourced volume. Each skill reflects Pocock's actual development workflow, tested in real TypeScript projects. Skills like "grill-me" (relentless design interrogation) and "design-an-interface" (parallel sub-agent exploration) showcase novel agent interaction patterns that most skill collections lack.

---

## 9. [pathway](https://github.com/pathwaycom/pathway)
> Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

**Language:** Python  |  **Stars:** 62,169  |  **Forks:** 1,618  |  **Score:** 7,180  |  **Created:** 2022-11-27

**Background:** Pathway is a Python ETL framework powered by a scalable Rust engine based on Differential Dataflow. It handles both batch and streaming data with a unified API, allowing the same code to run in development, CI/CD, and production. Listed in the CNCF Landscape, it has grown to over 62,000 stars by addressing the growing demand for real-time data processing in LLM and RAG pipelines. It supports connectors for file systems, Google Drive, SharePoint, S3, Kafka, and PostgreSQL.

**Problem it solves:** Building real-time data pipelines typically requires choosing between batch-oriented tools (which have stale data) and stream-processing frameworks (which have steep learning curves and operational complexity). Pathway lets developers write Python code that works identically for batch and stream processing, with incremental computation handled by the Rust engine under the hood. This eliminates the need to maintain separate batch and streaming codepaths.

**Why another one?** Pathway's combination of a Python API with a Rust-powered incremental engine gives it both developer ergonomics and production-grade performance. Its specific optimizations for LLM pipelines and RAG — including built-in vector indexing, hybrid search, and real-time document syncing — position it uniquely at the intersection of data engineering and AI application development, a niche that general-purpose stream processors do not target.

---

## 10. [llm-app](https://github.com/pathwaycom/llm-app)
> Ready-to-run cloud templates for RAG, AI pipelines, and enterprise search with live data.

**Language:** Jupyter Notebook  |  **Stars:** 58,639  |  **Forks:** 1,392  |  **Score:** 7,002  |  **Created:** 2023-07-19

**Background:** Pathway AI Pipelines (llm-app) is a companion repository to the Pathway framework, providing production-ready application templates for RAG, AI-powered enterprise search, and document indexing. Templates range from basic question-answering RAG to multimodal pipelines, all built on Pathway's real-time data processing engine. The repository has accumulated over 58,000 stars since July 2023, offering both notebook and Docker deployment formats.

**Problem it solves:** Standing up a production RAG system requires connecting data sources, building indexing pipelines, handling incremental updates, and serving queries — each with its own complexity. These templates provide pre-built pipelines that connect to Google Drive, SharePoint, S3, Kafka, and PostgreSQL out of the box, with built-in vector, hybrid, and full-text search, scaling to millions of pages of documents.

**Why another one?** Most RAG tutorials demonstrate static document ingestion. Pathway's templates are designed for live data synchronization — when a document changes in the connected source, the index updates automatically without re-ingestion. This live-sync capability is critical for enterprise deployments where data freshness directly impacts answer quality, and it is the primary differentiator from static RAG template collections.

---

## 11. [gstack](https://github.com/garrytan/gstack)
> Use Garry Tan's exact Claude Code setup: 15 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**Language:** TypeScript  |  **Stars:** 39,705  |  **Forks:** 4,906  |  **Score:** 6,492  |  **Created:** 2026-03-11

**Background:** Gstack is Garry Tan's personal open-source software factory — a collection of 20 specialist roles and 8 power tools implemented as Claude Code slash commands. Tan, President & CEO of Y Combinator, built it to sustain a personal output of 10,000–20,000 lines of production code per day while running YC full-time. The repository launched on March 11, 2026, and reached nearly 40,000 stars in one week, fueled by Tan's public output metrics: 600,000+ lines in 60 days, 35% tests.

**Problem it solves:** A solo developer using AI agents lacks the review, QA, design critique, and release management that a full engineering team provides. Gstack recreates these roles as automated slash commands — `/plan-ceo-review` for product rethinking, `/review` for code review, `/qa` for browser-based QA, `/cso` for security audits, and `/ship` for release management. This gives a single builder the guardrails that normally require a team.

**Why another one?** Gstack's appeal is provenance — it is the exact tooling that the CEO of YC uses daily to ship production code, with public GitHub contribution graphs as evidence. While other skill collections are theoretical, Tan's 600K-line output demonstrates real-world effectiveness. The MIT license and opinionated design make it immediately usable rather than requiring assembly.

---

## 12. [deepagents](https://github.com/langchain-ai/deepagents)
> Agent harness built with LangChain and LangGraph. Equipped with a planning tool, a filesystem backend, and the ability to spawn subagents.

**Language:** Python  |  **Stars:** 17,096  |  **Forks:** 2,411  |  **Score:** 5,884  |  **Created:** 2025-07-27

**Background:** Deep Agents is LangChain's opinionated, batteries-included agent harness — a ready-to-run agent that ships with planning, filesystem tools, shell access, sub-agent delegation, smart prompts, and automatic context management including summarization for long conversations. It provides both a Python SDK (`create_deep_agent()`) and a CLI that functions as a terminal-based coding agent similar to Claude Code, powered by any LLM.

**Problem it solves:** Building a capable agent from LangChain primitives requires wiring up prompts, tools, context management, sub-agent orchestration, and output handling. Deep Agents provides all of this out of the box with sensible defaults, so developers get a working agent immediately and customize only what they need. The auto-summarization feature prevents context window overflow during long sessions.

**Why another one?** Deep Agents is LangChain's official answer to the growing demand for a complete agent runtime rather than a component library. Its CLI positions it as an open, model-agnostic alternative to Claude Code and Cursor, while the SDK allows embedding the same agent capabilities into custom applications. MCP support via langchain-mcp-adapters gives it access to the expanding tool ecosystem.

---

## 13. [context-hub](https://github.com/andrewyng/context-hub)
> Curated, versioned docs for coding agents that get smarter with every task.

**Language:** JavaScript  |  **Stars:** 11,819  |  **Forks:** 1,038  |  **Score:** 5,687  |  **Created:** 2025-10-30

**Background:** Context Hub, created by Andrew Ng, is a CLI tool and open content repository that provides curated, versioned API documentation to coding agents. Instead of searching the web and encountering noisy, outdated results, agents fetch precise documentation via `chub get openai/chat --lang py` and can annotate docs locally for future sessions. All content is maintained as open Markdown in the repository, making it inspectable and community-contributable.

**Problem it solves:** Coding agents hallucinate API signatures and forget workarounds between sessions. Context Hub addresses both problems: curated docs reduce hallucination by providing accurate reference material, and persistent local annotations allow agents to accumulate knowledge across sessions. The feedback mechanism (upvote/downvote) flows back to doc authors, creating a continuous improvement loop.

**Why another one?** Web search is noisy and unversioned — agents cannot distinguish outdated Stack Overflow answers from current API docs. Context Hub provides a structured, language-specific documentation layer purpose-built for agent consumption, with incremental fetch to minimize token usage. Andrew Ng's involvement gives it credibility and community momentum that other doc-serving tools lack.

---

## 14. [gofr](https://github.com/gofr-dev/gofr)
> An opinionated GoLang framework for accelerated microservice development. Built in support for databases and observability.

**Language:** Go  |  **Stars:** 19,813  |  **Forks:** 1,748  |  **Score:** 5,277  |  **Created:** 2023-10-24

**Background:** GoFr is an opinionated Go microservice framework listed in the CNCF Landscape, designed to simplify Kubernetes deployment and provide out-of-the-box observability. It bundles REST standards, configuration management, logging/tracing/metrics, auth middleware, gRPC support, pub/sub, health checks, database migrations, cron jobs, websockets, and Swagger rendering into a single cohesive framework. Since October 2023, it has grown to nearly 20,000 stars.

**Problem it solves:** Building production-ready microservices in Go typically involves assembling a dozen separate libraries for routing, middleware, database access, observability, and configuration, then writing glue code to make them work together. GoFr provides all of these as built-in features with a simple API surface, reducing the boilerplate required to go from a new project to a deployable, observable service.

**Why another one?** Go's standard library and minimal frameworks like Chi and Gin provide routing but leave observability, database integration, and operational concerns to the developer. GoFr's opinionated approach — choosing sensible defaults for everything from log format to health check endpoints — targets teams that value convention over configuration and want Kubernetes-native behavior without writing Helm charts for every integration.

---

## 15. [taste-skill](https://github.com/Leonxlnx/taste-skill)
> Taste-Skill (High-Agency Frontend) - gives your AI good taste. Stops the AI from generating boring, generic, "slop"

**Language:** N/A  |  **Stars:** 5,385  |  **Forks:** 497  |  **Score:** 5,010  |  **Created:** 2026-02-19

**Background:** Taste Skill is a collection of agent skills that improve how AI tools generate frontend code, replacing generic interfaces with modern, premium designs featuring proper animations, spacing, and visual quality. It includes seven skills — the main taste-skill, a redesign-skill for upgrading existing projects, a soft-skill for luxury aesthetics, a minimalist-skill inspired by Notion and Linear, a brutalist-skill, and an output-skill that prevents lazy code generation. It is compatible with Cursor, Claude Code, Antigravity, and other agent platforms.

**Problem it solves:** AI-generated frontend code tends toward bland, template-like interfaces — centered layouts, default spacing, no animation, and generic color schemes. Taste Skill encodes specific design principles (layout variance, motion intensity, visual density) as configurable parameters, so the AI produces interfaces that look intentionally designed rather than auto-generated.

**Why another one?** Most AI coding skills focus on logic and architecture. Taste Skill targets the aesthetic gap — the visual quality difference between AI-generated and designer-crafted interfaces. Its configurable settings (1–10 scales for variance, motion, and density) give developers fine-grained control over the design output, and the separate skills for different aesthetics (soft, minimalist, brutalist) show a depth of design thinking absent from generic UI prompts.

---

## 16. [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
> An AI SKILL that provides design intelligence for building professional UI/UX across multiple platforms

**Language:** Python  |  **Stars:** 49,030  |  **Forks:** 4,747  |  **Score:** 4,915  |  **Created:** 2025-11-30

**Background:** UI UX Pro Max is a design intelligence skill for AI agents, featuring 161 reasoning rules and 67 UI styles. Version 2.0 introduced an AI-powered Design System Generator that analyzes project requirements and produces a complete, tailored design system — including layout patterns, color palettes, typography, and component specifications. The project has reached 49,000 stars since November 2025 and offers an npm CLI for installation alongside the Python-based core.

**Problem it solves:** AI agents can generate functional UIs but lack the design reasoning that professional designers apply — understanding conversion patterns, choosing appropriate visual hierarchy, matching design language to brand identity. This skill injects design intelligence into the agent's reasoning process, so it produces UIs informed by professional design principles rather than generic component assembly.

**Why another one?** At 49,000 stars, UI UX Pro Max has become the de facto design skill in the agentic ecosystem. Its combination of reasoning rules (not just visual templates) and automated design system generation differentiates it from simpler CSS or component-focused tools. The v2.0 Design System Generator produces a complete system in seconds, eliminating the manual process of defining tokens, components, and patterns.

---

## 17. [Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders)
> Practical marketing resources to get the first 10 / 100 / 1000 users for your SaaS / App / Startup

**Language:** N/A  |  **Stars:** 5,850  |  **Forks:** 553  |  **Score:** 4,906  |  **Created:** 2025-05-19

**Background:** Marketing for Founders is a curated collection of practical marketing resources organized by channel — launch platforms, Product Hunt strategy, social media, cold outreach, SEO, LLM SEO, Reddit marketing, email, content marketing, ads, influencer marketing, affiliates, landing pages, pricing, conversion optimization, idea validation, and user research. It was created by Edo Stradella and has grown to 5,850 stars by focusing exclusively on early-stage acquisition tactics.

**Problem it solves:** Most marketing advice targets funded startups with budgets and existing user bases. Bootstrapped founders and solo builders need actionable tactics for acquiring their first 10 to 1,000 users with zero budget. This repository organizes free and low-cost acquisition channels with specific platform recommendations, submission links, and tactical guidance rather than high-level strategy.

**Why another one?** Its recurring trend appearances coincide with the wave of solo builders and vibe-coders shipping products with AI assistance — developers who can build quickly but lack marketing knowledge. The LLM SEO section (AEO, GEO) is particularly timely as AI-generated search results become a primary discovery channel, and few marketing resources address this emerging channel.

---

## 18. [unsloth](https://github.com/unslothai/unsloth)
> Unsloth Studio is a web UI for training and running open models like Qwen, DeepSeek, gpt-oss and Gemma locally.

**Language:** Python  |  **Stars:** 57,675  |  **Forks:** 4,860  |  **Score:** 4,696  |  **Created:** 2023-11-29

**Background:** Unsloth Studio is a local inference and training platform with a web UI, supporting text, audio, embedding, and vision models on Windows, Linux, and macOS. It provides training up to 2x faster with 70% less VRAM through custom Triton kernels, along with reinforcement learning support using 80% less VRAM for GRPO. The team works directly with model providers including gpt-oss, Qwen3, Llama 4, Mistral, Gemma, and Phi-4 to fix bugs and improve accuracy.

**Problem it solves:** Running and fine-tuning open models locally requires navigating fragmented tooling — separate inference servers, training scripts, GGUF conversion tools, and RL pipelines. Unsloth Studio unifies all of these behind a single web UI with automated parameter tuning, data recipe generation from PDFs and CSVs, self-healing tool calling, and code execution in sandbox environments.

**Why another one?** Unsloth's VRAM efficiency is its primary moat — 2x faster training and 70% less memory usage means models that require an A100 on other platforms can train on consumer GPUs. Direct collaboration with model providers means Unsloth often ships fixes and optimizations before they reach the upstream model repositories, making it the fastest path to running cutting-edge open models.

---

## 19. [Crucix](https://github.com/calesthio/Crucix)
> Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

**Language:** JavaScript  |  **Stars:** 6,567  |  **Forks:** 1,003  |  **Score:** 4,622  |  **Created:** 2026-03-14

**Background:** Crucix is a self-hosted OSINT intelligence terminal that aggregates 27 open-source intelligence feeds — satellite fire detection, flight tracking, radiation monitoring, economic indicators, live market prices, conflict data, sanctions lists, and social sentiment — into a single Jarvis-style dashboard. It runs with zero cloud dependencies (just `node server.mjs`) and updates every 15 minutes. When connected to an LLM, it becomes a two-way intelligence assistant pushing multi-tier alerts to Telegram and Discord.

**Problem it solves:** Real-time intelligence data is publicly available but scattered across dozens of government APIs, research institutions, and open data feeds. Checking them individually is impractical. Crucix aggregates and cross-correlates these feeds on a single dashboard, providing researchers, journalists, traders, and OSINT analysts with a unified situational awareness view without enterprise subscriptions or security clearances.

**Why another one?** Commercial OSINT platforms are expensive and cloud-dependent. Crucix runs entirely locally with a single dependency (Express), no telemetry, and no subscriptions. Its LLM integration enables natural-language commands (`/brief`, `/sweep`) and automated trade idea generation grounded in cross-domain data — turning passive monitoring into active intelligence that alerts you while you sleep.

---

## 20. [claude-hud](https://github.com/jarrodwatts/claude-hud)
> A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress

**Language:** JavaScript  |  **Stars:** 12,154  |  **Forks:** 505  |  **Score:** 4,142  |  **Created:** 2026-01-02

**Background:** Claude HUD is a Claude Code plugin that provides real-time visibility into session state — context window usage, tool activity, running sub-agents, git branch, and todo progress — displayed as a persistent statusline below the input prompt. It uses Claude Code's native statusline API, requires no separate window or tmux, and updates every 300ms. The plugin has grown to over 12,000 stars since January 2026.

**Problem it solves:** Claude Code sessions can consume context rapidly during complex tasks, and there is no built-in indication of how much context remains, which tools are running, or whether sub-agents have stalled. Claude HUD surfaces this information in a compact, always-visible display, allowing developers to intervene before context exhaustion forces a session restart and to monitor autonomous agent activity.

**Why another one?** Claude HUD leverages the native statusline API for zero-overhead integration rather than parsing logs or running a separate monitoring process. Its configurable layout (Full/Essential/Minimal presets), color-coded context health bar (green to yellow to red), and 1M-context session support make it specifically optimized for the Claude Code ecosystem rather than being a generic terminal monitoring tool.

---

## 21. [MiroFish](https://github.com/666ghj/MiroFish)
> A Simple and Universal Swarm Intelligence Engine, Predicting Anything.

**Language:** Python  |  **Stars:** 40,933  |  **Forks:** 5,565  |  **Score:** 3,456  |  **Created:** 2025-11-26

**Background:** MiroFish is a multi-agent prediction engine backed by Shanda Group that constructs high-fidelity parallel digital worlds from real-world seed information — breaking news, policy drafts, financial signals. Within these simulated environments, thousands of agents with independent personalities, long-term memory, and behavioral logic interact and evolve. Users can inject variables from a "God's view" perspective to simulate future outcomes, from public opinion dynamics to lost novel endings.

**Problem it solves:** Traditional prediction models operate on statistical patterns without modeling the emergent behaviors that arise from individual interactions. MiroFish simulates the social dynamics — opinion formation, influence cascading, behavioral adaptation — that drive real-world outcomes. By providing a full digital sandbox rather than a point estimate, it allows decision-makers to explore multiple scenarios and observe how interventions propagate through a simulated population.

**Why another one?** MiroFish occupies a unique niche between agent-based modeling tools (typically academic and narrow) and simple prediction APIs (which output numbers without explanatory dynamics). Its emphasis on interactive exploration — where users can converse with individual simulated agents and inject real-time variables — makes it useful for both serious forecasting (policy, finance) and creative applications (exploring fictional storylines).

---

## 22. [ground-station](https://github.com/sgoudelis/ground-station)
> Ground Station is all-in-one satellite monitoring suite

**Language:** JavaScript  |  **Stars:** 3,166  |  **Forks:** 552  |  **Score:** 3,346  |  **Created:** 2025-03-01

**Background:** Ground Station is an open-source, full-featured satellite tracking and radio communication platform designed for amateur radio operators, satellite enthusiasts, and researchers. It provides real-time tracking of hundreds of satellites with automatic TLE updates from CelesTrak and SatNOGS, automated antenna rotator control, rig control via Hamlib, SDR waterfall visualization with live transcription, GMSK packet decoding, telemetry viewing, and automated observation scheduling. The project was built with the help of Claude Code and Codex.

**Problem it solves:** Amateur satellite communication requires juggling multiple specialized tools — satellite trackers, SDR software, rotator controllers, and packet decoders — each with different interfaces and data formats. Ground Station consolidates all of these into a single web-based application with a unified interface, reducing the setup complexity that deters newcomers from entering the hobby.

**Why another one?** Existing satellite tracking software is typically either commercial, desktop-only, or focused on a single aspect (tracking or decoding, not both). Ground Station's all-in-one web interface, support for multiple SDR hardware types (RTL-SDR, SoapySDR, UHD/USRP), and DSP topology visualization set it apart. Its construction using AI coding tools also makes it a notable example of complex domain software built with agentic assistance.

---

## 23. [claude-mem](https://github.com/thedotmack/claude-mem)
> A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI, and injects relevant context back into future sessions.

**Language:** TypeScript  |  **Stars:** 39,927  |  **Forks:** 2,937  |  **Score:** 3,305  |  **Created:** 2025-08-31

**Background:** Claude-Mem is a persistent memory compression system for Claude Code that automatically captures session activity, compresses it using Claude's agent SDK, and injects relevant context back into future sessions. Now at version 6.5.0 and nearly 40,000 stars, it has become one of the most widely adopted Claude Code plugins. The project is translated into over 25 languages and maintains active community engagement.

**Problem it solves:** Claude Code sessions lose all context when they end — decisions made, bugs discovered, architectural patterns established, and project conventions learned all vanish. Claude-Mem addresses this by building a compressed knowledge base from session transcripts that is automatically surfaced in future sessions, giving the agent continuity across interactions without manual context re-injection.

**Why another one?** While CLAUDE.md and project notes provide static context, Claude-Mem captures dynamic session knowledge — the specific bugs encountered, the solutions that worked, the patterns Claude discovered while exploring the codebase. Its AI-powered compression ensures the memory stays compact enough to inject without consuming excessive context window space, a balance that simple transcript storage cannot achieve.

---

## 24. [Mole](https://github.com/tw93/Mole)
> Deep clean and optimize your Mac.

**Language:** Shell  |  **Stars:** 43,618  |  **Forks:** 1,269  |  **Score:** 3,233  |  **Created:** 2025-09-23

**Background:** Mole is an all-in-one Mac system maintenance tool that combines the functionality of CleanMyMac, AppCleaner, DaisyDisk, and iStat Menus in a single binary. Created by Tw93 and available via Homebrew, it provides deep cleaning (caches, logs, browser leftovers), smart app uninstallation (including hidden remnants and launch agents), disk analysis with large file detection, build artifact purging, and live system monitoring for CPU, GPU, memory, disk, and network. It has reached 43,618 stars since September 2025.

**Problem it solves:** Mac users typically need four or five separate paid applications to clean caches, uninstall apps completely, analyze disk usage, and monitor system performance. Mole consolidates all of these into a single free CLI tool with safety-first defaults — path validation, protected directories, dry-run previews, and Trash-based deletion for the disk analyzer — reducing both cost and the risk of accidental data loss.

**Why another one?** Mole replaces multiple commercial macOS utilities (each $30–50) with a single MIT-licensed binary installable via Homebrew. Its safety-first design — conservative cleanup boundaries, explicit confirmation for destructive actions, and whitelist management — addresses the trust deficit that prevents power users from adopting automated cleanup tools. The experimental Windows branch signals cross-platform ambitions.

---

## 25. [code-review-graph](https://github.com/tirth8205/code-review-graph)
> Local knowledge graph for Claude Code. Builds a persistent map of your codebase so Claude reads only what matters — 6.8x fewer tokens on reviews and up to 49x on daily coding tasks.

**Language:** Python  |  **Stars:** 3,330  |  **Forks:** 299  |  **Score:** 3,232  |  **Created:** 2026-02-26

**Background:** Code-review-graph is a Claude Code plugin that builds a structural map of a codebase using Tree-sitter, storing it as a graph of functions, classes, imports, and their relationships (calls, inheritance, test coverage) in SQLite. When code changes, it computes the blast radius — every caller, dependent, and test affected — so Claude reads only the minimal set of files needed for a review. It supports 14 languages and re-indexes a 2,900-file project in under 2 seconds.

**Problem it solves:** Claude Code re-reads the entire codebase on every task, consuming tokens on irrelevant files and missing distant dependencies. Code-review-graph replaces this brute-force approach with targeted context — a 6.8x token reduction on code reviews and up to 49x on daily coding tasks. The incremental update mechanism ensures the graph stays current with every git commit without requiring a full rebuild.

**Why another one?** Generic code indexing tools provide file-level search but lack structural understanding. Code-review-graph's Tree-sitter-based AST parsing captures function-level relationships, enabling blast-radius analysis that understands which tests cover which functions and which callers depend on a changed interface. This semantic precision is the difference between reading 5 relevant files and scanning 500 irrelevant ones.

---

> **Day's theme:** The agentic skills ecosystem matured rapidly on March 18, 2026, with specialized toolkits for development workflows, cybersecurity, design intelligence, and persistent memory dominating alongside infrastructure projects for agent security, real-time data processing, and local AI model training.