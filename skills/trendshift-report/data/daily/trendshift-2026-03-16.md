# Trendshift Report — 2026-03-16
**Total:** 25 repositories

---

## 1. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 85,570  |  **Forks:** 6,721  |  **Score:** 12,796  |  **Created:** 2025-10-09

**Background:** Superpowers by Jesse Vincent (obra) is a complete software development workflow framework for coding agents. It provides composable "skills" and instructions that enforce a disciplined process: the agent first teases out a spec, presents it in digestible chunks, builds an implementation plan, then launches subagent-driven development with built-in review cycles.

**Problem it solves:** Coding agents left to their own devices tend to jump straight into writing code without understanding the full problem, producing poorly planned implementations. Superpowers enforces a structured workflow — spec, plan, implement, review — ensuring agents work methodically through TDD and YAGNI principles.

**Why another one?** While many agent frameworks focus on tool orchestration, Superpowers focuses on development methodology. Its subagent-driven development model allows Claude to work autonomously for hours at a time without drifting from the plan, a capability that distinguishes it from simpler prompt-based approaches.

---

## 2. [gstack](https://github.com/garrytan/gstack)
> Use Garry Tan's exact Claude Code setup: 10 opinionated tools that serve as CEO, Eng Manager, Release Manager, Doc Engineer, and QA

**Language:** TypeScript  |  **Stars:** 17,806  |  **Forks:** 1,980  |  **Score:** 9,060  |  **Created:** 2026-03-11

**Background:** Gstack by Garry Tan (Y Combinator CEO) packages twelve opinionated workflow skills for Claude Code as slash commands. Released just five days ago, it has already amassed nearly 18,000 stars. Each skill maps to a specific role — CEO plan review, eng manager architecture review, design review, one-command shipping, browser automation, and QA testing.

**Problem it solves:** A single Claude Code session treats every request the same way, with no role-specific depth. Gstack partitions workflows into specialist modes: `/plan-ceo-review` rethinks the product vision, `/plan-eng-review` locks in architecture and edge cases, and `/ship` handles the entire release process in one command.

**Why another one?** The celebrity factor of Garry Tan's personal setup drives adoption, but the substance is in the opinionated defaults. Rather than a framework that requires configuration, gstack provides a complete ready-to-use team of specialists, lowering the barrier from "build your own agent workflow" to "install and type a slash command."

---

## 3. [agency-agents](https://github.com/msitarzewski/agency-agents)
> A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**Language:** Shell  |  **Stars:** 46,473  |  **Forks:** 6,940  |  **Score:** 9,009  |  **Created:** 2025-10-13

**Background:** Agency Agents by Mark Sitarzewski provides a collection of pre-built AI agent personas for professional roles, each with defined personality traits, processes, and deliverable templates. The project has accumulated over 46,000 stars since its October 2025 launch, establishing itself as a staple in the agent ecosystem.

**Problem it solves:** Teams adopting AI agents for business tasks need role-specific system prompts and workflow definitions for every function — frontend development, community management, content strategy, and more. Agency Agents provides these ready-made, eliminating the prompt engineering overhead.

**Why another one?** The personality-driven approach sets it apart: agents have names, quirks, and strong opinions, making them entertaining to browse and share. This shareability has driven viral adoption well beyond the typical developer audience, and the breadth of covered roles (from "whimsy injectors" to "reality checkers") positions it as an agency-in-a-box rather than just a prompt library.

---

## 4. [system-design-academy](https://github.com/systemdesign42/system-design-academy)
> If you want to become good at system design, join this newsletter now

**Language:** N/A  |  **Stars:** 23,256  |  **Forks:** 2,876  |  **Score:** 7,356  |  **Created:** 2024-02-15

**Background:** System Design Academy is a curated collection of system design case studies organized by company, covering real-world engineering decisions at companies from A to Z. The repository serves as a companion to the System Design newsletter and has been a steady presence in trending lists for over two years.

**Problem it solves:** System design interview preparation and professional development typically require expensive courses or scattered blog posts. This repository aggregates real case studies from actual companies into a browsable, free reference organized alphabetically by company name.

**Why another one?** While interview-prep resources abound, System Design Academy focuses on real company case studies rather than abstract patterns. Its newsletter-companion model keeps content fresh and regularly updated, and the alphabetical company index makes it uniquely navigable for practitioners looking for precedents from specific organizations.

---

## 5. [deepagents](https://github.com/langchain-ai/deepagents)
> Agent harness built with LangChain and LangGraph. Equipped with a planning tool, a filesystem backend, and the ability to spawn subagents - well-equipped to handle complex agentic tasks.

**Language:** Python  |  **Stars:** 11,401  |  **Forks:** 1,818  |  **Score:** 6,074  |  **Created:** 2025-07-27

**Background:** Deep Agents is LangChain's official "batteries-included" agent harness, built on top of LangChain and LangGraph. It provides a planning tool, filesystem backend, and subagent spawning capabilities out of the box, positioning itself as LangChain's answer to the growing demand for production-grade agent frameworks.

**Problem it solves:** Building agents that can handle complex, multi-step tasks requires integrating planning, file I/O, and task decomposition from scratch. Deep Agents bundles these capabilities together so developers can focus on defining agent behavior rather than plumbing infrastructure.

**Why another one?** As an official LangChain project, Deep Agents benefits from tight integration with the LangChain and LangGraph ecosystem. The subagent spawning capability allows hierarchical task decomposition, and the filesystem backend provides persistent state — two features that generic agent frameworks often lack or require custom implementation.

---

## 6. [claude-mem](https://github.com/thedotmack/claude-mem)
> A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**Language:** TypeScript  |  **Stars:** 35,414  |  **Forks:** 2,524  |  **Score:** 5,976  |  **Created:** 2025-08-31

**Background:** Claude-Mem by thedotmack is a Claude Code plugin that serves as an automatic memory layer. It captures everything Claude does during coding sessions, compresses the information using AI, and injects relevant context back into future sessions. With over 35,000 stars, it has become one of the most popular Claude Code extensions.

**Problem it solves:** Claude Code sessions are stateless — each new conversation starts from scratch, losing valuable context about project decisions, patterns, and past work. Claude-Mem bridges this gap by automatically building and maintaining a persistent knowledge base that grows with each session.

**Why another one?** Unlike manual context-injection approaches (like maintaining a CLAUDE.md file by hand), Claude-Mem is fully automatic. It captures, compresses, and retrieves context without user intervention, and its use of Claude's own agent-sdk for compression ensures the summaries are optimized for Claude's own comprehension.

---

## 7. [Marketing-for-Founders](https://github.com/EdoStra/Marketing-for-Founders)
> Practical marketing resources to get the first 10 / 100 / 1000 users for your SaaS / App / Startup

**Language:** N/A  |  **Stars:** 4,761  |  **Forks:** 484  |  **Score:** 5,826  |  **Created:** 2025-05-19

**Background:** Marketing for Founders by EdoStra is a curated collection of practical marketing resources specifically targeted at technical founders taking their first steps with a startup. The repository focuses on actionable, low-budget tactics rather than the VC-funded scaling advice that dominates most marketing content.

**Problem it solves:** Most marketing advice online targets companies with established marketing budgets trying to scale to millions in revenue. Technical founders need a different playbook — one focused on getting the very first 10, 100, or 1,000 users with minimal spending and no marketing team.

**Why another one?** The explicit tiering by user milestone (10 / 100 / 1,000) makes this collection uniquely actionable. Instead of generic advice, founders can find tactics matched to their exact growth stage, and the focus on SaaS/app startups keeps the resources relevant rather than diluted across business types.

---

## 8. [OpenViking](https://github.com/volcengine/OpenViking)
> OpenViking is an open-source context database designed specifically for AI Agents. OpenViking unifies the management of context (memory, resources, and skills) that Agents need through a file system paradigm, enabling hierarchical context delivery and self-evolving.

**Language:** Python  |  **Stars:** 12,376  |  **Forks:** 847  |  **Score:** 4,906  |  **Created:** 2026-01-05

**Background:** OpenViking is an open-source context database from Volcengine (ByteDance's cloud arm) designed specifically for AI agents. It manages context — memory, resources, and skills — through a file system paradigm, allowing hierarchical context delivery and self-evolving agent capabilities.

**Problem it solves:** AI agents need to manage multiple types of context (conversation history, tool outputs, learned skills) but current solutions scatter this across vector databases, key-value stores, and ad-hoc files. OpenViking unifies all agent context under a single file-system-like abstraction with hierarchical delivery.

**Why another one?** The file system paradigm is the key differentiator. Rather than requiring agents to learn a new API for each context type, OpenViking uses familiar filesystem semantics — read, write, list, navigate — making it immediately intuitive. The self-evolving capability allows agents to improve their own context organization over time.

---

## 9. [MiroFish](https://github.com/666ghj/MiroFish)
> A Simple and Universal Swarm Intelligence Engine, Predicting Anything.

**Language:** Python  |  **Stars:** 26,759  |  **Forks:** 3,202  |  **Score:** 4,611  |  **Created:** 2025-11-26

**Background:** MiroFish by Shanda Group is a swarm intelligence prediction engine that applies bio-inspired collective intelligence algorithms — modeled on fish school behavior — to make predictions across financial markets, weather, and social trends. It has grown to nearly 27,000 stars since its November 2025 launch.

**Problem it solves:** Traditional prediction systems rely on monolithic models that are expensive to retrain and brittle to distribution shifts. MiroFish distributes prediction across a swarm of simple agents, each processing different signals, then aggregates their outputs for more robust and extensible predictions.

**Why another one?** The swarm intelligence approach offers a genuinely different architectural paradigm from the transformer-dominant landscape. By modeling collective behavior rather than individual model capacity, MiroFish provides a complementary prediction methodology that can be combined with conventional approaches for ensemble diversity.

---

## 10. [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> practice made claude perfect

**Language:** HTML  |  **Stars:** 17,254  |  **Forks:** 1,525  |  **Score:** 4,216  |  **Created:** 2025-10-31

**Background:** Claude Code Best Practice by shanraisshan is a community-maintained guide that documents proven patterns, tips, and implementation strategies for getting the most out of Claude Code. The repository is actively maintained and regularly updated with each Claude Code release.

**Problem it solves:** Claude Code is powerful but has a steep learning curve — users often discover effective patterns through trial and error over weeks. This repository consolidates community-learned best practices into a single reference, accelerating the onboarding process.

**Why another one?** Unlike official documentation that focuses on features, this repository captures the practitioner perspective — what actually works in daily use, common pitfalls, and workflow patterns that emerge from real-world usage. Its community-driven nature means it reflects diverse use cases rather than a single viewpoint.

---

## 11. [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
> GitNexus: The Zero-Server Code Intelligence Engine - a client-side knowledge graph creator that runs entirely in your browser.

**Language:** TypeScript  |  **Stars:** 14,368  |  **Forks:** 1,674  |  **Score:** 4,213  |  **Created:** 2025-08-02

**Background:** GitNexus by Abhigyan Patwari is a client-side code intelligence engine that creates interactive knowledge graphs entirely in the browser. Users drop in a GitHub repository URL or ZIP file and get a navigable knowledge graph with a built-in Graph RAG agent for code exploration. No server required.

**Problem it solves:** Understanding a new codebase requires significant time navigating files, tracing dependencies, and building a mental model. GitNexus automates this by generating a visual knowledge graph that maps relationships between code components, with an AI agent that can answer questions using the graph as context.

**Why another one?** The zero-server, browser-only architecture is the key differentiator. Unlike code intelligence tools that require backend infrastructure or IDE plugins, GitNexus runs entirely client-side, making it instantly accessible for exploring any public repository without installation or configuration.

---

## 12. [OpenAlice](https://github.com/TraderAlice/OpenAlice)
> File-driven AI trading agent engine for crypto and securities markets

**Language:** TypeScript  |  **Stars:** 1,680  |  **Forks:** 216  |  **Score:** 4,084  |  **Created:** 2026-02-18

**Background:** Open Alice is an AI trading agent that provides a personal research desk, quant team, trading floor, and risk management — all running on a laptop. It uses a file-driven architecture where Markdown defines personas and tasks, JSON defines config, and JSONL stores conversations. Both humans and AI control Alice by reading and modifying files.

**Problem it solves:** Algorithmic trading typically requires expensive infrastructure, proprietary platforms, and specialized engineering teams. OpenAlice democratizes this by providing a complete trading agent that runs locally, with every decision logged and every strategy defined in human-readable files.

**Why another one?** The file-driven design philosophy is distinctive: the same read/write primitives used in "vibe coding" transfer directly to "vibe trading." Every trading decision includes explicit reasoning, making the system transparent and auditable. No database or containers are needed — just files.

---

## 13. [project-nomad](https://github.com/Crosstalk-Solutions/project-nomad)
> Project N.O.M.A.D, is a self-contained, offline survival computer packed with critical tools, knowledge, and AI to keep you informed and empowered — anytime, anywhere.

**Language:** TypeScript  |  **Stars:** 1,455  |  **Forks:** 143  |  **Score:** 3,436  |  **Created:** 2025-06-24

**Background:** Project N.O.M.A.D. (Node for Offline Media, Archives, and Data) by Crosstalk Solutions is an offline-first knowledge and education server. It can be installed on any Debian-based system and provides tools, reference material, and AI capabilities accessible through a browser, designed to work without internet connectivity.

**Problem it solves:** In disaster scenarios, remote locations, or network-denied environments, access to critical knowledge and tools disappears. N.O.M.A.D. packages essential resources into a self-contained server that functions entirely offline, turning any compatible device into a portable knowledge hub.

**Why another one?** The offline-first design is the core differentiator. While most AI and knowledge tools assume persistent connectivity, N.O.M.A.D. is built from the ground up for disconnected operation. Its terminal-based installation and browser-based access make it deployable on minimal hardware without a desktop environment.

---

## 14. [cognee](https://github.com/topoteretes/cognee)
> Knowledge Engine for AI Agent Memory in 6 lines of code

**Language:** Python  |  **Stars:** 13,800  |  **Forks:** 1,382  |  **Score:** 3,324  |  **Created:** 2023-08-16

**Background:** Cognee by Topoteretes is a knowledge engine that builds AI memory through knowledge graphs. One of the older projects on today's list (created August 2023), it has matured into a well-documented platform with community plugins, add-ons, and integrations. Its tagline promises functional memory setup in just six lines of code.

**Problem it solves:** AI agents lack persistent, structured memory — they forget everything between sessions and cannot build upon prior knowledge. Cognee provides a knowledge graph-based memory system that allows agents to accumulate, organize, and retrieve knowledge over time.

**Why another one?** Cognee's longevity and 6-line setup promise distinguish it from newer memory solutions. While projects like Claude-Mem focus on session capture, Cognee builds a structured knowledge graph that enables semantic retrieval and relationship-based reasoning, offering deeper memory capabilities for agents that need to understand connections between concepts.

---

## 15. [Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)
> Official code repo for the O'Reilly Book - "Hands-On Large Language Models"

**Language:** Jupyter Notebook  |  **Stars:** 23,895  |  **Forks:** 5,530  |  **Score:** 2,882  |  **Created:** 2024-06-28

**Background:** This is the official code companion to the O'Reilly book "Hands-On Large Language Models" by Jay Alammar and Maarten Grootendorst. The repository contains Jupyter notebooks for all examples in the book, covering the full spectrum of LLM concepts from tokenization to fine-tuning.

**Problem it solves:** Reading about LLM concepts without runnable code leaves significant gaps in understanding. These notebooks provide tested, executable implementations of each concept discussed in the book, bridging the gap between theory and practice.

**Why another one?** As a companion to a published O'Reilly book by well-known authors (Jay Alammar of "The Illustrated Transformer" fame), this repository carries editorial quality assurance that community-driven tutorials lack. The notebooks are structured as a progressive curriculum rather than standalone examples.

---

## 16. [heretic](https://github.com/p-e-w/heretic)
> Fully automatic censorship removal for language models

**Language:** Python  |  **Stars:** 14,817  |  **Forks:** 1,505  |  **Score:** 2,878  |  **Created:** 2025-09-21

**Background:** Heretic by p-e-w removes safety alignment ("censorship") from transformer-based language models without expensive post-training. It combines an advanced implementation of directional ablation (abliteration) with a TPE-based parameter optimizer powered by Optuna, automating what previously required manual experimentation.

**Problem it solves:** Researchers and developers working with open-weight models often need uncensored outputs for legitimate use cases (creative writing, red-teaming, security research). Traditional approaches require costly fine-tuning or manual abliteration parameter tuning. Heretic fully automates the process.

**Why another one?** The fully automatic nature is the key differentiator. Previous abliteration tools required manual selection of refusal directions and thresholds. Heretic uses Optuna's optimization to find optimal parameters automatically, making the process accessible to users without deep mechanistic interpretability expertise.

---

## 17. [autoresearch](https://github.com/karpathy/autoresearch)
> AI agents running research on single-GPU nanochat training automatically

**Language:** Python  |  **Stars:** 38,849  |  **Forks:** 5,377  |  **Score:** 2,804  |  **Created:** 2026-03-06

**Background:** Autoresearch by Andrej Karpathy gives an AI agent a real LLM training setup (nanochat) and lets it experiment autonomously overnight. The agent modifies code, trains for 5 minutes, checks results, keeps or discards changes, and repeats. Users wake up to a log of experiments and potentially a better model. The project has accumulated nearly 39,000 stars in just ten days.

**Problem it solves:** The tedious cycle of hypothesis, code modification, experiment, and analysis that consumes a researcher's days. Autoresearch runs this loop continuously while the human is away, potentially accelerating the pace of empirical ML research by an order of magnitude.

**Why another one?** The key innovation is programming via `program.md` Markdown files rather than touching Python code directly. The agent operates on a research program specification, not a codebase, making it accessible to researchers who think in experimental methodology rather than software engineering. Karpathy's framing of AI agents eventually taking over all research adds a compelling narrative dimension.

---

## 18. [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)
> Open source repository of plugins primarily intended for knowledge workers to use in Claude Cowork

**Language:** Python  |  **Stars:** 9,203  |  **Forks:** 1,008  |  **Score:** 2,540  |  **Created:** 2026-01-23

**Background:** Knowledge Work Plugins is Anthropic's official open-source collection of plugins for Claude Cowork (and Claude Code). It includes 11 plugins covering productivity, sales, customer support, product management, and more, each bundling role-specific skills, connectors, and slash commands.

**Problem it solves:** Knowledge workers across different functions need Claude configured for their specific tools, terminology, and processes. These plugins provide pre-built integrations with services like Slack, Notion, HubSpot, Jira, and others, so teams can deploy Claude as a role-specific assistant without building custom integrations.

**Why another one?** As the official Anthropic offering, these plugins benefit from first-party integration quality and ongoing maintenance. The role-based design (sales, support, product management) maps to real organizational functions rather than abstract capabilities, making adoption straightforward for non-technical teams.

---

## 19. [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)
> Bash is all you need - A nano Claude Code-like agent, built from 0 to 1

**Language:** TypeScript  |  **Stars:** 27,884  |  **Forks:** 4,878  |  **Score:** 2,528  |  **Created:** 2025-06-29

**Background:** Learn Claude Code by shareAI-lab is an educational project that rebuilds a Claude Code-like agent from scratch, demonstrating that "the model IS the agent." The repository takes a philosophical stance: an agent is a neural network that has learned to act, not a framework or prompt chain. It traces this lineage from DeepMind DQN through OpenAI Five to modern coding agents.

**Problem it solves:** The proliferation of agent frameworks has obscured the fundamental insight that an agent is simply a capable model with tool access. Learn Claude Code strips away the abstraction layers to show how a minimal agent works, helping developers understand what is essential versus what is framework overhead.

**Why another one?** The "Bash is all you need" philosophy is deliberately provocative and educational. By building a functional agent with minimal dependencies, it demonstrates that most agent framework complexity is unnecessary — a powerful model with shell access can accomplish what elaborate orchestration layers promise.

---

## 20. [daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)
> LLM-driven A/H/US stock intelligent analyzer with multi-source data, real-time news, LLM decision dashboard, and multi-channel push notifications

**Language:** Python  |  **Stars:** 20,639  |  **Forks:** 21,366  |  **Score:** 2,482  |  **Created:** 2026-01-10

**Background:** Daily Stock Analysis by ZhuLinsen is an AI-powered stock analysis system covering A-shares, Hong Kong stocks, and US markets. It runs daily automated analysis combining technical indicators, fundamental data, and sentiment intelligence, then pushes "decision dashboards" to WeChat Work, Feishu, Telegram, Discord, and email.

**Problem it solves:** Individual investors lack the tools and time to perform comprehensive multi-dimensional analysis across global markets daily. This system automates the entire pipeline — data collection, technical analysis, fundamental context, and AI-generated conclusions with specific price targets and action checklists.

**Why another one?** The multi-market coverage (A-shares, Hong Kong, US) and multi-channel push delivery (WeChat Work, Feishu, Telegram, Discord, email) target the Chinese investor community specifically. The zero-cost, beginner-friendly design and GitHub Actions integration mean users can run it entirely for free on GitHub's infrastructure.

---

## 21. [claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
> Official, Anthropic-managed directory of high quality Claude Code Plugins.

**Language:** Python  |  **Stars:** 11,927  |  **Forks:** 1,153  |  **Score:** 2,417  |  **Created:** 2025-11-20

**Background:** Claude Plugins Official is Anthropic's curated marketplace of high-quality Claude Code plugins. It includes both internal plugins developed by Anthropic and vetted external plugins from partners and the community, installable directly via Claude Code's plugin system.

**Problem it solves:** The growing Claude Code plugin ecosystem needs a trusted central directory where users can find vetted, working plugins. This repository serves as that marketplace, with quality and security standards that external submissions must meet for inclusion.

**Why another one?** As the official Anthropic-managed directory, it provides a trust layer that community-driven lists cannot. The standard plugin structure (plugin.json, MCP configuration, commands, agents, skills) and the `/plugin install` integration make discovery and installation seamless.

---

## 22. [browser](https://github.com/lightpanda-io/browser)
> The headless browser built from scratch for AI agents and automation.

**Language:** Zig  |  **Stars:** 18,080  |  **Forks:** 672  |  **Score:** 2,380  |  **Created:** 2023-02-07

**Background:** Lightpanda Browser is a headless browser written from scratch in Zig, designed specifically for AI agents and automation. It is not a Chromium fork or WebKit patch — it is an entirely new browser engine built for headless usage, compatible with Playwright, Puppeteer, and chromedp through CDP.

**Problem it solves:** Chrome and Chromium-based headless browsers are resource-heavy — they were designed for human browsing and repurposed for automation. Lightpanda uses 9x less memory and runs 11x faster than Chrome for headless tasks, dramatically reducing the infrastructure cost of web automation at scale.

**Why another one?** The ground-up Zig implementation is the fundamental differentiator. By not inheriting Chromium's complexity, Lightpanda achieves an ultra-low memory footprint and exceptional speed that no fork-based approach can match. For AI agents that need to browse thousands of pages, the resource savings are transformative.

---

## 23. [dimos](https://github.com/dimensionalOS/dimos)
> The Agentive Operating System for Physical Space

**Language:** Python  |  **Stars:** 1,400  |  **Forks:** 217  |  **Score:** 2,333  |  **Created:** 2024-10-19

**Background:** DimOS by Dimensional is a pre-release operating system for generalist robotics. It provides an agent-driven framework for robots operating in physical spaces, with support for Nix, NixOS, CUDA, and Docker. The project includes an Agent CLI, MCP integration, and a blueprints system for defining robot behaviors.

**Problem it solves:** Programming robots typically requires specialized middleware stacks and hardware-specific code. DimOS provides a unified, agent-native operating system layer that lets AI agents control robots through familiar abstractions, bridging the gap between the software agent world and physical automation.

**Why another one?** The "agentive operating system" framing positions DimOS as infrastructure rather than an application framework. By providing OS-level primitives for physical space interaction, it enables the same AI agent patterns used in software development to extend into the physical world — a meaningful step toward embodied AI.

---

## 24. [Mole](https://github.com/tw93/Mole)
> Deep clean and optimize your Mac.

**Language:** Shell  |  **Stars:** 40,075  |  **Forks:** 1,116  |  **Score:** 2,319  |  **Created:** 2025-09-23

**Background:** Mole by Tw93 is a Mac cleaning and optimization tool distributed as a single binary. It combines the functionality of CleanMyMac, AppCleaner, DaisyDisk, and iStat Menus into one lightweight utility. Installable via Homebrew, it has reached 40,000 stars as a go-to Mac maintenance tool.

**Problem it solves:** Mac users typically need multiple paid applications (CleanMyMac for cleaning, AppCleaner for uninstalling, DaisyDisk for disk visualization, iStat Menus for monitoring) to maintain their systems. Mole replaces all of them with a single free, open-source binary.

**Why another one?** The single-binary distribution and Homebrew installation make Mole dramatically simpler to adopt than its commercial alternatives. It covers deep cleaning (caches, logs, browser leftovers), smart uninstalling (including hidden remnants), disk visualization, and live system monitoring — a breadth that no other single open-source tool matches on macOS.

---

## 25. [CLI-Anything](https://github.com/HKUDS/CLI-Anything)
> CLI-Anything: Making ALL Software Agent-Native

**Language:** Python  |  **Stars:** 16,206  |  **Forks:** 1,374  |  **Score:** 2,278  |  **Created:** 2026-03-08

**Background:** CLI-Anything by HKUDS (HKU Data Science Lab) automatically generates command-line interfaces for any software, making it agent-ready. The philosophy is that today's software serves humans, but tomorrow's users will be AI agents — CLI-Anything bridges that gap by wrapping GUI applications in structured CLI interfaces that agents can drive.

**Problem it solves:** AI agents interact with the world through text commands, but most software was built for human GUI interaction. CLI-Anything converts any application into an agent-controllable tool by generating CLI wrappers with JSON output, enabling agents to operate software that was never designed for programmatic access.

**Why another one?** The universal scope ("ALL Software") and the automatic generation approach distinguish it from manual CLI-building tools. With 13 demonstrated applications and 1,588 passing tests, CLI-Anything has shown breadth beyond proof-of-concept. The MIT license and the backing of a university research lab add credibility for production adoption.

---

> **Day's theme:** The agentic ecosystem matures into specialized roles — from CEO-mode planning and swarm intelligence to offline survival computers and physical-world robotics — as the community shifts from building agents to building the infrastructure, workflows, and operating systems that make agents effective specialists.
