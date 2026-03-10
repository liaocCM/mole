# Trendshift Report — 2026-02-27
**Total:** 25 repositories

---

## 1. [awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
> A community collection of OpenClaw use cases for making life easier.

**Language:** —  |  **Stars:** 22,126  |  **Forks:** 1,817  |  **Score:** 11,316  |  **Created:** 2026-02-08

**Background:** This is a community-curated list of real-life use cases for OpenClaw, the personal AI assistant platform. Maintained by Hesam Sheikh, it launched in early February 2026 and amassed over 22,000 stars in under three weeks. The repository explicitly focuses on practical applications rather than skills or plugins, aiming to show non-technical users how OpenClaw can fit into their daily routines.

**Problem it solves:** The biggest barrier to adopting a general-purpose AI assistant is not the software itself but knowing what to do with it. This collection bridges that gap by providing categorized, real-world examples — from automating household inventory to drafting legal correspondence — so users can discover workflows they had not considered.

**Why another one?** While awesome-openclaw-skills catalogs the technical building blocks, this repo targets the demand side: what life problems people are actually solving. The explosive star growth suggests that the OpenClaw ecosystem's bottleneck has shifted from tooling to imagination, and this list fills that gap.

---

## 2. [superpowers](https://github.com/obra/superpowers)
> An agentic skills framework & software development methodology that works.

**Language:** Shell  |  **Stars:** 75,000  |  **Forks:** 5,793  |  **Score:** 7,778  |  **Created:** 2025-10-09

**Background:** Superpowers is a composable set of agent skills and a structured software development workflow created by Jesse Vincent (obra). It installs into coding agents such as Claude Code, Cursor, Codex, and OpenCode via their plugin or skills marketplaces. The methodology enforces a multi-stage process: brainstorm a spec, get user sign-off, produce an implementation plan, then execute through subagent-driven development with two-stage code review per task.

**Problem it solves:** Coding agents left to their defaults tend to skip planning, ignore test-driven development, and drift from the original intent during long sessions. Superpowers installs guard rails — mandatory spec approval, red-green-refactor TDD enforcement, and plan checkpoints — so an agent can work autonomously for hours without derailing.

**Why another one?** Superpowers is not a new coding agent but a methodology layer that works across multiple agents via their plugin systems. Its portability across Claude Code, Cursor, Codex, and OpenCode, combined with subagent delegation rather than single long-running contexts, makes it uniquely positioned as an agent-agnostic workflow standard. At 75,000 stars it continues to trend because new agent releases keep expanding its install base.

---

## 3. [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)
> Bash is all you need — A nano Claude Code-like agent, built from 0 to 1

**Language:** TypeScript  |  **Stars:** 24,497  |  **Forks:** 4,467  |  **Score:** 6,256  |  **Created:** 2025-06-29

**Background:** Learn Claude Code is an educational project by shareAI-lab that builds a minimal Claude Code-like agent from scratch to teach how agentic coding tools work internally. The core loop — send messages to an LLM, check if the response requests tool use, execute tools, loop — is implemented in a few hundred lines. The project supports multiple languages (English, Chinese, Japanese) and has attracted a large Chinese-speaking developer community.

**Problem it solves:** Claude Code and similar agentic tools are powerful but opaque. Developers who want to understand the agent loop, tool-use protocol, and context management patterns have no way to learn from the production codebases since they are complex and partially proprietary. This nano implementation strips the pattern to its essentials, making the architecture accessible.

**Why another one?** The project keeps trending because it fills a specific educational niche: not another agent framework, but a teaching tool. Its concise codebase and multi-language documentation make it the go-to onboarding resource for developers entering the agentic coding space.

---

## 4. [Scrapling](https://github.com/D4Vinci/Scrapling)
> An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

**Language:** Python  |  **Stars:** 26,976  |  **Forks:** 1,985  |  **Score:** 5,561  |  **Created:** 2024-10-13

**Background:** Scrapling is a Python web scraping framework developed by D4Vinci that adapts to website changes automatically. Unlike traditional scraping tools that break when a site redesigns its HTML, Scrapling uses structural matching algorithms to relocate elements even after class names, IDs, or DOM hierarchy change. It supports both static HTML parsing and full browser automation with stealth anti-detection features built in.

**Problem it solves:** Web scraping scripts are notoriously fragile. A single CSS class rename or layout restructure breaks selectors and halts data pipelines. Scrapling's adaptive matching lets scrapers survive site redesigns without manual selector updates, reducing maintenance from hours per week to near zero for most sites.

**Why another one?** The combination of adaptive element matching, integrated stealth browser automation (passing bot detection tests like Cloudflare), and MCP server support for AI agent integration differentiates it from BeautifulSoup, Scrapy, and Playwright-based alternatives. It is designed to be both a standalone framework and a tool that AI agents can invoke directly.

---

## 5. [deer-flow](https://github.com/bytedance/deer-flow)
> An open-source SuperAgent harness that researches, codes, and creates.

**Language:** Python  |  **Stars:** 26,928  |  **Forks:** 3,192  |  **Score:** 5,384  |  **Created:** 2025-05-07

**Background:** DeerFlow is an open-source multi-agent framework from ByteDance, now in version 2.0. It orchestrates research, coding, and content creation tasks by coordinating specialized subagents with tools for web search, code execution in sandboxes, and content generation. The project uses LangGraph for workflow management and supports multiple LLM providers including OpenAI, Anthropic, and local models.

**Problem it solves:** Complex knowledge work — deep research, report generation, data analysis — requires chaining multiple steps that each demand different capabilities. DeerFlow automates these multi-step workflows: a research agent gathers sources, a coding agent processes data, and a writing agent synthesizes the output, all within a single supervised pipeline.

**Why another one?** DeerFlow differentiates through ByteDance's engineering focus on sandboxed execution environments, persistent memory across sessions, and a skills system that lets subagents acquire new capabilities at runtime. The 2.0 rewrite adds interactive report generation with embedded visualizations, positioning it as a research-first alternative to general-purpose agent frameworks.

---

## 6. [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
> GitNexus: The Zero-Server Code Intelligence Engine

**Language:** TypeScript  |  **Stars:** 11,399  |  **Forks:** 1,361  |  **Score:** 5,354  |  **Created:** 2025-08-02

**Background:** GitNexus is a client-side knowledge graph creator built by Abhigyan Patwari that runs entirely in the browser with no server component. Users drop in a GitHub repository URL or a ZIP file, and it generates an interactive knowledge graph of the codebase with a built-in Graph RAG agent for natural language code exploration. All processing happens locally using WebAssembly and IndexedDB.

**Problem it solves:** Understanding an unfamiliar codebase typically requires cloning it, setting up an IDE, and manually tracing call paths. GitNexus eliminates that setup: paste a repo URL and immediately get a visual dependency graph with an AI-powered Q&A interface that can answer questions about architecture, data flow, and module relationships.

**Why another one?** The zero-server architecture is the key differentiator. Unlike cloud-based code intelligence tools (Sourcegraph, CodeSee), GitNexus runs entirely in the browser — no API keys, no data leaving the machine. The Graph RAG approach provides more structurally aware answers than flat-file RAG systems because it traverses the actual dependency graph rather than searching text chunks.

---

## 7. [vinext](https://github.com/cloudflare/vinext)
> Vite plugin that reimplements the Next.js API surface — deploy anywhere

**Language:** TypeScript  |  **Stars:** 6,319  |  **Forks:** 210  |  **Score:** 4,678  |  **Created:** 2026-02-24

**Background:** Vinext is an experimental Vite plugin from Cloudflare that reimplements the Next.js API surface on top of Vite, removing the dependency on the Next.js compiler and runtime. According to Cloudflare's announcement blog post, it was "rebuilt with AI in one week." The project supports the App Router API, server components, server actions, and middleware, all running on standard Vite infrastructure.

**Problem it solves:** Next.js locks developers into its specific build tooling and deployment model. Projects that want Next.js conventions (file-based routing, server components, server actions) but need to deploy on Cloudflare Workers, Deno, or other non-Vercel platforms face significant friction. Vinext decouples the API surface from the runtime.

**Why another one?** The Cloudflare backing gives this project credibility that community alternatives lack. By targeting API compatibility rather than fork-level compatibility, Vinext can be leaner and faster (Vite's build speed) while still letting teams use their existing Next.js knowledge. The three-day-old repo already has 6,300 stars, signaling strong demand for this unbundling.

---

## 8. [skills](https://github.com/anthropics/skills)
> Public repository for Agent Skills

**Language:** Python  |  **Stars:** 88,119  |  **Forks:** 9,339  |  **Score:** 4,510  |  **Created:** 2025-09-22

**Background:** This is Anthropic's official public repository for agent skills, the composable instruction sets that extend Claude Code and other Claude-based agents with domain-specific capabilities. Skills follow the Agent Skills standard (agentskills.io) and can be installed from the Skills Registry. The repo contains both first-party skills authored by Anthropic and serves as a reference implementation for the skills format.

**Problem it solves:** AI coding agents are general-purpose by default but most real work requires domain-specific conventions — a team's code review checklist, a company's deployment procedure, a framework's best practices. Skills package these conventions into installable, version-controlled units that persist across sessions and team members.

**Why another one?** As the official Anthropic repository, this is the canonical source for first-party skills and the reference implementation for the skills standard. It keeps trending because the skills ecosystem is expanding rapidly, and developers monitor this repo for new official releases and format changes.

---

## 9. [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)
> The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry.

**Language:** —  |  **Stars:** 33,181  |  **Forks:** 3,144  |  **Score:** 4,273  |  **Created:** 2026-01-25

**Background:** Maintained by VoltAgent, this repository curates and categorizes over 5,400 skills from the OpenClaw Skills Registry into browsable, searchable categories. It organizes skills by domain (coding, research, writing, data analysis) and provides quality ratings, install counts, and compatibility information. The project launched in late January 2026 and rapidly became the primary discovery interface for the OpenClaw skills ecosystem.

**Problem it solves:** The official OpenClaw Skills Registry is functional but flat — finding the right skill among thousands requires knowing what to search for. This curated list adds editorial categorization, quality filtering, and side-by-side comparisons that the official registry does not provide.

**Why another one?** Every platform ecosystem eventually needs a curated directory alongside its official marketplace. This repo fills the same role that awesome-react or awesome-python fill for their ecosystems: trusted human curation layered on top of a machine-searchable registry.

---

## 10. [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
> A comprehensive collection of Agent Skills for context engineering, multi-agent architectures, and production agent systems.

**Language:** Python  |  **Stars:** 13,664  |  **Forks:** 1,051  |  **Score:** 4,213  |  **Created:** 2025-12-21

**Background:** This repository by Murat Can Koylan provides a collection of agent skills specifically focused on context engineering — the discipline of managing what information an AI agent has access to at each step of a task. The skills cover multi-agent architectures, production agent system debugging, memory management, and context window optimization techniques.

**Problem it solves:** As agent tasks grow more complex, the quality of results depends heavily on what context the agent sees at each decision point. Poor context management leads to hallucinations, repeated work, and incoherent outputs. These skills encode best practices for context window management, retrieval strategies, and inter-agent communication patterns.

**Why another one?** Context engineering is an emerging discipline that most existing skills collections treat as an afterthought. This repo makes it the central focus, providing specialized skills for context budgeting, dynamic retrieval, and multi-agent context sharing — areas that general-purpose skill sets do not cover in depth.

---

## 11. [openclaw](https://github.com/openclaw/openclaw)
> Your own personal AI assistant. Any OS. Any Platform. The lobster way.

**Language:** TypeScript  |  **Stars:** 289,626  |  **Forks:** 54,924  |  **Score:** 4,142  |  **Created:** 2025-11-24

**Background:** OpenClaw is a cross-platform personal AI assistant that runs on any device — desktop, mobile, embedded — and connects to multiple LLM providers. With nearly 290,000 stars, it is one of the most popular open-source AI projects. The project uses a plugin architecture with a skills system, supports voice interaction, and provides native apps for every major platform. Its lobster mascot and "the lobster way" branding have become iconic in the open-source AI community.

**Problem it solves:** Commercial AI assistants (Siri, Google Assistant, Alexa) are locked to their respective ecosystems and send all data to corporate servers. OpenClaw gives users a fully self-hosted alternative with local model support, cross-platform availability, and no data leaving the user's infrastructure.

**Why another one?** OpenClaw keeps trending because it occupies the center of a rapidly growing ecosystem — skills, use cases, studio tools, and community contributions all reference it. Each new satellite project (awesome-openclaw-usecases, awesome-openclaw-skills, openclaw-studio) drives traffic back to the core repo.

---

## 12. [hello-agents](https://github.com/datawhalechina/hello-agents)
> "From Zero to Agents" — A tutorial on building agents from first principles.

**Language:** Python  |  **Stars:** 26,281  |  **Forks:** 2,949  |  **Score:** 4,043  |  **Created:** 2025-09-07

**Background:** Hello-Agents is an educational project by Datawhale China, a well-known Chinese open-source education community. The tutorial walks readers through building AI agents from scratch, covering prompt engineering, tool use, memory systems, multi-agent orchestration, and evaluation. It is written primarily in Chinese with English summaries and targets beginners with no prior agent development experience.

**Problem it solves:** The agent development ecosystem moves faster than documentation can keep up. Most tutorials assume familiarity with LangChain, LlamaIndex, or similar frameworks. Hello-Agents starts from raw API calls and builds up incrementally, so readers understand the fundamentals rather than just framework abstractions.

**Why another one?** Its strength is the Datawhale community's proven model of structured, cohort-based learning. The tutorial is designed to be followed in study groups with exercises and checkpoints, which drives engagement and star growth far beyond what a solo-authored tutorial achieves.

---

## 13. [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
> System prompts, internal tools & AI models of major AI coding tools.

**Language:** —  |  **Stars:** 129,730  |  **Forks:** 33,055  |  **Score:** 3,932  |  **Created:** 2025-03-05

**Background:** This repository collects and publishes the leaked or reverse-engineered system prompts, internal tool definitions, and model configurations of major AI tools including Claude Code, Cursor, Windsurf, Devin, Lovable, Replit, and many others. With nearly 130,000 stars, it has become the definitive reference for understanding how commercial AI products are configured under the hood.

**Problem it solves:** AI tool vendors treat their system prompts as proprietary, making it impossible for users to understand why their tool behaves a certain way or to build competing products. This collection provides transparency, letting developers study prompt engineering techniques used in production and replicate successful patterns.

**Why another one?** It keeps trending because every new AI tool launch generates fresh system prompt leaks, and this repo is the first place they get published. The continuous update cycle and comprehensive coverage (28+ tools) make it a living reference rather than a static snapshot.

---

## 14. [claude-flow](https://github.com/ruvnet/claude-flow)
> The leading agent orchestration platform for Claude.

**Language:** TypeScript  |  **Stars:** 15,205  |  **Forks:** 1,766  |  **Score:** 3,404  |  **Created:** 2025-06-02

**Background:** Claude-flow (now branded as RuFlo v3.5) is an enterprise-grade agent orchestration platform by ruvnet that coordinates multi-agent swarms using Claude as the underlying model. It supports distributed swarm intelligence, RAG integration, and native integration with Claude Code and Codex. The platform provides both a CLI and a web-based orchestration interface for designing and monitoring agent workflows.

**Problem it solves:** Running a single Claude agent is straightforward; coordinating dozens of agents working on different aspects of a complex task is not. Claude-flow provides the scheduling, communication, and state management infrastructure for multi-agent systems — task routing, inter-agent messaging, shared memory, and failure recovery.

**Why another one?** Claude-flow focuses exclusively on Claude-native orchestration rather than being model-agnostic, which allows tighter integration with Claude's specific capabilities (tool use, extended thinking, computer use). The enterprise-grade positioning with audit logging, role-based access, and deployment templates targets production use cases that hobby-tier orchestration tools do not address.

---

## 15. [opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf)
> PDF Parsing for RAG — Convert to Markdown & JSON, Fast, Local, No GPU

**Language:** Java  |  **Stars:** 1,927  |  **Forks:** 133  |  **Score:** 3,238  |  **Created:** 2025-05-13

**Background:** OpenDataLoader PDF is a Java-based PDF parsing library designed specifically for RAG (Retrieval-Augmented Generation) pipelines. It converts PDFs to clean Markdown or structured JSON without requiring a GPU or cloud API. The library handles complex layouts including multi-column text, tables, headers/footers, and embedded images, running entirely on CPU with low memory footprint.

**Problem it solves:** PDF parsing for RAG is deceptively hard. Most tools either require GPU-based vision models (expensive) or produce garbled output from complex layouts (unreliable). OpenDataLoader PDF uses rule-based layout analysis combined with lightweight heuristics to produce structured output that preserves document hierarchy — headings, paragraphs, tables — which is critical for chunk quality in RAG systems.

**Why another one?** The Java implementation is the key differentiator. Most PDF-to-markdown tools are Python-based, which creates friction in Java/JVM enterprise environments where the rest of the data pipeline runs on Spark, Flink, or Spring. OpenDataLoader PDF drops into existing JVM infrastructure without a Python sidecar or microservice boundary.

---

## 16. [agent-browser](https://github.com/vercel-labs/agent-browser)
> Browser automation CLI for AI agents

**Language:** Rust  |  **Stars:** 20,352  |  **Forks:** 1,189  |  **Score:** 2,940  |  **Created:** 2026-01-11

**Background:** Agent-browser is a headless browser automation CLI from Vercel Labs, written in Rust with a Node.js fallback. It provides a fast, programmatic interface for AI agents to navigate websites, extract content, fill forms, and interact with web applications. The Rust implementation prioritizes startup speed and memory efficiency over the Playwright/Puppeteer alternatives that require a full Node.js runtime.

**Problem it solves:** AI agents that need to interact with the web typically shell out to Playwright or Puppeteer, which are slow to start, memory-hungry, and designed for human-driven test automation rather than agent-driven workflows. Agent-browser provides a CLI optimized for the agent use case: fast startup, structured output, and minimal resource footprint.

**Why another one?** The Rust-first architecture delivers sub-second startup times and a single static binary with no runtime dependencies, compared to Playwright's 200MB+ install and multi-second initialization. The CLI interface is designed for tool-use protocols, returning structured JSON rather than requiring programmatic API integration.

---

## 17. [claude-code](https://github.com/anthropics/claude-code)
> Claude Code is an agentic coding tool that lives in your terminal.

**Language:** Shell  |  **Stars:** 75,677  |  **Forks:** 6,100  |  **Score:** 2,711  |  **Created:** 2025-02-22

**Background:** Claude Code is Anthropic's official CLI-based agentic coding tool. It operates directly in the terminal, understanding project context through file reading, search, and git integration. Users interact through natural language commands, and the agent executes tasks including code generation, refactoring, debugging, test writing, and git workflow management. It supports extensibility through the Agent Skills standard.

**Problem it solves:** IDE-integrated AI assistants require context-switching between chat panels and code editors. Claude Code eliminates that friction by operating in the same terminal where developers already run builds, tests, and git commands. It reads the full project context autonomously rather than relying on manual file selection.

**Why another one?** As Anthropic's first-party CLI tool, Claude Code has the tightest integration with Claude's capabilities — extended thinking, tool use, and the skills system all work natively. Its continued trending reflects the growing skills ecosystem (superpowers, everything-claude-code) that builds on top of it.

---

## 18. [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)
> Master programming by recreating your favorite technologies from scratch.

**Language:** Markdown  |  **Stars:** 473,392  |  **Forks:** 44,374  |  **Score:** 2,568  |  **Created:** 2018-05-09

**Background:** Build Your Own X is a curated collection of step-by-step tutorials for recreating popular technologies from scratch — databases, web servers, compilers, operating systems, game engines, and more. Maintained by CodeCrafters since 2018, it has grown to over 473,000 stars, making it one of the most-starred repositories on GitHub. Each entry links to a detailed tutorial that walks through building a working implementation.

**Problem it solves:** Reading documentation and source code teaches how to use a technology, not how it works internally. These tutorials close that gap by guiding developers through building simplified versions of real systems, which builds deep understanding of the underlying principles.

**Why another one?** It keeps trending because new tutorials are continuously added and the format — learn by building — resonates permanently. The repository serves as a canonical entry point for developers who want to move from using tools to understanding them, a need that never goes out of style.

---

## 19. [PageIndex](https://github.com/VectifyAI/PageIndex)
> PageIndex: Document Index for Vectorless, Reasoning-based RAG

**Language:** Python  |  **Stars:** 20,965  |  **Forks:** 1,612  |  **Score:** 2,533  |  **Created:** 2025-04-01

**Background:** PageIndex by VectifyAI is a document indexing system for RAG that eliminates vector embeddings entirely. Instead of chunking documents and computing embeddings, it builds a hierarchical page-level index that preserves document structure — sections, subsections, tables, figures — and uses LLM reasoning to navigate to the relevant pages at query time. The approach is inspired by how humans use a table of contents rather than keyword search.

**Problem it solves:** Vector-based RAG systems lose document structure during chunking, leading to context fragmentation and hallucination when the answer spans multiple sections. PageIndex preserves the full document hierarchy so the retrieval step can locate complete, coherent sections rather than isolated text fragments.

**Why another one?** The vectorless approach is a genuine architectural departure. While most RAG improvements focus on better embeddings or smarter chunking, PageIndex eliminates both entirely. The reasoning-based navigation also adapts to document structure without reindexing when the retrieval model changes, which reduces operational overhead.

---

## 20. [project-based-learning](https://github.com/practical-tutorials/project-based-learning)
> Curated list of project-based tutorials

**Language:** —  |  **Stars:** 260,554  |  **Forks:** 33,929  |  **Score:** 2,359  |  **Created:** 2017-04-12

**Background:** This is a curated list of programming tutorials organized by technology and language, maintained since 2017. It covers web development, mobile, game development, systems programming, machine learning, and more, with each entry linking to a complete project tutorial. At 260,000+ stars, it is one of the most popular educational resources on GitHub.

**Problem it solves:** Learners often struggle to find quality project-based tutorials that match their skill level and technology interest. This list provides a single organized reference, saving hours of searching across blogs, YouTube, and course platforms.

**Why another one?** Perennial popularity. Like build-your-own-x, this repo resurfaces periodically because the need for structured project-based learning is constant. New developers discover it continuously, and its breadth across languages and domains makes it relevant to virtually any programming learner.

---

## 21. [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted)
> A list of Free Software network services and web applications which can be hosted on your own servers

**Language:** —  |  **Stars:** 278,701  |  **Forks:** 12,754  |  **Score:** 2,301  |  **Created:** 2015-06-01

**Background:** Awesome-Selfhosted is the definitive directory of self-hostable open-source software, maintained since 2015. It catalogs hundreds of applications across categories — file storage, communication, project management, media streaming, home automation — with standardized entries listing language, license, and deployment method. At 278,000+ stars it is among the top 10 most-starred repositories on GitHub.

**Problem it solves:** Finding reliable self-hosted alternatives to commercial SaaS products requires extensive research across scattered project pages and forums. This list consolidates discovery into a single, community-vetted resource with consistent formatting and quality standards.

**Why another one?** It keeps trending because self-hosting interest grows with every data breach headline and SaaS price increase. The list is continuously updated with new projects and deprecated entries are removed, maintaining its relevance over a decade of curation.

---

## 22. [opencode](https://github.com/anomalyco/opencode)
> The open source coding agent.

**Language:** TypeScript  |  **Stars:** 118,953  |  **Forks:** 12,190  |  **Score:** 2,148  |  **Created:** 2025-04-30

**Background:** OpenCode is an open-source terminal-based coding agent that supports multiple LLM providers including Anthropic, OpenAI, Google, and local models via Ollama. Created by Anomaly, it provides a Claude Code-like experience with full model flexibility. The agent reads project context, executes commands, edits files, and manages git workflows, all from the terminal. With nearly 119,000 stars, it has become the leading open-source alternative to proprietary coding agents.

**Problem it solves:** Claude Code and Cursor are powerful but vendor-locked — Claude Code requires Anthropic API access, Cursor requires its subscription. OpenCode provides the same agentic coding workflow with any LLM provider, letting developers use whichever model fits their budget, privacy requirements, or performance needs.

**Why another one?** Model flexibility is the core differentiator. OpenCode treats the LLM as a swappable backend rather than a fixed dependency, which means teams can use Claude for complex refactoring, GPT-4 for routine tasks, and local models for sensitive codebases, all within the same tool and workflow.

---

## 23. [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
> The agent harness performance optimization system for Claude Code and beyond.

**Language:** JavaScript  |  **Stars:** 69,024  |  **Forks:** 8,618  |  **Score:** 2,109  |  **Created:** 2026-01-18

**Background:** Everything Claude Code is a comprehensive optimization and extension system by Affaan M. that enhances Claude Code, Codex, OpenCode, Cursor, and other coding agents. It provides skills, instincts (real-time behavioral adjustments), memory persistence across sessions, security hardening, and a research-first development methodology. The project has grown to 69,000 stars in under two months.

**Problem it solves:** Out-of-the-box coding agents lack persistent memory, security awareness, and performance optimization. Everything Claude Code layers these capabilities on top of existing agents — session memory survives restarts, security skills audit code for vulnerabilities during generation, and performance instincts reduce token waste.

**Why another one?** Unlike superpowers which focuses on development methodology, everything-claude-code targets runtime performance and security. The instincts system — real-time behavioral modifications that trigger based on context — is a novel pattern not found in other skills collections. Cross-agent compatibility (Claude Code, Codex, OpenCode, Cursor) extends its reach beyond any single tool.

---

## 24. [ladybird](https://github.com/LadybirdBrowser/ladybird)
> Truly independent web browser

**Language:** C++  |  **Stars:** 61,142  |  **Forks:** 2,852  |  **Score:** 2,073  |  **Created:** 2024-05-30

**Background:** Ladybird is an independent web browser using a novel engine built from scratch, not forked from Blink, Gecko, or WebKit. Originally a component of the SerenityOS hobby project by Andreas Kling, it was spun out as a standalone cross-platform browser project in 2024. The engine implements web standards from the ground up, including its own JavaScript engine (LibJS), layout engine, and networking stack.

**Problem it solves:** Browser engine diversity has collapsed to effectively two engines (Blink and Gecko), creating a monoculture where Google's implementation decisions become de facto web standards. Ladybird provides a genuinely independent implementation that can surface spec ambiguities and challenge assumptions baked into existing engines.

**Why another one?** Ladybird is the only serious from-scratch browser engine effort in over a decade. While it is pre-alpha and not suitable for daily use, its existence as an independent implementation is valuable for web standards health. Periodic trending reflects community support for browser engine diversity as a public good.

---

## 25. [ruvector](https://github.com/ruvnet/ruvector)
> RuVector is a High Performance, Real-Time, Self-Learning, Vector Graph Neural Network, and Database built in Rust.

**Language:** Rust  |  **Stars:** 2,932  |  **Forks:** 311  |  **Score:** 1,965  |  **Created:** 2025-11-19

**Background:** RuVector is a Rust-based vector database and graph neural network system by ruvnet, branded as a "self-learning agentic operating system." It won a CES 2026 Innovation Award and combines vector search, graph database capabilities, and neural network inference into a single runtime. The system targets real-time adaptive applications where the database layer needs to learn from query patterns and adjust its index structures dynamically.

**Problem it solves:** Traditional vector databases are passive storage systems — they index embeddings and return nearest neighbors but do not learn from usage patterns. RuVector integrates graph neural network inference directly into the database layer, allowing the system to refine its representations and routing based on actual query workloads.

**Why another one?** The self-learning aspect is the differentiator. While Pinecone, Weaviate, and Qdrant compete on scale and performance, RuVector competes on adaptability — the system improves its retrieval quality over time without manual reindexing or embedding model updates. The Rust implementation provides the performance baseline needed for real-time inference alongside database operations.

---

> **Day's theme:** The OpenClaw and agent skills ecosystems dominate the chart, with curated catalogs, educational resources, and orchestration tools all competing to become the standard infrastructure for personal AI assistants and autonomous coding agents.
