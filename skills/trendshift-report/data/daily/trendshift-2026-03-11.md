# Trendshift Report — 2026-03-11
**Total:** 25 repositories

---

## 1. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 46,473  |  **Forks:** 6,940  |  **Score:** 45,903  |  **Created:** 2025-10-13

**Background:** Agency Agents by Mark Sitarzewski continues to dominate the top spot with a massive score of 45,903 and has now crossed 46,000 stars. Born from a Reddit thread, the repository provides a growing collection of meticulously crafted AI agent personas covering professional roles like frontend development, community management, and content strategy.

**Problem it solves:** Building effective AI agent personas requires deep prompt engineering for each professional domain. Agency Agents delivers production-ready agent definitions with defined personality traits, communication styles, technical deliverables, and success metrics, removing the guesswork from role-specific AI deployment.

**Why another one?** Unlike generic prompt template libraries, each agent here has a distinct personality and voice with battle-tested workflows. The personality-driven approach makes agents entertaining to browse and share, which explains the viral trajectory from 18,000 stars just yesterday to 46,000 today.

---

## 2. [autoresearch](https://github.com/karpathy/autoresearch)
> AI agents running research on single-GPU nanochat training automatically

**Language:** Python  |  **Stars:** 38,849  |  **Forks:** 5,377  |  **Score:** 15,062  |  **Created:** 2026-03-06

**Background:** Karpathy's autonomous ML research experiment holds steady in second place. The project gives an AI agent a real LLM training setup built on nanochat and lets it experiment autonomously overnight — modifying code, training for 5 minutes, evaluating results, and iterating. The human programs research direction via Markdown files rather than touching Python code directly.

**Problem it solves:** The tedious hypothesis-code-train-evaluate cycle that dominates a researcher's day. Autoresearch automates this loop continuously, letting researchers wake up to a log of completed experiments and hopefully improved models.

**Why another one?** The deliberate architecture of three files (fixed data prep, modifiable training logic, and a Markdown research program) makes the barrier to entry remarkably low. Karpathy's sci-fi framing — AI agents eventually running all research on "compute cluster megastructures in the skies" — has captured imaginations well beyond the ML community.

---

## 3. [MiroFish](https://github.com/666ghj/MiroFish)
> A Simple and Universal Swarm Intelligence Engine, Predicting Anything

**Language:** Python  |  **Stars:** 26,759  |  **Forks:** 3,202  |  **Score:** 12,305  |  **Created:** 2025-11-26

**Background:** MiroFish by Shanda Group is a next-generation AI prediction engine based on multi-agent swarm intelligence. It constructs high-fidelity parallel digital worlds from seed information such as breaking news, policy drafts, and financial signals, then runs thousands of independently-personality agents through social simulation to predict future outcomes.

**Problem it solves:** Traditional prediction systems rely on monolithic models that are expensive to retrain and brittle to distribution shifts. MiroFish distributes prediction across a swarm of intelligent agents with individual personalities, long-term memory, and behavioral logic, enabling more robust forecasting through collective intelligence.

**Why another one?** The swarm intelligence approach offers a genuinely different architectural paradigm from the transformer-dominant prediction landscape. Users simply upload seed materials and describe their prediction needs in natural language, then observe outcomes from a "god's eye view" — making sophisticated simulation accessible without deep technical expertise.

---

## 4. [context-hub](https://github.com/andrewyng/context-hub)
> Curated, versioned docs for coding agents — with a learning loop

**Language:** JavaScript  |  **Stars:** 6,321  |  **Forks:** 597  |  **Score:** 10,088  |  **Created:** 2025-10-30

**Background:** Context Hub, associated with Andrew Ng's AI Suite ecosystem, provides curated and versioned API documentation that coding agents can fetch on demand. All content is maintained as open Markdown in the repository, so users can inspect exactly what their agent reads and contribute improvements back.

**Problem it solves:** Coding agents hallucinate APIs and forget what they learn between sessions. Context Hub gives them a searchable, versioned knowledge base via a simple CLI (`chub search`, `chub get`), with annotation and feedback mechanisms so documentation improves over time.

**Why another one?** Unlike static documentation sites, Context Hub is designed for agent consumption with a built-in learning loop. Agents can annotate gaps they discover locally, and community feedback flows back to authors. The integration with Claude Code skills makes it seamlessly available during development sessions.

---

## 5. [openclaw](https://github.com/openclaw/openclaw)
> Your own personal AI assistant. Any OS. Any Platform. The lobster way.

**Language:** TypeScript  |  **Stars:** 314,992  |  **Forks:** 60,226  |  **Score:** 8,061  |  **Created:** 2025-11-24

**Background:** OpenClaw is a personal AI assistant you run on your own devices, with support for over 20 messaging platforms including WhatsApp, Telegram, Slack, Discord, Signal, and iMessage. With nearly 315,000 stars, it is one of the most popular open-source projects on GitHub, functioning as platform infrastructure for a vast skills ecosystem.

**Problem it solves:** Users want a single, self-hosted AI assistant that integrates with every communication channel they already use, with voice support on macOS/iOS/Android and a live Canvas for visual interaction — all without sending data to third-party services.

**Why another one?** OpenClaw's extensible skills architecture has spawned thousands of community-built capabilities. Multiple ecosystem projects trending simultaneously (awesome-openclaw-skills, awesome-openclaw-usecases, OpenClaw-RL, Edict) each drive traffic back to the main repository, creating a self-reinforcing growth cycle.

---

## 6. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 85,570  |  **Forks:** 6,721  |  **Score:** 6,880  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent is a complete software development workflow for coding agents, built on composable skills. It transforms how coding agents operate: instead of jumping straight into writing code, the agent first teases out a spec, presents it in digestible chunks, then creates an implementation plan emphasizing TDD, YAGNI, and DRY principles.

**Problem it solves:** Coding agents left to their own devices produce unfocused, poorly structured code. Superpowers imposes a disciplined workflow — spec, plan, subagent-driven development with inspection and review — enabling Claude to work autonomously for hours without deviating from the agreed plan.

**Why another one?** Available through the official Claude plugin marketplace and supporting multiple platforms (Claude Code, Cursor, Codex, OpenCode), Superpowers stands out by focusing on methodology rather than just capability. The subagent-driven development process with built-in review gates is a more structured approach than most competing frameworks.

---

## 7. [page-agent](https://github.com/alibaba/page-agent)
> JavaScript in-page GUI agent. Control web interfaces with natural language.

**Language:** TypeScript  |  **Stars:** 8,803  |  **Forks:** 694  |  **Score:** 6,118  |  **Created:** 2025-09-23

**Background:** Page Agent by Alibaba is a GUI agent that lives directly inside web pages, enabling natural language control of web interfaces. Unlike browser-extension-based or headless-browser approaches, it operates entirely as in-page JavaScript, requiring no special permissions or multimodal LLMs.

**Problem it solves:** Automating web UI interactions typically requires browser extensions, Python scripts, or headless browsers with complex setup. Page Agent provides a lightweight, text-based DOM manipulation approach that works with any LLM — no screenshots or special vision models needed.

**Why another one?** The in-page JavaScript approach is a key differentiator: no browser extension, no Python dependency, no headless browser. It includes a human-in-the-loop UI, supports bring-your-own LLMs, and offers an optional Chrome extension for multi-tab scenarios, making it the most accessible entry point for GUI automation.

---

## 8. [promptfoo](https://github.com/promptfoo/promptfoo)
> Test your prompts, agents, and RAGs. Red teaming and vulnerability scanning for AI.

**Language:** TypeScript  |  **Stars:** 16,834  |  **Forks:** 1,458  |  **Score:** 6,090  |  **Created:** 2023-04-28

**Background:** Promptfoo is a well-established CLI and library for evaluating and red-teaming LLM applications. Founded in 2023, it has matured into one of the go-to tools for systematic prompt testing, with support for comparing performance across GPT, Claude, Gemini, Llama, and more using declarative YAML configs.

**Problem it solves:** The trial-and-error approach to prompt engineering wastes time and ships unreliable AI applications. Promptfoo provides systematic evaluation with side-by-side model comparisons, red teaming for security vulnerabilities, and CI/CD integration to catch regressions before deployment.

**Why another one?** As agent-based applications become more complex with multi-step workflows and tool use, the need for systematic evaluation has grown beyond simple prompt testing. Promptfoo's support for testing agents, RAG pipelines, and red-team security scanning positions it at the center of the emerging AI quality assurance category.

---

## 9. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry.

**Language:** N/A  |  **Stars:** 37,866  |  **Forks:** 3,638  |  **Score:** 5,669  |  **Created:** 2026-01-25

**Background:** Maintained by VoltAgent, this curated directory catalogs over 5,400 community-built OpenClaw skills sourced from ClawHub, OpenClaw's public skills registry. Skills are organized by category for easier discovery, with installation possible via ClawHub CLI or manual folder copying.

**Problem it solves:** With thousands of skills available in the OpenClaw ecosystem, discovery is a major bottleneck. This repository filters, categorizes, and presents the full registry in a browsable format so users can find the right skill without searching through an overwhelming catalog.

**Why another one?** At 37,866 stars, this has become the de facto discovery layer for the OpenClaw ecosystem. It serves both as a practical installation guide and as inspiration for new use cases, complementing the official registry with community curation and categorization.

---

## 10. [claude-skills](https://github.com/alirezarezvani/claude-skills)
> +192 Claude Code skills & agent plugins for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents.

**Language:** Python  |  **Stars:** 5,253  |  **Forks:** 604  |  **Score:** 5,432  |  **Created:** 2025-10-19

**Background:** This open-source library by Alireza Rezvani provides 192 production-ready skills and 17 agent plugins covering engineering, DevOps, marketing, compliance, and C-level advisory. Each skill includes a SKILL.md instruction file, Python CLI tools (all stdlib-only, zero pip installs), and reference documentation.

**Problem it solves:** AI coding agents lack domain expertise out of the box. This library provides modular instruction packages that give agents specialized knowledge across 11 different platforms, from Claude Code to Cursor to Gemini CLI, without requiring any external dependencies.

**Why another one?** The cross-platform compatibility across 11 coding agents is the standout feature. While most skill libraries target a single tool, this one provides a unified set of skills that work natively across Claude Code, OpenAI Codex, Gemini CLI, Cursor, Aider, Windsurf, and more, making it portable across team tooling preferences.

---

## 11. [hermes-agent](https://github.com/NousResearch/hermes-agent)
> The agent that grows with you

**Language:** Python  |  **Stars:** 7,969  |  **Forks:** 928  |  **Score:** 4,584  |  **Created:** 2025-07-22

**Background:** Hermes Agent by Nous Research is a self-improving AI agent with a built-in learning loop. It creates skills from experience, improves them during use, persists knowledge across sessions, and builds a deepening model of who you are over time. It can run on a $5 VPS, a GPU cluster, or serverless infrastructure.

**Problem it solves:** Most AI agents start from zero every session, losing context and learned preferences. Hermes Agent maintains persistent memory, searches past conversations, and builds user-specific models, creating an assistant that genuinely improves with continued use.

**Why another one?** The self-improving loop is the key differentiator: skills created from experience, automatic knowledge persistence, and cross-session user modeling. Combined with multi-platform presence (Telegram, Discord, Slack, WhatsApp, Signal, CLI) and support for 200+ models via OpenRouter, it offers a uniquely personal agent that is not tied to any single provider.

---

## 12. [BettaFish](https://github.com/666ghj/BettaFish)
> Multi-Agent public opinion analysis assistant — breaking information cocoons, restoring the full picture, predicting trends, and assisting decisions.

**Language:** Python  |  **Stars:** 38,857  |  **Forks:** 7,260  |  **Score:** 4,473  |  **Created:** 2024-07-01

**Background:** BettaFish is a multi-agent public opinion and sentiment analysis assistant built from scratch without any framework dependencies. Created by the same team behind MiroFish, it analyzes social media and news sources to break through information filter bubbles, restore the full picture of public discourse, and predict future sentiment trends.

**Problem it solves:** Information cocoons created by algorithmic feeds give users a distorted view of public opinion. BettaFish deploys multiple agents to gather and cross-reference sources, producing a comprehensive sentiment analysis that reveals the full landscape rather than a filtered slice.

**Why another one?** The zero-dependency, built-from-scratch approach gives users full transparency into how analysis is performed. Its connection to MiroFish creates a two-product ecosystem — BettaFish for understanding current sentiment, MiroFish for predicting future outcomes — that addresses the full opinion intelligence lifecycle.

---

## 13. [nanochat](https://github.com/karpathy/nanochat)
> The best ChatGPT that $100 can buy.

**Language:** Python  |  **Stars:** 48,769  |  **Forks:** 6,379  |  **Score:** 4,372  |  **Created:** 2025-10-13

**Background:** Karpathy's nanochat is a minimal experimental harness for training LLMs on a single GPU node, covering tokenization, pretraining, finetuning, evaluation, inference, and a chat UI. It famously allows training a GPT-2 capability LLM — which cost $43,000 in 2019 — for approximately $48 on an 8xH100 node in about two hours.

**Problem it solves:** LLM training frameworks are typically complex, multi-dependency systems designed for large teams. Nanochat provides a minimal, hackable codebase where a single "depth" parameter controls model complexity and all other hyperparameters are calculated automatically.

**Why another one?** Nanochat's continued trending alongside autoresearch is not coincidental — autoresearch uses nanochat as its training substrate. The GPT-2-for-$48 narrative and the active speedrun leaderboard create ongoing community engagement that keeps the project visible well beyond its initial launch.

---

## 14. [app-store-screenshots](https://github.com/ParthJadhav/app-store-screenshots)
> End to end app store screenshot creation using AI

**Language:** N/A  |  **Stars:** 2,837  |  **Forks:** 188  |  **Score:** 3,997  |  **Created:** 2026-03-07

**Background:** App Store Screenshots by Parth Jadhav is a skill for AI coding agents that generates production-ready App Store screenshots for iOS apps. It scaffolds a Next.js project, designs advertisement-style screenshots with compelling copy, renders them at full resolution with iPhone mockups, and exports PNGs at all four Apple-required device sizes.

**Problem it solves:** Creating App Store screenshots is tedious design work requiring precise dimensions, compelling copy, and device mockups for multiple screen sizes. This tool automates the entire pipeline from brand input to exported PNGs, with the results already proven by Apple's approval process.

**Why another one?** Rather than generating simple UI captures, it designs each screenshot as an advertisement with proven copywriting patterns. Support for locale-based sets, RTL-aware layouts, reusable theme presets, and bulk export across locale/device/theme combinations makes it production-grade rather than a toy demo.

---

## 15. [deer-flow](https://github.com/bytedance/deer-flow)
> An open-source SuperAgent harness that researches, codes, and creates.

**Language:** Python  |  **Stars:** 30,832  |  **Forks:** 3,713  |  **Score:** 3,671  |  **Created:** 2025-05-07

**Background:** DeerFlow 2.0 by ByteDance is a ground-up rewrite of the original deep research framework, now functioning as an open-source super agent harness orchestrating sub-agents, memory, sandboxes, and extensible skills. It claimed the number one spot on GitHub Trending in late February following its v2 launch.

**Problem it solves:** Complex tasks requiring research, coding, and content creation often span minutes to hours and need coordination across multiple specialized capabilities. DeerFlow orchestrates sub-agents with sandboxed execution environments and persistent memory to handle these multi-step workflows autonomously.

**Why another one?** The 2.0 rewrite shares no code with v1, signaling a fundamentally different architecture. Its backing by ByteDance and official recommendation of specific models (Doubao-Seed-2.0-Code, DeepSeek v3.2, Kimi 2.5) give it a curated, production-oriented feel compared to more generic agent frameworks.

---

## 16. [paperclip](https://github.com/paperclipai/paperclip)
> Open-source orchestration for zero-human companies

**Language:** TypeScript  |  **Stars:** 26,233  |  **Forks:** 3,483  |  **Score:** 3,279  |  **Created:** 2026-03-02

**Background:** Paperclip is a Node.js server and React UI that orchestrates a team of AI agents to run a business. It positions itself as the company layer above individual agents: "If OpenClaw is an employee, Paperclip is the company." Users define goals, hire agent teams (CEO, CTO, engineers, designers, marketers), and track work and costs from a single dashboard.

**Problem it solves:** Individual AI agents can execute tasks, but coordinating them into a coherent business operation requires org charts, budgets, governance, goal alignment, and cost tracking. Paperclip provides this orchestration layer so users manage business goals rather than pull requests.

**Why another one?** The "zero-human company" framing is provocative but the implementation is practical — it looks like a task manager but includes org charts, budgets, governance policies, and agent coordination under the hood. The business-goal orientation (e.g., "Build the #1 AI note-taking app to $1M MRR") differentiates it from code-centric agent frameworks.

---

## 17. [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)
> GEO-first SEO skill for Claude Code. Comprehensive AI search optimization for any website.

**Language:** Python  |  **Stars:** 2,525  |  **Forks:** 413  |  **Score:** 3,069  |  **Created:** 2026-02-18

**Background:** GEO-SEO Claude is a Claude Code skill focused on Generative Engine Optimization — optimizing websites for AI-powered search engines like ChatGPT, Claude, Perplexity, and Gemini rather than traditional Google search. It provides citability scoring, AI crawler analysis, brand authority measurement, schema markup generation, and PDF reports.

**Problem it solves:** AI search is growing at 527% year-over-year, yet only 23% of marketers are investing in GEO. This skill brings AI search optimization directly into the developer workflow with commands like `/geo audit` and `/geo citability`, addressing the gap between where traffic is going and where optimization efforts are focused.

**Why another one?** The GEO-first approach inverts the traditional SEO mindset. While SEO tools optimize for Google's crawlers, this tool optimizes for AI citation readiness — how likely AI systems are to reference and quote your content. The integration as a Claude Code skill means optimization happens alongside development rather than as a separate workflow.

---

## 18. [awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
> A community collection of OpenClaw use cases for making life easier.

**Language:** N/A  |  **Stars:** 25,079  |  **Forks:** 2,066  |  **Score:** 2,890  |  **Created:** 2026-02-08

**Background:** Maintained by Hesam Sheikh, this repository documents real-life use cases showing how people actually use OpenClaw in their daily lives, from social media digest automation to personal productivity workflows. It addresses the adoption bottleneck of knowing what is possible rather than how to install a skill.

**Problem it solves:** The biggest barrier to OpenClaw adoption is not the skills catalog but imagination — users do not know what workflows are possible. This collection bridges that gap with concrete, community-contributed examples covering social media, productivity, and personal automation.

**Why another one?** While awesome-openclaw-skills catalogs the technical components, this repository focuses on the human use cases. The security warning about unaudited third-party skills shows a mature, honest approach to community curation that builds trust in the ecosystem.

---

## 19. [humanizer](https://github.com/blader/humanizer)
> Claude Code skill that removes signs of AI-generated writing from text

**Language:** N/A  |  **Stars:** 9,565  |  **Forks:** 766  |  **Score:** 2,874  |  **Created:** 2026-01-18

**Background:** Humanizer is a Claude Code skill that detects and removes 24 specific patterns of AI-generated writing identified by Wikipedia's AI Cleanup WikiProject. It performs a multi-pass rewrite: first applying pattern-specific fixes, then an "obviously AI generated" audit pass, followed by a second rewrite to catch lingering AI-isms.

**Problem it solves:** AI-generated text follows statistically predictable patterns — significance inflation, promotional language, em-dash overuse, hedge-word stacking — that are increasingly detectable by readers and automated tools. Humanizer systematically addresses each of these patterns to produce more natural-sounding output.

**Why another one?** Grounded in Wikipedia's empirically-derived catalog of AI writing signatures (based on thousands of observed instances), Humanizer takes a pattern-by-pattern approach rather than a vague "make it sound human" prompt. The two-pass architecture — fix then audit — catches patterns that a single rewrite typically misses.

---

## 20. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster.

**Language:** Shell  |  **Stars:** 78,229  |  **Forks:** 6,409  |  **Score:** 2,746  |  **Created:** 2025-02-22

**Background:** Anthropic's official Claude Code is an agentic coding tool that lives in the terminal, understanding codebases and executing tasks through natural language commands. Now installable via curl, Homebrew, or WinGet (npm is deprecated), it supports a plugins system and can be tagged directly on GitHub for code review.

**Problem it solves:** Developers need to context-switch between reading code, writing code, and managing git workflows. Claude Code handles routine tasks, explains complex code, and manages git operations from within the terminal, keeping developers in their flow state.

**Why another one?** As the official Anthropic product, Claude Code benefits from first-party model integration and a growing plugins ecosystem. Its continued presence in the trending list alongside numerous Claude Code skills (humanizer, geo-seo-claude, claude-skills, app-store-screenshots) demonstrates its role as a platform for the emerging skills economy.

---

## 21. [Win11Debloat](https://github.com/Raphire/Win11Debloat)
> A simple, lightweight PowerShell script to remove pre-installed apps, disable telemetry, and customize Windows.

**Language:** PowerShell  |  **Stars:** 41,886  |  **Forks:** 1,647  |  **Score:** 2,685  |  **Created:** 2020-10-27

**Background:** Win11Debloat by Raphire is a long-running PowerShell script for decluttering Windows 10 and 11 installations. Originally created in 2020, it has steadily grown to over 41,000 stars, serving as one of the most popular Windows customization tools on GitHub.

**Problem it solves:** Fresh Windows installations come with pre-installed bloatware, telemetry services, and intrusive UI elements that degrade performance and privacy. Win11Debloat automates removal of these components with a single script rather than requiring users to navigate dozens of settings panels.

**Why another one?** Its longevity and 41,000+ stars reflect continued relevance as each Windows update re-introduces bloatware. The script's CLI support, Windows Audit mode compatibility, and multi-user capabilities make it useful for both individual users and system administrators deploying across fleets.

---

## 22. [dify](https://github.com/langgenius/dify)
> Production-ready platform for agentic workflow development.

**Language:** TypeScript  |  **Stars:** 133,119  |  **Forks:** 20,734  |  **Score:** 2,658  |  **Created:** 2023-04-12

**Background:** Dify by LangGenius is a production-ready platform for building agentic AI workflows, offering both a cloud service and self-hosted deployment. With over 133,000 stars, it is one of the most popular AI development platforms, providing visual workflow builders, model management, and deployment tooling.

**Problem it solves:** Going from AI prototype to production requires handling model orchestration, workflow design, deployment, and monitoring. Dify provides an integrated platform covering the full lifecycle so teams can ship agentic workflows without cobbling together separate tools.

**Why another one?** At 133,000 stars and with a mature cloud offering, Dify has achieved critical mass as the default agentic workflow platform. Its continued trending alongside newer agent frameworks suggests developers are looking for proven, production-grade infrastructure rather than experimental tools.

---

## 23. [openrag](https://github.com/langflow-ai/openrag)
> OpenRAG is a comprehensive, single package Retrieval-Augmented Generation platform built on Langflow, Docling, and OpenSearch.

**Language:** Python  |  **Stars:** 2,975  |  **Forks:** 269  |  **Score:** 2,470  |  **Created:** 2025-07-11

**Background:** OpenRAG by Langflow AI is a comprehensive RAG platform combining Langflow for workflow orchestration, Docling for document processing, and OpenSearch for semantic search. Built with FastAPI and Next.js, it provides document upload, processing, and AI-powered conversational search in a single deployable package.

**Problem it solves:** Setting up a production RAG pipeline typically requires integrating separate document processing, embedding, vector storage, and retrieval components. OpenRAG bundles these into a single package with intelligent agent-powered nudges via Langflow, reducing setup from days to minutes.

**Why another one?** The single-package approach — one install gets you document ingestion, semantic search, and chat interface — contrasts with the typical multi-service RAG architecture. The Langflow integration adds visual workflow editing for retrieval pipelines, making it accessible to non-developers who need document intelligence.

---

## 24. [OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL)
> OpenClaw-RL: Train any agent simply by talking

**Language:** TypeScript  |  **Stars:** 3,272  |  **Forks:** 313  |  **Score:** 2,372  |  **Created:** 2026-02-26

**Background:** OpenClaw-RL by Gen-Verse brings reinforcement learning to the OpenClaw ecosystem, enabling users to train personalized agents through natural language feedback rather than reward function engineering. It supports agentic RL in terminal, GUI, software engineering, and tool-call settings with fully async execution.

**Problem it solves:** Traditional RL requires designing reward functions and training infrastructure, which is inaccessible to most users. OpenClaw-RL lets users improve their agent's behavior simply by talking to it, providing language feedback that drives a hybrid RL training loop — zero API cost or zero GPU options available.

**Why another one?** The "train by talking" paradigm eliminates the reward engineering bottleneck that has kept RL out of reach for most agent users. Its integration with the OpenClaw ecosystem and support for real-world agentic settings (not just games or simulations) positions it as practical personalization infrastructure rather than a research toy.

---

## 25. [edict](https://github.com/cft0808/edict)
> Three Departments and Six Ministries - OpenClaw Multi-Agent Orchestration System with real-time dashboard and audit trails

**Language:** Python  |  **Stars:** 10,202  |  **Forks:** 933  |  **Score:** 2,326  |  **Created:** 2026-02-23

**Background:** Edict models AI multi-agent orchestration on the Tang Dynasty's Three Departments and Six Ministries governance structure. It deploys 12 specialized agents (11 business roles plus one compatibility role) organized into hierarchical phases: the Crown Prince sorts tasks, Zhongshu department plans, Menxia department reviews and vetoes, and Shangshu department dispatches to six parallel execution ministries.

**Problem it solves:** Multi-agent frameworks typically let agents act without institutional oversight, leading to unchecked errors cascading through workflows. Edict introduces mandatory review layers between planning and execution, ensuring no agent action proceeds without systematic approval and creating full audit trails.

**Why another one?** The ancient governance metaphor is not just branding — it maps to a real architectural pattern of separation between planning, review, and execution that mirrors how engineering organizations actually operate. The real-time dashboard, model configuration, and complete audit trails address the observability gap that production multi-agent deployments desperately need.

---

> **Day's theme:** The AI agent ecosystem matures beyond individual tools into full organizational infrastructure — from agent personality libraries and skill marketplaces to business orchestration platforms and RL-based personalization, with the OpenClaw platform at the center of a self-reinforcing growth cycle.
