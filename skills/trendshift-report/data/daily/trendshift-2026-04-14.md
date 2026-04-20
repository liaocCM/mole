# Trendshift Report — 2026-04-14
**Total:** 25 repos

---

## 1. [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
> A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**Language:** N/A  |  **Stars:** 54,695  |  **Forks:** 4,633  |  **Score:** 67,334  |  **Created:** 2026-01-27

**Background:** This project distills Andrej Karpathy's widely-shared observations about LLM coding pitfalls into a single CLAUDE.md file that improves Claude Code behavior. Now at nearly 55,000 stars — up roughly 40,000 in under three months — it has become a de facto starting configuration for developers who want opinionated guardrails without writing their own.

**Problem it solves:** LLMs make wrong assumptions without checking, overcomplicate APIs and abstractions, produce bloated code where concise solutions exist, and silently change or remove comments and code they do not understand. These failure modes compound across sessions, degrading codebase quality over time.

**Why another one?** The project packages authoritative observations from one of the most respected voices in AI into an immediately actionable format — a single file dropped into any project. Unlike general-purpose guidelines, these rules target specific, documented failure modes with concrete countermeasures, and the rapid star growth reflects how directly the rules match developers' lived frustrations.

---

## 2. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> from vibe coding to agentic engineering - practice makes claude perfect

**Language:** HTML  |  **Stars:** 45,972  |  **Forks:** 4,468  |  **Score:** 21,119  |  **Created:** 2025-10-31

**Background:** Claude Code Best Practice is a comprehensive guide for moving from vibe coding to agentic engineering, continuously updated to match the latest Claude Code releases. With nearly 46,000 stars, it provides best practices, implementation guides, and orchestration workflows that give teams a structured learning path rather than a scattered reference.

**Problem it solves:** Developers using Claude Code often default to unstructured prompting — "vibe coding" — which produces inconsistent results. Without systematic practices for requirements specification, orchestration, and quality control, the AI agent becomes a fast but undisciplined coder whose output varies wildly across runs.

**Why another one?** The project is continuously updated with version-tagged badges showing currency, and its structured progression from best practices to implementation to orchestration workflows mirrors how professional engineering teams actually onboard new members. It is a curriculum for agentic engineering rather than a reference document.

---

## 3. [hermes-agent](https://github.com/NousResearch/hermes-agent)
> The agent that grows with you

**Language:** Python  |  **Stars:** 97,902  |  **Forks:** 13,800  |  **Score:** 19,231  |  **Created:** 2025-07-22

**Background:** Hermes Agent by Nous Research is a self-improving AI agent with a built-in learning loop that creates skills from experience and builds a deepening model of the user across sessions. Approaching 100,000 stars, it is the largest project in the growing category of agents that improve themselves during use rather than starting fresh every session.

**Problem it solves:** AI agents start from zero in every session — they do not remember past interactions, learn from mistakes, or adapt to user preferences. This forces users to re-explain context repeatedly and prevents the agent from developing domain expertise over time.

**Why another one?** Hermes Agent's learning loop is its core differentiator: it creates skills from experience, improves them during use, and builds persistent user models across sessions. It runs on any infrastructure from a $5 VPS to a GPU cluster, supports 200+ models via OpenRouter, and operates across Telegram, Discord, Slack, WhatsApp, and Signal from a single gateway.

---

## 4. [magika](https://github.com/google/magika)
> Fast and accurate AI powered file content types detection

**Language:** Python  |  **Stars:** 15,947  |  **Forks:** 895  |  **Score:** 11,862  |  **Created:** 2023-08-22

**Background:** Magika by Google is a deep-learning file type detection tool with a custom model weighing only a few megabytes. Now at nearly 16,000 stars and distributed as PyPI, npm, and Go packages, it has become a widely adopted replacement for traditional magic-byte libraries in security and content pipelines.

**Problem it solves:** Identifying file types from raw bytes is a classic problem where traditional tools (libmagic, file(1)) rely on hand-crafted signatures that miss edge cases, misclassify obfuscated content, and fail on newer formats. Security scanners and data pipelines need accurate type detection to route content correctly.

**Why another one?** Magika's ML-based approach generalizes across formats rather than matching fixed signatures, and Google's continuous investment keeps the model up to date. The multi-language distribution (Python, Node, Go) and CLI tool make it drop-in compatible with existing pipelines regardless of their runtime.

---

## 5. [claude-mem](https://github.com/thedotmack/claude-mem)
> A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**Language:** TypeScript  |  **Stars:** 63,104  |  **Forks:** 5,284  |  **Score:** 11,070  |  **Created:** 2025-08-31

**Background:** Claude-Mem is a Claude Code plugin that automatically captures session activity, compresses it with AI, and injects relevant context back into future sessions. At over 63,000 stars and translated into more than 15 languages, it has become one of the dominant memory plugins for Claude Code users who want continuity without manual note-taking.

**Problem it solves:** Claude Code sessions end with full context, but the next session starts blank — every decision, debugging insight, and architectural choice must be re-explained. Manual context files go stale, and developers waste the first minutes of each session recreating state instead of making progress.

**Why another one?** Claude-Mem automates the full capture-compress-inject cycle using Claude's own agent SDK, eliminating the manual curation step that memory systems typically require. The plugin architecture means it drops directly into Claude Code without external infrastructure, and the compression step keeps token costs low even across long histories.

---

## 6. [caveman](https://github.com/JuliusBrussee/caveman)
> why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**Language:** Python  |  **Stars:** 37,069  |  **Forks:** 1,789  |  **Score:** 10,069  |  **Created:** 2026-04-04

**Background:** Caveman is a Claude Code skill that dramatically reduces token consumption by rewriting agent output in compressed, caveman-style language. Created just ten days ago, it has already doubled from 18,000 to 37,000 stars — a sharp climb reflecting developer interest in cost optimization for AI coding workflows.

**Problem it solves:** AI coding agents are verbose by default, consuming tokens on polite phrasing, redundant explanations, and stylistic flourishes that add no functional value. This drives up API costs and slows down interactions, especially in long sessions with extensive back-and-forth.

**Why another one?** Caveman's approach is uniquely playful yet effective — rather than complex prompt engineering or output filtering, it simply teaches the agent to communicate in compressed language. The claimed 65% token reduction translates directly to cost savings, and the skill installs with a single command into any Claude Code setup.

---

## 7. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 159,794  |  **Forks:** 13,929  |  **Score:** 8,926  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent is a complete software development workflow for coding agents, now at nearly 160,000 stars. It enforces a structured process — spec extraction, design review in digestible chunks, implementation planning, and supervised subagent execution — that prevents agents from jumping straight into code.

**Problem it solves:** AI coding agents jump directly into writing code without proper planning, producing solutions that miss requirements or need extensive rework. The enthusiasm-without-judgment pattern leads to code that works in isolation but fails in production contexts.

**Why another one?** Superpowers' subagent-driven development is its key differentiator — it launches sub-agents for each engineering task, inspects their work, and continues autonomously. The skills trigger automatically based on context, and the framework supports Claude Code, Cursor, Codex, and OpenCode, making it the most broadly compatible skills framework available.

---

## 8. [awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
> A collection of DESIGN.md files inspired by popular brand design systems. Drop one into your project and let coding agents generate a matching UI.

**Language:** N/A  |  **Stars:** 58,491  |  **Forks:** 7,288  |  **Score:** 8,727  |  **Created:** 2026-03-31

**Background:** Awesome DESIGN.md is a curated collection of DESIGN.md files that capture design systems from popular websites, maintained by VoltAgent. Now at nearly 59,000 stars just two weeks after launch, it has become a standard resource for developers who want AI agents to generate UI matching real-world design systems.

**Problem it solves:** AI coding agents produce generic, inconsistent UI because they lack visual design context. Developers either describe designs in prose (which agents interpret loosely) or export Figma files (which agents cannot read). DESIGN.md files give agents structured design specifications in the format LLMs read best — markdown.

**Why another one?** The project provides ready-to-use design system files extracted from real websites rather than requiring developers to write their own. Dropping one into a project gives any AI coding agent immediate access to a complete design system, bridging the gap between how agents build and how interfaces should look.

---

## 9. [claude-cookbooks](https://github.com/anthropics/claude-cookbooks)
> A collection of notebooks/recipes showcasing some fun and effective ways of using Claude.

**Language:** Jupyter Notebook  |  **Stars:** 41,065  |  **Forks:** 4,543  |  **Score:** 8,458  |  **Created:** 2023-08-15

**Background:** Claude Cookbooks by Anthropic is the official collection of notebooks and recipes showcasing effective ways of using Claude. At over 41,000 stars, it is the reference implementation resource for developers building on the Anthropic API — covering RAG, tool use, multimodal workflows, and production patterns.

**Problem it solves:** Developers exploring the Claude API often learn by trial and error, rediscovering patterns that Anthropic has already documented. Without official recipes, teams reinvent prompt structures, retrieval strategies, and evaluation harnesses that could be borrowed from canonical examples.

**Why another one?** As the first-party resource from the model provider, Claude Cookbooks carries authority that community examples cannot match — patterns here reflect how Anthropic itself recommends using the API. The Jupyter notebook format makes each recipe immediately runnable, lowering the barrier from reading to prototyping.

---

## 10. [ChinaTextbook](https://github.com/TapXWorld/ChinaTextbook)
> Collection of all Chinese primary, middle school, high school, and university PDF textbooks.

**Language:** Roff  |  **Stars:** 70,025  |  **Forks:** 15,652  |  **Score:** 5,848  |  **Created:** 2020-01-05

**Background:** ChinaTextbook is an open-source collection of Chinese education textbooks in PDF format, covering primary school through university. With over 70,000 stars and 15,000 forks, it is one of the most popular educational resource repositories on GitHub, serving both domestic students and overseas Chinese families.

**Problem it solves:** While Chinese educational websites provide free resources, access remains limited for many people, and some sellers repackage these public resources with private watermarks for profit. This project centralizes and open-sources the materials to promote educational equity and eliminate regional education poverty.

**Why another one?** The project specifically addresses the needs of overseas Chinese families who want their children to continue learning the Chinese curriculum. By hosting materials on GitHub, it provides globally accessible, free educational resources that cannot be paywalled or restricted by regional content delivery networks.

---

## 11. [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)
> An AI Hedge Fund Team

**Language:** Python  |  **Stars:** 56,277  |  **Forks:** 9,771  |  **Score:** 5,484  |  **Created:** 2024-11-29

**Background:** AI Hedge Fund is a proof-of-concept AI-powered hedge fund team with over 56,000 stars. It employs multiple agents modeled after famous investors — Aswath Damodaran, Ben Graham, Bill Ackman, Cathie Wood, Charlie Munger — each applying their distinct investment philosophies to analyze stocks and make trading decisions.

**Problem it solves:** Investment analysis requires synthesizing multiple frameworks — value investing, growth investing, activist strategies, quantitative analysis — that individual analysts rarely master simultaneously. Getting diverse investment perspectives typically requires a large team of specialists.

**Why another one?** The multi-agent approach with named investor personas makes the reasoning process transparent and educational. Users can see how a Graham-style value analysis differs from a Cathie Wood growth thesis on the same stock, making it a learning tool as much as an analysis engine. The educational framing sets clear expectations that this is not real trading software.

---

## 12. [voicebox](https://github.com/jamiepine/voicebox)
> The open-source voice synthesis studio

**Language:** TypeScript  |  **Stars:** 19,836  |  **Forks:** 2,278  |  **Score:** 5,457  |  **Created:** 2026-01-25

**Background:** Voicebox by Jamie Pine is an open-source voice synthesis studio that runs entirely locally — clone voices, generate speech, apply effects, and build voice-powered apps without cloud dependencies. At nearly 20,000 stars, it packages a desktop UI with an API surface, making it both a consumer tool and a developer platform.

**Problem it solves:** Voice synthesis and cloning tools are fragmented between commercial cloud services (expensive, privacy-invasive) and research models (powerful but inaccessible without ML expertise). Developers building voice-powered apps lack a unified local toolchain that handles generation, cloning, and effects in one place.

**Why another one?** Voicebox's local-first architecture avoids the privacy and cost issues of cloud TTS, and the studio UI makes advanced voice work accessible without code. The bundled API lets developers embed voice capabilities into their own apps using the same engine that powers the studio, unifying end-user and developer workflows.

---

## 13. [PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR)
> Open-source, low-cost 10.5 GHz PLFM phased array RADAR system

**Language:** PLSQL  |  **Stars:** 13,824  |  **Forks:** 2,914  |  **Score:** 5,314  |  **Created:** 2026-03-08

**Background:** AERIS-10 (PLFM_RADAR) is an open-source 10.5 GHz phased array radar system with Pulse Linear Frequency Modulated modulation, released under CERN-OHL-P hardware and MIT software licenses. At nearly 14,000 stars in under six weeks, the project has drawn unusual attention for a hardware repo, reflecting growing interest in accessible radar research.

**Problem it solves:** Phased array radar technology has traditionally been confined to defense contractors and national laboratories, with component costs and export controls putting it out of reach for researchers, drone developers, and SDR enthusiasts. Commercial modules exist but are expensive and opaque, blocking experimentation.

**Why another one?** AERIS-10 democratizes phased array radar by publishing schematics, firmware, and PCB designs under permissive licenses, available in 3km and 20km range variants. The modular design lets builders swap components for their specific experiments, and the low-cost bill of materials makes hands-on radar work feasible for hobbyist budgets.

---

## 14. [markitdown](https://github.com/microsoft/markitdown)
> Python tool for converting files and office documents to Markdown.

**Language:** Python  |  **Stars:** 112,434  |  **Forks:** 7,270  |  **Score:** 5,228  |  **Created:** 2024-11-13

**Background:** MarkItDown by Microsoft's AutoGen team is a Python tool that converts files and office documents to Markdown, now past 112,000 stars. It added an MCP server earlier this year for integration with LLM applications like Claude Desktop, making document conversion a native capability for AI workflows.

**Problem it solves:** AI agents and LLMs work best with markdown text but enterprise content lives in Word documents, Excel spreadsheets, PowerPoint presentations, and PDFs. Manual conversion is tedious and lossy, creating a bottleneck when feeding real-world documents into AI pipelines.

**Why another one?** MarkItDown's institutional backing from Microsoft and its integration with the AutoGen ecosystem give it reliability advantages over ad hoc converters. The MCP server makes it directly callable by AI agents, and the modular dependency system lets users install only the converters they need.

---

## 15. [Kronos](https://github.com/shiyu-coder/Kronos)
> Kronos: A Foundation Model for the Language of Financial Markets

**Language:** Python  |  **Stars:** 19,542  |  **Forks:** 3,540  |  **Score:** 4,602  |  **Created:** 2025-07-01

**Background:** Kronos is a foundation model specifically designed for financial market language, providing deep understanding of market dynamics, trading patterns, and financial text. Now at nearly 20,000 stars, it represents a growing trend of domain-specific foundation models trained on specialized corpora rather than general web text.

**Problem it solves:** General-purpose LLMs lack the specialized knowledge needed to interpret financial market language — earnings calls, SEC filings, analyst reports, and trading signals use domain-specific terminology and reasoning patterns that generic models handle poorly, leading to unreliable financial analysis.

**Why another one?** Kronos is purpose-built for financial markets rather than fine-tuned from a general model, giving it native understanding of market-specific concepts. The live demo and Hugging Face integration make it immediately accessible, and its foundation model architecture allows fine-tuning for specific financial sub-domains.

---

## 16. [WeClone](https://github.com/xming521/WeClone)
> One-stop solution for creating your AI twin from chat history. Fine-tune LLMs with your chat logs to capture your unique style, then bind to a chatbot to bring your digital self to life.

**Language:** Python  |  **Stars:** 17,574  |  **Forks:** 1,493  |  **Score:** 4,590  |  **Created:** 2024-01-31

**Background:** WeClone is an end-to-end pipeline for building a digital avatar from chat history — ingest messages, fine-tune a base LLM on your conversational style, and bind the result to a chatbot that imitates you. At over 17,500 stars, it has a large active community in the Chinese-speaking developer ecosystem with QQ, Xiaohongshu, and Telegram channels.

**Problem it solves:** Creating a convincing digital version of yourself requires capturing the specific ways you phrase things, joke, and respond — traits that generic chatbots cannot imitate. Manually crafting prompts to reproduce personal style is impossible at scale, and most fine-tuning toolchains are disconnected from real chat data.

**Why another one?** WeClone integrates the full loop — chat export, data cleaning, fine-tuning, and chatbot deployment — in a single opinionated pipeline rather than expecting users to stitch separate tools together. The focus on chat-history-as-training-data makes it practical for non-ML users to produce a faithful digital twin without understanding the underlying mechanics.

---

## 17. [multica](https://github.com/multica-ai/multica)
> The open-source managed agents platform. Turn coding agents into real teammates — assign tasks, track progress, compound skills.

**Language:** TypeScript  |  **Stars:** 16,680  |  **Forks:** 2,072  |  **Score:** 4,339  |  **Created:** 2026-01-13

**Background:** Multica is an open-source managed agents platform that frames AI agents as team members rather than tools. Now past 16,000 stars with a "your next 10 hires won't be human" positioning, it provides issue assignment, progress tracking, and skill compounding that lets agents behave like colleagues on a project board.

**Problem it solves:** Current AI agent usage is session-based and ephemeral — developers interact with agents one task at a time with no continuity between sessions. There is no way to assign tasks, track completion, or build on previous work the way one would with a human teammate.

**Why another one?** Multica's managed platform approach — assigning tasks, tracking progress, compounding reusable skills over time — provides the organizational layer that individual agent tools lack. The self-hosted option gives teams full control over their agent infrastructure, and the open-source model allows customization for specific team workflows.

---

## 18. [mempalace](https://github.com/MemPalace/mempalace)
> The best-benchmarked open-source AI memory system. And it's free.

**Language:** Python  |  **Stars:** 47,614  |  **Forks:** 6,217  |  **Score:** 3,996  |  **Created:** 2026-04-05

**Background:** MemPalace is a local-first AI memory system that stores conversations verbatim rather than summarizing them, indexing content into *wings* (people/projects), *rooms* (topics), and *drawers* (original content). Created just nine days ago, it has already surpassed 47,000 stars on the back of a reported 96.6% R@5 result on LongMemEval — the highest benchmark score for an open system.

**Problem it solves:** Every conversation with an AI — decisions, debugging sessions, architecture debates — disappears when the session ends. Other memory systems try to fix this by letting AI decide what to remember, but they extract shallow summaries and discard the reasoning behind decisions, leaving the recovered context thin and unreliable.

**Why another one?** MemPalace stores everything rather than selectively extracting summaries, preserving the full context of why decisions were made. The scoped retrieval structure (wings/rooms/drawers) avoids flat-corpus search failures, the backend is pluggable (ChromaDB by default), and nothing leaves the user's machine unless they opt in — a privacy posture that cloud-based memory systems cannot match.

---

## 19. [CorridorKey](https://github.com/nikopueringer/CorridorKey)
> Perfect Green Screen Keys

**Language:** Python  |  **Stars:** 11,139  |  **Forks:** 671  |  **Score:** 3,966  |  **Created:** 2026-02-25

**Background:** CorridorKey by Niko Pueringer (of Corridor Crew) is a neural network that unmixes green screen footage — separating the true foreground color from the green contamination in semi-transparent edge pixels. At over 11,000 stars since its February launch, it targets the VFX community that has long struggled with the limitations of traditional keyers.

**Problem it solves:** Green screen compositing produces pixels along subject edges that are a mix of foreground and background color. Traditional keyers force artists to choose between harsh binary mattes or spend hours building garbage mattes and rotoscoping to recover semi-transparent pixels like motion blur and out-of-focus edges.

**Why another one?** CorridorKey attacks the unmixing problem directly — it predicts the unmultiplied foreground color alongside a linear alpha channel rather than just a binary mask. This preserves delicate edge detail that "AI Roto" tools destroy, and the single-hint workflow replaces hours of manual matte construction with one interactive step.

---

## 20. [agent-skills](https://github.com/addyosmani/agent-skills)
> Production-grade engineering skills for AI coding agents.

**Language:** Shell  |  **Stars:** 17,291  |  **Forks:** 2,185  |  **Score:** 3,952  |  **Created:** 2026-02-15

**Background:** Agent Skills by Addy Osmani provides production-grade engineering skills for AI coding agents, packaging senior engineer workflows and quality gates into seven slash commands mapped to the development lifecycle. Now at over 17,000 stars, it continues to grow as the AI skills ecosystem matures.

**Problem it solves:** AI coding agents jump straight into writing code without following disciplined processes — specifying requirements, planning incrementally, testing thoroughly, and reviewing before shipping. This leads to code that works in isolation but fails in production.

**Why another one?** The skills activate automatically based on context — designing an API triggers the api-and-interface-design skill, building UI triggers frontend-ui-engineering. The structured DEFINE-PLAN-BUILD-VERIFY-REVIEW-SHIP pipeline ensures no development phase is skipped, and marketplace integration makes installation a single command.

---

## 21. [agentmemory](https://github.com/rohitg00/agentmemory)
> #1 Persistent memory for AI coding agents based on real-world benchmarks

**Language:** TypeScript  |  **Stars:** 1,829  |  **Forks:** 182  |  **Score:** 3,776  |  **Created:** 2026-02-25

**Background:** Agentmemory is a persistent memory layer for AI coding agents that extends Karpathy's LLM Wiki pattern with confidence scoring, lifecycle management, knowledge graphs, and hybrid search. It works across Claude Code, Cursor, Gemini CLI, OpenCode, and any MCP client, with the underlying design document having gone viral (825 stars on the gist alone).

**Problem it solves:** Coding agents re-explain the same project decisions every session because they have no persistent memory. Existing memory tools lock users into a single agent or fail to weight information by confidence and recency, leaving the agent to pick unreliable or outdated facts during retrieval.

**Why another one?** Agentmemory's confidence scoring and lifecycle — memories have freshness, verification status, and decay — distinguish it from flat key-value stores, and the MCP-client-agnostic design means the same memory follows the developer across every agent they use. The knowledge graph and hybrid search layer provide retrieval that flat embedding stores cannot match.

---

## 22. [skills](https://github.com/anthropics/skills)
> Public repository for Agent Skills

**Language:** Python  |  **Stars:** 120,404  |  **Forks:** 13,955  |  **Score:** 3,712  |  **Created:** 2025-09-22

**Background:** Skills by Anthropic is the official public repository for Agent Skills, now past 120,000 stars. It serves as the canonical source of first-party skills and the reference implementation for the skill format that third-party ecosystems (Superpowers, Agent Skills by Addy Osmani, Caveman) build upon.

**Problem it solves:** Without a standard format, AI agent capabilities fragment across tools — Cursor rules, Claude Code skills, Gemini extensions — none portable. Teams that invest in crafting agent behavior risk lock-in to a single tool, and newcomers struggle to discover which capabilities exist.

**Why another one?** As Anthropic's official repository, this is the reference point that defines the skill format and ships the first-party skills other tools extend. The scale (120K stars, 14K forks) reflects its role as the central hub of the broader skills ecosystem, with community contributions flowing through a single canonical source.

---

## 23. [ralph](https://github.com/snarktank/ralph)
> Ralph is an autonomous AI agent loop that runs repeatedly until all PRD items are complete.

**Language:** TypeScript  |  **Stars:** 17,120  |  **Forks:** 1,704  |  **Score:** 3,304  |  **Created:** 2026-01-07

**Background:** Ralph by Ryan Carson is an autonomous AI agent loop that runs coding tools (Amp or Claude Code) repeatedly until all PRD items are complete, with each iteration running in a fresh context. Based on Geoffrey Huntley's Ralph pattern, the project has reached over 17,000 stars as developers adopt run-to-completion automation for multi-step projects.

**Problem it solves:** Long coding projects overflow agent context windows, degrading output quality as the conversation grows. Developers either babysit agents turn-by-turn or watch them lose track of earlier decisions, defeating the point of automation for substantial work.

**Why another one?** Ralph's fresh-context-per-iteration model solves the context window problem by encoding progress in external state — git history, progress.txt, and prd.json — rather than the conversation itself. The loop continues until PRD items are done, making it genuinely autonomous rather than interactive, and the prompt templates support both Amp and Claude Code out of the box.

---

## 24. [Apollo-11](https://github.com/chrislgarry/Apollo-11)
> Original Apollo 11 Guidance Computer (AGC) source code for the command and lunar modules.

**Language:** Assembly  |  **Stars:** 67,331  |  **Forks:** 7,652  |  **Score:** 3,296  |  **Created:** 2014-04-03

**Background:** Apollo-11 preserves the original Apollo 11 Guidance Computer source code for the command and lunar modules, transcribed from NASA's historical documentation. At over 67,000 stars and a decade old, it has become a canonical historical code repository — cited in computing history courses and regularly rediscovered by new generations of developers.

**Problem it solves:** The AGC source code is one of the foundational artifacts of software engineering, but it existed only as scanned printouts from NASA archives — hard to read, impossible to diff, and at risk of being lost. Without a machine-readable version, the code could not be studied, simulated, or learned from.

**Why another one?** By transcribing the printouts into plain text under version control, this project makes one of computing's most iconic codebases accessible to anyone with a browser. The assembly source is paired with module organization from the original listings, preserving historical structure while making the code navigable in modern tools.

---

## 25. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**Language:** Shell  |  **Stars:** 115,798  |  **Forks:** 19,303  |  **Score:** 2,825  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official terminal-native agentic coding tool, now past 115,000 stars and over 19,000 forks. It executes routine tasks, explains complex code, and handles git workflows through natural language, and has become the reference agent harness that third-party skills, memory systems, and workflows target.

**Problem it solves:** Developers want agentic coding without leaving the terminal — IDE-integrated agents force context switches, and web-based agents isolate the model from the local filesystem and shell. A terminal-native agent keeps the developer's existing tools and workflows intact while adding AI capabilities.

**Why another one?** As Anthropic's first-party tool, Claude Code has direct access to the latest model capabilities and the skill ecosystem standard. The terminal-native design integrates cleanly with git, shell scripts, and existing editor workflows, and the active release cadence keeps it aligned with the newest Claude models the moment they ship.

---

> **Day's theme:** Memory and context engineering dominate today's rankings — Andrej Karpathy Skills tops the board at #1 with 67K score, followed by a cluster of context tools (Claude-Mem at #5, MemPalace at #18, Agentmemory at #21) that attack the same problem from different angles: plugin capture, verbatim storage, and confidence-weighted graphs. The skills ecosystem continues to consolidate around Anthropic's official Skills repo (#22, 120K stars) while third-party frameworks (Superpowers, Agent Skills, Caveman) extend it with opinionated workflows. Outside the AI-coding core, two domain projects stand out: CorridorKey (#19) bringing neural unmixing to VFX, and AERIS-10 PLFM_RADAR (#13) democratizing phased array radar hardware — reminders that trending repos are not only about LLM tooling but also about open-sourcing expertise that used to be gatekept by industry.
