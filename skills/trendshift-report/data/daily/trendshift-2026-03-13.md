# Trendshift Report — 2026-03-13
**Total:** 25 repositories

---

## 1. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers.

**Language:** Shell  |  **Stars:** 46,473  |  **Forks:** 6,940  |  **Score:** 23,393  |  **Created:** 2025-10-13

**Background:** Agency Agents by Mark Sitarzewski is a collection of meticulously crafted AI agent personas for professional roles, distributed as shell scripts and prompt configurations. Originally born from a Reddit thread, the project has grown to 46,000+ stars by providing specialized agents with defined personalities, workflows, and deliverables for roles ranging from frontend development to community management.

**Problem it solves:** Teams adopting AI coding agents need role-specific system prompts and workflow definitions tailored to each professional function. Agency Agents provides production-ready agent personas that eliminate the prompt engineering overhead of defining new specialist roles from scratch.

**Why another one?** Unlike generic prompt template collections, each agent here has a distinct personality, communication style, and measurable success metrics. The personality-driven approach makes agents more memorable and shareable, while the battle-tested workflows and deliverable templates ground the personas in practical utility.

---

## 2. [CLI-Anything](https://github.com/HKUDS/CLI-Anything)
> CLI-Anything: Making ALL Software Agent-Native

**Language:** Python  |  **Stars:** 16,206  |  **Forks:** 1,374  |  **Score:** 17,903  |  **Created:** 2026-03-08

**Background:** CLI-Anything is a tool from HKUDS (Hong Kong University Data Science lab) that wraps any desktop application with a command-line interface, making GUI-only software accessible to AI agents. Released just five days ago, it has already amassed over 16,000 stars, signaling massive demand for bridging the gap between human-facing software and agent-driven workflows.

**Problem it solves:** Most existing software was designed for human interaction through graphical interfaces. AI agents like Claude Code, Cursor, and OpenClaw cannot operate GUI applications directly. CLI-Anything generates CLI wrappers with one command, producing JSON and human-readable output that agents can consume programmatically.

**Why another one?** Rather than building agent-specific integrations for each application, CLI-Anything takes a universal approach: any software gets a CLI in minutes. It supports 13+ demonstrated applications with 1,588 passing tests, and its MIT-licensed Python implementation keeps the barrier to entry low.

---

## 3. [BitNet](https://github.com/microsoft/BitNet)
> Official inference framework for 1-bit LLMs

**Language:** Python  |  **Stars:** 34,674  |  **Forks:** 2,937  |  **Score:** 11,750  |  **Created:** 2024-08-05

**Background:** BitNet is Microsoft's official inference framework for 1-bit large language models (specifically BitNet b1.58). The project provides optimized kernels for fast, lossless inference of 1.58-bit models on both CPU and GPU, with a companion 2B-parameter model available on Hugging Face and a live demo for immediate testing.

**Problem it solves:** Running large language models typically requires expensive GPU hardware due to their memory and compute demands. BitNet's 1-bit quantization reduces model weights to ternary values (-1, 0, 1), enabling LLM inference on commodity CPUs while maintaining quality comparable to full-precision models.

**Why another one?** BitNet is not a post-training quantization hack but a native 1-bit architecture with dedicated inference kernels. The official Microsoft backing, a public demo, and support for both CPU and GPU execution paths make it the reference implementation for an emerging class of extreme-efficiency LLMs.

---

## 4. [pua](https://github.com/tanweai/pua)
> A high-motivation skill for AI agents. Double your Codex / Claude Code productivity and output.

**Language:** HTML  |  **Stars:** 7,879  |  **Forks:** 373  |  **Score:** 11,718  |  **Created:** 2026-03-08

**Background:** PUA is a satirical-yet-functional skill that applies performance improvement plan (PIP) pressure to AI coding agents. The project frames the AI as a P8-level engineer placed on a 30-day PIP by Anthropic, using motivational pressure techniques to push the agent toward higher output and more thorough work. It supports Claude Code, OpenAI Codex CLI, Cursor, and other agent platforms.

**Problem it solves:** AI coding agents often produce lazy or incomplete outputs, stopping short of thorough implementations. PUA applies social pressure dynamics to the agent's system prompt, reportedly doubling productivity by making the AI treat every task as if its job depends on it.

**Why another one?** The tongue-in-cheek framing — an AI on a PIP — has made it a viral sensation in Chinese and English developer communities simultaneously. It taps into a genuine frustration with agent laziness while packaging the solution as entertainment, driving organic sharing across WeChat, Telegram, and Discord.

---

## 5. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 85,570  |  **Forks:** 6,721  |  **Score:** 10,625  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent is a complete software development workflow for coding agents, built on composable skills that trigger automatically. With over 85,000 stars, it has become one of the most adopted agentic development frameworks. The system enforces a structured process: spec elicitation, chunked design review, implementation planning, and subagent-driven development with TDD and YAGNI principles.

**Problem it solves:** Without guidance, AI coding agents jump straight to writing code without understanding requirements, skip testing, and produce sprawling implementations. Superpowers imposes a disciplined engineering methodology — from spec to plan to test-driven implementation — that enables hours of autonomous agent work without deviation.

**Why another one?** Superpowers is not just a prompt collection but a complete development methodology with automated skill triggering. Its subagent-driven development process, where agents work through tasks while being inspected and reviewed, represents a more structured approach than competitors that simply enhance individual prompts.

---

## 6. [AstrBot](https://github.com/AstrBotDevs/AstrBot)
> Agentic IM Chatbot infrastructure that integrates lots of IM platforms, LLMs, plugins and AI features.

**Language:** Python  |  **Stars:** 25,271  |  **Forks:** 1,723  |  **Score:** 9,889  |  **Created:** 2022-12-08

**Background:** AstrBot is an agentic instant messaging chatbot infrastructure project that has grown steadily since its 2022 inception. It provides a unified platform for deploying AI chatbots across multiple IM platforms with support for various LLM backends, a plugin system, and built-in AI capabilities. Documentation is available in Chinese, English, Japanese, French, and Russian.

**Problem it solves:** Deploying AI chatbots across different messaging platforms (WeChat, Telegram, Discord, QQ) requires separate integrations and boilerplate for each. AstrBot provides a single infrastructure layer that handles multi-platform messaging, LLM routing, and plugin management in one deployable package.

**Why another one?** AstrBot's longevity since 2022 gives it a maturity advantage over newer chatbot frameworks. Its plugin ecosystem and multi-language documentation indicate an established international community, and its positioning as an OpenClaw alternative broadens its appeal to users seeking self-hosted IM automation.

---

## 7. [public-apis](https://github.com/public-apis/public-apis)
> A collective list of free APIs

**Language:** Python  |  **Stars:** 411,142  |  **Forks:** 44,435  |  **Score:** 8,127  |  **Created:** 2016-03-20

**Background:** Public APIs is one of the most-starred repositories on GitHub, a community-curated directory of free APIs organized by category. Maintained since 2016, it has become the default starting point for developers searching for third-party API integrations, spanning domains from finance to weather to entertainment.

**Problem it solves:** Discovering reliable, free APIs for side projects and production applications requires scattered searches across documentation sites, blog posts, and forums. Public APIs consolidates thousands of entries with descriptions, authentication requirements, and HTTPS/CORS support indicators in one browsable list.

**Why another one?** At 411,000+ stars, public-apis is effectively the canonical resource in its category. Its continued trending reflects persistent utility rather than novelty — developers building AI agents and applications regularly return to discover new integration endpoints. The community-maintained nature keeps it current as APIs launch and deprecate.

---

## 8. [promptfoo](https://github.com/promptfoo/promptfoo)
> Test your prompts, agents, and RAGs. Red teaming and vulnerability scanning for AI.

**Language:** TypeScript  |  **Stars:** 16,834  |  **Forks:** 1,458  |  **Score:** 5,401  |  **Created:** 2023-04-28

**Background:** Promptfoo is an open-source LLM evaluation and red teaming platform that enables developers to test prompts, agents, and RAG pipelines. It supports comparing performance across GPT, Claude, Gemini, Llama, and other models using declarative YAML configurations, with CLI and CI/CD integration for automated testing pipelines.

**Problem it solves:** LLM-powered applications are notoriously difficult to test — outputs are non-deterministic, regressions are subtle, and security vulnerabilities are hard to enumerate. Promptfoo provides systematic evaluation, red teaming, and pentesting capabilities that treat LLM testing with the same rigor as traditional software testing.

**Why another one?** Promptfoo distinguishes itself with its declarative config approach and CI/CD-native design. Rather than requiring custom Python scripts for each evaluation, developers define test cases in YAML and run them across multiple models simultaneously, making it practical to integrate LLM quality gates into existing deployment pipelines.

---

## 9. [openrag](https://github.com/langflow-ai/openrag)
> OpenRAG is a comprehensive, single package Retrieval-Augmented Generation platform built on Langflow, Docling, and OpenSearch.

**Language:** Python  |  **Stars:** 2,975  |  **Forks:** 269  |  **Score:** 5,292  |  **Created:** 2025-07-11

**Background:** OpenRAG is a RAG platform from the Langflow team that bundles document ingestion, semantic search, and AI-powered chat into a single deployable package. Built on FastAPI and Next.js, it uses Langflow for workflow orchestration, Docling for document processing, and OpenSearch as the vector and keyword search backend.

**Problem it solves:** Setting up a production RAG system typically requires stitching together separate document processing, vector database, retrieval, and chat components. OpenRAG ships all of these as one integrated platform with a chat interface, intelligent nudges, and documentation-ready out of the box.

**Why another one?** OpenRAG's single-package design eliminates the integration tax of assembling RAG from individual components. Its Langflow foundation means users can visually inspect and modify retrieval workflows, while the OpenSearch backend provides enterprise-grade search capabilities beyond what simpler vector stores offer.

---

## 10. [LuxTTS](https://github.com/ysharma3501/LuxTTS)
> A high-quality rapid TTS voice cloning model that reaches speeds of 150x realtime.

**Language:** Python  |  **Stars:** 2,065  |  **Forks:** 257  |  **Score:** 5,054  |  **Created:** 2026-01-23

**Background:** LuxTTS is a lightweight text-to-speech model based on the ZipVoice architecture, designed for high-quality voice cloning at extreme speeds. It generates clear 48kHz speech at 150x realtime on GPU and faster than realtime on CPU, while fitting within 1GB of VRAM. Models and demos are available on Hugging Face.

**Problem it solves:** Most high-quality TTS models require significant GPU resources and run at modest speeds, making them impractical for real-time or cost-sensitive applications. LuxTTS delivers voice cloning quality on par with models 10x its size while running on hardware as modest as a laptop CPU.

**Why another one?** The combination of 150x realtime speed, 48kHz output clarity (versus the 24kHz ceiling of most competitors), and a sub-1GB VRAM footprint creates a unique position in the TTS landscape. It makes production-quality voice cloning feasible on edge devices and low-cost cloud instances.

---

## 11. [OpenViking](https://github.com/volcengine/OpenViking)
> OpenViking is an open-source context database designed specifically for AI Agents.

**Language:** Python  |  **Stars:** 12,376  |  **Forks:** 847  |  **Score:** 4,779  |  **Created:** 2026-01-05

**Background:** OpenViking from ByteDance's Volcengine division is a context database purpose-built for AI agents. It unifies the management of agent context — memory, resources, and skills — through a file system paradigm, enabling hierarchical context delivery and self-evolving knowledge structures. The project addresses challenges specific to long-running agent tasks.

**Problem it solves:** Agent developers face fragmented context management: memories live in code, resources sit in vector databases, and skills are scattered across files. OpenViking provides a unified context layer with hierarchical organization, preventing the information loss that occurs when traditional RAG systems truncate or compress context.

**Why another one?** OpenViking's file system metaphor for context management is a distinctive architectural choice — developers interact with agent context using familiar directory and file operations rather than learning a new query language. Its focus on observability addresses the "black box retrieval" problem that plagues traditional RAG pipelines.

---

## 12. [InsForge](https://github.com/InsForge/InsForge)
> Give agents everything they need to ship fullstack apps. The backend built for agentic development.

**Language:** TypeScript  |  **Stars:** 4,600  |  **Forks:** 474  |  **Score:** 4,500  |  **Created:** 2025-07-29

**Background:** InsForge is a backend platform designed specifically for AI agents building fullstack applications. It provides infrastructure services — databases, authentication, storage, and deployment — packaged for consumption by coding agents via MCP (Model Context Protocol) rather than human-operated dashboards. Setup is Docker-based with a one-command local deployment.

**Problem it solves:** Coding agents can write application code but struggle with backend infrastructure provisioning, which typically requires navigating cloud dashboards and configuration UIs. InsForge exposes backend services through agent-friendly interfaces, letting agents autonomously provision and manage infrastructure as part of their development workflow.

**Why another one?** InsForge targets the specific gap between "agent writes code" and "agent ships a working app." While platforms like Supabase and Firebase serve human developers, InsForge's MCP integration and agent-first API design make it purpose-built for the emerging agentic development workflow where the AI handles end-to-end delivery.

---

## 13. [MiroFish](https://github.com/666ghj/MiroFish)
> A Simple and Universal Swarm Intelligence Engine, Predicting Anything.

**Language:** Python  |  **Stars:** 26,759  |  **Forks:** 3,202  |  **Score:** 4,275  |  **Created:** 2025-11-26

**Background:** MiroFish by Shanda Group is a multi-agent prediction engine that constructs high-fidelity parallel digital worlds from seed information such as breaking news, policy drafts, and financial signals. Within these simulated environments, thousands of agents with independent personalities, long-term memory, and behavioral logic interact and evolve, allowing users to observe future scenarios from a "God's eye view."

**Problem it solves:** Traditional prediction systems rely on monolithic models that are expensive to retrain and brittle to distribution shifts. MiroFish distributes prediction across a swarm of autonomous agents, each processing different signals and simulating social dynamics, then aggregating their outputs for more robust forecasting.

**Why another one?** The swarm intelligence paradigm — inspired by collective animal behavior — offers a genuinely different approach from transformer-based forecasting. Users can dynamically inject variables into the simulation and observe cascading effects in real time, making it a tool for scenario planning rather than point prediction.

---

## 14. [impeccable](https://github.com/pbakaus/impeccable)
> The design language that makes your AI harness better at design.

**Language:** JavaScript  |  **Stars:** 8,712  |  **Forks:** 343  |  **Score:** 3,918  |  **Created:** 2025-11-16

**Background:** Impeccable by Paul Bakaus builds on Anthropic's frontend-design skill to provide deeper design expertise for AI coding agents. It ships one comprehensive skill with 7 domain-specific reference files (typography, color, spatial design, motion, interaction, responsive design, and UX writing), 20 steering commands, and curated anti-patterns that explicitly tell the AI what not to do.

**Problem it solves:** Every LLM learned from the same generic templates, producing predictable design mistakes: Inter font, purple gradients, cards nested in cards, gray text on colored backgrounds. Impeccable provides the domain expertise and explicit constraints needed to break AI agents out of these default patterns.

**Why another one?** While Anthropic's original frontend-design skill provides a foundation, Impeccable adds substantially deeper coverage across seven design domains plus 20 actionable commands (audit, review, polish, animate, etc.). The anti-pattern approach — telling the AI what not to do — is particularly effective at correcting the systematic biases in LLM-generated UI.

---

## 15. [openui](https://github.com/thesysdev/openui)
> The Open Standard for Generative UI

**Language:** TypeScript  |  **Stars:** 1,753  |  **Forks:** 138  |  **Score:** 3,862  |  **Created:** 2024-12-02

**Background:** OpenUI by TheSysDev is a full-stack generative UI framework built around OpenUI Lang, a compact streaming-first language for model-generated user interfaces. It provides a React runtime with built-in component libraries, ready-to-use chat interfaces, and claims up to 67% more token efficiency than JSON-based UI generation approaches.

**Problem it solves:** When LLMs generate UI, they typically output verbose JSON or HTML that consumes tokens inefficiently and arrives in chunks that are hard to render incrementally. OpenUI Lang is designed for streaming output, letting agents define and render structured UI components as the model generates them, with a pre-approved component catalog for security.

**Why another one?** OpenUI takes a standards-based approach: rather than each agent framework inventing its own UI rendering format, OpenUI proposes a shared specification that any client can implement. The streaming-first design and component catalog security model address practical concerns that generic HTML generation cannot.

---

## 16. [page-agent](https://github.com/alibaba/page-agent)
> JavaScript in-page GUI agent. Control web interfaces with natural language.

**Language:** TypeScript  |  **Stars:** 8,803  |  **Forks:** 694  |  **Score:** 3,575  |  **Created:** 2025-09-23

**Background:** Page Agent from Alibaba is a JavaScript library that enables natural language control of web interfaces directly within the browser. Unlike browser automation tools that require extensions, Python, or headless browsers, Page Agent operates as in-page JavaScript, using text-based DOM manipulation without screenshots or multimodal LLMs.

**Problem it solves:** Existing web automation approaches require external infrastructure — browser extensions, Playwright/Puppeteer servers, or screenshot-based multimodal models. Page Agent eliminates these dependencies by running entirely within the page's JavaScript context, making it trivial to add natural language control to any web application.

**Why another one?** The in-page, text-only approach is a meaningful architectural distinction. No screenshots means no multimodal LLM costs, no browser extension means no installation friction, and no external process means it works in any environment where JavaScript runs. The human-in-the-loop UI and optional Chrome extension provide flexibility without mandating complexity.

---

## 17. [autoresearch](https://github.com/karpathy/autoresearch)
> AI agents running research on single-GPU nanochat training automatically

**Language:** Python  |  **Stars:** 38,849  |  **Forks:** 5,377  |  **Score:** 3,413  |  **Created:** 2026-03-06

**Background:** Karpathy's autoresearch is an experiment in autonomous AI-driven ML research. The system gives an AI agent a simplified single-GPU LLM training setup (based on nanochat) and lets it run unsupervised overnight, modifying code, training for 5 minutes, checking results, keeping or discarding changes, and repeating. The repo is deliberately small — three core files drive the entire system.

**Problem it solves:** The hypothesis-code-experiment-analysis cycle that consumes a researcher's days runs continuously while the human sleeps. Autoresearch automates the tedious loop of empirical ML experimentation, potentially compressing weeks of manual iteration into overnight runs.

**Why another one?** The project's power lies in its simplicity and narrative framing. Rather than building a complex research automation platform, Karpathy provides a minimal three-file setup that anyone with a GPU can run. The science-fiction README — imagining a future where "research is entirely the domain of autonomous swarms of AI agents" — has captured imaginations far beyond the ML community.

---

## 18. [fish-speech](https://github.com/fishaudio/fish-speech)
> SOTA Open Source TTS

**Language:** Python  |  **Stars:** 27,372  |  **Forks:** 2,285  |  **Score:** 3,353  |  **Created:** 2023-10-10

**Background:** Fish Speech is a state-of-the-art open-source text-to-speech system from Fish Audio, featuring the S2 model for expressive voice cloning. The project has matured since its 2023 launch into a production-ready TTS platform with Docker support, a Hugging Face model hub presence, and an active multilingual community across Discord and QQ.

**Problem it solves:** High-quality voice cloning and TTS have traditionally been locked behind proprietary APIs with per-character pricing. Fish Speech provides comparable quality as an open-source, self-hostable solution, eliminating ongoing costs for applications that need voice generation at scale.

**Why another one?** Fish Speech's S2 model has achieved Product Hunt recognition and strong community traction, positioning it as the leading open-source alternative to commercial TTS APIs. Its expressive voice cloning capabilities and the backing of Fish Audio's dedicated team give it a sustainability advantage over single-developer TTS projects.

---

## 19. [A2UI](https://github.com/google/A2UI)
> Agent-to-User Interface: an open standard for agent-generated UIs.

**Language:** TypeScript  |  **Stars:** 13,231  |  **Forks:** 993  |  **Score:** 3,338  |  **Created:** 2025-09-24

**Background:** A2UI (Agent-to-User Interface) is a Google open-source project that provides a declarative JSON format and renderer libraries for agent-generated user interfaces. Currently in v0.8 public preview, it allows agents to "speak UI" by sending declarative descriptions that client applications render using their own native component libraries (Flutter, Angular, Lit, etc.).

**Problem it solves:** AI agents generating UI face a security-expressiveness tradeoff: arbitrary HTML/JS is unsafe, but plain text is limiting. A2UI provides a middle ground — a declarative data format where agents can only request pre-approved UI components from the client's catalog, making outputs "safe like data, but expressive like code."

**Why another one?** A2UI's security-first design is its key differentiator. The format is declarative data, not executable code, so LLM-generated UI cannot execute arbitrary scripts. The flat-list-with-ID-references structure is specifically optimized for LLM token efficiency and incremental updates, and the multi-platform renderer support (Flutter, Angular, Lit) reflects Google's cross-platform philosophy.

---

## 20. [hindsight](https://github.com/vectorize-io/hindsight)
> Hindsight: Agent Memory That Learns

**Language:** Python  |  **Stars:** 3,995  |  **Forks:** 279  |  **Score:** 3,282  |  **Created:** 2025-10-30

**Background:** Hindsight by Vectorize.io is an agent memory system focused on making agents learn over time rather than simply recall conversation history. Backed by a published research paper on arXiv, it claims state-of-the-art performance on long-term memory benchmarks and offers both a self-hosted option and a managed cloud service.

**Problem it solves:** Most agent memory systems store and retrieve conversation history, but they do not distill experience into reusable knowledge. Hindsight goes beyond recall to create agents that genuinely improve with use, eliminating the shortcomings of RAG and knowledge graph approaches for long-term memory tasks.

**Why another one?** The academic backing (arXiv paper) and benchmark results distinguish Hindsight from ad-hoc memory solutions. Its focus on learning rather than remembering addresses a fundamental limitation of current agent architectures, and the dual self-hosted/cloud deployment model lowers the barrier to adoption.

---

## 21. [browser](https://github.com/lightpanda-io/browser)
> Lightpanda: the headless browser designed for AI and automation

**Language:** Zig  |  **Stars:** 18,080  |  **Forks:** 672  |  **Score:** 2,974  |  **Created:** 2023-02-07

**Background:** Lightpanda is a headless browser written from scratch in Zig — not a Chromium fork or WebKit patch. Purpose-built for AI agents and web automation, it supports JavaScript execution, Web APIs, and compatibility with Playwright, Puppeteer, and chromedp through the Chrome DevTools Protocol (CDP).

**Problem it solves:** Chrome-based headless browsers are resource hogs — high memory consumption, slow startup, and significant per-instance costs when running at scale. Lightpanda uses 9x less memory and runs 11x faster than Chrome with instant startup, making large-scale web automation economically viable.

**Why another one?** Building a browser from scratch in Zig is an audacious technical choice that pays off in performance. The 9x memory reduction and 11x speed improvement are not incremental optimizations but architectural advantages of starting clean. CDP compatibility means existing automation scripts work without modification, removing the migration barrier.

---

## 22. [nanochat](https://github.com/karpathy/nanochat)
> The best ChatGPT that $100 can buy.

**Language:** Python  |  **Stars:** 48,769  |  **Forks:** 6,379  |  **Score:** 2,874  |  **Created:** 2025-10-13

**Background:** Nanochat by Andrej Karpathy is a minimal experimental harness for training LLMs on a single GPU node. It covers all major LLM stages — tokenization, pretraining, finetuning, evaluation, inference, and a ChatGPT-like web UI. Users can train a GPT-2 capability model for approximately $48 (2 hours on 8xH100) or as low as $15 on spot instances by setting a single `--depth` parameter.

**Problem it solves:** LLM training is typically associated with massive infrastructure and complex distributed systems. Nanochat makes the entire pipeline — from data prep to chat UI — accessible on a single GPU node with minimal, hackable code that anyone can understand and modify.

**Why another one?** Nanochat's continued trending alongside autoresearch reflects a symbiotic relationship — autoresearch uses nanochat as its training substrate. The GPT-2 speedrun leaderboard has created a competitive community dynamic that drives continuous optimization, while the single `--depth` dial for model complexity makes experimentation trivially accessible.

---

## 23. [hermes-agent](https://github.com/NousResearch/hermes-agent)
> The agent that grows with you

**Language:** Python  |  **Stars:** 7,969  |  **Forks:** 928  |  **Score:** 2,751  |  **Created:** 2025-07-22

**Background:** Hermes Agent is a self-improving AI agent built by Nous Research, the team behind the Hermes series of open-source language models. It features a built-in learning loop that creates skills from experience, improves them during use, and builds a deepening model of the user across sessions. It runs on anything from a $5 VPS to a GPU cluster and connects through Telegram, Discord, Slack, WhatsApp, Signal, and CLI.

**Problem it solves:** Most AI agents start from zero in every conversation, losing all learned context and preferences. Hermes Agent persists knowledge between sessions, searches its own conversation history, and creates reusable skills from repeated tasks, so the agent genuinely improves the more it is used.

**Why another one?** The self-improvement loop — not just memory recall but active skill creation and refinement — is the core differentiator. Combined with Nous Research's model expertise, multi-platform messaging support, and the ability to switch between 200+ models via OpenRouter without code changes, Hermes Agent offers a uniquely portable and adaptive agent experience.

---

## 24. [paperclip](https://github.com/paperclipai/paperclip)
> Open-source orchestration for zero-human companies

**Language:** TypeScript  |  **Stars:** 26,233  |  **Forks:** 3,483  |  **Score:** 2,709  |  **Created:** 2026-03-02

**Background:** Paperclip is a Node.js server and React UI that orchestrates teams of AI agents to run a business. Framed as "if OpenClaw is an employee, Paperclip is the company," it lets users define business goals, hire agent teams (CEO, CTO, engineers, designers, marketers), and track their work and costs from a single dashboard. Released less than two weeks ago, it has already gathered over 26,000 stars.

**Problem it solves:** Individual AI agents can execute tasks, but coordinating multiple agents toward a shared business objective — with budgets, org charts, governance, and goal alignment — requires orchestration that no single-agent framework provides. Paperclip manages business-level goals rather than pull requests.

**Why another one?** Paperclip operates at a fundamentally different abstraction layer than coding agents or task runners. Its org chart, budget tracking, and governance features model the structure of a human company, not a software project. The "zero-human company" framing, while provocative, reflects a real architectural need for multi-agent coordination beyond simple task queues.

---

## 25. [ai-engineering-field-guide](https://github.com/alexeygrigorev/ai-engineering-field-guide)
> Research into AI engineering interview assignments, take-home challenges, and hiring practices from Q4 2025 / Q1 2026

**Language:** HTML  |  **Stars:** 1,129  |  **Forks:** 124  |  **Score:** 2,652  |  **Created:** 2026-02-04

**Background:** The AI Engineering Field Guide by Alexey Grigorev is a data-driven resource for AI engineering roles, skills, and interviews. Based on analysis of 1,765 real job descriptions, actual interview experiences, and practitioner stories, it covers role analysis, job market data, interview questions, learning paths, and the gap between job postings and reality.

**Problem it solves:** AI engineering is a rapidly crystallizing role with unclear boundaries, inconsistent interview processes, and a disconnect between what companies post and what candidates experience. This guide provides empirical data on what the role actually entails, extracted from thousands of real job descriptions and interview reports.

**Why another one?** Unlike AI-generated career guides, every insight here comes from analyzing real data — 5,694+ job responsibilities, 4,525 use cases, and 100+ interview question sources. The emphasis on "reality vs. job postings" and the practical focus on what companies actually build with AI make it uniquely grounded in evidence rather than speculation.

---

> **Day's theme:** The agent ecosystem matures beyond individual coding assistants toward complete organizational infrastructure — from agent-native CLI wrappers and context databases to business-level orchestration, self-improving memory systems, and the design languages that make agent-generated interfaces look professional.
