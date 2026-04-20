# Trendshift Report — 2026-04-19
**Total:** 25 repos

---

## 1. [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
> A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**Language:** N/A  |  **Stars:** 54,695  |  **Forks:** 4,633  |  **Score:** 10,427  |  **Created:** 2026-01-27

**Background:** Karpathy-Inspired Claude Code Guidelines packages four principles — Think Before Coding, Simplicity First, Surgical Changes, and Goal-Driven Execution — into a single CLAUDE.md drop-in file. A week after last week's trendshift appearance it has added over 40,000 stars, reflecting continued momentum behind authoritative, single-file guardrails for coding agents.

**Problem it solves:** LLM coding agents make silent assumptions, overcomplicate APIs, bloat abstractions, and change orthogonal code they do not fully understand. Those failure modes compound across sessions and erode codebase quality even when individual edits look acceptable.

**Why another one?** The project is uniquely derived from a specific, widely-circulated Karpathy post listing concrete agent failure modes, then translated into four actionable rules rather than abstract advice. A single file dropped into any project root applies the guardrails to every subsequent Claude Code session without configuration.

---

## 2. [hyperframes](https://github.com/heygen-com/hyperframes)
> Write HTML. Render video. Built for agents.

**Language:** HTML  |  **Stars:** 2,849  |  **Forks:** 217  |  **Score:** 8,398  |  **Created:** 2026-03-10

**Background:** HyperFrames by HeyGen is an open-source video rendering framework that lets AI agents author and render HTML-based video compositions. The `/hyperframes` slash command teaches Claude Code, Cursor, Gemini CLI, and Codex how to write correct compositions and GSAP animations, with a live npm package and demo GIF driving adoption.

**Problem it solves:** Programmatic video generation normally requires specialized tools like Remotion, After Effects, or FFmpeg templating, each with their own DSL. Agents struggle to produce correct output in these formats, and humans must still stitch the results into real workflows.

**Why another one?** HyperFrames makes HTML + CSS + GSAP the authoring surface — a format LLMs already know how to produce — and ships dedicated skills so the agent emits correct compositions on the first attempt. First-class agent integration (slash commands, cold-start and warm-start prompts) makes it the first video framework designed around agent workflows rather than humans.

---

## 3. [FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal)
> FinceptTerminal is a modern finance application offering advanced market analytics, investment research, and economic data tools, designed for interactive exploration and data-driven decision-making in a user-friendly environment.

**Language:** Python  |  **Stars:** 6,079  |  **Forks:** 964  |  **Score:** 6,341  |  **Created:** 2024-08-29

**Background:** Fincept Terminal is a state-of-the-art open-source financial intelligence platform built with C++20, Qt6, and Python 3.11+, offering CFA-level analytics, AI automation, and unlimited data connectivity. With over 6,000 stars and an AGPL-3.0 license, it positions itself as a grass-roots alternative to Bloomberg-style terminals.

**Problem it solves:** Professional financial terminals like Bloomberg and FactSet cost tens of thousands per seat annually, pricing out independent researchers, students, and small funds. Free tools exist for individual tasks but lack the integrated data, analytics, and workflow that justify a "terminal" experience.

**Why another one?** FinceptTerminal's combination of native C++/Qt performance with a Python extension layer gives it desktop-grade UI responsiveness plus scriptable analytics — a mix most open-source alternatives cannot match. The AGPL licensing plus commercial license option creates a sustainable path while keeping the platform genuinely open for research use.

---

## 4. [lingbot-map](https://github.com/Robbyant/lingbot-map)
> A feed-forward 3D foundation model for reconstructing scenes from streaming data

**Language:** Python  |  **Stars:** 2,419  |  **Forks:** 171  |  **Score:** 5,816  |  **Created:** 2026-04-15

**Background:** LingBot-Map is a Geometric Context Transformer for streaming 3D reconstruction, released with paper, HuggingFace and ModelScope weights, and a project site. Only four days old, it has already gathered over 2,400 stars on the strength of ~20 FPS streaming inference over sequences exceeding 10,000 frames.

**Problem it solves:** Existing 3D reconstruction pipelines either run iterative optimization (slow, offline) or sacrifice accuracy for speed. Long streaming sequences accumulate drift and cannot hold coordinate grounding without dense geometric cues, limiting applications in robotics, AR, and surveying.

**Why another one?** LingBot-Map unifies coordinate grounding, dense geometric cues, and long-range drift correction within a single streaming framework using anchor context, pose-reference window, and trajectory memory. FlashInfer paged KV-cache attention enables real-time inference at 518x378 resolution, and the model ships as a true feed-forward foundation model rather than a narrow specialist.

---

## 5. [taste-skill](https://github.com/Leonxlnx/taste-skill)
> Taste-Skill (High-Agency Frontend) - gives your AI good taste. stops the AI from generating boring, generic, "slop"

**Language:** Shell  |  **Stars:** 10,266  |  **Forks:** 992  |  **Score:** 5,608  |  **Created:** 2026-02-19

**Background:** Taste Skill is a frontend code skill for AI tools (Cursor, Claude Code, Antigravity, Codex, Windsurf, Copilot) that pushes them to produce modern, premium designs instead of generic "slop" UI. At over 10,000 stars with a v2 beta underway, it bundles variants — `taste-skill`, `gpt-taste`, `redesign-skill`, `soft-skill`, `output-skill` — for different visual styles and fix modes.

**Problem it solves:** Default LLM-generated UI tends toward visually bland output — uniform spacing, generic typography, no motion, and vanilla color palettes. Users want premium, animated interfaces but prompt-level direction rarely survives across a whole session.

**Why another one?** Taste Skill is a dedicated anti-slop skill rather than a general UI library, and it ships as multiple opinionated variants (GPT-specific, redesign-focused, softer aesthetic, lazy-model override) so teams pick the right pressure for each project. Single-command install via `npx skills add` works across every major AI coding agent.

---

## 6. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 83,422  |  **Forks:** 13,313  |  **Score:** 5,326  |  **Created:** 2025-10-13

**Background:** The Agency is a curated collection of AI agent personalities — each with its own domain expertise, voice, and deliverables — now at over 83,000 stars. Born from a Reddit thread and months of iteration, it bundles specialized agents (frontend wizards, Reddit ninjas, whimsy injectors, reality checkers) that install into Claude Code, Cursor, OpenClaw, Copilot, Aider, Gemini CLI, and more.

**Problem it solves:** One generic AI assistant cannot consistently produce high-quality work across every domain — marketing, frontend, QA, community, architecture. Users either re-prompt constantly or accept generic output, missing the benefit of specialist framing that improves both code and decisions.

**Why another one?** Agency Agents emphasizes personality and deliverables over generic prompt templates — each agent has defined success metrics, communication style, and battle-tested workflows. Cross-tool installers auto-detect which AI CLIs you have installed and configure them in one command, making it the broadest-compatible agent pack available.

---

## 7. [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
> Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy.

**Language:** Shell  |  **Stars:** 11,792  |  **Forks:** 1,717  |  **Score:** 5,041  |  **Created:** 2026-02-12

**Background:** Claude Code Game Studios turns a single Claude Code session into a complete game development studio with 49 specialized agents, 72 skills, 12 hooks, and 11 rules organized into a real studio hierarchy — directors, department leads, and specialists. With nearly 12,000 stars, it is one of the most ambitious Claude Code domain packs to date.

**Problem it solves:** Solo game development with AI suffers from structural chaos — no one stops you from hardcoding magic numbers, skipping design docs, or shipping spaghetti code. Without QA, design review, or vision enforcement, a single chat session produces prototypes that never become shippable games.

**Why another one?** The project maps a real-world game studio's hierarchy onto AI agents with defined responsibilities, escalation paths, and quality gates — rather than a flat list of helpers. Slash commands, hooks, and rules combine into a coherent governance system that keeps a solo developer aligned to a design vision from brainstorm to launch.

---

## 8. [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S)
> LEAKED SYSTEM PROMPTS FOR CHATGPT, GEMINI, GROK, CLAUDE, PERPLEXITY, CURSOR, DEVIN, REPLIT, AND MORE! - AI SYSTEMS TRANSPARENCY FOR ALL!

**Language:** N/A  |  **Stars:** 14,647  |  **Forks:** 2,910  |  **Score:** 4,592  |  **Created:** 2025-03-04

**Background:** CL4R1T4S is a running archive of extracted system prompts, guidelines, and tool definitions from major AI models and coding agents — OpenAI, Google, Anthropic, xAI, Perplexity, Cursor, Windsurf, Devin, Manus, Replit, and others. With over 14,000 stars, it has become the reference repository for understanding how frontier AI products are actually steered.

**Problem it solves:** Commercial AI products are shaped by large hidden prompt scaffolds that determine what they will say, which personas they adopt, how they refuse, and which ethical frames they apply. Without visibility into these system prompts, users cannot evaluate the bias, limitations, or risks of the AI they trust.

**Why another one?** The repo is a central, continuously-updated clearinghouse for leaked and reverse-engineered system prompts, with model name, extraction date, and context notes for each entry. Its neutral archival approach (contribution-based, no commentary) makes it useful to researchers, red-teamers, and developers studying prompt engineering at frontier scale.

---

## 9. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 159,794  |  **Forks:** 13,929  |  **Score:** 3,892  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent is a complete software development methodology built on composable skills, now at over 159,000 stars. It distributes through the official Claude plugin marketplace, its own marketplace, OpenAI Codex CLI, and more, making it the most broadly installed agentic framework on GitHub.

**Problem it solves:** Coding agents jump straight into writing code without a spec, plan, or review process. Enthusiastic-but-unsupervised agents produce code that works in isolation but misses requirements, lacks tests, and cannot be verified against the actual problem.

**Why another one?** Superpowers enforces a structured flow — spec extraction, digestible design review, implementation planning, then subagent-driven execution with automatic inspection. Subagents work autonomously for hours without deviating from the signed-off plan, and skills trigger automatically based on context so users never have to wire it up manually.

---

## 10. [awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
> A collection of DESIGN.md files inspired by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.

**Language:** N/A  |  **Stars:** 58,491  |  **Forks:** 7,288  |  **Score:** 3,828  |  **Created:** 2026-03-31

**Background:** Awesome DESIGN.md is a curated collection of 69 DESIGN.md files inspired by developer-focused websites, maintained by VoltAgent. Less than three weeks old and already at over 58,000 stars, it builds on Google Stitch's DESIGN.md convention to bridge the gap between how agents code and how interfaces should look.

**Problem it solves:** AI coding agents produce generic, inconsistent UI because they lack structured design context. Figma exports are unreadable by agents and prose descriptions are interpreted loosely, so teams settle for bland output or endless corrections.

**Why another one?** The project offers ready-to-use DESIGN.md files extracted from real websites, so a developer can drop one in and get "build me a page that looks like this" behavior from any AI agent. The markdown-only format is precisely the input LLMs parse best, bypassing all the failure modes of Figma or JSON schema-based design handoffs.

---

## 11. [gstack](https://github.com/garrytan/gstack)
> Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**Language:** TypeScript  |  **Stars:** 74,943  |  **Forks:** 10,622  |  **Score:** 3,168  |  **Created:** 2026-03-11

**Background:** gstack is Garry Tan's personal Claude Code setup, packaging 23 opinionated tools that act as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA roles. With over 74,000 stars in roughly five weeks, it rides the broader narrative that a single builder with the right tooling can now out-ship a traditional team.

**Problem it solves:** Solo developers using AI coding agents end up wearing every role — product, design, architecture, QA, docs — and the context switching degrades output quality. Without structured handoffs between these roles, "vibe coding" produces inconsistent results that do not scale past prototypes.

**Why another one?** gstack bakes a specific, battle-tested role hierarchy into the agent rather than offering generic slash commands. Tan's public claim of ~810x 2013 productivity gives it a strong adoption narrative, and the opinionated configuration — released as a complete stack rather than a menu — removes setup decisions for users who want a known-good starting point.

---

## 12. [PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR)
> Open-source, low-cost 10.5 GHz PLFM phased array RADAR system

**Language:** PLSQL  |  **Stars:** 13,824  |  **Forks:** 2,914  |  **Score:** 3,164  |  **Created:** 2026-03-08

**Background:** AERIS-10 is an open-source 10.5 GHz phased array radar system with Pulse Linear Frequency Modulated modulation, available in 3 km and 20 km range variants. With over 13,000 stars in about six weeks and a CERN-OHL-P hardware license, it is one of the most ambitious open radar projects to reach mainstream visibility.

**Problem it solves:** Phased array radar technology has historically been locked behind defense contractors and seven-figure budgets, keeping it inaccessible to researchers, drone developers, and SDR hobbyists. Even educational radar platforms usually stop at simple pulse/Doppler demos, not full beamforming systems.

**Why another one?** AERIS-10 ships complete schematics, PCB layouts, FPGA firmware, and a Python GUI with map integration — the full stack, not fragments. Dual configurations (8x16 patch array at 3 km, 32x16 waveguide array at 20 km) with ±45° electronic beam steering in both axes give it genuine research-grade capability rather than hobby-tier output.

---

## 13. [openai-agents-python](https://github.com/openai/openai-agents-python)
> A lightweight, powerful framework for multi-agent workflows

**Language:** Python  |  **Stars:** 22,915  |  **Forks:** 3,603  |  **Score:** 2,962  |  **Created:** 2025-03-11

**Background:** The OpenAI Agents SDK is a lightweight framework for multi-agent workflows, provider-agnostic across 100+ LLMs and supporting OpenAI's Responses and Chat Completions APIs. With 22,000+ stars it has become the reference Python implementation for OpenAI's agent primitives — including the newly-added Sandbox Agents and Realtime voice agents.

**Problem it solves:** Building reliable multi-agent systems requires handoffs, guardrails, tracing, human-in-the-loop checkpoints, and session management. Most DIY implementations skip several of these, producing brittle demos that break under real workloads.

**Why another one?** The SDK is a first-party OpenAI framework so model releases (gpt-realtime-1.5, new Responses API features) are supported on day one. Built-in tracing, guardrails, and session management remove boilerplate that custom stacks reimplement poorly, and the provider-agnostic design (100+ non-OpenAI models) prevents vendor lock-in despite the OpenAI branding.

---

## 14. [ppt-master](https://github.com/hugohe3/ppt-master)
> AI generates natively editable PPTX from any document — real PowerPoint shapes, not images — no design skills needed

**Language:** Python  |  **Stars:** 6,215  |  **Forks:** 709  |  **Score:** 2,962  |  **Created:** 2025-12-10

**Background:** PPT Master is a skill-style workflow that runs inside AI IDEs (Claude Code, Cursor, VS Code + Copilot, Codebuddy) to turn PDFs, DOCX, URLs, or Markdown into genuinely editable `.pptx` files — real shapes, text boxes, and charts rather than rasterized slides. With over 6,000 stars and v2.3.0 shipped, it is gaining traction among daily presentation builders.

**Problem it solves:** Existing AI presentation tools either export images (pretty but not editable) or produce bare text boxes that look unprofessional. Most also require cloud upload, monthly subscriptions, and platform lock-in, which is unacceptable for confidential or enterprise content.

**Why another one?** PPT Master outputs real PowerPoint files that behave like any human-authored deck — every shape is selectable and editable in PowerPoint, Keynote, or Google Slides. The workflow runs entirely in the user's IDE with no file uploads, no subscriptions, and MIT licensing, directly addressing the privacy and lock-in gaps in commercial alternatives.

---

## 15. [thunderbolt](https://github.com/thunderbird/thunderbolt)
> AI You Control: Choose your models. Own your data. Eliminate vendor lock-in.

**Language:** TypeScript  |  **Stars:** 1,159  |  **Forks:** 57  |  **Score:** 2,702  |  **Created:** 2025-07-23

**Background:** Thunderbolt by Thunderbird is an open-source, cross-platform AI client (web, iOS, Android, Mac, Linux, Windows) targeting enterprise on-prem deployment. Backed by the Thunderbird/Mozilla community and currently under security audit, it is positioning as a principled alternative to closed commercial AI clients.

**Problem it solves:** Enterprise users of AI chat products face a choice between cloud-locked services (data leaves their network) and brittle self-hosted rollouts (no polished UX across devices). Frontier models, local models, and on-prem deployments rarely coexist cleanly in a single client.

**Why another one?** Thunderbolt's Mozilla/Thunderbird heritage gives it credibility on privacy and auditability that startup alternatives cannot match. Its unified multi-platform apps with provider-agnostic model support — frontier APIs, Ollama, llama.cpp, or any OpenAI-compatible endpoint — target enterprise deployments where vendor lock-in is a hard blocker.

---

## 16. [android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill)
> Claude Code skill to support Android app's reverse engineering

**Language:** Shell  |  **Stars:** 2,746  |  **Forks:** 285  |  **Score:** 2,449  |  **Created:** 2026-02-02

**Background:** Android Reverse Engineering Skill is a Claude Code plugin that decompiles APK, XAPK, JAR, and AAR files using jadx and Fernflower/Vineflower, then extracts the HTTP APIs — Retrofit endpoints, OkHttp calls, hardcoded URLs, auth patterns. Over 2,700 stars reflect strong demand in the security research community.

**Problem it solves:** Documenting or reproducing an Android app's API surface without source code normally requires days of manual decompilation, tracing Activities through ViewModels to HTTP calls, and handling ProGuard/R8 obfuscation. Each step uses different tools with no unified workflow.

**Why another one?** The skill bundles the entire reverse engineering workflow — dependency check, decompilation, API extraction, call-flow tracing — behind a single `/decompile` slash command. Side-by-side comparison between jadx and Fernflower/Vineflower output helps analysts pick the cleanest decompilation for each function, which no standalone tool offers.

---

## 17. [rustdesk](https://github.com/rustdesk/rustdesk)
> An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer.

**Language:** Rust  |  **Stars:** 112,011  |  **Forks:** 16,755  |  **Score:** 2,405  |  **Created:** 2020-09-28

**Background:** RustDesk is an open-source remote desktop solution written in Rust, with over 112,000 stars and translations in 25+ languages. A multi-year project with a paid Server Pro tier, it has matured into the default self-hosted TeamViewer alternative for both technical users and small businesses.

**Problem it solves:** Commercial remote desktop tools (TeamViewer, AnyDesk, Splashtop) route sessions through proprietary servers, raising privacy concerns and licensing costs that scale painfully with IT fleets. Existing open-source options often lack polish or cross-platform parity.

**Why another one?** RustDesk works out of the box with no configuration while still allowing full self-hosting for organizations that need complete data sovereignty. Its Rust foundation gives it strong security and performance characteristics, and the commercial Server Pro tier funds ongoing development without compromising the open-source client.

---

## 18. [Recordly](https://github.com/webadderall/Recordly)
> Create polished screen recordings for free. An open-source alternative to Screen Studio.

**Language:** TypeScript  |  **Stars:** 8,158  |  **Forks:** 614  |  **Score:** 2,365  |  **Created:** 2026-03-12

**Background:** Recordly is an open-source screen recorder and editor for walkthroughs, demos, and product videos — an alternative to paid tools like Screen Studio. Running natively on macOS 14+, Windows 10+, and Linux with over 8,000 stars, it ships with auto-zooms, cursor polish, webcam overlays, and timeline editing.

**Problem it solves:** Creating polished demo videos normally means either paying for Screen Studio/Loom Premium or sending raw footage to a motion designer for cursor polish, zooms, and framed backgrounds. Free tools usually output raw captures that look unprofessional.

**Why another one?** Recordly bundles the full motion-driven presentation workflow in one free AGPL-licensed app — auto-zoom suggestions, smooth cursor motion, styled frames with wallpapers and gradients, webcam overlay bubbles, and a demo-focused timeline editor. Native capture helpers (ScreenCaptureKit, Windows Graphics Capture) keep recording quality on par with paid competitors.

---

## 19. [paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)
> A community-supported supercharged document management system: scan, index and archive all your documents

**Language:** Python  |  **Stars:** 38,367  |  **Forks:** 2,455  |  **Score:** 2,168  |  **Created:** 2022-02-12

**Background:** Paperless-ngx is the community-maintained successor to Paperless and Paperless-ng, offering self-hosted document management: scan, OCR, tag, and search everything. With over 38,000 stars and a four-year community track record, it is the de facto open-source alternative to commercial DMS products.

**Problem it solves:** Personal and small-business paperwork piles up as physical documents and scattered PDFs with no uniform indexing or search. Commercial DMS products are expensive and usually cloud-hosted, conflicting with privacy requirements for tax, medical, and legal documents.

**Why another one?** Paperless-ngx specifically distributes maintenance across a team rather than depending on a single developer — addressing the sustainability gap that killed its predecessor. Its mature OCR pipeline, tag/correspondent/document-type model, and long history of self-host deployments make it a safer long-term bet than newer entrants.

---

## 20. [agent-skills](https://github.com/addyosmani/agent-skills)
> Production-grade engineering skills for AI coding agents.

**Language:** Shell  |  **Stars:** 17,291  |  **Forks:** 2,185  |  **Score:** 2,108  |  **Created:** 2026-02-15

**Background:** Agent Skills by Addy Osmani encodes senior-engineer workflows and quality gates into seven slash commands — `/spec`, `/plan`, `/build`, `/test`, `/review`, `/code-simplify`, `/ship` — covering the full development lifecycle. Over 17,000 stars reflect continued traction since its earlier trendshift appearances.

**Problem it solves:** AI coding agents jump straight into writing code without specifying requirements, planning incrementally, testing, or reviewing. Without disciplined phase gates, the output works in isolation but fails in production, and teams lose the quality discipline that made senior engineers valuable.

**Why another one?** The project maps explicit slash commands to the DEFINE-PLAN-BUILD-VERIFY-REVIEW-SHIP pipeline, with automatic skill activation based on context (API design triggers `api-and-interface-design`, UI triggers `frontend-ui-engineering`). Marketplace installation via `/plugin install` makes it a one-command upgrade to structured agent workflows.

---

## 21. [hermes-agent](https://github.com/NousResearch/hermes-agent)
> The agent that grows with you

**Language:** Python  |  **Stars:** 97,902  |  **Forks:** 13,800  |  **Score:** 2,062  |  **Created:** 2025-07-22

**Background:** Hermes Agent by Nous Research is a self-improving AI agent approaching 100,000 stars, with a built-in learning loop that creates skills from experience, improves them during use, and builds persistent user models across sessions. It runs on anything from a $5 VPS to GPU clusters and connects to 200+ models via Nous Portal, OpenRouter, NVIDIA NIM, Moonshot, MiniMax, and more.

**Problem it solves:** Most AI agents start fresh every session — no memory of past tasks, no accumulated user model, no skills growing from experience. Users re-explain context, watch the agent repeat the same mistakes, and lose the compounding value that makes human assistants useful.

**Why another one?** Hermes is the only mainstream agent with a closed learning loop — agent-curated memory with periodic nudges, autonomous skill creation after complex tasks, skills that self-improve during use, FTS5 cross-session search with LLM summarization. Multi-channel presence (Telegram, Discord, Slack, WhatsApp, Signal, CLI) from a single gateway means context travels with the user across devices.

---

## 22. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Language:** Shell  |  **Stars:** 115,798  |  **Forks:** 19,303  |  **Score:** 1,973  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official agentic coding CLI, now over 115,000 stars. It runs in the terminal, IDE, or via `@claude` on GitHub, and has become the anchor product for the entire Claude Code skills ecosystem that dominates this week's trendshift list.

**Problem it solves:** Chat-style LLM interfaces require constant copy-pasting between the browser and the developer's real environment — terminal, files, git, CI. That friction is incompatible with the rate at which coding agents can actually produce work.

**Why another one?** Claude Code is a first-party Anthropic product with direct access to the latest Claude models, no API intermediaries, and continuous integration with Anthropic's agent features (skills, plugins, hooks, marketplaces). The ecosystem effect — every major agent skill, including most projects in this report, targets Claude Code first — makes it the natural default.

---

## 23. [claude-desktop-buddy](https://github.com/anthropics/claude-desktop-buddy)
> Reference and an example for the Bluetooth API for makers in Claude Cowork & Claude Code Desktop

**Language:** C++  |  **Stars:** 248  |  **Forks:** 17  |  **Score:** 1,902  |  **Created:** 2026-04-09

**Background:** Claude Desktop Buddy is Anthropic's official reference for a new Bluetooth Low Energy API that lets Claude Cowork and Claude Code Desktop talk to maker hardware. The featured example is an ESP32/M5StickC Plus desk pet that sleeps, wakes on new sessions, and lets you approve permission prompts from the device itself.

**Problem it solves:** Claude's permission prompts and session events are invisible unless the user is actively watching the app. Developers who want physical, ambient feedback — a desk pet, an approval button, a session LED — had no official API to build on and had to reverse-engineer the desktop app.

**Why another one?** This is Anthropic's first official wire protocol for maker hardware, using standard Nordic UART Service UUIDs plus documented JSON schemas and a folder push transport. A lightweight, opt-in BLE API legitimizes an entire hobbyist/maker segment around Claude, turning experimental builds into supported integrations.

---

## 24. [claude-code-local](https://github.com/nicedreamzapp/claude-code-local)
> Run Claude Code with local AI on Apple Silicon. 122B model at 41 tok/s with Google TurboQuant. No cloud, no API fees.

**Language:** Python  |  **Stars:** 1,124  |  **Forks:** 210  |  **Score:** 1,771  |  **Created:** 2026-03-26

**Background:** Claude Code Local is a local-only setup for running Claude Code on Apple Silicon with three local model options — including a 122B model at 41 tok/s via Google TurboQuant and Qwen 3.5 at 65 tok/s — in four modes ranging from hands-free voice to pure offline. Zero cloud, zero API fees.

**Problem it solves:** Cloud-hosted coding agents have recurring API costs, privacy exposure on every request, and outages that halt work. Existing local model setups for coding rarely match the speed or polish of Claude Code's UX, especially on MacBooks.

**Why another one?** The project benchmarks specific models on Apple Silicon (Claude Code task completed in 17.6s with Qwen) and documents the full local-first stack — voice, ambient computing, 100% on-device. Its opinionated "pick your fighter" setup removes the research burden of figuring out which local model actually works well with Claude Code's agent loop.

---

## 25. [context-mode](https://github.com/mksglu/context-mode)
> Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 12 platforms

**Language:** TypeScript  |  **Stars:** 7,484  |  **Forks:** 524  |  **Score:** 1,736  |  **Created:** 2026-02-23

**Background:** Context Mode is a context-window optimizer for AI coding agents, sandboxing tool output for a claimed 98% reduction across 12 platforms. With over 7,400 stars, listed usage across Microsoft, Google, Meta, Amazon, IBM, NVIDIA, ByteDance, and Stripe, and a Hacker News #1 post at 570+ points, it has rapid enterprise traction.

**Problem it solves:** Coding agents blow their context window on verbose tool output — grep dumps, build logs, file reads — leaving little room for reasoning. Each extra turn pays a token tax on previously-seen output, and long sessions hit context limits well before the task is done.

**Why another one?** Context Mode sandboxes tool output so the agent sees a summary or a handle rather than the raw bytes, claiming 98% token reduction without losing information fidelity. Broad platform coverage (12 agents) and strong enterprise adoption make it a drop-in efficiency upgrade rather than a bespoke optimization.

---

> **Day's theme:** The Claude Code skills ecosystem dominates today's list with at least twelve projects (andrej-karpathy-skills, taste-skill, agency-agents, Claude-Code-Game-Studios, superpowers, awesome-design-md, gstack, agent-skills, android-reverse-engineering-skill, ppt-master, claude-code, claude-desktop-buddy) all extending Anthropic's CLI through skills, slash commands, and role-based agent packs. Two counter-currents round out the picture: local-first AI (claude-code-local, thunderbolt, hermes-agent, rustdesk) responding to cloud cost and privacy concerns, and hard-science open hardware/foundation-model releases (lingbot-map's 3D reconstruction transformer, PLFM_RADAR's 10.5 GHz phased array) showing that the trend toward opinionated open packaging extends well beyond LLM tooling.
