# Trendshift Report — 2026-04-18
**Total:** 25 repos

---

## 1. [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
> A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**Language:** N/A  |  **Stars:** 54,695  |  **Forks:** 4,633  |  **Score:** 19,244  |  **Created:** 2026-01-27

**Background:** Andrej-Karpathy-Skills distills Andrej Karpathy's widely-shared observations about LLM coding pitfalls into a single CLAUDE.md file that tightens Claude Code behavior. After peaking last week, the repo is back at the top spot with 54K+ stars — clear evidence that "authoritative one-file config" is becoming the default AI-agent onboarding pattern.

**Problem it solves:** LLMs make wrong assumptions without checking, overcomplicate APIs, produce bloated code, and silently remove comments or code they do not understand. These failure modes compound across sessions and degrade codebase quality over time.

**Why another one?** The project packages observations from one of the most respected voices in AI into an immediately actionable format — a single file dropped into any project. Unlike general-purpose guidelines, each rule targets a specific, documented failure mode with a concrete countermeasure.

---

## 2. [PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR)
> Open-source, low-cost 10.5 GHz PLFM phased array RADAR system

**Language:** PLSQL  |  **Stars:** 13,824  |  **Forks:** 2,914  |  **Score:** 11,378  |  **Created:** 2026-03-08

**Background:** AERIS-10 (PLFM_RADAR) is an open-source, low-cost 10.5 GHz Pulse Linear Frequency Modulated phased array radar system. Shipped in two variants — a 3 km Nexus build and a 20 km Extended build — with full schematics, firmware, and a Python GUI, it targets researchers, drone developers, and advanced SDR enthusiasts.

**Problem it solves:** Phased array radar has historically been locked behind defense-industry price tags and proprietary IP, leaving academic researchers and drone startups without a hackable platform to experiment with beamforming, pulse compression, Doppler processing, and target tracking.

**Why another one?** AERIS-10 is one of the very few genuinely end-to-end open hardware radar projects — CERN-OHL-P hardware licensing, MIT software, on-board FPGA signal processing, and ±45° electronic beam steering. The modular board split (power, frequency synth, main RF) lets builders reuse subsystems independently, which simple SDR-based radar kits cannot offer.

---

## 3. [hyperframes](https://github.com/heygen-com/hyperframes)
> Write HTML. Render video. Built for agents.

**Language:** HTML  |  **Stars:** 2,849  |  **Forks:** 217  |  **Score:** 11,336  |  **Created:** 2026-03-10

**Background:** HyperFrames by HeyGen is an open-source video rendering framework that turns HTML compositions into rendered video, with first-class support for AI coding agents. A single `npx skills add heygen-com/hyperframes` teaches Claude Code, Cursor, Gemini CLI, or Codex how to author HyperFrames compositions and GSAP animations via slash commands.

**Problem it solves:** Programmatic video generation traditionally requires Remotion-style React expertise or specialized tools like After Effects. Asking an AI agent to create video is hard because there is no format LLMs already know — Figma exports, MP4 encoders, and timeline editors all require tool-specific glue.

**Why another one?** HyperFrames leans all the way into HTML + CSS + GSAP, the stack LLMs already write fluently, and packages the knowledge as installable skills rather than library docs. The result is "describe the video, get the video" for any agent-driven workflow — cold-start prompts, PDF-to-pitch conversion, CSV-to-bar-chart-race, vertical TikTok hooks, all from natural language.

---

## 4. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 159,794  |  **Forks:** 13,929  |  **Score:** 6,417  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent is a complete agentic software development workflow, now at nearly 160,000 stars. It enforces a structured process — spec extraction, digestible design review, implementation planning, supervised subagent execution — that prevents coding agents from jumping straight into code.

**Problem it solves:** AI coding agents rush into writing code without proper planning, producing solutions that miss requirements or need extensive rework. The enthusiasm-without-judgment pattern ships code that works in isolation but fails in production.

**Why another one?** Superpowers' subagent-driven development is the differentiator: it launches sub-agents for each engineering task, inspects their work, and continues autonomously. Skills trigger from context, and the framework runs on Claude Code, Cursor, Codex, and OpenCode — making it the most broadly compatible skills framework today.

---

## 5. [awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
> A collection of DESIGN.md files inspired by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.

**Language:** N/A  |  **Stars:** 58,491  |  **Forks:** 7,288  |  **Score:** 6,286  |  **Created:** 2026-03-31

**Background:** Awesome DESIGN.md is a curated collection of DESIGN.md files capturing design systems from popular brands and websites, now above 58,000 stars in under three weeks. Dropping one of these files into a project gives any AI coding agent a complete, structured design specification written in the format LLMs read best — markdown.

**Problem it solves:** AI coding agents produce generic, inconsistent UI because they lack visual design context. Prose descriptions are interpreted loosely, and Figma files are unreadable to agents — so there is no reliable way to say "build it in the style of Linear" or "Stripe" and get consistent results.

**Why another one?** The project ships dozens of ready-to-use design system files extracted from real websites, removing the need for teams to write their own. Its markdown-first format is exactly what LLMs consume most accurately, closing the gap between how agents build and how modern interfaces should look.

---

## 6. [openai-agents-python](https://github.com/openai/openai-agents-python)
> A lightweight, powerful framework for multi-agent workflows

**Language:** Python  |  **Stars:** 22,915  |  **Forks:** 3,603  |  **Score:** 4,878  |  **Created:** 2025-03-11

**Background:** OpenAI Agents Python is OpenAI's own lightweight framework for building multi-agent workflows. With over 22,000 stars, it is becoming the default reference implementation for agent handoffs, guardrails, and tracing when using OpenAI models directly.

**Problem it solves:** Multi-agent orchestration across frameworks like LangChain, CrewAI, or AutoGen adds heavy abstractions and opinionated patterns that are hard to reason about. Teams using OpenAI models want a minimal, native-feeling SDK that exposes agents, tools, and handoffs without framework overhead.

**Why another one?** Coming from OpenAI itself, the library tracks the latest API features — responses API, structured outputs, built-in tool types, and tracing — faster than third-party wrappers can. The lightweight surface area makes it easy to compose into larger systems, and the official status signals long-term maintenance.

---

## 7. [ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)
> Learn it. Build it. Ship it for others.

**Language:** Python  |  **Stars:** 3,835  |  **Forks:** 813  |  **Score:** 4,774  |  **Created:** 2026-03-18

**Background:** AI Engineering from Scratch is a 260+ lesson, 20-phase, ~290-hour curriculum that teaches AI engineering from linear algebra to autonomous agent swarms. Created a month ago and already nearing 4K stars, it spans Python, TypeScript, Rust, and Julia across PyTorch, JAX, Claude Code, and MCP workflows.

**Problem it solves:** AI learning resources fragment across math textbooks, framework tutorials, and agent cookbooks, leaving learners without a single path from foundations to shipping production agent systems. Most paid courses are narrow; most free resources stop at "hello world."

**Why another one?** The course is explicitly AI-native — learners use AI coding agents to work through the lessons, then build the tools and agents themselves. The 20-phase structure gives a clear roadmap, and the open-source format keeps it free and continuously updated, unlike frozen bootcamp material.

---

## 8. [magic-resume](https://github.com/JOYCEQL/magic-resume)
> free online AI resume editor, the only official website is https://magicv.art

**Language:** TypeScript  |  **Stars:** 6,397  |  **Forks:** 724  |  **Score:** 4,528  |  **Created:** 2024-05-19

**Background:** Magic Resume is a free, open-source online AI resume editor with over 6,300 stars. Built in TypeScript, it provides an approachable editing experience for job seekers who want AI-assisted resume drafting without the subscription fees charged by commercial resume builders.

**Problem it solves:** Commercial resume builders lock essential features — PDF export, template variety, AI rewriting — behind paywalls. For students and early-career job seekers, this friction disproportionately affects the people who need good resumes most.

**Why another one?** Magic Resume's fully free, browser-based approach removes the paywall entirely while keeping the polished UX users expect from SaaS tools. The open-source code means organizations can self-host a branded version for career centers or bootcamps without vendor lock-in.

---

## 9. [android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill)
> Claude Code skill to support Android app's reverse engineering

**Language:** Shell  |  **Stars:** 2,746  |  **Forks:** 285  |  **Score:** 4,276  |  **Created:** 2026-02-02

**Background:** Android Reverse Engineering Skill is a Claude Code plugin that decompiles APK, XAPK, JAR, and AAR files using jadx and Fernflower/Vineflower, then extracts the HTTP APIs an Android app actually uses — Retrofit endpoints, OkHttp calls, hardcoded URLs, auth headers and tokens.

**Problem it solves:** Documenting the private API of a mobile-first service typically requires hours of manual decompilation, trace collection, and cross-referencing. For security researchers and integration engineers, the legwork of "what endpoints does this app actually call" is the most time-consuming part of every job.

**Why another one?** This skill packages the entire RE toolchain into a Claude Code slash command — decompile, trace call flows from Activities through ViewModels into HTTP calls, and produce clean API documentation. ProGuard/R8-handling strategies are built in, which most naive decompile-and-grep scripts cannot do.

---

## 10. [FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal)
> FinceptTerminal is a modern finance application offering advanced market analytics, investment research, and economic data tools, designed for interactive exploration and data-driven decision-making in a user-friendly environment.

**Language:** Python  |  **Stars:** 6,079  |  **Forks:** 964  |  **Score:** 4,016  |  **Created:** 2024-08-29

**Background:** Fincept Terminal is an open-source finance application that bundles market analytics, investment research, and economic data tools into a single interactive interface. With over 6,000 stars, it positions itself as a developer-friendly alternative to Bloomberg Terminal-style paid platforms.

**Problem it solves:** Professional finance terminals like Bloomberg and Refinitiv cost tens of thousands of dollars per year per seat, pricing out independent traders, small funds, and academic researchers. Free alternatives usually ship fragmented data and unreliable charting.

**Why another one?** Fincept Terminal is Python-native and open source, so users can inspect the data pipeline, add custom analytics, and integrate it with their own models. The interactive UI focuses on exploratory research rather than just read-only data access, differentiating it from simple market-data widgets.

---

## 11. [cognee](https://github.com/topoteretes/cognee)
> Knowledge Engine for AI Agent Memory in 6 lines of code

**Language:** Python  |  **Stars:** 16,426  |  **Forks:** 1,691  |  **Score:** 3,636  |  **Created:** 2023-08-16

**Background:** Cognee is a knowledge engine that gives AI agents structured, queryable memory in just six lines of code. Now with 16,000+ stars, it targets teams that want graph-backed memory without building their own ingestion, embedding, and retrieval pipeline from scratch.

**Problem it solves:** Agent memory is usually glued together from vector stores, keyword indexes, and bespoke retrievers, each with different APIs and semantics. The result is brittle recall and token-heavy context injection that degrades agent reliability over long sessions.

**Why another one?** Cognee collapses memory setup to a minimal API while offering graph-based retrieval under the hood, which captures relationships vector search alone cannot. The long-standing maintenance (since 2023) and broad adoption make it a mature choice compared to newer single-purpose memory libraries.

---

## 12. [evolver](https://github.com/EvoMap/evolver)
> The GEP-Powered Self-Evolution Engine for AI Agents. Genome Evolution Protocol. | evomap.ai

**Language:** JavaScript  |  **Stars:** 4,724  |  **Forks:** 460  |  **Score:** 3,616  |  **Created:** 2026-02-01

**Background:** Evolver is a Genome Evolution Protocol (GEP) powered self-evolution engine for AI agents, designed to turn ad hoc prompt tweaks into auditable, reusable evolution assets. It is the core engine behind EvoMap, a network where AI agents evolve through validated collaboration — complete with live agent maps and evolution leaderboards.

**Problem it solves:** Prompt iteration is usually untracked and unreviewed — engineers modify prompts in place, lose the rollback trail, and cannot share improvements across teams. "Which tweak actually helped?" becomes unanswerable as prompts accumulate.

**Why another one?** Evolver applies protocol-constrained evolution with genes, capsules, and audit trails, turning prompt governance into a first-class engineering practice. The git-backed rollback and blast-radius calculation require a real VCS, which encodes a "ship changes safely" discipline missing from most prompt registries.

---

## 13. [pi-autoresearch](https://github.com/davebcn87/pi-autoresearch)
> Autonomous experiment loop extension for pi

**Language:** TypeScript  |  **Stars:** 5,507  |  **Forks:** 294  |  **Score:** 3,370  |  **Created:** 2026-03-11

**Background:** pi-autoresearch is an extension for pi — an AI coding agent — that implements an autonomous optimization loop: try an idea, benchmark it, keep improvements, revert regressions, repeat. Inspired by Karpathy's autoresearch, it works for any optimization target: test speed, bundle size, LLM training, build times, Lighthouse scores.

**Problem it solves:** "Try-measure-compare" is the right loop for almost every performance optimization, but nobody runs it rigorously — engineers make a change, eyeball the result, and move on, losing regressions and leaving wins on the table.

**Why another one?** pi-autoresearch gives an AI agent the tools to run this loop autonomously — session config, timed experiment runs, auto-commit logs, and a live dashboard. The skill bundled with the extension teaches the agent exactly what to ask before starting a session, so humans do not have to hand-design the optimization harness.

---

## 14. [CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S)
> LEAKED SYSTEM PROMPTS FOR CHATGPT, GEMINI, GROK, CLAUDE, PERPLEXITY, CURSOR, DEVIN, REPLIT, AND MORE! - AI SYSTEMS TRANSPARENCY FOR ALL!

**Language:** N/A  |  **Stars:** 14,647  |  **Forks:** 2,910  |  **Score:** 3,308  |  **Created:** 2025-03-04

**Background:** CL4R1T4S is a community-maintained archive of leaked or reverse-engineered system prompts from major AI systems — ChatGPT, Gemini, Grok, Claude, Perplexity, Cursor, Devin, Replit, and more. With 14,000+ stars, it has become the go-to reference for researchers studying how production AI products shape model behavior behind the scenes.

**Problem it solves:** Commercial AI products hide their system prompts, leaving developers guessing about safety policies, tool-use conventions, and reasoning patterns that shape outputs. Understanding these design choices is essential for building competing products or evaluating alignment claims.

**Why another one?** CL4R1T4S is the most comprehensive and actively updated of the system-prompt-leak repositories, covering coding agents, search products, and general chatbots in one place. The consistent formatting across entries makes cross-vendor comparison tractable, which scattered individual leaks cannot offer.

---

## 15. [dive-into-llms](https://github.com/Lordog/dive-into-llms)
> 《动手学大模型Dive into LLMs》系列编程实践教程

**Language:** Jupyter Notebook  |  **Stars:** 32,425  |  **Forks:** 3,935  |  **Score:** 3,178  |  **Created:** 2024-04-08

**Background:** Dive into LLMs is a hands-on Chinese-language tutorial series on large language models, distributed as Jupyter Notebooks. With over 32,000 stars, it serves as a leading Mandarin-language resource for students and engineers learning LLM fundamentals and building practical applications.

**Problem it solves:** High-quality LLM learning material is overwhelmingly English-first, creating a significant barrier for Chinese-speaking learners. Translated tutorials often lag behind the frontier and miss local context like Chinese model families and deployment constraints.

**Why another one?** The notebook-based, runnable format lets learners execute code as they read, closing the theory-practice gap that static tutorials leave open. The series is maintained in Chinese by native speakers, so terminology and cultural framing match the audience rather than being awkward translations.

---

## 16. [opensre](https://github.com/Tracer-Cloud/opensre)
> Build your own AI SRE agents. The open source toolkit for the AI era

**Language:** Python  |  **Stars:** 1,653  |  **Forks:** 183  |  **Score:** 2,894  |  **Created:** 2026-01-13

**Background:** OpenSRE by Tracer Cloud is an open-source framework for building AI SRE agents, with the training and evaluation environment they need to improve over time. It connects to 60+ SRE tools, supports custom workflow definitions, and runs investigations on your own infrastructure rather than a vendor cloud.

**Problem it solves:** Commercial AI SRE products lock teams into opaque models, fixed integrations, and uncontrolled data egress. On-call engineers need agents that can actually investigate incidents using the specific tools their company runs — not a generic playbook.

**Why another one?** OpenSRE ships not just an agent but the training and eval environment around it, so teams can improve agents against their own incident history. The 60+ integrations cover the tools real SRE teams already use (monitoring, logging, tracing, runbooks), making it immediately usable rather than a demo-ware framework.

---

## 17. [claude-mem](https://github.com/thedotmack/claude-mem)
> A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**Language:** TypeScript  |  **Stars:** 63,104  |  **Forks:** 5,284  |  **Score:** 2,779  |  **Created:** 2025-08-31

**Background:** claude-mem is a Claude Code plugin that captures every tool call, file edit, and decision from a coding session, compresses it with Claude's agent SDK, and injects the relevant slice back into future sessions. With 63,000+ stars, it has become one of the most popular memory plugins in the Claude Code ecosystem.

**Problem it solves:** Claude Code sessions lose all context when they end — project conventions, past debugging decisions, and architectural rationale disappear. Developers end up re-explaining the same background to every new session.

**Why another one?** claude-mem's approach of full-capture-then-compress preserves fidelity other memory tools lose by trying to summarize in real time. By using Claude's own agent SDK for compression, it keeps the summaries on-model for future retrieval, and the automatic context injection removes the manual "prime the agent" ritual.

---

## 18. [omi](https://github.com/BasedHardware/omi)
> AI that sees your screen, listens to your conversations and tells you what to do

**Language:** Dart  |  **Stars:** 10,825  |  **Forks:** 1,749  |  **Score:** 2,746  |  **Created:** 2024-03-22

**Background:** Omi by Based Hardware is a wearable and desktop AI that observes screen content and spoken conversations, then delivers proactive guidance. With over 10,000 stars, it sits at the intersection of ambient computing and personal AI assistants, combining open-source software with hardware integrations.

**Problem it solves:** Assistants that only respond to explicit prompts miss the continuous context of daily life — meetings you did not transcribe, screen content you glanced past, decisions you made verbally. Capturing that stream requires always-on capture and on-device intelligence.

**Why another one?** Omi's open-source full stack — wearable firmware, mobile app, desktop client — is unique in the proactive-assistant space, which is dominated by closed products. The ability to self-host the intelligence layer means users keep their screen and conversation data local instead of piping it to a vendor.

---

## 19. [GenericAgent](https://github.com/lsdefine/GenericAgent)
> Self-evolving agent: grows skill tree from 3.3K-line seed, achieving full system control with 6x less token consumption

**Language:** Python  |  **Stars:** 4,506  |  **Forks:** 481  |  **Score:** 2,648  |  **Created:** 2026-01-16

**Background:** GenericAgent is a minimal, self-evolving autonomous agent framework with a ~3K-line core and 9 atomic tools that give any LLM system-level control over a local computer — browser, terminal, filesystem, keyboard/mouse, screen vision, and Android via ADB. Its design philosophy: don't preload skills, evolve them.

**Problem it solves:** Heavyweight agent frameworks load hundreds of skills up front, inflating context windows to 200K–1M tokens and drowning the model in irrelevant tooling. This raises cost, slows reasoning, and introduces hallucinations when the model chooses the wrong preloaded skill.

**Why another one?** GenericAgent keeps the context under 30K by crystallizing each task's successful execution path into a reusable skill after the first completion — the longer you use it, the richer the skill tree becomes. The demo set (ordering food delivery, screening stocks, driving Alipay via ADB) shows real cross-platform system control, not just file edits.

---

## 20. [hermes-agent](https://github.com/NousResearch/hermes-agent)
> The agent that grows with you

**Language:** Python  |  **Stars:** 97,902  |  **Forks:** 13,800  |  **Score:** 2,606  |  **Created:** 2025-07-22

**Background:** Hermes Agent by Nous Research is a self-improving AI agent with a built-in learning loop that creates skills from experience and builds a deepening model of the user across sessions. Nearing 100,000 stars, it is the flagship example of "agents that grow" rather than restarting fresh each session.

**Problem it solves:** AI agents start from zero in every session — they do not remember past interactions, learn from mistakes, or adapt to user preferences. This forces users to re-explain context repeatedly and prevents the agent from developing domain expertise over time.

**Why another one?** Hermes Agent's learning loop is the differentiator: it creates skills from experience, improves them during use, and builds persistent user models across sessions. It runs on any infrastructure from a $5 VPS to a GPU cluster, supports 200+ models via OpenRouter, and operates across Telegram, Discord, Slack, WhatsApp, and Signal from a single gateway.

---

## 21. [lingbot-map](https://github.com/Robbyant/lingbot-map)
> A feed-forward 3D foundation model for reconstructing scenes from streaming data

**Language:** Python  |  **Stars:** 2,419  |  **Forks:** 171  |  **Score:** 2,581  |  **Created:** 2026-04-15

**Background:** LingBot-Map is a feed-forward 3D foundation model for streaming 3D scene reconstruction, released only three days ago and already crossing 2,400 stars. Its Geometric Context Transformer unifies coordinate grounding, dense geometric cues, and long-range drift correction into a single streaming framework.

**Problem it solves:** Streaming 3D reconstruction is usually slow and drift-prone — iterative optimization methods produce quality but not speed, while feed-forward methods cannot handle long sequences without drift. Neither path scales to thousands of frames at interactive frame rates.

**Why another one?** LingBot-Map hits ~20 FPS on 518×378 inputs over 10,000+ frame sequences by using paged KV cache attention and a dedicated anchor/reference/memory design. Full paper, PyTorch code, and both Hugging Face and ModelScope weights ship day-one, making it immediately usable by researchers instead of being a paper-only release.

---

## 22. [rustdesk](https://github.com/rustdesk/rustdesk)
> An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer.

**Language:** Rust  |  **Stars:** 112,011  |  **Forks:** 16,755  |  **Score:** 2,556  |  **Created:** 2020-09-28

**Background:** RustDesk is a self-hosted remote desktop application positioned as an open-source alternative to TeamViewer, now at over 112,000 stars. Built in Rust, it provides the cross-platform, low-latency screen sharing that IT admins and power users have historically paid commercial vendors for.

**Problem it solves:** Commercial remote desktop tools charge per-seat fees, limit concurrent connections, and force all traffic through vendor relay servers — creating both cost and privacy problems for schools, non-profits, and organizations handling sensitive data.

**Why another one?** RustDesk's self-hosted relay server is the killer feature: organizations run their own infrastructure, keeping all connection metadata and screen traffic on their own servers. The Rust implementation gives it a strong security and performance baseline, and the multi-platform clients (Windows, macOS, Linux, iOS, Android) match what TeamViewer offers without the licensing tax.

---

## 23. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 83,422  |  **Forks:** 13,313  |  **Score:** 2,532  |  **Created:** 2025-10-13

**Background:** Agency Agents is a meticulously crafted collection of specialist AI agent personalities — each with defined voice, processes, and deliverables — born from a Reddit thread and months of iteration. Now at over 83,000 stars, it installs into Claude Code with a single shell script.

**Problem it solves:** Most "AI agent" collections are just lightly-decorated prompt templates that produce generic output regardless of which persona is selected. Teams need agents that actually behave differently — a frontend specialist should think about accessibility and performance, not just say "I am a frontend specialist."

**Why another one?** Agency Agents puts specialization and deliverables first — every agent ships with concrete workflows and success metrics, not just a role description. The Reddit-origin story and months of iteration show up in the care taken with each personality's voice, processes, and output format.

---

## 24. [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)
> Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy.

**Language:** Shell  |  **Stars:** 11,792  |  **Forks:** 1,717  |  **Score:** 2,445  |  **Created:** 2026-02-12

**Background:** Claude Code Game Studios turns a single Claude Code session into a full game development studio with 49 specialized agents, 72 skills, 12 hooks, and 11 rules organized into a studio hierarchy of directors, department leads, and hands-on specialists. Now at nearly 12,000 stars, it is one of the most elaborate domain-specific agent packages on Claude Code.

**Problem it solves:** Solo game development with a single AI chat session has no structure — nothing stops hardcoded magic numbers, missing design docs, or spaghetti code, and there is no QA pass or design review to catch issues early. The unstructured approach produces demos that never reach ship quality.

**Why another one?** The studio-hierarchy framing (directors guarding vision, leads owning domains, specialists executing) encodes real game studio processes rather than generic project management. Escalation paths and quality gates mean the agents proactively ask the right questions, mirroring the constructive friction a real team provides to a solo developer.

---

## 25. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Language:** Shell  |  **Stars:** 115,798  |  **Forks:** 19,303  |  **Score:** 2,423  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official agentic coding CLI, now at nearly 116,000 stars. It lives in the terminal, understands whole codebases, and executes routine tasks — tests, refactors, git workflows — through natural language. Its continued trending presence reflects how much of the day's ecosystem (skills, plugins, memory systems) is built directly on top of it.

**Problem it solves:** General-purpose AI chat tools are not structurally aware of repositories — they cannot reliably navigate large codebases, run tests, commit changes, or coordinate multi-file edits. Copy-pasting between an editor and a chat window is slow and error-prone for non-trivial projects.

**Why another one?** Claude Code is the terminal-native, codebase-aware entry point to Anthropic's models, with first-party support for plugins, skills, and hooks — the foundation that the rest of today's trending list (karpathy-skills, hyperframes, claude-mem, agency-agents, game studios) extends. The official status guarantees long-term alignment with new Claude model releases.

---

> **Day's theme:** Today's board is a cross-section of the Claude Code skill economy. The top spot (andrej-karpathy-skills) and 7 of the top 25 entries (hyperframes, superpowers, awesome-design-md, android-reverse-engineering-skill, claude-mem, agency-agents, Claude-Code-Game-Studios, and claude-code itself) are directly Claude Code plugins, skills, or the host CLI — a concentration that shows the ecosystem has crossed from novelty to daily tooling. Alongside skills, two other threads dominate: agent self-evolution and memory (evolver, cognee, claude-mem, hermes-agent, GenericAgent) and open-source alternatives to closed-stack verticals (PLFM_RADAR vs defense radar, FinceptTerminal vs Bloomberg, opensre vs vendor AI SRE, rustdesk vs TeamViewer). Scattered among them, frontier research (lingbot-map's streaming 3D reconstruction) and curricula (ai-engineering-from-scratch, dive-into-llms) remind us that the substrate underneath all the agents is still actively being written.
