# Trendshift Report — 2026-03-27
**Total:** 25 repositories

---

## 1. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 138,686  |  **Forks:** 11,746  |  **Score:** 14,216  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent is a complete software development workflow for coding agents, now commanding over 138,000 stars. It enforces a disciplined spec-plan-implement-review process using composable skills that trigger automatically, ensuring agents work methodically through TDD and YAGNI principles rather than jumping straight into code.

**Problem it solves:** Coding agents left unsupervised jump directly into writing code without understanding the full problem, producing poorly planned implementations. Superpowers enforces a structured workflow where the agent first teases out a spec, presents it in digestible chunks, builds an implementation plan, then launches subagent-driven development with built-in review cycles.

**Why another one?** Superpowers focuses on development methodology rather than tool orchestration. Its subagent-driven development model allows Claude to work autonomously for hours without deviating from the plan, and at 138,000 stars it has proven its approach at scale as the de facto reference implementation for structured agent-driven development.

---

## 2. [last30days-skill](https://github.com/mvanhorn/last30days-skill)
> AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary.

**Language:** Python  |  **Stars:** 18,665  |  **Forks:** 1,503  |  **Score:** 12,288  |  **Created:** 2026-01-23

**Background:** /last30days by mvanhorn is a Claude Code skill that researches any topic across Reddit, X, YouTube, Hacker News, Polymarket, Bluesky, Instagram, and TikTok from the last 30 days, then synthesizes a grounded narrative with real citations. Now at version 2.9.5, it includes comparative mode, per-project config, and 455+ tests.

**Problem it solves:** The AI world reinvents itself monthly, and staying current requires manually scanning multiple platforms. /last30days automates multi-source research with a composite scoring pipeline — bidirectional text similarity, engagement velocity, source authority weighting, and cross-platform convergence detection — delivering a single grounded briefing.

**Why another one?** The multi-signal quality-ranking pipeline is the differentiator. Rather than simple keyword search across platforms, /last30days applies sophisticated relevance scoring with Polymarket prediction data for calibrated confidence levels. The comparative mode ("X vs Y") with parallel research passes and side-by-side verdicts goes beyond what any single-source tool offers.

---

## 3. [insanely-fast-whisper](https://github.com/Vaibhavs10/insanely-fast-whisper)
> An opinionated CLI to transcribe audio files with Whisper on-device, powered by Transformers, Optimum, and Flash Attention.

**Language:** Jupyter Notebook  |  **Stars:** 12,399  |  **Forks:** 914  |  **Score:** 9,018  |  **Created:** 2023-10-10

**Background:** Insanely Fast Whisper is an opinionated CLI for on-device audio transcription using OpenAI's Whisper models with Hugging Face Transformers. It can transcribe 150 minutes of audio in under 98 seconds on an Nvidia A100 using Flash Attention 2, making blazingly fast transcription a practical reality.

**Problem it solves:** Running Whisper transcription out of the box is slow — standard fp32 inference takes over 30 minutes for 2.5 hours of audio. Insanely Fast Whisper combines fp16 precision, batching, and Flash Attention 2 to achieve a 20x speedup, making large-scale transcription feasible on single GPUs.

**Why another one?** The project started as a benchmark showcase but evolved into a lightweight, installable CLI that makes these optimizations accessible to non-experts. A simple `pipx install` and one command gets you state-of-the-art transcription speed without manually configuring Transformers, batching, or attention backends.

---

## 4. [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)
> Teams-first Multi-agent orchestration for Claude Code.

**Language:** TypeScript  |  **Stars:** 24,305  |  **Forks:** 2,215  |  **Score:** 7,788  |  **Created:** 2026-01-09

**Background:** Oh My ClaudeCode (OMC) by Yeachan Heo is a multi-agent orchestration layer for Claude Code with zero learning curve. It provides both a terminal CLI and in-session skills for team orchestration, autopilot mode, and cross-provider advisor queries (including Codex), with a companion project oh-my-codex for OpenAI's CLI.

**Problem it solves:** A single Claude Code session lacks the ability to coordinate multiple agents on parallel tasks or consult different AI providers for second opinions. OMC adds team orchestration, autopilot workflows, and multi-provider advisory through simple slash commands and CLI invocations.

**Why another one?** OMC's "don't learn Claude Code, just use OMC" philosophy lowers the barrier to advanced orchestration. The dual-surface design (CLI for terminal users, slash commands for in-session users) and cross-provider support (Claude, Codex, and others through the `/ask` flow) make it uniquely accessible compared to framework-heavy alternatives.

---

## 5. [skills](https://github.com/slavingia/skills)
> Claude Code skills based on The Minimalist Entrepreneur by Sahil Lavingia.

**Language:** N/A  |  **Stars:** 6,804  |  **Forks:** 616  |  **Score:** 6,152  |  **Created:** 2026-03-23

**Background:** Minimalist Entrepreneur Skills by Sahil Lavingia (CEO of Gumroad and author of The Minimalist Entrepreneur) packages the book's methodology into 10 Claude Code skills. Released just four days ago, it has already accumulated 6,800 stars, reflecting strong interest in applying entrepreneurship frameworks through AI coding tools.

**Problem it solves:** First-time founders make predictable mistakes — building before validating, underpricing, scaling prematurely. These skills encode a proven entrepreneurship methodology as interactive slash commands (`/find-community`, `/validate-idea`, `/mvp`, `/pricing`) that guide founders through each decision with structured frameworks.

**Why another one?** As the author's own implementation of his book's methodology, these skills carry unique authority. The progression from community discovery through sustainable growth mirrors the book's chapter structure, creating a guided entrepreneurship journey rather than isolated business tools.

---

## 6. [chandra](https://github.com/datalab-to/chandra)
> OCR model that handles complex tables, forms, handwriting with full layout.

**Language:** Python  |  **Stars:** 8,400  |  **Forks:** 858  |  **Score:** 5,534  |  **Created:** 2025-10-08

**Background:** Chandra OCR 2 by Datalab is a state-of-the-art OCR model that converts images and PDFs into structured HTML, Markdown, or JSON while preserving layout information. Version 2 launched in March 2026 with significant improvements to math, tables, layout, and multilingual OCR across 90+ languages.

**Problem it solves:** Traditional OCR tools struggle with complex document layouts — tables within forms, handwritten notes alongside printed text, mathematical equations, and multilingual content. Chandra handles all of these while reconstructing the spatial layout, extracting images with captions, and preserving checkbox states in forms.

**Why another one?** Chandra 2 tops the olmocr benchmark and shows significant improvements in multilingual performance. Unlike cloud-only OCR services, it offers both local HuggingFace inference and remote vLLM server modes, giving users control over their data. The structured output formats (HTML/Markdown/JSON) make downstream processing straightforward.

---

## 7. [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
> Turn Claude Code into a full game dev studio — 48 AI agents, 36 workflow skills, and a complete coordination system mirroring real studio hierarchy.

**Language:** Shell  |  **Stars:** 8,174  |  **Forks:** 1,230  |  **Score:** 4,847  |  **Created:** 2026-02-12

**Background:** Claude Code Game Studios by Donchitos transforms a single Claude Code session into a full game development studio with 49 agents, 72 skills, 12 hooks, and 11 rules. The agents are organized into a three-tier studio hierarchy — directors (Opus), department leads (Sonnet), and specialists (Sonnet/Haiku) — mirroring how real game studios operate.

**Problem it solves:** Building a game solo with AI lacks the structure of a real studio — there is no one to stop you from hardcoding magic numbers, skipping design docs, or writing spaghetti code. Game Studios provides specialized agents for each role with defined responsibilities, escalation paths, and quality gates that catch mistakes early.

**Why another one?** The studio hierarchy metaphor maps directly to how real game studios operate, making it intuitive for game developers. The scale — 49 agents across design, programming, art, audio, narrative, QA, and production — goes well beyond proof-of-concept into production-grade complexity with document templates for GDDs, UX specs, and sprint plans.

---

## 8. [awesome-opensource-ai](https://github.com/alvinunreal/awesome-opensource-ai)
> Curated list of the best truly open-source AI projects, models, tools, and infrastructure.

**Language:** N/A  |  **Stars:** 2,064  |  **Forks:** 158  |  **Score:** 4,671  |  **Created:** 2026-03-24

**Background:** Awesome Open Source AI by Boring Dystopia Development is a curated directory of battle-tested, production-proven open-source AI projects organized into 14 categories — from core frameworks and foundation models to inference engines, agentic systems, RAG, generative media, training tools, and MLOps. Released just three days ago, it has quickly gathered 2,064 stars.

**Problem it solves:** The open-source AI landscape is vast and fragmented, making it difficult to identify which projects are truly production-ready versus research experiments. This list applies strict quality criteria — only "elite-tier" projects make the cut — providing a reliable starting point for teams evaluating open-source AI infrastructure.

**Why another one?** The focus on "truly open-source" and "production-proven" projects distinguishes it from broader AI directories that mix research prototypes with battle-tested tools. The 14-category taxonomy provides comprehensive coverage from training through deployment, and the emerging projects section tracks promising newcomers separately.

---

## 9. [Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam)
> real time face swap and one-click video deepfake with only a single image.

**Language:** Python  |  **Stars:** 89,167  |  **Forks:** 12,954  |  **Score:** 4,600  |  **Created:** 2023-09-24

**Background:** Deep-Live-Cam 2.1 is a real-time face swap and video deepfake tool that requires only a single source image. With nearly 90,000 stars, it is one of the most popular computer vision projects on GitHub, offering features like mouth masking for accurate lip sync, multi-face mapping, and live performance mode.

**Problem it solves:** Creating face swaps traditionally requires extensive training data, powerful hardware, and technical expertise. Deep-Live-Cam reduces this to three clicks — select a face, choose a camera, and press live — enabling real-time face swapping for content creation, entertainment, and creative projects.

**Why another one?** The real-time capability is the core differentiator. While most deepfake tools process video offline, Deep-Live-Cam operates live with a webcam feed. Built-in ethical safeguards prevent processing inappropriate media, and the one-click simplicity makes it accessible to non-technical users for legitimate creative applications.

---

## 10. [claude-howto](https://github.com/luongnv89/claude-howto)
> A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value.

**Language:** Python  |  **Stars:** 20,611  |  **Forks:** 2,462  |  **Score:** 3,998  |  **Created:** 2025-11-07

**Background:** Claude How To by luongnv89 is a structured, visual, example-driven guide to mastering Claude Code, featuring 10 tutorial modules, Mermaid diagrams, copy-paste templates, and a guided learning path. At over 20,000 stars, it has become the definitive practitioner reference beyond official documentation.

**Problem it solves:** Claude Code's official documentation describes features but does not show how to combine them into effective workflows. Users discover powerful patterns through weeks of trial and error. Claude How To provides a progressive learning path with production-ready templates for hooks, skills, subagents, and MCP configurations.

**Why another one?** Unlike official docs that are feature-organized, Claude How To follows a progressive learning path from beginner to power user (11-13 hours). Built-in self-assessment via `/self-assessment` and `/lesson-quiz` slash commands help users identify gaps, and the visual Mermaid diagrams explain how each feature works internally.

---

## 11. [expect](https://github.com/millionco/expect)
> Expect tests your app in a browser so you don't have to.

**Language:** TypeScript  |  **Stars:** 3,060  |  **Forks:** 125  |  **Score:** 3,910  |  **Created:** 2026-03-12

**Background:** Expect by Million is an AI-powered browser testing tool that automatically tests web applications by navigating them in a real browser. Released just two weeks ago, it has gathered 3,060 stars with a notably low fork ratio, indicating strong individual developer interest in AI-driven end-to-end testing.

**Problem it solves:** Writing and maintaining browser tests is tedious — selectors break, test logic drifts from actual user flows, and coverage gaps accumulate silently. Expect automates browser testing by having an AI agent interact with your application as a real user would, identifying issues without manually written test scripts.

**Why another one?** Expect focuses specifically on AI-driven browser testing rather than adding AI to an existing test framework. The low-friction approach — point it at your app and it tests — eliminates the test authoring bottleneck that makes many teams underinvest in end-to-end testing.

---

## 12. [dev-browser](https://github.com/SawyerHood/dev-browser)
> A Claude Skill to give your agent the ability to use a web browser.

**Language:** TypeScript  |  **Stars:** 5,441  |  **Forks:** 344  |  **Score:** 3,630  |  **Created:** 2025-12-02

**Background:** Dev Browser by SawyerHood (brought to you by Do Browser) is a browser automation tool that lets AI agents and developers control browsers with sandboxed JavaScript scripts. It features persistent pages, auto-connection to running Chrome instances, and full Playwright API support — all running scripts in a QuickJS WASM sandbox.

**Problem it solves:** AI coding agents cannot interact with web content — they cannot verify UI changes, scrape data, or test web applications during development. Dev Browser bridges this gap by giving agents browser control through a CLI that supports headless execution, Chrome attachment, and full page interaction.

**Why another one?** The sandboxed execution model is the key differentiator. Scripts run in a QuickJS WASM environment with no host access, making it safe to pre-approve in Claude Code's permission system. The CLI-first design means agents just run `dev-browser --help` and get a full LLM usage guide — no plugin or skill installation required.

---

## 13. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 71,854  |  **Forks:** 11,138  |  **Score:** 3,426  |  **Created:** 2025-10-13

**Background:** Agency Agents by Mark Sitarzewski provides a growing collection of meticulously crafted AI agent personas for professional roles. Now at over 71,000 stars (up from 60,000 a week ago), it continues rapid growth. Each agent has defined personality traits, core missions, workflows, technical deliverables, and success metrics, with multi-tool support for Cursor, Aider, Windsurf, Gemini CLI, and more.

**Problem it solves:** Teams adopting AI agents need role-specific system prompts and workflow definitions for every business function — frontend, backend, mobile, DevOps, marketing, and more. Agency Agents provides these ready-made with battle-tested workflows and measurable success metrics, eliminating prompt engineering overhead.

**Why another one?** The personality-driven approach — agents with unique voices, communication styles, and strong opinions — makes them entertaining and shareable, driving viral adoption. The cross-tool support (Claude Code, Cursor, Copilot, Aider, Windsurf, Kimi) via automated conversion scripts makes it the most portable agent persona library available.

---

## 14. [gitagent](https://github.com/open-gitagent/gitagent)
> A framework-agnostic, git-native standard for defining AI agents.

**Language:** TypeScript  |  **Stars:** 2,541  |  **Forks:** 307  |  **Score:** 3,368  |  **Created:** 2026-02-24

**Background:** Gitagent by open-gitagent is a framework-agnostic, git-native standard for defining AI agents. The core idea: drop an `agent.yaml` manifest and a `SOUL.md` identity file into any git repo, and it becomes a portable agent definition that can be exported to Claude Code, OpenAI, LangChain, CrewAI, AutoGen, or any other framework via adapters.

**Problem it solves:** Every AI framework has its own agent definition structure with no universal, portable format. Moving an agent from Claude Code to LangChain requires rewriting the entire definition. Gitagent provides a standard file-system layout that any framework can consume through adapters, with version control, branching, and diffing built in.

**Why another one?** The git-native approach is the key innovation — agents get versioning, branching, PRs, and collaboration for free. First-class compliance support (FINRA, SEC, segregation of duties via DUTIES.md) targets regulated industries where other agent frameworks have no story. The composable architecture allows agents to extend and delegate to sub-agents.

---

## 15. [dexter](https://github.com/virattt/dexter)
> An autonomous agent for deep financial research.

**Language:** TypeScript  |  **Stars:** 20,975  |  **Forks:** 2,519  |  **Score:** 3,062  |  **Created:** 2025-10-14

**Background:** Dexter by virattt is an autonomous financial research agent that decomposes complex financial questions into structured research plans, executes them using live market data, validates its own work, and iterates until it has confident, data-backed answers. Built with Bun and supporting multiple LLM providers, it includes an evaluation suite with LLM-as-judge scoring.

**Problem it solves:** Financial research requires navigating income statements, balance sheets, cash flow data, and market context — a process that is time-consuming and error-prone when done manually. Dexter automates the entire research cycle with intelligent task planning, autonomous tool selection, and self-validation with loop detection.

**Why another one?** Dexter's self-reflection and self-validation loop distinguishes it from simpler financial query tools. The built-in evaluation suite with LangSmith tracking provides measurable accuracy, and support for WhatsApp integration makes research results accessible beyond the terminal. Multi-provider LLM support (OpenAI, Anthropic, Google, Ollama) avoids vendor lock-in.

---

## 16. [HolyClaude](https://github.com/CoderLuii/HolyClaude)
> AI coding workstation: Claude Code + web UI + 7 AI CLIs + headless browser + 50+ tools.

**Language:** Dockerfile  |  **Stars:** 1,856  |  **Forks:** 207  |  **Score:** 3,042  |  **Created:** 2026-03-22

**Background:** HolyClaude by CoderLuii is a Docker-based AI development workstation that packages Claude Code, a web UI, a headless browser, Playwright, 7 AI CLIs, and 50+ development tools into a single container. Released five days ago, it has gathered 1,856 stars from developers tired of manually solving Docker configuration problems for Claude Code.

**Problem it solves:** Running Claude Code in Docker triggers a cascade of configuration issues — Chromium fails because shared memory is 64MB, Xvfb is not configured, container UID mismatches cause permission errors, and Claude Code's installer hangs in root-owned directories. HolyClaude solves every one of these problems in a pre-built container.

**Why another one?** HolyClaude works with existing Claude Code subscriptions — Max, Pro, or API key — without requiring a separate service. The container has been battle-tested daily on a real server, with every Docker edge case diagnosed and fixed. The one-command `docker compose up` setup eliminates hours of manual configuration.

---

## 17. [deer-flow](https://github.com/bytedance/deer-flow)
> An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.

**Language:** Python  |  **Stars:** 58,942  |  **Forks:** 7,410  |  **Score:** 3,039  |  **Created:** 2025-05-07

**Background:** DeerFlow 2.0 by ByteDance is a ground-up rewrite of the original deep research framework, now positioned as an open-source super agent harness. With nearly 59,000 stars and an official website at deerflow.tech, it orchestrates sub-agents, persistent memory, and sandboxes for tasks spanning minutes to hours, with Claude Code integration and support for Doubao, DeepSeek, and Kimi models.

**Problem it solves:** Complex tasks that span research, code generation, and content creation require orchestrating multiple tools and maintaining context across long-running sessions. DeerFlow provides a unified harness with sandbox mode, MCP server support, IM channel integration, and LangSmith/Langfuse tracing for production observability.

**Why another one?** DeerFlow's backing by ByteDance provides engineering resources and sustained investment — the 2.0 ground-up rewrite shares no code with v1. The InfoQuest integration (BytePlus's intelligent search and crawling toolset) adds enterprise-grade information retrieval, and Docker-first deployment makes production use straightforward.

---

## 18. [carbonyl](https://github.com/fathyb/carbonyl)
> Chromium running inside your terminal.

**Language:** Rust  |  **Stars:** 18,190  |  **Forks:** 474  |  **Score:** 2,781  |  **Created:** 2023-01-20

**Background:** Carbonyl by fathyb renders Chromium directly inside a terminal emulator, providing a full web browsing experience in text mode. With over 18,000 stars since its January 2023 launch, it continues to trend as developers discover new use cases for terminal-based web browsing, particularly in server and container environments.

**Problem it solves:** Accessing web content from headless servers, SSH sessions, or minimal container environments typically requires either forwarding a display server or using text-only browsers that cannot render modern web applications. Carbonyl provides a full Chromium engine that renders directly to the terminal.

**Why another one?** Unlike text-mode browsers (lynx, w3m) that parse HTML into text, Carbonyl runs the actual Chromium rendering engine and converts the output to terminal graphics. This means full JavaScript execution, CSS rendering, and modern web application support — capabilities no text browser can match.

---

## 19. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Language:** Shell  |  **Stars:** 110,318  |  **Forks:** 18,343  |  **Score:** 2,770  |  **Created:** 2025-02-22

**Background:** Claude Code by Anthropic is the official agentic coding tool that lives in your terminal, now surpassing 110,000 stars. Available via native installers for macOS, Linux, and Windows (plus Homebrew and WinGet), it supports terminal, IDE, and GitHub integration via @claude mentions. The recent addition of a plugin marketplace has catalyzed the ecosystem visible throughout this report.

**Problem it solves:** Developers spend significant time on routine coding tasks — navigating codebases, writing boilerplate, managing git workflows, and debugging. Claude Code automates these through natural language commands while maintaining the developer's terminal-native workflow, eliminating the context switch to browser-based AI tools.

**Why another one?** As Anthropic's official tool, Claude Code has direct access to the latest Claude models and features. The plugin ecosystem (visible in today's trending list) has created a network effect — the more skills, hooks, and agents the community builds, the more valuable the platform becomes for every user.

---

## 20. [twenty](https://github.com/twentyhq/twenty)
> Building a modern alternative to Salesforce, powered by the community.

**Language:** TypeScript  |  **Stars:** 43,670  |  **Forks:** 5,851  |  **Score:** 2,708  |  **Created:** 2022-12-01

**Background:** Twenty is the number-one open-source CRM, building a modern alternative to Salesforce with community power. At over 43,000 stars and three years of development, it provides customizable objects and fields, workflow automation with triggers and actions, email/calendar integration, AI agents, and MCP support.

**Problem it solves:** CRMs are expensive and lock in customer data to justify price hikes. Twenty provides a self-hostable, open-source alternative with modern UX patterns inspired by Notion, Airtable, and Linear — including filters, kanban views, custom roles, and workflow automation — without vendor lock-in.

**Why another one?** Twenty's combination of open-source licensing, modern UX, and a three-year maturity track record positions it uniquely against both legacy CRMs (Salesforce, HubSpot) and newer closed-source alternatives. The plugin ecosystem and community of hundreds of contributors ensure it evolves with real user needs rather than enterprise sales targets.

---

## 21. [onyx](https://github.com/onyx-dot-app/onyx)
> Open Source AI Platform - AI Chat with advanced features that works with every LLM.

**Language:** Python  |  **Stars:** 25,588  |  **Forks:** 3,411  |  **Score:** 2,646  |  **Created:** 2023-04-27

**Background:** Onyx is an open-source AI platform that serves as the application layer for LLMs, providing RAG, web search, code execution, file creation, deep research, and custom agents with 50+ indexing connectors. Deployable with a single command, it supports both standard and lite modes, with Docker, Kubernetes, and Helm/Terraform deployment options.

**Problem it solves:** Building a production-ready AI application requires assembling RAG pipelines, search integrations, code sandboxes, and agent frameworks from scratch. Onyx provides all of these as a cohesive platform that works with any LLM provider — self-hosted (Ollama, vLLM) or proprietary (Anthropic, OpenAI, Gemini).

**Why another one?** Onyx's deep research capability tops its own public benchmark leaderboard (as of February 2026), providing measurable quality rather than just feature claims. The lite deployment mode (under 1GB memory) makes it accessible for testing, while the full stack scales to enterprise with MCP actions, voice mode, and image generation.

---

## 22. [claude-subconscious](https://github.com/letta-ai/claude-subconscious)
> Give Claude Code a subconscious.

**Language:** TypeScript  |  **Stars:** 2,583  |  **Forks:** 184  |  **Score:** 2,610  |  **Created:** 2026-01-14

**Background:** Claude Subconscious by Letta AI is a background agent that watches Claude Code sessions, reads your codebase, builds persistent memory over time, and whispers guidance back before each prompt. Built on the Letta Code SDK, it demonstrates persistent, cross-session agent memory with real tool access (Read, Grep, Glob, web search).

**Problem it solves:** Claude Code forgets everything between sessions — every new session starts from zero context. Claude Subconscious maintains persistent memory across sessions and projects, surfacing relevant context, patterns, and reminders automatically without blocking the main workflow.

**Why another one?** The "subconscious" metaphor captures the design perfectly — it never blocks, runs in the background, and whispers rather than commands. Using Letta's Conversations feature, a single agent serves multiple Claude Code sessions in parallel with shared memory. Nothing is written to CLAUDE.md, keeping the memory layer invisible to the user.

---

## 23. [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
> An AI SKILL that provides design intelligence for building professional UI/UX multi-platform applications.

**Language:** Python  |  **Stars:** 60,341  |  **Forks:** 5,996  |  **Score:** 2,600  |  **Created:** 2025-11-30

**Background:** UI UX Pro Max by NextLevelBuilder is an AI skill providing design intelligence for building professional UI/UX across multiple platforms and frameworks. With 161 reasoning rules, 67 UI styles, and over 60,000 stars, it has established itself as the leading design intelligence layer for AI coding agents. Version 2.0 introduced an AI-powered Design System Generator.

**Problem it solves:** AI coding agents produce functional but visually poor interfaces because they lack design reasoning. UI UX Pro Max provides structured design intelligence — layout patterns, color theory, typography rules, responsive breakpoints, and accessibility guidelines — that agents apply automatically when building UI components.

**Why another one?** The v2.0 Design System Generator analyzes project requirements and generates complete, tailored design systems in seconds — from color palettes and typography scales to component hierarchies and conversion-optimized layouts. The 161 reasoning rules encode design expertise that no generic prompt can replicate.

---

## 24. [strix](https://github.com/usestrix/strix)
> Open-source AI hackers to find and fix your app's vulnerabilities.

**Language:** Python  |  **Stars:** 23,220  |  **Forks:** 2,510  |  **Score:** 2,564  |  **Created:** 2025-08-05

**Background:** Strix provides autonomous AI agents that act like real hackers — running code dynamically, finding vulnerabilities, and validating them through actual proof-of-concepts. With over 23,000 stars and CI/CD pipeline integration, it has matured into a developer-first security testing platform with auto-fix capabilities and compliance reports.

**Problem it solves:** Security testing is either slow and expensive (manual pentesting) or unreliable (static analysis with false positives). Strix agents run your code dynamically, discover real vulnerabilities, and validate them with reproducible PoCs — providing pentesting results in hours rather than weeks with actionable remediation.

**Why another one?** Strix validates findings with actual proof-of-concept exploits rather than pattern-matching, dramatically reducing false positives. The GitHub Actions integration runs security scans on every pull request, blocking insecure code before it reaches production. The one-click autofix generates ready-to-merge PRs for discovered vulnerabilities.

---

## 25. [gstack](https://github.com/garrytan/gstack)
> Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA.

**Language:** TypeScript  |  **Stars:** 64,509  |  **Forks:** 8,786  |  **Score:** 2,422  |  **Created:** 2026-03-11

**Background:** Gstack by Garry Tan (Y Combinator CEO) packages 23 opinionated workflow skills for Claude Code as slash commands. In just sixteen days since release, it has amassed over 64,000 stars. Tan reports shipping 600,000+ lines of production code in the last 60 days (10,000-20,000 lines per day) while running YC full-time, using these exact tools.

**Problem it solves:** A single Claude Code session treats every request uniformly with no role-specific depth. Gstack partitions workflows into specialist modes — `/plan-ceo-review` rethinks product vision, `/plan-eng-review` locks architecture, `/design-review` evaluates UI, `/qa` opens a real browser for testing, and `/ship` handles the full release process.

**Why another one?** The substance is in the opinionated defaults backed by twenty years of product building experience (Palantir, Posterous, Y Combinator). Gstack provides a complete ready-to-use team of 23 specialists with eight power tools, lowering the barrier from "build your own agent workflow" to "install and type a slash command." The MIT license and Markdown-only implementation make it trivially forkable.

---

> **Day's theme:** The Claude Code ecosystem reaches critical mass as the platform itself trends alongside 15+ projects built on top of it — from orchestration layers and persistent memory to game studios, financial research agents, and entrepreneurship coaches — while adjacent categories (OCR, deepfakes, CRM, security testing, terminal browsers) demonstrate that AI-augmented development tools are pulling the entire open-source landscape into their orbit.
