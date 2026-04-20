# Trendshift Report — 2026-04-13
**Total:** 25 repos

---

## 1. [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
> A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**Language:** N/A  |  **Stars:** 54,695  |  **Forks:** 4,633  |  **Score:** 25,896  |  **Created:** 2026-01-27

**Background:** Karpathy-Inspired Claude Code Guidelines distills Andrej Karpathy's widely-shared X thread on LLM coding pitfalls into a single CLAUDE.md drop-in file. The project surged past 54,000 stars as developers reached for an authoritative, minimal ruleset rather than hand-rolling project memory.

**Problem it solves:** LLMs routinely make silent assumptions, overcomplicate APIs, and edit or delete code they do not understand — side effects that compound across sessions. Generic "be careful" instructions do not target these specific failure modes, so teams end up rewriting the same guardrails repeatedly.

**Why another one?** The file encodes four testable principles — Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution — each mapped to a specific Karpathy observation. It installs as a Claude Code plugin or a literal CLAUDE.md file, making authoritative advice instantly portable across projects.

---

## 2. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> from vibe coding to agentic engineering - practice makes claude perfect

**Language:** HTML  |  **Stars:** 45,972  |  **Forks:** 4,468  |  **Score:** 14,084  |  **Created:** 2025-10-31

**Background:** Claude Code Best Practice is a living catalog that walks readers from "vibe coding" to disciplined agentic engineering, with best-practice docs and ready-to-use implementations for every Claude Code primitive. The repo reached 45,000 stars by pairing conceptual guides with working examples under `.claude/agents`, `.claude/commands`, `.claude/skills`, and `.claude/hooks`.

**Problem it solves:** Claude Code exposes many primitives — subagents, commands, skills, workflows, hooks, MCP servers — and the official docs explain each in isolation. Developers assembling a real workflow have to discover conventions, file layouts, and orchestration patterns by trial and error.

**Why another one?** This repo gives every primitive a best-practice doc plus a matching implementation, including a full orchestration-workflow example. It tracks upstream Claude Code releases aggressively (current badge shows v2.1.114), and every tag in the README links to the actual source file so readers can copy-paste rather than interpret prose.

---

## 3. [hermes-agent](https://github.com/NousResearch/hermes-agent)
> The agent that grows with you

**Language:** Python  |  **Stars:** 97,902  |  **Forks:** 13,800  |  **Score:** 12,357  |  **Created:** 2025-07-22

**Background:** Hermes Agent from Nous Research is now approaching 100,000 stars, positioning itself as the flagship self-improving AI agent with a built-in learning loop. It creates skills from experience, improves them during use, nudges itself to persist knowledge, and builds deepening user models across sessions.

**Problem it solves:** Most agents reset every session — no skills accumulate, no user model sharpens, no knowledge persists. This traps users in a loop of re-explaining context and prevents agents from becoming more capable over time.

**Why another one?** Hermes is the only major agent with a closed learning loop — FTS5 cross-session search, Honcho dialectic user modeling, autonomous skill creation, and compatibility with the agentskills.io standard. It runs on a $5 VPS, Docker, SSH, Daytona, Singularity, or Modal, and fronts Telegram, Discord, Slack, WhatsApp, Signal, and a full TUI from a single gateway.

---

## 4. [Kronos](https://github.com/shiyu-coder/Kronos)
> Kronos: A Foundation Model for the Language of Financial Markets

**Language:** Python  |  **Stars:** 18,980  |  **Forks:** 3,473  |  **Score:** 8,974  |  **Created:** 2025-07-01

**Background:** Kronos is the first open-source foundation model for financial candlesticks (K-lines), trained on data from over 45 global exchanges. Accepted to AAAI 2026, it treats OHLCV sequences as a specialized "language" with its own tokenizer and autoregressive Transformer.

**Problem it solves:** General-purpose time-series foundation models handle financial data poorly because markets are exceptionally noisy, multidimensional, and regime-shifting. Most quant teams end up building bespoke models per task (prediction, regime detection, risk), duplicating effort across firms.

**Why another one?** Kronos's two-stage design — a hierarchical tokenizer that quantizes continuous OHLCV into discrete tokens, followed by a decoder-only Transformer — yields a unified model that fine-tunes to many quantitative tasks. A family of sizes ships on Hugging Face with a live BTC/USDT demo, making it immediately accessible to researchers and traders.

---

## 5. [markitdown](https://github.com/microsoft/markitdown)
> Python tool for converting files and office documents to Markdown.

**Language:** Python  |  **Stars:** 112,434  |  **Forks:** 7,270  |  **Score:** 7,522  |  **Created:** 2024-11-13

**Background:** MarkItDown from Microsoft's AutoGen team has crossed 112,000 stars as the de facto utility for converting files to Markdown for LLM pipelines. A companion markitdown-mcp server now exposes the converter directly to LLM clients like Claude Desktop.

**Problem it solves:** LLMs consume Markdown most efficiently, but the world stores documents in PDF, Word, Excel, PowerPoint, images, audio, HTML, and ZIPs. Converting these manually — or glueing together ad hoc extractors — is lossy, tedious, and inconsistent across document types.

**Why another one?** MarkItDown preserves document structure (headings, lists, tables, links) rather than dumping raw text, and ships a plugin architecture so teams install only the converters they need. The new streaming API and MCP server integration make it the cleanest bridge between enterprise documents and modern agent pipelines.

---

## 6. [caveman](https://github.com/JuliusBrussee/caveman)
> why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**Language:** Python  |  **Stars:** 37,069  |  **Forks:** 1,789  |  **Score:** 6,875  |  **Created:** 2026-04-04

**Background:** Caveman is a Claude Code skill (and Codex plugin) that makes coding agents talk like a caveman, cutting roughly 75% of output tokens while preserving technical accuracy. Nine days after launch it sits at 37,000 stars and now ships a full ecosystem — `cavemem` for memory and `cavekit` for development workflows.

**Problem it solves:** Agent replies default to verbose, polite prose — "Sure! I'd be happy to help you with that…" — which bloats token bills and slows long sessions. The information density of useful agent output is far lower than the byte count suggests.

**Why another one?** Caveman's approach is linguistic rather than architectural: teach the agent to drop filler and grammatical scaffolding, and tokens fall dramatically with zero accuracy loss. It also bundles `caveman-compress` (46% input-token cut), `caveman-commit`, `caveman-review`, and a wenyan (文言文) mode, installs in one line, and is compatible with Claude Code and Codex.

---

## 7. [claude-mem](https://github.com/thedotmack/claude-mem)
> A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**Language:** TypeScript  |  **Stars:** 61,190  |  **Forks:** 5,065  |  **Score:** 6,496  |  **Created:** 2025-08-31

**Background:** Claude-Mem is a persistent memory compression system purpose-built for Claude Code, now above 61,000 stars and translated into over 30 languages. It hooks into every session, uses the Claude agent-sdk to compress observations, and injects the most relevant context into future sessions automatically.

**Problem it solves:** Claude Code sessions are episodic — context is dropped when a session ends, and developers end up re-describing their codebase, past decisions, and stylistic preferences each time. Long projects pay a repeated onboarding tax that manual /memory commands only partially solve.

**Why another one?** Claude-Mem runs the capture-compress-inject loop automatically with no manual bookkeeping, using Claude itself to summarize and rank what matters. Its plugin form factor means zero code changes for users, and the agent-sdk integration keeps summaries aligned with Claude's own retrieval heuristics.

---

## 8. [VoxCPM](https://github.com/OpenBMB/VoxCPM)
> VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-Life Cloning

**Language:** Python  |  **Stars:** 14,077  |  **Forks:** 1,683  |  **Score:** 6,148  |  **Created:** 2025-09-16

**Background:** VoxCPM2 from OpenBMB is a 2B-parameter tokenizer-free TTS model trained on over 2 million hours of multilingual speech, now supporting 30 languages, voice design from text, controllable cloning, and 48kHz studio-quality output. It builds on a MiniCPM-4 backbone and uses an end-to-end diffusion autoregressive architecture.

**Problem it solves:** Discrete token-based TTS systems bottleneck on their tokenizer — quality, expressiveness, and languages coverage are all capped by the tokenization stage. Existing open systems also struggle with fine-grained voice control and studio-grade fidelity.

**Why another one?** VoxCPM2 bypasses discrete tokens entirely, generating continuous speech representations directly. Voice Design lets users create new voices from natural-language descriptions (no reference audio needed), and built-in super-resolution from 16kHz input to 48kHz output eliminates external upsamplers. Real-time streaming runs at ~0.3 RTF on a 4090, accelerating to ~0.13 with vLLM-Omni.

---

## 9. [awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
> A collection of DESIGN.md files inspired by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.

**Language:** N/A  |  **Stars:** 58,491  |  **Forks:** 7,288  |  **Score:** 5,215  |  **Created:** 2026-03-31

**Background:** Awesome DESIGN.md is a curated collection of DESIGN.md files extracted from real websites and brand systems, designed to be dropped into a project so AI coding agents can generate pixel-matching UI. The repo jumped to 58,000 stars within two weeks of launch as DESIGN.md gained traction alongside Google Stitch.

**Problem it solves:** AGENTS.md tells an agent how to build, but nothing tells it how things should look. Without a design spec, agents produce generic UIs that clash with a project's brand, and designers cannot hand off aesthetics through Figma exports that agents do not read.

**Why another one?** DESIGN.md is plain markdown — the format LLMs read best — so there is no schema, no plugin, no Figma integration required. This repo ships 69 ready-to-use files covering AI platforms, dev tools, and consumer brands, turning an entire class of brand aesthetics into copy-paste project fixtures.

---

## 10. [mempalace](https://github.com/MemPalace/mempalace)
> The best-benchmarked open-source AI memory system. And it's free.

**Language:** Python  |  **Stars:** 47,614  |  **Forks:** 6,217  |  **Score:** 4,983  |  **Created:** 2026-04-05

**Background:** MemPalace is a local-first AI memory system that stores conversation history verbatim and retrieves it via semantic search, scoring 96.6% R@5 on LongMemEval without any API calls. Eight days after launch it has drawn 47,000 stars, positioning itself as the highest-benchmarked open memory layer.

**Problem it solves:** Most AI memory systems summarize or paraphrase, losing the exact quote, decision, or context the user needs later. They also typically require cloud APIs for embeddings or reasoning, leaking private data and adding cost per recall.

**Why another one?** MemPalace keeps the original text verbatim and organizes it spatially — people and projects become wings, topics become rooms, and content lives in drawers — so searches can be scoped instead of run against a flat corpus. The retrieval backend is pluggable (ChromaDB default), nothing leaves the machine unless opted in, and the install is two commands from `pip` to working memory.

---

## 11. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 157,560  |  **Forks:** 13,696  |  **Score:** 4,724  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent (obra) has grown to 157,000 stars as a complete software development methodology built on composable skills. It is distributed through Anthropic's official Claude plugin marketplace and now supports Codex CLI as well.

**Problem it solves:** Coding agents jump straight to writing code without clarifying intent, producing plans, or planning verification — the exact opposite of how senior engineers work. Ad-hoc prompts cannot reliably enforce TDD, YAGNI, and DRY across long autonomous runs.

**Why another one?** Superpowers replaces prompts with skills that trigger automatically based on the current phase — specification, planning, implementation, review. Its subagent-driven-development process lets Claude work autonomously for hours at a time without deviating from the human-approved plan, and the methodology is shaped by explicit research on where agents typically fail.

---

## 12. [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)
> An AI Hedge Fund Team

**Language:** Python  |  **Stars:** 56,277  |  **Forks:** 9,771  |  **Score:** 4,434  |  **Created:** 2024-11-29

**Background:** AI Hedge Fund simulates a full investment committee with 19 specialized agents, each modeling a famous investor's philosophy — Warren Buffett, Cathie Wood, Michael Burry, Nassim Taleb, and more — plus valuation, sentiment, risk, and portfolio management agents. It has crossed 56,000 stars as a go-to template for multi-agent reasoning systems.

**Problem it solves:** Single-agent trading systems produce brittle, single-perspective signals that miss the adversarial debate real investment committees provide. Researchers also lack a rich, well-structured benchmark for multi-agent coordination on a recognizable task.

**Why another one?** The agent cast is unusually wide (19 distinct philosophies), each prompt encoding a specific investor's documented reasoning style. The system ships both a CLI and a web application, makes zero real trades, and is explicitly framed as an educational sandbox for AI-on-markets research — which is why it has become a popular reference implementation for multi-agent architectures.

---

## 13. [ralph](https://github.com/snarktank/ralph)
> Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete.

**Language:** TypeScript  |  **Stars:** 17,120  |  **Forks:** 1,704  |  **Score:** 4,386  |  **Created:** 2026-01-07

**Background:** Ralph is an autonomous AI agent loop that runs Amp or Claude Code repeatedly until every PRD item is complete, based on Geoffrey Huntley's Ralph pattern. Each iteration is a fresh instance with clean context; memory persists via git history, `progress.txt`, and `prd.json`.

**Problem it solves:** Long-running agent sessions drift as context fills up — models hallucinate, revisit closed issues, or lose track of the plan. Ad-hoc restart strategies reset too much or not enough, making unattended multi-hour runs unreliable.

**Why another one?** Ralph's design is aggressively stateless: fresh context every iteration, with state externalized into a structured PRD and plain-text progress log. It ships as a Claude Code marketplace plugin with `/prd` and `/ralph` skills, supports Amp auto-handoff, and deliberately limits the agent to one small loop that is easy to inspect and resume.

---

## 14. [CorridorKey](https://github.com/nikopueringer/CorridorKey)
> Perfect Green Screen Keys

**Language:** Python  |  **Stars:** 11,139  |  **Forks:** 671  |  **Score:** 4,272  |  **Created:** 2026-02-25

**Background:** CorridorKey from Corridor Digital is a neural green-screen keyer that solves the "unmixing" problem — separating foreground color from green spill at every pixel, including semi-transparent ones like motion blur and out-of-focus edges. It outputs linear alpha and straight color in 16/32-bit EXR for direct use in Nuke, Fusion, or Resolve.

**Problem it solves:** Traditional chroma keyers produce harsh binary mattes and destroy edge transparency, forcing hours of garbage-matte painting or rotoscoping. Even modern "AI Roto" tools output binary masks, losing the physically correct color math needed for believable VFX composites.

**Why another one?** CorridorKey is a physically-accurate unmixer rather than a mask generator — for every pixel it reconstructs the foreground's true un-multiplied color as if the green screen were never there. It runs resolution-independently at a native 2048² backbone, scaling up to 4K plates, and supports NVIDIA CUDA, AMD ROCm, and Apple Silicon unified memory.

---

## 15. [claude-cookbooks](https://github.com/anthropics/claude-cookbooks)
> A collection of notebooks/recipes showcasing some fun and effective ways of using Claude.

**Language:** Jupyter Notebook  |  **Stars:** 40,904  |  **Forks:** 4,513  |  **Score:** 4,236  |  **Created:** 2023-08-15

**Background:** Claude Cookbooks is Anthropic's official collection of notebooks and recipes for building with the Claude API, now at nearly 41,000 stars. It covers classification, RAG, summarization, tool use, multimodal vision, and third-party integrations (Pinecone, Wikipedia, Voyage embeddings).

**Problem it solves:** API documentation shows you how endpoints work but rarely shows end-to-end recipes for realistic tasks — an agent that calls SQL, an extractor that cites sources, a vision pipeline that grades charts. Developers end up building these from scratch each time.

**Why another one?** As the first-party cookbook, it ships reference implementations that track Claude's latest features, including prompt caching, tool use patterns, and structured outputs. Its copy-pasteable notebooks plus links to the Fundamentals course make it the canonical starting point, and the breadth of third-party integrations removes lock-in concerns.

---

## 16. [multica](https://github.com/multica-ai/multica)
> The open-source managed agents platform. Turn coding agents into real teammates — assign tasks, track progress, compound skills.

**Language:** TypeScript  |  **Stars:** 15,307  |  **Forks:** 1,889  |  **Score:** 4,213  |  **Created:** 2026-01-13

**Background:** Multica is an open-source managed agents platform that treats coding agents as teammates — they have profiles, pick up issues off a board, post comments, and report blockers autonomously. The tagline "your next 10 hires won't be human" captures its positioning as infrastructure for human + AI engineering teams.

**Problem it solves:** Running coding agents today means copy-pasting prompts, babysitting terminal windows, and losing work when a run fails. There is no shared visibility, no task lifecycle, and no way for multiple agents to accumulate reusable team skills.

**Why another one?** Multica manages the full agent lifecycle with WebSocket progress streaming, multi-workspace isolation, and an auto-detecting runtime layer for local and cloud compute. It is vendor-neutral — Claude Code, Codex, OpenClaw, OpenCode, Hermes, Gemini, Pi, and Cursor Agent all plug in — and ships as a Homebrew install with a self-hosted or cloud option.

---

## 17. [voicebox](https://github.com/jamiepine/voicebox)
> The open-source voice synthesis studio

**Language:** TypeScript  |  **Stars:** 19,836  |  **Forks:** 2,278  |  **Score:** 4,064  |  **Created:** 2026-01-25

**Background:** Voicebox from Jamie Pine is a local-first voice cloning studio positioned as a free, open-source alternative to ElevenLabs. It bundles 7 TTS engines, 50+ preset voices, 23 languages, timeline-based multi-voice editing, and a REST API, all running natively on the user's machine.

**Problem it solves:** Commercial voice services are expensive, rate-limited, and require uploading sensitive voice data to the cloud. Existing local TTS tools are fragmented — one project per engine, no unified UI, no effects chain, and no project file for multi-voice composition.

**Why another one?** Voicebox unifies Qwen3-TTS, Qwen CustomVoice, LuxTTS, Chatterbox, HumeAI TADA, and Kokoro behind one app, with post-processing (pitch, reverb, delay, compression), paralinguistic tags like `[laugh]`, and a Stories editor for conversations. It is built in Tauri (Rust) for native performance and runs on CUDA, MLX/Metal, ROCm, and Intel Arc.

---

## 18. [hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution)
> Evolutionary self-improvement for Hermes Agent — optimize skills, prompts, and code using DSPy + GEPA

**Language:** Python  |  **Stars:** 1,870  |  **Forks:** 177  |  **Score:** 3,876  |  **Created:** 2026-03-09

**Background:** Hermes Agent Self-Evolution applies DSPy + GEPA (Genetic-Pareto Prompt Evolution, ICLR 2026 Oral) to automatically evolve Hermes Agent's skills, tool descriptions, system prompts, and code. Optimization runs use API calls only — no GPU training — at roughly $2-10 per run.

**Problem it solves:** Agent skills and prompts are authored once and then slowly rot as models, tools, and tasks change. Humans rarely have the time or telemetry discipline to continuously regenerate them, so skill quality drifts below what the current model could produce.

**Why another one?** GEPA reads execution traces to understand *why* things fail and proposes targeted mutations, rather than brute-force prompt search. Every evolved variant must pass the full test suite, size limits, and semantic-preservation checks before being PR'd, yielding an auditable continuous-improvement pipeline tailored for Hermes but generalizable.

---

## 19. [agent-skills](https://github.com/addyosmani/agent-skills)
> Production-grade engineering skills for AI coding agents.

**Language:** Shell  |  **Stars:** 17,291  |  **Forks:** 2,185  |  **Score:** 3,561  |  **Created:** 2026-02-15

**Background:** Agent Skills from Addy Osmani encodes senior-engineering workflows — spec, plan, build, test, review, ship — as production-grade skills for AI coding agents. Seven slash commands map to the full development lifecycle, with skills activating automatically based on what the agent is working on.

**Problem it solves:** Without explicit engineering guardrails, coding agents produce code that skips specs, skips tests, or refactors recklessly. Generic "be a senior engineer" prompts do not deliver consistent quality gates across design, implementation, and review phases.

**Why another one?** Each skill encodes a specific engineering principle — "spec before code", "small atomic tasks", "tests are proof", "clarity over cleverness" — and domain skills auto-activate for API design, frontend, and backend tasks. It installs via Claude Code marketplace, Cursor rules, or Gemini CLI native skills, giving every major agent platform the same production-grade playbook.

---

## 20. [ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook)
> 所有小初高、大学PDF教材。

**Language:** Roff  |  **Stars:** 70,025  |  **Forks:** 15,652  |  **Score:** 3,376  |  **Created:** 2020-01-05

**Background:** ChinaTextbook is a 70,000-star archive of every Chinese primary, middle, high school, and university textbook as PDFs, organized by grade and subject. It has grown steadily since 2020 as the reference resource for Chinese educational materials outside mainland distribution.

**Problem it solves:** Although domestic Chinese education sites host these textbooks for free, practical access is limited and third parties re-sell watermarked versions for profit. Overseas Chinese families in particular struggle to find clean, complete materials to keep children connected to mainland curricula.

**Why another one?** The project centralizes and open-sources the full K-12 and college catalog in one repository, removing paywalls and watermarks while preserving the official publisher versions. Its scope — every subject, every grade — makes it a single URL reference rather than a scattered collection, and the 15,000+ forks suggest heavy mirroring for resilience.

---

## 21. [airllm](https://github.com/lyogavin/airllm)
> AirLLM 70B inference with single 4GB GPU

**Language:** Jupyter Notebook  |  **Stars:** 16,393  |  **Forks:** 1,723  |  **Score:** 3,324  |  **Created:** 2023-06-12

**Background:** AirLLM optimizes inference memory usage so 70B-parameter LLMs run on a single 4GB GPU — and Llama 3.1 405B on 8GB of VRAM — all without quantization, distillation, or pruning. It supports Llama, Qwen2.5, Mixtral, ChatGLM, Baichuan, Mistral, InternLM, and runs on macOS.

**Problem it solves:** Running frontier-size open models locally usually requires $10,000+ of GPU hardware, or forces users into lossy quantization that degrades accuracy. This puts state-of-the-art LLMs out of reach for hobbyists and small teams with gaming-class GPUs.

**Why another one?** AirLLM achieves memory reduction through layerwise loading and prefetching, streaming weights on and off the GPU during generation rather than compressing them. Loss-free full-precision 70B inference on a $200 GPU is a qualitatively different accessibility regime, and the project has tracked every new model family over three years of updates.

---

## 22. [Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)
> "Vibe-Trading: Your Personal Trading Agent"

**Language:** Python  |  **Stars:** 2,084  |  **Forks:** 477  |  **Score:** 3,231  |  **Created:** 2026-04-01

**Background:** Vibe-Trading from HKUDS packages 71 skills, 29 swarm presets, 27 tools, and 5 data sources into a single-command trading agent with FastAPI backend and React 19 frontend. Recent releases added shadow-account backtesting, a trade journal analyzer, and a universal document reader covering PDF, Word, Excel, PowerPoint, and OCR'd images.

**Problem it solves:** Retail traders lack systematic tools to extract their own strategy rules, backtest alternative decisions, and quantify behavioral biases. Professional research platforms are expensive and closed, and stitching together open pieces (brokers, charting, bias analysis, reports) is beyond most individuals.

**Why another one?** Vibe-Trading ships a shadow-account tool that extracts your strategy from a broker journal, backtests it across markets, and produces an 8-section HTML/PDF showing exactly how much you leave on the table through rule violations or early exits. It installs via `pip install vibe-trading-ai`, exposes 22 MCP tools for Claude and other agents, and integrates broker exports from 同花顺, 东财, and 富途.

---

## 23. [code-review-graph](https://github.com/tirth8205/code-review-graph)
> Local knowledge graph for Claude Code. Builds a persistent map of your codebase so Claude reads only what matters — 6.8× fewer tokens on reviews and up to 49× on daily coding tasks.

**Language:** Python  |  **Stars:** 10,806  |  **Forks:** 1,213  |  **Score:** 3,032  |  **Created:** 2026-02-26

**Background:** Code-review-graph builds a Tree-sitter-based structural map of a codebase, tracks changes incrementally, and exposes MCP tools so AI assistants read only the relevant subgraph. Benchmarks show 8.2× average token reduction across 6 real repositories, with up to 49× on daily coding tasks.

**Problem it solves:** AI coding tools re-read the entire codebase (or large chunks of it) on every task, burning tokens and latency on files that have nothing to do with the change at hand. Naive file search returns too much, grep returns too little, and neither understands semantic scope.

**Why another one?** A structural knowledge graph gives the assistant precise context — the functions a change touches, their callers, their tests — without shipping whole files. One `install` command auto-configures every supported platform (Codex, Claude Code, Cursor, Windsurf, Zed, Continue, OpenCode, Antigravity, Qwen, Qoder, Kiro), and the incremental update keeps the graph fresh during active development.

---

## 24. [gbrain](https://github.com/garrytan/gbrain)
> Garry's Opinionated OpenClaw/Hermes Agent Brain

**Language:** TypeScript  |  **Stars:** 9,171  |  **Forks:** 1,057  |  **Score:** 2,923  |  **Created:** 2026-04-05

**Background:** GBrain is the production memory layer powering Y Combinator CEO Garry Tan's personal AI agents — 17,888 pages, 4,383 people, 723 companies, and 21 autonomous cron jobs built in 12 days. It is packaged as 26 skills plus an MCP server exposing 30+ tools over stdio or remote HTTP.

**Problem it solves:** Agents that ingest meetings, emails, tweets, and voice calls accumulate unstructured memory that vector search alone cannot navigate — questions like "who works at Acme?" or "what did Bob invest in?" require typed relationships and a real knowledge graph. Most memory systems stop at RAG.

**Why another one?** GBrain wires itself: every page write extracts entity references and creates typed links (`attended`, `works_at`, `invested_in`, `founded`, `advises`) with zero LLM calls. Benchmarks show Recall@5 rising from 83% to 95% and graph-only F1 of 86.6% vs grep's 57.8%. It runs on PGLite with no server and installs in ~30 minutes, including on OpenClaw and Hermes agent platforms.

---

## 25. [fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)
> Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.

**Language:** Python  |  **Stars:** 3,677  |  **Forks:** 321  |  **Score:** 2,865  |  **Created:** 2026-04-10

**Background:** Fireworks-tech-graph is a Claude Code skill that turns natural-language descriptions (English or Chinese) into publication-ready SVG diagrams, then exports high-resolution PNGs via `rsvg-convert`. It ships with 7 visual styles and full support for all 14 UML diagram types, with built-in knowledge of AI/Agent patterns like RAG, Mem0, and Multi-Agent flows.

**Problem it solves:** Technical writers and engineers spend hours hand-drawing architecture diagrams in Excalidraw, Figma, or draw.io — and the results rarely match the polish of commercial tech-company diagrams. Existing text-to-diagram tools (Mermaid, PlantUML) produce generic output that looks nothing like the brand styles people actually want to reproduce.

**Why another one?** The skill classifies the request (e.g. "Memory Architecture Diagram, Style 2"), generates proper SVG (swim lanes, cylinders, semantic arrows), and exports a 1920px retina PNG in seconds. Seven styles — Flat Icon, Dark Terminal, Blueprint, Notion Clean, Glassmorphism, Claude Official, OpenAI Official — cover the dominant aesthetics of modern AI company diagrams.

---

> **Day's theme:** Skills, memory, and token economics dominate today's chart. The top of the list reads like a skills catalog — Karpathy-Inspired Guidelines, Claude Code Best Practice, Caveman, Superpowers, Claude-Mem, Agent Skills, Fireworks Tech Graph — while the middle holds a new wave of memory systems (MemPalace, Claude-Mem, GBrain, code-review-graph) explicitly measuring themselves on recall benchmarks rather than shipping black-box RAG. The Hermes Agent ecosystem now spans three repos on today's board (core agent, self-evolution, plus supporting tools like Multica and GBrain), hinting at a standardized self-improving agent stack. Finance shows up in three distinct flavors — Kronos as a financial foundation model, AI Hedge Fund as a multi-agent committee, Vibe-Trading as a personal trading skill bundle — and VFX (CorridorKey) plus TTS (VoxCPM2, Voicebox) confirm local-first creative tooling remains a durable trending category alongside the dominant AI-agent narrative.
