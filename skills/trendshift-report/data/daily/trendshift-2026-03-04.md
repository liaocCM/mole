# Trendshift Report — 2026-03-04
**Total:** 25 repositories

---

## 1. [worldmonitor](https://github.com/koala73/worldmonitor)
> Real-time global intelligence dashboard — AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking.

**Language:** TypeScript  |  **Stars:** 34,697  |  **Forks:** 5,833  |  **Score:** 9,274  |  **Created:** 2026-01-08

**Background:** World Monitor takes the top spot today, an open-source situational awareness platform built in TypeScript that aggregates global news, geopolitical events, and infrastructure status into a unified dashboard. It offers domain-specific variants — tech, finance, commodity, and happy news — each with tailored data sources. Since launching in January 2026, it has crossed 34K stars with sustained multi-day trending momentum.

**Problem it solves:** Professionals who need to track global events across multiple domains currently switch between dozens of news sites, financial terminals, and monitoring tools. World Monitor consolidates all of this into a single AI-powered interface that classifies, prioritizes, and surfaces the most relevant signals based on professional context.

**Why another one?** World Monitor has climbed from rank 11 two days ago to rank 1 today, with its score growing from 3,572 to 9,274. The multi-variant deployment model — same engine, different configurations per professional domain — is proving to be a winning formula. The AGPL v3 license and self-hosting support differentiate it from commercial alternatives like Bloomberg Terminal or Dataminr.

---

## 2. [RuView](https://github.com/ruvnet/RuView)
> WiFi DensePose turns commodity WiFi signals into real-time human pose estimation, vital sign monitoring, and presence detection — all without video.

**Language:** Rust  |  **Stars:** 31,832  |  **Forks:** 4,198  |  **Score:** 8,890  |  **Created:** 2025-06-07

**Background:** RuView is the edge AI perception system that uses WiFi Channel State Information to reconstruct human pose, breathing rate, heart rate, and presence without cameras. Built on RuVector and implementing Carnegie Mellon's WiFi DensePose research as a practical edge system, it runs on ESP32 meshes at $1 per node. After yesterday's viral spike (score 24,100), it settles at 8,890 today while maintaining rank 2.

**Problem it solves:** Camera-based monitoring is privacy-invasive, fails through walls and in darkness, and requires line-of-sight. RuView provides equivalent sensing capabilities using only WiFi signal disturbances, enabling monitoring in elder care, security, and smart building scenarios where cameras are impractical or unacceptable.

**Why another one?** The score correction from 24,100 to 8,890 suggests the viral spike is normalizing, but 31K stars (doubled in two days) indicates lasting interest rather than a one-day novelty. The edge-only, camera-free, internet-free design resonates with privacy-conscious developers and IoT practitioners. RuView has established itself as the reference implementation for WiFi-based sensing.

---

## 3. [openclaw](https://github.com/openclaw/openclaw)
> OpenClaw — Personal AI Assistant that runs on your own devices across 20+ messaging channels.

**Language:** TypeScript  |  **Stars:** 289,626  |  **Forks:** 54,924  |  **Score:** 7,303  |  **Created:** 2025-11-24

**Background:** OpenClaw is the 290K-star personal AI assistant platform that connects to WhatsApp, Telegram, Slack, Discord, Signal, iMessage, and 15+ more channels. The Gateway architecture separates the control plane from the assistant experience, and the platform supports voice (macOS/iOS/Android), live Canvas, persistent memory, and scheduled tasks. MIT-licensed and fully self-hosted.

**Problem it solves:** AI assistants that live in their own apps force users to context-switch. OpenClaw puts the assistant inside the messaging apps users already have open, providing a persistent, always-on AI presence that works across every communication channel without requiring a dedicated interface.

**Why another one?** Score jumped from 4,485 to 7,303, its highest in this three-day window. The surrounding ecosystem activity — skills, use cases, Studio, Star Office UI — creates a flywheel where each new tool drives attention back to the core platform. At 290K stars, OpenClaw has transcended "popular project" status and become a platform ecosystem comparable to major open-source frameworks.

---

## 4. [Perplexica](https://github.com/ItzCrazyKns/Perplexica)
> A privacy-focused AI answering engine that runs entirely on your own hardware.

**Language:** TypeScript  |  **Stars:** 32,359  |  **Forks:** 3,474  |  **Score:** 6,298  |  **Created:** 2024-04-09

**Background:** Perplexica (now rebranded as Vane) is a privacy-focused AI search engine that combines web search with local or cloud LLMs (Ollama, OpenAI, Claude, Groq) to deliver cited answers. It features multiple search modes — Speed, Balanced, and Quality — and can search across web pages, discussions, or academic papers. Docker deployment keeps everything self-contained. The project launched in April 2024 and has accumulated over 32K stars.

**Problem it solves:** Commercial AI search engines (Perplexity, Google AI Overviews) process queries on remote servers, creating privacy and data retention concerns. Perplexica runs the entire search-and-answer pipeline locally, keeping queries and results private. The cited sources model provides verifiability that opaque AI answers lack.

**Why another one?** Perplexica is the leading open-source Perplexity alternative, and it keeps trending as privacy awareness grows. The rebranding to Vane signals a maturation from "Perplexity clone" to independent product identity. Support for mixing local and cloud LLMs (Ollama for privacy-sensitive queries, cloud for complex ones) provides flexibility that pure-local or pure-cloud alternatives lack.

---

## 5. [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
> A compilation of well-written, step-by-step guides for re-creating our favorite technologies from scratch.

**Language:** Markdown  |  **Stars:** 473,392  |  **Forks:** 44,374  |  **Score:** 5,636  |  **Created:** 2018-05-09

**Background:** One of GitHub's top 5 most-starred repositories, Build Your Own X collects step-by-step tutorials for rebuilding fundamental technologies — databases, operating systems, compilers, neural networks, Docker, Git, web servers, and more. Maintained by CodeCrafters since 2018, following Feynman's "what I cannot create, I do not understand."

**Problem it solves:** Deep understanding of technologies requires implementation experience, not just API familiarity. These tutorials provide structured paths from zero to working implementation for dozens of technologies, producing fundamentally deeper knowledge than reading documentation or source code.

**Why another one?** Score increased from 3,964 to 5,636. Build Your Own X trends perpetually because new developers discover it continuously and because the collection grows with new tutorials. At 473K stars, it is permanent infrastructure in the developer education ecosystem.

---

## 6. [canopy](https://github.com/canopy-network/canopy)
> Official golang implementation of the Canopy Network Protocol — a peer-to-peer launchpad for new blockchains.

**Language:** Go  |  **Stars:** 4,262  |  **Forks:** 9,293  |  **Score:** 5,628  |  **Created:** 2024-10-30

**Background:** Canopy Network is a recursive blockchain framework where chains bootstrap each other into independence, forming a web of mutual utility and security. The Go implementation provides both the recursive chain-building framework and the seed chain that started the cycle. Currently in Betanet, the project combines Go for the protocol layer with Next.js for the web interface.

**Problem it solves:** Launching a new blockchain requires building validator sets, establishing security guarantees, and bootstrapping economic activity — a cold-start problem that most new chains solve through centralized launches. Canopy's recursive architecture allows existing chains to provide security and validator infrastructure for new chains, eliminating the cold-start problem.

**Why another one?** Canopy's unusually high fork-to-star ratio (9,293 forks vs 4,262 stars — a 2:1 ratio) suggests validator/node operator participation rather than casual interest. The recursive chain-launching model is architecturally novel compared to Cosmos SDK's hub-and-spoke or Polkadot's parachain approach. The Betanet status and road-to-mainnet indicate this is actively progressing toward production.

---

## 7. [shannon](https://github.com/KeygraphHQ/shannon)
> Shannon — AI Pentester for web applications and APIs by Keygraph.

**Language:** TypeScript  |  **Stars:** 32,869  |  **Forks:** 3,275  |  **Score:** 5,604  |  **Created:** 2025-09-27

**Background:** Shannon is an autonomous, white-box AI pentester by Keygraph that combines source code analysis with live exploitation. It analyzes web application source code to identify attack vectors, then uses browser automation and command-line tools to execute real exploits — injection attacks, authentication bypass, SSRF, XSS — against the running application. Only vulnerabilities with working proof-of-concept exploits make it into the final report. Now supports Claude models on AWS Bedrock and Google Vertex AI.

**Problem it solves:** AI-assisted coding (Claude Code, Cursor) has accelerated code production, but security testing has not kept pace. Shannon addresses this gap by performing automated security testing at development speed — analyzing source code for vulnerabilities and proving them exploitable before they reach production.

**Why another one?** Shannon differentiates from traditional scanners (which produce false positives) by requiring a working PoC for every reported vulnerability. The white-box approach (source code analysis + live exploitation) is more thorough than black-box scanners. The recent addition of Claude on Bedrock and Vertex AI support expands enterprise deployment options. At 32K stars, it is the most popular open-source AI pentesting tool.

---

## 8. [agency-agents](https://github.com/msitarzewski/agency-agents)
> The Agency — a collection of meticulously crafted AI agent personalities for specialized workflows.

**Language:** Shell  |  **Stars:** 18,396  |  **Forks:** 2,842  |  **Score:** 5,598  |  **Created:** 2025-10-13

**Background:** The Agency is a collection of specialized AI agent personality templates, born from a Reddit thread and months of iteration by msitarzewski. Each agent is defined with a specific domain expertise, communication style, and deliverable focus — from frontend developers and DevOps engineers to Reddit community managers and "whimsy injectors." The templates work with Claude Code, Cursor, and other agent platforms.

**Problem it solves:** Generic AI agents produce generic output. By defining specialized personas with domain expertise, process workflows, and quality metrics, The Agency produces agents that behave like domain experts rather than general-purpose assistants. Each agent template encodes the decision-making patterns and communication style of a real specialist.

**Why another one?** At 18K stars, The Agency has found a sweet spot between rigid workflow automation and open-ended chat. The personality-driven approach — giving agents specific voices, processes, and success metrics — produces more consistent output than system prompts alone. The Reddit community origin ensures the templates are battle-tested by real users rather than designed in theory.

---

## 9. [awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
> A community collection of OpenClaw use cases for making life easier.

**Language:**   |  **Stars:** 22,126  |  **Forks:** 1,817  |  **Score:** 5,089  |  **Created:** 2026-02-08

**Background:** Hesam Sheikh's community-curated collection of 36+ real-world OpenClaw use cases, covering social media automation, productivity workflows, development tooling, finance tracking, health monitoring, and home automation. Each entry provides reproducible steps for setting up the workflow.

**Problem it solves:** Users adopt OpenClaw but struggle to find concrete applications beyond basic chat. This repository provides a gallery of tested, outcome-focused recipes — daily Reddit digests, YouTube channel summaries, calendar management — that answer "what should I use my AI assistant for?"

**Why another one?** Remains steady near 5,000 score across all three days, indicating baseline demand from the continuous flow of new OpenClaw users. The outcome-oriented format (what you get) rather than tool-oriented format (what you install) makes it the most accessible entry point for non-technical OpenClaw users.

---

## 10. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> Discover 5490+ community-built OpenClaw skills, organized by category.

**Language:**   |  **Stars:** 33,181  |  **Forks:** 3,144  |  **Score:** 4,933  |  **Created:** 2026-01-25

**Background:** VoltAgent's catalog of 5,490+ OpenClaw skills sourced from ClawHub and organized by category. Functions as the browsable "app store" that OpenClaw's CLI-first design does not natively provide. Also links to related AI agent research papers.

**Problem it solves:** Finding relevant skills among thousands of options requires curation. This awesome-list provides categorized, community-vetted discovery that raw registry browsing cannot match.

**Why another one?** Score decreased slightly from 6,619 to 4,933 but remains firmly in the top 10. The list trends consistently because every new OpenClaw skill generates cross-referencing, and every new OpenClaw user needs to discover what skills exist. At 33K stars, it is the de facto OpenClaw skill directory.

---

## 11. [agent-browser](https://github.com/vercel-labs/agent-browser)
> Headless browser automation CLI for AI agents — fast Rust CLI with Node.js fallback.

**Language:** Rust  |  **Stars:** 20,352  |  **Forks:** 1,189  |  **Score:** 4,758  |  **Created:** 2026-01-11

**Background:** Agent-browser is Vercel Labs' headless browser automation CLI built in Rust with a Node.js fallback. It provides a command-line interface for AI agents to control Chrome — opening pages, taking accessibility snapshots with ref-based selectors, clicking, filling forms, getting text content, and taking screenshots. The accessibility-tree-based interaction model (snapshot + click/fill by ref) is designed for LLM consumption rather than traditional CSS selectors.

**Problem it solves:** AI agents need to interact with web pages, but existing browser automation tools (Playwright, Puppeteer) generate output designed for human developers, not LLMs. Agent-browser produces accessibility tree snapshots with stable reference IDs that agents can use to identify and interact with page elements, reducing the token overhead and error rate of web automation.

**Why another one?** The ref-based interaction model (snapshot, then act by @ref) is specifically designed for LLM agents, not humans. The Rust CLI provides sub-millisecond parsing overhead (vs Node.js startup latency), and Vercel's backing ensures integration with the Next.js/Vercel ecosystem. At 20K stars, it is rapidly becoming the standard CLI for agent-driven browser automation.

---

## 12. [superpowers](https://github.com/obra/superpowers)
> A complete software development workflow for your coding agents, built on composable skills.

**Language:** Shell  |  **Stars:** 75,000  |  **Forks:** 5,793  |  **Score:** 4,663  |  **Created:** 2025-10-09

**Background:** Jesse Vincent's composable skills framework and structured development methodology for coding agents. Installs into Claude Code, Cursor, Codex, and OpenCode. Enforces spec-first design, TDD, YAGNI, and subagent-driven development. 75K stars make it the most widely adopted agent skill framework.

**Problem it solves:** Unguided coding agents produce inconsistent results — skipping tests, drifting from intent, and making poor architectural decisions during long sessions. Superpowers imposes engineering discipline on agents, enabling multi-hour autonomous sessions that follow professional software development practices.

**Why another one?** Maintains a steady ~4,600-4,800 score across all three days, reflecting stable baseline demand rather than viral spikes. Its cross-agent portability (same skills in 4+ agent platforms) is the key differentiator — as agent diversity grows, methodology-layer tools that work everywhere become more valuable than platform-specific optimizations.

---

## 13. [CoPaw](https://github.com/agentscope-ai/CoPaw)
> CoPaw — a collaborative AI agent framework by AgentScope

**Language:** Python  |  **Stars:** 9,613  |  **Forks:** 1,072  |  **Score:** 4,258  |  **Created:** 2026-02-24

**Background:** AgentScope AI's collaborative agent framework, providing Python primitives for multi-agent collaboration — shared state, task delegation, coordination, and conflict resolution. Licensed under Apache 2.0, distributed via PyPI, and following black code style. Nearly 10K stars in its first 10 days.

**Problem it solves:** Multi-agent systems that need to collaborate (not just run in parallel) require coordination primitives that most frameworks lack. CoPaw provides these as a library — shared state management, message passing, task allocation — so developers define agent behavior rather than distributed systems logic.

**Why another one?** Score stabilized from 5,787 to 4,258, indicating sustained interest beyond the launch spike. CoPaw's collaboration-first positioning (vs autonomy-focused frameworks) addresses the emerging pattern of multi-agent workflows where agents need to coordinate rather than work independently. The AgentScope ecosystem suggests a broader platform vision.

---

## 14. [prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)
> A comprehensive step-by-step understanding of how to engineer optimal prompts within Claude.

**Language:** Jupyter Notebook  |  **Stars:** 33,102  |  **Forks:** 3,371  |  **Score:** 4,198  |  **Created:** 2024-04-02

**Background:** Anthropic's official 9-chapter interactive prompt engineering course with hands-on Jupyter Notebook exercises. Covers prompt structure, clarity techniques, model-specific behavior, and advanced methods using Claude 3 Haiku for cost-effective experimentation. Also available as a Google Sheets version.

**Problem it solves:** Effective Claude prompt engineering requires understanding model-specific behavior, not just generic advice. This tutorial teaches Claude-specific techniques with immediate feedback, providing the fastest path from beginner to effective user.

**Why another one?** Score stabilized around 4,200-5,200 across the three-day window, reflecting a steady stream of new Claude users rather than viral spikes. As the authoritative first-party resource, it captures every wave of Claude adoption. The interactive format remains more effective than static documentation.

---

## 15. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> Practice makes Claude perfect — best practices for Claude Code workflows.

**Language:** HTML  |  **Stars:** 12,935  |  **Forks:** 1,213  |  **Score:** 3,953  |  **Created:** 2025-10-31

**Background:** A community reference by shanraisshan documenting best practices for Claude Code, including commands, sub-agents, and skills. The repo provides both best-practice documentation and concrete implementations, plus an orchestration workflow showing how Commands, Agents, and Skills compose together. Updated regularly (last update March 7, 2026), it includes curated insights from practitioners like Boris Cherny.

**Problem it solves:** Claude Code's documentation covers features but not workflows. Users need opinionated best practices for structuring commands, organizing sub-agents, and composing skills into effective development workflows. This repo provides those patterns with concrete examples and implementation guides.

**Why another one?** At 12.9K stars, this is the most popular community guide for Claude Code. The Command -> Agent -> Skill orchestration workflow it documents has become a de facto standard for organizing Claude Code projects. Regular updates (reflecting the March 2026 last-update date) keep it current with Claude Code's rapid evolution.

---

## 16. [claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)
> 170+ ready-to-use scientific and research skills for AI agents — biology, chemistry, medicine, genomics, molecular dynamics, and more.

**Language:** Python  |  **Stars:** 14,105  |  **Forks:** 1,530  |  **Score:** 3,935  |  **Created:** 2025-10-19

**Background:** K-Dense AI's collection of 170+ scientific skills and 250+ database interfaces implementing the open Agent Skills standard. Covers cancer genomics, drug-target binding, molecular dynamics, RNA velocity, geospatial science, time series forecasting, FRED economic data, and more. Works with Cursor, Claude Code, Codex, and other compatible agents.

**Problem it solves:** General-purpose coding agents lack the domain knowledge needed for scientific computing — querying protein databases, running molecular docking, performing gene expression analysis. These skills provide specialized knowledge and API integrations that transform general agents into research assistants.

**Why another one?** Score remained stable around 3,900-4,500 across all three days, reflecting consistent demand from the scientific computing community. The cross-agent compatibility via the Agent Skills standard ensures these skills remain relevant regardless of which coding agent wins market share. K-Dense Web as the commercial companion validates the quality of the open-source foundation.

---

## 17. [waoowaoo](https://github.com/waoowaooAI/waoowaoo)
> An AI-powered short drama and comic video production tool — from novel text to complete video.

**Language:** TypeScript  |  **Stars:** 8,285  |  **Forks:** 1,700  |  **Score:** 3,496  |  **Created:** 2026-01-22

**Background:** Waoowaoo AI Studio is an AI video production tool that converts novel text into complete short-form videos. It automates the pipeline from script analysis (extracting characters, scenes, and plot) through AI-generated consistent character images and scene backgrounds, storyboard-based video assembly, and multi-character AI voice synthesis. Built with Docker for easy deployment, the project targets Chinese and English users.

**Problem it solves:** Producing short-form drama or comic videos from written content requires a multi-disciplinary team — scriptwriters, artists, animators, voice actors, editors. Waoowaoo replaces this entire pipeline with AI, taking a novel or script as input and producing a finished video with consistent characters, matching scenes, and synchronized voiceover.

**Why another one?** Waoowaoo targets the booming Chinese short-drama market specifically, where AI-generated content is being adopted faster than in Western markets. The end-to-end pipeline (text to finished video) is more ambitious than tools that handle only one step (image generation or voice synthesis). The Docker-first deployment and bilingual support (CN/EN) reflect a practical, ship-now philosophy.

---

## 18. [OpenSandbox](https://github.com/alibaba/OpenSandbox)
> A general-purpose sandbox platform for AI applications with multi-language SDKs and unified APIs.

**Language:** Python  |  **Stars:** 7,180  |  **Forks:** 526  |  **Score:** 3,480  |  **Created:** 2025-12-17

**Background:** Alibaba's sandbox platform for AI workloads, providing multi-language SDKs and a formal sandbox protocol for lifecycle management and execution. Supports Docker and Kubernetes runtimes for coding agents, GUI agents, agent evaluation, code execution, and RL training.

**Problem it solves:** Every AI agent executing code needs sandboxing, but teams typically build ad-hoc Docker solutions. OpenSandbox provides a production-tested, protocol-driven platform with multi-language SDK support, so agent teams can focus on agent logic rather than container orchestration.

**Why another one?** Score stabilized around 3,500 after the initial spike, suggesting settled adoption rather than hype. OpenSandbox fills a genuine infrastructure gap — as agent platforms multiply, the demand for standardized, enterprise-grade sandboxing grows proportionally. Alibaba's backing provides the maintenance guarantees enterprise users require.

---

## 19. [vscode-dark-islands](https://github.com/bwya77/vscode-dark-islands)
> A dark color theme for VS Code inspired by easemate IDE — floating glass panels, rounded corners, smooth animations.

**Language:** PowerShell  |  **Stars:** 5,123  |  **Forks:** 151  |  **Score:** 3,056  |  **Created:** 2026-02-14

**Background:** Islands Dark recreates the easemate IDE's aesthetic in VS Code — deep dark canvas, glass-effect floating panels, rounded corners, pill-shaped scrollbars, and smooth CSS transitions. The theme requires both a color theme extension and custom CSS injection to achieve effects beyond VS Code's standard theming API. Ships with IBM Plex Mono for the editor and FiraCode Nerd Font Mono for the terminal.

**Problem it solves:** VS Code's theming system controls colors but not UI geometry. Islands Dark pushes beyond these constraints with CSS injection that adds glassmorphism, directional light simulation, and hover-triggered animations — visual refinements that make long coding sessions more pleasant.

**Why another one?** Score dropped from 4,724 to 3,056 as the easemate-inspired aesthetic moves from viral novelty to sustained adoption. The 34:1 star-to-fork ratio confirms most users consume rather than customize the theme. The two-part installation (extension + CSS hack) is an unusual barrier, but the visual result is compelling enough to justify the extra steps.

---

## 20. [qmd](https://github.com/tobi/qmd)
> Query Markup Documents — an on-device search engine for your notes, transcripts, and documentation.

**Language:** TypeScript  |  **Stars:** 13,649  |  **Forks:** 788  |  **Score:** 2,933  |  **Created:** 2025-12-08

**Background:** QMD (Query Markup Documents) by Tobi is a local-first search engine for markdown documents. It combines BM25 full-text search, vector semantic search (via node-llama-cpp with GGUF models), and LLM re-ranking — all running on-device. Users create collections from their notes, meeting transcripts, and documentation, then search across everything with keyword, semantic, or hybrid queries. The context tree system lets users annotate collections with descriptions that improve LLM-driven search relevance.

**Problem it solves:** Personal knowledge (notes, meeting transcripts, documentation) accumulates in markdown files scattered across directories. Finding information requires remembering file names or grepping through thousands of files. QMD indexes everything into a searchable corpus with semantic understanding, so "quarterly planning process" finds relevant content even if those exact words do not appear.

**Why another one?** QMD's killer feature is the context tree — hierarchical annotations that provide LLMs with semantic context about document collections, dramatically improving search relevance. The triple search approach (BM25 + vector + re-ranking) ensures both keyword precision and semantic recall. Running entirely on-device via GGUF models means no data leaves the user's machine, unlike cloud-based knowledge search tools.

---

## 21. [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
> The performance optimization system for AI agent harnesses — Anthropic Hackathon Winner.

**Language:** JavaScript  |  **Stars:** 69,024  |  **Forks:** 8,618  |  **Score:** 2,739  |  **Created:** 2026-01-18

**Background:** Everything Claude Code (ECC) by Affaan M is a multi-language performance optimization system for AI agent harnesses, winner of an Anthropic Hackathon. It includes npm-distributed utilities (ecc-universal, ecc-agentshield), a GitHub App with 150+ installations, and support for 6 languages. At 69K stars with 30 contributors, it has become a critical performance layer in the Claude Code ecosystem.

**Problem it solves:** AI agents operate within harness constraints — token limits, context windows, tool call overhead — that degrade performance on large codebases. ECC optimizes agent behavior within these constraints, reducing token waste and improving task completion rates through specialized optimization layers.

**Why another one?** Score decreased from 2,375 to 2,739 (slight increase), reflecting stable demand. ECC addresses the meta-problem of agent efficiency rather than adding features, which makes it complementary to every other tool on this list. The Anthropic Hackathon pedigree and GitHub App distribution channel provide credibility and reach.

---

## 22. [MinecraftConsoles](https://github.com/smartcmd/MinecraftConsoles)
> Source code of Minecraft Legacy Console Edition v1.6.0560.0 (TU19) with fixes and improvements.

**Language:** C++  |  **Stars:** 4,286  |  **Forks:** 808  |  **Score:** 2,702  |  **Created:** 2026-03-01

**Background:** A community-maintained source code release of Minecraft Legacy Console Edition TU19 with applied fixes — keyboard/mouse input, fullscreen support, LAN multiplayer, high-resolution timers, native screen resolution. Windows is the primary platform, with unofficial Wine compatibility on macOS/Linux. Created just three days ago.

**Problem it solves:** Minecraft Legacy Console Edition was discontinued, leaving its player community without updates or modifications. This project preserves the console edition codebase and adds community-requested features (LAN multiplayer, keyboard input) that the original never received.

**Why another one?** Score held steady from yesterday (2,866 to 2,702), maintaining its chart position after a strong debut. Game preservation projects generate sustained interest from nostalgic communities. The LAN multiplayer implementation addresses the top requested feature for local play, giving the project practical utility beyond historical preservation.

---

## 23. [superset](https://github.com/superset-sh/superset)
> The Terminal for Coding Agents — run multiple agents simultaneously with worktree isolation.

**Language:** TypeScript  |  **Stars:** 6,327  |  **Forks:** 403  |  **Score:** 2,503  |  **Created:** 2025-10-21

**Background:** Superset is a macOS terminal for parallel coding agent execution. Each agent task gets its own git worktree and branch, a built-in diff viewer enables code review, and monitoring with notifications keeps developers informed across 10+ simultaneous agents. Available for macOS download.

**Problem it solves:** Multiple agents modifying the same codebase simultaneously cause conflicts and interference. Superset provides automatic worktree isolation, agent status monitoring, and integrated diff review — the complete workflow for parallel agent-assisted development.

**Why another one?** Maintains a consistent ~2,500-3,000 score across all three days. As parallel agent workflows become standard practice, dedicated orchestration tools like Superset become essential infrastructure. The purpose-built approach (vs configuring tmux or screen) provides a significantly better experience for the specific pattern of agent-parallel development.

---

## 24. [skills](https://github.com/anthropics/skills)
> Anthropic's implementation of skills for Claude — instructions, scripts, and resources Claude loads dynamically.

**Language:** Python  |  **Stars:** 88,119  |  **Forks:** 9,339  |  **Score:** 2,479  |  **Created:** 2025-09-22

**Background:** This is Anthropic's official skills repository, containing the reference implementations that demonstrate Claude's skills system. Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. The repository includes skills ranging from creative applications (art, music, design) to technical tasks (testing, MCP server generation) to enterprise workflows (communications, branding). It also contains the source-available skills powering Claude's document creation capabilities (docx, pdf, pptx, xlsx).

**Problem it solves:** Claude's base capabilities are broad but not deep in any specific domain. Skills teach Claude how to complete specialized tasks repeatably — following brand guidelines, executing organization-specific workflows, or automating personal tasks — without retraining the underlying model.

**Why another one?** At 88K stars, this is the canonical reference for Claude skill development. Its appearance today reflects the broader trend of skill ecosystem growth visible across this chart. The inclusion of document creation skills (docx, pdf, pptx, xlsx) that power Claude's native features provides real-world production examples of skill design patterns.

---

## 25. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster.

**Language:** Shell  |  **Stars:** 75,677  |  **Forks:** 6,100  |  **Score:** 2,427  |  **Created:** 2025-02-22

**Background:** Anthropic's official terminal-based agentic coding tool, now over a year old. It operates in the terminal with full codebase understanding, executes tasks through natural language, and supports plugins, a marketplace, IDE integration, and GitHub @claude tagging. The plugin ecosystem has become a development platform in its own right.

**Problem it solves:** Context-switching between terminals, IDEs, and AI chat interfaces wastes developer attention. Claude Code brings the AI agent into the terminal — the environment where many developers already work — with native access to the filesystem, git, and project context.

**Why another one?** Claude Code's position at #25 with a 2,427 score is modest compared to its 75K stars, reflecting stable background adoption rather than a viral spike. As the official Anthropic coding agent, it serves as the platform on which much of this chart's ecosystem is built — Superpowers, Everything Claude Code, visual-explainer, and claude-code-best-practice all depend on it.

---

> **Day's theme:** The AI tooling stack is crystallizing into layers — situational awareness platforms (World Monitor), sensing infrastructure (RuView), personal assistants (OpenClaw), security testing (Shannon), browser automation (agent-browser), and local knowledge search (QMD) — with cross-cutting ecosystem tools (skills, best practices, agent personalities) gluing them together.
