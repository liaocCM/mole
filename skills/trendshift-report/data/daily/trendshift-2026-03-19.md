# Trendshift Report — 2026-03-19
**Total:** 25 repositories

---

## 1. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 108,363  |  **Forks:** 8,701  |  **Score:** 21,916  |  **Created:** 2025-10-09

**Background:** Superpowers is a composable agent skills framework and structured software development methodology created by Jesse Vincent (obra), designed to install into coding agents such as Claude Code, Cursor, Codex, OpenCode, and Gemini CLI via their plugin marketplaces. It enforces a multi-stage workflow: brainstorming and spec refinement before any code is written, an implementation plan broken into bite-sized tasks, and subagent-driven development with two-stage code review. The project has accumulated over 108,000 stars since launching in October 2025.

**Problem it solves:** Coding agents left to defaults tend to dive directly into writing code, skip test-driven development, and drift from the original intent mid-session. Superpowers installs guard rails — mandatory spec approval, red-green-refactor TDD enforcement, and plan checkpoints — so an agent can work autonomously for hours without derailing from what was agreed upon.

**Why another one?** Rather than being a new coding agent, Superpowers is a methodology layer that works across multiple agents via their native plugin systems. The differentiating angle is portability (same skills install in Claude Code, Cursor, Codex, OpenCode, and Gemini CLI) and the emphasis on subagent delegation rather than a single long-running context, which limits drift.

---

## 2. [skills](https://github.com/mattpocock/skills)
> My personal directory of skills, straight from my .claude directory.

**Language:** Shell  |  **Stars:** 9,379  |  **Forks:** 769  |  **Score:** 15,284  |  **Created:** 2026-02-03

**Background:** This is Matt Pocock's personal collection of agent skills extracted from his own `.claude` directory, covering the full arc from planning through development to tooling. The collection includes skills for writing PRDs via interactive interviews, converting PRDs into multi-phase implementation plans using tracer-bullet vertical slices, TDD workflows, codebase architecture improvement, and utilities like setting up pre-commit hooks and git guardrails for Claude Code.

**Problem it solves:** Coding agents are only as good as the instructions they receive. Most developers start from scratch when configuring agent workflows, leading to inconsistent results. This collection provides battle-tested, opinionated skill files that enforce structured planning (PRD-first), disciplined development (TDD, vertical slices), and safety practices (git guardrails) out of the box.

**Why another one?** While frameworks like Superpowers provide a complete methodology, Pocock's skills are modular and individually installable via `npx skills@latest add`. Each skill is self-contained — you can adopt just `write-a-prd` or just `tdd` without buying into an entire workflow. The collection reflects a TypeScript-heavy, Total TypeScript author's perspective, with domain-specific skills like `migrate-to-shoehorn` and `scaffold-exercises` that general frameworks do not cover.

---

## 3. [NemoClaw](https://github.com/NVIDIA/NemoClaw)
> Run OpenClaw more securely inside NVIDIA OpenShell with managed inference.

**Language:** JavaScript  |  **Stars:** 16,028  |  **Forks:** 1,685  |  **Score:** 12,775  |  **Created:** 2026-03-15

**Background:** NVIDIA NemoClaw is an open-source reference stack released in early alpha on March 16, 2026, that simplifies running OpenClaw always-on assistants inside the NVIDIA OpenShell sandboxed runtime. It bundles OpenShell (NVIDIA's agent security runtime), open-source NVIDIA Nemotron models, and a guided onboard wizard that creates a sandbox, configures inference, and applies security policies. The stack supports Docker on Linux, Colima or Docker Desktop on macOS, and Docker Desktop with WSL on Windows.

**Problem it solves:** Running autonomous AI assistants with full shell access is inherently risky — they can read credentials, exfiltrate data, and make uncontrolled network requests. NemoClaw wraps OpenClaw in a sandboxed environment with declarative YAML network policies enforced at the HTTP method and path level, so agents operate within explicit security boundaries without requiring users to configure sandboxing from scratch.

**Why another one?** NemoClaw is not an alternative to OpenClaw but an officially supported deployment harness from NVIDIA. The value proposition is the integration of managed inference (Nemotron models via NVIDIA's build platform) with a security-first runtime (OpenShell), targeting enterprises and developers who want to run always-on agents with auditable, policy-governed network access rather than unrestricted shell environments.

---

## 4. [unsloth](https://github.com/unslothai/unsloth)
> Unsloth Studio is a web UI for training and running open models like Qwen, DeepSeek, gpt-oss and Gemma locally.

**Language:** Python  |  **Stars:** 57,675  |  **Forks:** 4,860  |  **Score:** 9,572  |  **Created:** 2023-11-29

**Background:** Unsloth Studio is a unified local interface for running and training text, audio, embedding, and vision models on Windows, Linux, and macOS. The project started in November 2023 as an efficient fine-tuning library with custom Triton kernels and has since expanded into a full-featured web UI (Studio Beta) with model search, download, inference, export (GGUF, safetensors), reinforcement learning, data recipe workflows, and multi-GPU training support. It works directly with model teams behind gpt-oss, Qwen3, Llama 4, Mistral, Gemma, and Phi-4.

**Problem it solves:** Training and running open models locally typically requires juggling multiple tools — separate inference servers, training scripts, quantization utilities, and dataset preparation pipelines. Unsloth Studio consolidates these into a single interface: search and download models, chat with tool calling and code execution, create training datasets from PDFs and CSVs via visual node workflows, and fine-tune with up to 2x speed and 70% less VRAM than standard approaches.

**Why another one?** The differentiator is the combination of inference and training in one UI, backed by custom mathematical kernels that deliver measurable efficiency gains. Where tools like Ollama focus on inference and Hugging Face TRL focuses on training, Unsloth bridges both with the same model management layer. The reinforcement learning support (GRPO with 80% less VRAM, FP8 training) and direct collaboration with major model teams for day-one compatibility are further distinguishing factors.

---

## 5. [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)
> Open Multi-Agent Interactive Classroom — Get an immersive, multi-agent learning experience in just one click.

**Language:** TypeScript  |  **Stars:** 11,788  |  **Forks:** 1,763  |  **Score:** 9,510  |  **Created:** 2026-03-11

**Background:** OpenMAIC is an open-source AI education platform from Tsinghua University (THU-MAIC) that turns any topic or document into a multi-agent interactive classroom. Built with Next.js 16, React 19, and LangGraph, it generates slides, quizzes, interactive HTML simulations, and project-based learning activities, all delivered by AI teachers and AI classmates who can speak via TTS, draw on a whiteboard, and engage in real-time discussions. The project was published in JCST 2026 and includes built-in OpenClaw integration for generating classrooms directly from messaging apps like Feishu, Slack, or Telegram.

**Problem it solves:** Self-directed learning with LLMs is typically a solo, text-only experience — you ask questions, you get answers, and the interaction lacks the dynamics of a real classroom. OpenMAIC simulates a classroom environment with multiple AI agents playing distinct roles (teacher, peers), producing rich scene types (slides, quizzes, interactive simulations) that provide structured, multi-modal learning from a single topic description or uploaded document.

**Why another one?** The multi-agent classroom paradigm is the differentiator. Rather than a single chatbot answering questions, OpenMAIC orchestrates multiple agents into a teaching scenario with lecture, discussion, and interactive activities. The one-click deployment via Vercel, export to editable PPTX, and integration with messaging platforms via OpenClaw make it accessible to non-technical educators, not just AI researchers.

---

## 6. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers.

**Language:** Shell  |  **Stars:** 60,953  |  **Forks:** 9,146  |  **Score:** 7,984  |  **Created:** 2025-10-13

**Background:** The Agency is a growing collection of meticulously crafted AI agent personalities created by Mark Sitarzewski, born from a Reddit thread and months of iteration. Each agent is a specialized expert with a unique personality, communication style, deep domain expertise, and production-ready workflows with measurable success metrics. The roster spans engineering (frontend, backend, mobile, AI, DevOps, security), marketing, content, community, and operations divisions, with each agent file containing identity traits, core mission, technical deliverables with code examples, and success metrics.

**Problem it solves:** When using coding agents, most people start with a blank prompt or a generic system instruction. The Agency provides pre-built, personality-driven specialist profiles that give the agent domain expertise, a defined communication style, and deliverable-focused workflows — eliminating the cold-start problem of configuring an agent for a specific role.

**Why another one?** The differentiator is breadth and personality. While skill frameworks like Superpowers focus on development methodology, The Agency provides role-based personas across the entire product organization — from frontend developers and security engineers to Reddit community managers and whimsy injectors. The multi-tool integration (Claude Code, Cursor, Aider, Windsurf, Gemini CLI, OpenCode) via automated conversion scripts makes these agents portable across the ecosystem.

---

## 7. [open-swe](https://github.com/langchain-ai/open-swe)
> An Open-Source Asynchronous Coding Agent.

**Language:** Python  |  **Stars:** 8,172  |  **Forks:** 964  |  **Score:** 7,138  |  **Created:** 2025-05-21

**Background:** Open SWE is LangChain's open-source framework for building internal coding agents, modeled on the patterns used by Stripe (Minions), Ramp (Inspect), and Coinbase (Cloudbot). Built on LangGraph and Deep Agents, it provides cloud sandboxes (Modal, Daytona, Runloop, LangSmith), Slack and Linear invocation, subagent orchestration, and automatic PR creation. Every task runs in an isolated cloud sandbox with full shell access and zero production access.

**Problem it solves:** Elite engineering organizations are building internal coding agents — Slackbots, CLIs, and web apps that operate with minimal human oversight — but each builds from scratch. Open SWE provides the same architecture as a customizable, open-source starting point: isolated sandboxes, invocation from existing tools (Slack, Linear), and the agent harness wiring that otherwise takes weeks to build internally.

**Why another one?** Open SWE is explicitly not another general-purpose coding assistant. It targets the internal-agent-for-your-org use case: connected to internal systems, respecting internal permissioning, and operating asynchronously within safety boundaries. The composition on Deep Agents (rather than forking an existing agent) provides an upgrade path for pulling in upstream improvements while customizing orchestration, tools, and middleware for a specific organization.

---

## 8. [gstack](https://github.com/garrytan/gstack)
> Use Garry Tan's exact Claude Code setup: 15 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, and more.

**Language:** TypeScript  |  **Stars:** 39,705  |  **Forks:** 4,906  |  **Score:** 6,653  |  **Created:** 2026-03-11

**Background:** gstack is Y Combinator president Garry Tan's personal open-source software factory for Claude Code, packaging 20+ slash commands that turn the agent into a virtual engineering team — a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production bugs, a QA lead who opens a real browser, a security officer who runs OWASP and STRIDE audits, and a release engineer who ships the PR. Tan reports shipping 10,000-20,000 lines of production code per day part-time using this setup.

**Problem it solves:** Claude Code is powerful but unstructured. Without explicit roles and review stages, it produces code that may work but lacks the quality controls a real engineering team would enforce — design review, security audit, QA with real browser testing, and structured release management. gstack layers these roles on top of Claude Code as slash commands.

**Why another one?** The personal-brand angle is the differentiator. Tan is shipping this as his actual daily workflow, not a theoretical framework. The combination of specific, opinionated tools (`/qa` opens a real browser via Playwright, `/cso` runs OWASP + STRIDE audits, `/retro` generates retrospective metrics across projects) goes beyond planning-focused frameworks into the full build-review-ship cycle, targeting founders and technical CEOs who want to ship at scale without a large team.

---

## 9. [claude-hud](https://github.com/jarrodwatts/claude-hud)
> A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress.

**Language:** JavaScript  |  **Stars:** 12,154  |  **Forks:** 505  |  **Score:** 6,221  |  **Created:** 2026-01-02

**Background:** Claude HUD is a Claude Code plugin by Jarrod Watts that adds an always-visible status line below the input showing context window health, tool activity, running subagents, and todo progress. It uses Claude Code's native statusline API — no separate window or tmux required — and parses the transcript for real-time tool and agent activity updates every 300ms. The plugin supports configurable layouts (Full, Essential, Minimal) with toggleable display elements.

**Problem it solves:** Claude Code sessions become opaque as they grow longer: you cannot see how much context window remains, which tools are currently executing, what subagents are doing, or how far along a task list has progressed. Claude HUD makes all of this visible in real time, preventing the surprise of hitting context limits or losing track of parallel agent activity.

**Why another one?** Claude HUD is not an alternative to Claude Code but an observability layer for it. The native statusline integration (no external window) and the use of Claude Code's actual token data (not estimated) make it a first-party-feeling extension. The context health bar that transitions from green to yellow to red provides an early warning system that no built-in feature currently offers.

---

## 10. [ground-station](https://github.com/sgoudelis/ground-station)
> Ground Station is all-in-one satellite monitoring suite.

**Language:** JavaScript  |  **Stars:** 3,166  |  **Forks:** 552  |  **Score:** 5,767  |  **Created:** 2025-03-01

**Background:** Ground Station is a full-featured, open-source satellite tracking and radio communication platform designed for amateur radio operators, satellite enthusiasts, and researchers. It provides real-time tracking of hundreds of satellites with high-precision orbital models, automated antenna rotator control, rig control via Hamlib, SDR waterfall visualization with live transcription and GMSK packet decoding, telemetry packet viewing, automated observation scheduling, and TLE data synchronization from CelesTrak and SatNOGS. The project was built with Claude Code and Codex.

**Problem it solves:** Amateur satellite tracking and radio communication requires juggling multiple separate tools — tracking software, SDR applications, rotator controllers, and telemetry decoders — each with its own interface and configuration. Ground Station consolidates these into a single web-based platform with an integrated DSP pipeline, automated pass scheduling, and decoded output management.

**Why another one?** The all-in-one integration is the differentiator. Existing open-source tools like GPredict handle tracking, SDR# handles waterfall display, and SatNOGS handles observation scheduling, but none combine all three with live transcription, packet decoding, and file management in a unified web interface. The SDR hardware management supporting RTL-SDR, SoapySDR, and UHD/USRP radios with remote capability broadens the hardware compatibility beyond typical single-SDR tools.

---

## 11. [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)
> Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper.

**Language:** Python  |  **Stars:** 8,119  |  **Forks:** 865  |  **Score:** 5,736  |  **Created:** 2026-03-15

**Background:** AutoResearchClaw is a fully autonomous research pipeline from the Aiming Lab that takes a research idea as input and produces a complete academic paper as output, with zero human intervention. The v0.3.2 release supports cross-platform agent backends (Claude Code, Codex CLI, Copilot CLI, Gemini CLI, Kimi CLI) and messaging platforms (Discord, Telegram, Lark, WeChat) via OpenClaw bridge. The showcase includes 8 papers across 8 domains — math, statistics, biology, computing, NLP, RL, vision, and robustness — all generated autonomously.

**Problem it solves:** Academic research involves a long pipeline from literature review through hypothesis formulation, experiment design, code implementation, result analysis, and paper writing. Each stage requires different skills and tools. AutoResearchClaw automates the entire pipeline end-to-end, including an anti-fabrication system (VerifiedRegistry plus experiment diagnosis and repair loop) to prevent hallucinated results.

**Why another one?** The self-evolving and cross-platform aspects differentiate it. v0.3.2 delegates compute-heavy stages (code generation and experiment execution) to external CLI agents with budget control and timeout management, rather than running everything in a single context. The anti-fabrication system — explicitly flagging and repairing fabricated experimental results — addresses a trust problem that simpler paper-generation tools ignore.

---

## 12. [opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf)
> PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.

**Language:** Java  |  **Stars:** 8,284  |  **Forks:** 562  |  **Score:** 5,302  |  **Created:** 2025-05-13

**Background:** OpenDataLoader PDF is an open-source PDF parser that extracts Markdown, JSON (with bounding boxes), and HTML from any PDF, ranking first in benchmarks with 0.90 overall accuracy and 0.93 table extraction accuracy across 200 real-world PDFs. Built in Java 11+ with Python, Node.js, and Java SDKs, it offers a deterministic local mode processing at 0.05s per page and an AI hybrid mode for complex documents including scanned PDFs with OCR in 80+ languages. The project also pioneers open-source PDF auto-tagging for accessibility compliance, planned for Q2 2026.

**Problem it solves:** Converting PDFs to structured data for RAG and LLM pipelines is notoriously unreliable — tables break, reading order is wrong, formulas are lost, and scanned documents need OCR. OpenDataLoader PDF addresses all of these with a benchmark-leading extraction engine that provides bounding boxes for every element and an XY-Cut++ reading order algorithm, making the output directly usable for RAG chunking and source citations.

**Why another one?** Two differentiators: benchmark accuracy and accessibility automation. On the extraction side, it claims the top position in overall accuracy with deterministic output (no LLM randomness in local mode). On the accessibility side, it is the first open-source tool to generate Tagged PDFs end-to-end — a capability that matters as accessibility regulations are enforced worldwide and manual PDF remediation costs $50-200 per document.

---

## 13. [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
> Master programming by recreating your favorite technologies from scratch.

**Language:** Markdown  |  **Stars:** 482,545  |  **Forks:** 45,406  |  **Score:** 5,084  |  **Created:** 2018-05-09

**Background:** Build Your Own X is a curated compilation of step-by-step tutorials for recreating popular technologies from scratch, maintained by CodeCrafters since May 2018. It covers 30+ categories including 3D renderers, databases, Docker, operating systems, programming languages, search engines, web servers, and more, with tutorials in C, C++, Python, JavaScript, Rust, Go, Java, and other languages. With over 482,000 stars, it is one of the most-starred repositories on GitHub.

**Problem it solves:** Understanding how a technology works at a deep level — not just using its API but knowing what happens inside — requires building it from scratch. Finding high-quality, step-by-step tutorials for this is difficult because they are scattered across blogs, university pages, and book chapters. This repository indexes them by technology category with direct links.

**Why another one?** The repository keeps trending because it is continuously updated with new tutorials and the quality bar (well-written, step-by-step guides only) makes it a reliable resource. The Feynman-inspired premise ("What I cannot create, I do not understand") resonates with developers at every level, and the 482k-star social proof drives recurring discovery.

---

## 14. [code-review-graph](https://github.com/tirth8205/code-review-graph)
> Local knowledge graph for Claude Code. Builds a persistent map of your codebase so Claude reads only what matters — 6.8x fewer tokens.

**Language:** Python  |  **Stars:** 3,330  |  **Forks:** 299  |  **Score:** 5,042  |  **Created:** 2026-02-26

**Background:** code-review-graph is a Claude Code plugin that builds a structural map of a codebase using Tree-sitter, storing functions, classes, imports, call relationships, inheritance, and test coverage as a graph in SQLite. When a file changes, the graph performs blast-radius analysis — tracing every caller, dependent, and test that could be affected — and provides Claude with only the minimal set of files needed for review. It supports 14 languages including Python, TypeScript, Go, Rust, Java, and C#, with incremental updates completing in under 2 seconds for 2,900-file projects.

**Problem it solves:** Claude Code re-reads the entire codebase on every task, consuming tokens and context window space on files that are irrelevant to the current change. code-review-graph reduces token usage by 6.8x by computing the precise blast radius of a change and feeding Claude only the affected files, resulting in higher review quality with lower cost.

**Why another one?** The blast-radius approach is the differentiator. Rather than heuristic file filtering or embedding-based retrieval, it uses actual AST-level dependency analysis (Tree-sitter) to determine which files are structurally affected by a change. The incremental update mechanism (SHA-256 hash checks, re-parse only changed files) keeps the graph fresh without full rebuilds, and the Claude Code plugin integration makes it transparent to the user's workflow.

---

## 15. [get-shit-done](https://github.com/gsd-build/get-shit-done)
> A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TACHES.

**Language:** JavaScript  |  **Stars:** 39,428  |  **Forks:** 3,197  |  **Score:** 4,662  |  **Created:** 2025-12-14

**Background:** GSD (Get Shit Done) is a context engineering and spec-driven development system for Claude Code, OpenCode, Gemini CLI, Codex, Copilot, and Antigravity, created by TACHES. It solves "context rot" — the quality degradation that happens as Claude fills its context window — through XML prompt formatting, subagent orchestration, and state management. Installation is a single `npx` command, and the system works on Mac, Windows, and Linux. Trusted by engineers at Amazon, Google, Shopify, and Webflow.

**Problem it solves:** Vibecoding produces inconsistent results that fall apart at scale because the AI lacks structured context about what is being built and why. GSD provides the context engineering layer: it extracts a complete understanding of the project, maintains it across sessions, and gives Claude everything it needs to do the work and verify it, preventing the quality degradation that occurs as conversations grow longer.

**Why another one?** GSD explicitly positions itself against "enterprise theater" tools (sprint ceremonies, story points, Jira workflows). Where BMAD, Speckit, and similar systems add process overhead, GSD hides the complexity (context engineering, XML formatting, subagent orchestration) behind a few commands that "just work." The single-developer, anti-ceremony philosophy and the focus on context rot as a specific technical problem give it a distinct audience among solo builders.

---

## 16. [stop-slop](https://github.com/hardikpandya/stop-slop)
> A skill file for removing AI tells from prose.

**Language:** —  |  **Stars:** 2,335  |  **Forks:** 196  |  **Score:** 4,660  |  **Created:** 2026-01-11

**Background:** Stop Slop is an agent skill by Hardik Pandya that teaches Claude (or any LLM) to detect and remove AI-characteristic patterns from prose. It consists of a core SKILL.md with instructions, plus reference files cataloguing banned phrases (throat-clearing openers, emphasis crutches, business jargon, all adverbs), structural cliches (binary contrasts, dramatic fragmentation, rhetorical setups, false agency), and sentence-level rules (no Wh- sentence starters, no em dashes, active voice required). It includes a 1-10 scoring rubric across five dimensions: directness, rhythm, trust, authenticity, and density.

**Problem it solves:** AI-generated prose has recognizable patterns — predictable phrases, structures, and rhythms — that make it instantly identifiable as machine-written. For writers using AI as a drafting tool, these patterns undermine credibility. Stop Slop provides a systematic detection and removal framework that can be applied as a post-processing step to any AI-generated text.

**Why another one?** Stop Slop is not a rewriting tool but a pattern reference — a curated taxonomy of what makes prose sound AI-generated, with before-and-after examples. This approach is more transparent and controllable than "humanizer" tools that obscure their logic. The skill-file format makes it composable with other agent workflows: it can be loaded alongside development skills to ensure documentation, commit messages, and user-facing text avoid AI tells.

---

## 17. [OpenShell](https://github.com/NVIDIA/OpenShell)
> OpenShell is the safe, private runtime for autonomous AI agents.

**Language:** Rust  |  **Stars:** 3,572  |  **Forks:** 352  |  **Score:** 4,418  |  **Created:** 2026-02-24

**Background:** NVIDIA OpenShell is a sandboxed execution runtime for autonomous AI agents, written in Rust and released as alpha software in February 2026. It provides isolated container environments governed by declarative YAML policies that prevent unauthorized file access, data exfiltration, and uncontrolled network activity at the HTTP method and path level. Sandboxes include pre-installed agent runtimes (Claude, OpenCode, Codex, Copilot), language runtimes (Python 3.13, Node 22), and developer tools (gh, git, vim). It supports Docker on Linux, Colima or Docker Desktop on macOS, and remote deployment via `--remote user@host`.

**Problem it solves:** Giving autonomous AI agents shell access is a security liability — they can read SSH keys, exfiltrate API tokens, and make arbitrary network requests. OpenShell enforces security at the runtime level: every sandbox starts with minimal outbound access, additional access requires an explicit YAML policy, and the proxy enforces rules at L7 (HTTP method + path), not just IP/port. This means an agent can GET from GitHub's API but not POST to it, unless the policy allows it.

**Why another one?** OpenShell targets a specific gap: L7 policy enforcement for agent sandboxes. Docker containers provide process isolation but not fine-grained network control. OpenShell's proxy sits between the sandbox and the internet, enforcing per-endpoint read/write permissions. The Rust implementation, agent-first design (ships with agent skills for cluster debugging and policy generation), and the NemoClaw integration for managed inference position it as infrastructure rather than a standalone product.

---

## 18. [Mole](https://github.com/tw93/Mole)
> Deep clean and optimize your Mac.

**Language:** Shell  |  **Stars:** 43,618  |  **Forks:** 1,269  |  **Score:** 4,409  |  **Created:** 2025-09-23

**Background:** Mole is a macOS system maintenance tool by tw93 that combines the functionality of CleanMyMac, AppCleaner, DaisyDisk, and iStat Menus in a single CLI binary installable via Homebrew. It provides deep cleaning (caches, logs, browser leftovers), smart uninstallation (apps plus launch agents, preferences, and hidden remnants), disk analysis with large file detection, live system monitoring (CPU, GPU, memory, disk, network), and project build artifact purging. An experimental Windows version is available in a separate branch.

**Problem it solves:** Mac maintenance tools are typically commercial ($30-100 per year for CleanMyMac, DaisyDisk, etc.) and each handles only one aspect — cleaning, uninstalling, disk visualization, or monitoring. Mole consolidates all four into a free, open-source CLI tool with safety-first defaults: path validation, protected-directory rules, dry-run previews, and explicit confirmation for higher-risk actions.

**Why another one?** The CLI-first, single-binary approach is the differentiator. Where CleanMyMac and similar tools are GUI applications with annual subscriptions, Mole is a `brew install` away and runs from the terminal. The `mo analyze` command moves files to Trash through Finder (recoverable) rather than deleting directly, and whitelisting support lets users protect specific caches and optimization rules.

---

## 19. [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)
> Bash is all you need - A nano claude code-like agent harness, built from 0 to 1.

**Language:** TypeScript  |  **Stars:** 37,344  |  **Forks:** 5,917  |  **Score:** 4,286  |  **Created:** 2025-06-29

**Background:** Learn Claude Code is an educational project from shareAI-lab that builds a minimal Claude Code-like agent harness from scratch, demonstrating that the core of a coding agent is a model placed in an environment with tools to perceive and act. The project makes a philosophical argument — grounded in the history of DeepMind DQN, OpenAI Five, AlphaStar, and Tencent Jueyu — that the "agent" is always the model itself, not the surrounding framework, and that the harness is just the minimal infrastructure to let the model operate.

**Problem it solves:** The "agent" label has been co-opted by prompt-chaining frameworks and no-code workflow builders that obscure what an agent actually is. This project strips away the abstraction layers to show that a coding agent is fundamentally a model with bash access, file tools, and a loop — demystifying the architecture for developers who want to understand (and build) agents rather than just consume them.

**Why another one?** The pedagogical framing is the differentiator. Where Claude Code, Codex, and Cursor are production tools, and Deep Agents and LangGraph are frameworks, Learn Claude Code is an explainer. It teaches harness engineering — how to wire a model to tools, manage context, and handle errors — by building the minimal viable version. The 37k stars suggest significant demand for this kind of first-principles understanding.

---

## 20. [Crucix](https://github.com/calesthio/Crucix)
> Your personal intelligence agent. Watches the world from multiple data sources and pings you when something changes.

**Language:** JavaScript  |  **Stars:** 6,567  |  **Forks:** 1,003  |  **Score:** 4,285  |  **Created:** 2026-03-14

**Background:** Crucix is a self-hosted, Jarvis-style OSINT dashboard that pulls from 27 open-source intelligence feeds — satellite fire detection, flight tracking, radiation monitoring, satellite constellation tracking, economic indicators, live market prices, conflict data, sanctions lists, and social sentiment — in parallel every 15 minutes, rendering everything on a single dashboard with 3D globe and world map views. It has only one dependency (Express) and runs with a single `node server.mjs` command. A live demo is available at crucix.live.

**Problem it solves:** Real-time intelligence data — satellite imagery, radiation levels, conflict events, economic indicators, flight and maritime tracking — is publicly available but scattered across dozens of government APIs, research institutions, and open data feeds. Crucix aggregates and cross-correlates these sources on a single self-hosted dashboard, updated every 15 minutes, with no subscription or cloud dependency.

**Why another one?** The LLM integration turns it from a passive dashboard into an active intelligence assistant: it pushes multi-tier alerts to Telegram and Discord when something meaningful changes, responds to commands like `/brief` and `/sweep` from a phone, and generates actionable insights grounded in cross-domain data. The minimal dependency footprint (just Express), zero-cloud architecture, and AGPL license target researchers, journalists, traders, and OSINT analysts who want full control over their intelligence feed.

---

## 21. [frontend-slides](https://github.com/zarazhangrui/frontend-slides)
> Create beautiful slides on the web using Claude's frontend skills.

**Language:** CSS  |  **Stars:** 11,081  |  **Forks:** 818  |  **Score:** 3,100  |  **Created:** 2026-01-28

**Background:** Frontend Slides is a Claude Code skill for creating animation-rich HTML presentations from scratch or by converting PowerPoint files. It uses a "show, don't tell" approach: instead of asking users to describe aesthetic preferences in words, it generates visual style previews and lets users pick. Output is a single HTML file with inline CSS and JS — no npm, no build tools, no frameworks. The skill includes 12 curated style presets across dark, light, and specialty themes, with an explicit anti-AI-slop design philosophy.

**Problem it solves:** Non-designers struggle to create visually compelling presentations, and AI-generated slides tend to converge on generic aesthetics (purple gradients on white). Frontend Slides removes both barriers: the visual style discovery process lets users choose from distinctive presets without articulating design preferences, and the curated styles are specifically designed to avoid generic AI aesthetics.

**Why another one?** The zero-dependency output is the key differentiator. Tools like Slidev and reveal.js require build tooling and framework knowledge. Frontend Slides produces a single self-contained HTML file that can be opened in any browser, shared as-is, or customized directly. The PPT conversion feature (extracting text, images, and notes from existing PowerPoints) and the progressive-disclosure skill architecture (main file is 180 lines, supporting files loaded on demand) make it both powerful and lightweight.

---

## 22. [llm-app](https://github.com/pathwaycom/llm-app)
> Ready-to-run cloud templates for RAG, AI pipelines, and enterprise search with live data. Docker-friendly. Always in sync.

**Language:** Jupyter Notebook  |  **Stars:** 58,639  |  **Forks:** 1,392  |  **Score:** 3,100  |  **Created:** 2023-07-19

**Background:** Pathway AI Pipelines is a collection of ready-to-deploy LLM application templates for RAG, enterprise search, and AI pipelines that maintain real-time synchronization with data sources including file systems, Google Drive, Sharepoint, S3, Kafka, PostgreSQL, and real-time APIs. The templates scale to millions of pages and include built-in data indexing with vector search, hybrid search, and full-text search — all in-memory with cache. No separate infrastructure setup is required.

**Problem it solves:** Building production RAG systems requires solving the data freshness problem: documents change, new files are added, old ones are deleted, and the index must reflect the current state. Most RAG tutorials show static indexing. Pathway's templates continuously sync with data sources, automatically reflecting additions, deletions, and updates without manual re-indexing.

**Why another one?** The live-sync architecture is the differentiator. Where LangChain and LlamaIndex focus on the retrieval and generation pipeline, Pathway focuses on the data pipeline underneath: real-time indexing that stays in sync with changing data sources. The templates are production-ready (Docker-deployable on GCP, AWS, Azure, Render) and include multimodal RAG, knowledge graph RAG, and adaptive RAG variants that go beyond basic question-answering.

---

## 23. [daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)
> LLM-powered stock analysis system for A/H/US markets.

**Language:** Python  |  **Stars:** 24,734  |  **Forks:** 25,594  |  **Score:** 3,068  |  **Created:** 2026-01-10

**Background:** Daily Stock Analysis is an LLM-powered stock analysis system by ZhuLinsen that covers A-shares, Hong Kong stocks, and US markets including major indices (SPX, DJI, IXIC). It produces daily decision dashboards with one-sentence core conclusions, precise buy/sell price levels, and operation checklists, combining technical analysis (real-time MA, multi-head alignment), chip distribution, sentiment intelligence, and real-time market data. The system supports multiple AI backends via LiteLLM (Gemini, OpenAI, DeepSeek, Claude, Ollama) and pushes results to WeChat Work, Feishu, Telegram, Discord, Slack, DingTalk, email, and Pushover.

**Problem it solves:** Individual investors typically rely on fragmented tools for technical analysis, news monitoring, and sentiment tracking, and must manually synthesize these signals into trading decisions. This system automates the entire pipeline: data collection from multiple sources (AkShare, Tushare, YFinance), multi-dimensional analysis, LLM-powered decision synthesis, and automated delivery to messaging platforms — all running on GitHub Actions with zero server cost.

**Why another one?** The zero-cost automation via GitHub Actions and the Chinese market focus (A-shares, Hong Kong stocks) differentiate it from English-language alternatives. Built-in market strategy systems (three-phase review strategy for A-shares, regime strategy for US stocks), AI backtesting verification of historical analysis accuracy, and the new Agent conversational mode supporting 11 built-in strategies (MA golden cross, Chan theory, Elliott wave) make it more than a simple alert system.

---

## 24. [deepagents](https://github.com/langchain-ai/deepagents)
> Agent harness built with LangChain and LangGraph. Equipped with a planning tool, a filesystem backend, and the ability to delegate to sub-agents.

**Language:** Python  |  **Stars:** 17,096  |  **Forks:** 2,411  |  **Score:** 3,026  |  **Created:** 2025-07-27

**Background:** Deep Agents is LangChain's batteries-included agent harness — an opinionated, ready-to-run agent that provides planning (write_todos), filesystem operations (read, write, edit, ls, glob, grep), shell execution, sub-agent delegation, smart context management with auto-summarization, and a CLI with an interactive TUI. It also supports web search, headless mode for CI scripting, remote sandboxes, persistent memory, custom skills, and human-in-the-loop approval. A JS/TS version (deepagents.js) is also available.

**Problem it solves:** Building a capable coding agent from LangGraph primitives requires wiring up prompts, tools, context management, and sub-agent orchestration — a non-trivial amount of boilerplate. Deep Agents provides all of this out of the box: `pip install deepagents` and `create_deep_agent()` gives you a working agent that can plan, execute, delegate, and manage its own context, ready to customize.

**Why another one?** Deep Agents is the harness layer that Open SWE and other LangChain-ecosystem agents compose on top of. Where Claude Code and Codex are closed (or partially open) end-user products, Deep Agents is an explicitly composable Python library: swap models, add tools, customize prompts, and configure sub-agents programmatically. The LangGraph-native architecture means agents are deployable as LangGraph applications with built-in observability via LangSmith.

---

## 25. [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
> 734+ structured cybersecurity skills for AI agents. MITRE ATT&CK mapped. agentskills.io open standard. Works with Claude Code and more.

**Language:** Python  |  **Stars:** 3,627  |  **Forks:** 360  |  **Score:** 2,906  |  **Created:** 2026-02-25

**Background:** Anthropic Cybersecurity Skills is the largest open-source collection of cybersecurity skills for AI agents, providing 753 production-grade skills across 26 security domains. Each skill follows the agentskills.io open standard: YAML frontmatter for discovery, structured Markdown for step-by-step execution, and reference files for deep technical context. The entire collection is mapped to MITRE ATT&CK (all 14 Enterprise tactics, 200+ techniques) and aligned to NIST CSF 2.0. It works with Claude Code, GitHub Copilot, and custom LangChain pipelines.

**Problem it solves:** Security practitioners carry domain knowledge — how to perform memory forensics, hunt for C2 beaconing, audit Kubernetes RBAC, reverse .NET malware — that AI agents lack out of the box. This collection gives agents the same structured knowledge as a one-command install, enabling them to perform cybersecurity tasks with the methodology and rigor of an experienced professional.

**Why another one?** The MITRE ATT&CK mapping is the differentiator. Rather than a generic collection of security prompts, each skill is mapped to specific ATT&CK tactics and techniques, making the collection useful for threat hunting, incident response, and compliance workflows that reference ATT&CK as a standard. The agentskills.io open standard and cross-platform compatibility (Claude Code, Copilot, LangChain) make it an ecosystem contribution rather than a vendor-specific tool.

---

> **Day's theme:** The dominant narrative across today's 25 repos is the maturation of the AI coding agent ecosystem into a layered stack — skills and methodology frameworks (Superpowers, gstack, GSD, skills), sandboxed runtimes and security enforcement (OpenShell, NemoClaw), observability and context optimization (Claude HUD, code-review-graph), and composable agent harnesses (Deep Agents, Open SWE) — mirroring the emergence of a full platform architecture around autonomous software development, while domain-specific applications in education, OSINT, research automation, and cybersecurity demonstrate the pattern spreading beyond code.
