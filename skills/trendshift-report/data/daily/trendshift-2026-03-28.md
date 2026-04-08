# Trendshift Report — 2026-03-28
**Total:** 25 repositories

---

## 1. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 135,699  |  **Forks:** 11,370  |  **Score:** 13,235  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent is a complete software development workflow for coding agents, now surpassing 135,000 stars. It enforces a disciplined process where the agent teases out a spec, presents it in digestible chunks, builds an implementation plan, then launches subagent-driven development with built-in review cycles. Available across Claude Code, Cursor, Codex, OpenCode, and Gemini CLI, it has become the de facto standard for structured agent-driven development.

**Problem it solves:** Coding agents left unsupervised jump straight into writing code without understanding the full problem, producing poorly planned implementations. Superpowers enforces a structured spec-plan-implement-review workflow with true red/green TDD, YAGNI principles, and bite-sized tasks — ensuring agents work methodically rather than producing spaghetti code.

**Why another one?** Superpowers focuses on development methodology rather than tool orchestration. Its composable skills trigger automatically without special invocation, and the subagent-driven development model allows autonomous work for hours at a time without drifting from the agreed plan. At 135,000 stars, it has proven its approach at scale across every major AI coding platform.

---

## 2. [Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam)
> real time face swap and one-click video deepfake with only a single image

**Language:** Python  |  **Stars:** 88,592  |  **Forks:** 12,850  |  **Score:** 12,710  |  **Created:** 2023-09-24

**Background:** Deep-Live-Cam 2.1 is a real-time face swap and video deepfake tool that requires only a single image to operate. Originally launched in September 2023, it has grown to nearly 89,000 stars and continues to trend strongly. The tool supports live streaming, video processing, and real-time face mapping across multiple subjects simultaneously.

**Problem it solves:** Creating face swaps traditionally requires extensive video editing skills, multiple reference images, and significant processing time. Deep-Live-Cam reduces this to three clicks — select a face, choose a camera, and press live — enabling real-time face swapping for content creation, live performances, and creative projects.

**Why another one?** The real-time capability is the core differentiator. While most deepfake tools process video offline, Deep-Live-Cam operates at live-streaming speeds with features like mouth masking for accurate lip movement and multi-face mapping. The v2.7 beta adds 30+ extra features over the open-source version, including pre-built binaries for non-technical users.

---

## 3. [last30days-skill](https://github.com/mvanhorn/last30days-skill)
> AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

**Language:** Python  |  **Stars:** 18,665  |  **Forks:** 1,503  |  **Score:** 9,517  |  **Created:** 2026-01-23

**Background:** last30days is a Claude Code skill (v2.9.5) that researches any topic across Reddit, X, YouTube, Hacker News, Polymarket, and the broader web, then synthesizes a grounded summary. Installable via the plugin marketplace, it has accumulated over 18,000 stars since its January 2026 launch, reflecting strong demand for research automation within coding agent workflows.

**Problem it solves:** Staying current on fast-moving topics requires manually checking multiple platforms — Reddit threads, X posts, YouTube videos, HN discussions, and prediction markets. last30days automates this cross-platform research and produces a single synthesized summary with source attribution.

**Why another one?** As a native Claude Code skill installed via the plugin marketplace, last30days integrates directly into the developer's existing workflow without separate tools or APIs. Its coverage of prediction markets (Polymarket) alongside traditional social platforms provides a unique signal about market consensus that pure social media aggregators miss.

---

## 4. [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)
> Teams-first Multi-agent orchestration for Claude Code

**Language:** TypeScript  |  **Stars:** 24,305  |  **Forks:** 2,215  |  **Score:** 7,762  |  **Created:** 2026-01-09

**Background:** oh-my-claudecode (OMC) by Yeachan Heo is a multi-agent orchestration layer for Claude Code with zero learning curve. Available as both an npm package and a Claude Code plugin, it provides team orchestration, autopilot mode, and cross-provider advisor capabilities. Translated into seven languages, it has grown to over 24,000 stars and spawned a companion project (oh-my-codex) for OpenAI Codex CLI.

**Problem it solves:** Running multiple Claude Code sessions for complex tasks requires manual coordination — splitting work, tracking progress, and merging results. OMC automates this with team orchestration that launches parallel workers via tmux or native in-session workflows, plus an autopilot mode that handles end-to-end task execution.

**Why another one?** OMC's "zero learning curve" philosophy means users can type `/autopilot "build a REST API"` and get results immediately without learning Claude Code internals. The dual-surface design (terminal CLI and in-session skills) covers both automation scripts and interactive use, and the cross-provider `/ask` command lets users query Codex, Gemini, or other providers from within Claude Code.

---

## 5. [onyx](https://github.com/onyx-dot-app/onyx)
> Open Source AI Platform - AI Chat with advanced features that works with every LLM

**Language:** Python  |  **Stars:** 24,473  |  **Forks:** 3,279  |  **Score:** 6,528  |  **Created:** 2023-04-27

**Background:** Onyx is an open-source AI platform that serves as the application layer for LLMs, providing a feature-rich interface that anyone can self-host. With over 24,000 stars and nearly three years of development, it offers agentic RAG, deep research, custom agents, web search, code execution, and artifact generation — all deployable with a single curl command.

**Problem it solves:** Organizations need a unified AI interface that connects to their internal data while supporting multiple LLM providers. Onyx provides over 50 indexing connectors, agentic RAG that tops deep research benchmarks, and enterprise features like custom agents, MCP actions, and voice mode — all self-hosted for data sovereignty.

**Why another one?** Onyx's breadth of features in a single self-hosted package is unmatched. While most open-source AI chat tools focus on conversation, Onyx adds deep research, code execution, image generation, file creation, and workflow automation. Its provider-agnostic design supports both self-hosted models (Ollama, vLLM) and proprietary APIs (OpenAI, Anthropic, Gemini).

---

## 6. [ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)
> Clone any website with one command using AI coding agents

**Language:** TypeScript  |  **Stars:** 7,790  |  **Forks:** 1,037  |  **Score:** 6,353  |  **Created:** 2026-03-13

**Background:** AI Website Cloner Template by JCodesMore is a reusable template for reverse-engineering any website into a clean Next.js codebase using AI coding agents. Released just two weeks ago, it has already gathered nearly 8,000 stars. The `/clone-website` skill runs a multi-phase pipeline — reconnaissance, foundation, component specs, and parallel builders — to reconstruct every section of a target site.

**Problem it solves:** Recreating an existing website's design in a modern framework requires painstaking manual inspection of styles, assets, layout, and interactions. This template automates the entire process — from screenshot-based design token extraction through component spec generation to parallel section building — reducing days of work to a single command.

**Why another one?** The multi-agent pipeline architecture is the differentiator. Rather than a simple scraper, the cloner dispatches parallel builders after writing detailed component specs with exact computed CSS values, states, and behaviors. It supports 13 AI coding agents (Claude Code, Codex, Cursor, Copilot, and more) and outputs a clean Next.js 16 + Tailwind CSS v4 codebase.

---

## 7. [twenty](https://github.com/twentyhq/twenty)
> Building a modern alternative to Salesforce, powered by the community.

**Language:** TypeScript  |  **Stars:** 43,594  |  **Forks:** 5,820  |  **Score:** 6,248  |  **Created:** 2022-12-01

**Background:** Twenty is the number-one open-source CRM, building a modern alternative to Salesforce with community-driven development. With over 43,000 stars and three years of active development, it offers customizable objects and fields, workflow automation, email and calendar integration, and permission management with custom roles.

**Problem it solves:** CRMs are expensive, and vendors use locked-in customer data to hike prices. Twenty provides a fully open-source alternative that organizations can self-host, customize, and extend — eliminating vendor lock-in while offering a modern UX inspired by tools like Notion, Airtable, and Linear.

**Why another one?** Twenty's ground-up rebuild avoids the legacy baggage of older open-source CRMs. Its data model is fully customizable (not just configurable), the workflow automation supports triggers and actions, and the Figma design system ensures a polished experience. Hundreds of community contributors provide the momentum that solo-maintained alternatives cannot sustain.

---

## 8. [paperclip](https://github.com/paperclipai/paperclip)
> Open-source orchestration for zero-human companies

**Language:** TypeScript  |  **Stars:** 46,219  |  **Forks:** 7,290  |  **Score:** 5,406  |  **Created:** 2026-03-02

**Background:** Paperclip is a Node.js server and React UI that orchestrates a team of AI agents to run a business autonomously. Launched less than a month ago, it has already surpassed 46,000 stars. It provides org charts, budgets, governance, goal alignment, and agent coordination — managing business goals rather than pull requests. A forthcoming "Clipmart" marketplace will offer downloadable company templates.

**Problem it solves:** Coordinating many different AI agents (Claude Code, Codex, Cursor, OpenClaw) toward a common business goal requires manual oversight across dozens of simultaneous sessions. Paperclip provides a unified dashboard for defining goals, hiring agent teams, setting budgets, approving strategies, and monitoring autonomous 24/7 operations.

**Why another one?** Paperclip operates at the company level rather than the project level. While tools like OpenClaw are individual "employees," Paperclip is the "company" — providing organizational structure, cost monitoring, budget enforcement, and goal alignment across multiple agents and providers. The phone-friendly dashboard enables management of autonomous businesses from anywhere.

---

## 9. [chandra](https://github.com/datalab-to/chandra)
> OCR model that handles complex tables, forms, handwriting with full layout.

**Language:** Python  |  **Stars:** 8,339  |  **Forks:** 851  |  **Score:** 5,072  |  **Created:** 2025-10-08

**Background:** Chandra OCR 2 by Datalab is a state-of-the-art OCR model that converts images and PDFs into structured HTML, Markdown, or JSON while preserving layout information. The March 2026 release of version 2 brought significant improvements to math, tables, layout, and multilingual OCR, supporting over 90 languages with top benchmark scores.

**Problem it solves:** Extracting structured data from documents with complex tables, handwritten text, mathematical formulas, and multi-column layouts remains a challenge for traditional OCR tools. Chandra handles all of these while preserving the original layout, reconstructing forms with checkboxes, and extracting images with captions.

**Why another one?** Chandra 2 tops the external olmocr benchmark and provides significant multilingual improvements over competitors. It runs locally via HuggingFace or a vLLM server, avoiding cloud dependencies. The dual inference mode (local and remote) and CLI-first design make it immediately usable for document processing pipelines without API costs.

---

## 10. [InsForge](https://github.com/InsForge/InsForge)
> Give agents everything they need to ship fullstack apps. The backend built for agentic development.

**Language:** TypeScript  |  **Stars:** 7,244  |  **Forks:** 568  |  **Score:** 4,741  |  **Created:** 2025-07-29

**Background:** InsForge is a backend development platform built specifically for AI coding agents and AI code editors. It exposes backend primitives — databases, auth, storage, and functions — through a semantic layer that agents can understand, reason about, and operate end to end. With over 7,000 stars, it bridges the gap between what agents can generate and what backends actually need.

**Problem it solves:** AI coding agents can generate frontend code effectively but struggle with backend infrastructure — database schemas, authentication flows, storage configuration, and serverless functions require contextual understanding that agents lack. InsForge provides a semantic abstraction layer that makes these primitives agent-comprehensible.

**Why another one?** InsForge is purpose-built for agentic development rather than adapted from human-facing tools. The semantic layer translates backend concepts into a format agents can reason about, and the MCP Server integration allows agents to connect directly. Docker-based local setup and Apache 2.0 licensing make it accessible for both individual developers and teams.

---

## 11. [insanely-fast-whisper](https://github.com/Vaibhavs10/insanely-fast-whisper)
> Insanely fast audio transcription powered by Transformers, Optimum & Flash Attention

**Language:** Jupyter Notebook  |  **Stars:** 12,360  |  **Forks:** 907  |  **Score:** 4,350  |  **Created:** 2023-10-10

**Background:** Insanely Fast Whisper is an opinionated CLI for on-device audio transcription using OpenAI's Whisper models, powered by Hugging Face Transformers, Optimum, and Flash Attention. It can transcribe 150 minutes of audio in under 98 seconds on an Nvidia A100, and continues to trend with over 12,000 stars since its October 2023 launch.

**Problem it solves:** Whisper transcription without optimization is painfully slow — over 31 minutes for 150 minutes of audio using standard FP32 inference. Insanely Fast Whisper applies batching, FP16, and Flash Attention 2 to achieve the same transcription in under 2 minutes, making real-time and near-real-time transcription practical.

**Why another one?** The CLI-first approach makes it immediately usable via pipx without any setup beyond installation. Support for both Whisper Large v3 and distil-whisper models provides a speed-accuracy tradeoff, and Flash Attention 2 integration delivers performance that neither Faster Whisper nor standard Transformers can match on supported hardware.

---

## 12. [dexter](https://github.com/virattt/dexter)
> An autonomous agent for deep financial research

**Language:** TypeScript  |  **Stars:** 20,975  |  **Forks:** 2,519  |  **Score:** 4,081  |  **Created:** 2025-10-14

**Background:** Dexter is an autonomous financial research agent that performs analysis using task planning, self-reflection, and real-time market data. Built with Bun and TypeScript, it decomposes complex financial questions into structured research plans, executes them using live data (income statements, balance sheets, cash flows), and validates its own work with built-in loop detection and step limits.

**Problem it solves:** Financial research requires synthesizing data from multiple sources — income statements, balance sheets, cash flow statements, and web sources — while maintaining analytical rigor. Dexter automates this end-to-end with intelligent task planning that selects the right tools, gathers data, checks its work, and iterates until confident.

**Why another one?** Dexter's self-validation loop distinguishes it from simple query-response financial tools. The agent checks its own work and iterates until tasks are complete, with safety features preventing runaway execution. Its evaluation suite with LLM-as-judge scoring provides measurable quality benchmarks, and the WhatsApp integration enables research on the go.

---

## 13. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 71,854  |  **Forks:** 11,138  |  **Score:** 3,992  |  **Created:** 2025-10-13

**Background:** Agency Agents by Mark Sitarzewski provides a collection of meticulously crafted AI agent personas for professional roles. Now at over 71,000 stars (up from 60,000 just days ago), its growth continues to accelerate. Each agent has defined personality traits, specialized expertise, production-ready workflows, and measurable success metrics covering engineering, marketing, design, and operations divisions.

**Problem it solves:** Teams adopting AI agents need role-specific system prompts, workflows, and deliverable definitions for every business function. Agency Agents provides these ready-made with deep domain expertise — not generic prompt templates — eliminating weeks of prompt engineering per role.

**Why another one?** The personality-driven approach with unique voices and communication styles makes agents entertaining and shareable, driving viral adoption. Multi-tool support (Claude Code, Cursor, Aider, Windsurf, Gemini CLI, Copilot, and more) via conversion scripts means the agents work everywhere, and the breadth of covered roles positions it as an agency-in-a-box.

---

## 14. [agentscope](https://github.com/agentscope-ai/agentscope)
> Build and run agents you can see, understand and trust.

**Language:** Python  |  **Stars:** 22,999  |  **Forks:** 2,370  |  **Score:** 3,792  |  **Created:** 2024-01-12

**Background:** AgentScope is a production-ready agent framework backed by an arXiv paper (2402.14034), designed for increasingly agentic LLMs. Rather than constraining models with strict prompts and opinionated orchestrations, it leverages models' native reasoning and tool use abilities. With nearly 23,000 stars, it provides built-in ReAct agents, tools, skills, memory, planning, realtime voice, and model finetuning support.

**Problem it solves:** Building production-grade AI agents requires integrating tools, memory, human-in-the-loop steering, multi-agent orchestration, and observability — a stack that most teams assemble from disparate libraries. AgentScope provides all of these in a single, extensible framework with built-in support for MCP, A2A, and OpenTelemetry.

**Why another one?** AgentScope's design philosophy of working with rising model capability rather than constraining it sets it apart. The framework provides essential abstractions that become more powerful as models improve, rather than opinionated orchestrations that may become obsolete. Built-in finetuning support and serverless/K8s deployment options make it production-ready out of the box.

---

## 15. [NOMAD](https://github.com/mauriceboe/NOMAD)
> A self-hosted travel/trip planner with real-time collaboration, interactive maps, PWA support, SSO, budgets, packing lists, and more.

**Language:** TypeScript  |  **Stars:** 1,308  |  **Forks:** 106  |  **Score:** 3,717  |  **Created:** 2026-03-19

**Background:** NOMAD (also known as TREK) by Maurice Boe is a self-hosted, real-time collaborative travel planner with interactive Leaflet maps, drag-and-drop day planning, budget tracking, packing lists, and PWA support. Released just nine days ago, it has already gathered over 1,300 stars and offers a live demo that resets hourly.

**Problem it solves:** Trip planning is typically fragmented across multiple apps — Google Maps for routes, spreadsheets for budgets, shared docs for itineraries, and messaging apps for coordination. NOMAD consolidates all of these into a single self-hosted application with real-time WebSocket sync for collaborative planning.

**Why another one?** The self-hosted approach gives users full control over their travel data, unlike cloud-based alternatives. NOMAD's PWA support with offline caching makes it usable during travel when connectivity is unreliable, and features like route optimization, weather forecasts (via Open-Meteo, no API key needed), bag weight tracking, and PDF export go well beyond basic trip planning tools.

---

## 16. [Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills)
> A collection of Awesome Finance Agent Skills for free and easy to start

**Language:** Python  |  **Stars:** 1,593  |  **Forks:** 205  |  **Score:** 3,506  |  **Created:** 2026-01-31

**Background:** Awesome Finance Skills by RKiding is a plug-and-play skill collection that transforms AI agents into financial analysts. It includes eight specialized skills — real-time news aggregation (10+ sources including Polymarket), stock data (A-Share, HK, and US markets), FinBERT sentiment analysis, Kronos time-series forecasting, logic chain visualization, and professional report generation.

**Problem it solves:** AI agents lack domain-specific financial capabilities out of the box — they cannot access real-time market data, perform sentiment analysis on financial news, or generate logic chain diagrams explaining market impacts. Awesome Finance Skills adds these capabilities with one-step installation via `npx skills`.

**Why another one?** The bilingual (English/Chinese) support and coverage of both Western and Chinese financial markets (A-Shares, HK stocks) set it apart from English-only alternatives. The live demo on DeepEar, logic chain visualization generating Draw.io XML, and support for six agent frameworks (Claude Code, Codex, OpenCode, Antigravity, OpenClaw, Cursor) make it unusually accessible.

---

## 17. [claude-howto](https://github.com/luongnv89/claude-howto)
> A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value.

**Language:** Python  |  **Stars:** 17,870  |  **Forks:** 2,125  |  **Score:** 3,462  |  **Created:** 2025-11-07

**Background:** Claude How To by luongnv89 is a structured, visual, example-driven guide to mastering Claude Code. Available in English, Vietnamese, and Chinese, it has grown to nearly 18,000 stars with 10 tutorial modules, copy-paste configs, Mermaid diagrams, and a guided learning path from beginner to power user in 11-13 hours. It includes built-in self-assessment via `/self-assessment` and `/lesson-quiz` skills.

**Problem it solves:** Claude Code's official documentation describes features but does not show how to combine them effectively. Users who installed Claude Code and ran a few prompts have no clear learning path for hooks, skills, subagents, MCP servers, and multi-agent orchestration — leaving 90% of the tool's power unused.

**Why another one?** Unlike official docs that are reference-oriented, Claude How To provides a progressive learning path with visual Mermaid diagrams showing how each feature works internally. The production-ready templates, interactive quizzes, and time-estimated roadmap make it a structured course rather than yet another feature reference.

---

## 18. [VibeVoice](https://github.com/microsoft/VibeVoice)
> Open-Source Frontier Voice AI

**Language:** Python  |  **Stars:** 36,265  |  **Forks:** 4,144  |  **Score:** 3,234  |  **Created:** 2025-08-25

**Background:** VibeVoice by Microsoft is an open-source frontier voice AI framework covering both text-to-speech (TTS) and automatic speech recognition (ASR). The ASR model handles 60-minute long-form audio in a single pass, generating structured transcriptions with speaker identification, timestamps, and content — supporting over 50 languages. The TTS models include a real-time 0.5B streaming model with multilingual voices.

**Problem it solves:** Voice AI requires separate solutions for speech recognition and synthesis, each with their own limitations — short audio windows, lack of speaker diarization, and limited language support. VibeVoice provides unified, frontier-quality voice AI with 60-minute single-pass ASR, user-customizable context, and streaming TTS in nine languages.

**Why another one?** Microsoft's institutional backing ensures sustained development and integration with the broader ML ecosystem (VibeVoice-ASR is now part of Hugging Face Transformers v5.3.0). The unified framework for both TTS and ASR, combined with the 60-minute single-pass capability and community adoption (Vibing voice input app), positions it as the open-source voice AI reference implementation.

---

## 19. [expect](https://github.com/millionco/expect)
> Expect tests your app in a browser so you don't have to.

**Language:** TypeScript  |  **Stars:** 3,060  |  **Forks:** 125  |  **Score:** 3,127  |  **Created:** 2026-03-12

**Background:** Expect by Million is an AI-powered browser testing tool that automates end-to-end testing by interacting with your application in a real browser. Released just over two weeks ago, it has gathered over 3,000 stars. The tool observes your app's behavior and generates tests automatically, eliminating the manual test-writing bottleneck.

**Problem it solves:** Writing and maintaining end-to-end browser tests is tedious and brittle — CSS selectors break, UI changes invalidate tests, and the effort of writing tests often exceeds the time saved by automation. Expect uses AI to understand page semantics and test applications the way a human would, without fragile selectors.

**Why another one?** Expect's AI-first approach means tests understand what the application does rather than relying on implementation details like element IDs or class names. This semantic understanding makes tests inherently more resilient to UI changes, addressing the primary reason teams abandon browser testing.

---

## 20. [gstack](https://github.com/garrytan/gstack)
> Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**Language:** TypeScript  |  **Stars:** 64,509  |  **Forks:** 8,786  |  **Score:** 2,997  |  **Created:** 2026-03-11

**Background:** Gstack by Garry Tan (Y Combinator CEO) packages 23 opinionated workflow skills for Claude Code as slash commands. In just 17 days since release, it has amassed over 64,000 stars — a remarkable growth trajectory driven by Tan's high profile and the project's practical utility. Tan reports shipping 600,000+ lines of production code in 60 days using these tools while running YC full-time.

**Problem it solves:** A single Claude Code session treats every request uniformly, with no role-specific depth. Gstack partitions workflows into specialist modes — `/plan-ceo-review` rethinks the product vision, `/plan-eng-review` locks architecture, `/design-review` evaluates UI decisions, `/qa` opens a real browser for testing, and `/ship` handles the entire release process.

**Why another one?** The credibility of YC's CEO sharing his personal setup with claimed 10,000-20,000 lines per day output drives initial adoption. Beyond the celebrity factor, gstack provides a complete ready-to-use team of 23 specialists plus 8 power tools, lowering the barrier from "build your own agent workflow" to "install and type a slash command." MIT licensed and genuinely used daily by its creator.

---

## 21. [skills](https://github.com/slavingia/skills)
> Claude Code skills based on The Minimalist Entrepreneur by Sahil Lavingia

**Language:** N/A  |  **Stars:** 6,804  |  **Forks:** 616  |  **Score:** 2,847  |  **Created:** 2026-03-23

**Background:** Minimalist Entrepreneur Skills by Sahil Lavingia (Gumroad founder) is a set of 10 Claude Code skills based on his book "The Minimalist Entrepreneur." Released just five days ago, it has already gathered nearly 7,000 stars. Each skill maps to a chapter in the book's progression — from finding a community through validation, building, selling, pricing, and growing sustainably.

**Problem it solves:** Founders and solo entrepreneurs face business decisions that require frameworks they may not have internalized — when to validate vs. build, how to price, when to hire, and how to grow sustainably. These skills embed proven entrepreneurial methodology directly into Claude Code sessions, providing structured guidance at the moment of decision.

**Why another one?** The direct connection to a published, proven methodology gives these skills depth that generic business advice prompts lack. The `/processize` skill (turning a product idea into a manual process before writing code) and `/minimalist-review` (gut-checking any business decision) encode specific, opinionated frameworks rather than open-ended brainstorming.

---

## 22. [liteparse](https://github.com/run-llama/liteparse)
> A fast, helpful, and open-source document parser

**Language:** TypeScript  |  **Stars:** 3,755  |  **Forks:** 236  |  **Score:** 2,699  |  **Created:** 2026-02-09

**Background:** LiteParse by LlamaIndex (run-llama) is a standalone open-source PDF parsing tool focused on fast, lightweight local parsing. It provides spatial text parsing with bounding boxes using PDF.js, flexible OCR (built-in Tesseract.js, or pluggable HTTP servers), and screenshot generation for LLM agents. Available as both a CLI tool and an agent skill via `npx skills`.

**Problem it solves:** PDF parsing for AI pipelines often requires cloud services or heavyweight dependencies. LiteParse runs entirely locally with zero cloud dependencies, providing structured text extraction with bounding boxes, multi-format output (JSON, text), and page screenshots — everything an LLM agent needs to process documents.

**Why another one?** LiteParse's explicit focus on being "fast and light" positions it as the local-first complement to LlamaIndex's cloud-based LlamaParse. The standalone binary, brew installation, and agent skill integration make it immediately usable in any environment. For complex documents, users can upgrade to LlamaParse — a clean product ladder rather than feature bloat.

---

## 23. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Language:** Shell  |  **Stars:** 109,016  |  **Forks:** 18,014  |  **Score:** 2,360  |  **Created:** 2025-02-22

**Background:** Claude Code by Anthropic is the official agentic coding tool that lives in the terminal, understanding codebases and executing tasks through natural language commands. Surpassing 109,000 stars, it has become the foundation that an entire ecosystem of skills, plugins, and orchestration tools is built upon — as evidenced by the many Claude Code-focused projects on today's trending list.

**Problem it solves:** Developers spend significant time on routine coding tasks — reading unfamiliar code, handling git workflows, writing boilerplate, and debugging. Claude Code automates these through natural language, working directly in the terminal with full codebase context rather than requiring copy-paste into a separate chat window.

**Why another one?** As Anthropic's official tool, Claude Code benefits from first-party model integration and the rapidly growing plugin/skills ecosystem visible across this trending list. Its terminal-native design, IDE integration, and GitHub @claude tagging provide multiple entry points, and the extensibility via skills, hooks, and MCP has spawned a thriving community.

---

## 24. [firecrawl](https://github.com/firecrawl/firecrawl)
> The Web Data API for AI - Power AI agents with clean web data

**Language:** TypeScript  |  **Stars:** 104,287  |  **Forks:** 6,826  |  **Score:** 2,274  |  **Created:** 2024-04-15

**Background:** Firecrawl is the web data API for AI, providing search, scrape, and interact capabilities at scale. Surpassing 104,000 stars, it covers 96% of the web including JS-heavy pages with P95 latency of 3.4 seconds across millions of pages. It outputs LLM-ready markdown, structured JSON, and screenshots, and supports agent integration via MCP with a single command.

**Problem it solves:** AI agents need clean, structured web data, but scraping modern websites involves rotating proxies, handling JavaScript rendering, managing rate limits, and parsing diverse page layouts. Firecrawl handles all of this, delivering clean markdown and structured JSON that reduces token usage and improves AI application quality.

**Why another one?** Firecrawl's industry-leading 96% web coverage and 3.4-second P95 latency set the performance bar. The "interact" endpoint (click, scroll, write, wait before extracting) goes beyond static scraping, and the agent-ready MCP integration means AI agents can connect with a single command. Media parsing for PDFs and DOCX further extends its utility beyond web pages.

---

## 25. [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
> Turn Claude Code into a full game dev studio — 48 AI agents, 36 workflow skills, and a complete coordination system mirroring real studio hierarchy.

**Language:** Shell  |  **Stars:** 8,174  |  **Forks:** 1,230  |  **Score:** 2,268  |  **Created:** 2026-02-12

**Background:** Claude Code Game Studios by Donchitos transforms a single Claude Code session into a full game development studio with 49 specialized agents, 72 skills, 12 hooks, and 11 rules. The agents are organized into a three-tier studio hierarchy — Opus-powered directors, Sonnet-powered department leads, and Sonnet/Haiku-powered specialists — mirroring how real studios operate.

**Problem it solves:** Game development requires coordination across many disciplines — design, art, programming, audio, narrative, QA, and production. A single AI agent cannot effectively context-switch between creative direction, engine programming, sound design, and quality assurance. Game Studios provides dedicated agents for each role with workflows that enforce proper handoffs and quality gates.

**Why another one?** The studio hierarchy metaphor with 49 agents across three tiers goes well beyond proof-of-concept into production-grade complexity. The 72 slash commands cover every workflow phase from `/start` through `/design-system`, `/create-epics`, and `/story-done`. Model-tier assignment (Opus for directors, Sonnet for leads, Haiku for specialists) optimizes both quality and cost.

---

> **Day's theme:** The agentic ecosystem reaches escape velocity as specialized orchestration layers — from zero-human company management and multi-agent coding teams to financial research agents and game studio hierarchies — stack on top of foundational tools like Claude Code and Firecrawl, while methodology-first projects (Superpowers, gstack, Minimalist Entrepreneur skills) prove that structured workflows and opinionated defaults matter more than raw model capability for shipping production software.
